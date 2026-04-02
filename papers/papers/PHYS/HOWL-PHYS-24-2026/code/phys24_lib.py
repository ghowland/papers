#!/usr/bin/env python3
"""
HOWL PHYS-24 PLATFORM LIBRARY
==============================
The single source of truth for all HOWL computation from Session 4 forward.

Every script imports this file:
    from phys24_lib import *

Every constant, every helper, every check function lives here.
If a value changes (new PDG, new CODATA), it changes HERE and nowhere else.
If a name becomes an alias, the mapping goes at the end of this file.

Registry: [@HOWL-PHYS24-LIB-2026]
Date: April 2 2026
Status: Operational platform
Test: phys24_lib_test.py (146/146 PASS)

Backed by: DATA-4 (146 entries, 38/38 checks), all Session 3 scripts (98/98 checks)

PRECISION CONVENTION:
  Every constant has two names:
    foo     = working value at published precision
    foo_full = maximum available precision (100+ digits for analyticals,
               full published digits for measured, exact for defined)
  If they are identical, foo_full = foo (alias, no duplication).
  Scripts use foo for normal work, foo_full for precision-critical paths.

RULES:
  - No floating point enters the computation chain. Fraction only.
  - mpf conversion happens at the display boundary via f2m().
  - This file imports only: sys, fractions.Fraction, mpmath.
  - No math module. No numpy. No scipy. No float().
  - Values only grow. Nothing is removed. Aliases go at the end.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, log10 as mlog10

mp.dps = 100


# ================================================================
# STANDARD HELPERS — identical in every script that imports this
# ================================================================

def f2m(f):
    """Fraction to mpf at working precision."""
    return mpf(f.numerator) / mpf(f.denominator)

def digits_of(got, expected):
    """Digits of agreement between got and expected.
    Returns mpf. Only valid when expected != 0.
    For quantities expected to be exactly zero, use chk_bool
    with an absolute tolerance instead."""
    if expected == mpf(0):
        if got == mpf(0):
            return mp.inf
        return mpf(0)
    rel = abs((got - expected) / expected)
    if rel == mpf(0):
        return mp.inf
    return -mlog10(rel)

def show(label, value):
    """Print a labeled value at standard precision (11 sf minimum)."""
    print("  %-40s %s" % (label, mp.nstr(value, 11)))

def chk(tag, got, expected, need, checks):
    """Standard numerical check. got and expected are mpf.
    d is always mpf (returned by digits_of)."""
    d = digits_of(got, expected)
    if d == mp.inf:
        d_str = "EXACT"
        ok = True
    else:
        d_str = mp.nstr(d, 4)
        ok = (d >= need)
    status = "PASS" if ok else "FAIL"
    checks.append((tag, status))
    print("  [%s] %s" % (status, tag))
    print("        expected: %s" % mp.nstr(expected, 11))
    print("        got:      %s" % mp.nstr(got, 11))
    print("        digits:   %s (need %d)" % (d_str, need))

def chk_exact(tag, got, expected, checks):
    """Exact Fraction check. Both sides must be Fraction."""
    ok = (got == expected)
    status = "PASS" if ok else "FAIL"
    checks.append((tag, status))
    print("  [%s] %s" % (status, tag))
    print("        expected: %s = %s" % (expected, mp.nstr(f2m(expected), 11)))
    print("        got:      %s = %s" % (got, mp.nstr(f2m(got), 11)))
    print("        match:    %s" % ("EXACT" if ok else "MISMATCH"))

def chk_bool(tag, condition, detail, checks):
    """Boolean check. Condition must be True to pass."""
    status = "PASS" if condition else "FAIL"
    checks.append((tag, status))
    print("  [%s] %s" % (status, tag))
    print("        %s" % detail)

def print_summary(checks):
    """Print the standard summary line. Call at end of every script."""
    print()
    n_pass = sum(1 for _, s in checks if s == "PASS")
    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print("  TOTAL: %d PASS, %d FAIL out of %d" % (n_pass, n_fail, len(checks)))


# ================================================================
# Q335 BASIS
# ================================================================

Q335 = 2**335


# ================================================================
# SECTION A: SI FUNDAMENTAL CONSTANTS (Type E — exact by definition)
# DATA-4 entries A1-A7. These are exact. _full = same value.
# ================================================================

c        = Fraction(299792458, 1)                         # A1: speed of light, m/s
h_planck = Fraction(662607015, 10**42)                    # A2: Planck constant, J*s
e_charge = Fraction(1602176634, 10**28)                   # A3: elementary charge, C
k_B      = Fraction(1380649, 10**29)                      # A4: Boltzmann constant, J/K
N_A      = Fraction(602214076, 1) * Fraction(10**15, 1)   # A5: Avogadro number, mol^-1
dv_Cs    = Fraction(9192631770, 1)                        # A6: Cs-133 hyperfine, Hz
K_cd     = Fraction(683, 1)                               # A7: luminous efficacy, lm/W

c_full        = c
h_planck_full = h_planck
e_charge_full = e_charge
k_B_full      = k_B
N_A_full      = N_A
dv_Cs_full    = dv_Cs
K_cd_full     = K_cd


# ================================================================
# SECTION B: MEASURED FUNDAMENTAL CONSTANTS (CODATA 2022, Type M)
# DATA-4 entries B1-B13. All digits are the full CODATA published
# precision. _full = same value (no higher precision exists).
# ================================================================

alpha_inv = Fraction(137035999177, 10**9)     # B1:  alpha^-1, 12 source digits
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

alpha_inv_full = alpha_inv
m_e_full       = m_e
m_mu_full      = m_mu
m_tau_full     = m_tau
m_p_full       = m_p
mp_me_full     = mp_me
R_inf_full     = R_inf
a_0_full       = a_0
a_e_full       = a_e
a_mu_full      = a_mu
sin2_tW_full   = sin2_tW
alpha_s_full   = alpha_s
mu_0_full      = mu_0


# ================================================================
# SECTION C: ELECTROWEAK OBSERVABLES (LEP/PDG, Type M)
# DATA-4 entries C1-C6. Full published precision. _full = same.
# ================================================================

M_Z       = Fraction(911876, 10)              # C1: Z mass, MeV, 6 sf
Gamma_Z   = Fraction(24952, 10)               # C2: Z width, MeV, 5 sf
M_W       = Fraction(803692, 10)              # C3: W mass, MeV, 6 sf
m_t       = Fraction(172570, 1)               # C4: top mass, MeV, 5 sf
m_H       = Fraction(125200, 1)               # C5: Higgs mass, MeV, 5 sf
G_F       = Fraction(11663788, 10**12)        # C6: Fermi constant, GeV^-2, 8 sf

M_Z_full     = M_Z
Gamma_Z_full = Gamma_Z
M_W_full     = M_W
m_t_full     = m_t
m_H_full     = m_H
G_F_full     = G_F


# ================================================================
# SECTION D: QUARK MASSES AND CKM (PDG 2024 / FLAG, Type M)
# DATA-4 entries D1-D11. Full published precision. _full = same.
# ================================================================

m_u       = Fraction(216, 100)                # D1: up quark MS-bar 2 GeV, MeV, 3 sf
m_d       = Fraction(470, 100)                # D2: down quark MS-bar 2 GeV, MeV, 3 sf
m_s       = Fraction(935, 10)                 # D3: strange MS-bar 2 GeV, MeV, 3 sf
m_c       = Fraction(1273, 1)                 # D4: charm MS-bar at m_c, MeV, 4 sf
m_b       = Fraction(4183, 1)                 # D5: bottom MS-bar at m_b, MeV, 4 sf
sin_t12   = Fraction(22501, 100000)           # D6: sin theta_12 Cabibbo, 5 sf
sin_t23   = Fraction(4182, 100000)            # D7: sin theta_23 CKM, 4 sf
sin_t13   = Fraction(3685, 1000000)           # D8: sin theta_13 CKM, 4 sf
mc_ms     = Fraction(11783, 1000)             # D9:  m_c/m_s lattice FLAG, 5 sf [INDEPENDENT]
mb_mc     = Fraction(4578, 1000)              # D10: m_b/m_c lattice FLAG, 4 sf [INDEPENDENT]
mu_md     = Fraction(485, 1000)               # D11: m_u/m_d lattice FLAG, 3 sf [INDEPENDENT]

m_u_full     = m_u
m_d_full     = m_d
m_s_full     = m_s
m_c_full     = m_c
m_b_full     = m_b
sin_t12_full = sin_t12
sin_t23_full = sin_t23
sin_t13_full = sin_t13
mc_ms_full   = mc_ms
mb_mc_full   = mb_mc
mu_md_full   = mu_md


# ================================================================
# SECTION E: NUCLEAR/HADRON MASSES (Type M)
# DATA-4 entries E1-E8. Full published precision. _full = same.
# ================================================================

m_n        = Fraction(93956542194, 10**8)     # E1: neutron mass, MeV, 11 sf
mn_mp_diff = Fraction(129333251, 10**8)       # E2: m_n - m_p, MeV, 8 sf
m_pi_p     = Fraction(13957039, 10**5)        # E3: charged pion, MeV, 8 sf
m_pi_0     = Fraction(1349770, 10**4)         # E4: neutral pion, MeV, 7 sf
m_K_p      = Fraction(493677, 10**3)          # E5: charged kaon, MeV, 6 sf
m_D        = Fraction(187561294500, 10**8)    # E6: deuteron, MeV, 12 sf
m_He4      = Fraction(37273794118, 10**7)     # E7: helium-4, MeV, 10 sf
E_D        = Fraction(222456614, 10**8)       # E8: deuteron binding, MeV, 8 sf

m_n_full        = m_n
mn_mp_diff_full = mn_mp_diff
m_pi_p_full     = m_pi_p
m_pi_0_full     = m_pi_0
m_K_p_full      = m_K_p
m_D_full        = m_D
m_He4_full      = m_He4
E_D_full        = E_D


# ================================================================
# SECTION F: ATOMIC SPECTROSCOPY (Type M)
# DATA-4 entry F1. Full published precision. _full = same.
# ================================================================

H_1S2S = Fraction(2466061413187018, 1)        # F1: H 1S-2S, Hz, 16 sf

H_1S2S_full = H_1S2S


# ================================================================
# SECTION G: Q335 ANALYTICAL CONSTANTS (Type A, 100+ digits)
# DATA-4 entries G1-G14 plus extended basis.
# Numerators verified against mpmath at 100+ digits.
# First 20 digits shown in comment for corruption check.
#
# Working values (p_foo) and full values (p_foo_full) are the same
# for all constants EXCEPT the three that were recomputed:
#   Li4(1/2), K(k2=3/4), E(k2=3/4)
# For those three, p_foo is the original (lower precision) and
# p_foo_full is the recomputed 100-digit version.
# The Fraction variables use the _full numerators throughout.
# ================================================================

# G1: pi — first 20: 21988642587319235101...
p_pi    = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_pi_full = p_pi

# G2: e — first 20: 19025804478276920258...
p_e     = 190258044782769202588129925521314757831284456026137946619894798297742927086075833929023100244479638112
p_e_full = p_e

# G3: ln(2) — first 20: 48514773537953331556...
p_ln2   = 48514773537953331556699584584828624926234404478840896710102416707062925979128257345653169777835518667
p_ln2_full = p_ln2

# G4: sqrt(2) — first 20: 98983668457552556369...
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506
p_sqrt2_full = p_sqrt2

# G5: sqrt(3) — first 20: 12122974029491289523...
p_sqrt3 = 121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154
p_sqrt3_full = p_sqrt3

# G6: sqrt(5) — first 20: 15650692174241595562...
p_sqrt5 = 156506921742415955629073428753920319855839958763030979672136303700342980177725995879548801953564656455
p_sqrt5_full = p_sqrt5

# G7: sqrt(7) — first 20: 18518148712709215377...
p_sqrt7 = 185181487127092153770432076884133468631121666203542492409943031514633653137939942068870811445311050320
p_sqrt7_full = p_sqrt7

# G8: phi — first 20: 11324947246773616860...
p_phi   = 113249472467736168604496750010842101773570690275806888818880481552730738076053012711350611809151189412
p_phi_full = p_phi

# G9: zeta(3) — first 20: 84134394645319852071...
p_zeta3 = 84134394645319852071522700710261177454128732241134555234516209978359598548186272768450592529361881680
p_zeta3_full = p_zeta3

# G10: zeta(5) — first 20: 72576671487518636549...
p_zeta5 = 72576671487518636549061590533542457287978428544763113598602740326685645428855657003519154452098433211
p_zeta5_full = p_zeta5

# G11: pi^2 — first 20: 69079358014733772680...
p_pi2   = 690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976
p_pi2_full = p_pi2

# G12: zeta(2) = pi^2/6 — first 20: 11513226335788962113...
p_zeta2 = 115132263357889621134046274580724461723153559023165751333812058739254898959299399994115897270944762663
p_zeta2_full = p_zeta2

# G16: zeta(7) — first 20: 70576406009217185140...
p_zeta7 = 70576406009217185140477287997534501576465097090915039072079935823330498368871276340729511665245547897
p_zeta7_full = p_zeta7

# G17: zeta(9) — first 20: 70132594670320295983...
p_zeta9 = 70132594670320295983139855937304501893252881833203086513273190166429397615458038473270078404250783123
p_zeta9_full = p_zeta9

# G18: Li4(1/2) — first 20: 36219406486600619537...
# Original: 99.93 digits (300 series terms). Full: 101+ digits (500 terms).
p_li4      = 36219406486600619537883622883703292936779255100080725994962678520983767482244581297270363585520219319
p_li4_full = 36219406486600619537883622883703292936779255100080725994962678520983767482244581297270363585520219323

# G19: Li5(1/2) — first 20: 35583985133688170166...
p_li5   = 35583985133688170166306037175162928642925623616862298753523275026390371034409012151295446453318371300
p_li5_full = p_li5

# G20: Li6(1/2) — first 20: 35282656774609749602...
p_li6   = 35282656774609749602762817166109208543702553381047559953228866852351129819554712308313482817872368698
p_li6_full = p_li6

# G21: Li7(1/2) — first 20: 35137014959475068515...
p_li7   = 35137014959475068515954957014616125661516964672001297075936753763641708154735402197723626031134809681
p_li7_full = p_li7

# G22: Catalan — first 20: 64110285111693582641...
p_cat   = 64110285111693582641294563817927086726382757371148180987419195376360958765615024299223500526530512841
p_cat_full = p_cat

# G23: e^pi — first 20: 16196638954568755371...
p_epi   = 1619663895456875537109657111692739211478931048048038025064408441944407978010684548404551575192727763397
p_epi_full = p_epi

# G24: ln(3) — first 20: 76894096788635086096...
p_ln3   = 76894096788635086096158790585166115140009649181250777410832538562395270797691729322128736655820466233
p_ln3_full = p_ln3

# G25: ln(5) — first 20: 11264781569487179915...
p_ln5   = 112647815694871799155432631259623524245586803429977893615314774516410370135500048646041895614334987799
p_ln5_full = p_ln5

# Elliptic integrals at rational k^2
# G26: K(k2=1/4) — 100+ digits
p_K_quarter = 117989077931746246669536463608571504131360583333027243232890507036739190774329661417331393753625714572
p_K_quarter_full = p_K_quarter

# G27: K(k2=1/2) — 100+ digits
p_K_half    = 129770437815336149625337005383682890154430113513873971233598625754177767600926159185769969469708490140
p_K_half_full = p_K_half

# G28: K(k2=3/4) — Original: 65 digits (500 terms). Full: 102+ digits (800 terms).
p_K_3qtr      = 150938893215984029553377685418519737141065147186163571808125275364447868626347932829365815859373329213
p_K_3qtr_full = 150938893215984029553377685418519737141065147186163571808125275365154423280994971525495673821397923285

# G29: E(k2=1/4) — 100+ digits
p_E_quarter = 102710648991018944512111562171582647666468378205524378904250096462468756583900713021496404009967434392
p_E_quarter_full = p_E_quarter

# G30: E(k2=1/2) — 100+ digits
p_E_half    = 94534297847848588347052844773285508650235488054028753181946155149242607686796867398257970751308038442
p_E_half_full = p_E_half

# G31: E(k2=3/4) — Original: 68 digits (500 terms). Full: 101+ digits (800 terms).
p_E_3qtr      = 84764261569662347707538768367490464738685729133628558884550025911328567207530988965657970144420559883
p_E_3qtr_full = 84764261569662347707538768367490464738685729133628558884550025911327865499334760166418456672850663532


# Build Fraction variables from FULL numerators throughout
pi_f    = Fraction(p_pi_full, Q335)        # G1
e_f     = Fraction(p_e_full, Q335)         # G2
ln2_f   = Fraction(p_ln2_full, Q335)       # G3
sqrt2_f = Fraction(p_sqrt2_full, Q335)     # G4
sqrt3_f = Fraction(p_sqrt3_full, Q335)     # G5
sqrt5_f = Fraction(p_sqrt5_full, Q335)     # G6
sqrt7_f = Fraction(p_sqrt7_full, Q335)     # G7
phi_f   = Fraction(p_phi_full, Q335)       # G8
zeta3_f = Fraction(p_zeta3_full, Q335)     # G9
zeta5_f = Fraction(p_zeta5_full, Q335)     # G10
pi2_f   = Fraction(p_pi2_full, Q335)       # G11
zeta2_f = Fraction(p_zeta2_full, Q335)     # G12

# G13-G15: derived from above
R2_f    = pi_f / 4                         # G13: R_2 = pi/4
R4_f    = pi2_f / 32                       # G14: R_4 = pi^2/32
twopi_f = 2 * pi_f                         # G15: 2*pi

# Extended basis
zeta7_f = Fraction(p_zeta7_full, Q335)     # G16
zeta9_f = Fraction(p_zeta9_full, Q335)     # G17
li4_f   = Fraction(p_li4_full, Q335)       # G18: uses FULL numerator (101+ digits)
li5_f   = Fraction(p_li5_full, Q335)       # G19
li6_f   = Fraction(p_li6_full, Q335)       # G20
li7_f   = Fraction(p_li7_full, Q335)       # G21
cat_f   = Fraction(p_cat_full, Q335)       # G22
epi_f   = Fraction(p_epi_full, Q335)       # G23
ln3_f   = Fraction(p_ln3_full, Q335)       # G24
ln5_f   = Fraction(p_ln5_full, Q335)       # G25

K_quarter_f = Fraction(p_K_quarter_full, Q335)  # G26
K_half_f    = Fraction(p_K_half_full, Q335)     # G27
K_3qtr_f    = Fraction(p_K_3qtr_full, Q335)    # G28: uses FULL numerator (102+ digits)
E_quarter_f = Fraction(p_E_quarter_full, Q335)  # G29
E_half_f    = Fraction(p_E_half_full, Q335)     # G30
E_3qtr_f    = Fraction(p_E_3qtr_full, Q335)    # G31: uses FULL numerator (101+ digits)

# _full aliases for Fraction variables (all already use full numerators)
pi_f_full    = pi_f
e_f_full     = e_f
ln2_f_full   = ln2_f
sqrt2_f_full = sqrt2_f
sqrt3_f_full = sqrt3_f
sqrt5_f_full = sqrt5_f
sqrt7_f_full = sqrt7_f
phi_f_full   = phi_f
zeta3_f_full = zeta3_f
zeta5_f_full = zeta5_f
pi2_f_full   = pi2_f
zeta2_f_full = zeta2_f
R2_f_full    = R2_f
R4_f_full    = R4_f
twopi_f_full = twopi_f
zeta7_f_full = zeta7_f
zeta9_f_full = zeta9_f
li4_f_full   = li4_f
li5_f_full   = li5_f
li6_f_full   = li6_f
li7_f_full   = li7_f
cat_f_full   = cat_f
epi_f_full   = epi_f
ln3_f_full   = ln3_f
ln5_f_full   = ln5_f
K_quarter_f_full = K_quarter_f
K_half_f_full    = K_half_f
K_3qtr_f_full    = K_3qtr_f
E_quarter_f_full = E_quarter_f
E_half_f_full    = E_half_f
E_3qtr_f_full    = E_3qtr_f


# ================================================================
# SECTION K: DIMENSIONLESS MASS RATIOS (Type M)
# DATA-4 entries K1-K8. Full published precision. _full = same.
# ================================================================

mmu_me   = Fraction(20676828270846717969, 10**17)   # K1: m_mu/m_e, 10 sf
mtau_me  = Fraction(347723, 100)                     # K2: m_tau/m_e, 6 sf
mtau_mmu = Fraction(168170, 10000)                   # K3: m_tau/m_mu, 5 sf
mn_mp    = Fraction(10013784194633623804, 10**19)    # K4: m_n/m_p, 11 sf
MW_MZ    = Fraction(881361, 10**6)                   # K5: M_W/M_Z, 6 sf
mH_MZ    = Fraction(137299, 10**5)                   # K6: m_H/M_Z, 5 sf
mt_MZ    = Fraction(189247, 10**5)                   # K7: m_t/M_Z, 5 sf
K_koide  = Fraction(6666605115, 10**10)              # K8: Koide ratio K(e,mu,tau), 6 sf

mmu_me_full   = mmu_me
mtau_me_full  = mtau_me
mtau_mmu_full = mtau_mmu
mn_mp_full    = mn_mp
MW_MZ_full    = MW_MZ
mH_MZ_full    = mH_MZ
mt_MZ_full    = mt_MZ
K_koide_full  = K_koide


# ================================================================
# SECTION L: CABIBBO DOUBLET PARAMETERS (Type G — STAGED)
# DATA-4 entries L1-L6 (entries 124-129)
# ================================================================

M_VL_lo = Fraction(1500000, 1)       # L1: 1.5 TeV lower bound (LHC)
M_VL_hi = Fraction(6000000, 1)       # L1: 6.0 TeV upper bound (perturbativity)
theta14_est = Fraction(45, 1000)     # L2: ~0.045 from CKM deficit

M_VL_lo_full     = M_VL_lo
M_VL_hi_full     = M_VL_hi
theta14_est_full = theta14_est


# ================================================================
# SECTION N: GUT AND UNIFICATION PARAMETERS (Type D — Derived)
# DATA-4 entries N1-N17. All exact Fractions. _full = same.
# ================================================================

b1_SM = Fraction(41, 10)             # N1: U(1)_Y, GUT normalization
b2_SM = Fraction(-19, 6)             # N2: SU(2)_L
b3_SM = Fraction(-7, 1)              # N3: SU(3)_c

db1_VL = Fraction(1, 15)             # N4: VL U(1) shift
db2_VL = Fraction(1, 1)              # N5: VL SU(2) shift
db3_VL = Fraction(1, 3)              # N6: VL SU(3) shift

b1_mod = b1_SM + db1_VL              # N7: = 25/6
b2_mod = b2_SM + db2_VL              # N8: = -13/6
b3_mod = b3_SM + db3_VL              # N9: = -20/3

gap_SM   = (b1_SM - b2_SM) / (b2_SM - b3_SM)      # N10: = 218/115
gap_VL   = (b1_mod - b2_mod) / (b2_mod - b3_mod)   # N11: = 38/27
gap_MSSM = Fraction(7, 5)                           # N12: MSSM gap ratio

# N13: Measured gap ratio (Derived from Level 2 couplings)
alpha_frac = Fraction(1, 1) / alpha_inv
cos2_tW    = Fraction(1, 1) - sin2_tW
alpha_1_GUT = Fraction(5, 3) * alpha_frac / cos2_tW
alpha_2_GUT = alpha_frac / sin2_tW
alpha_3_GUT = alpha_s
inv_a1 = Fraction(1, 1) / alpha_1_GUT
inv_a2 = Fraction(1, 1) / alpha_2_GUT
inv_a3 = Fraction(1, 1) / alpha_3_GUT
gap_measured = (inv_a1 - inv_a2) / (inv_a2 - inv_a3)   # N13: ~1.358

# N14: Two-loop SM b_ij matrix (Level 1, exact)
b_ij_SM = [
    [Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)],
    [Fraction(9, 10),   Fraction(35, 6),  Fraction(12, 1)],
    [Fraction(11, 10),  Fraction(9, 2),   Fraction(-26, 1)],
]

# N15-N17: Two-loop unification results at M_VL = 500 GeV
delta_1loop = Fraction(-117, 100)        # N15: one-loop miss
delta_2loop = Fraction(-40, 100)         # N16: two-loop miss
twoloop_improvement = Fraction(66, 100)  # N17: 66% improvement

# _full aliases (all exact Fractions — same values)
b1_SM_full  = b1_SM
b2_SM_full  = b2_SM
b3_SM_full  = b3_SM
db1_VL_full = db1_VL
db2_VL_full = db2_VL
db3_VL_full = db3_VL
b1_mod_full = b1_mod
b2_mod_full = b2_mod
b3_mod_full = b3_mod
gap_SM_full      = gap_SM
gap_VL_full      = gap_VL
gap_MSSM_full    = gap_MSSM
gap_measured_full = gap_measured


# ================================================================
# DERIVED COUPLING CONSTANTS
# ================================================================

alpha_em = alpha_frac
alpha_em_full = alpha_em


# ================================================================
# KOIDE DERIVED (from DATA-2 Addendum, Type K)
# ================================================================

a2_lep  = Fraction(20000, 10000)      # a^2(leptons) ~ 2.0000 (6 sf)
a2_down = Fraction(23877, 10000)      # a^2(down quarks) ~ 2.3877 (3 sf)
a2_up   = Fraction(30928, 10000)      # a^2(up quarks) ~ 3.0928 (3 sf)

a2_lep_full  = a2_lep
a2_down_full = a2_down
a2_up_full   = a2_up


# ================================================================
# NAMED CONSTANTS (series vocabulary)
# ================================================================

CD_SU3 = 3                            # Cabibbo Doublet: color triplet
CD_SU2 = 2                            # Cabibbo Doublet: weak doublet
CD_Y   = Fraction(1, 6)              # Cabibbo Doublet: hypercharge 1/6

db_per_gen = (Fraction(4, 3), Fraction(4, 3), Fraction(4, 3))

casimir_gap = Fraction(2, 1)          # pure-gauge gap ratio = 2

hbar = h_planck / (2 * pi_f)         # reduced Planck (Fraction, Q335 precision)
hbar_full = hbar


# ================================================================
# NAME MAPPINGS AND ALIASES
# If a name collapses to an existing value, map it here.
# No equations or code above this section ever changes.
# ================================================================

# (none yet — this section grows as the series evolves)


# ================================================================
# SELF-TEST (run this file directly to verify internal consistency)
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHYS24_LIB SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    chk_exact("SM gap ratio = 218/115",
              gap_SM, Fraction(218, 115), checks)

    chk_exact("CD gap ratio = 38/27",
              gap_VL, Fraction(38, 27), checks)

    chk_exact("MSSM gap ratio = 7/5",
              gap_MSSM, Fraction(7, 5), checks)

    chk_exact("b1_mod = 25/6",
              b1_mod, Fraction(25, 6), checks)

    chk_exact("b2_mod = -13/6",
              b2_mod, Fraction(-13, 6), checks)

    chk_exact("b3_mod = -20/3",
              b3_mod, Fraction(-20, 3), checks)

    old_dps = mp.dps
    mp.dps = 120
    from mpmath import pi as mpi
    chk("Q335 pi matches mpmath",
        f2m(pi_f), mpi, 100, checks)
    mp.dps = old_dps

    chk("R2 = pi/4",
        f2m(R2_f), f2m(pi_f) / 4, 100, checks)

    chk("R4 = pi^2/32",
        f2m(R4_f), f2m(pi2_f) / 32, 100, checks)

    chk("zeta(2) ~ pi^2/6",
        f2m(zeta2_f), f2m(pi2_f / 6), 99, checks)

    from mpmath import sqrt as msqrt
    sum_m = f2m(m_e + m_mu + m_tau)
    sum_sq = msqrt(f2m(m_e)) + msqrt(f2m(m_mu)) + msqrt(f2m(m_tau))
    K_comp = sum_m / (sum_sq * sum_sq)
    chk("Koide K(e,mu,tau) from masses",
        K_comp, f2m(K_koide), 6, checks)

    chk_exact("Pure-gauge Casimir gap = 2",
              casimir_gap, Fraction(2, 1), checks)

    chk_exact("Per-gen db1 = 4/3",
              db_per_gen[0], Fraction(4, 3), checks)

    chk_exact("Per-gen db2 = 4/3",
              db_per_gen[1], Fraction(4, 3), checks)

    chk_exact("Per-gen db3 = 4/3",
              db_per_gen[2], Fraction(4, 3), checks)

    chk_bool("Measured gap ratio in [1.2, 1.5]",
             1.2 < float(f2m(gap_measured)) < 1.5,
             "gap = %s" % mp.nstr(f2m(gap_measured), 7), checks)

    # Verify the three recomputed constants at 100 digits
    mp.dps = 120
    from mpmath import polylog, ellipk, ellipe
    chk("Li4(1/2) full precision",
        f2m(li4_f), polylog(4, mpf(1)/2), 100, checks)
    chk("K(k2=3/4) full precision",
        f2m(K_3qtr_f), ellipk(mpf(3)/4), 100, checks)
    chk("E(k2=3/4) full precision",
        f2m(E_3qtr_f), ellipe(mpf(3)/4), 100, checks)
    mp.dps = 100

    print_summary(checks)

    print()
    print("=" * 70)
    print("PHYS24_LIB SELF-TEST COMPLETE")
    print("=" * 70)

    