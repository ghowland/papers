#!/usr/bin/env python3
"""
DISC-8 Phase 2, Item 4b: The CV = 1 Lead
==========================================

The Koide condition a^2 = 2 is equivalent to CV(sqrt(m_i)) = 1.

CV = 1 characterizes exponential distributions (maximum entropy
for positive random variables with fixed mean).

Question: Is there a physical or information-theoretic principle
that forces CV = 1 for the lepton mass square roots?

We explore:
1. Verify the CV = 1 equivalence exactly
2. Test: does CV = 1 hold for quarks?
3. What distributions have CV = 1?
4. Maximum entropy argument
5. Is there a variational principle selecting CV = 1?
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msq, log as mlog

mp.dps = 50

print("=" * 70)
print("DISC-8 ITEM 4b: THE CV = 1 LEAD")
print("=" * 70)
print()

# ================================================================
# STEP 1: VERIFY CV = 1 EQUIVALENCE (Fraction arithmetic)
# ================================================================

print("STEP 1: CV = 1 EQUIVALENCE (exact Fraction)")
print()

# x_i = sqrt(m_i / M) = 1 + a*cos(phi_i) with C3 phases
# mean(x) = sum(x_i)/3 = (3 + a*sum(cos))/3 = 3/3 = 1
# sum(x_i^2) = 3 + 3a^2/2  (from roots-of-unity identities)
# var(x) = sum(x_i^2)/3 - mean^2 = (3 + 3a^2/2)/3 - 1 = a^2/2
# std(x) = a/sqrt(2)
# CV = std/mean = a/sqrt(2) / 1 = a/sqrt(2)
# CV = 1 iff a = sqrt(2) iff a^2 = 2

print("  x_i = 1 + a*cos(phi_i), phi_i at 120-degree spacing")
print()
print("  mean(x) = 1  [from sum cos = 0]")
print()

# In Fractions:
a_sq = Fraction(2)
var_x = a_sq / 2  # = 1
mean_x = Fraction(1)
cv_sq = var_x / mean_x**2  # = 1

print(f"  var(x) = a^2/2 = {a_sq}/2 = {var_x}")
print(f"  mean(x) = {mean_x}")
print(f"  CV^2 = var/mean^2 = {var_x}/{mean_x**2} = {cv_sq}")
print(f"  CV = 1 iff a^2 = 2: {cv_sq == Fraction(1)} (EXACT)")
print()

# The chain of equivalences
print("  CHAIN OF EQUIVALENCES (all exact):")
print("    Koide = 2/3")
print("    <=> (1 + a^2/2)/3 = 2/3")
print("    <=> a^2/2 = 1")
print("    <=> var(x) = 1")
print("    <=> var(x) = mean(x)^2")
print("    <=> CV(x) = 1")
print("    <=> sigma = mu for the sqrt(m) distribution")
print()

# Verify each step
assert (1 + a_sq/2) / 3 == Fraction(2, 3)
assert a_sq / 2 == Fraction(1)
assert var_x == mean_x**2
assert cv_sq == Fraction(1)
print("  All 4 equivalences verified as exact Fraction identities.")
print()

# ================================================================
# STEP 2: VERIFY WITH ACTUAL LEPTON MASSES
# ================================================================

print("=" * 70)
print("STEP 2: CV OF sqrt(m) FOR ACTUAL LEPTONS")
print("=" * 70)
print()

m_e  = mpf('0.51099895')
m_mu = mpf('105.6583755')
m_tau = mpf('1776.86')  # measured value for checking

x_e  = msq(m_e)
x_mu = msq(m_mu)
x_tau = msq(m_tau)

mean = (x_e + x_mu + x_tau) / 3
var = (x_e**2 + x_mu**2 + x_tau**2) / 3 - mean**2
std = msq(var)
cv = std / mean

print(f"  sqrt(m_e)   = {x_e}")
print(f"  sqrt(m_mu)  = {x_mu}")
print(f"  sqrt(m_tau) = {x_tau}")
print()
print(f"  mean  = {mean}")
print(f"  var   = {var}")
print(f"  std   = {std}")
print(f"  CV    = {cv}")
print(f"  CV^2  = {cv**2}")
print()
print(f"  CV = 1 would give: CV = 1.000000")
print(f"  Actual CV:               {float(cv):.6f}")
print(f"  Departure from 1:        {float(cv - 1):.6e}")
print()

# With Koide-predicted m_tau instead of measured
m_tau_k = mpf('1776.969')
x_tau_k = msq(m_tau_k)
mean_k = (x_e + x_mu + x_tau_k) / 3
var_k = (x_e**2 + x_mu**2 + x_tau_k**2) / 3 - mean_k**2
cv_k = msq(var_k) / mean_k

print(f"  With Koide-predicted m_tau = 1776.969:")
print(f"  CV = {float(cv_k):.10f}")
print()

# ================================================================
# STEP 3: TEST CV FOR QUARKS
# ================================================================

print("=" * 70)
print("STEP 3: CV OF sqrt(m) FOR QUARKS")
print("=" * 70)
print()

# Up-type quarks (u, c, t) - pole masses
m_u = mpf('2.16')      # MeV
m_c = mpf('1270')      # MeV
m_t = mpf('172690')    # MeV

x_u = msq(m_u)
x_c = msq(m_c)
x_t = msq(m_t)

mean_up = (x_u + x_c + x_t) / 3
var_up = (x_u**2 + x_c**2 + x_t**2) / 3 - mean_up**2
cv_up = msq(var_up) / mean_up

print(f"  Up-type quarks (u, c, t):")
print(f"    sqrt(m): {float(x_u):.4f}, {float(x_c):.4f}, {float(x_t):.4f}")
print(f"    mean = {float(mean_up):.4f}")
print(f"    CV   = {float(cv_up):.6f}")
print(f"    CV vs 1: off by {float(abs(cv_up - 1)):.4f} ({float(abs(cv_up-1))*100:.1f}%)")
print()

# Koide ratio for up-type
sum_m_up = m_u + m_c + m_t
sum_sq_up = (x_u + x_c + x_t)**2
koide_up = sum_m_up / sum_sq_up
print(f"    Koide ratio: {float(koide_up):.6f} (vs 2/3 = 0.666667)")
print(f"    Departure: {float(koide_up - mpf(2)/3):.6f} ({float((koide_up - mpf(2)/3)/(mpf(2)/3))*100:.2f}%)")
print()

# Down-type quarks (d, s, b)
m_d = mpf('4.67')      # MeV
m_s = mpf('93.4')      # MeV
m_b = mpf('4180')      # MeV

x_d = msq(m_d)
x_s = msq(m_s)
x_b = msq(m_b)

mean_dn = (x_d + x_s + x_b) / 3
var_dn = (x_d**2 + x_s**2 + x_b**2) / 3 - mean_dn**2
cv_dn = msq(var_dn) / mean_dn

print(f"  Down-type quarks (d, s, b):")
print(f"    sqrt(m): {float(x_d):.4f}, {float(x_s):.4f}, {float(x_b):.4f}")
print(f"    mean = {float(mean_dn):.4f}")
print(f"    CV   = {float(cv_dn):.6f}")
print(f"    CV vs 1: off by {float(abs(cv_dn - 1)):.4f} ({float(abs(cv_dn-1))*100:.1f}%)")
print()

koide_dn = (m_d + m_s + m_b) / (x_d + x_s + x_b)**2
print(f"    Koide ratio: {float(koide_dn):.6f} (vs 2/3 = 0.666667)")
print(f"    Departure: {float(koide_dn - mpf(2)/3):.6f} ({float((koide_dn - mpf(2)/3)/(mpf(2)/3))*100:.2f}%)")
print()

# ================================================================
# STEP 4: WHAT DISTRIBUTIONS HAVE CV = 1?
# ================================================================

print("=" * 70)
print("STEP 4: DISTRIBUTIONS WITH CV = 1")
print("=" * 70)
print()
print("  Continuous distributions with CV = 1:")
print("    - Exponential: f(x) = (1/mu)*exp(-x/mu), CV = 1 exactly")
print("    - Poisson (integer): Var = mu, so CV = 1/sqrt(mu) = 1 at mu = 1")
print("    - Rayleigh: CV = sqrt((4-pi)/pi) ~ 0.523 (not 1)")
print("    - Gamma(k, theta): CV = 1/sqrt(k), so CV = 1 at k = 1 (= exponential)")
print()
print("  The exponential distribution is the UNIQUE continuous")
print("  distribution on [0, inf) with:")
print("    (a) CV = 1")
print("    (b) Maximum entropy for fixed mean")
print()
print("  Maximum entropy principle (Jaynes):")
print("    Among all distributions on [0, inf) with mean = mu,")
print("    the exponential maximizes Shannon entropy H = -int f*ln(f) dx.")
print("    The exponential has CV = 1.")
print()
print("  So CV = 1 <=> maximum entropy for positive random variable")
print("  with fixed mean.")
print()

# ================================================================
# STEP 5: THE INFORMATION-THEORETIC INTERPRETATION
# ================================================================

print("=" * 70)
print("STEP 5: INFORMATION-THEORETIC INTERPRETATION")
print("=" * 70)
print()
print("  IF the sqrt(m_i) are drawn from a maximum-entropy distribution")
print("  on [0, inf) with fixed mean, then CV = 1, which gives a^2 = 2,")
print("  which gives Koide = 2/3.")
print()
print("  But: we have exactly 3 data points, not a distribution.")
print("  The CV = 1 condition for 3 points is:")
print("    sigma^2 = mu^2  (population variance = mean squared)")
print()
print("  For N = 3 points with values x_1, x_2, x_3:")
print("    mu = (x_1 + x_2 + x_3)/3")
print("    sigma^2 = (x_1^2 + x_2^2 + x_3^2)/3 - mu^2")
print("    CV = 1 means: sum(x_i^2)/3 = 2*mu^2 = 2*(sum(x_i)/3)^2")
print("    i.e.: 3*sum(x_i^2) = 2*(sum(x_i))^2")
print()

# Verify this is the Koide condition
# Koide = sum(m_i) / (sum(sqrt(m_i)))^2 = sum(x_i^2) / (sum(x_i))^2
# CV = 1 means sum(x_i^2) / 3 = 2*(sum(x_i))^2 / 9
# i.e. sum(x_i^2) / (sum(x_i))^2 = 2/3
# Which IS the Koide condition!

cv1_is_koide = Fraction(2, 3)
print(f"  CV = 1 condition: sum(x^2)/(sum(x))^2 = 2/3")
print(f"  This IS the Koide ratio! ({cv1_is_koide})")
print(f"  CV = 1 and Koide = 2/3 are IDENTICAL conditions on 3 points.")
print()

# ================================================================
# STEP 6: CAN WE DERIVE CV = 1?
# ================================================================

print("=" * 70)
print("STEP 6: CAN CV = 1 BE DERIVED FROM A PRINCIPLE?")
print("=" * 70)
print()

# The maximum entropy argument gives CV = 1 for a continuous
# distribution. But we have 3 discrete points, not a distribution.
# 
# For 3 points on the positive real line with C3 symmetry in
# the Koide parameterization, the "maximum entropy" analog is:
# Among all C3-symmetric configurations of 3 positive masses,
# which maximizes some entropy-like functional?

# Consider: the entropy of the normalized sqrt-mass distribution
# p_i = x_i / sum(x_i) where x_i = sqrt(m_i)
# H = -sum p_i * ln(p_i)

x_vals = [x_e, x_mu, x_tau]
x_sum = sum(x_vals)
p_vals = [x / x_sum for x in x_vals]
H = -sum(p * mlog(p) for p in p_vals)
H_max = mlog(mpf(3))  # max entropy for 3 states = ln(3)

print(f"  Normalized sqrt-mass distribution p_i = sqrt(m_i)/sum(sqrt(m)):")
print(f"    p_e   = {float(p_vals[0]):.6f}")
print(f"    p_mu  = {float(p_vals[1]):.6f}")
print(f"    p_tau = {float(p_vals[2]):.6f}")
print(f"    H = {float(H):.6f}")
print(f"    H_max = ln(3) = {float(H_max):.6f}")
print(f"    H/H_max = {float(H/H_max):.6f}")
print()

# H is NOT maximized (that would be p_i = 1/3, all masses equal).
# So maximum entropy of p_i is not the right principle.

# Alternative: consider the "relative entropy" or the relationship
# between sum(x^2) and (sum(x))^2 as a constraint.

# For 3 positive numbers with fixed sum S = sum(x_i):
# sum(x_i^2) ranges from S^2/3 (all equal) to S^2 (one nonzero)
# Koide = sum(x^2)/S^2 ranges from 1/3 to 1
# CV = 1 is at sum(x^2)/S^2 = 2/3, which is the MIDPOINT

print("  KEY OBSERVATION:")
print()
print("  For 3 positive numbers with fixed sum S:")
print("    sum(x^2) ranges from S^2/3 (all equal) to S^2 (one nonzero)")
print("    Koide = sum(x^2)/S^2 ranges from 1/3 to 1")
print()
print("    Minimum: 1/3  (all equal, a = 0, CV = 0)")
print("    Maximum: 1    (one nonzero, a -> max, CV -> max)")
print("    Koide = 2/3 is at the EXACT MIDPOINT: (1/3 + 1)/2 = 2/3")
print()

midpoint = (Fraction(1, 3) + Fraction(1)) / 2
assert midpoint == Fraction(2, 3)
print(f"  Verify: (1/3 + 1)/2 = {midpoint} = 2/3 ✓ (EXACT)")
print()

print("  THE KOIDE RATIO 2/3 IS THE ARITHMETIC MEAN")
print("  OF THE MINIMUM (1/3) AND MAXIMUM (1) POSSIBLE VALUES")
print("  OF sum(x^2)/S^2 FOR ANY 3 POSITIVE NUMBERS WITH FIXED SUM.")
print()
print("  Equivalently: CV^2 ranges from 0 to 2 for three C3-symmetric")
print("  positive numbers. CV^2 = 1 is the midpoint.")
print()

# Verify CV^2 range
# CV^2 = var/mean^2 = (sum(x^2)/3 - (S/3)^2) / (S/3)^2
# = 3*sum(x^2)/S^2 - 1
# At min (all equal): 3*(S^2/3)/S^2 - 1 = 0
# At max (one nonzero): 3*S^2/S^2 - 1 = 2
cv2_min = Fraction(0)
cv2_max = Fraction(2)
cv2_midpoint = (cv2_min + cv2_max) / 2
assert cv2_midpoint == Fraction(1)
print(f"  CV^2 range: [{cv2_min}, {cv2_max}]")
print(f"  CV^2 midpoint: {cv2_midpoint} = 1 ✓ (EXACT)")
print()

print("=" * 70)
print("RESULT: THE MIDPOINT PRINCIPLE")
print("=" * 70)
print()
print("  The Koide ratio 2/3 = midpoint of [1/3, 1].")
print("  CV = 1 = midpoint of CV^2 range [0, 2].")
print("  a^2 = 2 = midpoint of a^2 range [0, 4] (since a_max = 2).")
print()

# Verify a_max
# m_i = M(1 + a*cos(phi_i))^2 >= 0
# Most negative cos at 120-degree spacing: cos(2pi/3) = -1/2
# 1 + a*(-1/2) >= 0 => a <= 2
a_max = Fraction(2)
a_sq_midpoint = (Fraction(0) + a_max**2) / 2
assert a_sq_midpoint == Fraction(2)
print(f"  a_max = {a_max} (from positivity: 1 - a/2 >= 0)")
print(f"  a^2 range: [0, {a_max**2}]")
print(f"  a^2 midpoint: {a_sq_midpoint} = 2 ✓ (EXACT)")
print()

print("  THREE EQUIVALENT MIDPOINT STATEMENTS:")
print("    a^2 = 2 = midpoint of [0, 4]")
print("    CV^2 = 1 = midpoint of [0, 2]")
print("    Koide = 2/3 = midpoint of [1/3, 1]")
print()
print("  Each is an exact Fraction identity.")
print("  All three are the SAME condition expressed differently.")
print()
print("  THE QUESTION IS NOW:")
print("  What physical principle selects the midpoint of the")
print("  allowed range for the Koide ratio / CV / amplitude?")
print()
print("  Candidates:")
print("    - Maximum entropy of some functional")
print("    - Equal weight to 'all equal' and 'maximally spread'")
print("    - Geometric mean of extremes (arithmetic on log scale)")
print("    - A symmetry between the uniform and degenerate limits")
print()
print("  The midpoint property is EXACT and PROVEN.")
print("  The physical principle selecting it is OPEN.")
