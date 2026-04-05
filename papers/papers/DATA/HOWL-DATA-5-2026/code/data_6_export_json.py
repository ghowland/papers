#!/usr/bin/env python3
"""
DATA-6 JSON EXPORTER
=====================
Imports the HOWL platform libraries and exports all values,
connections, programs, and metadata to versioned JSON files.

Usage:
    Place in the same directory as phys24_lib.py and all
    platform libraries. Run:

        python data_6_export.py

    Output goes to ./data_6_export/ directory.

Rules:
    - No default values. Only export what the source contains.
    - Fraction serialized as {"_type": "Fraction", "num": str, "den": str}
      (string for large Q335 numerators that exceed JSON int limits)
    - mpf serialized as {"_type": "mpf", "value": "string"}
    - Grouped by section/topic. No mega files.
    - All filenames versioned with _v0.
"""

import sys
import os
import json

try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 100


# ================================================================
# OUTPUT SETUP
# ================================================================

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "data_6_export")
os.makedirs(OUTDIR, exist_ok=True)


def _json_default(obj):
    """JSON serializer for Fraction, mpf, and other types."""
    if isinstance(obj, Fraction):
        return {
            "_type": "Fraction",
            "num": str(obj.numerator),
            "den": str(obj.denominator),
        }
    if isinstance(obj, mpf):
        return {
            "_type": "mpf",
            "value": mp.nstr(obj, 30),
        }
    return str(obj)


def write_json(filename, data):
    """Write a JSON file to the export directory."""
    path = os.path.join(OUTDIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=_json_default)
    count = len(data) if isinstance(data, list) else len(data.get("nodes", data))
    print("  wrote %s (%d entries)" % (filename, count))


# ================================================================
# ENVELOPE BUILDER
# ================================================================


def _normalize_decimal(s):
    """Convert sci-notation string to plain decimal.
    '2.1969811e-6' -> '0.0000021969811'
    '6.674e-11' -> '0.00000000006674'
    '1.989e30' -> '1989000000000000000000000000000'
    '197.3269804' -> '197.3269804' (unchanged)
    Preserves all significant digits. No rounding.
    """
    s = s.strip()
    if "e" not in s.lower():
        return s
    coeff, exp = s.lower().split("e")
    exp = int(exp)
    sign = ""
    if coeff.startswith("-"):
        sign = "-"
        coeff = coeff[1:]
    if "." in coeff:
        integer_part, frac_part = coeff.split(".")
    else:
        integer_part = coeff
        frac_part = ""
    all_digits = integer_part + frac_part
    dot_pos = len(integer_part) + exp
    if dot_pos <= 0:
        return sign + "0." + "0" * (-dot_pos) + all_digits
    elif dot_pos >= len(all_digits):
        return sign + all_digits + "0" * (dot_pos - len(all_digits))
    else:
        return sign + all_digits[:dot_pos] + "." + all_digits[dot_pos:]


def make_value(key, value, unit, level, source,
               digits=None, section=None, notes=None,
               tags=None, legacy_refs=None, uncertainty=None,
               ref=None, pitfalls=None):
    """Build a DATA-6 value node dict."""
    # Determine value_type
    if value is None:
        vtype = "deferred"
    elif isinstance(value, Fraction):
        vtype = "exact_fraction"
    elif isinstance(value, int):
        vtype = "exact_integer"
    elif isinstance(value, str):
        if value in ("chiral", "vector-like", "vector_like",
                     "near_k_two_thirds", "far_from_k_two_thirds",
                     "weak", "strong", "intermediate"):
            vtype = "classification"
        else:
            vtype = "approximate"
            value = _normalize_decimal(value)
    elif isinstance(value, mpf):
        vtype = "approximate"
    else:
        vtype = "approximate"

    # Normalize uncertainty string if present
    if uncertainty is not None and isinstance(uncertainty, str):
        uncertainty = _normalize_decimal(uncertainty)

    # Extract topic and term from key
    parts = key.split("_")
    if parts[-1] == "v0":
        parts = parts[:-1]
    topic = parts[0] if parts else ""
    term = "_".join(parts[1:]) if len(parts) > 1 else ""

    node = {
        "key": key,
        "canonical": key.replace("_v0", ""),
        "version": 0,
        "node_type": "value",
        "topic": topic,
        "term": term,
        "level": level,
        "source": source,
        "value": value,
        "value_type": vtype,
        "unit": unit,
    }

    if digits is not None:
        node["digits"] = digits
    if section is not None:
        node["section"] = section
    if notes is not None:
        node["notes"] = notes
    if tags is not None:
        node["tags"] = tags
    if legacy_refs is not None:
        node["legacy_refs"] = legacy_refs
    if uncertainty is not None:
        node["uncertainty"] = uncertainty
    if ref is not None:
        node["ref"] = ref
    if pitfalls is not None:
        node["pitfalls"] = pitfalls

    return node

# ================================================================
# IMPORT PLATFORM LIBRARIES
# ================================================================

print("=" * 70)
print("DATA-6 JSON EXPORTER")
print("=" * 70)
print()
print("Importing platform libraries...")

from phys24_lib import *

try:
    from phys24_structure_lib import (
        CABIBBO_DOUBLET, Q_L, u_R, d_R, L_L, e_R, HIGGS,
        SM_GENERATION, PARTICLE_CATALOG,
        ANOMALIES, CLOSED_PATHS, PAPER_TOPICS, EXPERIMENTS,
        DATA4_MAP, ENERGY_DOMAINS, GUT_PARTICLES,
    )
    HAS_STRUCTURES = True
    print("  phys24_structure_lib: loaded")
except ImportError:
    HAS_STRUCTURES = False
    print("  phys24_structure_lib: NOT FOUND (skipping)")

try:
    from phys24_domain_lib import (
        R2, R4, EIGHT_R2, FOUR_R2, SIXTEEN_R2,
        J11, J01, AIRY_CONST, C_C_EXACT,
        OPTICAL_DISCS, FIBER_OPTICS, SPEAKERS,
        AWG_DATA, CU_RESISTIVITY, EPSILON_0,
        JUST_INTONATION, SAMPLE_RATES,
        STORAGE_INTERFACES, MEMORY_STANDARDS,
        RF_STANDARDS, SEMICONDUCTOR,
        BCS_DATA, DWDM_BANDS,
        R2_EQUATIONS, R2_CANCELLATIONS,
        SPEAKER_IMPEDANCES, RF_IMPEDANCES,
        FLOW_CONSTANTS, GEODESY, METROLOGY,
        MATH_NORMALIZATIONS,
    )
    HAS_DOMAIN = True
    print("  phys24_domain_lib: loaded")
except ImportError:
    HAS_DOMAIN = False
    print("  phys24_domain_lib: NOT FOUND (skipping)")

try:
    from phys24_hubble_lib import (
        H0_MEASUREMENTS, H0_ORDERED,
        H0_local, H0_far, cumulative_ratio,
        HYPOTHESIS_STATUS, STRUCTURAL_PARALLELS,
        SERIES_CONNECTIONS, VP_STEP_SIZE,
    )
    HAS_HUBBLE = True
    print("  phys24_hubble_lib: loaded")
except ImportError:
    HAS_HUBBLE = False
    print("  phys24_hubble_lib: NOT FOUND (skipping)")

try:
    from phys24_boundary_map_lib import (
        BOUNDARY_STACK, FORCES, DISTANCE_SCALES,
        hbar_c_MeV_fm as boundary_hbar_c,
    )
    HAS_BOUNDARY = True
    print("  phys24_boundary_map_lib: loaded")
except ImportError:
    HAS_BOUNDARY = False
    print("  phys24_boundary_map_lib: NOT FOUND (skipping)")

print()


# ================================================================
# EXPORT 1: SI EXACT CONSTANTS (Section A, 7 entries)
# ================================================================

print("EXPORTING VALUES...")
print("-" * 70)

si_nodes = [
    make_value("si_speed_of_light_v0", c, "m/s", 0,
               "SI 2019 (exact)", digits=9, section="SI",
               legacy_refs={"data4": "A1", "phys24": "c"}),
    make_value("si_planck_constant_v0", h_planck, "J*s", 0,
               "SI 2019 (exact)", digits=9, section="SI",
               legacy_refs={"data4": "A2", "phys24": "h_planck"}),
    make_value("si_elementary_charge_v0", e_charge, "C", 0,
               "SI 2019 (exact)", digits=10, section="SI",
               legacy_refs={"data4": "A3", "phys24": "e_charge"}),
    make_value("si_boltzmann_constant_v0", k_B, "J/K", 0,
               "SI 2019 (exact)", digits=7, section="SI",
               legacy_refs={"data4": "A4", "phys24": "k_B"}),
    make_value("si_avogadro_number_v0", N_A, "mol^-1", 0,
               "SI 2019 (exact)", digits=9, section="SI",
               legacy_refs={"data4": "A5", "phys24": "N_A"}),
    make_value("si_cesium_hyperfine_v0", dv_Cs, "Hz", 0,
               "SI 2019 (exact)", digits=10, section="SI",
               legacy_refs={"data4": "A6", "phys24": "dv_Cs"}),
    make_value("si_luminous_efficacy_v0", K_cd, "lm/W", 0,
               "SI 2019 (exact)", digits=3, section="SI",
               legacy_refs={"data4": "A7", "phys24": "K_cd"}),
]

