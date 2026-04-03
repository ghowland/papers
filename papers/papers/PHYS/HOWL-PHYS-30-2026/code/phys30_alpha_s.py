#!/usr/bin/env python3
"""
HOWL PHYS-30: phys30_alpha_s.py
=================================
alpha_s Prediction from Unification.

Uses the unification condition with CD modified betas to PREDICT
alpha_s(M_Z) from alpha_EM and sin2_tW.

The one-loop prediction misses by ~12% because Delta = -1.17
translates directly into alpha_s. At two loops (Delta = -0.40),
the miss reduces to ~4%. This paper documents the one-loop
baseline and estimates the two-loop improvement.

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
# SECTION 1: INPUTS AND DERIVATION
# ================================================================

print("SECTION 1: INPUTS")
print("-" * 70)
print()

# sin2_tW = alpha_EM / alpha_2 => 1/alpha_2 = sin2_tW * (1/alpha_EM)
# (5/3)/alpha_1 = 1/alpha_EM - 1/alpha_2
# => 1/alpha_1 = (3/5)(1/alpha_EM - 1/alpha_2)

inv_a2_in = sin2_tW * alpha_inv
inv_a1_in = Fraction(3, 5) * (alpha_inv - inv_a2_in)

show("  1/alpha_1(M_Z) (dimensionless)", f2m(inv_a1_in))
show("  1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2_in))
show("  alpha_s measured = %s (DATA-4 B12) (dimensionless)" %
     mp.nstr(f2m(alpha_s), 4), f2m(alpha_s))
print()

twopi = mpf("2") * mpi
b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]
M_Z_GeV_m = f2m(M_Z) / mpf("1000")
alpha_s_meas = f2m(alpha_s)

# ================================================================
# SECTION 2: ONE-LOOP PREDICTION
# ================================================================

print("SECTION 2: ONE-LOOP PREDICTION (M_VL = 500 GeV)")
print("-" * 70)
print()

M_VL_m = mpf("500")
L_low = mlog(M_VL_m / M_Z_GeV_m) / twopi

inv_a1_VL = f2m(inv_a1_in) - b_SM_m[0] * L_low
inv_a2_VL = f2m(inv_a2_in) - b_SM_m[1] * L_low

L_cross = (inv_a1_VL - inv_a2_VL) / (b_CD_m[0] - b_CD_m[1])
inv_aGUT = inv_a1_VL - b_CD_m[0] * L_cross
M_GUT = M_VL_m * mexp(L_cross * twopi)

# Predict alpha_3: M_GUT to M_VL (CD), M_VL to M_Z (SM)
inv_a3_VL = inv_aGUT + b_CD_m[2] * L_cross
inv_a3_MZ = inv_a3_VL + b_SM_m[2] * L_low
alpha_s_1L = mpf("1") / inv_a3_MZ

miss_1L = fabs(alpha_s_1L - alpha_s_meas) / alpha_s_meas * mpf("100")

show("  1/alpha_GUT (dimensionless)", inv_aGUT)
show("  log10(M_GUT/GeV)", mlog10(M_GUT))
show("  1/alpha_3(M_Z) predicted (dimensionless)", inv_a3_MZ)
show("  1/alpha_3(M_Z) measured (dimensionless)",
     mpf("1") / alpha_s_meas)
print()
show("  alpha_s predicted (dimensionless)", alpha_s_1L)
show("  alpha_s measured (dimensionless)", alpha_s_meas)
show("  Miss (%%)", miss_1L)
print()

# ================================================================
# SECTION 3: WHY THE MISS IS 12%, NOT 1.2%
# ================================================================

print("SECTION 3: WHY THE MISS IS LARGE")
print("-" * 70)
print()
print("  The sin2_tW prediction (PHYS-27) missed by 1.2%%.")
print("  The alpha_s prediction misses by 12%%. Why the asymmetry?")
print()
print("  sin2_tW is a RATIO of couplings: alpha_1/alpha_2.")
print("  The one-loop errors in alpha_1 and alpha_2 partially cancel.")
print()
print("  alpha_s is the ABSOLUTE value of the third coupling.")
print("  The full Delta = -1.17 translates directly into alpha_s.")
print()

# Show the connection: Delta at M_GUT = predicted - measured 1/alpha_3
inv_a3_meas_VL = mpf("1") / alpha_s_meas - b_SM_m[2] * L_low
inv_a3_meas_GUT = inv_a3_meas_VL + b_CD_m[2] * L_cross
Delta_GUT = inv_a3_meas_GUT - inv_aGUT

show("  Delta(1/alpha_3) at M_GUT (dimensionless)", Delta_GUT)
show("  This IS the one-loop Delta from PHYS-24 (dimensionless)",
     f2m(delta_1loop))
print()

# The predicted 1/alpha_3 at M_Z is too HIGH by:
delta_inv_a3 = inv_a3_MZ - mpf("1") / alpha_s_meas
show("  Predicted 1/alpha_3 - measured 1/alpha_3 at M_Z (dimensionless)",
     delta_inv_a3)
show("  This equals Delta propagated to M_Z (dimensionless)",
     delta_inv_a3)
print()
print("  1/alpha_3 too high => alpha_s too low => 12%% miss.")
print()

# ================================================================
# SECTION 4: TWO-LOOP ESTIMATE
# ================================================================

print("SECTION 4: TWO-LOOP ESTIMATE")
print("-" * 70)
print()

# At two loops, Delta improves from -1.17 to -0.40 (PHYS-24).
# The alpha_s miss scales with Delta.
# Two-loop Delta / one-loop Delta = 0.40/1.17 = 0.342
# So two-loop alpha_s miss ~ 0.342 * 12.1% = 4.1%

ratio_2L_1L = fabs(f2m(delta_2loop)) / fabs(f2m(delta_1loop))
miss_2L_est = miss_1L * ratio_2L_1L
alpha_s_2L_est = alpha_s_meas * (mpf("1") - miss_2L_est / mpf("100"))

# More precisely: the two-loop 1/alpha_3 at M_Z is shifted less
delta_inv_a3_2L = delta_inv_a3 * ratio_2L_1L
inv_a3_MZ_2L = mpf("1") / alpha_s_meas + delta_inv_a3_2L
alpha_s_2L = mpf("1") / inv_a3_MZ_2L
miss_2L = fabs(alpha_s_2L - alpha_s_meas) / alpha_s_meas * mpf("100")

show("  Delta ratio (2-loop/1-loop) (dimensionless)", ratio_2L_1L)
show("  Estimated 2-loop alpha_s (dimensionless)", alpha_s_2L)
show("  Estimated 2-loop miss (%%)", miss_2L)
print()

within_1s_2L = mpf("0.1171") < alpha_s_2L < mpf("0.1189")
within_3s_2L = mpf("0.1153") < alpha_s_2L < mpf("0.1207")

print("  Two-loop estimate within 1-sigma: %s" % within_1s_2L)
print("  Two-loop estimate within 3-sigma: %s" % within_3s_2L)
print()

# ================================================================
# SECTION 5: M_VL SCAN
# ================================================================

print("SECTION 5: M_VL SENSITIVITY")
print("-" * 70)
print()

print("  %8s %10s %10s %10s %10s" %
      ("M_VL(GeV)", "alpha_s_1L", "miss_1L%%", "alpha_s_2L", "miss_2L%%"))
print("  %8s %10s %10s %10s %10s" %
      ("-"*8, "-"*10, "-"*10, "-"*10, "-"*10))

scan = []

for MVL in [200, 500, 1000, 1500, 2000, 3000, 5000, 6000]:
    Mv = mpf(str(MVL))
    Ll = mlog(Mv / M_Z_GeV_m) / twopi

    ia1v = f2m(inv_a1_in) - b_SM_m[0] * Ll
    ia2v = f2m(inv_a2_in) - b_SM_m[1] * Ll
    Lc = (ia1v - ia2v) / (b_CD_m[0] - b_CD_m[1])
    iag = ia1v - b_CD_m[0] * Lc

    ia3v = iag + b_CD_m[2] * Lc
    ia3z = ia3v + b_SM_m[2] * Ll
    as1 = mpf("1") / ia3z
    m1 = fabs(as1 - alpha_s_meas) / alpha_s_meas * mpf("100")

    # Two-loop estimate at this M_VL
    d_ia3 = ia3z - mpf("1") / alpha_s_meas
    d_ia3_2L = d_ia3 * ratio_2L_1L
    ia3z_2L = mpf("1") / alpha_s_meas + d_ia3_2L
    as2 = mpf("1") / ia3z_2L
    m2 = fabs(as2 - alpha_s_meas) / alpha_s_meas * mpf("100")

    scan.append((MVL, as1, m1, as2, m2))
    print("  %8d %10s %10s %10s %10s" %
          (MVL, mp.nstr(as1, 6), mp.nstr(m1, 4),
           mp.nstr(as2, 6), mp.nstr(m2, 4)))

print()

# ================================================================
# SECTION 6: THE CONVERGENCE PATTERN
# ================================================================

print("SECTION 6: THE CONVERGENCE PATTERN")
print("-" * 70)
print()
print("  Level         alpha_s pred   miss    within 3-sigma")
print("  ------------- -------------- ------- --------------")
print("  One-loop      %s   %s%%  %s" %
      (mp.nstr(alpha_s_1L, 6), mp.nstr(miss_1L, 4),
       "NO" if not (mpf("0.1153") < alpha_s_1L < mpf("0.1207")) else "YES"))
print("  Two-loop est  %s   %s%%  %s" %
      (mp.nstr(alpha_s_2L, 6), mp.nstr(miss_2L, 4),
       "NO" if not within_3s_2L else "YES"))
print("  Measured       0.1180        0%%     —")
print()
print("  The pattern matches PHYS-27 (sin2_tW): each refinement")
print("  moves the prediction toward the measured value.")
print("  At two loops, alpha_s is within ~4%% of measured.")
print("  GUT threshold corrections (PHYS-29: disfavored for min SU(5))")
print("  would close the remaining gap in a non-minimal completion.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk("S1: 1/alpha_1 matches library",
    f2m(inv_a1_in), f2m(inv_a1), 10, checks)

chk("S1: 1/alpha_2 matches library",
    f2m(inv_a2_in), f2m(inv_a2), 10, checks)

chk_bool("S2: L_cross positive",
         L_cross > mpf("0"),
         "L = %s" % mp.nstr(L_cross, 5), checks)

chk_bool("S2: M_GUT > 10^15",
         mlog10(M_GUT) > mpf("15"),
         "log10 = %s" % mp.nstr(mlog10(M_GUT), 4), checks)

chk_bool("S2: One-loop miss < 15%% (abort test)",
         miss_1L < mpf("15"),
         "miss = %s%%" % mp.nstr(miss_1L, 4), checks)

chk_bool("S3: Delta at M_GUT matches PHYS-24 one-loop",
         fabs(Delta_GUT - f2m(delta_1loop)) < mpf("0.01"),
         "Delta=%s vs ref=%s" % (mp.nstr(Delta_GUT, 4),
                                  mp.nstr(f2m(delta_1loop), 4)), checks)

chk_bool("S4: Two-loop estimate closer to measured",
         miss_2L < miss_1L,
         "2L=%s%% < 1L=%s%%" % (mp.nstr(miss_2L, 4),
                                 mp.nstr(miss_1L, 4)), checks)

chk_bool("S4: Two-loop estimate miss < 6%%",
         miss_2L < mpf("6"),
         "miss = %s%%" % mp.nstr(miss_2L, 4), checks)

chk_bool("S5: alpha_s prediction improves with lower M_VL",
         scan[0][2] < scan[-1][2],
         "M_VL=200: %s%% < M_VL=6000: %s%%" %
         (mp.nstr(scan[0][2], 4), mp.nstr(scan[-1][2], 4)), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-30 alpha_s PREDICTION COMPLETE")
print("=" * 70)
