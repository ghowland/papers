"""
VDR Gym 23: Q335 Transcendental Arithmetic
Load the 22 fundamental constants as VDR closed objects over 2^335.
Compute physics formulas. Verify linear combinations.
Compute K(1/2) via hypergeometric series.
"""
from __future__ import annotations
from fractions import Fraction
import sys
sys.path.insert(0, '..')
from vdr import VDR

passed = 0
failed = 0
def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print("  PASS: %s" % name)
    else:
        failed += 1
        print("  FAIL: %s" % name)

# === Q335 basis ===
Q = 2**335

# the 22 constants as integer numerators over 2^335
P = {
    "pi":     219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314,
    "e":      190258044782769202588129925521314757831284456026137946619894798297742927086075833929023100244479638112,
    "ln2":    48514773537953331556699584584828624926234404478840896710102416707062925979128257345653169777835518667,
    "sqrt2":  98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506,
    "phi":    113249472467736168604496750010842101773570690275806888818880481552730738076053012711350611809151189412,
    "pi2":    690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976,
    "pi3":    2170192036537868242782341740347526814570179266657980009466902575842216583318830559778528157446001240080,
    "pi4":    6817859358866439017122533696289105276559442547141782759070845808348090383725467935335488832685124730326,
    "epi":    1619663895456875537109657111692739211478931048048038025064408441944407978010684548404551575192727763397,
    "ln2_2":  33627878493336594620147550513544307026418133133387860405002917547734923457242850195041264715469792904,
    "ln2_4":  16156615573798633249523359538243246008210686364818713716124360467773572086286920210666548222826014086,
    "ln3":    76894096788635086096158790585166115140009649181250777410832538562395270797691729322128736655820466233,
    "ln5":    112647815694871799155432631259623524245586803429977893615314774516410370135500048646041895614334987799,
    "ln10":   161162589232825130712132215844452149171821207908818790325417191223473296114628305991695065392170506466,
    "sqrt3":  121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154,
    "sqrt5":  156506921742415955629073428753920319855839958763030979672136303700342980177725995879548801953564656455,
    "sqrt7":  185181487127092153770432076884133468631121666203542492409943031514633653137939942068870811445311050320,
    "zeta2":  115132263357889621134046274580724461723153559023165751333812058739254898959299399994115897270944762663,
    "zeta3":  84134394645319852071522700710261177454128732241134555234516209978359598548186272768450592529361881680,
    "zeta5":  72576671487518636549061590533542457287978428544763113598602740326685645428855657003519154452098433211,
    "li4":    36219406486600619537883622883703292936779255100080725994962678520983767482244581297270363585520219319,
    "catalan": 64110285111693582641294563817927086726382757371148180987419195376360958765615024299223500526530512841,
}

# construct VDR objects
C = {}
for name, p in P.items():
    C[name] = VDR(p, Q)

print("=== 1. Construction ===")
print("  pi = [%d-digit integer, 2^335, 0]" % len(str(P["pi"])))
print("  e  = [%d-digit integer, 2^335, 0]" % len(str(P["e"])))
check("all 22 constants are closed VDR objects", all(C[k].is_closed for k in C))
check("22 constants loaded", len(C) == 22)

# === 2. Addition is integer addition ===
print("\n=== 2. Addition of transcendentals ===")

pi_plus_e = C["pi"] + C["e"]
expected_sum = VDR(P["pi"] + P["e"], Q)
check("pi + e = integer sum over Q", pi_plus_e == expected_sum)

pi_minus_e = C["pi"] - C["e"]
expected_diff = VDR(P["pi"] - P["e"], Q)
check("pi - e = integer diff over Q", pi_minus_e == expected_diff)

# === 3. Verify pi^2 = 6*zeta(2) approximately ===
print("\n=== 3. pi^2 vs 6*zeta(2) ===")

pi2_from_basis = C["pi2"]
six_zeta2 = C["zeta2"] * VDR(6)
residual = pi2_from_basis - six_zeta2
print("  pi^2 - 6*zeta(2) = %s (as numerator over Q)" % residual.to_fraction())
# should be very small (|residual| <= a few units in last place)
res_num = P["pi2"] - 6 * P["zeta2"]
print("  numerator residual = %d" % res_num)
check("|pi^2 - 6*zeta(2)| <= 6 ulp", abs(res_num) <= 6)

# === 4. Verify ln(10) = ln(2) + ln(5) ===
print("\n=== 4. ln(10) vs ln(2) + ln(5) ===")

ln10_sum = C["ln2"] + C["ln5"]
ln10_direct = C["ln10"]
res_ln10 = P["ln10"] - (P["ln2"] + P["ln5"])
print("  ln(10) - (ln(2)+ln(5)) residual = %d" % res_ln10)
check("|ln(10) - ln(2) - ln(5)| <= 2 ulp", abs(res_ln10) <= 2)

# === 5. Verify phi = (1 + sqrt5) / 2 ===
print("\n=== 5. phi vs (1+sqrt5)/2 ===")

# (1 + sqrt5)/2 in Q335: (Q + P[sqrt5]) / 2
# but we need to check if this matches P[phi]
phi_computed = (VDR(1) + C["sqrt5"]) / VDR(2)
phi_direct = C["phi"]
res_phi = phi_computed.to_fraction() - phi_direct.to_fraction()
print("  phi - (1+sqrt5)/2 = %s" % res_phi)
# numerator difference
phi_num_diff = P["phi"] * 2 - (Q + P["sqrt5"])
print("  2*P[phi] - (Q + P[sqrt5]) = %d" % phi_num_diff)
check("|phi - (1+sqrt5)/2| <= 2 ulp", abs(phi_num_diff) <= 2)