write_json("values_si_exact_v0.json", {"nodes": si_nodes})


# ================================================================
# EXPORT 2: MEASURED CONSTANTS (Section B, 13 entries)
# ================================================================

measured_nodes = [
    make_value("coupling_alpha_em_inverse_v0", alpha_inv, "dimensionless", 2,
               "CODATA 2022", digits=12, section="measured",
               tags=["EM", "coupling"],
               legacy_refs={"data4": "B1", "phys24": "alpha_inv"}),
    make_value("mass_electron_v0", m_e, "MeV", 2,
               "CODATA 2022", digits=11, section="measured",
               tags=["lepton", "mass"],
               legacy_refs={"data4": "B2", "phys24": "m_e"}),
    make_value("mass_muon_v0", m_mu, "MeV", 2,
               "CODATA 2022", digits=10, section="measured",
               tags=["lepton", "mass"],
               legacy_refs={"data4": "B3", "phys24": "m_mu"}),
    make_value("mass_tau_v0", m_tau, "MeV", 2,
               "CODATA 2022", digits=6, section="measured",
               tags=["lepton", "mass", "Koide"],
               legacy_refs={"data4": "B4", "phys24": "m_tau"}),
    make_value("mass_proton_v0", m_p, "MeV", 2,
               "CODATA 2022", digits=11, section="measured",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "B5", "phys24": "m_p"}),
    make_value("ratio_proton_electron_mass_v0", mp_me, "dimensionless", 2,
               "CODATA 2022", digits=13, section="measured",
               tags=["ratio"],
               legacy_refs={"data4": "B6", "phys24": "mp_me"}),
    make_value("atomic_rydberg_constant_v0", R_inf, "m^-1", 2,
               "CODATA 2022", digits=13, section="measured",
               tags=["atomic"],
               legacy_refs={"data4": "B7", "phys24": "R_inf"}),
    make_value("atomic_bohr_radius_v0", a_0, "m", 2,
               "CODATA 2022", digits=12, section="measured",
               tags=["atomic"],
               legacy_refs={"data4": "B8", "phys24": "a_0"}),
    make_value("coupling_electron_anomalous_moment_v0", a_e, "dimensionless", 2,
               "CODATA 2022", digits=12, section="measured",
               tags=["EM"],
               legacy_refs={"data4": "B9", "phys24": "a_e"}),
    make_value("coupling_muon_anomalous_moment_v0", a_mu, "dimensionless", 2,
               "CODATA 2022", digits=9, section="measured",
               tags=["EM"],
               legacy_refs={"data4": "B10", "phys24": "a_mu"}),
    make_value("coupling_sin2_theta_w_v0", sin2_tW, "dimensionless", 2,
               "LEP-SLD", digits=5, section="measured",
               tags=["weak", "coupling", "EW"],
               legacy_refs={"data4": "B11", "phys24": "sin2_tW"}),
    make_value("coupling_alpha_s_mz_v0", alpha_s, "dimensionless", 2,
               "PDG", digits=4, section="measured",
               tags=["strong", "coupling", "QCD"],
               legacy_refs={"data4": "B12", "phys24": "alpha_s"}),
    make_value("coupling_vacuum_permeability_v0", mu_0, "N/A^2", 2,
               "CODATA 2022", digits=12, section="measured",
               tags=["EM"],
               legacy_refs={"data4": "B13", "phys24": "mu_0"}),
]

write_json("values_measured_v0.json", {"nodes": measured_nodes})


# ================================================================
# EXPORT 3: ELECTROWEAK OBSERVABLES (Section C, 6 entries)
# ================================================================

ew_nodes = [
    make_value("mass_z_boson_v0", M_Z, "MeV", 2,
               "LEP/PDG", digits=6, section="electroweak",
               tags=["EW", "PDG"],
               legacy_refs={"data4": "C1", "phys24": "M_Z"}),
    make_value("mass_z_boson_width_v0", Gamma_Z, "MeV", 2,
               "LEP/PDG", digits=5, section="electroweak",
               tags=["EW", "PDG"],
               legacy_refs={"data4": "C2", "phys24": "Gamma_Z"}),
    make_value("mass_w_boson_v0", M_W, "MeV", 2,
               "LEP/PDG", digits=6, section="electroweak",
               tags=["EW", "PDG"],
               legacy_refs={"data4": "C3", "phys24": "M_W"}),
    make_value("mass_top_quark_v0", m_t, "MeV", 2,
               "LEP/PDG", digits=5, section="electroweak",
               tags=["quark", "mass"],
               legacy_refs={"data4": "C4", "phys24": "m_t"}),
    make_value("mass_higgs_boson_v0", m_H, "MeV", 2,
               "LEP/PDG", digits=5, section="electroweak",
               tags=["scalar", "EW"],
               legacy_refs={"data4": "C5", "phys24": "m_H"}),
    make_value("coupling_fermi_constant_v0", G_F, "GeV^-2", 2,
               "LEP/PDG", digits=8, section="electroweak",
               tags=["EW"],
               legacy_refs={"data4": "C6", "phys24": "G_F"}),
]

write_json("values_electroweak_v0.json", {"nodes": ew_nodes})


# ================================================================
# EXPORT 4: QUARKS AND CKM (Section D, 11 entries)
# ================================================================

quark_nodes = [
    make_value("mass_up_quark_v0", m_u, "MeV", 2,
               "PDG 2024", digits=3, section="quarks",
               tags=["quark", "mass"],
               legacy_refs={"data4": "D1", "phys24": "m_u"},
               notes="MS-bar at 2 GeV"),
    make_value("mass_down_quark_v0", m_d, "MeV", 2,
               "PDG 2024", digits=3, section="quarks",
               tags=["quark", "mass"],
               legacy_refs={"data4": "D2", "phys24": "m_d"},
               notes="MS-bar at 2 GeV"),
    make_value("mass_strange_quark_v0", m_s, "MeV", 2,
               "PDG 2024", digits=3, section="quarks",
               tags=["quark", "mass"],
               legacy_refs={"data4": "D3", "phys24": "m_s"},
               notes="MS-bar at 2 GeV"),
    make_value("mass_charm_quark_v0", m_c, "MeV", 2,
               "PDG 2024", digits=4, section="quarks",
               tags=["quark", "mass"],
               legacy_refs={"data4": "D4", "phys24": "m_c"},
               notes="MS-bar at m_c"),
    make_value("mass_bottom_quark_v0", m_b, "MeV", 2,
               "PDG 2024", digits=4, section="quarks",
               tags=["quark", "mass"],
               legacy_refs={"data4": "D5", "phys24": "m_b"},
               notes="MS-bar at m_b"),
    make_value("ckm_sin_theta_12_v0", sin_t12, "dimensionless", 2,
               "PDG 2024", digits=5, section="quarks",
               tags=["CKM"],
               legacy_refs={"data4": "D6", "phys24": "sin_t12"}),
    make_value("ckm_sin_theta_23_v0", sin_t23, "dimensionless", 2,
               "PDG 2024", digits=4, section="quarks",
               tags=["CKM"],
               legacy_refs={"data4": "D7", "phys24": "sin_t23"}),
    make_value("ckm_sin_theta_13_v0", sin_t13, "dimensionless", 2,
               "PDG 2024", digits=4, section="quarks",
               tags=["CKM"],
               legacy_refs={"data4": "D8", "phys24": "sin_t13"}),
    make_value("ratio_charm_strange_lattice_v0", mc_ms, "dimensionless", 2,
               "FLAG lattice", digits=5, section="quarks",
               tags=["ratio", "FLAG"],
               legacy_refs={"data4": "D9", "phys24": "mc_ms"},
               notes="Independent of D3/D4. See DATA-4 Finding 15."),
    make_value("ratio_bottom_charm_lattice_v0", mb_mc, "dimensionless", 2,
               "FLAG lattice", digits=4, section="quarks",
               tags=["ratio", "FLAG"],
               legacy_refs={"data4": "D10", "phys24": "mb_mc"},
               notes="Independent of D4/D5. See DATA-4 Finding 15."),
    make_value("ratio_up_down_lattice_v0", mu_md, "dimensionless", 2,
               "FLAG lattice", digits=3, section="quarks",
               tags=["ratio", "FLAG"],
               legacy_refs={"data4": "D11", "phys24": "mu_md"},
               notes="Independent of D1/D2. See DATA-4 Finding 15."),
]

write_json("values_quarks_ckm_v0.json", {"nodes": quark_nodes})


# ================================================================
# EXPORT 5: NUCLEAR AND SPECTROSCOPY (Sections E + F, 9 entries)
# ================================================================

