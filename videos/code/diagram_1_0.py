#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Slides V1-V10
10 figures for video presentation slides.
Output: PNG files to ./figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

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

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(outdir, exist_ok=True)

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def styled_box(ax, xy, w, h, text, color, fontsize=11, textcolor=WHITE, alpha=0.25):
    box = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.15",
                         facecolor=color, edgecolor=color, alpha=alpha, linewidth=2)
    ax.add_patch(box)
    ax.text(xy[0] + w/2, xy[1] + h/2, text, ha='center', va='center',
            fontsize=fontsize, color=textcolor, fontweight='bold', wrap=True)

# ================================================================
# FIG 1: THE CKS KILL TIMELINE
# Type: Progression/Sequence
# Shows: The visceral scale of killing 363 papers — the collapse
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
ax.set_facecolor(BG)

days_build = np.arange(1, 46)
papers_build = np.linspace(8, 363, len(days_build))

for i, (d, p) in enumerate(zip(days_build, papers_build)):
    green_alpha = 0.3 + 0.5 * (i / len(days_build))
    ax.bar(d, p, width=0.8, color=GREEN, alpha=green_alpha, edgecolor=GREEN, linewidth=0.5)

ax.plot(46, 363, 'X', color=RED, markersize=28, markeredgewidth=3, zorder=10)
ax.text(46, 380, "Circular derivation\nfound", ha='center', va='bottom',
        fontsize=11, color=RED, fontweight='bold')

days_kill = [47, 48]
for d in days_kill:
    ax.bar(d, 5, width=0.8, color=DIM, alpha=0.5, edgecolor=DIM, linewidth=0.5)

ax.annotate('', xy=(46.5, 363), xytext=(47.5, 10),
            arrowprops=dict(arrowstyle='->', color=RED, lw=3, connectionstyle='arc3,rad=-0.3'))

ax.text(48, 50, "All 363 killed\non Zenodo", ha='center', va='bottom',
        fontsize=12, color=DIM, fontstyle='italic')

ax.text(44, 340, "363 papers", ha='right', va='top',
        fontsize=16, color=GREEN, fontweight='bold')

ax.text(48.5, 300, "The failure that\ntaught LEMU",
        ha='left', va='top', fontsize=13, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.8))

ax.set_xlim(0, 52)
ax.set_ylim(0, 420)
ax.set_xlabel("Days", fontsize=12, color=SILVER)
ax.set_ylabel("Papers Published", fontsize=12, color=SILVER)
ax.set_title("From 363 Papers to Zero: The CKS Kill",
             fontsize=17, fontweight='bold', color=GOLD, pad=15)
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "v01_cks_kill_timeline.png")

# ================================================================
# FIG 2: THE SMUGGLED ANSWER
# Type: Connection/Integer Map
# Shows: The circular derivation triangle — the loop IS the lie
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 9)

# Three boxes in a triangle
# Box A (top center) — Known answer
ax_a = (3.5, 7.0)
styled_box(ax, (ax_a[0], ax_a[1]), 4, 1.2, "", RED, alpha=0.2)
ax.text(ax_a[0]+2, ax_a[1]+0.6, "Known answer\n" + r"$\alpha$ = 1/137.036",
        ha='center', va='center', fontsize=13, color=RED, fontweight='bold')

# Box B (bottom left) — Derivation
bx_b = (0.5, 1.5)
styled_box(ax, (bx_b[0], bx_b[1]), 3.5, 1.2, "", CYAN, alpha=0.2)
ax.text(bx_b[0]+1.75, bx_b[1]+0.6, "Derivation\nfunction",
        ha='center', va='center', fontsize=13, color=CYAN, fontweight='bold')

# Box C (bottom right) — Output
cx_c = (7, 1.5)
styled_box(ax, (cx_c[0], cx_c[1]), 3.5, 1.2, "", GREEN, alpha=0.2)
ax.text(cx_c[0]+1.75, cx_c[1]+0.6, "Output\n" + r"$\alpha$ = 1/137.036",
        ha='center', va='center', fontsize=13, color=GREEN, fontweight='bold')

# Arrow A → B (smuggled)
ax.annotate('', xy=(1.5, 2.7), xytext=(4.0, 7.0),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5, linestyle='dashed',
                           connectionstyle='arc3,rad=0.2'))
ax.text(1.2, 5.2, 'smuggled in as\n"initial guess"', ha='center', va='center',
        fontsize=10, color=RED, rotation=55)

