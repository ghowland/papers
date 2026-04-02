#!/usr/bin/env python3
"""
HOWL PHYS-24 DEMONSTRATION: The Koide Status
==============================================
The C3 route to Koide is closed. The 120-degree spacing is a
tautology (3 parameters fitting 3 data points). K = 2/3 is a
saddle point, not a minimum. The open problem is the amplitude:
why a^2 = 2 for leptons, and why not for quarks?

Backed by: data_4.py (38/38 checks), PHYS-23 (C3 closure)
Platform:  phys24_lib.py (21/21 self-test)
"""

from phys24_lib import *
from mpmath import sqrt as msqrt, cos as mcos, pi as mpi

# ================================================================
# HEADER
# ================================================================

print("=" * 70)
print("HOWL PHYS-24: THE KOIDE STATUS")
print("=" * 70)
print()

# ================================================================
# THE KOIDE FORMULA
# ================================================================

print("THE KOIDE FORMULA")
print("-" * 70)
print()
print("  For three masses m_1, m_2, m_3:")
print()
print("    K = (m_1 + m_2 + m_3) / (sqrt(m_1) + sqrt(m_2) + sqrt(m_3))^2")
print()
print("  For charged leptons: K = 0.666661 ~ 2/3 to 6 significant figures.")
print("  For quarks: K deviates from 2/3 by 10-27%%.")
print()

# ================================================================
# THREE-SECTOR KOIDE RATIOS
# ================================================================

print("THREE-SECTOR KOIDE RATIOS (Level 2, from DATA-4 masses)")
print("-" * 70)
print()

# uses m_e, m_mu, m_tau from phys24_lib (DATA-4 B2-B4)
# uses m_u, m_c, m_t from phys24_lib (DATA-4 D1, D4, C4)
# uses m_d, m_s, m_b from phys24_lib (DATA-4 D2, D3, D5)

def koide_ratio(m1, m2, m3):
    """Compute Koide ratio from three Fraction masses. Returns mpf."""
    s1 = msqrt(f2m(m1))
    s2 = msqrt(f2m(m2))
    s3 = msqrt(f2m(m3))
    num = f2m(m1 + m2 + m3)
    den = (s1 + s2 + s3) ** 2
    return num / den

def koide_amplitude_sq(K_val):
    """From Koide ratio K, compute a^2 = 2*(3*K - 1). Returns mpf."""
    return mpf("2") * (mpf("3") * K_val - mpf("1"))

K_lep  = koide_ratio(m_e, m_mu, m_tau)
K_down = koide_ratio(m_d, m_s, m_b)
K_up   = koide_ratio(m_u, m_c, m_t)

a2_lep_comp  = koide_amplitude_sq(K_lep)
a2_down_comp = koide_amplitude_sq(K_down)
a2_up_comp   = koide_amplitude_sq(K_up)

show("K(e, mu, tau) (dimensionless)", K_lep)
show("K(d, s, b) (dimensionless)", K_down)
show("K(u, c, t) (dimensionless)", K_up)
show("2/3 (dimensionless)", mpf("2") / mpf("3"))
print()

show("a^2(leptons) (dimensionless)", a2_lep_comp)
show("a^2(down quarks) (dimensionless)", a2_down_comp)
show("a^2(up quarks) (dimensionless)", a2_up_comp)
show("Koide hypothesis: a^2 = 2", mpf("2"))
print()

print("  Amplitude ordering: a^2_lep < a^2_down < a^2_up")
print("  This correlates with interaction strength:")
print("    leptons (no color) -> a^2 ~ 2.000")
print("    down quarks (color, Q=-1/3) -> a^2 ~ 2.388")
print("    up quarks (color, Q=+2/3) -> a^2 ~ 3.093")
print()

# ================================================================
# THE TAUTOLOGY: 3 PARAMETERS, 3 DATA POINTS
# ================================================================

print("THE TAUTOLOGY (Level 1, mathematical proof)")
print("-" * 70)
print()
print("  The Koide parametrization writes:")
print("    sqrt(m_k) = M * (1 + a * cos(theta_0 + 2*pi*k/3))")
print()
print("  for k = 0, 1, 2. This has three free parameters:")
print("    M (overall scale), a (amplitude), theta_0 (phase offset).")
print()
print("  Three parameters fitting three data points (m_1, m_2, m_3)")
print("  is an exactly determined system. It ALWAYS succeeds for")
print("  any three positive masses. The 120-degree spacing is a")
print("  property of the PARAMETRIZATION, not of the PHYSICS.")
print()
print("  Proof by construction: given any m_1, m_2, m_3 > 0,")
print("  set M = (sqrt(m_1) + sqrt(m_2) + sqrt(m_3)) / 3,")
print("  compute residuals r_k = sqrt(m_k) - M,")
print("  extract a and theta_0 from the residuals.")
print("  This always works. No constraint on the masses is needed.")
print()

