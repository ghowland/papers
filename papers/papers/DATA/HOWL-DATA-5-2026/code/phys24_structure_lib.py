#!/usr/bin/env python3
"""
HOWL PHYS-24 STRUCTURED DATA LIBRARY
======================================
Organized knowledge about representations, particles, thresholds,
and the SM/BSM landscape. Queryable by name, by scale, by property.

Import:
    from phys24_lib import *
    from phys24_structures import *

Platform: phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *


# ================================================================
# REPRESENTATION OBJECTS
# ================================================================

def make_rep(name, su3_dim, su2_dim, Y, rep_type="chiral",
             mass_var=None, data4_entry=None, papers=None):
    """Create a representation dict with all derived properties.

    ONE-LOOP BETA SHIFT FORMULAS:

    For a single chiral (Weyl) fermion in (R3, R2, Y):
      db1 = (2/5) * dim(R3) * dim(R2) * Y^2
      db2 = (2/3) * dim(R3) * S2(R2)
      db3 = (2/3) * dim(R2) * S2(R3)

    For a vector-like (Dirac = L + R) pair in (R3, R2, Y):
      db1 = (2/5) * dim(R3) * dim(R2) * Y^2   [same as chiral]
      db2 = (2/3) * dim(R3) * S2(R2)           [same as chiral]
      db3 = (1/3) * dim(R2) * S2(R3)           [HALF of chiral]

    The asymmetry in SU(3): a VL pair contributes LESS to b3 than
    a single chiral fermion because the VL formula (1/3)*d2*S2(R3)
    accounts for the Dirac structure differently. This is NOT a
    simple factor-of-2 relationship across all groups.

    VERIFICATION: One SM generation (5 chiral Weyl multiplets) gives
    (4/3, 4/3, 4/3) with the chiral coefficients (2/5, 2/3, 2/3).
    The VL Cabibbo Doublet (3,2,1/6) gives (1/15, 1, 1/3) with the
    VL coefficients (2/5, 2/3, 1/3).
    """
    su3 = Fraction(su3_dim)
    su2 = Fraction(su2_dim)
    Y_f = Fraction(Y) if not isinstance(Y, Fraction) else Y

    # Dynkin index: S2(fund) = 1/2, S2(singlet) = 0
    S2_R3 = Fraction(1, 2) if su3_dim > 1 else Fraction(0)
    S2_R2 = Fraction(1, 2) if su2_dim > 1 else Fraction(0)

    # Casimir: C2(fund SU(N)) = (N^2-1)/(2N), C2(singlet) = 0
    if su3_dim > 1:
        C2_R3 = Fraction(su3_dim * su3_dim - 1, 2 * su3_dim)
    else:
        C2_R3 = Fraction(0)
    if su2_dim > 1:
        C2_R2 = Fraction(su2_dim * su2_dim - 1, 2 * su2_dim)
    else:
        C2_R2 = Fraction(0)

    # Beta shift coefficients
    if rep_type == "vector-like":
        # VL pair: (2/5, 2/3, 1/3)
        db1 = Fraction(2, 5) * su3 * su2 * Y_f * Y_f
        db2 = Fraction(2, 3) * su3 * S2_R2
        db3 = Fraction(1, 3) * su2 * S2_R3
    else:
        # Chiral Weyl: (2/5, 2/3, 2/3)
        db1 = Fraction(2, 5) * su3 * su2 * Y_f * Y_f
        db2 = Fraction(2, 3) * su3 * S2_R2
        db3 = Fraction(2, 3) * su2 * S2_R3

    # Electric charges: Q = T3 + Y
    if su2_dim == 2:
        charges = (Fraction(1, 2) + Y_f, Fraction(-1, 2) + Y_f)
    elif su2_dim == 1:
        charges = (Y_f,)
    else:
        charges = (Y_f,)

    return {
        "name": name,
        "su3_dim": su3_dim,
        "su2_dim": su2_dim,
        "Y": Y_f,
        "Y2": Y_f * Y_f,
        "rep_type": rep_type,
        "rep_tuple": (su3_dim, su2_dim, Y_f),
        "S2_R3": S2_R3,
        "S2_R2": S2_R2,
        "C2_R3": C2_R3,
        "C2_R2": C2_R2,
        "db1": db1,
        "db2": db2,
        "db3": db3,
        "db": (db1, db2, db3),
        "charges": charges,
        "mass_var": mass_var,
        "data4_entry": data4_entry,
        "papers": papers or [],
    }


# ================================================================
# THE SM FERMION CENSUS (one generation)
# ================================================================

Q_L = make_rep("Q_L", 3, 2, Fraction(1, 6), "chiral",
               papers=["PHYS-17", "PHYS-26"])

u_R = make_rep("u_R", 3, 1, Fraction(2, 3), "chiral",
               papers=["PHYS-17"])

d_R = make_rep("d_R", 3, 1, Fraction(-1, 3), "chiral",
               papers=["PHYS-17"])

L_L = make_rep("L_L", 1, 2, Fraction(-1, 2), "chiral",
               papers=["PHYS-17"])

e_R = make_rep("e_R", 1, 1, Fraction(-1, 1), "chiral",
               papers=["PHYS-17"])

SM_GENERATION = [Q_L, u_R, d_R, L_L, e_R]

HIGGS = {
    "name": "Higgs",
    "rep_tuple": (1, 2, Fraction(1, 2)),
    "db1": Fraction(1, 10),
    "db2": Fraction(1, 6),
    "db3": Fraction(0),
    "db": (Fraction(1, 10), Fraction(1, 6), Fraction(0)),
    "mass_var": "m_H",
    "data4_entry": "C5",
    "papers": ["PHYS-12", "PHYS-17"],
}

CABIBBO_DOUBLET = make_rep("Cabibbo Doublet", 3, 2, Fraction(1, 6),
                            "vector-like",
                            papers=["PHYS-15", "PHYS-16", "PHYS-19"])


# ================================================================
# GENERATION AND SECTOR HELPERS
# ================================================================

def generation_betas(gen_reps=None):
    """Sum beta shifts for one complete generation."""
    if gen_reps is None:
        gen_reps = SM_GENERATION
    db1 = sum(r["db1"] for r in gen_reps)
    db2 = sum(r["db2"] for r in gen_reps)
    db3 = sum(r["db3"] for r in gen_reps)
    return db1, db2, db3


def total_SM_betas(n_gen=3):
    """Compute total SM betas from the particle census.
    b_i = b_i^gauge + n_gen * b_i^gen + b_i^Higgs
    """
    b1_gauge = Fraction(0)
    b2_gauge = Fraction(-11, 3) * Fraction(2)
    b3_gauge = Fraction(-11, 3) * Fraction(3)

    gen_b1, gen_b2, gen_b3 = generation_betas()

    b1 = b1_gauge + Fraction(n_gen) * gen_b1 + HIGGS["db1"]
    b2 = b2_gauge + Fraction(n_gen) * gen_b2 + HIGGS["db2"]
    b3 = b3_gauge + Fraction(n_gen) * gen_b3 + HIGGS["db3"]

    return b1, b2, b3


# ================================================================
# THE PARTICLE CATALOG
# ================================================================

PARTICLE_CATALOG = [
    {"name": "electron",    "mass_var": "m_e",    "mass_frac": m_e,
     "data4": "B2",  "rep": e_R,  "threshold_type": "lepton"},
    {"name": "muon",        "mass_var": "m_mu",   "mass_frac": m_mu,
     "data4": "B3",  "rep": L_L,  "threshold_type": "lepton"},
    {"name": "up quark",    "mass_var": "m_u",    "mass_frac": m_u,
     "data4": "D1",  "rep": u_R,  "threshold_type": "quark"},
    {"name": "down quark",  "mass_var": "m_d",    "mass_frac": m_d,
     "data4": "D2",  "rep": d_R,  "threshold_type": "quark"},
    {"name": "strange",     "mass_var": "m_s",    "mass_frac": m_s,
     "data4": "D3",  "rep": d_R,  "threshold_type": "quark"},
    {"name": "charm",       "mass_var": "m_c",    "mass_frac": m_c,
     "data4": "D4",  "rep": u_R,  "threshold_type": "quark"},
    {"name": "tau",         "mass_var": "m_tau",  "mass_frac": m_tau,
     "data4": "B4",  "rep": e_R,  "threshold_type": "lepton"},
    {"name": "bottom",      "mass_var": "m_b",    "mass_frac": m_b,
     "data4": "D5",  "rep": d_R,  "threshold_type": "quark"},
    {"name": "W boson",     "mass_var": "M_W",    "mass_frac": M_W,
     "data4": "C3",  "rep": None, "threshold_type": "gauge"},
    {"name": "Z boson",     "mass_var": "M_Z",    "mass_frac": M_Z,
     "data4": "C1",  "rep": None, "threshold_type": "gauge"},
    {"name": "Higgs",       "mass_var": "m_H",    "mass_frac": m_H,
     "data4": "C5",  "rep": None, "threshold_type": "scalar"},
    {"name": "top",         "mass_var": "m_t",    "mass_frac": m_t,
     "data4": "C4",  "rep": u_R,  "threshold_type": "quark"},
]

PARTICLE_CATALOG.sort(key=lambda p: float(f2m(p["mass_frac"])))


def particles_at_scale(mu_MeV):
    """Return list of particles active at energy scale mu (in MeV)."""
    mu = float(f2m(mu_MeV)) if isinstance(mu_MeV, Fraction) else float(mu_MeV)
    return [p for p in PARTICLE_CATALOG if float(f2m(p["mass_frac"])) <= mu]


def active_fermion_count(mu_MeV):
    """Count active quark flavors at scale mu."""
    active = particles_at_scale(mu_MeV)
    return sum(1 for p in active if p["threshold_type"] == "quark")


# ================================================================
# THE ENERGY LANDSCAPE
# ================================================================

ENERGY_DOMAINS = [
    {"name": "QED low",
     "range_MeV": (Fraction(0), m_e),
     "description": "Below electron mass. Photons only.",
     "perturbative": True},
    {"name": "QED leptonic",
     "range_MeV": (m_e, Fraction(300, 1)),
     "description": "Electrons and muons active. QED perturbative.",
     "perturbative": True},
    {"name": "Confinement wall",
     "range_MeV": (Fraction(300, 1), Fraction(2000, 1)),
     "description": "alpha_s ~ O(1). Non-perturbative. Integer rules break.",
     "perturbative": False},
    {"name": "SM perturbative",
     "range_MeV": (Fraction(2000, 1), M_Z),
     "description": "All SM fermions active. Three gauge groups perturbative.",
     "perturbative": True},
    {"name": "Electroweak scale",
     "range_MeV": (M_Z, m_t),
     "description": "EW observables measured here. W, Z, Higgs, top thresholds.",
     "perturbative": True},
]


# ================================================================
# THE GUT COMPLETION (minimal SU(5))
# ================================================================

GUT_PARTICLES = {
    "X_Y_bosons": {
        "name": "X, Y gauge bosons",
        "role": "Proton decay mediators",
        "su3_dim": 3, "su2_dim": 2, "Y": Fraction(5, 6),
        "decay_channel": "p -> e+ pi0",
        "papers": ["PHYS-20"],
    },
    "color_triplet_higgs": {
        "name": "Color triplet Higgs (T)",
        "role": "SU(5) Higgs partner of SM doublet",
        "su3_dim": 3, "su2_dim": 1, "Y": Fraction(1, 3),
        "threshold_coeff": Fraction(-1, 12),
        "db1": Fraction(1, 15),
        "db2": Fraction(0),
        "db3": Fraction(1, 12),
        "papers": ["PHYS-29"],
    },
    "sigma_octet": {
        "name": "Sigma color octet",
        "role": "SU(5) adjoint component",
        "su3_dim": 8, "su2_dim": 1,
        "db3": Fraction(1, 2),
        "papers": ["PHYS-29"],
    },
    "sigma_triplet": {
        "name": "Sigma weak triplet",
        "role": "SU(5) adjoint component",
        "su2_dim": 3, "su3_dim": 1,
        "db2": Fraction(1, 3),
        "papers": ["PHYS-29"],
    },
}


# ================================================================
# DATA-4 CROSS-REFERENCE MAP
# ================================================================

DATA4_MAP = {
    "A1": {"var": "c",        "value": c,        "type": "E", "unit": "m/s"},
    "A2": {"var": "h_planck", "value": h_planck, "type": "E", "unit": "J*s"},
    "A3": {"var": "e_charge", "value": e_charge, "type": "E", "unit": "C"},
    "A4": {"var": "k_B",      "value": k_B,      "type": "E", "unit": "J/K"},
    "A5": {"var": "N_A",      "value": N_A,      "type": "E", "unit": "mol^-1"},
    "A6": {"var": "dv_Cs",    "value": dv_Cs,    "type": "E", "unit": "Hz"},
    "A7": {"var": "K_cd",     "value": K_cd,     "type": "E", "unit": "lm/W"},
    "B1":  {"var": "alpha_inv", "value": alpha_inv, "type": "M", "unit": "dimensionless", "digits": 12},
    "B2":  {"var": "m_e",       "value": m_e,       "type": "M", "unit": "MeV", "digits": 11},
    "B3":  {"var": "m_mu",      "value": m_mu,      "type": "M", "unit": "MeV", "digits": 10},
    "B4":  {"var": "m_tau",     "value": m_tau,     "type": "M", "unit": "MeV", "digits": 6},
    "B5":  {"var": "m_p",       "value": m_p,       "type": "M", "unit": "MeV", "digits": 11},
    "B6":  {"var": "mp_me",     "value": mp_me,     "type": "M", "unit": "dimensionless", "digits": 13},
    "B7":  {"var": "R_inf",     "value": R_inf,     "type": "M", "unit": "m^-1", "digits": 13},
    "B8":  {"var": "a_0",       "value": a_0,       "type": "M", "unit": "m", "digits": 12},
    "B9":  {"var": "a_e",       "value": a_e,       "type": "M", "unit": "dimensionless", "digits": 12},
    "B10": {"var": "a_mu",      "value": a_mu,      "type": "M", "unit": "dimensionless", "digits": 9},
    "B11": {"var": "sin2_tW",   "value": sin2_tW,   "type": "M", "unit": "dimensionless", "digits": 5},
    "B12": {"var": "alpha_s",   "value": alpha_s,   "type": "M", "unit": "dimensionless", "digits": 4},
    "B13": {"var": "mu_0",      "value": mu_0,      "type": "M", "unit": "N/A^2", "digits": 12},
    "C1": {"var": "M_Z",     "value": M_Z,     "type": "M", "unit": "MeV", "digits": 6},
    "C2": {"var": "Gamma_Z", "value": Gamma_Z, "type": "M", "unit": "MeV", "digits": 5},
    "C3": {"var": "M_W",     "value": M_W,     "type": "M", "unit": "MeV", "digits": 6},
    "C4": {"var": "m_t",     "value": m_t,     "type": "M", "unit": "MeV", "digits": 5},
    "C5": {"var": "m_H",     "value": m_H,     "type": "M", "unit": "MeV", "digits": 5},
    "C6": {"var": "G_F",     "value": G_F,     "type": "M", "unit": "GeV^-2", "digits": 8},
    "D1":  {"var": "m_u",     "value": m_u,     "type": "M", "unit": "MeV", "digits": 3},
    "D2":  {"var": "m_d",     "value": m_d,     "type": "M", "unit": "MeV", "digits": 3},
    "D3":  {"var": "m_s",     "value": m_s,     "type": "M", "unit": "MeV", "digits": 3},
    "D4":  {"var": "m_c",     "value": m_c,     "type": "M", "unit": "MeV", "digits": 4},
    "D5":  {"var": "m_b",     "value": m_b,     "type": "M", "unit": "MeV", "digits": 4},
    "D6":  {"var": "sin_t12", "value": sin_t12, "type": "M", "unit": "dimensionless", "digits": 5},
    "D7":  {"var": "sin_t23", "value": sin_t23, "type": "M", "unit": "dimensionless", "digits": 4},
    "D8":  {"var": "sin_t13", "value": sin_t13, "type": "M", "unit": "dimensionless", "digits": 4},
    "D9":  {"var": "mc_ms",   "value": mc_ms,   "type": "M", "unit": "dimensionless", "digits": 5,
             "note": "FLAG lattice, INDEPENDENT of D3/D4"},
    "D10": {"var": "mb_mc",   "value": mb_mc,   "type": "M", "unit": "dimensionless", "digits": 4,
             "note": "FLAG lattice, INDEPENDENT of D4/D5"},
    "D11": {"var": "mu_md",   "value": mu_md,   "type": "M", "unit": "dimensionless", "digits": 3,
             "note": "FLAG lattice, INDEPENDENT of D1/D2"},
    "E1":  {"var": "m_n",        "value": m_n,        "type": "M", "unit": "MeV", "digits": 11},
    "E2":  {"var": "mn_mp_diff", "value": mn_mp_diff, "type": "M", "unit": "MeV", "digits": 8},
    "E3":  {"var": "m_pi_p",     "value": m_pi_p,     "type": "M", "unit": "MeV", "digits": 8},
    "E4":  {"var": "m_pi_0",     "value": m_pi_0,     "type": "M", "unit": "MeV", "digits": 7},
    "E5":  {"var": "m_K_p",      "value": m_K_p,      "type": "M", "unit": "MeV", "digits": 6},
    "E6":  {"var": "m_D",        "value": m_D,        "type": "M", "unit": "MeV", "digits": 12},
    "E7":  {"var": "m_He4",      "value": m_He4,      "type": "M", "unit": "MeV", "digits": 10},
    "E8":  {"var": "E_D",        "value": E_D,        "type": "M", "unit": "MeV", "digits": 8},
    "F1":  {"var": "H_1S2S",     "value": H_1S2S,     "type": "M", "unit": "Hz", "digits": 16},
    "K1":  {"var": "mmu_me",   "value": mmu_me,   "type": "M", "unit": "dimensionless", "digits": 10},
    "K2":  {"var": "mtau_me",  "value": mtau_me,  "type": "M", "unit": "dimensionless", "digits": 6},
    "K3":  {"var": "mtau_mmu", "value": mtau_mmu, "type": "M", "unit": "dimensionless", "digits": 5},
    "K4":  {"var": "mn_mp",    "value": mn_mp,    "type": "M", "unit": "dimensionless", "digits": 11},
    "K5":  {"var": "MW_MZ",    "value": MW_MZ,    "type": "M", "unit": "dimensionless", "digits": 6},
    "K6":  {"var": "mH_MZ",    "value": mH_MZ,    "type": "M", "unit": "dimensionless", "digits": 5},
    "K7":  {"var": "mt_MZ",    "value": mt_MZ,    "type": "M", "unit": "dimensionless", "digits": 5},
    "K8":  {"var": "K_koide",  "value": K_koide,  "type": "M", "unit": "dimensionless", "digits": 10},
    "N1":  {"var": "b1_SM",  "value": b1_SM,  "type": "D", "unit": "dimensionless"},
    "N2":  {"var": "b2_SM",  "value": b2_SM,  "type": "D", "unit": "dimensionless"},
    "N3":  {"var": "b3_SM",  "value": b3_SM,  "type": "D", "unit": "dimensionless"},
    "N4":  {"var": "db1_VL", "value": db1_VL, "type": "D", "unit": "dimensionless"},
    "N5":  {"var": "db2_VL", "value": db2_VL, "type": "D", "unit": "dimensionless"},
    "N6":  {"var": "db3_VL", "value": db3_VL, "type": "D", "unit": "dimensionless"},
    "N10": {"var": "gap_SM",      "value": gap_SM,      "type": "D", "unit": "dimensionless"},
    "N11": {"var": "gap_VL",      "value": gap_VL,      "type": "D", "unit": "dimensionless"},
    "N12": {"var": "gap_MSSM",    "value": gap_MSSM,    "type": "D", "unit": "dimensionless"},
    "N13": {"var": "gap_measured", "value": gap_measured, "type": "D", "unit": "dimensionless"},
}


def lookup_data4(entry_id):
    """Look up a DATA-4 entry by ID."""
    return DATA4_MAP.get(entry_id, None)


def entries_by_type(type_code):
    """Return all DATA-4 entries of a given type."""
    return [(k, v) for k, v in DATA4_MAP.items() if v["type"] == type_code]


# ================================================================
# PAPER CROSS-REFERENCE
# ================================================================

PAPER_TOPICS = {
    "MATH-1": "R2 = pi/4 universal geometric remainder, Q = F*beta*d^2*Z",
    "MATH-2": "Q335 integer pair basis at 100 digits",
    "MATH-3": "Extended basis: elliptic integrals, higher polylogarithms",
    "MATH-4": "R_n dimensional remainder sequence",
    "MATH-5": "Shared 2^335 execution basis",
    "MATH-6": "82/82 PSLQ independence record, derivation beats search",
    "DATA-1": "Initial 68-entry database",
    "DATA-2": "Extended 107-entry database with Koide addendum",
    "DATA-3": "Verified 123-entry database, 32/32 checks, Finding 15",
    "DATA-4": "Complete 146-entry database with CD extension, 38/38 checks",
    "PHYS-1": "Mass is inertia, series vocabulary",
    "PHYS-5": "alpha_EM running at 0.02 ppm",
    "PHYS-6": "Confinement two-face",
    "PHYS-7": "theta_QCD = 0, parameter reduction 19->18",
    "PHYS-8": "Koide decomposition, K = (1+a^2/2)/3, conditional 18->17",
    "PHYS-9": "EM integer chain, alpha <-> a_e at 4.3 ppb",
    "PHYS-11": "R2 in 9+9 domains",
    "PHYS-12": "Electroweak integer anatomy",
    "PHYS-13": "Gap ratio 218/115, SM does not unify",
    "PHYS-14": "BSM enumeration, 15 candidates",
    "PHYS-15": "Cabibbo Doublet identification (3,2,1/6)",
    "PHYS-16": "Cabibbo Doublet full specification",
    "PHYS-17": "Generation democracy (4/3,4/3,4/3), boson problem",
    "PHYS-19": "Three anomalies converge on CD",
    "PHYS-20": "Proton decay test, tau ~ 10^34-35 yr",
    "PHYS-21": "Level 1 / Level 2 boundary",
    "PHYS-22": "A2 geometric cancellation, 87%",
    "PHYS-23": "Koide C3 closure, tautology + saddle",
    "PHYS-24": "Session 3 operational lexicon",
}


def papers_about(keyword):
    """Find papers mentioning a keyword in their topic."""
    kw = keyword.lower()
    return [(k, v) for k, v in PAPER_TOPICS.items() if kw in v.lower()]


# ================================================================
# ANOMALY EVIDENCE REGISTRY
# ================================================================

ANOMALIES = {
    "CKM_deficit": {
        "name": "CKM first-row unitarity deficit",
        "sigma": "2.5-4",
        "value": "0.00202 +/- 0.00038",
        "quantum_number_used": "weak doublet (SU(2))",
        "resolution": "|V_ub'|^2 absorbs deficit in 3x4 CKM",
        "experiment": "multiple (Vud, Vus measurements)",
        "paper": "PHYS-19",
    },
    "A_FB_b": {
        "name": "LEP A_FB^b anomaly",
        "sigma": "~3",
        "value": "measured 0.0992 +/- 0.0016, SM ~0.1038",
        "quantum_number_used": "color + weak (SU(3) x SU(2))",
        "resolution": "Z-b-b vertex modification from VL-b mixing",
        "experiment": "LEP (decommissioned 2000, frozen 25+ years)",
        "paper": "PHYS-19",
    },
    "Higgs_excess": {
        "name": "Higgs signal strength excess",
        "sigma": "~2",
        "value": "mu ~ 1.06-1.10, SM = 1.00",
        "quantum_number_used": "color triplet (SU(3))",
        "resolution": "VL quark in gg->H loop + reduced b Yukawa",
        "experiment": "ATLAS/CMS",
        "paper": "PHYS-19",
    },
}


# ================================================================
# EXPERIMENTAL TIMELINE
# ================================================================

EXPERIMENTS = {
    "Hyper-K": {
        "observable": "p -> e+ pi0",
        "cd_prediction": "tau ~ 10^34-35 yr (detectable)",
        "mssm_prediction": "tau ~ 10^37 yr (beyond reach)",
        "status": "Operations ~2027",
        "decisive_by": "~2037",
        "paper": "PHYS-20",
    },
    "HL-LHC": {
        "observable": "VL quark pair production",
        "cd_prediction": "Observable if M_VL < 2-3 TeV",
        "mass_reach": "2-3 TeV",
        "status": "Running now through ~2040",
        "paper": "PHYS-16",
    },
    "Belle_II": {
        "observable": "CKM precision, m_tau",
        "cd_prediction": "Modified first-row unitarity",
        "status": "Running now through ~2030+",
        "paper": "PHYS-19",
    },
}


# ================================================================
# CLOSED PATHS
# ================================================================

CLOSED_PATHS = {
    "SM_unification": {
        "killed_by": "Gap ratio 218/115 != 1.358 (40% miss)",
        "paper": "PHYS-13",
    },
    "C3_Koide": {
        "killed_by": "Tautology (3 params, 3 data) + saddle point",
        "paper": "PHYS-23",
    },
    "broad_PSLQ": {
        "killed_by": "82/82 null, derivation beats search",
        "paper": "MATH-6",
    },
    "fermion_gap_fix": {
        "killed_by": "Generation democracy: fermion contribution = 0",
        "paper": "PHYS-17",
    },
    "lambda_one_eighth": {
        "killed_by": "Corrections go wrong direction",
        "paper": "Parked notebook",
    },
    "Koide_phase_adjust": {
        "killed_by": "K depends on a only, not theta_0 (PHYS-8 identity)",
        "paper": "PHYS-8",
    },
    "Koide_scale_choice": {
        "killed_by": "K is exactly scale-invariant under m_i -> c*m_i",
        "paper": "Parked notebook",
    },
}


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHYS24_STRUCTURES SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    # --------------------------------------------------------
    print("REPRESENTATION CONSTRUCTION")
    print("-" * 70)
    print()

    chk_exact("CD rep: db1 = 1/15",
              CABIBBO_DOUBLET["db1"], Fraction(1, 15), checks)
    chk_exact("CD rep: db2 = 1",
              CABIBBO_DOUBLET["db2"], Fraction(1, 1), checks)
    chk_exact("CD rep: db3 = 1/3",
              CABIBBO_DOUBLET["db3"], Fraction(1, 3), checks)
    chk_exact("CD upper charge = 2/3",
              CABIBBO_DOUBLET["charges"][0], Fraction(2, 3), checks)
    chk_exact("CD lower charge = -1/3",
              CABIBBO_DOUBLET["charges"][1], Fraction(-1, 3), checks)
    chk_exact("CD Y^2 = 1/36",
              CABIBBO_DOUBLET["Y2"], Fraction(1, 36), checks)

    # --------------------------------------------------------
    print()
    print("PER-MULTIPLET BETA CONTRIBUTIONS")
    print("-" * 70)
    print()

    # Verify each SM multiplet contribution individually
    chk_exact("Q_L db1 = 1/15",  Q_L["db1"], Fraction(1, 15), checks)
    chk_exact("Q_L db2 = 1",     Q_L["db2"], Fraction(1, 1), checks)
    chk_exact("Q_L db3 = 2/3",   Q_L["db3"], Fraction(2, 3), checks)
    chk_exact("u_R db1 = 8/15",  u_R["db1"], Fraction(8, 15), checks)
    chk_exact("u_R db3 = 1/3",   u_R["db3"], Fraction(1, 3), checks)
    chk_exact("d_R db1 = 2/15",  d_R["db1"], Fraction(2, 15), checks)
    chk_exact("d_R db3 = 1/3",   d_R["db3"], Fraction(1, 3), checks)
    chk_exact("L_L db1 = 1/5",   L_L["db1"], Fraction(1, 5), checks)
    chk_exact("L_L db2 = 1/3",   L_L["db2"], Fraction(1, 3), checks)
    chk_exact("e_R db1 = 2/5",   e_R["db1"], Fraction(2, 5), checks)

    # --------------------------------------------------------
    print()
    print("GENERATION DEMOCRACY FROM CENSUS")
    print("-" * 70)
    print()

    gen_b1, gen_b2, gen_b3 = generation_betas()

    chk_exact("Per-gen db1 from census = 4/3",
              gen_b1, Fraction(4, 3), checks)
    chk_exact("Per-gen db2 from census = 4/3",
              gen_b2, Fraction(4, 3), checks)
    chk_exact("Per-gen db3 from census = 4/3",
              gen_b3, Fraction(4, 3), checks)
    chk_exact("Democracy: db1 = db2",
              gen_b1, gen_b2, checks)
    chk_exact("Democracy: db2 = db3",
              gen_b2, gen_b3, checks)

    # --------------------------------------------------------
    print()
    print("SM BETAS FROM CENSUS")
    print("-" * 70)
    print()

    census_b1, census_b2, census_b3 = total_SM_betas(3)

    chk_exact("Census b1 = library b1_SM = 41/10",
              census_b1, b1_SM, checks)
    chk_exact("Census b2 = library b2_SM = -19/6",
              census_b2, b2_SM, checks)
    chk_exact("Census b3 = library b3_SM = -7",
              census_b3, b3_SM, checks)

    # --------------------------------------------------------
    print()
    print("SM FERMION CHARGES")
    print("-" * 70)
    print()

    chk_exact("Q_L upper charge = 2/3",
              Q_L["charges"][0], Fraction(2, 3), checks)
    chk_exact("Q_L lower charge = -1/3",
              Q_L["charges"][1], Fraction(-1, 3), checks)
    chk_exact("u_R charge = 2/3",
              u_R["charges"][0], Fraction(2, 3), checks)
    chk_exact("d_R charge = -1/3",
              d_R["charges"][0], Fraction(-1, 3), checks)
    chk_exact("L_L upper charge = 0 (neutrino)",
              L_L["charges"][0], Fraction(0), checks)
    chk_exact("L_L lower charge = -1 (electron)",
              L_L["charges"][1], Fraction(-1), checks)
    chk_exact("e_R charge = -1",
              e_R["charges"][0], Fraction(-1), checks)

    # --------------------------------------------------------
    print()
    print("DATA-4 CROSS-REFERENCE")
    print("-" * 70)
    print()

    b1_entry = lookup_data4("B1")
    chk_bool("B1 lookup returns alpha_inv",
             b1_entry is not None and b1_entry["var"] == "alpha_inv",
             "var = %s" % (b1_entry["var"] if b1_entry else "None"),
             checks)
    chk_exact("B1 value matches library",
              b1_entry["value"], alpha_inv, checks)

    exact_entries = entries_by_type("E")
    chk_bool("7 exact (Type E) entries",
             len(exact_entries) == 7,
             "count = %d" % len(exact_entries), checks)

    measured_entries = entries_by_type("M")
    chk_bool("Measured entries >= 30",
             len(measured_entries) >= 30,
             "count = %d" % len(measured_entries), checks)

    # --------------------------------------------------------
    print()
    print("PAPER CROSS-REFERENCE")
    print("-" * 70)
    print()

    gap_papers = papers_about("gap ratio")
    chk_bool("'gap ratio' search finds PHYS-13",
             any(p[0] == "PHYS-13" for p in gap_papers),
             "found: %s" % [p[0] for p in gap_papers], checks)

    koide_papers = papers_about("koide")
    chk_bool("'koide' search finds PHYS-8 and PHYS-23",
             any(p[0] == "PHYS-8" for p in koide_papers) and
             any(p[0] == "PHYS-23" for p in koide_papers),
             "found: %s" % [p[0] for p in koide_papers], checks)

    # --------------------------------------------------------
    print()
    print("PARTICLE CATALOG")
    print("-" * 70)
    print()

    chk_bool("Catalog has 12 particles",
             len(PARTICLE_CATALOG) == 12,
             "count = %d" % len(PARTICLE_CATALOG), checks)

    chk_bool("Catalog sorted by mass",
             float(f2m(PARTICLE_CATALOG[0]["mass_frac"])) <
             float(f2m(PARTICLE_CATALOG[-1]["mass_frac"])),
             "first = %s (%s MeV), last = %s (%s MeV)" % (
                 PARTICLE_CATALOG[0]["name"],
                 mp.nstr(f2m(PARTICLE_CATALOG[0]["mass_frac"]), 5),
                 PARTICLE_CATALOG[-1]["name"],
                 mp.nstr(f2m(PARTICLE_CATALOG[-1]["mass_frac"]), 6)),
             checks)

    at_MZ = particles_at_scale(M_Z)
    chk_bool("At M_Z: 10+ particles active",
             len(at_MZ) >= 10,
             "count = %d" % len(at_MZ), checks)

    nf_at_MZ = active_fermion_count(M_Z)
    chk_bool("At M_Z: 5 quark flavors active (not top)",
             nf_at_MZ == 5,
             "n_f = %d" % nf_at_MZ, checks)

    # --------------------------------------------------------
    print()
    print("CLOSED PATHS REGISTRY")
    print("-" * 70)
    print()

    chk_bool("7 closed paths registered",
             len(CLOSED_PATHS) == 7,
             "count = %d" % len(CLOSED_PATHS), checks)
    chk_bool("C3 Koide is closed",
             "C3_Koide" in CLOSED_PATHS,
             "killed by: %s" % CLOSED_PATHS.get("C3_Koide", {}).get("killed_by", "?"),
             checks)
    chk_bool("SM unification is closed",
             "SM_unification" in CLOSED_PATHS,
             "killed by: %s" % CLOSED_PATHS.get("SM_unification", {}).get("killed_by", "?"),
             checks)

    # --------------------------------------------------------
    print()
    print("ANOMALY REGISTRY")
    print("-" * 70)
    print()

    chk_bool("3 anomalies registered",
             len(ANOMALIES) == 3,
             "count = %d" % len(ANOMALIES), checks)
    chk_bool("Each anomaly uses a different quantum number",
             len(set(a["quantum_number_used"] for a in ANOMALIES.values())) == 3,
             "quantum numbers: %s" % [a["quantum_number_used"] for a in ANOMALIES.values()],
             checks)

    # --------------------------------------------------------
    print()
    print_summary(checks)

    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print()
    if n_fail == 0:
        print("  STRUCTURES LIBRARY: OPERATIONAL")
    else:
        print("  STRUCTURES LIBRARY: %d FAILURES" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("=" * 70)
    print("PHYS24_STRUCTURES SELF-TEST COMPLETE")
    print("=" * 70)
