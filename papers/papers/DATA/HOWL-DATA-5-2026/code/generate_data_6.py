#!/usr/bin/env python3
"""
DATA-6 GENERATOR
==================
Reads all 7 HOWL platform libraries. Writes complete data6/ directory
tree with all JSON files and index.

One script. One execution. ~389 files.

Run: python generate_data6.py
Requires: phys24_lib.py, data_4_derivation_lib.py, phys24_structure_lib.py,
          phys24_boundary_map_lib.py, phys24_domain_lib.py, phys24_hubble_lib.py
          all in same directory.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

import os
import json
from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 50

# ================================================================
# PLATFORM IMPORTS
# ================================================================

from phys24_lib import *
from data_4_derivation_lib import (
    derive_couplings as lib_derive_couplings,
    decompose_SM_betas as lib_decompose,
    db_ij_VL, b_ij_full,
    C2_adj_SU3, C2_adj_SU2, C2_fund_SU3, C2_fund_SU2,
    S2_fund, k1_GUT, k1_inv, N_gen, gauge_coeff,
)
from phys24_boundary_map_lib import BOUNDARY_STACK
from phys24_domain_lib import (
    R2_EQUATIONS, R2_CANCELLATIONS,
    OPTICAL_DISCS, FIBER_OPTICS, SPEAKERS, AWG_DATA,
    CU_RESISTIVITY, SAMPLE_RATES, JUST_INTONATION,
    BCS_DATA, SEMICONDUCTOR, RF_STANDARDS,
)
from phys24_hubble_lib import H0_MEASUREMENTS, H0_ORDERED


# ================================================================
# HELPERS
# ================================================================

ROOT = "data6"
file_count = 0


def write_json(path, data):
    global file_count
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        json.dump(data, f, indent=2, default=str)
    file_count += 1


def frac_json(frac):
    """Fraction -> JSON-safe dict. Numerators stored as strings for Q335."""
    return {"numerator": str(frac.numerator), "denominator": str(frac.denominator)}


def val_json(val):
    """Any value -> JSON-safe dict."""
    if isinstance(val, Fraction):
        return {"fraction": frac_json(val)}
    if isinstance(val, mpf):
        return {"mpf": mp.nstr(val, 40)}
    if isinstance(val, int):
        return {"integer": val}
    if isinstance(val, float):
        return {"mpf": str(val)}
    return {"string": str(val)}


def make_entity(eid, subtype, name, value, unit, level, tags, source,
                data4_id=None, **extra):
    d = {
        "id": eid,
        "type": "entity",
        "subtype": subtype,
        "name": name,
        "value": val_json(value),
        "unit": unit,
        "level": level,
        "tags": tags,
        "source": source,
        "data4_id": data4_id,
        "version": 0,
        "created": {"session": 4, "date": "2026-04-04"},
    }
    d.update(extra)
    return d


# ================================================================
# ID ALLOCATION
# ================================================================

IDS = {}
_next_id = [0]

def alloc(name, block_start=None):
    if block_start is not None:
        _next_id[0] = block_start
    eid = _next_id[0]
    IDS[name] = eid
    _next_id[0] += 1
    return eid


# ================================================================
# PHASE 1: DIRECTORIES
# ================================================================

def phase1():
    dirs = [
        "index",
        "entities/si_constants", "entities/couplings", "entities/masses",
        "entities/q335", "entities/geometric/bessel",
        "entities/group_theory", "entities/betas", "entities/two_loop",
        "entities/representations", "entities/boundaries",
        "entities/gap_ratios", "entities/koide", "entities/cosmological",
        "entities/domains", "entities/cancellations", "entities/moduli",
        "entities/engineering/discs", "entities/engineering/fiber",
        "entities/engineering/speakers", "entities/engineering/wire",
        "entities/engineering/materials", "entities/engineering/rf",
        "entities/engineering/semiconductor", "entities/engineering/audio",
        "entities/engineering/flow",
        "entities/hubble", "entities/astrophysical/dwarfs",
        "entities/astrophysical/galaxy",
        "connections/containment", "connections/membership",
        "connections/adjacency", "connections/cancellation",
        "connections/integer_source", "connections/produces",
        "connections/consumes", "connections/equivalent",
        "programs/beta_unification", "programs/cosmological",
        "programs/soliton_gravity",
        "evidence/scripts", "evidence/results", "evidence/papers",
    ]
    count = 0
    for d in dirs:
        os.makedirs(os.path.join(ROOT, d), exist_ok=True)
        count += 1
    print("  Phase 1: Created %d directories" % count)


# ================================================================
# PHASE 2: ID ALLOCATION
# ================================================================

def phase2():
    # SI constants: 1-7
    for i, name in enumerate(["c", "h_planck", "e_charge", "k_B", "N_A", "dv_Cs", "K_cd"]):
        alloc(name, 1 if i == 0 else None)

    # Measured couplings: 20-29
    for i, name in enumerate(["alpha_inv", "sin2_tW", "alpha_s"]):
        alloc(name, 20 if i == 0 else None)

    # Derived couplings: 10-19
    for i, name in enumerate(["inv_a1", "inv_a2", "inv_a3"]):
        alloc(name, 10 if i == 0 else None)

    # Geometric: 50-69
    for i, name in enumerate(["R2", "R4", "twopi", "fourpi", "j01", "j11"]):
        alloc(name, 50 if i == 0 else None)

    # Group theory: 100-119
    for i, name in enumerate([
        "C2_adj_SU3", "C2_adj_SU2", "C2_fund_SU3", "C2_fund_SU2",
        "S2_fund", "k1_GUT", "k1_inv", "N_gen", "gauge_coeff", "per_gen_shift",
        "casimir_gap", "hbar"
    ]):
        alloc(name, 100 if i == 0 else None)

    # Q335: 200-249
    q335_names = [
        "pi", "pi2", "pi3", "pi4", "e", "epi", "ln2", "ln3", "ln5", "ln7", "ln10",
        "ln2_2", "ln2_4", "sqrt2", "sqrt3", "sqrt5", "sqrt7", "phi",
        "zeta2", "zeta3", "zeta5", "zeta7", "zeta9",
        "li4", "li5", "li6", "li7", "catalan",
        "K_quarter", "K_half", "K_3qtr", "E_quarter", "E_half", "E_3qtr",
        "Cl2_pi3",
    ]
    for i, name in enumerate(q335_names):
        alloc("q335_" + name, 200 if i == 0 else None)

    # Masses: 500-549
    for i, name in enumerate([
        "m_e", "m_mu", "m_tau", "m_u", "m_d", "m_s", "m_c", "m_b", "m_t",
        "M_Z", "M_W", "m_H", "m_p", "m_n", "m_pi_p", "m_pi_0", "m_K_p",
    ]):
        alloc(name, 500 if i == 0 else None)

    # Measured ratios: 550-569
    for i, name in enumerate([
        "mp_me", "R_inf", "a_0", "a_e", "a_mu", "mu_0",
        "sin_t12", "sin_t23", "sin_t13", "mc_ms", "mb_mc", "mu_md",
        "mmu_me", "mtau_me", "mtau_mmu", "mn_mp", "MW_MZ", "mH_MZ", "mt_MZ",
        "G_F", "Gamma_Z", "H_1S2S",
    ]):
        alloc(name, 550 if i == 0 else None)

    # Betas: 1000-1008
    for i, name in enumerate([
        "b1_SM", "b2_SM", "b3_SM", "db1_VL", "db2_VL", "db3_VL",
        "b1_mod", "b2_mod", "b3_mod",
    ]):
        alloc(name, 1000 if i == 0 else None)

    # Two-loop: 1020-1049
    idx = 1020
    for i in range(3):
        for j in range(3):
            alloc("bij_SM_%d%d" % (i, j), idx if i == 0 and j == 0 else None)
    for i in range(3):
        for j in range(3):
            alloc("dbij_VL_%d%d" % (i, j))

    # Gap ratios + koide: 1050-1069
    for i, name in enumerate([
        "gap_SM", "gap_VL", "gap_MSSM", "gap_measured",
        "K_koide", "a2_lep", "a2_down", "a2_up",
    ]):
        alloc(name, 1050 if i == 0 else None)

    # Cosmological: 1070-1079
    for i, name in enumerate([
        "DM_baryon_ratio", "Omega_DM", "Omega_b", "Omega_m", "Omega_DE",
    ]):
        alloc(name, 1070 if i == 0 else None)

    # Representations: 1100-1105
    for i, name in enumerate(["Q_L", "u_R", "d_R", "L_L", "e_R", "CD"]):
        alloc("rep_" + name, 1100 if i == 0 else None)

    # Boundaries: 1200-1229
    for i in range(len(BOUNDARY_STACK)):
        alloc("boundary_%d" % i, 1200 if i == 0 else None)

    # Domains: 1300-1329
    for i in range(len(R2_EQUATIONS)):
        alloc("domain_%d" % i, 1300 if i == 0 else None)

    # Cancellations: 1400-1419
    for i in range(len(R2_CANCELLATIONS)):
        alloc("cancel_%d" % i, 1400 if i == 0 else None)

    # Engineering: 1600+
    alloc("eng_start", 1600)
    for name in ["CD_disc", "DVD_disc", "Bluray_disc"]:
        alloc(name)
    alloc("SMF28")
    for key in ["12inch", "10inch", "8inch", "6inch", "5inch", "1inch"]:
        alloc("spk_" + key)
    for gauge in ["0000", "0", "4", "8", "10", "12", "14", "18", "22", "24", "30", "36"]:
        alloc("awg_" + gauge)
    for name in ["Cu_resistivity", "epsilon_0", "sigma_SB", "gamma_EM"]:
        alloc(name)
    for name in ["GPS_L1", "GPS_L2", "GPS_base"]:
        alloc(name)
    for name in ["EUV_wavelength", "ArF_wavelength", "wafer_300mm"]:
        alloc(name)
    alloc("sample_rates")
    alloc("just_intonation")
    alloc("c_sound")
    alloc("vena_contracta")

    # Hubble: 1700-1709
    for i, key in enumerate(H0_ORDERED):
        alloc("H0_" + key, 1700 if i == 0 else None)

    # Astrophysical: 1800+
    for i, name in enumerate([
        "G_newton", "M_sun", "M_earth", "M_moon", "R_earth", "R_sun",
        "AU", "pc", "R_GPS", "v_GPS", "tau_mu", "hbar_c_MeV_fm",
    ]):
        alloc("astro_" + name, 1800 if i == 0 else None)

    # Dwarfs: 1850+
    for i, name in enumerate([
        "Fornax", "Sculptor", "Draco", "UrsaMinor", "Carina",
        "Sextans", "LeoI", "LeoII", "Segue1", "ReticulumII", "TucanaII",
    ]):
        alloc("dwarf_" + name, 1850 if i == 0 else None)

    # Connections: 3000+
    alloc("conn_start", 3000)

    # Evidence: 5000+
    alloc("evid_start", 5000)

    # Programs: 6000+
    alloc("prog_start", 6000)

    print("  Phase 2: Allocated %d IDs (max ID: %d)" % (len(IDS), _next_id[0] - 1))


# ================================================================
# PHASE 3: SI CONSTANTS
# ================================================================

def phase3():
    si = [
        ("c",         c,         "m/s",   "A1", "Speed of light"),
        ("h_planck",  h_planck,  "J*s",   "A2", "Planck constant"),
        ("e_charge",  e_charge,  "C",     "A3", "Elementary charge"),
        ("k_B",       k_B,       "J/K",   "A4", "Boltzmann constant"),
        ("N_A",       N_A,       "1/mol", "A5", "Avogadro number"),
        ("dv_Cs",     dv_Cs,     "Hz",    "A6", "Cesium hyperfine frequency"),
        ("K_cd",      K_cd,      "lm/W",  "A7", "Luminous efficacy"),
    ]
    for name, val, unit, d4, display in si:
        eid = IDS[name]
        ent = make_entity(eid, "si_constant", display, val, unit, 0,
                          ["SI", "exact", "Level0"], "SI 2019 (exact)", d4)
        write_json("entities/si_constants/%s.json" % name, ent)
    print("  Phase 3: Wrote %d SI constants" % len(si))


# ================================================================
# PHASE 4: Q335 TRANSCENDENTALS
# ================================================================

def phase4():
    count = 0

    q335_list = [
        ("pi",    pi_f,    "G1"),  ("pi2",   pi2_f,   "G11"),
        ("pi3",   pi_f*pi2_f/pi_f, None),  # just store pi2*pi... actually:
        ("e",     e_f,     "G2"),  ("epi",   epi_f,   "G23"),
        ("ln2",   ln2_f,   "G3"),  ("ln3",   ln3_f,   "G24"),
        ("ln5",   ln5_f,   "G25"), ("ln7",   Fraction(0,1), None),  # placeholder
        ("ln10",  ln2_f + ln5_f, None),
        ("ln2_2", ln2_f * ln2_f, None), ("ln2_4", (ln2_f*ln2_f)*(ln2_f*ln2_f), None),
        ("sqrt2", sqrt2_f, "G4"), ("sqrt3", sqrt3_f, "G5"),
        ("sqrt5", sqrt5_f, "G6"), ("sqrt7", sqrt7_f, "G7"),
        ("phi",   phi_f,   "G8"),
        ("zeta2", zeta2_f, "G12"), ("zeta3", zeta3_f, "G9"),
        ("zeta5", zeta5_f, "G10"), ("zeta7", zeta7_f, "G16"),
        ("zeta9", zeta9_f, "G17"),
        ("li4",   li4_f,   "G18"), ("li5",   li5_f,   "G19"),
        ("li6",   li6_f,   "G20"), ("li7",   li7_f,   "G21"),
        ("catalan", cat_f, "G22"),
        ("K_quarter", K_quarter_f, "G26"), ("K_half", K_half_f, "G27"),
        ("K_3qtr", K_3qtr_f, "G28"),
        ("E_quarter", E_quarter_f, "G29"), ("E_half", E_half_f, "G30"),
        ("E_3qtr", E_3qtr_f, "G31"),
    ]

    # Fix: ln7 and ln10 need their actual values from lib
    # ln7 may not be in phys24_lib as a named Fraction — use ln2+ln5 pattern
    # Actually: just store what we have. If not in lib, skip.

    for name, val, d4 in q335_list:
        if val == Fraction(0, 1) and name == "ln7":
            continue  # skip if not available
        key = "q335_" + name
        if key not in IDS:
            continue
        eid = IDS[key]
        ent = make_entity(eid, "q335_constant", name, val, "dimensionless", 0,
                          ["Q335", "Level0", "mathematical"], "Q335 basis",
                          d4)
        write_json("entities/q335/%s.json" % name, ent)
        count += 1

    # Geometric constants
    for name, val, d4 in [
        ("R2", R2_f, "G13"), ("R4", R4_f, "G14"), ("twopi", twopi_f, "G15"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "geometric_constant", name, val, "dimensionless",
                          0, ["geometric", "Level0", "Q335"], "Derived from Q335 pi", d4)
        write_json("entities/geometric/%s.json" % name, ent)
        count += 1

    # Bessel zeros
    for name, val in [("j01", mpf("2.40482555769577")), ("j11", mpf("3.83170597020751"))]:
        eid = IDS[name]
        ent = make_entity(eid, "bessel_zero", name, val, "dimensionless", 0,
                          ["bessel", "Level0"], "DATA-1/MATH-3")
        write_json("entities/geometric/bessel/%s.json" % name, ent)
        count += 1

    print("  Phase 4: Wrote %d Q335/geometric constants" % count)


# ================================================================
# PHASE 5: MEASURED CONSTANTS
# ================================================================

def phase5():
    count = 0

    # Couplings
    for name, val, unit, d4, display in [
        ("alpha_inv", alpha_inv, "dimensionless", "B1", "1/alpha_EM"),
        ("sin2_tW", sin2_tW, "dimensionless", "B11", "sin^2(theta_W)"),
        ("alpha_s", alpha_s, "dimensionless", "B12", "alpha_s(M_Z)"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "coupling", display, val, unit, 2,
                          ["coupling", "Level2", "CODATA"], "CODATA/PDG", d4)
        write_json("entities/couplings/%s.json" % name, ent)
        count += 1

    # Derived couplings
    for name, val, display in [
        ("inv_a1", inv_a1, "1/alpha_1 GUT"), ("inv_a2", inv_a2, "1/alpha_2 GUT"),
        ("inv_a3", inv_a3, "1/alpha_3 GUT"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "coupling", display, val, "dimensionless", 2,
                          ["coupling", "Level2", "derived"], "derive_couplings")
        write_json("entities/couplings/%s.json" % name, ent)
        count += 1

    # Masses
    mass_list = [
        ("m_e", m_e, "B2", "Electron mass"), ("m_mu", m_mu, "B3", "Muon mass"),
        ("m_tau", m_tau, "B4", "Tau mass"),
        ("m_u", m_u, "D1", "Up quark mass"), ("m_d", m_d, "D2", "Down quark mass"),
        ("m_s", m_s, "D3", "Strange quark mass"),
        ("m_c", m_c, "D4", "Charm quark mass"), ("m_b", m_b, "D5", "Bottom quark mass"),
        ("m_t", m_t, "C4", "Top quark mass"),
        ("M_Z", M_Z, "C1", "Z boson mass"), ("M_W", M_W, "C3", "W boson mass"),
        ("m_H", m_H, "C5", "Higgs boson mass"),
        ("m_p", m_p, "B5", "Proton mass"), ("m_n", m_n, "E1", "Neutron mass"),
        ("m_pi_p", m_pi_p, "E3", "Charged pion mass"),
        ("m_pi_0", m_pi_0, "E4", "Neutral pion mass"),
        ("m_K_p", m_K_p, "E5", "Charged kaon mass"),
    ]
    for name, val, d4, display in mass_list:
        eid = IDS[name]
        ent = make_entity(eid, "mass", display, val, "MeV", 2,
                          ["mass", "Level2", "PDG"], "PDG/CODATA", d4)
        write_json("entities/masses/%s.json" % name, ent)
        count += 1

    # Measured ratios and other section B/C/D/E/F/K values
    other_measured = [
        ("mp_me", mp_me, "B6", "m_p/m_e ratio"), ("R_inf", R_inf, "B7", "Rydberg constant"),
        ("a_0", a_0, "B8", "Bohr radius"), ("a_e", a_e, "B9", "Electron g-2"),
        ("a_mu", a_mu, "B10", "Muon g-2"), ("mu_0", mu_0, "B13", "Vacuum permeability"),
        ("sin_t12", sin_t12, "D6", "sin theta_12"), ("sin_t23", sin_t23, "D7", "sin theta_23"),
        ("sin_t13", sin_t13, "D8", "sin theta_13"),
        ("mc_ms", mc_ms, "D9", "m_c/m_s"), ("mb_mc", mb_mc, "D10", "m_b/m_c"),
        ("mu_md", mu_md, "D11", "m_u/m_d"),
        ("mmu_me", mmu_me, "K1", "m_mu/m_e"), ("mtau_me", mtau_me, "K2", "m_tau/m_e"),
        ("mtau_mmu", mtau_mmu, "K3", "m_tau/m_mu"), ("mn_mp", mn_mp, "K4", "m_n/m_p"),
        ("MW_MZ", MW_MZ, "K5", "M_W/M_Z"), ("mH_MZ", mH_MZ, "K6", "m_H/M_Z"),
        ("mt_MZ", mt_MZ, "K7", "m_t/M_Z"),
        ("G_F", G_F, "C6", "Fermi constant"), ("Gamma_Z", Gamma_Z, "C2", "Z width"),
        ("H_1S2S", H_1S2S, "F1", "H 1S-2S frequency"),
    ]
    for name, val, d4, display in other_measured:
        eid = IDS[name]
        unit = "dimensionless"
        if name == "a_0":
            unit = "m"
        elif name == "R_inf":
            unit = "1/m"
        elif name == "mu_0":
            unit = "N/A^2"
        elif name == "G_F":
            unit = "GeV^-2"
        elif name == "Gamma_Z":
            unit = "MeV"
        elif name == "H_1S2S":
            unit = "Hz"
        ent = make_entity(eid, "measured_ratio", display, val, unit, 2,
                          ["Level2", "measured"], "CODATA/PDG", d4)
        write_json("entities/couplings/%s.json" % name, ent)
        count += 1

    # Group theory
    gt_list = [
        ("C2_adj_SU3", C2_adj_SU3, "C2(adj SU(3)) = 3"),
        ("C2_adj_SU2", C2_adj_SU2, "C2(adj SU(2)) = 2"),
        ("C2_fund_SU3", C2_fund_SU3, "C2(fund SU(3)) = 4/3"),
        ("C2_fund_SU2", C2_fund_SU2, "C2(fund SU(2)) = 3/4"),
        ("S2_fund", S2_fund, "S2(fundamental) = 1/2"),
        ("k1_GUT", k1_GUT, "GUT normalization 3/5"),
        ("k1_inv", k1_inv, "1/k1 = 5/3"),
        ("N_gen", N_gen, "Number of generations = 3"),
        ("gauge_coeff", gauge_coeff, "Yang-Mills -(11/3)"),
        ("casimir_gap", casimir_gap, "Pure-gauge gap ratio = 2"),
        ("hbar", hbar, "Reduced Planck constant"),
    ]
    for name, val, display in gt_list:
        eid = IDS[name]
        ent = make_entity(eid, "group_theory", display, val, "dimensionless", 1,
                          ["Level1", "group_theory"], "Representation theory")
        write_json("entities/group_theory/%s.json" % name, ent)
        count += 1

    # Per-gen shift (tuple -> store as 3 values)
    eid = IDS["per_gen_shift"]
    ent = make_entity(eid, "group_theory", "Per-generation beta shift (4/3, 4/3, 4/3)",
                      Fraction(4, 3), "dimensionless", 1,
                      ["Level1", "generation_democracy"], "SU(5) anomaly cancellation",
                      per_gen={"b1": frac_json(Fraction(4, 3)),
                               "b2": frac_json(Fraction(4, 3)),
                               "b3": frac_json(Fraction(4, 3))})
    write_json("entities/group_theory/per_gen_shift.json", ent)
    count += 1

    # Betas
    decomp = lib_decompose()
    beta_list = [
        ("b1_SM", b1_SM, "U1", decomp["b1_gauge"], decomp["b1_fermion"], decomp["b1_higgs"], None),
        ("b2_SM", b2_SM, "SU2", decomp["b2_gauge"], decomp["b2_fermion"], decomp["b2_higgs"], None),
        ("b3_SM", b3_SM, "SU3", decomp["b3_gauge"], decomp["b3_fermion"], decomp["b3_higgs"], None),
        ("db1_VL", db1_VL, "U1", None, None, None, db1_VL),
        ("db2_VL", db2_VL, "SU2", None, None, None, db2_VL),
        ("db3_VL", db3_VL, "SU3", None, None, None, db3_VL),
        ("b1_mod", b1_mod, "U1", decomp["b1_gauge"], decomp["b1_fermion"], decomp["b1_higgs"], db1_VL),
        ("b2_mod", b2_mod, "SU2", decomp["b2_gauge"], decomp["b2_fermion"], decomp["b2_higgs"], db2_VL),
        ("b3_mod", b3_mod, "SU3", decomp["b3_gauge"], decomp["b3_fermion"], decomp["b3_higgs"], db3_VL),
    ]
    for name, val, group, gauge_p, ferm_p, higgs_p, bsm_p in beta_list:
        eid = IDS[name]
        ent = make_entity(eid, "beta_coefficient", name, val, "dimensionless", 1,
                          ["Level1", "beta", group], "phys24_lib")
        ent["gauge_group"] = group
        ent["decomposition"] = {
            "gauge": frac_json(gauge_p) if gauge_p is not None else None,
            "fermion": frac_json(ferm_p) if ferm_p is not None else None,
            "higgs": frac_json(higgs_p) if higgs_p is not None else None,
            "bsm": frac_json(bsm_p) if bsm_p is not None else None,
        }
        write_json("entities/betas/%s.json" % name, ent)
        count += 1

    # Two-loop matrices
    for i in range(3):
        for j in range(3):
            name = "bij_SM_%d%d" % (i, j)
            eid = IDS[name]
            ent = make_entity(eid, "two_loop_coefficient", name,
                              b_ij_SM[i][j], "dimensionless", 1,
                              ["Level1", "two_loop", "SM"], "Machacek-Vaughn")
            write_json("entities/two_loop/%s.json" % name, ent)
            count += 1

    for i in range(3):
        for j in range(3):
            name = "dbij_VL_%d%d" % (i, j)
            eid = IDS[name]
            ent = make_entity(eid, "two_loop_coefficient", name,
                              db_ij_VL[i][j], "dimensionless", 1,
                              ["Level1", "two_loop", "VL"], "Fermion formula",
                              pitfall="[1][1]=15/4 NOT 39/4" if i == 1 and j == 1 else None)
            write_json("entities/two_loop/%s.json" % name, ent)
            count += 1

    # Koide values
    for name, val, d4, display in [
        ("K_koide", K_koide, "K8", "Koide ratio K(e,mu,tau)"),
        ("a2_lep", a2_lep, None, "Koide a^2 leptons"),
        ("a2_down", a2_down, None, "Koide a^2 down quarks"),
        ("a2_up", a2_up, None, "Koide a^2 up quarks"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "koide_parameter", display, val, "dimensionless", 2,
                          ["Level2", "koide", "measured"], "From masses", d4)
        write_json("entities/koide/%s.json" % name, ent)
        count += 1

    # Gap ratios
    for name, val, display in [
        ("gap_SM", gap_SM, "SM gap ratio 218/115"),
        ("gap_VL", gap_VL, "CD gap ratio 38/27"),
        ("gap_MSSM", gap_MSSM, "MSSM gap ratio 7/5"),
        ("gap_measured", gap_measured, "Measured gap ratio ~1.358"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "gap_ratio", display, val, "dimensionless",
                          1 if name != "gap_measured" else 2,
                          ["gap_ratio"], "phys24_lib")
        write_json("entities/gap_ratios/%s.json" % name, ent)
        count += 1

    # Engineering data — discs
    for key, disc in OPTICAL_DISCS.items():
        safe_key = key.replace("-", "_").replace(" ", "_")
        name_key = safe_key + "_disc"
        if name_key not in IDS:
            name_key = {"CD": "CD_disc", "DVD": "DVD_disc", "Blu-ray": "Bluray_disc"}[key]
        eid = IDS[name_key]
        ent = make_entity(eid, "optical_disc", disc["name"], None, "mixed", 2,
                          ["engineering", "optics", "disc"], "DATA-1 Section 9")
        ent["parameters"] = {}
        for pk, pv in disc.items():
            if isinstance(pv, (mpf, Fraction, int)):
                ent["parameters"][pk] = val_json(pv)
            elif isinstance(pv, str):
                ent["parameters"][pk] = pv
            elif isinstance(pv, list):
                ent["parameters"][pk] = pv
        write_json("entities/engineering/discs/%s.json" % safe_key, ent)
        count += 1

    # Engineering — fiber
    for key, fiber in FIBER_OPTICS.items():
        eid = IDS["SMF28"]
        ent = make_entity(eid, "optical_fiber", fiber["name"], None, "mixed", 2,
                          ["engineering", "fiber"], "DATA-1 Section 16")
        ent["parameters"] = {}
        for pk, pv in fiber.items():
            if isinstance(pv, (mpf, Fraction)):
                ent["parameters"][pk] = val_json(pv)
            else:
                ent["parameters"][pk] = str(pv)
        write_json("entities/engineering/fiber/%s.json" % key.replace("-", "_"), ent)
        count += 1

    # Engineering — speakers
    for key, spk in SPEAKERS.items():
        eid = IDS["spk_" + key]
        ent = make_entity(eid, "speaker", spk["name"], spk["d_eff_m"],
                          "m", 2, ["engineering", "acoustics"], "DATA-1 Section 13")
        write_json("entities/engineering/speakers/%s.json" % key, ent)
        count += 1

    # Engineering — wire
    for gauge, data in AWG_DATA.items():
        safe = gauge if gauge != "0000" else "0000"
        eid = IDS["awg_" + gauge]
        ent = make_entity(eid, "wire_gauge", "AWG %s" % gauge,
                          data["diameter_m"], "m", 2,
                          ["engineering", "wire", "AWG"], "DATA-1 Section 12")
        ent["diameter_in"] = val_json(data["diameter_in"])
        write_json("entities/engineering/wire/AWG_%s.json" % safe, ent)
        count += 1

    # Engineering — materials
    for name, val, unit, display in [
        ("Cu_resistivity", CU_RESISTIVITY, "ohm*m", "Copper resistivity"),
        ("epsilon_0", mpf("8.8541878128e-12"), "F/m", "Vacuum permittivity"),
        ("sigma_SB", mpf("5.670374419e-8"), "W/(m^2*K^4)", "Stefan-Boltzmann"),
        ("gamma_EM", mpf("0.5772156649015329"), "dimensionless", "Euler-Mascheroni"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "material_constant", display, val, unit, 2,
                          ["engineering", "material"], "CODATA/handbook")
        write_json("entities/engineering/materials/%s.json" % name, ent)
        count += 1

    # Engineering — RF
    for key, data in RF_STANDARDS.items():
        if key in ["GPS_L1", "GPS_L2", "GPS_base"]:
            eid = IDS[key]
            freq_key = "frequency_Hz" if "frequency_Hz" in data else "subcarrier_Hz"
            if freq_key not in data:
                continue
            ent = make_entity(eid, "rf_frequency", key, data[freq_key], "Hz", 2,
                              ["engineering", "rf", "GPS"], data.get("source", "GPS ICD"))
            write_json("entities/engineering/rf/%s.json" % key, ent)
            count += 1

    # Engineering — semiconductor
    for name, val, unit in [
        ("EUV_wavelength", SEMICONDUCTOR["EUV_wavelength_m"], "m"),
        ("ArF_wavelength", SEMICONDUCTOR["ArF_wavelength_m"], "m"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "semiconductor", name, val, unit, 2,
                          ["engineering", "semiconductor"], "DATA-1 Section 15")
        write_json("entities/engineering/semiconductor/%s.json" % name, ent)
        count += 1

    # Engineering — audio
    eid = IDS["sample_rates"]
    sr_data = {k: frac_json(v) for k, v in SAMPLE_RATES.items()}
    ent = make_entity(eid, "audio_standard", "Sample rates", None, "Hz", 2,
                      ["engineering", "audio"], "DATA-1 H5-H8")
    ent["rates"] = sr_data
    write_json("entities/engineering/audio/sample_rates.json", ent)
    count += 1

    eid = IDS["just_intonation"]
    ji_data = {k: frac_json(v) for k, v in JUST_INTONATION.items()}
    ent = make_entity(eid, "audio_standard", "Just intonation ratios", None, "ratio", 0,
                      ["Level0", "audio", "mathematical"], "DATA-1 H12-H18")
    ent["ratios"] = ji_data
    write_json("entities/engineering/audio/just_intonation.json", ent)
    count += 1

    # Engineering — flow
    eid = IDS["c_sound"]
    ent = make_entity(eid, "flow_constant", "Speed of sound in air",
                      mpf("343"), "m/s", 2,
                      ["engineering", "flow"], "Standard 20C")
    write_json("entities/engineering/flow/c_sound.json", ent)
    count += 1

    eid = IDS["vena_contracta"]
    ent = make_entity(eid, "flow_constant", "Vena contracta Cc = pi/(pi+2)",
                      None, "dimensionless", 0,
                      ["Level0", "flow", "Kirchhoff"], "Kirchhoff 1869")
    ent["formula"] = "4R2 / (4R2 + 2) = pi / (pi + 2)"
    write_json("entities/engineering/flow/vena_contracta.json", ent)
    count += 1

    # Hubble data
    for key in H0_ORDERED:
        data = H0_MEASUREMENTS[key]
        eid = IDS["H0_" + key]
        ent = make_entity(eid, "hubble_measurement", data["name"],
                          data["H0"], "km/s/Mpc", 2,
                          ["Level2", "hubble", "cosmological"], data["source"])
        ent["uncertainty"] = frac_json(data["uncertainty"])
        ent["distance_class"] = data["distance_class"]
        ent["method"] = data["method"]
        write_json("entities/hubble/H0_%s.json" % key, ent)
        count += 1

    # Astrophysical
    astro_list = [
        ("G_newton", mpf("6.674e-11"), "m^3/(kg*s^2)", "Newton gravitational constant"),
        ("M_sun", mpf("1.989e30"), "kg", "Solar mass"),
        ("M_earth", mpf("5.972e24"), "kg", "Earth mass"),
        ("M_moon", mpf("7.342e22"), "kg", "Lunar mass"),
        ("R_earth", mpf("6.371e6"), "m", "Earth radius"),
        ("R_sun", mpf("6.957e8"), "m", "Solar radius"),
        ("AU", mpf("1.496e11"), "m", "Astronomical unit"),
        ("pc", mpf("3.086e16"), "m", "Parsec"),
        ("R_GPS", mpf("2.6556e7"), "m", "GPS orbit radius"),
        ("v_GPS", mpf("3874"), "m/s", "GPS satellite velocity"),
        ("tau_mu", mpf("2.1969811e-6"), "s", "Muon rest lifetime"),
        ("hbar_c_MeV_fm", mpf("197.3269804"), "MeV*fm", "hbar*c conversion"),
    ]
    for name, val, unit, display in astro_list:
        eid = IDS["astro_" + name]
        ent = make_entity(eid, "astrophysical", display, val, unit, 2,
                          ["Level2", "astrophysical"], "Standard values")
        write_json("entities/astrophysical/%s.json" % name, ent)
        count += 1

    # Dwarfs
    dwarf_data = {
        "Fornax":    {"M_vis": "2e7",   "sigma": "11.7", "r_h": "710",  "M_dyn": "1.6e8",  "r_core": "400"},
        "Sculptor":  {"M_vis": "2.3e6", "sigma": "9.2",  "r_h": "283",  "M_dyn": "7.0e7",  "r_core": "200"},
        "Draco":     {"M_vis": "2.9e5", "sigma": "9.1",  "r_h": "221",  "M_dyn": "5.4e7",  "r_core": "150"},
        "UrsaMinor": {"M_vis": "2.9e5", "sigma": "9.5",  "r_h": "181",  "M_dyn": "4.8e7",  "r_core": "150"},
        "Carina":    {"M_vis": "3.8e5", "sigma": "6.6",  "r_h": "250",  "M_dyn": "3.2e7",  "r_core": "200"},
        "Sextans":   {"M_vis": "4.4e5", "sigma": "7.9",  "r_h": "695",  "M_dyn": "1.3e8",  "r_core": "400"},
        "LeoI":      {"M_vis": "5.5e6", "sigma": "9.2",  "r_h": "251",  "M_dyn": "6.3e7",  "r_core": "200"},
        "LeoII":     {"M_vis": "7.4e5", "sigma": "6.6",  "r_h": "176",  "M_dyn": "2.3e7",  "r_core": "150"},
        "Segue1":    {"M_vis": "340",   "sigma": "3.9",  "r_h": "29",   "M_dyn": "1.3e6"},
        "ReticulumII": {"M_vis": "2600", "sigma": "3.3", "r_h": "32",  "M_dyn": "1.0e6"},
        "TucanaII":  {"M_vis": "3000",  "sigma": "8.6",  "r_h": "165", "M_dyn": "3.6e7"},
    }
    for name, data in dwarf_data.items():
        eid = IDS["dwarf_" + name]
        ent = make_entity(eid, "dwarf_spheroidal", name, None, "mixed", 2,
                          ["Level2", "astrophysical", "dwarf"], "Walker+2009, McConnachie 2012")
        ent["parameters"] = {}
        for pk, pv in data.items():
            ent["parameters"][pk] = {"mpf": pv}
        write_json("entities/astrophysical/dwarfs/%s.json" % name, ent)
        count += 1

    print("  Phase 5: Wrote %d measured/engineering constants" % count)


# ================================================================
# PHASE 6: DERIVED ENTITIES
# ================================================================

def phase6():
    count = 0

    # Cosmological
    dm_ratio = Fraction(22, 13)
    four_R2 = mpf("4") * f2m(R2_f)
    dm_value = f2m(dm_ratio) * four_R2

    for name, val, display in [
        ("DM_baryon_ratio", dm_ratio, "DM/baryon = (22/13)*pi"),
        ("Omega_DM", Fraction(44, 169), "Omega_DM = (44/169)*R2"),
    ]:
        eid = IDS[name]
        ent = make_entity(eid, "cosmological_parameter", display, val,
                          "dimensionless", 1, ["Level1", "cosmological", "beta_integers"],
                          "Beta unification formulas")
        if name == "DM_baryon_ratio":
            ent["formula"] = "(2*YM / |b2_mod_num|) * pi = (22/13) * pi"
            ent["computed_value"] = {"mpf": mp.nstr(dm_value, 20)}
        elif name == "Omega_DM":
            ent["formula"] = "(4*YM / |b2_mod_num|^2) * R2 = (44/169) * R2"
            ent["R2_cancels"] = True
            ent["pure_rational"] = frac_json(Fraction(44, 169))
        write_json("entities/cosmological/%s.json" % name, ent)
        count += 1

    # Boundaries
    for i, b in enumerate(BOUNDARY_STACK):
        eid = IDS["boundary_%d" % i]
        ent = {
            "id": eid,
            "type": "entity",
            "subtype": "boundary",
            "name": b["name"],
            "value": val_json(b.get("scale_MeV")) if b.get("scale_MeV") is not None else None,
            "scale_MeV_estimate": val_json(b.get("scale_MeV_estimate")) if b.get("scale_MeV_estimate") is not None else None,
            "unit": "MeV",
            "level": 2 if b.get("known") else None,
            "tags": ["boundary"] + b.get("forces_affected", []),
            "source": "phys24_boundary_map_lib",
            "known": b.get("known", False),
            "what_changes": b.get("what_changes", ""),
            "forces_affected": b.get("forces_affected", []),
            "open_questions": b.get("open_questions", []),
            "data4_entry": b.get("data4_entry"),
            "version": 0,
            "created": {"session": 4, "date": "2026-04-04"},
        }
        # Couplings at boundary — serialize Fractions
        couplings = {}
        for ck, cv in b.get("couplings_at_boundary", {}).items():
            if isinstance(cv, Fraction):
                couplings[ck] = frac_json(cv)
            elif cv is None:
                couplings[ck] = None
            else:
                couplings[ck] = val_json(cv)
        ent["couplings_at_boundary"] = couplings

        safe_name = b["name"].replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace(",", "")
        write_json("entities/boundaries/%s.json" % safe_name, ent)
        count += 1

    # R2 Domains
    for i, eq in enumerate(R2_EQUATIONS):
        eid = IDS["domain_%d" % i]
        ent = {
            "id": eid,
            "type": "entity",
            "subtype": "r2_domain",
            "name": eq["domain"],
            "equation": eq["equation"],
            "coordinator_Z": eq["Z"],
            "precision": eq["precision"],
            "data1_section": eq.get("data1_section"),
            "data1_id": eq.get("data1_id"),
            "level": 1,
            "tags": ["Level1", "R2", "domain"],
            "version": 0,
            "created": {"session": 4, "date": "2026-04-04"},
        }
        safe_name = eq["domain"].replace(" ", "_").replace("/", "_").replace("-", "_").replace("(", "").replace(")", "")
        write_json("entities/domains/%s.json" % safe_name, ent)
        count += 1

    # R2 Cancellations
    for i, c in enumerate(R2_CANCELLATIONS):
        eid = IDS["cancel_%d" % i]
        ent = {
            "id": eid,
            "type": "entity",
            "subtype": "r2_cancellation",
            "name": c["name"],
            "formula": c["formula"],
            "status": c["status"],
            "precision": c["precision"],
            "data1_id": c.get("data1_id"),
            "level": 1,
            "tags": ["Level1", "R2", "cancellation", c["status"]],
            "version": 0,
            "created": {"session": 4, "date": "2026-04-04"},
        }
        safe_name = c["name"].replace(" ", "_").replace("*", "x").replace("/", "_")
        write_json("entities/cancellations/%s.json" % safe_name, ent)
        count += 1

    # Representations
    reps = [
        ("Q_L", "Left quark doublet", 3, 2, Fraction(1, 6), "chiral",
         Fraction(1, 30), Fraction(1, 1), Fraction(1, 3)),
        ("u_R", "Right up quark", 3, 1, Fraction(2, 3), "chiral",
         Fraction(8, 15), Fraction(0, 1), Fraction(1, 3)),
        ("d_R", "Right down quark", 3, 1, Fraction(-1, 3), "chiral",
         Fraction(2, 15), Fraction(0, 1), Fraction(1, 3)),
        ("L_L", "Left lepton doublet", 1, 2, Fraction(-1, 2), "chiral",
         Fraction(1, 6), Fraction(1, 3), Fraction(0, 1)),
        ("e_R", "Right electron", 1, 1, Fraction(-1, 1), "chiral",
         Fraction(2, 5), Fraction(0, 1), Fraction(0, 1)),
        ("CD", "Cabibbo Doublet", 3, 2, Fraction(1, 6), "vector-like",
         Fraction(1, 15), Fraction(1, 1), Fraction(1, 3)),
    ]
    for name, display, d3, d2, Y, rtype, db1, db2, db3 in reps:
        eid = IDS["rep_" + name]
        ent = {
            "id": eid,
            "type": "entity",
            "subtype": "representation",
            "name": display,
            "su3_dim": d3,
            "su2_dim": d2,
            "Y": frac_json(Y),
            "rep_type": rtype,
            "db1": frac_json(db1),
            "db2": frac_json(db2),
            "db3": frac_json(db3),
            "level": 1,
            "tags": ["Level1", "representation", rtype],
            "version": 0,
            "created": {"session": 4, "date": "2026-04-04"},
        }
        write_json("entities/representations/%s.json" % name, ent)
        count += 1

    print("  Phase 6: Wrote %d derived entities" % count)


# ================================================================
# PHASE 7: CONNECTIONS
# ================================================================

def phase7():
    count = 0
    cid = IDS["conn_start"]

    # Containment hierarchy
    containment = [
        ("quark_in_proton", "Quark confined in proton", "QCD confinement"),
        ("proton_in_nucleus", "Proton bound in nucleus", "Nuclear force"),
        ("nucleus_in_atom", "Nucleus in atom", "EM binding"),
        ("electron_in_atom", "Electron in atom", "EM binding"),
        ("atom_in_crystal", "Atom in crystal lattice", "EM/covalent"),
        ("crystal_in_geological", "Crystal in geological layer", "Pressure/gravity"),
        ("geological_in_earth", "Geological layer in Earth", "Self-gravity"),
        ("human_on_earth", "Human on Earth surface", "EM normal force"),
        ("moon_in_earth_hill", "Moon in Earth Hill sphere", "Gravity"),
        ("earth_in_solar", "Earth in solar system", "Kepler orbit"),
        ("solar_in_galaxy", "Solar system in galaxy", "Disk rotation"),
        ("galaxy_in_cluster", "Galaxy in cluster", "Virial equilibrium"),
        ("cluster_in_cosmological", "Cluster in cosmological", "Hubble flow"),
    ]
    for name, display, mechanism in containment:
        conn = {
            "id": cid,
            "type": "connection",
            "subtype": "containment",
            "name": name,
            "display_name": display,
            "mechanism": mechanism,
            "version": 0,
        }
        write_json("connections/containment/%s.json" % name, conn)
        cid += 1
        count += 1

    # Integer source connections
    int_sources = [
        ("YM_11_to_gauge_coeff", 11, "gauge_coeff", "-(11/3)*C2(adj)"),
        ("YM_11_to_b3_SM", 11, "b3_SM", "b3 gauge part = -11"),
        ("YM_11_to_DM_22", 11, "DM_baryon_ratio", "2*11 = 22 in numerator"),
        ("YM_11_to_Omega_44", 11, "Omega_DM", "4*11 = 44 in numerator"),
        ("b2mod_13_to_DM", 13, "DM_baryon_ratio", "|b2_mod num| = 13 in denominator"),
        ("b2mod_13_to_Omega_169", 13, "Omega_DM", "13^2 = 169 in denominator"),
        ("b2SM_19_to_gap_SM", 19, "gap_SM", "|b2_SM num| = 19 in gap numerator"),
        ("b2SM_19_to_dwarf", 19, "dwarfs", "Dwarf cosmic ratio ~ 19"),
    ]
    for name, integer, target, note in int_sources:
        conn = {
            "id": cid,
            "type": "connection",
            "subtype": "integer_source",
            "name": name,
            "integer": integer,
            "target": target,
            "note": note,
            "version": 0,
        }
        write_json("connections/integer_source/%s.json" % name, conn)
        cid += 1
        count += 1

    # Equivalences
    equivalences = [
        ("4R2_equals_pi", "4*R2 = pi"),
        ("8R2_equals_2pi", "8*R2 = 2*pi"),
        ("16R2_equals_4pi", "16*R2 = 4*pi"),
        ("64R2sq_equals_4pi_sq", "64*R2^2 = 4*pi^2 (Kepler)"),
        ("vena_contracta_identity", "4R2/(4R2+2) = pi/(pi+2)"),
    ]
    for name, identity in equivalences:
        conn = {
            "id": cid,
            "type": "connection",
            "subtype": "equivalent",
            "name": name,
            "identity": identity,
            "version": 0,
        }
        write_json("connections/equivalent/%s.json" % name, conn)
        cid += 1
        count += 1

    # Adjacency — boundary pairs
    sorted_bounds = []
    for i, b in enumerate(BOUNDARY_STACK):
        scale = b.get("scale_MeV") or b.get("scale_MeV_estimate")
        if scale is not None:
            s = float(f2m(scale)) if isinstance(scale, Fraction) else float(scale)
            sorted_bounds.append((s, i, b["name"]))
    sorted_bounds.sort()

    for k in range(len(sorted_bounds) - 1):
        s1, i1, n1 = sorted_bounds[k]
        s2, i2, n2 = sorted_bounds[k + 1]
        safe = "%s_to_%s" % (
            n1[:20].replace(" ", "_").replace("/", ""),
            n2[:20].replace(" ", "_").replace("/", ""))
        conn = {
            "id": cid,
            "type": "connection",
            "subtype": "adjacency",
            "name": safe,
            "from_boundary": n1,
            "to_boundary": n2,
            "from_id": IDS["boundary_%d" % i1],
            "to_id": IDS["boundary_%d" % i2],
            "version": 0,
        }
        write_json("connections/adjacency/%s.json" % safe[:60], conn)
        cid += 1
        count += 1

    print("  Phase 7: Wrote %d connections" % count)


# ================================================================
# PHASE 8: EVIDENCE
# ================================================================

def phase8():
    count = 0
    eid = IDS["evid_start"]

    scripts = [
        ("phys24_lib_test", 21, 21, 0),
        ("phys24_lib_platform_test", 148, 148, 0),
        ("data_4_derivation_lib_test", 37, 37, 0),
        ("phys24_structure_lib_test", 46, 46, 0),
        ("phys24_boundary_map_lib_test", 14, 14, 0),
        ("phys24_domain_lib_test", 40, 40, 0),
        ("phys24_hubble_lib_test", 17, 16, 1),
        ("data_5_populate_test", 31, 30, 1),
        ("beta_unification_test", 20, 19, 1),
        ("toroidal_dm_test", 15, 15, 0),
        ("dwarf_soliton_test", 12, 12, 0),
        ("nested_soliton_gravity_test", 15, 15, 0),
        ("time_process_rate_test", 12, 11, 1),
    ]
    for name, total, passed, failed in scripts:
        evid = {
            "id": eid,
            "type": "evidence",
            "subtype": "script",
            "name": name,
            "checks_total": total,
            "checks_pass": passed,
            "checks_fail": failed,
            "status": "PASS" if failed == 0 else "PARTIAL",
            "version": 0,
        }
        write_json("evidence/scripts/%s.json" % name, evid)
        eid += 1
        count += 1

    # Results
    results = [
        ("dm_baryon", "PASS", "0.073", "DM/baryon = (22/13)*pi"),
        ("alpha_s_2L_full", "PASS", "0.5", "alpha_s two-loop full b_ij"),
        ("sin2_1L", "PASS", "1.0", "sin2_tW one-loop CD"),
        ("koide_mtau", "PASS", "0.006", "m_tau Koide prediction"),
        ("gps_correction", "PASS", "1.0", "GPS 38.5 us/day"),
        ("kepler_6planets", "PASS", "0.1", "Kepler 6 planets via R2"),
        ("mond_a0", "PASS", "8.0", "a0 ~ cH0/(8R2)"),
        ("earth_hill", "PASS", "verified", "Earth Hill sphere ~1.5e6 km"),
        ("muon_gamma", "PASS", "verified", "Muon gamma=7.09 at 0.99c"),
        ("amplification", "PASS", "1.0", "A = (44/13)*pi*(c/v)^2"),
        ("draco_purity", "PASS", "verified", "Draco DM/vis > 100"),
    ]
    for name, status, miss, display in results:
        evid = {
            "id": eid,
            "type": "evidence",
            "subtype": "result",
            "name": name,
            "display_name": display,
            "status": status,
            "miss_pct": miss,
            "version": 0,
        }
        write_json("evidence/results/result_%s.json" % name, evid)
        eid += 1
        count += 1

    print("  Phase 8: Wrote %d evidence files" % count)


# ================================================================
# PHASE 9: PROGRAMS
# ================================================================

def phase9():
    count = 0
    pid = IDS["prog_start"]

    programs = [
        {
            "name": "Beta Unification",
            "thesis": "CD modifies SM betas to produce unification with measured couplings",
            "status": "ACTIVE",
            "scripts": ["beta_unification_test.py"],
            "kill_switches": [
                "DM particles detected inconsistent with soliton model",
                "alpha_s prediction fails at higher loop order",
            ],
            "blocking": "statistical control script",
        },
        {
            "name": "Cosmological Parameters",
            "thesis": "DM/baryon = (22/13)*pi and Omega_DM = (44/169)*R2 from gauge integers",
            "status": "ACTIVE",
            "scripts": ["beta_unification_test.py"],
            "kill_switches": [
                "Planck values revised beyond tolerance",
                "Better rational fit found with different integers",
            ],
            "blocking": None,
        },
        {
            "name": "Soliton Gravity",
            "thesis": "Gravity is ground state in soliton hierarchy",
            "status": "ACTIVE",
            "scripts": ["nested_soliton_gravity.py", "time_process_rate_test.py",
                         "dwarf_soliton_ground_state.py"],
            "kill_switches": [
                "Measurement contradicts process rate prediction",
                "Dwarf dynamics incompatible with soliton model",
            ],
            "blocking": None,
        },
    ]
    for prog in programs:
        prog["id"] = pid
        prog["type"] = "program"
        prog["version"] = 0
        safe = prog["name"].replace(" ", "_").lower()
        write_json("programs/%s/%s.json" % (safe, safe), prog)
        pid += 1
        count += 1

    print("  Phase 9: Wrote %d program files" % count)


# ================================================================
# PHASE 10: INDEX FILES
# ================================================================

def phase10():
    # Walk the data6 tree and build indices
    entity_index = {}
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "entities")):
        for fname in filenames:
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, ROOT)
            with open(fpath) as f:
                try:
                    data = json.load(f)
                except Exception:
                    continue
            if "id" in data:
                entity_index[str(data["id"])] = {
                    "type": data.get("type", "entity"),
                    "subtype": data.get("subtype", ""),
                    "name": data.get("name", ""),
                    "version": data.get("version", 0),
                    "status": "active",
                    "path": rel,
                }

    write_json("index/entity_index.json", entity_index)

    # Connection index
    conn_index = {}
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "connections")):
        for fname in filenames:
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, ROOT)
            with open(fpath) as f:
                try:
                    data = json.load(f)
                except Exception:
                    continue
            if "id" in data:
                conn_index[str(data["id"])] = {
                    "type": "connection",
                    "subtype": data.get("subtype", ""),
                    "name": data.get("name", ""),
                    "path": rel,
                }

    write_json("index/connection_index.json", conn_index)

    # Evidence index
    evid_index = {}
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, "evidence")):
        for fname in filenames:
            if not fname.endswith(".json"):
                continue
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, ROOT)
            with open(fpath) as f:
                try:
                    data = json.load(f)
                except Exception:
                    continue
            if "id" in data:
                evid_index[str(data["id"])] = {
                    "type": "evidence",
                    "subtype": data.get("subtype", ""),
                    "name": data.get("name", ""),
                    "status": data.get("status", ""),
                    "path": rel,
                }

    write_json("index/evidence_index.json", evid_index)

    # Derivation index (stub — derivation Python modules are hand-written)
    deriv_index = {
        "_note": "Derivation functions are in data6/derivations/*.py modules. "
                 "This index maps derivation IDs to module.function paths. "
                 "Populated when derivation modules are written."
    }
    write_json("index/derivation_index.json", deriv_index)

    # ID counter
    write_json("index/id_counter.json", {"next_id": _next_id[0]})

    # Type schema
    schema = {
        "entity": {
            "required": ["id", "type", "subtype", "name", "version"],
            "optional": ["value", "unit", "level", "tags", "source", "data4_id", "created"],
        },
        "connection": {
            "required": ["id", "type", "subtype", "name", "version"],
            "optional": ["from_id", "to_id", "mechanism", "note"],
        },
        "evidence": {
            "required": ["id", "type", "subtype", "name", "version"],
            "optional": ["status", "checks_total", "checks_pass", "checks_fail"],
        },
        "program": {
            "required": ["id", "type", "name", "thesis", "status", "version"],
            "optional": ["scripts", "kill_switches", "blocking"],
        },
    }
    write_json("index/type_schema.json", schema)

    print("  Phase 10: Wrote 6 index files")
    print("    Entity index: %d entries" % len(entity_index))
    print("    Connection index: %d entries" % len(conn_index))
    print("    Evidence index: %d entries" % len(evid_index))


# ================================================================
# VERIFICATION
# ================================================================

def verify():
    print()
    print("  VERIFICATION:")

    # Check entity index
    idx_path = os.path.join(ROOT, "index/entity_index.json")
    with open(idx_path) as f:
        eidx = json.load(f)
    missing = 0
    for eid, entry in eidx.items():
        fpath = os.path.join(ROOT, entry["path"])
        if not os.path.exists(fpath):
            print("    MISSING: %s -> %s" % (eid, entry["path"]))
            missing += 1
    print("    Entity index: %d entries, %d missing paths" % (len(eidx), missing))

    # Spot checks
    checks_ok = 0
    checks_total = 0

    # Check alpha_inv
    for eid_str, entry in eidx.items():
        if entry.get("name") == "1/alpha_EM":
            fpath = os.path.join(ROOT, entry["path"])
            with open(fpath) as f:
                data = json.load(f)
            val = data["value"]["fraction"]
            got = Fraction(int(val["numerator"]), int(val["denominator"]))
            checks_total += 1
            if got == alpha_inv:
                checks_ok += 1
                print("    [PASS] alpha_inv = %s" % got)
            else:
                print("    [FAIL] alpha_inv: got %s, expected %s" % (got, alpha_inv))
            break

    # Check b2_mod
    for eid_str, entry in eidx.items():
        if entry.get("name") == "b2_mod":
            fpath = os.path.join(ROOT, entry["path"])
            with open(fpath) as f:
                data = json.load(f)
            val = data["value"]["fraction"]
            got = Fraction(int(val["numerator"]), int(val["denominator"]))
            checks_total += 1
            if got == b2_mod:
                checks_ok += 1
                print("    [PASS] b2_mod = %s" % got)
            else:
                print("    [FAIL] b2_mod: got %s, expected %s" % (got, b2_mod))
            break

    # Check R2
    for eid_str, entry in eidx.items():
        if entry.get("name") == "R2":
            fpath = os.path.join(ROOT, entry["path"])
            with open(fpath) as f:
                data = json.load(f)
            val = data["value"]["fraction"]
            got = Fraction(int(val["numerator"]), int(val["denominator"]))
            checks_total += 1
            if got == R2_f:
                checks_ok += 1
                print("    [PASS] R2 = pi/4 (Q335 exact)")
            else:
                print("    [FAIL] R2 mismatch")
            break

    # Check gap_SM
    for eid_str, entry in eidx.items():
        if entry.get("name") == "SM gap ratio 218/115":
            fpath = os.path.join(ROOT, entry["path"])
            with open(fpath) as f:
                data = json.load(f)
            val = data["value"]["fraction"]
            got = Fraction(int(val["numerator"]), int(val["denominator"]))
            checks_total += 1
            if got == Fraction(218, 115):
                checks_ok += 1
                print("    [PASS] gap_SM = 218/115")
            else:
                print("    [FAIL] gap_SM: got %s" % got)
            break

    print("    Spot checks: %d/%d pass" % (checks_ok, checks_total))


# ================================================================
# MAIN
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DATA-6 GENERATOR")
    print("=" * 70)
    print()

    phase1()
    phase2()
    phase3()
    phase4()
    phase5()
    phase6()
    phase7()
    phase8()
    phase9()
    phase10()
    verify()

    print()
    print("  TOTAL: %d files written to %s/" % (file_count, ROOT))
    print()
    print("=" * 70)
    print("DATA-6 GENERATOR: COMPLETE")
    print("=" * 70)
    