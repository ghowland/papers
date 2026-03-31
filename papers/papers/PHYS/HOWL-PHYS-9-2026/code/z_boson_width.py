"""
Z Boson Width in Integer Arithmetic

Gamma(Z -> ff-bar) = (G_F * M_Z^3) / (6*pi*sqrt(2)) * N_c * (v_f^2 + a_f^2) * (1 + corrections)

Vector coupling:  v_f = T3_f - 2*Q_f*sin^2(theta_W)
Axial coupling:   a_f = T3_f

All coefficients are integers or simple rationals.
All transcendentals (pi, sqrt(2)) are MATH-2 integer pairs.
All measured inputs are Fractions.

MEASURED INPUTS:
  G_F = 1.1663788e-5 GeV^-2
  M_Z = 91.1876 GeV
  sin^2(theta_W) = 0.23122 (MSbar at M_Z)
  alpha_s(M_Z) = 0.1180
  alpha_EM(M_Z) = 1/127.906

CODATA COMPARISON:
  Gamma_Z(total) = 2.4955 +/- 0.0023 GeV (PDG 2024)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from math import gcd
from mpmath import mp, mpf

mp.dps = 60


# ================================================================
# Transcendentals (MATH-2)
# ================================================================

def rat_arctan(x, terms=80):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0:
            result += power / n
        else:
            result -= power / n
        power *= x_sq
    return result

def rat_pi(terms=80):
    a1 = rat_arctan(Fraction(1, 5), terms)
    a2 = rat_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def simplify(f, max_digits=40):
    n, d = f.numerator, f.denominator
    while n.bit_length() > int(max_digits * 3.32) or d.bit_length() > int(max_digits * 3.32):
        n //= 2
        d //= 2
    if d == 0:
        d = 1
    g = gcd(abs(n), abs(d))
    return Fraction(n // g, d // g)

def rat_sqrt(x, iters=20):
    if x == Fraction(0):
        return Fraction(0)
    g = Fraction(int(float(x) ** 0.5 * 10**18), 10**18)
    for i in range(iters):
        g = (g + x / g) / 2
        if i % 3 == 2:
            g = simplify(g, 40)
    return simplify(g, 40)


# ================================================================
# Compute transcendentals
# ================================================================

print("Computing transcendentals...")
pi_rat = rat_pi(80)
sqrt2 = rat_sqrt(Fraction(2))
print(f"  pi: {pi_rat.numerator.bit_length()} bits")
print(f"  sqrt(2): {sqrt2.numerator.bit_length()} bits")
print()


# ================================================================
# Measured inputs (all Fraction)
# ================================================================

# G_F in GeV^-2: 1.1663788e-5 = 11663788 / 10^12
# But we work in MeV throughout, so G_F in MeV^-2:
# 1.1663788e-5 GeV^-2 = 1.1663788e-5 / (1000)^2 MeV^-2 = 1.1663788e-11 MeV^-2
# = 11663788 / 10^18 MeV^-2
G_F = Fraction(11663788, 10**18)  # MeV^-2

M_Z = Fraction(455938, 5)  # 91187.6 MeV
sin2_tW = Fraction(23122, 100000)  # 0.23122
alpha_s = Fraction(59, 500)  # 0.1180
alpha_EM_inv = Fraction(63953, 500)  # 127.906
alpha_EM = Fraction(1) / alpha_EM_inv

print("MEASURED INPUTS (all Fraction):")
print(f"  G_F        = {G_F} MeV^-2 ({float(G_F):.7e})")
print(f"  M_Z        = {M_Z} MeV ({float(M_Z)} MeV)")
print(f"  sin^2(tW)  = {sin2_tW} ({float(sin2_tW)})")
print(f"  alpha_s    = {alpha_s} ({float(alpha_s)})")
print(f"  alpha_EM   = 1/{alpha_EM_inv} ({float(alpha_EM):.6e})")
print()


# ================================================================
# The prefactor: G_F * M_Z^3 / (6 * pi * sqrt(2))
# ================================================================

prefactor = G_F * M_Z * M_Z * M_Z / (Fraction(6) * pi_rat * sqrt2)

print(f"PREFACTOR = G_F * M_Z^3 / (6*pi*sqrt(2))")
print(f"  = {float(prefactor):.6f} MeV")
print(f"  = {float(prefactor)/1000:.6f} GeV")
print()


# ================================================================
# Fermion couplings (all exact rationals from SM quantum numbers)
# ================================================================

# Each fermion: (name, T3, Q, Nc, is_quark)
fermions = [
    ("nu_e",    Fraction(1, 2),  Fraction(0),     Fraction(1), False),
    ("nu_mu",   Fraction(1, 2),  Fraction(0),     Fraction(1), False),
    ("nu_tau",  Fraction(1, 2),  Fraction(0),     Fraction(1), False),
    ("e",       Fraction(-1, 2), Fraction(-1),    Fraction(1), False),
    ("mu",      Fraction(-1, 2), Fraction(-1),    Fraction(1), False),
    ("tau",     Fraction(-1, 2), Fraction(-1),    Fraction(1), False),
    ("u",       Fraction(1, 2),  Fraction(2, 3),  Fraction(3), True),
    ("c",       Fraction(1, 2),  Fraction(2, 3),  Fraction(3), True),
    ("d",       Fraction(-1, 2), Fraction(-1, 3), Fraction(3), True),
    ("s",       Fraction(-1, 2), Fraction(-1, 3), Fraction(3), True),
    ("b",       Fraction(-1, 2), Fraction(-1, 3), Fraction(3), True),
]
# Note: top quark excluded — M_Z < 2*m_t, kinematically forbidden

print("=" * 75)
print("PARTIAL WIDTHS")
print("=" * 75)
print()
print(f"  {'Fermion':<10} {'T3':>6} {'Q':>6} {'Nc':>4} {'v_f':>10} {'a_f':>10} "
      f"{'v^2+a^2':>12} {'Gamma(MeV)':>12} {'Gamma(GeV)':>12}")
print(f"  {'-'*98}")

total_width = Fraction(0)
had_width = Fraction(0)
lep_width = Fraction(0)
inv_width = Fraction(0)

for name, T3, Q, Nc, is_quark in fermions:
    # Couplings
    v_f = T3 - Fraction(2) * Q * sin2_tW
    a_f = T3
    v2_plus_a2 = v_f * v_f + a_f * a_f

    # QCD correction for quarks
    if is_quark:
        delta_qcd = Fraction(1) + alpha_s / pi_rat
    else:
        delta_qcd = Fraction(1)

    # QED correction (small, include for completeness)
    delta_qed = Fraction(1) + Fraction(3) * alpha_EM * Q * Q / (Fraction(4) * pi_rat)

    # Partial width
    gamma_f = prefactor * Nc * v2_plus_a2 * delta_qcd * delta_qed

    total_width += gamma_f
    if is_quark:
        had_width += gamma_f
    elif Q == 0:
        inv_width += gamma_f
    else:
        lep_width += gamma_f

    print(f"  {name:<10} {float(T3):>6.1f} {float(Q):>6.2f} {float(Nc):>4.0f} "
          f"{float(v_f):>10.6f} {float(a_f):>10.1f} "
          f"{float(v2_plus_a2):>12.6f} {float(gamma_f):>12.4f} {float(gamma_f)/1000:>12.6f}")

print(f"  {'-'*98}")
print()


# ================================================================
# Totals
# ================================================================

print("=" * 75)
print("TOTALS")
print("=" * 75)
print()
print(f"  Invisible (3 neutrinos):  {float(inv_width):.4f} MeV = {float(inv_width)/1000:.6f} GeV")
print(f"  Leptonic (e + mu + tau):  {float(lep_width):.4f} MeV = {float(lep_width)/1000:.6f} GeV")
print(f"  Hadronic (u,c,d,s,b):    {float(had_width):.4f} MeV = {float(had_width)/1000:.6f} GeV")
print(f"  Total:                    {float(total_width):.4f} MeV = {float(total_width)/1000:.6f} GeV")
print()


# ================================================================
# Comparison to PDG
# ================================================================

# PDG values (MeV)
pdg_total = Fraction(24955, 10)     # 2495.5 MeV = 2.4955 GeV
pdg_had = Fraction(17441, 10)       # 1744.1 MeV = 1.7441 GeV
pdg_inv = Fraction(4990, 10)        # 499.0 MeV = 0.4990 GeV
pdg_lep = Fraction(839, 10)         # 83.9 MeV per lepton * 3 = 251.7 total
pdg_lep_total = Fraction(2517, 10)  # 251.7 MeV total leptonic

print("=" * 75)
print("COMPARISON TO PDG 2024")
print("=" * 75)
print()

for label, ours, pdg in [
    ("Total width", total_width, pdg_total),
    ("Hadronic", had_width, pdg_had),
    ("Invisible", inv_width, pdg_inv),
    ("Leptonic", lep_width, pdg_lep_total),
]:
    diff = float(ours) - float(pdg)
    pct = diff / float(pdg) * 100
    print(f"  {label:<20} Ours: {float(ours)/1000:.4f} GeV  PDG: {float(pdg)/1000:.4f} GeV  "
          f"Diff: {diff:.2f} MeV ({pct:+.2f}%)")

print()


# ================================================================
# Derived quantities
# ================================================================

print("=" * 75)
print("DERIVED QUANTITIES")
print("=" * 75)
print()

# R_Z = Gamma_had / Gamma_lep
# Gamma_lep here = single lepton species (e)
gamma_e = Fraction(0)
for name, T3, Q, Nc, is_quark in fermions:
    if name == "e":
        v_f = T3 - Fraction(2) * Q * sin2_tW
        a_f = T3
        v2_plus_a2 = v_f * v_f + a_f * a_f
        delta_qed = Fraction(1) + Fraction(3) * alpha_EM * Q * Q / (Fraction(4) * pi_rat)
        gamma_e = prefactor * Nc * v2_plus_a2 * delta_qed

R_Z = had_width / gamma_e
sigma_had_0 = Fraction(12) * pi_rat * gamma_e * gamma_e * had_width / (M_Z * M_Z * total_width * total_width)

# Number of neutrino generations from invisible width
# Gamma_inv / Gamma_nu_SM = N_nu
gamma_nu_SM = inv_width / 3  # our prediction for one neutrino species
N_nu = inv_width / gamma_nu_SM  # should be exactly 3 by construction
# More useful: compare measured invisible width to our per-neutrino prediction
# PDG invisible: 499.0 MeV. Our per-neutrino: inv_width/3
N_nu_from_pdg = pdg_inv / gamma_nu_SM

print(f"  R_Z = Gamma_had / Gamma_e = {float(R_Z):.4f}")
print(f"    PDG: 20.767 +/- 0.025")
print(f"    Difference: {float(R_Z) - 20.767:+.4f} ({(float(R_Z)/20.767-1)*100:+.2f}%)")
print()
print(f"  Gamma(e) = {float(gamma_e):.4f} MeV = {float(gamma_e)/1000:.6f} GeV")
print(f"    PDG: 83.984 +/- 0.086 MeV")
print()
print(f"  N_nu (from PDG invisible / our Gamma_nu) = {float(N_nu_from_pdg):.4f}")
print(f"    PDG: 2.9963 +/- 0.0074")
print()


# ================================================================
# Proof of integer arithmetic
# ================================================================

print("=" * 75)
print("ARITHMETIC VERIFICATION")
print("=" * 75)
print()

items = {
    "G_F": G_F,
    "M_Z": M_Z,
    "sin2_tW": sin2_tW,
    "alpha_s": alpha_s,
    "alpha_EM": alpha_EM,
    "prefactor": prefactor,
    "total_width": total_width,
    "had_width": had_width,
    "inv_width": inv_width,
    "lep_width": lep_width,
    "R_Z": R_Z,
}

all_frac = True
for name, val in items.items():
    ok = isinstance(val, Fraction)
    if not ok:
        all_frac = False
    print(f"  {name:<20}: {type(val).__name__:>10}  {'PASS' if ok else 'FAIL'}")

print()
print(f"  All Fraction: {'YES' if all_frac else 'NO'}")
print()


# ================================================================
# Integer content accounting
# ================================================================

print("=" * 75)
print("WHAT IS INTEGER, WHAT IS MEASURED")
print("=" * 75)
print()
print("INTEGER COMPONENTS (from SM quantum numbers):")
print("  T3 = +/- 1/2           (weak isospin)")
print("  Q = 0, -1, +2/3, -1/3  (electric charge)")
print("  Nc = 1 (leptons), 3 (quarks)  (color)")
print("  6 in denominator        (from phase space)")
print("  pi, sqrt(2)             (MATH-2 integer pairs)")
print("  3/4 in QED correction   (from loop integral)")
print()
print("MEASURED INPUTS (5 rationals):")
print(f"  G_F        = {G_F}")
print(f"  M_Z        = {M_Z}")
print(f"  sin^2(tW)  = {sin2_tW}")
print(f"  alpha_s    = {alpha_s}")
print(f"  alpha_EM   = 1/{alpha_EM_inv}")
print()
print("The Z width is determined by 5 measured rationals,")
print("SM quantum numbers (integers and simple rationals),")
print("and MATH-2 transcendentals (pi, sqrt(2)).")
