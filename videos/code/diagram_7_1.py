#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 7, Slides 11-20
10 figures covering: mass hierarchy, Koide conditional, lithium problem,
four elements scorecard, theta QCD, CD search window,
CD dependency map, complete map, kill switch coverage, trust from failures.
Output: PNG files to ./figures/

RULES:
- No edgecolor parameter on any element
- No edgecolors parameter on any element
- All text inside axis limits
- Vertical offset to prevent label overlap
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# -- Output directory --
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(outdir, exist_ok=True)

# -- Color palette --
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

def rounded_box(ax, x, y, w, h, text, color, fontsize=10, textcolor=WHITE, alpha=0.25):
    box = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.15", facecolor=color, alpha=alpha,
        linewidth=1.5)
    ax.add_patch(box)
    if text:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=textcolor, fontweight='bold', zorder=10)


# ================================================================
# FIG 11: THE MASS HIERARCHY — SIX INPUTS NOT DERIVED
# Type: Scale/Landscape
# Shows: log-scale mass gap with INPUT labels on all six
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

particles = [
    (r"$e$", 0.511, CYAN),
    (r"$\mu$", 105.7, CYAN),
    (r"$\tau$", 1776.9, CYAN),
    (r"$M_H$", 125200, GREEN),
    (r"$M_Z$", 91188, GREEN),
    (r"$m_t$", 172570, RED),
]

y_pos = np.arange(len(particles))
masses = [p[1] for p in particles]
names = [p[0] for p in particles]
colors_p = [p[2] for p in particles]

# Sort by mass for visual
sorted_idx = np.argsort(masses)
masses_s = [masses[i] for i in sorted_idx]
names_s = [names[i] for i in sorted_idx]
colors_s = [colors_p[i] for i in sorted_idx]

ax.barh(y_pos, masses_s, height=0.5, color=colors_s, alpha=0.6)

