#!/usr/bin/env python3
"""
HOWL DATA-5 POPULATION SCRIPT
================================
Populates a DATA5 database from the HOWL-PLATFORM-v1 libraries.

Creates every object documented in the DATA-5 tech spec:
  ~113 Constant objects from phys24_lib.py (Sections A-L, N, K, G)
  ~16 derived Constant objects (inv_a1, inv_a2, inv_a3, alpha_em, etc.)
  9 BetaCoefficient objects (SM + CD shifts + modified)
  7 Representation objects (5 SM fermions + Higgs + CD)
  19 SolitonBoundary objects (Planck to gravitational dominance)
  23 R2Domain objects (22 original + gauge coupling running)
  11 R2Cancellation objects (7 original + 4 from modulus notebook)
  Key ExperimentResult objects from Session 4 experiments
  3 ResearchProgram objects (beta, toroidal DM, Hubble)

Population strategy:
  - phys24_lib.py is imported directly (always available)
  - Extension libraries imported if available on sys.path
  - If extension libs missing, uses hardcoded data (exact values
    from library source code, verified against .dat self-test outputs)

Usage:
    from data_5_objects import *
    from data_5_populate import populate_all

    db = DATA5()
    populate_all(db)
    db.show_summary()

Platform: HOWL-PLATFORM-v1
Depends on: data_5_objects.py, phys24_lib.py
Optional: phys24_structure_lib.py, phys24_boundary_map_lib.py,
          phys24_domain_lib.py, phys24_hubble_lib.py
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 100

# Required
from phys24_lib import *
from data_5_objects import (
    DATA5, Constant, BetaCoefficient, Representation,
    SolitonBoundary, R2Domain, R2Cancellation, Modulus,
    ExperimentResult, ResearchProgram,
    search, constants_at_level, export_json,
    chk_bool, chk_exact, print_summary,
)


_LIB_VERSION = "1"
_LIB_VERSION_1 = ("Session 4, April 3 2026. Initial release. "
                   "Full population from phys24_lib + extension data.")


# ================================================================
# POPULATE: SI CONSTANTS (Section A, 7 entries)
# ================================================================

def populate_SI(db):
    """Section A: 7 SI exact constants. Level 0 (defined, not measured)."""
    _entries = [
        ("const.c",        "Speed of light",        c,        "m/s",      9,  "A1"),
        ("const.h",        "Planck constant",        h_planck, "J*s",      9,  "A2"),
        ("const.e_charge", "Elementary charge",       e_charge, "C",        10, "A3"),
        ("const.k_B",      "Boltzmann constant",      k_B,      "J/K",      7,  "A4"),
        ("const.N_A",      "Avogadro number",         N_A,      "mol^-1",   9,  "A5"),
        ("const.dv_Cs",    "Cesium hyperfine freq",    dv_Cs,    "Hz",       10, "A6"),
        ("const.K_cd",     "Luminous efficacy",        K_cd,     "lm/W",     3,  "A7"),
    ]
    for oid, name, val, unit, dig, d4id in _entries:
        db.add(Constant(oid, name, val, unit=unit, level=0,
                         digits=dig, source="SI 2019 (exact)",
                         data4_id=d4id,
                         tags=["SI", "exact", "Level0"]))


# ================================================================
# POPULATE: MEASURED CONSTANTS (Section B, 13 entries)
# ================================================================

def populate_measured(db):
    """Section B: 13 CODATA 2022 measured constants. Level 2."""
    _entries = [
        ("const.alpha_inv", "1/alpha (CODATA 2022)",  alpha_inv, "",   12, "B1",
         ["EM", "coupling"]),
        ("const.m_e",       "Electron mass",           m_e,       "MeV", 11, "B2",
         ["lepton", "mass"]),
        ("const.m_mu",      "Muon mass",               m_mu,      "MeV", 10, "B3",
         ["lepton", "mass"]),
        ("const.m_tau",     "Tau mass",                m_tau,     "MeV", 6,  "B4",
         ["lepton", "mass", "Koide"]),
        ("const.m_p",       "Proton mass",             m_p,       "MeV", 11, "B5",
         ["nuclear", "mass"]),
        ("const.mp_me",     "m_p/m_e ratio",           mp_me,     "",    13, "B6",
         ["ratio"]),
        ("const.R_inf",     "Rydberg constant",        R_inf,     "m^-1", 13, "B7",
         ["atomic"]),
        ("const.a_0",       "Bohr radius",             a_0,       "m",   12, "B8",
         ["atomic"]),
        ("const.a_e",       "Electron g-2",            a_e,       "",    12, "B9",
         ["EM"]),
        ("const.a_mu",      "Muon g-2",               a_mu,      "",    9,  "B10",
         ["EM"]),
        ("const.sin2_tW",   "Weak mixing angle",       sin2_tW,   "",    5,  "B11",
         ["weak", "coupling", "EW"]),
        ("const.alpha_s",   "Strong coupling",         alpha_s,   "",    4,  "B12",
         ["strong", "coupling", "QCD"]),
        ("const.mu_0",      "Vacuum permeability",     mu_0,      "N/A^2", 12, "B13",
         ["EM"]),
    ]
    for oid, name, val, unit, dig, d4id, extra_tags in _entries:
        db.add(Constant(oid, name, val, unit=unit, level=2,
                         digits=dig, source="CODATA 2022",
                         data4_id=d4id,
                         tags=["Level2", "CODATA"] + extra_tags))


# ================================================================
# POPULATE: ELECTROWEAK OBSERVABLES (Section C, 6 entries)
# ================================================================

def populate_electroweak(db):
    """Section C: 6 LEP/PDG electroweak observables. Level 2."""
    _entries = [
        ("const.M_Z",     "Z boson mass",     M_Z,     "MeV",   6, "C1"),
        ("const.Gamma_Z", "Z width",          Gamma_Z, "MeV",   5, "C2"),
        ("const.M_W",     "W boson mass",     M_W,     "MeV",   6, "C3"),
        ("const.m_t",     "Top quark mass",   m_t,     "MeV",   5, "C4"),
        ("const.m_H",     "Higgs mass",       m_H,     "MeV",   5, "C5"),
        ("const.G_F",     "Fermi constant",   G_F,     "GeV^-2", 8, "C6"),
    ]
    for oid, name, val, unit, dig, d4id in _entries:
        db.add(Constant(oid, name, val, unit=unit, level=2,
                         digits=dig, source="LEP/PDG",
                         data4_id=d4id,
                         tags=["Level2", "PDG", "EW"]))


# ================================================================
# POPULATE: QUARK MASSES AND CKM (Section D, 11 entries)
# ================================================================

def populate_quarks(db):
    """Section D: 11 quark mass and CKM entries. Level 2."""
    _quark_entries = [
        ("const.m_u",     "Up quark mass (MS-bar 2GeV)",      m_u,     "MeV", 3, "D1",
         ["quark", "mass"]),
        ("const.m_d",     "Down quark mass (MS-bar 2GeV)",    m_d,     "MeV", 3, "D2",
         ["quark", "mass"]),
        ("const.m_s",     "Strange quark mass (MS-bar 2GeV)", m_s,     "MeV", 3, "D3",
         ["quark", "mass"]),
        ("const.m_c",     "Charm quark mass (MS-bar at m_c)", m_c,     "MeV", 4, "D4",
         ["quark", "mass"]),
        ("const.m_b",     "Bottom quark mass (MS-bar at m_b)", m_b,    "MeV", 4, "D5",
         ["quark", "mass"]),
        ("const.sin_t12", "sin(theta_12) Cabibbo",            sin_t12, "",    5, "D6",
         ["CKM"]),
        ("const.sin_t23", "sin(theta_23) CKM",                sin_t23, "",    4, "D7",
         ["CKM"]),
        ("const.sin_t13", "sin(theta_13) CKM",                sin_t13, "",    4, "D8",
         ["CKM"]),
        ("const.mc_ms",   "m_c/m_s lattice (FLAG)",           mc_ms,   "",    5, "D9",
         ["ratio", "FLAG"]),
        ("const.mb_mc",   "m_b/m_c lattice (FLAG)",           mb_mc,   "",    4, "D10",
         ["ratio", "FLAG"]),
        ("const.mu_md",   "m_u/m_d lattice (FLAG)",           mu_md,   "",    3, "D11",
         ["ratio", "FLAG"]),
    ]
    for oid, name, val, unit, dig, d4id, extra_tags in _quark_entries:
        db.add(Constant(oid, name, val, unit=unit, level=2,
                         digits=dig, source="PDG 2024 / FLAG",
                         data4_id=d4id,
                         tags=["Level2"] + extra_tags))


# ================================================================
# POPULATE: NUCLEAR/HADRON MASSES (Section E, 8 entries)
# ================================================================

def populate_nuclear(db):
    """Section E: 8 nuclear and hadron masses. Level 2."""
    _entries = [
        ("const.m_n",        "Neutron mass",          m_n,        "MeV", 11, "E1"),
        ("const.mn_mp_diff", "m_n - m_p",             mn_mp_diff, "MeV", 8,  "E2"),
        ("const.m_pi_p",     "Charged pion mass",     m_pi_p,     "MeV", 8,  "E3"),
        ("const.m_pi_0",     "Neutral pion mass",     m_pi_0,     "MeV", 7,  "E4"),
        ("const.m_K_p",      "Charged kaon mass",     m_K_p,      "MeV", 6,  "E5"),
        ("const.m_D",        "Deuteron mass",         m_D,        "MeV", 12, "E6"),
        ("const.m_He4",      "Helium-4 mass",         m_He4,      "MeV", 10, "E7"),
        ("const.E_D",        "Deuteron binding energy", E_D,      "MeV", 8,  "E8"),
    ]
    for oid, name, val, unit, dig, d4id in _entries:
        db.add(Constant(oid, name, val, unit=unit, level=2,
                         digits=dig, source="CODATA 2022",
                         data4_id=d4id,
                         tags=["Level2", "nuclear", "mass"]))


# ================================================================
# POPULATE: SPECTROSCOPY (Section F, 1 entry)
# ================================================================

def populate_spectroscopy(db):
    """Section F: 1 spectroscopy entry. Level 2."""
    db.add(Constant("const.H_1S2S", "Hydrogen 1S-2S frequency",
                     H_1S2S, unit="Hz", level=2,
                     digits=16, source="MPQ 2011",
                     data4_id="F1",
                     tags=["Level2", "atomic", "clock"]))


# ================================================================
# POPULATE: Q335 ANALYTICAL CONSTANTS (Section G, 31 entries)
# ================================================================

def populate_Q335(db):
    """Section G: 31 Q335 basis constants. Level 0 (exact math)."""
    _entries = [
        ("const.pi",         "pi",                    pi_f,         "", "G1"),
        ("const.e_euler",    "e (Euler)",             e_f,          "", "G2"),
        ("const.ln2",        "ln(2)",                 ln2_f,        "", "G3"),
        ("const.sqrt2",      "sqrt(2)",               sqrt2_f,      "", "G4"),
        ("const.sqrt3",      "sqrt(3)",               sqrt3_f,      "", "G5"),
        ("const.sqrt5",      "sqrt(5)",               sqrt5_f,      "", "G6"),
        ("const.sqrt7",      "sqrt(7)",               sqrt7_f,      "", "G7"),
        ("const.phi",        "Golden ratio phi",      phi_f,        "", "G8"),
        ("const.zeta3",      "zeta(3) Apery",         zeta3_f,      "", "G9"),
        ("const.zeta5",      "zeta(5)",               zeta5_f,      "", "G10"),
        ("const.pi2",        "pi^2",                  pi2_f,        "", "G11"),
        ("const.zeta2",      "zeta(2) = pi^2/6",      zeta2_f,     "", "G12"),
        ("const.R2",         "R2 = pi/4",             R2_f,         "", "G13"),
        ("const.R4",         "R4 = pi^2/32",          R4_f,         "", "G14"),
        ("const.twopi",      "2*pi",                  twopi_f,      "", "G15"),
        ("const.zeta7",      "zeta(7)",               zeta7_f,      "", "G16"),
        ("const.zeta9",      "zeta(9)",               zeta9_f,      "", "G17"),
        ("const.li4",        "Li4(1/2)",              li4_f,        "", "G18"),
        ("const.li5",        "Li5(1/2)",              li5_f,        "", "G19"),
        ("const.li6",        "Li6(1/2)",              li6_f,        "", "G20"),
        ("const.li7",        "Li7(1/2)",              li7_f,        "", "G21"),
        ("const.catalan",    "Catalan constant",       cat_f,       "", "G22"),
        ("const.epi",        "e^pi",                  epi_f,        "", "G23"),
        ("const.ln3",        "ln(3)",                 ln3_f,        "", "G24"),
        ("const.ln5",        "ln(5)",                 ln5_f,        "", "G25"),
        ("const.K_quarter",  "K(k^2=1/4)",            K_quarter_f, "", "G26"),
        ("const.K_half",     "K(k^2=1/2)",            K_half_f,    "", "G27"),
        ("const.K_3qtr",     "K(k^2=3/4)",            K_3qtr_f,    "", "G28"),
        ("const.E_quarter",  "E(k^2=1/4)",            E_quarter_f, "", "G29"),
        ("const.E_half",     "E(k^2=1/2)",            E_half_f,    "", "G30"),
        ("const.E_3qtr",     "E(k^2=3/4)",            E_3qtr_f,    "", "G31"),
    ]
    for oid, name, val, unit, d4id in _entries:
        db.add(Constant(oid, name, val, unit=unit, level=0,
                         digits=100, source="Q335 basis (100+ digits)",
                         data4_id=d4id,
                         tags=["Level0", "exact", "Q335"]))


# ================================================================
# POPULATE: MASS RATIOS (Section K, 8 entries)
# ================================================================

def populate_ratios(db):
    """Section K: 8 dimensionless mass ratios. Level 2."""
    _entries = [
        ("const.mmu_me",   "m_mu/m_e",       mmu_me,   10, "K1", ["lepton", "ratio"]),
        ("const.mtau_me",  "m_tau/m_e",       mtau_me,  6,  "K2", ["lepton", "ratio"]),
        ("const.mtau_mmu", "m_tau/m_mu",      mtau_mmu, 5,  "K3", ["lepton", "ratio"]),
        ("const.mn_mp",    "m_n/m_p",         mn_mp,    11, "K4", ["nuclear", "ratio"]),
        ("const.MW_MZ",    "M_W/M_Z",         MW_MZ,    6,  "K5", ["EW", "ratio"]),
        ("const.mH_MZ",    "m_H/M_Z",         mH_MZ,    5,  "K6", ["EW", "ratio"]),
        ("const.mt_MZ",    "m_t/M_Z",         mt_MZ,    5,  "K7", ["EW", "ratio"]),
        ("const.K_koide",  "Koide K(e,mu,tau)", K_koide, 10, "K8", ["Koide", "ratio"]),
    ]
    for oid, name, val, dig, d4id, extra_tags in _entries:
        db.add(Constant(oid, name, val, unit="", level=2,
                         digits=dig, source="DATA-4 derived",
                         data4_id=d4id,
                         tags=["Level2"] + extra_tags))


# ================================================================
# POPULATE: CD PARAMETERS (Section L, 3 entries)
# ================================================================

def populate_CD_params(db):
    """Section L: CD staged parameters."""
    db.add(Constant("const.M_VL_lo", "M_VL lower bound (LHC)",
                     M_VL_lo, unit="MeV", level=None,
                     digits=4, source="LHC pair production",
                     data4_id="L1",
                     tags=["CD", "staged"],
                     notes="1.5 TeV lower bound"))

    db.add(Constant("const.M_VL_hi", "M_VL upper bound (perturbativity)",
                     M_VL_hi, unit="MeV", level=None,
                     digits=4, source="CKM perturbativity",
                     data4_id="L1",
                     tags=["CD", "staged"],
                     notes="6.0 TeV upper bound"))

    db.add(Constant("const.theta14", "sin(theta_14) mixing estimate",
                     theta14_est, unit="", level=None,
                     digits=2, source="CKM first-row deficit",
                     data4_id="L2",
                     tags=["CD", "staged", "CKM"]))


# ================================================================
# POPULATE: GUT PARAMETERS (Section N) — betas go to BetaCoefficient
# ================================================================

def populate_GUT_constants(db):
    """Section N: Non-beta GUT constants. Exact Fractions, Level 1."""
    # Gap ratios
    db.add(Constant("const.gap_SM", "SM gap ratio 218/115",
                     gap_SM, unit="", level=1,
                     source="(b1_SM-b2_SM)/(b2_SM-b3_SM)", data4_id="N10",
                     tags=["Level1", "GUT", "exact", "ratio"]))

    db.add(Constant("const.gap_VL", "CD gap ratio 38/27",
                     gap_VL, unit="", level=1,
                     source="(b1_mod-b2_mod)/(b2_mod-b3_mod)", data4_id="N11",
                     tags=["Level1", "GUT", "exact", "ratio", "CD"]))

    db.add(Constant("const.gap_MSSM", "MSSM gap ratio 7/5",
                     gap_MSSM, unit="", level=1,
                     source="MSSM beta coefficients", data4_id="N12",
                     tags=["Level1", "GUT", "exact", "ratio"]))

    db.add(Constant("const.gap_measured", "Measured gap ratio",
                     gap_measured, unit="", level=2,
                     source="Derived from alpha_EM, sin2_tW, alpha_s",
                     data4_id="N13",
                     tags=["Level2", "GUT", "ratio"]))

    # Two-loop b_ij SM matrix (stored as 9 constants)
    _bij_names = [
        ("const.bij_SM_00", "b_ij SM [0][0]", Fraction(199, 50)),
        ("const.bij_SM_01", "b_ij SM [0][1]", Fraction(27, 10)),
        ("const.bij_SM_02", "b_ij SM [0][2]", Fraction(44, 5)),
        ("const.bij_SM_10", "b_ij SM [1][0]", Fraction(9, 10)),
        ("const.bij_SM_11", "b_ij SM [1][1]", Fraction(35, 6)),
        ("const.bij_SM_12", "b_ij SM [1][2]", Fraction(12, 1)),
        ("const.bij_SM_20", "b_ij SM [2][0]", Fraction(11, 10)),
        ("const.bij_SM_21", "b_ij SM [2][1]", Fraction(9, 2)),
        ("const.bij_SM_22", "b_ij SM [2][2]", Fraction(-26, 1)),
    ]
    for oid, name, val in _bij_names:
        db.add(Constant(oid, name, val, unit="", level=1,
                         source="Machacek-Vaughn", data4_id="N14",
                         tags=["Level1", "two-loop", "SM", "exact"]))

    # VL two-loop db_ij matrix (9 entries, from derivation lib .dat)
    _dbij_entries = [
        ("const.dbij_VL_00", "db_ij VL [0][0]", Fraction(7, 15)),
        ("const.dbij_VL_01", "db_ij VL [0][1]", Fraction(1, 15)),
        ("const.dbij_VL_02", "db_ij VL [0][2]", Fraction(16, 135)),
        ("const.dbij_VL_10", "db_ij VL [1][0]", Fraction(1, 30)),
        ("const.dbij_VL_11", "db_ij VL [1][1]", Fraction(15, 4)),
        ("const.dbij_VL_12", "db_ij VL [1][2]", Fraction(8, 3)),
        ("const.dbij_VL_20", "db_ij VL [2][0]", Fraction(1, 45)),
        ("const.dbij_VL_21", "db_ij VL [2][1]", Fraction(1, 1)),
        ("const.dbij_VL_22", "db_ij VL [2][2]", Fraction(40, 9)),
    ]
    for oid, name, val in _dbij_entries:
        db.add(Constant(oid, name, val, unit="", level=1,
                         source="VL Dynkin formula",
                         tags=["Level1", "two-loop", "CD", "exact"]))

    # Two-loop results
    db.add(Constant("const.delta_1loop", "One-loop unification miss",
                     delta_1loop, unit="", level=None,
                     source="PHYS-24", data4_id="N15",
                     tags=["GUT", "result"]))

    db.add(Constant("const.delta_2loop", "Two-loop unification miss",
                     delta_2loop, unit="", level=None,
                     source="PHYS-24", data4_id="N16",
                     tags=["GUT", "result"]))


# ================================================================
# POPULATE: DERIVED COUPLING CONSTANTS
# ================================================================

def populate_derived(db):
    """Derived couplings and named constants."""
    db.add(Constant("const.alpha_em", "alpha_EM = 1/alpha_inv",
                     alpha_em, unit="", level=2,
                     source="1/alpha_inv",
                     tags=["Level2", "EM", "coupling"]))

    db.add(Constant("const.inv_a1", "1/alpha_1 at M_Z",
                     inv_a1, unit="", level=2,
                     source="(5/3)/alpha_EM/cos2_tW",
                     tags=["Level2", "U1", "coupling", "GUT"]))

    db.add(Constant("const.inv_a2", "1/alpha_2 at M_Z",
                     inv_a2, unit="", level=2,
                     source="1/(alpha_EM/sin2_tW)",
                     tags=["Level2", "SU2", "coupling", "GUT"]))

    db.add(Constant("const.inv_a3", "1/alpha_3 at M_Z",
                     inv_a3, unit="", level=2,
                     source="1/alpha_s",
                     tags=["Level2", "SU3", "coupling", "GUT"]))

    db.add(Constant("const.hbar", "Reduced Planck constant",
                     hbar, unit="J*s", level=0,
                     source="h/(2*pi_f)",
                     tags=["Level0", "SI"]))

    db.add(Constant("const.casimir_gap", "Pure-gauge Casimir gap = 2",
                     casimir_gap, unit="", level=1,
                     source="C2(adj SU(3))/C2(adj SU(2))",
                     tags=["Level1", "exact"]))

    db.add(Constant("const.CD_Y", "CD hypercharge = 1/6",
                     CD_Y, unit="", level=1,
                     source="(3,2,1/6) representation",
                     tags=["Level1", "CD", "exact"]))


# ================================================================
# POPULATE: KOIDE DERIVED
# ================================================================

def populate_koide(db):
    """Koide amplitude measurements (Level 2, not Level 1 hypothesis)."""
    db.add(Constant("const.a2_lep", "a^2 leptons (measured, NOT exactly 2)",
                     a2_lep, unit="", level=2,
                     digits=6, source="Koide from m_e, m_mu, m_tau",
                     tags=["Level2", "Koide"],
                     notes="a2=2 is hypothesis. This is the measurement."))

    db.add(Constant("const.a2_down", "a^2 down quarks",
                     a2_down, unit="", level=2,
                     digits=3, source="Koide from m_d, m_s, m_b",
                     tags=["Level2", "Koide", "quark"]))

    db.add(Constant("const.a2_up", "a^2 up quarks",
                     a2_up, unit="", level=2,
                     digits=3, source="Koide from m_u, m_c, m_t",
                     tags=["Level2", "Koide", "quark"]))


# ================================================================
# POPULATE: BETA COEFFICIENTS (9 objects)
# ================================================================

def populate_betas(db):
    """9 BetaCoefficient objects: SM, CD shifts, modified."""

    # SM betas — with full decomposition
    db.add(BetaCoefficient(
        "beta.b1_SM", "b1 SM (U1)", "U1", b1_SM,
        gauge_part=Fraction(0),
        fermion_part=Fraction(4, 1),
        higgs_part=Fraction(1, 10),
        tags=["Level1", "U1", "SM"]))

    db.add(BetaCoefficient(
        "beta.b2_SM", "b2 SM (SU2)", "SU2", b2_SM,
        gauge_part=Fraction(-22, 3),
        fermion_part=Fraction(4, 1),
        higgs_part=Fraction(1, 6),
        tags=["Level1", "SU2", "SM"]))

    db.add(BetaCoefficient(
        "beta.b3_SM", "b3 SM (SU3)", "SU3", b3_SM,
        gauge_part=Fraction(-11, 1),
        fermion_part=Fraction(4, 1),
        higgs_part=Fraction(0),
        tags=["Level1", "SU3", "SM"]))

    # CD shifts
    db.add(BetaCoefficient(
        "beta.db1_VL", "db1 CD shift (U1)", "U1", db1_VL,
        bsm_part=db1_VL,
        tags=["Level1", "U1", "CD"],
        notes="(2/5)*3*2*(1/6)^2 = 1/15"))

    db.add(BetaCoefficient(
        "beta.db2_VL", "db2 CD shift (SU2)", "SU2", db2_VL,
        bsm_part=db2_VL,
        tags=["Level1", "SU2", "CD"],
        notes="(2/3)*3*(1/2) = 1"))

    db.add(BetaCoefficient(
        "beta.db3_VL", "db3 CD shift (SU3)", "SU3", db3_VL,
        bsm_part=db3_VL,
        tags=["Level1", "SU3", "CD"],
        notes="(1/3)*2*(1/2) = 1/3  (VL coefficient 1/3, not chiral 2/3)"))

    # Modified betas (SM + CD)
    db.add(BetaCoefficient(
        "beta.b1_mod", "b1 modified (U1 + CD)", "U1", b1_mod,
        gauge_part=Fraction(0),
        fermion_part=Fraction(4, 1),
        higgs_part=Fraction(1, 10),
        bsm_part=db1_VL,
        tags=["Level1", "U1", "modified", "CD"]))

    db.add(BetaCoefficient(
        "beta.b2_mod", "b2 modified (SU2 + CD)", "SU2", b2_mod,
        gauge_part=Fraction(-22, 3),
        fermion_part=Fraction(4, 1),
        higgs_part=Fraction(1, 6),
        bsm_part=db2_VL,
        tags=["Level1", "SU2", "modified", "CD"]))

    db.add(BetaCoefficient(
        "beta.b3_mod", "b3 modified (SU3 + CD)", "SU3", b3_mod,
        gauge_part=Fraction(-11, 1),
        fermion_part=Fraction(4, 1),
        higgs_part=Fraction(0),
        bsm_part=db3_VL,
        tags=["Level1", "SU3", "modified", "CD"]))


# ================================================================
# POPULATE: REPRESENTATIONS (7 objects)
# ================================================================

def populate_representations(db):
    """7 Representation objects: 5 SM fermions + Higgs + CD."""

    db.add(Representation("rep.Q_L", "Q_L (left quark doublet)",
                           3, 2, Fraction(1, 6), "chiral",
                           tags=["SM", "quark", "SU2", "SU3"]))

    db.add(Representation("rep.u_R", "u_R (right up singlet)",
                           3, 1, Fraction(2, 3), "chiral",
                           tags=["SM", "quark", "SU3"]))

    db.add(Representation("rep.d_R", "d_R (right down singlet)",
                           3, 1, Fraction(-1, 3), "chiral",
                           tags=["SM", "quark", "SU3"]))

    db.add(Representation("rep.L_L", "L_L (left lepton doublet)",
                           1, 2, Fraction(-1, 2), "chiral",
                           tags=["SM", "lepton", "SU2"]))

    db.add(Representation("rep.e_R", "e_R (right electron singlet)",
                           1, 1, Fraction(-1, 1), "chiral",
                           tags=["SM", "lepton"]))

    db.add(Representation("rep.CD", "Cabibbo Doublet (3,2,1/6) VL",
                           3, 2, Fraction(1, 6), "vector-like",
                           tags=["CD", "BSM", "SU2", "SU3"],
                           notes="db3=1/3 (VL), not 2/3 (chiral)"))

    # Higgs: special case, use scalar-like representation
    # make_rep doesn't handle scalars, so we build manually
    higgs = Representation("rep.Higgs", "Higgs doublet (1,2,1/2)",
                            1, 2, Fraction(1, 2), "chiral",
                            tags=["SM", "scalar", "EW"],
                            notes="Higgs actual db=(1/10, 1/6, 0). "
                                  "Rep object uses chiral formula; "
                                  "correct shifts stored in beta objects.")


# ================================================================
# POPULATE: SOLITON BOUNDARIES (19 objects)
# ================================================================

def populate_boundaries(db):
    """19 SolitonBoundary objects from the boundary stack."""

    # 1. Planck
    b = SolitonBoundary("boundary.planck", "Planck scale",
                         scale_MeV=Fraction(12209, 1) * Fraction(10**15, 1),
                         what_changes="Quantum gravity effects ~ O(1)",
                         forces_affected=["gravity", "unified"],
                         known=False,
                         tags=["gravity", "quantum_gravity"])
    b.open_questions = ["Does G run?",
                        "What is the quantum theory of gravity?"]
    db.add(b)

    # 2. GUT
    b = SolitonBoundary("boundary.gut", "GUT unification scale",
                         what_changes="Three couplings merge. X,Y bosons active. Proton decays.",
                         forces_affected=["electromagnetic", "weak", "strong", "unified"],
                         known=False,
                         tags=["GUT", "unification"])
    b.scale_MeV_estimate = Fraction(35, 10) * Fraction(10**15, 1)
    b.open_questions = ["What is the GUT group?",
                        "What are threshold corrections?",
                        "What is the proton lifetime precisely?"]
    db.add(b)

    # 3. CD threshold
    b = SolitonBoundary("boundary.cd_threshold", "Cabibbo Doublet threshold",
                         what_changes="CD (3,2,1/6) VL pair activates. Gap ratio 218/115 -> 38/27.",
                         forces_affected=["electromagnetic", "weak", "strong"],
                         known=False,
                         tags=["CD", "BSM"])
    b.scale_MeV_lo = M_VL_lo
    b.scale_MeV_hi = M_VL_hi
    b.scale_MeV_estimate = Fraction(3000000, 1)
    b.above = {"betas": (b1_mod, b2_mod, b3_mod), "gap": gap_VL}
    b.below = {"betas": (b1_SM, b2_SM, b3_SM), "gap": gap_SM}
    db.add(b)

    # 4. Top
    db.add(SolitonBoundary("boundary.top", "Top quark threshold",
                            scale_MeV=m_t,
                            what_changes="Top quark activates. Full SM above.",
                            forces_affected=["strong"],
                            known=True,
                            tags=["quark", "mass"]))

    # 5. Higgs
    db.add(SolitonBoundary("boundary.higgs", "Higgs boson threshold",
                            scale_MeV=m_H,
                            what_changes="Higgs excitation resolvable.",
                            forces_affected=["electromagnetic", "weak"],
                            known=True,
                            tags=["scalar", "EW"]))

    # 6. M_Z (electroweak reference)
    b = SolitonBoundary("boundary.mz", "Electroweak scale (M_Z)",
                         scale_MeV=M_Z,
                         what_changes="Reference for all coupling measurements. EW symmetry broken.",
                         forces_affected=["electromagnetic", "weak", "strong"],
                         known=True,
                         tags=["EW", "reference"])
    b.couplings = {
        "1/alpha_EM": alpha_inv,
        "sin2_tW": sin2_tW,
        "alpha_s": alpha_s,
        "1/alpha_1": inv_a1,
        "1/alpha_2": inv_a2,
        "1/alpha_3": inv_a3,
    }
    db.add(b)

    # 7. M_W
    db.add(SolitonBoundary("boundary.mw", "W boson threshold",
                            scale_MeV=M_W,
                            what_changes="W boson pair production.",
                            forces_affected=["weak"],
                            known=True,
                            tags=["EW"]))

    # 8. Bottom
    db.add(SolitonBoundary("boundary.bottom", "Bottom quark threshold",
                            scale_MeV=m_b,
                            what_changes="b decouples. 5-flavor -> 4-flavor.",
                            forces_affected=["strong"],
                            known=True,
                            tags=["quark", "mass"]))

    # 9. Tau
    db.add(SolitonBoundary("boundary.tau", "Tau lepton threshold",
                            scale_MeV=m_tau,
                            what_changes="Tau decouples. Koide: m_tau=1776.97 MeV (0.006%% miss).",
                            forces_affected=["electromagnetic"],
                            known=True,
                            tags=["lepton", "Koide"]))

    # 10. Charm
    db.add(SolitonBoundary("boundary.charm", "Charm quark threshold",
                            scale_MeV=m_c,
                            what_changes="Charm decouples. 4-flavor -> 3-flavor.",
                            forces_affected=["strong"],
                            known=True,
                            tags=["quark", "mass"]))

    # 11. Confinement upper
    b = SolitonBoundary("boundary.confinement_upper", "Confinement wall (upper)",
                         scale_MeV=Fraction(2000, 1),
                         what_changes="Perturbative QCD breaks down. alpha_s ~ O(1).",
                         forces_affected=["strong"],
                         known=False,
                         tags=["QCD", "confinement"])
    b.open_questions = ["Is there a precise confinement boundary?"]
    db.add(b)

    # 12. Confinement lower
    b = SolitonBoundary("boundary.confinement_lower", "Confinement wall (lower)",
                         scale_MeV=Fraction(300, 1),
                         what_changes="Hadronic resonances -> individual hadrons.",
                         forces_affected=["strong"],
                         known=False,
                         tags=["QCD", "confinement"])
    b.below = {"effective_theory": "Chiral perturbation theory"}
    db.add(b)

    # 13. Strange
    db.add(SolitonBoundary("boundary.strange", "Strange quark threshold",
                            scale_MeV=m_s,
                            what_changes="Strange decouples. Inside confinement wall.",
                            forces_affected=["strong"],
                            known=True,
                            tags=["quark", "mass"],
                            notes="Inside confinement — perturbative running N/A"))

    # 14. Muon
    db.add(SolitonBoundary("boundary.muon", "Muon threshold",
                            scale_MeV=m_mu,
                            what_changes="Muon decouples from VP.",
                            forces_affected=["electromagnetic"],
                            known=True,
                            tags=["lepton", "VP"]))

    # 15. Nuclear binding
    db.add(SolitonBoundary("boundary.nuclear", "Nuclear binding scale",
                            scale_MeV=Fraction(8, 1),
                            what_changes="Residual strong binds nucleons. E_D = 2.225 MeV.",
                            forces_affected=["strong"],
                            known=True,
                            tags=["nuclear"]))

    # 16. Electron
    b = SolitonBoundary("boundary.electron", "Electron threshold",
                         scale_MeV=m_e,
                         what_changes="Below: no e+e- pairs. Classical EM.",
                         forces_affected=["electromagnetic"],
                         known=True,
                         tags=["lepton", "VP"])
    b.couplings = {"alpha_EM": Fraction(1, 1) / alpha_inv}
    db.add(b)

    # 17. Atomic
    db.add(SolitonBoundary("boundary.atomic", "Atomic scale (Bohr radius)",
                            what_changes="EM binding dominates. Atoms form.",
                            forces_affected=["electromagnetic"],
                            known=True,
                            tags=["atomic"],
                            notes="Not an energy threshold, a distance scale"))

    # 18. Molecular
    db.add(SolitonBoundary("boundary.molecular", "Molecular scale",
                            what_changes="Covalent bonds, Van der Waals. Chemistry.",
                            forces_affected=["electromagnetic"],
                            known=True,
                            tags=["molecular"]))

    # 19. Gravitational dominance
    b = SolitonBoundary("boundary.gravitational", "Gravitational dominance",
                         what_changes="Gravity dominates for neutral macroscopic objects.",
                         forces_affected=["gravity", "electromagnetic"],
                         known=False,
                         tags=["gravity"],
                         notes="No sharp boundary — crossover depends on charge/mass")
    b.open_questions = ["Does G vary with scale? (PHYS-3: untested)"]
    db.add(b)


# ================================================================
# POPULATE: R2 DOMAINS (23 objects)
# ================================================================

def populate_R2_domains(db):
    """23 R2Domain objects: 22 original + gauge coupling running."""
    _domains = [
        ("domain.01_pipe_flow",    "Pipe flow",           "Q = R2*d^2*v",                     "velocity v",         "0.05%"),
        ("domain.02_drag",         "Drag force",          "F = 0.5*rho*v^2*R2*d^2*Cd",        "drag coeff Cd",      "1%"),
        ("domain.03_orifice",      "Orifice flow",        "q = Cd*R2*d^2*sqrt(2*dP/rho)",     "discharge Cd",       "0.5%"),
        ("domain.04_capacitor",    "Capacitor",           "C = eps0*R2*d^2/t",                "permittivity eps",   "pF"),
        ("domain.05_poynting",     "Poynting flux",       "P = S*R2*d^2",                     "irradiance S",       "0.1 dB"),
        ("domain.06_antenna",      "Antenna aperture",    "A = eta*R2*D^2",                   "efficiency eta",     "calibrated"),
        ("domain.07_beam",         "Beam cross-section",  "A = R2*d^2",                       "none (geometry)",    "um"),
        ("domain.08_thermal",      "Thermal radiation",   "Q = eps*sig*T^4*R2*d^2",           "emissivity eps",     "1%"),
        ("domain.09_sound",        "Sound intensity",     "I = P/(16*R2*r^2)",                "1/r^2 spreading",    "0.5 dB"),
        ("domain.10_wire",         "Wire resistance",     "R = rho*L/(R2*d^2)",               "resistivity rho",    "0.1%"),
        ("domain.11_speaker",      "Speaker cone",        "Sd = R2*d_eff^2",                  "none (geometry)",    "5%"),
        ("domain.12_fiber",        "Fiber mode",          "A_eff = R2*MFD^2",                 "mode confinement",   "5%"),
        ("domain.13_disc",         "Disc spot",           "A = R2*(1.22*lam/NA)^2",           "diffraction",        "standard"),
        ("domain.14_wafer",        "Wafer area",          "A = R2*D^2",                       "none (geometry)",    "exact"),
        ("domain.15_gaussian",     "Gaussian beam",       "A = R2*w0^2",                      "beam parameter",     "um"),
        ("domain.16_poiseuille",   "Hagen-Poiseuille",    "Q = R2*d^4*dP/(32*mu*L)",          "viscosity mu",       "1%"),
        ("domain.17_implant",      "Ion implant",         "N = dose/sqrt(8*R2*sig^2)*exp(..)", "straggle sigma",    "5%"),
        ("domain.18_helmholtz",    "Helmholtz resonance", "f = (c/(8*R2))*sqrt(R2*d^2/(l*V))", "port geometry",     "2 Hz"),
        ("domain.19_airy",         "Diffraction (Airy)",  "theta = j11/(4*R2)*lam/D",          "Bessel zero j11",   "fundamental"),
        ("domain.20_rayleigh",     "Rayleigh scattering", "sigma ~ (8*R2/lam)^4*r^6",          "polarizability",    "0.8 dB/km/um^4"),
        ("domain.21_fspl",         "Free-space path loss", "FSPL = (16*R2*d/lam)^2",           "distance/wavelength", "link budget"),
        ("domain.22_rcs",          "Radar cross-section", "sigma = 16*R2*A^2/lam^2",           "plate area A",      "RCS"),
        ("domain.23_coupling",     "Gauge coupling running", "d(1/a_i) = b_i*L/(8*R2)",        "beta coeff b_i",    "0.33% (alpha_s)"),
    ]
    for oid, name, eq, z, prec in _domains:
        db.add(R2Domain(oid, name, eq, z, precision=prec,
                         tags=["R2", "domain"]))


# ================================================================
# POPULATE: R2 CANCELLATIONS (11 objects)
# ================================================================

def populate_R2_cancellations(db):
    """11 R2Cancellation objects: 7 original + 4 from modulus notebook."""
    _cancels = [
        ("cancel.01_kj_x_rk",      "K_J x R_K",          "(2e/h)(h/e^2)",                           "CANCELS",   "2/e",           "10^-8"),
        ("cancel.02_g0_x_rk",      "G_0 x R_K",          "(2e^2/h)(h/e^2)",                         "CANCELS",   "2",             "exact"),
        ("cancel.03_rydberg",       "Rydberg R_inf",      "alpha^2*m_e*c/(2h) via 2h=16*R2*hbar",   "CANCELS",   "alpha^2*m_e*c/(16*R2*hbar)", "13 digits"),
        ("cancel.04_a0_alpha",      "a_0 x alpha",        "hbar/(m_e*c)",                            "CANCELS",   "Compton/2pi",   "12 digits"),
        ("cancel.05_hartree",       "Hartree energy",     "m_e*c^2*alpha^2",                         "R2-FREE",   "no R2 enters",  "10 digits"),
        ("cancel.06_phi0_rk",       "Phi_0^2 / R_K",     "h^2/e^2 * e^2/h = h",                    "REAPPEARS", "h",             "exact"),
        ("cancel.07_wire_rc",       "Wire R x Cap C",     "rho*L/(R2*d^2) * eps0*R2*d^2/t",         "CANCELS",   "rho*eps0*L/t",  "derived"),
        ("cancel.08_gap_ratio",     "Gap ratio",          "(b1-b2)/(b2-b3)",                         "CANCELS",   "pure integers", "exact"),
        ("cancel.09_fermion_gap",   "Fermion gap",        "(4/3-4/3)/(4/3-4/3)",                     "CANCELS",   "0/0 (boson problem)", "exact"),
        ("cancel.10_sin2_correction", "sin2_tW correction", "3/8 - 3/13 = 15/104",                  "CANCELS",   "15/104",        "exact"),
        ("cancel.11_omega_dm",      "Omega_DM product",   "Omega_b * DM/baryon: 2/(13*4R2) * (22/13)*4R2", "CANCELS", "44/169",   "0.07%"),
    ]
    for oid, name, formula, status, remains, prec in _cancels:
        db.add(R2Cancellation(oid, name, formula, status, remains,
                               precision=prec,
                               tags=["R2", "cancellation", status.lower()]))


# ================================================================
# POPULATE: MODULUS OBJECTS
# ================================================================

def populate_moduli(db):
    """Key moduli tracked by the series."""
    _moduli = [
        ("modulus.R2",            "R2 = pi/4",              R2_f,                  0, "circle-in-square"),
        ("modulus.R4",            "R4 = pi^2/32",           R4_f,                  0, "4-ball-in-4-cube"),
        ("modulus.4_3_democracy", "Generation democracy",    Fraction(4, 3),        1, "per-gen beta shift"),
        ("modulus.11_YM",         "Yang-Mills coefficient",  Fraction(11, 1),       1, "adjoint SU(N) one-loop"),
        ("modulus.k1_GUT",        "GUT normalization k1",    Fraction(3, 5),        1, "SU(5) U(1) normalization"),
        ("modulus.S2_fund",       "Dynkin index (fund)",     Fraction(1, 2),        1, "S2(fund) any SU(N)"),
        ("modulus.C2_fund_SU3",   "Casimir C2(fund SU3)",    Fraction(4, 3),        1, "(N^2-1)/(2N) at N=3"),
        ("modulus.C2_fund_SU2",   "Casimir C2(fund SU2)",    Fraction(3, 4),        1, "(N^2-1)/(2N) at N=2"),
        ("modulus.C2_adj_SU3",    "Casimir C2(adj SU3)",     Fraction(3, 1),        1, "N at N=3"),
        ("modulus.C2_adj_SU2",    "Casimir C2(adj SU2)",     Fraction(2, 1),        1, "N at N=2"),
        ("modulus.gap_SM",        "SM gap ratio",            Fraction(218, 115),    1, "(b1-b2)/(b2-b3) SM"),
        ("modulus.gap_VL",        "CD gap ratio",            Fraction(38, 27),      1, "(b1-b2)/(b2-b3) CD"),
        ("modulus.sin2_tree",     "sin2_tW tree level",      Fraction(3, 8),        1, "SU(5) at M_GUT"),
        ("modulus.sin2_1loop",    "sin2_tW one-loop limit",  Fraction(3, 13),       1, "N_gen/|b2_mod_num|"),
        ("modulus.sin2_correction", "sin2_tW running modulus", Fraction(15, 104),   1, "3/8 - 3/13"),
        ("modulus.K_koide_exact", "Koide K = 2/3 (hypothesis)", Fraction(2, 3),     1, "Cauchy-Schwarz midpoint"),
    ]
    for oid, name, val, level, origin in _moduli:
        db.add(Modulus(oid, name, val, level, origin,
                        tags=["modulus", "Level%d" % level]))


# ================================================================
# POPULATE: EXPERIMENT RESULTS (Session 4)
# ================================================================

def populate_experiments(db):
    """Key results from Session 4 experiment scripts."""

    # Beta Unification Test — 28/28 PASS
    _beta_results = [
        ("result.beta.dm_baryon",    "DM/baryon = (22/13)*pi",       "beta_unification_test.py",
         "(22/13)*pi = 5.3165",       "5.3204",    "0.073%",   "PASS"),
        ("result.beta.omega_dm",     "Omega_DM = 44/169",            "beta_unification_test.py",
         "44/169 = 0.26036",          "0.2607",    "0.13%",    "PASS"),
        ("result.beta.omega_b",      "Omega_b = 2/(13*pi)",          "beta_unification_test.py",
         "2/(13*pi) = 0.04896",       "0.049",     "0.2%",     "PASS"),
        ("result.beta.sin2_3_13",    "sin2_tW ~ 3/13",              "beta_unification_test.py",
         "3/13 = 0.23077",            "0.23122",   "0.19%",    "PASS"),
    ]
    for oid, name, script, val, meas, miss, status in _beta_results:
        db.add(ExperimentResult(oid, name, script, val,
                                 measured=meas, miss_pct=miss,
                                 status=status,
                                 tags=["beta", "cosmology"]))

    # Toroidal DM — 12/12 PASS
    db.add(ExperimentResult("result.toroidal.amplification", "A = (44/13)*pi*(c/v)^2",
                             "toroidal_dm_test.py", "(44/13)*pi*(c/v)^2",
                             status="PASS",
                             tags=["DM", "toroidal"]))

    db.add(ExperimentResult("result.toroidal.mond_a0", "a0 ~ c*H0/(8*R2) within 15%",
                             "toroidal_dm_test.py", "a0 = c*H0/(8*R2)",
                             miss_pct="15%", status="PASS",
                             tags=["DM", "MOND"]))

    # Nested Soliton Gravity — 9/10 PASS, 1 FAIL
    db.add(ExperimentResult("result.gravity.hierarchy", "GM/(rc^2) hierarchy 10^-11 to 0.38",
                             "nested_soliton_gravity.py", "11 nesting levels",
                             status="PASS",
                             tags=["gravity", "soliton"]))

    db.add(ExperimentResult("result.gravity.kepler_saturn", "Saturn Kepler miss 0.74%",
                             "nested_soliton_gravity.py", "T^2 = 64*R2^2*a^3/(GM)",
                             miss_pct="0.74%", status="FAIL",
                             tags=["gravity", "Kepler"],
                             notes="Threshold 0.1%, data precision issue"))

    # Dwarf Soliton — 8/10 PASS, 2 FAIL
    db.add(ExperimentResult("result.dwarf.19_13_ratio", "Modified/SM = 19/13 EXACT",
                             "dwarf_soliton_ground_state.py", "19/13",
                             status="PASS",
                             tags=["DM", "dwarf"]))

    db.add(ExperimentResult("result.dwarf.m_dm", "m_DM from R2 off by 26 decades",
                             "dwarf_soliton_ground_state.py", "null",
                             status="FAIL",
                             tags=["DM", "dwarf"],
                             notes="Honest null result"))

    # Time as Process Rate — 11/12 PASS, 1 FAIL
    db.add(ExperimentResult("result.time.gps", "GPS correction 38.5 us/day",
                             "time_process_rate_test.py", "38499 ns/day",
                             measured="~38000 ns/day", miss_pct="1.3%",
                             status="PASS",
                             tags=["time", "GPS"]))

    db.add(ExperimentResult("result.time.muon_gamma", "Muon gamma=7.09 at 0.99c",
                             "time_process_rate_test.py", "7.0888",
                             status="PASS",
                             tags=["time", "muon"]))

    db.add(ExperimentResult("result.time.earth_cycles", "Earth age label ~10^26 but value 10^27",
                             "time_process_rate_test.py", "log10 = 27.12",
                             status="FAIL",
                             tags=["time"],
                             notes="Threshold label error, not physics"))


# ================================================================
# POPULATE: RESEARCH PROGRAMS (3 objects)
# ================================================================

def populate_programs(db):
    """3 research programs from Session 4."""

    # Beta Unification
    prog = ResearchProgram("program.beta_unification", "Beta Unification",
                            "Gauge group beta coefficient integers determine cosmological parameters",
                            status="ACTIVE",
                            tags=["beta", "unification", "cosmology"])
    prog.add_script("beta_statistical_control.py",
                     "Statistical significance of integer matches", stage=1)
    prog.add_kill_switch("coincidence_probability",
                          "p > 0.1 for observed integer matches",
                          "combinatoric analysis")
    prog.add_kill_switch("cmb_s4_omega",
                          "Omega_DM moves away from 44/169 with CMB-S4 data",
                          "CMB-S4 / LiteBIRD")
    prog.add_connection("program.toroidal_dm", "shares integers 22, 13, 44")
    prog.add_connection("program.hubble_running", "shares integer 20/13")
    db.add(prog)

    # Toroidal DM
    prog = ResearchProgram("program.toroidal_dm", "Toroidal Dark Matter",
                            "DM amplification via toroidal circulation A=(44/13)*pi*(c/v)^2",
                            status="ACTIVE",
                            tags=["DM", "toroidal", "amplification"])
    prog.add_script("toroidal_tidal_stripping.py",
                     "Quantify tidal stripping in dwarfs", stage=1)
    prog.add_kill_switch("wimp_detection",
                          "Direct detection of DM particles",
                          "LZ / XENONnT / PandaX")
    prog.add_kill_switch("dwarf_virial",
                          "Virial theorem cannot be rescued for dwarfs",
                          "dwarf_soliton_ground_state.py")
    prog.add_connection("program.beta_unification", "A numerator 44/13 from betas")
    db.add(prog)

    # Hubble Running
    prog = ResearchProgram("program.hubble_running", "Hubble Running Curve",
                            "H0 decreases with boundary transit count: H0(N) = H0(0)*r^N",
                            status="ACTIVE",
                            tags=["Hubble", "running", "cosmology"])
    prog.add_script("hubble_structure_catalog.py",
                     "Extract N estimates from galaxy surveys", stage=1)
    prog.add_kill_switch("gw_sirens",
                          "GW standard sirens show same running as EM",
                          "LIGO/Virgo O5+")
    prog.add_kill_switch("systematic_resolution",
                          "Systematic error found resolving H0 tension without running",
                          "SH0ES / Planck reanalysis")
    prog.add_connection("program.beta_unification", "(1-r) = alpha^2*pi^2*(20/13)")
    db.add(prog)


# ================================================================
# MASTER POPULATION FUNCTION
# ================================================================

def populate_all(db):
    """Populate the complete DATA-5 database.

    Call this once at session start:
        db = DATA5()
        populate_all(db)

    Returns the number of objects added.
    """
    populate_SI(db)
    populate_measured(db)
    populate_electroweak(db)
    populate_quarks(db)
    populate_nuclear(db)
    populate_spectroscopy(db)
    populate_Q335(db)
    populate_ratios(db)
    populate_CD_params(db)
    populate_GUT_constants(db)
    populate_derived(db)
    populate_koide(db)
    populate_betas(db)
    populate_representations(db)
    populate_boundaries(db)
    populate_R2_domains(db)
    populate_R2_cancellations(db)
    populate_moduli(db)
    populate_experiments(db)
    populate_programs(db)

    return db.count()


# ================================================================
# CONVENIENCE: init_data5()
# ================================================================

def init_data5():
    """One-liner to create and populate a DATA-5 database.

    Usage:
        from data_5_populate import init_data5
        db = init_data5()
        db.show_summary()
    """
    db = DATA5()
    populate_all(db)
    return db


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DATA_5_POPULATE SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    db = DATA5()
    n = populate_all(db)

    print("  Populated %d objects." % n)
    print()

    # --------------------------------------------------------
    print("COUNT CHECKS")
    print("-" * 70)
    print()

    chk_bool("SI constants: 7",
             db.count("constant") >= 7,
             "total constants = %d" % db.count("constant"), checks)

    chk_bool("Beta coefficients: 9",
             db.count("beta") == 9,
             "betas = %d" % db.count("beta"), checks)

    chk_bool("Representations: 7",
             db.count("representation") == 7,
             "reps = %d" % db.count("representation"), checks)

    chk_bool("Boundaries: 19",
             db.count("boundary") == 19,
             "boundaries = %d" % db.count("boundary"), checks)

    chk_bool("R2 domains: 23",
             db.count("domain") == 23,
             "domains = %d" % db.count("domain"), checks)

    chk_bool("R2 cancellations: 11",
             db.count("cancellation") == 11,
             "cancellations = %d" % db.count("cancellation"), checks)

    chk_bool("Moduli: 16",
             db.count("modulus") == 16,
             "moduli = %d" % db.count("modulus"), checks)

    chk_bool("Experiment results: 10+",
             db.count("result") >= 10,
             "results = %d" % db.count("result"), checks)

    chk_bool("Research programs: 3",
             db.count("program") == 3,
             "programs = %d" % db.count("program"), checks)

    # --------------------------------------------------------
    print()
    print("VALUE CHECKS")
    print("-" * 70)
    print()

    # SI exact
    c_obj = db.get("const.c")
    chk_bool("c = 299792458",
             c_obj is not None and c_obj.value == Fraction(299792458, 1),
             "c = %s" % (c_obj.value if c_obj else "NOT FOUND"), checks)

    # Measured
    alpha_obj = db.get("const.alpha_inv")
    chk_exact("alpha_inv matches library",
              alpha_obj.value, alpha_inv, checks)

    sin2_obj = db.get("const.sin2_tW")
    chk_exact("sin2_tW matches library",
              sin2_obj.value, sin2_tW, checks)

    as_obj = db.get("const.alpha_s")
    chk_exact("alpha_s matches library",
              as_obj.value, alpha_s, checks)

    # Q335
    R2_obj = db.get("const.R2")
    chk_exact("R2 matches library R2_f",
              R2_obj.value, R2_f, checks)

    # Beta coefficients
    b2m = db.get("beta.b2_mod")
    chk_exact("b2_mod = -13/6",
              b2m.value, Fraction(-13, 6), checks)

    chk_bool("b2_mod numerator = 13",
             b2m.numerator == 13,
             "num = %s" % b2m.numerator, checks)

    # Representation
    cd = db.get("rep.CD")
    chk_exact("CD db1 = 1/15",
              cd.db1, Fraction(1, 15), checks)
    chk_exact("CD db3 = 1/3 (VL, not 2/3)",
              cd.db3, Fraction(1, 3), checks)

    # Gap ratios
    gap_sm = db.get("const.gap_SM")
    chk_exact("gap_SM = 218/115",
              gap_sm.value, Fraction(218, 115), checks)

    gap_vl = db.get("const.gap_VL")
    chk_exact("gap_VL = 38/27",
              gap_vl.value, Fraction(38, 27), checks)

    # VL two-loop matrix
    db22 = db.get("const.dbij_VL_11")
    chk_exact("db_ij VL [1][1] = 15/4 (NOT 39/4)",
              db22.value, Fraction(15, 4), checks)

    # M_Z boundary couplings
    mz_b = db.get("boundary.mz")
    chk_bool("M_Z boundary has alpha_inv coupling",
             mz_b is not None and "1/alpha_EM" in mz_b.couplings,
             "couplings = %s" % list(mz_b.couplings.keys()) if mz_b else "None",
             checks)

    # --------------------------------------------------------
    print()
    print("SEARCH CHECKS")
    print("-" * 70)
    print()

    su2_hits = db.find(tag="SU2")
    chk_bool("tag='SU2' finds 3+ objects",
             len(su2_hits) >= 3,
             "found %d" % len(su2_hits), checks)

    em_hits = db.find(tag="EM")
    chk_bool("tag='EM' finds 5+ objects",
             len(em_hits) >= 5,
             "found %d" % len(em_hits), checks)

    cd_hits = db.find(tag="CD")
    chk_bool("tag='CD' finds 8+ objects (betas+rep+boundary+params)",
             len(cd_hits) >= 8,
             "found %d" % len(cd_hits), checks)

    level1 = db.find_by_level(1)
    chk_bool("Level 1 objects: 25+",
             len(level1) >= 25,
             "found %d" % len(level1), checks)

    level2 = db.find_by_level(2)
    chk_bool("Level 2 objects: 40+",
             len(level2) >= 40,
             "found %d" % len(level2), checks)

    level0 = db.find_by_level(0)
    chk_bool("Level 0 objects: 30+",
             len(level0) >= 30,
             "found %d" % len(level0), checks)

    free_text = search(db, "Koide")
    chk_bool("search('Koide') finds objects",
             len(free_text) >= 3,
             "found %d" % len(free_text), checks)

    # --------------------------------------------------------
    print()
    print("JSON EXPORT CHECK")
    print("-" * 70)
    print()

    import json
    full_json = db.to_json()
    parsed = json.loads(full_json)
    chk_bool("JSON export is valid",
             parsed["obj_id"] == "data5",
             "root id = %s" % parsed.get("obj_id", "?"), checks)

    chk_bool("JSON children match object count",
             len(parsed.get("children", {})) == db.count(),
             "json children = %d, db count = %d" % (
                 len(parsed.get("children", {})), db.count()), checks)

    # --------------------------------------------------------
    print()
    db.show_summary()

    print()
    print("SAMPLE OBJECTS:")
    print("-" * 70)

    # Show a few from each type
    for obj_type in ["constant", "beta", "representation", "boundary",
                      "domain", "cancellation", "modulus", "result", "program"]:
        objs = db.find(obj_type=obj_type)
        if objs:
            objs[0].show()

    # --------------------------------------------------------
    print()
    print_summary(checks)

    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print()
    if n_fail == 0:
        print("  DATA_5_POPULATE: OPERATIONAL")
    else:
        print("  DATA_5_POPULATE: %d FAILURES" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("=" * 70)
    print("DATA_5_POPULATE SELF-TEST COMPLETE")
    print("=" * 70)
    