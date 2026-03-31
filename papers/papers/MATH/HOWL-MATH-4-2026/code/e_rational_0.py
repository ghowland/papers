from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120

# e as a MATH-2 integer pair
def compute_e(n_terms=80):
    total = Fraction(0)
    factorial = 1
    for i in range(n_terms):
        total += Fraction(1, factorial)
        factorial *= (i + 1)
    return total

e_rat = compute_e(80)
e_mp = mpf(e_rat.numerator) / mpf(e_rat.denominator)

print("=" * 65)
print("RATIONAL APPROXIMATIONS TO e")
print("=" * 65)
print()
print(f"e = {mp.nstr(e_mp, 50)}")
print()

# First: verify 87/32
r = Fraction(87, 32)
diff = float(r) - float(e_rat)
print(f"87/32 = {float(r):.10f}")
print(f"e     = {float(e_rat):.10f}")
print(f"diff  = {diff:+.10f} ({abs(diff)/float(e_rat)*100:.4f}%)")
print(f"87 = 3 * 29, 32 = 2^5")
print()

# What's the BEST rational with denominator 32?
# e * 32 = 86.985... so floor = 86, ceil = 87
# 87/32 is the nearest fraction with denom 32
print("Best rational with denominator 2^n:")
for n in range(1, 20):
    d = 2**n
    p = round(float(e_rat) * d)
    r = Fraction(p, d)
    # Reduce
    r_red = Fraction(p, d)  # auto-reduces
    diff = float(r) - float(e_rat)
    ppm = abs(diff) / float(e_rat) * 1e6
    print(f"  2^{n:>2} = {d:>8}: {p}/{d} = {r_red} = {float(r):.15f}  "
          f"diff={diff:+.2e} ({ppm:.2f} ppm)")

print()

# Convergents of the continued fraction of e
# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
# The CF of e has the famous pattern [2; 1, 2k, 1] for k=1,2,3,...
print("=" * 65)
print("CONTINUED FRACTION CONVERGENTS OF e")
print("=" * 65)
print()

# Compute CF coefficients of e
def cf_coefficients(x, n_terms=30):
    """Extract continued fraction coefficients from a Fraction."""
    coeffs = []
    for _ in range(n_terms):
        a = int(x)
        coeffs.append(a)
        x = x - a
        if x == 0:
            break
        x = Fraction(1) / x
    return coeffs

cf = cf_coefficients(e_rat, 40)
print(f"CF coefficients: {cf[:30]}")
print()

# The pattern: [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, ...]
# Every third coefficient (positions 2, 5, 8, 11, ...) is 2k for k=1,2,3,...
# All others are 1 (except the initial 2)

# Compute convergents
def convergents(coeffs):
    """Compute convergents p_n/q_n from CF coefficients."""
    p_prev, p_curr = 1, coeffs[0]
    q_prev, q_curr = 0, 1
    results = [(p_curr, q_curr)]
    for i in range(1, len(coeffs)):
        p_new = coeffs[i] * p_curr + p_prev
        q_new = coeffs[i] * q_curr + q_prev
        results.append((p_new, q_new))
        p_prev, p_curr = p_curr, p_new
        q_prev, q_curr = q_curr, q_new
    return results

convs = convergents(cf[:25])

print(f"{'n':>3} {'p':>15} {'q':>15} {'p/q':>20} {'error':>15} {'ppm':>12} {'CF coeff':>10}")
print("-" * 95)
for i, (p, q) in enumerate(convs):
    r = Fraction(p, q)
    diff = float(r) - float(e_rat)
    ppm = abs(diff) / float(e_rat) * 1e6
    cf_c = cf[i] if i < len(cf) else ''
    print(f"{i:>3} {p:>15} {q:>15} {float(r):>20.15f} {diff:>+15.2e} {ppm:>12.4f} {cf_c:>10}")

print()

# Where does 87/32 sit relative to the convergents?
print("=" * 65)
print("WHERE IS 87/32?")
print("=" * 65)
print()

r87 = Fraction(87, 32)
diff87 = abs(float(r87) - float(e_rat))
print(f"87/32: error = {diff87:.2e}, ppm = {diff87/float(e_rat)*1e6:.2f}")
print()
print("Convergents with similar or better precision:")
for i, (p, q) in enumerate(convs):
    r = Fraction(p, q)
    diff = abs(float(r) - float(e_rat))
    if diff < diff87 * 2:
        print(f"  [{i}] {p}/{q} (error {diff:.2e}, q = {q})")

print()

# Is 87/32 a semiconvergent or best rational approximation?
# Best rational: no fraction with smaller or equal denominator is closer
print("Best rationals with q <= 32:")
best = None
for q in range(1, 33):
    for p in range(2*q, 3*q+1):
        r = Fraction(p, q)
        diff = abs(float(r) - float(e_rat))
        if best is None or diff < best[2]:
            best = (p, q, diff)
            
print(f"  Best: {best[0]}/{best[1]} = {float(Fraction(best[0],best[1])):.10f}, error = {best[2]:.2e}")
print(f"  87/32 error = {diff87:.2e}")
print(f"  87/32 is {'THE' if best[0]==87 and best[1]==32 else 'NOT the'} best rational with q <= 32")
print()

# Power-of-2 denominators specifically
print("=" * 65)
print("POWER-OF-2 DENOMINATORS: PATTERN?")
print("=" * 65)
print()

print(f"{'2^n':>6} {'p':>20} {'p/2^n':>25} {'error ppm':>12} {'p factored':>30}")

def factor(n):
    if n <= 1: return str(n)
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return ' * '.join(str(f) for f in factors)

for n in range(1, 40):
    d = 2**n
    p = round(float(e_rat) * d)
    r = Fraction(p, d)
    diff = abs(float(r) - float(e_rat))
    ppm = diff / float(e_rat) * 1e6
    # Only show if ppm < 100 or n <= 10
    if ppm < 50 or n <= 10:
        print(f"  2^{n:>2} {p:>20} {float(r):>25.18f} {ppm:>12.4f}   {factor(p)}")
        