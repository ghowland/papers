#!/usr/bin/env python3
"""
HOWL Video 1 — Methodology Diagram
Single figure explaining the Integer Physics methodology.
Output: PNG to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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

# ================================================================
# FIG 1: METHODOLOGY
# Type: Progression (D5.7)
# Shows: Four-stage methodology as a left-to-right pipeline.
# Each stage has a title, description, and concrete example.
# The viewer understands the full method in one image.
# ================================================================

fig, ax = plt.subplots(figsize=(20, 11), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.text(0.50, 0.97, 'Integer Physics: Methodology',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=22, fontweight='bold', color=GOLD)

# Four stages, top to bottom with arrows between
stages = [
    {
        'num': '1',
        'title': 'Convert CODATA to exact fractions',
        'desc': (
            "Every measured input is stored as a ratio\n"
            "of two integers. No decimals enter the system.\n"
            "Python Fraction class preserves exactness."
        ),
        'example': (
            "m_e = 10219979 / 20000000 MeV\n"
            u"\u03b1\u207b\u00b9(M_Z) = 63953 / 500\n"
            "M_Z = 455938 / 5 MeV"
        ),
        'color': CYAN,
        'y': 0.78,
    },
    {
        'num': '2',
        'title': 'Run standard textbook equations',
        'desc': (
            "No new physics. Standard Model equations\n"
            "from QED, QCD, electroweak theory, BBN.\n"
            "Same formulas, integer arithmetic."
        ),
        'example': (
            "QED: A2 = 197/144 + (1/12)pi^2\n"
            "         + (3/4)zeta(3) - (1/2)pi^2 ln(2)\n"
            "VP running: R_f / (3 pi) per lepton"
        ),
        'color': GREEN,
        'y': 0.56,
    },
    {
        'num': '3',
        'title': 'Cross domains where derivation paths exist',
        'desc': (
            "When one result feeds into another domain,\n"
            "follow the chain. Single-domain matches are\n"
            "weak. Cross-domain chains are strong."
        ),
        'example': (
            "22/13 x pi (particle counting x geometry)\n"
            u"  \u2192 dark matter ratio (cosmology)\n"
            u"  \u2192 baryon density \u2192 D, He, Li (nuclear)"
        ),
        'color': PURPLE,
        'y': 0.34,
    },
    {
        'num': '4',
        'title': 'Flatten terminology where isomorphic',
        'desc': (
            "Different fields use different names for\n"
            "the same structure. Identify isomorphisms.\n"
            "Remove naming barriers to expose connections."
        ),
        'example': (
            "Field = Standing Wave = Vortex\n"
            "Mass = Inertia (F=ma has no substance)\n"
            "Constant = Running Reading"
        ),
        'color': ORANGE,
        'y': 0.12,
    },
]

box_w = 0.28
box_h = 0.16

for stage in stages:
    y = stage['y']
    color = stage['color']

    # Number circle
    circle_x = 0.06
    circle_y = y + box_h / 2
    circle = plt.Circle((0, 0), 1, transform=ax.transAxes, clip_on=True)  # placeholder
    ax.add_patch(mpatches.FancyBboxPatch(
        (0.03, circle_y - 0.025), 0.04, 0.05,
        transform=ax.transAxes,
        boxstyle='round,pad=0.01',
        facecolor=color, edgecolor=color, linewidth=2,
        alpha=0.3, clip_on=True))
    ax.text(0.05, circle_y, stage['num'],
            transform=ax.transAxes, ha='center', va='center',
            fontsize=20, fontweight='bold', color=color)

    # Title
    ax.text(0.10, y + box_h - 0.01, stage['title'],
            transform=ax.transAxes, ha='left', va='top',
            fontsize=14, fontweight='bold', color=color)

    # Description box
    ax.add_patch(mpatches.FancyBboxPatch(
        (0.10, y), box_w, box_h - 0.03,
        transform=ax.transAxes,
        boxstyle='round,pad=0.015',
        facecolor=PAN, edgecolor=DIM, linewidth=1,
        clip_on=True))
    ax.text(0.11, y + (box_h - 0.03) / 2, stage['desc'],
            transform=ax.transAxes, ha='left', va='center',
            fontsize=10, color=SILVER, linespacing=1.5)

    # Example box
    ax.add_patch(mpatches.FancyBboxPatch(
        (0.42, y), 0.32, box_h - 0.03,
        transform=ax.transAxes,
        boxstyle='round,pad=0.015',
        facecolor=PAN, edgecolor=color, linewidth=1.5,
        clip_on=True))
    ax.text(0.42 + 0.005, y + box_h - 0.04, 'Example:',
            transform=ax.transAxes, ha='left', va='top',
            fontsize=9, color=DIM, fontstyle='italic')
    ax.text(0.43, y + (box_h - 0.03) / 2 - 0.01, stage['example'],
            transform=ax.transAxes, ha='left', va='center',
            fontsize=10, color=WHITE, family='monospace', linespacing=1.5)

    # Result arrow pointing right
    ax.annotate('',
                xy=(0.78, y + (box_h - 0.03) / 2),
                xytext=(0.74, y + (box_h - 0.03) / 2),
                transform=ax.transAxes,
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Right side: what each step produces
outputs = [
    (0.78, stages[0]['y'], '13 inputs as\ninteger fractions', CYAN),
    (0.78, stages[1]['y'], '53 derived values\nat high precision', GREEN),
    (0.78, stages[2]['y'], 'Cross-domain chains\n(not curve fitting)', PURPLE),
    (0.78, stages[3]['y'], '5-word vocabulary\nacross all scales', ORANGE),
]

for x, y, text, color in outputs:
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), 0.18, box_h - 0.03,
        transform=ax.transAxes,
        boxstyle='round,pad=0.015',
        facecolor=BG, edgecolor=color, linewidth=1.5,
        clip_on=True))
    ax.text(x + 0.09, y + (box_h - 0.03) / 2, text,
            transform=ax.transAxes, ha='center', va='center',
            fontsize=11, fontweight='bold', color=color)

# Arrows between stages (vertical, connecting stages)
for i in range(len(stages) - 1):
    y_from = stages[i]['y']
    y_to = stages[i + 1]['y'] + box_h - 0.03
    ax.annotate('',
                xy=(0.05, y_to + 0.01),
                xytext=(0.05, y_from - 0.01),
                transform=ax.transAxes,
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

save(fig, 'vid1_09_methodology.png')
