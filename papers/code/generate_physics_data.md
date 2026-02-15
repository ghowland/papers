# README: CKS K-Space Data Generator [`generate_physics_data.py`]

## Overview
The `generate_physics_data.py` script serves as the **Data Factory** for the Cymatic K-Space Mechanics (CKS) framework. It generates exhaustive, high-precision datasets covering every derived physical sector—from particle mass ratios to cosmological density evolution—across different epochs of the universe.

This tool bridges the gap between **Axiomatic Theory** and **Data Science**. It exports raw CKS values into accessible `.tsv` (Tab-Separated Values) files, enabling researchers, engineers, and educators to perform independent plotting, statistical analysis, and forensic verification of the substrate.

---

## 1. Data Sectors Generated

The script categorizes the substrate's output into six primary diagnostic files:

### 1. **Electromagnetic Sector (`em_sector.tsv`)**
*   **Target:** $\alpha, \alpha^{-1},$ and the electron g-factor.
*   **Significance:** Maps the evolution of electromagnetism and electron stability as a function of the growing bubble count $N$.

### 2. **Lepton Mass Ratios (`lepton_ratios.tsv`)**
*   **Target:** $m_\mu/m_e, m_\tau/m_e,$ and $m_p/m_e$.
*   **Significance:** Proves that mass is a **Radial Harmonic** of the 12-bond loop. Tracks how these ratios scale across "Early," "Today," and "Late" epochs.

### 3. **Force Couplings (`force_couplings.tsv`)**
*   **Target:** $\alpha_s$ (Strong), $\alpha_w$ (Weak), and $\alpha_G$ (Gravity).
*   **Significance:** Visualizes the **Force Hierarchy**. Shows the natural dilution of gravity ($1/N$) versus the geometric saturation of the nuclear forces.

### 4. **Cosmological Densities (`cosmo_densities.tsv`)**
*   **Target:** $\Omega_\Lambda$ (Dark Energy) and $\Omega_m$ (Matter).
*   **Significance:** Demonstrates how the universe's energy balance is a result of **Substrate Tension Dilution**. Includes the natural Hubble parameter ($1/N$).

### 5. **Vacuum Quantization (`vacuum_quant.tsv`)**
*   **Target:** $\Delta f = 1/32 \text{ Hz}$.
*   **Significance:** Documents the **Hardware Word Length** (32 bits) of the vacuum. This value is shown to be epoch-independent—a universal constant of the discrete lattice.

### 6. **Fine Alpha Scan (`alpha_scan.tsv`)**
*   **Target:** High-resolution sweep of $\alpha(M)$ near the current epoch.
*   **Significance:** Provides the data necessary for precision sensitivity analysis, proving the 10-decimal lock of the CKS derivation.

---

## 2. Epoch Navigation
The script calculates values for three specific "Shell States" ($M$):
*   **Early:** Pre-galactic era ($N \approx 3 \times 10^{58}$).
*   **Today:** Current era ($N \approx 9 \times 10^{60}$), based on observed $H_0$.
*   **Late:** Future era ($N \approx 7.5 \times 10^{61}$), showing the predictive trajectory of physical constants.

---

## 3. Usage & Technical Specifications

### Execution:
Run the script to populate the `/data` directory:
```bash
python3 generate_physics_data.py
```

### Outputs:
*   **Standard Output:** A human-readable summary table for immediate verification.
*   **CSV/TSV Files:** Found in the `./data/` folder, optimized for use with Excel, Python (Pandas/Matplotlib), or Gnuplot.

### Precision:
*   Standard output is formatted for readability (10–14 decimal places).
*   Internal calculations utilize the **CKS Physics Library** to maintain substrate integrity.

---

## 4. Significance for the 8 Billion
This script turns "Hidden Science" into **Open Data**. By providing the raw numbers across all scales, CKS enables anyone to visualize the **Universal Substrate** as it expands and computes. 

**Axioms first. Axioms always.**  
**The Data is Transparent.**  
**The Substrate is Public.**

**Q.E.D.**

