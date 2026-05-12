#!/usr/bin/env python3
"""
SSH Fuel Allocation Paper — Diagrams
8 figures covering nervous system fuel allocation
as a contributing mechanism to SSH type formation.
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
    
TYPE_COLORS = {
    'Alpha': GOLD,
    'Bravo': CYAN,
    'Delta': GREEN,
    'Gamma': MAG,
    'Omega': RED,
    'Sigma': PURPLE,
}

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
# FIG 1: FUEL PRIORITY HIERARCHY — NEURAL ARCHITECTURE
# Type: Geometric Cross-Section
# Shows: The layered architecture of neural fuel priority,
#        with fuel flowing bottom-to-top and constraint cutting
#        top-first. This spatial structure IS the mechanism.
# ================================================================

fig1, ax1 = plt.subplots(figsize=(16, 12))
ax1.set_facecolor(PAN)
ax1.axis('off')
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.set_title('Neural Fuel Priority Architecture',
              color=GOLD, fontsize=17, fontweight='bold', pad=25)

# Layers from bottom to top
layers = [
    {'name': 'Brainstem / Autonomic', 'y': 10, 'h': 12, 'color': RED,
     'funds': 'Breathing, heartbeat, survival reflexes',
     'priority': 'HIGHEST PRIORITY — Always funded'},
    {'name': 'Limbic / Threat Assessment', 'y': 27, 'h': 12, 'color': ORANGE,
     'funds': 'Fear, status monitoring, threat detection',
     'priority': 'High — Overdriven in Gamma, Omega'},
    {'name': 'Cortical / Social Cognition', 'y': 44, 'h': 12, 'color': CYAN,
     'funds': 'People-modeling, room-reading, sympathy',
     'priority': 'Medium — Requires surplus to function'},
    {'name': 'Frontal / Executive Override', 'y': 61, 'h': 12, 'color': BLUE,
     'funds': 'Impulse control, planning, behavioral override',
     'priority': 'LOWEST PRIORITY — Cut first under stress'},
]

for layer in layers:
    rect = mpatches.FancyBboxPatch(
        (12, layer['y']), 50, layer['h'],
        boxstyle='round,pad=0.8',
        facecolor=layer['color'], alpha=0.25,
        edgecolor=layer['color'], linewidth=2
    )
    ax1.add_patch(rect)
    ax1.text(37, layer['y'] + layer['h'] * 0.6, layer['name'],
             color=WHITE, fontsize=12, fontweight='bold',
             ha='center', va='center')
    ax1.text(37, layer['y'] + layer['h'] * 0.25, layer['funds'],
             color=SILVER, fontsize=8, ha='center', va='center')
    ax1.text(68, layer['y'] + layer['h'] * 0.5, layer['priority'],
             color=layer['color'], fontsize=9, ha='left', va='center')

# Fuel flow arrow (bottom to top)
ax1.annotate('', xy=(8, 74), xytext=(8, 10),
             arrowprops=dict(arrowstyle='->', color=GREEN,
                             lw=3, mutation_scale=20))
ax1.text(5, 42, 'FUEL\nFLOW', color=GREEN, fontsize=10,
         fontweight='bold', ha='center', va='center', rotation=90)

# Surplus region at top
surplus_rect = mpatches.FancyBboxPatch(
    (12, 78), 50, 10,
    boxstyle='round,pad=0.8',
    facecolor=GOLD, alpha=0.15,
    edgecolor=GOLD, linewidth=2, linestyle='--'
)
ax1.add_patch(surplus_rect)
ax1.text(37, 83, 'SURPLUS', color=GOLD, fontsize=13,
         fontweight='bold', ha='center', va='center')
ax1.text(68, 83, 'What remains after all layers are served',
         color=GOLD, fontsize=9, ha='left', va='center')

# Constraint line
ax1.plot([10, 64], [56, 56], color=RED, linewidth=2,
         linestyle='-.', alpha=0.7)
ax1.text(65, 56, 'Stress constraint line\nmoves DOWN under load',
         color=RED, fontsize=9, ha='left', va='center')

# Key principle
ax1.text(50, 3, 'Under constraint, the system cuts from the TOP first — frontal loses fuel before limbic, limbic before brainstem',
         color=SILVER, fontsize=9, ha='center', va='center',
         style='italic')

save(fig1, 'ssh_01_neural_architecture.png')


# ================================================================
# FIG 2: FUEL DISTRIBUTION STACK BY TYPE
# Type: Comparison Bar Chart
# Shows: Proportional fuel allocation across 5 neural layers
#        for all 6 SSH types. The surplus difference between
#        types is visible as the gap at the top.
# ================================================================

fig2, ax2 = plt.subplots(figsize=(18, 10))
style_ax(ax2,
         title='Fuel Distribution Across Neural Layers by SSH Type',
         xlabel='SSH Type',
         ylabel='Proportional Fuel Allocation (%)')

types_list = ['Alpha', 'Bravo', 'Delta', 'Gamma', 'Omega', 'Sigma']

# Fuel allocation profiles (brainstem, autonomic, limbic, cortical, frontal, surplus)
# These represent proportional allocation of total available fuel
profiles = {
    'Alpha':  [12, 10, 10, 20, 18, 30],
    'Bravo':  [12, 10, 12, 19, 17, 25],  # +orientation cost in limbic
    'Delta':  [12, 10, 15, 28,  8, 12],  # heavy cortical-task, low frontal
    'Gamma':  [12, 10, 30, 18,  5, 10],  # overdriven limbic
    'Omega':  [12, 10, 40, 10,  3,  5],  # threat surveillance dominates
    'Sigma':  [12, 10, 10, 22, 18, 28],  # alpha-equivalent via efficiency
}

layer_names = ['Brainstem', 'Autonomic', 'Limbic/Threat', 'Cortical', 'Frontal', 'SURPLUS']
layer_colors = [RED, ORANGE, MAG, CYAN, BLUE, GOLD]

x = np.arange(len(types_list))
bar_width = 0.55

bottoms = np.zeros(len(types_list))
for i, (layer, color) in enumerate(zip(layer_names, layer_colors)):
    values = [profiles[t][i] for t in types_list]
    alpha_val = 0.85 if layer == 'SURPLUS' else 0.65
    ax2.bar(x, values, bar_width, bottom=bottoms, color=color,
            alpha=alpha_val, edgecolor=color, linewidth=1.5,
            label=layer)
    # Label surplus values on top segment
    if layer == 'SURPLUS':
        for j, v in enumerate(values):
            ax2.text(x[j], bottoms[j] + v / 2, '%d%%' % v,
                     color=BG, fontsize=10, fontweight='bold',
                     ha='center', va='center')
    bottoms += np.array(values)

ax2.set_xticks(x)
ax2.set_xticklabels(types_list, color=WHITE, fontsize=11, fontweight='bold')
ax2.set_ylim(0, 115)
ax2.set_xlim(-0.6, len(types_list) - 0.4)

# Color-code x-tick labels
for j, label in enumerate(ax2.get_xticklabels()):
    label.set_color(TYPE_COLORS[types_list[j]])

legend = ax2.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
                    labelcolor=WHITE, fontsize=9, framealpha=0.9)

# Annotation
ax2.text(len(types_list) - 0.5, 108,
         'SURPLUS = fuel available for social cognition, empathy, gaze freedom, behavioral override',
         color=GOLD, fontsize=8, ha='right', va='center', style='italic')

save(fig2, 'ssh_02_fuel_distribution.png')


# ================================================================
# FIG 3: SURPLUS CURVE — SUPPLY VS DEMAND GAP
# Type: Running/Convergence Chart
# Shows: Two curves per type — total capacity and self-management
#        cost — with the vertical gap being surplus. The gap shape
#        IS the surplus principle made visible.
# ================================================================

fig3, ax3 = plt.subplots(figsize=(18, 10))
style_ax(ax3,
         title='The Surplus Principle: Total Capacity vs Self-Management Cost',
         xlabel='SSH Type (ordered by surplus)',
         ylabel='Relative Nervous System Fuel (arbitrary units)')

# Order by surplus: Omega, Gamma, Delta, Bravo, Sigma, Alpha
ordered_types = ['Omega', 'Gamma', 'Delta', 'Bravo', 'Sigma', 'Alpha']

# Total capacity and self-management demand
capacity = {
    'Omega': 60, 'Gamma': 72, 'Delta': 65,
    'Bravo': 85, 'Sigma': 78, 'Alpha': 92
}
demand = {
    'Omega': 55, 'Gamma': 62, 'Delta': 50,
    'Bravo': 55, 'Sigma': 42, 'Alpha': 48
}

x = np.arange(len(ordered_types))
cap_vals = [capacity[t] for t in ordered_types]
dem_vals = [demand[t] for t in ordered_types]
surplus_vals = [capacity[t] - demand[t] for t in ordered_types]

# Shaded surplus region
ax3.fill_between(x, dem_vals, cap_vals, alpha=0.15, color=GOLD)

# Curves
ax3.plot(x, cap_vals, 'o-', color=CYAN, linewidth=2.5, markersize=12,
         markeredgecolor=WHITE, markeredgewidth=2, label='Total Fuel Capacity',
         zorder=5)
ax3.plot(x, dem_vals, 's-', color=RED, linewidth=2.5, markersize=12,
         markeredgecolor=WHITE, markeredgewidth=2, label='Self-Management Cost',
         zorder=5)

# Surplus labels in the gap — offset to avoid overlap
for i, t in enumerate(ordered_types):
    gap = surplus_vals[i]
    mid_y = (cap_vals[i] + dem_vals[i]) / 2
    ax3.text(i + 0.25, mid_y, 'surplus\n= %d' % gap,
             color=GOLD, fontsize=9, fontweight='bold',
             ha='left', va='center',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=GOLD, alpha=0.8))

# Type labels at bottom
ax3.set_xticks(x)
ax3.set_xticklabels(ordered_types, color=WHITE, fontsize=11, fontweight='bold')
for j, label in enumerate(ax3.get_xticklabels()):
    label.set_color(TYPE_COLORS[ordered_types[j]])

ax3.set_ylim(25, 105)
ax3.set_xlim(-0.5, len(ordered_types) - 0.3)

# Note about sigma efficiency
ax3.annotate('Sigma: lower total capacity\nbut lowest demand = efficient',
             xy=(4, capacity['Sigma']),
             xytext=(2.8, 95),
             color=PURPLE, fontsize=9,
             arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=PURPLE, alpha=0.8))

legend = ax3.legend(loc='lower right', facecolor=PAN, edgecolor=DIM,
                    labelcolor=WHITE, fontsize=10, framealpha=0.9)

save(fig3, 'ssh_03_surplus_curve.png')


# ================================================================
# FIG 4: THREAT LOAD VS OUTWARD ATTENTION TRADEOFF
# Type: Threshold/Region Chart
# Shows: Inverse relationship between threat assessment fuel
#        consumption and capacity for outward attention (sympathy,
#        empathy, social modeling). Types cluster at natural
#        breakpoints. Shaded regions show behavioral regimes.
# ================================================================

fig4, ax4 = plt.subplots(figsize=(18, 10))
style_ax(ax4,
         title='Threat Assessment Load vs Outward Attention Capacity',
         xlabel='Threat Assessment Fuel Consumption (% of total)',
         ylabel='Outward Attention Capacity (empathy, sympathy, social modeling)')

# Type positions on the tradeoff curve
threat_load = {
    'Alpha': 10, 'Bravo': 14, 'Sigma': 11,
    'Delta': 22, 'Gamma': 38, 'Omega': 55
}
outward_cap = {
    'Alpha': 92, 'Bravo': 82, 'Sigma': 88,
    'Delta': 55, 'Gamma': 28, 'Omega': 8
}

# Generate smooth tradeoff curve
t_smooth = np.linspace(5, 65, 200)
# Inverse curve with threshold cliff around 30-35%
o_smooth = 100.0 / (1.0 + np.exp(0.12 * (t_smooth - 30))) * 1.0
# Scale to fit the data points approximately
o_smooth = 5 + 90.0 / (1.0 + np.exp(0.1 * (t_smooth - 28)))

ax4.plot(t_smooth, o_smooth, color=DIM, linewidth=1.5, linestyle='--',
         alpha=0.5, zorder=1)

# Shaded regions
ax4.axhspan(70, 100, alpha=0.06, color=GREEN)
ax4.axhspan(35, 70, alpha=0.06, color=ORANGE)
ax4.axhspan(0, 35, alpha=0.06, color=RED)

# Region labels
ax4.text(62, 85, 'SOCIAL MASTERY ZONE', color=GREEN, fontsize=10,
         fontweight='bold', ha='right', va='center', alpha=0.7)
ax4.text(62, 52, 'PARTIAL SOCIAL\nAWARENESS', color=ORANGE, fontsize=10,
         fontweight='bold', ha='right', va='center', alpha=0.7)
ax4.text(62, 18, 'SOCIAL BLINDNESS /\nINVERTED EMPATHY', color=RED, fontsize=10,
         fontweight='bold', ha='right', va='center', alpha=0.7)

# Threshold line
ax4.axhline(y=35, color=RED, linewidth=1.5, linestyle='-.', alpha=0.5)
ax4.text(6, 37, 'Empathy collapse threshold', color=RED, fontsize=8,
         style='italic')

# Plot types as scatter points
offsets = {
    'Alpha': (3, 4), 'Bravo': (3, -6), 'Sigma': (-5, -7),
    'Delta': (3, 5), 'Gamma': (3, 5), 'Omega': (3, 5)
}
for t in threat_load:
    ax4.scatter(threat_load[t], outward_cap[t], s=250,
                color=TYPE_COLORS[t], edgecolors=WHITE,
                linewidth=2, zorder=10)
    ox, oy = offsets[t]
    ax4.annotate(t,
                 xy=(threat_load[t], outward_cap[t]),
                 xytext=(threat_load[t] + ox, outward_cap[t] + oy),
                 color=TYPE_COLORS[t], fontsize=11, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=TYPE_COLORS[t],
                                 lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                           edgecolor=TYPE_COLORS[t], alpha=0.8))

ax4.set_xlim(3, 65)
ax4.set_ylim(-2, 103)

# Key insight annotation
ax4.text(35, 96,
         'Types cluster at natural breakpoints on the tradeoff curve',
         color=SILVER, fontsize=9, ha='center', va='center',
         style='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                   edgecolor=DIM, alpha=0.8))

save(fig4, 'ssh_04_threat_attention_tradeoff.png')


# ================================================================
# FIG 5: PREY-PREDATOR POSTURAL GEOMETRY
# Type: Geometric Cross-Section
# Shows: Two body configurations — prey pattern (spine extended,
#        peripheral vision cone, escape vectors) vs predator
#        pattern (spine flexed, foveal cone, engagement vector).
#        Type labels show who defaults to which.
# ================================================================

fig5, (ax5a, ax5b) = plt.subplots(1, 2, figsize=(20, 12),
                                   gridspec_kw={'wspace': 0.35})

for ax_panel in [ax5a, ax5b]:
    ax_panel.set_facecolor(PAN)
    ax_panel.axis('off')
    ax_panel.set_xlim(0, 100)
    ax_panel.set_ylim(0, 100)

# === LEFT PANEL: PREY PATTERN ===
ax5a.set_title('PREY PATTERN', color=RED, fontsize=16, fontweight='bold', pad=20)

# Simplified body — vertical line for spine, circle for head
# Spine extended (tall, straight, tense)
spine_x = 40
ax5a.plot([spine_x, spine_x], [20, 65], color=RED, linewidth=4, alpha=0.7)
# Head
head = plt.Circle((spine_x, 70), 5, facecolor=RED, alpha=0.3,
                   edgecolor=RED, linewidth=2)
ax5a.add_patch(head)

# Peripheral vision cone — wide angle
cone_left_x = spine_x - 35
cone_right_x = spine_x + 35
cone_y = 88
ax5a.fill([spine_x, cone_left_x, cone_right_x], [70, cone_y, cone_y],
          color=RED, alpha=0.08)
ax5a.plot([spine_x, cone_left_x], [70, cone_y], color=RED,
          linewidth=1.5, linestyle='--', alpha=0.5)
ax5a.plot([spine_x, cone_right_x], [70, cone_y], color=RED,
          linewidth=1.5, linestyle='--', alpha=0.5)
ax5a.text(spine_x, 90, 'PERIPHERAL VISION\n(wide scan, diffuse)',
          color=RED, fontsize=9, ha='center', va='center',
          fontweight='bold')

# Escape vectors — arrows pointing away
for angle_deg in [-40, -20, 0, 20, 40]:
    angle = np.radians(angle_deg - 90)
    dx = 10 * np.cos(angle)
    dy = 10 * np.sin(angle)
    ax5a.annotate('', xy=(spine_x + dx, 15 + dy),
                  xytext=(spine_x, 18),
                  arrowprops=dict(arrowstyle='->', color=ORANGE,
                                  lw=1.5, alpha=0.6))

ax5a.text(spine_x, 7, 'ESCAPE VECTORS', color=ORANGE,
          fontsize=9, ha='center', fontweight='bold')

# Spine label
ax5a.text(spine_x + 10, 42, 'Spine EXTENDED\n(tall, tense,\nescape-ready)',
          color=RED, fontsize=9, ha='left', va='center',
          bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                    edgecolor=RED, alpha=0.8))

# Type labels — who defaults here
ax5a.text(85, 55, 'Default types:', color=SILVER, fontsize=9,
          ha='center', va='center', fontweight='bold')
ax5a.text(85, 48, 'Omega', color=TYPE_COLORS['Omega'], fontsize=11,
          ha='center', va='center', fontweight='bold')
ax5a.text(85, 41, 'Delta\n(under pressure)', color=TYPE_COLORS['Delta'],
          fontsize=9, ha='center', va='center')
ax5a.text(85, 31, 'Gamma\n(oscillates)', color=TYPE_COLORS['Gamma'],
          fontsize=9, ha='center', va='center')

# === RIGHT PANEL: PREDATOR PATTERN ===
ax5b.set_title('PREDATOR PATTERN', color=GREEN, fontsize=16,
               fontweight='bold', pad=20)

# Spine flexed (leaning forward, coiled)
spine_base_x = 45
spine_top_x = 38
ax5b.plot([spine_base_x, spine_top_x], [20, 60], color=GREEN,
          linewidth=4, alpha=0.7)
# Head — slightly forward
head2 = plt.Circle((spine_top_x - 2, 65), 5, facecolor=GREEN, alpha=0.3,
                    edgecolor=GREEN, linewidth=2)
ax5b.add_patch(head2)

# Foveal cone — narrow, focused
fov_center_x = spine_top_x - 2
fov_y = 65
cone_half = 8
target_y = 88
ax5b.fill([fov_center_x, fov_center_x - cone_half, fov_center_x + cone_half],
          [fov_y, target_y, target_y],
          color=GREEN, alpha=0.08)
ax5b.plot([fov_center_x, fov_center_x - cone_half], [fov_y, target_y],
          color=GREEN, linewidth=1.5, linestyle='--', alpha=0.5)
ax5b.plot([fov_center_x, fov_center_x + cone_half], [fov_y, target_y],
          color=GREEN, linewidth=1.5, linestyle='--', alpha=0.5)
ax5b.text(fov_center_x, 92, 'FOVEAL FOCUS\n(narrow, locked on target)',
          color=GREEN, fontsize=9, ha='center', va='center',
          fontweight='bold')

# Engagement vector — single forward arrow
ax5b.annotate('', xy=(spine_base_x - 15, 12),
              xytext=(spine_base_x, 18),
              arrowprops=dict(arrowstyle='->', color=CYAN,
                              lw=3, alpha=0.7))
ax5b.text(spine_base_x - 18, 7, 'ENGAGEMENT\nVECTOR', color=CYAN,
          fontsize=9, ha='center', fontweight='bold')

# Spine label
ax5b.text(spine_base_x + 12, 40, 'Spine FLEXED\n(coiled, loaded,\nengagement-ready)',
          color=GREEN, fontsize=9, ha='left', va='center',
          bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                    edgecolor=GREEN, alpha=0.8))

# Type labels
ax5b.text(85, 55, 'Default types:', color=SILVER, fontsize=9,
          ha='center', va='center', fontweight='bold')
ax5b.text(85, 48, 'Alpha', color=TYPE_COLORS['Alpha'], fontsize=11,
          ha='center', va='center', fontweight='bold')
ax5b.text(85, 41, 'Bravo', color=TYPE_COLORS['Bravo'], fontsize=10,
          ha='center', va='center', fontweight='bold')
ax5b.text(85, 34, 'Sigma', color=TYPE_COLORS['Sigma'], fontsize=10,
          ha='center', va='center', fontweight='bold')
ax5b.text(85, 27, 'Delta\n(at workbench)', color=TYPE_COLORS['Delta'],
          fontsize=9, ha='center', va='center')

# Shared caption
fig5.text(0.5, 0.02,
          'The same nervous system architecture produces opposite body configurations depending on threat assessment state',
          color=SILVER, fontsize=10, ha='center', va='center', style='italic')

save(fig5, 'ssh_05_prey_predator_posture.png')


# ================================================================
# FIG 6: BROKEN ALPHA DEGRADATION CASCADE
# Type: Progression/Sequence Diagram
# Shows: Sequential fuel drains from baseline alpha surplus,
#        each stage feeding the next. The cascade shape shows
#        how small drains compound to eliminate surplus entirely.
# ================================================================

fig6, ax6 = plt.subplots(figsize=(20, 10))
style_ax(ax6,
         title='The Broken Alpha: Degradation Cascade',
         xlabel='', ylabel='Remaining Surplus (arbitrary units)')

stages = [
    ('Baseline\nAlpha', 30, GREEN, ''),
    ('Chronic\nPain', -6, RED, 'Constant\nfuel drain'),
    ('Sleep\nLoss', -5, RED, 'Less total\ncapacity/day'),
    ('Exercise\nDrops', -5, ORANGE, 'Neurochemical\ndegradation'),
    ('Social\nReading\nDegrades', -4, ORANGE, 'Empathy &\npatience\nshrink'),
    ('Relationship\nStrain', -4, MAG, 'Harsh with\ncrew & family'),
    ('Self-\nSustaining\nLoop', -3, MAG, 'Each effect\nfeeds the\nnext'),
    ('Near\nZero', -2, RED, 'Pattern fires,\ncannot\ncomplete'),
]

x_positions = np.linspace(5, 92, len(stages))
cumulative = 0
bar_values = []

for i, (label, change, color, note) in enumerate(stages):
    if i == 0:
        cumulative = change
        bar_values.append((x_positions[i], 0, cumulative, GREEN))
    else:
        old = cumulative
        cumulative += change
        bar_values.append((x_positions[i], cumulative, old - cumulative, color))

ax6.set_xlim(0, 100)
ax6.set_ylim(-5, 40)

bar_w = 7

for i, (xp, bottom, height, color) in enumerate(bar_values):
    if i == 0:
        ax6.bar(xp, height, bar_w, bottom=bottom, color=color,
                alpha=0.7, edgecolor=color, linewidth=1.5)
        ax6.text(xp, height / 2, '%d' % height, color=BG,
                 fontsize=11, fontweight='bold', ha='center', va='center')
    else:
        # Waterfall: show the remaining level
        remaining = stages[0][1] + sum(s[1] for s in stages[1:i+1])
        # Draw remaining bar from 0
        ax6.bar(xp, max(remaining, 0.5), bar_w, bottom=0, color=GOLD,
                alpha=0.3, edgecolor=GOLD, linewidth=1)
        # Draw the loss segment on top
        ax6.bar(xp, height, bar_w, bottom=remaining, color=color,
                alpha=0.6, edgecolor=color, linewidth=1.5)
        ax6.text(xp, remaining + height + 1.2, '-%d' % height,
                 color=color, fontsize=9, fontweight='bold', ha='center')
        # Remaining value inside bar
        if remaining > 2:
            ax6.text(xp, remaining / 2, '%d' % remaining, color=WHITE,
                     fontsize=9, fontweight='bold', ha='center', va='center')

    # Stage label below
    label_text = stages[i][0]
    ax6.text(xp, -3.5, label_text, color=WHITE, fontsize=8,
             ha='center', va='center', fontweight='bold')

    # Note above
    note_text = stages[i][3]
    if note_text and i > 0:
        remaining = stages[0][1] + sum(s[1] for s in stages[1:i+1])
        note_y = remaining + stages[i][1] * -1 + 4.5
        if note_y > 36:
            note_y = 36
        ax6.text(xp, note_y, note_text, color=SILVER, fontsize=7,
                 ha='center', va='center', style='italic')

# Cascade arrows between bars
for i in range(len(x_positions) - 1):
    ax6.annotate('',
                 xy=(x_positions[i+1] - bar_w/2 - 0.5, 15),
                 xytext=(x_positions[i] + bar_w/2 + 0.5, 15),
                 arrowprops=dict(arrowstyle='->', color=DIM,
                                 lw=1.2, alpha=0.5))

ax6.axhline(y=0, color=RED, linewidth=1.5, linestyle='--', alpha=0.5)
ax6.text(97, 1, 'ZERO\nSURPLUS', color=RED, fontsize=8,
         ha='center', fontweight='bold')

# Remove x-axis ticks (we have custom labels)
ax6.set_xticks([])

save(fig6, 'ssh_06_broken_alpha_cascade.png')


# ================================================================
# FIG 7: SIGMA DEVELOPMENT PATH — FUEL REALLOCATION
# Type: Progression/Sequence Diagram
# Shows: Stacked area chart showing fuel allocation across
#        neural layers changing over developmental time.
#        Omega pattern on left transforms to sigma pattern on right.
# ================================================================

fig7, ax7 = plt.subplots(figsize=(18, 10))
style_ax(ax7,
         title='Sigma Development: Fuel Reallocation Over Time',
         xlabel='Developmental Time',
         ylabel='Proportional Fuel Allocation (%)')

# Time axis (arbitrary developmental progression)
t = np.linspace(0, 10, 200)

# Transition function (sigmoid)
def sigmoid(x, center, steepness):
    return 1.0 / (1.0 + np.exp(-steepness * (x - center)))

# Each layer's allocation over time
# Brainstem: constant
brainstem = np.full_like(t, 12.0)

# Autonomic: constant
autonomic = np.full_like(t, 10.0)

# Limbic/Threat: starts very high (omega), drops (sigma)
# Omega = 40%, Sigma = 10%
limbic = 40.0 - 30.0 * sigmoid(t, 5.0, 1.5)

# Cortical: starts low, rises
cortical = 10.0 + 12.0 * sigmoid(t, 5.0, 1.5)

# Frontal: starts very low, rises
frontal = 3.0 + 15.0 * sigmoid(t, 5.5, 1.5)

# Surplus: remainder
surplus = 100.0 - brainstem - autonomic - limbic - cortical - frontal
# Clamp negative
surplus = np.maximum(surplus, 0)

# Stack from bottom
layers_data = [brainstem, autonomic, limbic, cortical, frontal, surplus]
colors_stack = [RED, ORANGE, MAG, CYAN, BLUE, GOLD]
labels_stack = ['Brainstem', 'Autonomic', 'Limbic/Threat', 'Cortical',
                'Frontal', 'SURPLUS']
alphas_stack = [0.5, 0.5, 0.6, 0.6, 0.6, 0.7]

# Plot stacked areas
bottom_stack = np.zeros_like(t)
for i, (data, color, label, a) in enumerate(zip(layers_data, colors_stack,
                                                  labels_stack, alphas_stack)):
    ax7.fill_between(t, bottom_stack, bottom_stack + data,
                     color=color, alpha=a, label=label)
    bottom_stack = bottom_stack + data

# Phase labels
ax7.text(1.5, 95, 'OMEGA PHASE', color=RED, fontsize=13,
         fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                   edgecolor=RED, alpha=0.8))
ax7.text(8.5, 95, 'SIGMA PHASE', color=PURPLE, fontsize=13,
         fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                   edgecolor=PURPLE, alpha=0.8))

# Transition marker
ax7.axvline(x=5.0, color=WHITE, linewidth=1.5, linestyle=':', alpha=0.4)
ax7.text(5.0, 85, 'THREAT\nRECALIBRATION', color=WHITE, fontsize=9,
         fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                   edgecolor=WHITE, alpha=0.7))

# Layer labels at right edge
right_positions = [
    (brainstem[-1] / 2, 'Brainstem', RED),
    (brainstem[-1] + autonomic[-1] / 2, 'Autonomic', ORANGE),
    (brainstem[-1] + autonomic[-1] + limbic[-1] / 2, 'Limbic', MAG),
    (brainstem[-1] + autonomic[-1] + limbic[-1] + cortical[-1] / 2,
     'Cortical', CYAN),
    (brainstem[-1] + autonomic[-1] + limbic[-1] + cortical[-1] +
     frontal[-1] / 2, 'Frontal', BLUE),
    (brainstem[-1] + autonomic[-1] + limbic[-1] + cortical[-1] +
     frontal[-1] + surplus[-1] / 2, 'SURPLUS', GOLD),
]

for y_pos, label, color in right_positions:
    ax7.text(10.3, y_pos, label, color=color, fontsize=8,
             fontweight='bold', ha='left', va='center')

ax7.set_xlim(0, 10.2)
ax7.set_ylim(0, 105)
ax7.set_xticks([])

# Key insight
ax7.text(5.0, 4, 'Threat recalibration frees fuel to upper structures — same total capacity, radically different allocation',
         color=SILVER, fontsize=8, ha='center', style='italic')

save(fig7, 'ssh_07_sigma_development.png')


# ================================================================
# FIG 8: PATTERN STORAGE DIVERGENCE OVER LIFETIME
# Type: Running/Convergence Chart
# Shows: Cumulative pattern storage fuel cost diverging over
#        lifetime for each type. Alpha's curve is shallow
#        (tactical updates). Omega's is steep (threat patterns).
#        The divergence shape explains type entrenchment.
# ================================================================

fig8, ax8 = plt.subplots(figsize=(18, 10))
style_ax(ax8,
         title='Pattern Storage Fuel Cost: Lifetime Divergence by Type',
         xlabel='Age (years)',
         ylabel='Cumulative Pattern Maintenance Cost (arbitrary units)')

age = np.linspace(5, 65, 200)

# Growth curves for pattern storage cost
# Alpha: shallow — mostly tactical updates, low maintenance cost
alpha_cost = 5 + 8 * np.log(age / 5.0)

# Bravo: slightly steeper — tactical + orientation patterns
bravo_cost = 5 + 11 * np.log(age / 5.0)

# Delta: moderate — competence patterns accumulate steadily
delta_cost = 5 + 18 * np.log(age / 5.0) + 0.1 * (age - 5)

# Gamma: steep — status anxiety, delusion bubble layers compound
gamma_cost = 5 + 15 * np.log(age / 5.0) + 0.4 * (age - 5)

# Omega: steepest — threat patterns densely layered, each one costly
omega_cost = 5 + 12 * np.log(age / 5.0) + 0.7 * (age - 5)

# Sigma: starts as omega, then flattens after recalibration ~20
sigma_cost = np.where(
    age < 20,
    5 + 12 * np.log(age / 5.0) + 0.7 * (age - 5),
    # After recalibration: previous accumulated cost + slow alpha-like growth
    5 + 12 * np.log(20.0 / 5.0) + 0.7 * 15 + 8 * np.log(age / 20.0)
)

curves = [
    ('Alpha', alpha_cost, TYPE_COLORS['Alpha'], '-'),
    ('Bravo', bravo_cost, TYPE_COLORS['Bravo'], '-'),
    ('Delta', delta_cost, TYPE_COLORS['Delta'], '-'),
    ('Gamma', gamma_cost, TYPE_COLORS['Gamma'], '-'),
    ('Omega', omega_cost, TYPE_COLORS['Omega'], '-'),
    ('Sigma', sigma_cost, TYPE_COLORS['Sigma'], '--'),
]

for name, cost, color, ls in curves:
    ax8.plot(age, cost, color=color, linewidth=2.5, linestyle=ls,
             label=name, zorder=5)

# End-of-life labels — offset to avoid overlap
label_offsets = {
    'Alpha': (2, -1),
    'Bravo': (2, -1),
    'Delta': (2, 1),
    'Gamma': (2, 1),
    'Omega': (2, 1),
    'Sigma': (2, -2),
}

for name, cost, color, ls in curves:
    final_val = cost[-1]
    ox, oy = label_offsets[name]
    ax8.text(65 + ox, final_val + oy, '%s (%.0f)' % (name, final_val),
             color=color, fontsize=10, fontweight='bold', va='center')

# Sigma recalibration marker
ax8.axvline(x=20, color=PURPLE, linewidth=1.2, linestyle=':', alpha=0.5)
ax8.text(21, 8, 'Sigma threat\nrecalibration', color=PURPLE, fontsize=8,
         style='italic',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                   edgecolor=PURPLE, alpha=0.7))

# Region annotation
ax8.fill_between(age, alpha_cost, omega_cost, alpha=0.04, color=WHITE)
ax8.text(40, 18,
         'This gap is why types\nbecome more entrenched\nwith age',
         color=SILVER, fontsize=9, ha='center',
         style='italic',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                   edgecolor=DIM, alpha=0.8))

ax8.set_xlim(3, 80)
ax8.set_ylim(0, 55)

legend = ax8.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
                    labelcolor=WHITE, fontsize=10, framealpha=0.9)

save(fig8, 'ssh_08_pattern_divergence.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n  All 8 figures saved:")
print("    ssh_01_neural_architecture.png")
print("    ssh_02_fuel_distribution.png")
print("    ssh_03_surplus_curve.png")
print("    ssh_04_threat_attention_tradeoff.png")
print("    ssh_05_prey_predator_posture.png")
print("    ssh_06_broken_alpha_cascade.png")
print("    ssh_07_sigma_development.png")
print("    ssh_08_pattern_divergence.png")
