#!/usr/bin/env python3
"""
cabibbo_doublet_diagrams.py
============================
Complete visual specification of the Cabibbo Doublet:
its quantum numbers, interactions, experimental tests,
the two-road convergence, the elimination cascade,
and its connections to the full HOWL series.

Uses exact values from phys24_lib.py.
Output: PNG files to ../figures/
"""

import sys
sys.path.insert(0, '.')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Wedge
import numpy as np
import os

from phys24_lib import *
from mpmath import log as mlog, pi as mpi

# Extract exact values at display boundary
gap_SM_f = float(f2m(gap_SM))       # 218/115 = 1.8957
gap_VL_f = float(f2m(gap_VL))       # 38/27 = 1.4074
gap_meas_f = float(f2m(gap_measured))  # 1.3582
alpha_f = float(f2m(alpha_frac))
R2_v = float(f2m(R2_f))
R4_v = float(f2m(R4_f))

OUT = "../figures"
os.makedirs(OUT, exist_ok=True)

BG = '#0d1117'
SPHERE = '#58a6ff'
TORUS = '#f0883e'
WEAK = '#8b949e'
TEXT = '#e6edf3'
ACCENT = '#7ee787'
RED = '#f85149'
PURPLE = '#d2a8ff'
YELLOW = '#ffcc00'
CYAN = '#79c0ff'
DARK = '#161b22'
PINK = '#ff9bce'


def make_fig(w, h):
    fig, ax = plt.subplots(1, 1, figsize=(w, h), facecolor=BG)
    ax.set_facecolor(BG)
    return fig, ax


def box(ax, x, y, w, h, title, lines, color, title_size=11):
    r = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25",
                        facecolor=DARK, edgecolor=color, linewidth=2)
    ax.add_patch(r)
    ax.text(x + w/2, y + h - 0.45, title, color=color,
            fontsize=title_size, ha='center', fontweight='bold')
    for i, line in enumerate(lines):
        ax.text(x + w/2, y + h - 1.1 - i * 0.45, line,
                color=TEXT, fontsize=8, ha='center')


# ================================================================
# FIGURE 1: THE IDENTITY CARD
# ================================================================

fig, ax = make_fig(16, 11)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.5, 11)
ax.axis('off')

ax.text(8, 10.3, 'THE CABIBBO DOUBLET',
        color=YELLOW, fontsize=24, ha='center', fontweight='bold')
ax.text(8, 9.6, 'Vector-Like Quark Doublet  (3, 2, 1/6)',
        color=TEXT, fontsize=13, ha='center')

# Central particle diagram: two components
# Upper component Q = +2/3
circ_u = Circle((6, 6.5), 1.0, fill=True, facecolor='#1a3a1a',
                edgecolor=ACCENT, linewidth=3)
ax.add_patch(circ_u)
ax.text(6, 6.8, 'U', color=ACCENT, fontsize=28, ha='center',
        fontweight='bold')
ax.text(6, 6.1, 'Q = +2/3', color=ACCENT, fontsize=10, ha='center')

# Lower component Q = -1/3
circ_d = Circle((10, 6.5), 1.0, fill=True, facecolor='#1a1a3a',
                edgecolor=SPHERE, linewidth=3)
ax.add_patch(circ_d)
ax.text(10, 6.8, 'D', color=SPHERE, fontsize=28, ha='center',
        fontweight='bold')
ax.text(10, 6.1, 'Q = -1/3', color=SPHERE, fontsize=10, ha='center')

# SU(2) doublet bracket
ax.plot([5.5, 5.5, 10.5, 10.5], [5.2, 4.9, 4.9, 5.2],
        color=TORUS, linewidth=2)
ax.text(8, 4.5, 'SU(2) DOUBLET', color=TORUS, fontsize=10,
        ha='center', fontweight='bold')

