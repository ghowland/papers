#!/usr/bin/env python3
"""
HOWL DATA-5 HELPERS — CHUNK 1: DERIVATION & GROUP THEORY
==========================================================
Physics-aware helper functions that wrap data_4_derivation_lib.py
and phys24_structure_lib.py through the DATA5 object system.

Every function takes a db (DATA5 instance) as first argument and
pulls constants from the database objects — not from flat imports.
This ensures all computations trace through the version chain.

Categories in this chunk:
  COUPLING EXTRACTION  — derive GUT couplings from db constants
  GAP RATIO            — compute and compare gap ratios from any betas
  ONE-LOOP RUNNING     — predict alpha_s and sin2_tW at one loop
  TWO-LOOP RUNNING     — predict alpha_s and sin2_tW at two loops
  KOIDE                — ratio, amplitude, m_tau prediction
  BETA DECOMPOSITION   — break down betas into gauge/fermion/higgs/BSM
  GROUP THEORY         — Casimirs, Dynkin indices, representation tests
  WHAT-IF              — test arbitrary BSM representations against data

Usage:
    from data_5_populate import init_data5
    from data_5_helpers_derivation import *

    db = init_data5()
    couplings = extract_couplings(db)
    pred = predict_alpha_s_1L(db)
    show_prediction("alpha_s 1L", pred)

Platform: HOWL-PLATFORM-v1
Depends on: data_5_objects.py, data_5_populate.py, phys24_lib.py,
            data_4_derivation_lib.py

~40 functions across 8 categories:

| Category | Count | Key functions |
|---|---|---|
| Coupling extraction | 2 | `extract_couplings`, `show_couplings` |
| Gap ratio | 6 | `gap_ratio`, `gap_ratio_SM`, `gap_ratio_CD`, `gap_ratio_measured`, `gap_distance`, `show_gap_ratios` |
| One-loop | 5 | `find_crossing_L`, `L_to_scale_MeV`, `run_one_loop`, `predict_alpha_s_1L`, `predict_sin2_1L` |
| Two-loop | 6 | `_get_bij_SM`, `_get_dbij_VL`, `_get_bij_full`, `_euler_two_loop`, `predict_alpha_s_2L`, `predict_sin2_2L` |
| Display | 2 | `show_prediction`, `show_all_predictions` |
| Koide | 5 | `koide_ratio_db`, `koide_amplitude_sq`, `koide_predict`, `show_koide` |
| Beta decomposition | 2 | `decompose_beta`, `show_beta_decomposition` |
| Group theory | 6 | `casimir_adj`, `casimir_fund`, `dynkin_fund`, `yang_mills_coefficient`, `gauge_beta`, `generation_democracy_check` |
| What-if | 3 | `whatif_rep`, `whatif_scan`, `whatif_custom_betas` |
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
_LIB_VERSION_1 = ("Session 4, April 3 2026. Chunk 1: Derivation & "
                   "group theory helpers. ~40 functions.")


# ================================================================
# INTERNAL: Pull values from db with fallback
# ================================================================

def _val(db, obj_id):
    """Get value from db. Returns Fraction or None."""
    obj = db.get(obj_id)
    if obj is None:
        return None
    if hasattr(obj, 'value'):
        return obj.value
    return None


def _mpf(db, obj_id):
    """Get value from db as mpf."""
    v = _val(db, obj_id)
    if v is None:
        return None
    if isinstance(v, Fraction):
        return f2m(v)
    return mpf(str(v))


def _beta_val(db, beta_id):
    """Get beta coefficient value from db."""
    obj = db.get(beta_id)
    if obj is None:
        return None
    return obj.value


# ================================================================
# COUPLING EXTRACTION
# ================================================================

def extract_couplings(db):
    """Extract GUT-normalized inverse couplings at M_Z from db constants.

    Uses: const.alpha_inv, const.sin2_tW, const.alpha_s
    Returns: dict with inv_a1, inv_a2, inv_a3 as Fractions

    Derivation (PHYS-30):
      1/alpha_2 = sin2_tW * alpha_inv  (NOT alpha_inv / sin2_tW)
      1/alpha_1 = (3/5) * (alpha_inv - 1/alpha_2)
      1/alpha_3 = 1/alpha_s
    """
    alpha_inv_f = _val(db, "const.alpha_inv")
    sin2_f = _val(db, "const.sin2_tW")
    alpha_s_f = _val(db, "const.alpha_s")

    inv_a2 = sin2_f * alpha_inv_f
    inv_a1 = Fraction(3, 5) * (alpha_inv_f - inv_a2)
    inv_a3 = Fraction(1, 1) / alpha_s_f

    return {
        "inv_a1": inv_a1,
        "inv_a2": inv_a2,
        "inv_a3": inv_a3,
        "inv_a1_mpf": f2m(inv_a1),
        "inv_a2_mpf": f2m(inv_a2),
        "inv_a3_mpf": f2m(inv_a3),
    }


def show_couplings(db):
    """Print the three GUT-normalized couplings at M_Z."""
    c = extract_couplings(db)
    print("  GUT COUPLINGS AT M_Z (from db constants):")
    print("    1/alpha_1 = %s = %s" % (c["inv_a1"], mp.nstr(c["inv_a1_mpf"], 7)))
    print("    1/alpha_2 = %s = %s" % (c["inv_a2"], mp.nstr(c["inv_a2_mpf"], 7)))
    print("    1/alpha_3 = %s = %s" % (c["inv_a3"], mp.nstr(c["inv_a3_mpf"], 7)))


# ================================================================
# GAP RATIO
# ================================================================

def gap_ratio(db, b1_id, b2_id, b3_id):
    """Compute gap ratio from three beta coefficient db objects.

    gap = (b1 - b2) / (b2 - b3)

    Usage:
        gap_ratio(db, "beta.b1_SM", "beta.b2_SM", "beta.b3_SM")  -> 218/115
        gap_ratio(db, "beta.b1_mod", "beta.b2_mod", "beta.b3_mod")  -> 38/27
    """
    b1 = _beta_val(db, b1_id)
    b2 = _beta_val(db, b2_id)
    b3 = _beta_val(db, b3_id)
    return (b1 - b2) / (b2 - b3)


def gap_ratio_SM(db):
    """SM gap ratio from db beta objects. Should be 218/115."""
    return gap_ratio(db, "beta.b1_SM", "beta.b2_SM", "beta.b3_SM")


def gap_ratio_CD(db):
    """CD (modified) gap ratio from db. Should be 38/27."""
    return gap_ratio(db, "beta.b1_mod", "beta.b2_mod", "beta.b3_mod")


def gap_ratio_measured(db):
    """Measured gap ratio from db. ~1.358."""
    return _val(db, "const.gap_measured")


def gap_distance(db, b1_id, b2_id, b3_id):
    """Distance between a model's gap ratio and the measured value.

    Usage: gap_distance(db, "beta.b1_mod", "beta.b2_mod", "beta.b3_mod")
    """
    model_gap = gap_ratio(db, b1_id, b2_id, b3_id)
    meas_gap = gap_ratio_measured(db)
    return abs(f2m(model_gap) - f2m(meas_gap))


def show_gap_ratios(db):
    """Print all gap ratios with distance from measured."""
    meas = f2m(gap_ratio_measured(db))
    print("  GAP RATIO COMPARISON:")
    print("  %-15s %-15s %-12s %s" % ("Model", "Fraction", "Decimal", "Distance"))
    print("  %-15s %-15s %-12s %s" % ("-" * 15, "-" * 15, "-" * 12, "-" * 12))

    for name, b1, b2, b3 in [
        ("SM", "beta.b1_SM", "beta.b2_SM", "beta.b3_SM"),
        ("CD", "beta.b1_mod", "beta.b2_mod", "beta.b3_mod"),
    ]:
        g = gap_ratio(db, b1, b2, b3)
        gv = f2m(g)
        dist = abs(gv - meas)
        pct = dist / meas * mpf("100")
        print("  %-15s %-15s %-12s %s%%" % (
            name, g, mp.nstr(gv, 6), mp.nstr(pct, 4)))

    mssm = _val(db, "const.gap_MSSM")
    if mssm is not None:
        gv = f2m(mssm)
        dist = abs(gv - meas)
        pct = dist / meas * mpf("100")
        print("  %-15s %-15s %-12s %s%%" % (
            "MSSM", mssm, mp.nstr(gv, 6), mp.nstr(pct, 4)))

    print("  %-15s %-15s %-12s %s" % (
        "Measured", "", mp.nstr(meas, 6), "—"))


# ================================================================
# ONE-LOOP RUNNING
# ================================================================

def find_crossing_L(db, b1_id="beta.b1_mod", b2_id="beta.b2_mod"):
    """Find L_GUT where 1/alpha_1 = 1/alpha_2 at one loop.

    L = (1/a1 - 1/a2) / (b1 - b2)

    Returns: L as Fraction (exact)
    """
    c = extract_couplings(db)
    b1 = _beta_val(db, b1_id)
    b2 = _beta_val(db, b2_id)
    return (c["inv_a1"] - c["inv_a2"]) / (b1 - b2)


def L_to_scale_MeV(db, L_val):
    """Convert L = ln(mu/M_Z)/(2*pi) to energy scale in MeV.

    Returns: (mu_MeV, log10_mu_GeV) as mpf tuple
    """
    M_Z_mpf = _mpf(db, "const.M_Z")
    L = f2m(L_val) if isinstance(L_val, Fraction) else L_val
    mu = M_Z_mpf * mexp(mpf("2") * mpi * L)
    log10_mu_GeV = mlog(mu / mpf("1000"), 10)
    return mu, log10_mu_GeV


def run_one_loop(db, betas_ids, L):
    """Run three couplings at one loop over L steps.

    Args:
        betas_ids: list of 3 beta obj_ids
        L: mpf or Fraction, dimensionless running parameter
    Returns: list of 3 mpf [1/a1, 1/a2, 1/a3] at mu
    """
    c = extract_couplings(db)
    inv_a = [c["inv_a1_mpf"], c["inv_a2_mpf"], c["inv_a3_mpf"]]
    betas = [f2m(_beta_val(db, bid)) for bid in betas_ids]
    L_mpf = f2m(L) if isinstance(L, Fraction) else L
    return [inv_a[i] - betas[i] * L_mpf for i in range(3)]


def predict_alpha_s_1L(db):
    """Predict alpha_s from one-loop CD unification.

    Uses db constants and modified betas.
    Returns: dict with alpha_s_pred, miss_pct, Delta, L_GUT, M_GUT_GeV
    """
    c = extract_couplings(db)
    b1 = _beta_val(db, "beta.b1_mod")
    b2 = _beta_val(db, "beta.b2_mod")
    b3 = _beta_val(db, "beta.b3_mod")

    L_GUT = f2m((c["inv_a1"] - c["inv_a2"]) / (b1 - b2))
    inv_a_GUT = c["inv_a1_mpf"] - f2m(b1) * L_GUT
    inv_a3_at_GUT = c["inv_a3_mpf"] - f2m(b3) * L_GUT
    Delta = inv_a3_at_GUT - inv_a_GUT

    inv_a3_pred = inv_a_GUT + f2m(b3) * L_GUT
    alpha_s_pred = mpf("1") / inv_a3_pred
    alpha_s_meas = _mpf(db, "const.alpha_s")
    miss_pct = abs(alpha_s_pred - alpha_s_meas) / alpha_s_meas * mpf("100")

    _, log10_MGUT = L_to_scale_MeV(db, L_GUT)

    return {
        "alpha_s_pred": alpha_s_pred,
        "miss_pct": miss_pct,
        "Delta": Delta,
        "L_GUT": L_GUT,
        "M_GUT_log10_GeV": log10_MGUT,
        "inv_a_GUT": inv_a_GUT,
    }


def predict_sin2_1L(db):
    """Predict sin2_tW from one-loop CD unification.

    Uses alpha_EM and alpha_s (NOT sin2_tW — that's the prediction).
    Returns: dict with sin2_pred, miss_pct, b_EM
    """
    alpha_inv_f = _val(db, "const.alpha_inv")
    alpha_s_f = _val(db, "const.alpha_s")
    b1 = _beta_val(db, "beta.b1_mod")
    b2 = _beta_val(db, "beta.b2_mod")
    b3 = _beta_val(db, "beta.b3_mod")

    b_EM = Fraction(5, 3) * b1 + b2

    inv_a_EM = f2m(alpha_inv_f)
    eight_thirds_inv_as = f2m(Fraction(8, 3) / alpha_s_f)
    b_EM_mpf = f2m(b_EM)
    b3_mpf = f2m(b3)
    eight_thirds = f2m(Fraction(8, 3))

    L_GUT = (inv_a_EM - eight_thirds_inv_as) / (b_EM_mpf - eight_thirds * b3_mpf)

    inv_a3_val = f2m(Fraction(1, 1) / alpha_s_f)
    inv_a_GUT = inv_a3_val - b3_mpf * L_GUT
    inv_a2_pred = inv_a_GUT + f2m(b2) * L_GUT
    sin2_pred = inv_a2_pred / inv_a_EM

    sin2_meas = _mpf(db, "const.sin2_tW")
    miss_pct = abs(sin2_pred - sin2_meas) / sin2_meas * mpf("100")

    return {
        "sin2_pred": sin2_pred,
        "miss_pct": miss_pct,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
        "inv_a2_pred": inv_a2_pred,
        "b_EM": b_EM,
    }


# ================================================================
# TWO-LOOP RUNNING
# ================================================================

def _get_bij_SM(db):
    """Reconstruct the 3x3 SM b_ij matrix from db constants."""
    bij = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            oid = "const.bij_SM_%d%d" % (i, j)
            bij[i][j] = _val(db, oid)
    return bij


def _get_dbij_VL(db):
    """Reconstruct the 3x3 VL db_ij matrix from db constants."""
    dbij = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            oid = "const.dbij_VL_%d%d" % (i, j)
            dbij[i][j] = _val(db, oid)
    return dbij


def _get_bij_full(db):
    """Reconstruct the full b_ij = SM + VL from db constants."""
    sm = _get_bij_SM(db)
    vl = _get_dbij_VL(db)
    return [[sm[i][j] + vl[i][j] for j in range(3)] for i in range(3)]


def _euler_two_loop(inv_a_start, b1loop, bij, L_total, n_steps):
    """Euler integration of two-loop RGEs.

    d(1/alpha_i)/dL = -b_i - sum_j b_ij * alpha_j / (4*pi)

    Both terms have MINUS signs. The b_ij term uses alpha_j at each step.
    """
    fourpi = mpf("4") * mpi
    inv_a = [mpf(x) for x in inv_a_start]
    dL = L_total / mpf(n_steps)

    for _ in range(n_steps):
        alphas = [mpf("1") / inv_a[k] for k in range(3)]
        d_inv = [mpf("0")] * 3
        for i in range(3):
            d_inv[i] = -b1loop[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi * dL
        for i in range(3):
            inv_a[i] += d_inv[i]

    return inv_a


def predict_alpha_s_2L(db, bij_tag="full", n_steps=500):
    """Predict alpha_s from two-loop unification via binary search.

    Args:
        db: DATA5 instance
        bij_tag: "SM" for SM b_ij only, "full" for SM+VL
        n_steps: Euler integration steps

    Returns: dict with alpha_s_pred, miss_pct, Delta, L_GUT
    """
    c = extract_couplings(db)
    inv_a_start = [c["inv_a1_mpf"], c["inv_a2_mpf"], c["inv_a3_mpf"]]

    b1loop = [f2m(_beta_val(db, "beta.b%d_mod" % (i+1) if i < 3 else "beta.b3_mod"))
              for i in range(3)]
    # Fix: use the correct beta IDs
    b1loop = [f2m(_beta_val(db, bid)) for bid in
              ["beta.b1_mod", "beta.b2_mod", "beta.b3_mod"]]

    if bij_tag == "SM":
        bij_frac = _get_bij_SM(db)
    else:
        bij_frac = _get_bij_full(db)

    bij_mpf = [[f2m(bij_frac[i][j]) for j in range(3)] for i in range(3)]

    # One-loop L estimate
    L_est = f2m(find_crossing_L(db))

    # Binary search for two-loop crossing
    L_lo = L_est * mpf("0.8")
    L_hi = L_est * mpf("1.2")

    for _ in range(60):
        L_mid = (L_lo + L_hi) / mpf("2")
        result = _euler_two_loop(inv_a_start, b1loop, bij_mpf, L_mid, n_steps)
        diff = result[0] - result[1]
        if diff > mpf("0"):
            L_lo = L_mid
        else:
            L_hi = L_mid

    L_GUT = (L_lo + L_hi) / mpf("2")

    at_GUT = _euler_two_loop(inv_a_start, b1loop, bij_mpf, L_GUT, n_steps)
    inv_a_GUT = (at_GUT[0] + at_GUT[1]) / mpf("2")
    Delta = at_GUT[2] - inv_a_GUT

    inv_a_unified = [inv_a_GUT, inv_a_GUT, inv_a_GUT]
    at_MZ = _euler_two_loop(inv_a_unified, b1loop, bij_mpf, -L_GUT, n_steps)
    alpha_s_pred = mpf("1") / at_MZ[2]

    alpha_s_meas = _mpf(db, "const.alpha_s")
    miss_pct = abs(alpha_s_pred - alpha_s_meas) / alpha_s_meas * mpf("100")

    return {
        "alpha_s_pred": alpha_s_pred,
        "miss_pct": miss_pct,
        "Delta": Delta,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
        "bij_tag": bij_tag,
    }


def predict_sin2_2L(db, n_steps=500):
    """Predict sin2_tW from two-loop unification.

    Uses alpha_EM and alpha_s only (sin2_tW is the prediction).
    Returns: dict with sin2_pred, miss_pct, L_GUT
    """
    # One-loop estimate for starting point
    result_1L = predict_sin2_1L(db)
    sin2_est = result_1L["sin2_pred"]

    alpha_inv_f = _val(db, "const.alpha_inv")
    alpha_s_f = _val(db, "const.alpha_s")

    inv_a2_est = sin2_est * f2m(alpha_inv_f)
    inv_a1_est = f2m(Fraction(3, 5)) * (f2m(alpha_inv_f) - inv_a2_est)
    inv_a3_val = f2m(Fraction(1, 1) / alpha_s_f)

    inv_a_start = [inv_a1_est, inv_a2_est, inv_a3_val]
    b1loop = [f2m(_beta_val(db, bid)) for bid in
              ["beta.b1_mod", "beta.b2_mod", "beta.b3_mod"]]
    bij_frac = _get_bij_full(db)
    bij_mpf = [[f2m(bij_frac[i][j]) for j in range(3)] for i in range(3)]

    L_est = result_1L["L_GUT"]
    L_lo = L_est * mpf("0.8")
    L_hi = L_est * mpf("1.2")

    for _ in range(60):
        L_mid = (L_lo + L_hi) / mpf("2")
        result = _euler_two_loop(inv_a_start, b1loop, bij_mpf, L_mid, n_steps)
        diff = result[0] - result[1]
        if diff > mpf("0"):
            L_lo = L_mid
        else:
            L_hi = L_mid

    L_GUT = (L_lo + L_hi) / mpf("2")
    at_GUT = _euler_two_loop(inv_a_start, b1loop, bij_mpf, L_GUT, n_steps)
    inv_a_GUT = (at_GUT[0] + at_GUT[1]) / mpf("2")

    inv_a_unified = [inv_a_GUT, inv_a_GUT, inv_a_GUT]
    at_MZ = _euler_two_loop(inv_a_unified, b1loop, bij_mpf, -L_GUT, n_steps)

    sin2_pred = at_MZ[1] / f2m(alpha_inv_f)
    sin2_meas = _mpf(db, "const.sin2_tW")
    miss_pct = abs(sin2_pred - sin2_meas) / sin2_meas * mpf("100")

    return {
        "sin2_pred": sin2_pred,
        "miss_pct": miss_pct,
        "L_GUT": L_GUT,
        "inv_a_GUT": inv_a_GUT,
    }


# ================================================================
# PREDICTION DISPLAY
# ================================================================

def show_prediction(name, pred_dict):
    """Print a prediction result dict in standard format.

    Usage: show_prediction("alpha_s 2L full", predict_alpha_s_2L(db))
    """
    print("  PREDICTION: %s" % name)
    for k, v in pred_dict.items():
        if isinstance(v, mpf):
            print("    %-20s = %s" % (k, mp.nstr(v, 7)))
        elif isinstance(v, Fraction):
            print("    %-20s = %s = %s" % (k, v, mp.nstr(f2m(v), 7)))
        else:
            print("    %-20s = %s" % (k, v))


def show_all_predictions(db, n_steps=500):
    """Run and display all predictions: alpha_s (1L, 2L SM, 2L full),
    sin2_tW (1L, 2L), Koide m_tau.

    This is the derivation summary table.
    """
    print("  PREDICTION SUMMARY (from db constants):")
    print("  %-35s %12s %12s" % ("Prediction", "Value", "Miss"))
    print("  %-35s %12s %12s" % ("-" * 35, "-" * 12, "-" * 12))

    as_1L = predict_alpha_s_1L(db)
    print("  %-35s %12s %12s" % ("alpha_s (one-loop CD)",
        mp.nstr(as_1L["alpha_s_pred"], 6),
        "%s%%" % mp.nstr(as_1L["miss_pct"], 4)))

    as_2L_SM = predict_alpha_s_2L(db, bij_tag="SM", n_steps=n_steps)
    print("  %-35s %12s %12s" % ("alpha_s (two-loop SM b_ij)",
        mp.nstr(as_2L_SM["alpha_s_pred"], 6),
        "%s%%" % mp.nstr(as_2L_SM["miss_pct"], 4)))

    as_2L_full = predict_alpha_s_2L(db, bij_tag="full", n_steps=n_steps)
    print("  %-35s %12s %12s" % ("alpha_s (two-loop full b_ij)",
        mp.nstr(as_2L_full["alpha_s_pred"], 6),
        "%s%%" % mp.nstr(as_2L_full["miss_pct"], 4)))

    sin2_1L = predict_sin2_1L(db)
    print("  %-35s %12s %12s" % ("sin2_tW (one-loop CD)",
        mp.nstr(sin2_1L["sin2_pred"], 6),
        "%s%%" % mp.nstr(sin2_1L["miss_pct"], 4)))

    sin2_2L = predict_sin2_2L(db, n_steps=n_steps)
    print("  %-35s %12s %12s" % ("sin2_tW (two-loop full)",
        mp.nstr(sin2_2L["sin2_pred"], 6),
        "%s%%" % mp.nstr(sin2_2L["miss_pct"], 4)))

    k = koide_predict(db)
    print("  %-35s %12s %12s" % ("m_tau (Koide K=2/3)",
        mp.nstr(k["m_tau_pred"], 7),
        "%s%%" % mp.nstr(k["miss_pct"], 4)))

    print()
    print("  %-35s %12s" % ("Measured alpha_s",
        mp.nstr(_mpf(db, "const.alpha_s"), 6)))
    print("  %-35s %12s" % ("Measured sin2_tW",
        mp.nstr(_mpf(db, "const.sin2_tW"), 6)))
    print("  %-35s %12s" % ("Measured m_tau (MeV)",
        mp.nstr(_mpf(db, "const.m_tau"), 7)))


# ================================================================
# KOIDE
# ================================================================

def koide_ratio_db(db, m1_id="const.m_e", m2_id="const.m_mu", m3_id="const.m_tau"):
    """Compute Koide ratio K = sum(m) / (sum(sqrt(m)))^2 from db masses.

    K = 2/3 for leptons (hypothesis).
    K = sum_m / (sum_sqrt)^2  (NOT (sum_sqrt)^2 / (3*sum_m)).
    """
    m1 = _mpf(db, m1_id)
    m2 = _mpf(db, m2_id)
    m3 = _mpf(db, m3_id)
    s1, s2, s3 = msqrt(m1), msqrt(m2), msqrt(m3)
    return (m1 + m2 + m3) / (s1 + s2 + s3) ** 2


def koide_amplitude_sq(K_val):
    """From K, compute a^2 = 2*(3*K - 1).

    At K = 2/3: a^2 = 2. The hypothesis.
    At measured K = 0.66666051: a^2 = 1.9999630688.
    """
    return mpf("2") * (mpf("3") * K_val - mpf("1"))


def koide_predict(db):
    """Predict m_tau from m_e and m_mu using K = 2/3.

    Derivation:
      K = 2/3 => x^2 - 4sx + (3S - 2s^2) = 0
      where s = sqrt(m_e) + sqrt(m_mu), S = m_e + m_mu, x = sqrt(m_tau).

    Returns: dict with m_tau_pred, miss_pct, other_root, K_computed, a_sq
    """
    m_e_f = _val(db, "const.m_e")
    m_mu_f = _val(db, "const.m_mu")
    m_tau_f = _val(db, "const.m_tau")

    s_e = msqrt(f2m(m_e_f))
    s_mu = msqrt(f2m(m_mu_f))
    s = s_e + s_mu
    S = f2m(m_e_f + m_mu_f)

    discriminant = mpf("6") * s * s - mpf("3") * S
    sqrt_disc = msqrt(discriminant)

    x_plus = mpf("2") * s + sqrt_disc
    x_minus = mpf("2") * s - sqrt_disc

    m_tau_pred = x_plus * x_plus
    m_tau_other = x_minus * x_minus

    K_computed = koide_ratio_db(db)
    a_sq = koide_amplitude_sq(K_computed)

    m_tau_meas = f2m(m_tau_f)
    miss_pct = abs(m_tau_pred - m_tau_meas) / m_tau_meas * mpf("100")

    return {
        "m_tau_pred": m_tau_pred,
        "miss_pct": miss_pct,
        "m_tau_other": m_tau_other,
        "K_computed": K_computed,
        "a_sq": a_sq,
        "a_sq_miss_from_2": abs(a_sq - mpf("2")),
    }


def show_koide(db):
    """Print Koide analysis for all three sectors."""
    print("  KOIDE ANALYSIS (from db masses):")
    print()

    for name, ids in [
        ("Leptons (e, mu, tau)", ("const.m_e", "const.m_mu", "const.m_tau")),
        ("Up quarks (u, c, t)", ("const.m_u", "const.m_c", "const.m_t")),
        ("Down quarks (d, s, b)", ("const.m_d", "const.m_s", "const.m_b")),
    ]:
        K = koide_ratio_db(db, ids[0], ids[1], ids[2])
        a2 = koide_amplitude_sq(K)
        print("    %s:" % name)
        print("      K = %s (2/3 = %s)" % (mp.nstr(K, 8), mp.nstr(mpf("2")/mpf("3"), 8)))
        print("      a^2 = %s (hypothesis: 2)" % mp.nstr(a2, 6))
        print()

    k = koide_predict(db)
    print("    m_tau prediction: %s MeV (miss %s%%)" % (
        mp.nstr(k["m_tau_pred"], 7), mp.nstr(k["miss_pct"], 4)))
    print("    Other root: %s MeV" % mp.nstr(k["m_tau_other"], 4))


# ================================================================
# BETA DECOMPOSITION
# ================================================================

def decompose_beta(db, beta_id):
    """Show the full decomposition of a beta coefficient from db.

    Usage: decompose_beta(db, "beta.b2_mod")
    """
    obj = db.get(beta_id)
    if obj is None:
        print("  Beta '%s' not found." % beta_id)
        return None

    result = {
        "name": obj.name,
        "gauge_group": obj.gauge_group,
        "total": obj.value,
        "gauge": obj.gauge_part,
        "fermion": obj.fermion_part,
        "higgs": obj.higgs_part,
        "bsm": obj.bsm_part,
    }

    # Verify sum
    parts = [p for p in [obj.gauge_part, obj.fermion_part, obj.higgs_part, obj.bsm_part]
             if p is not None]
    if parts:
        result["sum_parts"] = sum(parts)
        result["sum_matches"] = (sum(parts) == obj.value)

    return result


def show_beta_decomposition(db):
    """Print full decomposition of all 9 beta coefficients."""
    print("  BETA DECOMPOSITION:")
    print("  %-30s %8s %8s %8s %8s %8s %s" % (
        "Beta", "Total", "Gauge", "Ferm", "Higgs", "BSM", "Check"))
    print("  %-30s %8s %8s %8s %8s %8s %s" % (
        "-" * 30, "-" * 8, "-" * 8, "-" * 8, "-" * 8, "-" * 8, "-" * 5))

    for bid in ["beta.b1_SM", "beta.b2_SM", "beta.b3_SM",
                "beta.db1_VL", "beta.db2_VL", "beta.db3_VL",
                "beta.b1_mod", "beta.b2_mod", "beta.b3_mod"]:
        d = decompose_beta(db, bid)
        if d is None:
            continue
        check = "OK" if d.get("sum_matches") else "?"
        print("  %-30s %8s %8s %8s %8s %8s %s" % (
            d["name"],
            d["total"],
            d["gauge"] if d["gauge"] is not None else "—",
            d["fermion"] if d["fermion"] is not None else "—",
            d["higgs"] if d["higgs"] is not None else "—",
            d["bsm"] if d["bsm"] is not None else "—",
            check))


# ================================================================
# GROUP THEORY
# ================================================================

def casimir_adj(N):
    """C_2(adjoint SU(N)) = N. Exact Fraction."""
    return Fraction(N, 1)


def casimir_fund(N):
    """C_2(fundamental SU(N)) = (N^2-1)/(2N). Exact Fraction."""
    return Fraction(N * N - 1, 2 * N)


def dynkin_fund():
    """S_2(fundamental) = 1/2 for any SU(N). Exact."""
    return Fraction(1, 2)


def yang_mills_coefficient():
    """The 11/3 from one-loop gauge self-coupling."""
    return Fraction(11, 3)


def gauge_beta(N):
    """Pure gauge one-loop beta for SU(N): -(11/3)*N."""
    return Fraction(-11, 3) * Fraction(N, 1)


def generation_democracy_check(db):
    """Verify generation democracy: per-gen = (4/3, 4/3, 4/3) from reps.

    Sums the 5 SM chiral reps in the db.
    """
    sm_reps = ["rep.Q_L", "rep.u_R", "rep.d_R", "rep.L_L", "rep.e_R"]
    db1 = Fraction(0)
    db2 = Fraction(0)
    db3 = Fraction(0)

    for rid in sm_reps:
        r = db.get(rid)
        if r is None:
            continue
        db1 += r.db1
        db2 += r.db2
        db3 += r.db3

    democracy = (db1 == db2 == db3 == Fraction(4, 3))

    print("  GENERATION DEMOCRACY CHECK:")
    print("    Per-gen db: (%s, %s, %s)" % (db1, db2, db3))
    print("    Equal? %s" % democracy)
    print("    Value? %s" % ("4/3 = YES" if db1 == Fraction(4, 3) else "NOT 4/3"))
    return democracy


# ================================================================
# WHAT-IF: TEST ARBITRARY BSM REPRESENTATIONS
# ================================================================

def whatif_rep(db, name, su3_dim, su2_dim, Y, rep_type="vector-like"):
    """Test a hypothetical BSM representation against the measured gap ratio.

    Computes: modified betas, gap ratio, distance from measured.
    Does NOT add anything to the database.

    Usage: whatif_rep(db, "test (3,1,2/3)", 3, 1, Fraction(2,3))
    """
    from data_5_objects import Representation

    r = Representation("whatif.test", name, su3_dim, su2_dim, Y, rep_type)

    b1_new = _beta_val(db, "beta.b1_SM") + r.db1
    b2_new = _beta_val(db, "beta.b2_SM") + r.db2
    b3_new = _beta_val(db, "beta.b3_SM") + r.db3

    gap_new = (b1_new - b2_new) / (b2_new - b3_new)
    gap_meas = gap_ratio_measured(db)

    dist = abs(f2m(gap_new) - f2m(gap_meas))
    dist_pct = dist / f2m(gap_meas) * mpf("100")

    gap_cd = f2m(_val(db, "const.gap_VL"))
    dist_cd = abs(gap_cd - f2m(gap_meas))

    return {
        "name": name,
        "rep": (su3_dim, su2_dim, Y),
        "rep_type": rep_type,
        "db": (r.db1, r.db2, r.db3),
        "betas_new": (b1_new, b2_new, b3_new),
        "gap": gap_new,
        "gap_decimal": f2m(gap_new),
        "distance": dist,
        "distance_pct": dist_pct,
        "closer_than_CD": dist < dist_cd,
    }


def whatif_scan(db, candidates=None):
    """Scan multiple BSM candidates and rank by gap ratio distance.

    Default candidates: the PHYS-14 enumeration.

    Usage: whatif_scan(db)
    """
    if candidates is None:
        candidates = [
            ("(3,2,1/6) CD",      3, 2, Fraction(1, 6)),
            ("(3,1,2/3) u'-type", 3, 1, Fraction(2, 3)),
            ("(3,1,-1/3) d'-type", 3, 1, Fraction(-1, 3)),
            ("(1,2,1/2) L'-type", 1, 2, Fraction(1, 2)),
            ("(3,2,7/6) exotic",  3, 2, Fraction(7, 6)),
            ("(3,3,1/3) triplet", 3, 3, Fraction(1, 3)),
        ]

    results = []
    for name, d3, d2, Y in candidates:
        r = whatif_rep(db, name, d3, d2, Y)
        results.append(r)

    results.sort(key=lambda x: float(x["distance"]))

    print("  BSM CANDIDATE SCAN (ranked by gap ratio distance):")
    print("  %-25s %-10s %-15s %-10s %s" % (
        "Candidate", "Gap", "Fraction", "Dist%%", "Beats CD?"))
    print("  %-25s %-10s %-15s %-10s %s" % (
        "-" * 25, "-" * 10, "-" * 15, "-" * 10, "-" * 9))

    for r in results:
        print("  %-25s %-10s %-15s %-10s %s" % (
            r["name"],
            mp.nstr(r["gap_decimal"], 6),
            r["gap"],
            mp.nstr(r["distance_pct"], 4),
            "YES" if r["closer_than_CD"] else "no"))

    print()
    print("  Measured gap: %s" % mp.nstr(f2m(gap_ratio_measured(db)), 6))
    print("  Winner: %s" % results[0]["name"])

    return results


def whatif_custom_betas(db, b1_new, b2_new, b3_new, name="custom"):
    """Test arbitrary beta coefficients against unification.

    Returns gap ratio, alpha_s prediction (1L), distance from measured.
    """
    gap_new = (b1_new - b2_new) / (b2_new - b3_new)
    gap_meas = gap_ratio_measured(db)
    dist = abs(f2m(gap_new) - f2m(gap_meas))

    # One-loop alpha_s prediction with these betas
    c = extract_couplings(db)
    L_GUT = f2m((c["inv_a1"] - c["inv_a2"]) / (b1_new - b2_new))
    inv_a_GUT = c["inv_a1_mpf"] - f2m(b1_new) * L_GUT
    inv_a3_pred = inv_a_GUT + f2m(b3_new) * L_GUT
    alpha_s_pred = mpf("1") / inv_a3_pred

    alpha_s_meas = _mpf(db, "const.alpha_s")
    miss_pct = abs(alpha_s_pred - alpha_s_meas) / alpha_s_meas * mpf("100")

    return {
        "name": name,
        "betas": (b1_new, b2_new, b3_new),
        "gap": gap_new,
        "gap_distance": dist,
        "alpha_s_pred": alpha_s_pred,
        "alpha_s_miss_pct": miss_pct,
        "L_GUT": L_GUT,
    }

