#!/usr/bin/env python3
"""
HOWL VDR-6 Diagrams — Computational Primitives and Operational Environments
8 figures covering the execution layer for VDR-LLM-Prolog.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Wedge
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


# ================================================================
# FIG 1: IDENTITY CARD — VDR-6 EXECUTION LAYER
# Type: Identity Card (D5.8)
# Shows: Complete execution system at a glance — 262 primitives,
#        20 categories, 4 env types, grants, versioning
# ================================================================
print("Fig 1: Identity card")

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1, 13)

# Title
ax.text(8, 12.2, "VDR-6: The Execution Layer", ha='center',
        fontsize=22, fontweight='bold', color=GOLD)
ax.text(8, 11.4, "Computational Primitives \u2022 Command Tokens \u2022 Operational Environments",
        ha='center', fontsize=12, color=SILVER)

# Left column: primitive summary
ax.text(1.0, 10.2, "Pure Primitives", fontsize=13, fontweight='bold', color=GREEN)
pure_cats = [
    ("String", 17), ("List", 34), ("Arithmetic", 26), ("Set", 14),
    ("Dictionary", 15), ("LinAlg", 16), ("Statistics", 16), ("Conversion", 14),
    ("Date/Time", 10), ("Hash", 8), ("Graph", 13), ("Regex", 7),
    ("Logic", 11), ("KB/Constraint", 15),
]
for i, (name, count) in enumerate(pure_cats):
    y = 9.5 - i * 0.52
    ax.text(1.0, y, name, fontsize=7.5, color=SILVER)
    ax.text(4.2, y, str(count), fontsize=7.5, color=GREEN, fontweight='bold', ha='right')
    bar_w = count / 34.0 * 2.5
    ax.barh(y, bar_w, height=0.32, left=4.4, color=GREEN, alpha=0.3, edgecolor=GREEN, linewidth=0.8)

ax.text(1.0, 2.1, "Total Pure: 218", fontsize=10, fontweight='bold', color=GREEN)

# Middle column: operational + system stats
ax.text(8.0, 10.2, "Operational Primitives", fontsize=13, fontweight='bold', color=RED)
op_cats = [
    ("Filesystem", 15), ("Compilation", 4), ("Execution", 5),
    ("Linting", 8), ("Network", 5), ("Process", 7),
]
for i, (name, count) in enumerate(op_cats):
    y = 9.5 - i * 0.65
    ax.text(8.0, y, name, fontsize=8, color=SILVER)
    ax.text(10.8, y, str(count), fontsize=8, color=RED, fontweight='bold', ha='right')
    bar_w = count / 15.0 * 2.0
    ax.barh(y, bar_w, height=0.4, left=11.0, color=RED, alpha=0.3, edgecolor=RED, linewidth=0.8)

ax.text(8.0, 5.3, "Total Operational: 44", fontsize=10, fontweight='bold', color=RED)

# Key numbers panel
ax.text(8.0, 4.3, "System Totals", fontsize=13, fontweight='bold', color=GOLD)
stats = [
    ("262", "total primitives"),
    ("20", "categories"),
    ("16", "command token types"),
    ("4", "environment types"),
    ("12", "resource address schemes"),
    ("~1515", "planned tests"),
]
for i, (num, label) in enumerate(stats):
    y = 3.6 - i * 0.5
    ax.text(8.0, y, num, fontsize=12, fontweight='bold', color=GOLD)
    ax.text(9.5, y, label, fontsize=9, color=SILVER)

# Right column: architecture reminder
ax.text(14.0, 10.2, "Architecture", fontsize=13, fontweight='bold', color=PURPLE)
layers = [
    ("Conversation", PURPLE, 9.3),
    ("Logic (Prolog)", CYAN, 8.3),
    ("Execution", ORANGE, 7.3),
    ("ML Stack", BLUE, 6.3),
    ("Arithmetic", GREEN, 5.3),
]
for name, color, y in layers:
    rounded_box(ax, 14.8, y, 3.2, 0.7, color, alpha=0.15, lw=1.5, ec=color)
    ax.text(14.8, y, name, ha='center', fontsize=8, fontweight='bold', color=color)

ax.text(14.8, 4.3, "\u2190 VDR-6 specifies\n    this layer", ha='center',
        fontsize=9, color=ORANGE, style='italic')

save(fig, "vdr6_01_identity_card.png")


# ================================================================
# FIG 2: COMPLETE EXECUTION FLOW (GYM_25 EXAMPLE)
# Type: Progression/Sequence (D5.7)
# Shows: End-to-end example from write through upload, execute,
#        poll, store, version — with exact data at every step
# ================================================================
print("Fig 2: Complete execution flow")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18.5)
ax.set_ylim(-0.5, 10)

ax.text(9.0, 9.3, "Complete Execution Flow: Write \u2192 Test \u2192 Store \u2192 Version",
        ha='center', fontsize=15, fontweight='bold', color=GOLD)

steps = [
    ("LLM\nGenerates\nScript", CYAN, 1.2,
     "CMD: TEXT\ngym_25_.py"),
    ("Upload\nto Env", BLUE, 4.0,
     "CMD: ENV_UPLOAD\nenv_vdr_test\n/workspace/gym/"),
    ("Execute\n(async)", ORANGE, 6.8,
     "CMD: ENV_EXEC\npython3 gym_25\n\u2192 task_049"),
    ("Poll /\nComplete", GREEN, 9.6,
     "task_049\ncompleted\n16/16 passed"),
    ("Store\nResult", PURPLE, 12.4,
     "CMD: STORE_RESULT\nkb_vdr_gyms/\ngym_25_result_v1"),
    ("Create\nVersion", GOLD, 15.2,
     "CMD: VERSION_CREATE\nv1, 16/16 passed\n+ update stats"),
]

step_y = 5.5
data_y = 2.8
label_y = 8.0

for i, (name, color, x, data) in enumerate(steps):
    rounded_box(ax, x, step_y, 2.2, 1.8, color, alpha=0.2, lw=2, ec=color)
    ax.text(x, step_y, name, ha='center', va='center',
            fontsize=9, fontweight='bold', color=color)

    ax.text(x, data_y, data, ha='center', va='center',
            fontsize=7, color=WHITE, family='monospace',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

    if i < len(steps) - 1:
        next_x = steps[i + 1][2]
        ax.annotate('', xy=(next_x - 1.2, step_y), xytext=(x + 1.2, step_y),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.8, mutation_scale=15))

# Timeline annotation
ax.text(1.2, label_y, "Turn N", fontsize=8, color=SILVER, ha='center')
ax.text(4.0, label_y, "Turn N", fontsize=8, color=SILVER, ha='center')
ax.text(6.8, label_y, "Turn N", fontsize=8, color=SILVER, ha='center')
ax.text(9.6, label_y, "Turn N+k", fontsize=8, color=ORANGE, ha='center', fontweight='bold')
ax.text(12.4, label_y, "Turn N+k", fontsize=8, color=SILVER, ha='center')
ax.text(15.2, label_y, "Turn N+k", fontsize=8, color=SILVER, ha='center')

# Async gap
ax.plot([7.9, 8.5], [step_y, step_y], color=ORANGE, lw=2, linestyle='--')
ax.text(8.2, step_y + 0.5, "async\ngap", ha='center', fontsize=7, color=ORANGE, style='italic')

ax.text(9.0, 0.8, "Every step is a command token. Every result stored in KB. File available as direct download.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr6_02_execution_flow.png")


# ================================================================
# FIG 3: COMMAND TOKEN OUTPUT STREAM
# Type: Progression/Sequence (D5.7)
# Shows: Text and command tokens interleaving in the LLM output,
#        with execution arrows from commands to primitive layer
# ================================================================
print("Fig 3: Command token stream")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18)
ax.set_ylim(-0.5, 10)

ax.text(8.75, 9.3, "Output Stream: Text Tokens and Command Tokens",
        ha='center', fontsize=15, fontweight='bold', color=GOLD)

# Stream blocks
stream_y = 7.0
blocks = [
    ("TEXT", "\"I'll write the\ntest script...\"", WHITE, 1.5),
    ("CMD", "ENV_UPLOAD\nscript.py", ORANGE, 4.5),
    ("CMD", "ENV_EXEC\npython3 test", ORANGE, 7.5),
    ("TEXT", "\"Tests running.\nTask: 049\"", WHITE, 10.5),
    ("CMD", "STORE_RESULT\nkb/result_v1", PURPLE, 13.5),
    ("ATTACH", "Direct\ndownload", GOLD, 16.5),
]

for btype, content, color, x in blocks:
    if btype == "TEXT":
        ec = DIM
        alpha = 0.12
    elif btype == "ATTACH":
        ec = GOLD
        alpha = 0.2
    else:
        ec = ORANGE
        alpha = 0.2
    rounded_box(ax, x, stream_y, 2.4, 1.6, color, alpha=alpha, lw=2, ec=ec)
    ax.text(x, stream_y + 0.45, btype, ha='center', fontsize=8,
            fontweight='bold', color=color)
    ax.text(x, stream_y - 0.25, content, ha='center', fontsize=7,
            color=SILVER, family='monospace')

# Arrows between blocks
for i in range(len(blocks) - 1):
    x1 = blocks[i][3] + 1.3
    x2 = blocks[i + 1][3] - 1.3
    ax.annotate('', xy=(x2, stream_y), xytext=(x1, stream_y),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2, mutation_scale=12))

# Execution layer below
exec_y = 3.5
ax.plot([0.5, 17.5], [exec_y + 1.2, exec_y + 1.2], color=DIM, lw=1, linestyle='--', alpha=0.5)
ax.text(0.8, exec_y + 1.4, "Execution Layer", fontsize=9, color=DIM)

# Execution targets for CMD blocks
exec_targets = [
    (4.5, "Docker:\nupload file", BLUE),
    (7.5, "Docker:\nrun process", BLUE),
    (13.5, "KB:\nassert fact", CYAN),
]
for x, label, color in exec_targets:
    rounded_box(ax, x, exec_y, 2.2, 1.2, color, alpha=0.15, lw=1.5, ec=color)
    ax.text(x, exec_y, label, ha='center', fontsize=7.5, color=color)
    ax.annotate('', xy=(x, exec_y + 0.7), xytext=(x, stream_y - 0.9),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5, mutation_scale=12))

# User sees
ax.text(1.5, 4.8, "User sees:", fontsize=9, color=WHITE, fontweight='bold')
ax.text(10.5, 4.8, "User sees:", fontsize=9, color=WHITE, fontweight='bold')
ax.text(16.5, 4.8, "User sees:", fontsize=9, color=WHITE, fontweight='bold')
ax.annotate('', xy=(1.5, stream_y - 0.9), xytext=(1.5, 5.1),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1, mutation_scale=10))
ax.annotate('', xy=(10.5, stream_y - 0.9), xytext=(10.5, 5.1),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1, mutation_scale=10))
ax.annotate('', xy=(16.5, stream_y - 0.9), xytext=(16.5, 5.1),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1, mutation_scale=10))

ax.text(4.5, 1.8, "CMD executed silently (or shown if show_commands=true)",
        ha='center', fontsize=8, color=DIM, style='italic')
ax.text(13.5, 1.8, "TEXT + ATTACH rendered to user",
        ha='center', fontsize=8, color=DIM, style='italic')

ax.text(8.75, 0.6, "Two channels: text for humans, commands for machines. Same output stream.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr6_03_command_token_stream.png")


# ================================================================
# FIG 4: UNIFIED ENVIRONMENT INTERFACE
# Type: Geometric Cross-Section (D5.4)
# Shows: Four env types converging on one shared interface surface
# ================================================================
print("Fig 4: Unified environment interface")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 17.5)
ax.set_ylim(-0.5, 10)

ax.text(8.5, 9.3, "Unified Environment Interface",
        ha='center', fontsize=16, fontweight='bold', color=GOLD)
ax.text(8.5, 8.6, "Four backends, one interface. Same command tokens for all.",
        ha='center', fontsize=10, color=SILVER)

# Interface surface (horizontal band in middle)
interface_y = 5.0
ax.fill_between([1, 16], [interface_y - 0.4]*2, [interface_y + 0.4]*2,
                color=GOLD, alpha=0.08)
ax.plot([1, 16], [interface_y + 0.4, interface_y + 0.4], color=GOLD, lw=2, alpha=0.6)
ax.plot([1, 16], [interface_y - 0.4, interface_y - 0.4], color=GOLD, lw=2, alpha=0.6)

# Interface operations listed
ops = ["exec()", "upload()", "download()", "shell()", "file_read()", "file_write()",
       "list_dir()", "proc_start()", "proc_poll()", "proc_output()"]
for i, op in enumerate(ops):
    x = 1.5 + i * 1.45
    ax.text(x, interface_y, op, fontsize=6.5, color=GOLD, ha='center', va='center',
            fontweight='bold', rotation=0)

ax.text(0.5, interface_y, "Interface:", fontsize=8, color=GOLD, fontweight='bold',
        ha='right', va='center')

# Environment types above
envs = [
    ("Docker", BLUE, 2.5, "python:3.8-slim\nubuntu:24.04\nalpine:3.19"),
    ("VM", CYAN, 6.5, "VirtualBox\nQEMU\nCloud VM"),
    ("Local", GREEN, 10.5, "Direct host\nexecution\n(trusted only)"),
    ("SSH Remote", PURPLE, 14.5, "gpu01.lab\nvia pubkey\nport 22"),
]

for name, color, x, details in envs:
    rounded_box(ax, x, 7.3, 3.0, 2.0, color, alpha=0.15, lw=2, ec=color)
    ax.text(x, 7.8, name, ha='center', fontsize=11, fontweight='bold', color=color)
    ax.text(x, 6.8, details, ha='center', fontsize=7, color=SILVER)

    ax.annotate('', xy=(x, interface_y + 0.5), xytext=(x, 6.2),
                arrowprops=dict(arrowstyle='->', color=color, lw=2, mutation_scale=15))

# Command tokens above
ax.text(8.5, 3.5, "Command Tokens", fontsize=12, fontweight='bold',
        color=ORANGE, ha='center')
cmd_examples = [
    "ENV_EXEC(env, cmd, args)",
    "ENV_UPLOAD(env, content, path)",
    "ENV_DOWNLOAD(env, path)",
]
for i, cmd in enumerate(cmd_examples):
    ax.text(8.5, 2.8 - i * 0.55, cmd, ha='center', fontsize=8,
            color=ORANGE, family='monospace')

ax.annotate('', xy=(8.5, interface_y - 0.5), xytext=(8.5, 3.7),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2, mutation_scale=15))

ax.text(8.5, 0.6, "The LLM issues the same commands regardless of backend. Environment selection is a KB configuration.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr6_04_unified_environment.png")


# ================================================================
# FIG 5: PRIMITIVE CATEGORY NESTING RINGS
# Type: Geometric Cross-Section (D5.4)
# Shows: Inner ring pure/operational, middle ring categories,
#        proportional sizing by primitive count
# ================================================================
print("Fig 5: Primitive category rings")

fig, ax = plt.subplots(figsize=(14, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)

ax.text(0, 7.2, "262 Primitives Across 20 Categories",
        ha='center', fontsize=16, fontweight='bold', color=GOLD)

# Inner circle: Pure vs Operational
inner_r = 1.8
pure_angle = 218.0 / 262.0 * 360.0
op_angle = 44.0 / 262.0 * 360.0

wedge_pure = Wedge((0, 0), inner_r, 90, 90 + pure_angle,
                   facecolor=GREEN, alpha=0.4, edgecolor=GREEN, linewidth=2)
wedge_op = Wedge((0, 0), inner_r, 90 + pure_angle, 90 + 360,
                 facecolor=RED, alpha=0.4, edgecolor=RED, linewidth=2)
ax.add_patch(wedge_pure)
ax.add_patch(wedge_op)

ax.text(0, 0.4, "Pure", fontsize=11, fontweight='bold', color=GREEN, ha='center')
ax.text(0, -0.1, "218", fontsize=14, fontweight='bold', color=GREEN, ha='center')
ax.text(0, -0.7, "Op: 44", fontsize=9, color=RED, ha='center')

# Outer ring: categories
outer_r_inner = 2.5
outer_r_outer = 5.5

categories = [
    ("List", 34, GREEN), ("Arithmetic", 26, GREEN), ("String", 17, GREEN),
    ("LinAlg", 16, GREEN), ("Stats", 16, GREEN), ("Dict", 15, GREEN),
    ("KB", 15, GREEN), ("Set", 14, GREEN), ("Convert", 14, GREEN),
    ("Graph", 13, GREEN), ("Logic", 11, GREEN), ("Date", 10, GREEN),
    ("Hash", 8, GREEN), ("Regex", 7, GREEN),
    ("Filesystem", 15, RED), ("Lint", 8, RED), ("Process", 7, RED),
    ("Execute", 5, RED), ("Network", 5, RED), ("Compile", 4, RED),
]

total = sum(c[1] for c in categories)
start_angle = 90
for name, count, color in categories:
    sweep = count / float(total) * 360.0
    mid_angle = start_angle + sweep / 2.0
    mid_rad = np.radians(mid_angle)

    wedge = Wedge((0, 0), outer_r_outer, start_angle, start_angle + sweep,
                  width=outer_r_outer - outer_r_inner,
                  facecolor=color, alpha=0.2, edgecolor=color, linewidth=1)
    ax.add_patch(wedge)

    label_r = (outer_r_inner + outer_r_outer) / 2.0 + 0.15
    lx = label_r * np.cos(mid_rad)
    ly = label_r * np.sin(mid_rad)

    rotation = mid_angle - 90
    if mid_angle > 180 and mid_angle < 360:
        rotation = mid_angle + 90

    ax.text(lx, ly, "%s\n%d" % (name, count), ha='center', va='center',
            fontsize=6.5, color=WHITE, fontweight='bold', rotation=0)

    start_angle += sweep

# Legend
ax.text(-6.5, -6.5, "\u25cf Pure (no grant required)", fontsize=10, color=GREEN)
ax.text(-6.5, -7.0, "\u25cf Operational (positive grant)", fontsize=10, color=RED)
ax.text(3.0, -6.5, "Total: 262 primitives", fontsize=10, color=GOLD, fontweight='bold')
ax.text(3.0, -7.0, "20 categories", fontsize=10, color=SILVER)

save(fig, "vdr6_05_primitive_rings.png")


# ================================================================
# FIG 6: DIRECT DOWNLOAD VS LLM REGENERATION
# Type: Comparison (side-by-side) (D5.6)
# Shows: Two paths — direct KB-to-user vs KB-to-LLM-to-user
# ================================================================
print("Fig 6: Direct download vs LLM regen")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)

for ax in [ax1, ax2]:
    ax.set_facecolor(PAN)
    ax.axis('off')
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 10)

# Left panel: Direct download
ax1.text(5, 9.2, "Direct Download", fontsize=15, fontweight='bold', color=GREEN)
ax1.text(5, 8.5, "KB data served to user without LLM", fontsize=9, color=SILVER)

rounded_box(ax1, 5, 6.5, 4, 1.2, CYAN, alpha=0.2, lw=2, ec=CYAN)
ax1.text(5, 6.5, "KB: exact data\nfraction(31, 140)", ha='center',
         fontsize=9, color=CYAN)

ax1.annotate('', xy=(5, 3.3), xytext=(5, 5.8),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=3, mutation_scale=20))
ax1.text(6.5, 4.5, "ONE step\nExact\nNo tokens", fontsize=9, color=GREEN,
         fontweight='bold')

rounded_box(ax1, 5, 2.5, 4, 1.2, GOLD, alpha=0.2, lw=2, ec=GOLD)
ax1.text(5, 2.5, "User receives:\n31/140 exactly", ha='center',
         fontsize=9, color=GOLD)

ax1.text(5, 0.8, "\u2713 Cannot hallucinate", fontsize=10, color=GREEN)
ax1.text(5, 0.2, "\u2713 No token limit", fontsize=10, color=GREEN)

# Right panel: LLM regeneration
ax2.text(5, 9.2, "LLM Regeneration", fontsize=15, fontweight='bold', color=RED)
ax2.text(5, 8.5, "LLM reads data, generates tokens to reproduce it", fontsize=9, color=SILVER)

rounded_box(ax2, 5, 7.2, 4, 1.0, CYAN, alpha=0.2, lw=2, ec=CYAN)
ax2.text(5, 7.2, "KB: exact data", ha='center', fontsize=9, color=CYAN)

ax2.annotate('', xy=(5, 5.8), xytext=(5, 6.6),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, mutation_scale=12))

rounded_box(ax2, 5, 5.2, 4, 1.0, MAG, alpha=0.2, lw=2, ec=MAG)
ax2.text(5, 5.2, "LLM tokenizes\nand regenerates", ha='center', fontsize=9, color=MAG)

ax2.annotate('', xy=(5, 3.8), xytext=(5, 4.6),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, mutation_scale=12))

rounded_box(ax2, 5, 3.2, 4, 1.0, RED, alpha=0.15, lw=2, ec=RED)
ax2.text(5, 3.2, "User receives:\n\"about 0.221...\"", ha='center',
         fontsize=9, color=RED)

ax2.text(5, 1.6, "\u2717 Can hallucinate values", fontsize=10, color=RED)
ax2.text(5, 1.0, "\u2717 Truncated by token limit", fontsize=10, color=RED)
ax2.text(5, 0.4, "\u2717 Three steps, lossy", fontsize=10, color=RED)

save(fig, "vdr6_06_direct_vs_regen.png")


# ================================================================
# FIG 7: OPERATIONAL PRIMITIVE WITH GRANT GATE
# Type: Progression/Sequence (D5.7)
# Shows: Command enters grant verification, authorized commands
#        proceed, blocked commands rejected — with details at each stage
# ================================================================
print("Fig 7: Grant-gated execution")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18)
ax.set_ylim(-0.5, 10)

ax.text(8.75, 9.3, "Positive Grant Gating: Every Operational Primitive Authorized",
        ha='center', fontsize=15, fontweight='bold', color=GOLD)

# LLM issues command
rounded_box(ax, 1.5, 5.5, 2.4, 2.0, CYAN, alpha=0.2, lw=2, ec=CYAN)
ax.text(1.5, 6.1, "LLM Issues", fontsize=9, fontweight='bold', color=CYAN)
ax.text(1.5, 5.3, "CMD: OP_FN\nexec_pytest\nenv_vdr_test", fontsize=7,
        color=SILVER, ha='center', family='monospace')

# Arrow to gate
ax.annotate('', xy=(4.0, 5.5), xytext=(2.8, 5.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2, mutation_scale=15))

# Grant verification gate
gate_x = 5.8
rounded_box(ax, gate_x, 5.5, 2.8, 3.2, ORANGE, alpha=0.15, lw=2.5, ec=ORANGE)
ax.text(gate_x, 6.8, "GRANT GATE", fontsize=10, fontweight='bold', color=ORANGE)
checks = ["grant_valid?", "grant_covers?", "constraints_ok?", "uses_remaining?"]
for i, check in enumerate(checks):
    ax.text(gate_x, 6.1 - i * 0.5, "\u2022 " + check, fontsize=7.5,
            color=WHITE, ha='center')

# Authorized path (top)
ax.annotate('', xy=(9.0, 6.8), xytext=(7.3, 6.8),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5, mutation_scale=15))
ax.text(8.15, 7.3, "AUTHORIZED", fontsize=8, fontweight='bold', color=GREEN)

# Environment execution
rounded_box(ax, 10.5, 6.8, 2.4, 1.4, BLUE, alpha=0.2, lw=2, ec=BLUE)
ax.text(10.5, 7.1, "Environment", fontsize=9, fontweight='bold', color=BLUE)
ax.text(10.5, 6.5, "exec_pytest\nin Docker", fontsize=7, color=SILVER, ha='center')

# Result to KB
ax.annotate('', xy=(13.2, 6.8), xytext=(11.8, 6.8),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, mutation_scale=12))

rounded_box(ax, 14.5, 6.8, 2.4, 1.4, PURPLE, alpha=0.2, lw=2, ec=PURPLE)
ax.text(14.5, 7.1, "KB: Store", fontsize=9, fontweight='bold', color=PURPLE)
ax.text(14.5, 6.5, "result + log\n+ grant used", fontsize=7, color=SILVER, ha='center')

# Result to user
ax.annotate('', xy=(16.8, 6.8), xytext=(15.8, 6.8),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, mutation_scale=12))
ax.text(17.2, 6.8, "\u2192 User", fontsize=9, color=GOLD, fontweight='bold')

# Blocked path (bottom)
ax.annotate('', xy=(9.0, 4.2), xytext=(7.3, 4.2),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5, mutation_scale=15))
ax.text(8.15, 3.6, "BLOCKED", fontsize=8, fontweight='bold', color=RED)

rounded_box(ax, 10.5, 4.2, 2.4, 1.4, RED, alpha=0.15, lw=2, ec=RED)
ax.text(10.5, 4.5, "Rejected", fontsize=9, fontweight='bold', color=RED)
ax.text(10.5, 3.9, "no valid grant\nfor this op", fontsize=7, color=SILVER, ha='center')

# Log rejection
ax.annotate('', xy=(13.2, 4.2), xytext=(11.8, 4.2),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5, mutation_scale=12))

rounded_box(ax, 14.5, 4.2, 2.4, 1.4, DIM, alpha=0.15, lw=1.5, ec=DIM)
ax.text(14.5, 4.5, "KB: Log", fontsize=9, fontweight='bold', color=DIM)
ax.text(14.5, 3.9, "blocked op\nreason + time", fontsize=7, color=SILVER, ha='center')

# Grant details
ax.text(1.0, 1.8, "Grant example:", fontsize=9, color=ORANGE, fontweight='bold')
grant_text = ('name="alice_exec", class=execute, ops=[exec_python, exec_pytest],\n'
              'location="/workspace/", expires=2026-05-17T10:00, uses=1000')
ax.text(1.0, 1.1, grant_text, fontsize=7, color=SILVER, family='monospace')

ax.text(8.75, 0.3, "Default is denial. Every operational primitive requires an explicit positive grant.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr6_07_grant_gated_execution.png")


# ================================================================
# FIG 8: VERSION HISTORY CHAIN WITH DIFFS
# Type: Progression/Sequence (D5.7)
# Shows: v1 → v2 → v3 chain with diffs, tags, and test results
# ================================================================
print("Fig 8: Version history chain")

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 17.5)
ax.set_ylim(-0.5, 10)

ax.text(8.5, 9.3, "Version History: gym_16_graph_theory.py",
        ha='center', fontsize=15, fontweight='bold', color=GOLD)

versions = [
    ("v1", "initial", "19/20 passed", "maxflow BFS\nhas a bug", None, RED, 2.5),
    ("v2", "maxflow_fixed", "20/20 passed", "fixed BFS loop\ntermination", "release", GREEN, 8.5),
    ("v3", "perf_update", "20/20 passed", "optimized\nDijkstra", None, BLUE, 14.5),
]

ver_y = 5.5
tag_y = 8.0
test_y = 2.5
diff_y = 3.8

for i, (vname, label, test, notes, tag, color, x) in enumerate(versions):
    # Main version box
    rounded_box(ax, x, ver_y, 3.5, 2.2, color, alpha=0.15, lw=2, ec=color)
    ax.text(x, ver_y + 0.6, vname, fontsize=14, fontweight='bold', color=color, ha='center')
    ax.text(x, ver_y - 0.05, label, fontsize=8, color=WHITE, ha='center')
    ax.text(x, ver_y - 0.55, notes, fontsize=7, color=SILVER, ha='center')

    # Test result below
    test_color = GREEN if "20/20" in test else RED
    ax.text(x, test_y, test, fontsize=10, fontweight='bold', color=test_color,
            ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=test_color, alpha=0.6))

    # Tag above (if present)
    if tag is not None:
        rounded_box(ax, x, tag_y, 1.8, 0.7, GOLD, alpha=0.25, lw=1.5, ec=GOLD)
        ax.text(x, tag_y, "tag: %s" % tag, fontsize=8, fontweight='bold',
                color=GOLD, ha='center')
        ax.plot([x, x], [tag_y - 0.4, ver_y + 1.2], color=GOLD, lw=1, linestyle='--', alpha=0.5)

    # Arrow to next version
    if i < len(versions) - 1:
        next_x = versions[i + 1][6]
        mid_x = (x + next_x) / 2.0
        ax.annotate('', xy=(next_x - 1.9, ver_y), xytext=(x + 1.9, ver_y),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=2, mutation_scale=15))

        # Diff annotation
        diff_text = "DIFF" if i == 0 else "DIFF"
        diff_details = "+12 lines\n-3 lines\nBFS fix" if i == 0 else "+5 lines\n-1 line\noptimize"
        ax.text(mid_x, ver_y + 0.5, diff_text, fontsize=8, fontweight='bold',
                color=ORANGE, ha='center')
        ax.text(mid_x, ver_y - 0.4, diff_details, fontsize=6.5, color=ORANGE,
                ha='center', family='monospace')

# Timeline
ax.text(2.5, 1.5, "turn 52", fontsize=8, color=DIM, ha='center')
ax.text(8.5, 1.5, "turn 58", fontsize=8, color=DIM, ha='center')
ax.text(14.5, 1.5, "turn 72", fontsize=8, color=DIM, ha='center')

ax.text(8.5, 0.5, "Every version stored as KB fact. Diffs computed by pure primitive. Tags queryable.",
        ha='center', fontsize=10, color=SILVER)

save(fig, "vdr6_08_version_history.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n--- All 8 figures saved ---")
print("  vdr6_01_identity_card.png")
print("  vdr6_02_execution_flow.png")
print("  vdr6_03_command_token_stream.png")
print("  vdr6_04_unified_environment.png")
print("  vdr6_05_primitive_rings.png")
print("  vdr6_06_direct_vs_regen.png")
print("  vdr6_07_grant_gated_execution.png")
print("  vdr6_08_version_history.png")
