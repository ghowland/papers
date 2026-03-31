import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 60

# ================================================================
# Recover exact alpha^-1 as Fraction from a_e inversion
# (Abbreviated — skip the slow zeta5, use 500 terms)
# ================================================================

def rational_arctan(x, terms=160):
    result = Fraction(0); power = x; x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0: result += power / n
        else: result -= power / n
        power *= x_sq
    return result

def rational_pi(terms=160):
    return 4 * (4 * rational_arctan(Fraction(1,5), terms) - rational_arctan(Fraction(1,239), terms))

def rational_arctanh(x, terms=160):
    result = Fraction(0); power = x; x_sq = x * x
    for k in range(terms):
        result += power / (2 * k + 1)
        power *= x_sq
    return result

def rational_ln2(terms=160):
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def rational_zeta3(n_terms=180):
    total = Fraction(0)
    for k in range(1, n_terms + 1):
        cbc = Fraction(1)
        for j in range(1, k + 1):
            cbc = cbc * (k + j) / j
        total += Fraction((-1)**(k-1)) / (k * k * k * cbc)
    return Fraction(5, 2) * total

def rational_zeta5(n_terms=500):
    eta5 = Fraction(0)
    for n in range(1, n_terms + 1):
        eta5 += Fraction((-1)**(n-1), n**5)
    return Fraction(16, 15) * eta5

def rational_Li4_half(n_terms=300):
    total = Fraction(0); p2 = Fraction(1, 2)
    for n in range(1, n_terms + 1):
        total += p2 / (n**4); p2 /= 2
    return total

print("Computing transcendentals...")
pi_f = rational_pi(160)
ln2 = rational_ln2(160)
ln2_2 = ln2 * ln2; ln2_4 = ln2_2 * ln2_2
pi2 = pi_f * pi_f; pi4 = pi2 * pi2
print("  zeta(3)...")
zeta3 = rational_zeta3(180)
print("  zeta(5) (500 terms)...")
zeta5 = rational_zeta5(500)
print("  Li4(1/2)...")
li4 = rational_Li4_half(300)
print("  Done.")

A1 = Fraction(1, 2)
A2 = (Fraction(197, 144) + pi2/12 + Fraction(3,4)*zeta3 - pi2*ln2/2)
A3 = (Fraction(83,72)*pi2*zeta3 - Fraction(215,24)*zeta5
      + Fraction(100,3)*(li4 + ln2_4/24 - pi2*ln2_2/24)
      - Fraction(239,2160)*pi4 + Fraction(139,18)*zeta3
      - Fraction(298,9)*pi2*ln2 + Fraction(17101,810)*pi2 + Fraction(28259,5184))
A4 = Fraction(-1912245764926445574152647167440, 10**30)

a_e = Fraction(115965218059, 10**14)

# Newton inversion
def f(x):
    x2 = x*x; x3 = x2*x; x4 = x3*x
    return A1*x + A2*x2 + A3*x3 + A4*x4 - a_e

def fprime(x):
    x2 = x*x; x3 = x2*x
    return A1 + 2*A2*x + 3*A3*x2 + 4*A4*x3

x = Fraction(2) * a_e
for i in range(8):
    fx = f(x)
    fpx = fprime(x)
    x = x - fx / fpx
    print(f"  iter {i+1}: 1/alpha = {float(Fraction(1)/(x * pi_f)):.12f}")

# x = alpha/pi as exact Fraction
alpha_over_pi = x
alpha_f = x * pi_f
alpha_inv_f = Fraction(1) / alpha_f

print()
print(f"alpha/pi as Fraction:")
print(f"  numerator has {len(str(alpha_over_pi.numerator))} digits")
print(f"  denominator has {len(str(alpha_over_pi.denominator))} digits")
print()
print(f"alpha^-1 as Fraction:")
print(f"  numerator has {len(str(alpha_inv_f.numerator))} digits")
print(f"  denominator has {len(str(alpha_inv_f.denominator))} digits")
print(f"  float value: {float(alpha_inv_f):.15f}")
print()

