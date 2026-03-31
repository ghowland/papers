"""
Koide Formula in Integer Arithmetic

The Koide relation: (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3

Three charged lepton inertias (PHYS-1: mass is inertia) satisfy a geometric
constraint with constant 2/3 — the same rational as the subtracted VP constant (PHYS-5).

Given m_e and m_mu as measured rationals, solve for m_tau assuming Koide exact.
All computation in Fraction arithmetic with controlled simplification for sqrt.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from math import gcd
from mpmath import mp, mpf
import math

mp.dps = 120


# ================================================================
# Controlled-precision sqrt (from session notes: MUST simplify)
# ================================================================

def simplify(f, max_digits=40):
    """Reduce Fraction to ~max_digits precision to prevent explosion."""
    n, d = f.numerator, f.denominator
    while n.bit_length() > int(max_digits * 3.32) or d.bit_length() > int(max_digits * 3.32):
        n //= 2
        d //= 2
    if d == 0:
        d = 1
    g = gcd(abs(n), abs(d))
    return Fraction(n // g, d // g)


def rat_sqrt(x, iters=20):
    """Newton sqrt with simplification every 3 steps."""
    if x == Fraction(0):
        return Fraction(0)
    # Initial guess from float
    g = Fraction(int(float(x) ** 0.5 * 10**18), 10**18)
    for i in range(iters):
        g = (g + x / g) / 2
        if i % 3 == 2:
            g = simplify(g, 40)
    return simplify(g, 40)


# ================================================================
# Measured inputs (lepton inertias, MeV)
# ================================================================

m_e = Fraction(51099895, 100000000)        # 0.51099895 MeV
m_mu = Fraction(1056583755, 10000000)      # 105.6583755 MeV
m_tau_measured = Fraction(177686, 100)      # 1776.86 MeV
m_tau_uncertainty = Fraction(12, 100)       # ±0.12 MeV

print("=" * 70)
print("KOIDE FORMULA IN INTEGER ARITHMETIC")
print("=" * 70)
print()
print("MEASURED INPUTS (lepton inertias):")
print(f"  m_e   = {m_e} MeV = {float(m_e)} MeV")
print(f"  m_mu  = {m_mu} MeV = {float(m_mu)} MeV")
print(f"  m_tau = {m_tau_measured} MeV = {float(m_tau_measured)} MeV (PDG)")
print()


# ================================================================
# Step 1: Verify Koide with measured masses
# ================================================================

print("STEP 1: VERIFY KOIDE WITH MEASURED MASSES")
print("-" * 50)

sqrt_me = rat_sqrt(m_e)
sqrt_mmu = rat_sqrt(m_mu)
sqrt_mtau = rat_sqrt(m_tau_measured)

numerator = m_e + m_mu + m_tau_measured
sum_sqrt = sqrt_me + sqrt_mmu + sqrt_mtau
denominator = sum_sqrt * sum_sqrt

koide_ratio = simplify(numerator / denominator, 40)
two_thirds = Fraction(2, 3)

koide_mp = mpf(koide_ratio.numerator) / mpf(koide_ratio.denominator)
diff_mp = koide_mp - mpf(2)/3

print(f"  Koide ratio:  {mp.nstr(koide_mp, 25)}")
print(f"  2/3:          {mp.nstr(mpf(2)/3, 25)}")
print(f"  Deviation:    {mp.nstr(abs(diff_mp)/(mpf(2)/3)*100, 8)}%")
print()


# ================================================================
# Step 2: Predict m_tau from exact Koide
# ================================================================

print("STEP 2: PREDICT m_tau FROM KOIDE (exact 2/3)")
print("-" * 50)

# Koide: (B + s^2) / (A + s)^2 = 2/3  where s = sqrt(m_tau), A = sqrt(m_e)+sqrt(m_mu), B = m_e+m_mu
# => 3(B + s^2) = 2(A + s)^2
# => s^2 - 4As + (3B - 2A^2) = 0
# => s = 2A ± sqrt(4A^2 - 3B + 2A^2) = 2A ± sqrt(6A^2 - 3B) = 2A ± sqrt(3(2A^2 - B))

A = sqrt_me + sqrt_mmu
B = m_e + m_mu

disc_inner = simplify(Fraction(2) * A * A - B, 40)
discriminant = simplify(Fraction(3) * disc_inner, 40)

print(f"  A = sqrt(m_e) + sqrt(m_mu) = {float(A):.10f}")
print(f"  B = m_e + m_mu = {float(B):.10f}")
print(f"  2A^2 - B = {float(disc_inner):.10f}")

sqrt_disc = rat_sqrt(discriminant)

s_plus = simplify(Fraction(2) * A + sqrt_disc, 40)
s_minus = simplify(Fraction(2) * A - sqrt_disc, 40)

m_tau_predicted = simplify(s_plus * s_plus, 40)
m_tau_second = simplify(s_minus * s_minus, 40)

print(f"  m_tau (+ branch): {float(m_tau_predicted):.6f} MeV")
print(f"  m_tau (- branch): {float(m_tau_second):.6f} MeV")
print()

diff_mtau = float(m_tau_predicted) - float(m_tau_measured)
sigma = diff_mtau / float(m_tau_uncertainty)

print(f"  m_tau predicted:  {float(m_tau_predicted):.4f} MeV")
print(f"  m_tau measured:   {float(m_tau_measured):.4f} MeV")
print(f"  Difference:       {diff_mtau:+.4f} MeV")
print(f"  Sigma:            {sigma:.2f}σ")
print()


# ================================================================
# Step 3: Verify prediction satisfies Koide
# ================================================================

print("STEP 3: VERIFY PREDICTION")
print("-" * 50)

sqrt_mtau_pred = s_plus
num_check = m_e + m_mu + m_tau_predicted
sum_sqrt_check = sqrt_me + sqrt_mmu + sqrt_mtau_pred
den_check = sum_sqrt_check * sum_sqrt_check
koide_check = simplify(num_check / den_check, 40)

koide_check_mp = mpf(koide_check.numerator) / mpf(koide_check.denominator)
check_diff = abs(koide_check_mp - mpf(2)/3)

print(f"  Koide with predicted m_tau: {mp.nstr(koide_check_mp, 25)}")
print(f"  Deviation from 2/3:        {mp.nstr(check_diff, 10)}")
print(f"  (Not exactly 2/3 due to controlled simplification in sqrt)")
print()


# ================================================================
# Step 4: Koide parametrization
# ================================================================

print("STEP 4: KOIDE PARAMETRIZATION")
print("-" * 50)

# M = (sum sqrt(m)) / 3
M_param = simplify((sqrt_me + sqrt_mmu + sqrt_mtau_pred) / 3, 40)
M_squared = simplify(M_param * M_param, 40)

print(f"  M = {float(M_param):.10f} MeV^(1/2)")
print(f"  M^2 = {float(M_squared):.4f} MeV")

# Compare M^2 to m_proton/3
m_proton = Fraction(93827208816, 100000000)  # 938.27208816 MeV
m_proton_over_3 = m_proton / 3

print(f"  m_proton/3 = {float(m_proton_over_3):.4f} MeV")
print(f"  M^2 / (m_p/3) = {float(M_squared / m_proton_over_3):.6f}")
print(f"  Difference: {float((M_squared - m_proton_over_3)/m_proton_over_3 * 100):.2f}%")
print()

# Extract theta_0
sqrt2 = rat_sqrt(Fraction(2))
cos_theta0 = simplify((sqrt_me / M_param - 1) / sqrt2, 40)

theta0 = math.acos(float(cos_theta0))
theta0_deg = math.degrees(theta0)

# Cabibbo angle
theta_C = math.asin(0.2253)
theta_C_deg = math.degrees(theta_C)

print(f"  cos(theta_0) = {float(cos_theta0):.10f}")
print(f"  theta_0 = {theta0:.8f} rad = {theta0_deg:.4f}°")
print(f"  Cabibbo angle = {theta_C:.8f} rad = {theta_C_deg:.4f}°")
print(f"  Difference: {abs(theta0_deg - theta_C_deg):.4f}°")
print()


# ================================================================
# The 2/3 connection
# ================================================================

print("=" * 70)
print("THE 2/3 IN TWO CONTEXTS")
print("=" * 70)
print()
print("Context 1 — Koide formula:")
print("  Three lepton inertias at 120° in sqrt(inertia) space")
print("  Constraint constant = 2/3")
print()
print("Context 2 — Subtracted VP (PHYS-5):")
print("  Feynman parameter integral: -5/3 (unsubtracted)")
print("  After subtraction: -2/3")
print("  Per fermion boundary constant: 1/3 = (2/3)/2")
print()
print("Both involve three fermion species (e, mu, tau / u, d, s / ...)")
print("Both produce the rational 2/3")
print("Connection status: OPEN")
print()


# ================================================================
# Proof of integer arithmetic
# ================================================================

print("=" * 70)
print("PROOF OF INTEGER ARITHMETIC")
print("=" * 70)
print()

items = {
    "m_e": m_e,
    "m_mu": m_mu,
    "m_tau_predicted": m_tau_predicted,
    "koide_ratio": koide_ratio,
    "two_thirds": two_thirds,
    "M_param": M_param,
    "cos_theta0": cos_theta0,
}

all_frac = True
for name, val in items.items():
    ok = isinstance(val, Fraction)
    if not ok:
        all_frac = False
    print(f"  {name:<25}: {type(val).__name__:>10}  {'PASS' if ok else 'FAIL'}")

print()
print(f"All Fraction: {'YES' if all_frac else 'NO'}")
print()


# ================================================================
# Summary
# ================================================================

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print(f"  Koide ratio (measured):     {mp.nstr(koide_mp, 15)}")
print(f"  2/3:                        0.666666666666667")
print(f"  Deviation:                  {mp.nstr(abs(diff_mp)/(mpf(2)/3)*100, 6)}%")
print()
print(f"  m_tau (Koide, exact 2/3):   {float(m_tau_predicted):.4f} MeV")
print(f"  m_tau (PDG):                {float(m_tau_measured):.4f} MeV ± {float(m_tau_uncertainty)}")
print(f"  Tension:                    {sigma:.2f}σ")
print()
print("  If Koide exact: 18 → 17 free parameters")
print("  m_tau determined by m_e, m_mu, and the integer 2/3")
