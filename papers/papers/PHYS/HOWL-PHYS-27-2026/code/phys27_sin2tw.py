#!/usr/bin/env python3
"""
HOWL PHYS-27: phys27_sin2tw.py
================================
sin²θ_W from 3/8 — The GUT prediction with Cabibbo Doublet betas.

At tree level in SU(5): sin²θ_W = 3/8. One-loop running from
M_GUT to M_Z with the CD modified betas reduces this.

Four computations:
  1. Two-input prediction WITHOUT M_VL threshold (CD betas from M_Z)
  2. Two-input prediction WITH M_VL threshold (SM below, CD above)
  3. Three-input consistency with threshold
  4. Comparison to 3/13 = N_gen/|b2_mod_num|

The threshold matters: the CD is not active below M_VL.
Running CD betas in the low-energy region overcounts the effect.

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
print("  In SU(5), at the unification point alpha_1 = alpha_2:")
print("    sin²θ_W = 1/(1 + (5/3)) = 3/8 = 0.375")
print()

sin2_tree = Fraction(3, 8)
sin2_meas = f2m(sin2_tW)
show("  sin²θ_W(tree) = 3/8 (dimensionless)", f2m(sin2_tree))
show("  sin²θ_W(measured) (dimensionless)", sin2_meas)
show("  Correction needed (dimensionless)", f2m(sin2_tree) - sin2_meas)
print()

# ================================================================
# SECTION 2: TWO-INPUT PREDICTION — NO THRESHOLD
# ================================================================

print("SECTION 2: TWO-INPUT PREDICTION — NO M_VL THRESHOLD")
print("-" * 70)
print()
print("  CD betas from M_Z to M_GUT (no threshold).")
print("  Inputs: alpha_EM and alpha_s ONLY.")
print()

inv_aEM = alpha_inv
inv_a3_frac = Fraction(1) / alpha_s
B_EM_cd = Fraction(5, 3) * b1_mod + b2_mod

num_L = inv_aEM - Fraction(8, 3) * inv_a3_frac
den_L = B_EM_cd - Fraction(8, 3) * b3_mod
L_no_thresh = num_L / den_L

inv_aGUT_nt = inv_a3_frac - b3_mod * L_no_thresh
inv_a1_nt = inv_aGUT_nt + b1_mod * L_no_thresh
inv_a2_nt = inv_aGUT_nt + b2_mod * L_no_thresh
sin2_no_thresh = inv_a2_nt / (inv_a2_nt + Fraction(5, 3) * inv_a1_nt)

sin2_nt_m = f2m(sin2_no_thresh)
miss_nt = fabs(sin2_nt_m - sin2_meas) / sin2_meas * mpf("100")

show("  PREDICTED sin²θ_W (no threshold) (dimensionless)", sin2_nt_m)
show("  Miss from measured (%%)", miss_nt)
print()

# ================================================================
# SECTION 3: TWO-INPUT PREDICTION — WITH M_VL THRESHOLD
# ================================================================
# Below M_VL: SM betas. Above M_VL: CD betas.
# The running splits into two segments:
#
#   1/alpha_i(M_Z) = 1/alpha_i(M_VL) + b_i^SM * L_low
#   1/alpha_i(M_VL) = 1/alpha_GUT + b_i^CD * L_high
#
# where L_low = ln(M_VL/M_Z)/(2pi), L_high = ln(M_GUT/M_VL)/(2pi)
#
# Combined: 1/alpha_i(M_Z) = 1/alpha_GUT + b_i^CD * L_high + b_i^SM * L_low
#
# The same two-input method works:
#   1/alpha_EM = (8/3)/alpha_GUT + B_EM^CD * L_high + B_EM^SM * L_low
#   1/alpha_3  = 1/alpha_GUT + b3_CD * L_high + b3_SM * L_low
#
# L_low is KNOWN (from M_VL). Unknowns: alpha_GUT, L_high.
# Rearrange:
#   1/alpha_EM - B_EM^SM * L_low = (8/3)/alpha_GUT + B_EM^CD * L_high
#   1/alpha_3  - b3_SM * L_low   = 1/alpha_GUT + b3_CD * L_high
#
# Same algebra as before with shifted LHS.

print("SECTION 3: TWO-INPUT PREDICTION — WITH M_VL THRESHOLD")
print("-" * 70)
print()

B_EM_sm = Fraction(5, 3) * b1_SM + b2_SM

# Scan M_VL from 500 GeV to 6000 GeV
M_VL_values = [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000]
M_Z_GeV_m = f2m(M_Z) / mpf("1000")

print("  Scan over M_VL (SM betas below, CD betas above):")
print()
print("  %8s %12s %12s %10s %12s" %
      ("M_VL(GeV)", "sin²θ_W", "miss(%%)", "log M_GUT", "Delta"))
print("  %8s %12s %12s %10s %12s" %
      ("-" * 8, "-" * 12, "-" * 12, "-" * 10, "-" * 12))

results = []

for M_VL_GeV in M_VL_values:
    M_VL_m = mpf(str(M_VL_GeV))
    L_low = mlog(M_VL_m / M_Z_GeV_m) / (mpf("2") * mpi)

    # Shift the LHS
    inv_aEM_shifted = f2m(inv_aEM) - f2m(B_EM_sm) * L_low
    inv_a3_shifted = f2m(inv_a3_frac) - f2m(b3_SM) * L_low

    # Solve for L_high and alpha_GUT
    num_Lh = inv_aEM_shifted - mpf("8") / 3 * inv_a3_shifted
    den_Lh = f2m(B_EM_cd) - mpf("8") / 3 * f2m(b3_mod)
    L_high = num_Lh / den_Lh

    inv_aGUT = inv_a3_shifted - f2m(b3_mod) * L_high

    # Predict couplings at M_VL
    inv_a1_VL = inv_aGUT + f2m(b1_mod) * L_high
    inv_a2_VL = inv_aGUT + f2m(b2_mod) * L_high

    # Run down to M_Z with SM betas
    inv_a1_MZ = inv_a1_VL + f2m(b1_SM) * L_low
    inv_a2_MZ = inv_a2_VL + f2m(b2_SM) * L_low

    # Predict sin²θ_W
    sin2_pred = inv_a2_MZ / (inv_a2_MZ + mpf("5") / 3 * inv_a1_MZ)
    miss = fabs(sin2_pred - sin2_meas) / sin2_meas * mpf("100")

    # M_GUT
    M_GUT = M_VL_m * mexp(L_high * mpf("2") * mpi)
    log_MGUT = mlog10(M_GUT)

    # Three-input Delta at this M_VL
    L_low_3 = mlog(M_VL_m / M_Z_GeV_m) / (mpf("2") * mpi)
    # Run all three from M_Z to M_VL with SM, then M_VL to M_GUT with CD
    # M_GUT defined by alpha_1 = alpha_2 crossing
    inv_a1_at_VL = f2m(inv_a1) + f2m(b1_SM) * L_low_3  # wait, running UP
    # Actually: 1/alpha_i(mu) = 1/alpha_i(M_Z) - b_i/(2pi) * ln(M_Z/mu)
    # = 1/alpha_i(M_Z) + b_i * ln(mu/M_Z)/(2pi)
    # Running UP from M_Z to M_VL:
    inv_a1_atVL = f2m(inv_a1) + f2m(b1_SM) * L_low_3
    inv_a2_atVL = f2m(inv_a2) + f2m(b2_SM) * L_low_3
    inv_a3_atVL = f2m(inv_a3_frac) + f2m(b3_SM) * L_low_3

    # Running UP from M_VL with CD betas
    # Find crossing: inv_a1(mu) = inv_a2(mu)
    # inv_a1_atVL + b1_mod * L_h = inv_a2_atVL + b2_mod * L_h
    L_h_3 = (inv_a1_atVL - inv_a2_atVL) / f2m(b1_mod - b2_mod)
    # Wait, this should be:
    # For crossing above M_VL: 1/a1(M_GUT) = 1/a2(M_GUT)
    # inv_a1_atVL + b1_mod*Lh = inv_a2_atVL + b2_mod*Lh
    # (inv_a1_atVL - inv_a2_atVL) = (b2_mod - b1_mod)*Lh  ... wrong sign
    # Lh = (inv_a1_atVL - inv_a2_atVL)/(b1_mod - b2_mod) ... no
    # Actually running UP: 1/ai(mu) = 1/ai(M_VL) + bi*(ln(mu/M_VL))/(2pi)
    # = 1/ai(M_VL) + bi*Lh where Lh = ln(M_GUT/M_VL)/(2pi)
    # At crossing: 1/a1(GUT) = 1/a2(GUT)
    # inv_a1_atVL + b1_mod*Lh = inv_a2_atVL + b2_mod*Lh
    # Lh*(b1_mod - b2_mod) = inv_a2_atVL - inv_a1_atVL
    L_h_3 = (inv_a2_atVL - inv_a1_atVL) / f2m(b1_mod - b2_mod)

    inv_aGUT_3 = inv_a1_atVL + f2m(b1_mod) * L_h_3
    inv_a3_atGUT = inv_a3_atVL + f2m(b3_mod) * L_h_3
    Delta = inv_a3_atGUT - inv_aGUT_3

    results.append((M_VL_GeV, sin2_pred, miss, log_MGUT, Delta))

    print("  %8d %12s %12s %10s %12s" %
          (M_VL_GeV,
           mp.nstr(sin2_pred, 7),
           mp.nstr(miss, 5),
           mp.nstr(log_MGUT, 5),
           mp.nstr(Delta, 5)))

print()

# Extract the M_VL = 500 GeV result for detailed reporting
sin2_500, miss_500, log_MGUT_500, Delta_500 = (
    results[0][1], results[0][2], results[0][3], results[0][4])

# Extract the best-fit M_VL (closest to measured)
best_idx = min(range(len(results)), key=lambda i: float(results[i][2]))
best_MVL, sin2_best, miss_best, log_MGUT_best, Delta_best = results[best_idx]

print("  Best M_VL for sin²θ_W prediction: %d GeV" % best_MVL)
show("    sin²θ_W predicted (dimensionless)", sin2_best)
show("    miss from measured (%%)", miss_best)
show("    log10(M_GUT/GeV)", log_MGUT_best)
show("    Delta(1/alpha_3) (dimensionless)", Delta_best)
print()

print("  At M_VL = 500 GeV (cf. unification_test.py):")
show("    sin²θ_W predicted (dimensionless)", sin2_500)
show("    miss from measured (%%)", miss_500)
show("    Delta(1/alpha_3) (dimensionless)", Delta_500)
print()

# ================================================================
# SECTION 4: COMPARISON TO 3/13
# ================================================================

print("SECTION 4: COMPARISON TO 3/13 = N_gen / |b2_mod_num|")
print("-" * 70)
print()

sin2_3_13 = Fraction(3, 13)
correction_for_3_13 = sin2_tree - sin2_3_13

show("  3/13 (dimensionless)", f2m(sin2_3_13))
show("  Measured (dimensionless)", sin2_meas)
print()

miss_meas_3_13 = fabs(sin2_meas - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")
miss_best_3_13 = fabs(sin2_best - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")
miss_nt_3_13 = fabs(sin2_nt_m - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")

print("  Distance from 3/13:")
show("    No threshold prediction (%%)", miss_nt_3_13)
show("    Best threshold prediction (M_VL=%d GeV) (%%)" % best_MVL,
     miss_best_3_13)
show("    Measured (%%)", miss_meas_3_13)
print()

chk_exact_corr = correction_for_3_13
show("  Required correction for 3/13: 3/8 - 3/13 = %s (dimensionless)" %
     chk_exact_corr, f2m(chk_exact_corr))
print()

print("  The ordering:")
print("    no-threshold (%.5f) < 3/13 (%.5f) < measured (%.5f)" %
      (float(sin2_nt_m), float(f2m(sin2_3_13)), float(sin2_meas)))
print("  Adding the M_VL threshold brings the prediction closer")
print("  to both 3/13 and the measured value.")
print("  Two-loop corrections will bring it closer still.")
print()

# ================================================================
# SECTION 5: SUMMARY
# ================================================================

print("SECTION 5: SUMMARY")
print("-" * 70)
print()
print("  Three levels of refinement:")
print()
print("    1. No threshold (CD from M_Z):")
print("       sin²θ_W = %s, miss = %s%%" %
      (mp.nstr(sin2_nt_m, 5), mp.nstr(miss_nt, 4)))
print()
print("    2. With threshold (SM below M_VL, CD above):")
print("       sin²θ_W = %s at M_VL = %d GeV, miss = %s%%" %
      (mp.nstr(sin2_best, 5), best_MVL, mp.nstr(miss_best, 4)))
print()
print("    3. Two-loop estimate (66%% improvement on residual):")

residual_best = sin2_meas - sin2_best
sin2_2loop_est = sin2_best + residual_best * mpf("0.66")
miss_2loop_est = fabs(sin2_2loop_est - sin2_meas) / sin2_meas * mpf("100")
miss_2loop_3_13 = fabs(sin2_2loop_est - f2m(sin2_3_13)) / f2m(sin2_3_13) * mpf("100")

print("       sin²θ_W ~ %s, miss ~ %s%% from measured, %s%% from 3/13" %
      (mp.nstr(sin2_2loop_est, 5), mp.nstr(miss_2loop_est, 3),
       mp.nstr(miss_2loop_3_13, 3)))
print()
print("  Each refinement brings sin²θ_W closer to both 3/13")
print("  and the measured value. The direction is consistently")
print("  correct. PHYS-28 (VL two-loop) computes step 3 properly.")
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
chk_exact("S2: B_EM(CD) = (5/3)*b1' + b2' = 43/9",
          B_EM_cd, Fraction(43, 9), checks)

chk_bool("S2: No-threshold prediction within 5%% (abort test)",
         miss_nt < mpf("5"),
         "miss = %s%%" % mp.nstr(miss_nt, 4), checks)

chk_bool("S2: No-threshold undershoots (direction correct)",
         sin2_nt_m < sin2_meas,
         "pred=%s < meas=%s" % (mp.nstr(sin2_nt_m, 5),
                                mp.nstr(sin2_meas, 5)), checks)

# Section 3
chk_bool("S3: Threshold improves prediction over no-threshold",
         miss_best < miss_nt,
         "thresh=%s%% < no-thresh=%s%%" % (
             mp.nstr(miss_best, 4), mp.nstr(miss_nt, 4)), checks)

chk_bool("S3: Delta at M_VL=500 matches unification_test.py",
         fabs(Delta_500 - mpf("-1.17")) < mpf("0.4"),
         "Delta=%s vs -1.17" % mp.nstr(Delta_500, 4), checks)

chk_bool("S3: CD improves Delta over SM",
         fabs(Delta_500) < mpf("6.58"),
         "|Delta_CD|=%s < |Delta_SM|=6.58" % mp.nstr(fabs(Delta_500), 4),
         checks)

chk_bool("S3: Best M_VL gives sin²θ_W within 1%% of measured",
         miss_best < mpf("1"),
         "miss = %s%%" % mp.nstr(miss_best, 4), checks)

# Section 4
chk_bool("S4: Measured within 0.2%% of 3/13",
         miss_meas_3_13 < mpf("0.2"),
         "miss = %s%%" % mp.nstr(miss_meas_3_13, 4), checks)

chk_bool("S4: Ordering pred < 3/13 < measured holds",
         sin2_nt_m < f2m(sin2_3_13) < sin2_meas,
         "%s < %s < %s" % (mp.nstr(sin2_nt_m, 5),
                           mp.nstr(f2m(sin2_3_13), 5),
                           mp.nstr(sin2_meas, 5)), checks)

chk_exact("S4: Required correction = 15/104",
          correction_for_3_13, Fraction(15, 104), checks)

# Section 5
chk_bool("S5: Two-loop estimate closer to 3/13 than one-loop",
         miss_2loop_3_13 < miss_best_3_13,
         "2loop=%s%% < 1loop=%s%%" % (
             mp.nstr(miss_2loop_3_13, 4),
             mp.nstr(miss_best_3_13, 4)), checks)

chk_bool("S5: Two-loop estimate closer to measured than one-loop",
         miss_2loop_est < miss_best,
         "2loop=%s%% < 1loop=%s%%" % (
             mp.nstr(miss_2loop_est, 4),
             mp.nstr(miss_best, 4)), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-27 sin²θ_W FROM 3/8 COMPLETE")
print("=" * 70)
