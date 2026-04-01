#!/usr/bin/env python3
"""
HOWL-DATA-2 Direction 1: Multi-Base Rational Search

For each measured constant, test representation in bases:
  2^335, 3^211, 5^144, 7^119, 11^96, 13^90, 17^81, 19^78, 23^72, 29^65, 31^63, 37^58

For each base B^k (chosen so B^k ~ 10^100):
  numerator = round(value * B^k)
  Factor numerator into primes <= 997
  Record cofactor size

If a constant is "native" to base B, its numerator in B^k will have
a MUCH smaller cofactor than in other bases — because the value is
p/B^j for some small p and j, and multiplying by B^k gives p * B^(k-j),
which is B-smooth with a small cofactor p.

Additionally: continued fraction expansion for each constant.
If any partial quotient is anomalously large, the constant is 
"almost" a simple fraction — that fraction is a candidate structure.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import mpmath
import math

getcontext().prec = 200
mpmath.mp.dps = 130

# ============================================================
# BASES TO TEST
# Each base B has exponent k chosen so B^k ~ 10^100
# ============================================================
BASES = [
    (2, 335),    # 2^335  ~ 10^100.9
    (3, 211),    # 3^211  ~ 10^100.6
    (5, 144),    # 5^144  ~ 10^100.6
    (6, 129),    # 6^129  ~ 10^100.4  (composite: 2*3)
    (7, 119),    # 7^119  ~ 10^100.5
    (10, 100),   # 10^100 ~ 10^100    (the "decimal" basis)
    (11, 96),    # 11^96  ~ 10^99.9
    (12, 93),    # 12^93  ~ 10^100.3  (composite: 2^2*3)
    (13, 90),    # 13^90  ~ 10^100.2
    (17, 81),    # 17^81  ~ 10^99.7
    (19, 78),    # 19^78  ~ 10^99.7
    (23, 72),    # 23^72  ~ 10^98.0
    (29, 65),    # 29^65  ~ 10^95.1
    (30, 65),    # 30^65  ~ 10^96.0  (composite: 2*3*5)
    (31, 63),    # 31^63  ~ 10^93.9
    (37, 58),    # 37^58  ~ 10^91.0
    (42, 55),    # 42^55  ~ 10^89.3  (composite: 2*3*7)
    (60, 50),    # 60^50  ~ 10^88.9  (composite: 2^2*3*5)
    (210, 38),   # 210^38 ~ 10^88.2  (composite: 2*3*5*7, primorial)
]

def factor_small(n, max_prime=997):
    """Extract all prime factors up to max_prime from |n|."""
    n = abs(n)
    if n == 0:
        return {}, 0
    factors = {}
    # test primes up to max_prime using simple trial division
    # generate primes via sieve
    sieve = list(range(max_prime + 1))
    sieve[1] = 0
    for i in range(2, int(max_prime**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_prime + 1, i):
                sieve[j] = 0
    primes = [x for x in sieve if x > 0]
    
    for p in primes:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    
    cofactor_digits = len(str(n)) if n > 1 else 0
    return factors, cofactor_digits


def test_in_base(value_dec, base, exp):
    """Test a Decimal value in base^exp. Return cofactor digit count."""
    B_pow = Decimal(base) ** exp
    num = int((value_dec * B_pow).to_integral_value())
    if num == 0:
        return 0, {}, 0
    _, cofactor_digits = factor_small(num)
    return len(str(abs(num))), {}, cofactor_digits


def continued_fraction(value_str, max_terms=50):
    """
    Compute continued fraction expansion of a value.
    Return list of partial quotients and the best rational approximations.
    """
    # Use mpmath for high precision
    x = mpmath.mpf(value_str)
    cf = []
    convergents = []
    
    # p_{-1}=1, p_0=a_0; q_{-1}=0, q_0=1
    p_prev, p_curr = mpmath.mpf(1), mpmath.floor(x)
    q_prev, q_curr = mpmath.mpf(0), mpmath.mpf(1)
    
    remainder = x
    for i in range(max_terms):
        a = int(mpmath.floor(remainder))
        cf.append(a)
        
        if i == 0:
            p_curr = mpmath.mpf(a)
            q_curr = mpmath.mpf(1)
        else:
            p_new = a * p_curr + p_prev
            q_new = a * q_curr + q_prev
            p_prev, p_curr = p_curr, p_new
            q_prev, q_curr = q_curr, q_new
        
        # Record convergent
        if q_curr > 0:
            conv_val = p_curr / q_curr
            err = abs(x - conv_val)
            if x != 0:
                rel_err = float(err / abs(x))
            else:
                rel_err = 0.0
            convergents.append({
                'p': int(p_curr), 'q': int(q_curr),
                'a': a, 'rel_err': rel_err
            })
        
        # Next step
        frac_part = remainder - a
        if abs(frac_part) < mpmath.mpf(10)**(-110):
            break
        remainder = 1 / frac_part
    
    return cf, convergents


# ============================================================
# THE VALUES TO TEST
# Only fundamentally measured or analytically derived values.
# Full precision strings, no compression.
# ============================================================

values = [
    # Measured fundamental (CODATA 2022) — dimensionless or natural units
    ("alpha^-1", "137.035999177", 12),
    ("m_e (MeV)", "0.51099895069", 11),
    ("m_mu (MeV)", "105.6583755", 10),
    ("m_tau (MeV)", "1776.86", 6),
    ("m_p (MeV)", "938.27208943", 11),
    ("m_p/m_e", "1836.15267343", 13),
    ("R_inf (m^-1)", "10973731.568157", 13),
    ("a_0 (m)", "0.0000000000529177210544", 12),
    ("a_e (g-2 anomaly)", "0.00115965218059", 12),
    ("a_mu (g-2 anomaly)", "0.00116592059", 9),
    ("sin2_theta_W", "0.23122", 5),
    ("alpha_s(M_Z)", "0.1180", 4),
    ("mu_0 (N/A^2)", "0.00000125663706127", 12),
    
    # Electroweak
    ("M_Z (MeV)", "91187.6", 6),
    ("Gamma_Z (MeV)", "2495.2", 5),
    ("M_W (MeV)", "80369.2", 6),
    ("m_t (MeV)", "172570", 5),
    ("m_H (MeV)", "125200", 5),
    ("G_F (GeV^-2)", "0.000011663788", 8),
    
    # Dimensionless mass ratios (the most important for pattern search)
    ("m_mu/m_e", "206.768282708", 10),
    ("m_tau/m_e", "3477.23", 6),
    ("m_tau/m_mu", "16.8170", 6),
    ("m_n/m_p", "1.00137841946", 11),
    ("M_W/M_Z", "0.881361", 6),
    
    # CKM
    ("sin_theta12", "0.22501", 5),
    ("sin_theta23", "0.04182", 4),
    ("sin_theta13", "0.003685", 4),
    
    # Lattice ratios
    ("m_c/m_s", "11.783", 5),
    ("m_b/m_c", "4.578", 4),
    ("m_u/m_d", "0.485", 3),
    
    # Hadron masses (MeV)
    ("m_n (MeV)", "939.56542194", 11),
    ("m_pi+ (MeV)", "139.57039", 8),
    ("m_pi0 (MeV)", "134.9770", 7),
    ("m_K+ (MeV)", "493.677", 6),
    ("m_D (MeV)", "1875.61294500", 12),
    ("E_D binding (MeV)", "2.22456614", 8),
    
    # Clock frequencies (Hz)
    ("H 1S-2S (Hz)", "2466061413187018", 16),
    ("H hyperfine (Hz)", "1420405751.768", 13),
    ("Sr-87 clock (Hz)", "429228004229873.0", 16),
    
    # Proton radius
    ("r_p (fm)", "0.84075", 5),
    
    # Analytical constants
    ("pi", mpmath.nstr(mpmath.pi, 105), 105),
    ("e (Euler)", mpmath.nstr(mpmath.e, 105), 105),
    ("ln(2)", mpmath.nstr(mpmath.log(2), 105), 105),
    ("R2 = pi/4", mpmath.nstr(mpmath.pi/4, 105), 105),
    ("R4 = pi^2/32", mpmath.nstr(mpmath.pi**2/32, 105), 105),
    ("zeta(3)", mpmath.nstr(mpmath.zeta(3), 105), 105),
    ("zeta(5)", mpmath.nstr(mpmath.zeta(5), 105), 105),
    ("sqrt(2)", mpmath.nstr(mpmath.sqrt(2), 105), 105),
    ("gamma (E-M)", mpmath.nstr(mpmath.euler, 105), 105),
    ("pi/(pi+2) vena", mpmath.nstr(mpmath.pi/(mpmath.pi+2), 105), 105),
    ("pi/exp(gamma) BCS", mpmath.nstr(mpmath.pi/mpmath.exp(mpmath.euler), 105), 105),
    ("j11 (Bessel)", mpmath.nstr(mpmath.besseljzero(1,1), 105), 105),
    ("j01 (Bessel)", mpmath.nstr(mpmath.besseljzero(0,1), 105), 105),
    
    # Koide ratio
    ("Koide K(e,mu,tau)", "0.666660511466", 6),
]

# ============================================================
# PART 1: MULTI-BASE COFACTOR SCAN
# ============================================================
print("=" * 90)
print("PART 1: MULTI-BASE COFACTOR SCAN")
print("For each value, test cofactor size in each base B^k")
print("A value 'native' to base B will have a SMALL cofactor in B^k")
print("=" * 90)

# Header
base_labels = [f"{b}^{e}" for b, e in BASES]
print(f"\n{'Value':30s}", end="")
for bl in base_labels:
    print(f" {bl:>7s}", end="")
print("  BEST_BASE")
print("-" * (30 + 8 * len(BASES) + 12))

# For each value, compute cofactor digits in each base
best_bases = {}
for name, val_str, src_dig in values:
    v = Decimal(val_str)
    row = []
    for base, exp in BASES:
        B_pow = Decimal(base) ** exp
        num = int((v * B_pow).to_integral_value())
        if num == 0:
            row.append(999)
            continue
        _, cof_dig = factor_small(num)
        row.append(cof_dig)
    
    # Find minimum cofactor
    min_cof = min(row)
    min_idx = row.index(min_cof)
    best_base = BASES[min_idx]
    best_bases[name] = (best_base, min_cof, row)
    
    print(f"{name:30s}", end="")
    for cd in row:
        marker = " " if cd > min_cof else "*"
        print(f" {cd:6d}{marker}", end="")
    print(f"  {best_base[0]}^{best_base[1]} ({min_cof}d)")

# Summary: which base wins most often?
print("\n" + "=" * 90)
print("BASE WINS SUMMARY (which base gives smallest cofactor most often)")
print("=" * 90)
base_wins = {}
for name, (bb, mc, row) in best_bases.items():
    key = f"{bb[0]}^{bb[1]}"
    base_wins[key] = base_wins.get(key, 0) + 1

for key in sorted(base_wins, key=lambda k: -base_wins[k]):
    print(f"  {key:12s}: {base_wins[key]:3d} wins")

# Values where a non-2 base wins significantly
print("\n" + "=" * 90)
print("VALUES WHERE A NON-POWER-OF-2 BASE WINS")
print("(potential signal of non-binary structure)")
print("=" * 90)
for name, (bb, mc, row) in best_bases.items():
    b2_cof = row[0]  # 2^335 is first base
    if bb[0] != 2 and mc < b2_cof - 2:
        print(f"  {name:30s} best={bb[0]}^{bb[1]} ({mc}d) vs 2^335 ({b2_cof}d)  "
              f"improvement: {b2_cof - mc} digits")


# ============================================================
# PART 2: CONTINUED FRACTION ANALYSIS
# ============================================================
print("\n\n" + "=" * 90)
print("PART 2: CONTINUED FRACTION ANALYSIS")
print("Looking for anomalously large partial quotients")
print("A large a_n means the previous convergent p/q is an unusually good approximation")
print("=" * 90)

for name, val_str, src_dig in values:
    cf, convs = continued_fraction(val_str, max_terms=40)
    
    # Find the largest partial quotient and its position
    if len(cf) < 2:
        continue
    
    max_a = max(cf[1:])  # skip a_0 (integer part)
    max_idx = cf[1:].index(max_a) + 1
    
    # Find convergents that are accurate to measurement precision
    # A convergent with rel_err < 10^(-src_dig) matches to full precision
    best_simple = None
    for c in convs:
        if c['q'] < 10**7 and c['rel_err'] > 0:  # small denominator
            if best_simple is None or c['rel_err'] < best_simple['rel_err']:
                best_simple = c
    
    # Print header for this value
    print(f"\n  {name} (value={val_str[:30]}{'...' if len(val_str)>30 else ''}, {src_dig} digits)")
    print(f"    CF = [{cf[0]}; {', '.join(str(a) for a in cf[1:20])}{'...' if len(cf)>20 else ''}]")
    print(f"    Largest partial quotient: a_{max_idx} = {max_a}")
    
    # Show convergents with small denominators
    print(f"    Best small-denominator approximations (q < 10^7):")
    shown = 0
    for c in convs:
        if c['q'] < 10**7 and c['q'] > 0 and shown < 5:
            # Factor the denominator
            q_factors, _ = factor_small(c['q'])
            q_fstr = " × ".join(f"{p}^{e}" if e > 1 else str(p) 
                               for p, e in sorted(q_factors.items())) if q_factors else str(c['q'])
            digits_matched = -int(math.log10(c['rel_err'])) if c['rel_err'] > 0 else 999
            print(f"      {c['p']}/{c['q']} (q={q_fstr})  "
                  f"rel_err={c['rel_err']:.3e}  matches {digits_matched} digits")
            shown += 1
    
    # Flag if any convergent matches to measurement precision with small q
    for c in convs:
        if c['q'] < 10**6 and c['rel_err'] > 0:
            digits_matched = -int(math.log10(c['rel_err'])) if c['rel_err'] > 0 else 999
            if digits_matched >= src_dig:
                print(f"    *** MATCH TO FULL PRECISION: {c['p']}/{c['q']} "
                      f"matches all {src_dig} source digits! ***")


# ============================================================
# PART 3: FACTOR THE SMALL COFACTORS COMPLETELY
# ============================================================
print("\n\n" + "=" * 90)
print("PART 3: COMPLETE FACTORIZATION OF SMALL COFACTORS")
print("Factoring all cofactors with <= 20 digits using extended trial division")
print("=" * 90)

def full_factor(n, max_trial=1000000):
    """Factor n completely if possible using trial division up to max_trial."""
    if n <= 1:
        return {1: 1}
    factors = {}
    # Trial division
    d = 2
    while d * d <= n and d <= max_trial:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1  # n is prime (or too large to factor)
    return factors

# Collect small cofactors from Q335 
print("\nFrom Q335 = 2^335:")
for name, val_str, src_dig in values:
    v = Decimal(val_str)
    B_pow = Decimal(2) ** 335
    num = int((v * B_pow).to_integral_value())
    if num == 0:
        continue
    n = abs(num)
    # Strip factors of 2
    twos = 0
    while n % 2 == 0:
        twos += 1
        n //= 2
    # Strip small primes
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
        while n % p == 0:
            n //= p
    
    cof_digits = len(str(n)) if n > 1 else 0
    if 1 < cof_digits <= 20:
        ff = full_factor(n)
        fstr = " × ".join(f"{p}^{e}" if e > 1 else str(p)
                         for p, e in sorted(ff.items()))
        is_complete = all(p < 10**10 for p in ff.keys())
        status = "COMPLETE" if is_complete else "PARTIAL"
        print(f"  {name:30s} cofactor={n:>20d} ({cof_digits:2d} digits)  = {fstr}  [{status}]")


print("\n" + "=" * 90)
print("SEARCH COMPLETE")
print("=" * 90)
