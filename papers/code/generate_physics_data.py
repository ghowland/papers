#!/usr/bin/env python3
"""
CKS K-Space Physics – exhaustive data generator
Produces CSV + human tables for *every* derived quantity.
Readers can grep/plot the CSV files directly.
"""

import os
from mpmath import mp, mpf, nstr
import kspace_physics as ksp

mp.dps = 15
OUT_DIR = "data"
os.makedirs(OUT_DIR, exist_ok=True)


# ----------  epoch grid  ----------------------------------------------------
epochs = {
    "early":  mpf('1.0e29'),      # N ≈ 3×10⁵⁸
    "today":  ksp.current_epoch_M(),
    "late":   mpf('5.0e30'),       # N ≈ 7.5×10⁶¹
}


# ----------  CSV writers  ----------------------------------------------------
def write_csv(filename, header, rows):
    with open(f"{OUT_DIR}/{filename}", "w") as f:
        f.write("# " + "\t".join(header) + "\n")
        for row in rows:
            f.write("\t".join(map(str, row)) + "\n")


# ----------  1.  Electromagnetic sector  -------------------------------------
def gen_em():
    header = ["epoch", "M", "N", "alpha_inv", "alpha", "g_factor"]
    rows = []
    for label, M in epochs.items():
        N = ksp.N_from_M(M)
        a_inv = ksp.SI_alpha_inv(M)
        a = ksp.SI_alpha(M)
        g = ksp.SI_g_electron(M)
        rows.append([label, float(M), float(N), float(a_inv), float(a), float(g)])
    write_csv("em_sector.tsv", header, rows)

    # quick human table
    print("\nElectromagnetic sector")
    for label, M in epochs.items():
        N = float(ksp.N_from_M(M))
        a_inv = float(ksp.SI_alpha_inv(M))
        g = float(ksp.SI_g_electron(M))
        print(f"{label:5s}  N={N:.2e}  α⁻¹={a_inv:.10f}  g={g:.14f}")


# ----------  2.  Lepton mass ratios  -----------------------------------------
def gen_leptons():
    header = ["epoch", "M", "mu_e", "tau_e", "proton_e"]
    rows = []
    for label, M in epochs.items():
        mu = float(ksp.SI_muon(M))
        tau = float(ksp.SI_tau(M))
        prot = float(ksp.SI_proton(M))
        rows.append([label, float(M), mu, tau, prot])
    write_csv("lepton_ratios.tsv", header, rows)

    print("\nLepton mass ratios (m_X / m_e)")
    for label, M in epochs.items():
        mu = float(ksp.SI_muon(M))
        tau = float(ksp.SI_tau(M))
        prot = float(ksp.SI_proton(M))
        print(f"{label:5s}  μ/e={mu:.6f}  τ/e={tau:.2f}  p/e={prot:.8f}")


# ----------  3.  Force couplings (natural units)  ----------------------------
def gen_forces():
    header = ["epoch", "M", "alpha_s", "alpha_w", "alpha_G"]
    rows = []
    for label, M in epochs.items():
        a_s = float(ksp.alpha_strong(M))
        a_w = float(ksp.alpha_weak(M))
        a_G = float(ksp.alpha_gravity(M))
        rows.append([label, float(M), a_s, a_w, a_G])
    write_csv("force_couplings.tsv", header, rows)

    print("\nForce couplings (natural units)")
    for label, M in epochs.items():
        a_s = float(ksp.alpha_strong(M))
        a_w = float(ksp.alpha_weak(M))
        print(f"{label:5s}  α_s={a_s:.4f}  α_w={a_w:.4f}")


# ----------  4.  Cosmological densities  -------------------------------------
def gen_cosmo():
    header = ["epoch", "M", "Omega_L", "Omega_M", "H_natural"]
    rows = []
    for label, M in epochs.items():
        O_L = float(ksp.omega_lambda(M))
        O_M = float(ksp.omega_matter(M))
        H = float(ksp.hubble_parameter_natural(M))
        rows.append([label, float(M), O_L, O_M, H])
    write_csv("cosmo_densities.tsv", header, rows)

    print("\nCosmological densities (natural units)")
    for label, M in epochs.items():
        O_L = float(ksp.omega_lambda(M))
        O_M = float(ksp.omega_matter(M))
        print(f"{label:5s}  Ω_Λ={O_L:.4f}  Ω_M={O_M:.4f}")


# ----------  5.  Vacuum quantisation  --------------------------------------
def gen_vacuum():
    header = ["epoch", "M", "delta_f_Hz"]
    rows = []
    for label, M in epochs.items():
        df = float(ksp.vacuum_quantization_unit())   # constant, but write anyway
        rows.append([label, float(M), df])
    write_csv("vacuum_quant.tsv", header, rows)

    print("\nVacuum quantisation")
    df = float(ksp.vacuum_quantization_unit())
    print(f"Δf = {df} Hz  (exact, epoch-independent)")


# ----------  6.  Sweep: α(M) fine scan  --------------------------------------
def gen_alpha_scan():
    """Fine scan of α vs M near current epoch"""
    M0 = ksp.current_epoch_M()
    dM = M0 * mpf('1e-4')
    header = ["M", "alpha_inv", "alpha"]
    rows = []
    for delta in range(-5, 6):
        M = M0 + delta * dM
        a_inv = float(ksp.SI_alpha_inv(M))
        a = float(ksp.SI_alpha(M))
        rows.append([float(M), a_inv, a])
    write_csv("alpha_scan.tsv", header, rows)

    print("\nFine scan α(M) near today (±0.05 %)")
    for delta in range(-5, 6):
        M = M0 + delta * dM
        a_inv = float(ksp.SI_alpha_inv(M))
        print(f"ΔM={delta:+2d}  α⁻¹={a_inv:.10f}")


# ----------  main  ----------------------------------------------------------
def main():
    print("CKS K-Space Physics – data generator")
    print("Output files written to ./data/")
    gen_em()
    gen_leptons()
    gen_forces()
    gen_cosmo()
    gen_vacuum()
    gen_alpha_scan()
    print("\nAll CSV files ready for plotting / inspection.")


if __name__ == '__main__':
    main()

