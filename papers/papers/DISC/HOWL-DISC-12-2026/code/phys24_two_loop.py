#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: Two-Loop Unification
==================================================
Two-loop corrections improve the Cabibbo Doublet unification miss
from Delta = -1.17 (one-loop) to Delta = -0.40 (two-loop), a 66%
improvement. The residual is within standard GUT threshold range.

This script displays the two-loop b_ij matrix and presents the
verified results from unification_test.py. It does NOT reimplement
the ODE solver — the numerical integration is in the Session 3
script which passes 6/6 checks.

Backed by: unification_test.py (6/6 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: TWO-LOOP UNIFICATION")
print("=" * 70)
print()

# ================================================================
# THE ONE-LOOP RUNNING EQUATION
# ================================================================

print("THE RUNNING EQUATIONS (Level 1)")
print("-" * 70)
print()
print("  One-loop:")
print("    d(1/alpha_i)/d(ln mu) = -b_i / (2*pi)")
print()
print("  Two-loop:")
print("    d(1/alpha_i)/d(ln mu) = -b_i / (2*pi)")
print("                            - sum_j b_ij * alpha_j / (8*pi^2)")
print()
print("  The one-loop slopes are exact rationals (the b_i).")
print("  The two-loop curvatures are exact rationals (the b_ij).")
print("  Both are Level 1: determined by the gauge group and")
print("  particle content, not by any measurement.")
print()

# ================================================================
# SM BETA COEFFICIENTS (one-loop, recap)
# ================================================================

print("SM ONE-LOOP BETAS (Level 1, exact)")
print("-" * 70)
print()

# uses b1_SM, b2_SM, b3_SM from phys24_lib (DATA-4 N1-N3)
show("b_1 = %s" % b1_SM, f2m(b1_SM))
show("b_2 = %s" % b2_SM, f2m(b2_SM))
show("b_3 = %s" % b3_SM, f2m(b3_SM))
print()

# ================================================================
# TWO-LOOP b_ij MATRIX
# ================================================================

print("TWO-LOOP b_ij MATRIX (Level 1, exact)")
print("-" * 70)
print()
print("  From Machacek-Vaughn (1983), Luo-Xiao (hep-ph/0207271).")
print("  All entries are exact Fractions. Convention:")
print("    d(1/a_i)/d(ln mu) includes -sum_j b_ij * a_j / (8*pi^2)")
print()

# uses b_ij_SM from phys24_lib (DATA-4 N14)
labels = ["U(1)", "SU(2)", "SU(3)"]

print("           %10s %10s %10s" % (labels[0], labels[1], labels[2]))
print("           %10s %10s %10s" % ("-" * 10, "-" * 10, "-" * 10))

for i in range(3):
    row_strs = []
    for j in range(3):
        row_strs.append("%10s" % str(b_ij_SM[i][j]))
    print("  %6s   %s" % (labels[i], " ".join(row_strs)))

print()

print("  Decimal values:")
print("           %10s %10s %10s" % (labels[0], labels[1], labels[2]))
print("           %10s %10s %10s" % ("-" * 10, "-" * 10, "-" * 10))

for i in range(3):
    row_strs = []
    for j in range(3):
        row_strs.append("%10s" % mp.nstr(f2m(b_ij_SM[i][j]), 5))
    print("  %6s   %s" % (labels[i], " ".join(row_strs)))

print()

# ================================================================
# THE DOMINANT TWO-LOOP EFFECT
# ================================================================

print("THE DOMINANT TWO-LOOP EFFECT")
print("-" * 70)
print()
print("  The largest entry is b_33 = %s." % b_ij_SM[2][2])
print("  This is the SU(3) self-coupling at two loops.")
print()
print("  At one loop, SU(3) runs as d(1/a3)/d(ln mu) = -b3/(2pi).")
print("  At two loop, it gets a correction: -b_33 * a3 / (8*pi^2).")
print()
print("  Since b_33 = -26 (negative) and a3 > 0, the correction")
print("  is POSITIVE: it SLOWS the SU(3) running.")
print("  Slower SU(3) running means 1/a3 is LARGER at M_GUT,")
print("  bringing it closer to the 1/a1 = 1/a2 crossing point.")
print()
print("  This is why two-loop improves unification: the dominant")
print("  effect pulls alpha_3 toward the crossing, reducing Delta.")
print()

# ================================================================
# CABIBBO DOUBLET MODIFIED BETAS (one-loop)
# ================================================================

print("CABIBBO DOUBLET MODIFIED BETAS (Level 1, exact)")
print("-" * 70)
print()

# uses db1_VL, db2_VL, db3_VL from phys24_lib (DATA-4 N4-N6)
# uses b1_mod, b2_mod, b3_mod from phys24_lib (DATA-4 N7-N9)
show("Db_1 = %s" % db1_VL, f2m(db1_VL))
show("Db_2 = %s" % db2_VL, f2m(db2_VL))
show("Db_3 = %s" % db3_VL, f2m(db3_VL))
print()
show("b_1' = %s" % b1_mod, f2m(b1_mod))
show("b_2' = %s" % b2_mod, f2m(b2_mod))
show("b_3' = %s" % b3_mod, f2m(b3_mod))
print()

# ================================================================
# TWO-LOOP UNIFICATION RESULTS
# ================================================================
# These are verified results from unification_test.py (6/6 checks).
# The script integrates the coupled two-loop RGE numerically with
# a step-function threshold at M_VL for the Cabibbo Doublet.
# Below M_VL: SM betas + SM two-loop b_ij.
# Above M_VL: SM+CD one-loop betas + SM two-loop b_ij.
# (VL two-loop contribution neglected — estimated ~0.1% effect.)

print("TWO-LOOP UNIFICATION RESULTS (Derived)")
print("-" * 70)
print()
print("  From unification_test.py (6/6 checks), at M_VL = 500 GeV:")
print()

# uses delta_1loop, delta_2loop, twoloop_improvement from phys24_lib (N15-N17)
show("One-loop Delta(1/alpha_3) (dimensionless)", f2m(delta_1loop))
show("Two-loop Delta(1/alpha_3) (dimensionless)", f2m(delta_2loop))
print()

improvement = (f2m(delta_1loop) - f2m(delta_2loop)) / f2m(delta_1loop) * mpf("100")
show("Improvement (%%)", improvement)
print()

print("  The two-loop correction reduces the unification miss")
print("  by two-thirds. The residual Delta = %s is within the" %
      mp.nstr(f2m(delta_2loop), 3))
print("  standard range for GUT threshold corrections in minimal")
print("  SU(5) with ordinary mass splittings (factor 2-5 between")
print("  heavy particles).")
print()

# ================================================================
# COMPARISON TABLE
# ================================================================

print("UNIFICATION QUALITY COMPARISON")
print("-" * 70)
print()
print("  %-30s %12s %12s %10s" % ("Scenario", "Gap Ratio", "Delta", "Quality"))
print("  %-30s %12s %12s %10s" % ("-" * 30, "-" * 12, "-" * 12, "-" * 10))

scenarios = [
    ("SM (no BSM)", gap_SM, Fraction(-658, 100), "Excluded"),
    ("SM + CD (one-loop)", gap_VL, delta_1loop, "Poor"),
    ("SM + CD (two-loop)", gap_VL, delta_2loop, "Near"),
    ("MSSM (one-loop)", gap_MSSM, Fraction(-69, 100), "Near"),
]

for name, gap, delta, quality in scenarios:
    print("  %-30s %12s %12s %10s" % (
        name,
        mp.nstr(f2m(gap), 6),
        mp.nstr(f2m(delta), 4),
        quality))

print()
print("  The Cabibbo Doublet at two loops achieves the same")
print("  unification quality as the MSSM at one loop: both need")
print("  GUT threshold corrections of comparable magnitude.")
print()

# ================================================================
# WHAT REMAINS
# ================================================================

print("WHAT REMAINS (Open)")
print("-" * 70)
print()
print("  1. VL two-loop b_ij contribution (neglected, ~0.1%% effect)")
print("  2. GUT threshold corrections: parametrize as function of")
print("     M_T/M_X splitting in minimal SU(5) completion")
print("  3. Find M_VL for exact unification (two-loop + thresholds)")
print("  4. Predict alpha_s from unification condition")
print("  5. Predict sin^2(theta_W) from 3/8 + running with CD betas")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: b_ij matrix entries match DATA-4 N14 (spot checks)
chk_exact("b_ij[0][0] = 199/50",
          b_ij_SM[0][0], Fraction(199, 50), checks)

chk_exact("b_ij[1][1] = 35/6",
          b_ij_SM[1][1], Fraction(35, 6), checks)

chk_exact("b_ij[2][2] = -26",
          b_ij_SM[2][2], Fraction(-26, 1), checks)

# Check 2: one-loop Delta matches Session 3
chk("One-loop Delta ~ -1.17",
    f2m(delta_1loop), mpf("-1.17"), 2, checks)

# Check 3: two-loop Delta matches Session 3
chk("Two-loop Delta ~ -0.40",
    f2m(delta_2loop), mpf("-0.40"), 2, checks)

# Check 4: improvement is ~66%
chk("Improvement ~ 66%%",
    improvement, mpf("66"), 2, checks)

# Check 5: two-loop is closer to zero than one-loop
chk_bool("Two-loop closer to unification than one-loop",
         abs(f2m(delta_2loop)) < abs(f2m(delta_1loop)),
         "|Delta_2loop| = %s < |Delta_1loop| = %s" % (
             mp.nstr(abs(f2m(delta_2loop)), 4),
             mp.nstr(abs(f2m(delta_1loop)), 4)), checks)

# Check 6: residual Delta is within threshold correction range (|Delta| < 1)
chk_bool("Residual Delta < 1 (within threshold range)",
         abs(f2m(delta_2loop)) < mpf("1"),
         "|Delta| = %s" % mp.nstr(abs(f2m(delta_2loop)), 4), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-24 TWO-LOOP DEMONSTRATION COMPLETE")
print("=" * 70)
