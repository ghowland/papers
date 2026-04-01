#!/usr/bin/env python3
"""
HOWL Figure 1: The Soliton Boundary Energy Landscape
=====================================================
The full energy map from atomic scales to M_GUT.
Each band is a domain with fixed integer rules (beta coefficients).
Boundaries are mass thresholds where the rules change.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 16.5)
ax.axis('off')

ax.text(5, 16.2, 'Figure 1: The Soliton Boundary Energy Landscape',
        ha='center', va='top', fontsize=16, fontweight='bold')
ax.text(5, 15.7, 'Integer rules on each side of every boundary. Values run between boundaries.',
        ha='center', va='top', fontsize=11, fontstyle='italic', color='#555')

# Energy axis
ax.annotate('', xy=(0.7, 15.5), xytext=(0.7, 0.5),
            arrowprops=dict(arrowstyle='->', color='#888', lw=1.2))
ax.text(0.7, 0.2, 'Energy', ha='center', fontsize=9, color='#888')

energy_labels = [
    (15.0, '$10^{16}$ GeV'),
    (13.8, '$10^{15.5}$ GeV'),
    (11.0, '$10^{3.5}$ GeV'),
    (9.0, '$10^{2.2}$ GeV'),
    (7.0, '$10^{0.6}$ GeV'),
    (4.5, '$10^{-0.5}$ GeV'),
    (1.0, '$10^{-3.3}$ GeV'),
]
for y, label in energy_labels:
    ax.text(0.55, y, label, ha='right', va='center', fontsize=8, color='#666')
    ax.plot([0.65, 1.2], [y, y], '--', color='#ccc', linewidth=0.5)

# Domain: Unified
rect = patches.FancyBboxPatch((1.3, 14.0), 5.5, 1.5,
       boxstyle="round,pad=0.1", facecolor='#EEEDFE', edgecolor='#534AB7', linewidth=1.5)
ax.add_patch(rect)
ax.text(4.05, 14.95, 'UNIFIED DOMAIN', ha='center', fontsize=12, fontweight='bold', color='#3C3489')
ax.text(4.05, 14.45, r'$\alpha_1 = \alpha_2 = \alpha_3 = \alpha_{GUT}$    •    One force', 
        ha='center', fontsize=9, color='#534AB7')

# Boundary: M_GUT
ax.plot([1.3, 6.8], [13.8, 13.8], '-', color='#534AB7', linewidth=2)
ax.text(7.0, 13.8, r'$M_{GUT} = 10^{15.5}$ GeV', ha='left', va='center', fontsize=9, fontweight='bold', color='#534AB7')

# Domain: Modified running (M_VL to M_GUT)
rect = patches.FancyBboxPatch((1.3, 11.3), 5.5, 2.3,
       boxstyle="round,pad=0.1", facecolor='#E1F5EE', edgecolor='#0F6E56', linewidth=1.5)
ax.add_patch(rect)
ax.text(4.05, 12.7, 'MODIFIED RUNNING', ha='center', fontsize=12, fontweight='bold', color='#085041')
ax.text(4.05, 12.2, 'b = (25/6, −13/6, −20/3)', ha='center', fontsize=10, color='#0F6E56')
ax.text(4.05, 11.75, 'Gap ratio = 38/27 = 1.407', ha='center', fontsize=10, fontweight='bold', color='#0F6E56')

# Boundary: Cabibbo Doublet
ax.plot([1.3, 6.8], [11.0, 11.0], '-', color='#D85A30', linewidth=3)
ax.plot([0.7, 1.3], [11.0, 11.0], '--', color='#D85A30', linewidth=1.5)
rect_cb = patches.FancyBboxPatch((7.0, 10.6), 2.8, 0.8,
          boxstyle="round,pad=0.1", facecolor='#FAECE7', edgecolor='#D85A30', linewidth=1)
ax.add_patch(rect_cb)
ax.text(8.4, 11.15, 'CABIBBO DOUBLET', ha='center', fontsize=9, fontweight='bold', color='#993C1D')
ax.text(8.4, 10.8, 'Gap ratio jumps here', ha='center', fontsize=8, color='#D85A30')

# Arrow showing the jump
ax.annotate('', xy=(8.4, 10.4), xytext=(8.4, 9.5),
            arrowprops=dict(arrowstyle='->', color='#D85A30', lw=2))
ax.text(9.5, 9.95, '218/115\n→ 38/27', ha='center', va='center', fontsize=10, fontweight='bold', color='#D85A30')

# Domain: SM full
rect = patches.FancyBboxPatch((1.3, 9.2), 5.5, 1.6,
       boxstyle="round,pad=0.1", facecolor='#E6F1FB', edgecolor='#185FA5', linewidth=1.5)
ax.add_patch(rect)
ax.text(4.05, 10.2, 'SM FULL (6 quarks, 3 leptons, Higgs)', ha='center', fontsize=11, fontweight='bold', color='#0C447C')
ax.text(4.05, 9.7, 'b = (41/10, −19/6, −7)    •    Gap = 218/115 = 1.896', 
        ha='center', fontsize=9, color='#185FA5')

# Boundary: m_t
ax.plot([1.3, 6.8], [9.0, 9.0], '--', color='#888', linewidth=0.8)
ax.text(7.0, 9.0, r'm$_t$ = 172.6 GeV', ha='left', va='center', fontsize=8, color='#888')

# Domain: 5-flavor
rect = patches.FancyBboxPatch((1.3, 7.3), 5.5, 1.5,
       boxstyle="round,pad=0.1", facecolor='#E6F1FB', edgecolor='#185FA5', linewidth=1)
ax.add_patch(rect)
ax.text(4.05, 8.25, '5-FLAVOR DOMAIN', ha='center', fontsize=11, fontweight='bold', color='#0C447C')
ax.text(4.05, 7.8, r'b$_3$ = −23/3   •   Gap STILL 218/115 (democracy!)', 
        ha='center', fontsize=9, color='#185FA5')

# Boundary: m_b
ax.plot([1.3, 6.8], [7.0, 7.0], '--', color='#888', linewidth=0.8)
ax.text(7.0, 7.0, r'm$_b$ = 4.18 GeV', ha='left', va='center', fontsize=8, color='#888')

# Domain: lower flavors
rect = patches.FancyBboxPatch((1.3, 5.3), 5.5, 1.5,
       boxstyle="round,pad=0.1", facecolor='#E6F1FB', edgecolor='#185FA5', linewidth=0.8)
ax.add_patch(rect)
ax.text(4.05, 6.25, '4- AND 3-FLAVOR DOMAINS', ha='center', fontsize=10, fontweight='bold', color='#0C447C')
ax.text(4.05, 5.8, 'c, τ, s thresholds   •   Gap always 218/115', 
        ha='center', fontsize=9, color='#185FA5')

# Confinement wall
rect = patches.FancyBboxPatch((1.3, 3.8), 5.5, 1.3,
       boxstyle="round,pad=0.1", facecolor='#FCEBEB', edgecolor='#A32D2D', linewidth=2)
ax.add_patch(rect)
ax.text(4.05, 4.65, 'CONFINEMENT WALL', ha='center', fontsize=12, fontweight='bold', color='#791F1F')
ax.text(4.05, 4.2, r'$\alpha_s$ → O(1)   •   No perturbative rules   •   BLANK ZONE', 
        ha='center', fontsize=9, color='#A32D2D')

# QED domain
rect = patches.FancyBboxPatch((1.3, 1.3), 5.5, 2.3,
       boxstyle="round,pad=0.1", facecolor='#F1EFE8', edgecolor='#5F5E5A', linewidth=1)
ax.add_patch(rect)
ax.text(4.05, 2.7, 'QED DOMAIN', ha='center', fontsize=11, fontweight='bold', color='#444441')
ax.text(4.05, 2.2, r'$\alpha_{em}$ = 1/137 at atomic scales', ha='center', fontsize=9, color='#5F5E5A')
ax.text(4.05, 1.75, r'Only 2 couplings ($\alpha_{em}$, $\alpha_s$)   •   No gap ratio test', 
        ha='center', fontsize=9, color='#5F5E5A')

# Legend
legend_items = [
    ('#E1F5EE', '#0F6E56', 'Modified running (Cabibbo Doublet active)'),
    ('#E6F1FB', '#185FA5', 'SM domains (fermions democratic, gap = 218/115)'),
    ('#FCEBEB', '#A32D2D', 'Confinement wall (no perturbative rules)'),
    ('#FAECE7', '#D85A30', 'Cabibbo Doublet threshold'),
]
for i, (fc, ec, label) in enumerate(legend_items):
    x = 1.3 + (i % 2) * 4.3
    y = 0.5 - (i // 2) * 0.4
    rect = patches.FancyBboxPatch((x, y-0.12), 0.3, 0.24,
           boxstyle="round,pad=0.02", facecolor=fc, edgecolor=ec, linewidth=0.8)
    ax.add_patch(rect)
    ax.text(x + 0.4, y, label, ha='left', va='center', fontsize=8, color='#444')

plt.tight_layout()
plt.savefig('fig1_energy_landscape.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 1 saved: fig1_energy_landscape.png")
