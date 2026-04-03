#!/usr/bin/env python3
"""
HOWL PHYS-34: phys34_sin2tw_twoloop.py
=========================================
sin²θ_W = 3/13 — The Exact Two-Loop Test.

PHYS-27 showed the one-loop sin²θ_W prediction (0.22845) is 1.2%
below measured (0.23122), with ordering converging toward 3/13.
PHYS-31 parked the FORMULA 3/13 as a numerological hit (p=0.81).
But the DYNAMICS question remains: does two-loop running produce
a sin²θ_W closer to 3/13?

Method: inputs are alpha_EM and alpha_s (same as PHYS-27).
Run alpha_1 and alpha_3 to the crossing (M_GUT).
Set alpha_2 = alpha_GUT at the crossing.
Run alpha_2 back down to M_Z.
Compute sin²θ_W = alpha_EM / alpha_2 = (1/alpha_2) / (1/alpha_EM).
Wait — sin²θ_W = alpha_EM / alpha_2 is wrong. The correct relation:
  sin²θ_W = (5/3)*alpha_1 / ((5/3)*alpha_1 + alpha_2)
But simpler: at the crossing alpha_1 = alpha_2 = alpha_GUT,
the predicted 1/alpha_2 at M_Z gives sin²θ_W through
  sin²θ_W = 1 - alpha_EM * (1/alpha_2)... no.
Actually: 1/alpha_EM = (5/3)/alpha_1 + 1/alpha_2
and sin²θ_W = alpha_EM/alpha_2 = (1/alpha_2) * alpha_EM.
Wait: sin²θ_W = alpha_EM / alpha_2 means
1/alpha_2 = sin²θ_W / alpha_EM = sin²θ_W * alpha_inv.
So sin²θ_W = (1/alpha_2) / alpha_inv = (1/alpha_2) * alpha_EM.

SIGN CONVENTION: 1/alpha_i(mu) = 1/alpha_i(mu0) - b_i * L

Backed by: phys28, phys27, phys30, phys24_lib
"""

from phys24_lib import *
from mpmath import log as mlog, exp as mexp, pi as mpi, fabs
from mpmath import log10 as mlog10
import math

