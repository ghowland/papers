#!/usr/bin/env python3
"""
HOWL CULT-15 Diagrams — Showing Your Work in 2026
8 figures covering the five-layer standard, BBN cross-domain example,
pre-registered falsification, anti-smuggling, and verification economics.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Global style ──────────────────────────────────────────────

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

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for sp in ax.spines.values():
        sp.set_color(DIM)
        sp.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=18)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=10)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=10)


# ================================================================
# FIG 1: BBN DOMAIN CROSSING MAP
# Type: Connection/Integer Map (Type 5)
# Shows: How gauge integers flow through three physics domains
#        with actual numerical values at each handoff point.
#        Text says "cross-domain" — this shows exactly where
#        13/264 becomes eta=6.090 becomes Y_p=0.2486.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 8.5)

ax.set_title('BBN Domain Crossing Map\nGauge Integers to Nuclear Abundances',
             color=GOLD, fontsize=16, fontweight='bold', pad=25)

# Domain background regions
dom_regions = [
    ((-0.3, 4.8), 3.4, 3.4, '#1a1a3a', 'PARTICLE PHYSICS', BLUE),
    ((3.5, 4.8), 3.4, 3.4, '#1a2a1a', 'COSMOLOGY', PURPLE),
    ((7.3, 4.8), 3.0, 3.4, '#2a1a1a', 'NUCLEAR PHYSICS', MAG),
]
for (x, y), w, h, fc, label, lc in dom_regions:
    rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15',
                          facecolor=fc, edgecolor=lc, linewidth=1.5, alpha=0.6)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 0.3, label, ha='center', va='top',
            color=lc, fontsize=10, fontweight='bold', alpha=0.8)

# Value boxes
boxes = [
    # (x, y, label_top, value, color)
    (0.7, 6.2, 'Gauge Integers', '11, 13', BLUE),
    (0.7, 5.2, r'$\Omega_b = 13/264$', '0.049036', CYAN),
    (4.0, 7.0, r'$\Omega_{DM} = \pi/12$', '0.2618', PURPLE),
    (4.0, 5.8, r'$\eta = n_b / n_\gamma$', '6.090e-10', CYAN),
    (4.0, 5.0, r'$\eta_{10}$', '6.090', GREEN),
    (8.0, 7.0, r'$Y_p$ (He-4)', '0.2486', ORANGE),
    (8.0, 6.0, 'D/H', '2.531e-5', GREEN),
    (8.0, 5.2, r'$N_{eff}$', '2.712', SILVER),
]

for bx, by, label, val, col in boxes:
    rect = FancyBboxPatch((bx - 0.6, by - 0.25), 1.9, 0.65,
                          boxstyle='round,pad=0.12',
                          facecolor=BG, edgecolor=col, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(bx + 0.35, by + 0.18, label, ha='center', va='center',
            color=col, fontsize=9, fontweight='bold')
    ax.text(bx + 0.35, by - 0.08, val, ha='center', va='center',
            color=WHITE, fontsize=10)

# Arrows between boxes
arrow_kw = dict(arrowstyle='->', color=GOLD, lw=2, mutation_scale=18)
arrow_list = [
    ((1.65, 6.2), (1.65, 5.65)),      # integers -> omega_b
    ((2.0, 5.35), (3.4, 5.85)),       # omega_b -> eta
    ((2.0, 6.2), (3.4, 7.0)),         # integers -> omega_dm (through pi)
    ((4.95, 5.55), (4.95, 5.25)),     # eta -> eta10
    ((5.5, 7.0), (7.4, 7.0)),         # (cosmology) -> Y_p
    ((5.5, 5.15), (7.4, 6.0)),        # eta10 -> D/H
    ((5.5, 5.0), (7.4, 5.2)),         # -> N_eff
]

for (x1, y1), (x2, y2) in arrow_list:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# Measured values (comparison annotations on right)
meas = [
    (9.6, 7.25, 'Measured: 0.2449', MAG),
    (9.6, 6.85, 'Miss: 1.53%', BG),
    (9.6, 6.25, 'Measured: 2.527e-5', MAG),
    (9.6, 5.85, 'Miss: 0.14%', BG),
    (9.6, 5.45, 'Standard: 3.044', MAG),
    (9.6, 5.05, 'Miss: 10.9%', BG),
]
for mx, my, mtxt, mc in meas:
    ax.text(mx, my, mtxt, color=mc, fontsize=8, va='center')

# Chain formula at bottom
ax.text(5.0, 4.4, r'Chain: integers $\rightarrow$ $\Omega_b$ $\rightarrow$ '
        r'$\eta$ $\rightarrow$ BBN $\rightarrow$ primordial abundances',
        ha='center', va='center', color=SILVER, fontsize=11,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM))

ax.text(5.0, 3.7, 'Three physics domains from two gauge integers\n'
        'Falsification: if integers wrong, helium and deuterium predictions break',
        ha='center', va='center', color=DIM, fontsize=9)

save(fig, 'cult15_01_bbn_domain_crossing.png')


# ================================================================
# FIG 2: DOMAIN CROSSING SCALE
# Type: Scale/Landscape (Type 2)
# Shows: Log-scale energy axis from quarks to cosmos with the
#        BBN derivation chain marked at each scale it touches.
#        The physical span of the computation is the claim.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9), facecolor=BG)
style_ax(ax, title='Domain Crossing Scale\nBBN Derivation Spans 25 Orders of Magnitude',
         xlabel='Energy Scale (GeV)', ylabel='')

energies = {
    'Planck': 1.22e19,
    'GUT': 2e16,
    r'$M_Z$': 91.2,
    r'$m_p$': 0.938,
    r'$m_e$': 0.000511,
    'BBN (1 MeV)': 0.001,
    'CMB (0.2 meV)': 2e-13,
    r'$H_0$': 1.5e-42,
}

log_e = {k: np.log10(v) for k, v in energies.items()}

y_base = 0.5
ax.set_xlim(-45, 22)
ax.set_ylim(-0.5, 4.5)

# Main energy axis line
ax.plot([-44, 21], [y_base, y_base], color=DIM, lw=2)

# Landmarks
y_offsets = [1.0, 1.5, 1.0, 1.5, 1.0, 1.5, 1.0, 1.5]
for i, (label, loge) in enumerate(log_e.items()):
    ax.plot([loge, loge], [y_base - 0.1, y_base + 0.1], color=SILVER, lw=1.5)
    yoff = y_base + 0.3 + y_offsets[i]
    ax.plot([loge, loge], [y_base + 0.1, yoff - 0.15], color=DIM, lw=0.8,
            ls='--', alpha=0.5)
    ax.text(loge, yoff, label, ha='center', va='bottom', color=WHITE,
            fontsize=9, fontweight='bold')
    ax.text(loge, yoff - 0.2, '%.0e GeV' % energies[list(energies.keys())[i]],
            ha='center', va='top', color=DIM, fontsize=7)

# BBN chain regions
chain_regions = [
    (np.log10(0.938) - 2, np.log10(91.2) + 2, 'Gauge Integers', BLUE, -0.3),
    (np.log10(2e-13) - 1, np.log10(0.938) + 1, 'Cosmological Bridge', PURPLE, -0.7),
    (np.log10(0.001) - 1.5, np.log10(0.001) + 1.5, 'Nucleosynthesis', MAG, -1.1),
    (np.log10(1.5e-42) - 1, np.log10(2e-13) + 1, r'$H_0$, CMB, $\Omega$', CYAN, -1.5),
]

for x1, x2, label, col, yoff in chain_regions:
    ax.fill_between([x1, x2], [y_base + yoff - 0.12]*2,
                    [y_base + yoff + 0.12]*2,
                    color=col, alpha=0.15)
    ax.plot([x1, x2], [y_base + yoff]*2, color=col, lw=3, alpha=0.7)
    mid = (x1 + x2) / 2
    ax.text(mid, y_base + yoff - 0.25, label, ha='center', va='top',
            color=col, fontsize=9, fontweight='bold')

# Arrow showing full span
ax.annotate('', xy=(-43, -0.3), xytext=(2, -0.3),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(-20, -0.5, 'Full derivation span: 25+ orders of magnitude',
        ha='center', va='top', color=GOLD, fontsize=10)

ax.set_yticks([])

save(fig, 'cult15_02_domain_crossing_scale.png')


# ================================================================
# FIG 3: COMPARISON VERDICT LANDSCAPE
# Type: Comparison Bar Chart (Type 6)
# Shows: All 13 BBN comparisons as horizontal bars on a log scale
#        of miss percentage, with PASS/FAIL/INFO status colored.
#        The falsification surface in one glance.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
style_ax(ax, title='BBN Experiment — Pre-Registered Falsification Surface\n'
         '13 Comparisons, All Declared Before Run',
         xlabel='Miss (log scale)', ylabel='')

comparisons = [
    (r'$\Omega_b$ vs Planck', 0.073, 'INFO', SILVER),
    (r'$\eta$ vs Planck', 0.237, 'INFO', SILVER),
    (r'$\eta_{10}$ vs Planck', 0.237, 'INFO', SILVER),
    (r'$Y_p$ vs measured', 1.528, 'INFO', SILVER),
    (r'$Y_p$ digits', 1.487, 'FAIL', RED),
    ('D/H vs measured', 0.143, 'INFO', SILVER),
    ('D/H digits', 0.024, 'PASS', GREEN),
    (r'$N_{eff}$ range', 0.0, 'PASS', GREEN),
    (r'$N_{eff}$ vs 3.044', 10.9, 'INFO', SILVER),
    (r'$\rho_\Lambda$ GeV$^4$', 10.94, 'INFO', SILVER),
    (r'$\rho_\Lambda$ g/cm$^3$', 0.152, 'INFO', SILVER),
    (r'$Y_p$ chain $<1\sigma$', 0.0, 'PASS', GREEN),
    ('D/H chain $<1\\sigma$', 0.0, 'PASS', GREEN),
]

y_positions = np.arange(len(comparisons))
bar_height = 0.55

for i, (label, miss, status, col) in enumerate(comparisons):
    bar_val = max(miss, 0.005)  # minimum visible bar
    ax.barh(i, np.log10(bar_val) + 3, height=bar_height, left=-1,
            color=col, alpha=0.6, edgecolor=col, linewidth=1.5)

    status_colors = {'PASS': GREEN, 'FAIL': RED, 'INFO': SILVER}
    sc = status_colors.get(status, SILVER)

    ax.text(-1.3, i, label, ha='right', va='center', color=WHITE, fontsize=9)
    ax.text(3.5, i + 0.0, '[%s]' % status, ha='left', va='center',
            color=sc, fontsize=9, fontweight='bold')
    if miss > 0:
        ax.text(3.5 + 1.0, i, '%.3g%%' % miss, ha='left', va='center',
                color=DIM, fontsize=8)

# Threshold lines
ax.axvline(x=np.log10(1.0) + 1, color=ORANGE, ls='--', lw=1.5, alpha=0.6)
ax.text(np.log10(1.0) + 1.05, len(comparisons) - 0.5, '1% miss',
        color=ORANGE, fontsize=8, va='center')
ax.axvline(x=np.log10(0.1) + 1, color=CYAN, ls='--', lw=1.5, alpha=0.4)
ax.text(np.log10(0.1) + 1.05, len(comparisons) - 1.0, '0.1% miss',
        color=CYAN, fontsize=8, va='center')

ax.set_yticks([])
ax.set_ylim(-1, len(comparisons) + 0.5)
ax.set_xlim(-1.5, 5.5)

ax.text(2.0, -0.7, 'Every comparison pre-registered in experiment definition before computation',
        ha='center', va='center', color=DIM, fontsize=9)

save(fig, 'cult15_03_verdict_landscape.png')


# ================================================================
# FIG 4: ANTI-SMUGGLING ARCHITECTURE
# Type: Geometric Cross-Section (Type 4)
# Shows: The boundary between declared dependencies and the value
#        store, with allowed paths drawn and blocked paths marked.
#        The architecture IS the guard.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 9)

ax.set_title('Anti-Smuggling Architecture\nStructural Prevention of Undeclared Inputs',
             color=GOLD, fontsize=16, fontweight='bold', pad=25)

# Value Store (large container on left)
store_box = FancyBboxPatch((0.2, 0.5), 3.5, 7.5, boxstyle='round,pad=0.3',
                           facecolor='#0d0d1f', edgecolor=CYAN, linewidth=2.5)
ax.add_patch(store_box)
ax.text(2.0, 7.7, 'VALUE STORE', ha='center', va='center',
        color=CYAN, fontsize=13, fontweight='bold')
ax.text(2.0, 7.2, '4900+ named nodes', ha='center', va='center',
        color=DIM, fontsize=9)

# Sample values in store
store_vals = [
    ('cosmo_yp_measured_v0', '0.2449', 6.3),
    ('cosmo_dh_measured_v0', '2.527e-5', 5.6),
    ('bbn_yp_a_coeff_v0', '0.2485', 4.9),
    ('geom_pi_v0', r'$\pi$', 4.2),
    ('si_speed_of_light_v0', '299792458', 3.5),
    ('mass_proton_v0', '938.272 MeV', 2.8),
    ('cosmo_h0_planck_v0', '67.4 km/s/Mpc', 2.1),
    ('UNDECLARED_value', '???', 1.2),
]

for key, val, yy in store_vals:
    is_undeclared = 'UNDECLARED' in key
    ec = RED if is_undeclared else DIM
    fc = '#1a0a0a' if is_undeclared else BG
    rect = FancyBboxPatch((0.5, yy - 0.22), 3.0, 0.44,
                          boxstyle='round,pad=0.08',
                          facecolor=fc, edgecolor=ec, linewidth=1)
    ax.add_patch(rect)
    ax.text(0.7, yy, key, color=SILVER if not is_undeclared else RED,
            fontsize=7, va='center', family='monospace')
    ax.text(3.3, yy, val, color=WHITE if not is_undeclared else RED,
            fontsize=8, va='center', ha='right')

# Experiment Definition (middle box)
def_box = FancyBboxPatch((4.5, 3.5), 2.8, 4.5, boxstyle='round,pad=0.3',
                         facecolor='#0d1a0d', edgecolor=GREEN, linewidth=2.5)
ax.add_patch(def_box)
ax.text(5.9, 7.7, 'EXPERIMENT\nDEFINITION', ha='center', va='center',
        color=GREEN, fontsize=12, fontweight='bold')

dep_labels = [
    'dependencies:', 6.8,
    '  cosmo_yp_measured', 6.3,
    '  cosmo_dh_measured', 5.8,
    '  bbn_yp_a_coeff', 5.3,
    '  geom_pi', 4.8,
    '  si_speed_of_light', 4.3,
    '  mass_proton', 3.8,
]
for i in range(0, len(dep_labels), 2):
    txt = dep_labels[i]
    yy = dep_labels[i+1]
    ax.text(4.8, yy, txt, color=GREEN if ':' in txt else BG,
            fontsize=8, va='center', family='monospace')

# Runner (right box)
run_box = FancyBboxPatch((8.0, 4.0), 2.5, 3.5, boxstyle='round,pad=0.3',
                         facecolor='#1a1a0d', edgecolor=GOLD, linewidth=2.5)
ax.add_patch(run_box)
ax.text(9.25, 7.2, 'RUNNER', ha='center', va='center',
        color=GOLD, fontsize=13, fontweight='bold')
ax.text(9.25, 6.6, 'Loads ONLY\ndeclared keys', ha='center', va='center',
        color=BG, fontsize=9)
ax.text(9.25, 5.6, 'Executes\nderivations', ha='center', va='center',
        color=BG, fontsize=9)
ax.text(9.25, 4.8, 'Evaluates\ncomparisons', ha='center', va='center',
        color=BG, fontsize=9)
ax.text(9.25, 4.2, 'Prints\nPASS / FAIL', ha='center', va='center',
        color=BG, fontsize=9)

# Allowed arrows (store -> definition -> runner)
for yy in [6.3, 5.6, 4.9, 4.2, 3.5, 2.8]:
    if yy >= 3.8:
        ax.annotate('', xy=(4.5, min(yy, 6.8)), xytext=(3.5, yy),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, alpha=0.6))

ax.annotate('', xy=(8.0, 5.8), xytext=(7.3, 5.8),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Blocked arrow (undeclared -> runner)
ax.annotate('', xy=(8.0, 1.5), xytext=(3.5, 1.2),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5, ls='--'))

# X mark on blocked arrow
ax.text(5.8, 1.8, r'$\times$  BLOCKED', color=RED, fontsize=14,
        fontweight='bold', va='center', ha='center')
ax.text(5.8, 1.3, 'Undeclared value cannot\nenter derivation', color=RED,
        fontsize=9, va='center', ha='center')

# Bottom annotation
ax.text(5.0, -0.3, 'Smuggling is structurally impossible:\n'
        'the runner has no mechanism to access undeclared values',
        ha='center', va='center', color=DIM, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.5))

save(fig, 'cult15_04_anti_smuggling.png')


# ================================================================
# FIG 5: VERIFICATION COST CURVE
# Type: Running/Convergence Chart (Type 1)
# Shows: Two curves — reader verification time vs number of readers.
#        Current practice: linear (each reader re-derives).
#        Five-layer: flat after initial author cost.
#        The crossover IS the economic argument.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Verification Cost: Current Practice vs Five-Layer Standard',
         xlabel='Number of Independent Readers Verifying the Result',
         ylabel='Total Person-Hours Invested')

readers = np.arange(0, 26)

# Current practice: author writes paper (10h) + each reader re-derives (5h each)
current_author = 10
current_per_reader = 5
current_total = current_author + readers * current_per_reader

# Five-layer: author writes paper (10h) + prepares artifacts (4h) + each reader reruns (0.25h)
layer_author = 14
layer_per_reader = 0.25
layer_total = layer_author + readers * layer_per_reader

ax.plot(readers, current_total, color=RED, lw=2.5, label='Current practice (prose description)')
ax.plot(readers, layer_total, color=GREEN, lw=2.5, label='Five-layer standard (rerunnable artifact)')

# Fill between
ax.fill_between(readers, layer_total, current_total,
                where=current_total > layer_total,
                color=GREEN, alpha=0.06)

# Crossover point
cross_x = (layer_author - current_author) / (current_per_reader - layer_per_reader)
cross_y = current_author + cross_x * current_per_reader
ax.scatter([cross_x], [cross_y], s=200, color=GOLD, edgecolors=WHITE,
           linewidth=2, zorder=10)
ax.annotate('Crossover: %.1f readers' % cross_x,
            xy=(cross_x, cross_y),
            xytext=(cross_x + 4, cross_y + 15),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Annotations at right edge
ax.text(25.5, current_total[-1], '%d hours\n(25 readers)' % current_total[-1],
        color=RED, fontsize=9, va='center')
ax.text(25.5, layer_total[-1] + 4, '%d hours\n(25 readers)' % layer_total[-1],
        color=GREEN, fontsize=9, va='center')

# Savings annotation
savings_at_10 = (current_author + 10*current_per_reader) - (layer_author + 10*layer_per_reader)
ax.annotate('Savings at 10 readers:\n%.0f person-hours' % savings_at_10,
            xy=(10, current_author + 10*current_per_reader),
            xytext=(12, 85),
            color=SILVER, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

ax.set_xlim(-0.5, 27)
ax.set_ylim(0, 145)
ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE,
          fontsize=10, framealpha=0.9)

ax.text(13.5, 5, 'Author overhead: +4 hours to prepare five-layer artifacts\n'
        'Reader savings: 4.75 hours per reader (95% reduction)',
        ha='center', va='center', color=DIM, fontsize=9)

save(fig, 'cult15_05_verification_cost.png')


# ================================================================
# FIG 6: MISS PERCENTAGE DISTRIBUTION
# Type: Threshold/Region Chart (Type 3)
# Shows: All 13 BBN comparisons on a log scale with threshold
#        regions for sub-percent, percent, and >10% miss.
#        The located failure is visible as crossing a threshold.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, title='BBN Experiment — Miss Distribution Across All Comparisons',
         xlabel='Comparison', ylabel='Miss (%)')

miss_data = [
    (r'$\Omega_b$', 0.073, 'INFO'),
    (r'$\eta$', 0.237, 'INFO'),
    (r'$\eta_{10}$', 0.237, 'INFO'),
    (r'$Y_p$ vs meas', 1.528, 'INFO'),
    (r'$Y_p$ digits', 1.487, 'FAIL'),
    ('D/H vs meas', 0.143, 'INFO'),
    ('D/H digits', 0.024, 'PASS'),
    (r'$N_{eff}$ range', 0.001, 'PASS'),
    (r'$N_{eff}$ vs 3.044', 10.9, 'INFO'),
    (r'$\rho_\Lambda$ GeV$^4$', 10.94, 'INFO'),
    (r'$\rho_\Lambda$ g/cm$^3$', 0.152, 'INFO'),
    (r'$Y_p$ $<1\sigma$', 0.001, 'PASS'),
    ('D/H $<1\\sigma$', 0.001, 'PASS'),
]

x = np.arange(len(miss_data))

# Threshold regions
ax.axhspan(0.0005, 0.1, color=GREEN, alpha=0.06)
ax.axhspan(0.1, 1.0, color=CYAN, alpha=0.04)
ax.axhspan(1.0, 100, color=ORANGE, alpha=0.04)

ax.axhline(y=0.1, color=CYAN, ls='--', lw=1, alpha=0.5)
ax.axhline(y=1.0, color=ORANGE, ls='--', lw=1.2, alpha=0.6)
ax.axhline(y=10.0, color=RED, ls='--', lw=1.2, alpha=0.6)

ax.text(len(miss_data) - 0.3, 0.04, 'Sub-0.1%', color=GREEN, fontsize=8,
        ha='right', va='center')
ax.text(len(miss_data) - 0.3, 0.3, '0.1% - 1%', color=CYAN, fontsize=8,
        ha='right', va='center')
ax.text(len(miss_data) - 0.3, 3.0, '1% - 10%', color=ORANGE, fontsize=8,
        ha='right', va='center')
ax.text(len(miss_data) - 0.3, 30.0, '>10%', color=RED, fontsize=8,
        ha='right', va='center')

for i, (label, miss, status) in enumerate(miss_data):
    col = GREEN if status == 'PASS' else (RED if status == 'FAIL' else SILVER)
    val = max(miss, 0.001)
    ax.scatter([i], [val], s=200, color=col, edgecolors=WHITE, linewidth=2, zorder=10)
    # Value label above each point
    y_txt = val * 2.0 if val > 0.01 else val * 4.0
    ax.text(i, y_txt, '%.3g%%' % miss if miss > 0.001 else 'range',
            ha='center', va='bottom', color=col, fontsize=8, fontweight='bold')

ax.set_yscale('log')
ax.set_ylim(0.0005, 80)
ax.set_xlim(-0.8, len(miss_data) - 0.2)
ax.set_xticks(x)
ax.set_xticklabels([d[0] for d in miss_data], rotation=45, ha='right',
                   fontsize=8, color=SILVER)

# Legend area
legend_items = [
    mpatches.Patch(color=GREEN, label='PASS'),
    mpatches.Patch(color=RED, label='FAIL'),
    mpatches.Patch(color=SILVER, label='INFO'),
]
ax.legend(handles=legend_items, loc='upper left', facecolor=PAN,
          edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'cult15_06_miss_distribution.png')

# ================================================================
# FIG 7: BBN PREDICTION VS MEASUREMENT
# Type: Comparison Bar Chart (Type 6)
# Shows: For each BBN quantity, predicted and measured values as
#        paired bars with error bars. The reader sees agreement
#        and the located miss at Y_p.
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(18, 12), facecolor=BG,
                         gridspec_kw={'hspace': 0.55, 'wspace': 0.40})

quantities = [
    {
        'title': r'Baryon Density $\Omega_b$',
        'predicted': 0.049036,
        'measured': 0.0490,
        'meas_unc': 0.0006,
        'miss_pct': 0.073,
    },
    {
        'title': r'Baryon-to-Photon $\eta_{10}$',
        'predicted': 6.0895,
        'measured': 6.104,
        'meas_unc': 0.058,
        'miss_pct': 0.237,
    },
    {
        'title': r'Primordial Helium $Y_p$',
        'predicted': 0.2486,
        'measured': 0.2449,
        'meas_unc': 0.0040,
        'miss_pct': 1.528,
    },
    {
        'title': r'Primordial Deuterium D/H ($\times 10^5$)',
        'predicted': 2.5306,
        'measured': 2.527,
        'meas_unc': 0.030,
        'miss_pct': 0.143,
    },
]

for idx, (axi, q) in enumerate(zip(axes.flat, quantities)):
    style_ax(axi, title=q['title'])

    pred = q['predicted']
    meas = q['measured']
    unc = q['meas_unc']

    # Compute sensible y-axis range: center on mean, span driven by
    # whichever is larger — the pred/meas difference or the uncertainty
    mean_val = (pred + meas) / 2.0
    spread = max(abs(pred - meas), unc) * 6.0
    spread = max(spread, abs(mean_val) * 0.02)  # at least 2% of value
    ymin = mean_val - spread
    ymax = mean_val + spread

    bars = axi.bar([0, 1], [pred, meas], width=0.45, color=[CYAN, MAG],
                   alpha=0.7, edgecolor=[CYAN, MAG], linewidth=2)
    axi.errorbar([1], [meas], yerr=[unc],
                 fmt='none', ecolor=WHITE, elinewidth=2, capsize=8, capthick=2)

    # Value labels just above each bar top
    label_offset = spread * 0.08
    axi.text(0, pred + label_offset, '%.6g' % pred, ha='center', va='bottom',
             color=WHITE, fontsize=11, fontweight='bold')
    axi.text(1, meas + unc + label_offset, '%.6g' % meas, ha='center', va='bottom',
             color=WHITE, fontsize=11, fontweight='bold')

    # Bar category labels below bars
    axi.text(0, ymin + spread * 0.05, 'Predicted\n(from integers)',
             ha='center', va='bottom', color=SILVER, fontsize=9)
    axi.text(1, ymin + spread * 0.05, 'Measured',
             ha='center', va='bottom', color=SILVER, fontsize=9)

    # Miss annotation at top center
    miss_col = RED if q['miss_pct'] > 1.0 else GREEN
    axi.text(0.5, ymax - spread * 0.08,
             'Miss: %.3g%%' % q['miss_pct'], ha='center', va='top',
             color=miss_col, fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=miss_col))

    axi.set_ylim(ymin, ymax)
    axi.set_xlim(-0.55, 1.55)
    axi.set_xticks([])

save(fig, 'cult15_07_prediction_vs_measurement.png')

# ================================================================
# FIG 8: VALUE NODE ANATOMY
# Type: Identity Card (Type 8)
# Shows: A single value store entry dissected with every field
#        labeled and annotated with its purpose. The fundamental
#        data unit of the five-layer standard.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.set_title('Anatomy of a Value Store Node\nThe Fundamental Data Unit of the Five-Layer Standard',
             color=GOLD, fontsize=16, fontweight='bold', pad=25)

# Central node box
node_box = FancyBboxPatch((1.5, 1.0), 5.0, 7.5, boxstyle='round,pad=0.4',
                          facecolor='#0d0d1f', edgecolor=CYAN, linewidth=2.5)
ax.add_patch(node_box)

# Field entries inside box
fields = [
    ('key:', 'cosmo_yp_measured_v0', 7.5, CYAN, BLUE),
    ('canonical:', 'cosmo_yp_measured', 7.0, DIM, BG),
    ('version:', '0', 6.5, DIM, BG),
    ('node_type:', 'value', 6.0, DIM, BG),
    ('value:', '0.2449', 5.3, GOLD, BLUE),
    ('value_type:', 'approximate', 4.8, DIM, BG),
    ('unit:', 'dimensionless', 4.3, DIM, BG),
    ('digits:', '4', 3.8, DIM, BG),
    ('uncertainty:', '0.0040', 3.3, ORANGE, BLUE),
    ('source:', 'Aver, Olive, Skillman 2015', 2.6, MAG, BLUE),
    ('', 'JCAP 07, 011', 2.2, MAG, BG),
    ('tags:', '["cosmology","BBN","helium"]', 1.7, DIM, BG),
    ('notes:', 'Primordial 4He mass fraction', 1.2, DIM, BG),
]

for fname, fval, fy, fcol, vcol in fields:
    if fname:
        ax.text(2.0, fy, fname, color=fcol, fontsize=10,
                fontweight='bold', family='monospace', va='center')
    ax.text(3.7, fy, fval, color=vcol, fontsize=10,
            family='monospace', va='center')

# Annotation arrows pointing to key fields
annotations = [
    ('key', 7.5, 'Unique machine-readable\nidentifier — no ambiguity', CYAN),
    ('value', 5.3, 'The datum itself\nExact fraction or stated precision', GOLD),
    ('uncertainty', 3.3, 'Measurement uncertainty\nEnables proper comparison', ORANGE),
    ('source', 2.6, 'Specific publication\nAnyone can verify', MAG),
]

for label, fy, desc, col in annotations:
    ax.annotate(desc,
                xy=(6.5, fy), xytext=(8.0, fy + 0.3),
                color=col, fontsize=9,
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=col, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                         edgecolor=col, linewidth=1))

# Properties callout at bottom
props = [
    'Named — every value has a unique key',
    'Typed — exact fraction, approximate, integer, boolean',
    'Versioned — schema version tracks changes',
    'Sourced — traceable to original publication',
    'Searchable — tags enable cross-domain queries',
]

for i, prop in enumerate(props):
    y = -0.1 - i * 0.35
    ax.text(4.0, y, prop, color=SILVER, fontsize=9, ha='center', va='center')

# Title for properties
ax.text(4.0, 0.3, 'Five Properties of Every Node:', color=WHITE,
        fontsize=11, fontweight='bold', ha='center', va='center')

# Anti-smuggling note
ax.text(4.0, -2.0, 'If a value is not in the store, the computation cannot access it.\n'
        'The store is the single source of truth for all inputs.',
        color=DIM, fontsize=9, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.5))

ax.set_ylim(-2.5, 9.5)

save(fig, 'cult15_08_value_node_anatomy.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n" + "="*60)
print("CULT-15 Diagrams Complete — 8 figures")
print("="*60)
figs = [
    'cult15_01_bbn_domain_crossing.png',
    'cult15_02_domain_crossing_scale.png',
    'cult15_03_verdict_landscape.png',
    'cult15_04_anti_smuggling.png',
    'cult15_05_verification_cost.png',
    'cult15_06_miss_distribution.png',
    'cult15_07_prediction_vs_measurement.png',
    'cult15_08_value_node_anatomy.png',
]
for f in figs:
    print("  %s" % f)
print("="*60)
