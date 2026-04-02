"""
Gatto-Sartori-Tonin and Extended CKM-Mass Relations
All computation in controlled-precision rational arithmetic.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from math import gcd

def simplify(f, max_digits=40):
    n, d = f.numerator, f.denominator
    while n.bit_length() > int(max_digits * 3.32) or d.bit_length() > int(max_digits * 3.32):
        n //= 2
        d //= 2
    if d == 0: d = 1
    g = gcd(abs(n), abs(d))
    return Fraction(n // g, d // g)

def rat_sqrt(x, iters=20):
    if x == Fraction(0): return Fraction(0)
    g = Fraction(int(float(x) ** 0.5 * 10**18), 10**18)
    for i in range(iters):
        g = (g + x / g) / 2
        if i % 3 == 2: g = simplify(g, 40)
    return simplify(g, 40)

# Quark inertias (MSbar at 2 GeV, PDG 2024) — all Fraction
m_u = Fraction(216, 100)     # 2.16 MeV
m_d = Fraction(467, 100)     # 4.67 MeV
m_s = Fraction(934, 10)      # 93.4 MeV
m_c = Fraction(1270, 1)      # 1270 MeV
m_b = Fraction(4180, 1)      # 4180 MeV
m_t = Fraction(172690, 1)    # 172690 MeV

# CKM angles — all Fraction
sin12 = Fraction(2253, 10000)    # 0.2253
sin23 = Fraction(412, 10000)     # 0.0412
sin13 = Fraction(350, 100000)    # 0.00350

print("=" * 65)
print("CKM-MASS RELATIONS IN INTEGER ARITHMETIC")
print("=" * 65)
print()
print("All inputs are Fraction:")
print(f"  m_u = {m_u}, m_d = {m_d}, m_s = {m_s}")
print(f"  m_c = {m_c}, m_b = {m_b}, m_t = {m_t}")
print(f"  sin12 = {sin12}, sin23 = {sin23}, sin13 = {sin13}")
print()

# The three relations
sqrt_ds = rat_sqrt(m_d / m_s)
sqrt_uc = rat_sqrt(m_u / m_c)
sqrt_ut = rat_sqrt(m_u / m_t)

print("=" * 65)
print("THE THREE RELATIONS")
print("=" * 65)
print()
for label, computed, measured, name in [
    ("sqrt(m_d/m_s)", sqrt_ds, sin12, "sin12"),
    ("sqrt(m_u/m_c)", sqrt_uc, sin23, "sin23"),
    ("sqrt(m_u/m_t)", sqrt_ut, sin13, "sin13"),
]:
    diff_pct = (float(computed) / float(measured) - 1) * 100
    print(f"  {label:20s} = {float(computed):.6f}")
    print(f"  {name:20s} = {float(measured):.6f}")
    print(f"  {'Difference':20s} = {diff_pct:+.2f}%")
    print()

# Independence check
sqrt_ct = rat_sqrt(m_c / m_t)
ratio_13_23 = sin13 / sin23  # Fraction / Fraction = Fraction
print("=" * 65)
print("INDEPENDENCE CHECK")
print("=" * 65)
print()
print(f"  sin13 / sin23       = {float(ratio_13_23):.6f}")
print(f"  sqrt(m_c / m_t)     = {float(sqrt_ct):.6f}")
print(f"  Difference          = {(float(ratio_13_23)/float(sqrt_ct)-1)*100:+.2f}%")
print()
print("  Relations 2 and 3 share m_u — NOT independent.")
print("  Two independent constraints. Third is consistency check.")
print()

# All down-type ratios for comparison (Fritzsch-type)
sqrt_sb = rat_sqrt(m_s / m_b)
sqrt_db = rat_sqrt(m_d / m_b)
print("=" * 65)
print("STANDARD FRITZSCH (down-type only) — FAILS for theta_23")
print("=" * 65)
print()
print(f"  sqrt(m_d/m_s) = {float(sqrt_ds):.6f}  vs  sin12 = {float(sin12):.6f}  ({(float(sqrt_ds)/float(sin12)-1)*100:+.2f}%)")
print(f"  sqrt(m_s/m_b) = {float(sqrt_sb):.6f}  vs  sin23 = {float(sin23):.6f}  ({(float(sqrt_sb)/float(sin23)-1)*100:+.1f}%)")
print(f"  sqrt(m_d/m_b) = {float(sqrt_db):.6f}  vs  sin13 = {float(sin13):.6f}  ({(float(sqrt_db)/float(sin13)-1)*100:+.1f}%)")
print()
print("  Fritzsch down-type FAILS for theta_23 (263% off)")
print("  Fritzsch down-type FAILS for theta_13 (855% off)")
print()

# Parameter reduction
print("=" * 65)
print("PARAMETER REDUCTION")
print("=" * 65)
print()
print("  Two independent relations:")
print("    sin(theta_12) = sqrt(inertia_d / inertia_s)")
print("    sin(theta_23) = sqrt(inertia_u / inertia_c)")
print()
print("  Derived consistency check:")
print("    sin(theta_13) = sqrt(inertia_u / inertia_t)")
print("    = sin(theta_23) * sqrt(inertia_c / inertia_t)")
print()
print("  If exact: 17 -> 15 (two CKM angles from quark masses)")
print("  delta_CP remains free")
print()

# Verify all components are Fraction
print("=" * 65)
print("ARITHMETIC VERIFICATION")
print("=" * 65)
print()
for name, val in [("m_d/m_s", m_d/m_s), ("sqrt_ds", sqrt_ds),
                   ("m_u/m_c", m_u/m_c), ("sqrt_uc", sqrt_uc),
                   ("m_u/m_t", m_u/m_t), ("sqrt_ut", sqrt_ut),
                   ("sin12", sin12), ("sin23", sin23), ("sin13", sin13),
                   ("sin13/sin23", ratio_13_23)]:
    print(f"  {name:<15}: {type(val).__name__:>10}  {'PASS' if isinstance(val, Fraction) else 'FAIL'}")
    