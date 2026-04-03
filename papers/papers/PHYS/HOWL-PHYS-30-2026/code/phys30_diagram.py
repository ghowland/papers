#!/usr/bin/env python3
"""
HOWL PHYS-30 Diagrams — alpha_s from Unification
8 figures covering the strong coupling prediction.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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
# DATA (from phys30_alpha_s.py output — source of truth)
# ================================================================

# Couplings at M_Z
inv_a1_MZ = 63.210
inv_a2_MZ = 31.685
inv_a3_MZ_meas = 8.475   # 1/0.1180

# CD betas
b1_CD = 25.0 / 6    # 4.1667
b2_CD = -13.0 / 6   # -2.1667
b3_CD = -20.0 / 3   # -6.6667

# SM betas
b1_SM = 41.0 / 10   # 4.1
b2_SM = -19.0 / 6   # -3.1667
b3_SM = -7.0         # -7.0

# The six scenarios
scenarios = [
    ("1-loop, no thresh",       0.10769, 8.74,  False),
    ("1-loop, M_VL=500",        0.10367, 12.15, False),
    ("2-loop SM b_ij, no thresh", 0.11753, 0.40, True),
    ("2-loop SM b_ij, M_VL=500", 0.11140, 5.60, False),
    ("2-loop full b_ij, no thresh", 0.11838, 0.33, True),
    ("2-loop full b_ij, M_VL=500", 0.11211, 4.99, False),
]

alpha_s_meas = 0.1180
alpha_s_1sig_lo = 0.1171
alpha_s_1sig_hi = 0.1189
alpha_s_3sig_lo = 0.1153
alpha_s_3sig_hi = 0.1207

# ================================================================
# FIG 1: THREE COUPLINGS RUNNING WITH PREDICTION PATH
# Type: Running/Convergence
# Shows: The full prediction method — run up, cross, run back
# ================================================================
print("Fig 1: Three Couplings with Prediction Path")

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE $\alpha_s$ PREDICTION — Run Up, Cross, Run Back",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Energy range: log10(E/GeV) from ~2 (M_Z) to ~15.5 (M_GUT)
log_MZ = np.log10(91.2)
log_MVL = np.log10(500)
log_MGUT = 15.43

# Running with CD betas (no threshold): 1/a_i(E) = 1/a_i(MZ) - b_i * L
# L = ln(E/M_Z) / (2*pi)
log_E = np.linspace(log_MZ, 16.5, 500)
E_GeV = 10**log_E
L = np.log(E_GeV / 91.2) / (2 * np.pi)

inv_a1 = inv_a1_MZ - b1_CD * L
inv_a2 = inv_a2_MZ - b2_CD * L
inv_a3_meas = inv_a3_MZ_meas - b3_CD * L

# Crossing point
L_cross_val = (inv_a1_MZ - inv_a2_MZ) / (b1_CD - b2_CD)
inv_aGUT = inv_a1_MZ - b1_CD * L_cross_val

# Predicted alpha_3: starts at alpha_GUT, runs DOWN
inv_a3_pred = inv_aGUT + b3_CD * (L_cross_val - L)

ax.plot(log_E, inv_a1, color=BLUE, linewidth=2.5, label=r'$1/\alpha_1$ (U(1))')
ax.plot(log_E, inv_a2, color=GREEN, linewidth=2.5, label=r'$1/\alpha_2$ (SU(2))')
ax.plot(log_E, inv_a3_meas, color=RED, linewidth=2.5, label=r'$1/\alpha_3$ (measured)')
ax.plot(log_E, inv_a3_pred, color=GOLD, linewidth=2.5, linestyle='--',
        label=r'$1/\alpha_3$ (predicted)')

# Mark the crossing
log_E_cross = log_MZ + L_cross_val * 2 * np.pi / np.log(10)
ax.scatter([log_E_cross], [inv_aGUT], s=200, color=WHITE, zorder=5,
           edgecolors=GOLD, linewidth=2.5)
ax.annotate(r'$M_{GUT}$: crossing' + '\n' + r'$1/\alpha_{GUT}$ = %.1f' % inv_aGUT,
            xy=(log_E_cross, inv_aGUT),
            xytext=(log_E_cross - 2.5, inv_aGUT + 6),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Mark M_Z
ax.axvline(x=log_MZ, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(log_MZ + 0.15, 62, r'$M_Z$', fontsize=10, color=DIM)

# Mark the miss at M_Z
inv_a3_pred_MZ = inv_aGUT + b3_CD * L_cross_val  # value at M_Z
ax.annotate('',
            xy=(log_MZ + 0.3, inv_a3_MZ_meas),
            xytext=(log_MZ + 0.3, inv_a3_pred_MZ),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(log_MZ + 0.6, (inv_a3_MZ_meas + inv_a3_pred_MZ) / 2,
        r'$\Delta = 1.17$' + '\n' + r'$\alpha_s$ miss',
        fontsize=10, color=ORANGE, fontweight='bold', va='center')

# Big arrow showing the prediction path
ax.annotate('RUN UP',
            xy=(8, 50), fontsize=11, color=WHITE, fontweight='bold',
            ha='center', alpha=0.6)
ax.annotate('',
            xy=(12, 47), xytext=(4, 53),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5, alpha=0.3))

ax.annotate('RUN BACK',
            xy=(8, 20), fontsize=11, color=GOLD, fontweight='bold',
            ha='center', alpha=0.6)
ax.annotate('',
            xy=(4, 15), xytext=(12, 38),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.3))

ax.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=12, color=SILVER)
ax.set_ylabel(r'Inverse coupling $1/\alpha_i$', fontsize=12, color=SILVER)
ax.set_xlim(log_MZ - 0.5, 17)
ax.set_ylim(-2, 72)
ax.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys30_01_prediction_path.png')

# ================================================================
# FIG 2: ENERGY LANDSCAPE — SM vs CD
# Type: Scale/Landscape
# Shows: Full log-scale view of SM (miss) vs CD (converge)
# ================================================================
print("Fig 2: Energy Landscape SM vs CD")

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
style_ax(ax)
fig.suptitle("ENERGY LANDSCAPE — SM Running vs CD Running",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

log_E = np.linspace(log_MZ, 17, 500)
E_GeV = 10**log_E
L = np.log(E_GeV / 91.2) / (2 * np.pi)

# SM running (solid)
inv_a1_sm = inv_a1_MZ - b1_SM * L
inv_a2_sm = inv_a2_MZ - b2_SM * L
inv_a3_sm = inv_a3_MZ_meas - b3_SM * L

# CD running (dashed)
inv_a1_cd = inv_a1_MZ - b1_CD * L
inv_a2_cd = inv_a2_MZ - b2_CD * L
inv_a3_cd = inv_a3_MZ_meas - b3_CD * L

ax.plot(log_E, inv_a1_sm, color=BLUE, linewidth=2, alpha=0.5, label=r'SM $1/\alpha_1$')
ax.plot(log_E, inv_a2_sm, color=GREEN, linewidth=2, alpha=0.5, label=r'SM $1/\alpha_2$')
ax.plot(log_E, inv_a3_sm, color=RED, linewidth=2, alpha=0.5, label=r'SM $1/\alpha_3$')

ax.plot(log_E, inv_a1_cd, color=BLUE, linewidth=2.5, linestyle='--',
        label=r'CD $1/\alpha_1$')
ax.plot(log_E, inv_a2_cd, color=GREEN, linewidth=2.5, linestyle='--',
        label=r'CD $1/\alpha_2$')
ax.plot(log_E, inv_a3_cd, color=RED, linewidth=2.5, linestyle='--',
        label=r'CD $1/\alpha_3$')

# SM non-convergence region
# Find where SM alpha_1 and alpha_2 would cross
L_sm_cross = (inv_a1_MZ - inv_a2_MZ) / (b1_SM - b2_SM)
log_E_sm_cross = log_MZ + L_sm_cross * 2 * np.pi / np.log(10)
inv_aGUT_sm = inv_a1_MZ - b1_SM * L_sm_cross
inv_a3_sm_at_cross = inv_a3_MZ_meas - b3_SM * L_sm_cross
delta_sm = inv_a3_sm_at_cross - inv_aGUT_sm

ax.scatter([log_E_sm_cross], [inv_aGUT_sm], s=150, color=RED, zorder=5,
           marker='x', linewidths=3)
ax.text(log_E_sm_cross + 0.3, inv_aGUT_sm + 2.5,
        'SM crossing\n' + r'$\Delta$ = %.1f' % delta_sm + '\n(40% miss)',
        fontsize=9, color=RED, fontweight='bold')

# CD convergence
ax.scatter([log_E_cross], [inv_aGUT], s=200, color=GREEN, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.text(log_E_cross - 3, inv_aGUT - 5,
        'CD crossing\n' + r'$\Delta$ = $-$1.17' + '\n(3.6% gap ratio miss)',
        fontsize=9, color=GREEN, fontweight='bold')

# Landmarks
for lx, label in [(log_MZ, r'$M_Z$'), (log_MVL, r'$M_{VL}$'),
                   (log_E_cross, r'$M_{GUT}^{CD}$')]:
    ax.axvline(x=lx, color=DIM, linewidth=0.7, linestyle=':', alpha=0.4)
    ax.text(lx, -3, label, fontsize=9, color=SILVER, ha='center')

ax.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=12, color=SILVER)
ax.set_ylabel(r'Inverse coupling $1/\alpha_i$', fontsize=12, color=SILVER)
ax.set_xlim(log_MZ - 0.5, 17)
ax.set_ylim(-6, 72)
ax.legend(fontsize=9, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, ncol=2)

save(fig, 'phys30_02_energy_landscape.png')

# ================================================================
# FIG 3: DELTA PROPAGATION — M_GUT MISS TO M_Z MISS
# Type: Running/Convergence
# Shows: How Delta = -1.17 at M_GUT becomes 12% alpha_s miss at M_Z
# ================================================================
print("Fig 3: Delta Propagation")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10), facecolor=BG,
                                 gridspec_kw={'width_ratios': [2, 1], 'wspace': 0.35})
for a in [ax1, ax2]:
    style_ax(a)

fig.suptitle(r"DELTA PROPAGATION — $M_{GUT}$ Miss Becomes $M_Z$ Miss",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Left: 1/alpha_3 running — predicted vs measured
log_E = np.linspace(log_MZ, 16, 400)
E_GeV = 10**log_E
L = np.log(E_GeV / 91.2) / (2 * np.pi)

inv_a3_m = inv_a3_MZ_meas - b3_CD * L
inv_a3_p_vals = inv_aGUT + b3_CD * (L_cross_val - L)

ax1.plot(log_E, inv_a3_m, color=RED, linewidth=2.5,
         label=r'$1/\alpha_3$ (measured $\alpha_s$)')
ax1.plot(log_E, inv_a3_p_vals, color=GOLD, linewidth=2.5, linestyle='--',
         label=r'$1/\alpha_3$ (predicted from unification)')

# Fill the gap between them
ax1.fill_between(log_E, inv_a3_m, inv_a3_p_vals, alpha=0.08, color=ORANGE)

# Mark Delta at M_GUT
ax1.annotate('',
             xy=(log_E_cross, inv_a3_m[np.argmin(np.abs(log_E - log_E_cross))]),
             xytext=(log_E_cross, inv_aGUT),
             arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2.5))
ax1.text(log_E_cross + 0.4, inv_aGUT - 1,
         r'$\Delta = -1.17$' + '\nat ' + r'$M_{GUT}$',
         fontsize=12, color=ORANGE, fontweight='bold')

# Mark miss at M_Z
inv_a3_pred_at_MZ = inv_aGUT + b3_CD * L_cross_val
ax1.annotate('',
             xy=(log_MZ + 0.2, inv_a3_MZ_meas),
             xytext=(log_MZ + 0.2, inv_a3_pred_at_MZ),
             arrowprops=dict(arrowstyle='<->', color=CYAN, lw=2.5))
ax1.text(log_MZ + 0.5, (inv_a3_MZ_meas + inv_a3_pred_at_MZ) / 2,
         r'+1.17 in $1/\alpha_3$' + '\n' + r'$\Rightarrow$ 12% in $\alpha_s$',
         fontsize=11, color=CYAN, fontweight='bold', va='center')

ax1.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=12, color=SILVER)
ax1.set_ylabel(r'$1/\alpha_3$', fontsize=12, color=SILVER)
ax1.set_xlim(log_MZ - 0.5, 16.5)
ax1.set_ylim(5, 50)
ax1.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE)
ax1.set_title(r'$1/\alpha_3$ Running: Predicted vs Measured', fontsize=12,
              color=WHITE, pad=15)

# Right: the translation — Delta vs alpha_s miss
deltas = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.17, 1.5, 2.0]
alpha_s_miss_pct = []
for d in deltas:
    inv_a3_pred_d = inv_a3_MZ_meas + d
    as_pred_d = 1.0 / inv_a3_pred_d
    miss_d = abs(as_pred_d - alpha_s_meas) / alpha_s_meas * 100
    alpha_s_miss_pct.append(miss_d)

ax2.plot(deltas, alpha_s_miss_pct, color=ORANGE, linewidth=2.5, marker='o',
         markersize=6, markeredgecolor=WHITE, markeredgewidth=1.5)

# Mark the actual Delta
ax2.scatter([1.17], [12.15], s=250, color=RED, zorder=5,
            edgecolors=WHITE, linewidth=2)
ax2.annotate(r'$\Delta$ = 1.17' + '\nmiss = 12.1%',
             xy=(1.17, 12.15),
             xytext=(1.5, 15),
             fontsize=10, color=RED, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# Mark the two-loop residual
ax2.scatter([0.40], [4.5], s=200, color=CYAN, zorder=5,
            edgecolors=WHITE, linewidth=2)
ax2.annotate(r'2-loop $\Delta$ ~ 0.4' + '\nmiss ~ 4.5%',
             xy=(0.40, 4.5),
             xytext=(0.7, 8),
             fontsize=10, color=CYAN, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax2.set_xlabel(r'$\Delta(1/\alpha_3)$ at $M_Z$', fontsize=12, color=SILVER)
ax2.set_ylabel(r'$\alpha_s$ miss (%)', fontsize=12, color=SILVER)
ax2.set_xlim(-0.1, 2.2)
ax2.set_ylim(-1, 22)
ax2.set_title(r'$\Delta$ $\rightarrow$ $\alpha_s$ Miss Translation',
              fontsize=12, color=WHITE, pad=15)

save(fig, 'phys30_03_delta_propagation.png')

# ================================================================
# FIG 4: THRESHOLD vs NO-THRESHOLD
# Type: Threshold/Region
# Shows: Why no-threshold gives better predictions
# ================================================================
print("Fig 4: Threshold vs No-Threshold")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10), facecolor=BG,
                                 gridspec_kw={'wspace': 0.3})
for a in [ax1, ax2]:
    style_ax(a)

fig.suptitle("THRESHOLD vs NO-THRESHOLD — Why Full-Range Running Wins",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Left panel: No threshold — CD betas from M_Z
ax1.set_title('NO THRESHOLD\nCD betas from ' + r'$M_Z$', fontsize=13,
              color=GREEN, fontweight='bold', pad=15)

log_E = np.linspace(log_MZ, 16, 400)
L = np.log(10**log_E / 91.2) / (2 * np.pi)

# All CD running
inv_a1_nt = inv_a1_MZ - b1_CD * L
inv_a2_nt = inv_a2_MZ - b2_CD * L
inv_a3_nt = inv_a3_MZ_meas - b3_CD * L

ax1.plot(log_E, inv_a1_nt, color=BLUE, linewidth=2)
ax1.plot(log_E, inv_a2_nt, color=GREEN, linewidth=2)
ax1.plot(log_E, inv_a3_nt, color=RED, linewidth=2)

# Shade full CD running range
ax1.axvspan(log_MZ, 16, color=GREEN, alpha=0.03)
ax1.text(8, 5, 'FULL CD RUNNING', fontsize=14, color=GREEN,
         ha='center', alpha=0.4, fontweight='bold')

ax1.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=11, color=SILVER)
ax1.set_ylabel(r'$1/\alpha_i$', fontsize=11, color=SILVER)
ax1.set_xlim(log_MZ - 0.3, 16.2)
ax1.set_ylim(-2, 68)

# Right panel: With threshold — SM below M_VL, CD above
ax2.set_title('THRESHOLD AT ' + r'$M_{VL}$ = 500 GeV' + '\nSM below, CD above',
              fontsize=13, color=ORANGE, fontweight='bold', pad=15)

# SM running from M_Z to M_VL
log_E_lo = np.linspace(log_MZ, log_MVL, 100)
L_lo = np.log(10**log_E_lo / 91.2) / (2 * np.pi)

inv_a1_lo = inv_a1_MZ - b1_SM * L_lo
inv_a2_lo = inv_a2_MZ - b2_SM * L_lo
inv_a3_lo = inv_a3_MZ_meas - b3_SM * L_lo

# Values at M_VL
L_VL = np.log(500 / 91.2) / (2 * np.pi)
inv_a1_atVL = inv_a1_MZ - b1_SM * L_VL
inv_a2_atVL = inv_a2_MZ - b2_SM * L_VL
inv_a3_atVL = inv_a3_MZ_meas - b3_SM * L_VL

# CD running from M_VL upward
log_E_hi = np.linspace(log_MVL, 16, 300)
L_hi = np.log(10**log_E_hi / 500) / (2 * np.pi)

inv_a1_hi = inv_a1_atVL - b1_CD * L_hi
inv_a2_hi = inv_a2_atVL - b2_CD * L_hi
inv_a3_hi = inv_a3_atVL - b3_CD * L_hi

ax2.plot(log_E_lo, inv_a1_lo, color=BLUE, linewidth=2)
ax2.plot(log_E_lo, inv_a2_lo, color=GREEN, linewidth=2)
ax2.plot(log_E_lo, inv_a3_lo, color=RED, linewidth=2)

ax2.plot(log_E_hi, inv_a1_hi, color=BLUE, linewidth=2, linestyle='--')
ax2.plot(log_E_hi, inv_a2_hi, color=GREEN, linewidth=2, linestyle='--')
ax2.plot(log_E_hi, inv_a3_hi, color=RED, linewidth=2, linestyle='--')

# Shade regions
ax2.axvspan(log_MZ, log_MVL, color=RED, alpha=0.04)
ax2.axvspan(log_MVL, 16, color=GREEN, alpha=0.03)
ax2.axvline(x=log_MVL, color=ORANGE, linewidth=2, linestyle='-')
ax2.text((log_MZ + log_MVL) / 2, 5, 'SM', fontsize=14, color=RED,
         ha='center', alpha=0.4, fontweight='bold')
ax2.text(10, 5, 'CD', fontsize=14, color=GREEN,
         ha='center', alpha=0.4, fontweight='bold')
ax2.text(log_MVL, 66, r'$M_{VL}$', fontsize=11, color=ORANGE,
         ha='center', fontweight='bold')

ax2.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=11, color=SILVER)
ax2.set_xlim(log_MZ - 0.3, 16.2)
ax2.set_ylim(-2, 68)

# Result annotations at bottom
ax1.text(8, -7, r'$\alpha_s$ = 0.1077  (miss 8.7%, 1-loop)',
         fontsize=11, color=GREEN, ha='center', fontweight='bold',
         transform=ax1.get_xaxis_transform(), clip_on=False)
ax2.text(8, -7, r'$\alpha_s$ = 0.1037  (miss 12.1%, 1-loop)',
         fontsize=11, color=ORANGE, ha='center', fontweight='bold',
         transform=ax2.get_xaxis_transform(), clip_on=False)

save(fig, 'phys30_04_threshold_comparison.png')

# ================================================================
# FIG 5: INTEGER CONNECTION MAP
# Type: Connection/Integer Map
# Shows: 13, 20, 25 → alpha_s prediction
# ================================================================
print("Fig 5: Integer Connection Map")

fig = plt.figure(figsize=(18, 12), facecolor=BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.90])
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

fig.suptitle(r"THE INTEGERS IN THE $\alpha_s$ PREDICTION",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

def rbox(ax, x, y, w, h, text, color, fontsize=11, subtext=None, stc=None):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.5",
        facecolor='#0f0f1a', edgecolor=color, linewidth=2))
    if subtext:
        ax.text(x + w/2, y + h/2 + 1.5, text, fontsize=fontsize,
                fontweight='bold', color=color, ha='center', va='center')
        ax.text(x + w/2, y + h/2 - 1.5, subtext, fontsize=9,
                color=stc or SILVER, ha='center', va='center')
    else:
        ax.text(x + w/2, y + h/2, text, fontsize=fontsize,
                fontweight='bold', color=color, ha='center', va='center')

def arrow(ax, x1, y1, x2, y2, color=SILVER, lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# Source: The representation
rbox(ax, 35, 58, 30, 8, '(3, 2, 1/6)', GOLD, 16,
     'Cabibbo Doublet', SILVER)

# Dynkin coefficients
rbox(ax, 5, 43, 18, 8, r'$\Delta b_1 = 1/15$', BLUE, 12, 'U(1)', BLUE)
rbox(ax, 30, 43, 18, 8, r'$\Delta b_2 = 1$', GREEN, 12, 'SU(2)', GREEN)
rbox(ax, 55, 43, 18, 8, r'$\Delta b_3 = 1/3$', RED, 12, 'SU(3)', RED)

arrow(ax, 42, 58, 14, 51, GOLD, 2)
arrow(ax, 50, 58, 39, 51, GOLD, 2)
arrow(ax, 58, 58, 64, 51, GOLD, 2)

# Modified betas
rbox(ax, 5, 28, 18, 8, r"$b_1' = 25/6$", BLUE, 12, '25', CYAN)
rbox(ax, 30, 28, 18, 8, r"$b_2' = -13/6$", GREEN, 12, '13', CYAN)
rbox(ax, 55, 28, 18, 8, r"$b_3' = -20/3$", RED, 12, '20', CYAN)

arrow(ax, 14, 43, 14, 36, BLUE, 1.5)
arrow(ax, 39, 43, 39, 36, GREEN, 1.5)
arrow(ax, 64, 43, 64, 36, RED, 1.5)

# Gap ratio and crossing
rbox(ax, 80, 43, 18, 8, '38/27', CYAN, 14,
     r"$(b_1'-b_2')/(b_2'-b_3')$", SILVER)
arrow(ax, 48, 46, 80, 47, DIM, 1)

# The prediction
rbox(ax, 20, 10, 25, 10, r'$\alpha_s = 0.1184$', GOLD, 16,
     'miss: 0.33%', GREEN)

# The integers flow into the prediction
arrow(ax, 14, 28, 28, 20, BLUE, 2)
arrow(ax, 39, 28, 35, 20, GREEN, 2)
arrow(ax, 64, 28, 42, 20, RED, 2)

# Cross-domain connections
rbox(ax, 60, 10, 25, 10, r'DM/baryon = $\frac{22}{13}\pi$', PURPLE, 12,
     'miss: 0.07%', GREEN)

arrow(ax, 39, 28, 70, 20, PURPLE, 1.5)
arrow(ax, 64, 28, 75, 20, PURPLE, 1.5)

# Label: same integers
ax.text(50, 4, 'Same integers from one representation ' + r'$\rightarrow$' +
        ' sub-percent predictions in both domains',
        fontsize=11, color=WHITE, ha='center', style='italic')

save(fig, 'phys30_05_integer_map.png')

# ================================================================
# FIG 6: CONVERGENCE STAIRCASE
# Type: Running/Convergence
# Shows: alpha_s prediction improving at each refinement level
# ================================================================
print("Fig 6: Convergence Staircase")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"PERTURBATIVE CONVERGENCE — $\alpha_s$ Prediction at Each Level",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Data points
levels = [0, 1, 2, 3]
labels = ['Tree level\n' + r'($\alpha_{GUT}$)',
          'One-loop\n(no thresh)',
          'Two-loop\n(SM ' + r'$b_{ij}$)',
          'Two-loop\n(SM+VL ' + r'$b_{ij}$)']
alphas = [0.024, 0.10769, 0.11753, 0.11838]
colors = [DIM, ORANGE, CYAN, GREEN]
misses = [79.7, 8.74, 0.40, 0.33]

# The measurement band
ax.axhspan(alpha_s_1sig_lo, alpha_s_1sig_hi, color=MAG, alpha=0.12)
ax.axhspan(alpha_s_3sig_lo, alpha_s_3sig_hi, color=MAG, alpha=0.05)
ax.axhline(y=alpha_s_meas, color=MAG, linewidth=2, linestyle='-',
           label=r'Measured $\alpha_s$ = 0.1180')

ax.text(3.6, alpha_s_meas + 0.0012, r'1$\sigma$', fontsize=9, color=MAG)
ax.text(3.6, alpha_s_3sig_hi + 0.0005, r'3$\sigma$', fontsize=9, color=MAG,
        alpha=0.7)

# Plot the predictions as steps with large markers
for i in range(len(levels)):
    ax.scatter([levels[i]], [alphas[i]], s=300, color=colors[i], zorder=5,
               edgecolors=WHITE, linewidth=2)

    side = 1 if i % 2 == 0 else -1
    offset = 0.006 * side if i > 0 else -0.015

    ax.annotate('%s\n' % labels[i] +
                r'$\alpha_s$ = %.5f' % alphas[i] + '\n' +
                'miss: %.2f%%' % misses[i],
                xy=(levels[i], alphas[i]),
                xytext=(levels[i] + 0.25, alphas[i] + offset),
                fontsize=9, color=colors[i], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=colors[i], lw=1),
                linespacing=1.4)

# Connecting lines
for i in range(len(levels) - 1):
    ax.plot([levels[i], levels[i+1]], [alphas[i], alphas[i+1]],
            color=DIM, linewidth=1, linestyle=':', alpha=0.5)

# Gap closed annotation
ax.annotate('96.2% of gap closed',
            xy=(2.5, 0.115), fontsize=13, color=GOLD,
            fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD,
                      alpha=0.9))

ax.set_xlabel('Perturbative level', fontsize=12, color=SILVER)
ax.set_ylabel(r'$\alpha_s$ (predicted)', fontsize=12, color=SILVER)
ax.set_xlim(-0.5, 4.2)
ax.set_ylim(0.015, 0.128)
ax.set_xticks(levels)
ax.set_xticklabels(['Tree', '1-loop', '2-loop\n(SM)', '2-loop\n(full)'],
                    fontsize=9, color=SILVER)
ax.legend(fontsize=10, loc='lower right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys30_06_convergence.png')

# ================================================================
# FIG 7: CROSSING ZOOM — PREDICTED vs MEASURED 1/alpha_3
# Type: Threshold/Region
# Shows: The Delta gap AT M_GUT between predicted and measured
# ================================================================
print("Fig 7: Crossing Zoom")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE CROSSING ZOOM — $\alpha_1 = \alpha_2$ and the $\alpha_3$ Gap",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Zoom into the region near M_GUT
log_E = np.linspace(14, 16.5, 400)
E_GeV = 10**log_E
L = np.log(E_GeV / 91.2) / (2 * np.pi)

inv_a1_z = inv_a1_MZ - b1_CD * L
inv_a2_z = inv_a2_MZ - b2_CD * L
inv_a3_meas_z = inv_a3_MZ_meas - b3_CD * L

ax.plot(log_E, inv_a1_z, color=BLUE, linewidth=2.5,
        label=r'$1/\alpha_1$ (U(1))')
ax.plot(log_E, inv_a2_z, color=GREEN, linewidth=2.5,
        label=r'$1/\alpha_2$ (SU(2))')
ax.plot(log_E, inv_a3_meas_z, color=RED, linewidth=2.5,
        label=r'$1/\alpha_3$ (from measured $\alpha_s$)')

# The predicted 1/alpha_3 = 1/alpha_GUT line
ax.axhline(y=inv_aGUT, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(14.1, inv_aGUT + 0.3, r'$1/\alpha_{GUT}$ = %.2f' % inv_aGUT,
        fontsize=10, color=GOLD)

# Mark crossing
ax.scatter([log_E_cross], [inv_aGUT], s=300, color=WHITE, zorder=5,
           edgecolors=GOLD, linewidth=3)

# Mark the Delta gap
inv_a3_at_GUT = inv_a3_MZ_meas - b3_CD * L_cross_val
ax.scatter([log_E_cross], [inv_a3_at_GUT], s=200, color=RED, zorder=5,
           edgecolors=WHITE, linewidth=2)

# Draw the gap
ax.annotate('',
            xy=(log_E_cross + 0.08, inv_aGUT),
            xytext=(log_E_cross + 0.08, inv_a3_at_GUT),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=3))

ax.text(log_E_cross + 0.25, (inv_aGUT + inv_a3_at_GUT) / 2,
        r'$\Delta$ = %.2f' % (inv_a3_at_GUT - inv_aGUT),
        fontsize=14, color=ORANGE, fontweight='bold', va='center')

# Shade the "exact unification" region
ax.axhspan(inv_aGUT - 0.5, inv_aGUT + 0.5, color=GOLD, alpha=0.08)
ax.text(14.1, inv_aGUT - 0.8, 'exact unification band',
        fontsize=9, color=GOLD, alpha=0.6, style='italic')

# Two-loop improvement arrow
inv_a3_2loop_est = inv_aGUT + 0.40   # roughly where 2-loop puts it
ax.scatter([log_E_cross - 0.15], [inv_a3_2loop_est], s=150, color=CYAN,
           zorder=5, marker='D', edgecolors=WHITE, linewidth=1.5)
ax.annotate('Two-loop residual\n' + r'$\Delta$ ~ $-$0.40',
            xy=(log_E_cross - 0.15, inv_a3_2loop_est),
            xytext=(14.3, inv_a3_2loop_est - 1.5),
            fontsize=10, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=12, color=SILVER)
ax.set_ylabel(r'$1/\alpha_i$', fontsize=12, color=SILVER)
ax.set_xlim(14, 16.5)
ax.set_ylim(38, 48)
ax.legend(fontsize=10, loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys30_07_crossing_zoom.png')

# ================================================================
# FIG 8: SIX SCENARIOS COMPARISON BARS
# Type: Comparison Bar Chart
# Shows: All six predictions against the measurement band
# ================================================================
print("Fig 8: Six Scenarios Comparison")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"SIX SCENARIOS — $\alpha_s$ Predictions vs Measurement",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

names = [s[0] for s in scenarios]
alpha_vals = [s[1] for s in scenarios]
misses_s = [s[2] for s in scenarios]
in_3sig = [s[3] for s in scenarios]

y_pos = np.arange(len(names))
bar_colors = [RED, RED, CYAN, ORANGE, GREEN, ORANGE]

bars = ax.barh(y_pos, alpha_vals, 0.55, color=bar_colors, alpha=0.6,
               edgecolor=bar_colors, linewidth=2)

# Measurement band
ax.axvspan(alpha_s_1sig_lo, alpha_s_1sig_hi, color=MAG, alpha=0.15)
ax.axvspan(alpha_s_3sig_lo, alpha_s_3sig_hi, color=MAG, alpha=0.05)
ax.axvline(x=alpha_s_meas, color=MAG, linewidth=2.5,
           label=r'Measured: $\alpha_s$ = 0.1180')

# Labels on each bar
for i in range(len(names)):
    x_label = alpha_vals[i] - 0.001
    if alpha_vals[i] < 0.112:
        x_label = alpha_vals[i] + 0.001
    ha = 'right' if alpha_vals[i] > 0.112 else 'left'

    status = r'$\checkmark$ 3$\sigma$' if in_3sig[i] else ''
    ax.text(x_label, y_pos[i],
            '%.5f  (%.2f%%)  %s' % (alpha_vals[i], misses_s[i], status),
            fontsize=9, color=WHITE, va='center', ha=ha, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(names, fontsize=10, color=SILVER)
ax.set_xlabel(r'$\alpha_s$ (predicted)', fontsize=12, color=SILVER)
ax.set_xlim(0.098, 0.125)

# Band labels
ax.text(alpha_s_meas + 0.0003, 5.7, r'1$\sigma$', fontsize=9, color=MAG)
ax.text(alpha_s_3sig_hi + 0.0003, 5.7, r'3$\sigma$', fontsize=9, color=MAG,
        alpha=0.7)

ax.legend(fontsize=10, loc='lower left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

# Highlight best
ax.add_patch(mpatches.FancyBboxPatch(
    (0.098, 3.7), 0.027, 0.6,
    boxstyle="round,pad=0.1", facecolor='none',
    edgecolor=GOLD, linewidth=2, linestyle='--'))
ax.text(0.099, 4.6, r'BEST: within 1$\sigma$', fontsize=10,
        color=GOLD, fontweight='bold')

save(fig, 'phys30_08_six_scenarios.png')

# ================================================================
print()
print("=" * 70)
print("PHYS-30 DIAGRAMS — 8 FIGURES GENERATED")
print("=" * 70)

filenames = [
    'phys30_01_prediction_path.png',
    'phys30_02_energy_landscape.png',
    'phys30_03_delta_propagation.png',
    'phys30_04_threshold_comparison.png',
    'phys30_05_integer_map.png',
    'phys30_06_convergence.png',
    'phys30_07_crossing_zoom.png',
    'phys30_08_six_scenarios.png',
]

for i, name in enumerate(filenames, 1):
    print("  Fig %d: %s" % (i, name))
    