#!/usr/bin/env python3
"""
HOWL PHYS-25 DEMONSTRATION: alpha_s from Unification
=====================================================
phys25_alpha_s.py

Using alpha_EM and sin^2(theta_W) as inputs, the unification
hypothesis with CD modified betas predicts alpha_s(M_Z).
CD prediction: 0.1077, miss −8.7% from measured 0.1180.
SM prediction: 0.0664, miss −44%. CD is 5x closer.

The alpha_s prediction is more sensitive to the one-loop
deficit than sin^2 because alpha_3 has the strongest running
and the largest two-loop correction (b_33 = -26).

Backed by: sin2_theta_w_1.py (9/9 checks)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *
from mpmath import exp as mexp, pi as mpi, log10 as mlog10

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-25: alpha_s FROM UNIFICATION")
print("=" * 70)
print()

# ================================================================
# INPUTS (Level 2)
# ================================================================

print("INPUTS (Level 2, from DATA-4)")
print("-" * 70)
print()

# uses alpha_inv from phys24_lib (DATA-4 B1, Type M, 12 digits)
# uses sin2_tW from phys24_lib (DATA-4 B11, Type M, 5 digits)
# uses inv_a1, inv_a2 (derived from B1, B11)
# TARGET: alpha_s = 0.1180 (DATA-4 B12, Type M, 4 digits)

show("alpha_EM^-1 (dimensionless)", f2m(alpha_inv))
show("sin^2(theta_W) (dimensionless)", f2m(sin2_tW))
print()
show("1/alpha_1(M_Z) GUT-normalized (dimensionless)", f2m(inv_a1))
show("1/alpha_2(M_Z) (dimensionless)", f2m(inv_a2))
print()
show("alpha_s(M_Z) measured (dimensionless)", f2m(alpha_s))
show("1/alpha_3(M_Z) measured (dimensionless)", f2m(inv_a3))
print()

# ================================================================
# BETAS (Level 1)
# ================================================================

print("BETAS (Level 1, CD modified)")
print("-" * 70)
print()

# uses b1_mod, b2_mod, b3_mod from phys24_lib (N7-N9)
show("b_1' = %s (dimensionless)" % b1_mod, f2m(b1_mod))
show("b_2' = %s (dimensionless)" % b2_mod, f2m(b2_mod))
show("b_3' = %s (dimensionless)" % b3_mod, f2m(b3_mod))
print()

# ================================================================
# THE PREDICTION
# ================================================================
# One-loop running: inv_a_i(M_Z) = 1/alpha_GUT + b_i' * L
# where L = ln(M_GUT/M_Z) / (2*pi) > 0.
#
# Unification of alpha_1 and alpha_2 at M_GUT:
#   L = (inv_a1 - inv_a2) / (b_1' - b_2')
#   1/alpha_GUT = inv_a1 - b_1'*L
#
# Predict alpha_3:
#   inv_a3_pred = 1/alpha_GUT + b_3'*L
#   alpha_s_pred = 1 / inv_a3_pred

print("THE PREDICTION: alpha_EM + sin^2 -> alpha_s")
print("-" * 70)
print()

b12_diff = b1_mod - b2_mod    # = 19/3
delta_12 = inv_a1 - inv_a2    # positive

L = delta_12 / b12_diff

show("b_1' - b_2' = %s (dimensionless)" % b12_diff, f2m(b12_diff))
show("inv_a1 - inv_a2 (dimensionless)", f2m(delta_12))
show("L = ln(M_GUT/M_Z)/(2*pi) (dimensionless)", f2m(L))
print()

# 1/alpha_GUT from the 1-2 crossing
alpha_GUT_inv = inv_a1 - b1_mod * L

show("1/alpha_GUT (dimensionless)", f2m(alpha_GUT_inv))
print()

# Cross-check: same from alpha_2
alpha_GUT_inv_check = inv_a2 - b2_mod * L

show("1/alpha_GUT from alpha_2 (dimensionless)", f2m(alpha_GUT_inv_check))
print()

# Predict inv_a3
inv_a3_pred = alpha_GUT_inv + b3_mod * L
alpha_s_pred = Fraction(1, 1) / inv_a3_pred

show("1/alpha_3 predicted (dimensionless)", f2m(inv_a3_pred))
show("alpha_s predicted (dimensionless)", f2m(alpha_s_pred))
print()
show("1/alpha_3 measured (dimensionless)", f2m(inv_a3))
show("alpha_s measured (dimensionless)", f2m(alpha_s))
print()

miss_abs = f2m(alpha_s_pred) - f2m(alpha_s)
miss_pct = miss_abs / f2m(alpha_s) * mpf("100")

show("Absolute miss (dimensionless)", miss_abs)
show("Relative miss (%%)", miss_pct)
print()

# ================================================================
# COUPLING CONVERGENCE AT M_GUT
# ================================================================

print("COUPLING CONVERGENCE AT M_GUT")
print("-" * 70)
print()

inv_a1_GUT = inv_a1 - b1_mod * L
inv_a2_GUT = inv_a2 - b2_mod * L
inv_a3_GUT = inv_a3 - b3_mod * L   # using MEASURED inv_a3

show("1/alpha_1(M_GUT) (dimensionless)", f2m(inv_a1_GUT))
show("1/alpha_2(M_GUT) (dimensionless)", f2m(inv_a2_GUT))
show("1/alpha_3(M_GUT) (dimensionless)", f2m(inv_a3_GUT))
print()

Delta = f2m(inv_a3_GUT) - f2m(inv_a1_GUT)

show("Delta = 1/a3(M_GUT) - 1/a_GUT (dimensionless)", Delta)
print()
print("  alpha_1 and alpha_2 unify by construction (L from 1-2 crossing).")
print("  alpha_3 misses by Delta = %s." % mp.nstr(Delta, 4))
print("  This is the one-loop unification deficit. The dominant")
print("  two-loop correction (b_33 = -26) slows SU(3) running,")
print("  pulling 1/alpha_3(M_GUT) upward toward the crossing point.")
print()

# ============================================================
