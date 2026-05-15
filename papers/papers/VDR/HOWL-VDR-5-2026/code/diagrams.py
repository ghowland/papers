
#!/usr/bin/env python3
"""
HOWL VDR-5 Diagrams — Exact Arithmetic Meets Logical Provenance
8 figures covering the VDR-LLM-Prolog architecture specification.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Output directory
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ---- Global Style ----

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

def rounded_box(ax, x, y, w, h, color, alpha=0.25, lw=1.5, ec=None):
    if ec is None:
        ec = color
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.15",
                         facecolor=color, alpha=alpha,
                         edgecolor=ec, linewidth=lw)
    ax.add_patch(box)
    return box

def arrow(ax, x1, y1, x2, y2, color=DIM, lw=1.5, style='->', head_w=8, head_l=6):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=12))


# ================================================================
# FIG 1: PROVENANCE CHAIN FOR ATTENTION WEIGHT
# Type: Progression/Sequence (D5.7)
# Shows: Complete derivation from raw text to output probability
#        with exact fractions at every stage
# ================================================================
print("Fig 1: Provenance chain")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 10)

stages = [
    ("Raw Text", '"the cat sat"', WHITE, 1.0),
    ("Tokenize", "[42, 17, 93]", SILVER, 3.0),
    ("Embed", "[3/7, 1/2]", CYAN, 5.0),
    ("Q\u00b7K\u1d40", "5/12", BLUE, 7.0),
    ("Softmax", "43545600\n/59565131", GREEN, 9.5),
    ("V Mix", "[11/15, 2/7]", PURPLE, 12.0),
    ("FF+ReLU", "[3/4, 1/9]", ORANGE, 14.0),
    ("Output P", "3/7", GOLD, 16.0),
]

stage_y = 5.5
label_y = 3.2
frac_y = 7.8

for i, (name, value, color, x) in enumerate(stages):
    rounded_box(ax, x, stage_y, 1.6, 1.4, color, alpha=0.2, lw=2, ec=color)
    ax.text(x, stage_y, name, ha='center', va='center',
            fontsize=9, fontweight='bold', color=color)
    ax.text(x, frac_y, value, ha='center', va='center',
            fontsize=8, color=WHITE, family='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, alpha=0.8))
    if i < len(stages) - 1:
        next_x = stages[i+1][3]
        ax.annotate('', xy=(next_x - 0.9, stage_y), xytext=(x + 0.9, stage_y),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, mutation_scale=15))

# provenance labels below
prov_labels = [
    (2.0, "source: file.txt", DIM),
    (4.0, "op: lookup", DIM),
    (6.0, "op: dot_product", DIM),
    (8.75, "op: softmax\nconstraint: sum=1", GREEN),
    (10.75, "op: weighted_sum", DIM),
    (13.0, "op: linear+relu", DIM),
    (15.0, "op: normalize\nconstraint: valid_dist", GOLD),
]
for x, label, color in prov_labels:
    ax.text(x, label_y, label, ha='center', va='center',
            fontsize=7, color=color, style='italic')

ax.text(8.5, 9.5, "Provenance Chain: Raw Text \u2192 Output Probability",
        ha='center', va='center', fontsize=15, fontweight='bold', color=GOLD)
ax.text(8.5, 1.8, "Every value is an exact VDR fraction. Every derivation step is a Prolog fact.",
        ha='center', va='center', fontsize=10, color=SILVER)

save(fig, "vdr5_01_provenance_chain.png")


# ================================================================
# FIG 2: EXACT GRADIENT CHAIN THROUGH NETWORK
# Type: Progression/Sequence (D5.7)
# Shows: Forward exact fractions and backward exact gradients
#        flowing through a 2-layer network
# ================================================================
print("Fig 2: Gradient chain")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 10)

# Network nodes: input -> linear1 -> relu -> linear2 -> loss
nodes = [
    ("Input", 1.5, SILVER),
    ("Linear\u2081", 4.5, CYAN),
    ("ReLU", 7.5, ORANGE),
    ("Linear\u2082", 10.5, BLUE),
    ("Loss", 13.5, RED),
]

fwd_y = 7.0
bwd_y = 3.0
node_y = 5.0

# forward values
fwd_vals = ["x=[1, 1]", "Wx+b\n=[8, 13]", "max(0,\u00b7)\n=[8, 13]", "Wx+b\n=[29]", "MSE\n=17/2"]
# backward gradients
bwd_vals = ["grad\n=[7, 10]", "grad\n=[1, 2]", "mask\n=[1, 1]", "grad\n=[1]", "\u22022L/\u2202p\n=1"]

for i, (name, x, color) in enumerate(nodes):
    rounded_box(ax, x, node_y, 2.2, 1.5, color, alpha=0.2, lw=2, ec=color)
    ax.text(x, node_y, name, ha='center', va='center',
            fontsize=10, fontweight='bold', color=color)

    ax.text(x, fwd_y, fwd_vals[i], ha='center', va='center',
            fontsize=8, color=GREEN, family='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN, alpha=0.5))

    ax.text(x, bwd_y, bwd_vals[i], ha='center', va='center',
            fontsize=8, color=MAG, family='monospace',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=MAG, alpha=0.5))

    if i < len(nodes) - 1:
        next_x = nodes[i+1][1]
        # forward arrow top
        ax.annotate('', xy=(next_x - 1.2, fwd_y), xytext=(x + 1.2, fwd_y),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, mutation_scale=12))
        # backward arrow bottom
        ax.annotate('', xy=(x + 1.2, bwd_y), xytext=(next_x - 1.2, bwd_y),
                    arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5, mutation_scale=12))

ax.text(1.5, fwd_y + 1.2, "FORWARD (exact fractions)", ha='center',
        fontsize=9, fontweight='bold', color=GREEN)
ax.text(1.5, bwd_y - 1.2, "BACKWARD (exact gradients)", ha='center',
        fontsize=9, fontweight='bold', color=MAG)

ax.text(7.5, 9.2, "Exact Gradient Chain: Forward Values and Backward Gradients",
        ha='center', va='center', fontsize=15, fontweight='bold', color=GOLD)
ax.text(7.5, 0.8, "d(x\u00b2)/dx at x=3 is exactly 6. MSE gradient is exactly 17/2. No float anywhere.",
        ha='center', va='center', fontsize=10, color=SILVER)

save(fig, "vdr5_02_gradient_chain.png")


# ================================================================
# FIG 3: IDENTITY CARD — VDR-LLM-PROLOG SYSTEM
# Type: Identity Card (D5.8)
# Shows: Three layers, key statistics, KB tree, exact fraction examples
# ================================================================
print("Fig 3: Identity card")

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 13)

# Title
ax.text(8, 12.2, "VDR-LLM-Prolog", ha='center', fontsize=22, fontweight='bold', color=GOLD)
ax.text(8, 11.4, "Exact Arithmetic \u00d7 Logical Provenance \u00d7 Scoped Knowledge",
        ha='center', fontsize=12, color=SILVER)

# Three layer boxes
layers = [
    ("Layer 3: Conversation", "Topics \u2022 Working Data \u2022 Constraints\n"
     "Scoped KBs \u2022 KB Surfacing", PURPLE, 9.5),
    ("Layer 2: Logic (Prolog)", "Facts \u2022 Rules \u2022 Derivations\n"
     "Unification \u2022 Constraint Verification", CYAN, 7.2),
    ("Layer 1: Arithmetic (VDR)", "Exact Fractions \u2022 Zero Drift\n"
     "Softmax \u2022 Autodiff \u2022 Transformer", GREEN, 4.9),
]

for name, desc, color, y in layers:
    rounded_box(ax, 4.5, y, 8.0, 1.8, color, alpha=0.12, lw=2, ec=color)
    ax.text(1.2, y + 0.3, name, ha='left', fontsize=11, fontweight='bold', color=color)
    ax.text(1.2, y - 0.4, desc, ha='left', fontsize=8, color=SILVER)

# Stats panel right side
stats_x = 12.5
stats = [
    ("705", "tests passed"),
    ("0", "VDR errors"),
    ("27", "modules"),
    ("23", "math domains"),
    ("24", "term types"),
    ("22", "Q335 constants"),
]
for i, (num, label) in enumerate(stats):
    y = 10.0 - i * 0.85
    ax.text(stats_x, y, num, ha='right', fontsize=14, fontweight='bold', color=GOLD)
    ax.text(stats_x + 0.3, y, label, ha='left', fontsize=9, color=SILVER)

# Key fractions panel bottom
ax.text(2.0, 3.0, "Key Exact Results:", fontsize=10, fontweight='bold', color=WHITE)
fracs = [
    ("softmax([1,2,3])[0]", "64826368 / 720042809"),
    ("attention sum", "= 1 exactly"),
    ("d(x\u00b2)/dx at x=3", "= 6 exactly"),
    ("\u03c0 (Q335)", "21988642587...314 / 2\u00b3\u00b3\u2075"),
]
for i, (label, val) in enumerate(fracs):
    y = 2.2 - i * 0.65
    ax.text(2.0, y, label + ":", fontsize=8, color=SILVER)
    ax.text(8.0, y, val, fontsize=8, color=GOLD, family='monospace')

save(fig, "vdr5_03_identity_card.png")


# ================================================================
# FIG 4: THREE-LAYER ARCHITECTURE STACK
# Type: Geometric Cross-Section (D5.4)
# Shows: VDR → Prolog → Conversation with data types flowing between
# ================================================================
print("Fig 4: Architecture stack")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 10)

ax.text(8, 9.3, "Three-Layer Architecture", ha='center',
        fontsize=16, fontweight='bold', color=GOLD)

# Layer boxes
layer_data = [
    (7.5, GREEN, "VDR Arithmetic", 1.8,
     ["Exact fractions [V, D, R]", "Softmax: sum = 1 exactly",
      "Autodiff: exact gradients", "Transformer: exact logits"]),
    (4.5, CYAN, "Prolog Logic Engine", 4.8,
     ["Facts: parameter_value(P, step(0), 1/4)",
      "Rules: depends_on(X,Y) :- derived_from(X,_,S), member(Y,S)",
      "Constraints: sum_to_one, gradient_bounded",
      "Unification: fraction(1,2) = fraction(2,4) exactly"]),
    (1.5, PURPLE, "Conversation Manager", 7.8,
     ["Scoped KBs: active/inactive by topic",
      "Working data: bob_age = 59 in story_b scope",
      "Topics: open/parked/closed lifecycle",
      "Surfacing: KB data direct to user, no LLM generation"]),
]

for y_center, color, title, y_pos, items in layer_data:
    rounded_box(ax, 8, y_pos, 14.0, 2.2, color, alpha=0.1, lw=2, ec=color)
    ax.text(1.5, y_pos + 0.6, title, fontsize=12, fontweight='bold', color=color)
    for j, item in enumerate(items):
        ax.text(1.8, y_pos + 0.1 - j * 0.4, "\u2022 " + item,
                fontsize=8, color=SILVER)

# flow arrows between layers
for y_top, y_bot, label, color in [
    (6.5, 6.0, "exact fractions \u2191\u2193 provenance facts", CYAN),
    (3.5, 3.0, "derivation chains \u2191\u2193 scoped queries", PURPLE),
]:
    ax.annotate('', xy=(8, y_top), xytext=(8, y_bot),
                arrowprops=dict(arrowstyle='<->', color=color, lw=2, mutation_scale=15))
    ax.text(12, (y_top + y_bot) / 2, label, fontsize=8, color=color, va='center')

save(fig, "vdr5_04_architecture_stack.png")


# ================================================================
# FIG 5: KB TREE WITH ACTIVE/INACTIVE SCOPING
# Type: Geometric Cross-Section (D5.4)
# Shows: Full hierarchy with active path illuminated, inactive dimmed
# ================================================================
print("Fig 5: KB tree scoping")

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 12)

ax.text(8, 11.3, "Knowledge Base Tree: Scoped Search",
        ha='center', fontsize=16, fontweight='bold', color=GOLD)
ax.text(8, 10.6, "Active topic: kb_vdr_llm. Gold = in scope. Dim = invisible to queries.",
        ha='center', fontsize=10, color=SILVER)

# Tree structure: (name, x, y, parent_x, parent_y, active)
tree_nodes = [
    ("kb_global", 8, 9.5, None, None, True),
    ("kb_project_vdr", 4, 7.5, 8, 9.5, True),
    ("kb_story_a", 12, 7.5, 8, 9.5, False),
    ("kb_story_b", 15, 7.5, 8, 9.5, False),
    ("kb_vdr_core", 2.5, 5.5, 4, 7.5, True),
    ("kb_math_series", 5.5, 5.5, 4, 7.5, False),
    ("kb_characters_a", 11, 5.5, 12, 7.5, False),
    ("kb_plot_a", 13, 5.5, 12, 7.5, False),
    ("kb_characters_b", 14.5, 5.5, 15, 7.5, False),
    ("kb_vdr_llm", 1.5, 3.5, 2.5, 5.5, True),
    ("kb_vdr_gyms", 4.0, 3.5, 2.5, 5.5, False),
    ("kb_vdr_training", 1.5, 1.5, 1.5, 3.5, True),
]

for name, x, y, px, py, active in tree_nodes:
    if active:
        color = GOLD
        alpha = 0.25
        text_color = GOLD
        lw = 2.5
    else:
        color = DIM
        alpha = 0.08
        text_color = DIM
        lw = 1.0

    rounded_box(ax, x, y, 2.4, 0.8, color, alpha=alpha, lw=lw, ec=color)
    ax.text(x, y, name.replace("kb_", ""), ha='center', va='center',
            fontsize=7.5, fontweight='bold' if active else 'normal', color=text_color)

    if px is not None:
        line_color = GOLD if active else DIM
        line_alpha = 0.8 if active else 0.3
        ax.plot([px, x], [py - 0.4, y + 0.4], color=line_color,
                alpha=line_alpha, lw=1.5 if active else 0.8)

# scope indicator
ax.text(1.5, 0.5, "\u2190 Active scope path: global \u2192 project_vdr \u2192 vdr_core \u2192 vdr_llm \u2192 vdr_training",
        fontsize=9, color=GOLD)
ax.text(12, 0.5, "Story KBs are OUT OF SCOPE \u2014 queries never reach them",
        fontsize=9, color=DIM)

save(fig, "vdr5_05_kb_tree_scoping.png")


# ================================================================
# FIG 6: SOFTMAX EXACT NORMALIZATION
# Type: Comparison Bar Chart (D5.6)
# Shows: Three exact fractions stacking to exactly 1
# ================================================================
print("Fig 6: Softmax exact bars")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)

# Left panel: VDR exact
ax1.set_facecolor(PAN)
fracs = [64826368/720042809, 176214841/720042809, 479001600/720042809]
labels = ["64826368\n/720042809", "176214841\n/720042809", "479001600\n/720042809"]
colors = [CYAN, BLUE, GREEN]
logit_labels = ["logit=1", "logit=2", "logit=3"]

bars = ax1.bar([0, 1, 2], fracs, color=colors, alpha=0.7, width=0.6,
               edgecolor=[CYAN, BLUE, GREEN], linewidth=2)

for i, (bar, label) in enumerate(zip(bars, labels)):
    ax1.text(i, bar.get_height() + 0.02, label,
             ha='center', va='bottom', fontsize=7, color=WHITE, family='monospace')
    ax1.text(i, -0.06, logit_labels[i],
             ha='center', va='top', fontsize=9, color=colors[i], fontweight='bold')

ax1.axhline(y=1.0, color=GOLD, linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(2.5, 1.02, "Sum = 1 exactly", fontsize=10, color=GOLD, fontweight='bold')

ax1.set_ylim(-0.12, 1.15)
ax1.set_xlim(-0.6, 2.8)
ax1.set_ylabel("Probability (exact fraction)", fontsize=11, color=SILVER)
ax1.set_title("VDR Softmax: Exact Fractions", fontsize=14, fontweight='bold', color=GREEN, pad=15)
ax1.set_xticks([])
for spine in ax1.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax1.tick_params(colors=DIM, labelsize=9)

# Right panel: Float comparison
ax2.set_facecolor(PAN)
float_vals = [0.09003057, 0.24472847, 0.66524096]
float_sum = sum(float_vals)

bars2 = ax2.bar([0, 1, 2], float_vals, color=colors, alpha=0.4, width=0.6,
                edgecolor=[CYAN, BLUE, GREEN], linewidth=1.5)

for i, bar in enumerate(bars2):
    ax2.text(i, bar.get_height() + 0.02, "%.8f" % float_vals[i],
             ha='center', va='bottom', fontsize=7, color=DIM, family='monospace')

ax2.axhline(y=1.0, color=RED, linestyle='--', linewidth=1.5, alpha=0.7)
ax2.text(2.4, 1.02, "Sum = %.15f" % float_sum, fontsize=8, color=RED, family='monospace')
ax2.text(2.4, 0.94, "\u2260 1", fontsize=12, color=RED, fontweight='bold')

ax2.set_ylim(-0.12, 1.15)
ax2.set_xlim(-0.6, 2.8)
ax2.set_ylabel("Probability (float64)", fontsize=11, color=SILVER)
ax2.set_title("Float Softmax: Silent Truncation", fontsize=14, fontweight='bold', color=RED, pad=15)
ax2.set_xticks([])
for spine in ax2.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax2.tick_params(colors=DIM, labelsize=9)

save(fig, "vdr5_06_softmax_exact_bars.png")


# ================================================================
# FIG 7: CONSTRAINT INHERITANCE THROUGH HIERARCHY
# Type: Progression/Sequence (D5.7)
# Shows: Org → Dept → Team → User with constraints accumulating
# ================================================================
print("Fig 7: Constraint inheritance")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 10)

ax.text(8, 9.3, "Constraint Inheritance Through Account Hierarchy",
        ha='center', fontsize=15, fontweight='bold', color=GOLD)

# Hierarchy levels
levels = [
    ("kb_global", 2.0, SILVER,
     ["exact_arithmetic", "sum_to_one"],
     "2 constraints"),
    ("org_acme_corp", 4.0, BLUE,
     ["gdpr_compliance", "data_retention_7yr"],
     "+2 = 4 total"),
    ("dept_engineering", 6.5, CYAN,
     ["code_review_req", "approved_langs\n  [py, zig, rust]"],
     "+2 = 6 total"),
    ("team_backend", 9.5, GREEN,
     ["database_logged", "approved_langs \u2192 OVERRIDE\n  [py, zig, rust, go]"],
     "+1 override = 7 total"),
    ("user_alice", 13.0, GOLD,
     ["30s_runtime (self)", "elevated_access (admin)"],
     "+2 = 9 total"),
]

level_y = 5.0
for i, (name, x, color, constraints, count_text) in enumerate(levels):
    rounded_box(ax, x, level_y, 2.6, 2.8, color, alpha=0.15, lw=2, ec=color)
    ax.text(x, level_y + 1.0, name, ha='center', fontsize=8, fontweight='bold', color=color)

    for j, c in enumerate(constraints):
        ax.text(x, level_y + 0.3 - j * 0.55, c, ha='center', fontsize=6.5,
                color=WHITE if "OVERRIDE" not in c else ORANGE)

    ax.text(x, level_y - 1.7, count_text, ha='center', fontsize=8,
            fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.5))

    if i < len(levels) - 1:
        next_x = levels[i+1][1]
        ax.annotate('', xy=(next_x - 1.4, level_y), xytext=(x + 1.4, level_y),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=2, mutation_scale=15))

# Override callout
ax.annotate("Override:\nteam adds Go\nto approved langs",
            xy=(9.5, level_y + 0.0), xytext=(9.5, 8.3),
            fontsize=8, color=ORANGE, ha='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.8))

ax.text(8, 1.5, "Constraints inherit downward. Children override by declaring same name. All transitions logged.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr5_07_constraint_inheritance.png")


# ================================================================
# FIG 8: MEMORY TIER RETENTION PYRAMID
# Type: Scale/Landscape (D5.2)
# Shows: Five tiers from persistent to transient with sizes
# ================================================================
print("Fig 8: Memory tier pyramid")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 10)

ax.text(8, 9.3, "Memory Tier Retention Pyramid",
        ha='center', fontsize=16, fontweight='bold', color=GOLD)

# Pyramid tiers (bottom = persistent, top = transient)
tiers = [
    ("Tier 1: Persistent", "Architecture, rules, axioms, accounts",
     "Never pruned", "~KB", GREEN, 1.2, 14.0),
    ("Tier 2: Checkpoint", "Parameter snapshots at declared steps",
     "Keep every Nth + anomaly", "~MB/ckpt", CYAN, 2.8, 11.5),
    ("Tier 3: Step-Transient", "Gradients, updates, intermediate state",
     "Prune unless retain_step(S)", "~KB/step", BLUE, 4.4, 9.0),
    ("Tier 4: Batch-Transient", "Embeddings, attention maps, logits",
     "Prune unless retain_batch(B)", "~MB/batch", PURPLE, 6.0, 6.5),
    ("Tier 5: Conv-Transient", "Per-turn drafts, reasoning traces",
     "Prune unless flagged", "~KB/turn", MAG, 7.6, 4.0),
]

for i, (name, contents, policy, size, color, y, width) in enumerate(tiers):
    x_center = 8
    h = 1.2
    box = FancyBboxPatch((x_center - width/2, y - h/2), width, h,
                         boxstyle="round,pad=0.12",
                         facecolor=color, alpha=0.12,
                         edgecolor=color, linewidth=2)
    ax.add_patch(box)

    ax.text(x_center - width/2 + 0.4, y + 0.15, name,
            fontsize=10, fontweight='bold', color=color)
    ax.text(x_center - width/2 + 0.4, y - 0.25, contents,
            fontsize=7.5, color=SILVER)

    ax.text(x_center + width/2 - 0.4, y + 0.15, size,
            fontsize=9, fontweight='bold', color=color, ha='right')
    ax.text(x_center + width/2 - 0.4, y - 0.25, policy,
            fontsize=7, color=DIM, ha='right', style='italic')

# Labels
ax.text(0.5, 1.2, "PERSISTENT\n(small, forever)", fontsize=9, color=GREEN,
        ha='center', fontweight='bold')
ax.text(0.5, 7.6, "TRANSIENT\n(large, pruned)", fontsize=9, color=MAG,
        ha='center', fontweight='bold')

ax.annotate('', xy=(0.5, 7.0), xytext=(0.5, 1.8),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2, mutation_scale=15))

ax.text(8, 0.2, "Retention policies are Prolog rules: declarative, inspectable, modifiable without code changes.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr5_08_memory_tiers.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n--- All 8 figures saved ---")
print("  vdr5_01_provenance_chain.png")
print("  vdr5_02_gradient_chain.png")
print("  vdr5_03_identity_card.png")
print("  vdr5_04_architecture_stack.png")
print("  vdr5_05_kb_tree_scoping.png")
print("  vdr5_06_softmax_exact_bars.png")
print("  vdr5_07_constraint_inheritance.png")
print("  vdr5_08_memory_tiers.png")
