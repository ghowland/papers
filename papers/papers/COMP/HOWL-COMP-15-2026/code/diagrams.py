
#!/usr/bin/env python3
"""
HOWL COMP-12 Diagrams — Closed Loop Architecture: A Complete OS in Four Flat Lists
8 figures covering execution cycles, orchestration maps, UAI curves, envelopes,
behavior landscapes, flow heatmaps, cardinality geometry, and boot timelines.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import numpy as np
import os

# Output directory
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Global style ──

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

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=10)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=10)


# ================================================================
# FIG 1: CLOSED LOOP EXECUTION CYCLE
# Type: 4 (Geometric Cross-Section)
# Shows: The circular closed-loop path — data feeds evaluation feeds
#        decisions feeds actions feeds data. Two entry points (Path A
#        per-entity, Path B system-level) enter the same ring.
#        Circularity communicates closure that a list cannot.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.4, 2.4)
ax.set_aspect('equal')

ax.text(0, 2.2, 'Closed Loop Execution Cycle', color=GOLD, fontsize=17,
        fontweight='bold', ha='center', va='center')

# Ring nodes: 6 stages around the loop
stages = [
    ('Entity\nData', CYAN),
    ('Prolog\nEvaluation', BLUE),
    ('SM Transition /\nEvent Constraint', GREEN),
    ('UAI Scoring /\nEvent Flow', ORANGE),
    ('Action /\nEvent Fire', MAG),
    ('Envelope /\nDirect Modify', PURPLE),
]
n = len(stages)
radius = 1.4
angles = [90 - i * 360.0 / n for i in range(n)]
node_positions = []
for i, ang_deg in enumerate(angles):
    ang = np.radians(ang_deg)
    x = radius * np.cos(ang)
    y = radius * np.sin(ang)
    node_positions.append((x, y))

# Draw curved arrows between nodes (arc segments)
for i in range(n):
    a1 = np.radians(angles[i] - 12)
    a2 = np.radians(angles[(i + 1) % n] + 12)
    # Draw arc as series of points
    t_vals = np.linspace(a1, a2, 40)
    xs = radius * np.cos(t_vals)
    ys = radius * np.sin(t_vals)
    ax.plot(xs, ys, color=DIM, linewidth=1.5, alpha=0.6)
    # Arrowhead at end
    ax.annotate('', xy=(xs[-1], ys[-1]),
                xytext=(xs[-3], ys[-3]),
                arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.8))

# Draw nodes
box_w = 0.52
box_h = 0.36
for i, (label, col) in enumerate(stages):
    x, y = node_positions[i]
    box = FancyBboxPatch((x - box_w, y - box_h), box_w * 2, box_h * 2,
                          boxstyle='round,pad=0.12', facecolor=BG,
                          edgecolor=col, linewidth=2.0)
    ax.add_patch(box)
    ax.text(x, y, label, color=col, fontsize=10, fontweight='bold',
            ha='center', va='center')

# Path A label - per-entity update
ax.annotate('Path A\nPer-Entity\nUpdate', xy=(node_positions[1][0] - 0.3, node_positions[1][1] + 0.3),
            xytext=(-2.0, 1.6), color=CYAN, fontsize=10, fontweight='bold',
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5, connectionstyle='arc3,rad=0.2'),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, linewidth=1.2))

# Path B label - system orchestration
ax.annotate('Path B\nSystem\nOrchestration', xy=(node_positions[2][0] - 0.3, node_positions[2][1] - 0.3),
            xytext=(-2.0, -0.8), color=ORANGE, fontsize=10, fontweight='bold',
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5, connectionstyle='arc3,rad=-0.2'),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, linewidth=1.2))

# Center label
ax.text(0, 0, 'CLOSED\nLOOP', color=GOLD, fontsize=14, fontweight='bold',
        ha='center', va='center', alpha=0.5)

# Envelope feedback note
ax.text(0, -2.15, 'Envelopes fire events on start / update / end,\nfeeding back into evaluation',
        color=SILVER, fontsize=9, ha='center', va='center', style='italic')

save(fig, 'comp12_01_closed_loop_cycle.png')


# ================================================================
# FIG 2: SINGLETON-POPULATION ORCHESTRATION MAP
# Type: 4 (Geometric Cross-Section)
# Shows: 15 One-cardinality singletons as inner ring, 20 Infinity-
#        cardinality populations as outer ring, with arrows showing
#        fan-out (One→Inf) and convergence (Inf→One). The hub-spoke
#        geometry IS the architecture.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 18), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.8, 3.8)
ax.set_aspect('equal')

ax.text(0, 3.5, 'Singleton-Population Orchestration Map', color=GOLD, fontsize=17,
        fontweight='bold', ha='center', va='center')

singletons = [
    'Kernel', 'Init\nSystem', 'Memory\nMgr', 'Scheduler', 'VFS',
    'Network\nStack', 'Display\nServer', 'Audio\nMixer', 'Device\nMgr',
    'Swap\nMgr', 'Firewall', 'DNS\nResolver', 'Session\nMgr',
    'System\nLogger', 'Package\nMgr'
]

populations = [
    'Process', 'Thread', 'File', 'FS Mount', 'Net Conn',
    'User Acct', 'User Sess', 'Device', 'Kernel Mod', 'Service',
    'Window', 'Net Iface', 'Perm Rule', 'Timer', 'Signal',
    'Pipe', 'Shared Mem', 'Env Vars', 'Cron Job', 'Log Entry'
]

# Key flows: (singleton_index, population_index) for fan-out arrows
key_flows = [
    (1, 9),   # Init → Service
    (1, 11),  # Init → Net Iface
    (3, 0),   # Scheduler → Process
    (4, 2),   # VFS → File
    (4, 3),   # VFS → FS Mount
    (5, 4),   # Network Stack → Net Conn
    (6, 10),  # Display Server → Window
    (8, 7),   # Device Mgr → Device
    (12, 6),  # Session Mgr → User Sess
    (13, 19), # System Logger → Log Entry
    (2, 0),   # Memory Mgr → Process (OOM kill)
    (9, 7),   # Swap Mgr → Device (swap device)
]

r_inner = 1.5
r_outer = 2.8

# Draw inner ring nodes (singletons)
s_positions = []
for i, name in enumerate(singletons):
    ang = np.radians(90 - i * 360.0 / len(singletons))
    x = r_inner * np.cos(ang)
    y = r_inner * np.sin(ang)
    s_positions.append((x, y))
    circle = plt.Circle((x, y), 0.28, facecolor=BG, edgecolor=CYAN,
                         linewidth=1.5, zorder=3)
    ax.add_patch(circle)
    ax.text(x, y, name, color=CYAN, fontsize=6.5, fontweight='bold',
            ha='center', va='center', zorder=4)

# Draw outer ring nodes (populations)
p_positions = []
for i, name in enumerate(populations):
    ang = np.radians(90 - i * 360.0 / len(populations))
    x = r_outer * np.cos(ang)
    y = r_outer * np.sin(ang)
    p_positions.append((x, y))
    box = FancyBboxPatch((x - 0.32, y - 0.18), 0.64, 0.36,
                          boxstyle='round,pad=0.06', facecolor=BG,
                          edgecolor=MAG, linewidth=1.2, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, name, color=MAG, fontsize=6.5, ha='center', va='center', zorder=4)

# Draw flow arrows
for si, pi in key_flows:
    sx, sy = s_positions[si]
    px, py = p_positions[pi]
    dx = px - sx
    dy = py - sy
    dist = np.sqrt(dx * dx + dy * dy)
    # Shorten arrow to not overlap nodes
    ux, uy = dx / dist, dy / dist
    x1 = sx + ux * 0.32
    y1 = sy + uy * 0.32
    x2 = px - ux * 0.36
    y2 = py - uy * 0.36
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=0.8, alpha=0.5))

# Ring labels
ax.text(0, 0, 'ONE\n(15 singletons)', color=CYAN, fontsize=11, fontweight='bold',
        ha='center', va='center', alpha=0.5)

ax.text(0, -3.45, 'INFINITY  (20 populations)', color=MAG, fontsize=11,
        fontweight='bold', ha='center', va='center', alpha=0.5)

# Legend
ax.text(-3.2, -3.45, 'Arrows: fan-out flows\n(One triggers many)', color=SILVER,
        fontsize=8, ha='left', va='center')

save(fig, 'comp12_02_orchestration_map.png')


# ================================================================
# FIG 3: UAI CONSIDERATION CURVES — MEMORY PRESSURE
# Type: 1 (Running/Convergence Chart)
# Shows: Four curve shapes (inverse linear, quadratic, exponential,
#        linear) on same axes, input 0→1, score 0→1. The SHAPE of
#        each curve is the insight — exponential barely responds then
#        explodes, inverse linear fires immediately.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='UAI Consideration Curves — Memory Pressure Response',
         xlabel='Input Value (normalized 0-1)',
         ylabel='Score (0-1)')

x = np.linspace(0.001, 1.0, 200)

# Curves
inv_linear = 1.0 - x
quadratic = x ** 2
exponential = (np.exp(3.0 * x) - 1.0) / (np.exp(3.0) - 1.0)
linear = x

curves = [
    (inv_linear, 'FreePageRatio (Inverse Linear)', CYAN, '-', 1.0),
    (quadratic, 'SwapUsageRatio (Quadratic)', ORANGE, '-', 0.8),
    (exponential, 'AllocationFailureRate (Exponential)', RED, '-', 1.2),
    (linear, 'PageFaultRate (Linear)', GREEN, '--', 0.6),
]

for yvals, label, col, ls, weight in curves:
    ax.plot(x, yvals, color=col, linewidth=2.5, linestyle=ls,
            label='%s  [w=%.1f]' % (label, weight))

# Threshold regions
ax.axhspan(0.0, 0.2, alpha=0.06, color=GREEN)
ax.text(0.02, 0.10, 'Low urgency', color=GREEN, fontsize=8, alpha=0.7, va='center')

ax.axhspan(0.8, 1.0, alpha=0.06, color=RED)
ax.text(0.02, 0.90, 'Critical urgency', color=RED, fontsize=8, alpha=0.7, va='center')

# Annotations for curve character
ax.annotate('Fires immediately\nas pressure begins', xy=(0.15, 0.85),
            xytext=(0.30, 0.72), color=CYAN, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.2))

ax.annotate('Barely responds\nthen explodes', xy=(0.75, 0.55),
            xytext=(0.55, 0.40), color=RED, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))

ax.annotate('Slow start,\naccelerates', xy=(0.6, 0.36),
            xytext=(0.75, 0.20), color=ORANGE, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.2))

ax.set_xlim(-0.05, 1.08)
ax.set_ylim(-0.08, 1.12)

legend = ax.legend(loc='center left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9, framealpha=0.9,
                   bbox_to_anchor=(0.01, 0.50))
legend.get_frame().set_linewidth(0.5)

ax.text(0.55, 1.05, 'Score multiplied across all considerations — any zero kills the behavior',
        color=SILVER, fontsize=8, ha='center', style='italic')

save(fig, 'comp12_03_uai_curves.png')


# ================================================================
# FIG 4: ENVELOPE ADSR WAVEFORM WITH EVENT HOOKS
# Type: 1 (Running/Convergence) + 5 (Connection Map)
# Shows: A DSP-style ADSR envelope over time, with three event hooks
#        (on-start, on-update, on-end) shown as arrows feeding back
#        into the system. The waveform shape and feedback arrows are
#        both geometric insights.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Envelope: ADSR Waveform with Event Hooks',
         xlabel='Time', ylabel='Modifier Value')

# Build ADSR envelope
# Attack: 0 to 1 over t=0..1
# Sustain: hold at 0.8 over t=1..4
# Decay: 1 to 0.8 over t=1..1.5 (overlaps with sustain start)
# Release: 0.8 to 0 over t=4..5.5

t_attack = np.linspace(0, 1.0, 50)
v_attack = t_attack  # linear ramp up

t_decay = np.linspace(1.0, 1.8, 30)
v_decay = 1.0 - 0.25 * ((t_decay - 1.0) / 0.8)  # 1.0 down to 0.75

t_sustain = np.linspace(1.8, 4.0, 80)
v_sustain = np.full_like(t_sustain, 0.75)

t_release = np.linspace(4.0, 5.5, 50)
v_release = 0.75 * (1.0 - ((t_release - 4.0) / 1.5) ** 1.5)

t_all = np.concatenate([t_attack, t_decay, t_sustain, t_release])
v_all = np.concatenate([v_attack, v_decay, v_sustain, v_release])

# Fill under curve
ax.fill_between(t_all, 0, v_all, alpha=0.08, color=PURPLE)
ax.plot(t_all, v_all, color=PURPLE, linewidth=2.5)

# Phase labels
phases = [
    (0.5, 'A', 'Attack'),
    (1.4, 'D', 'Decay'),
    (2.9, 'S', 'Sustain'),
    (4.75, 'R', 'Release'),
]
for tx, short, full in phases:
    idx = np.argmin(np.abs(t_all - tx))
    vy = v_all[idx]
    ax.text(tx, vy + 0.12, short, color=PURPLE, fontsize=14, fontweight='bold',
            ha='center', va='bottom')
    ax.text(tx, -0.12, full, color=SILVER, fontsize=8, ha='center', va='top')

# Phase boundary lines
for bt in [1.0, 1.8, 4.0]:
    ax.axvline(bt, color=DIM, linewidth=0.8, linestyle=':', alpha=0.5)

# Event hooks
event_hooks = [
    (0.0, 'on-start\nevent', GREEN, 0.0),
    (2.9, 'on-update\nevent (every frame)', CYAN, 0.75),
    (5.5, 'on-end\nevent', RED, 0.0),
]

for tx, label, col, vy in event_hooks:
    # Arrow pointing upward from event
    ax.plot(tx, vy, 'o', color=col, markersize=10, zorder=5)
    ax.annotate(label, xy=(tx, vy),
                xytext=(tx, vy + 0.35), color=col, fontsize=9, fontweight='bold',
                ha='center', va='bottom',
                arrowprops=dict(arrowstyle='->', color=col, lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=col, linewidth=1.0))

# Feedback arrow from events back to "system"
ax.annotate('Events feed back\ninto constraint evaluation',
            xy=(5.2, 0.55), xytext=(4.2, 0.95),
            color=GOLD, fontsize=9, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, connectionstyle='arc3,rad=0.3'),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1.0))

# Curve type annotation
ax.text(3.5, 0.55, 'Curve interpolation\n0-1 over duration', color=SILVER,
        fontsize=8, ha='center', style='italic')

# Modifier type note
ax.text(0.2, 0.90, 'Additive / Multiplicative / Override / Max',
        color=DIM, fontsize=8, ha='left')

ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-0.25, 1.25)

save(fig, 'comp12_04_envelope_adsr.png')


# ================================================================
# FIG 5: BEHAVIOR SET DECISION LANDSCAPE
# Type: 3 (Threshold/Region Chart)
# Shows: Nine behavior sets, each as a pressure-response curve.
#        X-axis is input pressure (0→1), Y-axis is response severity
#        (0=DoNothing, 1=maximum response). Different curve shapes
#        show whether the OS responds gradually or sharply. Threshold
#        regions separate "passive" from "active" from "emergency".
# ================================================================

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
style_ax(ax, title='Behavior Set Decision Landscape — Nine OS Decision Points',
         xlabel='Input Pressure (normalized)',
         ylabel='Response Severity')

x = np.linspace(0.0, 1.0, 200)

behavior_sets = [
    ('Memory Pressure', CYAN, lambda t: np.clip(1.5 * t ** 1.3, 0, 1)),
    ('Scheduling', BLUE, lambda t: np.clip(t, 0, 1)),
    ('Congestion', RED, lambda t: np.clip((np.exp(2.5 * t) - 1) / (np.exp(2.5) - 1), 0, 1)),
    ('Swap Pressure', PURPLE, lambda t: np.clip(1.2 * t ** 1.5, 0, 1)),
    ('Log Pressure', GREEN, lambda t: np.clip(t ** 0.7, 0, 1)),
    ('Connection Health', ORANGE, lambda t: np.clip((np.exp(2.0 * t) - 1) / (np.exp(2.0) - 1), 0, 1)),
    ('Session Idle', GOLD, lambda t: np.where(t < 0.3, 0, np.clip((t - 0.3) / 0.7, 0, 1))),
    ('Service Health', MAG, lambda t: np.where(t < 0.2, 0, np.clip(1.3 * ((t - 0.2) / 0.8) ** 1.2, 0, 1))),
    ('Device Recovery', SILVER, lambda t: np.where(t < 0.15, 0, np.clip(((t - 0.15) / 0.85) ** 0.8, 0, 1))),
]

for name, col, func in behavior_sets:
    y = func(x)
    ax.plot(x, y, color=col, linewidth=2.0, label=name)

# Threshold regions
ax.axhspan(0.0, 0.2, alpha=0.04, color=GREEN)
ax.axhspan(0.2, 0.6, alpha=0.04, color=ORANGE)
ax.axhspan(0.6, 1.0, alpha=0.04, color=RED)

# Region labels on right edge
ax.text(1.03, 0.10, 'Passive', color=GREEN, fontsize=9, va='center', fontweight='bold')
ax.text(1.03, 0.40, 'Active', color=ORANGE, fontsize=9, va='center', fontweight='bold')
ax.text(1.03, 0.80, 'Emergency', color=RED, fontsize=9, va='center', fontweight='bold')

# Threshold lines
ax.axhline(0.2, color=DIM, linewidth=1.0, linestyle='--', alpha=0.4)
ax.axhline(0.6, color=DIM, linewidth=1.0, linestyle='--', alpha=0.4)

ax.set_xlim(-0.05, 1.18)
ax.set_ylim(-0.08, 1.12)

legend = ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=8, framealpha=0.9, ncol=2,
                   bbox_to_anchor=(0.01, 0.98))
legend.get_frame().set_linewidth(0.5)

# Annotation
ax.text(0.50, -0.04, '9 decision points in the entire OS — everything else is deterministic force_action',
        color=SILVER, fontsize=8, ha='center', style='italic')

save(fig, 'comp12_05_behavior_landscape.png')


# ================================================================
# FIG 6: INTER-GROUP FLOW HEATMAP
# Type: 3 (Threshold/Region Chart)
# Shows: 37×37 matrix where cell (i,j) = number of flows from
#        group i to group j. Most cells zero. Clusters visible
#        around Init, Process, DeviceManager. The sparsity pattern
#        and clustering show where coupling actually lives.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 16), facecolor=BG)

group_names = [
    'BIOS', 'Bootldr', 'Kernel', 'Init', 'MemMgr', 'Sched', 'VFS',
    'NetStk', 'DispSrv', 'AudioMx', 'DevMgr', 'SwapMgr', 'Firewall',
    'DNS', 'SessMgr', 'SysLog', 'PkgMgr', 'Process', 'Thread', 'File',
    'FSMount', 'NetConn', 'UserAcc', 'UserSes', 'Device', 'KernMod',
    'Service', 'Window', 'NetIface', 'PermRule', 'Timer', 'Signal',
    'Pipe', 'ShrMem', 'EnvVars', 'CronJob', 'LogEntry'
]

n_groups = 37
flow_matrix = np.zeros((n_groups, n_groups))

# Intra-group flows (diagonal) — approximate counts from the spec
intra_counts = {
    0: 4, 1: 6, 2: 12, 3: 14, 4: 8, 5: 7, 6: 5, 7: 6,
    8: 7, 9: 6, 10: 6, 11: 5, 12: 5, 13: 5, 14: 7, 15: 5,
    16: 5, 17: 17, 18: 11, 19: 8, 20: 7, 21: 11, 22: 6,
    23: 13, 24: 13, 25: 5, 26: 16, 27: 10, 28: 8, 29: 3,
    30: 3, 31: 3, 32: 4, 33: 3, 34: 3, 35: 5, 36: 4
}
for g, c in intra_counts.items():
    flow_matrix[g][g] = c

# Inter-group flows from the spec
inter_flows = [
    (0, 1, 1),    # BIOS → Bootloader
    (1, 2, 1),    # Bootloader → Kernel
    (2, 3, 1),    # Kernel → Init
    (2, 4, 1),    # Kernel → MemMgr
    (4, 5, 1),    # MemMgr → Scheduler
    (2, 6, 1),    # Kernel → VFS
    (3, 7, 1),    # Init → NetStack
    (3, 8, 1),    # Init → DispSrv
    (3, 9, 1),    # Init → AudioMx
    (3, 15, 1),   # Init → SysLog
    (3, 12, 1),   # Init → Firewall
    (3, 13, 1),   # Init → DNS
    (8, 14, 1),   # DispSrv → SessMgr
    (3, 11, 1),   # Init → SwapMgr
    (3, 10, 1),   # Init → DevMgr
    (10, 24, 2),  # DevMgr → Device
    (3, 26, 2),   # Init → Service
    (3, 28, 1),   # Init → NetIface
    (3, 20, 2),   # Init → FSMount
    (5, 17, 1),   # Scheduler → Process
    (14, 23, 1),  # SessMgr → UserSess
    (8, 27, 1),   # DispSrv → Window
    (15, 36, 1),  # SysLog → LogEntry
    (7, 21, 1),   # NetStack → NetConn
    (12, 29, 1),  # Firewall → PermRule
    (26, 15, 1),  # Service → SysLog (convergence)
    (24, 2, 1),   # Device → Kernel (convergence)
    (24, 10, 1),  # Device → DevMgr (convergence)
    (20, 3, 1),   # FSMount → Init (convergence)
    (28, 3, 1),   # NetIface → Init (convergence)
    (26, 3, 1),   # Service → Init (escalation)
    (17, 5, 1),   # Process → Scheduler (convergence)
    (21, 7, 1),   # NetConn → NetStack (convergence)
    (27, 8, 1),   # Window → DispSrv (convergence)
    (36, 15, 1),  # LogEntry → SysLog (convergence)
    (24, 26, 1),  # Device → Service
    (26, 26, 2),  # Service → Service (dependency)
    (17, 18, 1),  # Process → Thread
    (17, 34, 1),  # Process → EnvVars
    (17, 19, 1),  # Process → File
    (17, 32, 1),  # Process → Pipe
    (17, 33, 1),  # Process → ShrMem
    (17, 31, 1),  # Process → Signal
    (17, 17, 2),  # Process → Process (fork)
    (17, 30, 1),  # Process → Timer
    (30, 35, 1),  # Timer → CronJob
    (35, 17, 1),  # CronJob → Process
    (23, 17, 1),  # UserSess → Process
    (23, 34, 1),  # UserSess → EnvVars
    (17, 31, 1),  # Process exit → Signal (to children)
    (32, 17, 1),  # Pipe broken → Process (signal)
]

for src, dst, count in inter_flows:
    flow_matrix[src][dst] += count

# Plot heatmap
# Use log scale for better visibility
display_matrix = np.where(flow_matrix > 0, np.log2(flow_matrix + 1), 0)

from matplotlib.colors import LinearSegmentedColormap
colors_list = [BG, '#1a1a3a', BLUE, CYAN, GOLD]
cmap = LinearSegmentedColormap.from_list('flows', colors_list, N=256)

im = ax.imshow(display_matrix, cmap=cmap, aspect='equal', interpolation='nearest')

ax.set_xticks(range(n_groups))
ax.set_yticks(range(n_groups))
ax.set_xticklabels(group_names, rotation=90, fontsize=6.5, color=SILVER)
ax.set_yticklabels(group_names, fontsize=6.5, color=SILVER)

ax.set_title('Inter-Group Flow Heatmap — Where Coupling Lives', color=GOLD,
             fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel('Target Group', color=SILVER, fontsize=11, labelpad=10)
ax.set_ylabel('Source Group', color=SILVER, fontsize=11, labelpad=10)

# Cardinality separator lines
# Zero: 0-1, One: 2-16, Infinity: 17-36
for sep in [1.5, 16.5]:
    ax.axhline(sep, color=GOLD, linewidth=1.0, alpha=0.4)
    ax.axvline(sep, color=GOLD, linewidth=1.0, alpha=0.4)

# Cardinality labels outside the matrix
ax.text(-2.5, 0.5, 'Zero', color=DIM, fontsize=8, ha='center', va='center', rotation=90)
ax.text(-2.5, 9.0, 'One', color=CYAN, fontsize=8, ha='center', va='center', rotation=90)
ax.text(-2.5, 26.5, 'Infinity', color=MAG, fontsize=8, ha='center', va='center', rotation=90)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.tick_params(colors=DIM, labelsize=6.5)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.6, pad=0.02)
cbar.set_label('Flow Count (log scale)', color=SILVER, fontsize=9)
cbar.ax.tick_params(colors=DIM, labelsize=8)
cbar.outline.set_edgecolor(DIM)

save(fig, 'comp12_06_flow_heatmap.png')


# ================================================================
# FIG 7: FAN-OUT / CONVERGENCE GEOMETRY
# Type: 4 (Geometric Cross-Section)
# Shows: Three cardinality interaction patterns as spatial diagrams
#        side by side: One→Infinity (fan-out), Infinity→One
#        (convergence), Infinity→Infinity (list-to-list). The three
#        patterns ARE geometric — spatial relationships.
# ================================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 9), facecolor=BG,
                          gridspec_kw={'wspace': 0.35})

patterns = [
    ('One \u2192 Infinity\n(Fan-Out)', CYAN, MAG),
    ('Infinity \u2192 One\n(Convergence)', MAG, CYAN),
    ('Infinity \u2192 Infinity\n(List-to-List)', MAG, ORANGE),
]

for idx, (title, left_col, right_col) in enumerate(patterns):
    ax = axes[idx]
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')

    ax.text(0, 2.2, title, color=GOLD, fontsize=12, fontweight='bold',
            ha='center', va='center')

    if idx == 0:  # One → Infinity (fan-out)
        # Single node on left
        circle = plt.Circle((-0.8, 0), 0.25, facecolor=BG, edgecolor=left_col,
                             linewidth=2.0, zorder=3)
        ax.add_patch(circle)
        ax.text(-0.8, 0, 'ONE', color=left_col, fontsize=8, fontweight='bold',
                ha='center', va='center', zorder=4)

        # Multiple nodes on right
        n_right = 5
        for i in range(n_right):
            y = 1.6 - i * 0.8
            box = FancyBboxPatch((0.45, y - 0.15), 0.6, 0.30,
                                  boxstyle='round,pad=0.06', facecolor=BG,
                                  edgecolor=right_col, linewidth=1.5, zorder=3)
            ax.add_patch(box)
            ax.text(0.75, y, 'N[%d]' % (i + 1), color=right_col, fontsize=7,
                    ha='center', va='center', zorder=4)
            ax.annotate('', xy=(0.45, y), xytext=(-0.55, 0),
                        arrowprops=dict(arrowstyle='->', color=DIM, lw=0.8, alpha=0.6,
                                        connectionstyle='arc3,rad=%.2f' % (0.1 * (i - 2))))

        ax.text(0, -1.8, 'Constraint filters\nwhich N receive', color=SILVER,
                fontsize=8, ha='center', style='italic')

    elif idx == 1:  # Infinity → One (convergence)
        # Multiple nodes on left
        n_left = 5
        for i in range(n_left):
            y = 1.6 - i * 0.8
            box = FancyBboxPatch((-1.3, y - 0.15), 0.6, 0.30,
                                  boxstyle='round,pad=0.06', facecolor=BG,
                                  edgecolor=left_col, linewidth=1.5, zorder=3)
            ax.add_patch(box)
            ax.text(-1.0, y, 'N[%d]' % (i + 1), color=left_col, fontsize=7,
                    ha='center', va='center', zorder=4)

        # Single node on right
        circle = plt.Circle((0.8, 0), 0.25, facecolor=BG, edgecolor=right_col,
                             linewidth=2.0, zorder=3)
        ax.add_patch(circle)
        ax.text(0.8, 0, 'ONE', color=right_col, fontsize=8, fontweight='bold',
                ha='center', va='center', zorder=4)

        # Highlight one specific node
        highlight_box = FancyBboxPatch((-1.3, 0.0 - 0.15), 0.6, 0.30,
                                        boxstyle='round,pad=0.06', facecolor=BG,
                                        edgecolor=GOLD, linewidth=2.5, zorder=5)
        ax.add_patch(highlight_box)

        # Arrow only from highlighted node
        ax.annotate('', xy=(0.55, 0), xytext=(-0.70, 0),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.8))

        # Dim arrows from others
        for i in range(n_left):
            if i == 2:
                continue
            y = 1.6 - i * 0.8
            ax.annotate('', xy=(0.55, 0), xytext=(-0.70, y),
                        arrowprops=dict(arrowstyle='->', color=DIM, lw=0.5, alpha=0.25,
                                        connectionstyle='arc3,rad=%.2f' % (0.1 * (i - 2))))

        ax.text(0, -1.8, 'One specific member\nreports to singleton', color=SILVER,
                fontsize=8, ha='center', style='italic')

    elif idx == 2:  # Infinity → Infinity (list-to-list)
        # Left population
        n_nodes = 4
        for i in range(n_nodes):
            y = 1.2 - i * 0.8
            box = FancyBboxPatch((-1.3, y - 0.15), 0.55, 0.30,
                                  boxstyle='round,pad=0.06', facecolor=BG,
                                  edgecolor=left_col, linewidth=1.5, zorder=3)
            ax.add_patch(box)
            ax.text(-1.02, y, 'A[%d]' % (i + 1), color=left_col, fontsize=7,
                    ha='center', va='center', zorder=4)

        # Right population
        for i in range(n_nodes):
            y = 1.2 - i * 0.8
            box = FancyBboxPatch((0.55, y - 0.15), 0.55, 0.30,
                                  boxstyle='round,pad=0.06', facecolor=BG,
                                  edgecolor=right_col, linewidth=1.5, zorder=3)
            ax.add_patch(box)
            ax.text(0.82, y, 'B[%d]' % (i + 1), color=right_col, fontsize=7,
                    ha='center', va='center', zorder=4)

        # Crossing arrows (filtered pairs)
        pairs = [(0, 1), (1, 0), (2, 3), (3, 2)]
        for ai, bi in pairs:
            ya = 1.2 - ai * 0.8
            yb = 1.2 - bi * 0.8
            ax.annotate('', xy=(0.55, yb), xytext=(-0.75, ya),
                        arrowprops=dict(arrowstyle='->', color=DIM, lw=0.8, alpha=0.5,
                                        connectionstyle='arc3,rad=0.1'))

        ax.text(0, -1.8, 'Build list A, build list B,\niterate pairs by constraint',
                color=SILVER, fontsize=8, ha='center', style='italic')

fig.suptitle('Cardinality Interaction Patterns', color=GOLD, fontsize=17,
             fontweight='bold', y=0.98)

save(fig, 'comp12_07_cardinality_patterns.png')


# ================================================================
# FIG 8: BOOT TIMELINE WITH PARALLEL FORKS
# Type: 7 (Progression/Sequence Diagram)
# Shows: The OS boot from BIOS to desktop as a left-to-right
#        timeline. Parallel sections (Kernel: console+PCI, Init:
#        clock+loopback) shown as diverging and reconverging lanes.
#        Fan-out points (Init→Services, DevMgr→Devices) shown as
#        one lane splitting to many. Cardinality transitions marked.
# ================================================================

fig, ax = plt.subplots(figsize=(20, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 21)
ax.set_ylim(-4, 5.5)

ax.text(10, 5.0, 'OS Boot Timeline — Parallel Forks and Cardinality Transitions',
        color=GOLD, fontsize=17, fontweight='bold', ha='center', va='center')

# Main timeline: groups as phases, left to right
# y=0 is the main lane
phases = [
    # (x_start, x_end, y, label, color, cardinality)
    (0, 2.0, 0, 'BIOS', DIM, 'Zero'),
    (2.2, 4.2, 0, 'Bootloader', DIM, 'Zero'),
    (4.5, 9.5, 0, 'Kernel', GREEN, 'One'),
    (9.8, 15.5, 0, 'Init System', CYAN, 'One'),
    (15.8, 17.5, 0, 'Display\nServer', BLUE, 'One'),
    (17.8, 20, 0, 'User\nSession', MAG, 'Inf'),
]

for x1, x2, y, label, col, card in phases:
    width = x2 - x1
    box = FancyBboxPatch((x1, y - 0.5), width, 1.0,
                          boxstyle='round,pad=0.15', facecolor=BG,
                          edgecolor=col, linewidth=1.5, zorder=2)
    ax.add_patch(box)
    ax.text((x1 + x2) / 2, y, label, color=col, fontsize=9, fontweight='bold',
            ha='center', va='center', zorder=3)
    ax.text((x1 + x2) / 2, y - 0.72, card, color=DIM, fontsize=7,
            ha='center', va='top')

# Arrows between phases on main lane
arrow_x = [2.0, 4.2, 9.5, 15.5, 17.5]
for ax_val in arrow_x:
    ax.annotate('', xy=(ax_val + 0.2, 0), xytext=(ax_val, 0),
                arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5))

# Cardinality transition markers
transitions = [
    (4.35, 'Zero\n\u2192 One', GREEN),
    (17.65, 'One\n\u2192 Inf', MAG),
]
for tx, label, col in transitions:
    ax.text(tx, 1.3, label, color=col, fontsize=8, fontweight='bold',
            ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.25', facecolor=BG, edgecolor=col, linewidth=1.0))
    ax.plot([tx, tx], [0.55, 1.25], color=col, linewidth=1.0, linestyle=':', alpha=0.5)

# Kernel parallel fork: Console + PCI
# Fork at x=6.5, rejoin at x=8.0
fork_x = 6.5
join_x = 8.2
y_upper = 1.8
y_lower = -1.8

# Fork lines
ax.plot([fork_x, fork_x + 0.3], [0.5, y_upper - 0.3], color=GREEN, linewidth=1.2, linestyle='--')
ax.plot([fork_x, fork_x + 0.3], [-0.5, y_lower + 0.3], color=GREEN, linewidth=1.2, linestyle='--')

# Parallel boxes
par_kernel = [
    (fork_x + 0.3, fork_x + 1.5, y_upper, 'Console Init', GREEN),
    (fork_x + 0.3, fork_x + 1.5, y_lower, 'PCI Enumerate', GREEN),
]
for x1, x2, y, label, col in par_kernel:
    width = x2 - x1
    box = FancyBboxPatch((x1, y - 0.3), width, 0.6,
                          boxstyle='round,pad=0.08', facecolor=BG,
                          edgecolor=col, linewidth=1.0, zorder=2, linestyle='--')
    ax.add_patch(box)
    ax.text((x1 + x2) / 2, y, label, color=col, fontsize=7,
            ha='center', va='center', zorder=3)

# Rejoin lines
ax.plot([fork_x + 1.5, join_x], [y_upper - 0.3, 0.5], color=GREEN, linewidth=1.2, linestyle='--')
ax.plot([fork_x + 1.5, join_x], [y_lower + 0.3, -0.5], color=GREEN, linewidth=1.2, linestyle='--')

# Parallel label
ax.text(fork_x + 0.9, y_upper + 0.55, 'PARALLEL', color=GREEN, fontsize=7,
        ha='center', fontweight='bold', alpha=0.7)

# Init parallel fork: Clock + Loopback
fork_x2 = 12.2
join_x2 = 13.5

ax.plot([fork_x2, fork_x2 + 0.3], [0.5, y_upper - 0.3], color=CYAN, linewidth=1.2, linestyle='--')
ax.plot([fork_x2, fork_x2 + 0.3], [-0.5, y_lower + 0.3], color=CYAN, linewidth=1.2, linestyle='--')

par_init = [
    (fork_x2 + 0.3, fork_x2 + 1.3, y_upper, 'Clock Sync', CYAN),
    (fork_x2 + 0.3, fork_x2 + 1.3, y_lower, 'Loopback Up', CYAN),
]
for x1, x2_val, y, label, col in par_init:
    width = x2_val - x1
    box = FancyBboxPatch((x1, y - 0.3), width, 0.6,
                          boxstyle='round,pad=0.08', facecolor=BG,
                          edgecolor=col, linewidth=1.0, zorder=2, linestyle='--')
    ax.add_patch(box)
    ax.text((x1 + x2_val) / 2, y, label, color=col, fontsize=7,
            ha='center', va='center', zorder=3)

ax.plot([fork_x2 + 1.3, join_x2], [y_upper - 0.3, 0.5], color=CYAN, linewidth=1.2, linestyle='--')
ax.plot([fork_x2 + 1.3, join_x2], [y_lower + 0.3, -0.5], color=CYAN, linewidth=1.2, linestyle='--')

ax.text(fork_x2 + 0.8, y_upper + 0.55, 'PARALLEL', color=CYAN, fontsize=7,
        ha='center', fontweight='bold', alpha=0.7)

# Fan-out points: Init → Services, DevMgr → Devices
fan_outs = [
    (14.5, 'Services\n(N instances)', MAG, -2.8),
    (11.0, 'Devices\n(N instances)', ORANGE, -3.2),
]
for fx, label, col, fy in fan_outs:
    # Fan-out arrow from main lane downward
    ax.annotate(label, xy=(fx, -0.55),
                xytext=(fx, fy), color=col, fontsize=8, fontweight='bold',
                ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color=col, lw=1.2),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=col, linewidth=1.0))

    ax.text(fx + 0.1, fy - 0.55, 'fan-out', color=DIM, fontsize=6,
            ha='center', style='italic')

# Key events along main timeline
key_events = [
    (0.5, 'POST', DIM),
    (1.5, 'MBR', DIM),
    (3.2, 'Kernel\nLoad', DIM),
    (5.0, 'PageTbl', GREEN),
    (5.8, 'MemMgr', GREEN),
    (8.8, 'RootFS', GREEN),
    (9.3, 'Switch', GREEN),
    (10.2, 'Runlvl', CYAN),
    (11.5, 'Udev', CYAN),
    (14.0, 'Network', CYAN),
    (15.0, 'DNS', CYAN),
    (16.5, 'Login', BLUE),
    (18.5, 'Auth', MAG),
    (19.5, 'Desktop', MAG),
]
for ex, label, col in key_events:
    ax.text(ex, -0.25, '.', color=col, fontsize=4, ha='center', va='center')
    ax.text(ex, 0.65, label, color=col, fontsize=5.5, ha='center', va='bottom',
            rotation=45, alpha=0.7)

# Summary at bottom
ax.text(10, -3.8, '~60 events from power-on to desktop  |  2 parallel forks  |  2 cardinality transitions  |  2 fan-out points',
        color=SILVER, fontsize=9, ha='center', style='italic')

save(fig, 'comp12_08_boot_timeline.png')


# ── Summary ──
print("\nAll figures saved:")
print("  1. comp12_01_closed_loop_cycle.png")
print("  2. comp12_02_orchestration_map.png")
print("  3. comp12_03_uai_curves.png")
print("  4. comp12_04_envelope_adsr.png")
print("  5. comp12_05_behavior_landscape.png")
print("  6. comp12_06_flow_heatmap.png")
print("  7. comp12_07_cardinality_patterns.png")
print("  8. comp12_08_boot_timeline.png")
