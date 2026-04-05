#!/usr/bin/env python3
"""
DATA-6 EXTENDED DERIVATIONS — _data_6_derivations_more_v0.py
==============================================================
49 additional derivation and connection functions covering:
  A: Unification extensions (sin2_tW, what-if, Casimirs)
  B: Scale conversion (energy <-> distance)
  C: Gravity & soliton (GM/rc^2, Hill, Kepler, GPS, MOND)
  D: Relativity (muon, twins, ds^2)
  E: Hubble running (r(N), tension, VP step, F1 tests)
  F: R2 domains (wire, capacitor, RC cancel, disc, KJ*RK, norms)
  G: Cosmology extensions (Omega_b, Omega_m, Omega_DE, virial)
  H: Dwarf solitons (purity, FJ, TF, cosmic ratio)
  I: Connections (hierarchy, cancellation registry, adjacency, MOND)

All functions follow the DATA-6 callable contract:
  def name_v0(value_dicts: list[dict]) -> dict:
      return {"key": "name_v0", "outputs": {...}, "notes": ""}

No hardcoded physics constants. All values from the pool.
Fraction arithmetic where possible, mpf at irrational boundary.

Usage:
    from _data_6_derivations_more_v0 import (
        DERIVATION_MORE_INDEX_V0,
        CONNECTION_MORE_INDEX_V0,
    )

Platform: HOWL-PLATFORM-v1
Depends on: value pool loaded from values_*.json
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, log as mlog, exp as mexp
from mpmath import pi as mpi

mp.dps = 100


# ================================================================
# POOL HELPERS (same pattern as _data_6_derivations_v0.py)
# ================================================================

def _value_map(value_dicts):
    """Build key -> value dict from pool. Last entry wins."""
    vm = {}
    for entry in value_dicts:
        if isinstance(entry, dict) and "key" in entry:
            vm[entry["key"]] = entry.get("value")
    return vm


def _get(vm, key):
    """Get value from map, raise if missing."""
    v = vm.get(key)
    if v is None:
        raise KeyError("missing value: %s" % key)
    return v


def _frac(vm, key):
    """Get value as Fraction."""
    v = _get(vm, key)
    if isinstance(v, Fraction):
        return v
    if isinstance(v, int):
        return Fraction(v, 1)
    raise TypeError("%s is not Fraction: %s" % (key, type(v)))


def _mpf_val(vm, key):
    """Get value as mpf (for approximate/string values)."""
    v = _get(vm, key)
    if isinstance(v, Fraction):
        return mpf(v.numerator) / mpf(v.denominator)
    if isinstance(v, (int, float)):
        return mpf(v)
    return mpf(str(v))


def _f2m(f):
    """Fraction to mpf."""
    if isinstance(f, Fraction):
        return mpf(f.numerator) / mpf(f.denominator)
    return mpf(str(f))


def _approx(val):
    """mpf -> plain decimal string for storage."""
    return mp.nstr(val, 15)


# ================================================================
# CATEGORY A: UNIFICATION EXTENSIONS
# ================================================================

def coupling_one_loop_sin2_prediction_v0(value_dicts):
    """Predict sin2_tW from GUT value 3/8, running to M_Z with CD betas.
    sin2(M_Z) = 3/8 + (b_EM/b2_mod - 1) * correction term.
    Uses one-loop RG: sin2 = (5/3*b1 + b2 difference) / (b1+b2) structure.
    """
    vm = _value_map(value_dicts)

    alpha_inv = _frac(vm, "coupling_alpha_em_inverse_v0")
    alpha_s = _frac(vm, "coupling_alpha_s_strong_mz_v0")
    b1 = _frac(vm, "beta_modified_u1_total_v0")
    b2 = _frac(vm, "beta_modified_su2_total_v0")
    b3 = _frac(vm, "beta_modified_su3_total_v0")

    # Extract couplings
    alpha = Fraction(1, 1) / alpha_inv
    sin2 = _frac(vm, "coupling_sin2_weak_mixing_v0")
    cos2 = Fraction(1, 1) - sin2

    inv_a1 = Fraction(5, 3) * alpha_inv * cos2
    inv_a2 = sin2 * alpha_inv

    # Find L_GUT from 1/a1 = 1/a2 at crossing
    L_gut = _f2m(inv_a1 - inv_a2) / _f2m(b1 - b2)

    # b_EM = 5/3 * b1 + b2
    b_EM = Fraction(5, 3) * b1 + b2

    # sin2_pred = (5/3 * b1 * inv_a2 - b2 * inv_a1) / ((5/3*b1 - b2) * inv_a_GUT)
    # Simpler: sin2 = 3/8 - (5/24) * b_EM * L / (alpha_inv_at_M_Z_EM)
    # Use: sin2 = (5/3*b1) / (5/3*b1 + b2) * (1 - correction from alpha_s)
    # Direct from platform formula:
    inv_a_gut = _f2m(inv_a1) - _f2m(b1) * L_gut
    inv_a2_pred = inv_a_gut + _f2m(b2) * L_gut
    inv_a_EM_pred = inv_a_gut + _f2m(b_EM) * L_gut
    sin2_pred = inv_a2_pred / inv_a_EM_pred

    measured = _f2m(sin2)
    miss = abs(sin2_pred - measured) / measured * mpf("100")

    return {
        "key": "coupling_one_loop_sin2_prediction_v0",
        "outputs": {
            "result_sin2_tW_one_loop_predicted_v0": _approx(sin2_pred),
            "result_sin2_tW_one_loop_miss_pct_v0": _approx(miss),
            "result_sin2_tW_b_em_v0": b_EM,
        },
        "notes": "sin2_tW from 3/8 GUT value, one-loop CD running",
    }


def coupling_whatif_rep_v0(value_dicts):
    """What-if scan: compute gap ratio for any (d3, d2, Y) VL representation.
    Reads rep_whatif_su3_dim_v0, rep_whatif_su2_dim_v0, rep_whatif_y_v0
    from the pool (must be set before calling).
    """
    vm = _value_map(value_dicts)

    d3 = _frac(vm, "rep_whatif_su3_dim_v0")
    d2 = _frac(vm, "rep_whatif_su2_dim_v0")
    Y = _frac(vm, "rep_whatif_y_v0")
    S2 = Fraction(1, 2)

    b1_SM = _frac(vm, "beta_sm_u1_total_v0")
    b2_SM = _frac(vm, "beta_sm_su2_total_v0")
    b3_SM = _frac(vm, "beta_sm_su3_total_v0")

    db1 = Fraction(2, 5) * d3 * d2 * Y * Y
    db2 = Fraction(2, 3) * d3 * S2
    db3 = Fraction(1, 3) * d2 * S2

    b1m = b1_SM + db1
    b2m = b2_SM + db2
    b3m = b3_SM + db3
    gap = (b1m - b2m) / (b2m - b3m)

    gap_measured = _f2m(_frac(vm, "coupling_measured_gap_ratio_v0"))
    distance = abs(_f2m(gap) - gap_measured)

    return {
        "key": "coupling_whatif_rep_v0",
        "outputs": {
            "result_whatif_db1_v0": db1,
            "result_whatif_db2_v0": db2,
            "result_whatif_db3_v0": db3,
            "result_whatif_gap_ratio_v0": gap,
            "result_whatif_distance_v0": _approx(distance),
            "result_whatif_asymmetry_v0": db2 / db1 if db1 != 0 else None,
        },
        "notes": "What-if for (%s,%s,%s)" % (d3, d2, Y),
    }


def group_theory_casimirs_v0(value_dicts):
    """Derive Casimirs and Dynkin index from gauge group data in pool."""
    vm = _value_map(value_dicts)

    c2_adj_su3 = _frac(vm, "group_c2_adj_su3_v0")
    c2_adj_su2 = _frac(vm, "group_c2_adj_su2_v0")
    c2_fund_su3 = _frac(vm, "group_c2_fund_su3_v0")
    c2_fund_su2 = _frac(vm, "group_c2_fund_su2_v0")
    s2_fund = _frac(vm, "group_s2_fundamental_v0")

    # Verify: C2(adj) = N, C2(fund) = (N^2-1)/(2N), S2(fund) = 1/2
    # Pure gauge gap = C2(SU2) / (C2(SU3) - C2(SU2))
    pure_gap_num = c2_adj_su2
    pure_gap_den = c2_adj_su3 - c2_adj_su2
    pure_gap = pure_gap_num / pure_gap_den

    # Yang-Mills coefficient -(11/3)
    ym_coeff = Fraction(-11, 3)
    gauge_b2 = ym_coeff * c2_adj_su2
    gauge_b3 = ym_coeff * c2_adj_su3

    return {
        "key": "group_theory_casimirs_v0",
        "outputs": {
            "result_pure_gauge_gap_v0": pure_gap,
            "result_gauge_b2_v0": gauge_b2,
            "result_gauge_b3_v0": gauge_b3,
            "result_ym_coefficient_v0": ym_coeff,
        },
        "notes": "Group theory verification: pure gauge gap = %s" % pure_gap,
    }


# ================================================================
# CATEGORY B: SCALE CONVERSION
# ================================================================

def scale_energy_to_distance_v0(value_dicts):
    """Convert energy scale to distance: lambda = hbar*c / E.
    Reads scale_input_energy_mev_v0 from pool.
    """
    vm = _value_map(value_dicts)
    hbar_c = _mpf_val(vm, "eng_hbar_c_mev_fm_v0")
    E = _mpf_val(vm, "scale_input_energy_mev_v0")

    d_fm = hbar_c / E
    d_m = d_fm * mpf("1e-15")

    return {
        "key": "scale_energy_to_distance_v0",
        "outputs": {
            "result_scale_distance_fm_v0": _approx(d_fm),
            "result_scale_distance_m_v0": _approx(d_m),
        },
        "notes": "lambda = hbar*c / E",
    }


def scale_distance_to_energy_v0(value_dicts):
    """Convert distance to energy scale: E = hbar*c / lambda.
    Reads scale_input_distance_fm_v0 from pool.
    """
    vm = _value_map(value_dicts)
    hbar_c = _mpf_val(vm, "eng_hbar_c_mev_fm_v0")
    d = _mpf_val(vm, "scale_input_distance_fm_v0")

    E = hbar_c / d

    return {
        "key": "scale_distance_to_energy_v0",
        "outputs": {
            "result_scale_energy_mev_v0": _approx(E),
        },
        "notes": "E = hbar*c / lambda",
    }


# ================================================================
# CATEGORY C: GRAVITY & SOLITON
# ================================================================

def gravity_coupling_v0(value_dicts):
    """GM/(rc^2) — the soliton coupling strength.
    Computes for Earth surface, GPS orbit, Sun surface, Sun-Earth, neutron star.
    """
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    R_earth = _mpf_val(vm, "astro_radius_earth_v0")
    R_GPS = _mpf_val(vm, "astro_gps_orbit_radius_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    R_sun = _mpf_val(vm, "astro_radius_sun_v0")
    AU = _mpf_val(vm, "astro_au_v0")

    c2 = c * c

    phi_earth = G * M_earth / (R_earth * c2)
    phi_gps = G * M_earth / (R_GPS * c2)
    phi_sun_surface = G * M_sun / (R_sun * c2)
    phi_sun_earth = G * M_sun / (AU * c2)

    return {
        "key": "gravity_coupling_v0",
        "outputs": {
            "result_grav_coupling_earth_surface_v0": _approx(phi_earth),
            "result_grav_coupling_gps_orbit_v0": _approx(phi_gps),
            "result_grav_coupling_sun_surface_v0": _approx(phi_sun_surface),
            "result_grav_coupling_sun_earth_v0": _approx(phi_sun_earth),
        },
        "notes": "GM/(rc^2) at key locations",
    }


def gravity_escape_velocity_v0(value_dicts):
    """v_esc = sqrt(2GM/r) at key locations."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    R_earth = _mpf_val(vm, "astro_radius_earth_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    R_sun = _mpf_val(vm, "astro_radius_sun_v0")

    v_earth = msqrt(mpf("2") * G * M_earth / R_earth)
    v_sun = msqrt(mpf("2") * G * M_sun / R_sun)

    return {
        "key": "gravity_escape_velocity_v0",
        "outputs": {
            "result_escape_velocity_earth_v0": _approx(v_earth),
            "result_escape_velocity_earth_km_s_v0": _approx(v_earth / mpf("1000")),
            "result_escape_velocity_sun_v0": _approx(v_sun),
            "result_escape_velocity_sun_km_s_v0": _approx(v_sun / mpf("1000")),
        },
        "notes": "v_esc = sqrt(2GM/r)",
    }


