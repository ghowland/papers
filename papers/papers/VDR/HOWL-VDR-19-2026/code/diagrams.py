
#!/usr/bin/env python3
"""
VDR-14 Diagrams — You Are Here: Complete System Specification
8 figures covering arithmetic foundations, convergence, architecture, and validation.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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


def style_ax(ax, title='', xlabel='', ylabel='', title_size=15):
    ax.set_facecolor(PAN)
    if title:
        ax.set_title(title, color=GOLD, fontsize=title_size, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=12)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=12)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)


# ================================================================
# FIG 1: DENOMINATOR GROWTH — FLAT FRACTION VS Q335 TREE
# Type: Running/Convergence Chart
# Shows: Exponential vs linear growth curves diverging after crossover.
#        The SHAPE of the divergence is the argument for tree-based
#        representation. Impossible to convey in text.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax,
         title='Denominator Growth: Flat Fraction vs Q335 Remainder Tree',
         xlabel='Logistic Map Steps (r = 4)',
         ylabel='Representation Size (digits, log scale)')

steps = np.array([0, 5, 10, 15, 20, 25, 30])
flat_digits = np.array([1, 31, 980, 31000, 990000, 31000000, 1e9])
q335_digits = np.array([102, 1020, 2040, 3060, 4080, 5100, 6120])

ax.semilogy(steps, flat_digits, color=RED, linewidth=2.5, marker='o',
            markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='Flat Fraction denominator', zorder=5)
ax.semilogy(steps, q335_digits, color=GREEN, linewidth=2.5, marker='s',
            markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='Q335 tree (structured)', zorder=5)

# Crossover region
ax.axvspan(9, 11, alpha=0.08, color=GOLD)
ax.annotate('Crossover\n~step 10',
            xy=(10, 1500), xytext=(13, 300),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            ha='left', va='center')

# Compression annotations
ax.annotate('163,000x more\ncompact at step 30',
            xy=(30, 6120), xytext=(25, 40000),
            color=GREEN, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5),
            ha='center', va='bottom')

ax.annotate('~10\u2079 digits\n(impractical)',
            xy=(30, 1e9), xytext=(26.5, 3e7),
            color=RED, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            ha='center', va='top')

# Same exact value note
ax.text(15, 8, 'Both representations hold the SAME exact value',
        color=SILVER, fontsize=9, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.9))

ax.set_xlim(-1.5, 32)
ax.set_ylim(0.5, 5e9)
ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.08, color=DIM)

save(fig, 'vdr14_01_denom_growth.png')


# ================================================================
# FIG 2: HILBERT MATRIX FLOAT ERROR ESCALATION
# Type: Running/Convergence Chart
# Shows: Float error escalating from 10^-16 to catastrophic while
#        VDR stays at exact zero. The SHAPE of the escalation shows
#        why condition number is irrelevant for exact arithmetic.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax,
         title='Hilbert Matrix Inverse: Float Error vs Matrix Size',
         xlabel='Matrix Size n',
         ylabel='Max Off-Diagonal Residual (H \u00d7 H\u207b\u00b9 \u2212 I)')

sizes = np.array([3, 4, 5, 6, 8, 10, 20, 30])
float_errors = np.array([1e-16, 1e-13, 1e-9, 1e-4, 1e4, 1e41, 1e170, 1e400])
# Cap for display
float_display = np.clip(float_errors, 1e-18, 1e50)

# Float curve
ax.semilogy(sizes, float_display, color=RED, linewidth=2.5, marker='D',
            markersize=11, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='Float64 residual', zorder=5)

# VDR line at zero (shown as a band at the bottom)
ax.axhspan(1e-19, 1e-17, alpha=0.15, color=GREEN, zorder=2)
ax.text(16.5, 3e-18, 'VDR: exactly zero for ALL sizes',
        color=GREEN, fontsize=11, fontweight='bold', ha='center', va='center')

# Threshold regions
ax.axhspan(1e-2, 1e50, alpha=0.04, color=RED)
ax.text(28, 1e20, 'CATASTROPHIC', color=RED, fontsize=12,
        fontweight='bold', ha='center', va='center', alpha=0.6)

ax.axhspan(1e-10, 1e-2, alpha=0.04, color=ORANGE)
ax.text(28, 1e-6, 'UNRELIABLE', color=ORANGE, fontsize=10,
        fontweight='bold', ha='center', va='center', alpha=0.6)

ax.axhspan(1e-18, 1e-10, alpha=0.04, color=CYAN)
ax.text(28, 1e-14, 'Acceptable', color=CYAN, fontsize=10,
        ha='center', va='center', alpha=0.6)

# Key annotations
ax.annotate('H\u2085: 10\u207b\u2079',
            xy=(5, 1e-9), xytext=(7, 1e-7),
            color=ORANGE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

ax.annotate('H\u2088: wrong SIGN\npossible (10\u2074)',
            xy=(8, 1e4), xytext=(11, 1e8),
            color=RED, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.annotate('H\u2081\u2080: meaningless',
            xy=(10, 1e41), xytext=(14, 1e38),
            color=RED, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# Det numerator note
ax.text(5, 1e45, 'Hilbert det numerator is always 1\nVDR computes H\u2083\u2080 routinely',
        color=GOLD, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9),
        ha='center', va='center')

ax.set_xlim(1, 32)
ax.set_ylim(1e-19, 1e50)
ax.legend(loc='lower right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.08, color=DIM)

save(fig, 'vdr14_02_hilbert_error.png')


# ================================================================
# FIG 3: FUNCTIONAL REMAINDER CONVERGENCE RATES
# Type: Running/Convergence Chart
# Shows: Multiple convergence curves showing why exp needs ~45 steps
#        for 100 digits but ln needs ~340. The SPREAD between curves
#        is the insight — depth requirements differ by 40x.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax,
         title='Functional Remainder Convergence: Depth to 100 Correct Digits',
         xlabel='Evaluation Depth (terms or iterations)',
         ylabel='Correct Decimal Digits (log scale)')

depths = np.arange(1, 51)

# Super-geometric: exp, sin, cos — roughly n*log(n)/log(10) digits
exp_digits = np.minimum(np.cumsum(np.log10(np.maximum(depths, 1.5))), 120)

# Geometric: ln at x=1 — roughly n*log10(2) digits (slow)
ln_digits = depths * 0.301

# Quadratic: Newton sqrt — digits double each step
newton_digits = np.minimum(1.5 * 2**depths, 150)
newton_depths = np.arange(1, 12)
newton_vals = np.minimum(1.5 * 2**newton_depths, 150)

# Geometric: arctan at x~1 — roughly n*log10(1) very slow
arctan_digits = depths * 0.29

ax.semilogy(depths, exp_digits, color=CYAN, linewidth=2.5,
            label='exp, sin, cos (super-geometric)', zorder=5)
ax.semilogy(depths, ln_digits, color=ORANGE, linewidth=2.5,
            label='ln(1+x) at x=1 (geometric, slow)', zorder=5)
ax.semilogy(depths, arctan_digits, color=MAG, linewidth=2.5, linestyle='--',
            label='arctan(x) at x=1 (geometric)', zorder=5)
ax.semilogy(newton_depths, newton_vals, color=GREEN, linewidth=2.5,
            marker='o', markersize=9, markeredgecolor=WHITE,
            markeredgewidth=1.5,
            label='Newton \u221an (quadratic, digits double)', zorder=6)

# 100-digit target line
ax.axhline(y=100, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.7, zorder=3)
ax.text(48, 115, '100-digit target', color=GOLD, fontsize=10,
        ha='right', va='bottom')

# Depth annotations
ax.annotate('Newton: ~8 steps',
            xy=(8, 100), xytext=(14, 70),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

ax.annotate('exp/sin/cos:\n~35-45 terms',
            xy=(40, 100), xytext=(42, 30),
            color=CYAN, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax.annotate('ln: ~340 terms\n(off chart \u2192)',
            xy=(50, 15), xytext=(38, 6),
            color=ORANGE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

# Note about Borwein
ax.text(25, 2.5, 'Borwein \u03b6(s): 210 terms for any s \u2265 2\n(universal 3\u207b\u207f convergence)',
        color=PURPLE, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=PURPLE, alpha=0.9),
        ha='center', va='center')

ax.set_xlim(0, 52)
ax.set_ylim(1, 200)
ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=9, framealpha=0.9)
ax.grid(True, alpha=0.08, color=DIM)

save(fig, 'vdr14_03_convergence_rates.png')


# ================================================================
# FIG 4: FIVE-STAGE BUILD CAPACITY PROGRESSION
# Type: Threshold/Region Chart
# Shows: Three curves rising through five shaded stage regions.
#        Shows where each capability threshold is crossed and that
#        each stage produces a complete testable system.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax,
         title='Five-Stage Implementation: Cumulative Capacity',
         xlabel='Implementation Stage',
         ylabel='Cumulative Count')

stages = [1, 2, 3, 4, 5]
stage_names = ['S1: Toy\nLifecycle', 'S2: Upgraded\nToy', 'S3: Capacity\nBuilding',
               'S4: Full\nIntegration', 'S5: Production']

builtins = [161, 300, 400, 437, 448]
tests = [150, 350, 600, 900, 1250]
modules = [24, 37, 49, 58, 65]

# Scale modules to be visible alongside others
modules_scaled = [m * 4 for m in modules]  # just for visibility on same axis

# Stage background shading
stage_colors = [BLUE, CYAN, GREEN, ORANGE, GOLD]
stage_bounds = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
for i in range(5):
    ax.axvspan(stage_bounds[i], stage_bounds[i + 1], alpha=0.06, color=stage_colors[i])

ax.plot(stages, builtins, color=CYAN, linewidth=2.5, marker='s',
        markersize=11, markeredgecolor=WHITE, markeredgewidth=1.5,
        label='Builtins active', zorder=5)
ax.plot(stages, tests, color=GREEN, linewidth=2.5, marker='o',
        markersize=11, markeredgecolor=WHITE, markeredgewidth=1.5,
        label='Cumulative tests', zorder=5)
ax.plot(stages, modules_scaled, color=ORANGE, linewidth=2.5, marker='^',
        markersize=11, markeredgecolor=WHITE, markeredgewidth=1.5,
        label='Modules (\u00d74 for scale)', zorder=5)

# Data labels
for i, s in enumerate(stages):
    ax.text(s, builtins[i] + 40, str(builtins[i]),
            color=CYAN, fontsize=10, ha='center', va='bottom', fontweight='bold')
    ax.text(s, tests[i] + 40, str(tests[i]),
            color=GREEN, fontsize=10, ha='center', va='bottom', fontweight='bold')
    ax.text(s, modules_scaled[i] - 50, '%d mod' % modules[i],
            color=ORANGE, fontsize=9, ha='center', va='top')

# Stage labels
for i, s in enumerate(stages):
    ax.text(s, -80, stage_names[i], color=stage_colors[i], fontsize=8,
            ha='center', va='top', fontweight='bold')

# Key thresholds
ax.axhline(y=448, color=CYAN, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5.35, 448, '448 builtins', color=CYAN, fontsize=8, va='center')

ax.axhline(y=1250, color=GREEN, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5.35, 1250, '1250 tests', color=GREEN, fontsize=8, va='center')

# Note
ax.text(3, 1150, 'Each stage: complete testable system\nAll prior tests must still pass',
        color=GOLD, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9),
        ha='center', va='center')

ax.set_xlim(0.3, 5.7)
ax.set_ylim(-120, 1400)
ax.set_xticks(stages)
ax.set_xticklabels(['1', '2', '3', '4', '5'])
ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.08, color=DIM, axis='y')

save(fig, 'vdr14_04_build_progression.png')


# ================================================================
# FIG 5: PHYSICAL COMPUTATION DOMAIN LANDSCAPE
# Type: Scale/Landscape Diagram
# Shows: 14 physical domains placed on a log-scale energy/size axis.
#        Shows the SPAN of exact computation from subatomic to planetary.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
style_ax(ax, title='Physical Domains with Exact VDR Arithmetic')
ax.axis('off')

# Vertical log-scale axis
ax_y = fig.add_axes([0.12, 0.08, 0.04, 0.82])
ax_y.set_facecolor(BG)
ax_y.set_ylim(-18, 25)
ax_y.set_xlim(0, 1)
ax_y.set_ylabel('Characteristic Scale (log\u2081\u2080 meters)', color=SILVER,
                fontsize=11, labelpad=15)
ax_y.tick_params(left=True, labelleft=True, right=False, bottom=False,
                 labelbottom=False, colors=DIM, labelsize=9)
for spine in ax_y.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax_y.spines['bottom'].set_visible(False)
ax_y.spines['top'].set_visible(False)
ax_y.spines['right'].set_visible(False)

# Scale landmarks
landmarks = [
    (-15, 'Planck length', DIM),
    (-10, 'Nuclear', MAG),
    (-8, 'Atomic', CYAN),
    (-3, 'Crystal lattice', PURPLE),
    (0, 'Human scale', SILVER),
    (7, 'Planetary', GREEN),
    (21, 'Cosmological', BLUE),
]
for pos, label, color in landmarks:
    ax_y.axhline(y=pos, color=color, linewidth=0.8, alpha=0.3, xmin=0, xmax=1)
    ax_y.text(1.1, pos, label, color=color, fontsize=8, va='center',
              transform=ax_y.get_yaxis_transform(), clip_on=False)

# Domain entries: (y_position, name, mechanism, color)
domains = [
    (-14, 'QED coefficients', 'Q335 add+multiply', MAG),
    (-13, 'Quantum 2\u00d72', 'Complex pairs', MAG),
    (-12, 'Quantum n\u00d7n', 'Gaussian + complex', MAG),
    (-10, 'DFT/FFT', 'Q335 twiddle + nesting', CYAN),
    (-9, 'IIR filters', 'Q335 multiply chain', CYAN),
    (-7, 'Transfer functions', 'Complex Horner', CYAN),
    (-6, 'State-space', 'Gaussian + matrix mul', BLUE),
    (-3, 'Crystallography', 'Rational matrix mul', PURPLE),
    (-1, 'Structural statics', 'Gaussian solve', ORANGE),
    (0, 'Paraxial optics', '2\u00d72 matrix power', GREEN),
    (2, 'Resonator stability', 'Rational comparison', GREEN),
    (5, 'Thermodynamics', 'Fn remainder exp/ln', ORANGE),
    (7, 'Geodesy', 'Rational matrix mul', GREEN),
    (10, 'Kepler orbits', 'Fn remainder Newton', GOLD),
]

# Draw domain markers on main axis
for i, (y_pos, name, mech, color) in enumerate(domains):
    x_base = 0.25
    x_end = 0.92

    # Alternating left/right placement for labels
    if i % 2 == 0:
        x_text = x_base
        ha = 'left'
        x_dot = x_base - 0.03
    else:
        x_text = x_end
        ha = 'right'
        x_dot = x_end + 0.03

    # Marker on the scale
    ax_y.plot(0.5, y_pos, 'o', color=color, markersize=8,
              markeredgecolor=WHITE, markeredgewidth=1.2, zorder=5)

    # Domain label on main figure area
    y_norm = (y_pos - (-18)) / (25 - (-18))
    ax.text(x_text, y_norm, name, color=color, fontsize=11,
            fontweight='bold', ha=ha, va='center',
            transform=ax.transAxes)
    ax.text(x_text, y_norm - 0.025, mech, color=SILVER, fontsize=8,
            ha=ha, va='center', transform=ax.transAxes)

# Title
ax.text(0.5, 0.97, 'Physical Computation Domains with Exact VDR Arithmetic',
        color=GOLD, fontsize=16, fontweight='bold',
        ha='center', va='top', transform=ax.transAxes)

# Footer
ax.text(0.5, 0.01, 'All 14 domains: zero drift, exact conservation laws, bit-identical reproducibility',
        color=SILVER, fontsize=10, fontstyle='italic',
        ha='center', va='bottom', transform=ax.transAxes)

save(fig, 'vdr14_05_domain_landscape.png')


# ================================================================
# FIG 6: PRECISION LANDSCAPE — FLOAT VS Q335
# Type: Scale/Landscape Diagram
# Shows: Horizontal precision axis with float at 15-16 digits,
#        Q335 at ~100 digits, and the 85-order-of-magnitude gap.
#        The SCALE of the gap is invisible in text.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
style_ax(ax,
         title='Precision Landscape: Float64 vs Q335 vs Physical Reality',
         xlabel='Precision (decimal digits)')

# Main horizontal axis
ax.set_xlim(-5, 120)
ax.set_ylim(-3, 8)
ax.set_yticks([])
ax.spines['left'].set_visible(False)

# Precision axis bar
ax.barh(4, 120, height=0.6, left=0, color=DIM, alpha=0.15, zorder=1)

# Float64 marker
ax.barh(4, 16, height=0.8, left=0, color=RED, alpha=0.5, zorder=3)
ax.plot(16, 4, 'D', color=RED, markersize=14, markeredgecolor=WHITE,
        markeredgewidth=2, zorder=6)
ax.text(16, 5.5, 'Float64\n15-16 digits', color=RED, fontsize=12,
        fontweight='bold', ha='center', va='bottom')

# Q335 marker
ax.barh(4, 100, height=0.8, left=0, color=GREEN, alpha=0.2, zorder=2)
ax.plot(100, 4, 's', color=GREEN, markersize=14, markeredgecolor=WHITE,
        markeredgewidth=2, zorder=6)
ax.text(100, 5.5, 'Q335\n~100 digits', color=GREEN, fontsize=12,
        fontweight='bold', ha='center', va='bottom')

# Gap annotation
ax.annotate('', xy=(17, 3), xytext=(99, 3),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(58, 2.2, '84 orders of magnitude gap', color=GOLD, fontsize=13,
        fontweight='bold', ha='center', va='top')

# Physical landmarks
landmarks = [
    (16, 'Engineering tolerance', SILVER, 1.5),
    (35, 'Planck length / observable universe', PURPLE, 1.5),
    (60, 'Q335 rounding error below\nPlanck by 10\u2076\u2076', CYAN, 0.5),
    (100, 'Sufficient for all known\nphysical computation', GREEN, 0.5),
]
for x, label, color, y_pos in landmarks:
    ax.plot(x, y_pos, '|', color=color, markersize=15, markeredgewidth=2)
    ax.text(x, y_pos - 0.6, label, color=color, fontsize=9,
            ha='center', va='top')

# Scalability note
ax.text(60, 7, 'Scalable: 2\u2076\u2076\u2078 for 200 digits, '
                '2\u00b3\u00b3\u00b2\u00b2 for 1000 digits',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=SILVER, alpha=0.9),
        ha='center', va='center')

# Key insight
ax.text(58, -1.5, 'Float truncates silently at every operation\n'
                   'Q335 reprojection is declared, auditable, with exact error bound',
        color=GOLD, fontsize=10, fontstyle='italic', ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.7))

ax.grid(True, alpha=0.05, color=DIM, axis='x')

save(fig, 'vdr14_06_precision_landscape.png')


# ================================================================
# FIG 7: SYSTEM ARCHITECTURE — LAYERED CROSS-SECTION
# Type: Geometric Cross-Section
# Shows: Concentric rings from VDR core outward through KB, Prolog,
#        primitives, command, inference, environments, lifecycle.
#        Every outer layer depends inward. Nesting IS the architecture.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_aspect('equal')
ax.axis('off')

layers = [
    (1.2, 'VDR\nArithmetic', GOLD, 0.55),
    (2.4, 'KB Engine', CYAN, 0.35),
    (3.5, 'Prolog', BLUE, 0.28),
    (4.6, 'Data\nPrimitives', GREEN, 0.22),
    (5.7, '448 Builtins', ORANGE, 0.18),
    (6.8, 'Command\nTokens', MAG, 0.15),
    (7.9, 'Sessions &\nClones', PURPLE, 0.12),
    (9.0, 'Inference\nOrchestration', CYAN, 0.10),
    (10.1, 'Environments', RED, 0.08),
    (11.0, 'Lifecycle', SILVER, 0.06),
]

# Draw rings from outside in so inner layers are on top
for i in range(len(layers) - 1, -1, -1):
    radius, label, color, alpha = layers[i]
    circle = plt.Circle((0, 0), radius, facecolor=color, alpha=alpha,
                         edgecolor=color, linewidth=1.5, zorder=i + 1)
    ax.add_patch(circle)

# Labels with offsets to avoid overlap
label_positions = [
    (0, 0, 11),          # VDR core - center
    (0, 1.9, 9),         # KB
    (2.6, 1.8, 9),       # Prolog
    (-3.2, 2.8, 8),      # Data Primitives
    (0, -4.2, 9),        # 448 Builtins
    (4.8, -2.5, 8),      # Command Tokens
    (-5.5, -4.0, 8),     # Sessions
    (0, 7.5, 9),         # Inference
    (7.2, 3.5, 8),       # Environments
    (-8.0, 6.0, 8),      # Lifecycle
]

for i, (x, y, fsize) in enumerate(label_positions):
    _, label, color, _ = layers[i]
    ax.text(x, y, label, color=WHITE, fontsize=fsize,
            fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=color, linewidth=1.5, alpha=0.85),
            zorder=20)

# Title
ax.text(0, 11.7, 'VDR-LLM-Prolog System Architecture',
        color=GOLD, fontsize=17, fontweight='bold', ha='center', va='bottom')

# Dependency arrow concept
ax.annotate('Every outer layer\ndepends inward',
            xy=(3, -8), xytext=(7, -10),
            color=SILVER, fontsize=10, fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5),
            ha='center', va='center')

# Core label
ax.text(0, -0.6, 'Integers\nOnly', color=GOLD, fontsize=8,
        ha='center', va='top', fontstyle='italic', zorder=25)

# Papers reference
papers_text = ('VDR-1\u20134: Core\nVDR-5: KB+Prolog\n'
               'VDR-6: Primitives\nVDR-8: Sessions\n'
               'VDR-9: Inference\nVDR-10: IOSE\n'
               'VDR-11: Build Plan')
ax.text(-10.5, -9.5, papers_text, color=DIM, fontsize=8,
        ha='left', va='top', family='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.8))

save(fig, 'vdr14_07_architecture.png')


# ================================================================
# FIG 8: FLOAT FAILURE HEATMAP ACROSS DOMAINS
# Type: Threshold/Region Chart
# Shows: 12 domains x (Float vs VDR) matrix. Green for VDR exact,
#        red gradient for float error magnitude. The PATTERN of
#        uniform green vs escalating red is the visual argument.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax,
         title='Float64 vs VDR: Error Across Physical Domains',
         title_size=16)

domains = [
    'Linear algebra\n(H\u2085)',
    'Linear algebra\n(H\u2081\u2080)',
    'Signal proc.\n(return-to-origin)',
    'Signal proc.\n(IIR filter)',
    'Quantum mech.\n(U\u2074=I)',
    'Probability\n(PMF sum)',
    'Orbital mech.\n(Kepler closure)',
    'Control sys.\n(Cayley-Hamilton)',
    'Optics\n(det after 1000)',
    'Geodesy\n(Helmert round.)',
    'Chaos\n(tent map 25st)',
    'Chaos\n(logistic r=4)',
]

# Float error exponents (negative = small error, positive = catastrophic)
# mapped to color intensity
float_exponents = [
    -9,    # H5: ~1e-9
    -2,    # H10: ~1e-2 catastrophic
    -16,   # 200-op: ~1e-16
    -16,   # IIR: ~1e-16
    -15,   # U^4: ~1e-15
    -16,   # PMF: ~1e-16
    -12,   # Kepler: ~1e-12
    -15,   # Cayley-Hamilton: ~1e-15
    -12,   # det: ~1e-12
    -9,    # Helmert: ~1nm
    99,    # tent: total loss
    99,    # logistic: total loss
]

float_labels = [
    '~10\u207b\u2079', '~10\u207b\u00b2', '~10\u207b\u00b9\u2076',
    '~10\u207b\u00b9\u2076', '~10\u207b\u00b9\u2075', '~10\u207b\u00b9\u2076',
    '~10\u207b\u00b9\u00b2', '~10\u207b\u00b9\u2075', '~10\u207b\u00b9\u00b2',
    '~1 nm', 'TOTAL\nLOSS', 'TOTAL\nLOSS',
]

n = len(domains)
y_positions = np.arange(n)

# VDR column (all green = exact zero)
for i in range(n):
    rect = mpatches.FancyBboxPatch(
        (0.5, i - 0.38), 3.5, 0.76,
        boxstyle='round,pad=0.05', facecolor=GREEN, alpha=0.35,
        edgecolor=GREEN, linewidth=1)
    ax.add_patch(rect)
    ax.text(2.25, i, '0\n(exact)', color=GREEN, fontsize=9,
            fontweight='bold', ha='center', va='center')

# Float column (red gradient based on error severity)
for i in range(n):
    exp = float_exponents[i]
    if exp == 99:
        alpha = 0.7
        color = RED
    elif exp >= -5:
        alpha = 0.55
        color = RED
    elif exp >= -10:
        alpha = 0.35
        color = ORANGE
    else:
        alpha = 0.2
        color = ORANGE

    rect = mpatches.FancyBboxPatch(
        (5.0, i - 0.38), 3.5, 0.76,
        boxstyle='round,pad=0.05', facecolor=color, alpha=alpha,
        edgecolor=color, linewidth=1)
    ax.add_patch(rect)

    label_color = WHITE if exp >= -5 or exp == 99 else SILVER
    ax.text(6.75, i, float_labels[i], color=label_color, fontsize=9,
            fontweight='bold', ha='center', va='center')

# Domain labels
for i in range(n):
    ax.text(-0.2, i, domains[i], color=WHITE, fontsize=9,
            ha='right', va='center')

# Column headers
ax.text(2.25, n + 0.3, 'VDR Error', color=GREEN, fontsize=13,
        fontweight='bold', ha='center', va='bottom')
ax.text(6.75, n + 0.3, 'Float64 Error', color=RED, fontsize=13,
        fontweight='bold', ha='center', va='bottom')

# Separator
ax.axvline(x=4.5, color=DIM, linewidth=1, alpha=0.3)

# Summary
ax.text(4.5, -1.8,
        '12 domains. VDR: zero error in all. Float: degrades from acceptable to catastrophic.',
        color=GOLD, fontsize=11, ha='center', va='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.8))

ax.set_xlim(-5.5, 11)
ax.set_ylim(-2.8, n + 1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

save(fig, 'vdr14_08_float_failure_heatmap.png')


# ================================================================
# SUMMARY
# ================================================================

print("\nVDR-14 Diagram Script Complete")
print("=" * 50)
filenames = [
    'vdr14_01_denom_growth.png',
    'vdr14_02_hilbert_error.png',
    'vdr14_03_convergence_rates.png',
    'vdr14_04_build_progression.png',
    'vdr14_05_domain_landscape.png',
    'vdr14_06_precision_landscape.png',
    'vdr14_07_architecture.png',
    'vdr14_08_float_failure_heatmap.png',
]
for f in filenames:
    print("  %s" % f)
print("=" * 50)
