#!/usr/bin/env python3
"""
HOWL Video 1 Diagrams — The First Integer Fraction Physics Model
8 figures for the 10-minute smash-up video.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures_cta')
os.makedirs(outdir, exist_ok=True)

# ── Global style ──────────────────────────────────────────────
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
# FIG 1: THE SCOREBOARD
# Type: Comparison (D5.6)
# Shows: All 10 results with precision and domain in one view.
# The volume and cross-domain spread is the argument against numerology.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.text(0.50, 0.97, 'The Integer Physics Scoreboard',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=20, fontweight='bold', color=GOLD)
ax.text(0.50, 0.925, 'From 13 measured inputs as integer fractions',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=13, color=SILVER)

results = [
    (u'\u03b1\u207b\u00b9 vs Rb recoil',   '7 ppt',       'QED',              GREEN),
    (u'\u03b1\u207b\u00b9 vs CODATA',       '0.9 ppb',     'QED',              GREEN),
    (u'\u03b1\u207b\u00b9 vs Cs recoil',    '1.2 ppb',     'QED',              GREEN),
    ('Hydrogen 1S\u20132S frequency',                   '11 digits',   'Atomic',           CYAN),
    (u'\u03b1\u207b\u00b9 running from M\u1d2a',        '0.02 ppm',    'QED \u2192 Atomic', CYAN),
    ('Electron g\u20132 series recovery',               '14 digits',   'QED',              GREEN),
    ('W boson mass (1-loop)',                            '350 ppm',      'Electroweak',      BLUE),
    ('Deuterium abundance',                             '0.12\u03c3',  'Cosmology \u2192 BBN', PURPLE),
    ('Helium abundance',                                '1.5%',        'Cosmology \u2192 BBN', PURPLE),
    ('Dark matter ratio',                               '725 ppm',     'Cosmology',        PURPLE),
]

y_top = 0.855
ax.text(0.05, y_top, 'Result', transform=ax.transAxes, ha='left',
        fontsize=12, fontweight='bold', color=DIM)
ax.text(0.62, y_top, 'Match', transform=ax.transAxes, ha='center',
        fontsize=12, fontweight='bold', color=DIM)
ax.text(0.82, y_top, 'Domain', transform=ax.transAxes, ha='center',
        fontsize=12, fontweight='bold', color=DIM)

ax.plot([0.04, 0.96], [y_top - 0.02, y_top - 0.02],
        transform=ax.transAxes, color=DIM, linewidth=0.8, alpha=0.5)

for i, (result, match, domain, color) in enumerate(results):
    y = y_top - 0.045 - i * 0.065
    if i % 2 == 0:
        ax.add_patch(mpatches.FancyBboxPatch(
            (0.03, y - 0.022), 0.94, 0.055,
            transform=ax.transAxes,
            boxstyle='round,pad=0.005',
            facecolor=PAN, edgecolor='none', alpha=0.5,
            clip_on=True))
    ax.text(0.05, y, result, transform=ax.transAxes, ha='left',
            fontsize=12, color=WHITE)
    ax.text(0.62, y, match, transform=ax.transAxes, ha='center',
            fontsize=13, fontweight='bold', color=color)
    ax.text(0.82, y, domain, transform=ax.transAxes, ha='center',
            fontsize=11, color=SILVER)

y_foot = y_top - 0.045 - len(results) * 0.065 - 0.04
ax.plot([0.04, 0.96], [y_foot + 0.025, y_foot + 0.025],
        transform=ax.transAxes, color=DIM, linewidth=0.8, alpha=0.5)
ax.text(0.50, y_foot - 0.04,
        'All arithmetic: Python Fraction.  Zero floating point.',
        transform=ax.transAxes, ha='center', fontsize=11, color=SILVER)

save(fig, 'vid1_01_scoreboard.png')


# ================================================================
# FIG 2: DIGIT-BY-DIGIT ALPHA COMPARISON
# Type: Progression (D5.7)
# Shows: The visual match between integer extraction and CODATA.
# The eye compares digit by digit faster than reading ppb numbers.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.text(0.50, 0.95, 'Fine structure constant: integer fraction extraction vs CODATA',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=18, fontweight='bold', color=GOLD)

digits_int = list('137.035998630')
digits_meas = list('137.035999177')

match_len = 0
for a, b in zip(digits_int, digits_meas):
    if a == b:
        match_len += 1
    else:
        break

x_start = 0.08
x_step = 0.065
y_int = 0.62
y_meas = 0.35
box_w = 0.050
box_h = 0.12

ax.text(x_start - 0.03, y_int, 'Integer\nFractions',
        transform=ax.transAxes, ha='right', va='center',
        fontsize=12, color=CYAN, fontweight='bold')
ax.text(x_start - 0.03, y_meas, 'CODATA\n2018',
        transform=ax.transAxes, ha='right', va='center',
        fontsize=12, color=MAG, fontweight='bold')

for i, (d_i, d_m) in enumerate(zip(digits_int, digits_meas)):
    x = x_start + i * x_step
    if d_i == '.':
        ax.text(x + box_w/2, y_int, '.', transform=ax.transAxes,
                ha='center', va='center', fontsize=24, fontweight='bold',
                color=WHITE)
        ax.text(x + box_w/2, y_meas, '.', transform=ax.transAxes,
                ha='center', va='center', fontsize=24, fontweight='bold',
                color=WHITE)
        continue

    is_match = (i < match_len)
    edge_color = GREEN if is_match else ORANGE

    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y_int - box_h/2), box_w, box_h,
        transform=ax.transAxes,
        boxstyle='round,pad=0.01',
        facecolor=BG, edgecolor=edge_color, linewidth=2,
        clip_on=True))
    ax.text(x + box_w/2, y_int, d_i, transform=ax.transAxes,
            ha='center', va='center', fontsize=22, fontweight='bold',
            color=edge_color)

    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y_meas - box_h/2), box_w, box_h,
        transform=ax.transAxes,
        boxstyle='round,pad=0.01',
        facecolor=BG, edgecolor=edge_color, linewidth=2,
        clip_on=True))
    ax.text(x + box_w/2, y_meas, d_m, transform=ax.transAxes,
            ha='center', va='center', fontsize=22, fontweight='bold',
            color=edge_color)

ax.text(0.50, 0.15,
        '9 digits match exactly.  Divergence at digit 10.  Difference: 3.3 ppb.',
        transform=ax.transAxes, ha='center', fontsize=13, color=SILVER)
ax.text(0.50, 0.08,
        'Fully corrected: 7 parts per trillion vs Rb recoil',
        transform=ax.transAxes, ha='center', fontsize=12, color=GREEN)

save(fig, 'vid1_02_digit_comparison.png')


# ================================================================
# FIG 3: THREE-MEASUREMENT TENSION BAR
# Type: Comparison (D5.6)
# Shows: Integer extraction anchored at zero, three independent
# measurements as markers at their ppb offsets. Triple-checked.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-0.5, 6.0)
ax.set_ylim(-0.5, 10.0)
ax.axis('off')

ax.text(3.0, 9.8,
        u'\u03b1\u207b\u00b9 from Integer Fractions vs Three Independent Measurements',
        ha='center', va='top', fontsize=16, fontweight='bold', color=GOLD)

# ── Corrected extraction (top section) ──
ax.text(0.0, 8.5, 'Fully corrected extraction', fontsize=12,
        fontweight='bold', color=GOLD)

# Number line for corrected
ax.plot([0.5, 5.5], [7.5, 7.5], color=DIM, linewidth=1.5)

# Anchor at 0
ax.plot(0.5, 7.5, 'o', markersize=14, color=GOLD, zorder=5)
ax.text(0.0, 7.0, 'Integer\nextraction', ha='center', fontsize=9, color=GOLD)

# Scale: 0 to 1.5 ppb mapped to x = 0.5 to 5.5
corr_data = [
    (0.007, 'Rb recoil', GREEN, '7 ppt'),
    # (0.90, 'CODATA', CYAN, ''),
    (1.18, 'Cs recoil', BLUE, '1.2 ppb'),
]
for ppb, label, color, txt in corr_data:
    x = 0.5 + (ppb / 1.5) * 5.0
    ax.plot(x, 7.5, 'D', markersize=12, color=color,
            markeredgecolor=WHITE, markeredgewidth=1.5, zorder=5)
    ax.text(x, 8.0, label, ha='center', fontsize=10, color=color)
    ax.text(x, 6.9, txt, ha='center', fontsize=10, fontweight='bold', color=color)

ax.text(0.5, 6.3, '0 ppb', ha='center', fontsize=9, color=DIM)
ax.text(5.5, 6.3, '1.5 ppb', ha='center', fontsize=9, color=DIM)

# ── Base extraction (bottom section) ──
ax.text(0.0, 5.0, 'Base extraction (QED only)', fontsize=12,
        fontweight='bold', color=SILVER)

ax.plot([0.5, 5.5], [4.0, 4.0], color=DIM, linewidth=1.5)

ax.plot(0.5, 4.0, 'o', markersize=14, color=GOLD, zorder=5)
ax.text(0.0, 3.5, 'Integer\nextraction', ha='center', fontsize=9, color=GOLD)

# Scale: 0 to 5 ppb mapped to x = 0.5 to 5.5
base_data = [
    (3.03, 'Cs recoil', BLUE, '3.0 ppb'),
    # (3.31, 'CODATA', CYAN, ''),
    (4.20, 'Rb recoil', GREEN, '4.2 ppb'),
]
for ppb, label, color, txt in base_data:
    x = 0.5 + (ppb / 5.0) * 5.0
    ax.plot(x, 4.0, 'D', markersize=12, color=color,
            markeredgecolor=WHITE, markeredgewidth=1.5, zorder=5)
    ax.text(x, 4.5, label, ha='center', fontsize=10, color=color)
    ax.text(x, 3.4, txt, ha='center', fontsize=10, fontweight='bold', color=color)

ax.text(0.5, 2.8, '0 ppb', ha='center', fontsize=9, color=DIM)
ax.text(5.5, 2.8, '5.0 ppb', ha='center', fontsize=9, color=DIM)

# ── Bottom note ──
ax.text(3.0, 1.5,
        'Corrections tighten the match 600\u00d7: from 4.2 ppb to 7 ppt',
        ha='center', fontsize=12, color=SILVER)

save(fig, 'vid1_03_tension_bar.png')


# ================================================================
# FIG 4: ALPHA EXTRACTION PIPELINE
# Type: Progression (D5.7)
# Shows: Input -> computation -> output. One measurement in, one number out.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.text(0.50, 0.95,
        u'Electron magnetic moment \u2192 \u03b1\u207b\u00b9 = 137.035999207 (7 ppt vs Rb recoil)',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=18, fontweight='bold', color=GOLD)

boxes = [
    (0.03, 0.30, 0.25, 0.45,
     'Harvard a_e\nmeasurement',
     'a_e = 0.00115965218059',
     'One electron in a\nmagnetic field\n13 digits',
     MAG),
    (0.35, 0.30, 0.30, 0.45,
     '5-loop QED series\n+ Newton inversion',
     'Integer fractions only',
     'Python Fraction class\nResidual: 10^{-204}',
     CYAN),
    (0.72, 0.30, 0.25, 0.45,
     u'\u03b1\u207b\u00b9 = 137.035999207',
     '',
     'vs Rb recoil: 7 ppt\nvs CODATA: 0.9 ppb\nvs Cs recoil: 1.2 ppb',
     GREEN),
]

for x, y, w, h, title, main, sub, color in boxes:
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h,
        transform=ax.transAxes,
        boxstyle='round,pad=0.02',
        facecolor=PAN, edgecolor=color, linewidth=2,
        clip_on=True))
    ax.text(x + w/2, y + h - 0.05, title,
            transform=ax.transAxes, ha='center', va='top',
            fontsize=13, fontweight='bold', color=color)
    if main:
        ax.text(x + w/2, y + h/2, main,
                transform=ax.transAxes, ha='center', va='center',
                fontsize=11, color=WHITE)
    ax.text(x + w/2, y + 0.05, sub,
            transform=ax.transAxes, ha='center', va='bottom',
            fontsize=10, color=SILVER)

for ax_x in [0.29, 0.66]:
    ax.annotate('', xy=(ax_x + 0.04, 0.525), xytext=(ax_x, 0.525),
                transform=ax.transAxes,
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

ax.text(0.50, 0.18,
        "Harvard measured a_e = 0.00115965218059 (13 digits) by trapping one electron in a Penning trap.",
        transform=ax.transAxes, ha='center', fontsize=11, color=SILVER)
ax.text(0.50, 0.13,
        "The 5-loop QED series (Schwinger 1948 through Laporta 2017) is inverted using Newtons method.",
        transform=ax.transAxes, ha='center', fontsize=11, color=SILVER)
ax.text(0.50, 0.08,
        "Every coefficient is a rational fraction times integer pair transcendentals. No floating point.",
        transform=ax.transAxes, ha='center', fontsize=11, color=SILVER)
ax.text(0.50, 0.03,
        u"Rb recoil (Morel et al. 2020, Paris) measures \u03b1 independently via atom interferometry. Agreement: 7 ppt.",
        transform=ax.transAxes, ha='center', fontsize=11, color=GOLD)

save(fig, 'vid1_04_alpha_pipeline.png')


# ================================================================
# FIG 5: DM -> BBN CHAIN
# Type: Connection/Integer Map (D5.5)
# Shows: 22/13 x pi -> DM ratio -> baryon density -> deuterium/helium.
# Cross-domain chain with actual fractions. The integers carry meaning.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')

ax.text(0.50, 0.97, 'One Chain: Particle Counting to Primordial Elements',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=18, fontweight='bold', color=GOLD)
ax.text(0.50, 0.925,
        'Cross-domain derivation: Cosmology \u2192 Nuclear',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=12, color=SILVER)

nodes = [
    (0.08, 0.55, 0.16, 0.28,
     'Particle Counting',
     '22 = 11 x 2\n(gluon self x chirality)\n\n'
     '13 = 19 - 6\n(weak - Cabibbo)',
     ORANGE),
    (0.28, 0.55, 0.14, 0.28,
     'Geometry',
     'x pi\n\nGalaxy as\ntoroid\n(circular\ncross-section)',
     CYAN),
    (0.46, 0.55, 0.14, 0.28,
     'DM Ratio',
     '22/13 x pi\n= 5.317\n\nMeasured:\n5.32\n(725 ppm)',
     GREEN),
    (0.64, 0.55, 0.14, 0.28,
     'Baryon Density',
     'eta from\nDM ratio\n-> Omega_b h^2',
     BLUE),
    (0.82, 0.55, 0.15, 0.28,
     'BBN Yields',
     'D/H: 2.531\nvs 2.527\n(0.12 sigma)\n\n'
     'He: 24.85%\nvs 24.49%\n(1.5%)',
     PURPLE),
]

for x, y, w, h, title, content, color in nodes:
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h,
        transform=ax.transAxes,
        boxstyle='round,pad=0.02',
        facecolor=PAN, edgecolor=color, linewidth=2,
        clip_on=True))
    ax.text(x + w/2, y + h - 0.03, title,
            transform=ax.transAxes, ha='center', va='top',
            fontsize=11, fontweight='bold', color=color)
    ax.text(x + w/2, y + h/2 - 0.02, content,
            transform=ax.transAxes, ha='center', va='center',
            fontsize=9, color=WHITE, linespacing=1.4)

arrow_xs = [(0.24, 0.28), (0.42, 0.46), (0.60, 0.64), (0.78, 0.82)]
for x1, x2 in arrow_xs:
    ax.annotate('', xy=(x2, 0.69), xytext=(x1, 0.69),
                transform=ax.transAxes,
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

domains = [
    (0.16, 'Particle\nPhysics', ORANGE),
    (0.35, 'Geometry', CYAN),
    (0.53, 'Cosmology', GREEN),
    (0.71, 'Cosmology', BLUE),
    (0.89, 'Nuclear', PURPLE),
]
for x, label, color in domains:
    ax.text(x, 0.48, label, transform=ax.transAxes,
            ha='center', fontsize=10, color=color, fontstyle='italic')

ax.text(0.50, 0.38,
        'Same integer fractions -> dark matter ratio -> baryon density -> element abundances',
        transform=ax.transAxes, ha='center', fontsize=12, color=SILVER)
ax.text(0.50, 0.33,
        'The standard model does not derive BBN from DM ratio from integer particle counts.',
        transform=ax.transAxes, ha='center', fontsize=11, color=GOLD)

save(fig, 'vid1_05_dm_bbn_chain.png')


# ================================================================
# FIG 6: DOMAIN MAP
# Type: Connection/Integer Map (D5.5)
# Shows: 13 inputs at center, 5 domains radiating outward.
# The cross-domain spread from one input pool is the anti-numerology argument.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

ax.text(0.50, 0.98, '13 Inputs \u2192 5 Domains',
        transform=ax.transAxes, ha='center', va='top',
        fontsize=20, fontweight='bold', color=GOLD)

center = plt.Circle((0, 0), 0.35, facecolor=PAN, edgecolor=GOLD,
                     linewidth=3, zorder=10)
ax.add_patch(center)
ax.text(0, 0.08, '13 Measured\nInputs', ha='center', va='center',
        fontsize=14, fontweight='bold', color=GOLD, zorder=11)
ax.text(0, -0.12, 'as integer\nfractions', ha='center', va='center',
        fontsize=11, color=SILVER, zorder=11)

domain_data = [
    (90, 1.05, 'QED',
     u'\u03b1\u207b\u00b9: 7 ppt\na_e: 14 digits',
     GREEN),
    (162, 1.05, 'Atomic',
     'H frequency:\n11 digits',
     CYAN),
    (234, 1.05, 'Electroweak',
     'M_W: 350 ppm (28 MeV)\nfrom PDG',
     BLUE),
    (306, 1.05, 'Cosmology',
     'DM ratio:\n725 ppm',
     PURPLE),
    (18, 1.05, 'Nuclear\n(BBN)',
     'Deuterium: 0.12 sigma\nHelium: 1.5%',
     ORANGE),
]

for angle_deg, dist, label, results, color in domain_data:
    angle = np.radians(angle_deg)
    x = dist * np.cos(angle)
    y = dist * np.sin(angle)

    x_inner = 0.38 * np.cos(angle)
    y_inner = 0.38 * np.sin(angle)
    ax.plot([x_inner, x*0.72], [y_inner, y*0.72],
            color=color, linewidth=2, alpha=0.6, zorder=5)

    domain_circle = plt.Circle((x, y), 0.32, facecolor=PAN,
                               edgecolor=color, linewidth=2, zorder=8)
    ax.add_patch(domain_circle)
    ax.text(x, y + 0.10, label, ha='center', va='center',
            fontsize=13, fontweight='bold', color=color, zorder=9)
    ax.text(x, y - 0.08, results, ha='center', va='center',
            fontsize=9, color=WHITE, zorder=9, linespacing=1.3)

save(fig, 'vid1_06_domain_map.png')


# ================================================================
# FIG 7: ALPHA RUNNING WATERFALL
# Type: Progression (D5.7)
# Shows: Starting at 127.906, each VP contribution stacks to reach
# 137.036. Every bar is a Fraction. The buildup is visible.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
ax.set_facecolor(BG)

components = [
    (u'\u03b1\u207b\u00b9(M_Z)', 127.906000, BLUE, 'Measured'),
    ('Electron VP', 2.4952797111, GREEN, 'Integer arithmetic'),
    ('Muon VP', 1.3638861640, GREEN, 'Integer arithmetic'),
    ('Tau VP', 0.7659766249, GREEN, 'Integer arithmetic'),
    ('Hadronic VP', 4.407860, MAG, 'Measured'),
    ('Top quark', 0.097000, CYAN, 'Perturbative'),
]

labels = [c[0] for c in components]
values = [c[1] for c in components]
colors = [c[2] for c in components]
sources = [c[3] for c in components]

cumulative = 0
bottoms = []
for v in values:
    bottoms.append(cumulative)
    cumulative += v

x_pos = np.arange(len(labels))
bars = ax.bar(x_pos, values, bottom=bottoms, color=colors,
              edgecolor=WHITE, linewidth=1.5, alpha=0.8, width=0.6)

# for i, (val, bot) in enumerate(zip(values, bottoms)):
#     y_mid = bot + val / 2
#     ax.text(i, y_mid, '%.3f' % val, ha='center', va='center',
#             fontsize=11, fontweight='bold', color=WHITE)
#     ax.text(i, bot + val + 0.3, sources[i], ha='center', va='bottom',
#             fontsize=8, color=SILVER, fontstyle='italic')

for i, (val, bot) in enumerate(zip(values, bottoms)):
    if bot + val / 2 < 127:
        y_mid = 127.4
    else:
        y_mid = bot + val / 2
    ax.text(i, y_mid, '%.3f' % val, ha='center', va='center',
            fontsize=11, fontweight='bold', color=WHITE)
    y_source = max(bot + val + 0.15, 127.3)
    ax.text(i, y_source, sources[i], ha='center', va='bottom',
            fontsize=8, color=SILVER, fontstyle='italic')

total = sum(values)
ax.axhline(y=total, color=GOLD, linewidth=2, linestyle='--', alpha=0.8)
ax.text(len(labels) - 0.5, total + 0.6,
        '= %.7f' % total,
        ha='right', fontsize=13, fontweight='bold', color=GOLD)

codata = 137.035999
ax.axhline(y=codata, color=MAG, linewidth=1.5, linestyle=':', alpha=0.7)
ax.text(len(labels) - 0.5, codata - 0.4,
        'CODATA: %.6f' % codata,
        ha='right', fontsize=11, color=MAG)

ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=10, color=SILVER, rotation=15, ha='right')
ax.set_ylabel(u'\u03b1\u207b\u00b9', fontsize=14, color=SILVER)
ax.set_ylim(127, 138.5)
ax.tick_params(colors=DIM)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.set_title(u'Building \u03b1\u207b\u00b9 from Components: 127.906 \u2192 137.036',
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

save(fig, 'vid1_07_alpha_waterfall.png')



# ================================================================
print("\n  All 8 diagrams saved to %s" % outdir)
print("  vid1_01_scoreboard.png")
print("  vid1_02_digit_comparison.png")
print("  vid1_03_tension_bar.png")
print("  vid1_04_alpha_pipeline.png")
print("  vid1_05_dm_bbn_chain.png")
print("  vid1_06_domain_map.png")
print("  vid1_07_alpha_waterfall.png")
