#!/usr/bin/env python3
"""
HOWL DATA-5 HELPERS — CHUNK 3: BOUNDARY, HUBBLE & GRAVITY
============================================================
Physics-aware helpers wrapping phys24_boundary_map_lib.py,
phys24_hubble_lib.py, nested_soliton_gravity.py, and
time_process_rate_test.py through the DATA5 object system.

All R2 from Q335 basis via db. All mpf from string.
Conforms to chunk 1/2 API pattern.

Categories:
  BOUNDARY TRAVERSAL    — walk the stack, find by scale, show forces
  SCALE CONVERSION      — energy <-> distance via hbar*c from db
  HUBBLE RUNNING        — H0(N), required r, tension, falsification
  GRAVITY COUPLING      — GM/(rc^2), binding fraction, escape velocity
  HILL SPHERES          — soliton dominance boundaries
  KEPLER VIA R2         — T^2 = 64*R2^2*a^3/(GM) orbital periods
  PROCESS RATE          — gravitational dilation, GPS correction
  MUON & TWINS          — velocity boundary reading, twin paradox
  MOND a0               — cH0/(8R2) transition radius
  HIERARCHY DISPLAY     — nesting levels, coupling table

Usage:
    from data_5_populate import init_data5
    from data_5_helpers_boundary import *

    db = init_data5()
    show_boundary_stack(db)
    show_gps_correction(db)
    show_hubble_data(db)
    show_kepler(db)

Platform: HOWL-PLATFORM-v1
Depends on: data_5_objects.py, data_5_populate.py, phys24_lib.py

~45 functions across 10 categories:

| Category | Count | Key functions |
|---|---|---|
| Boundary traversal | 6 | `find_boundary`, `boundary_at_scale`, `boundaries_between`, `traverse_boundaries`, `show_boundary_stack`, `show_open_questions` |
| Scale conversion | 3 | `energy_to_distance_fm`, `distance_fm_to_energy`, `show_scale_conversion` |
| Hubble running | 9 | `hubble_local`, `hubble_far`, `hubble_cumulative_ratio`, `hubble_tension_sigma`, `hubble_required_r`, `hubble_one_minus_r`, `hubble_running`, `hubble_vp_step_size`, `show_hubble_data` |
| Hubble falsification | 2 | `test_F1_strict`, `test_F1_soft` |
| Gravity coupling | 4 | `grav_coupling`, `binding_fraction`, `escape_velocity`, `show_coupling_hierarchy` |
| Hill spheres | 2 | `hill_sphere`, `show_hill_spheres` |
| Kepler via R2 | 2 | `kepler_period`, `show_kepler` |
| Process rate | 4 | `process_rate_ratio`, `gps_correction`, `show_gps_correction`, `show_process_rates` |
| Muon & twins | 5 | `muon_observed_lifetime`, `twin_paradox`, `ds_squared`, `show_muon_table`, `show_twin_paradox` |
| MOND a0 | 3 | `mond_a0`, `mond_transition_radius`, `show_mond_a0` |
| Hierarchy | 1 | `show_soliton_hierarchy` |

"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, log as mlog, exp as mexp, sqrt as msqrt
from mpmath import pi as mpi

try:
    from phys24_lib import f2m
except ImportError:
    def f2m(f):
        return mpf(f.numerator) / mpf(f.denominator)


_LIB_VERSION = "1"
_LIB_VERSION_1 = ("Session 4, April 3 2026. Chunk 3: Boundary, Hubble "
                   "& gravity. Conforms to chunk 1/2 API pattern.")


# ================================================================
# INTERNAL: shared with chunks 1 and 2
# ================================================================

def _val(db, obj_id):
    """Get value from db. Returns Fraction, mpf, or None."""
    obj = db.get(obj_id)
    if obj is None:
        return None
    if hasattr(obj, 'value'):
        return obj.value
    return None

def _mpf(db, obj_id):
    """Get value as mpf."""
    v = _val(db, obj_id)
    if v is None:
        return None
    if isinstance(v, Fraction):
        return f2m(v)
    return mpf(str(v)) if not isinstance(v, mpf) else v

def _R2(db):
    """R2 = pi/4 from Q335."""
    return f2m(db.get("const.R2").value)

def _four_R2(db):
    return mpf("4") * _R2(db)

def _eight_R2(db):
    return mpf("8") * _R2(db)

def _sixteen_R2(db):
    return mpf("16") * _R2(db)


# ================================================================
# GRAVITATIONAL CONSTANTS — mpf from string
# Not in phys24_lib (Level 2 astrophysical values)
# ================================================================

_G      = mpf("6.674e-11")          # m^3/(kg s^2)
_M_sun  = mpf("1.989e30")           # kg
_M_earth = mpf("5.972e24")          # kg
_M_moon = mpf("7.342e22")           # kg
_R_earth = mpf("6.371e6")           # m
_R_sun  = mpf("6.957e8")            # m
_AU     = mpf("1.496e11")           # m
_pc_m   = mpf("3.086e16")           # m
_kpc_m  = _pc_m * mpf("1000")
_R_GPS  = mpf("2.6556e7")           # m (GPS orbit radius)
_v_GPS  = mpf("3874")               # m/s (GPS satellite velocity)
_c      = mpf("299792458")          # m/s exact
_tau_mu = mpf("2.1969811e-6")       # s (muon rest lifetime, PDG)

# hbar*c in MeV*fm for scale conversions
_hbar_c_MeV_fm = mpf("197.3269804") # MeV*fm


# ================================================================
# BOUNDARY TRAVERSAL
# ================================================================

def find_boundary(db, name_substring):
    """Find boundary objects by name substring (case-insensitive)."""
    q = name_substring.lower()
    return [b for b in db.find(obj_type="boundary")
            if q in b.name.lower()]


def boundary_at_scale(db, scale_MeV):
    """Find the nearest boundary to a given energy scale (MeV)."""
    target = float(mpf(str(scale_MeV)))
    best = None
    best_dist = float("inf")

    for b in db.find(obj_type="boundary"):
        scale = None
        if hasattr(b, 'scale_MeV') and b.scale_MeV is not None:
            scale = float(f2m(b.scale_MeV) if isinstance(b.scale_MeV, Fraction) else b.scale_MeV)
        elif hasattr(b, 'scale_MeV_estimate') and b.scale_MeV_estimate is not None:
            scale = float(f2m(b.scale_MeV_estimate) if isinstance(b.scale_MeV_estimate, Fraction) else b.scale_MeV_estimate)
        if scale is not None:
            dist = abs(scale - target)
            if dist < best_dist:
                best_dist = dist
                best = b
    return best


def boundaries_between(db, lo_MeV, hi_MeV):
    """All boundaries with energy scale between lo and hi (MeV).
    Returns list sorted by energy.
    """
    lo = float(mpf(str(lo_MeV)))
    hi = float(mpf(str(hi_MeV)))
    if lo > hi:
        lo, hi = hi, lo

    result = []
    for b in db.find(obj_type="boundary"):
        scale = None
        if hasattr(b, 'scale_MeV') and b.scale_MeV is not None:
            scale = float(f2m(b.scale_MeV) if isinstance(b.scale_MeV, Fraction) else b.scale_MeV)
        elif hasattr(b, 'scale_MeV_estimate') and b.scale_MeV_estimate is not None:
            scale = float(f2m(b.scale_MeV_estimate) if isinstance(b.scale_MeV_estimate, Fraction) else b.scale_MeV_estimate)
        if scale is not None and lo <= scale <= hi:
            result.append((scale, b))

    result.sort(key=lambda x: x[0])
    return [b for _, b in result]


def traverse_boundaries(db, from_id, to_id):
    """Walk the boundary stack between two boundary objects.
    Prints traversal and returns list of boundaries crossed.
    """
    b_from = db.get(from_id)
    b_to = db.get(to_id)
    if b_from is None or b_to is None:
        print("  ERROR: boundary not found (%s or %s)" % (from_id, to_id))
        return []

    all_with_scale = []
    for b in db.find(obj_type="boundary"):
        scale = None
        if hasattr(b, 'scale_MeV') and b.scale_MeV is not None:
            scale = float(f2m(b.scale_MeV) if isinstance(b.scale_MeV, Fraction) else b.scale_MeV)
        elif hasattr(b, 'scale_MeV_estimate') and b.scale_MeV_estimate is not None:
            scale = float(f2m(b.scale_MeV_estimate) if isinstance(b.scale_MeV_estimate, Fraction) else b.scale_MeV_estimate)
        if scale is not None:
            all_with_scale.append((scale, b))

    all_with_scale.sort(key=lambda x: x[0])

    scale_from = None
    scale_to = None
    for s, b in all_with_scale:
        if b.obj_id == from_id:
            scale_from = s
        if b.obj_id == to_id:
            scale_to = s

    if scale_from is None or scale_to is None:
        print("  ERROR: boundary has no energy scale")
        return []

    lo, hi = min(scale_from, scale_to), max(scale_from, scale_to)
    between = [(s, b) for s, b in all_with_scale if lo <= s <= hi]

    print("  TRAVERSAL: %s -> %s" % (b_from.name, b_to.name))
    print("  Boundaries crossed: %d" % len(between))
    print()

    questions = 0
    for s, b in between:
        b.show()
        if hasattr(b, 'open_questions'):
            questions += len(b.open_questions)

    print()
    print("  Open questions along path: %d" % questions)
    return [b for _, b in between]


def show_boundary_stack(db):
    """Print the complete boundary stack from db."""
    bounds = db.find(obj_type="boundary")
    with_scale = []
    without_scale = []
    for b in bounds:
        scale = None
        if hasattr(b, 'scale_MeV') and b.scale_MeV is not None:
            scale = float(f2m(b.scale_MeV) if isinstance(b.scale_MeV, Fraction) else b.scale_MeV)
        elif hasattr(b, 'scale_MeV_estimate') and b.scale_MeV_estimate is not None:
            scale = float(f2m(b.scale_MeV_estimate) if isinstance(b.scale_MeV_estimate, Fraction) else b.scale_MeV_estimate)
        if scale is not None:
            with_scale.append((scale, b))
        else:
            without_scale.append(b)

    with_scale.sort(key=lambda x: x[0], reverse=True)

    print("  BOUNDARY STACK (high energy -> low energy):")
    print("  %-35s %15s %8s %s" % ("Boundary", "Scale (MeV)", "Known", "Forces"))
    print("  %-35s %15s %8s %s" % ("-" * 35, "-" * 15, "-" * 8, "-" * 20))

    for s, b in with_scale:
        print("  %-35s %15s %8s %s" % (
            b.name[:35], mp.nstr(mpf(str(s)), 4),
            "YES" if b.known else "no",
            ",".join(b.forces_affected[:3]) if b.forces_affected else "—"))

    if without_scale:
        for b in without_scale:
            print("  %-35s %15s %8s %s" % (
                b.name[:35], "—",
                "YES" if b.known else "no",
                ",".join(b.forces_affected[:3]) if b.forces_affected else "—"))


def show_open_questions(db):
    """Print all open questions from boundary objects."""
    print("  OPEN QUESTIONS:")
    count = 0
    for b in db.find(obj_type="boundary"):
        if hasattr(b, 'open_questions') and b.open_questions:
            for q in b.open_questions:
                print("    [%s] %s" % (b.name[:25], q))
                count += 1
    print("  --- %d open questions ---" % count)


# ================================================================
# SCALE CONVERSION
# ================================================================

def energy_to_distance_fm(E_MeV):
    """lambda = hbar*c / E. E in MeV, returns fm."""
    E = mpf(str(E_MeV))
    return _hbar_c_MeV_fm / E


def distance_fm_to_energy(d_fm):
    """E = hbar*c / lambda. d in fm, returns MeV."""
    d = mpf(str(d_fm))
    return _hbar_c_MeV_fm / d


def show_scale_conversion(db, E_MeV):
    """Print energy and distance for a given scale."""
    E = mpf(str(E_MeV))
    d = energy_to_distance_fm(E)
    print("  SCALE: %s MeV = %s fm = %s m" % (
        mp.nstr(E, 4), mp.nstr(d, 4), mp.nstr(d * mpf("1e-15"), 4)))


# ================================================================
# HUBBLE RUNNING (HYPOTHESIS)
# ================================================================

# H0 data — exact Fractions from phys24_hubble_lib.py
_H0_DATA = {
    "SH0ES":      {"H0": Fraction(730, 10), "unc": Fraction(10, 10), "class": "local"},
    "H0LiCOW":    {"H0": Fraction(733, 10), "unc": Fraction(18, 10), "class": "local-medium"},
    "CCHP":       {"H0": Fraction(698, 10), "unc": Fraction(17, 10), "class": "medium"},
    "DES_BAO_BBN": {"H0": Fraction(674, 10), "unc": Fraction(12, 10), "class": "high"},
    "Planck":     {"H0": Fraction(674, 10), "unc": Fraction(5, 10),  "class": "maximum"},
}
_H0_ORDER = ["SH0ES", "H0LiCOW", "CCHP", "DES_BAO_BBN", "Planck"]


def hubble_local(db):
    """H0 local (SH0ES) = 73.0 km/s/Mpc."""
    return _H0_DATA["SH0ES"]["H0"]


def hubble_far(db):
    """H0 far (Planck) = 67.4 km/s/Mpc."""
    return _H0_DATA["Planck"]["H0"]


def hubble_cumulative_ratio(db):
    """H0_far / H0_local = 337/365."""
    return hubble_far(db) / hubble_local(db)


def hubble_tension_sigma(db):
    """Tension in sigma: (H0_local - H0_far) / sqrt(unc1^2 + unc2^2)."""
    local = f2m(_H0_DATA["SH0ES"]["H0"])
    far = f2m(_H0_DATA["Planck"]["H0"])
    u1 = f2m(_H0_DATA["SH0ES"]["unc"])
    u2 = f2m(_H0_DATA["Planck"]["unc"])
    return (local - far) / msqrt(u1 ** 2 + u2 ** 2)


def hubble_required_r(db, N):
    """r = (H0_far/H0_local)^(1/N) for a given boundary count N."""
    ratio = f2m(hubble_cumulative_ratio(db))
    return ratio ** (mpf("1") / mpf(str(N)))


def hubble_one_minus_r(db, N):
    """1 - r, the per-transit correction magnitude."""
    return mpf("1") - hubble_required_r(db, N)


def hubble_running(db, H0_0, r, N):
    """H0(N) = H0_0 * r^N."""
    h0 = f2m(H0_0) if isinstance(H0_0, Fraction) else mpf(str(H0_0))
    r_val = mpf(str(r))
    return h0 * r_val ** mpf(str(N))


def hubble_vp_step_size(db):
    """VP step = 1/(3*pi) = 1/(12*R2). The alpha running per-threshold step."""
    return mpf("1") / (mpf("12") * _R2(db))


def show_hubble_data(db):
    """Print H0 measurements and running curve constraints."""
    print("  HUBBLE MEASUREMENTS (from phys24_hubble_lib):")
    print("  %-15s %8s %6s %s" % ("Method", "H0", "±", "Class"))
    print("  %-15s %8s %6s %s" % ("-" * 15, "-" * 8, "-" * 6, "-" * 15))
    for key in _H0_ORDER:
        d = _H0_DATA[key]
        print("  %-15s %8s %6s %s" % (
            key, f2m(d["H0"]), f2m(d["unc"]), d["class"]))

    print()
    print("  Cumulative ratio: %s = %s" % (
        hubble_cumulative_ratio(db),
        mp.nstr(f2m(hubble_cumulative_ratio(db)), 6)))
    print("  Tension: %s sigma" % mp.nstr(hubble_tension_sigma(db), 3))
    print()
    print("  RUNNING CURVE r(N) = (67.4/73.0)^(1/N):")
    for N in [10, 100, 1000, 10000]:
        r = hubble_required_r(db, N)
        omr = hubble_one_minus_r(db, N)
        print("    N=%5d: r = %s, 1-r = %s" % (
            N, mp.nstr(r, 8), mp.nstr(omr, 4)))

    print()
    print("  VP step = 1/(12*R2) = %s" % mp.nstr(hubble_vp_step_size(db), 6))
    print("  STATUS: HYPOTHESIS. All effective_N = None.")


def test_F1_strict(db):
    """F1 strict: Are raw H0 values monotonically decreasing?
    Returns (passed, detail_string).
    """
    vals = [f2m(_H0_DATA[k]["H0"]) for k in _H0_ORDER]
    for i in range(len(vals) - 1):
        if vals[i + 1] > vals[i]:
            return (False, "H0 increases from %s to %s: %s > %s" % (
                _H0_ORDER[i], _H0_ORDER[i + 1],
                mp.nstr(vals[i + 1], 4), mp.nstr(vals[i], 4)))
    return (True, "Monotonically decreasing across %d points" % len(vals))


def test_F1_soft(db):
    """F1 soft: Monotonic within 1-sigma? Only fails if hard inversion."""
    violations = []
    for i in range(len(_H0_ORDER) - 1):
        near = _H0_DATA[_H0_ORDER[i]]
        far = _H0_DATA[_H0_ORDER[i + 1]]
        nv = f2m(near["H0"])
        fv = f2m(far["H0"])
        if fv > nv:
            f_lower = fv - f2m(far["unc"])
            n_upper = nv + f2m(near["unc"])
            if f_lower > n_upper:
                violations.append("%s > %s at 1-sigma" % (
                    _H0_ORDER[i + 1], _H0_ORDER[i]))
    return (len(violations) == 0, violations)


# ================================================================
# GRAVITY COUPLING
# ================================================================

def grav_coupling(M_kg, r_m):
    """GM/(rc^2) — the gravitational soliton coupling strength.
    Dimensionless. Determines well depth, GR corrections, process rate.
    """
    M = mpf(str(M_kg))
    r = mpf(str(r_m))
    return _G * M / (r * _c ** 2)


def binding_fraction(M_kg, R_m):
    """Self-gravitational binding: |U|/Mc^2 = 3GM/(5Rc^2).
    What fraction of rest mass is gravitational pattern energy.
    """
    M = mpf(str(M_kg))
    R = mpf(str(R_m))
    return mpf("3") * _G * M / (mpf("5") * R * _c ** 2)


def escape_velocity(M_kg, r_m):
    """v_esc = sqrt(2GM/r). Minimum speed to leave the soliton."""
    M = mpf(str(M_kg))
    r = mpf(str(r_m))
    return msqrt(mpf("2") * _G * M / r)


def show_coupling_hierarchy(db):
    """Print GM/(rc^2) at every level of the soliton hierarchy."""
    systems = [
        ("Earth-Moon orbit",  _M_earth, mpf("3.844e8")),
        ("Earth surface",     _M_earth, _R_earth),
        ("Sun-Earth orbit",   _M_sun,   _AU),
        ("Sun surface",       _M_sun,   _R_sun),
        ("Neutron star",      mpf("2.8") * _M_sun, mpf("1.1e4")),
    ]
    print("  GRAVITATIONAL COUPLING HIERARCHY  GM/(rc^2):")
    print("  %-25s %15s %15s" % ("System", "GM/(rc^2)", "v_esc/c"))
    print("  %-25s %15s %15s" % ("-" * 25, "-" * 15, "-" * 15))
    for name, M, r in systems:
        gc = grav_coupling(M, r)
        ve = escape_velocity(M, r)
        print("  %-25s %15s %15s" % (
            name, mp.nstr(gc, 4), mp.nstr(ve / _c, 4)))


# ================================================================
# HILL SPHERES — SOLITON DOMINANCE BOUNDARIES
# ================================================================

def hill_sphere(m_kg, M_kg, a_m):
    """R_Hill = a * (m/(3M))^(1/3).
    The soliton dominance boundary (R5).
    Inside: body's gravity dominates. Outside: container's.
    """
    m = mpf(str(m_kg))
    M = mpf(str(M_kg))
    a = mpf(str(a_m))
    return a * (m / (mpf("3") * M)) ** (mpf("1") / mpf("3"))


def show_hill_spheres(db):
    """Print Hill sphere table for key systems."""
    systems = [
        ("Earth in Solar",  _M_earth, _M_sun, _AU),
        ("Moon in Earth",   _M_moon, _M_earth, mpf("3.844e8")),
        ("Sun in Galaxy",   _M_sun, mpf("3.6e11") * _M_sun, mpf("8.2") * _kpc_m),
        ("Jupiter in Solar", mpf("1.898e27"), _M_sun, mpf("7.785e11")),
    ]
    print("  HILL SPHERES  R_Hill = a*(m/(3M))^(1/3):")
    print("  %-25s %15s %15s" % ("System", "R_Hill (km)", "R_Hill (AU)"))
    print("  %-25s %15s %15s" % ("-" * 25, "-" * 15, "-" * 15))
    for name, m, M, a in systems:
        rh = hill_sphere(m, M, a)
        print("  %-25s %15s %15s" % (
            name,
            mp.nstr(rh / mpf("1000"), 4),
            mp.nstr(rh / _AU, 4)))


# ================================================================
# KEPLER VIA R2
# ================================================================

def kepler_period(db, a_m, M_kg):
    """T = sqrt(64*R2^2 * a^3 / (GM)).
    Kepler's third law in R2 form: 4*pi^2 = (8R2)^2 = 64*R2^2.
    """
    a = mpf(str(a_m))
    M = mpf(str(M_kg))
    R2 = _R2(db)
    return msqrt(mpf("64") * R2 ** 2 * a ** 3 / (_G * M))


def show_kepler(db):
    """Print Kepler's law verification for solar system planets."""
    planets = [
        ("Mercury", mpf("5.791e10"), mpf("0.2408") * mpf("365.25") * mpf("86400")),
        ("Venus",   mpf("1.082e11"), mpf("0.6152") * mpf("365.25") * mpf("86400")),
        ("Earth",   _AU,             mpf("365.25") * mpf("86400")),
        ("Mars",    mpf("2.279e11"), mpf("1.8808") * mpf("365.25") * mpf("86400")),
        ("Jupiter", mpf("7.785e11"), mpf("11.862") * mpf("365.25") * mpf("86400")),
        ("Saturn",  mpf("1.434e12"), mpf("29.457") * mpf("365.25") * mpf("86400")),
    ]
    print("  KEPLER VIA R2  T^2 = 64*R2^2 * a^3 / (GM):")
    print("  %-10s %12s %14s %14s %10s" % (
        "Planet", "a (m)", "T_obs (s)", "T_R2 (s)", "Ratio"))
    print("  %-10s %12s %14s %14s %10s" % (
        "-" * 10, "-" * 12, "-" * 14, "-" * 14, "-" * 10))
    for name, a, T_obs in planets:
        T_r2 = kepler_period(db, a, _M_sun)
        ratio = T_r2 / T_obs
        print("  %-10s %12s %14s %14s %10s" % (
            name, mp.nstr(a, 4), mp.nstr(T_obs, 5),
            mp.nstr(T_r2, 5), mp.nstr(ratio, 6)))
    print("  4*pi^2 = (8R2)^2 = 64R2^2. Same R2 as pipes, wires, discs.")


