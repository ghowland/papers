#!/usr/bin/env python3
"""
HOWL GAME-1-2026 Diagrams — A Structural Taxonomy of Player Experience
8 figures covering temporal profiles, design space mapping, expression/pressure
tradeoffs, engagement density, loop hierarchy, gating pipelines, cognitive
budget, and feedback dynamics.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ── output directory ──────────────────────────────────────────────────
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── global palette ────────────────────────────────────────────────────
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
    
GAME_COLORS = [CYAN, RED, BLUE, GREEN, ORANGE, PURPLE]
GAME_NAMES  = ['Pac-Man', 'Quake 2', 'Skyrim', 'RimWorld', 'Dwarf Fortress', 'SimCity']


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


def style_ax(ax, title='', xlabel='', ylabel='', title_size=15):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=title_size, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)


# ================================================================
# FIG 1: GAME TEMPORAL PROFILES — HEATMAP
# Type: Comparison (D5 Type 6 adapted as heatmap)
# Shows: Each game's "fingerprint" across six loop levels. The reader
#        sees immediately that Quake burns hot on the left (fast loops)
#        while SimCity burns hot on the right (slow loops).
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Game Temporal Profiles — Activity Intensity by Loop Level')

loop_labels = ['0.2s\nReaction', '2s\nTactical', '10s\nEngagement',
               '60s\nNavigation', '300s\nObjective', '3000s\nStrategic']

#                      0.2s  2s   10s  60s  300s 3000s
profiles = np.array([
    [0.7,  0.9,  0.8,  0.2,  0.1,  0.0],   # Pac-Man
    [1.0,  0.9,  0.7,  0.3,  0.2,  0.1],   # Quake 2
    [0.3,  0.4,  0.6,  0.8,  0.9,  0.5],   # Skyrim
    [0.1,  0.3,  0.5,  0.7,  0.9,  0.8],   # RimWorld
    [0.1,  0.2,  0.5,  0.7,  0.8,  1.0],   # Dwarf Fortress
    [0.0,  0.1,  0.2,  0.4,  0.8,  1.0],   # SimCity
])

cell_w = 0.75
cell_h = 0.65
x_start = 0.5
y_start = 0.5

ax.set_xlim(0, len(loop_labels) + 0.5)
ax.set_ylim(0, len(GAME_NAMES) + 0.5)

for row in range(len(GAME_NAMES)):
    for col in range(len(loop_labels)):
        v = profiles[row, col]
        r = int(0x0a + (0xe0 - 0x0a) * v * 0.3)
        g = int(0x0a + (0xcd - 0x0a) * v * 0.7)
        b = int(0x12 + (0xc4 - 0x12) * v * 0.9)
        cell_color = '#%02x%02x%02x' % (r, g, b)

        cx = x_start + col
        cy = y_start + (len(GAME_NAMES) - 1 - row)

        rect = mpatches.FancyBboxPatch(
            (cx - cell_w / 2, cy - cell_h / 2), cell_w, cell_h,
            boxstyle='round,pad=0.05', facecolor=cell_color,
            edgecolor=DIM, linewidth=0.5
        )
        ax.add_patch(rect)

        txt_color = WHITE if v > 0.4 else DIM
        ax.text(cx, cy, '%.1f' % v, ha='center', va='center',
                fontsize=11, color=txt_color, fontweight='bold')

for i, name in enumerate(GAME_NAMES):
    cy = y_start + (len(GAME_NAMES) - 1 - i)
    ax.text(x_start - cell_w / 2 - 0.12, cy, name, ha='right', va='center',
            fontsize=11, color=GAME_COLORS[i], fontweight='bold')

for j, label in enumerate(loop_labels):
    cx = x_start + j
    ax.text(cx, y_start + len(GAME_NAMES) - 0.5 + 0.15, label,
            ha='center', va='bottom', fontsize=9, color=SILVER)

ax.text(x_start + 2.5, y_start - 0.7, 'Faster loops (twitch)  \u2190\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2192  Slower loops (strategic)',
        ha='center', va='center', fontsize=9, color=DIM)

ax.axis('off')

save(fig, 'game1_01_temporal_profiles.png')


# ================================================================
# FIG 2: DEPTH VS ACCESSIBILITY — PLAYER SPACE
# Type: Threshold/Region Chart (D5 Type 3)
# Shows: Games plotted on cognitive demand × consequence severity,
#        with shaded audience regions. The reader sees the design
#        space and where games cluster.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Design Space — Cognitive Demand vs Consequence Severity',
         xlabel='Cognitive Demand (systems \u00d7 tracking \u00d7 decisions)',
         ylabel='Consequence Severity (cost of failure)')

games_ds = {
    'Desktop Toy':      (0.5,  0.2),
    'Pac-Man':          (2.5,  5.0),
    'Casual Builder':   (2.0,  1.0),
    'Skyrim\n(Normal)': (4.0,  3.0),
    'Quake 2\n(DM)':    (3.5,  7.5),
    'Dark Souls':       (5.0,  8.0),
    'RimWorld':         (6.5,  6.0),
    'XCOM':             (5.5,  7.0),
    'Dwarf Fortress':   (9.0,  7.5),
    'Stardew Valley':   (3.0,  1.5),
}

regions = [
    (0, 0, 3.5, 3.5, 'Casual', CYAN, 0.06),
    (2.5, 2.0, 6.0, 6.5, 'Mainstream', GREEN, 0.05),
    (4.5, 4.5, 8.0, 8.5, 'Dedicated', ORANGE, 0.05),
    (7.0, 5.5, 10.5, 10.0, 'Niche', RED, 0.05),
]

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 10.0)

for x0, y0, x1, y1, label, color, alpha in regions:
    rect = mpatches.FancyBboxPatch(
        (x0, y0), x1 - x0, y1 - y0,
        boxstyle='round,pad=0.2', facecolor=color, alpha=alpha,
        edgecolor=color, linewidth=1.0, linestyle='--'
    )
    ax.add_patch(rect)
    ax.text(x1 - 0.2, y1 - 0.3, label, ha='right', va='top',
            fontsize=10, color=color, alpha=0.7, fontstyle='italic')

colors_ds = [DIM, CYAN, CYAN, BLUE, RED, MAG, GREEN, ORANGE, RED, GREEN]
for idx, (name, (x, y)) in enumerate(games_ds.items()):
    c = colors_ds[idx]
    ax.scatter(x, y, s=200, color=c, edgecolors=WHITE, linewidth=1.5, zorder=5)
    offset_x = 0.3
    offset_y = 0.3
    if 'Dark' in name:
        offset_x = -0.3
        offset_y = 0.4
    if 'Dwarf' in name:
        offset_y = -0.5
    if 'XCOM' in name:
        offset_x = 0.4
        offset_y = -0.3
    if 'Quake' in name:
        offset_x = -0.3
        offset_y = 0.4
    if 'Desktop' in name:
        offset_x = 0.4
        offset_y = -0.2
    if 'Stardew' in name:
        offset_y = -0.4
    ax.annotate(name, (x, y), xytext=(x + offset_x, y + offset_y),
                fontsize=9, color=c, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=DIM, lw=0.7))

ax.text(5.0, 0.3,
        'Player cognitive budget determines accessible region',
        ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic')

save(fig, 'game1_02_design_space.png')


# ================================================================
# FIG 3: EXPRESSION UNDER PRESSURE — TRADEOFF CURVE
# Type: Threshold/Region Chart (D5 Type 3)
# Shows: The tradeoff between disruption frequency and creative
#        expression capacity. Three builder games positioned on the
#        curve. Regions labeled expression-dominant vs survival-dominant.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Expression Under Pressure — Disruption vs Creative Capacity',
         xlabel='Disruption Frequency (events per play-hour)',
         ylabel='Effective Creative Expression Capacity')

x_curve = np.linspace(0.2, 12, 200)
y_curve = 9.0 / (1.0 + 0.35 * x_curve)

ax.plot(x_curve, y_curve, color=GOLD, linewidth=2.5, zorder=3, label='Expression capacity frontier')

ax.fill_between(x_curve, y_curve, 9.5, alpha=0.04, color=GREEN)
ax.fill_between(x_curve, 0, y_curve, alpha=0.04, color=RED)

ax.text(1.5, 8.2, 'Expression-Dominant', fontsize=11, color=GREEN, alpha=0.7,
        fontstyle='italic')
ax.text(9.0, 1.5, 'Survival-Dominant', fontsize=11, color=RED, alpha=0.7,
        fontstyle='italic')

games_expr = {
    'SimCity\n(disasters off)': (0.5, 8.5, CYAN),
    'SimCity\n(disasters on)':  (2.0, 6.8, BLUE),
    'RimWorld':                 (5.0, 4.2, GREEN),
    'Dwarf Fortress':           (8.0, 2.7, ORANGE),
    'SimCity \u00d710\ndisasters':  (10.0, 0.8, RED),
}

for name, (x, y, c) in games_expr.items():
    ax.scatter(x, y, s=220, color=c, edgecolors=WHITE, linewidth=1.5, zorder=5)
    ha_val = 'left'
    off_x = 0.4
    off_y = 0.2
    if 'off' in name:
        off_x = 0.4
        off_y = -0.4
    if 'Dwarf' in name:
        off_x = -0.3
        off_y = 0.5
        ha_val = 'right'
    if '\u00d710' in name:
        off_x = -0.3
        off_y = 0.4
        ha_val = 'right'
    ax.annotate(name, (x, y), xytext=(x + off_x, y + off_y),
                fontsize=9, color=c, fontweight='bold', ha=ha_val,
                arrowprops=dict(arrowstyle='->', color=DIM, lw=0.7))

ax.axhline(y=3.0, color=DIM, linestyle='--', linewidth=1, alpha=0.5)
ax.text(11.5, 3.2, 'Minimum viable\nexpression', fontsize=8, color=DIM,
        ha='right', va='bottom')

ax.set_xlim(-0.3, 12.5)
ax.set_ylim(-0.3, 9.5)
ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'game1_03_expression_pressure.png')


# ================================================================
# FIG 4: ENGAGEMENT DENSITY — DEATH STRANDING VS SKYRIM
# Type: Running/Convergence adapted as timeline (D5 Type 1)
# Shows: 300s of play in two games. Death Stranding has continuous
#        0.2s engagement; Skyrim has sparse 10s bursts with empty
#        navigation between. Demonstrates principle GR13.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

style_ax(ax1, title='Death Stranding — 300s Journey',
         xlabel='Time (seconds)', ylabel='Engagement Intensity')
style_ax(ax2, title='Skyrim — 300s Walking',
         xlabel='Time (seconds)', ylabel='Engagement Intensity')

np.random.seed(42)
t = np.linspace(0, 300, 3000)

ds_base = 0.5 + 0.15 * np.sin(2 * np.pi * t / 40)
ds_micro = 0.15 * np.random.rand(3000)
ds_terrain = np.zeros(3000)
for peak_t in [45, 95, 140, 185, 230, 270]:
    ds_terrain += 0.25 * np.exp(-0.5 * ((t - peak_t) / 8) ** 2)
ds_signal = np.clip(ds_base + ds_micro + ds_terrain, 0, 1.0)

ax1.fill_between(t, 0, ds_signal, alpha=0.3, color=CYAN)
ax1.plot(t, ds_signal, color=CYAN, linewidth=0.8, alpha=0.8)

ax1.axhline(y=0.3, color=GOLD, linestyle='--', linewidth=1, alpha=0.5)
ax1.text(295, 0.33, 'Minimum\nactive play', fontsize=8, color=GOLD,
         ha='right', va='bottom', alpha=0.7)

ax1.text(150, 0.92, 'Continuous 0.2s balance loop\nNested inside 300s traversal',
         fontsize=9, color=WHITE, ha='center', va='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, alpha=0.8))

ax1.set_xlim(0, 300)
ax1.set_ylim(0, 1.05)

sky_signal = np.full(3000, 0.08)
sky_signal += 0.04 * np.random.rand(3000)

encounters = [
    (35, 55, 0.6),
    (110, 125, 0.7),
    (200, 215, 0.5),
    (260, 275, 0.8),
]
for start, end, intensity in encounters:
    mask = (t >= start) & (t <= end)
    ramp_up = np.clip((t[mask] - start) / 3.0, 0, 1)
    ramp_down = np.clip((end - t[mask]) / 3.0, 0, 1)
    envelope = np.minimum(ramp_up, ramp_down)
    sky_signal[mask] = intensity * envelope + 0.1 * np.random.rand(np.sum(mask))

ax2.fill_between(t, 0, sky_signal, alpha=0.3, color=BLUE)
ax2.plot(t, sky_signal, color=BLUE, linewidth=0.8, alpha=0.8)

ax2.axhline(y=0.3, color=GOLD, linestyle='--', linewidth=1, alpha=0.5)
ax2.text(295, 0.33, 'Minimum\nactive play', fontsize=8, color=GOLD,
         ha='right', va='bottom', alpha=0.7)

for start, end, intensity in encounters:
    mid = (start + end) / 2.0
    ax2.annotate('~10s\nencounter', (mid, intensity * 0.5),
                 xytext=(mid, intensity * 0.5 + 0.25),
                 fontsize=7, color=ORANGE, ha='center',
                 arrowprops=dict(arrowstyle='->', color=ORANGE, lw=0.7))

ax2.text(150, 0.92, 'Empty navigation loop\nSparse 10s interruptions',
         fontsize=9, color=WHITE, ha='center', va='top',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=BLUE, alpha=0.8))

ax2.set_xlim(0, 300)
ax2.set_ylim(0, 1.05)

fig.text(0.5, 0.02, 'Principle GR13: Active inner loops sustain outer loops',
         ha='center', fontsize=11, color=GOLD, fontstyle='italic')

save(fig, 'game1_04_engagement_density.png')


# ================================================================
# FIG 5: LOOP HIERARCHY — NESTED TIME STRUCTURE
# Type: Geometric Cross-Section (D5 Type 4)
# Shows: Six temporal loops as concentric rings from 0.2s (inner)
#        to 3000s (outer). Each ring labeled with time scale, name,
#        cognitive mode, and example activities. The nesting shows
#        containment.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 16), facecolor=BG)
style_ax(ax)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Loop Hierarchy — Nested Temporal Structure',
             color=GOLD, fontsize=17, fontweight='bold', pad=20)

loops = [
    ('3000s', 'Strategic',    'Deliberative planning',    'Build path, faction choice', PURPLE),
    ('300s',  'Objective',    'Goal pursuit',             'Quest loop, dungeon clear',  ORANGE),
    ('60s',   'Navigation',   'Oriented movement',        'Walk between landmarks',     BLUE),
    ('10s',   'Engagement',   'Discrete interaction',     'Fight, talk, puzzle',        GREEN),
    ('2s',    'Tactical',     'Situation reading',        'Dodge-or-attack decision',   CYAN),
    ('0.2s',  'Reaction',     'Motor reflex',             'Dodge roll, aim snap',       MAG),
]

radii = [4.8, 4.0, 3.2, 2.4, 1.6, 0.8]
cx, cy = 0, 0

for i, (time, name, mode, example, color) in enumerate(loops):
    r = radii[i]
    alpha = 0.12 + i * 0.04
    circle = plt.Circle((cx, cy), r, facecolor=color, alpha=alpha,
                         edgecolor=color, linewidth=1.5, linestyle='-')
    ax.add_patch(circle)

    angle_rad = np.radians(210 - i * 18)
    label_r = r - 0.08
    lx = cx + label_r * np.cos(angle_rad)
    ly = cy + label_r * np.sin(angle_rad)

    if i < 3:
        ext_r = r + 0.35
        ex = cx + ext_r * np.cos(angle_rad)
        ey = cy + ext_r * np.sin(angle_rad)

        txt_r = r + 0.6
        if i == 0:
            txt_r = r + 0.5
        tx = cx + txt_r * np.cos(angle_rad)
        ty = cy + txt_r * np.sin(angle_rad)

        ha_val = 'right' if tx < cx else 'left'
        if abs(tx - cx) < 0.3:
            ha_val = 'center'

        ax.plot([lx, ex], [ly, ey], color=color, linewidth=0.7, alpha=0.6)
        label_text = '%s  %s\n%s\n%s' % (time, name, mode, example)
        ax.text(tx, ty, label_text, ha=ha_val, va='center',
                fontsize=9, color=color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=color, alpha=0.7))
    else:
        angle_rad2 = np.radians(30 + i * 20)
        ext_r = r + 0.35
        ex = cx + ext_r * np.cos(angle_rad2)
        ey = cy + ext_r * np.sin(angle_rad2)

        txt_r_inner = radii[0] + 0.6 + (i - 3) * 0.7
        tx = cx + txt_r_inner * np.cos(angle_rad2)
        ty = cy + txt_r_inner * np.sin(angle_rad2)

        lx2 = cx + r * np.cos(angle_rad2)
        ly2 = cy + r * np.sin(angle_rad2)

        ha_val = 'left' if tx > cx else 'right'

        ax.annotate('', xy=(lx2, ly2), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle='->', color=color, lw=0.8))
        label_text = '%s  %s\n%s\n%s' % (time, name, mode, example)
        ax.text(tx, ty, label_text, ha=ha_val, va='center',
                fontsize=9, color=color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=color, alpha=0.7))

ax.text(cx, cy, 'PLAYER', ha='center', va='center',
        fontsize=12, color=WHITE, fontweight='bold')

lim = 6.5
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

save(fig, 'game1_05_loop_hierarchy.png')


# ================================================================
# FIG 6: QUEST GATING PIPELINE — GAMEPLAY LOOP
# Type: Progression/Sequence Diagram (D5 Type 7)
# Shows: The Fallout NV quest loop as a circular pipeline with
#        gate types, dominant loop levels, and time scales at each
#        stage. The cycle shows the repeating structure.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14), facecolor=BG)
style_ax(ax)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Quest Gating Pipeline — The Gameplay Loop',
             color=GOLD, fontsize=17, fontweight='bold', pad=20)

stages = [
    ('Quest\nAssignment',  'Knowledge Gate',  '10s loop',   CYAN),
    ('Traversal',          'Traversal Gate',   '60s loop',   BLUE),
    ('Encounter',          'Skill Gate',       '2\u201310s loop', GREEN),
    ('Evidence',           'Resource Gate',    '10s loop',   ORANGE),
    ('Reward',             'Positive\nConsequence', '10s loop', GOLD),
]

n = len(stages)
radius = 3.5
angles = [np.pi / 2 - i * 2 * np.pi / n for i in range(n)]

node_positions = []
for i in range(n):
    x = radius * np.cos(angles[i])
    y = radius * np.sin(angles[i])
    node_positions.append((x, y))

for i in range(n):
    x, y = node_positions[i]
    name, gate, loop, color = stages[i]

    box = mpatches.FancyBboxPatch(
        (x - 1.2, y - 0.9), 2.4, 1.8,
        boxstyle='round,pad=0.15', facecolor=BG,
        edgecolor=color, linewidth=2.0
    )
    ax.add_patch(box)

    ax.text(x, y + 0.35, name, ha='center', va='center',
            fontsize=11, color=WHITE, fontweight='bold')
    ax.text(x, y - 0.15, gate, ha='center', va='center',
            fontsize=9, color=color, fontstyle='italic')
    ax.text(x, y - 0.55, loop, ha='center', va='center',
            fontsize=8, color=DIM)

for i in range(n):
    j = (i + 1) % n
    x1, y1 = node_positions[i]
    x2, y2 = node_positions[j]

    dx = x2 - x1
    dy = y2 - y1
    dist = np.sqrt(dx * dx + dy * dy)
    ux, uy = dx / dist, dy / dist

    shrink = 1.5
    sx = x1 + ux * shrink
    sy = y1 + uy * shrink
    ex = x2 - ux * shrink
    ey = y2 - uy * shrink

    color_arrow = stages[i][3]
    ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
                arrowprops=dict(arrowstyle='->', color=color_arrow,
                                lw=2.0, connectionstyle='arc3,rad=0.15'))

ax.text(0, 0, 'GAMEPLAY\nLOOP', ha='center', va='center',
        fontsize=14, color=GOLD, fontweight='bold', alpha=0.5)

ax.text(0, -0.8, 'Repeat with escalation', ha='center', va='center',
        fontsize=9, color=DIM, fontstyle='italic')

lim = 5.8
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

save(fig, 'game1_06_gating_pipeline.png')


# ================================================================
# FIG 7: COGNITIVE BUDGET — STACKED DEMAND VS CAPACITY
# Type: Comparison Bar Chart / stacked (D5 Type 6)
# Shows: Three games with cognitive demand broken into four components,
#        stacked. Horizontal threshold lines show player capacity for
#        different profiles. The reader sees which games exceed which
#        thresholds and which demand components dominate.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Cognitive Budget — Stacked Demand vs Player Capacity',
         xlabel='', ylabel='Total Cognitive Demand (relative units)')

cog_games = ['Skyrim', 'RimWorld', 'Dwarf\nFortress']
x_pos = np.array([1.0, 2.5, 4.0])
bar_width = 0.8

components = {
    'System Tracking':    [2.0, 4.0, 7.0],
    'State Tracking':     [2.5, 3.0, 5.0],
    'Decision Frequency': [1.5, 3.0, 4.0],
    'Causal Depth':       [1.0, 2.5, 4.5],
}
comp_colors = [CYAN, BLUE, GREEN, PURPLE]
comp_names = list(components.keys())

bottoms = np.zeros(3)
bars_collection = []
for idx, (comp_name, values) in enumerate(components.items()):
    vals = np.array(values)
    b = ax.bar(x_pos, vals, bar_width, bottom=bottoms,
               color=comp_colors[idx], alpha=0.7,
               edgecolor=comp_colors[idx], linewidth=1.5,
               label=comp_name)
    bars_collection.append(b)

    for k in range(3):
        if vals[k] > 0.8:
            ax.text(x_pos[k], bottoms[k] + vals[k] / 2.0,
                    '%.1f' % vals[k], ha='center', va='center',
                    fontsize=9, color=WHITE, fontweight='bold')
    bottoms += vals

for k in range(3):
    ax.text(x_pos[k], bottoms[k] + 0.4, '%.1f' % bottoms[k],
            ha='center', va='bottom', fontsize=11, color=GOLD, fontweight='bold')

thresholds = [
    (7.0,  'Casual player capacity',     CYAN),
    (12.5, 'Dedicated player capacity',   GREEN),
    (18.0, 'Hardcore player capacity',    ORANGE),
]

for y_val, label, color in thresholds:
    ax.axhline(y=y_val, color=color, linestyle='--', linewidth=1.5, alpha=0.6)
    ax.text(4.9, y_val + 0.2, label, fontsize=9, color=color,
            ha='left', va='bottom')

ax.set_xticks(x_pos)
ax.set_xticklabels(cog_games, fontsize=12, color=WHITE)
ax.set_xlim(0.0, 6.2)
ax.set_ylim(0, 23)

ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'game1_07_cognitive_budget.png')


# ================================================================
# FIG 8: FEEDBACK LOOP DYNAMICS
# Type: Geometric Cross-Section (D5 Type 4)
# Shows: Four feedback loop types as small geometric diagrams —
#        positive (outward spiral), negative (convergent),
#        stabilizing (bounded oscillation), destabilizing (runaway).
#        Each with game example and behavioral consequence.
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 14), facecolor=BG,
                          gridspec_kw={'hspace': 0.35, 'wspace': 0.30})

loop_types = [
    ('Positive Feedback',    'Success \u2192 more success',
     'Rich-get-richer snowball\nin 4X strategy games',      GREEN),
    ('Negative Feedback',    'Success \u2192 harder challenge',
     'Rubber-banding in\nracing games',                     CYAN),
    ('Stabilizing',          'Extremes self-correct',
     'Ecosystem balance in\nsimulation games',              BLUE),
    ('Destabilizing',        'Problems cascade',
     'Death spiral: wounded\ncan\'t fight \u2192 more wounded', RED),
]

for idx, ax in enumerate(axes.flat):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.set_aspect('equal')
    ax.axis('off')

    name, subtitle, example, color = loop_types[idx]

    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)

    ax.text(0, 1.6, name, ha='center', va='top',
            fontsize=13, color=color, fontweight='bold')
    ax.text(0, 1.25, subtitle, ha='center', va='top',
            fontsize=10, color=SILVER)

    if idx == 0:
        theta = np.linspace(0, 4 * np.pi, 500)
        r = 0.2 + 0.18 * theta
        r = np.clip(r, 0, 1.1)
        x = r * np.cos(theta)
        y = r * np.sin(theta) - 0.15
        ax.plot(x, y, color=color, linewidth=2.0)
        ax.annotate('', xy=(x[-1], y[-1]),
                    xytext=(x[-3], y[-3]),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))

    elif idx == 1:
        theta = np.linspace(0, 4 * np.pi, 500)
        r = 1.1 - 0.18 * theta
        r = np.clip(r, 0.15, 1.1)
        x = r * np.cos(theta)
        y = r * np.sin(theta) - 0.15
        ax.plot(x, y, color=color, linewidth=2.0)
        ax.annotate('', xy=(x[-1], y[-1]),
                    xytext=(x[-3], y[-3]),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))

    elif idx == 2:
        theta = np.linspace(0, 6 * np.pi, 800)
        r_base = 0.6
        amplitude = 0.3 * np.exp(-0.15 * theta)
        r = r_base + amplitude * np.sin(theta * 3)
        x = r * np.cos(theta)
        y = r * np.sin(theta) - 0.15
        ax.plot(x, y, color=color, linewidth=2.0)

        circle_bound = plt.Circle((0, -0.15), r_base, facecolor='none',
                                   edgecolor=color, linewidth=1.0,
                                   linestyle=':', alpha=0.4)
        ax.add_patch(circle_bound)

    else:
        theta = np.linspace(0, 3 * np.pi, 400)
        r_base = 0.3
        amplitude = 0.08 * np.exp(0.25 * theta)
        r = r_base + amplitude * np.sin(theta * 2.5)
        r = np.clip(r, 0, 1.2)
        x = r * np.cos(theta)
        y = r * np.sin(theta) - 0.15
        ax.plot(x, y, color=color, linewidth=2.0)
        ax.annotate('', xy=(x[-1], y[-1]),
                    xytext=(x[-3], y[-3]),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))

    ax.text(0, -1.45, example, ha='center', va='top',
            fontsize=9, color=SILVER,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=DIM, alpha=0.8))

save(fig, 'game1_08_feedback_loops.png')


# ── summary ───────────────────────────────────────────────────────
print("\nHOWL GAME-1-2026 — All 8 figures:")
print("  1. game1_01_temporal_profiles.png")
print("  2. game1_02_design_space.png")
print("  3. game1_03_expression_pressure.png")
print("  4. game1_04_engagement_density.png")
print("  5. game1_05_loop_hierarchy.png")
print("  6. game1_06_gating_pipeline.png")
print("  7. game1_07_cognitive_budget.png")
print("  8. game1_08_feedback_loops.png")
print("Done.")
