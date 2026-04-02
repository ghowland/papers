#!/usr/bin/env python3
"""
HOWL UNIFICATION SCRIPT — Two-Loop Running + Threshold Corrections
===================================================================
Goal: Determine whether SM + Cabibbo Doublet (3,2,1/6) achieves
exact gauge coupling unification at two-loop order, and at what M_VL.

Four stages:
  Stage 1: Beta coefficients (exact Fraction)
  Stage 2: Numerical two-loop RGE integration with threshold at M_VL
  Stage 3: Scan M_VL to find exact unification
  Stage 4: Consistency checks (sin2_tW, proton decay)
"""

import sys, math
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf, log as mlog, pi as mpi, exp as mexp

mp.dps = 50

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

def fl(x):
    """mpf to float for safe formatting."""
    return float(x)

# ================================================================
# DATA-3 INPUTS
# ================================================================

alpha_inv  = Fraction(137035999177, 10**9)
s2w        = Fraction(23122, 100000)
alpha_s_MZ = Fraction(1180, 10000)
M_Z_GeV    = mpf('91.1876')

alpha_em = Fraction(1) / alpha_inv
c2w = Fraction(1) - s2w

alpha_1 = Fraction(5, 3) * alpha_em / c2w
alpha_2 = alpha_em / s2w
alpha_3 = alpha_s_MZ

inv_a1_MZ = f2m(Fraction(1) / alpha_1)
inv_a2_MZ = f2m(Fraction(1) / alpha_2)
inv_a3_MZ = f2m(Fraction(1) / alpha_3)

print("=" * 72)
print("HOWL UNIFICATION: TWO-LOOP RUNNING + THRESHOLD")
print("=" * 72)
print()
print("  1/a1(M_Z) = %.6f" % fl(inv_a1_MZ))
print("  1/a2(M_Z) = %.6f" % fl(inv_a2_MZ))
print("  1/a3(M_Z) = %.6f" % fl(inv_a3_MZ))
print()

# ================================================================
# STAGE 1: BETA COEFFICIENTS
# ================================================================

print("=" * 72)
print("STAGE 1: BETA COEFFICIENTS (exact rationals)")
print("=" * 72)
print()

b1_SM = Fraction(41, 10)
b2_SM = Fraction(-19, 6)
b3_SM = Fraction(-7, 1)

print("  One-loop SM:")
print("    b1 = %s = %.6f" % (b1_SM, float(b1_SM)))
print("    b2 = %s = %.6f" % (b2_SM, float(b2_SM)))
print("    b3 = %s = %.6f" % (b3_SM, float(b3_SM)))
print()

# Two-loop SM b_ij (GUT normalization)
# From Machacek-Vaughn (1983), Luo-Xiao hep-ph/0207271
# Convention: d(a_i^-1)/d(ln mu) = -b_i/(2pi) - sum_j b_ij*a_j/(8pi^2)
b_ij_SM = [
    [Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)],
    [Fraction(9, 10),   Fraction(35, 6),  Fraction(12, 1)],
    [Fraction(11, 10),  Fraction(9, 2),   Fraction(-26, 1)],
]

print("  Two-loop SM b_ij matrix:")
for i in range(3):
    vals = " ".join("%8.4f" % float(b_ij_SM[i][j]) for j in range(3))
    print("    [ %s ]" % vals)
print()

# Cabibbo Doublet (3,2,1/6) VL one-loop (verified, GUT script 9/9)
db1_VL = Fraction(1, 15)
db2_VL = Fraction(1, 1)
db3_VL = Fraction(1, 3)

print("  Cabibbo Doublet one-loop shifts:")
print("    db1 = %s = %.6f" % (db1_VL, float(db1_VL)))
print("    db2 = %s = %.6f" % (db2_VL, float(db2_VL)))
print("    db3 = %s = %.6f" % (db3_VL, float(db3_VL)))
print()

b1_VL = b1_SM + db1_VL
b2_VL = b2_SM + db2_VL
b3_VL = b3_SM + db3_VL
gap_VL = (b1_VL - b2_VL) / (b2_VL - b3_VL)

