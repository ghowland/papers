#!/usr/bin/env python3
"""
HOWL PHYS-19 Diagrams — Independent Anomaly Evidence for the Cabibbo Doublet
8 figures covering quantum number mapping, mass window timeline, test matrix,
12 orders of magnitude, four evidence lines, CKM context, historical parallel.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: EACH ANOMALY USES A DIFFERENT QUANTUM NUMBER
# Type: Connection/geometric
# Shows: CKM deficit needs SU(2), A_FB^b needs SU(3)xSU(2),
# Higgs mu needs SU(3). Only (3,2,1/6) has all three.
# ================================================================

fig, ax = dark_canvas("Each Anomaly Uses a Different Quantum Number",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'Three Anomalies, Three Quantum Numbers, One Particle',
        fontsize=16, color=GOLD, ha='center', fontweight='bold')

# The three anomalies on the left
anomalies = [
    ('CKM Deficit\n(2.5\u20134\u03c3)', 'Expands CKM\n3\u00d73 \u2192 3\u00d74', RED, 7.5),
    ('A_FB^b\n(~3\u03c3)', 'Modifies\nZ-b-b vertex', ORANGE, 5.0),
    ('Higgs \u03bc\n(~2\u03c3)', 'Loop in\ngg\u2192H', BLUE, 2.5),
]

for label, mechanism, color, y in anomalies:
    ax.text(1.5, y, label, fontsize=12, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color,
                      linewidth=2))
    ax.text(3.5, y, mechanism, fontsize=9, color=SILVER, ha='center')

# The quantum numbers needed (middle)
qn_map = [
    ('CKM', 'SU(2) doublet', GREEN, 7.5, 'Weak charge\nfor CKM mixing'),
    ('A_FB^b', 'SU(3) \u00d7 SU(2)', CYAN, 5.0, 'Color + weak\nfor Z-b vertex'),
    ('Higgs', 'SU(3) triplet', RED, 2.5, 'Color for\ngluon-fusion loop'),
]

for anomaly, qn, color, y, detail in qn_map:
    ax.annotate('', xy=(5.5, y), xytext=(4.2, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    ax.text(6.5, y, qn, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(6.5, y - 0.5, detail, fontsize=8, color=DIM, ha='center')

# The particle (right)
ax.annotate('', xy=(8.5, 5.0), xytext=(7.5, 7.2),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.annotate('', xy=(8.5, 5.0), xytext=(7.5, 5.0),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax.annotate('', xy=(8.5, 5.0), xytext=(7.5, 2.8),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))

ax.text(8.5, 5.0, '(3,2,1/6)', fontsize=20, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=3))
ax.text(8.5, 3.8, 'Color triplet\nWeak doublet\nY = 1/6', fontsize=9,
        color=SILVER, ha='center')

# Bottom
ax.text(5, 1.0, 'No single quantum number resolves all three.\n'
        'A color singlet cannot fix the Higgs excess.\n'
        'A weak singlet cannot fix the CKM deficit.\n'
        'Only the full (3,2,1/6) addresses all three simultaneously.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys19_01_quantum_number_map.png')


# ================================================================
# FIG 2: MASS WINDOW WITH EXPERIMENTAL TIMELINE
# Type: Scale/timeline
# Shows: 1.5-6 TeV window with HL-LHC reach expanding over time,
# Belle II sharpening the CKM constraint, FCC-hh projected.
# ================================================================

fig, ax = dark_fig("The Mass Window: Closing Over Time",
                   xlabel="Year",
                   ylabel="Mass reach / constraint (TeV)",
                   size=(16, 10))

# The window
years = [2024, 2026, 2028, 2030, 2035, 2040, 2045, 2050]

# LHC lower bound expanding
lhc_reach = [1.5, 1.5, 1.7, 2.0, 2.5, 3.0, 3.0, 3.0]
# CKM upper bound (may tighten with Belle II)
ckm_upper = [6.0, 6.0, 5.5, 5.0, 5.0, 5.0, 5.0, 5.0]
# FCC-hh reach (hypothetical, post-2050)
fcc_reach = [0, 0, 0, 0, 0, 0, 0, 6.0]

# Shade the allowed window
ax.fill_between(years, lhc_reach, ckm_upper, alpha=0.08, color=GREEN)

curve(ax, years, lhc_reach, 'LHC/HL-LHC lower bound (pair prod.)', RED, 2.5)
curve(ax, years, ckm_upper, 'CKM upper bound (perturbativity)', GOLD, 2.5,
      style='--')

# Mark key milestones
milestones = [
    (2024, 1.5, 'LHC Run 2\nexclusion', RED),
    (2027, 1.7, 'Hyper-K\nbegins', MAG),
    (2030, 2.0, 'Belle II\nfull dataset', ORANGE),
    (2040, 3.0, 'HL-LHC\nfull reach', CYAN),
]

for year, mass, label, color in milestones:
    data_point(ax, year, mass, '', color, size=200)
    ax.text(year, mass + 0.4, label, fontsize=8, color=color,
            ha='center', fontweight='bold')

# The window label
ax.text(2032, 4.0, 'ALLOWED\nWINDOW', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')

# Discovery vs exclusion zones
ax.text(2035, 1.5, 'HL-LHC discovers\nif M < 3 TeV', fontsize=8,
        color=CYAN, ha='center')
ax.text(2035, 5.5, 'FCC-hh needed\nif M > 3 TeV', fontsize=8,
        color=DIM, ha='center')

result_box(ax, 2040, 7,
           'Less than half a decade in energy.\n'
           'The window narrows as LHC reach grows\n'
           'and Belle II sharpens the CKM constraint.',
           GOLD, 9)

ax.set_xlim(2023, 2052)
ax.set_ylim(0, 8)

save_fig(fig, 'phys19_02_mass_window_timeline.png')


# ================================================================
# FIG 3: THE TEST MATRIX — WHAT EACH EXPERIMENT TESTS
# Type: Grid/flow
# Shows: Three experiments (Hyper-K, HL-LHC, Belle II) and
# which aspect of the Cabibbo Doublet each tests.
# ================================================================

fig, ax = dark_canvas("The Experimental Program: Three Tests for One Particle",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'Three Experiments Test Different Aspects',
        fontsize=16, color=GOLD, ha='center', fontweight='bold')

# Three experiment columns
experiments = [
    ('Hyper-K\n(2027\u20132037)', 'Proton decay\n\u03c4 ~ 10\u00b3\u2074\u207b\u00b3\u2075 yr',
     'M_GUT = 10^{15.5}', 'Gap ratio path', MAG, 1.5),
    ('HL-LHC\n(now\u20132040)', 'Direct production\nif M < 2\u20133 TeV',
     'Mass M_VL', 'Anomaly path', CYAN, 5.0),
    ('Belle II\n(now\u20132030+)', 'CKM precision\nV_us, V_ub',
     'Mixing |V_ub\'|', 'Anomaly path', ORANGE, 8.5),
]

for name, what_it_does, what_it_tests, which_road, color, x in experiments:
    # Experiment box
    ax.text(x, 7.5, name, fontsize=14, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=color,
                      linewidth=2.5))

    # What it does
    ax.text(x, 6.0, what_it_does, fontsize=10, color=SILVER, ha='center')

    # What it tests
    ax.text(x, 4.5, 'Tests:', fontsize=10, color=WHITE, ha='center',
            fontweight='bold')
    ax.text(x, 3.8, what_it_tests, fontsize=11, color=color, ha='center',
            fontweight='bold')

    # Which road
    ax.text(x, 2.8, 'From: %s' % which_road, fontsize=8, color=DIM, ha='center')

    # Arrow down to conclusion
    ax.annotate('', xy=(x, 1.8), xytext=(x, 2.5),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

# Discriminator table at bottom
ax.text(5, 1.5, 'THE DISCRIMINATOR', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

disc_items = [
    ('Hyper-K sees proton decay:', 'CD confirmed, MSSM excluded', GREEN),
    ('HL-LHC finds VL quark:', 'Direct discovery', GREEN),
    ('Belle II sharpens CKM to 5\u03c3:', 'Anomaly path strongly confirmed', GREEN),
    ('None of the above:', 'Minimal scenario excluded; search continues', RED),
]
for i, (condition, result, color) in enumerate(disc_items):
    y = 1.0 - i * 0.4
    ax.text(2.5, y, condition, fontsize=8, color=SILVER)
    ax.text(7.5, y, result, fontsize=8, color=color, fontweight='bold')

save_fig(fig, 'phys19_03_test_matrix.png')


# ================================================================
# FIG 4: 12 ORDERS OF MAGNITUDE BETWEEN TWO ROADS
# Type: Scale/landscape
# Shows: Gap ratio at 10^15 GeV, anomalies at 10^3 GeV.
# The enormous energy separation explains why the connection
# was missed.
# ================================================================

fig, ax = dark_fig("12 Orders of Magnitude: Why the Connection Was Missed",
                   xlabel="log\u2081\u2080(Energy / GeV)",
                   ylabel="",
                   size=(16, 10))

# Energy axis
log_E = np.linspace(-1, 17, 300)
ax.plot(log_E, [0.5] * len(log_E), color=DIM, linewidth=2, alpha=0.3)

# Anomaly path region (TeV scale)
shaded_region(ax, 2.5, 4.0, ORANGE, 0.08)
ax.text(3.25, 2.5, 'ANOMALY PATH\n10\u00b3 GeV\n(TeV scale)', fontsize=12,
        color=ORANGE, ha='center', fontweight='bold')

anomaly_items = [
    ('CKM deficit', 'Nuclear \u03b2 decay', -1),
    ('A_FB^b', 'LEP Z pole', 2),
    ('Higgs \u03bc', 'LHC', 3.5),
]
for label, source, log_e in anomaly_items:
    data_point(ax, log_e, 0.5, '', ORANGE, size=120)
    ax.text(log_e, 1.2, '%s\n(%s)' % (label, source), fontsize=7,
            color=ORANGE, ha='center')

# Gap ratio path region (GUT scale)
shaded_region(ax, 14.5, 16.5, CYAN, 0.08)
ax.text(15.5, 2.5, 'GAP RATIO PATH\n10\u00b9\u2075 GeV\n(GUT scale)', fontsize=12,
        color=CYAN, ha='center', fontweight='bold')

data_point(ax, 15.5, 0.5, '', CYAN, size=200)
ax.text(15.5, 1.2, 'Gauge coupling\nunification', fontsize=8,
        color=CYAN, ha='center')

# The gap
ax.annotate('', xy=(4.5, -0.5), xytext=(14.0, -0.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=3))
ax.text(9.25, -1.0, '12 orders of magnitude', fontsize=16, color=GOLD,
        ha='center', fontweight='bold')
ax.text(9.25, -1.7, 'Different communities. Different journals.\n'
        'Different conferences. Different mathematics.\n'
        'Same particle: (3, 2, 1/6).',
        fontsize=10, color=SILVER, ha='center')

# The particle bridges both
ax.text(9.25, 3.5, '(3, 2, 1/6)', fontsize=18, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD,
                  linewidth=2.5))
ax.annotate('', xy=(4.5, 3.3), xytext=(8.0, 3.3),
            arrowprops=dict(arrowstyle='<-', color=ORANGE, lw=2))
ax.annotate('', xy=(14.0, 3.3), xytext=(10.5, 3.3),
            arrowprops=dict(arrowstyle='<-', color=CYAN, lw=2))

ax.set_xlim(-2, 18)
ax.set_ylim(-2.5, 4.5)
ax.set_yticks([])

save_fig(fig, 'phys19_04_twelve_orders.png')


# ================================================================
# FIG 5: FOUR INDEPENDENT EVIDENCE LINES CONVERGING
# Type: Connection/convergence
# Shows: Gap ratio, CKM, A_FB^b, Higgs mu — four independent
# arrows pointing to (3,2,1/6). More than any prior BSM candidate.
# ================================================================

fig, ax = dark_canvas("Four Independent Evidence Lines \u2192 One Particle",
                      size=(16, 14))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')

# Central particle
ax.text(0, 0, '(3,2,1/6)', fontsize=22, color=GOLD, ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=GOLD,
                  linewidth=3))
ax.text(0, -0.6, 'Cabibbo\nDoublet', fontsize=11, color=GOLD,
        ha='center', fontweight='bold')

# Four evidence lines
lines = [
    (0, 2.2, 'GAP RATIO\n218/115 \u2192 38/27',
     'Exact rational\narithmetic\n(PHYS-15)', CYAN),
    (2.2, 0, 'CKM DEFICIT\n0.998 \u2260 1.000',
     'Nuclear \u03b2 + kaon\ndecays\n(Belfatto 2020)', RED),
    (0, -2.2, 'A_FB^b\n0.0992 vs 0.1038',
     'LEP Z pole\n(persistent 25+ yr)', ORANGE),
    (-2.2, 0, 'HIGGS \u03bc\n~1.06\u20131.10',
     'LHC Run 1+2\n(weakest, 2\u03c3)', BLUE),
]

for x, y, label, detail, color in lines:
    # Arrow toward center
    dx = -x * 0.5
    dy = -y * 0.5
    ax.annotate('', xy=(x * 0.4, y * 0.4), xytext=(x, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=3))

    # Label
    ax.text(x * 1.15, y * 1.15, label, fontsize=11, color=color,
            ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(x * 1.15, y * 1.15 - 0.6, detail, fontsize=7, color=SILVER,
            ha='center')

# Bottom
ax.text(0, -2.9, 'Four independent roads from four independent datasets.\n'
        'No shared data, no shared methods, no shared community.\n'
        'All arrive at the same (3,2,1/6) representation.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys19_05_four_evidence_lines.png')


# ================================================================
# FIG 6: |V_ub'| IN CONTEXT OF KNOWN CKM ELEMENTS
# Type: Scale/comparison
# Shows: |V_ub'| ~ 0.045 sits naturally among known CKM elements,
# comparable to |V_cb| ~ 0.041.
# ================================================================

fig, ax = dark_fig("|V_ub'| in Context: A Typical Inter-Generation Mixing",
                   xlabel="CKM matrix element",
                   ylabel="Magnitude |V_ij|  (log scale)")

elements = [
    ('|V_ud|', 0.974, SILVER, 'Dominant\n(same gen)'),
    ('|V_us|', 0.224, CYAN, 'Cabibbo\nangle'),
    ('|V_cb|', 0.041, GREEN, '2nd-3rd gen\nmixing'),
    ("|V_ub'|", 0.045, GOLD, 'NEW\n(1st gen to CD)'),
    ('|V_ub|', 0.004, BLUE, '1st-3rd gen\n(smallest known)'),
]

x_pos = np.arange(len(elements))

for i, (label, value, color, note_text) in enumerate(elements):
    ax.bar(i, value, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    ax.text(i, value * 1.3, '%.3f' % value, fontsize=11, color=color,
            ha='center', fontweight='bold')
    ax.text(i, value * 0.3, note_text, fontsize=7, color=DIM, ha='center')

# Highlight that V_ub' is similar to V_cb
ax.annotate('', xy=(2, 0.041), xytext=(3, 0.045),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=2))
ax.text(2.5, 0.06, 'Comparable\nmagnitudes', fontsize=10, color=WHITE,
        ha='center', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels([e[0] for e in elements], fontsize=10, color=SILVER)
ax.set_yscale('log')
ax.set_xlim(-0.8, 4.8)
ax.set_ylim(0.002, 2)

result_box(ax, 3, 0.5,
           '|V_ub\'| \u2248 0.045 is not anomalously\n'
           'large or small. It sits naturally\n'
           'among known CKM elements \u2014\n'
           'comparable to |V_cb| \u2248 0.041.',
           GOLD, 9)

save_fig(fig, 'phys19_06_vub_prime_context.png')


# ================================================================
# FIG 7: HISTORICAL PARALLEL — PARTICLES PREDICTED BEFORE DISCOVERY
# Type: Timeline/comparison
# Shows: Charm, top, W/Z all had multi-path predictions confirmed.
# The Cabibbo Doublet has the same pattern.
# ================================================================

fig, ax = dark_canvas("Historical Pattern: Multi-Path Prediction \u2192 Discovery",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.text(5, 9.3, 'Particles Predicted Before Discovery', fontsize=16,
        color=GOLD, ha='center', fontweight='bold')

particles = [
    ('Charm Quark', '1970', '1974', 'GIM mechanism (FCNC)\n+ K\u2070 mixing rate',
     '~1.5 GeV', '1.5 GeV', GREEN, 7.5),
    ('W and Z Bosons', '1967', '1983', 'SU(2)\u00d7U(1) gauge theory\n+ neutral currents',
     '80 + 91 GeV', '80 + 91 GeV', CYAN, 5.5),
    ('Top Quark', '1973', '1995', 'KM matrix (integer)\n+ b partner (anomaly)\n+ \u0394\u03c1 (precision)',
     '~170 GeV', '176 GeV', ORANGE, 3.5),
    ('Cabibbo Doublet', '2019-2026', '???', 'Gap ratio (integer)\n+ CKM deficit\n+ A_FB^b + Higgs \u03bc',
     '1.5\u20136 TeV', '???', GOLD, 1.5),
]

for name, predicted, found, evidence, predicted_mass, found_mass, color, y in particles:
    ax.text(0.5, y, name, fontsize=12, color=color, fontweight='bold')
    ax.text(2.8, y, 'Predicted: %s' % predicted, fontsize=8, color=SILVER)
    ax.text(2.8, y - 0.3, 'Found: %s' % found, fontsize=8,
            color=GREEN if found != '???' else DIM)
    ax.text(5.0, y, evidence, fontsize=7, color=SILVER)
    ax.text(7.5, y, 'Predicted: %s' % predicted_mass, fontsize=8, color=SILVER)
    ax.text(9.0, y, found_mass, fontsize=8,
            color=GREEN if found_mass != '???' else GOLD,
            fontweight='bold')

# Headers
for x, header in [(0.5, 'Particle'), (2.8, 'Timeline'), (5.0, 'Evidence Lines'),
                   (7.5, 'Mass'), (9.0, 'Found')]:
    ax.text(x, 8.5, header, fontsize=10, color=WHITE, fontweight='bold')

ax.plot([0.3, 9.7], [8.2, 8.2], color=DIM, linewidth=1, alpha=0.4)

# Highlight the pattern
ax.plot([0.3, 9.7], [2.5, 2.5], color=GOLD, linewidth=2, linestyle='--', alpha=0.3)
ax.text(5, 0.5, 'Multi-path, multi-anomaly, multi-decade convergence\n'
        'has historically preceded experimental confirmation.\n'
        'The Cabibbo Doublet has FOUR independent evidence lines \u2014\n'
        'matching or exceeding the pre-discovery evidence for charm, W/Z, and top.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys19_07_historical_parallel.png')


# ================================================================
# FIG 8: PHYS-19 IDENTITY CARD
# Type: Identity card
# Shows: Three anomalies, two roads, one particle.
# ================================================================

fig, ax = dark_canvas("PHYS-19 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THREE EXPERIMENTS. TWO ROADS. ONE PARTICLE.',
        fontsize=18, color=GOLD, ha='center', fontweight='bold')
ax.text(5, 8.5, 'The data was already there. The connection was not.',
        fontsize=11, color=SILVER, ha='center', style='italic')

# The three anomalies — left
ax.text(2.5, 7.5, 'THREE ANOMALIES', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

anom_items = [
    ('CKM deficit', '2.5\u20134\u03c3', 'Nuclear \u03b2 + kaon', RED),
    ('A_FB^b', '~3\u03c3', 'LEP (1993\u20132000)', ORANGE),
    ('Higgs \u03bc', '~2\u03c3', 'LHC (2012\u2013now)', BLUE),
]
for i, (name, sig, source, color) in enumerate(anom_items):
    y = 6.7 - i * 0.7
    ax.text(1.0, y, name, fontsize=10, color=color, fontweight='bold')
    ax.text(2.5, y, sig, fontsize=9, color=SILVER)
    ax.text(4.0, y, source, fontsize=8, color=DIM)

# The two roads — right
ax.text(7.5, 7.5, 'TWO ROADS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

road_items = [
    ('Gap ratio', '38/27 = 1.407', 'M_GUT = 10^{15.5}', CYAN),
    ('Anomaly fit', 'M = 1.5\u20136 TeV', '|V_ub\'| \u2248 0.045', ORANGE),
]
for i, (road, result, detail, color) in enumerate(road_items):
    y = 6.7 - i * 0.7
    ax.text(6.0, y, road, fontsize=10, color=color, fontweight='bold')
    ax.text(7.5, y, result, fontsize=9, color=color)
    ax.text(9.0, y, detail, fontsize=8, color=DIM)

# The particle — center
ax.text(5, 4.5, '(3, 2, 1/6)', fontsize=24, color=GOLD,
        ha='center', fontweight='bold', fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=3))
ax.text(5, 3.7, 'THE CABIBBO DOUBLET', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')

# Key facts
ax.plot([0.5, 9.5], [2.8, 2.8], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

facts = [
    ('Independence:', '12 orders of magnitude, no shared data', SILVER),
    ('Each anomaly:', 'uses a different quantum number', CYAN),
    ('Mass window:', '1.5\u20136 TeV (< half a decade)', ORANGE),
    ('Tests:', 'Hyper-K (proton), HL-LHC (direct), Belle II (CKM)', GREEN),
]
for i, (label, detail, color) in enumerate(facts):
    y = 2.2 - i * 0.5
    ax.text(2.5, y, label, fontsize=9, color=SILVER)
    ax.text(6.0, y, detail, fontsize=9, color=color, fontweight='bold')

save_fig(fig, 'phys19_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-19 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys19_01_quantum_number_map.png',
    'phys19_02_mass_window_timeline.png',
    'phys19_03_test_matrix.png',
    'phys19_04_twelve_orders.png',
    'phys19_05_four_evidence_lines.png',
    'phys19_06_vub_prime_context.png',
    'phys19_07_historical_parallel.png',
    'phys19_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    