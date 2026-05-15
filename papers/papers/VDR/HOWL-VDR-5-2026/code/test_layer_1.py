"""
test_layer1.py — Tests for Layer 1: linalg, parse, serialize, export

Run:  python test_layer1.py
"""

from fractions import Fraction
import json

from vdr.vdr import VDR, Remainder
from vdr.linalg import (
    Vec, Mat, LinAlgError,
    parse_vdr, vdr_to_dict, vdr_from_dict, vdr_to_latex,
)
from vdr.export import to_decimal, to_float, to_fraction


def section(title):
    print("\n=== %s ===" % title)


# =========================================================================
section("1. Vec basics")
# =========================================================================

v = Vec([VDR(1, 2), VDR(1, 3), VDR(1, 7)])
w = Vec([VDR(1, 2), VDR(2, 3), VDR(6, 7)])
print("  v = %s" % v)
print("  w = %s" % w)

s = v + w
print("  v + w = %s" % s)
assert s[0] == VDR(1), "vec add [0]"
assert s[1] == VDR(1), "vec add [1]"
assert s[2] == VDR(1), "vec add [2]"

d = w - v
print("  w - v = %s" % d)
assert d[0] == VDR(0), "vec sub [0]"

neg = -v
print("  -v = %s" % neg)
assert neg[0] == VDR(-1, 2), "vec neg"

scaled = v * VDR(2)
print("  v * 2 = %s" % scaled)
assert scaled[0] == VDR(1), "vec scale"

dot = v.dot(w)
print("  v · w = %s  (= %s)" % (dot, dot.to_fraction()))

# from_ints
vi = Vec.from_ints([1, 2, 3])
assert vi[0] == VDR(1)
assert vi[2] == VDR(3)

# zero
z = Vec.zero(3)
assert v + z == v, "zero vec identity"

# =========================================================================
section("2. Mat basics")
# =========================================================================

m = Mat.from_ints([[1, 2], [3, 4]])
print("  m =")
print(m.pretty())

assert m.shape == (2, 2)
assert m[0, 0] == VDR(1)
assert m[1, 1] == VDR(4)

# identity
I = Mat.identity(2)
print("  I =")
print(I.pretty())
assert m * I == m, "identity multiplication"
assert I * m == m, "identity multiplication"

# transpose
mt = m.T
print("  m^T =")
print(mt.pretty())
assert mt[0, 1] == VDR(3)
assert mt[1, 0] == VDR(2)

# =========================================================================
section("3. Mat arithmetic")
# =========================================================================

a = Mat.from_ints([[1, 2], [3, 4]])
b = Mat.from_ints([[5, 6], [7, 8]])

s = a + b
print("  a + b =")
print(s.pretty())
assert s[0, 0] == VDR(6)
assert s[1, 1] == VDR(12)

d = b - a
print("  b - a =")
print(d.pretty())
assert d[0, 0] == VDR(4)

p = a * b
print("  a * b =")
print(p.pretty())
# [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]] = [[19,22],[43,50]]
assert p[0, 0] == VDR(19)
assert p[0, 1] == VDR(22)
assert p[1, 0] == VDR(43)
assert p[1, 1] == VDR(50)

# scalar mult
s2 = a * VDR(1, 2)
print("  a * 1/2 =")
print(s2.pretty())
assert s2[0, 0] == VDR(1, 2)

# =========================================================================
section("4. Determinant")
# =========================================================================

m2 = Mat.from_ints([[1, 2], [3, 4]])
det2 = m2.det()
print("  det([[1,2],[3,4]]) = %s" % det2)
assert det2 == VDR(-2), "2x2 det"

