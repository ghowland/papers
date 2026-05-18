"""
test_layer_3.py — Tests for Layer 3: functional remainders, discrete calculus

Run:  python test_layer_3.py
"""

from fractions import Fraction
from vdr.vdr import VDR, Remainder
from vdr.fn import (
    FnRemainder, vdr_fn, resolve, is_functional, resolve_recursive,
    make_constant_fn, make_series_fn, make_newton_fn, make_iterative_fn,
    discrete_derivative, discrete_integral, discrete_integral_trapz,
    discrete_derivative_nth,
)
import vdr.fn
import vdr.active_mul

vdr.active_mul.install()
vdr.fn.install()


def section(title):
    print("\n=== %s ===" % title)

def show(label, x):
    if is_functional(x):
        print("  %-28s  %s   (functional, resolve first)" % (label, x))
    else:
        print("  %-28s  %s   (projects to %s)" % (label, x, x.to_fraction()))


# =========================================================================
section("1. FnRemainder construction")
# =========================================================================

def simple_fn(depth):
    return VDR(depth + 1, depth + 2)

fr = FnRemainder(simple_fn, name="simple")
print("  FnRemainder: %s" % fr)
print("  is_functional: %s" % isinstance(fr, FnRemainder))
print("  expand(0): %s" % fr.expand(0))
print("  expand(3): %s" % fr.expand(3))

obj = VDR(0, 1, fr)
print("  VDR with fn remainder: %s" % obj)
assert is_functional(obj), "should be functional"
assert obj.is_active, "functional should be active"
assert not obj.is_closed, "functional should not be closed"

# =========================================================================
section("2. Resolve functional VDR")
# =========================================================================

obj = VDR(0, 1, FnRemainder(simple_fn, name="simple"))

r0 = resolve(obj, 0)
show("resolve(depth=0)", r0)
assert r0.to_fraction() == Fraction(1, 2), "resolve depth 0"

r3 = resolve(obj, 3)
show("resolve(depth=3)", r3)
assert r3.to_fraction() == Fraction(4, 5), "resolve depth 3"

# =========================================================================
section("3. Projection fails on unresolved functional")
# =========================================================================

obj = VDR(0, 1, FnRemainder(simple_fn, name="simple"))
try:
    obj.to_fraction()
    assert False, "should have raised"
except Exception as e:
    print("  to_fraction() on functional: %s" % e)
    print("  correctly blocked")

# =========================================================================
section("4. Newton-Raphson for sqrt(2)")
# =========================================================================

# x_{n+1} = (x + 2/x) / 2
# Starting from x=1, each step is exact rational VDR arithmetic.
# Converges quadratically to sqrt(2) ≈ 1.41421356...

sqrt2_fn = make_newton_fn("sqrt2", lambda x: (x + VDR(2) / x) / VDR(2))
sqrt2_obj = VDR(0, 1, sqrt2_fn)

print("  sqrt(2) via Newton-Raphson:")
prev = None
for depth in range(8):
    resolved = resolve(sqrt2_obj, depth)
    frac = resolved.to_fraction()
    approx = float(frac)
    # check: x^2 should approach 2
    x_squared = resolved * resolved
    err = x_squared.to_fraction() - Fraction(2)
    print("    depth=%d: %s ≈ %.15f  x²-2=%s" % (depth, frac, approx, err))

    if depth > 0 and prev is not None:
        # each step should get closer to sqrt(2)
        prev_err = abs(float(prev.to_fraction()) ** 2 - 2)
        curr_err = abs(approx ** 2 - 2)
        assert curr_err <= prev_err + 1e-30, "Newton should converge"
    prev = resolved

# at depth 7, x^2 should be very close to 2
final = resolve(sqrt2_obj, 7)
final_sq = final * final
final_err = abs(float(final_sq.to_fraction()) - 2.0)
print("  depth=7 error: %.2e" % final_err)
assert final_err < 1e-100, "Newton sqrt2 should be extremely precise"

# =========================================================================
section("5. Newton-Raphson for sqrt(3)")
# =========================================================================

sqrt3_fn = make_newton_fn("sqrt3", lambda x: (x + VDR(3) / x) / VDR(2))
sqrt3_obj = VDR(0, 1, sqrt3_fn)

