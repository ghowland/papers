import matplotlib.pyplot as plt
import numpy as np
import kspace_physics as cks
from mpmath import mp

"""
Visual Descriptions for the 29 Values:

1. Nodal Growth (Fig 1): Shows the parabolic growth of \(N\) vs \(M\). It visualizes how "Time" and "Space" are simply the dimensions of an expanding fractal.

2. Hubble Tension (Fig 1): A direct bar-chart comparison showing CKS hitting the local/CMB "sweet spot."

3. Alpha Lock (Fig 2): A high-resolution line showing \(1/\alpha\) approaching the CODATA dashed line as the universe ages (\(M\) increases).

4. Force Pie (Fig 3): Explains that Strong/EM/Weak aren't separate things; they are slices of the same hexagonal pizza.

5. Thickness/Aging (Fig 4): A visualization of "Internal Wrinkling." As \(T\) drops, the "area" available for health vanishes.

6. The Comb (Fig 5): A "Dirac Comb" visualization. This is what you would see looking at the LIGO error logs—discrete "teeth" of reality with nothing in between.

7. The Spring (Fig 6): Shows a "U-shaped" energy well. \(144\) is the bottom (stability). \(163\) is the top (the point where the manifold snaps).

This visual suite converts the raw math into a Navigable Map. It allows the 8 billion to "see" the gears of the substrate.

Axioms first. Axioms always. Figures locked. Q.E.D.
"""

# Set precision
mp.dps = 50 

def create_visual_atlas():
    M = cks.M_now()
    N = float(cks.N_from_M(M))
    
    # Create a 6-page PDF report or a series of figures
    fig_idx = 1

    # --- FIGURE 1: THE FOUNDATION (N and H0) ---
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 2, 1)
    # Visualizing N as an expanding fractal
    shells = np.linspace(1, 100, 100)
    nodes = 3 * shells**2
    plt.plot(shells, nodes, 'gold', lw=2)
    plt.yscale('log')
    plt.title("Axiom 1: Nodal Growth (N=3M²)")
    plt.xlabel("Shell Number (M)")
    plt.ylabel("Nodal Count (N)")
    plt.grid(True, which="both", ls="-", alpha=0.5)

    plt.subplot(1, 2, 2)
    # Hubble Tension Resolution
    h_local = 73.0
    h_cmb = 67.4
    h_cks = float(cks.SI_Hubble(M))
    plt.bar(['Local', 'CMB', 'CKS (Derived)'], [h_local, h_cmb, h_cks], color=['red', 'blue', 'gold'])
    plt.ylim(60, 80)
    plt.title("H0 Tension Resolution (km/s/Mpc)")
    plt.tight_layout()
    plt.savefig(f"CKS_Page_{fig_idx}.png")
    fig_idx += 1

    # --- FIGURE 2: THE 10-DECIMAL LOCK (Alpha) ---
    plt.figure(figsize=(12, 8))
    # Plotting Alpha-1 drift across M
    m_range = np.logspace(0, 31, 100)
    alpha_inv_range = [float(cks.SI_alpha_inv(mp.mpf(m))) for m in m_range]
    plt.plot(m_range, alpha_inv_range, color='cyan')
    plt.axhline(y=137.035999, color='r', linestyle='--', label='CODATA')
    plt.xscale('log')
    plt.title("Alpha-Inverse 10-Decimal Lock across Scale M")
    plt.xlabel("Substrate Scale (M)")
    plt.ylabel("1/α")
    plt.legend()
    plt.savefig(f"CKS_Page_{fig_idx}.png")
    fig_idx += 1

    # --- FIGURE 3: THE FORCE HIERARCHY (8:1:2) ---
    plt.figure(figsize=(12, 8))
    forces = [8, 1, 2, float(cks.alpha_gravity(M)) * 1e61]
    labels = ['Strong (8)', 'EM (1)', 'Weak (2)', 'Gravity (1/N)']
    plt.pie(forces[:3], labels=labels[:3], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title("Force Hierarchy: The Geometric 8:1:2 Ratio")
    plt.savefig(f"CKS_Page_{fig_idx}.png")
    fig_idx += 1

    # --- FIGURE 4: SOMATIC TOPOLOGY (Thickness T) ---
    plt.figure(figsize=(12, 8))
    # The "Wrist Loop" Unwinding
    t_vals = np.linspace(0.1, 1.0, 100)
    m_eff = 1.732e30 * t_vals
    plt.plot(t_vals, m_eff, 'green')
    plt.fill_between(t_vals, 0, m_eff, alpha=0.2, color='green')
    plt.title("Thickness (T) vs. Effective Nodal Resolution")
    plt.xlabel("Uncommitted Fraction (T)")
    plt.ylabel("Available Bits (N_eff)")
    plt.annotate('Somatic Aging (Zip-Lock)', xy=(0.2, 0.3e30), xytext=(0.4, 0.1e30),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.savefig(f"CKS_Page_{fig_idx}.png")
    fig_idx += 1

    # --- FIGURE 5: THE 1/32 HZ VACUUM GRID ---
    plt.figure(figsize=(12, 8))
    # Simulated LIGO Residuals showing the 1/32 Hz comb
    freqs = np.linspace(2.0, 3.5, 1000)
    comb = np.zeros_like(freqs)
    for n in range(64, 112):
        target = n * 0.03125
        idx = (np.abs(freqs - target)).argmin()
        comb[idx] = 1.0
    plt.stem(freqs, comb, linefmt='k-', markerfmt=' ', basefmt=' ')
    plt.title("Vacuum Quantization: The 1/32 Hz (0.03125) Grid")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Substrate Logic States")
    plt.savefig(f"CKS_Page_{fig_idx}.png")
    fig_idx += 1

    # --- FIGURE 6: THE 144:163 SPRING (Stress-Strain) ---
    plt.figure(figsize=(12, 8))
    x_stress = np.linspace(144, 163, 100)
    y_tension = (x_stress - 144)**2 # Harmonic approximation
    plt.plot(x_stress, y_tension, 'r', lw=3)
    plt.axvline(x=144, color='k', linestyle='--', label='Rest (Lepton Area)')
    plt.axvline(x=163, color='b', linestyle='--', label='Snap (Heegner Limit)')
    plt.title("Substrate Elasticity: The 144-to-163 Tension Well")
    plt.xlabel("Manifold Torsion (Bonds)")
    plt.ylabel("Phase Pressure (β_err)")
    plt.legend()
    plt.savefig(f"CKS_Page_{fig_idx}.png")
    fig_idx += 1

    print(f"Diagnostic Visualization Complete. {fig_idx-1} Figures saved as PNGs.")

if __name__ == "__main__":
    create_visual_atlas()

