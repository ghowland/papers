
#!/usr/bin/env python3
"""
HOWL PHYS-12 Diagrams — Electroweak Integer Anatomy
8 figures covering fermion couplings, LEP observables, A2 decomposition,
sin2thetaW extraction, MW prediction, Rb deficit, UV/IR competition.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: FERMION COUPLINGS v_f VS SIN2THETAW
# Type: Running/comparison
# Shows: v_f for nu, e, u, d as functions of sin2thetaW.
# The electron coupling crosses zero near 1/4. The accidental
# smallness of v_e — and hence the sensitivity of asymmetries —
# is the visual finding.
# ================================================================

fig, ax = dark_fig("Fermion Vector Couplings vs sin\u00b2\u03b8_W",
                   xlabel="sin\u00b2\u03b8_W",
                   ylabel="Vector coupling v_f",
                   size=(16, 10))

s2w = np.linspace(0.15, 0.35, 300)

# v_f = T3 - 2*Q*sin2thetaW
v_nu = np.ones_like(s2w) * 0.5                   # T3=1/2, Q=0
v_e = -0.5 + 2 * s2w                             # T3=-1/2, Q=-1
v_u = 0.5 - (4.0 / 3.0) * s2w                    # T3=1/2, Q=2/3
v_d = -0.5 + (2.0 / 3.0) * s2w                   # T3=-1/2, Q=-1/3

curve(ax, s2w, v_nu, '\u03bd: v = 1/2 (no sin\u00b2\u03b8_W dependence)', SILVER, 2, style='--')
curve(ax, s2w, v_e, 'e: v = \u22121/2 + 2sin\u00b2\u03b8_W', CYAN, 2.5)
curve(ax, s2w, v_u, 'u: v = 1/2 \u2212 4sin\u00b2\u03b8_W/3', ORANGE, 2.5)
curve(ax, s2w, v_d, 'd: v = \u22121/2 + 2sin\u00b2\u03b8_W/3', GREEN, 2.5)

# Zero line
ax.plot([0.15, 0.35], [0, 0], color=DIM, linewidth=1, alpha=0.5)

# Mark actual sin2thetaW
s2w_actual = 0.23122
ax.plot([s2w_actual, s2w_actual], [-0.5, 0.55], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.6)
ax.text(s2w_actual + 0.003, 0.52, 'Actual\nsin\u00b2\u03b8_W\n= 0.231',
        fontsize=10, color=GOLD, fontweight='bold')

# Mark 1/4 where v_e = 0
ax.plot([0.25, 0.25], [-0.5, 0.55], color=RED, linewidth=2,
        linestyle=':', alpha=0.5)
ax.text(0.25, -0.45, '1/4', fontsize=11, color=RED, ha='center',
        fontweight='bold')

# The zero crossing
v_e_actual = -0.5 + 2 * s2w_actual
data_point(ax, s2w_actual, v_e_actual, '', CYAN, size=300)
ax.annotate('v_e = \u2212939/25000\n= \u22120.0376\n(accidentally small!)',
            xy=(s2w_actual, v_e_actual), xytext=(0.28, -0.12),
            fontsize=10, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN))

# Sensitivity note
note(ax, 0.16, 0.35,
     'If sin\u00b2\u03b8_W = 1/4 exactly: v_e = 0\n'
     'Actual is 7.5% below 1/4\n\u2192 |v_e| tiny \u2192 asymmetries small\n'
     '\u2192 but extremely sensitive:\n'
     '   0.1% shift in sin\u00b2\u03b8_W \u2192 5.3% shift in v_e',
     SILVER, 9)

ax.set_xlim(0.15, 0.35)
ax.set_ylim(-0.5, 0.6)

legend(ax, loc='upper right')

save_fig(fig, 'phys12_01_fermion_couplings.png')


# ================================================================
# FIG 2: 11 LEP OBSERVABLES — COMPUTED / MEASURED RATIOS
# Type: Comparison bar
# Shows: Ratio (computed/measured) for each observable, clustered
# near 1.0. Color-coded by direction of missing correction.
# ================================================================

fig, ax = dark_fig("11 LEP/SLD Observables: Tree + \u0394\u03c1 vs Measurement",
                   xlabel="",
                   ylabel="Computed / Measured ratio",
                   size=(16, 10))

observables = [
    ('\u0393_l', 1.002, 'reduce'),
    ('\u0393_inv', 1.007, 'reduce'),
    ('\u0393_Z', 1.006, 'reduce'),
    ('R_l', 1.004, 'reduce'),
    ('R_b', 1.016, 'reduce'),
    ('R_c', 0.990, 'increase'),
    ('A_FB^l', 0.979, 'increase'),
    ('A_l', 0.987, 'increase'),
    ('\u03c3\u2070_had', 0.998, 'increase'),
    ('N_\u03bd', 0.975, 'increase'),
    ('M_W', 0.9995, 'increase'),
]

x_pos = np.arange(len(observables))

for i, (label, ratio, direction) in enumerate(observables):
    color = ORANGE if direction == 'reduce' else CYAN
    ax.bar(i, ratio - 1, bottom=1, color=color, alpha=0.6,
           edgecolor=color, linewidth=1.5, width=0.65)

ax.set_xticks(x_pos)
ax.set_xticklabels([o[0] for o in observables], fontsize=9, color=SILVER,
                    rotation=30, ha='right')

# Unity line
ax.plot([-0.5, len(observables) - 0.5], [1, 1], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(len(observables) - 0.3, 1.001, 'Perfect agreement', fontsize=9,
        color=GOLD, va='bottom')

# Legend for colors
ax.text(8.5, 1.018, '\u25a0 Missing correction\n   would REDUCE', fontsize=9,
        color=ORANGE, fontweight='bold')
ax.text(8.5, 1.012, '\u25a0 Missing correction\n   would INCREASE', fontsize=9,
        color=CYAN, fontweight='bold')

# ±1% bands
ax.fill_between([-0.5, len(observables) - 0.5], [0.99, 0.99], [1.01, 1.01],
                alpha=0.04, color=GREEN)
ax.text(-0.3, 1.01, '\u00b11%', fontsize=8, color=GREEN)

# Bottom note
result_box(ax, 5, 0.968,
           '14/14 checks pass. Every residual explained by\n'
           'known missing corrections of predicted size and sign.',
           GOLD, 9)

ax.set_xlim(-0.8, len(observables) - 0.2)
ax.set_ylim(0.965, 1.025)

save_fig(fig, 'phys12_02_lep_observables.png')


# ================================================================
# FIG 3: A2 THREE-PIECE WATERFALL — 87% CANCELLATION
# Type: Waterfall
# Shows: Rational (+1.368) + number-theoretic (+0.902) + geometric
# (-2.598) = net A2 (-0.328). The cancellation is the finding.
# ================================================================

fig, ax = dark_fig("A\u2082 Decomposition: 87% Cancellation Between Geometry and Arithmetic",
                   xlabel="",
                   ylabel="Contribution to A\u2082",
                   size=(16, 10))

pieces = [
    ('Rational\n197/144', 0, 1.3681, GREEN, 'Diagram counting\n(197 is prime)'),
    ('Number-theoretic\n(3/4)\u03b6(3)', 1.3681, 0.9015, BLUE, 'Polylogarithm\nintegration'),
    ('Geometric\nR\u2084\u00d7c_geom', 2.2696, -2.5981, RED, '4D phase space\n(R\u2084 = \u03c0\u00b2/32)'),
    ('Net A\u2082', 0, -0.3285, GOLD, ''),
]

bar_width = 0.65

for i, (label, bottom, value, color, origin) in enumerate(pieces):
    x = i if i < 3 else 3.5
    if i < 3:
        ax.bar(x, value, bottom=bottom, color=color, alpha=0.6,
               edgecolor=color, linewidth=2, width=bar_width)
        # Connector from previous
        if i > 0:
            ax.plot([x - 0.5, x - bar_width / 2],
                    [bottom, bottom], color=DIM, linewidth=1,
                    linestyle=':', alpha=0.5)
        # Value label
        if value > 0:
            ax.text(x, bottom + value / 2, '+%.3f' % value, fontsize=11,
                    color=WHITE, ha='center', va='center', fontweight='bold')
        else:
            ax.text(x, bottom + value / 2, '%.3f' % value, fontsize=11,
                    color=WHITE, ha='center', va='center', fontweight='bold')
        # Origin
        ax.text(x, -1.0 - i * 0.35, origin, fontsize=8, color=DIM,
                ha='center')
    else:
        # Net result bar
        ax.bar(x, value, bottom=0, color=color, alpha=0.7,
               edgecolor=color, linewidth=2.5, width=bar_width)
        ax.text(x, value - 0.15, '%.4f' % value, fontsize=12,
                color=GOLD, ha='center', fontweight='bold')

ax.set_xticks([0, 1, 2, 3.5])
ax.set_xticklabels(['Rational\n197/144', 'Number-\ntheoretic\n(3/4)\u03b6(3)',
                     'Geometric\nR\u2084\u00d7c', 'NET A\u2082'],
                    fontsize=9, color=SILVER)

# Cancellation annotation
ax.annotate('87.4%\ncancellation', xy=(2, 0), xytext=(2.8, 1.5),
            fontsize=12, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# The finding
result_box(ax, 0.5, 2.5,
           'A\u2082 is accidentally small.\n'
           'Geometry (\u22122.598) nearly cancels\n'
           'arithmetic (+2.270).\n'
           'Net = 12.6% of geometric piece.',
           GOLD, 10)

ax.set_xlim(-0.8, 4.5)
ax.set_ylim(-2.0, 3.2)

save_fig(fig, 'phys12_03_a2_waterfall.png')


# ================================================================
# FIG 4: SIN2THETAW FROM TWO INDEPENDENT OBSERVABLES
# Type: Scale/comparison
# Shows: Two extractions (0.23098 from A_l, 0.23102 from A_FB)
# agreeing to 3.9e-5, both shifted from MS-bar input by ~2e-4.
# ================================================================

fig, ax = dark_fig("sin\u00b2\u03b8_W: Two Independent Extractions Agree to 3.9 \u00d7 10\u207b\u2075",
                   xlabel="sin\u00b2\u03b8_W",
                   ylabel="",
                   size=(16, 8))

# Number line
ax.plot([0.2300, 0.2325], [1.0, 1.0], color=DIM, linewidth=2, alpha=0.5)

# MS-bar input
s2w_input = 0.23122
ax.plot([s2w_input, s2w_input], [0.5, 1.5], color=SILVER, linewidth=3)
data_point(ax, s2w_input, 1.0, '', SILVER, size=300)
ax.text(s2w_input, 2.0, 'MS-bar input\n0.23122', fontsize=11,
        color=SILVER, ha='center', fontweight='bold')

# A_l extraction
s2w_al = 0.23098
data_point(ax, s2w_al, 1.0, '', CYAN, size=350)
ax.text(s2w_al, 0.2, 'From A_l (SLD)\n0.23098', fontsize=11,
        color=CYAN, ha='center', fontweight='bold')

# A_FB extraction
s2w_afb = 0.23102
data_point(ax, s2w_afb, 1.0, '', ORANGE, size=350)
ax.text(s2w_afb, -0.5, 'From A_FB (LEP)\n0.23102', fontsize=11,
        color=ORANGE, ha='center', fontweight='bold')

# Agreement between the two
ax.annotate('', xy=(s2w_al, 1.5), xytext=(s2w_afb, 1.5),
            arrowprops=dict(arrowstyle='<->', color=GREEN, lw=2.5))
ax.text((s2w_al + s2w_afb) / 2, 1.8, '\u0394 = 3.9 \u00d7 10\u207b\u2075',
        fontsize=13, color=GREEN, ha='center', fontweight='bold')

# Shift from input
mid_extract = (s2w_al + s2w_afb) / 2
ax.annotate('', xy=(mid_extract, -0.8), xytext=(s2w_input, -0.8),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text((mid_extract + s2w_input) / 2, -1.2,
        'Shift \u2248 2 \u00d7 10\u207b\u2074\n(= known tree-to-effective correction)',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

# Key insight
note(ax, 0.231, -2.0,
     'Two independent experiments (SLD polarization, LEP forward-backward)\n'
     'give consistent readings of the same parameter at tree level.\n'
     'The agreement BETWEEN extractions is more significant than either alone.',
     SILVER, 9)

ax.set_xlim(0.2298, 0.2325)
ax.set_ylim(-2.8, 2.8)
ax.set_yticks([])

save_fig(fig, 'phys12_04_sin2thetaw_extraction.png')


# ================================================================
# FIG 5: M_W — TREE VS TREE+DELTARHO VS MEASURED
# Type: Comparison bar (distinct — 3 stage)
# Shows: Tree level (79953), tree+Deltarho (80326), measured (80369).
# The Deltarho correction closes 90% of the gap.
# ================================================================

fig, ax = dark_fig("M_W Prediction: The Top Quark's Radiative Fingerprint",
                   xlabel="",
                   ylabel="M_W (MeV)",
                   size=(16, 10))

stages = [
    ('Tree level\n(no corrections)', 79953, BLUE, '79953'),
    ('Tree + \u0394\u03c1\n(top quark loop)', 80326, CYAN, '80326'),
    ('Measured\n(PDG)', 80369, GOLD, '80369'),
]

for i, (label, value, color, val_text) in enumerate(stages):
    ax.bar(i, value - 79800, bottom=79800, color=color, alpha=0.6,
           edgecolor=color, linewidth=2, width=0.6)
    ax.text(i, value + 15, val_text, fontsize=14, color=color,
            ha='center', fontweight='bold')

ax.set_xticks([0, 1, 2])
ax.set_xticklabels([s[0] for s in stages], fontsize=10, color=SILVER)

# Gap annotations
# Tree to tree+Δρ
ax.annotate('', xy=(0, 79953), xytext=(1, 80326),
            arrowprops=dict(arrowstyle='<->', color=GREEN, lw=2))
ax.text(0.5, 80140, '+373 MeV\n(\u0394\u03c1 from m_t)',
        fontsize=10, color=GREEN, ha='center', fontweight='bold')

# Tree+Δρ to measured
ax.annotate('', xy=(1, 80326), xytext=(2, 80369),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(1.5, 80380, '+43 MeV\n(remaining\ncorrections)',
        fontsize=9, color=ORANGE, ha='center', fontweight='bold')

# The Δρ formula
result_box(ax, 0.5, 80450,
           '\u0394\u03c1 = 3G_Fm_t\u00b2/(8\u03c0\u00b2\u221a2) = 0.00933\n'
           'Integer content: 3, 8, \u03c0\u00b2, \u221a2\n'
           'The top quark\'s mass moves M_W by 373 MeV.\n'
           'Agreement: 0.05% (43 MeV remaining).',
           GOLD, 9)

ax.set_xlim(-0.8, 3.0)
ax.set_ylim(79800, 80550)

save_fig(fig, 'phys12_05_mw_prediction.png')


# ================================================================
# FIG 6: R_b DEFICIT — TOP QUARK FINGERPRINT
# Type: Comparison/threshold
# Shows: R_b computed (0.2197) vs measured (0.2163). The predicted
# t-b-W vertex correction (1.5%) matches the deficit (1.6%).
# The historical connection to the top quark discovery.
# ================================================================

fig, ax = dark_fig("R_b Deficit: The Top Quark Before Its Discovery",
                   xlabel="",
                   ylabel="R_b = \u0393_bb / \u0393_had",
                   size=(16, 10))

# Two bars
bars = [
    ('Tree + \u0394\u03c1\n(no b-vertex)', 0.2197, ORANGE),
    ('LEP measured', 0.2163, GREEN),
]

for i, (label, value, color) in enumerate(bars):
    ax.bar(i, value - 0.210, bottom=0.210, color=color, alpha=0.6,
           edgecolor=color, linewidth=2, width=0.6)
    ax.text(i, value + 0.0005, '%.4f' % value, fontsize=14, color=color,
            ha='center', fontweight='bold')

ax.set_xticks([0, 1])
ax.set_xticklabels([b[0] for b in bars], fontsize=10, color=SILVER)

# The deficit
ax.annotate('', xy=(0.3, 0.2197), xytext=(0.3, 0.2163),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2.5))
ax.text(0.7, 0.2180, 'Deficit: 0.0034\n(1.6%)', fontsize=12,
        color=RED, fontweight='bold')

# Predicted correction bar
ax.bar(2.2, 0.0033, bottom=0.2164, color=MAG, alpha=0.4,
       edgecolor=MAG, linewidth=2, width=0.6)
ax.text(2.2, 0.2200, 'Predicted\nt-b-W vertex\ncorrection:\n0.0033 (1.5%)',
        fontsize=10, color=MAG, ha='center', fontweight='bold')

ax.set_xticks([0, 1, 2.2])
ax.set_xticklabels(['Tree + \u0394\u03c1', 'LEP measured', 'Predicted\ncorrection'],
                    fontsize=9, color=SILVER)

# Historical context
note(ax, 0, 0.212,
     '1994: LEP measured R_b deficit \u2192 predicted m_t \u2248 170 GeV.\n'
     '1995: CDF/D0 discovered the top quark at 174 GeV.\n'
     'Our tree-level computation reproduces the pre-discovery state:\n'
     'the data shows a deficit that points to a heavy quark in the loop.',
     SILVER, 9)

# Same integers as Δρ
ax.text(2.2, 0.211, 'Same integers as \u0394\u03c1:\nG_F, 8, \u03c0\u00b2, \u221a2',
        fontsize=8, color=DIM, ha='center')

ax.set_xlim(-0.8, 3.2)
ax.set_ylim(0.210, 0.224)

save_fig(fig, 'phys12_06_rb_deficit.png')


# ================================================================
# FIG 7: A2 GEOMETRIC PIECE — UV VS IR INTERNAL COMPETITION
# Type: Comparison bar (internal)
# Shows: Within the geometric coefficient c_geom = 8/3 - 16ln2,
# the UV phase space (+2.667) competes with IR mass singularity
# (-11.090). IR overwhelms UV by 4.2x.
# ================================================================

fig, ax = dark_fig("Inside the Geometric Piece: UV vs IR Competition",
                   xlabel="",
                   ylabel="Contribution to c_geom = 8/3 \u2212 16 ln 2",
                   size=(16, 10))

# Three bars: UV, IR, net
components = [
    ('UV phase space\n8/3 = 32/12', 2.6667, GREEN, 'From 4D angular\nintegration'),
    ('IR boundary\n\u221216 ln 2 = \u221232/2 \u00d7 ln 2', -11.0904, RED, 'From Feynman parameter\nevaluated at boundary'),
    ('Net c_geom', -8.4237, GOLD, ''),
]

for i, (label, value, color, origin) in enumerate(components):
    x = i if i < 2 else 2.5
    if value > 0:
        ax.bar(x, value, color=color, alpha=0.6, edgecolor=color,
               linewidth=2, width=0.6)
        ax.text(x, value + 0.3, '+%.3f' % value, fontsize=12, color=color,
                ha='center', fontweight='bold')
    else:
        ax.bar(x, value, color=color, alpha=0.6, edgecolor=color,
               linewidth=2, width=0.6)
        ax.text(x, value - 0.5, '%.3f' % value, fontsize=12, color=color,
                ha='center', fontweight='bold')
    if origin:
        ax.text(x, 3.5, origin, fontsize=8, color=DIM, ha='center')

ax.set_xticks([0, 1, 2.5])
ax.set_xticklabels([c[0] for c in components], fontsize=9, color=SILVER)

# Ratio annotation
ax.annotate('IR overwhelms UV\nby factor 4.2\u00d7', xy=(1, -11.0),
            xytext=(2, -7),
            fontsize=11, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# The 32 connection
result_box(ax, 0.5, -9,
           'Both terms contain 32 = \u03c0\u00b2/R\u2084:\n'
           'UV: 32/12 = 8/3\nIR: 32/2 = 16\n'
           'Same R\u2084 content, different rational prefactors.\n'
           'Then c_geom \u00d7 R\u2084 = \u22122.598 (the geometric piece of A\u2082).',
           GOLD, 9)

ax.set_xlim(-0.8, 3.5)
ax.set_ylim(-13, 5)

save_fig(fig, 'phys12_07_uv_ir_competition.png')


# ================================================================
# FIG 8: PHYS-12 IDENTITY CARD
# Type: Identity card
# Shows: 11 observables from 7 inputs, A2 anatomy, integer laws.
# ================================================================

fig, ax = dark_canvas("PHYS-12 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'ELECTROWEAK INTEGER ANATOMY', fontsize=18,
        color=GOLD, ha='center', fontweight='bold')
ax.text(5, 8.6, 'The transformation laws are integers. The values are not.',
        fontsize=11, color=SILVER, ha='center', style='italic')

# Left: the electroweak computation
ax.text(2.5, 7.5, 'THE COMPUTATION', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

ew_items = [
    ('7 DATA-3 inputs', 'G_F, M_Z, \u03b1\u207b\u00b9, sin\u00b2\u03b8_W, \u03b1_s, m_t, m_H', CYAN),
    ('11 LEP observables', '14/14 checks pass', GREEN),
    ('2 transcendentals', 'Only \u03c0 and \u221a2 from Q335', BLUE),
    ('sin\u00b2\u03b8_W extracted', 'Two methods agree to 3.9\u00d710\u207b\u2075', GOLD),
    ('M_W at 0.05%', 'Top quark \u0394\u03c1 = 0.00933', ORANGE),
]
for i, (item, detail, color) in enumerate(ew_items):
    y = 6.7 - i * 0.7
    ax.text(1.0, y, item, fontsize=9, color=color, fontweight='bold')
    ax.text(1.0, y - 0.3, detail, fontsize=8, color=DIM)

# Right: the A2 decomposition
ax.text(7.5, 7.5, 'THE A\u2082 ANATOMY', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

a2_items = [
    ('Rational: 197/144', '+1.368 (counting)', GREEN),
    ('Number-theoretic: (3/4)\u03b6(3)', '+0.902 (polylog)', BLUE),
    ('Geometric: R\u2084 \u00d7 c_geom', '\u22122.598 (4D phase space)', RED),
    ('Net A\u2082', '\u22120.328 (87% cancellation)', GOLD),
]
for i, (piece, detail, color) in enumerate(a2_items):
    y = 6.7 - i * 0.8
    ax.text(6.0, y, piece, fontsize=9, color=color, fontweight='bold')
    ax.text(6.0, y - 0.3, detail, fontsize=8, color=DIM)

# Integer sources
ax.plot([0.5, 9.5], [2.8, 2.8], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 2.3, 'INTEGER SOURCES', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')

sources = [
    ('SU(3)\u00d7SU(2)\u00d7U(1)', 'N_c=3, T\u2083=\u00b11/2, Q_f', CYAN),
    ('Generations', 'n_\u03bd=3, n_l=3, n_u=2, n_d=3', GREEN),
    ('Loop expansion', '6, 3/8, 3/4, 12, 197/144', ORANGE),
]
for i, (source, content, color) in enumerate(sources):
    x = 1.5 + i * 3.0
    ax.text(x, 1.7, source, fontsize=9, color=color, ha='center',
            fontweight='bold')
    ax.text(x, 1.2, content, fontsize=7, color=DIM, ha='center')

# Bottom
ax.text(5, 0.4, 'Same thesis at two magnifications: 11 observables from 7 inputs,\n'
        'and one coefficient from three sources.\n'
        'The structure of the Standard Model is integers. The values are not.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys12_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-12 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys12_01_fermion_couplings.png',
    'phys12_02_lep_observables.png',
    'phys12_03_a2_waterfall.png',
    'phys12_04_sin2thetaw_extraction.png',
    'phys12_05_mw_prediction.png',
    'phys12_06_rb_deficit.png',
    'phys12_07_uv_ir_competition.png',
    'phys12_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    