"""
W Boson Mass at Two-Loop Order in Integer Arithmetic

Extends mw_prediction.py with the dominant two-loop correction.

The leading 2-loop correction to Delta_rho from top quark loops:

  Delta_rho^(2) = [3*G_F*m_t^2/(8*pi^2*sqrt(2))]^2 * rho_2

where rho_2 = (19 - 2*pi^2)/3

The integer 19 and the MATH-2 constant pi^2 enter.
The coefficient rho_2 = (19 - 2*pi^2)/3 ≈ -0.2464...

Additional 2-loop pieces:
  - O(alpha*alpha_s^2) QCD correction to Delta_rho
  - O(G_F^2 * m_t^2 * M_Z^2) subleading
  
We implement the leading O(G_F^2 * m_t^4) piece which accounts
for the bulk of the ~28 MeV shift.

MEASURED INPUTS (same 8 as 1-loop script):
  G_F, alpha(0), alpha(M_Z), M_Z, m_t, m_H, alpha_s

All intermediate values Fraction (with controlled simplification for sqrt).
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


def simplify(f, max_digits=30):
    n, d = f.numerator, f.denominator
    while n.bit_length() > int(max_digits * 3.32) or d.bit_length() > int(max_digits * 3.32):
        n //= 2
        d //= 2
    if d == 0: d = 1
    g = gcd(abs(n), abs(d))
    return Fraction(n // g, d // g)

def rat_arctan(x, N=40):
    r, p, xsq = Fraction(0), x, x * x
    for k in range(N):
        n = 2 * k + 1
        r += p / n if k % 2 == 0 else -p / n
        p *= xsq
        if k % 10 == 9:
            r = simplify(r, 40)
            p = simplify(p, 40)
    return r

def rat_pi(N=40):
    return 4 * (4 * rat_arctan(Fraction(1, 5), N) - rat_arctan(Fraction(1, 239), N))

def rat_arctanh(x, N=15):
    r, p, xsq = Fraction(0), x, x * x
    for k in range(N):
        r += p / (2 * k + 1)
        p *= xsq
    return r

def rat_ln_ratio(p, q, N=15):
    ratio = Fraction(p, q)
    ln2 = 2 * rat_arctanh(Fraction(1, 3), N)
    pw = 0
    r = ratio
    while r > 2: r /= 2; pw += 1
    while r < Fraction(1, 2): r *= 2; pw -= 1
    return pw * ln2 + 2 * rat_arctanh((r - 1) / (r + 1), N)

def rat_sqrt(x, iters=12):
    g = Fraction(int(float(x) ** 0.5 * 10**15), 10**15)
    for i in range(iters):
        g = (g + x / g) / 2
        if i % 3 == 2: g = simplify(g, 30)
    return g


# ================================================================
# Compute pi
# ================================================================

print("Computing pi...")
pi_r = rat_pi(40)
pi_r = simplify(pi_r, 40)
pi2 = simplify(pi_r * pi_r, 40)
sqrt2 = rat_sqrt(Fraction(2), 10)
sqrt2 = simplify(sqrt2, 30)


# ================================================================
# Measured inputs
# ================================================================

G_F = Fraction(11663788, 10**18)          # MeV^-2
alpha_0 = Fraction(10**9, 137035999177)
alpha_MZ = Fraction(500, 63953)
M_Z = Fraction(455938, 5)                 # 91187.6 MeV
m_t = Fraction(172690)
m_H = Fraction(125100)
alpha_s = Fraction(59, 500)

print()
print("MEASURED INPUTS")
print("=" * 60)
print(f"  G_F      = {float(G_F):.7e} MeV^-2")
print(f"  M_Z      = {float(M_Z):.1f} MeV")
print(f"  m_t      = {float(m_t):.0f} MeV")
print(f"  m_H      = {float(m_H):.0f} MeV")
print(f"  alpha_s  = {float(alpha_s):.4f}")
print()


# ================================================================
# Tree level (same as 1-loop script)
# ================================================================

A2 = simplify(pi_r * alpha_0 / (sqrt2 * G_F * M_Z * M_Z), 30)
disc = Fraction(1) - 4 * A2
sd = rat_sqrt(simplify(disc, 30), 10)
x0 = (Fraction(1) + sd) / 2
MW2 = simplify(x0 * M_Z * M_Z, 30)
MW_tree = rat_sqrt(MW2, 10)
MW_tree = simplify(MW_tree, 25)

print(f"Tree level: M_W = {float(MW_tree)/1000:.4f} GeV")
print()


# ================================================================
# 1-loop corrections (same as before)
# ================================================================

Delta_alpha = simplify(Fraction(1) - alpha_0 / alpha_MZ, 30)

Delta_rho_1loop = simplify(
    Fraction(3) * G_F * m_t * m_t / (Fraction(8) * pi2 * sqrt2), 30
)

qcd_1loop = simplify(Fraction(1) - Fraction(2) * alpha_s / (Fraction(3) * pi_r), 30)
Delta_rho_1loop_qcd = simplify(Delta_rho_1loop * qcd_1loop, 30)

ln_mH2_MW2 = simplify(Fraction(2) * rat_ln_ratio(125100, 80400, 12), 30)


# ================================================================
# 2-loop correction: leading O(G_F^2 * m_t^4)
# ================================================================

print("=" * 60)
print("2-LOOP CORRECTION")
print("=" * 60)
print()

# The leading 2-loop top contribution to Delta_rho:
# Delta_rho^(2) = (Delta_rho^(1))^2 * rho_2
# where rho_2 = (19 - 2*pi^2) / 3
#
# 19 is an integer. pi^2 is a MATH-2 constant.
# rho_2 ≈ (19 - 19.739) / 3 ≈ -0.246

rho_2 = (Fraction(19) - Fraction(2) * pi2) / Fraction(3)

print(f"  rho_2 = (19 - 2*pi^2) / 3")
print(f"        = ({float(Fraction(19) - Fraction(2)*pi2):.6f}) / 3")
print(f"        = {float(rho_2):.6f}")
print()

# Delta_rho^(2) = Delta_rho_1loop^2 * rho_2
# But more precisely, the 2-loop correction to Delta_r involves:
# delta_2loop = Delta_rho_1loop * rho_2 * (cos2/sin2)
# because Delta_rho enters Delta_r multiplied by cos2/sin2

# The O(alpha_s^2) correction to Delta_rho:
# Delta_rho gets multiplied by (1 - 2*alpha_s/(3*pi) - alpha_s^2 * (pi^2/3 - 13/4 + ...))
# At 2-loop QCD: the alpha_s^2 coefficient
# For the leading piece: -(alpha_s/pi)^2 * (pi^2/3 + ...)
# This is smaller. We include it as:
# qcd_2loop = 1 - 2*alpha_s/(3*pi) - (alpha_s/pi)^2 * (pi^2/3 - 13/4)

as_over_pi = alpha_s / pi_r
as_over_pi_sq = as_over_pi * as_over_pi

qcd_2loop_coeff = simplify(pi2 / 3 - Fraction(13, 4), 30)
qcd_2loop = simplify(
    Fraction(1) - Fraction(2) * as_over_pi / 3 + as_over_pi_sq * qcd_2loop_coeff,
    30
)

print(f"  QCD correction to Delta_rho:")
print(f"    1-loop: 1 - 2*alpha_s/(3*pi) = {float(qcd_1loop):.6f}")
print(f"    2-loop coeff: pi^2/3 - 13/4 = {float(qcd_2loop_coeff):.6f}")
print(f"    2-loop: {float(qcd_2loop):.6f}")
print()


# ================================================================
# Iterate to convergence with 2-loop corrections
# ================================================================

print("=" * 60)
print("ITERATING WITH 2-LOOP CORRECTIONS")
print("=" * 60)
print()

MW = MW_tree
for it in range(8):
    x = simplify((MW * MW) / (M_Z * M_Z), 25)
    sin2 = Fraction(1) - x
    cos2_sin2 = simplify(x / sin2, 25)

    # Higgs correction (1-loop)
    Delta_r_H = simplify(
        Fraction(11, 3) * alpha_MZ / (Fraction(16) * pi_r * sin2)
        * (ln_mH2_MW2 - Fraction(5, 6)),
        25,
    )

    # Delta_rho with 2-loop QCD
    Delta_rho_2qcd = simplify(Delta_rho_1loop * qcd_2loop, 25)

    # 2-loop top: Delta_rho^(1) * rho_2 adds to Delta_rho
    # The full 2-loop Delta_rho contribution to Delta_r:
    # -(cos2/sin2) * [Delta_rho_2qcd + Delta_rho_1loop^2 * rho_2]
    Delta_rho_2loop_top = simplify(Delta_rho_1loop * Delta_rho_1loop * rho_2, 25)

    Delta_r = simplify(
        Delta_alpha
        - cos2_sin2 * (Delta_rho_2qcd + Delta_rho_2loop_top)
        + Delta_r_H,
        25
    )

    A2_corr = simplify(A2 / (Fraction(1) - Delta_r), 25)
    disc_corr = Fraction(1) - 4 * A2_corr
    sqrt_disc = rat_sqrt(simplify(disc_corr, 25), 8)
    x_new = (Fraction(1) + sqrt_disc) / 2
    MW_new = rat_sqrt(simplify(x_new * M_Z * M_Z, 25), 8)
    MW_new = simplify(MW_new, 20)

    change = abs(float(MW_new) - float(MW))
    print(f"  Iter {it+1}: M_W = {float(MW_new)/1000:.5f} GeV, "
          f"Delta_r = {float(Delta_r):.8f}, change = {change:.2f} MeV")

    MW = MW_new
    if change < 0.1:
        print("  Converged.")
        break

print()


# ================================================================
# Result
# ================================================================

MW_1loop = Fraction(80386, 1)  # Our 1-loop result, MeV (approximate)
MW_2loop = MW

print("=" * 60)
print("RESULT")
print("=" * 60)
print()
print(f"  M_W (tree):         {float(MW_tree)/1000:.4f} GeV")
print(f"  M_W (1-loop):       80.3860 GeV (from previous script)")
print(f"  M_W (2-loop):       {float(MW_2loop)/1000:.5f} GeV")
print()
print(f"  2-loop shift:       {float(MW_2loop)/1000 - 80.386:+.4f} GeV = {float(MW_2loop) - 80386:+.1f} MeV")
print()
print("COMPARISON")
print(f"  M_W (our 2-loop):       {float(MW_2loop)/1000:.4f} GeV")
print(f"  M_W (SM best, PDG):     80.3577 ± 0.0046 GeV")
print(f"  M_W (ATLAS 2024):       80.3665 ± 0.0159 GeV")
print(f"  M_W (CDF II 2022):      80.4335 ± 0.0094 GeV")
print(f"  M_W (world avg excl CDF): 80.369 ± 0.013 GeV")
print()
print(f"  Our - SM best:  {float(MW_2loop)/1000 - 80.3577:+.4f} GeV = {float(MW_2loop) - 80357.7:+.1f} MeV")
print()

print("INTEGER CONTENT OF 2-LOOP:")
print(f"  rho_2 = (19 - 2*pi^2) / 3")
print(f"  19 is an integer")
print(f"  pi^2 is a MATH-2 integer pair")
print(f"  QCD 2-loop: pi^2/3 - 13/4 (integers + pi^2)")
print(f"  All intermediate values: Fraction")
print(f"  Type check: {type(MW_2loop).__name__}")

