#!/usr/bin/env python3
"""
gym_12_cryptographic_primitives.py — VDR exercises with modular arithmetic

Modular exponentiation, RSA-style key generation (toy sizes),
Chinese Remainder Theorem, and modular inverse — all exact VDR.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from fractions import Fraction

def section(title):
    print("\n=== %s ===" % title)

def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print("  %-55s %s" % (label, status))
    return condition

results = {"pass": 0, "fail": 0}
def record(ok):
    if ok: results["pass"] += 1
    else: results["fail"] += 1

# =========================================================================
section("1. Modular exponentiation (exact)")
# =========================================================================

def vdr_mod(a, m):
    return VDR(int(a.to_fraction()) % int(m.to_fraction()))

def vdr_pow_mod(base, exp, mod):
    """Exact modular exponentiation using repeated squaring."""
    result = VDR(1)
    b = vdr_mod(base, mod)
    e = int(exp.to_fraction())
    while e > 0:
        if e % 2 == 1:
            result = vdr_mod(result * b, mod)
        b = vdr_mod(b * b, mod)
        e //= 2
    return result

# Fermat's little theorem: a^(p-1) ≡ 1 (mod p)
for p in [7, 11, 13, 17, 23, 29, 31]:
    for a in [2, 3, 5]:
        result = vdr_pow_mod(VDR(a), VDR(p - 1), VDR(p))
        ok = result == VDR(1)
        record(check("%d^%d mod %d = %s" % (a, p-1, p, result), ok))

# =========================================================================
section("2. Extended Euclidean algorithm (exact)")
# =========================================================================

def extended_gcd(a, b):
    """Extended GCD: returns (gcd, x, y) such that a*x + b*y = gcd."""
    if b == VDR(0):
        return a, VDR(1), VDR(0)
    a_int = int(a.to_fraction())
    b_int = int(b.to_fraction())

    old_r, r = a_int, b_int
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return VDR(old_r), VDR(old_s), VDR(old_t)

# test
g, x, y = extended_gcd(VDR(35), VDR(15))
print("  gcd(35,15) = %s, 35*%s + 15*%s = %s" % (g, x, y, VDR(35)*x + VDR(15)*y))
record(check("gcd(35,15) = 5", g == VDR(5)))
record(check("Bezout identity holds", VDR(35) * x + VDR(15) * y == g))

# =========================================================================
section("3. Modular inverse (exact)")
# =========================================================================

def mod_inverse(a, m):
    """Modular inverse: a^(-1) mod m, exact VDR."""
    g, x, _ = extended_gcd(a, m)
    if g != VDR(1):
        return None  # not invertible
    return vdr_mod(x, m)

# test known inverses
test_cases = [(3, 7, 5), (5, 11, 9), (7, 13, 2)]
for a, m, expected in test_cases:
    inv = mod_inverse(VDR(a), VDR(m))
    print("  %d^(-1) mod %d = %s" % (a, m, inv))
    # verify: a * inv ≡ 1 (mod m)
    check_val = vdr_mod(VDR(a) * inv, VDR(m))
    record(check("%d * %d mod %d = 1" % (a, int(inv.to_fraction()), m),
                 check_val == VDR(1)))

# =========================================================================
section("4. Chinese Remainder Theorem (exact)")
# =========================================================================

def chinese_remainder(remainders, moduli):
    """
    Solve x ≡ r_i (mod m_i) for all i.
    Returns x mod M where M = product of all m_i.
    Exact VDR throughout.
    """
    M = VDR(1)
    for m in moduli:
        M = M * m

    result = VDR(0)
    for r, m in zip(remainders, moduli):
        Mi = M / m
        yi = mod_inverse(Mi, m)
        result = result + r * Mi * yi

    return vdr_mod(result, M)

# x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
remainders = [VDR(2), VDR(3), VDR(2)]
moduli = [VDR(3), VDR(5), VDR(7)]
x_crt = chinese_remainder(remainders, moduli)
print("  CRT solution: x = %s (mod 105)" % x_crt)

# verify
for r, m in zip(remainders, moduli):
    check_val = vdr_mod(x_crt, m)
    record(check("x mod %s = %s" % (m, r), check_val == r))

# =========================================================================
section("5. RSA toy example (exact)")
# =========================================================================

# toy RSA with small primes
p, q = 61, 53
n = p * q  # 3233
phi_n = (p - 1) * (q - 1)  # 3120
e = 17  # public exponent

# private exponent: d = e^(-1) mod phi(n)
d_vdr = mod_inverse(VDR(e), VDR(phi_n))
d = int(d_vdr.to_fraction())
print("  RSA toy: n=%d, e=%d, d=%d" % (n, e, d))

# verify: e*d ≡ 1 (mod phi(n))
record(check("e*d mod phi(n) = 1",
             vdr_mod(VDR(e) * VDR(d), VDR(phi_n)) == VDR(1)))

# encrypt and decrypt a message
message = 42
cipher = vdr_pow_mod(VDR(message), VDR(e), VDR(n))
decrypted = vdr_pow_mod(cipher, VDR(d), VDR(n))
print("  message=%d  cipher=%s  decrypted=%s" % (
    message, cipher, decrypted))
record(check("RSA decrypt recovers message", decrypted == VDR(message)))

# encrypt/decrypt several messages
for msg in [7, 100, 1234, 3000]:
    c = vdr_pow_mod(VDR(msg), VDR(e), VDR(n))
    m = vdr_pow_mod(c, VDR(d), VDR(n))
    ok = m == VDR(msg)
    record(check("RSA roundtrip message=%d" % msg, ok))

# =========================================================================
section("6. Discrete logarithm (baby-step giant-step, toy)")
# =========================================================================

def baby_giant(g, h, p):
    """
    Solve g^x ≡ h (mod p) using baby-step giant-step.
    Exact VDR modular arithmetic.
    """
    import math
    m = int(math.ceil(math.sqrt(int(p.to_fraction()))))

    # baby steps: g^j for j = 0..m-1
    table = {}
    power = VDR(1)
    for j in range(m):
        table[int(power.to_fraction())] = j
        power = vdr_mod(power * g, p)

    # giant step factor: g^(-m) mod p
    g_inv_m = vdr_pow_mod(mod_inverse(g, p), VDR(m), p)

    # giant steps
    gamma = h
    for i in range(m):
        gamma_int = int(gamma.to_fraction())
        if gamma_int in table:
            return VDR(i * m + table[gamma_int])
        gamma = vdr_mod(gamma * g_inv_m, p)

    return None

# solve 2^x ≡ 8 (mod 13) → x = 3
result = baby_giant(VDR(2), VDR(8), VDR(13))
print("  2^x ≡ 8 (mod 13): x = %s" % result)
record(check("discrete log: 2^3 = 8 mod 13", result == VDR(3)))

# solve 3^x ≡ 9 (mod 17) → x = ?
result2 = baby_giant(VDR(3), VDR(9), VDR(17))
print("  3^x ≡ 9 (mod 17): x = %s" % result2)
# verify
if result2 is not None:
    check_val = vdr_pow_mod(VDR(3), result2, VDR(17))
    record(check("3^%s mod 17 = 9" % result2, check_val == VDR(9)))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 12 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
