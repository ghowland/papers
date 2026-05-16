#!/usr/bin/env python3
"""
gym_14_fixed_point.py — VDR exercises with fixed-point iteration

Banach fixed-point theorem applications, contraction mappings,
and iterated function systems — all exact VDR rational.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from vdr.fn import FnRemainder, resolve, make_iterative_fn
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
section("1. Fixed point of x = (x + 2/x) / 2 (sqrt(2))")
# =========================================================================

def sqrt2_step(x):
    return (x + VDR(2) / x) / VDR(2)

x = VDR(1)
print("  fixed point iteration for sqrt(2):")
for i in range(8):
    x = sqrt2_step(x)
    sq = x * x
    err = sq.to_fraction() - 2
    print("    step %d: %s  x^2-2 = %s" % (i+1, x.to_fraction(), err))

# x^2 should be very close to 2
record(check("x^2 - 2 denominator > 10^20 at step 5",
             (x * x - VDR(2)).to_fraction().denominator > 10**20))

# =========================================================================
section("2. Fixed point of x = cos(x) via rational approximation")
# =========================================================================

# cos(x) ≈ 1 - x^2/2 + x^4/24 (Taylor series, exact rational coefficients)
# fixed point of x = 1 - x^2/2 + x^4/24 - ...

def cos_approx(x, terms=6):
    """Exact rational Taylor approximation of cos(x)."""
    result = VDR(0)
    power = VDR(1)
    factorial = 1
    for n in range(terms):
        if n > 0:
            power = power * x
            factorial *= n
        if n % 2 == 0:
            sign = VDR(1) if (n // 2) % 2 == 0 else VDR(-1)
            result = result + sign * power / VDR(factorial)
    return result

# iterate x = cos_approx(x) starting from x = 1
x = VDR(1)
print("  fixed point of x = cos_Taylor(x):")
for i in range(10):
    x = cos_approx(x, terms=8)
    print("    step %d: %s ≈ %.10f" % (i+1, x.to_fraction(), float(x.to_fraction())))

import math
dottie = 0.739085133  # Dottie number (fixed point of cos)
err = abs(float(x.to_fraction()) - dottie)
print("  error from Dottie number: %.6e" % err)
record(check("approaches Dottie number (error < 0.01)", err < 0.01))

# =========================================================================
section("3. Contraction mapping: f(x) = x/2 + 1")
# =========================================================================

# fixed point: x = x/2 + 1 → x = 2
def contract(x):
    return x / VDR(2) + VDR(1)

x = VDR(100)
print("  f(x) = x/2 + 1, start at 100:")
for i in range(15):
    x = contract(x)
    print("    step %d: %s" % (i+1, x.to_fraction()))

# after enough steps should be very close to 2
# exact: x_n = 2 + (x_0 - 2) / 2^n = 2 + 98/2^n
for n in [5, 10, 15]:
    x_check = VDR(100)
    for _ in range(n):
        x_check = contract(x_check)
    expected = Fraction(2) + Fraction(98, 2 ** n)
    ok = x_check.to_fraction() == expected
    record(check("step %d = 2 + 98/2^%d" % (n, n), ok))

# =========================================================================
section("4. Fixed point as functional remainder")
# =========================================================================

# represent the iteration as a functional VDR
sqrt2_fn = make_iterative_fn("sqrt2_fp", sqrt2_step, VDR(1))
sqrt2_vdr = VDR(0, 1, sqrt2_fn)

for depth in [3, 5, 7]:
    resolved = resolve(sqrt2_vdr, depth)
    sq = resolved * resolved
    err = sq.to_fraction() - 2
    record(check("fn sqrt2 depth %d: x^2-2 denom > 10^%d" % (depth, depth*3),
                 abs(err.denominator) > 10 ** (depth * 3)))

# =========================================================================
section("5. Iterated affine map")
# =========================================================================

# f(x) = (2x + 3) / 5  — contraction with fixed point 1
def affine(x):
    return (VDR(2) * x + VDR(3)) / VDR(5)

x = VDR(10)
print("  f(x) = (2x+3)/5, start at 10:")
for i in range(15):
    x = affine(x)
    print("    step %d: %s" % (i+1, x.to_fraction()))

# fixed point: x = (2x+3)/5 → 5x = 2x+3 → 3x = 3 → x = 1
err = abs(float(x.to_fraction()) - 1)
record(check("affine converges to 1 (error < 1e-5)", err < 1e-5))

# exact: x_n = 1 + (x_0-1) * (2/5)^n
for n in [5, 10]:
    x_check = VDR(10)
    for _ in range(n):
        x_check = affine(x_check)
    expected = Fraction(1) + Fraction(9) * Fraction(2, 5) ** n
    ok = x_check.to_fraction() == expected
    record(check("affine step %d matches closed form" % n, ok))

# =========================================================================
section("6. Collatz sequence in VDR")
# =========================================================================

def collatz_step(n):
    """One Collatz step, exact VDR integer."""
    n_int = int(n.to_fraction())
    if n_int % 2 == 0:
        return VDR(n_int // 2)
    else:
        return VDR(3 * n_int + 1)

start = VDR(27)
x = start
trajectory = [x]
for _ in range(200):
    x = collatz_step(x)
    trajectory.append(x)
    if x == VDR(1):
        break

print("  Collatz(27): %d steps to reach 1" % (len(trajectory) - 1))
print("    max value: %s" % max(int(t.to_fraction()) for t in trajectory))
record(check("Collatz(27) reaches 1", trajectory[-1] == VDR(1)))

# all values are exact integers
all_int = all(t.to_fraction().denominator == 1 for t in trajectory)
record(check("all Collatz values are exact integers", all_int))

# =========================================================================
section("7. Rational logistic map")
# =========================================================================

# x_{n+1} = r * x * (1 - x) with rational r and x
# for r = 3, this has period-2 orbit at x = (1 ± 1/sqrt(3))/... but
# since sqrt(3) is irrational, the rational orbit won't settle to period-2.
# However, for r = 2, the fixed point is x = 1/2.

r = VDR(2)
x = VDR(1, 4)
print("  logistic map r=2, x0=1/4:")
for i in range(10):
    x = r * x * (VDR(1) - x)
    print("    step %d: %s" % (i+1, x.to_fraction()))

# should converge to 1/2
record(check("logistic r=2 converges to 1/2 (error < 0.01)",
             abs(float(x.to_fraction()) - 0.5) < 0.01))

# r = 4: chaotic, but still exact rational at each step
r4 = VDR(4)
x4 = VDR(1, 3)
print("  logistic map r=4, x0=1/3 (chaotic, exact):")
for i in range(10):
    x4 = r4 * x4 * (VDR(1) - x4)
    f = x4.to_fraction()
    print("    step %d: %s (denom has %d digits)" % (
        i+1, f, len(str(abs(f.denominator)))))

# key observation: denominators grow exponentially in chaotic regime
# but every single value is an EXACT rational — no float approximation
denoms = []
x_test = VDR(1, 3)
for i in range(15):
    x_test = r4 * x_test * (VDR(1) - x_test)
    denoms.append(len(str(abs(x_test.to_fraction().denominator))))
print("  denominator digit growth: %s" % denoms)
record(check("chaotic logistic: denom digits grow",
             denoms[-1] > denoms[0] * 3))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 14 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)

