import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

# ================================================================
# GENERATORS
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

def compute_Li4_half(n_terms=300):
    total = Fraction(0)
    p2 = Fraction(1, 2)
    for n in range(1, n_terms + 1):
        total += p2 / (n**4)
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

def borwein_zeta5(n=210):
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
        total += Fraction((-1)**k) * (d[k] - d_n) / Fraction((k + 1) ** 5)
    eta5 = -total / d_n
    return Fraction(16, 15) * eta5

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
print("Computing basis constants...")
pi_f = rational_pi(160);           print("  pi")
e_f = compute_e(80);               print("  e")
ln2_f = compute_ln2(160);          print("  ln(2)")
sqrt2_f = newton_sqrt(2, 10);      print("  sqrt(2)")
sqrt3_f = newton_sqrt(3, 10);      print("  sqrt(3)")
sqrt5_f = newton_sqrt(5, 10);      print("  sqrt(5)")
sqrt7_f = newton_sqrt(7, 10);      print("  sqrt(7)")
phi_f = compute_phi(10);           print("  phi")
zeta3_f = compute_zeta3(180);      print("  zeta(3)")
li4_f = compute_Li4_half(300);     print("  Li4(1/2)")
cat_f = compute_catalan(350);      print("  Catalan")

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
pp = Fraction(1)
fac = 1
for k in range(120):
    epi_f += pp / fac; pp *= pi_f; fac *= (k+1)
print("  e^pi")

print("  zeta(5) via Borwein (210 terms)...")
zeta5_f = borwein_zeta5(210)
print("  zeta(5) done")
print()

# ================================================================
constants = [
    ("pi",       pi_f,     mp.pi),
    ("pi^2",     pi2_f,    mp.pi**2),
    ("pi^3",     pi3_f,    mp.pi**3),
    ("pi^4",     pi4_f,    mp.pi**4),
    ("e",        e_f,      mp.e),
    ("e^pi",     epi_f,    mp.exp(mp.pi)),
    ("ln(2)",    ln2_f,    mp.ln(2)),
    ("ln(3)",    ln3_f,    mp.ln(3)),
    ("ln(5)",    ln5_f,    mp.ln(5)),
    ("ln(10)",   ln10_f,   mp.ln(10)),
    ("ln(2)^2",  ln2_2_f,  mp.ln(2)**2),
    ("ln(2)^4",  ln2_4_f,  mp.ln(2)**4),
    ("sqrt(2)",  sqrt2_f,  mp.sqrt(2)),
    ("sqrt(3)",  sqrt3_f,  mp.sqrt(3)),
    ("sqrt(5)",  sqrt5_f,  mp.sqrt(5)),
    ("sqrt(7)",  sqrt7_f,  mp.sqrt(7)),
    ("phi",      phi_f,    mp.phi),
    ("zeta(2)",  zeta2_f,  mp.pi**2/6),
    ("zeta(3)",  zeta3_f,  mp.zeta(3)),
    ("zeta(5)",  zeta5_f,  mp.zeta(5)),
    ("Li4(1/2)", li4_f,    mp.polylog(4, mpf(1)/2)),
    ("Catalan",  cat_f,    mp.catalan),
]

print("=" * 75)
print(f"MATH-2 UNIVERSAL BASIS OVER 2^{N}")
print("=" * 75)
print()

basis = {}
all_match = True
print(f"  {'Constant':<12} {'Match':>6} {'p digits':>9} {'p bits':>7}")
print(f"  {'-'*12} {'-'*6} {'-'*9} {'-'*7}")

for name, frac_val, ref_val in constants:
    p, match = to_basis(name, frac_val, ref_val)
    basis[name] = p
    if not match: all_match = False
    print(f"  {name:<12} {'YES' if match else 'NO':>6} {len(str(abs(p))):>9} {abs(p).bit_length():>7}")

print()
print(f"  ALL 100-DIGIT MATCHES: {'YES' if all_match else 'NO'}")
print()

# Print full basis
print("=" * 75)
print("THE COMPLETE BASIS")
print("=" * 75)
print()
for name, _, _ in constants:
    print(f"{name}:")
    print(f"  {basis[name]}")
    print()

# Arithmetic demo
print("=" * 75)
print("ARITHMETIC: ADD NUMERATORS")
print("=" * 75)
print()

s = basis["pi"] + basis["e"]
ref = mp.pi + mp.e
our = mpf(s) / mpf(Q)
print(f"  pi + e: {mp.nstr(our, 30)}")
print(f"  mpmath: {mp.nstr(ref, 30)}")
print(f"  match:  {mp.nstr(our, 100) == mp.nstr(ref, 100)}")
print()

d = basis["pi^2"] - 6 * basis["zeta(2)"]
print(f"  pi^2 - 6*zeta(2) = {d}  (rounding residual)")
print()

# Compression
print("=" * 75)
print("COMPRESSION vs MATH-2")
print("=" * 75)
print()
math2 = {
    "pi":(554,553),"pi^2":(1107,1106),"pi^3":(1660,1659),"pi^4":(2213,2212),
    "e":(117,116),"ln(2)":(213,213),"sqrt(2)":(392,392),"sqrt(3)":(293,293),
    "sqrt(5)":(215,214),"sqrt(7)":(421,421),"phi":(428,428),"zeta(2)":(1107,1106),
    "zeta(3)":(309,309),"Li4(1/2)":(309,309),"Catalan":(857,857),"e^pi":(65935,65933),
}
print(f"  {'Constant':<12} {'MATH-2':>10} {'2^335':>10} {'Ratio':>8}")
print(f"  {'-'*12} {'-'*10} {'-'*10} {'-'*8}")
for name in math2:
    if name in basis:
        pd,qd = math2[name]
        nd = len(str(abs(basis[name])))
        print(f"  {name:<12} {pd+qd:>10} {nd:>10} {(pd+qd)/nd:>7.1f}x")

total_digits = sum(len(str(abs(basis[n]))) for n in basis)
print()
print(f"  Total basis: {total_digits} digits + shared 2^{N}")
