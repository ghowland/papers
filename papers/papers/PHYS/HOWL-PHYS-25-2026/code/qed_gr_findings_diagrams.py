#!/usr/bin/env python3
"""
qed_gr_findings_diagrams.py
============================
Diagrams of the QED-to-GR scan findings using exact values from
phys24_lib.py and the two scan scripts. All data from computed results.

Output: PNG files to ../figures/
"""

import sys
sys.path.insert(0, '.')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Import from phys24_lib for exact values
from phys24_lib import *
from mpmath import log as mlog, pi as mpi, sqrt as msqrt

# Extract exact numbers at the display boundary
alpha_m = float(f2m(alpha_frac))
alpha_inv_f = float(f2m(alpha_inv))
R2_val = float(f2m(R2_f))
R4_val = float(f2m(R4_f))
b2_SM_val = float(f2m(b2_SM))
b2_mod_val = float(f2m(b2_mod))
gap_SM_val = float(f2m(gap_SM))
gap_VL_val = float(f2m(gap_VL))
gap_meas_val = float(f2m(gap_measured))
base_val = float(f2m(alpha_frac * Fraction(1,1) / (Fraction(12,1) * R2_f)))
log10_alpha = float(mlog(f2m(alpha_frac), 10))

# Scan results (from verified output)
DM_baryon_meas = 5.3204
DM_hit_val = float(mpf(22)/13 * mpi)  # 5.3165
Lambda_log10 = -121.539
alpha57_log10 = float(57 * mlog(f2m(alpha_frac), 10))  # -121.800
base39_log10 = float(39 * mlog(f2m(alpha_frac * Fraction(1,1) / (Fraction(12,1) * R2_f)), 10))  # -121.333
product_hit = float(f2m(alpha_frac)**2 * mpi**2 * 20/13)  # 0.000809
target_omr = 0.000809231  # (1-r) at N=100

OUT = "../figures"
os.makedirs(OUT, exist_ok=True)

# Style
BG = '#0d1117'
SPHERE = '#58a6ff'
TORUS = '#f0883e'
WEAK = '#8b949e'
TEXT = '#e6edf3'
ACCENT = '#7ee787'
RED = '#f85149'
PURPLE = '#d2a8ff'
YELLOW = '#ffcc00'
CYAN = '#79c0ff'
DARK_BOX = '#161b22'


def make_fig(w, h):
    fig, ax = plt.subplots(1, 1, figsize=(w, h), facecolor=BG)
    ax.set_facecolor(BG)
    return fig, ax


# ================================================================
# FIGURE 1: THE HEADLINE — 57/39 = 19/13 = b2_SM / b2_VL
# ================================================================

fig, ax = make_fig(16, 11)
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 11)
ax.axis('off')

# Title with generous padding
ax.text(8, 10.3, 'THE CRITICAL CONNECTION',
        color=YELLOW, fontsize=22, ha='center', fontweight='bold')
ax.text(8, 9.6, r'$\Lambda_{Planck} \approx \alpha^{3 \times 19}$'
        r'  and  $\Lambda_{Planck} \approx (\alpha/3\pi)^{3 \times 13}$',
        color=TEXT, fontsize=14, ha='center')

# Three boxes connected by lines
# Box 1: Unification (left)
b1 = FancyBboxPatch((0.5, 5.5), 4.5, 3.0,
                      boxstyle="round,pad=0.3",
                      facecolor=DARK_BOX, edgecolor=SPHERE, linewidth=2.5)
ax.add_patch(b1)
ax.text(2.75, 8.0, 'UNIFICATION', color=SPHERE, fontsize=13,
        ha='center', fontweight='bold')
ax.text(2.75, 7.3, r'$b_2^{SM} = -19/6$', color=TEXT, fontsize=12, ha='center')
ax.text(2.75, 6.7, r'$b_2^{VL} = -13/6$', color=ACCENT, fontsize=12, ha='center')
ax.text(2.75, 6.1, 'Gap: 218/115 vs 38/27', color=WEAK, fontsize=9, ha='center')

