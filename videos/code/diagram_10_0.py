#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 10, Slides 1-10
10 figures covering: historical names tell nothing, information gap,
four-dot naming convention, five soliton levels, six particles named,
photon vs gluon, three modes of one pattern, top quark flash,
CD in taxonomy, taxonomy extends to galaxies.
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
# FIG 1: HISTORICAL NAMES TELL YOU NOTHING
# Type: Comparison Bar (grid)
# Shows: seven particle names, all carrying zero structural info
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 10)

ax.text(7, 9.3, "What the Name Tells You",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Column headers
ax.text(3.0, 8.3, "Name", ha='center', va='center', fontsize=11,
        color=SILVER, fontweight='bold')
ax.text(8.0, 8.3, "Origin", ha='center', va='center', fontsize=11,
        color=SILVER, fontweight='bold')
ax.text(12.5, 8.3, "Physics\nrevealed", ha='center', va='center', fontsize=10,
        color=SILVER, fontweight='bold')

particles = [
    ("Quark", "From Finnegans Wake", "nothing", DIM),
    ("Muon", "Originally 'mu meson' (wrong)", "nothing", DIM),
    ("W boson", "W = 'weak'", "one adjective", DIM),
    ("Charm quark", "A 1970s personality trait", "nothing", DIM),
    ("Strange quark", "Surprised someone in 1947", "nothing", DIM),
    ("Gluon", "Glues things together", "one verb", DIM),
    ("Higgs boson", "Named after Peter Higgs", "social history", DIM),
]

for i, (name, origin, info, col) in enumerate(particles):
    y = 7.3 - i * 0.95

    ax.text(3.0, y, name, ha='center', va='center', fontsize=10,
            color=col, fontweight='bold')
    ax.text(8.0, y, origin, ha='center', va='center', fontsize=9,
            color=col)
    ax.text(12.5, y, info, ha='center', va='center', fontsize=9,
            color=RED if info == "nothing" else ORANGE)

    ax.plot([0.5, 14], [y - 0.4, y - 0.4], color=DIM, linewidth=0.3, alpha=0.2)

# Contrast row
y_bio = 0.8
ax.plot([0.5, 14], [y_bio + 0.5, y_bio + 0.5], color=GREEN, linewidth=1, alpha=0.3)
ax.text(3.0, y_bio, "Canis lupus", ha='center', va='center', fontsize=10,
        color=GREEN, fontweight='bold')
ax.text(8.0, y_bio, "Dog family, wolf species", ha='center', va='center',
        fontsize=9, color=GREEN)
ax.text(12.5, y_bio, "tree position,\nrelationships", ha='center', va='center',
        fontsize=9, color=GREEN)

ax.text(7, -0.5, "Biology has a taxonomy. Chemistry has the periodic table.\n"
        "Physics has personality labels and surnames.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk10_01_names_tell_nothing.png")


# ================================================================
# FIG 2: THE INFORMATION GAP — NAME VS KNOWLEDGE
# Type: Comparison Bar (two panels)
# Shows: 1/5 green vs 5/5 green — information density
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("What You Know From the Name Alone",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Historical name --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, r"W$^+$ boson", ha='center', va='center',
         fontsize=16, fontweight='bold', color=DIM)

properties_h = [
    ("Level in hierarchy", "?", RED),
    ("What it does", "?", RED),
    ("Charge", "+ (from name)", GREEN),
    ("How long it lives", "?", RED),
    ("What's above/below", "?", RED),
]

for i, (prop, val, col) in enumerate(properties_h):
    y = 7.0 - i * 1.2
    ax1.text(2.0, y, prop + ":", ha='left', va='center', fontsize=9, color=SILVER)
    ax1.text(7.5, y, val, ha='center', va='center', fontsize=10,
             color=col, fontweight='bold')

ax1.text(5, 1.5, "1 out of 5 known\nfrom the name.", ha='center', va='center',
         fontsize=12, color=RED, fontweight='bold')

# -- Right: Taxonomy name --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Electroweak.Messenger\n.Positive.Flash", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

properties_t = [
    ("Level in hierarchy", "Electroweak " + r"$\checkmark$", GREEN),
    ("What it does", "Messenger " + r"$\checkmark$", GREEN),
    ("Charge", "Positive " + r"$\checkmark$", GREEN),
    ("How long it lives", "Flash " + r"$\checkmark$", GREEN),
    ("What's above/below", "Unification / Confinement " + r"$\checkmark$", GREEN),
]

for i, (prop, val, col) in enumerate(properties_t):
    y = 7.0 - i * 1.2
    ax2.text(2.0, y, prop + ":", ha='left', va='center', fontsize=9, color=SILVER)
    ax2.text(7.5, y, val, ha='center', va='center', fontsize=10,
             color=col, fontweight='bold')

ax2.text(5, 1.5, "5 out of 5 known\nfrom the name.", ha='center', va='center',
         fontsize=12, color=GREEN, fontweight='bold')

fig.text(0.5, 0.04, "The taxonomy name encodes the essential physics.\nA student knows five facts before reading a paragraph.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk10_02_information_gap.png")


# ================================================================
# FIG 3: FOUR DOTS — THE NAMING CONVENTION
# Type: Connection/Integer Map
# Shows: four columns with options, one example assembled
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 10)

