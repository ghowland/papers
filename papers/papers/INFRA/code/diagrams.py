#!/usr/bin/env python3
"""
HOWL OpsDB Reading Guide Diagrams - How to Read the Series
8 figures covering reading order, paper dependencies, stage-to-paper mapping,
section pointers, comprehension order, knowledge accumulation, pitfalls, and
re-read access patterns.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
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

# Stage colors (consistent across figures)
STAGE_COLORS = {
    1: GOLD,    # Context (INFRA-7)
    2: BLUE,    # Architecture (INFRA-2)
    3: ORANGE,  # Path (INFRA-9)
    4: CYAN,    # Details (INFRA-3,4,5,6,8)
    5: PURPLE,  # Vocabulary (INFRA-1)
}

# Paper data: (id, stage, short_title, deliverable)
PAPERS = [
    ('INFRA-7', 1, 'Coherent Operations',     'What it is, what you get'),
    ('INFRA-2', 2, 'OpsDB Design',            'Architectural commitments'),
    ('INFRA-9', 3, 'Implementation Path',     'How to build it'),
    ('INFRA-3', 4, 'Example Schema',          'What the data looks like'),
    ('INFRA-4', 4, 'Runner Design',           'Operational logic layer'),
    ('INFRA-5', 4, 'API Layer',               'The governance gate'),
    ('INFRA-6', 4, 'Schema Construction',     'Schema as data, governed'),
    ('INFRA-8', 4, 'Library Suite',           'Framework around runners'),
    ('INFRA-1', 5, 'Taxonomy',                'Vocabulary that grounds it'),
]

def style_axes(ax):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

# ================================================================
# FIG 1: FIVE-STAGE ONION (NESTED LAYERS)
# Type: 4 (Geometric Cross-Section)
# Shows: each stage builds on the prior. Outermost is taxonomy
# (read last); innermost is context (read first). The nesting
# communicates the build-up that text cannot.
# ================================================================

fig, ax = plt.subplots(figsize=(15, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-9, 9)
ax.set_ylim(-9, 9)
ax.set_aspect('equal')
ax.axis('off')

# Concentric circles, outermost first
# Stage 5 (vocabulary) outermost - read last
# Stage 1 (context) innermost - read first
ring_specs = [
    (5, 8.0, PURPLE, 'Stage 5: Taxonomy',           'INFRA-1'),
    (4, 6.5, CYAN,   'Stage 4: Details',            'INFRA-3, 4, 5, 6, 8'),
    (3, 4.8, ORANGE, 'Stage 3: Path',               'INFRA-9'),
    (2, 3.2, BLUE,   'Stage 2: Architecture',       'INFRA-2'),
    (1, 1.6, WHITE,   'Stage 1: Context',            'INFRA-7'),
]

# Draw outermost first so smaller circles overlay
for stage, radius, color, label, papers in ring_specs:
    alpha = 0.20 + (5 - stage) * 0.10
    circle = Circle((0, 0), radius, facecolor=color, edgecolor=color,
                    linewidth=2, alpha=alpha)
    ax.add_patch(circle)

# Now place labels inside each ring band (between concentric boundaries)
# Stage 1 center
ax.text(0, 0.4, 'Stage 1', color=GOLD, fontsize=12,
        ha='center', va='center', fontweight='bold')
ax.text(0, -0.2, 'Context', color=GOLD, fontsize=10,
        ha='center', va='center')
ax.text(0, -0.7, 'INFRA-7', color=WHITE, fontsize=11,
        ha='center', va='center', fontweight='bold')

# Stage 2 band (between r=1.6 and r=3.2), label at top of band
ax.text(0, 2.4, 'Stage 2: Architecture', color=BLUE, fontsize=11,
        ha='center', va='center', fontweight='bold')
ax.text(0, 2.0, 'INFRA-2', color=WHITE, fontsize=10,
        ha='center', va='center')

# Stage 3 band (between r=3.2 and r=4.8), label at top
ax.text(0, 4.0, 'Stage 3: Path', color=ORANGE, fontsize=11,
        ha='center', va='center', fontweight='bold')
ax.text(0, 3.6, 'INFRA-9', color=WHITE, fontsize=10,
        ha='center', va='center')

# Stage 4 band (between r=4.8 and r=6.5), label at top
ax.text(0, 5.65, 'Stage 4: Details', color=CYAN, fontsize=11,
        ha='center', va='center', fontweight='bold')
ax.text(0, 5.20, 'INFRA-3, 4, 5, 6, 8', color=WHITE, fontsize=10,
        ha='center', va='center')

# Stage 5 band (between r=6.5 and r=8.0), label at top
ax.text(0, 7.25, 'Stage 5: Taxonomy', color=PURPLE, fontsize=11,
        ha='center', va='center', fontweight='bold')
ax.text(0, 6.85, 'INFRA-1', color=WHITE, fontsize=10,
        ha='center', va='center')

# "Read first" arrow pointing to center (offset to left)
ax.annotate('Read FIRST\n(innermost)',
            xy=(-1.0, 0), xytext=(-7.0, 0),
            color=GOLD, fontsize=10, ha='center', va='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# "Read last" arrow pointing to outer ring (right side)
ax.annotate('Read LAST\n(outermost)',
            xy=(7.5, 0), xytext=(7.7, -3.5),
            color=PURPLE, fontsize=10, ha='center', va='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.5))

# Bottom note
ax.text(0, -8.5,
        'Each layer builds on the prior. Inner stages are prerequisites for outer ones.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.set_title('The Five Stages of the Reading Path: Each Layer Builds on the Prior',
             color=GOLD, fontsize=15, fontweight='bold', pad=18)

save(fig, 'reading_guide_01_five_stage_onion.png')

# ================================================================
# FIG 2: PAPER DEPENDENCY DAG
# Type: 5 (Connection Map)
# Shows: actual dependency relationships between papers. Text cannot
# convey graph structure efficiently.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')

# Position papers in dependency layout
# Top: foundational/reference layer (INFRA-1)
# Below: arch (INFRA-2 sits at the heart)
# Spread the rest by their conceptual position
positions = {
    'INFRA-1': (8.0, 9.5),   # Taxonomy (referenced by all)
    'INFRA-7': (2.0, 7.5),   # Intro
    'INFRA-2': (8.0, 7.5),   # Design (central)
    'INFRA-9': (14.0, 7.5),  # Implementation path
    'INFRA-3': (3.0, 4.5),   # Schema example
    'INFRA-4': (6.5, 4.5),   # Runners
    'INFRA-5': (10.0, 4.5),  # API
    'INFRA-6': (13.0, 4.5),  # Schema construction
    'INFRA-8': (8.0, 2.0),   # Library suite (sits below runners and API)
}

# Stage colors per paper
paper_stage = {p[0]: p[1] for p in PAPERS}
paper_title = {p[0]: p[2] for p in PAPERS}

# Draw dependency edges first (so nodes overlay)
# Numbered-order dependencies: each paper builds on prior in numbered series
deps = [
    ('INFRA-2', 'INFRA-3'),  # 3 demonstrates 2's design
    ('INFRA-2', 'INFRA-4'),  # 4 specifies runners for 2's design
    ('INFRA-2', 'INFRA-5'),  # 5 specifies API for 2's gate claim
    ('INFRA-3', 'INFRA-6'),  # 6 specifies how to build 3's schema
    ('INFRA-2', 'INFRA-6'),  # 6 implements 2's schema commitment
    ('INFRA-4', 'INFRA-8'),  # 8 specifies libraries 4 promised
    ('INFRA-5', 'INFRA-8'),  # 8 closes 5's runner authority gap
    ('INFRA-2', 'INFRA-7'),  # 7 introduces 2's design
    ('INFRA-2', 'INFRA-9'),  # 9 specifies how to build 2's design
    ('INFRA-1', 'INFRA-2'),  # 2 uses 1's vocabulary
    ('INFRA-1', 'INFRA-4'),
    ('INFRA-1', 'INFRA-5'),
]

for src, dst in deps:
    sx, sy = positions[src]
    dx, dy = positions[dst]
    arrow = FancyArrowPatch((sx, sy), (dx, dy),
                             arrowstyle='->', color=DIM,
                             linewidth=1.0, alpha=0.5,
                             mutation_scale=12,
                             connectionstyle='arc3,rad=0.1')
    ax.add_patch(arrow)

# Draw paper nodes
for paper_id, (x, y) in positions.items():
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]
    title = paper_title[paper_id]

    # Box
    w, h = 1.7, 0.95
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle='round,pad=0.05', facecolor=PAN,
                          edgecolor=color, linewidth=2, zorder=3)
    ax.add_patch(box)
    ax.text(x, y + 0.18, paper_id, color=WHITE, fontsize=10,
            ha='center', va='center', fontweight='bold', zorder=4)
    ax.text(x, y - 0.20, title, color=color, fontsize=8.5,
            ha='center', va='center', zorder=4)

# Legend for stages
legend_handles = [
    mpatches.Patch(color=GOLD,   label='Stage 1: Context'),
    mpatches.Patch(color=BLUE,   label='Stage 2: Architecture'),
    mpatches.Patch(color=ORANGE, label='Stage 3: Path'),
    mpatches.Patch(color=CYAN,   label='Stage 4: Details'),
    mpatches.Patch(color=PURPLE, label='Stage 5: Taxonomy'),
]
leg = ax.legend(handles=legend_handles, loc='lower left',
                bbox_to_anchor=(0.02, 0.02),
                facecolor=PAN, edgecolor=DIM,
                labelcolor=WHITE, fontsize=9)

# Notes
ax.text(15.5, 0.5,
        'Arrows: paper at\ntail informs paper\nat head',
        color=DIM, fontsize=9, ha='right', va='bottom', style='italic')

ax.set_title('Paper Dependency Graph: Which Papers Inform Which',
             color=GOLD, fontsize=15, fontweight='bold', y=0.97)

save(fig, 'reading_guide_02_dependency_dag.png')

# ================================================================
# FIG 3: STAGE-TO-PAPER MAPPING WITH DELIVERABLES
# Type: 4 (Geometric / labeled grid)
# Shows: five columns, papers grouped by stage, deliverables under
# each. The bulk of the document content visually.
# ================================================================

fig, ax = plt.subplots(figsize=(20, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 20)
ax.set_ylim(0, 11)
ax.axis('off')

# Five columns
col_centers = [2.0, 5.6, 9.2, 13.8, 18.0]
col_widths  = [2.8, 2.8, 2.8, 5.0, 2.8]

stage_info = [
    (1, 'Stage 1', 'Context',          GOLD,
     ['INFRA-7'], 0),
    (2, 'Stage 2', 'Architecture',     BLUE,
     ['INFRA-2'], 1),
    (3, 'Stage 3', 'Path',             ORANGE,
     ['INFRA-9'], 2),
    (4, 'Stage 4', 'Details',          CYAN,
     ['INFRA-3', 'INFRA-4', 'INFRA-5', 'INFRA-6', 'INFRA-8'], 3),
    (5, 'Stage 5', 'Taxonomy',         PURPLE,
     ['INFRA-1'], 4),
]

# Deliverables by paper
deliverables = {
    'INFRA-7': [
        'Picture absorbable in one sitting',
        '10 capabilities orgs gain',
        '8 before/after walkthroughs',
        'Honest cost-benefit framing',
    ],
    'INFRA-2': [
        '10 architectural commitments',
        'Cardinality rule (1 or N, no 2)',
        'Comprehensive scope argument',
        'Three populations claim',
        'Construction discipline',
    ],
    'INFRA-9': [
        'Six-phase implementation path',
        'Per-phase decisions/deliverables',
        'DSNC list-of-N test',
        'Required roles',
        'Dev-to-operational cutover',
    ],
    'INFRA-3': [
        'Recurring structural patterns',
        'Unified substrate hierarchy',
        'Service abstraction graph',
        '~150 entity types',
    ],
    'INFRA-4': [
        'Get-act-set runner pattern',
        '11 runner kinds (open list)',
        'Three load-bearing disciplines',
        'Change-management gating',
        'GitOps integration example',
    ],
    'INFRA-5': [
        '10-step gate sequence',
        'Five-layer authorization',
        'change_set lifecycle',
        'Field-level versioning',
        'Runner report keys',
    ],
    'INFRA-6': [
        'Repository layout',
        'Closed constraint vocabulary',
        'Forbidden ops list',
        'Constraint/policy split',
        'Reconciliation discipline',
    ],
    'INFRA-8': [
        'Library/runner boundary',
        'Contract not implementation',
        'World-side substrate libs',
        'Two-sided policy enforcement',
    ],
    'INFRA-1': [
        'Three-axis vocabulary',
        '~60 mechanisms',
        '21 properties',
        '22 principles',
        'Diagnostic appendices',
    ],
}

# Header for stages (top row)
for stage, label, name, color, papers, col_idx in stage_info:
    cx = col_centers[col_idx]
    # Stage header box
    header_box = FancyBboxPatch((cx - col_widths[col_idx]/2, 9.7),
                                  col_widths[col_idx], 0.9,
                                  boxstyle='round,pad=0.05', facecolor=PAN,
                                  edgecolor=color, linewidth=2)
    ax.add_patch(header_box)
    ax.text(cx, 10.32, label, color=color, fontsize=12,
            ha='center', va='center', fontweight='bold')
    ax.text(cx, 9.92, name, color=WHITE, fontsize=10,
            ha='center', va='center')

# Reading order arrows between stage headers
for i in range(4):
    sx = col_centers[i] + col_widths[i]/2 + 0.05
    dx = col_centers[i+1] - col_widths[i+1]/2 - 0.05
    arrow = FancyArrowPatch((sx, 10.15), (dx, 10.15),
                             arrowstyle='->', color=GOLD,
                             linewidth=1.5, mutation_scale=15)
    ax.add_patch(arrow)

# Papers and deliverables under each stage header
for stage, label, name, color, papers, col_idx in stage_info:
    cx = col_centers[col_idx]
    cw = col_widths[col_idx]

    # For details (col_idx=3) lay out 5 papers in a 5-row stack inside the wider column
    paper_top = 9.0
    if col_idx == 3:
        # 5 papers stacked vertically in wide column
        for i, paper_id in enumerate(papers):
            py = paper_top - i * 1.65
            # Paper title box
            box = FancyBboxPatch((cx - cw/2 + 0.15, py - 0.30),
                                  cw - 0.30, 0.55,
                                  boxstyle='round,pad=0.03', facecolor=BG,
                                  edgecolor=color, linewidth=1)
            ax.add_patch(box)
            ax.text(cx - cw/2 + 0.30, py, paper_id, color=color, fontsize=9.5,
                    ha='left', va='center', fontweight='bold')
            ax.text(cx - cw/2 + 1.40, py, paper_title[paper_id],
                    color=WHITE, fontsize=8.5, ha='left', va='center')

            # Deliverable list (compact)
            for j, d in enumerate(deliverables[paper_id]):
                ax.text(cx - cw/2 + 0.30, py - 0.45 - j * 0.20,
                        '- ' + d, color=SILVER, fontsize=7.5,
                        ha='left', va='center')
    else:
        # Single paper in this column
        paper_id = papers[0]
        # Paper title block
        box = FancyBboxPatch((cx - cw/2 + 0.15, 8.55),
                              cw - 0.30, 0.6,
                              boxstyle='round,pad=0.03', facecolor=BG,
                              edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(cx, 8.85, paper_id, color=color, fontsize=11,
                ha='center', va='center', fontweight='bold')

        # Deliverables
        dlist = deliverables[paper_id]
        start_y = 7.95
        for j, d in enumerate(dlist):
            ax.text(cx, start_y - j * 0.50, '- ' + d, color=SILVER,
                    fontsize=9, ha='center', va='center', wrap=True)

# Bottom note
ax.text(10, 0.3,
        'Reading order: Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5. '
        'Each stage delivers what the next requires.',
        color=GOLD, fontsize=10, ha='center', style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN,
                  edgecolor=GOLD, linewidth=1))

ax.set_title('Stage-to-Paper Mapping: What Each Paper Gives You',
             color=GOLD, fontsize=15, fontweight='bold', y=0.98)

save(fig, 'reading_guide_03_stage_mapping.png')

# ================================================================
# FIG 4: READING ORDER WITH SECTION POINTERS
# Type: 4 (Geometric / progression with section markers)
# Shows: nine papers in comprehension order with the specific
# section pointers the guide directs readers to. Makes the
# reference structure tangible.
# ================================================================

fig, ax = plt.subplots(figsize=(20, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 20)
ax.set_ylim(0, 11)
ax.axis('off')

# Comprehension order
comp_order = ['INFRA-7', 'INFRA-2', 'INFRA-9', 'INFRA-3', 'INFRA-4',
              'INFRA-5', 'INFRA-6', 'INFRA-8', 'INFRA-1']

# Section pointers per paper (from the guide)
sections = {
    'INFRA-7': ['§2 starting state', '§4 capabilities', '§4.10 compounding',
                '§5 walkthroughs', '§6 cost-benefit'],
    'INFRA-2': ['§4 commitments', '§5 cardinality', '§5.4 N reasons',
                '§5.6 not N', '§6.13 all-of-ops', '§7 populations',
                '§14 discipline'],
    'INFRA-9': ['§3 cardinality', '§4 schema', '§5 dev API',
                '§5.4-7 DSNC', '§6 libs', '§7 CM',
                '§8 phase 6', '§9 roles', '§10 cutover'],
    'INFRA-3': ['§6 substrate', '§7 services', '§21 boundaries',
                'patterns: DSNC, versioning, payloads'],
    'INFRA-4': ['§2 pattern', '§3 lifecycle', '§4 kinds',
                '§7 disciplines', '§8 gating', '§10 GitOps',
                '§11 contrasts'],
    'INFRA-5': ['§3.5 10-step gate', '§5 versioning', '§5.6 concurrency',
                '§6.2 5 layers', '§7.2 lifecycle', '§7.7 to-perform queue',
                '§8 report keys', '§9 audit'],
    'INFRA-6': ['§3 layout', '§4 directory.yaml', '§6 vocabulary',
                '§7 forbidden', '§8 constraints split', '§12 evolution',
                '§12.4 duplication', '§13 reconciliation'],
    'INFRA-8': ['§1.2 contracts', '§3 boundary', '§4 API client',
                '§5 world-side', '§6 resilience', '§7 observation',
                '§13 two-sided'],
    'INFRA-1': ['§2 three axes', '§4.5 orthogonality', '§5.7 opposed principles',
                '§7 honest sections', 'App F gap analysis',
                'App I confusables', 'App M reverse index'],
}

# Layout: 9 papers in a single row across the width
n_papers = len(comp_order)
margin = 0.5
total_w = 20 - 2 * margin
col_w = total_w / n_papers
paper_centers = [margin + col_w/2 + i * col_w for i in range(n_papers)]

# Draw papers
for i, paper_id in enumerate(comp_order):
    cx = paper_centers[i]
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]

    # Paper number indicator above
    ax.text(cx, 10.3, str(i + 1), color=GOLD, fontsize=14,
            ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='circle,pad=0.3', facecolor=BG,
                      edgecolor=GOLD, linewidth=1.5))

    # Paper id box
    pbox = FancyBboxPatch((cx - 0.85, 8.7), 1.7, 0.85,
                           boxstyle='round,pad=0.05', facecolor=PAN,
                           edgecolor=color, linewidth=2)
    ax.add_patch(pbox)
    ax.text(cx, 9.30, paper_id, color=WHITE, fontsize=9.5,
            ha='center', va='center', fontweight='bold')
    ax.text(cx, 8.92, paper_title[paper_id], color=color, fontsize=7.5,
            ha='center', va='center')

    # Section pointers below in a tall narrow box
    secs = sections[paper_id]
    n_secs = len(secs)
    sec_box_h = 0.35 + n_secs * 0.32
    sec_box_top = 8.50
    sec_box_bot = sec_box_top - sec_box_h

    sbox = FancyBboxPatch((cx - 0.95, sec_box_bot), 1.9, sec_box_h,
                           boxstyle='round,pad=0.03', facecolor=BG,
                           edgecolor=DIM, linewidth=0.8)
    ax.add_patch(sbox)

    for j, sec in enumerate(secs):
        sy = sec_box_top - 0.15 - j * 0.32
        ax.text(cx, sy, sec, color=SILVER, fontsize=7.0,
                ha='center', va='center')

# Reading-order arrows between papers
for i in range(n_papers - 1):
    sx = paper_centers[i] + 0.85
    dx = paper_centers[i+1] - 0.85
    arrow = FancyArrowPatch((sx, 9.12), (dx, 9.12),
                             arrowstyle='->', color=GOLD,
                             linewidth=1.2, mutation_scale=12, alpha=0.7)
    ax.add_patch(arrow)

# Bottom legend
ax.text(10, 0.4,
        'Numbers above = comprehension order. Boxes below each paper = section pointers in the reading guide.',
        color=DIM, fontsize=9, ha='center', style='italic')

ax.set_title('Reading Order with Section Pointers: Where the Guide Directs You Within Each Paper',
             color=GOLD, fontsize=14, fontweight='bold', y=0.98)

save(fig, 'reading_guide_04_section_pointers.png')

# ================================================================
# FIG 5: NUMBERED VS COMPREHENSION PARALLEL TRACKS
# Type: 6 (Comparison)
# Shows: two sequences side-by-side with crossover lines connecting
# the same paper in each. The visual makes "dependency order is not
# learning order" immediate.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

# Top track: numbered order
numbered_order = ['INFRA-1', 'INFRA-2', 'INFRA-3', 'INFRA-4', 'INFRA-5',
                  'INFRA-6', 'INFRA-7', 'INFRA-8', 'INFRA-9']
# Bottom track: comprehension order
comp_order = ['INFRA-7', 'INFRA-2', 'INFRA-9', 'INFRA-3', 'INFRA-4',
              'INFRA-5', 'INFRA-6', 'INFRA-8', 'INFRA-1']

n = 9
margin = 1.0
total_w = 18 - 2 * margin
col_w = total_w / n
top_centers = [margin + col_w/2 + i * col_w for i in range(n)]
bot_centers = [margin + col_w/2 + i * col_w for i in range(n)]

top_y = 7.8
bot_y = 2.8

# Track labels
ax.text(0.5, top_y, 'Numbered\norder',
        color=DIM, fontsize=10, ha='left', va='center', fontweight='bold')
ax.text(0.5, bot_y, 'Comprehension\norder',
        color=GOLD, fontsize=10, ha='left', va='center', fontweight='bold')

ax.text(9, 9.3, 'Numbered Order (the dependency order, for reference)',
        color=DIM, fontsize=11, ha='center', fontweight='bold')
ax.text(9, 1.2, 'Comprehension Order (the learning order, for the first read)',
        color=GOLD, fontsize=11, ha='center', fontweight='bold')

# Position lookup: where each paper sits on each track
top_pos = {p: top_centers[i] for i, p in enumerate(numbered_order)}
bot_pos = {p: bot_centers[i] for i, p in enumerate(comp_order)}

# Crossover lines (drawn first so nodes overlay)
for paper_id in numbered_order:
    sx = top_pos[paper_id]
    dx = bot_pos[paper_id]
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]
    ax.plot([sx, dx], [top_y - 0.5, bot_y + 0.5],
            color=color, linewidth=1.2, alpha=0.55)

# Top track nodes
for i, paper_id in enumerate(numbered_order):
    cx = top_centers[i]
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]
    box = FancyBboxPatch((cx - 0.7, top_y - 0.45), 1.4, 0.9,
                          boxstyle='round,pad=0.05', facecolor=PAN,
                          edgecolor=color, linewidth=1.5, zorder=3)
    ax.add_patch(box)
    ax.text(cx, top_y, paper_id, color=WHITE, fontsize=9,
            ha='center', va='center', fontweight='bold', zorder=4)

# Bottom track nodes with order numbers
for i, paper_id in enumerate(comp_order):
    cx = bot_centers[i]
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]
    box = FancyBboxPatch((cx - 0.7, bot_y - 0.45), 1.4, 0.9,
                          boxstyle='round,pad=0.05', facecolor=PAN,
                          edgecolor=color, linewidth=2, zorder=3)
    ax.add_patch(box)
    ax.text(cx, bot_y, paper_id, color=WHITE, fontsize=9,
            ha='center', va='center', fontweight='bold', zorder=4)
    # Order number above bottom node
    ax.text(cx, bot_y - 0.85, '#%d' % (i + 1),
            color=GOLD, fontsize=9, ha='center', va='center', fontweight='bold')

# Top track arrows (left-to-right)
for i in range(n - 1):
    sx = top_centers[i] + 0.7
    dx = top_centers[i+1] - 0.7
    arrow = FancyArrowPatch((sx, top_y), (dx, top_y),
                             arrowstyle='->', color=DIM,
                             linewidth=1.0, mutation_scale=10, alpha=0.6)
    ax.add_patch(arrow)

# Bottom track arrows (left-to-right)
for i in range(n - 1):
    sx = bot_centers[i] + 0.7
    dx = bot_centers[i+1] - 0.7
    arrow = FancyArrowPatch((sx, bot_y), (dx, bot_y),
                             arrowstyle='->', color=GOLD,
                             linewidth=1.5, mutation_scale=12)
    ax.add_patch(arrow)

# Center callout
ax.text(9, 5.3, 'The same nine papers, in two different sequences.\n'
                'Crossover lines show how each paper moves between orders.',
        color=WHITE, fontsize=11, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN,
                  edgecolor=GOLD, linewidth=1.2))

# Bottom note
ax.text(9, 0.4,
        'Numbered order is for reference. Comprehension order is for the first read.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.set_title('Two Orders, Same Papers: Why the First Read Is Not the Numbered Order',
             color=GOLD, fontsize=15, fontweight='bold', y=0.97)

save(fig, 'reading_guide_05_two_orders.png')

# ================================================================
# FIG 6: KNOWLEDGE STACK (CAPABILITY ACCUMULATION)
# Type: 4 (Geometric Cross-Section, vertical stack)
# Shows: capabilities accumulate as stages are completed. Each
# horizontal slab is a stage with what the reader can do after it.
# ================================================================

fig, ax = plt.subplots(figsize=(15, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.axis('off')

# Stack of capability slabs from bottom (Stage 1) to top (Stage 5)
slab_specs = [
    (1, 0.5,  GOLD,
     'After Stage 1 (INFRA-7)',
     ['Decide if your org should adopt the OpsDB',
      'Recognize the fragmentation pattern',
      'Speak in capabilities, not features']),
    (2, 2.7,  BLUE,
     'After Stage 2 (INFRA-2)',
     ['State the architectural commitments',
      'Defend the cardinality rule',
      'Recognize feature-creep antipatterns']),
    (3, 4.9,  ORANGE,
     'After Stage 3 (INFRA-9)',
     ['Plan the implementation phases',
      'Apply the validation criteria',
      'Identify required roles']),
    (4, 7.1,  CYAN,
     'After Stage 4 (INFRA-3, 4, 5, 6, 8)',
     ['Read the schema as data',
      'Design runners that compose',
      'Walk the 10-step gate sequence',
      'Govern schema evolution']),
    (5, 9.3,  PURPLE,
     'After Stage 5 (INFRA-1)',
     ['Use precise mechanism vocabulary',
      'Distinguish properties from claims',
      'Diagnose principle violations']),
]

slab_h = 1.9
slab_x = 0.5
slab_w = 14.0

for stage, y_bot, color, title, caps in slab_specs:
    box = FancyBboxPatch((slab_x, y_bot), slab_w, slab_h,
                          boxstyle='round,pad=0.05', facecolor=PAN,
                          edgecolor=color, linewidth=2, alpha=0.95)
    ax.add_patch(box)

    # Stage label on the left
    ax.text(slab_x + 0.35, y_bot + slab_h - 0.4, title,
            color=color, fontsize=12, ha='left', va='center', fontweight='bold')

    # Capabilities listed horizontally? Better: vertical with offsets
    n_caps = len(caps)
    # Lay out in two columns to use horizontal space without overlapping
    col1_caps = caps[:(n_caps + 1) // 2]
    col2_caps = caps[(n_caps + 1) // 2:]

    cap_top = y_bot + slab_h - 0.8
    for i, cap in enumerate(col1_caps):
        ax.text(slab_x + 0.55, cap_top - i * 0.35,
                '> ' + cap, color=WHITE, fontsize=9.5, ha='left', va='center')
    for i, cap in enumerate(col2_caps):
        ax.text(slab_x + slab_w/2 + 0.5, cap_top - i * 0.35,
                '> ' + cap, color=WHITE, fontsize=9.5, ha='left', va='center')

# Upward arrow on the right showing accumulation
ax.annotate('',
            xy=(slab_x + slab_w + 0.2, 11.0),
            xytext=(slab_x + slab_w + 0.2, 0.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.text(slab_x + slab_w + 0.5, 5.7, 'Capabilities\naccumulate',
        color=GOLD, fontsize=11, ha='left', va='center',
        fontweight='bold', rotation=90)

# Bottom note
ax.text(7.5, 11.65,
        'Each stage adds capabilities. Earlier capabilities remain; nothing is unlearned.',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.set_title('Knowledge Stack: What You Can Do After Each Stage',
             color=GOLD, fontsize=15, fontweight='bold', y=0.99)

save(fig, 'reading_guide_06_knowledge_stack.png')

# ================================================================
# FIG 7: NUMBERED-ORDER PITFALL MAP
# Type: 3 (Threshold/Region)
# Shows: what goes wrong if you start in numbered order. Three
# zones marking the failure modes when the wrong paper is read first.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM, labelsize=9)

# X-axis: papers in numbered order, 1-9
# Y-axis: comprehension achievable when starting here
papers_x = list(range(1, 10))
papers_labels = ['1\nTaxonomy', '2\nDesign', '3\nSchema', '4\nRunners',
                 '5\nAPI', '6\nSchema\nConstr.', '7\nIntro',
                 '8\nLibrary', '9\nImpl.\nPath']

# Comprehension-achievable score when starting at each paper
# Rough conceptual scoring based on the guide's pitfall callouts
comp_score = [0.10, 0.35, 0.15, 0.20, 0.25, 0.30, 0.95, 0.30, 0.55]

# Zones
ax.axhspan(0.7, 1.05, alpha=0.10, color=GREEN)    # Good zone
ax.axhspan(0.3, 0.7, alpha=0.08, color=ORANGE)    # Confusing zone
ax.axhspan(0,   0.3, alpha=0.10, color=RED)        # Bad zone

# Zone labels at right edge
ax.text(9.6, 0.87, 'Good first\nread', color=GREEN, fontsize=10,
        ha='left', va='center', fontweight='bold')
ax.text(9.6, 0.50, 'Confusing\nfirst read', color=ORANGE, fontsize=10,
        ha='left', va='center', fontweight='bold')
ax.text(9.6, 0.15, 'Bad first\nread', color=RED, fontsize=10,
        ha='left', va='center', fontweight='bold')

# Bars showing comprehension score per starting paper
bar_colors = []
for s in comp_score:
    if s >= 0.7:
        bar_colors.append(GREEN)
    elif s >= 0.3:
        bar_colors.append(ORANGE)
    else:
        bar_colors.append(RED)

bars = ax.bar(papers_x, comp_score, color=bar_colors, alpha=0.75,
              edgecolor=WHITE, linewidth=1.5, width=0.7)

# Pitfall callouts (offset to alternate above and below to avoid overlap)
pitfalls = {
    1: ('Vocabulary without\ncontext to use it', -0.18),
    2: ('Commitments without\nseeing what they produce', 0.10),
    3: ('150 entities without\nframe for why', 0.06),
    4: ('Runners without\nsubstrate context', 0.08),
    5: ('10-step gate without\nknowing what is gated', 0.10),
    6: ('Schema discipline without\nseeing the schema', 0.13),
    7: ('Just right - introduces\nthe whole architecture', -0.20),
    8: ('Library framework without\nrunners or substrate', 0.13),
    9: ('Implementation without\nknowing what to build', 0.18),
}

for x, (txt, dy) in pitfalls.items():
    bar_top = comp_score[x - 1]
    label_y = bar_top + dy
    color = GREEN if x == 7 else (RED if comp_score[x-1] < 0.3 else ORANGE)

    # Make sure label stays inside axis (clamp)
    if label_y > 0.95:
        label_y = 0.92
    if label_y < 0.04:
        label_y = 0.04

    ax.text(x, label_y, txt, color=color, fontsize=8.5,
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.25', facecolor=BG,
                      edgecolor=color, linewidth=0.8))

ax.set_xticks(papers_x)
ax.set_xticklabels(papers_labels, color=SILVER, fontsize=9)
ax.set_xlim(0.3, 11.0)
ax.set_ylim(0, 1.05)
ax.set_xlabel('"What if I start with this paper?"', color=SILVER, fontsize=12)
ax.set_ylabel('Comprehension achievable from this starting point',
              color=SILVER, fontsize=12)
ax.set_title('The Numbered-Order Pitfall: Why Starting at INFRA-1 Fails',
             color=GOLD, fontsize=15, fontweight='bold', pad=18)

ax.text(5, -0.13,
        'Only INFRA-7 is a viable first read. Every other entry point produces a partial picture.',
        color=DIM, fontsize=9, ha='center', style='italic',
        transform=ax.transData)

save(fig, 'reading_guide_07_pitfall_map.png')

# ================================================================
# FIG 8: FIRST-READ VS REFERENCE-READ SPLIT
# Type: 6 (Comparison)
# Shows: two access patterns. Linear comprehension on top; targeted
# reference jumps on bottom. The guide's two use cases visualized.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

# Top half: linear first-read path
ax.text(9, 9.5, 'FIRST READ: Linear Comprehension Path',
        color=GOLD, fontsize=13, ha='center', fontweight='bold')
ax.text(9, 9.0, '(Read every paper, in this order, to build the picture)',
        color=SILVER, fontsize=10, ha='center', style='italic')

# Linear sequence in top half
comp_order = ['INFRA-7', 'INFRA-2', 'INFRA-9', 'INFRA-3', 'INFRA-4',
              'INFRA-5', 'INFRA-6', 'INFRA-8', 'INFRA-1']

top_y = 7.8
n = 9
margin = 1.0
total_w = 18 - 2 * margin
col_w = total_w / n
centers = [margin + col_w/2 + i * col_w for i in range(n)]

for i, paper_id in enumerate(comp_order):
    cx = centers[i]
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]
    box = FancyBboxPatch((cx - 0.75, top_y - 0.45), 1.5, 0.9,
                          boxstyle='round,pad=0.05', facecolor=PAN,
                          edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(cx, top_y, paper_id, color=WHITE, fontsize=9,
            ha='center', va='center', fontweight='bold')

# Linear arrows
for i in range(n - 1):
    sx = centers[i] + 0.75
    dx = centers[i+1] - 0.75
    arrow = FancyArrowPatch((sx, top_y), (dx, top_y),
                             arrowstyle='->', color=GOLD,
                             linewidth=1.5, mutation_scale=12)
    ax.add_patch(arrow)

# Divider
ax.axhline(5.0, color=DIM, linewidth=0.8, linestyle='--', alpha=0.6)

# Bottom half: reference-read pattern
ax.text(9, 4.5, 'REFERENCE READ: Targeted Jumps by Phase or Concern',
        color=CYAN, fontsize=13, ha='center', fontweight='bold')
ax.text(9, 4.0, '(Already understand the architecture; jump to specific sections as needed)',
        color=SILVER, fontsize=10, ha='center', style='italic')

# Reference scenarios shown as starting points jumping into specific papers
scenarios = [
    ('Phase 1 work',         (1.5, 2.5),  ['INFRA-2 §5', 'INFRA-9 §3']),
    ('Phase 2 work',         (5.0, 2.5),  ['INFRA-3', 'INFRA-6']),
    ('Phase 4 work',         (8.5, 2.5),  ['INFRA-8 §15.1']),
    ('Phase 6 runner build', (12.0, 2.5), ['INFRA-4 §4', 'INFRA-8 §5']),
    ('Schema evolution',     (15.5, 2.5), ['INFRA-6 §12']),
]

# Bottom row papers (reference targets)
ref_papers_y = 0.8
ref_papers = ['INFRA-2', 'INFRA-3', 'INFRA-4', 'INFRA-5', 'INFRA-6',
              'INFRA-8', 'INFRA-9']
ref_n = len(ref_papers)
ref_centers = [1.5 + i * (15 / (ref_n - 1)) for i in range(ref_n)]

for i, paper_id in enumerate(ref_papers):
    cx = ref_centers[i]
    stage = paper_stage[paper_id]
    color = STAGE_COLORS[stage]
    box = FancyBboxPatch((cx - 0.65, ref_papers_y - 0.30), 1.3, 0.6,
                          boxstyle='round,pad=0.04', facecolor=PAN,
                          edgecolor=color, linewidth=1.2)
    ax.add_patch(box)
    ax.text(cx, ref_papers_y, paper_id, color=WHITE, fontsize=8.5,
            ha='center', va='center', fontweight='bold')

# Scenario boxes with arrows to their targets
ref_pos = {p: ref_centers[i] for i, p in enumerate(ref_papers)}

for label, (sx, sy), targets in scenarios:
    # Scenario box
    box = FancyBboxPatch((sx - 1.1, sy - 0.35), 2.2, 0.7,
                          boxstyle='round,pad=0.04', facecolor=BG,
                          edgecolor=CYAN, linewidth=1.2)
    ax.add_patch(box)
    ax.text(sx, sy, label, color=CYAN, fontsize=9,
            ha='center', va='center', fontweight='bold')

    # Arrows from scenario to each target
    for t in targets:
        # Extract paper id from "INFRA-X" or "INFRA-X §Y"
        paper_id = t.split(' ')[0]
        if paper_id in ref_pos:
            tx = ref_pos[paper_id]
            arrow = FancyArrowPatch((sx, sy - 0.35), (tx, ref_papers_y + 0.30),
                                     arrowstyle='->', color=CYAN,
                                     linewidth=0.9, alpha=0.5,
                                     mutation_scale=10,
                                     connectionstyle='arc3,rad=0.05')
            ax.add_patch(arrow)

# Bottom margin note
ax.text(9, 0.05,
        'The first read builds the picture; reference reads exploit it. Both use the same nine papers.',
        color=DIM, fontsize=9, ha='center', style='italic')

ax.set_title('Two Access Patterns: Linear First Read vs Targeted Reference Jumps',
             color=GOLD, fontsize=15, fontweight='bold', y=0.97)

save(fig, 'reading_guide_08_first_vs_reference.png')

# ================================================================
# SUMMARY
# ================================================================

print("\nReading guide diagram script complete. 8 figures generated:")
print("  1. reading_guide_01_five_stage_onion.png       - Five-stage onion (nested layers)")
print("  2. reading_guide_02_dependency_dag.png         - Paper dependency DAG")
print("  3. reading_guide_03_stage_mapping.png          - Stage-to-paper mapping with deliverables")
print("  4. reading_guide_04_section_pointers.png       - Reading order with section pointers")
print("  5. reading_guide_05_two_orders.png             - Numbered vs comprehension parallel tracks")
print("  6. reading_guide_06_knowledge_stack.png        - Knowledge stack (capability accumulation)")
print("  7. reading_guide_07_pitfall_map.png            - Numbered-order pitfall map")
print("  8. reading_guide_08_first_vs_reference.png     - First-read vs reference-read split")
