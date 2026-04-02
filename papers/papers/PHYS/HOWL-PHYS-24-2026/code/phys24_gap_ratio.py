#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: The Gap Ratio
==========================================
The SM gauge couplings do not unify at one loop.
The gap ratio 218/115 = 1.896 misses the measured 1.358 by 40%.

Backed by: sin2_theta_w_1.py (9/9 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *

# ================================================================
# INPUTS
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: THE GAP RATIO")
print("=" * 70)
print()
print("INPUTS")
print("-" * 70)
print()

# uses alpha_inv from phys24_lib (DATA-4 B1, Type M, 12 source digits)
# uses sin2_tW from phys24_lib (DATA-4 B11, Type M, 5 source digits)
# uses alpha_s from phys24_lib (DATA-4 B12, Type M, 4 source digits)

show("alpha_EM^-1 (dimensionless)", f2m(alpha_inv))
show("sin^2(theta_W) (dimensionless)", f2m(sin2_tW))
show("alpha_s(M_Z) (dimensionless)", f2m(alpha_s))
print()

# ================================================================
# GUT NORMALIZATION
# ================================================================
# The SM U(1)_Y coupling is NOT alpha_EM.
# GUT normalization embeds U(1)_Y into SU(5):
#   alpha_1_GUT = (5/3) * alpha_EM / cos^2(theta_W)
#   alpha_2     = alpha_EM / sin^2(theta_W)
#   alpha_3     = alpha_s
#
# The factor 5/3 is Level 1: it comes from the SU(5) charge
# normalization Tr(Y^2) = (5/3) Tr(T_3^2) over a complete
# generation. Without this factor, the three couplings are
# not in the same normalization and cannot be compared.
#
# We work with inverses 1/alpha_i throughout.
# These are computed in phys24_lib as inv_a1, inv_a2, inv_a3.

print("GUT-NORMALIZED INVERSE COUPLINGS AT M_Z")
print("-" * 70)
print()

# uses inv_a1, inv_a2, inv_a3 from phys24_lib (derived from B1, B11, B12)
show("1/alpha_1(M_Z) (dimensionless)", f2m(inv_a1))
show("1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2))
show("1/alpha_3(M_Z) (dimensionless)", f2m(inv_a3))
print()

# Verify GUT normalization is self-consistent:
# 1/alpha_EM = (5/3) * 1/alpha_1 + 1/alpha_2
alpha_em_recon = Fraction(5, 3) * inv_a1 + inv_a2
show("(5/3)/alpha_1 + 1/alpha_2 (dimensionless)", f2m(alpha_em_recon))
show("1/alpha_EM input (dimensionless)", f2m(alpha_inv))
print()

# ================================================================
# SM BETA COEFFICIENTS
# ================================================================

print("SM ONE-LOOP BETA COEFFICIENTS (Level 1, exact)")
print("-" * 70)
print()

# uses b1_SM, b2_SM, b3_SM from phys24_lib (DATA-4 N1-N3, Type D, exact)
# These are exact rationals from the gauge group and SM particle content.
show("b_1 = %s" % b1_SM, f2m(b1_SM))
show("b_2 = %s" % b2_SM, f2m(b2_SM))
show("b_3 = %s" % b3_SM, f2m(b3_SM))
print()

# ================================================================
# THE GAP RATIO
# ================================================================
# At one loop, the inverse couplings run as straight lines:
#   1/alpha_i(mu) = 1/alpha_i(M_Z) - b_i/(2pi) * ln(mu/M_Z)
#
# For exact unification (all three lines meeting at one point),
# the ratio of the gaps at M_Z must equal the ratio of the slopes:
#
#   (1/a1 - 1/a2) / (1/a2 - 1/a3)  =  (b1 - b2) / (b2 - b3)
#
# The left side is measured. The right side is exact rational.
# If they match, the SM unifies at one loop.

print("THE GAP RATIO")
print("-" * 70)
print()

# uses gap_SM from phys24_lib (DATA-4 N10, = 218/115, exact)
b1_minus_b2 = b1_SM - b2_SM
b2_minus_b3 = b2_SM - b3_SM

show("b_1 - b_2 = %s" % b1_minus_b2, f2m(b1_minus_b2))
show("b_2 - b_3 = %s" % b2_minus_b3, f2m(b2_minus_b3))
print()
show("SM gap ratio (Level 1) = %s" % gap_SM, f2m(gap_SM))
print()

# uses gap_measured from phys24_lib (DATA-4 N13, derived from Level 2)
show("Measured gap ratio (Derived)", f2m(gap_measured))
print()

# ================================================================
# THE CONFRONTATION
# ================================================================

print("THE CONFRONTATION")
print("-" * 70)
print()

miss_abs = f2m(gap_SM) - f2m(gap_measured)
miss_pct = miss_abs / f2m(gap_measured) * mpf("100")

show("SM prediction (Level 1)", f2m(gap_SM))
show("Measured (Derived)", f2m(gap_measured))
show("Absolute miss (dimensionless)", miss_abs)
show("Relative miss (%%)", miss_pct)
print()
print("  THE SM DOES NOT UNIFY.")
print()
print("  The gap ratio is a ratio of exact rationals (218/115)")
print("  compared to a number derived from three measurements.")
print("  The 40%% miss is not a rounding error or an approximation.")
print("  It means the three coupling lines do not meet at a point.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: SM gap ratio is exactly 218/115 (Level 1 algebraic identity)
chk_exact("SM gap ratio = 218/115",
          gap_SM, Fraction(218, 115), checks)

# Check 2: gap ratio computed from betas matches library value
gap_from_betas = b1_minus_b2 / b2_minus_b3
chk_exact("Gap from betas matches library",
          gap_from_betas, gap_SM, checks)

# Check 3: measured gap ratio matches Session 3 value
chk("Measured gap ratio vs Session 3",
    f2m(gap_measured), mpf("1.358193"), 4, checks)

# Check 4: SM misses by more than 30%
chk_bool("SM miss exceeds 30%%",
         miss_pct > mpf("30"),
         "miss = %s%%" % mp.nstr(miss_pct, 4), checks)

# Check 5: GUT normalization self-consistency
chk("GUT normalization: (5/3)/a1 + 1/a2 = 1/alpha_EM",
    f2m(alpha_em_recon), f2m(alpha_inv), 11, checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-24 GAP RATIO DEMONSTRATION COMPLETE")
print("=" * 70)
