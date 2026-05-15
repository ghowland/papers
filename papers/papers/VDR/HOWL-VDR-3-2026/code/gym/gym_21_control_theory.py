"""
VDR Gym 21: Control Theory
State space models, controllability, observability, transfer functions.
All with rational coefficients and exact VDR arithmetic.
"""
from __future__ import annotations
from fractions import Fraction
import sys
sys.path.insert(0, '..')
from vdr import VDR, Vec, Mat

passed = 0
failed = 0
def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print("  PASS: %s" % name)
    else:
        failed += 1
        print("  FAIL: %s" % name)

# === 1. State space model: x' = Ax + Bu, y = Cx ===
print("\n=== 1. State space model ===")

# 2-state system
A = Mat([
    [VDR(0), VDR(1)],
    [VDR(-2), VDR(-3)],
])
B = Mat([
    [VDR(0)],
    [VDR(1)],
])
C = Mat([
    [VDR(1), VDR(0)],
])

print("  A =")
print(A.pretty())
print("  B = [[0],[1]]")
print("  C = [[1, 0]]")

# === 2. Controllability matrix [B, AB, A²B, ...] ===
print("\n=== 2. Controllability ===")

AB = A * B
ctrl = Mat([
    [B[0, 0], AB[0, 0]],
    [B[1, 0], AB[1, 0]],
])
print("  controllability matrix =")
print(ctrl.pretty())

ctrl_rank = ctrl.rank()
check("controllability rank = 2 (full)", ctrl_rank == 2)

ctrl_det = ctrl.det()
print("  det(ctrl) = %s" % ctrl_det)
check("ctrl det != 0 (controllable)", ctrl_det != VDR(0))

# === 3. Observability matrix [C; CA; CA²; ...] ===
print("\n=== 3. Observability ===")

CA = C * A
obs = Mat([
    [C[0, 0], C[0, 1]],
    [CA[0, 0], CA[0, 1]],
])
print("  observability matrix =")
print(obs.pretty())

obs_rank = obs.rank()
check("observability rank = 2 (full)", obs_rank == 2)

obs_det = obs.det()
print("  det(obs) = %s" % obs_det)
check("obs det != 0 (observable)", obs_det != VDR(0))

# === 4. Characteristic polynomial ===
print("\n=== 4. Characteristic polynomial ===")

# char poly of A: det(sI - A) = s^2 + 3s + 2 = (s+1)(s+2)
# trace = 0 + (-3) = -3, det = 0*(-3) - 1*(-2) = 2
tr = A.trace()
det_A = A.det()
print("  trace(A) = %s, det(A) = %s" % (tr, det_A))
check("trace = -3", tr == VDR(-3))
check("det = 2", det_A == VDR(2))
# char poly: s^2 - trace*s + det = s^2 + 3s + 2
# poles at s = -1, -2 (both negative = stable)
# verify Cayley-Hamilton: A^2 + 3A + 2I = 0
A2 = A * A
I2 = Mat.identity(2)
CH = A2 + A.scale(VDR(3)) + I2.scale(VDR(2))
print("  A² + 3A + 2I =")
print(CH.pretty())
ch_zero = True
for i in range(2):
    for j in range(2):
        if CH[i, j] != VDR(0):
            ch_zero = False
check("Cayley-Hamilton: A²+3A+2I = 0", ch_zero)

# === 5. Transfer function evaluation ===
print("\n=== 5. Transfer function H(s) = C(sI-A)^{-1}B ===")

# evaluate at s = 1 (rational)
s = VDR(1)
sI_A = Mat([
    [s - A[0, 0], VDR(0) - A[0, 1]],
    [VDR(0) - A[1, 0], s - A[1, 1]],
])
print("  sI - A at s=1:")
print(sI_A.pretty())