# ================================================================
# PROCESS RATE (gravitational time dilation)
# ================================================================

def process_rate_ratio(M_kg, r_m):
    """sqrt(1 - 2GM/(rc^2)). Process rate relative to infinity.
    = 1 for infinity, < 1 deeper in the well.
    """
    coupling = grav_coupling(M_kg, r_m)
    exact = msqrt(mpf("1") - mpf("2") * coupling)
    return {
        "coupling": coupling,
        "exact_ratio": exact,
        "fractional_shift": mpf("1") - exact,
    }


def gps_correction(db):
    """Compute GPS clock correction: gravitational + velocity effects.
    Returns dict with components in ns/day and us/day.
    """
    # Gravitational: df/f = GM/c^2 * (1/R_earth - 1/R_GPS)
    grav_shift = _G * _M_earth / _c ** 2 * (
        mpf("1") / _R_earth - mpf("1") / _R_GPS)

    # Velocity: df/f = -v^2/(2c^2)
    vel_shift = -_v_GPS ** 2 / (mpf("2") * _c ** 2)

    total_shift = grav_shift + vel_shift

    ns_per_day_grav = grav_shift * mpf("86400") * mpf("1e9")
    ns_per_day_vel = vel_shift * mpf("86400") * mpf("1e9")
    ns_per_day_total = total_shift * mpf("86400") * mpf("1e9")

    return {
        "grav_shift": grav_shift,
        "vel_shift": vel_shift,
        "total_shift": total_shift,
        "grav_ns_day": ns_per_day_grav,
        "vel_ns_day": ns_per_day_vel,
        "total_ns_day": ns_per_day_total,
        "total_us_day": ns_per_day_total / mpf("1000"),
    }


