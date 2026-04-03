#!/usr/bin/env python3
"""
HOWL PHYS-30: phys30_alpha_s.py
=================================
alpha_s Prediction from Unification.

Uses the unification condition (alpha_1 = alpha_2 = alpha_3 at M_GUT)
with CD modified betas to PREDICT alpha_s(M_Z) from only alpha_EM
and sin2_tW as inputs.

The method: alpha_EM and sin2_tW determine alpha_1 and alpha_2 at M_Z.
The CD betas determine M_GUT (where alpha_1 = alpha_2 cross).
At M_GUT, alpha_3 = alpha_GUT (unification condition).
Running alpha_3 back down to M_Z with the CD betas PREDICTS alpha_s.

SIGN CONVENTION (from PHYS-28):
  d(1/alpha_i)/d(ln mu) = -b_i/(2pi)
  1/alpha_i(mu) = 1/alpha_i(mu0) - b_i * L, L = ln(mu/mu0)/(2pi)

Backed by: phys28_vl_twoloop.py (11/11), phys27_sin2tw.py (13/13)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, fabs
from mpmath import log10 as mlog10

# ================================================================
print("=" * 70)
print("HOWL PHYS-30: alpha_s PREDICTION FROM UNIFICATION")
print("Does the unification condition predict the right alpha_s?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: THE INPUTS
# ================================================================

print("SECTION 1: THE TWO INPUTS")
print("-" * 70)
print()
print("  Input 1: alpha_EM = 1/%s (DATA-4 B1, 12 digits)" %
      mp.nstr(f2m(alpha_inv), 12))
print("  Input 2: sin2_tW  = %s (DATA-4 B11, 5 digits)" %
      mp.nstr(f2m(sin2_tW), 5))
print()
print("  From these two, compute alpha_1 and alpha_2 at M_Z:")
print()

# alpha_1 and alpha_2 from alpha_EM and sin2_tW
# sin2_tW = alpha_EM / alpha_2  =>  alpha_2 = alpha_EM / sin2_tW
# 1/alpha_EM = (5/3)/alpha_1 + 1/alpha_2
# => (5/3)/alpha_1 = 1/alpha_EM - 1/alpha_2
# => 1/alpha_1 = (3/5) * (1/alpha_EM - 1/alpha_2)

inv_a2_input = alpha_inv / sin2_tW          # Fraction
inv_a1_input = Fraction(3, 5) * (alpha_inv - inv_a2_input)   # Fraction

show("  1/alpha_1(M_Z) (dimensionless)", f2m(inv_a1_input))
show("  1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2_input))
print()

# Verify these match the library values
show("  Library 1/alpha_1 (dimensionless)", f2m(inv_a1))
show("  Library 1/alpha_2 (dimensionless)", f2m(inv_a2))
print()

twopi = mpf("2") * mpi
b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]

# ================================================================
# SECTION 2: ONE-LOOP PREDICTION
# ================================================================

print("SECTION 2: ONE-LOOP PREDICTION")
print("-" * 70)
print()
print("  Method: run alpha_1 and alpha_2 to crossing with CD betas.")
print("  At crossing: alpha_GUT determined. Predict alpha_3 by")
print("  running alpha_GUT back down to M_Z.")
print()

# Step 1: SM betas from M_Z to M_VL
M_Z_GeV_m = f2m(M_Z) / mpf("1000")
M_VL_m = mpf("500")
L_low = mlog(M_VL_m / M_Z_GeV_m) / twopi

inv_a1_VL = f2m(inv_a1_input) - b_SM_m[0] * L_low
inv_a2_VL = f2m(inv_a2_input) - b_SM_m[1] * L_low

show("  1/alpha_1(M_VL) (dimensionless)", inv_a1_VL)
show("  1/alpha_2(M_VL) (dimensionless)", inv_a2_VL)
print()

# Step 2: CD betas from M_VL to crossing
L_cross = (inv_a1_VL - inv_a2_VL) / (b_CD_m[1] - b_CD_m[0])
# Wait: the sign. Running UP: 1/a(mu) = 1/a(mu0) - b*L
# At crossing: inv_a1_VL - b1*L = inv_a2_VL - b2*L
# L*(b1 - b2) = inv_a1_VL - inv_a2_VL  ... no
# inv_a1_VL - b1*L = inv_a2_VL - b2*L
# inv_a1_VL - inv_a2_VL = b1*L - b2*L = (b1 - b2)*L
# L = (inv_a1_VL - inv_a2_VL) / (b1 - b2)
# b1 - b2 = 25/6 - (-13/6) = 38/6 > 0
# inv_a1 - inv_a2 = 62.1 - 32.5 = 29.6 > 0 (since alpha_1 < alpha_2... wait)
# Actually: inv_a1 > inv_a2 (63 > 31), and b1 > b2 (4.17 > -2.17)
# b1 > 0 means 1/a1 DECREASES running up. b2 < 0 means 1/a2 INCREASES.
# So the gap closes. L should be positive.
# L = (inv_a1_VL - inv_a2_VL) / (b1_CD - b2_CD)
# = positive / positive = positive. Good.

L_cross = (inv_a1_VL - inv_a2_VL) / (b_CD_m[0] - b_CD_m[1])
inv_aGUT = inv_a1_VL - b_CD_m[0] * L_cross
M_GUT = M_VL_m * mexp(L_cross * twopi)

show("  L to crossing (dimensionless)", L_cross)
show("  1/alpha_GUT (dimensionless)", inv_aGUT)
show("  log10(M_GUT/GeV)", mlog10(M_GUT))
print()

# Step 3: Predict alpha_3 by running back down
# From M_GUT to M_VL with CD betas:
# 1/alpha_3(M_VL) = 1/alpha_GUT - b3_CD * (-L_cross)
# = 1/alpha_GUT + b3_CD * L_cross
# (running DOWN: L is negative, so -b*L = -b*(-L_cross) = +b*L_cross)
# Actually: 1/a3(M_VL) = 1/a3(M_GUT) - b3 * L_down
# where L_down = ln(M_VL/M_GUT)/(2pi) = -L_cross
# So: 1/a3(M_VL) = inv_aGUT - b3_CD * (-L_cross) = inv_aGUT + b3_CD * L_cross

inv_a3_VL = inv_aGUT + b_CD_m[2] * L_cross

# From M_VL to M_Z with SM betas:
inv_a3_MZ = inv_a3_VL + b_SM_m[2] * L_low

alpha_s_pred_1loop = mpf("1") / inv_a3_MZ
alpha_s_meas = f2m(alpha_s)

show("  1/alpha_3(M_VL) predicted (dimensionless)", inv_a3_VL)
show("  1/alpha_3(M_Z) predicted (dimensionless)", inv_a3_MZ)
show("  alpha_s predicted (dimensionless)", alpha_s_pred_1loop)
show("  alpha_s measured (dimensionless)", alpha_s_meas)
print()

miss_1loop = fabs(alpha_s_pred_1loop - alpha_s_meas) / alpha_s_meas * mpf("100")
show("  Relative miss (%%)", miss_1loop)
print()

# The uncertainty band: alpha_s = 0.1180 +/- 0.0009
alpha_s_hi = mpf("0.1189")
alpha_s_lo = mpf("0.1171")
within_1sigma = alpha_s_lo < alpha_s_pred_1loop < alpha_s_hi
within_3sigma = mpf("0.1153") < alpha_s_pred_1loop < mpf("0.1207")

print("  Measured: alpha_s = 0.1180 +/- 0.0009")
print("  1-sigma range: [0.1171, 0.1189]")
print("  3-sigma range: [0.1153, 0.1207]")
print("  Predicted: %s" % mp.nstr(alpha_s_pred_1loop, 5))
print("  Within 1-sigma: %s" % within_1sigma)
print("  Within 3-sigma: %s" % within_3sigma)
print()

# ================================================================
# SECTION 3: THE DELTA PERSPECTIVE
# ================================================================

print("SECTION 3: CONNECTION TO DELTA")
print("-" * 70)
print()
print("  The alpha_s prediction is the INVERSE of the Delta test.")
print("  In the Delta test: measured alpha_s runs to M_GUT, misses.")
print("  Here: unification FORCES alpha_3 = alpha_GUT, then runs down.")
print("  The prediction misses the measured alpha_s by the same")
print("  amount that Delta measures at M_GUT.")
print()

# Delta from the three-input test
inv_a3_meas_VL = f2m(Fraction(1) / alpha_s) - b_SM_m[2] * L_low
inv_a3_meas_GUT = inv_a3_meas_VL + b_CD_m[2] * L_cross
Delta = inv_a3_meas_GUT - inv_aGUT

show("  Delta(1/alpha_3) at M_GUT (dimensionless)", Delta)
print()

# The predicted alpha_s corresponds to Delta = 0
# The miss in alpha_s corresponds to the miss in Delta
# delta(1/alpha_s) = delta(1/alpha_3) at M_Z from the Delta
# = Delta propagated down through the running

delta_inv_a3 = inv_a3_MZ - f2m(Fraction(1) / alpha_s)
show("  delta(1/alpha_3) at M_Z (dimensionless)", delta_inv_a3)
show("  delta(alpha_s) = -alpha_s^2 * delta(1/alpha_s) (dimensionless)",
     -alpha_s_meas**2 * delta_inv_a3)
print()

# ================================================================
# SECTION 4: SENSITIVITY TO M_VL
# ================================================================

print("SECTION 4: SENSITIVITY TO M_VL")
print("-" * 70)
print()
print("  The alpha_s prediction depends on M_VL through the")
print("  threshold. Scan M_VL to see the sensitivity.")
print()

print("  %8s %12s %12s %12s" %
      ("M_VL(GeV)", "alpha_s pred", "miss(%%)", "within 3sigma"))
print("  %8s %12s %12s %12s" %
      ("-" * 8, "-" * 12, "-" * 12, "-" * 12))

scan_results = []

for M_VL_GeV in [200, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000]:
    M_VL_scan = mpf(str(M_VL_GeV))
    L_lo = mlog(M_VL_scan / M_Z_GeV_m) / twopi

    ia1_v = f2m(inv_a1_input) - b_SM_m[0] * L_lo
    ia2_v = f2m(inv_a2_input) - b_SM_m[1] * L_lo

    L_c = (ia1_v - ia2_v) / (b_CD_m[0] - b_CD_m[1])
    ia_gut = ia1_v - b_CD_m[0] * L_c

    ia3_v = ia_gut + b_CD_m[2] * L_c
    ia3_mz = ia3_v + b_SM_m[2] * L_lo
    as_pred = mpf("1") / ia3_mz
    miss = fabs(as_pred - alpha_s_meas) / alpha_s_meas * mpf("100")
    w3s = mpf("0.1153") < as_pred < mpf("0.1207")

    scan_results.append((M_VL_GeV, as_pred, miss, w3s))

    print("  %8d %12s %12s %12s" %
          (M_VL_GeV, mp.nstr(as_pred, 6), mp.nstr(miss, 4),
           "YES" if w3s else "NO"))

print()

# Best M_VL
best_idx = min(range(len(scan_results)), key=lambda i: float(scan_results[i][2]))
best_MVL = scan_results[best_idx][0]
best_as = scan_results[best_idx][1]
best_miss = scan_results[best_idx][2]

print("  Best M_VL: %d GeV" % best_MVL)
show("    alpha_s predicted (dimensionless)", best_as)
show("    miss (%%)", best_miss)
print()

# ================================================================
# SECTION 5: COMPARISON TO sin2_tW PREDICTION
# ================================================================

print("SECTION 5: TWO PREDICTIONS COMPARED")
print("-" * 70)
print()
print("  The CD framework makes two predictions from unification:")
print()
print("  1. sin2_tW from alpha_EM + alpha_s (PHYS-27):")
print("     Predicted: 0.22845 (no threshold)")
print("     Measured:  0.23122")
print("     Miss: 1.2%%")
print()
print("  2. alpha_s from alpha_EM + sin2_tW (this paper):")
show("     Predicted (dimensionless)", alpha_s_pred_1loop)
show("     Measured (dimensionless)", alpha_s_meas)
show("     Miss (%%)", miss_1loop)
print()
print("  Both predictions use two of the three couplings as input")
print("  and predict the third. Both miss by ~1-2%% at one loop.")
print("  Both are expected to improve at two loops.")
print()

# ================================================================
# SECTION 6: PARAMETER COUNT
# ================================================================

print("SECTION 6: PARAMETER COUNT IMPLICATIONS")
print("-" * 70)
print()
print("  If unification is exact (Delta = 0), the three couplings")
print("  alpha_EM, sin2_tW, alpha_s are related by the unification")
print("  condition. Only TWO are independent. The third is derived.")
print()
print("  Combined with theta_QCD = 0 (PHYS-7) and the Koide")
print("  conditional (m_tau from K=2/3), the parameter reductions:")
print()
print("    theta_QCD = 0:  19 -> 18  (energy minimization)")
print("    m_tau:          18 -> 17  (Koide conditional on a^2=2)")
print("    alpha_s:        17 -> 16  (unification condition)")
print("    sin2_tW:        (redundant with alpha_s — same condition)")
print()
print("  The unification condition reduces by 1, not 2, because")
print("  it relates three couplings with one condition. Either")
print("  alpha_s or sin2_tW is derived, not both independently.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Section 1: inputs match library
chk("S1: 1/alpha_1 from inputs matches library",
    f2m(inv_a1_input), f2m(inv_a1), 10, checks)

chk("S1: 1/alpha_2 from inputs matches library",
    f2m(inv_a2_input), f2m(inv_a2), 10, checks)

# Section 2: one-loop prediction
chk_bool("S2: L_cross positive (crossing above M_VL)",
         L_cross > mpf("0"),
         "L = %s" % mp.nstr(L_cross, 5), checks)

chk_bool("S2: M_GUT > 10^15",
         mlog10(M_GUT) > mpf("15"),
         "log10 = %s" % mp.nstr(mlog10(M_GUT), 4), checks)

chk_bool("S2: alpha_s within 3-sigma (abort test)",
         within_3sigma,
         "pred=%s in [0.1153, 0.1207]" % mp.nstr(alpha_s_pred_1loop, 5),
         checks)

chk_bool("S2: alpha_s miss < 5%%",
         miss_1loop < mpf("5"),
         "miss = %s%%" % mp.nstr(miss_1loop, 4), checks)

# Section 3: Delta consistency
chk_bool("S3: Delta negative (same physics as PHYS-24)",
         Delta < mpf("0"),
         "Delta = %s" % mp.nstr(Delta, 4), checks)

# Section 4: all M_VL within 3-sigma
all_3sigma = all(r[3] for r in scan_results)
chk_bool("S4: All M_VL give alpha_s within 3-sigma",
         all_3sigma,
         "all within [0.1153, 0.1207]", checks)

# Section 5: miss comparable to sin2_tW miss
chk_bool("S5: alpha_s miss < 3%% (comparable to sin2_tW)",
         miss_1loop < mpf("3"),
         "miss = %s%%" % mp.nstr(miss_1loop, 4), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-30 alpha_s PREDICTION COMPLETE")
print("=" * 70)
