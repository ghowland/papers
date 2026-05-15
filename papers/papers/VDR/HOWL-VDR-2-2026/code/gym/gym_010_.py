#!/usr/bin/env python3
"""
gym_10_optimization.py — VDR exercises in optimization

Golden section search, Newton's method for optimization,
linear programming (simplex), and gradient descent —
all using exact VDR rational arithmetic.
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
section("1. Newton's method for optimization (exact)")
# =========================================================================

# minimize f(x) = x^2 - 4x + 7
# f'(x) = 2x - 4, f''(x) = 2
# Newton step: x_{n+1} = x_n - f'(x_n)/f''(x_n) = x_n - (2x-4)/2 = 2

def newton_optimize(f_prime, f_double_prime, x0, n_steps):
    """Newton's method for optimization using exact VDR."""
    x = x0
    trajectory = [x]
    for _ in range(n_steps):
        x = x - f_prime(x) / f_double_prime(x)
        trajectory.append(x)
    return trajectory

fp = lambda x: VDR(2) * x - VDR(4)
fpp = lambda x: VDR(2)

traj = newton_optimize(fp, fpp, VDR(10), 5)
print("  Newton optimization for x^2-4x+7:")
for i, x in enumerate(traj):
    print("    step %d: x = %s" % (i, x.to_fraction()))

# should converge to x=2 in ONE step for quadratic
record(check("converges to x=2 in 1 step", traj[1] == VDR(2)))

# cubic: f(x) = x^3 - 6x^2 + 9x + 1
# f'(x) = 3x^2 - 12x + 9, f''(x) = 6x - 12
fp_cubic = lambda x: VDR(3) * x * x - VDR(12) * x + VDR(9)
fpp_cubic = lambda x: VDR(6) * x - VDR(12)

traj2 = newton_optimize(fp_cubic, fpp_cubic, VDR(0), 10)
print("  Newton for x^3-6x^2+9x+1:")
for i, x in enumerate(traj2[:6]):
    print("    step %d: x = %s" % (i, x.to_fraction()))

# should approach x=3 (local min) — check convergence
diffs = [abs(float(traj2[i+1].to_fraction() - traj2[i].to_fraction()))
         for i in range(min(8, len(traj2)-1))]
record(check("Newton cubic converges (diffs decrease)",
             all(diffs[i] >= diffs[i+1] - 1e-15 for i in range(len(diffs)-1))))

# =========================================================================
section("2. Gradient descent with exact rational step")
# =========================================================================

# minimize f(x,y) = x^2 + 2y^2
# gradient: [2x, 4y]
# step: [x,y] -= lr * [2x, 4y]

def gradient_descent_2d(grad, x0, y0, lr, steps):
    x, y = x0, y0
    traj = [(x, y)]
    for _ in range(steps):
        gx, gy = grad(x, y)
        x = x - lr * gx
        y = y - lr * gy
        traj.append((x, y))
    return traj

grad_f = lambda x, y: (VDR(2) * x, VDR(4) * y)
lr = VDR(1, 10)

traj_gd = gradient_descent_2d(grad_f, VDR(
    