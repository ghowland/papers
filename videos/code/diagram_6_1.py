#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 6, Slides 11-20
10 figures covering: kill switch anatomy, statistical block,
graveyard of dead ends, program status map, provenance chain,
version control comparison, 253 comparisons domain map,
precision staircase sorted, complete system architecture,
physics vs software practices.
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
# FIG 11: KILL SWITCH ANATOMY
# Type: Identity Card
# Shows: three concrete kill switches with named experiments
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 12)

ax.text(5, 11.2, "What a Kill Switch Looks Like",
        ha='center', va='center', fontsize=18, fontweight='bold', color=GOLD)

# Program header
rounded_box(ax, 5, 9.8, 8, 1.0, "program_beta_unification_v0", GOLD,
            fontsize=13, alpha=0.2)

# Three kill switches
switches = [
    ("coincidence_probability",
     "p > 0.1 for observed\ninteger matches",
     "combinatoric analysis",
     7.5),
    ("cmb_s4_omega",
     r"$\Omega_{DM}$ moves away from" + "\n44/169 with CMB-S4 data",
     "CMB-S4 / LiteBIRD",
     5.0),
    ("lhc_no_cd",
     "LHC excludes CD at all\nmasses up to 6 TeV",
     "LHC Run 3 + HL-LHC",
     2.5),
]

for i, (name, condition, source, sy) in enumerate(switches):
    # Kill switch card
    card = mpatches.FancyBboxPatch((0.5, sy - 1.0), 9.0, 2.0,
        boxstyle="round,pad=0.15", facecolor=BG, alpha=0.8,
        linewidth=2)
    ax.add_patch(card)

    # Red left border
    ax.plot([0.5, 0.5], [sy - 1.0, sy + 1.0], color=RED, linewidth=4, alpha=0.7)

    # Skull/X icon
    ax.text(1.3, sy + 0.5, r"$\times$", ha='center', va='center',
            fontsize=18, color=RED, fontweight='bold')

    # Fields
    ax.text(2.5, sy + 0.5, "name:", ha='left', va='center', fontsize=9, color=SILVER)
    ax.text(4.0, sy + 0.5, name, ha='left', va='center', fontsize=10,
            color=RED, fontweight='bold')

    ax.text(2.5, sy - 0.1, "condition:", ha='left', va='center', fontsize=9, color=SILVER)
    ax.text(4.5, sy - 0.1, condition, ha='left', va='center', fontsize=9,
            color=WHITE)

    ax.text(2.5, sy - 0.65, "data source:", ha='left', va='center', fontsize=9, color=SILVER)
    ax.text(4.5, sy - 0.65, source, ha='left', va='center', fontsize=9,
            color=CYAN)

ax.text(5, 0.5, "Pre-registered failure conditions. Not vague. Not movable.\n"
        "Named experiments, named thresholds, named consequences.\n"
        "If the condition is met, the program dies.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_11_kill_switch_anatomy.png")


# ================================================================
# FIG 12: THE STATISTICAL BLOCK
# Type: Threshold/Region
# Shows: p = 0.81 dot in the red zone — own system blocks own claim
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Horizontal p-value scale
p_vals = np.linspace(0, 1, 200)

# Shaded zones
ax.axvspan(0, 0.1, color=GREEN, alpha=0.08)
ax.axvspan(0.1, 1.0, color=RED, alpha=0.06)

# Threshold line
ax.axvline(x=0.1, color=GREEN, linewidth=2.5, linestyle='--', alpha=0.7)
ax.text(0.1, 0.85, "threshold\np = 0.1", ha='center', va='center',
        fontsize=10, color=GREEN, fontweight='bold')

# Zone labels
ax.text(0.05, 0.65, "CLEAR\nwould allow\nclaim to\nadvance", ha='center', va='center',
        fontsize=10, color=GREEN, fontstyle='italic')
ax.text(0.55, 0.65, "BLOCKED\nclaim cannot advance\nuntil statistics resolved", ha='center',
        va='center', fontsize=11, color=RED, fontstyle='italic')

# Measured p dot
ax.scatter([0.81], [0.4], s=400, color=RED, zorder=5, marker='o')
ax.text(0.81, 0.52, "p = 0.81", ha='center', va='bottom', fontsize=14,
        color=RED, fontweight='bold')
ax.text(0.81, 0.28, "Random integers match\n81% of the time", ha='center', va='top',
        fontsize=9, color=SILVER)