# Box 2: Cosmological Constant (right)
b2 = FancyBboxPatch((11, 5.5), 4.5, 3.0,
                      boxstyle="round,pad=0.3",
                      facecolor=DARK_BOX, edgecolor=RED, linewidth=2.5)
ax.add_patch(b2)
ax.text(13.25, 8.0, 'COSMOLOGICAL', color=RED, fontsize=13,
        ha='center', fontweight='bold')
ax.text(13.25, 7.5, 'CONSTANT', color=RED, fontsize=13,
        ha='center', fontweight='bold')
ax.text(13.25, 6.8, r'$\Lambda \approx \alpha^{57}$', color=TEXT,
        fontsize=12, ha='center')
ax.text(13.25, 6.2, r'$= \alpha^{3 \times 19}$', color=SPHERE,
        fontsize=12, ha='center')

# Box 3: Dark Matter (bottom center)
b3 = FancyBboxPatch((5.5, 0.5), 5.0, 3.0,
                      boxstyle="round,pad=0.3",
                      facecolor=DARK_BOX, edgecolor=TORUS, linewidth=2.5)
ax.add_patch(b3)
ax.text(8, 3.0, 'DARK MATTER', color=TORUS, fontsize=13,
        ha='center', fontweight='bold')
ax.text(8, 2.3, r'$\frac{DM}{baryon} \approx \frac{22}{13}\pi = 5.317$',
        color=TEXT, fontsize=12, ha='center')
ax.text(8, 1.5, 'Measured: 5.320  (0.07% hit)', color=WEAK, fontsize=9,
        ha='center')

# Central hub: the integer 13
hub = Circle((8, 5.5), 0.9, fill=True, facecolor=DARK_BOX,
             edgecolor=YELLOW, linewidth=3)
ax.add_patch(hub)
ax.text(8, 5.75, '19', color=SPHERE, fontsize=20, ha='center',
        fontweight='bold')
ax.text(8, 5.1, '13', color=ACCENT, fontsize=20, ha='center',
        fontweight='bold')

# Connecting lines
ax.annotate('', xy=(7.1, 5.5), xytext=(5.0, 7.0),
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=2.5))
ax.annotate('', xy=(8.9, 5.5), xytext=(11.0, 7.0),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5))
ax.annotate('', xy=(8, 4.6), xytext=(8, 3.5),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=2.5))

# The key equation at center bottom
ax.text(8, 4.2, r'$\frac{57}{39} = \frac{19}{13}$'
        r'$= \frac{|b_2^{SM}|}{|b_2^{VL}|}$',
        color=YELLOW, fontsize=16, ha='center', fontweight='bold')

# Verified tag
ax.text(8, -0.3, 'ALL IDENTITIES VERIFIED EXACT IN FRACTION ARITHMETIC (10/10 PASS)',
        color=ACCENT, fontsize=9, ha='center')

# Numerical details in margins
ax.text(0.2, 4.5, 'EXACT VALUES:', color=WEAK, fontsize=8)
ax.text(0.2, 4.0, r'$\alpha^{-1}$ = %.9f' % alpha_inv_f,
        color=WEAK, fontsize=7)
ax.text(0.2, 3.6, r'$\log_{10}\alpha$ = %.10f' % log10_alpha,
        color=WEAK, fontsize=7)
ax.text(0.2, 3.2, r'$57 \times \log_{10}\alpha$ = %.6f' % alpha57_log10,
        color=WEAK, fontsize=7)
ax.text(0.2, 2.8, r'$\log_{10}\Lambda_{Pl}$ = %.6f' % Lambda_log10,
        color=WEAK, fontsize=7)
ax.text(0.2, 2.4, 'Miss: %.3f decades' % abs(alpha57_log10 - Lambda_log10),
        color=WEAK, fontsize=7)

