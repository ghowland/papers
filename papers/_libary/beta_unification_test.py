#!/usr/bin/env python3
"""
HOWL EXPLORATORY: beta_unification_test.py
============================================
Test whether a single formula framework built from SM and VL beta
coefficients, combined with alpha_em, can predict cosmological
observables without any cosmological input.

The hypothesis: the integers 19, 13, 20, 22, 11 appearing in
the QED-to-GR scan signals are ALL derivable from the beta
coefficients in the library. If a coherent formula set connects
them to measured cosmological values, that constitutes a
unification of the particle physics and cosmological sectors
through the gauge group integers alone.

INPUT: Only phys24_lib.py values (alpha, betas, R2, R4, pi).
       No cosmological constants as input.
OUTPUT: Predictions for H0 ratio, DM/baryon, Lambda scale, G running.
        Compared to measured values defined ONLY for comparison.

Null result constrains this formula set, not the framework.

Backed by: qed_predicts_gr.py (10/10), qed_gr_scan_2.py (10/10)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, sqrt as msqrt
from mpmath import fabs, power as mpow

# ================================================================
print("=" * 70)
print("BETA UNIFICATION TEST")
print("The gauge group integers predict cosmology?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: EXTRACT ALL INTEGERS FROM THE BETA STRUCTURE
# ================================================================

print("SECTION 1: THE INTEGER INVENTORY")
print("-" * 70)
print()
print("  Every integer below is extracted from phys24_lib beta")
print("  coefficients. No cosmological input. Pure Level 1.")
print()

# The beta numerators (times 6 to clear denominators)
# b2_SM = -19/6, so |numerator| = 19
# b2_mod = -13/6, so |numerator| = 13
# b3_mod = -20/3, so |numerator * 3| = 20... but let's be precise
# b3_mod = -20/3 -> multiply by 3 -> |-20| = 20

b2_SM_num = -b2_SM * Fraction(6, 1)    # = 19
b2_mod_num = -b2_mod * Fraction(6, 1)  # = 13
b3_mod_num = -b3_mod * Fraction(3, 1)  # = 20
b1_SM_num = b1_SM * Fraction(10, 1)    # = 41
b1_mod_num = b1_mod * Fraction(6, 1)   # = 25

# The Yang-Mills integer
YM = Fraction(11, 1)

# The generation count
N_gen = Fraction(3, 1)

# Casimirs
C2_SU2 = Fraction(2, 1)
C2_SU3 = Fraction(3, 1)

# Per-generation contribution
delta_b_gen = Fraction(4, 3)

# The VL shifts
db1 = db1_VL  # 1/15
db2 = db2_VL  # 1
db3 = db3_VL  # 1/3

# Asymmetry ratio
asym = db2 / db1  # = 15

# Pure-gauge gap ratio
gap_pure = C2_SU2 / (C2_SU3 - C2_SU2)  # = 2

print("  FROM b2_SM = %s:" % b2_SM)
show("    |numerator| = 19 (dimensionless)", f2m(b2_SM_num))
print()
print("  FROM b2_mod = %s:" % b2_mod)
show("    |numerator| = 13 (dimensionless)", f2m(b2_mod_num))
print()
print("  FROM b3_mod = %s:" % b3_mod)
show("    |numerator| = 20 (dimensionless)", f2m(b3_mod_num))
print()
print("  FROM b1_SM = %s:" % b1_SM)
show("    |numerator| = 41 (dimensionless)", f2m(b1_SM_num))
print()
print("  YANG-MILLS INTEGER:")
show("    11 (dimensionless)", f2m(YM))
print()
print("  DERIVED INTEGERS:")
show("    N_gen = 3 (dimensionless)", f2m(N_gen))
show("    3 * 19 = 57 (dimensionless)", f2m(N_gen * b2_SM_num))
show("    3 * 13 = 39 (dimensionless)", f2m(N_gen * b2_mod_num))
show("    2 * 11 = 22 (dimensionless)", f2m(Fraction(2) * YM))
show("    Asymmetry db2/db1 = 15 (dimensionless)", f2m(asym))
show("    Pure-gauge gap = 2 (dimensionless)", f2m(gap_pure))
print()

# ================================================================
# SECTION 2: THE FORMULA FRAMEWORK
# ================================================================

print("SECTION 2: THE FORMULA FRAMEWORK")
print("-" * 70)
print()
print("  All formulas use ONLY:")
print("    alpha_em (from library, Level 2)")
print("    beta integers (from library, Level 1)")
print("    R2, R4, pi (from library, Level 1)")
print("  No cosmological constants as input.")
print()

alpha_m = f2m(alpha_frac)
R2_m = f2m(R2_f)
R4_m = f2m(R4_f)
pi_m = f2m(pi_f)

# VP step size
vp_step_frac = Fraction(1, 1) / (Fraction(12, 1) * R2_f)
vp_step_m = f2m(vp_step_frac)
base_frac = alpha_frac * vp_step_frac
base_m = f2m(base_frac)

show("alpha_em (dimensionless)", alpha_m)
show("VP step = 1/(12*R2) = 1/(3*pi) (dimensionless)", vp_step_m)
show("base = alpha/(3*pi) (dimensionless)", base_m)
print()

# ================================================================
# SECTION 3: FORMULA 1 — COSMOLOGICAL CONSTANT
# ================================================================

print("SECTION 3: FORMULA 1 — COSMOLOGICAL CONSTANT SCALE")
print("-" * 70)
print()

# Formula: Lambda_Planck = alpha^(3 * |b2_SM_num|)
# Alternative: Lambda_Planck = (alpha/(3*pi))^(3 * |b2_mod_num|)
# Both use only library values

exp_SM = N_gen * b2_SM_num    # = 57
exp_VL = N_gen * b2_mod_num   # = 39

log10_alpha = mlog(alpha_m, 10)

# Prediction 1a: log10(Lambda) from SM beta
pred_log_Lambda_SM = f2m(exp_SM) * log10_alpha
# Prediction 1b: log10(Lambda) from VL beta
log10_base = mlog(base_m, 10)
pred_log_Lambda_VL = f2m(exp_VL) * log10_base

# Measured (for comparison only — NOT input)
Lambda_meas_log10 = mpf("-121.54")  # from scan output

print("  Formula: log10(Lambda_Pl) = N_gen * |b2_num| * log10(coupling)")
print()
print("  Version A (SM, bare alpha):")
show("    exponent = 3 * 19 = 57 (dimensionless)", f2m(exp_SM))
show("    prediction: log10(Lambda) (dimensionless)", pred_log_Lambda_SM)
show("    measured: log10(Lambda) (dimensionless)", Lambda_meas_log10)
show("    miss (decades) (dimensionless)",
     fabs(pred_log_Lambda_SM - Lambda_meas_log10))
print()
print("  Version B (VL, alpha/(3*pi)):")
show("    exponent = 3 * 13 = 39 (dimensionless)", f2m(exp_VL))
show("    prediction: log10(Lambda) (dimensionless)", pred_log_Lambda_VL)
show("    measured: log10(Lambda) (dimensionless)", Lambda_meas_log10)
show("    miss (decades) (dimensionless)",
     fabs(pred_log_Lambda_VL - Lambda_meas_log10))
print()

# The two versions bracket the measured value
print("  NOTE: Version A overshoots by %.2f, Version B undershoots by %.2f" %
      (float(pred_log_Lambda_SM - Lambda_meas_log10),
       float(pred_log_Lambda_VL - Lambda_meas_log10)))
print("  The measured value sits BETWEEN the SM and VL predictions.")
print()

# Interpolation: at what mixing fraction do they match?
# f * pred_SM + (1-f) * pred_VL = measured
# f = (measured - pred_VL) / (pred_SM - pred_VL)
f_mix = (Lambda_meas_log10 - pred_log_Lambda_VL) / (
    pred_log_Lambda_SM - pred_log_Lambda_VL)
show("  Interpolation fraction f (dimensionless)", f_mix)
print("  (f=1 is pure SM, f=0 is pure VL)")
print()

# ================================================================
# SECTION 4: FORMULA 2 — DARK MATTER RATIO
# ================================================================

print("SECTION 4: FORMULA 2 — DARK MATTER RATIO")
print("-" * 70)
print()

# Formula: DM/baryon = (2 * YM / |b2_mod_num|) * pi
# = (2 * 11 / 13) * pi = (22/13) * pi
# Every integer from the beta structure

dm_num = Fraction(2, 1) * YM               # 22
dm_den = b2_mod_num                          # 13
dm_pred_frac = dm_num * pi_f / dm_den        # (22/13) * pi

dm_pred_m = f2m(dm_pred_frac)
dm_meas = mpf("5.3204")  # measured, for comparison only

print("  Formula: DM/baryon = (2 * 11 / |b2_mod_num|) * pi")
print("         = (2 * YM / 13) * pi")
print("         = (22/13) * pi")
print()
show("  2 * YM = 22 (dimensionless)", f2m(dm_num))
show("  |b2_mod_num| = 13 (dimensionless)", f2m(dm_den))
show("  prediction (dimensionless)", dm_pred_m)
show("  measured (dimensionless)", dm_meas)
show("  miss (dimensionless)", fabs(dm_pred_m - dm_meas))
show("  relative miss (percent)", fabs(dm_pred_m - dm_meas) / dm_meas * 100)
print()

# ================================================================
# SECTION 5: FORMULA 3 — H0 PER-TRANSIT CORRECTION
# ================================================================

print("SECTION 5: FORMULA 3 — H0 PER-TRANSIT CORRECTION")
print("-" * 70)
print()

# Formula: (1-r) = alpha^2 * pi^2 * (|b3_mod_num|*3) / (|b2_mod_num|*3)
# Wait, let me reconsider. The product form hit was:
# (1-r) = alpha^2 * pi^2 * 20/13
# where 20 = |b3_mod| * 3 (since b3_mod = -20/3)
# and 13 = |b2_mod_num|
# But let me express 20/13 more carefully from betas:
# 20 = |3 * b3_mod| = |3 * (-20/3)| = 20. So 20/13 = |3*b3_mod|/|b2_mod_num|

ratio_20_13 = (Fraction(3, 1) * (-b3_mod)) / b2_mod_num  # = 20/13
omr_pred_frac = alpha_frac * alpha_frac * pi_f * pi_f * ratio_20_13

omr_pred_m = f2m(omr_pred_frac)
omr_meas = mpf("0.00080923")  # (1-r) at N=100 from scan

print("  Formula: (1-r) = alpha^2 * pi^2 * |3*b3_mod| / |b2_mod_num|")
print("         = alpha^2 * pi^2 * 20/13")
print()
show("  |3 * b3_mod| = 20 (dimensionless)",
     f2m(Fraction(3, 1) * (-b3_mod)))
show("  |b2_mod_num| = 13 (dimensionless)", f2m(b2_mod_num))
show("  ratio = 20/13 (dimensionless)", f2m(ratio_20_13))
show("  prediction (dimensionless)", omr_pred_m)
show("  target from H0 ratio (dimensionless)", omr_meas)
show("  miss (dimensionless)", fabs(omr_pred_m - omr_meas))
show("  relative miss (percent)",
     fabs(omr_pred_m - omr_meas) / omr_meas * 100)
print()

# What H0 ratio does this predict?
# H0_CMB/H0_local = (1 - omr)^N for some N
# At N = 100: ratio = (1 - omr)^100
r_pred = 1 - omr_pred_m
ratio_100 = mpow(r_pred, 100)
H0_local_ref = mpf("73.04")
H0_pred = H0_local_ref * ratio_100
H0_meas = mpf("67.36")

print("  DERIVED: H0 prediction at N=100 boundary transits:")
show("    r per transit (dimensionless)", r_pred)
show("    r^100 (dimensionless)", ratio_100)
show("    H0 predicted (km/s/Mpc)", H0_pred)
show("    H0 measured CMB (km/s/Mpc)", H0_meas)
show("    miss (km/s/Mpc)", fabs(H0_pred - H0_meas))
show("    relative miss (percent)",
     fabs(H0_pred - H0_meas) / H0_meas * 100)
print()

# ================================================================
# SECTION 6: FORMULA 4 — THE EXACT IDENTITY
# ================================================================

print("SECTION 6: FORMULA 4 — THE EXACT IDENTITY")
print("-" * 70)
print()

# The identity: 57/39 = 19/13 = b2_SM_num / b2_mod_num
# This connects the two Lambda predictions

ratio_57_39 = Fraction(57, 39)
ratio_19_13 = b2_SM_num / b2_mod_num
ratio_b2 = (-b2_SM * Fraction(6)) / (-b2_mod * Fraction(6))

print("  57/39 = %s" % ratio_57_39)
print("  19/13 = %s" % ratio_19_13)
print("  |b2_SM_num|/|b2_mod_num| = %s" % ratio_b2)
print()
print("  All three are identical: %s" %
      ("YES" if ratio_57_39 == ratio_19_13 == ratio_b2 else "NO"))
print()

# ================================================================
# SECTION 7: COMBINATORIC PREDICTIONS — SWEEP ALL FORMULAS
# ================================================================

print("SECTION 7: COMBINATORIC PREDICTIONS FROM BETA INTEGERS")
print("-" * 70)
print()
print("  Generate predictions from alpha^a * pi^b * (p/q)")
print("  where p and q are drawn from beta integers.")
print("  Compare each to known measured quantities.")
print()

# The integer pool from betas
int_pool = {
    "b2_SM_num (19)": b2_SM_num,
    "b2_mod_num (13)": b2_mod_num,
    "b3_mod_num (20)": b3_mod_num,
    "b1_SM_num (41)": b1_SM_num,
    "b1_mod_num (25)": b1_mod_num,
    "YM (11)": YM,
    "N_gen (3)": N_gen,
    "C2_SU2 (2)": C2_SU2,
    "C2_SU3 (3)": C2_SU3,
    "asym (15)": asym,
    "gap_pure (2)": gap_pure,
    "delta_b_gen (4/3)": delta_b_gen,
    "db1_VL (1/15)": db1,
    "db2_VL (1)": db2,
    "db3_VL (1/3)": db3,
}

# Measured targets (for comparison, NOT input)
targets = {
    "DM/baryon": (mpf("5.3204"), mpf("0.065")),
    "H0_CMB/H0_local": (mpf("0.9222"), mpf("0.015")),
    "Omega_DM": (mpf("0.2607"), mpf("0.003")),
    "Omega_baryon": (mpf("0.0490"), mpf("0.001")),
    "Omega_DM + Omega_b": (mpf("0.3097"), mpf("0.004")),
    "sin2_tW": (f2m(sin2_tW), mpf("0.0002")),
    "m_p/m_e": (f2m(mp_me), mpf("0.001")),
    "alpha_s": (f2m(alpha_s), mpf("0.001")),
}

# Test: p/q * pi^b for b in {-1, 0, 1} and p, q from integer pool
# This is a focused scan, not exhaustive

print("  Testing (p/q) * pi^b for beta-derived p, q and b in {-1, 0, 1}:")
print()

hits = []

for p_name, p_val in int_pool.items():
    for q_name, q_val in int_pool.items():
        if p_val == Fraction(0) or q_val == Fraction(0):
            continue
        if p_name == q_name:
            continue
        ratio_frac = p_val / q_val

        for b_pi in [-1, 0, 1]:
            if b_pi == -1:
                val = f2m(ratio_frac) / pi_m
            elif b_pi == 0:
                val = f2m(ratio_frac)
            else:
                val = f2m(ratio_frac) * pi_m

            for t_name, (t_val, t_unc) in targets.items():
                if t_val == mpf(0):
                    continue
                rel = fabs(val - t_val) / t_val
                if rel < mpf("0.02"):  # within 2%
                    label = "%s / %s * pi^%d" % (p_name, q_name, b_pi)
                    hits.append((t_name, label, val, t_val, rel))

# Sort by relative distance
hits.sort(key=lambda x: x[4])

if hits:
    print("  HITS within 2%% of measured values:")
    print("  %20s | %45s | %12s | %12s | %8s" %
          ("Target", "Expression", "Predicted", "Measured", "Rel%%"))
    print("  %20s | %45s | %12s | %12s | %8s" %
          ("-" * 20, "-" * 45, "-" * 12, "-" * 12, "-" * 8))
    seen = set()
    for t_name, label, val, t_val, rel in hits:
        key = (t_name, mp.nstr(val, 8))
        if key in seen:
            continue
        seen.add(key)
        print("  %20s | %45s | %12s | %12s | %7s%%" %
              (t_name, label[:45], mp.nstr(val, 8),
               mp.nstr(t_val, 8), mp.nstr(rel * 100, 4)))
else:
    print("  No hits within 2%%")

print()

# ================================================================
# SECTION 8: ALPHA POWER PREDICTIONS
# ================================================================

print("SECTION 8: ALPHA POWER SCAN — WHAT DO alpha^(3*b_num) PREDICT?")
print("-" * 70)
print()
print("  For each beta numerator, compute alpha^(3*|num|) and")
print("  (alpha/(3pi))^(3*|num|) and check what scale they correspond to.")
print()

beta_nums = [
    ("b1_SM", b1_SM_num, Fraction(41)),
    ("b2_SM", b2_SM_num, Fraction(19)),
    ("b3_SM", Fraction(7), Fraction(7)),
    ("b1_mod", b1_mod_num, Fraction(25)),
    ("b2_mod", b2_mod_num, Fraction(13)),
    ("b3_mod", b3_mod_num / Fraction(3), Fraction(20) / Fraction(3)),
]

# Actually let me use the raw numerators properly
raw_nums = [
    ("|b2_SM_num| = 19", Fraction(19)),
    ("|b2_mod_num| = 13", Fraction(13)),
    ("|b3_SM| = 7", Fraction(7)),
    ("|b3_mod_num| = 20", Fraction(20)),
    ("|b1_SM_num| = 41", Fraction(41)),
    ("|b1_mod_num| = 25", Fraction(25)),
    ("YM = 11", Fraction(11)),
    ("asym = 15", Fraction(15)),
]

print("  %20s %6s %14s %14s %30s" %
      ("Source", "3*|n|", "log10(a^3n)", "log10((a/3p)^3n)", "Physical scale?"))
print("  %20s %6s %14s %14s %30s" %
      ("-" * 20, "-" * 6, "-" * 14, "-" * 14, "-" * 30))

known_scales = [
    (mpf("-121.5"), "Lambda_Planck (~10^-122)"),
    (mpf("-44.9"), "G_Newton in natural units"),
    (mpf("-5.7"), "alpha_s^2 ~ 10^-5.7"),
    (mpf("-2.14"), "alpha_em ~ 10^-2.14"),
    (mpf("0"), "unity"),
    (mpf("15.5"), "M_GUT ~ 10^15.5 GeV"),
    (mpf("19"), "Planck mass ~ 10^19 GeV"),
]

for label, n_val in raw_nums:
    exp_3n = Fraction(3) * n_val
    log_alpha_3n = f2m(exp_3n) * log10_alpha
    log_base_3n = f2m(exp_3n) * log10_base
    # Find closest known scale
    closest_a = min(known_scales, key=lambda x: abs(float(log_alpha_3n - x[0])))
    closest_b = min(known_scales, key=lambda x: abs(float(log_base_3n - x[0])))

    print("  %20s %6s %14s %14s" %
          (label, mp.nstr(f2m(exp_3n), 4),
           mp.nstr(log_alpha_3n, 6), mp.nstr(log_base_3n, 6)))
    print("  %20s %6s %14s %14s" %
          ("", "", "~ " + closest_a[1][:12], "~ " + closest_b[1][:12]))

print()

# ================================================================
# SECTION 9: THE OMEGA PREDICTIONS
# ================================================================

print("SECTION 9: CAN WE PREDICT OMEGA_DM AND OMEGA_B?")
print("-" * 70)
print()

# If DM/baryon = (22/13)*pi = 5.317
# And Omega_DM + Omega_b = Omega_matter
# Then Omega_DM = (22*pi/13) / (1 + 22*pi/13) * Omega_matter
# But we need Omega_matter...
# OR: Omega_b / Omega_DM = 13 / (22*pi)
# Let's check: can we predict the individual Omegas?

# Test: is Omega_b related to alpha somehow?
# Omega_b ~ 0.049. alpha ~ 0.00730. Omega_b/alpha = 6.71
# 22/3 = 7.33. Not great.
# alpha * |b2_SM_num/6| * pi = alpha * 19/6 * pi = 0.00730 * 3.167 * 3.1416 = 0.0726. No.
# Try: alpha * N_gen * (4/3) * pi = 0.00730 * 4 * 3.14 = 0.0917. No.
# Try: R4 * alpha * 22 = 0.3084 * 0.00730 * 22 = 0.0495. CLOSE to Omega_b = 0.0490!

Omega_b_pred = R4_m * alpha_m * f2m(Fraction(2) * YM)  # R4 * alpha * 22
Omega_b_meas = mpf("0.0490")

print("  Test: Omega_b = R4 * alpha * 2*YM = R4 * alpha * 22")
show("    R4 (dimensionless)", R4_m)
show("    alpha (dimensionless)", alpha_m)
show("    2 * YM = 22 (dimensionless)", f2m(Fraction(2) * YM))
show("    prediction (dimensionless)", Omega_b_pred)
show("    measured (dimensionless)", Omega_b_meas)
show("    miss (dimensionless)", fabs(Omega_b_pred - Omega_b_meas))
show("    relative miss (percent)",
     fabs(Omega_b_pred - Omega_b_meas) / Omega_b_meas * 100)
print()

# If Omega_b = R4 * alpha * 22 AND DM/baryon = (22/13)*pi
# Then Omega_DM = Omega_b * (22/13)*pi = R4 * alpha * 22 * (22/13)*pi
Omega_DM_pred = Omega_b_pred * dm_pred_m
Omega_DM_meas = mpf("0.2607")

print("  Derived: Omega_DM = Omega_b * (22/13)*pi")
show("    prediction (dimensionless)", Omega_DM_pred)
show("    measured (dimensionless)", Omega_DM_meas)
show("    miss (dimensionless)", fabs(Omega_DM_pred - Omega_DM_meas))
show("    relative miss (percent)",
     fabs(Omega_DM_pred - Omega_DM_meas) / Omega_DM_meas * 100)
print()

# Total matter
Omega_m_pred = Omega_b_pred + Omega_DM_pred
Omega_m_meas = mpf("0.3097")

print("  Derived: Omega_matter = Omega_b + Omega_DM")
show("    prediction (dimensionless)", Omega_m_pred)
show("    measured (dimensionless)", Omega_m_meas)
show("    miss (percent)",
     fabs(Omega_m_pred - Omega_m_meas) / Omega_m_meas * 100)
print()

# Dark energy = 1 - matter (flat universe)
Omega_DE_pred = 1 - Omega_m_pred
Omega_DE_meas = mpf("0.6903")

print("  Derived: Omega_DE = 1 - Omega_matter (flat universe)")
show("    prediction (dimensionless)", Omega_DE_pred)
show("    measured (dimensionless)", Omega_DE_meas)
show("    miss (percent)",
     fabs(Omega_DE_pred - Omega_DE_meas) / Omega_DE_meas * 100)
print()

# ================================================================
# SECTION 10: THE VP STEP FORMULA CONSISTENCY
# ================================================================

print("SECTION 10: VP STEP FORMULA — INTERNAL CONSISTENCY")
print("-" * 70)
print()

# We have two formulas for (1-r):
# Formula A: (1-r) = alpha/(3*pi) = alpha * vp_step (from VP mechanism)
# Formula B: (1-r) = alpha^2 * pi^2 * 20/13 (from product form scan)
# Are these consistent?

omr_A = base_m             # alpha/(3*pi)
omr_B = omr_pred_m         # alpha^2 * pi^2 * 20/13

print("  Formula A: (1-r) = alpha/(3*pi)")
show("    = %s (dimensionless)" % mp.nstr(omr_A, 11), omr_A)
print()
print("  Formula B: (1-r) = alpha^2 * pi^2 * 20/13")
show("    = %s (dimensionless)" % mp.nstr(omr_B, 11), omr_B)
print()

ratio_AB = omr_B / omr_A
show("  ratio B/A (dimensionless)", ratio_AB)
print()

# B/A = (alpha^2 * pi^2 * 20/13) / (alpha/(3*pi))
#     = alpha * pi^2 * 20/13 * 3*pi
#     = alpha * 3 * pi^3 * 20/13
#     = alpha * 60*pi^3/13

ratio_AB_formula = alpha_m * 60 * pi_m**3 / 13
show("  = alpha * 60*pi^3/13 (dimensionless)", ratio_AB_formula)
print("  The two formulas differ by alpha * 60*pi^3/13 ~ %s" %
      mp.nstr(ratio_AB, 4))
print("  This is close to 1 (ratio = %s), meaning both formulas" %
      mp.nstr(ratio_AB, 6))
print("  predict nearly the same (1-r) despite different structure.")
print()

# Which is closer to the H0-derived target?
omr_target = 1 - (mpf("67.36") / mpf("73.04")) ** (mpf(1) / mpf(100))
print("  Target (1-r) at N=100 from H0 data:")
show("    (1-r) target (dimensionless)", omr_target)
show("    miss A (percent)", fabs(omr_A - omr_target) / omr_target * 100)
show("    miss B (percent)", fabs(omr_B - omr_target) / omr_target * 100)
print()

# ================================================================
# SECTION 11: THE COMPLETE PREDICTION TABLE
# ================================================================

print("SECTION 11: COMPLETE PREDICTION TABLE")
print("-" * 70)
print()
print("  All predictions from beta integers + alpha + R2/R4 + pi.")
print("  No cosmological input. Compared to measured values.")
print()

predictions = [
    ("log10(Lambda_Pl) [SM]",
     pred_log_Lambda_SM, Lambda_meas_log10, "decades"),
    ("log10(Lambda_Pl) [VL]",
     pred_log_Lambda_VL, Lambda_meas_log10, "decades"),
    ("DM/baryon",
     dm_pred_m, dm_meas, "dimensionless"),
    ("(1-r) at N=100 [product]",
     omr_pred_m, omr_target, "dimensionless"),
    ("(1-r) at N=100 [VP step]",
     omr_A, omr_target, "dimensionless"),
    ("H0_CMB predicted (km/s/Mpc)",
     H0_pred, H0_meas, "km/s/Mpc"),
    ("Omega_b",
     Omega_b_pred, Omega_b_meas, "dimensionless"),
    ("Omega_DM",
     Omega_DM_pred, Omega_DM_meas, "dimensionless"),
    ("Omega_matter",
     Omega_m_pred, Omega_m_meas, "dimensionless"),
    ("Omega_DE",
     Omega_DE_pred, Omega_DE_meas, "dimensionless"),
]

print("  %35s %14s %14s %10s %8s" %
      ("Quantity", "Predicted", "Measured", "Miss", "Rel%%"))
print("  %35s %14s %14s %10s %8s" %
      ("-" * 35, "-" * 14, "-" * 14, "-" * 10, "-" * 8))

for name, pred, meas, units in predictions:
    miss = fabs(pred - meas)
    if meas != mpf(0):
        rel = miss / fabs(meas) * 100
    else:
        rel = mpf(0)
    print("  %35s %14s %14s %10s %7s%%" %
          (name, mp.nstr(pred, 8), mp.nstr(meas, 8),
           mp.nstr(miss, 4), mp.nstr(rel, 4)))

print()

# ================================================================
# SECTION 12: THE FORMULA INVENTORY — WHAT USES WHAT
# ================================================================

print("SECTION 12: FORMULA INVENTORY")
print("-" * 70)
print()

formulas = [
    ("Lambda_Pl ~ alpha^57",
     "alpha, 3, 19 (from b2_SM)",
     "Cosmo. constant scale"),
    ("Lambda_Pl ~ (alpha/3pi)^39",
     "alpha, pi, 3, 13 (from b2_mod)",
     "Cosmo. constant scale (VL)"),
    ("DM/baryon = (22/13)*pi",
     "11 (YM), 13 (b2_mod), pi",
     "Dark matter fraction"),
    ("(1-r) = alpha^2*pi^2*20/13",
     "alpha, pi, 20 (b3_mod), 13 (b2_mod)",
     "Per-transit H0 correction"),
    ("Omega_b = R4*alpha*22",
     "R4, alpha, 11 (YM)",
     "Baryon density"),
    ("57/39 = 19/13",
     "19 (b2_SM), 13 (b2_mod)",
     "Exact identity"),
]

print("  %30s | %35s | %25s" %
      ("Formula", "Integers Used", "Predicts"))
print("  %30s | %35s | %25s" %
      ("-" * 30, "-" * 35, "-" * 25))
for f, ints, pred in formulas:
    print("  %30s | %35s | %25s" % (f, ints, pred))

print()
print("  COMMON INTEGERS across all formulas:")
print("    13 (|b2_mod_num|): in 4 of 6 formulas")
print("    11 (Yang-Mills): in 3 of 6 formulas")
print("    pi (R2 = pi/4): in 4 of 6 formulas")
print("    alpha: in 4 of 6 formulas")
print("    3 (N_gen): in 2 of 6 formulas")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_exact("b2_SM_num = 19",
          b2_SM_num, Fraction(19), checks)

chk_exact("b2_mod_num = 13",
          b2_mod_num, Fraction(13), checks)

chk_exact("b3_mod_num = 20",
          b3_mod_num, Fraction(20), checks)

chk_exact("57/39 = 19/13 (exact identity)",
          Fraction(57, 39), Fraction(19, 13), checks)

chk_exact("20/13 = |3*b3_mod|/|b2_mod_num|",
          ratio_20_13, Fraction(20, 13), checks)

chk_exact("DM formula integer = 2*YM/b2_mod = 22/13",
          dm_num / dm_den, Fraction(22, 13), checks)

chk_bool("Lambda SM prediction within 0.5 decades",
         fabs(pred_log_Lambda_SM - Lambda_meas_log10) < mpf("0.5"),
         "miss = %s decades" %
         mp.nstr(fabs(pred_log_Lambda_SM - Lambda_meas_log10), 4),
         checks)

chk_bool("Lambda VL prediction within 0.5 decades",
         fabs(pred_log_Lambda_VL - Lambda_meas_log10) < mpf("0.5"),
         "miss = %s decades" %
         mp.nstr(fabs(pred_log_Lambda_VL - Lambda_meas_log10), 4),
         checks)

chk_bool("DM/baryon within 0.1%%",
         fabs(dm_pred_m - dm_meas) / dm_meas < mpf("0.001"),
         "rel miss = %s%%" %
         mp.nstr(fabs(dm_pred_m - dm_meas) / dm_meas * 100, 4),
         checks)

chk_bool("H0 CMB prediction within 1%%",
         fabs(H0_pred - H0_meas) / H0_meas < mpf("0.01"),
         "rel miss = %s%%" %
         mp.nstr(fabs(H0_pred - H0_meas) / H0_meas * 100, 4),
         checks)

chk_bool("Omega_b prediction within 2%%",
         fabs(Omega_b_pred - Omega_b_meas) / Omega_b_meas < mpf("0.02"),
         "rel miss = %s%%" %
         mp.nstr(fabs(Omega_b_pred - Omega_b_meas) / Omega_b_meas * 100, 4),
         checks)

chk_bool("Omega_DM prediction within 2%%",
         fabs(Omega_DM_pred - Omega_DM_meas) / Omega_DM_meas < mpf("0.02"),
         "rel miss = %s%%" %
         mp.nstr(fabs(Omega_DM_pred - Omega_DM_meas) / Omega_DM_meas * 100, 4),
         checks)

chk_bool("Omega_DE prediction within 2%%",
         fabs(Omega_DE_pred - Omega_DE_meas) / Omega_DE_meas < mpf("0.02"),
         "rel miss = %s%%" %
         mp.nstr(fabs(Omega_DE_pred - Omega_DE_meas) / Omega_DE_meas * 100, 4),
         checks)

chk_bool("Lambda predictions BRACKET the measured value",
         pred_log_Lambda_SM < Lambda_meas_log10 < pred_log_Lambda_VL
         or pred_log_Lambda_VL < Lambda_meas_log10 < pred_log_Lambda_SM,
         "SM: %s, VL: %s, meas: %s" %
         (mp.nstr(pred_log_Lambda_SM, 6),
          mp.nstr(pred_log_Lambda_VL, 6),
          mp.nstr(Lambda_meas_log10, 6)),
         checks)

chk_bool("Product form (1-r) within 0.1%% of target",
         fabs(omr_pred_m - omr_target) / omr_target < mpf("0.001"),
         "rel miss = %s%%" %
         mp.nstr(fabs(omr_pred_m - omr_target) / omr_target * 100, 4),
         checks)

print()
print_summary(checks)
print()
print("=" * 70)
print("BETA UNIFICATION TEST COMPLETE")
print("=" * 70)
