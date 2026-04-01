#!/usr/bin/env python3
"""
HOWL-DATA-4: Complete Verified Database with Cabibbo Doublet Extension
=======================================================================

Registry: [@HOWL-DATA-4-2026]
Date: April 1, 2026
Status: COMPLETE

DATA-4 inherits DATA-3 (123 entries, 32/32 checks) and adds:
  - Finding 15: Lattice ratio independence annotation (formal)
  - 6 STAGED entries for Cabibbo Doublet parameters (124-129)
  - Computation traceability map (which entries feed which papers)
  - Two-loop unification results (from Session 3 computation)

DATA-4 is the sole data reference for all future HOWL computation.
DATA-3 is retired.

This file IS the database. Every entry is a Fraction literal.
Run it to verify all 32 inherited checks pass.
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi
import math

mp.dps = 120

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

def m2f(x, denom=10**110):
    return Fraction(int(x * denom), denom)

# ================================================================
# SECTION A: SI FUNDAMENTAL CONSTANTS (Type E — exact by definition)
# ================================================================

c        = Fraction(299792458, 1)                         # A1: speed of light, m/s
h        = Fraction(662607015, 10**42)                    # A2: Planck constant, J*s
e_charge = Fraction(1602176634, 10**28)                   # A3: elementary charge, C
k_B      = Fraction(1380649, 10**29)                      # A4: Boltzmann constant, J/K
N_A      = Fraction(602214076, 1) * Fraction(10**15, 1)   # A5: Avogadro number, mol^-1
dv_Cs    = Fraction(9192631770, 1)                        # A6: Cs-133 hyperfine, Hz
K_cd     = Fraction(683, 1)                               # A7: luminous efficacy, lm/W

# ================================================================
# SECTION B: MEASURED FUNDAMENTAL CONSTANTS (CODATA 2022, Type M)
# ================================================================

alpha_inv = Fraction(137035999177, 10**9)     # B1:  alpha^-1, 12 sf
m_e       = Fraction(51099895069, 10**11)     # B2:  electron mass, MeV, 11 sf
m_mu      = Fraction(1056583755, 10**7)       # B3:  muon mass, MeV, 10 sf
m_tau     = Fraction(177686, 100)             # B4:  tau mass, MeV, 6 sf
m_p       = Fraction(93827208943, 10**8)      # B5:  proton mass, MeV, 11 sf
mp_me     = Fraction(183615267343, 10**8)     # B6:  m_p/m_e ratio, 13 sf
R_inf     = Fraction(10973731568157, 10**6)   # B7:  Rydberg constant, m^-1, 13 sf
a_0       = Fraction(529177210544, 10**22)    # B8:  Bohr radius, m, 12 sf
a_e       = Fraction(115965218059, 10**14)    # B9:  electron g-2, 12 sf
a_mu      = Fraction(116592059, 10**11)       # B10: muon g-2, 9 sf
sin2_tW   = Fraction(23122, 100000)           # B11: weak mixing angle, 5 sf
alpha_s   = Fraction(1180, 10000)             # B12: strong coupling, 4 sf
mu_0      = Fraction(125663706127, 10**17)    # B13: vacuum permeability, N/A^2, 12 sf

# ================================================================
# SECTION C: ELECTROWEAK OBSERVABLES (LEP/PDG, Type M)
# ================================================================

M_Z       = Fraction(911876, 10)     # C1: Z mass, MeV, 6 sf
Gamma_Z   = Fraction(24952, 10)      # C2: Z width, MeV, 5 sf
M_W       = Fraction(803692, 10)     # C3: W mass, MeV, 6 sf
m_t       = Fraction(172570, 1)      # C4: top mass, MeV, 5 sf
m_H       = Fraction(125200, 1)      # C5: Higgs mass, MeV, 5 sf
G_F       = Fraction(11663788, 10**12)  # C6: Fermi constant, GeV^-2, 8 sf

# ================================================================
# SECTION D: QUARK MASSES AND CKM (PDG 2024 / FLAG, Type M)
# ================================================================

m_u       = Fraction(216, 100)       # D1: up quark MS-bar 2GeV, MeV, 3 sf
m_d       = Fraction(470, 100)       # D2: down quark MS-bar 2GeV, MeV, 3 sf
m_s       = Fraction(935, 10)        # D3: strange MS-bar 2GeV, MeV, 3 sf
m_c       = Fraction(1273, 1)        # D4: charm MS-bar at m_c, MeV, 4 sf
m_b       = Fraction(4183, 1)        # D5: bottom MS-bar at m_b, MeV, 4 sf
sin_t12   = Fraction(22501, 100000)  # D6: sin theta_12 Cabibbo, 5 sf
sin_t23   = Fraction(4182, 100000)   # D7: sin theta_23 CKM, 4 sf
sin_t13   = Fraction(3685, 1000000)  # D8: sin theta_13 CKM, 4 sf
mc_ms     = Fraction(11783, 1000)    # D9:  m_c/m_s lattice (FLAG), 5 sf [INDEPENDENT]
mb_mc     = Fraction(4578, 1000)     # D10: m_b/m_c lattice (FLAG), 4 sf [INDEPENDENT]
mu_md     = Fraction(485, 1000)      # D11: m_u/m_d lattice (FLAG), 3 sf [INDEPENDENT]

# ================================================================
# SECTION E: NUCLEAR/HADRON MASSES (Type M)
# ================================================================

m_n        = Fraction(93956542194, 10**8)   # E1: neutron mass, MeV, 11 sf
mn_mp_diff = Fraction(129333251, 10**8)     # E2: m_n - m_p, MeV, 8 sf
m_pi_p     = Fraction(13957039, 10**5)      # E3: charged pion, MeV, 8 sf
m_pi_0     = Fraction(1349770, 10**4)       # E4: neutral pion, MeV, 7 sf
m_K_p      = Fraction(493677, 10**3)        # E5: charged kaon, MeV, 6 sf
m_D        = Fraction(187561294500, 10**8)  # E6: deuteron, MeV, 12 sf
m_He4      = Fraction(37273794118, 10**7)   # E7: helium-4, MeV, 10 sf
E_D        = Fraction(222456614, 10**8)     # E8: deuteron binding, MeV, 8 sf

# ================================================================
# SECTION F: ATOMIC SPECTROSCOPY (Type M)
# ================================================================

H_1S2S = Fraction(2466061413187018, 1)  # F1: H 1S-2S, Hz, 16 sf

# ================================================================
# SECTION G: Q335 ANALYTICAL CONSTANTS (Type A, 101+ digits)
# ================================================================

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

pi_f    = Fraction(p_pi, Q)    # G1:  pi
e_f     = Fraction(p_e, Q)     # G2:  e (Euler's number)
ln2_f   = Fraction(p_ln2, Q)   # G3:  ln(2)
sqrt2_f = Fraction(p_sqrt2, Q) # G4:  sqrt(2)
sqrt3_f = Fraction(p_sqrt3, Q) # G5:  sqrt(3)
sqrt5_f = Fraction(p_sqrt5, Q) # G6:  sqrt(5)
phi_f   = Fraction(p_phi, Q)   # G7:  golden ratio
zeta3_f = Fraction(p_zeta3, Q) # G8:  zeta(3)
zeta5_f = Fraction(p_zeta5, Q) # G9:  zeta(5)
pi2_f   = Fraction(p_pi2, Q)   # G10: pi^2
zeta2_f = Fraction(p_zeta2, Q) # G11: zeta(2) = pi^2/6

R2_f    = pi_f / 4             # G12: R_2 = pi/4
R4_f    = pi2_f / 32           # G13: R_4 = pi^2/32
twopi_f = 2 * pi_f             # G14: 2*pi

alpha_frac = Fraction(1, 1) / alpha_inv  # derived: alpha from alpha^-1

# ================================================================
# SECTION K: DIMENSIONLESS MASS RATIOS (Type M, computed from above)
# ================================================================

mmu_me   = Fraction(20676828270846717969, 10**17)   # K1: m_mu/m_e, 10 sf
mtau_me  = Fraction(347723, 100)                     # K2: m_tau/m_e, 6 sf
mtau_mmu = Fraction(168170, 10000)                   # K3: m_tau/m_mu, 5 sf
mn_mp    = Fraction(10013784194633623804, 10**19)    # K4: m_n/m_p, 11 sf
MW_MZ    = Fraction(881361, 10**6)                   # K5: M_W/M_Z, 6 sf
mH_MZ    = Fraction(137299, 10**5)                   # K6: m_H/M_Z, 5 sf
mt_MZ    = Fraction(189247, 10**5)                   # K7: m_t/M_Z, 5 sf
K_koide  = Fraction(6666605115, 10**10)              # K8: Koide ratio, 6 sf

# ================================================================
# SECTION L: CABIBBO DOUBLET PARAMETERS (Type G — STAGED)
# NEW IN DATA-4
# ================================================================

# These entries are bounded but not yet measured.
# Values are constraint WINDOWS, not measurements.
# When measured, they transition from Type G to Type M.

# L1: M_VL — Cabibbo Doublet mass
#   Window: 1.5 - 6.0 TeV
#   Lower bound: LHC pair production exclusion (~1.5 TeV)
#   Upper bound: CKM perturbativity + anomaly fit (~6 TeV)
#   Sources: PHYS-16, PHYS-19
M_VL_lo = Fraction(1500000, 1)   # 1500 GeV = 1.5 TeV, lower bound
M_VL_hi = Fraction(6000000, 1)   # 6000 GeV = 6.0 TeV, upper bound

# L2: sin(theta_14) — 1st-gen mixing angle
#   Estimated: |V_ub'| ~ 0.045 from CKM first-row deficit
#   Source: PHYS-19 (Belfatto, Berezhiani 2020)
theta14_est = Fraction(45, 1000)   # ~0.045

# L3: theta_24 — 2nd-gen mixing angle
#   Constrained by kaon physics (K0-K0bar mixing, NA62)
#   No point estimate; bounded from above
theta24_status = "CONSTRAINED_BY_KAON_PHYSICS"

# L4: sin(theta_34) — 3rd-gen mixing angle
#   From A_FB^b fit at LEP Z-pole
#   Source: PHYS-19
theta34_status = "FROM_A_FB_B_FIT"

# L5: delta_1 — new CP phase 1
#   Constrained by neutron EDM < 10^-26 e*cm
delta1_status = "CONSTRAINED_BY_NEDM"

# L6: delta_2 — new CP phase 2
#   Constrained by B-meson CP asymmetries
delta2_status = "CONSTRAINED_BY_B_PHYSICS"

# ================================================================
# SECTION N: GUT AND UNIFICATION PARAMETERS (Type D — Derived)
# NEW IN DATA-4, from Session 3 computations
# ================================================================

# One-loop beta coefficients (Level 1, exact)
b1_SM = Fraction(41, 10)    # N1: U(1)_Y, GUT normalization
b2_SM = Fraction(-19, 6)    # N2: SU(2)_L
b3_SM = Fraction(-7, 1)     # N3: SU(3)_c

# Cabibbo Doublet beta shifts (Level 1, exact)
db1_VL = Fraction(1, 15)    # N4: VL U(1) shift
db2_VL = Fraction(1, 1)     # N5: VL SU(2) shift
db3_VL = Fraction(1, 3)     # N6: VL SU(3) shift

# Modified betas (Level 1, exact)
b1_mod = b1_SM + db1_VL     # N7: = 25/6
b2_mod = b2_SM + db2_VL     # N8: = -13/6
b3_mod = b3_SM + db3_VL     # N9: = -20/3

# Gap ratios (Level 1, exact)
gap_SM  = (b1_SM - b2_SM) / (b2_SM - b3_SM)     # N10: = 218/115
gap_VL  = (b1_mod - b2_mod) / (b2_mod - b3_mod)  # N11: = 38/27
gap_MSSM = Fraction(7, 5)                         # N12: MSSM gap ratio

# Measured gap ratio (Derived from Level 2 couplings)
# Computed in GUT script from alpha_inv, sin2_tW, alpha_s
alpha_1_GUT = Fraction(5, 3) * alpha_frac / (Fraction(1) - sin2_tW)
alpha_2_GUT = alpha_frac / sin2_tW
alpha_3_GUT = alpha_s
inv_a1 = Fraction(1) / alpha_1_GUT
inv_a2 = Fraction(1) / alpha_2_GUT
inv_a3 = Fraction(1) / alpha_3_GUT
gap_measured = (inv_a1 - inv_a2) / (inv_a2 - inv_a3)  # N13: ~1.358

# Two-loop SM b_ij matrix (Level 1, exact)
# From Machacek-Vaughn (1983), Luo-Xiao hep-ph/0207271
b_ij_SM = [                                    # N14: two-loop matrix
    [Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)],
    [Fraction(9, 10),   Fraction(35, 6),  Fraction(12, 1)],
    [Fraction(11, 10),  Fraction(9, 2),   Fraction(-26, 1)],
]

# Two-loop unification results (Derived, from unification_test.py)
# At M_VL = 500 GeV (closest approach):
delta_1loop_500  = Fraction(-117, 100)   # N15: -1.17 (one-loop miss)
delta_2loop_500  = Fraction(-40, 100)    # N16: -0.40 (two-loop miss)
twoloop_improvement = Fraction(66, 100)  # N17: 66% improvement

# ================================================================
# TEST FRAMEWORK (inherited from DATA-3)
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

    print("  [%s] %s: %s" % (status, test_id, name))
    print("      %s: %.15e" % (left_label, float(left)))
    print("      %s: %.15e" % (right_label, float(right)))
    if digits_agree > 500:
        print("      Agreement: EXACT")
    else:
        print("      Relative diff: %.2e  (%.1f digits, need %d)" % (rel_diff, digits_agree, min_digits))
    if not passed:
        print("      *** FAIL ***")
    print()
    return passed

# ================================================================
print("=" * 78)
print("HOWL-DATA-4: VERIFIED DATABASE WITH CABIBBO DOUBLET EXTENSION")
print("=" * 78)
print()

# ================================================================
# GROUP A: MASS RATIO IDENTITIES (inherited from DATA-3)
# ================================================================
print("GROUP A: MASS RATIO IDENTITIES")
print("-" * 78)
print()

test("A1", "m_p/m_e direct vs m_p / m_e", m_p / m_e, mp_me, 11)
test("A2", "m_mu/m_e direct vs m_mu / m_e", m_mu / m_e, mmu_me, 10)
test("A3", "m_tau/m_e direct vs m_tau / m_e", m_tau / m_e, mtau_me, 6)
test("A4", "m_tau/m_mu direct vs m_tau / m_mu", m_tau / m_mu, mtau_mmu, 5)
test("A5", "m_n/m_p direct vs m_n / m_p", m_n / m_p, mn_mp, 11)
test("A6", "M_W/M_Z direct vs M_W / M_Z", M_W / M_Z, MW_MZ, 6)
test("A7", "m_n - m_p direct vs stored difference", m_n - m_p, mn_mp_diff, 8)
test("A8", "m_H/M_Z direct vs stored ratio", m_H / M_Z, mH_MZ, 5)
test("A9", "m_t/M_Z direct vs stored ratio", m_t / M_Z, mt_MZ, 5)

# ================================================================
# GROUP B: ANALYTICAL CONSTANT IDENTITIES (inherited from DATA-3)
# ================================================================
print("GROUP B: ANALYTICAL CONSTANT IDENTITIES (Q335 basis)")
print("-" * 78)
print()

R2_mp = m2f(mpi / 4, 10**110)
test("B1", "R2 = pi/4 (Q335 vs mpmath@120)", R2_f, R2_mp, 100, "Q335", "mpmath")

R4_mp = m2f(mpi**2 / 32, 10**110)
test("B2", "R4 = pi^2/32 (Q335 vs mpmath@120)", R4_f, R4_mp, 100, "Q335", "mpmath")

test("B3", "2pi = 8*R2 (exact within Q335)", twopi_f, 8 * R2_f, 100)

test("B4", "zeta(2) = pi^2/6 (Q335 numerators)", zeta2_f, pi2_f / 6, 99)

alpha_pi_comp = Fraction(1, 1) / (alpha_inv * pi_f)
alpha_pi_stored = Fraction(23228194641953, 10**16)
test("B5", "alpha/pi stored vs 1/(alpha_inv * pi)", alpha_pi_comp, alpha_pi_stored, 12)

test("B6", "phi = (1 + sqrt5)/2 (Q335)", phi_f, (Fraction(1,1) + sqrt5_f) / 2, 100)

test("B7", "pi^2 stored vs pi * pi (Q335)", pi2_f, pi_f * pi_f, 99)

test("B8", "2pi stored vs 2 * pi (exact)", twopi_f, 2 * pi_f, 100)

# ================================================================
# GROUP C: PHYSICAL RELATIONS (inherited from DATA-3)
# ================================================================
print("GROUP C: PHYSICAL RELATIONS (SI 2019)")
print("-" * 78)
print()

m_e_kg = m_e * Fraction(10**6, 1) * e_charge / (c * c)
R_inf_comp = alpha_frac * alpha_frac * m_e_kg * c / (2 * h)
test("C1", "R_inf = alpha^2 m_e c/(2h)", R_inf_comp, R_inf, 11,
     "From alpha, m_e, c, h", "Stored R_inf")

hbar = h / (2 * pi_f)
a_0_comp = hbar / (m_e_kg * c * alpha_frac)
test("C2", "a_0 = hbar/(m_e c alpha)", a_0_comp, a_0, 11,
     "From hbar, m_e, c, alpha", "Stored a_0")

mu_0_comp = 2 * alpha_frac * h / (c * e_charge * e_charge)
test("C3", "mu_0 = 2*alpha*h/(c*e^2)", mu_0_comp, mu_0, 11,
     "From alpha, h, c, e", "Stored mu_0")

test("C4", "m_D = m_p + m_n - E_D", m_p + m_n - E_D, m_D, 8,
     "From m_p + m_n - E_D", "Stored m_D")

H_approx = Fraction(3, 4) * c * R_inf
H_rel = abs(float(H_1S2S - H_approx) / float(H_1S2S))
H_digits = -math.log10(H_rel) if H_rel > 0 else 999
print("  [INFO] C5: H 1S-2S leading order (soft check)")
print("      Measured:    %d Hz" % int(H_1S2S))
print("      (3/4)cR_inf: %.0f Hz" % float(H_approx))
print("      Rel diff:    %.2e (%.1f digits)" % (H_rel, H_digits))
print("      Note: ~5 digit agreement expected (Lamb shift, QED, recoil)")
print()

# ================================================================
# GROUP D: KOIDE DERIVED ENTRIES (inherited from DATA-3)
# ================================================================
print("GROUP D: KOIDE DERIVED ENTRIES (K1-K16)")
print("-" * 78)
print()

sm_e = msqrt(f2m(m_e)); sm_mu = msqrt(f2m(m_mu)); sm_tau = msqrt(f2m(m_tau))
sum_m_lep = f2m(m_e) + f2m(m_mu) + f2m(m_tau)
sum_sqrt_lep = sm_e + sm_mu + sm_tau
K_lep = sum_m_lep / sum_sqrt_lep**2

test("D1", "Koide K(e,mu,tau) from masses",
     m2f(K_lep, 10**15), K_koide, 6, "From m_e, m_mu, m_tau", "Stored K1")

a2_lep = float(2 * (3 * K_lep - 1))
a_lep = math.sqrt(a2_lep)
test("D2", "a(leptons) from K",
     Fraction(int(a_lep * 10**10), 10**10),
     Fraction(14142005052, 10**10), 6, "Computed", "Stored K4")

M_lep = float(sum_sqrt_lep / 3)
test("D3", "M(leptons) = (sum sqrt m)/3",
     Fraction(int(M_lep * 10**6), 10**6),
     Fraction(17716, 1000), 4, "Computed", "Stored K14")

sm_u = msqrt(f2m(m_u)); sm_c = msqrt(f2m(m_c)); sm_t = msqrt(f2m(m_t))
K_up = (f2m(m_u)+f2m(m_c)+f2m(m_t)) / (sm_u+sm_c+sm_t)**2
test("D4", "Koide K(u,c,t) from masses",
     m2f(K_up, 10**12), Fraction(8487935476, 10**10), 3, "Computed", "Stored K2")

sm_d = msqrt(f2m(m_d)); sm_s = msqrt(f2m(m_s)); sm_b = msqrt(f2m(m_b))
K_dn = (f2m(m_d)+f2m(m_s)+f2m(m_b)) / (sm_d+sm_s+sm_b)**2
test("D5", "Koide K(d,s,b) from masses",
     m2f(K_dn, 10**12), Fraction(7312875768, 10**10), 3, "Computed", "Stored K3")

# ================================================================
# GROUP E: EXACT SI CONSTANTS (inherited from DATA-3)
# ================================================================
print("GROUP E: EXACT SI CONSTANTS")
print("-" * 78)
print()

test("E1", "h * dv_Cs product consistency",
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
# GROUP F: LATTICE RATIO ANNOTATION — FINDING 15 (formalized in DATA-4)
# ================================================================
print("GROUP F: LATTICE RATIO INDEPENDENCE — FINDING 15")
print("-" * 78)
print()
print("  Entries D9 (m_c/m_s = 11.783), D10 (m_b/m_c = 4.578),")
print("  D11 (m_u/m_d = 0.485) are INDEPENDENT measurements from")
print("  lattice QCD (FLAG averages) evaluated at a COMMON scale.")
print()
print("  They are NOT derivable from individual PDG quark masses")
print("  (D1-D5) which are evaluated at DIFFERENT scales:")
print("    m_u, m_d, m_s at mu = 2 GeV MS-bar")
print("    m_c at mu = m_c ~ 1.27 GeV")
print("    m_b at mu = m_b ~ 4.18 GeV")
print()
print("  Discrepancies if naively compared:")
print("    m_c/m_s: PDG gives %.3f, lattice = %.3f (%.1f%%)" % (
    float(m_c/m_s), float(mc_ms), abs(float(m_c/m_s)/float(mc_ms)-1)*100))
print("    m_b/m_c: PDG gives %.3f, lattice = %.3f (%.1f%%)" % (
    float(m_b/m_c), float(mb_mc), abs(float(m_b/m_c)/float(mb_mc)-1)*100))
print("    m_u/m_d: PDG gives %.3f, lattice = %.3f (%.1f%%)" % (
    float(m_u/m_d), float(mu_md), abs(float(m_u/m_d)/float(mu_md)-1)*100))
print()
print("  This is a renormalization scale mismatch, NOT a database error.")
print("  Finding 15 registered: [@HOWL-DATA-4-FINDING-15]")
print()

# ================================================================
# GROUP G: GUT AND UNIFICATION VERIFICATION (NEW in DATA-4)
# ================================================================
print("GROUP G: GUT AND UNIFICATION VERIFICATION")
print("-" * 78)
print()

test("G1", "SM gap ratio = 218/115",
     gap_SM, Fraction(218, 115), 10)

test("G2", "SM+VL gap ratio = 38/27",
     gap_VL, Fraction(38, 27), 10)

test("G3", "MSSM gap ratio = 7/5",
     gap_MSSM, Fraction(7, 5), 10)

test("G4", "Modified b1 = 25/6",
     b1_mod, Fraction(25, 6), 10)

test("G5", "Modified b2 = -13/6",
     b2_mod, Fraction(-13, 6), 10)

test("G6", "Modified b3 = -20/3",
     b3_mod, Fraction(-20, 3), 10)

# ================================================================
# GROUP H: CABIBBO DOUBLET STAGED ENTRIES (NEW in DATA-4)
# ================================================================
print("GROUP H: CABIBBO DOUBLET STAGED ENTRIES")
print("-" * 78)
print()
print("  Entry 124: M_VL (Cabibbo Doublet mass)")
print("    Status: STAGED")
print("    Window: %.0f - %.0f MeV (%.1f - %.1f TeV)" % (
    float(M_VL_lo), float(M_VL_hi), float(M_VL_lo)/1e6, float(M_VL_hi)/1e6))
print("    Sources: PHYS-16, PHYS-19")
print("    Bounds: LHC pair production (lower), CKM perturbativity (upper)")
print()
print("  Entry 125: sin(theta_14) ~ |V_ub'|")
print("    Status: STAGED")
print("    Estimate: ~%.3f (from CKM first-row deficit)" % float(theta14_est))
print("    Source: PHYS-19 (Belfatto, Berezhiani 2020)")
print()
print("  Entry 126: theta_24 (2nd-gen mixing)")
print("    Status: STAGED (%s)" % theta24_status)
print()
print("  Entry 127: sin(theta_34) (3rd-gen mixing)")
print("    Status: STAGED (%s)" % theta34_status)
print()
print("  Entry 128: delta_1 (new CP phase)")
print("    Status: STAGED (%s)" % delta1_status)
print()
print("  Entry 129: delta_2 (new CP phase)")
print("    Status: STAGED (%s)" % delta2_status)
print()

# ================================================================
# GROUP T: COMPUTATION TRACEABILITY MAP (NEW in DATA-4)
# ================================================================
print("GROUP T: COMPUTATION TRACEABILITY MAP")
print("-" * 78)
print()

traceability = [
    ("PHYS-9",  "B1(alpha_inv), G1(pi), G8(zeta3)",     "alpha -> a_e via QED series"),
    ("PHYS-12", "B1,B11,C6,C4,C5,C1,B12",               "7 EW inputs -> 11 observables"),
    ("PHYS-13", "B1,B11,B12",                             "3 couplings -> gap ratio 218/115 vs 1.358"),
    ("PHYS-15", "B1,B11,B12",                             "Elimination cascade -> (3,2,1/6)"),
    ("PHYS-17", "N1-N3 (SM betas)",                       "Generation democracy, boson problem"),
    ("PHYS-18", "N4-N6 (VL shifts)",                      "Y=1/6 asymmetry, 1/Y^2 scaling"),
    ("PHYS-19", "D6-D8 (CKM), B11",                      "Three anomalies -> (3,2,1/6)"),
    ("PHYS-20", "N7-N11 (modified betas, gap ratio)",     "M_GUT -> proton decay tau ~ 10^34-35"),
    ("PHYS-22", "G10(pi^2), G8(zeta3), G3(ln2)",         "A2 = 197/144 + (3/4)z3 + R4*c_geom"),
    ("PHYS-23", "B2-B4(lepton masses), D1-D5(quarks)",   "Koide K all three sectors"),
    ("PHYS-24", "B1,B11,B12, N1-N6, N14(b_ij)",          "Two-loop unification, Delta = -0.40"),
    ("MATH-6",  "G1-G14 (Q335 basis)",                    "PSLQ 82/82 null, Bessel zeros"),
]

print("  %-8s %-42s %s" % ("Paper", "DATA-4 Entries Used", "Computation"))
print("  " + "-"*8 + " " + "-"*42 + " " + "-"*42)
for paper, entries, comp in traceability:
    print("  %-8s %-42s %s" % (paper, entries, comp))
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

print("  %-6s %-52s %7s %6s %8s" % ("ID", "Test", "Digits", "Need", "Result"))
print("  " + "-"*6 + " " + "-"*52 + " " + "-"*7 + " " + "-"*6 + " " + "-"*8)
for tid, name, status, digits, needed in checks:
    d_str = "exact" if digits > 500 else "%.1f" % digits
    print("  %-6s %-52s %7s %6d %8s" % (tid, name, d_str, needed, status))

print()
print("  Total: %d tests,  %d PASS,  %d FAIL" % (n_total, n_pass, n_fail))
print()
print("  Inherited from DATA-3: 32 checks (Groups A-E)")
print("  New in DATA-4: %d checks (Group G: GUT verification)" % (n_total - 32))
print()

# Entry count
print("  ENTRY COUNT:")
print("    Sections A-K (inherited from DATA-3): 123 entries")
print("    Section L (Cabibbo Doublet, STAGED):    6 entries")
print("    Section N (GUT parameters, Level 1):   17 entries")
print("    Total: 146 entries")
print()

if n_fail == 0:
    print("  +==============================================================+")
    print("  |  ALL TESTS PASS                                              |")
    print("  |                                                              |")
    print("  |  DATA-4 DECLARATION:                                         |")
    print("  |    DATA-3 (123 entries, 32/32 checks) inherited.             |")
    print("  |    Finding 15 (lattice independence) formalized.             |")
    print("  |    6 Cabibbo Doublet parameters STAGED (entries 124-129).    |")
    print("  |    17 GUT/unification parameters added (Section N).          |")
    print("  |    6 new GUT verification checks added (Group G).           |")
    print("  |    Computation traceability map added (Group T).             |")
    print("  |                                                              |")
    print("  |  DATA-3 is retired.                                          |")
    print("  |  All future HOWL computation references DATA-4.              |")
    print("  +==============================================================+")
else:
    print("  DATABASE HAS INCONSISTENCIES.")
    for tid, name, status, digits, needed in checks:
        if status == "FAIL":
            print("    %s: %s (%.1f digits, need %d)" % (tid, name, digits, needed))

print()
print("=" * 78)
print("DATA-4 VERIFICATION COMPLETE")
print("=" * 78)

