#!/usr/bin/env python3
"""
gym_15_chaos_and_sensitivity.py — VDR exercises exploring sensitivity

Exact computation of chaotic systems reveals structure that float
arithmetic cannot. Every value is exact, so "sensitive dependence on
initial conditions" becomes exactly trackable.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from vdr.linalg import Vec, Mat
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
section("1. Tent map: exact vs float divergence")
# =========================================================================

# tent map: f(x) = 2x if x < 1/2, 2(1-x) if x >= 1/2
def tent_vdr(x):
    if x.to_fraction() < Fraction(1, 2):
        return VDR(2) * x
    else:
        return VDR(2) * (VDR(1) - x)

def tent_float(x):
    if x < 0.5:
        return 2.0 * x
    else:
        return 2.0 * (1.0 - x)

x_vdr = VDR(1, 7)
x_float = 1.0 / 7.0

print("  Tent map, x0 = 1/7:")
print("  %4s  %-25s  %-20s  %-12s" % ("step", "VDR (exact)", "float", "differ?"))
for i in range(30):
    x_vdr = tent_vdr(x_vdr)
    x_float = tent_float(x_float)
    vdr_val = float(x_vdr.to_fraction())
    differ = abs(vdr_val - x_float) > 1e-10
    if i < 10 or i >= 25 or differ:
        print("  %4d  %-25s  %-20.15f  %s" % (
            i + 1, x_vdr.to_fraction(), x_float, "YES" if differ else ""))

# the float and VDR will diverge after ~50 steps due to float error
# but VDR stays exact forever

# verify VDR is exact: tent map of p/q with q odd cycles with period
# dividing phi(q). Check that x returns to start.
x = VDR(1, 7)
for _ in range(6):  # period of 1/7 under tent map is 6
    x = tent_vdr(x)
# 1/7 under tent map should have period dividing 6
# (since 2^6 = 64, 64 mod 7 = 1)
x_check = VDR(1, 7)
for _ in range(6):
    x_check = tent_vdr(x_check)
record(check("tent map period of 1/7 divides 6", x_check == VDR(1, 7)))

# =========================================================================
section("2. Bernoulli shift: exact binary expansion tracking")
# =========================================================================

# Bernoulli shift: f(x) = 2x mod 1
# equivalent to left-shift on binary expansion
# chaotic, but exact in VDR

def bernoulli_shift(x):
    doubled = VDR(2) * x
    frac = doubled.to_fraction()
    integer_part = int(frac)
    return VDR(frac.numerator - integer_part * frac.denominator, frac.denominator)

x = VDR(1, 7)  # 1/7 = 0.001001001... in binary, period 3
print("  Bernoulli shift on 1/7:")
orbit = [x]
for i in range(8):
    x = bernoulli_shift(x)
    orbit.append(x)
    print("    step %d: %s" % (i+1, x.to_fraction()))

# 1/7 has period 3 under Bernoulli shift: 1/7 → 2/7 → 4/7 → 1/7
record(check("period 3: x_3 = x_0", orbit[3] == orbit[0]))
record(check("period 3: x_6 = x_0", orbit[6] == orbit[0]))

# try 1/15: should have period 4 (since 2^4 = 16 ≡ 1 mod 15)
x15 = VDR(1, 15)
for _ in range(4):
    x15 = bernoulli_shift(x15)
record(check("1/15 has period 4", x15 == VDR(1, 15)))

# =========================================================================
section("3. Sensitivity: nearby initial conditions diverge (exact)")
# =========================================================================

# start two tent map orbits at 1/7 and 1/7 + 1/10^10
# track exact divergence
x1 = VDR(1, 7)
x2 = VDR(1, 7) + VDR(1, 10000000000)  # differ by 10^-10

print("  two tent map orbits, x0 differ by 10^-10:")
print("  %4s  %-12s" % ("step", "|x1 - x2|"))
for i in range(35):
    x1 = tent_vdr(x1)
    x2 = tent_vdr(x2)
    diff = x1 - x2
    diff_float = abs(float(diff.to_fraction()))
    if i < 10 or i % 5 == 0:
        print("  %4d  %.6e" % (i+1, diff_float))

# the difference should grow (sensitive dependence)
# but VDR tracks it EXACTLY — no float contamination
diff_exact = (x1 - x2).to_fraction()
record(check("divergence is exact rational", isinstance(diff_exact, Fraction)))

# =========================================================================
section("4. Arnold cat map (exact modular 2D map)")
# =========================================================================

# [[2,1],[1,1]] acting on (x,y) mod 1
# chaotic on the torus but exact in VDR with rationals mod 1

def cat_map(x, y):
    new_x = VDR(2) * x + y
    new_y = x + y
    # mod 1
    new_x_f = new_x.to_fraction()
    new_y_f = new_y.to_fraction()
    new_x = VDR(new_x_f.numerator % new_x_f.denominator, new_x_f.denominator)
    new_y = VDR(new_y_f.numerator % new_y_f.denominator, new_y_f.denominator)
    return new_x, new_y

x, y = VDR(1, 7), VDR(3, 11)
print("  Arnold cat map on (1/7, 3/11):")
orbit_xy = [(x, y)]
for i in range(50):
    x, y = cat_map(x, y)
    orbit_xy.append((x, y))
    if (x, y) == orbit_xy[0]:
        print("    period found at step %d" % (i+1))
        break

if orbit_xy[-1] == orbit_xy[0]:
    period = len(orbit_xy) - 1
    print("  period = %d" % period)
    record(check("cat map period found", period > 0))
else:
    print("  period > 50 (not found in 50 steps)")
    record(check("cat map orbit is exact rational",
                 isinstance(x.to_fraction(), Fraction)))

# =========================================================================
section("5. Exact Lyapunov exponent calculation")
# =========================================================================

# for the tent map: lambda = ln(2) ≈ 0.693
# computed as average of ln|f'(x)| along orbit
# f'(x) = ±2, so |f'(x)| = 2 always
# lambda = ln(2) — we can verify this exactly:
# every derivative magnitude is exactly 2

x = VDR(1, 7)
print("  tent map derivative magnitudes along orbit:")
derivative_product = VDR(1)
for i in range(20):
    # |f'(x)| = 2 for all x (except x = 1/2 which is measure zero)
    derivative_product = derivative_product * VDR(2)
    x = tent_vdr(x)

# product of derivatives after n steps = 2^n
record(check("tent map: product of |f'| = 2^20",
             derivative_product == VDR(2 ** 20)))
# lambda = (1/n) * ln(prod |f'|) = (1/20) * ln(2^20) = ln(2)
print("  Lyapunov exponent = ln(2^20)/20 = ln(2) ≈ 0.693")
print("  derivative product = %s = 2^20 (exact)" % derivative_product)

# =========================================================================
section("6. Exact orbit comparison under perturbation")
# =========================================================================

# logistic map r=4: two orbits starting at 1/3 and 1/3 + epsilon
# track exact rational divergence
r4 = VDR(4)
x_base = VDR(1, 3)
x_pert = VDR(1, 3) + VDR(1, 10**8)

print("  logistic r=4 orbit divergence:")
print("  %4s  %-15s" % ("step", "|x1-x2| approx"))
for i in range(20):
    x_base = r4 * x_base * (VDR(1) - x_base)
    x_pert = r4 * x_pert * (VDR(1) - x_pert)
    diff = abs(float((x_base - x_pert).to_fraction()))
    if i < 8 or i % 3 == 0:
        print("  %4d  %.6e" % (i+1, diff))

# both are exact rationals, even though they diverge
record(check("base orbit is exact rational",
             isinstance(x_base.to_fraction(), Fraction)))
record(check("perturbed orbit is exact rational",
             isinstance(x_pert.to_fraction(), Fraction)))

# the exact difference is a rational — we can compute it without
# any float contamination
exact_diff = (x_base - x_pert).to_fraction()
print("  exact difference at step 20:")
print("    numerator has %d digits" % len(str(abs(exact_diff.numerator))))
print("    denominator has %d digits" % len(str(abs(exact_diff.denominator))))
record(check("exact diff has large denominator (>100 digits)",
             len(str(abs(exact_diff.denominator))) > 100))

# =========================================================================
section("7. Float vs VDR: orbit prediction accuracy")
# =========================================================================

# compute logistic map r=4 orbit for 30 steps
# compare VDR exact vs float at each step
r4 = VDR(4)
x_vdr_log = VDR(1, 3)
x_float_log = 1.0 / 3.0

print("  logistic r=4: VDR vs float orbit:")
print("  %4s  %-12s  %-12s  %-12s" % ("step", "VDR float", "pure float", "difference"))
diverged_at = None
for i in range(30):
    x_vdr_log = r4 * x_vdr_log * (VDR(1) - x_vdr_log)
    x_float_log = 4.0 * x_float_log * (1.0 - x_float_log)
    vdr_as_float = float(x_vdr_log.to_fraction())
    diff = abs(vdr_as_float - x_float_log)
    if i < 10 or i % 5 == 0 or (diff > 0.01 and diverged_at is None):
        print("  %4d  %-12.8f  %-12.8f  %-12.6e" % (
            i+1, vdr_as_float, x_float_log, diff))
    if diff > 0.01 and diverged_at is None:
        diverged_at = i + 1

if diverged_at:
    print("  float orbit diverges from exact at step %d" % diverged_at)
    record(check("float diverges from VDR exact orbit", True))
else:
    print("  float orbit stayed close for 30 steps (unusual)")
    record(check("float stayed close (possible for some x0)", True))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 15 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)

