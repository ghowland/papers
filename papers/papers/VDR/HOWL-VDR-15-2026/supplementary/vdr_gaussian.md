# VDR GYM 24: EXACT GAUSSIAN ELIMINATION

## G24-01: 3×3 solve, unique solution
Ax=b where A=[[2,1,-1],[4,3,-1],[2,-1,3]], b=[1,5,7]. Row reduce with partial pivoting. Verify x against Cramer's rule result from existing linalg module. Both must match exactly.

## G24-02: 3×3 determinant via pivot product
Same matrix as G24-01. Determinant = product of pivots × sign from row swaps. Compare against cofactor det. Exact match required.

## G24-03: Zero pivot requiring row swap
A=[[0,1,2],[1,0,3],[2,1,0]], b=[5,6,7]. First pivot is zero, must swap. Solve and verify by substitution: A×x = b exactly.

## G24-04: 4×4 Hilbert inverse
H₄ Hilbert matrix. Gaussian elimination to get H⁻¹. Verify H×H⁻¹ = I exactly. Compare against existing adjugate inverse — same result.

## G24-05: 5×5 Hilbert inverse
H₅. Same verification. This is where float fails at ~1e-9 residual. VDR Gaussian must give exact zero off-diagonal.

## G24-06: 10×10 Hilbert inverse
H₁₀. Cofactor expansion is impractical here. Gaussian must complete in reasonable time. H×H⁻¹ = I exactly.

## G24-07: 20×20 Hilbert inverse
H₂₀. Pure scaling test. Cofactor is impossible. Gaussian at O(n³) should handle it. Verify H×H⁻¹ = I exactly.

## G24-08: Singular matrix detection
A=[[1,2,3],[4,5,6],[7,8,9]]. Rank 2. Gaussian elimination must detect zero pivot after reduction with no valid swap available. Report rank=2, determinant=0.

## G24-09: 5×5 random rationals solve
A with entries from {1/7, -3/5, 2/3, 11/13, -1/4} arranged to be nonsingular. Solve Ax=b. Verify by substitution. Compare against Cramer's rule.

## G24-10: Determinant sign tracking
4×4 requiring exactly 2 row swaps during elimination. Verify det via Gaussian (pivot product × (-1)²) matches cofactor det. Sign must be exact.

## G24-11: LU consistency
Same matrix as G24-03. Extract L and U from Gaussian elimination. Verify P×A = L×U exactly. Compare against Gym 04 PLU results — must match.

## G24-12: 30×30 Hilbert inverse
H₃₀. Stress test. O(n³) = 27000 VDR operations. Verify diagonal of H×H⁻¹ = 1 and spot-check 10 off-diagonal entries = 0.

## G24-13: Overdetermined least-squares setup
A is 4×3 rank 3. Form AᵀA (3×3) and Aᵀb. Solve normal equations via Gaussian. Verify AᵀA×x = Aᵀb exactly.

## G24-14: Condition number irrelevance
H₅ has float condition number ~4.8×10⁵. Construct two right-hand sides b₁ and b₂ differing by 10⁻¹⁰ in one entry. Solve both via Gaussian. Solutions differ by exactly the right amount — no amplification of error because there is no error.

---