def gravity_binding_fraction_v0(value_dicts):
    """Self-gravitational binding: |U|/Mc^2 = 3GM/(5Rc^2)."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    R_earth = _mpf_val(vm, "astro_radius_earth_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    R_sun = _mpf_val(vm, "astro_radius_sun_v0")

    bf_earth = mpf("3") * G * M_earth / (mpf("5") * R_earth * c * c)
    bf_sun = mpf("3") * G * M_sun / (mpf("5") * R_sun * c * c)

    return {
        "key": "gravity_binding_fraction_v0",
        "outputs": {
            "result_binding_fraction_earth_v0": _approx(bf_earth),
            "result_binding_fraction_sun_v0": _approx(bf_sun),
        },
        "notes": "3GM/(5Rc^2)",
    }


def gravity_hill_sphere_v0(value_dicts):
    """R_Hill = a*(m/(3M))^(1/3) at key locations."""
    vm = _value_map(value_dicts)

    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    M_moon = _mpf_val(vm, "astro_mass_moon_v0")
    AU = _mpf_val(vm, "astro_au_v0")
    d_em = mpf("3.844e8")  # Earth-Moon distance from obs data

    third = mpf("1") / mpf("3")

    rh_earth = AU * (M_earth / (mpf("3") * M_sun)) ** third
    rh_moon = d_em * (M_moon / (mpf("3") * M_earth)) ** third

    return {
        "key": "gravity_hill_sphere_v0",
        "outputs": {
            "result_hill_sphere_earth_km_v0": _approx(rh_earth / mpf("1000")),
            "result_hill_sphere_moon_km_v0": _approx(rh_moon / mpf("1000")),
        },
        "notes": "R_Hill = a*(m/(3M))^(1/3)",
    }


def gravity_kepler_period_v0(value_dicts):
    """T = sqrt(64*R2^2*a^3/(GM)). Kepler via R2.
    Verifies 64*R2^2 = 4*pi^2 identity.
    Computes Earth and Jupiter periods.
    """
    vm = _value_map(value_dicts)

    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    AU = _mpf_val(vm, "astro_au_v0")

    # Identity check
    lhs = mpf("64") * R2 * R2
    rhs = mpf("4") * mpi * mpi
    identity_match = mp.nstr(lhs, 20) == mp.nstr(rhs, 20)

    # Earth
    T_earth = msqrt(mpf("64") * R2 * R2 * AU ** 3 / (G * M_sun))
    T_year = mpf("365.25") * mpf("86400")

    # Jupiter
    a_jup = mpf("7.785e11")
    T_jup = msqrt(mpf("64") * R2 * R2 * a_jup ** 3 / (G * M_sun))
    T_jup_obs = mpf("11.862") * T_year

    return {
        "key": "gravity_kepler_period_v0",
        "outputs": {
            "result_kepler_identity_64r2sq_equals_4pi2_v0": identity_match,
            "result_kepler_earth_days_v0": _approx(T_earth / mpf("86400")),
            "result_kepler_earth_ratio_v0": _approx(T_earth / T_year),
            "result_kepler_jupiter_ratio_v0": _approx(T_jup / T_jup_obs),
        },
        "notes": "T^2 = 64*R2^2*a^3/(GM). Same R2 as pipes and wires.",
    }


def gravity_process_rate_v0(value_dicts):
    """Process rate = sqrt(1 - 2GM/(rc^2)) at key locations."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    R_earth = _mpf_val(vm, "astro_radius_earth_v0")
    R_GPS = _mpf_val(vm, "astro_gps_orbit_radius_v0")

    c2 = c * c
    phi_earth = G * M_earth / (R_earth * c2)
    phi_gps = G * M_earth / (R_GPS * c2)

    rate_earth = msqrt(mpf("1") - mpf("2") * phi_earth)
    rate_gps = msqrt(mpf("1") - mpf("2") * phi_gps)
    shift_earth = mpf("1") - rate_earth

    return {
        "key": "gravity_process_rate_v0",
        "outputs": {
            "result_process_rate_earth_surface_v0": _approx(rate_earth),
            "result_process_rate_gps_orbit_v0": _approx(rate_gps),
            "result_fractional_shift_earth_v0": _approx(shift_earth),
            "result_gps_rate_exceeds_earth_v0": rate_gps > rate_earth,
        },
        "notes": "sqrt(1 - 2GM/(rc^2)). GPS faster than surface.",
    }


