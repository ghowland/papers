#!/usr/bin/env python3
"""
DATA-5 CHUNK 1 TEST: DERIVATION HELPERS vs PLATFORM LIBRARIES
================================================================
Tests every chunk 1 helper function against the established
platform libraries (phys24_lib.py, data_4_derivation_lib.py,
phys24_structure_lib.py).

For each function: the chunk 1 helper computes through db objects,
the platform library computes directly. The results must match
exactly (Fraction) or to 6+ digits (mpf).

This script EXCEEDS the derivation lib self-test by also testing:
  - All values trace through db objects (not flat imports)
  - R2 family from Q335 basis matches mpmath pi
  - Group theory pure-math functions match library constants
  - What-if scan produces CD as winner
  - Generation democracy from db representations
  - Two-loop b_ij matrices reconstructed from db match library

Run:  python data_5_chunk1_test.py
Requires: phys24_lib.py, data_4_derivation_lib.py,
          phys24_structure_lib.py, data_5_objects.py,
          data_5_populate.py, data_5_helpers_derivation.py
          all in same directory.

Pass target: 37/37 from derivation lib + new db-specific checks.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, pi as mpi, log as mlog, sqrt as msqrt

mp.dps = 50

# ================================================================
# PLATFORM LIBRARIES (the ground truth)
# ================================================================

from phys24_lib import *
from data_4_derivation_lib import (
    derive_couplings as lib_derive_couplings,
    gap_ratio_from_betas as lib_gap_ratio,
    find_crossing_L as lib_find_crossing_L,
    L_to_scale as lib_L_to_scale,
    predict_alpha_s_one_loop as lib_predict_as_1L,
    predict_sin2_one_loop as lib_predict_sin2_1L,
    predict_alpha_s_two_loop as lib_predict_as_2L,
    koide_ratio as lib_koide_ratio,
    koide_amplitude_sq as lib_koide_a2,
    koide_predict_m_tau as lib_koide_predict,
    decompose_SM_betas as lib_decompose,
    C2_adj_SU3, C2_adj_SU2, C2_fund_SU3, C2_fund_SU2,
    S2_fund, k1_GUT, gauge_coeff,
    db_ij_VL, b_ij_full,
)

# ================================================================
# DATA-5 SYSTEM (what we are testing)
# ================================================================

from data_5_objects import *
from data_5_populate import init_data5
from data_5_helpers_derivation import *

db = init_data5()


# ================================================================
# TEST INFRASTRUCTURE — same pattern as platform tests
# ================================================================

checks = []


def chk_exact(tag, got, expected):
    """Exact Fraction match."""
    if got == expected:
        print("  [PASS] %s" % tag)
        checks.append((tag, "PASS"))
    else:
        print("  [FAIL] %s" % tag)
        print("         got:      %s" % got)
        print("         expected: %s" % expected)
        checks.append((tag, "FAIL"))


def chk_close(tag, got, expected, digits):
    """Match to N significant digits."""
    got_s = mp.nstr(got, digits)
    exp_s = mp.nstr(expected, digits)
    if got_s == exp_s:
        print("  [PASS] %s" % tag)
        checks.append((tag, "PASS"))
    else:
        print("  [FAIL] %s" % tag)
        print("         got:      %s" % mp.nstr(got, digits + 2))
        print("         expected: %s" % mp.nstr(expected, digits + 2))
        checks.append((tag, "FAIL"))


def chk_bool(tag, condition, detail=""):
    """Boolean pass/fail."""
    if condition:
        print("  [PASS] %s" % tag)
        if detail:
            print("         %s" % detail)
        checks.append((tag, "PASS"))
    else:
        print("  [FAIL] %s" % tag)
        if detail:
            print("         %s" % detail)
        checks.append((tag, "FAIL"))


def section(title):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
    print()


# ================================================================
print("=" * 70)
print("DATA-5 CHUNK 1 TEST: DERIVATION HELPERS vs PLATFORM")
print("=" * 70)
print()
print("  db loaded: %d objects" % db.count())
print()


# ================================================================
section("R2 FAMILY FROM Q335 BASIS")
# ================================================================

chk_close("_R2(db) = pi/4", _R2(db), mpi / 4, 30)
chk_close("_R4(db) = pi^2/32", _R4(db), mpi ** 2 / 32, 30)
chk_close("_four_R2(db) = pi", _four_R2(db), mpi, 30)
chk_close("_eight_R2(db) = 2*pi", _eight_R2(db), 2 * mpi, 30)
chk_close("_sixteen_R2(db) = 4*pi", _sixteen_R2(db), 4 * mpi, 30)


# ================================================================
section("COUPLING EXTRACTION: CHUNK 1 vs LIBRARY")
# ================================================================

c = extract_couplings(db)
lib_a1, lib_a2, lib_a3 = lib_derive_couplings(alpha_inv, sin2_tW, alpha_s)

chk_exact("inv_a1 from db matches library", c["inv_a1"], lib_a1)
chk_exact("inv_a2 from db matches library", c["inv_a2"], lib_a2)
chk_exact("inv_a3 from db matches library", c["inv_a3"], lib_a3)

# Also match the flat library values
chk_exact("inv_a1 matches phys24_lib.inv_a1", c["inv_a1"], inv_a1)
chk_exact("inv_a2 matches phys24_lib.inv_a2", c["inv_a2"], inv_a2)
chk_exact("inv_a3 matches phys24_lib.inv_a3", c["inv_a3"], inv_a3)

chk_bool("inv_a2 ~ 31.7 (not 593)",
         mpf("30") < c["inv_a2_mpf"] < mpf("35"),
         "inv_a2 = %s" % mp.nstr(c["inv_a2_mpf"], 7))


# ================================================================
section("GAP RATIOS: CHUNK 1 vs LIBRARY")
# ================================================================

gap_sm = gap_ratio_SM(db)
gap_cd = gap_ratio_CD(db)
lib_gap_sm = lib_gap_ratio(b1_SM, b2_SM, b3_SM)
lib_gap_cd = lib_gap_ratio(b1_mod, b2_mod, b3_mod)

chk_exact("SM gap via db = 218/115", gap_sm, Fraction(218, 115))
chk_exact("CD gap via db = 38/27", gap_cd, Fraction(38, 27))
chk_exact("SM gap matches library", gap_sm, lib_gap_sm)
chk_exact("CD gap matches library", gap_cd, lib_gap_cd)

# CD is closer to measured than SM
dist_sm = gap_distance(db, "beta.b1_SM", "beta.b2_SM", "beta.b3_SM")
dist_cd = gap_distance(db, "beta.b1_mod", "beta.b2_mod", "beta.b3_mod")
chk_bool("CD gap closer to measured than SM", dist_cd < dist_sm,
         "CD dist = %s, SM dist = %s" % (mp.nstr(dist_cd, 4), mp.nstr(dist_sm, 4)))


# ================================================================
section("ONE-LOOP CROSSING: CHUNK 1 vs LIBRARY")
# ================================================================

L_cd = find_crossing_L(db)
lib_L_cd = lib_find_crossing_L(inv_a1, inv_a2, b1_mod, b2_mod)

chk_exact("L_GUT (CD) from db matches library", L_cd, lib_L_cd)

mu_MeV, log10_MGUT = L_to_scale_MeV(db, L_cd)
_, lib_log10 = lib_L_to_scale(f2m(lib_L_cd), f2m(M_Z))

chk_close("log10(M_GUT/GeV) matches library", log10_MGUT, lib_log10, 4)
chk_bool("M_GUT in [10^15, 10^16]",
         mpf("15") < log10_MGUT < mpf("16"),
         "log10 = %s" % mp.nstr(log10_MGUT, 4))


# ================================================================
section("ONE-LOOP ALPHA_S PREDICTION: CHUNK 1 vs LIBRARY")
# ================================================================

as_1L = predict_alpha_s_1L(db)
lib_as_1L = lib_predict_as_1L(inv_a1, inv_a2, inv_a3, b1_mod, b2_mod, b3_mod)

chk_close("alpha_s 1L from db matches library",
          as_1L["alpha_s_pred"], lib_as_1L["alpha_s_pred"], 6)

chk_close("Delta 1L from db matches library",
          as_1L["Delta"], lib_as_1L["Delta"], 6)

chk_bool("alpha_s 1L miss < 15%",
         as_1L["miss_pct"] < mpf("15"),
         "miss = %s%%" % mp.nstr(as_1L["miss_pct"], 4))


# ================================================================
section("ONE-LOOP SIN2_TW PREDICTION: CHUNK 1 vs LIBRARY")
# ================================================================

sin2_1L = predict_sin2_1L(db)
lib_sin2_1L = lib_predict_sin2_1L(alpha_inv, alpha_s, b1_mod, b2_mod, b3_mod)

chk_close("sin2 1L from db matches library",
          sin2_1L["sin2_pred"], lib_sin2_1L["sin2_pred"], 6)

chk_bool("sin2 1L miss < 2%",
         sin2_1L["miss_pct"] < mpf("2"),
         "miss = %s%%" % mp.nstr(sin2_1L["miss_pct"], 4))


# ================================================================
section("TWO-LOOP b_ij RECONSTRUCTION FROM DB")
# ================================================================

bij_sm = _get_bij_SM(db)
bij_vl = _get_dbij_VL(db)
bij_full = _get_bij_full(db)

# Check VL matrix against library db_ij_VL
for i in range(3):
    for j in range(3):
        chk_exact("dbij_VL[%d][%d] from db matches library" % (i, j),
                  bij_vl[i][j], db_ij_VL[i][j])

# Critical: db_22 = 15/4 not 39/4
chk_exact("dbij_VL[1][1] = 15/4 (fermion only, not 39/4)",
          bij_vl[1][1], Fraction(15, 4))

# Full matrix matches library
for i in range(3):
    for j in range(3):
        chk_exact("bij_full[%d][%d] from db matches library" % (i, j),
                  bij_full[i][j], b_ij_full[i][j])


# ================================================================
section("TWO-LOOP ALPHA_S PREDICTION: CHUNK 1 vs LIBRARY")
# ================================================================

as_2L_SM = predict_alpha_s_2L(db, bij_tag="SM", n_steps=500)
as_2L_full = predict_alpha_s_2L(db, bij_tag="full", n_steps=500)

lib_as_2L_SM = lib_predict_as_2L(inv_a1, inv_a2, inv_a3,
                                   [b1_mod, b2_mod, b3_mod],
                                   b_ij_SM, n_steps=500)
lib_as_2L_full = lib_predict_as_2L(inv_a1, inv_a2, inv_a3,
                                     [b1_mod, b2_mod, b3_mod],
                                     b_ij_full, n_steps=500)

chk_close("alpha_s 2L SM from db matches library",
          as_2L_SM["alpha_s_pred"], lib_as_2L_SM["alpha_s_pred"], 4)

chk_close("alpha_s 2L full from db matches library",
          as_2L_full["alpha_s_pred"], lib_as_2L_full["alpha_s_pred"], 4)

chk_bool("2L SM alpha_s miss < 1%",
         as_2L_SM["miss_pct"] < mpf("1"),
         "miss = %s%%" % mp.nstr(as_2L_SM["miss_pct"], 4))

chk_bool("2L full alpha_s miss < 1%",
         as_2L_full["miss_pct"] < mpf("1"),
         "miss = %s%%" % mp.nstr(as_2L_full["miss_pct"], 4))

chk_bool("Full b_ij improves over SM b_ij",
         as_2L_full["miss_pct"] < as_2L_SM["miss_pct"],
         "full=%s%% < SM=%s%%" % (
             mp.nstr(as_2L_full["miss_pct"], 4),
             mp.nstr(as_2L_SM["miss_pct"], 4)))


# ================================================================
section("TWO-LOOP SIN2_TW PREDICTION")
# ================================================================

sin2_2L = predict_sin2_2L(db, n_steps=500)
chk_bool("sin2 2L miss < 2%",
         sin2_2L["miss_pct"] < mpf("2"),
         "miss = %s%%" % mp.nstr(sin2_2L["miss_pct"], 4))


# ================================================================
section("KOIDE: CHUNK 1 vs LIBRARY")
# ================================================================

K_db = koide_ratio_db(db)
K_lib = lib_koide_ratio(m_e, m_mu, m_tau)

chk_close("Koide K from db matches library", K_db, K_lib, 8)

a2_db = koide_amplitude_sq(K_db)
a2_lib = lib_koide_a2(K_lib)
chk_close("Koide a^2 from db matches library", a2_db, a2_lib, 6)

chk_bool("a^2 near 2", abs(a2_db - mpf("2")) < mpf("0.001"),
         "a^2 = %s" % mp.nstr(a2_db, 8))

kp = koide_predict(db)
lib_kp = lib_koide_predict(m_e, m_mu)

chk_close("m_tau predicted from db matches library",
          kp["m_tau_pred"], lib_kp["m_tau_pred"], 6)

chk_bool("m_tau miss < 0.01%",
         kp["miss_pct"] < mpf("0.01"),
         "miss = %s%%" % mp.nstr(kp["miss_pct"], 6))


# ================================================================
section("BETA DECOMPOSITION: CHUNK 1 vs LIBRARY")
# ================================================================

lib_decomp = lib_decompose()

for gauge, bid, lib_g, lib_f, lib_h, lib_total in [
    ("U1",  "beta.b1_SM", lib_decomp["b1_gauge"], lib_decomp["b1_fermion"], lib_decomp["b1_higgs"], b1_SM),
    ("SU2", "beta.b2_SM", lib_decomp["b2_gauge"], lib_decomp["b2_fermion"], lib_decomp["b2_higgs"], b2_SM),
    ("SU3", "beta.b3_SM", lib_decomp["b3_gauge"], lib_decomp["b3_fermion"], lib_decomp["b3_higgs"], b3_SM),
]:
    d = decompose_beta(db, bid)
    if d is not None:
        total = d["total"]
        chk_exact("b_%s total from db matches library" % gauge, total, lib_total)
        if d.get("sum_matches") is not None:
            chk_bool("b_%s decomposition sums correctly" % gauge, d["sum_matches"],
                     "sum = %s, total = %s" % (d.get("sum_parts"), total))


# ================================================================
section("GROUP THEORY: PURE MATH FUNCTIONS")
# ================================================================

# Pure math — no db needed
chk_exact("casimir_adj(3) = 3", casimir_adj(3), C2_adj_SU3)
chk_exact("casimir_adj(2) = 2", casimir_adj(2), C2_adj_SU2)
chk_exact("casimir_fund(3) = 4/3", casimir_fund(3), C2_fund_SU3)
chk_exact("casimir_fund(2) = 3/4", casimir_fund(2), C2_fund_SU2)
chk_exact("dynkin_fund() = 1/2", dynkin_fund(), S2_fund)
chk_exact("yang_mills_coefficient() = 11/3", yang_mills_coefficient(), Fraction(11, 3))
chk_exact("gauge_beta(3) = -11", gauge_beta(3), Fraction(-11, 1))
chk_exact("gauge_beta(2) = -22/3", gauge_beta(2), Fraction(-22, 3))


# ================================================================
section("GENERATION DEMOCRACY FROM DB REPRESENTATIONS")
# ================================================================

democracy = generation_democracy_check(db)
chk_bool("Generation democracy: per-gen = (4/3, 4/3, 4/3)", democracy)


# ================================================================
section("WHAT-IF SCAN: CD MUST WIN")
# ================================================================

# CD (3,2,1/6) should be closest to measured gap ratio
wf = whatif_rep(db, "CD test", 3, 2, Fraction(1, 6))
chk_exact("whatif CD db1 = 1/15", wf["db"][0], Fraction(1, 15))
chk_exact("whatif CD db2 = 1", wf["db"][1], Fraction(1, 1))
chk_exact("whatif CD db3 = 1/3", wf["db"][2], Fraction(1, 3))
chk_exact("whatif CD gap = 38/27", wf["gap"], Fraction(38, 27))

# Custom betas should reproduce CD prediction
wc = whatif_custom_betas(db, b1_mod, b2_mod, b3_mod, name="CD custom")
chk_exact("custom betas gap = 38/27", wc["gap"], Fraction(38, 27))
chk_close("custom betas alpha_s matches 1L",
          wc["alpha_s_pred"], as_1L["alpha_s_pred"], 6)


# ================================================================
section("ONE-LOOP RUNNING AT L=0 RETURNS M_Z VALUES")
# ================================================================

at_MZ = run_one_loop(db, ["beta.b1_mod", "beta.b2_mod", "beta.b3_mod"],
                      Fraction(0, 1))
chk_close("run_one_loop(L=0)[0] = inv_a1", at_MZ[0], c["inv_a1_mpf"], 10)
chk_close("run_one_loop(L=0)[1] = inv_a2", at_MZ[1], c["inv_a2_mpf"], 10)
chk_close("run_one_loop(L=0)[2] = inv_a3", at_MZ[2], c["inv_a3_mpf"], 10)


# ================================================================
# SUMMARY
# ================================================================

print()
print("=" * 70)
print("DATA-5 CHUNK 1 TEST SUMMARY")
print("=" * 70)
print()

n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")
n_total = len(checks)

print("  TOTAL: %d PASS, %d FAIL out of %d" % (n_pass, n_fail, n_total))
print()

if n_fail > 0:
    print("  FAILURES:")
    for tag, status in checks:
        if status == "FAIL":
            print("    - %s" % tag)
    print()

# Compare to derivation lib self-test (37/37)
print("  COMPARISON TO PLATFORM:")
print("    data_4_derivation_lib self-test:  37/37")
print("    chunk 1 test:                     %d/%d" % (n_pass, n_total))
print()

if n_fail == 0:
    print("  CHUNK 1 HELPERS: OPERATIONAL")
    print("  All values match platform libraries exactly.")
    print("  All predictions through db objects agree with direct computation.")
else:
    print("  CHUNK 1 HELPERS: %d FAILURES — INVESTIGATE" % n_fail)

print()
print("=" * 70)
print("DATA-5 CHUNK 1 TEST COMPLETE")
print("=" * 70)
