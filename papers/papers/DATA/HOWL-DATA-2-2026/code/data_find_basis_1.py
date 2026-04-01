#!/usr/bin/env python3
"""
HOWL-DATA-2 Control Test: Is the composite-base improvement 
specific to physics/math constants, or universal for all irrationals?

Test: generate control irrationals (sqrt of primes, cube roots, 
log ratios, etc.) and measure cofactor improvement from 2^335 
to 60^50 and 210^38. Compare to the improvement seen for 
pi, zeta(3), gamma, R2, etc.

If control irrationals show the SAME improvement → effect is mathematical
If control irrationals show LESS improvement → physics constants have 
genuine structure in composite bases, and we should change basis.
"""

from decimal import Decimal, getcontext
import mpmath

getcontext().prec = 200
mpmath.mp.dps = 130

def factor_small(n, max_prime=997):
    """Extract all prime factors up to max_prime from |n|. Return cofactor digit count."""
    n = abs(n)
    if n == 0:
        return 0
    sieve = list(range(max_prime + 1))
    sieve[1] = 0
    for i in range(2, int(max_prime**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_prime + 1, i):
                sieve[j] = 0
    primes = [x for x in sieve if x > 0]
    for p in primes:
        while n % p == 0:
            n //= p
    return len(str(n)) if n > 1 else 0


def cofactor_in_base(value_str, base, exp):
    """Compute cofactor digit count for value in base^exp."""
    v = Decimal(value_str)
    B_pow = Decimal(base) ** exp
    num = int((v * B_pow).to_integral_value())
    if num == 0:
        return 999
    return factor_small(num)


# ============================================================
# THREE BASES TO COMPARE
# ============================================================
BASES = [
    (2, 335),    # our current basis
    (60, 50),    # best for gamma, R2, ln2, BCS, Bessel
    (210, 38),   # best for pi, zeta(3), zeta(5), sqrt(2)
]

# ============================================================
# PHYSICS/MATH CONSTANTS (the ones that showed improvement)
# ============================================================
physics_constants = [
    ("pi", mpmath.nstr(mpmath.pi, 110)),
    ("e (Euler)", mpmath.nstr(mpmath.e, 110)),
    ("ln(2)", mpmath.nstr(mpmath.log(2), 110)),
    ("R2 = pi/4", mpmath.nstr(mpmath.pi/4, 110)),
    ("R4 = pi^2/32", mpmath.nstr(mpmath.pi**2/32, 110)),
    ("zeta(3)", mpmath.nstr(mpmath.zeta(3), 110)),
    ("zeta(5)", mpmath.nstr(mpmath.zeta(5), 110)),
    ("sqrt(2)", mpmath.nstr(mpmath.sqrt(2), 110)),
    ("sqrt(3)", mpmath.nstr(mpmath.sqrt(3), 110)),
    ("phi (golden)", mpmath.nstr((1+mpmath.sqrt(5))/2, 110)),
    ("gamma (E-M)", mpmath.nstr(mpmath.euler, 110)),
    ("pi/(pi+2) vena", mpmath.nstr(mpmath.pi/(mpmath.pi+2), 110)),
    ("pi/exp(gamma) BCS", mpmath.nstr(mpmath.pi/mpmath.exp(mpmath.euler), 110)),
    ("j11 (Bessel J1 zero)", mpmath.nstr(mpmath.besseljzero(1,1), 110)),
    ("j01 (Bessel J0 zero)", mpmath.nstr(mpmath.besseljzero(0,1), 110)),
    ("2*pi", mpmath.nstr(2*mpmath.pi, 110)),
    ("ln(3)", mpmath.nstr(mpmath.log(3), 110)),
    ("ln(5)", mpmath.nstr(mpmath.log(5), 110)),
    ("ln(7)", mpmath.nstr(mpmath.log(7), 110)),
    ("pi^2/6 = zeta(2)", mpmath.nstr(mpmath.pi**2/6, 110)),
]

# ============================================================
# CONTROL GROUP 1: Square roots of primes (no connection to physics)
# These are algebraic irrationals with no special series structure
# ============================================================
control_sqrt_primes = []
primes_for_sqrt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                   53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for p in primes_for_sqrt:
    val = mpmath.nstr(mpmath.sqrt(p), 110)
    control_sqrt_primes.append((f"sqrt({p})", val))

# ============================================================
# CONTROL GROUP 2: Cube roots of primes (algebraic, different degree)
# ============================================================
control_cbrt_primes = []
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    val = mpmath.nstr(mpmath.cbrt(p), 110)
    control_cbrt_primes.append((f"cbrt({p})", val))

# ============================================================
# CONTROL GROUP 3: Logarithms of primes (transcendental but "generic")
# ============================================================
control_log_primes = []
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    val = mpmath.nstr(mpmath.log(p), 110)
    control_log_primes.append((f"ln({p})", val))

# ============================================================
# CONTROL GROUP 4: Ratios of logarithms (transcendental, unrelated to physics)
# ============================================================
control_log_ratios = []
pairs = [(2,3), (2,5), (2,7), (3,5), (3,7), (5,7), (2,11), (3,11), 
         (5,11), (7,11), (2,13), (3,13), (5,13), (7,13), (11,13)]
for a, b in pairs:
    val = mpmath.nstr(mpmath.log(a)/mpmath.log(b), 110)
    control_log_ratios.append((f"ln({a})/ln({b})", val))

# ============================================================
# CONTROL GROUP 5: "Random" transcendentals from special functions
# ============================================================
control_special = [
    ("BesselJ(0,1)", mpmath.nstr(mpmath.besselj(0, 1), 110)),
    ("BesselJ(1,1)", mpmath.nstr(mpmath.besselj(1, 1), 110)),
    ("BesselJ(0,2)", mpmath.nstr(mpmath.besselj(0, 2), 110)),
    ("Ai(1) Airy", mpmath.nstr(mpmath.airyai(1), 110)),
    ("Ai(2) Airy", mpmath.nstr(mpmath.airyai(2), 110)),
    ("Bi(1) Airy", mpmath.nstr(mpmath.airybi(1), 110)),
    ("erfc(1)", mpmath.nstr(mpmath.erfc(1), 110)),
    ("erfc(2)", mpmath.nstr(mpmath.erfc(2), 110)),
    ("Gamma(1/3)", mpmath.nstr(mpmath.gamma(mpmath.mpf(1)/3), 110)),
    ("Gamma(1/4)", mpmath.nstr(mpmath.gamma(mpmath.mpf(1)/4), 110)),
    ("Gamma(1/5)", mpmath.nstr(mpmath.gamma(mpmath.mpf(1)/5), 110)),
    ("Gamma(1/6)", mpmath.nstr(mpmath.gamma(mpmath.mpf(1)/6), 110)),
    ("Gamma(2/3)", mpmath.nstr(mpmath.gamma(mpmath.mpf(2)/3), 110)),
    ("Gamma(3/4)", mpmath.nstr(mpmath.gamma(mpmath.mpf(3)/4), 110)),
    ("Catalan G", mpmath.nstr(mpmath.catalan, 110)),
    ("Khinchin K", mpmath.nstr(mpmath.khinchin, 110)),
    ("Glaisher A", mpmath.nstr(mpmath.glaisher, 110)),
    ("MRB const", mpmath.nstr(mpmath.nsum(lambda n: (-1)**n * (n**(1/n) - 1), [1, mpmath.inf]), 40)),
    ("sin(1)", mpmath.nstr(mpmath.sin(1), 110)),
    ("cos(1)", mpmath.nstr(mpmath.cos(1), 110)),
]

# ============================================================
# RUN THE TEST
# ============================================================

def test_group(group_name, entries):
    """Test a group of constants across all three bases. Return improvement stats."""
    improvements_60 = []
    improvements_210 = []
    
    print(f"\n{'='*80}")
    print(f"  {group_name} ({len(entries)} entries)")
    print(f"{'='*80}")
    print(f"  {'Name':30s} {'2^335':>7s} {'60^50':>7s} {'210^38':>7s} {'Δ(60)':>7s} {'Δ(210)':>7s}")
    print(f"  {'-'*30} {'-'*7} {'-'*7} {'-'*7} {'-'*7} {'-'*7}")
    
    for name, val_str in entries:
        cofs = []
        for base, exp in BASES:
            cd = cofactor_in_base(val_str, base, exp)
            cofs.append(cd)
        
        d60 = cofs[0] - cofs[1]   # improvement from 2^335 to 60^50
        d210 = cofs[0] - cofs[2]  # improvement from 2^335 to 210^38
        improvements_60.append(d60)
        improvements_210.append(d210)
        
        marker60 = " ***" if d60 > 15 else ""
        marker210 = " ***" if d210 > 15 else ""
        
        print(f"  {name:30s} {cofs[0]:7d} {cofs[1]:7d} {cofs[2]:7d} {d60:+7d}{marker60:4s} {d210:+7d}{marker210}")
    
    # Statistics
    avg_60 = sum(improvements_60) / len(improvements_60) if improvements_60 else 0
    avg_210 = sum(improvements_210) / len(improvements_210) if improvements_210 else 0
    max_60 = max(improvements_60) if improvements_60 else 0
    max_210 = max(improvements_210) if improvements_210 else 0
    min_60 = min(improvements_60) if improvements_60 else 0
    min_210 = min(improvements_210) if improvements_210 else 0
    
    print(f"\n  STATISTICS for {group_name}:")
    print(f"    Improvement 2^335 → 60^50:  avg={avg_60:+.1f}  min={min_60:+d}  max={max_60:+d}")
    print(f"    Improvement 2^335 → 210^38: avg={avg_210:+.1f}  min={min_210:+d}  max={max_210:+d}")
    
    return improvements_60, improvements_210


print("=" * 80)
print("COMPOSITE BASE CONTROL TEST")
print("Question: do physics/math constants show MORE improvement in")
print("composite bases (60^50, 210^38) than generic irrationals?")
print("=" * 80)

# Run all groups
results = {}
results['physics'] = test_group(
    "PHYSICS/MATH CONSTANTS (our constants)", physics_constants)
results['sqrt_primes'] = test_group(
    "CONTROL 1: sqrt(p) for 25 primes", control_sqrt_primes)
results['cbrt_primes'] = test_group(
    "CONTROL 2: cbrt(p) for 15 primes", control_cbrt_primes)
results['log_primes'] = test_group(
    "CONTROL 3: ln(p) for 15 primes", control_log_primes)
results['log_ratios'] = test_group(
    "CONTROL 4: ln(a)/ln(b) for 15 pairs", control_log_ratios)
results['special'] = test_group(
    "CONTROL 5: Special function values (20 entries)", control_special)

# ============================================================
# FINAL COMPARISON
# ============================================================
print("\n\n" + "=" * 80)
print("FINAL COMPARISON: Average cofactor improvement by group")
print("=" * 80)
print(f"  {'Group':45s} {'Avg Δ(60)':>10s} {'Avg Δ(210)':>10s} {'N':>5s}")
print(f"  {'-'*45} {'-'*10} {'-'*10} {'-'*5}")

for group_name, key in [
    ("PHYSICS/MATH CONSTANTS", 'physics'),
    ("Control 1: sqrt(primes)", 'sqrt_primes'),
    ("Control 2: cbrt(primes)", 'cbrt_primes'),
    ("Control 3: ln(primes)", 'log_primes'),
    ("Control 4: ln(a)/ln(b) ratios", 'log_ratios'),
    ("Control 5: Special functions", 'special'),
]:
    imp60, imp210 = results[key]
    avg60 = sum(imp60) / len(imp60)
    avg210 = sum(imp210) / len(imp210)
    print(f"  {group_name:45s} {avg60:+10.1f} {avg210:+10.1f} {len(imp60):5d}")

# Compute significance: is physics group different from controls?
all_control_60 = []
all_control_210 = []
for key in ['sqrt_primes', 'cbrt_primes', 'log_primes', 'log_ratios', 'special']:
    all_control_60.extend(results[key][0])
    all_control_210.extend(results[key][1])

phys_60 = results['physics'][0]
phys_210 = results['physics'][1]

avg_phys_60 = sum(phys_60) / len(phys_60)
avg_ctrl_60 = sum(all_control_60) / len(all_control_60)
avg_phys_210 = sum(phys_210) / len(phys_210)
avg_ctrl_210 = sum(all_control_210) / len(all_control_210)

# Standard deviation of controls
import math
std_ctrl_60 = math.sqrt(sum((x - avg_ctrl_60)**2 for x in all_control_60) / len(all_control_60))
std_ctrl_210 = math.sqrt(sum((x - avg_ctrl_210)**2 for x in all_control_210) / len(all_control_210))

# Z-score for physics group
if std_ctrl_60 > 0:
    z60 = (avg_phys_60 - avg_ctrl_60) / (std_ctrl_60 / math.sqrt(len(phys_60)))
else:
    z60 = 0
if std_ctrl_210 > 0:
    z210 = (avg_phys_210 - avg_ctrl_210) / (std_ctrl_210 / math.sqrt(len(phys_210)))
else:
    z210 = 0

print(f"\n  SIGNIFICANCE TEST:")
print(f"    Physics avg improvement (60^50):  {avg_phys_60:+.1f} digits")
print(f"    Control avg improvement (60^50):  {avg_ctrl_60:+.1f} digits  (σ={std_ctrl_60:.1f})")
print(f"    Z-score (60^50): {z60:.2f}")
print(f"")
print(f"    Physics avg improvement (210^38): {avg_phys_210:+.1f} digits")
print(f"    Control avg improvement (210^38): {avg_ctrl_210:+.1f} digits  (σ={std_ctrl_210:.1f})")
print(f"    Z-score (210^38): {z210:.2f}")
print(f"")
if abs(z60) > 2 or abs(z210) > 2:
    print(f"  *** SIGNIFICANT DIFFERENCE DETECTED ***")
    print(f"  Physics constants show {'MORE' if z60 > 0 else 'LESS'} improvement than controls")
    print(f"  in composite bases. This is NOT a generic mathematical property.")
else:
    print(f"  NO SIGNIFICANT DIFFERENCE.")
    print(f"  The improvement is a generic property of composite bases,")
    print(f"  not specific to physics/math constants.")
    print(f"  Base choice is purely a transport optimization.")

print(f"\n  Total control irrationals tested: {len(all_control_60)}")
print(f"  Total physics constants tested: {len(phys_60)}")

print("\n" + "=" * 80)
print("CONTROL TEST COMPLETE")
print("=" * 80)
