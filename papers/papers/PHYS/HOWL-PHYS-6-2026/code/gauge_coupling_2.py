"""
The Standard Model Gauge Couplings in Integer Arithmetic

Runs all three gauge couplings (alpha_1, alpha_2, alpha_3) from M_Z
to 10^16 GeV using exact rational arithmetic.

One-loop RGE: alpha_i^{-1}(mu2) = alpha_i^{-1}(mu1) - b0_i/(2*pi) * ln(mu2/mu1)

Two segments:
  M_Z -> m_t:   5 active quarks (top decoupled)
  m_t -> high:  6 active quarks (all SM particles)

For alpha_3, the slope changes exactly at m_t:
  b0_3(5f) = -23/3,  b0_3(6f) = -7

For alpha_1 and alpha_2, the top's individual contribution to the
electroweak beta functions is small over the short interval
ln(m_t/M_Z) ~ 0.64. The full 3-generation slopes are used for
both segments; the induced error is ~0.03 in 1/alpha, negligible
against the ~30 units of running to the GUT scale.

MEASURED INPUTS:
  alpha_EM(M_Z)^-1 = 63953/500       (127.906)
  sin^2(theta_W)   = 23122/100000    (0.23122)
  alpha_s(M_Z)     = 59/500          (0.1180)
  m_t              = 173000 MeV
  M_Z              = 455938/5 MeV    (91187.6)

INTEGER COMPONENTS:
  b0 slopes: 41/10, -19/6, -7 (particle counting, 3 generations + 1 Higgs)
  pi, ln: integer pairs at 160-term precision
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf
import math

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
two_pi = Fraction(2) * pi_rat
print(f"  Done. {pi_rat.numerator.bit_length()} bits.")
print()


# ================================================================
# Measured inputs at M_Z
# ================================================================

alpha_EM_inv_MZ = Fraction(63953, 500)         # 127.906
sin2_tW_MZ = Fraction(23122, 100000)           # 0.23122
cos2_tW_MZ = Fraction(1) - sin2_tW_MZ
alpha_s_MZ = Fraction(59, 500)                 # 0.1180

M_Z_MeV = Fraction(455938, 5)                  # 91187.6 MeV
m_t_MeV = Fraction(173000, 1)                  # 173000 MeV

# Extract individual couplings at M_Z
# alpha_2 = alpha_EM / sin^2(theta_W)
# alpha_1_SM = alpha_EM / cos^2(theta_W)
# alpha_1_GUT = (5/3) * alpha_1_SM
alpha_EM_MZ = Fraction(1) / alpha_EM_inv_MZ
alpha_2_MZ = alpha_EM_MZ / sin2_tW_MZ
alpha_1_SM_MZ = alpha_EM_MZ / cos2_tW_MZ
alpha_1_GUT_MZ = Fraction(5, 3) * alpha_1_SM_MZ

a1_inv_MZ = Fraction(1) / alpha_1_GUT_MZ
a2_inv_MZ = Fraction(1) / alpha_2_MZ
a3_inv_MZ = Fraction(1) / alpha_s_MZ


# ================================================================
# Beta function slopes (exact rationals from particle counting)
# ================================================================

# n_g=3 generations, n_H=1 Higgs doublet:
# b0_1 = (4/3)*n_g + (1/10)*n_H = 41/10
# b0_2 = (4/3)*n_g - 22/3 + (1/6)*n_H = -19/6
# b0_3(6f) = (2/3)*6 - 11 = -7
# b0_3(5f) = (2/3)*5 - 11 = -23/3

b0_1 = Fraction(41, 10)
b0_2 = Fraction(-19, 6)
b0_3_6f = Fraction(-7, 1)
b0_3_5f = Fraction(-23, 3)


# ================================================================
# Print inputs
# ================================================================

print("MEASURED INPUTS AT M_Z")
print(f"  1/alpha_EM    = {float(alpha_EM_inv_MZ):.6f}")
print(f"  sin^2(theta_W)= {float(sin2_tW_MZ):.6f}")
print(f"  alpha_s       = {float(alpha_s_MZ):.6f}")
print()
print("EXTRACTED COUPLINGS AT M_Z")
print(f"  1/alpha_1_GUT = {float(a1_inv_MZ):.6f}")
print(f"  1/alpha_2     = {float(a2_inv_MZ):.6f}")
print(f"  1/alpha_3     = {float(a3_inv_MZ):.6f}")
print()
print("BETA FUNCTION SLOPES (from particle counting)")
print(f"  b0_1 = {b0_1}  ({float(b0_1):.6f})")
print(f"  b0_2 = {b0_2}  ({float(b0_2):.6f})")
print(f"  b0_3 = {b0_3_6f} (6f), {b0_3_5f} (5f)")
print()


# ================================================================
# Segment 1: M_Z -> m_t (5 active quark flavors for alpha_3)
# ================================================================

print("=" * 70)
print("RUNNING THE THREE GAUGE COUPLINGS")
print("=" * 70)
print()

p_seg1 = m_t_MeV.numerator * M_Z_MeV.denominator
q_seg1 = m_t_MeV.denominator * M_Z_MeV.numerator
ln_mt_mz = rational_ln_ratio(p_seg1, q_seg1, terms=160)
factor_seg1 = ln_mt_mz / two_pi

a1_inv_mt = a1_inv_MZ - b0_1 * factor_seg1
a2_inv_mt = a2_inv_MZ - b0_2 * factor_seg1
a3_inv_mt = a3_inv_MZ - b0_3_5f * factor_seg1

print(f"Segment 1: M_Z -> m_t  (ln = {float(ln_mt_mz):.6f})")
print(f"  b0_3 = {b0_3_5f} (top decoupled)")
print(f"  1/a1 = {float(a1_inv_mt):.6f}")
print(f"  1/a2 = {float(a2_inv_mt):.6f}")
print(f"  1/a3 = {float(a3_inv_mt):.6f}")
print()


# ================================================================
# Segment 2: m_t -> high scales (6 active quarks)
# ================================================================

scales = [
    ("1 TeV",    Fraction(10**6, 1)),
    ("10 TeV",   Fraction(10**7, 1)),
    ("100 TeV",  Fraction(10**8, 1)),
    ("10^6 GeV", Fraction(10**9, 1)),
    ("10^8 GeV", Fraction(10**11, 1)),
    ("10^10 GeV", Fraction(10**13, 1)),
    ("10^12 GeV", Fraction(10**15, 1)),
    ("10^14 GeV", Fraction(10**17, 1)),
    ("10^16 GeV", Fraction(10**19, 1)),
]

results = [("M_Z", M_Z_MeV, a1_inv_MZ, a2_inv_MZ, a3_inv_MZ)]
results.append(("m_t", m_t_MeV, a1_inv_mt, a2_inv_mt, a3_inv_mt))

for name, scale_MeV in scales:
    p = scale_MeV.numerator * m_t_MeV.denominator
    q = scale_MeV.denominator * m_t_MeV.numerator
    ln_val = rational_ln_ratio(p, q, terms=160)
    factor = ln_val / two_pi

    a1_inv = a1_inv_mt - b0_1 * factor
    a2_inv = a2_inv_mt - b0_2 * factor
    a3_inv = a3_inv_mt - b0_3_6f * factor

    results.append((name, scale_MeV, a1_inv, a2_inv, a3_inv))


# ================================================================
# Display all couplings
# ================================================================

print("=" * 65)
print("ALL COUPLINGS AT EVERY SCALE")
print("=" * 65)
print()
print(f"{'Scale':<12} {'1/a1':>10} {'1/a2':>10} {'1/a3':>10} "
      f"{'sin2_tW':>10} {'1/a_EM':>10}")
print("-" * 65)

for name, scale_MeV, a1_inv, a2_inv, a3_inv in results:
    sin2 = Fraction(3) * a2_inv / (Fraction(3) * a2_inv + Fraction(5) * a1_inv)
    aEM_inv = Fraction(5, 3) * a1_inv + a2_inv
    a3_str = f"{float(a3_inv):>10.4f}" if a3_inv > 0 else f"{'<0':>10}"

    print(f"{name:<12} {float(a1_inv):>10.4f} {float(a2_inv):>10.4f} {a3_str} "
          f"{float(sin2):>10.6f} {float(aEM_inv):>10.4f}")

print("-" * 65)
print()


# ================================================================
# GUT convergence analysis
# ================================================================

print("=" * 70)
print("GUT CONVERGENCE ANALYSIS")
print("=" * 70)
print()

def crossing(ai_mt, aj_mt, bi, bj):
    """Find scale where alpha_i^{-1} = alpha_j^{-1}, running from m_t with 6f slopes."""
    L = (aj_mt - ai_mt) / (bj - bi)
    ln_val = L * two_pi
    a_val = ai_mt - bi * L
    mu_GeV = 173 * math.exp(float(ln_val))
    return ln_val, a_val, mu_GeV

ln_12, a_12, mu_12 = crossing(a1_inv_mt, a2_inv_mt, b0_1, b0_2)
ln_13, a_13, mu_13 = crossing(a1_inv_mt, a3_inv_mt, b0_1, b0_3_6f)
ln_23, a_23, mu_23 = crossing(a2_inv_mt, a3_inv_mt, b0_2, b0_3_6f)

print(f"Pairwise crossing points:")
print(f"  a1 = a2:  mu ~ {mu_12:.2e} GeV,  1/alpha = {float(a_12):.4f}")
print(f"  a1 = a3:  mu ~ {mu_13:.2e} GeV,  1/alpha = {float(a_13):.4f}")
print(f"  a2 = a3:  mu ~ {mu_23:.2e} GeV,  1/alpha = {float(a_23):.4f}")
print()
print(f"Crossing scale spread:")
print(f"  ln(mu_12/mu_13) = {float(ln_12 - ln_13):.4f}")
print(f"  ln(mu_12/mu_23) = {float(ln_12 - ln_23):.4f}")
print(f"  For exact unification these would be 0. They are not.")
print()


# ================================================================
# Gap ratio
# ================================================================

print("=" * 70)
print("GAP RATIO")
print("=" * 70)
print()

gap_predicted = (b0_1 - b0_2) / (b0_2 - b0_3_6f)
gap_measured = (a1_inv_MZ - a2_inv_MZ) / (a2_inv_MZ - a3_inv_MZ)

print(f"From beta function slopes (pure integer):")
print(f"  (b1 - b2) = {b0_1 - b0_2} = {float(b0_1 - b0_2):.6f}")
print(f"  (b2 - b3) = {b0_2 - b0_3_6f} = {float(b0_2 - b0_3_6f):.6f}")
print(f"  Ratio     = {gap_predicted} = {float(gap_predicted):.10f}")
print()
print(f"From measured couplings at M_Z:")
print(f"  (a1^-1 - a2^-1) = {float(a1_inv_MZ - a2_inv_MZ):.6f}")
print(f"  (a2^-1 - a3^-1) = {float(a2_inv_MZ - a3_inv_MZ):.6f}")
print(f"  Ratio            = {float(gap_measured):.10f}")
print()
print(f"Miss: {abs(float(gap_predicted) - float(gap_measured)) / float(gap_measured) * 100:.1f}%")
print(f"The 36% miss quantifies the Standard Model's incomplete particle content.")
print()


# ================================================================
# Proof of integer arithmetic
# ================================================================

print("=" * 70)
print("PROOF OF INTEGER ARITHMETIC")
print("=" * 70)
print()

frac_checks = {
    "a1_inv_MZ":     a1_inv_MZ,
    "a2_inv_MZ":     a2_inv_MZ,
    "a3_inv_MZ":     a3_inv_MZ,
    "gap_predicted":  gap_predicted,
    "gap_measured":   gap_measured,
    "pi_rat":         pi_rat,
}

all_frac = True
for name, val in frac_checks.items():
    ok = isinstance(val, Fraction)
    if not ok:
        all_frac = False
    print(f"  {name:<20}: {type(val).__name__:>10}  {'PASS' if ok else 'FAIL'}")

print()
print(f"All components Fraction: {'YES' if all_frac else 'NO'}")
print()


# ================================================================
# Summary
# ================================================================

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("MEASURED INPUTS (3 rationals + masses):")
print(f"  alpha_EM(M_Z)^-1 = {alpha_EM_inv_MZ}")
print(f"  sin^2(theta_W)   = {sin2_tW_MZ}")
print(f"  alpha_s(M_Z)     = {alpha_s_MZ}")
print(f"  m_t = {m_t_MeV} MeV,  M_Z = {M_Z_MeV} MeV")
print()
print("INTEGER COMPONENTS:")
print(f"  b0 slopes: {b0_1}, {b0_2}, {b0_3_6f} (from particle counting)")
print(f"  b0_3(5f): {b0_3_5f}")
print(f"  pi: integer pair, {pi_rat.numerator.bit_length()} bits")
print()
print("FINDINGS:")
print(f"  Gap ratio: {gap_predicted} = {float(gap_predicted):.6f} predicted vs {float(gap_measured):.6f} measured ({abs(float(gap_predicted) - float(gap_measured)) / float(gap_measured) * 100:.1f}% miss)")
print(f"  Three couplings do NOT unify at one loop in the Standard Model")
print(f"  a1=a2 at ~{mu_12:.1e} GeV, a2=a3 at ~{mu_23:.1e} GeV")
print(f"  Non-unification is the signature of missing particle content")
