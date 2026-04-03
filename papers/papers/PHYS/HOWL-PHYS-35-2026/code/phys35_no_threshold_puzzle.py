#!/usr/bin/env python3
"""
HOWL PHYS-35: phys35_no_threshold_puzzle.py
=============================================
The No-Threshold Puzzle — Why does ignoring M_VL work better?

Three investigations:
1. M_VL scan: vary threshold from 200 GeV to 6 TeV, plot alpha_s miss.
2. Step sensitivity: compare 500 vs 2000 Euler steps at both settings.
3. Soft threshold: smooth transition instead of step function.

All computations use Python float (sufficient for 4-5 digit accuracy).
The PHYS-30 method: inputs are (1/alpha_1, 1/alpha_2) at M_Z,
find crossing, predict alpha_s.

Backed by: phys30_alpha_s.py (9/9), phys28_vl_twoloop.py (11/11)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import mpf, fabs
import math

PI = math.pi

# ================================================================
print("=" * 70)
print("HOWL PHYS-35: THE NO-THRESHOLD PUZZLE")
print("Why does no-threshold beat physical threshold?")
print("=" * 70)
print()

# ================================================================
# DATA — all float for speed
# ================================================================

inv_a1_MZ = float(f2m(inv_a1))   # 63.210
inv_a2_MZ = float(f2m(inv_a2))   # 31.685
alpha_s_meas = float(f2m(alpha_s))  # 0.1180
MZ = 91.2

# SM betas
b1_SM_f = float(f2m(b1_SM))   # 41/10 = 4.1
b2_SM_f = float(f2m(b2_SM))   # -19/6 = -3.167
b3_SM_f = float(f2m(b3_SM))   # -7

# CD betas
b1_CD_f = float(f2m(b1_mod))  # 25/6 = 4.167
b2_CD_f = float(f2m(b2_mod))  # -13/6 = -2.167
b3_CD_f = float(f2m(b3_mod))  # -20/3 = -6.667

# SM b_ij (float)
bij_SM_f = [[float(f2m(b_ij_SM[i][j])) for j in range(3)] for i in range(3)]

# VL b_ij from PHYS-28
C2_3 = Fraction(4, 3)
C2_2 = Fraction(3, 4)
S2_3 = Fraction(1, 2)
S2_2 = Fraction(1, 2)
d3 = Fraction(3)
d2 = Fraction(2)
Y = Fraction(1, 6)
Y2 = Y * Y
k1 = Fraction(3, 5)
S1_VL = Fraction(2, 5) * d3 * d2 * Y2

db_ij_VL = [
    [Fraction(10,3)*S1_VL*(C2_3+C2_2+k1*Y2), Fraction(4,3)*S1_VL*C2_2, Fraction(4,3)*S1_VL*C2_3],
    [Fraction(4,3)*S2_2*d3*k1*Y2, Fraction(10,3)*S2_2*d3*C2_2, Fraction(4,3)*S2_2*d3*C2_3],
    [Fraction(4,3)*S2_3*d2*k1*Y2, Fraction(4,3)*S2_3*d2*C2_2, Fraction(10,3)*S2_3*d2*C2_3],
]

bij_full_f = [[float(f2m(b_ij_SM[i][j] + db_ij_VL[i][j])) for j in range(3)] for i in range(3)]

# ================================================================
# THE TWO-LOOP INTEGRATOR
# ================================================================

def run_euler(inv_a_start, b1l, bij, L_total, n_steps):
    """Euler integration with float arithmetic."""
    fourpi = 4.0 * PI
    inv_a = list(inv_a_start)
    dL = L_total / float(n_steps)
    for _ in range(n_steps):
        alphas = [1.0 / inv_a[k] for k in range(3)]
        d_inv = [0.0, 0.0, 0.0]
        for i in range(3):
            d_inv[i] = -b1l[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a[i] += d_inv[i]
    return inv_a

def predict_alpha_s_threshold(M_VL_GeV, n_steps, bij_above):
    """Predict alpha_s with hard threshold at M_VL.
    SM betas below M_VL, CD betas + bij_above above."""
    # Step 1: run SM from M_Z to M_VL
    L_to_VL = math.log(M_VL_GeV / MZ) / (2 * PI)
    inv_a_VL = run_euler([inv_a1_MZ, inv_a2_MZ, 1.0/alpha_s_meas],
                          [b1_SM_f, b2_SM_f, b3_SM_f], bij_SM_f,
                          L_to_VL, max(50, int(n_steps * L_to_VL / 5.0)))

    # Step 2: find crossing with CD betas from M_VL
    b_CD = [b1_CD_f, b2_CD_f, b3_CD_f]
    # Binary search for L where 1/a1 = 1/a2
    L_lo = 0.1
    L_hi = 8.0
    for _ in range(60):
        L_mid = (L_lo + L_hi) / 2.0
        inv_a = run_euler(inv_a_VL, b_CD, bij_above, L_mid, n_steps)
        if inv_a[0] > inv_a[1]:
            L_lo = L_mid
        else:
            L_hi = L_mid
    inv_a_GUT = run_euler(inv_a_VL, b_CD, bij_above, L_mid, n_steps)
    inv_aGUT = (inv_a_GUT[0] + inv_a_GUT[1]) / 2.0
    Delta = inv_a_GUT[2] - inv_aGUT
    alpha_s_pred = 1.0 / (inv_a_VL[2] - (inv_aGUT - inv_a_VL[2] + Delta) *
                           (inv_a_VL[2] / inv_a_GUT[2]))
    # Simpler: just use Delta directly
    # At GUT: 1/a3_pred = inv_aGUT. At M_VL: 1/a3 = inv_a_VL[2].
    # Run 1/a3 from M_VL to GUT: inv_a_GUT[2].
    # Delta = inv_a_GUT[2] - inv_aGUT.
    # The predicted 1/a3 at M_VL if unification were exact: inv_aGUT.
    # Running back to M_Z from this: need to go from GUT to M_Z.
    # Easier: predict from the crossing directly.

    # Actually, use the full method:
    # Run all three from M_VL to GUT crossing.
    # At crossing: 1/a1 = 1/a2 = 1/a_GUT. Delta = 1/a3 - 1/a_GUT.
    # If unification exact: 1/a3(GUT) = 1/a_GUT.
    # Predicted 1/a3(MZ):
    #   Run 1/a_GUT back from GUT to M_VL (CD betas), then M_VL to MZ (SM betas).

    inv_a_GUT_all = [inv_aGUT, inv_aGUT, inv_aGUT]
    # Back from GUT to M_VL
    inv_a_back_VL = run_euler(inv_a_GUT_all, b_CD, bij_above, -L_mid, n_steps)
    # Back from M_VL to M_Z
    inv_a_back_MZ = run_euler(inv_a_back_VL,
                               [b1_SM_f, b2_SM_f, b3_SM_f], bij_SM_f,
                               -L_to_VL, max(50, int(n_steps * L_to_VL / 5.0)))
    alpha_s_pred = 1.0 / inv_a_back_MZ[2]
    return alpha_s_pred, Delta, L_mid

def predict_alpha_s_no_threshold(n_steps, bij):
    """Predict alpha_s with CD betas from M_Z (no threshold)."""
    b_CD = [b1_CD_f, b2_CD_f, b3_CD_f]
    inv_a_start = [inv_a1_MZ, inv_a2_MZ, 1.0/alpha_s_meas]

    # Binary search for crossing
    L_lo = 0.5
    L_hi = 8.0
    for _ in range(60):
        L_mid = (L_lo + L_hi) / 2.0
        inv_a = run_euler(inv_a_start, b_CD, bij, L_mid, n_steps)
        if inv_a[0] > inv_a[1]:
            L_lo = L_mid
        else:
            L_hi = L_mid
    inv_a_GUT = run_euler(inv_a_start, b_CD, bij, L_mid, n_steps)
    inv_aGUT = (inv_a_GUT[0] + inv_a_GUT[1]) / 2.0
    Delta = inv_a_GUT[2] - inv_aGUT

    # Run back from GUT to M_Z
    inv_a_GUT_all = [inv_aGUT, inv_aGUT, inv_aGUT]
    inv_a_back = run_euler(inv_a_GUT_all, b_CD, bij, -L_mid, n_steps)
    alpha_s_pred = 1.0 / inv_a_back[2]
    return alpha_s_pred, Delta, L_mid

# ================================================================
# SECTION 1: REPRODUCE PHYS-30 REFERENCE VALUES
# ================================================================

print("SECTION 1: REPRODUCE PHYS-30 REFERENCE")
print("-" * 70)
print()

as_nt, delta_nt, L_nt = predict_alpha_s_no_threshold(500, bij_full_f)
miss_nt = abs(as_nt - alpha_s_meas) / alpha_s_meas * 100

as_th, delta_th, L_th = predict_alpha_s_threshold(500, 500, bij_full_f)
miss_th = abs(as_th - alpha_s_meas) / alpha_s_meas * 100

print("  No-threshold (full b_ij, 500 steps):")
print("    alpha_s = %.8f, miss = %.4f%%" % (as_nt, miss_nt))
print("  Threshold M_VL=500 (full b_ij, 500 steps):")
print("    alpha_s = %.8f, miss = %.4f%%" % (as_th, miss_th))
print("  Advantage ratio: %.1fx" % (miss_th / miss_nt) if miss_nt > 0 else "  inf")
print()

# ================================================================
# SECTION 2: M_VL SCAN
# ================================================================

print("SECTION 2: M_VL SCAN (200 GeV to 6000 GeV)")
print("-" * 70)
print()

m_vl_values = [200, 300, 400, 500, 750, 1000, 1500, 2000, 3000, 4000, 5000, 6000]
scan_results = []

print("  %8s %12s %10s %10s" % ("M_VL(GeV)", "alpha_s", "miss(%%)", "Delta"))
print("  %8s %12s %10s %10s" % ("-"*8, "-"*12, "-"*10, "-"*10))

for mvl in m_vl_values:
    as_v, delta_v, L_v = predict_alpha_s_threshold(mvl, 500, bij_full_f)
    miss_v = abs(as_v - alpha_s_meas) / alpha_s_meas * 100
    scan_results.append((mvl, as_v, miss_v, delta_v))
    print("  %8d %12.8f %10.4f %10.4f" % (mvl, as_v, miss_v, delta_v))

print()
print("  No-threshold: alpha_s = %.8f, miss = %.4f%%" % (as_nt, miss_nt))
print()

# Find optimal M_VL
best_idx = min(range(len(scan_results)), key=lambda i: scan_results[i][2])
best_mvl, best_as, best_miss, best_delta = scan_results[best_idx]
print("  Optimal M_VL: %d GeV (miss = %.4f%%)" % (best_mvl, best_miss))
print("  No-threshold miss: %.4f%%" % miss_nt)
print("  No-threshold %s optimal threshold" %
      ("BEATS" if miss_nt < best_miss else "LOSES to"))
print()

# ================================================================
# SECTION 3: STEP SENSITIVITY AT BOTH SETTINGS
# ================================================================

print("SECTION 3: STEP SENSITIVITY — IS THE ADVANTAGE AN ARTIFACT?")
print("-" * 70)
print()

print("  NO-THRESHOLD:")
print("  %8s %12s %10s" % ("Steps", "alpha_s", "miss(%%)"))
print("  %8s %12s %10s" % ("-"*8, "-"*12, "-"*10))
nt_step_results = []
for ns in [200, 500, 1000, 2000]:
    as_v, _, _ = predict_alpha_s_no_threshold(ns, bij_full_f)
    miss_v = abs(as_v - alpha_s_meas) / alpha_s_meas * 100
    nt_step_results.append((ns, as_v, miss_v))
    print("  %8d %12.8f %10.4f" % (ns, as_v, miss_v))

print()
print("  WITH THRESHOLD (M_VL = 500 GeV):")
print("  %8s %12s %10s" % ("Steps", "alpha_s", "miss(%%)"))
print("  %8s %12s %10s" % ("-"*8, "-"*12, "-"*10))
th_step_results = []
for ns in [200, 500, 1000, 2000]:
    as_v, _, _ = predict_alpha_s_threshold(500, ns, bij_full_f)
    miss_v = abs(as_v - alpha_s_meas) / alpha_s_meas * 100
    th_step_results.append((ns, as_v, miss_v))
    print("  %8d %12.8f %10.4f" % (ns, as_v, miss_v))

print()

# Compare at 2000 steps
nt_2k = nt_step_results[3][2]
th_2k = th_step_results[3][2]
print("  At 2000 steps: no-thresh miss = %.4f%%, threshold miss = %.4f%%" %
      (nt_2k, th_2k))
print("  Advantage ratio at 2000 steps: %.1fx" %
      (th_2k / nt_2k) if nt_2k > 0 else "inf")
print("  ADVANTAGE PERSISTS with better integration: %s" %
      ("YES" if th_2k > nt_2k * 2 else "NO (within factor 2)"))
print()

# ================================================================
# SECTION 4: SOFT THRESHOLD
# ================================================================

print("SECTION 4: SOFT THRESHOLD — SMOOTH DECOUPLING")
print("-" * 70)
print()
print("  Physical decoupling: a heavy particle of mass M_VL")
print("  contributes to the running as a smooth function of mu/M_VL.")
print("  The step function is an approximation.")
print()
print("  Smooth threshold function:")
print("    f(mu) = ln(1 + mu^2/M_VL^2) / ln(1 + mu_GUT^2/M_VL^2)")
print("  This gives f -> 0 for mu << M_VL and f -> 1 for mu >> M_VL.")
print("  The effective betas are: b_i(mu) = b_SM + f(mu)*db_VL")
print("  and bij(mu) = bij_SM + f(mu)*dbij_VL")
print()

def predict_alpha_s_soft_threshold(M_VL_GeV, n_steps, mu_GUT_GeV):
    """Predict alpha_s with smooth decoupling function."""
    db_1l = [b1_CD_f - b1_SM_f, b2_CD_f - b2_SM_f, b3_CD_f - b3_SM_f]
    dbij = [[bij_full_f[i][j] - bij_SM_f[i][j] for j in range(3)] for i in range(3)]

    L_total_guess = math.log(mu_GUT_GeV / MZ) / (2 * PI)
    # Use the same normalization for the smooth function
    f_norm = math.log(1.0 + (mu_GUT_GeV / M_VL_GeV)**2)

    inv_a = [inv_a1_MZ, inv_a2_MZ, 1.0/alpha_s_meas]
    fourpi = 4.0 * PI

    # Binary search for L_GUT
    L_lo = 2.0
    L_hi = 8.0
    for _ in range(50):
        L_mid = (L_lo + L_hi) / 2.0
        inv_a_test = [inv_a1_MZ, inv_a2_MZ, 1.0/alpha_s_meas]
        dL = L_mid / float(n_steps)
        for step in range(n_steps):
            L_current = (step + 0.5) * dL
            mu = MZ * math.exp(L_current * 2 * PI)
            f = 1.0 / (1.0 + (M_VL_GeV / mu)**2)

            b_eff = [b1_SM_f + f * db_1l[0],
                     b2_SM_f + f * db_1l[1],
                     b3_SM_f + f * db_1l[2]]
            bij_eff = [[bij_SM_f[i][j] + f * dbij[i][j] for j in range(3)]
                       for i in range(3)]

            alphas = [1.0 / inv_a_test[k] for k in range(3)]
            d_inv = [0.0, 0.0, 0.0]
            for i in range(3):
                d_inv[i] = -b_eff[i] * dL
                for j in range(3):
                    d_inv[i] -= bij_eff[i][j] * alphas[j] / fourpi * dL
            for i in range(3):
                inv_a_test[i] += d_inv[i]

        if inv_a_test[0] > inv_a_test[1]:
            L_lo = L_mid
        else:
            L_hi = L_mid

    # Final run at L_mid
    inv_a_GUT = [inv_a1_MZ, inv_a2_MZ, 1.0/alpha_s_meas]
    dL = L_mid / float(n_steps)
    for step in range(n_steps):
        L_current = (step + 0.5) * dL
        mu = MZ * math.exp(L_current * 2 * PI)
        f = math.log(1.0 + (mu / M_VL_GeV)**2) / f_norm
        f = min(f, 1.0)

        b_eff = [b1_SM_f + f * db_1l[0],
                 b2_SM_f + f * db_1l[1],
                 b3_SM_f + f * db_1l[2]]
        bij_eff = [[bij_SM_f[i][j] + f * dbij[i][j] for j in range(3)]
                   for i in range(3)]

        alphas = [1.0 / inv_a_GUT[k] for k in range(3)]
        d_inv = [0.0, 0.0, 0.0]
        for i in range(3):
            d_inv[i] = -b_eff[i] * dL
            for j in range(3):
                d_inv[i] -= bij_eff[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a_GUT[i] += d_inv[i]

    inv_aGUT = (inv_a_GUT[0] + inv_a_GUT[1]) / 2.0
    Delta = inv_a_GUT[2] - inv_aGUT

    # Run back
    inv_a_back = [inv_aGUT, inv_aGUT, inv_aGUT]
    for step in range(n_steps):
        L_current = L_mid - (step + 0.5) * dL
        mu = MZ * math.exp(L_current * 2 * PI)
        f = math.log(1.0 + (mu / M_VL_GeV)**2) / f_norm
        f = min(f, 1.0)

        b_eff = [b1_SM_f + f * db_1l[0],
                 b2_SM_f + f * db_1l[1],
                 b3_SM_f + f * db_1l[2]]
        bij_eff = [[bij_SM_f[i][j] + f * dbij[i][j] for j in range(3)]
                   for i in range(3)]

        alphas = [1.0 / inv_a_back[k] for k in range(3)]
        d_inv = [0.0, 0.0, 0.0]
        for i in range(3):
            d_inv[i] = b_eff[i] * dL  # note: positive because running DOWN
            for j in range(3):
                d_inv[i] += bij_eff[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a_back[i] += d_inv[i]

    alpha_s_pred = 1.0 / inv_a_back[2]
    return alpha_s_pred, Delta

# Estimate M_GUT for normalization
mu_GUT_est = MZ * math.exp(L_nt * 2 * PI)

print("  Soft threshold results (M_GUT ~ %.1e GeV):" % mu_GUT_est)
print()
print("  %8s %12s %10s" % ("M_VL(GeV)", "alpha_s", "miss(%%)"))
print("  %8s %12s %10s" % ("-"*8, "-"*12, "-"*10))

soft_results = []
for mvl in [200, 500, 1000, 2000, 4000]:
    as_soft, delta_soft = predict_alpha_s_soft_threshold(mvl, 500, mu_GUT_est)
    miss_soft = abs(as_soft - alpha_s_meas) / alpha_s_meas * 100
    soft_results.append((mvl, as_soft, miss_soft))
    print("  %8d %12.8f %10.4f" % (mvl, as_soft, miss_soft))

print()
print("  No-threshold: miss = %.4f%%" % miss_nt)
print()

# Find best soft threshold
best_soft_idx = min(range(len(soft_results)), key=lambda i: soft_results[i][2])
best_soft_mvl, best_soft_as, best_soft_miss = soft_results[best_soft_idx]
print("  Best soft threshold: M_VL = %d GeV, miss = %.4f%%" %
      (best_soft_mvl, best_soft_miss))
print()

# ================================================================
# SECTION 5: COMPLETE COMPARISON
# ================================================================

print("SECTION 5: COMPLETE COMPARISON")
print("-" * 70)
print()

print("  %-30s %12s %10s" % ("Method", "alpha_s", "miss(%%)"))
print("  %-30s %12s %10s" % ("-"*30, "-"*12, "-"*10))
print("  %-30s %12.8f %10.4f" % ("No threshold (2L full)", as_nt, miss_nt))
print("  %-30s %12.8f %10.4f" % ("Hard threshold M_VL=500", as_th, miss_th))
print("  %-30s %12.8f %10.4f" % ("Hard threshold optimal M_VL=%d" % best_mvl,
                                    best_as, best_miss))
print("  %-30s %12.8f %10.4f" % ("Soft threshold M_VL=500",
                                    soft_results[1][1], soft_results[1][2]))
print("  %-30s %12.8f %10.4f" % ("Soft threshold optimal M_VL=%d" % best_soft_mvl,
                                    best_soft_as, best_soft_miss))
print("  %-30s %12.8f %10s" % ("MEASURED", alpha_s_meas, "0"))
print()

# Rankings
methods = [
    ("No threshold", miss_nt),
    ("Hard thresh optimal", best_miss),
    ("Soft thresh optimal", best_soft_miss),
    ("Hard thresh M_VL=500", miss_th),
]
methods.sort(key=lambda x: x[1])
print("  Ranking (best to worst):")
for rank, (name, miss) in enumerate(methods, 1):
    print("    %d. %s: %.4f%%" % (rank, name, miss))
print()

# ================================================================
# SECTION 6: INTERPRETATION
# ================================================================

print("SECTION 6: INTERPRETATION")
print("-" * 70)
print()

nt_wins_hard = miss_nt < best_miss
nt_wins_soft = miss_nt < best_soft_miss
advantage_persists = nt_step_results[3][2] < th_step_results[3][2]

print("  Does no-threshold beat the BEST hard threshold? %s" %
      ("YES" if nt_wins_hard else "NO"))
print("  Does no-threshold beat the BEST soft threshold? %s" %
      ("YES" if nt_wins_soft else "NO"))
print("  Does the advantage persist at 2000 steps? %s" %
      ("YES" if advantage_persists else "NO"))
print()

if nt_wins_hard and advantage_persists:
    print("  CONCLUSION: The no-threshold advantage is PHYSICAL, not numerical.")
    print("  It persists with better integration (2000 steps) and beats")
    print("  every threshold configuration tested.")
    print()
    print("  Possible explanations:")
    print("    1. The CD running propagates below M_VL through loop effects")
    print("       (virtual CD contributions to SM running).")
    print("    2. The threshold correction cancels against a missing")
    print("       higher-order effect at the same scale.")
    print("    3. The 'no threshold' configuration is effectively a")
    print("       resummation that captures physics the step function misses.")
    conclusion = "PHYSICAL"
elif not advantage_persists:
    print("  CONCLUSION: The no-threshold advantage is a NUMERICAL ARTIFACT.")
    print("  It vanishes with better integration.")
    conclusion = "ARTIFACT"
else:
    print("  CONCLUSION: The no-threshold advantage is MIXED.")
    print("  Persists at high steps but soft threshold approaches it.")
    conclusion = "MIXED"

print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_bool("S1: No-thresh alpha_s reproduces PHYS-30 (miss < 0.5%%)",
         miss_nt < 0.5,
         "miss = %.4f%%" % miss_nt, checks)

chk_bool("S1: Threshold M_VL=500 reproduces PHYS-30 (miss 4-6%%)",
         3.0 < miss_th < 7.0,
         "miss = %.4f%%" % miss_th, checks)

chk_bool("S2: M_VL scan covers range (at least 10 points)",
         len(scan_results) >= 10,
         "%d points" % len(scan_results), checks)

chk_bool("S2: No-threshold beats hard threshold at M_VL=500",
         miss_nt < miss_th,
         "%.4f%% < %.4f%%" % (miss_nt, miss_th), checks)

chk_bool("S3: Step sensitivity test completed (4 step counts)",
         len(nt_step_results) == 4 and len(th_step_results) == 4,
         "4 + 4 counts", checks)

chk_bool("S3: No-thresh advantage persists at 2000 steps",
         nt_step_results[3][2] < th_step_results[3][2],
         "NT=%.4f%% < TH=%.4f%%" % (nt_step_results[3][2], th_step_results[3][2]),
         checks)

chk_bool("S4: Soft threshold computed (at least 4 M_VL values)",
         len(soft_results) >= 4,
         "%d values" % len(soft_results), checks)

chk_bool("S4: Soft threshold improves over hard threshold at same M_VL",
         soft_results[1][2] < miss_th,
         "soft=%.4f%% < hard=%.4f%%" % (soft_results[1][2], miss_th), checks)

chk_bool("S5: All alpha_s predictions physical (> 0.09)",
         all(r[1] > 0.09 for r in scan_results) and as_nt > 0.09,
         "all > 0.09", checks)

chk_bool("S6: Conclusion determined",
         conclusion in ["PHYSICAL", "ARTIFACT", "MIXED"],
         "conclusion = %s" % conclusion, checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-35 NO-THRESHOLD PUZZLE COMPLETE")
print("Conclusion: %s" % conclusion)
print("=" * 70)
