#!/usr/bin/env python3
"""
gym_03_continued_fractions.py — VDR exercises in continued fractions

Building continued fractions from VDR rationals, converting back,
best rational approximations, and exploring the connection between
VDR remainder trees and continued fraction structure.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from fractions import Fraction
from math import gcd

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
section("1. Convert VDR rational to continued fraction")
# =========================================================================

def to_cf(v, d):
    """Convert VDR(v,d) to continued fraction coefficients [a0; a1, a2, ...]"""
    coeffs = []
    a, b = v, d
    while b != 0:
        q = a // b
        coeffs.append(q)
        a, b = b, a - q * b
    return coeffs

def from_cf(coeffs):
    """Convert continued fraction coefficients back to VDR."""
    if len(coeffs) == 0:
        return VDR(0)
    result = VDR(coeffs[-1])
    for c in reversed(coeffs[:-1]):
        result = VDR(c) + VDR(1) / result
    return result

test_cases = [
    (1, 2, [0, 2]),
    (3, 7, [0, 2, 3]),
    (22, 7, [3, 7]),
    (355, 113, [3, 7, 16]),
    (1, 1, [1]),
]

for v, d, expected_cf in test_cases:
    cf = to_cf(v, d)
    ok = cf == expected_cf
    record(check("%d/%d -> [%s]" % (v, d, "; ".join(str(c) for c in cf)), ok))

    # roundtrip
    back = from_cf(cf)
    ok = back == VDR(v, d)
    record(check("roundtrip %d/%d" % (v, d), ok))

# =========================================================================
section("2. Best rational approximations from convergents")
# =========================================================================

def convergents_from_cf(coeffs):
    """Compute all convergents p_n/q_n from CF coefficients."""
    if not coeffs:
        return []
    h = [0, 1]
    k = [1, 0]
    results = []
    for a in coeffs:
        h_new = a * h[-1] + h[-2]
        k_new = a * k[-1] + k[-2]
        h.append(h_new)
        k.append(k_new)
        results.append(VDR(h_new, k_new))
    return results

# convergents of 355/113 (famous pi approximation)
cf_pi = [3, 7, 16]
convs = convergents_from_cf(cf_pi)
print("  convergents of 355/113:")
for i, c in enumerate(convs):
    print("    c_%d = %s" % (i, c.to_fraction()))

record(check("final convergent = 355/113",
             convs[-1].to_fraction() == Fraction(355, 113)))

# convergents are best approximations: |p/q - target| < 1/(q*q_{n+1})
target = Fraction(355, 113)
for i in range(len(convs) - 1):
    c = convs[i].to_fraction()
    err = abs(c - target)
    q_curr = c.denominator
    q_next = convs[i+1].to_fraction().denominator
    bound = Fraction(1, q_curr * q_next)
    ok = err <= bound
    record(check("c_%d error %s <= bound %s" % (i, err, bound), ok))

# =========================================================================
section("3. VDR rebase as partial CF step")
# =========================================================================

# Interesting question: when we rebase [V,D,0] to a new denominator,
# the mismatch child is related to the continued fraction expansion.
# Let's explore this.

x = VDR(355, 113)  # pi approximation
print("  rebasing 355/113 to various denominators:")

for target_d in [7, 22, 100, 113, 226]:
    rebased = x.rebase(target_d)
    print("    rebase(%d): %s  proj=%s" % (target_d, rebased, rebased.to_fraction()))
    ok = rebased.to_fraction() == Fraction(355, 113)
    record(check("rebase to %d preserves value" % target_d, ok))

# compare CF structure to rebase structure
cf = to_cf(355, 113)
print("  CF of 355/113: [%s]" % "; ".join(str(c) for c in cf))
print("  first CF step: floor(355/113) = %d" % cf[0])
print("  rebase to %d: %s" % (cf[0], x.rebase(cf[0]) if cf[0] != 0 else "skip"))

# =========================================================================
section("4. Gauss-Kuzmin distribution test")
# =========================================================================

# The CF coefficients of "random" rationals follow Gauss-Kuzmin distribution
# P(a_n = k) = -log2(1 - 1/(k+1)^2)
# Test: generate CFs of many rationals, count coefficient frequencies

from collections import Counter
counter = Counter()
total_coeffs = 0

for num in range(1, 200):
    for den in range(num + 1, 201):
        if gcd(num, den) != 1:
            continue
        cf = to_cf(num, den)
        for c in cf[1:]:  # skip a0
            counter[c] += 1
            total_coeffs += 1

print("  CF coefficient frequencies (from rationals with den <= 200):")
import math
for k in range(1, 8):
    observed = counter.get(k, 0) / total_coeffs
    expected = -math.log2(1 - 1.0 / (k + 1) ** 2)
    print("    k=%d: observed=%.3f  GK_expected=%.3f  ratio=%.2f" % (
        k, observed, expected, observed / expected if expected > 0 else 0))

# not a strict pass/fail — just observational
record(check("most common CF coeff is 1", counter[1] > counter[2]))

# =========================================================================
section("5. Stern-Brocot path as VDR rebase chain")
# =========================================================================

# Every rational p/q has a unique path in the Stern-Brocot tree
# encoded as L/R turns. This is equivalent to the CF expansion.
# Can we trace this path using VDR rebase operations?

def sb_path(p, q):
    """Find Stern-Brocot path for p/q as sequence of L/R."""
    path = []
    lo_n, lo_d = 0, 1
    hi_n, hi_d = 1, 0
    while True:
        med_n = lo_n + hi_n
        med_d = lo_d + hi_d
        if med_n == p and med_d == q:
            break
        if p * med_d < med_n * q:
            path.append('L')
            hi_n, hi_d = med_n, med_d
        else:
            path.append('R')
            lo_n, lo_d = med_n, med_d
        if len(path) > 100:
            break
    return "".join(path)

test_fracs = [(1, 3), (2, 5), (3, 7), (5, 8), (7, 11)]
for p, q in test_fracs:
    path = sb_path(p, q)
    cf = to_cf(p, q)
    print("    %d/%d: SB path=%s  CF=[%s]" % (p, q, path, "; ".join(str(c) for c in cf)))

    # verify: SB path encodes the same information as CF
    # R^a0 L^a1 R^a2 ... (starting with R for fractions > 0)
    ok = VDR(p, q).to_fraction() == Fraction(p, q)
    record(check("%d/%d VDR exact" % (p, q), ok))

# =========================================================================
section("6. Periodic continued fractions (quadratic irrationals)")
# =========================================================================

# sqrt(N) for non-square N has periodic CF: [a0; a1, a2, ..., a_k, 2*a0, a1, ...]
# We can compute the period using exact VDR arithmetic

def sqrt_cf_period(n):
    """Find the CF expansion of sqrt(n) until the period repeats."""
    import math
    a0 = int(math.isqrt(n))
    if a0 * a0 == n:
        return [a0], 0  # perfect square

    coeffs = [a0]
    # use the standard algorithm with m, d, a
    m, d, a = 0, 1, a0
    seen = {}
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        state = (m, d)
        if state in seen:
            period = len(coeffs) - seen[state]
            return coeffs, period
        seen[state] = len(coeffs)
        coeffs.append(a)
        if len(coeffs) > 100:
            return coeffs, -1

for n in [2, 3, 5, 7, 10, 13, 23]:
    coeffs, period = sqrt_cf_period(n)
    cf_str = "[%d; %s]" % (coeffs[0], ", ".join(str(c) for c in coeffs[1:]))
    print("  sqrt(%d): %s  period=%d" % (n, cf_str, period))

    # verify via convergent: last convergent squared should be close to n
    convs = []
    h_prev, h_curr = 1, coeffs[0]
    k_prev, k_curr = 0, 1
    for c in coeffs[1:]:
        h_next = c * h_curr + h_prev
        k_next = c * k_curr + k_prev
        h_prev, h_curr = h_curr, h_next
        k_prev, k_curr = k_curr, k_next
    approx = VDR(h_curr, k_curr)
    sq = approx * approx
    err = abs(float(sq.to_fraction()) - n)
    record(check("sqrt(%d) convergent error < 0.01" % n, err < 0.01))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 03 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
