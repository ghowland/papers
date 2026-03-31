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

# ================================================================
# Quark inertias (MSbar at 2 GeV, PDG 2024)
# ================================================================

m_u = Fraction(216, 100)     # 2.16 MeV
m_d = Fraction(467, 100)     # 4.67 MeV
m_s = Fraction(934, 10)      # 93.4 MeV
m_c = Fraction(1270, 1)      # 1270 MeV
m_b = Fraction(4180, 1)      # 4180 MeV
m_t = Fraction(172690, 1)    # 172690 MeV (pole mass, not MSbar)

# For t quark, MSbar at m_t scale is ~163 GeV
m_t_msbar = Fraction(163000, 1)  # approximate MSbar

print("=" * 65)
print("KOIDE TEST FOR QUARK SECTORS")
print("=" * 65)
print()

# Koide ratio: (m1 + m2 + m3) / (sqrt(m1) + sqrt(m2) + sqrt(m3))^2
# = 2/3 for charged leptons

def koide_ratio(m1, m2, m3, label):
    s1 = rat_sqrt(m1)
    s2 = rat_sqrt(m2)
    s3 = rat_sqrt(m3)
    num = m1 + m2 + m3
    den = (s1 + s2 + s3) * (s1 + s2 + s3)
    ratio = num / den
    print(f"  {label}:")
    print(f"    masses: {float(m1):.4f}, {float(m2):.4f}, {float(m3):.4f}")
    print(f"    sum(m) = {float(num):.4f}")
    print(f"    (sum sqrt(m))^2 = {float(den):.4f}")
    print(f"    Koide ratio = {float(ratio):.6f}")
    print(f"    vs 2/3 =       0.666667")
    print(f"    difference:     {float(ratio) - 2/3:+.6f} ({(float(ratio)/(2/3) - 1)*100:+.2f}%)")
    print()
    return ratio

# Charged leptons (reference)
m_e = Fraction(51099895, 100000000)
m_mu = Fraction(1056583755, 10000000)
m_tau = Fraction(177686, 100)

koide_ratio(m_e, m_mu, m_tau, "Charged leptons (e, mu, tau)")

# Down-type quarks
koide_ratio(m_d, m_s, m_b, "Down-type quarks (d, s, b) — MSbar 2 GeV")

# Up-type quarks with pole m_t
koide_ratio(m_u, m_c, m_t, "Up-type quarks (u, c, t) — pole m_t")

# Up-type quarks with MSbar m_t
koide_ratio(m_u, m_c, m_t_msbar, "Up-type quarks (u, c, t) — MSbar m_t")

# What Koide ratio DO the quarks give?
# And: what amplitude 'a' does each correspond to?
# From PHYS-8: ratio = (1 + a^2/2) / 3
# So a^2 = 2 * (3*ratio - 1)

print("=" * 65)
print("AMPLITUDE EXTRACTION")
print("=" * 65)
print()

for label, m1, m2, m3 in [
    ("Leptons", m_e, m_mu, m_tau),
    ("Down quarks", m_d, m_s, m_b),
    ("Up quarks (pole t)", m_u, m_c, m_t),
    ("Up quarks (MSbar t)", m_u, m_c, m_t_msbar),
]:
    s1, s2, s3 = rat_sqrt(m1), rat_sqrt(m2), rat_sqrt(m3)
    num = m1 + m2 + m3
    den = (s1 + s2 + s3) * (s1 + s2 + s3)
    ratio = float(num) / float(den)
    a_sq = 2 * (3 * ratio - 1)
    print(f"  {label}:")
    print(f"    Koide ratio = {ratio:.6f}")
    print(f"    a^2 = 2*(3*ratio - 1) = {a_sq:.6f}")
    print(f"    a = {a_sq**0.5:.6f}" if a_sq > 0 else f"    a^2 < 0 — outside Koide parametrization")
    print(f"    Koide (a=sqrt(2)): a^2 = 2.000")
    print()

# Also check: are quarks equally spaced on a circle?
# If so, the phases should be 120 degrees apart
# sqrt(m_i) = M * (1 + a*cos(theta_0 + 2*pi*i/3))
# This means sqrt(m) values should satisfy certain sum rules

print("=" * 65)
print("EQUAL SPACING CHECK")
print("=" * 65)
print()

for label, m1, m2, m3 in [
    ("Leptons", m_e, m_mu, m_tau),
    ("Down quarks", m_d, m_s, m_b),
    ("Up quarks (pole t)", m_u, m_c, m_t),
]:
    s1, s2, s3 = float(rat_sqrt(m1)), float(rat_sqrt(m2)), float(rat_sqrt(m3))
    S = s1 + s2 + s3
    M = S / 3  # from equal spacing: sum = 3M
    # residuals from M
    r1, r2, r3 = s1 - M, s2 - M, s3 - M
    # if equal spacing: r_i = a*M*cos(theta + 2pi*i/3)
    # sum of r_i = 0 (guaranteed)
    # sum of r_i^2 = (3/2)*a^2*M^2
    sum_r2 = r1**2 + r2**2 + r3**2
    a_sq_from_spacing = 2 * sum_r2 / (3 * M**2)
    print(f"  {label}:")
    print(f"    sqrt(m): {s1:.6f}, {s2:.6f}, {s3:.6f}")
    print(f"    M = sum/3 = {M:.6f}")
    print(f"    residuals: {r1:.6f}, {r2:.6f}, {r3:.6f}")
    print(f"    sum(residuals) = {r1+r2+r3:.2e} (should be ~0)")
    print(f"    a^2 from spacing = {a_sq_from_spacing:.6f}")
    # Check if residuals are consistent with 120-degree spacing
    # For 120 degrees: r1*r2 + r2*r3 + r1*r3 = -3/2 * a^2 * M^2 / 2... 
    # Actually check the cos pattern directly
    import math
    if abs(r1) > 1e-10 and abs(r2) > 1e-10:
        # reconstruct angles
        angles = []
        for r in [r1, r2, r3]:
            cos_val = r / (math.sqrt(a_sq_from_spacing) * M) if a_sq_from_spacing > 0 else 0
            cos_val = max(-1, min(1, cos_val))
            angles.append(math.acos(cos_val) * 180 / math.pi)
        print(f"    reconstructed angles: {angles[0]:.1f}°, {angles[1]:.1f}°, {angles[2]:.1f}°")
        # spacing
        print(f"    spacing: {abs(angles[1]-angles[0]):.1f}°, {abs(angles[2]-angles[1]):.1f}°")
        print(f"    equal spacing would be 120°, 120°, 120°")
    print()
    