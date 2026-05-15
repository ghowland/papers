#!/usr/bin/env python3
"""
gym_02_polynomial.py — VDR exercises in polynomial arithmetic

Polynomial evaluation, construction, addition, multiplication,
division with remainder, root finding via rational root theorem,
interpolation, and resultants.

Polynomials are represented as lists of VDR coefficients.
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
# Polynomial representation: list of VDR coefficients, index = degree
# p = [a0, a1, a2, ...] means a0 + a1*x + a2*x^2 + ...
# =========================================================================

def poly_eval(p, x):
    """Evaluate polynomial at VDR point x using Horner's method."""
    result = VDR(0)
    for coeff in reversed(p):
        result = result * x + coeff
    return result

def poly_add(p, q):
    """Add two polynomials."""
    n = max(len(p), len(q))
    result = []
    for i in range(n):
        a = p[i] if i < len(p) else VDR(0)
        b = q[i] if i < len(q) else VDR(0)
        result.append(a + b)
    # trim trailing zeros
    while len(result) > 1 and result[-1] == VDR(0):
        result.pop()
    return result

def poly_mul(p, q):
    """Multiply two polynomials."""
    n = len(p) + len(q) - 1
    result = [VDR(0)] * n
    for i in range(len(p)):
        for j in range(len(q)):
            result[i + j] = result[i + j] + p[i] * q[j]
    while len(result) > 1 and result[-1] == VDR(0):
        result.pop()
    return result

def poly_scale(p, s):
    """Multiply polynomial by scalar."""
    return [c * s for c in p]

def poly_neg(p):
    """Negate polynomial."""
    return [-c for c in p]

def poly_degree(p):
    """Degree of polynomial."""
    d = len(p) - 1
    while d > 0 and p[d] == VDR(0):
        d -= 1
    return d

def poly_str(p):
    """String representation."""
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

def poly_divmod(p, q):
    """Polynomial division: p = quotient*q + remainder."""
    p = list(p)
    dq = poly_degree(q)
    dp = poly_degree(p)
    if dq > dp:
        return [VDR(0)], p

    quotient = [VDR(0)] * (dp - dq + 1)
    remainder = list(p)

    for i in range(dp - dq, -1, -1):
        coeff = remainder[i + dq] / q[dq]
        quotient[i] = coeff
        for j in range(dq + 1):
            remainder[i + j] = remainder[i + j] - coeff * q[j]

    # trim
    while len(remainder) > 1 and remainder[-1] == VDR(0):
        remainder.pop()
    while len(quotient) > 1 and quotient[-1] == VDR(0):
        quotient.pop()

    return quotient, remainder

# =========================================================================
section("1. Polynomial evaluation — Horner's method")
# =========================================================================

# p(x) = 2x^3 - 3x^2 + x - 5
p = [VDR(-5), VDR(1), VDR(-3), VDR(2)]
print("  p(x) = %s" % poly_str(p))

test_points = [(VDR(0), VDR(-5)), (VDR(1), VDR(-5)), (VDR(2), VDR(1)),
               (VDR(-1), VDR(-11)), (VDR(1, 2), VDR(-19, 4))]
for x, expected in test_points:
    result = poly_eval(p, x)
    ok = result == expected
    record(check("p(%s) = %s" % (x.to_fraction(), result.to_fraction()), ok))

# =========================================================================
section("2. Polynomial addition and multiplication")
# =========================================================================

# (x + 1)(x - 1) = x^2 - 1
p1 = [VDR(1), VDR(1)]    # x + 1
p2 = [VDR(-1), VDR(1)]   # x - 1
product = poly_mul(p1, p2)
expected = [VDR(-1), VDR(0), VDR(1)]  # x^2 - 1
ok = all(a == b for a, b in zip(product, expected))
record(check("(x+1)(x-1) = x^2 - 1", ok))

