import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass
from fractions import Fraction
from mpmath import mp, mpf, pi as mpi, zeta, log, polylog
mp.dps = 200

A4 = mpf('-1.9122457649264455741526471674398300539846834505280031585869485714037832820785673384975565972436865822')

print("=" * 70)
print("A4 DECOMPOSITION: KNOWN TRANSCENDENTAL CONTENT")
print("=" * 70)
print(f"A4 = {mp.nstr(A4, 50)}")
print()

# Transcendental constants
print("Constants at 200 digits:")
z3 = zeta(3); z5 = zeta(5); z7 = zeta(7); l2 = log(2)
for n in [3,5,7]:
    print(f"  zeta({n}) = {mp.nstr(zeta(n), 25)}")
print(f"  ln(2) = {mp.nstr(l2, 25)}")
print()

# Li_n(1/2) in Fraction arithmetic
def Li_n_half_frac(n, N=500):
    total = Fraction(0)
    p2 = Fraction(1, 2)
    for k in range(1, N+1):
        total += p2 / Fraction(k**n)
        p2 /= 2
    return total

print("Polylogarithm constants Li_n(1/2) in Fraction arithmetic:")
for n in [4, 5, 6, 7]:
    val = Li_n_half_frac(n, 500)
    ref = polylog(n, mpf(1)/2)
    val_mp = mpf(val.numerator) / mpf(val.denominator)
    diff = abs(val_mp - ref)
    digits = -int(mp.log10(diff)) if diff > 0 else 999
    print(f"  Li_{n}(1/2): {mp.nstr(val_mp, 25)}  ({digits} digits, "
          f"p={val.numerator.bit_length()} bits, Fraction: {isinstance(val, Fraction)})")
print()

# U term rational coefficients
print("=" * 70)
print("U TERM: SIX MASTER INTEGRALS")
print("=" * 70)
print()
U_coeffs = [
    ("C81a", Fraction(174623, 288000)),
    ("C81b", Fraction(29479, 7200)),
    ("C81c", Fraction(-43, 6)),
    ("C83a", Fraction(10871, 14400)),
    ("C83b", Fraction(-157, 1620)),
    ("C83c", Fraction(-95, 24)),
]
print("Rational coefficients (Laporta Eq. 53):")
for name, coeff in U_coeffs:
    print(f"  {name}: {coeff} = {float(coeff):.8f}")
print()
print("  All coefficients are exact Fraction.")
print("  Master integral values: NOT PUBLIC (4800 digits, Laporta private)")
print("  Awaiting response from Prof. Laporta.")
print()

# Assessment
print("=" * 70)
print("DECOMPOSITION STATUS")
print("=" * 70)
print()
print("  A4 = T + V + W + E + U")
print()
print("  Component    | Content                         | Status")
print("  -------------|--------------------------------|------------------")
print("  T (wt 0-7)   | zeta, ln(2), Li_n(1/2)          | IN OUR BASIS")
print("  V            | H-polylogs at exp(i*pi/3)       | COMPUTABLE")
print("  W            | H-polylogs at exp(i*pi/2)       | COMPUTABLE")
print("  E            | Integrated K(x) products        | PARTIALLY COMPUTABLE")
print("  U            | 6 master integrals              | NOT PUBLIC")
print()
print("  Estimated split:")
print("    |T+V+W+E| / |A4| ~ 85%  (known analytical)")
print("    |U| / |A4| ~ 15%        (six masters)")
print()
print("  The framework handles T+V+W. E requires quadrature.")
print("  U requires the 4800-digit values from Laporta.")
print()
print("  MATH-2/MATH-3 basis now includes:")
print("    pi (999 digits), ln(2) (999 digits)")
print("    zeta(3), zeta(5), zeta(7), zeta(9) (100+ digits, Borwein)")
print("    Li_4(1/2) through Li_7(1/2) (150+ digits, direct series)")
print("    K(k), E(k) at k^2 = 1/4, 1/2, 3/4 (64-999 digits)")
print("    Total: ~30 integer-pair constants")
print()
print("  The PSLQ null on A4-as-a-whole is EXPECTED:")
print("    A4 is a SUM of terms from different transcendental classes.")
print("    The correct strategy is subtract T+V+W+E, then PSLQ on")
print("    the residual (= U) against the master integrals.")
print("    This requires either:")
print("      (a) The master integral values (from Laporta)")
print("      (b) The complete T+V+W+E expression (from the paper)")
