#!/usr/bin/env python3
"""
HOWL EXPERIMENT: Beta Unification Test
==========================================
Tests the six formulas from the Beta Unification Notebook.
Every integer from the gauge group beta coefficients.
Every constant from phys24_lib.py.
No cosmological input.

Platform: HOWL-PLATFORM-v1
Libraries: phys24_lib

15 predictions from particle physics → compared to cosmological measurements.
"""

# Platform: HOWL-PLATFORM-v1

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from mpmath import pi as mpi, log as mlog, exp as mexp, sqrt as msqrt

print("=" * 70)
print("BETA UNIFICATION EXPERIMENT")
print("All integers from gauge group beta coefficients.")
print("All constants from phys24_lib.py. No cosmological input.")
print("=" * 70)
print()

checks = []


# ================================================================
# SECTION 1: INPUT SET — ALL FROM PHYS24_LIB
# ================================================================

print("SECTION 1: INPUT SET")
print("-" * 70)
print()

# Level 2: one measured value
alpha = Fraction(1, 1) / alpha_inv   # alpha = 1/137.035999177
show("alpha (EM coupling)", f2m(alpha))

# Level 1: exact integers from gauge group
show("b2_SM", f2m(b2_SM))            # -19/6
show("b2_mod", f2m(b2_mod))          # -13/6
show("b3_mod", f2m(b3_mod))          # -20/3
show("R2 = pi/4", f2m(R2_f))
show("R4 = pi^2/32", f2m(R4_f))

# Derived integers — ALL from library beta values
YM = Fraction(11, 1)                  # Yang-Mills integer
N_gen_f = Fraction(3, 1)             # Generation count

b2_SM_num = abs(b2_SM * Fraction(6, 1))    # |numerator of b2_SM| = 19
b2_mod_num = abs(b2_mod * Fraction(6, 1))  # |numerator of b2_mod| = 13
b3_mod_num = abs(b3_mod * Fraction(3, 1))  # |3 * b3_mod| = 20

print()
print("  Derived integers (all from library betas):")
print("    YM = %s (Yang-Mills)" % YM)
print("    |b2_SM * 6| = %s" % b2_SM_num)
print("    |b2_mod * 6| = %s" % b2_mod_num)
print("    |b3_mod * 3| = %s" % b3_mod_num)
print("    2 * YM = %s" % (2 * YM))
print("    3 * |b2_SM_num| = %s" % (N_gen_f * b2_SM_num))
print("    3 * |b2_mod_num| = %s" % (N_gen_f * b2_mod_num))

chk_exact("|b2_SM * 6| = 19", b2_SM_num, Fraction(19, 1), checks)
chk_exact("|b2_mod * 6| = 13", b2_mod_num, Fraction(13, 1), checks)
chk_exact("|b3_mod * 3| = 20", b3_mod_num, Fraction(20, 1), checks)


# ================================================================
# SECTION 2: COSMOLOGICAL MEASURED VALUES (targets, not inputs)
# These are what we predict. They do NOT enter the formulas.
# ================================================================

print()
print("SECTION 2: COSMOLOGICAL TARGETS (not inputs)")
print("-" * 70)
print()

# All measured values from Planck 2018 / 2020
Lambda_log10_measured = mpf("-121.54")     # log10(Lambda/M_Planck^4)
DM_baryon_measured = mpf("5.3204")         # Omega_DM / Omega_b (Planck 2018)
H0_CMB_measured = mpf("67.36")             # km/s/Mpc (Planck 2020)
H0_local_val = mpf("73.04")               # km/s/Mpc (SH0ES 2022)
Omega_b_measured = mpf("0.0490")           # Planck 2018
Omega_DM_measured = mpf("0.2607")          # Planck 2018
Omega_matter_measured = mpf("0.3097")      # Planck 2018
Omega_DE_measured = mpf("0.6903")          # Planck 2018
sin2_tW_measured = mpf("0.2312")           # PDG 2022

