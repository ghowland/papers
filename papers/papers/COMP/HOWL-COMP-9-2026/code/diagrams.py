#!/usr/bin/env python3
"""
HOWL COMP-9 Diagrams — Building Applications with OpsDB Application Architecture
8 figures covering code reduction, method composition, gating modes, effort distribution,
runner data flow, AI containment, governed state spectrum, and property impact.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as mpatch
import numpy as np
import os

# ============================================================
# GLOBAL STYLE
# ============================================================
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

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for sp in ax.spines.values():
        sp.set_color(DIM)
        sp.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=14)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)


# ================================================================
# FIG 1: CODE REDUCTION RATIOS BY APPLICATION TYPE
# Type: Type 6 (Comparison Bar)
# Shows: The order-of-magnitude gap between conventional and AppDB
#        backend size — visible as bar length difference
# ================================================================

app_names = [
    'Recipe app', 'Personal finance', 'Inventory mgmt', 'Procurement',
    'Project mgmt', 'Education', 'Legal case mgmt', 'HR platform',
    'Compliance', 'CRM',
    'Booking', 'CMS', 'IoT fleet', 'Sub. billing', 'E-commerce',
    'ML platform', 'Chat platform', 'Game backend', 'Video stream', 'Ad auction'
]
conventional = [
    15, 20, 35, 35, 40, 45, 40, 50, 45, 60,
    40, 50, 50, 55, 80,
    45, 70, 60, 65, 55
]
appdb = [
    1.2, 2, 2.5, 2.5, 3, 3.5, 3.5, 4, 3.5, 4,
    6, 5.5, 9, 8, 12,
    19, 43, 34, 29, 24
]
positions = [
    'AP01','AP01','AP01','AP01','AP01','AP01','AP01','AP01','AP01','AP01',
    'AP02','AP02','AP02','AP02','AP02',
    'AP03','AP03','AP03','AP03','AP03'
]
pos_colors = {'AP01': GREEN, 'AP02': CYAN, 'AP03': ORANGE}

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
style_ax(ax, title='Backend Code Size: Conventional vs AppDB',
         xlabel='Lines of Code (thousands)', ylabel='')

y_pos = np.arange(len(app_names))
bar_h = 0.35

# Conventional bars
ax.barh(y_pos + bar_h/2, conventional, height=bar_h, color=RED, alpha=0.6,
        edgecolor=RED, linewidth=1.2, label='Conventional')
# AppDB bars
for i in range(len(app_names)):
    c = pos_colors[positions[i]]
    ax.barh(y_pos[i] - bar_h/2, appdb[i], height=bar_h, color=c, alpha=0.7,
            edgecolor=c, linewidth=1.2)

# Numeric labels
for i in range(len(app_names)):
    ax.text(conventional[i] + 1.2, y_pos[i] + bar_h/2, '%dK' % conventional[i],
            va='center', ha='left', color=RED, fontsize=8, alpha=0.9)
    ratio = conventional[i] / appdb[i]
    c = pos_colors[positions[i]]
    lbl = '%.1fK' % appdb[i] if appdb[i] < 10 else '%dK' % int(appdb[i])
    ax.text(appdb[i] + 0.8, y_pos[i] - bar_h/2, '%s  (%d:1)' % (lbl, int(ratio)),
            va='center', ha='left', color=c, fontsize=8, alpha=0.9)

ax.set_yticks(y_pos)
ax.set_yticklabels(app_names, color=SILVER, fontsize=9)
ax.set_xlim(0, 92)
ax.set_ylim(-0.8, len(app_names) - 0.2)
ax.invert_yaxis()

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=RED, alpha=0.6, edgecolor=RED, label='Conventional'),
    Patch(facecolor=GREEN, alpha=0.7, edgecolor=GREEN, label='AppDB (Primary backend)'),
    Patch(facecolor=CYAN, alpha=0.7, edgecolor=CYAN, label='AppDB (Split backend)'),
    Patch(facecolor=ORANGE, alpha=0.7, edgecolor=ORANGE, label='AppDB (Wrapper)')
]
leg = ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
                facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

# Region labels
ax.axhline(y=9.5, color=DIM, linewidth=0.8, linestyle='--', alpha=0.5)
ax.axhline(y=14.5, color=DIM, linewidth=0.8, linestyle='--', alpha=0.5)
ax.text(88, 4.5, 'Primary\nBackend', color=GREEN, fontsize=8, ha='center',
        va='center', alpha=0.7)
ax.text(88, 12, 'Split\nBackend', color=CYAN, fontsize=8, ha='center',
        va='center', alpha=0.7)
ax.text(88, 17, 'Wrapper', color=ORANGE, fontsize=8, ha='center',
        va='center', alpha=0.7)

save(fig, 'comp9_01_code_reduction_ratios.png')


# ================================================================
# FIG 2: METHOD COMPOSITION BY APPLICATION TYPE
# Type: Type 6 (Heatmap)
# Shows: Which of the 47 methods apply to each application type —
#        the universal core vs position-specific edges
# ================================================================

method_groups = [
    ('Domain\nAnalysis', 'M01-M09', 9),
    ('Schema\nConstruction', 'M10-M18', 9),
    ('Policy\nConstruction', 'M19-M23', 5),
    ('Runner\nConstruction', 'M24-M33', 10),
    ('Frontend\nIntegration', 'M34-M38', 5),
    ('AI\nAssistance', 'M44-M47', 4),
    ('App\nPattern', 'M39-M43', 5),
]

app_types = ['Governed-State\nDominant', 'Split\nBackend', 'Operational\nWrapper',
             'Personal', 'Distributed']

# applicability: fraction of methods in each group used by each app type
# rows = app types, cols = method groups
data = np.array([
    [6/9, 9/9, 5/5, 8/10, 5/5, 4/4, 1/5],   # governed-state
    [9/9, 9/9, 5/5, 10/10, 5/5, 4/4, 1/5],   # split
    [5/9, 4/9, 2/5, 4/10, 3/5, 2/4, 1/5],     # wrapper
    [4/9, 6/9, 1/5, 5/10, 4/5, 2/4, 1/5],     # personal
    [9/9, 9/9, 5/5, 10/10, 5/5, 4/4, 2/5],    # distributed (inner + M43)
])

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Method Applicability by Application Type')

im = ax.imshow(data, cmap='YlGn', aspect='auto', vmin=0, vmax=1, alpha=0.85)

ax.set_xticks(range(len(method_groups)))
ax.set_xticklabels([g[0] for g in method_groups], color=SILVER, fontsize=9, ha='center')
ax.set_yticks(range(len(app_types)))
ax.set_yticklabels(app_types, color=SILVER, fontsize=10)

# Cell labels: show fraction and actual count
for i in range(len(app_types)):
    for j in range(len(method_groups)):
        val = data[i, j]
        total = method_groups[j][2]
        count = int(round(val * total))
        txt_color = BG if val > 0.55 else WHITE
        ax.text(j, i, '%d/%d' % (count, total), ha='center', va='center',
                color=txt_color, fontsize=10, fontweight='bold')

# Method ID ranges below each column
for j in range(len(method_groups)):
    ax.text(j, len(app_types) - 0.5 + 0.45, method_groups[j][1],
            ha='center', va='top', color=DIM, fontsize=7)

ax.set_xlim(-0.5, len(method_groups) - 0.5)
ax.set_ylim(len(app_types) - 0.5, -0.5)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.6, pad=0.03)
cbar.set_label('Fraction of Methods Used', color=SILVER, fontsize=10)
cbar.ax.tick_params(colors=DIM, labelsize=8)

# Annotation
ax.text(len(method_groups) - 0.5, -0.85, '47 construction methods across 7 groups',
        ha='right', va='bottom', color=DIM, fontsize=8, style='italic')

save(fig, 'comp9_02_method_composition.png')


# ================================================================
# FIG 3: GATING MODE PROPERTY ACCUMULATION
# Type: Type 2 (Scale/Landscape)
# Shows: Governance gradient from direct write to approval-required —
#        each mode accumulates properties as visible layers
# ================================================================

modes = ['Direct\nWrite', 'Auto-\nApprove', 'Post-\nApproval', 'Emergency', 'Approval\nRequired']
properties_list = [
    'Authentication',
    'Authorization (5 layers)',
    'Schema Validation',
    'Bound Validation',
    'Audit Logging',
    'Change Set Created',
    'Version Row Created',
    'Approval Routing',
    'Segregation of Duties',
    'Full Review Period'
]

# Which properties each mode provides (1 = yes, 0 = no)
mode_props = np.array([
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # direct write
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # auto-approve
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # post-approval
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # emergency (reduced approval)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # approval-required
])

prop_colors = [BLUE, BLUE, CYAN, CYAN, ORANGE, GREEN, GREEN, MAG, MAG, GOLD]

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Gating Mode: Property Accumulation',
         xlabel='', ylabel='')

cell_w = 0.85
cell_h = 0.7
x_start = 0.5
y_start = 0.5

for mi in range(len(modes)):
    mx = x_start + mi * 1.2
    # Mode label at top
    ax.text(mx + cell_w/2, y_start + len(properties_list) * 0.85 + 0.5,
            modes[mi], ha='center', va='bottom', color=WHITE, fontsize=10,
            fontweight='bold')

    for pi in range(len(properties_list)):
        my = y_start + pi * 0.85
        if mode_props[mi, pi]:
            rect = mpatches.FancyBboxPatch(
                (mx, my), cell_w, cell_h,
                boxstyle='round,pad=0.05',
                facecolor=prop_colors[pi], alpha=0.5,
                edgecolor=prop_colors[pi], linewidth=1.0
            )
        else:
            rect = mpatches.FancyBboxPatch(
                (mx, my), cell_w, cell_h,
                boxstyle='round,pad=0.05',
                facecolor=PAN, alpha=0.3,
                edgecolor=DIM, linewidth=0.5, linestyle='--'
            )
        ax.add_patch(rect)

# Property labels on the left
for pi in range(len(properties_list)):
    my = y_start + pi * 0.85
    ax.text(x_start - 0.15, my + cell_h/2, properties_list[pi],
            ha='right', va='center', color=SILVER, fontsize=9)

# Property count at bottom of each column
for mi in range(len(modes)):
    mx = x_start + mi * 1.2
    count = int(mode_props[mi].sum())
    ax.text(mx + cell_w/2, y_start - 0.35, '%d/10' % count,
            ha='center', va='top', color=GOLD, fontsize=11, fontweight='bold')

# Governance arrow at bottom
arrow_x1 = x_start + cell_w/2
arrow_x2 = x_start + (len(modes) - 1) * 1.2 + cell_w/2
arrow_y = y_start - 0.7
ax.annotate('', xy=(arrow_x2, arrow_y), xytext=(arrow_x1, arrow_y),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
ax.text((arrow_x1 + arrow_x2) / 2, arrow_y - 0.25, 'Increasing Governance',
        ha='center', va='top', color=GOLD, fontsize=10, style='italic')

ax.set_xlim(-2.5, x_start + len(modes) * 1.2 + 0.5)
ax.set_ylim(arrow_y - 0.5, y_start + len(properties_list) * 0.85 + 1.2)
ax.axis('off')

save(fig, 'comp9_03_gating_mode_properties.png')


# ================================================================
# FIG 4: CONSTRUCTION EFFORT DISTRIBUTION BY POSITION
# Type: Type 6 (Stacked Bar)
# Shows: How effort allocation shifts across architecture positions —
#        the crossover from schema-dominant to specialized-system-dominant
# ================================================================

positions_names = ['Primary\nBackend\n(AP01)', 'Split\nBackend\n(AP02)',
                   'Operational\nWrapper\n(AP03)', 'Personal\n(AP05)',
                   'Distributed\n(AP06)']

# Effort percentages for each category
schema_design =   [40, 20, 8, 35, 18]
policy_config =   [10, 8, 5, 5, 8]
runner_impl =     [25, 15, 8, 25, 15]
hot_path =        [0, 35, 55, 0, 30]
frontend =        [25, 22, 24, 35, 24]
release_pkg =     [0, 0, 0, 0, 5]

categories = ['Schema Design', 'Policy Config', 'Runner Implementation',
              'Hot-Path / Specialized', 'Frontend', 'Release Packaging']
cat_colors = [GREEN, PURPLE, CYAN, RED, BLUE, ORANGE]
cat_data = [schema_design, policy_config, runner_impl, hot_path, frontend, release_pkg]

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, title='Construction Effort Distribution by Architecture Position',
         xlabel='', ylabel='Effort (%)')

x = np.arange(len(positions_names))
bar_width = 0.55
bottom = np.zeros(len(positions_names))

bars_list = []
for ci in range(len(categories)):
    vals = np.array(cat_data[ci], dtype=float)
    b = ax.bar(x, vals, bar_width, bottom=bottom, color=cat_colors[ci],
               alpha=0.7, edgecolor=cat_colors[ci], linewidth=1.2,
               label=categories[ci])
    bars_list.append(b)
    # Labels inside segments (only if tall enough)
    for i in range(len(positions_names)):
        if vals[i] >= 8:
            ax.text(x[i], bottom[i] + vals[i]/2, '%d%%' % int(vals[i]),
                    ha='center', va='center', color=WHITE, fontsize=9,
                    fontweight='bold')
    bottom += vals

ax.set_xticks(x)
ax.set_xticklabels(positions_names, color=SILVER, fontsize=10)
ax.set_ylim(0, 108)
ax.set_xlim(-0.6, len(positions_names) - 0.4)

leg = ax.legend(loc='upper right', fontsize=9, facecolor=PAN, edgecolor=DIM,
                labelcolor=WHITE, ncol=2)

# Annotation
ax.text(0, 105, 'Governed-state apps:\neffort is schema + runners',
        color=GREEN, fontsize=8, ha='center', va='bottom', alpha=0.8)
ax.text(2, 105, 'Wrapper apps:\neffort is the specialized system',
        color=RED, fontsize=8, ha='center', va='bottom', alpha=0.8)

save(fig, 'comp9_04_effort_distribution.png')


# ================================================================
# FIG 5: RUNNER DATA FLOW TOPOLOGY
# Type: Type 4 (Geometric)
# Shows: Circulation of data — pullers in from external, reconcilers
#        compare, verifiers produce evidence, config push sends out
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.set_title('Runner Data Flow Topology', color=GOLD, fontsize=16,
             fontweight='bold', pad=18)

def draw_box(ax, x, y, w, h, label, color, sublabel=None):
    rect = mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle='round,pad=0.15',
        facecolor=color, alpha=0.18, edgecolor=color, linewidth=1.8
    )
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2 + (0.12 if sublabel else 0),
            label, ha='center', va='center', color=color,
            fontsize=11, fontweight='bold')
    if sublabel:
        ax.text(x + w/2, y + h/2 - 0.22, sublabel,
                ha='center', va='center', color=color, fontsize=7, alpha=0.7)

# Central: OpsDB substrate
draw_box(ax, 6.0, 4.0, 6.0, 4.0, 'OpsDB Substrate', GOLD)
# Sub-regions inside OpsDB
draw_box(ax, 6.4, 6.2, 2.4, 1.4, 'Governed\nEntities', GREEN, None)
draw_box(ax, 9.2, 6.2, 2.4, 1.4, 'Observation\nCache', CYAN, None)
draw_box(ax, 6.4, 4.4, 2.4, 1.4, 'Policies &\nRunner Specs', PURPLE, None)
draw_box(ax, 9.2, 4.4, 2.4, 1.4, 'Evidence\nRecords', MAG, None)

# External systems (left)
draw_box(ax, 0.3, 6.5, 3.0, 1.8, 'External\nSystems', RED,
         'Cloud, K8s, IdP, APIs')

# Hot-path system (right)
draw_box(ax, 14.7, 6.5, 3.0, 1.8, 'Hot-Path\nSystems', ORANGE,
         'Trading, Chat, Gaming')

# Frontend (top)
draw_box(ax, 7.5, 10.5, 3.0, 1.2, 'Frontend / API\nConsumers', BLUE)

# Runner kinds around the edges
runner_specs = [
    (1.0, 3.8, 'Puller\nRunners', GREEN, 'RK01'),
    (1.0, 1.5, 'Observation\nPull Runners', CYAN, 'RK08'),
    (5.0, 1.5, 'Reconciler\nRunners', BLUE, 'RK02'),
    (9.0, 1.5, 'Verifier\nRunners', MAG, 'RK03'),
    (13.0, 1.5, 'Config Push\nRunners', ORANGE, 'RK07'),
    (15.0, 3.8, 'AI Observation\nRunners', PURPLE, 'RK09'),
    (5.0, 3.0, 'Notification\nRunners', SILVER, 'RK04'),
    (13.0, 3.0, 'Reaper\nRunners', DIM, 'RK06'),
]

for rx, ry, rlabel, rcolor, rid in runner_specs:
    draw_box(ax, rx, ry, 2.2, 1.2, rlabel, rcolor, rid)

# Arrows showing data flow
arrow_kw = dict(arrowstyle='->', lw=1.8, connectionstyle='arc3,rad=0.1')

# Puller: External -> Observation Cache
ax.annotate('', xy=(9.2, 6.9), xytext=(3.3, 7.4),
            arrowprops=dict(color=GREEN, **arrow_kw))
ax.text(6.0, 7.8, 'pull state', color=GREEN, fontsize=7, ha='center',
        alpha=0.8, style='italic')

# Config Push: Governed -> Hot-Path
ax.annotate('', xy=(14.7, 7.4), xytext=(11.6, 6.9),
            arrowprops=dict(color=ORANGE, **arrow_kw))
ax.text(13.2, 7.8, 'push config', color=ORANGE, fontsize=7, ha='center',
        alpha=0.8, style='italic')

# Observation Pull: Hot-Path -> Observation Cache
ax.annotate('', xy=(10.4, 6.2), xytext=(14.7, 6.8),
            arrowprops=dict(color=CYAN, **arrow_kw))
ax.text(13.2, 6.0, 'pull results', color=CYAN, fontsize=7, ha='center',
        alpha=0.8, style='italic')

# Reconciler: Governed + Obs Cache -> Change Sets
ax.annotate('', xy=(7.6, 4.4), xytext=(6.1, 2.7),
            arrowprops=dict(color=BLUE, **arrow_kw))
ax.text(5.5, 3.5, 'propose\ncorrections', color=BLUE, fontsize=7, ha='center',
        alpha=0.8, style='italic')

# Verifier: reads targets, writes evidence
ax.annotate('', xy=(10.4, 4.4), xytext=(10.1, 2.7),
            arrowprops=dict(color=MAG, **arrow_kw))
ax.text(11.0, 3.3, 'write\nevidence', color=MAG, fontsize=7, ha='center',
        alpha=0.8, style='italic')

# AI Obs: reads governed, writes observation cache
ax.annotate('', xy=(10.4, 5.8), xytext=(15.1, 5.0),
            arrowprops=dict(color=PURPLE, **arrow_kw))
ax.text(13.5, 5.0, 'AI summaries', color=PURPLE, fontsize=7, ha='center',
        alpha=0.8, style='italic')

# Frontend: reads from OpsDB
ax.annotate('', xy=(9.0, 8.0), xytext=(9.0, 10.5),
            arrowprops=dict(color=BLUE, arrowstyle='<->', lw=1.5,
                           connectionstyle='arc3,rad=0'))
ax.text(9.6, 9.3, 'API', color=BLUE, fontsize=8, alpha=0.8)

# Gate pipeline label
ax.text(9.0, 8.3, 'Gate Pipeline (10 steps)', ha='center', va='bottom',
        color=GOLD, fontsize=8, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD,
                  alpha=0.8))

save(fig, 'comp9_05_runner_data_flow.png')


# ================================================================
# FIG 6: AI CONTAINMENT WITHIN GOVERNANCE BOUNDARY
# Type: Type 4 (Geometric)
# Shows: Structural containment of AI actions — change sets enter
#        pipeline, observation cache is direct-write target, human
#        approval gates governed changes
# ================================================================

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.set_title('AI Containment Within Governance Boundary', color=GOLD,
             fontsize=16, fontweight='bold', pad=18)

# Outer governance boundary
gov_rect = mpatches.FancyBboxPatch(
    (2.5, 1.0), 13.0, 8.5, boxstyle='round,pad=0.3',
    facecolor=GOLD, alpha=0.04, edgecolor=GOLD, linewidth=2.5
)
ax.add_patch(gov_rect)
ax.text(9.0, 9.7, 'OpsDB Governance Boundary', ha='center', va='bottom',
        color=GOLD, fontsize=12, fontweight='bold')

# AI Runner (left, outside-ish)
draw_box(ax, 0.2, 5.5, 2.5, 2.0, 'AI Runner', PURPLE, 'LLM calls via\nlibrary suite')

# Gate Pipeline (center)
gate_x = 5.0
gate_y = 3.5
gate_w = 4.5
gate_h = 5.0
gate_rect = mpatches.FancyBboxPatch(
    (gate_x, gate_y), gate_w, gate_h, boxstyle='round,pad=0.15',
    facecolor=ORANGE, alpha=0.08, edgecolor=ORANGE, linewidth=1.8
)
ax.add_patch(gate_rect)
ax.text(gate_x + gate_w/2, gate_y + gate_h - 0.3, 'Gate Pipeline',
        ha='center', va='top', color=ORANGE, fontsize=11, fontweight='bold')

# Gate steps (stacked vertically inside pipeline)
gate_steps = [
    ('1. Auth', BLUE), ('2. Authz (5 layers)', BLUE),
    ('3. Schema Validate', CYAN), ('4. Bound Validate', CYAN),
    ('5. Policy Evaluate', PURPLE), ('6. Versioning', GREEN),
    ('7. Change Mgmt', MAG), ('8. Audit Log', ORANGE),
    ('9. Execute', GREEN), ('10. Response', SILVER)
]
step_h = 0.38
step_gap = 0.04
total_steps_h = len(gate_steps) * (step_h + step_gap)
step_y_start = gate_y + gate_h - 0.7

for si, (sname, scolor) in enumerate(gate_steps):
    sy = step_y_start - si * (step_h + step_gap)
    sr = mpatches.FancyBboxPatch(
        (gate_x + 0.3, sy), gate_w - 0.6, step_h,
        boxstyle='round,pad=0.05',
        facecolor=scolor, alpha=0.2, edgecolor=scolor, linewidth=0.8
    )
    ax.add_patch(sr)
    ax.text(gate_x + gate_w/2, sy + step_h/2, sname,
            ha='center', va='center', color=scolor, fontsize=7.5)

# Human Approval Gate (between step 7 and pipeline output)
draw_box(ax, 10.2, 5.2, 2.8, 1.8, 'Human\nApproval', MAG, 'Reviews AI\nproposals')

# Governed Entities (right)
draw_box(ax, 13.5, 6.5, 2.5, 2.0, 'Governed\nEntities', GREEN,
         'Versioned, audited\nchange-managed')

# Observation Cache (right, lower)
draw_box(ax, 13.5, 3.5, 2.5, 2.0, 'Observation\nCache', CYAN,
         'AI summaries\nfreshness-stamped')

# Audit Log (bottom center)
draw_box(ax, 6.5, 1.3, 3.0, 1.5, 'Audit Log', ORANGE,
         'Every action\nrecorded')

# Arrows
arrow_kw2 = dict(arrowstyle='->', lw=2.0)

# AI -> Gate Pipeline (proposes change sets)
ax.annotate('', xy=(5.0, 6.8), xytext=(2.7, 6.5),
            arrowprops=dict(color=PURPLE, **arrow_kw2))
ax.text(3.8, 7.3, 'Propose\nChange Set', color=PURPLE, fontsize=8,
        ha='center', va='bottom')

# AI -> Observation Cache (direct write path)
ax.annotate('', xy=(13.5, 4.5), xytext=(2.7, 5.7),
            arrowprops=dict(color=CYAN, lw=1.5, arrowstyle='->',
                           connectionstyle='arc3,rad=-0.3'))
ax.text(7.0, 2.8, 'Direct write (observations only)', color=CYAN,
        fontsize=8, ha='center', style='italic')

# Gate Pipeline -> Human Approval
ax.annotate('', xy=(10.2, 6.1), xytext=(9.5, 6.1),
            arrowprops=dict(color=MAG, **arrow_kw2))

# Human Approval -> Governed Entities
ax.annotate('', xy=(13.5, 7.2), xytext=(13.0, 6.5),
            arrowprops=dict(color=GREEN, **arrow_kw2))
ax.text(13.2, 7.0, 'Approved', color=GREEN, fontsize=8, ha='center')

# Human Approval -> Rejection
ax.text(11.6, 5.0, 'or Reject', color=RED, fontsize=8, ha='center',
        style='italic', alpha=0.7)

# Gate -> Audit (everything audited)
ax.annotate('', xy=(8.0, 2.8), xytext=(8.0, 3.5),
            arrowprops=dict(color=ORANGE, lw=1.2, arrowstyle='->'))

# Key insight labels
ax.text(1.0, 1.5, 'AI never writes governed state directly\n'
        'AI proposes — humans approve — infrastructure enforces',
        color=GOLD, fontsize=9, ha='left', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD,
                  alpha=0.8))

save(fig, 'comp9_06_ai_containment.png')


# ================================================================
# FIG 7: GOVERNED STATE RATIO SPECTRUM
# Type: Type 3 (Threshold/Region)
# Shows: Clustering of application types by governed percentage —
#        most software at 95%+, region boundaries visible
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, title='Governed State Ratio Spectrum',
         xlabel='Governed State (%)', ylabel='')

# Application types with their governed ratios
apps_spectrum = [
    ('Compliance platform', 99, 'AP01'),
    ('Personal data', 99, 'AP01'),
    ('Business SaaS (CRM/ERP)', 95, 'AP01'),
    ('Internal tools', 95, 'AP01'),
    ('Case management', 95, 'AP01'),
    ('Healthcare records', 95, 'AP01'),
    ('Education platform', 95, 'AP01'),
    ('Document/Knowledge mgmt', 95, 'AP01'),
    ('Inventory/Asset tracking', 95, 'AP01'),
    ('Procurement', 95, 'AP01'),
    ('Financial services', 90, 'AP02'),
    ('Research data mgmt', 90, 'AP02'),
    ('Content management', 85, 'AP02'),
    ('Booking/Scheduling', 85, 'AP02'),
    ('API gateway config', 85, 'AP02'),
    ('Sub. billing', 85, 'AP02'),
    ('E-commerce', 80, 'AP02'),
    ('Supply chain', 80, 'AP02'),
    ('Workflow engine', 80, 'AP02'),
    ('Turn-based games', 75, 'AP02'),
    ('IoT fleet mgmt', 70, 'AP02'),
    ('ML platform', 20, 'AP03'),
    ('Real-time comms', 20, 'AP03'),
    ('Video streaming', 15, 'AP03'),
    ('Stream processing', 15, 'AP03'),
    ('Real-time gaming', 15, 'AP03'),
    ('Ad auction / RTB', 10, 'AP03'),
    ('High-freq trading', 10, 'AP03'),
]

# Region shading
ax.axvspan(70, 100, alpha=0.06, color=GREEN)
ax.axvspan(30, 70, alpha=0.06, color=CYAN)
ax.axvspan(0, 30, alpha=0.06, color=ORANGE)

# Region labels at top
ax.text(85, len(apps_spectrum) + 0.5, 'Primary Backend (AP01)',
        ha='center', va='bottom', color=GREEN, fontsize=10, fontweight='bold')
ax.text(50, len(apps_spectrum) + 0.5, 'Split Backend\n(AP02)',
        ha='center', va='bottom', color=CYAN, fontsize=10, fontweight='bold')
ax.text(15, len(apps_spectrum) + 0.5, 'Wrapper (AP03)',
        ha='center', va='bottom', color=ORANGE, fontsize=10, fontweight='bold')

# Boundary lines
ax.axvline(x=70, color=DIM, linewidth=1.0, linestyle='--', alpha=0.5)
ax.axvline(x=30, color=DIM, linewidth=1.0, linestyle='--', alpha=0.5)

# Plot each app as a horizontal point
y_positions = list(range(len(apps_spectrum)))
for i, (name, ratio, pos) in enumerate(apps_spectrum):
    c = pos_colors.get(pos, SILVER)
    ax.scatter(ratio, i, s=180, color=c, edgecolors=WHITE, linewidth=1.5,
               zorder=5, alpha=0.85)
    # Label to the right of the point, or left if too close to right edge
    if ratio > 80:
        ax.text(ratio - 2, i, name, ha='right', va='center', color=SILVER,
                fontsize=8)
    else:
        ax.text(ratio + 2, i, name, ha='left', va='center', color=SILVER,
                fontsize=8)

ax.set_yticks([])
ax.set_xlim(-2, 105)
ax.set_ylim(-1.5, len(apps_spectrum) + 2)
ax.invert_yaxis()

# Annotation: most software clusters here
cluster_rect = mpatches.FancyBboxPatch(
    (88, -0.5), 14, 11, boxstyle='round,pad=0.2',
    facecolor=GREEN, alpha=0.04, edgecolor=GREEN, linewidth=1.0,
    linestyle='--'
)
ax.add_patch(cluster_rect)
ax.text(102, 5, 'Most business\nsoftware', ha='center', va='center',
        color=GREEN, fontsize=8, style='italic', alpha=0.7)

save(fig, 'comp9_07_governed_state_spectrum.png')


# ================================================================
# FIG 8: PROPERTY IMPACT OF GOVERNANCE FLAGS
# Type: Type 1 (Radar/Convergence)
# Shows: Area reduction from full governance to draft mode —
#        specific axes contract while others hold
# ================================================================

properties_radar = [
    'Schema\nValidation',
    'Authorization\n(5 layers)',
    'Bound\nValidation',
    'Policy\nEvaluation',
    'Per-write\nVersioning',
    'Change\nManagement',
    'Audit\nLogging',
    'Point-in-time\nReconstruction',
    'Optimistic\nConcurrency',
    'Search\nAPI'
]

N_props = len(properties_radar)
angles = np.linspace(0, 2 * np.pi, N_props, endpoint=False).tolist()
angles += angles[:1]  # close the polygon

# Full governance: all at 1.0
full_gov = [1.0] * N_props + [1.0]

# Draft mode: versioning, change mgmt, audit reduced
draft_mode = [1.0, 1.0, 1.0, 1.0, 0.15, 0.15, 0.15, 0.4, 1.0, 1.0]
draft_mode += draft_mode[:1]

# Change-set bypass: versioning and change mgmt gone, audit preserved
cs_bypass = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.1, 0.5, 1.0]
cs_bypass += cs_bypass[:1]

fig, ax = plt.subplots(figsize=(14, 12), facecolor=BG,
                        subplot_kw=dict(polar=True))
ax.set_facecolor(PAN)

# Draw the radar
ax.plot(angles, full_gov, 'o-', color=GREEN, linewidth=2.5, label='Full Governance',
        markersize=6)
ax.fill(angles, full_gov, color=GREEN, alpha=0.08)

ax.plot(angles, draft_mode, 's-', color=CYAN, linewidth=2.0, label='Draft Mode',
        markersize=5)
ax.fill(angles, draft_mode, color=CYAN, alpha=0.08)

ax.plot(angles, cs_bypass, 'D-', color=ORANGE, linewidth=2.0,
        label='Change-Set Bypass', markersize=5)
ax.fill(angles, cs_bypass, color=ORANGE, alpha=0.08)

# Axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(properties_radar, color=SILVER, fontsize=9)

# Radial grid
ax.set_yticks([0.25, 0.5, 0.75, 1.0])
ax.set_yticklabels(['25%', '50%', '75%', '100%'], color=DIM, fontsize=7)
ax.set_ylim(0, 1.1)

# Grid styling
ax.xaxis.grid(True, color=DIM, linewidth=0.5, alpha=0.3)
ax.yaxis.grid(True, color=DIM, linewidth=0.5, alpha=0.3)
ax.spines['polar'].set_color(DIM)
ax.spines['polar'].set_linewidth(0.5)

# Title
ax.set_title('Property Coverage by Governance Mode', color=GOLD,
             fontsize=15, fontweight='bold', pad=30)

# Legend
leg = ax.legend(loc='lower right', bbox_to_anchor=(1.25, -0.05), fontsize=10,
                facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

# Annotations for weakened properties
# Using figure text to avoid polar coordinate issues
fig.text(0.5, 0.02,
         'Draft mode weakens: per-write versioning, change management, audit logging\n'
         'Preserved: schema validation, authorization, bound validation, policy, search',
         ha='center', va='bottom', color=SILVER, fontsize=9,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

save(fig, 'comp9_08_property_impact_radar.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n  HOWL COMP-9 Diagrams Complete:")
print("  1. comp9_01_code_reduction_ratios.png")
print("  2. comp9_02_method_composition.png")
print("  3. comp9_03_gating_mode_properties.png")
print("  4. comp9_04_effort_distribution.png")
print("  5. comp9_05_runner_data_flow.png")
print("  6. comp9_06_ai_containment.png")
print("  7. comp9_07_governed_state_spectrum.png")
print("  8. comp9_08_property_impact_radar.png")
