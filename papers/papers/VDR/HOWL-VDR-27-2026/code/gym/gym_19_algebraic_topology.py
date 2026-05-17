"""
VDR Gym 19: Algebraic Topology
Boundary operators, chain complexes, Betti numbers, Euler characteristic.
All over Q using exact VDR rational arithmetic.
"""
from __future__ import annotations
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

# === 1. Triangle boundary operators ===
print("\n=== 1. Triangle boundary operators ===")

# simplicial complex: triangle with vertices {0,1,2}
# 0-simplices (vertices): v0, v1, v2
# 1-simplices (edges): e01, e02, e12
# 2-simplices (faces): f012

# boundary_1: edges -> vertices
# d(e01) = v1 - v0, d(e02) = v2 - v0, d(e12) = v2 - v1
#          v0  v1  v2
# e01:    [-1,  1,  0]
# e02:    [-1,  0,  1]
# e12:    [ 0, -1,  1]
B1 = Mat([
    [VDR(-1), VDR(1), VDR(0)],
    [VDR(-1), VDR(0), VDR(1)],
    [VDR(0), VDR(-1), VDR(1)],
])

# boundary_2: faces -> edges
# d(f012) = e12 - e02 + e01
#           e01  e02  e12
# f012:   [ 1,  -1,   1]
B2 = Mat([
    [VDR(1), VDR(-1), VDR(1)],
])

print("  B1 =")
print(B1.pretty())
print("  B2 =")
print(B2.pretty())

# === 2. Fundamental property: B1 * B2^T = 0 ===
print("\n=== 2. d∘d = 0 ===")

# B1 is 3x3 (3 edges, 3 vertices), B2 is 1x3 (1 face, 3 edges)
# B1 * B2^T should be 3x1 zero matrix
product = B1.T * B2.T
print("  B1 * B2^T =")
print(product.pretty())
is_zero = True
for i in range(product.nrows):
    for j in range(product.ncols):
        if product[i, j] != VDR(0):
            is_zero = False
check("d∘d = 0 (B1 * B2^T = 0)", is_zero)

# === 3. Betti numbers of triangle ===
print("\n=== 3. Betti numbers of filled triangle ===")

# beta_0 = dim(ker B1) = #vertices - rank(B1)
# For B1: rank = 2 (two independent rows)
rank_B1 = B1.T.rank()  # rank of B1 as a linear map
beta_0 = 3 - rank_B1
print("  rank(B1) = %d, beta_0 = %d" % (rank_B1, beta_0))
check("beta_0 = 1 (connected)", beta_0 == 1)

# beta_1 = dim(ker B1 restricted to image B2) ... 
# = #edges - rank(B1) - rank(B2)
rank_B2 = B2.rank()
beta_1 = 3 - rank_B1 - rank_B2
print("  rank(B2) = %d, beta_1 = %d" % (rank_B2, beta_1))
check("beta_1 = 0 (no holes)", beta_1 == 0)

# beta_2 = #faces - rank(B2) = 1 - 1 = 0 (for filled triangle, no voids)
# actually for a 2D filled triangle, there are no 3-simplices, so beta_2 = dim ker(B3) on 2-chains
# since there's only one 2-simplex and no boundary_3 operator, beta_2 = 1 - rank(B2) ... 
# wait: beta_2 = dim(ker partial_2) = dim of 2-cycles
# partial_2 maps 2-chains to 1-chains. If the face is a cycle (boundary is 0 in 1-chains), then...
# B2^T gives the boundary: B2^T * [1] = [1, -1, 1]^T which is nonzero in C_1
# so ker(partial_2) = 0, beta_2 = 0
check("beta_2 = 0 (no voids)", 1 - rank_B2 == 0)

# === 4. Euler characteristic ===
print("\n=== 4. Euler characteristic ===")

# chi = V - E + F = 3 - 3 + 1 = 1
# also chi = beta_0 - beta_1 + beta_2 = 1 - 0 + 0 = 1
chi_count = VDR(3) - VDR(3) + VDR(1)
chi_betti = VDR(beta_0) - VDR(beta_1) + VDR(0)
print("  chi (count) = %s, chi (Betti) = %s" % (chi_count, chi_betti))
check("Euler char = 1", chi_count == VDR(1))
check("Euler char from Betti = 1", chi_betti == VDR(1))
check("both methods agree", chi_count == chi_betti)

# === 5. Hollow triangle (boundary only, no face) ===
print("\n=== 5. Hollow triangle (cycle) ===")

# same B1, but no B2 (no 2-simplex)
# beta_0 = 3 - rank(B1) = 3 - 2 = 1
# beta_1 = #edges - rank(B1) = 3 - 2 = 1 (the triangle loop is a 1-cycle)
beta_1_hollow = 3 - rank_B1
print("  beta_1 (hollow) = %d" % beta_1_hollow)
check("hollow triangle beta_1 = 1 (one loop)", beta_1_hollow == 1)