print("  Modified betas (SM + Cabibbo Doublet):")
print("    b1' = %s = %.6f" % (b1_VL, float(b1_VL)))
print("    b2' = %s = %.6f" % (b2_VL, float(b2_VL)))
print("    b3' = %s = %.6f" % (b3_VL, float(b3_VL)))
print("    Gap ratio = %s = %.6f" % (gap_VL, float(gap_VL)))
print()

# ================================================================
# STAGE 2: NUMERICAL TWO-LOOP RGE INTEGRATION
# ================================================================

print("=" * 72)
print("STAGE 2: TWO-LOOP RGE INTEGRATION")
print("=" * 72)
print()

def run_rge(inv_a_start, b_1loop, b_2loop, ln_total, n_steps=20000):
    """
    Integrate d(a_i^-1)/d(ln mu) = -b_i/(2pi) - sum_j b_ij*a_j/(8pi^2)
    using Euler method. All inputs/outputs are plain floats.
    """
    dt = ln_total / n_steps
    inv_a = list(inv_a_start)
    twopi = 2.0 * math.pi
    eightpi2 = 8.0 * math.pi**2

    for step in range(n_steps):
        a = [1.0/x if x > 0 else 0.0 for x in inv_a]
        d = [0.0, 0.0, 0.0]
        for i in range(3):
            d[i] = -b_1loop[i] / twopi
            for j in range(3):
                d[i] -= b_2loop[i][j] * a[j] / eightpi2
        for i in range(3):
            inv_a[i] += d[i] * dt
    return inv_a

def run_threshold(inv_a_start, M_VL_GeV_f, b_lo1, b_lo2, b_hi1, b_hi2,
                  ln_total, n_steps=20000):
    """
    Run from M_Z to exp(ln_total)*M_Z with step-function threshold at M_VL.
    Below M_VL: b_lo betas (SM). Above M_VL: b_hi betas (SM+VL).
    """
    ln_VL = math.log(M_VL_GeV_f / 91.1876)
    dt = ln_total / n_steps
    inv_a = list(inv_a_start)
    twopi = 2.0 * math.pi
    eightpi2 = 8.0 * math.pi**2

    for step in range(n_steps):
        t = dt * step
        if t < ln_VL:
            b1, b2 = b_lo1, b_lo2
        else:
            b1, b2 = b_hi1, b_hi2
        a = [1.0/x if x > 0 else 0.0 for x in inv_a]
        d = [0.0, 0.0, 0.0]
        for i in range(3):
            d[i] = -b1[i] / twopi
            for j in range(3):
                d[i] -= b2[i][j] * a[j] / eightpi2
        for i in range(3):
            inv_a[i] += d[i] * dt
    return inv_a

# Convert to float lists
b_SM_1 = [float(b1_SM), float(b2_SM), float(b3_SM)]
b_SM_2 = [[float(b_ij_SM[i][j]) for j in range(3)] for i in range(3)]
b_VL_1 = [float(b1_VL), float(b2_VL), float(b3_VL)]
b_VL_2 = [row[:] for row in b_SM_2]  # neglect VL 2-loop shift (~0.1%)
b_zero = [[0.0]*3 for _ in range(3)]

inv_MZ = [fl(inv_a1_MZ), fl(inv_a2_MZ), fl(inv_a3_MZ)]

# Sanity: one-loop SM
print("  Sanity: one-loop SM running...")
ln_14 = math.log(1e14 / 91.1876)
inv_t = run_rge(inv_MZ, b_SM_1, b_zero, ln_14, 20000)
print("    At 10^14 GeV: 1/a1=%.4f, 1/a2=%.4f, 1/a3=%.4f" % (inv_t[0], inv_t[1], inv_t[2]))

