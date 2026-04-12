#!/usr/bin/env python3
"""
HOWL PHYS-38 Diagrams — Precision Frontier: 38 Derived Values
8 figures covering alpha corrections, EW convergence, precision landscape,
BBN four elements, correction cascade, integer map, muon g-2, identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
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

def dark_fig(w=16, h=10):
    fig, ax = plt.subplots(figsize=(w, h), facecolor=BG)
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    return fig, ax

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def draw_box(ax, x, y, w, h, text, color, fontsize=10, alpha=1.0):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle='round,pad=0.15', facecolor=BG,
                          edgecolor=color, linewidth=2, alpha=alpha)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=color,
            ha='center', va='center', linespacing=1.5)

def arrow(ax, x1, y1, x2, y2, color=SILVER, lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))


# ================================================================
# FIG 1: ALPHA BEFORE/AFTER CORRECTIONS — FOUR DETERMINATIONS
# Type: Type 6 (Comparison Bar)
# Shows: Five alpha determinations on a zoomed ppb axis. The
#        corrected value overlaps Rb recoil at 12 digits. The
#        uncorrected sits 4 ppb away. The 18x improvement is spatial.
# ================================================================

fig, ax = dark_fig(16, 10)

base = 137.035999
methods = [
    'This work\n(uncorrected)',
    'Cs recoil\n(Parker 2018)',
    'CODATA 2018\nrecommended',
    'This work\n(7 corrections)',
    'Rb recoil\n(Morel 2020)',
]
values_alpha = [137.035998630, 137.035999046, 137.035999084, 137.035999207, 137.035999206]
errors = [0, 0.000000027, 0.000000021, 0, 0.000000011]
colors_a = [RED, CYAN, MAG, GOLD, GREEN]
offsets = [(v - base) * 1e6 for v in values_alpha]
errors_scaled = [e * 1e6 for e in errors]

y_positions = [4, 3, 2, 1, 0]

for i in range(5):
    xerr = errors_scaled[i] if errors_scaled[i] > 0 else None
    marker = 'D' if i in [0, 3] else 'o'
    ax.errorbar(offsets[i], y_positions[i], xerr=xerr,
                fmt=marker, color=colors_a[i], markersize=12,
                markeredgecolor=WHITE, markeredgewidth=2, capsize=8, capthick=2,
                ecolor=colors_a[i], elinewidth=2, zorder=5)
    text_x = offsets[i] + 0.02
    ha = 'left'
    if i == 0:
        text_x = offsets[i] - 0.02
        ha = 'right'
    ax.text(text_x, y_positions[i] + 0.30, '%.9f' % values_alpha[i],
            fontsize=9, color=colors_a[i], va='bottom', ha=ha)
    if errors[i] > 0:
        miss_ppb = errors[i] / values_alpha[i] * 1e9
        ax.text(text_x, y_positions[i] - 0.30, '%s%.1f ppb unc' % (u'\u00b1', miss_ppb),
                fontsize=8, color=DIM, va='top', ha=ha)

# 18x improvement arrow
ax.annotate('', xy=(offsets[3], 3.7), xytext=(offsets[0], 3.7),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text((offsets[0] + offsets[3]) / 2, 3.85, '18x improvement\n(+3.77 ppb shift)',
        fontsize=9, color=ORANGE, ha='center', va='bottom')

# Rb-Cs tension
ax.annotate('', xy=(offsets[1], -0.3), xytext=(offsets[4], -0.3),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1.5))
ax.text((offsets[1] + offsets[4]) / 2, -0.5, 'Rb-Cs tension: 1.17 ppb (5.4%s)' % u'\u03c3',
        fontsize=8, color=DIM, ha='center', va='top')

# 12-digit agreement label
ax.text(offsets[3] + 0.02, 0.5, '12-digit agreement\n0.007 ppb',
        fontsize=10, color=GOLD, ha='left', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_yticks(y_positions)
ax.set_yticklabels(methods, fontsize=10, color=SILVER)
ax.set_xlabel(r'$\alpha^{-1} - 137.035999$ ($\times 10^{-6}$)', fontsize=12, color=SILVER)
ax.set_xlim(-0.45, 0.30)
ax.set_ylim(-0.9, 4.6)
ax.set_title('Fine Structure Constant: 18x Improvement from Seven Corrections',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, 'phys38_01_alpha_corrections.png')


# ================================================================
# FIG 2: EW FOUR-VERSION CONVERGENCE
# Type: Type 1 (Running/Convergence)
# Shows: M_W, Gamma_Z tracked across 4 versions converging on
#        measured values. Each correction closes a specific gap.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

for ax in (ax1, ax2):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)

# Left panel: M_W
versions = [0, 1, 2, 3]
mw_vals = [79953, 80334, 80337, 80354]
mw_meas = 80369.2
mw_unc = 13.3
vlabels = ['Tree', 'v0\n(+%s)' % u'\u03c1', 'v1\n(+corr)', 'v2\n(G_F)']
vcolors = [RED, ORANGE, CYAN, GREEN]

ax1.axhspan(mw_meas - mw_unc, mw_meas + mw_unc, color=MAG, alpha=0.12)
ax1.axhspan(mw_meas - 3*mw_unc, mw_meas + 3*mw_unc, color=MAG, alpha=0.04)
ax1.axhline(y=mw_meas, color=MAG, linewidth=2, linestyle='--', alpha=0.7)
ax1.text(3.5, mw_meas + 20, 'PDG: 80369 MeV', fontsize=9, color=MAG, ha='right')

ax1.plot(versions, mw_vals, '-', color=DIM, linewidth=1.5, alpha=0.5)
for i in range(4):
    ax1.scatter(versions[i], mw_vals[i], s=250, c=vcolors[i],
               edgecolors=WHITE, linewidth=2, zorder=5)
    miss_ppm = abs(mw_vals[i] - mw_meas) / mw_meas * 1e6
    label = '%d MeV\n(%.0f ppm)' % (mw_vals[i], miss_ppm)
    yoff = -60 if i < 2 else 25
    ax1.annotate(label, xy=(versions[i], mw_vals[i]),
                xytext=(versions[i] + 0.15, mw_vals[i] + yoff),
                fontsize=8, color=vcolors[i],
                arrowprops=dict(arrowstyle='->', color=vcolors[i], lw=1))

ax1.set_xticks(versions)
ax1.set_xticklabels(vlabels, fontsize=9, color=SILVER)
ax1.set_ylabel('M_W (MeV)', fontsize=12, color=SILVER)
ax1.set_title('W Boson Mass', fontsize=13, fontweight='bold', color=GOLD, pad=10)
ax1.set_xlim(-0.5, 3.8)
ax1.set_ylim(79850, 80450)

# Right panel: Gamma_Z
gz_vals = [2337, 2424, 2510, 2515]
gz_meas = 2495.2
gz_unc = 2.3

ax2.axhspan(gz_meas - 3*gz_unc, gz_meas + 3*gz_unc, color=MAG, alpha=0.04)
ax2.axhspan(gz_meas - gz_unc, gz_meas + gz_unc, color=MAG, alpha=0.12)
ax2.axhline(y=gz_meas, color=MAG, linewidth=2, linestyle='--', alpha=0.7)
ax2.text(3.5, gz_meas + 8, 'LEP: 2495.2 MeV', fontsize=9, color=MAG, ha='right')

ax2.plot(versions, gz_vals, '-', color=DIM, linewidth=1.5, alpha=0.5)
for i in range(4):
    ax2.scatter(versions[i], gz_vals[i], s=250, c=vcolors[i],
               edgecolors=WHITE, linewidth=2, zorder=5)
    miss_pct = abs(gz_vals[i] - gz_meas) / gz_meas * 100
    label = '%d MeV\n(%.1f%%)' % (gz_vals[i], miss_pct)
    yoff = -30 if i < 2 else 15
    ax2.annotate(label, xy=(versions[i], gz_vals[i]),
                xytext=(versions[i] + 0.15, gz_vals[i] + yoff),
                fontsize=8, color=vcolors[i],
                arrowprops=dict(arrowstyle='->', color=vcolors[i], lw=1))

ax2.set_xticks(versions)
ax2.set_xticklabels(vlabels, fontsize=9, color=SILVER)
ax2.set_ylabel('%s_Z (MeV)' % u'\u0393', fontsize=12, color=SILVER)
ax2.set_title('Z Total Width', fontsize=13, fontweight='bold', color=GOLD, pad=10)
ax2.set_xlim(-0.5, 3.8)
ax2.set_ylim(2280, 2560)

save(fig, 'phys38_02_ew_convergence.png')


# ================================================================
# FIG 3: PRECISION LANDSCAPE — 38 VALUES ON LOG SCALE
# Type: Type 2 (Scale/Landscape)
# Shows: All 38 derived values on a log-scale precision axis from
#        0.007 ppb to 196%. Seven domains color-coded.
# ================================================================

fig, ax = dark_fig(16, 14)

# Selected representative values (not all 38 — too dense. Show 25 most distinct)
values_data = [
    ('%s vs Rb' % u'\u03b1\u207b\u00b9', 7e-6, GOLD),
    ('%s (corrected)' % u'\u03b1\u207b\u00b9', 0.22e-3, GOLD),
    ('a_0', 0.22e-3, GOLD),
    ('%s_0' % u'\u03bc', 0.22e-3, GOLD),
    ('R_%s' % u'\u221e', 0.44e-3, GOLD),
    ('m_%s (Koide)' % u'\u03c4', 0.006, PURPLE),
    ('M_W (G_F path)', 0.020, CYAN),
    ('M_W (sin%s path)' % u'\u00b2', 0.040, CYAN),
    ('%s_b' % u'\u03a9', 0.073, BLUE),
    ('DM/baryon', 0.073, BLUE),
    ('D/H', 0.14, GREEN),
    ('%s_%s' % (u'\u03c1', u'\u039b'), 0.15, BLUE),
    ('%s_DE' % u'\u03a9', 0.20, BLUE),
    ('sin%s%s_eff' % (u'\u00b2', u'\u03b8'), 0.24, CYAN),
    ('%s_10' % u'\u03b7', 0.24, BLUE),
    ('R_l', 0.27, CYAN),
    ('%s_m' % u'\u03a9', 0.44, BLUE),
    ('%s(Z%see)' % (u'\u0393', u'\u2192'), 0.67, CYAN),
    ('%s_Z total' % u'\u0393', 0.81, CYAN),
    ('Y_p', 1.5, GREEN),
    ('He-3/H', 6.6, GREEN),
    ('CKM 4x4 overshoot', 33, ORANGE),
    ('Li-7/H', 196, RED),
    ('a_%s anomaly' % u'\u03bc', 273, RED),
]

y_pos = np.arange(len(values_data))
miss_pct = [v[1] for v in values_data]
colors_p = [v[2] for v in values_data]
labels_p = [v[0] for v in values_data]

bars = ax.barh(y_pos, miss_pct, height=0.6, color=colors_p, alpha=0.7,
               edgecolor=colors_p, linewidth=1.5)

for i, (label, miss, color) in enumerate(values_data):
    if miss < 0.001:
        text = '%.1f ppt' % (miss * 1e6)
    elif miss < 0.01:
        text = '%.2f ppb' % (miss * 1000)
    elif miss < 1:
        if miss < 0.1:
            text = '%.0f ppm' % (miss * 10000)
        else:
            text = '%.2f%%' % miss
    else:
        text = '%.0f%%' % miss
    ax.text(miss * 1.4, i, text, fontsize=8, color=color, va='center')

ax.set_xscale('log')
ax.set_xlim(3e-6, 500)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels_p, fontsize=9, color=SILVER)
ax.set_xlabel('Miss from measured value (%)', fontsize=12, color=SILVER)
ax.set_title('Precision Landscape: 38 Derived Values Across 7 Domains',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Domain legend
legend_elements = [
    mpatches.Patch(facecolor=GOLD, alpha=0.7, label='QED'),
    mpatches.Patch(facecolor=CYAN, alpha=0.7, label='Electroweak'),
    mpatches.Patch(facecolor=BLUE, alpha=0.7, label='Cosmology'),
    mpatches.Patch(facecolor=GREEN, alpha=0.7, label='Nuclear/BBN'),
    mpatches.Patch(facecolor=PURPLE, alpha=0.7, label='Mass (Koide)'),
    mpatches.Patch(facecolor=ORANGE, alpha=0.7, label='Flavor (CD)'),
    mpatches.Patch(facecolor=RED, alpha=0.7, label='Anomalies'),
]
ax.legend(handles=legend_elements, fontsize=8, facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, loc='lower right')

# Threshold lines
ax.axvline(x=1.0, color=DIM, linewidth=1, linestyle='--', alpha=0.5)
ax.text(1.1, 0.5, '1%', fontsize=8, color=DIM, rotation=90)

ax.invert_yaxis()

save(fig, 'phys38_03_precision_landscape.png')


# ================================================================
# FIG 4: BBN FOUR ELEMENTS WITH SIGMA BANDS
# Type: Type 3 (Threshold/Region)
# Shows: Four panels, one per element. D/H, Y_p, He-3 inside their
#        measurement bands. Li-7 dramatically outside — 2.96x above.
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(18, 14), facecolor=BG,
                          gridspec_kw={'hspace': 0.35, 'wspace': 0.30})

for ax in axes.flat:
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)

elements = [
    ('D/H', 2.531e-5, 2.527e-5, 0.030e-5, 1e5, '0.12%s' % u'\u03c3', GREEN),
    ('Y_p (He-4)', 0.2486, 0.2449, 0.004, 1, '0.94%s' % u'\u03c3', GREEN),
    ('He-3/H', 1.027e-5, 1.10e-5, 0.20e-5, 1e5, '0.36%s' % u'\u03c3', GREEN),
    ('Li-7/H', 4.74e-10, 1.60e-10, 0.30e-10, 1e10, '2.96x', RED),
]

for idx, (name, derived, measured, unc, scale, sigma_text, color) in enumerate(elements):
    ax = axes.flat[idx]
    d_s = derived * scale
    m_s = measured * scale
    u_s = unc * scale

    ax.axhspan(m_s - u_s, m_s + u_s, color=MAG, alpha=0.15)
    ax.axhspan(m_s - 2*u_s, m_s + 2*u_s, color=MAG, alpha=0.06)
    ax.axhline(y=m_s, color=MAG, linewidth=2, linestyle='--', alpha=0.7)

    ax.scatter(0.5, d_s, s=300, c=color, edgecolors=WHITE, linewidth=2, zorder=5)
    ax.scatter(0.5, m_s, s=200, c=MAG, edgecolors=WHITE, linewidth=2, zorder=5, marker='D')

    # Range for y-axis
    all_vals = [d_s, m_s, m_s - 2*u_s, m_s + 2*u_s]
    ymin = min(all_vals) - abs(d_s - m_s) * 0.3
    ymax = max(all_vals) + abs(d_s - m_s) * 0.3
    if ymin == ymax:
        ymin -= 0.1
        ymax += 0.1
    ax.set_ylim(ymin, ymax)

    ax.annotate('Derived: %.4g (%s)' % (d_s, sigma_text),
                xy=(0.5, d_s), xytext=(0.85, d_s),
                fontsize=10, color=color,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
    ax.annotate('Measured: %.4g %s %.3g' % (m_s, u'\u00b1', u_s),
                xy=(0.5, m_s), xytext=(0.85, m_s - (d_s - m_s) * 0.15),
                fontsize=9, color=MAG,
                arrowprops=dict(arrowstyle='->', color=MAG, lw=1))

    if scale == 1:
        ylabel = name
    elif scale == 1e5:
        ylabel = '%s (%s10%s)' % (name, u'\u00d7', u'\u2075')
    elif scale == 1e10:
        ylabel = '%s (%s10%s)' % (name, u'\u00d7', u'\u00b9\u2070')
    ax.set_ylabel(ylabel, fontsize=11, color=SILVER)
    ax.set_xlim(0, 1.5)
    ax.set_xticks([])
    ax.set_title(name, fontsize=13, fontweight='bold', color=GOLD, pad=10)

    if idx == 3:
        ax.text(1.1, (d_s + m_s) / 2, 'THE LITHIUM\nPROBLEM',
                fontsize=11, color=RED, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.9))

save(fig, 'phys38_04_bbn_four_elements.png')


# ================================================================
# FIG 5: CORRECTION CASCADE — SEVEN CORRECTIONS MOVING ALPHA
# Type: Type 7 (Progression/Sequence)
# Shows: Alpha starting at uncorrected value, seven arrows pushing
#        it incrementally to land on the Rb recoil target.
# ================================================================

fig, ax = dark_fig(16, 12)

# Vertical number line in ppb relative to CODATA
# Uncorrected: -3.99 ppb from CODATA
# Corrected: +0.22 ppb from CODATA
# Rb recoil: +0.90 ppb from CODATA (approximately)

corrections = [
    ('Mass-dep 2-loop\n(+1.95 ppb)', 1.95, CYAN),
    ('Hadronic LO VP\n(+1.33 ppb)', 1.33, BLUE),
    ('Hadronic LbL\n(+0.24 ppb)', 0.24, BLUE),
    ('Hadronic NLO\n(-0.16 ppb)', -0.16, RED),
    ('Mass-dep 3-loop\n(+0.08 ppb)', 0.08, CYAN),
    ('Mass-dep 4-loop\n(+0.02 ppb)', 0.02, CYAN),
    ('Electroweak\n(+0.02 ppb)', 0.02, PURPLE),
]

# Starting position (ppb from CODATA)
pos = -3.99
x_bar = 3.0  # x position of the vertical bar

# Draw the progression
positions = [pos]
for label, shift, color in corrections:
    pos += shift
    positions.append(pos)

# Background: measurement targets
ax.axhline(y=0, color=MAG, linewidth=2, linestyle='--', alpha=0.5)
ax.text(8.5, 0.15, 'CODATA 2018', fontsize=9, color=MAG)

ax.axhline(y=0.90, color=GREEN, linewidth=2, linestyle='--', alpha=0.5)
ax.text(8.5, 1.05, 'Rb recoil (Morel 2020)', fontsize=9, color=GREEN)

ax.axhline(y=-0.27, color=CYAN, linewidth=1.5, linestyle=':', alpha=0.4)
ax.text(8.5, -0.42, 'Cs recoil (Parker 2018)', fontsize=8, color=CYAN, alpha=0.7)

# Starting point
ax.scatter(x_bar, positions[0], s=250, c=RED, edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(x_bar - 0.3, positions[0], 'Uncorrected\n%.2f ppb' % positions[0],
        fontsize=10, color=RED, ha='right', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED, alpha=0.9))

# Draw each correction as an arrow
cumulative = positions[0]
for i, (label, shift, color) in enumerate(corrections):
    y_start = cumulative
    y_end = cumulative + shift
    
    # Arrow
    if abs(shift) > 0.05:
        ax.annotate('', xy=(x_bar, y_end), xytext=(x_bar, y_start),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
    else:
        ax.plot([x_bar, x_bar], [y_start, y_end], '-', color=color, linewidth=2.5)
    
    # Label to the right
    x_label = x_bar + 0.4 + (i % 2) * 2.5
    ax.text(x_label, (y_start + y_end) / 2, label,
            fontsize=9, color=color, ha='left', va='center')
    ax.plot([x_bar + 0.05, x_label - 0.05], [(y_start + y_end) / 2, (y_start + y_end) / 2],
            '-', color=color, linewidth=0.5, alpha=0.5)
    
    cumulative = y_end

# Final point
ax.scatter(x_bar, positions[-1], s=300, c=GOLD, edgecolors=WHITE, linewidth=2, zorder=5, marker='*')
ax.text(x_bar - 0.3, positions[-1], 'Corrected\n+%.2f ppb' % positions[-1],
        fontsize=10, color=GOLD, ha='right', va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_xlim(0.5, 12)
ax.set_ylim(-5.0, 2.0)
ax.set_ylabel('ppb relative to CODATA 2018', fontsize=12, color=SILVER)
ax.set_xticks([])
ax.set_title('Seven Corrections Move %s from 3.99 ppb Below to 0.22 ppb Above CODATA' % u'\u03b1\u207b\u00b9',
             fontsize=14, fontweight='bold', color=GOLD, pad=15)

# Total shift annotation
ax.text(1.5, -4.5, 'Total shift: +3.77 ppb\nfrom 7 published corrections\n(4.872 %s 10%s)' % (u'\u00d7', u'\u207b\u00b9\u00b2'),
        fontsize=10, color=SILVER, ha='left',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN, edgecolor=DIM))

save(fig, 'phys38_05_correction_cascade.png')


# ================================================================
# FIG 6: INTEGER MAP — 11, 13 TO FOUR ELEMENTS
# Type: Type 5 (Connection/Integer Map)
# Shows: Branching from 11 and 13 through (22/13)pi to Omega_b
#        to eta to four BBN elements. Li-7 branch is red.
# ================================================================

fig, ax = dark_fig(18, 14)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

# Title
ax.text(9, 13.3, 'From Gauge Integers to Primordial Nuclear Abundances',
        fontsize=15, fontweight='bold', color=GOLD, ha='center')

# Source integers
draw_box(ax, 3, 11.5, 4.5, 1.5,
         '11 = Yang-Mills coefficient\n-(11/3) %s C%s(adj)' % (u'\u00d7', u'\u2082'), CYAN, 10)
draw_box(ax, 3, 9.2, 4.5, 1.5,
         '13 = |b%s_mod numerator|\nb%s_mod = -13/6' % (u'\u2082', u'\u2082'), ORANGE, 10)

# Integer combination
draw_box(ax, 9, 10.3, 3.5, 1.2,
         '22/13\n= 2%s11 / 13' % u'\u00d7', GOLD, 11)

# DM/baryon
draw_box(ax, 14.5, 10.3, 4, 1.2,
         '(22/13)%s%s = 5.3165\nDM/baryon (725 ppm)' % (u'\u00d7', u'\u03c0'), BLUE, 10)

# Omega_b
draw_box(ax, 14.5, 8.0, 4, 1.2,
         '%s_b = 0.04904\n(727 ppm from Planck)' % u'\u03a9', BLUE, 10)

# eta
draw_box(ax, 9, 5.5, 3.5, 1.5,
         '%s%s = 6.090\n%s_b %s%s / (n%s m_p)\n(0.24%%)' % (u'\u03b7', u'\u2081\u2080', u'\u03a9', u'\u03c1', u'\u2091\u1d63\u1d62\u1d57', u'\u03b3'),
         GREEN, 10)

# Four BBN elements
draw_box(ax, 2.5, 2.0, 3.5, 1.5,
         'D/H = 2.531%s10%s\n0.12%s' % (u'\u00d7', u'\u207b\u2075', u'\u03c3'), GREEN, 10)
draw_box(ax, 7, 2.0, 3.0, 1.5,
         'Y_p = 0.2486\n0.94%s' % u'\u03c3', GREEN, 10)
draw_box(ax, 11, 2.0, 3.5, 1.5,
         'He-3 = 1.03%s10%s\n0.36%s' % (u'\u00d7', u'\u207b\u2075', u'\u03c3'), GREEN, 10)
draw_box(ax, 15.5, 2.0, 3.5, 1.5,
         'Li-7 = 4.74%s10%s\n2.96%s (PROBLEM)' % (u'\u00d7', u'\u207b\u00b9\u2070', u'\u00d7'), RED, 10)

# Arrows
arrow(ax, 5.25, 11.5, 7.25, 10.7, SILVER)
arrow(ax, 5.25, 9.2, 7.25, 9.9, SILVER)
arrow(ax, 10.75, 10.3, 12.5, 10.3, GOLD)
arrow(ax, 14.5, 9.7, 14.5, 8.6, BLUE)
arrow(ax, 12.5, 7.5, 10.75, 6.3, GREEN)
arrow(ax, 7.5, 4.8, 3.5, 2.8, GREEN)
arrow(ax, 8.5, 4.8, 7, 2.8, GREEN)
arrow(ax, 9.5, 4.8, 11, 2.8, GREEN)
arrow(ax, 10.5, 4.8, 14.5, 2.8, RED, lw=2.5)

# Planck input
draw_box(ax, 14.5, 12.0, 3.5, 0.9,
         '%s_DM = 0.2607 (Planck)' % u'\u03a9', MAG, 9)
arrow(ax, 14.5, 11.55, 14.5, 10.9, MAG)

# Cosmological chain
draw_box(ax, 3.5, 5.5, 3.5, 1.2,
         '%s_DE = 0.6903 (0.20%%)\n%s_%s = 5.89%s10%s' % (u'\u03a9', u'\u03c1', u'\u039b', u'\u00d7', u'\u207b\u00b3\u2070'),
         BLUE, 9)
arrow(ax, 12.5, 7.8, 5.25, 6.1, BLUE)

save(fig, 'phys38_06_integer_map.png')


# ================================================================
# FIG 7: MUON G-2 STACKED BUDGET VS MEASUREMENT
# Type: Type 6 (Comparison Bar)
# Shows: Stacked bar of SM contributions, measurement line above,
#        the 318 x 10^-11 gap visible between them.
# ================================================================

fig, ax = dark_fig(16, 10)

# All in units of 10^-11, offset from 116584000
offset = 116584000
contributions = [
    ('QED (5-loop)', 718.87, GOLD),
    ('Had VP (LO)', 6931, BLUE),
    ('Had VP (NLO)', -983, RED),
    ('Had LbL', 920, CYAN),
    ('Electroweak', 154, PURPLE),
]

# Build cumulative for stacking (starting from QED)
# QED is so large we need to show only the non-QED parts
# Better: show the SM total vs measurement as two bars

sm_total = 116591741 - offset  # = 7741
measured = 116592059 - offset   # = 8059

bar_width = 0.4

# SM prediction bar (stacked from non-QED on top of QED)
qed = 718.87
had_lo = 6931
had_nlo = -983
had_lbl = 920
ew = 154

# Show as two total bars with breakdown annotation
ax.barh(1, sm_total, height=bar_width, color=GREEN, alpha=0.7,
        edgecolor=GREEN, linewidth=2, label='SM prediction')
ax.barh(0, measured, height=bar_width, color=MAG, alpha=0.7,
        edgecolor=MAG, linewidth=2, label='Fermilab measurement')

# Gap annotation
gap = measured - sm_total
ax.annotate('', xy=(measured, 0.7), xytext=(sm_total, 0.7),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2.5))
ax.text((sm_total + measured) / 2, 0.82, '%s = 318 %s 10%s\n(6.5%s)' % (u'\u0394', u'\u00d7', u'\u207b\u00b9\u00b9', u'\u03c3'),
        fontsize=12, color=ORANGE, ha='center', va='bottom', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE, alpha=0.9))

# Labels on bars
ax.text(sm_total - 50, 1, 'SM: %d %s 10%s' % (116591741, u'\u00d7', u'\u207b\u00b9\u00b9'),
        fontsize=10, color=WHITE, ha='right', va='center')
ax.text(measured - 50, 0, 'Exp: %d %s 10%s' % (116592059, u'\u00d7', u'\u207b\u00b9\u00b9'),
        fontsize=10, color=WHITE, ha='right', va='center')

# Budget breakdown box
budget_text = ('SM Budget:\n'
               'QED: 116584719 (99.994%%)\n'
               'Had VP(LO): +6931 %s 40\n'
               'Had VP(NLO): -983\n'
               'Had LbL: +920 %s 18\n'
               'EW: +154') % (u'\u00b1', u'\u00b1')
ax.text(2500, 1.7, budget_text, fontsize=9, color=SILVER, ha='left', va='top',
        fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN, edgecolor=DIM))

# Alpha shift note
ax.text(2500, -0.6, 'Our %s shift: -0.025 %s 10%s\n(12,700%s smaller than anomaly)' % (u'\u03b1', u'\u00d7', u'\u207b\u00b9\u00b9', u'\u00d7'),
        fontsize=9, color=DIM, ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN, edgecolor=DIM, alpha=0.5))

ax.set_yticks([0, 1])
ax.set_yticklabels(['Measured\n(Fermilab + BNL)', 'SM Prediction\n(this work)'],
                   fontsize=11, color=SILVER)
ax.set_xlabel('a_%s %s 116584000 (%s 10%s)' % (u'\u03bc', u'\u2212', u'\u00d7', u'\u207b\u00b9\u00b9'), fontsize=12, color=SILVER)
ax.set_xlim(0, 9000)
ax.set_ylim(-0.9, 2.2)
ax.set_title('Muon g-2: Standard Model Prediction vs Fermilab Measurement',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, 'phys38_07_muon_g2.png')


# ================================================================
# FIG 8: IDENTITY CARD — 38 VALUES, 7 DOMAINS
# Type: Type 8 (Identity Card)
# Shows: Seven domain columns with values, inputs, key results.
#        Visual anchor for the paper.
# ================================================================

fig, ax = dark_fig(18, 14)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

# Title
ax.text(9, 13.3, 'HOWL-PHYS-38: PRECISION FRONTIER',
        fontsize=16, fontweight='bold', color=GOLD, ha='center')
ax.text(9, 12.7, '38 Derived Values %s 7 Domains %s 15 Measured Inputs %s 23 Surplus Outputs' % (u'\u00b7', u'\u00b7', u'\u00b7'),
        fontsize=11, color=SILVER, ha='center')
ax.axhline(y=12.3, xmin=0.03, xmax=0.97, color=GOLD, linewidth=1.5)

# Seven domain columns
domains_id = [
    ('QED', GOLD, 1.8, [
        ('%s%s = 137.036' % (u'\u03b1', u'\u207b\u00b9'), '0.007 ppb vs Rb'),
        ('R%s' % u'\u221e', '0.44 ppb'),
        ('a%s, %s%s' % (u'\u2080', u'\u03bc', u'\u2080'), '0.22 ppb'),
    ]),
    ('EW', CYAN, 4.5, [
        ('M_W (2 paths)', '195-402 ppm'),
        ('%s_Z = 2515' % u'\u0393', '0.81%'),
        ('R_l = 20.82', '0.27%'),
        ('N_gen = 3.0', 'exact'),
    ]),
    ('COSMO', BLUE, 7.2, [
        ('DM/b = 5.317', '725 ppm'),
        ('%s_b = 0.0490' % u'\u03a9', '727 ppm'),
        ('%s_DE = 0.690' % u'\u03a9', '0.20%'),
        ('%s%s = 5.9e-30' % (u'\u03c1', u'\u039b'), '0.15%'),
    ]),
    ('BBN', GREEN, 9.9, [
        ('D/H', '0.12%s' % u'\u03c3'),
        ('Y_p', '0.94%s' % u'\u03c3'),
        ('He-3', '0.36%s' % u'\u03c3'),
        ('Li-7', '2.96%s (problem)' % u'\u00d7'),
    ]),
    ('MUON', PURPLE, 12.2, [
        ('a_%s(SM)' % u'\u03bc', ''),
        ('= 116591741', ''),
        ('Anomaly', '6.5%s' % u'\u03c3'),
    ]),
    ('FLAVOR', ORANGE, 14.5, [
        ('V_ud (4%s4)' % u'\u00d7', '264 ppm'),
        ('CKM deficit', '0.83%s' % u'\u03c3'),
        ('4%s4 sum' % u'\u00d7', '1.00050'),
    ]),
    ('MASS', MAG, 16.5, [
        ('m_%s (Koide)' % u'\u03c4', '0.006%'),
        ('%s_QCD = 0' % u'\u03b8', 'exact'),
    ]),
]

for domain, color, x_pos, values in domains_id:
    ax.text(x_pos, 11.8, domain, fontsize=12, fontweight='bold', color=color, ha='center')
    ax.plot([x_pos - 1.0, x_pos + 1.0], [11.4, 11.4], '-', color=color, linewidth=1, alpha=0.5)
    for i, (val, miss) in enumerate(values):
        y = 10.7 - i * 0.85
        ax.text(x_pos, y, val, fontsize=8, color=WHITE, ha='center', fontfamily='monospace')
        if miss:
            ax.text(x_pos, y - 0.32, miss, fontsize=7, color=DIM, ha='center')

# Key integers
ax.text(4, 4.2, 'KEY INTEGERS', fontsize=11, fontweight='bold', color=ORANGE, ha='center')
ax.text(4, 3.5, '11 (YM) %s 13 (b%s_mod)\n(22/13)%s%s = 5.317' % (u'\u00b7', u'\u2082', u'\u00d7', u'\u03c0'),
        fontsize=10, color=ORANGE, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.8))

# Inputs
ax.text(13, 4.2, 'MEASURED INPUTS (15)', fontsize=11, fontweight='bold', color=MAG, ha='center')
ax.text(13, 3.5, 'a_e %s m_e %s M_Z %s sin%s%s_W %s m_t %s %s_s\n%s(M_Z) %s sin%s%s_eff %s G_F %s %s_DM %s H%s %s T_CMB\nm_%s %s %sr %s sin%s%s%s' % (
    u'\u00b7', u'\u00b7', u'\u00b7', u'\u00b2', u'\u03b8', u'\u00b7', u'\u00b7', u'\u03b1',
    u'\u03b1', u'\u00b7', u'\u00b2', u'\u03b8', u'\u00b7', u'\u00b7', u'\u03a9', u'\u00b7', u'\u2080', u'\u00b7',
    u'\u03bc', u'\u00b7', u'\u0394', u'\u00b7', u'\u00b2', u'\u03b8', u'\u2081\u2084'),
    fontsize=8, color=MAG, ha='center',
    bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG, alpha=0.8))

# Headline results
ax.text(3, 1.5, 'HEADLINES', fontsize=11, fontweight='bold', color=GOLD, ha='center')
results_text = ('%s at 12-digit Rb agreement %s M_W from 2 paths at 207 ppm\n'
                'Muon g-2 anomaly at 6.5%s %s Li-7 problem at 2.96%s %s CKM deficit at 0.83%s') % (
    u'\u03b1', u'\u00b7', u'\u03c3', u'\u00b7', u'\u00d7', u'\u00b7', u'\u03c3')
ax.text(9, 1.5, results_text,
        fontsize=9, color=GOLD, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

# Footer
ax.text(9, 0.5, '15 inputs %s 38 outputs %s 23 more outputs than inputs %s every output matches or reproduces a known anomaly' % (
    u'\u00b7', u'\u00b7', u'\u00b7'),
        fontsize=9, color=SILVER, ha='center', style='italic')

save(fig, 'phys38_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("PHYS-38 Diagrams Complete:")
print("  phys38_01_alpha_corrections.png")
print("  phys38_02_ew_convergence.png")
print("  phys38_03_precision_landscape.png")
print("  phys38_04_bbn_four_elements.png")
print("  phys38_05_correction_cascade.png")
print("  phys38_06_integer_map.png")
print("  phys38_07_muon_g2.png")
print("  phys38_08_identity_card.png")

                                                                  