#!/usr/bin/env python3
"""
DATA-5 CHUNK 3 TEST: BOUNDARY, HUBBLE & GRAVITY vs PLATFORM
================================================================
Tests every chunk 3 helper against phys24_boundary_map_lib.py,
phys24_hubble_lib.py, and the physics in nested_soliton_gravity.py
and time_process_rate_test.py.

For each computation: chunk 3 produces a result, we verify against
the platform library or against known physics values computed
independently with mpmath.

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
    get_boundary_by_name as lib_get_boundary,
    boundaries_between_scales as lib_between,
)
from phys24_hubble_lib import (
    H0_MEASUREMENTS, H0_ORDERED,
    H0_local as lib_H0_local, H0_far as lib_H0_far,
    required_r as lib_required_r,
    one_minus_r as lib_one_minus_r,
    H0_running as lib_H0_running,
    test_F1_strict as lib_test_F1_strict,
    test_F1_soft as lib_test_F1_soft,
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

# E -> distance
for E in ["91187.6", "1000", "0.511", "173000"]:
    got = energy_to_distance_fm(E)
    expected = lib_e2d(mpf(E))
    chk_close("energy_to_distance(%s MeV) matches lib" % E,
              got, expected, 8)

# distance -> E (inverse)
for d in ["1.0", "0.001", "197.3"]:
    got = distance_fm_to_energy(d)
    expected = lib_d2e(mpf(d))
    chk_close("distance_to_energy(%s fm) matches lib" % d,
              got, expected, 8)

# Round-trip: E -> d -> E
E_rt = mpf("91187.6")
d_rt = energy_to_distance_fm(E_rt)
E_back = distance_fm_to_energy(d_rt)
chk_close("round-trip E->d->E at M_Z", E_back, E_rt, 10)


# ================================================================
section("BOUNDARY SEARCH AND TRAVERSAL")
# ================================================================

# find_boundary by name
mz_bounds = find_boundary(db, "Z boson")
chk_bool("find_boundary('Z boson') returns result",
         len(mz_bounds) > 0,
         "found %d" % len(mz_bounds))

# boundary_at_scale near M_Z
b_near_mz = boundary_at_scale(db, "91187.6")
chk_bool("boundary_at_scale(91187.6) finds something",
         b_near_mz is not None,
         "found: %s" % (b_near_mz.name if b_near_mz else "None"))

# boundaries_between
between = boundaries_between(db, "100", "200000")
chk_bool("boundaries_between(100, 200000 MeV) finds boundaries",
         len(between) > 0,
         "found %d" % len(between))

# All 19 boundaries present
total_bounds = db.find(obj_type="boundary")
chk_bool("19 boundaries in db", len(total_bounds) == 19,
         "count = %d" % len(total_bounds))


# ================================================================
section("HUBBLE DATA: CHUNK 3 vs HUBBLE LIB")
# ================================================================

# H0 values match library Fractions exactly
chk_exact("H0 local (SH0ES) = 73.0",
          hubble_local(db), Fraction(730, 10))
chk_exact("H0 far (Planck) = 67.4",
          hubble_far(db), Fraction(674, 10))

# Match library values
chk_exact("H0 local matches lib",
          hubble_local(db), lib_H0_local)
chk_exact("H0 far matches lib",
          hubble_far(db), lib_H0_far)

# Cumulative ratio
cum_ratio = hubble_cumulative_ratio(db)
expected_ratio = Fraction(674, 730)
chk_exact("cumulative ratio = 674/730 = 337/365",
          cum_ratio, expected_ratio)

# Tension in sigma
tension = hubble_tension_sigma(db)
chk_bool("Hubble tension > 4 sigma",
         tension > mpf("4"),
         "tension = %s sigma" % mp.nstr(tension, 3))

# Required r at several N
for N in [10, 100, 1000]:
    got_r = hubble_required_r(db, N)
    expected_r = lib_required_r(N)
    chk_close("required_r(N=%d) matches lib" % N,
              got_r, expected_r, 8)

    got_omr = hubble_one_minus_r(db, N)
    expected_omr = lib_one_minus_r(N)
    chk_close("one_minus_r(N=%d) matches lib" % N,
              got_omr, expected_omr, 8)

# Running curve: H0(0)*r^N should give H0(N)
r_100 = hubble_required_r(db, 100)
H0_at_100 = hubble_running(db, hubble_local(db), r_100, 100)
chk_close("H0_running(73.0, r, 100) = 67.4",
          H0_at_100, f2m(hubble_far(db)), 4)

# VP step size
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

# F1 strict may fail due to H0LiCOW > SH0ES
# Both chunk 3 and lib should give same answer
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

# Earth surface: GM/(Rc^2)
G = mpf("6.674e-11")
M_e = mpf("5.972e24")
R_e = mpf("6.371e6")
c = mpf("299792458")

gc_earth = grav_coupling(M_e, R_e)
expected_gc = G * M_e / (R_e * c ** 2)
chk_close("grav_coupling(Earth surface) matches direct",
          gc_earth, expected_gc, 10)

chk_bool("Earth coupling << 1 (non-relativistic)",
         gc_earth < mpf("1e-8"),
         "GM/(Rc^2) = %s" % mp.nstr(gc_earth, 4))

# Sun surface
M_s = mpf("1.989e30")
R_s = mpf("6.957e8")
gc_sun = grav_coupling(M_s, R_s)
expected_gc_sun = G * M_s / (R_s * c ** 2)
chk_close("grav_coupling(Sun surface) matches direct",
          gc_sun, expected_gc_sun, 10)

# Binding fraction: 3GM/(5Rc^2)
bf_earth = binding_fraction(M_e, R_e)
expected_bf = mpf("3") * G * M_e / (mpf("5") * R_e * c ** 2)
chk_close("binding_fraction(Earth) matches 3GM/(5Rc^2)",
          bf_earth, expected_bf, 10)

chk_bool("Earth binding << rest mass",
         bf_earth < mpf("1e-8"),
         "fraction = %s" % mp.nstr(bf_earth, 4))

# Escape velocity: v_esc = sqrt(2GM/R)
v_esc = escape_velocity(M_e, R_e)
expected_vesc = msqrt(mpf("2") * G * M_e / R_e)
chk_close("escape_velocity(Earth) matches sqrt(2GM/R)",
          v_esc, expected_vesc, 10)

chk_bool("Earth escape velocity ~ 11.2 km/s",
         mpf("11000") < v_esc < mpf("11300"),
         "v_esc = %s m/s" % mp.nstr(v_esc, 5))


# ================================================================
section("HILL SPHERES: PHYSICS VERIFICATION")
# ================================================================

# Earth Hill sphere: a * (M_e/(3*M_s))^(1/3)
AU = mpf("1.496e11")
rh_earth = hill_sphere(M_e, M_s, AU)
expected_rh = AU * (M_e / (mpf("3") * M_s)) ** (mpf("1") / mpf("3"))
chk_close("hill_sphere(Earth) matches a*(m/3M)^(1/3)",
          rh_earth, expected_rh, 10)

rh_earth_km = rh_earth / mpf("1000")
chk_bool("Earth Hill sphere ~ 1.5 million km",
         mpf("1.4e6") < rh_earth_km < mpf("1.6e6"),
         "R_Hill = %s km" % mp.nstr(rh_earth_km, 4))

# Moon Hill sphere
M_moon = mpf("7.342e22")
d_em = mpf("3.844e8")
rh_moon = hill_sphere(M_moon, M_e, d_em)
chk_bool("Moon Hill sphere > 0 and < Earth-Moon distance",
         mpf("0") < rh_moon < d_em,
         "R_Hill = %s km" % mp.nstr(rh_moon / mpf("1000"), 4))


# ================================================================
section("KEPLER VIA R2: VERIFICATION AGAINST 4*pi^2 FORMULA")
# ================================================================

# Earth: T = sqrt(4*pi^2 * a^3 / (GM))
# In R2: T = sqrt(64*R2^2 * a^3 / (GM))
# These are identical because 64*R2^2 = 64*(pi/4)^2 = 64*pi^2/16 = 4*pi^2

# Verify the identity first
R2_val = _R2(db)
identity_lhs = mpf("64") * R2_val ** 2
identity_rhs = mpf("4") * mpi ** 2
chk_close("64*R2^2 = 4*pi^2 (Kepler identity)", identity_lhs, identity_rhs, 20)

# Earth orbital period
T_earth = kepler_period(db, AU, M_s)
T_expected = msqrt(mpf("4") * mpi ** 2 * AU ** 3 / (G * M_s))
chk_close("kepler_period(Earth) matches 4pi^2 formula",
          T_earth, T_expected, 8)

# Compare to 365.25 days
T_year = mpf("365.25") * mpf("86400")
ratio_earth = T_earth / T_year
chk_bool("Earth Kepler period ~ 1 year",
         abs(ratio_earth - mpf("1")) < mpf("0.005"),
         "T_kepler/T_year = %s" % mp.nstr(ratio_earth, 6))

# Jupiter
a_jup = mpf("7.785e11")
T_jup = kepler_period(db, a_jup, M_s)
T_jup_obs = mpf("11.862") * T_year
ratio_jup = T_jup / T_jup_obs
chk_bool("Jupiter Kepler period within 0.5%",
         abs(ratio_jup - mpf("1")) < mpf("0.005"),
         "T_kepler/T_obs = %s" % mp.nstr(ratio_jup, 6))


# ================================================================
section("PROCESS RATE: PHYSICS VERIFICATION")
# ================================================================

# Earth surface: sqrt(1 - 2GM/(Rc^2))
pr_earth = process_rate_ratio(M_e, R_e)
expected_pr = msqrt(mpf("1") - mpf("2") * G * M_e / (R_e * c ** 2))
chk_close("process_rate(Earth) matches sqrt(1-2GM/Rc^2)",
          pr_earth["exact_ratio"], expected_pr, 12)

chk_bool("Earth process rate < 1 (slower than infinity)",
         pr_earth["exact_ratio"] < mpf("1"),
         "ratio = %s" % mp.nstr(pr_earth["exact_ratio"], 12))

chk_bool("Earth fractional shift ~ 7e-10",
         mpf("5e-10") < pr_earth["fractional_shift"] < mpf("1e-9"),
         "shift = %s" % mp.nstr(pr_earth["fractional_shift"], 4))

# GPS orbit: should be closer to 1 than Earth surface
pr_gps = process_rate_ratio(M_e, mpf("2.6556e7"))
chk_bool("GPS orbit rate > Earth surface rate",
         pr_gps["exact_ratio"] > pr_earth["exact_ratio"],
         "GPS=%s > Earth=%s" % (
             mp.nstr(pr_gps["exact_ratio"], 11),
             mp.nstr(pr_earth["exact_ratio"], 11)))


# ================================================================
section("GPS CORRECTION: PHYSICS VERIFICATION")
# ================================================================

gps = gps_correction(db)

# Gravitational shift must be positive (higher = faster)
chk_bool("GPS gravitational shift > 0",
         gps["grav_shift"] > mpf("0"),
         "grav = %s" % mp.nstr(gps["grav_shift"], 4))

# Velocity shift must be negative (moving = slower)
chk_bool("GPS velocity shift < 0",
         gps["vel_shift"] < mpf("0"),
         "vel = %s" % mp.nstr(gps["vel_shift"], 4))

# Net shift must be positive (gravity wins)
chk_bool("GPS net shift > 0 (gravity dominates)",
         gps["total_shift"] > mpf("0"),
         "total = %s" % mp.nstr(gps["total_shift"], 4))

# Total correction ~ 38.5 us/day (well-known value)
chk_bool("GPS total correction ~ 38 us/day",
         mpf("35") < gps["total_us_day"] < mpf("42"),
         "total = %s us/day" % mp.nstr(gps["total_us_day"], 4))

# Gravitational component ~ +45 us/day
chk_bool("GPS gravitational component ~ +45 us/day",
         mpf("40") < gps["grav_ns_day"] / mpf("1000") < mpf("50"),
         "grav = %s us/day" % mp.nstr(gps["grav_ns_day"] / mpf("1000"), 4))

# Velocity component ~ -7 us/day
chk_bool("GPS velocity component ~ -7 us/day",
         mpf("-10") < gps["vel_ns_day"] / mpf("1000") < mpf("-5"),
         "vel = %s us/day" % mp.nstr(gps["vel_ns_day"] / mpf("1000"), 4))


# ================================================================
section("MUON LIFETIME: PHYSICS VERIFICATION")
# ================================================================

# At rest: gamma = 1, tau = tau_rest
m0 = muon_observed_lifetime("0")
chk_close("muon at rest: gamma = 1", m0["gamma"], mpf("1"), 10)
chk_close("muon at rest: tau_obs = tau_rest",
          m0["tau_observed_us"], m0["tau_rest_us"], 10)

# At v = 0.99c: gamma = 1/sqrt(1-0.99^2) = 1/sqrt(0.0199) ~ 7.09
m99 = muon_observed_lifetime("0.99")
expected_gamma = mpf("1") / msqrt(mpf("1") - mpf("0.99") ** 2)
chk_close("muon at 0.99c: gamma matches", m99["gamma"], expected_gamma, 6)
chk_bool("muon at 0.99c: observed lifetime > rest",
         m99["tau_observed_us"] > m99["tau_rest_us"],
         "obs=%s > rest=%s" % (
             mp.nstr(m99["tau_observed_us"], 4),
             mp.nstr(m99["tau_rest_us"], 4)))

# Gamma monotonically increasing
gammas = []
for v in ["0", "0.5", "0.9", "0.99", "0.999"]:
    m = muon_observed_lifetime(v)
    gammas.append(m["gamma"])
monotonic = all(gammas[i] < gammas[i + 1] for i in range(len(gammas) - 1))
chk_bool("gamma monotonically increasing with v", monotonic)


# ================================================================
section("TWIN PARADOX: PHYSICS VERIFICATION")
# ================================================================

# At v = 0.9c, 10 years
tp = twin_paradox(db, "0.9", "10")
expected_gamma_tp = mpf("1") / msqrt(mpf("1") - mpf("0.9") ** 2)
chk_close("twin gamma at 0.9c", tp["gamma"], expected_gamma_tp, 6)

chk_bool("twin B ages less than A",
         tp["years_B"] < tp["years_A"],
         "A=%s, B=%s" % (mp.nstr(tp["years_A"], 4), mp.nstr(tp["years_B"], 4)))

chk_bool("twin cycle difference > 0",
         tp["cycle_difference"] > mpf("0"),
         "diff = %s cycles" % mp.nstr(tp["cycle_difference"], 4))

# Cesium cycles from db
dv_db = f2m(db.get("const.dv_Cs").value)
chk_bool("twin uses dv_Cs from db (9192631770)",
         dv_db == mpf("9192631770"),
         "dv_Cs = %s" % mp.nstr(dv_db, 11))

# At v=0: both twins should agree
tp0 = twin_paradox(db, "0", "10")
chk_close("twin at v=0: years_B = years_A",
          tp0["years_B"], tp0["years_A"], 10)
chk_close("twin at v=0: cycle difference = 0",
          tp0["cycle_difference"], mpf("0"), 10)


# ================================================================
section("ds^2 MINKOWSKI INTERVAL")
# ================================================================

# Lightlike: ds^2 = 0 for dt=1, dx=c
ds_light = ds_squared("1", str(c))
chk_close("ds^2 = 0 for light (dt=1, dx=c)", ds_light, mpf("0"), 10)

# Timelike: ds^2 < 0 for stationary particle (dt=1, dx=0)
ds_time = ds_squared("1", "0")
chk_bool("ds^2 < 0 for stationary (timelike)",
         ds_time < mpf("0"),
         "ds^2 = %s" % mp.nstr(ds_time, 6))

# Spacelike: ds^2 > 0 for simultaneous separation (dt=0, dx=1)
ds_space = ds_squared("0", "1")
chk_bool("ds^2 > 0 for simultaneous separation (spacelike)",
         ds_space > mpf("0"),
         "ds^2 = %s" % mp.nstr(ds_space, 6))


# ================================================================
section("MOND a0: PHYSICS VERIFICATION")
# ================================================================

a0 = mond_a0(db)

# a0 should be ~ 1.2e-10 m/s^2 (published MOND)
chk_bool("a0 ~ 1.2e-10 m/s^2 (within factor 2)",
         mpf("0.5e-10") < a0 < mpf("2.5e-10"),
         "a0 = %s m/s^2" % mp.nstr(a0, 4))

# a0 = c*H0/(8*R2) should equal c*H0/(2*pi)
H0_SI = mpf("67.4") * mpf("1000") / mpf("3.086e22")
a0_twopi = c * H0_SI / (mpf("2") * mpi)
chk_close("a0 via 8*R2 = a0 via 2*pi (identity)",
          a0, a0_twopi, 12)

# Transition radius for Earth
r_a0_earth = mond_transition_radius(db, M_e)
expected_r_a0 = msqrt(G * M_e / a0)
chk_close("mond_transition_radius(Earth) matches sqrt(GM/a0)",
          r_a0_earth, expected_r_a0, 8)

chk_bool("Earth a0 radius > Hill sphere",
         r_a0_earth > rh_earth,
         "r_a0=%s > R_Hill=%s" % (
             mp.nstr(r_a0_earth, 4), mp.nstr(rh_earth, 4)))

# Sun transition
r_a0_sun = mond_transition_radius(db, M_s)
chk_bool("Sun a0 radius > 100 AU",
         r_a0_sun > mpf("100") * AU,
         "r_a0_sun = %s AU" % mp.nstr(r_a0_sun / AU, 3))


# ================================================================
section("INTERNAL CONSISTENCY CHECKS")
# ================================================================

# R2 family from db
R2_db = _R2(db)
chk_close("_R2(db) = pi/4", R2_db, mpi / 4, 30)
chk_close("_eight_R2(db) = 2*pi", _eight_R2(db), mpf("2") * mpi, 30)

# grav_coupling = v_esc^2 / (2c^2)
gc = grav_coupling(M_e, R_e)
ve = escape_velocity(M_e, R_e)
chk_close("GM/(Rc^2) = v_esc^2/(2c^2)",
          gc, (ve / c) ** 2 / mpf("2"), 8)

# Process rate shift ~ GM/(Rc^2) for weak fields
pr = process_rate_ratio(M_e, R_e)
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

print("  SECTIONS TESTED:")
print("    Scale conversion:      E <-> distance round-trip")
print("    Boundary search:       find, nearest, between, count")
print("    Hubble data:           H0 values, ratio, tension, r(N), running")
print("    Hubble falsification:  F1 strict/soft agree with lib")
print("    Gravity coupling:      GM/(rc^2), binding, escape velocity")
print("    Hill spheres:          Earth, Moon size ranges")
print("    Kepler via R2:         64R2^2=4pi^2, Earth and Jupiter periods")
print("    Process rate:          Earth, GPS, shift ~ coupling")
print("    GPS correction:        grav/vel/total, ~38 us/day")
print("    Muon lifetime:         rest, 0.99c, monotonic gamma")
print("    Twin paradox:          aging, cycle counts, v=0 identity")
print("    ds^2 interval:         lightlike, timelike, spacelike")
print("    MOND a0:               value, 8R2=2pi, transition radii")
print("    Internal consistency:  coupling identities, weak-field")
print()

if n_fail == 0:
    print("  CHUNK 3 HELPERS: OPERATIONAL")
    print("  All boundary, Hubble, gravity, process rate, muon, Kepler,")
    print("  and MOND computations verified against platform and physics.")
else:
    print("  CHUNK 3 HELPERS: %d FAILURES — INVESTIGATE" % n_fail)

print()
print("=" * 70)
print("DATA-5 CHUNK 3 TEST COMPLETE")
print("=" * 70)