# (x + 1)^3 = x^3 + 3x^2 + 3x + 1
p_cubed = poly_mul(poly_mul(p1, p1), p1)
expected_cube = [VDR(1), VDR(3), VDR(3), VDR(1)]
ok = all(a == b for a, b in zip(p_cubed, expected_cube))
record(check("(x+1)^3 = x^3+3x^2+3x+1", ok))

# distributivity: p1 * (p2 + p3) = p1*p2 + p1*p3
p3 = [VDR(2), VDR(0), VDR(1)]  # x^2 + 2
lhs = poly_mul(p1, poly_add(p2, p3))
rhs = poly_add(poly_mul(p1, p2), poly_mul(p1, p3))
ok = all(a == b for a, b in zip(lhs, rhs)) and len(lhs) == len(rhs)
record(check("p1*(p2+p3) = p1*p2 + p1*p3", ok))

# =========================================================================
section("3. Polynomial division with remainder")
# =========================================================================

# (x^3 + 2x^2 - x - 2) / (x - 1) should give quotient x^2+3x+2, remainder 0
dividend = [VDR(-2), VDR(-1), VDR(2), VDR(1)]
divisor = [VDR(-1), VDR(1)]
quot, rem = poly_divmod(dividend, divisor)
print("  quotient: %s" % poly_str(quot))
print("  remainder: %s" % poly_str(rem))
ok = rem == [VDR(0)]
record(check("x^3+2x^2-x-2 divides evenly by x-1", ok))

# verify: quotient * divisor + remainder = dividend
recon = poly_add(poly_mul(quot, divisor), rem)
ok = all(a == b for a, b in zip(recon, dividend))
record(check("quotient * divisor + remainder = dividend", ok))

# non-exact division: x^2 + 1 divided by x - 1 gives remainder 2
dividend2 = [VDR(1), VDR(0), VDR(1)]
quot2, rem2 = poly_divmod(dividend2, divisor)
print("  (x^2+1)/(x-1): quot=%s rem=%s" % (poly_str(quot2), poly_str(rem2)))
ok = rem2 == [VDR(2)]
record(check("(x^2+1)/(x-1) remainder = 2", ok))

# =========================================================================
section("4. Rational root theorem")
# =========================================================================

# Find rational roots of p(x) = 2x^3 - 3x^2 - 3x + 2
# Rational root candidates: ±{1,2} / {1,2} = ±{1, 2, 1/2}
p = [VDR(2), VDR(-3), VDR(-3), VDR(2)]
print("  p(x) = %s" % poly_str(p))

def rational_roots(p):
    """Find all rational roots using rational root theorem."""
    a0 = abs(int(p[0].to_fraction()))
    an = abs(int(p[-1].to_fraction()))
    # factors of a0
    factors_a0 = [i for i in range(1, a0 + 1) if a0 % i == 0]
    factors_an = [i for i in range(1, an + 1) if an % i == 0]
    candidates = set()
    for p_val in factors_a0:
        for q_val in factors_an:
            candidates.add(Fraction(p_val, q_val))
            candidates.add(Fraction(-p_val, q_val))
    roots = []
    for c in sorted(candidates):
        x = VDR(c.numerator, c.denominator)
        if poly_eval(p, x) == VDR(0):
            roots.append(x)
    return roots

roots = rational_roots(p)
print("  rational roots: %s" % [r.to_fraction() for r in roots])
for r in roots:
    ok = poly_eval(p, r) == VDR(0)
    record(check("p(%s) = 0" % r.to_fraction(), ok))

# =========================================================================
section("5. Lagrange interpolation")
# =========================================================================

# Given points, construct the unique polynomial passing through them
def lagrange_interpolate(points):
    """
    Given [(x0,y0), (x1,y1), ...], return polynomial coefficients.
    Uses VDR exact arithmetic throughout.
    """
    n = len(points)
    # basis polynomials
    result = [VDR(0)] * n
    for i in range(n):
        # L_i(x) = product of (x - x_j)/(x_i - x_j) for j != i
        basis = [VDR(1)]
        for j in range(n):
            if i == j:
                continue
            xi = points[i][0]
            xj = points[j][0]
            denom = xi - xj
            # multiply basis by (x - xj) / denom = (-xj/denom) + (1/denom)*x
            factor = [VDR(0) - xj / denom, VDR(1) / denom]
            basis = poly_mul(basis, factor)
        # scale by y_i
        term = poly_scale(basis, points[i][1])
        result = poly_add(result, term)
    return result

