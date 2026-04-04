#!/usr/bin/env python3
"""
HOWL PHYS-16 Diagrams — The Cabibbo Doublet
8 figures covering mass window, two roads, three anomalies, CKM extension,
parameter count, energy landscape, decay channels.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: MASS WINDOW 1.5–6 TEV
# Type: Scale/threshold
# Shows: LHC lower bound (1.5 TeV), CKM upper bound (~6 TeV),
# HL-LHC projected reach (2-3 TeV). The narrow window.
# ================================================================

fig, ax = dark_fig("The Mass Window: 1.5 \u2013 6 TeV",
                   xlabel="Mass (TeV)",
                   ylabel="",
                   size=(16, 8))

# Main axis
ax.plot([0.5, 8], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Excluded region (below LHC bound)
ax.fill_between([0.5, 1.5], [0.0, 0.0], [1.0, 1.0], alpha=0.08, color=RED)
ax.plot([1.5, 1.5], [0.0, 1.0], color=RED, linewidth=3)
ax.text(1.0, -0.5, 'EXCLUDED\n(LHC Run 2\npair production)', fontsize=9,
        color=RED, ha='center', fontweight='bold')

# Allowed window
ax.fill_between([1.5, 6.0], [0.2, 0.2], [0.8, 0.8], alpha=0.06, color=GREEN)
ax.text(3.75, 1.3, 'ALLOWED WINDOW\n1.5 \u2013 6 TeV', fontsize=16,
        color=GREEN, ha='center', fontweight='bold')
ax.text(3.75, 0.5, '< half a decade in energy', fontsize=10,
        color=SILVER, ha='center')

# Upper bound from CKM
ax.plot([6.0, 6.0], [0.0, 1.0], color=GOLD, linewidth=3)
ax.text(6.0, -0.5, 'CKM upper bound\n|V_ub\'| \u2248 0.045\nrequires M < 6 TeV',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

# HL-LHC reach
ax.plot([2.5, 2.5], [0.15, 0.85], color=CYAN, linewidth=2.5, linestyle='--')
ax.text(2.5, -0.8, 'HL-LHC reach\n(pair production)\n~2\u20133 TeV', fontsize=9,
        color=CYAN, ha='center', fontweight='bold')

# FCC-hh reach
ax.plot([6.5, 6.5], [0.3, 0.7], color=MAG, linewidth=1.5, linestyle=':')
ax.text(7.0, 0.5, 'FCC-hh\n(100 TeV)', fontsize=8, color=MAG, ha='center')

# Discovery scenarios
result_box(ax, 4.0, -1.5,
           'Lower half (1.5\u20133 TeV): HL-LHC discovers directly.\n'
           'Upper half (3\u20136 TeV): single production at HL-LHC\n'
           'or pair production at FCC-hh.',
           GOLD, 9)

ax.set_xlim(0, 8.5)
ax.set_ylim(-2.2, 2.0)
ax.set_yticks([])

save_fig(fig, 'phys16_01_mass_window.png')


# ================================================================
# FIG 2: TWO ROADS CONVERGING ON (3,2,1/6)
# Type: Dual-path convergence
# Shows: Top-down path (gap ratio) and bottom-up path (anomalies)
# arriving independently at the same particle representation.
# ================================================================

fig, ax = dark_canvas("Two Roads to the Same Particle",
                      size=(18, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)

# Left path: gap ratio (top-down)
ax.text(2.5, 11.0, 'ROAD 1: Gap Ratio\n(Top-Down)', fontsize=14,
        color=CYAN, ha='center', fontweight='bold')

gap_steps = [
    ('3 couplings at M_Z', '\u03b1_em, sin\u00b2\u03b8_W, \u03b1_s'),
    ('SM gap ratio = 218/115', 'From beta coefficients'),
    ('Measured: 1.358', '40% miss'),
    ('Enumerate 15 candidates', 'Exact Fraction arithmetic'),
    ('Eliminate 13', 'Gap ratio + proton decay'),
]
for i, (step, detail) in enumerate(gap_steps):
    y = 9.8 - i * 1.2
    ax.text(2.5, y, step, fontsize=9, color=CYAN, ha='center',
            fontweight='bold')
    ax.text(2.5, y - 0.35, detail, fontsize=7, color=DIM, ha='center')
    if i < len(gap_steps) - 1:
        ax.annotate('', xy=(2.5, y - 0.6), xytext=(2.5, y - 0.1),
                    arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5, alpha=0.5))

ax.text(2.5, 3.0, 'Determines:\nRepresentation (3,2,1/6)\nM_GUT = 10^{15.5} GeV',
        fontsize=9, color=CYAN, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN))

# Right path: anomalies (bottom-up)
ax.text(7.5, 11.0, 'ROAD 2: Three Anomalies\n(Bottom-Up)', fontsize=14,
        color=ORANGE, ha='center', fontweight='bold')

anomaly_steps = [
    ('CKM unitarity deficit', '|V_ud|\u00b2 + |V_us|\u00b2 = 0.998 \u2260 1'),
    ('A_FB^b at LEP', '0.0992 vs SM 0.1038'),
    ('Higgs \u03bc excess', '~1.06\u20131.10 vs SM 1.00'),
    ('Global fit', 'Belfatto 2020, Cheung 2020'),
    ('One particle resolves all', 'VL quark doublet, 1.5\u20136 TeV'),
]
for i, (step, detail) in enumerate(anomaly_steps):
    y = 9.8 - i * 1.2
    ax.text(7.5, y, step, fontsize=9, color=ORANGE, ha='center',
            fontweight='bold')
    ax.text(7.5, y - 0.35, detail, fontsize=7, color=DIM, ha='center')
    if i < len(anomaly_steps) - 1:
        ax.annotate('', xy=(7.5, y - 0.6), xytext=(7.5, y - 0.1),
                    arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5, alpha=0.5))

ax.text(7.5, 3.0, 'Determines:\nMass 1.5\u20136 TeV\nMixing |V_ub\'| \u2248 0.045',
        fontsize=9, color=ORANGE, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE))

# Convergence at bottom
ax.annotate('', xy=(5.0, 1.5), xytext=(2.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=3))
ax.annotate('', xy=(5.0, 1.5), xytext=(7.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=3))

ax.text(5.0, 1.0, 'THE CABIBBO DOUBLET\n(3, 2, 1/6)', fontsize=18,
        color=GOLD, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=3))
ax.text(5.0, 0.2, 'Neither path knew about the other.\nBoth arrive at the same particle.',
        fontsize=10, color=SILVER, ha='center')

save_fig(fig, 'phys16_02_two_roads.png')


# ================================================================
# FIG 3: THREE ANOMALIES — CKM, A_FB, HIGGS MU
# Type: Comparison/scatter
# Shows: Three data points, each showing measured vs SM prediction,
# with sigma deviation labeled. The pattern of deviations.
# ================================================================

fig, ax = dark_fig("Three Anomalies Pointing to One Particle",
                   xlabel="",
                   ylabel="Deviation from SM (\u03c3)",
                   size=(16, 10))

anomalies = [
    ('CKM First Row\nUnitarity', 'SM: 1.000\nMeas: 0.998', 3.5, RED,
     '|V_ud|\u00b2+|V_us|\u00b2+|V_ub|\u00b2\n= 0.99798 \u00b1 0.00038'),
    ('A_FB^b\nat LEP', 'SM: 0.1038\nMeas: 0.0992', 2.9, ORANGE,
     'Forward-backward\nb-quark asymmetry\n(persistent 25+ years)'),
    ('Higgs Signal\nStrength \u03bc', 'SM: 1.00\nMeas: ~1.08', 2.0, BLUE,
     'Combined LHC\nRun 1 + Run 2\n(weakest anomaly)'),
]

x_pos = np.arange(len(anomalies))

for i, (label, values, sigma, color, detail) in enumerate(anomalies):
    # Bar showing sigma deviation
    ax.bar(i, sigma, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    ax.text(i, sigma + 0.15, '%.1f\u03c3' % sigma, fontsize=14, color=color,
            ha='center', fontweight='bold')

    # Values
    ax.text(i, -0.7, values, fontsize=8, color=SILVER, ha='center')

    # Detail
    ax.text(i, -1.8, detail, fontsize=7, color=DIM, ha='center')

ax.set_xticks(x_pos)
ax.set_xticklabels([a[0] for a in anomalies], fontsize=10, color=SILVER)

# Significance thresholds
ax.plot([-0.5, 2.5], [2, 2], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(2.6, 2.0, '2\u03c3', fontsize=8, color=DIM)
ax.plot([-0.5, 2.5], [3, 3], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(2.6, 3.0, '3\u03c3', fontsize=8, color=DIM)
ax.plot([-0.5, 2.5], [5, 5], color=GOLD, linewidth=1, linestyle=':', alpha=0.3)
ax.text(2.6, 5.0, '5\u03c3 (discovery)', fontsize=8, color=GOLD)

# The finding
result_box(ax, 1, 4.5,
           'All three anomalies are resolved\nby a single VL quark doublet (3,2,1/6)\n'
           'at 1.5\u20136 TeV.\n\n'
           'Belfatto, Berezhiani (2020)\nCheung, Keung, Lu, Tseng (2020)',
           GOLD, 9)

ax.set_xlim(-0.8, 3.2)
ax.set_ylim(-2.5, 5.5)

save_fig(fig, 'phys16_03_three_anomalies.png')


# ================================================================
# FIG 4: CKM MATRIX EXTENSION — 3x3 TO 3x4
# Type: Geometric/connection
# Shows: The standard 3x3 CKM with deficit in row 1, then the
# extended matrix with the fourth column absorbing the deficit.
# ================================================================

fig, ax = dark_canvas("The CKM Extension: Where the Missing 0.2% Goes",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Standard 3x3 CKM — left
ax.text(2.5, 9.0, 'Standard CKM (3\u00d73)', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

# Grid
sm_matrix = [
    ['V_ud', 'V_us', 'V_ub'],
    ['V_cd', 'V_cs', 'V_cb'],
    ['V_td', 'V_ts', 'V_tb'],
]
row_labels = ['u', 'c', 't']
col_labels = ['d', 's', 'b']

for i in range(3):
    for j in range(3):
        x = 1.2 + j * 1.1
        y = 7.5 - i * 1.0
        color = RED if i == 0 else SILVER
        ax.text(x, y, sm_matrix[i][j], fontsize=10, color=color,
                ha='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=BG,
                          edgecolor=color if i == 0 else DIM,
                          linewidth=1.5 if i == 0 else 0.5))
    ax.text(0.7, 7.5 - i * 1.0, row_labels[i], fontsize=10, color=CYAN,
            ha='center', fontweight='bold')

for j in range(3):
    ax.text(1.2 + j * 1.1, 8.3, col_labels[j], fontsize=10, color=GREEN,
            ha='center', fontweight='bold')

# Row 1 sum with deficit
ax.text(2.5, 4.8, 'Row 1: |V_ud|\u00b2 + |V_us|\u00b2 + |V_ub|\u00b2', fontsize=10,
        color=RED, ha='center', fontweight='bold')
ax.text(2.5, 4.2, '= 0.99798 \u00b1 0.00038', fontsize=12, color=RED,
        ha='center', fontweight='bold')
ax.text(2.5, 3.6, '\u2260 1.000 (deficit: 0.002)', fontsize=10, color=RED,
        ha='center')

# Arrow to extended
ax.annotate('', xy=(6.0, 6.5), xytext=(4.5, 6.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=3))
ax.text(5.25, 7.0, 'Add 4th\ncolumn', fontsize=10, color=GOLD,
        ha='center', fontweight='bold')

# Extended 3x4 CKM — right
ax.text(7.5, 9.0, 'Extended CKM (3\u00d74)', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')

ext_matrix = [
    ['V_ud', 'V_us', 'V_ub', "V_ub'"],
    ['V_cd', 'V_cs', 'V_cb', "V_cb'"],
    ['V_td', 'V_ts', 'V_tb', "V_tb'"],
]
ext_col_labels = ['d', 's', 'b', "b'"]

for i in range(3):
    for j in range(4):
        x = 5.8 + j * 1.1
        y = 7.5 - i * 1.0
        if j == 3:
            color = GOLD
            edge = GOLD
            lw = 2
        elif i == 0:
            color = GREEN
            edge = GREEN
            lw = 1.5
        else:
            color = SILVER
            edge = DIM
            lw = 0.5
        ax.text(x, y, ext_matrix[i][j], fontsize=10, color=color,
                ha='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=BG,
                          edgecolor=edge, linewidth=lw))

for j in range(4):
    color = GOLD if j == 3 else GREEN
    ax.text(5.8 + j * 1.1, 8.3, ext_col_labels[j], fontsize=10, color=color,
            ha='center', fontweight='bold')

# Row 1 sum with fourth column
ax.text(7.5, 4.8, 'Row 1: |V_ud|\u00b2 + |V_us|\u00b2 + |V_ub|\u00b2 + |V_ub\'|\u00b2',
        fontsize=10, color=GREEN, ha='center', fontweight='bold')
ax.text(7.5, 4.2, '= 0.998 + 0.002 = 1.000', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')
ax.text(7.5, 3.6, '|V_ub\'| \u2248 0.045 absorbs the deficit', fontsize=10,
        color=GOLD, ha='center', fontweight='bold')

# Bottom
ax.text(5.0, 1.5, 'Every nuclear beta decay and kaon decay since the 1950s\n'
        'has been leaking a tiny fraction into the Cabibbo Doublet.\n'
        'The leakage IS the unitarity deficit.',
        fontsize=10, color=SILVER, ha='center')

save_fig(fig, 'phys16_04_ckm_extension.png')


# ================================================================
# FIG 5: PARAMETER COUNT — SM VS SM+CD VS MSSM
# Type: Comparison bar
# Shows: Parameters and unresolved anomalies for each scenario.
# The economy of the Cabibbo Doublet.
# ================================================================

fig, ax = dark_fig("Parameter Economy: What Each Scenario Costs and Buys",
                   xlabel="",
                   ylabel="",
                   size=(16, 10))

scenarios = [
    ('SM', 17, 3, RED, '3 anomalies\nunresolved'),
    ('SM +\nCabibbo Doublet', 23, 0, CYAN, '0 anomalies\n+6 params'),
    ('MSSM', 122, 0, GREEN, '0 anomalies\n+105 params'),
]

# Parameters bars
for i, (label, params, anomalies, color, note_text) in enumerate(scenarios):
    x = i * 2.5
    # Parameter bar
    ax.bar(x, params, color=color, alpha=0.5, edgecolor=color,
           linewidth=2, width=1.0)
    ax.text(x, params + 3, '%d\nparameters' % params, fontsize=12,
            color=color, ha='center', fontweight='bold')

    # Anomalies indicator
    if anomalies > 0:
        for a in range(anomalies):
            ax.text(x + 0.3 * (a - 1), params - 5, '\u2717', fontsize=16,
                    color=RED, ha='center')
        ax.text(x, params - 10, '%d unresolved\nanomalies' % anomalies,
                fontsize=9, color=RED, ha='center', fontweight='bold')
    else:
        ax.text(x, params - 5, '\u2713', fontsize=20, color=GREEN,
                ha='center')
        ax.text(x, params - 10, 'All anomalies\nresolved', fontsize=9,
                color=GREEN, ha='center', fontweight='bold')

ax.set_xticks([i * 2.5 for i in range(3)])
ax.set_xticklabels([s[0] for s in scenarios], fontsize=11, color=SILVER)

# Gap ratio quality
gap_data = [
    (0, '218/115\n40% miss', RED),
    (2.5, '38/27\n3.6% miss', CYAN),
    (5.0, '7/5\n3.1% miss', GREEN),
]
for x, text, color in gap_data:
    ax.text(x, -18, 'Gap ratio:\n%s' % text, fontsize=8, color=color,
            ha='center')

# The point
result_box(ax, 2.5, 100,
           'The Cabibbo Doublet adds 6 parameters.\n'
           'It resolves 3 anomalies, fixes the gap ratio,\n'
           'and produces a testable proton decay prediction.\n'
           'The MSSM adds 105+ for similar gap ratio quality.',
           GOLD, 9)

ax.set_xlim(-1.5, 6.5)
ax.set_ylim(-25, 140)
ax.set_yticks([])

save_fig(fig, 'phys16_05_parameter_count.png')


# ================================================================
# FIG 6: ENERGY LANDSCAPE — NEW THRESHOLD AT M_VL
# Type: Running/landscape
# Shows: The full energy axis with the Cabibbo Doublet threshold
# highlighted. Below M_VL: gap ratio = 218/115. Above: 38/27.
# ================================================================

fig, ax = dark_fig("The New Threshold: Where the Gap Ratio Changes",
                   xlabel="log\u2081\u2080(E / GeV)",
                   ylabel="Gap ratio",
                   size=(16, 10))

# Energy range
log_E = np.linspace(2, 16, 300)

# Gap ratio is 218/115 below M_VL, 38/27 above
M_VL_log = np.log10(3000)  # ~3 TeV as representative
gap_below = 218.0 / 115
gap_above = 38.0 / 27

gap_ratio = np.where(log_E < M_VL_log, gap_below, gap_above)

# Plot as step function
curve(ax, log_E[log_E < M_VL_log], gap_ratio[log_E < M_VL_log],
      'SM: 218/115 = 1.896', RED, 3)
curve(ax, log_E[log_E >= M_VL_log], gap_ratio[log_E >= M_VL_log],
      'SM + CD: 38/27 = 1.407', CYAN, 3)

# Threshold
ax.plot([M_VL_log, M_VL_log], [1.2, 2.0], color=GOLD, linewidth=3,
        linestyle='--')
ax.text(M_VL_log, 2.05, 'M_VL\n(1.5\u20136 TeV)', fontsize=12, color=GOLD,
        ha='center', fontweight='bold')

# Step annotation
ax.annotate('', xy=(M_VL_log + 0.1, gap_above), xytext=(M_VL_log - 0.1, gap_below),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
ax.text(M_VL_log + 1.5, (gap_below + gap_above) / 2,
        '\u0394b = (1/15, 1, 1/3)\nOne threshold\nchanges the ratio\nby 26%',
        fontsize=10, color=GREEN, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))

# Measured line
ax.plot([2, 16], [1.358, 1.358], color=GOLD, linewidth=2,
        linestyle=':', alpha=0.6)
ax.text(14.5, 1.38, 'Measured\n1.358', fontsize=10, color=GOLD,
        fontweight='bold')

# SM fermion thresholds (unchanged gap ratio)
sm_thresholds = [
    (np.log10(1.777), 'm_\u03c4'),
    (np.log10(4.183), 'm_b'),
    (np.log10(91.19), 'M_Z'),
    (np.log10(172.57), 'm_t'),
]
for log_m, label in sm_thresholds:
    ax.plot([log_m, log_m], [1.85, 1.92], color=DIM, linewidth=1, alpha=0.4)
    ax.text(log_m, 1.93, label, fontsize=6, color=DIM, ha='center')

# Note: SM thresholds don't change gap ratio
ax.text(1.5, 1.25, 'SM thresholds: gap ratio unchanged\n'
        '(\u0394b\u2081 = \u0394b\u2082 = \u0394b\u2083 = 4/3 per gen)',
        fontsize=8, color=DIM)

ax.set_xlim(0, 16.5)
ax.set_ylim(1.15, 2.15)

legend(ax, loc='upper right')

save_fig(fig, 'phys16_06_energy_landscape.png')


# ================================================================
# FIG 7: DECAY CHANNELS — 50/25/25 BRANCHING PATTERN
# Type: Comparison bar (distinct — decay modes)
# Shows: The characteristic branching ratios for upper (+2/3)
# and lower (-1/3) components of the Cabibbo Doublet.
# ================================================================

fig = plt.figure(figsize=(18, 9), facecolor=BG)

# Left: upper component VL_U (+2/3)
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_facecolor(BG)

channels_u = [
    ('Wb', 50, RED, 'Dominant'),
    ('Zt', 25, BLUE, 'Subdominant'),
    ('Ht', 25, GREEN, 'Subdominant'),
]

for i, (ch, frac, color, note_text) in enumerate(channels_u):
    ax1.bar(i, frac, color=color, alpha=0.6, edgecolor=color,
            linewidth=2, width=0.6)
    ax1.text(i, frac + 2, '%d%%' % frac, fontsize=14, color=color,
             ha='center', fontweight='bold')
    ax1.text(i, -5, 'VL_U \u2192 %s' % ch, fontsize=9, color=SILVER,
             ha='center')

ax1.set_title('Upper Component (Q = +2/3)', fontsize=13, color=CYAN,
              fontweight='bold', pad=15)
ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['Wb', 'Zt', 'Ht'], fontsize=11, color=SILVER)
ax1.set_ylabel('Branching ratio (%)', fontsize=10, color=SILVER)
ax1.set_ylim(-10, 65)
ax1.tick_params(colors=DIM)
for spine in ax1.spines.values():
    spine.set_color(PAN)

# Right: lower component VL_D (-1/3)
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_facecolor(BG)

channels_d = [
    ('Wt', 50, RED, 'Dominant'),
    ('Zb', 25, BLUE, 'Subdominant'),
    ('Hb', 25, GREEN, 'Subdominant'),
]

for i, (ch, frac, color, note_text) in enumerate(channels_d):
    ax2.bar(i, frac, color=color, alpha=0.6, edgecolor=color,
            linewidth=2, width=0.6)
    ax2.text(i, frac + 2, '%d%%' % frac, fontsize=14, color=color,
             ha='center', fontweight='bold')
    ax2.text(i, -5, 'VL_D \u2192 %s' % ch, fontsize=9, color=SILVER,
             ha='center')

ax2.set_title('Lower Component (Q = \u22121/3)', fontsize=13, color=ORANGE,
              fontweight='bold', pad=15)
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['Wt', 'Zb', 'Hb'], fontsize=11, color=SILVER)
ax2.set_ylim(-10, 65)
ax2.tick_params(colors=DIM)
for spine in ax2.spines.values():
    spine.set_color(PAN)

fig.suptitle('Cabibbo Doublet Decay Channels: The 50/25/25 Signature',
             fontsize=15, color=GOLD, fontweight='bold', y=0.98)

fig.text(0.5, 0.03, 'From the Goldstone boson equivalence theorem. '
         'Exact at M_VL \u226b M_W, M_Z, m_H. Phase space corrections at ~1.5 TeV.',
         fontsize=9, color=SILVER, ha='center')

path = os.path.join(get_outdir(), 'phys16_07_decay_channels.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys16_07_decay_channels.png")


# ================================================================
# FIG 8: PHYS-16 IDENTITY CARD
# Type: Identity card
# Shows: Two roads, three anomalies, one particle, mass window.
# ================================================================

fig, ax = dark_canvas("PHYS-16 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE CABIBBO DOUBLET', fontsize=22, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'One particle. Two roads. Three anomalies. One test.',
        fontsize=12, color=SILVER, ha='center', style='italic')

# The particle
ax.text(5, 7.5, '(3, 2, 1/6)', fontsize=24, color=WHITE,
        ha='center', fontweight='bold', fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=3))
ax.text(5, 6.7, 'Upper: +2/3    Lower: \u22121/3    Vector-like    Anomaly-free',
        fontsize=9, color=SILVER, ha='center')

# Left: Road 1
ax.text(2.0, 5.7, 'ROAD 1: Gap Ratio', fontsize=11, color=CYAN,
        ha='center', fontweight='bold')
road1 = [
    ('Gap ratio:', '38/27 = 1.407'),
    ('Distance:', '0.049 from measured'),
    ('M_GUT:', '10^{15.5} GeV'),
    ('\u0394b\u2082/\u0394b\u2081:', '15:1 (maximum)'),
]
for i, (prop, val) in enumerate(road1):
    ax.text(1.0, 5.0 - i * 0.45, prop, fontsize=8, color=SILVER)
    ax.text(3.0, 5.0 - i * 0.45, val, fontsize=9, color=CYAN, fontweight='bold')

# Right: Road 2
ax.text(8.0, 5.7, 'ROAD 2: Anomalies', fontsize=11, color=ORANGE,
        ha='center', fontweight='bold')
road2 = [
    ('CKM deficit:', '0.002 \u2192 |V_ub\'| \u2248 0.045'),
    ('A_FB^b:', '3\u03c3 resolved by Z-b mixing'),
    ('Higgs \u03bc:', '~2\u03c3 enhanced by loop'),
    ('Mass window:', '1.5\u20136 TeV'),
]
for i, (prop, val) in enumerate(road2):
    ax.text(6.5, 5.0 - i * 0.45, prop, fontsize=8, color=SILVER)
    ax.text(9.0, 5.0 - i * 0.45, val, fontsize=9, color=ORANGE,
            fontweight='bold')

# The tests
ax.plot([0.5, 9.5], [2.5, 2.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 2.0, 'THE TESTS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

tests = [
    ('Hyper-K (2027+):', 'Proton decay \u03c4 ~ 10\u00b3\u2074\u207b\u00b3\u2075 yr', GREEN),
    ('HL-LHC (now\u20132040):', 'Direct production if M < 2\u20133 TeV', CYAN),
    ('Belle II (now\u20132030+):', 'CKM precision \u2192 sharpen anomaly', ORANGE),
]
for i, (exp, prediction, color) in enumerate(tests):
    ax.text(2.5, 1.3 - i * 0.45, exp, fontsize=9, color=SILVER)
    ax.text(6.5, 1.3 - i * 0.45, prediction, fontsize=9, color=color,
            fontweight='bold')

save_fig(fig, 'phys16_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-16 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys16_01_mass_window.png',
    'phys16_02_two_roads.png',
    'phys16_03_three_anomalies.png',
    'phys16_04_ckm_extension.png',
    'phys16_05_parameter_count.png',
    'phys16_06_energy_landscape.png',
    'phys16_07_decay_channels.png',
    'phys16_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    