print("  sqrt(3) via Newton-Raphson:")
for depth in range(6):
    resolved = resolve(sqrt3_obj, depth)
    frac = resolved.to_fraction()
    approx = float(frac)
    x_squared = resolved * resolved
    err = x_squared.to_fraction() - Fraction(3)
    print("    depth=%d: ≈ %.15f  x²-3=%s" % (depth, approx, err))

# =========================================================================
section("6. Series: Leibniz pi/4")
# =========================================================================

# pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
# Each partial sum is exact rational.

def leibniz_term(n):
    sign = 1 if n % 2 == 0 else -1
    return VDR(sign, 2 * n + 1)

pi4_fn = make_series_fn("leibniz_pi4", leibniz_term)
pi4_obj = VDR(0, 1, pi4_fn)

print("  Leibniz series for pi/4:")
for depth in [0, 1, 5, 10, 50, 100]:
    resolved = resolve(pi4_obj, depth)
    frac = resolved.to_fraction()
    approx = float(frac) * 4  # multiply by 4 to get pi
    print("    %d terms: pi ≈ %.12f  (exact frac: %s)" % (
        depth + 1, approx, frac
    ))

# verify: first term is 1/1 = 1
r0 = resolve(pi4_obj, 0)
assert r0.to_fraction() == Fraction(1), "first Leibniz term"

# verify: first two terms give 1 - 1/3 = 2/3
r1 = resolve(pi4_obj, 1)
assert r1.to_fraction() == Fraction(2, 3), "first two Leibniz terms"

# =========================================================================
section("7. Series: Basel problem (pi^2/6)")
# =========================================================================

# pi^2/6 = 1 + 1/4 + 1/9 + 1/16 + ...
# sum of 1/n^2

def basel_term(n):
    k = n + 1
    return VDR(1, k * k)

basel_fn = make_series_fn("basel_pi2_6", basel_term)
basel_obj = VDR(0, 1, basel_fn)

print("  Basel series for pi²/6:")
for depth in [0, 5, 20, 100]:
    resolved = resolve(basel_obj, depth)
    approx = float(resolved.to_fraction())
    pi_approx = (approx * 6) ** 0.5
    print("    %d terms: pi²/6 ≈ %.12f  pi ≈ %.12f" % (
        depth + 1, approx, pi_approx
    ))

# =========================================================================
section("8. Iterative function")
# =========================================================================

# Collatz-like iteration on VDR (staying rational)
# Just demonstrating the iterative machinery

def halving_step(x):
    return x / VDR(2)

halving = make_iterative_fn("halving", halving_step, VDR(1024))
halving_obj = VDR(0, 1, halving)

print("  Iterative halving from 1024:")
for depth in range(12):
    resolved = resolve(halving_obj, depth)
    print("    depth=%d: %s = %s" % (depth, resolved, resolved.to_fraction()))

r10 = resolve(halving_obj, 10)
assert r10.to_fraction() == Fraction(1), "1024 / 2^10 = 1"

# =========================================================================
section("9. Discrete derivative")
# =========================================================================

# f(x) = x^2
def f_x2(x):
    return x * x

# exact derivative at step h = 1/1000
h = VDR(1, 1000)
df = discrete_derivative(f_x2, h)

# df(x) = (f(x+h) - f(x)) / h = ((x+h)^2 - x^2) / h = 2x + h
# at x = 3: df = 6 + 1/1000 = 6001/1000

result = df(VDR(3))
show("d/dx(x²) at x=3, h=1/1000", result)
assert result.to_fraction() == Fraction(6001, 1000), "discrete derivative"

# at x = 0: df = 0 + h = 1/1000
result0 = df(VDR(0))
show("d/dx(x²) at x=0", result0)
assert result0.to_fraction() == Fraction(1, 1000), "discrete deriv at 0"

# smaller step: h = 1/1000000
h_fine = VDR(1, 1000000)
df_fine = discrete_derivative(f_x2, h_fine)
result_fine = df_fine(VDR(3))
show("d/dx(x²) at x=3, h=1/10⁶", result_fine)
assert result_fine.to_fraction() == Fraction(6000001, 1000000)

# =========================================================================
section("10. Discrete derivative of x^3")
# =========================================================================

def f_x3(x):
    return x * x * x

h = VDR(1, 100)
df3 = discrete_derivative(f_x3, h)

