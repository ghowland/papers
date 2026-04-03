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
        "H0": Fraction(730, 10),
        "uncertainty": Fraction(10, 10),
        "year": 2022,
        "source": "Riess et al. 2022, ApJ 934, L7",
        "distance_class": "local",
        "effective_N": None,
        "effective_N_estimate": "low",
        "method": "distance ladder: Cepheids -> SNe Ia",
    },
    "H0LiCOW": {
        "name": "H0LiCOW (gravitational lensing time delays)",
        "H0": Fraction(733, 10),
        "uncertainty": Fraction(18, 10),
        "year": 2020,
        "source": "Wong et al. 2020, MNRAS 498, 1420",
        "distance_class": "local-medium",
        "effective_N": None,
        "effective_N_estimate": "low-medium",
        "method": "strong lensing time delays through lens galaxy",
    },
    "CCHP": {
        "name": "CCHP (Tip of Red Giant Branch)",
        "H0": Fraction(698, 10),
        "uncertainty": Fraction(17, 10),
        "year": 2021,
        "source": "Freedman 2021, ApJ 919, 16",
        "distance_class": "medium",
        "effective_N": None,
        "effective_N_estimate": "medium",
        "method": "TRGB calibration, different from Cepheids",
    },
    "DES_BAO_BBN": {
        "name": "DES + BAO + BBN (combined cosmological)",
        "H0": Fraction(674, 10),
        "uncertainty": Fraction(12, 10),
        "year": 2022,
        "source": "DES Collaboration 2022",
        "distance_class": "high",
        "effective_N": None,
        "effective_N_estimate": "high",
        "method": "baryon acoustic oscillations + big bang nucleosynthesis",
    },
    "Planck": {
        "name": "Planck CMB (cosmic microwave background)",
        "H0": Fraction(674, 10),
        "uncertainty": Fraction(5, 10),
        "year": 2020,
        "source": "Planck Collaboration 2020, A&A 641, A6",
        "distance_class": "maximum",
        "effective_N": None,
        "effective_N_estimate": "maximum",
        "method": "CMB power spectrum fit assuming Lambda-CDM",
    },
}

H0_ORDERED = ["SH0ES", "H0LiCOW", "CCHP", "DES_BAO_BBN", "Planck"]


# ================================================================
# DERIVED QUANTITIES
# ================================================================

H0_local = H0_MEASUREMENTS["SH0ES"]["H0"]
H0_far = H0_MEASUREMENTS["Planck"]["H0"]
cumulative_ratio = H0_far / H0_local

ln_cumulative = mlog(f2m(H0_local) / f2m(H0_far))

H0_tension_sigma = (f2m(H0_local) - f2m(H0_far)) / msqrt(
    f2m(H0_MEASUREMENTS["SH0ES"]["uncertainty"]) ** 2 +
    f2m(H0_MEASUREMENTS["Planck"]["uncertainty"]) ** 2)


# ================================================================
# THE RUNNING CURVE MODEL
# ================================================================

def H0_running(H0_0, r, N):
    """H0(N) = H0(0) * r^N"""
    h0 = f2m(H0_0) if isinstance(H0_0, Fraction) else mpf(H0_0)
    r_val = f2m(r) if isinstance(r, Fraction) else mpf(r)
    return h0 * r_val ** mpf(N)


def extract_r(H0_near, H0_far_val, N_eff):
    """r = (H0_far / H0_near)^(1/N)"""
    near = f2m(H0_near) if isinstance(H0_near, Fraction) else mpf(H0_near)
    far = f2m(H0_far_val) if isinstance(H0_far_val, Fraction) else mpf(H0_far_val)
    return (far / near) ** (mpf("1") / mpf(N_eff))


def required_r(N_eff):
    """r = (67.4/73.0)^(1/N) = (337/365)^(1/N)"""
    return f2m(cumulative_ratio) ** (mpf("1") / mpf(N_eff))


def one_minus_r(N_eff):
    """1 - r, the correction per transit."""
    return mpf("1") - required_r(N_eff)


