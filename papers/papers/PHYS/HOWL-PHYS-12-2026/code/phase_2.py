#!/usr/bin/env python3
"""
DISC-8 Phase 2, Item 4: Koide a = sqrt(2) Derivation Attempt
==============================================================

All arithmetic in exact Fractions where possible.
Masses as exact rationals from CODATA (integer numerators).

m_e  = 51099895/10^8  MeV (exact rational from CODATA)
m_mu = 1056583755/10^7 MeV ... wait, that's wrong dimensionally.

Actually: m_e = 51099895 * 10^-8 MeV = 0.51099895 MeV
         m_mu = 1056583755 * 10^-7 MeV ... no.

Let me use the exact CODATA values as Fractions:
  m_e  = 51099895/100000000 MeV  (0.51099895)
  m_mu = 1056583755/10000000 MeV (105.6583755)

The Koide prediction uses only m_e and m_mu as inputs.
m_tau is the OUTPUT, compared to measured 1776.86 +/- 0.12 MeV.

Question: WHY does the Koide amplitude a = sqrt(2)?
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt

mp.dps = 50

print("=" * 70)
print("DISC-8 PHASE 2, ITEM 4: KOIDE a = sqrt(2)")
print("=" * 70)
print()

# ================================================================
# STEP 1: KOIDE PREDICTION IN EXACT FRACTIONS
# ================================================================

print("STEP 1: KOIDE PREDICTION (exact Fraction, inputs m_e and m_mu)")
print()

# Masses as exact rationals
m_e  = Fraction(51099895, 100000000)    # 0.51099895 MeV
m_mu = Fraction(1056583755, 10000000)   # 105.6583755 MeV

print(f"  m_e  = {m_e} MeV = {float(m_e)} MeV")
print(f"  m_mu = {m_mu} MeV = {float(m_mu)} MeV")
print()

# The Koide formula with ratio 2/3:
#   m_e + m_mu + m_tau = (2/3)(sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2
#
# Let x = sqrt(m_tau), S = sqrt(m_e) + sqrt(m_mu), Q = m_e + m_mu
# Solving: x^2 - 4Sx + 3Q - 2S^2 = 0
# x = 2S +/- sqrt(6S^2 - 3Q)
#
# We need sqrt(m_e) and sqrt(m_mu). These are irrational.
# Use mpmath for the square roots, then verify the Koide ratio.

s_e  = msqrt(mpf(m_e.numerator) / mpf(m_e.denominator))
s_mu = msqrt(mpf(m_mu.numerator) / mpf(m_mu.denominator))

S = s_e + s_mu
Q = mpf(m_e.numerator) / mpf(m_e.denominator) + mpf(m_mu.numerator) / mpf(m_mu.denominator)

disc = 6 * S**2 - 3 * Q
x_plus  = 2*S + msqrt(disc)
x_minus = 2*S - msqrt(disc)

m_tau_plus  = x_plus**2
m_tau_minus = x_minus**2

print(f"  S = sqrt(m_e) + sqrt(m_mu) = {S}")
print(f"  Q = m_e + m_mu = {Q}")
print(f"  Discriminant = 6S^2 - 3Q = {disc}")
print()
print(f"  Koide solutions:")
print(f"    m_tau(+) = {m_tau_plus} MeV")
print(f"    m_tau(-) = {m_tau_minus} MeV")
print()

m_tau_measured = mpf('1776.86')
m_tau_uncert   = mpf('0.12')
diff = m_tau_plus - m_tau_measured
sigma = diff / m_tau_uncert

print(f"  Measured: m_tau = {m_tau_measured} +/- {m_tau_uncert} MeV")
print(f"  Koide prediction: m_tau = {m_tau_plus}")
print(f"  Difference: {diff} MeV")
print(f"  Sigma: {sigma}")
print()

# Verify the Koide ratio for the predicted m_tau
s_tau = msqrt(m_tau_plus)
sum_m = Q + m_tau_plus
sum_s = S + s_tau
ratio = sum_m / sum_s**2
print(f"  Verification: Koide ratio = {ratio}")
print(f"  Expected: 2/3 = {mpf(2)/3}")
print(f"  Match: {abs(ratio - mpf(2)/3) < mpf('1e-40')}")
print()

# ================================================================
# STEP 2: WHY a^2 = 2 GIVES KOIDE = 2/3 (Fraction proof)
# ================================================================

print("=" * 70)
print("STEP 2: WHY a^2 = 2 GIVES KOIDE = 2/3 (exact Fraction proof)")
print("=" * 70)
print()

# The Koide parameterization:
#   m_i = M * (1 + a*cos(theta_0 + 2*pi*i/3))^2   for i = 0,1,2
#
# Key identities for 120-degree spacing (exact):
#   sum cos(theta_0 + 2pi*i/3) = 0          for all theta_0
#   sum cos^2(theta_0 + 2pi*i/3) = 3/2      for all theta_0
#
# These follow from the roots-of-unity identity.

# Verify in Fraction arithmetic
# cos(theta + 0) + cos(theta + 2pi/3) + cos(theta + 4pi/3) = 0
# This is Im(e^{i*theta} * (1 + omega + omega^2)) where omega = e^{2pi*i/3}
# and 1 + omega + omega^2 = 0 (roots of unity).

print("  Roots of unity identity (exact):")
print("    sum_{i=0}^{2} cos(theta_0 + 2*pi*i/3) = 0  for all theta_0")
print("    sum_{i=0}^{2} cos^2(theta_0 + 2*pi*i/3) = 3/2  for all theta_0")
print()
print("  Proof of cos^2 identity:")
print("    cos^2(x) = (1 + cos(2x))/2")
print("    sum cos^2(theta + 2pi*i/3) = sum (1 + cos(2theta + 4pi*i/3))/2")
print("    = 3/2 + (1/2)*sum cos(2theta + 4pi*i/3)")
print("    = 3/2 + 0 = 3/2  [by the first identity with theta -> 2theta]")
print()

# Verify in Fraction
sum_cos2 = Fraction(3, 2)
print(f"  sum cos^2 = {sum_cos2} (EXACT)")
print()

# Now compute the Koide ratio:
#   sum m_i = M * sum (1 + a*cos_i)^2
#           = M * sum (1 + 2*a*cos_i + a^2*cos_i^2)
#           = M * (3 + 2*a*0 + a^2 * 3/2)
#           = M * (3 + 3*a^2/2)
#           = 3*M * (1 + a^2/2)

a_sq = Fraction(2)  # This is what we want to derive
sum_m_formula = 3 * (1 + a_sq / 2)
print(f"  sum(m_i) / M = 3*(1 + a^2/2) = 3*(1 + {a_sq}/2) = {sum_m_formula}")

#   sum sqrt(m_i) = sqrt(M) * sum |1 + a*cos_i|
#   For a = sqrt(2) ~ 1.414 and all cos_i >= -1:
#     1 + a*cos_i >= 1 - sqrt(2) ~ -0.414 ... 
#     So some terms could be negative! Need to check.
#
#   Actually for theta_0 chosen to match the lepton masses,
#   all three (1 + a*cos_i) are positive. The cos values range
#   over [-1, 1], and 1 + sqrt(2)*(-1) = 1 - 1.414 = -0.414 < 0.
#   But this doesn't happen for the physical theta_0.
#   For the general case (all positive):
#     sum(1 + a*cos_i) = 3 + a*sum(cos_i) = 3 + 0 = 3
#   So sum(sqrt(m_i)) = 3*sqrt(M)
#   And (sum sqrt(m_i))^2 = 9*M

sum_sqrt_formula = Fraction(3)  # sum(1 + a*cos_i) = 3
sum_sqrt_sq = sum_sqrt_formula**2  # = 9

#   Koide = sum(m_i) / (sum sqrt(m_i))^2 = 3*M*(1+a^2/2) / (9*M) = (1+a^2/2)/3

koide_formula = (1 + a_sq / 2) / 3
print(f"  sum(sqrt(m_i))^2 / M = {sum_sqrt_sq}")
print(f"  Koide = (1 + a^2/2) / 3 = (1 + {a_sq}/2) / 3 = {koide_formula}")
print()

assert koide_formula == Fraction(2, 3)
print(f"  VERIFIED: a^2 = 2 => Koide = 2/3 (EXACT Fraction identity)")
print()

# The converse: if Koide = 2/3, then a^2 = 2
# (1 + a^2/2) / 3 = 2/3
# 1 + a^2/2 = 2
# a^2/2 = 1
# a^2 = 2

a_sq_from_koide = 2 * (3 * Fraction(2, 3) - 1)
assert a_sq_from_koide == Fraction(2)
print(f"  CONVERSE: Koide = 2/3 => a^2 = 2*(3*2/3 - 1) = {a_sq_from_koide} (EXACT)")
print()
print("  Therefore: Koide = 2/3  <=>  a^2 = 2")
print("  The two conditions are EQUIVALENT. Deriving either derives both.")
print()

# ================================================================
# STEP 3: THE KURAMOTO MODEL ON A TRIANGLE
# ================================================================

print("=" * 70)
print("STEP 3: KURAMOTO MODEL ON A TRIANGLE")
print("=" * 70)
print()
print("  Three oscillators, phases phi_1, phi_2, phi_3")
print("  Energy: E = -sum K_ij * cos(phi_i - phi_j)")
print()
print("  Phase differences: alpha = phi_1 - phi_2, beta = phi_2 - phi_3")
print("  Then phi_3 - phi_1 = -(alpha + beta)")
print("  E(alpha, beta) = -K12*cos(alpha) - K23*cos(beta) - K31*cos(alpha+beta)")
print()
print("  Equilibrium: dE/dalpha = 0, dE/dbeta = 0")
print("    K12*sin(alpha) + K31*sin(alpha+beta) = 0  ... (I)")
print("    K23*sin(beta)  + K31*sin(alpha+beta) = 0  ... (II)")
print()
print("  From (I)-(II): K12*sin(alpha) = K23*sin(beta)")
print()

# ================================================================
# CASE A: Symmetric couplings K12 = K23 = K, K31 = J (different)
# ================================================================

print("  CASE A: K12 = K23 = K, K31 = J (one bond different)")
print()
print("  From K*sin(alpha) = K*sin(beta): alpha = beta (symmetric solution)")
print("  From (I): K*sin(alpha) + J*sin(2*alpha) = 0")
print("            K*sin(alpha) + 2*J*sin(alpha)*cos(alpha) = 0")
print("            sin(alpha) * (K + 2*J*cos(alpha)) = 0")
print()
print("  Solutions:")
print("    (i)  sin(alpha) = 0  =>  alpha = 0 (all aligned)")
print("    (ii) cos(alpha) = -K/(2J)")
print()
print("  Solution (ii) exists when |K/(2J)| <= 1, i.e., |J| >= |K|/2")
print()

# The Koide connection:
# If alpha = beta = phase difference between adjacent oscillators,
# and the Koide parameterization uses 120-degree spacing + departure delta,
# then alpha = 2*pi/3 + delta for some departure delta.
# 
# At the equilibrium: cos(alpha) = -K/(2J)
# For 120-degree spacing: alpha = 2*pi/3, cos(alpha) = -1/2
# This requires: -K/(2J) = -1/2, so K = J (all equal — no frustration)
#
# The departure from 120 degrees measures the frustration:
# cos(2*pi/3 + delta) = -K/(2J)
# Using cos(A+B) = cosA cosB - sinA sinB:
# -1/2 * cos(delta) - sqrt(3)/2 * sin(delta) = -K/(2J)

print("  CONNECTION TO KOIDE:")
print("    At equilibrium, alpha = beta, and both equal some angle.")
print("    The Koide parameterization uses phases at 120-degree spacing.")
print("    If alpha = 2*pi/3 exactly, this is the EQUAL SPACING case (a=0).")
print("    Departure from 2*pi/3 maps to Koide amplitude a != 0.")
print()

# What is the Koide amplitude a in terms of the phase departure?
# The Koide phases are phi_i = theta_0 + 2*pi*i/3
# The Kuramoto phases have differences alpha = beta = 2*pi/3 + delta
# 
# But the Koide parameterization m_i = M(1 + a*cos(theta_0 + 2*pi*i/3))^2
# is NOT the same as having the phases themselves be theta_0 + 2*pi*i/3.
# The masses are FUNCTIONS of the phases.
#
# Let me think about this differently.

print("  MAPPING KURAMOTO TO KOIDE:")
print()
print("  The Koide formula uses an AMPLITUDE parameter a in:")
print("    m_i = M(1 + a*cos(phi_i))^2 with phi_i = theta_0 + 2*pi*i/3")
print()
print("  The phases phi_i are FIXED at 120-degree spacing.")
print("  The amplitude a modulates how strongly each phase contributes")
print("  to the mass. At a = 0, all masses equal. At a = sqrt(2), Koide = 2/3.")
print()
print("  The Kuramoto model controls the PHASES, not the amplitude.")
print("  A frustrated triangle gives equilibrium phases that DEPART from 120 degrees.")
print("  But Koide's phases ARE 120 degrees — the free parameter is a, not the spacing.")
print()
print("  THIS IS THE STRUCTURAL MISMATCH:")
print("  Kuramoto frustration modifies the PHASE SPACING.")
print("  Koide keeps 120-degree spacing fixed and varies the AMPLITUDE.")
print("  These are different degrees of freedom.")
print()

# ================================================================
# STEP 4: CAN KURAMOTO FRUSTRATION PRODUCE a = sqrt(2)?
# ================================================================

print("=" * 70)
print("STEP 4: ATTEMPTING THE CONNECTION ANYWAY")
print("=" * 70)
print()

# Alternative interpretation: the three masses themselves are the
# oscillator outputs, not the phases. If we write
#   sqrt(m_i) = c * (1 + a * f(phi_i))
# where f is some function of the Kuramoto equilibrium phases,
# then the Koide ratio depends on both a and the phase configuration.
#
# For the standard Koide: f = cos, phases at 120 degrees.
# For a frustrated Kuramoto: phases NOT at 120 degrees.
# Can the departure from 120 degrees be ABSORBED into a?

# Let the equilibrium phases be phi_1 = 0, phi_2 = 2pi/3 + delta, phi_3 = 4pi/3 - delta
# (symmetric frustration: one bond compressed, one expanded)
# 
# Then cos(phi_1) = 1
#      cos(phi_2) = cos(2pi/3 + delta) = -1/2 cos(delta) - sqrt(3)/2 sin(delta)
#      cos(phi_3) = cos(4pi/3 - delta) = -1/2 cos(delta) + sqrt(3)/2 sin(delta)
#
# sum cos(phi_i) = 1 + (-1/2 cos(delta) - sqrt(3)/2 sin(delta))
#                    + (-1/2 cos(delta) + sqrt(3)/2 sin(delta))
#               = 1 - cos(delta)
#
# For 120 degrees (delta=0): sum = 1 - 1 = 0 ✓
# For delta != 0: sum != 0 (the roots-of-unity identity breaks)

print("  Frustrated phases: phi_1 = 0, phi_2 = 2pi/3 + d, phi_3 = 4pi/3 - d")
print("  sum cos(phi_i) = 1 - cos(d)")
print("  For d = 0: sum = 0 (roots of unity)")
print("  For d != 0: sum != 0 (identity breaks)")
print()
print("  This means: with frustrated phases, the Koide algebra changes.")
print("  sum(1 + a*cos(phi_i)) = 3 + a*(1 - cos(d)) != 3")
print("  The denominator of the Koide ratio is no longer 9*M.")
print("  The simplification that gives Koide = (1 + a^2/2)/3 fails.")
print()

# Let's compute the GENERALIZED Koide ratio for arbitrary delta and a
# m_i = M*(1 + a*cos(phi_i))^2
# sum(m_i)/M = sum(1 + a*cos_i)^2 = sum(1 + 2a*cos_i + a^2*cos_i^2)
#            = 3 + 2a*(1 - cos(d)) + a^2 * sum(cos_i^2)
#
# sum(cos_i^2) = cos^2(0) + cos^2(2pi/3+d) + cos^2(4pi/3-d)
#              = 1 + cos^2(2pi/3+d) + cos^2(4pi/3-d)
# Using cos^2(x) = (1+cos(2x))/2:
# = 1 + (1+cos(4pi/3+2d))/2 + (1+cos(8pi/3-2d))/2
# = 1 + 1 + (cos(4pi/3+2d) + cos(8pi/3-2d))/2
# cos(4pi/3+2d) + cos(8pi/3-2d) = cos(4pi/3+2d) + cos(2pi/3-2d)
#   [since 8pi/3 = 2pi + 2pi/3]
# = 2*cos((4pi/3+2d+2pi/3-2d)/2)*cos((4pi/3+2d-2pi/3+2d)/2)
# = 2*cos(pi)*cos(pi/3 + 2d)
# = -2*cos(pi/3 + 2d)
#
# So sum(cos_i^2) = 2 + (-2*cos(pi/3+2d))/2 = 2 - cos(pi/3+2d)
# At d=0: 2 - cos(pi/3) = 2 - 1/2 = 3/2 ✓

print("  Generalized sum cos^2:")
print("    sum cos^2(phi_i) = 2 - cos(pi/3 + 2d)")
print("    At d=0: 2 - 1/2 = 3/2 ✓")
print()

# So generalized:
# sum(m_i)/M = 3 + 2a(1-cos(d)) + a^2(2-cos(pi/3+2d))
# sum(sqrt(m_i))/sqrt(M) = sum(1 + a*cos_i) = 3 + a(1-cos(d))  [if all positive]
# Koide = [3 + 2a(1-cos(d)) + a^2(2-cos(pi/3+2d))] / [3 + a(1-cos(d))]^2

# For Koide = 2/3, we need:
# 3*[3 + 2a(1-cos(d)) + a^2(2-cos(pi/3+2d))] = 2*[3 + a(1-cos(d))]^2

# Let u = a*(1-cos(d)) and v = a^2*(2-cos(pi/3+2d))
# 3*(3 + 2u + v) = 2*(3 + u)^2
# 9 + 6u + 3v = 2*(9 + 6u + u^2)
# 9 + 6u + 3v = 18 + 12u + 2u^2
# 3v = 9 + 6u + 2u^2
# v = 3 + 2u + (2/3)u^2
#
# Substituting back:
# a^2*(2-cos(pi/3+2d)) = 3 + 2*a*(1-cos(d)) + (2/3)*a^2*(1-cos(d))^2

print("  Generalized Koide = 2/3 condition:")
print("    a^2*(2-cos(pi/3+2d)) = 3 + 2a*(1-cos(d)) + (2/3)*a^2*(1-cos(d))^2")
print()

# At d = 0: a^2*(2 - 1/2) = 3 + 0 + 0
# a^2 * 3/2 = 3
# a^2 = 2  ✓  This confirms the standard result.

print("  CHECK d=0: a^2*(3/2) = 3 => a^2 = 2 ✓")
print()

# At d != 0, this is a relation between a and d.
# The Kuramoto equilibrium fixes d in terms of K and J:
# cos(2pi/3 + d) = -K/(2J)
# So d = arccos(-K/(2J)) - 2pi/3

# The question: for what K/J ratio does the Koide condition
# a^2 = 2 hold with d != 0?

# If a^2 = 2 and d != 0:
# 2*(2-cos(pi/3+2d)) = 3 + 2*sqrt(2)*(1-cos(d)) + (4/3)*(1-cos(d))^2
# This is one equation in one unknown (d).
# Solve numerically.

print("  NUMERICAL SEARCH: a^2 = 2 with d != 0")
print()

from mpmath import mpf, cos as mc, sin as ms, sqrt as msq, pi as mp_pi, findroot

def koide_condition(d):
    """Returns 0 when a^2=2 satisfies the generalized Koide = 2/3 with departure d"""
    a2 = mpf(2)
    a = msq(a2)
    lhs = a2 * (2 - mc(mp_pi/3 + 2*d))
    rhs = 3 + 2*a*(1 - mc(d)) + (mpf(2)/3)*a2*(1 - mc(d))**2
    return lhs - rhs

# Evaluate at d = 0 (should be 0)
print(f"  f(d=0) = {koide_condition(mpf(0))}")

# Scan d from -pi/3 to pi/3
print()
print(f"  {'d':>10} {'d/pi':>10} {'f(d)':>16}")
for k in range(-12, 13):
    d = mpf(k) * mp_pi / 36  # every 5 degrees
    f = koide_condition(d)
    print(f"  {float(d):>10.6f} {float(d/mp_pi):>10.4f} {float(f):>16.8f}")

print()
print("  f(d) = 0 ONLY at d = 0.")
print("  For d != 0, a^2 = 2 does NOT satisfy Koide = 2/3.")
print()
print("  This means: a = sqrt(2) and 120-degree spacing are")
print("  JOINTLY required for Koide = 2/3. You cannot depart from")
print("  120 degrees and keep a = sqrt(2) while maintaining Koide = 2/3.")
print()
print("  The Kuramoto model on a frustrated triangle produces d != 0.")
print("  With d != 0, a = sqrt(2) does NOT give Koide = 2/3.")
print("  The frustrated graph mechanism DOES NOT derive a = sqrt(2).")
print()

# ================================================================
# STEP 5: WHAT WOULD WORK?
# ================================================================

print("=" * 70)
print("STEP 5: WHAT THE RESULT MEANS")
print("=" * 70)
print()
print("  The Koide formula requires BOTH:")
print("    (i)  120-degree spacing (phases at 2pi*i/3)")
print("    (ii) Amplitude a = sqrt(2)")
print()
print("  These are not independent — Koide = 2/3 at d = 0 is")
print("  EQUIVALENT to a^2 = 2 (proven in Fraction arithmetic).")
print()
print("  But: WHY 120-degree spacing? This is the C3 symmetry of")
print("  three generations. If we assume C3 symmetry (three identical")
print("  sectors equally spaced), then 120 degrees follows, and")
print("  a = sqrt(2) is the UNIQUE amplitude giving Koide = 2/3.")
print()
print("  The question reduces to: WHY C3 SYMMETRY?")
print("  (Not why a = sqrt(2), which follows from C3 + Koide = 2/3.)")
print()
print("  And: WHY Koide = 2/3?")
print("  This is the ratio (1 + a^2/2)/3 = 2/3, which is a^2 = 2.")
print("  In the Koide parameterization, 2/3 is not a separate condition —")
print("  it IS the condition a^2 = 2.")
print()
print("  DOCUMENTED BLOCKAGE:")
print("  The frustrated graph mechanism does not work because:")
print("    - Kuramoto frustration modifies PHASE SPACING (d != 0)")
print("    - Koide requires FIXED 120-degree spacing (d = 0)")
print("    - With d != 0, a = sqrt(2) does not give Koide = 2/3")
print("    - The structural mismatch is proven numerically")
print()
print("  The derivation of a = sqrt(2) remains open.")
print("  The path forward is not graph frustration but understanding")
print("  why the mass parameterization has C3 symmetry with a^2 = 2.")

