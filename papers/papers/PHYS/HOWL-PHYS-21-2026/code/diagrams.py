#!/usr/bin/env python3
"""
HOWL PHYS-21 Diagrams — The Level 1 / Level 2 Boundary
8 figures covering three-region classification, CD boundary split,
confrontation table, Level 1 chain, amplification, historical rate/timeline.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: LEVEL 1 / LEVEL 2 / DERIVED — THREE REGIONS
# Type: Geometric/Venn
# Shows: Three regions with specific results placed in each.
# Level 1 = pure math. Level 2 = pure measurement.
# Derived = Level 1 applied to Level 2. Physics lives at the meeting.
# ================================================================

fig, ax = dark_canvas("The Three Categories: Level 1, Level 2, Derived",
                      size=(18, 14))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')

# Three regions as overlapping circles
r = 2.0
centers = [(-1.1, 0.8), (1.1, 0.8), (0, -1.0)]
labels_top = ['LEVEL 1\n(Framework)', 'LEVEL 2\n(Universe)', 'DERIVED\n(L1 applied to L2)']
circle_colors = [CYAN, ORANGE, GREEN]

for (cx, cy), color in zip(centers, circle_colors):
    circ = plt.Circle((cx, cy), r, fill=True, facecolor=color,
                        alpha=0.04, edgecolor=color, linewidth=2.5, zorder=2)
    ax.add_patch(circ)

# Region labels (outside)
ax.text(-2.8, 2.8, 'LEVEL 1\nFramework-Determined\n(no measurement needed)',
        fontsize=11, color=CYAN, fontweight='bold')
ax.text(1.5, 2.8, 'LEVEL 2\nUniverse-Supplied\n(requires experiment)',
        fontsize=11, color=ORANGE, fontweight='bold')
ax.text(0, -3.2, 'DERIVED: Level 1 functions applied to Level 2 inputs.\nThe physics lives HERE.',
        fontsize=11, color=GREEN, ha='center', fontweight='bold')

# Level 1 contents (left)
l1_items = [
    'b\u2081=41/10, b\u2082=\u221219/6, b\u2083=\u22127',
    'Gap ratio 218/115',
    'Democracy (4/3,4/3,4/3)',
    'CD: (3,2,1/6), \u0394b=(1/15,1,1/3)',
    'Gap 38/27, asymmetry 15',
    '\u03c4 \u221d M_GUT\u2074 scaling',
]
for i, item in enumerate(l1_items):
    ax.text(-2.3, 1.8 - i * 0.42, item, fontsize=7, color=CYAN)

# Level 2 contents (right)
l2_items = [
    '\u03b1\u207b\u00b9 = 137.036',
    'sin\u00b2\u03b8_W = 0.23122',
    '\u03b1_s = 0.1180',
    'm_e, m_\u03bc, m_\u03c4, quarks',
    'CKM angles, CP phases',
    'M_VL = 1.5\u20136 TeV (?)',
    'CD existence (?)',
]
for i, item in enumerate(l2_items):
    ax.text(1.3, 1.8 - i * 0.42, item, fontsize=7, color=ORANGE)

# Derived contents (bottom center / overlap)
d_items = [
    ('\u03b8_QCD = 0', 'L1 minimization + L2 masses'),
    ('M_GUT = 10\u00b9\u2075\u00b7\u2075', 'L1 betas + L2 couplings'),
    ('\u03c4_p ~ 10\u00b3\u2034\u207b\u00b3\u2035', 'L1 scaling + L2 M_GUT'),
    ('a_e at 4.3 ppb', 'L1 QED series + L2 \u03b1'),
    ('CKM deficit 0.002', 'L1 unitarity + L2 V_ij'),
]
for i, (result, source) in enumerate(d_items):
    y = -0.3 - i * 0.45
    ax.text(0, y, '%s  (%s)' % (result, source), fontsize=7, color=GREEN,
            ha='center')

save_fig(fig, 'phys21_01_three_regions.png')


# ================================================================
# FIG 2: CABIBBO DOUBLET BOUNDARY CARD — L1 VS L2 SPLIT
# Type: Geometric/split
# Shows: The CD with left half (Level 1, all known) and
# right half (Level 2, all pending). The split IS the finding.
# ================================================================

fig, ax = dark_canvas("The Cabibbo Doublet: Level 1 Known, Level 2 Pending",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, '(3, 2, 1/6)', fontsize=28, color=GOLD, ha='center',
        fontweight='bold', fontfamily='monospace')

# Dividing line
ax.plot([5, 5], [1.0, 8.5], color=GOLD, linewidth=3, alpha=0.6)

# Left: Level 1 (known)
ax.text(2.5, 8.2, 'LEVEL 1', fontsize=18, color=CYAN, ha='center',
        fontweight='bold')
ax.text(2.5, 7.6, '(determined by integers)', fontsize=10, color=SILVER,
        ha='center')

l1_props = [
    ('Representation:', '(3, 2, 1/6) VL', CYAN),
    ('Charges:', '+2/3 and \u22121/3', CYAN),
    ('\u0394b\u2081:', '1/15', CYAN),
    ('\u0394b\u2082:', '1', CYAN),
    ('\u0394b\u2083:', '1/3', CYAN),
    ('Gap ratio:', '38/27 = 1.407', GOLD),
    ('\u0394b\u2082/\u0394b\u2081:', '15 (maximum)', GREEN),
    ('1/Y\u00b2 scaling:', 'Sharp optimum at Y=1/6', GREEN),
    ('\u03c4 \u221d M_GUT\u2074:', 'Scaling law (dim-6)', GREEN),
]
for i, (prop, val, color) in enumerate(l1_props):
    y = 6.8 - i * 0.55
    ax.text(0.5, y, prop, fontsize=9, color=SILVER)
    ax.text(3.0, y, val, fontsize=10, color=color, fontweight='bold')

ax.text(2.5, 1.5, 'ALL KNOWN\nfrom exact Fraction\narithmetic on\ngauge group integers.',
        fontsize=10, color=CYAN, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN))

# Right: Level 2 (pending)
ax.text(7.5, 8.2, 'LEVEL 2', fontsize=18, color=ORANGE, ha='center',
        fontweight='bold')
ax.text(7.5, 7.6, '(supplied by experiment)', fontsize=10, color=SILVER,
        ha='center')

l2_props = [
    ('Mass M_VL:', '1.5\u20136 TeV', 'LHC + CKM'),
    ('\u03b8\u2081\u2084:', '|V_ub\'| \u2248 0.045', 'CKM deficit'),
    ('\u03b8\u2082\u2084:', 'Constrained', 'Kaon physics'),
    ('\u03b8\u2083\u2084:', 'From A_FB^b', 'LEP fit'),
    ('\u03b4\u2081:', 'Constrained', 'Neutron EDM'),
    ('\u03b4\u2082:', 'Constrained', 'B physics'),
    ('', '', ''),
    ('', '', ''),
    ('EXISTS?', 'NOT YET CONFIRMED', 'LHC, Hyper-K, Belle II'),
]
for i, (prop, val, source) in enumerate(l2_props):
    y = 6.8 - i * 0.55
    if prop:
        ax.text(5.5, y, prop, fontsize=9, color=SILVER)
        color = ORANGE if val != 'NOT YET CONFIRMED' else RED
        ax.text(7.5, y, val, fontsize=10, color=color, fontweight='bold')
        ax.text(9.3, y, source, fontsize=7, color=DIM)

ax.text(7.5, 1.5, 'ALL PENDING\nfrom experiments\nnot yet completed.',
        fontsize=10, color=ORANGE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE))

save_fig(fig, 'phys21_02_cd_boundary_split.png')


# ================================================================
# FIG 3: THE CONFRONTATION TABLE — L1 VS L2
# Type: Connection/comparison
# Shows: Six confrontations between Level 1 predictions and
# Level 2 measurements. Agreement, mismatch, or at boundary.
# ================================================================

fig, ax = dark_canvas("The Confrontation: Where Level 1 Meets Level 2",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.text(5, 9.3, 'Level 1 vs Level 2: The Physics Is in the Meeting',
        fontsize=16, color=GOLD, ha='center', fontweight='bold')

# Headers
ax.text(2.0, 8.3, 'Level 1\n(integers say)', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(5.0, 8.3, 'vs', fontsize=14, color=WHITE, ha='center',
        fontweight='bold')
ax.text(7.0, 8.3, 'Level 2\n(universe says)', fontsize=12, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(9.0, 8.3, 'Finding', fontsize=12, color=GOLD, ha='center',
        fontweight='bold')

ax.plot([0.3, 9.7], [7.8, 7.8], color=DIM, linewidth=1, alpha=0.5)

confrontations = [
    ('218/115 = 1.896', '1.358', '40% miss', RED, 'SM does not unify'),
    ('38/27 = 1.407', '1.358', '3.6% miss', GREEN, 'CD nearly fixes it'),
    ('7/5 = 1.400', '1.358', '3.1% miss', GREEN, 'MSSM nearly fixes it'),
    ('Row sum = 1.000', '0.998', '0.2% deficit', ORANGE, '4th quark mixing'),
    ('R_b (tree+\u0394\u03c1)', 'R_b = 0.2163', '1.6% over', ORANGE, 'Missing vertex corr.'),
    ('\u03c4 ~ 10\u00b3\u2034\u207b\u00b3\u2035', '> 2.4\u00d710\u00b3\u2034', 'At boundary', GOLD, 'Hyper-K tests'),
]

for i, (l1, l2, result, color, finding) in enumerate(confrontations):
    y = 7.2 - i * 1.0
    ax.text(2.0, y, l1, fontsize=10, color=CYAN, ha='center',
            fontweight='bold')

    # Arrow between
    ax.annotate('', xy=(3.8, y), xytext=(3.2, y),
                arrowprops=dict(arrowstyle='<->', color=color, lw=2))

    ax.text(5.5, y, l2, fontsize=10, color=ORANGE, ha='center',
            fontweight='bold')

    ax.text(7.5, y, result, fontsize=10, color=color, ha='center',
            fontweight='bold')

    ax.text(9.0, y, finding, fontsize=8, color=SILVER, ha='center')

# Bottom
ax.text(5, 0.5, 'Every row is a meeting between mathematics and measurement.\n'
        'The physics is in the meeting.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys21_03_confrontation.png')


# ================================================================
# FIG 4: THE LEVEL 1 CHAIN
# Type: Connection map with numbers
# Shows: Integer 11 → gauge asymmetry → betas → gap ratio 218/115
# → elimination → CD (3,2,1/6) → gap 38/27 → M_GUT → tau.
# Each node carries its Level classification.
# ================================================================

fig, ax = dark_canvas("The Level 1 Chain: From the Integer 11 to Proton Decay",
                      size=(20, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Chain nodes
nodes = [
    (0.8, 5.0, 'Integer 11\n(\u221211C\u2082/3)', 'Yang-Mills\ncoefficient', CYAN),
    (2.3, 5.0, 'Gauge\nasymmetry\n(0,\u221222/3,\u221211)', 'L1', CYAN),
    (3.8, 5.0, 'SM betas\n41/10,\u221219/6,\u22127', 'L1', CYAN),
    (5.3, 5.0, 'Gap ratio\n218/115', 'L1', CYAN),
    (5.3, 2.5, '15 candidates\n\u2192 eliminate 13', 'L1', GREEN),
    (6.8, 2.5, 'CD (3,2,1/6)\ngap = 38/27', 'L1', GOLD),
    (8.3, 2.5, 'M_GUT\n10\u00b9\u2075\u00b7\u2075', 'DERIVED\n(+L2 couplings)', GREEN),
    (9.5, 2.5, '\u03c4_p\n10\u00b3\u2034\u207b\u00b3\u2035', 'DERIVED\n(+L2 matrix el.)', GREEN),
]

for x, y, label, sublabel, color in nodes:
    ax.text(x, y, label, fontsize=9, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color,
                      linewidth=1.5))
    ax.text(x, y - 0.9, sublabel, fontsize=7, color=DIM, ha='center')

# Arrows along chain (top row)
for i in range(3):
    x1 = nodes[i][0] + 0.5
    x2 = nodes[i + 1][0] - 0.5
    ax.annotate('', xy=(x2, 5.0), xytext=(x1, 5.0),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

# Arrow down from gap ratio to elimination
ax.annotate('', xy=(5.3, 3.2), xytext=(5.3, 4.3),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.text(4.5, 3.8, '+L2 target\n1.358', fontsize=7, color=ORANGE)

# Arrows along bottom row
for i in range(4, 7):
    x1 = nodes[i][0] + 0.5
    x2 = nodes[i + 1][0] - 0.5
    ax.annotate('', xy=(x2, 2.5), xytext=(x1, 2.5),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# Level 2 inputs entering from above
ax.text(7.5, 7.0, 'Level 2 enters here', fontsize=10, color=ORANGE,
        ha='center', fontweight='bold')
ax.annotate('', xy=(8.3, 3.2), xytext=(8.3, 6.5),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2,
                            linestyle='--'))
ax.text(8.3, 5.5, '\u03b1, sin\u00b2\u03b8_W, \u03b1_s\nfrom DATA-3', fontsize=8,
        color=ORANGE, ha='center')

# The boundary line
ax.plot([7.5, 7.5], [1.5, 3.5], color=GOLD, linewidth=2, linestyle=':',
        alpha=0.5)
ax.text(7.5, 1.0, 'L1/L2\nboundary', fontsize=8, color=GOLD, ha='center')

# Legend
ax.text(1.0, 8.5, 'Pure Level 1 (no measurement)', fontsize=9, color=CYAN)
ax.text(1.0, 8.0, 'Derived (L1 + L2)', fontsize=9, color=GREEN)
ax.text(1.0, 7.5, 'Level 2 inputs', fontsize=9, color=ORANGE)

save_fig(fig, 'phys21_04_level1_chain.png')


# ================================================================
# FIG 5: THE AMPLIFICATION CHAIN WITH LEVEL CLASSIFICATION
# Type: Progression
# Shows: Gap ratio (L1) → distance (Derived) → M_GUT (Derived)
# → tau (Derived). Each step labeled with its Level and the
# amplification factor.
# ================================================================

fig, ax = dark_canvas("From Integers to Experiment: The Amplification Chain",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Four stages left to right
stages = [
    (1.5, 'Gap Ratio\n38/27 = 1.407', 'LEVEL 1\n(exact Fraction)', CYAN,
     'Distance\nfrom 1.358:\n0.049'),
    (4.0, 'M_GUT\n10\u00b9\u2075\u00b7\u2075 GeV', 'DERIVED\n(+L2 couplings)', GREEN,
     'From running\nequations'),
    (6.5, '\u03c4(proton)\n10\u00b3\u2034\u207b\u00b3\u2035 yr', 'DERIVED\n(+L2 matrix el.)', GREEN,
     'From \u03c4 \u221d M_GUT\u2074'),
    (9.0, 'Hyper-K\n2027\u20132047', 'LEVEL 2\n(experiment)', ORANGE,
     'Covers full\nprediction range'),
]

for x, label, level, color, detail in stages:
    ax.text(x, 6.0, label, fontsize=12, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=color,
                      linewidth=2))
    ax.text(x, 4.5, level, fontsize=9, color=color, ha='center',
            fontweight='bold')
    ax.text(x, 3.5, detail, fontsize=8, color=SILVER, ha='center')

# Arrows between stages
amplifications = [
    (2.5, 'Running over\n15 decades', GOLD),
    (5.2, 'M_GUT\u2074\nscaling', GOLD),
    (7.8, 'Compare to\nexperiment', GOLD),
]

for x, label, color in amplifications:
    ax.annotate('', xy=(x + 0.5, 6.0), xytext=(x - 0.5, 6.0),
                arrowprops=dict(arrowstyle='->', color=color, lw=3))
    ax.text(x, 7.5, label, fontsize=9, color=color, ha='center',
            fontweight='bold')

# The key insight
result_box(ax, 5.0, 1.5,
           'Pure integers (Level 1) \u2192 applied to measurements (Level 2)\n'
           '\u2192 produce testable predictions (Derived)\n'
           '\u2192 confronted with experiment (Level 2).\n\n'
           'The chain crosses the L1/L2 boundary TWICE:\n'
           'once when DATA-3 couplings enter the running,\n'
           'once when the prediction meets the detector.',
           GOLD, 10)

save_fig(fig, 'phys21_05_amplification_chain.png')


# ================================================================
# FIG 6: HISTORICAL SUCCESS RATE — 6 CONFIRMED, 5 NOT YET
# Type: Comparison bar
# Shows: Level 1 identifications: 6 found (green) and 5 not yet
# found (red). The honest assessment of predictive success.
# ================================================================

fig, ax = dark_fig("Level 1 Identifications: Historical Success Rate",
                   xlabel="",
                   ylabel="",
                   size=(16, 10))

# Confirmed particles (green)
confirmed = [
    ('Charm\n(1970\u21921974)', 4, GREEN),
    ('Bottom\n(1973\u21921977)', 4, GREEN),
    ('W boson\n(1967\u21921983)', 16, GREEN),
    ('Z boson\n(1967\u21921983)', 16, GREEN),
    ('Top\n(1977\u21921995)', 18, GREEN),
    ('Higgs\n(1964\u21922012)', 48, GREEN),
]

# Not yet confirmed (red)
not_confirmed = [
    ('Monopole\n(1931)', 95, RED),
    ('Axion\n(1977)', 49, RED),
    ('SUSY\n(1970s)', 50, RED),
    ('Gravitino\n(1973)', 53, RED),
    ('p decay\n(1974)', 52, RED),
]

all_items = confirmed + not_confirmed
x_pos = np.arange(len(all_items))

for i, (label, years, color) in enumerate(all_items):
    ax.bar(i, years, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.65)
    ax.text(i, years + 2, '%d yr' % years, fontsize=8, color=color,
            ha='center', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels([item[0] for item in all_items], fontsize=8,
                    color=SILVER, rotation=30, ha='right')

# Dividing line
ax.plot([5.5, 5.5], [0, 100], color=GOLD, linewidth=2, linestyle='--',
        alpha=0.5)

# Labels
ax.text(2.5, 90, 'CONFIRMED\n(6 particles)', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')
ax.text(8.0, 90, 'NOT YET\n(5 predictions)', fontsize=14, color=RED,
        ha='center', fontweight='bold')

# Success rate
ax.text(5.5, 75, '6/11\n(55%)', fontsize=16, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Where CD sits
ax.text(5.5, 60, 'Cabibbo Doublet:\n3 anomalies + gap ratio\n= stronger motivation\n'
        'than most unconfirmed entries',
        fontsize=9, color=SILVER, ha='center')

ax.set_xlim(-0.8, 10.8)
ax.set_ylim(0, 100)
ax.set_yticks([])

save_fig(fig, 'phys21_06_success_rate.png')


# ================================================================
# FIG 7: HISTORICAL TIMELINE — L1 IDENTIFICATION TO L2 CONFIRMATION
# Type: Timeline
# Shows: Charm (4 yr), W/Z (16 yr), Higgs (48 yr), CD (?).
# The gap between Level 1 and Level 2 for each particle.
# ================================================================

fig, ax = dark_fig("From Level 1 Identification to Level 2 Confirmation",
                   xlabel="Year",
                   ylabel="",
                   size=(16, 10))

particles_timeline = [
    ('Charm', 1970, 1974, CYAN, 'GIM mechanism', 'J/\u03c8 at BNL+SLAC'),
    ('W / Z', 1967, 1983, GREEN, 'SU(2)\u00d7U(1)', 'UA1 at CERN'),
    ('Top', 1977, 1995, ORANGE, 'b partner +\n\u0394\u03c1 constraint', 'Tevatron'),
    ('Higgs', 1964, 2012, MAG, 'EW symmetry\nbreaking', 'ATLAS/CMS'),
]

for i, (name, l1_year, l2_year, color, l1_label, l2_label) in enumerate(particles_timeline):
    y = 7.5 - i * 1.8

    # L1 identification point
    data_point(ax, l1_year, y, '', CYAN, size=200)
    ax.text(l1_year, y + 0.5, l1_label, fontsize=7, color=CYAN,
            ha='center')

    # L2 confirmation point
    data_point(ax, l2_year, y, '', GREEN, size=200)
    ax.text(l2_year, y + 0.5, l2_label, fontsize=7, color=GREEN,
            ha='center')

    # Gap bar
    ax.plot([l1_year, l2_year], [y, y], color=color, linewidth=4, alpha=0.4)
    gap = l2_year - l1_year
    ax.text((l1_year + l2_year) / 2, y - 0.4, '%s: %d yr gap' % (name, gap),
            fontsize=9, color=color, ha='center', fontweight='bold')

# Cabibbo Doublet — open-ended
y_cd = 0.8
data_point(ax, 2020, y_cd, '', GOLD, size=250)
ax.text(2020, y_cd + 0.5, 'Gap ratio +\nanomalies', fontsize=7, color=GOLD,
        ha='center')
ax.annotate('', xy=(2045, y_cd), xytext=(2020, y_cd),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=4, alpha=0.4))
ax.text(2033, y_cd - 0.4, 'Cabibbo Doublet: ? yr gap', fontsize=9,
        color=GOLD, ha='center', fontweight='bold')
ax.text(2037, y_cd + 0.5, 'Hyper-K\n2027\u20132037', fontsize=7,
        color=MAG, ha='center')

# Legend
ax.text(1960, 9.0, '\u25cf Level 1 identification', fontsize=9, color=CYAN)
ax.text(1980, 9.0, '\u25cf Level 2 confirmation', fontsize=9, color=GREEN)

ax.set_xlim(1955, 2050)
ax.set_ylim(-0.5, 9.5)
ax.set_yticks([])

save_fig(fig, 'phys21_07_historical_timeline.png')


# ================================================================
# FIG 8: PHYS-21 IDENTITY CARD
# Type: Identity card
# Shows: The principle, the boundary, the extension to CD.
# ================================================================

fig, ax = dark_canvas("PHYS-21 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE LEVEL 1 / LEVEL 2 BOUNDARY', fontsize=20, color=GOLD,
        ha='center', fontweight='bold')

# The principle
ax.text(5, 8.2, 'The integers tell you WHAT. The universe tells you HOW MUCH.',
        fontsize=13, color=WHITE, ha='center', fontweight='bold',
        style='italic')

# Left: Level 1
ax.text(2.5, 7.0, 'LEVEL 1', fontsize=16, color=CYAN, ha='center',
        fontweight='bold')
l1_summary = [
    'Representations',
    'Beta coefficients',
    'Gap ratios (exact)',
    'Scaling laws',
    'Elimination cascades',
    'Asymmetry mechanisms',
]
for i, item in enumerate(l1_summary):
    ax.text(2.5, 6.2 - i * 0.45, item, fontsize=9, color=CYAN, ha='center')

# Right: Level 2
ax.text(7.5, 7.0, 'LEVEL 2', fontsize=16, color=ORANGE, ha='center',
        fontweight='bold')
l2_summary = [
    'Masses',
    'Coupling constants',
    'Mixing angles',
    'CP phases',
    'Experimental bounds',
    'Existence of particles',
]
for i, item in enumerate(l2_summary):
    ax.text(7.5, 6.2 - i * 0.45, item, fontsize=9, color=ORANGE, ha='center')

# The extension
ax.plot([0.5, 9.5], [3.0, 3.0], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 2.5, 'THE EXTENSION', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')

ax.text(5, 1.7, 'The Cabibbo Doublet is the first particle in this series\n'
        'where Level 1 identifies WHAT should exist\n'
        'before Level 2 confirms WHETHER it exists.',
        fontsize=10, color=WHITE, ha='center', fontweight='bold')

ax.text(5, 0.5, 'Same pattern as charm (4 yr), W/Z (16 yr), Higgs (48 yr).\n'
        'Also same pattern as monopoles (95 yr, still waiting).\n'
        'Level 1 identifies. Level 2 decides.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys21_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-21 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys21_01_three_regions.png',
    'phys21_02_cd_boundary_split.png',
    'phys21_03_confrontation.png',
    'phys21_04_level1_chain.png',
    'phys21_05_amplification_chain.png',
    'phys21_06_success_rate.png',
    'phys21_07_historical_timeline.png',
    'phys21_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    