# Arrow B → C (labeled as derived)
ax.annotate('', xy=(7.0, 2.1), xytext=(4.0, 2.1),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
ax.text(5.5, 2.7, 'labeled as "derived"', ha='center', va='bottom',
        fontsize=10, color=GREEN)

# Arrow C → A (matches!)
ax.annotate('', xy=(7.0, 7.2), xytext=(9.5, 2.7),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5, linestyle='dotted',
                           connectionstyle='arc3,rad=-0.2'))
ax.text(9.5, 5.2, '"matches!"\n(of course it does)', ha='center', va='center',
        fontsize=10, color=GOLD, rotation=-55)

# Title and annotation
ax.text(5.5, 9.0, "How a Circular Derivation Hides",
        ha='center', va='top', fontsize=17, color=GOLD, fontweight='bold')
ax.text(5.5, 0.3, "The loop is the lie. The output was never derived \u2014 it was copied.",
        ha='center', va='bottom', fontsize=12, color=SILVER, fontstyle='italic')

save(fig, "v02_smuggled_answer.png")

# ================================================================
# FIG 3: WHAT DECIMALS DESTROY
# Type: Comparison Bar (side by side)
# Shows: The visual death when fractions become decimals
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.35})

for ax in [ax1, ax2]:
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

# Left panel — Fractions (alive)
labels_l = [r'$b_1 = 41/10$', r'$b_2 = -19/6$', r'$b_3 = -7/1$']
values_l = [41/10, 19/6, 7]
meanings = ["41 counts U(1) charges", "19 counts SU(2) charges", "7 = 11 gluons \u2212 4 quarks"]
y_pos = [2, 1, 0]

ax1.barh(y_pos, values_l, height=0.55, color=GOLD, alpha=0.75, edgecolor=GOLD, linewidth=2)
for i, (y, v, m) in enumerate(zip(y_pos, values_l, meanings)):
    ax1.text(v + 0.2, y, m, va='center', fontsize=10, color=WHITE, fontweight='bold')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(labels_l, fontsize=13, color=GOLD, fontweight='bold')
ax1.set_xlim(0, 12)
ax1.set_title("As a Fraction (exact)", fontsize=15, color=GOLD, fontweight='bold', pad=12)
ax1.tick_params(axis='x', colors=DIM, labelsize=9)
ax1.set_xlabel("Magnitude", fontsize=11, color=SILVER)

# Right panel — Decimals (dead)
labels_r = ['4.1', '\u22123.1667', '\u22127.0']
values_r = [4.1, 3.1667, 7.0]
dead_notes = ["counts nothing", "counts nothing", "accidentally still integer"]

ax2.barh(y_pos, values_r, height=0.55, color=DIM, alpha=0.4, edgecolor=DIM, linewidth=2)
for i, (y, v, m) in enumerate(zip(y_pos, values_r, dead_notes)):
    ax2.text(v + 0.2, y, m, va='center', fontsize=10, color=DIM, fontstyle='italic')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(labels_r, fontsize=13, color=DIM)
ax2.set_xlim(0, 12)
ax2.set_title("As a Decimal (dead)", fontsize=15, color=DIM, pad=12)
ax2.tick_params(axis='x', colors=DIM, labelsize=9)
ax2.set_xlabel("Magnitude", fontsize=11, color=SILVER)

fig.suptitle("The Same Number, Two Representations",
             fontsize=17, color=WHITE, fontweight='bold', y=0.98)
fig.text(0.5, 0.02, "The integers ARE the physics. The decimals are a lossy format.",
         ha='center', fontsize=13, color=SILVER, fontstyle='italic')

save(fig, "v03_decimals_destroy.png")

# ================================================================
# FIG 4: Q335 PRECISION SCALE
# Type: Scale/Landscape
# Shows: The absurd overkill — 65 digits past Planck
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
ax.set_facecolor(BG)

# Three segments of the precision bar
ax.barh(1, 15, left=0, height=0.6, color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=1.5)
ax.barh(1, 20, left=15, height=0.6, color=GREEN, alpha=0.7, edgecolor=GREEN, linewidth=1.5)
ax.barh(1, 65, left=35, height=0.6, color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=1.5)

