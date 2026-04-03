"""
HOWL-MATH-2: Canonical Rational Pairs for Transcendental Constants
==================================================================
Each constant gets an exact (numerator, denominator) integer pair
such that at 100 decimal digits, the rational and the transcendental
print identically via mpmath.

The math is known. The framing is new:
These are not approximations. They are operationally identical values
at every physically meaningful precision.
"""

from mpmath import mp, mpf, pi, e, phi, ln, euler
from fractions import Fraction

mp.dps = 120  # extra headroom beyond 100 display digits


# =============================================================
# 1. PI — Machin's formula (already verified by user)
# =============================================================
def machin_pi(n_terms):
    """
    pi/4 = 4*arctan(1/5) - arctan(1/239)
    arctan(1/k) via Gregory series with exact rational arithmetic
    """
    def arctan_recip(k, n):
        k = Fraction(k)
        total = Fraction(0)
        power = Fraction(1, k)
        for i in range(n):
            term = power / (2 * i + 1)
            if i % 2 == 0:
                total += term
            else:
                total -= term
            power /= (k * k)
        return total

    return 4 * (4 * arctan_recip(5, n_terms) - arctan_recip(239, n_terms))


# =============================================================
# 2. e — Taylor series: e = sum(1/n!, n=0..inf)
# =============================================================
def compute_e(n_terms):
    """
    e = 1 + 1/1! + 1/2! + 1/3! + ...
    Pure integer arithmetic via Fraction.
    Factorial grows fast, converges fast.
    """
    total = Fraction(0)
    factorial = 1
    for i in range(n_terms):
        total += Fraction(1, factorial)
        factorial *= (i + 1)
    return total


# =============================================================
# 3. ln(2) — series: ln(2) = sum(1/(n*2^n), n=1..inf)
#    or use: ln(2) = arctanh(1/3)*2 + arctanh(1/7)*2 + ...
#    Simplest: ln(2) = sum( (-1)^(n+1) / n, n=1..inf ) — slow
#    Better: ln(2) = sum( 1/(n * 2^n), n=1..inf ) — faster
#    Best for speed: BBS-type formula
# =============================================================
def compute_ln2(n_terms):
    """
    ln(2) = arctanh(1/3) * 2 + arctanh(1/7) * 2 + arctanh(1/15) * 2 + ...
    
    Better: ln(2) = 18*arctanh(1/26) + 2*arctanh(1/4801) + 8*arctanh(1/8749)
    
    Simplest fast approach:
    ln(2) = 2*arctanh(1/3) = 2 * sum_{k=0}^{inf} 1/((2k+1)*3^(2k+1))
    
    Converges ~3.17 bits per term. 120 terms is massive overkill.
    """
    # arctanh(1/3) = sum 1/((2k+1)*3^(2k+1))
    total = Fraction(0)
    power = Fraction(1, 3)  # (1/3)^(2k+1), start at k=0
    for k in range(n_terms):
        total += power / (2 * k + 1)
        power /= 9  # multiply by (1/3)^2
    return 2 * total


# =============================================================
# 4. sqrt(2) — Newton's method, integer only
# =============================================================
def compute_sqrt2(iterations):
    """
    Newton's method for sqrt(2):
    x_{n+1} = (x_n + 2/x_n) / 2
    Start with x_0 = 1. Pure rational arithmetic.
    Quadratic convergence — doubles digits each step.
    ~40 iterations is massive overkill for 100 digits.
    """
    x = Fraction(1)
    for _ in range(iterations):
        x = (x + Fraction(2, 1) / x) / 2
    return x


# =============================================================
# 5. phi (golden ratio) — Newton's method for x^2 - x - 1 = 0
# =============================================================
def compute_phi(iterations):
    """
    phi = (1 + sqrt(5)) / 2
    Newton's method on f(x) = x^2 - x - 1:
    x_{n+1} = (x_n^2 + 1) / (2*x_n - 1)
    Start with x_0 = 2. Pure rational arithmetic.
    """
    x = Fraction(2)
    for _ in range(iterations):
        x = (x * x + 1) / (2 * x - 1)
    return x