# Color lines (three colors per component)
for cx in [6, 10]:
    for i, (col, label) in enumerate(
            [(RED, 'r'), (ACCENT, 'g'), (SPHERE, 'b')]):
        angle = np.pi/2 + (i - 1) * 0.4
        dx = 1.3 * np.cos(angle)
        dy = 1.3 * np.sin(angle)
        ax.plot([cx, cx + dx], [6.5, 6.5 + dy], color=col,
                linewidth=1.5, alpha=0.5)
    ax.text(cx, 8.2, 'SU(3) triplet', color=WEAK, fontsize=7,
            ha='center')

# Properties table on left
props_left = [
    ('Hypercharge Y', '1/6'),
    ('Spin', '1/2 (fermion)'),
    ('Chirality', 'Vector-like (L = R)'),
    ('Bare mass', 'Allowed (no Higgs needed)'),
    ('Anomaly', 'Free by construction'),
    ('New fields', '4 Weyl spinors'),
]

ax.text(0.5, 8.5, 'PROPERTIES', color=YELLOW, fontsize=10,
        fontweight='bold')
for i, (prop, val) in enumerate(props_left):
    ax.text(0.5, 8.0 - i * 0.45, '%s:' % prop,
            color=WEAK, fontsize=7)
    ax.text(3.0, 8.0 - i * 0.45, val,
            color=TEXT, fontsize=7)

# Beta function contributions on right
ax.text(12.5, 8.5, 'BETA SHIFTS', color=YELLOW, fontsize=10,
        fontweight='bold')
betas = [
    (r'$\Delta b_1$ = 1/15', '0.0667', 'U(1) — small (Y=1/6)'),
    (r'$\Delta b_2$ = 1', '1.0000', 'SU(2) — LARGE'),
    (r'$\Delta b_3$ = 1/3', '0.3333', 'SU(3) — moderate'),
]
for i, (label, val, note) in enumerate(betas):
    ax.text(12.5, 7.8 - i * 0.55, label,
            color=ACCENT if i == 1 else TEXT, fontsize=9,
            fontweight='bold' if i == 1 else 'normal')
    ax.text(14.5, 7.8 - i * 0.55, note,
            color=WEAK, fontsize=7)

ax.text(12.5, 6.0, 'ASYMMETRY RATIO', color=YELLOW, fontsize=9,
        fontweight='bold')
ax.text(12.5, 5.5, r'$\Delta b_2 / \Delta b_1$ = 15',
        color=ACCENT, fontsize=12, fontweight='bold')
ax.text(12.5, 5.0, 'Highest of any candidate tested',
        color=WEAK, fontsize=7)

# Gap ratio result at bottom
gap_box = FancyBboxPatch((2, 1.0), 12, 2.5,
                          boxstyle="round,pad=0.3",
                          facecolor=DARK, edgecolor=ACCENT, linewidth=2.5)
ax.add_patch(gap_box)
ax.text(8, 3.0, 'GAP RATIO', color=ACCENT, fontsize=14,
        ha='center', fontweight='bold')
ax.text(8, 2.3,
        'SM: 218/115 = %.4f (40%% miss)     '
        'Cabibbo Doublet: 38/27 = %.4f (3.6%% miss)     '
        'Measured: %.4f' % (gap_SM_f, gap_VL_f, gap_meas_f),
        color=TEXT, fontsize=9, ha='center')
ax.text(8, 1.5,
        'One particle reduces the miss by a factor of 11',
        color=YELLOW, fontsize=10, ha='center', fontweight='bold')

