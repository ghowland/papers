"""
test_basic.py — minimal VDR exercise

Run:  python test_basic.py
"""

from fractions import Fraction
from vdr.vdr import VDR, Remainder

def show(label, x):
    print("  %-12s  %s   (projects to %s)" % (label, x, x.to_fraction()))

def section(title):
    print("\n=== %s ===" % title)


# -------------------------------------------------------------------------
section("1. Construction")
# -------------------------------------------------------------------------

a = VDR(1, 2)          # 1/2
b = VDR(1, 3)          # 1/3
c = VDR(5)             # integer 5
d = VDR.from_fraction(Fraction(7, 11))

show("a = 1/2", a)
show("b = 1/3", b)
show("c = 5", c)
show("d = 7/11", d)

# -------------------------------------------------------------------------
section("2. Closed arithmetic")
# -------------------------------------------------------------------------

s = a + b
show("a + b", s)
assert s == VDR(5, 6), "addition failed"

diff = a - b
show("a - b", diff)
assert diff == VDR(1, 6), "subtraction failed"

prod = a * b
show("a * b", prod)
assert prod == VDR(1, 6), "multiplication failed"

quot = a / b
show("a / b", quot)
assert quot == VDR(3, 2), "division failed"

neg = -a
show("-a", neg)
assert neg == VDR(-1, 2), "negation failed"

# -------------------------------------------------------------------------
section("3. Normalization and equality")
# -------------------------------------------------------------------------

raw = VDR(2, 4)
normed = raw.normalize()
show("raw [2,4,0]", raw)
show("normalized", normed)
assert raw == a, "value equality failed: [2,4,0] should equal [1,2,0]"
assert not raw.structural_eq(a), "structural eq should fail"
print("  [2,4,0] == [1,2,0]? %s (value eq)" % (raw == a))
print("  [2,4,0] ≡ₛ [1,2,0]? %s (structural eq)" % raw.structural_eq(a))

neg_denom = VDR(1, -2)
show("[1,-2,0]", neg_denom)
show("normalized", neg_denom.normalize())
assert neg_denom == VDR(-1, 2), "sign normalization failed"

# -------------------------------------------------------------------------
section("4. Return-to-origin (equality recovery)")
# -------------------------------------------------------------------------

x = VDR(3, 7)
show("start", x)

y = x + VDR(5, 13)
show("+5/13", y)

z = y - VDR(5, 13)
show("-5/13", z)

assert z == x, "return-to-origin failed: exact equality not recovered"
print("  recovered: %s == %s? %s" % (z, x, z == x))

# -------------------------------------------------------------------------
section("5. Multiply/divide roundtrip")
# -------------------------------------------------------------------------

x = VDR(3, 7)
show("start", x)

y = x * VDR(11, 3)
show("*11/3", y)

z = y / VDR(11, 3)
show("/11/3", z)

assert z == x, "mul/div roundtrip failed"
print("  recovered: %s" % (z == x))

# -------------------------------------------------------------------------
section("6. Closed rebase")
# -------------------------------------------------------------------------

x = VDR(1, 2)
show("start", x)

r4 = x.rebase(4)
show("rebase→4", r4)
assert r4 == x, "rebase should preserve value"

r6 = x.rebase(6)
show("rebase→6", r6)
assert r6 == x, "rebase should preserve value"

# -------------------------------------------------------------------------
section("7. Active rebase (closed source, incompatible target)")
# -------------------------------------------------------------------------

x = VDR(1, 2)
show("start", x)

r3 = x.rebase(3)
show("rebase→3", r3)
print("  projects to: %s" % r3.to_fraction())
assert r3.to_fraction() == Fraction(1, 2), \
    "active rebase must preserve projected value"
print("  depth: %d  size: %d  den_complexity: %s" % (
    r3.depth(), r3.size(), r3.den_complexity()
))

# -------------------------------------------------------------------------
section("8. Active object construction")
# -------------------------------------------------------------------------

# [2, 5, 1] — active object, not equal to [3, 5, 0]
active = VDR(2, 5, 1)
closed = VDR(3, 5)
show("[2,5,1]", active)
show("[3,5,0]", closed)
print("  [2,5,1] == [3,5,0]? %s (Path B: must be False)" % (active == closed))
assert active != closed, "Path B: active != closed with same scalar image"

# -------------------------------------------------------------------------
section("9. Active same-frame addition")
# -------------------------------------------------------------------------

p = VDR(2, 5, 1)
q = VDR(3, 5, -1)
show("p", p)
show("q", q)

r = p + q
show("p + q", r)
print("  result is closed: %s" % r.is_closed)
assert r.is_closed, "active cancellation should produce closed result"

# -------------------------------------------------------------------------
section("10. Lift")
# -------------------------------------------------------------------------

r0 = Remainder(1)
print("  lift(1, 3) = %s" % r0.lift(3))
assert r0.lift(3) == Remainder(3)

child = VDR(1, 3)
lifted = child._lift_vdr(2)
show("lift([1,3,0], 2)", lifted)
assert lifted.v == 2 and lifted.d == 3, "lift should scale V, preserve D"

# -------------------------------------------------------------------------
section("11. Interop with Fraction")
# -------------------------------------------------------------------------

f = Fraction(22, 7)
x = VDR.from_fraction(f)
show("from 22/7", x)
assert x.to_fraction() == f, "roundtrip through Fraction failed"

# mix VDR and int
y = x + 1
show("22/7 + 1", y)
assert y.to_fraction() == Fraction(29, 7)

# -------------------------------------------------------------------------
section("12. Long chain drift test")
# -------------------------------------------------------------------------

x = VDR(1, 7)
original = x.to_fraction()

# add 1/13 one hundred times, then subtract it one hundred times
step = VDR(1, 13)
for _ in range(100):
    x = x + step
for _ in range(100):
    x = x - step

show("after 200 ops", x)
assert x.to_fraction() == original, \
    "drift detected after long chain: %s != %s" % (x.to_fraction(), original)
print("  zero drift after 200 operations: PASS")

# -------------------------------------------------------------------------
print("\n" + "=" * 50)
print("ALL TESTS PASSED")
print("=" * 50)
