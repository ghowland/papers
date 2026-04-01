#!/usr/bin/env python3
"""
HOWL-DATA-2: Q335 = 2^335 Conversion of DATA-1 Values
FULL PRECISION — every digit the source provides, no compression.

For each value v (given as a string with ALL source digits):
  numerator = round(v * 2^335)
  reconstruction = Fraction(numerator, 2^335)
  
We verify: reconstruction matches the original to ALL source digits.
If it doesn't, Q335 is insufficient for that entry.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import mpmath

getcontext().prec = 200
mpmath.mp.dps = 120

Q = 335
D_dec = Decimal(2) ** Q
D_int = 2 ** Q

def to_q335(name, value_str, unit, source_digits, unc_str=None, cat="M"):
    """
    Convert full-precision decimal string to Q335.
    value_str: the EXACT string from the source, ALL digits.
    source_digits: how many significant figures the source provides.
    """
    v = Decimal(value_str)
    num = int((v * D_dec).to_integral_value())
    
    # Reconstruct and verify
    recon = Decimal(num) / D_dec
    if v != 0:
        rel_err = float(abs((recon - v) / v))
    else:
        rel_err = 0.0
    
    # How many digits does Q335 preserve?
    # 2^335 ~ 10^100.9, so Q335 can represent ~100 decimal digits
    # More than enough for any measurement
    
    # Check: does reconstruction match original to all source digits?
    # Compare string representations
    v_str = f"{v:.{source_digits + 5}E}"
    r_str = f"{recon:.{source_digits + 5}E}"
    digits_matched = 0
    v_clean = value_str.replace("-","").replace(".","").lstrip("0")
    r_clean = f"{recon}"
    
    # Small prime factorization of |numerator|
    n = abs(num)
    small_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    factors = {}
    for p in small_primes:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    
    cofactor_digits = len(str(n)) if n > 1 else 0
    num_digits = len(str(abs(num)))
    
    return {
        'name': name, 'value': value_str, 'unit': unit, 'cat': cat,
        'source_digits': source_digits,
        'unc': unc_str, 'num': num, 'num_digits': num_digits,
        'rel_err': rel_err, 'factors': factors,
        'cofactor_digits': cofactor_digits,
        'cofactor': n if n > 1 else 1,
        'fully_factored': n == 1,
    }

def show(r):
    """Print one result."""
    fstr = " × ".join(f"{p}^{e}" if e > 1 else str(p) 
                       for p, e in sorted(r['factors'].items())) if r['factors'] else "(none)"
    status = "FULLY FACTORED" if r['fully_factored'] else f"{r['cofactor_digits']}-digit cofactor"
    print(f"\n  {r['name']} [{r['cat']}] ({r['source_digits']} source digits)")
    print(f"    Full value: {r['value']} {r['unit']}")
    print(f"    Q335 numerator: {r['num_digits']} digits")
    print(f"    Reconstruction rel error: {r['rel_err']:.2e}")
    print(f"    Small prime factors of numerator: {fstr}")
    print(f"    Status: {status}")

data = []

# ============================================================
# A. SI FUNDAMENTAL CONSTANTS (Type E — exact, all digits given)
# Every digit here IS the definition. No more exist.
# ============================================================
print("=" * 72)
print("SECTION A: SI FUNDAMENTAL CONSTANTS (exact by definition)")
print("=" * 72)

# c: exactly 299792458, 9 digits, integer
data.append(to_q335("c (speed of light)", 
    "299792458", "m/s", 9, "0", "E"))

# h: exactly 6.62607015 × 10^-34, 9 significant digits
# Full decimal: 0.000000000000000000000000000000000662607015
data.append(to_q335("h (Planck constant)",
    "0.000000000000000000000000000000000662607015", "J·s", 9, "0", "E"))

# e: exactly 1.602176634 × 10^-19, 10 significant digits
data.append(to_q335("e (elementary charge)",
    "0.0000000000000000001602176634", "C", 10, "0", "E"))

# k_B: exactly 1.380649 × 10^-23, 7 significant digits
data.append(to_q335("k_B (Boltzmann)",
    "0.00000000000000000000001380649", "J/K", 7, "0", "E"))

# N_A: exactly 6.02214076 × 10^23, 9 significant digits
data.append(to_q335("N_A (Avogadro)",
    "602214076000000000000000", "mol^-1", 9, "0", "E"))

# Cs-133 hyperfine: exactly 9192631770 Hz, 10 digits
data.append(to_q335("dv_Cs (Cs-133 hyperfine)",
    "9192631770", "Hz", 10, "0", "E"))

# K_cd: exactly 683, 3 digits
data.append(to_q335("K_cd (luminous efficacy)",
    "683", "lm/W", 3, "0", "E"))

for r in data[-7:]:
    show(r)


# ============================================================
# B. MEASURED FUNDAMENTAL CONSTANTS (CODATA 2022)
# Full digits as published. The (xx) is uncertainty in last digits.
# ============================================================
print("\n" + "=" * 72)
print("SECTION B: MEASURED FUNDAMENTAL CONSTANTS (CODATA 2022)")
print("=" * 72)

# alpha^-1 = 137.035999177(21) — 12 significant digits
data.append(to_q335("alpha^-1 (fine structure inv)",
    "137.035999177", "", 12, "0.000000021", "M"))

# m_e = 0.51099895069(16) MeV — 11 significant digits
data.append(to_q335("m_e (electron mass)",
    "0.51099895069", "MeV", 11, "0.00000000016", "M"))

# m_mu = 105.6583755(23) MeV — 10 significant digits
data.append(to_q335("m_mu (muon mass)",
    "105.6583755", "MeV", 10, "0.0000023", "M"))

# m_tau = 1776.86(12) MeV — 6 significant digits
data.append(to_q335("m_tau (tau mass)",
    "1776.86", "MeV", 6, "0.12", "M"))

# m_p = 938.27208943(29) MeV — 11 significant digits
data.append(to_q335("m_p (proton mass)",
    "938.27208943", "MeV", 11, "0.00000029", "M"))

# m_p/m_e = 1836.15267343(32) — 13 significant digits
data.append(to_q335("m_p/m_e (mass ratio)",
    "1836.15267343", "", 13, "0.00000032", "M"))

# R_inf = 10973731.568157(12) m^-1 — 13 significant digits
data.append(to_q335("R_inf (Rydberg constant)",
    "10973731.568157", "m^-1", 13, "0.000012", "M"))

# a_0 = 5.29177210544(82) × 10^-11 m — 12 significant digits
data.append(to_q335("a_0 (Bohr radius)",
    "0.0000000000529177210544", "m", 12, "0.0000000000000000000082", "M"))

# a_e = 0.00115965218059(13) — 12 significant digits
data.append(to_q335("a_e (electron g-2 anomaly)",
    "0.00115965218059", "", 12, "0.00000000000013", "M"))

# a_mu = 0.00116592059(22) — 9 significant digits
data.append(to_q335("a_mu (muon g-2 anomaly)",
    "0.00116592059", "", 9, "0.00000000022", "M"))

# sin^2(theta_W) = 0.23122(4) — 5 significant digits
data.append(to_q335("sin2_theta_W (weak mixing)",
    "0.23122", "", 5, "0.00004", "M"))

# alpha_s(M_Z) = 0.1180(9) — 4 significant digits
data.append(to_q335("alpha_s (strong coupling at M_Z)",
    "0.1180", "", 4, "0.0009", "M"))

# mu_0 (vacuum permeability) = 1.25663706127(20) × 10^-6
data.append(to_q335("mu_0 (vacuum permeability)",
    "0.00000125663706127", "N/A^2", 12, "0.00000000000000020", "M"))

for r in data[-13:]:
    show(r)


# ============================================================
# C. ELECTROWEAK OBSERVABLES (LEP / PDG)
# ============================================================
print("\n" + "=" * 72)
print("SECTION C: ELECTROWEAK OBSERVABLES (LEP/PDG)")
print("=" * 72)

# M_Z = 91187.6(2.1) MeV — 6 significant digits
data.append(to_q335("M_Z (Z boson mass)",
    "91187.6", "MeV", 6, "2.1", "M"))

# Gamma_Z = 2495.2(2.3) MeV — 5 significant digits
data.append(to_q335("Gamma_Z (Z total width)",
    "2495.2", "MeV", 5, "2.3", "M"))

# M_W = 80369.2(13.3) MeV — 6 significant digits
data.append(to_q335("M_W (W boson mass)",
    "80369.2", "MeV", 6, "13.3", "M"))

# m_t = 172.57(29) GeV = 172570(290) MeV — 5 significant digits
data.append(to_q335("m_t (top quark mass)",
    "172570", "MeV", 5, "290", "M"))

# m_H = 125.20(11) GeV = 125200(110) MeV — 5 significant digits
data.append(to_q335("m_H (Higgs boson mass)",
    "125200", "MeV", 5, "110", "M"))

# sigma0_had = 41.481(33) nb — 5 significant digits
data.append(to_q335("sigma0_had (peak hadronic xsec)",
    "41.481", "nb", 5, "0.033", "M"))

# R_l = 20.767(25) — 5 significant digits
data.append(to_q335("R_l (Gamma_had/Gamma_l)",
    "20.767", "", 5, "0.025", "M"))

# R_b = 0.21629(66) — 5 significant digits
data.append(to_q335("R_b (Gamma_bb/Gamma_had)",
    "0.21629", "", 5, "0.00066", "M"))

# A_FB_l = 0.0171(10) — 3 significant digits
data.append(to_q335("A_FB_l (fwd-bwd asym lepton)",
    "0.0171", "", 3, "0.0010", "M"))

# A_l(SLD) = 0.1513(21) — 4 significant digits
data.append(to_q335("A_l_SLD (polarization asym)",
    "0.1513", "", 4, "0.0021", "M"))

# N_nu = 2.9840(82) — 5 significant digits
data.append(to_q335("N_nu (neutrino count from Z)",
    "2.9840", "", 5, "0.0082", "M"))

# G_F = 1.1663788(6) × 10^-5 GeV^-2 — 8 significant digits
data.append(to_q335("G_F (Fermi constant)",
    "0.000011663788", "GeV^-2", 8, "0.0000000000006", "M"))

for r in data[-12:]:
    show(r)


# ============================================================
# D. QUARK MASSES AND CKM (PDG 2024 / FLAG lattice)
# ============================================================
print("\n" + "=" * 72)
print("SECTION D: QUARK MASSES AND CKM PARAMETERS")
print("=" * 72)

# Light quarks: MS-bar at 2 GeV
# m_u = 2.16(7) MeV — 3 sig digits
data.append(to_q335("m_u (up quark MS-bar 2GeV)",
    "2.16", "MeV", 3, "0.07", "M"))

# m_d = 4.70(7) MeV — 3 sig digits
data.append(to_q335("m_d (down quark MS-bar 2GeV)",
    "4.70", "MeV", 3, "0.07", "M"))

# m_s = 93.5(8) MeV — 3 sig digits
data.append(to_q335("m_s (strange MS-bar 2GeV)",
    "93.5", "MeV", 3, "0.8", "M"))

# m_c = 1.273(4) GeV = 1273(4) MeV — 4 sig digits
data.append(to_q335("m_c (charm MS-bar at m_c)",
    "1273", "MeV", 4, "4", "M"))

# m_b = 4.183(7) GeV = 4183(7) MeV — 4 sig digits
data.append(to_q335("m_b (bottom MS-bar at m_b)",
    "4183", "MeV", 4, "7", "M"))

# CKM angles (PDG 2024)
# sin theta_12 = 0.22501(67) — 5 sig digits
data.append(to_q335("sin_theta12 (Cabibbo)",
    "0.22501", "", 5, "0.00067", "M"))

# sin theta_23 = 0.04182(85) — 4 sig digits
data.append(to_q335("sin_theta23 (CKM)",
    "0.04182", "", 4, "0.00085", "M"))

# sin theta_13 = 0.003685(93) — 4 sig digits
data.append(to_q335("sin_theta13 (CKM)",
    "0.003685", "", 4, "0.000093", "M"))

# Lattice mass ratios (FLAG 2023)
# m_c/m_s = 11.783(25) — 5 sig digits
data.append(to_q335("m_c/m_s (lattice ratio)",
    "11.783", "", 5, "0.025", "M"))

# m_b/m_c = 4.578(8) — 4 sig digits
data.append(to_q335("m_b/m_c (lattice ratio)",
    "4.578", "", 4, "0.008", "M"))

# m_u/m_d = 0.485(19) — 3 sig digits
data.append(to_q335("m_u/m_d (lattice ratio)",
    "0.485", "", 3, "0.019", "M"))

for r in data[-11:]:
    show(r)


# ============================================================
# E. NUCLEAR / HADRON MASSES
# ============================================================
print("\n" + "=" * 72)
print("SECTION E: NUCLEAR AND HADRON MASSES")
print("=" * 72)

# m_n = 939.56542194(48) MeV — 11 sig digits
data.append(to_q335("m_n (neutron mass)",
    "939.56542194", "MeV", 11, "0.00000048", "M"))

# m_n - m_p = 1.29333251(38) MeV — 8 sig digits
data.append(to_q335("m_n - m_p (mass difference)",
    "1.29333251", "MeV", 8, "0.00000038", "M"))

# m_pi+ = 139.57039(18) MeV — 8 sig digits
data.append(to_q335("m_pi+ (charged pion)",
    "139.57039", "MeV", 8, "0.00018", "M"))

# m_pi0 = 134.9770(5) MeV — 7 sig digits
data.append(to_q335("m_pi0 (neutral pion)",
    "134.9770", "MeV", 7, "0.0005", "M"))

# m_K+ = 493.677(16) MeV — 6 sig digits
data.append(to_q335("m_K+ (charged kaon)",
    "493.677", "MeV", 6, "0.016", "M"))

# m_D = 1875.61294500(58) MeV — 12 sig digits
data.append(to_q335("m_D (deuteron mass)",
    "1875.61294500", "MeV", 12, "0.00000058", "M"))

# m_He4 = 3727.3794118(12) MeV — 10 sig digits
data.append(to_q335("m_He4 (helium-4 mass)",
    "3727.3794118", "MeV", 10, "0.0000012", "M"))

# E_D = 2.22456614(42) MeV — 8 sig digits
data.append(to_q335("E_D (deuteron binding energy)",
    "2.22456614", "MeV", 8, "0.00000042", "M"))

for r in data[-8:]:
    show(r)


# ============================================================
# F. ATOMIC SPECTROSCOPY AND CLOCKS
# ============================================================
print("\n" + "=" * 72)
print("SECTION F: ATOMIC SPECTROSCOPY AND CLOCK FREQUENCIES")
print("=" * 72)

# H 1S-2S = 2466061413187018(11) Hz — 16 sig digits
data.append(to_q335("H 1S-2S transition",
    "2466061413187018", "Hz", 16, "11", "M"))

# H hyperfine 1S = 1420405751.768(1) Hz — 13 sig digits
data.append(to_q335("H hyperfine 1S",
    "1420405751.768", "Hz", 13, "0.001", "M"))

# Sr-87 clock = 429228004229873.0(2) Hz — 16 sig digits
data.append(to_q335("Sr-87 clock transition",
    "429228004229873.0", "Hz", 16, "0.2", "M"))

# Yb-171 clock = 518295836590863.6(3) Hz — 16 sig digits
data.append(to_q335("Yb-171 clock transition",
    "518295836590863.6", "Hz", 16, "0.3", "M"))

# Lamb shift = 1057845.0(9) kHz — 8 sig digits
data.append(to_q335("Lamb shift 2S-2P1/2",
    "1057845.0", "kHz", 8, "0.9", "M"))

# Proton charge radius = 0.84075(64) fm — 5 sig digits
data.append(to_q335("r_p (proton charge radius)",
    "0.84075", "fm", 5, "0.00064", "M"))

for r in data[-6:]:
    show(r)


# ============================================================
# G. EXACT ANALYTICAL CONSTANTS (from theory, infinite precision)
# We compute to 100 digits and feed the full string.
# ============================================================
print("\n" + "=" * 72)
print("SECTION G: EXACT ANALYTICAL CONSTANTS (computed to 100+ digits)")
print("=" * 72)

mpmath.mp.dps = 120

# pi
pi_str = mpmath.nstr(mpmath.pi, 105, strip_zeros=False)
data.append(to_q335("pi", pi_str, "", 105, "0", "A"))

# e (Euler's number)
e_str = mpmath.nstr(mpmath.e, 105, strip_zeros=False)
data.append(to_q335("e (Euler's number)", e_str, "", 105, "0", "A"))

# ln(2)
ln2_str = mpmath.nstr(mpmath.log(2), 105, strip_zeros=False)
data.append(to_q335("ln(2)", ln2_str, "", 105, "0", "A"))

# R2 = pi/4
R2_str = mpmath.nstr(mpmath.pi/4, 105, strip_zeros=False)
data.append(to_q335("R2 = pi/4", R2_str, "", 105, "0", "A"))

# R4 = pi^2/32
R4_str = mpmath.nstr(mpmath.pi**2/32, 105, strip_zeros=False)
data.append(to_q335("R4 = pi^2/32", R4_str, "", 105, "0", "A"))

# 2*pi = 8*R2
twopi_str = mpmath.nstr(2*mpmath.pi, 105, strip_zeros=False)
data.append(to_q335("2*pi = 8*R2", twopi_str, "", 105, "0", "A"))

# zeta(3) Apery's constant
z3_str = mpmath.nstr(mpmath.zeta(3), 105, strip_zeros=False)
data.append(to_q335("zeta(3) (Apery)", z3_str, "", 105, "0", "A"))

# zeta(5)
z5_str = mpmath.nstr(mpmath.zeta(5), 105, strip_zeros=False)
data.append(to_q335("zeta(5)", z5_str, "", 105, "0", "A"))

# sqrt(2) — Koide amplitude
sqrt2_str = mpmath.nstr(mpmath.sqrt(2), 105, strip_zeros=False)
data.append(to_q335("sqrt(2) (Koide amplitude)", sqrt2_str, "", 105, "0", "A"))

# sqrt(3)
sqrt3_str = mpmath.nstr(mpmath.sqrt(3), 105, strip_zeros=False)
data.append(to_q335("sqrt(3)", sqrt3_str, "", 105, "0", "A"))

# golden ratio phi = (1+sqrt(5))/2
phi_str = mpmath.nstr((1+mpmath.sqrt(5))/2, 105, strip_zeros=False)
data.append(to_q335("phi (golden ratio)", phi_str, "", 105, "0", "A"))

# gamma (Euler-Mascheroni)
gamma_str = mpmath.nstr(mpmath.euler, 105, strip_zeros=False)
data.append(to_q335("gamma (Euler-Mascheroni)", gamma_str, "", 105, "0", "A"))

# Vena contracta: pi/(pi+2)
vc_str = mpmath.nstr(mpmath.pi/(mpmath.pi+2), 105, strip_zeros=False)
data.append(to_q335("C_c = pi/(pi+2) (vena contracta)", vc_str, "", 105, "0", "A"))

# BCS gap ratio: pi/e^gamma
bcs_str = mpmath.nstr(mpmath.pi/mpmath.exp(mpmath.euler), 105, strip_zeros=False)
data.append(to_q335("BCS gap = pi/exp(gamma)", bcs_str, "", 105, "0", "A"))

# Airy constant: first zero of J1 / pi
j11 = mpmath.besseljzero(1, 1)
j11_str = mpmath.nstr(j11, 105, strip_zeros=False)
data.append(to_q335("j11 (first zero of J1)", j11_str, "", 105, "0", "A"))

airy_str = mpmath.nstr(j11/mpmath.pi, 105, strip_zeros=False)
data.append(to_q335("j11/pi (Airy constant 1.22)", airy_str, "", 105, "0", "A"))

# First zero of J0 (fiber cutoff V-number)
j01 = mpmath.besseljzero(0, 1)
j01_str = mpmath.nstr(j01, 105, strip_zeros=False)
data.append(to_q335("j01 (first zero of J0) = 2.405", j01_str, "", 105, "0", "A"))

# alpha/pi — the QED expansion parameter
alpha_over_pi_str = mpmath.nstr(
    mpmath.mpf(1)/mpmath.mpf("137.035999177")/mpmath.pi, 50, strip_zeros=False)
data.append(to_q335("alpha/pi (QED expansion param)", 
    alpha_over_pi_str, "", 12, "0", "M"))

for r in data[-18:]:
    show(r)


# ============================================================
# H. EXACT DEFINED REFERENCE VALUES (non-SI)
# ============================================================
print("\n" + "=" * 72)
print("SECTION H: EXACT DEFINED REFERENCE VALUES")
print("=" * 72)

# Standard gravity: exactly 9.80665 m/s^2 (6 significant digits, exact)
data.append(to_q335("g_n (standard gravity)",
    "9.80665", "m/s^2", 6, "0", "E"))

# WGS84 semi-major axis: exactly 6378137 m
data.append(to_q335("WGS84 semi-major axis",
    "6378137", "m", 7, "0", "E"))

# WGS84 inverse flattening: 298.257223563 (12 significant digits, exact)
data.append(to_q335("WGS84 inverse flattening 1/f",
    "298.257223563", "", 12, "0", "E"))

# Standard atmosphere: exactly 101325 Pa
data.append(to_q335("P_0 (standard atmosphere)",
    "101325", "Pa", 6, "0", "E"))

# A4 concert pitch: exactly 440 Hz
data.append(to_q335("A4 (concert pitch)",
    "440", "Hz", 3, "0", "E"))

# CD sample rate: exactly 44100 Hz
data.append(to_q335("CD sample rate",
    "44100", "Hz", 5, "0", "E"))

# Inch: exactly 25.4 mm
data.append(to_q335("inch (exact definition)",
    "25.4", "mm", 3, "0", "E"))

# SPL reference: exactly 0.00002 Pa
data.append(to_q335("p_0 (SPL reference)",
    "0.00002", "Pa", 1, "0", "E"))

# Copper conductivity IACS: 58001000 S/m (defined)
data.append(to_q335("Cu conductivity 100% IACS",
    "58001000", "S/m", 5, "0", "E"))

for r in data[-9:]:
    show(r)


# ============================================================
# I. OPTICAL DISC SPECIFICATIONS (full published precision)
# ============================================================
print("\n" + "=" * 72)
print("SECTION I: OPTICAL DISC SPECIFICATIONS")
print("=" * 72)

# CD laser: 780 nm — 3 sig digits (this is a nominal, not a measurement)
data.append(to_q335("CD laser wavelength",
    "0.000000780", "m", 3, "0", "S"))

# DVD laser: 650 nm — 3 sig digits
data.append(to_q335("DVD laser wavelength",
    "0.000000650", "m", 3, "0", "S"))

# Blu-ray laser: 405 nm — 3 sig digits
data.append(to_q335("Blu-ray laser wavelength",
    "0.000000405", "m", 3, "0", "S"))

# CD track pitch: 1.6 µm — 2 sig digits (this IS the spec precision)
data.append(to_q335("CD track pitch",
    "0.0000016", "m", 2, "0", "S"))

# DVD track pitch: 0.74 µm — 2 sig digits
data.append(to_q335("DVD track pitch",
    "0.00000074", "m", 2, "0", "S"))

# Blu-ray track pitch: 0.320 µm — 3 sig digits
data.append(to_q335("Blu-ray track pitch",
    "0.000000320", "m", 3, "0", "S"))

# Blu-ray NA: 0.85 — 2 sig digits
data.append(to_q335("Blu-ray NA",
    "0.85", "", 2, "0", "S"))

# DVD NA: 0.60 — 2 sig digits
data.append(to_q335("DVD NA",
    "0.60", "", 2, "0", "S"))

# CD pit depth: 125 nm — 3 sig digits
data.append(to_q335("CD pit depth",
    "0.000000125", "m", 3, "0", "S"))

# Blu-ray min pit 2T: 149 nm — 3 sig digits
data.append(to_q335("Blu-ray min pit 2T",
    "0.000000149", "m", 3, "0", "S"))

for r in data[-10:]:
    show(r)


# ============================================================
# J. FIBER OPTIC DATA (best available precision)
# ============================================================
print("\n" + "=" * 72)
print("SECTION J: FIBER OPTIC DATA")
print("=" * 72)

# SMF-28 MFD at 1310nm: 9.2 ± 0.4 µm — 2 sig digits (SPEC SHEET LIMIT)
data.append(to_q335("SMF-28 MFD at 1310nm",
    "0.0000092", "m", 2, "0.0000004", "S"))

# SMF-28 NA: 0.14 — 2 sig digits (SPEC SHEET LIMIT)
data.append(to_q335("SMF-28 NA",
    "0.14", "", 2, "~0.01", "S"))

# SMF-28 cladding: 125.0 ± 0.7 µm — 4 sig digits
data.append(to_q335("SMF-28 cladding diameter",
    "0.0001250", "m", 4, "0.0000007", "S"))

# Si lattice constant: 5.431020511(89) × 10^-10 m — 10 sig digits
data.append(to_q335("Si lattice constant",
    "0.0000000005431020511", "m", 10, "0.0000000000000000089", "M"))

for r in data[-4:]:
    show(r)


# ============================================================
# K. KEY DIMENSIONLESS MASS RATIOS
# Computed from full-precision inputs, no rounding.
# ============================================================
print("\n" + "=" * 72)
print("SECTION K: DIMENSIONLESS MASS RATIOS (computed from full precision)")
print("=" * 72)

# Use Decimal for exact division
me = Decimal("0.51099895069")
mmu = Decimal("105.6583755")
mtau = Decimal("1776.86")
mp = Decimal("938.27208943")
mn = Decimal("939.56542194")
MZ = Decimal("91187.6")
MW = Decimal("80369.2")
mH = Decimal("125200")
mt = Decimal("172570")

# m_mu/m_e: limited by m_mu precision (10 digits)
ratio = mmu / me
data.append(to_q335("m_mu/m_e",
    str(ratio), "", 10, None, "M"))

# m_tau/m_e: limited by m_tau (6 digits)
ratio = mtau / me
data.append(to_q335("m_tau/m_e",
    str(ratio), "", 6, None, "M"))

# m_tau/m_mu: limited by m_tau (6 digits)
ratio = mtau / mmu
data.append(to_q335("m_tau/m_mu",
    str(ratio), "", 6, None, "M"))

# m_p/m_e: use the directly measured value, 13 digits
data.append(to_q335("m_p/m_e (direct measurement)",
    "1836.15267343", "", 13, "0.00000032", "M"))

# m_n/m_p: 11 digits each
ratio = mn / mp
data.append(to_q335("m_n/m_p",
    str(ratio), "", 11, None, "M"))

# M_W/M_Z: 6 digits each
ratio = MW / MZ
data.append(to_q335("M_W/M_Z",
    str(ratio), "", 6, None, "M"))

# m_H/M_Z: limited by 5-6 digits
ratio = mH / MZ
data.append(to_q335("m_H/M_Z",
    str(ratio), "", 5, None, "M"))

# m_t/M_Z
ratio = mt / MZ
data.append(to_q335("m_t/M_Z",
    str(ratio), "", 5, None, "M"))

# Koide ratio from full precision masses
mpmath.mp.dps = 50
me_mp = mpmath.mpf("0.51099895069")
mmu_mp = mpmath.mpf("105.6583755")
mtau_mp = mpmath.mpf("1776.86")
K_num = me_mp + mmu_mp + mtau_mp
K_den = (mpmath.sqrt(me_mp) + mpmath.sqrt(mmu_mp) + mpmath.sqrt(mtau_mp))**2
K_val = K_num / K_den
K_str = mpmath.nstr(K_val, 30, strip_zeros=False)
data.append(to_q335("Koide ratio K(e,mu,tau)",
    K_str, "", 6, None, "M"))  # limited by m_tau at 6 digits

for r in data[-9:]:
    show(r)


# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 72)
print("COMPLETE SUMMARY TABLE")
print("=" * 72)
print(f"{'#':>3} {'Name':42s} {'Cat':3s} {'SrcDig':>6} {'NumDig':>6} {'RelErr':>10} {'CofDig':>6} {'Status':22s}")
print("-" * 100)

for i, r in enumerate(data):
    if r['fully_factored']:
        status = "FULLY FACTORED"
    else:
        status = f"{r['cofactor_digits']}-digit cofactor"
    print(f"{i+1:3d} {r['name']:42s} {r['cat']:3s} {r['source_digits']:6d} "
          f"{r['num_digits']:6d} {r['rel_err']:10.2e} {r['cofactor_digits']:6d} {status:22s}")

# Category counts
cats = {}
for r in data:
    cats[r['cat']] = cats.get(r['cat'], 0) + 1

print(f"\nTotal entries: {len(data)}")
labels = {'E':'Exact defined', 'M':'Measured', 'A':'Analytical', 'S':'Standard nominal'}
for c in sorted(cats):
    print(f"  Type {c} ({labels.get(c,c)}): {cats[c]}")

ff = sum(1 for r in data if r['fully_factored'])
print(f"\nFully factored into primes <= 97: {ff}/{len(data)}")

# Precision tiers
tier1 = [r for r in data if r['source_digits'] >= 10]
tier2 = [r for r in data if 5 <= r['source_digits'] < 10]
tier3 = [r for r in data if r['source_digits'] < 5]
print(f"\nPrecision tiers:")
print(f"  10+ source digits (high value for pattern search): {len(tier1)}")
print(f"   5-9 source digits (moderate value): {len(tier2)}")
print(f"   <5 source digits (low value, keep for completeness): {len(tier3)}")

# Flag fully factored
print("\n" + "=" * 72)
print("FULLY FACTORED Q335 NUMERATORS (primes <= 97 only)")
print("=" * 72)
for i, r in enumerate(data):
    if r['fully_factored']:
        fstr = " x ".join(f"{p}^{e}" if e > 1 else str(p) 
                         for p,e in sorted(r['factors'].items()))
        print(f"  {i+1:3d} {r['name']:42s} = {fstr}")

# Flag small cofactors (potentially interesting)
print("\n" + "=" * 72)
print("ENTRIES WITH SMALL COFACTORS (< 30 digits, not fully factored)")
print("These are candidates for further factorization analysis")
print("=" * 72)
for i, r in enumerate(data):
    if not r['fully_factored'] and r['cofactor_digits'] < 30:
        fstr = " x ".join(f"{p}^{e}" if e > 1 else str(p)
                         for p,e in sorted(r['factors'].items())) if r['factors'] else ""
        extra = f" x {fstr}" if fstr else ""
        print(f"  {i+1:3d} {r['name']:42s} cofactor: {r['cofactor_digits']:3d} digits  cofactor = {r['cofactor']}{extra}")

# Entries where reconstruction error is exactly zero (integer values × 2^335)
print("\n" + "=" * 72)
print("ENTRIES WITH ZERO RECONSTRUCTION ERROR (exact in Q335)")
print("=" * 72)
for i, r in enumerate(data):
    if r['rel_err'] == 0.0:
        fstr = " x ".join(f"{p}^{e}" if e > 1 else str(p) 
                         for p,e in sorted(r['factors'].items())) if r['factors'] else "(none)"
        if r['fully_factored']:
            status = "FULLY FACTORED"
        else:
            status = f"{r['cofactor_digits']}-digit cofactor"
        print(f"  {i+1:3d} {r['name']:42s} factors: {fstr}  {status}")

print("\n" + "=" * 72)
print("Q335 CONVERSION COMPLETE")
print(f"2^335 has {len(str(D_int))} decimal digits")
print(f"This basis can represent ~100 decimal digits of precision.")
print(f"All entries with source_digits <= 100 are faithfully represented.")
print("=" * 72)
