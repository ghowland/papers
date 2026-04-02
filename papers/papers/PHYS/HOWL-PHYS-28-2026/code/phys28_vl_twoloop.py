#!/usr/bin/env python3
"""
HOWL PHYS-28: phys28_vl_twoloop.py
=====================================
VL Two-Loop Beta Contributions — The missing piece.

Computes the Cabibbo Doublet's contribution to the two-loop b_ij
matrix using Machacek-Vaughn (1983-84) fermion contribution formulas.
Then reruns two-loop unification with FULL b_ij (SM + CD).

SIGN CONVENTION:
  d(1/alpha_i)/d(ln mu) = -b_i/(2*pi) - sum_j b_ij*alpha_j/(8*pi^2)
  Therefore: 1/alpha_i(mu) = 1/alpha_i(mu_0) - b_i * L
  where L = ln(mu/mu_0)/(2*pi) > 0 for mu > mu_0.
  The MINUS sign means b_i > 0 causes 1/alpha_i to DECREASE running up.

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

C2_3 = Fraction(4, 3)
C2_2 = Fraction(3, 4)
S2_3 = Fraction(1, 2)
S2_2 = Fraction(1, 2)
d3 = Fraction(3)
d2 = Fraction(2)
Y = Fraction(1, 6)
Y2 = Y * Y
k1 = Fraction(3, 5)

show("  C_2(fund SU(3)) (dimensionless)", f2m(C2_3))
show("  C_2(fund SU(2)) (dimensionless)", f2m(C2_2))
show("  Y^2 = 1/36 (dimensionless)", f2m(Y2))
print()

# ================================================================
# SECTION 2: VL TWO-LOOP b_ij
# ================================================================

print("SECTION 2: VL TWO-LOOP b_ij CONTRIBUTIONS")
print("-" * 70)
print()
print("  Fermion-only contribution per Dirac fermion in (3,2,1/6).")
print("  Diagonal: (10/3)*S_a*d_other*C_a(R)")
print("  Off-diag: (4/3)*S_a*d_other*C_b(R)")
print()

S1_VL = Fraction(2, 5) * d3 * d2 * Y2

db12 = Fraction(4, 3) * S1_VL * C2_2
db13 = Fraction(4, 3) * S1_VL * C2_3
db21 = Fraction(4, 3) * S2_2 * d3 * k1 * Y2
db23 = Fraction(4, 3) * S2_2 * d3 * C2_3
db31 = Fraction(4, 3) * S2_3 * d2 * k1 * Y2
db32 = Fraction(4, 3) * S2_3 * d2 * C2_2

db11 = Fraction(10, 3) * S1_VL * (C2_3 + C2_2 + k1 * Y2)
db22 = Fraction(10, 3) * S2_2 * d3 * C2_2
db33 = Fraction(10, 3) * S2_3 * d2 * C2_3

db_ij_VL = [
    [db11, db12, db13],
    [db21, db22, db23],
    [db31, db32, db33],
]

print("  VL two-loop db_ij (exact Fractions):")
for i in range(3):
    row = ["%s" % db_ij_VL[i][j] for j in range(3)]
    print("    [%s]" % ", ".join(row))
print()
print("  Decimal:")
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
        sm = f2m(b_ij_SM[i][j])
        vl = f2m(db_ij_VL[i][j])
        if sm != mpf("0"):
            r = vl / sm * mpf("100")
            print("    b_%d%d: SM=%s, VL=%s, VL/SM=%s%%" %
                  (i+1, j+1, mp.nstr(sm, 6), mp.nstr(vl, 6), mp.nstr(r, 4)))
print()

# ================================================================
# SECTION 4: VERIFY SIGN CONVENTION
# ================================================================

print("SECTION 4: SIGN CONVENTION VERIFICATION")
print("-" * 70)
print()
print("  RGE: d(1/alpha_i)/d(ln mu) = -b_i/(2pi)")
print("  So: 1/alpha_i(mu) = 1/alpha_i(mu0) - b_i * L")
print("  where L = ln(mu/mu0)/(2pi) > 0 for mu > mu0.")
print()
print("  Check: b1_SM = 41/10 > 0, so 1/alpha_1 DECREASES running up.")
print("  Check: b2_SM = -19/6 < 0, so 1/alpha_2 INCREASES running up.")
print("  They CONVERGE at high energy. Correct for unification.")
print()

# Verify: run SM betas from M_Z and check that 1/a1 and 1/a2 converge
inv_a_MZ = [f2m(inv_a1), f2m(inv_a2), f2m(Fraction(1) / alpha_s)]
b_SM_m = [f2m(b1_SM), f2m(b2_SM), f2m(b3_SM)]
b_CD_m = [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)]

# At M_Z: gap = 1/a1 - 1/a2 = 63.2 - 31.7 = 31.5
gap_MZ = inv_a_MZ[0] - inv_a_MZ[1]
# At M_Z + small L with MINUS sign: gap should decrease
L_test = mpf("1")
gap_test = (inv_a_MZ[0] - b_SM_m[0] * L_test) - (inv_a_MZ[1] - b_SM_m[1] * L_test)
show("  Gap at M_Z (dimensionless)", gap_MZ)
show("  Gap at L=1 with -b*L (dimensionless)", gap_test)
print("  Gap decreased: %s (should be True)" % (gap_test < gap_MZ))
print()

# ================================================================
# SECTION 5: TWO-LOOP RUNNING
# ================================================================

print("SECTION 5: TWO-LOOP RUNNING AT M_VL = 500 GeV")
print("-" * 70)
print()

bij_SM_m = [[f2m(b_ij_SM[i][j]) for j in range(3)] for i in range(3)]
bij_full_m = [[f2m(b_ij_SM[i][j] + db_ij_VL[i][j]) for j in range(3)] for i in range(3)]

M_Z_GeV_m = f2m(M_Z) / mpf("1000")
M_VL_m = mpf("500")
L_low = mlog(M_VL_m / M_Z_GeV_m) / (mpf("2") * mpi)
fourpi = mpf("4") * mpi

# Run M_Z to M_VL with SM betas (MINUS sign: 1/a = 1/a0 - b*L)
inv_a_VL = [inv_a_MZ[i] - b_SM_m[i] * L_low for i in range(3)]

show("  1/alpha_1(M_VL) (dimensionless)", inv_a_VL[0])
show("  1/alpha_2(M_VL) (dimensionless)", inv_a_VL[1])
show("  1/alpha_3(M_VL) (dimensionless)", inv_a_VL[2])
print()

# SCENARIO A: one-loop from M_VL to M_GUT with CD betas
# Crossing: 1/a1(VL) - b1*L = 1/a2(VL) - b2*L
# L*(b2 - b1) = 1/a2(VL) - 1/a1(VL)
# L = (1/a2(VL) - 1/a1(VL)) / (b2 - b1)
# Since b2 < b1 and 1/a2 < 1/a1: both negative -> L positive. Good.
L_A = (inv_a_VL[1] - inv_a_VL[0]) / (b_CD_m[1] - b_CD_m[0])
inv_aGUT_A = inv_a_VL[0] - b_CD_m[0] * L_A
inv_a3_A = inv_a_VL[2] - b_CD_m[2] * L_A
Delta_A = inv_a3_A - inv_aGUT_A
M_GUT_A = M_VL_m * mexp(L_A * mpf("2") * mpi)

show("  SCENARIO A (one-loop, CD betas):", mpf("0"))
show("    L_GUT (dimensionless)", L_A)
show("    1/alpha_GUT (dimensionless)", inv_aGUT_A)
show("    1/alpha_3(M_GUT) (dimensionless)", inv_a3_A)
show("    Delta(1/alpha_3) (dimensionless)", Delta_A)
show("    log10(M_GUT/GeV)", mlog10(M_GUT_A))
print()

# Euler integrator with correct sign
def run_2loop(inv_a_start, b1l, bij, L_total, n_steps):
    """Euler integration. 1/a_i(mu+dmu) = 1/a_i(mu) - b_i*dL - sum bij*aj/(4pi)*dL"""
    inv_a = [inv_a_start[0], inv_a_start[1], inv_a_start[2]]
    dL = L_total / mpf(str(n_steps))
    for _ in range(n_steps):
        alphas = [mpf("1") / inv_a[k] for k in range(3)]
        d_inv = [mpf("0"), mpf("0"), mpf("0")]
        for i in range(3):
            d_inv[i] = -b1l[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a[i] += d_inv[i]
    return inv_a

n_steps = 500

def find_crossing(inv_a_start, b1l, bij, L_guess, n_steps):
    """Binary search for L where 1/a1 = 1/a2."""
    L_lo = L_guess * mpf("0.7")
    L_hi = L_guess * mpf("1.3")
    for _ in range(50):
        L_mid = (L_lo + L_hi) / 2
        inv_a = run_2loop(inv_a_start, b1l, bij, L_mid, n_steps)
        diff = inv_a[0] - inv_a[1]
        if diff > 0:
            L_lo = L_mid
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
show("    Delta(1/alpha_3) (dimensionless)", Delta_B)
print()

# SCENARIO C: two-loop with full b_ij
L_C, inv_aGUT_C, Delta_C = find_crossing(
    inv_a_VL, b_CD_m, bij_full_m, L_A, n_steps)

show("  SCENARIO C (two-loop, SM+VL b_ij):", mpf("0"))
show("    L_GUT (dimensionless)", L_C)
show("    Delta(1/alpha_3) (dimensionless)", Delta_C)
print()

# ================================================================
# SECTION 6: COMPARISON
# ================================================================

print("SECTION 6: COMPARISON")
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

chk_exact("S1: S_1 effective = db1_VL = 1/15",
          S1_VL, db1_VL, checks)

chk_bool("S2: All VL b_ij are exact Fractions",
         all(isinstance(db_ij_VL[i][j], Fraction)
             for i in range(3) for j in range(3)),
         "all Fraction", checks)

chk_bool("S2: VL b_ij magnitudes < SM b_ij for all entries",
         all(fabs(f2m(db_ij_VL[i][j])) < fabs(f2m(b_ij_SM[i][j]))
             for i in range(3) for j in range(3)
             if b_ij_SM[i][j] != Fraction(0)),
         "all |VL| < |SM|", checks)

chk_bool("S4: Sign check — gap decreases running up",
         gap_test < gap_MZ,
         "gap_MZ=%s, gap_L1=%s" % (mp.nstr(gap_MZ, 5), mp.nstr(gap_test, 5)),
         checks)

chk_bool("S4: L_A positive",
         L_A > mpf("0"),
         "L_A = %s" % mp.nstr(L_A, 5), checks)

chk_bool("S4: M_GUT > 10^14 GeV",
         mlog10(M_GUT_A) > mpf("14"),
         "log10 = %s" % mp.nstr(mlog10(M_GUT_A), 5), checks)

chk_bool("S4: One-loop Delta negative",
         Delta_A < mpf("0"),
         "Delta = %s" % mp.nstr(Delta_A, 4), checks)

chk_bool("S5: Two-loop SM b_ij improves over one-loop",
         fabs(Delta_B) < fabs(Delta_A),
         "|B|=%s < |A|=%s" % (mp.nstr(fabs(Delta_B), 4),
                               mp.nstr(fabs(Delta_A), 4)), checks)

chk_bool("S5: Full b_ij improves over one-loop",
         fabs(Delta_C) < fabs(Delta_A),
         "|C|=%s < |A|=%s" % (mp.nstr(fabs(Delta_C), 4),
                               mp.nstr(fabs(Delta_A), 4)), checks)

chk_bool("S6: VL two-loop effect small relative to Delta",
         vl_pct < mpf("20"),
         "VL effect = %s%%" % mp.nstr(vl_pct, 3), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-28 VL TWO-LOOP BETA CONTRIBUTIONS COMPLETE")
print("=" * 70)

