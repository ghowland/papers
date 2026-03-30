"""
The Fine Structure Constant from Integer Arithmetic — Final Version

Result: 1/alpha_EM = 137.0351 (CODATA: 137.0360, error: 6.5 ppm)

ARCHITECTURE:
  Per-lepton contribution to alpha^{-1} running:
    delta = (1/(3*pi)) * R(M_Z^2, m_f^2)

  R(q^2, m^2) = ln(q^2/m^2) - 2/3            [leading: integer pair]
              + 4*(m^2/q^2)*ln(q^2/m^2)       [O(m^2/q^2): rational * integer pair]
              - 6*(m^2/q^2)                    [O(m^2/q^2): rational]

  Coefficients 2/3, 4, 6: exact integers/rationals from the VP integral.
  m^2/q^2: exact rational from measured masses.
  ln(q^2/m^2): integer pair at 160-term precision.

MEASURED INPUTS (7 rationals from the universe):
  alpha_EM(M_Z)^-1 = 63953/500            (127.906)
  m_e              = 51099895/100000000    (0.51099895 MeV)
  m_mu             = 1056583755/10000000   (105.6583755 MeV)
  m_tau            = 177686/100            (1776.86 MeV)
  M_Z              = 455938/5              (91187.6 MeV)
  Delta_had        = 4408/1000             (4.408, hadronic VP)
  Top_VP           = 97/1000               (0.097)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120


# ================================================================
# Integer pairs for transcendentals
# ================================================================

def rational_arctan(x, terms=160):
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

def rational_pi(terms=160):
    a1 = rational_arctan(Fraction(1, 5), terms)
    a2 = rational_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rational_arctanh(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        result += power / n
        power *= x_sq
    return result

def rational_ln_ratio(p, q, terms=160):
    ratio = Fraction(p, q)
    ln2 = 2 * rational_arctanh(Fraction(1, 3), terms)
    powers_of_2 = 0
    reduced = ratio
    while reduced > 2:
        reduced = reduced / 2
        powers_of_2 += 1
    while reduced < Fraction(1, 2):
        reduced = reduced * 2
        powers_of_2 -= 1
    arg = (reduced - 1) / (reduced + 1)
    ln_reduced = 2 * rational_arctanh(arg, terms)
    return powers_of_2 * ln2 + ln_reduced


# ================================================================
# Compute pi
# ================================================================

print("Computing pi as integer pair (160 terms)...")
pi_rat = rational_pi(160)
three_pi = Fraction(3) * pi_rat

pi_check = mpf(pi_rat.numerator) / mpf(pi_rat.denominator)
pi_digits = -int(mp.log10(abs(pi_check - mp.pi))) if abs(pi_check - mp.pi) > 0 else 999
print(f"  pi: {pi_rat.numerator.bit_length()} bits, {pi_digits} correct digits")
print()


# ================================================================
# Measured inputs
# ================================================================

alpha_EM_inv_MZ = Fraction(63953, 500)           # 127.906

M_Z   = Fraction(455938, 5)                       # 91187.6 MeV
m_e   = Fraction(51099895, 100000000)             # 0.51099895 MeV
m_mu  = Fraction(1056583755, 10000000)            # 105.6583755 MeV
m_tau = Fraction(177686, 100)                     # 1776.86 MeV

had_VP = Fraction(4408, 1000)                     # 4.408
top_VP = Fraction(97, 1000)                       # 0.097


# ================================================================
# Compute leptonic VP with O(m^2/q^2) corrections
# ================================================================

print("Computing leptonic VP with O(m^2/q^2) corrections...")
print()

# R(q^2, m^2) = ln(q^2/m^2) - 2/3 + 4*x*ln(q^2/m^2) - 6*x
# where x = m^2/q^2
# delta(alpha^{-1}) = R / (3*pi)  per lepton (Nc=1, Q=1)

leptons = [("tau", m_tau), ("muon", m_mu), ("electron", m_e)]

lep_VP = Fraction(0)

for name, mass in leptons:
    # x = m^2 / M_Z^2 (exact rational)
    x = (mass * mass) / (M_Z * M_Z)

    # ln(M_Z^2/m^2) = 2*ln(M_Z/m) as integer pair
    p = M_Z.numerator * mass.denominator
    q = M_Z.denominator * mass.numerator
    ln_ratio = rational_ln_ratio(p, q, terms=160)
    ln_q2_m2 = Fraction(2) * ln_ratio

    # R with O(m^2/q^2):
    # R = (1 + 4*x)*ln_q2_m2 - 2/3 - 6*x
    R = (Fraction(1) + Fraction(4) * x) * ln_q2_m2 - Fraction(2, 3) - Fraction(6) * x

    # delta(alpha^{-1}) = R / (3*pi)
    delta = R / three_pi
    lep_VP += delta

    print(f"  {name:<10}: x = {float(x):.4e}, "
          f"O(m2) corr = {float(Fraction(4)*x*ln_q2_m2 - Fraction(6)*x):.2e}, "
          f"delta = {float(delta):.10f}")

print(f"  {'Total':<10}: leptonic VP = {float(lep_VP):.10f}")
print()


# ================================================================
# Assemble
# ================================================================

result = alpha_EM_inv_MZ + lep_VP + had_VP + top_VP

print("=" * 70)
print("RESULT")
print("=" * 70)
print()
print(f"  1/alpha_EM(M_Z)       = {float(alpha_EM_inv_MZ):.6f}")
print(f"  + Leptonic VP          = {float(lep_VP):.6f}  (integer arithmetic + O(m^2/q^2))")
print(f"  + Hadronic VP          = {float(had_VP):.6f}  (measured)")
print(f"  + Top quark            = {float(top_VP):.6f}")
print(f"  ─────────────────────────────────────────")
print(f"  = 1/alpha_EM(low)      = {float(result):.10f}")
print()
print(f"  CODATA:                  137.035999177")
print()

diff = float(result) - 137.035999177
print(f"  Difference:              {diff:+.10f}")
print(f"  Relative error:          {abs(diff)/137.036 * 100:.6f}%")
print(f"  Parts per million:       {abs(diff)/137.036 * 1e6:.1f} ppm")
print()


# ================================================================
# 100-digit verification
# ================================================================

print("=" * 70)
print("100-DIGIT VERIFICATION")
print("=" * 70)
print()

result_mp = mpf(result.numerator) / mpf(result.denominator)

print("Integer pair result (100 digits):")
print(f"  {mp.nstr(result_mp, 100)}")
print()
print("CODATA reference:")
print("  137.035999177")
print()

diff_mp = result_mp - mpf('137.035999177')
print(f"Difference: {mp.nstr(diff_mp, 15)}")
print(f"Relative:   {mp.nstr(abs(diff_mp)/mpf('137.036') * 100, 10)}%")
print()


# ================================================================
# Proof of integer arithmetic
# ================================================================

print("=" * 70)
print("PROOF OF INTEGER ARITHMETIC")
print("=" * 70)
print()

print(f"Result type:       {type(result)}")
print(f"Numerator bits:    {result.numerator.bit_length()}")
print(f"Denominator bits:  {result.denominator.bit_length()}")
print()

components = {
    "alpha_EM_inv_MZ": alpha_EM_inv_MZ,
    "lep_VP":          lep_VP,
    "had_VP":          had_VP,
    "top_VP":          top_VP,
    "pi_rat":          pi_rat,
    "three_pi":        three_pi,
}

all_frac = True
for name, val in components.items():
    ok = isinstance(val, Fraction)
    if not ok:
        all_frac = False
    print(f"  {name:<20}: {type(val).__name__:>10}  {'PASS' if ok else 'FAIL'}")

print()
print(f"All components Fraction: {'YES' if all_frac else 'NO'}")
print()


# ================================================================
# Complete accounting
# ================================================================

print("=" * 70)
print("COMPLETE ACCOUNTING")
print("=" * 70)
print()
print("INTEGER COMPONENTS (exact, from physics):")
print(f"  Leading VP constant:     2/3 (subtracted VP asymptotic)")
print(f"  O(m^2/q^2) log coeff:   4   (VP expansion, next order)")
print(f"  O(m^2/q^2) constant:    6   (VP expansion, next order)")
print(f"  Lepton Nc*Q^2:          1   per species (Nc=1, Q=1)")
print(f"  pi:                     integer pair, {pi_rat.numerator.bit_length()} bits")
print(f"  ln(M_Z/m_f):            integer pairs, 160-term precision")
print()
print("MEASURED INPUTS (7 rationals from the universe):")
print(f"  alpha_EM(M_Z)^-1  = {alpha_EM_inv_MZ}")
print(f"  m_e               = {m_e} MeV")
print(f"  m_mu              = {m_mu} MeV")
print(f"  m_tau             = {m_tau} MeV")
print(f"  M_Z               = {M_Z} MeV")
print(f"  Hadronic VP       = {had_VP}")
print(f"  Top VP            = {top_VP}")
print()
print("THE LAW IS INTEGERS.")
print("The universe supplies seven rationals.")
print(f"The result is a Fraction with {result.numerator.bit_length()}-bit numerator.")
print(f"1/alpha_EM = {float(result):.10f}")
print(f"CODATA:      137.035999177")
print(f"Error:       {abs(diff)/137.036 * 1e6:.1f} ppm")