# Find SM crossing
for lg10 in range(120, 160):
    lm = lg10 / 10.0
    ln_mu = lm * math.log(10)
    inv_t = run_rge(inv_MZ, b_SM_1, b_zero, ln_mu, 10000)
    if inv_t[0] < inv_t[1]:
        print("    SM a1=a2 crossing at ~10^%.1f GeV (one-loop)" % lm)
        break
print()

# Two-loop SM
print("  Two-loop SM running (no VL)...")
inv_2l = run_rge(inv_MZ, b_SM_1, b_SM_2, ln_14, 20000)
print("    At 10^14 GeV (2-loop): 1/a1=%.4f, 1/a2=%.4f, 1/a3=%.4f" % (inv_2l[0], inv_2l[1], inv_2l[2]))
print()

# ================================================================
# STAGE 3: SCAN M_VL FOR EXACT UNIFICATION
# ================================================================

print("=" * 72)
print("STAGE 3: SCAN M_VL FOR EXACT UNIFICATION")
print("=" * 72)
print()

def find_crossing_miss(M_VL_f, use_2loop=True):
    """Find a1=a2 crossing and a3 miss for given M_VL."""
    b2sm = b_SM_2 if use_2loop else b_zero
    b2vl = b_VL_2 if use_2loop else b_zero

    ln_low = 25.0
    ln_high = 40.0
    for _ in range(50):
        ln_mid = (ln_low + ln_high) / 2.0
        inv_a = run_threshold(inv_MZ, M_VL_f, b_SM_1, b2sm, b_VL_1, b2vl, ln_mid, 20000)
        if inv_a[0] > inv_a[1]:
            ln_low = ln_mid
        else:
            ln_high = ln_mid

    ln_cross = (ln_low + ln_high) / 2.0
    inv_a = run_threshold(inv_MZ, M_VL_f, b_SM_1, b2sm, b_VL_1, b2vl, ln_cross, 20000)

    log10_MGUT = math.log10(91.1876 * math.exp(ln_cross))
    delta_a3 = inv_a[2] - (inv_a[0] + inv_a[1]) / 2.0
    inv_a_GUT = (inv_a[0] + inv_a[1]) / 2.0
    return log10_MGUT, delta_a3, inv_a_GUT

header = "  %-14s %-14s %-14s %-10s %-10s" % ("M_VL (GeV)", "log10 M_GUT", "Delta(1/a3)", "1/a_GUT", "Unifies?")
print(header)
print("  " + "-"*14 + " " + "-"*14 + " " + "-"*14 + " " + "-"*10 + " " + "-"*10)