for i in range(len(particles)):
    # Mass label right of bar
    ax.text(masses_s[i] * 1.5, y_pos[i], "%.1f MeV" % masses_s[i] if masses_s[i] < 10000
            else "%.0f MeV" % masses_s[i],
            ha='left', va='center', fontsize=9, color=SILVER)

    # INPUT label
    ax.text(masses_s[i] * 5, y_pos[i], "INPUT", ha='left', va='center',
            fontsize=10, color=ORANGE, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(names_s, fontsize=14, color=WHITE)
ax.set_xscale('log')
ax.set_xlabel("Mass (MeV)", fontsize=11, color=SILVER)
ax.set_title("The Mass Hierarchy: Why Is the Top 340,000" + r"$\times$" + " the Electron?",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Span annotation
ax.annotate("340,000" + r"$\times$" + "\nwhy?",
            xy=(172570, 5), xytext=(1000, 5.3),
            fontsize=12, color=GOLD, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# Lepton sub-spans
ax.annotate("207" + r"$\times$", xy=(105.7, 1), xytext=(20, 0.5),
            fontsize=9, color=CYAN,
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1))

# Koide hint
ax.text(5, 2.7, "Koide: if a" + r"$^2$" + " = 2,\n" + r"$m_\tau$" + " predicted\nat 62 ppm.\nBut a" + r"$^2$" + " = 2\nis assumed,\nnot derived.",
        ha='center', va='center', fontsize=8, color=GOLD, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(100, -0.8, "6 of the 13 inputs are masses. If derivable from gauge integers,\n"
        "input count drops from 13 to 7. The biggest open problem.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0.3, 500000)
ax.set_ylim(-1.2, 6.2)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_11_mass_hierarchy.png")


# ================================================================
# FIG 12: THE KOIDE CONDITIONAL — IF A^2 = 2
# Type: Threshold/Region
# Shows: predicted dot just inside measured band — precarious
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

measured_tau = 1776.86
meas_unc = 0.12
predicted_tau = 1776.97

# Measured band
ax.axhspan(measured_tau - meas_unc * 3, measured_tau + meas_unc * 3, color=MAG, alpha=0.05)
ax.axhspan(measured_tau - meas_unc, measured_tau + meas_unc, color=MAG, alpha=0.12)
ax.axhline(y=measured_tau, color=MAG, linewidth=1.5, linestyle='--', alpha=0.6)

# Measured label
ax.text(3.5, measured_tau - 0.2, "PDG 2024: 1776.86 " + r"$\pm$" + " 0.12 MeV",
        ha='center', va='top', fontsize=10, color=MAG)

# Predicted point
ax.scatter([1.5], [predicted_tau], s=300, color=GOLD, zorder=5, marker='o')
ax.text(1.5, predicted_tau + 0.18, "If a" + r"$^2$" + " = 2 exactly:\n1776.97 MeV\nMiss: 62 ppm",
        ha='center', va='bottom', fontsize=10, color=GOLD, fontweight='bold')

# Current a^2 value
ax.text(3.5, 1777.3, "Current: a" + r"$^2$" + " = 1.99996...\nClose to 2 but not proven\nto be exactly 2",
        ha='center', va='center', fontsize=9, color=CYAN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Kill switch
ax.text(3.5, 1776.2, "Kill: Belle II or FCC-ee measures\n" + r"$m_\tau$" +
        " > 3" + r"$\sigma$" + " from 1776.97",
        ha='center', va='center', fontsize=9, color=RED,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Status
ax.text(1.0, 1776.15, "Status: ACTIVE\nConditional prediction\nCondition not derived",
        ha='center', va='center', fontsize=8, color=ORANGE)

ax.set_xlim(0.5, 5.0)
ax.set_ylim(1776.0, 1777.5)
ax.set_ylabel(r"$m_\tau$ (MeV)", fontsize=12, color=SILVER)
ax.set_xticks([])
ax.set_title("The Koide Conditional: A Bridge That Might Not Exist",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_12_koide_conditional.png")


# ================================================================
# FIG 13: THE LITHIUM PROBLEM — THE RIGHT WRONG ANSWER
# Type: Comparison Bar
# Shows: factor 3x gap with context bars showing everyone is wrong
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

labels = ["RUM\nprediction", "Standard\nBBN", "Any model\nthat gets\nD/H right", "Measured"]
values = [4.74, 4.74, 4.74, 1.60]
bar_colors = [GOLD, DIM, DIM, MAG]
alphas = [0.7, 0.3, 0.3, 0.7]

x = np.arange(len(labels))

for i in range(len(labels)):
    ax.bar(x[i], values[i], width=0.5, color=bar_colors[i], alpha=alphas[i])
    ax.text(x[i], values[i] + 0.15, "%.2f" % values[i], ha='center', va='bottom',
            fontsize=11, color=bar_colors[i], fontweight='bold')

# Factor annotation
ax.annotate("2.96" + r"$\times$" + "\noverprediction",
            xy=(1.5, 3.0), xytext=(1.5, 3.0),
            fontsize=14, color=RED, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Arrows showing "same height"
ax.annotate("same", xy=(0.3, 4.74), xytext=(0.8, 4.74),
            fontsize=8, color=DIM, ha='center',
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1))
ax.annotate("same", xy=(1.3, 4.74), xytext=(1.8, 4.74),
            fontsize=8, color=DIM, ha='center',
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1))

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, color=WHITE)
ax.set_ylabel("Li-7 / H " + r"($\times 10^{-10}$)", fontsize=11, color=SILVER)
ax.set_title("Lithium-7: Every Model Gets This Wrong",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(1.5, 0.5, "40-year unsolved problem. Same nuclear physics.\n"
        "Same result. Reproducing the right wrong answer\n"
        "confirms the chain is doing correct physics.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_ylim(0, 5.5)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_13_lithium_problem.png")


# ================================================================
# FIG 14: FOUR ELEMENTS — THREE RIGHT, ONE WRONG
# Type: Comparison Bar
# Shows: three green checkmarks, one red X
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

elements = ["Deuterium", "Helium-4", "Helium-3", "Lithium-7"]
pred_ratio = [1.002, 1.015, 1.04, 2.96]  # pred/meas ratio
misses = [r"0.12$\sigma$", r"0.94$\sigma$", "consistent", r"2.96$\times$"]
elem_colors = [GREEN, GREEN, CYAN, RED]
icons = [r"$\checkmark$", r"$\checkmark$", r"$\checkmark$", r"$\times$"]

x = np.arange(len(elements))
w = 0.35

# Predicted bars (as ratio to measured)
for i in range(len(elements)):
    ax.bar(x[i] - w/2, pred_ratio[i], w, color=GOLD, alpha=0.6)
    ax.bar(x[i] + w/2, 1.0, w, color=elem_colors[i], alpha=0.6)

# Unity line
ax.axhline(y=1.0, color=SILVER, linewidth=1, linestyle='--', alpha=0.3)
ax.text(3.5, 1.03, "perfect agreement", ha='right', va='bottom',
        fontsize=7, color=SILVER)

# Labels
for i in range(len(elements)):
    top = max(pred_ratio[i], 1.0)
    # Miss label
    ax.text(x[i], top + 0.12, misses[i], ha='center', va='bottom',
            fontsize=11, color=elem_colors[i], fontweight='bold')
    # Icon higher up
    ax.text(x[i], top + 0.35, icons[i], ha='center', va='bottom',
            fontsize=18, color=elem_colors[i])

ax.set_xticks(x)
ax.set_xticklabels(elements, fontsize=12, color=WHITE)
ax.set_ylabel("Predicted / Measured", fontsize=11, color=SILVER)
ax.set_title("Primordial Abundances: The Scorecard",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(0.5, 2.5, "GOLD = predicted\nCOLOR = measured", ha='left',
        va='center', fontsize=8, color=SILVER)

ax.text(1.5, 0.3, "Three greens confirm the chain.\nOne red is inherited from standard nuclear physics.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_ylim(0.0, 3.8)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_14_four_elements.png")


# ================================================================
# FIG 15: THETA QCD — DERIVED OR ASSUMED?
# Type: Comparison Bar (two panels)
# Shows: two approaches to strong CP — one complex, one simple but uncertain
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The Strong CP Problem: Solved or Sidestepped?",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Standard approach --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Standard Approach", ha='center', va='center',
         fontsize=13, fontweight='bold', color=DIM)

# Potential curve with minimum at theta=0
theta_x = np.linspace(0, 10, 100)
theta_v = 5.0 + 1.5 * np.cos((theta_x - 5) * 0.8)
ax1.plot(theta_x, theta_v, color=DIM, linewidth=2)
ax1.scatter([5], [3.5], s=100, color=DIM, zorder=5, marker='v')
ax1.text(5, 3.0, r"$\theta$ = 0", ha='center', va='top', fontsize=9, color=DIM)

ax1.text(5, 7.5, "Add an axion field\nto drive " + r"$\theta \rightarrow 0$" + "\ndynamically",
         ha='center', va='center', fontsize=10, color=DIM)

ax1.text(5, 1.5, "Requires a new particle (axion).\nNot found after 40 years.",
         ha='center', va='center', fontsize=9, color=RED, fontstyle='italic')

# -- Right: RUM approach --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "RUM Approach", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

# Same potential curve
ax2.plot(theta_x, theta_v, color=GOLD, linewidth=2, alpha=0.5)
ax2.scatter([5], [3.5], s=150, color=GOLD, zorder=5, marker='v')
ax2.text(5, 3.0, r"$\theta$ = 0", ha='center', va='top', fontsize=9, color=GOLD)

ax2.text(5, 7.5, r"$\theta$ = 0 is the ground state" + "\nof an integer topological system.\nNo axion needed.",
         ha='center', va='center', fontsize=10, color=GOLD)

ax2.text(5, 5.5, "?", ha='center', va='center', fontsize=30, color=ORANGE, alpha=0.5)

ax2.text(5, 1.5, "Is this a derivation\nor an assumption?",
         ha='center', va='center', fontsize=10, color=ORANGE, fontstyle='italic')

# Kill switch
fig.text(0.5, 0.05, "Kill: neutron electric dipole moment experiment detects nonzero " +
         r"$\theta$" + ". Running at SNS now.\n"
         "Whether this is genuine or assumed is debatable. The experiment will decide.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk7_15_theta_qcd.png")


# ================================================================
# FIG 16: PREDICTED BUT NOT FOUND — CD SEARCH WINDOW
# Type: Threshold/Region
# Shows: excluded region, predicted window, future reach
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Energy axis
e_range = np.linspace(100, 10000, 300)

# Excluded region
ax.axvspan(100, 1500, color=RED, alpha=0.1)
ax.text(800, 0.7, "LHC Run 2:\nsearched and\nnot found", ha='center', va='center',
        fontsize=10, color=RED)

# Predicted window
ax.axvspan(1500, 6000, color=GOLD, alpha=0.08)
ax.text(3750, 0.7, "Predicted mass:\n1.5 to 6 TeV", ha='center', va='center',
        fontsize=12, color=GOLD, fontweight='bold')

# Reference mass
ax.axvline(x=3000, color=CYAN, linewidth=2, linestyle='--', alpha=0.5)
ax.text(3000, 0.92, "Reference: 3 TeV\nHL-LHC sensitivity", ha='center', va='center',
        fontsize=9, color=CYAN)

# Beyond LHC
ax.axvspan(6000, 10000, color=DIM, alpha=0.05)
ax.text(8000, 0.7, "Would require\n100 TeV collider\n(FCC-hh)\nDecades away",
        ha='center', va='center', fontsize=9, color=DIM)

# Kill switch
ax.text(3750, 0.3, "Kill: LHC or successor searches entire\n1.5-6 TeV window and finds nothing.",
        ha='center', va='center', fontsize=10, color=RED,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# What survives
ax.text(3750, 0.12, "If killed: QED chain, EW anatomy, Q335 survive.\n"
        "Unification, DM ratio, proton decay, CKM column die.",
        ha='center', va='center', fontsize=8, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlabel("Energy (GeV)", fontsize=11, color=SILVER)
ax.set_title("The Cabibbo Doublet: Where Is It?",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)
ax.set_xscale('log')
ax.set_xlim(100, 10000)
ax.set_ylim(0.0, 1.0)
ax.set_yticks([])

# Tick labels
ax.set_xticks([100, 500, 1000, 1500, 3000, 6000, 10000])
ax.set_xticklabels(["100\nGeV", "500", "1000", "1500", "3000", "6000", "10000\nGeV"],
                   fontsize=8, color=DIM)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_16_cd_search_window.png")


# ================================================================
# FIG 17: WHAT DEPENDS ON THE CD AND WHAT DOESN'T
# Type: Connection/Integer Map
# Shows: modular framework — which pieces survive if CD dies
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 11)

ax.text(7, 10.3, "The Framework Without the Cabibbo Doublet",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# CD box in center
rounded_box(ax, 7, 6.5, 3.0, 1.2, "Cabibbo Doublet\n(3, 2, 1/6)", GOLD, fontsize=10, alpha=0.2)
ax.text(7, 5.6, "Predicted. Not found.", ha='center', va='center',
        fontsize=8, color=ORANGE, fontstyle='italic')

# CD-dependent (left, dies if CD dies)
ax.text(3.0, 9.5, "DIES IF CD KILLED", ha='center', va='center',
        fontsize=11, color=RED, fontweight='bold')

cd_dep = [
    r"sin$^2\theta_W$ from integers",
    r"$\alpha_s$ from crossing",
    "DM/baryon = (22/13)" + r"$\pi$",
    r"$\Omega_{DM}$ = 44/169",
    "Proton decay prediction",
    "CKM fourth column",
    "Sector splitting formula",
]

for i, item in enumerate(cd_dep):
    y = 8.5 - i * 0.9
    rounded_box(ax, 3.0, y, 3.5, 0.6, item, RED, fontsize=7, alpha=0.1, textcolor=RED)

# CD-independent (right, survives)
ax.text(11.0, 9.5, "SURVIVES WITHOUT CD", ha='center', va='center',
        fontsize=11, color=GREEN, fontweight='bold')

cd_indep = [
    r"QED $\alpha$ extraction (0.007 ppb)",
    "Rydberg, Bohr radius",
    "H 1S-2S frequency",
    "Q335 basis (82/82 null)",
    "EW anatomy (gap = 2)",
    "Koide relation",
    "GR dilation (18 tests)",
]

for i, item in enumerate(cd_indep):
    y = 8.5 - i * 0.9
    rounded_box(ax, 11.0, y, 3.5, 0.6, item, GREEN, fontsize=7, alpha=0.12, textcolor=GREEN)

# Arrows from CD to dependent items
for i in range(len(cd_dep)):
    y = 8.5 - i * 0.9
    ax.plot([5.3, 4.8], [6.5, y], color=RED, linewidth=0.5, alpha=0.2)

ax.text(7, 1.5, "The framework is designed so pieces can be killed independently.\n"
        "7 results die with the CD. 7 results survive without it.\nModular, not monolithic.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk7_17_cd_dependency.png")


# ================================================================
# FIG 18: THE COMPLETE MAP — GREEN, YELLOW, RED
# Type: Connection/Integer Map
# Shows: three zones showing confirmed, active, open
# ================================================================
fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 13)

ax.text(7, 12.3, "The Map: What We Know, What We're Working On, What We Don't",
        ha='center', va='center', fontsize=15, fontweight='bold', color=GOLD)

# GREEN ZONE — Confirmed
ax.text(7, 11.3, "CONFIRMED (automated tests pass)", ha='center', va='center',
        fontsize=11, color=GREEN, fontweight='bold')

confirmed = [
    ("QED chain\n0.007 ppb", 1.5, 10.3),
    ("EW sector\nM_W, " + r"$\Gamma_Z$", 4.5, 10.3),
    ("BBN chain\nD/H 0.12" + r"$\sigma$", 7.5, 10.3),
    ("Q335 basis\n82/82 null", 10.5, 10.3),
    (r"$\beta$ coefficients" + "\nexact fractions", 1.5, 9.0),
    ("GR dilation\n17/18 pass", 4.5, 9.0),
    ("Confinement\nboundary", 7.5, 9.0),
    ("Boundary\nthickness exact", 10.5, 9.0),
]
for label, cx, cy in confirmed:
    rounded_box(ax, cx, cy, 2.5, 0.8, label, GREEN, fontsize=7, alpha=0.12)

# Separator
ax.plot([0, 14], [8.2, 8.2], color=GOLD, linewidth=1, linestyle=':', alpha=0.3)

# YELLOW ZONE — Active frontiers
ax.text(7, 7.8, "ACTIVE FRONTIERS (kill switches set)", ha='center', va='center',
        fontsize=11, color=ORANGE, fontweight='bold')

active = [
    ("Gap = 0.027\n3-loop pending", 1.5, 6.8),
    ("CD search\n1.5-6 TeV", 4.5, 6.8),
    ("Koide a" + r"$^2$" + "=2\nconditional", 7.5, 6.8),
    ("Sector splitting\nTh-229, 2028", 10.5, 6.8),
    ("Statistical\ncontrol p=0.81", 3.0, 5.7),
    ("Hubble tension\nframing", 7.0, 5.7),
]
for label, cx, cy in active:
    col = RED if "p=0.81" in label else ORANGE
    rounded_box(ax, cx, cy, 2.5, 0.8, label, col, fontsize=7, alpha=0.12,
                textcolor=col)

# Separator
ax.plot([0, 14], [5.0, 5.0], color=RED, linewidth=1, linestyle=':', alpha=0.3)

# RED ZONE — Open problems
ax.text(7, 4.6, "OPEN PROBLEMS (documented as unknown)", ha='center', va='center',
        fontsize=11, color=RED, fontweight='bold')

open_probs = [
    ("Mass hierarchy\n6 inputs not derived", 1.5, 3.6),
    ("Confinement wall\n300 MeV " + r"$-$" + " 2 GeV", 4.5, 3.6),
    ("Gravity " + r"$\leftrightarrow$" + "\ngauge integers", 7.5, 3.6),
    ("Lithium\nfactor 3", 10.5, 3.6),
    (r"$\theta_{QCD}$" + "\nderived or\nassumed?", 3.0, 2.3),
]
for label, cx, cy in open_probs:
    rounded_box(ax, cx, cy, 2.5, 0.8, label, RED, fontsize=7, alpha=0.1, textcolor=RED)

# Summary
ax.text(7, 0.5, "Everything green has passed automated tests.\n"
        "Everything yellow has active programs with kill switches.\n"
        "Everything red is documented as unknown.\n"
        "The map has edges and the edges are labeled.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN))

save(fig, "talk7_18_complete_map.png")


# ================================================================
# FIG 19: KILL SWITCH COVERAGE — EVERY CLAIM HAS A DEATH CONDITION
# Type: Comparison Bar (grid)
# Shows: one-to-one pairing of claims and kill conditions
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 10)

ax.text(7, 9.3, "Every Active Claim Has a Way to Die",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

claims = [
    ("Gauge unification via CD",
     "3-loop gap doesn't close\n+ no threshold fix",
     "Computation"),
    ("DM/baryon = (22/13)" + r"$\pi$",
     "Statistical control stays\nat p > 0.1",
     "PHYS-31"),
    ("Proton decay in\nHyper-K window",
     "Hyper-K null at\n" + r"$\tau > 10^{35}$" + " years",
     "Hyper-K 2027+"),
    ("Sector splitting " + r"$\varepsilon$",
     "Th-229 vs Sr-87 agree\nto " + r"$10^{-19}$",
     "PTB/JILA 2028"),
    ("CD exists at\n1.5-6 TeV",
     "Full mass window\nsearched, nothing",
     "LHC/FCC"),
    (r"$\theta_{QCD}$ = 0" + "\nby minimization",
     "nEDM detects\nnonzero " + r"$\theta$",
     "SNS experiment"),
    ("Koide a" + r"$^2$" + " = 2",
     "Belle II " + r"$m_\tau$" + " > 3" + r"$\sigma$" + "\nfrom 1776.97",
     "Belle II / FCC-ee"),
]

for i, (claim, kill, source) in enumerate(claims):
    y = 8.0 - i * 1.15

    # Claim (green)
    rounded_box(ax, 3.0, y, 4.0, 0.8, claim, GREEN, fontsize=7, alpha=0.12, textcolor=GREEN)

    # Arrow
    ax.annotate("", xy=(6.5, y), xytext=(5.2, y),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

    # Kill (red)
    rounded_box(ax, 9.0, y, 4.0, 0.8, kill, RED, fontsize=7, alpha=0.1, textcolor=RED)

    # Source
    ax.text(12.5, y, source, ha='left', va='center', fontsize=7, color=DIM)

# Column headers
ax.text(3.0, 9.0, "CLAIM", ha='center', va='center', fontsize=10,
        color=GREEN, fontweight='bold')
ax.text(9.0, 9.0, "KILL CONDITION", ha='center', va='center', fontsize=10,
        color=RED, fontweight='bold')
ax.text(12.5, 9.0, "SOURCE", ha='center', va='center', fontsize=10,
        color=SILVER, fontweight='bold')

ax.text(7, -0.2, "No claim exists without a kill switch.\nFalsifiability is built in, not bolted on.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk7_19_kill_switch_coverage.png")


# ================================================================
# FIG 20: TRUST IS BUILT FROM FAILURES, NOT SUCCESSES
# Type: Comparison Bar (two panels)
# Shows: successes list (short) vs failures list (detailed) — asymmetry
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("What Builds Trust",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Showing successes --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Showing Successes", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GREEN)

successes = [
    r"$\alpha^{-1}$ at 0.007 ppb  $\checkmark$",
    r"D/H at 0.12$\sigma$  $\checkmark$",
    r"Mercury at 2.8 ppm  $\checkmark$",
    r"GPS at 0.35%  $\checkmark$",
]
for i, s in enumerate(successes):
    ax1.text(5, 7.0 - i * 1.0, s, ha='center', va='center', fontsize=10, color=GREEN)

ax1.text(5, 2.5, "Anyone can show you\ntheir best results.\nThis doesn't prove anything.",
         ha='center', va='center', fontsize=10, color=DIM, fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

# -- Right: Showing failures --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Showing Failures", ha='center', va='center',
         fontsize=13, fontweight='bold', color=ORANGE)

failures = [
    "Gap = 0.027 not zero",
    "p = 0.81 (BLOCKED)",
    "Confinement wall blank",
    "Gravity not connected",
    "Lithium factor 3",
    "CD not found",
    "Mass hierarchy not derived",
    "GPA FAIL at 2.47%",
]
for i, f in enumerate(failures):
    col = RED if "FAIL" in f or "BLOCKED" in f else ORANGE
    ax2.text(5, 7.5 - i * 0.8, f, ha='center', va='center', fontsize=10, color=col)

ax2.text(5, 1.0, "Showing exactly where\nthe model doesn't work,\nwith documentation\nand kill switches.\nTHIS builds trust.",
         ha='center', va='center', fontsize=10, color=GOLD, fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

# [continuing from where it cut off]

# Center arrow between panels
fig.text(0.50, 0.50, "The test of a model isn't\nhow many things it gets right.\nIt's whether it tells you\nwhat it gets wrong.",
         ha='center', va='center', fontsize=11, color=WHITE,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

fig.text(0.50, 0.04, "A model that hides its failures is a model you can't trust.\n"
         "A model that shows you exactly where it doesn't work is a model you can investigate.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk7_20_trust_from_failures.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 7, 11-20) generated ===")
filenames = [
    "talk7_11_mass_hierarchy.png",
    "talk7_12_koide_conditional.png",
    "talk7_13_lithium_problem.png",
    "talk7_14_four_elements.png",
    "talk7_15_theta_qcd.png",
    "talk7_16_cd_search_window.png",
    "talk7_17_cd_dependency.png",
    "talk7_18_complete_map.png",
    "talk7_19_kill_switch_coverage.png",
    "talk7_20_trust_from_failures.png",
]
for f in filenames:
    print("  %s" % f)
    