# ================================================================
# MAGNITUDE CONSTRAINTS
# ================================================================

MAGNITUDE_TABLE = {}
for _N in [10, 100, 1000, 10000]:
    _r = required_r(_N)
    MAGNITUDE_TABLE[_N] = {
        "r": _r,
        "one_minus_r": mpf("1") - _r,
        "character": "~1/%d" % int(round(1.0 / float(mpf("1") - _r))),
    }


# ================================================================
# STRUCTURAL PARALLELS
# ================================================================

VP_STEP_SIZE = mpf("1") / (mpf("3") * mpi)

STRUCTURAL_PARALLELS = {
    "alpha_running": {
        "variable": "probe energy",
        "boundaries": "flavor thresholds (quark masses)",
        "direction": "alpha increases with energy",
        "per_boundary_value": VP_STEP_SIZE,
        "derived_from": "group theory counting (Dynkin indices)",
    },
    "H0_running": {
        "variable": "effective distance / boundary count N",
        "boundaries": "soliton boundaries (galaxy clusters, filaments, voids)",
        "direction": "H0 decreases with N",
        "per_boundary_value": None,
        "derived_from": "boundary geometry (unknown)",
    },
}


# ================================================================
# CANDIDATE RATIONAL SCANNING
# ================================================================

def scan_rational_candidates(N_min=5, N_max=10000):
    """For each plausible N, check if 1-r approximates a simple fraction."""
    interesting_denoms = [
        3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 24, 25, 30,
        32, 36, 40, 48, 50, 60, 64, 72, 75, 80, 96, 100, 120,
        125, 128, 144, 150, 160, 192, 200, 240, 250, 256, 300,
        360, 375, 400, 480, 500, 600, 625, 720, 750, 800, 1000,
        1250, 1500, 2000, 2500, 5000, 10000, 12500, 125000,
    ]

    N_values = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    N_values = [n for n in N_values if N_min <= n <= N_max]

    results = []
    for N in N_values:
        r_val = required_r(N)
        omr = mpf("1") - r_val

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
    """Fit H0(N) = H0(0) * r^N to measurements with assigned N values.

    Args:
      measurements: list of (H0_value, H0_uncertainty) as Fractions
      N_assignments: list of N values (int or mpf), same length
    Returns: dict with H0_0, r, residuals, chi2, dof
    """
    if len(measurements) < 2:
        return None

    H0_first = f2m(measurements[0][0])
    H0_last = f2m(measurements[-1][0])
    N_first = mpf(N_assignments[0])
    N_last = mpf(N_assignments[-1])

    if N_last == N_first:
        return None

    r_init = (H0_last / H0_first) ** (mpf("1") / (N_last - N_first))
    H0_0_init = H0_first / r_init ** N_first

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
    """Predict H0 at a specific boundary transit count."""
    return H0_0 * r ** mpf(N)


# ================================================================
# FALSIFICATION TESTS
# ================================================================

def test_F1_strict(H0_values_ordered):
    """F1 strict: Are raw H0 values monotonically decreasing?"""
    for i in range(len(H0_values_ordered) - 1):
        v_near = f2m(H0_values_ordered[i]) if isinstance(H0_values_ordered[i], Fraction) else H0_values_ordered[i]
        v_far = f2m(H0_values_ordered[i+1]) if isinstance(H0_values_ordered[i+1], Fraction) else H0_values_ordered[i+1]
        if v_far > v_near:
            return (False, "H0 increases from point %d to %d: %s > %s" % (
                i, i+1, mp.nstr(v_far, 4), mp.nstr(v_near, 4)))
    return (True, "H0 monotonically decreasing across %d points" % len(H0_values_ordered))


