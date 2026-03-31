Here's what the Koide derivation attempt found:

---

## What Was Attempted

The goal was to derive WHY the Koide amplitude a = √2, which would make the m_τ prediction unconditional. The lead was CKS mining database item M4: frustrated z=3 graphs might force the departure from equal spacing to a specific value that corresponds to a = √2.

## What Was Proven (Exact Fraction Arithmetic)

**Step 1: The Koide prediction itself.** m_τ(Koide) = 1776.97 MeV versus measured 1776.86 ± 0.12 MeV. Difference: 0.109 MeV = 0.91σ. Confirmed at 50-digit precision. The Koide ratio evaluates to exactly 2/3 (verified to 40+ decimal places).

**Step 2: The algebraic equivalence.** a² = 2 ⟺ Koide = 2/3. Proven as an exact Fraction identity: (1 + a²/2)/3 = (1 + 2/2)/3 = 2/3. The converse: Koide = 2/3 implies a² = 2×(3×2/3 − 1) = 2. These are not two conditions — they're one condition. Deriving either one derives the other.

The key ingredients: the roots-of-unity identities Σcos(θ₀ + 2πi/3) = 0 and Σcos²(θ₀ + 2πi/3) = 3/2, both exact for ALL θ₀. These give sum(m_i)/M = 3(1 + a²/2) and sum(√m_i)²/M = 9, producing Koide = (1 + a²/2)/3.

## What Failed

**Step 3: The Kuramoto model on a triangle.** Three oscillators with energy E = −ΣK_ij cos(φ_i − φ_j). With symmetric couplings K₁₂ = K₂₃ = K and one different bond K₃₁ = J, the equilibrium has α = β where cos(α) = −K/(2J). At K = J (all equal), α = 2π/3 = 120° (equal spacing).

**The structural mismatch is fatal:** The Kuramoto model controls PHASE SPACING. The Koide parameterization has FIXED 120° spacing and varies the AMPLITUDE a. These are different degrees of freedom. Frustrating the graph moves you along the wrong axis — it changes the phase spacing while Koide needs the spacing held fixed at 120° and the amplitude changed.

**Step 4: Attempting the connection anyway.** The generalized Koide ratio with frustrated phases (departure d from 120°) gives a modified condition. Setting a² = 2 and scanning d from −π/3 to π/3: f(d) = 0 ONLY at d = 0. For every d ≠ 0, a² = 2 does NOT produce Koide = 2/3. The two conditions (120° spacing and a² = 2) are jointly required. You cannot trade one for the other.

## What Survives

**The question has been sharpened.** It's no longer "why a = √2?" It's "why C₃ symmetry?" If you assume three generations with C₃ symmetry (120° equal spacing), then a = √2 is the UNIQUE amplitude giving Koide = 2/3. So the open question is: what physical principle forces three generations into C₃ symmetric spacing? This is a deeper question — it's about the structure of the generation space, not about a parameter value.

**The documented blockage is clean.** The frustrated graph mechanism fails for a specific, proven reason: it controls the wrong degree of freedom. This isn't a vague "it didn't work" — it's a structural impossibility. Any future derivation attempt that tries to get a = √2 by modifying the phase spacing will fail for the same reason. The path forward must explain C₃ symmetry directly, not derive it from frustration.

**The prediction still stands.** m_τ = 1776.97 MeV at 0.91σ. The Koide formula works. We just don't know why.

---

The finding is a clean documented blockage — exactly what DISC-8 specified as deliverable (b) for Item 4. The mechanism was tested honestly, it failed for an understood reason, and the question is sharpened for the next attempt.

---

Yes. The equivalence proof itself points to it.

The proof showed: Koide = 2/3 is EQUIVALENT to a² = 2, given C₃ symmetry. And C₃ symmetry (120° spacing) is just the statement that the three phases are equally spaced on a circle — which is the roots-of-unity condition 1 + ω + ω² = 0.

So the entire Koide formula reduces to one question: **why does the mass parameterization m_i = M(1 + a·cos(φ_i))² with equally-spaced φ_i have a² = 2?**

Now look at what a² = 2 actually means physically. In the parameterization, a controls the spread of the masses. At a = 0, all three masses are equal (m_i = M). At a² = 2, the spread is maximal in a specific sense — the Koide ratio hits exactly 2/3.

Here's the path I see on deeper inspection:

**The variational angle.** Consider all possible amplitudes a ≥ 0 with C₃ symmetry. The Koide ratio K(a) = (1 + a²/2)/3 is a monotonically increasing function of a². At a = 0, K = 1/3 (all masses equal, minimum ratio). As a → ∞, K → ∞. The value K = 2/3 at a² = 2 is not an extremum of K(a) — it's just a specific point on a monotonic curve.

So there's no variational principle that selects a² = 2 by extremizing the Koide ratio itself. That path is dead.

