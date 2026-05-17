#!/usr/bin/env python3
"""
gym_09_differential_equations.py — VDR exercises with ODEs

Euler method, RK4, exact linear ODE solutions via matrix exponential,
and Picard iteration — all using exact VDR arithmetic.
"""

import sys
sys.path.insert(0, '..')
from vdr.vdr import VDR, Remainder
from vdr.linalg import Vec, Mat
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
section("1. Exact Euler method: dy/dx = y, y(0) = 1")
# =========================================================================

# Analytical solution: y = e^x
# Euler: y_{n+1} = y_n + h * f(x_n, y_n) = y_n * (1 + h)
# With VDR, every step is exact rational.

def euler_solve(f, y0, x0, h, n_steps):
    """Exact Euler method using VDR arithmetic."""
    x = x0
    y = y0
    trajectory = [(x, y)]
    for _ in range(n_steps):
        y = y + h * f(x, y)
        x = x + h
        trajectory.append((x, y))
    return trajectory

# dy/dx = y
f_exp = lambda x, y: y
h = VDR(1, 10)
traj = euler_solve(f_exp, VDR(1), VDR(0), h, 10)

print("  Euler method for dy/dx=y, h=1/10:")
import math
for x, y in traj[::2]:  # every other step
    exact = math.exp(float(x.to_fraction()))
    print("    x=%s  y=%s  (exact e^x=%.6f)" % (
        x.to_fraction(), y.to_fraction(), exact))

# key check: y(1) with h=1/10 should be (11/10)^10 exactly
y_final = traj[-1][1]
expected = Fraction(11, 10) ** 10
ok = y_final.to_fraction() == expected
record(check("Euler y(1) = (11/10)^10 exactly", ok))
print("  y(1) = %s = %s" % (y_final.to_fraction(), float(y_final.to_fraction())))

# =========================================================================
section("2. Euler method: dy/dx = -y, y(0) = 1 (decay)")
# =========================================================================

f_decay = lambda x, y: -y
h = VDR(1, 10)
traj_decay = euler_solve(f_decay, VDR(1), VDR(0), h, 20)

print("  Euler for dy/dx = -y:")
for x, y in traj_decay[::5]:
    print("    x=%s  y=%s" % (x.to_fraction(), y.to_fraction()))

# y(2) with h=1/10 should be (9/10)^20 exactly
y2 = traj_decay[-1][1]
expected_decay = Fraction(9, 10) ** 20
ok = y2.to_fraction() == expected_decay
record(check("decay y(2) = (9/10)^20 exactly", ok))

# =========================================================================
section("3. Exact RK4")
# =========================================================================

def rk4_step(f, x, y, h):
    """Single RK4 step using exact VDR arithmetic."""
    k1 = f(x, y)
    k2 = f(x + h / VDR(2), y + h / VDR(2) * k1)
    k3 = f(x + h / VDR(2), y + h / VDR(2) * k2)
    k4 = f(x + h, y + h * k3)
    return y + h / VDR(6) * (k1 + VDR(2) * k2 + VDR(2) * k3 + k4)

def rk4_solve(f, y0, x0, h, n_steps):
    """Exact RK4 using VDR arithmetic."""
    x = x0
    y = y0
    trajectory = [(x, y)]
    for _ in range(n_steps):
        y = rk4_step(f, x, y, h)
        x = x + h
        trajectory.append((x, y))
    return trajectory

# dy/dx = y with RK4 and h=1/4, 4 steps to reach x=1
traj_rk4 = rk4_solve(f_exp, VDR(1), VDR(0), VDR(1, 4), 4)
y_rk4 = traj_rk4[-1][1]
print("  RK4 y(1) = %s" % y_rk4.to_fraction())
print("  RK4 float = %.15f  (e = %.15f)" % (
    float(y_rk4.to_fraction()), math.e))

# RK4 should be more accurate than Euler
rk4_err = abs(float(y_rk4.to_fraction()) - math.e)
euler_err = abs(float(traj[-1][1].to_fraction()) - math.e)
print("  Euler error: %.6e" % euler_err)
print("  RK4 error:   %.6e" % rk4_err)
record(check("RK4 more accurate than Euler", rk4_err < euler_err))

# the value is exact rational — no float involved in computation
record(check("RK4 result is exact rational",
             y_rk4.to_fraction().denominator > 1))

# =========================================================================
section("4. Linear system: matrix exponential approach")
# =========================================================================

# dx/dt = Ax, x(0) = x0
# solution: x(t) = e^(At) * x0
# for rational A and t, partial sum of e^(At) is exact