# Planck wall
ax.axvline(x=35, color=RED, linewidth=4, linestyle='-', alpha=0.9, zorder=10)
ax.text(35, 2.0, "PLANCK\nTHRESHOLD", ha='center', va='bottom',
        fontsize=14, color=RED, fontweight='bold')
ax.text(35, 1.85, "Nothing smaller exists", ha='center', va='top',
        fontsize=10, color=RED, alpha=0.8)

# Landmarks
ax.annotate("Your calculator\n(double float)", xy=(15, 0.7), xytext=(10, 0.0),
            fontsize=10, color=CYAN, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax.annotate("Q335 " + r"$\pi$" + "\n(what we use)", xy=(100, 1.0), xytext=(90, 2.2),
            fontsize=12, color=GOLD, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# The overkill annotation
ax.annotate('', xy=(35, 0.5), xytext=(100, 0.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(67.5, 0.2, "65 digits beyond the smallest\nthing in the universe",
        ha='center', va='top', fontsize=12, color=GOLD, fontweight='bold')

ax.set_xlim(-5, 108)
ax.set_ylim(-0.5, 2.8)
ax.set_xlabel("Number of Correct Digits", fontsize=12, color=SILVER)
ax.set_yticks([])
ax.set_title("How Many Digits Do You Need?",
             fontsize=17, fontweight='bold', color=GOLD, pad=15)
ax.tick_params(colors=DIM, labelsize=10)
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color(DIM)
ax.spines['bottom'].set_linewidth(0.5)

# Tick marks at key positions
ax.set_xticks([0, 15, 35, 50, 75, 100])

save(fig, "v04_q335_precision.png")

# ================================================================
# FIG 5: THE THREE NOUNS
# Type: Geometric Cross-Section (3 panels)
# Shows: Inertia, vortex, soliton as spatial objects
# ================================================================

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 8), facecolor=BG,
                                     gridspec_kw={'wspace': 0.25})

for ax in [ax1, ax2, ax3]:
    ax.set_facecolor(BG)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

# Panel 1: INERTIA — ball resisting a push
ball = Circle((0.2, 0), 0.5, facecolor=ORANGE, edgecolor=WHITE, linewidth=2, alpha=0.6)
ax1.add_patch(ball)
# Force arrow
ax1.annotate('', xy=(-0.1, 0), xytext=(-1.2, 0),
             arrowprops=dict(arrowstyle='->', color=WHITE, lw=3))
ax1.text(-1.2, 0.3, "Force", ha='left', fontsize=11, color=WHITE)
# Tiny resistance arrow
ax1.annotate('', xy=(0.5, 0), xytext=(0.9, 0),
             arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
ax1.text(0.9, 0.25, "resists", ha='left', fontsize=10, color=ORANGE, fontstyle='italic')
ax1.set_title("Inertia", fontsize=15, color=ORANGE, fontweight='bold', pad=10)
ax1.text(0, -1.2, "m = F/a\nMass is resistance,\nnot substance",
         ha='center', fontsize=9, color=SILVER)

# Panel 2: VORTEX — circular flow
theta = np.linspace(0, 2*np.pi, 100)
r_vortex = 0.7
ax2.plot(r_vortex*np.cos(theta), r_vortex*np.sin(theta), color=CYAN, lw=2, alpha=0.4)
n_arrows = 8
for i in range(n_arrows):
    t = 2*np.pi*i/n_arrows
    x = r_vortex*np.cos(t)
    y = r_vortex*np.sin(t)
    dx = -0.25*np.sin(t)
    dy = 0.25*np.cos(t)
    ax2.annotate('', xy=(x+dx, y+dy), xytext=(x, y),
                 arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax2.set_title("Vortex", fontsize=15, color=CYAN, fontweight='bold', pad=10)
ax2.text(0, -1.2, "A self-sustaining\ncirculation pattern.\nElectron. Proton. Galaxy.",
         ha='center', fontsize=9, color=SILVER)

# Panel 3: SOLITON BOUNDARY — inside/outside
outer = Circle((0, 0), 1.0, facecolor=BLUE, edgecolor=GOLD, linewidth=3, alpha=0.15)
inner = Circle((0, 0), 0.6, facecolor=RED, edgecolor='none', alpha=0.25)
ax3.add_patch(outer)
ax3.add_patch(inner)
boundary = Circle((0, 0), 0.8, facecolor='none', edgecolor=GOLD, linewidth=3, linestyle='--')
ax3.add_patch(boundary)
ax3.text(0, 0, r"$\alpha_s \approx 1$" + "\ninside", ha='center', va='center',
         fontsize=10, color=RED, fontweight='bold')
ax3.text(0, 1.2, r"$\alpha_s = 0.118$" + "\noutside", ha='center', va='center',
         fontsize=10, color=BLUE, fontweight='bold')
ax3.set_title("Soliton Boundary", fontsize=15, color=GOLD, fontweight='bold', pad=10)
ax3.text(0, -1.2, "The boundary where\nreadings change.\nCross it: different physics.",
         ha='center', fontsize=9, color=SILVER)

fig.suptitle("Three Nouns: The Complete Vocabulary of Structure",
             fontsize=17, color=WHITE, fontweight='bold', y=0.98)

save(fig, "v05_three_nouns.png")

# ================================================================
# FIG 6: THE TWO VERBS — READING AND RUNNING
# Type: Running/Convergence
# Shows: A dot (reading) vs a curve (running reading)
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(BG)

# alpha_s running curve (one-loop approximate)
log_mu = np.linspace(0, 16, 500)  # log10(E/GeV)
b3 = -7
alpha_s_inv_mz = 1.0 / 0.118
log_mz = np.log10(91.2)

alpha_s_inv = alpha_s_inv_mz - b3/(2*np.pi) * (log_mu - log_mz) * np.log(10)
alpha_s = np.where(alpha_s_inv > 0.5, 1.0/alpha_s_inv, np.nan)

# Clip to reasonable range
mask = (alpha_s > 0) & (alpha_s < 1.5)
ax.plot(log_mu[mask], alpha_s[mask], color=CYAN, lw=2.5, label="Running reading (the movie)", zorder=5)

# The reading — single dot at M_Z
ax.scatter([log_mz], [0.118], s=250, color=GOLD, edgecolor=WHITE, linewidth=2, zorder=10)
ax.annotate(r"$\alpha_s$ = 0.118 at $M_Z$" + "\nOne number. One place.",
            xy=(log_mz, 0.118), xytext=(log_mz + 2.5, 0.25),
            fontsize=12, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# # Landmarks
# landmarks = [(0, r"$\Lambda_{QCD}$" + "\n~0.2 GeV", RED),
#              (np.log10(0.938), "proton", GREEN),
#              (log_mz, r"$M_Z$" + "\n91 GeV", SILVER),
#              (15.5, "GUT\nscale", PURPLE)]
# for lx, ltxt, lc in landmarks:
#     ax.axvline(x=lx, color=lc, alpha=0.3, linestyle='--', linewidth=1)
#     ax.text(lx, 1.35, ltxt, ha='center', va='top', fontsize=9, color=lc)

landmarks = [(0, r"$\Lambda_{QCD}$" + "\n~0.2 GeV", RED),
             (np.log10(0.938), "proton", GREEN),
             (log_mz, r"$M_Z$" + "\n91 GeV", SILVER),
             (15.5, "GUT\nscale", PURPLE)]
for lx, ltxt, lc in landmarks:
    ax.axvline(x=lx, color=lc, alpha=0.3, linestyle='--', linewidth=1)
    if ltxt == "proton":
        ax.text(lx, 1.55, ltxt, ha='center', va='top', fontsize=9, color=lc)
    else:
        ax.text(lx, 1.35, ltxt, ha='center', va='top', fontsize=9, color=lc)

ax.text(3, 0.85, "Same force.\nDifferent reading\nat every scale.",
        fontsize=14, color=CYAN, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, alpha=0.6))

ax.set_xlim(-1, 17)
ax.set_ylim(0, 1.5)
ax.set_xlabel(r"Energy scale: $\log_{10}(E/\mathrm{GeV})$", fontsize=12, color=SILVER)
ax.set_ylabel(r"$\alpha_s$ (strong coupling)", fontsize=12, color=SILVER)
ax.set_title("Reading vs Running Reading",
             fontsize=17, fontweight='bold', color=GOLD, pad=15)
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.text(14, 0.1, "A reading is a snapshot.\nA running reading is the whole movie.",
        ha='right', va='bottom', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "v06_reading_vs_running.png")

# ================================================================
# FIG 7: THE NESTING — CONCENTRIC CIRCLES
# Type: Geometric Cross-Section
# Shows: 8 levels deep, the geometry IS the hierarchy
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-8, 12)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.axis('off')

levels = [
    (6.5, "Universe", PURPLE, 0.08, r"$10^{26}$ m"),
    (5.5, "Galaxy", DIM, 0.12, r"$10^{21}$ m"),
    (4.5, "Star (Sun)", ORANGE, 0.15, r"$10^{9}$ m"),
    (3.5, "Planet (Earth)", GREEN, 0.18, r"$10^{7}$ m"),
    (2.5, "Atom", BLUE, 0.22, r"$10^{-10}$ m"),
    (1.5, "Nucleus", RED, 0.28, r"$10^{-15}$ m"),
    (0.8, "Proton", MAG, 0.40, r"$10^{-15}$ m"),
    (0.3, "Quark", CYAN, 0.60, r"$< 10^{-18}$ m"),
]

for radius, name, color, alpha, scale in levels:
    circ = Circle((0, 0), radius, facecolor=color, edgecolor=color,
                  alpha=alpha, linewidth=2)
    ax.add_patch(circ)

# Labels on the right side with leader lines
for i, (radius, name, color, alpha, scale) in enumerate(levels):
    label_x = 8.0
    label_y = 6.5 - i * 1.6
    # Leader line from circle edge to label
    edge_x = radius * 0.95
    edge_y = label_y * (radius / 6.5) if abs(label_y) < radius else 0
    ax.plot([radius, label_x - 0.1], [edge_y, label_y], color=color, alpha=0.5, lw=1)
    ax.text(label_x, label_y, "%s  %s" % (name, scale), ha='left', va='center',
            fontsize=11, color=color, fontweight='bold')

# Flat/curved annotations
ax.text(0, -7.2, '"Inside reads flat. Outside reads curved.\nEvery level. Every scale. No exceptions."',
        ha='center', va='center', fontsize=12, color=SILVER, fontstyle='italic')

ax.set_title("The Nesting: Every Level Is a Boundary",
             fontsize=17, fontweight='bold', color=GOLD, pad=15,
             position=(0.5, 1.0))

save(fig, "v07_nesting.png")

# ================================================================
# FIG 8: FLAT INSIDE, CURVED OUTSIDE
# Type: Geometric Cross-Section (side by side)
# Shows: The perceptual flip — same surface, different reading
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.25})

for ax in [ax1, ax2]:
    ax.set_facecolor(BG)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 2)
    ax.set_aspect('equal')
    ax.axis('off')

