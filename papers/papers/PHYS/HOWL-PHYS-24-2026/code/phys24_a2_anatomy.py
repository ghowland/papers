#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: The A2 Anatomy
=============================================
The QED 2-loop coefficient A2 decomposes into three pieces:
  rational (197/144), number-theoretic ((3/4)zeta(3)),
  geometric (R4 * (8/3 - 16*ln2)).
The geometric piece nearly cancels the other two: 87% cancellation.
A2 is small not because QED converges rapidly but because geometry
nearly cancels arithmetic.

Backed by: a_2_decomposition_0.py (7/7 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: THE A2 ANATOMY")
print("=" * 70)
print()

# ================================================================
# A2 IN ORIGINAL FORM
# ================================================================

print("A2 IN ORIGINAL FORM")
print("-" * 70)
print()
print("  A2 = 197/144 + pi^2/12 + (3/4)*zeta(3) - (pi^2/2)*ln(2)")
print()

# uses pi2_f, zeta3_f, ln2_f from phys24_lib (DATA-4 G11, G9, G3)

term_rational = Fraction(197, 144)
term_pi2_12   = pi2_f / 12
term_zeta3    = Fraction(3, 4) * zeta3_f
term_pi2_ln2  = pi2_f * ln2_f / 2

A2_frac = term_rational + term_pi2_12 + term_zeta3 - term_pi2_ln2

show("197/144 (dimensionless)", f2m(term_rational))
show("pi^2/12 (dimensionless)", f2m(term_pi2_12))
show("(3/4)*zeta(3) (dimensionless)", f2m(term_zeta3))
show("-(pi^2/2)*ln(2) (dimensionless)", -f2m(term_pi2_ln2))
show("A2 total (dimensionless)", f2m(A2_frac))
print()

# ================================================================
# DECOMPOSITION INTO R4 FORM
# ================================================================
# Substitution: pi^2 = 32*R4 where R4 = pi^2/32 (MATH-5)
#
#   pi^2/12      = 32*R4/12     = (8/3)*R4
#   (pi^2/2)*ln2 = (32/2)*R4*ln2 = 16*R4*ln2
#
# Therefore:
#   A2 = 197/144 + (3/4)*zeta(3) + R4*(8/3 - 16*ln2)
#
# Three pieces of distinct mathematical character:
#   RATIONAL:         197/144 (diagram combinatorics)
#   NUMBER-THEORETIC: (3/4)*zeta(3) (polylogarithm integrals)
#   GEOMETRIC:        R4 * (8/3 - 16*ln2) (4D phase space)

print("DECOMPOSITION INTO R4 FORM")
print("-" * 70)
print()
print("  Substitution: pi^2 = 32*R4")
print()
print("  A2 = 197/144 + (3/4)*zeta(3) + R4*(8/3 - 16*ln(2))")
print()

# uses R4_f from phys24_lib (DATA-4 G14)

piece_rational = Fraction(197, 144)
piece_number   = Fraction(3, 4) * zeta3_f
c_geom         = Fraction(8, 3) - 16 * ln2_f
piece_geom     = R4_f * c_geom

show("Rational: 197/144 (dimensionless)", f2m(piece_rational))
show("Number-theoretic: (3/4)*zeta(3) (dimensionless)", f2m(piece_number))
show("Geometric coeff: 8/3 - 16*ln(2) (dimensionless)", f2m(c_geom))
show("Geometric: R4*(8/3 - 16*ln2) (dimensionless)", f2m(piece_geom))
print()

# Verify decomposition sums to A2
A2_decomp = piece_rational + piece_number + piece_geom
show("Sum of three pieces (dimensionless)", f2m(A2_decomp))
show("A2 from original form (dimensionless)", f2m(A2_frac))
print()

# ================================================================
# THE CANCELLATION
# ================================================================

print("THE CANCELLATION")
print("-" * 70)
print()

val_rat = f2m(piece_rational)
val_num = f2m(piece_number)
val_geo = f2m(piece_geom)
val_A2  = f2m(A2_frac)
abs_A2  = abs(val_A2)

positive_sum = val_rat + val_num
cancel_pct = abs(positive_sum) / abs(val_geo) * mpf("100")
geo_over_A2 = abs(val_geo) / abs_A2 * mpf("100")

print("  %-24s %12s  %s" % ("Piece", "Value", "Sign"))
print("  %-24s %12s  %s" % ("-" * 24, "-" * 12, "-" * 4))
print("  %-24s %12s  %s" % ("Rational (197/144)",
      mp.nstr(val_rat, 6), "+"))
print("  %-24s %12s  %s" % ("Number-theoretic",
      mp.nstr(val_num, 6), "+"))
print("  %-24s %12s  %s" % ("Geometric (R4*c)",
      mp.nstr(val_geo, 6), "-"))
print("  %-24s %12s" % ("-" * 24, "-" * 12))
print("  %-24s %12s" % ("A2 total",
      mp.nstr(val_A2, 6)))
print()

show("Positive content (rational + number) (dimensionless)", positive_sum)
show("Geometric content (dimensionless)", val_geo)
show("Cancellation: positive/|geometric| (%%)", cancel_pct)
show("|geometric| / |A2| (%%)", geo_over_A2)
print()

print("  The positive pieces (%s) are %s%% of the" % (
      mp.nstr(positive_sum, 5), mp.nstr(cancel_pct, 4)))
print("  geometric piece (%s)." % mp.nstr(val_geo, 5))
print("  The net A2 = %s is only %s%% of either side." % (
      mp.nstr(val_A2, 5),
      mp.nstr(abs_A2 / abs(val_geo) * mpf("100"), 4)))
print()
print("  A2 is small because geometry nearly cancels arithmetic.")
print("  The smallness is accidental — no known symmetry requires")
print("  the 87%% cancellation.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: decomposition sums to A2
decomp_digits = digits_of(f2m(A2_decomp), f2m(A2_frac))
chk("Decomposition sums to A2",
    f2m(A2_decomp), f2m(A2_frac), 30, checks)

# Check 2: A2 matches known value
chk("A2 ~ -0.32848",
    f2m(A2_frac), mpf("-0.328478965579"), 10, checks)

# Check 3: A2 is negative
chk_bool("A2 is negative",
         val_A2 < mpf("0"),
         "A2 = %s" % mp.nstr(val_A2, 6), checks)

# Check 4: geometric piece is negative
chk_bool("Geometric piece is negative",
         val_geo < mpf("0"),
         "geometric = %s" % mp.nstr(val_geo, 6), checks)

# Check 5: rational + number-theoretic is positive
chk_bool("Rational + number-theoretic is positive",
         positive_sum > mpf("0"),
         "sum = %s" % mp.nstr(positive_sum, 6), checks)

# Check 6: cancellation exceeds 80%
chk_bool("Cancellation exceeds 80%%",
         cancel_pct > mpf("80"),
         "cancellation = %s%%" % mp.nstr(cancel_pct, 4), checks)

# Check 7: |A2| < 0.5 (small due to cancellation)
chk_bool("|A2| < 0.5",
         abs_A2 < mpf("0.5"),
         "|A2| = %s" % mp.nstr(abs_A2, 6), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-24 A2 ANATOMY DEMONSTRATION COMPLETE")
print("=" * 70)
