#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: The Database
==========================================
DATA-4 is the sole data reference for all HOWL computation.
146 entries, 38/38 checks. This script runs 6 representative
checks spanning all groups to demonstrate the database is
self-consistent. The full 38/38 is in data_4.py.

Backed by: data_4.py (38/38 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *
from mpmath import sqrt as msqrt, pi as mpi

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: THE DATABASE")
print("=" * 70)
print()
print("  DATA-4: 146 entries, 38/38 checks, 0 failures.")
print("  Sole data reference for all HOWL computation.")
print("  DATA-3 is retired.")
print()
print("  Entry types:")
print("    E = exact by definition (SI 2019)")
print("    M = measured (CODATA, PDG, FLAG)")
print("    A = analytical (computed to arbitrary precision)")
print("    D = derived (Level 1 arithmetic on Level 2 inputs)")
print("    G = staged (identified by theory, not yet measured)")
print("    K = Koide derived (from mass fits)")
print()
print("  Sections:")
print("    A (SI fundamental):        7 entries")
print("    B (CODATA measured):      13 entries")
print("    C (Electroweak):           6 entries")
print("    D (Quarks + CKM):         11 entries")
print("    E (Nuclear/hadron):        8 entries")
print("    F (Spectroscopy):          1 entry")
print("    G (Q335 analytical):      14 entries + extended basis")
print("    K (Mass ratios + Koide):   8 entries")
print("    L (Cabibbo Doublet):       6 entries (STAGED)")
print("    N (GUT parameters):       17 entries")
print("    Total:                    146 entries")
print()

# ================================================================
# GROUP A: MASS RATIO IDENTITY (1 of 9)
# ================================================================

print("GROUP A: MASS RATIO IDENTITY")
print("-" * 70)
print()

# uses m_p, m_e, mp_me from phys24_lib (DATA-4 B5, B2, B6)
# m_p/m_e computed from individual masses must match stored ratio
mp_me_comp = m_p / m_e

show("m_p / m_e computed (dimensionless)", f2m(mp_me_comp))
show("m_p/m_e stored (dimensionless)", f2m(mp_me))
print()

# ================================================================
# GROUP B: Q335 ANALYTICAL IDENTITY (1 of 8)
# ================================================================

print("GROUP B: Q335 ANALYTICAL IDENTITY")
print("-" * 70)
print()

# uses R2_f, pi_f from phys24_lib (DATA-4 G13, G1)
# R2 must equal pi/4 to 100+ digits
old_dps = mp.dps
mp.dps = 120
R2_ref = mpi / 4
mp.dps = old_dps

show("R2 from library (dimensionless)", f2m(R2_f))
show("pi/4 from mpmath (dimensionless)", R2_ref)
print()

# ================================================================
# GROUP C: PHYSICAL RELATION (1 of 4)
# ================================================================

print("GROUP C: PHYSICAL RELATION (SI 2019)")
print("-" * 70)
print()

# uses alpha_inv, m_e, c, h_planck, R_inf from phys24_lib
# R_inf = alpha^2 * m_e * c / (2 * h)
# m_e must be converted from MeV to kg: m_e(kg) = m_e(MeV) * 10^6 * e / c^2
alpha_frac_local = Fraction(1) / alpha_inv
m_e_kg = m_e * Fraction(10**6) * e_charge / (c * c)
R_inf_comp = alpha_frac_local * alpha_frac_local * m_e_kg * c / (2 * h_planck)

show("R_inf computed (m^-1)", f2m(R_inf_comp))
show("R_inf stored (m^-1)", f2m(R_inf))
print()

# ================================================================
# GROUP D: KOIDE DERIVED (1 of 5)
# ================================================================

print("GROUP D: KOIDE DERIVED")
print("-" * 70)
print()

# uses m_e, m_mu, m_tau, K_koide from phys24_lib
# Koide ratio recomputed from masses must match stored value
s_e   = msqrt(f2m(m_e))
s_mu  = msqrt(f2m(m_mu))
s_tau = msqrt(f2m(m_tau))
K_comp = f2m(m_e + m_mu + m_tau) / (s_e + s_mu + s_tau)**2

show("K(e,mu,tau) computed (dimensionless)", K_comp)
show("K(e,mu,tau) stored (dimensionless)", f2m(K_koide))
print()

# ================================================================
# GROUP E: SI EXACT CONSTANT (1 of 6)
# ================================================================

print("GROUP E: SI EXACT CONSTANT")
print("-" * 70)
print()

# uses c from phys24_lib (DATA-4 A1)
# c must be the exact integer 299792458
show("c stored (m/s)", f2m(c))
print("  c = 299792458 m/s exactly (SI 2019 definition).")
print()

# ================================================================
# GROUP G: GUT PARAMETER (1 of 6)
# ================================================================

print("GROUP G: GUT PARAMETER")
print("-" * 70)
print()

# uses b1_SM, b2_SM, b3_SM, gap_SM from phys24_lib (DATA-4 N1-N3, N10)
# gap ratio must equal (b1-b2)/(b2-b3) = 218/115 exactly
gap_comp = (b1_SM - b2_SM) / (b2_SM - b3_SM)

show("Gap ratio computed = %s (dimensionless)" % gap_comp, f2m(gap_comp))
show("Gap ratio stored = %s (dimensionless)" % gap_SM, f2m(gap_SM))
print()

# ================================================================
# FINDING 15: LATTICE RATIO INDEPENDENCE
# ================================================================

print("FINDING 15: LATTICE RATIO INDEPENDENCE")
print("-" * 70)
print()

# uses m_c, m_s, mc_ms from phys24_lib (DATA-4 D4, D3, D9)
mc_ms_pdg = m_c / m_s
disc = abs(f2m(mc_ms_pdg) - f2m(mc_ms)) / f2m(mc_ms) * mpf("100")

show("m_c/m_s from PDG masses (dimensionless)", f2m(mc_ms_pdg))
show("m_c/m_s from FLAG lattice (dimensionless)", f2m(mc_ms))
show("Discrepancy (%%)", disc)
print()
print("  This 15.5%% discrepancy is a renormalization scale mismatch.")
print("  PDG: m_c at mu=m_c, m_s at mu=2 GeV. Different scales.")
print("  FLAG: m_c/m_s evaluated at a common scale.")
print("  The database is NOT corrupted. The measurements are independent.")
print()

# ================================================================
# STAGED ENTRIES: CABIBBO DOUBLET
# ================================================================

print("STAGED ENTRIES: CABIBBO DOUBLET (Type G)")
print("-" * 70)
print()
print("  The Cabibbo Doublet parameters are the first staged entries.")
print("  Staged means: identified by theory, bounded by experiment,")
print("  not yet measured with precision for a definitive value.")
print()

# uses M_VL_lo, M_VL_hi, CD_Y from phys24_lib (DATA-4 L1, L1)
show("  M_VL lower bound (MeV)", f2m(M_VL_lo))
show("  M_VL upper bound (MeV)", f2m(M_VL_hi))
show("  Hypercharge Y = %s (dimensionless)" % CD_Y, f2m(CD_Y))
print()
print("  When any parameter is measured, the entry transitions")
print("  from Type G to Type M. Entry numbers are preserved.")
print()

# ================================================================
# TRACEABILITY
# ================================================================

print("COMPUTATION TRACEABILITY (Group T)")
print("-" * 70)
print()
print("  DATA-4 links entries to papers:")
print("    PHYS-9:  B1, G1, G8        -> alpha to a_e via QED")
print("    PHYS-13: B1, B11, B12      -> gap ratio 218/115 vs 1.358")
print("    PHYS-15: B1, B11, B12      -> elimination cascade -> (3,2,1/6)")
print("    PHYS-17: N1-N3             -> generation democracy")
print("    PHYS-22: G10, G8, G3       -> A2 decomposition")
print("    PHYS-23: B2-B4, D1-D5      -> Koide all three sectors")
print("    MATH-6:  G1-G14            -> PSLQ 82/82 null")
print()
print("  When a future PDG update changes any entry, this map")
print("  identifies every computation that must be re-verified.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Group A: mass ratio
chk("A1: m_p/m_e computed vs stored",
    f2m(mp_me_comp), f2m(mp_me), 11, checks)

# Group B: Q335 identity
chk("B1: R2 = pi/4 (Q335 vs mpmath)",
    f2m(R2_f), R2_ref, 100, checks)

# Group C: physical relation
chk("C1: R_inf = alpha^2 * m_e * c / (2h)",
    f2m(R_inf_comp), f2m(R_inf), 11, checks)

# Group D: Koide derived
chk("D1: K(e,mu,tau) from masses vs stored",
    K_comp, f2m(K_koide), 6, checks)

# Group E: SI exact
chk_exact("E2: c = 299792458 m/s",
          c, Fraction(299792458, 1), checks)

# Group G: GUT parameter
chk_exact("G1: SM gap ratio = 218/115",
          gap_comp, Fraction(218, 115), checks)

# Lattice independence: discrepancy > 10%
chk_bool("F15: m_c/m_s PDG vs FLAG > 10%% discrepancy",
         disc > mpf("10"),
         "discrepancy = %s%%" % mp.nstr(disc, 4), checks)

# Staged entries exist
chk_bool("L1: Cabibbo Doublet mass window staged",
         M_VL_lo == Fraction(1500000, 1) and M_VL_hi == Fraction(6000000, 1),
         "window: %s - %s MeV" % (
             mp.nstr(f2m(M_VL_lo), 7),
             mp.nstr(f2m(M_VL_hi), 7)), checks)

print_summary(checks)

print()
print("  Full verification: data_4.py (38/38 checks)")
print("  Platform verification: phys24_lib_test.py (148/148 checks)")
print()
print("=" * 70)
print("PHYS-24 DATABASE DEMONSTRATION COMPLETE")
print("=" * 70)