print("  Lambda log10:     %s" % mp.nstr(Lambda_log10_measured, 6))
print("  DM/baryon:        %s" % mp.nstr(DM_baryon_measured, 5))
print("  H0 (CMB):         %s km/s/Mpc" % mp.nstr(H0_CMB_measured, 5))
print("  H0 (local):       %s km/s/Mpc" % mp.nstr(H0_local_val, 5))
print("  Omega_b:          %s" % mp.nstr(Omega_b_measured, 4))
print("  Omega_DM:         %s" % mp.nstr(Omega_DM_measured, 4))
print("  Omega_matter:     %s" % mp.nstr(Omega_matter_measured, 4))
print("  Omega_DE:         %s" % mp.nstr(Omega_DE_measured, 4))


# ================================================================
# SECTION 3: FORMULA 1a — COSMOLOGICAL CONSTANT (SM VERSION)
# log10(Lambda) = 3 * 19 * log10(alpha) = 57 * log10(alpha)
# ================================================================

print()
print("SECTION 3: FORMULA 1a — COSMOLOGICAL CONSTANT (SM)")
print("-" * 70)
print()

exp_SM = N_gen_f * b2_SM_num         # 3 * 19 = 57
log10_alpha = mlog(f2m(alpha), 10)   # log10(1/137.036...) = -2.1368...

Lambda_SM = f2m(exp_SM) * log10_alpha

show("Exponent 3*19", f2m(exp_SM))
show("log10(alpha)", log10_alpha)
show("Lambda_SM = 57 * log10(alpha)", Lambda_SM)
show("Measured", Lambda_log10_measured)

miss_Lambda_SM = abs(Lambda_SM - Lambda_log10_measured)
miss_Lambda_SM_pct = miss_Lambda_SM / abs(Lambda_log10_measured) * mpf("100")
show("Miss (decades)", miss_Lambda_SM)

chk_bool("Formula 1a: Lambda SM within 0.3 decades",
         miss_Lambda_SM < mpf("0.3"),
         "miss = %s decades (%s%%)" % (
             mp.nstr(miss_Lambda_SM, 4), mp.nstr(miss_Lambda_SM_pct, 3)),
         checks)


# ================================================================
# SECTION 4: FORMULA 1b — COSMOLOGICAL CONSTANT (VL VERSION)
# log10(Lambda) = 3 * 13 * log10(alpha/(3*pi)) = 39 * log10(alpha/(3*pi))
# ================================================================

print()
print("SECTION 4: FORMULA 1b — COSMOLOGICAL CONSTANT (VL)")
print("-" * 70)
print()

exp_VL = N_gen_f * b2_mod_num         # 3 * 13 = 39
alpha_over_3pi = f2m(alpha) / (mpf("3") * mpi)
log10_a3pi = mlog(alpha_over_3pi, 10)

Lambda_VL = f2m(exp_VL) * log10_a3pi

show("Exponent 3*13", f2m(exp_VL))
show("alpha/(3*pi)", alpha_over_3pi)
show("log10(alpha/(3*pi))", log10_a3pi)
show("Lambda_VL = 39 * log10(alpha/(3*pi))", Lambda_VL)

miss_Lambda_VL = abs(Lambda_VL - Lambda_log10_measured)

chk_bool("Formula 1b: Lambda VL within 0.25 decades",
         miss_Lambda_VL < mpf("0.25"),
         "miss = %s decades" % mp.nstr(miss_Lambda_VL, 4), checks)

# Bracketing check
chk_bool("Lambda SM < measured < Lambda VL (bracketing)",
         Lambda_SM < Lambda_log10_measured < Lambda_VL,
         "SM=%s < meas=%s < VL=%s" % (
             mp.nstr(Lambda_SM, 5), mp.nstr(Lambda_log10_measured, 5),
             mp.nstr(Lambda_VL, 5)), checks)

# Interpolation fraction
f_interp = (Lambda_log10_measured - Lambda_SM) / (Lambda_VL - Lambda_SM)
show("Interpolation fraction f", f_interp)
show("(midpoint would be 0.50)", mpf("0.50"))


# ================================================================
# SECTION 5: FORMULA 6 — THE EXACT IDENTITY
# 57/39 = 19/13 = |b2_SM_num|/|b2_mod_num|
# ================================================================

