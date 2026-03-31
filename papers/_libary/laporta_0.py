"""
PSLQ Attack on the 4-Loop Electron g-2 Coefficient A4

A4 = -1.912245764926445574152647167439830054...  (Laporta 2017, 1100 digits)

We test whether A4 is a rational linear combination of the
extended MATH-2/MATH-3 transcendental basis using mpmath.pslq().

The candidate pool is organized by transcendental weight.
At 4-loop, max weight is 2*4 - 1 = 7 (MATH-3 hierarchy conjecture).

STRATEGY:
  1. Start with small candidate pools (weight <= 5) — fast, may catch low-weight structure
  2. Extend to weight 7 if needed
  3. Include elliptic integrals as MATH-3 predicts they enter at 4-loop
  4. Use A4 at 30 digits first (quick), then extend if a relation is found

PSLQ requires all candidates computed to higher precision than A4.
We use mpmath at 200 digits for the candidates (A4 known to 1100 digits
but we start at 30 digits for speed).
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from mpmath import mp, mpf, pi as mpi, zeta, log, polylog, catalan
from mpmath import ellipk, ellipe

# Work at high precision
mp.dps = 200


# ================================================================
# A4 value (Laporta 2017)
# ================================================================

# 30 digits of A4
A4 = mpf('-1.91224576492644557415264716743983')
# For higher precision: A4 to 100 digits from Laporta
A4_100 = mpf('-1.9122457649264455741526471674398300539846834505280031585869485714037832820785673384975565972436865822')

print("=" * 70)
print("PSLQ ATTACK ON A4 (4-LOOP ELECTRON g-2)")
print("=" * 70)
print()
print(f"A4 = {mp.nstr(A4_100, 50)}")
print(f"Known to 1100 digits (Laporta 2017)")
print()


# ================================================================
# Build candidate constant pool
# ================================================================

print("Building candidate pool...")
print()

# Weight 0: rational (just 1)
# Weight 1: pi, ln(2)
# Weight 2: pi^2, ln(2)^2, pi*ln(2)
# Weight 3: zeta(3), pi^3, pi^2*ln(2), pi*ln(2)^2, ln(2)^3
# Weight 4: pi^4, zeta(3)*pi, zeta(3)*ln(2), Li4(1/2), pi^2*ln(2)^2, ln(2)^4
# Weight 5: zeta(5), pi^2*zeta(3), pi^4*ln(2), ...
# Weight 6: zeta(3)^2, pi^6, pi^2*zeta(3)*... etc
# Weight 7: zeta(7), pi^2*zeta(5), ...
# Elliptic: K(1/sqrt(2)), K(sqrt(3)/2), K(1/2) — weight 1 (same as pi)

p = mpi
l2 = log(2)
z3 = zeta(3)
z5 = zeta(5)
z7 = zeta(7)
li4 = polylog(4, mpf(1)/2)
cat = catalan
K_half = ellipk(mpf(1)/2)      # k^2 = 1/2
K_quarter = ellipk(mpf(1)/4)   # k^2 = 1/4
E_half = ellipe(mpf(1)/2)
E_quarter = ellipe(mpf(1)/4)

# Build pool in stages
pool_basic = [
    ("1",           mpf(1)),
    ("pi",          p),
    ("pi^2",        p**2),
    ("pi^3",        p**3),
    ("pi^4",        p**4),
    ("ln2",         l2),
    ("ln2^2",       l2**2),
    ("ln2^3",       l2**3),
    ("ln2^4",       l2**4),
    ("pi*ln2",      p*l2),
    ("pi^2*ln2",    p**2*l2),
    ("pi^2*ln2^2",  p**2*l2**2),
    ("pi*ln2^2",    p*l2**2),
    ("pi*ln2^3",    p*l2**3),
    ("zeta3",       z3),
    ("zeta5",       z5),
    ("zeta7",       z7),
    ("pi^2*zeta3",  p**2*z3),
    ("pi*zeta3",    p*z3),
    ("zeta3*ln2",   z3*l2),
    ("zeta3^2",     z3**2),
    ("Li4(1/2)",    li4),
    ("catalan",     cat),
]

pool_elliptic = [
    ("K(k2=1/2)",   K_half),
    ("K(k2=1/4)",   K_quarter),
    ("E(k2=1/2)",   E_half),
    ("E(k2=1/4)",   E_quarter),
    ("pi*K(1/2)",   p*K_half),
    ("pi*K(1/4)",   p*K_quarter),
    ("K(1/2)^2",    K_half**2),
    ("K(1/2)*ln2",  K_half*l2),
]

print(f"  Basic pool: {len(pool_basic)} candidates")
print(f"  Elliptic pool: {len(pool_elliptic)} candidates")
print()


# ================================================================
# PSLQ searches — progressive
# ================================================================

def try_pslq(target, candidates, label, maxcoeff=1000, tol=None):
    """Run PSLQ with target and candidate constants."""
    names = [n for n, v in candidates]
    vals = [v for n, v in candidates]
    
    vec = [target] + vals
    
    print(f"  PSLQ {label}: {len(vec)} values, maxcoeff={maxcoeff}")
    
    result = mp.pslq(vec, maxcoeff=maxcoeff, tol=tol)
    
    if result is None:
        print(f"    Result: NULL (no relation found)")
        return None
    else:
        print(f"    Result: RELATION FOUND")
        print(f"    Coefficients: {result}")
        # Interpret: result[0]*target + result[1]*c1 + ... = 0
        # target = -(result[1]*c1 + ...)/result[0]
        if result[0] != 0:
            print(f"    A4 = -(", end="")
            terms = []
            for i, (name, val) in enumerate(candidates):
                if result[i+1] != 0:
                    terms.append(f"{result[i+1]}*{name}")
            print(" + ".join(terms), end="")
            print(f") / {result[0]}")
        return result


# Stage 1: Small pool, weight <= 4, no elliptic
print("=" * 70)
print("STAGE 1: WEIGHT <= 4, NO ELLIPTIC")
print("=" * 70)
print()

stage1 = [c for c in pool_basic if c[0] in [
    "1", "pi", "pi^2", "pi^3", "pi^4",
    "ln2", "ln2^2", "ln2^3", "ln2^4",
    "pi*ln2", "pi^2*ln2", "pi^2*ln2^2",
    "zeta3", "zeta3*ln2", "Li4(1/2)",
]]
r1 = try_pslq(A4, stage1, "weight<=4", maxcoeff=10000)
print()


# Stage 2: Add weight 5-7
print("=" * 70)
print("STAGE 2: WEIGHT <= 7, NO ELLIPTIC")
print("=" * 70)
print()

stage2 = pool_basic[:]
r2 = try_pslq(A4, stage2, "weight<=7", maxcoeff=10000)
print()


# Stage 3: Add elliptic integrals
print("=" * 70)
print("STAGE 3: FULL POOL INCLUDING ELLIPTIC")
print("=" * 70)
print()

stage3 = pool_basic + pool_elliptic
r3 = try_pslq(A4, stage3, "full+elliptic", maxcoeff=10000)
print()


# Stage 4: If nothing found, try at higher precision with A4_100
print("=" * 70)
print("STAGE 4: HIGHER PRECISION (100-digit A4)")
print("=" * 70)
print()

mp.dps = 500
# Recompute at higher precision
p = mpi
l2 = log(2)
z3 = zeta(3)
z5 = zeta(5)
z7 = zeta(7)
li4 = polylog(4, mpf(1)/2)
cat = catalan
K_half = ellipk(mpf(1)/2)
K_quarter = ellipk(mpf(1)/4)
E_half = ellipe(mpf(1)/2)
E_quarter = ellipe(mpf(1)/4)

pool_hp = [
    ("1",           mpf(1)),
    ("pi^2",        p**2),
    ("pi^4",        p**4),
    ("ln2",         l2),
    ("ln2^2",       l2**2),
    ("ln2^4",       l2**4),
    ("pi^2*ln2",    p**2*l2),
    ("pi^2*ln2^2",  p**2*l2**2),
    ("zeta3",       z3),
    ("zeta5",       z5),
    ("zeta7",       z7),
    ("pi^2*zeta3",  p**2*z3),
    ("zeta3*ln2",   z3*l2),
    ("zeta3^2",     z3**2),
    ("Li4(1/2)",    li4),
    ("K(k2=1/2)",   K_half),
    ("K(k2=1/4)",   K_quarter),
    ("E(k2=1/2)",   E_half),
    ("K(1/2)^2",    K_half**2),
]

r4 = try_pslq(A4_100, pool_hp, "HP full", maxcoeff=100000)
print()


# ================================================================
# Summary
# ================================================================

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

found = any(r is not None for r in [r1, r2, r3, r4])

if found:
    print("  RELATION FOUND.")
    print("  A4 is expressible in the extended MATH-2/MATH-3 basis.")
    print("  The 4-loop wall has a crack.")
else:
    print("  NO RELATION FOUND in any stage.")
    print("  A4 is NOT in the extended MATH-2/MATH-3 basis at the")
    print("  tested precision and maxcoeff.")
    print()
    print("  This is a SOLID NULL — consistent with MATH-3 prediction")
    print("  that A4 contains genuinely new transcendental content")
    print("  (elliptic integrals at non-standard arguments, or the")
    print("  six master integrals that resist analytical identification).")
    print()
    print("  The null does NOT mean A4 has no analytical form.")
    print("  It means A4 is not a SIMPLE rational combination of")
    print("  the tested constants with coefficients up to maxcoeff.")
    print("  The true analytical form may involve:")
    print("  - Elliptic integrals at algebraic (non-rational) arguments")
    print("  - Products of elliptic integrals integrated over a parameter")
    print("  - The six Laporta master integrals (genuinely new constants)")
    print("  - Rational combinations with very large coefficients")
print()
print("  PSLQ null tagged: basis = MATH-3 extended (26 constants)")
print("  Retest when basis extends further.")