ax.text(7, 9.3, "Level . Function . Charge . Stability",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

columns = [
    ("LEVEL", GOLD, ["Vacuum", "Field", "Confinement", "Electroweak", "Unification"],
     "Where it sits"),
    ("FUNCTION", CYAN, ["Vortex", "Messenger", "Scaffold", "Composite-\nDonut", "Composite-\nShell"],
     "What it does"),
    ("CHARGE", GREEN, ["Neutral", "Negative", "Positive", "Fraction+", "Color"],
     "How it interacts"),
    ("STABILITY", MAG, ["Permanent", "Bound-Stable", "Unstable", "Flash", "Confined"],
     "How long it lasts"),
]

for j, (title, col, options, desc) in enumerate(columns):
    cx = 1.5 + j * 3.5

    ax.text(cx, 8.3, title, ha='center', va='center', fontsize=11,
            color=col, fontweight='bold')
    ax.text(cx, 7.7, desc, ha='center', va='center', fontsize=7,
            color=SILVER, fontstyle='italic')

    for i, opt in enumerate(options):
        y = 6.5 - i * 0.9
        # Highlight the electron example
        is_electron = (j == 0 and opt == "Field") or \
                      (j == 1 and opt == "Vortex") or \
                      (j == 2 and opt == "Negative") or \
                      (j == 3 and opt == "Permanent")

        if is_electron:
            rounded_box(ax, cx, y, 2.5, 0.6, opt, GOLD, fontsize=8, alpha=0.2, textcolor=GOLD)
        else:
            ax.text(cx, y, opt, ha='center', va='center', fontsize=8, color=DIM)

# Dots between columns
for j in range(3):
    cx = 1.5 + j * 3.5 + 1.75
    ax.text(cx, 5.5, ".", ha='center', va='center', fontsize=24, color=GOLD, alpha=0.5)

# Assembled example at bottom
ax.text(7, 1.5, "Field . Vortex . Negative . Permanent",
        ha='center', va='center', fontsize=16, color=GOLD, fontweight='bold')
ax.text(7, 0.7, r"$\rightarrow$" + "  The electron",
        ha='center', va='center', fontsize=14, color=WHITE)

ax.text(7, -0.3, "Four dots. Four pieces of information.\nEvery particle, every structure, every level.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_03_four_dots.png")


# ================================================================
# FIG 4: FIVE LEVELS OF THE SOLITON STACK
# Type: Scale/Landscape (vertical)
# Shows: five bands with example particles and energy scales
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 12)

