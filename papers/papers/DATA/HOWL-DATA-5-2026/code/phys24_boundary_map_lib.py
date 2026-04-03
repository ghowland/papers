#!/usr/bin/env python3
"""
HOWL PHYS-24 BOUNDARY MAP LIBRARY
====================================
The complete map of physical reality from cosmological to Planck scale,
organized as a traversable boundary stack.

Every boundary has: a scale, what changes there, coupling values
(or None if unknown), which forces are affected, and links to
other data objects in the platform.

The map has holes. Holes are marked with None and tagged with
what would be needed to fill them. This is not a weakness —
it is the honest state of knowledge.

Import:
    from phys24_lib import *
    from phys24_structures import *
    from phys24_boundaries import *

Platform: phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from mpmath import pi as mpi, log as mlog, exp as mexp


# ================================================================
# FORCES
# ================================================================

FORCES = {
    "gravity": {
        "name": "Gravity",
        "gauge_group": None,
        "coupling_name": "G_N",
        "coupling_var": None,       # not in phys24_lib — no quantum theory
        "mediator": "graviton (hypothetical)",
        "range": "infinite",
        "status": "classical only — no verified quantum description",
        "papers": ["PHYS-3"],
        "notes": "G untested across any soliton boundary (PHYS-3)",
    },
    "electromagnetic": {
        "name": "Electromagnetism",
        "gauge_group": "U(1)_EM",
        "coupling_name": "alpha_EM",
        "coupling_var": "alpha_inv",
        "mediator": "photon",
        "range": "infinite",
        "status": "complete QFT, tested to 4.3 ppb (PHYS-9)",
        "papers": ["PHYS-5", "PHYS-9", "PHYS-12"],
    },
    "weak": {
        "name": "Weak force",
        "gauge_group": "SU(2)_L",
        "coupling_name": "alpha_2",
        "coupling_var": "sin2_tW",  # extracted via alpha_EM/sin2_tW
        "mediator": "W+, W-, Z0",
        "range": "~10^-18 m (1/M_W)",
        "status": "complete QFT, broken by Higgs mechanism",
        "papers": ["PHYS-12"],
    },
    "strong": {
        "name": "Strong force (QCD)",
        "gauge_group": "SU(3)_c",
        "coupling_name": "alpha_s",
        "coupling_var": "alpha_s",
        "mediator": "8 gluons",
        "range": "~10^-15 m (confinement)",
        "status": "complete QFT, non-perturbative below ~2 GeV",
        "papers": ["PHYS-6"],
    },
    "unified": {
        "name": "Unified force (hypothetical)",
        "gauge_group": "SU(5) or SO(10) or larger",
        "coupling_name": "alpha_GUT",
        "coupling_var": None,       # not measured
        "mediator": "X, Y bosons + SM mediators",
        "range": "~10^-31 m (1/M_GUT)",
        "status": "hypothetical — Cabibbo Doublet framework predicts M_GUT ~ 10^15.5 GeV",
        "papers": ["PHYS-13", "PHYS-15", "PHYS-20"],
    },
}


# ================================================================
# SCALE CONVERSIONS
# ================================================================

# hbar*c in MeV*m (for converting between energy and distance)
# hbar*c = h*c/(2*pi) = 197.3269804 MeV*fm = 197.3269804e-15 MeV*m
hbar_c_MeV_fm = Fraction(1973269804, 10**7)  # MeV*fm, 10 sf

def energy_to_distance_fm(E_MeV):
    """Convert energy scale (MeV) to distance scale (fm).
    lambda = hbar*c / E.
    """
    return f2m(hbar_c_MeV_fm) / f2m(E_MeV) if isinstance(E_MeV, Fraction) else f2m(hbar_c_MeV_fm) / E_MeV

def distance_fm_to_energy(d_fm):
    """Convert distance scale (fm) to energy scale (MeV).
    E = hbar*c / lambda.
    """
    return f2m(hbar_c_MeV_fm) / d_fm

# Common distance scales for reference
DISTANCE_SCALES = {
    "Planck_length":     {"fm": mpf("1.616e-20"),    "meters": mpf("1.616e-35")},
    "proton_radius":     {"fm": mpf("0.84"),          "meters": mpf("8.4e-16")},
    "nuclear_radius":    {"fm": mpf("1.2"),           "meters": mpf("1.2e-15")},
    "atom_radius":       {"fm": mpf("5.29e4"),        "meters": mpf("5.29e-11")},
    "virus":             {"fm": mpf("1e8"),            "meters": mpf("1e-7")},
    "cell":              {"fm": mpf("1e10"),           "meters": mpf("1e-5")},
    "orange":            {"fm": mpf("1e14"),           "meters": mpf("0.1")},
    "earth_radius":      {"fm": mpf("6.371e21"),      "meters": mpf("6.371e6")},
    "earth_sun":         {"fm": mpf("1.496e26"),      "meters": mpf("1.496e11")},
    "observable_universe": {"fm": mpf("4.4e40"),      "meters": mpf("4.4e25")},
}


# ================================================================
# THE BOUNDARY STACK
# ================================================================
# Every boundary where the rules of physics change.
# Ordered from highest energy (smallest distance) to lowest.
# Each boundary has:
#   scale_MeV: energy in MeV (Fraction if known, None if unknown)
#   scale_fm: distance in fm (computed or None)
#   name: human-readable name
#   what_changes: what physical rules change at this boundary
#   above: dict of properties above this boundary
#   below: dict of properties below this boundary
#   forces_affected: list of force keys
#   couplings_at_boundary: dict of coupling values (or None)
#   known: True if scale is measured, False if theoretical, None if unknown
#   data4_entry: DATA-4 entry ID if applicable
#   papers: list of PHYS papers
#   open_questions: list of unresolved issues at this boundary

BOUNDARY_STACK = [

    # ============================================================
    # PLANCK BOUNDARY
    # ============================================================
    {
        "name": "Planck scale",
        "scale_MeV": Fraction(12209, 1) * Fraction(10**15, 1),  # ~1.22e19 GeV
        "scale_fm": mpf("1.616e-20"),
        "what_changes": "Quantum gravity effects become order 1. "
                        "Spacetime geometry itself may be quantized.",
        "above": {
            "description": "Unknown. Possibly string/quantum gravity regime.",
            "rules": None,
        },
        "below": {
            "description": "QFT on classical spacetime background.",
            "rules": "Standard gauge theory applies.",
        },
        "forces_affected": ["gravity", "unified"],
        "couplings_at_boundary": {
            "G_N": None,            # G at Planck scale unknown
            "alpha_GUT": None,      # coupling at Planck unknown
        },
        "known": False,
        "data4_entry": None,
        "papers": ["PHYS-3"],
        "open_questions": [
            "Does G run?",
            "What is the quantum theory of gravity?",
            "Is there a desert between M_GUT and M_Planck?",
        ],
    },

    # ============================================================
    # GUT BOUNDARY
    # ============================================================
    {
        "name": "GUT unification scale",
        "scale_MeV": None,          # computed, not measured
        "scale_MeV_estimate": Fraction(3000000, 1),  # 3 TeV midpoint of [1.5, 6] TeV window
        "scale_fm": None,           # computed from energy
        "what_changes": "Three gauge couplings merge into one. "
                        "SU(3)xSU(2)xU(1) -> SU(5) or larger. "
                        "X, Y gauge bosons become active. Proton can decay.",
        "above": {
            "description": "Unified gauge theory. One coupling.",
            "rules": "SU(5) or SO(10) gauge symmetry.",
            "active_particles": "X, Y bosons, color triplet Higgs, Sigma fields + all SM",
        },
        "below": {
            "description": "SM gauge theory with separate couplings.",
            "rules": "SU(3)xSU(2)xU(1) with beta coefficients.",
        },
        "forces_affected": ["electromagnetic", "weak", "strong", "unified"],
        "couplings_at_boundary": {
            "1/alpha_GUT": None,     # estimated ~42 from CD running
            "1/alpha_1": None,       # = 1/alpha_GUT at unification
            "1/alpha_2": None,       # = 1/alpha_GUT at unification
            "1/alpha_3": None,       # approximately 1/alpha_GUT (within Delta)
        },
        "known": False,
        "data4_entry": None,
        "papers": ["PHYS-13", "PHYS-15", "PHYS-20"],
        "open_questions": [
            "What is the GUT group? SU(5)? SO(10)?",
            "What are the threshold corrections?",
            "Does exact unification occur?",
            "What is the proton lifetime precisely?",
        ],
    },

    # ============================================================
    # CABIBBO DOUBLET BOUNDARY (STAGED)
    # ============================================================
    {
        "name": "Cabibbo Doublet threshold",
        "scale_MeV": None,          # in window [1.5e6, 6e6] MeV
        "scale_MeV_lo": M_VL_lo,    # 1.5 TeV = 1500000 MeV
        "scale_MeV_hi": M_VL_hi,    # 6.0 TeV = 6000000 MeV
        "scale_fm": None,
        "what_changes": "Cabibbo Doublet (3,2,1/6) VL pair becomes active. "
                        "Beta coefficients change: b_i -> b_i + Db_i. "
                        "Gap ratio changes from 218/115 to 38/27.",
        "above": {
            "description": "SM + Cabibbo Doublet.",
            "betas": (b1_mod, b2_mod, b3_mod),
            "gap_ratio": gap_VL,
        },
        "below": {
            "description": "Standard Model only.",
            "betas": (b1_SM, b2_SM, b3_SM),
            "gap_ratio": gap_SM,
        },
        "forces_affected": ["electromagnetic", "weak", "strong"],
        "couplings_at_boundary": {
            "1/alpha_1": None,       # depends on M_VL
            "1/alpha_2": None,
            "1/alpha_3": None,
        },
        "known": False,              # staged, not measured
        "data4_entry": "L1",
        "papers": ["PHYS-15", "PHYS-16", "PHYS-19"],
        "open_questions": [
            "What is M_VL exactly?",
            "Is there a sharp threshold or smooth transition?",
            "What are the mixing angles?",
        ],
    },

    # ============================================================
    # TOP QUARK THRESHOLD
    # ============================================================
    {
        "name": "Top quark threshold",
        "scale_MeV": m_t,
        "scale_fm": energy_to_distance_fm(m_t),
        "what_changes": "Top quark becomes active. Last SM fermion threshold. "
                        "Full SM particle content above this scale.",
        "above": {
            "description": "Full SM: 6 quarks, 3 leptons, gauge bosons, Higgs.",
            "n_f": 6,
        },
        "below": {
            "description": "5-flavor SM.",
            "n_f": 5,
        },
        "forces_affected": ["strong"],
        "couplings_at_boundary": {
            "alpha_s": None,         # alpha_s at m_t not directly in DATA-4
        },
        "known": True,
        "data4_entry": "C4",
        "papers": [],
        "open_questions": [],
    },

    # ============================================================
    # HIGGS THRESHOLD
    # ============================================================
    {
        "name": "Higgs boson threshold",
        "scale_MeV": m_H,
        "scale_fm": energy_to_distance_fm(m_H),
        "what_changes": "Higgs field excitation becomes resolvable. "
                        "Higgs contribution to beta functions active.",
        "above": {
            "description": "Higgs active as propagating degree of freedom.",
        },
        "below": {
            "description": "Higgs condensate present but not resolvable as particle.",
        },
        "forces_affected": ["electromagnetic", "weak"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "C5",
        "papers": ["PHYS-12"],
        "open_questions": [
            "Is lambda (Higgs self-coupling) derivable? (parked, PHYS-24 Appendix J)",
        ],
    },

    # ============================================================
    # Z BOSON / ELECTROWEAK SCALE
    # ============================================================
    {
        "name": "Electroweak scale (M_Z)",
        "scale_MeV": M_Z,
        "scale_fm": energy_to_distance_fm(M_Z),
        "what_changes": "Reference scale for all coupling measurements. "
                        "Electroweak symmetry is broken below this scale. "
                        "W and Z acquire mass.",
        "above": {
            "description": "Electroweak theory with massive W, Z.",
        },
        "below": {
            "description": "Same, but approaching b-quark threshold.",
        },
        "forces_affected": ["electromagnetic", "weak", "strong"],
        "couplings_at_boundary": {
            "1/alpha_EM": alpha_inv,           # DATA-4 B1
            "sin2_tW": sin2_tW,                 # DATA-4 B11
            "alpha_s": alpha_s,                 # DATA-4 B12
            "1/alpha_1": inv_a1,                # derived
            "1/alpha_2": inv_a2,                # derived
            "1/alpha_3": inv_a3,                # derived
        },
        "known": True,
        "data4_entry": "C1",
        "papers": ["PHYS-12", "PHYS-13"],
        "open_questions": [],
    },

    # ============================================================
    # W BOSON THRESHOLD
    # ============================================================
    {
        "name": "W boson threshold",
        "scale_MeV": M_W,
        "scale_fm": energy_to_distance_fm(M_W),
        "what_changes": "W boson pair production threshold.",
        "above": {"description": "W bosons resolvable."},
        "below": {"description": "W exchange only virtual."},
        "forces_affected": ["weak"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "C3",
        "papers": ["PHYS-12"],
        "open_questions": [],
    },

    # ============================================================
    # BOTTOM QUARK THRESHOLD
    # ============================================================
    {
        "name": "Bottom quark threshold",
        "scale_MeV": m_b,
        "scale_fm": energy_to_distance_fm(m_b),
        "what_changes": "Bottom quark decouples below this scale. "
                        "Effective theory changes from 5-flavor to 4-flavor.",
        "above": {"n_f": 5},
        "below": {"n_f": 4},
        "forces_affected": ["strong"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "D5",
        "papers": [],
        "open_questions": [],
    },

    # ============================================================
    # TAU LEPTON THRESHOLD
    # ============================================================
    {
        "name": "Tau lepton threshold",
        "scale_MeV": m_tau,
        "scale_fm": energy_to_distance_fm(m_tau),
        "what_changes": "Tau lepton decouples. "
                        "Koide prediction: m_tau = 1776.97 MeV (0.006%% miss).",
        "above": {"description": "3 charged leptons active."},
        "below": {"description": "2 charged leptons active."},
        "forces_affected": ["electromagnetic"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "B4",
        "papers": ["PHYS-8", "PHYS-23"],
        "open_questions": [
            "Is m_tau derivable from Koide? (conditional, a^2=2 unresolved)",
        ],
    },

    # ============================================================
    # CHARM QUARK THRESHOLD
    # ============================================================
    {
        "name": "Charm quark threshold",
        "scale_MeV": m_c,
        "scale_fm": energy_to_distance_fm(m_c),
        "what_changes": "Charm decouples. 4-flavor to 3-flavor.",
        "above": {"n_f": 4},
        "below": {"n_f": 3},
        "forces_affected": ["strong"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "D4",
        "papers": [],
        "open_questions": [],
    },

    # ============================================================
    # CONFINEMENT WALL (UPPER)
    # ============================================================
    {
        "name": "Confinement wall (upper face)",
        "scale_MeV": Fraction(2000, 1),  # ~2 GeV, approximate
        "scale_fm": energy_to_distance_fm(Fraction(2000, 1)),
        "what_changes": "Perturbative QCD breaks down. "
                        "alpha_s approaches O(1). "
                        "Integer beta function rules cease to apply. "
                        "This is the OUTSIDE face of the confinement wall.",
        "above": {
            "description": "Perturbative QCD. Integer rules apply.",
            "alpha_s_regime": "perturbative (alpha_s < 0.5)",
        },
        "below": {
            "description": "Non-perturbative. Confinement zone.",
            "alpha_s_regime": "non-perturbative (alpha_s ~ O(1))",
        },
        "forces_affected": ["strong"],
        "couplings_at_boundary": {
            "alpha_s": None,         # alpha_s at 2 GeV not precisely defined
        },
        "known": False,              # boundary is approximate, not sharp
        "data4_entry": None,
        "papers": ["PHYS-6"],
        "open_questions": [
            "Is there a precise definition of the confinement boundary?",
            "What is alpha_s at the transition?",
        ],
    },

    # ============================================================
    # CONFINEMENT WALL (LOWER)
    # ============================================================
    {
        "name": "Confinement wall (lower face)",
        "scale_MeV": Fraction(300, 1),   # ~300 MeV = Lambda_QCD, approximate
        "scale_fm": energy_to_distance_fm(Fraction(300, 1)),
        "what_changes": "Hadronic resonances resolve into individual hadrons. "
                        "Below this scale, quarks are confined inside hadrons. "
                        "This is the INSIDE face of the confinement wall.",
        "above": {
            "description": "Non-perturbative QCD. Resonances, glueballs.",
        },
        "below": {
            "description": "Hadronic physics. Pions, protons, neutrons.",
            "effective_theory": "Chiral perturbation theory",
        },
        "forces_affected": ["strong"],
        "couplings_at_boundary": {
            "alpha_s": None,
            "f_pi": Fraction(13041, 100),  # pion decay constant ~130.41 MeV
        },
        "known": False,
        "data4_entry": None,
        "papers": ["PHYS-6"],
        "open_questions": [
            "What is the non-perturbative structure of the confinement transition?",
            "Is there a soliton interpretation of confinement?",
        ],
    },

    # ============================================================
    # STRANGE QUARK THRESHOLD
    # ============================================================
    {
        "name": "Strange quark threshold",
        "scale_MeV": m_s,
        "scale_fm": energy_to_distance_fm(m_s),
        "what_changes": "Strange quark decouples. 3-flavor to 2-flavor. "
                        "Note: this is INSIDE the confinement wall — the "
                        "threshold is real but perturbative beta running "
                        "does not apply here.",
        "above": {"n_f": 3},
        "below": {"n_f": 2},
        "forces_affected": ["strong"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "D3",
        "papers": [],
        "open_questions": [
            "What is the correct treatment of flavor thresholds inside confinement?",
        ],
    },

    # ============================================================
    # MUON THRESHOLD
    # ============================================================
    {
        "name": "Muon threshold",
        "scale_MeV": m_mu,
        "scale_fm": energy_to_distance_fm(m_mu),
        "what_changes": "Muon decouples from vacuum polarization.",
        "above": {"description": "e + mu contribute to VP."},
        "below": {"description": "Electron only in VP."},
        "forces_affected": ["electromagnetic"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": "B3",
        "papers": ["PHYS-5"],
        "open_questions": [],
    },

    # ============================================================
    # NUCLEAR BINDING SCALE
    # ============================================================
    {
        "name": "Nuclear binding scale",
        "scale_MeV": Fraction(8, 1),  # ~8 MeV per nucleon binding
        "scale_fm": energy_to_distance_fm(Fraction(8, 1)),
        "what_changes": "Nuclear force (residual strong) binds nucleons. "
                        "Deuteron binding energy E_D = 2.225 MeV.",
        "above": {"description": "Free nucleons."},
        "below": {"description": "Bound nuclei."},
        "forces_affected": ["strong"],
        "couplings_at_boundary": {
            "E_D": E_D,               # deuteron binding, DATA-4 E8
        },
        "known": True,
        "data4_entry": "E8",
        "papers": [],
        "open_questions": [],
    },

    # ============================================================
    # ELECTRON THRESHOLD
    # ============================================================
    {
        "name": "Electron threshold",
        "scale_MeV": m_e,
        "scale_fm": energy_to_distance_fm(m_e),
        "what_changes": "Electron-positron pairs can no longer be created. "
                        "Below this, only photons propagate freely.",
        "above": {"description": "QED with electron VP."},
        "below": {"description": "Classical electrodynamics. No VP."},
        "forces_affected": ["electromagnetic"],
        "couplings_at_boundary": {
            "alpha_EM": Fraction(1, 1) / alpha_inv,  # alpha at m_e ~ 1/137
        },
        "known": True,
        "data4_entry": "B2",
        "papers": ["PHYS-5", "PHYS-9"],
        "open_questions": [],
    },

    # ============================================================
    # ATOMIC SCALE
    # ============================================================
    {
        "name": "Atomic scale (Bohr radius)",
        "scale_MeV": None,          # not an energy threshold
        "scale_fm": mpf("5.29e4"),   # a_0 = 5.29e-11 m = 5.29e4 fm
        "what_changes": "Electromagnetic binding dominates. "
                        "Atoms form. Quantum mechanics governs structure.",
        "above": {"description": "Free electrons and nuclei."},
        "below": {"description": "Bound atoms. Chemistry begins."},
        "forces_affected": ["electromagnetic"],
        "couplings_at_boundary": {
            "alpha_EM": Fraction(1, 1) / alpha_inv,
            "a_0": a_0,               # DATA-4 B8
            "R_inf": R_inf,            # DATA-4 B7
        },
        "known": True,
        "data4_entry": "B8",
        "papers": ["PHYS-9"],
        "open_questions": [],
    },

    # ============================================================
    # MOLECULAR / CHEMICAL SCALE
    # ============================================================
    {
        "name": "Molecular scale",
        "scale_MeV": None,
        "scale_fm": mpf("1e6"),      # ~1 nm = 10^6 fm
        "what_changes": "Electromagnetic interactions between atoms form molecules. "
                        "Chemistry. Biology begins at larger scales.",
        "above": {"description": "Individual atoms."},
        "below": {"description": "Molecular structures. Van der Waals, covalent bonds."},
        "forces_affected": ["electromagnetic"],
        "couplings_at_boundary": {},
        "known": True,
        "data4_entry": None,
        "papers": [],
        "open_questions": [],
    },

    # ============================================================
    # GRAVITATIONAL DOMINANCE (macroscopic)
    # ============================================================
    {
        "name": "Gravitational dominance scale",
        "scale_MeV": None,
        "scale_fm": None,            # not a sharp boundary
        "scale_meters_approx": mpf("1e-1"),  # ~10 cm, roughly orange-size
        "what_changes": "Gravity becomes the dominant long-range force for "
                        "neutral massive objects. EM dominates for charged objects. "
                        "No sharp boundary — crossover depends on charge/mass ratio.",
        "above": {"description": "EM-dominated for charged, gravity for neutral."},
        "below": {"description": "Gravity dominates for macroscopic neutral objects."},
        "forces_affected": ["gravity", "electromagnetic"],
        "couplings_at_boundary": {
            "G_N": None,             # G_N not in phys24_lib
            "G_N_CODATA": "6.67430e-11 m^3 kg^-1 s^-2",  # reference only
        },
        "known": False,              # not a sharp boundary
        "data4_entry": None,
        "papers": ["PHYS-3"],
        "open_questions": [
            "Does G vary with scale? (PHYS-3: untested across boundaries)",
            "Is there a precise crossover scale?",
        ],
    },
]


# ================================================================
# BOUNDARY TRAVERSAL FUNCTIONS
# ================================================================

def get_boundary_by_name(name):
    """Find a boundary by name (case-insensitive substring match)."""
    name_lower = name.lower()
    return [b for b in BOUNDARY_STACK if name_lower in b["name"].lower()]


def boundaries_between_scales(E_lo_MeV, E_hi_MeV):
    """Return all boundaries between two energy scales (MeV).

    Args: E_lo_MeV, E_hi_MeV as Fraction or mpf
    Returns: list of boundary dicts, ordered low to high energy
    """
    lo = float(f2m(E_lo_MeV)) if isinstance(E_lo_MeV, Fraction) else float(E_lo_MeV)
    hi = float(f2m(E_hi_MeV)) if isinstance(E_hi_MeV, Fraction) else float(E_hi_MeV)
    if lo > hi:
        lo, hi = hi, lo

    result = []
    for b in BOUNDARY_STACK:
        scale = b.get("scale_MeV")
        if scale is None:
            # Check for estimate or window
            scale = b.get("scale_MeV_estimate")
        if scale is None:
            continue
        s = float(f2m(scale)) if isinstance(scale, Fraction) else float(scale)
        if lo <= s <= hi:
            result.append(b)

    result.sort(key=lambda b: float(f2m(b.get("scale_MeV") or b.get("scale_MeV_estimate", Fraction(0)))))
    return result


def traverse(start_scale_MeV, end_scale_MeV):
    """Traverse the boundary stack between two scales.

    Returns a report dict with:
      boundaries: list of boundaries crossed
      unknown_couplings: list of (boundary_name, coupling_name) with None values
      open_questions: list of all open questions along the path
      force_changes: list of (boundary_name, forces_affected)
      rule_changes: list of (boundary_name, what_changes)
    """
    boundaries = boundaries_between_scales(start_scale_MeV, end_scale_MeV)

    unknown_couplings = []
    open_questions = []
    force_changes = []
    rule_changes = []

    for b in boundaries:
        # Collect unknowns
        for coupling_name, value in b.get("couplings_at_boundary", {}).items():
            if value is None:
                unknown_couplings.append((b["name"], coupling_name))

        # Collect open questions
        for q in b.get("open_questions", []):
            open_questions.append((b["name"], q))

        # Collect force changes
        force_changes.append((b["name"], b.get("forces_affected", [])))

        # Collect rule changes
        rule_changes.append((b["name"], b["what_changes"]))

    return {
        "boundaries": boundaries,
        "count": len(boundaries),
        "unknown_couplings": unknown_couplings,
        "open_questions": open_questions,
        "force_changes": force_changes,
        "rule_changes": rule_changes,
    }


def print_traversal(start_MeV, end_MeV):
    """Print a human-readable traversal report."""
    report = traverse(start_MeV, end_MeV)

    print("=" * 70)
    print("BOUNDARY TRAVERSAL: %s MeV -> %s MeV" % (
        mp.nstr(f2m(start_MeV) if isinstance(start_MeV, Fraction) else start_MeV, 4),
        mp.nstr(f2m(end_MeV) if isinstance(end_MeV, Fraction) else end_MeV, 4)))
    print("=" * 70)
    print()
    print("  Boundaries crossed: %d" % report["count"])
    print()

    for b in report["boundaries"]:
        scale = b.get("scale_MeV")
        if scale is not None:
            print("  --- %s ---" % b["name"])
            print("      Scale: %s MeV" % mp.nstr(f2m(scale) if isinstance(scale, Fraction) else scale, 6))
            if b.get("scale_fm"):
                print("      Distance: %s fm" % mp.nstr(b["scale_fm"], 4))
        else:
            print("  --- %s ---" % b["name"])
            est = b.get("scale_MeV_estimate")
            if est:
                print("      Scale: ~%s MeV (estimated)" % mp.nstr(f2m(est), 4))
            else:
                print("      Scale: UNKNOWN")

        print("      Changes: %s" % b["what_changes"][:80])
        print("      Forces: %s" % ", ".join(b.get("forces_affected", [])))

        couplings = b.get("couplings_at_boundary", {})
        if couplings:
            for cn, cv in couplings.items():
                if cv is None:
                    print("      %s: UNKNOWN" % cn)
                elif isinstance(cv, Fraction):
                    print("      %s: %s" % (cn, mp.nstr(f2m(cv), 7)))
                elif isinstance(cv, str):
                    print("      %s: %s" % (cn, cv))
                else:
                    print("      %s: %s" % (cn, mp.nstr(cv, 7)))

        for q in b.get("open_questions", []):
            print("      ? %s" % q)
        print()

    if report["unknown_couplings"]:
        print("  UNKNOWN COUPLINGS:")
        for bname, cname in report["unknown_couplings"]:
            print("    - %s at %s" % (cname, bname))
        print()

    if report["open_questions"]:
        print("  OPEN QUESTIONS:")
        for bname, q in report["open_questions"]:
            print("    [%s] %s" % (bname, q))
        print()


# ================================================================
# SELF-TEST
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PHYS24_BOUNDARIES SELF-TEST")
    print("=" * 70)
    print()

    checks = []

    # --------------------------------------------------------
    print("BOUNDARY STACK")
    print("-" * 70)
    print()

    chk_bool("Boundary stack has 15+ entries",
             len(BOUNDARY_STACK) >= 15,
             "count = %d" % len(BOUNDARY_STACK), checks)

    # Check M_Z boundary has correct couplings
    mz_bounds = get_boundary_by_name("electroweak")
    chk_bool("Electroweak boundary found",
             len(mz_bounds) >= 1,
             "matches = %d" % len(mz_bounds), checks)

    if mz_bounds:
        mz_b = mz_bounds[0]
        chk_exact("M_Z boundary: alpha_inv stored",
                  mz_b["couplings_at_boundary"]["1/alpha_EM"],
                  alpha_inv, checks)
        chk_exact("M_Z boundary: sin2_tW stored",
                  mz_b["couplings_at_boundary"]["sin2_tW"],
                  sin2_tW, checks)
        chk_exact("M_Z boundary: alpha_s stored",
                  mz_b["couplings_at_boundary"]["alpha_s"],
                  alpha_s, checks)

    # --------------------------------------------------------
    print()
    print("TRAVERSAL: PROTON TO ORANGE")
    print("-" * 70)
    print()

    # Proton: ~938 MeV. Orange: ~0.1 m ~ 2e-12 MeV (using hbar*c/r)
    # But traversal works in energy, so orange is ~2e-12 MeV
    # Let's use electron scale (0.511 MeV) to proton scale (938 MeV)
    report = traverse(m_e, m_p)
    chk_bool("e to p: crosses confinement wall",
             any("Confinement" in b["name"] for b in report["boundaries"]),
             "boundaries: %s" % [b["name"] for b in report["boundaries"]],
             checks)

    # --------------------------------------------------------
    print()
    print("TRAVERSAL: M_Z TO GUT")
    print("-" * 70)
    print()

    report_gut = traverse(M_Z, Fraction(10**19, 1))
    chk_bool("M_Z to GUT: crosses CD threshold",
             any("Cabibbo" in b["name"] for b in report_gut["boundaries"]),
             "boundaries: %s" % [b["name"] for b in report_gut["boundaries"]],
             checks)

    chk_bool("M_Z to GUT: has unknown couplings",
             len(report_gut["unknown_couplings"]) > 0,
             "unknowns: %d" % len(report_gut["unknown_couplings"]),
             checks)

    chk_bool("M_Z to GUT: has open questions",
             len(report_gut["open_questions"]) > 0,
             "questions: %d" % len(report_gut["open_questions"]),
             checks)

    # --------------------------------------------------------
    print()
    print("FORCES REGISTRY")
    print("-" * 70)
    print()

    chk_bool("5 forces registered",
             len(FORCES) == 5,
             "count = %d" % len(FORCES), checks)

    chk_bool("Gravity has no gauge group",
             FORCES["gravity"]["gauge_group"] is None,
             "gauge_group = %s" % FORCES["gravity"]["gauge_group"],
             checks)

    chk_bool("Strong force is SU(3)",
             FORCES["strong"]["gauge_group"] == "SU(3)_c",
             "gauge_group = %s" % FORCES["strong"]["gauge_group"],
             checks)

    # --------------------------------------------------------
    print()
    print("SCALE CONVERSIONS")
    print("-" * 70)
    print()

    proton_fm = energy_to_distance_fm(m_p)
    chk_bool("Proton Compton wavelength ~ 0.2 fm",
             mpf("0.1") < proton_fm < mpf("0.5"),
             "lambda = %s fm" % mp.nstr(proton_fm, 4), checks)

    mz_fm = energy_to_distance_fm(M_Z)
    chk_bool("M_Z distance ~ 0.002 fm",
             mpf("0.001") < mz_fm < mpf("0.01"),
             "lambda = %s fm" % mp.nstr(mz_fm, 4), checks)

    # --------------------------------------------------------
    print()
    print("DEMO: FULL TRAVERSAL e -> GUT")
    print("-" * 70)
    print()

    print_traversal(m_e, Fraction(10**19, 1))

    # --------------------------------------------------------
    print()
    print_summary(checks)

    n_fail = sum(1 for _, s in checks if s == "FAIL")
    print()
    if n_fail == 0:
        print("  BOUNDARIES LIBRARY: OPERATIONAL")
    else:
        print("  BOUNDARIES LIBRARY: %d FAILURES" % n_fail)
        for tag, status in checks:
            if status == "FAIL":
                print("    - %s" % tag)

    print()
    print("=" * 70)
    print("PHYS24_BOUNDARIES SELF-TEST COMPLETE")
    print("=" * 70)
