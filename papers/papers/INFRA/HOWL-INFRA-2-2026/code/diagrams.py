#!/usr/bin/env python3
"""
HOWL ENG-02 Diagrams — What True Cost Is, and Why Credentialing Has Failed Software
8 figures covering True Cost domains, the three-tier credentialing model,
and the structural reasons software credentialing fails.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Wedge, Rectangle
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
# FIG 1: TWO DOMAINS OF TRUE COST
# Type: 2 (Scale/Landscape)
# Shows: physical/civ True Cost vs financial/availability True Cost
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

# Two regions
# Bottom-left: financial / reversible (business engineering)
ax.axhspan(0, 4, xmin=0.0, xmax=0.55, alpha=0.08, color=BLUE, zorder=0)
# Top-right: physical/civ / irreversible (traditional)
ax.axhspan(6, 10, xmin=0.55, xmax=1.0, alpha=0.10, color=RED, zorder=0)
# Crossover zone
ax.axhspan(5, 9, xmin=0.45, xmax=0.95, alpha=0.05, color=GOLD, zorder=0)

ax.text(2.0, 3.0, 'BUSINESS\nENGINEERING\nDOMAIN',
        ha='center', va='center', fontsize=12,
        color=BLUE, fontweight='bold', alpha=0.85)
ax.text(8.0, 9.5, 'TRADITIONAL\nENGINEERING\nDOMAIN',
        ha='center', va='center', fontsize=12,
        color=RED, fontweight='bold', alpha=0.85)
ax.text(7.5, 7.3, 'crossover region',
        ha='center', va='center', fontsize=10,
        color=GOLD, style='italic', alpha=0.85)

# Examples placed
examples = [
    # (name, reversibility 0=reversible 10=irreversible, magnitude 0=low 10=mortality)
    ('SaaS outage', 1.5, 1.5, BLUE),
    ('Failed startup', 4.0, 2.5, BLUE),
    ('Data loss\n(restorable)', 2.5, 2.0, BLUE),
    ('Major data breach', 5.5, 4.0, ORANGE),
    ('MapReduce job fail', 0.8, 0.8, BLUE),
    ('Pacemaker bug', 9.0, 9.0, RED),
    ('Bridge collapse', 9.5, 9.5, RED),
    ('Therac-25', 9.5, 9.8, RED),
    ('Avionics failure', 9.5, 9.5, RED),
    ('Industrial accident', 9.0, 8.8, RED),
    ('Grid failure\n(cascading)', 8.5, 8.5, RED),
    ('Autonomous vehicle\ncollision', 9.0, 9.0, RED),
    ('Algo trading crash', 6.5, 5.5, ORANGE),
    ('Election\ndisinformation', 7.5, 6.5, ORANGE),
]

count = 0
for name, x, y, c in examples:
    ax.scatter(x, y, s=200, color=c, edgecolors=WHITE,
               linewidth=1.5, zorder=5, alpha=0.9)
    
    offsetY = 0
    if count % 2 == 1:
        offsetY = -0.75

    ax.annotate(name, xy=(x, y), xytext=(x - 0.5, y + 0.25 + offsetY),
                fontsize=9, color=WHITE)
    count += 1

ax.set_xlabel('Reversibility of Cost  \u2192  (reversible \u2192 irreversible)',
              color=SILVER, fontsize=12)
ax.set_ylabel('Cost Magnitude  \u2192  (bounded \u2192 mortality / civilizational)',
              color=SILVER, fontsize=12)
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 10.5)

ax.set_title('Two Domains of True Cost: Different Magnitudes, Different Reversibility',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng02_01_two_domains_truecost.png')

# ================================================================
# FIG 2: SUBSTRATE STABILITY ACROSS DISCIPLINES
# Type: 1 (Running/Convergence Chart)
# Shows: substrate change rate over time for each engineering discipline
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

years = np.linspace(1900, 2026, 200)

# Civil/Mechanical/Electrical: nearly flat (substrate barely changes)
civil = 95 + 2 * np.sin((years - 1900) / 30) + 0.5 * (years - 1900) / 126
mech = 93 + 2 * np.cos((years - 1900) / 25) + 0.7 * (years - 1900) / 126
elec = 90 + 5 * np.sin((years - 1900) / 20) + 1.0 * (years - 1900) / 126

# Software: extreme volatility
# Mainframes (1950s-60s), minis (70s), PCs (80s), web (90s), cloud (2000s),
# containers (2010s), AI/serverless (2020s)
sw = np.zeros_like(years)
for i, y in enumerate(years):
    if y < 1950:
        sw[i] = 95
    else:
        # Each transition drops stability sharply, recovers partially
        transitions = [1955, 1972, 1985, 1995, 2006, 2014, 2022]
        base = 60
        for t in transitions:
            base -= 8 * np.exp(-((y - t) ** 2) / 20)
        # Constant churn between transitions
        sw[i] = max(20, base + 5 * np.sin((y - 1950) / 3))

ax.plot(years, civil, color=BLUE, linewidth=2.5,
        label='Civil engineering')
ax.plot(years, mech, color=GREEN, linewidth=2.5,
        label='Mechanical engineering')
ax.plot(years, elec, color=PURPLE, linewidth=2.5,
        label='Electrical engineering')
ax.plot(years, sw, color=ORANGE, linewidth=2.8,
        label='Software engineering')

# Mark software substrate transitions
transitions_marks = [
    (1955, 'mainframes'),
    (1972, 'minis'),
    (1985, 'PCs'),
    (1995, 'web'),
    (2006, 'cloud'),
    (2014, 'containers'),
    (2022, 'AI / serverless'),
]
for ty, tname in transitions_marks:
    ax.axvline(ty, color=ORANGE, linestyle=':', linewidth=0.8, alpha=0.4)
    ax.text(ty, 12, tname, fontsize=8, color=ORANGE,
            rotation=90, ha='center', va='bottom', alpha=0.85)

# Annotation: stability threshold for credentialing
ax.axhline(80, color=GOLD, linestyle='--', linewidth=1.2, alpha=0.6)
ax.text(1905, 82, 'credentialing-viable threshold',
        fontsize=9, color=GOLD)

ax.set_xlabel('Year', color=SILVER, fontsize=12)
ax.set_ylabel('Substrate Stability (%)', color=SILVER, fontsize=12)
ax.set_xlim(1900, 2030)
ax.set_ylim(0, 105)

leg = ax.legend(loc='lower left', facecolor=PAN, edgecolor=DIM,
                labelcolor=WHITE, fontsize=10)

ax.set_title('Substrate Stability: Why Software Cannot Be Credentialed Like Civil',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng02_02_substrate_stability.png')

# ================================================================
# FIG 3: THE THREE-TIER CREDENTIALING MATRIX
# Type: 5/6 (Connection Map / Comparison)
# Shows: the central framework as a structured matrix
# ================================================================
fig, ax = plt.subplots(figsize=(18, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5.0, 9.5, 'THE THREE-TIER CREDENTIALING MODEL',
        ha='center', fontsize=16, color=GOLD, fontweight='bold')
ax.text(5.0, 9.05, 'credentialing follows cost domain, not activity',
        ha='center', fontsize=11, color=SILVER, style='italic')

# Header row
headers = ['Tier', 'Cost Domain', 'Substrate', 'Credentialing Target', 'Why It Works']
header_x = [0.7, 2.7, 4.7, 6.5, 8.5]
header_widths = [1.6, 1.6, 1.6, 1.6, 1.4]

for h, x, w in zip(headers, header_x, header_widths):
    box = FancyBboxPatch((x - w/2 + 0.05, 7.8), w - 0.1, 0.7,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=GOLD, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 8.15, h, ha='center', va='center',
            fontsize=11, color=GOLD, fontweight='bold')

# Three tier rows
tiers = [
    {
        'name': 'TRADITIONAL',
        'color': RED,
        'cost': 'Physical /\ncivilizational\n(mortality)',
        'substrate': 'Stable\n(physics holds still)',
        'target': 'PERSON\n(then output\nvia stamp)',
        'why': 'Costs justify\noverhead; codes\nexist; competence\nportable',
        'y': 6.0,
    },
    {
        'name': 'BUSINESS',
        'color': BLUE,
        'cost': 'Financial /\nservice-availability\n(bounded, reversible)',
        'substrate': 'Unstable\n(continuous churn)',
        'target': 'NONE\n(market handles\ncompetence)',
        'why': 'Costs don\'t justify;\nsubstrate moves;\nno formal codes\npossible',
        'y': 4.0,
    },
    {
        'name': 'CROSSOVER',
        'color': GOLD,
        'cost': 'Traditional cost\nvia software\n(mortality reached)',
        'substrate': 'System-specific\n(internal consistency)',
        'target': 'OUTPUT\n(certified by\ndomain engineer)',
        'why': 'SW competence\nnot portable;\nsystem is the\nunit',
        'y': 2.0,
    },
]

for t in tiers:
    # Tier label box
    box = FancyBboxPatch((0.05, t['y'] - 0.7), 1.3, 1.4,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=t['color'], linewidth=2)
    ax.add_patch(box)
    ax.text(0.7, t['y'], t['name'], ha='center', va='center',
            fontsize=12, color=t['color'], fontweight='bold', rotation=0)

    # Cost domain
    box = FancyBboxPatch((1.95, t['y'] - 0.7), 1.5, 1.4,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=DIM, linewidth=1)
    ax.add_patch(box)
    ax.text(2.7, t['y'], t['cost'], ha='center', va='center',
            fontsize=9, color=WHITE)

    # Substrate
    box = FancyBboxPatch((3.95, t['y'] - 0.7), 1.5, 1.4,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=DIM, linewidth=1)
    ax.add_patch(box)
    ax.text(4.7, t['y'], t['substrate'], ha='center', va='center',
            fontsize=9, color=WHITE)

    # Credentialing target
    box = FancyBboxPatch((5.75, t['y'] - 0.7), 1.5, 1.4,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=t['color'], linewidth=1.5)
    ax.add_patch(box)
    ax.text(6.5, t['y'], t['target'], ha='center', va='center',
            fontsize=10, color=t['color'], fontweight='bold')

    # Why
    box = FancyBboxPatch((7.85, t['y'] - 0.7), 1.7, 1.4,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=DIM, linewidth=1)
    ax.add_patch(box)
    ax.text(8.7, t['y'], t['why'], ha='center', va='center',
            fontsize=8.5, color=SILVER)

# Footer note
ax.text(5.0, 0.6, 'Same SWE may cross between tiers across their career.',
        ha='center', fontsize=10, color=SILVER, style='italic')
ax.text(5.0, 0.3, 'The tier follows the work, not the person.',
        ha='center', fontsize=10, color=SILVER, style='italic')

save(fig, 'eng02_03_three_tier_matrix.png')

# ================================================================
# FIG 4: COST MAGNITUDE vs CREDENTIALING OVERHEAD
# Type: 3 (Threshold/Region Chart)
# Shows: society's credentialing apparatus follows cost magnitude
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_axes(ax)

x = np.linspace(0, 10, 300)
# Step-like curve: nothing at low cost, ramps up at mortality threshold
# Society's investment in credentialing infrastructure
overhead = 5 + 90 / (1 + np.exp(-1.5 * (x - 6)))

ax.plot(x, overhead, color=GOLD, linewidth=2.8,
        label='Society\'s credentialing apparatus')

# Region shading
ax.axvspan(0, 4, alpha=0.07, color=BLUE, zorder=0)
ax.axvspan(4, 7, alpha=0.07, color=ORANGE, zorder=0)
ax.axvspan(7, 10, alpha=0.10, color=RED, zorder=0)

# Region labels
ax.text(2.0, 95, 'BUSINESS COST', ha='center',
        fontsize=11, color=BLUE, fontweight='bold')
ax.text(2.0, 89, 'no apparatus', ha='center',
        fontsize=9, color=BLUE, style='italic')

ax.text(5.5, 95, 'EDGE / EMERGING', ha='center',
        fontsize=11, color=ORANGE, fontweight='bold')
ax.text(5.5, 89, 'partial / contested', ha='center',
        fontsize=9, color=ORANGE, style='italic')

ax.text(8.5, 95, 'TRADITIONAL COST', ha='center',
        fontsize=11, color=RED, fontweight='bold')
ax.text(8.5, 89, 'full apparatus', ha='center',
        fontsize=9, color=RED, style='italic')

# Mark example activities
markers = [
    ('CRUD app dev', 1.0, 'business'),
    ('SaaS ops at scale', 2.5, 'business'),
    ('Distributed systems', 3.5, 'business'),
    ('Algo trading', 5.5, 'edge'),
    ('Medical AI', 7.0, 'crossover'),
    ('Auto vehicles', 7.5, 'crossover'),
    ('Avionics SW', 8.5, 'crossover'),
    ('Pacemaker firmware', 8.8, 'crossover'),
    ('Bridge engineering', 9.3, 'traditional'),
]

for name, xv, _ in markers:
    yv = 5 + 90 / (1 + np.exp(-1.5 * (xv - 6)))
    if xv < 4:
        c = BLUE
    elif xv < 7:
        c = ORANGE
    else:
        c = RED
    ax.scatter(xv, yv, s=160, color=c, edgecolors=WHITE,
               linewidth=1.5, zorder=5)
    ax.annotate(name, xy=(xv, yv), xytext=(xv + 0.15, yv - 7),
                fontsize=9, color=WHITE,
                arrowprops=dict(arrowstyle='-', color=DIM, lw=0.5, alpha=0.5))

# Threshold annotation
ax.axvline(6.0, color=DIM, linestyle='--', linewidth=1, alpha=0.5)
ax.text(6.05, 25, 'mortality\nthreshold', fontsize=9, color=DIM, va='center')

ax.set_xlabel('True Cost Magnitude  \u2192',
              color=SILVER, fontsize=12)
ax.set_ylabel('Credentialing Apparatus Society Builds (%)',
              color=SILVER, fontsize=12)
ax.set_xlim(0, 10)
ax.set_ylim(0, 105)

ax.set_title('Credentialing Overhead Follows Cost Magnitude',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

save(fig, 'eng02_04_cost_vs_credentialing.png')

# ================================================================
# FIG 5: INTERNAL CONSISTENCY RATIO — BRIDGE vs PACEMAKER
# Type: 6 (Comparison Bar Chart)
# Shows: where engineering effort goes — software is internally consistent first
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
style_axes(ax1)
style_axes(ax2)

# Bridge engineering effort distribution
bridge_categories = ['External\ninterface\n(loads, soil,\nwind, traffic)',
                     'Internal\nconsistency\n(rebar, joints,\nbolts)']
bridge_values = [70, 30]
bridge_colors = [RED, CYAN]

# Pacemaker firmware effort distribution
pace_categories = ['External\ninterface\n(actual cardiac\ndecision)',
                   'Internal\nconsistency\n(state machines,\nerror handling,\ncomms, diagnostics)']
pace_values = [10, 90]
pace_colors = [RED, CYAN]

# Bridge bars
y_pos = np.arange(len(bridge_categories))
bars1 = ax1.barh(y_pos, bridge_values, color=bridge_colors, alpha=0.7,
                 edgecolor=bridge_colors, linewidth=2)
for i, (v, c) in enumerate(zip(bridge_values, bridge_categories)):
    ax1.text(v + 1.5, i, str(v) + '%',
             va='center', ha='left', fontsize=12,
             color=WHITE, fontweight='bold')

ax1.set_yticks(y_pos)
ax1.set_yticklabels(bridge_categories, color=WHITE, fontsize=10)
ax1.set_xlim(0, 100)
ax1.set_xticks([0, 25, 50, 75, 100])
ax1.set_xlabel('% of Engineering Effort', color=SILVER, fontsize=11)
ax1.set_title('Bridge Engineering',
              color=BLUE, fontsize=14, fontweight='bold', pad=12)
ax1.text(50, 1.7,
         'External interface dominates.\nInternal organization follows from loads.',
         ha='center', fontsize=9, color=SILVER, style='italic')

# Pacemaker bars
y_pos = np.arange(len(pace_categories))
bars2 = ax2.barh(y_pos, pace_values, color=pace_colors, alpha=0.7,
                 edgecolor=pace_colors, linewidth=2)
for i, (v, c) in enumerate(zip(pace_values, pace_categories)):
    ax2.text(v + 1.5, i, str(v) + '%',
             va='center', ha='left', fontsize=12,
             color=WHITE, fontweight='bold')

ax2.set_yticks(y_pos)
ax2.set_yticklabels(pace_categories, color=WHITE, fontsize=10)
ax2.set_xlim(0, 100)
ax2.set_xticks([0, 25, 50, 75, 100])
ax2.set_xlabel('% of Engineering Effort', color=SILVER, fontsize=11)
ax2.set_title('Pacemaker Firmware',
              color=ORANGE, fontsize=14, fontweight='bold', pad=12)
ax2.text(50, 1.7,
         'Internal consistency dominates.\nMortality decision is a fraction.',
         ha='center', fontsize=9, color=SILVER, style='italic')

fig.suptitle('Software is Internally Consistent First, Crossover-to-Reality Second',
             color=GOLD, fontsize=15, fontweight='bold', y=0.98)

save(fig, 'eng02_05_internal_consistency_ratio.png')

# ================================================================
# FIG 6: A THOUSAND ENGINEERS, SAME PROBLEM
# Type: 6 (Comparison — scatter clouds)
# Shows: civil engineers converge, software engineers diverge
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9),
                                gridspec_kw={'wspace': 0.25})
fig.patch.set_facecolor(BG)
style_axes(ax1)
style_axes(ax2)

# Set seed for reproducibility
np.random.seed(42)

# Civil engineers: tight cluster around correct solution
n = 1000
civil_x = np.random.normal(5, 0.4, n)
civil_y = np.random.normal(5, 0.4, n)

# A few outliers at small distance
civil_x_out = np.random.normal(5, 1.0, 50)
civil_y_out = np.random.normal(5, 1.0, 50)

ax1.scatter(civil_x, civil_y, s=20, color=BLUE, alpha=0.4,
            edgecolors='none', zorder=3)
ax1.scatter(civil_x_out, civil_y_out, s=20, color=BLUE, alpha=0.3,
            edgecolors='none', zorder=2)

# Mark the "correct solution region"
correct = Circle((5, 5), 0.6, fill=False, edgecolor=GREEN,
                  linewidth=2, linestyle='--', zorder=4)
ax1.add_patch(correct)
ax1.text(5, 6.4, 'physics\nconstrains\nsolution space',
         ha='center', fontsize=10, color=GREEN, fontweight='bold')

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title('1000 Civil Engineers, Same Bridge Site',
              color=BLUE, fontsize=14, fontweight='bold', pad=12)
ax1.text(5, 0.5,
         'Designs cluster tightly. Competence is portable.',
         ha='center', fontsize=10, color=SILVER, style='italic')

# Software engineers: spread across solution space
sw_x = np.random.uniform(0.5, 9.5, n)
sw_y = np.random.uniform(0.5, 9.5, n)

# Distribute in clusters representing different architectural choices
clusters = [(2, 2), (2, 8), (8, 2), (8, 8), (5, 5), (3, 6), (7, 4), (4, 8)]
sw_x_clust = []
sw_y_clust = []
for cx, cy in clusters:
    sw_x_clust.extend(np.random.normal(cx, 0.7, 125))
    sw_y_clust.extend(np.random.normal(cy, 0.7, 125))
sw_x_clust = np.array(sw_x_clust)
sw_y_clust = np.array(sw_y_clust)

# Clip to plot area
sw_x_clust = np.clip(sw_x_clust, 0.3, 9.7)
sw_y_clust = np.clip(sw_y_clust, 0.3, 9.7)

ax2.scatter(sw_x_clust, sw_y_clust, s=20, color=ORANGE, alpha=0.4,
            edgecolors='none', zorder=3)

# Multiple "internally consistent" regions
for cx, cy in clusters[:5]:
    region = Circle((cx, cy), 0.9, fill=False, edgecolor=GREEN,
                     linewidth=1.5, linestyle='--', alpha=0.6, zorder=4)
    ax2.add_patch(region)

ax2.text(5, 0.5,
         'Architectures spread. Competence is system-specific.',
         ha='center', fontsize=10, color=SILVER, style='italic')

ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_title('1000 SWEs, Same Crossover System',
              color=ORANGE, fontsize=14, fontweight='bold', pad=12)

fig.suptitle('Why Software Person-Credentialing Cannot Work Like Civil',
             color=GOLD, fontsize=15, fontweight='bold', y=0.98)

save(fig, 'eng02_06_thousand_engineers.png')

# ================================================================
# FIG 7: TWO-ROLE CROSSOVER MODEL
# Type: 4 (Geometric Cross-Section)
# Shows: SWE builds, domain engineer certifies, accountability flow
# ================================================================
fig, ax = plt.subplots(figsize=(16, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect('equal')
ax.axis('off')

# Outer ring: users / public
outer = Circle((0, 0), 6.0, facecolor='#1a1a2a', edgecolor=DIM,
                linewidth=1.0, alpha=0.95, zorder=1)
ax.add_patch(outer)

# Middle ring: certification regime + domain engineer
mid = Circle((0, 0), 4.2, facecolor='#1f1f30', edgecolor=GOLD,
              linewidth=1.8, alpha=0.95, zorder=2)
ax.add_patch(mid)

# Inner ring: SWE builds the system
inner = Circle((0, 0), 2.5, facecolor='#252538', edgecolor=CYAN,
                linewidth=1.8, alpha=0.95, zorder=3)
ax.add_patch(inner)

# Core: the artifact
core = Circle((0, 0), 1.0, facecolor=PAN, edgecolor=WHITE,
               linewidth=1.5, alpha=1.0, zorder=4)
ax.add_patch(core)

# Labels
ax.text(0, 0.15, 'CERTIFIED', ha='center', va='center',
        fontsize=10, color=WHITE, fontweight='bold')
ax.text(0, -0.25, 'SYSTEM', ha='center', va='center',
        fontsize=10, color=WHITE, fontweight='bold')

ax.text(0, 1.75, 'SWE builds the artifact',
        ha='center', va='center', fontsize=11,
        color=CYAN, fontweight='bold')
ax.text(0, 1.40, '(internal consistency,', ha='center',
        fontsize=8.5, color=SILVER, style='italic')
ax.text(0, 1.15, 'validation, testing)', ha='center',
        fontsize=8.5, color=SILVER, style='italic')

ax.text(0, 3.5, 'Domain engineer certifies',
        ha='center', va='center', fontsize=12,
        color=GOLD, fontweight='bold')
ax.text(0, 3.15, '(PE-credentialed, holds the safety claim)',
        ha='center', fontsize=9, color=SILVER, style='italic')

ax.text(0, -3.5, 'CERTIFICATION REGIME',
        ha='center', va='center', fontsize=11,
        color=GOLD, fontweight='bold')
ax.text(0, -3.85, 'DO-178C / FDA / ISO 26262 / IEC 61508',
        ha='center', fontsize=9, color=SILVER, style='italic')

ax.text(0, 5.3, 'GOAL-SEEKERS / USERS',
        ha='center', va='center', fontsize=12,
        color=RED, fontweight='bold')
ax.text(0, 4.95, '(receive certified output, bear True Cost on failure)',
        ha='center', fontsize=9, color=SILVER, style='italic')

ax.text(0, -5.3, 'PUBLIC',
        ha='center', va='center', fontsize=12,
        color=RED, fontweight='bold')
ax.text(0, -5.65, '(structural accountability anchored at certification regime)',
        ha='center', fontsize=9, color=SILVER, style='italic')

# Accountability flow arrows
# When system fails, accountability flows OUT through certifier
arrow_angles = [60, 120, 240, 300]
for ang in arrow_angles:
    rad = np.radians(ang)
    x1, y1 = 1.2 * np.cos(rad), 1.2 * np.sin(rad)
    x2, y2 = 4.0 * np.cos(rad), 4.0 * np.sin(rad)
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle='->', mutation_scale=18,
                             color=RED, linewidth=1.8, alpha=0.7,
                             zorder=5)
    ax.add_patch(arrow)

# Title
ax.text(0, 6.5, 'Two-Role Crossover Model: Where the Safety Claim Lives',
        ha='center', fontsize=14, color=GOLD, fontweight='bold')

# Side annotations
ax.text(-6.5, 0, 'SWE\ndoes engineering\nat crossover\nmagnitude',
        ha='left', va='center', fontsize=9, color=CYAN,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN))

ax.text(6.5, 0, 'Domain engineer\nholds the safety\nclaim via\ndomain credential',
        ha='right', va='center', fontsize=9, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

save(fig, 'eng02_07_two_role_model.png')

# ================================================================
# FIG 8: REGULATORY REGIMES ON THE THREE-TIER MODEL
# Type: 5 (Connection / Integer Map)
# Shows: existing regimes placed on the framework
# ================================================================
fig, ax = plt.subplots(figsize=(18, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Three tier bands
ax.axhspan(7, 10, alpha=0.06, color=RED, zorder=0)
ax.axhspan(3.5, 7, alpha=0.06, color=GOLD, zorder=0)
ax.axhspan(0, 3.5, alpha=0.06, color=BLUE, zorder=0)

# Tier labels (left side)
ax.text(0.4, 8.5, 'TRADITIONAL', ha='center', va='center',
        fontsize=11, color=RED, fontweight='bold', rotation=90)
ax.text(0.4, 5.3, 'CROSSOVER', ha='center', va='center',
        fontsize=11, color=GOLD, fontweight='bold', rotation=90)
ax.text(0.4, 1.7, 'BUSINESS', ha='center', va='center',
        fontsize=11, color=BLUE, fontweight='bold', rotation=90)

# Title
ax.text(5.0, 9.5, 'Existing Regulatory Regimes Map to the Three-Tier Model',
        ha='center', fontsize=15, color=GOLD, fontweight='bold')

# Place regimes
regimes = [
    # Traditional tier
    {'name': 'PE\n(civil/mech/elec)', 'x': 2.0, 'y': 8.5, 'color': RED,
     'note': 'person-level\ncredential'},
    {'name': 'Chartered\nEngineer', 'x': 4.0, 'y': 8.5, 'color': RED,
     'note': 'person-level\ncredential'},
    {'name': 'Building codes\n(IBC, NEC, ASME)', 'x': 6.0, 'y': 8.5, 'color': RED,
     'note': 'output-level\nstandard'},
    {'name': 'Stamped\ndrawings', 'x': 8.0, 'y': 8.5, 'color': RED,
     'note': 'output cert\nvia person'},

    # Crossover tier
    {'name': 'DO-178C\n(avionics)', 'x': 2.0, 'y': 5.3, 'color': GOLD,
     'note': 'system\ncertification'},
    {'name': 'FDA 510(k)/PMA\n(medical devices)', 'x': 4.0, 'y': 5.3, 'color': GOLD,
     'note': 'system\ncertification'},
    {'name': 'ISO 26262\n(automotive)', 'x': 6.0, 'y': 5.3, 'color': GOLD,
     'note': 'system\ncertification'},
    {'name': 'IEC 61508\n(industrial)', 'x': 8.0, 'y': 5.3, 'color': GOLD,
     'note': 'system\ncertification'},

    # Business tier
    {'name': 'AWS / GCP /\nAzure certs', 'x': 2.0, 'y': 1.7, 'color': BLUE,
     'note': 'weak; vendor\nspecific; obsoletes'},
    {'name': 'IEEE CSDP', 'x': 4.0, 'y': 1.7, 'color': BLUE,
     'note': 'weak; not\nadopted'},
    {'name': 'ABET\nSW programs', 'x': 6.0, 'y': 1.7, 'color': BLUE,
     'note': 'academic; not\nlicensure'},
    {'name': 'Market\n(interviews, reputation)', 'x': 8.0, 'y': 1.7, 'color': BLUE,
     'note': 'what actually\nworks'},
]

for r in regimes:
    box = FancyBboxPatch((r['x'] - 0.85, r['y'] - 0.55), 1.7, 1.1,
                          boxstyle='round,pad=0.05',
                          facecolor=PAN, edgecolor=r['color'], linewidth=1.5)
    ax.add_patch(box)
    ax.text(r['x'], r['y'] + 0.1, r['name'],
            ha='center', va='center', fontsize=9.5,
            color=WHITE, fontweight='bold')
    ax.text(r['x'], r['y'] - 0.32, r['note'],
            ha='center', va='center', fontsize=7.5,
            color=r['color'], style='italic')

# Footer notes
ax.text(5.0, 0.6,
        'Crossover regimes converged on system-level certification by domain experts \u2014',
        ha='center', fontsize=10, color=SILVER, style='italic')
ax.text(5.0, 0.3,
        'the only credentialing model that fits software\'s structural facts.',
        ha='center', fontsize=10, color=SILVER, style='italic')

save(fig, 'eng02_08_regulatory_regimes.png')

# ================================================================
# SUMMARY
# ================================================================
print("\nGenerated 8 figures:")
print("  eng02_01_two_domains_truecost.png          (Type 2)")
print("  eng02_02_substrate_stability.png           (Type 1)")
print("  eng02_03_three_tier_matrix.png             (Type 5/6)")
print("  eng02_04_cost_vs_credentialing.png         (Type 3)")
print("  eng02_05_internal_consistency_ratio.png    (Type 6)")
print("  eng02_06_thousand_engineers.png            (Type 6)")
print("  eng02_07_two_role_model.png                (Type 4)")
print("  eng02_08_regulatory_regimes.png            (Type 5)")
print("\nType coverage: 6 distinct types (1, 2, 3, 4, 5, 6)")
print("Output directory: %s" % outdir)