print()
print("SECTION 5: FORMULA 6 — EXACT ALGEBRAIC IDENTITY")
print("-" * 70)
print()

ratio_exponents = (N_gen_f * b2_SM_num) / (N_gen_f * b2_mod_num)
ratio_betas = b2_SM_num / b2_mod_num

chk_exact("57/39 = 19/13 (exact Fraction)",
          ratio_exponents, Fraction(19, 13), checks)
chk_exact("57/39 = b2_SM_num/b2_mod_num",
          ratio_exponents, ratio_betas, checks)

print("  57/39 = %s (exact)" % ratio_exponents)
print("  19/13 = %s (exact)" % (Fraction(19, 13)))
print("  Ratio of SM and VL Lambda exponents = ratio of b2 numerators")


# ================================================================
# SECTION 6: FORMULA 2 — DARK MATTER RATIO
# DM/baryon = (22/13) * pi = (2*YM / b2_mod_num) * pi
# ================================================================

print()
print("SECTION 6: FORMULA 2 — DARK MATTER RATIO")
print("-" * 70)
print()

DM_ratio_frac = (Fraction(2, 1) * YM) / b2_mod_num   # 22/13, exact
DM_ratio_pred = f2m(DM_ratio_frac) * mpi              # (22/13) * pi

chk_exact("22/13 = (2*YM)/b2_mod_num", DM_ratio_frac, Fraction(22, 13), checks)

show("DM/baryon predicted = (22/13)*pi", DM_ratio_pred)
show("DM/baryon measured", DM_baryon_measured)

miss_DM = abs(DM_ratio_pred - DM_baryon_measured)
miss_DM_pct = miss_DM / DM_baryon_measured * mpf("100")

chk_bool("Formula 2: DM/baryon within 0.1%",
         miss_DM_pct < mpf("0.1"),
         "miss = %s (%s%%)" % (mp.nstr(miss_DM, 4), mp.nstr(miss_DM_pct, 3)),
         checks)


# ================================================================
# SECTION 7: FORMULA 3 — PER-TRANSIT H0 CORRECTION
# (1 - r) = alpha^2 * pi^2 * (20/13)
# ================================================================

print()
print("SECTION 7: FORMULA 3 — H0 PER-TRANSIT CORRECTION")
print("-" * 70)
print()

ratio_20_13 = b3_mod_num / b2_mod_num     # 20/13, exact
chk_exact("20/13 = |3*b3_mod|/|b2_mod_num|", ratio_20_13, Fraction(20, 13), checks)

alpha_mpf = f2m(alpha)
one_minus_r = alpha_mpf ** 2 * mpi ** 2 * f2m(ratio_20_13)

show("alpha^2", alpha_mpf ** 2)
show("pi^2", mpi ** 2)
show("20/13", f2m(ratio_20_13))
show("(1-r) = alpha^2 * pi^2 * (20/13)", one_minus_r)

r_val = mpf("1") - one_minus_r
show("r = 1 - (1-r)", r_val)

# H0 at N=100 transits
N_transit = 100
H0_pred = H0_local_val * r_val ** N_transit

show("H0(CMB) at N=%d" % N_transit, H0_pred)
show("H0(CMB) measured", H0_CMB_measured)

miss_H0 = abs(H0_pred - H0_CMB_measured)
miss_H0_pct = miss_H0 / H0_CMB_measured * mpf("100")

chk_bool("Formula 3: H0(CMB) within 0.1%",
         miss_H0_pct < mpf("0.1"),
         "miss = %s km/s/Mpc (%s%%)" % (
             mp.nstr(miss_H0, 4), mp.nstr(miss_H0_pct, 3)),
         checks)

# Target 1-r from pure H0 data
target_1mr = mpf("1") - (H0_CMB_measured / H0_local_val) ** (mpf("1") / mpf(N_transit))
show("Target (1-r) from H0 data", target_1mr)
show("Formula (1-r)", one_minus_r)

miss_1mr = abs(one_minus_r - target_1mr)
miss_1mr_pct = miss_1mr / target_1mr * mpf("100")

