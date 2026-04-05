#!/usr/bin/env python3
"""
HOWL PHYS-24 Diagrams — The Session 3 Operational Lexicon
8 figures covering unification ladder, parameter scorecard, two-loop
improvement, gap ratio landscape, proton lifetime, work landscape,
derivation vs search, identity card.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: UNIFICATION QUALITY LADDER
# Type: Comparison bar/progression
# Shows: Delta(1/alpha_3) improving from -6.58 (SM) through
# -1.17 (CD 1-loop) to -0.40 (CD 2-loop) toward ~0 (closable).
# ================================================================

fig, ax = dark_fig("\u0394(1/\u03b1\u2083) at M_GUT: The Unification Quality Ladder",
                   xlabel="",
                   ylabel="\u0394(1/\u03b1\u2083) at unification crossing",
                   size=(16, 10))

stages = [
    ('SM\n(no BSM)', -6.58, RED, 'Excluded\n(40% miss)'),
    ('SM + CD\n(one-loop)', -1.17, ORANGE, 'Poor\n(closable by\nthresholds?)'),
    ('SM + CD\n(two-loop)', -0.40, GREEN, 'Near\n(66% improvement)'),
    ('SM + CD\n(+ GUT thresholds)', 0.0, GOLD, 'Target\n(projected)'),
]

for i, (label, delta, color, quality) in enumerate(stages):
    ax.bar(i, delta, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.65)
    y_text = delta - 0.3 if delta < -0.2 else delta + 0.3
    ax.text(i, y_text, '%.2f' % delta, fontsize=14, color=color,
            ha='center', fontweight='bold')
    ax.text(i, 1.5, quality, fontsize=8, color=SILVER, ha='center')

ax.set_xticks(range(4))
ax.set_xticklabels([s[0] for s in stages], fontsize=9, color=SILVER)

# Zero line = perfect unification
ax.plot([-0.5, 3.5], [0, 0], color=GOLD, linewidth=2.5, linestyle='--',
        alpha=0.6)
ax.text(3.3, 0.2, 'Perfect\nunification\n\u0394 = 0', fontsize=9, color=GOLD,
        fontweight='bold')

# Improvement arrows
ax.annotate('', xy=(1, -1.17), xytext=(0, -6.58),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax.annotate('66%', xy=(2, -0.40), xytext=(1, -1.17),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

# MSSM comparison
ax.plot([-0.5, 3.5], [-0.69, -0.69], color=DIM, linewidth=1.5,
        linestyle=':', alpha=0.5)
ax.text(-0.3, -0.55, 'MSSM 1-loop:\n\u0394 = \u22120.69', fontsize=8, color=DIM)

result_box(ax, 2, -5.5,
           'The CD at two loops achieves the same\n'
           'unification quality as the MSSM at one loop.\n'
           'Both need GUT threshold corrections of\n'
           'comparable magnitude to close the residual.',
           GOLD, 9)

ax.set_xlim(-0.8, 4.0)
ax.set_ylim(-7.5, 2.5)

save_fig(fig, 'phys24_01_unification_ladder.png')


# ================================================================
# FIG 2: PARAMETER SCORECARD — 19 → 18 → 17 → 23
# Type: Progression
# Shows: Parameter count changes at each step with the trade:
# what was gained for each parameter added or removed.
# ================================================================

fig, ax = dark_canvas("Parameter Scorecard: What Each Step Costs and Buys",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'The Parameter Journey: 19 \u2192 18 \u2192 17 \u2192 23',
        fontsize=16, color=GOLD, ha='center', fontweight='bold')

# Four stages as columns
stages_param = [
    (1.5, '19', 'SM\n(original)', SILVER,
     ['19 free parameters', '3 anomalies unresolved', 'Gap ratio: 40% miss']),
    (3.5, '18', '\u03b8_QCD = 0\n(PHYS-7)', GREEN,
     ['\u22121 parameter', 'Energy minimization', '\u03b8_QCD derived, not free']),
    (5.5, '17', 'Koide K=2/3\n(conditional)', CYAN,
     ['\u22121 parameter (if exact)', 'm_\u03c4 predicted from m_e, m_\u03bc', 'Conditional on a\u00b2 = 2']),
    (8.0, '23', '+ Cabibbo\nDoublet', GOLD,
     ['+6 parameters', '0 anomalies unresolved', 'Gap ratio: 3.6% miss',
      'Proton decay testable', '3 anomalies resolved']),
]

for x, count, label, color, details in stages_param:
    # Count circle
    ax.text(x, 7.0, count, fontsize=36, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=color,
                      linewidth=2.5))
    ax.text(x, 5.5, label, fontsize=10, color=color, ha='center',
            fontweight='bold')
    for j, detail in enumerate(details):
        ax.text(x, 4.5 - j * 0.5, detail, fontsize=8, color=SILVER,
                ha='center')

# Arrows between stages
arrow_data = [
    (2.2, 7.0, '\u22121', GREEN),
    (4.2, 7.0, '\u22121\n(cond.)', CYAN),
    (6.5, 7.0, '+6', ORANGE),
]
for x, y, label, color in arrow_data:
    ax.annotate('', xy=(x + 0.5, y), xytext=(x - 0.5, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
    ax.text(x, y + 0.8, label, fontsize=11, color=color, ha='center',
            fontweight='bold')

# Bottom summary
ax.text(5, 1.0, 'Net: +4 parameters over SM.\n'
        'Trade: 6 new parameters buy 3 anomaly resolutions,\n'
        'gap ratio improvement from 40% to 3.6%,\n'
        'approximate unification, and testable proton decay.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys24_02_parameter_scorecard.png')


# ================================================================
# FIG 3: TWO-LOOP IMPROVEMENT
# Type: Comparison bar
# Shows: Delta improving from -1.17 (one-loop) to -0.40 (two-loop).
# The b33 = -26 as the dominant effect.
# ================================================================

fig, ax = dark_fig("Two-Loop Improvement: \u0394(1/\u03b1\u2083) from \u22121.17 to \u22120.40",
                   xlabel="",
                   ylabel="\u0394(1/\u03b1\u2083) at M_GUT",
                   size=(16, 10))

# Two bars
ax.bar(0, -1.17, color=ORANGE, alpha=0.6, edgecolor=ORANGE,
       linewidth=2, width=0.7)
ax.text(0, -1.30, '\u22121.17', fontsize=18, color=ORANGE, ha='center',
        fontweight='bold')
ax.text(0, 0.2, 'One-loop', fontsize=12, color=ORANGE, ha='center',
        fontweight='bold')

ax.bar(2, -0.40, color=GREEN, alpha=0.6, edgecolor=GREEN,
       linewidth=2, width=0.7)
ax.text(2, -0.55, '\u22120.40', fontsize=18, color=GREEN, ha='center',
        fontweight='bold')
ax.text(2, 0.2, 'Two-loop', fontsize=12, color=GREEN, ha='center',
        fontweight='bold')

# Zero line
ax.plot([-0.5, 3.5], [0, 0], color=GOLD, linewidth=2, linestyle='--',
        alpha=0.5)

# Improvement annotation
ax.annotate('66% improvement', xy=(2, -0.40), xytext=(0, -1.17),
            fontsize=14, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=3))

# The mechanism
result_box(ax, 2.5, -2.0,
           'Dominant effect: b\u2083\u2083 = \u221226\n'
           '(largest entry in the 3\u00d73 two-loop matrix).\n\n'
           'b\u2083\u2083 < 0 and \u03b1\u2083 > 0 \u2192\n'
           'two-loop SLOWS SU(3) running \u2192\n'
           '1/\u03b1\u2083 larger at M_GUT \u2192\n'
           'closer to the \u03b1\u2081 = \u03b1\u2082 crossing.',
           CYAN, 9)

# b_ij matrix highlight
ax.text(-0.3, -3.5, 'Two-loop b_ij matrix (dominant entry):', fontsize=10,
        color=WHITE, fontweight='bold')
ax.text(-0.3, -4.0, '         U(1)    SU(2)   SU(3)\n'
        'U(1)   199/50   27/10   44/5\n'
        'SU(2)   9/10    35/6     12\n'
        'SU(3)  11/10    9/2    \u221226  \u2190',
        fontsize=8, color=SILVER, fontfamily='monospace')
ax.text(2.5, -4.0, 'b\u2083\u2083 = \u221226\nis the key',
        fontsize=10, color=RED, fontweight='bold')

ax.set_xticks([0, 2])
ax.set_xticklabels(['One-loop\n(SM + CD)', 'Two-loop\n(SM + CD)'],
                    fontsize=10, color=SILVER)
ax.set_xlim(-1.0, 4.0)
ax.set_ylim(-4.5, 1.0)

save_fig(fig, 'phys24_03_two_loop.png')


# ================================================================
# FIG 4: COMPLETE GAP RATIO LANDSCAPE
# Type: Scale/landscape
# Shows: All 15 exact rational gap ratios on a number line,
# plus the SM at 218/115 and the measured at 1.358.
# The two survivors highlighted.
# ================================================================

fig, ax = dark_fig("The Complete Gap Ratio Landscape: 15 Candidates + SM + Measured",
                   xlabel="Gap ratio",
                   ylabel="",
                   size=(16, 8))

# Main axis
ax.plot([1.2, 2.35], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.3)

# All 15 candidates (from PHYS-15 enumeration)
candidates_all = [
    ('MSSM', 1.400, GREEN, True),
    ('CD', 1.407, CYAN, True),
    ('5+5\u0305', 1.481, ORANGE, False),
    ('3\u00d7H', 1.631, DIM, False),
    ('Sc(3,2)', 1.632, DIM, False),
    ('Sc(1,3)', 1.664, DIM, False),
    ('VL(1,2)', 1.712, DIM, False),
    ('2\u00d7H', 1.712, DIM, False),
    ('Sc(1,2)', 1.800, DIM, False),
    ('10+10\u0305', 1.948, DIM, False),
    ('Sc(3,1)', 2.000, DIM, False),
    ('VL e', 2.000, DIM, False),
    ('VL d', 2.114, DIM, False),
    ('Sc(8,1)', 2.180, DIM, False),
    ('VL u', 2.229, DIM, False),
]

for name, gap, color, survivor in candidates_all:
    size = 200 if survivor else 80
    lw = 2.5 if survivor else 1
    ax.plot([gap, gap], [0.3, 0.7], color=color, linewidth=lw)
    data_point(ax, gap, 0.5, '', color, size=size)

# Labels for survivors and 5+5bar
ax.text(1.400, 1.2, 'MSSM\n7/5', fontsize=9, color=GREEN,
        ha='center', fontweight='bold')
ax.text(1.407, -0.3, 'CD\n38/27', fontsize=9, color=CYAN,
        ha='center', fontweight='bold')
ax.text(1.481, 1.2, '5+5\u0305\n40/27', fontsize=8, color=ORANGE,
        ha='center')

# SM gap ratio
ax.plot([218.0 / 115, 218.0 / 115], [0.15, 0.85], color=RED, linewidth=3)
ax.text(218.0 / 115, 1.2, 'SM\n218/115', fontsize=10, color=RED,
        ha='center', fontweight='bold')

# Measured
ax.plot([1.358, 1.358], [0.1, 0.9], color=GOLD, linewidth=3)
data_point(ax, 1.358, 0.5, '', GOLD, size=400)
ax.text(1.358, -0.5, 'Measured\n1.358', fontsize=12, color=GOLD,
        ha='center', fontweight='bold')

# Window
ax.fill_between([1.208, 1.508], [0.1, 0.1], [0.9, 0.9],
                alpha=0.05, color=GREEN)
ax.text(1.358, -1.0, '\u00b10.15 window', fontsize=8, color=GREEN,
        ha='center')

# Pack of eliminated
ax.text(1.9, -0.5, '12 eliminated\n(gap ratio > 1.508)', fontsize=8,
        color=DIM, ha='center')

ax.set_xlim(1.2, 2.35)
ax.set_ylim(-1.3, 1.8)
ax.set_yticks([])

save_fig(fig, 'phys24_04_gap_landscape.png')


# ================================================================
# FIG 5: PROTON LIFETIME DISCRIMINATOR — CD VS MSSM
# Type: Scale (distinct — log tau)
# Shows: log10(tau) from 30 to 38. SM excluded, CD at boundary,
# MSSM beyond reach. Super-K bound, Hyper-K reach. 10^7 separation.
# ================================================================

fig, ax = dark_fig("Proton Lifetime: The 10\u2077 Discriminator",
                   xlabel="log\u2081\u2080(\u03c4 / years)",
                   ylabel="",
                   size=(16, 8))

# Main axis
ax.plot([29, 39], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.3)

# Scenarios
tau_scenarios = [
    (30, 'SM\n(excl.)', RED, 'min SU(5)\n10\u00b9\u00b3\u00b7\u2078'),
    (34.5, 'Cabibbo\nDoublet', GOLD, '10\u00b9\u2075\u00b7\u2075\n\u03c4 ~ 10\u00b3\u2034\u207b\u00b3\u2035'),
    (37, 'MSSM', GREEN, '10\u00b9\u2077\u00b7\u00b3\n\u03c4 ~ 10\u00b3\u2037'),
]

for log_t, label, color, detail in tau_scenarios:
    ax.plot([log_t, log_t], [0.15, 0.85], color=color, linewidth=2.5)
    data_point(ax, log_t, 0.5, '', color, size=300)
    ax.text(log_t, -0.5, label, fontsize=10, color=color,
            ha='center', fontweight='bold')
    ax.text(log_t, 1.2, detail, fontsize=8, color=SILVER, ha='center')

# Super-K bound
ax.plot([np.log10(2.4e34), np.log10(2.4e34)], [0.0, 1.0],
        color=RED, linewidth=3)
ax.fill_between([29, np.log10(2.4e34)], [0.0, 0.0], [1.0, 1.0],
                alpha=0.06, color=RED)
ax.text(32, 1.5, 'EXCLUDED\nby Super-K', fontsize=10, color=RED,
        ha='center', fontweight='bold')

# Hyper-K reach
ax.plot([35, 35], [0.0, 1.0], color=MAG, linewidth=2.5, linestyle='--')
ax.text(35, 1.5, 'Hyper-K\nreach\n(20 yr)', fontsize=9, color=MAG,
        ha='center', fontweight='bold')

# 10^7 separation
ax.annotate('', xy=(34.5, -1.2), xytext=(37, -1.2),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.5))
ax.text(35.75, -1.5, '10\u2077\u00d7 separation\n(from gap ratio\ndifference of 0.007)',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

ax.set_xlim(29, 39)
ax.set_ylim(-2.0, 2.0)
ax.set_yticks([])

save_fig(fig, 'phys24_05_proton_lifetime.png')


# ================================================================
# FIG 6: THE WORK LANDSCAPE — CLOSED / OPEN / DEPRIORITIZED
# Type: Three-region geometric
# Shows: Three columns with specific items placed in each.
# The state of the series after Session 3.
# ================================================================

fig, ax = dark_canvas("The Work Landscape: What Is Closed, Open, and Deprioritized",
                      size=(18, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Three columns
col_data = [
    (1.5, 'CLOSED', RED, [
        'SM non-unification',
        'Generation democracy',
        'Boson problem',
        'C\u2083 route to Koide',
        '82/82 PSLQ null',
        '\u03bb = 1/8 for Higgs',
        'Quark Koide phase/scale',
        'MSSM as minimal fix',
    ]),
    (5.0, 'OPEN', GREEN, [
        'VL two-loop b_ij',
        'GUT thresholds',
        'M_VL for exact unification',
        'sin\u00b2\u03b8_W from 3/8',
        '\u03b1_s prediction',
        'S, T oblique params',
        'Z-b-b vertex correction',
        'Koide a\u00b2 = 2 derivation',
    ]),
    (8.5, 'DEPRIORITIZED', DIM, [
        'Cosmological boundaries',
        'Re-open C\u2083 paths',
        'Broad PSLQ scans',
        'A\u2084 wall (blocked)',
        'CKM from masses',
        '\u03bb = g\'\u00b2 impedance',
    ]),
]

for x, title, color, items in col_data:
    ax.text(x, 9.3, title, fontsize=16, color=color, ha='center',
            fontweight='bold')
    # Column background
    rect = plt.Rectangle((x - 1.3, 1.5), 2.6, 7.5, facecolor=color,
                           alpha=0.03, edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    for i, item in enumerate(items):
        y = 8.3 - i * 0.8
        marker = '\u2717' if title == 'CLOSED' else ('\u25cf' if title == 'OPEN' else '\u25cb')
        ax.text(x, y, '%s %s' % (marker, item), fontsize=9, color=color,
                ha='center')

# Highlight sin2theta_W as unblocked
ax.text(5.0, 5.3, '\u2190 UNBLOCKED\n(~10 lines)', fontsize=8,
        color=GOLD, fontweight='bold')

# Bottom
ax.text(5, 0.5, 'After Session 3: 8 paths closed, 8 paths open, 6 deprioritized.\n'
        'The ground is set until falsified.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys24_06_work_landscape.png')


# ================================================================
# FIG 7: DERIVATION BEATS SEARCH
# Type: Comparison
# Shows: 3 derivation successes vs 82 PSLQ nulls.
# The methodological conclusion.
# ================================================================

fig, ax = dark_fig("Derivation Beats Search: 3 Successes vs 82 Nulls",
                   xlabel="",
                   ylabel="",
                   size=(16, 10))

# Left: derivation successes
ax.text(2, 8.5, 'DERIVATION', fontsize=18, color=GREEN, ha='center',
        fontweight='bold')
ax.text(2, 7.8, '3 / 3 succeed', fontsize=14, color=GREEN, ha='center',
        fontweight='bold')

derivations = [
    ('\u03b8_QCD = 0', 'Energy minimization\nof QCD vacuum', 'PHYS-7'),
    ('\u03b1 \u2194 a_e at 4.3 ppb', 'QED perturbation\ntheory (4 loops)', 'PHYS-9'),
    ('Koide K = 2/3', 'Trigonometric identity\n(conditional)', 'PHYS-8'),
]

for i, (result, method, source) in enumerate(derivations):
    y = 6.5 - i * 1.8
    ax.text(2, y, '\u2713 %s' % result, fontsize=11, color=GREEN,
            ha='center', fontweight='bold')
    ax.text(2, y - 0.5, method, fontsize=8, color=SILVER, ha='center')
    ax.text(2, y - 1.0, source, fontsize=7, color=DIM, ha='center')

# Right: PSLQ nulls
ax.text(7, 8.5, 'PSLQ SEARCH', fontsize=18, color=RED, ha='center',
        fontweight='bold')
ax.text(7, 7.8, '0 / 82 succeed', fontsize=14, color=RED, ha='center',
        fontweight='bold')

pslq_cats = [
    ('Physical constants', '59 tests\n(4-15 digits)', '\u2717 all null'),
    ('Dynamical quantities', '3 tests\n(10-30 digits)', '\u2717 all null'),
    ('Analytical constants', '10 tests\n(100 digits)', '\u2717 all null'),
    ('+ Bessel zeros', '10 tests\n(100 digits)', '\u2717 independent'),
]

for i, (category, scope, result) in enumerate(pslq_cats):
    y = 6.5 - i * 1.5
    ax.text(7, y, '%s: %s' % (category, result), fontsize=10, color=RED,
            ha='center', fontweight='bold')
    ax.text(7, y - 0.4, scope, fontsize=8, color=SILVER, ha='center')

# Sanity check
ax.text(7, 1.5, '\u2713 Sanity: PSLQ finds \u03c0\u00b2 = 6\u03b6(2)\nas [1, 0, \u22126]',
        fontsize=9, color=GREEN, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))

# The divider
ax.plot([4.5, 4.5], [1, 9], color=GOLD, linewidth=2, linestyle='--',
        alpha=0.4)

# Bottom conclusion
ax.text(4.5, 0.5, 'Every reduced parameter came from physical derivation.\n'
        'Every PSLQ search returned null. Prioritize derivation.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

ax.set_xlim(0, 9)
ax.set_ylim(0, 9.5)
ax.set_xticks([])
ax.set_yticks([])

save_fig(fig, 'phys24_07_derivation_vs_search.png')


# ================================================================
# FIG 8: PHYS-24 IDENTITY CARD
# Type: Identity card
# Shows: The operational ground. You are here.
# ================================================================

fig, ax = dark_canvas("PHYS-24 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE SESSION 3 OPERATIONAL LEXICON', fontsize=18, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'You are here. The ground is set until falsified.',
        fontsize=11, color=SILVER, ha='center', style='italic')

# Four pillars
pillars = [
    (1.5, 'GAP RATIO', [
        'SM: 218/115 = 1.896',
        'CD: 38/27 = 1.407',
        'Measured: 1.358',
        'SM misses by 40%',
        'CD misses by 3.6%',
    ], CYAN),
    (4.0, 'CABIBBO\nDOUBLET', [
        '(3,2,1/6) VL',
        '\u0394b = (1/15, 1, 1/3)',
        'Asymmetry: 15',
        'M_GUT = 10\u00b9\u2075\u00b7\u2075',
        'Mass: 1.5\u20136 TeV',
    ], GOLD),
    (6.5, 'TWO-LOOP', [
        '\u0394: \u22121.17 \u2192 \u22120.40',
        '66% improvement',
        'b\u2083\u2083 = \u221226 dominant',
        'Matches MSSM quality',
        'Thresholds close it',
    ], GREEN),
    (9.0, 'TESTS', [
        'Hyper-K: 2027\u20132037',
        'HL-LHC: now\u20132040',
        'Belle II: now\u20132030+',
        '\u03c4_CD/\u03c4_MSSM = 10\u2077',
        'One decade, one answer',
    ], ORANGE),
]

for x, title, items, color in pillars:
    ax.text(x, 7.5, title, fontsize=11, color=color, ha='center',
            fontweight='bold')
    for i, item in enumerate(items):
        ax.text(x, 6.5 - i * 0.5, item, fontsize=7, color=SILVER,
                ha='center')

# Bottom section
ax.plot([0.5, 9.5], [3.5, 3.5], color=DIM, linewidth=1, linestyle=':',
        alpha=0.4)

# The numbers
ax.text(5, 2.8, 'THE NUMBERS', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

numbers = [
    ('Papers:', '6 MATH + 24 PHYS + 4 DATA = 34', SILVER),
    ('Scripts:', '6 Session 3 + 8 demo = 14', SILVER),
    ('Checks:', '329/329 pass, 0 fail', GREEN),
    ('DATA-4:', '146 entries, 38/38 checks', CYAN),
    ('Closed paths:', '8 (stop re-litigating)', RED),
    ('Open paths:', '8 (where to spend time)', GREEN),
]
for i, (label, val, color) in enumerate(numbers):
    col = 0 if i < 3 else 1
    row = i % 3
    x = 2.5 + col * 5
    y = 2.0 - row * 0.5
    ax.text(x - 1.5, y, label, fontsize=9, color=SILVER)
    ax.text(x + 0.5, y, val, fontsize=9, color=color, fontweight='bold')

save_fig(fig, 'phys24_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-24 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys24_01_unification_ladder.png',
    'phys24_02_parameter_scorecard.png',
    'phys24_03_two_loop.png',
    'phys24_04_gap_landscape.png',
    'phys24_05_proton_lifetime.png',
    'phys24_06_work_landscape.png',
    'phys24_07_derivation_vs_search.png',
    'phys24_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    