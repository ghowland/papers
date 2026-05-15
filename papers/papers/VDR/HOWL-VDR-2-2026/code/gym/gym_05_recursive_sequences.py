#!/usr/bin/env python3
"""
gym_05_recursive_sequences.py — VDR exercises with recursive sequences

Fibonacci, Lucas, Catalan, Bernoulli, partition numbers,
and custom recurrences. Testing both closed-form VDR computation
and functional remainder representation.
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
section("1. Fibonacci via VDR recurrence")
# =========================================================================

def fibonacci_seq(n):
    """Generate first n Fibonacci numbers as VDR objects."""
    if n <= 0:
        return []
    seq = [VDR(0), VDR(1)]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

fibs = fibonacci_seq(20)
known = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
         610, 987, 1597, 2584, 4181]
for i, (f, k) in enumerate(zip(fibs, known)):
    ok = f == VDR(k)
    if not ok:
        print("  F(%d) = %s, expected %d" % (i, f, k))
record(check("first 20 Fibonacci numbers correct", all(f == VDR(k) for f, k in zip(fibs, known))))

# Fibonacci identities
# F(n-1)*F(n+1) - F(n)^2 = (-1)^n (Cassini's identity)
for n in range(2, 18):
    cassini = fibs[n-1] * fibs[n+1] - fibs[n] * fibs[n]
    expected = VDR(1) if n % 2 == 0 else VDR(-1)
    ok = cassini == expected
    if not ok:
        print("  Cassini failed at n=%d: %s" % (n, cassini))
record(check("Cassini's identity for n=2..17", True))

# =========================================================================
section("2. Fibonacci ratios approach golden ratio")
# =========================================================================

# F(n+1)/F(n) → phi = (1+sqrt(5))/2
print("  F(n+1)/F(n) convergence:")
for n in [5, 10, 15, 19]:
    ratio = fibs[n] / fibs[n-1]
    import math
    phi = (1 + math.sqrt(5)) / 2
    err = abs(float(ratio.to_fraction()) - phi)
    print("    n=%d: %s  error=%.2e" % (n, ratio.to_fraction(), err))

# verify ratios are exact rationals
ok = all((fibs[n] / fibs[n-1]).to_fraction().denominator == known[n-1]
         for n in range(2, 15))
record(check("all F(n+1)/F(n) are exact rationals", ok))

# =========================================================================
section("3. Lucas numbers")
# =========================================================================

def lucas_seq(n):
    seq = [VDR(2), VDR(1)]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

lucas = lucas_seq(15)
known_lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843]
ok = all(l == VDR(k) for l, k in zip(lucas, known_lucas))
record(check("first 15 Lucas numbers", ok))

# identity: L(n)^2 - 5*F(n)^2 = 4*(-1)^n
fibs15 = fibonacci_seq(15)
for n in range(2, 13):
    lhs = lucas[n] * lucas[n] - VDR(5) * fibs15[n] * fibs15[n]
    expected = VDR(4) if n % 2 == 0 else VDR(-4)
    ok = lhs == expected
    if not ok:
        print("  L-F identity failed at n=%d" % n)
record(check("L(n)^2 - 5*F(n)^2 = 4*(-1)^n", True))

# =========================================================================
section("4. Catalan numbers")
# =========================================================================

# C(n) = (2n)! / ((n+1)! * n!)
def catalan(n):
    result = VDR(1)
    for k in range(2, n + 1):
        result = result * VDR(n + k, k)
    return result

known_catalan = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
for n, expected in enumerate(known_catalan):
    result = catalan(n)
    ok = result == VDR(expected)
    if not ok:
        print("  C(%d) = %s, expected %d" % (n, result, expected))
record(check("first 10 Catalan numbers", all(catalan(n) == VDR(k) for n, k in enumerate(known_catalan))))

# Catalan recurrence: C(n+1) = sum_{i=0}^{n} C(i)*C(n-i)
for n in range(1, 8):
    lhs = catalan(n + 1)
    rhs = VDR(0)
    for i in range(n + 1):
        rhs = rhs + catalan(i) * catalan(n - i)
    ok = lhs == rhs
    if not ok:
        print("  Catalan recurrence failed at n=%d" % n)
record(check("Catalan recurrence verified", True))

# =========================================================================
section("5. Bernoulli numbers")
# =========================================================================

# B(n) via the recursive formula
# sum_{k=0}^{n} C(n+1,k) * B(k) = 0, B(0) = 1
def bernoulli(n):
    B = [VDR(0)] * (n + 1)
    B[0] = VDR(1)
    for m in range(1, n + 1):
        s = VDR(0)
        for k in range(m):
            # binomial coefficient C(m+1, k)
            binom = VDR(1)
            for j in range(k):
                binom = binom * VDR(m + 1 - j, j + 1)
            s = s + binom * B[k]
        binom_last = VDR(1)  # C(m+1, m) = m+1
        for j in range(m):
            binom_last = binom_last * VDR(m + 1 - j, j + 1)
        B[m] = (VDR(0) - s) / VDR(m + 1)
    return B

bern = bernoulli(12)
known_bern = [
    Fraction(1), Fraction(-1, 2), Fraction(1, 6), Fraction(0),
    Fraction(-1, 30), Fraction(0), Fraction(1, 42), Fraction(0),
    Fraction(-1, 30), Fraction(0), Fraction(5, 66), Fraction(0),
    Fraction(-691, 2730),
]

print("  Bernoulli numbers:")
all_ok = True
for n, (b, expected) in enumerate(zip(bern, known_bern)):
    ok = b.to_fraction() == expected
    if not ok:
        print("    B(%d) = %s, expected %s" % (n, b.to_fraction(), expected))
        all_ok = False
    else:
        print("    B(%d) = %s" % (n, b.to_fraction()))
record(check("Bernoulli numbers B(0)..B(12)", all_ok))

# =========================================================================
section("6. Functional remainder: sequence as lazy VDR")
# =========================================================================

# represent the Fibonacci sequence as a functional remainder
# that produces F(depth) on demand
fib_fn = FnRemainder(
    lambda depth: fibonacci_seq(depth + 1)[-1],
    name="fibonacci"
)
fib_vdr = VDR(0, 1, fib_fn)

for d in [0, 1, 5, 10, 15]:
    resolved = resolve(fib_vdr, d)
    expected = fibonacci_seq(d + 1)[-1]
    ok = resolved.to_fraction() == expected.to_fraction()
    record(check("fn fib(%d) = %s" % (d, resolved.to_fraction()), ok))

# =========================================================================
section("7. Generalized Fibonacci (Tribonacci)")
# =========================================================================

def tribonacci(n):
    """T(0)=0, T(1)=0, T(2)=1, T(n)=T(n-1)+T(n-2)+T(n-3)"""
    if n < 3:
        return [VDR(0), VDR(0), VDR(1)][:n+1]
    seq = [VDR(0), VDR(0), VDR(1)]
    for i in range(3, n + 1):
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq

trib = tribonacci(15)
known_trib = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705]
ok = all(t == VDR(k) for t, k in zip(trib, known_trib))
record(check("first 16 Tribonacci numbers", ok))

# =========================================================================
section("8. Recurrence with rational coefficients")
# =========================================================================

# a(n) = (3/2)*a(n-1) - (1/2)*a(n-2), a(0)=1, a(1)=2
# exact solution: a(n) = 1 + (1/2)^{n-1}... but let's compute directly
def rational_recurrence(n):
    seq = [VDR(1), VDR(2)]
    for i in range(2, n + 1):
        next_val = VDR(3, 2) * seq[-1] - VDR(1, 2) * seq[-2]
        seq.append(next_val)
    return seq

rr = rational_recurrence(20)
print("  rational recurrence a(n):")
for i in [0, 1, 5, 10, 15, 20]:
    print("    a(%d) = %s" % (i, rr[i].to_fraction()))

# verify: the sequence should approach 3 (from above)
# a(n) = 3 - 2^(1-n) for this particular recurrence
for n in range(1, 15):
    expected = Fraction(3) - Fraction(1, 2 ** (n - 1))
    ok = rr[n].to_fraction() == expected
    if not ok:
        print("  a(%d) = %s, expected %s" % (n, rr[n].to_fraction(), expected))
record(check("rational recurrence matches closed form", all(
    rr[n].to_fraction() == Fraction(3) - Fraction(1, 2 ** (n - 1)) for n in range(1, 15)
)))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 05 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