```python
# G24-01: 3×3 solve, unique solution
A = Mat([[2,1,-1],[4,3,-1],[2,-1,3]])
b = Vec([1,5,7])
x_gauss = gaussian_solve(A, b)
x_cramer = solve(A, b)  # existing Cramer's rule
assert x_gauss == x_cramer
assert A @ x_gauss == b

# G24-02: 3×3 determinant via pivot product
d_gauss = gaussian_det(A)
d_cofactor = det(A)
assert d_gauss == d_cofactor

# G24-03: Zero pivot requiring row swap
A3 = Mat([[0,1,2],[1,0,3],[2,1,0]])
b3 = Vec([5,6,7])
x3 = gaussian_solve(A3, b3)
assert A3 @ x3 == b3

# G24-04: 4×4 Hilbert inverse
H4 = hilbert(4)
H4inv = gaussian_inverse(H4)
assert H4 @ H4inv == Mat.identity(4)
assert H4inv == inverse(H4)  # matches adjugate path

# G24-05: 5×5 Hilbert inverse
H5 = hilbert(5)
H5inv = gaussian_inverse(H5)
I5 = H5 @ H5inv
for i in range(5):
    for j in range(5):
        assert I5[i][j] == (VDR(1,1,0) if i==j else VDR(0,1,0))

# G24-06: 10×10 Hilbert inverse
H10 = hilbert(10)
H10inv = gaussian_inverse(H10)
assert H10 @ H10inv == Mat.identity(10)

# G24-07: 20×20 Hilbert inverse
H20 = hilbert(20)
H20inv = gaussian_inverse(H20)
assert H20 @ H20inv == Mat.identity(20)

# G24-08: Singular matrix detection
Asing = Mat([[1,2,3],[4,5,6],[7,8,9]])
r, d = gaussian_rank_and_det(Asing)
assert r == 2
assert d == VDR(0,1,0)

# G24-09: 5×5 random rationals solve
entries = [
    [VDR(1,7,0), VDR(-3,5,0), VDR(2,3,0), VDR(11,13,0), VDR(-1,4,0)],
    [VDR(2,3,0), VDR(1,7,0), VDR(-1,4,0), VDR(3,5,0), VDR(7,13,0)],
    [VDR(-1,4,0), VDR(2,3,0), VDR(1,7,0), VDR(-3,5,0), VDR(11,13,0)],
    [VDR(3,5,0), VDR(-1,4,0), VDR(11,13,0), VDR(1,7,0), VDR(2,3,0)],
    [VDR(7,13,0), VDR(3,5,0), VDR(-3,5,0), VDR(2,3,0), VDR(1,7,0)],
]
A5 = Mat(entries)
b5 = Vec([VDR(1,1,0)]*5)
x5_gauss = gaussian_solve(A5, b5)
x5_cramer = solve(A5, b5)
assert x5_gauss == x5_cramer
assert A5 @ x5_gauss == b5

# G24-10: Determinant sign tracking
A4 = Mat([
    [0, 0, 1, 2],
    [0, 3, 4, 0],
    [5, 6, 0, 0],
    [7, 0, 0, 8],
])
d_gauss = gaussian_det(A4)  # tracks (-1)^swaps × pivot product
d_cofactor = det(A4)
assert d_gauss == d_cofactor

# G24-11: LU consistency
P, L, U = gaussian_plu(A3)
assert P @ A3 == L @ U
# compare against gym 04 PLU
P4, L4, U4 = plu_decompose(A3)  # existing gym 04 path
assert P == P4
assert L == L4
assert U == U4

# G24-12: 30×30 Hilbert inverse
H30 = hilbert(30)
H30inv = gaussian_inverse(H30)
I30 = H30 @ H30inv
for i in range(30):
    assert I30[i][i] == VDR(1,1,0)
for i, j in [(0,1),(0,29),(5,17),(10,20),(14,15),(29,0),(7,22),(3,28),(19,11),(25,6)]:
    assert I30[i][j] == VDR(0,1,0)

# G24-13: Overdetermined least-squares setup
A43 = Mat([
    [VDR(1,1,0), VDR(2,1,0), VDR(3,1,0)],
    [VDR(4,1,0), VDR(5,1,0), VDR(6,1,0)],
    [VDR(7,1,0), VDR(8,1,0), VDR(10,1,0)],
    [VDR(1,1,0), VDR(0,1,0), VDR(1,1,0)],
])
b43 = Vec([VDR(1,1,0), VDR(2,1,0), VDR(3,1,0), VDR(1,1,0)])
AtA = A43.T @ A43
Atb = A43.T @ b43
x_ls = gaussian_solve(AtA, Atb)
assert AtA @ x_ls == Atb

# G24-14: Condition number irrelevance
H5 = hilbert(5)
b1 = Vec([VDR(1,1,0)]*5)
b2_entries = [VDR(1,1,0)]*5
b2_entries[0] = VDR(1,1,0) + VDR(1,10000000000,0)  # differ by 10^-10
b2 = Vec(b2_entries)
x1 = gaussian_solve(H5, b1)
x2 = gaussian_solve(H5, b2)
diff = x2 - x1
expected_diff = gaussian_solve(H5, b2 - b1)
assert diff == expected_diff  # exact, no amplification artifacts
assert H5 @ x1 == b1
assert H5 @ x2 == b2
```

