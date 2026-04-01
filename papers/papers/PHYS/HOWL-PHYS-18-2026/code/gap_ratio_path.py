#!/usr/bin/env python3
"""
HOWL Figure 5: Two Roads to the Same Particle
==============================================
Gap ratio path (top-down) and anomaly path (bottom-up)
converge on (3,2,1/6).
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1, 1, figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.7, 'Figure 5: Two Roads to the Cabibbo Doublet', ha='center', fontsize=16, fontweight='bold')
ax.text(7, 9.2, 'Two independent paths converge on the same particle. Neither knew about the other.',
        ha='center', fontsize=11, fontstyle='italic', color='#555')

# LEFT PATH: Gap ratio (top-down)
rect = patches.FancyBboxPatch((0.3, 7.5), 5.5, 1.2,
       boxstyle="round,pad=0.1", facecolor='#E1F5EE', edgecolor='#0F6E56', linewidth=1.5)
ax.add_patch(rect)
ax.text(3.05, 8.3, 'GAP RATIO PATH (this series)', ha='center', fontsize=11, fontweight='bold', color='#085041')
ax.text(3.05, 7.85, r'Start: $\alpha_{em}$, sin²θ$_W$, $\alpha_s$ at M$_Z$', 
        ha='center', fontsize=9, color='#0F6E56')

steps_left = [
    'Compute SM gap ratio: 218/115',
    'Compare to measured: 1.358 (40% miss)',
    'Enumerate 15 single-multiplet extensions',
    'Eliminate 13 by gap ratio, 1 by proton decay',
]
for i, step in enumerate(steps_left):
    y = 7.0 - i * 0.7
    ax.text(0.5, y, f'→ {step}', ha='left', fontsize=9, color='#0F6E56')
    
ax.text(3.05, 4.4, 'DETERMINES:', ha='center', fontsize=9, fontweight='bold', color='#085041')
ax.text(3.05, 4.05, 'Representation (3,2,1/6)', ha='center', fontsize=9, color='#0F6E56')
ax.text(3.05, 3.7, r'M$_{GUT}$ = 10$^{15.5}$ GeV', ha='center', fontsize=9, color='#0F6E56')
ax.text(3.05, 3.35, r'Proton lifetime ~ 10$^{34-35}$ yr', ha='center', fontsize=9, color='#0F6E56')

# RIGHT PATH: Anomaly (bottom-up)
rect = patches.FancyBboxPatch((8.2, 7.5), 5.5, 1.2,
       boxstyle="round,pad=0.1", facecolor='#EEEDFE', edgecolor='#534AB7', linewidth=1.5)
ax.add_patch(rect)
ax.text(10.95, 8.3, 'ANOMALY PATH (literature)', ha='center', fontsize=11, fontweight='bold', color='#3C3489')
ax.text(10.95, 7.85, r'Start: V$_{ud}$, V$_{us}$, A$^b_{FB}$, μ$_{Higgs}$',
        ha='center', fontsize=9, color='#534AB7')

steps_right = [
    'CKM unitarity deficit: 2.5-4σ',
    'LEP A_FB^b anomaly: ~3σ',
    'Higgs signal strength excess: ~2σ',
    'Global fit: VL quark doublet resolves all three',
]
for i, step in enumerate(steps_right):
    y = 7.0 - i * 0.7
    ax.text(8.4, y, f'→ {step}', ha='left', fontsize=9, color='#534AB7')

ax.text(10.95, 4.4, 'DETERMINES:', ha='center', fontsize=9, fontweight='bold', color='#3C3489')
ax.text(10.95, 4.05, 'Representation (3,2,1/6)', ha='center', fontsize=9, color='#534AB7')
ax.text(10.95, 3.7, 'Mass: 1.5-6 TeV', ha='center', fontsize=9, color='#534AB7')
ax.text(10.95, 3.35, '|V_ub\'| ≈ 0.045, mixing angles', ha='center', fontsize=9, color='#534AB7')

# CONVERGENCE: Center box
rect = patches.FancyBboxPatch((3.5, 1.0), 7, 2.0,
       boxstyle="round,pad=0.15", facecolor='#FAECE7', edgecolor='#D85A30', linewidth=2.5)
ax.add_patch(rect)
ax.text(7, 2.4, 'THE CABIBBO DOUBLET', ha='center', fontsize=14, fontweight='bold', color='#993C1D')
ax.text(7, 1.95, '(3, 2, 1/6) vector-like quark doublet', ha='center', fontsize=11, color='#D85A30')
ax.text(7, 1.5, 'Q = +2/3, −1/3   •   Mass 1.5-6 TeV   •   Gap 38/27', ha='center', fontsize=9, color='#993C1D')

# Arrows converging
ax.annotate('', xy=(5.0, 2.5), xytext=(3.05, 3.2),
            arrowprops=dict(arrowstyle='->', color='#0F6E56', lw=2.5, 
                           connectionstyle='arc3,rad=0.15'))
ax.annotate('', xy=(9.0, 2.5), xytext=(10.95, 3.2),
            arrowprops=dict(arrowstyle='->', color='#534AB7', lw=2.5,
                           connectionstyle='arc3,rad=-0.15'))

# Key references
ax.text(7, 0.5, 'Gap ratio: PHYS-15 (2026)    |    Anomaly: Belfatto, Berezhiani (2020); Cheung et al. (2020)',
        ha='center', fontsize=9, color='#888')

plt.tight_layout()
plt.savefig('fig5_two_roads.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 5 saved: fig5_two_roads.png")