def show_gps_correction(db):
    """Print GPS clock correction breakdown."""
    g = gps_correction(db)
    print("  GPS CLOCK CORRECTION (soliton reading difference):")
    print("    Gravitational (higher = faster): +%s us/day" % mp.nstr(
        g["grav_ns_day"] / mpf("1000"), 4))
    print("    Velocity (moving = slower):      %s us/day" % mp.nstr(
        g["vel_ns_day"] / mpf("1000"), 4))
    print("    NET correction:                  +%s us/day" % mp.nstr(
        g["total_us_day"], 4))
    print("    Without correction: GPS drifts ~10 km/day.")
    print("    The correction = GM/(rc^2), the soliton coupling strength.")


def show_process_rates(db):
    """Print process rate at key locations."""
    locations = [
        ("Earth surface",           _M_earth, _R_earth),
        ("GPS orbit",               _M_earth, _R_GPS),
        ("Sun surface",             _M_sun,   _R_sun),
        ("Neutron star",            mpf("2.8") * _M_sun, mpf("1.1e4")),
        ("Earth orbit (Sun field)", _M_sun,   _AU),
    ]
    print("  PROCESS RATE = sqrt(1 - 2GM/(rc^2)):")
    print("  %-30s %15s %15s" % ("Location", "GM/(rc^2)", "Shift from inf"))
    print("  %-30s %15s %15s" % ("-" * 30, "-" * 15, "-" * 15))
    for name, M, r in locations:
        pr = process_rate_ratio(M, r)
        print("  %-30s %15s %15s" % (
            name, mp.nstr(pr["coupling"], 4),
            mp.nstr(pr["fractional_shift"], 4)))


