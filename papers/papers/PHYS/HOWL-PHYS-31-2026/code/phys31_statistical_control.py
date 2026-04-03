#!/usr/bin/env python3
"""
HOWL PHYS-31: phys31_statistical_control.py
=============================================
Statistical Control — Are the Beta Integers Special?

Generates 10,000 random integer pools of the same size and range
as the beta-derived pool. For each random pool, scans all (p/q)*pi^b
formulas against eight measured cosmological targets. Counts how many
random pools produce hits of equal or better quality.

The beta-derived pool: the integers that appear in the SM and CD
modified betas. The measured targets: Lambda, DM/baryon, Omega_b,
Omega_DM, H_0 ratio, sin2_tW, n_s, and the fine structure constant
power for Lambda.

This IS the abort test for Track B.

Backed by: phys25_platform.py (47/47)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import log as mlog, pi as mpi, fabs, mpf, log10 as mlog10
from mpmath import power as mpow
import random

random.seed(2026)  # reproducible

# ================================================================
print("=" * 70)
print("HOWL PHYS-31: STATISTICAL CONTROL")
print("Are the beta integers special?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: THE BETA-DERIVED INTEGER POOL
# ================================================================

print("SECTION 1: THE BETA INTEGER POOL")
print("-" * 70)
print()

# The integers from the SM and CD modified betas:
# SM: b1=41/10, b2=-19/6, b3=-7  -> numerators 41, 19, 7, denoms 10, 6, 1
# CD: b1'=25/6, b2'=-13/6, b3'=-20/3 -> numerators 25, 13, 20, denoms 6, 6, 3
# Shifts: db1=1/15, db2=1, db3=1/3 -> numerators 1, 1, 1, denoms 15, 1, 3
# Derived: 38 (gap num), 27 (gap den), 22 (=2*11, DM integer)
# Also: 3 (N_gen), 5 (from k1=3/5)

beta_pool = sorted(list(set([
    1, 3, 5, 6, 7, 10, 13, 15, 19, 20, 22, 25, 27, 38, 41
])))

print("  Pool: %s" % beta_pool)
print("  Size: %d integers" % len(beta_pool))
print("  Range: [%d, %d]" % (min(beta_pool), max(beta_pool)))
print()

# ================================================================
# SECTION 2: THE EIGHT MEASURED TARGETS
# ================================================================

print("SECTION 2: THE EIGHT MEASURED TARGETS")
print("-" * 70)
print()

# Each target has a measured value and a tolerance (relative %)
# The scan tests formulas of the form (p/q) * pi^b where p,q from pool, b in {-2,-1,0,1,2}
# For dimensionless ratios and log-scale quantities

targets = [
    ("DM/baryon ratio",      5.320,    0.5),    # measured Omega_DM/Omega_b
    ("Omega_b (×100)",       4.93,     1.0),    # Planck 2018: 0.0493
    ("Omega_DM (×100)",      26.4,     1.0),    # Planck 2018: 0.264
    ("H0_CMB/H0_local",      0.9189,   1.0),    # 67.4/73.3 approx
    ("sin2_tW",              0.23122,  0.5),    # electroweak
    ("n_s (spectral index)",  0.965,    0.5),    # Planck
    ("log10(Lambda_Planck)", -121.54,   0.3),    # cosmological constant
    ("alpha_s",              0.1180,   1.0),    # strong coupling
]

for name, val, tol in targets:
    print("  %-25s = %s  (tol: %.1f%%)" % (name, val, tol))
print()

# ================================================================
# SECTION 3: THE SCAN METHOD
# ================================================================

print("SECTION 3: THE SCAN METHOD")
print("-" * 70)
print()
print("  For a pool of N integers, test all formulas:")
print("    value = (p/q) * pi^b")
print("  where p, q are from the pool (p != q), b in {-2,-1,0,1,2}.")
print()
print("  A 'hit' on target T is when |value - T| / |T| < tolerance.")
print("  The score for a pool = number of targets hit.")
print()
print("  Also test:")
print("    value = (p/q)  (no pi)")
print("    value = p * pi^b  (q=1)")
print("    value = (p/q) * pi^b * alpha  (with alpha = 1/137.036)")
print()

pi_val = mpi
alpha_val = mpf("1") / f2m(alpha_inv)
pi_powers = [mpf("1") / (pi_val * pi_val),
             mpf("1") / pi_val,
             mpf("1"),
             pi_val,
             pi_val * pi_val]
pi_labels = [-2, -1, 0, 1, 2]

def scan_pool(pool, targets_list):
    """Scan a pool of integers against all targets.
    Returns (n_hits, per_target_hits, best_formulas)."""
    hit_targets = set()
    best = {}

    # Generate all candidate values
    candidates = []

    for p in pool:
        for q in pool:
            if p == q:
                continue
            ratio = mpf(str(p)) / mpf(str(q))
            for bi, pw in enumerate(pi_powers):
                val = ratio * pw
                candidates.append((val, p, q, pi_labels[bi], False))
                # Also with alpha factor
                val_a = val * alpha_val
                candidates.append((val_a, p, q, pi_labels[bi], True))

        # p alone with pi powers (q=1)
        for bi, pw in enumerate(pi_powers):
            val = mpf(str(p)) * pw
            candidates.append((val, p, 1, pi_labels[bi], False))

    # Also test p*q combinations (products, not just ratios)
    for i in range(len(pool)):
        for j in range(i+1, len(pool)):
            prod = pool[i] * pool[j]
            for bi, pw in enumerate(pi_powers):
                val = mpf(str(prod)) * pw
                candidates.append((val, prod, 1, pi_labels[bi], False))

    # Check each candidate against each target
    for ti, (tname, tval, ttol) in enumerate(targets_list):
        tval_m = mpf(str(tval))
        tol_frac = mpf(str(ttol)) / mpf("100")

        for val, p, q, b, has_alpha in candidates:
            if tval_m != mpf("0"):
                miss = fabs(val - tval_m) / fabs(tval_m)
            else:
                continue

            if miss < tol_frac:
                if ti not in hit_targets:
                    hit_targets.add(ti)
                    best[ti] = (p, q, b, has_alpha, float(miss) * 100)
                else:
                    if float(miss) * 100 < best[ti][4]:
                        best[ti] = (p, q, b, has_alpha, float(miss) * 100)

    return len(hit_targets), hit_targets, best

# ================================================================
# SECTION 4: BETA POOL SCORE
# ================================================================

print("SECTION 4: BETA POOL SCORE")
print("-" * 70)
print()

n_hits_beta, hits_beta, best_beta = scan_pool(beta_pool, targets)

print("  Beta pool hits: %d / %d targets" % (n_hits_beta, len(targets)))
print()

for ti in range(len(targets)):
    if ti in best_beta:
        p, q, b, ha, miss = best_beta[ti]
        alpha_str = " * alpha" if ha else ""
        if q == 1:
            formula = "%d * pi^%d%s" % (p, b, alpha_str)
        else:
            formula = "(%d/%d) * pi^%d%s" % (p, q, b, alpha_str)
        print("    [HIT] %-25s  %s  (miss: %.3f%%)" %
              (targets[ti][0], formula, miss))
    else:
        print("    [MISS] %-25s  no formula found within tolerance" %
              targets[ti][0])
print()

# ================================================================
# SECTION 5: RANDOM POOL MONTE CARLO
# ================================================================

print("SECTION 5: RANDOM POOL MONTE CARLO (10,000 trials)")
print("-" * 70)
print()

N_trials = 10000
pool_size = len(beta_pool)
pool_min = 1
pool_max = 50   # range covering the beta pool

count_equal_or_better = 0
random_scores = []

print("  Generating %d random pools of %d integers from [%d, %d]..." %
      (N_trials, pool_size, pool_min, pool_max))
print()

# Progress reporting
milestones = set([1000, 2000, 3000, 5000, 7500, 10000])

for trial in range(N_trials):
    # Generate random pool: pool_size distinct integers from [1, 50]
    rpool = sorted(random.sample(range(pool_min, pool_max + 1), pool_size))

    n_hits_r, _, _ = scan_pool(rpool, targets)
    random_scores.append(n_hits_r)

    if n_hits_r >= n_hits_beta:
        count_equal_or_better += 1

    if (trial + 1) in milestones:
        p_so_far = count_equal_or_better / (trial + 1)
        print("    Trial %5d:  %d pools >= %d hits.  p ~ %.4f" %
              (trial + 1, count_equal_or_better, n_hits_beta, p_so_far))

print()

# ================================================================
# SECTION 6: P-VALUE AND RESULT
# ================================================================

print("SECTION 6: P-VALUE AND RESULT")
print("-" * 70)
print()

p_value = count_equal_or_better / N_trials

show("  Beta pool hits (dimensionless)", mpf(str(n_hits_beta)))
show("  Random pools tested (dimensionless)", mpf(str(N_trials)))
show("  Random pools with >= %d hits (dimensionless)" % n_hits_beta,
     mpf(str(count_equal_or_better)))
show("  p-value (dimensionless)", mpf(str(p_value)))
print()

# Distribution of random scores
from collections import Counter
score_dist = Counter(random_scores)
print("  Random score distribution:")
for s in sorted(score_dist.keys()):
    pct = score_dist[s] / N_trials * 100
    bar = "#" * int(pct / 2)
    print("    %d hits: %5d pools (%5.1f%%) %s" %
          (s, score_dist[s], pct, bar))
print()

# Mean and std of random scores
mean_score = sum(random_scores) / len(random_scores)
var_score = sum((x - mean_score)**2 for x in random_scores) / len(random_scores)
std_score = var_score ** 0.5

show("  Mean random score (dimensionless)", mpf(str(mean_score)))
show("  Std random score (dimensionless)", mpf(str(std_score)))
show("  Beta pool sigma = (beta - mean) / std (dimensionless)",
     mpf(str((n_hits_beta - mean_score) / std_score)) if std_score > 0 else mpf("0"))
print()

# Decision
print("  DECISION:")
print()
if p_value < 0.01:
    print("  p = %.4f < 0.01" % p_value)
    print("  The beta integers ARE special.")
    print("  Track B: PROMOTED to high confidence.")
    decision = "PROMOTED"
elif p_value < 0.05:
    print("  p = %.4f < 0.05" % p_value)
    print("  The beta integers are moderately special.")
    print("  Track B: ACTIVE (proceed with caution).")
    decision = "ACTIVE"
else:
    print("  p = %.4f >= 0.05" % p_value)
    print("  The beta integers are NOT special.")
    print("  Track B: PARKED (formulas may be coincidence).")
    decision = "PARKED"
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_bool("S1: Beta pool has 15 integers",
         len(beta_pool) == 15,
         "size = %d" % len(beta_pool), checks)

chk_bool("S1: Beta pool range [1, 41]",
         min(beta_pool) == 1 and max(beta_pool) == 41,
         "range = [%d, %d]" % (min(beta_pool), max(beta_pool)), checks)

chk_bool("S4: Beta pool hits > 0",
         n_hits_beta > 0,
         "hits = %d" % n_hits_beta, checks)

chk_bool("S4: Beta pool hits at least 3 targets",
         n_hits_beta >= 3,
         "hits = %d" % n_hits_beta, checks)

chk_bool("S5: All 10,000 trials completed",
         len(random_scores) == N_trials,
         "trials = %d" % len(random_scores), checks)

chk_bool("S5: Random score distribution is reasonable (mean > 0)",
         mean_score > 0,
         "mean = %.2f" % mean_score, checks)

chk_bool("S6: p-value computed",
         p_value >= 0 and p_value <= 1,
         "p = %.4f" % p_value, checks)

# The abort test
chk_bool("S6: Abort test — p < 0.05 (Track B survives)",
         p_value < 0.05,
         "p = %.4f %s 0.05" % (p_value, "<" if p_value < 0.05 else ">="),
         checks)

# Bonus: is beta pool in the top 1%?
chk_bool("S6: Beta pool in top 1%% (p < 0.01, high confidence)",
         p_value < 0.01,
         "p = %.4f %s 0.01" % (p_value, "<" if p_value < 0.01 else ">="),
         checks)

# Check DM/baryon is hit (the strongest known hit at 0.07%)
chk_bool("S4: DM/baryon ratio is hit",
         0 in hits_beta,
         "target 0 %s" % ("HIT" if 0 in hits_beta else "MISS"), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-31 STATISTICAL CONTROL COMPLETE")
print("Track B status: %s" % decision)
print("=" * 70)
