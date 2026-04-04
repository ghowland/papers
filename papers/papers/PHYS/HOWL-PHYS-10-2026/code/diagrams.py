#!/usr/bin/env python3
"""
HOWL PHYS-10 Diagrams — Remainder as Observable
8 figures covering five formal domains, VP thresholds, Brillouin zones,
Berry phase, RG flow, complete enumeration, modular search.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: VP THRESHOLD DECOMPOSITION — INTEGER + CONTINUOUS
# Type: Running/threshold
# Shows: Fermion count (integer) incrementing at each mass threshold,
# with continuous VP running (remainder) accumulating between.
# The discrete + continuous structure IS the quotient-remainder.
# ================================================================

fig, ax = dark_fig("VP Running: Integer Fermion Count + Continuous Remainder",
                   xlabel="Energy scale (GeV, log scale)",
                   ylabel="\u03b1\u207b\u00b9 running contribution (cumulative)")

# Thresholds and running
thresholds = [
    (0.000511, 'm_e', 1, CYAN),
    (0.10566, 'm_\u03bc', 2, BLUE),
    (1.77686, 'm_\u03c4', 3, ORANGE),
]

# Schematic VP contribution curve
E = np.logspace(-4, 2, 500)
vp_running = np.zeros_like(E)

for i, e in enumerate(E):
    contrib = 0
    if e > 0.000511:
        contrib += 0.8 * np.log10(e / 0.000511)
    if e > 0.10566:
        contrib += 0.8 * np.log10(e / 0.10566)
    if e > 1.77686:
        contrib += 0.8 * np.log10(e / 1.77686)
    vp_running[i] = contrib

curve(ax, E, vp_running, 'Cumulative leptonic VP', CYAN, 2.5)

# Threshold lines with integer labels
for mass, label, n_active, color in thresholds:
    ax.plot([mass, mass], [0, 10], color=color, linewidth=2,
            linestyle='--', alpha=0.5)
    ax.text(mass, 9.5, label, fontsize=10, color=color, ha='center',
            fontweight='bold')
    # Integer label
    ax.text(mass * 3, 0.8, 'n = %d' % n_active, fontsize=12, color=color,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))

# Confinement wall
shaded_region(ax, 0.3, 3.0, RED, 0.06)
ax.text(1.0, 8.5, 'Confinement\nwall', fontsize=9, color=RED,
        ha='center', fontweight='bold')

# Decomposition labels
ax.text(0.003, 7.0, 'INTEGER:\nfermion count\n(discrete jumps\nat thresholds)',
        fontsize=10, color=GREEN, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN))

ax.text(30, 5.0, 'REMAINDER:\nlogarithmic running\n(continuous between\nthresholds)',
        fontsize=10, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Arrows from integer to thresholds
for mass, label, n, color in thresholds:
    ax.annotate('', xy=(mass, 1.5), xytext=(mass * 3, 1.0),
                arrowprops=dict(arrowstyle='->', color=color, lw=1, alpha=0.5))

ax.set_xscale('log')
ax.set_xlim(0.0001, 200)
ax.set_ylim(0, 11)

save_fig(fig, 'phys10_01_vp_threshold_decomposition.png')


# ================================================================
# FIG 2: BRILLOUIN ZONE — BAND STRUCTURE WITH ZONE FOLDING
# Type: Running/threshold (distinct)
# Shows: E(k) band structure with zone boundaries. Crystal momentum
# folds back into the first BZ. Zone index = integer, k mod G = remainder.
# ================================================================

fig, ax = dark_fig("Brillouin Zone: Integer Zone Index + Crystal Momentum Remainder",
                   xlabel="Crystal momentum k (units of \u03c0/a)",
                   ylabel="Energy E(k)")

# Simple 1D band structure — free electron model with gaps
k = np.linspace(-3, 3, 600)

# Bands in extended zone
for n in range(-2, 3):
    k_shifted = k - 2 * n
    E_band = k_shifted**2
    # Only plot in the appropriate zone
    mask = (k >= 2 * n - 1) & (k <= 2 * n + 1)
    k_plot = k[mask]
    E_plot = E_band[mask]
    if len(k_plot) > 0:
        curve(ax, k_plot, E_plot, '' if n != 0 else 'Free electron bands', DIM, 1.5,
              alpha=0.3)

# Reduced zone scheme — folded bands
k_bz = np.linspace(-1, 1, 200)
for band in range(4):
    if band == 0:
        E_bz = k_bz**2
        color = CYAN
    elif band == 1:
        E_bz = (np.abs(k_bz) + 1)**2 * 0.9  # approximate with gap
        E_bz = np.where(np.abs(k_bz) < 0.95, E_bz, E_bz * 0.95)
        color = BLUE
    elif band == 2:
        E_bz = (np.abs(k_bz) + 2)**2 * 0.85
        color = GREEN
    else:
        E_bz = (np.abs(k_bz) + 3)**2 * 0.8
        color = ORANGE

    curve(ax, k_bz, E_bz, '', color, 2.5)

# Zone boundaries
for boundary in [-1, 1]:
    ax.plot([boundary, boundary], [0, 18], color=GOLD, linewidth=2.5,
            linestyle='--', alpha=0.7)

ax.text(0, 17, 'First Brillouin Zone', fontsize=12, color=GOLD,
        ha='center', fontweight='bold')

# Band gap markers
ax.annotate('Band gap\n(at zone boundary)', xy=(1, 1.0),
            xytext=(2, 5),
            fontsize=9, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# Decomposition labels
result_box(ax, -2.5, 14,
           'k_total = n \u00b7 G + (k mod G)\n\n'
           'INTEGER: zone index n\nREMAINDER: crystal momentum\n'
           'in first BZ\n\nRemainder determines ALL\nphysical properties',
           GOLD, 9)

ax.set_xlim(-3.2, 3.2)
ax.set_ylim(0, 19)

save_fig(fig, 'phys10_02_brillouin_zone.png')


# ================================================================
# FIG 3: ALL FIVE DOMAINS AS GEOMETRIC PANELS
# Type: Multi-panel geometric
# Shows: Five small panels each showing the quotient-remainder
# decomposition for its domain. The common pattern is the finding.
# ================================================================

fig = plt.figure(figsize=(18, 10), facecolor=BG)

domains = [
    ('Berry Phase', '\u03b3 = 2\u03c0n + R', '2\u03c0', 'Winding n', 'Geometric phase R'),
    ('Brillouin Zone', 'k = nG + R', '2\u03c0/a', 'Zone index n', 'Crystal momentum R'),
    ('Bohr-Sommerfeld', '\u222ep\u00b7dq = 2\u03c0\u0127(n+\u03bc/4)', '2\u03c0\u0127', 'Quantum number n', 'Maslov correction \u03bc/4'),
    ('Chern-Simons', 'CS = n + R', '1', 'Chern number n', 'Fractional CS mod \u2124'),
    ('Theta Vacuum', '\u03b8 \u2208 [0,2\u03c0)', '2\u03c0', 'Instanton \u03bd \u2208 \u2124', 'Vacuum angle \u03b8'),
]

for idx, (title, formula, modulus, integer_label, remainder_label) in enumerate(domains):
    ax = fig.add_subplot(1, 5, idx + 1)
    ax.set_facecolor(BG)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-2.5, 2.5)
    ax.axis('off')

    colors_domain = [CYAN, BLUE, GREEN, ORANGE, MAG]
    color = colors_domain[idx]

    # Simple circle representing the modular structure
    circle = plt.Circle((0, 0.5), 0.8, fill=False, edgecolor=color,
                          linewidth=2, zorder=3)
    ax.add_patch(circle)

    # A point on the circle (the remainder)
    angle = np.pi / 4 + idx * 0.4
    px = 0.8 * np.cos(angle)
    py = 0.5 + 0.8 * np.sin(angle)
    data_point(ax, px, py, '', GOLD, size=150)

    # Integer winding indicator
    if idx < 4:
        arc = np.linspace(0, 2 * np.pi * 0.85, 50)
        ax.plot(0.5 * np.cos(arc), 0.5 + 0.5 * np.sin(arc), color=DIM,
                linewidth=1, alpha=0.3)
        ax.text(0, 0.5, 'n', fontsize=10, color=DIM, ha='center')

    # Title
    ax.text(0, 2.2, title, fontsize=10, color=color, ha='center',
            fontweight='bold')

    # Formula
    ax.text(0, -1.0, formula, fontsize=8, color=WHITE, ha='center',
            fontfamily='monospace')

    # Modulus
    ax.text(0, -1.5, 'mod: %s' % modulus, fontsize=7, color=SILVER, ha='center')

    # Integer
    ax.text(0, -1.9, 'Int: %s' % integer_label, fontsize=6, color=GREEN, ha='center')

    # Remainder
    ax.text(0, -2.3, 'Rem: %s' % remainder_label, fontsize=6, color=GOLD, ha='center')

fig.suptitle('Five Domains, One Pattern: Integer = Protected, Remainder = Observable',
             fontsize=16, color=GOLD, fontweight='bold', y=0.98)

path = os.path.join(get_outdir(), 'phys10_03_five_domains.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys10_03_five_domains.png")


# ================================================================
# FIG 4: COMPLETE ENUMERATION — FOUR TIERS OF CONSTANTS
# Type: Scale/hierarchy
# Shows: Pure integers (top), simple rationals, Q335 transcendentals,
# measured tier-3. The inventory of everything physics uses.
# ================================================================

fig, ax = dark_canvas("The Complete Inventory: What Physics Uses",
                      size=(18, 14))
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 12)

# Four tiers top to bottom
tiers = [
    (10.5, 'TIER 0: PURE INTEGERS', GREEN,
     '1, 2, 3, 4, 5, 6, 7, 8, 11, 19, 41, 109, 197, 218',
     'Counting, gauge groups, Casimirs, beta slopes'),
    (8.0, 'TIER 1: SIMPLE RATIONALS', CYAN,
     '1/2, 1/3, 2/3, 3/4, 5/6, 197/144, 41/10, \u221219/6, \u22127',
     'QED coefficients, VP constants, beta functions'),
    (5.5, 'TIER 2: Q335 TRANSCENDENTALS (34 constants)', BLUE,
     '\u03c0, e, ln(2), \u221a2, \u03c6, \u03b6(3), \u03b6(5), Li\u2084(\u00bd), K(k\u00b2), ...',
     'Integer pairs at 100+ digits, shared denominator 2\u00b3\u00b3\u2075'),
    (3.0, 'TIER 3: MEASURED FROM THE UNIVERSE', ORANGE,
     '\u03b1\u207b\u00b9 = 137.036, \u03b1_s = 0.118, sin\u00b2\u03b8_W = 0.231, m_e, m_\u03bc, ...',
     '17 dimensionless ratios (after \u03b8_QCD = 0 and Koide)'),
]

for y, title, color, examples, description in tiers:
    # Box
    rect = plt.Rectangle((0.5, y - 0.8), 9.0, 1.6,
                           facecolor=color, alpha=0.05, edgecolor=color,
                           linewidth=2, zorder=2)
    ax.add_patch(rect)

    ax.text(5.0, y + 0.4, title, fontsize=13, color=color,
            ha='center', fontweight='bold')
    ax.text(5.0, y - 0.1, examples, fontsize=9, color=WHITE,
            ha='center', fontfamily='monospace')
    ax.text(5.0, y - 0.5, description, fontsize=8, color=SILVER,
            ha='center', style='italic')

# Arrows showing relationship
for i in range(3):
    y_top = tiers[i][0] - 0.8
    y_bot = tiers[i + 1][0] + 0.8
    ax.annotate('', xy=(5.0, y_bot), xytext=(5.0, y_top),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, alpha=0.4))

# Key relationships
ax.text(8.5, 9.3, 'Laws use\nTiers 0-2', fontsize=9, color=GREEN,
        fontweight='bold')
ax.text(8.5, 4.0, 'Universe\nsupplies\nTier 3', fontsize=9, color=ORANGE,
        fontweight='bold')

# The dividing line
ax.plot([0.5, 9.5], [4.3, 4.3], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.6)
ax.text(9.0, 4.5, 'THE LINE\nAbove: math provides.\nBelow: universe provides.',
        fontsize=9, color=GOLD, ha='right', fontweight='bold')

# Bottom
ax.text(5.0, 0.2, 'The quotient-remainder decomposition operates on Tiers 0-2.\n'
        'The modulus connecting Tier 2 to Tier 3 is the open question.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys10_04_complete_enumeration.png')


# ================================================================
# FIG 5: BERRY PHASE — ACCUMULATING AROUND A LOOP
# Type: Geometric
# Shows: A quantum system transported around a parameter space loop,
# accumulating geometric phase. Integer windings are invisible;
# the remainder IS the observable.
# ================================================================

fig, ax = dark_canvas("Berry Phase: The Remainder Is the Observable",
                      size=(14, 14))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

# Parameter space loop
loop = plt.Circle((0, 0), 1.5, fill=False, edgecolor=CYAN,
                    linewidth=2.5, zorder=3)
ax.add_patch(loop)
ax.text(0, 0, 'Parameter\nspace\nloop', fontsize=10, color=DIM,
        ha='center', va='center')

# Phase accumulation — spiral around the loop
n_winds = 2  # integer windings
remainder_frac = 0.35  # fractional remainder
total_angle = (n_winds + remainder_frac) * 2 * np.pi

t = np.linspace(0, total_angle, 500)
r_spiral = 1.5 + 0.15 * np.sin(8 * t)  # slight modulation for visibility
x_spiral = r_spiral * np.cos(t / (n_winds + remainder_frac))
y_spiral = r_spiral * np.sin(t / (n_winds + remainder_frac))

# Color-code: gray for integer windings, gold for remainder
n_int_pts = int(len(t) * n_winds / (n_winds + remainder_frac))
ax.plot(x_spiral[:n_int_pts], y_spiral[:n_int_pts], color=DIM,
        linewidth=2, alpha=0.4, zorder=4)
ax.plot(x_spiral[n_int_pts:], y_spiral[n_int_pts:], color=GOLD,
        linewidth=3, zorder=5)

# Start point
data_point(ax, x_spiral[0], y_spiral[0], '', GREEN, size=200)
ax.text(x_spiral[0] + 0.2, y_spiral[0] + 0.2, 'Start', fontsize=9,
        color=GREEN, fontweight='bold')

# End point
data_point(ax, x_spiral[-1], y_spiral[-1], '', GOLD, size=250)

# Labels
ax.text(0, 2.2, 'n = %d complete windings' % n_winds, fontsize=11,
        color=DIM, ha='center', style='italic')
ax.text(0, -2.0, 'REMAINDER = 0.35 \u00d7 2\u03c0', fontsize=13,
        color=GOLD, ha='center', fontweight='bold')
ax.text(0, -2.4, 'This is the Berry phase. This is the observable.',
        fontsize=10, color=GOLD, ha='center')

# Decomposition
result_box(ax, -2.0, -1.2,
           '\u03b3 = 2\u03c0 \u00d7 2 + 0.35\u00d72\u03c0\n'
           'Integer (invisible)\n+ Remainder (observable)',
           CYAN, 9)

save_fig(fig, 'phys10_05_berry_phase.png')


# ================================================================
# FIG 6: RG FLOW — COUPLING RUNNING TOWARD FIXED POINT
# Type: Running/convergence
# Shows: Coupling g(mu) running toward fixed point g*. Decomposed
# into g* (reference, "integer analog") and displacement g - g*.
# The flow direction determines the phase of matter.
# ================================================================

fig, ax = dark_fig("RG Flow: Fixed Point + Displacement (Analogous Domain)",
                   xlabel="Energy scale \u03bc (log)",
                   ylabel="Coupling g(\u03bc)")

mu = np.linspace(0, 10, 500)

# Two trajectories approaching fixed point from different sides
g_star = 3.5
g_above = g_star + 2.0 * np.exp(-0.5 * mu)
g_below = g_star - 1.5 * np.exp(-0.5 * mu)

curve(ax, mu, g_above, 'g > g*: flows toward fixed point', ORANGE, 2.5)
curve(ax, mu, g_below, 'g < g*: flows toward fixed point', CYAN, 2.5)

# Fixed point line
ax.plot([0, 10], [g_star, g_star], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(10.3, g_star, 'g* = fixed point\n("integer analog")', fontsize=10,
        color=GOLD, va='center', fontweight='bold')

# Displacement arrows
ax.annotate('', xy=(2, g_star), xytext=(2, g_above[int(2 / 10 * 500)]),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(2.5, (g_star + g_above[int(2 / 10 * 500)]) / 2,
        'g \u2212 g*\n(displacement\n= "remainder")',
        fontsize=9, color=RED, fontweight='bold')

# Phase labels
shaded_region_h(ax, g_star + 0.1, 6.0, ORANGE, 0.04)
shaded_region_h(ax, 1.5, g_star - 0.1, CYAN, 0.04)

ax.text(8, 5.5, 'Phase A\n(g > g*)', fontsize=9, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(8, 2.2, 'Phase B\n(g < g*)', fontsize=9, color=CYAN,
        ha='center', fontweight='bold')

# Key distinction
result_box(ax, 5, 1.0,
           'ANALOGOUS, not formal:\ng* is NOT topologically protected.\n'
           'It can change continuously if\nthe theory content changes.\n'
           'But the decomposition is\nphysically meaningful.',
           SILVER, 9)

ax.set_xlim(-0.5, 11)
ax.set_ylim(1.0, 6.5)

legend(ax, loc='upper right')

save_fig(fig, 'phys10_06_rg_flow.png')


# ================================================================
# FIG 7: ALPHA^-1 MOD ZETA(3) — MOST NOTABLE MODULAR HIT
# Type: Scale/comparison
# Shows: alpha^-1 = 114 * zeta(3) + 0.00151. The quotient 114
# and the tiny remainder on a number line.
# ================================================================

fig, ax = dark_fig("\u03b1\u207b\u00b9 mod \u03b6(3): The Most Notable Modular Hit",
                   xlabel="",
                   ylabel="")

# Number line showing the decomposition
# alpha^-1 = 114 * zeta(3) + 0.00151
# zeta(3) = 1.20206
# 114 * zeta(3) = 137.03448
# remainder = 0.00151

# Visual: zoom in on the region around 137.035
ax.plot([136.5, 137.6], [2.0, 2.0], color=DIM, linewidth=2, alpha=0.5)

# Tick marks for multiples of zeta(3) near 137
for mult in [113, 114]:
    val = mult * 1.20206
    ax.plot([val, val], [1.7, 2.3], color=CYAN, linewidth=2)
    ax.text(val, 1.3, '%d\u00b7\u03b6(3)\n= %.3f' % (mult, val), fontsize=9,
            color=CYAN, ha='center')

# Alpha^-1
alpha_inv = 137.036
ax.plot([alpha_inv, alpha_inv], [1.5, 2.5], color=GOLD, linewidth=3)
data_point(ax, alpha_inv, 2.0, '', GOLD, size=400)
ax.text(alpha_inv, 2.8, '\u03b1\u207b\u00b9 = 137.036', fontsize=14,
        color=GOLD, ha='center', fontweight='bold')

# The remainder
val_114 = 114 * 1.20206
ax.annotate('', xy=(alpha_inv, 3.5), xytext=(val_114, 3.5),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text((alpha_inv + val_114) / 2, 3.8,
        'Remainder = 0.00151\n(0.13% of \u03b6(3))',
        fontsize=11, color=RED, ha='center', fontweight='bold')

# The quotient
ax.text(136.8, 4.5, 'Quotient: 114 = 2 \u00d7 3 \u00d7 19', fontsize=12,
        color=CYAN, fontweight='bold')

# Statistical assessment
result_box(ax, 137.0, 0.5,
           'Visually striking but NOT statistically significant.\n'
           'Expected near-hits at 0.13% level: ~1 across 17 targets.\n'
           'Observed: 1.  PSLQ on residual 0.00151: NULL.\n'
           'The remainder does not decompose into the basis.',
           SILVER, 9)

ax.set_xlim(136.4, 137.7)
ax.set_ylim(-0.3, 5.5)
ax.set_yticks([])

save_fig(fig, 'phys10_07_alpha_mod_zeta3.png')


# ================================================================
# FIG 8: PHYS-10 IDENTITY CARD
# Type: Identity card
# Shows: Five domains, Q335 tool, null search, remainder = observable.
# ================================================================

fig, ax = dark_canvas("PHYS-10 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'REMAINDER AS OBSERVABLE', fontsize=20,
        color=GOLD, ha='center', fontweight='bold')

# Left column: five domains
ax.text(2.5, 8.0, 'FIVE FORMAL DOMAINS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

domain_list = [
    ('Berry phase', '2\u03c0', 'Hall conductance', CYAN),
    ('Brillouin zone', '2\u03c0/a', 'Band structure', BLUE),
    ('Bohr-Sommerfeld', '2\u03c0\u0127', 'Energy levels', GREEN),
    ('Chern-Simons', '1', 'Fractional statistics', ORANGE),
    ('Theta vacuum', '2\u03c0', '\u03b8 = 0 (PHYS-7)', MAG),
]

for i, (name, modulus, observable, color) in enumerate(domain_list):
    y = 7.0 - i * 0.7
    ax.text(0.5, y, name, fontsize=9, color=color, fontweight='bold')
    ax.text(2.5, y, 'mod %s' % modulus, fontsize=8, color=SILVER, ha='center')
    ax.text(4.2, y, '\u2192 %s' % observable, fontsize=8, color=DIM)

# Common pattern
ax.text(2.5, 3.5, 'Common pattern:\nInteger = protected\nRemainder = observable\n'
        'Modulus = symmetry', fontsize=10, color=GOLD, ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Right column: the tool and the search
ax.text(7.5, 8.0, 'Q335 TOOL', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')
ax.text(7.5, 7.2, 'C = p / 2\u00b3\u00b3\u2075\nq = \u230ap_X / p_C\u230b\nr = p_X \u2212 q\u00b7p_C\n\n'
        'Exact integer division\non 100-digit numerators.\nNo rounding at any step.',
        fontsize=9, color=SILVER, ha='center')

ax.text(7.5, 4.8, 'THE SEARCH', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

search_items = [
    ('17 SM targets', '\u00d7 34 moduli', CYAN),
    ('51 PSLQ tests', 'maxcoeff 10,000', BLUE),
    ('Result:', 'ALL NULL', RED),
]
for i, (item, detail, color) in enumerate(search_items):
    y = 4.0 - i * 0.6
    ax.text(6.5, y, item, fontsize=10, color=color, fontweight='bold')
    ax.text(8.5, y, detail, fontsize=10, color=SILVER)

# Bottom
ax.plot([0.5, 9.5], [1.5, 1.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5.0, 1.0, 'The structure is proven. The tool is demonstrated. The search is reported.',
        fontsize=12, color=GOLD, ha='center', fontweight='bold')
ax.text(5.0, 0.4, 'The modulus connecting integer arithmetic to SM parameters\n'
        'is not any single basis constant. The search space is bounded, not closed.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys10_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-10 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys10_01_vp_threshold_decomposition.png',
    'phys10_02_brillouin_zone.png',
    'phys10_03_five_domains.png',
    'phys10_04_complete_enumeration.png',
    'phys10_05_berry_phase.png',
    'phys10_06_rg_flow.png',
    'phys10_07_alpha_mod_zeta3.png',
    'phys10_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    