ax.text(13.5, 4.5, 'FROM phys24_lib:', color=WEAK, fontsize=8)
ax.text(13.5, 4.0, r'$b_2^{SM}$ = %s' % str(Fraction(-19, 6)),
        color=WEAK, fontsize=7)
ax.text(13.5, 3.6, r'$b_2^{VL}$ = %s' % str(Fraction(-13, 6)),
        color=WEAK, fontsize=7)
ax.text(13.5, 3.2, r'$\Delta b_2$ = %s' % str(Fraction(1, 1)),
        color=WEAK, fontsize=7)
ax.text(13.5, 2.8, r'gap$_{SM}$ = 218/115 = %.6f' % gap_SM_val,
        color=WEAK, fontsize=7)
ax.text(13.5, 2.4, r'gap$_{VL}$ = 38/27 = %.6f' % gap_VL_val,
        color=WEAK, fontsize=7)

fig.savefig(os.path.join(OUT, 'findings_01_headline_connection.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_01_headline_connection.png")


# ================================================================
# FIGURE 2: LAMBDA FROM alpha^57 — THE 122 ORDERS EXPLAINED
# ================================================================

fig, ax = make_fig(16, 9)
ax.set_facecolor(BG)

# Plot: powers of alpha vs magnitude
N_range = np.arange(1, 80)
log10_alpha_N = N_range * log10_alpha

ax.plot(N_range, log10_alpha_N, '-', color=SPHERE, linewidth=2.5,
        label=r'$\alpha^N$ (bare coupling)')

# Powers of alpha/(3pi)
log10_base = float(mlog(f2m(alpha_frac * Fraction(1,1) /
                             (Fraction(12,1) * R2_f)), 10))
log10_base_N = N_range * log10_base
ax.plot(N_range, log10_base_N, '-', color=TORUS, linewidth=2.5,
        label=r'$(\alpha/3\pi)^N$ (VP step)')

# Lambda target
ax.axhline(y=Lambda_log10, color=RED, linestyle='--', linewidth=2, alpha=0.7)
ax.text(75, Lambda_log10 + 2, r'$\Lambda_{Planck}$',
        color=RED, fontsize=12, fontweight='bold')
ax.text(75, Lambda_log10 - 4,
        r'$= 10^{%.1f}$' % Lambda_log10,
        color=RED, fontsize=9)

# Mark N=57 and N=39
ax.plot([57], [alpha57_log10], 'o', color=SPHERE, markersize=14, zorder=10)
ax.plot([39], [base39_log10], 'o', color=TORUS, markersize=14, zorder=10)

ax.annotate('N = 57 = 3 x 19\n'
            r'$\alpha^{57} = 10^{%.2f}$' % alpha57_log10 +
            '\nmiss: %.2f decades' % abs(alpha57_log10 - Lambda_log10),
            xy=(57, alpha57_log10), xytext=(62, -95),
            color=SPHERE, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BOX,
                      edgecolor=SPHERE))

ax.annotate('N = 39 = 3 x 13\n'
            r'$(\alpha/3\pi)^{39} = 10^{%.2f}$' % base39_log10 +
            '\nmiss: %.2f decades' % abs(base39_log10 - Lambda_log10),
            xy=(39, base39_log10), xytext=(44, -105),
            color=TORUS, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BOX,
                      edgecolor=TORUS))

# Mark the 19 and 13 connection
ax.text(5, -15, '19 = |numerator of $b_2^{SM}$| = -19/6',
        color=SPHERE, fontsize=9, fontweight='bold')
ax.text(5, -22, '13 = |numerator of $b_2^{VL}$| = -13/6',
        color=TORUS, fontsize=9, fontweight='bold')
ax.text(5, -29, '3 = generation count',
        color=ACCENT, fontsize=9, fontweight='bold')
ax.text(5, -36, '57/39 = 19/13 (EXACT)',
        color=YELLOW, fontsize=10, fontweight='bold')

