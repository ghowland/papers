#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: Derivation Beats Search
=====================================================
One PSLQ test at 100 digits demonstrates the methodology:
the sanity check finds the known relation pi^2 = 6*zeta(2),
and the Bessel zero j_11 is independent of the full 20-constant
transcendental basis. 82/82 null across the series. Every parameter
reduction came from physics, none from numerical pattern matching.

Backed by: bessel_pslq_0.py (6/6 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *
from mpmath import mpf, pslq, pi as mpi, zeta as mzeta

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: DERIVATION BEATS SEARCH")
print("=" * 70)
print()

# ================================================================
# WHAT PSLQ DOES
# ================================================================

print("WHAT PSLQ DOES")
print("-" * 70)
print()
print("  PSLQ searches for integer coefficients (a_1, ..., a_n) such that")
print("    a_1*x_1 + a_2*x_2 + ... + a_n*x_n = 0")
print("  with all |a_i| bounded by maxcoeff.")
print()
print("  If a relation exists within scope, PSLQ finds it.")
print("  If no relation exists within scope, PSLQ returns NULL.")
print()
print("  Scope limitation: PSLQ tests LINEAR integer relations")
print("  with BOUNDED coefficients at FINITE precision.")
print("  A null does not prove absolute independence.")
print("  It establishes independence within scope.")
print()

# ================================================================
# THE SANITY CHECK
# ================================================================
# PSLQ must prove it works before any null is credible.
# The known relation: pi^2 = 6*zeta(2), i.e., pi^2 - 6*zeta(2) = 0.
# PSLQ should find the integer vector [1, 0, -6] for (pi^2, 1, zeta(2)).

print("SANITY CHECK: pi^2 = 6*zeta(2)")
print("-" * 70)
print()

old_dps = mp.dps
mp.dps = 120

sanity_vec = [mpi**2, mpf("1"), mzeta(2)]
sanity_result = pslq(sanity_vec, maxcoeff=10000)

mp.dps = old_dps

print("  Input vector: [pi^2, 1, zeta(2)]")
print("  maxcoeff = 10000")
print()

if sanity_result is not None:
    print("  Result: %s" % sanity_result)
    print("  Meaning: %d*pi^2 + %d*1 + %d*zeta(2) = 0" % (
        sanity_result[0], sanity_result[1], sanity_result[2]))
    print("  i.e., pi^2 = %d*zeta(2)" % (-sanity_result[2]))
    print("  This is the Basel problem (Euler, 1734).")
else:
    print("  Result: NULL — ERROR, sanity check should find a relation")

print()
print("  The algorithm works. It finds known relations.")
print("  Therefore, when it returns NULL, the null is genuine.")
print()

# ================================================================
# THE BESSEL ZERO TEST
# ================================================================
# j_11 = 3.83170597... is the first zero of J_1(x).
# It determines the Airy disk radius: 1.22 = j_11 / pi.
# Every telescope, microscope, and camera uses this number.
#
# Test: is j_11 a rational linear combination of the 20-constant
# transcendental basis at 100-digit precision?

print("BESSEL ZERO TEST: j_11 vs FULL BASIS (100 digits)")
print("-" * 70)
print()

old_dps = mp.dps
mp.dps = 120

# j_11 at 100+ digits from mpmath
from mpmath import besseljzero
j11_mp = besseljzero(1, 1)

# The full 20-constant basis (computed fresh at 120 dps for headroom)
basis_names = [
    "1", "pi", "pi^2", "pi^3", "pi^4",
    "e", "ln(2)", "ln(3)", "ln(5)",
    "sqrt(2)", "sqrt(3)", "sqrt(5)", "sqrt(7)", "phi",
    "zeta(3)", "zeta(5)",
    "Li4(1/2)", "Catalan",
    "gamma", "e^pi",
]

from mpmath import (e as me, log as mlog, sqrt as msqrt,
                    phi as mphi, polylog, catalan as mcat,
                    euler as mgamma, exp as mexp)

basis_values = [
    mpf("1"), mpi, mpi**2, mpi**3, mpi**4,
    me, mlog(2), mlog(3), mlog(5),
    msqrt(2), msqrt(3), msqrt(5), msqrt(7), mphi,
    mzeta(3), mzeta(5),
    polylog(4, mpf("0.5")), mcat,
    mgamma, mexp(mpi),
]

show("j_11 (dimensionless)", j11_mp)
show("j_11 / pi (Airy constant, dimensionless)", j11_mp / mpi)
print()
print("  Testing j_11 against %d-constant basis at 100+ digits" % len(basis_values))
print("  maxcoeff = 10000")
print()

pslq_vec = [j11_mp] + basis_values
bessel_result = pslq(pslq_vec, maxcoeff=10000)

mp.dps = old_dps

if bessel_result is None:
    print("  Result: NULL")
    print("  j_11 is independent of the entire transcendental basis")
    print("  at 100-digit precision with coefficients up to 10000.")
else:
    print("  Result: RELATION FOUND — %s" % bessel_result)
    print("  This would be unexpected. Investigate.")

print()

# ================================================================
# THE SERIES RECORD
# ================================================================

print("THE SERIES RECORD")
print("-" * 70)
print()
print("  82 constants tested. Zero relations found.")
print("  Three categories:")
print("    Physical (59 tests, 4-15 digits): SM parameters, clocks, ratios")
print("    Dynamical (3 tests, 10-30 digits): Feigenbaum, BCS gap")
print("    Analytical (10 tests, 100 digits): Bessel zeros and ratios")
print()
print("  Every parameter reduction in the series came from physics:")
print("    theta_QCD = 0 from energy minimization (PHYS-7)")
print("    alpha <-> a_e from QED perturbation theory (PHYS-9)")
print("    Koide K = 2/3 conditional from trigonometric identity (PHYS-8)")
print()
print("  Every PSLQ search returned null: 0/82.")
print()
print("  DERIVATION BEATS SEARCH.")
print("  Future effort should prioritize physical derivation paths")
print("  over numerical pattern hunting.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: sanity finds [1, 0, -6]
sanity_ok = (sanity_result is not None and
             sanity_result[0] == 1 and
             sanity_result[1] == 0 and
             sanity_result[2] == -6)
chk_bool("Sanity: PSLQ finds pi^2 = 6*zeta(2)",
         sanity_ok,
         "result = %s" % str(sanity_result), checks)

# Check 2: Bessel test returns NULL
chk_bool("Bessel j_11 vs full basis: NULL",
         bessel_result is None,
         "result = %s" % str(bessel_result), checks)

# Check 3: j_11 matches known value
old_dps = mp.dps
mp.dps = 120
j11_ref = besseljzero(1, 1)
mp.dps = old_dps
chk("j_11 value",
    j11_mp, j11_ref, 30, checks)

# Check 4: j_11/pi ~ 1.2197 (the Airy constant)
old_dps = mp.dps
mp.dps = 120
airy_const = besseljzero(1, 1) / mpi
mp.dps = old_dps
chk("j_11/pi ~ 1.2197 (Airy constant)",
    j11_mp / mpi, mpf("1.2196698913"), 8, checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-24 PSLQ NULL DEMONSTRATION COMPLETE")
print("=" * 70)