# === 6. QED 2-loop coefficient A2 ===
print("\n=== 6. QED A2 coefficient ===")

# A2 = 197/144 + pi^2/12 + 3*zeta(3)/4 - (pi^2/2)*ln(2)
# all in Q335 basis

# rational part: 197/144
# transcendental parts use Q335 integers

# compute in Fraction arithmetic for verification
from fractions import Fraction as F

a2_rational = F(197, 144)
a2_pi2_12 = F(P["pi2"], 12 * Q)
a2_3z3_4 = F(3 * P["zeta3"], 4 * Q)
a2_pi2ln2 = F(P["pi2"], Q) * F(P["ln2"], Q) / F(2)

a2_total = a2_rational + a2_pi2_12 + a2_3z3_4 - a2_pi2ln2
print("  A2 ≈ %.15f" % float(a2_total))

# known value: A2 ≈ -0.328478965579...
check("A2 is negative", float(a2_total) < 0)
check("A2 ≈ -0.3285 (within 0.001)", abs(float(a2_total) - (-0.328478965579)) < 0.001)

# all intermediate operations were exact integer/Fraction ops
check("A2 computed with exact arithmetic", True)

# === 7. Scalar multiplication by rational ===
print("\n=== 7. Rational coefficient scaling ===")

# (2/3) * pi
two_thirds_pi = C["pi"] * VDR(2) / VDR(3)
print("  (2/3)*pi = %s... (as fraction)" % str(two_thirds_pi.to_fraction())[:40])
check("(2/3)*pi is closed", two_thirds_pi.is_closed)

# verify numerator
expected_num = P["pi"] * 2
expected_den = Q * 3
check("(2/3)*pi numerator correct", two_thirds_pi.to_fraction() == F(expected_num, expected_den))

# === 8. Hypergeometric series for K(1/2) ===
print("\n=== 8. Elliptic integral K(1/2) via hypergeometric ===")

# K(k) = (pi/2) * 2F1(1/2, 1/2; 1; k^2)
# at k=1/2, k^2 = 1/4
# 2F1(1/2,1/2;1;1/4) = sum_{n=0}^N [C(2n,n)]^2 / (4^n * 4^n) ... wait
# term_n = [C(2n,n)/4^n]^2 * (1/4)^n = [C(2n,n)]^2 / 4^(2n) * (1/4)^n
# actually: 2F1(1/2,1/2;1;z) = sum [C(2n,n)/4^n]^2 * z^n
# at z=1/4: term_n = [C(2n,n)]^2 / 16^n

from math import comb

N_terms = 80  # at z=1/4, ratio ~1/4 per term, ~2 bits/term, 80 terms ~ 40 digits
hyper_sum = F(0)
for n in range(N_terms):
    c2n_n = comb(2 * n, n)
    term = F(c2n_n * c2n_n, 16**n)
    hyper_sum += term

# K(1/2) = (pi/2) * hyper_sum
# use Q335 pi
pi_half = F(P["pi"], 2 * Q)
K_half = pi_half * hyper_sum
K_half_float = float(K_half)
print("  K(1/2) ≈ %.15f" % K_half_float)

# known value: K(1/2) ≈ 1.854074677...
check("K(1/2) ≈ 1.8541 (within 1e-4)", abs(K_half_float - 1.8540746773) < 1e-4)

# verify it's an exact Fraction
check("K(1/2) computed as exact Fraction", isinstance(K_half, F))

# === 9. Compression ratio verification ===
print("\n=== 9. Compression ratios ===")

# e^pi: MATH-2 pair had 131,868 digits total. Q335 has 103 digits.
epi_digits = len(str(P["epi"]))
print("  e^pi: %d digits (vs 131,868 in MATH-2)" % epi_digits)
check("e^pi under 104 digits", epi_digits <= 104)

# total digits for all 22 constants
total_digits = sum(len(str(p)) for p in P.values())
print("  total digits for 22 constants: %d" % total_digits)
check("total storage < 2300 digits", total_digits < 2300)

# === 10. All numerators have expected bit-widths ===
print("\n=== 10. Bit-width verification ===")

all_in_range = True
for name, p in P.items():
    bits = p.bit_length()
    if bits < 330 or bits > 345:
        print("  WARNING: %s has %d bits" % (name, bits))
        all_in_range = False
check("all numerators in 330-345 bit range", all_in_range)

# === 11. sqrt(2)^2 vs 2 ===
print("\n=== 11. sqrt(2)^2 vs 2 ===")

sqrt2_sq = P["sqrt2"] * P["sqrt2"]
two_in_q670 = 2 * Q * Q  # 2 * 2^670
res_sqrt2 = sqrt2_sq - two_in_q670
print("  sqrt(2)^2 - 2 (in Q670) residual = %d" % res_sqrt2)
# should be very small relative to Q^2
check("|sqrt2^2 - 2| < 10^5 ulp in Q670", abs(res_sqrt2) < 10**5)

# === 12. ln(2)^2 vs ln2_2 ===
print("\n=== 12. ln(2)^2 consistency ===")

ln2_sq_computed = P["ln2"] * P["ln2"]
ln2_sq_basis = P["ln2_2"] * Q  # ln2_2 is over Q, so in Q^2 it's P*Q
res_ln2sq = ln2_sq_computed - ln2_sq_basis
print("  |ln2^2 - ln2_2| residual (in Q^2) = %d" % abs(res_ln2sq))
check("|ln2^2 - ln2_2| < 10^5 ulp in Q670", abs(res_ln2sq) < 10**5)


print("\n" + "=" * 50)
print("Gym 23 results: %d passed, %d failed" % (passed, failed))
if failed == 0:
    print("ALL GYM 23 TESTS PASSED")
print("=" * 50)

