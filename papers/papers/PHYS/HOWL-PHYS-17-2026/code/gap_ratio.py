#!/usr/bin/env python3
"""
HOWL Figure 2: Gap Ratio Anatomy — The Boson Problem
=====================================================
Numerator and denominator decomposition: gauge, fermion, Higgs.
Plus the gap ratio progression from 2.000 to 1.358.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

# ============================================================
# LEFT: Numerator and Denominator bars
# ============================================================
ax = ax1
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 12)
ax.axis('off')

ax.text(5, 11.7, 'Where does 218/115 come from?', ha='center', fontsize=14, fontweight='bold')
ax.text(5, 11.2, 'Gap ratio = (b₁−b₂) / (b₂−b₃)', ha='center', fontsize=11, color='#534AB7')

# NUMERATOR section
ax.text(5, 10.2, 'NUMERATOR: b₁ − b₂ = 109/15 = 7.267', ha='center', fontsize=11, fontweight='bold', color='#0C447C')

# Gauge bar (scaled: 7.333 out of ~7.5 max)
scale = 0.9
w_gauge = 7.333 * scale
rect = patches.FancyBboxPatch((1, 9.0), w_gauge, 0.7,
       boxstyle="round,pad=0.05", facecolor='#EEEDFE', edgecolor='#534AB7', linewidth=1)
ax.add_patch(rect)
ax.text(1.2, 9.35, 'Gauge: +22/3 = +7.333', ha='left', fontsize=9, fontweight='bold', color='#3C3489')
ax.text(1 + w_gauge - 0.1, 9.35, '100.9%', ha='right', fontsize=9, color='#534AB7')

# Fermion bar (ZERO)
rect = patches.FancyBboxPatch((1, 8.0), 0.5, 0.7,
       boxstyle="round,pad=0.05", facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=1.5)
ax.add_patch(rect)
ax.text(1.7, 8.35, 'Fermions: ZERO  (4/3 − 4/3 = 0)', ha='left', fontsize=9, fontweight='bold', color='#791F1F')
ax.text(7.5, 8.35, '0%', ha='right', fontsize=12, fontweight='bold', color='#A32D2D')

# Higgs bar (tiny)
rect = patches.FancyBboxPatch((1, 7.0), 0.5, 0.7,
       boxstyle="round,pad=0.05", facecolor='#FAEEDA', edgecolor='#854F0B', linewidth=1)
ax.add_patch(rect)
ax.text(1.7, 7.35, 'Higgs: −1/15 = −0.067', ha='left', fontsize=9, fontweight='bold', color='#633806')
ax.text(7.5, 7.35, '−0.9%', ha='right', fontsize=9, color='#854F0B')

# DENOMINATOR section
ax.text(5, 5.8, 'DENOMINATOR: b₂ − b₃ = 23/6 = 3.833', ha='center', fontsize=11, fontweight='bold', color='#0C447C')

w_gauge_d = 3.667 * scale
rect = patches.FancyBboxPatch((1, 4.6), w_gauge_d, 0.7,
       boxstyle="round,pad=0.05", facecolor='#EEEDFE', edgecolor='#534AB7', linewidth=1)
ax.add_patch(rect)
ax.text(1.2, 4.95, 'Gauge: +11/3 = +3.667', ha='left', fontsize=9, fontweight='bold', color='#3C3489')
ax.text(1 + w_gauge_d - 0.1, 4.95, '95.7%', ha='right', fontsize=9, color='#534AB7')

rect = patches.FancyBboxPatch((1, 3.6), 0.5, 0.7,
       boxstyle="round,pad=0.05", facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=1.5)
ax.add_patch(rect)
ax.text(1.7, 3.95, 'Fermions: ZERO', ha='left', fontsize=9, fontweight='bold', color='#791F1F')
ax.text(7.5, 3.95, '0%', ha='right', fontsize=12, fontweight='bold', color='#A32D2D')

w_higgs_d = 0.167 * scale + 0.5
rect = patches.FancyBboxPatch((1, 2.6), w_higgs_d, 0.7,
       boxstyle="round,pad=0.05", facecolor='#FAEEDA', edgecolor='#854F0B', linewidth=1)
ax.add_patch(rect)
ax.text(1.7, 2.95, 'Higgs: +1/6 = +0.167', ha='left', fontsize=9, fontweight='bold', color='#633806')
ax.text(7.5, 2.95, '4.3%', ha='right', fontsize=9, color='#854F0B')

# Verdict box
rect = patches.FancyBboxPatch((0.5, 0.5), 9, 1.5,
       boxstyle="round,pad=0.1", facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=2)
ax.add_patch(rect)
ax.text(5, 1.55, 'THE BOSON PROBLEM', ha='center', fontsize=14, fontweight='bold', color='#791F1F')
ax.text(5, 0.95, 'All 12 SM fermions (e, μ, τ, ν₁₂₃, u, d, c, s, t, b) contribute 0%.', 
        ha='center', fontsize=10, color='#A32D2D')

# ============================================================
# RIGHT: Gap ratio progression
# ============================================================
ax = ax2
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 12)
ax.axis('off')

ax.text(5, 11.7, 'The gap ratio: from gauge to measurement', ha='center', fontsize=14, fontweight='bold')

scenarios = [
    ('Gauge only\n(no matter at all)', 2.000, '22/11 = 2.000', '#EEEDFE', '#534AB7', '#3C3489'),
    ('+ Higgs doublet\n(still no fermions)', 1.896, '218/115 = 1.896', '#FAEEDA', '#854F0B', '#633806'),
    ('+ 1 generation\n(e, νe, u, d)', 1.896, 'STILL 218/115', '#E6F1FB', '#185FA5', '#0C447C'),
    ('+ 3 generations\n(full SM)', 1.896, 'STILL 218/115', '#E6F1FB', '#185FA5', '#0C447C'),
    ('+ 10 generations\n(hypothetical)', 1.896, 'STILL 218/115!', '#E6F1FB', '#185FA5', '#0C447C'),
    ('+ Cabibbo Doublet\n(1 particle)', 1.407, '38/27 = 1.407', '#E1F5EE', '#0F6E56', '#085041'),
    ('MEASURED\n(from DATA-3)', 1.358, '1.358', '#F1EFE8', '#5F5E5A', '#444441'),
]

bar_left = 0.5
bar_max_width = 8.5
val_min = 1.2
val_max = 2.1

for i, (label, val, ratio_str, fc, ec, tc) in enumerate(scenarios):
    y = 10.0 - i * 1.4
    w = (val - val_min) / (val_max - val_min) * bar_max_width
    
    rect = patches.FancyBboxPatch((bar_left, y - 0.35), w, 0.7,
           boxstyle="round,pad=0.05", facecolor=fc, edgecolor=ec, linewidth=1)
    ax.add_patch(rect)
    
    ax.text(bar_left + 0.15, y + 0.05, label.split('\n')[0], ha='left', fontsize=9, fontweight='bold', color=tc)
    if '\n' in label:
        ax.text(bar_left + 0.15, y - 0.2, label.split('\n')[1], ha='left', fontsize=8, color=ec)
    
    ax.text(bar_left + w + 0.15, y, ratio_str, ha='left', va='center', fontsize=9, fontweight='bold', color=tc)

# Bracket showing "fermions don't matter"
ax.annotate('', xy=(9.2, 7.6), xytext=(9.2, 4.2),
            arrowprops=dict(arrowstyle='-', color='#A32D2D', lw=1.5))
ax.plot([9.0, 9.2], [7.6, 7.6], '-', color='#A32D2D', lw=1.5)
ax.plot([9.0, 9.2], [4.2, 4.2], '-', color='#A32D2D', lw=1.5)
ax.text(9.4, 5.9, 'Fermions\nchange\nNOTHING', ha='left', va='center', fontsize=9, fontweight='bold', color='#A32D2D')

# Arrow from Cabibbo Doublet showing the jump
ax.annotate('', xy=(bar_left + (1.407 - val_min)/(val_max-val_min)*bar_max_width, 2.05),
            xytext=(bar_left + (1.896 - val_min)/(val_max-val_min)*bar_max_width, 2.75),
            arrowprops=dict(arrowstyle='->', color='#D85A30', lw=2))

# Measured line
measured_x = bar_left + (1.358 - val_min) / (val_max - val_min) * bar_max_width
ax.plot([measured_x, measured_x], [0.2, 10.5], '--', color='#A32D2D', linewidth=1, alpha=0.5)
ax.text(measured_x, 10.7, 'Target: 1.358', ha='center', fontsize=9, fontweight='bold', color='#A32D2D')

plt.tight_layout()
plt.savefig('fig2_gap_ratio_anatomy.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 2 saved: fig2_gap_ratio_anatomy.png")