# Left panel: INSIDE — flat grid, person standing
# Draw flat ground
for i in range(-4, 5):
    ax1.plot([i*0.5, i*0.5], [-0.05, 0.0], color=GREEN, alpha=0.4, lw=1)
ax1.plot([-2, 2], [0, 0], color=GREEN, lw=2, alpha=0.6)
for i in range(1, 6):
    ax1.plot([-2, 2], [0, 0], color=GREEN, alpha=0.1, lw=1)

# Horizon line
ax1.plot([-2, 2], [0.8, 0.8], color=GREEN, alpha=0.2, lw=1, linestyle='--')
ax1.text(0, 0.9, "horizon", ha='center', fontsize=9, color=GREEN, alpha=0.5)

# Grid lines (flat)
for x in np.linspace(-1.8, 1.8, 9):
    ax1.plot([x, x], [0, 0.6], color=GREEN, alpha=0.15, lw=1)
for y in np.linspace(0, 0.6, 4):
    ax1.plot([-1.8, 1.8], [y, y], color=GREEN, alpha=0.15, lw=1)

# Stick figure
ax1.plot([0, 0], [0, 0.5], color=WHITE, lw=2)  # body
ax1.plot([-0.15, 0.15], [0.3, 0.3], color=WHITE, lw=2)  # arms
ax1.scatter([0], [0.55], s=100, color=WHITE, zorder=10)  # head
ax1.plot([-0.1, 0], [0, 0.15], color=WHITE, lw=2)  # legs
ax1.plot([0.1, 0], [0, 0.15], color=WHITE, lw=2)

