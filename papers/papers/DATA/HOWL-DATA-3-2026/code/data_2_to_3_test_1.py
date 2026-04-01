#!/usr/bin/env python3
"""
HOWL-DATA-3: Database Consistency Verification (Final)
=======================================================

Run every testable internal relation in DATA-2.
All computation in Fraction arithmetic.
Square roots via mpmath at 120 digits.

FIXES from v1:
  - A2: mmu_me exponent corrected (10^19 → 10^17)
  - B1, B2: mpmath precision raised to 120 digits
  - C3: threshold 12 → 11 (rounding margin at last digit)
  - A10-A12, F1-F3: REMOVED (lattice ratios at common scale
    cannot be compared to PDG masses at different scales)
  - F4: formula corrected (3/2 → 3/4)
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi
import math

mp.dps = 120

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

def m2f(x, denom=10**110):
    """Convert mpf to Fraction at high precision."""
    return Fraction(int(x * denom), denom)

# ================================================================
# DATA-2 ENTRIES
# ================================================================

# --- Section A: SI fundamental (exact by definition) ---
c        = Fraction(299792458, 1)
h        = Fraction(662607015, 10**42)
e_charge = Fraction(1602176634, 10**28)
k_B      = Fraction(1380649, 10**29)
N_A      = Fraction(602214076, 1) * Fraction(10**15, 1)
dv_Cs    = Fraction(9192631770, 1)
K_cd     = Fraction(683, 1)

# --- Section B: Measured fundamental (CODATA 2022) ---
alpha_inv = Fraction(137035999177, 10**9)
m_e       = Fraction(51099895069, 10**11)
m_mu      = Fraction(1056583755, 10**7)
m_tau     = Fraction(177686, 100)
m_p       = Fraction(93827208943, 10**8)
mp_me     = Fraction(183615267343, 10**8)
R_inf     = Fraction(10973731568157, 10**6)
a_0       = Fraction(529177210544, 10**22)
a_e       = Fraction(115965218059, 10**14)
a_mu      = Fraction(116592059, 10**11)
sin2_tW   = Fraction(23122, 100000)
alpha_s   = Fraction(1180, 10000)
mu_0      = Fraction(125663706127, 10**17)

# --- Section C: Electroweak ---
M_Z       = Fraction(911876, 10)
Gamma_Z   = Fraction(24952, 10)
M_W       = Fraction(803692, 10)
m_t       = Fraction(172570, 1)
m_H       = Fraction(125200, 1)
G_F       = Fraction(11663788, 10**12)

# --- Section D: Quarks and CKM ---
m_u       = Fraction(216, 100)
m_d       = Fraction(470, 100)
m_s       = Fraction(935, 10)
m_c       = Fraction(1273, 1)
m_b       = Fraction(4183, 1)
sin_t12   = Fraction(22501, 100000)
sin_t23   = Fraction(4182, 100000)
sin_t13   = Fraction(3685, 1000000)
mc_ms     = Fraction(11783, 1000)
mb_mc     = Fraction(4578, 1000)
mu_md     = Fraction(485, 1000)

# --- Section E: Nuclear/hadron ---
m_n        = Fraction(93956542194, 10**8)
mn_mp_diff = Fraction(129333251, 10**8)
m_pi_p     = Fraction(13957039, 10**5)
m_pi_0     = Fraction(1349770, 10**4)
m_K_p      = Fraction(493677, 10**3)
m_D        = Fraction(187561294500, 10**8)
m_He4      = Fraction(37273794118, 10**7)
E_D        = Fraction(222456614, 10**8)

# --- Section F: Atomic spectroscopy ---
H_1S2S     = Fraction(2466061413187018, 1)

# --- Section K: Dimensionless ratios ---
mmu_me     = Fraction(20676828270846717969, 10**17)    # FIXED: was 10^19
mtau_me    = Fraction(347723, 100)
mtau_mmu   = Fraction(168170, 10000)
mn_mp      = Fraction(10013784194633623804, 10**19)
MW_MZ      = Fraction(881361, 10**6)
mH_MZ      = Fraction(137299, 10**5)
mt_MZ      = Fraction(189247, 10**5)
K_koide    = Fraction(6666605115, 10**10)

# --- Section G: Q335 analytical constants ---
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

R2_f    = pi_f / 4
R4_f    = pi2_f / 32
twopi_f = 2 * pi_f
alpha_frac = Fraction(1, 1) / alpha_inv

# ================================================================
# TEST FRAMEWORK
# ================================================================

checks = []

def test(test_id, name, left, right, min_digits, left_label="Computed", right_label="Stored"):
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
    print(f"      {left_label}: {float(left):.15e}")
    print(f"      {right_label}: {float(right):.15e}")
    if digits_agree > 500:
        print(f"      Agreement: EXACT")
    else:
        print(f"      Relative diff: {rel_diff:.2e}  ({digits_agree:.1f} digits, need {min_digits})")
    if not passed:
        print(f"      *** FAIL ***")
    print()
    return passed

# ================================================================
print("=" * 78)
print("HOWL-DATA-3: DATABASE CONSISTENCY VERIFICATION")
print("=" * 78)
print()

# ================================================================
# GROUP A: MASS RATIO IDENTITIES
# ================================================================
print("GROUP A: MASS RATIO IDENTITIES")
print("-" * 78)
print()

test("A1", "m_p/m_e direct vs m_p / m_e",
     m_p / m_e, mp_me, 11)

test("A2", "m_μ/m_e direct vs m_μ / m_e",
     m_mu / m_e, mmu_me, 10)

test("A3", "m_τ/m_e direct vs m_τ / m_e",
     m_tau / m_e, mtau_me, 6)

test("A4", "m_τ/m_μ direct vs m_τ / m_μ",
     m_tau / m_mu, mtau_mmu, 5)

test("A5", "m_n/m_p direct vs m_n / m_p",
     m_n / m_p, mn_mp, 11)

test("A6", "M_W/M_Z direct vs M_W / M_Z",
     M_W / M_Z, MW_MZ, 6)

test("A7", "m_n − m_p direct vs stored difference",
     m_n - m_p, mn_mp_diff, 8)

test("A8", "m_H/M_Z direct vs stored ratio",
     m_H / M_Z, mH_MZ, 5)

test("A9", "m_t/M_Z direct vs stored ratio",
     m_t / M_Z, mt_MZ, 5)

# ================================================================
# GROUP B: ANALYTICAL CONSTANT IDENTITIES
# ================================================================
print("GROUP B: ANALYTICAL CONSTANT IDENTITIES (Q335 basis)")
print("-" * 78)
print()

# B1: R2 = pi/4 — compare Q335 Fraction to mpmath at 120 digits
R2_mp = m2f(mpi / 4, 10**110)
test("B1", "R₂ = π/4 (Q335 vs mpmath@120)",
     R2_f, R2_mp, 100, "Q335", "mpmath")

# B2: R4 = pi^2/32
R4_mp = m2f(mpi**2 / 32, 10**110)
test("B2", "R₄ = π²/32 (Q335 vs mpmath@120)",
     R4_f, R4_mp, 100, "Q335", "mpmath")

# B3: 2pi = 8*R2 (exact identity within Q335)
test("B3", "2π = 8R₂ (exact within Q335)",
     twopi_f, 8 * R2_f, 100)

# B4: zeta(2) = pi^2/6
test("B4", "ζ(2) = π²/6 (Q335 numerators)",
     zeta2_f, pi2_f / 6, 99)

# B5: alpha/pi from components
alpha_pi_comp = Fraction(1, 1) / (alpha_inv * pi_f)
alpha_pi_stored = Fraction(23228194641953, 10**16)
test("B5", "α/π stored vs 1/(α⁻¹ × π)",
     alpha_pi_comp, alpha_pi_stored, 12)

# B6: phi = (1+sqrt5)/2
test("B6", "φ = (1 + √5)/2 (Q335)",
     phi_f, (Fraction(1,1) + sqrt5_f) / 2, 100)

# B7: pi^2 stored vs pi * pi
test("B7", "π² stored vs π × π (Q335)",
     pi2_f, pi_f * pi_f, 99)

# B8: 2pi stored vs 2 * pi (exact)
test("B8", "2π stored vs 2 × π (exact)",
     twopi_f, 2 * pi_f, 100)

# ================================================================
# GROUP C: PHYSICAL RELATIONS
# ================================================================
print("GROUP C: PHYSICAL RELATIONS (SI 2019)")
print("-" * 78)
print()

# C1: R_inf = alpha^2 * m_e * c / (2h)
# m_e in kg: m_e(MeV) * 10^6 * e(C) / c^2
m_e_kg = m_e * Fraction(10**6, 1) * e_charge / (c * c)
R_inf_comp = alpha_frac * alpha_frac * m_e_kg * c / (2 * h)
test("C1", "R∞ = α²m_ec/(2h)",
     R_inf_comp, R_inf, 11,
     "From α, m_e, c, h", "Stored R∞")

# C2: a_0 = hbar / (m_e c alpha)
hbar = h / (2 * pi_f)
a_0_comp = hbar / (m_e_kg * c * alpha_frac)
test("C2", "a₀ = ℏ/(m_e c α)",
     a_0_comp, a_0, 11,
     "From ℏ, m_e, c, α", "Stored a₀")

# C3: mu_0 = 2 alpha h / (c e^2)  [exact in SI 2019 given alpha]
mu_0_comp = 2 * alpha_frac * h / (c * e_charge * e_charge)
test("C3", "μ₀ = 2αh/(ce²)",
     mu_0_comp, mu_0, 11,
     "From α, h, c, e", "Stored μ₀")

# C4: m_D = m_p + m_n - E_D
test("C4", "m_D = m_p + m_n − E_D",
     m_p + m_n - E_D, m_D, 8,
     "From m_p + m_n − E_D", "Stored m_D")

# C5: H 1S-2S leading order = (3/4) c R_inf  [soft check, ~ppm]
H_approx = Fraction(3, 4) * c * R_inf
H_rel = abs(float(H_1S2S - H_approx) / float(H_1S2S))
H_digits = -math.log10(H_rel) if H_rel > 0 else 999
print(f"  [INFO] C5: H 1S-2S leading order (soft check)")
print(f"      Measured:    {int(H_1S2S)} Hz")
print(f"      (3/4)cR∞:   {float(H_approx):.0f} Hz")
print(f"      Rel diff:    {H_rel:.2e} ({H_digits:.1f} digits)")
print(f"      Note: ~5 digit agreement expected (Lamb shift, QED, recoil)")
print()

# ================================================================
# GROUP D: KOIDE DERIVED ENTRIES
# ================================================================
print("GROUP D: KOIDE DERIVED ENTRIES (K1-K16)")
print("-" * 78)
print()

sm_e = msqrt(f2m(m_e))
sm_mu = msqrt(f2m(m_mu))
sm_tau = msqrt(f2m(m_tau))
sum_m_lep = f2m(m_e) + f2m(m_mu) + f2m(m_tau)
sum_sqrt_lep = sm_e + sm_mu + sm_tau
K_lep = sum_m_lep / sum_sqrt_lep**2

test("D1", "Koide K(e,μ,τ) from masses",
     m2f(K_lep, 10**15), K_koide, 6,
     "From m_e, m_μ, m_τ", "Stored K1")

# D2: amplitude
a2_lep = float(2 * (3 * K_lep - 1))
a_lep = math.sqrt(a2_lep)
test("D2", "a(leptons) from K",
     Fraction(int(a_lep * 10**10), 10**10),
     Fraction(14142005052, 10**10), 6,
     "Computed", "Stored K4")

# D3: scale M
M_lep = float(sum_sqrt_lep / 3)
test("D3", "M(leptons) = (Σ√m)/3",
     Fraction(int(M_lep * 10**6), 10**6),
     Fraction(17716, 1000), 4,
     "Computed", "Stored K14")

# D4: up quarks
sm_u = msqrt(f2m(m_u)); sm_c = msqrt(f2m(m_c)); sm_t = msqrt(f2m(m_t))
K_up = (f2m(m_u)+f2m(m_c)+f2m(m_t)) / (sm_u+sm_c+sm_t)**2
test("D4", "Koide K(u,c,t) from masses",
     m2f(K_up, 10**12), Fraction(8487935476, 10**10), 3,
     "Computed", "Stored K2")

# D5: down quarks
sm_d = msqrt(f2m(m_d)); sm_s = msqrt(f2m(m_s)); sm_b = msqrt(f2m(m_b))
K_dn = (f2m(m_d)+f2m(m_s)+f2m(m_b)) / (sm_d+sm_s+sm_b)**2
test("D5", "Koide K(d,s,b) from masses",
     m2f(K_dn, 10**12), Fraction(7312875768, 10**10), 3,
     "Computed", "Stored K3")

# ================================================================
# GROUP E: EXACT SI CONSTANTS
# ================================================================
print("GROUP E: EXACT SI CONSTANTS")
print("-" * 78)
print()

test("E1", "h × Δν_Cs product consistency",
     h * dv_Cs, Fraction(662607015, 10**42) * Fraction(9192631770, 1), 15)

test("E2", "c is exact integer 299792458",
     c, Fraction(299792458, 1), 15)

test("E3", "h exact SI 2019 value",
     h, Fraction(662607015, 10**42), 9)

test("E4", "e exact SI 2019 value",
     e_charge, Fraction(1602176634, 10**28), 10)

test("E5", "k_B exact SI 2019 value",
     k_B, Fraction(1380649, 10**29), 7)

test("E6", "N_A exact SI 2019 value",
     N_A, Fraction(602214076, 1) * Fraction(10**15, 1), 9)

# ================================================================
# GROUP F: LATTICE RATIO ANNOTATION (no numeric test)
# ================================================================
print("GROUP F: LATTICE RATIO ANNOTATION")
print("-" * 78)
print()
print("  [NOTE] Lattice ratios (m_c/m_s, m_b/m_c, m_u/m_d) are evaluated")
print("  at a COMMON renormalization scale by lattice QCD collaborations.")
print("  The individual PDG masses (m_u, m_d, m_s at 2 GeV MS-bar;")
print("  m_c at m_c; m_b at m_b) are at DIFFERENT scales.")
print("  Simple division of PDG masses does NOT reproduce lattice ratios.")
print("  This is not a database error — it is a renormalization scale mismatch.")
print()
print("  Entries 41 (m_c/m_s = 11.783), 42 (m_b/m_c = 4.578),")
print("  43 (m_u/m_d = 0.485) are INDEPENDENT data from lattice QCD")
print("  and are NOT derivable from entries 33-37.")
print()
print("  Discrepancies if naively compared:")
print(f"    m_c/m_s: PDG gives {float(m_c/m_s):.3f}, lattice = {float(mc_ms):.3f}")
print(f"    m_b/m_c: PDG gives {float(m_b/m_c):.3f}, lattice = {float(mb_mc):.3f}")
print(f"    m_u/m_d: PDG gives {float(m_u/m_d):.3f}, lattice = {float(mu_md):.3f}")
print()

# ================================================================
# SUMMARY
# ================================================================
print("=" * 78)
print("RESULTS")
print("=" * 78)
print()

n_pass = sum(1 for _, _, s, _, _ in checks if s == "PASS")
n_fail = sum(1 for _, _, s, _, _ in checks if s == "FAIL")
n_total = len(checks)

print(f"  {'ID':<6s} {'Test':<52s} {'Digits':>7s} {'Need':>6s} {'Result':>8s}")
print(f"  {'-'*6} {'-'*52} {'-'*7} {'-'*6} {'-'*8}")
for tid, name, status, digits, needed in checks:
    d_str = "exact" if digits > 500 else f"{digits:.1f}"
    print(f"  {tid:<6s} {name:<52s} {d_str:>7s} {needed:>6d} {status:>8s}")

print()
print(f"  Total: {n_total} tests,  {n_pass} PASS,  {n_fail} FAIL")
print()

if n_fail == 0:
    print("  ╔══════════════════════════════════════════════════════════════╗")
    print("  ║  ALL TESTS PASS                                            ║")
    print("  ║                                                            ║")
    print("  ║  DATA-3 DECLARATION: The DATA-2 database (107 original +   ║")
    print("  ║  16 Koide-derived = 123 entries) is internally consistent  ║")
    print("  ║  to the precision of all source measurements.              ║")
    print("  ║                                                            ║")
    print("  ║  DATA-2 is promoted to DATA-3.                            ║")
    print("  ║  DATA-2 is retired.                                       ║")
    print("  ║  All future HOWL computation references DATA-3.           ║")
    print("  ╚══════════════════════════════════════════════════════════════╝")
else:
    print("  DATABASE HAS INCONSISTENCIES.")
    print("  Failures:")
    for tid, name, status, digits, needed in checks:
        if status == "FAIL":
            print(f"    {tid}: {name} ({digits:.1f} digits, need {needed})")

print()
print("=" * 78)
print("DATA-3 VERIFICATION COMPLETE")
print("=" * 78)