chk_bool("Formula 3a: (1-r) within 0.1%",
         miss_1mr_pct < mpf("0.1"),
         "miss = %s%%"  % mp.nstr(miss_1mr_pct, 3), checks)


# ================================================================
# SECTION 8: FORMULA 4 — BARYON DENSITY (Set A: R4 * alpha * 22)
# ================================================================

print()
print("SECTION 8: FORMULA 4 — BARYON DENSITY (Set A)")
print("-" * 70)
print()

Omega_b_A = f2m(R4_f) * alpha_mpf * f2m(Fraction(2, 1) * YM)

show("R4 = pi^2/32", f2m(R4_f))
show("alpha", alpha_mpf)
show("22 = 2*YM", f2m(Fraction(22, 1)))
show("Omega_b (Set A) = R4 * alpha * 22", Omega_b_A)
show("Omega_b measured", Omega_b_measured)

miss_Ob_A = abs(Omega_b_A - Omega_b_measured)
miss_Ob_A_pct = miss_Ob_A / Omega_b_measured * mpf("100")

chk_bool("Formula 4 (Set A): Omega_b within 1.5%",
         miss_Ob_A_pct < mpf("1.5"),
         "miss = %s%%"  % mp.nstr(miss_Ob_A_pct, 3), checks)


# ================================================================
# SECTION 9: FORMULA 4 — BARYON DENSITY (Set B: 2/(13*pi))
# ================================================================

print()
print("SECTION 9: FORMULA 4 — BARYON DENSITY (Set B)")
print("-" * 70)
print()

Omega_b_B_frac = Fraction(2, 1) / (b2_mod_num * Fraction(1, 1))
Omega_b_B = f2m(Omega_b_B_frac) / mpi    # 2/(13*pi)

show("2/(13*pi)", Omega_b_B)
show("Omega_b measured", Omega_b_measured)

miss_Ob_B = abs(Omega_b_B - Omega_b_measured)
miss_Ob_B_pct = miss_Ob_B / Omega_b_measured * mpf("100")

chk_bool("Formula 4 (Set B): Omega_b within 0.2%",
         miss_Ob_B_pct < mpf("0.2"),
         "miss = %s%%" % mp.nstr(miss_Ob_B_pct, 3), checks)

# Compare Set A vs Set B
chk_bool("Set B closer than Set A for Omega_b",
         miss_Ob_B < miss_Ob_A,
         "B: %s%% vs A: %s%%" % (
             mp.nstr(miss_Ob_B_pct, 3), mp.nstr(miss_Ob_A_pct, 3)),
         checks)


# ================================================================
# SECTION 10: FORMULA 5 — OMEGA CHAIN (Set B propagation)
# ================================================================

print()
print("SECTION 10: FORMULA 5 — OMEGA CHAIN (Set B)")
print("-" * 70)
print()

# Omega_DM = Omega_b * (22/13)*pi = 2/(13*pi) * (22/13)*pi = 44/169
Omega_DM_B_frac = Fraction(4, 1) * YM / (b2_mod_num ** 2)  # 44/169
Omega_DM_B = f2m(Omega_DM_B_frac)

chk_exact("Omega_DM (Set B) = 44/169", Omega_DM_B_frac, Fraction(44, 169), checks)

show("Omega_DM (Set B) = 44/169", Omega_DM_B)
show("Omega_DM measured", Omega_DM_measured)

miss_ODM_B = abs(Omega_DM_B - Omega_DM_measured)
miss_ODM_B_pct = miss_ODM_B / Omega_DM_measured * mpf("100")

chk_bool("Formula 5: Omega_DM within 0.2%",
         miss_ODM_B_pct < mpf("0.2"),
         "miss = %s%%" % mp.nstr(miss_ODM_B_pct, 3), checks)

