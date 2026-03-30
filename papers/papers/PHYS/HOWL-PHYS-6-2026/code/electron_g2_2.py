"""
The Electron Anomalous Magnetic Moment from Integer Arithmetic

a_e = (g-2)/2 = sum_n A_n * (alpha/pi)^n

A1 = 1/2                              (Schwinger 1948, exact)
A2 = 197/144 + pi^2/12 + 3*zeta(3)/4  (Petermann/Sommerfield 1957, exact)
     - (pi^2/2)*ln(2)
A3 = [see below]                       (Laporta/Remiddi 1996, exact)
A4 = -1.91224576492644...              (Laporta 2017, 1100 digits)
A5 = 6.678(192) or 5.891(61)          (AHKN 2018 / Volkov 2024, 5σ tension)

A1 through A3: every coefficient is a rational times a MATH-2 integer pair.
A4: imported as a rational at 30-digit precision.
A5: imported as a rational at 4-digit precision.

Alpha: from CODATA 2022, alpha^-1 = 137.035999177
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120


# ================================================================
# Integer pairs for transcendentals (MATH-2)
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
        n = 2 * k + 1
        result += power / n
        power *= x_sq
    return result

def rational_ln2(terms=160):
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def rational_zeta3(n_terms=180):
    """ζ(3) via central binomial series: ζ(3) = 5/2 * Σ (-1)^(k-1)/(k³·C(2k,k))"""
    total = Fraction(0)
    for k in range(1, n_terms + 1):
        cbc = Fraction(1)
        for j in range(1, k + 1):
            cbc = cbc * (k + j) / j
        sign = (-1) ** (k - 1)
        total += Fraction(sign) / (k * k * k * cbc)
    return Fraction(5, 2) * total

def rational_zeta5(n_terms=10000):
    """ζ(5) via direct alternating eta series + relation η(5) = 15/16·ζ(5).
    η(5) = Σ (-1)^(n-1)/n^5. After N terms, error ~ 1/(N+1)^5.
    10000 terms gives 20 correct digits — sufficient for 12-digit a_e."""
    eta5 = Fraction(0)
    for n in range(1, n_terms + 1):
        eta5 += Fraction((-1)**(n-1), n**5)
    return Fraction(16, 15) * eta5

def rational_Li4_half(n_terms=300):
    """Li₄(1/2) = Σ_{n=1}^∞ 1/(2^n · n⁴). Converges geometrically."""
    total = Fraction(0)
    power_of_2 = Fraction(1, 2)
    for n in range(1, n_terms + 1):
        total += power_of_2 / (n * n * n * n)
        power_of_2 /= 2
    return total


# ================================================================
# Compute all transcendentals
# ================================================================

print("Computing transcendentals as integer pairs...")
print()

pi_rat = rational_pi(160)
pi2 = pi_rat * pi_rat
pi4 = pi2 * pi2
ln2 = rational_ln2(160)
ln2_2 = ln2 * ln2
ln2_4 = ln2_2 * ln2_2

print(f"  pi:     {pi_rat.numerator.bit_length()} bits")
print(f"  ln(2):  {ln2.numerator.bit_length()} bits")

print("  Computing zeta(3)...")
zeta3 = rational_zeta3(180)
print(f"  zeta(3): {zeta3.numerator.bit_length()} bits")

print("  Computing zeta(5) (10000 terms)...")
zeta5 = rational_zeta5(10000)
print(f"  zeta(5): {zeta5.numerator.bit_length()} bits")

print("  Computing Li4(1/2)...")
a4_li4 = rational_Li4_half(300)
print(f"  Li4(1/2): {a4_li4.numerator.bit_length()} bits")
print()

# Verify against mpmath
print("Verifying transcendentals...")
checks = [
    ("pi", pi_rat, mp.pi),
    ("ln(2)", ln2, mp.ln(2)),
    ("zeta(3)", zeta3, mp.zeta(3)),
    ("zeta(5)", zeta5, mp.zeta(5)),
    ("Li4(1/2)", a4_li4, mp.polylog(4, mpf(1)/2)),
]

for name, rat_val, ref_val in checks:
    our = mpf(rat_val.numerator) / mpf(rat_val.denominator)
    diff = abs(our - ref_val)
    digits = -int(mp.log10(diff)) if diff > 0 else 999
    print(f"  {name:<10}: {digits} correct digits")
print()


# ================================================================
# Compute the QED coefficients A1, A2, A3 in integer arithmetic
# ================================================================

print("=" * 70)
print("QED COEFFICIENTS IN INTEGER ARITHMETIC")
print("=" * 70)
print()

# A1 = 1/2 (Schwinger 1948)
A1 = Fraction(1, 2)
print(f"A1 = {A1} = {float(A1)}")
print()

# A2 = 197/144 + zeta(2)/2 + 3*zeta(3)/4 - 3*zeta(2)*ln(2)
# where zeta(2) = pi^2/6
# = 197/144 + pi^2/12 + 3*zeta(3)/4 - (pi^2/2)*ln(2)
A2 = (Fraction(197, 144) 
      + pi2 / 12 
      + Fraction(3, 4) * zeta3 
      - pi2 * ln2 / 2)

A2_check = mpf(A2.numerator) / mpf(A2.denominator)
print(f"A2 = 197/144 + pi^2/12 + 3*zeta(3)/4 - (pi^2/2)*ln(2)")
print(f"   = {mp.nstr(A2_check, 30)}")
print(f"   Expected: -0.328478965579193...")
print()

# A3 (Laporta & Remiddi 1996)
# = 83/72*pi^2*zeta(3) - 215/24*zeta(5) 
#   + 100/3*(Li4(1/2) + ln(2)^4/24 - pi^2*ln(2)^2/24)
#   - 239/2160*pi^4 + 139/18*zeta(3) 
#   - 298/9*pi^2*ln(2) + 17101/810*pi^2 + 28259/5184
A3 = (Fraction(83, 72) * pi2 * zeta3
      - Fraction(215, 24) * zeta5
      + Fraction(100, 3) * (a4_li4 + ln2_4 / 24 - pi2 * ln2_2 / 24)
      - Fraction(239, 2160) * pi4
      + Fraction(139, 18) * zeta3
      - Fraction(298, 9) * pi2 * ln2
      + Fraction(17101, 810) * pi2
      + Fraction(28259, 5184))

A3_check = mpf(A3.numerator) / mpf(A3.denominator)
print(f"A3 = 83/72*pi^2*zeta(3) - 215/24*zeta(5) + ...")
print(f"   = {mp.nstr(A3_check, 30)}")
print(f"   Expected: 1.18124145658720...")
print()


# ================================================================
# A4 and A5: numerical inputs as rationals
# ================================================================

# A4 (Laporta 2017, 1100 digits — use first 30 for rational)
# A4 = -1.912245764926445574152647167439830054...
# As rational at 30 digits: 
A4 = Fraction(-1912245764926445574152647167440, 10**30)
A4_check = mpf(A4.numerator) / mpf(A4.denominator)
print(f"A4 = {mp.nstr(A4_check, 30)}  (Laporta 2017, 30-digit rational)")
print(f"   Expected: -1.91224576492644557415264...")
print()

# A5: TWO VALUES (5σ tension)
# AHKN 2018: 6.678 ± 0.192
# Volkov 2024: 5.891 ± 0.061
A5_AHKN = Fraction(6678, 1000)
A5_Volkov = Fraction(5891, 1000)
print(f"A5 (AHKN 2018):   {float(A5_AHKN)} ± 0.192")
print(f"A5 (Volkov 2024): {float(A5_Volkov)} ± 0.061")
print(f"Discrepancy: 5 sigma — active controversy")
print()


# ================================================================
# Alpha as measured rational
# ================================================================

# CODATA 2022: alpha^-1 = 137.035999177(21)
alpha_inv = Fraction(137035999177, 1000000000)
alpha = Fraction(1) / alpha_inv
alpha_over_pi = alpha / pi_rat

print(f"alpha^-1 = {float(alpha_inv)}")
print(f"alpha/pi = {float(alpha_over_pi):.15e}")
print()


# ================================================================
# Compute a_e = sum A_n * (alpha/pi)^n
# ================================================================

print("=" * 70)
print("COMPUTING a_e = (g-2)/2")
print("=" * 70)
print()

ap = alpha_over_pi
ap2 = ap * ap
ap3 = ap2 * ap
ap4 = ap3 * ap
ap5 = ap4 * ap

# Individual contributions
term1 = A1 * ap
term2 = A2 * ap2
term3 = A3 * ap3
term4 = A4 * ap4
term5_AHKN = A5_AHKN * ap5
term5_Volkov = A5_Volkov * ap5

a_e_3loop = term1 + term2 + term3
a_e_4loop = a_e_3loop + term4
a_e_5loop_AHKN = a_e_4loop + term5_AHKN
a_e_5loop_Volkov = a_e_4loop + term5_Volkov

print(f"Individual contributions:")
print(f"  1-loop: A1*(α/π)¹ = {float(term1):.15e}")
print(f"  2-loop: A2*(α/π)² = {float(term2):.15e}")
print(f"  3-loop: A3*(α/π)³ = {float(term3):.15e}")
print(f"  4-loop: A4*(α/π)⁴ = {float(term4):.15e}")
print(f"  5-loop (AHKN):     = {float(term5_AHKN):.15e}")
print(f"  5-loop (Volkov):   = {float(term5_Volkov):.15e}")
print()

print(f"Cumulative:")
print(f"  Through 3-loop:      {float(a_e_3loop):.15e}")
print(f"  Through 4-loop:      {float(a_e_4loop):.15e}")
print(f"  Through 5-loop (AK): {float(a_e_5loop_AHKN):.15e}")
print(f"  Through 5-loop (V):  {float(a_e_5loop_Volkov):.15e}")
print()


# ================================================================
# Compare to experiment
# ================================================================

# Experimental value (Fan et al. 2023, Northwestern):
# a_e(exp) = 1 159 652 180.59(13) × 10^{-12}
a_e_exp = Fraction(115965218059, 10**14)  # in natural units: 0.00115965218059

print("=" * 70)
print("COMPARISON TO EXPERIMENT")
print("=" * 70)
print()

# Convert to units of 10^{-12} for comparison
scale = mpf(10)**12

a_e_3loop_mp = mpf(a_e_3loop.numerator) / mpf(a_e_3loop.denominator)
a_e_4loop_mp = mpf(a_e_4loop.numerator) / mpf(a_e_4loop.denominator)
a_e_5loop_AHKN_mp = mpf(a_e_5loop_AHKN.numerator) / mpf(a_e_5loop_AHKN.denominator)
a_e_5loop_Volkov_mp = mpf(a_e_5loop_Volkov.numerator) / mpf(a_e_5loop_Volkov.denominator)
a_e_exp_mp = mpf('0.00115965218059')

print(f"{'Result':<25} {'a_e × 10¹²':>22} {'Diff from exp × 10¹²':>22}")
print("-" * 70)
print(f"{'Experiment':25} {mp.nstr(a_e_exp_mp * scale, 15):>22}")
print(f"{'3-loop (integer)':25} {mp.nstr(a_e_3loop_mp * scale, 15):>22} "
      f"{mp.nstr((a_e_3loop_mp - a_e_exp_mp) * scale, 8):>22}")
print(f"{'4-loop':25} {mp.nstr(a_e_4loop_mp * scale, 15):>22} "
      f"{mp.nstr((a_e_4loop_mp - a_e_exp_mp) * scale, 8):>22}")
print(f"{'5-loop (AHKN)':25} {mp.nstr(a_e_5loop_AHKN_mp * scale, 15):>22} "
      f"{mp.nstr((a_e_5loop_AHKN_mp - a_e_exp_mp) * scale, 8):>22}")
print(f"{'5-loop (Volkov)':25} {mp.nstr(a_e_5loop_Volkov_mp * scale, 15):>22} "
      f"{mp.nstr((a_e_5loop_Volkov_mp - a_e_exp_mp) * scale, 8):>22}")
print()

# Note: we have NOT included:
# - Mass-dependent QED corrections (muon and tau loops)
# - Electroweak corrections
# - Hadronic corrections
# These are all small but contribute at the level of ~1-2 × 10^{-12}

print("NOTE: This computation includes only the mass-independent QED terms.")
print("Missing contributions (all small):")
print(f"  Mass-dependent QED (mu/tau loops): ~{5.2e-7 * float(ap2) * 1e12:.2f} × 10⁻¹²")
print(f"  Electroweak corrections:           ~0.030 × 10⁻¹²")
print(f"  Hadronic VP + light-by-light:      ~1.7 × 10⁻¹²")
print(f"  Total missing:                     ~1.7 × 10⁻¹²")
print()


# ================================================================
# Proof of integer arithmetic
# ================================================================

print("=" * 70)
print("PROOF OF INTEGER ARITHMETIC")
print("=" * 70)
print()

print(f"A1: {type(A1).__name__}")
print(f"A2: {type(A2).__name__}, numerator {A2.numerator.bit_length()} bits")
print(f"A3: {type(A3).__name__}, numerator {A3.numerator.bit_length()} bits")
print(f"A4: {type(A4).__name__} (30-digit rational input)")
print(f"A5: {type(A5_AHKN).__name__} (4-digit rational input)")
print(f"alpha/pi: {type(alpha_over_pi).__name__}")
print(f"a_e (4-loop): {type(a_e_4loop).__name__}, numerator {a_e_4loop.numerator.bit_length()} bits")
print()
print("All components are Fraction. No float in computation.")
print()


# ================================================================
# What is integer, what is measured
# ================================================================

print("=" * 70)
print("WHAT IS INTEGER, WHAT IS MEASURED")
print("=" * 70)
print()
print("EXACT INTEGER ARITHMETIC (A1, A2, A3):")
print(f"  A1 = 1/2")
print(f"  A2 = 197/144 + pi^2/12 + 3*zeta(3)/4 - (pi^2/2)*ln(2)")
print(f"     Every coefficient rational, every transcendental a MATH-2 pair")
print(f"  A3 = 83/72*pi^2*zeta(3) - 215/24*zeta(5) + ... + 28259/5184")
print(f"     10 terms, every coefficient rational, transcendentals:")
print(f"     pi, zeta(3), zeta(5), ln(2), Li4(1/2) — all MATH-2 pairs")
print()
print("NUMERICAL RATIONALS (A4, A5):")
print(f"  A4 = -1912245764926445574152647167440 / 10^30")
print(f"     (Laporta 2017, from 1100-digit numerical evaluation)")
print(f"     Semi-analytical fit exists but involves elliptic integrals")
print(f"  A5 = 6678/1000 (AHKN) or 5891/1000 (Volkov)")
print(f"     (5σ discrepancy between groups — active controversy)")
print()
print("MEASURED:")
print(f"  alpha^-1 = {alpha_inv}")
print(f"  a_e(exp) = 0.00115965218059(13)")
print()
print("STRUCTURAL FINDING:")
print(f"  Through 3 loops, every QED coefficient is a rational combination")
print(f"  of five transcendentals: pi, ln(2), zeta(3), zeta(5), Li4(1/2).")
print(f"  All five are MATH-2 integer pairs. The first three orders of")
print(f"  the most precisely tested prediction in physics are integers.")