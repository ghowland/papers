#!/usr/bin/env python3
"""
DATA-5 CHUNK 2 TEST: DOMAIN HELPERS vs PLATFORM LIBRARIES
============================================================
Tests every chunk 2 helper function against phys24_domain_lib.py.

For each domain computation: chunk 2 computes through db R2,
the platform library computes directly. Results must match
to 10+ digits.

Also tests:
  - R2 cancellation identities (RC product, K_J*R_K)
  - Cross-domain area consistency
  - All engineering data matches domain lib exactly
  - Bessel zeros and Airy constant from Q335 R2
  - BCS gap ratio pi/e^gamma from Q335 R2
  - Vena contracta pi/(pi+2) from Q335 R2
  - Normalizations 1/(8R2), 1/sqrt(8R2)

Run:  python data_5_chunk2_test.py
Requires: phys24_lib.py, phys24_domain_lib.py, data_5_objects.py,
          data_5_populate.py, data_5_helpers_domain.py
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
from phys24_domain_lib import (
    R2, R4, EIGHT_R2, FOUR_R2, SIXTEEN_R2,
    J11, J01, AIRY_CONST, C_C_EXACT,
    domain_area as lib_domain_area,
    domain_area_from_radius as lib_domain_area_radius,
    airy_resolution as lib_airy_resolution,
    spot_area as lib_spot_area,
    rayleigh_range as lib_rayleigh_range,
    beam_divergence as lib_beam_divergence,
    wire_resistance as lib_wire_resistance,
    circular_capacitance as lib_circular_capacitance,
    pipe_flow as lib_pipe_flow,
    orifice_flow as lib_orifice_flow,
    hagen_poiseuille as lib_hagen_poiseuille,
    helmholtz_frequency as lib_helmholtz_freq,
    sound_intensity as lib_sound_intensity,
    thermal_radiation as lib_thermal_radiation,
    antenna_effective_area as lib_antenna_area,
    friis_path_loss as lib_friis,
    fiber_V_number as lib_fiber_V,
    fiber_mode_area as lib_fiber_mode_area,
    rayleigh_scattering_loss as lib_rayleigh_loss,
    gaussian_peak as lib_gaussian_peak,
    fourier_norm as lib_fourier_norm,
    gaussian_norm as lib_gaussian_norm,
    litho_resolution as lib_litho,
    disc_spot_size as lib_disc_spot_size,
    disc_spot_area as lib_disc_spot_area,
    disc_area as lib_disc_area,
    speaker_cone_area as lib_speaker_cone_area,
    awg_area as lib_awg_area,
    awg_resistance_per_m as lib_awg_resistance,
    rf_wavelength as lib_rf_wavelength,
    fspl_dB as lib_fspl_dB,
    OPTICAL_DISCS, FIBER_OPTICS, SPEAKERS, AWG_DATA,
    CU_RESISTIVITY, EPSILON_0,
    BCS_DATA,
)


# ================================================================
# DATA-5 SYSTEM (what we are testing)
# ================================================================

from data_5_objects import *
from data_5_populate import init_data5
from data_5_helpers_domain import *

db = init_data5()


# ================================================================
# TEST INFRASTRUCTURE
# ================================================================

checks = []


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
print("DATA-5 CHUNK 2 TEST: DOMAIN HELPERS vs PLATFORM")
print("=" * 70)
print()
print("  db loaded: %d objects" % db.count())
print()


# ================================================================
section("R2 CORE: CHUNK 2 vs DOMAIN LIB CONSTANTS")
# ================================================================

chk_close("_R2(db) matches domain lib R2", _R2(db), R2, 30)
chk_close("_R4(db) matches domain lib R4", _R4(db), R4, 30)
chk_close("_four_R2(db) matches FOUR_R2", _four_R2(db), FOUR_R2, 30)
chk_close("_eight_R2(db) matches EIGHT_R2", _eight_R2(db), EIGHT_R2, 30)
chk_close("_sixteen_R2(db) matches SIXTEEN_R2", _sixteen_R2(db), SIXTEEN_R2, 30)

chk_close("_airy_const(db) matches lib AIRY_CONST",
          _airy_const(db), AIRY_CONST, 12)

chk_close("vena_contracta(db) matches lib C_C_EXACT",
          vena_contracta(db), C_C_EXACT, 12)


# ================================================================
section("R2 AREA: CHUNK 2 vs DOMAIN LIB")
# ================================================================

# Test with multiple diameters
for d_str, d_val in [("0.120", mpf("0.120")),
                      ("0.300", mpf("0.300")),
                      ("2.053e-3", mpf("2.053e-3")),
                      ("0.305", mpf("0.305"))]:
    got = R2_area(db, d_str)
    expected = lib_domain_area(d_val)
    chk_close("R2_area(db, %s) matches domain_area" % d_str,
              got, expected, 12)

# Radius form
got_r = R2_area_from_radius(db, "0.060")
expected_r = lib_domain_area_radius(mpf("0.060"))
chk_close("R2_area_from_radius matches domain_area_from_radius",
          got_r, expected_r, 12)


# ================================================================
section("OPTICAL DISCS: CHUNK 2 vs DOMAIN LIB")
# ================================================================

for fmt in ["CD", "DVD", "Blu-ray"]:
    ds = disc_spot(db, fmt)
    lib_spot_d = lib_disc_spot_size(fmt)
    lib_spot_a = lib_disc_spot_area(fmt)
    lib_da = lib_disc_area(fmt)

    chk_close("%s spot diameter matches lib" % fmt,
              ds["spot_m"], lib_spot_d, 10)
    chk_close("%s spot area matches lib" % fmt,
              ds["area_m2"], lib_spot_a, 10)
    chk_close("%s disc area matches lib" % fmt,
              ds["disc_area_m2"], lib_da, 10)

# Airy resolution direct call
for lam_str, na_str, lam_val, na_val in [
    ("780e-9", "0.45", mpf("780e-9"), mpf("0.45")),
    ("405e-9", "0.85", mpf("405e-9"), mpf("0.85")),
]:
    got = airy_resolution(db, lam_str, na_str)
    expected = lib_airy_resolution(lam_val, na_val, mode="NA")
    chk_close("airy_resolution(db, %s, %s) matches lib" % (lam_str, na_str),
              got, expected, 10)


# ================================================================
section("GAUSSIAN BEAM: CHUNK 2 vs DOMAIN LIB")
# ================================================================

w0 = mpf("5e-6")
lam = mpf("632.8e-9")

got_zr = rayleigh_range(db, w0, lam)
exp_zr = lib_rayleigh_range(w0, lam)
chk_close("rayleigh_range matches lib", got_zr, exp_zr, 10)

got_div = beam_divergence(db, w0, lam)
exp_div = lib_beam_divergence(w0, lam)
chk_close("beam_divergence matches lib", got_div, exp_div, 10)


# ================================================================
section("FIBER OPTICS: CHUNK 2 vs DOMAIN LIB")
# ================================================================

# Mode area at 1550nm
smf_MFD = mpf("10.4e-6")
got_ma = fiber_mode_area(db, smf_MFD)
exp_ma = lib_fiber_mode_area("SMF-28", 1550)
chk_close("fiber_mode_area(SMF-28@1550) matches lib",
          got_ma, exp_ma, 10)

# V number
core_r = mpf("62.5e-6")
NA_smf = mpf("0.14")
lam_cut = mpf("1260e-9")
got_V = fiber_V_number(db, core_r, NA_smf, lam_cut)
exp_V = lib_fiber_V(core_r, NA_smf, lam_cut)
chk_close("fiber_V_number matches lib", got_V, exp_V, 10)

# Single mode check
chk_bool("SMF-28 at 1550nm is single mode",
         fiber_single_mode(db, core_r, NA_smf, mpf("1550e-9")),
         "V should be < j01 = 2.405")

# Rayleigh loss
got_rl = rayleigh_loss("1.550")
exp_rl = lib_rayleigh_loss(mpf("1.550"))
chk_close("rayleigh_loss(1.550um) matches lib", got_rl, exp_rl, 10)

got_rl2 = rayleigh_loss("1.310")
exp_rl2 = lib_rayleigh_loss(mpf("1.310"))
chk_close("rayleigh_loss(1.310um) matches lib", got_rl2, exp_rl2, 10)


# ================================================================
section("SPEAKER CONES: CHUNK 2 vs DOMAIN LIB")
# ================================================================

for key in ["12inch", "8inch", "1inch"]:
    d_eff = SPEAKER_DATA[key]["d_eff_m"]
    got = speaker_cone_area(db, d_eff)
    expected = lib_speaker_cone_area(key)
    chk_close("speaker_cone_area(%s) matches lib" % key,
              got, expected, 10)


# ================================================================
section("WIRE & CIRCUITS: CHUNK 2 vs DOMAIN LIB")
# ================================================================

# Wire area
for gauge in ["12", "14", "22", "36"]:
    got = wire_area(db, AWG[gauge])
    expected = lib_awg_area(gauge)
    chk_close("wire_area(AWG %s) matches lib" % gauge,
              got, expected, 10)

# Wire resistance
for gauge in ["12", "14"]:
    got = wire_resistance(db, _CU_RHO, "1", AWG[gauge])
    expected = lib_awg_resistance(gauge)
    chk_close("wire_resistance(AWG %s, 1m Cu) matches lib" % gauge,
              got, expected, 10)

# Capacitance
d_cap = mpf("0.010")
gap_cap = mpf("1e-3")
got_cap = circular_capacitance(db, d_cap, gap_cap)
exp_cap = lib_circular_capacitance(d_cap, gap_cap)
chk_close("circular_capacitance(10mm, 1mm) matches lib",
          got_cap, exp_cap, 10)


# ================================================================
section("R2 CANCELLATION: RC PRODUCT")
# ================================================================

# R*C must be R2-independent
d12 = AWG["12"]
rc = rc_product(db, _CU_RHO, "1", d12, "1e-3")
diff_rc = abs(rc["RC"] - rc["RC_direct"])

chk_bool("RC with R2 = RC without R2 (cancellation)",
         diff_rc < mpf("1e-30"),
         "diff = %s" % mp.nstr(diff_rc, 4))

# Also test numerically: RC = rho * eps0 * L / t
expected_RC = mpf(str(_CU_RHO)) * _EPSILON_0 * mpf("1") / mpf("1e-3")
chk_close("RC product matches rho*eps0*L/t exactly",
          rc["RC"], expected_RC, 15)


# ================================================================
section("FLOW & THERMAL: CHUNK 2 vs DOMAIN LIB")
# ================================================================

# Pipe flow
d_pipe = mpf("0.050")
v_pipe = mpf("2.0")
got_pf = pipe_flow(db, d_pipe, v_pipe)
exp_pf = lib_pipe_flow(d_pipe, v_pipe)
chk_close("pipe_flow(50mm, 2m/s) matches lib", got_pf, exp_pf, 10)

# Orifice flow with default Cd
d_or = mpf("0.025")
dP_or = mpf("100000")
rho_or = mpf("1000")
got_of = orifice_flow(db, d_or, dP_or, rho_or)
exp_of = lib_orifice_flow(d_or, dP_or, rho_or)
chk_close("orifice_flow(25mm, 100kPa, water) matches lib",
          got_of, exp_of, 10)

# Hagen-Poiseuille
d_hp = mpf("0.010")
dP_hp = mpf("1000")
mu_hp = mpf("0.001")
L_hp = mpf("1")
got_hp = hagen_poiseuille(db, d_hp, dP_hp, mu_hp, L_hp)
exp_hp = lib_hagen_poiseuille(d_hp, dP_hp, mu_hp, L_hp)
chk_close("hagen_poiseuille(10mm, 1kPa, water, 1m) matches lib",
          got_hp, exp_hp, 10)

# Thermal radiation
got_th = thermal_radiation(db, "1", "300", "0.100")
exp_th = lib_thermal_radiation(mpf("1"), mpf("300"), mpf("0.100"))
chk_close("thermal_radiation(e=1, 300K, 100mm) matches lib",
          got_th, exp_th, 10)

# Sound intensity
got_si = sound_intensity(db, "1", "10")
exp_si = lib_sound_intensity(mpf("1"), mpf("10"))
chk_close("sound_intensity(1W, 10m) matches lib", got_si, exp_si, 10)

# Helmholtz
got_hz = helmholtz_freq(db, "0.076", "0.15", "0.050")
exp_hz = lib_helmholtz_freq(mpf("0.076"), mpf("0.15"), mpf("0.050"))
chk_close("helmholtz_freq(76mm, 15cm, 50L) matches lib",
          got_hz, exp_hz, 10)


# ================================================================
section("RF & TELECOM: CHUNK 2 vs DOMAIN LIB")
# ================================================================

# RF wavelength
gps_f = mpf("1575.42e6")
got_lam = rf_wavelength(gps_f)
exp_lam = lib_rf_wavelength(gps_f)
chk_close("rf_wavelength(GPS L1) matches lib", got_lam, exp_lam, 10)

# FSPL
got_fspl = fspl_dB(db, "1000", gps_f)
exp_fspl = lib_fspl_dB(mpf("1000"), gps_f)
chk_close("fspl_dB(1km, GPS L1) matches lib", got_fspl, exp_fspl, 8)

# Antenna area
got_aa = antenna_area(db, "1", got_lam)
exp_aa = lib_antenna_area(mpf("1"), exp_lam)
chk_close("antenna_area(isotropic, GPS L1) matches lib",
          got_aa, exp_aa, 10)


# ================================================================
section("SEMICONDUCTOR: CHUNK 2 vs DOMAIN LIB")
# ================================================================

euv = mpf("13.5e-9")
na_euv = mpf("0.33")
got_litho = litho_resolution(db, euv, na_euv)
exp_litho = lib_litho(euv, na_euv)
chk_close("litho_resolution(EUV, 0.33) matches lib",
          got_litho, exp_litho, 10)

# Wafer area
got_wafer = R2_area(db, "0.300")
exp_wafer = lib_domain_area(mpf("0.300"))
chk_close("wafer area R2*(0.3)^2 matches lib",
          got_wafer, exp_wafer, 12)


# ================================================================
section("NORMALIZATIONS: CHUNK 2 vs DOMAIN LIB AND MPMATH")
# ================================================================

# Fourier: 1/(2*pi)
got_fn = fourier_norm(db)
exp_fn = lib_fourier_norm()
chk_close("fourier_norm matches lib 1/(2*pi)", got_fn, exp_fn, 15)
chk_close("fourier_norm matches mpmath 1/(2*pi)",
          got_fn, mpf("1") / (mpf("2") * mpi), 15)

# Gaussian: 1/sqrt(2*pi)
got_gn = gaussian_norm(db)
exp_gn = lib_gaussian_norm()
chk_close("gaussian_norm matches lib 1/sqrt(2*pi)", got_gn, exp_gn, 15)
chk_close("gaussian_norm matches mpmath",
          got_gn, mpf("1") / msqrt(mpf("2") * mpi), 15)

# Gaussian peak
got_gp = gaussian_peak(db, "1e15", "50e-7")
exp_gp = lib_gaussian_peak(mpf("1e15"), mpf("50e-7"))
chk_close("gaussian_peak(1e15, 50nm) matches lib", got_gp, exp_gp, 10)

# BCS gap: pi/e^gamma
got_bcs = bcs_gap(db)
exp_bcs = BCS_DATA["gap_ratio_exact"]
chk_close("bcs_gap = pi/e^gamma matches lib", got_bcs, exp_bcs, 10)
chk_close("bcs_gap ~ 1.76388", got_bcs, mpf("1.76388"), 5)

# Vena contracta: pi/(pi+2)
got_vc = vena_contracta(db)
exp_vc = mpi / (mpi + mpf("2"))
chk_close("vena_contracta = pi/(pi+2) matches mpmath",
          got_vc, exp_vc, 15)


# ================================================================
section("ENGINEERING DATA MATCHES DOMAIN LIB EXACTLY")
# ================================================================

# Disc data
for fmt in ["CD", "DVD", "Blu-ray"]:
    lib_disc = OPTICAL_DISCS[fmt]
    ch2_disc = DISC_DATA[fmt]
    chk_close("%s lambda matches domain lib" % fmt,
              ch2_disc["lambda_m"], lib_disc["laser_wavelength_m"], 15)
    chk_close("%s NA matches domain lib" % fmt,
              ch2_disc["NA"], lib_disc["NA"], 15)

# AWG wire data
for gauge in ["12", "14", "22"]:
    lib_d = AWG_DATA[gauge]["diameter_m"]
    ch2_d = AWG[gauge]
    chk_close("AWG %s diameter matches domain lib" % gauge,
              ch2_d, lib_d, 15)

# Fiber data
chk_close("SMF-28 MFD@1550 matches domain lib",
          FIBER_DATA["SMF-28"]["MFD_1550_m"],
          FIBER_OPTICS["SMF-28"]["MFD_1550_m"], 15)

# Cu resistivity
chk_close("CU_RHO matches domain lib",
          _CU_RHO, CU_RESISTIVITY, 15)

# Epsilon0
chk_close("EPSILON_0 matches domain lib",
          _EPSILON_0, EPSILON_0, 15)


# ================================================================
section("CROSS-DOMAIN CONSISTENCY")
# ================================================================

# Same diameter through different domain functions must give same R2*d^2
test_d = mpf("0.050")  # 50mm
area_direct = R2_area(db, test_d)
area_pipe = pipe_flow(db, test_d, "1")  # Q = R2*d^2*v, at v=1 -> Q = A
area_wire = _CU_RHO / wire_resistance(db, _CU_RHO, "1", test_d)  # R = rho/(R2*d^2)
area_cap = circular_capacitance(db, test_d, "1") / _EPSILON_0  # C/eps0 = R2*d^2/t, at t=1
area_speaker = speaker_cone_area(db, test_d)

chk_close("pipe Q at v=1 = R2*d^2", area_pipe, area_direct, 12)
chk_close("rho/R from wire = R2*d^2", area_wire, area_direct, 12)
chk_close("C/eps0 at t=1 = R2*d^2", area_cap, area_direct, 12)
chk_close("speaker Sd = R2*d^2", area_speaker, area_direct, 12)


# ================================================================
section("K_J * R_K CANCELLATION (if h and e in db)")
# ================================================================

h_obj = db.get("const.h")
e_obj = db.get("const.e_charge")

if h_obj is not None and e_obj is not None:
    h_val = f2m(h_obj.value)
    e_val = f2m(e_obj.value)
    K_J = mpf("2") * e_val / h_val
    R_K = h_val / (e_val ** 2)
    product = K_J * R_K
    expected = mpf("2") / e_val
    diff_kj = abs(product - expected)
    chk_bool("K_J * R_K = 2/e (R2 cancels in h)",
             diff_kj < mpf("1e-20"),
             "diff = %s" % mp.nstr(diff_kj, 4))
else:
    print("  [SKIP] K_J*R_K: h or e_charge not in db")


# ================================================================
section("JUST INTONATION AND SAMPLE RATES: EXACT FRACTIONS")
# ================================================================

chk_bool("perfect_fifth = 3/2",
         JUST_INTONATION["perfect_fifth"] == Fraction(3, 2))
chk_bool("perfect_fourth = 4/3",
         JUST_INTONATION["perfect_fourth"] == Fraction(4, 3))
chk_bool("CD sample rate = 44100",
         SAMPLE_RATES["CD"] == Fraction(44100, 1))
chk_bool("44100 = 2^2 * 3^2 * 5^2 * 7^2",
         SAMPLE_RATES["CD"] == Fraction(4 * 9 * 25 * 49, 1))


# ================================================================
# SUMMARY
# ================================================================

print()
print("=" * 70)
print("DATA-5 CHUNK 2 TEST SUMMARY")
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

print("  COMPARISON TO PLATFORM:")
print("    phys24_domain_lib self-test:  40/40")
print("    chunk 2 test:                 %d/%d" % (n_pass, n_total))
print()

if n_fail == 0:
    print("  CHUNK 2 HELPERS: OPERATIONAL")
    print("  All domain computations through db R2 match platform exactly.")
    print("  All engineering data matches domain lib constants.")
    print("  R2 cancellation verified numerically.")
    print("  Cross-domain consistency confirmed: same R2*d^2 everywhere.")
else:
    print("  CHUNK 2 HELPERS: %d FAILURES — INVESTIGATE" % n_fail)

print()
print("=" * 70)
print("DATA-5 CHUNK 2 TEST COMPLETE")
print("=" * 70)
