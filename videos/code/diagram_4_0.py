#!/usr/bin/env python3
"""
RUM Video 4 Diagrams — What Unification Actually Gets You
20 figures covering fiber optics, radio, Q335 FFT, semiconductors,
medicine, climate, and the general principle.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================

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

def setup_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

print("Video 4 Diagrams — What Unification Gets You")
print("=" * 50)


# ================================================================
# V1: THE GENERAL PRINCIPLE — THE DERIVATION CHAIN
# Type: Progression/Sequence
# Shows: Gauge integers → couplings → atoms → materials → engineering
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(9, 8.5, 'The General Principle: Integers to Engineering',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

boxes = [
    (1.5, 'Gauge\nIntegers', GOLD, '3, 2, 1\n41/10, -19/6, -7'),
    (5, 'Fundamental\nCouplings', CYAN, r'$\alpha = 1/137$' + '\n' + r'$\alpha_s = 0.118$'),
    (8.5, 'Atomic\nStructure', GREEN, 'Si: Z=14\nO: Z=8\nC: Z=6'),
    (12, 'Material\nProperties', BLUE, 'Band gap\nRefractive index\nBond strength'),
    (15.5, 'Engineering\nPerformance', MAG, 'Bandwidth\nEfficiency\nDrug binding'),
]

for bx, title, color, content in boxes:
    rect = FancyBboxPatch((bx - 1.3, 3), 2.6, 3.5,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(bx, 5.8, title, color=color, fontsize=11,
            fontweight='bold', ha='center')
    ax.text(bx, 4.3, content, color=color, fontsize=8,
            ha='center', alpha=0.8)

# Arrows
for i in range(4):
    x1 = boxes[i][0] + 1.3
    x2 = boxes[i+1][0] - 1.3
    ax.annotate('', xy=(x2, 4.75), xytext=(x1, 4.75),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))
    labels = ['group\ntheory', 'quantum\nmechanics', 'solid state\nchemistry', 'applied\nphysics']
    ax.text((x1+x2)/2, 5.3, labels[i], color=DIM, fontsize=7,
            ha='center', style='italic')

ax.text(9, 1.5,
        'Every engineering problem depends on a material property.\n'
        'Every material property traces back to gauge integers.\n'
        'Every link uses known equations. No link requires new physics.',
        color=SILVER, fontsize=11, ha='center', style='italic')

ax.text(9, 0.5,
        'The only thing missing is the computation and the willingness to cross departmental walls.',
        color=GOLD, fontsize=11, ha='center', fontweight='bold')

save(fig, 'talk4_01_general_principle.png')


# ================================================================
# V2: FIBER OPTICS — THE BANDWIDTH GAP
# Type: Comparison Bar
# Shows: Current vs lab record vs theoretical limit
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Throughput (Tbps)')

categories = ['Current\nCommercial\nDWDM', 'Lab Record\n(2024)', 'Theoretical\nLimit\n(SMF)']
values = [100, 430, 600]
colors_b = [CYAN, GREEN, GOLD]

bars = ax.bar(range(3), values, color=colors_b, alpha=0.7,
              edgecolor=colors_b, linewidth=2, width=0.55)

for i, (v, c) in enumerate(zip(values, colors_b)):
    ax.text(i, v + 15, '%d Tbps' % v, color=c, fontsize=16,
            fontweight='bold', ha='center')

# Gap annotations
ax.annotate('', xy=(1, 430), xytext=(2, 600),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(1.8, 520, '170 Tbps\ngap', color=ORANGE, fontsize=12,
        fontweight='bold', ha='center')

ax.annotate('', xy=(0, 100), xytext=(2, 600),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=1.5, alpha=0.5))
ax.text(0.8, 380, '500 Tbps\ntotal gap', color=RED, fontsize=10,
        ha='center', alpha=0.7)

ax.set_xticks(range(3))
ax.set_xticklabels(categories, color=WHITE, fontsize=11)
ax.set_ylim(0, 700)

ax.text(1, 670, 'The gap exists because safety margins are set from empirical curve fitting,\n'
        'not from first-principles derivation of optical parameters.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.set_title('Fiber Optics: The Bandwidth Gap',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

save(fig, 'talk4_02_fiber_bandwidth.png')


# ================================================================
# V3: THE SELLMEIER CHAIN — INTEGERS TO REFRACTIVE INDEX
# Type: Progression/Sequence
# Shows: alpha → Si/O nuclear charges → bonds → Sellmeier → channel spacing
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(9, 8.5, 'The Sellmeier Chain: Integers to Refractive Index',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

chain = [
    (1.5, r'$\alpha = 1/137$', GOLD, 'Fine structure\nconstant'),
    (4.5, 'Si: Z=14\nO: Z=8', CYAN, 'Nuclear\ncharges'),
    (7.5, 'SiO' + r'$_2$' + '\nbond angles\npolarizability', GREEN, 'Molecular\nstructure'),
    (10.5, 'Sellmeier\ncoefficients\n(6 params)', BLUE, 'Bulk optical\nproperties'),
    (13.5, 'Refractive\nindex n(' + r'$\lambda$' + ')', ORANGE, 'Wavelength\ndependence'),
    (16.5, 'Channel\nspacing', MAG, 'DWDM\nengineering'),
]

for bx, text, color, subtitle in chain:
    rect = FancyBboxPatch((bx - 1.2, 3.5), 2.4, 3,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(bx, 5.5, text, color=color, fontsize=9,
            fontweight='bold', ha='center')
    ax.text(bx, 3.8, subtitle, color=color, fontsize=7,
            ha='center', alpha=0.7)

for i in range(5):
    x1 = chain[i][0] + 1.2
    x2 = chain[i+1][0] - 1.2
    ax.annotate('', xy=(x2, 5), xytext=(x1, 5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.8))

ax.text(9, 2.0,
        'Every link is known physics. Nobody has run the chain in exact arithmetic.\n'
        'Current Sellmeier coefficients: empirically fitted. Precision: limited by the fit.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.text(9, 1.0,
        'Derive them from integers ' + r'$\to$' + ' operate closer to true limits ' +
        r'$\to$' + ' more channels ' + r'$\to$' + ' more bandwidth.',
        color=GOLD, fontsize=11, ha='center', fontweight='bold')

save(fig, 'talk4_03_sellmeier_chain.png')


# ================================================================
# V4: DWDM CHANNEL PLAN — SAFETY MARGINS
# Type: Threshold/Region
# Shows: Channel spacing with margins vs theoretical minimum
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Wavelength (nm)', 'Power')

# Simulate DWDM channels
wavelengths = np.linspace(1530, 1565, 5000)
channels = np.linspace(1535, 1560, 40)
signal = np.zeros_like(wavelengths)

for ch in channels:
    signal += 0.8 * np.exp(-((wavelengths - ch) / 0.15)**2)

ax.fill_between(wavelengths, 0, signal, color=CYAN, alpha=0.3)
ax.plot(wavelengths, signal, color=CYAN, lw=1)

# Safety margin bands between channels
for ch in channels[:-1]:
    mid = ch + (channels[1] - channels[0]) / 2
    ax.axvspan(mid - 0.15, mid + 0.15, color=RED, alpha=0.08)

# Annotations
ax.text(1548, 0.9, 'Signal channels', color=CYAN, fontsize=11,
        fontweight='bold')
ax.text(1548, 0.75, 'Safety margins\n(conservative)', color=RED, fontsize=10)

# Theoretical limit annotation
ax.axhline(0.05, color=GOLD, lw=1.5, ls='--', alpha=0.5)
ax.text(1560, 0.08, 'Theoretical minimum\nchannel separation', color=GOLD,
        fontsize=9, ha='right')

ax.set_xlim(1530, 1565)
ax.set_ylim(0, 1.1)

ax.set_title('DWDM Channel Plan: Where Safety Margins Waste Bandwidth',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'talk4_04_dwdm_channels.png')


# ================================================================
# V5: 5G MARGINS — PERFORMANCE LEFT ON THE TABLE
# Type: Comparison Bar
# Shows: Four margins in 5G systems and their performance cost
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Margin (% of optimal)')

margins = [
    'Impedance\nmatching', 'Guard band\nspacing', 'PA\nbackoff', 'FFT\nprecision'
]
values_m = [5, 8, 3, 0.001]
colors_m = [RED, ORANGE, MAG, GREEN]
savings = ['+2% throughput', '+5% spectrum', '+1 dB range', 'enables 4096-QAM']

bars = ax.bar(range(4), values_m, color=colors_m, alpha=0.7,
              edgecolor=colors_m, linewidth=2, width=0.55)

for i, (v, c, s) in enumerate(zip(values_m, colors_m, savings)):
    if v > 0.01:
        ax.text(i, v + 0.3, '%.0f%%' % v if v > 0.01 else '%.3f%%' % v,
                color=c, fontsize=14, fontweight='bold', ha='center')
    else:
        ax.text(i, v + 0.3, '~0%\n(Q335)', color=c, fontsize=12,
                fontweight='bold', ha='center')
    ax.text(i, -1.0, s, color=GOLD, fontsize=9, ha='center')

ax.set_xticks(range(4))
ax.set_xticklabels(margins, color=WHITE, fontsize=11)
ax.set_ylim(-1.5, 12)

ax.axhline(0, color=DIM, lw=1, alpha=0.5)

ax.text(1.5, 11, 'Every margin is lost performance.\n'
        'Derive tighter values ' + r'$\to$' + ' operate closer to true limits ' +
        r'$\to$' + ' better performance on existing hardware.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.set_title('5G Systems: Performance Left on the Table',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'talk4_05_5g_margins.png')


# ================================================================
# V6: THE Q335 FFT — FLOAT VS INTEGER
# Type: Comparison Bar (side by side panels)
# Shows: Floating point pi vs Q335 pi in the FFT
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.3})
fig.patch.set_facecolor(BG)

# Left: Float FFT
ax1.set_facecolor(PAN)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
for spine in ax1.spines.values():
    spine.set_color(RED)
    spine.set_linewidth(2)

ax1.set_title('Standard FFT (Float64)', color=RED, fontsize=14,
              fontweight='bold', pad=10)

ax1.text(5, 8.5, r'$\pi$ = 3.141592653589793', color=RED, fontsize=12,
         ha='center')
ax1.text(5, 7.5, '15 digits', color=DIM, fontsize=10, ha='center')
ax1.text(5, 6.0, 'Twiddle factor:\n' + r'$e^{-2\pi i k/N}$' +
         '\ncomputed in float64\n' + r'$\pm 10^{-15}$ error per butterfly',
         color=RED, fontsize=10, ha='center')
ax1.text(5, 3.5, '4096-point FFT:\n' + r'$\sim 10^{-12}$ accumulated error',
         color=ORANGE, fontsize=11, ha='center', fontweight='bold')
ax1.text(5, 1.5, 'Limits QAM to 1024\n(10 bits/symbol)',
         color=DIM, fontsize=10, ha='center')

# Right: Q335 FFT
ax2.set_facecolor(PAN)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
for spine in ax2.spines.values():
    spine.set_color(GOLD)
    spine.set_linewidth(2)

ax2.set_title('Q335 FFT (Integer)', color=GOLD, fontsize=14,
              fontweight='bold', pad=10)

ax2.text(5, 8.5, r'$\pi_{Q335}$ = integer / $2^{335}$', color=GOLD,
         fontsize=12, ha='center')
ax2.text(5, 7.5, '100+ digits', color=GREEN, fontsize=10, ha='center')
ax2.text(5, 6.0, 'Twiddle factor:\n' + r'$e^{-2\pi i k/N}$' +
         '\ncomputed in exact integer\n' + r'$\pm 10^{-100}$ error per butterfly',
         color=GOLD, fontsize=10, ha='center')
ax2.text(5, 3.5, '4096-point FFT:\n' + r'$\sim 10^{-97}$ accumulated error',
         color=GREEN, fontsize=11, ha='center', fontweight='bold')
ax2.text(5, 1.5, 'Enables 4096-QAM\n(12 bits/symbol)\n+20% throughput',
         color=GOLD, fontsize=10, ha='center', fontweight='bold')

fig.text(0.5, 0.03,
         'Same algorithm. Same hardware. Different number system. 20% more throughput.',
         color=GOLD, fontsize=13, ha='center', fontweight='bold')

save(fig, 'talk4_06_q335_fft.png')


# ================================================================
# V7: QAM CONSTELLATION — 1024 VS 4096
# Type: Geometric Cross-Section (two panels)
# Shows: Denser constellation enabled by lower noise floor
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.25})
fig.patch.set_facecolor(BG)

for ax, qam, bits, color, title in [
    (ax1, 32, 10, CYAN, '1024-QAM (current)'),
    (ax2, 64, 12, GOLD, '4096-QAM (Q335 enables)')
]:
    setup_ax(ax, title, 'I', 'Q')
    grid = np.linspace(-1, 1, qam)
    for xi in grid:
        for yi in grid:
            ax.plot(xi, yi, '.', color=color, markersize=2, alpha=0.6)
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.text(0, -1.35, '%d bits/symbol' % bits, color=color,
            fontsize=12, ha='center', fontweight='bold')

fig.text(0.5, 0.02,
         'Denser constellation = more bits per symbol. '
         'Requires lower noise floor. Q335 eliminates arithmetic noise.',
         color=SILVER, fontsize=11, ha='center', style='italic')

save(fig, 'talk4_07_qam_constellation.png')


# ================================================================
# V8: Q335 FFT CHIP — SIZE AND COST
# Type: Identity Card
# Shows: The physical specifications of the Q335 FFT block
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(8, 9.5, 'Q335 FFT: Patent Specification',
        color=GOLD, fontsize=18, fontweight='bold', ha='center')

specs = [
    ('FFT size', '4096 points', CYAN),
    ('Twiddle table', '~335 KB (trivial for modern silicon)', CYAN),
    ('Arithmetic', 'Integer multiply + bit shift (no FPU)', GREEN),
    ('Die area', r'< 1 mm$^2$ at 5 nm', GREEN),
    ('Modem die fraction', '< 4%', GREEN),
    ('Error floor', r'$10^{-100}$ (vs $10^{-15}$ for float)', GOLD),
    ('QAM enabled', '4096-QAM (12 bits/symbol)', GOLD),
    ('Throughput gain', '+20% on same spectrum', GOLD),
    ('Prior art', 'None. Empty patent space above 64 bits.', MAG),
    ('Applicability', 'Every handset, router, base station, radar, satellite, audio', WHITE),
]

for i, (label, value, color) in enumerate(specs):
    y = 8.3 - i * 0.8
    ax.text(2, y, label + ':', color=SILVER, fontsize=11, ha='left')
    ax.text(8.5, y, value, color=color, fontsize=11, ha='left',
            fontweight='bold')

rect = FancyBboxPatch((1, 0.3), 14, 0.8,
                       boxstyle='round,pad=0.15',
                       facecolor=BG, edgecolor=GOLD, linewidth=2)
ax.add_patch(rect)
ax.text(8, 0.7, 'One building block, made exact, applicable everywhere.',
        color=GOLD, fontsize=13, ha='center', fontweight='bold')

save(fig, 'talk4_08_fft_chip.png')


# ================================================================
# V9: SEMICONDUCTOR — THE BAND GAP CHAIN
# Type: Progression/Sequence
# Shows: alpha → Z=14 → crystal → band gap → transistor
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(9, 8.5, 'The Band Gap Chain: Integers to Transistors',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

chain = [
    (2, r'$\alpha = 1/137$', GOLD, 'EM coupling'),
    (5.5, 'Si: Z = 14', CYAN, '14 protons\n14 electrons'),
    (9, 'Diamond\ncubic\nlattice', GREEN, 'a = 5.431 ' + r'$\AA$'),
    (12.5, 'Band gap\n1.12 eV', ORANGE, 'Current: DFT\n' + r'$\pm$ 10%'),
    (16, 'Every\ntransistor', MAG, '10' + r'$^{22}$' + ' on\nEarth'),
]

for bx, text, color, subtitle in chain:
    rect = FancyBboxPatch((bx - 1.3, 3.5), 2.6, 3,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(bx, 5.5, text, color=color, fontsize=10,
            fontweight='bold', ha='center')
    ax.text(bx, 3.8, subtitle, color=color, fontsize=8,
            ha='center', alpha=0.8)

for i in range(4):
    x1 = chain[i][0] + 1.3
    x2 = chain[i+1][0] - 1.3
    ax.annotate('', xy=(x2, 5), xytext=(x1, 5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.8))

ax.text(9, 1.5,
        'The equations are known. Solving them exactly for billions of electrons is the bottleneck.\n'
        'But the starting point \u2014 ' + r'$\alpha$' + ' to 12 digits \u2014 is already in place.',
        color=SILVER, fontsize=10, ha='center', style='italic')

save(fig, 'talk4_09_bandgap_chain.png')


# ================================================================
# V10: BAND GAP PRECISION — CURRENT VS NEEDED
# Type: Threshold/Region
# Shows: Current DFT accuracy vs measurement vs integer target
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Silicon band gap (eV)')

# Measured band
ax.axhspan(1.11, 1.13, color=GREEN, alpha=0.1)
ax.axhline(1.12, color=GREEN, lw=2, label='Measured: 1.12 eV')

# DFT range
ax.axhspan(0.5, 1.3, color=RED, alpha=0.04)
ax.text(0.3, 0.6, 'DFT range\n(LDA: 0.5 eV)', color=RED, fontsize=10)
ax.text(0.3, 1.25, 'DFT range\n(hybrid: 1.2 eV)', color=RED, fontsize=10)

# GW approximation
ax.axhspan(1.05, 1.20, color=CYAN, alpha=0.06)
ax.text(0.7, 1.15, 'GW approx\n(best theory)', color=CYAN, fontsize=10)

# Integer target
ax.plot(0.5, 1.12, '*', color=GOLD, markersize=20, zorder=6)
ax.text(0.55, 1.14, 'Integer target:\nderive from Z=14 + ' + r'$\alpha$',
        color=GOLD, fontsize=10, fontweight='bold')

ax.set_xlim(0, 1)
ax.set_ylim(0.3, 1.4)
ax.set_xticks([])

ax.set_title('Silicon Band Gap: Current Theory vs Integer Target',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='lower right')

save(fig, 'talk4_10_bandgap_precision.png')


# ================================================================
# V11: MEDICINE — THE DRUG DESIGN PIPELINE
# Type: Progression/Sequence
# Shows: Current pipeline: 10-15 years, $2B, 90% failure
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(9, 8.5, 'Drug Design: The Current Pipeline',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

stages = [
    (2, 'Target\nIdentification', GREEN, '2 years'),
    (5.5, 'Lead\nOptimization', CYAN, '3 years'),
    (9, 'Preclinical\nTrials', ORANGE, '2 years'),
    (12.5, 'Clinical\nTrials\n(Phase I-III)', RED, '6 years'),
    (16, 'Approval', GOLD, '1 year'),
]

for bx, text, color, duration in stages:
    rect = FancyBboxPatch((bx - 1.3, 4), 2.6, 2.5,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(bx, 5.8, text, color=color, fontsize=10,
            fontweight='bold', ha='center')
    ax.text(bx, 4.3, duration, color=color, fontsize=9, ha='center')

for i in range(4):
    x1 = stages[i][0] + 1.3
    x2 = stages[i+1][0] - 1.3
    ax.annotate('', xy=(x2, 5.2), xytext=(x1, 5.2),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

# Failure annotations
ax.text(9, 3.2, '90% failure rate', color=RED, fontsize=16,
        fontweight='bold', ha='center')
ax.text(9, 2.4, '10-15 years per drug.  $1-2 billion per approval.',
        color=SILVER, fontsize=12, ha='center')
ax.text(9, 1.5,
        'The bottleneck: predicting binding. Current accuracy: 70%.\n'
        'The 30% error comes from fitted parameters in force fields \u2014 '
        'not derived from integers.',
        color=ORANGE, fontsize=10, ha='center', style='italic')

save(fig, 'talk4_11_drug_pipeline.png')


# ================================================================
# V12: THE FORCE FIELD CHAIN — INTEGERS TO BINDING
# Type: Progression/Sequence
# Shows: alpha → C,N,O,H,S charges → bonds → force fields → binding
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(9, 8.5, 'The Force Field Chain: Five Integers to Drug Binding',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

chain = [
    (1.5, r'$\alpha = 1/137$', GOLD, 'EM\ncoupling'),
    (4.2, 'C:6  N:7\nO:8  H:1\nS:16', CYAN, 'Five nuclear\ncharges'),
    (7, 'Electronic\nstructure\n(QM)', GREEN, 'Orbitals\npolarizability'),
    (9.8, 'Lennard-Jones\npartial charges\ntorsion barriers', ORANGE,
     'Force field\nparameters'),
    (12.6, 'Protein\nfolding', MAG, 'Molecular\ndynamics'),
    (15.5, 'Drug\nbinding\nprediction', RED, '70% ' + r'$\to$' + ' ?\naccuracy'),
]

for bx, text, color, subtitle in chain:
    rect = FancyBboxPatch((bx - 1.2, 3.5), 2.4, 3,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(bx, 5.5, text, color=color, fontsize=9,
            fontweight='bold', ha='center')
    ax.text(bx, 3.8, subtitle, color=color, fontsize=7,
            ha='center', alpha=0.8)

for i in range(5):
    x1 = chain[i][0] + 1.2
    x2 = chain[i+1][0] - 1.2
    ax.annotate('', xy=(x2, 5), xytext=(x1, 5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

ax.text(9, 2.0,
        'Five integers determine everything about how proteins fold and drugs bind.\n'
        'The endpoint is decades away. Every step that improves saves billions in failed trials.',
        color=SILVER, fontsize=10, ha='center', style='italic')

# Highlight fitted vs derived
ax.text(9.8, 2.8, 'Currently: FITTED\nTarget: DERIVED',
        color=ORANGE, fontsize=10, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE))

save(fig, 'talk4_12_forcefield_chain.png')


# ================================================================
# V13: THE FITTED PARAMETERS — WHAT'S NOT DERIVED
# Type: Comparison Bar
# Shows: Three fitted parameters and their error margins
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Typical uncertainty (%)')

params = ['Lennard-Jones\nwell depth\n' + r'$\epsilon$',
          'Partial\ncharges\nq',
          'Torsion\nbarriers\n' + r'$V_n$']
uncertainties = [15, 10, 20]
colors_p = [RED, ORANGE, MAG]

bars = ax.bar(range(3), uncertainties, color=colors_p, alpha=0.7,
              edgecolor=colors_p, linewidth=2, width=0.55)

for i, (v, c) in enumerate(zip(uncertainties, colors_p)):
    ax.text(i, v + 0.8, '%d%%' % v, color=c, fontsize=16,
            fontweight='bold', ha='center')

ax.text(1, 25, 'All fitted, not derived. All trace back to ' + r'$\alpha$' +
        ' and nuclear charges.',
        color=SILVER, fontsize=11, ha='center', style='italic')

ax.set_xticks(range(3))
ax.set_xticklabels(params, color=WHITE, fontsize=10)
ax.set_ylim(0, 28)

ax.set_title('Molecular Force Field Parameters: Fitted, Not Derived',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'talk4_13_fitted_params.png')


# ================================================================
# V14: CLIMATE — THE CO2 CHAIN
# Type: Progression/Sequence
# Shows: alpha → C:6, O:8 → CO2 bonds → vibrational spectrum → greenhouse
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(9, 8.5, 'The CO' + r'$_2$' + ' Chain: Two Integers to the Greenhouse Effect',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

chain = [
    (2, r'$\alpha = 1/137$', GOLD, 'EM coupling'),
    (5, 'C: Z=6\nO: Z=8', CYAN, 'Two nuclear\ncharges'),
    (8, 'O=C=O\nbond angle\nbond strength', GREEN, 'Molecular\nstructure'),
    (11, 'Vibrational\n& rotational\nspectrum', ORANGE, 'IR absorption\nbands'),
    (14, 'Greenhouse\neffect', RED, 'How much IR\nthe atmosphere\ntraps'),
]

for bx, text, color, subtitle in chain:
    rect = FancyBboxPatch((bx - 1.3, 3.5), 2.6, 3,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(bx, 5.5, text, color=color, fontsize=10,
            fontweight='bold', ha='center')
    ax.text(bx, 3.8, subtitle, color=color, fontsize=8,
            ha='center', alpha=0.8)

for i in range(4):
    x1 = chain[i][0] + 1.3
    x2 = chain[i+1][0] - 1.3
    ax.annotate('', xy=(x2, 5), xytext=(x1, 5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.8))

ax.text(9, 2.0,
        'CO' + r'$_2$' + ' is three atoms. The many-body problem is manageable.\n'
        'This is one of the nearest targets: short chain, known physics, high-precision data to compare against.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.text(9, 1.0,
        'Move ' + r'$\alpha$' + ' by 10% and CO' + r'$_2$' +
        ' might not absorb infrared at all.',
        color=GOLD, fontsize=11, ha='center', fontweight='bold')

save(fig, 'talk4_14_co2_chain.png')


# ================================================================
# V15: CO2 ABSORPTION SPECTRUM
# Type: Running/Convergence
# Shows: The IR absorption bands of CO2 — where the greenhouse lives
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Wavelength (' + r'$\mu$' + 'm)', 'Absorption')

# Simulated CO2 absorption bands
wavelength = np.linspace(2, 20, 2000)
absorption = np.zeros_like(wavelength)

# 4.3 micron band (asymmetric stretch)
absorption += 0.95 * np.exp(-((wavelength - 4.3) / 0.3)**2)
# 15 micron band (bending mode) — the big one
absorption += 0.85 * np.exp(-((wavelength - 15) / 1.5)**2)
# 2.7 micron band (combination)
absorption += 0.3 * np.exp(-((wavelength - 2.7) / 0.15)**2)

ax.fill_between(wavelength, 0, absorption, color=RED, alpha=0.3)
ax.plot(wavelength, absorption, color=RED, lw=2)

# Band labels
ax.annotate('4.3 ' + r'$\mu$' + 'm\nasymmetric stretch',
            xy=(4.3, 0.95), xytext=(6, 0.85),
            color=ORANGE, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

ax.annotate('15 ' + r'$\mu$' + 'm\nbending mode\n(the greenhouse band)',
            xy=(15, 0.85), xytext=(11, 0.65),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Earth's thermal emission window
ax.axvspan(8, 13, color=CYAN, alpha=0.04)
ax.text(10.5, 0.15, 'Earth\'s thermal\nemission window', color=CYAN,
        fontsize=9, ha='center', style='italic')

ax.set_xlim(2, 20)
ax.set_ylim(0, 1.1)

ax.set_title('CO' + r'$_2$' + ' Absorption Spectrum: Where the Greenhouse Effect Lives',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

ax.text(11, 1.0,
        'These bands are determined by C:6 and O:8.\n'
        'Derivable from ' + r'$\alpha$' + ' and two integers.',
        color=SILVER, fontsize=10, ha='center', style='italic')

save(fig, 'talk4_15_co2_spectrum.png')


# ================================================================
# V16: WHAT CHANGES FOR ORDINARY PEOPLE
# Type: Connection/Integer Map
# Shows: Mystery → understanding for four concepts
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(9, 9.5, 'Understanding Replaces Mystery',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

mysteries = [
    ('Dark matter', 'Unknown particle\nweighs the galaxy', RED,
     '(22/13)' + r'$\pi$' + ' = 5.317\nInteger ratio matches\nsatellite at 725 ppm', GREEN),
    ('Cosmological\nconstant', 'Worst prediction\nin physics\n(10' + r'$^{120}$' + r'$\times$' + ' wrong)', RED,
     'Ground state reading\nof outermost boundary.\nLarger = lower.', GREEN),
    ('Four forces', 'Why four?\nWhy different?', RED,
     'Four readings of one thing.\nSame instrument,\ndifferent depths.', GREEN),
    ('Flatness', 'Why is the universe\nexactly flat?\nFine-tuning?', RED,
     'You\'re inside.\nInsides read flat.\nSame as Earth\'s surface.', GREEN),
]

for i, (topic, mystery, mc, understanding, uc) in enumerate(mysteries):
    y = 7.5 - i * 2.0

    # Mystery box
    rect_m = FancyBboxPatch((0.5, y - 0.7), 4, 1.4,
                             boxstyle='round,pad=0.15',
                             facecolor=BG, edgecolor=mc, linewidth=1.5)
    ax.add_patch(rect_m)
    ax.text(2.5, y, mystery, color=mc, fontsize=8, ha='center', va='center')

    # Topic
    ax.text(5.5, y, topic, color=WHITE, fontsize=10, fontweight='bold',
            ha='center', va='center')

    # Arrow
    ax.annotate('', xy=(8, y), xytext=(7, y),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

    # Understanding box
    rect_u = FancyBboxPatch((8.5, y - 0.7), 5, 1.4,
                             boxstyle='round,pad=0.15',
                             facecolor=BG, edgecolor=uc, linewidth=1.5)
    ax.add_patch(rect_u)
    ax.text(11, y, understanding, color=uc, fontsize=8,
            ha='center', va='center')

# Labels
ax.text(2.5, 9, 'Mystery', color=RED, fontsize=13, fontweight='bold',
        ha='center')
ax.text(11, 9, 'Understanding', color=GREEN, fontsize=13,
        fontweight='bold', ha='center')

save(fig, 'talk4_16_mystery_understanding.png')


# ================================================================
# V17: THE PROMISE AND THE HONEST LIMIT
# Type: Comparison Bar
# Shows: Computed chains (green) vs future chains (gray)
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', '')

chains = [
    ('Integers ' + r'$\to$' + ' deuterium', 'COMPUTED', GREEN, '0.12' + r'$\sigma$'),
    ('Electron ' + r'$\to$' + ' hydrogen freq', 'COMPUTED', GREEN, '11 digits'),
    ('Integers ' + r'$\to$' + ' sin' + r'$^2\theta_W$', 'COMPUTED', GREEN, '12 ppm'),
    ('Integers ' + r'$\to$' + ' W mass', 'COMPUTED', GREEN, '195 ppm'),
    ('Integers ' + r'$\to$' + ' DM ratio', 'COMPUTED', GREEN, '725 ppm'),
    (r'$\alpha$' + ' ' + r'$\to$' + ' Si band gap', 'FUTURE', DIM, 'years'),
    (r'$\alpha$' + ' ' + r'$\to$' + ' CO' + r'$_2$' + ' spectrum', 'FUTURE', DIM, 'years'),
    (r'$\alpha$' + ' ' + r'$\to$' + ' protein folding', 'FUTURE', DIM, 'decades'),
]

for i, (chain, status, color, precision) in enumerate(chains):
    y = len(chains) - 1 - i
    width = 10 if status == 'COMPUTED' else 4
    ax.barh(y, width, height=0.7, color=color, alpha=0.5 if status == 'COMPUTED' else 0.2,
            edgecolor=color, linewidth=1.5)
    ax.text(-0.2, y, chain, color=WHITE, fontsize=10, ha='right', va='center')
    ax.text(width + 0.3, y, precision, color=color, fontsize=10,
            va='center', fontweight='bold')
    ax.text(width / 2, y, status, color=BG if status == 'COMPUTED' else DIM,
            fontsize=9, ha='center', va='center', fontweight='bold')

ax.set_xlim(-8, 14)
ax.set_ylim(-0.5, len(chains))
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('The Promise and the Honest Limit',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

ax.text(5, -0.3, 'Every chain that has been computed works. The walls are departmental, not physical.',
        color=GOLD, fontsize=11, ha='center', style='italic')

save(fig, 'talk4_17_promise_limit.png')


# ================================================================
# V18: THE FOUR INDUSTRIES — SAME PRINCIPLE
# Type: Connection/Integer Map
# Shows: Same pattern applied to fiber, radio, semicond, medicine
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(9, 11.5, 'Same Principle, Four Industries',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

# Central principle
rect_center = FancyBboxPatch((5.5, 6.5), 7, 2,
                              boxstyle='round,pad=0.2',
                              facecolor=BG, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(rect_center)
ax.text(9, 7.5, 'Derive tighter values for empirical parameters\n'
        + r'$\to$' + ' operate closer to true limits\n'
        + r'$\to$' + ' better performance on existing hardware',
        color=GOLD, fontsize=10, ha='center', fontweight='bold')

industries = [
    (2, 3, 'FIBER\nOPTICS', CYAN, 'Sellmeier\ncoeffs', '+170 Tbps\npotential'),
    (7, 3, 'WIRELESS', GREEN, 'Impedance\nmatching', '+20%\nthroughput'),
    (12, 3, 'SEMICON-\nDUCTOR', ORANGE, 'Band gap\nprecision', 'Better\ndesign'),
    (17, 3, 'MEDICINE', MAG, 'Force field\nparams', 'Faster\ndrug design'),
]

for ix, iy, title, color, param, benefit in industries:
    rect = FancyBboxPatch((ix - 1.8, iy - 1.5), 3.6, 3,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(ix, iy + 0.8, title, color=color, fontsize=11,
            fontweight='bold', ha='center')
    ax.text(ix, iy - 0.2, param, color=color, fontsize=8, ha='center')
    ax.text(ix, iy - 1.0, benefit, color=GOLD, fontsize=8,
            ha='center', fontweight='bold')

    ax.plot([ix, ix], [6.5, iy + 1.5], color=color, lw=1.5, alpha=0.5)

save(fig, 'talk4_18_four_industries.png')


# ================================================================
# V19: EDUCATION — ONE PRINCIPLE, FOUR READINGS
# Type: Geometric Cross-Section
# Shows: One gauge with four reading depths vs four separate textbooks
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.3})
fig.patch.set_facecolor(BG)

# Left: four textbooks
ax1.set_facecolor(PAN)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Current: Four Subjects', color=RED, fontsize=14,
              fontweight='bold', pad=10)

books = [
    (2.5, 7.5, 'ELECTRO-\nMAGNETISM', BLUE),
    (7.5, 7.5, 'WEAK\nFORCE', GREEN),
    (2.5, 3, 'STRONG\nFORCE', RED),
    (7.5, 3, 'GRAVITY', PURPLE),
]
for bx, by, title, color in books:
    rect = FancyBboxPatch((bx - 2, by - 1.5), 4, 3,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax1.add_patch(rect)
    ax1.text(bx, by, title, color=color, fontsize=10,
             fontweight='bold', ha='center', va='center')

ax1.text(5, 0.5, 'Four departments.\nFour professors.\nFour exams.',
         color=DIM, fontsize=10, ha='center')

# Right: one gauge
ax2.set_facecolor(PAN)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('RUM: One Principle, Four Readings', color=GOLD, fontsize=14,
              fontweight='bold', pad=10)

# Vertical gauge
ax2.plot([5, 5], [1, 9], color=WHITE, lw=3)
readings = [
    (8.5, '1/42 (unification)', GOLD),
    (6.5, '1/30 (weak)', GREEN),
    (4.5, '1/137 (EM)', BLUE),
    (2.5, '~1 (confinement)', RED),
]
for ry, label, color in readings:
    ax2.plot([4.5, 5.5], [ry, ry], color=color, lw=2.5)
    ax2.plot(5, ry, 'o', color=color, markersize=10,
             edgecolors=WHITE, linewidth=1.5, zorder=5)
    ax2.text(6, ry, label, color=color, fontsize=10,
             fontweight='bold', va='center')

ax2.text(3.5, 5, 'Same\ninstrument.\nDifferent\ndepths.', color=SILVER,
         fontsize=10, ha='center', style='italic')

ax2.text(5, 0.5, 'One principle.\nOne vocabulary.\nOne exam.',
         color=GOLD, fontsize=10, ha='center', fontweight='bold')

save(fig, 'talk4_19_education.png')


# ================================================================
# V20: CLOSE — THE DISCOVERY IS DONE, COMPUTATION REMAINS
# Type: Identity Card
# Shows: Summary of what's computed, what's not, what's next
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(8, 9.5, 'The Discovery Is Done. The Computation Remains.',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

# Three columns
sections = [
    (3, 'COMPUTED', GREEN, [
        'Integers ' + r'$\to$' + ' deuterium',
        'Electron ' + r'$\to$' + ' H frequency',
        'Integers ' + r'$\to$' + ' sin' + r'$^2\theta_W$',
        'Integers ' + r'$\to$' + ' W mass',
        'Integers ' + r'$\to$' + ' DM ratio',
        'All 253 comparisons',
    ]),
    (8, 'NOT YET', ORANGE, [
        'Integers ' + r'$\to$' + ' band gap',
        r'$\alpha$' + ' ' + r'$\to$' + ' CO' + r'$_2$' + ' spectrum',
        'Integers ' + r'$\to$' + ' Sellmeier',
        'Integers ' + r'$\to$' + ' force fields',
        'Q335 FFT in silicon',
        'Nuclear clock test',
    ]),
    (13, 'PREDICTION', MAG, [
        'Cabibbo Doublet particle',
        'Proton decay (Hyper-K)',
        'Clock sector splitting',
        'Q335 enables 4096-QAM',
        'Tighter fiber margins',
        'Better drug binding',
    ]),
]

for sx, title, color, items in sections:
    ax.text(sx, 8.5, title, color=color, fontsize=14,
            fontweight='bold', ha='center')
    ax.plot([sx - 2, sx + 2], [8.2, 8.2], color=color, lw=2)
    for i, item in enumerate(items):
        y = 7.5 - i * 0.9
        ax.text(sx, y, item, color=color, fontsize=9, ha='center',
                alpha=0.9)

# Bottom
rect = FancyBboxPatch((2, 0.3), 12, 1.2,
                       boxstyle='round,pad=0.15',
                       facecolor=BG, edgecolor=GOLD, linewidth=2)
ax.add_patch(rect)
ax.text(8, 0.9,
        'Unification connects the gauge group to your internet bandwidth '
        'and the price of your medication.\n'
        'The chains are visible. The links remain to be computed.',
        color=GOLD, fontsize=10, ha='center')

save(fig, 'talk4_20_discovery_done.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 20 figures saved:")
for i in range(1, 21):
    print("  talk4_%02d_*.png" % i)
print("=" * 50)