fig.savefig(os.path.join(OUT, 'cabibbo_01_identity_card.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_01_identity_card.png")


# ================================================================
# FIGURE 2: THE TWO ROADS
# ================================================================

fig, ax = make_fig(16, 11)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.5, 11)
ax.axis('off')

ax.text(8, 10.3, 'TWO INDEPENDENT ROADS TO THE SAME PARTICLE',
        color=TEXT, fontsize=16, ha='center', fontweight='bold')

# Left road: Gap ratio (top-down)
box(ax, 0.3, 6.0, 6.5, 4.0,
    'GAP RATIO PATH (this series)',
    ['Start: 3 couplings at M_Z',
     'Compute: gap = 218/115 vs measured 1.358',
     'Enumerate: 15 candidates',
     'Eliminate: 13 by gap ratio, 1 by proton decay',
     'Survive: MSSM + Cabibbo Doublet',
     'Determines: representation (3,2,1/6)'],
    SPHERE, 10)

# Right road: Anomaly (bottom-up)
box(ax, 9.2, 6.0, 6.5, 4.0,
    'ANOMALY PATH (literature)',
    ['Start: 3 experimental anomalies',
     'CKM unitarity deficit: 2.5-4 sigma',
     'A_FB^b at LEP: ~3 sigma',
     'Higgs signal strength: ~2 sigma',
     'Fit: VL quark doublet resolves all 3',
     'Determines: mass 1.5-6 TeV, mixings'],
    TORUS, 10)

# Convergence arrow to central particle
ax.annotate('', xy=(8, 4.5), xytext=(3.5, 6.0),
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=3))
ax.annotate('', xy=(8, 4.5), xytext=(12.5, 6.0),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=3))

# Central: the particle
particle = Circle((8, 3.5), 1.2, fill=True, facecolor=DARK,
                   edgecolor=YELLOW, linewidth=3)
ax.add_patch(particle)
ax.text(8, 3.9, 'CABIBBO', color=YELLOW, fontsize=12,
        ha='center', fontweight='bold')
ax.text(8, 3.3, 'DOUBLET', color=YELLOW, fontsize=12,
        ha='center', fontweight='bold')
ax.text(8, 2.8, '(3,2,1/6)', color=TEXT, fontsize=9, ha='center')

# What each road determines
ax.text(2.5, 5.5, 'Gives: representation, M_GUT, proton decay',
        color=SPHERE, fontsize=8, ha='center')
ax.text(13.5, 5.5, 'Gives: mass, mixing angles, decay modes',
        color=TORUS, fontsize=8, ha='center')

# Bottom: combined specification
combined = FancyBboxPatch((2.5, 0.2), 11, 1.8,
                           boxstyle="round,pad=0.2",
                           facecolor=DARK, edgecolor=ACCENT,
                           linewidth=2)
ax.add_patch(combined)
ax.text(8, 1.6, 'COMBINED: representation + mass + mixing + M_GUT + tests',
        color=ACCENT, fontsize=10, ha='center', fontweight='bold')
ax.text(8, 0.9, 'Neither road alone gives the full picture. '
        'Together they fully specify the particle.',
        color=TEXT, fontsize=8, ha='center')

ax.annotate('', xy=(8, 2.0), xytext=(8, 2.3),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))

# Timeline
ax.text(0.5, 0.0, '2019-2020: Anomaly path (Belfatto, Cheung et al.)',
        color=WEAK, fontsize=7)
ax.text(9.0, 0.0, '2026: Gap ratio path (HOWL PHYS-13/15)',
        color=WEAK, fontsize=7)

