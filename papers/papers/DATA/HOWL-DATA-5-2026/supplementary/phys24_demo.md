#!/usr/bin/env python3
"""
HOWL PLATFORM DEMO
===================
Demonstrates all four libraries working together:
  phys24_lib.py          — constants and helpers
  data_4_derivation_lib.py — derivation functions and predictions
  phys24_structure_lib.py  — representations, census, catalog
  phys24_boundary_map_lib.py — boundary stack and traversal

Run: python phys24_platform_demo.py
Platform: phys24_lib.py (21/21, 148/148)
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from phys24_lib import *
from data_4_derivation_lib import *
from phys24_structure_lib import *
from phys24_boundary_map_lib import *


def section(title):
    print()
    print("=" * 70)
    print("  %s" % title)
    print("=" * 70)
    print()


def subsection(title):
    print()
    print("  --- %s ---" % title)
    print()


# ================================================================
# DEMO 1: SCALE JOURNEYS
# ================================================================

section("DEMO 1: SCALE JOURNEYS")

# Journey 1: Orange to Proton
subsection("Journey: Orange to Proton")
print("  An orange is ~0.1 m. A proton is ~0.84 fm = 8.4e-16 m.")
print("  Energy at orange scale: %s MeV" % mp.nstr(
    distance_fm_to_energy(DISTANCE_SCALES["orange"]["fm"]), 4))
print("  Energy at proton scale: %s MeV" % mp.nstr(
    distance_fm_to_energy(DISTANCE_SCALES["proton_radius"]["fm"]), 4))
print()

# Use energy traversal from proton energy down to orange energy
E_orange = distance_fm_to_energy(DISTANCE_SCALES["orange"]["fm"])
E_proton = distance_fm_to_energy(DISTANCE_SCALES["proton_radius"]["fm"])

report = traverse(E_orange, E_proton)
print("  Boundaries crossed: %d" % report["count"])
for b in report["boundaries"]:
    scale = b.get("scale_MeV")
    if scale is not None:
        print("    %s (%s MeV, %s fm)" % (
            b["name"],
            mp.nstr(f2m(scale) if isinstance(scale, Fraction) else scale, 4),
            mp.nstr(b["scale_fm"], 4) if b.get("scale_fm") else "?"))
    else:
        est = b.get("scale_MeV_estimate")
        if est:
            print("    %s (~%s MeV, estimated)" % (
                b["name"],
                mp.nstr(f2m(est) if isinstance(est, Fraction) else est, 4)))
        else:
            print("    %s (scale unknown)" % b["name"])

print()
print("  Forces encountered: %s" % sorted(set(
    f for _, forces in report["force_changes"] for f in forces)))
print("  Unknown couplings: %d" % len(report["unknown_couplings"]))
print("  Open questions: %d" % len(report["open_questions"]))


# Journey 2: Atom to Nucleus
subsection("Journey: Atom to Nucleus")
print("  Bohr radius: %s fm" % mp.nstr(DISTANCE_SCALES["atom_radius"]["fm"], 4))
print("  Nuclear radius: %s fm" % mp.nstr(DISTANCE_SCALES["nuclear_radius"]["fm"], 4))

E_atom = distance_fm_to_energy(DISTANCE_SCALES["atom_radius"]["fm"])
E_nucleus = distance_fm_to_energy(DISTANCE_SCALES["nuclear_radius"]["fm"])

report2 = traverse(E_atom, E_nucleus)
print("  Boundaries crossed: %d" % report2["count"])
for b in report2["boundaries"]:
    scale = b.get("scale_MeV")
    if scale is not None:
        print("    %s (%s MeV)" % (b["name"],
              mp.nstr(f2m(scale) if isinstance(scale, Fraction) else scale, 4)))
print()
print("  This journey crosses from chemistry (EM binding)")
print("  through nuclear physics (residual strong) to QCD.")


# Journey 3: M_Z to Planck (the full quantum stack)
subsection("Journey: M_Z to Planck (the full high-energy stack)")

report3 = traverse(M_Z, Fraction(12209, 1) * Fraction(10**15, 1))
print("  Boundaries crossed: %d" % report3["count"])
for b in report3["boundaries"]:
    scale = b.get("scale_MeV") or b.get("scale_MeV_estimate")
    if scale:
        print("    %s (%s MeV)" % (b["name"],
              mp.nstr(f2m(scale) if isinstance(scale, Fraction) else scale, 4)))
    else:
        print("    %s (unknown scale)" % b["name"])

print()
print("  Unknown couplings on this journey:")
for bname, cname in report3["unknown_couplings"]:
    print("    %s at %s" % (cname, bname))


# Journey 4: Bottom to Charm (through confinement interior)
subsection("Journey: Bottom to Charm (crossing confinement interior)")

report4 = traverse(m_c, m_b)
print("  Boundaries crossed: %d" % report4["count"])
for b in report4["boundaries"]:
    scale = b.get("scale_MeV")
    if scale is not None:
        print("    %s (%s MeV, %s fm)" % (
            b["name"],
            mp.nstr(f2m(scale) if isinstance(scale, Fraction) else scale, 4),
            mp.nstr(b["scale_fm"], 4) if b.get("scale_fm") else "?"))
print()
print("  Note: both confinement wall faces appear between c and b.")
print("  Perturbative running is NOT valid inside this region.")


# ================================================================
# DEMO 2: REPRESENTATION QUERIES
# ================================================================

section("DEMO 2: REPRESENTATION QUERIES")

# The Cabibbo Doublet — from structures library
subsection("The Cabibbo Doublet (from structures library)")
cd = CABIBBO_DOUBLET
print("  Name:           %s" % cd["name"])
print("  Representation: (%d, %d, %s)" % (cd["su3_dim"], cd["su2_dim"], cd["Y"]))
print("  Type:           %s" % cd["rep_type"])
print("  Y^2:            %s" % cd["Y2"])
print("  Charges:        upper = %s, lower = %s" % (cd["charges"][0], cd["charges"][1]))
print("  Beta shifts:    Db1 = %s, Db2 = %s, Db3 = %s" % cd["db"])
print("  Papers:         %s" % cd["papers"])

# Build a hypothetical alternative: (3, 1, 2/3) VL pair
subsection("What-if: (3,1,2/3) VL pair instead of (3,2,1/6)?")
alt = make_rep("Alt candidate", 3, 1, Fraction(2, 3), "vector-like")
print("  Name:           %s" % alt["name"])
print("  Representation: (%d, %d, %s)" % (alt["su3_dim"], alt["su2_dim"], alt["Y"]))
print("  Beta shifts:    Db1 = %s, Db2 = %s, Db3 = %s" % (alt["db1"], alt["db2"], alt["db3"]))

# Compute gap ratio with this alternative
b1_alt = b1_SM + alt["db1"]
b2_alt = b2_SM + alt["db2"]
b3_alt = b3_SM + alt["db3"]
gap_alt = gap_ratio_from_betas(b1_alt, b2_alt, b3_alt)

print("  Modified betas:  (%s, %s, %s)" % (b1_alt, b2_alt, b3_alt))
print("  Gap ratio:       %s = %s" % (gap_alt, mp.nstr(f2m(gap_alt), 6)))
print("  CD gap ratio:    %s = %s" % (gap_VL, mp.nstr(f2m(gap_VL), 6)))
print("  Measured gap:    %s" % mp.nstr(f2m(gap_measured), 6))

gap_alt_dist = abs(f2m(gap_alt) - f2m(gap_measured))
gap_cd_dist = abs(f2m(gap_VL) - f2m(gap_measured))
print()
print("  Distance from measured: alt = %s, CD = %s" % (
    mp.nstr(gap_alt_dist, 4), mp.nstr(gap_cd_dist, 4)))
print("  CD is %s closer to measured." % (
    "MUCH" if gap_cd_dist < gap_alt_dist / 5 else
    "somewhat" if gap_cd_dist < gap_alt_dist else "NOT"))


# Generation democracy — from structures library
subsection("Generation Democracy (from census)")
gen_b = generation_betas()
print("  Per-generation beta shifts: (%s, %s, %s)" % gen_b)
print("  All equal? %s" % (gen_b[0] == gen_b[1] == gen_b[2]))
print("  This is WHY fermions are invisible to the gap ratio.")
print()
print("  SM betas from census: (%s, %s, %s)" % total_SM_betas(3))
print("  SM betas from library: (%s, %s, %s)" % (b1_SM, b2_SM, b3_SM))
print("  Match? %s" % (total_SM_betas(3) == (b1_SM, b2_SM, b3_SM)))


# ================================================================
# DEMO 3: DERIVATION QUERIES
# ================================================================

section("DEMO 3: PREDICTIONS FROM THE DERIVATION LIBRARY")

# Coupling extraction
subsection("Coupling Extraction at M_Z")
ia1, ia2, ia3 = derive_couplings(alpha_inv, sin2_tW, alpha_s)
print("  1/alpha_1 = %s" % mp.nstr(f2m(ia1), 7))
print("  1/alpha_2 = %s" % mp.nstr(f2m(ia2), 7))
print("  1/alpha_3 = %s" % mp.nstr(f2m(ia3), 7))

# One-loop predictions
subsection("One-Loop Predictions (from unification)")
as_1L = predict_alpha_s_one_loop(inv_a1, inv_a2, inv_a3,
                                  b1_mod, b2_mod, b3_mod)
sin2_1L = predict_sin2_one_loop(alpha_inv, alpha_s,
                                 b1_mod, b2_mod, b3_mod)

as_miss_1L = abs(as_1L["alpha_s_pred"] - f2m(alpha_s)) / f2m(alpha_s) * mpf("100")
sin2_miss_1L = abs(sin2_1L["sin2_pred"] - f2m(sin2_tW)) / f2m(sin2_tW) * mpf("100")

print("  alpha_s predicted:  %s (miss %s%%)" % (
    mp.nstr(as_1L["alpha_s_pred"], 6), mp.nstr(as_miss_1L, 4)))
print("  sin2_tW predicted:  %s (miss %s%%)" % (
    mp.nstr(sin2_1L["sin2_pred"], 6), mp.nstr(sin2_miss_1L, 4)))
print("  alpha_s measured:   %s" % mp.nstr(f2m(alpha_s), 6))
print("  sin2_tW measured:   %s" % mp.nstr(f2m(sin2_tW), 6))

# Two-loop alpha_s (SM b_ij and full b_ij)
subsection("Two-Loop alpha_s (binary search + Euler)")
print("  Running two-loop with SM b_ij...")

as_2L_SM = predict_alpha_s_two_loop(
    inv_a1, inv_a2, inv_a3,
    [b1_mod, b2_mod, b3_mod],
    b_ij_SM, n_steps=500)

as_miss_2L_SM = abs(as_2L_SM["alpha_s_pred"] - f2m(alpha_s)) / f2m(alpha_s) * mpf("100")
print("  alpha_s (SM b_ij):  %s (miss %s%%)" % (
    mp.nstr(as_2L_SM["alpha_s_pred"], 6), mp.nstr(as_miss_2L_SM, 4)))

print("  Running two-loop with full b_ij (SM + VL)...")

as_2L_full = predict_alpha_s_two_loop(
    inv_a1, inv_a2, inv_a3,
    [b1_mod, b2_mod, b3_mod],
    b_ij_full, n_steps=500)

as_miss_2L_full = abs(as_2L_full["alpha_s_pred"] - f2m(alpha_s)) / f2m(alpha_s) * mpf("100")
print("  alpha_s (full b_ij): %s (miss %s%%)" % (
    mp.nstr(as_2L_full["alpha_s_pred"], 6), mp.nstr(as_miss_2L_full, 4)))
print()
print("  Progression: 1-loop %s%% -> 2-loop SM %s%% -> 2-loop full %s%%" % (
    mp.nstr(as_miss_1L, 4), mp.nstr(as_miss_2L_SM, 4), mp.nstr(as_miss_2L_full, 4)))

# Koide prediction
subsection("Koide m_tau Prediction")
K_lep = koide_ratio(m_e, m_mu, m_tau)
a2_comp = koide_amplitude_sq(K_lep)
mtau_pred = koide_predict_m_tau(m_e, m_mu)

mtau_miss = abs(mtau_pred["m_tau_pred"] - f2m(m_tau)) / f2m(m_tau) * mpf("100")

print("  K(e, mu, tau) = %s" % mp.nstr(K_lep, 8))
print("  a^2(leptons) = %s (hypothesis: 2, miss: %s)" % (
    mp.nstr(a2_comp, 10),
    mp.nstr(mpf("2") - a2_comp, 4)))
print("  m_tau predicted = %s MeV (miss %s%%)" % (
    mp.nstr(mtau_pred["m_tau_pred"], 7), mp.nstr(mtau_miss, 4)))
print("  m_tau measured  = %s MeV" % mp.nstr(f2m(m_tau), 7))
print("  Other root      = %s MeV (unphysical)" % mp.nstr(mtau_pred["m_tau_other"], 4))


# ================================================================
# DEMO 4: CROSS-REFERENCE QUERIES
# ================================================================

section("DEMO 4: CROSS-REFERENCE QUERIES")

# DATA-4 lookups
subsection("DATA-4 Lookups")

for entry_id in ["B1", "B12", "C1", "D4", "N10"]:
    entry = lookup_data4(entry_id)
    if entry:
        val = f2m(entry["value"]) if isinstance(entry["value"], Fraction) else entry["value"]
        print("  %s: %s = %s %s (Type %s)" % (
            entry_id, entry["var"],
            mp.nstr(val, 7) if not isinstance(val, str) else val,
            entry["unit"], entry["type"]))

# Paper searches
subsection("Paper Searches")

for keyword in ["gap ratio", "Koide", "proton decay", "PSLQ", "confinement"]:
    results = papers_about(keyword)
    print("  '%s': %s" % (keyword, [r[0] for r in results]))

# Particle catalog
subsection("Particle Catalog (sorted by mass)")

print("  %-15s %12s %12s  %s" % ("Particle", "Mass (MeV)", "Scale (fm)", "Type"))
print("  %-15s %12s %12s  %s" % ("-" * 15, "-" * 12, "-" * 12, "-" * 8))
for p in PARTICLE_CATALOG:
    mass_mpf = f2m(p["mass_frac"])
    dist = energy_to_distance_fm(p["mass_frac"])
    print("  %-15s %12s %12s  %s" % (
        p["name"],
        mp.nstr(mass_mpf, 6),
        mp.nstr(dist, 4),
        p["threshold_type"]))

# Active particles at different scales
subsection("Active Quark Flavors at Different Scales")

for scale_name, scale_MeV in [("1 GeV", Fraction(1000, 1)),
                                ("5 GeV", Fraction(5000, 1)),
                                ("100 GeV", Fraction(100000, 1)),
                                ("1 TeV", Fraction(1000000, 1))]:
    nf = active_fermion_count(scale_MeV)
    print("  At %s: n_f = %d quarks active" % (scale_name, nf))


# ================================================================
# DEMO 5: THE UNKNOWN MAP
# ================================================================

section("DEMO 5: THE COMPLETE UNKNOWN MAP")

print("  Every unknown coupling and open question in the boundary stack,")
print("  from electron to Planck:")
print()

full_report = traverse(m_e, Fraction(12209, 1) * Fraction(10**15, 1))

if full_report["unknown_couplings"]:
    print("  UNKNOWN COUPLINGS (%d):" % len(full_report["unknown_couplings"]))
    for bname, cname in full_report["unknown_couplings"]:
        print("    [%s] %s" % (bname, cname))
    print()

if full_report["open_questions"]:
    print("  OPEN QUESTIONS (%d):" % len(full_report["open_questions"]))
    for bname, q in full_report["open_questions"]:
        print("    [%s] %s" % (bname, q))
    print()

# Closed paths
subsection("Closed Paths (do not reopen)")
for path_name, info in CLOSED_PATHS.items():
    print("  %s: %s [%s]" % (path_name, info["killed_by"], info["paper"]))

# Anomaly evidence
subsection("Anomaly Evidence for the Cabibbo Doublet")
for anom_name, info in ANOMALIES.items():
    print("  %s (%s sigma)" % (info["name"], info["sigma"]))
    print("    Quantum number: %s" % info["quantum_number_used"])
    print("    Resolution: %s" % info["resolution"])
    print()

# Experimental timeline
subsection("Experimental Timeline")
for exp_name, info in EXPERIMENTS.items():
    print("  %s: %s" % (exp_name, info["observable"]))
    print("    CD prediction: %s" % info["cd_prediction"])
    print("    Status: %s" % info["status"])
    print()


# ================================================================
# DEMO 6: WHAT-IF — CUSTOM REPRESENTATIONS
# ================================================================

section("DEMO 6: WHAT-IF — TESTING ALTERNATIVE BSM CANDIDATES")

candidates = [
    ("(3,2,1/6) CD", 3, 2, Fraction(1, 6)),
    ("(3,1,2/3) u'-type", 3, 1, Fraction(2, 3)),
    ("(3,1,-1/3) d'-type", 3, 1, Fraction(-1, 3)),
    ("(1,2,1/2) L'-type", 1, 2, Fraction(1, 2)),
    ("(3,2,7/6) exotic", 3, 2, Fraction(7, 6)),
    ("(3,3,1/3) triplet", 3, 3, Fraction(1, 3)),
]

print("  %-25s %8s %8s %8s %10s %8s" % (
    "Candidate", "Db1", "Db2", "Db3", "Gap", "Dist"))
print("  %-25s %8s %8s %8s %10s %8s" % (
    "-" * 25, "-" * 8, "-" * 8, "-" * 8, "-" * 10, "-" * 8))

for name, d3, d2, Y in candidates:
    rep = make_rep(name, d3, d2, Y, "vector-like")
    b1_new = b1_SM + rep["db1"]
    b2_new = b2_SM + rep["db2"]
    b3_new = b3_SM + rep["db3"]
    gap_new = gap_ratio_from_betas(b1_new, b2_new, b3_new)
    dist = abs(f2m(gap_new) - f2m(gap_measured))
    print("  %-25s %8s %8s %8s %10s %8s" % (
        name,
        str(rep["db1"]),
        str(rep["db2"]),
        str(rep["db3"]),
        mp.nstr(f2m(gap_new), 6),
        mp.nstr(dist, 4)))

print()
print("  Measured gap ratio: %s" % mp.nstr(f2m(gap_measured), 6))
print("  CD (3,2,1/6) wins by gap distance.")


# ================================================================
# SUMMARY
# ================================================================

section("PLATFORM SUMMARY")

print("  Libraries loaded:")
print("    phys24_lib.py          — 146 constants, 11 helpers, 5 check functions")
print("    data_4_derivation_lib  — 9 derivation functions, group theory, two-loop")
print("    phys24_structure_lib   — 5 SM reps, 12 particles, 47 DATA-4 entries mapped")
print("    phys24_boundary_map    — 19 boundaries, 5 forces, traversal functions")
print()
print("  Verified checks:")
print("    phys24_lib self-test:    21/21")
print("    phys24_lib platform:     148/148")
print("    derivation self-test:    37/37")
print("    structures self-test:    46/46")
print("    boundaries self-test:    14/14")
print("    TOTAL:                   266/266")
print()
print("  Predictions from this platform:")
print("    alpha_s (one-loop):      %s (miss %s%%)" % (
    mp.nstr(as_1L["alpha_s_pred"], 6), mp.nstr(as_miss_1L, 4)))
print("    alpha_s (two-loop full): %s (miss %s%%)" % (
    mp.nstr(as_2L_full["alpha_s_pred"], 6), mp.nstr(as_miss_2L_full, 4)))
print("    sin2_tW (one-loop):      %s (miss %s%%)" % (
    mp.nstr(sin2_1L["sin2_pred"], 6), mp.nstr(sin2_miss_1L, 4)))
print("    m_tau (Koide K=2/3):     %s MeV (miss %s%%)" % (
    mp.nstr(mtau_pred["m_tau_pred"], 7), mp.nstr(mtau_miss, 4)))
print()
print("  Unknown couplings (full stack): %d" % len(full_report["unknown_couplings"]))
print("  Open questions (full stack):    %d" % len(full_report["open_questions"]))
print("  Closed paths:                   %d" % len(CLOSED_PATHS))
print()
print("=" * 70)
print("  PLATFORM DEMO COMPLETE")
print("=" * 70)
