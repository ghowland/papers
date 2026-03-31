#!/usr/bin/env python3
"""
DISC-8 Phase 1, Item 1: Formal Control Test
=============================================
Generate 1000 random numbers per SM target magnitude.
Run identical modular scan from DISC-7 Phase 4B.
Compare hit rates: SM targets vs random controls.

This gates the priority of all derivation attempts.
"""

import random
from mpmath import mp, mpf, pi, zeta, log, sqrt, e as me, phi

mp.dps = 50
random.seed(42)  # Fixed seed for reproducibility

print("=" * 70)
print("DISC-8 PHASE 1, ITEM 1: FORMAL CONTROL TEST")
print("=" * 70)
print()

R2 = pi / 4
R4 = pi**2 / 32

# The 18 moduli from DISC-7 Phase 4B (identical protocol)
moduli = [
    ("R2", R2), ("2R2", 2*R2), ("4R2=pi", 4*R2), ("8R2=2pi", 8*R2),
    ("R4", R4), ("32R4=pi^2", 32*R4), ("256R4=8pi^2", 256*R4),
    ("pi*ln2", pi*log(2)), ("pi*zeta3", pi*zeta(3)),
    ("pi*e", pi*me), ("R2*zeta3", R2*zeta(3)),
    ("R2*ln2", R2*log(2)), ("R2*e", R2*me),
    ("R4*pi", R4*pi), ("ln2*zeta3", log(2)*zeta(3)),
    ("sqrt2*pi", sqrt(2)*pi),
    ("1/(12R2)", 1/(12*R2)), ("1/(3pi)", 1/(3*pi)),
]

# The SM targets from DISC-7 Phase 4B (13 targets)
sm_targets = [
    ("alpha_inv",    137.035999177),
    ("alpha_inv_MZ", 127.906),
    ("sin2_tW",      0.23122),
    ("alpha_s",      0.1180),
    ("m_mu/m_e",     206.7682830),
    ("m_tau/m_e",    3477.1507),
    ("m_tau/m_mu",   16.8170),
    ("M_W/M_Z",      0.88147),
    ("M_H/M_Z",      1.37193),
    ("M_H/M_W",      1.55670),
    ("sin_t12",      0.2253),
    ("sin_t23",      0.0412),
    ("delta_CP",     1.36),
]

def count_hits(target_val, moduli_list, threshold=0.0005, max_denom=20):
    """Count modular hits for a single target value.
    Identical protocol to DISC-7 Phase 4B."""
    hits = 0
    for mname, mval in moduli_list:
        mval_f = float(mval)
        if mval_f <= 0 or mval_f > abs(target_val) * 1000:
            continue
        q = int(target_val / mval_f)
        r = target_val - q * mval_f
        rm = r / mval_f
        if rm < 0:
            rm += 1
            q -= 1
        for d in range(1, max_denom + 1):
            p_num = round(rm * d)
            if p_num >= 0 and d > 0:
                diff = abs(rm - p_num / d)
                if diff < threshold and not (p_num == 0 and q == 0):
                    hits += 1
    return hits

# ================================================================
# COUNT SM HITS (reproduce DISC-7 numbers)
# ================================================================

print("SM TARGET HITS (DISC-7 Phase 4B protocol):")
print()
print(f"  {'Target':<14} {'Value':>14} {'Hits':>6}")
print(f"  {'-'*14} {'-'*14} {'-'*6}")

sm_hit_counts = {}
sm_total = 0
for tname, tval in sm_targets:
    h = count_hits(tval, moduli)
    sm_hit_counts[tname] = h
    sm_total += h
    print(f"  {tname:<14} {tval:>14.6f} {h:>6}")

print(f"  {'TOTAL':<14} {'':>14} {sm_total:>6}")
print()

# ================================================================
# CONTROL: 1000 RANDOM NUMBERS PER TARGET MAGNITUDE
# ================================================================

print("CONTROL TEST: 1000 random numbers per target magnitude")
print()

N_RANDOM = 1000

print(f"  {'Target':<14} {'Range':>20} {'Mean hits':>10} {'Std':>8} "
      f"{'SM hits':>8} {'z-score':>8} {'p < 0.05?':>10}")
