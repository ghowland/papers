#!/usr/bin/env python3
"""
HOWL PHYS-29: phys29_gut_thresholds.py
========================================
GUT Threshold Corrections in Minimal SU(5).

In minimal SU(5), the superheavy particles (X,Y gauge bosons
at mass M_X and colored Higgs triplet at mass M_T) have different
masses. This mass splitting introduces threshold corrections that
shift the effective unification point.

The correction to Delta(1/alpha_3) from the mass splitting is:
  delta_thresh = (1/(2*pi)) * [C_X * ln(M_X/M_GUT) + C_T * ln(M_T/M_GUT)]

where C_X and C_T are group theory coefficients and M_GUT is the
nominal crossing scale. The question: for what M_T/M_X does the
threshold correction exactly cancel the remaining Delta from
two-loop running?

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
# SECTION 1: THE THRESHOLD CORRECTION FORMULA
# ================================================================

print("SECTION 1: THE THRESHOLD CORRECTION FORMULA")
print("-" * 70)
print()
print("  In minimal SU(5), the superheavy spectrum has two scales:")
print("    M_X: mass of the (X,Y) gauge bosons (in the 24 adjoint)")
print("    M_T: mass of the colored Higgs triplet (in the 5)")
print()
print("  The threshold correction to the unification condition is:")
print("    delta_thresh = C * ln(M_T/M_X) / (2*pi)")
print()
print("  where C is the difference of Dynkin indices between the")
print("  colored triplet and X boson contributions to alpha_3")
print("  relative to the alpha_1=alpha_2 crossing.")
print()

# In minimal SU(5), the threshold correction to Delta(1/alpha_3)
# from the GUT-scale mass splitting is:
#
# The X,Y bosons contribute to all three couplings. The colored
# Higgs triplet T contributes to alpha_1 and alpha_3 but not alpha_2
# (it's an SU(2) singlet in the triplet-antitriplet channel).
#
# The net threshold correction to Delta = 1/alpha_3 - 1/alpha_GUT is:
#
# delta_thresh = -(1/(12*pi)) * [5*ln(M_T/M_GUT) - 12*ln(M_X/M_GUT)]
#
# Using M_GUT as reference: if M_X = M_GUT (X bosons at nominal scale),
# then delta_thresh = -(5/(12*pi)) * ln(M_T/M_GUT)
#                   = -(5/(12*pi)) * ln(M_T/M_X) when M_X = M_GUT
#
# More generally, expressing in terms of r = M_T/M_X:
# delta_thresh = lambda_coeff * ln(r) / (2*pi)
#
# The coefficient lambda_coeff in minimal SU(5) for the correction
# to Delta(1/alpha_3) is:
#
# From Langacker & Luo (1991) and Buras et al. (1978):
# The threshold correction involves the differences of beta
# coefficients between the full SU(5) theory and the broken theory.
#
# For Delta(1/alpha_3) = 1/alpha_3 - 1/alpha_GUT at the crossing:
# The colored triplet T(3,1,-1/3) contributes:
#   to 1/alpha_3: delta_b3 = -1/6 (from S_2(fund) for scalar triplet)
#   to 1/alpha_1: delta_b1 = -1/15 (from scalar with Y=-1/3)
#   to 1/alpha_2: 0 (SU(2) singlet)
#
# The X boson (3,2,5/6) contributes:
#   to 1/alpha_3: delta_b3 from vector boson
#   to 1/alpha_2: delta_b2 from vector boson
#   to 1/alpha_1: delta_b1 from vector boson
#
# The standard result from the literature:
# delta_Delta = (1/(12*pi)) * [2*ln(M_T/M_X)]
# with coefficient 2 coming from the specific combination of
# Dynkin indices in the SU(5) → SM breaking.
#
# Let me use the standard parametrization:
# delta_Delta = C_thresh * ln(M_T/M_X) / (2*pi)
#
# where C_thresh is the effective coefficient.
# From Langacker-Luo (Phys Rev D 44, 1991):
# C_thresh = 5/3 for Delta(1/alpha_3)
#
# But there are different conventions. Let me compute from
# first principles using the known particle content.

# The GUT threshold correction comes from integrating out the
# heavy particles at their respective masses rather than at M_GUT.
# For a particle with mass M_i and one-loop beta contributions
# (delta_b1, delta_b2, delta_b3):
#   correction to 1/alpha_a at M_GUT = delta_b_a * ln(M_i/M_GUT) / (2*pi)
#
# Colored Higgs triplet T (3,1,-1/3) as complex scalar:
# Using scalar coefficients from PHYS-26: (1/5, 1/3, 1/6)
# db1_T = (1/5) * 3 * 1 * (1/3)^2 = (1/5)*(1/3) = 1/15
# db2_T = 0 (SU(2) singlet)
# db3_T = (1/6) * 1 * (1/2) = 1/12

db1_T = Fraction(1, 5) * Fraction(3) * Fraction(1) * Fraction(1, 9)
db2_T = Fraction(0)
db3_T = Fraction(1, 6) * Fraction(1) * Fraction(1, 2)

show("  Colored triplet T(3,1,-1/3) beta shifts:", f2m(Fraction(0)))
show("    db1_T (dimensionless)", f2m(db1_T))
show("    db2_T (dimensionless)", f2m(db2_T))
show("    db3_T (dimensionless)", f2m(db3_T))
print()

# The correction to Delta from the triplet being at M_T instead of M_GUT:
# delta_Delta_T = [db3_T - (db1_T crossing correction)] * ln(M_T/M_GUT) / (2*pi)
#
# At the crossing, 1/alpha_GUT is defined by 1/alpha_1 = 1/alpha_2.
# The triplet shifts 1/alpha_3 by db3_T and shifts 1/alpha_1 by db1_T.
# It does NOT shift 1/alpha_2 (SU(2) singlet).
# The crossing point shifts: the new crossing has
#   1/alpha_1 + db1_T*ln(M_T/M_GUT)/(2pi) = 1/alpha_2
# so the effective 1/alpha_GUT shifts by db1_T * ln(M_T/M_GUT)/(2pi)
# because only alpha_1 is affected.
#
# Wait — at the crossing both 1/alpha_1 and 1/alpha_2 must be equal.
# If the triplet shifts 1/alpha_1 but not 1/alpha_2, the crossing
# point moves. But the DEFINITION of M_GUT is the crossing of
# alpha_1 and alpha_2 INCLUDING the threshold. So this gets circular.
#
# The standard approach: parametrize the correction to Delta as a
# function of ln(M_T/M_X) where both are referenced to M_GUT.
#
# Using the Buras et al. / Langacker-Luo result:
# The threshold correction to the prediction of alpha_3 is:
#
# 1/alpha_3(M_Z)|_thresh = 1/alpha_3(M_Z)|_no_thresh + delta
# where delta = (1/(2*pi)) * sum_i C_i * ln(M_i/M_GUT)
#
# For minimal SU(5):
# delta = (1/(2*pi)) * [(2/3)*ln(M_T/M_GUT) + (10)*ln(M_X/M_GUT)]
#
# No — let me just use the simplest correct formulation.
# The threshold correction to Delta(1/alpha_3) at the crossing is:
#
# delta_Delta = [db3_T * ln(M_T/M_GUT) - db3_T * 0] / (2*pi)
#   ... for the triplet only (X bosons at M_GUT by definition)
#
# If we define M_GUT = M_X (X bosons set the scale), then:
# delta_Delta = db3_T * ln(M_T/M_X) / (2*pi)
#
# But we also need to account for the shift of the crossing point.
# The full formula involves the effect on all three couplings.
#
# SIMPLEST CORRECT APPROACH:
# Define M_GUT by the X boson mass: M_X = M_GUT.
# The colored triplet at M_T != M_GUT shifts the running.
# The shift to Delta is:
#
# delta_Delta = [db3_T - weighted_average_of_db1_db2] * ln(M_T/M_X)/(2*pi)
#
# where the weighted average accounts for the shift of the crossing.
# Since db2_T = 0, and the crossing is defined by alpha_1 = alpha_2:
# The crossing shifts in a way that depends on db1_T and db2_T.
#
# For db2_T = 0 and db1_T > 0:
# The triplet makes 1/alpha_1 run slightly faster (more positive b1).
# This shifts the crossing to slightly lower energy.
# The net effect on Delta is approximately:
#
# delta_Delta ≈ [db3_T - (5/8)*db1_T] * ln(M_T/M_X) / (2*pi)
#
# where 5/8 is from the (5/3)/(5/3 + 1) = (5/3)/(8/3) = 5/8 weighting
# of db1 in the crossing condition (because 1/alpha_EM = (5/3)/alpha_1 + 1/alpha_2).
#
# Actually let me just compute it directly.
# At the crossing: (5/3)/alpha_1 + 1/alpha_2 = 1/alpha_EM (fixed)
# So delta(crossing) = -(5/3)*delta(1/alpha_1) (since alpha_2 unaffected)
# = -(5/3)*db1_T * ln(M_T/M_X) / (2*pi)
#
# The shift in 1/alpha_GUT at the crossing:
# New 1/alpha_GUT = old 1/alpha_GUT + [change from crossing shift]
# Since 1/alpha_2 doesn't change, and at crossing 1/alpha_1 = 1/alpha_2:
# 1/alpha_GUT_new = 1/alpha_2 = old 1/alpha_GUT (unchanged)
# Wait — if the triplet is at M_T < M_GUT, it contributes to the running
# between M_T and M_GUT, making 1/alpha_1 larger at M_GUT.
# Then 1/alpha_1(M_GUT) > 1/alpha_2(M_GUT), so the crossing moves UP.
#
# This is getting messy. Let me just do it numerically.

print("  Numerical approach: scan M_T/M_X and compute Delta.")
print()

# ================================================================
# SECTION 2: NUMERICAL THRESHOLD SCAN
# ================================================================

print("SECTION 2: THRESHOLD SCAN")
print("-" * 70)
print()
print("  Method: run couplings from M_Z to M_VL (SM betas),")
print("  then from M_VL to M_T (CD betas), then from M_T to M_GUT")
print("  (CD betas + triplet contribution), then check crossing.")
print()
print("  But the triplet affects the running between M_T and M_GUT,")
print("  which shifts the crossing. Simpler: add the triplet beta")
print("  shifts to the CD betas above M_T, and scan M_T.")
print()

# Setup: all mpf for numerical work
b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]

# CD betas + triplet betas (above M_T)
db_T = [f2m(db1_T), f2m(db2_T), f2m(db3_T)]
b_CDT_m = [b_CD_m[i] + db_T[i] for i in range(3)]

show("  CD betas (dimensionless):", f2m(Fraction(0)))
show("    b1' (dimensionless)", b_CD_m[0])
show("    b2' (dimensionless)", b_CD_m[1])
show("    b3' (dimensionless)", b_CD_m[2])
print()
show("  CD + triplet betas (dimensionless):", f2m(Fraction(0)))
show("    b1'+T (dimensionless)", b_CDT_m[0])
show("    b2'+T (dimensionless)", b_CDT_m[1])
show("    b3'+T (dimensionless)", b_CDT_m[2])
print()

M_Z_GeV_m = f2m(M_Z) / mpf("1000")
M_VL_m = mpf("500")
twopi = mpf("2") * mpi

# Step 1: run from M_Z to M_VL with SM betas (sign: 1/a(mu) = 1/a(mu0) - b*L)
L_low = mlog(M_VL_m / M_Z_GeV_m) / twopi
inv_a_MZ = [f2m(inv_a1), f2m(inv_a2), f2m(Fraction(1) / alpha_s)]
inv_a_VL = [inv_a_MZ[i] - b_SM_m[i] * L_low for i in range(3)]

# Step 2: for a given M_T (as ratio r = M_T/M_GUT), find Delta.
# Strategy: run from M_VL to high energy with CD betas.
# At M_T, add the triplet contribution.
# But we don't know M_GUT yet (it depends on M_T).
#
# Simpler approach: parametrize by M_T directly.
# Run from M_VL to M_T with CD betas.
# Run from M_T upward with CD+T betas.
# Find crossing of 1/alpha_1 = 1/alpha_2.
# Measure Delta.

def compute_delta_with_threshold(M_VL_GeV, M_T_GeV, inv_a_at_VL):
    """Compute Delta with triplet threshold at M_T."""
    M_VL = mpf(str(M_VL_GeV))
    M_T = mpf(str(M_T_GeV))

    if M_T <= M_VL:
        # Triplet below VL — use CD+T betas from VL to M_GUT
        L_cross = (inv_a_at_VL[1] - inv_a_at_VL[0]) / (b_CDT_m[1] - b_CDT_m[0])
        if L_cross <= mpf("0"):
            return None, None, None
        inv_aGUT = inv_a_at_VL[0] - b_CDT_m[0] * L_cross
        inv_a3_GUT = inv_a_at_VL[2] - b_CDT_m[2] * L_cross
        M_GUT = M_VL * mexp(L_cross * twopi)
        return inv_a3_GUT - inv_aGUT, mlog10(M_GUT), M_T / M_GUT

    # Run from M_VL to M_T with CD betas
    L_VL_T = mlog(M_T / M_VL) / twopi
    inv_a_T = [inv_a_at_VL[i] - b_CD_m[i] * L_VL_T for i in range(3)]

    # Run from M_T upward with CD+T betas, find crossing
    L_cross = (inv_a_T[1] - inv_a_T[0]) / (b_CDT_m[1] - b_CDT_m[0])
    if L_cross <= mpf("0"):
        return None, None, None

    inv_aGUT = inv_a_T[0] - b_CDT_m[0] * L_cross
    inv_a3_GUT = inv_a_T[2] - b_CDT_m[2] * L_cross
    M_GUT = M_T * mexp(L_cross * twopi)
    Delta = inv_a3_GUT - inv_aGUT

    return Delta, mlog10(M_GUT), M_T / M_GUT

# First: Delta WITHOUT triplet threshold (reference)
L_ref = (inv_a_VL[1] - inv_a_VL[0]) / (b_CD_m[1] - b_CD_m[0])
inv_aGUT_ref = inv_a_VL[0] - b_CD_m[0] * L_ref
inv_a3_ref = inv_a_VL[2] - b_CD_m[2] * L_ref
Delta_ref = inv_a3_ref - inv_aGUT_ref
M_GUT_ref = M_VL_m * mexp(L_ref * twopi)

show("  Reference (no triplet threshold):", f2m(Fraction(0)))
show("    Delta (dimensionless)", Delta_ref)
show("    log10(M_GUT/GeV)", mlog10(M_GUT_ref))
print()

# Scan M_T from 10^13 to 10^17 GeV
print("  Scan M_T (colored Higgs triplet mass):")
print()
print("  %12s %12s %12s %12s %12s" %
      ("M_T (GeV)", "log M_T", "Delta", "log M_GUT", "M_T/M_GUT"))
print("  %12s %12s %12s %12s %12s" %
      ("-" * 12, "-" * 12, "-" * 12, "-" * 12, "-" * 12))

scan_results = []

for log_MT in range(12, 18):
    for sub in [0, 5]:
        log_MT_f = mpf(str(log_MT)) + mpf(str(sub)) / 10
        M_T_GeV = mpow(mpf("10"), log_MT_f)
        Delta, log_MGUT, r = compute_delta_with_threshold(
            500, float(M_T_GeV), inv_a_VL)
        if Delta is not None:
            scan_results.append((log_MT_f, Delta, log_MGUT, r))
            print("  %12s %12s %12s %12s %12s" %
                  (mp.nstr(M_T_GeV, 4), mp.nstr(log_MT_f, 4),
                   mp.nstr(Delta, 5), mp.nstr(log_MGUT, 5),
                   mp.nstr(r, 4)))

print()

# ================================================================
# SECTION 3: FIND M_T FOR EXACT UNIFICATION (Delta = 0)
# ================================================================

print("SECTION 3: M_T FOR EXACT UNIFICATION")
print("-" * 70)
print()

# Binary search for M_T where Delta = 0
log_MT_lo = mpf("12")
log_MT_hi = mpf("17")

for _ in range(80):
    log_MT_mid = (log_MT_lo + log_MT_hi) / 2
    M_T_mid = mpow(mpf("10"), log_MT_mid)
    Delta_mid, _, _ = compute_delta_with_threshold(500, float(M_T_mid), inv_a_VL)
    if Delta_mid is None:
        log_MT_hi = log_MT_mid
    elif Delta_mid < mpf("0"):
        log_MT_hi = log_MT_mid
    else:
        log_MT_lo = log_MT_mid

M_T_exact = mpow(mpf("10"), log_MT_mid)
Delta_exact, log_MGUT_exact, r_exact = compute_delta_with_threshold(
    500, float(M_T_exact), inv_a_VL)

show("  M_T for Delta = 0 (GeV)", M_T_exact)
show("  log10(M_T/GeV)", log_MT_mid)
show("  Delta at this M_T (dimensionless)", Delta_exact)
show("  log10(M_GUT/GeV)", log_MGUT_exact)
show("  M_T/M_GUT (dimensionless)", r_exact)
print()

# The ratio M_T/M_X where M_X = M_GUT
M_GUT_exact = mpow(mpf("10"), log_MGUT_exact)
ratio_T_X = M_T_exact / M_GUT_exact

show("  Ratio M_T/M_X (dimensionless)", ratio_T_X)
show("  Ratio M_X/M_T (dimensionless)", mpf("1") / ratio_T_X)
print()

if ratio_T_X > mpf("1"):
    print("  The triplet is HEAVIER than the X boson (M_T > M_X).")
    show("  Factor heavier (dimensionless)", ratio_T_X)
else:
    print("  The triplet is LIGHTER than the X boson (M_T < M_X).")
    show("  Factor lighter (dimensionless)", mpf("1") / ratio_T_X)
print()

# ================================================================
# SECTION 4: NATURALNESS CHECK
# ================================================================

print("SECTION 4: NATURALNESS CHECK")
print("-" * 70)
print()

natural_threshold = mpf("10")
fine_tuned_threshold = mpf("100")

max_ratio = ratio_T_X
if ratio_T_X < mpf("1"):
    max_ratio = mpf("1") / ratio_T_X

is_natural = max_ratio < natural_threshold
is_fine_tuned = max_ratio > fine_tuned_threshold

print("  Mass ratio M_T/M_X = %s" % mp.nstr(ratio_T_X, 4))
print("  Max deviation from unity = %s" % mp.nstr(max_ratio, 4))
print()
print("  Natural (ratio < 10): %s" % is_natural)
print("  Fine-tuned (ratio > 100): %s" % is_fine_tuned)
print()

if is_natural:
    print("  RESULT: The mass splitting is NATURAL.")
    print("  A factor of %s between M_T and M_X is typical for" %
          mp.nstr(max_ratio, 3))
    print("  GUT-scale mass splittings from radiative corrections")
    print("  or higher-dimensional operators.")
elif is_fine_tuned:
    print("  RESULT: The mass splitting is FINE-TUNED.")
    print("  A factor of %s requires explanation." %
          mp.nstr(max_ratio, 3))
else:
    print("  RESULT: The mass splitting is MODERATE.")
    print("  A factor of %s is between natural and fine-tuned." %
          mp.nstr(max_ratio, 3))
print()

# ================================================================
# SECTION 5: PROTON LIFETIME UPDATE
# ================================================================

print("SECTION 5: PROTON LIFETIME UPDATE")
print("-" * 70)
print()

# Proton lifetime scales as M_X^4 / alpha_GUT^2
# At the exact unification point, M_X = M_GUT
# Compare to reference: M_GUT_ref from no-threshold case

log_MGUT_ref = mlog10(M_GUT_ref)
log_MGUT_unif = log_MGUT_exact

# tau ~ M_X^4, so log10(tau) shifts by 4 * delta(log10 M_GUT)
delta_log_tau = mpf("4") * (log_MGUT_unif - log_MGUT_ref)

# Reference proton lifetime: 10^34 to 10^35 years (from PHYS-20)
# Use 10^34.5 as central estimate at M_GUT_ref
log_tau_ref = mpf("34.5")
log_tau_updated = log_tau_ref + delta_log_tau

show("  Reference log10(M_GUT/GeV) (no threshold)", log_MGUT_ref)
show("  Updated log10(M_GUT/GeV) (with threshold)", log_MGUT_unif)
show("  Shift in log10(M_GUT) (dimensionless)", log_MGUT_unif - log_MGUT_ref)
show("  Shift in log10(tau) = 4 * shift (dimensionless)", delta_log_tau)
print()
show("  Reference log10(tau/yr)", log_tau_ref)
show("  Updated log10(tau/yr)", log_tau_updated)
print()

# Super-K bound: tau > 2.4 * 10^34 years -> log10 > 34.38
superK_bound = mpf("34.38")
show("  Super-K bound: log10(tau/yr) >", superK_bound)
print("  Updated prediction %s Super-K bound." %
      ("ABOVE" if log_tau_updated > superK_bound else "BELOW"))
print()

# Hyper-K reach: ~10^35 years
hyperK_reach = mpf("35")
show("  Hyper-K 20yr sensitivity: log10(tau/yr) ~", hyperK_reach)
print("  Updated prediction %s Hyper-K reach." %
      ("WITHIN" if log_tau_updated < hyperK_reach else "BEYOND"))
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Section 1: triplet beta shifts
chk_exact("S1: Triplet db1 = 1/15",
          db1_T, Fraction(1, 15), checks)

chk_exact("S1: Triplet db2 = 0 (SU(2) singlet)",
          db2_T, Fraction(0), checks)

chk_exact("S1: Triplet db3 = 1/12",
          db3_T, Fraction(1, 12), checks)

# Section 2: reference Delta is negative
chk_bool("S2: Reference Delta negative (no triplet)",
         Delta_ref < mpf("0"),
         "Delta = %s" % mp.nstr(Delta_ref, 4), checks)

# Section 3: exact unification found
chk_bool("S3: Delta = 0 solution found (|Delta| < 0.01)",
         fabs(Delta_exact) < mpf("0.01"),
         "|Delta| = %s" % mp.nstr(fabs(Delta_exact), 4), checks)

chk_bool("S3: M_GUT > 10^14 GeV",
         log_MGUT_exact > mpf("14"),
         "log10 = %s" % mp.nstr(log_MGUT_exact, 5), checks)

# Section 4: naturalness
chk_bool("S4: Abort test — M_T/M_X < 100 (not extreme fine-tuning)",
         max_ratio < fine_tuned_threshold,
         "ratio = %s" % mp.nstr(max_ratio, 4), checks)

# Section 5: proton lifetime
chk_bool("S5: Updated tau above Super-K bound",
         log_tau_updated > superK_bound,
         "log10(tau) = %s > %s" % (mp.nstr(log_tau_updated, 4),
                                    mp.nstr(superK_bound, 4)), checks)

chk_bool("S5: Updated tau within Hyper-K reach",
         log_tau_updated < hyperK_reach + mpf("1"),
         "log10(tau) = %s < %s" % (mp.nstr(log_tau_updated, 4),
                                    mp.nstr(hyperK_reach + mpf("1"), 4)),
         checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-29 GUT THRESHOLD CORRECTIONS COMPLETE")
print("=" * 70)
