#!/usr/bin/env python3
"""
HOWL Figure 6: The Y = 1/6 Asymmetry
=====================================
Why the Cabibbo Doublet works: smallest hypercharge
creates maximum Δb₂/Δb₁ ratio.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

# ============================================================
# LEFT: Δb₂/Δb₁ ratio vs Y for (3,2,Y) vector-like fermion
# ============================================================
ax = ax1
Y_vals = np.array([1/6, 1/3, 1/2, 2/3, 5/6, 1.0, 7/6])
ratios = 1 / (Y_vals * 6)**2 * 36 * 15  # Δb₂/Δb₁ = 15/((6Y)²/36) simplified

# Actually compute properly: Δb₁ ∝ Y², Δb₂ = 1 (fixed)
# For (3,2,Y) VL: Δb₁ = (4/5)(Y²)(3)(2)(1/3) = 8Y²/5
# Δb₂ = (4/3)(1/2)(3) = 2... but known value at Y=1/6 is Δb₁=1/15, Δb₂=1
# So Δb₂/Δb₁ = 1/(1/15 * (Y/1/6)²) = 1/((Y²)/(1/36) * 1/15) = 15 * (1/36)/Y² = 15/(36Y²)
# At Y=1/6: 15/(36/36) = 15 ✓
# At Y=1/2: 15/(36/4) = 15/9 = 5/3 ✓

ratios_correct = 15.0 / (36 * Y_vals**2)

ax.bar(range(len(Y_vals)), ratios_correct, color=['#D85A30'] + ['#B4B2A9']*6, 
       edgecolor=['#993C1D'] + ['#888']*6, linewidth=1)

ax.set_xticks(range(len(Y_vals)))
ax.set_xticklabels(['1/6\n(Cabibbo\nDoublet)', '1/3', '1/2', '2/3', '5/6', '1', '7/6'], fontsize=9)
ax.set_ylabel(r'$\Delta b_2 / \Delta b_1$ (asymmetry ratio)', fontsize=11)
ax.set_xlabel('Hypercharge Y for (3,2,Y) vector-like fermion', fontsize=11)
ax.set_title('The Y = 1/6 asymmetry spike', fontsize=13, fontweight='bold')

# Annotate the peak
ax.annotate(f'Δb₂/Δb₁ = 15', xy=(0, 15), xytext=(1.5, 13),
            fontsize=11, fontweight='bold', color='#D85A30',
            arrowprops=dict(arrowstyle='->', color='#D85A30', lw=1.5))

ax.axhline(y=1, color='#A32D2D', linestyle='--', linewidth=0.8, alpha=0.5)
ax.text(5.5, 1.3, 'Ratio = 1 (symmetric)', fontsize=8, color='#A32D2D')

ax.set_ylim(0, 17)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================
# RIGHT: Gap ratio distance vs Y
# ============================================================
ax = ax2

# Compute gap ratios for each Y
# b1_new = 41/10 + Δb1, b2_new = -19/6 + 1, b3_new = -7 + 1/3
# Δb₁ scales as Y², keeping Δb₂=1, Δb₃=1/3 fixed
# At Y=1/6: Δb₁ = 1/15. For general Y: Δb₁ = 1/15 * (Y/(1/6))² = 1/15 * 36Y² = 36Y²/15 = 12Y²/5

gaps = []
dists = []
for Y in Y_vals:
    db1 = 12 * Y**2 / 5
    b1_new = 41/10 + db1
    b2_new = -19/6 + 1
    b3_new = -7 + 1/3
    gap = (b1_new - b2_new) / (b2_new - b3_new)
    gaps.append(gap)
    dists.append(abs(gap - 1.358))

ax.bar(range(len(Y_vals)), dists, color=['#0F6E56'] + ['#B4B2A9']*6,
       edgecolor=['#085041'] + ['#888']*6, linewidth=1)

ax.set_xticks(range(len(Y_vals)))
ax.set_xticklabels(['1/6\n(Cabibbo\nDoublet)', '1/3', '1/2', '2/3', '5/6', '1', '7/6'], fontsize=9)
ax.set_ylabel('Distance from measured gap ratio (1.358)', fontsize=11)
ax.set_xlabel('Hypercharge Y for (3,2,Y) vector-like fermion', fontsize=11)
ax.set_title('Gap ratio distance: sharp optimum at Y = 1/6', fontsize=13, fontweight='bold')

ax.annotate(f'Distance = 0.049', xy=(0, 0.049), xytext=(1.5, 0.15),
            fontsize=11, fontweight='bold', color='#0F6E56',
            arrowprops=dict(arrowstyle='->', color='#0F6E56', lw=1.5))

# SM gap ratio distance for reference
ax.axhline(y=0.538, color='#A32D2D', linestyle='--', linewidth=0.8, alpha=0.5)
ax.text(4.5, 0.55, 'SM distance (0.538)', fontsize=8, color='#A32D2D')

ax.set_ylim(0, 0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('fig6_y16_asymmetry.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure 6 saved: fig6_y16_asymmetry.png")
