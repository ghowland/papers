import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf, ellipk, ellipe, clsin

mp.dps = 120

# ================================================================
# GENERATORS (from basis_335.py, plus new ones)
# ================================================================

def rational_arctan(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0: result += power / n
        else: result -= power / n
        power *= x_sq
    return result

def rational_pi(terms=160):
    return 4 * (4 * rational_arctan(Fraction(1,5), terms) - rational_arctan(Fraction(1,239), terms))

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

def compute_ln_from_2(p, q, terms=160):
    """Compute ln(p/q) using ln(2) and arctanh."""
    ln2 = compute_ln2(terms)
    ratio = Fraction(p, q)
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
        total += Fraction((-1)**(k-1)) / (k * k * k * cbc)
    return Fraction(5, 2) * total

def compute_Li_n_half(n, n_terms=500):
    total = Fraction(0)
    p2 = Fraction(1, 2)
    for k in range(1, n_terms + 1):
        total += p2 / Fraction(k**n)
        p2 /= 2
    return total

def compute_catalan(n_terms=350):
    a = [Fraction(1, (2*k+1)**2) for k in range(n_terms + 1)]
    row = list(a)
    total = Fraction(0)
    pow2_inv = Fraction(1, 2)
    sign = Fraction(1)
    for n_val in range(n_terms):
        total += sign * row[0] * pow2_inv
        sign = -sign
        pow2_inv /= 2
        row = [row[i+1] - row[i] for i in range(len(row)-1)]
        if not row: break
    return total

def borwein_zeta(s, n=210):
    """Borwein acceleration for zeta(s). 100+ digits at n=210."""
    d = [Fraction(0)] * (n + 1)
    term = Fraction(1, n)
    running_sum = term
    d[0] = Fraction(n) * running_sum
    for k in range(1, n + 1):
        i = k - 1
        term = term * Fraction(4 * (n + i) * (n - i), (2*i + 1) * (2*i + 2))
        running_sum += term
        d[k] = Fraction(n) * running_sum
    d_n = d[n]
    total = Fraction(0)
    for k in range(n):
        total += Fraction((-1)**k) * (d[k] - d_n) / Fraction((k + 1) ** s)
    eta_s = -total / d_n
    power = 2 ** (s - 1)
    return Fraction(power, power - 1) * eta_s

def hyper_2F1_K(k_squared, N_terms):
    """2F1(1/2, 1/2; 1; k^2) for K(k)."""
    total = Fraction(1)
    term = Fraction(1)
    for n in range(N_terms):
        ratio = Fraction((2*n + 1) * (2*n + 1), (2*n + 2) * (2*n + 2))
        term = term * ratio * k_squared
        total += term
    return total

def hyper_2F1_E(k_squared, N_terms):
    """2F1(-1/2, 1/2; 1; k^2) for E(k)."""
    total = Fraction(1)
    term = Fraction(1)
    for n in range(N_terms):
        a_n = Fraction(-1, 2) + n
        b_n = Fraction(1, 2) + n
        c_n = Fraction(1) + n
        ratio = a_n * b_n / (c_n * (n + 1)) * k_squared
        term = term * ratio
        total += term
    return total

def compute_clausen2_pi3(pi_frac, n_terms=500):
    """Cl_2(pi/3) = sum_{n=1}^{inf} sin(n*pi/3) / n^2.
    sin(n*pi/3) cycles: sqrt(3)/2, sqrt(3)/2, 0, -sqrt(3)/2, -sqrt(3)/2, 0
    Pattern repeats every 6 terms.
    Cl_2(pi/3) = (sqrt(3)/2) * [1/1^2 + 1/2^2 - 1/4^2 - 1/5^2 + 1/7^2 + 1/8^2 - ...]
    """
    sqrt3 = newton_sqrt(3, 10)
    total = Fraction(0)
    for n in range(1, n_terms + 1):
        r = n % 6
        if r == 1 or r == 2:
            total += Fraction(1, n * n)
        elif r == 4 or r == 5:
            total -= Fraction(1, n * n)
        # r == 0 or r == 3: sin = 0, skip
    return sqrt3 * total / 2

# ================================================================
N = 335
Q = 2**N

def to_basis(name, frac_val, ref_val):
    prod = frac_val * Q
    p_floor = prod.numerator // prod.denominator
    remainder = prod - p_floor
    p = p_floor + 1 if remainder >= Fraction(1, 2) else p_floor
    our = mpf(p) / mpf(Q)
    our_str = mp.nstr(our, 100)
    ref_str = mp.nstr(ref_val, 100)
    return p, (our_str == ref_str)

# ================================================================
# COMPUTE ALL 36 CONSTANTS
# ================================================================

print("Computing 36-constant basis...")
print()

# Original 22 from MATH-4
pi_f = rational_pi(160);                    print("  pi")
e_f = compute_e(80);                        print("  e")
ln2_f = compute_ln2(160);                   print("  ln(2)")
sqrt2_f = newton_sqrt(2, 10);               print("  sqrt(2)")
sqrt3_f = newton_sqrt(3, 10);               print("  sqrt(3)")
sqrt5_f = newton_sqrt(5, 10);               print("  sqrt(5)")
sqrt7_f = newton_sqrt(7, 10);               print("  sqrt(7)")
phi_f = compute_phi(10);                    print("  phi")
zeta3_f = compute_zeta3(180);               print("  zeta(3)")
li4_f = compute_Li_n_half(4, 300);          print("  Li4(1/2)")
cat_f = compute_catalan(350);               print("  Catalan")

pi2_f = pi_f * pi_f
pi3_f = pi2_f * pi_f
pi4_f = pi2_f * pi2_f
ln2_2_f = ln2_f * ln2_f
ln2_4_f = ln2_2_f * ln2_2_f
zeta2_f = pi2_f / 6

x32 = (Fraction(3,2)-1)/(Fraction(3,2)+1)
ln3_f = ln2_f + 2 * rational_arctanh(x32, 160)
x54 = (Fraction(5,4)-1)/(Fraction(5,4)+1)
ln5_f = 2*ln2_f + 2*rational_arctanh(x54, 160)
ln10_f = ln2_f + ln5_f
print("  ln(3), ln(5), ln(10)")

epi_f = Fraction(0)
pp = Fraction(1); fac = 1
for k in range(120):
    epi_f += pp / fac; pp *= pi_f; fac *= (k+1)
print("  e^pi")

print("  zeta(5) via Borwein...")
zeta5_f = borwein_zeta(5, 210)
print("  zeta(5) done")

# NEW: 14 additional constants

print("  zeta(7) via Borwein...")
zeta7_f = borwein_zeta(7, 210)
print("  zeta(7) done")

print("  zeta(9) via Borwein...")
zeta9_f = borwein_zeta(9, 210)
print("  zeta(9) done")

print("  Li5(1/2)...")
li5_f = compute_Li_n_half(5, 500)
print("  Li5 done")

print("  Li6(1/2)...")
li6_f = compute_Li_n_half(6, 500)
print("  Li6 done")

print("  Li7(1/2)...")
li7_f = compute_Li_n_half(7, 500)
print("  Li7 done")

print("  ln(7)...")
x74 = (Fraction(7,4)-1)/(Fraction(7,4)+1)
ln7_f = 2*ln2_f + 2*rational_arctanh(x74, 160)  # ln(7) = ln(4) + ln(7/4) = 2ln2 + 2arctanh(3/11)
print("  ln(7) done")

# Elliptic integrals: K and E at three arguments
# K(k) = (pi/2) * 2F1(1/2, 1/2; 1; k^2)
pi_half = pi_f / 2

print("  K(k^2=1/4)...")
K_quarter_f = pi_half * hyper_2F1_K(Fraction(1, 4), 500)
print("  K(1/4) done")

print("  K(k^2=1/2)...")
K_half_f = pi_half * hyper_2F1_K(Fraction(1, 2), 500)
print("  K(1/2) done")

print("  K(k^2=3/4)...")
K_three_quarter_f = pi_half * hyper_2F1_K(Fraction(3, 4), 500)
print("  K(3/4) done")

print("  E(k^2=1/4)...")
E_quarter_f = pi_half * hyper_2F1_E(Fraction(1, 4), 500)
print("  E(1/4) done")

print("  E(k^2=1/2)...")
E_half_f = pi_half * hyper_2F1_E(Fraction(1, 2), 500)
print("  E(1/2) done")

print("  E(k^2=3/4)...")
E_three_quarter_f = pi_half * hyper_2F1_E(Fraction(3, 4), 500)
print("  E(3/4) done")

print("  Cl2(pi/3)...")
cl2_pi3_f = compute_clausen2_pi3(pi_f, 2000)
print("  Cl2(pi/3) done")

print()

# ================================================================
# BUILD THE 36-CONSTANT BASIS
# ================================================================

constants = [
    # Original 22
    ("pi",        pi_f,              mp.pi),
    ("pi^2",      pi2_f,             mp.pi**2),
    ("pi^3",      pi3_f,             mp.pi**3),
    ("pi^4",      pi4_f,             mp.pi**4),
    ("e",         e_f,               mp.e),
    ("e^pi",      epi_f,             mp.exp(mp.pi)),
    ("ln(2)",     ln2_f,             mp.ln(2)),
    ("ln(3)",     ln3_f,             mp.ln(3)),
    ("ln(5)",     ln5_f,             mp.ln(5)),
    ("ln(10)",    ln10_f,            mp.ln(10)),
    ("ln(2)^2",   ln2_2_f,           mp.ln(2)**2),
    ("ln(2)^4",   ln2_4_f,           mp.ln(2)**4),
    ("sqrt(2)",   sqrt2_f,           mp.sqrt(2)),
    ("sqrt(3)",   sqrt3_f,           mp.sqrt(3)),
    ("sqrt(5)",   sqrt5_f,           mp.sqrt(5)),
    ("sqrt(7)",   sqrt7_f,           mp.sqrt(7)),
    ("phi",       phi_f,             mp.phi),
    ("zeta(2)",   zeta2_f,           mp.pi**2/6),
    ("zeta(3)",   zeta3_f,           mp.zeta(3)),
    ("zeta(5)",   zeta5_f,           mp.zeta(5)),
    ("Li4(1/2)",  li4_f,             mp.polylog(4, mpf(1)/2)),
    ("Catalan",   cat_f,             mp.catalan),
    # New 14
    ("zeta(7)",   zeta7_f,           mp.zeta(7)),
    ("zeta(9)",   zeta9_f,           mp.zeta(9)),
    ("Li5(1/2)",  li5_f,             mp.polylog(5, mpf(1)/2)),
    ("Li6(1/2)",  li6_f,             mp.polylog(6, mpf(1)/2)),
    ("Li7(1/2)",  li7_f,             mp.polylog(7, mpf(1)/2)),
    ("ln(7)",     ln7_f,             mp.ln(7)),
    ("K(k2=1/4)", K_quarter_f,       ellipk(mpf(1)/4)),
    ("K(k2=1/2)", K_half_f,          ellipk(mpf(1)/2)),
    ("K(k2=3/4)", K_three_quarter_f, ellipk(mpf(3)/4)),
    ("E(k2=1/4)", E_quarter_f,       ellipe(mpf(1)/4)),
    ("E(k2=1/2)", E_half_f,          ellipe(mpf(1)/2)),
    ("E(k2=3/4)", E_three_quarter_f, ellipe(mpf(3)/4)),
    ("Cl2(pi/3)", cl2_pi3_f,         mp.clsin(2, mp.pi/3)),
    ("ln(7)",     ln7_f,             mp.ln(7)),
]

# Remove duplicate ln(7)
seen = set()
unique_constants = []
for item in constants:
    if item[0] not in seen:
        seen.add(item[0])
        unique_constants.append(item)
constants = unique_constants

print("=" * 75)
print(f"EXTENDED BASIS: {len(constants)} CONSTANTS OVER 2^{N}")
print("=" * 75)
print()

basis = {}
all_match = True
print(f"  {'#':>3} {'Constant':<14} {'Match':>6} {'p digits':>9} {'p bits':>7}")
print(f"  {'---':>3} {'-'*14} {'-'*6} {'-'*9} {'-'*7}")

for i, (name, frac_val, ref_val) in enumerate(constants):
    p, match = to_basis(name, frac_val, ref_val)
    basis[name] = p
    if not match: all_match = False
    print(f"  {i+1:>3} {name:<14} {'YES' if match else 'NO':>6} {len(str(abs(p))):>9} {abs(p).bit_length():>7}")

print()
print(f"  ALL 100-DIGIT MATCHES: {'YES' if all_match else 'NO'}")

if not all_match:
    print()
    print("  Failures:")
    for name, frac_val, ref_val in constants:
        p = basis[name]
        our = mpf(p) / mpf(Q)
        our_s = mp.nstr(our, 100)
        ref_s = mp.nstr(ref_val, 100)
        if our_s != ref_s:
            for j, (a, b) in enumerate(zip(our_s, ref_s)):
                if a != b:
                    print(f"    {name}: diverges at position {j}")
                    break

print()

# Print all numerators
print("=" * 75)
print("ALL NUMERATORS")
print("=" * 75)
print()
for name, _, _ in constants:
    print(f"{name}:")
    print(f"  {basis[name]}")
    print()

# Summary
total_digits = sum(len(str(abs(basis[n]))) for n in basis)
print("=" * 75)
print("SUMMARY")
print("=" * 75)
print()
print(f"  Constants: {len(constants)}")
print(f"  All 100-digit match: {'YES' if all_match else 'NO'}")
print(f"  Total numerator storage: {total_digits} digits")
print(f"  Shared denominator: 2^{N}")
print(f"  Average numerator: {total_digits/len(constants):.0f} digits")
