#!/usr/bin/env python3
"""
HOWL PHYS-3 Diagrams — G Has Never Been Tested Outside Earth's Soliton Boundary
8 figures covering Hill sphere scale, nested boundaries, G disagreements, proposed experiment.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: EARTH-TO-HILL-SPHERE LOG SCALE
# Type: Scale/landscape
# Shows: Every G measurement location on a log-distance axis from
# Earth's surface to the Hill sphere. All measurements cluster
# at <1% of the boundary distance. The gap is visual.
# ================================================================

fig, ax = dark_fig("Every G Measurement: Deep Inside the Hill Sphere",
                   xlabel="Distance from Earth center (km, log scale)",
                   ylabel="",
                   size=(18, 10))

# Measurement locations (distance from Earth center in km)
locations = [
    (6371, 'Earth surface\n(all torsion balances)', RED, 'surface'),
    (6771, 'ISS (400 km alt)', ORANGE, 'ISS'),
    (26560, 'GPS satellites', BLUE, 'GPS'),
    (384400, 'Moon', CYAN, 'Moon'),
    (1491000, 'L1 (DSCOVR, SOHO)', GREEN, 'L1'),
    (1501000, 'L2 (JWST, Gaia)', GREEN, 'L2'),
    (1500000, 'HILL SPHERE\nBOUNDARY', GOLD, 'boundary'),
]

# Plot on log scale
for i, (dist, label, color, tag) in enumerate(locations):
    y_pos = 0.5
    data_point(ax, np.log10(dist), y_pos, '', color, size=250)

    # Stagger labels to avoid overlap
    if tag == 'surface':
        ax.annotate(label, xy=(np.log10(dist), y_pos),
                    xytext=(np.log10(dist), 1.5),
                    fontsize=9, color=color, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
    elif tag == 'ISS':
        ax.annotate(label, xy=(np.log10(dist), y_pos),
                    xytext=(np.log10(dist) + 0.15, 1.8),
                    fontsize=9, color=color, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0))
    elif tag == 'GPS':
        ax.annotate(label, xy=(np.log10(dist), y_pos),
                    xytext=(np.log10(dist), 1.5),
                    fontsize=9, color=color, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0))
    elif tag == 'Moon':
        ax.annotate(label, xy=(np.log10(dist), y_pos),
                    xytext=(np.log10(dist), 1.5),
                    fontsize=9, color=color, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0))
    elif tag in ['L1', 'L2']:
        dy = 1.5 if tag == 'L1' else 1.8
        ax.annotate(label, xy=(np.log10(dist), y_pos),
                    xytext=(np.log10(dist), dy),
                    fontsize=9, color=color, fontweight='bold', ha='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0))
    elif tag == 'boundary':
        ax.plot([np.log10(dist), np.log10(dist)], [-0.5, 2.3], color=GOLD,
                linewidth=3, linestyle='--', alpha=0.7)
        ax.text(np.log10(dist) + 0.05, 2.5, label, fontsize=12, color=GOLD,
                ha='center', fontweight='bold')

# Shade G measurement region
shaded_region(ax, np.log10(5000), np.log10(7000), RED, 0.10)
ax.text(np.log10(6371), -0.6, 'ALL direct G measurements\nare HERE (0.42% of boundary)',
        fontsize=11, color=RED, ha='center', fontweight='bold')

# Percentages
pcts = [
    (6371, '0.42%'),
    (6771, '0.45%'),
    (26560, '1.8%'),
    (384400, '25.6%'),
]
for dist, pct in pcts:
    ax.text(np.log10(dist), -0.2, pct, fontsize=8, color=DIM, ha='center')

ax.set_xlim(3.5, 6.5)
ax.set_ylim(-1.2, 3.0)
ax.set_yticks([])

save_fig(fig, 'phys3_01_hill_sphere_scale.png')


# ================================================================
# FIG 2: NESTED BOUNDARY HIERARCHY
# Type: Geometric cross-section
# Shows: Earth Hill sphere inside Solar system Hill sphere inside
# Galactic boundary. Every measurement ever made is inside all
# three. The nesting at log scale is impossible in text.
# ================================================================

fig, ax = dark_canvas("Nested Boundaries: Every Measurement Inside All Three",
                      size=(16, 16))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Galactic boundary (outermost)
gal = plt.Circle((0, 0), 4.0, fill=True, facecolor=PURPLE,
                   alpha=0.05, edgecolor=PURPLE, linewidth=2, linestyle='--',
                   zorder=1)
ax.add_patch(gal)
ax.text(0, 4.3, 'GALACTIC BOUNDARY', fontsize=12, color=PURPLE,
        ha='center', fontweight='bold')
ax.text(0, 3.7, '~50-100 kpc from galactic center', fontsize=8,
        color=DIM, ha='center')

# Solar system Hill sphere
solar = plt.Circle((0, 0), 2.5, fill=True, facecolor=BLUE,
                     alpha=0.06, edgecolor=BLUE, linewidth=2, linestyle='--',
                     zorder=2)
ax.add_patch(solar)
ax.text(0, 2.8, 'SOLAR SYSTEM HILL SPHERE', fontsize=11, color=BLUE,
        ha='center', fontweight='bold')
ax.text(0, 2.3, '~1-2 light years', fontsize=8, color=DIM, ha='center')

# Earth Hill sphere
earth_hs = plt.Circle((0, 0), 1.2, fill=True, facecolor=CYAN,
                        alpha=0.08, edgecolor=CYAN, linewidth=2.5,
                        zorder=3)
ax.add_patch(earth_hs)
ax.text(0, 1.45, 'EARTH HILL SPHERE', fontsize=11, color=CYAN,
        ha='center', fontweight='bold')
ax.text(0, 1.1, '~1.5 million km', fontsize=8, color=DIM, ha='center')

# Earth (tiny dot at center)
earth = plt.Circle((0, 0), 0.15, fill=True, facecolor=GREEN,
                     alpha=0.6, edgecolor=GREEN, linewidth=2, zorder=5)
ax.add_patch(earth)
ax.text(0, -0.05, 'Earth', fontsize=9, color=GREEN, ha='center',
        fontweight='bold', zorder=6)

# All measurements marker
ax.text(0, 0.35, 'ALL G measurements\nare HERE', fontsize=10,
        color=RED, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED),
        zorder=7)

# Arrows pointing inward to show nesting
for r, color in [(4.0, PURPLE), (2.5, BLUE), (1.2, CYAN)]:
    for angle in [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]:
        ax.annotate('', xy=(r * 0.85 * np.cos(angle), r * 0.85 * np.sin(angle)),
                    xytext=(r * np.cos(angle), r * np.sin(angle)),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1, alpha=0.4))

# Bottom note
ax.text(0, -4.5, 'The universality claim spans from Earth to the observable universe.\n'
        'The evidence spans from Earth\'s surface to Earth\'s surface.\n'
        'Sample size for cross-boundary universality: ZERO.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys3_02_nested_boundaries.png')


# ================================================================
# FIG 3: UNIVERSALITY CLAIM VS EVIDENCE — THE GAP
# Type: Scale/landscape (claim vs evidence)
# Shows: A single log axis from 10^4 km to 10^23 km. The claim
# spans the whole axis. The evidence covers a sliver at the left.
# The gap between claim and evidence is the finding.
# ================================================================

fig, ax = dark_canvas("The Universality Claim vs The Evidence",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Two horizontal bars
# Top: THE CLAIM
claim_y = 7.0
ax.plot([0.5, 9.5], [claim_y, claim_y], color=GOLD, linewidth=4, alpha=0.6)
ax.text(5.0, claim_y + 0.6, 'THE CLAIM: G is universal', fontsize=14,
        color=GOLD, ha='center', fontweight='bold')

# Claim bar endpoints
claim_labels = [
    (0.5, 'Earth surface\n6,371 km'),
    (2.5, 'Hill sphere\n1.5M km'),
    (4.5, 'Solar Hill sphere\n1-2 ly'),
    (6.5, 'Galactic edge\n~100 kpc'),
    (9.5, 'Observable universe\n46 billion ly'),
]
for x, label in claim_labels:
    ax.plot([x, x], [claim_y - 0.2, claim_y + 0.2], color=GOLD, linewidth=2)
    ax.text(x, claim_y - 0.6, label, fontsize=7, color=DIM, ha='center')

# Bottom: THE EVIDENCE
evidence_y = 3.5
# Evidence covers ONLY the first tiny sliver
evidence_width = 0.15  # Visually tiny
ax.plot([0.5, 0.5 + evidence_width], [evidence_y, evidence_y], color=RED,
        linewidth=8, solid_capstyle='round')
ax.text(5.0, evidence_y + 0.6, 'THE EVIDENCE: Direct G measurements', fontsize=14,
        color=RED, ha='center', fontweight='bold')

# Evidence label
ax.annotate('All measurements\nare HERE\n(0.42% of first boundary)',
            xy=(0.5 + evidence_width / 2, evidence_y),
            xytext=(2.5, evidence_y - 1.5),
            fontsize=11, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))

# The gap
ax.annotate('', xy=(9.5, 5.3), xytext=(0.65, 5.3),
            arrowprops=dict(arrowstyle='<->', color=MAG, lw=2.5))
ax.text(5.0, 5.6, 'THE GAP', fontsize=18, color=MAG, ha='center',
        fontweight='bold')
ax.text(5.0, 4.8, 'Zero direct measurements anywhere in this range',
        fontsize=11, color=SILVER, ha='center')

# Bottom
ax.text(5.0, 0.8, 'The gap between the claim and the evidence\n'
        'is the largest in physics.',
        fontsize=12, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys3_03_claim_vs_evidence.png')


# ================================================================
# FIG 4: L1/L2 EXPERIMENT — SPACECRAFT AT THE BOUNDARY
# Type: Geometric
# Shows: Earth at center, Hill sphere as circle, L1 and L2 at
# boundary with spacecraft, Moon inside. The proposed experiment
# location sits ON the boundary.
# ================================================================

fig, ax = dark_canvas("The Proposed Experiment: L1/L2 at the Hill Sphere Boundary",
                      size=(16, 14))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

# Hill sphere boundary
hs = plt.Circle((0, 0), 1.8, fill=False, edgecolor=CYAN,
                  linewidth=2.5, linestyle='--', zorder=3)
ax.add_patch(hs)
ax.text(0, 2.05, 'HILL SPHERE BOUNDARY', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(0, 1.9, '1.5 million km', fontsize=9, color=DIM, ha='center')

# Interior shading
hs_fill = plt.Circle((0, 0), 1.8, fill=True, facecolor=CYAN,
                       alpha=0.04, edgecolor='none', zorder=1)
ax.add_patch(hs_fill)

# Earth at center
earth = plt.Circle((0, 0), 0.12, fill=True, facecolor=GREEN,
                     alpha=0.7, edgecolor=GREEN, linewidth=2, zorder=5)
ax.add_patch(earth)
ax.text(0, -0.3, 'Earth', fontsize=10, color=GREEN, ha='center',
        fontweight='bold')

# Moon orbit
moon_orbit = plt.Circle((0, 0), 0.46, fill=False, edgecolor=DIM,
                          linewidth=1, linestyle=':', zorder=2)
ax.add_patch(moon_orbit)
moon_angle = np.pi / 3
moon_x = 0.46 * np.cos(moon_angle)
moon_y = 0.46 * np.sin(moon_angle)
data_point(ax, moon_x, moon_y, '', SILVER, size=100)
ax.text(moon_x + 0.15, moon_y + 0.1, 'Moon\n(25.6%)', fontsize=8,
        color=SILVER)

# Sun direction
ax.annotate('', xy=(-2.3, 0), xytext=(-2.0, 0),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
ax.text(-2.3, 0.15, 'To Sun', fontsize=9, color=ORANGE, ha='center')

# L1 (toward Sun)
l1_x = -1.8
data_point(ax, l1_x, 0, '', GOLD, size=350)
ax.scatter([l1_x], [0], s=400, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)
ax.text(l1_x, -0.35, 'L1', fontsize=14, color=GOLD, ha='center',
        fontweight='bold')
ax.text(l1_x, -0.65, 'DSCOVR, SOHO', fontsize=8, color=SILVER, ha='center')
ax.text(l1_x, -0.9, 'G measured: NO', fontsize=9, color=RED, ha='center',
        fontweight='bold')

# L2 (away from Sun)
l2_x = 1.8
data_point(ax, l2_x, 0, '', GOLD, size=350)
ax.scatter([l2_x], [0], s=400, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)
ax.text(l2_x, -0.35, 'L2', fontsize=14, color=GOLD, ha='center',
        fontweight='bold')
ax.text(l2_x, -0.65, 'JWST, Gaia, Planck', fontsize=8, color=SILVER,
        ha='center')
ax.text(l2_x, -0.9, 'G measured: NO', fontsize=9, color=RED, ha='center',
        fontweight='bold')

# All measurements cluster
ax.text(0, 0.5, 'All direct G measurements\nare within 0.45% of center',
        fontsize=9, color=RED, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# Bottom
ax.text(0, -2.2, 'Spacecraft at the boundary exist. None measures G.\n'
        'The question has never been framed.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys3_04_l1_l2_experiment.png')


# ================================================================
# FIG 5: G VS ALTITUDE — CLUSTERED AT ZERO, VOID ABOVE
# Type: Scatter/prediction
# Shows: All G measurements plotted vs altitude. All cluster at
# ~0 km altitude. The void above shows the untested space.
# The prediction of a depth trend is visible as the clustering.
# ================================================================

fig, ax = dark_fig("G Measurements vs Altitude: All Clustered at the Surface",
                   xlabel="G (\u00d710\u207b\u00b9\u00b9 m\u00b3 kg\u207b\u00b9 s\u207b\u00b2)",
                   ylabel="Altitude above sea level (km, log scale)",
                   size=(16, 10))

# G measurements with approximate altitudes (all near surface)
measurements = [
    (6.67545, 0.05, 0.00018, 'BIPM', RED),
    (6.67191, 0.08, 0.00099, 'LENS', GREEN),
    (6.67425, 0.15, 0.00012, 'Zurich', BLUE),
    (6.67484, 0.03, 0.00012, 'HUST-a', ORANGE),
    (6.67349, 0.06, 0.00018, 'HUST-b', ORANGE),
    (6.674215, 0.10, 0.000092, 'UWash', CYAN),
    (6.6726, 0.12, 0.0005, 'NIST', MAG),
]

# Jitter altitudes slightly for visibility (all are ~0 km)
for g_val, alt, g_err, name, color in measurements:
    measured_diamond(ax, g_val, alt, '', color, size=200)
    ax.errorbar([g_val], [alt], xerr=[g_err], fmt='none', ecolor=color,
                elinewidth=1.5, capsize=4, capthick=1.5, zorder=9)
    ax.text(g_val + g_err + 0.0002, alt + 0.01, name, fontsize=8,
            color=color, va='center')

# The void above
shaded_region_h(ax, 1, 1600, DIM, 0.03)
ax.text(6.674, 200, 'UNTESTED', fontsize=24, color=DIM, ha='center',
        fontweight='bold', alpha=0.3)

# Key altitudes
threshold_line(ax, 400, 'ISS (400 km)', SILVER, vertical=False)
threshold_line(ax, 1500000, '', GOLD, vertical=False)
ax.text(6.678, 1200, 'Hill sphere boundary\n(1,500,000 km)', fontsize=9,
        color=GOLD, fontweight='bold')

# The prediction
ax.annotate('If G is boundary-dependent:\na systematic trend should\nappear with altitude',
            xy=(6.676, 50), xytext=(6.678, 30),
            fontsize=10, color=GOLD, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# CODATA band
measurement_band_v(ax, 6.67430, 0.00015, '', SILVER)

ax.set_xlim(6.669, 6.680)
ax.set_yscale('log')
ax.set_ylim(0.01, 2000000)

save_fig(fig, 'phys3_05_g_vs_altitude.png')


# ================================================================
# FIG 6: G MEASUREMENT TIMELINE 1798-2018
# Type: Running/timeline
# Shows: G values over 220 years. Precision improves but
# disagreement persists. The non-convergence IS the anomaly.
# ================================================================

fig, ax = dark_fig("220 Years of G Measurements: Precision Improves, Disagreement Persists",
                   xlabel="Year",
                   ylabel="G (\u00d710\u207b\u00b9\u00b9 m\u00b3 kg\u207b\u00b9 s\u207b\u00b2)")

# Historical + modern measurements
timeline = [
    (1798, 6.74, 0.05, 'Cavendish', DIM),
    (1982, 6.6726, 0.0005, 'NIST', MAG),
    (1995, 6.7154, 0.0006, 'Wuppertal', DIM),
    (2000, 6.674215, 0.000092, 'UWash', CYAN),
    (2001, 6.67559, 0.00027, 'BIPM', BLUE),
    (2007, 6.693, 0.027, 'Fixler', DIM),
    (2009, 6.67349, 0.00018, 'HUST', ORANGE),
    (2014, 6.67545, 0.00018, 'BIPM', RED),
    (2014, 6.67191, 0.00099, 'LENS', GREEN),
    (2018, 6.67484, 0.00012, 'HUST-a', ORANGE),
    (2018, 6.67349, 0.00018, 'HUST-b', ORANGE),
]

for year, g_val, g_err, name, color in timeline:
    measured_diamond(ax, year, g_val, '', color, size=150)
    ax.errorbar([year], [g_val], yerr=[g_err], fmt='none', ecolor=color,
                elinewidth=1.5, capsize=4, capthick=1.5, zorder=9)

# CODATA 2018 band
measurement_band(ax, 6.67430, 0.00015, '', GOLD)

# Labels for key points (staggered to avoid overlap)
label_data = [
    (1798, 6.74, 'Cavendish\n1798', DIM, (1810, 6.75)),
    (1995, 6.7154, 'Wuppertal\n(outlier)', DIM, (1985, 6.72)),
    (2000, 6.674215, 'UWash', CYAN, (1990, 6.672)),
    (2014, 6.67545, 'BIPM', RED, (2008, 6.678)),
    (2014, 6.67191, 'LENS', GREEN, (2008, 6.669)),
    (2018, 6.67484, 'HUST', ORANGE, (2022, 6.676)),
]

for year, g_val, name, color, text_pos in label_data:
    ax.annotate(name, xy=(year, g_val), xytext=text_pos,
                fontsize=7, color=color,
                arrowprops=dict(arrowstyle='->', color=color, lw=0.8, alpha=0.6))

# Annotation
result_box(ax, 1900, 6.665,
           '220 years of improving precision.\n'
           'The disagreement does NOT resolve.\n'
           'Systematic error? Or structural signal?',
           GOLD, 10)

ax.set_xlim(1790, 2025)
ax.set_ylim(6.660, 6.760)

save_fig(fig, 'phys3_06_g_timeline.png')


# ================================================================
# FIG 7: FRACTION OF HILL SPHERE REACHED — LOG BAR CHART
# Type: Comparison bar
# Shows: How far each measurement location reaches toward the
# Hill sphere boundary. ISS is laughably close. L1/L2 are at 99%.
# ================================================================

fig, ax = dark_fig("How Far Toward the Boundary?",
                   xlabel="",
                   ylabel="Fraction of Hill sphere radius (%)",
                   size=(16, 10))

bar_data = [
    ('Earth\nsurface', 0.42, RED),
    ('ISS\n(400 km)', 0.45, ORANGE),
    ('GPS\n(20,200 km)', 1.8, BLUE),
    ('Moon\n(384,400 km)', 25.6, CYAN),
    ('L1\n(1.49M km)', 99.0, GREEN),
    ('L2\n(1.50M km)', 100.0, GREEN),
]

x_pos = np.arange(len(bar_data))

for i, (label, pct, color) in enumerate(bar_data):
    ax.bar(i, pct, color=color, alpha=0.7, edgecolor=color,
           linewidth=1.5, width=0.7)
    # Value label
    if pct < 5:
        ax.text(i, pct + 3, '%.2f%%' % pct, fontsize=10, color=color,
                ha='center', fontweight='bold')
    else:
        ax.text(i, pct + 3, '%.1f%%' % pct, fontsize=10, color=color,
                ha='center', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels([d[0] for d in bar_data], fontsize=9, color=SILVER)

# 100% line
ax.plot([-0.5, 5.5], [100, 100], color=GOLD, linewidth=2.5, linestyle='--',
        alpha=0.7)
ax.text(5.5, 103, 'Hill sphere boundary (100%)', fontsize=10, color=GOLD,
        ha='right', fontweight='bold')

# Annotations
ax.annotate('G measured here\n(thousands of times)', xy=(0, 0.42),
            xytext=(1.5, 50),
            fontsize=10, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

ax.annotate('G measured here:\nNEVER', xy=(4.5, 99),
            xytext=(3, 75),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))

ax.set_xlim(-0.8, 6.0)
ax.set_ylim(0, 120)

save_fig(fig, 'phys3_07_fraction_reached.png')


# ================================================================
# FIG 8: PHYS-3 IDENTITY CARD
# Type: Identity card
# Shows: Hill sphere at 1.5M km, zero measurements outside,
# the G disagreement, the proposed L1/L2 experiment.
# ================================================================

fig, ax = dark_canvas("PHYS-3 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'G HAS NEVER BEEN TESTED\nOUTSIDE EARTH\'S HILL SPHERE',
        fontsize=18, color=GOLD, ha='center', fontweight='bold')

# Left column: the gap
ax.text(2.5, 7.5, 'THE GAP', fontsize=14, color=RED,
        ha='center', fontweight='bold')

gap_items = [
    ('Hill sphere boundary', '1.5 million km', CYAN),
    ('Farthest G measurement', '~6,400 km (surface)', RED),
    ('Fraction reached', '0.42%', ORANGE),
    ('Cross-boundary measurements', 'ZERO', RED),
    ('Years of measurements', '227 (since 1798)', DIM),
]
for i, (label, value, color) in enumerate(gap_items):
    y = 6.6 - i * 0.7
    ax.text(1.0, y, label + ':', fontsize=9, color=SILVER)
    ax.text(4.0, y, value, fontsize=10, color=color, fontweight='bold')

# Right column: the experiment
ax.text(7.5, 7.5, 'THE EXPERIMENT', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')

expt_items = [
    ('Location', 'L1 or L2 Lagrange point', GREEN),
    ('Distance', '~1.5 million km', CYAN),
    ('Boundary status', 'AT the Hill sphere', GOLD),
    ('Existing spacecraft', 'JWST, DSCOVR, SOHO, Gaia', SILVER),
    ('G measurement performed', 'NEVER', RED),
]
for i, (label, value, color) in enumerate(expt_items):
    y = 6.6 - i * 0.7
    ax.text(5.5, y, label + ':', fontsize=9, color=SILVER)
    ax.text(8.5, y, value, fontsize=10, color=color, fontweight='bold',
            ha='left')

# The G disagreement
ax.plot([0.5, 9.5], [3.2, 3.2], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 2.8, 'THE DISAGREEMENT', fontsize=13, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(5, 2.1, 'G measurements disagree beyond stated uncertainties.\n'
        '220 years of "unidentified systematic errors."\n'
        'Alternative: different depths produce different readings.',
        fontsize=10, color=SILVER, ha='center')

# The key comparison
ax.text(5, 1.0, 'THE PATTERN', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(5, 0.4, '\u03b1, \u03b1_s, weak: boundary identified \u2192 running confirmed '
        '\u2192 no method disagreement\n'
        'G: boundary NOT identified \u2192 running NOT tested '
        '\u2192 persistent method disagreement',
        fontsize=9, color=GOLD, ha='center')

save_fig(fig, 'phys3_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-3 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys3_01_hill_sphere_scale.png',
    'phys3_02_nested_boundaries.png',
    'phys3_03_claim_vs_evidence.png',
    'phys3_04_l1_l2_experiment.png',
    'phys3_05_g_vs_altitude.png',
    'phys3_06_g_timeline.png',
    'phys3_07_fraction_reached.png',
    'phys3_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    