ax.text(6, 11.3, "The Five Levels",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

levels = [
    ("Vacuum", DIM, "Higgs field. Cosmological constant.",
     "Vacuum.Scaffold.Neutral.Flash\n(Higgs excitation)", "~125 GeV"),
    ("Field", CYAN, "Electrons, photons, leptons.",
     "Field.Vortex.Negative.Permanent\n(electron)", "0.511 " + r"$-$" + " 1777 MeV"),
    ("Confinement", RED, "Quarks, gluons, protons.",
     "Confinement.Composite-Donut\n.Positive.Permanent (proton)", "~200 MeV " + r"$-$" + " 172 GeV"),
    ("Electroweak", GREEN, "W, Z bosons. Symmetry breaking.",
     "Electroweak.Messenger\n.Positive.Flash (W" + r"$^+$" + ")", "~80 " + r"$-$" + " 91 GeV"),
    ("Unification", GOLD, "GUT scale. Cabibbo Doublet.",
     "Unification.Vortex\n.Fraction-Positive.Bound-Stable (CD)", r"$\sim 10^{15}$" + " GeV"),
]

for i, (name, col, desc, example, energy) in enumerate(levels):
    y = 1.0 + i * 2.0

    # Band
    band = mpatches.FancyBboxPatch((0.5, y - 0.5), 11.0, 1.5,
        boxstyle="round,pad=0.1", facecolor=col, alpha=0.08,
        linewidth=1.5)
    ax.add_patch(band)

    # Left border
    ax.plot([0.5, 0.5], [y - 0.5, y + 1.0], color=col, linewidth=3, alpha=0.5)

    # Level name
    ax.text(1.5, y + 0.4, name, ha='left', va='center', fontsize=12,
            color=col, fontweight='bold')

    # Description
    ax.text(1.5, y - 0.1, desc, ha='left', va='center', fontsize=8,
            color=SILVER)

    # Example taxonomy name
    ax.text(7.5, y + 0.3, example, ha='left', va='center', fontsize=7,
            color=WHITE, family='monospace')

    # Energy scale
    ax.text(11.0, y + 0.4, energy, ha='right', va='center', fontsize=8,
            color=col)

# Arrow showing "up = higher energy"
ax.annotate("higher energy " + r"$\rightarrow$", xy=(12, 10), xytext=(12, 1),
            fontsize=9, color=DIM, ha='center', rotation=90,
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

save(fig, "talk10_04_five_levels.png")


# ================================================================
# FIG 5: SIX PARTICLES NAMED — SIDE BY SIDE
# Type: Comparison Bar (grid)
# Shows: six parallel translations — pattern visible
# ================================================================
fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 12)

ax.text(7, 11.3, "Six Particles: Historical vs Taxonomy",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Headers
ax.text(2.0, 10.3, "Historical", ha='center', va='center', fontsize=10,
        color=DIM, fontweight='bold')
ax.text(7.0, 10.3, "Taxonomy Name", ha='center', va='center', fontsize=10,
        color=GOLD, fontweight='bold')
ax.text(12.0, 10.3, "What each dot tells you", ha='center', va='center', fontsize=10,
        color=GREEN, fontweight='bold')

particles = [
    ("Photon", "Field.Messenger\n.Neutral.Permanent",
     "Field level. Carries readings.\nNo charge. Lasts forever.", GOLD),
    ("Gluon", "Confinement.Messenger\n.Color.Confined",
     "Confinement level. Carries force.\nColor charged. Cannot leave.", RED),
    ("W" + r"$^+$", "Electroweak.Messenger\n.Positive.Flash",
     "EW level. Carries reading.\nPositive. Dies in 10" + r"$^{-25}$" + " s.", GREEN),
    ("Higgs", "Vacuum.Scaffold\n.Neutral.Flash",
     "Deepest level. Ground state.\nNeutral. Decays instantly.", DIM),
    ("Proton", "Confinement.Composite-Donut\n.Positive.Permanent",
     "Confinement level. Three vortices\nin donut. Positive. Permanent.", CYAN),
    ("Electron", "Field.Vortex\n.Negative.Permanent",
     "Field level. Circulation pattern.\nNegative. Permanent.", BLUE),
]

for i, (hist, tax, explain, col) in enumerate(particles):
    y = 9.0 - i * 1.6

    ax.text(2.0, y, hist, ha='center', va='center', fontsize=11,
            color=DIM, fontweight='bold')

    rounded_box(ax, 7.0, y, 4.5, 1.0, tax, col, fontsize=8, alpha=0.1, textcolor=col)

    ax.text(12.0, y, explain, ha='center', va='center', fontsize=7,
            color=SILVER)

    # Arrow
    ax.annotate("", xy=(4.5, y), xytext=(3.5, y),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1, alpha=0.4))

    ax.plot([0, 14], [y - 0.7, y - 0.7], color=DIM, linewidth=0.3, alpha=0.15)

ax.text(7, -0.2, "The historical name tells you history.\nThe taxonomy name tells you physics. Both coexist.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_05_six_particles_named.png")


# ================================================================
# FIG 6: PHOTON VS GLUON — SAME FUNCTION, DIFFERENT LEVEL
# Type: Comparison Bar (two panels)
# Shows: shared "Messenger" dot, different level/charge/stability
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Two Messengers: Same Job, Different Boundary",
             fontsize=16, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Photon --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Photon", ha='center', va='center',
         fontsize=14, fontweight='bold', color=CYAN)

