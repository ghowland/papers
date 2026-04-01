#!/usr/bin/env python3
"""
PHYS-12 Phase 0: Establish the Exact Arithmetic Foundation
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi, acos as macos

mp.dps = 60

def f2m(f):
    """Fraction to mpf via string to avoid TypeError on old mpmath."""
    return mpf(f.numerator) / mpf(f.denominator)

print("=" * 70)
print("PHYS-12 PHASE 0: EXACT ARITHMETIC FOUNDATION")
print("=" * 70)
print()

# Q335 BASIS
Q = 2**335
p_pi    = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_pi2   = 690793580147337726804277647484346770338921354138994508002872352435529393755796399964695383625668575976
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506
p_sqrt3 = 121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154

pi_frac    = Fraction(p_pi, Q)
sqrt2_frac = Fraction(p_sqrt2, Q)
sqrt3_frac = Fraction(p_sqrt3, Q)

mp.dps = 40
for name, frac, ref in [("pi", pi_frac, mpi),
                         ("sqrt(2)", sqrt2_frac, msqrt(2)),
                         ("sqrt(3)", sqrt3_frac, msqrt(3))]:
    val = f2m(frac)
    s1, s2 = mp.nstr(val, 30), mp.nstr(ref, 30)
    assert s1 == s2, f"{name} FAILED: {s1} vs {s2}"
    print(f"  {name:<10} Q335 30-dig: OK")

two_pi_over_3 = Fraction(2 * p_pi, 3 * Q)
v = f2m(two_pi_over_3)
r = 2 * mpi / 3
assert mp.nstr(v, 25) == mp.nstr(r, 25)
print(f"  2pi/3      25-dig: OK")
print(f"  cos(2pi/3) = -1/2 EXACT")
print()

# DATA-2 MASSES
m_e   = Fraction(51099895069, 10**11)
m_mu  = Fraction(1056583755, 10**7)
m_tau = Fraction(177686, 100)
m_u = Fraction(216, 100)
m_c = Fraction(1273, 1)
m_t = Fraction(172570, 1)
m_d = Fraction(470, 100)
m_s = Fraction(935, 10)
m_b = Fraction(4183, 1)

print("  MASSES (Fraction):")
for nm, v in [('m_e',m_e),('m_mu',m_mu),('m_tau',m_tau),
              ('m_u',m_u),('m_c',m_c),('m_t',m_t),
              ('m_d',m_d),('m_s',m_s),('m_b',m_b)]:
    print(f"    {nm:<6} = {float(v):.6f} MeV")
print()

# ================================================================
# KOIDE COMPUTATION
# ================================================================

def koide_full(m1, m2, m3, label=""):
    mp.dps = 50
    M1, M2, M3 = f2m(m1), f2m(m2), f2m(m3)
    s1, s2, s3 = msqrt(M1), msqrt(M2), msqrt(M3)
    roots = sorted([s1, s2, s3])
    s1, s2, s3 = roots  # ascending order

    sum_m = M1 + M2 + M3
    sum_sqrt = s1 + s2 + s3
    K = sum_m / sum_sqrt**2

    a_sq = 2 * (3 * K - 1)
    a = msqrt(abs(a_sq)) if a_sq >= 0 else mpf(0)
    M = sum_sqrt / 3

    print(f"  {label}:")
    print(f"    K         = {mp.nstr(K, 15)}")
    print(f"    K - 2/3   = {mp.nstr(K - mpf(2)/3, 10)}")
    print(f"    a^2       = {mp.nstr(a_sq, 12)}")
    print(f"    a         = {mp.nstr(a, 12)}")
    print(f"    a - sqrt2 = {mp.nstr(a - msqrt(2), 10)}")
    print(f"    M         = {mp.nstr(M, 10)} sqrt(MeV)")

    # Extract phases: cos(phi_k) = (s_k/M - 1)/a
    phases = []
    for si in [s1, s2, s3]:
        c = float((si / M - 1) / a)
        if abs(c) <= 1.0:
            phases.append(float(macos(mpf(c))))
        elif abs(c) < 1.001:
            c = max(-1.0, min(1.0, c))
            phases.append(float(macos(mpf(c))))
        else:
            phases.append(None)

    if all(p is not None for p in phases):
        print(f"    phases:   [{phases[0]:.8f}, {phases[1]:.8f}, {phases[2]:.8f}]")
        # Sort phases descending for gap computation
        ps = sorted(phases, reverse=True)
        g01 = ps[0] - ps[1]
        g12 = ps[1] - ps[2]
        g20 = 2 * float(mpi) - ps[0] + ps[2]
        gaps = sorted([g01, g12, g20])
        ref = float(2 * mpi / 3)
        devs = [g - ref for g in gaps]
        D = sum(d**2 for d in devs)**0.5
        print(f"    gaps:     [{gaps[0]:.8f}, {gaps[1]:.8f}, {gaps[2]:.8f}]")
        print(f"    2pi/3:    {ref:.8f}")
        print(f"    devs:     [{devs[0]:.8f}, {devs[1]:.8f}, {devs[2]:.8f}]")
        print(f"    D:        {D:.8f}")
    else:
        D = None
        print(f"    phases:   NOT EXTRACTABLE")
        for i, si in enumerate([s1, s2, s3]):
            c = float((si / M - 1) / a)
            print(f"      cos(phi_{i}) = {c:.8f}")

    return float(K), float(a_sq), float(a), float(M), phases, D

print("=" * 70)
print("KOIDE RATIOS — ALL THREE SECTORS")
print("=" * 70)
print()

K_lep, a2_lep, a_lep, M_lep, ph_lep, D_lep = koide_full(
    m_e, m_mu, m_tau, "Charged Leptons (e, mu, tau)")
print()

K_up, a2_up, a_up, M_up, ph_up, D_up = koide_full(
    m_u, m_c, m_t, "Up-type Quarks (u, c, t)")
print()

K_dn, a2_dn, a_dn, M_dn, ph_dn, D_dn = koide_full(
    m_d, m_s, m_b, "Down-type Quarks (d, s, b)")
print()

# ================================================================
# SUMMARY
# ================================================================

print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print()
print(f"  {'Sector':<16} {'K':>12} {'K-2/3':>14} {'a':>10} {'a^2':>10} {'D':>10}")
print(f"  {'-'*16} {'-'*12} {'-'*14} {'-'*10} {'-'*10} {'-'*10}")
for lbl, K, a, a2, D in [("Leptons", K_lep, a_lep, a2_lep, D_lep),
                          ("Up quarks", K_up, a_up, a2_up, D_up),
                          ("Down quarks", K_dn, a_dn, a2_dn, D_dn)]:
    D_s = f"{D:.6f}" if D is not None else "N/A"
    print(f"  {lbl:<16} {K:>12.8f} {K-2/3:>14.8f} {a:>10.6f} {a2:>10.6f} {D_s:>10}")

print()
print(f"  sqrt(2) = 1.41421356...")
print(f"  2/3     = 0.66666667...")
print()

# ORDERING
print("=" * 70)
print("ORDERING TESTS")
print("=" * 70)
print()
ord_K = K_lep < K_dn < K_up
print(f"  K: lep ({K_lep:.6f}) < dn ({K_dn:.6f}) < up ({K_up:.6f}) : {ord_K}")
ord_a = a_lep < a_dn < a_up
print(f"  a: lep ({a_lep:.6f}) < dn ({a_dn:.6f}) < up ({a_up:.6f}) : {ord_a}")
if D_lep is not None and D_dn is not None and D_up is not None:
    ord_D = D_lep < D_dn < D_up
    print(f"  D: lep ({D_lep:.6f}) < dn ({D_dn:.6f}) < up ({D_up:.6f}) : {ord_D}")
else:
    print(f"  D: incomplete (some phases not extractable)")
print()

# KEY: all quarks K > 2/3, leptons K < 2/3
print(f"  Leptons K < 2/3: {K_lep < 2/3}")
print(f"  Up      K > 2/3: {K_up > 2/3}")
print(f"  Down    K > 2/3: {K_dn > 2/3}")
print()

# ASSERTIONS
assert abs(K_lep - 2/3) < 0.001
assert K_up > 2/3
assert K_dn > 2/3
assert ord_K
assert ord_a

print("=" * 70)
print("ALL PHASE 0 ASSERTIONS PASS")
print("=" * 70)

