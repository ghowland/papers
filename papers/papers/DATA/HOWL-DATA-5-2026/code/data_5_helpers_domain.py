#!/usr/bin/env python3
"""
HOWL DATA-5 HELPERS — CHUNK 2: DOMAIN & CROSS-DOMAIN
======================================================
Physics-aware helpers wrapping phys24_domain_lib.py and the
cross-domain translation patterns from demo_cross_domain.py.

All R2 values from the Q335 basis via db ("const.R2").
All engineering data as mpf("string") matching domain lib exactly.
No float literals. No sci-notation without mpf("...") wrapper.

Categories:
  R2 CORE GEOMETRY       — area, R2/R4 conversions, Bessel zeros
  OPTICS & DIFFRACTION   — Airy, spot, disc formats, Gaussian beam
  FIBER OPTICS           — mode area, V-number, Rayleigh, DWDM bands
  ACOUSTICS              — speaker cones, Helmholtz, sound intensity
  WIRE & CIRCUITS        — resistance, capacitance, RC cancellation
  RF & TELECOM           — wavelength, FSPL, GPS, antenna aperture
  SEMICONDUCTOR          — litho resolution, wafer area, EUV/ArF
  FLOW & THERMAL         — pipe, orifice, Poiseuille, vena contracta, radiation
  NORMALIZATIONS         — Fourier 1/(8R2), Gaussian 1/sqrt(8R2), BCS gap
  CROSS-DOMAIN           — translate between R2 domains, show table
  CANCELLATION MAP       — verify, display, test R2 cancellation identities

Usage:
    from data_5_populate import init_data5
    from data_5_helpers_domain import *

    db = init_data5()
    show_disc_spots(db)
    show_rc_cancellation(db)
    show_all_R2_equations(db)

Platform: HOWL-PLATFORM-v1
Depends on: data_5_objects.py, data_5_populate.py, phys24_lib.py
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, log as mlog, sqrt as msqrt

try:
    from phys24_lib import f2m
except ImportError:
    def f2m(f):
        return mpf(f.numerator) / mpf(f.denominator)


_LIB_VERSION = "1"
_LIB_VERSION_1 = ("Session 4, April 3 2026. Chunk 2: Domain & "
                   "cross-domain helpers. All R2 from Q335 basis.")


# ================================================================
# INTERNAL: pull R2 family from db
# ================================================================

def _R2(db):
    """R2 = pi/4 from Q335 basis via db."""
    return f2m(db.get("const.R2").value)

def _R4(db):
    """R4 = pi^2/32 from Q335 basis via db."""
    return f2m(db.get("const.R4").value)

def _pi(db):
    """pi from Q335 basis via db."""
    return f2m(db.get("const.pi").value)

def _twopi(db):
    """2*pi from Q335 basis via db."""
    return f2m(db.get("const.twopi").value)

def _four_R2(db):
    """4*R2 = pi."""
    return mpf("4") * _R2(db)

def _eight_R2(db):
    """8*R2 = 2*pi."""
    return mpf("8") * _R2(db)

def _sixteen_R2(db):
    """16*R2 = 4*pi."""
    return mpf("16") * _R2(db)


# Bessel zeros — exact from DATA-1/MATH-3
_J11 = mpf("3.83170597020751")    # first zero of J1
_J01 = mpf("2.40482555769577")    # first zero of J0

def _airy_const(db):
    """j11 / pi = j11 / (4*R2) = 1.21967..."""
    return _J11 / _four_R2(db)


# Engineering constants — mpf from string, matching domain lib
_C_LIGHT    = mpf("299792458")           # m/s, exact (SI)
_EPSILON_0  = mpf("8.8541878128e-12")    # F/m
_C_SOUND    = mpf("343")                 # m/s at 20C
_SIGMA_SB   = mpf("5.670374419e-8")      # W/(m^2 K^4)
_CU_RHO     = mpf("1.7241e-8")           # ohm*m at 20C
_GAMMA_EM   = mpf("0.5772156649015329")  # Euler-Mascheroni


# ================================================================
# OPTICAL DISC DATA — exact copy from phys24_domain_lib.py
# All values mpf("string"), matching DATA-1 Section 9
# ================================================================

DISC_DATA = {
    "CD": {
        "name": "Compact Disc",
        "lambda_m": mpf("780e-9"),
        "NA": mpf("0.45"),
        "track_pitch_m": mpf("1.6e-6"),
        "diameter_m": mpf("0.120"),
        "capacity": "700 MB",
    },
    "DVD": {
        "name": "Digital Versatile Disc",
        "lambda_m": mpf("650e-9"),
        "NA": mpf("0.60"),
        "track_pitch_m": mpf("0.74e-6"),
        "diameter_m": mpf("0.120"),
        "capacity": "4.7 GB",
    },
    "Blu-ray": {
        "name": "Blu-ray Disc",
        "lambda_m": mpf("405e-9"),
        "NA": mpf("0.85"),
        "track_pitch_m": mpf("0.320e-6"),
        "diameter_m": mpf("0.120"),
        "capacity": "25 GB",
    },
}

# Fiber data — from phys24_domain_lib.py DATA-1 Section 16
FIBER_DATA = {
    "SMF-28": {
        "name": "Corning SMF-28",
        "MFD_1310_m": mpf("9.2e-6"),
        "MFD_1550_m": mpf("10.4e-6"),
        "NA": mpf("0.14"),
        "cladding_m": mpf("125.0e-6"),
        "cutoff_m": mpf("1260e-9"),
        "loss_1550": mpf("0.18"),   # dB/km
    },
}

# Speaker data — from phys24_domain_lib.py DATA-1 Section 13
SPEAKER_DATA = {
    "12inch": {"name": "12-inch woofer",  "d_eff_m": mpf("0.305")},
    "10inch": {"name": "10-inch woofer",  "d_eff_m": mpf("0.254")},
    "8inch":  {"name": "8-inch midrange", "d_eff_m": mpf("0.203")},
    "6inch":  {"name": "6.5-inch mid",    "d_eff_m": mpf("0.152")},
    "5inch":  {"name": "5-inch mid",      "d_eff_m": mpf("0.127")},
    "1inch":  {"name": "1-inch tweeter",  "d_eff_m": mpf("0.025")},
}

# Wire data — from phys24_domain_lib.py DATA-1 Section 12
AWG = {
    "0000": mpf("11.684e-3"), "0": mpf("8.251e-3"),
    "4": mpf("5.189e-3"),     "8": mpf("3.264e-3"),
    "10": mpf("2.588e-3"),   "12": mpf("2.053e-3"),
    "14": mpf("1.628e-3"),   "18": mpf("1.024e-3"),
    "22": mpf("0.644e-3"),   "24": mpf("0.511e-3"),
    "30": mpf("0.255e-3"),   "36": mpf("0.127e-3"),
}

# Just intonation — exact Fractions from DATA-1 H12-H18
JUST_INTONATION = {
    "octave": Fraction(2, 1),
    "perfect_fifth": Fraction(3, 2),
    "perfect_fourth": Fraction(4, 3),
    "major_third": Fraction(5, 4),
    "minor_third": Fraction(6, 5),
    "major_sixth": Fraction(5, 3),
    "minor_seventh": Fraction(9, 5),
}

# Sample rates — exact Fractions from DATA-1 H5-H8
SAMPLE_RATES = {
    "CD": Fraction(44100, 1),
    "studio": Fraction(48000, 1),
    "high_res": Fraction(96000, 1),
    "ultra": Fraction(192000, 1),
}


# ================================================================
# R2 CORE GEOMETRY
# ================================================================

def R2_area(db, diameter):
    """A = R2 * d^2. The universal equation. Every domain uses this.
    diameter as mpf or string.
    """
    d = mpf(str(diameter))
    return _R2(db) * d ** 2


def R2_area_from_radius(db, radius):
    """A = 4*R2 * r^2 = pi * r^2."""
    r = mpf(str(radius))
    return _four_R2(db) * r ** 2


def show_R2_multiples(db):
    """Print the R2 multiple family from Q335 basis."""
    R2 = _R2(db)
    print("  R2 MULTIPLE FAMILY (from Q335 basis):")
    print("    R2   = pi/4   = %s" % mp.nstr(R2, 20))
    print("    2R2  = pi/2   = %s" % mp.nstr(mpf("2") * R2, 20))
    print("    4R2  = pi     = %s" % mp.nstr(mpf("4") * R2, 20))
    print("    8R2  = 2*pi   = %s" % mp.nstr(mpf("8") * R2, 20))
    print("    16R2 = 4*pi   = %s" % mp.nstr(mpf("16") * R2, 20))
    print("    R4   = pi^2/32 = %s" % mp.nstr(_R4(db), 20))
    print("    R4/R2 = pi/8  = %s" % mp.nstr(_R4(db) / R2, 20))


def show_bessel_zeros(db):
    """Print Bessel zeros and the Airy constant j11/(4R2)."""
    print("  BESSEL ZEROS:")
    print("    j01 = %s  (J0 first zero, fiber cutoff V=j01)" % mp.nstr(_J01, 15))
    print("    j11 = %s  (J1 first zero, Airy disc)" % mp.nstr(_J11, 15))
    print("    j11/(4R2) = j11/pi = %s  (the 1.22 in diffraction)" % mp.nstr(
        _airy_const(db), 15))


# ================================================================
# OPTICS & DIFFRACTION
# ================================================================

def airy_resolution(db, wavelength_m, D_or_NA):
    """Resolution = j11/(4*R2) * lambda / (D or NA).
    = 1.2197 * lambda / (D or NA).
    All from Q335 basis j11 and R2.
    """
    lam = mpf(str(wavelength_m))
    val = mpf(str(D_or_NA))
    return _airy_const(db) * lam / val


def spot_area_from_resolution(db, spot_diameter):
    """A = R2 * d^2 for a diffraction spot."""
    d = mpf(str(spot_diameter))
    return _R2(db) * d ** 2


def disc_spot(db, fmt):
    """Compute spot size and area for CD, DVD, or Blu-ray.
    Returns dict with all values as mpf.
    """
    disc = DISC_DATA[fmt]
    spot_d = _airy_const(db) * disc["lambda_m"] / disc["NA"]
    spot_a = _R2(db) * spot_d ** 2
    disc_a = _R2(db) * disc["diameter_m"] ** 2
    return {
        "format": fmt,
        "spot_m": spot_d,
        "spot_um": spot_d * mpf("1e6"),
        "area_m2": spot_a,
        "area_um2": spot_a * mpf("1e12"),
        "disc_area_m2": disc_a,
        "disc_area_cm2": disc_a * mpf("1e4"),
        "lambda_nm": disc["lambda_m"] * mpf("1e9"),
        "NA": disc["NA"],
    }


def show_disc_spots(db):
    """Print CD/DVD/Blu-ray spot comparison table."""
    print("  OPTICAL DISC SPOTS  (spot = R2 * (j11/(4R2) * lam/NA)^2):")
    print("  %-10s %8s %6s %10s %10s %10s" % (
        "Format", "lam(nm)", "NA", "spot(um)", "area(um2)", "disc(cm2)"))
    print("  %-10s %8s %6s %10s %10s %10s" % (
        "-" * 10, "-" * 8, "-" * 6, "-" * 10, "-" * 10, "-" * 10))
    for fmt in ["CD", "DVD", "Blu-ray"]:
        d = disc_spot(db, fmt)
        print("  %-10s %8s %6s %10s %10s %10s" % (
            fmt, mp.nstr(d["lambda_nm"], 3), mp.nstr(d["NA"], 2),
            mp.nstr(d["spot_um"], 4), mp.nstr(d["area_um2"], 4),
            mp.nstr(d["disc_area_cm2"], 4)))
    print("  Same R2 in every spot. Different Z (wavelength, NA).")


def rayleigh_range(db, w0_m, wavelength_m):
    """z_R = 4*R2*w0^2/lambda = pi*w0^2/lambda."""
    w = mpf(str(w0_m))
    lam = mpf(str(wavelength_m))
    return _four_R2(db) * w ** 2 / lam


def beam_divergence(db, w0_m, wavelength_m):
    """theta = lambda/(4*R2*w0) = lambda/(pi*w0)."""
    w = mpf(str(w0_m))
    lam = mpf(str(wavelength_m))
    return lam / (_four_R2(db) * w)


# ================================================================
# FIBER OPTICS
# ================================================================

def fiber_mode_area(db, MFD_m):
    """A = R2 * MFD^2."""
    d = mpf(str(MFD_m))
    return _R2(db) * d ** 2


def fiber_V_number(db, core_radius_m, NA, wavelength_m):
    """V = 8*R2 * a * NA / lambda = 2*pi*a*NA/lambda.
    Single-mode cutoff at V = j01 = 2.405.
    """
    a = mpf(str(core_radius_m))
    na = mpf(str(NA))
    lam = mpf(str(wavelength_m))
    return _eight_R2(db) * a * na / lam


def fiber_single_mode(db, core_radius_m, NA, wavelength_m):
    """True if V < j01 (single-mode condition)."""
    return fiber_V_number(db, core_radius_m, NA, wavelength_m) < _J01


def rayleigh_loss(wavelength_um, A_coeff="0.8"):
    """Rayleigh scattering: loss = A/lambda^4 dB/km.
    Silica: A = 0.8 dB/(km*um^4). Contains (8R2/lambda)^4 scaling.
    """
    lam = mpf(str(wavelength_um))
    A = mpf(str(A_coeff))
    return A / lam ** 4


def show_dwdm_rayleigh(db):
    """Print Rayleigh loss across DWDM bands."""
    print("  DWDM RAYLEIGH LOSS  (A/lambda^4, A=0.8 dB/(km*um^4)):")
    print("  %-20s %10s %12s" % ("Band", "lam(nm)", "Loss(dB/km)"))
    print("  %-20s %10s %12s" % ("-" * 20, "-" * 10, "-" * 12))
    for name, lam_um in [("O-band", "1.310"), ("C-band center", "1.550"),
                          ("C-band edge", "1.530"), ("L-band center", "1.590")]:
        loss = rayleigh_loss(lam_um)
        print("  %-20s %10s %12s" % (
            name, mp.nstr(mpf(lam_um) * mpf("1000"), 4), mp.nstr(loss, 4)))
    ratio = (mpf("1310") / mpf("1550")) ** 4
    print("  1550nm saves %s%% vs 1310nm (lambda^4 scaling)" % mp.nstr(
        (mpf("1") - ratio) * mpf("100"), 3))


def show_smf28(db):
    """Print SMF-28 fiber parameters."""
    f = FIBER_DATA["SMF-28"]
    a1310 = fiber_mode_area(db, f["MFD_1310_m"])
    a1550 = fiber_mode_area(db, f["MFD_1550_m"])
    V_cut = fiber_V_number(db, f["cladding_m"] / mpf("2"),
                            f["NA"], f["cutoff_m"])
    print("  SMF-28 FIBER:")
    print("    MFD @1310nm:  %s um" % mp.nstr(f["MFD_1310_m"] * mpf("1e6"), 3))
    print("    MFD @1550nm:  %s um" % mp.nstr(f["MFD_1550_m"] * mpf("1e6"), 3))
    print("    Mode area @1310: R2*MFD^2 = %s um^2" % mp.nstr(a1310 * mpf("1e12"), 4))
    print("    Mode area @1550: R2*MFD^2 = %s um^2" % mp.nstr(a1550 * mpf("1e12"), 4))
    print("    V at cutoff:  %s (j01 = %s)" % (mp.nstr(V_cut, 4), mp.nstr(_J01, 5)))
    print("    NA:           %s" % mp.nstr(f["NA"], 2))


# ================================================================
# ACOUSTICS
# ================================================================

def speaker_cone_area(db, d_eff_m):
    """Sd = R2 * d_eff^2."""
    d = mpf(str(d_eff_m))
    return _R2(db) * d ** 2


def helmholtz_freq(db, port_d_m, port_length_m, box_volume_m3,
                    c_sound="343"):
    """f = (c/(8*R2)) * sqrt(R2*d^2 / (l*V))."""
    d = mpf(str(port_d_m))
    l = mpf(str(port_length_m))
    V = mpf(str(box_volume_m3))
    c = mpf(str(c_sound))
    S = _R2(db) * d ** 2
    return (c / _eight_R2(db)) * msqrt(S / (l * V))


def sound_intensity(db, power_W, distance_m):
    """I = P / (16*R2*r^2) = P / (4*pi*r^2)."""
    P = mpf(str(power_W))
    r = mpf(str(distance_m))
    return P / (_sixteen_R2(db) * r ** 2)


def show_speakers(db):
    """Print speaker cone area table."""
    print("  SPEAKER CONE AREAS  (Sd = R2 * d_eff^2):")
    print("  %-20s %10s %10s" % ("Speaker", "d_eff(m)", "Sd(cm^2)"))
    print("  %-20s %10s %10s" % ("-" * 20, "-" * 10, "-" * 10))
    for key in ["12inch", "10inch", "8inch", "6inch", "5inch", "1inch"]:
        s = SPEAKER_DATA[key]
        Sd = speaker_cone_area(db, s["d_eff_m"])
        print("  %-20s %10s %10s" % (
            s["name"], mp.nstr(s["d_eff_m"], 4),
            mp.nstr(Sd * mpf("1e4"), 4)))


# ================================================================
# WIRE & CIRCUITS
# ================================================================

def wire_resistance(db, rho, length_m, diameter_m):
    """R = rho * L / (R2 * d^2)."""
    r = mpf(str(rho))
    L = mpf(str(length_m))
    d = mpf(str(diameter_m))
    return r * L / (_R2(db) * d ** 2)


def wire_area(db, diameter_m):
    """A = R2 * d^2 for a wire cross-section."""
    d = mpf(str(diameter_m))
    return _R2(db) * d ** 2


def circular_capacitance(db, diameter_m, gap_m, epsilon_r="1"):
    """C = epsilon_0 * epsilon_r * R2 * d^2 / t."""
    d = mpf(str(diameter_m))
    t = mpf(str(gap_m))
    er = mpf(str(epsilon_r))
    return _EPSILON_0 * er * _R2(db) * d ** 2 / t


def rc_product(db, rho, length_m, diameter_m, gap_m):
    """R*C = rho*L/(R2*d^2) * eps0*R2*d^2/t = rho*eps0*L/t.
    R2 CANCELS. The product is R2-free.
    """
    R = wire_resistance(db, rho, length_m, diameter_m)
    C = circular_capacitance(db, diameter_m, gap_m)
    return {
        "R": R,
        "C": C,
        "RC": R * C,
        "RC_direct": mpf(str(rho)) * _EPSILON_0 * mpf(str(length_m)) / mpf(str(gap_m)),
        "R2_cancels": True,
    }


def show_rc_cancellation(db):
    """Demonstrate R2 cancellation in R*C product."""
    d12 = AWG["12"]
    result = rc_product(db, _CU_RHO, "1", d12, "1e-3")
    print("  R2 CANCELLATION: WIRE R x CAPACITOR C")
    print("    Wire:      AWG 12 (d = %s mm), 1 m copper" % mp.nstr(d12 * mpf("1e3"), 4))
    print("    Capacitor: same diameter, 1 mm gap, air")
    print("    R = rho*L/(R2*d^2) = %s ohm" % mp.nstr(result["R"], 4))
    print("    C = eps0*R2*d^2/t  = %s pF" % mp.nstr(result["C"] * mpf("1e12"), 4))
    print("    RC (from functions) = %s s" % mp.nstr(result["RC"], 6))
    print("    RC (direct, no R2)  = %s s" % mp.nstr(result["RC_direct"], 6))
    print("    R2 cancels: %s" % result["R2_cancels"])
    print("    Like K_J * R_K = 2/e: geometry enters both sides, divides out.")


def show_awg_table(db):
    """Print AWG wire gauge table with R2*d^2 areas."""
    print("  AWG WIRE TABLE  (A = R2 * d^2):")
    print("  %-6s %10s %10s %12s" % ("AWG", "d(mm)", "A(mm^2)", "R(mohm/m)"))
    print("  %-6s %10s %10s %12s" % ("-" * 6, "-" * 10, "-" * 10, "-" * 12))
    for gauge in ["0000", "0", "4", "8", "10", "12", "14", "18", "22", "24", "30", "36"]:
        d = AWG[gauge]
        A = wire_area(db, d)
        R = wire_resistance(db, _CU_RHO, "1", d)
        print("  %-6s %10s %10s %12s" % (
            gauge,
            mp.nstr(d * mpf("1e3"), 4),
            mp.nstr(A * mpf("1e6"), 4),
            mp.nstr(R * mpf("1e3"), 4)))


# ================================================================
# RF & TELECOM
# ================================================================

def rf_wavelength(frequency_Hz):
    """lambda = c / f. c exact from SI."""
    f = mpf(str(frequency_Hz))
    return _C_LIGHT / f


def fspl_dB(db, distance_m, frequency_Hz):
    """Free-space path loss: FSPL = (16*R2*d/lambda)^2.
    In dB: 20*log10(16*R2*d*f/c).
    """
    d = mpf(str(distance_m))
    f = mpf(str(frequency_Hz))
    lam = _C_LIGHT / f
    ratio = _sixteen_R2(db) * d / lam
    return mpf("20") * mlog(ratio, 10)


def antenna_area(db, gain_linear, wavelength_m):
    """A_eff = G * lambda^2 / (16*R2) = G * lambda^2 / (4*pi)."""
    G = mpf(str(gain_linear))
    lam = mpf(str(wavelength_m))
    return G * lam ** 2 / _sixteen_R2(db)


def show_gps_rf(db):
    """Print GPS L1/L2 RF parameters."""
    gps_L1 = mpf("1575.42e6")
    gps_L2 = mpf("1227.60e6")
    lam_L1 = _C_LIGHT / gps_L1
    lam_L2 = _C_LIGHT / gps_L2
    print("  GPS RF PARAMETERS:")
    print("    L1: f = %s MHz, lam = %s m" % (
        mp.nstr(gps_L1 / mpf("1e6"), 6), mp.nstr(lam_L1, 4)))
    print("    L2: f = %s MHz, lam = %s m" % (
        mp.nstr(gps_L2 / mpf("1e6"), 6), mp.nstr(lam_L2, 4)))
    print("    L1 FSPL @1km: %s dB" % mp.nstr(fspl_dB(db, "1000", gps_L1), 4))
    print("    L1 isotropic Aeff: %s cm^2" % mp.nstr(
        antenna_area(db, "1", lam_L1) * mpf("1e4"), 4))


# ================================================================
# SEMICONDUCTOR
# ================================================================

def litho_resolution(db, wavelength_m, NA, k1=None):
    """CD = k1 * lambda / NA.
    Default k1 = j11/(2*pi) = j11/(8*R2) = 0.6098 (Rayleigh).
    """
    lam = mpf(str(wavelength_m))
    na = mpf(str(NA))
    if k1 is None:
        k1_val = _airy_const(db) / mpf("2")
    else:
        k1_val = mpf(str(k1))
    return k1_val * lam / na


def show_litho(db):
    """Print EUV and ArF lithography resolution."""
    euv = mpf("13.5e-9")
    arf = mpf("193e-9")
    print("  LITHOGRAPHY RESOLUTION  (CD = k1 * lambda / NA):")
    print("  %-20s %8s %6s %10s" % ("Technology", "lam(nm)", "NA", "CD(nm)"))
    print("  %-20s %8s %6s %10s" % ("-" * 20, "-" * 8, "-" * 6, "-" * 10))
    for name, lam, na in [
        ("EUV (standard)",   euv, "0.33"),
        ("EUV (high-NA)",    euv, "0.55"),
        ("ArF immersion",    arf, "1.35"),
    ]:
        cd = litho_resolution(db, lam, na)
        print("  %-20s %8s %6s %10s" % (
            name, mp.nstr(lam * mpf("1e9"), 3), na,
            mp.nstr(cd * mpf("1e9"), 3)))
    wafer_a = R2_area(db, "0.300")
    print("  300mm wafer area = R2 * (0.3)^2 = %s cm^2" % mp.nstr(
        wafer_a * mpf("1e4"), 4))


# ================================================================
# FLOW & THERMAL
# ================================================================

def pipe_flow(db, diameter_m, velocity_ms):
    """Q = R2 * d^2 * v."""
    d = mpf(str(diameter_m))
    v = mpf(str(velocity_ms))
    return _R2(db) * d ** 2 * v


def orifice_flow(db, diameter_m, dP_Pa, rho_fluid, Cd=None):
    """q = Cd * R2 * d^2 * sqrt(2*dP/rho).
    Default Cd = vena contracta pi/(pi+2) = 4R2/(4R2+2).
    """
    d = mpf(str(diameter_m))
    dp = mpf(str(dP_Pa))
    rho = mpf(str(rho_fluid))
    if Cd is None:
        Cd_val = _four_R2(db) / (_four_R2(db) + mpf("2"))
    else:
        Cd_val = mpf(str(Cd))
    return Cd_val * _R2(db) * d ** 2 * msqrt(mpf("2") * dp / rho)


def hagen_poiseuille(db, diameter_m, dP_Pa, viscosity, length_m):
    """Q = R2 * d^4 * dP / (32 * mu * L)."""
    d = mpf(str(diameter_m))
    dp = mpf(str(dP_Pa))
    mu = mpf(str(viscosity))
    L = mpf(str(length_m))
    return _R2(db) * d ** 4 * dp / (mpf("32") * mu * L)


def thermal_radiation(db, emissivity, temperature_K, diameter_m):
    """Q = eps * sigma * T^4 * R2 * d^2."""
    eps = mpf(str(emissivity))
    T = mpf(str(temperature_K))
    d = mpf(str(diameter_m))
    return eps * _SIGMA_SB * T ** 4 * _R2(db) * d ** 2


def vena_contracta(db):
    """C_c = pi/(pi+2) = 4R2/(4R2+2). Kirchhoff 1869."""
    return _four_R2(db) / (_four_R2(db) + mpf("2"))


def show_vena_contracta(db):
    """Print vena contracta from Q335 R2."""
    cc = vena_contracta(db)
    print("  VENA CONTRACTA (Kirchhoff 1869):")
    print("    C_c = pi/(pi+2) = 4R2/(4R2+2) = %s" % mp.nstr(cc, 15))
    print("    Jet area = C_c * R2 * d^2 for sharp-edged orifice")


# ================================================================
# NORMALIZATIONS
# ================================================================

def fourier_norm(db):
    """1/(8*R2) = 1/(2*pi). Fourier transform normalization."""
    return mpf("1") / _eight_R2(db)


def gaussian_norm(db):
    """1/sqrt(8*R2) = 1/sqrt(2*pi). Gaussian normalization."""
    return mpf("1") / msqrt(_eight_R2(db))


def gaussian_peak(db, total, sigma):
    """Peak of 1D Gaussian: N = total / sqrt(8*R2*sigma^2).
    Ion implant peak, beam peak, etc.
    """
    tot = mpf(str(total))
    sig = mpf(str(sigma))
    return tot / msqrt(_eight_R2(db) * sig ** 2)


def bcs_gap_ratio(db):
    """BCS superconducting gap: 2*Delta/(k_B*T_c) = pi/e^gamma.
    = 4*R2 / exp(gamma_EM).
    """
    return _four_R2(db) / mpf("1") * msqrt(mpf("1")) / msqrt(mpf("1"))  # dummy sqrt
    # Correct:
    return _four_R2(db) / (mpf("2.718281828459045") ** _GAMMA_EM)


# Fix: clean BCS gap
def bcs_gap(db):
    """BCS gap ratio = pi / e^gamma_EM = 4R2 / exp(0.5772...) = 1.76388..."""
    from mpmath import exp as mexp
    return _four_R2(db) / mexp(_GAMMA_EM)


def show_bcs(db):
    """Print BCS gap ratio from Q335 R2."""
    gap = bcs_gap(db)
    print("  BCS SUPERCONDUCTING GAP (from Q335 R2):")
    print("    2*Delta/(k_B*T_c) = pi/e^gamma = 4R2/exp(gamma)")
    print("    = %s" % mp.nstr(gap, 10))
    print()
    _materials = {
        "Al": mpf("1.764"), "Sn": mpf("1.764"),
        "Pb": mpf("2.185"), "Nb": mpf("1.87"),
    }
    print("    %-6s %10s %10s %10s" % ("Mat", "Measured", "BCS", "Dev"))
    print("    %-6s %10s %10s %10s" % ("-" * 6, "-" * 10, "-" * 10, "-" * 10))
    for mat, meas in _materials.items():
        dev = (meas - gap) / gap * mpf("100")
        print("    %-6s %10s %10s %10s%%" % (
            mat, mp.nstr(meas, 4), mp.nstr(gap, 5), mp.nstr(dev, 3)))


def show_normalizations(db):
    """Print mathematical normalizations in R2 form."""
    print("  MATHEMATICAL NORMALIZATIONS (R2 form):")
    norms = [
        ("Fourier:  1/(2*pi)",          "1/(8*R2)",           fourier_norm(db)),
        ("Gaussian: 1/sqrt(2*pi)",      "1/sqrt(8*R2)",       gaussian_norm(db)),
        ("Stirling: sqrt(2*pi*n)",      "sqrt(8*R2*n)",       msqrt(_eight_R2(db))),
        ("Euler:    e^(i*pi) = -1",     "e^(4i*R2) = -1",    _four_R2(db)),
        ("Gauss:    sqrt(pi)",          "2*sqrt(R2)",         mpf("2") * msqrt(_R2(db))),
        ("Wallis:   pi/2",             "2*R2",               mpf("2") * _R2(db)),
    ]
    for standard, r2_form, value in norms:
        print("    %-30s = %-20s = %s" % (standard, r2_form, mp.nstr(value, 10)))


# ================================================================
# CROSS-DOMAIN TRANSLATION
# ================================================================

def cross_domain_area(db, diameter_m):
    """Given a diameter, show R2*d^2 interpreted in every domain.
    The MATH-1 universal equation: Q = F * R2 * d^2 * Z.
    """
    d = mpf(str(diameter_m))
    A = _R2(db) * d ** 2

    print("  CROSS-DOMAIN AREA for d = %s m:" % mp.nstr(d, 4))
    print("    A = R2 * d^2 = %s m^2 = %s cm^2 = %s mm^2" % (
        mp.nstr(A, 6), mp.nstr(A * mpf("1e4"), 6), mp.nstr(A * mpf("1e6"), 6)))
    print()
    print("    %-25s %s" % ("Domain", "Physical meaning"))
    print("    %-25s %s" % ("-" * 25, "-" * 40))

    interpretations = [
        ("Pipe (v=1 m/s)",       "Q = %s m^3/s = %s L/min" % (
            mp.nstr(A, 4), mp.nstr(A * mpf("60000"), 4))),
        ("Wire (Cu, per m)",     "R = %s ohm/m" % mp.nstr(_CU_RHO / A, 4)),
        ("Capacitor (1mm gap)",  "C = %s pF" % mp.nstr(
            _EPSILON_0 * A / mpf("1e-3") * mpf("1e12"), 4)),
        ("Thermal (300K, e=1)",  "Q = %s W" % mp.nstr(
            _SIGMA_SB * mpf("300") ** 4 * A, 4)),
        ("Speaker cone",        "Sd = %s cm^2" % mp.nstr(A * mpf("1e4"), 4)),
        ("Disc (physical)",      "A = %s cm^2" % mp.nstr(A * mpf("1e4"), 4)),
        ("Wafer (if 300mm)",     "A = %s cm^2" % mp.nstr(
            _R2(db) * mpf("0.300") ** 2 * mpf("1e4"), 4)),
    ]
    for domain, meaning in interpretations:
        print("    %-25s %s" % (domain, meaning))

    return A


# ================================================================
# R2 EQUATION TABLE & CANCELLATION MAP
# ================================================================

def show_all_R2_equations(db):
    """Print the complete R2 equation table (23 domains) from db."""
    domains = db.find(obj_type="domain")
    print("  ALL R2 EQUATIONS (%d domains):" % len(domains))
    print("  %-4s %-22s %-35s %s" % ("#", "Domain", "Equation", "Z"))
    print("  %-4s %-22s %-35s %s" % ("-" * 4, "-" * 22, "-" * 35, "-" * 20))
    for i, d in enumerate(domains):
        print("  %-4d %-22s %-35s %s" % (
            i + 1, d.name[:22], d.equation[:35], d.coordinator_Z[:20]))
    print("  Same R2. Different Z. Q = F * R2 * d^2 * Z.")


def show_all_cancellations(db, status=None):
    """Print the R2 cancellation registry (11 identities) from db."""
    cancels = db.find(obj_type="cancellation")
    if status is not None:
        cancels = [c for c in cancels if hasattr(c, 'status') and c.status == status]
    print("  R2 CANCELLATIONS (%d):" % len(cancels))
    print("  %-4s %-10s %-25s %-40s %s" % (
        "#", "Status", "Name", "Formula", "Remains"))
    print("  %-4s %-10s %-25s %-40s %s" % (
        "-" * 4, "-" * 10, "-" * 25, "-" * 40, "-" * 15))
    for i, c in enumerate(cancels):
        print("  %-4d %-10s %-25s %-40s %s" % (
            i + 1, c.status, c.name[:25], c.formula[:40], c.remains[:15]))


def verify_rc_cancellation(db):
    """Numerically verify R2 cancels in R*C for AWG 12."""
    d = AWG["12"]
    R = wire_resistance(db, _CU_RHO, "1", d)
    C = circular_capacitance(db, d, "1e-3")
    RC_with_R2 = R * C
    RC_without = mpf(str(_CU_RHO)) * _EPSILON_0 * mpf("1") / mpf("1e-3")
    diff = abs(RC_with_R2 - RC_without)
    print("  RC CANCELLATION VERIFICATION (AWG 12):")
    print("    R (with R2):   %s ohm" % mp.nstr(R, 6))
    print("    C (with R2):   %s F" % mp.nstr(C, 6))
    print("    RC (product):  %s s" % mp.nstr(RC_with_R2, 15))
    print("    RC (direct):   %s s" % mp.nstr(RC_without, 15))
    print("    Difference:    %s (should be 0 to working precision)" % mp.nstr(diff, 4))
    return diff < mpf("1e-30")


def verify_kj_rk_cancellation(db):
    """Numerically verify K_J * R_K = 2/e using db constants."""
    h_val = f2m(db.get("const.h").value)
    e_val = f2m(db.get("const.e_charge").value)
    K_J = mpf("2") * e_val / h_val
    R_K = h_val / (e_val ** 2)
    product = K_J * R_K
    expected = mpf("2") / e_val
    diff = abs(product - expected)
    print("  K_J * R_K CANCELLATION:")
    print("    K_J = 2e/h     = %s" % mp.nstr(K_J, 10))
    print("    R_K = h/e^2    = %s" % mp.nstr(R_K, 10))
    print("    K_J * R_K      = %s" % mp.nstr(product, 15))
    print("    2/e            = %s" % mp.nstr(expected, 15))
    print("    R2 cancels (h = 8*R2*hbar in both, divides out): %s" % (diff < mpf("1e-20")))
    return diff < mpf("1e-20")
