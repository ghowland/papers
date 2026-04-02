#!/usr/bin/env python3
"""
HOWL PHYS-28: phys28_vl_twoloop.py
=====================================
VL Two-Loop Beta Contributions — The missing piece.

Computes the Cabibbo Doublet's contribution to the two-loop b_ij
matrix using Machacek-Vaughn (1983-84) fermion contribution formulas.
Then reruns two-loop unification with FULL b_ij (SM + CD).

Key correction: the diagonal two-loop fermion contribution uses
(10/3)*C_a(R), NOT (2*C_G + (10/3)*C_a(R)). The 2*C_G term is
from the gauge self-coupling and is already in the SM b_ij.

Backed by: unification_test.py (6/6), phys26_normalization.py (20/20)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, fabs
from mpmath import log10 as mlog10

# ================================================================
print("=" * 70)
print("HOWL PHYS-28: VL TWO-LOOP BETA CONTRIBUTIONS")
print("The Cabibbo Doublet's contribution to the b_ij matrix.")
print("=" * 70)
print()

# ================================================================
# SECTION 1: GROUP THEORY DATA
# ================================================================

print("SECTION 1: GROUP THEORY DATA")
print("-" * 70)
print()

C2_3 = Fraction(4, 3)     # Casimir C_2(fund SU(3))
C2_2 = Fraction(3, 4)     # Casimir C_2(fund SU(2))
S2_3 = Fraction(1, 2)     # Dynkin S_2(fund SU(3))
S2_2 = Fraction(1, 2)     # Dynkin S_2(fund SU(2))
d3 = Fraction(3)
d2 = Fraction(2)
Y = Fraction(1, 6)
Y2 = Y * Y
k1 = Fraction(3, 5)

show("  C_2(fund SU(3)) (dimensionless)", f2m(C2_3))
show("  C_2(fund SU(2)) (dimensionless)", f2m(C2_2))
show("  Y^2 = 1/36 (dimensionless)", f2m(Y2))
show("  k_1 = 3/5 (dimensionless)", f2m(k1))
print()

# ================================================================
# SECTION 2: VL TWO-LOOP b_ij
# ================================================================
# Machacek-Vaughn fermion contribution to two-loop betas.
# For a SINGLE Dirac fermion (= one VL pair) in (R3, R2, Y):
#
# OFF-DIAGONAL (a != b):
#   db_ab = (4/3) * S_a(R) * d_other * C_b(R)
#   where d_other = product of dims of reps not in group a or b
#
# DIAGONAL (fermion part only, NOT including gauge self-coupling):
#   db_aa = (10/3) * S_a(R) * d_other * C_a(R)
#
# The key point: the 2*C_G term in the full MV diagonal formula
# comes from the gauge-gauge diagram. It is ALREADY in the SM b_ij.
# The VL fermion adds ONLY the (10/3)*C_a(R) fermion piece.

print("SECTION 2: VL TWO-LOOP b_ij CONTRIBUTIONS")
print("-" * 70)
print()
print("  Fermion-only contribution (no gauge self-coupling term).")
print("  Diagonal: (10/3)*S_a*d_other*C_a(R)")
print("  Off-diag: (4/3)*S_a*d_other*C_b(R)")
print()

# Effective U(1) Dynkin index
S1_VL = Fraction(2, 5) * d3 * d2 * Y2   # = 1/15

# Off-diagonal
db12 = Fraction(4, 3) * S1_VL * C2_2
db13 = Fraction(4, 3) * S1_VL * C2_3
db21 = Fraction(4, 3) * S2_2 * d3 * k1 * Y2
db23 = Fraction(4, 3) * S2_2 * d3 * C2_3
db31 = Fraction(4, 3) * S2_3 * d2 * k1 * Y2
db32 = Fraction(4, 3) * S2_3 * d2 * C2_2

# Diagonal — fermion part only: (10/3)*S_a*d_other*C_a(R)
db11 = Fraction(10, 3) * S1_VL * (C2_3 + C2_2 + k1 * Y2)
db22 = Fraction(10, 3) * S2_2 * d3 * C2_2
db33 = Fraction(10, 3) * S2_3 * d2 * C2_3

db_ij_VL = [
    [db11, db12, db13],
    [db21, db22, db23],
    [db31, db32, db33],
]

print("  VL two-loop db_ij matrix (exact Fractions):")
for i in range(3):
    row = ["%s" % db_ij_VL[i][j] for j in range(3)]
    print("    [%s]" % ", ".join(row))
print()
print("  Decimal values:")
for i in range(3):
    row = [mp.nstr(f2m(db_ij_VL[i][j]), 6) for j in range(3)]
    print("    [%s]" % ", ".join(row))
print()

# ================================================================
# SECTION 3: MAGNITUDE COMPARISON
# ================================================================

print("SECTION 3: MAGNITUDE COMPARISON TO SM b_ij")
print("-" * 70)
print()

for i in range(3):
    for j in range(3):
        sm_val = f2m(b_ij_SM[i][j])
        vl_val = f2m(db_ij_VL[i][j])
        if sm_val != mpf("0"):
            ratio = vl_val / sm_val * mpf("100")
            print("    b_%d%d: SM=%s, VL=%s, VL/SM=%s%%" %
                  (i+1, j+1, mp.nstr(sm_val, 6),
                   mp.nstr(vl_val, 6), mp.nstr(ratio, 4)))
print()

# ================================================================
# SECTION 4: TWO-LOOP RUNNING
# ================================================================

print("SECTION 4: TWO-LOOP RUNNING AT M_VL = 500 GeV")
print("-" * 70)
print()

# All mpf for integration
b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]
bij_SM_m = [[f2m(b_ij_SM[i][j]) for j in range(3)] for i in range(3)]
bij_full_m = [[f2m(b_ij_SM[i][j] + db_ij_VL[i][j]) for j in range(3)] for i in range(3)]

M_Z_GeV_m = f2m(M_Z) / mpf("1000")
M_VL_m = mpf("500")
L_low = mlog(M_VL_m / M_Z_GeV_m) / (mpf("2") * mpi)
fourpi = mpf("4") * mpi

inv_a_MZ = [f2m(inv_a1), f2m(inv_a2), f2m(Fraction(1) / alpha_s)]

# Run M_Z to M_VL with SM one-loop betas
inv_a_VL = [inv_a_MZ[i] + b_SM_m[i] * L_low for i in range(3)]

show("  1/alpha_1(M_VL) (dimensionless)", inv_a_VL[0])
show("  1/alpha_2(M_VL) (dimensionless)", inv_a_VL[1])
show("  1/alpha_3(M_VL) (dimensionless)", inv_a_VL[2])
print()

# SCENARIO A: one-loop from M_VL to M_GUT (CD betas)
# Crossing: inv_a1 + b1*L = inv_a2 + b2*L
# L = (inv_a1 - inv_a2) / (b2 - b1)  [positive because inv_a1 > inv_a2 and b2 < b1]
L_A = (inv_a_VL[0] - inv_a_VL[1]) / (b_CD_m[1] - b_CD_m[0])
inv_aGUT_A = inv_a_VL[0] + b_CD_m[0] * L_A
inv_a3_GUT_A = inv_a_VL[2] + b_CD_m[2] * L_A
Delta_A = inv_a3_GUT_A - inv_aGUT_A
M_GUT_A = M_VL_m * mexp(L_A * mpf("2") * mpi)

show("  SCENARIO A (one-loop only):", mpf("0"))
show("    L_GUT (dimensionless)", L_A)
show("    1/alpha_GUT (dimensionless)", inv_aGUT_A)
show("    Delta(1/alpha_3) (dimensionless)", Delta_A)
show("    log10(M_GUT/GeV)", mlog10(M_GUT_A))
print()

# Euler integrator — all mpf
def run_2loop(inv_a_start, b1l, bij, L_total, n_steps):
    """Euler integration of two-loop RGEs. All mpf. L_total > 0 = running UP."""
    inv_a = [inv_a_start[0], inv_a_start[1], inv_a_start[2]]
    dL = L_total / mpf(str(n_steps))
    for _ in range(n_steps):
        alphas = [mpf("1") / inv_a[k] for k in range(3)]
        d_inv = [mpf("0"), mpf("0"), mpf("0")]
        for i in range(3):
            d_inv[i] = b1l[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a[i] += d_inv[i]
    return inv_a

n_steps = 500

def find_crossing(inv_a_start, b1l, bij, L_guess, n_steps):
    """Binary search for L where inv_a1 = inv_a2. L > 0."""
    L_lo = L_guess * mpf("0.7")
    L_hi = L_guess * mpf("1.3")
    for _ in range(50):
        L_mid = (L_lo + L_hi) / 2
        inv_a = run_2loop(inv_a_start, b1l, bij, L_mid, n_steps)
        diff = inv_a[0] - inv_a[1]  # should decrease as L increases
        if diff > 0:
            L_lo = L_mid   # need more running to close the gap
        else:
            L_hi = L_mid
    inv_a = run_2loop(inv_a_start, b1l, bij, L_mid, n_steps)
    inv_aGUT = (inv_a[0] + inv_a[1]) / 2
    Delta = inv_a[2] - inv_aGUT
    return L_mid, inv_aGUT, Delta

# SCENARIO B: two-loop with SM b_ij
L_B, inv_aGUT_B, Delta_B = find_crossing(
    inv_a_VL, b_CD_m, bij_SM_m, L_A, n_steps)

show("  SCENARIO B (two-loop, SM b_ij):", mpf("0"))
show("    L_GUT (dimensionless)", L_B)
show("    1/alpha_GUT (dimensionless)", inv_aGUT_B)
show("    Delta(1/alpha_3) (dimensionless)", Delta_B)
print()

# SCENARIO C: two-loop with full b_ij
L_C, inv_aGUT_C, Delta_C = find_crossing(
    inv_a_VL, b_CD_m, bij_full_m, L_A, n_steps)

show("  SCENARIO C (two-loop, SM+VL b_ij):", mpf("0"))
show("    L_GUT (dimensionless)", L_C)
show("    1/alpha_GUT (dimensionless)", inv_aGUT_C)
show("    Delta(1/alpha_3) (dimensionless)", Delta_C)
print()

# ================================================================
# SECTION 5: COMPARISON
# ================================================================

print("SECTION 5: COMPARISON")
print("-" * 70)
print()

print("  %-35s %12s" % ("Scenario", "Delta"))
print("  %-35s %12s" % ("-" * 35, "-" * 12))
print("  %-35s %12s" % ("A: One-loop only", mp.nstr(Delta_A, 5)))
print("  %-35s %12s" % ("B: Two-loop, SM b_ij", mp.nstr(Delta_B, 5)))
print("  %-35s %12s" % ("C: Two-loop, SM+VL b_ij", mp.nstr(Delta_C, 5)))
print("  %-35s %12s" % ("PHYS-24 ref (SM b_ij, M_VL=500)", "-0.40"))
print()

improv_B = (mpf("1") - fabs(Delta_B) / fabs(Delta_A)) * mpf("100")
improv_C = (mpf("1") - fabs(Delta_C) / fabs(Delta_A)) * mpf("100")
vl_shift = Delta_C - Delta_B
vl_pct = fabs(vl_shift) / fabs(Delta_A) * mpf("100")

show("  Improvement B over A (%%)", improv_B)
show("  Improvement C over A (%%)", improv_C)
show("  VL shift: Delta_C - Delta_B (dimensionless)", vl_shift)
show("  VL shift as %% of one-loop Delta (%%)", vl_pct)
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_exact("S1: C_2(fund SU(3)) = 4/3",
          C2_3, Fraction(4, 3), checks)

chk_exact("S1: C_2(fund SU(2)) = 3/4",
          C2_2, Fraction(3, 4), checks)

chk_exact("S1: S_1 effective = db1_VL = 1/15",
          S1_VL, db1_VL, checks)

chk_bool("S2: All VL b_ij are exact Fractions",
         all(isinstance(db_ij_VL[i][j], Fraction)
             for i in range(3) for j in range(3)),
         "all Fraction", checks)

chk_bool("S2: VL b_33 positive",
         db33 > Fraction(0),
         "db_33 = %s" % db33, checks)

chk_bool("S2: VL b_22 positive",
         db22 > Fraction(0),
         "db_22 = %s" % db22, checks)

chk_bool("S2: VL b_ij magnitudes < SM b_ij for all entries",
         all(fabs(f2m(db_ij_VL[i][j])) < fabs(f2m(b_ij_SM[i][j]))
             for i in range(3) for j in range(3)
             if b_ij_SM[i][j] != Fraction(0)),
         "all |VL| < |SM|", checks)

chk_bool("S4: L_A positive (running UP to M_GUT)",
         L_A > mpf("0"),
         "L_A = %s" % mp.nstr(L_A, 5), checks)

chk_bool("S4: One-loop Delta negative",
         Delta_A < mpf("0"),
         "Delta_A = %s" % mp.nstr(Delta_A, 4), checks)

chk_bool("S4: Two-loop SM b_ij improves Delta (|B| < |A|)",
         fabs(Delta_B) < fabs(Delta_A),
         "|B|=%s < |A|=%s" % (mp.nstr(fabs(Delta_B), 4),
                               mp.nstr(fabs(Delta_A), 4)), checks)

chk_bool("S4: Full b_ij improves Delta (|C| < |A|)",
         fabs(Delta_C) < fabs(Delta_A),
         "|C|=%s < |A|=%s" % (mp.nstr(fabs(Delta_C), 4),
                               mp.nstr(fabs(Delta_A), 4)), checks)

chk_bool("S5: VL two-loop effect < 10%% of one-loop Delta",
         vl_pct < mpf("10"),
         "VL effect = %s%%" % mp.nstr(vl_pct, 3), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-28 VL TWO-LOOP BETA CONTRIBUTIONS COMPLETE")
print("=" * 70)
