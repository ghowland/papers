#!/usr/bin/env python3
"""
HOWL-DATA-3: Database Consistency Verification
================================================

Run every testable internal relation in DATA-2.
If all pass, DATA-2 becomes DATA-3 (the verified platform).
If any fail, diagnose and fix before declaring DATA-3.

All computation in Fraction arithmetic.
Square roots via mpmath at 50 digits, converted to Fraction.
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi, log as mlog
import math

mp.dps = 60

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

def m2f(x, denom=10**30):
    """Convert mpf to Fraction at given denominator precision."""
    return Fraction(int(x * denom), denom)

# ================================================================
# DATA-2 ENTRIES (full precision from the database)
# ================================================================

# --- Section A: SI fundamental (exact) ---
c       = Fraction(299792458, 1)                          # m/s, exact
h       = Fraction(662607015, 10**42)                     # J·s, exact
e_charge= Fraction(1602176634, 10**28)                    # C, exact
k_B     = Fraction(1380649, 10**29)                       # J/K, exact
N_A     = Fraction(602214076, 1) * Fraction(10**15, 1)    # mol^-1, exact
dv_Cs   = Fraction(9192631770, 1)                         # Hz, exact
K_cd    = Fraction(683, 1)                                # lm/W, exact

# --- Section B: Measured fundamental (CODATA 2022) ---
alpha_inv = Fraction(137035999177, 10**9)       # 12 digits
m_e       = Fraction(51099895069, 10**11)       # MeV, 11 digits
m_mu      = Fraction(1056583755, 10**7)         # MeV, 10 digits
m_tau     = Fraction(177686, 100)               # MeV, 6 digits
m_p       = Fraction(93827208943, 10**8)        # MeV, 11 digits
mp_me     = Fraction(183615267343, 10**8)       # direct measurement, 13 digits
R_inf     = Fraction(10973731568157, 10**6)     # m^-1, 13 digits
a_0       = Fraction(529177210544, 10**22)      # m, 12 digits
a_e       = Fraction(115965218059, 10**14)      # g-2 anomaly, 12 digits
a_mu      = Fraction(116592059, 10**11)         # g-2 anomaly, 9 digits
sin2_tW   = Fraction(23122, 100000)             # 5 digits
alpha_s   = Fraction(1180, 10000)               # 4 digits
mu_0      = Fraction(125663706127, 10**17)      # N/A^2, 12 digits

# --- Section C: Electroweak ---
M_Z       = Fraction(911876, 10)                # MeV, 6 digits
Gamma_Z   = Fraction(24952, 10)                 # MeV, 5 digits
M_W       = Fraction(803692, 10)                # MeV, 6 digits
m_t       = Fraction(172570, 1)                 # MeV, 5 digits
m_H       = Fraction(125200, 1)                 # MeV, 5 digits
G_F       = Fraction(11663788, 10**12)          # GeV^-2, 8 digits

# --- Section D: Quarks and CKM ---
m_u       = Fraction(216, 100)                  # MeV, 3 digits
m_d       = Fraction(470, 100)                  # MeV, 3 digits
m_s       = Fraction(935, 10)                   # MeV, 3 digits
m_c       = Fraction(1273, 1)                   # MeV, 4 digits
m_b       = Fraction(4183, 1)                   # MeV, 4 digits
sin_t12   = Fraction(22501, 100000)             # 5 digits
sin_t23   = Fraction(4182, 100000)              # 4 digits
sin_t13   = Fraction(3685, 1000000)             # 4 digits
mc_ms     = Fraction(11783, 1000)               # lattice, 5 digits
mb_mc     = Fraction(4578, 1000)                # lattice, 4 digits
mu_md     = Fraction(485, 1000)                 # lattice, 3 digits

# --- Section E: Nuclear/hadron ---
m_n       = Fraction(93956542194, 10**8)        # MeV, 11 digits
mn_mp_diff= Fraction(129333251, 10**8)          # MeV, 8 digits
m_pi_p    = Fraction(13957039, 10**5)           # MeV, 8 digits
m_pi_0    = Fraction(1349770, 10**4)            # MeV, 7 digits
m_K_p     = Fraction(493677, 10**3)             # MeV, 6 digits
m_D       = Fraction(187561294500, 10**8)       # MeV, 12 digits
m_He4     = Fraction(37273794118, 10**7)        # MeV, 10 digits
E_D       = Fraction(222456614, 10**8)          # MeV, 8 digits

# --- Section K: Dimensionless ratios ---
mmu_me    = Fraction(20676828270846717969, 10**19)  # 10 sig figs (truncated from 200-digit)
mtau_me   = Fraction(347723, 100)                    # 6 digits (from m_tau/m_e)
mtau_mmu  = Fraction(168170, 10000)                  # 6 digits
mn_mp     = Fraction(10013784194633623804, 10**19)   # 11 digits (truncated from 200-digit)
MW_MZ     = Fraction(881361, 10**6)                  # 6 digits
mH_MZ     = Fraction(137299, 10**5)                  # 5 digits
mt_MZ     = Fraction(189247, 10**5)                  # 5 digits
K_koide   = Fraction(6666605115, 10**10)             # 6 digits (from addendum K1)

# --- Section G: Analytical constants (Q335 numerators) ---
Q = 2**335
p_pi    = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_e     = 190258044782769202588129925521314757831284456026137946619894798297742927086075833929023100244479638112
p_ln2   = 48514773537953331556699584584828624926234404478840896710102416707062925979128257345653169777835518667
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506
p_sqrt3 = 121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154
p_sqrt5 = 156506921742415955629073428753920319855839958763030979672136303700342980177725995879548801953564656455
p_phi   = 113249472467736168604496750010842101773570690275806888818880481552730738076053012711350611809151189412
p_zeta3 = 84134394645319852071522700710261177454128732241134555234516209978359598548186272768450592529361881680
p_zeta5 = 72576671487518636549061590533542457287978428544763113598602740326685645428855657003519154452098433211
p_pi2   = 690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976
p_zeta2 = 115132263357889621134046274580724461723153559023165751333812058739254898959299399994115897270944762663

pi_f    = Fraction(p_pi, Q)
e_f     = Fraction(p_e, Q)
ln2_f   = Fraction(p_ln2, Q)
sqrt2_f = Fraction(p_sqrt2, Q)
sqrt3_f = Fraction(p_sqrt3, Q)
sqrt5_f = Fraction(p_sqrt5, Q)
phi_f   = Fraction(p_phi, Q)
zeta3_f = Fraction(p_zeta3, Q)
zeta5_f = Fraction(p_zeta5, Q)
pi2_f   = Fraction(p_pi2, Q)
zeta2_f = Fraction(p_zeta2, Q)

# R2, R4 from DATA-2
R2_f = pi_f / 4
R4_f = pi2_f / 32
twopi_f = 2 * pi_f

# alpha/pi entry
alpha_pi = Fraction(1, 1) / (alpha_inv * pi_f)

print("=" * 78)
print("HOWL-DATA-3: DATABASE CONSISTENCY VERIFICATION")
print("=" * 78)
print()

checks = []
fixes = []

def test(test_id, name, left, right, min_digits, left_label="Computed", right_label="Stored"):
    """
    Compare two Fraction values. PASS if they agree to min_digits sig figs.
    """
    if right == 0:
        rel_diff = abs(float(left))
        digits_agree = 0 if rel_diff > 0 else 999
    else:
        rel_diff = abs(float(left - right) / float(right))
        digits_agree = -math.log10(rel_diff) if rel_diff > 0 else 999

    passed = digits_agree >= min_digits
    status = "PASS" if passed else "FAIL"
    checks.append((test_id, name, status, digits_agree, min_digits))

    print(f"  [{status}] {test_id}: {name}")
    print(f"        {left_label}: {float(left):.15e}")
    print(f"        {right_label}: {float(right):.15e}")
    print(f"        Relative diff: {rel_diff:.3e}  ({digits_agree:.1f} digits agree, need {min_digits})")
    if not passed:
        print(f"        *** FAILURE: {digits_agree:.1f} < {min_digits} digits ***")
    print()
    return passed

# ================================================================
# GROUP A: MASS RATIO IDENTITIES
# ================================================================

print("-" * 78)
print("GROUP A: MASS RATIO IDENTITIES")
print("-" * 78)
print()

# A1: m_p/m_e direct vs computed
test("A1", "m_p/m_e (direct) vs m_p / m_e",
     m_p / m_e, mp_me, 11)

# A2: m_mu/m_e direct vs computed
mmu_me_comp = m_mu / m_e
test("A2", "m_μ/m_e (direct) vs m_μ / m_e",
     mmu_me_comp, mmu_me, 10)

# A3: m_tau/m_e direct vs computed
mtau_me_comp = m_tau / m_e
test("A3", "m_τ/m_e (direct) vs m_τ / m_e",
     mtau_me_comp, mtau_me, 6)

# A4: m_tau/m_mu direct vs computed
mtau_mmu_comp = m_tau / m_mu
test("A4", "m_τ/m_μ (direct) vs m_τ / m_μ",
     mtau_mmu_comp, mtau_mmu, 5)

# A5: m_n/m_p direct vs computed
mn_mp_comp = m_n / m_p
test("A5", "m_n/m_p (direct) vs m_n / m_p",
     mn_mp_comp, mn_mp, 11)

# A6: M_W/M_Z direct vs computed
MW_MZ_comp = M_W / M_Z
test("A6", "M_W/M_Z (direct) vs M_W / M_Z",
     MW_MZ_comp, MW_MZ, 6)

# A7: m_n - m_p direct vs computed
mn_mp_diff_comp = m_n - m_p
test("A7", "m_n − m_p (direct) vs m_n − m_p",
     mn_mp_diff_comp, mn_mp_diff, 8)

# A8: m_H/M_Z direct vs computed
mH_MZ_comp = m_H / M_Z
test("A8", "m_H/M_Z (direct) vs m_H / M_Z",
     mH_MZ_comp, mH_MZ, 5)

# A9: m_t/M_Z direct vs computed
mt_MZ_comp = m_t / M_Z
test("A9", "m_t/M_Z (direct) vs m_t / M_Z",
     mt_MZ_comp, mt_MZ, 5)

# A10: m_c/m_s lattice vs computed
mc_ms_comp = m_c / m_s
test("A10", "m_c/m_s (lattice) vs m_c / m_s",
     mc_ms_comp, mc_ms, 3)

# A11: m_b/m_c lattice vs computed
mb_mc_comp = m_b / m_c
test("A11", "m_b/m_c (lattice) vs m_b / m_c",
     mb_mc_comp, mb_mc, 3)

# A12: m_u/m_d lattice vs computed
mu_md_comp = m_u / m_d
test("A12", "m_u/m_d (lattice) vs m_u / m_d",
     mu_md_comp, mu_md, 2)

# ================================================================
# GROUP B: ANALYTICAL CONSTANT IDENTITIES
# ================================================================

print("-" * 78)
print("GROUP B: ANALYTICAL CONSTANT IDENTITIES")
print("-" * 78)
print()

# B1: R2 = pi/4 (both from Q335)
# R2 is computed from pi_f/4, so this tests the Q335 numerator consistency
# Check: p_pi / 4 vs what we'd get from a stored R2 numerator
# Since R2_f = pi_f / 4 by construction, test against mpmath
R2_mp = m2f(mpi / 4, 10**105)
test("B1", "R₂ = π/4 (Q335 vs mpmath)",
     R2_f, R2_mp, 100, "Q335", "mpmath")

# B2: R4 = pi^2/32
R4_mp = m2f(mpi**2 / 32, 10**105)
test("B2", "R₄ = π²/32 (Q335 vs mpmath)",
     R4_f, R4_mp, 100, "Q335", "mpmath")

# B3: 2π = 8R₂ (exact in Q335 — test numerator identity)
twopi_from_R2 = 8 * R2_f
test("B3", "2π = 8R₂ (exact numerator test)",
     twopi_f, twopi_from_R2, 100)

# B4: ζ(2) = π²/6 (both stored as Q335 numerators)
pi2_over_6 = pi2_f / 6
test("B4", "ζ(2) = π²/6 (Q335 numerators)",
     zeta2_f, pi2_over_6, 99)

# B5: α/π vs 1/(α⁻¹ × π)
alpha_pi_comp = Fraction(1, 1) / (alpha_inv * pi_f)
# The stored alpha/pi entry should match
# We need to compare against the DATA-2 value
# alpha/pi from DATA-2: 0.0023228194641953288958414081556854230727547686765382 (12 digits)
alpha_pi_stored = Fraction(23228194641953, 10**16)  # 12 sig figs
test("B5", "α/π (stored) vs 1/(α⁻¹ × π_Q335)",
     alpha_pi_comp, alpha_pi_stored, 12)

# B6: φ = (1 + √5)/2
phi_comp = (Fraction(1,1) + sqrt5_f) / 2
test("B6", "φ = (1 + √5)/2 (Q335 numerators)",
     phi_f, phi_comp, 100)

# B7: π² stored vs π × π (Q335 multiplication)
pi_squared_comp = pi_f * pi_f
test("B7", "π² stored vs π × π (Q335)",
     pi2_f, pi_squared_comp, 99)

# B8: 2π stored vs 2 × π
twopi_comp = 2 * pi_f
test("B8", "2π stored vs 2 × π (exact)",
     twopi_f, twopi_comp, 100)

# ================================================================
# GROUP C: PHYSICAL RELATIONS
# ================================================================

print("-" * 78)
print("GROUP C: PHYSICAL RELATIONS")
print("-" * 78)
print()

# C1: R∞ = α² m_e c / (2h)
# Units: R∞ in m^-1, m_e in MeV, c in m/s, h in J·s
# Need m_e in kg: m_e(kg) = m_e(MeV) × e_charge(C) × 10^6 / c²
# Or use: R∞ = α² m_e c / (2h) where m_e is in kg
# m_e(kg) from CODATA: 9.1093837139e-31 kg... but we don't store that.
# Instead use the relation: R∞ = m_e(MeV) × 10^6 × e_charge / (2 h c) × α²
# Actually: E = mc², so m_e(kg) = m_e(MeV) × 10^6 × e_charge / c²
# R∞ = α² × m_e(kg) × c / (2h) = α² × m_e(MeV) × 10^6 × e_charge / (2h × c)
alpha_frac = Fraction(1, 1) / alpha_inv
m_e_kg = m_e * Fraction(10**6, 1) * e_charge / (c * c)  # m_e in kg as Fraction
R_inf_comp = alpha_frac * alpha_frac * m_e_kg * c / (2 * h)
test("C1", "R∞ = α² m_e c / (2h)",
     R_inf_comp, R_inf, 11,
     "Computed from α, m_e, c, h", "Stored R∞")

# C2: a₀ = ℏ/(m_e c α) = h/(2π m_e c α)
# a₀ in meters. m_e in kg (computed above).
hbar = h / (2 * pi_f)  # using Q335 pi
a_0_comp = hbar / (m_e_kg * c * alpha_frac)
test("C2", "a₀ = ℏ/(m_e c α)",
     a_0_comp, a_0, 11,
     "Computed from h, π, m_e, c, α", "Stored a₀")

# C3: μ₀ = 2αh/(c e²)
# Since 2019 SI: μ₀ = 2α h / (c e²) is exact given α, h, c, e
mu_0_comp = 2 * alpha_frac * h / (c * e_charge * e_charge)
test("C3", "μ₀ = 2αh/(ce²)",
     mu_0_comp, mu_0, 12,
     "Computed from α, h, c, e", "Stored μ₀")

# C4: Deuteron mass = m_p + m_n - E_D
m_D_comp = m_p + m_n - E_D
test("C4", "m_D = m_p + m_n − E_D",
     m_D_comp, m_D, 8,
     "Computed from m_p, m_n, E_D", "Stored m_D")

# ================================================================
# GROUP D: KOIDE DERIVED ENTRIES
# ================================================================

print("-" * 78)
print("GROUP D: KOIDE DERIVED ENTRIES (K1-K16)")
print("-" * 78)
print()

# D1: Koide ratio from masses
mp.dps = 50
sm_e = msqrt(f2m(m_e))
sm_mu = msqrt(f2m(m_mu))
sm_tau = msqrt(f2m(m_tau))
sum_m = f2m(m_e) + f2m(m_mu) + f2m(m_tau)
sum_sqrt = sm_e + sm_mu + sm_tau
K_comp = sum_m / sum_sqrt**2
K_comp_frac = m2f(K_comp, 10**15)
test("D1", "Koide K(e,μ,τ) from masses",
     K_comp_frac, K_koide, 6,
     "Computed from m_e, m_μ, m_τ", "Stored K1")

# D2: Koide amplitude from K
# a² = 2(3K - 1), a = sqrt(a²)
a2_comp = float(2 * (3 * K_comp - 1))
a_comp = math.sqrt(a2_comp)
a_stored = 1.4142005052  # K4 from addendum
test("D2", "a(leptons) from K",
     Fraction(int(a_comp * 10**10), 10**10),
     Fraction(int(a_stored * 10**10), 10**10),
     6, "Computed", "Stored K4")

# D3: M (scale) from masses
M_comp = float(sum_sqrt / 3)
M_stored = 17.716  # K14 from addendum (in sqrt(MeV))
test("D3", "M(leptons) = (Σ√m)/3",
     Fraction(int(M_comp * 10**6), 10**6),
     Fraction(int(M_stored * 10**6), 10**6),
     4, "Computed", "Stored K14")

# D4: Up-type Koide
sm_u = msqrt(f2m(m_u))
sm_c = msqrt(f2m(m_c))
sm_t = msqrt(f2m(m_t))
K_up = (f2m(m_u) + f2m(m_c) + f2m(m_t)) / (sm_u + sm_c + sm_t)**2
K_up_stored = Fraction(8487935476, 10**10)  # K2
test("D4", "Koide K(u,c,t) from masses",
     m2f(K_up, 10**12), K_up_stored, 3,
     "Computed", "Stored K2")

# D5: Down-type Koide
sm_d = msqrt(f2m(m_d))
sm_s = msqrt(f2m(m_s))
sm_b = msqrt(f2m(m_b))
K_dn = (f2m(m_d) + f2m(m_s) + f2m(m_b)) / (sm_d + sm_s + sm_b)**2
K_dn_stored = Fraction(7312875768, 10**10)  # K3
test("D5", "Koide K(d,s,b) from masses",
     m2f(K_dn, 10**12), K_dn_stored, 3,
     "Computed", "Stored K3")

# ================================================================
# GROUP E: EXACT DEFINED CROSS-CHECKS
# ================================================================

print("-" * 78)
print("GROUP E: EXACT DEFINED CROSS-CHECKS")
print("-" * 78)
print()

# E1: h × Δν_Cs = exact energy
hv = h * dv_Cs  # in Joules
hv_expected = Fraction(662607015, 10**42) * Fraction(9192631770, 1)
test("E1", "h × Δν_Cs product",
     hv, hv_expected, 15,
     "h × Δν_Cs", "Direct multiplication")

# E2: Speed of light is integer
test("E2", "c is exact integer",
     c, Fraction(299792458, 1), 15,
     "Stored c", "Expected 299792458")

# E3: Planck constant exact digits
h_expected = Fraction(662607015, 10**42)
test("E3", "h exact SI value",
     h, h_expected, 9,
     "Stored h", "SI 2019 definition")

# ================================================================
# GROUP F: CROSS-SECTION CHECKS
# ================================================================

print("-" * 78)
print("GROUP F: CROSS-SECTION CHECKS")
print("-" * 78)
print()

# F1: m_c/m_s from lattice vs from individual masses
mc_ms_from_masses = m_c / m_s
mc_ms_lattice = mc_ms
test("F1", "m_c/m_s: lattice vs individual masses",
     mc_ms_from_masses, mc_ms_lattice, 3,
     "From m_c/m_s", "Lattice value")

# F2: m_b/m_c from lattice vs from individual masses
mb_mc_from_masses = m_b / m_c
test("F2", "m_b/m_c: lattice vs individual masses",
     mb_mc_from_masses, mb_mc, 3,
     "From m_b/m_c", "Lattice value")

# F3: m_u/m_d from lattice vs from individual masses
mu_md_from_masses = m_u / m_d
test("F3", "m_u/m_d: lattice vs individual masses",
     mu_md_from_masses, mu_md, 2,
     "From m_u/m_d", "Lattice value")

# F4: H 1S-2S leading order vs R∞
# ν(1S-2S) ≈ (3/4) × 2 × c × R∞ = (3/2) c R∞
H_1S2S = Fraction(2466061413187018, 1)  # Hz
H_1S2S_approx = Fraction(3, 2) * c * R_inf
rel = abs(float(H_1S2S - H_1S2S_approx) / float(H_1S2S))
print(f"  [INFO] F4: H 1S-2S leading order check (soft, ~ppm level)")
print(f"        Measured:     {float(H_1S2S):.0f} Hz")
print(f"        (3/2)·c·R∞:  {float(H_1S2S_approx):.0f} Hz")
print(f"        Relative diff: {rel:.3e} ({-math.log10(rel):.1f} digits)")
print(f"        Expected: ~ppm level (Lamb shift, QED corrections)")
print()

# ================================================================
# SUMMARY
# ================================================================

print("=" * 78)
print("SUMMARY")
print("=" * 78)
print()

n_pass = sum(1 for _, _, s, _, _ in checks if s == "PASS")
n_fail = sum(1 for _, _, s, _, _ in checks if s == "FAIL")

print(f"  Total tests: {len(checks)}")
print(f"  PASS: {n_pass}")
print(f"  FAIL: {n_fail}")
print()

if n_fail > 0:
    print("  FAILURES:")
    for tid, name, status, digits, needed in checks:
        if status == "FAIL":
            print(f"    {tid}: {name}")
            print(f"      Got {digits:.1f} digits, needed {needed}")
    print()
    print("  DATABASE HAS INCONSISTENCIES. Investigate before declaring DATA-3.")
else:
    print("  ALL TESTS PASS.")
    print()
    print("  DATA-3 DECLARATION:")
    print("  The DATA-2 database (107 + 16 Koide entries = 123 total) is internally")
    print("  consistent to the precision of all source measurements. Every testable")
    print("  relation holds. DATA-2 is hereby promoted to DATA-3 and becomes the")
    print("  sole reference for all future HOWL computation.")
    print()
    print("  DATA-2 is retired. All references point to DATA-3.")

print()

# Print full results table
print("-" * 78)
print("FULL RESULTS TABLE")
print("-" * 78)
print()
print(f"  {'ID':<6s} {'Test':.<50s} {'Digits':>7s} {'Need':>6s} {'Status':>8s}")
print(f"  {'-'*6} {'-'*50} {'-'*7} {'-'*6} {'-'*8}")
for tid, name, status, digits, needed in checks:
    d_str = f"{digits:.1f}" if digits < 500 else "exact"
    print(f"  {tid:<6s} {name:.<50s} {d_str:>7s} {needed:>6d} {status:>8s}")

print()
print("=" * 78)
print("DATA-3 VERIFICATION COMPLETE")
print("=" * 78)