# interpolate through (0,1), (1,3), (2,7) — should give 1 + x + x^2
points = [(VDR(0), VDR(1)), (VDR(1), VDR(3)), (VDR(2), VDR(7))]
p_interp = lagrange_interpolate(points)
print("  interpolated: %s" % poly_str(p_interp))

# verify at all points
for x, y in points:
    result = poly_eval(p_interp, x)
    ok = result == y
    record(check("p(%s) = %s" % (x.to_fraction(), y.to_fraction()), ok))

# verify coefficients: should be [1, 1, 1]
ok = (len(p_interp) == 3 and p_interp[0] == VDR(1)
      and p_interp[1] == VDR(1) and p_interp[2] == VDR(1))
record(check("coefficients are [1, 1, 1]", ok))

# rational points
points2 = [(VDR(1, 2), VDR(1, 3)), (VDR(1, 3), VDR(1, 5)), (VDR(1, 5), VDR(1, 7))]
p2 = lagrange_interpolate(points2)
print("  rational interpolation: %s" % poly_str(p2))
for x, y in points2:
    result = poly_eval(p2, x)
    ok = result == y
    record(check("p(%s) = %s" % (x.to_fraction(), y.to_fraction()), ok))

# =========================================================================
section("6. Polynomial GCD (Euclidean algorithm)")
# =========================================================================

def poly_gcd(p, q):
    """GCD of two polynomials via Euclidean algorithm."""
    while poly_degree(q) > 0 or q != [VDR(0)]:
        _, r = poly_divmod(p, q)
        p = q
        q = r
        if q == [VDR(0)]:
            break
    # normalize: make leading coefficient 1
    if p[-1] != VDR(0):
        lc = p[-1]
        p = [c / lc for c in p]
    return p

# gcd of (x^2-1) and (x^2+2x+1) should be (x+1)
p1 = [VDR(-1), VDR(0), VDR(1)]     # x^2 - 1
p2 = [VDR(1), VDR(2), VDR(1)]      # x^2 + 2x + 1
g = poly_gcd(p1, p2)
print("  gcd(x^2-1, x^2+2x+1) = %s" % poly_str(g))
expected_gcd = [VDR(1), VDR(1)]     # x + 1
ok = all(a == b for a, b in zip(g, expected_gcd)) and len(g) == len(expected_gcd)
record(check("poly gcd = x + 1", ok))

# =========================================================================
section("7. Characteristic polynomial of a matrix")
# =========================================================================

# For 2x2 matrix [[a,b],[c,d]], char poly = x^2 - (a+d)x + (ad-bc)
from vdr.linalg import Mat

def char_poly_2x2(m):
    """Characteristic polynomial of 2x2 VDR matrix."""
    a, b = m[0, 0], m[0, 1]
    c, d = m[1, 0], m[1, 1]
    trace = a + d
    det = a * d - b * c
    # x^2 - trace*x + det
    return [det, -trace, VDR(1)]

m = Mat.from_ints([[2, 1], [1, 3]])
cp = char_poly_2x2(m)
print("  char poly of [[2,1],[1,3]]: %s" % poly_str(cp))
# = x^2 - 5x + 5

# Cayley-Hamilton: m^2 - 5m + 5I = 0
m2 = m * m
result_ch = m2 - m * VDR(5) + Mat.identity(2) * VDR(5)
all_zero = all(result_ch[i, j] == VDR(0) for i in range(2) for j in range(2))
record(check("Cayley-Hamilton: m^2 - 5m + 5I = 0", all_zero))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 02 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