# Euler: V - E = 3 - 3 = 0
chi_hollow = VDR(3) - VDR(3)
check("hollow triangle chi = 0", chi_hollow == VDR(0))

# === 6. Tetrahedron boundary ===
print("\n=== 6. Tetrahedron boundary operators ===")

# vertices: 0,1,2,3
# edges (6): 01,02,03,12,13,23
# faces (4): 012, 013, 023, 123
# B1 (6x4): boundary of edges -> vertices
# edge ordering: e01,e02,e03,e12,e13,e23
B1_tet = Mat([
    [VDR(-1), VDR(1), VDR(0), VDR(0)],   # e01
    [VDR(-1), VDR(0), VDR(1), VDR(0)],   # e02
    [VDR(-1), VDR(0), VDR(0), VDR(1)],   # e03
    [VDR(0), VDR(-1), VDR(1), VDR(0)],   # e12
    [VDR(0), VDR(-1), VDR(0), VDR(1)],   # e13
    [VDR(0), VDR(0), VDR(-1), VDR(1)],   # e23
])

# B2 (4x6): boundary of faces -> edges
# face 012: e12 - e02 + e01 = +e01 -e02 +0e03 +e12 +0e13 +0e23
# face 013: e13 - e03 + e01 = +e01 +0e02 -e03 +0e12 +e13 +0e23
# face 023: e23 - e03 + e02 = +0e01 +e02 -e03 +0e12 +0e13 +e23
# face 123: e23 - e13 + e12 = +0e01 +0e02 +0e03 +e12 -e13 +e23
B2_tet = Mat([
    [VDR(1), VDR(-1), VDR(0), VDR(1), VDR(0), VDR(0)],   # f012
    [VDR(1), VDR(0), VDR(-1), VDR(0), VDR(1), VDR(0)],   # f013
    [VDR(0), VDR(1), VDR(-1), VDR(0), VDR(0), VDR(1)],   # f023
    [VDR(0), VDR(0), VDR(0), VDR(1), VDR(-1), VDR(1)],   # f123
])

# d∘d = 0
prod_tet = B1_tet.T * B2_tet.T  # 4x4
is_zero_tet = True
for i in range(prod_tet.nrows):
    for j in range(prod_tet.ncols):
        if prod_tet[i, j] != VDR(0):
            is_zero_tet = False
check("tetrahedron d∘d = 0", is_zero_tet)

# Betti numbers of filled tetrahedron (solid, with interior)
# actually just the surface (hollow tetrahedron = sphere S^2)
rank_B1_tet = B1_tet.T.rank()
rank_B2_tet = B2_tet.rank()
print("  rank(B1) = %d, rank(B2) = %d" % (rank_B1_tet, rank_B2_tet))

# surface of tetrahedron = S^2
# beta_0 = 4 - rank(B1) = 4 - 3 = 1
# beta_1 = 6 - rank(B1) - rank(B2) = 6 - 3 - 3 = 0
# beta_2 = 4 - rank(B2) = 4 - 3 = 1
beta_0_tet = 4 - rank_B1_tet
beta_1_tet = 6 - rank_B1_tet - rank_B2_tet
beta_2_tet = 4 - rank_B2_tet

check("tetrahedron beta_0 = 1", beta_0_tet == 1)
check("tetrahedron beta_1 = 0", beta_1_tet == 0)
check("tetrahedron beta_2 = 1", beta_2_tet == 1)

# Euler: V-E+F = 4-6+4 = 2 (sphere)
chi_tet = VDR(4) - VDR(6) + VDR(4)
check("tetrahedron chi = 2 (sphere)", chi_tet == VDR(2))
check("chi = beta_0 - beta_1 + beta_2",
      chi_tet == VDR(beta_0_tet) - VDR(beta_1_tet) + VDR(beta_2_tet))

# === 7. Two disconnected edges ===
print("\n=== 7. Two disconnected edges ===")

# vertices: 0,1,2,3
# edges: 01, 23 (disconnected)
B1_disc = Mat([
    [VDR(-1), VDR(1), VDR(0), VDR(0)],
    [VDR(0), VDR(0), VDR(-1), VDR(1)],
])
rank_disc = B1_disc.T.rank()
beta_0_disc = 4 - rank_disc
print("  rank = %d, beta_0 = %d" % (rank_disc, beta_0_disc))
check("two components: beta_0 = 2", beta_0_disc == 2)


print("\n" + "=" * 50)
print("Gym 19 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 19 TESTS PASSED")
print("=" * 50)

