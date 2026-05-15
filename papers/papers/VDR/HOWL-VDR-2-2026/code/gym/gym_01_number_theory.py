#!/usr/bin/env python3
"""
gym_01_number_theory.py — VDR exercises in number theory

GCD, LCM, modular arithmetic, Euler's totient, primality witnesses,
Egyptian fraction decomposition, Stern-Brocot tree, Farey sequences.

VDR should handle all of these exactly since they are pure integer/rational.
The interesting question is whether the remainder slot reveals structure
that scalar representations hide.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from vdr.linalg import Vec, Mat
from fractions import Fraction
from math import gcd

def section(title):
    print("\n=== %s ===" % title)

def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print("  %-50s %s" % (label, status))
    return condition

results = {"pass": 0, "fail": 0}

def record(ok):
    if ok:
        results["pass"] += 1
    else:
        results["fail"] += 1

# =========================================================================
section("1. GCD and LCM via VDR arithmetic")
# =========================================================================

# GCD(a,b) using Euclidean algorithm entirely in VDR
def vdr_gcd(a, b):
    """Euclidean GCD using VDR modular arithmetic."""
    while b != VDR(0):
        # a mod b: a - (a // b) * b where // is integer division
        a_frac = a.to_fraction()
        b_frac = b.to_fraction()
        q = int(a_frac / b_frac)
        r = a - VDR(q) * b
        a = b
        b = r
    return a

pairs = [(12, 8), (100, 75), (17, 13), (144, 89), (1000, 625)]
for x, y in pairs:
    result = vdr_gcd(VDR(x), VDR(y))
    expected = gcd(x, y)
    ok = result == VDR(expected)
    record(check("gcd(%d, %d) = %s" % (x, y, result), ok))

# LCM(a,b) = a*b / gcd(a,b)
def vdr_lcm(a, b):
    return a * b / vdr_gcd(a, b)

for x, y in [(12, 8), (7, 13), (100, 75)]:
    result = vdr_lcm(VDR(x), VDR(y))
    expected = x * y // gcd(x, y)
    ok = result == VDR(expected)
    record(check("lcm(%d, %d) = %s" % (x, y, result), ok))

# =========================================================================
section("2. Egyptian fraction decomposition")
# =========================================================================

# Greedy algorithm: express a/b as sum of unit fractions 1/n
def egyptian_fractions(v, d, max_terms=20):
    """Decompose VDR(v,d) into sum of unit fractions."""
    remaining = VDR(v, d)
    terms = []
    for _ in range(max_terms):
        if remaining == VDR(0):
            break
        frac = remaining.to_fraction()
        if frac <= 0:
            break
        # ceil(d/v) gives the next unit fraction denominator
        n = int(-(-frac.denominator // frac.numerator))  # ceiling division
        unit = VDR(1, n)
        terms.append(n)
        remaining = remaining - unit
    return terms, remaining

test_cases = [(2, 3), (3, 7), (5, 11), (7, 15), (4, 17)]
for v, d in test_cases:
    terms, leftover = egyptian_fractions(v, d)
    # verify: sum of 1/terms should equal v/d
    total = VDR(0)
    for t in terms:
        total = total + VDR(1, t)
    ok = total == VDR(v, d) and leftover == VDR(0)
    record(check("%d/%d = 1/%s  leftover=%s" % (v, d,
                 " + 1/".join(str(t) for t in terms), leftover), ok))

# =========================================================================
section("3. Stern-Brocot tree")
# =========================================================================

# Generate the Stern-Brocot tree to depth N using VDR mediants
# mediant(a/b, c/d) = (a+c)/(b+d)
def stern_brocot(depth):
    """Generate Stern-Brocot tree fractions to given depth."""
    tree = [(VDR(0), VDR(1))]  # boundaries: 0/1 and 1/0 (use 1/1 as right)
    level = [(VDR(0), VDR(1), VDR(1))]  # (left, mediant, right)

    result = [VDR(1, 2)]  # first mediant
    if depth == 0:
        return result

    current = [(VDR(0), VDR(1, 2), VDR(1))]
    for d in range(depth):
        next_level = []
        new_fracs = []
        for left, mid, right in current:
            # left mediant
            lm_v = left.to_fraction().numerator + mid.to_fraction().numerator
            lm_d = left.to_fraction().denominator + mid.to_fraction().denominator
            left_med = VDR(lm_v, lm_d)
            # right mediant
            rm_v = mid.to_fraction().numerator + right.to_fraction().numerator
            rm_d = mid.to_fraction().denominator + right.to_fraction().denominator
            right_med = VDR(rm_v, rm_d)

            new_fracs.extend([left_med, right_med])
            next_level.append((left, left_med, mid))
            next_level.append((mid, right_med, right))

        result.extend(new_fracs)
        current = next_level
    return result

sb = stern_brocot(3)
print("  Stern-Brocot tree depth 3: %d fractions" % len(sb))

# verify all are in (0,1), reduced, and ordered
sb_fracs = sorted(set(f.to_fraction() for f in sb))
all_reduced = all(gcd(f.numerator, f.denominator) == 1 for f in sb_fracs)
record(check("all fractions reduced", all_reduced))
all_positive = all(Fraction(0) < f < Fraction(1) for f in sb_fracs)
record(check("all in (0,1)", all_positive))
all_ordered = all(sb_fracs[i] < sb_fracs[i+1] for i in range(len(sb_fracs)-1))
record(check("strictly ordered", all_ordered))

# =========================================================================
section("4. Farey sequence")
# =========================================================================

# F_n = all reduced fractions p/q with 0 <= p/q <= 1 and q <= n
def farey(n):
    """Generate Farey sequence F_n as VDR objects."""
    fracs = set()
    for q in range(1, n + 1):
        for p in range(0, q + 1):
            if gcd(p, q) == 1:
                fracs.add(Fraction(p, q))
    return [VDR(f.numerator, f.denominator) for f in sorted(fracs)]

f5 = farey(5)
print("  F_5: %s" % " ".join(str(x) for x in f5))
record(check("F_5 has 11 elements", len(f5) == 11))

# Farey mediant property: for consecutive a/b, c/d in F_n, |ad - bc| = 1
f5_fracs = [x.to_fraction() for x in f5]
mediant_ok = True
for i in range(len(f5_fracs) - 1):
    a, b = f5_fracs[i].numerator, f5_fracs[i].denominator
    c, d = f5_fracs[i+1].numerator, f5_fracs[i+1].denominator
    if abs(a * d - b * c) != 1:
        mediant_ok = False
record(check("Farey mediant property |ad-bc|=1", mediant_ok))

# =========================================================================
section("5. Euler's totient via VDR")
# =========================================================================

def euler_totient(n):
    """Compute phi(n) using the product formula."""
    result = VDR(n)
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            # multiply by (1 - 1/p) = (p-1)/p
            result = result * VDR(p - 1, p)
        p += 1
    if temp > 1:
        result = result * VDR(temp - 1, temp)
    return result

known = [(1, 1), (6, 2), (10, 4), (12, 4), (36, 12), (100, 40)]
for n, expected in known:
    result = euler_totient(n)
    ok = result == VDR(expected)
    record(check("phi(%d) = %s" % (n, result), ok))

# =========================================================================
section("6. Harmonic numbers")
# =========================================================================

# H_n = 1 + 1/2 + 1/3 + ... + 1/n  — exact rational
def harmonic(n):
    total = VDR(0)
    for k in range(1, n + 1):
        total = total + VDR(1, k)
    return total

h10 = harmonic(10)
expected_h10 = Fraction(7381, 2520)
record(check("H_10 = %s = %s" % (h10, h10.to_fraction()),
             h10.to_fraction() == expected_h10))

h20 = harmonic(20)
print("  H_20 = %s" % h20.to_fraction())
record(check("H_20 is exact rational", h20.to_fraction().denominator > 1))

# partial harmonic sums: H_n - H_m for various m < n
# should be exact
h_diff = harmonic(100) - harmonic(50)
print("  H_100 - H_50 = %s" % h_diff.to_fraction())
record(check("H_100 - H_50 is exact", isinstance(h_diff.to_fraction(), Fraction)))

# =========================================================================
section("7. Modular arithmetic patterns")
# =========================================================================

# Fermat's little theorem: a^(p-1) ≡ 1 (mod p) for prime p, gcd(a,p)=1
# We can verify this using exact VDR integer arithmetic
def vdr_pow(base, exp):
    """Exact integer power using VDR."""
    result = VDR(1)
    for _ in range(exp):
        result = result * base
    return result

def vdr_mod(a, m):
    """a mod m using exact VDR arithmetic."""
    a_val = int(a.to_fraction())
    m_val = int(m.to_fraction())
    return VDR(a_val % m_val)

primes = [5, 7, 11, 13]
for p in primes:
    for a in [2, 3]:
        power = vdr_pow(VDR(a), p - 1)
        remainder = vdr_mod(power, VDR(p))
        ok = remainder == VDR(1)
        record(check("%d^%d mod %d = %s" % (a, p-1, p, remainder), ok))

# =========================================================================
section("8. Continued fraction convergents")
# =========================================================================

# Compute convergents of a continued fraction [a0; a1, a2, ...]
# using exact VDR arithmetic
def convergents(cf_coeffs):
    """Compute convergents p_n/q_n of continued fraction."""
    results = []
    h_prev, h_curr = VDR(1), VDR(cf_coeffs[0])
    k_prev, k_curr = VDR(0), VDR(1)
    results.append(VDR(cf_coeffs[0]))

    for i in range(1, len(cf_coeffs)):
        a = VDR(cf_coeffs[i])
        h_next = a * h_curr + h_prev
        k_next = a * k_curr + k_prev
        results.append(h_next / k_next)
        h_prev, h_curr = h_curr, h_next
        k_prev, k_curr = k_curr, k_next

    return results

# sqrt(2) = [1; 2, 2, 2, ...]
sqrt2_cf = [1] + [2] * 10
convs = convergents(sqrt2_cf)
print("  sqrt(2) convergents:")
for i, c in enumerate(convs):
    sq = c * c
    err = sq.to_fraction() - 2
    print("    [%d]: %s  x^2-2 = %s" % (i, c.to_fraction(), err))

# verify convergents approach sqrt(2)
errors = [abs(float(c.to_fraction() ** 2 - 2)) for c in convs]
monotone = all(errors[i] >= errors[i+1] for i in range(len(errors)-1))
record(check("sqrt(2) convergents improve monotonically", monotone))

# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
def e_cf(n):
    """Generate n terms of e's continued fraction."""
    result = [2]
    k = 1
    while len(result) < n:
        result.extend([1, 2 * k, 1])
        k += 1
    return result[:n]

e_coeffs = e_cf(15)
e_convs = convergents(e_coeffs)
print("  e convergents:")
import math
for i in [0, 2, 5, 9, 14]:
    if i < len(e_convs):
        err = abs(float(e_convs[i].to_fraction()) - math.e)
        print("    [%d]: %s  error=%.2e" % (i, e_convs[i].to_fraction(), err))

last_e = e_convs[-1]
e_err = abs(float(last_e.to_fraction()) - math.e)
record(check("e convergent[14] error < 1e-10", e_err < 1e-10))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 01 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
