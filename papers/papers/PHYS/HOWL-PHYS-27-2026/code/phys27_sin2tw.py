#!/usr/bin/env python3
"""
HOWL PHYS-27: phys27_sin2tw.py
================================
sin²θ_W from 3/8 — The GUT prediction with Cabibbo Doublet betas.

At tree level in SU(5): sin²θ_W = 3/8. One-loop running from
M_GUT to M_Z with the CD modified betas reduces this. The
prediction uses only alpha_EM and alpha_s as input (two Level 2
values) and PREDICTS sin²θ_W as output.

The test: does the CD framework predict the correct sin²θ_W
from only two of the three couplings?

Also tests: is the predicted sin²θ_W close to 3/13?

Backed by: sin2_theta_w_1.py (9/9), phys26_normalization.py (20/20)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, fabs

# ================================================================
print("=" * 70)
print("HOWL PHYS-27: sin²θ_W FROM 3/8")
print("The GUT tree-level prediction + one-loop running.")
print("=" * 70)
print()

# ================================================================
# SECTION 1: THE TREE-LEVEL VALUE
# ================================================================

print("SECTION 1: THE TREE-LEVEL VALUE")
print("-" * 70)
print()
print("  In SU(5), all three gauge couplings unify at M_GUT:")
print("    alpha_1 = alpha_2 = alpha_3 = alpha_GUT")
print()
print("  At the unification point:")
print("    sin²θ_W = 1/(1 + (5/3)) = 3/8 = 0.375")
print()

sin2_tree = Fraction(3, 8)
show("  sin²θ_W(tree) = 3/8 (dimensionless)", f2m(sin2_tree))
show("  sin²θ_W(measured) (dimensionless)", f2m(sin2_tW))
show("  Tree - measured (dimensionless)", f2m(sin2_tree) - f2m(sin2_tW))
print()
print("  The running from M_GUT to M_Z must produce a correction")
print("  of −0.144 to bring 0.375 down to 0.231.")
print()

# ================================================================
# SECTION 2: THE ONE-LOOP RUNNING PREDICTION
# ================================================================
# Strategy: use alpha_EM and alpha_s as the TWO inputs.
# From these + the CD betas, PREDICT sin²θ_W.
#
# At one loop:
#   1/alpha_i(M_Z) = 1/alpha_GUT - b_i'/(2*pi) * ln(M_Z/M_GUT)
#
# Define L = ln(M_GUT/M_Z)/(2*pi) > 0.
# Then: 1/alpha_i(M_Z) = 1/alpha_GUT + b_i' * L
#
# Three equations, two unknowns (alpha_GUT, L):
#   1/alpha_1 = 1/alpha_GUT + b1' * L
#   1/alpha_2 = 1/alpha_GUT + b2' * L
#   1/alpha_3 = 1/alpha_GUT + b3' * L
#
# From equations 1 and 3 (using alpha_EM and alpha_s):
#   1/alpha_1 - 1/alpha_3 = (b1' - b3') * L
#   L = (1/alpha_1 - 1/alpha_3) / (b1' - b3')
#
# But 1/alpha_1 depends on sin²θ_W... which we want to predict.
# So use 1/alpha_EM and alpha_s directly:
#   1/alpha_EM = (5/3)/alpha_1 + 1/alpha_2
#             = (5/3)*(1/alpha_GUT + b1'*L) + (1/alpha_GUT + b2'*L)
#             = (8/3)/alpha_GUT + ((5/3)*b1' + b2')*L
#
#   1/alpha_3 = 1/alpha_GUT + b3'*L
#
# Two equations in two unknowns (1/alpha_GUT, L):
#   1/alpha_EM = (8/3)/alpha_GUT + B_EM * L    where B_EM = (5/3)*b1' + b2'
#   1/alpha_3  = 1/alpha_GUT + b3' * L
#
# From equation 2: 1/alpha_GUT = 1/alpha_3 - b3'*L
# Substitute into equation 1:
#   1/alpha_EM = (8/3)*(1/alpha_3 - b3'*L) + B_EM*L
#             = (8/3)/alpha_3 - (8/3)*b3'*L + B_EM*L
#             = (8/3)/alpha_3 + (B_EM - (8/3)*b3')*L
#
# Solve for L:
#   L = (1/alpha_EM - (8/3)/alpha_3) / (B_EM - (8/3)*b3')

print("SECTION 2: ONE-LOOP RUNNING PREDICTION")
print("-" * 70)
print()
print("  Inputs: alpha_EM and alpha_s only.")
print("  Output: predicted sin²θ_W.")
print()

# uses alpha_inv, alpha_s from phys24_lib (DATA-4 B1, B12)
# uses b1_mod, b2_mod, b3_mod from phys24_lib (DATA-4 N7-N9)

inv_aEM = alpha_inv                          # Fraction
inv_a3 = Fraction(1) / alpha_s               # Fraction

B_EM = Fraction(5, 3) * b1_mod + b2_mod     # (5/3)*b1' + b2'

# L = (1/alpha_EM - (8/3)/alpha_3) / (B_EM - (8/3)*b3')
numerator_L = inv_aEM - Fraction(8, 3) * inv_a3
denominator_L = B_EM - Fraction(8, 3) * b3_mod

L_pred = numerator_L / denominator_L         # Fraction

show("  B_EM = (5/3)*b1' + b2' = %s (dimensionless)" % B_EM, f2m(B_EM))
show("  L numerator = 1/alpha_EM - (8/3)/alpha_s (dimensionless)",
     f2m(numerator_L))
show("  L denominator = B_EM - (8/3)*b3' (dimensionless)",
     f2m(denominator_L))
show("  L = ln(M_GUT/M_Z)/(2*pi) (dimensionless)", f2m(L_pred))
print()

# From L, get 1/alpha_GUT
inv_aGUT = inv_a3 - b3_mod * L_pred         # Fraction

show("  1/alpha_GUT (dimensionless)", f2m(inv_aGUT))
print()

# Now predict 1/alpha_1 and 1/alpha_2 at M_Z
inv_a1_pred = inv_aGUT + b1_mod * L_pred     # Fraction
inv_a2_pred = inv_aGUT + b2_mod * L_pred     # Fraction

show("  Predicted 1/alpha_1(M_Z) (dimensionless)", f2m(inv_a1_pred))
show("  Predicted 1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2_pred))
print()

# Predict sin²θ_W = 1/(1 + (5/3)*inv_a1/inv_a2)
# In Fraction arithmetic:
sin2_pred_frac = inv_a2_pred / (inv_a2_pred + Fraction(5, 3) * inv_a1_pred)
sin2_pred = f2m(sin2_pred_frac)
sin2_meas = f2m(sin2_tW)

show("  Predicted sin²θ_W (dimensionless)", sin2_pred)
show("  Measured sin²θ_W (dimensionless)", sin2_meas)
show("  Difference (dimensionless)", sin2_pred - sin2_meas)

miss_pct = fabs(sin2_pred - sin2_meas) / sin2_meas * mpf("100")
show("  Relative miss (%%)", miss_pct)
print()

# ================================================================
# SECTION 3: COMPARISON TO 3/13
# ================================================================

print("SECTION 3: COMPARISON TO 3/13")
print("-" * 70)
print()

sin2_3over13 = Fraction(3, 13)
miss_from_3_13 = fabs(sin2_pred - f2m(sin2_3over13)) / f2m(sin2_3over13) * mpf("100")
miss_meas_from_3_13 = fabs(sin2_meas - f2m(sin2_3over13)) / f2m(sin2_3over13) * mpf("100")

show("  3/13 (dimensionless)", f2m(sin2_3over13))
show("  Predicted sin²θ_W (dimensionless)", sin2_pred)
show("  Measured sin²θ_W (dimensionless)", sin2_meas)
print()
show("  Predicted miss from 3/13 (%%)", miss_from_3_13)
show("  Measured miss from 3/13 (%%)", miss_meas_from_3_13)
print()

# Does the running produce exactly 3/13?
# sin2_pred_frac should equal 3/13 if the running gives exactly that
show("  sin²θ_W predicted (Fraction) (dimensionless)", f2m(sin2_pred_frac))
print("  sin²θ_W predicted as Fraction = %s" % sin2_pred_frac)
print("  3/13 = %s" % sin2_3over13)
print("  Are they equal? %s" % ("YES" if sin2_pred_frac == sin2_3over13 else "NO"))
print()

# What is the required correction for exactly 3/13?
# 3/8 - correction = 3/13
# correction = 3/8 - 3/13 = (39 - 24)/104 = 15/104
correction_exact = Fraction(3, 8) - Fraction(3, 13)
show("  Required correction for 3/13: 3/8 - 3/13 = %s (dimensionless)" % correction_exact,
     f2m(correction_exact))
actual_correction = sin2_tree - sin2_pred_frac
show("  Actual correction from running = %s (dimensionless)" % actual_correction,
     f2m(actual_correction))
print()

# ================================================================
# SECTION 4: M_GUT AND CONSISTENCY
# ================================================================

print("SECTION 4: M_GUT AND CONSISTENCY")
print("-" * 70)
print()

M_Z_GeV = f2m(M_Z) / mpf("1000")
from mpmath import log10 as mlog10
M_GUT_pred = M_Z_GeV * mexp(f2m(L_pred) * mpf("2") * mpi)
log10_MGUT = mlog10(M_GUT_pred)

show("  M_GUT (GeV)", M_GUT_pred)
show("  log10(M_GUT/GeV)", log10_MGUT)
print()

# Check: does 1/alpha_3 at M_GUT match 1/alpha_GUT?
inv_a3_at_GUT = f2m(inv_a3) - f2m(b3_mod) * f2m(L_pred)
show("  1/alpha_3(M_GUT) (dimensionless)", inv_a3_at_GUT)
show("  1/alpha_GUT (dimensionless)", f2m(inv_aGUT))

# The unification miss: Delta(1/alpha_3)
# At M_GUT defined by alpha_1 = alpha_2 crossing:
# 1/alpha_3(M_GUT) should equal 1/alpha_GUT if exact unification
# The one-loop miss is:
inv_a1_at_GUT = f2m(inv_a1_pred) - f2m(b1_mod) * f2m(L_pred)
inv_a2_at_GUT = f2m(inv_a2_pred) - f2m(b2_mod) * f2m(L_pred)

# Actually the crossing is where inv_a1 = inv_a2, and L was defined by that
# So inv_a3 at the crossing gives the miss
Delta_unif = inv_a3_at_GUT - f2m(inv_aGUT)
show("  Delta(1/alpha_3) at M_GUT (dimensionless)", Delta_unif)
print()

# ================================================================
# SECTION 5: THE PHYSICAL CONTENT
# ================================================================

print("SECTION 5: THE PHYSICAL CONTENT")
print("-" * 70)
print()
print("  This computation uses TWO measured inputs:")
print("    alpha_EM = 1/%s (DATA-4 B1)" % mp.nstr(f2m(alpha_inv), 11))
print("    alpha_s  = %s (DATA-4 B12)" % mp.nstr(f2m(alpha_s), 4))
print()
print("  And ONE Level 1 input:")
print("    sin²θ_W(M_GUT) = 3/8 (SU(5) tree level)")
print()
print("  It PREDICTS sin²θ_W(M_Z) = %s" % mp.nstr(sin2_pred, 11))
print("  The measured value is %s" % mp.nstr(sin2_meas, 5))
print()
print("  If the prediction matches, sin²θ_W is DERIVED from")
print("  alpha_EM, alpha_s, and the gauge group — reducing the")
print("  SM parameter count by 1.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: tree level = 3/8
chk_exact("Tree level sin²θ_W = 3/8",
          sin2_tree, Fraction(3, 8), checks)

# Check 2: B_EM computation
B_EM_expected = Fraction(5, 3) * Fraction(25, 6) + Fraction(-13, 6)
chk_exact("B_EM = (5/3)*b1' + b2'",
          B_EM, B_EM_expected, checks)

# Check 3: prediction within 5% of measured (abort test)
chk_bool("Predicted sin²θ_W within 5%% of measured",
         miss_pct < mpf("5"),
         "miss = %s%%" % mp.nstr(miss_pct, 6), checks)

# Check 4: prediction matches measured
# How many digits of agreement?
chk("Predicted sin²θ_W matches measured",
    sin2_pred, sin2_meas, 4, checks)

# Check 5: M_GUT in expected range
chk_bool("M_GUT in [10^15, 10^16]",
         mpf("15") < log10_MGUT < mpf("16"),
         "log10(M_GUT) = %s" % mp.nstr(log10_MGUT, 4), checks)

# Check 6: Delta is the known one-loop miss
chk("Delta(1/alpha_3) ~ -1.17",
    Delta_unif, mpf("-1.17"), 2, checks)

# Check 7: prediction close to 3/13
chk_bool("Predicted sin²θ_W within 0.5%% of 3/13",
         miss_from_3_13 < mpf("0.5"),
         "miss from 3/13 = %s%%" % mp.nstr(miss_from_3_13, 4), checks)

# Check 8: measured close to 3/13
chk_bool("Measured sin²θ_W within 0.3%% of 3/13",
         miss_meas_from_3_13 < mpf("0.3"),
         "miss from 3/13 = %s%%" % mp.nstr(miss_meas_from_3_13, 4), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-27 sin²θ_W FROM 3/8 COMPLETE")
print("=" * 70)