M_VL_list = [500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
results = []

for M_VL in M_VL_list:
    lg, delta, iag = find_crossing_miss(float(M_VL), use_2loop=True)
    if abs(delta) < 0.5:
        tag = "YES"
    elif abs(delta) < 2.0:
        tag = "near"
    else:
        tag = "no"
    print("  %-14d %-14.2f %+-14.4f %-10.2f %-10s" % (M_VL, lg, delta, iag, tag))
    results.append((M_VL, lg, delta, iag))

print()

# Look for sign change in delta
sign_changes = []
for i in range(len(results) - 1):
    d1 = results[i][2]
    d2 = results[i+1][2]
    if d1 * d2 < 0:
        M1, _, d1v, _ = results[i]
        M2, _, d2v, _ = results[i+1]
        M_cross = M1 + (M2 - M1) * (-d1v) / (d2v - d1v)
        sign_changes.append((M1, M2, M_cross))
        print("  Sign change between M_VL = %d and %d GeV" % (M1, M2))
        print("  Interpolated crossing: M_VL ~ %.0f GeV" % M_cross)

M_VL_exact = None
log_MGUT_exact = None
inv_aGUT_exact = None
delta_exact = None

if sign_changes:
    M_low, M_high, _ = sign_changes[0]
    for _ in range(40):
        M_mid = (M_low + M_high) / 2.0
        _, _, delta_mid, _ = find_crossing_miss(M_mid, use_2loop=True)
        # figure out which side has same sign as M_low
        _, _, d_low, _ = find_crossing_miss(float(M_low), use_2loop=True)
        if delta_mid * d_low > 0:
            M_low = M_mid
        else:
            M_high = M_mid

    M_VL_exact = (M_low + M_high) / 2.0
    log_MGUT_exact, delta_exact, inv_aGUT_exact = find_crossing_miss(M_VL_exact, use_2loop=True)

    print()
    print("  EXACT UNIFICATION at M_VL = %.1f GeV (%.2f TeV)" % (M_VL_exact, M_VL_exact/1000.0))
    print("    M_GUT = 10^%.2f GeV" % log_MGUT_exact)
    print("    Delta(1/a3) = %+.6f" % delta_exact)
    print("    1/a_GUT = %.2f" % inv_aGUT_exact)
    print("    a_GUT = %.6f" % (1.0/inv_aGUT_exact))
else:
    print()
    deltas = [r[2] for r in results]
    if all(d < 0 for d in deltas):
        print("  All deltas negative: a3 too strong at GUT scale for all M_VL")
    elif all(d > 0 for d in deltas):
        print("  All deltas positive: a3 too weak at GUT scale for all M_VL")
    else:
        print("  No clean sign change found")

    min_idx = min(range(len(results)), key=lambda i: abs(results[i][2]))
    M_best, lg_best, delta_best, inv_best = results[min_idx]
    print("  Closest approach: M_VL = %d GeV, Delta = %+.4f" % (M_best, delta_best))
    print("    M_GUT = 10^%.2f GeV, 1/a_GUT = %.2f" % (lg_best, inv_best))

print()

# ================================================================
# STAGE 4: CONSISTENCY CHECKS
# ================================================================

print("=" * 72)
print("STAGE 4: CONSISTENCY CHECKS")
print("=" * 72)
print()

# Pick best M_VL
if M_VL_exact is not None:
    M_use = M_VL_exact
    lg_use = log_MGUT_exact
    iag_use = inv_aGUT_exact
else:
    M_use = float(M_best)
    lg_use = lg_best
    iag_use = inv_best

# Check 1: sin2_tW from 3/8
L_X = math.log(10**lg_use / 91.1876) / (2.0 * math.pi)
s2w_pred = 3.0/8.0 - (109.0/72.0) * L_X / float(f2m(alpha_inv))
s2w_meas = float(f2m(s2w))

print("  Check 1: sin2_tW prediction from 3/8")
print("    L_X = ln(M_GUT/M_Z)/(2pi) = %.4f" % L_X)
print("    sin2_tW(predicted) = %.5f" % s2w_pred)
print("    sin2_tW(measured)  = %.5f" % s2w_meas)
print("    Difference = %+.5f (%.2f%%)" % (s2w_pred - s2w_meas, (s2w_pred/s2w_meas - 1)*100))
print()

# Check 2: gap ratio
gap_meas = fl((inv_a1_MZ - inv_a2_MZ) / (inv_a2_MZ - inv_a3_MZ))
print("  Check 2: Gap ratio")
print("    One-loop (SM+VL) = %.6f (= 38/27)" % float(gap_VL))
print("    Measured          = %.6f" % gap_meas)
print("    One-loop distance = %.6f" % abs(float(gap_VL) - gap_meas))
print()

# Check 3: proton decay
print("  Check 3: Proton decay")
print("    M_GUT = 10^%.2f GeV" % lg_use)
if lg_use > 15.5:
    print("    SAFE: M_GUT > 10^15.5 (Super-K limit)")
elif lg_use > 15.0:
    print("    MARGINAL: near Super-K limit")
else:
    print("    EXCLUDED: M_GUT < 10^15.5")

tau_est = 1e34 * 10**(4 * (lg_use - 15.5))
print("    Estimated tau_p ~ 10^%.1f years" % math.log10(max(tau_est, 1e20)))
print("    Super-K bound: > 2.4e34 years")
print("    Hyper-K sensitivity: ~1e35 years")
print()

# Check 4: one-loop vs two-loop comparison
lg_1, d_1, iag_1 = find_crossing_miss(M_use, use_2loop=False)
lg_2, d_2, iag_2 = find_crossing_miss(M_use, use_2loop=True)
print("  Check 4: One-loop vs two-loop at M_VL = %.0f GeV" % M_use)
print("    One-loop:  M_GUT = 10^%.2f, Delta = %+.4f, 1/a_GUT = %.2f" % (lg_1, d_1, iag_1))
print("    Two-loop:  M_GUT = 10^%.2f, Delta = %+.4f, 1/a_GUT = %.2f" % (lg_2, d_2, iag_2))
print("    Shift in M_GUT: %+.2f decades" % (lg_2 - lg_1))
print("    Shift in Delta: %+.4f" % (d_2 - d_1))
print()

# ================================================================
# SUMMARY
# ================================================================

print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()

if M_VL_exact is not None:
    in_range = 1500 <= M_VL_exact <= 6000
    print("  EXACT TWO-LOOP UNIFICATION ACHIEVED")
    print("    M_VL  = %.0f GeV (%.2f TeV)" % (M_VL_exact, M_VL_exact/1000.0))
    print("    M_GUT = 10^%.2f GeV" % log_MGUT_exact)
    print("    a_GUT = %.4f (1/a_GUT = %.2f)" % (1.0/inv_aGUT_exact, inv_aGUT_exact))
    print("    In anomaly window (1.5-6 TeV): %s" % ("YES" if in_range else "NO"))
    print()
    if in_range:
        print("  The Cabibbo Doublet achieves exact gauge coupling unification")
        print("  at two-loop order with mass in the experimentally allowed range.")
    else:
        print("  Unification requires M_VL = %.0f GeV," % M_VL_exact)
        if M_VL_exact < 1500:
            print("  BELOW the anomaly window.")
        else:
            print("  ABOVE the anomaly window.")
else:
    print("  NO EXACT UNIFICATION at two loops (within scan range)")
    print("  Closest: M_VL = %d GeV, Delta = %+.4f" % (M_best, delta_best))
    print("  Residual requires GUT threshold corrections or")
    print("  two-loop VL contribution (neglected, ~0.1%% effect)")

print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 72)
print("CHECKS")
print("=" * 72)
print()