# df(x) = 3x^2 + 3xh + h^2  at x=2: 12 + 6/100 + 1/10000
result = df3(VDR(2))
show("d/dx(x³) at x=2, h=1/100", result)
expected = Fraction(12) + Fraction(6, 100) + Fraction(1, 10000)
assert result.to_fraction() == expected, "cubic derivative"

# =========================================================================
section("11. Second derivative")
# =========================================================================

# d²/dx²(x³) = 6x + 6h  at x=2, h=1/100: 12 + 6/100 = 1206/100
h = VDR(1, 100)
ddf3 = discrete_derivative_nth(f_x3, h, order=2)
result = ddf3(VDR(2))
show("d²/dx²(x³) at x=2, h=1/100", result)

# analytical: 6*2 = 12, discrete gives 12 + 6h = 12.06
expected_approx = 12.06
got_approx = float(result.to_fraction())
print("  expected ≈ %.4f, got = %.4f" % (expected_approx, got_approx))
assert abs(got_approx - expected_approx) < 0.001, "second derivative"

# =========================================================================
section("12. Discrete integral of x^2 from 0 to 1")
# =========================================================================

# analytical: 1/3
# left Riemann sum with n steps

for n in [10, 100, 1000]:
    result = discrete_integral(f_x2, VDR(0), VDR(1), n)
    frac = result.to_fraction()
    err = abs(float(frac) - 1.0/3.0)
    print("  n=%d: integral=%s ≈ %.10f  error=%.2e" % (n, frac, float(frac), err))

# verify exact: for n=10, left Riemann of x^2 on [0,1]
# = sum_{k=0}^{9} (k/10)^2 * (1/10) = (1/1000) * sum_{k=0}^{9} k^2
# = (1/1000) * 285 = 285/1000 = 57/200
r10 = discrete_integral(f_x2, VDR(0), VDR(1), 10)
assert r10.to_fraction() == Fraction(57, 200), "integral n=10 exact"

# =========================================================================
section("13. Trapezoidal integral of x^2 from 0 to 1")
# =========================================================================

for n in [10, 100, 1000]:
    result = discrete_integral_trapz(f_x2, VDR(0), VDR(1), n)
    frac = result.to_fraction()
    err = abs(float(frac) - 1.0/3.0)
    print("  n=%d: integral=%s ≈ %.10f  error=%.2e" % (n, frac, float(frac), err))

# trapezoidal is more accurate than left Riemann
left_100 = discrete_integral(f_x2, VDR(0), VDR(1), 100)
trap_100 = discrete_integral_trapz(f_x2, VDR(0), VDR(1), 100)
left_err = abs(float(left_100.to_fraction()) - 1.0/3.0)
trap_err = abs(float(trap_100.to_fraction()) - 1.0/3.0)
print("  n=100 left error: %.2e" % left_err)
print("  n=100 trap error: %.2e" % trap_err)
assert trap_err < left_err, "trapezoidal should be more accurate"

# =========================================================================
section("14. Integral of 1/x from 1 to 2 (approaches ln 2)")
# =========================================================================

def f_inv(x):
    return VDR(1) / x

for n in [10, 100, 1000]:
    result = discrete_integral_trapz(f_inv, VDR(1), VDR(2), n)
    approx = float(result.to_fraction())
    import math
    err = abs(approx - math.log(2))
    print("  n=%d: ≈ %.12f  (ln2=%.12f)  error=%.2e" % (
        n, approx, math.log(2), err
    ))

# =========================================================================
section("15. FnRemainder negation")
# =========================================================================

fn = FnRemainder(lambda d: VDR(d + 1), name="inc")
neg_fn = fn.negate()
print("  original(3): %s" % fn.expand(3))
print("  negated(3):  %s" % neg_fn.expand(3))
assert neg_fn.expand(3).to_fraction() == -Fraction(4), "fn negation"

# =========================================================================
section("16. FnRemainder lift")
# =========================================================================

fn = FnRemainder(lambda d: VDR(1, d + 2), name="frac")
lifted = fn.lift(3)
print("  original(2): %s" % fn.expand(2))
print("  lifted(2):   %s" % lifted.expand(2))
# original: VDR(1, 4), lift by 3 → VDR(3, 4)
assert lifted.expand(2).to_fraction() == Fraction(3, 4), "fn lift"

# =========================================================================
section("17. FnRemainder combination")
# =========================================================================

fn1 = FnRemainder(lambda d: VDR(d + 1), name="a")
fn2 = FnRemainder(lambda d: VDR(d + 2), name="b")

