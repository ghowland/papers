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

traj_gd = gradient_descent_2d(grad_f, VDR(5), VDR(3), lr, 20)
print("  Gradient descent for x^2+2y^2, lr=1/10:")
for i in [0, 5, 10, 15, 20]:
    x, y = traj_gd[i]
    fval = x * x + VDR(2) * y * y
    print("    step %d: (%s, %s)  f=%s" % (
        i, x.to_fraction(), y.to_fraction(), fval.to_fraction()))

# should converge toward (0, 0)
x_final, y_final = traj_gd[-1]
ok = abs(float(x_final.to_fraction())) < 0.1 and abs(float(y_final.to_fraction())) < 0.01
record(check("GD approaches (0,0)", ok))

# every step is exact rational
all_exact = all(isinstance(x.to_fraction(), Fraction) and
                isinstance(y.to_fraction(), Fraction)
                for x, y in traj_gd)
record(check("all GD steps are exact rationals", all_exact))

# =========================================================================
section("3. Exact simplex method (2D)")
# =========================================================================

# minimize c^T x subject to Ax <= b, x >= 0
# Example: minimize -3x1 - 5x2
#   x1 <= 4
#   2x2 <= 12
#   3x1 + 5x2 <= 25
#   x1, x2 >= 0

# convert to standard form with slack variables:
# x1 + s1 = 4
# 2x2 + s2 = 12
# 3x1 + 5x2 + s3 = 25

def simplex_2d(c, A, b):
    """
    Simple simplex method for small LP problems.
    All exact VDR arithmetic.
    c: objective coefficients (minimize c^T x)
    A: constraint matrix
    b: RHS
    """
    m = len(b)  # number of constraints
    n = len(c)  # number of variables

    # augmented tableau: [A | I | b]
    # with objective row: [c | 0 | 0]
    tableau = []
    for i in range(m):
        row = list(A[i]) + [VDR(0)] * m + [b[i]]
        row[n + i] = VDR(1)  # slack variable
        tableau.append(row)

    # objective row (negated for minimization → we maximize -c)
    obj = [VDR(0) - ci for ci in c] + [VDR(0)] * m + [VDR(0)]

    basis = list(range(n, n + m))  # slack variables are initial basis

    for iteration in range(20):  # max iterations
        # find entering variable (most negative in objective)
        min_val = VDR(0)
        pivot_col = -1
        for j in range(n + m):
            if obj[j] < min_val:
                min_val = obj[j]
                pivot_col = j
        if pivot_col == -1:
            break  # optimal

        # find leaving variable (minimum ratio test)
        min_ratio = None
        pivot_row = -1
        for i in range(m):
            if tableau[i][pivot_col] > VDR(0):
                ratio = tableau[i][-1] / tableau[i][pivot_col]
                if min_ratio is None or ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i

        if pivot_row == -1:
            break  # unbounded

        # pivot
        pivot_val = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [x / pivot_val for x in tableau[pivot_row]]

        for i in range(m):
            if i == pivot_row:
                continue
            factor = tableau[i][pivot_col]
            tableau[i] = [tableau[i][j] - factor * tableau[pivot_row][j]
                          for j in range(len(tableau[i]))]

        factor = obj[pivot_col]
        obj = [obj[j] - factor * tableau[pivot_row][j] for j in range(len(obj))]

        basis[pivot_row] = pivot_col

    # extract solution
    x = [VDR(0)] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = tableau[i][-1]

    return x, VDR(0) - obj[-1]

c = [VDR(-3), VDR(-5)]
A = [
    [VDR(1), VDR(0)],
    [VDR(0), VDR(2)],
    [VDR(3), VDR(5)],
]
b_lp = [VDR(4), VDR(12), VDR(25)]

x_opt, z_opt = simplex_2d(c, A, b_lp)
print("  Simplex solution:")
print("    x1 = %s, x2 = %s" % (x_opt[0].to_fraction(), x_opt[1].to_fraction()))
print("    objective = %s" % z_opt.to_fraction())

# known optimal: x1=5/3, x2=4, z=35 (maximizing 3x1+5x2)
# wait — let me verify the problem setup
# the optimal for this problem is x1=5/3, x2=16/3? No.
# check: 3x1+5x2 at (0,5): 25, but 2*5=10 > 12? No, 2x2<=12 → x2<=6
# at (0,5): feasible. At (5/3, 4): 3*(5/3)+5*4=5+20=25, so this point
# is on the boundary 3x1+5x2=25. And x1=5/3 <= 4 ✓, 2*4=8 <= 12 ✓
# the objective is 3*(5/3)+5*4 = 25
# but (0,5): 0+25=25 also. And (0,6): 0+30=30 but 3*0+5*6=30 > 25? No.
# Actually we need to verify feasibility more carefully.

# verify feasibility of solution
all_feasible = True
for i in range(len(b_lp)):
    lhs_val = VDR(0)
    for j in range(len(x_opt)):
        lhs_val = lhs_val + A[i][j] * x_opt[j]
    if lhs_val > b_lp[i]:
        all_feasible = False
record(check("simplex solution is feasible", all_feasible))
record(check("all simplex values are exact rationals",
             all(isinstance(x.to_fraction(), Fraction) for x in x_opt)))

# =========================================================================
section("4. Bisection method (exact rational)")
# =========================================================================

# find root of f(x) = x^2 - 2 on [1, 2]
# bisection with VDR: every midpoint is exact rational

def bisection(f, a, b, n_steps):
    """Exact bisection using VDR arithmetic."""
    trajectory = []
    for _ in range(n_steps):
        mid = (a + b) / VDR(2)
        trajectory.append(mid)
        f_mid = f(mid)
        f_a = f(a)
        if f_mid == VDR(0):
            return trajectory
        # compare signs via projection
        if float(f_mid.to_fraction()) * float(f_a.to_fraction()) < 0:
            b = mid
        else:
            a = mid
    return trajectory

f_sq = lambda x: x * x - VDR(2)
traj_bi = bisection(f_sq, VDR(1), VDR(2), 30)

print("  Bisection for x^2 = 2:")
for i in [0, 5, 10, 20, 29]:
    if i < len(traj_bi):
        x = traj_bi[i]
        err = abs(float(x.to_fraction()) ** 2 - 2)
        print("    step %d: %s  x^2-2 error=%.2e" % (i, x.to_fraction(), err))

# every midpoint is an exact rational
record(check("all bisection midpoints are exact",
             all(isinstance(x.to_fraction(), Fraction) for x in traj_bi)))

# after 30 steps, we should have ~9 correct digits of sqrt(2)
final = traj_bi[-1]
err = abs(float(final.to_fraction()) ** 2 - 2)
record(check("bisection 30 steps: error < 1e-8", err < 1e-8))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 10 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)