# ================================================================
# MUON LIFETIME & TWIN PARADOX
# ================================================================

def muon_observed_lifetime(v_over_c):
    """Muon lifetime as observed across velocity boundary.
    tau_obs = tau_rest * gamma. Internal rate is FIXED.
    gamma = 1/sqrt(1 - v^2/c^2).
    """
    v = mpf(str(v_over_c))
    gamma = mpf("1") / msqrt(mpf("1") - v ** 2)
    return {
        "v_over_c": v,
        "gamma": gamma,
        "tau_rest_us": _tau_mu * mpf("1e6"),
        "tau_observed_us": _tau_mu * gamma * mpf("1e6"),
    }


def twin_paradox(db, v_over_c, years_A):
    """Twin A stays home, Twin B travels at v/c for years_A (A's clock).
    Returns cycle counts using dv_Cs from db.
    """
    v = mpf(str(v_over_c))
    yA = mpf(str(years_A))
    gamma = mpf("1") / msqrt(mpf("1") - v ** 2)
    yB = yA / gamma

    dv = _mpf(db, "const.dv_Cs")
    sec_per_year = mpf("365.25") * mpf("86400")
    cycles_A = yA * sec_per_year * dv
    cycles_B = yB * sec_per_year * dv

    return {
        "v_over_c": v,
        "gamma": gamma,
        "years_A": yA,
        "years_B": yB,
        "cycles_A": cycles_A,
        "cycles_B": cycles_B,
        "cycle_difference": cycles_A - cycles_B,
    }