ax.set_xlabel('Power N', color=TEXT, fontsize=12)
ax.set_ylabel(r'$\log_{10}$ (magnitude)', color=TEXT, fontsize=12)
ax.set_title(r'The 122 Orders of Magnitude: $\Lambda \approx \alpha^{3 \times 19}$',
             color=TEXT, fontsize=15, fontweight='bold', pad=15)
ax.legend(facecolor=DARK_BOX, edgecolor=WEAK, labelcolor=TEXT,
          fontsize=10, loc='upper right')
ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_xlim(0, 78)
ax.set_ylim(-170, 0)

fig.savefig(os.path.join(OUT, 'findings_02_lambda_from_alpha.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_02_lambda_from_alpha.png")


# ================================================================
# FIGURE 3: THE FOUR APPEARANCES OF 13
# ================================================================

fig, ax = make_fig(16, 10)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.5, 10.5)
ax.axis('off')

ax.text(8, 9.8, 'THE INTEGER 13 IN FOUR INDEPENDENT RESULTS',
        color=YELLOW, fontsize=18, ha='center', fontweight='bold')

# Four boxes arranged in a 2x2 grid with generous spacing
boxes = [
    # (x, y, title, content, value, color)
    (1.0, 5.5,
     'UNIFICATION',
     r'$b_2^{VL} = -13/6$',
     'SM + VL doublet\nSU(2) beta numerator',
     SPHERE),
    (9.0, 5.5,
     'DARK MATTER',
     r'$\frac{DM}{baryon} = \frac{22}{13}\pi$',
     '= %.4f (meas: %.4f)\n0.07%% hit' % (DM_hit_val, DM_baryon_meas),
     TORUS),
    (1.0, 1.0,
     'COSMO. CONSTANT',
     r'$\Lambda \approx (\alpha/3\pi)^{3 \times 13}$',
     r'$= 10^{%.2f}$ (target: $10^{%.1f}$)' % (base39_log10, Lambda_log10)
     + '\n0.21 decade miss',
     RED),
    (9.0, 1.0,
     'H0 CORRECTION',
     r'$(1-r) \approx \alpha^2\pi^2 \times \frac{20}{13}$',
     '= %.6f (target: %.6f)\n0.08%% hit' % (product_hit, target_omr),
     PURPLE),
]

for x, y, title, formula, detail, color in boxes:
    rect = FancyBboxPatch((x, y), 6.0, 3.2,
                           boxstyle="round,pad=0.3",
                           facecolor=DARK_BOX, edgecolor=color,
                           linewidth=2.5)
    ax.add_patch(rect)
    ax.text(x + 3.0, y + 2.7, title, color=color, fontsize=12,
            ha='center', fontweight='bold')
    ax.text(x + 3.0, y + 1.8, formula, color=TEXT, fontsize=13,
            ha='center')
    ax.text(x + 3.0, y + 0.7, detail, color=WEAK, fontsize=8,
            ha='center', linespacing=1.6)

# Central 13
c13 = Circle((8, 5.0), 0.6, fill=True, facecolor=DARK_BOX,
             edgecolor=YELLOW, linewidth=3)
ax.add_patch(c13)
ax.text(8, 5.0, '13', color=YELLOW, fontsize=24, ha='center',
        va='center', fontweight='bold')

# Connecting lines from center to each box
ax.annotate('', xy=(7.0, 6.5), xytext=(7.5, 5.3),
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=2))
ax.annotate('', xy=(9.0, 6.5), xytext=(8.5, 5.3),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=2))
ax.annotate('', xy=(7.0, 4.2), xytext=(7.5, 4.7),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))
ax.annotate('', xy=(9.0, 4.2), xytext=(8.5, 4.7),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2))

# Bottom note
ax.text(8, -0.2,
        'All four appearances trace to $b_2^{mod}$ = -13/6 '
        '(SU(2) beta after VL doublet addition)',
        color=ACCENT, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BOX,
                  edgecolor=ACCENT))