nuclear_nodes = [
    make_value("mass_neutron_v0", m_n, "MeV", 2,
               "CODATA 2022", digits=11, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E1", "phys24": "m_n"}),
    make_value("mass_neutron_proton_diff_v0", mn_mp_diff, "MeV", 2,
               "CODATA 2022", digits=8, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E2", "phys24": "mn_mp_diff"}),
    make_value("mass_pion_charged_v0", m_pi_p, "MeV", 2,
               "CODATA 2022", digits=8, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E3", "phys24": "m_pi_p"}),
    make_value("mass_pion_neutral_v0", m_pi_0, "MeV", 2,
               "CODATA 2022", digits=7, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E4", "phys24": "m_pi_0"}),
    make_value("mass_kaon_charged_v0", m_K_p, "MeV", 2,
               "CODATA 2022", digits=6, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E5", "phys24": "m_K_p"}),
    make_value("mass_deuteron_v0", m_D, "MeV", 2,
               "CODATA 2022", digits=12, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E6", "phys24": "m_D"}),
    make_value("mass_helium4_v0", m_He4, "MeV", 2,
               "CODATA 2022", digits=10, section="nuclear",
               tags=["nuclear", "mass"],
               legacy_refs={"data4": "E7", "phys24": "m_He4"}),
    make_value("energy_deuteron_binding_v0", E_D, "MeV", 2,
               "CODATA 2022", digits=8, section="nuclear",
               tags=["nuclear"],
               legacy_refs={"data4": "E8", "phys24": "E_D"}),
    make_value("spectro_hydrogen_1s2s_v0", H_1S2S, "Hz", 2,
               "MPQ 2011", digits=16, section="spectroscopy",
               tags=["atomic", "clock"],
               legacy_refs={"data4": "F1", "phys24": "H_1S2S"}),
]

write_json("values_nuclear_spectro_v0.json", {"nodes": nuclear_nodes})


# ================================================================
# EXPORT 6: Q335 ANALYTICAL CONSTANTS (Section G, 31 entries)
# ================================================================

q335_nodes = [
    make_value("geom_pi_v0", pi_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G1", "phys24": "pi_f"}),
    make_value("geom_e_euler_v0", e_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G2", "phys24": "e_f"}),
    make_value("geom_ln2_v0", ln2_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G3", "phys24": "ln2_f"}),
    make_value("geom_sqrt2_v0", sqrt2_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G4", "phys24": "sqrt2_f"}),
    make_value("geom_sqrt3_v0", sqrt3_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G5", "phys24": "sqrt3_f"}),
    make_value("geom_sqrt5_v0", sqrt5_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G6", "phys24": "sqrt5_f"}),
    make_value("geom_sqrt7_v0", sqrt7_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G7", "phys24": "sqrt7_f"}),
    make_value("geom_golden_ratio_v0", phi_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G8", "phys24": "phi_f"}),
    make_value("geom_zeta3_v0", zeta3_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G9", "phys24": "zeta3_f"}),
    make_value("geom_zeta5_v0", zeta5_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G10", "phys24": "zeta5_f"}),
    make_value("geom_pi_squared_v0", pi2_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G11", "phys24": "pi2_f"}),
    make_value("geom_zeta2_v0", zeta2_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G12", "phys24": "zeta2_f"},
               notes="zeta(2) = pi^2/6"),
    make_value("geom_r2_v0", R2_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G13", "phys24": "R2_f"},
               notes="R2 = pi/4. The universal geometric remainder."),
    make_value("geom_r4_v0", R4_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G14", "phys24": "R4_f"},
               notes="R4 = pi^2/32"),
    make_value("geom_two_pi_v0", twopi_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G15", "phys24": "twopi_f"}),
    make_value("geom_zeta7_v0", zeta7_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G16", "phys24": "zeta7_f"}),
    make_value("geom_zeta9_v0", zeta9_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G17", "phys24": "zeta9_f"}),
    make_value("geom_li4_half_v0", li4_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G18", "phys24": "li4_f"}),
    make_value("geom_li5_half_v0", li5_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G19", "phys24": "li5_f"}),
    make_value("geom_li6_half_v0", li6_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G20", "phys24": "li6_f"}),
    make_value("geom_li7_half_v0", li7_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G21", "phys24": "li7_f"}),
    make_value("geom_catalan_v0", cat_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G22", "phys24": "cat_f"}),
    make_value("geom_e_to_pi_v0", epi_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G23", "phys24": "epi_f"}),
    make_value("geom_ln3_v0", ln3_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G24", "phys24": "ln3_f"}),
    make_value("geom_ln5_v0", ln5_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G25", "phys24": "ln5_f"}),
    make_value("geom_elliptic_k_quarter_v0", K_quarter_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G26", "phys24": "K_quarter_f"}),
    make_value("geom_elliptic_k_half_v0", K_half_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G27", "phys24": "K_half_f"}),
    make_value("geom_elliptic_k_threequarter_v0", K_3qtr_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G28", "phys24": "K_3qtr_f"}),
    make_value("geom_elliptic_e_quarter_v0", E_quarter_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G29", "phys24": "E_quarter_f"}),
    make_value("geom_elliptic_e_half_v0", E_half_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G30", "phys24": "E_half_f"}),
    make_value("geom_elliptic_e_threequarter_v0", E_3qtr_f, "dimensionless", 0,
               "Q335 basis (100+ digits)", digits=100, section="Q335",
               legacy_refs={"data4": "G31", "phys24": "E_3qtr_f"}),
]

write_json("values_q335_v0.json", {"nodes": q335_nodes})


# ================================================================
# EXPORT 7: MASS RATIOS AND KOIDE (Sections K + Koide)
# ================================================================

ratio_nodes = [
    make_value("ratio_muon_electron_v0", mmu_me, "dimensionless", 2,
               "DATA-4 derived", digits=10, section="ratios",
               legacy_refs={"data4": "K1", "phys24": "mmu_me"}),
    make_value("ratio_tau_electron_v0", mtau_me, "dimensionless", 2,
               "DATA-4 derived", digits=6, section="ratios",
               legacy_refs={"data4": "K2", "phys24": "mtau_me"}),
    make_value("ratio_tau_muon_v0", mtau_mmu, "dimensionless", 2,
               "DATA-4 derived", digits=5, section="ratios",
               legacy_refs={"data4": "K3", "phys24": "mtau_mmu"}),
    make_value("ratio_neutron_proton_v0", mn_mp, "dimensionless", 2,
               "DATA-4 derived", digits=11, section="ratios",
               legacy_refs={"data4": "K4", "phys24": "mn_mp"}),
    make_value("ratio_w_z_mass_v0", MW_MZ, "dimensionless", 2,
               "DATA-4 derived", digits=6, section="ratios",
               legacy_refs={"data4": "K5", "phys24": "MW_MZ"}),
    make_value("ratio_higgs_z_mass_v0", mH_MZ, "dimensionless", 2,
               "DATA-4 derived", digits=5, section="ratios",
               legacy_refs={"data4": "K6", "phys24": "mH_MZ"}),
    make_value("ratio_top_z_mass_v0", mt_MZ, "dimensionless", 2,
               "DATA-4 derived", digits=5, section="ratios",
               legacy_refs={"data4": "K7", "phys24": "mt_MZ"}),
    make_value("koide_charged_leptons_k_v0", K_koide, "dimensionless", 2,
               "DATA-4 derived", digits=10, section="koide",
               tags=["Koide", "ratio"],
               legacy_refs={"data4": "K8", "phys24": "K_koide"}),
    make_value("koide_charged_leptons_a2_v0", a2_lep, "dimensionless", 2,
               "Koide from m_e, m_mu, m_tau", digits=6, section="koide",
               tags=["Koide"],
               legacy_refs={"phys24": "a2_lep"},
               notes="Measurement, NOT hypothesis. a^2=2 is Level 1 hypothesis."),
    make_value("koide_down_quarks_a2_v0", a2_down, "dimensionless", 2,
               "Koide from m_d, m_s, m_b", digits=3, section="koide",
               tags=["Koide", "quark"],
               legacy_refs={"phys24": "a2_down"}),
    make_value("koide_up_quarks_a2_v0", a2_up, "dimensionless", 2,
               "Koide from m_u, m_c, m_t", digits=3, section="koide",
               tags=["Koide", "quark"],
               legacy_refs={"phys24": "a2_up"}),
]

write_json("values_ratios_koide_v0.json", {"nodes": ratio_nodes})


# ================================================================
# EXPORT 8: GUT AND BETA PARAMETERS (Section N + derived)
# ================================================================

gut_nodes = [
    # SM betas
    make_value("beta_sm_u1_total_v0", b1_SM, "dimensionless", 1,
               "SM one-loop", section="GUT", tags=["Level1", "U1", "SM"],
               legacy_refs={"data4": "N1", "phys24": "b1_SM"}),
    make_value("beta_sm_su2_total_v0", b2_SM, "dimensionless", 1,
               "SM one-loop", section="GUT", tags=["Level1", "SU2", "SM"],
               legacy_refs={"data4": "N2", "phys24": "b2_SM"}),
    make_value("beta_sm_su3_total_v0", b3_SM, "dimensionless", 1,
               "SM one-loop", section="GUT", tags=["Level1", "SU3", "SM"],
               legacy_refs={"data4": "N3", "phys24": "b3_SM"}),
    # CD shifts
    make_value("beta_cabibbo_doublet_u1_shift_v0", db1_VL, "dimensionless", 1,
               "VL Dynkin formula", section="GUT", tags=["Level1", "U1", "CD"],
               legacy_refs={"data4": "N4", "phys24": "db1_VL"}),
    make_value("beta_cabibbo_doublet_su2_shift_v0", db2_VL, "dimensionless", 1,
               "VL Dynkin formula", section="GUT", tags=["Level1", "SU2", "CD"],
               legacy_refs={"data4": "N5", "phys24": "db2_VL"}),
    make_value("beta_cabibbo_doublet_su3_shift_v0", db3_VL, "dimensionless", 1,
               "VL Dynkin formula", section="GUT", tags=["Level1", "SU3", "CD"],
               legacy_refs={"data4": "N6", "phys24": "db3_VL"},
               notes="1/3 for VL, not 2/3 for chiral"),
    # Modified betas
    make_value("beta_modified_u1_total_v0", b1_mod, "dimensionless", 1,
               "SM + CD", section="GUT", tags=["Level1", "U1", "modified", "CD"],
               legacy_refs={"phys24": "b1_mod"}),
    make_value("beta_modified_su2_total_v0", b2_mod, "dimensionless", 1,
               "SM + CD", section="GUT", tags=["Level1", "SU2", "modified", "CD"],
               legacy_refs={"phys24": "b2_mod"},
               pitfalls=[{"wrong": "b2_mod = -19/6 + 1 = -13/6 WRONG sign check",
                          "right": "b2_mod = -19/6 + 1 = -13/6 CORRECT",
                          "session": "verified"}]),
    make_value("beta_modified_su3_total_v0", b3_mod, "dimensionless", 1,
               "SM + CD", section="GUT", tags=["Level1", "SU3", "modified", "CD"],
               legacy_refs={"phys24": "b3_mod"}),
    # Gap ratios
    make_value("gap_sm_ratio_v0", gap_SM, "dimensionless", 1,
               "(b1_SM-b2_SM)/(b2_SM-b3_SM)", section="GUT",
               tags=["Level1", "GUT", "exact", "ratio"],
               legacy_refs={"data4": "N10", "phys24": "gap_SM"}),
    make_value("gap_cabibbo_doublet_ratio_v0", gap_VL, "dimensionless", 1,
               "(b1_mod-b2_mod)/(b2_mod-b3_mod)", section="GUT",
               tags=["Level1", "GUT", "exact", "ratio", "CD"],
               legacy_refs={"data4": "N11", "phys24": "gap_VL"}),
    make_value("gap_mssm_ratio_v0", gap_MSSM, "dimensionless", 1,
               "MSSM beta coefficients", section="GUT",
               tags=["Level1", "GUT", "exact", "ratio"],
               legacy_refs={"data4": "N12", "phys24": "gap_MSSM"}),
    make_value("gap_measured_ratio_v0", gap_measured, "dimensionless", 2,
               "Derived from alpha_EM, sin2_tW, alpha_s", section="GUT",
               tags=["Level2", "GUT", "ratio"],
               legacy_refs={"data4": "N13", "phys24": "gap_measured"}),
    # Two-loop b_ij SM matrix (9 entries)
    make_value("beta_two_loop_sm_bij_u1_u1_v0", b_ij_SM[0][0], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"],
               legacy_refs={"data4": "N14"}),
    make_value("beta_two_loop_sm_bij_u1_su2_v0", b_ij_SM[0][1], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_u1_su3_v0", b_ij_SM[0][2], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_su2_u1_v0", b_ij_SM[1][0], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_su2_su2_v0", b_ij_SM[1][1], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_su2_su3_v0", b_ij_SM[1][2], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_su3_u1_v0", b_ij_SM[2][0], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_su3_su2_v0", b_ij_SM[2][1], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    make_value("beta_two_loop_sm_bij_su3_su3_v0", b_ij_SM[2][2], "dimensionless", 1,
               "Machacek-Vaughn", section="GUT", tags=["Level1", "two-loop", "SM"]),
    # Derived couplings
    make_value("coupling_alpha_1_inverse_gut_normalized_mz_v0", inv_a1, "dimensionless", 2,
               "Derived: (3/5)*alpha_inv*cos2_tW", section="GUT",
               tags=["Level2", "U1", "coupling", "GUT"],
               legacy_refs={"phys24": "inv_a1"}),
    make_value("coupling_alpha_2_inverse_mz_v0", inv_a2, "dimensionless", 2,
               "Derived: sin2_tW * alpha_inv", section="GUT",
               tags=["Level2", "SU2", "coupling", "GUT"],
               legacy_refs={"phys24": "inv_a2"},
               pitfalls=[{"wrong": "1/a2 = alpha_inv / sin2_tW = 593",
                          "right": "1/a2 = sin2_tW * alpha_inv = 31.7",
                          "session": "PHYS-30"}]),
    make_value("coupling_alpha_3_inverse_mz_v0", inv_a3, "dimensionless", 2,
               "Derived: 1/alpha_s", section="GUT",
               tags=["Level2", "SU3", "coupling", "GUT"],
               legacy_refs={"phys24": "inv_a3"}),
    make_value("coupling_alpha_em_v0", alpha_em, "dimensionless", 2,
               "Derived: 1/alpha_inv", section="GUT",
               tags=["Level2", "EM", "coupling"],
               legacy_refs={"phys24": "alpha_em"}),
    # CD parameters
    make_value("cd_mass_lower_bound_v0", M_VL_lo, "MeV", None,
               "LHC pair production", section="CD",
               tags=["CD", "staged"],
               legacy_refs={"data4": "L1", "phys24": "M_VL_lo"},
               notes="1.5 TeV lower bound"),
    make_value("cd_mass_upper_bound_v0", M_VL_hi, "MeV", None,
               "CKM perturbativity", section="CD",
               tags=["CD", "staged"],
               legacy_refs={"data4": "L1", "phys24": "M_VL_hi"},
               notes="6.0 TeV upper bound"),
    make_value("cd_mixing_angle_estimate_v0", theta14_est, "dimensionless", None,
               "CKM first-row deficit", section="CD",
               tags=["CD", "staged", "CKM"],
               legacy_refs={"data4": "L2", "phys24": "theta14_est"}),
    # Named constants
    make_value("group_casimir_gap_v0", casimir_gap, "dimensionless", 1,
               "C2(adj SU(3))/C2(adj SU(2))", section="group_theory",
               tags=["Level1", "exact"],
               legacy_refs={"phys24": "casimir_gap"}),
    make_value("cd_hypercharge_v0", CD_Y, "dimensionless", 1,
               "(3,2,1/6) representation", section="GUT",
               tags=["Level1", "CD", "exact"],
               legacy_refs={"phys24": "CD_Y"}),
    make_value("si_reduced_planck_constant_v0", hbar, "J*s", 0,
               "h/(2*pi_f)", section="SI",
               legacy_refs={"phys24": "hbar"}),
]

write_json("values_gut_beta_v0.json", {"nodes": gut_nodes})


# ================================================================
# EXPORT 8b: INTEGER POOL (Table 16)
# ================================================================

integer_nodes = [
    make_value("integer_yang_mills_eleven_v0", 11, "dimensionless", 1,
               "Table 16 / phys24_lib.py", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_yang_mills_eleven_v0"}),
    make_value("integer_b2_modified_numerator_abs_v0", 13, "dimensionless", 1,
               "Table 16 / |numerator of b2_mod = -13/6|", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_b2_modified_numerator_abs_v0"}),
    make_value("integer_b2_sm_numerator_abs_v0", 19, "dimensionless", 1,
               "Table 16 / |numerator of b2_SM = -19/6|", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_b2_sm_numerator_abs_v0"}),
    make_value("integer_b3_modified_times_three_abs_v0", 20, "dimensionless", 1,
               "Table 16 / |3 * b3_mod| = |3 * -20/3|", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_b3_modified_times_three_abs_v0"}),
    make_value("integer_two_times_yang_mills_v0", 22, "dimensionless", 1,
               "Table 16 / 2 * 11", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_two_times_yang_mills_v0"}),
    make_value("integer_four_times_yang_mills_v0", 44, "dimensionless", 1,
               "Table 16 / 4 * 11", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_four_times_yang_mills_v0"}),
    make_value("integer_b2_modified_numerator_square_v0", 169, "dimensionless", 1,
               "Table 16 / 13^2", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_b2_modified_numerator_square_v0"}),
    make_value("integer_cabibbo_doublet_gap_numerator_v0", 38, "dimensionless", 1,
               "Table 16 / numerator of 38/27", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_cabibbo_doublet_gap_numerator_v0"}),
    make_value("integer_cabibbo_doublet_gap_denominator_v0", 27, "dimensionless", 1,
               "Table 16 / denominator of 38/27", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_cabibbo_doublet_gap_denominator_v0"}),
    make_value("integer_sm_gap_numerator_v0", 218, "dimensionless", 1,
               "Table 16 / numerator of 218/115", section="integer_pool",
               tags=["Level1", "exact"],
               legacy_refs={"data5": "integer_sm_gap_numerator_v0"}),
]

write_json("values_integer_pool_v0.json", {"nodes": integer_nodes})


# ================================================================
# EXPORT 8c: GENERATION DEMOCRACY SUMS (Table 8 note)
# ================================================================

gen_demo_nodes = [
    make_value("rep_sm_generation_democracy_db1_sum_v0",
               Fraction(4, 3), "dimensionless", 1,
               "Table 8 note: sum of db1 per generation",
               section="representation", tags=["SM", "generation_democracy"],
               notes="Q_L + u_R + d_R + L_L + e_R db1 sum per generation"),
    make_value("rep_sm_generation_democracy_db2_sum_v0",
               Fraction(4, 3), "dimensionless", 1,
               "Table 8 note: sum of db2 per generation",
               section="representation", tags=["SM", "generation_democracy"]),
    make_value("rep_sm_generation_democracy_db3_sum_v0",
               Fraction(4, 3), "dimensionless", 1,
               "Table 8 note: sum of db3 per generation",
               section="representation", tags=["SM", "generation_democracy"]),
]

write_json("values_generation_democracy_v0.json", {"nodes": gen_demo_nodes})


# ================================================================
# EXPORT 8d: GAP RATIOS (Table 3)
# ================================================================

gap_nodes = [
    make_value("gap_pure_gauge_ratio_v0", Fraction(2, 1), "dimensionless", 1,
               "Table 3 / C2(SU2)/(C2(SU3)-C2(SU2))", section="GUT",
               tags=["Level1", "exact", "ratio"]),
    make_value("gap_sm_numerator_v0", Fraction(109, 15), "dimensionless", 1,
               "b1_SM - b2_SM", section="GUT",
               tags=["Level1", "exact"]),
    make_value("gap_sm_denominator_v0", Fraction(23, 6), "dimensionless", 1,
               "b2_SM - b3_SM", section="GUT",
               tags=["Level1", "exact"]),
    make_value("gap_sm_cabibbo_doublet_ratio_v0", Fraction(38, 27), "dimensionless", 1,
               "(b1_mod - b2_mod) / (b2_mod - b3_mod)", section="GUT",
               tags=["Level1", "exact", "ratio", "CD"]),
    make_value("coupling_measured_gap_ratio_v0", gap_measured, "dimensionless", 2,
               "Derived from alpha_EM, sin2_tW, alpha_s", section="GUT",
               tags=["Level2", "ratio"]),
    make_value("cosmo_dm_to_baryon_ratio_prefactor_v0",
               Fraction(22, 13), "dimensionless", 1,
               "Table 15 / (22/13)*pi formula prefactor", section="cosmological",
               tags=["Level1", "exact", "ratio"],
               legacy_refs={"data5": "cosmo_dm_to_baryon_ratio_prefactor_v0"}),
    make_value("cosmo_omega_dm_r2_prefactor_v0",
               Fraction(44, 169), "dimensionless", 1,
               "Table 15 / (44/169)*R2 formula prefactor", section="cosmological",
               tags=["Level1", "exact", "ratio"],
               legacy_refs={"data5": "cosmo_omega_dm_r2_prefactor_v0"}),
]

write_json("values_gap_ratios_v0.json", {"nodes": gap_nodes})


# ================================================================
# EXPORT 8e: TWO-LOOP VL db_ij MATRIX (Table 7)
# ================================================================

vl_dbij = {
    "u1_u1": Fraction(7, 15),
    "u1_su2": Fraction(1, 15),
    "u1_su3": Fraction(16, 135),
    "su2_u1": Fraction(1, 30),
    "su2_su2": Fraction(15, 4),
    "su2_su3": Fraction(8, 3),
    "su3_u1": Fraction(1, 45),
    "su3_su2": Fraction(1, 1),
    "su3_su3": Fraction(40, 9),
}

vl_dbij_nodes = []
for name, value in vl_dbij.items():
    vl_dbij_nodes.append(make_value(
        "beta_two_loop_cabibbo_doublet_dbij_%s_v0" % name,
        value, "dimensionless", 1,
        "Table 7 / phys24_lib.py", section="GUT",
        tags=["Level1", "two-loop", "CD"],
        notes="su2_su2 = 15/4 is corrected value, not 39/4."))

write_json("values_two_loop_vl_dbij_v0.json", {"nodes": vl_dbij_nodes})


# ================================================================
# EXPORT 8f: REPRESENTATION ALIASES (DATA-5 key compatibility)
# ================================================================
# The derivation functions expect rep_cabibbo_doublet_* keys
# but the exporter wrote rep_cd_* keys. Export both forms.

rep_alias_nodes = [
    make_value("rep_cabibbo_doublet_su3_dim_v0",
               CABIBBO_DOUBLET["su3_dim"], "dimensionless", 1,
               "SM representation", section="representation",
               tags=["CD", "BSM", "SU3"]),
    make_value("rep_cabibbo_doublet_su2_dim_v0",
               CABIBBO_DOUBLET["su2_dim"], "dimensionless", 1,
               "SM representation", section="representation",
               tags=["CD", "BSM", "SU2"]),
    make_value("rep_cabibbo_doublet_y_v0",
               CABIBBO_DOUBLET["Y"], "dimensionless", 1,
               "SM representation", section="representation",
               tags=["CD", "BSM"]),
    make_value("rep_cabibbo_doublet_type_v0",
               CABIBBO_DOUBLET["rep_type"], "classification", 1,
               "SM representation", section="representation",
               tags=["CD", "BSM"]),
    make_value("rep_cabibbo_doublet_db1_v0",
               CABIBBO_DOUBLET["db1"], "dimensionless", 1,
               "Dynkin formula", section="representation",
               tags=["CD", "BSM"]),
    make_value("rep_cabibbo_doublet_db2_v0",
               CABIBBO_DOUBLET["db2"], "dimensionless", 1,
               "Dynkin formula", section="representation",
               tags=["CD", "BSM"]),
    make_value("rep_cabibbo_doublet_db3_v0",
               CABIBBO_DOUBLET["db3"], "dimensionless", 1,
               "Dynkin formula", section="representation",
               tags=["CD", "BSM"]),
]

write_json("values_rep_aliases_v0.json", {"nodes": rep_alias_nodes})


# ================================================================
# EXPORT 8g: BETA SHIFT ALIASES (DATA-5 key compatibility)
# ================================================================
# Derivations expect beta_cabibbo_doublet_vectorlike_u1_shift_v0
# but exporter wrote beta_cabibbo_doublet_u1_shift_v0

beta_alias_nodes = [
    make_value("beta_cabibbo_doublet_vectorlike_u1_shift_v0",
               db1_VL, "dimensionless", 1,
               "VL Dynkin formula", section="GUT",
               tags=["Level1", "U1", "CD"]),
    make_value("beta_cabibbo_doublet_vectorlike_su2_shift_v0",
               db2_VL, "dimensionless", 1,
               "VL Dynkin formula", section="GUT",
               tags=["Level1", "SU2", "CD"]),
    make_value("beta_cabibbo_doublet_vectorlike_su3_shift_v0",
               db3_VL, "dimensionless", 1,
               "VL Dynkin formula", section="GUT",
               tags=["Level1", "SU3", "CD"]),
]

write_json("values_beta_aliases_v0.json", {"nodes": beta_alias_nodes})


# ================================================================
# EXPORT 8h: HIGGS BETA SHIFTS (Table 1)
# ================================================================

higgs_beta_nodes = [
    make_value("beta_sm_u1_higgs_v0",
               Fraction(1, 10), "dimensionless", 1,
               "Table 1 / phys24_lib.py", section="GUT",
               tags=["Level1", "U1", "SM", "Higgs"]),
    make_value("beta_sm_su2_higgs_v0",
               Fraction(1, 6), "dimensionless", 1,
               "Table 1 / phys24_lib.py", section="GUT",
               tags=["Level1", "SU2", "SM", "Higgs"]),
    make_value("beta_sm_su3_higgs_v0",
               Fraction(0, 1), "dimensionless", 1,
               "Table 1 / phys24_lib.py", section="GUT",
               tags=["Level1", "SU3", "SM", "Higgs"]),
]

write_json("values_higgs_beta_v0.json", {"nodes": higgs_beta_nodes})

# ================================================================
# EXPORT 9: REPRESENTATIONS (from structure lib)
# ================================================================

if HAS_STRUCTURES:
    rep_nodes = []

    rep_map = [
        ("Q_L", Q_L, "Left quark doublet", ["SM", "quark", "SU2", "SU3"]),
        ("u_R", u_R, "Right up singlet", ["SM", "quark", "SU3"]),
        ("d_R", d_R, "Right down singlet", ["SM", "quark", "SU3"]),
        ("L_L", L_L, "Left lepton doublet", ["SM", "lepton", "SU2"]),
        ("e_R", e_R, "Right electron singlet", ["SM", "lepton"]),
        ("CD", CABIBBO_DOUBLET, "Cabibbo Doublet (3,2,1/6) VL",
         ["CD", "BSM", "SU2", "SU3"]),
    ]

    for short_name, rep, desc, tags in rep_map:
        prefix = "rep_%s" % short_name.lower()
        rep_nodes.append(make_value(
            "%s_su3_dim_v0" % prefix, rep["su3_dim"], "dimensionless", 1,
            "SM representation", section="representation", tags=tags))
        rep_nodes.append(make_value(
            "%s_su2_dim_v0" % prefix, rep["su2_dim"], "dimensionless", 1,
            "SM representation", section="representation", tags=tags))
        rep_nodes.append(make_value(
            "%s_hypercharge_v0" % prefix, rep["Y"], "dimensionless", 1,
            "SM representation", section="representation", tags=tags))
        rep_nodes.append(make_value(
            "%s_type_v0" % prefix, rep["rep_type"], "classification", 1,
            "SM representation", section="representation", tags=tags))
        rep_nodes.append(make_value(
            "%s_db1_v0" % prefix, rep["db1"], "dimensionless", 1,
            "Dynkin formula", section="representation", tags=tags))
        rep_nodes.append(make_value(
            "%s_db2_v0" % prefix, rep["db2"], "dimensionless", 1,
            "Dynkin formula", section="representation", tags=tags))
        rep_nodes.append(make_value(
            "%s_db3_v0" % prefix, rep["db3"], "dimensionless", 1,
            "Dynkin formula", section="representation", tags=tags))

    # Higgs (manual, not from make_rep)
    rep_nodes.append(make_value(
        "rep_higgs_db1_v0", HIGGS["db1"], "dimensionless", 1,
        "Scalar Higgs beta shift", section="representation",
        tags=["SM", "scalar", "EW"],
        notes="Higgs is scalar, not fermion. Different coefficients."))
    rep_nodes.append(make_value(
        "rep_higgs_db2_v0", HIGGS["db2"], "dimensionless", 1,
        "Scalar Higgs beta shift", section="representation",
        tags=["SM", "scalar", "EW"]))
    rep_nodes.append(make_value(
        "rep_higgs_db3_v0", HIGGS["db3"], "dimensionless", 1,
        "Scalar Higgs beta shift", section="representation",
        tags=["SM", "scalar", "EW"]))

    # Group theory constants
    rep_nodes.append(make_value(
        "group_c2_adj_su3_v0", Fraction(3, 1), "dimensionless", 1,
        "C2(adj SU(3)) = N for SU(N)", section="group_theory"))
    rep_nodes.append(make_value(
        "group_c2_adj_su2_v0", Fraction(2, 1), "dimensionless", 1,
        "C2(adj SU(2)) = N for SU(N)", section="group_theory"))
    rep_nodes.append(make_value(
        "group_c2_fund_su3_v0", Fraction(4, 3), "dimensionless", 1,
        "C2(fund SU(3)) = (N^2-1)/(2N)", section="group_theory"))
    rep_nodes.append(make_value(
        "group_c2_fund_su2_v0", Fraction(3, 4), "dimensionless", 1,
        "C2(fund SU(2)) = (N^2-1)/(2N)", section="group_theory"))
    rep_nodes.append(make_value(
        "group_s2_fundamental_v0", Fraction(1, 2), "dimensionless", 1,
        "S2(fund) = 1/2 for any SU(N)", section="group_theory"))
    rep_nodes.append(make_value(
        "group_k1_gut_normalization_v0", Fraction(3, 5), "dimensionless", 1,
        "SU(5) U(1) normalization", section="group_theory"))
    rep_nodes.append(make_value(
        "group_gauge_coeff_yang_mills_v0", Fraction(-11, 3), "dimensionless", 1,
        "One-loop gauge self-coupling -(11/3)*C2(adj)", section="group_theory"))
    rep_nodes.append(make_value(
        "group_sm_generation_count_v0", Fraction(3, 1), "dimensionless", 1,
        "Number of SM generations", section="group_theory"))
    rep_nodes.append(make_value(
        "group_per_gen_db_v0", Fraction(4, 3), "dimensionless", 1,
        "Per-generation beta shift (same for all three groups)",
        section="group_theory",
        notes="Generation democracy: db1=db2=db3=4/3 per gen"))

    write_json("values_representations_v0.json", {"nodes": rep_nodes})


# ================================================================
# EXPORT 10: ENGINEERING AND DOMAIN DATA
# ================================================================

if HAS_DOMAIN:
    eng_nodes = []

    # Bessel zeros
    eng_nodes.append(make_value(
        "math_bessel_j1_first_zero_v0", None, "dimensionless", 0,
        "DATA-1/MATH-3", section="mathematical",
        ref="mpmath j11 = 3.83170597020751"))
    eng_nodes.append(make_value(
        "math_bessel_j0_first_zero_v0", None, "dimensionless", 0,
        "DATA-1/MATH-3", section="mathematical",
        ref="mpmath j01 = 2.40482555769577"))

    # Engineering constants
    eng_nodes.append(make_value(
        "eng_copper_resistivity_v0", "1.7241e-8", "ohm*m", 2,
        "Handbook value at 20C", section="engineering",
        tags=["engineering"]))
    eng_nodes.append(make_value(
        "eng_vacuum_permittivity_v0", "8.8541878128e-12", "F/m", 2,
        "CODATA 2022", section="engineering",
        tags=["engineering", "EM"]))
    eng_nodes.append(make_value(
        "eng_speed_of_sound_air_v0", "343", "m/s", 2,
        "Standard conditions 20C", section="engineering",
        tags=["engineering", "acoustics"]))
    eng_nodes.append(make_value(
        "eng_stefan_boltzmann_v0", "5.670374419e-8", "W/(m^2*K^4)", 2,
        "CODATA 2022", section="engineering",
        tags=["engineering", "thermal"]))
    eng_nodes.append(make_value(
        "math_euler_mascheroni_v0", "0.5772156649015329", "dimensionless", 0,
        "mpmath", section="mathematical"))

    # AWG wire diameters
    for gauge, data in AWG_DATA.items():
        eng_nodes.append(make_value(
            "eng_awg_%s_diameter_v0" % gauge.replace("0000", "4_0"),
            data["diameter_m"], "m", 2,
            "DATA-1 Section 12", section="engineering",
            tags=["engineering", "wire"]))

    # Optical discs
    for fmt_key, disc in OPTICAL_DISCS.items():
        fmt_lower = fmt_key.lower().replace("-", "_")
        eng_nodes.append(make_value(
            "obs_disc_%s_wavelength_v0" % fmt_lower,
            disc["laser_wavelength_m"], "m", 2,
            "DATA-1 Section 9", section="observational",
            tags=["engineering", "optics"]))
        eng_nodes.append(make_value(
            "obs_disc_%s_na_v0" % fmt_lower,
            disc["NA"], "dimensionless", 2,
            "DATA-1 Section 9", section="observational",
            tags=["engineering", "optics"]))
        eng_nodes.append(make_value(
            "obs_disc_%s_track_pitch_v0" % fmt_lower,
            disc["track_pitch_m"], "m", 2,
            "DATA-1 Section 9", section="observational",
            tags=["engineering", "optics"]))
        eng_nodes.append(make_value(
            "obs_disc_%s_diameter_v0" % fmt_lower,
            disc["disc_diameter_m"], "m", 2,
            "DATA-1 Section 9", section="observational",
            tags=["engineering", "optics"]))

    # Fiber data
    for fiber_key, fiber in FIBER_OPTICS.items():
        fk = fiber_key.lower().replace("-", "_")
        eng_nodes.append(make_value(
            "obs_fiber_%s_mfd_1310_v0" % fk,
            fiber["MFD_1310_m"], "m", 2,
            "DATA-1 Section 16", section="observational",
            tags=["engineering", "fiber"]))
        eng_nodes.append(make_value(
            "obs_fiber_%s_mfd_1550_v0" % fk,
            fiber["MFD_1550_m"], "m", 2,
            "DATA-1 Section 16", section="observational",
            tags=["engineering", "fiber"]))
        eng_nodes.append(make_value(
            "obs_fiber_%s_na_v0" % fk,
            fiber["NA"], "dimensionless", 2,
            "DATA-1 Section 16", section="observational",
            tags=["engineering", "fiber"]))
        eng_nodes.append(make_value(
            "obs_fiber_%s_cutoff_v0" % fk,
            fiber["cutoff_wavelength_m"], "m", 2,
            "DATA-1 Section 16", section="observational",
            tags=["engineering", "fiber"]))
        eng_nodes.append(make_value(
            "obs_fiber_%s_loss_1550_v0" % fk,
            fiber["attenuation_1550_dB_km"], "dB/km", 2,
            "DATA-1 Section 16", section="observational",
            tags=["engineering", "fiber"]))

    # Speakers
    for spk_key, spk in SPEAKERS.items():
        eng_nodes.append(make_value(
            "obs_speaker_%s_deff_v0" % spk_key,
            spk["d_eff_m"], "m", 2,
            "DATA-1 Section 13", section="observational",
            tags=["engineering", "acoustics"]))

    # Sample rates (exact Fractions)
    for sr_key, sr_val in SAMPLE_RATES.items():
        eng_nodes.append(make_value(
            "eng_sample_rate_%s_v0" % sr_key,
            sr_val, "Hz", 0,
            "DATA-1", section="engineering",
            tags=["engineering", "audio"]))

    # Just intonation (exact Fractions)
    for ji_key, ji_val in JUST_INTONATION.items():
        eng_nodes.append(make_value(
            "eng_just_intonation_%s_v0" % ji_key,
            ji_val, "dimensionless", 0,
            "DATA-1 H12-H18", section="engineering",
            tags=["engineering", "audio"]))

    # Semiconductor
    eng_nodes.append(make_value(
        "eng_wafer_300mm_diameter_v0",
        SEMICONDUCTOR["wafer_300mm"]["diameter_m"], "m", 2,
        "SEMI standard", section="engineering",
        tags=["engineering", "semiconductor"]))
    eng_nodes.append(make_value(
        "eng_euv_wavelength_v0",
        SEMICONDUCTOR["EUV_wavelength_m"], "m", 2,
        "EUV lithography", section="engineering",
        tags=["engineering", "semiconductor"]))
    eng_nodes.append(make_value(
        "eng_arf_wavelength_v0",
        SEMICONDUCTOR["ArF_wavelength_m"], "m", 2,
        "ArF immersion lithography", section="engineering",
        tags=["engineering", "semiconductor"]))
    eng_nodes.append(make_value(
        "eng_silicon_lattice_v0",
        SEMICONDUCTOR["Si_lattice_m"], "m", 2,
        "CODATA 2022", section="engineering",
        tags=["engineering", "semiconductor"]))

    # RF standards
    for rf_key, rf_data in RF_STANDARDS.items():
        freq_key = "frequency_Hz" if "frequency_Hz" in rf_data else "subcarrier_Hz"
        if freq_key in rf_data:
            eng_nodes.append(make_value(
                "eng_rf_%s_freq_v0" % rf_key.lower(),
                rf_data[freq_key], "Hz", 2,
                rf_data.get("source", "standard"), section="engineering",
                tags=["engineering", "RF"]))

    # Geodesy
    eng_nodes.append(make_value(
        "eng_wgs84_semimajor_v0",
        GEODESY["WGS84_a_m"], "m", 2,
        "WGS84", section="engineering",
        tags=["engineering", "geodesy"]))
    eng_nodes.append(make_value(
        "eng_wgs84_inverse_flattening_v0",
        GEODESY["WGS84_inv_f"], "dimensionless", 2,
        "WGS84", section="engineering",
        tags=["engineering", "geodesy"]))

    write_json("values_engineering_v0.json", {"nodes": eng_nodes})


# ================================================================
# EXPORT 11: ASTROPHYSICAL CONSTANTS
# ================================================================

astro_nodes = [
    make_value("astro_gravitational_constant_v0", "6.674e-11", "m^3/(kg*s^2)", 2,
               "CODATA 2022", section="astrophysical",
               tags=["gravity"]),
    make_value("astro_mass_sun_v0", "1.989e30", "kg", 2,
               "IAU", section="astrophysical"),
    make_value("astro_mass_earth_v0", "5.972e24", "kg", 2,
               "IAU", section="astrophysical"),
    make_value("astro_mass_moon_v0", "7.342e22", "kg", 2,
               "IAU", section="astrophysical"),
    make_value("astro_radius_earth_v0", "6.371e6", "m", 2,
               "WGS84 mean", section="astrophysical"),
    make_value("astro_radius_sun_v0", "6.957e8", "m", 2,
               "IAU", section="astrophysical"),
    make_value("astro_au_v0", "1.496e11", "m", 2,
               "IAU 2012", section="astrophysical"),
    make_value("astro_parsec_v0", "3.086e16", "m", 2,
               "IAU", section="astrophysical"),
    make_value("astro_gps_orbit_radius_v0", "2.6556e7", "m", 2,
               "GPS ICD", section="astrophysical"),
    make_value("astro_gps_satellite_velocity_v0", "3874", "m/s", 2,
               "GPS ICD", section="astrophysical"),
    make_value("astro_muon_rest_lifetime_v0", "2.1969811e-6", "s", 2,
               "PDG", section="astrophysical",
               tags=["lepton"]),
    make_value("eng_hbar_c_mev_fm_v0", "197.3269804", "MeV*fm", 2,
               "CODATA derived", section="engineering"),
]

write_json("values_astrophysical_v0.json", {"nodes": astro_nodes})


# ================================================================
# EXPORT 12: HUBBLE MEASUREMENTS
# ================================================================

if HAS_HUBBLE:
    hubble_nodes = []

    for key in H0_ORDERED:
        m = H0_MEASUREMENTS[key]
        hubble_nodes.append(make_value(
            "cosmo_h0_%s_v0" % key.lower(),
            m["H0"], "km/s/Mpc", 2,
            m["source"], section="cosmological",
            tags=["Hubble", m["distance_class"]],
            uncertainty=str(m["uncertainty"]),
            notes="Method: %s. Year: %d." % (m["method"], m["year"])))

    # Cosmological target values (measured, for comparison)
    hubble_nodes.append(make_value(
        "cosmo_dm_baryon_ratio_planck2018_v0",
        "5.3204", "dimensionless", 2,
        "Planck 2018", section="cosmological",
        tags=["Planck", "DM"]))
    hubble_nodes.append(make_value(
        "cosmo_omega_b_planck2018_v0",
        "0.0490", "dimensionless", 2,
        "Planck 2018", section="cosmological",
        tags=["Planck"]))
    hubble_nodes.append(make_value(
        "cosmo_omega_dm_planck2018_v0",
        "0.2607", "dimensionless", 2,
        "Planck 2018", section="cosmological",
        tags=["Planck", "DM"]))
    hubble_nodes.append(make_value(
        "cosmo_omega_matter_planck2018_v0",
        "0.3111", "dimensionless", 2,
        "Planck 2018", section="cosmological"))
    hubble_nodes.append(make_value(
        "cosmo_omega_de_planck2018_v0",
        "0.6889", "dimensionless", 2,
        "Planck 2018", section="cosmological"))
    hubble_nodes.append(make_value(
        "cosmo_lambda_log10_planck_v0",
        "-121.54", "log10(Lambda/M_Planck^4)", 2,
        "Planck 2018", section="cosmological"))

    write_json("values_cosmological_v0.json", {"nodes": hubble_nodes})


# ================================================================
# EXPORT 13: OBSERVATIONAL CATALOGS (dwarfs)
# ================================================================

# Dwarf galaxy data from experiment scripts
dwarf_data = {
    "Fornax":    {"M_vis": "2e7",   "sigma": "11.7", "r_h": "710",  "M_dyn": "1.6e8",  "r_core": "400"},
    "Sculptor":  {"M_vis": "2.3e6", "sigma": "9.2",  "r_h": "283",  "M_dyn": "7.0e7",  "r_core": "200"},
    "Draco":     {"M_vis": "2.9e5", "sigma": "9.1",  "r_h": "221",  "M_dyn": "5.4e7",  "r_core": "150"},
    "UrsaMinor": {"M_vis": "2.9e5", "sigma": "9.5",  "r_h": "181",  "M_dyn": "4.8e7",  "r_core": "150"},
    "Carina":    {"M_vis": "3.8e5", "sigma": "6.6",  "r_h": "250",  "M_dyn": "3.2e7",  "r_core": "200"},
    "Sextans":   {"M_vis": "4.4e5", "sigma": "7.9",  "r_h": "695",  "M_dyn": "1.3e8",  "r_core": "400"},
    "LeoI":      {"M_vis": "5.5e6", "sigma": "9.2",  "r_h": "251",  "M_dyn": "6.3e7",  "r_core": "200"},
    "LeoII":     {"M_vis": "7.4e5", "sigma": "6.6",  "r_h": "176",  "M_dyn": "2.3e7",  "r_core": "150"},
}
uf_data = {
    "Segue1":      {"M_vis": "340",  "sigma": "3.9", "r_h": "29",  "M_dyn": "1.3e6"},
    "ReticulumII": {"M_vis": "2600", "sigma": "3.3", "r_h": "32",  "M_dyn": "1.0e6"},
    "TucanaII":    {"M_vis": "3000", "sigma": "8.6", "r_h": "165", "M_dyn": "3.6e7"},
}

obs_nodes = []

for name, d in list(dwarf_data.items()) + list(uf_data.items()):
    prefix = "obs_%s" % name.lower()
    src = "Walker+2009 / McConnachie 2012"
    obs_nodes.append(make_value(
        "%s_mass_visible_v0" % prefix, d["M_vis"], "M_sun", 2,
        src, section="observational", tags=["dwarf", "mass"]))
    obs_nodes.append(make_value(
        "%s_velocity_dispersion_v0" % prefix, d["sigma"], "km/s", 2,
        src, section="observational", tags=["dwarf", "kinematics"]))
    obs_nodes.append(make_value(
        "%s_half_light_radius_v0" % prefix, d["r_h"], "pc", 2,
        src, section="observational", tags=["dwarf", "structure"]))
    obs_nodes.append(make_value(
        "%s_mass_dynamical_v0" % prefix, d["M_dyn"], "M_sun", 2,
        src, section="observational", tags=["dwarf", "mass"]))
    if "r_core" in d:
        obs_nodes.append(make_value(
            "%s_core_radius_v0" % prefix, d["r_core"], "pc", 2,
            src, section="observational", tags=["dwarf", "structure"]))

write_json("values_observational_v0.json", {"nodes": obs_nodes})


# ================================================================
# EXPORT 14: CONNECTIONS
# ================================================================

connection_nodes = []

# R2 equations (from domain lib)
if HAS_DOMAIN:
    for i, eq in enumerate(R2_EQUATIONS):
        connection_nodes.append({
            "key": "connection_r2_equation_%02d_v0" % (i + 1),
            "canonical": "connection_r2_equation_%02d" % (i + 1),
            "version": 0,
            "node_type": "connection",
            "connection_type": "universal_equation",
            "topic": "connection",
            "term": "r2_equation_%02d" % (i + 1),
            "level": 0,
            "source": "DATA-1 Section %s" % eq.get("data1_section", "?"),
            "description": eq["domain"],
            "equation": eq["equation"],
            "coordinator_z": eq["Z"],
            "precision": eq["precision"],
        })

    # R2 cancellations
    for i, canc in enumerate(R2_CANCELLATIONS):
        connection_nodes.append({
            "key": "connection_r2_cancellation_%02d_v0" % (i + 1),
            "canonical": "connection_r2_cancellation_%02d" % (i + 1),
            "version": 0,
            "node_type": "connection",
            "connection_type": "cancellation",
            "topic": "connection",
            "term": "r2_cancellation_%02d" % (i + 1),
            "level": 0,
            "source": "DATA-1 Section 22",
            "description": canc["name"],
            "formula": canc["formula"],
            "status": canc["status"],
            "precision": canc["precision"],
        })

# Boundary stack (from boundary lib)
if HAS_BOUNDARY:
    for i, b in enumerate(BOUNDARY_STACK):
        node = {
            "key": "connection_boundary_%02d_v0" % (i + 1),
            "canonical": "connection_boundary_%02d" % (i + 1),
            "version": 0,
            "node_type": "connection",
            "connection_type": "boundary",
            "topic": "connection",
            "term": "boundary_%02d" % (i + 1),
            "level": None,
            "source": ", ".join(b.get("papers", [])) or "phys24_boundary_map_lib",
            "description": b["name"],
            "what_changes": b["what_changes"],
            "forces_affected": b.get("forces_affected", []),
            "known": b.get("known", False),
            "open_questions": b.get("open_questions", []),
        }
        if b.get("scale_MeV") is not None:
            node["scale_MeV"] = b["scale_MeV"]
        if b.get("scale_MeV_estimate") is not None:
            node["scale_MeV_estimate"] = b["scale_MeV_estimate"]
        if b.get("couplings_at_boundary"):
            # Only include non-None couplings
            known_couplings = {k: v for k, v in b["couplings_at_boundary"].items()
                               if v is not None}
            if known_couplings:
                node["couplings"] = known_couplings
            unknown_couplings = [k for k, v in b["couplings_at_boundary"].items()
                                 if v is None]
            if unknown_couplings:
                node["unknown_couplings"] = unknown_couplings

        connection_nodes.append(node)

    # Forces registry
    for force_key, force in FORCES.items():
        connection_nodes.append({
            "key": "connection_force_%s_v0" % force_key,
            "canonical": "connection_force_%s" % force_key,
            "version": 0,
            "node_type": "connection",
            "connection_type": "adjacency",
            "topic": "connection",
            "term": "force_%s" % force_key,
            "level": None,
            "source": ", ".join(force.get("papers", [])) or "standard model",
            "description": force["name"],
            "gauge_group": force.get("gauge_group"),
            "coupling_name": force.get("coupling_name"),
            "mediator": force.get("mediator"),
            "range": force.get("range"),
            "status": force.get("status"),
        })

# Closed paths (from structures)
if HAS_STRUCTURES:
    for path_key, path in CLOSED_PATHS.items():
        connection_nodes.append({
            "key": "connection_closed_path_%s_v0" % path_key.lower(),
            "canonical": "connection_closed_path_%s" % path_key.lower(),
            "version": 0,
            "node_type": "connection",
            "connection_type": "adjacency",
            "topic": "connection",
            "term": "closed_path_%s" % path_key.lower(),
            "level": None,
            "source": path.get("paper", ""),
            "description": "Closed path: %s" % path_key,
            "killed_by": path["killed_by"],
            "notes": "Status: KILLED. Do not reopen without new evidence.",
        })

    # Anomaly evidence
    for anom_key, anom in ANOMALIES.items():
        connection_nodes.append({
            "key": "connection_anomaly_%s_v0" % anom_key.lower(),
            "canonical": "connection_anomaly_%s" % anom_key.lower(),
            "version": 0,
            "node_type": "connection",
            "connection_type": "anomaly_evidence",
            "topic": "connection",
            "term": "anomaly_%s" % anom_key.lower(),
            "level": 2,
            "source": anom.get("paper", ""),
            "description": anom["name"],
            "sigma": anom["sigma"],
            "quantum_number_used": anom["quantum_number_used"],
            "resolution": anom["resolution"],
        })

write_json("connections_v0.json", {"nodes": connection_nodes})


# ================================================================
# EXPORT 15: PROGRAMS
# ================================================================

program_nodes = [
    {
        "key": "program_beta_unification_v0",
        "canonical": "program_beta_unification",
        "version": 0,
        "node_type": "program",
        "topic": "program",
        "term": "beta_unification",
        "level": None,
        "source": "Session 4",
        "thesis": "Gauge group beta coefficient integers determine cosmological parameters",
        "status": "ACTIVE",
        "tags": ["beta", "unification", "cosmology"],
        "scripts": [
            {"name": "beta_unification_test.py",
             "description": "15 cosmological predictions from particle physics integers",
             "stage": 1},
        ],
        "kill_switches": [
            {"name": "coincidence_probability",
             "condition": "p > 0.1 for observed integer matches",
             "data_source": "combinatoric analysis"},
            {"name": "cmb_s4_omega",
             "condition": "Omega_DM moves away from 44/169 with CMB-S4 data",
             "data_source": "CMB-S4 / LiteBIRD"},
        ],
        "program_connections": {
            "program_toroidal_dm": "shares integers 22, 13, 44",
            "program_hubble_running": "shares integer 20/13",
        },
    },
    {
        "key": "program_toroidal_dm_v0",
        "canonical": "program_toroidal_dm",
        "version": 0,
        "node_type": "program",
        "topic": "program",
        "term": "toroidal_dm",
        "level": None,
        "source": "Session 4",
        "thesis": "DM amplification via toroidal circulation A=(44/13)*pi*(c/v)^2",
        "status": "ACTIVE",
        "tags": ["DM", "toroidal", "amplification"],
        "scripts": [
            {"name": "toroidal_tidal_stripping.py",
             "description": "Quantify tidal stripping in dwarfs",
             "stage": 1},
        ],
        "kill_switches": [
            {"name": "wimp_detection",
             "condition": "Direct detection of DM particles",
             "data_source": "LZ / XENONnT / PandaX"},
            {"name": "dwarf_virial",
             "condition": "Virial theorem cannot be rescued for dwarfs",
             "data_source": "dwarf_soliton_ground_state.py"},
        ],
        "program_connections": {
            "program_beta_unification": "A numerator 44/13 from betas",
        },
    },
    {
        "key": "program_hubble_running_v0",
        "canonical": "program_hubble_running",
        "version": 0,
        "node_type": "program",
        "topic": "program",
        "term": "hubble_running",
        "level": None,
        "source": "Session 4",
        "thesis": "H0 decreases with boundary transit count: H0(N) = H0(0)*r^N",
        "status": "ACTIVE",
        "tags": ["Hubble", "running", "cosmology"],
        "scripts": [
            {"name": "hubble_structure_catalog.py",
             "description": "Extract N estimates from galaxy surveys",
             "stage": 1},
        ],
        "kill_switches": [
            {"name": "gw_sirens",
             "condition": "GW standard sirens show same running as EM",
             "data_source": "LIGO/Virgo O5+"},
            {"name": "systematic_resolution",
             "condition": "Systematic error found resolving H0 tension without running",
             "data_source": "SH0ES / Planck reanalysis"},
        ],
        "program_connections": {
            "program_beta_unification": "(1-r) = alpha^2*pi^2*(20/13)",
        },
    },
]

write_json("programs_v0.json", {"nodes": program_nodes})


# ================================================================
# EXPORT 16: PAPER CROSS-REFERENCES
# ================================================================

if HAS_STRUCTURES:
    paper_nodes = []
    for paper_key, topic in PAPER_TOPICS.items():
        paper_nodes.append({
            "key": "connection_paper_%s_v0" % paper_key.lower().replace("-", "_"),
            "canonical": "connection_paper_%s" % paper_key.lower().replace("-", "_"),
            "version": 0,
            "node_type": "connection",
            "connection_type": "paper_reference",
            "topic": "connection",
            "term": "paper_%s" % paper_key.lower().replace("-", "_"),
            "level": None,
            "source": paper_key,
            "description": topic,
        })

    write_json("connections_papers_v0.json", {"nodes": paper_nodes})


# ================================================================
# SUMMARY
# ================================================================

print()
print("=" * 70)
print("EXPORT COMPLETE")
print("=" * 70)
print()
print("  Output directory: %s" % OUTDIR)
print()

# Count total nodes
total = 0
for fname in sorted(os.listdir(OUTDIR)):
    if fname.endswith(".json"):
        path = os.path.join(OUTDIR, fname)
        with open(path) as f:
            data = json.load(f)
        n = len(data.get("nodes", []))
        total += n
        print("  %-45s %4d nodes" % (fname, n))

print()
print("  TOTAL: %d nodes exported" % total)
print()
print("=" * 70)
print("DATA-6 EXPORT COMPLETE")
print("=" * 70)
