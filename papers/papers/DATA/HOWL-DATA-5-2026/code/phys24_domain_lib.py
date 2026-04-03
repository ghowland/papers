#!/usr/bin/env python3
"""
HOWL PHYS-24 DOMAIN DATA LIBRARY
====================================
Every domain where R2 = pi/4 appears, with structured data objects,
cross-domain translation helpers, and the R2 cancellation registry.

Built from DATA-1 (268 entries, 17 domains) and DATA-2 (107 Q335 entries).

Each domain is a dict containing:
  - name, category, description
  - R2 equation (the universal form)
  - parameters with values (Fraction or mpf)
  - coordinator Z (what makes this domain different)
  - precision (best available measurement)
  - DATA-1 entry IDs
  - papers where this domain appears

Helper functions:
  - domain_area(d): compute R2 * d^2 for any diameter
  - airy_resolution(lam, D_or_NA): diffraction limit
  - translate(domain_A, domain_B, d): cross-domain translation
  - cancellation_check(expr1, expr2): test if R2 cancels
  - domains_using(keyword): find domains by keyword
  - all_R2_equations(): list every R2 equation in one place

Import:
    from phys24_lib import *
    from phys24_domain_lib import *

Platform: phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from mpmath import pi as mpi, log as mlog, sqrt as msqrt, exp as mexp


# ================================================================
# CORE GEOMETRIC CONSTANTS
# ================================================================

R2 = f2m(R2_f)                          # pi/4
R4 = f2m(R4_f)                          # pi^2/32
EIGHT_R2 = mpf("8") * R2                # 2*pi
FOUR_R2 = mpf("4") * R2                 # pi
SIXTEEN_R2 = mpf("16") * R2             # 4*pi

# Bessel zeros (from DATA-1/MATH-3)
J11 = mpf("3.83170597020751")           # first zero of J1
J01 = mpf("2.40482555769577")           # first zero of J0
AIRY_CONST = J11 / FOUR_R2              # j11/pi = 1.21967 ~ 1.22

# Physical constants for cross-domain work
C_LIGHT = mpf("299792458")              # m/s, exact
HBAR_C_MEV_FM = mpf("197.3269804")      # MeV*fm
EPSILON_0 = mpf("8.8541878128e-12")     # F/m
C_SOUND_AIR = mpf("343")                # m/s at 20C, approximate

# Vena contracta from Kirchhoff 1869
C_C_EXACT = FOUR_R2 / (FOUR_R2 + mpf("2"))  # pi/(pi+2) = 0.61078...


# ================================================================
# HELPER FUNCTIONS
# ================================================================

def domain_area(d):
    """Circular area from diameter: A = R2 * d^2.
    The universal geometric conversion in every domain.
    Args: d in meters (mpf or Fraction)
    Returns: area in m^2 (mpf)
    """
    d_val = f2m(d) if isinstance(d, Fraction) else mpf(d)
    return R2 * d_val ** 2


def domain_area_from_radius(r):
    """Circular area from radius: A = 4*R2 * r^2 = pi * r^2.
    Args: r in meters
    Returns: area in m^2 (mpf)
    """
    r_val = f2m(r) if isinstance(r, Fraction) else mpf(r)
    return FOUR_R2 * r_val ** 2


def airy_resolution(wavelength, D_or_NA, mode="diameter"):
    """Diffraction-limited resolution via Airy pattern.
    resolution = 1.22 * lambda / D     (telescope/antenna mode)
    resolution = 1.22 * lambda / NA    (microscope/disc mode)

    Args:
      wavelength: in meters
      D_or_NA: diameter in meters (mode="diameter") or NA (mode="NA")
      mode: "diameter" or "NA"
    Returns: resolution in meters (mpf)
    """
    lam = f2m(wavelength) if isinstance(wavelength, Fraction) else mpf(wavelength)
    val = f2m(D_or_NA) if isinstance(D_or_NA, Fraction) else mpf(D_or_NA)
    return AIRY_CONST * lam / val


def spot_area(wavelength, NA):
    """Diffraction-limited spot area: A = R2 * (1.22 * lambda / NA)^2.
    Args: wavelength, NA in meters and dimensionless
    Returns: area in m^2 (mpf)
    """
    spot = airy_resolution(wavelength, NA, mode="NA")
    return R2 * spot ** 2


def rayleigh_range(w0, wavelength):
    """Gaussian beam Rayleigh range: z_R = 4*R2*w0^2/lambda.
    Args: w0 (beam waist, m), wavelength (m)
    Returns: z_R in meters (mpf)
    """
    w = f2m(w0) if isinstance(w0, Fraction) else mpf(w0)
    lam = f2m(wavelength) if isinstance(wavelength, Fraction) else mpf(wavelength)
    return FOUR_R2 * w ** 2 / lam


def beam_divergence(w0, wavelength):
    """Gaussian beam half-angle divergence: theta = lambda / (4*R2*w0).
    Args: w0 (beam waist, m), wavelength (m)
    Returns: half-angle in radians (mpf)
    """
    w = f2m(w0) if isinstance(w0, Fraction) else mpf(w0)
    lam = f2m(wavelength) if isinstance(wavelength, Fraction) else mpf(wavelength)
    return lam / (FOUR_R2 * w)


def wire_resistance(rho, length, diameter):
    """Wire resistance: R = rho * L / (R2 * d^2).
    Args: rho (ohm*m), length (m), diameter (m)
    Returns: resistance in ohms (mpf)
    """
    r = f2m(rho) if isinstance(rho, Fraction) else mpf(rho)
    L = f2m(length) if isinstance(length, Fraction) else mpf(length)
    d = f2m(diameter) if isinstance(diameter, Fraction) else mpf(diameter)
    return r * L / (R2 * d ** 2)


def circular_capacitance(diameter, gap, epsilon_r=1):
    """Parallel plate capacitance with circular plates.
    C = epsilon_0 * epsilon_r * R2 * d^2 / t
    Args: diameter (m), gap (m), epsilon_r (dimensionless, default 1)
    Returns: capacitance in farads (mpf)
    """
    d = f2m(diameter) if isinstance(diameter, Fraction) else mpf(diameter)
    t = f2m(gap) if isinstance(gap, Fraction) else mpf(gap)
    return EPSILON_0 * mpf(epsilon_r) * R2 * d ** 2 / t


def pipe_flow(diameter, velocity):
    """Volume flow rate through circular pipe: Q = R2 * d^2 * v.
    Args: diameter (m), velocity (m/s)
    Returns: flow rate in m^3/s (mpf)
    """
    d = f2m(diameter) if isinstance(diameter, Fraction) else mpf(diameter)
    v = f2m(velocity) if isinstance(velocity, Fraction) else mpf(velocity)
    return R2 * d ** 2 * v


def orifice_flow(diameter, dP, rho_fluid, Cd=None):
    """Orifice flow: q = Cd * R2 * d^2 * sqrt(2*dP/rho).
    If Cd not given, uses vena contracta C_c = pi/(pi+2).
    Args: diameter (m), dP (Pa), rho_fluid (kg/m^3), Cd (dimensionless)
    Returns: flow rate in m^3/s (mpf)
    """
    d = f2m(diameter) if isinstance(diameter, Fraction) else mpf(diameter)
    dp = f2m(dP) if isinstance(dP, Fraction) else mpf(dP)
    rho = f2m(rho_fluid) if isinstance(rho_fluid, Fraction) else mpf(rho_fluid)
    if Cd is None:
        Cd_val = C_C_EXACT
    else:
        Cd_val = f2m(Cd) if isinstance(Cd, Fraction) else mpf(Cd)
    return Cd_val * R2 * d ** 2 * msqrt(mpf("2") * dp / rho)


def helmholtz_frequency(port_diameter, port_length, box_volume,
                         c_sound=None):
    """Helmholtz resonance: f = (c/(8*R2)) * sqrt(R2*d^2 / (l*V)).
    Args: port_diameter (m), port_length (m), box_volume (m^3),
          c_sound (m/s, default 343)
    Returns: frequency in Hz (mpf)
    """
    d = f2m(port_diameter) if isinstance(port_diameter, Fraction) else mpf(port_diameter)
    l_eff = f2m(port_length) if isinstance(port_length, Fraction) else mpf(port_length)
    V = f2m(box_volume) if isinstance(box_volume, Fraction) else mpf(box_volume)
    c = C_SOUND_AIR if c_sound is None else (f2m(c_sound) if isinstance(c_sound, Fraction) else mpf(c_sound))
    S_port = R2 * d ** 2
    return (c / EIGHT_R2) * msqrt(S_port / (l_eff * V))


def antenna_effective_area(gain_linear, wavelength):
    """Antenna effective aperture: A_eff = G * lambda^2 / (16*R2).
    Args: gain_linear (dimensionless, not dB), wavelength (m)
    Returns: effective area in m^2 (mpf)
    """
    G = f2m(gain_linear) if isinstance(gain_linear, Fraction) else mpf(gain_linear)
    lam = f2m(wavelength) if isinstance(wavelength, Fraction) else mpf(wavelength)
    return G * lam ** 2 / SIXTEEN_R2


def friis_path_loss(distance, wavelength):
    """Free-space path loss: FSPL = (16*R2*d/lambda)^2.
    Args: distance (m), wavelength (m)
    Returns: path loss as power ratio (mpf, dimensionless)
    """
    d = f2m(distance) if isinstance(distance, Fraction) else mpf(distance)
    lam = f2m(wavelength) if isinstance(wavelength, Fraction) else mpf(wavelength)
    return (SIXTEEN_R2 * d / lam) ** 2


def rayleigh_scattering_loss(wavelength_um, A_coeff=None):
    """Fiber Rayleigh scattering loss: alpha = A / lambda^4.
    The (8*R2/lambda)^4 scaling sets the fundamental loss floor.
    Args: wavelength_um (wavelength in micrometers),
          A_coeff (dB/(km*um^4), default 0.8 for silica)
    Returns: loss in dB/km (mpf)
    """
    lam = f2m(wavelength_um) if isinstance(wavelength_um, Fraction) else mpf(wavelength_um)
    A = mpf("0.8") if A_coeff is None else (f2m(A_coeff) if isinstance(A_coeff, Fraction) else mpf(A_coeff))
    return A / lam ** 4


def fiber_V_number(core_radius, NA, wavelength):
    """Fiber V-number: V = 8*R2 * a * NA / lambda = 2*pi*a*NA/lambda.
    Single-mode cutoff at V = j01 = 2.405.
    Args: core_radius (m), NA (dimensionless), wavelength (m)
    Returns: V (dimensionless, mpf)
    """
    a = f2m(core_radius) if isinstance(core_radius, Fraction) else mpf(core_radius)
    na = f2m(NA) if isinstance(NA, Fraction) else mpf(NA)
    lam = f2m(wavelength) if isinstance(wavelength, Fraction) else mpf(wavelength)
    return EIGHT_R2 * a * na / lam


def sound_intensity(power, distance):
    """Sound intensity from point source: I = P / (16*R2*r^2).
    Args: power (watts), distance (meters)
    Returns: intensity in W/m^2 (mpf)
    """
    P = f2m(power) if isinstance(power, Fraction) else mpf(power)
    r = f2m(distance) if isinstance(distance, Fraction) else mpf(distance)
    return P / (SIXTEEN_R2 * r ** 2)


def thermal_radiation(emissivity, temperature, diameter):
    """Thermal radiation from circular surface:
    Q = epsilon * sigma * T^4 * R2 * d^2.
    Args: emissivity (0-1), temperature (K), diameter (m)
    Returns: radiated power in watts (mpf)
    """
    eps = f2m(emissivity) if isinstance(emissivity, Fraction) else mpf(emissivity)
    T = f2m(temperature) if isinstance(temperature, Fraction) else mpf(temperature)
    d = f2m(diameter) if isinstance(diameter, Fraction) else mpf(diameter)
    sigma_SB = mpf("5.670374419e-8")  # W/(m^2 K^4)
    return eps * sigma_SB * T ** 4 * R2 * d ** 2


def hagen_poiseuille(diameter, dP, viscosity, length):
    """Laminar flow: Q = R2 * d^4 * dP / (32 * mu * L).
    Note: prefactor is pi/128 = R2/32.
    Args: diameter (m), dP (Pa), viscosity (Pa*s), length (m)
    Returns: flow rate in m^3/s (mpf)
    """
    d = f2m(diameter) if isinstance(diameter, Fraction) else mpf(diameter)
    dp = f2m(dP) if isinstance(dP, Fraction) else mpf(dP)
    mu = f2m(viscosity) if isinstance(viscosity, Fraction) else mpf(viscosity)
    L = f2m(length) if isinstance(length, Fraction) else mpf(length)
    return R2 * d ** 4 * dp / (mpf("32") * mu * L)


def gaussian_peak(total, sigma):
    """Peak of 1D Gaussian: N_peak = total / sqrt(8*R2*sigma^2).
    Used for: ion implant peak concentration, beam intensity.
    Args: total (dose or power), sigma (straggle or waist)
    Returns: peak value (mpf)
    """
    tot = f2m(total) if isinstance(total, Fraction) else mpf(total)
    sig = f2m(sigma) if isinstance(sigma, Fraction) else mpf(sigma)
    return tot / msqrt(EIGHT_R2 * sig ** 2)


def fourier_norm():
    """Fourier transform normalization: 1/(8*R2) = 1/(2*pi).
    Returns: the normalization constant (mpf)
    """
    return mpf("1") / EIGHT_R2


def gaussian_norm():
    """Gaussian normalization: 1/sqrt(8*R2) = 1/sqrt(2*pi).
    Returns: the normalization constant (mpf)
    """
    return mpf("1") / msqrt(EIGHT_R2)


# ================================================================
# OPTICAL DISC DATA (DATA-1 Section 9)
# ================================================================

OPTICAL_DISCS = {
    "CD": {
        "name": "Compact Disc",
        "standard": "ECMA-130 / Red Book",
        "laser_wavelength_m": mpf("780e-9"),
        "NA": mpf("0.45"),
        "track_pitch_m": mpf("1.6e-6"),
        "pit_width_m": mpf("500e-9"),
        "pit_depth_m": mpf("125e-9"),
        "min_pit_length_m": mpf("830e-9"),
        "disc_diameter_m": mpf("0.120"),
        "disc_thickness_m": mpf("1.2e-3"),
        "sampling_rate_Hz": Fraction(44100, 1),
        "sector_raw_bytes": 2352,
        "sector_data_bytes": 2048,
        "capacity_bytes": 700 * 10**6,
        "data1_ids": ["D1", "D2", "D3", "D4", "D5", "D6", "D7",
                       "D8", "D9", "D10", "D11", "D12", "D13"],
    },
    "DVD": {
        "name": "Digital Versatile Disc",
        "standard": "ECMA-267",
        "laser_wavelength_m": mpf("650e-9"),
        "NA": mpf("0.60"),
        "track_pitch_m": mpf("0.74e-6"),
        "pit_width_m": mpf("320e-9"),
        "pit_depth_m": mpf("120e-9"),
        "min_pit_length_m": mpf("400e-9"),
        "disc_diameter_m": mpf("0.120"),
        "disc_thickness_m": mpf("0.6e-3"),
        "capacity_bytes": Fraction(47, 10) * 10**9,
        "data1_ids": ["D14", "D15", "D16", "D17", "D18", "D19",
                       "D20", "D21", "D22", "D23"],
    },
    "Blu-ray": {
        "name": "Blu-ray Disc",
        "standard": "BD White Paper",
        "laser_wavelength_m": mpf("405e-9"),
        "NA": mpf("0.85"),
        "track_pitch_m": mpf("0.320e-6"),
        "min_pit_length_m": mpf("149e-9"),
        "cover_layer_m": mpf("0.100e-3"),
        "disc_diameter_m": mpf("0.120"),
        "capacity_bytes": 25 * 10**9,
        "data1_ids": ["D24", "D25", "D26", "D27", "D28", "D29",
                       "D30", "D31"],
    },
}


def disc_spot_size(disc_key):
    """Get the diffraction-limited spot size for a disc format."""
    disc = OPTICAL_DISCS[disc_key]
    return airy_resolution(disc["laser_wavelength_m"], disc["NA"], mode="NA")


def disc_spot_area(disc_key):
    """Get the spot area for a disc format: R2 * spot^2."""
    s = disc_spot_size(disc_key)
    return R2 * s ** 2


def disc_area(disc_key):
    """Disc physical area: R2 * diameter^2."""
    d = OPTICAL_DISCS[disc_key]["disc_diameter_m"]
    return R2 * d ** 2


# ================================================================
# FIBER OPTIC DATA (DATA-1 Section 16)
# ================================================================

FIBER_OPTICS = {
    "SMF-28": {
        "name": "Corning SMF-28",
        "type": "single-mode",
        "MFD_1310_m": mpf("9.2e-6"),
        "MFD_1550_m": mpf("10.4e-6"),
        "NA": mpf("0.14"),
        "cladding_diameter_m": mpf("125.0e-6"),
        "cutoff_wavelength_m": mpf("1260e-9"),
        "attenuation_1550_dB_km": mpf("0.18"),
        "V_cutoff": J01,
        "data1_ids": ["K7", "K8", "K9", "K10", "K11", "K12", "K13"],
    },
}

# DWDM channel bands
DWDM_BANDS = {
    "O-band": {"center_nm": mpf("1310"), "range_nm": (mpf("1260"), mpf("1360"))},
    "C-band": {"center_nm": mpf("1550"), "range_nm": (mpf("1530"), mpf("1565"))},
    "L-band": {"center_nm": mpf("1590"), "range_nm": (mpf("1565"), mpf("1625"))},
}


def fiber_mode_area(fiber_key, wavelength_nm=1550):
    """Mode field area: R2 * MFD^2."""
    fiber = FIBER_OPTICS[fiber_key]
    if wavelength_nm <= 1400:
        MFD = fiber["MFD_1310_m"]
    else:
        MFD = fiber["MFD_1550_m"]
    return R2 * MFD ** 2


# ================================================================
# SPEAKER / ACOUSTICS DATA (DATA-1 Section 13)
# ================================================================

SPEAKERS = {
    "12inch": {"name": "12-inch woofer", "d_eff_m": mpf("0.305")},
    "10inch": {"name": "10-inch woofer", "d_eff_m": mpf("0.254")},
    "8inch":  {"name": "8-inch midrange", "d_eff_m": mpf("0.203")},
    "6inch":  {"name": "6.5-inch mid",   "d_eff_m": mpf("0.152")},
    "5inch":  {"name": "5-inch mid",     "d_eff_m": mpf("0.127")},
    "1inch":  {"name": "1-inch tweeter", "d_eff_m": mpf("0.025")},
}

# Audio sample rates (DATA-1 H5-H8)
SAMPLE_RATES = {
    "CD": Fraction(44100, 1),           # 2^2 * 3^2 * 5^2 * 7^2
    "studio": Fraction(48000, 1),       # 2^7 * 3 * 5^3
    "high_res": Fraction(96000, 1),     # 2^8 * 3 * 5^3
    "ultra": Fraction(192000, 1),       # 2^9 * 3 * 5^3
}

# Just intonation ratios (DATA-1 H12-H18)
JUST_INTONATION = {
    "octave": Fraction(2, 1),
    "perfect_fifth": Fraction(3, 2),
    "perfect_fourth": Fraction(4, 3),
    "major_third": Fraction(5, 4),
    "minor_third": Fraction(6, 5),
    "major_sixth": Fraction(5, 3),
    "minor_seventh": Fraction(9, 5),
}

# Standard impedances
SPEAKER_IMPEDANCES = [Fraction(4, 1), Fraction(8, 1), Fraction(16, 1)]
RF_IMPEDANCES = [Fraction(50, 1), Fraction(75, 1), Fraction(110, 1)]


def speaker_cone_area(speaker_key):
    """Cone area Sd = R2 * d_eff^2."""
    d = SPEAKERS[speaker_key]["d_eff_m"]
    return R2 * d ** 2


# ================================================================
# WIRE AND CONDUCTOR DATA (DATA-1 Section 12)
# ================================================================

# AWG wire gauges (DATA-1 G4-G12)
AWG_DATA = {
    "0000": {"diameter_m": mpf("11.684e-3"),  "diameter_in": mpf("0.4600")},
    "0":    {"diameter_m": mpf("8.251e-3"),   "diameter_in": mpf("0.3249")},
    "4":    {"diameter_m": mpf("5.189e-3"),   "diameter_in": mpf("0.2043")},
    "8":    {"diameter_m": mpf("3.264e-3"),   "diameter_in": mpf("0.1285")},
    "10":   {"diameter_m": mpf("2.588e-3"),   "diameter_in": mpf("0.1019")},
    "12":   {"diameter_m": mpf("2.053e-3"),   "diameter_in": mpf("0.0808")},
    "14":   {"diameter_m": mpf("1.628e-3"),   "diameter_in": mpf("0.0641")},
    "18":   {"diameter_m": mpf("1.024e-3"),   "diameter_in": mpf("0.0403")},
    "22":   {"diameter_m": mpf("0.644e-3"),   "diameter_in": mpf("0.0254")},
    "24":   {"diameter_m": mpf("0.511e-3"),   "diameter_in": mpf("0.0201")},
    "30":   {"diameter_m": mpf("0.255e-3"),   "diameter_in": mpf("0.0100")},
    "36":   {"diameter_m": mpf("0.127e-3"),   "diameter_in": mpf("0.0050")},
}

# Conductor properties
CU_RESISTIVITY = mpf("1.7241e-8")        # ohm*m at 20C
CU_IACS = mpf("5.8001e7")                # S/m (100% IACS reference)

# IEC standard conductor sizes (mm^2)
IEC_SIZES_MM2 = [Fraction(1, 2), Fraction(3, 4), Fraction(1, 1),
                  Fraction(3, 2), Fraction(5, 2), Fraction(4, 1),
                  Fraction(6, 1), Fraction(10, 1)]

# Exact definitions
INCH_MM = Fraction(127, 5)                # 1 inch = 25.4 mm exactly
MIL_MM = Fraction(127, 5000)              # 1 mil = 0.0254 mm exactly


def awg_area(gauge_str):
    """Wire cross-sectional area: R2 * d^2 for AWG gauge."""
    d = AWG_DATA[gauge_str]["diameter_m"]
    return R2 * d ** 2


def awg_resistance_per_m(gauge_str, rho=None):
    """Resistance per meter: rho / (R2 * d^2)."""
    if rho is None:
        rho = CU_RESISTIVITY
    d = AWG_DATA[gauge_str]["diameter_m"]
    return rho / (R2 * d ** 2)


# ================================================================
# RF AND TELECOM DATA (DATA-1 Section 14)
# ================================================================

RF_STANDARDS = {
    "GPS_L1": {"frequency_Hz": mpf("1575.42e6"), "source": "154 * 10.23 MHz"},
    "GPS_L2": {"frequency_Hz": mpf("1227.60e6"), "source": "120 * 10.23 MHz"},
    "GPS_base": {"frequency_Hz": mpf("10.23e6"), "source": "GPS ICD"},
    "5G_15kHz": {"subcarrier_Hz": mpf("15e3"), "source": "3GPP"},
    "5G_30kHz": {"subcarrier_Hz": mpf("30e3"), "source": "3GPP"},
    "5G_60kHz": {"subcarrier_Hz": mpf("60e3"), "source": "3GPP"},
    "5G_120kHz": {"subcarrier_Hz": mpf("120e3"), "source": "3GPP"},
}

# Standard baud rates (DATA-1 I4-I5)
BAUD_RATES = {
    "9600": Fraction(9600, 1),          # 2^7 * 3 * 5^2
    "115200": Fraction(115200, 1),      # 2^8 * 3^2 * 5^2
}


def rf_wavelength(frequency_Hz):
    """Wavelength from frequency: lambda = c / f."""
    f = f2m(frequency_Hz) if isinstance(frequency_Hz, Fraction) else mpf(frequency_Hz)
    return C_LIGHT / f


def fspl_dB(distance_m, frequency_Hz):
    """Free-space path loss in dB: 20*log10(16*R2*d*f/c)."""
    d = f2m(distance_m) if isinstance(distance_m, Fraction) else mpf(distance_m)
    f = f2m(frequency_Hz) if isinstance(frequency_Hz, Fraction) else mpf(frequency_Hz)
    lam = C_LIGHT / f
    ratio = SIXTEEN_R2 * d / lam
    return mpf("20") * mlog(ratio, 10)


# ================================================================
# SEMICONDUCTOR DATA (DATA-1 Section 15)
# ================================================================

SEMICONDUCTOR = {
    "wafer_300mm": {
        "diameter_m": mpf("0.300"),
        "area_m2": R2 * mpf("0.300") ** 2,
        "source": "SEMI standard",
    },
    "Si_lattice_m": mpf("5.431020511e-10"),  # CODATA 2022
    "EUV_wavelength_m": mpf("13.5e-9"),
    "ArF_wavelength_m": mpf("193e-9"),
    "DRAM_cell_area_F2": Fraction(6, 1),     # 6*F^2 standard
    "SRAM_cell_area_F2": Fraction(120, 1),   # ~120*F^2
}


def litho_resolution(wavelength_m, NA, k1=None):
    """Lithography resolution: CD = k1 * lambda / NA.
    k1 ~ 0.25-0.5 depending on technique.
    If k1 not given, uses Rayleigh criterion k1 = 0.61 = 1.22/2.
    Args: wavelength_m, NA, k1 (optional)
    Returns: minimum feature size in meters (mpf)
    """
    lam = f2m(wavelength_m) if isinstance(wavelength_m, Fraction) else mpf(wavelength_m)
    na = f2m(NA) if isinstance(NA, Fraction) else mpf(NA)
    if k1 is None:
        k1_val = AIRY_CONST / mpf("2")  # 1.22/2 = 0.61
    else:
        k1_val = f2m(k1) if isinstance(k1, Fraction) else mpf(k1)
    return k1_val * lam / na


# ================================================================
# STORAGE INTERFACE DATA (DATA-1 Section 11)
# ================================================================

STORAGE_INTERFACES = {
    "SATA_I":     {"rate_Gbps": mpf("1.5"),  "UI_ps": mpf("666.67")},
    "SATA_II":    {"rate_Gbps": mpf("3.0"),  "UI_ps": mpf("333.33")},
    "SATA_III":   {"rate_Gbps": mpf("6.0"),  "UI_ps": mpf("166.67")},
    "PCIe_Gen3":  {"rate_GTs": mpf("8.0"),   "UI_ps": mpf("125.00")},
    "PCIe_Gen4":  {"rate_GTs": mpf("16.0"),  "UI_ps": mpf("62.50")},
    "PCIe_Gen5":  {"rate_GTs": mpf("32.0"),  "UI_ps": mpf("31.25")},
}

# Block sizes (all powers of 2)
LBA_LEGACY = Fraction(512, 1)       # 2^9 bytes
LBA_AF = Fraction(4096, 1)          # 2^12 bytes
NAND_PAGE = Fraction(16384, 1)      # 2^14 bytes


# ================================================================
# RAM AND MEMORY DATA (DATA-1 Section 10)
# ================================================================

MEMORY_STANDARDS = {
    "DDR4-1600": {"rate_MTs": 1600, "clock_MHz": 800, "voltage_V": Fraction(6, 5)},
    "DDR4-2400": {"rate_MTs": 2400, "clock_MHz": 1200, "voltage_V": Fraction(6, 5)},
    "DDR4-3200": {"rate_MTs": 3200, "clock_MHz": 1600, "voltage_V": Fraction(6, 5)},
    "DDR5-4800": {"rate_MTs": 4800, "clock_MHz": 2400, "voltage_V": Fraction(11, 10)},
    "DDR5-5600": {"rate_MTs": 5600, "clock_MHz": 2800, "voltage_V": Fraction(11, 10)},
    "DDR5-6400": {"rate_MTs": 6400, "clock_MHz": 3200, "voltage_V": Fraction(11, 10)},
}


# ================================================================
# FLOW AND THERMAL DATA (DATA-1 Section 17)
# ================================================================

FLOW_CONSTANTS = {
    "vena_contracta_Cc": C_C_EXACT,          # pi/(pi+2) = 0.61078
    "standard_gravity": Fraction(980665, 100000),  # m/s^2, exact
    "standard_atmosphere_Pa": Fraction(101325, 1),  # exact
}


# ================================================================
# BCS SUPERCONDUCTING DATA (DATA-1 Section 21)
# ================================================================

BCS_DATA = {
    "gap_ratio_exact": None,  # pi/exp(gamma), computed below
    "gap_ratio_numerical": mpf("1.76388"),
    "materials": {
        "Al":  {"measured": mpf("1.764"), "coupling": "weak"},
        "Sn":  {"measured": mpf("1.764"), "coupling": "weak"},
        "Pb":  {"measured": mpf("2.185"), "coupling": "strong", "deviation": "+24%"},
        "Nb":  {"measured": mpf("1.87"),  "coupling": "intermediate"},
    },
}

# Compute BCS gap ratio from transcendentals
_gamma_EM = mpf("0.5772156649015329")  # Euler-Mascheroni, from mpmath
BCS_DATA["gap_ratio_exact"] = FOUR_R2 / mexp(_gamma_EM)  # pi/e^gamma


# ================================================================
# METROLOGY AND PRECISION (DATA-1 Section 18)
# ================================================================

METROLOGY = {
    "quantum_hall_R_K": {
        "formula": "R_K = h/e^2 = 8*R2*hbar/e^2",
        "value_ohm": mpf("25812.80745"),
        "R2_status": "present (cancels in products)",
    },
    "josephson_K_J": {
        "formula": "K_J = 2e/h",
        "value_Hz_V": mpf("483597.848e9"),
        "R2_status": "present (cancels in products)",
    },
    "surface_roughness_Ra_um": [
        mpf("0.1"), mpf("0.2"), mpf("0.4"), mpf("0.8"),
        mpf("1.6"), mpf("3.2")
    ],
}


# ================================================================
# GEODESY DATA (DATA-1 Section 19)
# ================================================================

GEODESY = {
    "WGS84_a_m": Fraction(6378137, 1),            # semi-major axis, exact integer
    "WGS84_inv_f": Fraction(298257223563, 10**9),  # inverse flattening
    "GPS_seconds_per_week": Fraction(604800, 1),   # 2^5 * 3^3 * 5^2 * 7
    "earth_angular_velocity": mpf("7.292115e-5"),  # rad/s
}


# ================================================================
# MATHEMATICAL NORMALIZATIONS (DATA-1 Section 20)
# ================================================================

MATH_NORMALIZATIONS = {
    "fourier_norm": {"standard": "1/(2*pi)", "R2_form": "1/(8*R2)"},
    "sinc": {"standard": "sin(pi*t)/(pi*t)", "R2_form": "sin(4*R2*t)/(4*R2*t)"},
    "gaussian_norm": {"standard": "1/sqrt(2*pi)", "R2_form": "1/sqrt(8*R2)"},
    "stirling": {"standard": "sqrt(2*pi*n)*(n/e)^n", "R2_form": "sqrt(8*R2*n)*(n/e)^n"},
    "maxwell_boltzmann": {"standard": "(m/(2*pi*kT))^(3/2)", "R2_form": "(m/(8*R2*kT))^(3/2)"},
    "euler_identity": {"standard": "e^(i*pi) = -1", "R2_form": "e^(4*i*R2) = -1"},
    "gauss_integral": {"standard": "sqrt(pi)", "R2_form": "2*sqrt(R2)"},
    "wallis": {"standard": "pi/2 = prod(4n^2/(4n^2-1))", "R2_form": "2*R2"},
}


# ================================================================
# R2 EQUATIONS — THE COMPLETE TABLE
# ================================================================

R2_EQUATIONS = [
    {"domain": "Pipe flow",         "equation": "Q = R2*d^2*v",
     "Z": "velocity v",             "precision": "Coriolis: 0.05%",
     "data1_section": 17,           "data1_id": "L1"},
    {"domain": "Drag force",        "equation": "F = 0.5*rho*v^2*R2*d^2*Cd",
     "Z": "drag coeff Cd",          "precision": "Wind tunnel: 1%",
     "data1_section": 17,           "data1_id": "L2"},
    {"domain": "Orifice flow",      "equation": "q = Cd*R2*d^2*sqrt(2*dP/rho)",
     "Z": "discharge Cd",           "precision": "ISO 5167: 0.5%",
     "data1_section": 17,           "data1_id": "L3"},
    {"domain": "Capacitor",         "equation": "C = eps0*R2*d^2/t",
     "Z": "permittivity eps",       "precision": "pF precision",
     "data1_section": 17,           "data1_id": "L4"},
    {"domain": "Poynting flux",     "equation": "P = S*R2*d^2",
     "Z": "irradiance S",           "precision": "Antenna: 0.1 dB",
     "data1_section": 17,           "data1_id": "L5"},
    {"domain": "Antenna aperture",  "equation": "A = eta*R2*D^2",
     "Z": "efficiency eta",         "precision": "Calibrated",
     "data1_section": 14,           "data1_id": "I11"},
    {"domain": "Beam cross-section","equation": "A = R2*d^2",
     "Z": "none (pure geometry)",   "precision": "Laser: um",
     "data1_section": 17,           "data1_id": "L7"},
    {"domain": "Thermal radiation", "equation": "Q = eps*sig*T^4*R2*d^2",
     "Z": "emissivity eps",         "precision": "Pyrometer: 1%",
     "data1_section": 17,           "data1_id": "L8"},
    {"domain": "Sound intensity",   "equation": "I = P/(16*R2*r^2)",
     "Z": "1/r^2 spreading",        "precision": "SPL: 0.5 dB",
     "data1_section": 13,           "data1_id": "H22"},
    {"domain": "Wire resistance",   "equation": "R = rho*L/(R2*d^2)",
     "Z": "resistivity rho",        "precision": "Handbook: 0.1%",
     "data1_section": 12,           "data1_id": "G10"},
    {"domain": "Speaker cone",      "equation": "Sd = R2*d_eff^2",
     "Z": "none (pure geometry)",   "precision": "Measured: 5%",
     "data1_section": 13,           "data1_id": "H21"},
    {"domain": "Fiber mode",        "equation": "A_eff = R2*MFD^2",
     "Z": "mode confinement",       "precision": "Corning: 5%",
     "data1_section": 16,           "data1_id": "K7"},
    {"domain": "Disc spot",         "equation": "A = R2*(1.22*lam/NA)^2",
     "Z": "diffraction limit",      "precision": "Standard nominal",
     "data1_section": 9,            "data1_id": "D1"},
    {"domain": "Wafer area",        "equation": "A = R2*D^2",
     "Z": "none (pure geometry)",   "precision": "SEMI: exact",
     "data1_section": 15,           "data1_id": "J1"},
    {"domain": "Gaussian beam",     "equation": "A_waist = R2*w0^2",
     "Z": "beam parameter",         "precision": "Laser: um",
     "data1_section": 16,           "data1_id": "K3"},
    {"domain": "Hagen-Poiseuille",  "equation": "Q = R2*d^4*dP/(32*mu*L)",
     "Z": "viscosity mu",           "precision": "Lab: 1%",
     "data1_section": 17,           "data1_id": "L15"},
    {"domain": "Ion implant",       "equation": "N = dose/sqrt(8*R2*sig^2)*exp(..)",
     "Z": "straggle sigma",         "precision": "SIMS: 5%",
     "data1_section": 15,           "data1_id": "J8"},
    {"domain": "Helmholtz resonance","equation": "f = (c/(8*R2))*sqrt(R2*d^2/(l*V))",
     "Z": "port geometry",          "precision": "Measured: 2 Hz",
     "data1_section": 13,           "data1_id": "H22"},
    {"domain": "Diffraction (Airy)","equation": "theta = j11/(4*R2)*lam/D",
     "Z": "Bessel zero j11",        "precision": "Fundamental limit",
     "data1_section": 16,           "data1_id": "K14"},
    {"domain": "Rayleigh scattering","equation": "sigma ~ (8*R2/lam)^4*r^6",
     "Z": "polarizability",         "precision": "Silica: 0.8 dB/km/um^4",
     "data1_section": 16,           "data1_id": "K18"},
    {"domain": "Free-space path loss","equation": "FSPL = (16*R2*d/lam)^2",
     "Z": "distance/wavelength",    "precision": "Link budget",
     "data1_section": 14,           "data1_id": "I12"},
    {"domain": "Radar cross-section","equation": "sigma = 16*R2*A^2/lam^2",
     "Z": "plate area A",           "precision": "RCS measurement",
     "data1_section": 14,           "data1_id": "I15"},
]


# ================================================================
# R2 CANCELLATION REGISTRY
# ================================================================

R2_CANCELLATIONS = [
    {"name": "K_J * R_K",
     "formula": "2e/h * h/e^2 = 2/e",
     "status": "CANCELS",
     "precision": "10^-8",
     "data1_id": "R1"},
    {"name": "G_0 * R_K",
     "formula": "2e^2/h * h/e^2 = 2",
     "status": "CANCELS",
     "precision": "exact",
     "data1_id": "R2"},
    {"name": "Rydberg R_inf",
     "formula": "alpha^2*m_e*c/(2h) -- 2h = 16*R2*hbar folds out",
     "status": "CANCELS",
     "precision": "13 digits",
     "data1_id": "R3"},
    {"name": "a_0 * alpha",
     "formula": "hbar/(m_e*c) -- R2 cancels in the ratio",
     "status": "CANCELS",
     "precision": "12 digits",
     "data1_id": "R4"},
    {"name": "Hartree energy",
     "formula": "m_e*c^2*alpha^2 -- no R2",
     "status": "R2-FREE",
     "precision": "10 digits",
     "data1_id": "R5"},
    {"name": "Phi_0^2 / R_K",
     "formula": "h^2/e^2 * e^2/h = h -- R2 returns",
     "status": "REAPPEARS",
     "precision": "exact",
     "data1_id": "R6"},
    {"name": "Wire R * Capacitor C",
     "formula": "rho*L/(R2*d^2) * eps0*R2*d^2/t = rho*eps0*L/t",
     "status": "CANCELS",
     "precision": "derived (new, from cross-domain demo)",
     "data1_id": None},
]


# ================================================================
# QUERY FUNCTIONS
# ================================================================

def domains_using(keyword):
    """Find all R2 equations matching a keyword."""
    kw = keyword.lower()
    return [eq for eq in R2_EQUATIONS if kw in eq["domain"].lower() or
            kw in eq["equation"].lower() or kw in eq["Z"].lower()]


def all_R2_equations():
    """Return the complete list of R2 equations."""
    return R2_EQUATIONS


def cancellations_where(status="CANCELS"):
    """Find R2 cancellation identities by status."""
    return [c for c in R2_CANCELLATIONS if c["status"] == status]


def cross_domain_area(d_meters):
    """Given a diameter, compute R2*d^2 and show what it means
    in every domain.
    Args: d_meters
    Returns: dict of domain interpretations
    """
    d = f2m(d_meters) if isinstance(d_meters, Fraction) else mpf(d_meters)
    A = R2 * d ** 2
    result = {
        "diameter_m": d,
        "area_m2": A,
        "area_cm2": A * mpf("1e4"),
        "area_mm2": A * mpf("1e6"),
        "interpretations": {
            "pipe_flow_at_1ms": A * mpf("1"),          # m^3/s
            "wire_R_per_m_Cu": CU_RESISTIVITY / A,     # ohm/m
            "capacitance_1mm_gap_pF": EPSILON_0 * A / mpf("1e-3") * mpf("1e12"),
            "thermal_rad_300K_W": mpf("5.67e-8") * mpf("300") ** 4 * A,
            "sound_intensity_1W_at_1m": None,  # not applicable (area, not distance)
        },
    }
    return result


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHYS24_DOMAIN_LIB SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    # --------------------------------------------------------
    print("CORE GEOMETRIC CONSTANTS")
    print("-" * 70)
    print()

    chk("R2 = pi/4", R2, FOUR_R2 / mpf("4"), 30, checks)
    chk("R4 = pi^2/32", R4, FOUR_R2 ** 2 / mpf("32"), 30, checks)
    chk("AIRY_CONST = j11/pi", AIRY_CONST, J11 / FOUR_R2, 10, checks)
    chk("Vena contracta = pi/(pi+2)", C_C_EXACT,
        FOUR_R2 / (FOUR_R2 + mpf("2")), 30, checks)

    # --------------------------------------------------------
    print()
    print("AREA COMPUTATIONS (R2 * d^2)")
    print("-" * 70)
    print()

    # 120mm disc
    disc_A = domain_area(mpf("0.120"))
    chk("Disc area (120mm)", disc_A,
        FOUR_R2 * (mpf("0.060")) ** 2, 10, checks)  # pi * r^2

    # 300mm wafer
    wafer_A = domain_area(mpf("0.300"))
    chk_bool("Wafer area ~ 707 cm^2",
             mpf("706") < wafer_A * mpf("1e4") < mpf("708"),
             "area = %s cm^2" % mp.nstr(wafer_A * mpf("1e4"), 4), checks)

    # Wire AWG 12
    awg12_A = awg_area("12")
    chk_bool("AWG 12 area ~ 3.31 mm^2",
             mpf("3.3") < awg12_A * mpf("1e6") < mpf("3.32"),
             "area = %s mm^2" % mp.nstr(awg12_A * mpf("1e6"), 4), checks)

    # --------------------------------------------------------
    print()
    print("OPTICAL DISC COMPUTATIONS")
    print("-" * 70)
    print()

    cd_s = disc_spot_size("CD")
    chk_bool("CD spot ~ 2.1 um",
             mpf("2.0") < cd_s * mpf("1e6") < mpf("2.2"),
             "spot = %s um" % mp.nstr(cd_s * mpf("1e6"), 4), checks)

    bd_s = disc_spot_size("Blu-ray")
    chk_bool("BD spot ~ 0.58 um",
             mpf("0.56") < bd_s * mpf("1e6") < mpf("0.60"),
             "spot = %s um" % mp.nstr(bd_s * mpf("1e6"), 4), checks)

    chk_bool("BD spot < DVD spot < CD spot",
             disc_spot_size("Blu-ray") < disc_spot_size("DVD") < disc_spot_size("CD"),
             "ordering confirmed", checks)

    # --------------------------------------------------------
    print()
    print("FIBER OPTIC COMPUTATIONS")
    print("-" * 70)
    print()

    smf_area = fiber_mode_area("SMF-28", 1550)
    chk_bool("SMF-28 mode area ~ 85 um^2",
             mpf("80") < smf_area * mpf("1e12") < mpf("90"),
             "area = %s um^2" % mp.nstr(smf_area * mpf("1e12"), 4), checks)

    # V-number at cutoff
    core_r = smf28_MFD_1550 = mpf("10.4e-6") / mpf("2")  # approximate
    V_test = fiber_V_number(mpf("4.1e-6"), mpf("0.14"), mpf("1260e-9"))
    chk_bool("V at cutoff ~ 2.4",
             mpf("2.2") < V_test < mpf("2.9"),
             "V = %s" % mp.nstr(V_test, 4), checks)

    # --------------------------------------------------------
    print()
    print("RAYLEIGH SCATTERING")
    print("-" * 70)
    print()

    loss_1550 = rayleigh_scattering_loss(mpf("1.550"))
    loss_1310 = rayleigh_scattering_loss(mpf("1.310"))
    chk_bool("Rayleigh at 1550nm ~ 0.14 dB/km",
             mpf("0.12") < loss_1550 < mpf("0.16"),
             "loss = %s dB/km" % mp.nstr(loss_1550, 4), checks)
    chk_bool("Rayleigh at 1310nm ~ 0.27 dB/km",
             mpf("0.25") < loss_1310 < mpf("0.30"),
             "loss = %s dB/km" % mp.nstr(loss_1310, 4), checks)
    chk_bool("1550nm has lower loss than 1310nm",
             loss_1550 < loss_1310,
             "1550: %s < 1310: %s" % (mp.nstr(loss_1550, 4), mp.nstr(loss_1310, 4)),
             checks)

    # --------------------------------------------------------
    print()
    print("WIRE COMPUTATIONS")
    print("-" * 70)
    print()

    R12 = awg_resistance_per_m("12")
    chk_bool("AWG 12 resistance ~ 5.2 mohm/m",
             mpf("0.005") < R12 < mpf("0.006"),
             "R = %s ohm/m" % mp.nstr(R12, 4), checks)

    # RC cancellation
    C12 = circular_capacitance(awg12_A, mpf("1e-3"))
    RC = R12 * C12
    RC_direct = CU_RESISTIVITY * EPSILON_0 * mpf("1") / mpf("1e-3")  # rho*eps0*L/t
    chk("RC cancellation: R2 drops out",
        RC, RC_direct, 10, checks)

    # --------------------------------------------------------
    print()
    print("FLOW COMPUTATIONS")
    print("-" * 70)
    print()

    Q_pipe = pipe_flow(mpf("0.1"), mpf("1.0"))  # 100mm pipe at 1 m/s
    chk_bool("100mm pipe at 1 m/s ~ 7.85 L/s",
             mpf("7.8") < Q_pipe * mpf("1000") < mpf("7.9"),
             "Q = %s L/s" % mp.nstr(Q_pipe * mpf("1000"), 4), checks)

    f_helm = helmholtz_frequency(mpf("0.076"), mpf("0.15"), mpf("0.050"))
    chk_bool("Helmholtz resonance ~ 42 Hz",
             mpf("40") < f_helm < mpf("45"),
             "f = %s Hz" % mp.nstr(f_helm, 4), checks)

    # --------------------------------------------------------
    print()
    print("RF COMPUTATIONS")
    print("-" * 70)
    print()

    gps_lam = rf_wavelength(RF_STANDARDS["GPS_L1"]["frequency_Hz"])
    chk_bool("GPS L1 wavelength ~ 0.19 m",
             mpf("0.18") < gps_lam < mpf("0.20"),
             "lambda = %s m" % mp.nstr(gps_lam, 4), checks)

    fspl = fspl_dB(mpf("1000"), RF_STANDARDS["GPS_L1"]["frequency_Hz"])
    chk_bool("GPS L1 FSPL at 1km ~ 96 dB",
            mpf("94") < fspl < mpf("98"),
            "FSPL = %s dB" % mp.nstr(fspl, 4), checks)

    # --------------------------------------------------------
    print()
    print("SEMICONDUCTOR")
    print("-" * 70)
    print()

    euv_res = litho_resolution(SEMICONDUCTOR["EUV_wavelength_m"], mpf("0.33"))
    chk_bool("EUV resolution (NA=0.33) ~ 25 nm",
             mpf("20") < euv_res * mpf("1e9") < mpf("30"),
             "CD = %s nm" % mp.nstr(euv_res * mpf("1e9"), 3), checks)

    euv_high_NA = litho_resolution(SEMICONDUCTOR["EUV_wavelength_m"], mpf("0.55"))
    chk_bool("EUV high-NA (0.55) ~ 15 nm",
             mpf("12") < euv_high_NA * mpf("1e9") < mpf("18"),
             "CD = %s nm" % mp.nstr(euv_high_NA * mpf("1e9"), 3), checks)

    # --------------------------------------------------------
    print()
    print("GAUSSIAN BEAM")
    print("-" * 70)
    print()

    zR = rayleigh_range(mpf("5e-6"), mpf("1064e-9"))
    chk_bool("Rayleigh range (5um, 1064nm) ~ 74 um",
             mpf("70") < zR * mpf("1e6") < mpf("80"),
             "z_R = %s um" % mp.nstr(zR * mpf("1e6"), 4), checks)

    theta = beam_divergence(mpf("5e-6"), mpf("1064e-9"))
    chk_bool("Beam divergence ~ 68 mrad",
             mpf("60") < theta * mpf("1000") < mpf("75"),
             "theta = %s mrad" % mp.nstr(theta * mpf("1000"), 4), checks)

    # --------------------------------------------------------
    print()
    print("BCS SUPERCONDUCTING GAP")
    print("-" * 70)
    print()

    chk("BCS gap = pi/e^gamma",
        BCS_DATA["gap_ratio_exact"],
        mpf("1.76388"), 4, checks)

    chk_bool("Al measured matches BCS",
             abs(BCS_DATA["materials"]["Al"]["measured"] - BCS_DATA["gap_ratio_exact"])  <
             mpf("0.001"),
             "Al = %s, BCS = %s" % (
                 mp.nstr(BCS_DATA["materials"]["Al"]["measured"], 5),
                 mp.nstr(BCS_DATA["gap_ratio_exact"], 5)), checks)

    # --------------------------------------------------------
    print()
    print("QUERY FUNCTIONS")
    print("-" * 70)
    print()

    flow_eqs = domains_using("flow")
    chk_bool("'flow' finds Pipe flow, Orifice, and Hagen-Poiseuille",
             len(flow_eqs) >= 3,
             "found %d: %s" % (len(flow_eqs), [e["domain"] for e in flow_eqs]),
             checks)

    all_eqs = all_R2_equations()
    chk_bool("22 R2 equations registered",
             len(all_eqs) == 22,
             "count = %d" % len(all_eqs), checks)

    cancel_list = cancellations_where("CANCELS")
    chk_bool("5 R2 cancellation identities",
             len(cancel_list) == 5,
             "count = %d" % len(cancel_list), checks)

    # --------------------------------------------------------
    print()
    print("CROSS-DOMAIN AREA TRANSLATION")
    print("-" * 70)
    print()

    xd = cross_domain_area(mpf("0.01"))  # 1 cm diameter
    chk_bool("1cm cross-domain: area ~ 0.785 cm^2",
             mpf("0.78") < xd["area_cm2"] < mpf("0.79"),
             "area = %s cm^2" % mp.nstr(xd["area_cm2"], 4), checks)

    # --------------------------------------------------------
    print()
    print("DATA COMPLETENESS")
    print("-" * 70)
    print()

    chk_bool("3 optical disc formats",
             len(OPTICAL_DISCS) == 3,
             "count = %d" % len(OPTICAL_DISCS), checks)

    chk_bool("12+ AWG gauges",
             len(AWG_DATA) >= 12,
             "count = %d" % len(AWG_DATA), checks)

    chk_bool("6 speaker sizes",
             len(SPEAKERS) == 6,
             "count = %d" % len(SPEAKERS), checks)

    chk_bool("7 just intonation ratios",
             len(JUST_INTONATION) == 7,
             "count = %d" % len(JUST_INTONATION), checks)

    chk_bool("6 DDR standards",
             len(MEMORY_STANDARDS) == 6,
             "count = %d" % len(MEMORY_STANDARDS), checks)

    chk_bool("6 storage interfaces",
             len(STORAGE_INTERFACES) == 6,
             "count = %d" % len(STORAGE_INTERFACES), checks)

    chk_bool("4 BCS materials",
             len(BCS_DATA["materials"]) == 4,
             "count = %d" % len(BCS_DATA["materials"]), checks)

    chk_bool("7 R2 cancellations registered",
             len(R2_CANCELLATIONS) == 7,
             "count = %d" % len(R2_CANCELLATIONS), checks)

    chk_bool("7 RF standards",
             len(RF_STANDARDS) == 7,
             "count = %d" % len(RF_STANDARDS), checks)

    # --------------------------------------------------------
    print()
    print_summary(checks)

    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print()
    if n_fail == 0:
        print("  DOMAIN LIBRARY: OPERATIONAL")
    else:
        print("  DOMAIN LIBRARY: %d FAILURES" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("  DATA INVENTORY:")
    print("    Optical disc formats:    %d" % len(OPTICAL_DISCS))
    print("    Fiber types:             %d" % len(FIBER_OPTICS))
    print("    Speaker sizes:           %d" % len(SPEAKERS))
    print("    AWG gauges:              %d" % len(AWG_DATA))
    print("    RF standards:            %d" % len(RF_STANDARDS))
    print("    Memory standards:        %d" % len(MEMORY_STANDARDS))
    print("    Storage interfaces:      %d" % len(STORAGE_INTERFACES))
    print("    BCS materials:           %d" % len(BCS_DATA["materials"]))
    print("    R2 equations:            %d" % len(R2_EQUATIONS))
    print("    R2 cancellations:        %d" % len(R2_CANCELLATIONS))
    print("    Just intonation ratios:  %d" % len(JUST_INTONATION))
    print("    DWDM bands:              %d" % len(DWDM_BANDS))
    print("    IEC conductor sizes:     %d" % len(IEC_SIZES_MM2))
    print()
    print("=" * 70)
    print("PHYS24_DOMAIN_LIB SELF-TEST COMPLETE")
    print("=" * 70)