def ds_squared(dt, dx, dy="0", dz="0"):
    """Minkowski interval: ds^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2.
    Negative = timelike. Positive = spacelike. Zero = lightlike.
    """
    t = mpf(str(dt))
    x = mpf(str(dx))
    y = mpf(str(dy))
    z = mpf(str(dz))
    return -_c ** 2 * t ** 2 + x ** 2 + y ** 2 + z ** 2


def show_muon_table(db):
    """Print muon lifetime at several velocities."""
    print("  MUON LIFETIME (reading across velocity boundary):")
    print("  %-8s %10s %12s %12s" % ("v/c", "gamma", "tau_rest(us)", "tau_obs(us)"))
    print("  %-8s %10s %12s %12s" % ("-" * 8, "-" * 10, "-" * 12, "-" * 12))
    for v in ["0", "0.5", "0.9", "0.99", "0.999"]:
        m = muon_observed_lifetime(v)
        print("  %-8s %10s %12s %12s" % (
            v, mp.nstr(m["gamma"], 5),
            mp.nstr(m["tau_rest_us"], 5),
            mp.nstr(m["tau_observed_us"], 5)))
    print("  Muon process rate is FIXED. Observer reads across boundary.")


def show_twin_paradox(db, v_over_c="0.9", years="10"):
    """Print twin paradox analysis."""
    t = twin_paradox(db, v_over_c, years)
    print("  TWIN PARADOX (different cycle counts, not different time):")
    print("    Twin B velocity: %sc" % t["v_over_c"])
    print("    gamma: %s" % mp.nstr(t["gamma"], 5))
    print("    Twin A: %s years, %s cesium cycles" % (
        mp.nstr(t["years_A"], 4), mp.nstr(t["cycles_A"], 4)))
    print("    Twin B: %s years, %s cesium cycles" % (
        mp.nstr(t["years_B"], 4), mp.nstr(t["cycles_B"], 4)))
    print("    Difference: %s cycles" % mp.nstr(t["cycle_difference"], 4))
    print("    Two vortexes, different paths, different oscillation counts.")


