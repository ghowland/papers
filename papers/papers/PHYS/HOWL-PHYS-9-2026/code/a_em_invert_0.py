import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

# ================================================================
# Transcendentals (MATH-2)
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
    total = Fraction(0)
    p2 = Fraction(1, 2)
    for n in range(1, n_terms + 1):
        total += p2 / (n**4)
        p2 /= 2
    return total

# ================================================================
# Compute transcendentals
# ================================================================

print("Computing transcendentals...")
pi_rat = rational_pi(160)
ln2 = rational_ln2(160)
ln2_2 = ln2 * ln2
ln2_4 = ln2_2 * ln2_2
pi2 = pi_rat * pi_rat
pi4 = pi2 * pi2

print("  zeta(3)...")
zeta3 = rational_zeta3(180)

print("  zeta(5) (10000 terms)...")
zeta5 = rational_zeta5(10000)

print("  Li4(1/2)...")
li4 = rational_Li4_half(300)

print("  Done.")
print()

# ================================================================
# QED coefficients A1-A4 (all Fraction)
# ================================================================

A1 = Fraction(1, 2)

A2 = (Fraction(197, 144)
      + pi2 / 12
      + Fraction(3, 4) * zeta3
      - pi2 * ln2 / 2)

A3 = (Fraction(83, 72) * pi2 * zeta3
      - Fraction(215, 24) * zeta5
      + Fraction(100, 3) * (li4 + ln2_4 / 24 - pi2 * ln2_2 / 24)
      - Fraction(239, 2160) * pi4
      + Fraction(139, 18) * zeta3
      - Fraction(298, 9) * pi2 * ln2
      + Fraction(17101, 810) * pi2
      + Fraction(28259, 5184))

# A4 from Laporta (30-digit rational)
A4 = Fraction(-1912245764926445574152647167440, 10**30)

print("QED Coefficients (all Fraction):")
print(f"  A1 = {float(A1)}")
print(f"  A2 = {float(A2):.12f}")
print(f"  A3 = {float(A3):.12f}")
print(f"  A4 = {float(A4):.12f}")
print()

# ================================================================
# Measured input: a_e from experiment
# ================================================================

# Fan et al. 2023, Northwestern:
# a_e = 1 159 652 180.59(13) × 10^{-12}
# = 0.00115965218059(13)

a_e_measured = Fraction(115965218059, 10**14)

print(f"MEASURED INPUT (one rational from the universe):")
print(f"  a_e = {a_e_measured}")
print(f"      = {float(a_e_measured):.15e}")
print()

# ================================================================
# Solve: a_e = A1*x + A2*x^2 + A3*x^3 + A4*x^4
# for x = alpha/pi
#
# f(x) = A1*x + A2*x^2 + A3*x^3 + A4*x^4 - a_e = 0
# f'(x) = A1 + 2*A2*x + 3*A3*x^2 + 4*A4*x^3
#
# Newton: x_{n+1} = x_n - f(x_n)/f'(x_n)
# ================================================================

print("=" * 65)
print("INVERTING QED SERIES: solve for alpha from a_e")
print("=" * 65)
print()

def f(x):
    return A1*x + A2*x*x + A3*x*x*x + A4*x*x*x*x - a_e_measured

def fprime(x):
    return A1 + 2*A2*x + 3*A3*x*x + 4*A4*x*x*x

# Starting guess: x ~ a_e / A1 = 2*a_e (since A1 = 1/2)
x = Fraction(2) * a_e_measured
print(f"Starting guess: x = 2*a_e = {float(x):.15e}")
print()

# Newton iterations
for i in range(20):
    fx = f(x)
    fpx = fprime(x)
    dx = fx / fpx
    x = x - dx

    # Check convergence
    alpha_over_pi = x
    alpha = x * pi_rat
    alpha_inv = Fraction(1) / alpha if alpha != 0 else Fraction(0)

    residual = float(fx)
    print(f"  iter {i+1:>2}: alpha/pi = {float(x):.18e}, "
          f"1/alpha = {float(alpha_inv):.12f}, "
          f"|f| = {abs(residual):.2e}")

    if abs(residual) < 1e-50:
        print("  Converged.")
        break