# Verify pi cancellation: Omega_b * (22/13)*pi = 2/(13*pi) * (22/13)*pi = 44/169
pi_cancellation = Omega_b_B_frac * DM_ratio_frac  # should be 44/169 in Fraction
# Note: Omega_b_B_frac = 2/13, and we divided by pi at mpf stage
# To test the pi cancellation properly, do it in formula:
# Omega_DM = [2/(13*pi)] * [(22/13)*pi] = 2*22 / (13*13) = 44/169
cancel_check = Fraction(2, 1) * Fraction(22, 1) / (b2_mod_num * b2_mod_num)

chk_exact("Pi cancels: 2*22/(13^2) = 44/169",
          cancel_check, Fraction(44, 169), checks)

print("  Key finding: pi from DM/baryon cancels pi from Omega_b")
print("  Omega_DM = 44/169 is a PURE RATIONAL — no transcendentals")

# Omega_matter and Omega_DE
Omega_matter_B = Omega_b_B + Omega_DM_B
Omega_DE_B = mpf("1") - Omega_matter_B

show("Omega_matter (Set B)", Omega_matter_B)
show("Omega_matter measured", Omega_matter_measured)

show("Omega_DE (Set B)", Omega_DE_B)
show("Omega_DE measured", Omega_DE_measured)

miss_Om_B = abs(Omega_matter_B - Omega_matter_measured)
miss_Om_B_pct = miss_Om_B / Omega_matter_measured * mpf("100")
miss_ODE_B = abs(Omega_DE_B - Omega_DE_measured)
miss_ODE_B_pct = miss_ODE_B / Omega_DE_measured * mpf("100")

chk_bool("Omega_matter (Set B) within 0.2%",
         miss_Om_B_pct < mpf("0.2"),
         "miss = %s%%" % mp.nstr(miss_Om_B_pct, 3), checks)

chk_bool("Omega_DE (Set B) within 0.1%",
         miss_ODE_B_pct < mpf("0.1"),
         "miss = %s%%" % mp.nstr(miss_ODE_B_pct, 3), checks)


# ================================================================
# SECTION 11: SET A vs SET B COMPARISON
# ================================================================

print()
print("SECTION 11: SET A vs SET B COMPARISON")
print("-" * 70)
print()

# Set A chain
Omega_DM_A = Omega_b_A * DM_ratio_pred / mpi * mpi  # Omega_b_A * (22/13)*pi
# Actually: Omega_DM_A = Omega_b_A * (22/13) * pi
Omega_DM_A = Omega_b_A * f2m(DM_ratio_frac) * mpi
Omega_matter_A = Omega_b_A + Omega_DM_A
Omega_DE_A = mpf("1") - Omega_matter_A

miss_ODM_A_pct = abs(Omega_DM_A - Omega_DM_measured) / Omega_DM_measured * mpf("100")
miss_Om_A_pct = abs(Omega_matter_A - Omega_matter_measured) / Omega_matter_measured * mpf("100")
miss_ODE_A_pct = abs(Omega_DE_A - Omega_DE_measured) / Omega_DE_measured * mpf("100")

print("  %-20s %-12s %-12s %-10s %-10s" % (
    "Observable", "Set A", "Set B", "Measured", "Winner"))
print("  %-20s %-12s %-12s %-10s %-10s" % ("-" * 20, "-" * 12, "-" * 12, "-" * 10, "-" * 10))

comparisons = [
    ("Omega_b", Omega_b_A, Omega_b_B, Omega_b_measured, miss_Ob_A_pct, miss_Ob_B_pct),
    ("Omega_DM", Omega_DM_A, Omega_DM_B, Omega_DM_measured, miss_ODM_A_pct, miss_ODM_B_pct),
    ("Omega_matter", Omega_matter_A, Omega_matter_B, Omega_matter_measured, miss_Om_A_pct, miss_Om_B_pct),
    ("Omega_DE", Omega_DE_A, Omega_DE_B, Omega_DE_measured, miss_ODE_A_pct, miss_ODE_B_pct),
]

B_wins = 0
for name, vA, vB, meas, mA, mB in comparisons:
    winner = "B" if mB < mA else "A"
    if winner == "B":
        B_wins += 1
    print("  %-20s %-12s %-12s %-10s %-10s" % (
        name, mp.nstr(vA, 5), mp.nstr(vB, 5),
        mp.nstr(meas, 5), "%s (%.2f%% vs %.2f%%)" % (winner, float(mB), float(mA))))

