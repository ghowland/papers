#!/usr/bin/env python3
"""
HOWL PHYS-30: phys30_alpha_s.py
=================================
alpha_s Prediction from Unification.

Uses the unification condition with CD modified betas to PREDICT
alpha_s(M_Z) from only alpha_EM and sin2_tW as inputs.

sin2_tW = alpha_EM / alpha_2, so 1/alpha_2 = sin2_tW * (1/alpha_EM).
(5/3)/alpha_1 = 1/alpha_EM - 1/alpha_2.

SIGN CONVENTION: 1/alpha_i(mu) = 1/alpha_i(mu0) - b_i * L

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
# SECTION 1: THE TWO INPUTS
# ================================================================

print("SECTION 1: THE TWO INPUTS")
print("-" * 70)
print()
print("  Input 1: alpha_EM = 1/%s (DATA-4 B1)" %
      mp.nstr(f2m(alpha_inv), 12))
print("  Input 2: sin2_tW  = %s (DATA-4 B11)" %
      mp.nstr(f2m(sin2_tW), 5))
print()

# sin2_tW = alpha_EM / alpha_2
# => 1/alpha_2 = sin2_tW / alpha_EM = sin2_tW * alpha_inv
# (5/3)/alpha_1 = 1/alpha_EM - 1/alpha_2
# => 1/alpha_1 = (3/5) * (1/alpha_EM - 1/alpha_2)

inv_a2_input = sin2_tW * alpha_inv                          # Fraction
inv_a1_input = Fraction(3, 5) * (alpha_inv - inv_a2_input)  # Fraction

show("  Derived 1/alpha_1(M_Z) (dimensionless)", f2m(inv_a1_input))
show("  Derived 1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2_input))
print()
show("  Library 1/alpha_1 (dimensionless)", f2m(inv_a1))
show("  Library 1/alpha_2 (dimensionless)", f2m(inv_a2))
print()

twopi = mpf("2") * mpi
b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]
M_Z_GeV_m = f2m(M_Z) / mpf("1000")
alpha_s_meas = f2m(alpha_s)

# ================================================================
# SECTION 2: ONE-LOOP PREDICTION (M_VL = 500 GeV)
# ================================================================

print("SECTION 2: ONE-LOOP PREDICTION (M_VL = 500 GeV)")
print("-" * 70)
print()

M_VL_m = mpf("500")
L_low = mlog(M_VL_m / M_Z_GeV_m) / twopi

# SM betas from M_Z to M_VL
inv_a1_VL = f2m(inv_a1_input) - b_SM_m[0] * L_low
inv_a2_VL = f2m(inv_a2_input) - b_SM_m[1] * L_low

show("  1/alpha_1(M_VL) (dimensionless)", inv_a1_VL)
show("  1/alpha_2(M_VL) (dimensionless)", inv_a2_VL)
print()

# CD betas from M_VL to crossing
# 1/a1 - b1*L = 1/a2 - b2*L => L = (1/a1 - 1/a2)/(b1 - b2)
L_cross = (inv_a1_VL - inv_a2_VL) / (b_CD_m[0] - b_CD_m[1])
inv_aGUT = inv_a1_VL - b_CD_m[0] * L_cross
M_GUT = M_VL_m * mexp(L_cross * twopi)

show("  L to crossing (dimensionless)", L_cross)
show("  1/alpha_GUT (dimensionless)", inv_aGUT)
show("  log10(M_GUT/GeV)", mlog10(M_GUT))
print()

# Predict alpha_3: run from M_GUT down to M_Z
# M_GUT to M_VL: 1/a3(VL) = 1/a_GUT + b3_CD * L_cross
inv_a3_VL = inv_aGUT + b_CD_m[2] * L_cross
# M_VL to M_Z: 1/a3(MZ) = 1/a3(VL) + b3_SM * L_low
inv_a3_MZ = inv_a3_VL + b_SM_m[2] * L_low

alpha_s_pred = mpf("1") / inv_a3_MZ
miss_pct = fabs(alpha_s_pred - alpha_s_meas) / alpha_s_meas * mpf("100")

show("  1/alpha_3(M_Z) predicted (dimensionless)", inv_a3_MZ)
show("  alpha_s predicted (dimensionless)", alpha_s_pred)
show("  alpha_s measured (dimensionless)", alpha_s_meas)
show("  Miss (%%)", miss_pct)
print()

within_1s = mpf("0.1171") < alpha_s_pred < mpf("0.1189")
within_3s = mpf("0.1153") < alpha_s_pred < mpf("0.1207")

print("  Measured: 0.1180 +/- 0.0009")
print("  1-sigma: [0.1171, 0.1189]. Predicted in range: %s" % within_1s)
print("  3-sigma: [0.1153, 0.1207]. Predicted in range: %s" % within_3s)
print()

# ================================================================
# SECTION 3: M_VL SENSITIVITY SCAN
# ================================================================

print("SECTION 3: SENSITIVITY TO M_VL")
print("-" * 70)
print()

print("  %8s %12s %12s %8s" %
      ("M_VL(GeV)", "alpha_s", "miss(%%)", "3-sigma"))
print("  %8s %12s %12s %8s" %
      ("-" * 8, "-" * 12, "-" * 12, "-" * 8))

scan = []

for MVL in [200, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000]:
    M_v = mpf(str(MVL))
    Ll = mlog(M_v / M_Z_GeV_m) / twopi

    ia1v = f2m(inv_a1_input) - b_SM_m[0] * Ll
    ia2v = f2m(inv_a2_input) - b_SM_m[1] * Ll

    Lc = (ia1v - ia2v) / (b_CD_m[0] - b_CD_m[1])
    iag = ia1v - b_CD_m[0] * Lc

    ia3v = iag + b_CD_m[2] * Lc
    ia3z = ia3v + b_SM_m[2] * Ll
    asp = mpf("1") / ia3z
    miss = fabs(asp - alpha_s_meas) / alpha_s_meas * mpf("100")
    w3 = mpf("0.1153") < asp < mpf("0.1207")

    scan.append((MVL, asp, miss, w3))
    print("  %8d %12s %12s %8s" %
          (MVL, mp.nstr(asp, 6), mp.nstr(miss, 4),
           "YES" if w3 else "NO"))

print()

best_i = min(range(len(scan)), key=lambda i: float(scan[i][2]))
best_MVL, best_as, best_miss, best_w3 = scan[best_i]

print("  Best: M_VL = %d GeV" % best_MVL)
show("    alpha_s (dimensionless)", best_as)
show("    miss (%%)", best_miss)
print()

# ================================================================
# SECTION 4: COMPARISON TO sin2_tW PREDICTION
# ================================================================

print("SECTION 4: TWO PREDICTIONS COMPARED")
print("-" * 70)
print()
print("  Two-input predictions from the CD unification framework:")
print()
print("  PHYS-27: alpha_EM + alpha_s -> sin2_tW")
print("    Predicted: 0.22845 (no threshold)")
print("    Measured:  0.23122")
print("    Miss: 1.2%%")
print()
print("  PHYS-30: alpha_EM + sin2_tW -> alpha_s")
show("    Predicted (dimensionless)", alpha_s_pred)
show("    Measured (dimensionless)", alpha_s_meas)
show("    Miss (%%)", miss_pct)
print()
print("  Both use two couplings to predict the third.")
print("  Both miss by a similar amount at one loop.")
print("  The two predictions are the SAME unification condition")
print("  viewed from different angles.")
print()

# ================================================================
# SECTION 5: PARAMETER COUNT
# ================================================================

print("SECTION 5: PARAMETER COUNT")
print("-" * 70)
print()
print("  If unification is exact, alpha_EM + sin2_tW determine")
print("  alpha_s. The strong coupling is DERIVED, not independent.")
print()
print("  Reductions:")
print("    theta_QCD = 0:  19 -> 18  (energy minimization)")
print("    m_tau (Koide):  18 -> 17  (conditional on a^2 = 2)")
print("    alpha_s (unif): 17 -> 16  (unification condition)")
print()
print("  Note: sin2_tW prediction (PHYS-27) and alpha_s prediction")
print("  (this paper) are the SAME condition. Only one parameter")
print("  is reduced, not two.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk("S1: 1/alpha_1 from inputs matches library",
    f2m(inv_a1_input), f2m(inv_a1), 10, checks)

chk("S1: 1/alpha_2 from inputs matches library",
    f2m(inv_a2_input), f2m(inv_a2), 10, checks)

chk_bool("S2: L_cross positive",
         L_cross > mpf("0"),
         "L = %s" % mp.nstr(L_cross, 5), checks)

chk_bool("S2: M_GUT > 10^15",
         mlog10(M_GUT) > mpf("15"),
         "log10 = %s" % mp.nstr(mlog10(M_GUT), 4), checks)

chk_bool("S2: Abort test — alpha_s within 3-sigma",
         within_3s,
         "pred=%s in [0.1153, 0.1207]" % mp.nstr(alpha_s_pred, 5),
         checks)

chk_bool("S2: alpha_s miss < 5%%",
         miss_pct < mpf("5"),
         "miss = %s%%" % mp.nstr(miss_pct, 4), checks)

chk_bool("S3: All M_VL within 3-sigma",
         all(r[3] for r in scan),
         "all in [0.1153, 0.1207]", checks)

chk_bool("S3: Best miss < 3%%",
         best_miss < mpf("3"),
         "miss = %s%%" % mp.nstr(best_miss, 4), checks)

chk_bool("S4: alpha_s miss comparable to sin2_tW miss (<3%%)",
         miss_pct < mpf("3"),
         "alpha_s=%s%%, sin2_tW=1.2%%" % mp.nstr(miss_pct, 3), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-30 alpha_s PREDICTION COMPLETE")
print("=" * 70)

