#!/usr/bin/env python3
"""
HOWL Figure 4: The Elimination Cascade
=======================================
15 candidates → 3 → 2 → 1 minimal survivor
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1, 1, figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.7, 'Figure 4: The Elimination Cascade', ha='center', fontsize=16, fontweight='bold')
ax.text(7, 9.2, '15 candidates tested in exact rational arithmetic. One minimal survivor.',
        ha='center', fontsize=11, fontstyle='italic', color='#555')

# Stage 0: All 15
rect = patches.FancyBboxPatch((0.5, 7.8), 13, 1.0,
       boxstyle="round,pad=0.1", facecolor='#F1EFE8', edgecolor='#5F5E5A', linewidth=1)
ax.add_patch(rect)
ax.text(7, 8.45, '15 CANDIDATES', ha='center', fontsize=13, fontweight='bold', color='#444')
ax.text(7, 8.05, 'All single multiplets: SU(3) dim ≤ 8, SU(2) dim ≤ 4, |Y| ≤ 2, scalar or vector-like fermion',
        ha='center', fontsize=9, color='#666')

# Arrow down
ax.annotate('', xy=(7, 7.6), xytext=(7, 7.8),
            arrowprops=dict(arrowstyle='->', color='#A32D2D', lw=2))

# Stage 1: Gap ratio eliminates 12
rect = patches.FancyBboxPatch((0.5, 6.2), 13, 1.2,
       boxstyle="round,pad=0.1", facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=1.5)
ax.add_patch(rect)
ax.text(2, 7.0, 'STAGE 1: Gap ratio arithmetic', ha='left', fontsize=11, fontweight='bold', color='#791F1F')
ax.text(2, 6.6, '12 eliminated: modified gap ratio > 0.15 from measured 1.358', 
        ha='left', fontsize=9, color='#A32D2D')
ax.text(12, 6.8, '12 OUT', ha='center', fontsize=12, fontweight='bold', color='#A32D2D')

# Arrow down
ax.annotate('', xy=(7, 6.0), xytext=(7, 6.2),
            arrowprops=dict(arrowstyle='->', color='#888', lw=2))

# 3 survivors
rect = patches.FancyBboxPatch((0.5, 4.8), 13, 1.0,
       boxstyle="round,pad=0.1", facecolor='#E6F1FB', edgecolor='#185FA5', linewidth=1)
ax.add_patch(rect)
ax.text(7, 5.45, '3 SURVIVORS', ha='center', fontsize=12, fontweight='bold', color='#0C447C')

# Three survivor boxes
survivors = [
    ('MSSM\n7/5 = 1.400\ndist 0.042', '#EEEDFE', '#534AB7', '#3C3489'),
    ('Cabibbo Doublet\n38/27 = 1.407\ndist 0.049', '#E1F5EE', '#0F6E56', '#085041'),
    ('SU(5) 5+5̄\n40/27 = 1.481\ndist 0.123', '#F1EFE8', '#5F5E5A', '#444'),
]

for i, (label, fc, ec, tc) in enumerate(survivors):
    x = 2.0 + i * 4.0
    rect = patches.FancyBboxPatch((x - 1.5, 3.5), 3.8, 1.1,
           boxstyle="round,pad=0.1", facecolor=fc, edgecolor=ec, linewidth=1)
    ax.add_patch(rect)
    lines = label.split('\n')
    ax.text(x + 0.4, 4.25, lines[0], ha='center', fontsize=10, fontweight='bold', color=tc)
    ax.text(x + 0.4, 3.9, lines[1], ha='center', fontsize=9, color=ec)
    ax.text(x + 0.4, 3.65, lines[2], ha='center', fontsize=9, color=ec)

# Stage 2: Proton decay eliminates SU(5)
ax.annotate('', xy=(11.5, 3.3), xytext=(11.5, 3.5),
            arrowprops=dict(arrowstyle='->', color='#A32D2D', lw=2))
rect = patches.FancyBboxPatch((9.0, 2.3), 5.0, 0.8,
       boxstyle="round,pad=0.1", facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=1.5)
ax.add_patch(rect)
ax.text(11.5, 2.85, 'STAGE 2: Proton decay', ha='center', fontsize=10, fontweight='bold', color='#791F1F')
ax.text(11.5, 2.5, r'M$_{GUT}$ = 10$^{14.9}$ < 10$^{15.5}$ limit → EXCLUDED', 
        ha='center', fontsize=9, color='#A32D2D')

# Two survivors with boxes
rect1 = patches.FancyBboxPatch((0.5, 0.5), 5.5, 1.5,
        boxstyle="round,pad=0.1", facecolor='#EEEDFE', edgecolor='#534AB7', linewidth=1.5)
ax.add_patch(rect1)
ax.text(3.25, 1.5, 'MSSM (complete framework)', ha='center', fontsize=11, fontweight='bold', color='#3C3489')
ax.text(3.25, 1.05, 'Gap = 7/5   •   ~120 new fields   •   M$_{GUT}$ = 10$^{17.3}$',
        ha='center', fontsize=9, color='#534AB7')

rect2 = patches.FancyBboxPatch((6.5, 0.5), 5.5, 1.5,
        boxstyle="round,pad=0.1", facecolor='#E1F5EE', edgecolor='#0F6E56', linewidth=2)
ax.add_patch(rect2)
ax.text(9.25, 1.5, 'CABIBBO DOUBLET (minimal)', ha='center', fontsize=11, fontweight='bold', color='#085041')
ax.text(9.25, 1.05, 'Gap = 38/27   •   4 new fields   •   M$_{GUT}$ = 10$^{15.5}$',
        ha='center', fontsize=9, color='#0F6E56')

# Arrows from stage 1 to survivors
ax.annotate('', xy=(3.25, 2.0), xytext=(3.25, 3.5),
            arrowprops=dict(arrowstyle='->', color='#534AB7', lw=1.5))
ax.annotate('', xy=(9.25, 2.0), xytext=(7.0, 3.5),
            arrowprops=dict(arrowstyle='->', color='#0F6E56', lw=1.5))

plt.tight_layout()
plt.savefig('fig4_elimination_cascade.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 4 saved: fig4_elimination_cascade.png")