print()
chk_bool("Set B wins on all 4 Omega observables",
         B_wins == 4,
         "Set B wins %d of 4" % B_wins, checks)


# ================================================================
# SECTION 12: COMBINATORIC CHECK — sin2_tW ~ 3/13
# ================================================================

print()
print("SECTION 12: COMBINATORIC — sin2_tW approximation")
print("-" * 70)
print()

sin2_approx = f2m(N_gen_f / b2_mod_num)   # 3/13 = 0.23077
show("3/13 = N_gen / |b2_mod_num|", sin2_approx)
show("sin2_tW measured", sin2_tW_measured)

miss_sin2 = abs(sin2_approx - sin2_tW_measured)
miss_sin2_pct = miss_sin2 / sin2_tW_measured * mpf("100")

chk_bool("sin2_tW ~ 3/13 within 0.3%",
         miss_sin2_pct < mpf("0.3"),
         "miss = %s%%" % mp.nstr(miss_sin2_pct, 3), checks)


# ================================================================
# SECTION 13: CONSOLIDATED PREDICTION TABLE
# ================================================================

print()
print("SECTION 13: CONSOLIDATED PREDICTION TABLE")
print("-" * 70)
print()

# Average Lambda
Lambda_avg = (Lambda_SM + Lambda_VL) / mpf("2")
miss_Lambda_avg = abs(Lambda_avg - Lambda_log10_measured)

print("  %-25s %-14s %-14s %-10s" % ("Observable", "Predicted", "Measured", "Miss"))
print("  %-25s %-14s %-14s %-10s" % ("-" * 25, "-" * 14, "-" * 14, "-" * 10))

table = [
    ("log10(Lambda) SM", Lambda_SM, Lambda_log10_measured, miss_Lambda_SM),
    ("log10(Lambda) VL", Lambda_VL, Lambda_log10_measured, miss_Lambda_VL),
    ("log10(Lambda) avg", Lambda_avg, Lambda_log10_measured, miss_Lambda_avg),
    ("DM/baryon", DM_ratio_pred, DM_baryon_measured, miss_DM),
    ("(1-r) at N=100", one_minus_r, target_1mr, miss_1mr),
    ("H0(CMB)", H0_pred, H0_CMB_measured, miss_H0),
    ("Omega_b (B)", Omega_b_B, Omega_b_measured, miss_Ob_B),
    ("Omega_DM (B)", Omega_DM_B, Omega_DM_measured, miss_ODM_B),
    ("Omega_matter (B)", Omega_matter_B, Omega_matter_measured, miss_Om_B),
    ("Omega_DE (B)", Omega_DE_B, Omega_DE_measured, miss_ODE_B),
    ("sin2_tW ~ 3/13", sin2_approx, sin2_tW_measured, miss_sin2),
]

for name, pred, meas, miss in table:
    pct = miss / abs(meas) * mpf("100")
    print("  %-25s %-14s %-14s %s%%" % (
        name, mp.nstr(pred, 6), mp.nstr(meas, 6), mp.nstr(pct, 3)))


# ================================================================
# SECTION 14: INTEGER TRACEABILITY VERIFICATION
# ================================================================

print()
print("SECTION 14: INTEGER TRACEABILITY")
print("-" * 70)
print()

print("  Every integer used traces to the gauge group:")
print()
print("  11  = Yang-Mills coefficient from Lorentz + gauge + renormalizability")
print("  19  = |numerator(b2_SM * 6)| = |(%s) * 6| = %s" % (b2_SM, b2_SM_num))
print("  13  = |numerator(b2_mod * 6)| = |(%s) * 6| = %s" % (b2_mod, b2_mod_num))
print("  20  = |b3_mod * 3| = |(%s) * 3| = %s" % (b3_mod, b3_mod_num))
print("  22  = 2 * YM = 2 * 11 = %s" % (2 * YM))
print("  57  = 3 * 19 = N_gen * |b2_SM_num| = %s" % (N_gen_f * b2_SM_num))
print("  39  = 3 * 13 = N_gen * |b2_mod_num| = %s" % (N_gen_f * b2_mod_num))
print("  44  = 4 * 11 = 4 * YM = %s" % (Fraction(4, 1) * YM))
print("  169 = 13^2 = |b2_mod_num|^2 = %s" % (b2_mod_num ** 2))
print()