# ================================================================
# MOND a0 CONNECTION
# ================================================================

def mond_a0(db):
    """a0 = c*H0/(8*R2) = c*H0/(2*pi).
    The MOND acceleration scale from R2 and Hubble.
    Uses H0 = 67.4 km/s/Mpc (Planck) in SI units.
    """
    H0_SI = mpf("67.4") * mpf("1000") / mpf("3.086e22")
    return _c * H0_SI / (_eight_R2(db))


def mond_transition_radius(db, M_kg):
    """Radius where g(r) = GM/r^2 = a0. Below: Newtonian. Above: MOND.
    r = sqrt(GM/a0).
    """
    M = mpf(str(M_kg))
    a0 = mond_a0(db)
    return msqrt(_G * M / a0)


def show_mond_a0(db):
    """Print MOND a0 and transition radii."""
    a0 = mond_a0(db)
    print("  MOND a0 = c*H0/(8*R2) = c*H0/(2*pi):")
    print("    a0 = %s m/s^2" % mp.nstr(a0, 4))
    print("    a0 (published MOND) ~ 1.2e-10 m/s^2")
    print("    Match: %s%%" % mp.nstr(
        abs(a0 - mpf("1.2e-10")) / mpf("1.2e-10") * mpf("100"), 3))
    print()

    for name, M in [("Earth", _M_earth), ("Sun", _M_sun)]:
        r = mond_transition_radius(db, M)
        print("    %s: g = a0 at r = %s AU = %s pc" % (
            name, mp.nstr(r / _AU, 3),
            mp.nstr(r / _pc_m, 3)))


