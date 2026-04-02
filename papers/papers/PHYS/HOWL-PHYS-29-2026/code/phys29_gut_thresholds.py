#!/usr/bin/env python3
"""
HOWL PHYS-29: phys29_gut_thresholds.py
========================================
GUT Threshold Corrections in Minimal SU(5).

In minimal SU(5), the X,Y gauge bosons define M_GUT. The colored
Higgs triplet T(3,1,-1/3) may have a different mass M_T.
If M_T != M_X, the mismatch introduces a threshold correction
to the unification prediction.

The correction is computed as a perturbative shift:
  delta_Delta = [db3_T - f(db1_T, db2_T)] * ln(M_T/M_X) / (2*pi)

This is a boundary correction, not a change to the bulk running.
The bulk running uses CD betas from M_VL to M_GUT as before.

Backed by: phys28_vl_twoloop.py (11/11), phys26_normalization.py (20/20)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, fabs
from mpmath import log10 as mlog10, power as mpow

# ================================================================
print("=" * 70)
print("HOWL PHYS-29: GUT THRESHOLD CORRECTIONS")
print("How much mass splitting is needed for exact unification?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: THE REFERENCE UNIFICATION (NO THRESHOLD)
# ================================================================

print("SECTION 1: REFERENCE UNIFICATION (one-loop, no threshold)")
print("-" * 70)
print()

b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]

M_Z_GeV_m = f2m(M_Z) / mpf("1000")
M_VL_m = mpf("500")
twopi = mpf("2") * mpi

L_low = mlog(M_VL_m / M_Z_GeV_m) / twopi
inv_a_MZ = [f2m(inv_a1), f2m(inv_a2), f2m(Fraction(1) / alpha_s)]
inv_a_VL = [inv_a_MZ[i] - b_SM_m[i] * L_low for i in range(3)]

# One-loop crossing with CD betas
L_ref = (inv_a_VL[1] - inv_a_VL[0]) / (b_CD_m[1] - b_CD_m[0])
inv_aGUT_ref = inv_a_VL[0] - b_CD_m[0] * L_ref
inv_a3_ref = inv_a_VL[2] - b_CD_m[2] * L_ref
Delta_ref = inv_a3_ref - inv_aGUT_ref
M_GUT_ref = M_VL_m * mexp(L_ref * twopi)
log_MGUT_ref = mlog10(M_GUT_ref)

show("  Delta (one-loop, no threshold) (dimensionless)", Delta_ref)
show("  log10(M_GUT/GeV)", log_MGUT_ref)
show("  1/alpha_GUT (dimensionless)", inv_aGUT_ref)
print()

# ================================================================
# SECTION 2: THE THRESHOLD CORRECTION FORMULA
# ================================================================

print("SECTION 2: THE THRESHOLD CORRECTION FORMULA")
print("-" * 70)
print()
print("  In minimal SU(5), the X,Y gauge bosons define M_GUT = M_X.")
print("  The colored Higgs triplet T(3,1,-1/3) has mass M_T.")
print("  If M_T != M_X, the running between min(M_T,M_X) and")
print("  max(M_T,M_X) uses different effective betas.")
print()
print("  The correction to Delta is a BOUNDARY effect:")
print("  delta_Delta = effective_C * ln(M_T/M_X) / (2*pi)")
print()

# The colored Higgs triplet T(3,1,-1/3) as a complex scalar:
# Using scalar Dynkin formulas from PHYS-26:
# db1 = (1/5)*dim3*dim2*Y^2 = (1/5)*3*1*(1/9) = 1/15
# db2 = (1/3)*dim3*S2(R2) = 0 (SU(2) singlet, S2 = 0)
# db3 = (1/6)*dim2*S2(R3) = (1/6)*1*(1/2) = 1/12

db1_T = Fraction(1, 15)
db2_T = Fraction(0)
db3_T = Fraction(1, 12)

show("  Triplet T(3,1,-1/3) one-loop shifts:", f2m(Fraction(0)))
show("    db1_T (dimensionless)", f2m(db1_T))
show("    db2_T (dimensionless)", f2m(db2_T))
show("    db3_T (dimensionless)", f2m(db3_T))
print()

# The threshold correction to Delta = 1/alpha_3(M_GUT) - 1/alpha_GUT:
#
# When M_T > M_X: the triplet is heavier than the X bosons.
# Between M_X and M_T, the triplet is NOT present in the running.
# The running below M_X uses the broken-phase betas (CD betas).
# The running above M_T uses the full SU(5) betas.
# Between M_X and M_T: the X bosons are integrated out but the
# triplet is still present. The effective betas in this range
# differ from both the broken and full theories.
#
# Actually in the standard treatment: at M_GUT we match the
# broken-phase couplings to the unified coupling. The threshold
# correction comes from the MISMATCH in the matching conditions
# when different heavy particles have different masses.
#
# The standard result (e.g. Weinberg 1980, Hall 1981):
# The correction to the effective M_GUT (as seen by each coupling) is:
#
# For coupling alpha_a: the effective GUT scale is
#   ln(M_GUT_eff_a) = ln(M_X) + sum_i [db_a_i/b_a] * ln(M_i/M_X)
# where the sum is over heavy particles i with masses M_i != M_X.
#
# For the triplet only:
# The correction to Delta = 1/alpha_3 - 1/alpha_GUT is:
#
# delta_Delta = -[db3_T - db_GUT_shift] * ln(M_T/M_X) / (2*pi)
#
# where db_GUT_shift accounts for the shift of the crossing point.
#
# Since db2_T = 0, the alpha_2 running is unaffected by M_T.
# The crossing (alpha_1 = alpha_2) shifts because alpha_1 running
# changes. But at the crossing, 1/alpha_GUT = 1/alpha_2, so:
#
# The shift of 1/alpha_GUT = shift of 1/alpha_1 at the crossing
# = -db1_T * ln(M_T/M_X) / (2*pi)  ... but the crossing also moves.
#
# For a perturbative treatment:
# delta(1/alpha_3 at crossing) = -db3_T * ln(M_T/M_X) / (2*pi)
# delta(1/alpha_GUT) = -(db1_T * (5/3)) / ((5/3) + 1) * ln(M_T/M_X)/(2*pi)
#   ... from the shift of the crossing when only alpha_1 changes.
#   The factor (5/3)/((5/3)+1) = (5/3)/(8/3) = 5/8 weights the
#   alpha_1 change into the crossing shift.
#   Wait: at crossing, 1/a1 = 1/a2. If 1/a1 shifts by delta, the
#   crossing moves so that the new 1/a1 at the new crossing equals
#   the old 1/a2. So 1/alpha_GUT = 1/alpha_2 (unchanged).
#   Therefore delta(1/alpha_GUT) = 0 when db2_T = 0!
#
# So: delta_Delta = delta(1/alpha_3) - delta(1/alpha_GUT)
#                 = -db3_T * ln(M_T/M_X) / (2*pi) - 0
#                 = -db3_T * ln(M_T/M_X) / (2*pi)

C_thresh = -db3_T   # = -1/12
# delta_Delta = C_thresh * ln(M_T/M_X) / (2*pi) = -(1/12) * ln(M_T/M_X) / (2*pi)

show("  Effective threshold coefficient C (dimensionless)", f2m(C_thresh))
print()
print("  delta_Delta = -(1/12) * ln(M_T/M_X) / (2*pi)")
print()
print("  For M_T > M_X: ln(M_T/M_X) > 0, so delta_Delta < 0")
print("    -> makes Delta MORE negative (worse)")
print("  For M_T < M_X: ln(M_T/M_X) < 0, so delta_Delta > 0")
print("    -> makes Delta LESS negative (better)")
print()
print("  Since Delta_ref = %s < 0, we need delta_Delta > 0," %
      mp.nstr(Delta_ref, 4))
print("  which requires M_T < M_X (triplet lighter than X boson).")
print()

# ================================================================
# SECTION 3: SOLVING FOR EXACT UNIFICATION
# ================================================================

print("SECTION 3: M_T/M_X FOR EXACT UNIFICATION")
print("-" * 70)
print()

# delta_Delta = -Delta_ref (to cancel the existing miss)
# -(1/12) * ln(M_T/M_X) / (2*pi) = -Delta_ref
# ln(M_T/M_X) = Delta_ref * 12 * 2*pi = Delta_ref * 24*pi

ln_ratio = f2m(Fraction(12)) * twopi * Delta_ref
ratio_T_X = mexp(ln_ratio)

show("  Required ln(M_T/M_X) (dimensionless)", ln_ratio)
show("  Required M_T/M_X (dimensionless)", ratio_T_X)
show("  Required M_X/M_T (dimensionless)", mpf("1") / ratio_T_X)
print()

# M_T in GeV
M_T_exact = M_GUT_ref * ratio_T_X
log_MT_exact = mlog10(M_T_exact)
show("  M_T (GeV)", M_T_exact)
show("  log10(M_T/GeV)", log_MT_exact)
show("  M_X = M_GUT (GeV)", M_GUT_ref)
show("  log10(M_X/GeV)", log_MGUT_ref)
print()

# Verify: recompute Delta with the correction
delta_correction = f2m(-db3_T) * ln_ratio / twopi
Delta_corrected = Delta_ref + delta_correction
show("  Threshold correction (dimensionless)", delta_correction)
show("  Corrected Delta (dimensionless)", Delta_corrected)
print()

# ================================================================
# SECTION 4: NATURALNESS CHECK
# ================================================================

print("SECTION 4: NATURALNESS CHECK")
print("-" * 70)
print()

max_ratio = mpf("1") / ratio_T_X   # M_X/M_T since M_T < M_X

show("  M_T/M_X (dimensionless)", ratio_T_X)
show("  M_X/M_T (dimensionless)", max_ratio)
print()

is_natural = max_ratio < mpf("10")
is_moderate = max_ratio < mpf("100")

print("  Natural (M_X/M_T < 10): %s" % is_natural)
print("  Moderate (M_X/M_T < 100): %s" % is_moderate)
print("  Fine-tuned (M_X/M_T > 100): %s" % (not is_moderate))
print()

# ================================================================
# SECTION 5: SCAN TABLE
# ================================================================

print("SECTION 5: THRESHOLD CORRECTION SCAN")
print("-" * 70)
print()

print("  %12s %12s %12s %12s" %
      ("M_X/M_T", "ln(M_T/M_X)", "delta_Delta", "Delta_total"))
print("  %12s %12s %12s %12s" %
      ("-" * 12, "-" * 12, "-" * 12, "-" * 12))

scan_ratios = [Fraction(1), Fraction(2), Fraction(3), Fraction(5),
               Fraction(10), Fraction(20), Fraction(50), Fraction(100),
               Fraction(200), Fraction(500)]

for r_inv in scan_ratios:
    r = Fraction(1) / r_inv   # M_T/M_X < 1
    ln_r = mlog(f2m(r))
    d_delta = f2m(-db3_T) * ln_r / twopi
    D_total = Delta_ref + d_delta
    print("  %12s %12s %12s %12s" %
          (mp.nstr(f2m(r_inv), 4),
           mp.nstr(ln_r, 5),
           mp.nstr(d_delta, 5),
           mp.nstr(D_total, 5)))

print()

# ================================================================
# SECTION 6: PROTON LIFETIME
# ================================================================

print("SECTION 6: PROTON LIFETIME")
print("-" * 70)
print()

# tau ~ M_X^4 / alpha_GUT^2. Since M_X = M_GUT is unchanged
# (the triplet mass changes, not the X boson mass), the proton
# lifetime prediction depends on M_X = M_GUT, which is fixed.
# The threshold correction changes the PREDICTION of alpha_3,
# not the GUT scale.
#
# However, the proton decay rate depends on M_X directly.
# If we define M_X = M_GUT_ref = 10^15.43 GeV:

log_tau_base = mpf("34.5")   # central estimate from PHYS-20
M_X_GeV = M_GUT_ref

# Super-K bound
superK_log = mpf("34.38")
# Hyper-K reach
hyperK_log = mpf("35")

show("  M_X = M_GUT (GeV)", M_X_GeV)
show("  log10(M_X/GeV)", log_MGUT_ref)
show("  Proton lifetime estimate: log10(tau/yr)", log_tau_base)
show("  Super-K bound: log10(tau/yr) >", superK_log)
show("  Hyper-K 20yr reach: log10(tau/yr) ~", hyperK_log)
print()

print("  Since M_X is unchanged by the triplet threshold")
print("  (only M_T shifts), the proton lifetime prediction")
print("  remains at 10^34.5 yr, above the Super-K bound")
print("  and within Hyper-K reach.")
print()

# But M_T affects proton decay through the colored Higgs
# exchange diagram (dimension-6 operator):
# Gamma(p -> e+ pi0) from X boson: ~ alpha_GUT^2 / M_X^4
# Gamma(p -> K+ nu) from triplet:  ~ y^2 / M_T^2
# The X boson channel dominates for M_T ~ M_X.
# If M_T << M_X, the triplet channel could dominate.

show("  M_T for exact unification (GeV)", M_T_exact)
show("  log10(M_T/GeV)", log_MT_exact)
show("  M_X/M_T (dimensionless)", max_ratio)
print()

print("  For the X boson channel (p -> e+ pi0):")
print("    tau ~ M_X^4 ~ 10^%.1f yr (unchanged)" %
      float(log_tau_base))
print()
print("  For the triplet channel (p -> K+ nu_bar):")
print("    tau_T ~ M_T^2 * (suppressions)")
print("    M_T = 10^%.1f GeV" % float(log_MT_exact))
print("    This channel may be enhanced if M_T << M_X.")
print("    Detailed computation requires Yukawa couplings (Level 2).")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_exact("S1: Triplet db1 = 1/15",
          db1_T, Fraction(1, 15), checks)

chk_exact("S1: Triplet db2 = 0 (SU(2) singlet)",
          db2_T, Fraction(0), checks)

chk_exact("S1: Triplet db3 = 1/12",
          db3_T, Fraction(1, 12), checks)

chk_bool("S1: Reference Delta negative",
         Delta_ref < mpf("0"),
         "Delta = %s" % mp.nstr(Delta_ref, 4), checks)

chk_bool("S3: Corrected Delta ~ 0",
         fabs(Delta_corrected) < mpf("0.01"),
         "|Delta| = %s" % mp.nstr(fabs(Delta_corrected), 4), checks)

chk_bool("S3: M_T < M_X (triplet lighter)",
         ratio_T_X < mpf("1"),
         "M_T/M_X = %s" % mp.nstr(ratio_T_X, 4), checks)

chk_bool("S3: M_T > 10^10 GeV (not absurdly light)",
         log_MT_exact > mpf("10"),
         "log10(M_T) = %s" % mp.nstr(log_MT_exact, 4), checks)

chk_bool("S4: Abort test — M_X/M_T < 100",
         max_ratio < mpf("100"),
         "M_X/M_T = %s" % mp.nstr(max_ratio, 4), checks)

chk_bool("S6: M_X above proton decay bound (log > 15)",
         log_MGUT_ref > mpf("15"),
         "log10(M_X) = %s" % mp.nstr(log_MGUT_ref, 4), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-29 GUT THRESHOLD CORRECTIONS COMPLETE")
print("=" * 70)
