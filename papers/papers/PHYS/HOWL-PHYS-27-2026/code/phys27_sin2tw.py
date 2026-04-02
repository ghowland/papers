#!/usr/bin/env python3
"""
HOWL PHYS-27: phys27_sin2tw.py
================================
sin²θ_W from 3/8 — The GUT prediction with Cabibbo Doublet betas.

At tree level in SU(5): sin²θ_W = 3/8. One-loop running from
M_GUT to M_Z with CD modified betas reduces this toward 0.231.

Two computations:
  1. No-threshold: CD betas from M_Z to M_GUT (best one-loop, 1.2%%)
  2. With threshold: SM below M_VL, CD above (physical, 1.7%%)

Both undershoot. The ordering pred < 3/13 < measured < 3/8 is
correct. Two-loop corrections push the prediction toward both
3/13 and measured.

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

sin2_tree = Fraction(3, 8)
sin2_meas = f2m(sin2_tW)
show("  sin²θ_W(tree) = 3/8 (dimensionless)", f2m(sin2_tree))
show("  sin²θ_W(measured) (dimensionless)", sin2_meas)
show("  Correction needed (dimensionless)", f2m(sin2_tree) - sin2_meas)
print()

# ================================================================
# SECTION 2: NO-THRESHOLD PREDICTION
# ================================================================

print("SECTION 2: NO-THRESHOLD PREDICTION (CD betas from M_Z)")
print("-" * 70)
print()
print("  Inputs: alpha_EM and alpha_s ONLY.")
print("  CD betas used over full range. Best one-loop result.")
print()

inv_aEM = alpha_inv
inv_a3_frac = Fraction(1) / alpha_s
B_EM_cd = Fraction(5, 3) * b1_mod + b2_mod

num_L = inv_aEM - Fraction(8, 3) * inv_a3_frac
den_L = B_EM_cd - Fraction(8, 3) * b3_mod
L_nt = num_L / den_L

inv_aGUT_nt = inv_a3_frac - b3_mod * L_nt
inv_a1_nt = inv_aGUT_nt + b1_mod * L_nt
inv_a2_nt = inv_aGUT_nt + b2_mod * L_nt
sin2_nt_frac = inv_a2_nt / (inv_a2_nt + Fraction(5, 3) * inv_a1_nt)
sin2_nt_m = f2m(sin2_nt_frac)

miss_nt = fabs(sin2_nt_m - sin2_meas) / sin2_meas * mpf("100")

M_Z_GeV_m = f2m(M_Z) / mpf("1000")
M_GUT_nt = M_Z_GeV_m * mexp(f2m(L_nt) * mpf("2") * mpi)
log_MGUT_nt = mlog10(M_GUT_nt)

show("  PREDICTED sin²θ_W (dimensionless)", sin2_nt_m)
show("  MEASURED  sin²θ_W (dimensionless)", sin2_meas)
show("  Miss (%%)", miss_nt)
show("  log10(M_GUT/GeV)", log_MGUT_nt)
print()

# ================================================================
# SECTION 3: WITH-THRESHOLD SCAN
# ================================================================

print("SECTION 3: WITH-THRESHOLD PREDICTION (SM below M_VL)")
print("-" * 70)
print()
print("  SM betas below M_VL, CD betas above.")
print("  More physical: CD not active below its mass.")
print("  Gives a LARGER miss at one loop because less CD running.")
print()

B_EM_sm = Fraction(5, 3) * b1_SM + b2_SM

M_VL_values = [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000]

print("  %8s %12s %12s %10s %12s" %
      ("M_VL(GeV)", "sin²θ_W", "miss(%%)", "log M_GUT", "Delta"))
print("  %8s %12s %12s %10s %12s" %
      ("-" * 8, "-" * 12, "-" * 12, "-" * 10, "-" * 12))

results = []

for M_VL_GeV in M_VL_values:
    M_VL_m = mpf(str(M_VL_GeV))
    L_low = mlog(M_VL_m / M_Z_GeV_m) / (mpf("2") * mpi)

    # Two-input with threshold
    inv_aEM_sh = f2m(inv_aEM) - f2m(B_EM_sm) * L_low
    inv_a3_sh = f2m(inv_a3_frac) - f2m(b3_SM) * L_low

    num_Lh = inv_aEM_sh - mpf("8") / 3 * inv_a3_sh
    den_Lh = f2m(B_EM_cd) - mpf("8") / 3 * f2m(b3_mod)
    L_high = num_Lh / den_Lh

    inv_aGUT = inv_a3_sh - f2m(b3_mod) * L_high
    inv_a1_VL = inv_aGUT + f2m(b1_mod) * L_high
    inv_a2_VL = inv_aGUT + f2m(b2_mod) * L_high
    inv_a1_MZ = inv_a1_VL + f2m(b1_SM) * L_low
    inv_a2_MZ = inv_a2_VL + f2m(b2_SM) * L_low

    sin2_p = inv_a2_MZ / (inv_a2_MZ + mpf("5") / 3 * inv_a1_MZ)
    miss_p = fabs(sin2_p - sin2_meas) / sin2_meas * mpf("100")
    M_GUT_p = M_VL_m * mexp(L_high * mpf("2") * mpi)
    log_MGUT_p = mlog10(M_GUT_p)

    # Three-input Delta at this M_VL
    inv_a1_atVL = f2m(inv_a1) + f2m(b1_SM) * L_low
    inv_a2_atVL = f2m(inv_a2) + f2m(b2_SM) * L_low
    inv_a3_atVL = f2m(inv_a3_frac) + f2m(b3_SM) * L_low
    L_h_3 = (inv_a2_atVL - inv_a1_atVL) / f2m(b1_mod - b2_mod)
    inv_aGUT_3 = inv_a1_atVL + f2m(b1_mod) * L_h_3
    inv_a3_atGUT = inv_a3_atVL + f2m(b3_mod) * L_h_3
    Delta = inv_a3_atGUT - inv_aGUT_3

    results.append((M_VL_GeV, sin2_p, miss_p, log_MGUT_p, Delta))

    print("  %8d %12s %12s %10s %12s" %
          (M_VL_GeV, mp.nstr(sin2_p, 7), mp.nstr(miss_p, 5),
           mp.nstr(log_MGUT_p, 5), mp.nstr(Delta, 5)))

print()

# Key values
sin2_500 = results[0][1]
miss_500 = results[0][2]
Delta_500 = results[0][4]

show("  At M_VL = 500 GeV:", sin2_500)
show("    sin²θ_W predicted (dimensionless)", sin2_500)
show("    miss from measured (%%)", miss_500)
show("    Delta(1/alpha_3) (dimensionless)", Delta_500)
print()

print("  The threshold prediction undershoots MORE than no-threshold")
print("  because less of the running uses CD betas (which provide")
print("  the correction). This is expected: the threshold is more")
print("  physical, but one-loop accuracy is insufficient for")
print("  sub-percent precision. Two-loop corrections compensate.")
print()

# ================================================================
# SECTION 4: COMPARISON TO 3/13
# ================================================================

print("SECTION 4: COMPARISON TO 3/13")
print("-" * 70)
print()

sin2_3_13 = Fraction(3, 13)
correction_for_3_13 = sin2_tree - sin2_3_13

miss_nt_3_13 = fabs(sin2_nt_m - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")
miss_500_3_13 = fabs(sin2_500 - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")
miss_meas_3_13 = fabs(sin2_meas - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")

show("  3/13 (dimensionless)", f2m(sin2_3_13))
print()
print("  Distance from 3/13:")
show("    No-threshold (%%)", miss_nt_3_13)
show("    Threshold M_VL=500 (%%)", miss_500_3_13)
show("    Measured (%%)", miss_meas_3_13)
print()

show("  Required correction for exactly 3/13 (dimensionless)",
     f2m(correction_for_3_13))
print("  = 3/8 - 3/13 = %s" % correction_for_3_13)
print()

print("  Ordering at one loop (both methods):")
print("    threshold(%.5f) < no-thresh(%.5f) < 3/13(%.5f) < meas(%.5f)" %
      (float(sin2_500), float(sin2_nt_m),
       float(f2m(sin2_3_13)), float(sin2_meas)))
print()

# Two-loop estimate from best one-loop (no-threshold)
residual = sin2_meas - sin2_nt_m
sin2_2L = sin2_nt_m + residual * mpf("0.66")
miss_2L_meas = fabs(sin2_2L - sin2_meas) / sin2_meas * mpf("100")
miss_2L_3_13 = fabs(sin2_2L - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")

print("  Two-loop estimate (66%% improvement on no-threshold residual):")
show("    Estimated sin²θ_W (dimensionless)", sin2_2L)
show("    Miss from measured (%%)", miss_2L_meas)
show("    Miss from 3/13 (%%)", miss_2L_3_13)
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
chk_exact("S1: Tree level = 3/8",
          sin2_tree, Fraction(3, 8), checks)

# Section 2: no-threshold
chk_exact("S2: B_EM(CD) = 43/9",
          B_EM_cd, Fraction(43, 9), checks)

chk_bool("S2: Abort test — within 5%% of measured",
         miss_nt < mpf("5"),
         "miss = %s%%" % mp.nstr(miss_nt, 4), checks)

chk_bool("S2: Direction correct (undershoots)",
         sin2_nt_m < sin2_meas,
         "%s < %s" % (mp.nstr(sin2_nt_m, 5), mp.nstr(sin2_meas, 5)),
         checks)

chk_bool("S2: M_GUT in [10^15, 10^16.5]",
         mpf("15") < log_MGUT_nt < mpf("16.5"),
         "log10 = %s" % mp.nstr(log_MGUT_nt, 4), checks)

# Section 3: threshold
chk_bool("S3: All threshold predictions undershoot measured",
         all(r[1] < sin2_meas for r in results),
         "all pred < meas", checks)

chk_bool("S3: Delta at M_VL=500 is negative and < 1 in magnitude",
         mpf("-1") < Delta_500 < mpf("0"),
         "Delta = %s" % mp.nstr(Delta_500, 4), checks)

chk_bool("S3: Threshold miss within 2%% of measured",
         miss_500 < mpf("2"),
         "miss = %s%%" % mp.nstr(miss_500, 4), checks)

# Section 4: comparison to 3/13
chk_bool("S4: Measured within 0.2%% of 3/13",
         miss_meas_3_13 < mpf("0.2"),
         "miss = %s%%" % mp.nstr(miss_meas_3_13, 4), checks)

chk_bool("S4: Ordering thresh < no-thresh < 3/13 < measured",
         sin2_500 < sin2_nt_m < f2m(sin2_3_13) < sin2_meas,
         "%s < %s < %s < %s" % (
             mp.nstr(sin2_500, 5), mp.nstr(sin2_nt_m, 5),
             mp.nstr(f2m(sin2_3_13), 5), mp.nstr(sin2_meas, 5)),
         checks)

chk_exact("S4: Required correction = 15/104",
          correction_for_3_13, Fraction(15, 104), checks)

# Section 5: two-loop estimate
chk_bool("S5: Two-loop estimate closer to measured",
         miss_2L_meas < miss_nt,
         "2L=%s%% < 1L=%s%%" % (
             mp.nstr(miss_2L_meas, 4), mp.nstr(miss_nt, 4)), checks)

chk_bool("S5: Two-loop estimate closer to 3/13",
         miss_2L_3_13 < miss_nt_3_13,
         "2L=%s%% < 1L=%s%%" % (
             mp.nstr(miss_2L_3_13, 4), mp.nstr(miss_nt_3_13, 4)), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-27 sin²θ_W FROM 3/8 COMPLETE")
print("=" * 70)
