"""
VDR Gym 20: Tropical and Lattice Algebra
Min-plus matrix multiplication, tropical determinant, shortest path
as tropical matrix power, small LLL-style basis operations.
"""
from __future__ import annotations
import sys
sys.path.insert(0, '..')
from vdr import VDR, Mat

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

INF = VDR(10**9)

# === 1. Tropical (min-plus) matrix multiplication ===
print("\n=== 1. Tropical matrix multiplication ===")

def trop_mul(A, B, n):
    """Min-plus matrix product. A, B are n x n lists of lists of VDR."""
    C = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                val = A[i][k] + B[k][j]
                if val < C[i][j]:
                    C[i][j] = val
    return C

# adjacency matrix (weights)
# 3-node graph: 0->1: 2, 0->2: 5, 1->2: 1, 2->0: 3
W = [
    [VDR(0), VDR(2), VDR(5)],
    [INF, VDR(0), VDR(1)],
    [VDR(3), INF, VDR(0)],
]

# W^2 = shortest 2-hop paths
W2 = trop_mul(W, W, 3)
print("  W²[0][2] = %s (should be 3 = 0->1->2)" % W2[0][2])
check("W²[0][2] = 3 (path 0->1->2)", W2[0][2] == VDR(3))
print("  W²[2][1] = %s (should be 5 = 2->0->1)" % W2[2][1])
check("W²[2][1] = 5 (path 2->0->1)", W2[2][1] == VDR(5))

# W^3 = shortest 3-hop paths = all-pairs shortest path (for 3 nodes)
W3 = trop_mul(W2, W, 3)
print("  W³[0][0] = %s (should be min cycle through 0)" % W3[0][0])
# cycles through 0: 0->1->2->0 = 2+1+3=6, or just 0 (self)
check("W³[0][0] = 0 (self-loop)", W3[0][0] == VDR(0))
# 2->1: via 2->0->1 = 5, or 2->0->1->2->0->1 ... but 3-hop: 2->0->1 = 5
check("W³[2][1] = 5", W3[2][1] == VDR(5))

# === 2. Tropical determinant ===
print("\n=== 2. Tropical determinant ===")

def trop_det(M, n):
    """Tropical determinant = min over permutations of sum of M[i][sigma(i)]."""
    from itertools import permutations
    best = INF
    for perm in permutations(range(n)):
        total = VDR(0)
        for i in range(n):
            total = total + M[i][perm[i]]
        if total < best:
            best = total
    return best

M_td = [
    [VDR(1), VDR(3), VDR(2)],
    [VDR(4), VDR(1), VDR(5)],
    [VDR(2), VDR(3), VDR(1)],
]
td = trop_det(M_td, 3)
# diagonal: 1+1+1=3. perm (0,2,1): 2+5+3=10. etc. min should be 3.
print("  trop_det = %s" % td)
check("tropical det = 3 (diagonal)", td == VDR(3))

# identity: trop_det of tropical identity (0 on diag, INF off)
I_trop = [[VDR(0) if i == j else INF for j in range(3)] for i in range(3)]
check("trop_det(I) = 0", trop_det(I_trop, 3) == VDR(0))

# === 3. Shortest path as tropical matrix power ===
print("\n=== 3. Shortest path via tropical power ===")

# 4-node graph
G = [
    [VDR(0), VDR(1, 3), INF, VDR(1)],
    [INF, VDR(0), VDR(1, 4), INF],
    [INF, INF, VDR(0), VDR(1, 2)],
    [INF, INF, INF, VDR(0)],
]

# G^4 = all shortest paths (4 nodes, need at most 3 hops)
G2 = trop_mul(G, G, 4)
G3 = trop_mul(G2, G, 4)

# 0->2: 0->1->2 = 1/3 + 1/4 = 7/12
check("SP 0->2 = 7/12", G3[0][2] == VDR(7, 12))
# 0->3: min(0->3 direct = 1, 0->1->2->3 = 7/12+1/2 = 13/12)
# 1 < 13/12 so 0->3 = 1
check("SP 0->3 = 1", G3[0][3] == VDR(1))
# 0->1->2->3 = 13/12, direct 0->3 = 1. 1 < 13/12.
check("SP 1->3 = 3/4", G3[1][3] == VDR(3, 4))  # 1->2->3 = 1/4+1/2

# === 4. Lattice basis and Gram matrix ===
print("\n=== 4. Lattice Gram matrix ===")

# 2D lattice basis: v1 = (3, 1), v2 = (1, 2)
v1 = [VDR(3), VDR(1)]
v2 = [VDR(1), VDR(2)]

def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), VDR(0))

# Gram matrix G[i][j] = <vi, vj>
g11 = dot(v1, v1)  # 9+1 = 10
g12 = dot(v1, v2)  # 3+2 = 5
g22 = dot(v2, v2)  # 1+4 = 5
print("  G = [[%s, %s], [%s, %s]]" % (g11, g12, g12, g22))
check("g11 = 10", g11 == VDR(10))
check("g12 = 5", g12 == VDR(5))
check("g22 = 5", g22 == VDR(5))

