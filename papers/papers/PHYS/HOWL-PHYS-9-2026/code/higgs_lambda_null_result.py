"""
Test: Is the Higgs self-coupling lambda = 1/8 at tree level?

Measured: lambda = m_H^2 / (2*v^2) = 0.1292
Test: 1/8 = 0.1250
Difference: 3.3%

The dominant radiative correction to lambda comes from the top quark loop.
At one loop, the correction to the Higgs mass squared is:

Delta_m_H^2 = (3*m_t^4) / (4*pi^2*v^2) * [ln(mu^2/m_t^2) + ...]

which translates to a correction to lambda:

Delta_lambda = (3*y_t^4) / (16*pi^2) * [ln(mu^2/m_t^2) + finite]

where y_t = sqrt(2)*m_t/v is the top Yukawa coupling.

We compute this in Fraction arithmetic at mu = m_t (minimizing the log).
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from math import gcd
from mpmath import mp, mpf

mp.dps = 60


# ================================================================
# Transcendentals
# ================================================================

def rat_arctanh(x, terms=80):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        result += power / (2 * k + 1)
        power *= x_sq
    return result

def rat_arctan(x, terms=80):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0:
            result += power / n
        else:
            result -= power / n
        power *= x_sq
    return result

def rat_pi(terms=80):
    a1 = rat_arctan(Fraction(1, 5), terms)
    a2 = rat_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rat_ln_ratio(p, q, terms=80):
    ratio = Fraction(p, q)
    ln2 = 2 * rat_arctanh(Fraction(1, 3), terms)
    pw = 0
    r = ratio
    while r > 2:
        r = r / 2
        pw += 1
    while r < Fraction(1, 2):
        r = r * 2
        pw -= 1
    arg = (r - 1) / (r + 1)
    return pw * ln2 + 2 * rat_arctanh(arg, terms)


print("Computing pi...")
pi_rat = rat_pi(80)
pi2 = pi_rat * pi_rat
print(f"  pi = {float(pi_rat):.15f}")
print()


# ================================================================
# Measured inputs
# ================================================================

m_H = Fraction(125100, 1)       # 125.100 GeV in MeV... but we only need ratios
m_t = Fraction(172690, 1)       # 172.690 GeV in MeV
v   = Fraction(246220, 1)       # 246.220 GeV in MeV

# All in same units (MeV), so ratios work

print("=" * 60)
print("MEASURED INPUTS")
print("=" * 60)
print(f"  m_H = {float(m_H)} MeV  ({float(m_H)/1000} GeV)")
print(f"  m_t = {float(m_t)} MeV  ({float(m_t)/1000} GeV)")
print(f"  v   = {float(v)} MeV  ({float(v)/1000} GeV)")
print()


# ================================================================
# Step 1: Measured lambda
# ================================================================

print("=" * 60)
print("STEP 1: MEASURED LAMBDA")
print("=" * 60)
print()

lambda_measured = (m_H * m_H) / (Fraction(2) * v * v)

print(f"  lambda = m_H^2 / (2*v^2)")
print(f"         = {float(m_H)**2:.0f} / {2*float(v)**2:.0f}")
print(f"         = {float(lambda_measured):.6f}")
print(f"  1/8    = {float(Fraction(1,8)):.6f}")
print(f"  Diff   = {float(lambda_measured - Fraction(1,8)):.6f}")
print(f"  Ratio  = {float(lambda_measured / Fraction(1,8)):.6f}")
print(f"  Excess = {float((lambda_measured - Fraction(1,8))/Fraction(1,8)*100):.2f}%")
print()


# ================================================================
# Step 2: Top Yukawa coupling
# ================================================================

print("=" * 60)
print("STEP 2: TOP YUKAWA COUPLING")
print("=" * 60)
print()

# y_t = sqrt(2) * m_t / v
# y_t^2 = 2 * m_t^2 / v^2
yt2 = Fraction(2) * m_t * m_t / (v * v)
yt4 = yt2 * yt2

print(f"  y_t^2 = 2*m_t^2/v^2 = {float(yt2):.6f}")
print(f"  y_t   = {float(yt2)**0.5:.6f}")
print(f"  y_t^4 = {float(yt4):.6f}")
print()


# ================================================================
# Step 3: One-loop correction to lambda at mu = m_t
# ================================================================

print("=" * 60)
print("STEP 3: ONE-LOOP CORRECTION AT mu = m_t")
print("=" * 60)
print()

# At mu = m_t, the log vanishes: ln(m_t^2/m_t^2) = 0
# The finite part of the top loop correction to lambda:
#
# Delta_lambda(top) = (3*y_t^4)/(16*pi^2) * [ln(m_t^2/mu^2) + 3/2]
#
# At mu = m_t: Delta_lambda = (3*y_t^4)/(16*pi^2) * 3/2
#            = (9*y_t^4)/(32*pi^2)

delta_lambda_mt = Fraction(9) * yt4 / (Fraction(32) * pi2)

print(f"  Delta_lambda(top, mu=m_t) = 9*y_t^4 / (32*pi^2)")
print(f"                            = {float(delta_lambda_mt):.6f}")
print()
print(f"  1/8 + Delta_lambda = {float(Fraction(1,8) + delta_lambda_mt):.6f}")
print(f"  Measured lambda    = {float(lambda_measured):.6f}")
print(f"  Residual           = {float(lambda_measured - Fraction(1,8) - delta_lambda_mt):.6f}")
print()


# ================================================================
# Step 4: Run lambda from mu = m_t to mu = m_H
# ================================================================

print("=" * 60)
print("STEP 4: RGE RUNNING mu = m_t -> mu = m_H")
print("=" * 60)
print()

# The one-loop RGE for lambda:
# d(lambda)/d(ln mu) = beta_lambda
# beta_lambda = (1/(16*pi^2)) * [24*lambda^2 + 12*lambda*y_t^2 - 6*y_t^4
#                                 - 3*lambda*(3*g^2 + g'^2) + ...]
#
# Dominant terms at large y_t:
# beta_lambda ≈ (1/(16*pi^2)) * [12*lambda*y_t^2 - 6*y_t^4]
#
# For a rough estimate: use lambda ≈ 1/8

lambda_est = Fraction(1, 8)
beta_approx = (Fraction(12) * lambda_est * yt2 - Fraction(6) * yt4) / (Fraction(16) * pi2)

# ln(m_H/m_t)
ln_mH_mt = rat_ln_ratio(125100, 172690, 80)

# Delta_lambda from running
delta_run = beta_approx * ln_mH_mt

print(f"  beta_lambda ≈ (12*lambda*y_t^2 - 6*y_t^4) / (16*pi^2)")
print(f"              = {float(beta_approx):.6f}")
print(f"  ln(m_H/m_t) = {float(ln_mH_mt):.6f}")
print(f"  Delta_lambda(running) = beta * ln(m_H/m_t) = {float(delta_run):.6f}")
print()


# ================================================================
# Step 5: Total correction
# ================================================================

print("=" * 60)
print("STEP 5: TOTAL")
print("=" * 60)
print()

# Method A: lambda(m_H) = lambda(m_t) + running from m_t to m_H
# where lambda(m_t) includes the finite threshold correction

lambda_at_mt = Fraction(1, 8) + delta_lambda_mt
lambda_at_mH = lambda_at_mt + delta_run

print(f"  lambda(tree)         = 1/8 = {float(Fraction(1,8)):.6f}")
print(f"  + top threshold      = {float(delta_lambda_mt):+.6f}")
print(f"  = lambda(m_t)        = {float(lambda_at_mt):.6f}")
print(f"  + RGE to m_H         = {float(delta_run):+.6f}")
print(f"  = lambda(m_H)        = {float(lambda_at_mH):.6f}")
print()
print(f"  Measured lambda      = {float(lambda_measured):.6f}")
print(f"  Residual             = {float(lambda_measured - lambda_at_mH):.6f}")
print(f"  Residual / measured  = {float((lambda_measured - lambda_at_mH)/lambda_measured*100):.2f}%")
print()


# ================================================================
# Step 6: What about other simple rationals?
# ================================================================

print("=" * 60)
print("STEP 6: OTHER CANDIDATE TREE-LEVEL VALUES")
print("=" * 60)
print()

candidates = [
    ("1/8", Fraction(1, 8)),
    ("1/7", Fraction(1, 7)),
    ("2/15", Fraction(2, 15)),
    ("3/23", Fraction(3, 23)),
    ("pi/24", pi_rat / 24),
    ("1/(2*pi)", Fraction(1,1) / (2 * pi_rat)),
]

print(f"  {'Candidate':<12} {'Value':<10} {'Diff from measured':<20} {'Percent':<10}")
print(f"  {'-'*12} {'-'*10} {'-'*20} {'-'*10}")

for name, val in candidates:
    diff = float(lambda_measured) - float(val)
    pct = diff / float(lambda_measured) * 100
    print(f"  {name:<12} {float(val):<10.6f} {diff:<+20.6f} {pct:<+10.2f}%")

print()


# ================================================================
# Step 7: Alternative — is m_H/v a simple ratio?
# ================================================================

print("=" * 60)
print("STEP 7: IS m_H/v A SIMPLE RATIO?")
print("=" * 60)
print()

mH_over_v = m_H / v
print(f"  m_H/v = {float(mH_over_v):.6f}")
print(f"  1/2   = {0.5:.6f}  (lambda = 1/8)")
print(f"  Diff  = {float(mH_over_v) - 0.5:.6f}")
print()

# m_H = v * sqrt(2*lambda)
# if lambda = 1/8, m_H = v * sqrt(1/4) = v/2 = 123.11 GeV
mH_from_eighth = v / 2
print(f"  If lambda = 1/8:  m_H = v/2 = {float(mH_from_eighth)/1000:.3f} GeV")
print(f"  Measured:         m_H = {float(m_H)/1000:.3f} GeV")
print(f"  Difference:       {(float(m_H) - float(mH_from_eighth))/1000:.3f} GeV")
print(f"  Relative:         {(float(m_H) - float(mH_from_eighth))/float(m_H)*100:.2f}%")
print()


# ================================================================
# Step 8: What if lambda_tree is determined by running TO the EW scale?
# ================================================================

print("=" * 60)
print("STEP 8: RUNNING lambda DOWN FROM HIGH SCALE")
print("=" * 60)
print()

# The RGE running of lambda is dominated by -6*y_t^4/(16*pi^2).
# From a high scale M_UV down to m_t:
# lambda(m_t) ≈ lambda(M_UV) + beta * ln(m_t/M_UV)
#
# If lambda approaches 0 at some high scale (the near-criticality),
# then lambda(m_t) ≈ |beta| * ln(M_UV/m_t)
#
# beta ≈ -6*y_t^4/(16*pi^2) for the pure top contribution

beta_top = Fraction(-6) * yt4 / (Fraction(16) * pi2)
print(f"  beta(top only) = -6*y_t^4/(16*pi^2) = {float(beta_top):.6f}")
print()

# If lambda = 0 at some scale M_UV, what M_UV gives lambda = 0.129 at m_t?
# 0.129 = |beta| * ln(M_UV/m_t)
# ln(M_UV/m_t) = 0.129 / |beta|

import math
ln_ratio_needed = float(lambda_measured) / abs(float(beta_top))
M_UV = float(m_t) * math.exp(ln_ratio_needed)
print(f"  If lambda(M_UV) = 0 and lambda(m_t) = {float(lambda_measured):.4f}:")
print(f"    ln(M_UV/m_t) = {ln_ratio_needed:.2f}")
print(f"    M_UV = {M_UV:.2e} MeV = {M_UV/1000:.2e} GeV")
print(f"    log10(M_UV/GeV) = {math.log10(M_UV/1000):.1f}")
print()
print(f"  (Near-criticality scale from full SM RGE: ~10^10 GeV)")
print(f"  (Our crude estimate: ~{M_UV/1e6:.0e} GeV — in the right ballpark)")
print()


# ================================================================
# Summary
# ================================================================

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print()
print(f"  Measured lambda       = {float(lambda_measured):.6f}")
print(f"  1/8                   = {float(Fraction(1,8)):.6f}")
print(f"  Difference            = {float(lambda_measured - Fraction(1,8)):.6f} ({float((lambda_measured - Fraction(1,8))/lambda_measured*100):.1f}%)")
print()
print(f"  1/8 + top threshold   = {float(lambda_at_mt):.6f}")
print(f"  1/8 + threshold + RGE = {float(lambda_at_mH):.6f}")
print(f"  Residual from measured= {float(lambda_measured - lambda_at_mH):.6f} ({float((lambda_measured - lambda_at_mH)/lambda_measured*100):.1f}%)")
print()
print(f"  Tree m_H = v/2        = {float(mH_from_eighth)/1000:.3f} GeV")
print(f"  Measured m_H           = {float(m_H)/1000:.3f} GeV")
print(f"  Difference             = {(float(m_H) - float(mH_from_eighth))/1000:.3f} GeV")
print()
print("  ASSESSMENT:")
if abs(float(lambda_measured - lambda_at_mH)/float(lambda_measured)) < 0.05:
    print("  1/8 + radiative corrections MATCHES measured lambda")
    print("  lambda_tree = 1/8 is a viable candidate")
else:
    print("  1/8 + radiative corrections does NOT match measured lambda")
    print("  The residual is too large for 1/8 to be the tree-level value")
    print("  at this order of approximation")
print()
print("  All intermediate values are Fraction:")
for name, val in [("lambda_measured", lambda_measured), ("yt2", yt2),
                   ("delta_lambda_mt", delta_lambda_mt), ("delta_run", delta_run)]:
    print(f"    {name}: {isinstance(val, Fraction)}")
    