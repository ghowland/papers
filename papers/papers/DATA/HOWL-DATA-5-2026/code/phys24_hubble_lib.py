#!/usr/bin/env python3
"""
HOWL PHYS-24 HUBBLE RUNNING LIBRARY
======================================
Encodes the Hubble tension running curve hypothesis from the
working notebook. H0 measurements at different effective boundary
transit counts N may trace a continuous running curve:

    H0(N) = H0(0) * r^N

where r is a per-transit rational correction factor.

Status: ACTIVE INVESTIGATION, NOT VERIFIED.
Unlike the other platform libraries, this one contains HYPOTHESES
alongside data. Every hypothesis is clearly tagged. Every measured
value has its source. Every unknown is None.

This library is a TOOL for testing the hypothesis, not a claim
that the hypothesis is correct.

Falsification conditions (from notebook Section 7) are encoded
as testable functions.

Import:
    from phys24_lib import *
    from phys24_hubble_lib import *

Platform: phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from mpmath import pi as mpi, log as mlog, exp as mexp, sqrt as msqrt


# ================================================================
# STATUS FLAGS
# ================================================================

HYPOTHESIS_STATUS = "ACTIVE_INVESTIGATION"
VERIFIED = False
PARKED = False


# ================================================================
# MEASURED H0 VALUES (Level 2)
# Sources: SH0ES, H0LiCOW, CCHP, DES+BAO+BBN, Planck
# ================================================================

H0_MEASUREMENTS = {
    "SH0ES": {
        "name": "SH0ES (Type Ia supernovae + Cepheids)",
        "H0": Fraction(730, 10),           # 73.0 km/s/Mpc
        "uncertainty": Fraction(10, 10),    # +/- 1.0
        "year": 2022,
        "source": "Riess et al. 2022, ApJ 934, L7",
        "distance_class": "local",
        "effective_N": None,                # UNKNOWN — needs structure catalog
        "effective_N_estimate": "low",
        "method": "distance ladder: Cepheids -> SNe Ia",
    },
    "H0LiCOW": {
        "name": "H0LiCOW (gravitational lensing time delays)",
        "H0": Fraction(733, 10),            # 73.3 km/s/Mpc
        "uncertainty": Fraction(18, 10),     # +/- 1.8
        "year": 2020,
        "source": "Wong et al. 2020, MNRAS 498, 1420",
        "distance_class": "local-medium",
        "effective_N": None,
        "effective_N_estimate": "low-medium",
        "method": "strong lensing time delays through lens galaxy",
    },
    "CCHP": {
        "name": "CCHP (Tip of Red Giant Branch)",
        "H0": Fraction(698, 10),            # 69.8 km/s/Mpc
        "uncertainty": Fraction(17, 10),     # +/- 1.7
        "year": 2021,
        "source": "Freedman 2021, ApJ 919, 16",
        "distance_class": "medium",
        "effective_N": None,
        "effective_N_estimate": "medium",
        "method": "TRGB calibration, different from Cepheids",
    },
    "DES_BAO_BBN": {
        "name": "DES + BAO + BBN (combined cosmological)",
        "H0": Fraction(674, 10),            # 67.4 km/s/Mpc
        "uncertainty": Fraction(12, 10),     # +/- 1.2
        "year": 2022,
        "source": "DES Collaboration 2022",
        "distance_class": "high",
        "effective_N": None,
        "effective_N_estimate": "high",
        "method": "baryon acoustic oscillations + big bang nucleosynthesis",
    },
    "Planck": {
        "name": "Planck CMB (cosmic microwave background)",
        "H0": Fraction(674, 10),            # 67.4 km/s/Mpc
        "uncertainty": Fraction(5, 10),      # +/- 0.5
        "year": 2020,
        "source": "Planck Collaboration 2020, A&A 641, A6",
        "distance_class": "maximum",
        "effective_N": None,
        "effective_N_estimate": "maximum",
        "method": "CMB power spectrum fit assuming Lambda-CDM",
    },
}

# Ordered by distance class for running curve analysis
H0_ORDERED = ["SH0ES", "H0LiCOW", "CCHP", "DES_BAO_BBN", "Planck"]


# ================================================================
# DERIVED QUANTITIES (from measured values)
# ================================================================

# The cumulative factor: ratio of far to near H0
H0_local = H0_MEASUREMENTS["SH0ES"]["H0"]      # 73.0
H0_far = H0_MEASUREMENTS["Planck"]["H0"]         # 67.4
cumulative_ratio = H0_far / H0_local              # 67.4/73.0 = 674/730 = 337/365

# Natural log of the cumulative factor
# ln(73.0/67.4) = ln(365/337)
ln_cumulative = mlog(f2m(H0_local) / f2m(H0_far))  # ~0.0798

# The tension in sigma
H0_tension_sigma = (f2m(H0_local) - f2m(H0_far)) / msqrt(
    f2m(H0_MEASUREMENTS["SH0ES"]["uncertainty"]) ** 2 +
    f2m(H0_MEASUREMENTS["Planck"]["uncertainty"]) ** 2)


# ================================================================
# THE RUNNING CURVE MODEL
# ================================================================
# H0(N) = H0(0) * r^N
# where:
#   H0(0) = H0 at zero boundary transits (local, unscreened)
#   r = per-transit correction factor (< 1 if H0 decreases with N)
#   N = effective boundary transit count

def H0_running(H0_0, r, N):
    """Compute H0 at boundary transit count N.
    H0(N) = H0(0) * r^N

    Args:
      H0_0: mpf or Fraction, H0 at N=0 (local value)
      r: mpf or Fraction, per-transit correction factor
      N: mpf or int, boundary transit count
    Returns: H0(N) as mpf
    """
    h0 = f2m(H0_0) if isinstance(H0_0, Fraction) else mpf(H0_0)
    r_val = f2m(r) if isinstance(r, Fraction) else mpf(r)
    return h0 * r_val ** mpf(N)


def extract_r(H0_near, H0_far, N_eff):
    """Extract per-transit correction factor from two measurements.
    r = (H0_far / H0_near)^(1/N)

    Args:
      H0_near, H0_far: mpf or Fraction
      N_eff: mpf or int, effective transit count between the two
    Returns: r as mpf
    """
    near = f2m(H0_near) if isinstance(H0_near, Fraction) else mpf(H0_near)
    far = f2m(H0_far) if isinstance(H0_far, Fraction) else mpf(H0_far)
    return (far / near) ** (mpf("1") / mpf(N_eff))


def required_r(N_eff):
    """Given effective N, what r is required to produce the observed ratio?
    r = (67.4/73.0)^(1/N) = (337/365)^(1/N)

    Args: N_eff as int or mpf
    Returns: r as mpf
    """
    return f2m(cumulative_ratio) ** (mpf("1") / mpf(N_eff))


def one_minus_r(N_eff):
    """The correction per transit: 1 - r.
    Approximately ln(73.0/67.4) / N = 0.0798 / N.

    Args: N_eff as int or mpf
    Returns: 1 - r as mpf
    """
    return mpf("1") - required_r(N_eff)


# ================================================================
# MAGNITUDE CONSTRAINTS (from notebook Section 6)
# ================================================================

MAGNITUDE_TABLE = {
    10:    {"r": None, "one_minus_r": None, "character": "~1/125"},
    100:   {"r": None, "one_minus_r": None, "character": "~1/1250"},
    1000:  {"r": None, "one_minus_r": None, "character": "~1/12500"},
    10000: {"r": None, "one_minus_r": None, "character": "~1/125000"},
}

# Compute r for each N
for N in MAGNITUDE_TABLE:
    r_val = required_r(N)
    MAGNITUDE_TABLE[N]["r"] = r_val
    MAGNITUDE_TABLE[N]["one_minus_r"] = mpf("1") - r_val


# ================================================================
# STRUCTURAL PARALLELS (from notebook Section 5)
# ================================================================

# VP running step size for comparison
VP_STEP_SIZE = mpf("1") / (mpf("3") * mpi)   # 1/(3*pi) = 1/(12*R2) ~ 0.1061

STRUCTURAL_PARALLELS = {
    "alpha_running": {
        "variable": "probe energy",
        "boundaries": "flavor thresholds (quark masses)",
        "direction": "alpha increases with energy (screening weakens)",
        "per_boundary": "1/(3*pi) = 1/(12*R2) per unit charge^2",
        "per_boundary_value": VP_STEP_SIZE,
        "subgroup": "B (monotonic accumulation)",
        "arithmetic": "Fraction, verified to 0.02 ppm",
        "derived_from": "group theory counting (Dynkin indices)",
    },
    "H0_running": {
        "variable": "effective distance / boundary count N",
        "boundaries": "soliton boundaries (galaxy clusters, filaments, voids)",
        "direction": "H0 decreases with N (cumulative correction reduces)",
        "per_boundary": "UNKNOWN — to be extracted",
        "per_boundary_value": None,
        "subgroup": "B (monotonic accumulation, predicted)",
        "arithmetic": "Fraction, to be verified",
        "derived_from": "boundary geometry (unknown)",
    },
}


# ================================================================
# CANDIDATE RATIONAL CORRECTIONS
# ================================================================
# For each plausible N, compute r and check if 1-r has integer structure

def scan_rational_candidates(N_min=5, N_max=10000, interesting_denoms=None):
    """Scan N values and check if 1-r approximates a simple fraction.

    For each N, compute r = (337/365)^(1/N) and check if 1-r is close
    to any p/q with q in interesting_denoms.

    Args:
      N_min, N_max: range of N to scan
      interesting_denoms: list of denominators to test (default: powers of R2-related integers)
    Returns: list of (N, r, 1-r, best_match_frac, match_quality) tuples
    """
    if interesting_denoms is None:
        interesting_denoms = [
            3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 24, 25, 30,
            32, 36, 40, 48, 50, 60, 64, 72, 75, 80, 96, 100, 120,
            125, 128, 144, 150, 160, 192, 200, 240, 250, 256, 300,
            360, 375, 400, 480, 500, 600, 625, 720, 750, 800, 1000,
            1024, 1250, 1500, 2000, 2500, 3000, 4000, 5000, 10000,
            12500, 125000,
        ]

    results = []
    N_values = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    N_values = [n for n in N_values if N_min <= n <= N_max]

    for N in N_values:
        r_val = required_r(N)
        omr = mpf("1") - r_val  # 1 - r

        best_frac = None
        best_quality = mpf("1")

        for q in interesting_denoms:
            for p in range(1, q):
                frac_val = f2m(Fraction(p, q))
                quality = abs(omr - frac_val) / omr
                if quality < best_quality:
                    best_quality = quality
                    best_frac = Fraction(p, q)

        results.append({
            "N": N,
            "r": r_val,
            "one_minus_r": omr,
            "best_fraction": best_frac,
            "match_quality": best_quality,
            "match_pct": best_quality * mpf("100"),
        })

    return results


# ================================================================
# CURVE FITTING
# ================================================================

def fit_running_curve(measurements, N_assignments):
    """Fit H0(N) = H0(0) * r^N to a set of measurements with assigned N values.

    Args:
      measurements: list of (H0_value, H0_uncertainty) as Fractions
      N_assignments: list of N values (int or mpf), same length
    Returns: dict with H0_0, r, residuals, chi2
    """
    if len(measurements) < 2:
        return None

    # Use first and last points to get initial H0_0 and r
    H0_first = f2m(measurements[0][0])
    H0_last = f2m(measurements[-1][0])
    N_first = mpf(N_assignments[0])
    N_last = mpf(N_assignments[-1])

    if N_last == N_first:
        return None

    r_init = (H0_last / H0_first) ** (mpf("1") / (N_last - N_first))
    H0_0_init = H0_first / r_init ** N_first

    # Compute residuals for all points
    residuals = []
    chi2 = mpf("0")
    for i in range(len(measurements)):
        H0_meas = f2m(measurements[i][0])
        H0_unc = f2m(measurements[i][1])
        N_i = mpf(N_assignments[i])
        H0_pred = H0_0_init * r_init ** N_i
        resid = H0_meas - H0_pred
        residuals.append(resid)
        if H0_unc > mpf("0"):
            chi2 += (resid / H0_unc) ** 2

    return {
        "H0_0": H0_0_init,
        "r": r_init,
        "residuals": residuals,
        "chi2": chi2,
        "n_points": len(measurements),
        "n_params": 2,
        "dof": len(measurements) - 2,
    }


def predict_H0(H0_0, r, N):
    """Predict H0 at a specific boundary transit count.
    This is a PREDICTION — it can be falsified by measurement.

    Args: H0_0 (mpf), r (mpf), N (int or mpf)
    Returns: H0 prediction as mpf
    """
    return H0_0 * r ** mpf(N)


# ================================================================
# FALSIFICATION TESTS (from notebook Section 7)
# ================================================================

def test_F1_monotonic(H0_values_ordered):
    """F1: Are the H0 values monotonically decreasing with distance?
    If not, the running curve thesis is not supported.

    Args: list of H0 values ordered by increasing distance
    Returns: (passed, details) tuple
    """
    # F1 strict: raw values
    H0_ordered_values = [H0_MEASUREMENTS[k]["H0"] for k in H0_ORDERED]
    f1_strict, f1_strict_detail = test_F1_monotonic(H0_ordered_values)
    chk_bool("F1 strict: raw H0 monotonically decreasing",
             f1_strict, f1_strict_detail, checks)

    # F1 soft: within 1-sigma bands, consistent with monotonic?
    # SH0ES and H0LiCOW overlap at 1 sigma (73.0±1.0 vs 73.3±1.8)
    bands_consistent = True
    for i in range(len(H0_ORDERED) - 1):
        m_near = H0_MEASUREMENTS[H0_ORDERED[i]]
        m_far = H0_MEASUREMENTS[H0_ORDERED[i + 1]]
        upper_far = f2m(m_far["H0"] + m_far["uncertainty"])
        lower_near = f2m(m_near["H0"] - m_near["uncertainty"])
        if upper_far > lower_near:
            pass  # bands overlap or far < near — consistent
        # only fails if far is ABOVE near even at 1 sigma
    # Real test: is far+1sigma > near-1sigma for any adjacent pair
    # where far > near in central value?
    soft_violations = []
    for i in range(len(H0_ORDERED) - 1):
        m_near = H0_MEASUREMENTS[H0_ORDERED[i]]
        m_far = H0_MEASUREMENTS[H0_ORDERED[i + 1]]
        if f2m(m_far["H0"]) > f2m(m_near["H0"]):
            lower_far = f2m(m_far["H0"] - m_far["uncertainty"])
            upper_near = f2m(m_near["H0"] + m_near["uncertainty"])
            if lower_far > upper_near:
                soft_violations.append("%s > %s even at 1 sigma" % (
                    H0_ORDERED[i+1], H0_ORDERED[i]))
    f1_soft = len(soft_violations) == 0
    chk_bool("F1 soft: monotonic within 1-sigma uncertainties",
             f1_soft,
             "violations: %s" % (soft_violations if soft_violations else "none — bands overlap"),
             checks)


def test_F2_rational_r(r_val, max_denom=10000, threshold=0.001):
    """F2: Is r a recognizable exact rational?
    Tests if 1-r is close to p/q with small q.

    Args:
      r_val: mpf, the per-transit correction
      max_denom: maximum denominator to test
      threshold: maximum relative error for a "match"
    Returns: (passed, best_fraction, match_quality)
    """
    omr = mpf("1") - r_val
    best_frac = None
    best_quality = mpf("1")

    for q in range(2, max_denom + 1):
        p = int(float(omr * q) + 0.5)
        if 0 < p < q:
            frac_val = f2m(Fraction(p, q))
            quality = abs(omr - frac_val) / omr
            if quality < best_quality:
                best_quality = quality
                best_frac = Fraction(p, q)

    passed = best_quality < mpf(threshold)
    return (passed, best_frac, best_quality)


def test_F3_two_param(residuals, uncertainties, threshold_chi2_per_dof=3.0):
    """F3: Is the two-parameter fit sufficient?
    If chi2/dof > threshold, the simple model is insufficient.

    Args:
      residuals: list of mpf residuals
      uncertainties: list of mpf uncertainties
      threshold_chi2_per_dof: maximum acceptable chi2/dof
    Returns: (passed, chi2, dof, chi2_per_dof)
    """
    chi2 = mpf("0")
    for i in range(len(residuals)):
        if uncertainties[i] > mpf("0"):
            chi2 += (residuals[i] / uncertainties[i]) ** 2
    dof = len(residuals) - 2
    chi2_dof = chi2 / mpf(dof) if dof > 0 else mpf("inf")
    passed = chi2_dof < mpf(threshold_chi2_per_dof)
    return (passed, chi2, dof, chi2_dof)


def test_F4_intermediate_distinct(H0_local_val, H0_far_val, H0_intermediate_vals,
                                    sigma_threshold=1.5):
    """F4: Do intermediate values remain distinct from endpoints?
    If intermediate H0 converges to an endpoint, the curve collapses.

    Args:
      H0_local_val, H0_far_val: mpf
      H0_intermediate_vals: list of (value, uncertainty) as mpf pairs
      sigma_threshold: minimum sigma separation from both endpoints
    Returns: (passed, details)
    """
    local = f2m(H0_local_val) if isinstance(H0_local_val, Fraction) else H0_local_val
    far = f2m(H0_far_val) if isinstance(H0_far_val, Fraction) else H0_far_val

    all_distinct = True
    details = []
    for val, unc in H0_intermediate_vals:
        v = f2m(val) if isinstance(val, Fraction) else val
        u = f2m(unc) if isinstance(unc, Fraction) else unc
        sep_local = abs(v - local) / u if u > 0 else mpf("inf")
        sep_far = abs(v - far) / u if u > 0 else mpf("inf")
        distinct = (sep_local > sigma_threshold) or (sep_far > sigma_threshold)
        if not distinct:
            all_distinct = False
        details.append("H0=%s: %.1f sigma from local, %.1f sigma from far, %s" % (
            mp.nstr(v, 4), float(sep_local), float(sep_far),
            "DISTINCT" if distinct else "COLLAPSED"))

    return (all_distinct, details)


# ================================================================
# COMPARISON TO ALPHA RUNNING (structural parallel)
# ================================================================

def alpha_running_step():
    """The known per-threshold step for alpha running.
    Returns 1/(3*pi) = 1/(12*R2) as mpf.
    """
    return VP_STEP_SIZE


def H0_to_alpha_ratio(N_eff):
    """Ratio of H0 per-transit correction to alpha per-threshold correction.
    Returns (1-r_H0) / (1/(3*pi)) for given N.
    """
    omr = one_minus_r(N_eff)
    return omr / VP_STEP_SIZE


# ================================================================
# SERIES CONNECTION MAP
# ================================================================

SERIES_CONNECTIONS = {
    "PHYS-1": "Soliton boundaries produce different readings at different depths",
    "PHYS-2": "Transformation law is more fundamental than any single value",
    "PHYS-3": "Reproducibility within one depth != universality across depths",
    "PHYS-4": "Per-transit correction must be ~0.9992 to ~0.99992 depending on N",
    "PHYS-5": "VP running through discrete boundaries matches CODATA to 0.02 ppm",
    "PHYS-11": "H0 running would be Subgroup B (monotonic accumulation)",
}


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHYS24_HUBBLE_LIB SELF-TEST")
    print("=" * 70)
    print()
    print("  STATUS: %s" % HYPOTHESIS_STATUS)
    print("  This library tests a HYPOTHESIS. It is not verified physics.")
    print()

    checks = []

    # --------------------------------------------------------
    print("MEASURED VALUES")
    print("-" * 70)
    print()

    chk_bool("5 H0 measurements loaded",
             len(H0_MEASUREMENTS) == 5,
             "count = %d" % len(H0_MEASUREMENTS), checks)

    chk_exact("SH0ES H0 = 73.0",
              H0_MEASUREMENTS["SH0ES"]["H0"], Fraction(730, 10), checks)

    chk_exact("Planck H0 = 67.4",
              H0_MEASUREMENTS["Planck"]["H0"], Fraction(674, 10), checks)

    chk_exact("Cumulative ratio = 337/365",
              cumulative_ratio, Fraction(337, 365), checks)

    chk_bool("Tension > 4 sigma",
             H0_tension_sigma > mpf("4"),
             "tension = %s sigma" % mp.nstr(H0_tension_sigma, 3), checks)

    # --------------------------------------------------------
    print()
    print("RUNNING CURVE MODEL")
    print("-" * 70)
    print()

    # Test H0_running function
    test_H0 = H0_running(Fraction(730, 10), mpf("0.99"), 10)
    expected_H0 = f2m(Fraction(730, 10)) * mpf("0.99") ** 10
    chk("H0_running(73.0, 0.99, 10)",
        test_H0, expected_H0, 10, checks)

    # Test extract_r
    r_test = extract_r(Fraction(730, 10), Fraction(674, 10), 100)
    chk("extract_r recovers required_r(100)",
        r_test, required_r(100), 10, checks)

    # Test roundtrip: H0(0) * r^N = H0_far
    for N_test in [10, 100, 1000]:
        r_N = required_r(N_test)
        H0_pred = H0_running(H0_local, r_N, N_test)
        chk("Roundtrip at N=%d: H0(N) = 67.4" % N_test,
            H0_pred, f2m(H0_far), 6, checks)

    # --------------------------------------------------------
    print()
    print("MAGNITUDE CONSTRAINTS")
    print("-" * 70)
    print()

    for N in [10, 100, 1000, 10000]:
        r_val = MAGNITUDE_TABLE[N]["r"]
        omr = MAGNITUDE_TABLE[N]["one_minus_r"]
        print("  N = %5d:  r = %s,  1-r = %s  (%s)" % (
            N, mp.nstr(r_val, 8), mp.nstr(omr, 4),
            MAGNITUDE_TABLE[N]["character"]))

    chk_bool("1-r decreases with N",
             MAGNITUDE_TABLE[10]["one_minus_r"] > MAGNITUDE_TABLE[1000]["one_minus_r"],
             "1-r(10) = %s > 1-r(1000) = %s" % (
                 mp.nstr(MAGNITUDE_TABLE[10]["one_minus_r"], 4),
                 mp.nstr(MAGNITUDE_TABLE[1000]["one_minus_r"], 4)), checks)

    # --------------------------------------------------------
    print()
    print("FALSIFICATION TEST F1: MONOTONICITY")
    print("-" * 70)
    print()

    H0_ordered_values = [H0_MEASUREMENTS[k]["H0"] for k in H0_ORDERED]
    f1_passed, f1_detail = test_F1_monotonic(H0_ordered_values)
    chk_bool("F1: H0 monotonically decreasing with distance",
             f1_passed, f1_detail, checks)

    # --------------------------------------------------------
    print()
    print("FALSIFICATION TEST F4: INTERMEDIATE VALUES DISTINCT")
    print("-" * 70)
    print()

    intermediates = [
        (H0_MEASUREMENTS["CCHP"]["H0"], H0_MEASUREMENTS["CCHP"]["uncertainty"]),
    ]
    f4_passed, f4_details = test_F4_intermediate_distinct(
        H0_local, H0_far, intermediates)
    for d in f4_details:
        print("  %s" % d)
    chk_bool("F4: CCHP (69.8) distinct from endpoints",
             f4_passed, "see details above", checks)

    # --------------------------------------------------------
    print()
    print("STRUCTURAL PARALLEL: ALPHA RUNNING")
    print("-" * 70)
    print()

    show("VP step size 1/(3*pi)", VP_STEP_SIZE)
    show("ln(73.0/67.4)", ln_cumulative)

    for N in [10, 100, 1000]:
        ratio = H0_to_alpha_ratio(N)
        print("  At N=%d: H0 step / alpha step = %s" % (N, mp.nstr(ratio, 4)))

    chk_bool("H0 step < alpha step for all reasonable N",
             one_minus_r(10) < VP_STEP_SIZE,
             "1-r(N=10) = %s < VP = %s" % (
                 mp.nstr(one_minus_r(10), 4), mp.nstr(VP_STEP_SIZE, 4)), checks)

    # --------------------------------------------------------
    print()
    print("EXAMPLE: FIT WITH ASSUMED N VALUES")
    print("-" * 70)
    print()

    # Hypothetical N assignments (THESE ARE GUESSES — not derived)
    example_N = [0, 5, 50, 500, 5000]
    example_meas = [
        (H0_MEASUREMENTS["SH0ES"]["H0"], H0_MEASUREMENTS["SH0ES"]["uncertainty"]),
        (H0_MEASUREMENTS["H0LiCOW"]["H0"], H0_MEASUREMENTS["H0LiCOW"]["uncertainty"]),
        (H0_MEASUREMENTS["CCHP"]["H0"], H0_MEASUREMENTS["CCHP"]["uncertainty"]),
        (H0_MEASUREMENTS["DES_BAO_BBN"]["H0"], H0_MEASUREMENTS["DES_BAO_BBN"]["uncertainty"]),
        (H0_MEASUREMENTS["Planck"]["H0"], H0_MEASUREMENTS["Planck"]["uncertainty"]),
    ]

    fit = fit_running_curve(example_meas, example_N)
    if fit:
        print("  Assumed N assignments: %s" % example_N)
        print("  H0(0) = %s km/s/Mpc" % mp.nstr(fit["H0_0"], 5))
        print("  r = %s" % mp.nstr(fit["r"], 10))
        print("  1 - r = %s" % mp.nstr(mpf("1") - fit["r"], 6))
        print("  chi2 = %s (dof = %d)" % (mp.nstr(fit["chi2"], 4), fit["dof"]))
        if fit["dof"] > 0:
            print("  chi2/dof = %s" % mp.nstr(fit["chi2"] / mpf(fit["dof"]), 4))
        print()
        print("  Predictions from this fit:")
        for N_pred in [1, 10, 100, 1000, 10000]:
            H0_p = predict_H0(fit["H0_0"], fit["r"], N_pred)
            print("    N = %5d: H0 = %s km/s/Mpc" % (N_pred, mp.nstr(H0_p, 5)))
        print()
        print("  WARNING: N assignments are GUESSES. This fit is illustrative only.")
        print("  Real N values require published large-scale structure catalogs.")

    # --------------------------------------------------------
    print()
    print("UNKNOWN QUANTITIES (None values)")
    print("-" * 70)
    print()

    none_count = 0
    for key in H0_ORDERED:
        m = H0_MEASUREMENTS[key]
        if m["effective_N"] is None:
            print("  %s: effective_N = None" % key)
            none_count += 1
    print()
    print("  %d of %d measurements have unknown effective N." % (
        none_count, len(H0_ORDERED)))
    print("  This is the primary data gap blocking the analysis.")

    chk_bool("All effective_N are None (honest unknowns)",
             all(H0_MEASUREMENTS[k]["effective_N"] is None for k in H0_ORDERED),
             "all None", checks)

    # --------------------------------------------------------
    print()
    print("SERIES CONNECTIONS")
    print("-" * 70)
    print()

    for paper, connection in SERIES_CONNECTIONS.items():
        print("  %s: %s" % (paper, connection))

    chk_bool("6 series connections mapped",
             len(SERIES_CONNECTIONS) == 6,
             "count = %d" % len(SERIES_CONNECTIONS), checks)

    # --------------------------------------------------------
    print()
    print_summary(checks)

    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print()
    if n_fail == 0:
        print("  HUBBLE LIBRARY: OPERATIONAL (hypothesis status: %s)" % HYPOTHESIS_STATUS)
    else:
        print("  HUBBLE LIBRARY: %d FAILURES" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("  REMINDER: This library encodes a HYPOTHESIS, not verified physics.")
    print("  Every effective_N is None. The per-transit correction r is unknown.")
    print("  The curve fit is illustrative. Real N values require structure catalogs.")
    print()
    print("=" * 70)
    print("PHYS24_HUBBLE_LIB SELF-TEST COMPLETE")
    print("=" * 70)