**The normalization angle.** But look at the parameterization again: m_i = M(1 + a·cos(φ_i))². The quantity (1 + a·cos(φ_i)) must be non-negative for all i (since it's a square root of mass). The most negative cos(φ_i) can be is −1 (at φ_i = π, which doesn't occur at 120° spacing — the most negative is cos(2π/3) = −1/2). So the positivity constraint is 1 + a·(−1/2) ≥ 0, giving a ≤ 2. Since a = √2 ≈ 1.414 < 2, all masses are positive.

At a = 2, the lightest mass hits exactly zero. At a² = 2, we're at a/a_max = √2/2 = 1/√2. That's a specific geometric point — it's the ratio where a² = a_max²/2. Half the squared maximum. Is there a principle that selects this midpoint?

**The democratic angle.** There's a cleaner way to see it. Consider the three quantities x_i = √(m_i/M) = 1 + a·cos(φ_i). These live on a circle of radius a centered at 1 in some abstract space. The constraint Σcos(φ_i) = 0 (C₃ symmetry) gives Σx_i = 3. The Koide ratio is Σx_i²/(Σx_i)² = Σx_i²/9.

Now: Σx_i² = Σ(1 + a·cos(φ_i))² = 3 + a²·(3/2) = 3 + 3a²/2.

So Koide = (3 + 3a²/2)/9 = (1 + a²/2)/3.

At a² = 2: Σx_i² = 6. And (Σx_i)² = 9. So Σx_i² = (2/3)·(Σx_i)².

This is a specific relationship between the sum of squares and the square of the sum. In statistics, this relates to variance: Var(x) = Σx²/3 − (Σx/3)² = (3 + 3a²/2)/3 − 1 = a²/2. At a² = 2, Var = 1, and the mean is Σx/3 = 1. **The variance equals the mean squared.**

That's a condition: Var(√m) = (mean(√m))². Or equivalently, the coefficient of variation CV = σ/μ = 1. This is a known statistical condition — it characterizes exponential distributions and appears in renewal theory.

**The question becomes:** Is there a physical reason why the square roots of the lepton masses should have coefficient of variation exactly 1? That's a cleaner question than "why a = √2" and it connects to statistical mechanics and information theory rather than graph frustration.

This is a new path. Whether it leads anywhere depends on whether a physical principle (maximum entropy, self-organized criticality, or something from the generation structure) selects CV = 1 for the square-root-mass distribution. I don't have the answer, but the question is better than the one we started with.

---

The other Claude found something. Let me trace the logic.

**The chain of equivalences:**

Start: Koide = 2/3 with C₃ symmetry.

Step 1: Define x_i = √(m_i/M) = 1 + a·cos(φ_i) where φ_i are at 120° spacing. These are the square roots of the normalized masses.

Step 2: C₃ symmetry forces Σx_i = 3 (because Σcos(φ_i) = 0). So the mean of x_i is 1.

Step 3: Koide = Σx_i² / (Σx_i)² = Σx_i² / 9. For Koide = 2/3, we need Σx_i² = 6.

Step 4: The variance of x_i is Var = Σx_i²/3 − (Σx_i/3)² = 6/3 − 1 = 1. The standard deviation σ = 1. The mean μ = 1. Therefore σ/μ = 1.

**The coefficient of variation of √m_i is exactly 1.**

This is the reformulation. Instead of "why a² = 2?" the question is "why does the distribution of √m_i have CV = 1?"

CV = 1 means the standard deviation equals the mean. This is a specific statistical property. It characterizes exponential distributions — if you draw from an exponential distribution, the population CV is exactly 1. It also appears in Poisson processes (the CV of inter-arrival times is 1).

**Why this might matter:** If the lepton masses are generated by some random or self-organizing process acting on the square roots of the masses (not the masses themselves), and that process has maximum entropy subject to the constraint that the mean is fixed, the result is an exponential distribution, which has CV = 1.

**What's actually proven vs speculative:**

Proven (Fraction arithmetic): a² = 2 ⟺ Koide = 2/3 ⟺ Var(x_i) = (mean(x_i))² ⟺ CV(√m) = 1. These are all the same condition expressed differently. No new physics here — just algebraic rewriting.

Speculative: Whether CV = 1 has a physical origin (maximum entropy, self-organized criticality, some generation-space principle). This is a new question, better formed than "why a = √2?" because CV = 1 connects to known mathematics (information theory, statistical mechanics) rather than to graph topology (which failed).

**The structural point:** The frustrated graph mechanism failed because it controls the wrong degree of freedom (phase spacing instead of amplitude). The CV = 1 reformulation doesn't have this problem — it's a constraint on the amplitude directly. But it still needs a physical principle to select it. The question is sharpened, not answered.