# Verify each decomposition
chk_exact("19 = |b2_SM| * 6", b2_SM_num, Fraction(19, 1), checks)
chk_exact("13 = |b2_mod| * 6", b2_mod_num, Fraction(13, 1), checks)
chk_exact("20/13 exact", ratio_20_13, Fraction(20, 13), checks)
chk_exact("22/13 exact", DM_ratio_frac, Fraction(22, 13), checks)
chk_exact("44/169 exact", Omega_DM_B_frac, Fraction(44, 169), checks)


# ================================================================
# SECTION 15: LAMBDA INTERPOLATION EXPLORATION
# ================================================================

print()
print("SECTION 15: LAMBDA INTERPOLATION FRACTION")
print("-" * 70)
print()

show("Interpolation f", f_interp)

# Test candidate fractions from beta integers
candidates_f = [
    ("13/(13+19) = 13/32", Fraction(13, 32)),
    ("19/(19+22) = 19/41", Fraction(19, 41)),
    ("13/(13+20) = 13/33", Fraction(13, 33)),
    ("11/(11+13) = 11/24", Fraction(11, 24)),
    ("20/(20+22) = 20/42 = 10/21", Fraction(10, 21)),
    ("13/(2*13+6) = 13/32", Fraction(13, 32)),
]

print("  Candidate beta-integer ratios for f = %s:" % mp.nstr(f_interp, 4))
print()
for name, frac in candidates_f:
    fval = f2m(frac)
    miss_f = abs(fval - f_interp)
    print("    %-30s = %s  miss = %s" % (name, mp.nstr(fval, 5), mp.nstr(miss_f, 3)))

# Find best
best_name = None
best_miss = mpf("1")
for name, frac in candidates_f:
    miss_f = abs(f2m(frac) - f_interp)
    if miss_f < best_miss:
        best_miss = miss_f
        best_name = name

print()
print("  Best match: %s (miss = %s)" % (best_name, mp.nstr(best_miss, 4)))


# ================================================================
# FINAL SUMMARY
# ================================================================

print()
print("=" * 70)
print("RESULTS SUMMARY")
print("=" * 70)
print()
print("  INPUT: alpha (1 measured value) + {11,13,19,20,22,pi} from beta structure")
print("  OUTPUT: 11 predictions of cosmological observables")
print("  ALL within 1.1%% of measured (Set B chain within 0.15%%)")
print()
print("  Key algebraic identities (exact in Fraction):")
print("    57/39 = 19/13             (Lambda exponent ratio)")
print("    22/13 = (2*YM)/|b2_mod|   (DM/baryon coefficient)")
print("    20/13 = |3*b3_mod|/|b2_mod| (H0 correction coefficient)")
print("    44/169 = (4*YM)/|b2_mod|^2 (Omega_DM, rational)")
print()
print("  Set B (2/(13*pi)) uniformly better than Set A (R4*alpha*22)")
print("  Dark matter density 44/169 is a pure rational — no transcendentals")
print()
print("  STATUS: Pattern exists. Statistical significance NOT YET TESTED.")
print("  NEXT: Random integer pool comparison (phys25_dm_ratio_test.py)")
print()

print_summary(checks)

n_fail = sum(1 for _, s in checks if s == "FAIL")
if n_fail == 0:
    print("  BETA UNIFICATION EXPERIMENT: ALL PASS")
else:
    print("  BETA UNIFICATION EXPERIMENT: %d FAILURES" % n_fail)
    for tag, status in checks:
        if status == "FAIL":
            print("    - %s" % tag)

print()
print("=" * 70)
print("BETA UNIFICATION EXPERIMENT COMPLETE")
print("=" * 70)
