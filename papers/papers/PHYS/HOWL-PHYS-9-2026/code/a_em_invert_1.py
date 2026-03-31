import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

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

def rational_zeta5(n_terms=10000):
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
pi_rat = rational_pi(160)
ln2 = rational_ln2(160)
ln2_2 = ln2 * ln2; ln2_4 = ln2_2 * ln2_2
pi2 = pi_rat * pi_rat; pi4 = pi2 * pi2
print("  zeta(3)...")
zeta3 = rational_zeta3(180)
print("  zeta(5) (10000 terms)...")
zeta5 = rational_zeta5(10000)
print("  Li4(1/2)...")
li4 = rational_Li4_half(300)
print("  Done.")
print()

A1 = Fraction(1, 2)
A2 = (Fraction(197, 144) + pi2/12 + Fraction(3,4)*zeta3 - pi2*ln2/2)
A3 = (Fraction(83,72)*pi2*zeta3 - Fraction(215,24)*zeta5
      + Fraction(100,3)*(li4 + ln2_4/24 - pi2*ln2_2/24)
      - Fraction(239,2160)*pi4 + Fraction(139,18)*zeta3
      - Fraction(298,9)*pi2*ln2 + Fraction(17101,810)*pi2 + Fraction(28259,5184))
A4 = Fraction(-1912245764926445574152647167440, 10**30)

print("QED Coefficients:")
print(f"  A1 = {float(A1)}")
print(f"  A2 = {float(A2):.12f}")
print(f"  A3 = {float(A3):.12f}")
print(f"  A4 = {float(A4):.12f}")
print()

a_e_measured = Fraction(115965218059, 10**14)
print(f"MEASURED INPUT: a_e = {float(a_e_measured):.15e}")
print()

print("=" * 65)
print("INVERTING QED SERIES: solve for alpha from a_e")
print("=" * 65)
print()

def f(x):
    x2 = x*x; x3 = x2*x; x4 = x3*x
    return A1*x + A2*x2 + A3*x3 + A4*x4 - a_e_measured

def fprime(x):
    x2 = x*x; x3 = x2*x
    return A1 + 2*A2*x + 3*A3*x2 + 4*A4*x3

x = Fraction(2) * a_e_measured
print(f"Start: x0 = {float(x):.15e}")
print()

for i in range(15):
    fx = f(x)
    fpx = fprime(x)
    dx = fx / fpx
    x = x - dx
    alpha_inv = Fraction(1) / (x * pi_rat) if x != 0 else Fraction(0)
    print(f"  iter {i+1:>2}: 1/alpha = {float(alpha_inv):.12f}, |f| = {abs(float(fx)):.2e}")
    if abs(float(fx)) < 1e-50:
        print("  Converged.")
        break

print()

alpha_derived = x * pi_rat
alpha_inv_derived = Fraction(1) / alpha_derived

print("=" * 65)
print("RESULT")
print("=" * 65)
print()
print(f"  alpha^-1 (from a_e + QED integers) = {float(alpha_inv_derived):.12f}")
print(f"  alpha^-1 (CODATA 2022)              = 137.035999177")
diff = float(alpha_inv_derived) - 137.035999177
ppm = abs(diff) / 137.036 * 1e6
print(f"  Difference                           = {diff:+.12f}")
print(f"  PPM                                  = {ppm:.4f}")
print()
print(f"  CODATA uncertainty: ±0.000000021 (0.15 ppb)")
print()

# Compare to Cs determination directly
# Parker et al 2018 (Cs): alpha^-1 = 137.035999046(27)
# Morel et al 2020 (Rb): alpha^-1 = 137.035999206(11)
print("  Independent alpha determinations:")
print(f"    From a_e (our calc):     {float(alpha_inv_derived):.9f}")
print(f"    Cs interferometry 2018:  137.035999046(27)")
print(f"    Rb interferometry 2020:  137.035999206(11)")
cs_diff = float(alpha_inv_derived) - 137.035999046
rb_diff = float(alpha_inv_derived) - 137.035999206
print(f"    Our - Cs:                {cs_diff:+.9f} ({abs(cs_diff)/137.036*1e9:.1f} ppb)")
print(f"    Our - Rb:                {rb_diff:+.9f} ({abs(rb_diff)/137.036*1e9:.1f} ppb)")
print()

# Round trip
xcheck = alpha_derived / pi_rat
a_e_check = A1*xcheck + A2*xcheck**2 + A3*xcheck**3 + A4*xcheck**4
print("ROUND-TRIP:")
print(f"  a_e (reconstructed) = {float(a_e_check):.15e}")
print(f"  a_e (input)         = {float(a_e_measured):.15e}")
print(f"  Residual            = {float(a_e_check - a_e_measured):.2e}")
print()

print("=" * 65)
print("WHAT THIS MEANS")
print("=" * 65)
print()
print("  alpha is DERIVED from:")
print("    1. One measured rational: a_e = 115965218059 / 10^14")
print("    2. The integer QED transformation law: A1, A2, A3, A4")
print("    3. MATH-2 transcendentals: pi, zeta(3), zeta(5), Li4(1/2), ln(2)")
print("    4. Newton inversion in Fraction arithmetic")
print()
print("  No second measurement is needed.")
print("  alpha is not independently measured here.")
print("  It is the OUTPUT of the integer law applied to a_e.")
print()
print(f"  Type checks:")
print(f"    a_e:     {type(a_e_measured).__name__}")
print(f"    alpha:   {type(alpha_derived).__name__}")
print(f"    1/alpha: {type(alpha_inv_derived).__name__}")
print(f"    All A_i: {all(isinstance(c, Fraction) for c in [A1,A2,A3,A4])}")