fig.savefig(os.path.join(OUT, 'cabibbo_02_two_roads.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_02_two_roads.png")


# ================================================================
# FIGURE 3: THE ELIMINATION CASCADE
# ================================================================

fig, ax = make_fig(16, 10)
ax.set_facecolor(BG)

# All 15 candidates as horizontal bars (gap ratio)
candidates = [
    ('VL (3,1,2/3)', 2.229, RED),
    ('Scalar (8,1,0)', 2.180, RED),
    ('VL (3,1,-1/3)', 2.114, RED),
    ('Scalar (3,1,-1/3)', 2.000, RED),
    ('VL (1,1,-1)', 2.000, RED),
    ('SU(5) 10+10bar', 1.948, RED),
    ('Scalar (1,2,1/2)', 1.800, RED),
    ('VL (1,2,-1/2)', 1.712, RED),
    ('2x Scalar (1,2,1/2)', 1.712, RED),
    ('Scalar (1,3,0)', 1.664, RED),
    ('Scalar (3,2,1/6)', 1.632, RED),
    ('3x Scalar (1,2,1/2)', 1.631, RED),
    ('SU(5) 5+5bar', 1.481, PURPLE),
    ('CABIBBO DOUBLET', gap_VL_f, YELLOW),
    ('Full MSSM', 1.400, ACCENT),
]

y_positions = range(len(candidates))
for i, (name, gap, color) in enumerate(candidates):
    bar_width = gap - gap_meas_f
    ax.barh(i, bar_width, left=gap_meas_f, height=0.6,
            color=color, alpha=0.5 if color == RED else 0.8,
            edgecolor=color, linewidth=1)
    ax.text(gap + 0.02, i, '%.3f' % gap,
            color=color, fontsize=7, va='center')

ax.set_yticks(y_positions)
ax.set_yticklabels([c[0] for c in candidates], color=TEXT, fontsize=7)

# Measured line
ax.axvline(x=gap_meas_f, color=CYAN, linewidth=2.5, linestyle='-')
ax.text(gap_meas_f - 0.02, -1.5, 'Measured\n%.4f' % gap_meas_f,
        color=CYAN, fontsize=8, ha='center', fontweight='bold')

# Threshold window
ax.axvspan(gap_meas_f - 0.001, gap_meas_f + 0.15, alpha=0.08,
           color=ACCENT)
ax.text(gap_meas_f + 0.075, 15.5, 'Stage 1 window (0.15)',
        color=ACCENT, fontsize=8, ha='center')

# Stage labels
ax.text(2.0, 15.5, '12 ELIMINATED (gap ratio > 0.15)',
        color=RED, fontsize=9, fontweight='bold')
ax.text(1.55, 14.8, '1 ELIMINATED (proton decay)',
        color=PURPLE, fontsize=8)

ax.set_xlabel('Gap Ratio (dimensionless)', color=TEXT, fontsize=11)
ax.set_title('The Elimination Cascade: 15 Candidates to 2 Survivors',
             color=TEXT, fontsize=14, fontweight='bold', pad=12)
ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_xlim(1.3, 2.35)
ax.invert_yaxis()

fig.savefig(os.path.join(OUT, 'cabibbo_03_elimination_cascade.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_03_elimination_cascade.png")


# ================================================================
# FIGURE 4: THE THREE ANOMALIES
# ================================================================

fig, ax = make_fig(16, 9)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.5, 9.5)
ax.axis('off')

ax.text(8, 9.0, 'THREE EXPERIMENTAL ANOMALIES RESOLVED BY ONE PARTICLE',
        color=TEXT, fontsize=14, ha='center', fontweight='bold')

# Anomaly 1: CKM
box(ax, 0.3, 4.5, 5.0, 4.0,
    'CKM UNITARITY',
    ['|V_ud|^2+|V_us|^2+|V_ub|^2',
     '= 0.99798 +/- 0.00038',
     'Deficit: 0.00202 (2.5-4 sigma)',
     '',
     'FIX: 4th column absorbs deficit',
     '|V_ub\'| ~ 0.045'],
    RED, 10)

# Anomaly 2: A_FB^b
box(ax, 5.8, 4.5, 5.0, 4.0,
    'A_FB^b AT LEP',
    ['Measured: 0.0992 +/- 0.0016',
     'SM pred:  ~0.1038',
     'Deficit: ~3 sigma',
     'Persistent 25+ years',
     'FIX: VL-b mixing shifts g_bR',
     'Modifies Z-b-b vertex'],
    TORUS, 10)

# Anomaly 3: Higgs mu
box(ax, 11.3, 4.5, 5.0, 4.0,
    'HIGGS SIGNAL',
    ['Measured mu: 1.06-1.10',
     'SM pred: 1.00',
     'Excess: ~2 sigma',
     'Weakest anomaly',
     'FIX: gg->H loop enhanced',
     'Bottom Yukawa reduced'],
    PURPLE, 10)

# Central: the particle resolves all three
particle = Circle((8, 2.5), 1.2, fill=True, facecolor=DARK,
                   edgecolor=YELLOW, linewidth=3)
ax.add_patch(particle)
ax.text(8, 2.8, 'CABIBBO', color=YELLOW, fontsize=11,
        ha='center', fontweight='bold')
ax.text(8, 2.2, 'DOUBLET', color=YELLOW, fontsize=11,
        ha='center', fontweight='bold')

# Arrows from anomalies to particle
ax.annotate('', xy=(7.0, 3.0), xytext=(2.8, 4.5),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5))
ax.annotate('', xy=(8.0, 3.7), xytext=(8.3, 4.5),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=2.5))
ax.annotate('', xy=(9.0, 3.0), xytext=(13.8, 4.5),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2.5))

