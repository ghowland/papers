#!/usr/bin/env python3
"""
HOWL MATH-11 Diagrams — beta = pi/4 as L1/L2 Metric Conversion Factor
8 figures covering the staircase paradox, foundation integral, Lp family,
phase space cells, QED decomposition, lattice prediction, cosmic budget,
and Wilson loop lattice artifact.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Arc, Wedge
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

print("MATH-11 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: THE STAIRCASE PARADOX — L1 ON L2
# Type: Geometric Cross-Section (D5.4)
# Shows: A circle with a staircase approximation superimposed.
#        The staircase perimeter is 4d regardless of refinement.
#        The circle perimeter is pi*d. Two metrics, one geometry.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')

# Draw the circle
theta_c = np.linspace(0, 2 * np.pi, 500)
r = 3.0
cx, cy = 5, 5
ax.plot(cx + r * np.cos(theta_c), cy + r * np.sin(theta_c),
        color=CYAN, lw=3, label=r'L2 circumference = $\pi d$ = %.4f' % (2 * np.pi * r))

# Draw the bounding square
sq = r
ax.plot([cx - sq, cx + sq, cx + sq, cx - sq, cx - sq],
        [cy - sq, cy - sq, cy + sq, cy + sq, cy - sq],
        color=DIM, lw=1.5, ls='--', alpha=0.4)

# Draw staircase approximation (N steps per quadrant)
N = 16
stair_x = [cx + r]
stair_y = [cy]
for i in range(4 * N):
    angle = (i + 1) * (2 * np.pi) / (4 * N)
    target_x = cx + r * np.cos(angle)
    target_y = cy + r * np.sin(angle)
    prev_x = stair_x[-1]
    prev_y = stair_y[-1]
    # Move horizontally first, then vertically
    if i % 2 == 0:
        stair_x.append(target_x)
        stair_y.append(prev_y)
        stair_x.append(target_x)
        stair_y.append(target_y)
    else:
        stair_x.append(prev_x)
        stair_y.append(target_y)
        stair_x.append(target_x)
        stair_y.append(target_y)

ax.plot(stair_x, stair_y, color=RED, lw=1.5, alpha=0.7,
        label='L1 staircase = 4d = %.4f' % (4 * 2 * r))

# Perimeter annotations
ax.text(10.5, 8.5, r'L2 (Euclidean) = $\pi d$',
        color=CYAN, fontsize=13, fontweight='bold')
ax.text(10.5, 7.7, '= %.5f' % (2 * np.pi * r),
        color=CYAN, fontsize=12)

ax.text(10.5, 6.5, 'L1 (Manhattan) = 4d',
        color=RED, fontsize=13, fontweight='bold')
ax.text(10.5, 5.7, '= %.5f' % (4 * 2 * r),
        color=RED, fontsize=12)

ax.text(10.5, 4.5, r'Ratio L2/L1 = $\pi/4 = \beta$',
        color=GOLD, fontsize=14, fontweight='bold')
ax.text(10.5, 3.7, '= 0.78540...',
        color=GOLD, fontsize=12)

# Diameter label
ax.annotate('', xy=(cx + r, cy - 0.3), xytext=(cx - r, cy - 0.3),
            arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax.text(cx, cy - 0.8, 'd = %.1f' % (2 * r), color=SILVER,
        fontsize=11, ha='center')

ax.set_xlim(-0.5, 15)
ax.set_ylim(0.5, 10.5)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title(r'The Staircase Paradox: Two Metrics, One Circle, Ratio = $\beta$',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'math11_01_staircase_paradox.png')


# ================================================================
# FIG 2: THE FOUNDATION INTEGRAL — |sin theta| + |cos theta|
# Type: Running/Convergence (D5.1)
# Shows: The integrand shape over [0, 2pi]. Four identical quadrant
#        humps, each integrating to 2, total 8. The curve shape
#        PROVES C_1 = 8 visually.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\theta$ (radians)', r'$|\sin\theta| + |\cos\theta|$')

theta = np.linspace(0, 2 * np.pi, 1000)
integrand = np.abs(np.sin(theta)) + np.abs(np.cos(theta))

ax.fill_between(theta, 0, integrand, color=CYAN, alpha=0.12)
ax.plot(theta, integrand, color=CYAN, lw=2.5)

# Mark quadrant boundaries
for boundary in [np.pi/2, np.pi, 3*np.pi/2]:
    ax.axvline(boundary, color=DIM, lw=1, ls='--', alpha=0.5)

# Label each quadrant area
quadrant_centers = [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]
for i, qc in enumerate(quadrant_centers):
    ax.text(qc, 0.6, '= 2', color=WHITE, fontsize=14,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=CYAN, linewidth=1))

# Peak and trough annotations
ax.axhline(np.sqrt(2), color=GOLD, lw=1, ls=':', alpha=0.5)
ax.text(6.0, np.sqrt(2) + 0.05, r'Peak = $\sqrt{2}$ = %.4f' % np.sqrt(2),
        color=GOLD, fontsize=10)

ax.axhline(1, color=DIM, lw=1, ls=':', alpha=0.4)
ax.text(6.0, 1.05, 'Trough = 1', color=DIM, fontsize=10)

# Total integral result
ax.text(np.pi, 1.85,
        r'$\int_0^{2\pi} (|\sin\theta| + |\cos\theta|)\, d\theta = 4 \times 2 = 8$',
        color=GOLD, fontsize=14, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=2))

# Quadrant labels
ax.text(np.pi/4, -0.15, 'Q1', color=DIM, fontsize=9, ha='center')
ax.text(3*np.pi/4, -0.15, 'Q2', color=DIM, fontsize=9, ha='center')
ax.text(5*np.pi/4, -0.15, 'Q3', color=DIM, fontsize=9, ha='center')
ax.text(7*np.pi/4, -0.15, 'Q4', color=DIM, fontsize=9, ha='center')

# x-axis labels
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'],
                    color=DIM, fontsize=10)

ax.set_xlim(-0.1, 2 * np.pi + 0.3)
ax.set_ylim(-0.3, 2.0)

ax.set_title(r'The Foundation: $C_1 = \int_0^{2\pi}(|\sin\theta|+|\cos\theta|)\,d\theta = 8$',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'math11_02_foundation_integral.png')


# ================================================================
# FIG 3: BETA(p) FAMILY CURVE — L1 THROUGH L2 TO L-INFINITY
# Type: Running/Convergence (D5.1)
# Shows: The smooth monotonic rise of beta(p) from pi/4 at p=1
#        through 1 at p=2 to pi*sqrt(2)/4 at p=infinity.
#        The lattice-to-continuum transition IS the curve shape.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'p (Lp norm parameter)', r'$\beta(p) = 2\pi / C_p$')

# Compute beta(p) numerically
p_values = np.concatenate([
    np.linspace(1.0, 2.0, 200),
    np.linspace(2.0, 10.0, 200),
    np.linspace(10.0, 100.0, 100),
])
beta_values = []
theta_int = np.linspace(0, 2 * np.pi, 10000)

for p in p_values:
    integrand_p = (np.abs(np.sin(theta_int))**p + np.abs(np.cos(theta_int))**p)**(1.0/p)
    C_p = np.trapz(integrand_p, theta_int)
    beta_values.append(2 * np.pi / C_p)

beta_values = np.array(beta_values)

ax.plot(p_values, beta_values, color=CYAN, lw=2.5)

# Key points
beta_1 = np.pi / 4
beta_2 = 1.0
beta_inf = np.pi * np.sqrt(2) / 4

ax.plot(1.0, beta_1, 'o', color=RED, markersize=14, zorder=6)
ax.annotate(r'$\beta(1) = \pi/4$ = %.4f' % beta_1 + '\nLattice / Manhattan',
            xy=(1.0, beta_1), xytext=(3, beta_1 - 0.08),
            color=RED, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.plot(2.0, beta_2, 'o', color=GOLD, markersize=14, zorder=6)
ax.annotate(r'$\beta(2) = 1$' + '\nEuclidean / Free space',
            xy=(2.0, beta_2), xytext=(4, beta_2 + 0.02),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# L-infinity asymptote
ax.axhline(beta_inf, color=GREEN, lw=1.5, ls='--', alpha=0.6)
ax.text(80, beta_inf + 0.008,
        r'$\beta(\infty) = \pi\sqrt{2}/4$ = %.4f' % beta_inf + '  (Chebyshev)',
        color=GREEN, fontsize=10)

# L1 reference line
ax.axhline(beta_1, color=RED, lw=1, ls=':', alpha=0.4)

# Transition region annotation
ax.fill_between([1.0, 2.0], 0.7, 1.15, color=ORANGE, alpha=0.04)
ax.text(1.5, 0.73, 'Lattice ' + r'$\to$' + ' Continuum\ntransition',
        color=ORANGE, fontsize=9, ha='center', style='italic')

ax.set_xlim(0.5, 105)
ax.set_xscale('log')
ax.set_ylim(0.7, 1.15)

ax.set_title(r'The $\beta(p)$ Family: From Lattice to Continuum',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'math11_03_beta_p_family.png')


# ================================================================
# FIG 4: PHASE SPACE CELLS — h vs hbar
# Type: Geometric Cross-Section (D5.4)
# Shows: Two phase space cells side by side. Left: rectangular
#        (L1) with area h. Right: circular (L2) with area h-bar.
#        The conversion factor 8*beta = 2*pi between them is the
#        L1/L2 metric conversion applied to action quanta.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)

# Left: rectangular phase space cell (L1)
ax1.set_facecolor(PAN)
ax1.set_xlim(-1, 7)
ax1.set_ylim(-1, 7)
ax1.set_aspect('equal')

rect = plt.Rectangle((1, 1), 4, 4, facecolor=RED, alpha=0.15,
                       edgecolor=RED, linewidth=2.5)
ax1.add_patch(rect)

ax1.annotate('', xy=(5, 0.5), xytext=(1, 0.5),
             arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax1.text(3, 0.1, r'$\Delta x$', color=SILVER, fontsize=12, ha='center')

ax1.annotate('', xy=(0.5, 5), xytext=(0.5, 1),
             arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax1.text(0.1, 3, r'$\Delta p$', color=SILVER, fontsize=12, ha='center',
         rotation=90)

ax1.text(3, 3, r'Area = $h$', color=RED, fontsize=16,
         ha='center', va='center', fontweight='bold')
ax1.text(3, 2.2, 'L1 cell\n(rectangular)', color=RED, fontsize=11,
         ha='center', va='center')

ax1.set_xticks([])
ax1.set_yticks([])
for spine in ax1.spines.values():
    spine.set_visible(False)

ax1.set_title('L1 Phase Space: Planck cell', color=RED,
              fontsize=14, fontweight='bold', pad=10)

# Right: circular phase space cell (L2)
ax2.set_facecolor(PAN)
ax2.set_xlim(-1, 7)
ax2.set_ylim(-1, 7)
ax2.set_aspect('equal')

circle = Circle((3, 3), 2.0, facecolor=GOLD, alpha=0.15,
                 edgecolor=GOLD, linewidth=2.5)
ax2.add_patch(circle)

ax2.annotate('', xy=(5, 3), xytext=(3, 3),
             arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5))
ax2.text(4.2, 3.4, 'r', color=SILVER, fontsize=12)

ax2.text(3, 3, r'Area = $\hbar$', color=GOLD, fontsize=16,
         ha='center', va='center', fontweight='bold')
ax2.text(3, 2.2, 'L2 cell\n(circular)', color=GOLD, fontsize=11,
         ha='center', va='center')

# Angular coordinate
arc = Arc((3, 3), 3.0, 3.0, angle=0, theta1=0, theta2=60,
          color=CYAN, lw=1.5)
ax2.add_patch(arc)
ax2.text(4.7, 4.0, r'$\Delta\theta$', color=CYAN, fontsize=11)

ax2.set_xticks([])
ax2.set_yticks([])
for spine in ax2.spines.values():
    spine.set_visible(False)

ax2.set_title(r'L2 Phase Space: Dirac cell', color=GOLD,
              fontsize=14, fontweight='bold', pad=10)

# Central conversion annotation
fig.text(0.5, 0.06,
         r'$\hbar = h / (8\beta) = h / (2\pi)$'
         '       Conversion factor: ' + r'$8\beta = 2\pi$'
         '       One L1/L2 conversion per circular period',
         color=WHITE, fontsize=12, ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=2))

save(fig, 'math11_04_phase_space_cells.png')


# ================================================================
# FIG 5: QED A2 DECOMPOSITION — FOUR TERMS BY BETA CONTENT
# Type: Comparison Bar (D5.6)
# Shows: The four pieces of A2 with their signs and magnitudes.
#        The beta-squared terms (pi^2 content) nearly cancel the
#        beta-zero terms. The 87% cancellation is visible as
#        the tiny residual vs the huge individual bars.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Contribution to A' + r'$_2$')

terms = [
    ('197/144\n' + r'($\beta^0$, rational)', 197.0/144.0, SILVER, 0),
    (r'$(1/12)\pi^2$' + '\n' + r'($\beta^2$, angular)', np.pi**2 / 12.0, CYAN, 2),
    (r'$-(1/2)\pi^2 \ln 2$' + '\n' + r'($\beta^2$, angular+log)', -np.pi**2 * np.log(2) / 2.0, RED, 2),
    (r'$(3/4)\zeta(3)$' + '\n' + r'($\beta^0$, number theory)', 3.0/4.0 * 1.2020569, GREEN, 0),
]

x_pos = [0, 1.5, 3.0, 4.5]
for i, (label, value, color, beta_pow) in enumerate(terms):
    ax.bar(x_pos[i], value, width=0.9, color=color, alpha=0.6,
           edgecolor=color, linewidth=2)
    sign = '+' if value > 0 else ''
    ax.text(x_pos[i], value + (0.08 if value > 0 else -0.15),
            '%s%.4f' % (sign, value), color=color, fontsize=11,
            fontweight='bold', ha='center',
            va='bottom' if value > 0 else 'top')

ax.set_xticks(x_pos)
ax.set_xticklabels([t[0] for t in terms], color=WHITE, fontsize=8)

# Zero line
ax.axhline(0, color=DIM, lw=1, alpha=0.5)

# Net result
a2_sum = sum(t[1] for t in terms)
ax.axhline(a2_sum, color=GOLD, lw=2, ls='--')
ax.text(5.5, a2_sum + 0.05,
        'A' + r'$_2$' + ' = %.5f' % a2_sum,
        color=GOLD, fontsize=13, fontweight='bold')

# Cancellation annotation
total_positive = sum(t[1] for t in terms if t[1] > 0)
cancel_pct = (total_positive - abs(a2_sum)) / total_positive * 100
ax.text(2.25, -3.0,
        '%.0f%% cancellation between ' % cancel_pct +
        r'$\beta^2$' + ' and ' + r'$\beta^0$' + ' terms',
        color=ORANGE, fontsize=12, ha='center', style='italic')

# Beta content legend
ax.text(5.5, 1.0, r'$\beta^0$: topology + number theory', color=SILVER,
        fontsize=10)
ax.text(5.5, 0.7, r'$\beta^2$: angular integration (L1/L2)', color=CYAN,
        fontsize=10)

ax.set_xlim(-0.8, 6.5)
ax.set_ylim(-3.8, 1.8)

ax.set_title(r'QED $A_2$ Coefficient: Four Terms, Two $\beta$ Classes, 87% Cancellation',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'math11_05_qed_a2_decomposition.png')


# ================================================================
# FIG 6: LATTICE FACTOR C = 6*BETA VS DATA
# Type: Threshold/Region (D5.3)
# Shows: The predicted value C = 3*pi/2 = 4.712 against the
#        BMW lattice measurement C = 4.7 +/- 0.5. The prediction
#        sits inside the measurement band.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'$C = m_p / \Lambda_{QCD}$')

# Measurement band
c_meas = 4.7
c_unc = 0.5

ax.axhspan(c_meas - c_unc, c_meas + c_unc, color=MAG, alpha=0.10,
           label='BMW 2008: ' + r'$4.7 \pm 0.5$')
ax.axhspan(c_meas - c_unc/2, c_meas + c_unc/2, color=MAG, alpha=0.08)
ax.axhline(c_meas, color=MAG, lw=2, ls='-', alpha=0.6)

# Prediction
c_pred = 3 * np.pi / 2
ax.axhline(c_pred, color=GOLD, lw=2.5, ls='--',
           label=r'Prediction: $6\beta = 3\pi/2$ = %.5f' % c_pred)

# Deviation
ax.text(0.5, c_pred + 0.06,
        r'$6\beta = 3\pi/2 = %.5f$' % c_pred,
        color=GOLD, fontsize=14, fontweight='bold')
ax.text(0.5, c_meas - 0.15,
        r'BMW: $4.7 \pm 0.5$',
        color=MAG, fontsize=12)

deviation = abs(c_pred - c_meas) / c_unc
ax.text(0.5, 3.8,
        r'$|C_{pred} - C_{meas}| / \sigma$ = %.3f' % deviation + r'$\sigma$',
        color=GREEN, fontsize=13, fontweight='bold')

# The 6 decomposition
ax.text(0.5, 3.4,
        r'$6 = ?$  Candidates: 6 flavors, $3q \times 2\chi$, 6 cube faces, $3d \times 2$',
        color=SILVER, fontsize=10, style='italic')

# If confirmed
ax.text(0.5, 5.6,
        r'If $C = 6\beta$: $m_p = 6\beta \times \Lambda_{QCD}$',
        color=GOLD, fontsize=12,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

ax.set_xlim(0, 1)
ax.set_ylim(3.2, 6.0)
ax.set_xticks([])
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper right')

ax.set_title(r'Lattice Factor: $C = m_p / \Lambda_{QCD}$ vs Prediction $6\beta = 3\pi/2$',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'math11_06_lattice_factor.png')


# ================================================================
# FIG 7: COSMIC BUDGET FROM BETA — THREE SEGMENTS
# Type: Comparison Bar (D5.6)
# Shows: The three cosmic fractions (Omega_DM, Omega_b, Omega_Lambda)
#        all derived from beta and integers, matching Planck data.
#        A stacked bar showing the full budget summing to 1.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', '')

# Predicted values
omega_dm_pred = np.pi / 12.0
omega_b_pred = 13.0 / 264.0
omega_l_pred = 1.0 - omega_dm_pred - omega_b_pred

# Measured values
omega_dm_meas = 0.261
omega_b_meas = 0.0490
omega_l_meas = 0.689

# Stacked bar — predicted
bar_width = 0.35
x_pred = 0.3
x_meas = 0.7

# Predicted stack
ax.bar(x_pred, omega_b_pred, width=bar_width, color=CYAN, alpha=0.6,
       edgecolor=CYAN, linewidth=2, label=r'$\Omega_b$')
ax.bar(x_pred, omega_dm_pred, width=bar_width, bottom=omega_b_pred,
       color=PURPLE, alpha=0.6, edgecolor=PURPLE, linewidth=2,
       label=r'$\Omega_{DM}$')
ax.bar(x_pred, omega_l_pred, width=bar_width,
       bottom=omega_b_pred + omega_dm_pred,
       color=ORANGE, alpha=0.6, edgecolor=ORANGE, linewidth=2,
       label=r'$\Omega_\Lambda$')

# Measured stack
ax.bar(x_meas, omega_b_meas, width=bar_width, color=CYAN, alpha=0.3,
       edgecolor=CYAN, linewidth=1.5)
ax.bar(x_meas, omega_dm_meas, width=bar_width, bottom=omega_b_meas,
       color=PURPLE, alpha=0.3, edgecolor=PURPLE, linewidth=1.5)
ax.bar(x_meas, omega_l_meas, width=bar_width,
       bottom=omega_b_meas + omega_dm_meas,
       color=ORANGE, alpha=0.3, edgecolor=ORANGE, linewidth=1.5)

# Labels on predicted
ax.text(x_pred, omega_b_pred / 2,
        r'$\Omega_b = 13/264$' + '\n= %.5f' % omega_b_pred,
        color=WHITE, fontsize=9, ha='center', va='center', fontweight='bold')
ax.text(x_pred, omega_b_pred + omega_dm_pred / 2,
        r'$\Omega_{DM} = \pi/12$' + '\n= %.5f' % omega_dm_pred,
        color=WHITE, fontsize=9, ha='center', va='center', fontweight='bold')
ax.text(x_pred, omega_b_pred + omega_dm_pred + omega_l_pred / 2,
        r'$\Omega_\Lambda = 1 - \pi/12 - 13/264$' + '\n= %.5f' % omega_l_pred,
        color=WHITE, fontsize=9, ha='center', va='center', fontweight='bold')

# Labels on measured
ax.text(x_meas, omega_b_meas / 2,
        '%.4f' % omega_b_meas,
        color=CYAN, fontsize=9, ha='center', va='center')
ax.text(x_meas, omega_b_meas + omega_dm_meas / 2,
        '%.3f' % omega_dm_meas,
        color=PURPLE, fontsize=9, ha='center', va='center')
ax.text(x_meas, omega_b_meas + omega_dm_meas + omega_l_meas / 2,
        '%.3f' % omega_l_meas,
        color=ORANGE, fontsize=9, ha='center', va='center')

# Column labels
ax.text(x_pred, -0.05, 'Predicted\n(from ' + r'$\beta$' + ' + integers)',
        color=GOLD, fontsize=11, ha='center', fontweight='bold')
ax.text(x_meas, -0.05, 'Measured\n(Planck 2018)',
        color=MAG, fontsize=11, ha='center', fontweight='bold')

# Top line at 1.0
ax.axhline(1.0, color=GOLD, lw=1.5, ls='--', alpha=0.5)
ax.text(0.95, 1.02, 'Flat (= 1.000)', color=GOLD, fontsize=10)

# Deviations
ax.text(0.92, 0.85, 'Deviations:', color=SILVER, fontsize=10,
        fontweight='bold')
ax.text(0.92, 0.80, r'$\Omega_{DM}$: 0.4$\sigma$', color=PURPLE, fontsize=10)
ax.text(0.92, 0.75, r'$\Omega_b$: 0.6$\sigma$', color=CYAN, fontsize=10)
ax.text(0.92, 0.70, r'$\Omega_\Lambda$: 0.01$\sigma$', color=ORANGE, fontsize=10)

# Statistical warning
ax.text(0.5, -0.12, 'STATISTICAL CONTROL PENDING: combinatoric p-value not yet computed',
        color=RED, fontsize=10, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED, linewidth=1.5))

ax.set_xlim(0, 1.1)
ax.set_ylim(-0.18, 1.1)
ax.set_xticks([])
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

ax.set_title(r'The Cosmic Budget: Three Fractions from $\beta$ and Integers',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'math11_07_cosmic_budget.png')


# ================================================================
# FIG 8: WILSON LOOP ON LATTICE — THE STAIRCASE ARTIFACT
# Type: Geometric Cross-Section (D5.4)
# Shows: A circular Wilson loop drawn on a square lattice grid.
#        The lattice path follows the staircase. The continuum path
#        follows the circle. The ratio of their lengths is 1/beta.
#        The staircase paradox IS the lattice artifact.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')

# Draw lattice grid
grid_range = np.arange(-5, 6)
for g in grid_range:
    ax.plot([g, g], [-5, 5], color=DIM, lw=0.3, alpha=0.3)
    ax.plot([-5, 5], [g, g], color=DIM, lw=0.3, alpha=0.3)

# Draw continuum circle
theta_wl = np.linspace(0, 2 * np.pi, 500)
R = 3.5
ax.plot(R * np.cos(theta_wl), R * np.sin(theta_wl),
        color=CYAN, lw=3, alpha=0.8)

# Draw lattice staircase approximation of the circle
# Step around the circle, snapping to nearest lattice point
n_steps = 200
stair_x = []
stair_y = []
for i in range(n_steps + 1):
    angle = 2 * np.pi * i / n_steps
    # Snap to nearest lattice point
    cx_snap = round(R * np.cos(angle))
    cy_snap = round(R * np.sin(angle))
    if len(stair_x) == 0 or (cx_snap != stair_x[-1] or cy_snap != stair_y[-1]):
        stair_x.append(cx_snap)
        stair_y.append(cy_snap)
# Close the loop
stair_x.append(stair_x[0])
stair_y.append(stair_y[0])

# Draw staircase edges between consecutive lattice points
for i in range(len(stair_x) - 1):
    x0, y0 = stair_x[i], stair_y[i]
    x1, y1 = stair_x[i+1], stair_y[i+1]
    # Move horizontally then vertically
    ax.plot([x0, x1], [y0, y0], color=RED, lw=2, alpha=0.7)
    ax.plot([x1, x1], [y0, y1], color=RED, lw=2, alpha=0.7)

# Lattice points on the staircase path
for i in range(len(stair_x) - 1):
    ax.plot(stair_x[i], stair_y[i], 's', color=RED, markersize=4, alpha=0.6)

# Annotations
ax.text(4.5, 4.5, r'Continuum: $2\pi R$ (L2)',
        color=CYAN, fontsize=12, fontweight='bold')
ax.text(4.5, 3.8, r'= %.3f' % (2 * np.pi * R),
        color=CYAN, fontsize=11)

ax.text(4.5, 2.8, 'Lattice: staircase (L1)',
        color=RED, fontsize=12, fontweight='bold')

# Compute staircase L1 length
l1_total = 0
for i in range(len(stair_x) - 1):
    l1_total += abs(stair_x[i+1] - stair_x[i]) + abs(stair_y[i+1] - stair_y[i])
ax.text(4.5, 2.1, r'= %d lattice units' % l1_total,
        color=RED, fontsize=11)

ax.text(4.5, 1.0, 'Ratio: L2/L1 ' + r'$\approx \beta = \pi/4$',
        color=GOLD, fontsize=13, fontweight='bold')
ax.text(4.5, 0.3, r'Actual: %.4f' % (2 * np.pi * R / l1_total) +
        r'   $\beta$ = %.4f' % (np.pi/4),
        color=GOLD, fontsize=11)

# Correction annotation
ax.text(-4.5, -4.5,
        'Leading lattice artifact\nfor circular Wilson loops:\n' +
        r'$1/\beta = 4/\pi \approx 1.273$',
        color=ORANGE, fontsize=11,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, linewidth=1.5))

ax.set_xlim(-5.5, 9)
ax.set_ylim(-5.5, 5.5)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title(r'Wilson Loop on a Lattice: The Staircase IS the Artifact, $\beta$ IS the Correction',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'math11_08_wilson_loop_lattice.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  math11_01_staircase_paradox.png")
print("  math11_02_foundation_integral.png")
print("  math11_03_beta_p_family.png")
print("  math11_04_phase_space_cells.png")
print("  math11_05_qed_a2_decomposition.png")
print("  math11_06_lattice_factor.png")
print("  math11_07_cosmic_budget.png")
print("  math11_08_wilson_loop_lattice.png")
print("=" * 50)