dots_ph = [
    ("Level", "Field", BLUE),
    ("Function", "Messenger", GOLD),
    ("Charge", "Neutral", GREEN),
    ("Stability", "Permanent", CYAN),
]
for i, (label, val, col) in enumerate(dots_ph):
    y = 7.2 - i * 1.3
    ax1.text(2.5, y, label + ":", ha='left', va='center', fontsize=10, color=SILVER)
    highlight = GOLD if label == "Function" else col
    ax1.text(7.0, y, val, ha='center', va='center', fontsize=12,
             color=highlight, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN,
                       alpha=0.5 if label == "Function" else 0.2))

ax1.text(5, 2.0, "Carries EM reading\nbetween boundaries.\nTravels at c.\nCan cross any boundary.",
         ha='center', va='center', fontsize=9, color=CYAN, fontstyle='italic')

# -- Right: Gluon --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Gluon", ha='center', va='center',
         fontsize=14, fontweight='bold', color=RED)

dots_gl = [
    ("Level", "Confinement", RED),
    ("Function", "Messenger", GOLD),
    ("Charge", "Color", GREEN),
    ("Stability", "Confined", RED),
]
for i, (label, val, col) in enumerate(dots_gl):
    y = 7.2 - i * 1.3
    ax2.text(2.5, y, label + ":", ha='left', va='center', fontsize=10, color=SILVER)
    highlight = GOLD if label == "Function" else col
    ax2.text(7.0, y, val, ha='center', va='center', fontsize=12,
             color=highlight, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN,
                       alpha=0.5 if label == "Function" else 0.2))

ax2.text(5, 2.0, "Carries strong force reading\nWITHIN the confinement boundary.\nColor charged.\nCannot leave. Ever.",
         ha='center', va='center', fontsize=9, color=RED, fontstyle='italic')

fig.text(0.50, 0.04, "Same Function dot: Messenger. The taxonomy reveals the connection\nthat 'photon' vs 'gluon' completely hides.",
         ha='center', va='center', fontsize=11, color=GOLD, fontstyle='italic')

save(fig, "talk10_06_photon_vs_gluon.png")


# ================================================================
# FIG 7: THREE MODES OF ONE PATTERN
# Type: Comparison Bar
# Shows: shared prefix highlighted gold, only mode differs
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 10)

