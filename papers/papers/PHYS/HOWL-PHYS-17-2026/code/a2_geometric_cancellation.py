#!/usr/bin/env python3
"""
HOWL Figure 7: The A₂ Geometric Cancellation
=============================================
87% cancellation between geometry (R₄) and 
rational + number-theoretic content.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(0, 9.7, 'Figure 7: The A₂ Geometric Cancellation', ha='center', fontsize=16, fontweight='bold')
ax.text(0, 9.2, 'A₂ = 197/144 + (3/4)ζ(3) + R₄×(8/3 − 16ln2) = −0.328',
        ha='center', fontsize=11, fontstyle='italic', color='#555')

# Stacked bar showing the three pieces
bar_x = -0.6
bar_w = 1.2
scale = 2.5  # scale factor for visual

# Positive pieces (stacked upward from baseline at y=4)
baseline = 4.0

# Rational: +1.368
h_rat = 1.368 * scale
rect = patches.FancyBboxPatch((bar_x, baseline), bar_w, h_rat,
       boxstyle="round,pad=0.02", facecolor='#E6F1FB', edgecolor='#185FA5', linewidth=1)
ax.add_patch(rect)
ax.text(0, baseline + h_rat/2, '197/144\n+1.368', ha='center', va='center', fontsize=10, fontweight='bold', color='#0C447C')

# Number-theoretic: +0.902 (stacked on top)
h_num = 0.902 * scale
rect = patches.FancyBboxPatch((bar_x, baseline + h_rat), bar_w, h_num,
       boxstyle="round,pad=0.02", facecolor='#EEEDFE', edgecolor='#534AB7', linewidth=1)
ax.add_patch(rect)
ax.text(0, baseline + h_rat + h_num/2, '(3/4)ζ(3)\n+0.902', ha='center', va='center', fontsize=10, fontweight='bold', color='#3C3489')

# Geometric: -2.598 (goes downward from baseline)
h_geo = 2.598 * scale
rect = patches.FancyBboxPatch((bar_x, baseline - h_geo), bar_w, h_geo,
       boxstyle="round,pad=0.02", facecolor='#FAECE7', edgecolor='#D85A30', linewidth=1.5)
ax.add_patch(rect)
ax.text(0, baseline - h_geo/2, 'R₄×(8/3−16ln2)\n−2.598', ha='center', va='center', fontsize=10, fontweight='bold', color='#993C1D')

# Baseline
ax.plot([-2.5, 2.5], [baseline, baseline], '-', color='#888', linewidth=0.5)
ax.text(-2.7, baseline, '0', ha='right', va='center', fontsize=9, color='#888')

# Net A₂ marker
net_y = baseline + (1.368 + 0.902 - 2.598) * scale
ax.plot([-1.5, 1.5], [net_y, net_y], '-', color='#A32D2D', linewidth=2)
ax.text(1.7, net_y, 'Net A₂ = −0.328', ha='left', va='center', fontsize=11, fontweight='bold', color='#A32D2D')

# Labels on right side
labels = [
    (baseline + h_rat + h_num + 0.3, 'POSITIVE: +2.270', '(rational + number-theoretic)', '#534AB7'),
    (baseline - h_geo - 0.3, 'NEGATIVE: −2.598', '(geometric: 4D phase space)', '#D85A30'),
]
for y, main, sub, color in labels:
    ax.text(2.0, y, main, ha='left', va='center', fontsize=11, fontweight='bold', color=color)
    ax.text(2.0, y - 0.3, sub, ha='left', va='center', fontsize=9, color=color)

# Cancellation annotation
ax.annotate('', xy=(1.5, baseline + h_rat + h_num), xytext=(1.5, baseline - h_geo),
            arrowprops=dict(arrowstyle='<->', color='#888', lw=1))
ax.text(-2.5, baseline - h_geo/2, '87.4%\ncancellation', ha='center', va='center', 
        fontsize=12, fontweight='bold', color='#A32D2D',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=1))

# Legend
legend_items = [
    ('#E6F1FB', '#185FA5', 'Rational: diagram combinatorics (197 prime, 144 = 12²)'),
    ('#EEEDFE', '#534AB7', 'Number-theoretic: Feynman parameter integrals (ζ(3))'),
    ('#FAECE7', '#D85A30', 'Geometric: 4D phase space × IR regulation (R₄ = π²/32)'),
]
for i, (fc, ec, label) in enumerate(legend_items):
    y = 0.8 - i * 0.35
    rect = patches.FancyBboxPatch((-2.8, y - 0.1), 0.3, 0.2,
           boxstyle="round,pad=0.02", facecolor=fc, edgecolor=ec, linewidth=0.8)
    ax.add_patch(rect)
    ax.text(-2.4, y, label, ha='left', va='center', fontsize=8, color='#444')

plt.tight_layout()
plt.savefig('fig7_a2_cancellation.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 7 saved: fig7_a2_cancellation.png")