ax1.set_title("INSIDE: Flat", fontsize=15, color=GREEN, fontweight='bold', pad=10)
ax1.text(0, -0.5, "Standing on Earth: FLAT\nStanding in the universe: FLAT\nInside always reads flat",
         ha='center', fontsize=10, color=GREEN)

# Right panel: OUTSIDE — curved surface, seen from space
theta = np.linspace(-np.pi/2.5, np.pi/2.5, 100)
r_earth = 1.3
ax2.plot(r_earth*np.cos(theta), r_earth*np.sin(theta) - 0.3, color=CYAN, lw=3)

# Curved grid lines
for frac in [0.85, 0.9, 0.95, 1.0, 1.05]:
    ax2.plot(frac*r_earth*np.cos(theta), frac*r_earth*np.sin(theta) - 0.3,
             color=CYAN, alpha=0.12, lw=1)
for t_mark in np.linspace(-np.pi/3, np.pi/3, 7):
    x_s = 0.85*r_earth*np.cos(t_mark)
    y_s = 0.85*r_earth*np.sin(t_mark) - 0.3
    x_e = 1.05*r_earth*np.cos(t_mark)
    y_e = 1.05*r_earth*np.sin(t_mark) - 0.3
    ax2.plot([x_s, x_e], [y_s, y_e], color=CYAN, alpha=0.12, lw=1)

