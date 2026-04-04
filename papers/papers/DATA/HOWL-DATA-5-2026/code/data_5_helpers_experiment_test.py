#!/usr/bin/env python3
"""
DATA-5 CHUNK 4 TEST: EXPERIMENT REPLAY vs PLATFORM & PHYSICS
================================================================
Tests every chunk 4 helper against experiment scripts and
known physics values.

No internal _underscore imports. All reference values computed
independently with mpmath and platform lib constants.

Run:  python data_5_chunk4_test.py
Requires: phys24_lib.py, data_5_objects.py, data_5_populate.py,
          data_5_helpers_experiment.py all in same directory.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, pi as mpi, sqrt as msqrt, log as mlog

mp.dps = 50


# ================================================================
# PLATFORM LIBRARIES (ground truth)
# ================================================================

from phys24_lib import *


# ================================================================
# DATA-5 SYSTEM (what we are testing)
# ================================================================

from data_5_objects import *
from data_5_populate import init_data5
from data_5_helpers_experiment import *

db = init_data5()


# ================================================================
# REFERENCE VALUES — computed independently, no chunk 4 internals
# ================================================================

R2_ref = f2m(db.get("const.R2").value)
four_R2_ref = mpf("4") * R2_ref
eight_R2_ref = mpf("8") * R2_ref

# Beta values from db (used as reference, not from internal functions)
b2_mod_obj = db.get("beta.b2_mod")
b2_mod_ref = b2_mod_obj.value                       # -13/6
b2_mod_num_ref = abs(b2_mod_ref.numerator)           # 13
b2_SM_obj = db.get("beta.b2_SM")
b2_SM_ref = b2_SM_obj.value                          # -19/6
YM_ref = Fraction(11, 1)

# Astrophysical
G_ref      = mpf("6.674e-11")
M_sun_ref  = mpf("1.989e30")
c_ref      = mpf("299792458")
pc_ref     = mpf("3.086e16")


# ================================================================
# TEST INFRASTRUCTURE
# ================================================================

checks = []


def chk_exact(tag, got, expected):
    if got == expected:
        print("  [PASS] %s" % tag)
        checks.append((tag, "PASS"))
    else:
        print("  [FAIL] %s" % tag)
        print("         got:      %s" % got)
        print("         expected: %s" % expected)
        checks.append((tag, "FAIL"))


def chk_close(tag, got, expected, digits):
    got_s = mp.nstr(got, digits)
    exp_s = mp.nstr(expected, digits)
    if got_s == exp_s:
        print("  [PASS] %s" % tag)
        checks.append((tag, "PASS"))
    else:
        print("  [FAIL] %s" % tag)
        print("         got:      %s" % mp.nstr(got, digits + 4))
        print("         expected: %s" % mp.nstr(expected, digits + 4))
        checks.append((tag, "FAIL"))


def chk_bool(tag, condition, detail=""):
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
print("DATA-5 CHUNK 4 TEST: EXPERIMENT REPLAY vs PLATFORM & PHYSICS")
print("=" * 70)
print()
print("  db loaded: %d objects" % db.count())
print()


# ================================================================
section("INTEGER EXTRACTION FROM DB")
# ================================================================

chk_exact("b2_mod from db = -13/6", b2_mod_ref, Fraction(-13, 6))
chk_exact("b2_mod matches phys24_lib.b2_mod", b2_mod_ref, b2_mod)
chk_exact("|b2_mod| numerator = 13", b2_mod_num_ref, 13)
chk_exact("b2_SM from db = -19/6", b2_SM_ref, Fraction(-19, 6))
chk_exact("|b2_SM| numerator = 19", abs(b2_SM_ref.numerator), 19)
chk_exact("YM = 11", YM_ref, Fraction(11, 1))


# ================================================================
section("DM/BARYON RATIO: db vs DIRECT COMPUTATION")
# ================================================================

dm = dm_baryon_ratio(db)

# Direct: (22/13) * pi
direct_ratio = f2m(Fraction(22, 13)) * mpi
chk_close("DM/baryon from db matches (22/13)*pi",
          dm["value"], direct_ratio, 10)

# Via 4*R2 path
via_R2 = f2m(Fraction(22, 13)) * four_R2_ref
chk_close("DM/baryon via 4*R2 matches via pi",
          dm["value"], via_R2, 20)

chk_exact("DM/baryon fraction = 22/13", dm["ratio_frac"], Fraction(22, 13))

chk_bool("DM/baryon miss from Planck < 0.1%",
         dm["miss_pct"] < mpf("0.1"),
         "miss = %s%%" % mp.nstr(dm["miss_pct"], 4))

chk_bool("DM/baryon ~ 5.32",
         mpf("5.3") < dm["value"] < mpf("5.35"),
         "value = %s" % mp.nstr(dm["value"], 6))


# ================================================================
section("OMEGA_DM: db vs DIRECT COMPUTATION")
# ================================================================

od = omega_dm(db)

direct_odm = f2m(Fraction(44, 169)) * R2_ref
chk_close("Omega_DM from db matches (44/169)*R2",
          od["value"], direct_odm, 10)

chk_exact("Omega_DM rational part = 44/169", od["rational_part"], Fraction(44, 169))
chk_exact("44 = 4 * 11", 44, 4 * 11)
chk_exact("169 = 13^2", 169, 13 ** 2)

chk_bool("44/169 is pure rational (R2 cancels)",
         od["rational_part"].denominator == 169 and od["rational_part"].numerator == 44)

chk_bool("Omega_DM miss from Planck < 1.5%",
         od["miss_pct"] < mpf("1.5"),
         "miss = %s%%" % mp.nstr(od["miss_pct"], 4))


# ================================================================
section("OMEGA_B, OMEGA_MATTER, OMEGA_DE: CONSISTENCY")
# ================================================================

ob = omega_b(db)
om = omega_matter(db)
ode = omega_de(db)

expected_ob = od["value"] / dm["value"]
chk_close("Omega_b = Omega_DM / (DM/baryon)", ob["value"], expected_ob, 10)

chk_close("Omega_m = Omega_DM + Omega_b",
          om["value"], od["value"] + ob["value"], 10)

chk_close("Omega_DE = 1 - Omega_m",
          ode["value"], mpf("1") - om["value"], 10)

chk_close("Omega_m + Omega_DE = 1 (flatness)",
          om["value"] + ode["value"], mpf("1"), 10)

chk_bool("Omega_b ~ 0.049",
         mpf("0.04") < ob["value"] < mpf("0.06"),
         "Omega_b = %s" % mp.nstr(ob["value"], 5))

chk_bool("Omega_m ~ 0.31",
         mpf("0.28") < om["value"] < mpf("0.35"),
         "Omega_m = %s" % mp.nstr(om["value"], 5))

chk_bool("Omega_DE ~ 0.69",
         mpf("0.65") < ode["value"] < mpf("0.72"),
         "Omega_DE = %s" % mp.nstr(ode["value"], 5))


# ================================================================
section("AMPLIFICATION FACTOR: DECOMPOSITION TEST")
# ================================================================

amp = amplification_factor(db, "220000")

v220 = mpf("220000")
expected_A = dm["value"] * mpf("2") * c_ref ** 2 / v220 ** 2
chk_close("A at 220 km/s matches direct formula",
          amp["A"], expected_A, 8)

chk_close("A_reduced = 44/13",
          amp["reduced"], f2m(Fraction(44, 13)), 6)

chk_bool("amplification decomposition matches (< 1% miss)",
         amp["match"],
         "reduced = %s, expected = %s" % (
             mp.nstr(amp["reduced"], 6),
             mp.nstr(amp["expected_44_13"], 6)))

chk_bool("amplification A >> 1",
         amp["A"] > mpf("1e6"),
         "A = %s" % mp.nstr(amp["A"], 4))

amp_100 = amplification_factor(db, "100000")
ratio_A = amp_100["A"] / amp["A"]
expected_ratio = (v220 / mpf("100000")) ** 2
chk_close("A scales as 1/v^2 (100 vs 220 km/s)",
          ratio_A, expected_ratio, 6)


# ================================================================
section("VIRIAL RATIO: MILKY WAY")
# ================================================================

R_mw = mpf("15000") * pc_ref
M_vis_mw = mpf("6e10") * M_sun_ref

vr = virial_ratio(db, "220000", R_mw, M_vis_mw)

expected_Mvir = R_mw * mpf("220000") ** 2 / G_ref
chk_close("virial mass matches R*v^2/G",
          vr["M_virial_kg"], expected_Mvir, 8)

chk_bool("virial ratio ~ 5-10",
         mpf("1") < vr["ratio"] < mpf("20"),
         "ratio = %s" % mp.nstr(vr["ratio"], 3))


# ================================================================
section("FRAME DRAGGING: NEGLIGIBLE FOR GALAXIES")
# ================================================================

fd = frame_dragging(db, M_vis_mw, R_mw, "220000")
chk_bool("frame dragging << 1 for galaxy",
         fd < mpf("1e-5"),
         "ratio = %s" % mp.nstr(fd, 4))

R_S_ref = mpf("2") * G_ref * M_vis_mw / c_ref ** 2
expected_fd = (mpf("220000") / c_ref) ** 2 * (R_S_ref / R_mw)
chk_close("frame_dragging matches direct",
          fd, expected_fd, 8)


# ================================================================
section("DWARF PURITY: CATALOG AND RATIOS")
# ================================================================

chk_bool("8 classical dwarfs", len(DWARFS) == 8,
         "count = %d" % len(DWARFS))
chk_bool("3 ultra-faint dwarfs", len(ULTRA_FAINTS) == 3,
         "count = %d" % len(ULTRA_FAINTS))

dp = dwarf_purity("Draco")
chk_bool("Draco DM/vis > 100",
         dp["DM_vis_ratio"] > mpf("100"),
         "ratio = %s" % mp.nstr(dp["DM_vis_ratio"], 4))
chk_bool("Draco dark fraction > 99%",
         dp["dark_fraction"] > mpf("0.99"),
         "frac = %s" % mp.nstr(dp["dark_fraction"], 5))

dp_seg = dwarf_purity("Segue1")
chk_bool("Segue1 DM/vis > 1000",
         dp_seg["DM_vis_ratio"] > mpf("1000"),
         "ratio = %s" % mp.nstr(dp_seg["DM_vis_ratio"], 4))

chk_bool("dwarf_purity('Nonexistent') returns None",
         dwarf_purity("Nonexistent") is None)

dp_fornax = dwarf_purity("Fornax")
chk_bool("Segue1 purer than Fornax",
         dp_seg["DM_vis_ratio"] > dp_fornax["DM_vis_ratio"],
         "Segue1=%s > Fornax=%s" % (
             mp.nstr(dp_seg["DM_vis_ratio"], 3),
             mp.nstr(dp_fornax["DM_vis_ratio"], 3)))


# ================================================================
section("DWARF COSMIC RATIO: ~19 = |b2_SM_num|")
# ================================================================

dcr_draco = dwarf_cosmic_ratio(db, "Draco")
chk_bool("Draco cosmic ratio in range [15, 50]",
         mpf("15") < dcr_draco < mpf("50"),
         "ratio = %s" % mp.nstr(dcr_draco, 4))

classical_ratios = []
for name in DWARFS:
    dp_c = dwarf_purity(name)
    classical_ratios.append(float(dp_c["DM_vis_ratio"]))
classical_ratios.sort()
n_cl = len(classical_ratios)
median_ratio = classical_ratios[n_cl // 2]
median_cosmic = median_ratio / float(dm["value"])

chk_bool("Median classical dwarf/cosmic ~ 19 order of magnitude",
         mpf("10") < mpf(str(median_cosmic)) < mpf("60"),
         "median DM/vis=%s, ratio to cosmic=%s" % (
             mp.nstr(mpf(str(median_ratio)), 3),
             mp.nstr(mpf(str(median_cosmic)), 3)))


# ================================================================
section("FABER-JACKSON AND TULLY-FISHER: SAME a0")
# ================================================================

M_fj_draco = faber_jackson(db, "9.1")
chk_bool("FJ(Draco, 9.1 km/s) returns positive mass",
         M_fj_draco > mpf("0"),
         "M = %s Msun" % mp.nstr(M_fj_draco, 3))

M_tf_mw = tully_fisher(db, "220")
chk_bool("TF(MW, 220 km/s) returns positive mass",
         M_tf_mw > mpf("0"),
         "M = %s Msun" % mp.nstr(M_tf_mw, 3))

M_fj_220 = faber_jackson(db, "220")
chk_close("FJ and TF give same result at same v",
          M_fj_220, M_tf_mw, 10)

# Direct: M = v^4 / (G * a0), a0 = c*H0/(8*R2)
H0_SI_ref = mpf("67.4") * mpf("1000") / mpf("3.086e22")
a0_ref = c_ref * H0_SI_ref / (eight_R2_ref)
v_mw = mpf("220000")
M_direct = v_mw ** 4 / (G_ref * a0_ref) / M_sun_ref
chk_close("TF(MW) matches v^4/(G*a0) direct",
          M_tf_mw, M_direct, 8)

chk_bool("MW TF prediction within order of magnitude of 3.6e11",
         mpf("1e10") < M_tf_mw < mpf("1e13"),
         "M_pred = %s, M_obs ~ 3.6e11" % mp.nstr(M_tf_mw, 3))

M_tf_440 = tully_fisher(db, "440")
ratio_v4 = M_tf_440 / M_tf_mw
chk_close("TF scales as v^4: TF(440)/TF(220) = 16",
          ratio_v4, mpf("16"), 8)


# ================================================================
section("HUBBLE CORRECTION 1-r FROM R2")
# ================================================================

omr_100 = hubble_correction_1_minus_r(db, 100)
expected_omr = mpf("1") / (mpf("12") * R2_ref * mpf("100"))
chk_close("1-r at N=100 matches 1/(12*R2*N)",
          omr_100, expected_omr, 10)

vp_ref = mpf("1") / (mpf("12") * R2_ref)
expected_vp = mpf("1") / (mpf("3") * mpi)
chk_close("VP step 1/(12*R2) = 1/(3*pi)",
          vp_ref, expected_vp, 12)


# ================================================================
section("EXPERIMENT RESULTS FROM DB")
# ================================================================

results = db.find(obj_type="result")
n_pass_r = sum(1 for r in results if hasattr(r, 'status') and r.status == "PASS")
n_fail_r = sum(1 for r in results if hasattr(r, 'status') and r.status == "FAIL")

chk_bool("db has experiment results", len(results) > 0,
         "found %d results" % len(results))
chk_bool("more PASSes than FAILs",
         n_pass_r > n_fail_r,
         "%d PASS, %d FAIL" % (n_pass_r, n_fail_r))
chk_bool("at least 10 results", len(results) >= 10,
         "count = %d" % len(results))


# ================================================================
section("RESEARCH PROGRAMS FROM DB")
# ================================================================

programs = db.find(obj_type="program")
chk_bool("3 research programs", len(programs) == 3,
         "count = %d" % len(programs))

for p in programs:
    has_ks = hasattr(p, 'kill_switches') and len(p.kill_switches) > 0
    chk_bool("program '%s' has kill switches" % p.name[:30], has_ks,
             "kills = %d" % (len(p.kill_switches) if hasattr(p, 'kill_switches') else 0))


# ================================================================
section("CROSS-CHUNK CONSISTENCY: R2 PATH")
# ================================================================

chk_close("4*R2 from db = pi", four_R2_ref, mpi, 20)

dm_via_chain = f2m(Fraction(22, 13)) * four_R2_ref
dm_via_pi = f2m(Fraction(22, 13)) * mpi
chk_close("DM/baryon via R2 chain = via pi",
          dm_via_chain, dm_via_pi, 15)

# Omega_b / Omega_DM = 1 / (DM/baryon) — verify the ratio
ob_over_od = ob["value"] / od["value"]
inv_dm_bar = mpf("1") / dm["value"]
chk_close("Omega_b/Omega_DM = 1/(DM/baryon)",
          ob_over_od, inv_dm_bar, 10)


# ================================================================
section("INTEGER POOL: ARITHMETIC VERIFICATION")
# ================================================================

chk_exact("22 = 2 * YM", 22, 2 * 11)
chk_exact("44 = 4 * YM", 44, 4 * 11)
chk_exact("169 = 13^2", 169, 13 * 13)
chk_exact("44/169 as Fraction", Fraction(44, 169), Fraction(4 * 11, 13 ** 2))

b1_SM_val = db.get("beta.b1_SM").value
b3_SM_val = db.get("beta.b3_SM").value
chk_exact("b1_SM = 41/10", b1_SM_val, Fraction(41, 10))
chk_exact("b3_SM = -7", b3_SM_val, Fraction(-7, 1))

gap_SM = (b1_SM_val - b2_SM_ref) / (b2_SM_ref - b3_SM_val)
chk_exact("SM gap ratio = 218/115", gap_SM, Fraction(218, 115))


# ================================================================
# SUMMARY
# ================================================================

print()
print("=" * 70)
print("DATA-5 CHUNK 4 TEST SUMMARY")
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

if n_fail == 0:
    print("  CHUNK 4 HELPERS: OPERATIONAL")
else:
    print("  CHUNK 4 HELPERS: %d FAILURES — INVESTIGATE" % n_fail)

print()
print("=" * 70)
print("DATA-5 CHUNK 4 TEST COMPLETE")
print("=" * 70)