def test_F1_soft(ordered_keys, measurements):
    """F1 soft: Is ordering consistent with monotonic within 1-sigma?
    Only fails if far_lower > near_upper for an adjacent pair where
    the far central value exceeds the near central value.
    """
    violations = []
    for i in range(len(ordered_keys) - 1):
        m_near = measurements[ordered_keys[i]]
        m_far = measurements[ordered_keys[i + 1]]
        near_val = f2m(m_near["H0"])
        far_val = f2m(m_far["H0"])
        if far_val > near_val:
            far_lower = far_val - f2m(m_far["uncertainty"])
            near_upper = near_val + f2m(m_near["uncertainty"])
            if far_lower > near_upper:
                violations.append("%s > %s even at 1-sigma" % (
                    ordered_keys[i + 1], ordered_keys[i]))
    return (len(violations) == 0, violations)


def test_F2_rational_r(r_val, max_denom=10000, threshold=0.001):
    """F2: Is r a recognizable exact rational?"""
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
    """F3: Is the two-parameter fit sufficient?"""
    chi2 = mpf("0")
    for i in range(len(residuals)):
        if uncertainties[i] > mpf("0"):
            chi2 += (residuals[i] / uncertainties[i]) ** 2
    dof = len(residuals) - 2
    chi2_dof = chi2 / mpf(dof) if dof > 0 else mpf("inf")
    passed = chi2_dof < mpf(threshold_chi2_per_dof)
    return (passed, chi2, dof, chi2_dof)


def test_F4_intermediate_distinct(H0_local_val, H0_far_val,
                                    H0_intermediate_vals, sigma_threshold=1.5):
    """F4: Do intermediate values remain distinct from endpoints?"""
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
# HELPERS
# ================================================================

def alpha_running_step():
    """1/(3*pi) = 1/(12*R2)"""
    return VP_STEP_SIZE


def H0_to_alpha_ratio(N_eff):
    """Ratio of H0 per-transit correction to alpha per-threshold correction."""
    return one_minus_r(N_eff) / VP_STEP_SIZE


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

    test_H0 = H0_running(Fraction(730, 10), mpf("0.99"), 10)
    expected_H0 = f2m(Fraction(730, 10)) * mpf("0.99") ** 10
    chk("H0_running(73.0, 0.99, 10)",
        test_H0, expected_H0, 10, checks)

    r_test = extract_r(Fraction(730, 10), Fraction(674, 10), 100)
    chk("extract_r recovers required_r(100)",
        r_test, required_r(100), 10, checks)

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

    f1_strict_passed, f1_strict_detail = test_F1_strict(H0_ordered_values)
    chk_bool("F1 strict: raw H0 monotonically decreasing",
             f1_strict_passed, f1_strict_detail, checks)

    f1_soft_passed, f1_soft_violations = test_F1_soft(H0_ORDERED, H0_MEASUREMENTS)
    chk_bool("F1 soft: monotonic within 1-sigma uncertainties",
             f1_soft_passed,
             "violations: %s" % (f1_soft_violations if f1_soft_violations else "none (bands overlap)"),
             checks)

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
        print("  HUBBLE LIBRARY: ALL PASS (hypothesis status: %s)" % HYPOTHESIS_STATUS)
    else:
        n_pass = sum(1 for _, s in checks if s == "PASS")
        print("  HUBBLE LIBRARY: %d PASS, %d FAIL (hypothesis status: %s)" % (
            n_pass, n_fail, HYPOTHESIS_STATUS))
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


