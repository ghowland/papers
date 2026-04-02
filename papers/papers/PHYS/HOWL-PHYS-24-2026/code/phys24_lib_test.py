#!/usr/bin/env python3
"""
HOWL PHYS-24 PLATFORM PRECISION TEST
======================================
Comprehensive verification that phys24_lib.py stages every value
at the precision established by MATH-2, MATH-4, and DATA-4.

This is not a unit test. It is a human-readable precision report.
Every value is tested. Every digit count is printed. Every failure
is reported with full context. Nothing stops on failure.

Run: python phys24_lib_test.py
Requires: phys24_lib.py in the same directory.

Backed by: DATA-4 (38/38), q_335_basis.py (22/22), more_constants_335_basis.py (35/35)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from mpmath import (pi as mpi, e as me, euler as mgamma,
                    log as mlog, sqrt as msqrt, zeta as mzeta,
                    phi as mphi, polylog, catalan as mcat,
                    ellipk, ellipe, exp as mexp)

mp.dps = 120  # extra headroom for reference values


# ================================================================
# TEST INFRASTRUCTURE
# ================================================================

checks = []
section_counts = {}

def section(name):
    """Print a section header and track check counts."""
    print()
    print("=" * 70)
    print(name)
    print("=" * 70)
    print()
    section_counts[name] = 0

def note_check():
    """Increment the section counter for the most recent section."""
    key = list(section_counts.keys())[-1]
    section_counts[key] = section_counts[key] + 1


# ================================================================
# PART 1: Q335 ANALYTICAL BASIS — 100-DIGIT PRECISION
# Every Q335 numerator vs mpmath native computation.
# All constants now at 100+ digits after recomputation of
# Li4(1/2), K(k2=3/4), E(k2=3/4) with sufficient series terms.
# ================================================================

section("PART 1: Q335 ANALYTICAL CONSTANTS vs MPMATH (need 100 digits)")

q335_tests = [
    ("G1:  pi",           pi_f,         mpi,                    100),
    ("G2:  e",            e_f,          me,                     100),
    ("G3:  ln(2)",        ln2_f,        mlog(2),                100),
    ("G4:  sqrt(2)",      sqrt2_f,      msqrt(2),               100),
    ("G5:  sqrt(3)",      sqrt3_f,      msqrt(3),               100),
    ("G6:  sqrt(5)",      sqrt5_f,      msqrt(5),               100),
    ("G7:  sqrt(7)",      sqrt7_f,      msqrt(7),               100),
    ("G8:  phi",          phi_f,        mphi,                   100),
    ("G9:  zeta(3)",      zeta3_f,      mzeta(3),               100),
    ("G10: zeta(5)",      zeta5_f,      mzeta(5),               100),
    ("G11: pi^2",         pi2_f,        mpi**2,                 100),
    ("G12: zeta(2)",      zeta2_f,      mpi**2 / 6,             100),
    ("G13: R2 = pi/4",    R2_f,         mpi / 4,                100),
    ("G14: R4 = pi^2/32", R4_f,         mpi**2 / 32,            100),
    ("G15: 2*pi",         twopi_f,      2 * mpi,                100),
    ("G16: zeta(7)",      zeta7_f,      mzeta(7),               100),
    ("G17: zeta(9)",      zeta9_f,      mzeta(9),               100),
    ("G18: Li4(1/2)",     li4_f,        polylog(4, mpf(1)/2),   100),
    ("G19: Li5(1/2)",     li5_f,        polylog(5, mpf(1)/2),   100),
    ("G20: Li6(1/2)",     li6_f,        polylog(6, mpf(1)/2),   100),
    ("G21: Li7(1/2)",     li7_f,        polylog(7, mpf(1)/2),   100),
    ("G22: Catalan",      cat_f,        mcat,                   100),
    ("G23: e^pi",         epi_f,        mexp(mpi),              100),
    ("G24: ln(3)",        ln3_f,        mlog(3),                100),
    ("G25: ln(5)",        ln5_f,        mlog(5),                100),
    ("G26: K(k2=1/4)",    K_quarter_f,  ellipk(mpf(1)/4),       100),
    ("G27: K(k2=1/2)",    K_half_f,     ellipk(mpf(1)/2),       100),
    ("G28: K(k2=3/4)",    K_3qtr_f,     ellipk(mpf(3)/4),       100),
    ("G29: E(k2=1/4)",    E_quarter_f,  ellipe(mpf(1)/4),       100),
    ("G30: E(k2=1/2)",    E_half_f,     ellipe(mpf(1)/2),       100),
    ("G31: E(k2=3/4)",    E_3qtr_f,     ellipe(mpf(3)/4),       100),
]

for tag, frac_val, ref_val, need in q335_tests:
    chk(tag, f2m(frac_val), ref_val, need, checks)
    note_check()


# ================================================================
# PART 2: Q335 ALGEBRAIC IDENTITIES — EXACT OR NEAR-EXACT
# ================================================================

section("PART 2: Q335 ALGEBRAIC IDENTITIES")

chk("pi^2 vs pi*pi (Q335)",
    f2m(pi2_f), f2m(pi_f * pi_f), 99, checks)
note_check()

chk("zeta(2) vs pi^2/6 (Q335)",
    f2m(zeta2_f), f2m(pi2_f / 6), 99, checks)
note_check()

chk_exact("2*pi = 2 * pi_f",
          twopi_f, 2 * pi_f, checks)
note_check()

chk_exact("R2 = pi_f / 4",
          R2_f, pi_f / 4, checks)
note_check()

chk_exact("R4 = pi2_f / 32",
          R4_f, pi2_f / 32, checks)
note_check()

chk("phi vs (1+sqrt5)/2 (Q335)",
    f2m(phi_f), f2m((Fraction(1) + sqrt5_f) / 2), 100, checks)
note_check()


# ================================================================
# PART 3: MEASURED CONSTANTS — DECIMAL RECONSTRUCTION
# Every Fraction reconstructs to the correct published value
# at all source digits. No scientific notation. Full decimal strings.
# ================================================================

section("PART 3: MEASURED CONSTANTS — FULL PRECISION RECONSTRUCTION")

measured_tests = [
    ("B1:  alpha^-1",           alpha_inv,  "137.035999177",                              9),
    ("B2:  m_e (MeV)",          m_e,        "0.51099895069",                              9),
    ("B3:  m_mu (MeV)",         m_mu,       "105.6583755",                                8),
    ("B4:  m_tau (MeV)",        m_tau,      "1776.86",                                    5),
    ("B5:  m_p (MeV)",          m_p,        "938.27208943",                               9),
    ("B6:  m_p/m_e",            mp_me,      "1836.15267343",                             10),
    ("B7:  R_inf (m^-1)",       R_inf,      "10973731.568157",                           10),
    ("B8:  a_0 (m)",            a_0,        "0.0000000000529177210544",                   9),
    ("B9:  a_e",                a_e,        "0.00115965218059",                           9),
    ("B10: a_mu",               a_mu,       "0.00116592059",                              7),
    ("B11: sin2_tW",            sin2_tW,    "0.23122",                                    4),
    ("B12: alpha_s",            alpha_s,    "0.1180",                                     3),
    ("B13: mu_0 (N/A^2)",       mu_0,       "0.00000125663706127",                        9),
    ("C1:  M_Z (MeV)",          M_Z,        "91187.6",                                    5),
    ("C2:  Gamma_Z (MeV)",      Gamma_Z,    "2495.2",                                     4),
    ("C3:  M_W (MeV)",          M_W,        "80369.2",                                    5),
    ("C4:  m_t (MeV)",          m_t,        "172570",                                     5),
    ("C5:  m_H (MeV)",          m_H,        "125200",                                     5),
    ("C6:  G_F (GeV^-2)",       G_F,        "0.000011663788",                             6),
    ("D1:  m_u (MeV)",          m_u,        "2.16",                                       2),
    ("D2:  m_d (MeV)",          m_d,        "4.70",                                       2),
    ("D3:  m_s (MeV)",          m_s,        "93.5",                                       2),
    ("D4:  m_c (MeV)",          m_c,        "1273",                                       3),
    ("D5:  m_b (MeV)",          m_b,        "4183",                                       3),
    ("D6:  sin_t12",            sin_t12,    "0.22501",                                    4),
    ("D7:  sin_t23",            sin_t23,    "0.04182",                                    3),
    ("D8:  sin_t13",            sin_t13,    "0.003685",                                   3),
    ("D9:  m_c/m_s FLAG",       mc_ms,      "11.783",                                     4),
    ("D10: m_b/m_c FLAG",       mb_mc,      "4.578",                                      3),
    ("D11: m_u/m_d FLAG",       mu_md,      "0.485",                                      2),
    ("E1:  m_n (MeV)",          m_n,        "939.56542194",                               9),
    ("E2:  m_n-m_p (MeV)",      mn_mp_diff, "1.29333251",                                7),
    ("E3:  m_pi+ (MeV)",        m_pi_p,     "139.57039",                                  7),
    ("E4:  m_pi0 (MeV)",        m_pi_0,     "134.9770",                                   5),
    ("E5:  m_K+ (MeV)",         m_K_p,      "493.677",                                    5),
    ("E6:  m_D (MeV)",          m_D,        "1875.61294500",                              9),
    ("E7:  m_He4 (MeV)",        m_He4,      "3727.3794118",                               8),
    ("E8:  E_D (MeV)",          E_D,        "2.22456614",                                 7),
    ("F1:  H 1S-2S (Hz)",       H_1S2S,     "2466061413187018",                          15),
    ("K1:  m_mu/m_e",           mmu_me,     "206.76828270846717969",                     10),
    ("K2:  m_tau/m_e",          mtau_me,    "3477.23",                                    5),
    ("K3:  m_tau/m_mu",         mtau_mmu,   "16.8170",                                    4),
    ("K4:  m_n/m_p",            mn_mp,      "1.0013784194633623804",                     11),
    ("K5:  M_W/M_Z",            MW_MZ,      "0.881361",                                   5),
    ("K6:  m_H/M_Z",            mH_MZ,      "1.37299",                                    4),
    ("K7:  m_t/M_Z",            mt_MZ,      "1.89247",                                    4),
    ("K8:  Koide K(e,mu,tau)",   K_koide,    "0.6666605115",                               6),
]

for tag, frac_val, ref_str, need in measured_tests:
    chk(tag, f2m(frac_val), mpf(ref_str), need, checks)
    note_check()


# ================================================================
# PART 4: SI EXACT CONSTANTS — MUST BE EXACT INTEGERS OR RATIONALS
# ================================================================

section("PART 4: SI EXACT CONSTANTS")

chk_exact("A1: c = 299792458",
          c, Fraction(299792458, 1), checks)
note_check()

chk_exact("A2: h = 662607015/10^42",
          h_planck, Fraction(662607015, 10**42), checks)
note_check()

chk_exact("A3: e = 1602176634/10^28",
          e_charge, Fraction(1602176634, 10**28), checks)
note_check()

chk_exact("A4: k_B = 1380649/10^29",
          k_B, Fraction(1380649, 10**29), checks)
note_check()

chk_exact("A6: dv_Cs = 9192631770",
          dv_Cs, Fraction(9192631770, 1), checks)
note_check()

chk_exact("A7: K_cd = 683",
          K_cd, Fraction(683, 1), checks)
note_check()


# ================================================================
# PART 5: GUT PARAMETER IDENTITIES — EXACT FRACTION ARITHMETIC
# ================================================================

section("PART 5: GUT PARAMETERS (exact Fraction)")

chk_exact("N1:  b1_SM = 41/10",  b1_SM,  Fraction(41, 10), checks);  note_check()
chk_exact("N2:  b2_SM = -19/6",  b2_SM,  Fraction(-19, 6), checks);  note_check()
chk_exact("N3:  b3_SM = -7",     b3_SM,  Fraction(-7, 1),  checks);  note_check()
chk_exact("N4:  db1_VL = 1/15",  db1_VL, Fraction(1, 15),  checks);  note_check()
chk_exact("N5:  db2_VL = 1",     db2_VL, Fraction(1, 1),   checks);  note_check()
chk_exact("N6:  db3_VL = 1/3",   db3_VL, Fraction(1, 3),   checks);  note_check()
chk_exact("N7:  b1_mod = 25/6",  b1_mod, Fraction(25, 6),  checks);  note_check()
chk_exact("N8:  b2_mod = -13/6", b2_mod, Fraction(-13, 6), checks);  note_check()
chk_exact("N9:  b3_mod = -20/3", b3_mod, Fraction(-20, 3), checks);  note_check()
chk_exact("N10: gap_SM = 218/115",  gap_SM,   Fraction(218, 115), checks); note_check()
chk_exact("N11: gap_VL = 38/27",    gap_VL,   Fraction(38, 27),   checks); note_check()
chk_exact("N12: gap_MSSM = 7/5",    gap_MSSM, Fraction(7, 5),     checks); note_check()

chk_exact("N14: b_ij[0][0] = 199/50", b_ij_SM[0][0], Fraction(199, 50), checks); note_check()
chk_exact("N14: b_ij[1][2] = 12",     b_ij_SM[1][2], Fraction(12, 1),   checks); note_check()
chk_exact("N14: b_ij[2][2] = -26",    b_ij_SM[2][2], Fraction(-26, 1),  checks); note_check()


# ================================================================
# PART 6: MASS RATIO CROSS-CHECKS (DATA-4 Group A)
# ================================================================

section("PART 6: MASS RATIO CROSS-CHECKS")

chk("A1: m_p/m_e vs mp_me",     f2m(m_p / m_e),    f2m(mp_me),      11, checks); note_check()
chk("A2: m_mu/m_e vs mmu_me",   f2m(m_mu / m_e),   f2m(mmu_me),     10, checks); note_check()
chk("A3: m_tau/m_e vs mtau_me", f2m(m_tau / m_e),  f2m(mtau_me),      6, checks); note_check()
chk("A5: m_n/m_p vs mn_mp",     f2m(m_n / m_p),    f2m(mn_mp),       11, checks); note_check()
chk("A6: M_W/M_Z vs MW_MZ",     f2m(M_W / M_Z),    f2m(MW_MZ),        6, checks); note_check()
chk("A7: m_n - m_p vs mn_mp_diff", f2m(m_n - m_p), f2m(mn_mp_diff),   8, checks); note_check()


# ================================================================
# PART 7: PHYSICAL RELATIONS (DATA-4 Group C)
# ================================================================

section("PART 7: PHYSICAL RELATIONS")

m_e_kg = m_e * Fraction(10**6, 1) * e_charge / (c * c)
R_inf_comp = alpha_frac * alpha_frac * m_e_kg * c / (2 * h_planck)

chk("C1: R_inf = alpha^2 m_e c/(2h)",
    f2m(R_inf_comp), f2m(R_inf), 11, checks)
note_check()

hbar_comp = h_planck / (2 * pi_f)
a_0_comp = hbar_comp / (m_e_kg * c * alpha_frac)

chk("C2: a_0 = hbar/(m_e c alpha)",
    f2m(a_0_comp), f2m(a_0), 11, checks)
note_check()

mu_0_comp = 2 * alpha_frac * h_planck / (c * e_charge * e_charge)

chk("C3: mu_0 = 2*alpha*h/(c*e^2)",
    f2m(mu_0_comp), f2m(mu_0), 11, checks)
note_check()


# ================================================================
# PART 8: KOIDE SECTOR ANALYSIS
# ================================================================

section("PART 8: KOIDE SECTOR ANALYSIS")

def koide_from_masses(m1, m2, m3):
    """Compute Koide ratio from three Fraction masses. Returns mpf."""
    s1 = msqrt(f2m(m1))
    s2 = msqrt(f2m(m2))
    s3 = msqrt(f2m(m3))
    num = f2m(m1 + m2 + m3)
    den = (s1 + s2 + s3) ** 2
    return num / den

K_lep_comp = koide_from_masses(m_e, m_mu, m_tau)
K_down_comp = koide_from_masses(m_d, m_s, m_b)
K_up_comp = koide_from_masses(m_u, m_c, m_t)

chk("K8: Koide K(e,mu,tau)",
    K_lep_comp, f2m(K_koide), 6, checks)
note_check()

a2_lep_comp = 2 * (3 * K_lep_comp - 1)
a2_down_comp = 2 * (3 * K_down_comp - 1)
a2_up_comp = 2 * (3 * K_up_comp - 1)

chk("a^2(leptons) ~ 2.000",
    a2_lep_comp, f2m(a2_lep), 4, checks)
note_check()

chk("a^2(down quarks) ~ 2.388",
    a2_down_comp, f2m(a2_down), 3, checks)
note_check()

chk("a^2(up quarks) ~ 3.093",
    a2_up_comp, f2m(a2_up), 3, checks)
note_check()

chk_bool("K ordering: K_lep < K_down < K_up",
         K_lep_comp < K_down_comp < K_up_comp,
         "K_lep=%s, K_down=%s, K_up=%s" % (
             mp.nstr(K_lep_comp, 7),
             mp.nstr(K_down_comp, 7),
             mp.nstr(K_up_comp, 7)), checks)
note_check()


# ================================================================
# PART 9: GAP RATIO DERIVED QUANTITIES
# ================================================================

section("PART 9: GAP RATIO AND COUPLING CHECKS")

chk_bool("Measured gap ratio in [1.2, 1.5]",
         mpf("1.2") < f2m(gap_measured) < mpf("1.5"),
         "gap = %s" % mp.nstr(f2m(gap_measured), 7), checks)
note_check()

sm_miss = abs(f2m(gap_SM) - f2m(gap_measured)) / f2m(gap_measured) * 100
chk_bool("SM gap miss > 30%",
         sm_miss > 30,
         "miss = %s%%" % mp.nstr(sm_miss, 4), checks)
note_check()

cd_dist = abs(f2m(gap_VL) - f2m(gap_measured))
chk_bool("CD gap distance < 0.06",
         cd_dist < mpf("0.06"),
         "distance = %s" % mp.nstr(cd_dist, 6), checks)
note_check()

chk_bool("1/alpha_1 > 60",
         f2m(inv_a1) > 60,
         "1/a1 = %s" % mp.nstr(f2m(inv_a1), 7), checks)
note_check()

chk_bool("1/alpha_2 in [30, 35]",
         30 < float(f2m(inv_a2)) < 35,
         "1/a2 = %s" % mp.nstr(f2m(inv_a2), 7), checks)
note_check()

chk_bool("1/alpha_3 in [7, 10]",
         7 < float(f2m(inv_a3)) < 10,
         "1/a3 = %s" % mp.nstr(f2m(inv_a3), 7), checks)
note_check()

alpha_em_check = Fraction(5, 3) * inv_a1 + inv_a2
chk("GUT normalization: (5/3)/a1 + 1/a2 = 1/alpha_em",
    f2m(alpha_em_check), f2m(alpha_inv), 11, checks)
note_check()


# ================================================================
# PART 10: LATTICE INDEPENDENCE ANNOTATION (Finding 15)
# ================================================================

section("PART 10: LATTICE RATIO INDEPENDENCE (Finding 15)")

mc_ms_pdg = m_c / m_s
mb_mc_pdg = m_b / m_c
mu_md_pdg = m_u / m_d

disc_mc_ms = abs(float(f2m(mc_ms_pdg)) - float(f2m(mc_ms))) / float(f2m(mc_ms)) * 100
disc_mb_mc = abs(float(f2m(mb_mc_pdg)) - float(f2m(mb_mc))) / float(f2m(mb_mc)) * 100
disc_mu_md = abs(float(f2m(mu_md_pdg)) - float(f2m(mu_md))) / float(f2m(mu_md)) * 100

chk_bool("m_c/m_s PDG vs FLAG: >10% discrepancy",
         disc_mc_ms > 10,
         "PDG=%s, FLAG=%s, disc=%.1f%%" % (
             mp.nstr(f2m(mc_ms_pdg), 5),
             mp.nstr(f2m(mc_ms), 5),
             disc_mc_ms), checks)
note_check()

chk_bool("m_b/m_c PDG vs FLAG: >20% discrepancy",
         disc_mb_mc > 20,
         "PDG=%s, FLAG=%s, disc=%.1f%%" % (
             mp.nstr(f2m(mb_mc_pdg), 5),
             mp.nstr(f2m(mb_mc), 5),
             disc_mb_mc), checks)
note_check()

chk_bool("m_u/m_d PDG vs FLAG: >3% discrepancy",
         disc_mu_md > 3,
         "PDG=%s, FLAG=%s, disc=%.1f%%" % (
             mp.nstr(f2m(mu_md_pdg), 4),
             mp.nstr(f2m(mu_md), 4),
             disc_mu_md), checks)
note_check()

print("  Note: These discrepancies are renormalization scale mismatches,")
print("  NOT database errors. See DATA-4 Finding 15.")


# ================================================================
# PART 11: CABIBBO DOUBLET STAGED PARAMETERS
# ================================================================

section("PART 11: CABIBBO DOUBLET SPECIFICATION")

chk_bool("CD is color triplet",
         CD_SU3 == 3,
         "SU(3) = %d" % CD_SU3, checks)
note_check()

chk_bool("CD is weak doublet",
         CD_SU2 == 2,
         "SU(2) = %d" % CD_SU2, checks)
note_check()

chk_exact("CD hypercharge = 1/6",
          CD_Y, Fraction(1, 6), checks)
note_check()

chk_bool("M_VL lower bound = 1.5 TeV",
         M_VL_lo == Fraction(1500000, 1),
         "M_VL_lo = %s MeV" % mp.nstr(f2m(M_VL_lo), 7), checks)
note_check()

chk_bool("M_VL upper bound = 6.0 TeV",
         M_VL_hi == Fraction(6000000, 1),
         "M_VL_hi = %s MeV" % mp.nstr(f2m(M_VL_hi), 7), checks)
note_check()

db2_over_db1 = db2_VL / db1_VL
chk_exact("Asymmetry db2/db1 = 15",
          db2_over_db1, Fraction(15, 1), checks)
note_check()

chk_bool("Democracy: per-gen betas all equal",
         db_per_gen[0] == db_per_gen[1] == db_per_gen[2],
         "db = (%s, %s, %s)" % (db_per_gen[0], db_per_gen[1], db_per_gen[2]),
         checks)
note_check()

chk_exact("Pure-gauge gap = 2",
          casimir_gap, Fraction(2, 1), checks)
note_check()


# ================================================================
# PART 12: TWO-LOOP b_ij MATRIX (complete — all 9 entries)
# ================================================================

section("PART 12: TWO-LOOP b_ij MATRIX (all 9 entries)")

bij_expected = [
    [Fraction(199, 50), Fraction(27, 10), Fraction(44, 5)],
    [Fraction(9, 10),   Fraction(35, 6),  Fraction(12, 1)],
    [Fraction(11, 10),  Fraction(9, 2),   Fraction(-26, 1)],
]

for i in range(3):
    for j in range(3):
        tag = "b_ij[%d][%d] = %s" % (i, j, bij_expected[i][j])
        chk_exact(tag, b_ij_SM[i][j], bij_expected[i][j], checks)
        note_check()


# ================================================================
# SUMMARY
# ================================================================

print()
print("=" * 70)
print("PRECISION TEST SUMMARY")
print("=" * 70)
print()

for sec_name, count in section_counts.items():
    print("  %-55s %3d checks" % (sec_name, count))

print()
print_summary(checks)

n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")

print()
if n_fail == 0:
    print("  PLATFORM STATUS: STABLE")
    print("  All values verified at source precision.")
    print("  phys24_lib.py is operational for Session 4.")
else:
    print("  PLATFORM STATUS: UNSTABLE — %d FAILURES" % n_fail)
    print("  Do not proceed until all failures are resolved.")
    print()
    print("  Failed checks:")
    for tag, status in checks:
        if status == "FAIL":
            print("    - %s" % tag)

print()
print("=" * 70)
print("PHYS24_LIB_TEST COMPLETE")
print("=" * 70)