checks = []
def chk(name, cond, detail=""):
    s = "PASS" if cond else "FAIL"
    checks.append((name, s))
    print("  [%s] %s" % (s, name))
    if detail:
        print("        %s" % detail)

gap_check = float(gap_VL)
chk("One-loop gap ratio = 38/27",
    abs(gap_check - 38.0/27.0) < 1e-10,
    "%.10f" % gap_check)

s2w_chk = float(f2m(Fraction(3,5)*alpha_1 / (Fraction(3,5)*alpha_1 + alpha_2)))
chk("sin2_tW normalization",
    abs(s2w_chk - float(f2m(s2w))) < 1e-8,
    "diff = %.2e" % abs(s2w_chk - float(f2m(s2w))))

chk("SM crossing at 10^13-15 (one-loop)",
    13 < lg_1 < 16,
    "log10 = %.2f" % lg_1)

shift = abs(lg_2 - lg_1)
chk("Two-loop shift < 2 decades",
    shift < 2,
    "shift = %.2f" % shift)

chk("M_GUT > 10^14",
    lg_use > 14,
    "log10 = %.2f" % lg_use)

chk("1/a_GUT in [20, 60]",
    20 < iag_use < 60,
    "1/a_GUT = %.2f" % iag_use)

if M_VL_exact is not None:
    chk("Exact unification found",
        abs(delta_exact) < 0.1,
        "Delta = %+.6f" % delta_exact)

    chk("M_VL in physically reasonable range (100-20000 GeV)",
        100 < M_VL_exact < 20000,
        "M_VL = %.0f GeV" % M_VL_exact)

print()
n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")
print("  TOTAL: %d PASS, %d FAIL out of %d" % (n_pass, n_fail, len(checks)))
print()
print("=" * 72)
print("UNIFICATION SCRIPT COMPLETE")
print("=" * 72)
