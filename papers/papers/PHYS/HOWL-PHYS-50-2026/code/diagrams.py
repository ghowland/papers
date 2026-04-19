#!/usr/bin/env python3
"""
HOWL PHYS-50 Diagrams — The Dimensional Ratio
8 figures covering filling fraction bars, dimensional ratio sequence,
circle vs sphere visual, Koide vs R3/R2 match, lepton vs boson,
four-loop correction direction, Gamma mechanism, and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge
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

print("PHYS-50 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: FILLING FRACTION BARS R1 THROUGH R7
# Type: Comparison Bar (D5.6)
# Shows: R_n as bars with R3/R2 = 2/3 highlighted between R2 and R3.
#        The ratio between consecutive bars is labeled.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Dimension n', r'Filling fraction $R_n$')

dims = [1, 2, 3, 4, 5, 6, 7]
r_vals = [1.0, 0.7854, 0.5236, 0.3084, 0.1645, 0.0808, 0.0369]
colors_list = [DIM, CYAN, GOLD, DIM, DIM, DIM, DIM]

bars = ax.bar(dims, r_vals, 0.6, color=colors_list, alpha=0.7,
              edgecolor=[c for c in colors_list], linewidth=2)

# Value labels on bars
for d, r, c in zip(dims, r_vals, colors_list):
    ax.text(d, r + 0.02, '%.4f' % r, color=WHITE, fontsize=10,
            ha='center', fontweight='bold')

# Ratio labels between bars
ratios_text = [r'$\pi/4$', r'$\mathbf{2/3}$', r'$3\pi/16$',
               r'$8/5\pi$', r'$5\pi^2/192$', r'$16/7\pi$']
ratios_val = [0.7854, 0.6667, 0.5890, 0.5333, 0.4909, 0.4571]
ratios_color = [DIM, GOLD, DIM, DIM, DIM, DIM]

for i in range(6):
    mid_x = dims[i] + 0.5
    mid_y = max(r_vals[i], r_vals[i + 1]) + 0.08
    ax.annotate('', xy=(dims[i + 1], r_vals[i + 1] + 0.015),
                xytext=(dims[i], r_vals[i] + 0.015),
                arrowprops=dict(arrowstyle='->', color=ratios_color[i],
                                lw=1.5 if i != 1 else 2.5))
    ax.text(mid_x, mid_y, ratios_text[i], color=ratios_color[i],
            fontsize=11 if i != 1 else 14, ha='center',
            fontweight='normal' if i != 1 else 'bold')

# Highlight R3/R2
ax.annotate('THE ONLY\nSIMPLE FRACTION',
            xy=(2.5, 0.7), xytext=(4.5, 0.85),
            color=GOLD, fontsize=12, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.set_xlim(0.3, 7.7)
ax.set_ylim(0, 1.1)
ax.set_xticks(dims)
ax.set_xticklabels(['1D', '2D', '3D', '4D', '5D', '6D', '7D'],
                    color=WHITE, fontsize=10)

ax.set_title(r'Filling Fractions $R_n$: Only $R_3/R_2 = 2/3$ Is Rational',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys50_01_filling_fraction_bars.png')


# ================================================================
# FIG 2: DIMENSIONAL RATIO SEQUENCE — ONLY R3/R2 IS RATIONAL
# Type: Running/Convergence (D5.1)
# Shows: R_{n+1}/R_n as a curve with the value 2/3 highlighted.
#        All other points have error bars to nearest simple fraction.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Transition $n \to n+1$', r'$R_{n+1}/R_n$')

transitions = [1, 2, 3, 4, 5, 6]
ratio_vals = [0.7854, 0.6667, 0.5890, 0.5333, 0.4909, 0.4571]
nearest_pq = [7/9, 2/3, 3/5, 5/9, 1/2, 4/9]
miss_pct = [0.97, 0.0, 1.86, 4.17, 1.86, 2.78]

# Plot all points
for i, (t, r, npq, m) in enumerate(zip(transitions, ratio_vals, nearest_pq, miss_pct)):
    color = GOLD if i == 1 else DIM
    size = 16 if i == 1 else 10
    ax.plot(t, r, 'o', color=color, markersize=size, zorder=5)

    # Miss bar to nearest fraction
    if i != 1:
        ax.plot([t, t], [r, npq], color=RED, lw=1.5, alpha=0.5)
        ax.plot(t, npq, 'x', color=RED, markersize=8)
        ax.text(t + 0.15, (r + npq) / 2, '%.1f%%' % m, color=RED,
                fontsize=8, va='center')

# Connect with line
ax.plot(transitions, ratio_vals, '-', color=SILVER, lw=1, alpha=0.3)

# Highlight the 2/3 point
ax.axhline(2/3, color=GOLD, lw=1.5, ls='--', alpha=0.5)
ax.text(6.3, 2/3 + 0.01, '2/3', color=GOLD, fontsize=14, fontweight='bold')

# Annotation
ax.text(4, 0.75, 'Miss from nearest\nsimple fraction p/q',
        color=RED, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED, linewidth=1))

ax.annotate('EXACT MATCH\n0.000% miss', xy=(2, 2/3),
            xytext=(3.5, 0.72), color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# Labels
labels_tr = [r'$1\to 2$', r'$2\to 3$', r'$3\to 4$',
             r'$4\to 5$', r'$5\to 6$', r'$6\to 7$']
ax.set_xticks(transitions)
ax.set_xticklabels(labels_tr, color=WHITE, fontsize=10)
ax.set_xlim(0.5, 6.8)
ax.set_ylim(0.4, 0.85)

ax.set_title(r'The Dimensional Ladder: Only $R_3/R_2$ Hits a Simple Fraction',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys50_02_dimensional_ratio_sequence.png')


# ================================================================
# FIG 3: CIRCLE IN SQUARE vs SPHERE IN CUBE — VISUAL RATIO
# Type: Geometric Cross-Section (D5.4)
# Shows: Left: circle inscribed in square (R2 = pi/4 = 78.5%).
#        Right: sphere inscribed in cube (R3 = pi/6 = 52.4%).
#        Ratio labeled as 2/3.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.3})
fig.patch.set_facecolor(BG)

for ax in [ax1, ax2]:
    ax.set_facecolor(PAN)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

# Left: circle in square
sq1 = Rectangle((-1, -1), 2, 2, facecolor=CYAN, alpha=0.08,
                 edgecolor=CYAN, linewidth=2)
ax1.add_patch(sq1)
circ1 = Circle((0, 0), 1.0, facecolor=CYAN, alpha=0.2,
                edgecolor=CYAN, linewidth=2.5)
ax1.add_patch(circ1)

ax1.text(0, 0, r'$R_2 = \frac{\pi}{4}$' + '\n= 78.5%', color=WHITE,
         fontsize=16, ha='center', va='center', fontweight='bold')
ax1.text(0, -1.5, '2D: Circle in Square', color=CYAN, fontsize=13,
         ha='center', fontweight='bold')
ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-1.8, 1.8)

# Right: sphere in cube (projected as circle with 3D cues)
sq2 = Rectangle((-1, -1), 2, 2, facecolor=GOLD, alpha=0.08,
                 edgecolor=GOLD, linewidth=2)
ax2.add_patch(sq2)

# Draw cube edges (projected)
offset = 0.3
cube_back = Rectangle((-1 + offset, -1 + offset), 2, 2,
                        facecolor='none', edgecolor=GOLD, linewidth=1,
                        linestyle='--', alpha=0.3)
ax2.add_patch(cube_back)
# Connecting lines
for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
    ax2.plot([dx, dx + offset], [dy, dy + offset],
             color=GOLD, lw=1, ls='--', alpha=0.3)

circ2 = Circle((0, 0), 1.0, facecolor=GOLD, alpha=0.15,
                edgecolor=GOLD, linewidth=2.5)
ax2.add_patch(circ2)

# Shading to suggest 3D sphere
theta_shade = np.linspace(0, 2 * np.pi, 100)
for r_shade in [0.3, 0.6, 0.85]:
    ax2.plot(r_shade * np.cos(theta_shade), r_shade * np.sin(theta_shade),
             color=GOLD, lw=0.5, alpha=0.15)

ax2.text(0, 0, r'$R_3 = \frac{\pi}{6}$' + '\n= 52.4%', color=WHITE,
         fontsize=16, ha='center', va='center', fontweight='bold')
ax2.text(0, -1.5, '3D: Sphere in Cube', color=GOLD, fontsize=13,
         ha='center', fontweight='bold')
ax2.set_xlim(-1.8, 2.1)
ax2.set_ylim(-1.8, 1.8)

# The ratio between them
fig.text(0.5, 0.5, r'$\frac{R_3}{R_2} = \frac{\pi/6}{\pi/4} = \frac{2}{3}$',
         color=GOLD, fontsize=24, fontweight='bold',
         ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                   edgecolor=GOLD, linewidth=2))

fig.suptitle(r'The $\pi$ Cancels: $R_3/R_2 = 2/3$ Exactly',
             color=GOLD, fontsize=16, fontweight='bold', y=0.98)

save(fig, 'phys50_03_circle_vs_sphere.png')


# ================================================================
# FIG 4: KOIDE K vs R3/R2 — THE 9.2 ppm MATCH
# Type: Threshold/Region (D5.3)
# Shows: Two horizontal lines nearly overlapping: R3/R2 = 2/3 and
#        K_lepton = 0.666661. The gap (9.2 ppm) magnified.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'width_ratios': [1, 2], 'wspace': 0.3})
fig.patch.set_facecolor(BG)

# Left: full scale showing both values are indistinguishable
setup_ax(ax1, '', '', 'Value')
ax1.barh(1, 2/3, 0.4, color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=2,
         label=r'$R_3/R_2 = 2/3$')
ax1.barh(0, 0.666661, 0.4, color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=2,
         label=r'$K_{lepton}$')

ax1.set_yticks([0, 1])
ax1.set_yticklabels([r'$K_{lepton}$', r'$R_3/R_2$'], color=WHITE, fontsize=11)
ax1.set_xlim(0, 0.8)
ax1.text(0.35, 0.5, 'Indistinguishable\nat this scale',
         color=WHITE, fontsize=10, ha='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM))
ax1.set_title('Full Scale', color=SILVER, fontsize=12)

# Right: zoomed to show the 9.2 ppm gap
setup_ax(ax2, '', '', '')
r3r2 = 2/3
k_lep = 0.666660511

y_center = (r3r2 + k_lep) / 2
y_range = (r3r2 - k_lep) * 8

ax2.axhline(r3r2, color=GOLD, lw=3, label=r'$R_3/R_2 = 2/3$ (exact)')
ax2.axhline(k_lep, color=CYAN, lw=3, label=r'$K_{lepton} = 0.666661$')

# Tau mass uncertainty band
tau_unc_frac = 67e-6  # 67 ppm
k_unc = r3r2 * tau_unc_frac
ax2.axhspan(k_lep - k_unc, k_lep + k_unc, color=CYAN, alpha=0.08)
ax2.text(0.7, k_lep - k_unc * 0.8, r'$\tau$ mass uncertainty ($\pm$67 ppm)',
         color=CYAN, fontsize=9, ha='center', alpha=0.7)

# Gap annotation
mid_gap = (r3r2 + k_lep) / 2
ax2.annotate('', xy=(0.3, r3r2), xytext=(0.3, k_lep),
             arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax2.text(0.35, mid_gap, '9.2 ppm', color=GOLD, fontsize=14,
         fontweight='bold', va='center')

ax2.set_ylim(y_center - y_range / 2, y_center + y_range / 2)
ax2.set_xlim(0, 1)
ax2.set_xticks([])
ax2.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
           loc='upper right')
ax2.set_title('Zoomed: 9.2 ppm Gap', color=SILVER, fontsize=12)

fig.suptitle(r'$K_{Koide}$ Matches $R_3/R_2$ to 9.2 Parts Per Million',
             color=GOLD, fontsize=15, fontweight='bold', y=0.98)

save(fig, 'phys50_04_koide_vs_r3r2.png')


# ================================================================
# FIG 5: LEPTON vs BOSON IN KOIDE PARAMETER SPACE
# Type: Comparison Bar (D5.6)
# Shows: Two panels: K values and a^2 values for leptons and bosons.
#        Leptons at equator (2/3, 2). Bosons at pole (1/3, 0).
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.3})
fig.patch.set_facecolor(BG)

# Left: K values
setup_ax(ax1, '', '', 'Koide K')

ax1.bar(0.5, 2/3, 0.6, color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=2)
ax1.bar(1.5, 0.336, 0.6, color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=2)

ax1.axhline(2/3, color=GOLD, lw=1, ls='--', alpha=0.4)
ax1.axhline(1/3, color=CYAN, lw=1, ls='--', alpha=0.4)
ax1.axhline(1, color=DIM, lw=0.5, ls=':', alpha=0.3)

ax1.text(0.5, 2/3 + 0.03, '2/3', color=GOLD, fontsize=16,
         ha='center', fontweight='bold')
ax1.text(0.5, 2/3 - 0.06, 'MIDPOINT', color=GOLD, fontsize=9,
         ha='center', style='italic')
ax1.text(1.5, 0.336 + 0.03, r'$\approx$1/3', color=CYAN, fontsize=16,
         ha='center', fontweight='bold')
ax1.text(1.5, 0.336 - 0.06, 'POLE', color=CYAN, fontsize=9,
         ha='center', style='italic')

# Range markers
ax1.text(2.2, 1.0, 'K = 1\n(one mass\ndominates)', color=DIM,
         fontsize=8, va='center')
ax1.text(2.2, 1/3, 'K = 1/3\n(equal masses)', color=DIM,
         fontsize=8, va='center')

ax1.set_xticks([0.5, 1.5])
ax1.set_xticklabels(['Leptons', 'Bosons'], color=WHITE, fontsize=12)
ax1.set_ylim(0, 1.15)
ax1.set_xlim(-0.2, 2.5)
ax1.set_title('Koide Ratio K', color=SILVER, fontsize=13)

# Right: a^2 values
setup_ax(ax2, '', '', r'Amplitude $a^2$')

ax2.bar(0.5, 2.0, 0.6, color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=2)
ax2.bar(1.5, 0.018, 0.6, color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=2)

ax2.axhline(2.0, color=GOLD, lw=1, ls='--', alpha=0.4)

ax2.text(0.5, 2.15, r'$a^2 = 2$', color=GOLD, fontsize=16,
         ha='center', fontweight='bold')
ax2.text(0.5, 1.7, 'CRITICAL\nAMPLITUDE', color=GOLD, fontsize=9,
         ha='center', style='italic')
ax2.text(1.5, 0.15, r'$a^2 \approx 0$', color=CYAN, fontsize=14,
         ha='center', fontweight='bold')
ax2.text(1.5, -0.25, 'NO SPREAD', color=CYAN, fontsize=9,
         ha='center', style='italic')

ax2.set_xticks([0.5, 1.5])
ax2.set_xticklabels(['Leptons', 'Bosons'], color=WHITE, fontsize=12)
ax2.set_ylim(-0.4, 2.8)
ax2.set_xlim(-0.2, 2.2)
ax2.set_title(r'Amplitude $a^2$', color=SILVER, fontsize=13)

fig.suptitle('Leptons at the Equator, Bosons at the Pole',
             color=GOLD, fontsize=15, fontweight='bold', y=0.98)

save(fig, 'phys50_05_lepton_vs_boson.png')


# ================================================================
# FIG 6: FOUR-LOOP CORRECTION DIRECTION — TOWARD 2/3
# Type: Running/Convergence (D5.1)
# Shows: K before and after four-loop correction, with 2/3 as target.
#        Arrow showing direction TOWARD.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Koide K')

# The three values
k_before = 0.666660511
k_after = 0.666660548
k_target = 2/3

# Scale: show the relevant range
y_center = (k_target + k_before) / 2
y_range = (k_target - k_before) * 5

# Target line
ax.axhline(k_target, color=GOLD, lw=3, ls='-', label=r'$R_3/R_2 = 2/3$ (exact)')

# Before point
ax.plot(1, k_before, 'o', color=CYAN, markersize=16, zorder=5)
ax.text(1.15, k_before, 'Before: K = 0.666660511\n(miss 9.233 ppm)',
        color=CYAN, fontsize=10, va='center')

# After point
ax.plot(2, k_after, 'o', color=GREEN, markersize=16, zorder=5)
ax.text(2.15, k_after, 'After: K = 0.666660548\n(miss 9.178 ppm)',
        color=GREEN, fontsize=10, va='center')

# Arrow showing direction
ax.annotate('', xy=(2, k_after), xytext=(1, k_before),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5))

# Direction label
ax.text(1.5, k_before - (k_target - k_before) * 0.3,
        r'$\Delta K = +0.054$ ppm' + '\nTOWARD 2/3',
        color=GREEN, fontsize=14, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN, linewidth=1.5))

# Remaining gap
ax.annotate('', xy=(2.5, k_target), xytext=(2.5, k_after),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.5))
ax.text(2.65, (k_target + k_after) / 2, 'Remaining:\n9.178 ppm',
        color=GOLD, fontsize=10, va='center')

# Mass corrections annotation
ax.text(0.5, k_target + (k_target - k_before) * 1.5,
        'Four-loop mass corrections:\n'
        r'$e$: $3.0 \times 10^{-14}$' + '\n'
        r'$\mu$: $1.3 \times 10^{-9}$' + '\n'
        r'$\tau$: $3.6 \times 10^{-7}$',
        color=SILVER, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, linewidth=1))

ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)
ax.set_xlim(0, 3.5)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Pole masses', 'After 4-loop\ncorrection'],
                    color=WHITE, fontsize=10)

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='lower right')

ax.set_title('The Four-Loop Correction Moves K Toward 2/3',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys50_06_four_loop_direction.png')


# ================================================================
# FIG 7: THE GAMMA FUNCTION MECHANISM
# Type: Scale/Landscape (D5.2)
# Shows: Why pi cancels at n=2->3 and not elsewhere.
#        Visual: pi powers in R_n and Gamma contributions.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Table layout
rows = [
    ('n=2', r'$\pi^1$', r'$\Gamma(2) = 1$', r'$\pi/4$', r'$\pi^1$', ''),
    ('n=3', r'$\pi^{3/2}$', r'$\Gamma(5/2) = \frac{3\sqrt{\pi}}{4}$',
     r'$\pi/6$', r'$\pi^1$', r'$\sqrt{\pi}$ cancels!'),
    ('n=4', r'$\pi^2$', r'$\Gamma(3) = 2$', r'$\pi^2/32$', r'$\pi^2$', ''),
    ('n=5', r'$\pi^{5/2}$', r'$\Gamma(7/2) = \frac{15\sqrt{\pi}}{8}$',
     r'$\pi^2/120$', r'$\pi^2$', r'$\sqrt{\pi}$ cancels but $\pi$ remains'),
]

headers = ['Dim', r'$\pi$ in numerator', r'$\Gamma(n/2+1)$',
           r'$R_n$ simplified', r'Net $\pi$ power', 'Cancellation']
col_x = [0.02, 0.10, 0.28, 0.52, 0.68, 0.80]
y_head = 0.88

for i, h in enumerate(headers):
    ax.text(col_x[i], y_head, h, color=DIM, fontsize=10, fontweight='bold',
            transform=ax.transAxes)

ax.plot([0.02, 0.98], [y_head - 0.02, y_head - 0.02],
        color=DIM, lw=0.5, transform=ax.transAxes, clip_on=False)

row_colors = [CYAN, GOLD, DIM, DIM]
for j, (dim, pi_num, gamma, rn, net_pi, cancel) in enumerate(rows):
    y = 0.78 - j * 0.14
    color = row_colors[j]
    weight = 'bold' if j == 1 else 'normal'

    ax.text(col_x[0], y, dim, color=color, fontsize=12,
            fontweight=weight, transform=ax.transAxes)
    ax.text(col_x[1], y, pi_num, color=color, fontsize=12,
            fontweight=weight, transform=ax.transAxes)
    ax.text(col_x[2], y, gamma, color=color, fontsize=11,
            fontweight=weight, transform=ax.transAxes)
    ax.text(col_x[3], y, rn, color=color, fontsize=12,
            fontweight=weight, transform=ax.transAxes)
    ax.text(col_x[4], y, net_pi, color=color, fontsize=12,
            fontweight=weight, transform=ax.transAxes)
    ax.text(col_x[5], y, cancel, color=GREEN if 'cancels!' in cancel else ORANGE,
            fontsize=10, fontweight=weight, transform=ax.transAxes)

# The key insight box
ax.text(0.5, 0.22,
        r'$R_3/R_2 = \frac{\pi^1 / 6}{\pi^1 / 4} = \frac{4}{6} = \frac{2}{3}$'
        + '\n\n' + r'Same $\pi^1$ power in both $\to$ $\pi$ cancels completely',
        color=GOLD, fontsize=14, fontweight='bold', ha='center',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=2))

ax.text(0.5, 0.08,
        r'$R_5/R_4 = \frac{\pi^2 / 120}{\pi^2 / 32} = \frac{32}{120} = \frac{8}{5\pi}$   $\leftarrow$ $\pi$ survives!',
        color=ORANGE, fontsize=11, ha='center',
        transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title(r'Why $\pi$ Cancels Only at $2D \to 3D$: The $\Gamma$ Function Mechanism',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys50_07_gamma_mechanism.png')


# ================================================================
# FIG 8: IDENTITY CARD — R3/R2 = K_KOIDE = 2/3
# Type: Identity Card (D5.8)
# Shows: Summary card with all key numbers and the finding.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Title
ax.text(0.02, 0.95, r'THE DIMENSIONAL RATIO: $K_{Koide} = R_3/R_2 = 2/3$',
        color=GOLD, fontsize=18, fontweight='bold', transform=ax.transAxes)

# Left column: The identity
ax.text(0.02, 0.87, 'THE IDENTITY', color=CYAN, fontsize=13,
        fontweight='bold', transform=ax.transAxes)

id_lines = [
    (r'$R_2 = \pi/4 = 0.7854$', 'Circle fills 78.5% of bounding square'),
    (r'$R_3 = \pi/6 = 0.5236$', 'Sphere fills 52.4% of bounding cube'),
    (r'$R_3/R_2 = 2/3$ (exact)', r'$\pi$ cancels: $(\pi/6)/(\pi/4) = 4/6 = 2/3$'),
    ('Unique in sequence', 'Only simple fraction in R_{n+1}/R_n for n=1..7'),
]

for i, (left, right) in enumerate(id_lines):
    y = 0.81 - i * 0.05
    ax.text(0.04, y, left, color=WHITE, fontsize=11, transform=ax.transAxes)
    ax.text(0.35, y, right, color=SILVER, fontsize=9, transform=ax.transAxes)

# Middle: The match
ax.text(0.02, 0.58, 'THE MATCH', color=GOLD, fontsize=13,
        fontweight='bold', transform=ax.transAxes)

match_lines = [
    (r'$K_{lepton}$', '0.666660511', '9.2 ppm from 2/3'),
    (r'$a^2$', '1.99996', '18.5 ppm from 2'),
    (r'$\tau$ mass unc.', r'$\pm$67 ppm', 'Miss within uncertainty'),
    ('4-loop shift', '+0.054 ppm', 'TOWARD 2/3'),
]

for i, (key, val, note) in enumerate(match_lines):
    y = 0.52 - i * 0.05
    ax.text(0.04, y, key, color=GOLD, fontsize=10,
            fontweight='bold', transform=ax.transAxes)
    ax.text(0.22, y, val, color=WHITE, fontsize=10, transform=ax.transAxes)
    ax.text(0.42, y, note, color=SILVER, fontsize=9, transform=ax.transAxes)

# Right column: The dichotomy
ax.text(0.60, 0.87, 'LEPTON vs BOSON', color=PURPLE, fontsize=13,
        fontweight='bold', transform=ax.transAxes)

dichot_lines = [
    ('', 'Leptons', 'Bosons'),
    ('K', '2/3 (midpoint)', '1/3 (pole)'),
    (r'$a^2$', '2 (critical)', '0.018 (trivial)'),
    ('Range', r'3477$\times$', r'1.56$\times$'),
    ('Mechanism', 'Yukawa', 'Higgs'),
]

colors_d = [PURPLE, GOLD, CYAN]
for i, (key, lep, bos) in enumerate(dichot_lines):
    y = 0.81 - i * 0.05
    weight = 'bold' if i == 0 else 'normal'
    ax.text(0.62, y, key, color=DIM, fontsize=10, transform=ax.transAxes)
    ax.text(0.74, y, lep, color=GOLD, fontsize=10,
            fontweight=weight, transform=ax.transAxes)
    ax.text(0.88, y, bos, color=CYAN, fontsize=10,
            fontweight=weight, transform=ax.transAxes)

# Negative result
ax.text(0.60, 0.55, 'NEGATIVE RESULT', color=RED, fontsize=13,
        fontweight='bold', transform=ax.transAxes)

neg_lines = [
    ('Elliptic Koide (cn at k=0.984):', ''),
    (r'$\langle cn^2 \rangle$ = 0.310 $\neq$ 0.500', ''),
    (r'$a^2$ = 3.226 $\neq$ 2', ''),
    ('Koide is circular (k=0), NOT toroidal', ''),
]

for i, (text, _) in enumerate(neg_lines):
    y = 0.49 - i * 0.04
    ax.text(0.62, y, text, color=RED, fontsize=9, transform=ax.transAxes)

# Bottom: the eight formulations
ax.text(0.02, 0.28, 'EIGHT EQUIVALENT FORMULATIONS OF K = 2/3',
        color=WHITE, fontsize=12, fontweight='bold', transform=ax.transAxes)

forms = [
    '1. Koide ratio K = 2/3',
    r'2. Amplitude $a^2 = 2$',
    '3. CV = 1',
    r'4. Var = mean$^2$',
    '5. Midpoint of [1/3, 1]',
    '6. Critical amplitude',
    '7. Equipartition',
    r'8. $R_3/R_2 = (\pi/6)/(\pi/4)$ — NEW',
]

for i, f in enumerate(forms):
    col = i // 4
    row = i % 4
    x = 0.04 + col * 0.45
    y = 0.22 - row * 0.04
    color = GOLD if i == 7 else SILVER
    weight = 'bold' if i == 7 else 'normal'
    ax.text(x, y, f, color=color, fontsize=10, fontweight=weight,
            transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

save(fig, 'phys50_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys50_01_filling_fraction_bars.png")
print("  phys50_02_dimensional_ratio_sequence.png")
print("  phys50_03_circle_vs_sphere.png")
print("  phys50_04_koide_vs_r3r2.png")
print("  phys50_05_lepton_vs_boson.png")
print("  phys50_06_four_loop_direction.png")
print("  phys50_07_gamma_mechanism.png")
print("  phys50_08_identity_card.png")
print("=" * 50)
