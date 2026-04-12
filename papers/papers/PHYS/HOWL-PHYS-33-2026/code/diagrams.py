#!/usr/bin/env python3
"""
HOWL PHYS-33 Diagrams — The Koide Amplitude
8 figures covering the a^2 = 2 conditional.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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


def save(fig, name):
    p = os.path.join(outdir, name)
    fig.savefig(p, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % p)

def style_ax(ax):
    ax.set_facecolor(PAN)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

# ================================================================
# DATA (from phys33_koide_amplitude.py — source of truth)
# ================================================================

m_e = 0.51099895069
m_mu = 105.6583755
m_tau_meas = 1776.86
m_tau_pred = 1776.9690273
m_tau_other = 3.3173565444

sqrt_me = math.sqrt(m_e)
sqrt_mmu = math.sqrt(m_mu)
sqrt_mtau = math.sqrt(m_tau_meas)

K_meas = 0.66666051147
a2_lep = 1.9999630688
a2_down = 2.387725461
a2_up = 3.0927612855

M_scale = (sqrt_me + sqrt_mmu + sqrt_mtau) / 3.0
a_val = math.sqrt(a2_lep)
theta = 2.3166247339

# ================================================================
# FIG 1: K vs a² IDENTITY CURVE WITH THREE SECTORS
# Type: Running
# Shows: The identity K = (1+a²/2)/3 with lep, down, up marked
# ================================================================
print("Fig 1: K vs a² Identity Curve")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE KOIDE IDENTITY — $K = (1 + a^2/2) \,/\, 3$",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

a2 = np.linspace(0, 4, 500)
K_curve = (1 + a2 / 2) / 3

ax.plot(a2, K_curve, color=CYAN, linewidth=2.5, label=r'$K = (1+a^2/2)/3$')

# Mark the three sectors
sectors = [
    (a2_lep, K_meas, 'Leptons\n(e, ' + r'$\mu$, $\tau$)', GREEN, -0.4, 0.03),
    (a2_down, 0.731288, 'Down quarks\n(d, s, b)', ORANGE, 0.3, 0.03),
    (a2_up, 0.848794, 'Up quarks\n(u, c, t)', RED, 0.3, -0.04),
]

for a2v, Kv, label, color, dx, dy in sectors:
    ax.scatter([a2v], [Kv], s=250, color=color, zorder=5,
               edgecolors=WHITE, linewidth=2)
    ax.annotate(label + '\n' + r'$a^2$ = %.3f' % a2v,
                xy=(a2v, Kv), xytext=(a2v + dx, Kv + dy),
                fontsize=10, color=color, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5),
                linespacing=1.3)

# Mark K = 2/3
ax.axhline(y=2.0/3, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(3.5, 2.0/3 + 0.01, 'K = 2/3', fontsize=10, color=GOLD)

# Mark a² = 2
ax.axvline(x=2, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(2.05, 0.38, r'$a^2 = 2$', fontsize=10, color=GOLD)

# Endpoints
ax.scatter([0], [1.0/3], s=100, color=DIM, zorder=5)
ax.text(0.1, 1.0/3 - 0.02, 'All equal\n' + r'$a^2=0$', fontsize=8, color=DIM)

ax.scatter([4], [1.0], s=100, color=DIM, zorder=5)
ax.text(3.6, 1.0 + 0.01, 'One dominates\n' + r'$a^2=4$', fontsize=8, color=DIM)

ax.set_xlabel(r'Amplitude $a^2$', fontsize=12, color=SILVER)
ax.set_ylabel(r'Koide ratio $K$', fontsize=12, color=SILVER)
ax.set_xlim(-0.3, 4.5)
ax.set_ylim(0.25, 1.08)
ax.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys33_01_K_vs_a2.png')

# ================================================================
# FIG 2: KOIDE CIRCLE — MASSES AS 120° PROJECTIONS
# Type: Geometry
# Shows: sqrt(m_k) = M(1 + a*cos(theta + 2pi*k/3)) as circle
# ================================================================
print("Fig 2: Koide Circle")

fig, ax = plt.subplots(figsize=(14, 14), facecolor=BG)
style_ax(ax)
ax.set_aspect('equal')
fig.suptitle(r"THE KOIDE CIRCLE — $\sqrt{m_k}$ as Projections at 120$\degree$",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Draw the unit circle (amplitude = a)
circle_theta = np.linspace(0, 2*np.pi, 200)
circle_x = a_val * np.cos(circle_theta)
circle_y = a_val * np.sin(circle_theta)

ax.plot(circle_x, circle_y, color=DIM, linewidth=1, alpha=0.5)

# Draw the three vectors
colors_k = [GREEN, BLUE, GOLD]
names_k = ['e', r'$\mu$', r'$\tau$']
masses_k = [m_e, m_mu, m_tau_meas]

for k in range(3):
    angle = theta + 2 * np.pi * k / 3
    vx = a_val * np.cos(angle)
    vy = a_val * np.sin(angle)

    # Vector from origin
    ax.annotate('', xy=(vx, vy), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colors_k[k], lw=2.5))

    # Point
    ax.scatter([vx], [vy], s=200, color=colors_k[k], zorder=5,
               edgecolors=WHITE, linewidth=2)

    # Label
    sqrt_m = math.sqrt(masses_k[k])
    offset = 0.15
    ax.text(vx * (1 + offset), vy * (1 + offset),
            '%s\n' % names_k[k] +
            r'$\sqrt{m}$ = %.3f' % sqrt_m + '\n' +
            'cos = %.3f' % np.cos(angle),
            fontsize=10, color=colors_k[k], fontweight='bold',
            ha='center', va='center', linespacing=1.3)

# Center dot
ax.scatter([0], [0], s=100, color=WHITE, zorder=5)
ax.text(0.1, -0.15, 'M = %.2f' % M_scale, fontsize=10, color=SILVER)

# Show the 120° angles
for k in range(3):
    a1 = theta + 2*np.pi*k/3
    a2_a = theta + 2*np.pi*(k+1)/3
    arc_t = np.linspace(a1, a2_a, 50)
    arc_r = 0.35
    ax.plot(arc_r * np.cos(arc_t), arc_r * np.sin(arc_t),
            color=SILVER, linewidth=1, alpha=0.5)

ax.text(0.45, 0.2, r'120$\degree$', fontsize=9, color=SILVER)

# The formula
ax.text(0, -2.0,
        r'$\sqrt{m_k} = M \times (1 + a \cos(\theta + 2\pi k/3))$' +
        '\n' + r'$a = %.5f \approx \sqrt{2}$' % a_val +
        r'      $\theta = %.3f$ rad' % theta,
        fontsize=12, color=WHITE, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM))

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.5, 2.2)
ax.set_xticks([])
ax.set_yticks([])

save(fig, 'phys33_02_koide_circle.png')

# ================================================================
# FIG 3: THE QUADRATIC PARABOLA WITH BOTH ROOTS
# Type: Running
# Shows: x² - 4sx + c = 0 crossing zero at tau and 3.317
# ================================================================
print("Fig 3: Quadratic Parabola")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE QUADRATIC — Two Roots from $K = 2/3$",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

s = sqrt_me + sqrt_mmu
S = m_e + m_mu
c = 3*S - 2*s*s

x = np.linspace(-5, 55, 500)
y = x*x - 4*s*x + c

ax.plot(x, y, color=CYAN, linewidth=2.5)
ax.axhline(y=0, color=DIM, linewidth=1)

# Mark the roots
x_plus = 42.154110444
x_minus = 1.821361179

ax.scatter([x_plus], [0], s=300, color=GOLD, zorder=5,
           edgecolors=WHITE, linewidth=2.5)
ax.annotate(r'$x_+ = \sqrt{m_\tau}$ = %.2f' % x_plus +
            '\n' + r'$m_\tau$ = %.1f MeV' % m_tau_pred,
            xy=(x_plus, 0), xytext=(x_plus - 8, 300),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            linespacing=1.3)

ax.scatter([x_minus], [0], s=200, color=RED, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.annotate(r'$x_-$ = %.2f' % x_minus +
            '\n' + r'$m_-$ = %.2f MeV' % m_tau_other +
            '\n(no known particle)',
            xy=(x_minus, 0), xytext=(x_minus + 3, 400),
            fontsize=10, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            linespacing=1.3)

# Mark the vertex
x_vertex = 2 * s
y_vertex = -4*s*s + c + x_vertex*x_vertex - 4*s*x_vertex
ax.scatter([x_vertex], [c - 4*s*s], s=100, color=DIM, zorder=5)

# Label the equation
ax.text(35, 600,
        r'$x^2 - 4sx + c = 0$' + '\n' +
        r'$s = \sqrt{m_e} + \sqrt{m_\mu}$ = %.2f' % s + '\n' +
        r'$c = 3S - 2s^2$ = %.2f' % c,
        fontsize=11, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM),
        linespacing=1.4)

ax.set_xlabel(r'$x = \sqrt{m_\tau}$ (MeV$^{1/2}$)', fontsize=12, color=SILVER)
ax.set_ylabel(r'$f(x) = x^2 - 4sx + c$', fontsize=12, color=SILVER)
ax.set_xlim(-5, 55)
ax.set_ylim(-500, 800)

save(fig, 'phys33_03_quadratic.png')

# ================================================================
# FIG 4: MASS HIERARCHY ON LOG SCALE
# Type: Scale
# Shows: All masses + prediction + other root on log scale
# ================================================================
print("Fig 4: Mass Hierarchy")

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
style_ax(ax)
fig.suptitle("THE LEPTON MASS HIERARCHY — Measured, Predicted, and Other Root",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

masses_plot = [
    (m_e, r'$m_e$', GREEN, '0.511 MeV', 'measured'),
    (m_tau_other, r'$m_-$', RED, '3.317 MeV', 'other root'),
    (m_mu, r'$m_\mu$', BLUE, '105.66 MeV', 'measured'),
    (m_tau_meas, r'$m_\tau$ (meas)', MAG, '1776.86 MeV', 'measured'),
    (m_tau_pred, r'$m_\tau$ (pred)', GOLD, '1776.97 MeV', 'from K=2/3'),
]

y_base = 0.5
for i, (mass, label, color, val_str, note) in enumerate(masses_plot):
    lm = np.log10(mass)
    ax.scatter([lm], [y_base], s=250, color=color, zorder=5,
               edgecolors=WHITE, linewidth=2)

    y_text = y_base + 0.25 if i % 2 == 0 else y_base - 0.25
    va = 'bottom' if i % 2 == 0 else 'top'
    ax.annotate('%s\n%s\n(%s)' % (label, val_str, note),
                xy=(lm, y_base), xytext=(lm, y_text),
                fontsize=10, color=color, fontweight='bold',
                ha='center', va=va,
                arrowprops=dict(arrowstyle='->', color=color, lw=1),
                linespacing=1.3)

# Bracket: the other root sits between e and mu
ax.annotate('', xy=(np.log10(m_e), y_base - 0.05),
            xytext=(np.log10(m_mu), y_base - 0.05),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1.5))
ax.text((np.log10(m_e) + np.log10(m_mu)) / 2, y_base - 0.12,
        'Other root falls HERE', fontsize=9, color=RED,
        ha='center', style='italic')

ax.set_xlabel(r'$\log_{10}(m$ / MeV)', fontsize=12, color=SILVER)
ax.set_xlim(-0.8, 3.6)
ax.set_ylim(-0.5, 1.2)
ax.set_yticks([])

save(fig, 'phys33_04_mass_hierarchy.png')

# ================================================================
# FIG 5: THE a² RANGE [0,4] WITH MIDPOINT
# Type: Scale
# Shows: Where a²=2 sits — the geometric midpoint
# ================================================================
print("Fig 5: a² Range")

fig, ax = plt.subplots(figsize=(18, 7), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE AMPLITUDE RANGE — $a^2 \in [0, 4]$",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

y_line = 0.5

# Draw the range
ax.plot([0, 4], [y_line, y_line], color=DIM, linewidth=3)

# Endpoints
ax.scatter([0], [y_line], s=200, color=DIM, zorder=5, edgecolors=WHITE, linewidth=2)
ax.text(0, y_line + 0.2, r'$a^2 = 0$' + '\nAll masses equal\nK = 1/3',
        fontsize=10, color=DIM, ha='center', fontweight='bold', va='bottom',
        linespacing=1.3)

ax.scatter([4], [y_line], s=200, color=DIM, zorder=5, edgecolors=WHITE, linewidth=2)
ax.text(4, y_line + 0.2, r'$a^2 = 4$' + '\nOne mass dominates\nK = 1',
        fontsize=10, color=DIM, ha='center', fontweight='bold', va='bottom',
        linespacing=1.3)

# Midpoint
ax.scatter([2], [y_line], s=350, color=GOLD, zorder=6,
           edgecolors=WHITE, linewidth=3)
ax.text(2, y_line - 0.25, r'$a^2 = 2$' + '\n**LEPTONS**\nK = 2/3\nMidpoint of [0,4]',
        fontsize=12, color=GOLD, ha='center', fontweight='bold', va='top',
        linespacing=1.3)

# Quark positions
ax.scatter([a2_down], [y_line], s=200, color=ORANGE, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.text(a2_down, y_line + 0.15, 'Down\nquarks\n%.2f' % a2_down,
        fontsize=9, color=ORANGE, ha='center', va='bottom', linespacing=1.2)

ax.scatter([a2_up], [y_line], s=200, color=RED, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.text(a2_up, y_line + 0.15, 'Up\nquarks\n%.2f' % a2_up,
        fontsize=9, color=RED, ha='center', va='bottom', linespacing=1.2)

# Direction arrow
ax.annotate('', xy=(3.5, y_line - 0.45), xytext=(2.2, y_line - 0.45),
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5))
ax.text(2.85, y_line - 0.5, 'Stronger interaction ' + r'$\rightarrow$' +
        ' larger deviation from 2',
        fontsize=9, color=SILVER, ha='center', style='italic')

ax.set_xlim(-0.5, 4.8)
ax.set_ylim(-0.7, 1.0)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(['0', '1', '2', '3', '4'], fontsize=11, color=SILVER)
ax.set_yticks([])
ax.set_xlabel(r'$a^2$ (dimensionless)', fontsize=12, color=SILVER)

save(fig, 'phys33_05_a2_range.png')

# ================================================================
# FIG 6: ZOOM ON m_tau — PREDICTION INSIDE ERROR BAR
# Type: Threshold
# Shows: The prediction sits inside the measurement uncertainty
# ================================================================
print("Fig 6: m_tau Zoom")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE PREDICTION — $m_\tau$ from $K = 2/3$ vs Measured",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Measured value with error bar
m_tau_unc = 0.12
ax.errorbar([0], [m_tau_meas], yerr=m_tau_unc, fmt='D', color=MAG,
            markersize=15, capsize=10, capthick=2, elinewidth=2,
            markeredgecolor=WHITE, markeredgewidth=2,
            label='Measured: %.2f ' % m_tau_meas + r'$\pm$ %.2f MeV' % m_tau_unc)

# Measurement band
ax.axhspan(m_tau_meas - m_tau_unc, m_tau_meas + m_tau_unc,
           color=MAG, alpha=0.1)

# Predicted value
ax.scatter([1], [m_tau_pred], s=300, color=GOLD, zorder=5,
           edgecolors=WHITE, linewidth=2.5,
           label='Predicted: %.4f MeV' % m_tau_pred)

# Connect them
ax.plot([0, 1], [m_tau_meas, m_tau_pred], color=DIM, linewidth=1,
        linestyle=':')

# Delta annotation
ax.annotate(r'$\Delta$ = %.3f MeV (%.3f%%)' % (m_tau_pred - m_tau_meas,
            abs(m_tau_pred - m_tau_meas) / m_tau_meas * 100),
            xy=(0.5, (m_tau_meas + m_tau_pred) / 2),
            fontsize=13, color=WHITE, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Labels
ax.text(0, m_tau_meas - 0.25, 'Measured', fontsize=11, color=MAG,
        ha='center', fontweight='bold')
ax.text(1, m_tau_pred + 0.15, 'Predicted\n(from K = 2/3)', fontsize=11,
        color=GOLD, ha='center', fontweight='bold', va='bottom')

# Key finding
ax.text(0.5, m_tau_meas + 0.38,
        'Prediction is INSIDE the measurement uncertainty',
        fontsize=12, color=GREEN, ha='center', fontweight='bold')

ax.set_ylabel(r'$m_\tau$ (MeV)', fontsize=12, color=SILVER)
ax.set_xlim(-0.8, 1.8)
ax.set_ylim(m_tau_meas - 0.5, m_tau_meas + 0.5)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Measured', 'Predicted'], fontsize=11, color=SILVER)
ax.legend(fontsize=10, loc='lower right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys33_06_mtau_zoom.png')

# ================================================================
# FIG 7: m_tau vs a² CURVE
# Type: Running
# Shows: How sensitive the prediction is to the exact value of a²
# ================================================================
print("Fig 7: m_tau vs a²")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"SENSITIVITY — $m_\tau$ Prediction vs $a^2$",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# For each a², K = (1+a²/2)/3, then solve for m_tau
a2_scan = np.linspace(1.5, 2.5, 300)
m_tau_scan = []

for a2v in a2_scan:
    Kv = (1 + a2v / 2) / 3
    # sum_m / (sum_sqrt)^2 = Kv
    # (s+x)^2 = sum_m / Kv where sum_m = S + x^2
    # This is: (s+x)^2 = (S+x^2)/Kv
    # Kv*(s+x)^2 = S + x^2
    # Kv*s^2 + 2*Kv*s*x + Kv*x^2 = S + x^2
    # (Kv-1)*x^2 + 2*Kv*s*x + (Kv*s^2 - S) = 0
    s_val = sqrt_me + sqrt_mmu
    S_val = m_e + m_mu
    A_coeff = Kv - 1
    B_coeff = 2 * Kv * s_val
    C_coeff = Kv * s_val * s_val - S_val

    disc = B_coeff * B_coeff - 4 * A_coeff * C_coeff
    if disc >= 0 and A_coeff != 0:
        x_p = (-B_coeff + math.sqrt(disc)) / (2 * A_coeff)
        x_m = (-B_coeff - math.sqrt(disc)) / (2 * A_coeff)
        # Pick the root that gives a mass near 1777
        candidates = []
        for xv in [x_p, x_m]:
            if xv > 0:
                candidates.append(xv * xv)
        if candidates:
            best = min(candidates, key=lambda m: abs(m - 1777))
            m_tau_scan.append(best)
        else:
            m_tau_scan.append(np.nan)
    else:
        m_tau_scan.append(np.nan)

ax.plot(a2_scan, m_tau_scan, color=CYAN, linewidth=2.5)

# Measured band
ax.axhspan(m_tau_meas - m_tau_unc, m_tau_meas + m_tau_unc,
           color=MAG, alpha=0.1)
ax.axhline(y=m_tau_meas, color=MAG, linewidth=2, linestyle='--',
           label=r'Measured $m_\tau$')

# Mark a² = 2
ax.axvline(x=2, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.5)
ax.scatter([2], [m_tau_pred], s=250, color=GOLD, zorder=5,
           edgecolors=WHITE, linewidth=2.5)
ax.annotate(r'$a^2 = 2$: $m_\tau$ = %.1f' % m_tau_pred,
            xy=(2, m_tau_pred), xytext=(2.15, m_tau_pred + 30),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Mark measured a²
ax.scatter([a2_lep], [m_tau_meas], s=200, color=GREEN, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.annotate(r'$a^2_{meas}$ = %.4f' % a2_lep,
            xy=(a2_lep, m_tau_meas), xytext=(1.7, m_tau_meas - 30),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

ax.set_xlabel(r'$a^2$ (dimensionless)', fontsize=12, color=SILVER)
ax.set_ylabel(r'Predicted $m_\tau$ (MeV)', fontsize=12, color=SILVER)
ax.set_xlim(1.5, 2.5)
ax.set_ylim(1650, 1900)
ax.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys33_07_mtau_vs_a2.png')

# ================================================================
# FIG 8: POLAR PLOT — THREE sqrt(m) VECTORS AT 120°
# Type: Geometry
# Shows: The vector magnitudes proportional to sqrt(m)
# ================================================================
print("Fig 8: Polar Vector Plot")

fig, ax = plt.subplots(figsize=(14, 14), facecolor=BG, subplot_kw={'polar': True})
ax.set_facecolor(PAN)
ax.tick_params(colors=DIM, labelsize=8)
ax.spines['polar'].set_color(DIM)
ax.grid(color=DIM, alpha=0.3)

fig.suptitle(r"THREE VECTORS — $\sqrt{m_k}$ at 120$\degree$ Separation",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# The three angles and magnitudes
angles = [theta, theta + 2*np.pi/3, theta + 4*np.pi/3]
magnitudes = [sqrt_me, sqrt_mmu, sqrt_mtau]
colors_p = [GREEN, BLUE, GOLD]
labels_p = [r'$\sqrt{m_e}$ = %.3f' % sqrt_me,
            r'$\sqrt{m_\mu}$ = %.2f' % sqrt_mmu,
            r'$\sqrt{m_\tau}$ = %.2f' % sqrt_mtau]

for k in range(3):
    # Draw vector
    ax.annotate('', xy=(angles[k], magnitudes[k]), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colors_p[k], lw=3))
    # Marker
    ax.scatter([angles[k]], [magnitudes[k]], s=200, color=colors_p[k],
               zorder=5, edgecolors=WHITE, linewidth=2)
    # Label
    ax.text(angles[k], magnitudes[k] + 4, labels_p[k],
            fontsize=11, color=colors_p[k], fontweight='bold',
            ha='center', va='bottom')

# Connect the three points to form a triangle
for k in range(3):
    k_next = (k + 1) % 3
    ax.plot([angles[k], angles[k_next]],
            [magnitudes[k], magnitudes[k_next]],
            color=SILVER, linewidth=1, alpha=0.4, linestyle='--')

# The M circle (all masses equal would be on this circle)
theta_ring = np.linspace(0, 2*np.pi, 200)
ax.plot(theta_ring, [M_scale] * len(theta_ring),
        color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(np.pi/2, M_scale + 2, 'M = %.1f' % M_scale,
        fontsize=9, color=DIM, ha='center')

ax.set_rmax(52)
ax.set_rticks([10, 20, 30, 40, 50])
ax.set_yticklabels(['10', '20', '30', '40', '50'],
                    fontsize=8, color=DIM)

# Bottom text
ax.text(np.pi, -15, 'The tau vector (gold) dominates.\n'
        'The electron vector (green) is nearly at the origin.\n'
        'The triangle connecting them is the Koide geometry.',
        fontsize=10, color=SILVER, ha='center',
        transform=ax.transData)

save(fig, 'phys33_08_polar_vectors.png')

# ================================================================
print()
print("=" * 70)
print("PHYS-33 DIAGRAMS — 8 FIGURES GENERATED")
print("=" * 70)

filenames = [
    'phys33_01_K_vs_a2.png',
    'phys33_02_koide_circle.png',
    'phys33_03_quadratic.png',
    'phys33_04_mass_hierarchy.png',
    'phys33_05_a2_range.png',
    'phys33_06_mtau_zoom.png',
    'phys33_07_mtau_vs_a2.png',
    'phys33_08_polar_vectors.png',
]

for i, name in enumerate(filenames, 1):
    print("  Fig %d: %s" % (i, name))
    