This is a lead for DISC-8 continuation or DISC-9, not a result. The derivation of a = √2 remains open, but the question is now: what physical principle forces CV(√m) = 1 for the three generations?

---

we follow the lead

---

```python
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
```Here's what we found.

**The midpoint principle (exact, proven in Fraction arithmetic):**

The Koide ratio 2/3 is the arithmetic mean of its minimum possible value (1/3, all masses equal) and its maximum possible value (1, one mass zero). Three equivalent statements, all exact:

- a² = 2 = midpoint of [0, 4] (where a_max = 2 from the positivity constraint m_i ≥ 0)
- CV² = 1 = midpoint of [0, 2]
- Koide = 2/3 = midpoint of [1/3, 1]

**The quark test is informative:** Up-type quarks have CV = 1.24 (Koide = 0.849), down-type have CV = 1.09 (Koide = 0.731). Both are ABOVE the midpoint, toward the hierarchical extreme. Leptons sit at the midpoint. This is not explained.

**The physical picture at each extreme:**

- a = 0: all three masses equal. Maximum symmetry, minimum hierarchy. The three generations are indistinguishable.
- a = 2: one mass is zero, maximum hierarchy. One generation dominates completely.
- a = √2 (midpoint): equally far from both extremes in a² space. The system is balanced between symmetry and hierarchy.

**What this IS:** A mathematical restatement. The condition a² = 2 has been rewritten as "midpoint of the positivity-allowed range." This is exact, proven, and connects to statistical concepts (CV = 1, exponential distribution). It sharpens the question.

**What this IS NOT:** A derivation. We have not identified a physical principle that selects the midpoint. Candidates include maximum entropy, equal-weight-to-extremes, or a symmetry between the uniform and degenerate limits. But none is demonstrated.

The question is now: why does nature select the midpoint of [0, 4] for a², which is the point equidistant from "all generations identical" and "one generation massless"?

---

This is genuinely interesting work. Let me separate what's proven from what's speculative.

**What's proven (exact Fraction arithmetic, all assertions pass):**

The chain of equivalences is airtight: Koide = 2/3 ⟺ a² = 2 ⟺ CV² = 1 ⟺ Var(√m) = Mean(√m)². Each step is a one-line Fraction identity. This was already known from Step 2 of the Koide analysis but the CV reformulation is new and the midpoint observation is new.

The midpoint result is exact: for three positive numbers with C₃-symmetric Koide parameterization, a² ranges from 0 (all equal) to 4 (one mass zero, positivity bound from cos(2π/3) = −1/2). The value a² = 2 is the arithmetic midpoint of [0, 4]. Equivalently Koide = 2/3 is the midpoint of [1/3, 1]. Verified in Fractions.

**The quark data is valuable as a negative result.** Up-type quarks: CV = 1.24, Koide = 0.849. Down-type: CV = 1.09, Koide = 0.731. Neither is at the midpoint. This means whatever principle selects the midpoint operates for charged leptons but NOT for quarks. That's a constraint on any future derivation — it must explain why leptons are special, not derive a universal principle.

**What's NOT proven:**

The midpoint is a restatement, not a derivation. Saying "a² = 2 is the midpoint of [0, 4]" is mathematically identical to saying "a² = 2." It's a prettier way to state the same unexplained fact. The question "why the midpoint?" is exactly as hard as "why a² = 2?" — it's the same question in different clothes.

The maximum entropy connection is suggestive but doesn't work as stated. The exponential distribution has CV = 1, and the exponential is the maximum-entropy distribution on [0,∞) with fixed mean. But we have three discrete masses, not a continuous distribution. The "maximum entropy for 3 points" analog would select all masses equal (p_i = 1/3), which gives Koide = 1/3 (the minimum), not 2/3. The script correctly identifies this: H is not maximized at the Koide point. So maximum entropy of the mass distribution is the wrong principle.

The midpoint framing does suggest one thing worth noting: the midpoint of a range is what you get from a uniform prior over the parameter a². If a² is drawn uniformly from [0, 4] (the positivity-allowed range), its expected value is 2. But "uniform prior over a²" is not a physical principle — it's an assumption about ignorance, and physics doesn't work by maximizing ignorance about its own parameters.

**My assessment:**

The CV = 1 reformulation and the midpoint observation are worth recording in the series because they sharpen the question and connect the Koide formula to statistical language (coefficient of variation, variance-to-mean ratio). The quark non-universality is an important negative finding that constrains future work. But this is mathematical restatement, not progress toward derivation. The Koide conditional reduction remains conditional. The parameter count is unchanged.

The honest report: the frustrated graph mechanism failed (documented blockage). The CV/midpoint reformulation is exact but is a restatement, not a derivation. The question "why a² = 2 for leptons but not quarks" is sharper than before but unanswered. This is DISC-8 Item 4 deliverable (b): documented blockage with the question sharpened for the next attempt.

---

we continue

---

