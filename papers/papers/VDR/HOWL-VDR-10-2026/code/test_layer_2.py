"""
test_layer_2.py — Tests for Layer 2: active multiplication and division

Run:  python test_layer_2.py
"""

from fractions import Fraction
from vdr.vdr import VDR, Remainder
from vdr.linalg import Vec, Mat
import vdr.active_mul

# ensure installed
vdr.active_mul.install()


def section(title):
    print("\n=== %s ===" % title)

def show(label, x):
    print("  %-24s  %s   (projects to %s)" % (label, x, x.to_fraction()))

def check_projection(label, result, expected_frac):
    got = result.to_fraction()
    ok = got == expected_frac
    status = "OK" if ok else "FAIL (got %s)" % got
    print("  %-24s  %s  projection=%s  %s" % (label, result, got, status))
    assert ok, "%s: expected %s got %s" % (label, expected_frac, got)


# =========================================================================
section("1. Closed multiplication (unchanged)")
# =========================================================================

a = VDR(2, 3)
b = VDR(3, 5)
r = a * b
check_projection("(2/3)*(3/5)", r, Fraction(2, 5))

a = VDR(7, 11)
b = VDR(13, 17)
r = a * b
check_projection("(7/11)*(13/17)", r, Fraction(91, 187))

# =========================================================================
section("2. Closed division (unchanged)")
# =========================================================================

a = VDR(2, 3)
b = VDR(4, 5)
r = a / b
check_projection("(2/3)/(4/5)", r, Fraction(5, 6))

# division by integer
r2 = VDR(6, 7) / 3
check_projection("(6/7)/3", r2, Fraction(2, 7))

# =========================================================================
section("3. Active × closed")
# =========================================================================

# [2, 5, 1] × [3, 1, 0]
# projection: (2+1)/5 × 3 = 3/5 × 3 = 9/5
a = VDR(2, 5, 1)
b = VDR(3)
r = a * b
check_projection("[2,5,1] * 3", r, Fraction(9, 5))

# [1, 3, [1, 6, 0]] × [2, 1, 0]
# projection: (1 + 1/6)/3 × 2 = (7/6)/3 × 2 = 7/9
a = VDR(1, 3, Remainder(0, [VDR(1, 6)]))
b = VDR(2)
r = a * b
check_projection("[1,3,[1,6,0]] * 2", r, Fraction(7, 9))

# =========================================================================
section("4. Closed × active")
# =========================================================================

# commutative check
a = VDR(3)
b = VDR(2, 5, 1)
r = a * b
check_projection("3 * [2,5,1]", r, Fraction(9, 5))

# =========================================================================
section("5. Active × active (atomic remainders)")
# =========================================================================

# [2, 5, 1] × [3, 7, -1]
# proj: (2+1)/5 × (3-1)/7 = 3/5 × 2/7 = 6/35
a = VDR(2, 5, 1)
b = VDR(3, 7, -1)
r = a * b
check_projection("[2,5,1] * [3,7,-1]", r, Fraction(6, 35))

# [1, 2, 1] × [1, 3, 1]
# proj: (1+1)/2 × (1+1)/3 = 1 × 2/3 = 2/3
a = VDR(1, 2, 1)
b = VDR(1, 3, 1)
r = a * b
check_projection("[1,2,1] * [1,3,1]", r, Fraction(2, 3))

# =========================================================================
section("6. Active × active (nested remainders)")
# =========================================================================

# [1, 2, [1, 3, 0]] × [1, 4, [1, 5, 0]]
# proj: (1 + 1/3)/2 × (1 + 1/5)/4 = (4/3)/2 × (6/5)/4 = 2/3 × 3/10 = 1/5
a = VDR(1, 2, Remainder(0, [VDR(1, 3)]))
b = VDR(1, 4, Remainder(0, [VDR(1, 5)]))
r = a * b
check_projection("nested * nested", r, Fraction(1, 5))

# =========================================================================
section("7. Division: active / closed")
# =========================================================================

a = VDR(2, 5, 1)
b = VDR(3, 7)
r = a / b
# proj: (3/5) / (3/7) = (3/5)(7/3) = 7/5
check_projection("[2,5,1] / (3/7)", r, Fraction(7, 5))

# =========================================================================
section("8. Division: closed / active")
# =========================================================================

a = VDR(1, 2)
b = VDR(1, 3, 1)
# proj: (1/2) / ((1+1)/3) = (1/2) / (2/3) = 3/4
r = a / b
check_projection("(1/2) / [1,3,1]", r, Fraction(3, 4))

# =========================================================================
section("9. Division: active / active")
# =========================================================================

a = VDR(2, 5, 1)
b = VDR(1, 3, 1)
# proj: (3/5) / (2/3) = 9/10
r = a / b
check_projection("[2,5,1] / [1,3,1]", r, Fraction(9, 10))

# =========================================================================
section("10. Division by zero checks")
# =========================================================================

import sys

# closed zero
try:
    VDR(1, 2) / VDR(0)
    assert False, "should have raised"
except Exception as e:
    print("  closed zero div: raised %s" % e)

# active projecting to zero: [1, 2, -1] projects to (1-1)/2 = 0
try:
    VDR(1) / VDR(1, 2, -1)
    assert False, "should have raised"
except Exception as e:
    print("  active zero div:  raised %s" % e)

# =========================================================================
section("11. Multiplicative identity and inverse")
# =========================================================================

one = VDR(1)
a = VDR(2, 5, 1)
show("a", a)
show("a * 1", a * one)
assert (a * one).to_fraction() == a.to_fraction(), "mul identity"

# a * (1/a) should project to 1
a_frac = a.to_fraction()
a_inv = VDR(a_frac.denominator, a_frac.numerator)
prod = a * a_inv
check_projection("a * (1/a)", prod, Fraction(1))