# ================================================================
# NOW: remainder scan with exact Fraction alpha_inv
# ================================================================

print("=" * 70)
print("REMAINDER SCAN WITH EXACT FRACTION alpha^-1")
print("=" * 70)
print()

# alpha_inv_f is an exact Fraction. 
# Compute alpha_inv mod (basis constant) where basis constant is also Fraction.
# The quotient is exact integer. The remainder is exact Fraction.

basis_fracs = [
    ("pi",     pi_f),
    ("pi^2",   pi2),
    ("e",      None),  # need to compute
    ("ln(2)",  ln2),
    ("zeta(3)", zeta3),
    ("zeta(5)", zeta5),
]

# Compute e as Fraction
def compute_e(n=80):
    total = Fraction(0); fac = 1
    for i in range(n):
        total += Fraction(1, fac); fac *= (i+1)
    return total

e_f = compute_e(80)
sqrt2_f = Fraction(1); x = Fraction(2)
for _ in range(10): x = (x + Fraction(2)/x)/2
sqrt2_f = x

basis_fracs = [
    ("pi",      pi_f),
    ("2*pi",    2*pi_f),
    ("pi^2",    pi2),
    ("pi^2/6",  pi2/6),
    ("e",       e_f),
    ("ln(2)",   ln2),
    ("sqrt(2)", sqrt2_f),
    ("zeta(3)", zeta3),
    ("zeta(5)", zeta5),
]

print(f"  alpha^-1 = {float(alpha_inv_f):.15f}")
print()
print(f"  {'Modulus':<12} {'q (exact)':>10} {'R (exact float)':>18} {'R/mod':>12}")
print(f"  {'-'*12} {'-'*10} {'-'*18} {'-'*12}")

for name, mod_f in basis_fracs:
    # Exact integer division: q = floor(alpha_inv / mod)
    # alpha_inv_f / mod_f is a Fraction
    ratio = alpha_inv_f / mod_f
    q = int(ratio)  # floor
    remainder = alpha_inv_f - q * mod_f  # exact Fraction
    r_over_mod = remainder / mod_f  # exact Fraction
    
    print(f"  {name:<12} {q:>10} {float(remainder):>18.12f} {float(r_over_mod):>12.8f}")
    
    # Check if r_over_mod is close to a simple fraction
    r_float = float(r_over_mod)
    for denom in range(1, 31):
        numer = round(r_float * denom)
        if numer >= 0:
            diff = abs(r_float - numer/denom)
            if diff < 0.0005:
                print(f"    --> R/mod ~ {numer}/{denom} (off {diff:.6f})")

print()

# The BIG test: alpha_inv_f / zeta(3) — is it close to 114?
ratio_z3 = alpha_inv_f / zeta3
q_z3 = int(ratio_z3)
r_z3 = alpha_inv_f - q_z3 * zeta3
print(f"SPECIAL: alpha^-1 / zeta(3)")
print(f"  quotient = {q_z3}")
print(f"  remainder = {float(r_z3):.15f}")
print(f"  remainder / zeta(3) = {float(r_z3/zeta3):.15f}")
print(f"  Is alpha^-1 = 114 * zeta(3) + epsilon?")
print(f"  114 * zeta(3) = {float(114 * zeta3):.12f}")
print(f"  alpha^-1      = {float(alpha_inv_f):.12f}")
print(f"  epsilon        = {float(alpha_inv_f - 114*zeta3):.12f}")
print()

# Also: alpha_inv - 137 as exact Fraction
frac_part = alpha_inv_f - 137
print(f"alpha^-1 - 137 (exact Fraction):")
print(f"  = {float(frac_part):.15f}")
print()

# Test frac_part against basis
for name, mod_f in basis_fracs:
    ratio = frac_part / mod_f
    r_float = float(ratio)
    if abs(r_float) < 1:
        for denom in range(1, 31):
            numer = round(r_float * denom)
            diff = abs(r_float - numer/denom)
            if diff < 0.001 and numer != 0:
                print(f"  (a^-1 - 137) / {name} ~ {numer}/{denom} (off {diff:.6f})")
                