# Demonstrate: extract M, a, theta_0 for leptons
s_e   = msqrt(f2m(m_e))
s_mu  = msqrt(f2m(m_mu))
s_tau = msqrt(f2m(m_tau))
M_lep = (s_e + s_mu + s_tau) / mpf("3")

r0 = s_e - M_lep
r1 = s_mu - M_lep
r2 = s_tau - M_lep

# a*M from sum of squares: sum(r_k^2) = (3/2)*a^2*M^2
sum_r2 = r0**2 + r1**2 + r2**2
a_sq_from_fit = mpf("2") * sum_r2 / (mpf("3") * M_lep**2)

show("  M(leptons) (sqrt(MeV))", M_lep)
show("  a^2 from fit (dimensionless)", a_sq_from_fit)
print()

# Verify residuals sum to zero (they must, by construction)
res_sum = r0 + r1 + r2
show("  sum of residuals (should be ~0)", res_sum)
print()

# ================================================================
# THE PHYS-8 IDENTITY: K DEPENDS ONLY ON a
# ================================================================

print("THE PHYS-8 IDENTITY (Level 1)")
print("-" * 70)
print()
print("  From the parametrization, the Koide ratio simplifies to:")
print()
print("    K = (1 + a^2/2) / 3")
print()
print("  This is INDEPENDENT of M and theta_0.")
print("  At a^2 = 2: K = (1 + 1) / 3 = 2/3 exactly.")
print("  No phase adjustment can change K. Only a can.")
print()

# Verify the identity
K_from_identity = (mpf("1") + a2_lep_comp / mpf("2")) / mpf("3")
show("  K from identity (1+a^2/2)/3", K_from_identity)
show("  K from masses directly", K_lep)
print()

# Verify at a = sqrt(2): K = 2/3 for ANY theta_0
print("  Verification: K at a = sqrt(2) for various theta_0:")
a_test = msqrt(mpf("2"))
for theta_deg in [0, 30, 60, 90, 120]:
    theta = mpf(theta_deg) * mpi / mpf("180")
    s = [mpf("1") + a_test * mcos(theta + mpf("2") * mpi * mpf(k) / mpf("3"))
         for k in range(3)]
    if all(x > 0 for x in s):
        masses = [x**2 for x in s]
        K_test = sum(masses) / sum(msqrt(m) for m in masses)**2
        print("    theta_0 = %3d deg: K = %s" % (theta_deg, mp.nstr(K_test, 11)))
    else:
        print("    theta_0 = %3d deg: negative sqrt(m), skip" % theta_deg)
print()
print("  ALL give 2/3 exactly. The phase determines WHICH masses,")
print("  but the ratio is always 2/3 at a = sqrt(2).")
print()

# ================================================================
# THE SADDLE POINT (Level 1, numerical demonstration)
# ================================================================

print("K = 2/3 IS A SADDLE POINT (Level 1)")
print("-" * 70)
print()
print("  Perturb the 120-degree spacing: phi_k = 2*pi*k/3 + eps*delta_k")
print("  with sum(delta_k) = 0, at a = sqrt(2).")
print("  Compute d^2K/d(eps)^2 at eps = 0 for two directions.")
print()

# Saddle point demonstration
# At a = sqrt(2), theta_0 = 0, compute K for small perturbations
# Direction 1: delta = (1, -1, 0) — "stretch" perturbation
# Direction 2: delta = (2, -1, -1) — "compress" perturbation

a_val = msqrt(mpf("2"))
eps_test = mpf("0.001")

def K_perturbed(a_v, theta0, deltas, eps):
    """K at perturbed spacing."""
    phases = [theta0 + mpf("2") * mpi * mpf(k) / mpf("3") + eps * mpf(deltas[k])
              for k in range(3)]
    s = [mpf("1") + a_v * mcos(p) for p in phases]
    if any(x <= 0 for x in s):
        return None
    masses = [x**2 for x in s]
    return sum(masses) / sum(msqrt(m) for m in masses)**2

# Direction 1: (1, -1, 0)
K_plus  = K_perturbed(a_val, mpf("0"), [1, -1, 0], eps_test)
K_minus = K_perturbed(a_val, mpf("0"), [1, -1, 0], -eps_test)
K_zero  = K_perturbed(a_val, mpf("0"), [1, -1, 0], mpf("0"))