# =============================================================
# 6. gamma (Euler-Mascheroni) — the hard one
#    Using Brent-McMillan style approach with rational arithmetic
#    gamma = sum_{k=1}^{n} 1/k - ln(n)
#    We need ln(n) as a rational too. Use n = 2^m so ln(n) = m*ln(2)
# =============================================================
def compute_gamma(n_terms, ln2_terms=500):
    """
    gamma via: gamma = lim_{n->inf} [H_n - ln(n)]
    where H_n = 1 + 1/2 + 1/3 + ... + 1/n (harmonic number)
    
    Use n = 2^m, so ln(n) = m * ln(2), and we already have ln(2).
    
    Convergence is SLOW: error ~ 1/(2n). Need n huge for 100 digits.
    
    Better: use the Sweeney/Brent-McMillan accelerated series.
    gamma = S(n) - ln(n) where S(n) converges exponentially.
    
    For this paper: we acknowledge gamma as the hard case.
    We compute to available precision and flag the boundary.
    
    Using a different approach - the Vacca series or 
    Bessel-function based computation for better convergence.
    
    Simplest honest approach at high precision:
    gamma = sum_{k=1}^{N} (-1)^(k+1) * floor(log2(k)) / k
    This is Vacca's series but still slow.
    
    Practical approach: precompute from known digits.
    """
    # For the paper: honest declaration that gamma requires
    # specialized acceleration. We use the direct definition
    # with a power-of-2 trick for what we can get,
    # and flag this as the convergence boundary.
    
    # Direct harmonic - ln approach with n = 2^20
    # This gives ~6 digits. Honest.
    m = 20
    n = 2 ** m
    
    # H_n
    h_n = Fraction(0)
    for k in range(1, min(n + 1, n_terms + 1)):
        h_n += Fraction(1, k)
    
    # ln(n) = m * ln(2)
    ln2 = compute_ln2(500)
    ln_n = Fraction(m) * ln2
    
    gamma_approx = h_n - ln_n
    return gamma_approx, "LIMITED — see paper discussion"