print(f"  {'-'*14} {'-'*20} {'-'*10} {'-'*8} {'-'*8} {'-'*8} {'-'*10}")

total_random_hits = 0
significant_count = 0

for tname, tval in sm_targets:
    # Generate 1000 random numbers in [0.9X, 1.1X]
    lo = 0.9 * tval
    hi = 1.1 * tval
    
    random_hits = []
    for _ in range(N_RANDOM):
        rv = random.uniform(lo, hi)
        h = count_hits(rv, moduli)
        random_hits.append(h)
    
    mean_h = sum(random_hits) / len(random_hits)
    var_h = sum((x - mean_h)**2 for x in random_hits) / len(random_hits)
    std_h = var_h ** 0.5
    
    sm_h = sm_hit_counts[tname]
    
    if std_h > 0:
        z = (sm_h - mean_h) / std_h
    else:
        z = 0.0 if sm_h == mean_h else float('inf')
    
    sig = "YES" if abs(z) > 1.96 else "no"
    if abs(z) > 1.96:
        significant_count += 1
    
    total_random_hits += mean_h
    
    range_str = f"[{lo:.4f}, {hi:.4f}]"
    print(f"  {tname:<14} {range_str:>20} {mean_h:>10.2f} {std_h:>8.2f} "
          f"{sm_h:>8} {z:>8.2f} {sig:>10}")

print()
print(f"  SM total hits: {sm_total}")
print(f"  Random mean total: {total_random_hits:.1f}")
print(f"  Targets with significant excess: {significant_count} / {len(sm_targets)}")
print()

# ================================================================
# VERDICT
# ================================================================

print("=" * 70)
print("VERDICT")
print("=" * 70)
print()

if sm_total <= total_random_hits * 1.5:
    print("  OUTCOME (a): SM hit count is comparable to random controls.")
    print("  The DISC-7 modular search hits are consistent with noise.")
    print("  The alpha_s = pi*zeta(3)/32 candidate is DOWNGRADED.")
    print("  Item 3 (derivation attempt) drops in priority.")
elif sm_total > total_random_hits * 3:
    print("  OUTCOME (b): SM hit count significantly exceeds random controls.")
    print("  The modular search shows signal above noise.")
    print("  The alpha_s candidate is UPGRADED.")
    print("  Item 3 (derivation attempt) gains priority.")
else:
    print("  OUTCOME (c): Intermediate result.")
    print("  Some targets may show excess, others not.")
    print("  Per-target analysis needed.")
print()

# ================================================================
# ALPHA_S SPECIFIC CHECK
# ================================================================

print("=" * 70)
print("ALPHA_S SPECIFIC: Is the pi*zeta(3)/32 hit special?")
print("=" * 70)
print()

# How often does a random number near 0.118 produce a hit
# with R2*zeta3 at remainder ~1/8?
alpha_s_val = 0.1180
R2_zeta3 = float(R2 * zeta(3))

count_similar = 0
for _ in range(10000):
    rv = random.uniform(0.9 * alpha_s_val, 1.1 * alpha_s_val)
    q = int(rv / R2_zeta3)
    r = rv - q * R2_zeta3
    rm = r / R2_zeta3
    if rm < 0:
        rm += 1
    # Check if rm is within 0.0005 of 1/8
    if abs(rm - 1/8) < 0.0005:
        count_similar += 1

print(f"  Random numbers near {alpha_s_val} tested: 10000")
print(f"  Hits with R2*zeta3 remainder ~ 1/8 (within 0.05%): {count_similar}")
print(f"  Rate: {count_similar/10000*100:.2f}%")
print(f"  Expected by chance (0.1% window on [0,1]): ~0.1%")
print()
if count_similar > 5:
    print(f"  The hit rate {count_similar/100:.1f}% is comparable to random chance.")
    print("  The alpha_s = pi*zeta(3)/32 candidate is NOT distinguishable")
    print("  from a coincidence at this precision.")
else:
    print(f"  The hit rate {count_similar/100:.1f}% is below random expectation.")
    print("  The alpha_s candidate may have significance beyond chance.")

    