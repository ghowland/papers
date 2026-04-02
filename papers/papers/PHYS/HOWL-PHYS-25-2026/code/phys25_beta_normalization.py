#!/usr/bin/env python3
"""
HOWL PHYS-25 DEMONSTRATION: Beta Normalization Diagnostic
===========================================================
phys25_beta_normalization.py

Definitive diagnostic: compute SM one-loop betas field-by-field
in three conventions (standard Weyl, standard Dirac, library Dynkin)
and identify exactly where the library's VL formulas diverge.

The finding: the library's Dynkin coefficient for SU(3) is 1/3
where the standard Weyl formula gives 2/3. This gives the wrong
SM b_3 fermion contribution (2 instead of 4) when applied to
individual chiral fields. The library's VL shift Db_3 = 1/3 is
half the standard Weyl result of 2/3.

The gap ratio 38/27 was computed with Db_3 = 1/3. The standard
Weyl value Db_3 = 2/3 gives gap ratio 19/12 = 1.583. The full
Dirac value Db_3 = 4/3 gives gap ratio 6/5 = 1.200.

Backed by: sin2_theta_w_1.py (9/9 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-25: BETA NORMALIZATION DIAGNOSTIC")
print("=" * 70)
print()

# ================================================================
# THE THREE CONVENTIONS
# ================================================================
# All conventions use d(1/alpha_i)/d(ln mu) = -b_i/(2*pi) - ...
#
# Convention A: "Standard Weyl"
#   For one Weyl fermion in (R_3, R_2, Y):
#     Db_1 = (2/5)*Y^2*d2*d3
#     Db_2 = (2/3)*T2*d3
#     Db_3 = (2/3)*T3*d2
#   Coefficient pattern: (2/5, 2/3, 2/3)
#   Source: Machacek-Vaughn via document 18, halved for Weyl.
#   Cross-check: SM b_ij fermion piece matches when summed
#   over 3 generations of 5 Weyl fields.
#
# Convention B: "Standard Dirac"
#   For one Dirac fermion: double Convention A.
#     Db_1 = (4/5)*Y^2*d2*d3
#     Db_2 = (4/3)*T2*d3
#     Db_3 = (4/3)*T3*d2
#   Coefficient pattern: (4/5, 4/3, 4/3)
#   Source: document 18 directly.
#
# Convention C: "Library Dynkin" (phys24_cabibbo_doublet.py)
#   For a "vector-like pair":
#     Db_1 = (2/5)*Y^2*d2*d3
#     Db_2 = (2/3)*T2*d3
#     Db_3 = (1/3)*T3*d2         <--- 1/3, not 2/3
#   Coefficient pattern: (2/5, 2/3, 1/3)
#   Source: cabibbo_doublet.py lines with comment
#   "the SU(2) and SU(3) coefficients differ because
#   the Casimir normalization conventions differ"

print("THE THREE CONVENTIONS")
print("-" * 70)
print()
print("  A (Standard Weyl):  (2/5, 2/3, 2/3) per Weyl fermion")
print("  B (Standard Dirac): (4/5, 4/3, 4/3) per Dirac fermion")
print("  C (Library Dynkin):  (2/5, 2/3, 1/3) per VL pair")
print()
print("  A and B differ by factor 2 uniformly (Weyl vs Dirac).")
print("  C matches A for b_1 and b_2 but has HALF A for b_3.")
print()

# ================================================================
# SM FERMION CONTENT (one generation, 5 Weyl fields)
# ================================================================
# Each entry: (name, d3, d2, T3, T2, Y)
# T = Dynkin index = S_2 of the representation
# For fundamental of SU(N): T = 1/2
# For singlet: T = 0

sm_gen = [
    ("Q_L(3,2,1/6)",  Fraction(3), Fraction(2), Fraction(1,2), Fraction(1,2), Fraction(1,6)),
    ("u_R(3,1,2/3)",  Fraction(3), Fraction(1), Fraction(1,2), Fraction(0),   Fraction(2,3)),
    ("d_R(3,1,-1/3)", Fraction(3), Fraction(1), Fraction(1,2), Fraction(0),   Fraction(-1,3)),
    ("L_L(1,2,-1/2)", Fraction(1), Fraction(2), Fraction(0),   Fraction(1,2), Fraction(-1,2)),
    ("e_R(1,1,-1)",   Fraction(1), Fraction(1), Fraction(0),   Fraction(0),   Fraction(-1)),
]

# ================================================================
# COMPUTE SM b_i FERMION PIECE IN ALL THREE CONVENTIONS
# ================================================================

print("SM FERMION b_i: FIELD BY FIELD (one generation)")
print("-" * 70)
print()

def weyl_shifts(d3, d2, T3, T2, Y):
    """Convention A: standard Weyl."""
    db1 = Fraction(2, 5) * Y * Y * d2 * d3
    db2 = Fraction(2, 3) * T2 * d3
    db3 = Fraction(2, 3) * T3 * d2
    return (db1, db2, db3)

def library_shifts(d3, d2, T3, T2, Y):
    """Convention C: library Dynkin (from cabibbo_doublet.py)."""
    db1 = Fraction(2, 5) * d3 * d2 * Y * Y
    db2 = Fraction(2, 3) * d3 * T2
    db3 = Fraction(1, 3) * d2 * T3
    return (db1, db2, db3)

# Headers
print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "Field", "A:Db1", "A:Db2", "A:Db3", "C:Db1", "C:Db2", "C:Db3"))
print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "-"*16, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8))

sum_A = [Fraction(0)] * 3
sum_C = [Fraction(0)] * 3

for name, d3, d2, T3, T2, Y in sm_gen:
    a = weyl_shifts(d3, d2, T3, T2, Y)
    c = library_shifts(d3, d2, T3, T2, Y)
    print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
        name, a[0], a[1], a[2], c[0], c[1], c[2]))
    for i in range(3):
        sum_A[i] += a[i]
        sum_C[i] += c[i]

print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "-"*16, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8, "-"*8))
print("  %-16s  %8s %8s %8s  |  %8s %8s %8s" % (
    "Per generation", sum_A[0], sum_A[1], sum_A[2],
    sum_C[0], sum_C[1], sum_C[2]))
print()

# Three generations
ferm_A = [Fraction(3) * sum_A[i] for i in range(3)]
ferm_C = [Fraction(3) * sum_C[i] for i in range(3)]

print("  Three generations (A): %s, %s, %s" % (ferm_A[0], ferm_A[1], ferm_A[2]))
print("  Three generations (C): %s, %s, %s" % (ferm_C[0], ferm_C[1], ferm_C[2]))
print()

# ================================================================
# RECONSTRUCT SM BETAS
# ================================================================

print("SM BETA RECONSTRUCTION")
print("-" * 70)
print()

# Gauge contributions
b_gauge = [Fraction(0), Fraction(-22, 3), Fraction(-11)]

# Higgs contributions
b_higgs = [Fraction(1, 10), Fraction(1, 6), Fraction(0)]

# SM betas = gauge + Higgs + fermion
sm_A = [b_gauge[i] + b_higgs[i] + ferm_A[i] for i in range(3)]
sm_C = [b_gauge[i] + b_higgs[i] + ferm_C[i] for i in range(3)]

print("  %-24s  %12s %12s %12s" % ("Component", "b_1", "b_2", "b_3"))
print("  %-24s  %12s %12s %12s" % ("-"*24, "-"*12, "-"*12, "-"*12))
print("  %-24s  %12s %12s %12s" % ("Gauge", b_gauge[0], b_gauge[1], b_gauge[2]))
print("  %-24s  %12s %12s %12s" % ("Higgs", b_higgs[0], b_higgs[1], b_higgs[2]))
print("  %-24s  %12s %12s %12s" % ("Fermion (Conv A)", ferm_A[0], ferm_A[1], ferm_A[2]))
print("  %-24s  %12s %12s %12s" % ("Fermion (Conv C)", ferm_C[0], ferm_C[1], ferm_C[2]))
print("  %-24s  %12s %12s %12s" % ("-"*24, "-"*12, "-"*12, "-"*12))
print("  %-24s  %12s %12s %12s" % ("SM total (Conv A)", sm_A[0], sm_A[1], sm_A[2]))
print("  %-24s  %12s %12s %12s" % ("SM total (Conv C)", sm_C[0], sm_C[1], sm_C[2]))
print("  %-24s  %12s %12s %12s" % ("Library (DATA-4 N1-N3)", b1_SM, b2_SM, b3_SM))
print()

match_A = all(sm_A[i] == [b1_SM, b2_SM, b3_SM][i] for i in range(3))
match_C = all(sm_C[i] == [b1_SM, b2_SM, b3_SM][i] for i in range(3))

print("  Convention A reproduces SM betas: %s" % match_A)
print("  Convention C reproduces SM betas: %s" % match_C)
print()

if not match_C:
    print("  Convention C gives b_3 = %s, library has %s." % (sm_C[2], b3_SM))
    print("  The fermion contribution is %s (Conv C) vs %s (Conv A)." % (
        ferm_C[2], ferm_A[2]))
    print("  Convention C is WRONG for SM b_3 by a factor of %s." % (
        ferm_A[2] / ferm_C[2]))
    print()

# ================================================================
# VL (3,2,1/6) SHIFTS IN ALL CONVENTIONS
# ================================================================

print("VL (3,2,1/6) ONE-LOOP SHIFTS")
print("-" * 70)
print()

vl_d3 = Fraction(3)
vl_d2 = Fraction(2)
vl_T3 = Fraction(1, 2)
vl_T2 = Fraction(1, 2)
vl_Y  = Fraction(1, 6)

vl_weyl = weyl_shifts(vl_d3, vl_d2, vl_T3, vl_T2, vl_Y)
vl_dirac = tuple(Fraction(2) * vl_weyl[i] for i in range(3))
vl_lib_formula = library_shifts(vl_d3, vl_d2, vl_T3, vl_T2, vl_Y)
vl_lib_actual = (db1_VL, db2_VL, db3_VL)

print("  %-24s  %12s %12s %12s" % ("Convention", "Db_1", "Db_2", "Db_3"))
print("  %-24s  %12s %12s %12s" % ("-"*24, "-"*12, "-"*12, "-"*12))
print("  %-24s  %12s %12s %12s" % ("A: Weyl (one Weyl)",
    vl_weyl[0], vl_weyl[1], vl_weyl[2]))
print("  %-24s  %12s %12s %12s" % ("B: Dirac (one Dirac)",
    vl_dirac[0], vl_dirac[1], vl_dirac[2]))
print("  %-24s  %12s %12s %12s" % ("C: Library formula",
    vl_lib_formula[0], vl_lib_formula[1], vl_lib_formula[2]))
print("  %-24s  %12s %12s %12s" % ("Library actual (N4-N6)",
    vl_lib_actual[0], vl_lib_actual[1], vl_lib_actual[2]))
print()

# Ratios
print("  Ratios library_actual / convention:")
for label, conv in [("Weyl", vl_weyl), ("Dirac", vl_dirac)]:
    ratios = []
    for i in range(3):
        if conv[i] != Fraction(0):
            ratios.append(vl_lib_actual[i] / conv[i])
        else:
            ratios.append("n/a")
    print("    vs %-8s  %s, %s, %s" % (label, ratios[0], ratios[1], ratios[2]))
print()

# The library formula matches the library actual values
lib_formula_matches = all(vl_lib_formula[i] == vl_lib_actual[i] for i in range(3))
print("  Library formula matches library actual: %s" % lib_formula_matches)

# The library actual matches standard Weyl
lib_matches_weyl = all(vl_lib_actual[i] == vl_weyl[i] for i in range(3))
print("  Library actual matches Weyl: %s" % lib_matches_weyl)
if not lib_matches_weyl:
    for i in range(3):
        if vl_lib_actual[i] != vl_weyl[i]:
            print("    Component %d: library = %s, Weyl = %s" % (
                i+1, vl_lib_actual[i], vl_weyl[i]))
print()

# ================================================================
# THE DIVERGENCE: b_3 COEFFICIENT
# ================================================================

print("THE DIVERGENCE: SU(3) COEFFICIENT")
print("-" * 70)
print()
print("  Standard Weyl formula for b_3:")
print("    Db_3 = (2/3) * T(R_3) * dim(R_2)")
print()
print("  Library Dynkin formula for b_3:")
print("    Db_3 = (1/3) * dim(R_2) * S_2(R_3)")
print()
print("  T(R_3) = S_2(R_3) in all cases, so the ONLY")
print("  difference is the coefficient: 2/3 vs 1/3.")
print()
print("  For SM fermions (Convention A, Weyl):")
print("    b_3 fermion = 3 * sum_gen = 3 * 4/3 = 4")
print("    b_3_SM = -11 + 0 + 4 = -7  CORRECT")
print()
print("  For SM fermions (Convention C, library):")
print("    b_3 fermion = 3 * sum_gen = 3 * %s = %s" % (sum_C[2], ferm_C[2]))
print("    b_3_SM = -11 + 0 + %s = %s  WRONG (should be -7)" % (
    ferm_C[2], b_gauge[2] + b_higgs[2] + ferm_C[2]))
print()
print("  The library's b_3 Dynkin coefficient 1/3 is HALF the")
print("  standard Weyl coefficient 2/3. It does not reproduce")
print("  b_3_SM = -7 when applied to SM fermion fields.")
print()

# ================================================================
# GAP RATIO IN ALL CONVENTIONS
# ================================================================

print("GAP RATIO IN ALL CONVENTIONS")
print("-" * 70)
print()

# Convention A: VL = one Weyl (3,2,1/6)
b_mod_weyl = [b1_SM + vl_weyl[i] for i in range(3)]
gap_weyl = (b_mod_weyl[0] - b_mod_weyl[1]) / (b_mod_weyl[1] - b_mod_weyl[2])

# Convention B: VL = one Dirac (3,2,1/6)
b_mod_dirac = [b1_SM + vl_dirac[i] for i in range(3)]
gap_dirac = (b_mod_dirac[0] - b_mod_dirac[1]) / (b_mod_dirac[1] - b_mod_dirac[2])

# Convention C: library
b_mod_lib = [b1_SM + vl_lib_actual[i] for i in range(3)]
gap_lib = (b_mod_lib[0] - b_mod_lib[1]) / (b_mod_lib[1] - b_mod_lib[2])

# uses gap_measured from phys24_lib
gap_meas_val = f2m(gap_measured)

print("  %-28s %12s %12s %12s" % (
    "Convention", "Gap ratio", "Decimal", "Dist from 1.358"))
print("  %-28s %12s %12s %12s" % ("-"*28, "-"*12, "-"*12, "-"*12))

for label, gap in [
    ("SM (no VL)", gap_SM),
    ("A: Weyl (one Weyl)", gap_weyl),
    ("B: Dirac (one Dirac)", gap_dirac),
    ("C: Library (operational)", gap_lib),
    ("MSSM", gap_MSSM),
]:
    dist = abs(f2m(gap) - gap_meas_val)
    print("  %-28s %12s %12s %12s" % (
        label, gap, mp.nstr(f2m(gap), 6), mp.nstr(dist, 4)))

print()
show("Measured gap ratio (dimensionless)", gap_meas_val)
print()

# ================================================================
# WHAT A VL PAIR ACTUALLY IS
# ================================================================

print("WHAT IS THE VL PAIR?")
print("-" * 70)
print()
print("  A vector-like pair (3,2,1/6) consists of:")
print("    L component: one Weyl in (3,2,1/6)")
print("    R component: one Weyl in (3*,2*,-1/6)")
print("  Together they form one Dirac fermion.")
print()
print("  The SM generation has 5 Weyl fermions per generation.")
print("  The VL pair has 2 Weyl fermions (= 1 Dirac).")
print()
print("  The correct shift for the VL pair is Convention B")
print("  (Dirac), which is 2x Convention A (Weyl).")
print()
print("  The library uses Convention C, which matches Weyl")
print("  for b_1 and b_2 but gives HALF Weyl for b_3.")
print("  This is neither Weyl nor Dirac — it is a hybrid.")
print()

# ================================================================
# THE SESSION 3 QUESTION
# ================================================================

print("THE SESSION 3 QUESTION")
print("-" * 70)
print()
print("  The gap ratio 38/27 was verified in sin2_theta_w_1.py")
print("  (9/9 checks). That script used the library values")
print("  (1/15, 1, 1/3) to compute modified betas and the")
print("  gap ratio. It then compared against the MEASURED")
print("  coupling ratio from alpha_EM, sin2_tW, alpha_s.")
print()
print("  The gap ratio is a LEVEL 1 quantity: it depends only")
print("  on the betas. The measured gap ratio is DERIVED from")
print("  Level 2 couplings. They are compared, not equated.")
print("  The 9/9 checks verified that the computation is")
print("  internally consistent, not that Db_3 = 1/3 is the")
print("  physically correct shift for a VL (3,2,1/6) pair.")
print()
print("  The unification_test.py (6/6) used the library betas")
print("  for one-loop running above M_VL and SM betas below.")
print("  If Db_3 should be 2/3 or 4/3 instead of 1/3, the")
print("  unification scan results change significantly.")
print()

# ================================================================
# RESOLUTION PATH
# ================================================================

print("RESOLUTION PATH")
print("-" * 70)
print()
print("  The normalization must be resolved by an external")
print("  reference that explicitly lists the one-loop beta")
print("  shift for a VL (3,2,1/6) doublet in GUT normalization.")
print()
print("  Candidates:")
print("    - Kowalska & Kumar, JHEP 12 (2019) 094")
print("    - Bhattacherjee et al., JHEP 05 (2018) 090")
print("    - Dermisek, Phys. Rev. D 87 (2013) 055008")
print("  These papers enumerate VL representations and their")
print("  beta shifts. A table entry for (3,2,1/6) settles it.")
print()
print("  Until resolved, all three gap ratios should be tracked:")
print("    38/27 (library, Db_3=1/3)")
print("    19/12 (Weyl, Db_3=2/3)")
print("    6/5   (Dirac, Db_3=4/3)")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: Convention A reproduces SM betas
chk_bool("Conv A (Weyl) reproduces SM betas",
         match_A,
         "b = (%s, %s, %s)" % (sm_A[0], sm_A[1], sm_A[2]), checks)

# Check 2: Convention C does NOT reproduce SM b_3
chk_bool("Conv C (library) does NOT reproduce SM b_3",
         not match_C,
         "b_3(C) = %s, should be %s" % (sm_C[2], b3_SM), checks)

# Check 3: Library formula matches library actual
chk_bool("Library formula matches library actual values",
         lib_formula_matches,
         "all three components match", checks)

# Check 4: Library diverges from Weyl on b_3 only
b1_match = (vl_lib_actual[0] == vl_weyl[0])
b2_match = (vl_lib_actual[1] == vl_weyl[1])
b3_match = (vl_lib_actual[2] == vl_weyl[2])
chk_bool("Library matches Weyl for b_1 and b_2",
         b1_match and b2_match,
         "b_1: %s, b_2: %s" % (b1_match, b2_match), checks)

chk_bool("Library DIFFERS from Weyl for b_3",
         not b3_match,
         "library = %s, Weyl = %s" % (vl_lib_actual[2], vl_weyl[2]), checks)

# Check 5: The coefficient ratio is exactly 1/2 for b_3
b3_ratio = vl_lib_actual[2] / vl_weyl[2]
chk_exact("b_3 ratio library/Weyl = 1/2",
          b3_ratio, Fraction(1, 2), checks)

# Check 6: Per-generation democracy holds in Conv A
chk_exact("Per-gen (Conv A): b_1 = 4/3",
          sum_A[0], Fraction(4, 3), checks)
chk_exact("Per-gen (Conv A): b_2 = 4/3",
          sum_A[1], Fraction(4, 3), checks)
chk_exact("Per-gen (Conv A): b_3 = 4/3",
          sum_A[2], Fraction(4, 3), checks)

# Check 7: Per-gen democracy BROKEN in Conv C
chk_bool("Per-gen (Conv C): b_3 != 4/3 (democracy broken)",
         sum_C[2] != Fraction(4, 3),
         "b_3 per gen (C) = %s" % sum_C[2], checks)

# Check 8: Gap ratios computed correctly
chk_exact("Gap ratio (library) = 38/27",
          gap_lib, Fraction(38, 27), checks)
chk_exact("Gap ratio (Weyl) = 19/12",
          gap_weyl, Fraction(19, 12), checks)
chk_exact("Gap ratio (Dirac) = 6/5",
          gap_dirac, Fraction(6, 5), checks)

# Check 9: All CD conventions improve on SM
sm_dist = abs(f2m(gap_SM) - gap_meas_val)
lib_dist = abs(f2m(gap_lib) - gap_meas_val)
weyl_dist = abs(f2m(gap_weyl) - gap_meas_val)
dirac_dist = abs(f2m(gap_dirac) - gap_meas_val)

chk_bool("All CD conventions closer to measured than SM",
         lib_dist < sm_dist and weyl_dist < sm_dist and dirac_dist < sm_dist,
         "SM: %s, lib: %s, Weyl: %s, Dirac: %s" % (
             mp.nstr(sm_dist, 4), mp.nstr(lib_dist, 4),
             mp.nstr(weyl_dist, 4), mp.nstr(dirac_dist, 4)), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-25 BETA NORMALIZATION DIAGNOSTIC COMPLETE")
print("=" * 70)
