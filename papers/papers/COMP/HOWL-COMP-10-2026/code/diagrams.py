#!/usr/bin/env python3
"""
HOWL COMP-10 Diagrams — Tall-Infra Data-Only Execution
8 figures covering the five-layer stack, the wall, DSP architecture,
envelope parameterization, logic block convergence, field replacement,
funnel architecture, and Prolog rule composition.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Color palette ──
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

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

def style_ax(ax, spines=True):
    ax.set_facecolor(PAN)
    if spines:
        for s in ax.spines.values():
            s.set_color(DIM)
            s.set_linewidth(0.5)
        ax.tick_params(colors=DIM, labelsize=9)
    else:
        ax.axis('off')


# ================================================================
# FIG 1: PALADIN BEHAVIOR SCORING HEATMAP
# Type: Comparison (D5 Type 6)
# Shows: How 21 behaviors gate on boolean prolog rules —
#        more considerations = more specific but lower raw score.
#        The pattern of activation is impossible to see in a list.
# ================================================================

behaviors = [
    ("Approach",           ["has_target", "cant_melee"]),
    ("Charge",             ["has_target", "cant_melee", "hp_healthy", "has_stamina"]),
    ("Cautious_Approach",  ["has_target", "cant_melee", "hp_low"]),
    ("Strike",             ["has_target", "can_melee", "has_stamina", "target_in_front"]),
    ("Strike_Tired",       ["has_target", "can_melee", "stamina_low"]),
    ("Strike_Low_Stamina", ["has_target", "can_melee"]),
    ("Quick_Dispatch",     ["has_target", "can_melee", "has_stamina"]),
    ("Execute_Wounded",    ["has_target", "can_melee", "has_stamina"]),
    ("Power_Strike_Heavy", ["has_target", "can_melee", "stamina_high", "target_in_front"]),
    ("RangedAttack",       ["has_target", "can_ranged", "has_stamina"]),
    ("RangedAttack_Tired", ["has_target", "can_ranged", "stamina_low"]),
    ("Kite_RangedStrike",  ["has_target", "can_ranged", "has_stamina", "hp_low"]),
    ("FaceTarget",         ["has_target", "can_melee", "target_not_in_front"]),
    ("FaceTarget_Ranged",  ["has_target", "can_ranged", "target_not_in_front"]),
    ("Dodge",              ["has_target", "was_attacked", "has_stamina"]),
    ("Dodge_Critical",     ["has_target", "hp_critical", "has_stamina"]),
    ("Retreat",            ["has_target", "hp_critical", "stamina_low"]),
    ("Block",              ["has_target", "can_melee", "was_attacked", "has_stamina"]),
    ("Retaliate",          ["has_target", "can_melee", "was_attacked", "target_in_front", "has_stamina"]),
    ("Wait_For_Opening",   ["has_target", "target_not_in_front"]),
    ("Recover_Stamina",    ["has_target", "stamina_low", "cant_melee"]),
]

all_considerations = []
for _, cons in behaviors:
    for c in cons:
        if c not in all_considerations:
            all_considerations.append(c)

n_beh = len(behaviors)
n_con = len(all_considerations)
matrix = np.zeros((n_beh, n_con))
for i, (name, cons) in enumerate(behaviors):
    for c in cons:
        j = all_considerations.index(c)
        matrix[i, j] = 1.0

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
style_ax(ax, spines=False)

cell_w = 1.0
cell_h = 1.0
pad = 0.08

for i in range(n_beh):
    for j in range(n_con):
        x = j * cell_w
        y = (n_beh - 1 - i) * cell_h
        if matrix[i, j] > 0:
            color = CYAN
            alpha = 0.75
        else:
            color = DIM
            alpha = 0.12
        rect = FancyBboxPatch((x + pad, y + pad), cell_w - 2*pad, cell_h - 2*pad,
                              boxstyle="round,pad=0.05", facecolor=color, alpha=alpha,
                              edgecolor=DIM, linewidth=0.3)
        ax.add_patch(rect)

# Behavior labels on left
for i, (name, cons) in enumerate(behaviors):
    y = (n_beh - 1 - i) * cell_h + cell_h / 2
    count = len(cons)
    ax.text(-0.5, y, name, ha='right', va='center', fontsize=8, color=WHITE,
            fontweight='normal')
    # Count badge
    ax.text(n_con * cell_w + 0.4, y, "%d" % count, ha='left', va='center',
            fontsize=9, color=GOLD, fontweight='bold')

# Consideration labels on top
for j, con in enumerate(all_considerations):
    x = j * cell_w + cell_w / 2
    ax.text(x, n_beh * cell_h + 0.75, con, ha='center', va='bottom', fontsize=7.5,
            color=SILVER, rotation=55, rotation_mode='anchor')

# Column header
ax.text(n_con * cell_w + 0.4, n_beh * cell_h + 0.3, "Count", ha='left', va='bottom',
        fontsize=9, color=GOLD, fontweight='bold')

ax.set_xlim(-6.5, n_con * cell_w + 2.0)
ax.set_ylim(-1.5, n_beh * cell_h + 4.5)

ax.set_title("Paladin Combat AI — 21 Behaviors, Zero Code\nEach row is a behavior. Cyan cells are required Prolog rules. More rules = more specific.",
             fontsize=14, fontweight='bold', color=GOLD, pad=20)

# Legend
legend_y = -0.8
ax.add_patch(FancyBboxPatch((0, legend_y), 0.8, 0.6, boxstyle="round,pad=0.05",
             facecolor=CYAN, alpha=0.75, edgecolor=DIM, linewidth=0.3))
ax.text(1.2, legend_y + 0.3, "= Rule required (must pass)", ha='left', va='center',
        fontsize=9, color=SILVER)
ax.add_patch(FancyBboxPatch((8, legend_y), 0.8, 0.6, boxstyle="round,pad=0.05",
             facecolor=DIM, alpha=0.12, edgecolor=DIM, linewidth=0.3))
ax.text(9.2, legend_y + 0.3, "= Not required", ha='left', va='center',
        fontsize=9, color=SILVER)
ax.text(0, legend_y - 0.6, "Multiplicative scoring: any failing rule zeroes the entire behavior. More rules = lower score but higher specificity.",
        fontsize=8, color=DIM)

save(fig, "comp10_01_paladin_heatmap.png")


# ================================================================
# FIG 2: FIVE-LAYER STACK WITH COMPLETION STATUS
# Type: Scale/Landscape (D5 Type 2)
# Shows: The sandwich structure — two finished layers below,
#        one completable layer in the middle, two infinite layers above.
#        Text describes this linearly; the diagram shows the spatial
#        relationship and the asymmetry between finite and infinite.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 11), facecolor=BG)
style_ax(ax, spines=False)

layers = [
    ("Hardware",     "Transistors, ALUs, memory, buses",    "Settled",         GREEN,  0.7),
    ("Firmware",     "BIOS, device drivers, microcode",     "Settled",         GREEN,  0.6),
    ("Software",     "Compiled binary — the tall-infra",    "Completable",     GOLD,   0.7),
    ("Applications", "Games, tools, dashboards, editors",   "Ongoing forever", CYAN,   0.5),
    ("Services",     "APIs, data pipelines, integrations",  "Ongoing forever", CYAN,   0.4),
]

box_w = 10
box_h = 1.4
gap = 0.5
start_x = 1.0
start_y = 1.0

for i, (name, desc, status, color, alpha) in enumerate(layers):
    y = start_y + i * (box_h + gap)
    rect = FancyBboxPatch((start_x, y), box_w, box_h,
                          boxstyle="round,pad=0.15", facecolor=color, alpha=alpha * 0.25,
                          edgecolor=color, linewidth=2)
    ax.add_patch(rect)

    ax.text(start_x + 0.6, y + box_h * 0.62, name, ha='left', va='center',
            fontsize=14, fontweight='bold', color=color)
    ax.text(start_x + 0.6, y + box_h * 0.25, desc, ha='left', va='center',
            fontsize=9, color=SILVER)

    # Status badge on right
    badge_x = start_x + box_w - 0.5
    ax.text(badge_x, y + box_h * 0.5, status, ha='right', va='center',
            fontsize=11, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, linewidth=1.2))

# Bracket: finite layers
bracket_x = start_x + box_w + 1.2
y_hw = start_y + box_h * 0.5
y_sw = start_y + 2 * (box_h + gap) + box_h * 0.5
ax.annotate("", xy=(bracket_x, y_hw), xytext=(bracket_x, y_sw),
            arrowprops=dict(arrowstyle='-', color=GREEN, lw=2))
ax.plot([bracket_x - 0.15, bracket_x + 0.15], [y_hw, y_hw], color=GREEN, lw=2)
ax.plot([bracket_x - 0.15, bracket_x + 0.15], [y_sw, y_sw], color=GREEN, lw=2)
ax.text(bracket_x + 0.5, (y_hw + y_sw) / 2, "Engineering\n(finite,\ncompletable)",
        ha='left', va='center', fontsize=10, color=GREEN, fontweight='bold')

# Bracket: infinite layers
y_app = start_y + 3 * (box_h + gap) + box_h * 0.5
y_svc = start_y + 4 * (box_h + gap) + box_h * 0.5
ax.annotate("", xy=(bracket_x, y_app), xytext=(bracket_x, y_svc),
            arrowprops=dict(arrowstyle='-', color=CYAN, lw=2))
ax.plot([bracket_x - 0.15, bracket_x + 0.15], [y_app, y_app], color=CYAN, lw=2)
ax.plot([bracket_x - 0.15, bracket_x + 0.15], [y_svc, y_svc], color=CYAN, lw=2)
ax.text(bracket_x + 0.5, (y_app + y_svc) / 2, "Creativity\n(infinite,\ngoal-driven)",
        ha='left', va='center', fontsize=10, color=CYAN, fontweight='bold')

# Dividing line
div_y = start_y + 2.5 * (box_h + gap) + box_h * 0.5
ax.axhline(y=div_y, xmin=0.05, xmax=0.75, color=ORANGE, linewidth=1.5,
           linestyle='--', alpha=0.6)
ax.text(start_x + box_w / 2, div_y + 0.25, "The boundary: infrastructure below, goals above",
        ha='center', va='bottom', fontsize=9, color=ORANGE, fontstyle='italic')

ax.set_xlim(-0.5, 16)
ax.set_ylim(0, start_y + 5 * (box_h + gap) + 1.5)

ax.set_title("The Five-Layer Stack — Where Software Ends",
             fontsize=16, fontweight='bold', color=GOLD, pad=20)

save(fig, "comp10_02_five_layer_stack.png")


# ================================================================
# FIG 3: THE WALL MOVING THROUGH ENGINE ERAS
# Type: Progression/Sequence (D5 Type 7)
# Shows: How the boundary between data and compiled behavior moved
#        down over 30 years but never reached zero — until data-only.
#        The visual convergence that never completes is the argument.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, spines=True)

eras = ["1990s\nQuake\nHalf-Life", "2000s\nUnreal\nUnity", "2010s\nECS\nOverwatch",
        "2020s\nBevy\nDOTS", "Data-Only\nTall-Infra"]

# Percentage of behavior in code vs data (illustrative)
code_pct = [85, 65, 45, 30, 0]
data_pct = [15, 35, 55, 70, 100]

x = np.arange(len(eras))
bar_width = 0.55

bars_code = ax.bar(x, code_pct, bar_width, color=RED, alpha=0.65, edgecolor=RED,
                   linewidth=1.5, label='Compiled Behavior')
bars_data = ax.bar(x, data_pct, bar_width, bottom=code_pct, color=GREEN, alpha=0.55,
                   edgecolor=GREEN, linewidth=1.5, label='Data')

# The wall line
wall_y = code_pct
ax.plot(x, wall_y, color=ORANGE, linewidth=3, marker='o', markersize=10,
        markerfacecolor=ORANGE, markeredgecolor=WHITE, markeredgewidth=2,
        zorder=10, label='The Wall')

# Label the wall position
for i in range(len(eras)):
    if code_pct[i] > 0:
        ax.text(x[i], code_pct[i] + 2.5, "%d%%" % code_pct[i], ha='center', va='bottom',
                fontsize=10, fontweight='bold', color=ORANGE)
    else:
        ax.text(x[i], 3, "0%", ha='center', va='bottom',
                fontsize=12, fontweight='bold', color=GOLD)

# Annotations for anti-examples
notes = [
    "AI routines,\nweapon code",
    "Gameplay classes,\ndamage calcs",
    "Hero-specific\nsystems",
    "Compiled\nRust/C# systems",
    "Binary knows\nno domain nouns"
]
for i, note in enumerate(notes):
    note_y = code_pct[i] / 2 if code_pct[i] > 10 else 8
    col = WHITE if code_pct[i] > 10 else GOLD
    ax.text(x[i], note_y, note, ha='center', va='center', fontsize=7.5, color=col,
            fontstyle='italic')

ax.set_xticks(x)
ax.set_xticklabels([e for e in eras], fontsize=9, color=SILVER)
ax.set_ylabel("Proportion (%)", fontsize=11, color=SILVER)
ax.set_ylim(0, 115)
ax.set_xlim(-0.6, len(eras) - 0.4)

ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

ax.set_title("The Wall — 30 Years of Moving the Boundary, Never Eliminating It",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Annotation arrow to data-only
ax.annotate("Wall eliminated", xy=(4, 0), xytext=(3.2, 18),
            fontsize=10, fontweight='bold', color=GOLD,
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

save(fig, "comp10_03_wall_eras.png")


# ================================================================
# FIG 4: ENVELOPE PARAMETERIZATION LANDSCAPE
# Type: Running/Convergence (D5 Type 1)
# Shows: Five different game effects as amplitude-over-time curves,
#        all produced by the same envelope pipeline with different
#        parameters. The visual identity of the curves proves they
#        are the same code path. Text lists parameters; the diagram
#        shows the shapes.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, spines=True)

t = np.linspace(0, 12, 1000)

# Sword strike: short spike at t~0.3
sword = np.zeros_like(t)
mask = (t >= 0.15) & (t <= 0.45)
sword[mask] = 25 * np.sin((t[mask] - 0.15) / 0.3 * np.pi)

# Poison: periodic ticks
poison = np.zeros_like(t)
for tick_t in np.arange(0.5, 10.5, 1.0):
    pmask = (t >= tick_t) & (t < tick_t + 0.15)
    poison[pmask] = 5

# Shield buff: sustained plateau
shield = np.zeros_like(t)
smask = (t >= 0.2) & (t <= 8.0)
shield_attack = (t >= 0.2) & (t < 0.6)
shield_sustain = (t >= 0.6) & (t <= 7.5)
shield_release = (t > 7.5) & (t <= 8.0)
shield[shield_attack] = 15 * (t[shield_attack] - 0.2) / 0.4
shield[shield_sustain] = 15
shield[shield_release] = 15 * (8.0 - t[shield_release]) / 0.5

# Healing potion: instant spike
heal = np.zeros_like(t)
hmask = (t >= 1.0) & (t <= 1.08)
heal[hmask] = 50

# Passive enchant: flat forever
enchant = np.ones_like(t) * 10
enchant[t < 0.1] = 0

# Plot all
ax.fill_between(t, 0, sword, alpha=0.2, color=RED)
ax.plot(t, sword, color=RED, linewidth=2.5, label='Sword Strike (0.3s, -25 HP)')

ax.fill_between(t, 0, poison, alpha=0.15, color=MAG)
ax.plot(t, poison, color=MAG, linewidth=2, label='Poison (10s, -5/tick)')

ax.fill_between(t, 0, shield, alpha=0.12, color=BLUE)
ax.plot(t, shield, color=BLUE, linewidth=2, label='Shield Buff (30s, +15 armor)')

ax.fill_between(t, 0, heal, alpha=0.25, color=GREEN)
ax.plot(t, heal, color=GREEN, linewidth=2.5, label='Healing Potion (instant, +50 HP)')

ax.plot(t, enchant, color=PURPLE, linewidth=2, linestyle='--',
        label='Passive Enchant (permanent, +10 fire)')

# Annotations with offsets
ax.annotate("Spike: 0.3s duration", xy=(0.3, 25), xytext=(1.5, 42),
            fontsize=9, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.annotate("Ticks every 1.0s", xy=(3.5, 5), xytext=(4.5, 18),
            fontsize=9, color=MAG, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

ax.annotate("Attack / Sustain / Release", xy=(4.0, 15), xytext=(5.5, 32),
            fontsize=9, color=BLUE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5))

ax.annotate("Instant: resolves\nin one frame", xy=(1.04, 50), xytext=(2.2, 52),
            fontsize=9, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

ax.text(10.5, 11.5, "Never expires\n(duration = -1)", fontsize=9, color=PURPLE,
        fontweight='bold')

ax.set_xlabel("Time (seconds)", fontsize=11, color=SILVER)
ax.set_ylabel("Effect Magnitude", fontsize=11, color=SILVER)
ax.set_xlim(-0.5, 12.5)
ax.set_ylim(-3, 58)

ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

ax.set_title("Five Effects, One Pipeline — All Envelopes With Different Parameters",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Key insight box
ax.text(6.0, -1.5,
        "Same code path. Same envelope processor. Difference is parameterization only.",
        fontsize=9, color=GOLD, fontstyle='italic', ha='center')

save(fig, "comp10_04_envelope_landscape.png")


# ================================================================
# FIG 5: LOGIC BLOCK CONVERGENCE CURVE
# Type: Running/Convergence (D5 Type 1)
# Shows: New primitives required per application decays toward zero.
#        The SHAPE of the asymptotic approach is the completion
#        argument. Text says "it converges." The curve shows how.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, spines=True)

apps = np.arange(1, 16)
# Modeled decay: rapid early additions, asymptotic approach to zero
new_primitives = np.array([28, 15, 9, 6, 4, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0])
cumulative = np.cumsum(new_primitives)

# Primary curve: new per app
ax.bar(apps - 0.2, new_primitives, width=0.35, color=CYAN, alpha=0.7,
       edgecolor=CYAN, linewidth=1.5, label='New primitives this app', zorder=5)

# Cumulative curve on secondary axis
ax2 = ax.twinx()
ax2.set_facecolor('none')
ax2.plot(apps, cumulative, color=GOLD, linewidth=2.5, marker='o', markersize=8,
         markerfacecolor=GOLD, markeredgecolor=WHITE, markeredgewidth=1.5,
         label='Cumulative total', zorder=6)
ax2.set_ylabel("Cumulative Primitives", fontsize=11, color=GOLD)
ax2.tick_params(colors=GOLD, labelsize=9)
for s in ax2.spines.values():
    s.set_color(DIM)
    s.set_linewidth(0.5)

# Label key points
for i, v in enumerate(new_primitives):
    if v > 0:
        ax.text(apps[i] - 0.2, v + 0.8, str(v), ha='center', va='bottom',
                fontsize=9, color=CYAN, fontweight='bold')

# Completion zone
ax.axvspan(10.5, 15.5, alpha=0.06, color=GREEN)
ax.text(13, max(new_primitives) * 0.85, "Composition\nreplaces\nextension",
        ha='center', va='center', fontsize=11, color=GREEN, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, linewidth=1.2))

# Zero line
ax.axhline(y=0, color=DIM, linewidth=1, linestyle='-', alpha=0.5)

# Convergence annotation
ax.annotate("Binary scope finalized", xy=(11, 0), xytext=(8.5, 12),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.set_xlabel("Application Number (shipped on tall-infra)", fontsize=11, color=SILVER)
ax.set_ylabel("New Logic Block Types Added", fontsize=11, color=CYAN)
ax.set_xlim(0.2, 15.8)
ax.set_ylim(-2, max(new_primitives) + 5)
ax2.set_ylim(0, max(cumulative) + 8)

# Combined legend
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right',
          facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

ax.set_title("Logic Block Convergence — New Primitives Per Application",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, "comp10_05_lb_convergence.png")


# ================================================================
# FIG 6: FIELD REPLACEMENT — SAME DATA, DIFFERENT DOMAIN
# Type: Connection/Integer Map (D5 Type 5)
# Shows: How the same f32/i32 struct fields serve two completely
#        different domains through label replacement only. Arrows
#        from both domains converge on identical center fields.
#        The visual identity is impossible to convey in text.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
style_ax(ax, spines=False)

# Center column: actual struct fields
struct_fields = [
    ("character.health.value", "f32"),
    ("character.health.base_value", "f32"),
    ("character.stamina.value", "f32"),
    ("character.stamina.base_value", "f32"),
    ("character.level", "i32"),
    ("equipment.slot_0.count", "i32"),
    ("character.armor_rating", "f32"),
]

# Game domain labels
game_labels = [
    "Health",
    "Max Health",
    "Stamina",
    "Max Stamina",
    "Character Level",
    "Inventory Count",
    "Armor Rating",
]

# Business domain labels
biz_labels = [
    "Current Revenue",
    "Revenue Target",
    "Operating Budget",
    "Budget Ceiling",
    "Fiscal Quarter",
    "Transaction Count",
    "Insurance Cap",
]

center_x = 9.0
left_x = 2.0
right_x = 16.0
start_y = 1.5
row_h = 1.3
box_w = 4.5
box_h = 0.85

for i, (field, ftype) in enumerate(struct_fields):
    y = start_y + i * row_h

    # Center box
    rect = FancyBboxPatch((center_x - box_w/2, y - box_h/2), box_w, box_h,
                          boxstyle="round,pad=0.12", facecolor=PAN,
                          edgecolor=SILVER, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(center_x, y + 0.08, field, ha='center', va='center', fontsize=8.5,
            color=WHITE, fontfamily='monospace')
    ax.text(center_x, y - 0.22, ftype, ha='center', va='center', fontsize=7.5,
            color=DIM, fontfamily='monospace')

    # Game label (left)
    rect_l = FancyBboxPatch((left_x - 1.8, y - box_h/2), 3.6, box_h,
                            boxstyle="round,pad=0.12", facecolor=BG,
                            edgecolor=GREEN, linewidth=1.5)
    ax.add_patch(rect_l)
    ax.text(left_x, y, game_labels[i], ha='center', va='center', fontsize=10,
            color=GREEN, fontweight='bold')

    # Business label (right)
    rect_r = FancyBboxPatch((right_x - 1.8, y - box_h/2), 3.6, box_h,
                            boxstyle="round,pad=0.12", facecolor=BG,
                            edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(rect_r)
    ax.text(right_x, y, biz_labels[i], ha='center', va='center', fontsize=10,
            color=CYAN, fontweight='bold')

    # Arrows
    ax.annotate("", xy=(center_x - box_w/2 - 0.1, y), xytext=(left_x + 1.9, y),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, alpha=0.6))
    ax.annotate("", xy=(center_x + box_w/2 + 0.1, y), xytext=(right_x - 1.9, y),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5, alpha=0.6))

# Column headers
header_y = start_y + len(struct_fields) * row_h + 0.3
ax.text(left_x, header_y, "Game Domain\nsilo_field_replacement_id = -1",
        ha='center', va='bottom', fontsize=12, color=GREEN, fontweight='bold')
ax.text(center_x, header_y, "Actual Struct Fields\n(unchanged in binary)",
        ha='center', va='bottom', fontsize=12, color=SILVER, fontweight='bold')
ax.text(right_x, header_y, "Business Domain\nsilo_field_replacement_id = 42",
        ha='center', va='bottom', fontsize=12, color=CYAN, fontweight='bold')

ax.set_xlim(-1, 19.5)
ax.set_ylim(0, header_y + 2.5)

ax.set_title("Field Replacement — Same f32, Different Universe\nZero code change. Same pipeline. Same binary. Different labels.",
             fontsize=15, fontweight='bold', color=GOLD, pad=20)

# Key insight
ax.text(9.0, 0.4,
        "The binary processes f32 envelopes. It does not know if the f32 is health or revenue.",
        ha='center', va='center', fontsize=9.5, color=GOLD, fontstyle='italic')

save(fig, "comp10_06_field_replacement.png")


# ================================================================
# FIG 7: DSP FUNNEL — CANDIDATE REDUCTION PER LAYER
# Type: Threshold/Region (D5 Type 3)
# Shows: The funnel architecture narrowing from all possible
#        behaviors down to one winning action. The geometric shape
#        of the funnel IS the architecture. Each layer filters.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12), facecolor=BG)
style_ax(ax, spines=False)

layers = [
    ("All Possible Behaviors", "Everything the entity could ever do", None, DIM, 10.0),
    ("State Machine", "What am I doing overall?", "State-valid behaviors", BLUE, 8.0),
    ("Prolog Rules", "Are preconditions met?", "Precondition-satisfied", PURPLE, 6.0),
    ("Utility AI", "Which scores highest?", "Single winning behavior", CYAN, 4.0),
    ("Logic Blocks", "How do I execute?", "Field modifications", GREEN, 2.5),
    ("Envelopes", "Apply stat transformations", "Final frame values", GOLD, 1.5),
]

center_x = 8.0
start_y = 1.5
layer_h = 1.5
gap = 0.4

for i, (name, question, output, color, width) in enumerate(layers):
    y = start_y + (len(layers) - 1 - i) * (layer_h + gap)

    # Trapezoid-like shape using a rounded box
    rect = FancyBboxPatch((center_x - width/2, y), width, layer_h,
                          boxstyle="round,pad=0.15", facecolor=color, alpha=0.18,
                          edgecolor=color, linewidth=2)
    ax.add_patch(rect)

    # Name on left inside
    ax.text(center_x, y + layer_h * 0.65, name, ha='center', va='center',
            fontsize=12, fontweight='bold', color=color)

    # Question below name
    ax.text(center_x, y + layer_h * 0.3, question, ha='center', va='center',
            fontsize=9, color=SILVER, fontstyle='italic')

    # Output label on right side
    if output:
        ax.text(center_x + width/2 + 0.5, y + layer_h * 0.5, output,
                ha='left', va='center', fontsize=9, color=color,
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color,
                          linewidth=0.8, alpha=0.8))

    # Downward arrow between layers (except last)
    if i < len(layers) - 1:
        next_width = layers[i + 1][4]
        arrow_y = y - gap * 0.5
        ax.annotate("", xy=(center_x, arrow_y), xytext=(center_x, arrow_y + gap * 0.3),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Count annotations on left
counts = ["~1000", "~50", "~20", "~5", "1", "1"]
for i, count in enumerate(counts):
    y = start_y + (len(layers) - 1 - i) * (layer_h + gap)
    width = layers[i][4]
    ax.text(center_x - width/2 - 0.5, y + layer_h * 0.5, count,
            ha='right', va='center', fontsize=11, fontweight='bold', color=layers[i][3])

ax.text(center_x - 5.5, start_y + (len(layers) - 0.3) * (layer_h + gap),
        "Candidates", ha='center', va='center', fontsize=10, color=SILVER,
        fontweight='bold')

ax.set_xlim(0, 16)
ax.set_ylim(0, start_y + len(layers) * (layer_h + gap) + 2.0)

ax.set_title("The Funnel — Each Layer Reduces the Candidate Set\nFrom all possible behaviors to one winning action per entity per frame",
             fontsize=15, fontweight='bold', color=GOLD, pad=20)

save(fig, "comp10_07_dsp_funnel.png")


# ================================================================
# FIG 8: PROLOG RULE COMPOSITION TREE
# Type: Connection/Integer Map (D5 Type 5)
# Shows: How base predicates (entity field reads) compose into
#        derived rules, which compose further into complex conditions.
#        The tree structure with actual predicates and thresholds
#        at each node is impossible to convey in prose.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
style_ax(ax, spines=False)

def draw_rule_box(ax, x, y, text, color, w=3.0, h=0.7, fontsize=9.5):
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.15", facecolor=BG,
                          edgecolor=color, linewidth=1.8)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=color, fontweight='bold')
    return (x, y)

def draw_pred_box(ax, x, y, text, color=SILVER, w=3.2, h=0.55):
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.1", facecolor=PAN,
                          edgecolor=DIM, linewidth=1)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=8,
            color=color, fontfamily='monospace')

def connect(ax, x1, y1, x2, y2, color=DIM):
    ax.annotate("", xy=(x2, y2 + 0.35), xytext=(x1, y1 - 0.35),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.3, alpha=0.6))

# Layer 0: Base predicates (entity field reads)
base_y = 1.5
base_preds = [
    (2.5,  "awareness.target_entity_id"),
    (6.5,  "target_entity_distance(D)"),
    (10.5, "distance_melee(M)"),
    (14.5, "character.health.value(H)"),
]
for x, text in base_preds:
    draw_pred_box(ax, x, base_y, text, SILVER)

# Layer 0 label
ax.text(18, base_y, "Entity Field\nReads", ha='left', va='center',
        fontsize=9, color=DIM, fontstyle='italic')

# Layer 1: Comparison predicates
comp_y = 3.3
comp_preds = [
    (2.5,  "T != -1"),
    (5.5,  "T == -1"),
    (8.5,  "D < M"),
    (11.5, "D >= M"),
    (14.5, "H / MAX < 0.2"),
]
for x, text in comp_preds:
    draw_pred_box(ax, x, comp_y, text, ORANGE)

ax.text(18, comp_y, "Comparisons\n& Thresholds", ha='left', va='center',
        fontsize=9, color=DIM, fontstyle='italic')

# Connections: base to comparisons
connect(ax, 2.5, base_y, 2.5, comp_y, GREEN)
connect(ax, 2.5, base_y, 5.5, comp_y, GREEN)
connect(ax, 6.5, base_y, 8.5, comp_y, BLUE)
connect(ax, 10.5, base_y, 8.5, comp_y, BLUE)
connect(ax, 6.5, base_y, 11.5, comp_y, BLUE)
connect(ax, 10.5, base_y, 11.5, comp_y, BLUE)
connect(ax, 14.5, base_y, 14.5, comp_y, MAG)

# Layer 2: Derived rules
rule_y = 5.5
draw_rule_box(ax, 2.5, rule_y, "has_target", GREEN)
draw_rule_box(ax, 5.5, rule_y, "no_target", RED)
draw_rule_box(ax, 8.5, rule_y, "can_melee", CYAN)
draw_rule_box(ax, 11.5, rule_y, "cant_melee", ORANGE)
draw_rule_box(ax, 14.5, rule_y, "hp_critical", MAG)

ax.text(18, rule_y, "Derived\nRules", ha='left', va='center',
        fontsize=9, color=DIM, fontstyle='italic')

# Connections: comparisons to rules
connect(ax, 2.5, comp_y, 2.5, rule_y, GREEN)
connect(ax, 5.5, comp_y, 5.5, rule_y, RED)
connect(ax, 8.5, comp_y, 8.5, rule_y, CYAN)
connect(ax, 11.5, comp_y, 11.5, rule_y, ORANGE)
connect(ax, 14.5, comp_y, 14.5, rule_y, MAG)

# Layer 3: Composed rules
composed_y = 7.7
draw_rule_box(ax, 4.0, composed_y, "hp_low\nH/MAX < 0.4", MAG, w=3.2, h=0.9)
draw_rule_box(ax, 8.5, composed_y, "cornered\n3+ enemies AND hp_low", RED, w=4.0, h=0.9)
draw_rule_box(ax, 13.5, composed_y, "target_wounded\nHP > 0 AND HP < 0.2", PURPLE, w=4.0, h=0.9)

ax.text(18, composed_y, "Composed\nRules", ha='left', va='center',
        fontsize=9, color=DIM, fontstyle='italic')

# Connections to composed
connect(ax, 14.5, rule_y, 4.0, composed_y, MAG)
connect(ax, 14.5, rule_y, 8.5, composed_y, MAG)
connect(ax, 8.5, rule_y, 8.5, composed_y, CYAN)

# Layer 4: Used by behaviors
behavior_y = 9.8
draw_rule_box(ax, 3.0, behavior_y, "Retreat\n(hp_critical + stamina_low)", RED, w=4.5, h=0.9)
draw_rule_box(ax, 8.5, behavior_y, "Dodge_Critical\n(hp_critical + has_stamina)", ORANGE, w=4.5, h=0.9)
draw_rule_box(ax, 14.0, behavior_y, "Execute_Wounded\n(can_melee + has_stamina)", GREEN, w=4.5, h=0.9)

ax.text(18, behavior_y, "Behaviors\n(UAI scored)", ha='left', va='center',
        fontsize=9, color=DIM, fontstyle='italic')

# Connections to behaviors
connect(ax, 4.0, composed_y, 3.0, behavior_y, MAG)
connect(ax, 8.5, composed_y, 8.5, behavior_y, RED)
connect(ax, 13.5, composed_y, 14.0, behavior_y, PURPLE)
connect(ax, 14.5, rule_y, 8.5, behavior_y, MAG)

ax.set_xlim(-0.5, 20)
ax.set_ylim(0.3, 11.5)

ax.set_title("Prolog Rule Composition — From Entity Fields to Behavior Gating\nBase predicates compose into rules. Rules compose into conditions. Conditions gate behaviors.",
             fontsize=14, fontweight='bold', color=GOLD, pad=20)

save(fig, "comp10_08_prolog_composition.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n  COMP-10 Diagrams Complete:")
print("  1. comp10_01_paladin_heatmap.png")
print("  2. comp10_02_five_layer_stack.png")
print("  3. comp10_03_wall_eras.png")
print("  4. comp10_04_envelope_landscape.png")
print("  5. comp10_05_lb_convergence.png")
print("  6. comp10_06_field_replacement.png")
print("  7. comp10_07_dsp_funnel.png")
print("  8. comp10_08_prolog_composition.png")