# ================================================================
print("=" * 70)
print("HOWL PHYS-34: sin2_tW TWO-LOOP TEST")
print("Does two-loop running converge toward 3/13?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: INPUTS AND TARGETS
# ================================================================

print("SECTION 1: INPUTS AND TARGETS")
print("-" * 70)
print()

# Two inputs: alpha_EM and alpha_s
alpha_inv_m = f2m(alpha_inv)
alpha_s_m = f2m(alpha_s)

# Derive 1/alpha_1 and 1/alpha_3
# 1/alpha_EM = (5/3)/alpha_1 + 1/alpha_2
# But we use alpha_EM and alpha_s, not alpha_2.
# 1/alpha_1 is derived from alpha_EM and alpha_2,
# and 1/alpha_3 = 1/alpha_s.
# We need 1/alpha_1 without knowing alpha_2.
#
# From PHYS-27: the method uses b_EM and b_3 to find M_GUT.
# b_EM = (5/3)*b_1 + b_2 for the EM combination.
# 1/alpha_EM(mu) = 1/alpha_EM(MZ) - b_EM * L
# 1/alpha_3(mu) = 1/alpha_3(MZ) - b_3 * L
# At crossing: 1/alpha_EM = 8/(3*alpha_GUT) (from SU(5) relation)
# and 1/alpha_3 = 1/alpha_GUT.
# So at crossing: 1/alpha_EM = (8/3)/alpha_3
#
# Simpler approach: use the PHYS-30 method.
# We have 1/alpha_1 and 1/alpha_3 from:
# 1/alpha_1 = (3/5)*(1/alpha_EM - 1/alpha_2)
# But we don't know alpha_2! That's what we're predicting.
#
# The correct two-input method for sin²θ_W uses (alpha_EM, alpha_s):
# At M_GUT: all three couplings equal.
# 1/alpha_EM(M_GUT) = (5/3)/alpha_GUT + 1/alpha_GUT = (8/3)/alpha_GUT
# 1/alpha_3(M_GUT) = 1/alpha_GUT
# So: 1/alpha_EM(M_GUT) = (8/3)*1/alpha_3(M_GUT)
# Running: 1/alpha_EM(MZ) - b_EM*L = (8/3)*(1/alpha_3(MZ) - b_3*L)
# alpha_inv - b_EM*L = (8/3)*(1/alpha_s - b_3*L)
# alpha_inv - (8/3)/alpha_s = b_EM*L - (8/3)*b_3*L = (b_EM - (8/3)*b_3)*L
# L = (alpha_inv - (8/3)/alpha_s) / (b_EM - (8/3)*b_3)

# CD betas
b1_m = f2m(b1_mod)     # 25/6
b2_m = f2m(b2_mod)     # -13/6
b3_m = f2m(b3_mod)     # -20/3

# b_EM = (5/3)*b1 + b2 (the EM combination runs as this)
b_EM = f2m(Fraction(5, 3)) * b1_m + b2_m
b_EM_frac = Fraction(5, 3) * b1_mod + b2_mod

show("  alpha_inv = 1/alpha_EM (dimensionless)", alpha_inv_m)
show("  alpha_s = 1/alpha_3 -> 1/alpha_3 (dimensionless)", mpf("1") / alpha_s_m)
show("  b_EM = (5/3)*b1' + b2' (dimensionless)", b_EM)
show("  b_EM exact = %s (dimensionless)" % b_EM_frac, f2m(b_EM_frac))
show("  b3' (dimensionless)", b3_m)
print()

# Targets
sin2_meas = f2m(sin2_tW)
sin2_3_13 = f2m(Fraction(3, 13))

show("  sin²θ_W measured (dimensionless)", sin2_meas)
show("  3/13 (dimensionless)", sin2_3_13)
show("  Measured miss from 3/13 (%%)",
     fabs(sin2_meas - sin2_3_13) / sin2_3_13 * mpf("100"))
print()

twopi = mpf("2") * mpi
fourpi = mpf("4") * mpi
inv_as = mpf("1") / alpha_s_m

# ================================================================
# SECTION 2: ONE-LOOP PREDICTION (reproduce PHYS-27)
# ================================================================

print("SECTION 2: ONE-LOOP PREDICTION (no threshold)")
print("-" * 70)
print()

# L = (alpha_inv - (8/3)/alpha_s) / (b_EM - (8/3)*b3)
eight_thirds = mpf("8") / mpf("3")

L_1L = (alpha_inv_m - eight_thirds * inv_as) / (b_EM - eight_thirds * b3_m)
inv_aGUT_1L = inv_as - b3_m * L_1L
# At GUT: 1/alpha_2 = 1/alpha_GUT
# Run 1/alpha_2 back to M_Z:
inv_a2_pred_1L = inv_aGUT_1L + b2_m * L_1L

# sin²θ_W = (1/alpha_2) / (1/alpha_EM) = inv_a2 / alpha_inv
# Wait: sin²θ_W = alpha_EM / alpha_2 = (1/alpha_2) / (1/alpha_EM)... no.
# alpha_EM / alpha_2 = alpha_EM * (1/alpha_2)... that gives a small number times a big number.
# Actually: sin²θ_W = alpha_EM/alpha_2, and 1/alpha_2 = sin²θ_W * (1/alpha_EM).
# So: sin²θ_W = (1/alpha_2) * alpha_EM = inv_a2_pred / alpha_inv... no!
# sin²θ_W = alpha_EM / alpha_2 = (1/alpha_2) / (1/alpha_EM) = inv_a2 / alpha_inv.
# Wait: alpha_EM / alpha_2 = alpha_EM * (1/alpha_2).
# 1/alpha_EM = alpha_inv. alpha_EM = 1/alpha_inv.
# sin²θ_W = (1/alpha_inv) * inv_a2_pred... that's tiny * 30 = tiny.
# No: sin²θ_W = alpha_EM/alpha_2. alpha_EM = 1/137. alpha_2 = 1/31.7.
# sin²θ_W = (1/137) / (1/31.7) = 31.7/137 = 0.231. YES.
# So: sin²θ_W = inv_a2_pred / alpha_inv_m.

sin2_1L = inv_a2_pred_1L / alpha_inv_m
miss_1L = fabs(sin2_1L - sin2_meas) / sin2_meas * mpf("100")
miss_3_13_1L = fabs(sin2_1L - sin2_3_13) / sin2_3_13 * mpf("100")

show("  L_GUT (dimensionless)", L_1L)
show("  1/alpha_GUT (dimensionless)", inv_aGUT_1L)
show("  1/alpha_2 at M_Z predicted (dimensionless)", inv_a2_pred_1L)
show("  sin²θ_W predicted (dimensionless)", sin2_1L)
show("  Miss from measured (%%)", miss_1L)
show("  Miss from 3/13 (%%)", miss_3_13_1L)
print()

# ================================================================
# SECTION 3: TWO-LOOP PREDICTION
# ================================================================

print("SECTION 3: TWO-LOOP PREDICTION (no threshold)")
print("-" * 70)
print()

# Need all three 1/alpha_i at M_Z for the two-loop integrator.
# We have alpha_EM and alpha_s.
# For the integrator we need 1/alpha_1, 1/alpha_2, 1/alpha_3.
# But 1/alpha_2 is what we're predicting!
#
# Resolution: use the MEASURED 1/alpha_2 as the SEED for the
# integrator (it enters the two-loop cross-terms), then replace
# the predicted 1/alpha_2 at M_Z from the back-run.
# The two-loop correction to 1/alpha_2 depends weakly on 1/alpha_2
# itself (through b_2j terms), so using the measured value as seed
# is a good approximation.
#
# Alternative: iterate — seed with measured, get prediction, re-run
# with prediction as seed, converge.

# VL b_ij from PHYS-28
C2_3 = Fraction(4, 3)
C2_2 = Fraction(3, 4)
S2_3 = Fraction(1, 2)
S2_2 = Fraction(1, 2)
d3 = Fraction(3)
d2 = Fraction(2)
Y = Fraction(1, 6)
Y2 = Y * Y
k1 = Fraction(3, 5)
S1_VL = Fraction(2, 5) * d3 * d2 * Y2

db_ij_VL = [
    [Fraction(10,3)*S1_VL*(C2_3+C2_2+k1*Y2), Fraction(4,3)*S1_VL*C2_2, Fraction(4,3)*S1_VL*C2_3],
    [Fraction(4,3)*S2_2*d3*k1*Y2, Fraction(10,3)*S2_2*d3*C2_2, Fraction(4,3)*S2_2*d3*C2_3],
    [Fraction(4,3)*S2_3*d2*k1*Y2, Fraction(4,3)*S2_3*d2*C2_2, Fraction(10,3)*S2_3*d2*C2_3],
]

bij_full = [[float(f2m(b_ij_SM[i][j] + db_ij_VL[i][j])) for j in range(3)] for i in range(3)]
bij_SM_only = [[float(f2m(b_ij_SM[i][j])) for j in range(3)] for i in range(3)]

b_CD_f = [float(b1_m), float(b2_m), float(b3_m)]

PI = math.pi

def run_2loop_float(inv_a_start, b1l, bij, L_total, n_steps):
    """Euler integration with float arithmetic."""
    fourpi_f = 4.0 * PI
    inv_a = [inv_a_start[0], inv_a_start[1], inv_a_start[2]]
    dL = L_total / float(n_steps)
    for _ in range(n_steps):
        alphas = [1.0 / inv_a[k] for k in range(3)]
        d_inv = [0.0, 0.0, 0.0]
        for i in range(3):
            d_inv[i] = -b1l[i] * dL
            for j in range(3):
                d_inv[i] -= bij[i][j] * alphas[j] / fourpi_f * dL
        for i in range(3):
            inv_a[i] += d_inv[i]
    return inv_a

def find_sin2_twoloop(inv_a_MZ, b1l, bij, n_steps):
    """Find sin²θ_W from two-loop unification.
    Uses alpha_1 and alpha_3 crossing. Seeds alpha_2 from measured.
    Returns (sin2_pred, L_GUT, inv_aGUT)."""
    # One-loop L as guess
    # Use the EM + alpha_3 method for the crossing
    b_EM_f = (5.0/3.0) * b1l[0] + b1l[1]
    alpha_inv_f = float(alpha_inv_m)
    inv_a3_f = float(inv_as)
    L_guess = (alpha_inv_f - (8.0/3.0)*inv_a3_f) / (b_EM_f - (8.0/3.0)*b1l[2])

    # Binary search: find L where 1/alpha_1 = 1/alpha_3
    L_lo = L_guess * 0.7
    L_hi = L_guess * 1.3
    for _ in range(60):
        L_mid = (L_lo + L_hi) / 2.0
        inv_a = run_2loop_float(inv_a_MZ, b1l, bij, L_mid, n_steps)
        if inv_a[0] - inv_a[2] > 0:
            # 1/a1 still above 1/a3, need more running
            L_lo = L_mid
        else:
            L_hi = L_mid

    inv_a = run_2loop_float(inv_a_MZ, b1l, bij, L_mid, n_steps)
    inv_aGUT = (inv_a[0] + inv_a[2]) / 2.0

    # Run alpha_2 = alpha_GUT back to M_Z
    inv_a_GUT_all = [inv_aGUT, inv_aGUT, inv_aGUT]
    inv_a_back = run_2loop_float(inv_a_GUT_all, b1l, bij, -L_mid, n_steps)

    # sin²θ_W = inv_a2 / alpha_inv
    sin2_pred = inv_a_back[1] / alpha_inv_f
    return sin2_pred, L_mid, inv_aGUT

# Measured inputs for the integrator
inv_a1_MZ_f = float(f2m(inv_a1))
inv_a2_MZ_f = float(f2m(inv_a2))
inv_a3_MZ_f = float(inv_as)
inv_a_MZ_f = [inv_a1_MZ_f, inv_a2_MZ_f, inv_a3_MZ_f]

# Two-loop with SM b_ij only
sin2_2L_SM, L_2L_SM, iag_2L_SM = find_sin2_twoloop(
    inv_a_MZ_f, b_CD_f, bij_SM_only, 500)

miss_2L_SM = abs(sin2_2L_SM - float(sin2_meas)) / float(sin2_meas) * 100
miss_3_13_2L_SM = abs(sin2_2L_SM - 3.0/13.0) / (3.0/13.0) * 100

show("  TWO-LOOP (SM b_ij, 500 steps):", mpf("0"))
show("    sin²θ_W predicted (dimensionless)", mpf(str(sin2_2L_SM)))
show("    Miss from measured (%%)", mpf(str(miss_2L_SM)))
show("    Miss from 3/13 (%%)", mpf(str(miss_3_13_2L_SM)))
print()

# Two-loop with full b_ij
sin2_2L_full, L_2L_full, iag_2L_full = find_sin2_twoloop(
    inv_a_MZ_f, b_CD_f, bij_full, 500)

miss_2L_full = abs(sin2_2L_full - float(sin2_meas)) / float(sin2_meas) * 100
miss_3_13_2L_full = abs(sin2_2L_full - 3.0/13.0) / (3.0/13.0) * 100

show("  TWO-LOOP (SM+VL b_ij, 500 steps):", mpf("0"))
show("    sin²θ_W predicted (dimensionless)", mpf(str(sin2_2L_full)))
show("    Miss from measured (%%)", mpf(str(miss_2L_full)))
show("    Miss from 3/13 (%%)", mpf(str(miss_3_13_2L_full)))
print()

# ================================================================
# SECTION 4: STEP SENSITIVITY
# ================================================================

print("SECTION 4: EULER STEP SENSITIVITY")
print("-" * 70)
print()

print("  %8s %14s %10s %10s" %
      ("Steps", "sin²θ_W", "miss meas%%", "miss 3/13%%"))
print("  %8s %14s %10s %10s" %
      ("-" * 8, "-" * 14, "-" * 10, "-" * 10))

step_results = []
for ns in [200, 500, 1000, 2000]:
    s2, Lg, iag = find_sin2_twoloop(inv_a_MZ_f, b_CD_f, bij_full, ns)
    mm = abs(s2 - float(sin2_meas)) / float(sin2_meas) * 100
    m3 = abs(s2 - 3.0/13.0) / (3.0/13.0) * 100
    step_results.append((ns, s2, mm, m3))
    print("  %8d %14.8f %10.4f %10.4f" % (ns, s2, mm, m3))

print()

# ================================================================
# SECTION 5: THE COMPLETE COMPARISON
# ================================================================

print("SECTION 5: COMPLETE COMPARISON")
print("-" * 70)
print()

results = [
    ("Tree level (3/8)", 0.375, abs(0.375 - float(sin2_meas))/float(sin2_meas)*100,
     abs(0.375 - 3.0/13.0)/(3.0/13.0)*100),
    ("1-loop no-thresh", float(sin2_1L), float(miss_1L), float(miss_3_13_1L)),
    ("2-loop SM b_ij", sin2_2L_SM, miss_2L_SM, miss_3_13_2L_SM),
    ("2-loop full b_ij", sin2_2L_full, miss_2L_full, miss_3_13_2L_full),
]

print("  %-22s %12s %10s %10s" %
      ("Scenario", "sin²θ_W", "miss meas%%", "miss 3/13%%"))
print("  %-22s %12s %10s %10s" %
      ("-" * 22, "-" * 12, "-" * 10, "-" * 10))

for name, s2, mm, m3 in results:
    print("  %-22s %12.6f %10.4f %10.4f" % (name, s2, mm, m3))

print("  %-22s %12.6f %10s %10s" % ("3/13", 3.0/13.0, "—", "0"))
print("  %-22s %12.6f %10s %10s" % ("Measured", float(sin2_meas), "0", "0.195"))
print()

# Check: does each step move closer to 3/13?
converges_to_3_13 = (miss_3_13_2L_full < float(miss_3_13_1L))
converges_to_meas = (miss_2L_full < float(miss_1L))

print("  Convergence toward 3/13: %s" %
      ("YES" if converges_to_3_13 else "NO"))
print("    1-loop miss from 3/13: %.4f%%" % float(miss_3_13_1L))
print("    2-loop miss from 3/13: %.4f%%" % miss_3_13_2L_full)
print()
print("  Convergence toward measured: %s" %
      ("YES" if converges_to_meas else "NO"))
print("    1-loop miss from meas: %.4f%%" % float(miss_1L))
print("    2-loop miss from meas: %.4f%%" % miss_2L_full)
print()

# Does 2-loop overshoot 3/13?
overshoot = sin2_2L_full > 3.0/13.0
print("  Does 2-loop overshoot 3/13? %s" % ("YES" if overshoot else "NO"))
print("    2-loop: %.6f, 3/13: %.6f" % (sin2_2L_full, 3.0/13.0))
print()

# The ordering
values_ordered = [
    ("1-loop", float(sin2_1L)),
    ("2-loop full", sin2_2L_full),
    ("3/13", 3.0/13.0),
    ("measured", float(sin2_meas)),
]
values_ordered.sort(key=lambda x: x[1])
order_str = " < ".join(["%.5f(%s)" % (v, n) for n, v in values_ordered])
print("  Ordering: %s" % order_str)
print()

# ================================================================
# SECTION 6: THE 3/13 TEST RESULT
# ================================================================

print("SECTION 6: THE 3/13 TEST")
print("-" * 70)
print()

# The question: is the two-loop value closer to 3/13 than one-loop?
gap_closed_toward_3_13 = 1 - miss_3_13_2L_full / float(miss_3_13_1L)

print("  One-loop distance from 3/13: %.4f%%" % float(miss_3_13_1L))
print("  Two-loop distance from 3/13: %.4f%%" % miss_3_13_2L_full)
print("  Gap closed: %.1f%%" % (gap_closed_toward_3_13 * 100))
print()

if converges_to_3_13:
    print("  RESULT: Two-loop moves TOWARD 3/13.")
    print("  The perturbative series converges in the direction of")
    print("  3/13 = N_gen / |b₂' numerator|.")
    print("  3/13 is a plausible limit of the perturbative expansion.")
else:
    print("  RESULT: Two-loop does NOT move toward 3/13.")
    print("  The perturbative series overshoots or diverges.")
    print("  3/13 is not the limit of the expansion.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk("S2: 1-loop reproduces PHYS-27 (0.22845)",
    sin2_1L, mpf("0.22845"), 3, checks)

chk_bool("S2: 1-loop undershoots measured",
         sin2_1L < sin2_meas,
         "%.5f < %.5f" % (float(sin2_1L), float(sin2_meas)), checks)

chk_bool("S3: 2-loop closer to measured than 1-loop",
         miss_2L_full < float(miss_1L),
         "2L=%.3f%% < 1L=%.3f%%" % (miss_2L_full, float(miss_1L)), checks)

chk_bool("S3: 2-loop closer to 3/13 than 1-loop",
         miss_3_13_2L_full < float(miss_3_13_1L),
         "2L=%.3f%% < 1L=%.3f%%" % (miss_3_13_2L_full, float(miss_3_13_1L)),
         checks)

chk_bool("S3: Full b_ij improves over SM b_ij",
         miss_2L_full < miss_2L_SM,
         "full=%.3f%% < SM=%.3f%%" % (miss_2L_full, miss_2L_SM), checks)

chk_bool("S4: Step sensitivity < 0.1%% (500 vs 2000)",
         abs(step_results[1][1] - step_results[3][1]) / step_results[3][1] * 100 < 0.1,
         "|diff| = %.6f" % abs(step_results[1][1] - step_results[3][1]), checks)

chk_bool("S5: Ordering: 1L < 2L < 3/13 < measured",
         float(sin2_1L) < sin2_2L_full < 3.0/13.0 < float(sin2_meas),
         order_str, checks)

chk_bool("S5: 2-loop does not overshoot 3/13",
         sin2_2L_full < 3.0/13.0,
         "%.6f < %.6f" % (sin2_2L_full, 3.0/13.0), checks)

chk_bool("S6: Gap toward 3/13 closed > 30%%",
         gap_closed_toward_3_13 > 0.30,
         "closed = %.1f%%" % (gap_closed_toward_3_13 * 100), checks)

chk_bool("S6: 2-loop miss from measured < 1%%",
         miss_2L_full < 1.0,
         "miss = %.3f%%" % miss_2L_full, checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-34 sin²θ_W TWO-LOOP TEST COMPLETE")
print("=" * 70)