# Bottom: references
ax.text(8, 0.8, 'Belfatto, Berezhiani (2020): CKM deficit as VL signal',
        color=RED, fontsize=7, ha='center')
ax.text(8, 0.4, 'Cheung, Keung, Lu, Tseng (2020): three-anomaly simultaneous fit',
        color=TORUS, fontsize=7, ha='center')
ax.text(8, 0.0, 'Kitahara (2024): "prime candidate is the VL quark extension"',
        color=PURPLE, fontsize=7, ha='center')

fig.savefig(os.path.join(OUT, 'cabibbo_04_three_anomalies.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_04_three_anomalies.png")


# ================================================================
# FIGURE 5: THE EXPERIMENTAL TEST MATRIX
# ================================================================

fig, ax = make_fig(16, 10)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.5, 10.5)
ax.axis('off')

ax.text(8, 10.0, 'EXPERIMENTAL TESTS: WHEN AND WHERE',
        color=TEXT, fontsize=16, ha='center', fontweight='bold')

# Timeline axis
ax.plot([1, 15], [5.5, 5.5], color=WEAK, linewidth=2)
decades = [(2, '2025'), (5, '2030'), (8, '2035'), (11, '2040')]
for x, label in decades:
    ax.plot([x, x], [5.3, 5.7], color=WEAK, linewidth=1.5)
    ax.text(x, 5.0, label, color=WEAK, fontsize=8, ha='center')

# Experiments above timeline
experiments_above = [
    (2.5, 7.5, 'HYPER-K', 'Proton decay\np->e+pi0',
     'tau ~ 10^34-35 yr', 2, 11, ACCENT),
    (6, 8.5, 'HL-LHC', 'VL quark pair\nproduction',
     'M < 2-3 TeV', 1.5, 8, YELLOW),
    (3, 9.5, 'BELLE II', 'CKM precision\nV_us, V_ub',
     'Sharpen anomaly', 1.5, 7, TORUS),
]

for x, y, name, what, detail, x1, x2, color in experiments_above:
    r = FancyBboxPatch((x - 0.1, y - 0.6), 3.5, 1.5,
                        boxstyle="round,pad=0.15",
                        facecolor=DARK, edgecolor=color, linewidth=1.5)
    ax.add_patch(r)
    ax.text(x + 1.6, y + 0.5, name, color=color, fontsize=10,
            ha='center', fontweight='bold')
    ax.text(x + 1.6, y - 0.0, what, color=TEXT, fontsize=7,
            ha='center')
    # Timeline bar
    ax.plot([x1, x2], [5.7, 5.7], color=color, linewidth=6, alpha=0.4,
            solid_capstyle='round')
    ax.annotate('', xy=((x1+x2)/2, 5.7), xytext=(x+1.6, y-0.6),
                arrowprops=dict(arrowstyle='->', color=color, lw=1,
                               linestyle='--', alpha=0.5))

# Experiments below timeline
experiments_below = [
    (1.5, 3.0, 'NA62/KOTO', 'K->pi nu nu\n(tree FCNC)', CYAN),
    (5.5, 3.0, 'LHCb', 'B_s mixing\nb->s transitions', SPHERE),
    (9.5, 3.0, 'DUNE', 'p->K+ nu_bar\n(SO(10) channel)', RED),
    (13, 3.0, 'NEUTRON', 'V_ud precision\nnEDM', PURPLE),
]

for x, y, name, what, color in experiments_below:
    r = FancyBboxPatch((x - 0.1, y - 0.6), 3.0, 1.2,
                        boxstyle="round,pad=0.1",
                        facecolor=DARK, edgecolor=color, linewidth=1)
    ax.add_patch(r)
    ax.text(x + 1.4, y + 0.2, name, color=color, fontsize=9,
            ha='center', fontweight='bold')
    ax.text(x + 1.4, y - 0.3, what, color=TEXT, fontsize=6,
            ha='center')

# The decision tree at bottom
ax.text(8, 1.5, 'DECISION:', color=YELLOW, fontsize=11,
        ha='center', fontweight='bold')
ax.text(8, 0.9,
        'Hyper-K sees proton decay at 10^34-35 yr  '
        '-->  Cabibbo Doublet CONFIRMED, MSSM ruled out',
        color=ACCENT, fontsize=8, ha='center')
ax.text(8, 0.4,
        'HL-LHC sees VL quark at 1.5-3 TeV  '
        '-->  DIRECT DISCOVERY',
        color=YELLOW, fontsize=8, ha='center')
ax.text(8, -0.1,
        'Hyper-K null + LHC null  '
        '-->  Minimal scenario excluded, non-minimal or MSSM survives',
        color=RED, fontsize=8, ha='center')

fig.savefig(os.path.join(OUT, 'cabibbo_05_experimental_tests.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_05_experimental_tests.png")


# ================================================================
# FIGURE 6: THE MASS-ENERGY LANDSCAPE
# ================================================================

fig, ax = make_fig(14, 10)
ax.set_facecolor(BG)

# Vertical energy axis (log scale)
energies = [
    (0.511e-3, r'$m_e$', WEAK, ''),
    (0.106, r'$m_\mu$', WEAK, ''),
    (1.777, r'$m_\tau$', WEAK, ''),
    (4.18, r'$m_b$', WEAK, ''),
    (80.4, r'$M_W$', SPHERE, 'EW transition'),
    (91.2, r'$M_Z$', SPHERE, ''),
    (125, r'$M_H$', SPHERE, ''),
    (172.6, r'$m_t$', SPHERE, ''),
    (2000, r'$M_{VL}$', YELLOW, 'CABIBBO DOUBLET'),
    (10**15.5, r'$M_{GUT}$', ACCENT, 'Unification'),
]

# Plot positions (log scale)
y_min, y_max = -4, 17
ax.set_ylim(y_min - 0.5, y_max + 0.5)
ax.set_xlim(0, 10)

# Energy axis
ax.plot([2, 2], [y_min, y_max], color=WEAK, linewidth=2)

for E, label, color, note in energies:
    y = np.log10(E * 1e-3)  # convert MeV to GeV for log scale
    if E < 1:
        y = np.log10(E)

    # Use manual positioning for clarity
    if E == 0.511e-3:
        y = -4
    elif E == 0.106:
        y = -1
    elif E == 1.777:
        y = 0.2
    elif E == 4.18:
        y = 0.6
    elif E == 80.4:
        y = 1.9
    elif E == 91.2:
        y = 2.0
    elif E == 125:
        y = 2.1
    elif E == 172.6:
        y = 2.25
    elif E == 2000:
        y = 3.3
    elif E == 10**15.5:
        y = 15.5

    ax.plot([1.8, 2.2], [y, y], color=color, linewidth=2)
    ax.text(2.5, y, label, color=color, fontsize=9, va='center')

    if note:
        ax.text(4.5, y, note, color=color, fontsize=8, va='center',
                fontweight='bold')

# Gap ratio labels on right
ax.text(7, -2, 'Gap = 218/115', color=RED, fontsize=10,
        fontweight='bold')
ax.text(7, -2.6, '(SM: 40%% miss)', color=RED, fontsize=8)

# Arrow showing "below M_VL"
ax.annotate('', xy=(6.5, -1), xytext=(6.5, 3.0),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))

ax.text(7, 6, 'Gap = 38/27', color=ACCENT, fontsize=10,
        fontweight='bold')
ax.text(7, 5.4, '(CD: 3.6%% miss)', color=ACCENT, fontsize=8)

# Arrow showing "above M_VL"
ax.annotate('', xy=(6.5, 3.6), xytext=(6.5, 15),
            arrowprops=dict(arrowstyle='<->', color=ACCENT, lw=2))

# The VL threshold highlighted
ax.axhspan(3.0, 3.6, xmin=0.1, xmax=0.9, alpha=0.1, color=YELLOW)
ax.text(5, 3.3, 'CABIBBO DOUBLET THRESHOLD (1.5-6 TeV)',
        color=YELLOW, fontsize=9, fontweight='bold')
ax.text(5, 2.8, 'First boundary that changes the gap ratio',
        color=YELLOW, fontsize=7)

# Y-axis label
ax.text(0.5, 8, r'log$_{10}$(E/GeV)', color=WEAK, fontsize=10,
        rotation=90, va='center')

ax.set_title('The Energy Landscape: Where the Cabibbo Doublet Sits',
             color=TEXT, fontsize=13, fontweight='bold', pad=12)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
for spine in ax.spines.values():
    spine.set_visible(False)

fig.savefig(os.path.join(OUT, 'cabibbo_06_energy_landscape.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_06_energy_landscape.png")


# ================================================================
# FIGURE 7: CONNECTIONS TO THE FULL SERIES
# ================================================================

fig, ax = make_fig(16, 12)
ax.set_xlim(-1, 17)
ax.set_ylim(-0.5, 12)
ax.axis('off')

ax.text(8, 11.3, 'THE CABIBBO DOUBLET IN THE HOWL SERIES',
        color=TEXT, fontsize=16, ha='center', fontweight='bold')

# Central particle
particle = Circle((8, 6), 1.3, fill=True, facecolor=DARK,
                   edgecolor=YELLOW, linewidth=3)
ax.add_patch(particle)
ax.text(8, 6.3, 'CABIBBO', color=YELLOW, fontsize=12,
        ha='center', fontweight='bold')
ax.text(8, 5.7, 'DOUBLET', color=YELLOW, fontsize=12,
        ha='center', fontweight='bold')

# Connected papers arranged around
connections = [
    (2, 10, 'PHYS-1', 'Mass is inertia:\nnew pattern at 1.5-6 TeV', SPHERE),
    (8, 10, 'PHYS-5/9', 'VP running:\nmodified above M_VL', SPHERE),
    (14, 10, 'PHYS-7', 'theta=0:\nextended quark mass matrix', SPHERE),
    (0.5, 6, 'PHYS-12', 'EW sector:\nR_b, A_FB corrections', TORUS),
    (15, 6, 'PHYS-13-15', 'Gap ratio:\n218/115 -> 38/27', ACCENT),
    (2, 2, 'PHYS-14', 'Fermion democracy:\nCD breaks the symmetry', TORUS),
    (8, 1.5, 'QED-GR SCANS', 'b2_mod = -13/6:\nLambda ~ alpha^(3x13)', RED),
    (14, 2, 'PHYS-11', 'Remainder:\ngap as Subgroup B test', PURPLE),
]

for x, y, paper, desc, color in connections:
    r = FancyBboxPatch((x - 1.5, y - 0.7), 3.0, 1.4,
                        boxstyle="round,pad=0.1",
                        facecolor=DARK, edgecolor=color, linewidth=1.5)
    ax.add_patch(r)
    ax.text(x, y + 0.3, paper, color=color, fontsize=8,
            ha='center', fontweight='bold')
    ax.text(x, y - 0.25, desc, color=TEXT, fontsize=6,
            ha='center', linespacing=1.3)
    ax.annotate('', xy=(8 + 1.2*(x-8)/max(abs(x-8),0.01),
                        6 + 1.2*(y-6)/max(abs(y-6),0.01)),
                xytext=(x, y + (0.7 if y > 6 else -0.7)),
                arrowprops=dict(arrowstyle='->', color=color,
                               lw=1, alpha=0.5, linestyle='--'))

# The 19/13 connection highlighted
ax.text(8, 0.0,
        '19 (b2_SM) and 13 (b2_VL) connect unification, '
        'Lambda, dark matter, and H0',
        color=YELLOW, fontsize=9, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK,
                  edgecolor=YELLOW))

fig.savefig(os.path.join(OUT, 'cabibbo_07_series_connections.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_07_series_connections.png")


# ================================================================
# FIGURE 8: LEVEL 1 / LEVEL 2 CLASSIFICATION
# ================================================================

fig, ax = make_fig(14, 9)
ax.set_xlim(-1, 15)
ax.set_ylim(-0.5, 9.5)
ax.axis('off')

ax.text(7, 9.0, 'WHAT IS DETERMINED vs WHAT IS MEASURED',
        color=TEXT, fontsize=15, ha='center', fontweight='bold')

# Level 1 box (left)
l1 = FancyBboxPatch((0.3, 2.5), 6.0, 5.5,
                      boxstyle="round,pad=0.3",
                      facecolor=DARK, edgecolor=ACCENT, linewidth=2.5)
ax.add_patch(l1)
ax.text(3.3, 7.5, 'LEVEL 1: DETERMINED', color=ACCENT, fontsize=12,
        ha='center', fontweight='bold')
ax.text(3.3, 7.0, 'by the gauge group integers', color=ACCENT,
        fontsize=8, ha='center')

l1_items = [
    'Representation: (3, 2, 1/6)',
    'Db1 = 1/15, Db2 = 1, Db3 = 1/3',
    'Gap ratio: 38/27 (exact)',
    'Asymmetry: Db2/Db1 = 15',
    'Upper charge: +2/3',
    'Lower charge: -1/3',
    'Anomaly-free: automatic',
    'Bare mass: allowed',
]
for i, item in enumerate(l1_items):
    ax.text(0.8, 6.3 - i * 0.45, item, color=TEXT, fontsize=8)

# Level 2 box (right)
l2 = FancyBboxPatch((7.5, 2.5), 6.0, 5.5,
                      boxstyle="round,pad=0.3",
                      facecolor=DARK, edgecolor=TORUS, linewidth=2.5)
ax.add_patch(l2)
ax.text(10.5, 7.5, 'LEVEL 2: MEASURED', color=TORUS, fontsize=12,
        ha='center', fontweight='bold')
ax.text(10.5, 7.0, 'supplied by the universe', color=TORUS,
        fontsize=8, ha='center')

l2_items = [
    'Mass M_VL: 1.5-6 TeV (window)',
    'theta_14: |V_ub\'| ~ 0.045 (CKM)',
    'theta_24: constrained (kaons)',
    'theta_34: constrained (A_FB^b)',
    'delta_1: constrained (neutron EDM)',
    'delta_2: constrained (CP violation)',
    '',
    '6 new parameters total',
]
for i, item in enumerate(l2_items):
    ax.text(8.0, 6.3 - i * 0.45, item, color=TEXT, fontsize=8)

# Derived (middle bottom)
der = FancyBboxPatch((3.5, 0.3), 7.0, 1.5,
                      boxstyle="round,pad=0.2",
                      facecolor=DARK, edgecolor=YELLOW, linewidth=2)
ax.add_patch(der)
ax.text(7, 1.4, 'DERIVED (Level 1 + Level 2)', color=YELLOW,
        fontsize=10, ha='center', fontweight='bold')
ax.text(7, 0.8, 'M_GUT = 10^15.5 GeV    '
        'Proton lifetime ~ 10^34-35 yr', color=TEXT,
        fontsize=8, ha='center')

# Arrows
ax.annotate('', xy=(5, 1.8), xytext=(3.3, 2.5),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=1.5))
ax.annotate('', xy=(9, 1.8), xytext=(10.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=1.5))

fig.savefig(os.path.join(OUT, 'cabibbo_08_level1_level2.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: cabibbo_08_level1_level2.png")


print("\n=== ALL 8 DIAGRAMS SAVED ===")
print("Location: %s/cabibbo_*.png" % OUT)
