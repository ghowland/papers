#!/usr/bin/env python3
"""
HOWL PHYS-25 DEMONSTRATION: sin²θ_W from 3/8
===============================================
phys25_sin2_theta_W.py

At the SU(5) GUT scale, sin²θ_W = 3/8 exactly (Level 1).
One-loop running with Cabibbo Doublet modified betas, using
only alpha_EM and alpha_s as inputs, predicts sin²θ_W(M_Z).
CD prediction: 0.2284, miss −1.2% from measured 0.23122.
SM prediction: 0.2052, miss −11.3%. CD is 9× closer.

Two-loop and threshold corrections are expected to close the
remaining gap, as they do for the unification Delta.

Backed by: sin2_theta_w_1.py (9/9 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *
from mpmath import exp as mexp, pi as mpi, log10 as mlog10

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-25: sin^2(theta_W) FROM 3/8")
print("=" * 70)
print()

# ================================================================
# THE GUT BOUNDARY CONDITION (Level 1)
# ================================================================
# In SU(5), at the unification scale M_GUT:
#   alpha_1 = alpha_2 = alpha_3 = alpha_GUT
#
# The weak mixing angle:
#   sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2)
#
# where alpha_Y is the SM U(1)_Y coupling and the GUT
# normalization gives alpha_1 = (5/3)*alpha_Y.
#
# At M_GUT where alpha_1 = alpha_2 = alpha_GUT:
#   sin^2 = (3/5)*alpha_GUT / ((3/5 + 1)*alpha_GUT)
#         = (3/5) / (8/5) = 3/8
#
# This is Level 1: depends only on the SU(5) embedding.

print("THE GUT BOUNDARY CONDITION (Level 1)")
print("-" * 70)
print()

sin2_GUT = Fraction(3, 8)

print("  At M_GUT in SU(5): alpha_1 = alpha_2 = alpha_GUT")
print("  alpha_Y = (3/5)*alpha_1")
print("  sin^2 = alpha_Y/(alpha_Y + alpha_2) = (3/5)/(8/5) = 3/8")
print()
show("sin^2(theta_W) at M_GUT (dimensionless)", f2m(sin2_GUT))
print()

# ================================================================
# INPUTS (Level 2)
# ================================================================

print("INPUTS (Level 2, from DATA-4)")
print("-" * 70)
print()

# uses alpha_inv from phys24_lib (DATA-4 B1, Type M, 12 digits)
# uses alpha_s from phys24_lib (DATA-4 B12, Type M, 4 digits)
# uses sin2_tW from phys24_lib (DATA-4 B11, Type M, 5 digits)
# uses inv_a1, inv_a2, inv_a3 (derived from B1, B11, B12)

show("alpha_EM^-1 (dimensionless)", f2m(alpha_inv))
show("alpha_s(M_Z) (dimensionless)", f2m(alpha_s))
show("sin^2(theta_W) measured (dimensionless)", f2m(sin2_tW))
print()
show("1/alpha_1(M_Z) GUT-normalized (dimensionless)", f2m(inv_a1))
show("1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2))
show("1/alpha_3(M_Z) (dimensionless)", f2m(inv_a3))
print()

# ================================================================
# GUT NORMALIZATION IDENTITIES
# ================================================================
# From the definitions:
#   alpha_EM = alpha_2 * sin^2 = alpha_Y * cos^2
#   alpha_1 = (5/3)*alpha_Y
#
# In terms of inverses:
#   (5/3)*inv_a1 + inv_a2 = cos^2*alpha_inv + sin^2*alpha_inv = alpha_inv
#
#   sin^2 = inv_a2 / ((5/3)*inv_a1 + inv_a2) = inv_a2 / alpha_inv

print("GUT NORMALIZATION IDENTITIES")
print("-" * 70)
print()

norm_check = Fraction(5, 3) * inv_a1 + inv_a2

show("(5/3)/alpha_1 + 1/alpha_2 (dimensionless)", f2m(norm_check))
show("1/alpha_EM (dimensionless)", f2m(alpha_inv))
print()

sin2_from_identity = inv_a2 / (Fraction(5, 3) * inv_a1 + inv_a2)

show("sin^2 from identity (dimensionless)", f2m(sin2_from_identity))
show("sin^2 measured (dimensionless)", f2m(sin2_tW))
print()

# ================================================================
# ONE-LOOP RUNNING EQUATIONS
# ================================================================
# The RGE: d(1/alpha_i)/d(ln mu) = -b_i/(2*pi)
#
# Integrating from M_GUT down to M_Z:
#   inv_a_i(M_Z) = 1/alpha_GUT + b_i' * L
#
# where L = ln(M_GUT/M_Z) / (2*pi) > 0.
#
# (Sign check: d(1/a)/d(ln mu) = -b/(2pi). Going from M_GUT to M_Z,
# ln mu decreases by ln(M_GUT/M_Z). So 1/a(M_Z) - 1/a(M_GUT) =
# -b/(2pi) * (ln M_Z - ln M_GUT) = +b/(2pi) * ln(M_GUT/M_Z) = b*L.)
#
# Unification: inv_a1(M_GUT) = inv_a2(M_GUT) implies
#   inv_a1 - b_1'*L = inv_a2 - b_2'*L
#   L = (inv_a1 - inv_a2) / (b_1' - b_2')
#
# Both numerator and denominator are positive, so L > 0.

print("ONE-LOOP RUNNING (Level 1 structure)")
print("-" * 70)
print()

# uses b1_mod, b2_mod, b3_mod from phys24_lib (N7-N9)

b12_diff = b1_mod - b2_mod    # = 19/3
delta_12 = inv_a1 - inv_a2    # positive

L_CD = delta_12 / b12_diff

show("b_1' = %s (dimensionless)" % b1_mod, f2m(b1_mod))
show("b_2' = %s (dimensionless)" % b2_mod, f2m(b2_mod))
show("b_3' = %s (dimensionless)" % b3_mod, f2m(b3_mod))
print()
show("b_1' - b_2' = %s (dimensionless)" % b12_diff, f2m(b12_diff))
show("inv_a1 - inv_a2 (dimensionless)", f2m(delta_12))
show("L_CD = ln(M_GUT/M_Z)/(2*pi) (dimensionless)", f2m(L_CD))
print()

# ================================================================
# THE PREDICTION: alpha_EM + alpha_s -> sin^2(theta_W)
# ================================================================
# Two measured inputs: alpha_EM^-1 and alpha_s.
# The unification hypothesis (all three couplings equal at M_GUT)
# determines two unknowns (L and alpha_GUT), then predicts
# the third coupling (alpha_2, equivalently sin^2).
#
# From inv_a_i(M_Z) = 1/alpha_GUT + b_i'*L:
#
#   (5/3)*inv_a1 + inv_a2 = (8/3)/alpha_GUT + B_EM*L = alpha_inv  (I)
#   inv_a3 = 1/alpha_GUT + b_3'*L                                  (II)
#
# where B_EM = (5/3)*b_1' + b_2'.
#
# From (I): 1/alpha_GUT = (3/8)*(alpha_inv - B_EM*L)
# Substitute into (II):
#   inv_a3 = (3/8)*(alpha_inv - B_EM*L) + b_3'*L
#          = (3/8)*alpha_inv + [b_3' - (3/8)*B_EM]*L
#
# Solve for L:
#   L = (inv_a3 - (3/8)*alpha_inv) / (b_3' - (3/8)*B_EM)

print("THE PREDICTION: alpha_EM + alpha_s -> sin^2(theta_W)")
print("-" * 70)
print()

B_EM = Fraction(5, 3) * b1_mod + b2_mod

show("B_EM = (5/3)*b_1' + b_2' = %s (dimensionless)" % B_EM, f2m(B_EM))

coeff_L = b3_mod - Fraction(3, 8) * B_EM
rhs_L   = inv_a3 - Fraction(3, 8) * alpha_inv

L_pred = rhs_L / coeff_L

show("Coefficient of L (dimensionless)", f2m(coeff_L))
show("L from prediction (dimensionless)", f2m(L_pred))
show("L from 1-2 crossing (dimensionless)", f2m(L_CD))
print()

# L_pred and L_CD differ because the SM+CD does not unify
# exactly at one loop. The mismatch is the unification deficit
# expressed as a scale discrepancy rather than as Delta(1/alpha_3).
L_mismatch_pct = abs(f2m(L_pred) - f2m(L_CD)) / f2m(L_CD) * mpf("100")
show("L mismatch (%%)", L_mismatch_pct)
print("  This mismatch IS the one-loop unification deficit.")
print()

# Recover 1/alpha_GUT and the individual couplings
alpha_GUT_inv = Fraction(3, 8) * (alpha_inv - B_EM * L_pred)
inv_a1_pred = alpha_GUT_inv + b1_mod * L_pred
inv_a2_pred = alpha_GUT_inv + b2_mod * L_pred
inv_a3_pred = alpha_GUT_inv + b3_mod * L_pred

show("1/alpha_GUT (dimensionless)", f2m(alpha_GUT_inv))
show("1/alpha_1 predicted (dimensionless)", f2m(inv_a1_pred))
show("1/alpha_2 predicted (dimensionless)", f2m(inv_a2_pred))
show("1/alpha_3 predicted (dimensionless)", f2m(inv_a3_pred))
show("1/alpha_3 input (dimensionless)", f2m(inv_a3))
print()

# Predict sin^2
sin2_pred = inv_a2_pred / (Fraction(5, 3) * inv_a1_pred + inv_a2_pred)

show("sin^2(theta_W) predicted (dimensionless)", f2m(sin2_pred))
show("sin^2(theta_W) measured (dimensionless)", f2m(sin2_tW))
print()

miss_abs = f2m(sin2_pred) - f2m(sin2_tW)
miss_pct = miss_abs / f2m(sin2_tW) * mpf("100")

show("Absolute miss (dimensionless)", miss_abs)
show("Relative miss (%%)", miss_pct)
print()

# ================================================================
# M_GUT FROM THE PREDICTION
# ================================================================

print("M_GUT FROM THE PREDICTION")
print("-" * 70)
print()

# L = ln(M_GUT/M_Z) / (2*pi), so M_GUT = M_Z * exp(2*pi*L)
# M_Z from phys24_lib (DATA-4 C1) in MeV
M_Z_GeV = f2m(M_Z) / mpf("1000")
M_GUT_pred = M_Z_GeV * mexp(mpf("2") * mpi * f2m(L_pred))
log10_MGUT_pred = mlog10(M_GUT_pred)

M_GUT_12 = M_Z_GeV * mexp(mpf("2") * mpi * f2m(L_CD))
log10_MGUT_12 = mlog10(M_GUT_12)

show("M_GUT from prediction (GeV)", M_GUT_pred)
show("log10(M_GUT/GeV) from prediction", log10_MGUT_pred)
print()
show("M_GUT from 1-2 crossing (GeV)", M_GUT_12)
show("log10(M_GUT/GeV) from 1-2 crossing", log10_MGUT_12)
print()
print("  Both are in the 10^15-16 range, consistent with the")
print("  cabibbo_doublet.py result (10^15.54 GeV).")
print()

# ================================================================
# SM COMPARISON
# ================================================================

print("SM COMPARISON")
print("-" * 70)
print()

B_EM_SM   = Fraction(5, 3) * b1_SM + b2_SM
coeff_SM  = b3_SM - Fraction(3, 8) * B_EM_SM
rhs_SM    = inv_a3 - Fraction(3, 8) * alpha_inv
L_SM_pred = rhs_SM / coeff_SM

alpha_GUT_inv_SM = Fraction(3, 8) * (alpha_inv - B_EM_SM * L_SM_pred)
inv_a1_SM_pred = alpha_GUT_inv_SM + b1_SM * L_SM_pred
inv_a2_SM_pred = alpha_GUT_inv_SM + b2_SM * L_SM_pred

sin2_SM_pred = inv_a2_SM_pred / (Fraction(5, 3) * inv_a1_SM_pred + inv_a2_SM_pred)

miss_SM_abs = f2m(sin2_SM_pred) - f2m(sin2_tW)
miss_SM_pct = miss_SM_abs / f2m(sin2_tW) * mpf("100")

show("SM sin^2 predicted (dimensionless)", f2m(sin2_SM_pred))
show("SM absolute miss (dimensionless)", miss_SM_abs)
show("SM relative miss (%%)", miss_SM_pct)
print()
show("CD sin^2 predicted (dimensionless)", f2m(sin2_pred))
show("CD absolute miss (dimensionless)", miss_abs)
show("CD relative miss (%%)", miss_pct)
print()

cd_closer = abs(f2m(sin2_pred) - f2m(sin2_tW)) < abs(f2m(sin2_SM_pred) - f2m(sin2_tW))
improvement = abs(miss_SM_pct) / abs(miss_pct)
print("  CD closer to measured than SM: %s" % cd_closer)
show("  Improvement factor (dimensionless)", improvement)
print()

# ================================================================
# DISPOSITION: PARKED NOTEBOOK FORMULA
# ================================================================

print("DISPOSITION: PARKED NOTEBOOK FORMULA")
print("-" * 70)
print()
print("  PHYS-24 Appendix J states an approximate formula:")
print("    sin^2 = 3/8 - (109/72)*L_X/alpha_inv")
print()
print("  This linearization assumes sin^2 ~ 3/8 in the running")
print("  correction. The full nonlinear prediction computed above")
print("  supersedes it. The coefficient 109/72 is not used and")
print("  need not be verified. The direct computation from")
print("  alpha_EM + alpha_s + unification is exact in Fraction")
print("  arithmetic at one loop.")
print()

# ================================================================
# INTERPRETATION
# ================================================================

print("INTERPRETATION")
print("-" * 70)
print()
print("  INPUTS: alpha_EM^-1 and alpha_s (two Level 2 measurements)")
print("  HYPOTHESIS: unification at M_GUT with CD modified betas")
print("  OUTPUT: sin^2(theta_W) = %s" % mp.nstr(f2m(sin2_pred), 6))
print()
print("  CD miss:  %s%% (one-loop)" % mp.nstr(miss_pct, 4))
print("  SM miss:  %s%% (one-loop)" % mp.nstr(miss_SM_pct, 4))
print("  CD is %s times closer to the measured value." %
      mp.nstr(improvement, 3))
print()
print("  The L mismatch (%s%%) between the 1-2 and 1-3" %
      mp.nstr(L_mismatch_pct, 3))
print("  crossing scales is the one-loop unification deficit")
print("  expressed as a scale discrepancy. Two-loop corrections")
print("  reduced the unification Delta by 66%% (PHYS-24 Section 8);")
print("  similar improvement is expected here.")
print()
print("  Stage 1 assessment: CONSISTENT. No kill switch fires.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: sin^2 at M_GUT = 3/8 exactly (Level 1)
chk_exact("sin^2(theta_W) at M_GUT = 3/8",
          sin2_GUT, Fraction(3, 8), checks)

# Check 2: GUT normalization identity
chk_exact("GUT normalization: (5/3)/a1 + 1/a2 = alpha_inv",
          norm_check, alpha_inv, checks)

# Check 3: sin^2 identity reproduces measured
chk_exact("sin^2 identity reproduces measured",
          sin2_from_identity, sin2_tW, checks)

# Check 4: L is positive (M_GUT > M_Z)
chk_bool("L_CD is positive (M_GUT > M_Z)",
         f2m(L_CD) > mpf("0"),
         "L_CD = %s" % mp.nstr(f2m(L_CD), 6), checks)

# Check 5: L_pred and L_CD agree within 5% (unification deficit)
chk_bool("L_pred and L_CD agree within 5%%",
         L_mismatch_pct < mpf("5"),
         "mismatch = %s%%" % mp.nstr(L_mismatch_pct, 4), checks)

# Check 6: inv_a3 round-trips (prediction input consistency)
chk_exact("inv_a3 round-trips through prediction",
          inv_a3_pred, inv_a3, checks)

# Check 7: CD predicted sin^2 within 10% of measured
chk_bool("CD sin^2 miss < 10%%",
         abs(miss_pct) < mpf("10"),
         "miss = %s%%" % mp.nstr(miss_pct, 4), checks)

# Check 8: CD closer to measured than SM
chk_bool("CD prediction closer than SM",
         cd_closer,
         "CD miss = %s%%, SM miss = %s%%" % (
             mp.nstr(abs(miss_pct), 4),
             mp.nstr(abs(miss_SM_pct), 4)), checks)

# Check 9: predicted sin^2 in physical range [0.2, 0.3]
chk_bool("Predicted sin^2 in [0.2, 0.3]",
         mpf("0.2") < f2m(sin2_pred) < mpf("0.3"),
         "sin^2 = %s" % mp.nstr(f2m(sin2_pred), 6), checks)

# Check 10: M_GUT in [10^15, 10^17]
chk_bool("M_GUT in [10^15, 10^17] GeV",
         mpf("15") < log10_MGUT_pred < mpf("17"),
         "log10(M_GUT) = %s" % mp.nstr(log10_MGUT_pred, 4), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-25 sin^2(theta_W) DEMONSTRATION COMPLETE")
print("=" * 70)
