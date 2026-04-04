#!/usr/bin/env python3
"""
DATA-5 CHUNK 3 TEST: BOUNDARY, HUBBLE & GRAVITY vs PLATFORM
================================================================
Tests every chunk 3 helper against phys24_boundary_map_lib.py,
phys24_hubble_lib.py, and known physics values.

No internal _underscore imports. All reference values computed
independently with mpmath and platform lib constants.

Run:  python data_5_chunk3_test.py
Requires: phys24_lib.py, phys24_boundary_map_lib.py,
          phys24_hubble_lib.py, data_5_objects.py,
          data_5_populate.py, data_5_helpers_boundary.py
          all in same directory.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, pi as mpi, sqrt as msqrt, log as mlog, exp as mexp

mp.dps = 50


# ================================================================
# PLATFORM LIBRARIES (ground truth)
# ================================================================

from phys24_lib import *
from phys24_boundary_map_lib import (
    energy_to_distance_fm as lib_e2d,
    distance_fm_to_energy as lib_d2e,
)
from phys24_hubble_lib import (
    H0_MEASUREMENTS, H0_ORDERED,
    H0_local as lib_H0_local, H0_far as lib_H0_far,
    required_r as lib_required_r,
    one_minus_r as lib_one_minus_r,
    test_F1_strict as lib_test_F1_strict,
    alpha_running_step as lib_alpha_step,
)


# ================================================================
# DATA-5 SYSTEM (what we are testing)
# ================================================================

from data_5_objects import *
from data_5_populate import init_data5
from data_5_helpers_boundary import *

db = init_data5()


# ================================================================
# REFERENCE VALUES — computed independently, no chunk 3 internals
# ================================================================

R2_ref = f2m(db.get("const.R2").value)
eight_R2_ref = mpf("8") * R2_ref

# Astrophysical constants — same mpf("string") as chunk 3
G_ref      = mpf("6.674e-11")
M_sun_ref  = mpf("1.989e30")
M_earth_ref = mpf("5.972e24")
M_moon_ref = mpf("7.342e22")
R_earth_ref = mpf("6.371e6")
R_sun_ref  = mpf("6.957e8")
AU_ref     = mpf("1.496e11")
R_GPS_ref  = mpf("2.6556e7")
v_GPS_ref  = mpf("3874")
c_ref      = mpf("299792458")


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
print("DATA-5 CHUNK 3 TEST: BOUNDARY, HUBBLE & GRAVITY vs PLATFORM")
print("=" * 70)
print()
print("  db loaded: %d objects" % db.count())
print("  boundaries: %d" % db.count("boundary"))
print()


# ================================================================
section("SCALE CONVERSION: CHUNK 3 vs BOUNDARY MAP LIB")
# ================================================================

for E in ["91187.6", "1000", "0.511", "173000"]:
    got = energy_to_distance_fm(E)
    expected = lib_e2d(mpf(E))
    chk_close("energy_to_distance(%s MeV) matches lib" % E,
              got, expected, 8)

for d in ["1.0", "0.001", "197.3"]:
    got = distance_fm_to_energy(d)
    expected = lib_d2e(mpf(d))
    chk_close("distance_to_energy(%s fm) matches lib" % d,
              got, expected, 8)

E_rt = mpf("91187.6")
d_rt = energy_to_distance_fm(E_rt)
E_back = distance_fm_to_energy(d_rt)
chk_close("round-trip E->d->E at M_Z", E_back, E_rt, 10)


# ================================================================
section("BOUNDARY SEARCH AND TRAVERSAL")
# ================================================================

mz_bounds = find_boundary(db, "Z boson")
chk_bool("find_boundary('Z boson') returns result",
         len(mz_bounds) > 0,
         "found %d" % len(mz_bounds))

b_near_mz = boundary_at_scale(db, "91187.6")
chk_bool("boundary_at_scale(91187.6) finds something",
         b_near_mz is not None,
         "found: %s" % (b_near_mz.name if b_near_mz else "None"))

between = boundaries_between(db, "100", "200000")
chk_bool("boundaries_between(100, 200000 MeV) finds boundaries",
         len(between) > 0,
         "found %d" % len(between))

total_bounds = db.find(obj_type="boundary")
chk_bool("19 boundaries in db", len(total_bounds) == 19,
         "count = %d" % len(total_bounds))


# ================================================================
section("HUBBLE DATA: CHUNK 3 vs HUBBLE LIB")
# ================================================================

chk_exact("H0 local (SH0ES) = 73.0",
          hubble_local(db), Fraction(730, 10))
chk_exact("H0 far (Planck) = 67.4",
          hubble_far(db), Fraction(674, 10))

chk_exact("H0 local matches lib",
          hubble_local(db), lib_H0_local)
chk_exact("H0 far matches lib",
          hubble_far(db), lib_H0_far)

cum_ratio = hubble_cumulative_ratio(db)
chk_exact("cumulative ratio = 674/730 = 337/365",
          cum_ratio, Fraction(674, 730))

tension = hubble_tension_sigma(db)
chk_bool("Hubble tension > 4 sigma",
         tension > mpf("4"),
         "tension = %s sigma" % mp.nstr(tension, 3))

for N in [10, 100, 1000]:
    got_r = hubble_required_r(db, N)
    expected_r = lib_required_r(N)
    chk_close("required_r(N=%d) matches lib" % N,
              got_r, expected_r, 8)

    got_omr = hubble_one_minus_r(db, N)
    expected_omr = lib_one_minus_r(N)
    chk_close("one_minus_r(N=%d) matches lib" % N,
              got_omr, expected_omr, 8)

r_100 = hubble_required_r(db, 100)
H0_at_100 = hubble_running(db, hubble_local(db), r_100, 100)
chk_close("H0_running(73.0, r, 100) = 67.4",
          H0_at_100, f2m(hubble_far(db)), 4)

vp = hubble_vp_step_size(db)
expected_vp = lib_alpha_step()
chk_close("VP step 1/(12*R2) matches lib alpha_running_step",
          vp, expected_vp, 10)


# ================================================================
section("HUBBLE FALSIFICATION TESTS")
# ================================================================

f1_strict_pass, f1_strict_detail = test_F1_strict(db)
lib_f1_pass, lib_f1_vals = lib_test_F1_strict(
    [f2m(H0_MEASUREMENTS[k]["H0"]) for k in H0_ORDERED])

chk_bool("F1 strict: chunk 3 agrees with lib",
         f1_strict_pass == lib_f1_pass,
         "chunk3=%s, lib=%s" % (f1_strict_pass, lib_f1_pass))

f1_soft_pass, f1_soft_violations = test_F1_soft(db)
chk_bool("F1 soft: no hard inversions at 1-sigma",
         f1_soft_pass,
         "violations: %s" % (f1_soft_violations if not f1_soft_pass else "none"))


# ================================================================
section("GRAVITY COUPLING: PHYSICS VERIFICATION")
# ================================================================

gc_earth = grav_coupling(M_earth_ref, R_earth_ref)
expected_gc = G_ref * M_earth_ref / (R_earth_ref * c_ref ** 2)
chk_close("grav_coupling(Earth surface) matches direct",
          gc_earth, expected_gc, 10)

chk_bool("Earth coupling << 1 (non-relativistic)",
         gc_earth < mpf("1e-8"),
         "GM/(Rc^2) = %s" % mp.nstr(gc_earth, 4))

gc_sun = grav_coupling(M_sun_ref, R_sun_ref)
expected_gc_sun = G_ref * M_sun_ref / (R_sun_ref * c_ref ** 2)
chk_close("grav_coupling(Sun surface) matches direct",
          gc_sun, expected_gc_sun, 10)

bf_earth = binding_fraction(M_earth_ref, R_earth_ref)
expected_bf = mpf("3") * G_ref * M_earth_ref / (mpf("5") * R_earth_ref * c_ref ** 2)
chk_close("binding_fraction(Earth) matches 3GM/(5Rc^2)",
          bf_earth, expected_bf, 10)

chk_bool("Earth binding << rest mass",
         bf_earth < mpf("1e-8"),
         "fraction = %s" % mp.nstr(bf_earth, 4))

v_esc = escape_velocity(M_earth_ref, R_earth_ref)
expected_vesc = msqrt(mpf("2") * G_ref * M_earth_ref / R_earth_ref)
chk_close("escape_velocity(Earth) matches sqrt(2GM/R)",
          v_esc, expected_vesc, 10)

chk_bool("Earth escape velocity ~ 11.2 km/s",
         mpf("11000") < v_esc < mpf("11300"),
         "v_esc = %s m/s" % mp.nstr(v_esc, 5))


# ================================================================
section("HILL SPHERES: PHYSICS VERIFICATION")
# ================================================================

rh_earth = hill_sphere(M_earth_ref, M_sun_ref, AU_ref)
expected_rh = AU_ref * (M_earth_ref / (mpf("3") * M_sun_ref)) ** (mpf("1") / mpf("3"))
chk_close("hill_sphere(Earth) matches a*(m/3M)^(1/3)",
          rh_earth, expected_rh, 10)

rh_earth_km = rh_earth / mpf("1000")
chk_bool("Earth Hill sphere ~ 1.5 million km",
         mpf("1.4e6") < rh_earth_km < mpf("1.6e6"),
         "R_Hill = %s km" % mp.nstr(rh_earth_km, 4))

d_em = mpf("3.844e8")
rh_moon = hill_sphere(M_moon_ref, M_earth_ref, d_em)
chk_bool("Moon Hill sphere > 0 and < Earth-Moon distance",
         mpf("0") < rh_moon < d_em,
         "R_Hill = %s km" % mp.nstr(rh_moon / mpf("1000"), 4))


# ================================================================
section("KEPLER VIA R2: VERIFICATION AGAINST 4*pi^2 FORMULA")
# ================================================================

identity_lhs = mpf("64") * R2_ref ** 2
identity_rhs = mpf("4") * mpi ** 2
chk_close("64*R2^2 = 4*pi^2 (Kepler identity)", identity_lhs, identity_rhs, 20)

T_earth = kepler_period(db, AU_ref, M_sun_ref)
T_expected = msqrt(mpf("4") * mpi ** 2 * AU_ref ** 3 / (G_ref * M_sun_ref))
chk_close("kepler_period(Earth) matches 4pi^2 formula",
          T_earth, T_expected, 8)

T_year = mpf("365.25") * mpf("86400")
ratio_earth = T_earth / T_year
chk_bool("Earth Kepler period ~ 1 year",
         abs(ratio_earth - mpf("1")) < mpf("0.005"),
         "T_kepler/T_year = %s" % mp.nstr(ratio_earth, 6))

a_jup = mpf("7.785e11")
T_jup = kepler_period(db, a_jup, M_sun_ref)
T_jup_obs = mpf("11.862") * T_year
ratio_jup = T_jup / T_jup_obs
chk_bool("Jupiter Kepler period within 0.5%",
         abs(ratio_jup - mpf("1")) < mpf("0.005"),
         "T_kepler/T_obs = %s" % mp.nstr(ratio_jup, 6))


# ================================================================
section("PROCESS RATE: PHYSICS VERIFICATION")
# ================================================================

pr_earth = process_rate_ratio(M_earth_ref, R_earth_ref)
expected_pr = msqrt(mpf("1") - mpf("2") * G_ref * M_earth_ref / (R_earth_ref * c_ref ** 2))
chk_close("process_rate(Earth) matches sqrt(1-2GM/Rc^2)",
          pr_earth["exact_ratio"], expected_pr, 12)

chk_bool("Earth process rate < 1 (slower than infinity)",
         pr_earth["exact_ratio"] < mpf("1"),
         "ratio = %s" % mp.nstr(pr_earth["exact_ratio"], 12))

chk_bool("Earth fractional shift ~ 7e-10",
         mpf("5e-10") < pr_earth["fractional_shift"] < mpf("1e-9"),
         "shift = %s" % mp.nstr(pr_earth["fractional_shift"], 4))

pr_gps = process_rate_ratio(M_earth_ref, R_GPS_ref)
chk_bool("GPS orbit rate > Earth surface rate",
         pr_gps["exact_ratio"] > pr_earth["exact_ratio"],
         "GPS=%s > Earth=%s" % (
             mp.nstr(pr_gps["exact_ratio"], 11),
             mp.nstr(pr_earth["exact_ratio"], 11)))


# ================================================================
section("GPS CORRECTION: PHYSICS VERIFICATION")
# ================================================================

gps = gps_correction(db)

chk_bool("GPS gravitational shift > 0",
         gps["grav_shift"] > mpf("0"),
         "grav = %s" % mp.nstr(gps["grav_shift"], 4))

chk_bool("GPS velocity shift < 0",
         gps["vel_shift"] < mpf("0"),
         "vel = %s" % mp.nstr(gps["vel_shift"], 4))

chk_bool("GPS net shift > 0 (gravity dominates)",
         gps["total_shift"] > mpf("0"),
         "total = %s" % mp.nstr(gps["total_shift"], 4))

chk_bool("GPS total correction ~ 38 us/day",
         mpf("35") < gps["total_us_day"] < mpf("42"),
         "total = %s us/day" % mp.nstr(gps["total_us_day"], 4))

chk_bool("GPS gravitational component ~ +45 us/day",
         mpf("40") < gps["grav_ns_day"] / mpf("1000") < mpf("50"),
         "grav = %s us/day" % mp.nstr(gps["grav_ns_day"] / mpf("1000"), 4))

chk_bool("GPS velocity component ~ -7 us/day",
         mpf("-10") < gps["vel_ns_day"] / mpf("1000") < mpf("-5"),
         "vel = %s us/day" % mp.nstr(gps["vel_ns_day"] / mpf("1000"), 4))


# ================================================================
section("MUON LIFETIME: PHYSICS VERIFICATION")
# ================================================================

m0 = muon_observed_lifetime("0")
chk_close("muon at rest: gamma = 1", m0["gamma"], mpf("1"), 10)
chk_close("muon at rest: tau_obs = tau_rest",
          m0["tau_observed_us"], m0["tau_rest_us"], 10)

m99 = muon_observed_lifetime("0.99")
expected_gamma = mpf("1") / msqrt(mpf("1") - mpf("0.99") ** 2)
chk_close("muon at 0.99c: gamma matches", m99["gamma"], expected_gamma, 6)
chk_bool("muon at 0.99c: observed lifetime > rest",
         m99["tau_observed_us"] > m99["tau_rest_us"],
         "obs=%s > rest=%s" % (
             mp.nstr(m99["tau_observed_us"], 4),
             mp.nstr(m99["tau_rest_us"], 4)))

gammas = []
for v in ["0", "0.5", "0.9", "0.99", "0.999"]:
    m = muon_observed_lifetime(v)
    gammas.append(m["gamma"])
monotonic = all(gammas[i] < gammas[i + 1] for i in range(len(gammas) - 1))
chk_bool("gamma monotonically increasing with v", monotonic)


# ================================================================
section("TWIN PARADOX: PHYSICS VERIFICATION")
# ================================================================

tp = twin_paradox(db, "0.9", "10")
expected_gamma_tp = mpf("1") / msqrt(mpf("1") - mpf("0.9") ** 2)
chk_close("twin gamma at 0.9c", tp["gamma"], expected_gamma_tp, 6)

chk_bool("twin B ages less than A",
         tp["years_B"] < tp["years_A"],
         "A=%s, B=%s" % (mp.nstr(tp["years_A"], 4), mp.nstr(tp["years_B"], 4)))

chk_bool("twin cycle difference > 0",
         tp["cycle_difference"] > mpf("0"),
         "diff = %s cycles" % mp.nstr(tp["cycle_difference"], 4))

dv_db = f2m(db.get("const.dv_Cs").value)
chk_bool("twin uses dv_Cs from db (9192631770)",
         dv_db == mpf("9192631770"),
         "dv_Cs = %s" % mp.nstr(dv_db, 11))

tp0 = twin_paradox(db, "0", "10")
chk_close("twin at v=0: years_B = years_A",
          tp0["years_B"], tp0["years_A"], 10)
chk_close("twin at v=0: cycle difference = 0",
          tp0["cycle_difference"], mpf("0"), 10)


# ================================================================
section("ds^2 MINKOWSKI INTERVAL")
# ================================================================

ds_light = ds_squared("1", str(c_ref))
chk_close("ds^2 = 0 for light (dt=1, dx=c)", ds_light, mpf("0"), 10)

ds_time = ds_squared("1", "0")
chk_bool("ds^2 < 0 for stationary (timelike)",
         ds_time < mpf("0"),
         "ds^2 = %s" % mp.nstr(ds_time, 6))

ds_space = ds_squared("0", "1")
chk_bool("ds^2 > 0 for simultaneous separation (spacelike)",
         ds_space > mpf("0"),
         "ds^2 = %s" % mp.nstr(ds_space, 6))


# ================================================================
section("MOND a0: PHYSICS VERIFICATION")
# ================================================================

a0 = mond_a0(db)

chk_bool("a0 ~ 1.2e-10 m/s^2 (within factor 2)",
         mpf("0.5e-10") < a0 < mpf("2.5e-10"),
         "a0 = %s m/s^2" % mp.nstr(a0, 4))

# Independent computation: c*H0/(2*pi)
H0_SI_ref = mpf("67.4") * mpf("1000") / mpf("3.086e22")
a0_twopi = c_ref * H0_SI_ref / (mpf("2") * mpi)
chk_close("a0 via 8*R2 = a0 via 2*pi (identity)",
          a0, a0_twopi, 12)

r_a0_earth = mond_transition_radius(db, M_earth_ref)
expected_r_a0 = msqrt(G_ref * M_earth_ref / a0)
chk_close("mond_transition_radius(Earth) matches sqrt(GM/a0)",
          r_a0_earth, expected_r_a0, 8)

chk_bool("Earth a0 radius > Hill sphere",
         r_a0_earth > rh_earth,
         "r_a0=%s > R_Hill=%s" % (
             mp.nstr(r_a0_earth, 4), mp.nstr(rh_earth, 4)))

r_a0_sun = mond_transition_radius(db, M_sun_ref)
chk_bool("Sun a0 radius > 100 AU",
         r_a0_sun > mpf("100") * AU_ref,
         "r_a0_sun = %s AU" % mp.nstr(r_a0_sun / AU_ref, 3))


# ================================================================
section("INTERNAL CONSISTENCY CHECKS")
# ================================================================

chk_close("R2 from db = pi/4", R2_ref, mpi / 4, 30)
chk_close("8*R2 from db = 2*pi", eight_R2_ref, mpf("2") * mpi, 30)

# grav_coupling = v_esc^2 / (2c^2)
gc = grav_coupling(M_earth_ref, R_earth_ref)
ve = escape_velocity(M_earth_ref, R_earth_ref)
chk_close("GM/(Rc^2) = v_esc^2/(2c^2)",
          gc, (ve / c_ref) ** 2 / mpf("2"), 8)

# Process rate shift ~ GM/(Rc^2) for weak fields
pr = process_rate_ratio(M_earth_ref, R_earth_ref)
chk_bool("fractional_shift ~ coupling (weak field)",
         abs(pr["fractional_shift"] - pr["coupling"]) / pr["coupling"] < mpf("0.001"),
         "shift=%s, coupling=%s" % (
             mp.nstr(pr["fractional_shift"], 6),
             mp.nstr(pr["coupling"], 6)))


# ================================================================
# SUMMARY
# ================================================================

print()
print("=" * 70)
print("DATA-5 CHUNK 3 TEST SUMMARY")
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
    print("  CHUNK 3 HELPERS: OPERATIONAL")
else:
    print("  CHUNK 3 HELPERS: %d FAILURES — INVESTIGATE" % n_fail)

print()
print("=" * 70)
print("DATA-5 CHUNK 3 TEST COMPLETE")
print("=" * 70)