# Observer dot in space
ax2.scatter([0], [1.8], s=80, color=WHITE, zorder=10)
ax2.text(0.15, 1.75, "observer", ha='left', fontsize=9, color=WHITE, alpha=0.7)

ax2.set_title("OUTSIDE: Curved", fontsize=15, color=CYAN, fontweight='bold', pad=10)
ax2.text(0, -1.2, "Orbiting Earth: CURVED\nOutside the universe: CURVED\nOutside always reads curved",
         ha='center', fontsize=10, color=CYAN)

fig.suptitle("Same Surface, Different Reading",
             fontsize=17, color=WHITE, fontweight='bold', y=0.98)
fig.text(0.5, 0.02,
         "The flatness problem isn't a problem. You're inside. Insides read flat. That's what boundaries do.",
         ha='center', fontsize=12, color=SILVER, fontstyle='italic')

save(fig, "v08_flat_curved.png")

# ================================================================
# FIG 9: THE INTEGER DECOMPOSITION OF (22/13)pi
# Type: Connection/Integer Map (tree)
# Shows: Each integer has a named origin — the tree makes assembly visible
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)

# Top: Yang-Mills = 11
styled_box(ax, (6.5, 10), 5, 1.0, "Yang-Mills coefficient = 11\nGluon self-interactions (1973)", GOLD, fontsize=11, alpha=0.3)

# Left branch: x2 → 22
ax.annotate('', xy=(5.5, 8.5), xytext=(7.5, 10.0),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5))
ax.text(5.5, 9.4, r"$\times$ 2", fontsize=12, color=CYAN, fontweight='bold', ha='center')
ax.text(4.5, 9.0, "(vector-like:\nboth hands)", fontsize=9, color=CYAN, ha='center')
styled_box(ax, (3.5, 7.5), 3.5, 1.0, "22", CYAN, fontsize=18, alpha=0.3)

# Right branch: b2 numerator = 13
ax.annotate('', xy=(12.5, 8.5), xytext=(10.5, 10.0),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
ax.text(12.5, 9.4, r"$b_2'$ numerator", fontsize=10, color=GREEN, fontweight='bold', ha='center')
styled_box(ax, (11, 7.5), 3.5, 1.0, "13", GREEN, fontsize=18, alpha=0.3)

# Merge: 22/13
ax.annotate('', xy=(9, 6.2), xytext=(5.25, 7.5),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))
ax.annotate('', xy=(9, 6.2), xytext=(12.75, 7.5),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))
styled_box(ax, (6.5, 5.2), 5, 1.0, "22/13 = 1.6923...", WHITE, fontsize=14, alpha=0.15)

# Multiply by pi
ax.annotate('', xy=(9, 4.0), xytext=(9, 5.2),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.text(10, 4.6, r"$\times\;\pi$" + "\n(toroidal\ncross-section)", fontsize=10,
        color=GOLD, ha='left', fontweight='bold')
styled_box(ax, (5.5, 2.8), 7, 1.2, r"$(22/13)\pi$ = 5.3165", GOLD, fontsize=16, alpha=0.3)

# Comparison to measurement
ax.annotate('', xy=(9, 1.5), xytext=(9, 2.8),
            arrowprops=dict(arrowstyle='->', color=MAG, lw=2))
styled_box(ax, (5.5, 0.5), 7, 1.0, "Planck satellite measures: 5.3204", MAG, fontsize=13, alpha=0.25)

# Miss annotation
ax.text(14, 1.0, "725 ppm", fontsize=14, color=SILVER, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=SILVER))