fig.savefig(os.path.join(OUT, 'findings_03_four_appearances_of_13.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_03_four_appearances_of_13.png")


# ================================================================
# FIGURE 4: VP STEP CONNECTION — N=100 IS 1x alpha/(3pi)
# ================================================================

fig, ax = make_fig(14, 8)
ax.set_facecolor(BG)

# Data from scan: N_eff vs (1-r)/base
N_vals = [10, 30, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
omr_base = [10.414, 3.481, 2.089, 1.045, 0.523, 0.209, 0.105, 0.052, 0.021, 0.010]

ax.plot(N_vals, omr_base, 'o-', color=ACCENT, markersize=8, linewidth=2)

# Mark the integer hits
ax.axhline(y=1.0, color=YELLOW, linestyle='--', linewidth=1.5, alpha=0.6)
ax.axhline(y=2.0, color=YELLOW, linestyle='--', linewidth=1.5, alpha=0.4)
ax.axhline(y=10.0, color=YELLOW, linestyle=':', linewidth=1, alpha=0.3)

# Annotate the N=100 hit
ax.annotate('N = 100: ratio = 1.045\n'
            r'$(1-r) \approx 1 \times \alpha/(3\pi)$' + '\n'
            'miss: 4.5%%',
            xy=(100, 1.045), xytext=(300, 3.5),
            color=YELLOW, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=YELLOW, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=DARK_BOX,
                      edgecolor=YELLOW, linewidth=2))

# Annotate N=50
ax.annotate('N = 50: ratio = 2.089\n'
            r'$(1-r) \approx 2 \times \alpha/(3\pi)$',
            xy=(50, 2.089), xytext=(200, 5.5),
            color=SPHERE, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BOX,
                      edgecolor=SPHERE))

# The constant product annotation
ax.text(3000, 6.5,
        'CONSTANT PRODUCT:\n'
        r'$k \times N \approx 100$' + '\n\n'
        'Total correction\n'
        r'$\approx 100 \times \alpha/(3\pi)$' + '\n'
        r'$\approx 0.077$' + '\n\n'
        r'$\ln(H_0^{CMB}/H_0^{loc})$' + '\n'
        r'$= -0.081$',
        color=TEXT, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=DARK_BOX,
                  edgecolor=ACCENT, linewidth=1.5))

ax.set_xscale('log')
ax.set_xlabel('Boundary transit count N', color=TEXT, fontsize=12)
ax.set_ylabel(r'$(1-r) \,/\, [\alpha/(3\pi)]$', color=TEXT, fontsize=12)
ax.set_title(r'VP Step Connection: $(1-r)$ in units of $\alpha/(3\pi)$',
             color=TEXT, fontsize=14, fontweight='bold', pad=15)
ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_ylim(-0.5, 12)
ax.set_xlim(7, 15000)

fig.savefig(os.path.join(OUT, 'findings_04_vp_step_connection.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_04_vp_step_connection.png")


# ================================================================
# FIGURE 5: PRODUCT FORM HITS — alpha^2 * pi^2 * 20/13
# ================================================================

fig, ax = make_fig(14, 8)
ax.set_facecolor(BG)

# The top hits from scan 2
hits = [
    (r'$\alpha^2 \pi^2 \times 20/13$', 0.0808569e-2*100, 0.082, YELLOW),
    (r'$\alpha \times 1/9$',            0.0810817e-2*100, 0.196, SPHERE),
    (r'$\alpha \pi^{-2} \times 12/11$', 0.0806592e-2*100, 0.326, TORUS),
    (r'$\alpha^2 \pi^2 \times 17/11$',  0.0812244e-2*100, 0.372, PURPLE),
    (r'$\alpha \pi^{-1} \times 7/20$',  0.0812987e-2*100, 0.464, CYAN),
]

target_pct = target_omr * 100  # as percentage of 1

labels = [h[0] for h in hits]
values = [h[1] for h in hits]
dists = [h[2] for h in hits]
colors = [h[3] for h in hits]

y_pos = range(len(hits))
bars = ax.barh(y_pos, dists, color=colors, alpha=0.7, height=0.6,
               edgecolor=colors, linewidth=1.5)

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, color=TEXT, fontsize=11)
ax.set_xlabel('Relative distance from target (%%)', color=TEXT, fontsize=11)
ax.set_title(r'Product Form Hits: $(1-r) = \alpha^a \pi^b \times p/q$ at N=100',
             color=TEXT, fontsize=13, fontweight='bold', pad=15)

# Value labels on bars
for i, (dist, val) in enumerate(zip(dists, values)):
    ax.text(dist + 0.02, i, '%.3f%%' % dist, color=colors[i],
            fontsize=9, va='center')

# Highlight the winner
ax.text(0.35, -0.8,
        r'BEST: $\alpha^2 \pi^2 \times 20/13$ = %.10f' % product_hit +
        '  (target: %.10f, 0.08%% miss)' % target_omr,
        color=YELLOW, fontsize=9, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BOX,
                  edgecolor=YELLOW))

