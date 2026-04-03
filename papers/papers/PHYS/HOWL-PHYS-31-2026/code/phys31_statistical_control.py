#!/usr/bin/env python3
"""
HOWL PHYS-31: phys31_statistical_control.py
=============================================
Statistical Control — Are the Beta Integers Special?

Generates 10,000 random integer pools of the same size and range
as the beta-derived pool. For each, scans (p/q)*pi^b formulas
against eight measured targets. Reports the p-value.

Uses Python floats for the Monte Carlo (sufficient for %-level
tolerance checks). Fraction arithmetic only for the beta pool
verification against the library.

This IS the abort test for Track B.

Backed by: phys25_platform.py (47/47)
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *
from mpmath import pi as mpi, fabs as mfabs, mpf
import random
import math

random.seed(2026)

# ================================================================
print("=" * 70)
print("HOWL PHYS-31: STATISTICAL CONTROL")
print("Are the beta integers special?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: THE BETA INTEGER POOL
# ================================================================

print("SECTION 1: THE BETA INTEGER POOL")
print("-" * 70)
print()

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

targets = [
    ("DM/baryon ratio",       5.320,    0.5),
    ("Omega_b (x100)",        4.93,     1.0),
    ("Omega_DM (x100)",      26.4,      1.0),
    ("H0_CMB/H0_local",       0.9189,   1.0),
    ("sin2_tW",               0.23122,  0.5),
    ("n_s (spectral index)",  0.965,    0.5),
    ("log10(Lambda_Planck)", -121.54,   0.3),
    ("alpha_s",               0.1180,   1.0),
]

for name, val, tol in targets:
    print("  %-25s = %-10s (tol: %.1f%%)" % (name, val, tol))
print()

# ================================================================
# SECTION 3: SCAN METHOD (float arithmetic for speed)
# ================================================================

print("SECTION 3: SCAN METHOD")
print("-" * 70)
print()
print("  Formula: value = (p/q) * pi^b")
print("  p, q from pool (p != q), plus p with q=1")
print("  b in {-2, -1, 0, 1, 2}")
print("  Also: value * alpha (with alpha = 1/137.036)")
print("  Hit: |value - target| / |target| < tolerance")
print()

PI = math.pi
ALPHA = 1.0 / 137.035999177
PI_POWERS = [1.0 / (PI * PI), 1.0 / PI, 1.0, PI, PI * PI]
PI_LABELS = [-2, -1, 0, 1, 2]

def scan_pool_fast(pool, targets_list):
    """Scan using float arithmetic. Returns (n_hits, hit_set, best_dict)."""
    hit_set = set()
    best = {}

    # Precompute all candidate values
    candidates = []
    n = len(pool)

    # (p/q) * pi^b and (p/q) * pi^b * alpha
    for i in range(n):
        p = pool[i]
        for j in range(n):
            if i == j:
                continue
            q = pool[j]
            ratio = float(p) / float(q)
            for bi in range(5):
                val = ratio * PI_POWERS[bi]
                candidates.append((val, p, q, PI_LABELS[bi], False))
                candidates.append((val * ALPHA, p, q, PI_LABELS[bi], True))

        # p with q=1
        fp = float(p)
        for bi in range(5):
            val = fp * PI_POWERS[bi]
            candidates.append((val, p, 1, PI_LABELS[bi], False))
            candidates.append((val * ALPHA, p, 1, PI_LABELS[bi], True))

    # Check candidates against targets
    for ti in range(len(targets_list)):
        tname, tval, ttol = targets_list[ti]
        tol_frac = ttol / 100.0
        abs_tval = abs(tval)
        if abs_tval == 0:
            continue

        for val, p, q, b, ha in candidates:
            miss = abs(val - tval) / abs_tval
            if miss < tol_frac:
                if ti not in hit_set:
                    hit_set.add(ti)
                    best[ti] = (p, q, b, ha, miss * 100)
                elif miss * 100 < best[ti][4]:
                    best[ti] = (p, q, b, ha, miss * 100)

    return len(hit_set), hit_set, best

def scan_pool_count(pool, targets_list):
    """Fast version: only returns hit count."""
    hits = set()
    n = len(pool)

    for ti in range(len(targets_list)):
        tname, tval, ttol = targets_list[ti]
        tol_frac = ttol / 100.0
        abs_tval = abs(tval)
        if abs_tval == 0:
            continue

        found = False
        for i in range(n):
            if found:
                break
            p = pool[i]
            for j in range(n):
                if found:
                    break
                if i == j:
                    continue
                q = pool[j]
                ratio = float(p) / float(q)
                for bi in range(5):
                    val = ratio * PI_POWERS[bi]
                    if abs(val - tval) / abs_tval < tol_frac:
                        found = True
                        break
                    if abs(val * ALPHA - tval) / abs_tval < tol_frac:
                        found = True
                        break

            if not found:
                # p with q=1
                fp = float(p)
                for bi in range(5):
                    val = fp * PI_POWERS[bi]
                    if abs(val - tval) / abs_tval < tol_frac:
                        found = True
                        break
                    if abs(val * ALPHA - tval) / abs_tval < tol_frac:
                        found = True
                        break

        if found:
            hits.add(ti)

    return len(hits)

# ================================================================
# SECTION 4: BETA POOL SCORE
# ================================================================

print("SECTION 4: BETA POOL SCORE")
print("-" * 70)
print()

n_hits_beta, hits_beta, best_beta = scan_pool_fast(beta_pool, targets)

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
        print("    [HIT]  %-25s  %s  (miss: %.3f%%)" %
              (targets[ti][0], formula, miss))
    else:
        print("    [MISS] %-25s  no formula found" % targets[ti][0])
print()

# ================================================================
# SECTION 5: MONTE CARLO
# ================================================================

print("SECTION 5: MONTE CARLO (10,000 trials)")
print("-" * 70)
print()

N_trials = 10000
pool_size = len(beta_pool)
pool_min = 1
pool_max = 50

count_equal_or_better = 0
random_scores = []

print("  Running %d trials..." % N_trials)

for trial in range(N_trials):
    rpool = sorted(random.sample(range(pool_min, pool_max + 1), pool_size))
    n_hits_r = scan_pool_count(rpool, targets)
    random_scores.append(n_hits_r)
    if n_hits_r >= n_hits_beta:
        count_equal_or_better += 1

    if (trial + 1) % 2000 == 0:
        p_so_far = count_equal_or_better / (trial + 1)
        print("    Trial %5d:  %d pools >= %d hits.  p ~ %.4f" %
              (trial + 1, count_equal_or_better, n_hits_beta, p_so_far))

print()

# ================================================================
# SECTION 6: RESULTS
# ================================================================

print("SECTION 6: P-VALUE AND RESULT")
print("-" * 70)
print()

p_value = count_equal_or_better / N_trials

show("  Beta pool hits (dimensionless)", mpf(str(n_hits_beta)))
show("  Trials (dimensionless)", mpf(str(N_trials)))
show("  Pools >= %d hits (dimensionless)" % n_hits_beta,
     mpf(str(count_equal_or_better)))
show("  p-value (dimensionless)", mpf(str(p_value)))
print()

# Score distribution
print("  Random score distribution:")
from collections import Counter
score_dist = Counter(random_scores)
for s in sorted(score_dist.keys()):
    pct = score_dist[s] / N_trials * 100
    bar = "#" * max(1, int(pct / 2))
    print("    %d hits: %5d pools (%5.1f%%) %s" %
          (s, score_dist[s], pct, bar))
print()

mean_score = sum(random_scores) / len(random_scores)
var_score = sum((x - mean_score)**2 for x in random_scores) / len(random_scores)
std_score = var_score ** 0.5
if std_score > 0:
    sigma = (n_hits_beta - mean_score) / std_score
else:
    sigma = 0.0

show("  Mean random score (dimensionless)", mpf(str(round(mean_score, 3))))
show("  Std random score (dimensionless)", mpf(str(round(std_score, 3))))
show("  Beta pool sigma deviation (dimensionless)", mpf(str(round(sigma, 2))))
print()

# Decision
print("  DECISION:")
print()
if p_value < 0.01:
    print("  p = %.4f < 0.01" % p_value)
    print("  The beta integers ARE special (top 1%%).")
    print("  Track B: PROMOTED to high confidence.")
    decision = "PROMOTED"
elif p_value < 0.05:
    print("  p = %.4f < 0.05" % p_value)
    print("  The beta integers are moderately special.")
    print("  Track B: ACTIVE (proceed with caution).")
    decision = "ACTIVE"
else:
    print("  p = %.4f >= 0.05" % p_value)
    print("  The beta integers are NOT special at 5%% level.")
    print("  Track B: PARKED.")
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

chk_bool("S1: Pool range [1, 41]",
         min(beta_pool) == 1 and max(beta_pool) == 41,
         "[%d, %d]" % (min(beta_pool), max(beta_pool)), checks)

chk_bool("S4: Beta pool hits > 0",
         n_hits_beta > 0,
         "hits = %d" % n_hits_beta, checks)

chk_bool("S4: Beta pool hits >= 3",
         n_hits_beta >= 3,
         "hits = %d" % n_hits_beta, checks)

chk_bool("S4: DM/baryon is hit",
         0 in hits_beta,
         "target 0 %s" % ("HIT" if 0 in hits_beta else "MISS"), checks)

chk_bool("S4: sin2_tW is hit",
         4 in hits_beta,
         "target 4 %s" % ("HIT" if 4 in hits_beta else "MISS"), checks)

chk_bool("S5: All trials completed",
         len(random_scores) == N_trials,
         "%d trials" % len(random_scores), checks)

chk_bool("S5: Mean random score > 0",
         mean_score > 0,
         "mean = %.2f" % mean_score, checks)

chk_bool("S6: p-value valid",
         0 <= p_value <= 1,
         "p = %.4f" % p_value, checks)

# The gate
chk_bool("S6: GATE — p < 0.05 (Track B survives)",
         p_value < 0.05,
         "p = %.4f %s 0.05" % (p_value, "<" if p_value < 0.05 else ">="),
         checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-31 STATISTICAL CONTROL COMPLETE")
print("Track B status: %s" % decision)
print("=" * 70)
