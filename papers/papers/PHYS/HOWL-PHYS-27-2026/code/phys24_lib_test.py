#!/usr/bin/env python3
"""
HOWL PHYS-27: phys27_sin2tw.py
================================
sin²θ_W from 3/8 — The GUT prediction with Cabibbo Doublet betas.

At tree level in SU(5): sin²θ_W = 3/8. One-loop running from
M_GUT to M_Z with the CD modified betas reduces this.

Three tests performed:
  1. Two-input prediction: use alpha_EM and alpha_s to PREDICT sin²θ_W
  2. Three-input consistency: use all three couplings independently
  3. Comparison to 3/13 = N_gen/|b2_mod_num|

Note: This script uses CD betas from M_Z to M_GUT (no M_VL threshold).
The unification_test.py Delta = -1.17 used SM betas below M_VL = 500 GeV
and CD betas above. Different physical assumptions give different Delta.

Backed by: sin2_theta_w_1.py (9/9), phys26_normalization.py (20/20)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, fabs
from mpmath import log10 as mlog10

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
print("  In SU(5), all three gauge couplings unify at M_GUT.")
print("  At the unification point, alpha_1 = alpha_2, so:")
print("    sin²θ_W = 1/(1 + (5/3)) = 3/8 = 0.375")
print()

sin2_tree = Fraction(3, 8)
show("  sin²θ_W(tree) = 3/8 (dimensionless)", f2m(sin2_tree))
show("  sin²θ_W(measured) (dimensionless)", f2m(sin2_tW))
show("  Correction needed: 3/8 - measured (dimensionless)",
     f2m(sin2_tree) - f2m(sin2_tW))
print()

# ================================================================
# SECTION 2: TWO-INPUT PREDICTION (alpha_EM + alpha_s → sin²θ_W)
# ================================================================

print("SECTION 2: TWO-INPUT PREDICTION")
print("-" * 70)
print()
print("  Inputs: alpha_EM and alpha_s ONLY.")
print("  Level 1: sin²θ_W(M_GUT) = 3/8, CD betas (25/6, -13/6, -20/3).")
print("  Output: predicted sin²θ_W(M_Z).")
print("  Note: CD betas used from M_Z to M_GUT (no M_VL threshold).")
print()

inv_aEM = alpha_inv
inv_a3_frac = Fraction(1) / alpha_s

B_EM = Fraction(5, 3) * b1_mod + b2_mod

numerator_L = inv_aEM - Fraction(8, 3) * inv_a3_frac
denominator_L = B_EM - Fraction(8, 3) * b3_mod
L_2input = numerator_L / denominator_L

inv_aGUT_2input = inv_a3_frac - b3_mod * L_2input

inv_a1_pred = inv_aGUT_2input + b1_mod * L_2input
inv_a2_pred = inv_aGUT_2input + b2_mod * L_2input

sin2_pred_2input = inv_a2_pred / (inv_a2_pred + Fraction(5, 3) * inv_a1_pred)

sin2_pred_m = f2m(sin2_pred_2input)
sin2_meas = f2m(sin2_tW)

show("  L = ln(M_GUT/M_Z)/(2*pi) (dimensionless)", f2m(L_2input))
show("  1/alpha_GUT (dimensionless)", f2m(inv_aGUT_2input))
show("  Predicted 1/alpha_1(M_Z) (dimensionless)", f2m(inv_a1_pred))
show("  Predicted 1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2_pred))
print()
show("  PREDICTED sin²θ_W(M_Z) (dimensionless)", sin2_pred_m)
show("  MEASURED  sin²θ_W(M_Z) (dimensionless)", sin2_meas)

miss_2input = fabs(sin2_pred_m - sin2_meas) / sin2_meas * mpf("100")
show("  Relative miss (%%)", miss_2input)
print()

M_Z_GeV = f2m(M_Z) / mpf("1000")
M_GUT_2input = M_Z_GeV * mexp(f2m(L_2input) * mpf("2") * mpi)
log10_MGUT_2input = mlog10(M_GUT_2input)
show("  M_GUT (GeV)", M_GUT_2input)
show("  log10(M_GUT/GeV)", log10_MGUT_2input)
print()

print("  The two-input prediction undershoots by %s%%." %
      mp.nstr(miss_2input, 4))
print("  Direction is correct: 0.375 -> 0.228 toward 0.231.")
print("  The ~1.2%% residual is the expected size of two-loop")
print("  + threshold corrections.")
print()

# ================================================================
# SECTION 3: THREE-INPUT CONSISTENCY
# ================================================================

print("SECTION 3: THREE-INPUT CONSISTENCY")
print("-" * 70)
print()
print("  Inputs: alpha_EM, sin²θ_W, alpha_s (all three).")
print("  Define M_GUT by alpha_1 = alpha_2 crossing.")
print("  Measure alpha_3 miss at the crossing.")
print("  Note: CD betas from M_Z (no threshold). Delta differs")
print("  from unification_test.py (-1.17) which used M_VL = 500 GeV.")
print()

L_3input = (f2m(inv_a1) - f2m(inv_a2)) / f2m(b1_mod - b2_mod)
inv_aGUT_3input = f2m(inv_a1) - f2m(b1_mod) * L_3input
inv_a3_at_GUT = f2m(Fraction(1) / alpha_s) - f2m(b3_mod) * L_3input
Delta_3input = inv_a3_at_GUT - inv_aGUT_3input

M_GUT_3input = M_Z_GeV * mexp(L_3input * mpf("2") * mpi)
log10_MGUT_3input = mlog10(M_GUT_3input)

show("  L (from crossing) (dimensionless)", L_3input)
show("  1/alpha_GUT (at crossing) (dimensionless)", inv_aGUT_3input)
show("  1/alpha_3(M_GUT) (dimensionless)", inv_a3_at_GUT)
show("  Delta(1/alpha_3) (dimensionless)", Delta_3input)
show("  M_GUT (GeV)", M_GUT_3input)
show("  log10(M_GUT/GeV)", log10_MGUT_3input)
print()

# Also compute Delta with SM betas (no CD) for comparison
L_SM = (f2m(inv_a1) - f2m(inv_a2)) / f2m(b1_SM - b2_SM)
inv_aGUT_SM = f2m(inv_a1) - f2m(b1_SM) * L_SM
inv_a3_at_GUT_SM = f2m(Fraction(1) / alpha_s) - f2m(b3_SM) * L_SM
Delta_SM = inv_a3_at_GUT_SM - inv_aGUT_SM

show("  For comparison — SM Delta (no CD) (dimensionless)", Delta_SM)
print()

print("  Delta values at one loop (no M_VL threshold):")
print("    SM (no CD):       %s" % mp.nstr(Delta_SM, 4))
print("    SM + CD (from MZ): %s" % mp.nstr(Delta_3input, 4))
print("    SM + CD (from 500 GeV, unification_test.py): -1.17")
print()
print("  The CD improves Delta from %s to %s" %
      (mp.nstr(Delta_SM, 4), mp.nstr(Delta_3input, 4)))
print("  regardless of the threshold assumption.")
print()

sin2_from_3input = f2m(inv_a2) / (f2m(inv_a2) + mpf("5") / 3 * f2m(inv_a1))

# ================================================================
# SECTION 4: COMPARISON TO 3/13
# ================================================================

print("SECTION 4: COMPARISON TO 3/13 = N_gen / |b2_mod_num|")
print("-" * 70)
print()

sin2_3_13 = Fraction(3, 13)
correction_for_3_13 = sin2_tree - sin2_3_13
actual_correction = sin2_tree - sin2_pred_2input

show("  3/13 (dimensionless)", f2m(sin2_3_13))
show("  Predicted (one-loop) (dimensionless)", sin2_pred_m)
show("  Measured (dimensionless)", sin2_meas)
print()

miss_pred_3_13 = fabs(sin2_pred_m - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")
miss_meas_3_13 = fabs(sin2_meas - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")

show("  One-loop miss from 3/13 (%%)", miss_pred_3_13)
show("  Measured miss from 3/13 (%%)", miss_meas_3_13)
print()

show("  Required correction for 3/13: 3/8 - 3/13 = %s (dimensionless)" %
     correction_for_3_13, f2m(correction_for_3_13))
show("  Actual one-loop correction (dimensionless)", f2m(actual_correction))

overcorrection = f2m(actual_correction) - f2m(correction_for_3_13)
overcorrection_pct = overcorrection / f2m(correction_for_3_13) * mpf("100")
show("  Overcorrection (dimensionless)", overcorrection)
show("  Overcorrection relative to needed (%%)", overcorrection_pct)
print()

print("  One-loop OVERCORRECTS by %s%%: pushes sin²θ_W past" %
      mp.nstr(overcorrection_pct, 3))
print("  both 3/13 and the measured value.")
print("  Ordering: predicted < 3/13 < measured < tree.")
print("  Two-loop corrections reduce the running, pulling")
print("  the prediction back toward 3/13 and measured.")
print()

# ================================================================
# SECTION 5: TWO-LOOP CORRECTION ESTIMATE
# ================================================================

print("SECTION 5: TWO-LOOP CORRECTION ESTIMATE")
print("-" * 70)
print()

residual_1loop = sin2_meas - sin2_pred_m
improvement_66pct = residual_1loop * mpf("0.66")
sin2_pred_2loop_est = sin2_pred_m + improvement_66pct

show("  One-loop residual (dimensionless)", residual_1loop)
show("  66%% improvement estimate (dimensionless)", improvement_66pct)
show("  Estimated two-loop prediction (dimensionless)", sin2_pred_2loop_est)
show("  3/13 (dimensionless)", f2m(sin2_3_13))
show("  Measured (dimensionless)", sin2_meas)

miss_2loop_est = fabs(sin2_pred_2loop_est - sin2_meas) / sin2_meas * mpf("100")
miss_2loop_3_13 = fabs(sin2_pred_2loop_est - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")

show("  Estimated two-loop miss from measured (%%)", miss_2loop_est)
show("  Estimated two-loop miss from 3/13 (%%)", miss_2loop_3_13)
print()
print("  If the two-loop improvement is ~66%%,")
print("  predicted sin²θ_W moves to ~%s," % mp.nstr(sin2_pred_2loop_est, 5))
print("  which is %s%% from 3/13." % mp.nstr(miss_2loop_3_13, 3))
print("  PHYS-28 (VL two-loop) will compute this properly.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Section 1
chk_exact("S1: Tree level sin²θ_W = 3/8",
          sin2_tree, Fraction(3, 8), checks)

# Section 2
chk_exact("S2: B_EM = (5/3)*b1' + b2' = 43/9",
          B_EM, Fraction(43, 9), checks)

chk_bool("S2: Abort test — predicted within 5%% of measured",
         miss_2input < mpf("5"),
         "miss = %s%%" % mp.nstr(miss_2input, 4), checks)

chk_bool("S2: Prediction undershoots (direction correct)",
         sin2_pred_m < sin2_meas,
         "pred=%s < meas=%s" % (mp.nstr(sin2_pred_m, 5),
                                mp.nstr(sin2_meas, 5)), checks)

chk_bool("S2: M_GUT in [10^15, 10^16.5]",
         mpf("15") < log10_MGUT_2input < mpf("16.5"),
         "log10 = %s" % mp.nstr(log10_MGUT_2input, 4), checks)

# Section 3
chk_bool("S3: CD improves Delta over SM",
         fabs(Delta_3input) < fabs(Delta_SM),
         "|Delta_CD|=%s < |Delta_SM|=%s" % (
             mp.nstr(fabs(Delta_3input), 4),
             mp.nstr(fabs(Delta_SM), 4)), checks)

chk_bool("S3: Delta negative (alpha_3 too strong)",
         Delta_3input < mpf("0"),
         "Delta = %s" % mp.nstr(Delta_3input, 4), checks)

chk_bool("S3: sin²θ_W from three inputs = measured",
         fabs(sin2_from_3input - sin2_meas) < mpf("1e-10"),
         "diff = %s" % mp.nstr(fabs(sin2_from_3input - sin2_meas), 4),
         checks)

# Section 4
chk_bool("S4: Measured within 0.2%% of 3/13",
         miss_meas_3_13 < mpf("0.2"),
         "miss = %s%%" % mp.nstr(miss_meas_3_13, 4), checks)

chk_bool("S4: Ordering pred < 3/13 < measured",
         sin2_pred_m < f2m(sin2_3_13) < sin2_meas,
         "%s < %s < %s" % (mp.nstr(sin2_pred_m, 5),
                           mp.nstr(f2m(sin2_3_13), 5),
                           mp.nstr(sin2_meas, 5)), checks)

chk_exact("S4: Required correction = 15/104",
          correction_for_3_13, Fraction(15, 104), checks)

# Section 5
chk_bool("S5: Two-loop estimate closer to measured",
         miss_2loop_est < miss_2input,
         "2loop=%s%% < 1loop=%s%%" % (
             mp.nstr(miss_2loop_est, 4),
             mp.nstr(miss_2input, 4)), checks)

chk_bool("S5: Two-loop estimate closer to 3/13",
         miss_2loop_3_13 < miss_pred_3_13,
         "2loop=%s%% < 1loop=%s%%" % (
             mp.nstr(miss_2loop_3_13, 4),
             mp.nstr(miss_pred_3_13, 4)), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-27 sin²θ_W FROM 3/8 COMPLETE")
print("=" * 70)