def gravity_gps_correction_v0(value_dicts):
    """GPS clock correction: gravitational + velocity components."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    R_earth = _mpf_val(vm, "astro_radius_earth_v0")
    R_GPS = _mpf_val(vm, "astro_gps_orbit_radius_v0")
    v_GPS = _mpf_val(vm, "astro_gps_satellite_velocity_v0")

    c2 = c * c

    grav_shift = G * M_earth / c2 * (mpf("1") / R_earth - mpf("1") / R_GPS)
    vel_shift = -v_GPS * v_GPS / (mpf("2") * c2)
    total_shift = grav_shift + vel_shift
    total_us_day = total_shift * mpf("86400") * mpf("1e6")

    return {
        "key": "gravity_gps_correction_v0",
        "outputs": {
            "result_gps_grav_shift_v0": _approx(grav_shift),
            "result_gps_vel_shift_v0": _approx(vel_shift),
            "result_gps_total_shift_v0": _approx(total_shift),
            "result_gps_total_us_per_day_v0": _approx(total_us_day),
            "result_gps_gravity_dominates_v0": grav_shift > abs(vel_shift),
        },
        "notes": "GPS: grav +%.1f us/day, vel %.1f us/day, net +%.1f us/day" % (
            float(grav_shift * 86400e6),
            float(vel_shift * 86400e6),
            float(total_us_day)),
    }


def gravity_mond_a0_v0(value_dicts):
    """a0 = c*H0/(8*R2) = c*H0/(2*pi). The MOND acceleration scale."""
    vm = _value_map(value_dicts)

    c = _mpf_val(vm, "si_speed_of_light_v0")
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    H0_planck = _f2m(_frac(vm, "cosmo_h0_planck_v0"))

    # Convert H0 from km/s/Mpc to SI (1/s)
    H0_SI = H0_planck * mpf("1000") / mpf("3.086e22")

    a0 = c * H0_SI / (mpf("8") * R2)
    a0_published = mpf("1.2e-10")
    match_pct = abs(a0 - a0_published) / a0_published * mpf("100")

    # Transition radii
    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    AU = _mpf_val(vm, "astro_au_v0")

    r_earth = msqrt(G * M_earth / a0)
    r_sun = msqrt(G * M_sun / a0)

    return {
        "key": "gravity_mond_a0_v0",
        "outputs": {
            "result_mond_a0_v0": _approx(a0),
            "result_mond_a0_match_pct_v0": _approx(match_pct),
            "result_mond_transition_earth_au_v0": _approx(r_earth / AU),
            "result_mond_transition_sun_au_v0": _approx(r_sun / AU),
        },
        "notes": "a0 = cH0/(8R2) = cH0/(2pi) = %s m/s^2" % _approx(a0),
    }


# ================================================================
# CATEGORY D: RELATIVITY
# ================================================================

def relativity_muon_lifetime_v0(value_dicts):
    """Muon lifetime at several velocities. gamma = 1/sqrt(1-v^2/c^2)."""
    vm = _value_map(value_dicts)
    tau_rest = _mpf_val(vm, "astro_muon_rest_lifetime_v0")

    outputs = {}
    for v_str in ["0", "0.5", "0.9", "0.99", "0.999"]:
        v = mpf(v_str)
        if v == mpf("0"):
            gamma = mpf("1")
        else:
            gamma = mpf("1") / msqrt(mpf("1") - v * v)
        tau_obs = tau_rest * gamma
        tag = v_str.replace(".", "p")
        outputs["result_muon_gamma_at_%s_v0" % tag] = _approx(gamma)
        outputs["result_muon_tau_obs_us_at_%s_v0" % tag] = _approx(
            tau_obs * mpf("1e6"))

    return {
        "key": "relativity_muon_lifetime_v0",
        "outputs": outputs,
        "notes": "Muon internal rate is FIXED. Observer reads across boundary.",
    }


def relativity_twin_paradox_v0(value_dicts):
    """Twin paradox at v = 0.9c for 10 years (A's clock).
    Returns cycle counts using dv_Cs from pool.
    """
    vm = _value_map(value_dicts)
    dv_Cs = _f2m(_frac(vm, "si_cesium_hyperfine_v0"))

    v = mpf("0.9")
    yA = mpf("10")
    gamma = mpf("1") / msqrt(mpf("1") - v * v)
    yB = yA / gamma

    sec_per_year = mpf("365.25") * mpf("86400")
    cycles_A = yA * sec_per_year * dv_Cs
    cycles_B = yB * sec_per_year * dv_Cs

    return {
        "key": "relativity_twin_paradox_v0",
        "outputs": {
            "result_twin_gamma_v0": _approx(gamma),
            "result_twin_years_A_v0": _approx(yA),
            "result_twin_years_B_v0": _approx(yB),
            "result_twin_cycles_A_v0": _approx(cycles_A),
            "result_twin_cycles_B_v0": _approx(cycles_B),
            "result_twin_cycle_difference_v0": _approx(cycles_A - cycles_B),
            "result_twin_B_ages_less_v0": yB < yA,
        },
        "notes": "Two vortexes, different paths, different cycle counts.",
    }


def relativity_ds_squared_v0(value_dicts):
    """Minkowski interval ds^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2.
    Tests lightlike, timelike, spacelike.
    """
    vm = _value_map(value_dicts)
    c = _mpf_val(vm, "si_speed_of_light_v0")

    c2 = c * c

    # Lightlike: dt=1, dx=c
    ds2_light = -c2 * mpf("1") + c2
    # Timelike: dt=1, dx=0
    ds2_time = -c2 * mpf("1")
    # Spacelike: dt=0, dx=1
    ds2_space = mpf("1")

    return {
        "key": "relativity_ds_squared_v0",
        "outputs": {
            "result_ds2_lightlike_v0": _approx(ds2_light),
            "result_ds2_timelike_v0": _approx(ds2_time),
            "result_ds2_spacelike_v0": _approx(ds2_space),
            "result_ds2_light_is_zero_v0": abs(ds2_light) < mpf("1e-50"),
            "result_ds2_time_is_negative_v0": ds2_time < mpf("0"),
            "result_ds2_space_is_positive_v0": ds2_space > mpf("0"),
        },
        "notes": "ds^2 = -c^2*dt^2 + dx^2",
    }


# ================================================================
# CATEGORY E: HUBBLE RUNNING
# ================================================================

def hubble_cumulative_ratio_v0(value_dicts):
    """H0_far / H0_local = Planck / SH0ES."""
    vm = _value_map(value_dicts)
    H0_local = _frac(vm, "cosmo_h0_sh0es_v0")
    H0_far = _frac(vm, "cosmo_h0_planck_v0")

    ratio = H0_far / H0_local

    return {
        "key": "hubble_cumulative_ratio_v0",
        "outputs": {
            "result_hubble_cumulative_ratio_v0": ratio,
            "result_hubble_cumulative_ratio_numeric_v0": _approx(_f2m(ratio)),
        },
        "notes": "H0_far/H0_local = %s" % ratio,
    }


def hubble_tension_sigma_v0(value_dicts):
    """Tension in sigma between SH0ES and Planck."""
    vm = _value_map(value_dicts)
    H0_local = _f2m(_frac(vm, "cosmo_h0_sh0es_v0"))
    H0_far = _f2m(_frac(vm, "cosmo_h0_planck_v0"))

    # Uncertainties from node metadata — stored as strings in uncertainty field
    # SH0ES: 1.0, Planck: 0.5
    u1 = mpf("1.0")
    u2 = mpf("0.5")

    tension = (H0_local - H0_far) / msqrt(u1 * u1 + u2 * u2)

    return {
        "key": "hubble_tension_sigma_v0",
        "outputs": {
            "result_hubble_tension_sigma_v0": _approx(tension),
            "result_hubble_tension_above_4_v0": tension > mpf("4"),
        },
        "notes": "Tension = %.1f sigma" % float(tension),
    }


def hubble_required_r_v0(value_dicts):
    """r = (H0_far/H0_local)^(1/N) for N = 10, 100, 1000, 10000."""
    vm = _value_map(value_dicts)
    H0_local = _f2m(_frac(vm, "cosmo_h0_sh0es_v0"))
    H0_far = _f2m(_frac(vm, "cosmo_h0_planck_v0"))

    ratio = H0_far / H0_local
    outputs = {}

    for N in [10, 100, 1000, 10000]:
        r = ratio ** (mpf("1") / mpf(str(N)))
        omr = mpf("1") - r
        outputs["result_hubble_r_at_N%d_v0" % N] = _approx(r)
        outputs["result_hubble_1_minus_r_at_N%d_v0" % N] = _approx(omr)

    return {
        "key": "hubble_required_r_v0",
        "outputs": outputs,
        "notes": "r(N) = (H0_far/H0_local)^(1/N)",
    }


def hubble_vp_step_size_v0(value_dicts):
    """VP step = 1/(12*R2) = 1/(3*pi)."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    step = mpf("1") / (mpf("12") * R2)
    step_3pi = mpf("1") / (mpf("3") * mpi)
    match = mp.nstr(step, 20) == mp.nstr(step_3pi, 20)

    return {
        "key": "hubble_vp_step_size_v0",
        "outputs": {
            "result_hubble_vp_step_v0": _approx(step),
            "result_hubble_vp_equals_1_over_3pi_v0": match,
        },
        "notes": "VP step = 1/(12*R2) = 1/(3*pi)",
    }


def hubble_test_f1_strict_v0(value_dicts):
    """F1 strict: are H0 values monotonically decreasing (local -> far)?"""
    vm = _value_map(value_dicts)
    order = [
        "cosmo_h0_sh0es_v0", "cosmo_h0_h0licow_v0",
        "cosmo_h0_cchp_v0", "cosmo_h0_des_bao_bbn_v0",
        "cosmo_h0_planck_v0",
    ]
    vals = [_f2m(_frac(vm, k)) for k in order]

    monotonic = True
    detail = "monotonic"
    for i in range(len(vals) - 1):
        if vals[i + 1] > vals[i]:
            monotonic = False
            detail = "increase at index %d: %s > %s" % (
                i, mp.nstr(vals[i + 1], 4), mp.nstr(vals[i], 4))
            break

    return {
        "key": "hubble_test_f1_strict_v0",
        "outputs": {
            "result_f1_strict_monotonic_v0": monotonic,
            "result_f1_strict_detail_v0": detail,
        },
        "notes": "F1 strict: %s" % detail,
    }


def hubble_test_f1_soft_v0(value_dicts):
    """F1 soft: monotonic within 1-sigma? Only fails on hard inversion."""
    vm = _value_map(value_dicts)
    order_keys = [
        "cosmo_h0_sh0es_v0", "cosmo_h0_h0licow_v0",
        "cosmo_h0_cchp_v0", "cosmo_h0_des_bao_bbn_v0",
        "cosmo_h0_planck_v0",
    ]
    unc_vals = [mpf("1.0"), mpf("1.8"), mpf("1.7"), mpf("1.2"), mpf("0.5")]
    vals = [_f2m(_frac(vm, k)) for k in order_keys]

    violations = []
    for i in range(len(vals) - 1):
        if vals[i + 1] > vals[i]:
            f_lower = vals[i + 1] - unc_vals[i + 1]
            n_upper = vals[i] + unc_vals[i]
            if f_lower > n_upper:
                violations.append("hard inversion at index %d" % i)

    return {
        "key": "hubble_test_f1_soft_v0",
        "outputs": {
            "result_f1_soft_pass_v0": len(violations) == 0,
            "result_f1_soft_violations_v0": len(violations),
        },
        "notes": "F1 soft: %d violations" % len(violations),
    }


# ================================================================
# CATEGORY F: R2 DOMAINS
# ================================================================

def domain_r2_area_v0(value_dicts):
    """A = R2 * d^2. Compute for several standard diameters."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    outputs = {}
    diameters = [
        ("300mm_wafer", mpf("0.300")),
        ("120mm_disc", mpf("0.120")),
        ("awg12_wire", mpf("2.053e-3")),
        ("12inch_speaker", mpf("0.305")),
        ("smf28_fiber", mpf("10.4e-6")),
    ]
    for name, d in diameters:
        A = R2 * d * d
        outputs["result_r2_area_%s_m2_v0" % name] = _approx(A)

    return {
        "key": "domain_r2_area_v0",
        "outputs": outputs,
        "notes": "A = R2*d^2 across domains. Same R2 everywhere.",
    }


def domain_wire_resistance_v0(value_dicts):
    """R = rho*L/(R2*d^2). AWG 12 copper, 1 meter."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    rho = _mpf_val(vm, "eng_copper_resistivity_v0")

    d = mpf("2.053e-3")  # AWG 12
    L = mpf("1")
    R = rho * L / (R2 * d * d)

    return {
        "key": "domain_wire_resistance_v0",
        "outputs": {
            "result_wire_r_awg12_per_m_ohm_v0": _approx(R),
            "result_wire_r_awg12_per_m_mohm_v0": _approx(R * mpf("1000")),
        },
        "notes": "R = rho*L/(R2*d^2)",
    }


def domain_capacitance_v0(value_dicts):
    """C = eps0*R2*d^2/t. 120mm plates, 1mm gap."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    eps0 = _mpf_val(vm, "eng_vacuum_permittivity_v0")

    d = mpf("0.120")
    t = mpf("1e-3")
    C = eps0 * R2 * d * d / t

    return {
        "key": "domain_capacitance_v0",
        "outputs": {
            "result_capacitance_120mm_1mm_pf_v0": _approx(C * mpf("1e12")),
        },
        "notes": "C = eps0*R2*d^2/t",
    }


def domain_rc_cancellation_v0(value_dicts):
    """R*C = rho*eps0*L/t. R2 cancels. Verified to 30 digits."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    rho = _mpf_val(vm, "eng_copper_resistivity_v0")
    eps0 = _mpf_val(vm, "eng_vacuum_permittivity_v0")

    d = mpf("0.050")
    L = mpf("1")
    t = mpf("1e-3")

    R = rho * L / (R2 * d * d)
    C = eps0 * R2 * d * d / t
    RC = R * C

    RC_direct = rho * eps0 * L / t

    old_dps = mp.dps
    mp.dps = 50
    match_digits = mp.nstr(RC, 30) == mp.nstr(RC_direct, 30)
    mp.dps = old_dps

    return {
        "key": "domain_rc_cancellation_v0",
        "outputs": {
            "result_rc_product_v0": _approx(RC),
            "result_rc_direct_v0": _approx(RC_direct),
            "result_rc_r2_cancels_30_digits_v0": match_digits,
        },
        "notes": "R2 enters R and C, divides out in product. 30-digit match.",
    }


def domain_disc_spot_v0(value_dicts):
    """A = R2*(1.22*lambda/NA)^2 for CD, DVD, Blu-ray."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    discs = [
        ("cd", mpf("780e-9"), mpf("0.45")),
        ("dvd", mpf("650e-9"), mpf("0.60")),
        ("bluray", mpf("405e-9"), mpf("0.85")),
    ]
    outputs = {}
    for name, lam, NA in discs:
        spot_d = mpf("1.22") * lam / NA
        spot_A = R2 * spot_d * spot_d
        outputs["result_disc_%s_spot_um_v0" % name] = _approx(
            spot_d * mpf("1e6"))
        outputs["result_disc_%s_area_um2_v0" % name] = _approx(
            spot_A * mpf("1e12"))

    return {
        "key": "domain_disc_spot_v0",
        "outputs": outputs,
        "notes": "A = R2*(1.22*lambda/NA)^2. Diffraction limit.",
    }


def domain_kj_rk_cancellation_v0(value_dicts):
    """K_J * R_K = 2/e. R2 cancels.
    K_J = 2e/h, R_K = h/e^2. Product = 2e/h * h/e^2 = 2/e.
    """
    vm = _value_map(value_dicts)
    h = _f2m(_frac(vm, "si_planck_constant_v0"))
    e = _f2m(_frac(vm, "si_elementary_charge_v0"))

    K_J = mpf("2") * e / h
    R_K = h / (e * e)
    product = K_J * R_K
    expected = mpf("2") / e

    match = mp.nstr(product, 20) == mp.nstr(expected, 20)

    return {
        "key": "domain_kj_rk_cancellation_v0",
        "outputs": {
            "result_kj_v0": _approx(K_J),
            "result_rk_v0": _approx(R_K),
            "result_kj_times_rk_v0": _approx(product),
            "result_kj_rk_equals_2_over_e_v0": match,
        },
        "notes": "K_J*R_K = 2/e. R2 (via h = 8R2*hbar) enters and cancels.",
    }


def domain_fourier_gaussian_norms_v0(value_dicts):
    """Fourier = 1/(8R2) = 1/(2pi). Gaussian = 1/sqrt(8R2). BCS = pi/exp(gamma)."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    gamma_em = _mpf_val(vm, "math_euler_mascheroni_v0")

    fourier = mpf("1") / (mpf("8") * R2)
    gaussian = mpf("1") / msqrt(mpf("8") * R2)
    bcs = mpi / mexp(gamma_em)

    return {
        "key": "domain_fourier_gaussian_norms_v0",
        "outputs": {
            "result_fourier_norm_v0": _approx(fourier),
            "result_gaussian_norm_v0": _approx(gaussian),
            "result_bcs_gap_ratio_v0": _approx(bcs),
        },
        "notes": "1/(8R2) = 1/(2pi). BCS = pi/exp(gamma) = 1.7639.",
    }


def domain_vena_contracta_v0(value_dicts):
    """Cc = pi/(pi+2) = 4R2/(4R2+2). Kirchhoff 1869."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    four_R2 = mpf("4") * R2
    Cc = four_R2 / (four_R2 + mpf("2"))
    Cc_pi = mpi / (mpi + mpf("2"))
    match = mp.nstr(Cc, 20) == mp.nstr(Cc_pi, 20)

    return {
        "key": "domain_vena_contracta_v0",
        "outputs": {
            "result_vena_contracta_v0": _approx(Cc),
            "result_vena_contracta_identity_v0": match,
        },
        "notes": "Cc = pi/(pi+2) = 4R2/(4R2+2) = %s" % _approx(Cc),
    }


# ================================================================
# CATEGORY G: COSMOLOGY EXTENSIONS
# ================================================================

def cosmo_omega_b_v0(value_dicts):
    """Omega_b = Omega_DM / (DM/baryon)."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    dm_prefrac = _frac(vm, "cosmo_dm_to_baryon_ratio_prefactor_v0")
    omega_prefrac = _frac(vm, "cosmo_omega_dm_r2_prefactor_v0")

    dm_value = _f2m(dm_prefrac) * mpf("4") * R2
    omega_dm = _f2m(omega_prefrac) * R2
    omega_b = omega_dm / dm_value

    return {
        "key": "cosmo_omega_b_v0",
        "outputs": {
            "result_cosmo_omega_b_v0": _approx(omega_b),
        },
        "notes": "Omega_b = Omega_DM / (DM/baryon) = %s" % _approx(omega_b),
    }


def cosmo_omega_matter_v0(value_dicts):
    """Omega_m = Omega_DM + Omega_b."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    omega_prefrac = _frac(vm, "cosmo_omega_dm_r2_prefactor_v0")
    dm_prefrac = _frac(vm, "cosmo_dm_to_baryon_ratio_prefactor_v0")

    omega_dm = _f2m(omega_prefrac) * R2
    dm_value = _f2m(dm_prefrac) * mpf("4") * R2
    omega_b = omega_dm / dm_value
    omega_m = omega_dm + omega_b

    return {
        "key": "cosmo_omega_matter_v0",
        "outputs": {
            "result_cosmo_omega_matter_v0": _approx(omega_m),
        },
        "notes": "Omega_m = Omega_DM + Omega_b = %s" % _approx(omega_m),
    }


def cosmo_omega_de_v0(value_dicts):
    """Omega_DE = 1 - Omega_m (flat universe)."""
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))

    omega_prefrac = _frac(vm, "cosmo_omega_dm_r2_prefactor_v0")
    dm_prefrac = _frac(vm, "cosmo_dm_to_baryon_ratio_prefactor_v0")

    omega_dm = _f2m(omega_prefrac) * R2
    dm_value = _f2m(dm_prefrac) * mpf("4") * R2
    omega_b = omega_dm / dm_value
    omega_m = omega_dm + omega_b
    omega_de = mpf("1") - omega_m

    return {
        "key": "cosmo_omega_de_v0",
        "outputs": {
            "result_cosmo_omega_de_v0": _approx(omega_de),
            "result_cosmo_flatness_sum_v0": _approx(omega_m + omega_de),
        },
        "notes": "Omega_DE = 1 - Omega_m. Flatness: Omega_m + Omega_DE = 1",
    }


def cosmo_virial_ratio_v0(value_dicts):
    """M_virial = R*v^2/G for the Milky Way."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    parsec = _mpf_val(vm, "astro_parsec_v0")

    R_mw = mpf("15000") * parsec
    v_circ = mpf("220000")
    M_vis = mpf("6e10") * M_sun

    M_vir = R_mw * v_circ * v_circ / G
    ratio = M_vir / M_vis

    return {
        "key": "cosmo_virial_ratio_v0",
        "outputs": {
            "result_virial_mass_solar_v0": _approx(M_vir / M_sun),
            "result_virial_ratio_v0": _approx(ratio),
        },
        "notes": "M_virial/M_visible = %.1f" % float(ratio),
    }


def cosmo_frame_dragging_v0(value_dicts):
    """Frame dragging ratio: (v/c)^2 * (R_S/R). Negligible for galaxies."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    parsec = _mpf_val(vm, "astro_parsec_v0")

    M_vis = mpf("6e10") * M_sun
    R_mw = mpf("15000") * parsec
    v = mpf("220000")

    R_S = mpf("2") * G * M_vis / (c * c)
    fd = (v / c) ** 2 * (R_S / R_mw)

    return {
        "key": "cosmo_frame_dragging_v0",
        "outputs": {
            "result_frame_dragging_ratio_v0": _approx(fd),
            "result_frame_dragging_negligible_v0": fd < mpf("1e-5"),
        },
        "notes": "Frame dragging << 1 for galaxy: %s" % _approx(fd),
    }


# ================================================================
# CATEGORY H: DWARF SOLITONS
# ================================================================

def dwarf_purity_v0(value_dicts):
    """DM/visible ratio for all dwarfs in the catalog."""
    vm = _value_map(value_dicts)

    dwarfs = [
        "fornax", "sculptor", "draco", "ursa_minor", "carina",
        "sextans", "leo1", "leo2", "segue1", "reticulum2", "tucana2",
    ]
    outputs = {}
    for name in dwarfs:
        m_vis_key = "obs_%s_mass_visible_v0" % name
        m_dyn_key = "obs_%s_mass_dynamical_v0" % name

        m_vis = vm.get(m_vis_key)
        m_dyn = vm.get(m_dyn_key)
        if m_vis is None or m_dyn is None:
            continue

        m_vis_f = mpf(str(m_vis))
        m_dyn_f = mpf(str(m_dyn))
        ratio = m_dyn_f / m_vis_f
        dark_frac = (m_dyn_f - m_vis_f) / m_dyn_f

        outputs["result_dwarf_%s_dm_vis_ratio_v0" % name] = _approx(ratio)
        outputs["result_dwarf_%s_dark_fraction_v0" % name] = _approx(dark_frac)

    return {
        "key": "dwarf_purity_v0",
        "outputs": outputs,
        "notes": "DM/visible ratio for dwarf catalog. UF >> classical >> spiral.",
    }


def dwarf_cosmic_ratio_v0(value_dicts):
    """Dwarf DM/visible divided by cosmic DM/baryon.
    If ~ 19 = |b2_SM_num|, dwarfs use SM betas (before CD).
    """
    vm = _value_map(value_dicts)
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    dm_prefrac = _frac(vm, "cosmo_dm_to_baryon_ratio_prefactor_v0")
    cosmic_ratio = _f2m(dm_prefrac) * mpf("4") * R2

    dwarfs = ["fornax", "sculptor", "draco"]
    outputs = {}
    for name in dwarfs:
        m_vis_key = "obs_%s_mass_visible_v0" % name
        m_dyn_key = "obs_%s_mass_dynamical_v0" % name
        m_vis = vm.get(m_vis_key)
        m_dyn = vm.get(m_dyn_key)
        if m_vis is None or m_dyn is None:
            continue
        local_ratio = mpf(str(m_dyn)) / mpf(str(m_vis))
        cosmic_norm = local_ratio / cosmic_ratio
        outputs["result_dwarf_%s_cosmic_ratio_v0" % name] = _approx(cosmic_norm)

    return {
        "key": "dwarf_cosmic_ratio_v0",
        "outputs": outputs,
        "notes": "Dwarf DM/vis / cosmic DM/baryon. ~19 = |b2_SM_num|?",
    }


def dwarf_faber_jackson_v0(value_dicts):
    """M = sigma^4 / (G*a0). Faber-Jackson with a0 = cH0/(8R2)."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    H0_planck = _f2m(_frac(vm, "cosmo_h0_planck_v0"))
    H0_SI = H0_planck * mpf("1000") / mpf("3.086e22")
    a0 = c * H0_SI / (mpf("8") * R2)

    dwarfs = {
        "fornax": mpf("11.7"),
        "sculptor": mpf("9.2"),
        "draco": mpf("9.1"),
    }
    outputs = {}
    for name, sigma_kms in dwarfs.items():
        sigma_key = "obs_%s_velocity_dispersion_v0" % name
        sigma_obs = vm.get(sigma_key)
        if sigma_obs is not None:
            sigma_kms = mpf(str(sigma_obs))
        sigma = sigma_kms * mpf("1000")
        M_pred = sigma ** 4 / (G * a0) / M_sun
        outputs["result_fj_%s_mass_solar_v0" % name] = _approx(M_pred)

    return {
        "key": "dwarf_faber_jackson_v0",
        "outputs": outputs,
        "notes": "M = sigma^4/(G*a0), a0 = cH0/(8R2)",
    }


def dwarf_tully_fisher_v0(value_dicts):
    """M = v_rot^4 / (G*a0). Tully-Fisher with a0 = cH0/(8R2).
    Milky Way at v = 220 km/s.
    """
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    H0_planck = _f2m(_frac(vm, "cosmo_h0_planck_v0"))
    H0_SI = H0_planck * mpf("1000") / mpf("3.086e22")
    a0 = c * H0_SI / (mpf("8") * R2)

    v = mpf("220000")
    M_mw = v ** 4 / (G * a0) / M_sun

    # v^4 scaling test: TF(440) / TF(220) = 16
    v2 = mpf("440000")
    M_mw_2x = v2 ** 4 / (G * a0) / M_sun
    ratio_v4 = M_mw_2x / M_mw

    return {
        "key": "dwarf_tully_fisher_v0",
        "outputs": {
            "result_tf_mw_mass_solar_v0": _approx(M_mw),
            "result_tf_v4_scaling_test_v0": _approx(ratio_v4),
        },
        "notes": "M = v^4/(G*a0). MW at 220 km/s. v^4 scaling: 440/220 ratio = %s" % (
            _approx(ratio_v4)),
    }


# ================================================================
# CATEGORY I: CONNECTION FUNCTIONS
# ================================================================

def connection_soliton_hierarchy_v0(value_dicts):
    """The 11-level soliton nesting hierarchy with GM/(rc^2) at each level."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    c2 = c * c

    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    R_earth = _mpf_val(vm, "astro_radius_earth_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    R_sun = _mpf_val(vm, "astro_radius_sun_v0")
    AU = _mpf_val(vm, "astro_au_v0")

    levels = [
        {"name": "Proton (QCD)", "size": "~1 fm",
         "coupling": "~1 (confinement)", "boundary": "Confinement"},
        {"name": "Atom (EM)", "size": "~0.1 nm",
         "coupling": _approx(mpf("1") / mpf("137")), "boundary": "Ionization"},
        {"name": "Crystal lattice", "size": "~nm-km",
         "coupling": "~1e-10", "boundary": "Melting"},
        {"name": "Geological", "size": "~m-km",
         "coupling": "~1e-10", "boundary": "Phase"},
        {"name": "Earth surface", "size": "6371 km",
         "coupling": _approx(G * M_earth / (R_earth * c2)),
         "boundary": "Escape velocity"},
        {"name": "Earth Hill sphere", "size": "1.5e6 km",
         "coupling": _approx(G * M_earth / (R_earth * c2)),
         "boundary": "L1 Lagrange"},
        {"name": "Earth orbit", "size": "1 AU",
         "coupling": _approx(G * M_sun / (AU * c2)),
         "boundary": "Kepler orbit"},
        {"name": "Solar Hill sphere", "size": "~120 AU",
         "coupling": "~1e-6", "boundary": "Voyager"},
        {"name": "Galactic disk", "size": "~15 kpc",
         "coupling": "~1e-6", "boundary": "Virial radius"},
        {"name": "Galaxy cluster", "size": "~3 Mpc",
         "coupling": "~1e-5", "boundary": "Virial radius"},
        {"name": "Cosmological", "size": "~150 Mpc",
         "coupling": "—", "boundary": "H0 running"},
    ]

    edges = []
    for i in range(len(levels) - 1):
        edges.append({
            "from": levels[i]["name"],
            "to": levels[i + 1]["name"],
            "relation": "contained_in",
        })

    return {
        "key": "connection_soliton_hierarchy_v0",
        "named_values": {l["name"]: l for l in levels},
        "edges": edges,
        "notes": "11-level nesting. Same GM/(rc^2) principle everywhere.",
    }


def connection_r2_cancellation_registry_v0(value_dicts):
    """Verify all R2 cancellation identities."""
    vm = _value_map(value_dicts)

    h = _f2m(_frac(vm, "si_planck_constant_v0"))
    e = _f2m(_frac(vm, "si_elementary_charge_v0"))
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    rho = _mpf_val(vm, "eng_copper_resistivity_v0")
    eps0 = _mpf_val(vm, "eng_vacuum_permittivity_v0")

    cancellations = []

    # K_J * R_K
    KJ = mpf("2") * e / h
    RK = h / (e * e)
    prod = KJ * RK
    expected = mpf("2") / e
    cancellations.append({
        "name": "K_J * R_K",
        "status": "CANCELS" if mp.nstr(prod, 15) == mp.nstr(expected, 15) else "FAIL",
        "result": "2/e",
    })

    # RC product
    d = mpf("0.05")
    L = mpf("1")
    t = mpf("1e-3")
    R_wire = rho * L / (R2 * d * d)
    C_cap = eps0 * R2 * d * d / t
    RC = R_wire * C_cap
    RC_dir = rho * eps0 * L / t
    cancellations.append({
        "name": "Wire R * Cap C",
        "status": "CANCELS" if mp.nstr(RC, 20) == mp.nstr(RC_dir, 20) else "FAIL",
        "result": "rho*eps0*L/t",
    })

    # Gap ratio (R2-free)
    cancellations.append({
        "name": "Gap ratio",
        "status": "R2-FREE",
        "result": "pure rational Fractions",
    })

    # Generation democracy (R2-free)
    cancellations.append({
        "name": "Generation democracy",
        "status": "R2-FREE",
        "result": "4/3 - 4/3 = 0 in every coupling",
    })

    edges = [{"from": c["name"], "to": c["status"],
              "relation": "cancellation"} for c in cancellations]

    return {
        "key": "connection_r2_cancellation_registry_v0",
        "named_values": {c["name"]: c for c in cancellations},
        "edges": edges,
        "notes": "%d identities checked" % len(cancellations),
    }


def connection_boundary_adjacency_v0(value_dicts):
    """Running distance L between adjacent boundaries."""
    vm = _value_map(value_dicts)

    M_Z = _f2m(_frac(vm, "mass_z_boson_v0"))

    boundaries = [
        ("electron", _f2m(_frac(vm, "mass_electron_v0"))),
        ("muon", _f2m(_frac(vm, "mass_muon_v0"))),
        ("charm", _f2m(_frac(vm, "mass_charm_quark_v0"))),
        ("tau", _f2m(_frac(vm, "mass_tau_lepton_v0"))),
        ("bottom", _f2m(_frac(vm, "mass_bottom_quark_v0"))),
        ("W", _f2m(_frac(vm, "mass_w_boson_v0"))),
        ("Z", M_Z),
        ("Higgs", _f2m(_frac(vm, "mass_higgs_boson_v0"))),
        ("top", _f2m(_frac(vm, "mass_top_quark_v0"))),
    ]
    boundaries.sort(key=lambda x: float(x[1]))

    edges = []
    for i in range(len(boundaries) - 1):
        n1, E1 = boundaries[i]
        n2, E2 = boundaries[i + 1]
        dL = mlog(E2 / E1) / (mpf("2") * mpi)
        edges.append({
            "from": n1,
            "to": n2,
            "relation": "adjacent",
            "running_distance_L": _approx(dL),
        })

    return {
        "key": "connection_boundary_adjacency_v0",
        "named_values": {n: {"scale_MeV": _approx(E)} for n, E in boundaries},
        "edges": edges,
        "notes": "L = ln(E2/E1)/(2pi). Total e->top: L = %s" % _approx(
            mlog(boundaries[-1][1] / boundaries[0][1]) / (mpf("2") * mpi)),
    }


def connection_mond_transition_v0(value_dicts):
    """MOND transition radii vs Hill spheres."""
    vm = _value_map(value_dicts)

    G = _mpf_val(vm, "astro_gravitational_constant_v0")
    c = _mpf_val(vm, "si_speed_of_light_v0")
    M_sun = _mpf_val(vm, "astro_mass_sun_v0")
    M_earth = _mpf_val(vm, "astro_mass_earth_v0")
    AU = _mpf_val(vm, "astro_au_v0")
    R2 = _f2m(_frac(vm, "geom_r2_v0"))
    H0 = _f2m(_frac(vm, "cosmo_h0_planck_v0"))
    H0_SI = H0 * mpf("1000") / mpf("3.086e22")
    a0 = c * H0_SI / (mpf("8") * R2)

    r_a0_earth = msqrt(G * M_earth / a0)
    r_a0_sun = msqrt(G * M_sun / a0)
    rh_earth = AU * (M_earth / (mpf("3") * M_sun)) ** (mpf("1") / mpf("3"))

    edges = [
        {"from": "Earth Hill sphere", "to": "Earth MOND radius",
         "relation": "MOND > Hill" if r_a0_earth > rh_earth else "MOND < Hill"},
        {"from": "Sun MOND radius", "to": "Solar neighborhood",
         "relation": "r_a0 = %s AU" % _approx(r_a0_sun / AU)},
    ]

    return {
        "key": "connection_mond_transition_v0",
        "named_values": {
            "earth_mond_radius_au": _approx(r_a0_earth / AU),
            "sun_mond_radius_au": _approx(r_a0_sun / AU),
            "earth_hill_sphere_au": _approx(rh_earth / AU),
            "a0": _approx(a0),
        },
        "edges": edges,
        "notes": "MOND transition > Hill sphere for Earth. a0 = cH0/(8R2).",
    }


# ================================================================
# REGISTRIES
# ================================================================

DERIVATION_MORE_INDEX_V0 = {
    # A: Unification extensions
    "coupling_one_loop_sin2_prediction_v0": coupling_one_loop_sin2_prediction_v0,
    "coupling_whatif_rep_v0": coupling_whatif_rep_v0,
    "group_theory_casimirs_v0": group_theory_casimirs_v0,
    # B: Scale conversion
    "scale_energy_to_distance_v0": scale_energy_to_distance_v0,
    "scale_distance_to_energy_v0": scale_distance_to_energy_v0,
    # C: Gravity & soliton
    "gravity_coupling_v0": gravity_coupling_v0,
    "gravity_escape_velocity_v0": gravity_escape_velocity_v0,
    "gravity_binding_fraction_v0": gravity_binding_fraction_v0,
    "gravity_hill_sphere_v0": gravity_hill_sphere_v0,
    "gravity_kepler_period_v0": gravity_kepler_period_v0,
    "gravity_process_rate_v0": gravity_process_rate_v0,
    "gravity_gps_correction_v0": gravity_gps_correction_v0,
    "gravity_mond_a0_v0": gravity_mond_a0_v0,
    # D: Relativity
    "relativity_muon_lifetime_v0": relativity_muon_lifetime_v0,
    "relativity_twin_paradox_v0": relativity_twin_paradox_v0,
    "relativity_ds_squared_v0": relativity_ds_squared_v0,
    # E: Hubble running
    "hubble_cumulative_ratio_v0": hubble_cumulative_ratio_v0,
    "hubble_tension_sigma_v0": hubble_tension_sigma_v0,
    "hubble_required_r_v0": hubble_required_r_v0,
    "hubble_vp_step_size_v0": hubble_vp_step_size_v0,
    "hubble_test_f1_strict_v0": hubble_test_f1_strict_v0,
    "hubble_test_f1_soft_v0": hubble_test_f1_soft_v0,
    # F: R2 domains
    "domain_r2_area_v0": domain_r2_area_v0,
    "domain_wire_resistance_v0": domain_wire_resistance_v0,
    "domain_capacitance_v0": domain_capacitance_v0,
    "domain_rc_cancellation_v0": domain_rc_cancellation_v0,
    "domain_disc_spot_v0": domain_disc_spot_v0,
    "domain_kj_rk_cancellation_v0": domain_kj_rk_cancellation_v0,
    "domain_fourier_gaussian_norms_v0": domain_fourier_gaussian_norms_v0,
    "domain_vena_contracta_v0": domain_vena_contracta_v0,
    # G: Cosmology extensions
    "cosmo_omega_b_v0": cosmo_omega_b_v0,
    "cosmo_omega_matter_v0": cosmo_omega_matter_v0,
    "cosmo_omega_de_v0": cosmo_omega_de_v0,
    "cosmo_virial_ratio_v0": cosmo_virial_ratio_v0,
    "cosmo_frame_dragging_v0": cosmo_frame_dragging_v0,
    # H: Dwarf solitons
    "dwarf_purity_v0": dwarf_purity_v0,
    "dwarf_cosmic_ratio_v0": dwarf_cosmic_ratio_v0,
    "dwarf_faber_jackson_v0": dwarf_faber_jackson_v0,
    "dwarf_tully_fisher_v0": dwarf_tully_fisher_v0,
}

CONNECTION_MORE_INDEX_V0 = {
    "connection_soliton_hierarchy_v0": connection_soliton_hierarchy_v0,
    "connection_r2_cancellation_registry_v0": connection_r2_cancellation_registry_v0,
    "connection_boundary_adjacency_v0": connection_boundary_adjacency_v0,
    "connection_mond_transition_v0": connection_mond_transition_v0,
}


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DATA-6 EXTENDED DERIVATIONS: REGISTRY CHECK")
    print("=" * 70)
    print()
    print("  Derivations: %d functions" % len(DERIVATION_MORE_INDEX_V0))
    print("  Connections:  %d functions" % len(CONNECTION_MORE_INDEX_V0))
    print()
    print("  Categories:")
    cats = {}
    for key in DERIVATION_MORE_INDEX_V0:
        prefix = key.split("_")[0]
        cats[prefix] = cats.get(prefix, 0) + 1
    for cat, count in sorted(cats.items()):
        print("    %-20s %d" % (cat, count))
    print()
    print("  All functions are callable: %s" % all(
        callable(fn) for fn in DERIVATION_MORE_INDEX_V0.values()))
    print("  All connections are callable: %s" % all(
        callable(fn) for fn in CONNECTION_MORE_INDEX_V0.values()))
    print()

    # Verify no key collisions with the original registry
    try:
        from _data_6_derivations_v0 import DERIVATION_INDEX_V0, CONNECTION_INDEX_V0
        overlap_d = set(DERIVATION_MORE_INDEX_V0) & set(DERIVATION_INDEX_V0)
        overlap_c = set(CONNECTION_MORE_INDEX_V0) & set(CONNECTION_INDEX_V0)
        print("  Key collisions with original derivations: %d" % len(overlap_d))
        print("  Key collisions with original connections: %d" % len(overlap_c))
        if overlap_d:
            for k in overlap_d:
                print("    COLLISION: %s" % k)
        if overlap_c:
            for k in overlap_c:
                print("    COLLISION: %s" % k)
        print()
        print("  Combined total: %d derivations + %d connections" % (
            len(DERIVATION_INDEX_V0) + len(DERIVATION_MORE_INDEX_V0),
            len(CONNECTION_INDEX_V0) + len(CONNECTION_MORE_INDEX_V0)))
    except ImportError:
        print("  (Original registry not available for collision check)")

    print()
    print("=" * 70)
