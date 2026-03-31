import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

# ================================================================
# MATH-2 INTEGER PAIR GENERATORS
# ================================================================

def rational_arctan(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0:
            result += power / n
        else:
            result -= power / n
        power *= x_sq
    return result

def rational_pi(terms=160):
    a1 = rational_arctan(Fraction(1, 5), terms)
    a2 = rational_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rational_arctanh(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        result += power / (2 * k + 1)
        power *= x_sq
    return result

def compute_e(n_terms=80):
    total = Fraction(0)
    factorial = 1
    for i in range(n_terms):
        total += Fraction(1, factorial)
        factorial *= (i + 1)
    return total

def compute_ln2(terms=160):
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def compute_ln_ratio(p, q, terms=160):
    ratio = Fraction(p, q)
    ln2 = compute_ln2(terms)
    pw = 0
    r = ratio
    while r > 2: r /= 2; pw += 1
    while r < Fraction(1, 2): r *= 2; pw -= 1
    arg = (r - 1) / (r + 1)
    return pw * ln2 + 2 * rational_arctanh(arg, terms)

def newton_sqrt(n, iters=10):
    x = Fraction(n)
    for _ in range(iters):
        x = (x + Fraction(n) / x) / 2
    return x

def compute_phi(iters=10):
    x = Fraction(2)
    for _ in range(iters):
        x = (x * x + 1) / (2 * x - 1)
    return x

def compute_zeta3(n_terms=180):
    total = Fraction(0)
    for k in range(1, n_terms + 1):
        cbc = Fraction(1)
        for j in range(1, k + 1):
            cbc = cbc * (k + j) / j
        sign = (-1) ** (k - 1)
        total += Fraction(sign) / (k * k * k * cbc)
    return Fraction(5, 2) * total

def compute_zeta5(n_terms=10000):
    eta5 = Fraction(0)
    for n in range(1, n_terms + 1):
        eta5 += Fraction((-1)**(n-1), n**5)
    return Fraction(16, 15) * eta5

def compute_Li4_half(n_terms=300):
    total = Fraction(0)
    p2 = Fraction(1, 2)
    for n in range(1, n_terms + 1):
        total += p2 / (n * n * n * n)
        p2 /= 2
    return total

def compute_catalan(n_terms=350):
    a = [Fraction(1, (2*k+1)**2) for k in range(n_terms + 1)]
    row = list(a)
    total = Fraction(0)
    pow2_inv = Fraction(1, 2)
    sign = Fraction(1)
    for n in range(n_terms):
        total += sign * row[0] * pow2_inv
        sign = -sign
        pow2_inv /= 2
        row = [row[i+1] - row[i] for i in range(len(row)-1)]
        if not row:
            break
    return total

# ================================================================
# CONVERT TO p/2^329 FORMAT
# ================================================================

N = 329  # minimal power for 100-digit match
Q = 2**N

def to_power2(name, value_frac, ref_mpf):
    """Convert a MATH-2 Fraction to p/2^329, verify 100-digit match."""
    # p = round(value * 2^329)
    prod = value_frac * Q
    p_floor = prod.numerator // prod.denominator
    remainder = prod - p_floor
    p = p_floor + 1 if remainder >= Fraction(1, 2) else p_floor
    
    # Verify
    our = mpf(p) / mpf(Q)
    ref = ref_mpf
    our_str = mp.nstr(our, 100)
    ref_str = mp.nstr(ref, 100)
    match = (our_str == ref_str)
    
    return p, match, our_str, ref_str

# ================================================================
# COMPUTE ALL CONSTANTS
# ================================================================

print("Computing MATH-2 basis constants...")
print("(This takes a few minutes for zeta(5))")
print()

pi_frac = rational_pi(160)
print("  pi done")

e_frac = compute_e(80)
print("  e done")

ln2_frac = compute_ln2(160)
print("  ln(2) done")

sqrt2_frac = newton_sqrt(2, 10)
print("  sqrt(2) done")

sqrt3_frac = newton_sqrt(3, 10)
print("  sqrt(3) done")

sqrt5_frac = newton_sqrt(5, 10)
print("  sqrt(5) done")

sqrt7_frac = newton_sqrt(7, 10)
print("  sqrt(7) done")

phi_frac = compute_phi(10)
print("  phi done")

zeta3_frac = compute_zeta3(180)
print("  zeta(3) done")

li4_frac = compute_Li4_half(300)
print("  Li4(1/2) done")

catalan_frac = compute_catalan(350)
print("  Catalan done")

# Composed constants
pi2_frac = pi_frac * pi_frac
pi3_frac = pi2_frac * pi_frac
pi4_frac = pi2_frac * pi2_frac
ln2_2_frac = ln2_frac * ln2_frac
ln2_4_frac = ln2_2_frac * ln2_2_frac

# ln(3), ln(5), ln(10)
ln3_frac = compute_ln2(160) + 2 * rational_arctanh((Fraction(3,2) - 1)/(Fraction(3,2) + 1), 160)
ln5_frac = 2 * compute_ln2(160) + 2 * rational_arctanh((Fraction(5,4) - 1)/(Fraction(5,4) + 1), 160)
ln10_frac = ln2_frac + ln5_frac
print("  ln(3), ln(5), ln(10) done")

# zeta(2) = pi^2/6
zeta2_frac = pi2_frac / 6
print("  zeta(2) done")

# e^pi
print("  Computing e^pi (slow)...")
epi_frac = Fraction(0)
pi_power = Fraction(1)
factorial = 1
for k in range(120):
    epi_frac += pi_power / factorial
    pi_power *= pi_frac
    factorial *= (k + 1)
print("  e^pi done")

# zeta(5) — slow
print("  Computing zeta(5) (10000 terms, ~2 min)...")
zeta5_frac = compute_zeta5(10000)
print("  zeta(5) done")

print()
print("All constants computed. Converting to p/2^329 format...")
print()

# ================================================================
# BUILD THE BASIS TABLE
# ================================================================

constants = [
    ("pi",        pi_frac,     mp.pi),
    ("pi^2",      pi2_frac,    mp.pi**2),
    ("pi^3",      pi3_frac,    mp.pi**3),
    ("pi^4",      pi4_frac,    mp.pi**4),
    ("e",         e_frac,      mp.e),
    ("e^pi",      epi_frac,    mp.exp(mp.pi)),
    ("ln(2)",     ln2_frac,    mp.ln(2)),
    ("ln(3)",     ln3_frac,    mp.ln(3)),
    ("ln(5)",     ln5_frac,    mp.ln(5)),
    ("ln(10)",    ln10_frac,   mp.ln(10)),
    ("ln(2)^2",   ln2_2_frac,  mp.ln(2)**2),
    ("ln(2)^4",   ln2_4_frac,  mp.ln(2)**4),
    ("sqrt(2)",   sqrt2_frac,  mp.sqrt(2)),
    ("sqrt(3)",   sqrt3_frac,  mp.sqrt(3)),
    ("sqrt(5)",   sqrt5_frac,  mp.sqrt(5)),
    ("sqrt(7)",   sqrt7_frac,  mp.sqrt(7)),
    ("phi",       phi_frac,    mp.phi),
    ("zeta(2)",   zeta2_frac,  mp.pi**2/6),
    ("zeta(3)",   zeta3_frac,  mp.zeta(3)),
    ("zeta(5)",   zeta5_frac,  mp.zeta(5)),
    ("Li4(1/2)",  li4_frac,    mp.polylog(4, mpf(1)/2)),
    ("Catalan",   catalan_frac, mp.catalan),
]

print("=" * 75)
print(f"MATH-2 BASIS OVER 2^{N}")
print("=" * 75)
print()
print(f"Common denominator: 2^{N}")
print(f"All constants represented as p / 2^{N} where p is a single integer.")
print(f"Addition/subtraction = add/subtract numerators. No LCD computation.")
print()
print(f"  {'Constant':<12} {'100-dig':>8} {'p digits':>10} {'p bits':>8}")
print(f"  {'-'*12} {'-'*8} {'-'*10} {'-'*8}")

basis = {}
all_match = True

for name, frac_val, ref_val in constants:
    p, match, our_str, ref_str = to_power2(name, frac_val, ref_val)
    basis[name] = p
    if not match:
        all_match = False
    print(f"  {name:<12} {'YES' if match else 'NO':>8} {len(str(abs(p))):>10} {abs(p).bit_length():>8}")

print()
print(f"  All 100-digit matches: {'YES' if all_match else 'NO'}")
print()

# ================================================================
# DEMONSTRATE ARITHMETIC
# ================================================================

print("=" * 75)
print("ARITHMETIC DEMONSTRATION")
print("=" * 75)
print()
print("All operations are integer add/subtract/multiply on numerators.")
print(f"Common denominator 2^{N} is carried implicitly.")
print()

# Example 1: pi^2/6 should equal zeta(2)
p_pi2_over_6 = basis["pi^2"]  # This is pi^2 * 2^329, we need pi^2/(6*2^329)... 
# Actually, for division by a small integer, we need to be careful.
# p(pi^2) / 2^329 / 6 is not simply p(pi^2)/6 over 2^329
# unless p(pi^2) is divisible by 6.
# 
# Better: verify that p(zeta(2)) = round(p(pi^2) / 6)
# No — that loses precision.
#
# The right approach: division by small integers requires
# either extending the denominator (2^329 * 6) or noting that
# the numerator must be adjusted.

# For pure addition/subtraction, the common denominator works perfectly:
# pi + e: (p_pi + p_e) / 2^329

p_sum = basis["pi"] + basis["e"]
ref_sum = mp.pi + mp.e
our_sum = mpf(p_sum) / mpf(Q)
print(f"  pi + e:")
print(f"    integer add: p_pi + p_e = {p_sum}")
print(f"    decimal:     {mp.nstr(our_sum, 30)}")
print(f"    mpmath:      {mp.nstr(ref_sum, 30)}")
print(f"    match:       {mp.nstr(our_sum, 100) == mp.nstr(ref_sum, 100)}")
print()

# pi^2 - 6*zeta(2) should be ~0
p_test = basis["pi^2"] - 6 * basis["zeta(2)"]
print(f"  pi^2 - 6*zeta(2):")
print(f"    integer op: p_pi2 - 6*p_zeta2 = {p_test}")
print(f"    (should be 0 or ±1 from rounding)")
print()

# Schwinger term: alpha/(2*pi) where alpha = 1/137.036...
# alpha_inv = 137.036 as measured rational
# In our basis: we can compute 1/(2*pi) as an integer in the 2^329 basis
# p(1/(2*pi)) = round(2^329 / (2*pi)) = round(2^328 / pi)
p_inv_2pi = (2**(N-1) * pi_frac.denominator + pi_frac.numerator // 2) // pi_frac.numerator
# Actually let me do this properly
inv_2pi_frac = Fraction(1, 2) / pi_frac
p_inv_2pi, match_inv, _, _ = to_power2("1/(2pi)", inv_2pi_frac, 1/(2*mp.pi))

print(f"  1/(2*pi):")
print(f"    p = {p_inv_2pi}")
print(f"    100-digit match: {match_inv}")
print()

# A2 coefficient from electron g-2:
# A2 = 197/144 + pi^2/12 + 3*zeta(3)/4 - (pi^2/2)*ln(2)
# In integer arithmetic over 2^329:
# p(A2) = 197*Q/144 + p(pi^2)*Q/(12*Q) ... no, this doesn't work simply
# because rational coefficients times the numerators need the Q factor.
#
# Actually: A2 in the 2^329 basis means p(A2) = round(A2 * 2^329)
# We can compute A2 as a Fraction first (as we do now) then convert.
# OR we can compute directly:
# A2 * 2^329 = (197/144)*2^329 + (1/12)*pi^2*2^329 + ...
# = (197/144)*Q + (1/12)*p(pi^2) + (3/4)*p(zeta3) - (1/2)*p(pi^2*ln2)
# But 197*Q/144 needs Q divisible by 144... Q = 2^329, 144 = 2^4 * 3^2
# So Q/144 = 2^325 / 9 — not an integer.
#
# This shows the limitation: rational COEFFICIENTS times the basis
# require the denominator of the coefficient to divide Q.
# For power-of-2 denominators this works (2^k divides 2^329).
# For other denominators (3, 9, 144...) it doesn't.

print("=" * 75)
print("LIMITATION: RATIONAL COEFFICIENTS")
print("=" * 75)
print()
print("  Addition/subtraction of basis constants: EXACT (integer add)")
print("  Multiplication by integers: EXACT (integer multiply)")
print("  Multiplication by power-of-2 fractions: EXACT (bit shift)")
print("  Multiplication by other rationals (1/3, 197/144): requires")
print("    either extending the denominator or accepting truncation.")
print()
print("  The 2^329 basis is ideal for LINEAR COMBINATIONS with")
print("  integer or power-of-2 coefficients. For general rational")
print("  coefficients, the MATH-2 Fraction basis is more flexible.")
print()
print("  HYBRID: Use 2^329 for the transcendental constants,")
print("  Fraction for the rational coefficients, multiply at the end.")

print()

# ================================================================
# PRINT THE FULL BASIS
# ================================================================

print("=" * 75)
print(f"THE COMPLETE BASIS: p / 2^{N}")
print("=" * 75)
print()

for name, frac_val, ref_val in constants:
    p = basis[name]
    print(f"{name}:")
    print(f"  p = {p}")
    print()

# ================================================================
# STORAGE COMPARISON
# ================================================================

print("=" * 75)
print("STORAGE COMPARISON")
print("=" * 75)
print()
print(f"  {'Constant':<12} {'MATH-2 p+q digits':>20} {'2^329 p digits':>16} {'Compression':>12}")
print(f"  {'-'*12} {'-'*20} {'-'*16} {'-'*12}")

math2_sizes = {
    "pi": (554, 553),
    "pi^2": (1107, 1106),
    "pi^3": (1660, 1659),
    "pi^4": (2213, 2212),
    "e": (117, 116),
    "ln(2)": (213, 213),
    "sqrt(2)": (392, 392),
    "zeta(3)": (309, 309),
    "Catalan": (857, 857),
}

for name in math2_sizes:
    if name in basis:
        p_digits_m2, q_digits_m2 = math2_sizes[name]
        p_digits_new = len(str(abs(basis[name])))
        total_m2 = p_digits_m2 + q_digits_m2
        compression = total_m2 / (p_digits_new + 3)  # +3 for "329" exponent
        print(f"  {name:<12} {total_m2:>20} {p_digits_new:>16} {compression:>11.1f}x")

        