m3 = Mat.from_ints([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
det3 = m3.det()
print("  det(3x3) = %s" % det3)
assert det3 == VDR(-3), "3x3 det"

# singular
sing = Mat.from_ints([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dets = sing.det()
print("  det(singular) = %s" % dets)
assert dets == VDR(0), "singular det"

# =========================================================================
section("5. Trace")
# =========================================================================

tr = m3.trace()
print("  trace(3x3) = %s" % tr)
assert tr == VDR(16), "trace"

# =========================================================================
section("6. Inverse")
# =========================================================================

m2 = Mat.from_ints([[1, 2], [3, 4]])
m2i = m2.inv()
print("  inv([[1,2],[3,4]]) =")
print(m2i.pretty())

# verify: m * m^-1 = I
product = m2 * m2i
print("  m * m^-1 =")
print(product.pretty())
assert product == Mat.identity(2), "m * m^-1 should be identity"

# rational matrix inverse
mr = Mat([
    [VDR(1, 2), VDR(1, 3)],
    [VDR(1, 4), VDR(1, 5)],
])
mri = mr.inv()
print("  inv(rational mat) =")
print(mri.pretty())
check = mr * mri
assert check == Mat.identity(2), "rational inverse check"

# 3x3
m3i = m3.inv()
check3 = m3 * m3i
print("  3x3 * inv(3x3) = I? %s" % (check3 == Mat.identity(3)))
assert check3 == Mat.identity(3), "3x3 inverse"

# =========================================================================
section("7. Solve (Cramer)")
# =========================================================================

# Solve: [[2,1],[5,3]] x = [4, 7]
A = Mat.from_ints([[2, 1], [5, 3]])
b_vec = Vec.from_ints([4, 7])
x = A.solve(b_vec)
print("  solution: %s" % x)
# x = [5, -6]
assert x[0] == VDR(5), "solve x[0]"
assert x[1] == VDR(-6), "solve x[1]"

# verify
check = A * x
print("  A*x = %s (should be %s)" % (check, b_vec))
assert check == b_vec, "Ax = b check"

# rational system
Ar = Mat([
    [VDR(1, 2), VDR(1, 3)],
    [VDR(1, 4), VDR(1, 5)],
])
br = Vec([VDR(1), VDR(1)])
xr = Ar.solve(br)
print("  rational solve: %s" % xr)
checkr = Ar * xr
print("  A*x = %s (should be %s)" % (checkr, br))
assert checkr == br, "rational solve check"

# =========================================================================
section("8. Rank")
# =========================================================================

full = Mat.from_ints([[1, 0], [0, 1]])
print("  rank(I2) = %d" % full.rank())
assert full.rank() == 2

deficient = Mat.from_ints([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("  rank(singular 3x3) = %d" % deficient.rank())
assert deficient.rank() == 2

# =========================================================================
section("9. Matrix-vector product")
# =========================================================================

m = Mat.from_ints([[1, 2], [3, 4]])
v = Vec.from_ints([5, 6])
result = m * v
print("  [[1,2],[3,4]] * [5,6] = %s" % result)
assert result[0] == VDR(17), "matvec [0]"
assert result[1] == VDR(39), "matvec [1]"

# =========================================================================
section("10. Parse bracket notation")
# =========================================================================

tests = [
    ("[1, 2, 0]", VDR(1, 2)),
    ("[5, 1, 0]", VDR(5)),
    ("[-3, 4, 0]", VDR(-3, 4)),
    ("[1, 2, 3]", VDR(1, 2, 3)),
    ("[1, 3, [1, 6, 0]]", VDR(1, 3, Remainder(0, [VDR(1, 6)]))),
]

for text, expected in tests:
    parsed = parse_vdr(text)
    ok = parsed.structural_eq(expected)
    print("  parse('%s') → %s  %s" % (text, parsed, "OK" if ok else "FAIL"))
    assert ok, "parse failed for %s: got %s expected %s" % (text, parsed, expected)

# nested
nested = parse_vdr("[2, 5, 1 + [1, 3, 0] + [1, 7, 0]]")
print("  parse nested: %s" % nested)
assert nested.v == 2
assert nested.d == 5
assert nested.r.base == 1
assert len(nested.r.children) == 2

# =========================================================================
section("11. JSON serialization roundtrip")
# =========================================================================

cases = [
    VDR(1, 2),
    VDR(3, 7, 1),
    VDR(1, 3, Remainder(0, [VDR(1, 6)])),
    VDR(2, 5, Remainder(1, [VDR(1, 3), VDR(1, 7)])),
]

for x in cases:
    d = vdr_to_dict(x)
    j = json.dumps(d)
    back = vdr_from_dict(json.loads(j))
    ok = x.structural_eq(back)
    print("  %s → JSON → %s  %s" % (x, back, "OK" if ok else "FAIL"))
    assert ok, "roundtrip failed for %s" % x

# =========================================================================
section("12. LaTeX export")
# =========================================================================

cases_latex = [
    (VDR(1, 2), "\\frac{1}{2}"),
    (VDR(5), "5"),
    (VDR(-3, 4), "\\frac{-3}{4}"),
]

for x, expected in cases_latex:
    result = vdr_to_latex(x)
    ok = result == expected
    print("  %s → %s  %s" % (x, result, "OK" if ok else "FAIL (expected %s)" % expected))
    assert ok, "latex failed"

# active latex
active_latex = vdr_to_latex(VDR(1, 3, Remainder(0, [VDR(1, 6)])))
print("  active: %s" % active_latex)

# =========================================================================
section("13. Export boundary")
# =========================================================================

x = VDR(1, 7)
f = to_fraction(x)
print("  to_fraction(1/7) = %s" % f)
assert f == Fraction(1, 7)

fl = to_float(x)
print("  to_float(1/7) = %s" % fl)

dec = to_decimal(x, 30)
print("  to_decimal(1/7, 30) = %s" % dec)
assert dec.startswith("0.142857142857"), "decimal export"

# large precision
dec100 = to_decimal(VDR(1, 3), 100)
print("  to_decimal(1/3, 100) = %s..." % dec100[:40])
assert "3" * 20 in dec100, "repeating decimal"

# =========================================================================
section("14. Exact rational linear algebra stress test")
# =========================================================================

# Hilbert matrix — notoriously ill-conditioned for floats
# H[i,j] = 1/(i+j+1) for 0-indexed
n = 4
H = Mat([
    [VDR(1, i + j + 1) for j in range(n)]
    for i in range(n)
])
print("  Hilbert(%d) =" % n)
print(H.pretty())

detH = H.det()
print("  det(H4) = %s = %s" % (detH, detH.to_fraction()))

# H * H^-1 must be exactly I, no drift
Hi = H.inv()
product = H * Hi
print("  H4 * inv(H4) = I? %s" % (product == Mat.identity(n)))
assert product == Mat.identity(n), \
    "Hilbert matrix inverse MUST be exact — this is the VDR advantage"

# now do the same thing a float system cannot:
# invert, re-invert, and get back exactly
Hi2 = Hi.inv()
print("  inv(inv(H4)) == H4? %s" % (Hi2 == H))
assert Hi2 == H, "double inverse must recover exactly"

# =========================================================================
section("15. Long-chain matrix roundtrip")
# =========================================================================

A = Mat([
    [VDR(3, 7), VDR(1, 13)],
    [VDR(5, 11), VDR(2, 3)],
])
original = A

# multiply by B and then by B^-1, twenty times
B = Mat([
    [VDR(7, 3), VDR(2, 5)],
    [VDR(1, 9), VDR(4, 7)],
])
Bi = B.inv()

current = A
for _ in range(20):
    current = current * B
    current = current * Bi

print("  after 40 matrix ops: %s" % (current == original))
assert current == original, "matrix roundtrip drift detected"
print("  zero matrix drift after 40 operations: PASS")


# =========================================================================
print("\n" + "=" * 50)
print("ALL LAYER 1 TESTS PASSED")
print("=" * 50)