ax.text(9, 11.8, r"Where $(22/13)\pi$ Comes From",
        ha='center', fontsize=17, color=GOLD, fontweight='bold')

save(fig, "v09_dm_ratio_tree.png")

# ================================================================
# FIG 10: 725 PPM — WHAT DOES THAT MISS LOOK LIKE?
# Type: Comparison Bar with zoom inset
# Shows: The smallness of the miss — identical until you zoom in
# ================================================================

fig = plt.figure(figsize=(16, 10), facecolor=BG)

# Main axes — full bars
ax_main = fig.add_axes([0.08, 0.35, 0.84, 0.50], facecolor=BG)

measured = 5.3204
predicted = 5.3165

ax_main.barh([1.3], [measured], height=0.35, color=MAG, alpha=0.7,
             edgecolor=MAG, linewidth=2, label="Measured (Planck)")
ax_main.barh([0.7], [predicted], height=0.35, color=GOLD, alpha=0.7,
             edgecolor=GOLD, linewidth=2, label="Predicted (22/13)" + r"$\pi$")

ax_main.set_xlim(0, 6)
ax_main.set_ylim(0.2, 1.85)
ax_main.set_yticks([0.7, 1.3])
ax_main.set_yticklabels(["Predicted", "Measured"], fontsize=12, color=WHITE)
ax_main.set_xlabel("Dark matter / baryon ratio", fontsize=12, color=SILVER)
ax_main.tick_params(colors=DIM, labelsize=9)
for spine in ax_main.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

# Zoom indicator rectangle
zoom_left = 5.28
zoom_right = 5.36
rect = mpatches.Rectangle((zoom_left, 0.45), zoom_right - zoom_left, 1.25,
                            linewidth=2, edgecolor=SILVER, facecolor='none', linestyle='--', alpha=0.5)
ax_main.add_patch(rect)

ax_main.legend(loc='upper left', fontsize=10, facecolor=PAN, edgecolor=DIM,
               labelcolor=WHITE)

# Zoom inset axes
ax_zoom = fig.add_axes([0.25, 0.05, 0.50, 0.25], facecolor=PAN)

ax_zoom.barh([1.3], [measured], height=0.35, color=MAG, alpha=0.7,
             edgecolor=MAG, linewidth=2)
ax_zoom.barh([0.7], [predicted], height=0.35, color=GOLD, alpha=0.7,
             edgecolor=GOLD, linewidth=2)

ax_zoom.set_xlim(5.28, 5.36)
ax_zoom.set_ylim(0.35, 1.75)
ax_zoom.set_yticks([0.7, 1.3])
ax_zoom.set_yticklabels(["", ""], fontsize=9)
ax_zoom.tick_params(colors=DIM, labelsize=8)
for spine in ax_zoom.spines.values():
    spine.set_color(SILVER)
    spine.set_linewidth(1)

# Gap annotation in zoom
gap = measured - predicted
ax_zoom.annotate('', xy=(predicted, 1.0), xytext=(measured, 1.0),
                 arrowprops=dict(arrowstyle='<->', color=WHITE, lw=2))
ax_zoom.text((predicted + measured)/2, 1.15, "0.0039\n725 ppm",
             ha='center', va='bottom', fontsize=11, color=WHITE, fontweight='bold')

ax_zoom.text(5.29, 0.5, "ZOOMED", fontsize=9, color=SILVER, fontstyle='italic')

# Scale comparisons below
fig.text(0.5, 0.01,
         "1 second in 23 minutes  |  1 meter in 1.38 km  |  human hair vs football field",
         ha='center', fontsize=11, color=DIM)

fig.suptitle("How Close Is 725 Parts Per Million?",
             fontsize=17, color=GOLD, fontweight='bold', y=0.97)

save(fig, "v10_725ppm_zoom.png")

# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides generated ===")
filenames = [
    "v01_cks_kill_timeline.png",
    "v02_smuggled_answer.png",
    "v03_decimals_destroy.png",
    "v04_q335_precision.png",
    "v05_three_nouns.png",
    "v06_reading_vs_running.png",
    "v07_nesting.png",
    "v08_flat_curved.png",
    "v09_dm_ratio_tree.png",
    "v10_725ppm_zoom.png",
]
for f in filenames:
    print("  %s" % f)
print("Total: %d figures" % len(filenames))