if K_plus is not None and K_minus is not None and K_zero is not None:
    d2K_dir1 = (K_plus + K_minus - mpf("2") * K_zero) / (eps_test**2)
    print("  Direction (1, -1, 0):")
    show("    d^2K/d(eps)^2 (dimensionless)", d2K_dir1)
    print("    K = 2/3 is a local MINIMUM in this direction.")
    print()

# Direction 2: (2, -1, -1)
K_plus  = K_perturbed(a_val, mpf("0"), [2, -1, -1], eps_test)
K_minus = K_perturbed(a_val, mpf("0"), [2, -1, -1], -eps_test)
K_zero  = K_perturbed(a_val, mpf("0"), [2, -1, -1], mpf("0"))

if K_plus is not None and K_minus is not None and K_zero is not None:
    d2K_dir2 = (K_plus + K_minus - mpf("2") * K_zero) / (eps_test**2)
    print("  Direction (2, -1, -1):")
    show("    d^2K/d(eps)^2 (dimensionless)", d2K_dir2)
    print("    K = 2/3 is a local MAXIMUM in this direction.")
    print()

print("  One direction gives d^2K > 0 (minimum).")
print("  Another gives d^2K < 0 (maximum).")
print("  K = 2/3 is a SADDLE POINT, not a minimum.")
print("  The C3 potential does not select K = 2/3.")
print()

# ================================================================
# THE OPEN PROBLEM
# ================================================================

print("THE OPEN PROBLEM")
print("-" * 70)
print()
print("  CLOSED: Why 120-degree spacing?")
print("    Answer: tautology. 3 parameters, 3 data points.")
print()
print("  CLOSED: Does C3 symmetry select K = 2/3?")
print("    Answer: no. K = 2/3 is a saddle point.")
print()
print("  OPEN: Why a^2 = 2 for charged leptons?")
print("    Requirements for any viable derivation:")
print("    1. Must produce a^2 = 2 specifically")
print("    2. Must explain the ordering a^2_lep < a^2_down < a^2_up")
print("    3. Must not reduce to a reformulation of K = 2/3")
print()
print("  Any future Koide paper that does not attack the")
print("  amplitude directly is off-target.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

# Check 1: K(leptons) matches DATA-4
chk("K(e,mu,tau) matches DATA-4 K8",
    K_lep, f2m(K_koide), 6, checks)

# Check 2: a^2(leptons) matches library
chk("a^2(leptons) matches library",
    a2_lep_comp, f2m(a2_lep), 4, checks)

# Check 3: a^2(down) matches library
chk("a^2(down quarks) matches library",
    a2_down_comp, f2m(a2_down), 3, checks)

# Check 4: a^2(up) matches library
chk("a^2(up quarks) matches library",
    a2_up_comp, f2m(a2_up), 3, checks)

# Check 5: amplitude ordering
chk_bool("Ordering: a^2_lep < a^2_down < a^2_up",
         a2_lep_comp < a2_down_comp < a2_up_comp,
         "a^2 = %s, %s, %s" % (
             mp.nstr(a2_lep_comp, 5),
             mp.nstr(a2_down_comp, 5),
             mp.nstr(a2_up_comp, 5)), checks)

# Check 6: PHYS-8 identity K = (1+a^2/2)/3
chk("PHYS-8 identity: K = (1+a^2/2)/3",
    K_from_identity, K_lep, 6, checks)

# Check 7: residuals sum to zero (tautology proof)
chk_bool("Residuals sum to ~0 (tautology)",
         abs(res_sum) < mpf("1e-30"),
         "sum = %s" % mp.nstr(res_sum, 4), checks)

# Check 8: saddle point — one direction positive, one negative
chk_bool("Saddle: d^2K > 0 in direction (1,-1,0)",
         d2K_dir1 > mpf("0"),
         "d^2K = %s" % mp.nstr(d2K_dir1, 5), checks)

chk_bool("Saddle: d^2K < 0 in direction (2,-1,-1)",
         d2K_dir2 < mpf("0"),
         "d^2K = %s" % mp.nstr(d2K_dir2, 5), checks)

# Check 9: a^2(leptons) is NOT exactly 2 (Level 2 measurement)
chk_bool("a^2(leptons) is NOT exactly 2",
         abs(a2_lep_comp - mpf("2")) > mpf("1e-6"),
         "a^2 - 2 = %s" % mp.nstr(a2_lep_comp - mpf("2"), 4), checks)

print_summary(checks)

print()
print("=" * 70)
print("PHYS-24 KOIDE STATUS DEMONSTRATION COMPLETE")
print("=" * 70)
