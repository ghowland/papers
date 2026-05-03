#!/usr/bin/env python3
"""
HOWL ENG-01 Diagrams — What Engineering Is
8 figures covering the structural definition of engineering and its consequences.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Wedge
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

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

def style_axes(ax):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

# ================================================================
# FIG 1: REMOVAL TEST MATRIX
# Type: 6 (Comparison Bar Chart)
# Shows: each clause's load-bearing weight by what survives if removed
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

clauses = [
    'Evaluating\ntrade-offs',
    'Alignment of\nvariables/constants',
    'Efficiently',
    'Meet goals',
    'Against\nexternalities',
    'True Cost\non failure',
]
collapses_to = [
    'Execution / trades',
    'Opinion / preference',
    'Brute force',
    'Structure-fitting',
    'Pure mathematics',
    'Academic exercise',
]
severity = [9, 8, 7, 7, 10, 10]
colors = [ORANGE, ORANGE, CYAN, CYAN, RED, RED]

y_pos = np.arange(len(clauses))
bars = ax.barh(y_pos, severity, color=colors, alpha=0.7,
               edgecolor=colors, linewidth=2)

for i, (sev, collapse) in enumerate(zip(severity, collapses_to)):
    ax.text(sev + 0.2, i, '\u2192 ' + collapse,
            va='center', ha='left', fontsize=11, color=WHITE)
    ax.text(0.15, i, str(sev) + '/10',
            va='center', ha='left', fontsize=10, color=BG, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(clauses, color=WHITE, fontsize=11)
ax.set_xlabel('Severity of Definition Collapse if Clause Removed',
              color=SILVER, fontsize=12)
ax.set_xlim(0, 18)
ax.set_ylim(-0.6, len(clauses) - 0.4)
ax.invert_yaxis()
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.axvline(10, color=DIM, linestyle='--', linewidth=1, alpha=0.5)
ax.text(10.05, -0.45, 'maximum', fontsize=8, color=DIM)

ax.set_title('Removal Test: Each Clause is Load-Bearing',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)
ax.text(9, 6.3,
        'Drop any clause and engineering collapses into a different activity.',
        ha='center', fontsize=10, color=SILVER, style='italic')

save(fig, 'eng01_01_removal_test_matrix.png')

# ================================================================
# FIG 2: ACTIVITY LANDSCAPE ON TWO AXES
# Type: 3 (Threshold/Region Chart)
# Shows: where each activity sits in (externality presence) x (True Cost) space
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

# Engineering region (high externality, high True Cost)
ax.axhspan(6, 10, xmin=0.6, xmax=1.0, alpha=0.10, color=GOLD, zorder=0)
# Math region (low externality, low True Cost)
ax.axhspan(0, 4, xmin=0.0, xmax=0.4, alpha=0.10, color=BLUE, zorder=0)
# Trades region (high externality, low True Cost — execution layer)
ax.axhspan(0, 4, xmin=0.6, xmax=1.0, alpha=0.10, color=GREEN, zorder=0)
# Academic / exercise (mid externality, low cost)
ax.axhspan(0, 4, xmin=0.4, xmax=0.6, alpha=0.08, color=PURPLE, zorder=0)

ax.text(8.2, 8.5, 'ENGINEERING', fontsize=14, color=GOLD,
        fontweight='bold', alpha=0.9)
ax.text(1.5, 1.5, 'MATH', fontsize=14, color=BLUE,
        fontweight='bold', alpha=0.9)
ax.text(8.2, 1.5, 'TRADES', fontsize=14, color=GREEN,
        fontweight='bold', alpha=0.9)
ax.text(4.7, 1.5, 'ACADEMIC', fontsize=12, color=PURPLE,
        fontweight='bold', alpha=0.9)

# Activities as points
activities = [
    # (name, ext, cost, color)
    ('Pure crypto', 1.5, 1.2, BLUE),
    ('Lamport: Paxos proof', 2.5, 1.8, BLUE),
    ('Iteration', 1.0, 0.7, BLUE),
    ('Textbook bridge', 4.5, 1.5, PURPLE),
    ('Class Paxos impl', 5.0, 2.2, PURPLE),
    ('Cabling concrete', 8.5, 2.0, GREEN),
    ('Concrete pour', 9.0, 2.5, GREEN),
    ('CRUD app', 7.0, 2.3, GREEN),
    ('Senior ops on prod', 9.2, 8.5, GOLD),
    ('Therac-25 (failed)', 9.5, 9.5, RED),
    ('Quake netcode', 8.5, 7.0, GOLD),
    ('Spanner / Bigtable', 9.0, 8.8, GOLD),
    ('Applied crypto / TLS', 8.8, 8.0, GOLD),
    ('Unix / C', 8.0, 7.2, GOLD),
    ('Raft impl', 8.5, 7.8, GOLD),
]

for name, x, y, c in activities:
    ax.scatter(x, y, s=180, color=c, edgecolors=WHITE,
               linewidth=1.5, zorder=5, alpha=0.9)
    ax.annotate(name, xy=(x, y), xytext=(x + 0.15, y + 0.22),
                fontsize=9, color=WHITE)

ax.set_xlabel('Externalities Push Back  \u2192',
              color=SILVER, fontsize=12)
ax.set_ylabel('True Cost on Failure  \u2192',
              color=SILVER, fontsize=12)
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 10.5)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_yticks([0, 2, 4, 6, 8, 10])

ax.set_title('Activity Landscape: Engineering Occupies One Quadrant',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng01_02_activity_landscape.png')

# ================================================================
# FIG 3: SWE VELOCITY vs OPS STABILITY — COST SURFACES
# Type: 3 (Threshold/Region Chart)
# Shows: where internal-cost optimization diverges from True-Cost optimization
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

# X axis: shipping velocity (low to high)
# Y axis: cost (arbitrary units)
x = np.linspace(0, 10, 200)

# Internal cost: low when shipping fast, high when shipping slow
# (this is what SWE leadership feels: "we're behind schedule")
internal_cost = 8.0 * np.exp(-0.4 * x) + 0.5

# True cost: low when shipping safely, rises sharply when velocity exceeds capacity
# (this is what Ops sees: outages, data loss, revenue hit)
true_cost = 0.5 + 0.05 * x + 0.03 * np.maximum(0, x - 4) ** 2.5

ax.plot(x, internal_cost, color=BLUE, linewidth=2.5,
        label='Internal cost (felt by SWE leadership)')
ax.plot(x, true_cost, color=RED, linewidth=2.5,
        label='True Cost (paid by users / business)')

# Crossover region
crossover_idx = np.argmin(np.abs(internal_cost - true_cost))
crossover_x = x[crossover_idx]

# Aligned region (left of crossover)
ax.axvspan(0, crossover_x, alpha=0.06, color=GREEN, zorder=0)
# Diverged region (right of crossover)
ax.axvspan(crossover_x, 10, alpha=0.06, color=ORANGE, zorder=0)

ax.axvline(crossover_x, color=DIM, linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(crossover_x + 0.1, 9.0, 'crossover',
        fontsize=9, color=DIM, rotation=90, va='top')

ax.text(crossover_x / 2, 9.3, 'aligned: both costs agree',
        ha='center', fontsize=10, color=GREEN, fontweight='bold')
ax.text((crossover_x + 10) / 2, 9.3,
        'diverged: orgs choose which cost matters',
        ha='center', fontsize=10, color=ORANGE, fontweight='bold')

# Annotation showing the engineering position
ax.annotate('Ops gates here:\nTrue Cost rising',
            xy=(7.5, true_cost[150]),
            xytext=(5.5, 7.0),
            fontsize=10, color=WHITE,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED),
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))

ax.annotate('SWE leadership\nfeels pressure here',
            xy=(1.0, internal_cost[20]),
            xytext=(2.5, 5.5),
            fontsize=10, color=WHITE,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=BLUE),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.2))

ax.set_xlabel('Shipping Velocity  \u2192',
              color=SILVER, fontsize=12)
ax.set_ylabel('Cost (arbitrary units)',
              color=SILVER, fontsize=12)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

leg = ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
                labelcolor=WHITE, fontsize=10)

ax.set_title('Two Cost Surfaces: Internal Pressure vs True Cost',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng01_03_swe_ops_cost_surfaces.png')

# ================================================================
# FIG 4: SUBSTRATE-BITES THRESHOLD
# Type: 1 (Running/Convergence Chart)
# Shows: engineering content rises with how hard the substrate pushes back
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

x = np.linspace(0, 10, 200)
# Engineering content: low for soft substrates, rises sharply, saturates at extreme
eng_content = 100 / (1 + np.exp(-1.0 * (x - 5)))

ax.plot(x, eng_content, color=GOLD, linewidth=2.8,
        label='Engineering content of role')

# Region shading
ax.axvspan(0, 3, alpha=0.07, color=BLUE, zorder=0)
ax.axvspan(3, 6, alpha=0.07, color=PURPLE, zorder=0)
ax.axvspan(6, 10, alpha=0.07, color=GOLD, zorder=0)

ax.text(1.5, 95, 'forgiving substrate', ha='center',
        fontsize=10, color=BLUE, fontweight='bold')
ax.text(4.5, 95, 'mixed', ha='center',
        fontsize=10, color=PURPLE, fontweight='bold')
ax.text(8.0, 95, 'unforgiving substrate', ha='center',
        fontsize=10, color=GOLD, fontweight='bold')

# Plot example roles at their substrate-pressure x-values
roles = [
    ('CRUD app dev', 1.0, BLUE),
    ('Framework user', 1.8, BLUE),
    ('Backend service SWE', 3.2, PURPLE),
    ('Performance engineer', 6.0, PURPLE),
    ('DB internals', 7.8, GOLD),
    ('Senior ops at scale', 8.5, GOLD),
    ('Embedded / RT', 9.0, GOLD),
    ('Safety-critical', 9.5, GOLD),
]

for name, xv, c in roles:
    yv = 100 / (1 + np.exp(-1.0 * (xv - 5)))
    ax.scatter(xv, yv, s=180, color=c, edgecolors=WHITE,
               linewidth=1.5, zorder=5)
    ax.annotate(name, xy=(xv, yv), xytext=(xv + 0.1, yv - 4.5),
                fontsize=9, color=WHITE)

ax.set_xlabel('How Hard the Substrate Pushes Back  \u2192',
              color=SILVER, fontsize=12)
ax.set_ylabel('Engineering Content of the Work (%)',
              color=SILVER, fontsize=12)
ax.set_xlim(0, 10)
ax.set_ylim(0, 105)

ax.set_title('Engineering Content Tracks Substrate Pressure',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng01_04_substrate_threshold.png')

# ================================================================
# FIG 5: SWE EXAMPLES ON SUBSTRATE LANDSCAPE
# Type: 2 (Scale/Landscape Diagram)
# Shows: the paper's SWE examples placed on a substrate-pressure axis
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
style_axes(ax)

# Horizontal landscape: log-style spacing of substrate severity
examples = [
    # (name, position, true_cost_marker_size, color, year)
    ('Iteration\n(math)', 0.5, 80, BLUE, 'algorithm'),
    ('Lamport: Paxos\nas proof', 1.5, 100, BLUE, '1989'),
    ('Engelbart NLS\n+ remote demo', 4.5, 350, GOLD, '1968'),
    ('Unix / C', 5.5, 400, GOLD, '1969-73'),
    ('Quake netcode', 6.3, 380, GOLD, '1996'),
    ('Raft\n(implementable)', 7.0, 360, GOLD, '2014'),
    ('Acton: DOD\n(16ms wall)', 7.8, 420, GOLD, '2014'),
    ('MapReduce /\nSpanner', 8.5, 480, GOLD, '2004+'),
    ('Therac-25\n(failed)', 9.5, 600, RED, '1985-87'),
]

for name, xv, sz, c, year in examples:
    ax.scatter(xv, 0.5, s=sz, color=c, edgecolors=WHITE,
               linewidth=2, zorder=5, alpha=0.85)
    ax.text(xv, 0.78, name, ha='center', va='bottom',
            fontsize=10, color=WHITE)
    ax.text(xv, 0.22, year, ha='center', va='top',
            fontsize=8, color=DIM, style='italic')

# Horizontal axis line
ax.plot([0, 10], [0.5, 0.5], color=DIM, linewidth=0.8, alpha=0.5, zorder=1)

# Region labels
ax.axvspan(0, 3, alpha=0.06, color=BLUE, zorder=0)
ax.axvspan(3, 7, alpha=0.06, color=GOLD, zorder=0)
ax.axvspan(7, 10, alpha=0.10, color=GOLD, zorder=0)

ax.text(1.5, 0.95, 'MATH', ha='center', fontsize=11,
        color=BLUE, fontweight='bold')
ax.text(5.0, 0.95, 'ENGINEERING', ha='center', fontsize=11,
        color=GOLD, fontweight='bold')
ax.text(8.5, 0.95, 'EXTREME-COST ENGINEERING', ha='center',
        fontsize=11, color=GOLD, fontweight='bold')

# Legend for marker size
ax.text(0.2, 0.06,
        'marker size  =  True Cost magnitude',
        fontsize=9, color=SILVER, style='italic')

ax.set_xlabel('Substrate Pressure  \u2192  (forgiving \u2192 unforgiving)',
              color=SILVER, fontsize=12)
ax.set_xlim(-0.3, 10.3)
ax.set_ylim(0, 1.05)
ax.set_yticks([])
ax.set_xticks([])

ax.set_title('SWE Examples Placed on the Substrate Landscape',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng01_05_examples_landscape.png')

# ================================================================
# FIG 6: BRIDGE SUPPORT ANGLE — ALIGNMENT BASIN
# Type: 1 (Running/Convergence Chart)
# Shows: structural integrity vs angle, with steep falloff away from 90 degrees
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

angles = np.linspace(80, 100, 400)
# Integrity: gaussian-shaped basin centered at 90, with sharp dropoff
integrity = 100 * np.exp(-0.5 * ((angles - 90) / 1.2) ** 2)

ax.plot(angles, integrity, color=GOLD, linewidth=2.8,
        label='Structural integrity (% of design load)')

# Mark the 90-degree alignment peak
ax.axvline(90, color=GREEN, linestyle='-', linewidth=1.5, alpha=0.7)
ax.scatter([90], [100], s=250, color=GREEN, edgecolors=WHITE,
           linewidth=2, zorder=5)
ax.annotate('90\u00b0: aligned\nwith gravity',
            xy=(90, 100), xytext=(92.5, 92),
            fontsize=11, color=WHITE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2))

# Mark the failure points
fail_threshold = 50
ax.axhline(fail_threshold, color=RED, linestyle='--', linewidth=1.2, alpha=0.6)
ax.text(80.3, fail_threshold + 1.5, 'collapse threshold',
        fontsize=9, color=RED)

# Mark 89 and 91 degrees with their integrity values
for ang in [89, 91]:
    integ = 100 * np.exp(-0.5 * ((ang - 90) / 1.2) ** 2)
    ax.scatter([ang], [integ], s=180, color=ORANGE,
               edgecolors=WHITE, linewidth=1.5, zorder=5)
    ax.annotate('%d\u00b0: %.0f%%' % (ang, integ),
                xy=(ang, integ), xytext=(ang + (1.0 if ang > 90 else -3.0), integ - 12),
                fontsize=10, color=WHITE,
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1))

# Failure region shading
ax.fill_between(angles, 0, integrity, where=(integrity < fail_threshold),
                color=RED, alpha=0.12, zorder=0)

ax.text(82.5, 30, 'misaligned:\nfails',
        ha='center', fontsize=10, color=RED, fontweight='bold')
ax.text(97.5, 30, 'misaligned:\nfails',
        ha='center', fontsize=10, color=RED, fontweight='bold')

ax.set_xlabel('Support Angle (degrees)', color=SILVER, fontsize=12)
ax.set_ylabel('Structural Integrity (%)', color=SILVER, fontsize=12)
ax.set_xlim(80, 100)
ax.set_ylim(0, 110)

ax.set_title('Alignment is a Narrow Basin: 90\u00b0 vs 89\u00b0',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng01_06_bridge_alignment_basin.png')

# ================================================================
# FIG 7: ENGINEERING IDENTITY CARD
# Type: 8 (Identity Card) — one per paper
# Shows: definition, the 5 clauses, the True Cost asymmetry, the 3 tests
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title bar
ax.text(5.0, 9.5, 'ENGINEERING — STRUCTURAL DEFINITION',
        ha='center', fontsize=17, color=GOLD, fontweight='bold')

# The defining sentence in a panel
def_box = FancyBboxPatch((0.5, 7.8), 9.0, 1.2,
                          boxstyle='round,pad=0.1',
                          facecolor=PAN, edgecolor=GOLD, linewidth=2)
ax.add_patch(def_box)
ax.text(5.0, 8.55,
        '"Engineering is evaluating trade-offs to find alignment of variables and constants',
        ha='center', fontsize=12, color=WHITE, style='italic')
ax.text(5.0, 8.20,
        'that efficiently meet goals against externalities where failure has a True Cost."',
        ha='center', fontsize=12, color=WHITE, style='italic')

# The 5 clauses laid out as small panels
clause_titles = [
    'evaluating\ntrade-offs',
    'alignment of\nvars/consts',
    'efficiently',
    'meet goals',
    'against\nexternalities',
]
clause_subs = [
    'the activity',
    'the mechanism',
    'the criterion',
    'the direction',
    'the constraint',
]
clause_colors = [BLUE, CYAN, GREEN, ORANGE, MAG]

for i, (t, s, c) in enumerate(zip(clause_titles, clause_subs, clause_colors)):
    x0 = 0.5 + i * 1.85
    box = FancyBboxPatch((x0, 5.5), 1.65, 1.5,
                         boxstyle='round,pad=0.08',
                         facecolor=PAN, edgecolor=c, linewidth=1.8)
    ax.add_patch(box)
    ax.text(x0 + 0.825, 6.65, t, ha='center', va='center',
            fontsize=10, color=WHITE, fontweight='bold')
    ax.text(x0 + 0.825, 5.85, s, ha='center', va='center',
            fontsize=8, color=c, style='italic')

# True Cost panel (qualifier)
tc_box = FancyBboxPatch((0.5, 3.5), 9.0, 1.5,
                         boxstyle='round,pad=0.1',
                         facecolor=PAN, edgecolor=RED, linewidth=2)
ax.add_patch(tc_box)
ax.text(5.0, 4.6, 'True Cost on failure  —  the qualifier that excludes academic work',
        ha='center', fontsize=12, color=RED, fontweight='bold')
ax.text(5.0, 4.15,
        'True Cost is harm borne by goal-seekers and users when the engineered system fails.',
        ha='center', fontsize=11, color=WHITE, style='italic')
ax.text(5.0, 3.75,
        'The cost lands outside the engineering activity itself, on parties who did not do the work.',
        ha='center', fontsize=10, color=SILVER)

# The three-test filter
ax.text(5.0, 2.85, 'THE THREE TESTS',
        ha='center', fontsize=12, color=GOLD, fontweight='bold')

tests = [
    ('substrate?', 'is reality pushing back on the work?'),
    ('trade-offs live?', 'is something genuinely undecided?'),
    ('True Cost?', 'do goal-seekers / users pay if it fails?'),
]
for i, (q, exp) in enumerate(tests):
    x0 = 0.7 + i * 3.1
    box = FancyBboxPatch((x0, 1.3), 2.85, 1.25,
                         boxstyle='round,pad=0.1',
                         facecolor=PAN, edgecolor=GOLD, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x0 + 1.425, 2.10, q,
            ha='center', va='center', fontsize=11,
            color=GOLD, fontweight='bold')
    ax.text(x0 + 1.425, 1.62, exp,
            ha='center', va='center', fontsize=9, color=WHITE)

ax.text(5.0, 0.7, 'all three required  \u2192  engineering    |    any missing  \u2192  something else',
        ha='center', fontsize=10, color=SILVER, style='italic')

save(fig, 'eng01_07_identity_card.png')

# ================================================================
# FIG 8: COST ASYMMETRY — WHO PAYS WHEN ENGINEERING FAILS
# Type: 4 (Geometric Cross-Section)
# Shows: concentric responsibility/consequence rings with cost flowing outward
# ================================================================
fig, ax = plt.subplots(figsize=(14, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')

# Concentric rings (drawn outermost first for layering)
rings = [
    (5.5, '#1a1a2a', 0.95, 'USERS', 'people who depend on the system'),
    (4.0, '#1f1f30', 0.9, 'GOAL-SEEKERS', 'organization / business'),
    (2.5, '#252538', 0.85, 'TEAM / ORG', 'colleagues, management'),
    (1.0, '#2a2a40', 0.8, 'ENGINEER', 'the person doing the work'),
]

ring_labels = []
for r, fc, alpha, name, sub in rings:
    circle = Circle((0, 0), r, facecolor=fc, edgecolor=DIM,
                    linewidth=1.0, alpha=alpha, zorder=1)
    ax.add_patch(circle)
    ring_labels.append((r, name, sub))

# Label each ring
ax.text(0, 0, 'ENGINEER',
        ha='center', va='center', fontsize=11,
        color=WHITE, fontweight='bold')
ax.text(0, -0.4, 'the person\ndoing the work',
        ha='center', va='top', fontsize=8, color=SILVER, style='italic')

ax.text(0, 1.7, 'TEAM / ORG',
        ha='center', va='center', fontsize=11,
        color=CYAN, fontweight='bold')
ax.text(0, -1.7, 'colleagues, management',
        ha='center', va='center', fontsize=8, color=SILVER, style='italic')

ax.text(0, 3.2, 'GOAL-SEEKERS',
        ha='center', va='center', fontsize=12,
        color=ORANGE, fontweight='bold')
ax.text(0, -3.2, 'organization / business',
        ha='center', va='center', fontsize=9, color=SILVER, style='italic')

ax.text(0, 4.7, 'USERS',
        ha='center', va='center', fontsize=13,
        color=RED, fontweight='bold')
ax.text(0, -4.7, 'people who depend on the system',
        ha='center', va='center', fontsize=9, color=SILVER, style='italic')

# Arrows showing True Cost flowing OUTWARD (engineer cannot absorb it)
arrow_angles = [45, 135, 225, 315]
for ang in arrow_angles:
    rad = np.radians(ang)
    x1, y1 = 0.7 * np.cos(rad), 0.7 * np.sin(rad)
    x2, y2 = 5.2 * np.cos(rad), 5.2 * np.sin(rad)
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle='->', mutation_scale=22,
                             color=RED, linewidth=2.0, alpha=0.85,
                             zorder=5)
    ax.add_patch(arrow)

# Label the cost flow
ax.text(3.3, 3.3, 'True Cost\nflows outward',
        ha='center', va='center', fontsize=10,
        color=RED, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

ax.text(-3.3, -3.3, 'engineer cannot\nabsorb the cost',
        ha='center', va='center', fontsize=10,
        color=RED, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# Title and footer
ax.text(0, 5.7, 'True Cost Asymmetry: Who Pays When Engineering Fails',
        ha='center', fontsize=14, color=GOLD, fontweight='bold')

ax.text(0, -5.7,
        'Decisions made on behalf of users  \u2192  consequences borne by users.',
        ha='center', fontsize=10, color=SILVER, style='italic')
ax.text(0, -5.95,
        'This asymmetry is what creates the discipline\'s ethical obligation.',
        ha='center', fontsize=10, color=SILVER, style='italic')

save(fig, 'eng01_08_cost_asymmetry.png')

# ================================================================
# SUMMARY
# ================================================================
print("\nGenerated 8 figures:")
print("  eng01_01_removal_test_matrix.png     (Type 6)")
print("  eng01_02_activity_landscape.png      (Type 3)")
print("  eng01_03_swe_ops_cost_surfaces.png   (Type 3)")
print("  eng01_04_substrate_threshold.png     (Type 1)")
print("  eng01_05_examples_landscape.png      (Type 2)")
print("  eng01_06_bridge_alignment_basin.png  (Type 1)")
print("  eng01_07_identity_card.png           (Type 8)")
print("  eng01_08_cost_asymmetry.png          (Type 4)")
print("\nType coverage: 6 distinct types (1, 2, 3, 4, 6, 8)")
print("Output directory: %s" % outdir)
