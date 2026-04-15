#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 10, Slides 11-20
10 figures covering: dots adapt to scale, 17-level human stack,
nesting circles, namespace as database, no collisions,
fork-compute-merge, green/red/yellow map, rectification of names,
coexistence of naming systems, complete series card.
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
# FIG 11: HOW THE DOTS CHANGE ABOVE ATOMIC
# Type: Connection/Integer Map
# Shows: same principle, adapted vocabulary at macro scale
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 10)

ax.text(7, 9.3, "The Dots Adapt to the Scale",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Row 1: Particle scale
ax.text(7, 8.0, "Particle Scale", ha='center', va='center', fontsize=12,
        color=GOLD, fontweight='bold')

part_dots = [
    ("Dot 1: LEVEL", "Vacuum / Field /\nConfinement / EW /\nUnification"),
    ("Dot 2: FUNCTION", "Vortex / Messenger /\nScaffold / Composite"),
    ("Dot 3: CHARGE", r"$\pm$ / fractional /" + "\ncolor / neutral"),
    ("Dot 4: STABILITY", "Permanent / Flash /\nConfined / Unstable"),
]

for j, (title, opts) in enumerate(part_dots):
    cx = 1.0 + j * 3.5
    rounded_box(ax, cx, 6.3, 2.8, 2.0, "", GOLD, alpha=0.1)
    ax.text(cx, 7.0, title, ha='center', va='center', fontsize=7,
            color=GOLD, fontweight='bold')
    ax.text(cx, 6.0, opts, ha='center', va='center', fontsize=6, color=SILVER)

# Arrow down
ax.annotate("same principle\nadapted vocabulary", xy=(7, 4.5), xytext=(7, 5.0),
            fontsize=9, color=WHITE, ha='center',
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

# Row 2: Macro scale
ax.text(7, 4.0, "Macro Scale", ha='center', va='center', fontsize=12,
        color=CYAN, fontweight='bold')

macro_dots = [
    ("Dot 1: LEVEL", "Molecular / Cellular /\nOrgan / Organism /\nPlanetary / Stellar /\nGalactic"),
    ("Dot 2: STRUCTURE", "Bond / Membrane /\nChamber / Bilateral /\nSphere / Toroid"),
    ("Dot 3: FLOW", "Chemistry / Signals /\nMetabolism / Gravity /\nFusion"),
    ("Dot 4: PERSISTENCE", "Permanent / Cycling /\nSeasonal / Geological /\nStellar / Cosmological"),
]

for j, (title, opts) in enumerate(macro_dots):
    cx = 1.0 + j * 3.5
    rounded_box(ax, cx, 2.3, 2.8, 2.2, "", CYAN, alpha=0.1)
    ax.text(cx, 3.1, title, ha='center', va='center', fontsize=7,
            color=CYAN, fontweight='bold')
    ax.text(cx, 1.9, opts, ha='center', va='center', fontsize=6, color=SILVER)

ax.text(7, -0.5, "The hierarchy is continuous. The naming adapts.\nSame four-dot structure. Different vocabulary at each scale.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk10_11_dots_adapt.png")


# ================================================================
# FIG 12: ONE HUMAN, TOP TO BOTTOM — 17 LEVELS
# Type: Scale/Landscape (vertical)
# Shows: complete stack with "you are here" at level 11
# ================================================================
fig, ax = plt.subplots(figsize=(16, 18))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 18)

ax.text(6, 17.3, "One Person: Higgs to Universe\nin One Naming Convention",
        ha='center', va='center', fontsize=15, fontweight='bold', color=GOLD)

levels = [
    ("Vacuum.Scaffold.Neutral.Flash", "Higgs", DIM),
    ("Field.Messenger.Neutral.Permanent", "Photon", CYAN),
    ("Confinement.Vortex.Frac+.Confined", "Up quark", RED),
    ("Confinement.Composite-Donut.+.Perm", "Proton", RED),
    ("Atomic.Composite-Shell.Neutral.Perm", "Carbon", BLUE),
    ("Molecular.Bond.Chem.Perm", "Glucose", CYAN),
    ("Macro-Mol.Fold.Signals.Perm", "DNA", GREEN),
    ("Cellular.Membrane.Signals.Perm", "Neuron", GREEN),
    ("Tissue.Network.Signals.Perm", "Neural tissue", GREEN),
    ("Organ.Network.Signals.Perm", "Brain", ORANGE),
    ("Organism.Bilateral.Metab.Cycling", "YOU", GOLD),
    ("Ecosystem.Web.Metab.Seasonal", "Forest", GREEN),
    ("Geological.Strata.Material.Geol", "Continent", DIM),
    ("Planetary.Sphere.Gravity.Geol", "Earth", BLUE),
    ("Stellar.Sphere.Fusion.Stellar", "Sun", ORANGE),
    ("Galactic.Toroid.Gravity.Cosmo", "Milky Way", PURPLE),
    ("Cosmic.Boundary.Expansion.Cosmo", "Universe", GOLD),
]

for i, (taxname, thing, col) in enumerate(levels):
    y = 0.5 + i * 0.95

    is_you = (thing == "YOU")
    al = 0.2 if is_you else 0.08
    lw = 3 if is_you else 1

    band = mpatches.FancyBboxPatch((0.5, y - 0.25), 11.0, 0.65,
        boxstyle="round,pad=0.05", facecolor=col, alpha=al,
        linewidth=lw)
    ax.add_patch(band)

    ax.text(1.0, y + 0.08, taxname, ha='left', va='center', fontsize=6,
            color=col, family='monospace')
    ax.text(10.5, y + 0.08, thing, ha='right', va='center', fontsize=8,
            color=WHITE if is_you else col,
            fontweight='bold' if is_you else 'normal')

    if is_you:
        ax.annotate("YOU ARE HERE", xy=(11.2, y), xytext=(12, y),
                    fontsize=10, color=GOLD, fontweight='bold', ha='left',
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.text(6, -0.3, "17 levels. One naming convention. Level 11 of 17.\n"
        "You are nested inside the hierarchy at a specific depth.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_12_seventeen_levels.png")


# ================================================================
# FIG 13: THE NESTING — EACH LEVEL INSIDE THE NEXT
# Type: Geometric Cross-Section
# Shows: concentric circles with taxonomy names
# ================================================================
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')

ax.text(0, 7.3, "Every Level Is Inside the Next",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

circles = [
    (6.0, "Cosmic.Boundary", r"$10^{26}$" + " m", GOLD, 0.04),
    (5.0, "Galactic.Toroid", r"$10^{21}$" + " m", PURPLE, 0.06),
    (4.0, "Stellar.Sphere", r"$10^{9}$" + " m", ORANGE, 0.08),
    (3.0, "Planetary.Sphere", r"$10^{7}$" + " m", BLUE, 0.1),
    (2.0, "Organism.Bilateral", "~2 m", GOLD, 0.18),
    (1.3, "Atomic.Shell", r"$10^{-10}$" + " m", CYAN, 0.2),
    (0.7, "Confinement.Donut", r"$10^{-15}$" + " m", RED, 0.25),
    (0.3, "Vacuum.Scaffold", "base", DIM, 0.3),
]

for r, name, scale, col, al in circles:
    c = mpatches.Circle((0, 0), r, facecolor=col, alpha=al,
                          linewidth=1.5, linestyle='--')
    ax.add_patch(c)

# Labels on right — stagger to avoid overlap
for i, (r, name, scale, col, al) in enumerate(circles):
    label_x = 4.0
    label_y = 6.5 - i * 1.6

    ax.text(label_x, label_y + 0.2, name, ha='left', va='center',
            fontsize=8, color=col, fontweight='bold')
    ax.text(label_x, label_y - 0.2, scale, ha='left', va='center',
            fontsize=7, color=SILVER)

    # Leader line
    edge_x = min(r * 0.85, 3.8)
    ax.plot([edge_x, label_x - 0.2], [r * 0.3 - i * 0.2, label_y],
            color=col, linewidth=0.5, alpha=0.3)

# "You" marker
ax.scatter([0], [1.8], s=100, color=GOLD, zorder=10, marker='o')
ax.text(-1.5, 1.8, "you", ha='center', va='center', fontsize=9, color=GOLD)

ax.text(0, -7.0, "Everything is inside something.\nThe level prefix tells you which boundary you're inside.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk10_13_nesting_circles.png")


# ================================================================
# FIG 14: THE NAMESPACE AS DATABASE SCHEMA
# Type: Connection/Integer Map
# Shows: four example queries returning structured results
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 12)

ax.text(7, 11.3, "The Taxonomy Is a Database Index",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

queries = [
    ("Function = 'Messenger'",
     "photon, gluon, W" + r"$^+$" + ", W" + r"$^-$" + ", Z",
     "All force carriers\nacross all levels", GOLD),
    ("Stability = 'Flash'",
     "W" + r"$^+$" + ", W" + r"$^-$" + ", Z, Higgs, top quark",
     "Everything that\ndies instantly", RED),
    ("Level = 'Confinement'\nAND Function = 'Messenger'",
     "gluon (8 color states)",
     "All strong force\ncarriers. Two filters.", CYAN),
    ("Structure = 'Toroid'",
     "proton, galaxy",
     "Toroidal flow\nat any scale.\nSame shape " + r"$\rightarrow$" + "\nsame physics?", PURPLE),
]

for i, (query, result, note, col) in enumerate(queries):
    y = 9.5 - i * 2.3

    # Query box (left)
    rounded_box(ax, 3.0, y, 5.0, 1.2, "", col, alpha=0.1)
    ax.text(1.0, y + 0.3, "SELECT * WHERE", ha='left', va='center',
            fontsize=7, color=DIM, family='monospace')
    ax.text(1.0, y - 0.15, query, ha='left', va='center',
            fontsize=8, color=col, family='monospace')

    # Arrow
    ax.annotate("", xy=(6.5, y), xytext=(5.7, y),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

    # Result box (right)
    rounded_box(ax, 9.5, y, 4.0, 1.0, result, col, fontsize=8, alpha=0.12, textcolor=WHITE)

    # Note
    ax.text(12.5, y, note, ha='left', va='center', fontsize=7,
            color=SILVER, fontstyle='italic')

# Schema row at bottom
ax.text(7, 0.8, "Five columns: Level, Function, Charge, Stability, Scale.\nEach is a filterable index. The dotted notation IS the query language.",
        ha='center', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

ax.text(7, -0.2, "100 million experiments reduced to dozens of records.\nThe hierarchy IS the index.",
        ha='center', va='center', fontsize=9, color=GOLD, fontstyle='italic')

save(fig, "talk10_14_namespace_database.png")


# ================================================================
# FIG 15: NO COLLISIONS — THE LEVEL PREFIX
# Type: Comparison Bar
# Shows: same function word, different level, no collision
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 10)

ax.text(6, 9.3, "No Name Collisions Across Levels",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Collision examples
examples = [
    ("Donut structure", [
        ("Confinement.Composite-Donut", "Proton", RED),
        ("Galactic.Toroid", "Milky Way", PURPLE),
    ]),
    ("Messenger function", [
        ("Field.Messenger", "Photon", CYAN),
        ("Confinement.Messenger", "Gluon", RED),
        ("Electroweak.Messenger", "W/Z bosons", GREEN),
    ]),
    ("Permanent stability", [
        ("Field.Vortex...Permanent", "Electron", BLUE),
        ("Confinement.Composite...Permanent", "Proton", RED),
        ("Planetary.Sphere...Permanent", "Earth", GREEN),
    ]),
]

y_start = 7.5
for group_name, items in examples:
    ax.text(1.0, y_start + 0.3, group_name + ":", ha='left', va='center',
            fontsize=10, color=GOLD, fontweight='bold')

    for j, (taxname, thing, col) in enumerate(items):
        y = y_start - 0.5 - j * 0.7

        rounded_box(ax, 5.5, y, 5.0, 0.5, taxname, col, fontsize=8, alpha=0.1, textcolor=col)
        ax.text(9.0, y, r"$\rightarrow$ " + thing, ha='left', va='center',
                fontsize=9, color=WHITE)

    y_start -= len(items) * 0.7 + 1.0

ax.text(6, 0.5, "Same function word, different level prefix.\nNo collision. The prefix disambiguates.\nA proton donut and a galaxy donut are structurally related\nbut live at different addresses.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk10_15_no_collisions.png")


# ================================================================
# FIG 16: FORK, COMPUTE, MERGE
# Type: Progression/Sequence
# Shows: git-like workflow for distributed physics
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "The Distributed Physics Database",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Stage 1: Fork
rounded_box(ax, 3, 3.5, 4.0, 3.5, "", CYAN, alpha=0.12)
ax.text(3, 5.0, "1. FORK", ha='center', va='center', fontsize=14,
        color=CYAN, fontweight='bold')

# Main DB icon
rounded_box(ax, 2, 3.5, 1.5, 1.0, "POOL", DIM, fontsize=8, alpha=0.2)
# Fork arrow
ax.annotate("", xy=(3.8, 3.2), xytext=(2.8, 3.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))
# Copy
rounded_box(ax, 4.2, 3.0, 1.5, 0.8, "copy", CYAN, fontsize=7, alpha=0.15)

ax.text(3, 2.2, "Take a copy.\nYour workspace.", ha='center', va='center',
        fontsize=8, color=SILVER)

# Arrow to stage 2
ax.annotate("", xy=(6.0, 3.5), xytext=(5.2, 3.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

# Stage 2: Compute
rounded_box(ax, 8, 3.5, 4.0, 3.5, "", GOLD, alpha=0.12)
ax.text(8, 5.0, "2. COMPUTE", ha='center', va='center', fontsize=14,
        color=GOLD, fontweight='bold')

# New nodes
for dx, dy, nc in [(7.2, 3.8, GREEN), (7.8, 3.2, GREEN), (8.5, 3.6, GOLD), (8.8, 3.0, RED)]:
    ax.scatter([dx], [dy], s=60, color=nc, zorder=5, marker='o')

ax.text(8, 2.2, "Run derivations.\nProduce new values.\nGreen = exact.\nRed = approximate.",
        ha='center', va='center', fontsize=8, color=SILVER)

# Arrow to stage 3
ax.annotate("", xy=(11.0, 3.5), xytext=(10.2, 3.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

# Stage 3: Merge
rounded_box(ax, 13, 3.5, 4.0, 3.5, "", GREEN, alpha=0.12)
ax.text(13, 5.0, "3. MERGE", ha='center', va='center', fontsize=14,
        color=GREEN, fontweight='bold')

# Merged DB
rounded_box(ax, 13, 3.3, 2.5, 1.2, "POOL\n(updated)", GREEN, fontsize=8, alpha=0.2)

ax.text(13, 2.2, "Submit the merge.\nUnique address.\nCan't collide.",
        ha='center', va='center', fontsize=8, color=SILVER)

# Git analogy
ax.text(8, 0.5, "Branch " + r"$\rightarrow$" + " work " + r"$\rightarrow$" +
        " pull request " + r"$\rightarrow$" + " review " + r"$\rightarrow$" + " merge\n"
        "The same workflow that builds software.",
        ha='center', va='center', fontsize=10, color=CYAN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

ax.text(8, -0.5, "No departments in a distributed database. Just namespaces.\nEvery node that flips from red to green is permanent progress.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

save(fig, "talk10_16_fork_compute_merge.png")


# ================================================================
# FIG 17: GREEN, RED, YELLOW — THE MAP OF KNOWLEDGE
# Type: Connection/Integer Map
# Shows: grid of colored nodes — current state of knowledge
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 12)

ax.text(7, 11.3, "The Living Map: Exact, Approximate, Frontier",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Green nodes (exact)
ax.text(3.5, 10.0, "EXACT (never change)", ha='center', va='center',
        fontsize=10, color=GREEN, fontweight='bold')
green_items = [
    r"$\beta_1$ = 41/10", r"$\beta_2$ = $-$19/6", r"$\beta_3$ = $-$7",
    "gap = 38/27", r"sin$^2\theta_W$(tree) = 3/8",
    "thickness: 1/7", "thickness: 6/19", "thickness: 10/41",
    r"$N_\nu$ = 3", "gauge gap = 2",
]
np.random.seed(123)
for i, item in enumerate(green_items):
    col_i = i % 4
    row_i = i // 4
    x = 1.0 + col_i * 1.7
    y = 9.0 - row_i * 0.7
    ax.text(x, y, item, ha='center', va='center', fontsize=6,
            color=GREEN,
            bbox=dict(boxstyle='round,pad=0.15', facecolor=PAN, alpha=0.3))

# Red nodes (approximate)
ax.text(10.5, 10.0, "APPROXIMATE (improve with data)", ha='center', va='center',
        fontsize=10, color=RED, fontweight='bold')
red_items = [
    r"$\alpha^{-1}$ = 137.036", r"$M_Z$ = 91188", r"$m_t$ = 172570",
    r"$m_e$ = 0.511", r"$m_\mu$ = 105.7", r"$m_\tau$ = 1777",
    "G = 6.674" + r"$\times 10^{-11}$", r"$M_H$ = 125200",
    r"$H_0$ = 67.4", r"$\Omega_{DM}$ = 0.264",
]
for i, item in enumerate(red_items):
    col_i = i % 4
    row_i = i // 4
    x = 8.5 + col_i * 1.7
    y = 9.0 - row_i * 0.7
    ax.text(x, y, item, ha='center', va='center', fontsize=6,
            color=RED,
            bbox=dict(boxstyle='round,pad=0.15', facecolor=PAN, alpha=0.3))

# Yellow nodes (frontier)
ax.text(7, 5.5, "FRONTIER (being worked on)", ha='center', va='center',
        fontsize=10, color=ORANGE, fontweight='bold')
yellow_items = [
    "CD mass?", "sector splitting?", "Koide a" + r"$^2$" + "=2?",
    "gap 0.027?", "G running?", "Hubble tension?",
    "p = 0.81?", r"$\theta_{QCD}$" + " derivation?",
]
for i, item in enumerate(yellow_items):
    col_i = i % 4
    row_i = i // 4
    x = 3.5 + col_i * 2.5
    y = 4.5 - row_i * 0.7
    ax.text(x, y, item, ha='center', va='center', fontsize=7,
            color=ORANGE,
            bbox=dict(boxstyle='round,pad=0.15', facecolor=PAN, alpha=0.3))

# Direction arrows
ax.text(7, 2.5, "red " + r"$\rightarrow$" + " green = permanent progress (better measurement)\n"
        "yellow " + r"$\rightarrow$" + " green or red = resolved question\n"
        "The map grows in one direction.",
        ha='center', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

# Counts
ax.text(3.5, 1.5, "~20 exact", ha='center', va='center', fontsize=11,
        color=GREEN, fontweight='bold')
ax.text(7, 1.5, "~20 approximate", ha='center', va='center', fontsize=11,
        color=RED, fontweight='bold')
ax.text(10.5, 1.5, "~10 frontier", ha='center', va='center', fontsize=11,
        color=ORANGE, fontweight='bold')

save(fig, "talk10_17_knowledge_map.png")


# ================================================================
# FIG 18: CONFUCIUS APPLIED TO PHYSICS
# Type: Progression/Sequence
# Shows: wrong names -> wrong language -> wrong outcomes -> rectification
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "The Rectification of Names",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Three boxes of the Confucian chain
chain = [
    (2.5, 3.5, "If names are\nnot correct...", GOLD,
     "We call 4 readings\n'4 forces'.\nWe call a boundary\nreading 'a constant'.\nWe call Greek letters\n'explanations'."),
    (7.0, 3.5, "...language is not\nin accordance with\nthe truth of things...", CYAN,
     "Students learn 4 separate\nsubjects for 1 phenomenon.\nDepartments don't connect\nbecause words don't connect."),
    (11.5, 3.5, "...affairs cannot\nbe carried on\nto success.", RED,
     "Unification was missed\nfor 50 years because\nthe naming system hid\nthe connections."),
]

for i, (cx, cy, quote, col, example) in enumerate(chain):
    rounded_box(ax, cx, cy, 3.5, 4.0, "", col, alpha=0.1)
    ax.text(cx, cy + 1.2, quote, ha='center', va='center', fontsize=10,
            color=col, fontweight='bold', fontstyle='italic')
    ax.text(cx, cy - 0.5, example, ha='center', va='center', fontsize=7,
            color=SILVER)

    if i < 2:
        nx = chain[i+1][0]
        ax.annotate("", xy=(nx - 1.9, cy), xytext=(cx + 1.9, cy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

# Resolution arrow down
ax.annotate("", xy=(8, 0.3), xytext=(11.5, 1.3),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))

ax.text(8, -0.3, "The Rectification: call things what they are.\nName things for what they do. Encode the hierarchy in the name.\nThe soliton taxonomy IS the Rectification.",
        ha='center', va='center', fontsize=10, color=GREEN,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk10_18_rectification_of_names.png")


# ================================================================
# FIG 19: COEXISTENCE — HISTORICAL + TAXONOMY
# Type: Comparison Bar (two columns)
# Shows: both names for each particle — complementary
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 10)

ax.text(6, 9.3, "Both Names Coexist: History + Hierarchy",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

pairs = [
    ("Electron", "Field.Vortex.Negative.Permanent", CYAN),
    ("Proton", "Confinement.Composite-Donut.+.Permanent", RED),
    ("Photon", "Field.Messenger.Neutral.Permanent", GOLD),
    ("W" + r"$^+$ boson", "Electroweak.Messenger.Positive.Flash", GREEN),
    ("Cabibbo\nDoublet", "Unification.Vortex.Frac+.Bound-Stable", GOLD),
    ("Milky Way", "Galactic.Toroid.Gravity.Cosmo.GX-SBbc", PURPLE),
]

for i, (hist, tax, col) in enumerate(pairs):
    y = 7.8 - i * 1.2

    # Historical (silver, left)
    ax.text(2.5, y, hist, ha='center', va='center', fontsize=11,
            color=SILVER, fontweight='bold')

    # Equals
    ax.text(4.5, y, "=", ha='center', va='center', fontsize=14, color=DIM)

    # Taxonomy (colored, right)
    ax.text(8.5, y, tax, ha='center', va='center', fontsize=9,
            color=col, family='monospace',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, alpha=0.3))

# Analogy
ax.text(6, 0.8, '"Paris" = 48.86' + r"$^\circ$" + 'N, 2.35' + r"$^\circ$" + 'E',
        ha='center', va='center', fontsize=12, color=SILVER)
ax.text(6, 0.1, "Latitude and longitude don't replace city names.\nThey tell you where cities are.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_19_coexistence.png")


# ================================================================
# FIG 20: THE COMPLETE SERIES — TEN VIDEOS, ONE MODEL
# Type: Identity Card
# Shows: ten-video arc summary with key number per video
# ================================================================
fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 14)

ax.text(7, 13.3, "Ten Videos, Ten Chapters, One Model",
        ha='center', va='center', fontsize=18, fontweight='bold', color=GOLD)

videos = [
    ("1", "SWE Unifies Physics", "53 values from 13 inputs", GOLD),
    ("2", "Why Nobody Found This", "Wrong numbers, names, departments", CYAN),
    ("3", "The Physics Stack", "12 layers, vacuum to universe", GREEN),
    ("4", "What Unification Gets You", "Fiber optics, drug design, climate", BLUE),
    ("5", "The Number System", "Fractions, not decimals. Q335.", GOLD),
    ("6", "The Test Suite", "253 comparisons. 252 PASS. 1 FAIL.", GREEN),
    ("7", "The Map Has Edges", "p = 0.81. BLOCKED.", RED),
    ("8", "Human + AI", "Both names, same font size.", CYAN),
    ("9", "Gravity as Reading Depth", "Sector splitting, 2028-2032.", ORANGE),
    ("10", "The Soliton Taxonomy", "Level.Function.Charge.Stability.", GOLD),
]

for i, (num, title, key, col) in enumerate(videos):
    y = 11.8 - i * 1.1

    # Number badge
    ax.text(1.0, y, num, ha='center', va='center', fontsize=14,
            color=col, fontweight='bold',
            bbox=dict(boxstyle='circle,pad=0.2', facecolor=PAN, alpha=0.4))

    # Title
    ax.text(3.5, y, title, ha='left', va='center', fontsize=11,
            color=WHITE, fontweight='bold')

    # Key
    ax.text(10.5, y, key, ha='left', va='center', fontsize=9,
            color=col)

    # Separator
    ax.plot([0.5, 14], [y - 0.5, y - 0.5], color=DIM, linewidth=0.3, alpha=0.15)

# Closing statement
ax.text(7, 0.5, "The universe is rational. Check the numbers.\nThe field is open. There's room for everyone.",
        ha='center', va='center', fontsize=14, color=GOLD, fontweight='bold',
        linespacing=1.6)

# Links
ax.text(3.5, -0.7, "Code: GitHub", ha='center', va='center', fontsize=9, color=CYAN)
ax.text(7.0, -0.7, "Papers: Zenodo", ha='center', va='center', fontsize=9, color=GREEN)
ax.text(10.5, -0.7, "Book: Amazon ($3)", ha='center', va='center', fontsize=9, color=GOLD)

save(fig, "talk10_20_complete_series.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 10, 11-20) generated ===")
filenames = [
    "talk10_11_dots_adapt.png",
    "talk10_12_seventeen_levels.png",
    "talk10_13_nesting_circles.png",
    "talk10_14_namespace_database.png",
    "talk10_15_no_collisions.png",
    "talk10_16_fork_compute_merge.png",
    "talk10_17_knowledge_map.png",
    "talk10_18_rectification_of_names.png",
    "talk10_19_coexistence.png",
    "talk10_20_complete_series.png",
]
for f in filenames:
    print("  %s" % f)
    