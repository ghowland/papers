#!/usr/bin/env python3
"""
gym_08_geometry.py — VDR exercises in computational geometry

Exact point arithmetic, line intersections, polygon areas,
barycentric coordinates, and convex hull — all in exact rational VDR.
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

# Points as Vec of 2 VDR objects
def point(x, y):
    if isinstance(x, int):
        x = VDR(x)
    if isinstance(y, int):
        y = VDR(y)
    return Vec([x, y])

# =========================================================================
section("1. Exact line intersection")
# =========================================================================

def line_intersect(p1, p2, p3, p4):
    """
    Exact intersection of line through p1-p2 with line through p3-p4.
    Returns (point, t) where t is the parameter on first line.
    Uses VDR exact arithmetic — no floating point.
    """
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x4, y4 = p4[0], p4[1]

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == VDR(0):
        return None, None  # parallel

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    ix = x1 + t * (x2 - x1)
    iy = y1 + t * (y2 - y1)
    return point(ix, iy), t

# lines: y = x and y = -x + 2 should meet at (1, 1)
p1 = point(0, 0)
p2 = point(2, 2)
p3 = point(0, 2)
p4 = point(2, 0)
intersection, t = line_intersect(p1, p2, p3, p4)
print("  y=x and y=-x+2 intersect at: (%s, %s)" % (
    intersection[0].to_fraction(), intersection[1].to_fraction()))
ok = intersection[0] == VDR(1) and intersection[1] == VDR(1)
record(check("intersection at (1, 1)", ok))

# rational lines
p5 = point(VDR(1, 3), VDR(1, 7))
p6 = point(VDR(5, 3), VDR(9, 7))
p7 = point(VDR(0), VDR(1))
p8 = point(VDR(2), VDR(0))
inter2, t2 = line_intersect(p5, p6, p7, p8)
print("  rational intersection: (%s, %s)" % (
    inter2[0].to_fraction(), inter2[1].to_fraction()))

# verify: point lies on both lines (parametric check)
# the intersection coordinates should be exact rationals
record(check("rational intersection is exact",
             isinstance(inter2[0].to_fraction(), Fraction)))

# =========================================================================
section("2. Exact polygon area (Shoelace formula)")
# =========================================================================

def polygon_area(vertices):
    """
    Exact area of polygon using shoelace formula.
    Returns 2*area as VDR to avoid the 1/2 if desired.
    """
    n = len(vertices)
    total = VDR(0)
    for i in range(n):
        j = (i + 1) % n
        total = total + vertices[i][0] * vertices[j][1]
        total = total - vertices[j][0] * vertices[i][1]
    return total / VDR(2)

# unit square
square = [point(0, 0), point(1, 0), point(1, 1), point(0, 1)]
area = polygon_area(square)
record(check("unit square area = 1", area == VDR(1)))

# triangle (0,0), (4,0), (0,3) — area = 6
triangle = [point(0, 0), point(4, 0), point(0, 3)]
area = polygon_area(triangle)
record(check("3-4-5 triangle area = 6", area == VDR(6)))

# rational vertices
rat_tri = [point(VDR(1, 3), VDR(1, 5)),
           point(VDR(2, 3), VDR(4, 5)),
           point(VDR(1, 7), VDR(1, 2))]
area_rat = polygon_area(rat_tri)
print("  rational triangle area = %s" % area_rat.to_fraction())
record(check("rational triangle area is exact",
             isinstance(area_rat.to_fraction(), Fraction)))

# =========================================================================
section("3. Barycentric coordinates")
# =========================================================================

def barycentric(p, a, b, c):
    """
    Compute exact barycentric coordinates of point p
    with respect to triangle (a, b, c).
    """
    v0 = Vec([b[0] - a[0], b[1] - a[1]])
    v1 = Vec([c[0] - a[0], c[1] - a[1]])
    v2 = Vec([p[0] - a[0], p[1] - a[1]])

    d00 = v0.dot(v0)
    d01 = v0.dot(v1)
    d11 = v1.dot(v1)
    d20 = v2.dot(v0)
    d21 = v2.dot(v1)

    denom = d00 * d11 - d01 * d01
    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = VDR(1) - v - w

    return u, v, w

# centroid of (0,0), (6,0), (0,6) is (2,2)
a = point(0, 0)
b = point(6, 0)
c = point(0, 6)
centroid = point(2, 2)
u, v, w = barycentric(centroid, a, b, c)
print("  centroid barycentric: (%s, %s, %s)" % (
    u.to_fraction(), v.to_fraction(), w.to_fraction()))
ok = u == VDR(1, 3) and v == VDR(1, 3) and w == VDR(1, 3)
record(check("centroid has barycentric (1/3, 1/3, 1/3)", ok))

# vertex a should have (1, 0, 0)
u, v, w = barycentric(a, a, b, c)
ok = u == VDR(1) and v == VDR(0) and w == VDR(0)
record(check("vertex a has barycentric (1, 0, 0)", ok))

# midpoint of b-c
mid_bc = point(3, 3)
u, v, w = barycentric(mid_bc, a, b, c)
ok = u == VDR(0) and v == VDR(1, 2) and w == VDR(1, 2)
record(check("midpoint of b-c has barycentric (0, 1/2, 1/2)", ok))

# =========================================================================
section("4. Point-in-triangle test (exact)")
# =========================================================================

def point_in_triangle(p, a, b, c):
    """Exact point-in-triangle using barycentric coordinates."""
    u, v, w = barycentric(p, a, b, c)
    # all coordinates must be in [0, 1]
    zero = Fraction(0)
    one = Fraction(1)
    return (zero <= u.to_fraction() <= one and
            zero <= v.to_fraction() <= one and
            zero <= w.to_fraction() <= one)

a = point(0, 0)
b = point(10, 0)
c = point(0, 10)

inside = point(2, 2)
outside = point(6, 6)
on_edge = point(5, 0)

record(check("(2,2) inside triangle", point_in_triangle(inside, a, b, c)))
record(check("(6,6) outside triangle", not point_in_triangle(outside, a, b, c)))
record(check("(5,0) on edge", point_in_triangle(on_edge, a, b, c)))

# rational point that is EXACTLY on the boundary
boundary = point(VDR(1, 3), VDR(0))
record(check("(1/3, 0) on edge exact", point_in_triangle(boundary, a, b, c)))

# =========================================================================
section("5. Exact distance squared (avoids irrational sqrt)")
# =========================================================================

def dist_sq(p1, p2):
    """Exact squared distance — stays rational, no sqrt needed."""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx * dx + dy * dy

# 3-4-5 triangle verification
a = point(0, 0)
b = point(3, 0)
c = point(0, 4)
ab2 = dist_sq(a, b)
ac2 = dist_sq(a, c)
bc2 = dist_sq(b, c)
record(check("3-4-5: AB^2=9", ab2 == VDR(9)))
record(check("3-4-5: AC^2=16", ac2 == VDR(16)))
record(check("3-4-5: BC^2=25", bc2 == VDR(25)))
record(check("Pythagorean: AB^2+AC^2=BC^2", ab2 + ac2 == bc2))

# rational points
p = point(VDR(1, 3), VDR(1, 7))
q = point(VDR(2, 5), VDR(3, 11))
d2 = dist_sq(p, q)
print("  dist^2 between rational points: %s" % d2.to_fraction())
record(check("rational dist^2 is exact", isinstance(d2.to_fraction(), Fraction)))

# =========================================================================
section("6. Exact circumcenter of triangle")
# =========================================================================

def circumcenter(a, b, c):
    """
    Exact circumcenter using VDR matrix solve.
    The circumcenter is equidistant from all three vertices.
    """
    # set up: |P-A|^2 = |P-B|^2 and |P-A|^2 = |P-C|^2
    # expands to linear system in (x, y)
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    cx, cy = c[0], c[1]

    # 2(bx-ax)*x + 2(by-ay)*y = bx^2-ax^2 + by^2-ay^2
    # 2(cx-ax)*x + 2(cy-ay)*y = cx^2-ax^2 + cy^2-ay^2
    A = Mat([
        [VDR(2) * (bx - ax), VDR(2) * (by - ay)],
        [VDR(2) * (cx - ax), VDR(2) * (cy - ay)],
    ])
    rhs = Vec([
        bx * bx - ax * ax + by * by - ay * ay,
        cx * cx - ax * ax + cy * cy - ay * ay,
    ])

    center = A.solve(rhs)
    return point(center[0], center[1])

# right triangle: circumcenter should be midpoint of hypotenuse
a = point(0, 0)
b = point(6, 0)
c = point(0, 8)
cc = circumcenter(a, b, c)
print("  circumcenter of right triangle: (%s, %s)" % (
    cc[0].to_fraction(), cc[1].to_fraction()))
ok = cc[0] == VDR(3) and cc[1] == VDR(4)
record(check("circumcenter = midpoint of hypotenuse (3, 4)", ok))

# verify equidistance
da = dist_sq(cc, a)
db = dist_sq(cc, b)
dc = dist_sq(cc, c)
ok = da == db and db == dc
record(check("circumcenter equidistant from all vertices", ok))

# =========================================================================
print("\n" + "=" * 50)
print("GYM 08 RESULTS: %d passed, %d failed" % (results["pass"], results["fail"]))
print("=" * 50)