# Status
ax.text(0.5, 0.1, "Status: BLOCKING", ha='center', va='center',
        fontsize=18, color=RED, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlabel("p-value (probability of coincidence)", fontsize=11, color=SILVER)
ax.set_title("The Statistical Control: My Own System Blocks My Own Claim",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0.0, 0.95)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk6_12_statistical_block.png")


# ================================================================
# FIG 13: THE GRAVEYARD — SIX DOCUMENTED DEAD ENDS
# Type: Comparison Bar
# Shows: wall of red — six killed paths, all documented
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

killed = [
    ("SM unification\n(no CD)", "Gap 218/115 misses\nby 40%", "Not a small\ninteger ratio"),
    ("PSLQ search\nfor relations", "82/82 null", "No integer\nrelations exist"),
    ("Koide phase\nadjustment", "Identity proof", "Mathematical\nimpossibility"),
    ("Fermion\ngap fix", "Democracy zeroes it", "Generation democracy\ncancels correction"),
    ("Lambda\none-eighth", "Corrections wrong\ndirection", "Sign error in\ncorrection"),
    ("Hubble VP\nprediction", r"$N_{VP}$ = 0.71 < 1", "VP step too large\nfor boundary"),
]

y = np.arange(len(killed))

for i, (name, evidence, cause) in enumerate(killed):
    # Red bar
    ax.barh(y[i], 1.0, height=0.5, color=RED, alpha=0.4)

    # Name
    ax.text(0.02, y[i], name, ha='left', va='center', fontsize=9,
            color=RED, fontweight='bold')

    # Evidence
    ax.text(1.15, y[i] + 0.1, evidence, ha='left', va='center', fontsize=8,
            color=SILVER)

    # Cause of death
    ax.text(1.15, y[i] - 0.15, cause, ha='left', va='center', fontsize=7,
            color=DIM, fontstyle='italic')

    # KILLED stamp
    ax.text(2.8, y[i], "KILLED", ha='center', va='center', fontsize=10,
            color=RED, fontweight='bold', alpha=0.7)

ax.set_title("Killed Research Paths: Documented Dead Ends",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(1.5, -0.9, "The dead ends are as valuable as the successes.\n"
        "They save the next person from trying the same thing.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(-0.1, 3.5)
ax.set_ylim(-1.3, len(killed) - 0.3)
ax.set_xticks([])
ax.set_yticks([])
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk6_13_graveyard.png")


# ================================================================
# FIG 14: ALIVE VS KILLED VS BLOCKED — PROGRAM STATUS MAP
# Type: Comparison Bar (grid)
# Shows: balanced ratio of alive and killed — kills as many as keeps
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 10)

ax.text(7, 9.3, "Every Research Program: Alive, Killed, or Blocked",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# ACTIVE programs
active = ["beta\nunification", "toroidal\nDM", "hubble\nrunning",
          "GR reading\ndepth", "clock\ndecomposition", "confinement\nboundary"]

ax.text(3.5, 8.0, "ACTIVE (6)", ha='center', va='center', fontsize=12,
        color=GREEN, fontweight='bold')
for i, name in enumerate(active):
    col_idx = i % 3
    row_idx = i // 3
    x = 1.5 + col_idx * 2.2
    y = 7.0 - row_idx * 1.8
    rounded_box(ax, x, y, 1.9, 1.2, name, GREEN, fontsize=8, alpha=0.15)

# KILLED programs
killed_names = ["hubble VP\nprediction", "SM unification\n(no CD)", "PSLQ\nsearch",
                "Koide\nphase", "fermion\ngap", "lambda\n1/8"]

ax.text(10.5, 8.0, "KILLED (6)", ha='center', va='center', fontsize=12,
        color=RED, fontweight='bold')
for i, name in enumerate(killed_names):
    col_idx = i % 3
    row_idx = i // 3
    x = 8.5 + col_idx * 2.2
    y = 7.0 - row_idx * 1.8
    rounded_box(ax, x, y, 1.9, 1.2, name, RED, fontsize=8, alpha=0.12)

# BLOCKED program
ax.text(7, 2.5, "BLOCKED (1)", ha='center', va='center', fontsize=12,
        color=ORANGE, fontweight='bold')
rounded_box(ax, 7, 1.5, 3.5, 1.0, "statistical control\np = 0.81", ORANGE,
            fontsize=9, alpha=0.2)

ax.text(7, -0.3, "6 alive. 6 killed. 1 blocked.\n"
        "Every program has a status. Every status has a reason.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_14_program_status_map.png")


# ================================================================
# FIG 15: TRACING A RESULT BACK TO ITS SOURCE
# Type: Progression/Sequence (right to left)
# Shows: five links from prediction back to original measurement
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "Chain of Custody: Result to Measurement",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

links = [
    (13.5, 3.5, "RESULT", r"sin$^2\theta_W$" + "\n= 0.231223", GOLD),
    (10.5, 3.5, "DERIVATION", "sin2_from_\none_loop_\ncrossing_v0", CYAN),
    (7.5, 3.5, "INPUTS", r"$\alpha^{-1}$ = 137.036..." + "\n" + r"$\beta$" + " = 25/6, ...", GREEN),
    (4.5, 3.5, "SOURCE", "CODATA 2018\ngroup theory", BLUE),
    (1.5, 3.5, "MEASUREMENT", "Parker 2018\nMorel 2020\nLie algebra", MAG),
]

for i, (lx, ly, ltitle, ldesc, lcol) in enumerate(links):
    rounded_box(ax, lx, ly, 2.5, 2.5, "", lcol, alpha=0.15)
    ax.text(lx, ly + 0.7, ltitle, ha='center', va='center', fontsize=9,
            color=lcol, fontweight='bold')
    ax.text(lx, ly - 0.3, ldesc, ha='center', va='center', fontsize=8,
            color=SILVER)

    # Backward arrow
    if i < len(links) - 1:
        nx = links[i+1][0]
        ax.annotate("", xy=(nx + 1.4, ly), xytext=(lx - 1.4, ly),
                    arrowprops=dict(arrowstyle='<-', color=GOLD, lw=2, alpha=0.5))

# Arrow labels
arrow_labels = ["produced by", "from inputs", "sourced from", "measured by"]
for i, albl in enumerate(arrow_labels):
    mid_x = (links[i][0] + links[i+1][0]) / 2
    ax.text(mid_x, 4.9, albl, ha='center', va='center', fontsize=7,
            color=DIM, fontstyle='italic')

ax.text(8, 0.5, "Every number has a return address. Every derivation is a chain of custody.\n"
        "If a measurement improves, swap one JSON node and rerun.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_15_provenance_chain.png")


# ================================================================
# FIG 16: VERSION CONTROL FOR PHYSICS
# Type: Comparison Bar (two panels)
# Shows: long manual update chain vs short automated one
# ================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 9),
                                gridspec_kw={'hspace': 0.35})
fig.patch.set_facecolor(BG)
fig.suptitle("When a Measurement Improves",
             fontsize=17, fontweight='bold', color=GOLD, y=0.97)

# -- Top: Standard physics (long, manual) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 16)
ax1.set_ylim(0, 4)

ax1.text(0.5, 3.3, "Standard Physics", ha='left', va='center',
         fontsize=12, fontweight='bold', color=DIM)

std_steps = [
    (1.5, 1.8, "Old\npaper"),
    (4.0, 1.8, "New\npaper"),
    (6.5, 1.8, "Manually\nupdate\ndownstream"),
    (9.0, 1.8, "Hope you\ndidn't\nmiss one"),
    (11.5, 1.8, "Publish\ncorrection"),
    (14.0, 1.8, "Wait 6\nmonths"),
]
for i, (sx, sy, stxt) in enumerate(std_steps):
    rounded_box(ax1, sx, sy, 2.0, 1.2, stxt, DIM, fontsize=8, alpha=0.1)
    if i < len(std_steps) - 1:
        nx = std_steps[i+1][0]
        ax1.annotate("", xy=(nx - 1.1, sy), xytext=(sx + 1.1, sy),
                     arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, alpha=0.4))

ax1.text(8, 0.5, "Manual. Error-prone. Months.", ha='center', va='center',
         fontsize=9, color=DIM, fontstyle='italic')

# -- Bottom: RUM (short, automated) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 4)

ax2.text(0.5, 3.3, "RUM", ha='left', va='center',
         fontsize=12, fontweight='bold', color=GREEN)

rum_steps = [
    (2.5, 1.8, "Swap one\nJSON node"),
    (6.0, 1.8, "Rerun all\nexperiments"),
    (9.5, 1.8, "Every result\nupdates\nautomatically"),
    (13.0, 1.8, "PASS/FAIL\nin 30 seconds"),
]
rum_cols = [GOLD, CYAN, GREEN, GREEN]
for i, (sx, sy, stxt) in enumerate(rum_steps):
    rounded_box(ax2, sx, sy, 2.5, 1.2, stxt, rum_cols[i], fontsize=9, alpha=0.15)
    if i < len(rum_steps) - 1:
        nx = rum_steps[i+1][0]
        ax2.annotate("", xy=(nx - 1.4, sy), xytext=(sx + 1.4, sy),
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax2.text(8, 0.5, "Automated. Traceable. Seconds.", ha='center', va='center',
         fontsize=9, color=GREEN, fontstyle='italic')

save(fig, "talk6_16_version_control.png")


# ================================================================
# FIG 17: 253 COMPARISONS — DOMAIN MAP
# Type: Comparison Bar (stacked by domain)
# Shows: overwhelmingly green across nine domains
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

domains = ["QED", "EW", "GUT", "Cosmo", "BBN", "Muon\ng-2", "CKM", "Mass/\nKoide", "GR"]
passes =  [24, 33, 28, 18, 13, 7, 7, 5, 7]
infos =   [1, 2, 2, 2, 2, 1, 1, 0, 10]
fails =   [0, 0, 0, 0, 0, 0, 0, 0, 1]
dom_cols = [GOLD, CYAN, GREEN, PURPLE, BLUE, ORANGE, MAG, SILVER, RED]

y = np.arange(len(domains))

for i in range(len(domains)):
    # PASS segment
    ax.barh(y[i], passes[i], height=0.5, color=GREEN, alpha=0.6)
    # INFO segment
    ax.barh(y[i], infos[i], height=0.5, color=SILVER, alpha=0.4,
            left=passes[i])
    # FAIL segment
    if fails[i] > 0:
        ax.barh(y[i], fails[i], height=0.5, color=RED, alpha=0.8,
                left=passes[i] + infos[i])

    # Total label
    total = passes[i] + infos[i] + fails[i]
    ax.text(total + 0.5, y[i], str(total), ha='left', va='center',
            fontsize=9, color=dom_cols[i], fontweight='bold')

ax.set_yticks(y)
ax.set_yticklabels(domains, fontsize=10, color=WHITE)
ax.set_xlabel("Number of comparisons", fontsize=11, color=SILVER)
ax.set_title("253 Comparisons Across 9 Domains",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

# Legend
ax.text(30, 8, "GREEN = PASS", ha='left', va='center', fontsize=9, color=GREEN)
ax.text(30, 7.3, "SILVER = INFO", ha='left', va='center', fontsize=9, color=SILVER)
ax.text(30, 6.6, "RED = FAIL", ha='left', va='center', fontsize=9, color=RED)

# Totals
ax.text(20, 1, "PASS: %d  |  INFO: %d  |  FAIL: %d" % (sum(passes), sum(infos), sum(fails)),
        ha='center', va='center', fontsize=11, color=WHITE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 42)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk6_17_253_domain_map.png")


# ================================================================
# FIG 18: PRECISION STAIRCASE — ALL 253 SORTED
# Type: Running/Convergence
# Shows: smooth descent from ppb to percent, no catastrophic outliers
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Representative points spanning the range (not all 253, selected landmarks)
landmarks = [
    (1, 0.007, r"$\alpha^{-1}$ vs Rb", GOLD),
    (5, 0.015, "Planck length", GOLD),
    (10, 0.22, r"$\alpha^{-1}$ vs CODATA", GOLD),
    (20, 2.8, "Mercury", GREEN),
    (30, 12, r"sin$^2\theta_W$", CYAN),
    (40, 16, "Solar redshift", GREEN),
    (50, 42, "Hulse-Taylor", GREEN),
    (60, 62, "Koide " + r"$m_\tau$", SILVER),
    (80, 195, r"$M_W$ path B", CYAN),
    (100, 725, "DM/baryon", PURPLE),
    (120, 3300, r"$\alpha_s$", GREEN),
    (140, 3500, "GPS net", GREEN),
    (180, 8400, "Z width", CYAN),
    (220, 28600, "Proton mass\n(one-loop)", RED),
    (240, 51000, "Pion mass\n(one-loop)", RED),
]

# Interpolate a smooth curve through these
all_x = [p[0] for p in landmarks]
all_y = [p[1] for p in landmarks]

ax.semilogy(all_x, all_y, color=GOLD, linewidth=1.5, alpha=0.4)

for px, py, plabel, pcol in landmarks:
    ax.scatter([px], [py], s=80, color=pcol, zorder=5, marker='o')

# Labels — alternate sides to avoid overlap
for i, (px, py, plabel, pcol) in enumerate(landmarks):
    ha = 'left' if i % 2 == 0 else 'right'
    offset = 5 if i % 2 == 0 else -5
    ax.text(px + offset, py, plabel, ha=ha, va='center', fontsize=7,
            color=pcol)

# Reference lines
ax.axhline(y=1, color=DIM, linewidth=0.5, linestyle=':', alpha=0.3)
ax.text(245, 1, "1 ppb", ha='right', va='bottom', fontsize=7, color=DIM)
ax.axhline(y=1000, color=DIM, linewidth=0.5, linestyle=':', alpha=0.3)
ax.text(245, 1000, "0.1%", ha='right', va='bottom', fontsize=7, color=DIM)
ax.axhline(y=10000, color=DIM, linewidth=0.5, linestyle=':', alpha=0.3)
ax.text(245, 10000, "1%", ha='right', va='bottom', fontsize=7, color=DIM)

ax.set_xlabel("Comparison index (sorted by precision)", fontsize=11, color=SILVER)
ax.set_ylabel("Miss (ppm equivalent)", fontsize=11, color=SILVER)
ax.set_title("253 Comparisons Sorted by Precision",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(120, 0.003, "Smooth descent from ppb to percent.\n"
        "No catastrophic outliers. The worst ones have known fixes.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 253)
ax.set_ylim(0.002, 100000)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk6_18_precision_staircase_sorted.png")


# ================================================================
# FIG 19: THE COMPLETE SYSTEM — HOW EVERYTHING CONNECTS
# Type: Connection/Integer Map (four layers)
# Shows: pool -> experiments -> comparisons -> programs
# ================================================================
fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 13)

ax.text(7, 12.3, "The Complete System", ha='center', va='center',
        fontsize=18, fontweight='bold', color=GOLD)

# Layer 1: Value Pool (bottom)
pool_box = mpatches.FancyBboxPatch((1, 0.5), 12, 2.0,
    boxstyle="round,pad=0.2", facecolor=CYAN, alpha=0.1,
    linewidth=2)
ax.add_patch(pool_box)
ax.text(7, 1.5, "VALUE POOL: 2700+ nodes", ha='center', va='center',
        fontsize=13, color=CYAN, fontweight='bold')
ax.text(7, 0.9, "Every constant. Every measurement. Every result.", ha='center',
        va='center', fontsize=9, color=SILVER)

# Arrow up
ax.annotate("", xy=(7, 3.3), xytext=(7, 2.7),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Layer 2: Experiments
exp_box = mpatches.FancyBboxPatch((1, 3.3), 12, 2.0,
    boxstyle="round,pad=0.2", facecolor=GREEN, alpha=0.1,
    linewidth=2)
ax.add_patch(exp_box)
ax.text(7, 4.3, "36 EXPERIMENTS", ha='center', va='center',
        fontsize=13, color=GREEN, fontweight='bold')
ax.text(7, 3.7, "Each reads from pool, computes, produces outputs back to pool.",
        ha='center', va='center', fontsize=9, color=SILVER)

# Bidirectional arrow (experiments produce back into pool)
ax.annotate("", xy=(4, 2.7), xytext=(4, 3.3),
            arrowprops=dict(arrowstyle='<-', color=CYAN, lw=1.5, alpha=0.4))
ax.text(3.0, 3.0, "outputs\nback to\npool", ha='center', va='center',
        fontsize=7, color=CYAN, alpha=0.6)

# Arrow up
ax.annotate("", xy=(7, 6.1), xytext=(7, 5.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Layer 3: Comparisons
comp_box = mpatches.FancyBboxPatch((1, 6.1), 12, 2.0,
    boxstyle="round,pad=0.2", facecolor=GOLD, alpha=0.1,
    linewidth=2)
ax.add_patch(comp_box)
ax.text(7, 7.1, "253 COMPARISONS", ha='center', va='center',
        fontsize=13, color=GOLD, fontweight='bold')

# Mini pass/fail bar inside
bar_pass_w = 10.0
bar_info_w = 1.5
bar_fail_w = 0.1
bx0 = 2.0
by0 = 6.4
ax.barh(by0, bar_pass_w, height=0.3, color=GREEN, alpha=0.5, left=bx0)
ax.barh(by0, bar_info_w, height=0.3, color=SILVER, alpha=0.4, left=bx0 + bar_pass_w)
ax.barh(by0, bar_fail_w, height=0.3, color=RED, alpha=0.8, left=bx0 + bar_pass_w + bar_info_w)
ax.text(bx0 + bar_pass_w / 2, by0, "220 PASS", ha='center', va='center',
        fontsize=7, color=WHITE)

# Arrow up
ax.annotate("", xy=(7, 8.9), xytext=(7, 8.3),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Layer 4: Programs + Kill Switches
prog_box = mpatches.FancyBboxPatch((1, 8.9), 12, 2.5,
    boxstyle="round,pad=0.2", facecolor=PAN, alpha=0.3,
    linewidth=2)
ax.add_patch(prog_box)
ax.text(7, 10.8, "PROGRAMS + KILL SWITCHES", ha='center', va='center',
        fontsize=12, color=WHITE, fontweight='bold')

# Mini program boxes
prg_data = [
    (2.5, 9.7, "6 ACTIVE", GREEN),
    (7.0, 9.7, "6 KILLED", RED),
    (11.5, 9.7, "1 BLOCKED", ORANGE),
]
for px, py, ptxt, pcol in prg_data:
    rounded_box(ax, px, py, 2.5, 0.8, ptxt, pcol, fontsize=9, alpha=0.2)

# Side annotation
ax.text(7, -0.3, "Measurement " + r"$\rightarrow$" + " Pool " + r"$\rightarrow$" +
        " Derivation " + r"$\rightarrow$" + " Comparison " + r"$\rightarrow$" +
        " Program " + r"$\rightarrow$" + " Kill Switch\n"
        "Every link is traceable. Every link is documented.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_19_complete_system.png")


# ================================================================
# FIG 20: PHYSICS VS SOFTWARE PRACTICES
# Type: Comparison Bar (two columns, many rows)
# Shows: ten rows of dim vs green — systematic contrast
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 12)

ax.text(7, 11.3, "Physics Built Like Physics vs Physics Built Like Software",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Column headers
ax.text(4.0, 10.2, "Standard Practice", ha='center', va='center',
        fontsize=12, fontweight='bold', color=DIM)
ax.text(11.0, 10.2, "RUM Practice", ha='center', va='center',
        fontsize=12, fontweight='bold', color=GREEN)

rows = [
    ("Quality control", "Peer review\n(social, months)", "Test suite\n(computational, seconds)"),
    ("Failure handling", "Bury in\nsupplementary", "Same report,\nsame font size"),
    ("Dead ends", "Quietly\nabandoned", "Documented,\nKILLED, published"),
    ("Provenance", "Cite the\npaper", "Chain of custody\nto measurement"),
    ("Number format", "Float64\neverywhere", "Fraction arithmetic,\ndecimal at comparison"),
    ("Type system", "Everything is\na number", "exact_fraction vs\napproximate, tracked"),
    ("Updates", "Manual,\nerror-prone", "Swap one node,\nrerun all"),
    ("Self-doubt", "No formal\nmechanism", "Kill switches +\nstatistical blocking"),
    ("Reproducibility", "In principle\n(rarely checked)", "Every experiment\nrunnable by anyone"),
    ("Cross-domain", "Stay in your\ndepartment", "36 experiments\nspanning 9 domains"),
]

for i, (category, standard, rum) in enumerate(rows):
    y = 9.2 - i * 1.0

    # Category label (center)
    ax.text(0.5, y, category, ha='left', va='center', fontsize=8,
            color=SILVER, fontweight='bold')

    # Standard (dim)
    ax.text(4.0, y, standard, ha='center', va='center', fontsize=8,
            color=DIM,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, alpha=0.3))

    # RUM (green)
    ax.text(11.0, y, rum, ha='center', va='center', fontsize=8,
            color=GREEN,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, alpha=0.3))

    # Separator
    ax.plot([0, 14], [y - 0.45, y - 0.45], color=DIM, linewidth=0.3, alpha=0.2)

ax.text(7, -0.5, "Not a criticism of physicists. A criticism of the institution's tooling.\n"
        "The physics is the same. The engineering is different.\nThe engineering is why it works.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_20_physics_vs_software.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 6, 11-20) generated ===")
filenames = [
    "talk6_11_kill_switch_anatomy.png",
    "talk6_12_statistical_block.png",
    "talk6_13_graveyard.png",
    "talk6_14_program_status_map.png",
    "talk6_15_provenance_chain.png",
    "talk6_16_version_control.png",
    "talk6_17_253_domain_map.png",
    "talk6_18_precision_staircase_sorted.png",
    "talk6_19_complete_system.png",
    "talk6_20_physics_vs_software.png",
]
for f in filenames:
    print("  %s" % f)
    