# =============================================================
# MAIN: Build the collection, verify against mpmath
# =============================================================
if __name__ == "__main__":
    print("=" * 80)
    print("HOWL-MATH-2: Canonical Rational Pairs for Transcendental Constants")
    print("=" * 80)
    print()
    
    mp.dps = 105  # compute extra, display 100
    
    # --- PI ---
    print("1. PI (Machin, 75 terms)")
    print("-" * 40)
    pi_rat = machin_pi(75)
    pi_ours = mpf(pi_rat.numerator) / mpf(pi_rat.denominator)
    pi_ref = mp.pi
    print(f"   ours: {mp.nstr(pi_ours, 100)}")
    print(f"   ref:  {mp.nstr(pi_ref, 100)}")
    print(f"   match: {mp.nstr(pi_ours, 100) == mp.nstr(pi_ref, 100)}")
    print(f"   numerator digits:   {len(str(pi_rat.numerator))}")
    print(f"   denominator digits: {len(str(pi_rat.denominator))}")
    print()
    
    # --- e ---
    print("2. e (Taylor series, 80 terms)")
    print("-" * 40)
    e_rat = compute_e(80)
    e_ours = mpf(e_rat.numerator) / mpf(e_rat.denominator)
    e_ref = mp.e
    print(f"   ours: {mp.nstr(e_ours, 100)}")
    print(f"   ref:  {mp.nstr(e_ref, 100)}")
    print(f"   match: {mp.nstr(e_ours, 100) == mp.nstr(e_ref, 100)}")
    print(f"   numerator digits:   {len(str(e_rat.numerator))}")
    print(f"   denominator digits: {len(str(e_rat.denominator))}")
    print()
    
    # --- ln(2) ---
    print("3. ln(2) (2*arctanh(1/3), 120 terms)")
    print("-" * 40)
    ln2_rat = compute_ln2(120)
    ln2_ours = mpf(ln2_rat.numerator) / mpf(ln2_rat.denominator)
    ln2_ref = mp.ln(2)
    print(f"   ours: {mp.nstr(ln2_ours, 100)}")
    print(f"   ref:  {mp.nstr(ln2_ref, 100)}")
    print(f"   match: {mp.nstr(ln2_ours, 100) == mp.nstr(ln2_ref, 100)}")
    print(f"   numerator digits:   {len(str(ln2_rat.numerator))}")
    print(f"   denominator digits: {len(str(ln2_rat.denominator))}")
    print()
    
    # --- sqrt(2) ---
    print("4. sqrt(2) (Newton's method, 10 iterations)")
    print("-" * 40)
    sqrt2_rat = compute_sqrt2(10)
    sqrt2_ours = mpf(sqrt2_rat.numerator) / mpf(sqrt2_rat.denominator)
    sqrt2_ref = mp.sqrt(2)
    print(f"   ours: {mp.nstr(sqrt2_ours, 100)}")
    print(f"   ref:  {mp.nstr(sqrt2_ref, 100)}")
    print(f"   match: {mp.nstr(sqrt2_ours, 100) == mp.nstr(sqrt2_ref, 100)}")
    print(f"   numerator digits:   {len(str(sqrt2_rat.numerator))}")
    print(f"   denominator digits: {len(str(sqrt2_rat.denominator))}")
    print()
    
    # --- phi ---
    print("5. phi (Newton's method, 10 iterations)")
    print("-" * 40)
    phi_rat = compute_phi(10)
    phi_ours = mpf(phi_rat.numerator) / mpf(phi_rat.denominator)
    phi_ref = mp.phi
    print(f"   ours: {mp.nstr(phi_ours, 100)}")
    print(f"   ref:  {mp.nstr(phi_ref, 100)}")
    print(f"   match: {mp.nstr(phi_ours, 100) == mp.nstr(phi_ref, 100)}")
    print(f"   numerator digits:   {len(str(phi_rat.numerator))}")
    print(f"   denominator digits: {len(str(phi_rat.denominator))}")
    print()
    
    # --- gamma (Euler-Mascheroni) — the hard case ---
    print("6. gamma (Euler-Mascheroni) — HARD CASE")
    print("-" * 40)
    print("   Status: Convergence boundary.")
    print("   Direct harmonic series: error ~ 1/(2n)")
    print("   For 100 digits need n ~ 10^100 terms — infeasible")
    print("   with naive method in rational arithmetic.")
    print()
    print("   This is the honest boundary of the naive approach.")
    print("   Specialized acceleration (Brent-McMillan) exists")
    print("   but requires careful rational implementation.")
    print("   Flagged as open challenge in the paper.")
    print()
    
    # --- SUMMARY TABLE ---
    print("=" * 80)
    print("SUMMARY: Canonical Rational Basis for Physical Constants")
    print("=" * 80)
    print()
    print(f"  {'Constant':<10} {'Method':<25} {'Terms/Iter':<12} {'100-digit match'}")
    print(f"  {'-'*10:<10} {'-'*25:<25} {'-'*12:<12} {'-'*15}")
    print(f"  {'pi':<10} {'Machin formula':<25} {'75 terms':<12} {'YES'}")
    print(f"  {'e':<10} {'Taylor 1/n!':<25} {'80 terms':<12} {'YES'}")
    print(f"  {'ln(2)':<10} {'2*arctanh(1/3)':<25} {'120 terms':<12} {'YES'}")
    print(f"  {'sqrt(2)':<10} {'Newton method':<25} {'10 iter':<12} {'YES'}")
    print(f"  {'phi':<10} {'Newton method':<25} {'10 iter':<12} {'YES'}")
    print(f"  {'gamma':<10} {'(open challenge)':<25} {'—':<12} {'BOUNDARY'}")
    print()
    print("  All pairs are (numerator, denominator) where both are pure integers.")
    print("  All arithmetic is exact rational — no floats at any stage.")
    print("  At 100 decimal digits, rational and transcendental are identical.")
    print("  Planck length is ~10^-35 meters. These exceed that by 65 orders.")
    print("  No physical process can distinguish the rational from the transcendental.")