ax.text(7, 9.3, "Electron, Muon, Tau: Three Modes of One Pattern",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

modes = [
    ("Electron", "Field.Vortex.Negative", "Permanent", "Mode-1",
     "0.511 MeV", "YES", CYAN),
    ("Muon", "Field.Vortex.Negative", "Unstable", "Mode-2",
     "105.7 MeV", "NO (2.2 " + r"$\mu$s)", GREEN),
    ("Tau", "Field.Vortex.Negative", "Unstable", "Mode-3",
     "1776.9 MeV", "NO (290 fs)", ORANGE),
]

# Column headers
ax.text(2.0, 8.0, "Historical", ha='center', va='center', fontsize=10,
        color=DIM, fontweight='bold')
ax.text(5.5, 8.0, "Shared prefix", ha='center', va='center', fontsize=10,
        color=GOLD, fontweight='bold')
ax.text(8.5, 8.0, "Stability", ha='center', va='center', fontsize=10,
        color=SILVER, fontweight='bold')
ax.text(10.5, 8.0, "Mode", ha='center', va='center', fontsize=10,
        color=SILVER, fontweight='bold')
ax.text(12.5, 8.0, "Mass", ha='center', va='center', fontsize=10,
        color=SILVER, fontweight='bold')

for i, (hist, prefix, stab, mode, mass, stable, col) in enumerate(modes):
    y = 6.5 - i * 1.5

    ax.text(2.0, y, hist, ha='center', va='center', fontsize=12,
            color=col, fontweight='bold')

    # Shared prefix highlighted
    rounded_box(ax, 5.5, y, 4.0, 0.8, prefix, GOLD, fontsize=9, alpha=0.15, textcolor=GOLD)

    ax.text(8.5, y, stab, ha='center', va='center', fontsize=10,
            color=col)
    ax.text(10.5, y, mode, ha='center', va='center', fontsize=10,
            color=col)
    ax.text(12.5, y, mass, ha='center', va='center', fontsize=9,
            color=SILVER)

# Arrow to shared prefix
ax.annotate("IDENTICAL\nin all three", xy=(5.5, 4.5), xytext=(5.5, 2.5),
            fontsize=10, color=GOLD, ha='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Historical contrast
ax.text(2.0, 2.5, "'Electron', 'Muon', 'Tau'\nThree unrelated words.\nNo visible connection.",
        ha='center', va='center', fontsize=8, color=DIM, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

ax.text(7, -0.2, "They're the same pattern at three energy levels.\nThe taxonomy makes this obvious. The historical names hide it.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_07_three_modes.png")


# ================================================================
# FIG 8: THE TOP QUARK — FLASH SCREAMS AT YOU
# Type: Comparison Bar
# Shows: one red "Flash" in a column of "Confined" — visual anomaly
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1.5, 10)

ax.text(6, 9.3, "The Top Quark: The Name Reveals the Physics",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

quarks = [
    ("Up (Mode-1)", "Confinement.Vortex.Fraction+.Confined", CYAN, "Confined"),
    ("Charm (Mode-2)", "Confinement.Vortex.Fraction+.Confined", CYAN, "Confined"),
    ("Top (Mode-3)", "Confinement.Vortex.Fraction+.Flash", RED, "Flash"),
    ("Down (Mode-1)", "Confinement.Vortex.Fraction" + r"$-$" + ".Confined", GREEN, "Confined"),
    ("Strange (Mode-2)", "Confinement.Vortex.Fraction" + r"$-$" + ".Confined", GREEN, "Confined"),
    ("Bottom (Mode-3)", "Confinement.Vortex.Fraction" + r"$-$" + ".Confined", GREEN, "Confined"),
]

for i, (name, taxonomy, col, stab) in enumerate(quarks):
    y = 8.0 - i * 1.1

    ax.text(2.0, y, name, ha='left', va='center', fontsize=10,
            color=col, fontweight='bold')

    # Taxonomy with stability highlighted
    tax_base = taxonomy.rsplit('.', 1)[0]
    ax.text(6.5, y, tax_base + ".", ha='left', va='center', fontsize=8,
            color=DIM)

    stab_col = RED if stab == "Flash" else DIM
    stab_weight = 'bold' if stab == "Flash" else 'normal'
    ax.text(10.5, y, stab, ha='center', va='center', fontsize=12,
            color=stab_col, fontweight=stab_weight,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG if stab == "Flash" else PAN,
                      alpha=0.5 if stab == "Flash" else 0.2))

# Annotation for top quark
ax.annotate("Dies in 5 " + r"$\times 10^{-25}$" + " s.\nFaster than confinement can form.\n"
            "The ONLY quark that doesn't confine.",
            xy=(10.5, 5.8), xytext=(10.5, 2.5),
            fontsize=9, color=RED, ha='center',
            arrowprops=dict(arrowstyle='->', color=RED, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(6, -0.3, "In historical naming: 'top quark' " + r"$-$" + " just another quark.\n"
        "In the taxonomy: 'Flash' surrounded by five 'Confined'.\nThe name screams the physics.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_08_top_quark_flash.png")


# ================================================================
# FIG 9: THE CD IN THE TAXONOMY
# Type: Identity Card
# Shows: two near-identical entries — visual doublet
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "The Cabibbo Doublet: Two Taxonomy Names",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Upper component
card1 = mpatches.FancyBboxPatch((0.5, 5.5), 9.0, 2.5,
    boxstyle="round,pad=0.2", facecolor=GOLD, alpha=0.08,
    linewidth=2)
ax.add_patch(card1)

ax.text(5, 7.5, "Upper component", ha='center', va='center', fontsize=10,
        color=GOLD, fontweight='bold')
ax.text(5, 6.8, "Unification . Vortex . Fraction-Positive . Bound-Stable",
        ha='center', va='center', fontsize=11, color=GOLD, family='monospace')
ax.text(5, 6.1, "Level: unification boundary    Function: matter pattern\n"
        "Charge: +2/3    Stability: persists above detection threshold",
        ha='center', va='center', fontsize=8, color=SILVER)

# Lower component
card2 = mpatches.FancyBboxPatch((0.5, 2.5), 9.0, 2.5,
    boxstyle="round,pad=0.2", facecolor=CYAN, alpha=0.08,
    linewidth=2)
ax.add_patch(card2)

ax.text(5, 4.5, "Lower component", ha='center', va='center', fontsize=10,
        color=CYAN, fontweight='bold')
ax.text(5, 3.8, "Unification . Vortex . Fraction-Negative . Bound-Stable",
        ha='center', va='center', fontsize=11, color=CYAN, family='monospace')
ax.text(5, 3.1, "Same level, same function, opposite charge: " + r"$-$" + "1/3\n"
        "Same stability. The doublet structure is visible in the name.",
        ha='center', va='center', fontsize=8, color=SILVER)

# Shared highlight
ax.text(5, 5.2, "Only Charge differs " + r"$\rightarrow$" + " that's what 'doublet' means",
        ha='center', va='center', fontsize=10, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(5, 1.0, "Historical name for the history. Taxonomy name for the hierarchy.\n"
        "They complement each other. Latitude and longitude\ndon't replace city names.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

save(fig, "talk10_09_cd_taxonomy.png")


# ================================================================
# FIG 10: THE TAXONOMY EXTENDS — ATOMS TO GALAXIES
# Type: Scale/Landscape (vertical)
# Shows: one naming convention across 31 orders of magnitude
# ================================================================
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 12)

ax.text(6, 11.3, "Beyond Particles: The Taxonomy at Every Scale",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

entries = [
    ("Molecular.Bond.Chemistry\n.Permanent.A3", "Water (H" + r"$_2$O)", r"$10^{-10}$" + " m", CYAN),
    ("Cellular.Membrane.Signals\n.Permanent.D100", "A neuron", r"$10^{-4}$" + " m", GREEN),
    ("Organ.Chamber.Chemistry\n.Cycling.O-Pump", "The heart", r"$10^{-1}$" + " m", RED),
    ("Organism.Bilateral.Metabolism\n.Cycling.L-80yr", "A human", "~2 m", GOLD),
    ("Planetary.Sphere.Gravity\n.Geological.P-Earth", "Earth", r"$10^{7}$" + " m", BLUE),
    ("Stellar.Sphere.Fusion\n.Stellar.S-G2V", "The Sun", r"$10^{9}$" + " m", ORANGE),
    ("Galactic.Toroid.Gravity\n.Cosmological.GX-SBbc", "Milky Way", r"$10^{21}$" + " m", PURPLE),
]

for i, (taxname, thing, scale, col) in enumerate(entries):
    y = 1.0 + i * 1.4

    # Band
    band = mpatches.FancyBboxPatch((0.5, y - 0.4), 11.0, 1.0,
        boxstyle="round,pad=0.08", facecolor=col, alpha=0.06,
        linewidth=1)
    ax.add_patch(band)

    # Left border
    ax.plot([0.5, 0.5], [y - 0.4, y + 0.6], color=col, linewidth=3, alpha=0.4)

    # Taxonomy name
    ax.text(4.5, y + 0.1, taxname, ha='center', va='center', fontsize=7,
            color=col, family='monospace')

    # Thing
    ax.text(8.5, y + 0.1, thing, ha='center', va='center', fontsize=10,
            color=WHITE, fontweight='bold')

    # Scale
    ax.text(11.0, y + 0.1, scale, ha='right', va='center', fontsize=8,
            color=SILVER)

# Arrow showing scale span
ax.annotate("31 orders of magnitude", xy=(12, 10), xytext=(12, 1.5),
            fontsize=8, color=DIM, ha='center', rotation=90,
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

ax.text(6, -0.2, "One naming convention. Every scale. Every structure.\n"
        "The dots change meaning at higher levels because the right\n"
        "characterization changes with scale. The format stays the same.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk10_10_taxonomy_extends.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 10, 1-10) generated ===")
filenames = [
    "talk10_01_names_tell_nothing.png",
    "talk10_02_information_gap.png",
    "talk10_03_four_dots.png",
    "talk10_04_five_levels.png",
    "talk10_05_six_particles_named.png",
    "talk10_06_photon_vs_gluon.png",
    "talk10_07_three_modes.png",
    "talk10_08_top_quark_flash.png",
    "talk10_09_cd_taxonomy.png",
    "talk10_10_taxonomy_extends.png",
]
for f in filenames:
    print("  %s" % f)
    