print()

# ================================================================
# Result
# ================================================================

alpha_derived = x * pi_rat
alpha_inv_derived = Fraction(1) / alpha_derived

print("=" * 65)
print("RESULT")
print("=" * 65)
print()
print(f"  INPUT:")
print(f"    a_e (measured)     = {float(a_e_measured):.15e}")
print(f"    A1 = 1/2           (integer)")
print(f"    A2 = {float(A2):.10f}  (rationals + pi, zeta3, ln2)")
print(f"    A3 = {float(A3):.10f}   (rationals + pi, zeta3, zeta5, Li4, ln2)")
print(f"    A4 = {float(A4):.10f}  (Laporta 30-digit rational)")
print()
print(f"  OUTPUT:")
print(f"    alpha/pi           = {float(x):.18e}")
print(f"    alpha              = {float(alpha_derived):.15e}")
print(f"    alpha^-1           = {float(alpha_inv_derived):.12f}")
print()
print(f"  COMPARISON:")
print(f"    Our alpha^-1       = {float(alpha_inv_derived):.10f}")
print(f"    CODATA 2022        = 137.035999177")

diff = float(alpha_inv_derived) - 137.035999177
ppm = abs(diff) / 137.036 * 1e6
print(f"    Difference         = {diff:+.12f}")
print(f"    PPM                = {ppm:.4f}")
print()

# How does this compare to the Cs/Rb determination?
# CODATA 2022: alpha^-1 = 137.035999177(21) from Cs interferometry
# Our inversion gives alpha^-1 from a_e + QED integers
print(f"  CODATA uncertainty   = ±0.000000021 (0.15 ppb)")
print(f"  Our residual         = {abs(diff):.12f} ({ppm:.2f} ppm)")
print()

# ================================================================
# What is integer, what is measured
# ================================================================

print("=" * 65)
print("ACCOUNTING")
print("=" * 65)
print()
print("INTEGER CONTENT (the transformation law):")
print("  A1 = 1/2")
print("  A2 = 197/144 + pi^2/12 + 3*zeta(3)/4 - (pi^2/2)*ln(2)")
print("  A3 = [10 terms, all rational coefficients * MATH-2 pairs]")
print("  A4 = 30-digit rational from Laporta")
print("  pi = MATH-2 integer pair")
print("  Newton's method = rational iteration")
print()
print("MEASURED INPUT (one rational from the universe):")
print(f"  a_e = {a_e_measured}")
print()
print("DERIVED OUTPUT:")
print(f"  alpha^-1 = {float(alpha_inv_derived):.12f}")
print()
print("STRUCTURE:")
print("  The QED series is the transformation law.")
print("  The law is integers + MATH-2 transcendentals.")
print("  One measurement (a_e) + the law = alpha.")
print("  alpha is not independently measured here.")
print("  It is DERIVED from a_e via the integer transformation law.")
print()

# ================================================================
# Verify: plug our alpha back into QED series, get a_e back
# ================================================================

print("=" * 65)
print("ROUND-TRIP VERIFICATION")
print("=" * 65)
print()

xcheck = alpha_derived / pi_rat
a_e_check = A1*xcheck + A2*xcheck**2 + A3*xcheck**3 + A4*xcheck**4

print(f"  Plug alpha back into QED series:")
print(f"  a_e (reconstructed) = {float(a_e_check):.15e}")
print(f"  a_e (input)         = {float(a_e_measured):.15e}")
print(f"  Difference          = {float(a_e_check - a_e_measured):.2e}")
print()

# All Fraction check
print(f"  All Fraction:")
print(f"    a_e_measured:    {isinstance(a_e_measured, Fraction)}")
print(f"    alpha_derived:   {isinstance(alpha_derived, Fraction)}")
print(f"    alpha_inv:       {isinstance(alpha_inv_derived, Fraction)}")
print(f"    A1, A2, A3, A4:  {all(isinstance(x, Fraction) for x in [A1,A2,A3,A4])}")