# ================================================================
# HIERARCHY DISPLAY
# ================================================================

def show_soliton_hierarchy(db):
    """Print the complete 11-level nesting hierarchy."""
    hierarchy = [
        ("Proton (QCD)",       "~1 fm",       "99%%",      "b3 = -7",          "Confinement"),
        ("Atom (EM)",          "~0.1 nm",     "~10^-8",    "alpha = 1/137",   "Ionization"),
        ("Crystal lattice",    "~1 nm-km",    "~10^-10",   "Band structure",  "Melting"),
        ("Geological",         "~m-km",       "~10^-10",   "Material strength", "Phase boundary"),
        ("Human on surface",   "~1.7 m",      "~10^-9",    "GM_E/(R_E*c^2)",  "Jump height"),
        ("Earth Hill sphere",  "~1.5e6 km",   "~10^-9",    "M_E/M_Sun ratio", "L1 Lagrange"),
        ("Earth orbit",        "1 AU",        "~10^-8",    "Kepler T^2~a^3",  "v_escape"),
        ("Solar Hill sphere",  "~120 AU",     "~10^-6",    "M_Sun/M_gal",     "Voyager"),
        ("Galactic disk",      "~15 kpc",     "~10^-6",    "DM/bar=(22/13)pi", "Virial radius"),
        ("Galaxy cluster",     "~3 Mpc",      "~10^-5",    "DM ~ 85%%",       "Virial radius"),
        ("BAO/cosmological",   "~150 Mpc",    "—",         "N~100 boundaries", "H0 running"),
    ]
    print("  SOLITON NESTING HIERARCHY (11 levels):")
    print("  %-22s %12s %10s %-20s %s" % (
        "Level", "Size", "|U|/Mc^2", "Integer Rule", "Boundary"))
    print("  %-22s %12s %10s %-20s %s" % (
        "-" * 22, "-" * 12, "-" * 10, "-" * 20, "-" * 12))
    for name, size, coupling, rule, boundary in hierarchy:
        print("  %-22s %12s %10s %-20s %s" % (
            name, size, coupling, rule, boundary))
    print()
    print("  Same principle at every level: ground state within container.")
    print("  GM/(rc^2) determines well depth. R2 in every orbital area.")
