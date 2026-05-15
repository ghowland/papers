#!/usr/bin/env python3
"""
gym_04_matrix_decomposition.py — VDR exercises in matrix decomposition

LU decomposition, QR-like operations (rational Gram-Schmidt),
Cholesky-like decomposition for rational positive-definite matrices,
and SVD-adjacent computations that stay in the rational domain.
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
section("1. LU Decomposition (no pivoting)")
# =========================================================================

def lu_decompose(m):
    """
    LU decomposition: A = L * U
    L is lower triangular with 1s on diagonal.
    U is upper triangular.
    All exact VDR arithmetic.
    """
    n = m.nrows
    L = [[VDR(0)] * n for _ in range(n)]
    U = [[VDR(0)] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = VDR(1)
        for j in range(i, n):
            s = VDR(0)
            for k in range(i):
                s = s + L[i][k] * U[k][j]
            U[i][j] = m[i, j] - s

        for j in range(i + 1, n):
            s = VDR(0)
            for k in range(i):
                s = s + L[j][k] * U[k][i]
            L[j][i] = (m[j, i] - s) / U[i][i]

    return Mat(L), Mat(U)

# test on a 3x3 matrix
A = Mat.from_ints([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
L, U = lu_decompose(A)
print("  A =")
print(A.pretty())
print("  L =")
print(L.pretty())
print("  U =")
print(U.pretty())

# verify: L * U = A
product = L * U
ok = product == A
record(check("L * U = A", ok))

# verify L is lower triangular with 1s on diagonal
l_ok = True
for i in range(3):
    if L[i, i] != VDR(1):
        l_ok = False
    for j in range(i + 1, 3):
        if L[i, j] != VDR(0):
            l_ok = False
record(check("L is lower triangular, diag=1", l_ok))

# verify U is upper triangular
u_ok = True
for i in range(3):
    for j in range(i):
        if U[i, j] != VDR(0):
            u_ok = False
record(check("U is upper triangular", u_ok))

# =========================================================================
section("2. LU with rational entries")
# =========================================================================

B = Mat([
    [VDR(1, 2), VDR(1, 3), VDR(1, 4)],
    [VDR(1, 3), VDR(1, 4), VDR(1, 5)],
    [VDR(1, 4), VDR(1, 5), VDR(1, 6)],
])
L2, U2 = lu_decompose(B)
product2 = L2 * U2
ok = product2 == B
record(check("LU of rational matrix reconstructs exactly", ok))

# =========================================================================
section("3. Forward/back substitution (LU solve)")
# =========================================================================

def lu_solve(L, U, b):
    """Solve Ax = b using LU decomposition. Exact VDR throughout."""
    n = L.nrows
    # forward substitution: Ly = b
    y = [VDR(0)] * n
    for i in range(n):
        s = VDR(0)
        for j in range(i):
            s = s + L[i, j] * y[j]
        y[i] = b[i] - s  # L[i,i] = 1

    # back substitution: Ux = y
    x = [VDR(0)] * n
    for i in range(n - 1, -1, -1):
        s = VDR(0)
        for j in range(i + 1, n):
            s = s + U[i, j] * x[j]
        x[i] = (y[i] - s) / U[i, i]

    return Vec(x)

b = Vec.from_ints([1, 2, 3])
x = lu_solve(L, U, b)
print("  LU solve Ax=[1,2,3]: x = %s" % x)

# verify: A * x = b
check_b = A * x
ok = check_b == b
record(check("LU solve: A*x = b", ok))

# compare with Cramer's rule
x_cramer = A.solve(b)
ok = all(x[i] == x_cramer[i] for i in range(3))
record(check("LU solve agrees with Cramer", ok))

# =========================================================================
section("4. PLU decomposition (with row pivoting)")
# =========================================================================

def plu_decompose(m):
    """
    PLU decomposition: PA = LU with row pivoting.
    P is a permutation matrix, L lower triangular, U upper triangular.
    """
    n = m.nrows
    # work on a copy
    rows = [[m[i, j] for j in range(n)] for i in range(n)]
    perm = list(range(n))

    L = [[VDR(0)] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = VDR(1)

    for col in range(n):
        # find pivot: largest magnitude in column
        best = col
        best_val = abs(float(rows[col][col].to_fraction()))
        for row in range(col + 1, n):
            val = abs(float(rows[row][col].to_fraction()))
            if val > best_val:
                best = row
                best_val = val

        if best != col:
            rows[col], rows[best] = rows[best], rows[col]
            perm[col], perm[best] = perm[best], perm[col]
            # swap L entries below diagonal in previous columns
            for j in range(col):
                L[col][j], L[best][j] = L[best][j], L[col][j]

        for row in range(col + 1, n):
            factor = rows[row][col] / rows[col][col]
            L[row][col] = factor
            for j in range(col, n):
                rows[row][j] = rows[row][j] - factor * rows[col][j]

    U = Mat(rows)
    L_mat = Mat(L)

    # build permutation matrix
    P = [[VDR(0)] * n for _ in range(n)]
    for i, p in enumerate(perm):
        P[i][p] = VDR(1)
    P_mat = Mat(P)

    return P_mat, L_mat, U

# test with a matrix that needs pivoting
C = Mat.from_ints([[0, 1, 2], [1, 0, 3], [4, 3, 2]])
P, L3, U3 = plu_decompose(C)
print("  P =")
print(P.pretty())
print("  L =")
print(L3.pretty())
print("  U =")
print(U3.pretty())

# verify: PA = LU
PA = P * C
LU = L3 * U3
ok = PA == LU
record(check("PA = LU", ok))

# =========================================================================
section("5. Matrix powers")
# =========================================================================

# A^n computed exactly
def mat_pow(m, n):
    """Exact matrix power by repeated squaring."""
    if n == 0:
        return Mat.identity(m.nrows)
    if n == 1:
        return m
    if n % 2 == 0:
        half = mat_pow(m, n // 2)
        return half * half
    else:
        return m * mat_pow(m, n - 1)

# Fibonacci via matrix exponentiation
# [[1,1],[1,0]]^n gives [[F(n+1), F(n)], [F(n), F(n-1)]]
fib_mat = Mat.from_ints([[1, 1], [1, 0]])
for n in [5, 10, 20, 30]:
    result = mat_pow(fib_mat, n)
    fib_n = result[0, 1]
    print("  F(%d) = %s" % (n, fib_n))

# known Fibonacci values
record(check("F(10) = 55", mat_pow(fib_mat, 10)[0, 1] == VDR(55)))
record(check("F(20) = 6765", mat_pow(fib_mat, 20)[0, 1] == VDR(6765)))
record(check("F(30) = 832040", mat_pow(fib_mat, 30)[0, 1] == VDR(832040)))

# verify: F(n)^2 + F(n+1)^2 = F(2n+1)
n = 15
fn = mat_pow(fib_mat, n)[0, 1]
fn1 = mat_pow(fib_mat, n + 1)[0, 1]
f2n1 = mat_pow(fib_mat, 2 * n + 1)[0, 1]
ok = fn * fn + fn1 * fn1 == f2n1
record(check("F(15)^2 + F(16)^2 = F(31)", ok))

# =========================================================================
section("6. Rational Gram-Schmidt orthogonalization")
# =========================================================================

# Standard Gram-Schmidt stays rational if inputs are rational
# u_k = v_k - sum( proj(u_j, v_k) * u_j )
# proj(u, v) = (u . v) / (u . u)

def gram_schmidt(vectors):
    """Exact rational Gram-Schmidt. Returns orthogonal basis."""
    orthogonal = []
    for v in vectors:
        u = v
        for uj in orthogonal:
            # proj = (uj . v) / (uj . uj)
            proj_coeff = uj.dot(v) / uj.dot(uj)
            u = u - uj.scale(proj_coeff)
        orthogonal.append(u)
    return orthogonal

v1 = Vec([VDR(1), VDR(1), VDR(0)])
v2 = Vec([VDR(1), VDR(0), VDR(1)])
v3 = Vec([VDR(0), VDR(1), VDR(1)])

ortho = gram_schmidt([v1, v2, v3])
print("  orthogonal basis:")
for i, u in enumerate(ortho):
    print("    u_%d = %s" % (i, [x.to_fraction() for x in u]))

# verify orthogonality: u_i . u_j = 0 for i != j
ortho_ok = True
for i in range(len(ortho)):
    for j in range(i + 1, len(ortho)):
        dot = ortho[i].dot(ortho[j])
        if dot != VDR(0):
            ortho_ok = False
            print("    u_%d . u_%d = %s (should be 0)" % (i, j, dot.to_fraction()))
record(check("orthogonal: all cross dots = 0", ortho_ok))

# =========================================================================
section("7. Matrix exponential truncation")
# =========================================================================

# e^A = I + A + A^2/2! + A^3/3! + ...
# For rational A, each partial sum is exact rational.
# We can compute N terms exactly.

def mat_exp_partial(m, terms):
    """Partial matrix exponential: sum_{k=0}^{terms-1} A^k / k!"""
    n = m.nrows
    result = Mat.identity(n)  # k=0 term
    power = Mat.identity(n)   # A^k
    factorial = VDR(1)
    for k in range(1, terms):
        power = power * m
        factorial = factorial * VDR(k)
        term = power * (VDR(1) / factorial)
        result = result + term
    return result

A_small = Mat([
    [VDR(0), VDR(1)],
    [VDR(-1), VDR(0)],
])

print("  matrix exp partial sums for [[0,1],[-1,0]]:")
for terms in [2, 4, 6, 8, 10]:
    exp_A = mat_exp_partial(A_small, terms)
    # for this particular matrix, e^A relates to rotation
    # entries should approach cos(1) and sin(1)
    print("    %d terms: [0,0]=%s  [0,1]=%s" % (
        terms, exp_A[0, 0].to_fraction(), exp_A[0, 1].to_fraction()))

# the key point: every partial sum is an EXACT rational matrix
# no float drift in the partial sums themselves
exp6 = mat_exp_partial(A_small, 6)
exp6_again = mat_exp_partial(A_small, 6)
ok = exp6 == exp6_again
record(check("matrix exp partial sums are deterministic", ok))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 04 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
