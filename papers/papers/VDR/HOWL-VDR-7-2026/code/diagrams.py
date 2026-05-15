
#!/usr/bin/env python3
"""
HOWL VDR-7 Diagrams — Complete Lifecycle Technical Specification
8 figures covering training, feedback, deployment, and lifecycle.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Wedge
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)


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

def rbox(ax, x, y, w, h, color, alpha=0.2, lw=1.5, ec=None):
    if ec is None:
        ec = color
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.15",
                         facecolor=color, alpha=alpha,
                         edgecolor=ec, linewidth=lw)
    ax.add_patch(box)

def arr(ax, x1, y1, x2, y2, color=DIM, lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw, mutation_scale=13))


# ================================================================
# FIG 1: IDENTITY CARD
# Type: Identity Card (D5.8)
# Shows: Complete lifecycle at a glance
# ================================================================
print("Fig 1: Identity card")

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 13)

ax.text(8, 12.2, "VDR-7: Complete Lifecycle", ha='center',
        fontsize=22, fontweight='bold', color=GOLD)
ax.text(8, 11.4, "Training \u2022 Feedback \u2022 Evaluation \u2022 Deployment \u2022 Monitoring \u2022 Update",
        ha='center', fontsize=11, color=SILVER)

# 12 phases in two columns
phases_left = [
    ("1", "Data Sourcing", GREEN),
    ("2", "Corpus Preparation", GREEN),
    ("3", "Tokenization", CYAN),
    ("4", "Model Initialization", CYAN),
    ("5", "Pre-Training", BLUE),
    ("6", "Fine-Tuning", BLUE),
]
phases_right = [
    ("7", "Human Feedback", PURPLE),
    ("8", "Evaluation", ORANGE),
    ("9", "Deployment", GOLD),
    ("10", "Monitoring", MAG),
    ("11", "Update", RED),
    ("12", "Retirement", DIM),
]

for i, (num, name, color) in enumerate(phases_left):
    y = 10.0 - i * 0.85
    rbox(ax, 3.0, y, 5.0, 0.65, color, alpha=0.15, lw=1.5, ec=color)
    ax.text(1.0, y, num, fontsize=11, fontweight='bold', color=color)
    ax.text(1.5, y, name, fontsize=9, color=WHITE)

for i, (num, name, color) in enumerate(phases_right):
    y = 10.0 - i * 0.85
    rbox(ax, 11.5, y, 5.0, 0.65, color, alpha=0.15, lw=1.5, ec=color)
    ax.text(9.5, y, num, fontsize=11, fontweight='bold', color=color)
    ax.text(10.0, y, name, fontsize=9, color=WHITE)

# Key stats
ax.text(3.0, 3.5, "Key Numbers", fontsize=13, fontweight='bold', color=GOLD)
stats = [
    ("12", "lifecycle phases"),
    ("~60", "KB types total"),
    ("34", "modules"),
    ("255", "primitives"),
    ("~1652", "planned tests"),
    ("16", "build sprints"),
    ("0", "VDR computation errors (705 tests)"),
]
for i, (num, label) in enumerate(stats):
    y = 2.8 - i * 0.5
    ax.text(1.0, y, num, fontsize=11, fontweight='bold', color=GOLD)
    ax.text(2.5, y, label, fontsize=8, color=SILVER)

# Architecture layers
ax.text(11.5, 3.5, "Every Phase Is a KB", fontsize=13, fontweight='bold', color=CYAN, ha='center')
ax.text(11.5, 2.8, "Queryable \u2022 Constrainable \u2022 Versionable", ha='center',
        fontsize=9, color=SILVER)
ax.text(11.5, 2.2, "Surfaceable \u2022 Composable \u2022 Archivable", ha='center',
        fontsize=9, color=SILVER)
ax.text(11.5, 1.2, "The system is both\nAPI and Generator", ha='center',
        fontsize=11, fontweight='bold', color=GOLD)

save(fig, "vdr7_01_identity_card.png")


# ================================================================
# FIG 2: DATA LINEAGE CHAIN
# Type: Progression/Sequence (D5.7)
# Shows: Source → Corpus → Tokens → Model → Deploy with data at each
# ================================================================
print("Fig 2: Data lineage")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18)
ax.set_ylim(-0.5, 10)

ax.text(8.75, 9.3, "Data Lineage: Source to Deployment",
        ha='center', fontsize=16, fontweight='bold', color=GOLD)

stages = [
    ("Source", "wikipedia\n2026-03\nCC-BY-SA", GREEN, 1.5),
    ("Corpus", "1.5M docs\nfiltered\ndeduped", CYAN, 4.5),
    ("Tokens", "10B tokens\nBPE 32k\nvocab frozen", BLUE, 7.5),
    ("Pre-Train", "100k steps\nloss: 2.87\nckpt 100k", PURPLE, 10.5),
    ("Align", "DPO\n5k prefs\nckpt_safe", MAG, 13.5),
    ("Deploy", "prod_v1\n99.9% up\nmonitored", GOLD, 16.5),
]

stage_y = 5.5
data_y = 3.0

for i, (name, data, color, x) in enumerate(stages):
    rbox(ax, x, stage_y, 2.4, 1.6, color, alpha=0.2, lw=2, ec=color)
    ax.text(x, stage_y, name, ha='center', va='center',
            fontsize=10, fontweight='bold', color=color)
    ax.text(x, data_y, data, ha='center', va='center', fontsize=7.5,
            color=WHITE, family='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))
    if i < len(stages) - 1:
        next_x = stages[i + 1][3]
        arr(ax, x + 1.3, stage_y, next_x - 1.3, stage_y, DIM, 2)

# KB labels above
for i, (name, _, color, x) in enumerate(stages):
    ax.text(x, 7.8, "KB: %s" % name.lower(), ha='center', fontsize=7,
            color=color, style='italic')
    ax.plot([x, x], [7.4, stage_y + 0.9], color=color, lw=0.8, linestyle=':', alpha=0.5)

ax.text(8.75, 1.2, "Every stage produces a KB. Every KB references its parent. The full chain is one Prolog query.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr7_02_data_lineage.png")


# ================================================================
# FIG 3: TRAINING METRICS — LOSS + LR + DENOMINATOR
# Type: Running/Convergence (D5.1)
# Shows: Three curves during training — shape is the finding
# ================================================================
print("Fig 3: Training metrics")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 12),
                                     gridspec_kw={'hspace': 0.35})
fig.patch.set_facecolor(BG)

steps = np.arange(0, 100001, 1000)
steps_f = steps.astype(float)

# Panel 1: Loss
ax1.set_facecolor(PAN)
loss = 10.0 * np.exp(-steps_f / 20000.0) + 2.5 + 0.3 * np.random.RandomState(42).randn(len(steps)) * np.exp(-steps_f / 30000.0)
loss = np.maximum(loss, 2.3)
ax1.plot(steps, loss, color=CYAN, lw=2.5, label='Training loss')
ax1.axhline(y=2.5, color=GREEN, linestyle='--', lw=1.5, alpha=0.6, label='Target')
ax1.set_ylabel("Loss (exact fraction)", fontsize=11, color=SILVER)
ax1.set_title("Training Loss", fontsize=14, fontweight='bold', color=CYAN, pad=10)
ax1.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)
ax1.set_xlim(0, 100000)
ax1.set_ylim(2.0, 12)
for spine in ax1.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax1.tick_params(colors=DIM, labelsize=9)
ax1.set_xlabel("")

# Panel 2: Learning rate
ax2.set_facecolor(PAN)
warmup = np.minimum(steps_f / 1000.0, 1.0)
cosine = 0.5 * (1.0 + np.cos(np.pi * np.clip((steps_f - 1000) / 99000, 0, 1)))
lr = 3e-4 * warmup * cosine
lr = np.maximum(lr, 1e-5)
ax2.plot(steps, lr * 10000, color=ORANGE, lw=2.5)
ax2.set_ylabel("LR \u00d7 10\u2074 (exact fraction)", fontsize=11, color=SILVER)
ax2.set_title("Learning Rate Schedule (warmup + cosine decay)", fontsize=14,
              fontweight='bold', color=ORANGE, pad=10)
ax2.axvline(x=1000, color=DIM, linestyle=':', lw=1, alpha=0.7)
ax2.text(1500, 2.8, "warmup\nends", fontsize=8, color=DIM)
ax2.set_xlim(0, 100000)
ax2.set_ylim(0, 3.5)
for spine in ax2.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax2.tick_params(colors=DIM, labelsize=9)

# Panel 3: Denominator growth
ax3.set_facecolor(PAN)
denom_bits = 10 + 35 * (1 - np.exp(-steps_f / 30000.0)) + np.random.RandomState(7).randn(len(steps)) * 0.5
# Add reprojection events (sudden drops)
for reproj_step in [30000, 60000, 85000]:
    idx = reproj_step // 1000
    denom_bits[idx:] = denom_bits[idx:] - (denom_bits[idx] - 20)

ax3.plot(steps, denom_bits, color=MAG, lw=2.5)
ax3.axhline(y=48, color=RED, linestyle='--', lw=1.5, alpha=0.6, label='Budget: 2\u2074\u2078')
ax3.axhline(y=20, color=GREEN, linestyle='--', lw=1.5, alpha=0.6, label='Post-reproject')

for reproj_step in [30000, 60000, 85000]:
    ax3.axvline(x=reproj_step, color=PURPLE, linestyle=':', lw=1, alpha=0.5)
    ax3.text(reproj_step + 1000, 50, "reproject", fontsize=7, color=PURPLE, rotation=90)

ax3.set_ylabel("Max denominator (bits)", fontsize=11, color=SILVER)
ax3.set_xlabel("Training step", fontsize=11, color=SILVER)
ax3.set_title("Denominator Growth (VDR-specific)", fontsize=14,
              fontweight='bold', color=MAG, pad=10)
ax3.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='upper left')
ax3.set_xlim(0, 100000)
ax3.set_ylim(5, 55)
for spine in ax3.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax3.tick_params(colors=DIM, labelsize=9)

save(fig, "vdr7_03_training_metrics.png")


# ================================================================
# FIG 4: EVAL COMPARISON ACROSS MODEL VERSIONS
# Type: Comparison Bar Chart (D5.6)
# Shows: Benchmark scores improving through training stages
# ================================================================
print("Fig 4: Eval comparison")

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

benchmarks = ["Perplexity\n(lower=better)", "Next-token\nAccuracy", "Safety\nRate", "Math\nAccuracy", "Instruction\nFollowing"]
models = ["Pre-trained", "Fine-tuned", "Aligned"]
colors_m = [BLUE, CYAN, GREEN]

# Values (illustrative exact fractions displayed as decimals for visual)
values = {
    "Pre-trained": [23.5, 0.45, 0.82, 0.30, 0.25],
    "Fine-tuned":  [21.0, 0.52, 0.88, 0.42, 0.71],
    "Aligned":     [22.0, 0.50, 0.96, 0.40, 0.75],
}

x = np.arange(len(benchmarks))
width = 0.22
offsets = [-width, 0, width]

for i, (model, color) in enumerate(zip(models, colors_m)):
    vals = values[model]
    # Normalize perplexity to 0-1 scale for visual (invert: lower is better)
    display_vals = list(vals)
    display_vals[0] = display_vals[0] / 30.0  # scale to fit
    bars = ax.bar(x + offsets[i], display_vals, width, color=color, alpha=0.7,
                  edgecolor=color, linewidth=1.5, label=model)
    for j, bar in enumerate(bars):
        val_text = "%.1f" % vals[j] if j == 0 else "%.0f%%" % (vals[j] * 100)
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                val_text, ha='center', va='bottom', fontsize=7.5,
                color=WHITE, fontweight='bold')

# Safety threshold
ax.axhline(y=0.95, color=GOLD, linestyle='--', lw=1.5, alpha=0.6)
ax.text(4.5, 0.96, "Safety threshold (95%)", fontsize=8, color=GOLD, ha='right')

ax.set_xticks(x)
ax.set_xticklabels(benchmarks, fontsize=9, color=SILVER)
ax.set_ylabel("Score (normalized)", fontsize=11, color=SILVER)
ax.set_title("Evaluation Across Training Stages", fontsize=16,
             fontweight='bold', color=GOLD, pad=15)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10, loc='upper left')
ax.set_ylim(0, 1.15)
ax.set_xlim(-0.5, len(benchmarks) - 0.3)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM, labelsize=9)

save(fig, "vdr7_04_eval_comparison.png")


# ================================================================
# FIG 5: FULL LIFECYCLE KB TREE
# Type: Geometric Cross-Section (D5.4)
# Shows: Nesting of KBs from source through retirement
# ================================================================
print("Fig 5: Lifecycle KB tree")

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 13)

ax.text(8, 12.2, "Lifecycle KB Tree: Every Phase Is a Node",
        ha='center', fontsize=16, fontweight='bold', color=GOLD)

# Tree nodes: (name, x, y, parent_x, parent_y, color)
nodes = [
    ("source_registry", 2.0, 10.5, None, None, GREEN),
    ("corpus_v1", 2.0, 8.8, 2.0, 10.5, GREEN),
    ("vocab_bpe_32k", 4.5, 8.8, 2.0, 10.5, CYAN),
    ("tokenized_v1", 3.2, 7.1, 2.0, 8.8, CYAN),
    ("model_arch_v1", 7.5, 10.5, None, None, BLUE),
    ("model_init_v1", 7.5, 8.8, 7.5, 10.5, BLUE),
    ("run_pretrain", 6.0, 7.1, 7.5, 8.8, BLUE),
    ("ckpt_100k", 6.0, 5.4, 6.0, 7.1, PURPLE),
    ("run_finetune", 8.5, 5.4, 6.0, 5.4, PURPLE),
    ("ckpt_instruct", 8.5, 3.7, 8.5, 5.4, MAG),
    ("feedback_r1", 11.0, 5.4, 8.5, 5.4, MAG),
    ("reward_model", 11.0, 3.7, 11.0, 5.4, MAG),
    ("run_rlhf", 10.0, 2.0, 8.5, 3.7, RED),
    ("ckpt_safe", 10.0, 0.5, 10.0, 2.0, GOLD),
    ("eval_suite", 13.0, 3.7, 10.0, 2.0, ORANGE),
    ("deploy_prod", 13.0, 2.0, 10.0, 0.5, GOLD),
    ("monitoring", 15.0, 2.0, 13.0, 2.0, MAG),
    ("retirement", 15.0, 0.5, 13.0, 2.0, DIM),
]

for name, x, y, px, py, color in nodes:
    rbox(ax, x, y, 2.3, 0.7, color, alpha=0.2, lw=1.5, ec=color)
    display = name.replace("_", "\n") if len(name) > 12 else name
    ax.text(x, y, display, ha='center', va='center', fontsize=6.5,
            fontweight='bold', color=color)
    if px is not None:
        ax.plot([px, x], [py - 0.4, y + 0.4], color=color, lw=1.2, alpha=0.6)

ax.text(8, -0.5, "Every node is a KB. Every edge is a parent-child reference. The entire lifecycle is one queryable tree.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr7_05_lifecycle_kb_tree.png")


# ================================================================
# FIG 6: CANARY DEPLOYMENT WITH THRESHOLDS
# Type: Threshold/Region (D5.3)
# Shows: Canary metrics with pass/fail regions
# ================================================================
print("Fig 6: Canary deployment")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)

hours = np.arange(0, 25)

# Left panel: Latency
ax1.set_facecolor(PAN)
baseline_lat = 1200
canary_lat = 1200 + np.random.RandomState(42).randn(25) * 80
control_lat = 1200 + np.random.RandomState(43).randn(25) * 60

threshold_lat = baseline_lat * 1.1

ax1.fill_between(hours, threshold_lat, 1600, alpha=0.06, color=RED)
ax1.axhline(y=threshold_lat, color=RED, linestyle='--', lw=1.5, alpha=0.7)
ax1.text(24.5, threshold_lat + 10, "110% baseline", fontsize=8, color=RED, ha='right')

ax1.plot(hours, canary_lat, color=CYAN, lw=2, marker='o', markersize=5, label='Canary')
ax1.plot(hours, control_lat, color=DIM, lw=1.5, linestyle='--', label='Control')

ax1.set_xlabel("Hours since canary start", fontsize=11, color=SILVER)
ax1.set_ylabel("P99 latency (ms)", fontsize=11, color=SILVER)
ax1.set_title("Latency: Canary vs Control", fontsize=14, fontweight='bold', color=CYAN, pad=10)
ax1.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)
ax1.set_xlim(0, 24)
ax1.set_ylim(900, 1600)
for spine in ax1.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax1.tick_params(colors=DIM, labelsize=9)

# Right panel: Safety rate
ax2.set_facecolor(PAN)
canary_safety = 0.97 + np.random.RandomState(44).randn(25) * 0.005
control_safety = 0.965 + np.random.RandomState(45).randn(25) * 0.005

ax2.fill_between(hours, 0.90, 0.95, alpha=0.06, color=RED)
ax2.axhline(y=0.95, color=RED, linestyle='--', lw=1.5, alpha=0.7)
ax2.text(24.5, 0.951, "95% minimum", fontsize=8, color=RED, ha='right')

ax2.fill_between(hours, 0.95, 1.0, alpha=0.04, color=GREEN)

ax2.plot(hours, canary_safety, color=GREEN, lw=2, marker='o', markersize=5, label='Canary')
ax2.plot(hours, control_safety, color=DIM, lw=1.5, linestyle='--', label='Control')

ax2.set_xlabel("Hours since canary start", fontsize=11, color=SILVER)
ax2.set_ylabel("Safety rate", fontsize=11, color=SILVER)
ax2.set_title("Safety: Canary vs Control", fontsize=14, fontweight='bold', color=GREEN, pad=10)
ax2.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='lower right')
ax2.set_xlim(0, 24)
ax2.set_ylim(0.90, 1.01)
for spine in ax2.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax2.tick_params(colors=DIM, labelsize=9)

# Promotion annotation
fig.text(0.5, 0.02, "After 24 hours: latency within 110%, safety above 95% \u2192 PROMOTE canary to production",
         ha='center', fontsize=11, color=GOLD, fontweight='bold')

save(fig, "vdr7_06_canary_deployment.png")

