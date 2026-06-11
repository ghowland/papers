#!/usr/bin/env python3
"""
HOWL INFO-14 Diagrams — Bits and Ops: A Complete Theory of Information
8 figures covering dissolution curves, four states, cascade independence,
validity envelopes, budget consumption, three-term cost, Shannon scope,
and contention graph motifs.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Color palette ──

# ── Global palette (D7.2) ──
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

def style_ax(ax, xlabel='', ylabel='', title=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=18)


# ================================================================
# FIG 1: DISSOLUTION CURVES ACROSS DOMAINS
# Type: Running/Convergence (Type 1)
# Shows: Universal dissolution shape with domain-specific rates;
#        curves converge to same zero despite different starting
#        points and rates. Shape IS the finding.
# ================================================================

fig1, ax1 = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax1, xlabel='Repetitions (practice cycles)', ylabel='Processing Entropy (ops)',
         title='Dissolution Curves Across Domains')

n = np.linspace(1, 500, 500)

domains = [
    ('Medicine: Diagnosis',     55, 6,  0.008, MAG,   'o'),
    ('Driving: Mirror Check',   6,  1,  0.035, GREEN, 's'),
    ('Software: Bug Pattern',   30, 5,  0.012, CYAN,  '^'),
    ('Aviation: Threat Class.', 25, 4,  0.015, ORANGE,'D'),
    ('Cooking: Knife Technique', 18, 5, 0.020, PURPLE,'v'),
    ('Computation: Cache',       1,  0, 0.500, BLUE,  'p'),
]

for label, c0, rstar, lam, color, marker in domains:
    # Power-law dissolution: C0 * n^(-b) + R*  approaching 0
    # Use shifted power law that approaches zero
    b = lam * 30  # convert rate to power law exponent
    curve = c0 * np.power(n, -b)
    curve = np.maximum(curve, 0)
    ax1.plot(n, curve, color=color, linewidth=2.2, label=label, alpha=0.9)
    # Mark R* floor with a subtle dashed line segment
    if rstar > 0:
        ax1.axhline(y=rstar, color=color, linewidth=0.8, linestyle=':', alpha=0.3,
                     xmin=0.0, xmax=0.95)

# R* annotation region
ax1.fill_between([0, 500], 0, 1.5, color=GREEN, alpha=0.04)
ax1.text(400, 0.8, 'Dissolved (Zero-absent)\nHp = 0', color=GREEN, fontsize=9,
         ha='center', va='center', fontstyle='italic', alpha=0.7)

# R* bracket annotation
ax1.annotate('R* floors\n(domain-specific)', xy=(480, 5), xytext=(420, 18),
             color=SILVER, fontsize=9, ha='center',
             arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.0, alpha=0.5))

ax1.set_xlim(0, 520)
ax1.set_ylim(-1, 62)
ax1.legend(loc='upper right', fontsize=9, facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE, framealpha=0.9)

# Key insight annotation
ax1.text(260, 56, 'All curves converge toward zero — dissolution is universal',
         color=GOLD, fontsize=10, ha='center', fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.8))

save(fig1, 'info14_01_dissolution_curves.png')


# ================================================================
# FIG 2: FOUR-STATE TRANSITION DIAGRAM
# Type: Geometric Cross-Section (Type 4)
# Shows: Spatial relationships between states; allowed and
#        forbidden transitions; cascade regression path.
# ================================================================

fig2, ax2 = plt.subplots(figsize=(18, 12), facecolor=BG)
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(-1.5, 11.5)
ax2.set_ylim(-1.5, 9.5)

# State positions — generous spacing
states = {
    'inf':  (2.0, 7.0, 'INFINITY', 'Population\nawaiting reduction',
             'Hp > 0', PURPLE, 1.3),
    'one':  (8.0, 7.0, 'ONE', 'Under active\noperation',
             'Hp > 0\n(consuming)', CYAN, 1.3),
    'za':   (8.0, 2.0, 'ZERO-ABSENT', 'Dissolved into\nstructure',
             'Hp = 0', GREEN, 1.3),
    'ze':   (2.0, 2.0, 'ZERO-EXTERNAL', 'Permanently\noutside domain',
             'Hp undefined', RED, 1.3),
}

for key, (x, y, name, desc, hp, color, r) in states.items():
    circle = plt.Circle((x, y), r, facecolor=BG, edgecolor=color,
                         linewidth=2.5, alpha=0.9, zorder=2)
    ax2.add_patch(circle)
    ax2.text(x, y + 0.35, name, color=color, fontsize=13, fontweight='bold',
             ha='center', va='center', zorder=3)
    ax2.text(x, y - 0.15, desc, color=SILVER, fontsize=8.5,
             ha='center', va='center', zorder=3)
    ax2.text(x, y - 0.75, hp, color=DIM, fontsize=8,
             ha='center', va='center', fontstyle='italic', zorder=3)

# Transition arrows
arrow_kw = dict(arrowstyle='->', mutation_scale=20, linewidth=2.0)

# Infinity -> One (Reduction)
ax2.annotate('', xy=(6.55, 7.0), xytext=(3.45, 7.0),
             arrowprops=dict(color=GOLD, **arrow_kw), zorder=4)
ax2.text(5.0, 7.75, 'REDUCTION', color=GOLD, fontsize=10, fontweight='bold',
         ha='center', va='center')
ax2.text(5.0, 7.2, 'enumerate \u2192 filter \u2192 score \u2192 select',
         color=SILVER, fontsize=7.5, ha='center', va='center')

# One -> Zero-absent (Dissolution)
ax2.annotate('', xy=(8.0, 3.45), xytext=(8.0, 5.55),
             arrowprops=dict(color=GREEN, **arrow_kw), zorder=4)
ax2.text(9.3, 4.5, 'DISSOLUTION', color=GREEN, fontsize=10, fontweight='bold',
         ha='center', va='center', rotation=90)
ax2.text(10.2, 4.5, 'repetition in\nconsistent context',
         color=SILVER, fontsize=7.5, ha='center', va='center')

# Zero-absent -> One (Cascade / regression)
ax2.annotate('', xy=(8.65, 5.75), xytext=(8.65, 3.25),
             arrowprops=dict(color=RED, linestyle='dashed', **arrow_kw), zorder=4)
ax2.text(6.5, 3.7, 'CASCADE', color=RED, fontsize=10, fontweight='bold',
         ha='center', va='center')
ax2.text(6.5, 3.3, 'context crosses\nvalidity envelope',
         color=SILVER, fontsize=7.5, ha='center', va='center')

# One -> Infinity (Release back)
ax2.annotate('', xy=(3.45, 7.55), xytext=(6.55, 7.55),
             arrowprops=dict(color=DIM, linestyle='dashed', **arrow_kw), zorder=4)
ax2.text(5.0, 8.15, 'RELEASE', color=DIM, fontsize=9,
         ha='center', va='center')

# Zero-external: no outbound transitions
ax2.text(2.0, 0.3, 'No forward transitions\npossible — permanent boundary',
         color=RED, fontsize=8, ha='center', va='center', fontstyle='italic',
         alpha=0.7)

# Zero-external -> system (one-way events)
ax2.annotate('', xy=(3.45, 2.55), xytext=(2.6, 3.15),
             arrowprops=dict(color=RED, linestyle='dotted',
                             arrowstyle='->', mutation_scale=15, linewidth=1.5,
                             alpha=0.5), zorder=4)
ax2.text(0.3, 3.6, 'Events flow IN\nfrom boundary\n(one-way only)',
         color=RED, fontsize=7.5, ha='center', va='center', alpha=0.7)

# Title
ax2.text(5.0, 9.0, 'The Four States of Information Processing',
         color=GOLD, fontsize=16, fontweight='bold', ha='center', va='center')

# Subtitle
ax2.text(5.0, 8.5, 'Every element occupies exactly one state relative to processor, goal, and context',
         color=SILVER, fontsize=9, ha='center', va='center', fontstyle='italic')

save(fig2, 'info14_02_four_states.png')


# ================================================================
# FIG 3: CASCADE SEVERITY VS TRIGGER MAGNITUDE
# Type: Threshold/Region (Type 3)
# Shows: Independence of severity from magnitude — the absence
#        of correlation IS the visual finding.
# ================================================================

fig3, ax3 = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax3, xlabel='Trigger Magnitude (event size)',
         ylabel='Cascade Severity (simultaneous promotions)',
         title='Cascade Severity Is Independent of Trigger Magnitude')

np.random.seed(42)
n_points = 30
magnitudes = np.random.uniform(0.5, 9.5, n_points)
severities = np.random.uniform(0.5, 14.5, n_points)

ax3.scatter(magnitudes, severities, s=180, c=CYAN, alpha=0.5, edgecolors=WHITE,
            linewidth=1.5, zorder=3)

# Key labeled examples
examples = [
    (0.8, 12.0, 'Bee in cockpit', RED,    (-60, 30)),
    (1.5, 8.0,  'Phone notification\nwhile driving', ORANGE, (-80, 30)),
    (8.5, 2.0,  'Thunderclap\nduring flight', GREEN, (-60, -35)),
    (7.0, 11.0, 'Team reorganization', MAG, (-70, 30)),
    (2.0, 13.5, 'CPU context\nswitch', BLUE, (55, -15)),
    (9.0, 9.0,  'Codebase\nrefactor', PURPLE, (-75, 30)),
    (3.0, 1.5,  'Loud noise in OR\n(one dissolution)', GREEN, (55, 15)),
]

for x, y, label, color, offset in examples:
    ax3.scatter([x], [y], s=280, c=color, edgecolors=WHITE, linewidth=2.0, zorder=5)
    ax3.annotate(label, xy=(x, y), xytext=(x + offset[0]/18.0, y + offset[1]/18.0),
                 color=color, fontsize=8.5, fontweight='bold', ha='center', va='center',
                 arrowprops=dict(arrowstyle='->', color=color, lw=1.2, alpha=0.7),
                 bbox=dict(boxstyle='round,pad=0.35', facecolor=BG, edgecolor=color, alpha=0.7))

# No-correlation line (flat regression to emphasize independence)
ax3.axhline(y=7.5, color=DIM, linewidth=1.0, linestyle='--', alpha=0.4)
ax3.text(5.0, 6.5, 'No correlation — severity depends on\nenvelope geometry, not event size',
         color=GOLD, fontsize=10, ha='center', va='center', fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.7))

# Region labels
ax3.text(1.5, 14.0, 'SMALL TRIGGER\nLARGE CASCADE', color=RED, fontsize=9,
         ha='center', va='center', fontweight='bold', alpha=0.6)
ax3.text(8.5, 1.0, 'LARGE TRIGGER\nSMALL CASCADE', color=GREEN, fontsize=9,
         ha='center', va='center', fontweight='bold', alpha=0.6)

ax3.set_xlim(-0.5, 10.5)
ax3.set_ylim(-0.5, 15.5)

save(fig3, 'info14_03_cascade_independence.png')


# ================================================================
# FIG 4: VALIDITY ENVELOPE GEOMETRY IN 2D CONTEXT SPACE
# Type: Threshold/Region (Type 3)
# Shows: Overlapping envelopes in context space; cliff formation
#        where boundaries align; impossible without 2D geometry.
# ================================================================

fig4, ax4 = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax4, xlabel='Turbulence Intensity (m/s)',
         ylabel='Visibility (meters)',
         title='Validity Envelopes in Context Space — Cliff Formation')

# Define envelopes as rectangles in turbulence x visibility space
# Pilot trained mostly in calm/clear conditions — narrow envelopes
envelopes = [
    ('Altitude maintenance',  0, 3.0, 3000, 10000, CYAN,   0.10),
    ('Heading hold',          0, 2.8, 2800,  9500, BLUE,   0.08),
    ('Attitude awareness',    0, 3.2, 3500, 10000, GREEN,  0.08),
    ('Instrument scan',       0, 5.0, 1000, 10000, PURPLE, 0.06),
    ('Radio communication',   0, 7.0, 500,  10000, ORANGE, 0.06),
    ('Engine monitoring',     0, 8.0, 0,    10000, DIM,    0.05),
]

for label, t_lo, t_hi, v_lo, v_hi, color, alpha in envelopes:
    rect = mpatches.FancyBboxPatch((t_lo, v_lo), t_hi - t_lo, v_hi - v_lo,
                                    boxstyle='round,pad=0.05',
                                    facecolor=color, edgecolor=color,
                                    alpha=alpha, linewidth=1.5, zorder=1)
    ax4.add_patch(rect)
    # Boundary line at the turbulence edge (right edge of envelope)
    ax4.plot([t_hi, t_hi], [v_lo, v_hi], color=color, linewidth=1.8,
             linestyle='--', alpha=0.5, zorder=2)

# Labels for envelopes — positioned outside to the right
label_data = [
    ('Altitude',      3.0, 8500, CYAN),
    ('Heading',       2.8, 7500, BLUE),
    ('Attitude',      3.2, 6200, GREEN),
    ('Instrument scan', 5.0, 4500, PURPLE),
    ('Radio comm.',   7.0, 2500, ORANGE),
    ('Engine mon.',   8.0, 1200, DIM),
]
for label, x, y, color in label_data:
    ax4.text(x + 0.3, y, label, color=color, fontsize=8.5, fontweight='bold',
             va='center', ha='left', alpha=0.8)

# CLIFF ZONE — where many envelopes end (around turbulence 2.8-3.2)
ax4.axvspan(2.7, 3.3, color=RED, alpha=0.08, zorder=0)
ax4.text(3.0, 500, 'CLIFF ZONE', color=RED, fontsize=11, fontweight='bold',
         ha='center', va='center', rotation=90, alpha=0.8)
ax4.text(3.0, 9800, '3 envelopes end here\n= cascade of 3 promotions',
         color=RED, fontsize=8.5, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.7))

# PLATEAU ZONE — where all envelopes overlap (low turbulence, high visibility)
ax4.text(1.0, 8000, 'PLATEAU\n(all dissolved,\nHp = 0)', color=GREEN, fontsize=10,
         ha='center', va='center', fontweight='bold', alpha=0.6)

# Current operating point
ax4.scatter([1.5], [6000], s=300, c=GOLD, edgecolors=WHITE, linewidth=2.5,
            zorder=10, marker='*')
ax4.text(1.5, 5200, 'Current\ncontext', color=GOLD, fontsize=9,
         ha='center', va='center', fontweight='bold')

# Context change arrow crossing the cliff
ax4.annotate('', xy=(3.5, 6000), xytext=(1.5, 6000),
             arrowprops=dict(arrowstyle='->', color=RED, lw=2.5,
                             linestyle='-'), zorder=10)
ax4.text(2.5, 6500, 'Context\nchange', color=RED, fontsize=9,
         ha='center', va='center', fontweight='bold')

ax4.set_xlim(-0.5, 10.0)
ax4.set_ylim(-500, 10800)

save(fig4, 'info14_04_validity_envelopes.png')


# ================================================================
# FIG 5: FUNDAMENTAL INEQUALITY — BUDGET CONSUMPTION
# Type: Running/Convergence (Type 1)
# Shows: Op accumulation against time budget ceiling; dissolved
#        elements contributing nothing; cascade spike.
# ================================================================

fig5, ax5 = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax5, xlabel='Time', ylabel='Cumulative Ops',
         title='The Fundamental Inequality: Ops vs Time Budget')

t = np.linspace(0, 100, 1000)

# Time budget ceiling
budget = 85
ax5.axhline(y=budget, color=RED, linewidth=2.5, linestyle='-', alpha=0.7, zorder=3)
ax5.text(95, budget + 3, 'TIME BUDGET (N/d\u0304)', color=RED, fontsize=11,
         fontweight='bold', ha='right', va='bottom')

# Novice accumulation — steep, hits budget
novice_ops = 1.2 * t
novice_ops = np.minimum(novice_ops, 95)
ax5.plot(t, novice_ops, color=MAG, linewidth=2.5, label='Novice (high Hp — nothing dissolved)',
         alpha=0.9)

# Expert accumulation — shallow, lots of budget headroom
# Flat zones represent dissolved elements (zero ops)
expert_base = np.zeros_like(t)
expert_rate = 0.3
for i in range(1, len(t)):
    # Occasionally flat (dissolved elements being "processed" at zero cost)
    if (i % 80 < 30) and t[i] < 65:
        expert_base[i] = expert_base[i-1]  # dissolved: no ops consumed
    else:
        expert_base[i] = expert_base[i-1] + expert_rate * (t[1] - t[0])

ax5.plot(t, expert_base, color=GREEN, linewidth=2.5,
         label='Expert (low Hp — most routine dissolved)', alpha=0.9)

# CASCADE EVENT at t=65 for expert
cascade_t_start = 65
cascade_idx = np.argmin(np.abs(t - cascade_t_start))
expert_cascade = expert_base.copy()
# Sudden spike: 25 ops added rapidly (cascade promotions)
spike_duration = 8
for i in range(cascade_idx, min(cascade_idx + int(spike_duration / (t[1]-t[0])), len(t))):
    expert_cascade[i] = expert_base[cascade_idx] + (i - cascade_idx) * 0.35
# Recovery: return to normal rate
for i in range(cascade_idx + int(spike_duration / (t[1]-t[0])), len(t)):
    prev = expert_cascade[i-1]
    if (i % 80 < 30):
        expert_cascade[i] = prev
    else:
        expert_cascade[i] = prev + expert_rate * (t[1] - t[0])

ax5.plot(t, expert_cascade, color=ORANGE, linewidth=2.0,
         label='Expert with cascade event', linestyle='--', alpha=0.8)

# Shade the cascade spike region
ax5.axvspan(cascade_t_start, cascade_t_start + spike_duration, color=RED, alpha=0.06)
ax5.annotate('CASCADE\nDissolved elements\npromote back to One',
             xy=(cascade_t_start + 2, expert_cascade[cascade_idx + 20]),
             xytext=(cascade_t_start + 18, expert_cascade[cascade_idx + 20] + 15),
             color=ORANGE, fontsize=9, fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.7))

# Label dissolved regions
ax5.annotate('Dissolved elements:\nzero ops consumed\n(flat segments)',
             xy=(20, expert_base[200]),
             xytext=(30, 40),
             color=GREEN, fontsize=9, ha='center',
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2, alpha=0.6),
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.6))

# Novice hits budget annotation
ax5.annotate('Novice exceeds budget\n= FAILURE',
             xy=(71, budget),
             xytext=(55, 75),
             color=RED, fontsize=9, fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.7))

# Free budget region for expert
mid_t = 90
mid_ops = expert_cascade[-50]
ax5.annotate('Free budget\n= capacity for\nnovel challenges',
             xy=(mid_t, (budget + mid_ops) / 2),
             xytext=(mid_t, (budget + mid_ops) / 2),
             color=GOLD, fontsize=9, ha='center', va='center',
             fontstyle='italic', alpha=0.8)

ax5.fill_between(t[800:], expert_cascade[800:], budget, color=GOLD, alpha=0.04)

ax5.set_xlim(-2, 105)
ax5.set_ylim(-3, 100)
ax5.legend(loc='upper left', fontsize=9, facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE, framealpha=0.9)

# Remove tick labels on x-axis (abstract time)
ax5.set_xticks([])

save(fig5, 'info14_05_budget_consumption.png')


# ================================================================
# FIG 6: THREE-TERM COST SCENARIOS
# Type: Comparison Bar (Type 6)
# Shows: Dominant term shifts across scenarios; Shannon sufficiency
#        visible as the case where endpoint bars vanish.
# ================================================================

fig6, ax6 = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax6, ylabel='Relative Cost (ops + bits)',
         title='The Three Costs of Communication — Who Pays?')

scenarios = [
    'Expert\n\u2192 Expert',
    'Expert\n\u2192 Novice',
    'Novice\n\u2192 Expert',
    'Novice\n\u2192 Novice',
    'Teacher\n\u2192 Student',
    'Machine\n\u2192 Machine',
]

# (sender_ops, channel_bits, receiver_ops)
costs = [
    (1,  10, 1),    # Expert -> Expert
    (1,  10, 80),   # Expert -> Novice
    (60, 10, 1),    # Novice -> Expert
    (60, 10, 80),   # Novice -> Novice
    (30, 25, 40),   # Teacher -> Student
    (1,  10, 1),    # Machine -> Machine
]

x_pos = np.arange(len(scenarios)) * 2.0  # generous spacing
bar_w = 0.45

for i, (label, (s, c, r)) in enumerate(zip(scenarios, costs)):
    x = x_pos[i]
    # Sender ops
    ax6.bar(x - bar_w - 0.05, s, bar_w, color=BLUE, alpha=0.75,
            edgecolor=BLUE, linewidth=1.5, zorder=3)
    # Channel bits
    ax6.bar(x, c, bar_w, color=DIM, alpha=0.75,
            edgecolor=DIM, linewidth=1.5, zorder=3)
    # Receiver ops
    ax6.bar(x + bar_w + 0.05, r, bar_w, color=MAG, alpha=0.75,
            edgecolor=MAG, linewidth=1.5, zorder=3)

    # Value labels on top of bars
    for val, xb, color in [(s, x - bar_w - 0.05, BLUE),
                            (c, x, SILVER),
                            (r, x + bar_w + 0.05, MAG)]:
        ax6.text(xb, val + 2, str(val), color=color, fontsize=9,
                 ha='center', va='bottom', fontweight='bold')

ax6.set_xticks(x_pos)
ax6.set_xticklabels(scenarios, color=WHITE, fontsize=10)
ax6.set_xlim(x_pos[0] - 1.5, x_pos[-1] + 1.5)
ax6.set_ylim(0, 100)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=BLUE, alpha=0.75, label='Sender Ops  Hp(A, encode)'),
    mpatches.Patch(facecolor=DIM, alpha=0.75, label='Channel Bits  Hs'),
    mpatches.Patch(facecolor=MAG, alpha=0.75, label='Receiver Ops  Hp(B, decode)'),
]
ax6.legend(handles=legend_elements, loc='upper right', fontsize=10,
           facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, framealpha=0.9)

# Shannon sufficiency annotations
ax6.annotate('Shannon sufficient\n(both endpoints \u2248 0)',
             xy=(x_pos[0], 15), xytext=(x_pos[0], 35),
             color=GOLD, fontsize=9, ha='center',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2),
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.7))

ax6.annotate('Shannon sufficient',
             xy=(x_pos[5], 15), xytext=(x_pos[5], 35),
             color=GOLD, fontsize=9, ha='center',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2),
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.7))

ax6.annotate('Receiver\ndominates',
             xy=(x_pos[1] + bar_w + 0.05, 80), xytext=(x_pos[1] - 0.2, 90),
             color=MAG, fontsize=9, ha='center', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=MAG, lw=1.2))

ax6.annotate('Sender\ndominates',
             xy=(x_pos[2] - bar_w - 0.10, 60), xytext=(x_pos[2] - 1.2, 90),
             color=BLUE, fontsize=9, ha='center', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.2))

save(fig6, 'info14_06_three_term_cost.png')


# ================================================================
# FIG 7: SHANNON SCOPE VS COMPLETE FRAMEWORK
# Type: Geometric Cross-Section (Type 4)
# Shows: Shannon's coverage as the middle third; endpoint territory
#        flanking; spatial scope visible as nested regions.
# ================================================================

fig7, ax7 = plt.subplots(figsize=(18, 10), facecolor=BG)
ax7.set_facecolor(BG)
ax7.axis('off')
ax7.set_xlim(-1, 21)
ax7.set_ylim(-2, 10)

# Three regions: Sender Processing | Shannon Channel | Receiver Processing
# Draw as three adjacent rounded rectangles

# Full framework background
full_bg = FancyBboxPatch((0.5, 1.0), 19.0, 6.5,
                          boxstyle='round,pad=0.3',
                          facecolor=PAN, edgecolor=GOLD,
                          linewidth=2.5, alpha=0.4, zorder=1)
ax7.add_patch(full_bg)

# Sender processing region
sender = FancyBboxPatch((1.0, 1.5), 5.0, 5.5,
                         boxstyle='round,pad=0.2',
                         facecolor=BLUE, edgecolor=BLUE,
                         linewidth=2.0, alpha=0.12, zorder=2)
ax7.add_patch(sender)
ax7.text(3.5, 6.0, 'SENDER', color=BLUE, fontsize=14, fontweight='bold',
         ha='center', va='center', zorder=3)
ax7.text(3.5, 5.2, 'PROCESSING', color=BLUE, fontsize=11,
         ha='center', va='center', zorder=3)
ax7.text(3.5, 4.0, 'Hp(A, encode)', color=WHITE, fontsize=12,
         ha='center', va='center', fontweight='bold', zorder=3)
ax7.text(3.5, 3.2, 'Measured in ops', color=SILVER, fontsize=9,
         ha='center', va='center', zorder=3)
ax7.text(3.5, 2.3, 'Dissolution state\nof sender determines\nencoding cost',
         color=DIM, fontsize=8, ha='center', va='center',
         fontstyle='italic', zorder=3)

# Shannon channel region
channel = FancyBboxPatch((7.0, 1.5), 6.0, 5.5,
                          boxstyle='round,pad=0.2',
                          facecolor=DIM, edgecolor=WHITE,
                          linewidth=2.5, alpha=0.12, zorder=2)
ax7.add_patch(channel)
ax7.text(10.0, 6.0, 'SHANNON', color=WHITE, fontsize=14, fontweight='bold',
         ha='center', va='center', zorder=3)
ax7.text(10.0, 5.2, 'CHANNEL', color=WHITE, fontsize=11,
         ha='center', va='center', zorder=3)
ax7.text(10.0, 4.0, 'Hs(channel)', color=WHITE, fontsize=12,
         ha='center', va='center', fontweight='bold', zorder=3)
ax7.text(10.0, 3.2, 'Measured in bits', color=SILVER, fontsize=9,
         ha='center', va='center', zorder=3)
ax7.text(10.0, 2.3, 'Fully formalized\nby Shannon (1948)\nReceiver-independent',
         color=DIM, fontsize=8, ha='center', va='center',
         fontstyle='italic', zorder=3)

# Receiver processing region
receiver = FancyBboxPatch((14.0, 1.5), 5.0, 5.5,
                           boxstyle='round,pad=0.2',
                           facecolor=MAG, edgecolor=MAG,
                           linewidth=2.0, alpha=0.12, zorder=2)
ax7.add_patch(receiver)
ax7.text(16.5, 6.0, 'RECEIVER', color=MAG, fontsize=14, fontweight='bold',
         ha='center', va='center', zorder=3)
ax7.text(16.5, 5.2, 'PROCESSING', color=MAG, fontsize=11,
         ha='center', va='center', zorder=3)
ax7.text(16.5, 4.0, 'Hp(B, decode)', color=WHITE, fontsize=12,
         ha='center', va='center', fontweight='bold', zorder=3)
ax7.text(16.5, 3.2, 'Measured in ops', color=SILVER, fontsize=9,
         ha='center', va='center', zorder=3)
ax7.text(16.5, 2.3, 'Dissolution state\nof receiver determines\ndecoding cost',
         color=DIM, fontsize=8, ha='center', va='center',
         fontstyle='italic', zorder=3)

# Flow arrows between regions
ax7.annotate('', xy=(6.8, 4.2), xytext=(6.2, 4.2),
             arrowprops=dict(arrowstyle='->', color=SILVER, lw=2.0), zorder=5)
ax7.annotate('', xy=(13.8, 4.2), xytext=(13.2, 4.2),
             arrowprops=dict(arrowstyle='->', color=SILVER, lw=2.0), zorder=5)

# Title
ax7.text(10.0, 9.0, 'Two Halves of One Subject',
         color=GOLD, fontsize=17, fontweight='bold', ha='center', va='center')

# Complete equation
ax7.text(10.0, 8.2,
         'Cost(A \u2192 B)  =  Hp(A, encode)  +  Hs(channel)  +  Hp(B, decode)',
         color=WHITE, fontsize=12, ha='center', va='center',
         fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                   linewidth=1.5, alpha=0.8))

# Scope labels
ax7.text(3.5, 0.5, 'This framework (2026)', color=BLUE, fontsize=9,
         ha='center', va='center', fontstyle='italic')
ax7.text(10.0, 0.5, 'Shannon (1948)', color=WHITE, fontsize=9,
         ha='center', va='center', fontstyle='italic')
ax7.text(16.5, 0.5, 'This framework (2026)', color=MAG, fontsize=9,
         ha='center', va='center', fontstyle='italic')

# "ops" and "bits" unit labels with emphasis
ax7.text(3.5, -0.3, 'OPS', color=BLUE, fontsize=16, fontweight='bold',
         ha='center', va='center', alpha=0.4)
ax7.text(10.0, -0.3, 'BITS', color=WHITE, fontsize=16, fontweight='bold',
         ha='center', va='center', alpha=0.4)
ax7.text(16.5, -0.3, 'OPS', color=MAG, fontsize=16, fontweight='bold',
         ha='center', va='center', alpha=0.4)

save(fig7, 'info14_07_shannon_scope.png')


# ================================================================
# FIG 8: CONTENTION GRAPH MOTIFS
# Type: Geometric Cross-Section (Type 4)
# Shows: Topological differences between star, chain, complete,
#        partitioned, hierarchical. Scaling law per motif.
# ================================================================

fig8, axes8 = plt.subplots(1, 5, figsize=(20, 8), facecolor=BG)

motifs = [
    ('Star', 'O(n/(1\u2212n\u00b7f\u00b7h))', 'Divergent'),
    ('Chain', 'O(n)', 'Linear +\npropagation'),
    ('Complete', 'O(n\u00b2)', 'Quadratic\n(maximum tax)'),
    ('Partitioned', 'O(k), k=group', 'Bounded by\ngroup size'),
    ('Hierarchical', 'O(log n)', 'Logarithmic\ncommon case'),
]

motif_colors = [RED, ORANGE, MAG, GREEN, CYAN]

for idx, (ax, (name, scaling, character), color) in enumerate(zip(axes8, motifs, motif_colors)):
    ax.set_facecolor(PAN)
    ax.axis('off')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.8, 3.5)

    # Title
    ax.text(0, 3.1, name, color=color, fontsize=13, fontweight='bold',
            ha='center', va='center')

    node_r = 0.22
    resource_r = 0.18

    if name == 'Star':
        # Central resource, streams around it
        center = plt.Circle((0, 0.5), resource_r + 0.05, facecolor=color, edgecolor=WHITE,
                             linewidth=1.5, alpha=0.6, zorder=3)
        ax.add_patch(center)
        ax.text(0, 0.5, 'R', color=WHITE, fontsize=9, fontweight='bold',
                ha='center', va='center', zorder=4)
        for i in range(6):
            angle = i * 60 * np.pi / 180
            sx = 1.5 * np.cos(angle)
            sy = 0.5 + 1.5 * np.sin(angle)
            s_circle = plt.Circle((sx, sy), node_r, facecolor=BG, edgecolor=SILVER,
                                   linewidth=1.2, zorder=3)
            ax.add_patch(s_circle)
            ax.plot([0, sx], [0.5, sy], color=DIM, linewidth=1.0, alpha=0.5, zorder=1)

    elif name == 'Chain':
        # Linear chain with shared resources between adjacent
        positions = [(-1.8, 0.5), (-0.9, 0.5), (0, 0.5), (0.9, 0.5), (1.8, 0.5)]
        for i, (x, y) in enumerate(positions):
            s_circle = plt.Circle((x, y), node_r, facecolor=BG, edgecolor=SILVER,
                                   linewidth=1.2, zorder=3)
            ax.add_patch(s_circle)
            if i < len(positions) - 1:
                mx = (x + positions[i+1][0]) / 2
                r_circle = plt.Circle((mx, y + 0.5), resource_r, facecolor=color,
                                       edgecolor=WHITE, linewidth=1.0, alpha=0.5, zorder=3)
                ax.add_patch(r_circle)
                ax.plot([x, mx], [y, y + 0.5], color=DIM, linewidth=0.8, alpha=0.4)
                ax.plot([positions[i+1][0], mx], [y, y + 0.5], color=DIM,
                        linewidth=0.8, alpha=0.4)

    elif name == 'Complete':
        # All connected to all
        angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
        pts = [(1.2 * np.cos(a), 0.5 + 1.2 * np.sin(a)) for a in angles]
        # Draw all edges first
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                ax.plot([pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]],
                        color=color, linewidth=0.7, alpha=0.25, zorder=1)
        for x, y in pts:
            s_circle = plt.Circle((x, y), node_r, facecolor=BG, edgecolor=SILVER,
                                   linewidth=1.2, zorder=3)
            ax.add_patch(s_circle)

    elif name == 'Partitioned':
        # Two groups
        for gx, gc in [(-1.0, CYAN), (1.0, GREEN)]:
            for gy in [-0.3, 0.5, 1.3]:
                s_circle = plt.Circle((gx, gy), node_r, facecolor=BG, edgecolor=gc,
                                       linewidth=1.2, zorder=3)
                ax.add_patch(s_circle)
            # Internal edges
            ax.plot([gx, gx], [-0.3, 0.5], color=gc, linewidth=0.8, alpha=0.3)
            ax.plot([gx, gx], [0.5, 1.3], color=gc, linewidth=0.8, alpha=0.3)
            # Group resource
            r_circle = plt.Circle((gx + 0.45, 0.5), resource_r, facecolor=gc,
                                   edgecolor=WHITE, linewidth=1.0, alpha=0.4, zorder=3)
            ax.add_patch(r_circle)
        # Dividing line
        ax.plot([0, 0], [-0.8, 1.8], color=DIM, linewidth=1.0, linestyle=':', alpha=0.5)
        ax.text(0, 2.2, 'no cross-group\nedges', color=DIM, fontsize=7,
                ha='center', va='center', fontstyle='italic')

    elif name == 'Hierarchical':
        # Tree: root, two middle, four leaves
        root = (0, 1.8)
        mid = [(-0.9, 0.7), (0.9, 0.7)]
        leaves = [(-1.5, -0.4), (-0.5, -0.4), (0.5, -0.4), (1.5, -0.4)]

        # Root resource (global)
        r_root = plt.Circle(root, resource_r + 0.03, facecolor=color, edgecolor=WHITE,
                             linewidth=1.5, alpha=0.6, zorder=3)
        ax.add_patch(r_root)
        ax.text(root[0], root[1], 'G', color=WHITE, fontsize=8, fontweight='bold',
                ha='center', va='center', zorder=4)

        for mx, my in mid:
            r_mid = plt.Circle((mx, my), resource_r, facecolor=color, edgecolor=WHITE,
                                linewidth=1.0, alpha=0.4, zorder=3)
            ax.add_patch(r_mid)
            ax.text(mx, my, 'L', color=WHITE, fontsize=7, ha='center', va='center', zorder=4)
            ax.plot([root[0], mx], [root[1], my], color=DIM, linewidth=0.8, alpha=0.4)

        for i, (lx, ly) in enumerate(leaves):
            s_circle = plt.Circle((lx, ly), node_r, facecolor=BG, edgecolor=SILVER,
                                   linewidth=1.2, zorder=3)
            ax.add_patch(s_circle)
            parent = mid[0] if i < 2 else mid[1]
            ax.plot([parent[0], lx], [parent[1], ly], color=DIM, linewidth=0.8, alpha=0.4)

    # Scaling law and character
    ax.text(0, -1.6, scaling, color=WHITE, fontsize=9, fontweight='bold',
            ha='center', va='center', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=BG, edgecolor=color,
                      linewidth=1.2, alpha=0.8))
    ax.text(0, -2.3, character, color=SILVER, fontsize=8,
            ha='center', va='center')

# Suptitle
fig8.suptitle('Contention Graph Motifs — Topology Determines Tax Scaling',
              color=GOLD, fontsize=16, fontweight='bold', y=0.98)

# Legend
fig8.text(0.5, 0.02,
          'Circles = processing streams     Colored nodes = shared resources     '
          'Lines = resource dependencies',
          color=SILVER, fontsize=9, ha='center', va='center', fontstyle='italic')

plt.subplots_adjust(wspace=0.35, top=0.88, bottom=0.10)

save(fig8, 'info14_08_contention_motifs.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n" + "="*60)
print("HOWL INFO-14 Diagrams Complete")
print("="*60)
filenames = [
    'info14_01_dissolution_curves.png',
    'info14_02_four_states.png',
    'info14_03_cascade_independence.png',
    'info14_04_validity_envelopes.png',
    'info14_05_budget_consumption.png',
    'info14_06_three_term_cost.png',
    'info14_07_shannon_scope.png',
    'info14_08_contention_motifs.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
print("="*60)
