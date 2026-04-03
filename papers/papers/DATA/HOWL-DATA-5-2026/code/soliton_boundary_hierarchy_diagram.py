#!/usr/bin/env python3
"""
HOWL Soliton Boundary Hierarchy Diagrams
8 figures covering the boundary stack, coupling running,
non-interference principle, confinement wall, beta staircase,
nested structure, R2 domain connections, and alpha_s convergence.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

# Output directory
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

def style_ax(ax, title="", xlabel="", ylabel=""):
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


# ================================================================
# PHYSICS DATA
# ================================================================

# Beta coefficients (exact values as floats for plotting)
b1_SM = 41.0 / 10.0    # 4.1
b2_SM = -19.0 / 6.0    # -3.167
b3_SM = -7.0            # -7.0

b1_CD = 25.0 / 6.0     # 4.167
b2_CD = -13.0 / 6.0    # -2.167
b3_CD = -20.0 / 3.0    # -6.667

# Inverse couplings at M_Z
inv_a1_MZ = 63.21
inv_a2_MZ = 31.69
inv_a3_MZ = 8.47

# Key scales (log10 of GeV)
log_me = np.log10(0.000511)
log_mmu = np.log10(0.1057)
log_Lambda = np.log10(0.3)
log_mc = np.log10(1.273)
log_mtau = np.log10(1.777)
log_mb = np.log10(4.183)
log_MZ = np.log10(91.19)
log_mH = np.log10(125.2)
log_mt = np.log10(172.6)
log_MVL = np.log10(3000.0)
log_MGUT = 15.54
log_MPlanck = 19.09

# One-loop running function
def run_coupling(inv_a0, b, log_mu0, log_mu_array):
    """1/alpha(mu) = 1/alpha(mu0) - b * ln(mu/mu0) / (2*pi)"""
    L_array = (log_mu_array - log_mu0) * np.log(10) / (2 * np.pi)
    return inv_a0 - b * L_array


# ================================================================
# FIG 1: THE FULL ENERGY LANDSCAPE
# Type: Scale/Landscape
# Shows: All 19 boundaries from m_e to M_Planck with their names,
# forces, and known/unknown status. The SCALE communicates what
# text cannot: the vast desert between m_t and M_GUT.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
style_ax(ax)
ax.axis('off')
ax.set_xlim(-1, 10)
ax.set_ylim(-1.5, 20.5)

boundaries = [
    (-3.29, "Electron\nm$_e$ = 0.511 MeV", GREEN, True, "EM"),
    (-0.98, "Muon\nm$_\\mu$ = 105.7 MeV", GREEN, True, "EM"),
    (-0.52, "Confinement (lower)\n$\\Lambda_{QCD}$ ~ 300 MeV", RED, False, "Strong"),
    (0.10, "Charm\nm$_c$ = 1.27 GeV", CYAN, True, "Strong"),
    (0.25, "Tau\nm$_\\tau$ = 1.78 GeV", GREEN, True, "EM"),
    (0.30, "Confinement (upper)\n~ 2 GeV", RED, False, "Strong"),
    (0.62, "Bottom\nm$_b$ = 4.18 GeV", CYAN, True, "Strong"),
    (1.90, "W boson\nM$_W$ = 80.4 GeV", PURPLE, True, "Weak"),
    (1.96, "Z boson / EW scale\nM$_Z$ = 91.2 GeV", GOLD, True, "EM+Weak+Strong"),
    (2.10, "Higgs\nm$_H$ = 125.2 GeV", PURPLE, True, "EM+Weak"),
    (2.24, "Top quark\nm$_t$ = 172.6 GeV", CYAN, True, "Strong"),
    (3.48, "Cabibbo Doublet\nM$_{VL}$ ~ 3 TeV", ORANGE, False, "EM+Weak+Strong"),
    (15.54, "GUT unification\nM$_{GUT}$ ~ 10$^{15.5}$ GeV", MAG, False, "Unified"),
    (19.09, "Planck scale\nM$_{Pl}$ ~ 10$^{19}$ GeV", DIM, False, "Gravity"),
]

# Map to y positions (spread out for readability)
y_positions = np.linspace(0.5, 19.5, len(boundaries))

for idx, (log_E, label, color, known, forces) in enumerate(boundaries):
    y = y_positions[idx]
    marker = 'o' if known else 's'
    edge = WHITE if known else ORANGE

    # Scale bar
    ax.plot([1, 8], [y, y], color=DIM, linewidth=0.5, alpha=0.3)

    # Energy marker
    ax.scatter([1.5], [y], s=120, c=color, marker=marker,
               edgecolors=edge, linewidth=1.5, zorder=5)

    # Label (left side)
    ax.text(2.0, y, label, color=color, fontsize=9,
            va='center', ha='left', fontweight='bold')

    # Energy value (right side)
    ax.text(7.5, y, "log$_{10}$(E/GeV) = %.1f" % log_E, color=SILVER,
            fontsize=8, va='center', ha='right')

    # Forces (far right)
    ax.text(8.2, y, forces, color=DIM, fontsize=7, va='center', ha='left')

# Confinement wall shading
y_conf_lo = y_positions[2]
y_conf_hi = y_positions[5]
ax.fill_between([0.5, 9], y_conf_lo - 0.3, y_conf_hi + 0.3,
                color=RED, alpha=0.06)
ax.text(0.7, (y_conf_lo + y_conf_hi) / 2, "CONFINEMENT\nWALL\n(no integer rules)",
        color=RED, fontsize=8, va='center', ha='left', alpha=0.7,
        fontstyle='italic')

# Desert region
y_top = y_positions[10]
y_gut = y_positions[12]
ax.annotate('', xy=(0.8, y_gut - 0.3), xytext=(0.8, y_top + 0.3),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1.5))
ax.text(0.5, (y_top + y_gut) / 2, "THE\nDESERT",
        color=DIM, fontsize=9, va='center', ha='center', fontstyle='italic')

# Legend
ax.scatter([1.5], [-0.8], s=80, c=WHITE, marker='o', edgecolors=WHITE, linewidth=1)
ax.text(2.0, -0.8, "= measured", color=SILVER, fontsize=8, va='center')
ax.scatter([4.5], [-0.8], s=80, c=WHITE, marker='s', edgecolors=ORANGE, linewidth=1)
ax.text(5.0, -0.8, "= theoretical / staged", color=SILVER, fontsize=8, va='center')

ax.set_title("The Soliton Boundary Hierarchy\n19 Boundaries from m$_e$ to M$_{Planck}$",
             color=GOLD, fontsize=16, fontweight='bold', pad=15)

save(fig, "soliton_01_full_landscape.png")


# ================================================================
# FIG 2: THREE COUPLING RUNNING — CONVERGENCE TOWARD GUT
# Type: Running/Convergence
# Shows: The three inverse couplings running from M_Z toward M_GUT.
# The SHAPE shows convergence with SM betas (miss) and CD betas
# (near-unification). This is the central curve of the series.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title="Gauge Coupling Unification\nSM betas (dashed) vs Cabibbo Doublet betas (solid)",
         xlabel="log$_{10}$($\\mu$ / GeV)", ylabel="1/$\\alpha_i$($\\mu$)")

log_mu = np.linspace(log_MZ, 17, 500)

# SM running (no CD)
inv_a1_SM = run_coupling(inv_a1_MZ, b1_SM, log_MZ, log_mu)
inv_a2_SM = run_coupling(inv_a2_MZ, b2_SM, log_MZ, log_mu)
inv_a3_SM = run_coupling(inv_a3_MZ, b3_SM, log_MZ, log_mu)

ax.plot(log_mu, inv_a1_SM, color=BLUE, linewidth=1.5, linestyle='--', alpha=0.5, label='SM 1/$\\alpha_1$')
ax.plot(log_mu, inv_a2_SM, color=GREEN, linewidth=1.5, linestyle='--', alpha=0.5, label='SM 1/$\\alpha_2$')
ax.plot(log_mu, inv_a3_SM, color=RED, linewidth=1.5, linestyle='--', alpha=0.5, label='SM 1/$\\alpha_3$')

# CD running: SM below M_VL, CD above
log_mu_below = np.linspace(log_MZ, log_MVL, 200)
log_mu_above = np.linspace(log_MVL, 17, 300)

inv_a1_below = run_coupling(inv_a1_MZ, b1_SM, log_MZ, log_mu_below)
inv_a2_below = run_coupling(inv_a2_MZ, b2_SM, log_MZ, log_mu_below)
inv_a3_below = run_coupling(inv_a3_MZ, b3_SM, log_MZ, log_mu_below)

inv_a1_at_VL = inv_a1_below[-1]
inv_a2_at_VL = inv_a2_below[-1]
inv_a3_at_VL = inv_a3_below[-1]

inv_a1_above = run_coupling(inv_a1_at_VL, b1_CD, log_MVL, log_mu_above)
inv_a2_above = run_coupling(inv_a2_at_VL, b2_CD, log_MVL, log_mu_above)
inv_a3_above = run_coupling(inv_a3_at_VL, b3_CD, log_MVL, log_mu_above)

# Plot CD running
for arr_b, arr_a, c, lbl in [
    (inv_a1_below, inv_a1_above, BLUE, 'CD 1/$\\alpha_1$'),
    (inv_a2_below, inv_a2_above, GREEN, 'CD 1/$\\alpha_2$'),
    (inv_a3_below, inv_a3_above, RED, 'CD 1/$\\alpha_3$')]:
    ax.plot(log_mu_below, arr_b, color=c, linewidth=2.5, label=lbl)
    ax.plot(log_mu_above, arr_a, color=c, linewidth=2.5)

# Mark M_VL threshold
ax.axvline(log_MVL, color=ORANGE, linewidth=1.5, linestyle=':', alpha=0.7)
ax.text(log_MVL + 0.15, 58, "M$_{VL}$ ~ 3 TeV\nCD activates",
        color=ORANGE, fontsize=9, va='top')

# Mark approximate crossing
ax.axvline(log_MGUT, color=GOLD, linewidth=1, linestyle='--', alpha=0.5)
ax.text(log_MGUT + 0.15, 48, "M$_{GUT}$\n~ 10$^{15.5}$ GeV",
        color=GOLD, fontsize=9, va='top')

# Mark M_Z
ax.scatter([log_MZ, log_MZ, log_MZ],
           [inv_a1_MZ, inv_a2_MZ, inv_a3_MZ],
           s=150, c=[BLUE, GREEN, RED], edgecolors=WHITE, linewidth=2, zorder=10)

ax.set_xlim(log_MZ - 0.5, 17)
ax.set_ylim(0, 68)
ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=9, ncol=2)
ax.grid(True, alpha=0.1, color=DIM)

save(fig, "soliton_02_coupling_convergence.png")


# ================================================================
# FIG 3: BETA COEFFICIENT STAIRCASE
# Type: Progression/Sequence
# Shows: How b_3 (SU(3) beta) changes at each quark threshold.
# Each step is an exact rational. The staircase structure is
# impossible to convey in text — the eye sees the step sizes
# and where they cluster.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title="Beta Coefficient Staircase: b$_3$ at Each Quark Threshold",
         xlabel="log$_{10}$($\\mu$ / GeV)", ylabel="b$_3$ (one-loop)")

# b3 values at each threshold
# b3 = -(11/3)*3 + (2/3)*n_f + 0 (Higgs singlet)
# = -11 + (2/3)*n_f
thresholds = [
    (log_mc, 3, "charm\nactivates"),
    (log_mb, 4, "bottom\nactivates"),
    (log_mt, 5, "top\nactivates"),
    (log_MVL, 5, "CD\nactivates"),  # CD adds 1/3 to b3, not a new flavor
]

# b3 = -11 + (2/3)*n_f for SM; above CD: b3 = -7 + 1/3 = -20/3
nf_values = [3, 4, 5, 6]
b3_values = [-11 + (2.0/3.0) * nf for nf in nf_values]
b3_CD = -20.0 / 3.0  # after CD

# Draw staircase
log_edges = [0, log_mc, log_mb, log_mt, log_MVL, 5.0]
b3_levels = [b3_values[0], b3_values[0], b3_values[1], b3_values[2], b3_values[3], b3_values[3]]

# Below confinement: mark as unknown
ax.fill_between([log_Lambda - 0.3, 0.3], -12, -4,
                color=RED, alpha=0.06)
ax.text(-0.1, -5.2, "Confinement\n(non-perturbative)", color=RED,
        fontsize=8, va='top', ha='center', fontstyle='italic')

# Draw each level
segments = [
    (0.4, log_mc, -11 + 2.0/3.0*3, "n$_f$=3, b$_3$= $-$9", CYAN),
    (log_mc, log_mb, -11 + 2.0/3.0*4, "n$_f$=4, b$_3$= $-$23/3", GREEN),
    (log_mb, log_mt, -11 + 2.0/3.0*5, "n$_f$=5, b$_3$= $-$7", BLUE),
    (log_mt, log_MVL, -11 + 2.0/3.0*6, "n$_f$=6, b$_3$= $-$19/3", PURPLE),
    (log_MVL, 5.5, b3_CD, "SM+CD, b$_3$'= $-$20/3", ORANGE),
]

for x0, x1, b3, label, color in segments:
    ax.plot([x0, x1], [b3, b3], color=color, linewidth=3)
    ax.text((x0 + x1) / 2, b3 + 0.2, label, color=color, fontsize=9,
            ha='center', va='bottom', fontweight='bold')

# Draw vertical transitions
transitions = [
    (log_mc, -9, -11 + 2.0/3.0*4, "+2/3", GOLD),
    (log_mb, -11 + 2.0/3.0*4, -7, "+2/3", GOLD),
    (log_mt, -7, -11 + 2.0/3.0*6, "+2/3", GOLD),
    (log_MVL, -11 + 2.0/3.0*6, b3_CD, "+1/3\n(CD)", ORANGE),
]

for x, y0, y1, label, color in transitions:
    ax.annotate('', xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    ax.text(x + 0.08, (y0 + y1) / 2, label, color=color, fontsize=9,
            va='center', ha='left', fontweight='bold')

# Each quark threshold marked
for log_E, nf, name in thresholds:
    ax.axvline(log_E, color=DIM, linewidth=0.8, linestyle=':', alpha=0.5)

ax.set_xlim(-0.5, 5.5)
ax.set_ylim(-10.5, -4.5)
ax.grid(True, alpha=0.1, color=DIM)

# Note about democracy
ax.text(3.0, -4.8, "Each quark adds exactly +2/3 to b$_3$ (generation democracy)",
        color=GOLD, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.8))

save(fig, "soliton_03_beta_staircase.png")


# ================================================================
# FIG 4: THE CONFINEMENT WALL
# Type: Threshold/Region
# Shows: The blank zone between ~300 MeV and ~2 GeV where
# perturbative QCD fails. Perturbative regions on both sides
# with coupling curves. The wall itself is unmarked — honestly blank.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title="The Confinement Wall\n$\\alpha_s$ ~ O(1): Integer Rules Break Down",
         xlabel="Energy (GeV)", ylabel="$\\alpha_s$($\\mu$)")

# alpha_s running (perturbative regime only)
mu_above = np.logspace(np.log10(2.0), np.log10(91.19), 200)
# One-loop: alpha_s(mu) = alpha_s(MZ) / (1 + alpha_s(MZ)*b3*ln(mu/MZ)/(2*pi))
alpha_s_MZ = 0.1180
b3_5f = -11 + (2.0/3.0) * 5  # = -7, 5 flavors above b threshold

alpha_s_above = []
for mu in mu_above:
    L = np.log(mu / 91.19) / (2 * np.pi)
    inv_as = 1.0 / alpha_s_MZ - b3_5f * L  # note: minus sign, b3 < 0 means inv decreases going down
    if inv_as > 0:
        alpha_s_above.append(1.0 / inv_as)
    else:
        alpha_s_above.append(np.nan)

ax.plot(mu_above, alpha_s_above, color=RED, linewidth=2.5, label='$\\alpha_s$ (perturbative)')

# Mark the wall
ax.axvspan(0.3, 2.0, color=RED, alpha=0.1)
ax.text(0.8, 0.85, "CONFINEMENT\nWALL", color=RED, fontsize=14,
        ha='center', va='center', fontweight='bold', alpha=0.7)
ax.text(0.8, 0.65, "$\\alpha_s$ ~ O(1)\nNo integer rules\nNo perturbative $\\beta$",
        color=RED, fontsize=9, ha='center', va='center', fontstyle='italic', alpha=0.7)

# Below confinement
ax.text(0.15, 0.5, "Hadrons\nPions\nProtons", color=GREEN, fontsize=9,
        ha='center', va='center')

# Mark key thresholds
for mu, name, color in [(4.18, "m$_b$", CYAN), (1.78, "m$_\\tau$", GREEN),
                          (1.27, "m$_c$", CYAN), (91.19, "M$_Z$", GOLD)]:
    ax.axvline(mu, color=color, linewidth=1, linestyle=':', alpha=0.5)
    ax.text(mu * 1.05, 0.92, name, color=color, fontsize=8, va='top')

# alpha_s = 1 line
ax.axhline(1.0, color=ORANGE, linewidth=1, linestyle='--', alpha=0.5)
ax.text(50, 1.02, "$\\alpha_s$ = 1 (strong coupling)", color=ORANGE, fontsize=8, va='bottom')

# alpha_s at M_Z
ax.scatter([91.19], [0.1180], s=200, c=GOLD, edgecolors=WHITE,
           linewidth=2, zorder=10)
ax.text(70, 0.14, "$\\alpha_s$(M$_Z$) = 0.1180", color=GOLD, fontsize=10,
        va='bottom', ha='right')

ax.set_xscale('log')
ax.set_xlim(0.1, 100)
ax.set_ylim(0, 1.0)
ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=9)
ax.grid(True, alpha=0.1, color=DIM)

save(fig, "soliton_04_confinement_wall.png")


# ================================================================
# FIG 5: NON-INTERFERENCE PRINCIPLE
# Type: Running/Convergence
# Shows: Two scenarios for alpha_3 running at low energy (5-50 GeV):
# one with CD at 3 TeV, one without CD at all. The curves are
# IDENTICAL below the CD threshold. The eye sees: CD cannot reach down.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title="Non-Interference: The Cabibbo Doublet Cannot Affect Low-Energy Running",
         xlabel="log$_{10}$($\\mu$ / GeV)", ylabel="1/$\\alpha_3$($\\mu$)")

log_mu_full = np.linspace(0.7, 5, 400)

# Scenario A: SM only (no CD at any scale)
inv_a3_noCD = run_coupling(inv_a3_MZ, b3_SM, log_MZ, log_mu_full)

# Scenario B: CD at 3 TeV
inv_a3_withCD_below = run_coupling(inv_a3_MZ, b3_SM, log_MZ,
                                    log_mu_full[log_mu_full <= log_MVL])
log_above = log_mu_full[log_mu_full > log_MVL]
if len(log_above) > 0:
    inv_a3_at_VL = run_coupling(inv_a3_MZ, b3_SM, log_MZ, np.array([log_MVL]))[0]
    inv_a3_withCD_above = run_coupling(inv_a3_at_VL, b3_CD, log_MVL, log_above)

# Plot both
ax.plot(log_mu_full, inv_a3_noCD, color=RED, linewidth=2.5, linestyle='--',
        label='SM only (no CD)', alpha=0.8)
ax.plot(log_mu_full[log_mu_full <= log_MVL], inv_a3_withCD_below,
        color=CYAN, linewidth=3, label='SM + CD below M$_{VL}$')
if len(log_above) > 0:
    ax.plot(log_above, inv_a3_withCD_above,
            color=ORANGE, linewidth=3, label='SM + CD above M$_{VL}$')

# Mark the CD threshold
ax.axvline(log_MVL, color=ORANGE, linewidth=2, linestyle=':', alpha=0.7)
ax.text(log_MVL + 0.05, 6.5, "M$_{VL}$ ~ 3 TeV\nCD activates here",
        color=ORANGE, fontsize=10, va='bottom')

# Highlight the identical region
ax.axvspan(0.7, log_MVL, color=GREEN, alpha=0.03)
ax.text(2.0, 3.5, "IDENTICAL\nbelow M$_{VL}$",
        color=GREEN, fontsize=12, ha='center', va='center',
        fontweight='bold', alpha=0.8,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.6))

# Mark M_Z
ax.axvline(log_MZ, color=GOLD, linewidth=1, linestyle=':', alpha=0.5)
ax.text(log_MZ - 0.05, 10.5, "M$_Z$", color=GOLD, fontsize=9, ha='right')

ax.set_xlim(0.5, 5.2)
ax.set_ylim(2, 11)
ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=10)
ax.grid(True, alpha=0.1, color=DIM)

save(fig, "soliton_05_noninterference.png")


# ================================================================
# FIG 6: NESTED SOLITON STRUCTURE
# Type: Geometric Cross-Section
# Shows: Concentric shells representing the boundary hierarchy.
# Each shell is a soliton boundary. The nesting communicates
# that you PASS THROUGH each one in order. Cannot skip.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 16))
fig.patch.set_facecolor(BG)
style_ax(ax)
ax.axis('off')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')

shells = [
    (1.00, "Planck\n10$^{19}$ GeV", DIM, 0.15),
    (0.88, "GUT\n10$^{15.5}$ GeV", MAG, 0.20),
    (0.75, "Cabibbo Doublet\n~ 3 TeV", ORANGE, 0.25),
    (0.63, "Top / Higgs / EW\n91 - 173 GeV", GOLD, 0.30),
    (0.50, "Bottom\n4.2 GeV", BLUE, 0.35),
    (0.38, "Confinement Wall\n0.3 - 2 GeV", RED, 0.15),
    (0.25, "Nuclear\n~ 8 MeV", GREEN, 0.45),
    (0.12, "Electron\n0.511 MeV", CYAN, 0.55),
]

for radius, label, color, alpha_val in shells:
    circle = plt.Circle((0, 0), radius, fill=True, facecolor=color,
                         alpha=alpha_val * 0.15, edgecolor=color,
                         linewidth=2, linestyle='-')
    ax.add_patch(circle)

    # Label at the right edge
    angle = 0.4 + 0.3 * (1.0 - radius)  # stagger angles
    lx = (radius + 0.02) * np.cos(angle)
    ly = (radius + 0.02) * np.sin(angle)
    ax.text(lx + 0.08, ly, label, color=color, fontsize=9,
            ha='left', va='center', fontweight='bold')

# Center label
ax.text(0, 0, "VACUUM", color=WHITE, fontsize=11, ha='center', va='center',
        fontweight='bold')

# Confinement wall: extra marking
circle_conf = plt.Circle((0, 0), 0.38, fill=False, edgecolor=RED,
                          linewidth=3, linestyle='--')
ax.add_patch(circle_conf)

ax.set_title("Nested Soliton Boundaries\nEach shell changes the integer rules",
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

# Arrow from outside to center
ax.annotate('', xy=(0.02, -0.08), xytext=(0.85, -0.85),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2,
                            connectionstyle='arc3,rad=0.2'))
ax.text(0.75, -0.90, "traversal\ninward = higher energy",
        color=SILVER, fontsize=9, ha='center', va='top')

save(fig, "soliton_06_nested_shells.png")


# ================================================================
# FIG 7: R2 ACROSS 15 DOMAINS — CONNECTION MAP
# Type: Connection/Integer Map
# Shows: R2 = pi/4 appearing in 15 different domains, each with
# its specific equation. The central node is R2. The spokes carry
# the actual formula. This is the series thesis made visual.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 18))
fig.patch.set_facecolor(BG)
style_ax(ax)
ax.axis('off')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

domains = [
    ("Pipe flow", "Q = R$_2$d$^2$v", CYAN),
    ("Orifice", "q = C$_d$R$_2$d$^2\\sqrt{2\\Delta P/\\rho}$", CYAN),
    ("Drag", "F = $\\frac{1}{2}\\rho$v$^2$R$_2$d$^2$C$_d$", BLUE),
    ("Wire", "R = $\\rho$L/(R$_2$d$^2$)", ORANGE),
    ("Capacitor", "C = $\\varepsilon_0$R$_2$d$^2$/t", ORANGE),
    ("Antenna", "A$_{eff}$ = G$\\lambda^2$/(16R$_2$)", GREEN),
    ("Speaker", "S$_d$ = R$_2$d$^2_{eff}$", GREEN),
    ("Thermal", "Q = $\\varepsilon\\sigma$T$^4$R$_2$d$^2$", RED),
    ("Sound", "I = P/(16R$_2$r$^2$)", RED),
    ("Fiber mode", "A = R$_2$MFD$^2$", PURPLE),
    ("Disc spot", "A = R$_2$(1.22$\\lambda$/NA)$^2$", PURPLE),
    ("Gaussian beam", "z$_R$ = 4R$_2$w$_0^2$/$\\lambda$", MAG),
    ("Lithography", "CD = 0.61$\\lambda$/NA", MAG),
    ("QED", "$\\alpha/\\pi$ = $\\alpha$/(4R$_2$)", GOLD),
    ("Wafer", "A = R$_2$D$^2$", GOLD),
]

n = len(domains)
for i, (name, eq, color) in enumerate(domains):
    angle = 2 * np.pi * i / n - np.pi / 2
    r_name = 1.15
    r_eq = 0.85
    r_dot = 0.60

    # Spoke line
    ax.plot([0.25 * np.cos(angle), r_dot * np.cos(angle)],
            [0.25 * np.sin(angle), r_dot * np.sin(angle)],
            color=color, linewidth=1.5, alpha=0.6)

    # Domain dot
    ax.scatter([r_dot * np.cos(angle)], [r_dot * np.sin(angle)],
               s=100, c=color, edgecolors=WHITE, linewidth=1.5, zorder=5)

    # Domain name
    ha = 'left' if np.cos(angle) > 0.1 else ('right' if np.cos(angle) < -0.1 else 'center')
    ax.text(r_name * np.cos(angle), r_name * np.sin(angle), name,
            color=color, fontsize=10, ha=ha, va='center', fontweight='bold')

    # Equation
    ax.text(r_eq * np.cos(angle), r_eq * np.sin(angle), eq,
            color=SILVER, fontsize=7, ha=ha, va='center')

# Central R2 node
circle_center = plt.Circle((0, 0), 0.22, facecolor=GOLD, edgecolor=WHITE,
                             linewidth=3, alpha=0.3, zorder=10)
ax.add_patch(circle_center)
ax.text(0, 0.03, "R$_2$ = $\\pi$/4", color=WHITE, fontsize=14,
        ha='center', va='center', fontweight='bold', zorder=11)
ax.text(0, -0.08, "= 0.7854...", color=SILVER, fontsize=9,
        ha='center', va='center', zorder=11)

ax.set_title("R$_2$ = $\\pi$/4 Across 15 Domains\nSame geometry, different coordinator Z",
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, "soliton_07_R2_domain_map.png")


# ================================================================
# FIG 8: ALPHA_S PREDICTION CONVERGENCE
# Type: Comparison Bar
# Shows: The progression from one-loop to two-loop SM to two-loop
# full as the prediction converges toward the measured value.
# The eye sees the bars approaching the measurement band.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title="$\\alpha_s$ Prediction Convergence\nFrom One-Loop to Full Two-Loop",
         xlabel="", ylabel="$\\alpha_s$ prediction")

scenarios = [
    ("One-loop\nCD betas", 0.10769, 8.74, RED),
    ("Two-loop\nSM b$_{ij}$", 0.11753, 0.40, CYAN),
    ("Two-loop\nfull b$_{ij}$\n(SM+VL)", 0.11838, 0.33, GREEN),
]

x_pos = [1, 2.5, 4]
bar_width = 0.8

# Measurement band
alpha_s_meas = 0.1180
alpha_s_err = 0.0009
ax.axhspan(alpha_s_meas - alpha_s_err, alpha_s_meas + alpha_s_err,
           color=GOLD, alpha=0.15)
ax.axhspan(alpha_s_meas - alpha_s_err / 3, alpha_s_meas + alpha_s_err / 3,
           color=GOLD, alpha=0.15)
ax.axhline(alpha_s_meas, color=GOLD, linewidth=2, linestyle='-', alpha=0.8)
ax.text(5.2, alpha_s_meas, "$\\alpha_s$ = 0.1180 $\\pm$ 0.0009\n(measured)",
        color=GOLD, fontsize=10, va='center')

for i, (label, value, miss, color) in enumerate(scenarios):
    ax.bar(x_pos[i], value, width=bar_width, color=color, alpha=0.7,
           edgecolor=color, linewidth=2)
    ax.text(x_pos[i], value + 0.001, "%.5f" % value, color=WHITE,
            fontsize=11, ha='center', va='bottom', fontweight='bold')
    ax.text(x_pos[i], value - 0.002, "miss: %.2f%%" % miss, color=SILVER,
            fontsize=9, ha='center', va='top')
    ax.text(x_pos[i], 0.098, label, color=color, fontsize=10,
            ha='center', va='top', fontweight='bold')

# Arrow showing progression
ax.annotate('', xy=(4.6, 0.1175), xytext=(0.5, 0.1050),
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=2,
                            connectionstyle='arc3,rad=-0.15'))
ax.text(2.5, 0.102, "Systematic convergence toward measurement",
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

ax.set_xlim(0, 5.8)
ax.set_ylim(0.095, 0.125)
ax.set_xticks([])
ax.grid(True, axis='y', alpha=0.1, color=DIM)

save(fig, "soliton_08_alphas_convergence.png")


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("  SOLITON BOUNDARY HIERARCHY DIAGRAMS COMPLETE")
print("  8 figures saved to %s" % outdir)
print("=" * 60)
print()
print("  soliton_01_full_landscape.png      — Full energy landscape")
print("  soliton_02_coupling_convergence.png — Three couplings running to GUT")
print("  soliton_03_beta_staircase.png       — b3 staircase at quark thresholds")
print("  soliton_04_confinement_wall.png     — The blank zone")
print("  soliton_05_noninterference.png      — CD cannot affect low-energy running")
print("  soliton_06_nested_shells.png        — Concentric boundary shells")
print("  soliton_07_R2_domain_map.png        — R2 across 15 domains")
print("  soliton_08_alphas_convergence.png   — alpha_s prediction convergence")