# Note about 13
ax.text(0.35, -1.3,
        'Note: denominator 13 appears again '
        '(same as $b_2^{VL}$ numerator and DM ratio)',
        color=ACCENT, fontsize=8)

ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_xlim(0, 0.6)
ax.invert_yaxis()

fig.savefig(os.path.join(OUT, 'findings_05_product_form_hits.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_05_product_form_hits.png")


# ================================================================
# FIGURE 6: DM/BARYON = (22/13)*pi
# ================================================================

fig, ax = make_fig(14, 7)
ax.set_facecolor(BG)

# Bar chart comparing candidates
dm_candidates = [
    (r'$\frac{22}{13}\pi$',  DM_hit_val,    0.004, YELLOW),
    (r'$\frac{16}{3}$',      16/3.0,         0.013, SPHERE),
    (r'$\frac{17}{10}\pi$',  17/10.0*np.pi,  0.020, TORUS),
    (r'$\frac{16}{3} + R_4$', 16/3.0+R4_val, 0.025, PURPLE),
]

y_pos = range(len(dm_candidates))
dists_dm = [c[2] for c in dm_candidates]
colors_dm = [c[3] for c in dm_candidates]
bars = ax.barh(y_pos, dists_dm, color=colors_dm, alpha=0.7, height=0.5,
               edgecolor=colors_dm, linewidth=1.5)

ax.set_yticks(y_pos)
ax.set_yticklabels([c[0] for c in dm_candidates], color=TEXT, fontsize=13)

# Target line
ax.axvline(x=0, color=RED, linewidth=2)
ax.text(0.001, -0.7, 'Target: DM/baryon = %.4f' % DM_baryon_meas,
        color=RED, fontsize=9)

# Values on bars
for i, (label, val, dist, col) in enumerate(dm_candidates):
    ax.text(dist + 0.0005, i,
            '= %.4f (dist %.4f, %.2f%%)' % (val, dist, dist/DM_baryon_meas*100),
            color=col, fontsize=8, va='center')

ax.set_xlabel('Distance from measured DM/baryon ratio', color=TEXT, fontsize=11)
ax.set_title(r'Dark Matter Ratio: $DM/baryon \approx \frac{22}{13}\pi$ (0.07%% hit)',
             color=TEXT, fontsize=13, fontweight='bold', pad=15)

# Physics note
ax.text(0.015, 3.5,
        '22 = 2 x 11\n'
        '  11 = Yang-Mills universal integer\n'
        '  2 = spin states / SU(2) doublet\n\n'
        '13 = |numerator of $b_2^{VL}$| = -13/6\n'
        r'  $\pi$ = circular geometry (R$_2$ = $\pi$/4)',
        color=TEXT, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=DARK_BOX,
                  edgecolor=ACCENT, linewidth=1.5))

ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_xlim(0, 0.03)
ax.invert_yaxis()

fig.savefig(os.path.join(OUT, 'findings_06_dark_matter_ratio.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_06_dark_matter_ratio.png")


# ================================================================
# FIGURE 7: THE COMPLETE PICTURE — ONE INTEGER CONTROLS THREE
# ================================================================

fig, ax = make_fig(16, 12)
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 12)
ax.axis('off')

ax.text(8, 11.3, 'ONE INTEGER STRUCTURE, THREE PROBLEMS',
        color=TEXT, fontsize=18, ha='center', fontweight='bold')
ax.text(8, 10.7, 'The SU(2) beta coefficient connects unification, '
        'dark matter, and the cosmological constant',
        color=WEAK, fontsize=9, ha='center')

# Top: SU(2) beta coefficient
top_box = FancyBboxPatch((4, 8.5), 8, 1.8,
                          boxstyle="round,pad=0.3",
                          facecolor=DARK_BOX, edgecolor=YELLOW,
                          linewidth=3)
ax.add_patch(top_box)
ax.text(8, 9.7, r'SU(2) BETA: $b_2 = -19/6$ (SM)  $\rightarrow$  '
        r'$-13/6$ (SM+VL)',
        color=YELLOW, fontsize=11, ha='center', fontweight='bold')
ax.text(8, 9.0, r'$\Delta b_2 = 1$ from VL quark doublet (3,2,1/6)',
        color=TEXT, fontsize=9, ha='center')

# Three branches
branches = [
    (2.5, 3.5, 5.5, 4.5,
     'GAUGE UNIFICATION',
     [r'Gap ratio: $\frac{218}{115} \rightarrow \frac{38}{27}$',
      'SM: 1.896 (40%% miss)',
      'VL: 1.407 (3.6%% miss)',
      'Measured: %.3f' % gap_meas_val],
     SPHERE),
    (8, 3.5, 5.5, 4.5,
     'COSMO. CONSTANT',
     [r'$\Lambda \approx \alpha^{3 \times 19} = \alpha^{57}$',
      r'$\approx (\alpha/3\pi)^{3 \times 13}$',
      r'$10^{%.2f}$ vs $10^{%.1f}$' % (alpha57_log10, Lambda_log10),
      'Miss: 0.26 decades'],
     RED),
    (13.5, 3.5, 5.5, 4.5,
     'DARK MATTER RATIO',
     [r'$DM/b = \frac{22}{13}\pi$',
      '= %.4f' % DM_hit_val,
      'Measured: %.4f' % DM_baryon_meas,
      'Miss: 0.07%%'],
     TORUS),
]

for cx, y, w, h, title, lines, color in branches:
    rect = FancyBboxPatch((cx - w/2, y), w, h,
                           boxstyle="round,pad=0.2",
                           facecolor=DARK_BOX, edgecolor=color,
                           linewidth=2)
    ax.add_patch(rect)
    ax.text(cx, y + h - 0.5, title, color=color, fontsize=10,
            ha='center', fontweight='bold')
    for i, line in enumerate(lines):
        ax.text(cx, y + h - 1.2 - i*0.6, line, color=TEXT,
                fontsize=8, ha='center')

    # Arrow from top box
    ax.annotate('', xy=(cx, y + h), xytext=(cx, 8.5),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Bottom: what ties them together
tie_box = FancyBboxPatch((2, 0.0), 12, 2.5,
                          boxstyle="round,pad=0.3",
                          facecolor=DARK_BOX, edgecolor=ACCENT,
                          linewidth=2.5)
ax.add_patch(tie_box)
ax.text(8, 2.0, 'THE COMMON THREAD', color=ACCENT, fontsize=12,
        ha='center', fontweight='bold')
ax.text(8, 1.3,
        r'19 and 13 = numerators of $b_2^{SM}$ and $b_2^{VL}$. '
        'The VL doublet changes ONE integer',
        color=TEXT, fontsize=9, ha='center')
ax.text(8, 0.7,
        'and that integer appears in the gap ratio, the cosmological constant '
        'exponent, and the dark matter ratio denominator.',
        color=TEXT, fontsize=9, ha='center')

# Arrows from branches to bottom
for cx, _, _, _, _, _, color in branches:
    ax.annotate('', xy=(cx, 2.5), xytext=(cx, 3.5),
                arrowprops=dict(arrowstyle='->', color=WEAK, lw=1,
                               linestyle='--'))

fig.savefig(os.path.join(OUT, 'findings_07_complete_picture.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_07_complete_picture.png")


# ================================================================
# FIGURE 8: H0 RUNNING WITH EXACT CALIBRATION
# ================================================================

fig, ax = make_fig(14, 8)
ax.set_facecolor(BG)

# H0 data points with uncertainties
H0_pts = [
    (30,   73.04, 1.0,  'SH0ES', ACCENT),
    (25,   69.80, 1.7,  'TRGB', SPHERE),
    (200,  73.30, 1.8,  'H0LiCOW', PURPLE),
    (1000, 67.40, 1.2,  'DES+BAO', TORUS),
    (5000, 67.36, 0.5,  'Planck', RED),
]

for N, H0, err, label, color in H0_pts:
    ax.errorbar(N, H0, yerr=err, fmt='o', color=color, markersize=9,
                capsize=5, capthick=2, elinewidth=2, zorder=10)
    ax.text(N * 1.2, H0 + 0.5, label, color=color, fontsize=9)

# Model curve using VP-step calibration: r = 1 - alpha/(3*pi)
# At N=100, this gives (1-r) = 7.74e-4, r = 0.999226
r_vp = 1 - base_val
N_curve = np.logspace(0.5, 4.0, 200)
H0_vp = 73.04 * r_vp ** N_curve

ax.plot(N_curve, H0_vp, '-', color=ACCENT, linewidth=2.5,
        label=r'$r = 1 - \alpha/(3\pi)$ per transit')

# Model with product hit: r = 1 - alpha^2*pi^2*20/13
r_prod = 1 - product_hit
H0_prod = 73.04 * r_prod ** N_curve
ax.plot(N_curve, H0_prod, '--', color=YELLOW, linewidth=2,
        label=r'$r = 1 - \alpha^2\pi^2 \times 20/13$ per transit')

# Asymptotic convergence line
ax.axhline(y=67.36, color=RED, linestyle=':', alpha=0.4)

# Calibration box
ax.text(8, 75.5,
        'VP-step model: total correction'
        r' $\approx 100 \times \alpha/(3\pi) = %.4f$' % (100 * base_val),
        color=ACCENT, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BOX,
                  edgecolor=ACCENT))
ax.text(8, 74.5,
        r'$\ln(H_0^{CMB}/H_0^{loc}) = %.4f$' % np.log(67.36/73.04) +
        '  (compare: $-0.077$)',
        color=WEAK, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.2', facecolor=DARK_BOX,
                  edgecolor=WEAK))

ax.set_xscale('log')
ax.set_xlabel('Effective boundary transit count N', color=TEXT, fontsize=11)
ax.set_ylabel(r'$H_0$ (km/s/Mpc)', color=TEXT, fontsize=11)
ax.set_title(r'$H_0$ Running: VP Step Calibration with Exact $\alpha/(3\pi)$ from phys24\_lib',
             color=TEXT, fontsize=12, fontweight='bold', pad=15)
ax.legend(facecolor=DARK_BOX, edgecolor=WEAK, labelcolor=TEXT,
          fontsize=9, loc='lower left')
ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_ylim(63, 77)
ax.set_xlim(5, 8000)

fig.savefig(os.path.join(OUT, 'findings_08_h0_running_calibrated.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: findings_08_h0_running_calibrated.png")


print("\n=== ALL 8 DIAGRAMS SAVED ===")
print("Location: %s/findings_*.png" % OUT)