def mat_exp_at(A, t, terms):
    """Partial matrix exponential e^(At) = sum (At)^k / k!"""
    n = A.nrows
    At = A * t
    result = Mat.identity(n)
    power = Mat.identity(n)
    factorial = VDR(1)
    for k in range(1, terms):
        power = power * At
        factorial = factorial * VDR(k)
        result = result + power * (VDR(1) / factorial)
    return result

# simple rotation-like system: x' = [[0,1],[-1,0]] x
A = Mat([
    [VDR(0), VDR(1)],
    [VDR(-1), VDR(0)],
])
x0 = Vec([VDR(1), VDR(0)])

# compute x(1) using partial matrix exp with 10 terms
exp_A = mat_exp_at(A, VDR(1), 10)
x1 = exp_A * x0
print("  x(1) via matrix exp (10 terms):")
print("    x = %s" % [c.to_fraction() for c in x1])
# should approximate [cos(1), -sin(1)]
x1_float = [float(c.to_fraction()) for c in x1]
print("    float: [%.8f, %.8f]  (cos1=%.8f, -sin1=%.8f)" % (
    x1_float[0], x1_float[1], math.cos(1), -math.sin(1)))

# exact rational — no drift
record(check("matrix exp solution is exact rational",
             all(isinstance(c.to_fraction(), Fraction) for c in x1)))

# =========================================================================
section("5. Picard iteration")
# =========================================================================

# Picard iteration for dy/dx = y, y(0) = 1:
# y_0(x) = 1
# y_1(x) = 1 + integral_0^x y_0(t) dt = 1 + x
# y_2(x) = 1 + integral_0^x y_1(t) dt = 1 + x + x^2/2
# y_n(x) = sum_{k=0}^{n} x^k / k!  (truncated Taylor series for e^x)

# We can represent this as polynomial in x, exact VDR coefficients

def picard_exp(n_iterations):
    """Picard iterations for dy/dx = y, y(0) = 1.
    Returns polynomial coefficients [a0, a1, ..., an]."""
    # Start: y_0 = [1]  (constant polynomial)
    y = [VDR(1)]
    for iteration in range(n_iterations):
        # integrate: integral of [a0, a1, ..., ak] = [0, a0, a1/2, a2/3, ...]
        integrated = [VDR(0)]
        for i, coeff in enumerate(y):
            integrated.append(coeff / VDR(i + 1))
        # add initial condition: y = 1 + integral
        y = [VDR(1)] + integrated[1:]
    return y

# after n iterations, should get Taylor coefficients 1/k!
for n in [3, 5, 8]:
    coeffs = picard_exp(n)
    print("  Picard iteration %d:" % n)
    print("    coeffs = %s" % [c.to_fraction() for c in coeffs])

    # verify: coefficient of x^k should be 1/k!
    factorial = 1
    all_match = True
    for k in range(len(coeffs)):
        if k > 0:
            factorial *= k
        expected = Fraction(1, factorial)
        if coeffs[k].to_fraction() != expected:
            all_match = False
    record(check("Picard %d matches 1/k!" % n, all_match))

# evaluate at x=1: should approximate e
p8 = picard_exp(8)
e_approx = VDR(0)
for k, c in enumerate(p8):
    e_approx = e_approx + c  # x=1, so x^k = 1
print("  Picard e approx (8 terms): %s = %.12f" % (
    e_approx.to_fraction(), float(e_approx.to_fraction())))
err = abs(float(e_approx.to_fraction()) - math.e)
record(check("Picard e error < 1e-5", err < 1e-5))

# =========================================================================
section("6. System of ODEs: predator-prey (Euler)")
# =========================================================================

# Lotka-Volterra with rational parameters
# dx/dt = ax - bxy
# dy/dt = -cy + dxy
# with a=2/3, b=4/3, c=1, d=1 and (x0,y0) = (1, 1/2)

a_lv, b_lv, c_lv, d_lv = VDR(2, 3), VDR(4, 3), VDR(1), VDR(1)

def lv_step(state, h):
    x, y = state
    dx = a_lv * x - b_lv * x * y
    dy = VDR(0) - c_lv * y + d_lv * x * y
    return (x + h * dx, y + h * dy)

h = VDR(1, 100)
state = (VDR(1), VDR(1, 2))
trajectory_lv = [state]
for _ in range(200):
    state = lv_step(state, h)
    trajectory_lv.append(state)

print("  Lotka-Volterra (200 steps, h=1/100):")
for i in [0, 50, 100, 150, 200]:
    x, y = trajectory_lv[i]
    print("    t=%s: prey=%s  pred=%s" % (
        Fraction(i, 100), x.to_fraction(), y.to_fraction()))

# every value should be exact rational
all_exact = all(isinstance(x.to_fraction(), Fraction) and
                isinstance(y.to_fraction(), Fraction)
                for x, y in trajectory_lv)
record(check("all Lotka-Volterra values are exact rationals", all_exact))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 09 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