# determinant of Gram = volume^2 of fundamental domain
gram_det = g11 * g22 - g12 * g12  # 50 - 25 = 25
check("det(Gram) = 25", gram_det == VDR(25))

# === 5. Gram-Schmidt mu coefficients (exact rational) ===
print("\n=== 5. Lattice Gram-Schmidt coefficients ===")

# mu_21 = <v2, v1> / <v1, v1> = 5/10 = 1/2
mu_21 = g12 / g11
print("  mu_21 = %s" % mu_21.to_fraction())
check("mu_21 = 1/2", mu_21 == VDR(1, 2))

# v2* = v2 - mu_21 * v1 = (1,2) - 1/2*(3,1) = (-1/2, 3/2)
v2_star = [v2[i] - mu_21 * v1[i] for i in range(2)]
print("  v2* = (%s, %s)" % (v2_star[0].to_fraction(), v2_star[1].to_fraction()))
check("v2*[0] = -1/2", v2_star[0] == VDR(-1, 2))
check("v2*[1] = 3/2", v2_star[1] == VDR(3, 2))

# verify orthogonality
orth = dot(v1, v2_star)
check("v1 · v2* = 0", orth == VDR(0))

# === 6. Size reduction step ===
print("\n=== 6. Lattice size reduction ===")

# if |mu_21| > 1/2, reduce: v2 = v2 - round(mu_21)*v1
# mu_21 = 1/2, so |mu_21| = 1/2, no reduction needed
needs_reduction = mu_21 > VDR(1, 2) or mu_21 < VDR(-1, 2)
check("no size reduction needed (|mu| <= 1/2)", not needs_reduction)

# test with a basis that needs reduction
w1 = [VDR(1), VDR(0)]
w2 = [VDR(3), VDR(1)]
mu_w = dot(w2, w1) / dot(w1, w1)  # 3/1 = 3
print("  mu = %s (needs reduction)" % mu_w.to_fraction())
check("mu = 3 (> 1/2, needs reduction)", mu_w > VDR(1, 2))

# reduce: w2' = w2 - 3*w1 = (0, 1)
r = VDR(3)  # round(mu)
w2_red = [w2[i] - r * w1[i] for i in range(2)]
print("  reduced w2 = (%s, %s)" % (w2_red[0], w2_red[1]))
check("reduced w2 = (0, 1)", w2_red[0] == VDR(0) and w2_red[1] == VDR(1))

# new mu
mu_new = dot(w2_red, w1) / dot(w1, w1)
check("new mu = 0", mu_new == VDR(0))

# === 7. Lovász condition check ===
print("\n=== 7. Lovász condition ===")

# LLL condition: |v2*|^2 >= (3/4 - mu^2) * |v1|^2
# for our original basis:
# |v2*|^2 = 1/4 + 9/4 = 10/4 = 5/2
# |v1|^2 = 10
# 3/4 - (1/2)^2 = 3/4 - 1/4 = 1/2
# (1/2)*10 = 5
# 5/2 >= 5? No! So this basis is NOT LLL-reduced.
v2star_sq = dot(v2_star, v2_star)
lovasz_rhs = (VDR(3, 4) - mu_21 * mu_21) * g11
print("  |v2*|^2 = %s, threshold = %s" % (
    v2star_sq.to_fraction(), lovasz_rhs.to_fraction()))
lovasz_holds = v2star_sq >= lovasz_rhs
check("Lovász condition: 5/2 < 5 (fails, swap needed)", not lovasz_holds)

# after swap: v1'=v2=(1,2), v2'=v1=(3,1)
# recompute
v1s, v2s = v2, v1
g11s = dot(v1s, v1s)  # 5
g12s = dot(v2s, v1s)  # 5
mu_s = g12s / g11s     # 5/5 = 1
# size reduce: v2s = v2s - 1*v1s = (3,1)-(1,2) = (2,-1)
v2s = [v2s[i] - VDR(1) * v1s[i] for i in range(2)]
mu_s2 = dot(v2s, v1s) / dot(v1s, v1s)  # (2-2)/5 = 0
v2s_star = v2s  # since mu=0, v2* = v2
v2s_sq = dot(v2s_star, v2s_star)  # 4+1 = 5
lovasz_rhs2 = (VDR(3, 4) - mu_s2 * mu_s2) * dot(v1s, v1s)  # 3/4 * 5 = 15/4
lovasz2 = v2s_sq >= lovasz_rhs2  # 5 >= 15/4 = true
check("after swap+reduce: Lovász holds (5 >= 15/4)", lovasz2)


print("\n" + "=" * 50)
print("Gym 20 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 20 TESTS PASSED")
print("=" * 50)

