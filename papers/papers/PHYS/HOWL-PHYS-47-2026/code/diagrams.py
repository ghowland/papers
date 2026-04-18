#!/usr/bin/env python3
"""
HOWL PHYS-44 Diagrams — The Clock and the Reading
8 figures covering D/K decomposition, sector splitting, tick budgets,
GPS decomposition, muon product, soliton hierarchy, and WEP consistency.
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

print("PHYS-44 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: KAPPA SWEEP — SECTOR SPLITTING DETECTION THRESHOLD
# Type: Threshold/Region (D5.3)
# Shows: 13 orders of detectable kappa range. Three sector pairs
#        with different intercepts. Detection thresholds as bands.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(\kappa)$',
         r'$\log_{10}(\epsilon_{ij})$ at $\Delta h = 1000$ m')

log_kappa = np.linspace(-9, 1, 500)
delta_phi = 9.82 * 1000.0 / (2.998e8)**2

pairs = [
    (r'Strong$-$EM: $|\Delta\beta| = 111/10$', 111.0/10.0, CYAN),
    (r'Weak$-$EM: $|\Delta\beta| = 79/30$', 79.0/30.0, GREEN),
    (r'Strong$-$Weak: $|\Delta\beta| = 23/6$', 23.0/6.0, MAG),
]

for label, db, color in pairs:
    log_eps = log_kappa + np.log10(db * delta_phi)
    ax.plot(log_kappa, log_eps, color=color, lw=2.5, label=label)

thresholds = [
    (-18, r'Current optical clock ($10^{-18}$)', GREEN, '--'),
    (-19, r'Projected Th-229 ($10^{-19}$)', CYAN, '--'),
    (-21, r'Space clocks ($10^{-21}$)', PURPLE, ':'),
]
for val, label, color, ls in thresholds:
    ax.axhline(val, color=color, lw=1.5, ls=ls, alpha=0.6)
    ax.text(0.8, val + 0.3, label, color=color, fontsize=9, ha='right')

ax.fill_between(log_kappa, -18, -8, color=GREEN, alpha=0.04)
ax.text(-4, -9.5, 'DETECTABLE', color=GREEN, fontsize=14,
        fontweight='bold', ha='center', alpha=0.4)
ax.fill_between(log_kappa, -22, -18, color=RED, alpha=0.03)
ax.text(-4, -20, 'BELOW THRESHOLD', color=RED, fontsize=11,
        ha='center', alpha=0.3)

# Mark suppression mechanisms
suppress = [
    (0, r'$\kappa = 1$', GOLD),
    (np.log10(0.118), r'$\kappa = \alpha_s$', ORANGE),
    (np.log10(1.0/137.036), r'$\kappa = \alpha_{em}$', BLUE),
    (-4.28, r'$\kappa = \alpha_{em}^2$', PURPLE),
]
for xv, lab, col in suppress:
    eps_31 = xv + np.log10(111.0/10.0 * delta_phi)
    ax.plot(xv, eps_31, 'o', color=col, markersize=10,
            linewidth=1.5, zorder=5)
    ax.annotate(lab, xy=(xv, eps_31), xytext=(xv - 0.8, eps_31 + 1.0),
                color=col, fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=col, lw=1.2))

ax.set_xlim(-9.5, 1.5)
ax.set_ylim(-22, -8)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper left')

ax.set_title(r'Sector Splitting vs $\kappa$: 13 Orders of Detectable Range',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys44_01_kappa_sweep.png')


# ================================================================
# FIG 2: D/K CLASSIFICATION OF 18 TESTS — LANDSCAPE
# Type: Scale/Landscape (D5.2)
# Shows: All 18 PHYS-42 tests arranged by category, colored by D/K
#        classification. The reader sees the dominance of D at a glance.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

tests = [
    ('Pound-\nRebka', 'D', 'static gradient'),
    ('GPS\ngrav', 'D', 'static potential'),
    ('Gravity\nProbe A', 'D', 'static potential'),
    ('Solar\nredshift', 'D', 'static potential'),
    ('Mercury\nperihelion', 'D', 'geometric curvature'),
    ('Shapiro\nPPN '+r'$\gamma$', 'D', 'structural ratio'),
    ('g\nsurface', 'D', 'static gradient'),
    ('Earth\n'+r'$\Phi/c^2$', 'D', 'static potential'),
    ('Sun\n'+r'$\Phi/c^2$', 'D', 'static potential'),
    ('Earth\n'+r'$r_s$', 'D', 'static radius'),
    ('GPS\nvelocity', 'K', r'$v^2/2c^2$'),
    ('SN Ia\nstretch', 'K', 'epoch comparison'),
    ('GPS\nnet', 'M', 'D + K sum'),
    ('Muon\ndilation', 'M', r'$\gamma \times \tau_{rest}$'),
    ('Hulse-\nTaylor', 'M', 'instant D + cumul K'),
    ('Planck\ntime', 'S', 'tick step def'),
    ('Planck\nlength', 'S', 'spatial res def'),
    (r'$c = l_P/t_P$', 'S', 'ratio identity'),
]

# note: GPS velocity listed separately from GPS net for visual clarity
# but in the paper GPS velocity is part of the mixed GPS net discussion

colors_map = {'D': CYAN, 'K': ORANGE, 'M': GOLD, 'S': SILVER}
labels_map = {'D': 'Reading (D)', 'K': 'Tick (K)', 'M': 'Mixed (D'+r'$\times$'+'K)', 'S': 'Structural'}

# Group by category for visual clustering
order = [i for i in range(len(tests)) if tests[i][1] == 'D'] + \
        [i for i in range(len(tests)) if tests[i][1] == 'K'] + \
        [i for i in range(len(tests)) if tests[i][1] == 'M'] + \
        [i for i in range(len(tests)) if tests[i][1] == 'S']

x_positions = np.arange(len(order))
bar_height = 0.8

for idx, oi in enumerate(order):
    name, cat, desc = tests[oi]
    col = colors_map[cat]
    ax.barh(idx, 1, height=bar_height, color=col, alpha=0.6,
            edgecolor=col, linewidth=1.5)
    ax.text(-0.15, idx, name, color=WHITE, fontsize=9, ha='right',
            va='center', fontweight='bold')
    ax.text(1.1, idx, desc, color=col, fontsize=8, ha='left',
            va='center', alpha=0.8)

# Category dividers
d_count = sum(1 for t in tests if t[1] == 'D')
k_count = sum(1 for t in tests if t[1] == 'K')
m_count = sum(1 for t in tests if t[1] == 'M')

ax.axhline(d_count - 0.5, color=DIM, lw=1, ls='--', alpha=0.5)
ax.axhline(d_count + k_count - 0.5, color=DIM, lw=1, ls='--', alpha=0.5)
ax.axhline(d_count + k_count + m_count - 0.5, color=DIM, lw=1, ls='--', alpha=0.5)

# Category labels on right
ax.text(3.5, d_count/2 - 0.5, 'READING (D)\n10 tests = 56%',
        color=CYAN, fontsize=13, fontweight='bold', ha='center', va='center')
ax.text(3.5, d_count + k_count/2 - 0.5, 'TICK (K)\n2 tests = 11%',
        color=ORANGE, fontsize=13, fontweight='bold', ha='center', va='center')
ax.text(3.5, d_count + k_count + m_count/2 - 0.5, 'MIXED\n3 tests = 17%',
        color=GOLD, fontsize=13, fontweight='bold', ha='center', va='center')
ax.text(3.5, d_count + k_count + m_count + 1, 'STRUCTURAL\n3 tests = 17%',
        color=SILVER, fontsize=13, fontweight='bold', ha='center', va='center')

ax.set_xlim(-3, 5)
ax.set_ylim(-1, len(order))
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('D/K Classification of All 18 PHYS-42 Tests',
             color=GOLD, fontsize=16, fontweight='bold', pad=15)

# Bottom annotation
ax.text(1.5, -0.8, 'Frozen scan coverage: 89% of tests predictable from spatial geometry alone',
        color=GOLD, fontsize=11, ha='center', style='italic')

save(fig, 'phys44_02_dk_classification.png')


# ================================================================
# FIG 3: MUON D x K PRODUCT — READING TIMES TICKING
# Type: Progression/Sequence (D5.7)
# Shows: Left panel = spatial (gamma from trajectory), right panel =
#        temporal (tick budget), bottom = their product = observation.
# ================================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 9),
                          gridspec_kw={'wspace': 0.35, 'width_ratios': [1, 1, 1.2]})
fig.patch.set_facecolor(BG)

# Panel 1: D factor (gamma)
ax1 = axes[0]
setup_ax(ax1, '', r'$\beta = v/c$', r'$\gamma = 1/\sqrt{1-\beta^2}$')
beta = np.linspace(0.0, 0.999, 500)
gamma = 1.0 / np.sqrt(1.0 - beta**2)
ax1.plot(beta, gamma, color=CYAN, lw=2.5)
ax1.axhline(15.82, color=GOLD, lw=1.5, ls='--', alpha=0.6)
ax1.axvline(0.998, color=GOLD, lw=1.5, ls='--', alpha=0.6)
ax1.plot(0.998, 15.82, '*', color=GOLD, markersize=18, zorder=6)
ax1.annotate(r'Cosmic muon' + '\n' + r'$\beta = 0.998$' + '\n' + r'$\gamma = 15.8$',
             xy=(0.998, 15.82), xytext=(0.7, 22),
             color=GOLD, fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))
ax1.set_xlim(0, 1.02)
ax1.set_ylim(0, 35)
ax1.set_title('D Factor: Spatial Reading', color=CYAN, fontsize=13,
              fontweight='bold', pad=10)
ax1.text(0.5, 32, 'Frozen geometry\nNo ticking needed',
         color=CYAN, fontsize=9, ha='center', style='italic')

# Panel 2: K factor (tick budget)
ax2 = axes[1]
setup_ax(ax2, '', '', 'Planck ticks')
ax2.set_facecolor(PAN)
categories = [r'$\tau_{rest}$' + '\n2.197 '+r'$\mu$'+'s', r'$\tau_{lab}$' + '\n34.7 '+r'$\mu$'+'s']
values = [4.08e37, 6.44e38]
colors_b = [ORANGE, GOLD]
bars = ax2.bar([0, 1], values, color=colors_b, alpha=0.7,
               edgecolor=colors_b, linewidth=1.5, width=0.6)
ax2.set_yscale('log')
ax2.set_ylim(1e36, 1e40)
ax2.set_xticks([0, 1])
ax2.set_xticklabels(categories, color=WHITE, fontsize=10)
for i, v in enumerate(values):
    ax2.text(i, v * 1.5, '%.2e' % v, color=colors_b[i],
             fontsize=10, ha='center', fontweight='bold')
ax2.set_title('K Factor: Tick Budget', color=ORANGE, fontsize=13,
              fontweight='bold', pad=10)
ax2.text(0.5, 3e39, 'Internal counting\nRequires ticking',
         color=ORANGE, fontsize=9, ha='center', style='italic')

# Panel 3: The product
ax3 = axes[2]
ax3.set_facecolor(PAN)
for spine in ax3.spines.values():
    spine.set_color(GOLD)
    spine.set_linewidth(2)
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.set_xticks([])
ax3.set_yticks([])

ax3.text(5, 8.5, 'THE OBSERVATION', color=GOLD, fontsize=14,
         fontweight='bold', ha='center')
ax3.text(5, 7.0, r'$\tau_{lab} = \gamma \times \tau_{rest}$',
         color=WHITE, fontsize=18, ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))
ax3.text(5, 5.2, '= 15.82  ' + r'$\times$' + '  2.197 ' + r'$\mu$' + 's',
         color=WHITE, fontsize=14, ha='center')
ax3.text(5, 4.0, '= 34.7 ' + r'$\mu$' + 's',
         color=GOLD, fontsize=16, ha='center', fontweight='bold')

ax3.text(2.5, 2.2, 'D', color=CYAN, fontsize=20, fontweight='bold', ha='center')
ax3.text(3.8, 2.2, r'$\times$', color=WHITE, fontsize=20, ha='center')
ax3.text(5.0, 2.2, 'K', color=ORANGE, fontsize=20, fontweight='bold', ha='center')
ax3.text(6.3, 2.2, '=', color=WHITE, fontsize=20, ha='center')
ax3.text(7.8, 2.2, 'Observed', color=GOLD, fontsize=16, fontweight='bold', ha='center')

ax3.text(5, 0.8, 'Miss: 0.044%', color=GREEN, fontsize=12, ha='center')

ax3.set_title(r'$D \times K$ Product', color=GOLD, fontsize=13,
              fontweight='bold', pad=10)

save(fig, 'phys44_03_muon_dk_product.png')


# ================================================================
# FIG 4: SOLITON HIERARCHY WITH D/K LABELS
# Type: Geometric Cross-Section (D5.4)
# Shows: Nested boundaries with D/K classification at each level.
#        Ten D levels in cyan, K level in orange, mixed in gold.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.axis('off')

levels = [
    (7.0, 'Cosmos', 'K', r'SN Ia: $(1+z)$', ORANGE, 0.12),
    (5.8, 'Galaxy', 'D', r'$\Phi/c^2 \sim 10^{-6}$', CYAN, 0.15),
    (4.6, 'Heliosphere', 'D', r'$\Phi/c^2 \sim 10^{-8}$', CYAN, 0.18),
    (3.8, 'Star (Sun)', 'D', r'$\Phi/c^2 = 2.12 \times 10^{-6}$', CYAN, 0.22),
    (2.8, 'Planet (Earth)', 'D', r'$\Phi/c^2 = 6.96 \times 10^{-10}$', CYAN, 0.28),
    (2.0, 'GPS orbit', 'Mixed', r'D: $+45.85$ / K: $-7.21$ $\mu$s/day', GOLD, 0.33),
    (1.4, 'Laboratory', 'D', r'$\Delta\Phi/c^2 \sim 10^{-13}$/km', CYAN, 0.40),
    (0.8, 'Atom', 'D', r'EM sector: $\alpha_{em}$', CYAN, 0.50),
    (0.35, 'Nucleus', 'D', r'Strong sector: $\alpha_s$', CYAN, 0.60),
]

count = 0
for radius, name, cat, phi_label, color, alpha in levels:
    edgecolor = color
    circle = Circle((0, 0), radius, facecolor=color, alpha=alpha * 0.12,
                     edgecolor=edgecolor, linewidth=2.0 if cat != 'D' else 1.5,
                     linestyle='-' if cat == 'D' else '--')
    ax.add_patch(circle)

    # Name at top of circle
    ax.text(0, radius + 0.12, name, color=color, fontsize=10,
            fontweight='bold', ha='center', va='bottom')

    # Category tag
    tag_colors = {'D': CYAN, 'K': ORANGE, 'Mixed': GOLD}
    ax.text(-radius - 0.15, 0 + count * -0.25, '[%s]' % cat, color=tag_colors[cat],
            fontsize=8, fontweight='bold', ha='right', va='center')

    # Scale label at right
    ax.text(radius + 0.15, 0 + count * -0.25, phi_label, color=color, fontsize=8,
            ha='left', va='center', alpha=0.8)

    count += 1

# Center: Planck
ax.text(0, -0.02, 'Planck\n[Structural]', color=SILVER, fontsize=8,
        ha='center', va='center', fontweight='bold')
ax.text(0, -0.25, r'$t_P, l_P, c=l_P/t_P$', color=SILVER, fontsize=7,
        ha='center')

# Sector splitting marker between nucleus and atom
ax.annotate('SECTOR\nSPLITTING\nTEST', xy=(0.6, 0.6), xytext=(3.5, 1.5),
            color=GOLD, fontsize=11, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
ax.text(3.5, 0.8, r'$\epsilon = \kappa |\Delta\beta| \Delta\Phi/c^2$',
        color=GOLD, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Legend
ax.text(-7.5, 7.5, 'Reading (D) — frozen geometry', color=CYAN, fontsize=10)
ax.text(-7.5, 7.0, 'Tick (K) — epoch comparison', color=ORANGE, fontsize=10)
ax.text(-7.5, 6.5, 'Mixed — D + K combined', color=GOLD, fontsize=10)
ax.text(-7.5, 6.0, 'Structural — definitions', color=SILVER, fontsize=10)

ax.text(0, 7.7, 'The Soliton Hierarchy: Reading vs Ticking at Each Level',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

save(fig, 'phys44_04_hierarchy_dk.png')


# ================================================================
# FIG 5: TICK BUDGET LANDSCAPE — 49 ORDERS OF MAGNITUDE
# Type: Scale/Landscape (D5.2)
# Shows: Log-scale axis from 10^36 to 10^85 Planck ticks with
#        landmarks. Three regimes visible: decay, orbital, cosmological.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(N_{ticks})$  [Planck ticks]', '')

landmarks = [
    (36.1, 'Photon\n22.5 m transit', SILVER, 'D traversal'),
    (37.6, 'Muon\nrest lifetime', ORANGE, 'K budget'),
    (47.7, 'Hulse-Taylor\norbital period', MAG, 'K orbital'),
    (47.9, 'GPS\norbital period', GREEN, 'K orbital'),
    (50.1, 'Mercury\norbital period', CYAN, 'K orbital'),
    (60.5, 'SN Ia\nlookback z=0.5', PURPLE, 'K cosmological'),
    (60.9, 'Universe\nage', GOLD, 'K cosmological'),
    (85.3, 'Proton\nlifetime (GUT)', RED, 'K decay'),
]

# Draw the scale line
ax.axhline(0.5, color=DIM, lw=2, alpha=0.3)

for x, label, color, category in landmarks:
    ax.plot(x, 0.5, 'o', color=color, markersize=14,
            linewidth=1.8, zorder=5)
    # Alternate labels above and below
    idx = landmarks.index((x, label, color, category))
    if idx % 2 == 0:
        ax.annotate(label, xy=(x, 0.5), xytext=(x, 0.75),
                    color=color, fontsize=9, fontweight='bold',
                    ha='center', va='bottom',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1))
    else:
        ax.annotate(label, xy=(x, 0.5), xytext=(x, 0.25),
                    color=color, fontsize=9, fontweight='bold',
                    ha='center', va='top',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1))

# Regime shading
ax.axvspan(36, 38, color=ORANGE, alpha=0.05)
ax.axvspan(47, 51, color=GREEN, alpha=0.05)
ax.axvspan(59, 62, color=PURPLE, alpha=0.05)
ax.axvspan(84, 86, color=RED, alpha=0.05)

ax.text(37, 0.92, 'Decay\nticks', color=ORANGE, fontsize=9,
        ha='center', style='italic', alpha=0.7)
ax.text(49, 0.92, 'Orbital\nticks', color=GREEN, fontsize=9,
        ha='center', style='italic', alpha=0.7)
ax.text(60.5, 0.08, 'Cosmological\nticks', color=PURPLE, fontsize=9,
        ha='center', style='italic', alpha=0.7)
ax.text(85, 0.92, 'GUT\ndecay', color=RED, fontsize=9,
        ha='center', style='italic', alpha=0.7)

ax.set_xlim(34, 88)
ax.set_ylim(0, 1)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

ax.set_title('Tick Budgets: 49 Orders of Magnitude in the Counting Machine',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

# Span annotation
ax.annotate('', xy=(85.3, 0.5), xytext=(36.1, 0.5),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1, alpha=0.3))
ax.text(60, 0.55, '49 orders of magnitude', color=DIM, fontsize=10,
        ha='center', alpha=0.5)

save(fig, 'phys44_05_tick_budget.png')


# ================================================================
# FIG 6: THE 10/1/4/3 CLASSIFICATION BAR CHART
# Type: Comparison Bar (D5.6)
# Shows: Four bars for D/K/Mixed/Structural. The D bar dominates.
#        Each bar labeled with count and test names.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Number of PHYS-42 tests')

categories = ['Reading\n(D)', 'Tick\n(K)', 'Mixed\n(D'+r'$\times$'+'K)', 'Structural']
counts = [10, 1, 4, 3]
colors_bars = [CYAN, ORANGE, GOLD, SILVER]

bars = ax.bar(range(4), counts, color=colors_bars, alpha=0.7,
              edgecolor=colors_bars, linewidth=2, width=0.65)

# Count labels on bars
for i, (c, col) in enumerate(zip(counts, colors_bars)):
    ax.text(i, c + 0.3, str(c), color=col, fontsize=22,
            fontweight='bold', ha='center')

# Test name labels inside bars
d_tests = 'Pound-Rebka, GPS grav,\nGPA, Solar, Mercury,\nShapiro, g, Earth '+r'$\Phi$'+',\nSun '+r'$\Phi$'+', Earth '+r'$r_s$'
k_tests = 'SN Ia\nstretch'
m_tests = 'GPS net,\nGPS vel,\nMuon,\nHulse-Taylor'
s_tests = r'$t_P$'+', '+r'$l_P$'+',\n'+r'$c = l_P/t_P$'

test_labels = [d_tests, k_tests, m_tests, s_tests]
for i, (label, col) in enumerate(zip(test_labels, colors_bars)):
    y_pos = counts[i] / 2
    ax.text(i, y_pos, label, color=BG, fontsize=7,
            ha='center', va='center', fontweight='bold')

ax.set_xticks(range(4))
ax.set_xticklabels(categories, color=WHITE, fontsize=12)
ax.set_ylim(0, 13)

# Percentage annotations
percentages = ['56%', '6%', '22%', '17%']
for i, (pct, col) in enumerate(zip(percentages, colors_bars)):
    ax.text(i, counts[i] + 0.9, pct, color=col, fontsize=12,
            ha='center', style='italic')

# The 89% line
ax.text(3.3, 12, 'Frozen scan coverage: 89%',
        color=GOLD, fontsize=13, fontweight='bold', ha='right',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

ax.set_title('The 10 / 1 / 4 / 3 Decomposition',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

save(fig, 'phys44_06_classification_bars.png')


# ================================================================
# FIG 7: GPS DECOMPOSITION — 86% READING, 14% TICK
# Type: Comparison Bar (D5.6)
# Shows: Three bars: D component, K component, net. The asymmetry
#        between D and K is immediately visible. Signs shown.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'$\mu$s / day')

components = ['D: Gravitational\n(reading depth)', 'K: Velocity\n(tick allocation)',
              'Net\n(D + K)']
values_gps = [45.85, -7.21, 38.64]
colors_gps = [CYAN, ORANGE, GOLD]

bars = ax.bar(range(3), values_gps, color=colors_gps, alpha=0.7,
              edgecolor=colors_gps, linewidth=2, width=0.55)

for i, (v, col) in enumerate(zip(values_gps, colors_gps)):
    sign = '+' if v > 0 else ''
    y_pos = v + 1.5 if v > 0 else v - 2.5
    ax.text(i, y_pos, '%s%.2f' % (sign, v), color=col, fontsize=16,
            fontweight='bold', ha='center')

ax.axhline(0, color=DIM, lw=1, alpha=0.5)

ax.set_xticks(range(3))
ax.set_xticklabels(components, color=WHITE, fontsize=11)
ax.set_ylim(-12, 55)

# Percentage breakdown
ax.text(0, 50, '86.4%', color=CYAN, fontsize=18, fontweight='bold', ha='center')
ax.text(1, -10, '13.6%', color=ORANGE, fontsize=18, fontweight='bold', ha='center')
ax.text(2, 43, '100%', color=GOLD, fontsize=18, fontweight='bold', ha='center')

# Explanation
ax.text(0, 42, 'Shallower depth\n= faster updates',
        color=CYAN, fontsize=9, ha='center', style='italic')
ax.text(1, -8, 'Spatial displacement\n= fewer updates',
        color=ORANGE, fontsize=9, ha='center', style='italic')

# Formula
ax.text(1, 52, r'GPS net $= \frac{GM}{c^2}\left(\frac{1}{R_E} - \frac{1}{r_{gps}}\right) - \frac{v^2}{2c^2}$',
        color=WHITE, fontsize=11, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

ax.set_title('GPS: 86% Reading, 14% Ticking',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

save(fig, 'phys44_07_gps_decomposition.png')


# ================================================================
# FIG 8: WEP CONSISTENCY — SUM GRAVITY VS PER-SECTOR
# Type: Threshold/Region (D5.3)
# Shows: Two scenarios for how gravity couples to sector readings.
#        Sum gravity = no WEP violation. Per-sector = possible violation.
#        MICROSCOPE bound shown as threshold.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)

# Left panel: Sum gravity (RUM prediction)
setup_ax(ax1, '', '', '')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_xticks([])
ax1.set_yticks([])

ax1.set_title('Sum Gravity (RUM)', color=GREEN, fontsize=14,
              fontweight='bold', pad=10)

# Draw three sector bars stacking into one gravitational coupling
sectors_left = [
    (1.5, 'EM', BLUE, 3.0),
    (1.5, 'Weak', GREEN, 2.0),
    (1.5, 'Strong', RED, 4.0),
]
y_base = 1.5
for i, (x, label, color, height) in enumerate(sectors_left):
    rect = FancyBboxPatch((x + i*2.2, y_base), 1.8, height,
                           boxstyle='round,pad=0.1',
                           facecolor=color, alpha=0.3, edgecolor=color,
                           linewidth=1.5)
    ax1.add_patch(rect)
    ax1.text(x + i*2.2 + 0.9, y_base + height/2, label,
             color=color, fontsize=10, ha='center', va='center',
             fontweight='bold')

# Sum arrow
ax1.annotate('', xy=(4.5, 8.5), xytext=(4.5, 6.5),
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax1.text(4.5, 7.5, 'SUM', color=GOLD, fontsize=12, fontweight='bold',
         ha='center')

# Result
ax1.text(4.5, 9.0, r'$g = g_{EM} + g_{Weak} + g_{Strong}$',
         color=WHITE, fontsize=11, ha='center')
ax1.text(4.5, 8.5, 'Same total for all materials',
         color=GREEN, fontsize=10, ha='center')

# WEP result
rect_result = FancyBboxPatch((1.5, 0.3), 6, 0.8,
                              boxstyle='round,pad=0.1',
                              facecolor=BG, edgecolor=GREEN, linewidth=2)
ax1.add_patch(rect_result)
ax1.text(4.5, 0.7, r'WEP: $\Delta g / g = 0$  — No violation',
         color=GREEN, fontsize=11, ha='center', fontweight='bold')

# Right panel: Per-sector gravity (alternative)
setup_ax(ax2, '', '', '')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_xticks([])
ax2.set_yticks([])

ax2.set_title('Per-Sector Gravity (alternative)', color=RED, fontsize=14,
              fontweight='bold', pad=10)

# Draw sectors with DIFFERENT gravitational couplings
sectors_right = [
    (1.5, 'EM', BLUE, 3.0),
    (1.5, 'Weak', GREEN, 2.5),
    (1.5, 'Strong', RED, 4.5),
]
for i, (x, label, color, height) in enumerate(sectors_right):
    rect = FancyBboxPatch((x + i*2.2, y_base), 1.8, height,
                           boxstyle='round,pad=0.1',
                           facecolor=color, alpha=0.3, edgecolor=color,
                           linewidth=1.5)
    ax2.add_patch(rect)
    ax2.text(x + i*2.2 + 0.9, y_base + height/2, label,
             color=color, fontsize=10, ha='center', va='center',
             fontweight='bold')

# Different heights → different g
ax2.text(4.5, 7.5, 'Different sector\nweights per material',
         color=RED, fontsize=10, ha='center')

# MICROSCOPE bound
rect_micro = FancyBboxPatch((1.5, 0.3), 6, 0.8,
                             boxstyle='round,pad=0.1',
                             facecolor=BG, edgecolor=ORANGE, linewidth=2)
ax2.add_patch(rect_micro)
ax2.text(4.5, 0.7, r'MICROSCOPE: $\eta < 1.5 \times 10^{-15}$  — constrains $\kappa < 1.2$',
         color=ORANGE, fontsize=10, ha='center', fontweight='bold')

# Arrow showing the difference
ax2.annotate('', xy=(7.5, 6.0), xytext=(7.5, 4.5),
             arrowprops=dict(arrowstyle='<->', color=RED, lw=1.5))
ax2.text(8.2, 5.2, r'$\Delta g$', color=RED, fontsize=12, fontweight='bold')

# Overall title
fig.suptitle('WEP Consistency: Clocks Split, Free Fall Does Not',
             color=GOLD, fontsize=16, fontweight='bold', y=0.98)

save(fig, 'phys44_08_wep_consistency.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys44_01_kappa_sweep.png")
print("  phys44_02_dk_classification.png")
print("  phys44_03_muon_dk_product.png")
print("  phys44_04_hierarchy_dk.png")
print("  phys44_05_tick_budget.png")
print("  phys44_06_classification_bars.png")
print("  phys44_07_gps_decomposition.png")
print("  phys44_08_wep_consistency.png")
print("=" * 50)