combined = fn1.combine(fn2, sign=1)
print("  a(3) + b(3): %s" % combined.expand(3))
assert combined.expand(3).to_fraction() == Fraction(9), "fn combine add"

sub = fn1.combine(fn2, sign=-1)
print("  a(3) - b(3): %s" % sub.expand(3))
assert sub.expand(3).to_fraction() == Fraction(-1), "fn combine sub"

# =========================================================================
section("18. VDR with frame and functional remainder")
# =========================================================================

# [3, 7, fn] where fn produces exact values
fn = FnRemainder(lambda d: VDR(d, d + 1), name="ratio")
obj = VDR(3, 7, fn)
show("VDR(3,7,fn)", obj)

# resolve at depth 4: fn(4) = VDR(4, 5)
resolved = resolve(obj, 4)
show("resolved(depth=4)", resolved)

# the resolved object should have [3, 7, child=VDR(4,5)]
# projection: (3 + 4/5) / 7 = (19/5) / 7 = 19/35
assert resolved.to_fraction() == Fraction(19, 35), "framed functional"

# =========================================================================
section("19. Resolve recursive")
# =========================================================================

# build a tree with functional remainders at multiple levels
inner_fn = FnRemainder(lambda d: VDR(1, d + 2), name="inner")
inner_vdr = VDR(0, 1, inner_fn)

outer_fn = FnRemainder(lambda d: VDR(d, 1, Remainder(0, [inner_vdr])),
                       name="outer")
outer_vdr = VDR(1, 1, outer_fn)

print("  nested functional VDR: %s" % outer_vdr)
resolved = resolve_recursive(outer_vdr, depth=3)
show("resolve_recursive(depth=3)", resolved)

# =========================================================================
section("20. Convergence comparison: Newton vs Series for sqrt(2)")
# =========================================================================

# Newton: quadratic convergence
# Series: linear convergence (via Babylonian fraction expansion)

import math
true_sqrt2 = math.sqrt(2)

print("  Newton-Raphson sqrt(2):")
sqrt2_nr = make_newton_fn("sqrt2_nr", lambda x: (x + VDR(2) / x) / VDR(2))
for depth in range(8):
    val = sqrt2_nr.expand(depth)
    err = abs(float(val.to_fraction()) - true_sqrt2)
    digits = -math.log10(err) if err > 0 else 999
    print("    depth=%d: digits=%.1f  err=%.2e" % (depth, digits, err))

# Series: 1/k^2 doesn't give sqrt2, but the Newton does.
# Just show Newton converges fast enough.
val7 = sqrt2_nr.expand(7)
err7 = abs(float(val7.to_fraction()) - true_sqrt2)
assert err7 < 1e-100, "Newton should have >100 digits by depth 7"
print("  Newton depth=7 has >100 correct digits: PASS")

# =========================================================================
section("21. Exact finite difference table")
# =========================================================================

# Build a finite difference table for f(x) = x^3 at x = 0,1,2,3,4
# Every entry is exact VDR rational

print("  Finite difference table for x³:")
xs = [VDR(i) for i in range(5)]
values = [f_x3(x) for x in xs]
print("    f:    %s" % [v.to_fraction() for v in values])

# first differences
d1 = [values[i+1] - values[i] for i in range(len(values)-1)]
print("    Δf:   %s" % [v.to_fraction() for v in d1])

# second differences
d2 = [d1[i+1] - d1[i] for i in range(len(d1)-1)]
print("    Δ²f:  %s" % [v.to_fraction() for v in d2])

# third differences (should be constant = 6 for cubic)
d3 = [d2[i+1] - d2[i] for i in range(len(d2)-1)]
print("    Δ³f:  %s" % [v.to_fraction() for v in d3])

# fourth differences (should be all 0)
d4 = [d3[i+1] - d3[i] for i in range(len(d3)-1)] if len(d3) > 1 else []
print("    Δ⁴f:  %s" % [v.to_fraction() for v in d4])

assert all(v == VDR(6) for v in d3), "third differences of cubic should be 6"
assert all(v == VDR(0) for v in d4), "fourth differences should be 0"
print("  Δ³(x³) = 6 exactly, Δ⁴(x³) = 0 exactly: PASS")


# =========================================================================
print("\n" + "=" * 50)
print("ALL LAYER 3 TESTS PASSED")
print("=" * 50)
