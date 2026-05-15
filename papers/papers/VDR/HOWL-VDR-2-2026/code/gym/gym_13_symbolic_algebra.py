

#!/usr/bin/env python3
"""
gym_13_symbolic_algebra.py — VDR exercises in symbolic computation

Symbolic polynomial manipulation, partial fraction decomposition,
and rational function arithmetic — all exact VDR.
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

# reuse poly functions from gym_02
def poly_eval(p, x):
    result = VDR(0)
    for coeff in reversed(p):
        result = result * x + coeff
    return result

def poly_mul(p, q):
    n = len(p) + len(q) - 1
    result = [VDR(0)] * n
    for i in range(len(p)):
        for j in range(len(q)):
            result[i + j] = result[i + j] + p[i] * q[j]
    while len(result) > 1 and result[-1] == VDR(0):
        result.pop()
    return result

def poly_add(p, q):
    n = max(len(p), len(q))
    result = []
    for i in range(n):
        a = p[i] if i < len(p) else VDR(0)
        b = q[i] if i < len(q) else VDR(0)
        result.append(a + b)
    while len(result) > 1 and result[-1] == VDR(0):
        result.pop()
    return result

def poly_scale(p, s):
    return [c * s for c in p]

def poly_str(p):
    terms = []
    for i, c in enumerate(p):
        if c == VDR(0):
            continue
        cf = c.to_fraction()
        if i == 0:
            terms.append(str(cf))
        elif i == 1:
            terms.append("%s*x" % cf)
        else:
            terms.append("%s*x^%d" % (cf, i))
    return " + ".join(terms) if terms else "0"

# =========================================================================
section("1. Partial fraction decomposition (exact)")
# =========================================================================

# decompose p(x) / ((x-a)(x-b)) into A/(x-a) + B/(x-b)
# where a, b are distinct rational roots

def partial_fractions_simple(numerator, roots):
    """
    Decompose numerator(x) / product((x-r_i)) into sum of A_i/(x-r_i).
    Uses Heaviside cover-up: A_i = numerator(r_i) / product(r_i - r_j, j!=i).
    All exact VDR.
    """
    n = len(roots)
    coefficients = []
    for i in range(n):
        ri = roots[i]
        num_val = poly_eval(numerator, ri)
        denom_val = VDR(1)
        for j in range(n):
            if i != j:
                denom_val = denom_val * (ri - roots[j])
        coefficients.append(num_val / denom_val)
    return coefficients

# decompose 1 / ((x-1)(x-2)) = A/(x-1) + B/(x-2)
# numerator = [1] (constant 1)
# roots = [1, 2]
numerator = [VDR(1)]
roots = [VDR(1), VDR(2)]
coeffs = partial_fractions_simple(numerator, roots)
print("  1/((x-1)(x-2)) = %s/(x-1) + %s/(x-2)" % (
    coeffs[0].to_fraction(), coeffs[1].to_fraction()))
# should be -1/(x-1) + 1/(x-2)
record(check("A = -1", coeffs[0] == VDR(-1)))
record(check("B = 1", coeffs[1] == VDR(1)))

# verify at a test point: x = 3
# 1/((3-1)(3-2)) = 1/2
# -1/(3-1) + 1/(3-2) = -1/2 + 1 = 1/2
lhs = VDR(1) / ((VDR(3) - VDR(1)) * (VDR(3) - VDR(2)))
rhs = coeffs[0] / (VDR(3) - roots[0]) + coeffs[1] / (VDR(3) - roots[1])
record(check("PFD verified at x=3", lhs == rhs))

# more complex: (2x+3) / ((x-1)(x+1)(x-2))
numerator2 = [VDR(3), VDR(2)]  # 3 + 2x
roots2 = [VDR(1), VDR(-1), VDR(2)]
coeffs2 = partial_fractions_simple(numerator2, roots2)
print("  (2x+3)/((x-1)(x+1)(x-2)):")
for i, (c, r) in enumerate(zip(coeffs2, roots2)):
    print("    %s/(x - %s)" % (c.to_fraction(), r.to_fraction()))

# verify at x = 5
x_test = VDR(5)
lhs2 = poly_eval(numerator2, x_test)
denom = VDR(1)
for r in roots2:
    denom = denom * (x_test - r)
lhs2 = lhs2 / denom

rhs2 = VDR(0)
for c, r in zip(coeffs2, roots2):
    rhs2 = rhs2 + c / (x_test - r)
record(check("PFD verified at x=5", lhs2 == rhs2))

# =========================================================================
section("2. Rational function arithmetic")
# =========================================================================

# represent rational functions as (numerator_poly, denominator_poly)
# add: (p1/q1) + (p2/q2) = (p1*q2 + p2*q1) / (q1*q2)

def ratfun_add(pq1, pq2):
    p1, q1 = pq1
    p2, q2 = pq2
    num = poly_add(poly_mul(p1, q2), poly_mul(p2, q1))
    den = poly_mul(q1, q2)
    return num, den

def ratfun_mul(pq1, pq2):
    p1, q1 = pq1
    p2, q2 = pq2
    return poly_mul(p1, p2), poly_mul(q1, q2)

def ratfun_eval(pq, x):
    p, q = pq
    return poly_eval(p, x) / poly_eval(q, x)

# 1/(x-1) + 1/(x+1) = 2x/(x^2-1)
f1 = ([VDR(1)], [VDR(-1), VDR(1)])  # 1/(x-1)
f2 = ([VDR(1)], [VDR(1), VDR(1)])   # 1/(x+1)
f_sum = ratfun_add(f1, f2)
print("  1/(x-1) + 1/(x+1):")
print("    num: %s" % poly_str(f_sum[0]))
print("    den: %s" % poly_str(f_sum[1]))

# verify at x=3
val = ratfun_eval(f_sum, VDR(3))
expected = VDR(1) / VDR(2) + VDR(1) / VDR(4)  # 1/2 + 1/4 = 3/4
record(check("rational function sum at x=3", val == expected))

# =========================================================================
section("3. Power sums via exact rational algebra")
# =========================================================================

# S_k(n) = 1^k + 2^k + ... + n^k
# computed exactly as VDR rationals

def power_sum(k, n):
    """Exact power sum using VDR."""
    total = VDR(0)
    for i in range(1, n + 1):
        term = VDR(1)
        for _ in range(k):
            term = term * VDR(i)
        total = total + term
    return total

# known formulas:
# S_1(n) = n(n+1)/2
# S_2(n) = n(n+1)(2n+1)/6
# S_3(n) = [n(n+1)/2]^2

for n in [10, 50, 100]:
    s1 = power_sum(1, n)
    s1_formula = VDR(n) * VDR(n + 1) / VDR(2)
    record(check("S_1(%d) = %s" % (n, s1.to_fraction()), s1 == s1_formula))

    s2 = power_sum(2, n)
    s2_formula = VDR(n) * VDR(n + 1) * VDR(2 * n + 1) / VDR(6)
    record(check("S_2(%d) = %s" % (n, s2.to_fraction()), s2 == s2_formula))

    s3 = power_sum(3, n)
    s1_val = VDR(n) * VDR(n + 1) / VDR(2)
    s3_formula = s1_val * s1_val
    record(check("S_3(%d) = S_1(%d)^2" % (n, n), s3 == s3_formula))

# =========================================================================
section("4. Exact symbolic derivative of polynomial")
# =========================================================================

def poly_derivative(p):
    """Exact derivative of polynomial."""
    if len(p) <= 1:
        return [VDR(0)]
    return [VDR(i) * p[i] for i in range(1, len(p))]

def poly_integral(p, c=None):
    """Exact antiderivative with constant c."""
    if c is None:
        c = VDR(0)
    result = [c]
    for i, coeff in enumerate(p):
        result.append(coeff / VDR(i + 1))
    return result

# d/dx(x^3 + 2x^2 - x + 5) = 3x^2 + 4x - 1
p = [VDR(5), VDR(-1), VDR(2), VDR(1)]
dp = poly_derivative(p)
expected_dp = [VDR(-1), VDR(4), VDR(3)]
ok = all(a == b for a, b in zip(dp, expected_dp))
record(check("d/dx(x^3+2x^2-x+5) = 3x^2+4x-1", ok))

# integral of derivative should recover original (up to constant)
integral_dp = poly_integral(dp, p[0])
ok = all(a == b for a, b in zip(integral_dp, p))
record(check("integral of derivative recovers original", ok))

# =========================================================================
section("5. Definite integral via antiderivative (exact)")
# =========================================================================

def definite_integral(p, a, b):
    """Exact definite integral of polynomial from a to b."""
    anti = poly_integral(p)  # constant = 0
    return poly_eval(anti, b) - poly_eval(anti, a)

# integral of x^2 from 0 to 1 = 1/3
result = definite_integral([VDR(0), VDR(0), VDR(1)], VDR(0), VDR(1))
record(check("integral of x^2 from 0 to 1 = 1/3", result == VDR(1, 3)))

# integral of x^3 from 0 to 2 = 4
result = definite_integral([VDR(0), VDR(0), VDR(0), VDR(1)], VDR(0), VDR(2))
record(check("integral of x^3 from 0 to 2 = 4", result == VDR(4)))

# integral of 3x^2 + 2x + 1 from 1 to 3 = [x^3+x^2+x] from 1 to 3
# = (27+9+3) - (1+1+1) = 39 - 3 = 36
p = [VDR(1), VDR(2), VDR(3)]
result = definite_integral(p, VDR(1), VDR(3))
record(check("integral of 3x^2+2x+1 from 1 to 3 = 36", result == VDR(36)))

# rational bounds
result = definite_integral([VDR(0), VDR(0), VDR(1)], VDR(1, 3), VDR(2, 3))
print("  integral of x^2 from 1/3 to 2/3 = %s" % result.to_fraction())
expected = Fraction(2, 3) ** 3 / 3 - Fraction(1, 3) ** 3 / 3
record(check("integral with rational bounds", result.to_fraction() == expected))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 13 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)

