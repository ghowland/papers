#!/usr/bin/env python3
"""
HOWL CULT-18 Diagrams — Closing Physics at Scale
8 figures covering the coverage matrix methodology, BBN results,
precision architecture, velocity comparison, and domain coverage.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================


# Light mode
if True:
    # ── Global palette (Kindle / light mode) ──
    BG      = '#ffffff'
    PAN     = '#f0ede8'
    GOLD    = '#a07820'
    SILVER  = '#505860'
    CYAN    = '#1a8a80'
    MAG     = '#a03058'
    BLUE    = '#2855a0'
    GREEN   = '#2a7a3a'
    RED     = '#b82020'
    ORANGE  = '#c06a18'
    WHITE   = '#1a1a22'
    DIM     = '#908e88'
    PURPLE  = '#6040a0'
else:
    # ── Global palette (D7.2) ──
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


outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=12)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=12)

# ================================================================
# FIG 1: BBN DERIVATION CHAIN
# Type: Progression/Sequence (Type 7)
# Shows: The cross-domain chain from gauge integers through
#        cosmological parameters to nuclear abundances, with
#        computed values and miss percentages at each stage.
#        Three physics domains connected in one executable chain.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-1.5, 8.5)

# Domain background bands
domain_bands = [
    ((-0.3, -0.8), 3.1, 8.8, '#1a1a3a', 'PARTICLE\nPHYSICS'),
    ((2.8, -0.8), 3.4, 8.8, '#1a2a1a', 'COSMOLOGY'),
    ((6.2, -0.8), 4.1, 8.8, '#2a1a1a', 'NUCLEAR\nPHYSICS'),
]
for (x, y), w, h, c, label in domain_bands:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15',
                                   facecolor=c, edgecolor=DIM, linewidth=0.8, alpha=0.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 0.3, label, ha='center', va='top',
            color=DIM, fontsize=8, fontstyle='italic')

# Chain nodes
nodes = [
    (1.0, 6.5, 'Gauge Integers', '11, 13', CYAN, 'From SU(2)\nbeta structure'),
    (1.0, 3.5, 'DM/Baryon\nPrefactor', '22/13', CYAN, 'Exact fraction'),
    (4.0, 6.5, 'Baryon Density\n$\\Omega_b$', '0.04904', GREEN, 'Planck: 0.0490\nMiss: 0.073%'),
    (4.0, 3.5, 'Baryon-to-Photon\n$\\eta_{10}$', '6.090', GREEN, 'Planck: 6.104\nMiss: 0.24%'),
    (7.5, 6.5, 'Deuterium\nD/H', '2.531e-5', GOLD, 'Measured: 2.527e-5\nMiss: 0.14%'),
    (7.5, 3.5, 'Helium-4\n$Y_p$', '0.2486', ORANGE, 'Measured: 0.2449\nMiss: 1.53%'),
]

for (x, y, title, value, color, note) in nodes:
    box = patches.FancyBboxPatch((x - 0.85, y - 0.7), 1.7, 1.4,
                                  boxstyle='round,pad=0.2',
                                  facecolor=PAN, edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.3, title, ha='center', va='center',
            color=WHITE, fontsize=9, fontweight='bold')
    ax.text(x, y - 0.15, value, ha='center', va='center',
            color=color, fontsize=11, fontweight='bold')
    ax.text(x, y - 0.95, note, ha='center', va='top',
            color=SILVER, fontsize=7)

# Arrows connecting nodes
arrow_style = dict(arrowstyle='->', color=SILVER, lw=1.8, connectionstyle='arc3,rad=0')
arrow_pairs = [
    ((1.0, 5.8), (1.0, 4.25)),      # integers -> prefactor
    ((1.85, 3.5), (3.15, 3.5)),      # prefactor -> eta (through omega_b)
    ((1.85, 6.5), (3.15, 6.5)),      # integers -> omega_b
    ((4.0, 5.8), (4.0, 4.25)),       # omega_b -> eta
    ((4.85, 6.5), (6.65, 6.5)),      # eta -> D/H
    ((4.85, 3.5), (6.65, 3.5)),      # eta -> Y_p
]
for start, end in arrow_pairs:
    ax.annotate('', xy=end, xytext=start, arrowprops=arrow_style)

# Arrow labels
ax.text(1.25, 5.1, '$\\times \\pi$', ha='left', va='center', color=CYAN, fontsize=9)
ax.text(2.5, 6.8, '$\\Omega_{DM}$ / ratio', ha='center', va='bottom', color=SILVER, fontsize=8)
ax.text(4.25, 5.1, 'CMB + Bose-\nEinstein', ha='left', va='center', color=SILVER, fontsize=7)
ax.text(5.7, 6.8, 'Pitrou 2018\na=2.57, b=-0.44', ha='center', va='bottom', color=SILVER, fontsize=7)
ax.text(5.7, 3.2, 'Pitrou 2018\na=0.2485, b=0.0016', ha='center', va='top', color=SILVER, fontsize=7)

# Verdict badges
badge_data = [
    (9.2, 6.8, 'PASS', '3-digit\nmatch', GREEN),
    (9.2, 6.1, 'PASS', '0.12$\\sigma$', GREEN),
    (9.2, 3.8, 'PASS', '0.94$\\sigma$', GREEN),
    (9.2, 3.1, 'FAIL', '2-digit\nonly', RED),
]
for (x, y, verdict, detail, color) in badge_data:
    ax.text(x, y, verdict, ha='center', va='center', color=color,
            fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, linewidth=1.5))
    ax.text(x, y - 0.4, detail, ha='center', va='top', color=DIM, fontsize=7)

ax.set_title('BBN Derivation Chain: Gauge Integers to Nuclear Abundances',
             color=GOLD, fontsize=16, fontweight='bold', pad=25)

save(fig, 'cult18_01_bbn_chain.png')

# ================================================================
# FIG 2: R2 = pi/4 CROSS-DOMAIN CONNECTIONS
# Type: Connection/Integer Map (Type 5)
# Shows: The single geometric factor pi/4 appearing in four
#        different physics domains with the actual equations
#        and precision standards. The shared constant makes
#        cross-domain structure visible.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.set_xlim(-2, 12)
ax.set_ylim(-1, 11)

# Central node
central_x, central_y = 5.0, 5.5
circle = plt.Circle((central_x, central_y), 1.2, facecolor=PAN,
                     edgecolor=GOLD, linewidth=3)
ax.add_patch(circle)
ax.text(central_x, central_y + 0.25, '$R_2 = \\pi/4$', ha='center', va='center',
        color=GOLD, fontsize=18, fontweight='bold')
ax.text(central_x, central_y - 0.35, '= 0.785398...',
        ha='center', va='center', color=SILVER, fontsize=10)

# Domain nodes
domains = [
    (0.5, 9.5, 'PIPE FLOW', '$Q = R_2 \\cdot d^2 \\cdot v$',
     'Coordinator: velocity $v$', 'Coriolis: 0.05%', CYAN),
    (9.5, 9.5, 'DRAG FORCE', '$F = \\frac{1}{2}\\rho v^2 R_2 d^2 C_d$',
     'Coordinator: drag coeff $C_d$', 'Wind tunnel: 1%', BLUE),
    (0.5, 1.5, 'ORIFICE FLOW', '$q = C_d R_2 d^2 \\sqrt{2\\Delta P/\\rho}$',
     'Coordinator: discharge $C_d$', 'ISO 5167: 0.5%', GREEN),
    (9.5, 1.5, 'CAPACITANCE', '$C = \\varepsilon_0 R_2 d^2 / t$',
     'Coordinator: permittivity $\\varepsilon$', 'pF precision', MAG),
]

for (x, y, title, equation, coord, precision, color) in domains:
    box_w, box_h = 3.2, 2.4
    box = patches.FancyBboxPatch((x - box_w/2, y - box_h/2), box_w, box_h,
                                  boxstyle='round,pad=0.25',
                                  facecolor=PAN, edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y + 0.7, title, ha='center', va='center',
            color=color, fontsize=11, fontweight='bold')
    ax.text(x, y + 0.05, equation, ha='center', va='center',
            color=WHITE, fontsize=10)
    ax.text(x, y - 0.55, coord, ha='center', va='center',
            color=SILVER, fontsize=8)
    ax.text(x, y - 0.95, precision, ha='center', va='center',
            color=DIM, fontsize=8,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=DIM, linewidth=0.8))

# Arrows from center to domains
for (x, y, _, _, _, _, color) in domains:
    dx = x - central_x
    dy = y - central_y
    dist = np.sqrt(dx**2 + dy**2)
    start_x = central_x + 1.3 * dx / dist
    start_y = central_y + 1.3 * dy / dist
    end_x = x - 1.7 * dx / dist
    end_y = y - 1.3 * dy / dist
    ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                                connectionstyle='arc3,rad=0'))

ax.text(5.0, 10.5, '$\\pi/4$: The Cross-Section Invariant Across Four Domains',
        ha='center', va='center', color=GOLD, fontsize=16, fontweight='bold')
ax.text(5.0, -0.3, 'One geometric factor. Four domains. Each independently validated to stated precision.',
        ha='center', va='center', color=SILVER, fontsize=10)

save(fig, 'cult18_02_r2_connections.png')

# ================================================================
# FIG 3: PRECISION TOWER
# Type: Scale/Landscape (Type 2)
# Shows: The hierarchy of precision from exact SI constants
#        at the base through exact group-theory fractions
#        through 2^335 transcendentals to measured values.
#        The tower shows that the foundation is MORE precise
#        than the measurements built on it.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.set_xlim(-1, 11)
ax.set_ylim(-0.5, 12)

# Tower levels from bottom (most precise) to top (least precise)
levels = [
    (0.5, 0.5, 9.0, 2.0, 'SI 2019 EXACT CONSTANTS', GOLD,
     'Infinite precision — defined exact by international agreement',
     ['c = 299,792,458 m/s', 'h = 6.62607015e-34 J\u00b7s',
      'e = 1.602176634e-19 C', 'k_B = 1.380649e-23 J/K'],
     '\u221e digits'),
    (1.0, 3.0, 8.0, 2.0, 'GROUP THEORY EXACT FRACTIONS', CYAN,
     'Exact rational — derived from gauge group structure',
     ['b\u2081 = 41/10', 'b\u2082 = -19/6', 'b\u2083 = -7',
      'a\u2081 (Schwinger) = 1/2'],
     '\u221e digits'),
    (1.5, 5.5, 7.0, 2.0, 'TRANSCENDENTALS (2\u00b3\u00b3\u2075 BASIS)', BLUE,
     'Rational approximation — bounded error < 10\u207b\u00b9\u2070\u2070',
     ['\u03c0, e, \u03b6(3), \u03b6(5)', 'ln(2), ln(3), \u221a2, \u221a3',
      'K(k), E(k) at specific moduli', 'Catalan, Li\u2084 ... Li\u2087'],
     '100+ digits'),
    (2.0, 8.0, 6.0, 2.0, 'MEASURED VALUES', MAG,
     'Finite precision — from CODATA, PDG, Planck',
     ['\u03b1 = 7.297e-3 (\u00b1 0.3 ppb)', '\u03a9_b = 0.0490 (\u00b1 ~1%)',
      'D/H = 2.527e-5 (\u00b1 1.2%)', 'G = 6.674e-11 (\u00b1 22 ppm)'],
     '4\u201315 digits'),
]

for (x, y, w, h, title, color, desc, examples, precision) in levels:
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.2',
                                  facecolor=PAN, edgecolor=color, linewidth=2.5,
                                  alpha=0.9)
    ax.add_patch(box)
    ax.text(x + 0.4, y + h - 0.25, title, ha='left', va='top',
            color=color, fontsize=11, fontweight='bold')
    ax.text(x + 0.4, y + h - 0.65, desc, ha='left', va='top',
            color=SILVER, fontsize=8)

    ex_text = '    '.join(examples)
    ax.text(x + w/2, y + 0.5, ex_text, ha='center', va='center',
            color=WHITE, fontsize=8)

    ax.text(x + w - 0.3, y + h - 0.25, precision, ha='right', va='top',
            color=GOLD, fontsize=10, fontweight='bold')

# Vertical arrow showing precision direction
ax.annotate('', xy=(0.2, 9.8), xytext=(0.2, 0.7),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))
ax.text(-0.2, 5.5, 'DECREASING\nPRECISION', ha='center', va='center',
        color=DIM, fontsize=9, rotation=90)

ax.text(5.0, 11.5, 'The Precision Tower: Foundation More Exact Than Measurements',
        ha='center', va='center', color=GOLD, fontsize=15, fontweight='bold')
ax.text(5.0, 10.8, 'Exact arithmetic ensures derivation error is zero.\n'
        'All disagreement with measurement is in the physics, not the arithmetic.',
        ha='center', va='center', color=SILVER, fontsize=9)

save(fig, 'cult18_03_precision_tower.png')

# ================================================================
# FIG 4: BBN COMPARISON RESULTS
# Type: Comparison Bar Chart (Type 6)
# Shows: All 13 BBN comparisons as horizontal bars on a log
#        scale of miss percentage, color-coded by verdict.
#        The spread from 0.024% to 10.9% is immediately visible.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title='BBN Experiment: 13 Pre-Registered Comparisons',
         xlabel='Miss Percentage (log scale)', ylabel='')

comparisons = [
    ('D/H digits', 0.024, 'PASS', GREEN),
    ('\u03a9_b vs Planck', 0.073, 'INFO', BLUE),
    ('D/H vs measured', 0.143, 'INFO', BLUE),
    ('\u03a9_DE vs Planck', 0.198, 'INFO', BLUE),
    ('\u03b7 vs Planck', 0.237, 'INFO', BLUE),
    ('\u03a9_m vs Planck', 0.439, 'INFO', BLUE),
    ('\u03c1_\u039b g/cm\u00b3 vs obs', 0.152, 'INFO', BLUE),
    ('Y_p vs measured', 1.528, 'INFO', BLUE),
    ('Y_p digits', 1.487, 'FAIL', RED),
    ('N_eff vs Planck', 9.296, 'INFO', BLUE),
    ('\u03c1_\u039b GeV\u2074 vs obs', 10.94, 'INFO', BLUE),
    ('N_eff vs 3.044', 10.90, 'INFO', BLUE),
]

comparisons_sorted = sorted(comparisons, key=lambda x: x[1])

y_positions = np.arange(len(comparisons_sorted))
labels = [c[0] for c in comparisons_sorted]
values = [c[1] for c in comparisons_sorted]
colors = [c[3] for c in comparisons_sorted]
verdicts = [c[2] for c in comparisons_sorted]

bars = ax.barh(y_positions, values, height=0.6, color=colors, alpha=0.7,
               edgecolor=[c for c in colors], linewidth=1.5)

ax.set_xscale('log')
ax.set_xlim(0.01, 30)
ax.set_ylim(-0.8, len(comparisons_sorted) - 0.2)
ax.set_yticks(y_positions)
ax.set_yticklabels(labels, fontsize=9, color=SILVER)

# Value labels on bars
for i, (val, verdict, color) in enumerate(zip(values, verdicts, colors)):
    label_x = val * 1.3 if val < 15 else val * 0.5
    ax.text(label_x, i, '%.3f%%' % val, ha='left', va='center',
            color=WHITE, fontsize=8, fontweight='bold')
    ax.text(0.013, i, verdict, ha='left', va='center',
            color=color, fontsize=8, fontweight='bold')

# Threshold lines
ax.axvline(x=1.0, color=ORANGE, linestyle='--', linewidth=1.5, alpha=0.5)
ax.text(1.0, len(comparisons_sorted) - 0.5, '1%', ha='center', va='bottom',
        color=ORANGE, fontsize=9)

ax.axvline(x=0.1, color=GREEN, linestyle='--', linewidth=1.5, alpha=0.5)
ax.text(0.1, len(comparisons_sorted) - 0.5, '0.1%', ha='center', va='bottom',
        color=GREEN, fontsize=9)

# Summary box
summary_text = '4 PASS  |  1 FAIL  |  8 INFO\n57 output values  |  7 derivations'
ax.text(15, 1.5, summary_text, ha='center', va='center',
        color=WHITE, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

save(fig, 'cult18_04_bbn_comparisons.png')

# ================================================================
# FIG 5: VELOCITY COMPARISON
# Type: Scale/Landscape (Type 2)
# Shows: The structural time difference between institutional
#        peer review and platform experiment execution on a
#        log scale. The orders-of-magnitude gap is spatial.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 8.5)

# Log time axis (horizontal)
time_points = [
    (0.5, '1 second', CYAN),
    (1.5, '1 minute', CYAN),
    (2.5, '1 hour', GREEN),
    (4.0, '1 day', GREEN),
    (5.5, '1 week', ORANGE),
    (6.5, '1 month', ORANGE),
    (7.5, '3 months', RED),
    (8.5, '6 months', RED),
    (9.5, '1 year+', RED),
]

# Time axis line
ax.plot([0.2, 9.8], [4.0, 4.0], color=DIM, linewidth=1.5)
for x, label, color in time_points:
    ax.plot(x, 4.0, 'o', color=color, markersize=6)
    ax.text(x, 3.5, label, ha='center', va='top', color=color, fontsize=8, rotation=35)

# Platform events (top)
platform_events = [
    (0.5, 6.5, 'Run\nexperiment', 'Runner executes\n7 derivations', CYAN),
    (1.5, 6.5, 'Fork &\nmodify', 'Change 1 input\nre-run', CYAN),
    (2.5, 6.5, '100\nexperiments', 'One contributor\none day', GREEN),
    (4.0, 6.5, 'Community\nreview', 'Merge request\nevaluated', GREEN),
]

for x, y, title, detail, color in platform_events:
    box = patches.FancyBboxPatch((x - 0.55, y - 0.55), 1.1, 1.1,
                                  boxstyle='round,pad=0.15',
                                  facecolor=PAN, edgecolor=color, linewidth=1.8)
    ax.add_patch(box)
    ax.text(x, y + 0.15, title, ha='center', va='center',
            color=color, fontsize=9, fontweight='bold')
    ax.text(x, y - 0.8, detail, ha='center', va='top', color=SILVER, fontsize=7)

ax.text(2.0, 7.8, 'PLATFORM', ha='center', va='center',
        color=CYAN, fontsize=14, fontweight='bold')

# Institutional events (bottom)
inst_events = [
    (4.0, 1.5, 'Write\npaper', '15-30 pages\nprose', ORANGE),
    (5.5, 1.5, 'Submit &\nscreen', 'Editorial\nassessment', ORANGE),
    (6.5, 1.5, 'Peer\nreview', '2-3 reviewers\nread prose', RED),
    (7.5, 1.5, 'Revise &\nresubmit', 'Address\ncomments', RED),
    (9.0, 1.5, 'Publish', 'Accepted\nformatted', RED),
]

for x, y, title, detail, color in inst_events:
    box = patches.FancyBboxPatch((x - 0.55, y - 0.55), 1.1, 1.1,
                                  boxstyle='round,pad=0.15',
                                  facecolor=PAN, edgecolor=color, linewidth=1.8)
    ax.add_patch(box)
    ax.text(x, y + 0.15, title, ha='center', va='center',
            color=color, fontsize=9, fontweight='bold')
    ax.text(x, y - 0.8, detail, ha='center', va='top', color=SILVER, fontsize=7)

ax.text(6.5, 0.0, 'INSTITUTION', ha='center', va='center',
        color=RED, fontsize=14, fontweight='bold')

# Highlight the gap
ax.annotate('', xy=(0.5, 5.5), xytext=(0.5, 4.3),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax.annotate('', xy=(9.0, 2.6), xytext=(9.0, 3.7),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))

ax.text(5.0, 8.2, 'Velocity: Platform vs Institution',
        ha='center', va='center', color=GOLD, fontsize=16, fontweight='bold')
ax.text(5.0, -0.2, 'Same result. Different time. The gap is structural, not incremental.',
        ha='center', va='center', color=SILVER, fontsize=10)

save(fig, 'cult18_05_velocity_comparison.png')

# ================================================================
# FIG 6: ANTI-SMUGGLING BOUNDARY
# Type: Geometric Cross-Section (Type 4)
# Shows: The experiment definition as a containment boundary
#        with declared inputs as the only entry points, the
#        runner as the gate that rejects undeclared keys.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.set_xlim(-2, 14)
ax.set_ylim(-1.5, 11)

# Outer boundary: experiment definition
outer = patches.FancyBboxPatch((1.5, 0.5), 10, 8.5, boxstyle='round,pad=0.4',
                                facecolor='#0d0d1a', edgecolor=GOLD, linewidth=3,
                                linestyle='-')
ax.add_patch(outer)
ax.text(6.5, 9.3, 'EXPERIMENT DEFINITION BOUNDARY', ha='center', va='center',
        color=GOLD, fontsize=13, fontweight='bold')
ax.text(6.5, 8.7, 'Only declared dependencies may enter', ha='center', va='center',
        color=SILVER, fontsize=9)

# Declared inputs (inside, left side)
declared_inputs = [
    'si_speed_of_light_v0',
    'cosmo_omega_dm_planck_v0',
    'integer_yang_mills_eleven_v0',
    'bbn_dh_a_coeff_v0',
    'geom_pi_v0',
]

ax.text(3.5, 7.5, 'DECLARED INPUTS', ha='center', va='center',
        color=GREEN, fontsize=10, fontweight='bold')

for i, key in enumerate(declared_inputs):
    y = 6.5 - i * 1.1
    box = patches.FancyBboxPatch((2.2, y - 0.3), 2.8, 0.6,
                                  boxstyle='round,pad=0.12',
                                  facecolor=PAN, edgecolor=GREEN, linewidth=1.2)
    ax.add_patch(box)
    ax.text(3.6, y, key, ha='center', va='center', color=GREEN, fontsize=7)
    # Arrow from declared to runner
    ax.annotate('', xy=(6.0, y), xytext=(5.1, y),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2, alpha=0.6))

# Runner (center)
runner_box = patches.FancyBboxPatch((5.8, 1.5), 2.4, 6.0,
                                     boxstyle='round,pad=0.2',
                                     facecolor=PAN, edgecolor=CYAN, linewidth=2.5)
ax.add_patch(runner_box)
ax.text(7.0, 7.0, 'RUNNER', ha='center', va='center',
        color=CYAN, fontsize=12, fontweight='bold')
ax.text(7.0, 6.3, 'Resolves keys\nagainst store', ha='center', va='center',
        color=SILVER, fontsize=8)
ax.text(7.0, 4.5, 'Executes\nderivations', ha='center', va='center',
        color=SILVER, fontsize=8)
ax.text(7.0, 3.0, 'Evaluates\ncomparisons', ha='center', va='center',
        color=SILVER, fontsize=8)

# Output (inside, right side)
ax.text(9.8, 7.5, 'OUTPUTS', ha='center', va='center',
        color=GOLD, fontsize=10, fontweight='bold')

outputs = ['PASS: 4', 'FAIL: 1', 'INFO: 8', '57 values']
output_colors = [GREEN, RED, BLUE, SILVER]
for i, (label, color) in enumerate(zip(outputs, output_colors)):
    y = 6.5 - i * 1.1
    box = patches.FancyBboxPatch((9.0, y - 0.3), 1.8, 0.6,
                                  boxstyle='round,pad=0.12',
                                  facecolor=PAN, edgecolor=color, linewidth=1.2)
    ax.add_patch(box)
    ax.text(9.9, y, label, ha='center', va='center', color=color, fontsize=9)
    ax.annotate('', xy=(8.9, y), xytext=(8.3, y),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.2, alpha=0.6))

# Undeclared values (outside, rejected)
undeclared = [
    (-0.5, 5.5, 'hidden_constant_x'),
    (-0.5, 3.5, 'hardcoded_0.042'),
    (-0.5, 1.5, 'untracked_fudge'),
]

for x, y, label in undeclared:
    box = patches.FancyBboxPatch((x - 0.9, y - 0.3), 2.2, 0.6,
                                  boxstyle='round,pad=0.12',
                                  facecolor='#1a0a0a', edgecolor=RED, linewidth=1.5,
                                  linestyle='--')
    ax.add_patch(box)
    ax.text(x + 0.2, y, label, ha='center', va='center', color=RED, fontsize=7)
    # Rejected arrow
    ax.annotate('', xy=(1.3, y), xytext=(x + 1.2, y),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))
    ax.text(1.5, y + 0.35, '\u2717', ha='center', va='center', color=RED, fontsize=14)

ax.text(-0.5, 7.5, 'UNDECLARED', ha='center', va='center',
        color=RED, fontsize=10, fontweight='bold')
ax.text(-0.5, 7.0, 'Not in dependencies\n= cannot enter', ha='center', va='center',
        color=DIM, fontsize=8)

ax.text(6.5, 10.2, 'Anti-Smuggling: Architectural Enforcement',
        ha='center', va='center', color=GOLD, fontsize=15, fontweight='bold')
ax.text(6.5, -1.0, 'The infrastructure has no mechanism for undeclared values to participate.',
        ha='center', va='center', color=SILVER, fontsize=10)

save(fig, 'cult18_06_anti_smuggling.png')

# ================================================================
# FIG 7: BBN SIGMA DEVIATIONS
# Type: Threshold/Region (Type 3)
# Shows: D/H, Y_p, and N_eff sigma deviations plotted on a
#        0-3 sigma number line with 1-sigma and 2-sigma
#        regions shaded. Shows WHERE predictions fall relative
#        to measurement uncertainty.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 8))
fig.patch.set_facecolor(BG)
style_ax(ax, title='BBN Chain: Sigma Deviations from Measurement',
         xlabel='Standard Deviations ($\\sigma$) from Measured Value',
         ylabel='')

# Shaded regions
ax.axvspan(0, 1.0, alpha=0.12, color=GREEN)
ax.axvspan(1.0, 2.0, alpha=0.08, color=ORANGE)
ax.axvspan(2.0, 3.5, alpha=0.06, color=RED)

# Region labels
ax.text(0.5, 4.8, 'Within 1$\\sigma$', ha='center', va='center',
        color=GREEN, fontsize=11, alpha=0.7)
ax.text(1.5, 4.8, '1-2$\\sigma$', ha='center', va='center',
        color=ORANGE, fontsize=11, alpha=0.7)
ax.text(2.5, 4.8, '> 2$\\sigma$', ha='center', va='center',
        color=RED, fontsize=11, alpha=0.7)

# Data points
sigma_data = [
    ('D/H (deuterium)', 0.120, GREEN, 'Miss: 0.14%\n3-digit match'),
    ('Y_p (helium-4)', 0.936, GREEN, 'Miss: 1.53%\nWithin 1$\\sigma$'),
    ('N_eff (neutrino)', 1.635, ORANGE, 'Miss: 10.9%\nTension'),
    ('\u03a9_b (baryon density)', 0.073, GREEN, 'Miss: 0.073%\nSub-permille'),
]

y_positions = [3.5, 2.5, 1.5, 0.5]

for i, (label, sigma, color, note) in enumerate(sigma_data):
    y = y_positions[i]
    ax.scatter(sigma, y, s=300, color=color, edgecolors=WHITE,
               linewidth=2, zorder=5)
    ax.text(-0.15, y, label, ha='right', va='center',
            color=WHITE, fontsize=10, fontweight='bold')
    ax.text(sigma + 0.15, y + 0.2, '%.3f$\\sigma$' % sigma,
            ha='left', va='bottom', color=color, fontsize=10, fontweight='bold')
    ax.text(sigma + 0.15, y - 0.15, note, ha='left', va='top',
            color=SILVER, fontsize=8)

# Vertical threshold lines
ax.axvline(x=1.0, color=ORANGE, linestyle='--', linewidth=1.5, alpha=0.6)
ax.axvline(x=2.0, color=RED, linestyle='--', linewidth=1.5, alpha=0.6)

ax.set_xlim(-0.3, 3.5)
ax.set_ylim(-0.3, 5.5)
ax.set_yticks([])

# Summary
ax.text(2.8, 3.5, 'D/H: 0.12$\\sigma$\ndeep inside\nmeasurement\nuncertainty',
        ha='center', va='center', color=DIM, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, linewidth=0.8))

save(fig, 'cult18_07_sigma_deviations.png')

# ================================================================
# FIG 8: DOMAIN COVERAGE STATUS
# Type: Comparison Bar Chart (Type 6)
# Shows: 16 physics domains with current experiment counts,
#        revealing the coverage imbalance — some domains have
#        10 experiments, others have zero.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, title='Coverage Matrix: Current Experiment Count by Domain',
         xlabel='Number of Experiments', ylabel='')

domains_data = [
    ('QED', 10, CYAN),
    ('Electroweak', 9, BLUE),
    ('Cosmology', 4, PURPLE),
    ('GR / Gravity', 3, GREEN),
    ('BBN', 2, GOLD),
    ('Lepton masses', 3, CYAN),
    ('Dark matter', 1, PURPLE),
    ('Atomic / Hydrogen', 1, BLUE),
    ('GUT / Proton decay', 1, ORANGE),
    ('Cross-domain geometry', 1, GOLD),
    ('CKM mixing', 1, GREEN),
    ('QCD / Confinement', 1, RED),
    ('Nuclear', 0, DIM),
    ('Quark masses', 0, DIM),
    ('PMNS mixing', 0, DIM),
    ('Neutrino', 0, DIM),
]

domains_data_sorted = sorted(domains_data, key=lambda x: x[1])

y_positions = np.arange(len(domains_data_sorted))
labels = [d[0] for d in domains_data_sorted]
values = [d[1] for d in domains_data_sorted]
colors = [d[2] for d in domains_data_sorted]

bars = ax.barh(y_positions, values, height=0.65, color=colors, alpha=0.7,
               edgecolor=colors, linewidth=1.5)

# Zero-count domains get a marker
for i, (label, val, color) in enumerate(domains_data_sorted):
    if val == 0:
        ax.text(0.15, i, 'EMPTY', ha='left', va='center',
                color=RED, fontsize=9, fontweight='bold')
    else:
        ax.text(val + 0.2, i, str(val), ha='left', va='center',
                color=WHITE, fontsize=10, fontweight='bold')

ax.set_xlim(-0.5, 13)
ax.set_ylim(-0.8, len(domains_data_sorted) - 0.2)
ax.set_yticks(y_positions)
ax.set_yticklabels(labels, fontsize=9, color=SILVER)

# Annotation
total_exp = sum(values)
filled_domains = sum(1 for v in values if v > 0)
empty_domains = sum(1 for v in values if v == 0)

summary = '%d experiments across %d domains\n%d domains empty — each is a contribution opportunity' % (
    total_exp, filled_domains, empty_domains)
ax.text(8.5, 3.0, summary, ha='center', va='center',
        color=WHITE, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

save(fig, 'cult18_08_domain_coverage.png')

# ================================================================
# SUMMARY
# ================================================================

print("\nCULT-18 Diagrams Complete:")
print("  cult18_01_bbn_chain.png")
print("  cult18_02_r2_connections.png")
print("  cult18_03_precision_tower.png")
print("  cult18_04_bbn_comparisons.png")
print("  cult18_05_velocity_comparison.png")
print("  cult18_06_anti_smuggling.png")
print("  cult18_07_sigma_deviations.png")
print("  cult18_08_domain_coverage.png")