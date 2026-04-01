#!/usr/bin/env python3
"""
HOWL Figure 3: The Generation Democracy
========================================
Each generation contributes (4/3, 4/3, 4/3).
Democratic. Invisible to the gap ratio.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.7, 'Figure 3: The Generation Democracy', ha='center', fontsize=16, fontweight='bold')
ax.text(7, 9.2, 'Every complete generation contributes equally to all three beta functions',
        ha='center', fontsize=11, fontstyle='italic', color='#555')

# Three columns: Δb₁, Δb₂, Δb₃
col_x = [3.0, 7.0, 11.0]
col_labels = [r'$\Delta b_1$ (U(1))', r'$\Delta b_2$ (SU(2))', r'$\Delta b_3$ (SU(3))']
col_colors = [('#E6F1FB', '#185FA5', '#0C447C'),
              ('#EEEDFE', '#534AB7', '#3C3489'),
              ('#E1F5EE', '#0F6E56', '#085041')]

for j, (x, label, (fc, ec, tc)) in enumerate(col_x_data := list(zip(col_x, col_labels, col_colors))):
    ax.text(x, 8.5, label, ha='center', fontsize=12, fontweight='bold', color=tc)

# Source row labels
sources = [
    ('Gauge self-coupling', ['0', '−22/3', '−11'], '#888'),
    ('Per generation (×3)', ['4/3', '4/3', '4/3'], '#000'),
    ('Higgs doublet', ['1/10', '1/6', '0'], '#888'),
    ('SM TOTAL', ['41/10', '−19/6', '−7'], '#000'),
]

row_y = [7.5, 6.2, 4.9, 3.3]
row_heights = [0.8, 0.8, 0.8, 0.9]

for i, (src_label, values, text_color) in enumerate(sources):
    y = row_y[i]
    h = row_heights[i]
    
    # Source label
    ax.text(0.3, y, src_label, ha='left', va='center', fontsize=10, 
            fontweight='bold' if i == 3 else 'normal', color=text_color)
    
    for j, (x, val) in enumerate(zip(col_x, values)):
        fc, ec, tc = col_colors[j]
        
        if i == 1:  # Generation row — highlight with color
            rect = patches.FancyBboxPatch((x - 1.2, y - 0.4), 2.4, 0.8,
                   boxstyle="round,pad=0.05", facecolor='#FAEEDA', edgecolor='#BA7517', linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x, y, val, ha='center', va='center', fontsize=14, fontweight='bold', color='#633806')
        elif i == 3:  # Total row — bold with underline
            rect = patches.FancyBboxPatch((x - 1.2, y - 0.45), 2.4, 0.9,
                   boxstyle="round,pad=0.05", facecolor=fc, edgecolor=ec, linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x, y, val, ha='center', va='center', fontsize=13, fontweight='bold', color=tc)
        else:
            rect = patches.FancyBboxPatch((x - 1.2, y - 0.4), 2.4, 0.8,
                   boxstyle="round,pad=0.05", facecolor='#F8F8F6', edgecolor='#CCC', linewidth=0.5)
            ax.add_patch(rect)
            ax.text(x, y, val, ha='center', va='center', fontsize=12, color='#555')

# The key insight box
rect = patches.FancyBboxPatch((0.5, 1.2), 13, 1.6,
       boxstyle="round,pad=0.1", facecolor='#FAEEDA', edgecolor='#BA7517', linewidth=2)
ax.add_patch(rect)
ax.text(7, 2.3, 'GENERATION DEMOCRACY: 4/3 = 4/3 = 4/3', 
        ha='center', fontsize=14, fontweight='bold', color='#633806')
ax.text(7, 1.7, 'Equal contributions cancel in the gap ratio: (4/3 − 4/3) / (4/3 − 4/3) = 0/0 → no effect.\n'
        'The gap ratio is 218/115 for ANY number of complete generations (0, 1, 3, 10, N).',
        ha='center', fontsize=10, color='#854F0B')

# Verification
ax.text(7, 0.5, 'Verification: (41/10 − 0 − 1/10)/3 = 4/3 ✓    (−19/6 + 22/3 − 1/6)/3 = 4/3 ✓    (−7 + 11 − 0)/3 = 4/3 ✓',
        ha='center', fontsize=9, color='#888')

plt.tight_layout()
plt.savefig('fig3_generation_democracy.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 3 saved: fig3_generation_democracy.png")