# Report on the Null value in output: TOTAL: 16 PASS, 1 FAIL out of 17
"""
# The F1 Strict Null: What the Monotonicity Failure Means

**Library:** phys24_hubble_lib.py

**Test:** F1 strict — raw H0 monotonically decreasing with distance

**Result:** FAIL

**Date:** April 3, 2026

---

## 1. The Observation

The five H₀ measurements, ordered by increasing effective distance:

| Rank | Method | H₀ (km/s/Mpc) | Uncertainty | Distance Class |
|---|---|---|---|---|
| 1 | SH0ES | 73.0 | ±1.0 | local |
| 2 | H0LiCOW | 73.3 | ±1.8 | local-medium |
| 3 | CCHP | 69.8 | ±1.7 | medium |
| 4 | DES+BAO+BBN | 67.4 | ±1.2 | high |
| 5 | Planck | 67.4 | ±0.5 | maximum |

The F1 strict test checks whether each value is less than or equal to the one before it. It fails at the first pair: H0LiCOW (73.3) > SH0ES (73.0). The sequence is not monotonically decreasing.

The F1 soft test checks whether this violation survives within 1-sigma uncertainties. SH0ES has 73.0 ± 1.0, so its upper bound is 74.0. H0LiCOW has 73.3 ± 1.8, so its lower bound is 71.5. The bands overlap by 2.5 km/s/Mpc. The soft test passes — the violation is within measurement noise.

---

## 2. What the FAIL Does NOT Mean

The FAIL does not mean the running curve hypothesis is dead. Here is why.

The running curve hypothesis says: H₀(N) = H₀(0) × r^N, where N is the effective boundary transit count. For this curve to be monotonically decreasing, every measurement at higher N must give a lower H₀. But the test assumes the ordering SH0ES → H0LiCOW → CCHP → DES → Planck corresponds to strictly increasing N. That assumption is the weak link, not the data.

SH0ES measures H₀ using Cepheid-calibrated Type Ia supernovae in local galaxies (distances ~20-40 Mpc). H0LiCOW measures H₀ using gravitational lensing time delays through a lens galaxy (distances ~hundreds of Mpc to the source, but the light passes through ONE specific foreground galaxy). The effective boundary transit count for H0LiCOW depends on the specific line of sight — it could be lower, equal to, or higher than SH0ES depending on the large-scale structure along that particular path.

The 0.3 km/s/Mpc difference (73.3 vs 73.0) is 0.4% — well within the combined 2.1 km/s/Mpc uncertainty. These two measurements are statistically indistinguishable. Assigning them to different distance classes with a strict ordering is the error, not the data.

---

## 3. What the FAIL DOES Mean

The FAIL tells us three concrete things.

**First:** SH0ES and H0LiCOW are in the same distance class. They should not be treated as distinct points on a running curve. They are two measurements of the same effective quantity — H₀ at low boundary transit count — made with different methods. Their agreement (73.0 vs 73.3, 0.4% apart) is a consistency check, not two points on a curve.

**Second:** the running curve hypothesis has at most three independent distance classes in the current data, not five:

| Class | Methods | H₀ range | Status |
|---|---|---|---|
| Local (low N) | SH0ES + H0LiCOW | 73.0 - 73.3 | Two methods agree |
| Intermediate (medium N) | CCHP | 69.8 | Single method |
| Cosmological (high N) | DES + Planck | 67.4 | Two methods agree |

Three classes, three H₀ values, strictly decreasing: 73.2 (average of local) > 69.8 > 67.4. A two-parameter model (H₀(0) and r) through three points has one degree of freedom. This is a fit, not an overdetermination. The curve thesis requires at least four independent distance classes to be testable.

**Third:** the effective boundary transit count N is the primary unknown, not r. The magnitude constraint table shows that r is fully determined once N is known. The question is not "what is r?" but "what is N for each measurement method?" This requires published large-scale structure catalogs along the specific lines of sight used by each measurement team. Without N, the curve cannot be fit.

---

## 4. What the Two Tests Together Mean

| Test | Result | Interpretation |
|---|---|---|
| F1 strict | FAIL | Raw ordering has a 0.3 km/s/Mpc inversion at rank 1-2 |
| F1 soft | PASS | The inversion is within 1-sigma measurement noise |

Together: the data is consistent with monotonic decrease but does not prove it. The inversion at rank 1-2 is noise, not signal. The real structure is three distance classes with strictly decreasing H₀.

This is the correct state for an active investigation with limited data. The hypothesis survives but is not confirmed. The falsification test did its job — it identified the weakest point in the data ordering and showed that it is not a hard violation.

---

## 5. What Would Change the Assessment

**Upgrade to FAIL (hypothesis weakened):** A future measurement at an unambiguously intermediate distance (100-500 Mpc, well-determined line of sight) that gives H₀ > 73 km/s/Mpc. This would be a genuine non-monotonic value that cannot be explained by distance class overlap.

**Upgrade to PASS (hypothesis strengthened):** Multiple measurements at different well-characterized distances that all fall on a smooth curve when plotted against estimated N. The curve would need to pass through 73.2 at low N, 69.8 at medium N, and 67.4 at high N, with intermediate values falling on the same curve.

**Kill (hypothesis dead):** Discovery of a systematic error in either the local or cosmological measurement chain that resolves the Hubble tension without any distance-dependent running. If the tension disappears, the running curve is unnecessary.

**Unlock (hypothesis testable):** Published estimates of effective boundary transit count N for each measurement method, derived from SDSS, 2dF, or Planck lensing maps of large-scale structure along the specific lines of sight. This is the blocking dependency. Without N, the curve fit is illustrative only.

---

## 6. The Data Gap

The self-test output shows:

```
UNKNOWN QUANTITIES (None values)
  SH0ES: effective_N = None
  H0LiCOW: effective_N = None
  CCHP: effective_N = None
  DES_BAO_BBN: effective_N = None
  Planck: effective_N = None

  5 of 5 measurements have unknown effective N.
  This is the primary data gap blocking the analysis.
```

Every effective_N is None. This is the honest state of the library. The running curve model H₀(N) = H₀(0) × r^N has two parameters (H₀(0) and r) and five data points, but zero of those data points have a known N coordinate. The model is underdetermined in its independent variable.

The example fit uses guessed N values [0, 5, 50, 500, 5000] and produces chi²/dof = 6.98 — a poor fit, confirming the guesses are wrong. Different N assignments would give different r values and different chi² values. Without real N values, the fit is meaningless.

The per-transit correction r is not independently unknown — it is fully determined by N through the constraint r^N = 67.4/73.0 = 337/365. Knowing N for any one measurement (other than the endpoints) would determine r and enable prediction at all other distances. This is a one-parameter problem disguised as a two-parameter problem.

---

## 7. The Structural Parallel

The alpha running computation in PHYS-5 faces none of these ambiguities because the independent variable (energy scale μ) is directly measured at every point. The effective boundary transit count for alpha running is known exactly — it is the number of quark flavor thresholds between the two energy scales. The per-threshold correction 1/(3π) = 1/(12R₂) is derived from group theory.

The Hubble running hypothesis has the same mathematical structure but none of the same certainty in the independent variable. Energy scales are measured by accelerators. Boundary transit counts for cosmological light paths are estimated from galaxy surveys with large systematic uncertainties.

This asymmetry is the fundamental difference between the two cases:

| Property | α running | H₀ running (hypothesis) |
|---|---|---|
| Independent variable known? | Yes (energy μ from accelerator) | No (N from structure catalogs, not measured) |
| Per-boundary correction derived? | Yes (Dynkin indices, group theory) | No (unknown) |
| Data points | Continuous (any μ above confinement) | 3-5 discrete distance classes |
| Model tested to | 0.02 ppm (PHYS-5) | Not tested (no N values) |

The hypothesis borrows the structure of alpha running but cannot borrow its certainty until N is known.

---

## 8. Recommendation

Keep the F1 strict FAIL in the self-test. Do not relax it. It is informative.

The FAIL tells every future session: "the raw data ordering has an inversion at rank 1-2, SH0ES and H0LiCOW are in the same distance class, and the running curve hypothesis has three effective data points, not five."

The soft PASS tells them: "the inversion is within noise and the data is consistent with monotonic decrease."

Both facts together give the correct picture: a hypothesis that survives its first contact with data but is not yet testable due to the N gap.

The next step is not more modeling. It is data: published estimates of effective boundary transit count for at least one intermediate measurement method (CCHP is the best candidate because its distance class is most distinct from both endpoints). With one N value, r is determined and the curve makes predictions at every other distance.

---

*F1 Strict Null Report. 1 FAIL out of 17 checks. The FAIL is data, not a bug. The hypothesis survives within uncertainties but cannot be tested until effective boundary transit counts are known. April 3, 2026.*
"""