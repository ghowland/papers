import matplotlib.pyplot as plt
import numpy as np
import kspace_physics as cks
from mpmath import mp

"""

How to use the Four-Quadrant Atlas:

1. Top-Left (K-Space Hardware): This is the Reality of the Machine. It shows how the phase tension (\(\beta\)) dilutes purely as a function of the count \(N\). There is no "Physics" here, only Lattice Dynamics.

2. Top-Right (X-Space Software): This is the Holographic Projection. It shows how the "Forces" (like \(\alpha_{em}\)) emerge as the lattice grows. This is where the 12-bond loop starts to look like an electron.

3. Bottom-Left (The SI Bridge - Planck/THz): This is the Temporal Gearbox. It bridges the "Planck Tick" to the "Substrate Pulse." It explains why the substrate vibrates in the Terahertz range—it is the "Clock Speed" of the computer.

4. Bottom-Right (The Human Reality - SI Hz): This is the End-User Interface. It shows the 1.000s Second and the 2.1875 Hz carrier. This is where the 8 billion live. It proves that our "Seconds" and "Hertz" are just specific harmonics of the \(N \approx 9 \times 10^{60}\) epoch.

The Educational "Aha!" Moment:


By showing these four together, you eliminate the confusion between "Planck Units" and "SI Units."


- K-Space is the code.

- X-Space is the render.

- SI Units are just the zoom level we currently occupy.

Axioms first. Axioms always. The mapping is complete. Q.E.D.

"""

# Set precision
mp.dps = 50

def generate_coordinate_atlas():
    M_now = cks.M_now()
    # Range of M to show evolution (Early Universe to Now)
    m_range = np.logspace(10, 31, 100)
    
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    plt.subplots_adjust(hspace=0.3, wspace=0.3)

    # ------------------------------------------------------------------
    # FIGURE 1: K-SPACE (PURE SUBSTRATE)
    # Units: Phase Tension (β) / Bubble Count (N)
    # ------------------------------------------------------------------
    ax = axs[0, 0]
    n_vals = [float(cks.N_from_M(mp.mpf(m))) for m in m_range]
    beta_dilution = [2 * np.pi / n for n in n_vals]
    ax.plot(n_vals, beta_dilution, color='lime', lw=2)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title("1. K-SPACE (The Hardware)\nMetric: Phase Tension Dilution (β/N)")
    ax.set_xlabel("Bubble Count (N)")
    ax.set_ylabel("Local Tension β")
    ax.grid(True, alpha=0.3)
    ax.annotate('Axiom 2: Total β=2π', xy=(1e20, 1e-20), color='lime')

    # ------------------------------------------------------------------
    # FIGURE 2: X-SPACE (THE HOLOGRAM)
    # Units: Coupling Constants (α) / Normalized to N
    # ------------------------------------------------------------------
    ax = axs[0, 1]
    alpha_vals = [float(cks.alpha_em(mp.mpf(m))) for m in m_range]
    ax.plot(m_range, alpha_vals, color='gold', lw=2)
    ax.set_xscale('log')
    ax.set_title("2. X-SPACE (The Software)\nMetric: Coupling Evolution α_em(M)")
    ax.set_xlabel("Scale (M)")
    ax.set_ylabel("Force Strength α")
    ax.grid(True, alpha=0.3)
    ax.annotate('Emergent Physics', xy=(1e15, 0.007), color='orange')

    # ------------------------------------------------------------------
    # FIGURE 3: K-SPACE WITH SI BRIDGE (The "Xi" Problem)
    # Units: Frequency (THz) / Planck Units
    # ------------------------------------------------------------------
    ax = axs[1, 0]
    # Substrate THz heartbeat vs Planck Time
    f_sub = [float(cks.substrate_frequency(mp.mpf(m))) for m in m_range]
    ax.plot(m_range, f_sub, color='magenta', lw=2)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_title("3. K-SPACE + SI BRIDGE\nMetric: Substrate Pulse Frequency (THz)")
    ax.set_xlabel("Scale (M)")
    ax.set_ylabel("Frequency (THz)")
    ax.grid(True, alpha=0.3)
    ax.axhline(y=float(cks.substrate_frequency(M_now)), color='white', ls=':', alpha=0.5)
    ax.annotate(f'Current: {float(cks.substrate_frequency(M_now)):.2f} THz', 
                xy=(1e25, 10), color='magenta')

    # ------------------------------------------------------------------
    # FIGURE 4: X-SPACE WITH SI BRIDGE (Physical Reality)
    # Units: Seconds / Meters / kg / CODATA
    # ------------------------------------------------------------------
    ax = axs[1, 1]
    # The 1/32 Hz Grid reference
    step = float(cks.vacuum_quantization_unit())
    # Carrier frequency across scales
    f_car = [float(cks.holographic_carrier_frequency(mp.mpf(m))) for m in m_range]
    ax.plot(m_range, f_car, color='cyan', lw=2)
    ax.axhline(y=2.1875, color='r', ls='--', label='2.1875 Hz Lock')
    ax.set_xscale('log')
    ax.set_title("4. X-SPACE + SI BRIDGE\nMetric: Holographic Carrier (Hz)")
    ax.set_xlabel("Scale (M)")
    ax.set_ylabel("Frequency (Hz)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.annotate('The "Second" is Born', xy=(1e28, 2.5), color='cyan')

    plt.suptitle("CKS COORDINATE MAPPING: FROM SUBSTRATE TO SI REALITY", size=20)
    plt.savefig("CKS_Coordinate_Mapping.png", dpi=300)
    print("Four-Quadrant Atlas Generated: CKS_Coordinate_Mapping.png")

if __name__ == "__main__":
    generate_coordinate_atlas()

