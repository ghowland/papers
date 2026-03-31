"""
Gatto-Sartori-Tonin Relation in Integer Arithmetic

sin(theta_C) = sqrt(m_d / m_s)

The Cabibbo angle (quark mixing between 1st and 2nd generation)
may be determined by the ratio of down-type quark inertias.

If exact, this connects CKM Group (4 params) to quark mass Group (6 params),
reducing independent parameters.

All computation in Fraction arithmetic with controlled-precision sqrt.
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
# Measured inputs
# ================================================================

# Quark masses: MSbar at 2 GeV (PDG 2024)
# These are inertias in PHYS-1 language
m_u = Fraction(216, 100)    # 2.16 +0.49/-0.26 MeV
m_d = Fraction(467, 100)    # 4.67 +0.48/-0.17 MeV
m_s = Fraction(934, 10)     # 93.4 +8.6/-3.4 MeV
m_c = Fraction(1270, 1)     # 1270 ± 20 MeV
m_b = Fraction(4180, 1)     # 4180 +30/-20 MeV
m_t = Fraction(172690, 1)   # 172690 ± 300 MeV

# CKM parameters (PDG 2024)
sin_theta12 = Fraction(2253, 10000)   # 0.2253 ± 0.0007
sin_theta23 = Fraction(412, 10000)    # 0.0412 ± 0.0008
sin_theta13 = Fraction(350, 100000)   # 0.00350 ± 0.00014

# Uncertainties for sigma calculations (as floats, for assessment only)
sin_theta12_unc = 0.0007
m_d_unc_up = 0.48
m_d_unc_down = 0.17
m_s_unc_up = 8.6
m_s_unc_down = 3.4

print("=" * 65)
print("GATTO-SARTORI-TONIN RELATION IN INTEGER ARITHMETIC")
print("=" * 65)
print()
print("MEASURED INPUTS (quark inertias, MSbar at 2 GeV):")
print(f"  m_d = {m_d} MeV ({float(m_d)} MeV, unc +{m_d_unc_up}/-{m_d_unc_down})")
print(f"  m_s = {m_s} MeV ({float(m_s)} MeV, unc +{m_s_unc_up}/-{m_s_unc_down})")
print(f"  m_d/m_s = {float(m_d/m_s):.6f}")
print()
print("CKM (PDG 2024):")
print(f"  sin(theta_12) = {float(sin_theta12)} ± {sin_theta12_unc}")
print()


# ================================================================
# Step 1: Test GST relation sin(theta_C) = sqrt(m_d/m_s)
# ================================================================

print("=" * 65)
print("STEP 1: THE GATTO-SARTORI-TONIN RELATION")
print("=" * 65)
print()

ratio_ds = m_d / m_s
sqrt_ratio = rat_sqrt(ratio_ds)

print(f"  m_d/m_s          = {float(ratio_ds):.6f}")
print(f"  sqrt(m_d/m_s)    = {float(sqrt_ratio):.6f}")
print(f"  sin(theta_C)     = {float(sin_theta12):.6f}")
print()

diff_gst = float(sqrt_ratio) - float(sin_theta12)
diff_pct = diff_gst / float(sin_theta12) * 100

print(f"  Difference       = {diff_gst:+.6f}")
print(f"  Relative         = {diff_pct:+.2f}%")
print()

# Sigma estimate (accounting for quark mass uncertainties)
# Propagate: delta(sqrt(m_d/m_s)) = (1/2) * sqrt(1/(m_d*m_s)) * delta_m_d
#            + similar for m_s
# Approximate: fractional unc of sqrt(ratio) = (1/2)*sqrt((delta_m_d/m_d)^2 + (delta_m_s/m_s)^2)
frac_unc_d = max(m_d_unc_up, m_d_unc_down) / float(m_d)
frac_unc_s = max(m_s_unc_up, m_s_unc_down) / float(m_s)
frac_unc_ratio = 0.5 * (frac_unc_d**2 + frac_unc_s**2)**0.5
abs_unc_sqrt = float(sqrt_ratio) * frac_unc_ratio

print(f"  Uncertainty on sqrt(m_d/m_s):")
print(f"    frac unc m_d = {frac_unc_d:.2f} ({frac_unc_d*100:.0f}%)")
print(f"    frac unc m_s = {frac_unc_s:.2f} ({frac_unc_s*100:.0f}%)")
print(f"    frac unc sqrt(ratio) = {frac_unc_ratio:.4f}")
print(f"    abs unc sqrt(ratio)  = ±{abs_unc_sqrt:.4f}")
print()

# Combined uncertainty
total_unc = (abs_unc_sqrt**2 + sin_theta12_unc**2)**0.5
sigma = abs(diff_gst) / total_unc
print(f"  Combined uncertainty = ±{total_unc:.4f}")
print(f"  Tension              = {sigma:.2f}σ")
print()


# ================================================================
# Step 2: Extended GST — Wolfenstein hierarchy
# ================================================================

print("=" * 65)
print("STEP 2: WOLFENSTEIN HIERARCHY")
print("=" * 65)
print()
print("  If sin(theta_12) ≈ sqrt(m_d/m_s), does the pattern extend?")
print("  Wolfenstein: theta_23 ~ lambda^2, theta_13 ~ lambda^3")
print("  where lambda = sin(theta_12) ≈ 0.2253")
print()

lambda_W = float(sin_theta12)
lambda2 = lambda_W ** 2
lambda3 = lambda_W ** 3

print(f"  sin(theta_12) = {float(sin_theta12):.6f}")
print(f"  lambda^2      = {lambda2:.6f}")
print(f"  sin(theta_23) = {float(sin_theta23):.6f}")
print(f"  Ratio s23/lambda^2 = {float(sin_theta23)/lambda2:.4f}")
print()
print(f"  lambda^3      = {lambda3:.6f}")
print(f"  sin(theta_13) = {float(sin_theta13):.6f}")
print(f"  Ratio s13/lambda^3 = {float(sin_theta13)/lambda3:.4f}")
print()


# ================================================================
# Step 3: Quark mass ratios — all six
# ================================================================

print("=" * 65)
print("STEP 3: ALL QUARK INERTIA RATIOS")
print("=" * 65)
print()

quarks = [("u", m_u), ("d", m_d), ("s", m_s), ("c", m_c), ("b", m_b), ("t", m_t)]

print("Down-type ratios (relevant to CKM):")
print(f"  m_d/m_s = {float(m_d/m_s):.6f}")
print(f"  m_s/m_b = {float(m_s/m_b):.6f}")
print(f"  m_d/m_b = {float(m_d/m_b):.6f}")
print()
print(f"  sqrt(m_d/m_s) = {float(rat_sqrt(m_d/m_s)):.6f}  vs sin(theta_12) = {float(sin_theta12):.6f}")
print(f"  sqrt(m_s/m_b) = {float(rat_sqrt(m_s/m_b)):.6f}  vs sin(theta_23) = {float(sin_theta23):.6f}")
print(f"  sqrt(m_d/m_b) = {float(rat_sqrt(m_d/m_b)):.6f}  vs sin(theta_13) = {float(sin_theta13):.6f}")
print()

# Check: does sqrt(m_s/m_b) ≈ sin(theta_23)?
sqrt_sb = rat_sqrt(m_s / m_b)
diff_23 = float(sqrt_sb) - float(sin_theta23)
print(f"  sqrt(m_s/m_b) vs sin(theta_23): diff = {diff_23:+.6f} ({diff_23/float(sin_theta23)*100:+.1f}%)")

sqrt_db = rat_sqrt(m_d / m_b)
diff_13 = float(sqrt_db) - float(sin_theta13)
print(f"  sqrt(m_d/m_b) vs sin(theta_13): diff = {diff_13:+.6f} ({diff_13/float(sin_theta13)*100:+.1f}%)")
print()

print("Up-type ratios:")
print(f"  m_u/m_c = {float(m_u/m_c):.6f}")
print(f"  m_c/m_t = {float(m_c/m_t):.6f}")
print(f"  m_u/m_t = {float(m_u/m_t):.8f}")
print()
print(f"  sqrt(m_u/m_c) = {float(rat_sqrt(m_u/m_c)):.6f}")
print(f"  sqrt(m_c/m_t) = {float(rat_sqrt(m_c/m_t)):.6f}")
print()


# ================================================================
# Step 4: The product relation
# ================================================================

print("=" * 65)
print("STEP 4: PRODUCT RELATIONS")
print("=" * 65)
print()

# If sin(theta_12) = sqrt(m_d/m_s) and sin(theta_23) = sqrt(m_s/m_b)
# then sin(theta_12)*sin(theta_23) = sqrt(m_d/m_b)
# which should ≈ sin(theta_13) if the CKM has a specific structure

product_12_23 = float(sin_theta12) * float(sin_theta23)
print(f"  sin(theta_12) * sin(theta_23) = {product_12_23:.6f}")
print(f"  sin(theta_13)                 = {float(sin_theta13):.6f}")
print(f"  Ratio = {product_12_23/float(sin_theta13):.4f}")
print()
print(f"  sqrt(m_d/m_s) * sqrt(m_s/m_b) = sqrt(m_d/m_b) = {float(sqrt_db):.6f}")
print(f"  sin(theta_13)                  = {float(sin_theta13):.6f}")
print(f"  Ratio = {float(sqrt_db)/float(sin_theta13):.4f}")
print()


# ================================================================
# Step 5: The Cabibbo angle as a mass ratio
# ================================================================

print("=" * 65)
print("STEP 5: WHAT WOULD EXACT GST MEAN?")
print("=" * 65)
print()

# If sin(theta_12) = sqrt(m_d/m_s) exactly, then:
# Given m_s, theta_12 determines m_d, or vice versa
# m_d = m_s * sin^2(theta_12)

m_d_from_gst = m_s * sin_theta12 * sin_theta12
print(f"  If GST exact: m_d = m_s * sin^2(theta_12)")
print(f"  m_d predicted = {float(m_d_from_gst):.4f} MeV")
print(f"  m_d measured  = {float(m_d):.4f} MeV")
print(f"  Difference    = {float(m_d_from_gst - m_d):+.4f} MeV")
print()

# Or: sin^2(theta_12) = m_d/m_s
sin2_from_masses = m_d / m_s
sin_from_masses = rat_sqrt(sin2_from_masses)
print(f"  sin^2(theta_12) from masses = {float(sin2_from_masses):.6f}")
print(f"  sin^2(theta_12) measured    = {float(sin_theta12*sin_theta12):.6f}")
print(f"  sin(theta_12) from masses   = {float(sin_from_masses):.6f}")
print(f"  sin(theta_12) measured      = {float(sin_theta12):.6f}")
print()


# ================================================================
# Proof of integer arithmetic
# ================================================================

print("=" * 65)
print("ARITHMETIC VERIFICATION")
print("=" * 65)
print()
print("  Note: controlled-precision rational arithmetic (same as Koide)")
print()

items = {
    "m_d": m_d,
    "m_s": m_s,
    "ratio_ds": ratio_ds,
    "sqrt_ratio": sqrt_ratio,
    "sin_theta12": sin_theta12,
    "m_d_from_gst": m_d_from_gst,
}

for name, val in items.items():
    ok = isinstance(val, Fraction)
    print(f"  {name:<20}: {type(val).__name__:>10}  {'PASS' if ok else 'FAIL'}")
print()


# ================================================================
# Summary
# ================================================================

print("=" * 65)
print("SUMMARY")
print("=" * 65)
print()
print(f"  GST relation: sin(theta_C) = sqrt(m_d/m_s)")
print(f"    sqrt(m_d/m_s)  = {float(sqrt_ratio):.6f}")
print(f"    sin(theta_C)   = {float(sin_theta12):.6f}")
print(f"    Difference     = {diff_pct:+.2f}%")
print(f"    Tension        = {sigma:.2f}σ (dominated by quark mass uncertainty)")
print()
print(f"  Extended GST:")
print(f"    sqrt(m_s/m_b) vs sin(theta_23): {diff_23/float(sin_theta23)*100:+.1f}%")
print(f"    sqrt(m_d/m_b) vs sin(theta_13): {diff_13/float(sin_theta13)*100:+.1f}%")
print()
print(f"  If GST exact for theta_12:")
print(f"    m_d is determined by m_s and sin(theta_12)")
print(f"    OR sin(theta_12) is determined by m_d and m_s")
print(f"    Either way: one fewer free parameter")
print()
print(f"  Quark mass uncertainties (~10%) dominate.")
print(f"  The 0.7% difference between sqrt(m_d/m_s) and sin(theta_C)")
print(f"  is well within measurement uncertainty.")