# =========================================================================
section("12. Commutativity check")
# =========================================================================

pairs = [
    (VDR(2, 5, 1), VDR(3, 7, -1)),
    (VDR(1, 2, Remainder(0, [VDR(1, 3)])), VDR(4, 5)),
    (VDR(1, 3, 2), VDR(2, 7, -3)),
]

for a, b in pairs:
    ab = a * b
    ba = b * a
    ok = ab.to_fraction() == ba.to_fraction()
    print("  %s * %s: a*b=%s  b*a=%s  commutative=%s" % (
        a, b, ab.to_fraction(), ba.to_fraction(), ok
    ))
    assert ok, "commutativity failed"

# =========================================================================
section("13. Associativity check")
# =========================================================================

a = VDR(1, 2, 1)
b = VDR(2, 3, -1)
c = VDR(3, 5, 2)

ab_c = (a * b) * c
a_bc = a * (b * c)
ok = ab_c.to_fraction() == a_bc.to_fraction()
print("  (a*b)*c proj: %s" % ab_c.to_fraction())
print("  a*(b*c) proj: %s" % a_bc.to_fraction())
print("  associative: %s" % ok)
assert ok, "associativity failed"

# =========================================================================
section("14. Distributivity check")
# =========================================================================

a = VDR(1, 2, 1)
b = VDR(2, 3, -1)
c = VDR(3, 5, 2)

lhs = a * (b + c)
rhs = (a * b) + (a * c)
ok = lhs.to_fraction() == rhs.to_fraction()
print("  a*(b+c) proj: %s" % lhs.to_fraction())
print("  a*b+a*c proj: %s" % rhs.to_fraction())
print("  distributive: %s" % ok)
assert ok, "distributivity failed"

# =========================================================================
section("15. Active multiply/divide roundtrip")
# =========================================================================

x = VDR(3, 7, 2)
show("start", x)

y = x * VDR(5, 11, -1)
show("* [5,11,-1]", y)

z = y / VDR(5, 11, -1)
show("/ [5,11,-1]", z)

ok = z.to_fraction() == x.to_fraction()
print("  roundtrip preserves value: %s" % ok)
assert ok, "active mul/div roundtrip failed"

# =========================================================================
section("16. Active multiplication long chain")
# =========================================================================

x = VDR(1, 3, 1)
original_frac = x.to_fraction()

factor = VDR(2, 7, -1)
factor_frac = factor.to_fraction()

current = x
for _ in range(20):
    current = current * factor
for _ in range(20):
    current = current / factor

final_frac = current.to_fraction()
ok = final_frac == original_frac
print("  start:    %s" % original_frac)
print("  after 40: %s" % final_frac)
print("  exact:    %s" % ok)
assert ok, "long chain active mul/div drift"

# =========================================================================
section("17. Matrix with active entries")
# =========================================================================

# Now that active mul works, matrices with active entries should work
m = Mat([
    [VDR(1, 2, 1), VDR(1, 3)],
    [VDR(2, 5),    VDR(1, 7, -1)],
])
print("  active matrix:")
print(m.pretty())

det = m.det()
show("det", det)
expected_det = (
    m[0,0].to_fraction() * m[1,1].to_fraction()
    - m[0,1].to_fraction() * m[1,0].to_fraction()
)
assert det.to_fraction() == expected_det, "active matrix det"

# identity check
I = Mat.identity(2)
mI = m * I
Im = I * m
print("  m*I == m: %s" % (mI.to_fractions() == m.to_fractions()))
print("  I*m == m: %s" % (Im.to_fractions() == m.to_fractions()))

# =========================================================================
section("18. Mixed active/closed matrix multiply")
# =========================================================================

A = Mat([
    [VDR(1, 2, 1), VDR(1, 3)],
    [VDR(0),       VDR(1)],
])
B = Mat([
    [VDR(2), VDR(0)],
    [VDR(1, 5), VDR(3, 7, -1)],
])

C = A * B
print("  A*B =")
print(C.pretty())

# verify by projection
for i in range(2):
    for j in range(2):
        expected = Fraction(0)
        for k in range(2):
            expected += A[i,k].to_fraction() * B[k,j].to_fraction()
        got = C[i,j].to_fraction()
        assert got == expected, \
            "matrix mul [%d,%d]: expected %s got %s" % (i, j, expected, got)
print("  projection-verified: all entries match")

# =========================================================================
section("19. Scalar multiplication with active VDR")
# =========================================================================

v = Vec([VDR(1, 2), VDR(1, 3)])
s = VDR(2, 5, 1)  # active scalar
result = v * s
print("  [1/2, 1/3] * [2,5,1] = %s" % result)
for i in range(len(v)):
    expected = v[i].to_fraction() * s.to_fraction()
    got = result[i].to_fraction()
    assert got == expected, "scalar vec mul [%d]" % i
print("  projection-verified")

# =========================================================================
section("20. Int and Fraction interop with active mul")
# =========================================================================

a = VDR(2, 5, 1)

r1 = a * 3
check_projection("[2,5,1] * 3", r1, a.to_fraction() * 3)

r2 = 3 * a
check_projection("3 * [2,5,1]", r2, 3 * a.to_fraction())

r3 = a * Fraction(2, 7)
check_projection("[2,5,1] * 2/7", r3, a.to_fraction() * Fraction(2, 7))

r4 = a / 5
check_projection("[2,5,1] / 5", r4, a.to_fraction() / 5)

r5 = 1 / a
check_projection("1 / [2,5,1]", r5, Fraction(1) / a.to_fraction())


# =========================================================================
print("\n" + "=" * 50)
print("ALL LAYER 2 TESTS PASSED")
print("=" * 50)