sI_A_inv = sI_A.inv()
H_s = C * sI_A_inv * B
print("  H(1) = %s" % H_s[0, 0].to_fraction())
# (sI-A) at s=1: [[1,-1],[2,4]], det = 4+2 = 6
# inv = [[4,1],[-2,1]]/6
# inv*B = [[1],[-2+1]]/6 = [[1/6],[-1/6]] wait...
# inv = [[4/6, 1/6], [-2/6, 1/6]] = [[2/3, 1/6], [-1/3, 1/6]]
# inv*B = [[1/6],  [1/6]]
# C * inv * B = 1/6
check("H(1) = 1/6", H_s[0, 0] == VDR(1, 6))

# evaluate at s = 0
sI_A_0 = Mat([
    [VDR(0) - A[0, 0], VDR(0) - A[0, 1]],
    [VDR(0) - A[1, 0], VDR(0) - A[1, 1]],
])
H_0 = C * sI_A_0.inv() * B
print("  H(0) = %s (DC gain)" % H_0[0, 0].to_fraction())
# -A = [[0,-1],[2,3]], det=2, inv=[[3,1],[-2,0]]/2
# inv*B = [[1],[0]]/2 = [[1/2],[0]]
# C*[1/2,0] = 1/2
check("H(0) = 1/2 (DC gain)", H_0[0, 0] == VDR(1, 2))

# === 6. Discrete-time state evolution ===
print("\n=== 6. Discrete state evolution ===")

# x[k+1] = A_d * x[k] + B_d * u[k]
# use simple A_d = I + h*A (Euler discretization) with h = 1/10
h = VDR(1, 10)
A_d = Mat.identity(2) + A.scale(h)
B_d = B.scale(h)
print("  A_d =")
print(A_d.pretty())

# initial state x0 = [1, 0], input u = 0 (free response)
x = Vec([VDR(1), VDR(0)])
trajectory = [x]
for k in range(5):
    x = Vec([
        A_d[0, 0] * x.data[0] + A_d[0, 1] * x.data[1],
        A_d[1, 0] * x.data[0] + A_d[1, 1] * x.data[1],
    ])
    trajectory.append(x)

# all values should be exact rationals
all_exact = True
for t in trajectory:
    for xi in t._data:
        if not xi.is_closed:
            all_exact = False
check("all trajectory values exact rational", all_exact)

# system is stable (eigenvalues of A are -1, -2), so x should decay
# check |x[5]| < |x[0]|
x5_mag = trajectory[5][0] * trajectory[5][0] + trajectory[5][1] * trajectory[5][1]
x0_mag = VDR(1)  # |x0|^2 = 1
check("state decays (|x5|^2 < |x0|^2)", x5_mag < x0_mag)
print("  x[5] = (%s, %s)" % (
    trajectory[5][0].to_fraction(), trajectory[5][1].to_fraction()))

# === 7. Controllability Gramian (discrete, finite horizon) ===
print("\n=== 7. Finite controllability Gramian ===")

# W_c = sum_{k=0}^{N-1} A_d^k * B_d * B_d^T * (A_d^T)^k
# for N = 3 steps
def mat_pow(M, n):
    result = Mat.identity(M.nrows)
    for _ in range(n):
        result = result * M
    return result

W_c = Mat.zero(2, 2)
for k in range(3):
    Ak = mat_pow(A_d, k)
    term = Ak * B_d  # 2x1
    # term * term^T = 2x2
    tt = Mat([
        [term[0, 0] * term[0, 0], term[0, 0] * term[1, 0]],
        [term[1, 0] * term[0, 0], term[1, 0] * term[1, 0]],
    ])
    W_c = W_c + tt

print("  W_c =")
print(W_c.pretty())

# Gramian should be positive definite (det > 0, trace > 0)
wc_det = W_c.det()
wc_tr = W_c.trace()
print("  det(W_c) = %s, trace(W_c) = %s" % (
    wc_det.to_fraction(), wc_tr.to_fraction()))
check("Gramian det > 0 (controllable)", wc_det > VDR(0))
check("Gramian trace > 0", wc_tr > VDR(0))
check("Gramian symmetric", W_c == W_c.T)


print("\n" + "=" * 50)
print("Gym 21 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 21 TESTS PASSED")
print("=" * 50)

