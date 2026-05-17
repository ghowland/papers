#!/usr/bin/env python3
"""
gym_06_combinatorics.py — VDR exercises in combinatorics

Binomial coefficients, Pascal's triangle, Stirling numbers,
Bell numbers, partition function, and generating functions.
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
section("1. Binomial coefficients via exact VDR")
# =========================================================================

def binom(n, k):
    """C(n,k) = n! / (k! * (n-k)!) computed as exact VDR."""
    if k < 0 or k > n:
        return VDR(0)
    result = VDR(1)
    for i in range(min(k, n - k)):
        result = result * VDR(n - i, i + 1)
    return result

# verify against known values
for n in range(8):
    row = [binom(n, k) for k in range(n + 1)]
    print("  C(%d,*) = %s" % (n, [int(c.to_fraction()) for c in row]))

record(check("C(7,3) = 35", binom(7, 3) == VDR(35)))
record(check("C(10,5) = 252", binom(10, 5) == VDR(252)))
record(check("C(20,10) = 184756", binom(20, 10) == VDR(184756)))

# Pascal's rule: C(n,k) = C(n-1,k-1) + C(n-1,k)
pascal_ok = True
for n in range(2, 15):
    for k in range(1, n):
        if binom(n, k) != binom(n-1, k-1) + binom(n-1, k):
            pascal_ok = False
record(check("Pascal's rule for n=2..14", pascal_ok))

# Vandermonde: C(m+n, r) = sum C(m,k)*C(n,r-k)
m, n, r = 5, 7, 6
lhs = binom(m + n, r)
rhs = VDR(0)
for k in range(r + 1):
    rhs = rhs + binom(m, k) * binom(n, r - k)
record(check("Vandermonde: C(12,6) = sum C(5,k)*C(7,6-k)", lhs == rhs))

# =========================================================================
section("2. Stirling numbers of the second kind")
# =========================================================================

# S(n,k) = number of ways to partition n elements into k non-empty subsets
# S(n,k) = k*S(n-1,k) + S(n-1,k-1), S(n,1)=S(n,n)=1
def stirling2(n, k):
    if k == 1 or k == n:
        return VDR(1)
    if k <= 0 or k > n:
        return VDR(0)
    return VDR(k) * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

known_s = {
    (3, 2): 3, (4, 2): 7, (4, 3): 6, (5, 2): 15,
    (5, 3): 25, (5, 4): 10, (6, 3): 90,
}
for (n, k), expected in known_s.items():
    result = stirling2(n, k)
    ok = result == VDR(expected)
    record(check("S(%d,%d) = %s" % (n, k, result), ok))

# =========================================================================
section("3. Bell numbers")
# =========================================================================

# B(n) = sum_{k=0}^{n} S(n,k)
def bell(n):
    total = VDR(0)
    for k in range(n + 1):
        total = total + stirling2(n, k)
    return total

known_bell = [1, 1, 2, 5, 15, 52, 203, 877]
for n, expected in enumerate(known_bell):
    result = bell(n)
    ok = result == VDR(expected)
    record(check("B(%d) = %s" % (n, result), ok))

# =========================================================================
section("4. Derangements")
# =========================================================================

# D(n) = n! * sum_{k=0}^{n} (-1)^k / k!
def derangement(n):
    factorial_n = VDR(1)
    for i in range(1, n + 1):
        factorial_n = factorial_n * VDR(i)

    total = VDR(0)
    factorial_k = VDR(1)
    for k in range(n + 1):
        if k > 0:
            factorial_k = factorial_k * VDR(k)
        sign = VDR(1) if k % 2 == 0 else VDR(-1)
        total = total + sign / factorial_k

    return factorial_n * total

known_der = [1, 0, 1, 2, 9, 44, 265, 1854]
for n, expected in enumerate(known_der):
    result = derangement(n)
    ok = result == VDR(expected)
    record(check("D(%d) = %s" % (n, result), ok))

# =========================================================================
section("5. Generating function evaluation")
# =========================================================================

# The generating function for Catalan numbers:
# C(x) = (1 - sqrt(1 - 4x)) / (2x)
# At x = 1/5: C(1/5) = (1 - sqrt(1/5)) / (2/5) = 5(1 - 1/sqrt(5))/2

# We can compute partial sums of the generating function:
# C(x) = sum_{n=0}^{N} C_n * x^n
def catalan(n):
    result = VDR(1)
    for k in range(2, n + 1):
        result = result * VDR(n + k, k)
    return result

def catalan_gf(x, terms):
    """Partial sum of Catalan generating function at x."""
    total = VDR(0)
    x_power = VDR(1)
    for n in range(terms):
        total = total + catalan(n) * x_power
        x_power = x_power * x
    return total

# evaluate at x = 1/10 (well within radius of convergence 1/4)
x = VDR(1, 10)
for terms in [5, 10, 20]:
    result = catalan_gf(x, terms)
    print("  C(1/10) with %d terms: %s = %.10f" % (
        terms, result.to_fraction(), float(result.to_fraction())))

# every partial sum is exact
record(check("Catalan GF partial sums are exact rationals",
             catalan_gf(VDR(1, 10), 10).to_fraction().denominator > 1))

# =========================================================================
section("6. Multinomial coefficients")
# =========================================================================

def multinomial(n, ks):
    """Multinomial coefficient n! / (k1! * k2! * ... * km!)"""
    result = VDR(1)
    for k in ks:
        for i in range(1, k + 1):
            result = result * VDR(n, i)
            n -= 1
    return result

# C(10; 3,3,4) = 10! / (3!*3!*4!) = 4200
result = multinomial(10, [3, 3, 4])
record(check("multinomial(10; 3,3,4) = 4200", result == VDR(4200)))

# multinomial theorem: sum of all multinomials = k^n
# for k=3, n=4: sum of C(4; a,b,c) for a+b+c=4 should be 3^4 = 81
total = VDR(0)
for a in range(5):
    for b in range(5 - a):
        c = 4 - a - b
        total = total + multinomial(4, [a, b, c])
record(check("sum of trinomials for n=4 = 3^4 = 81", total == VDR(81)))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 06 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
