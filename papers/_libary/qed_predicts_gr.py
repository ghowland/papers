#!/usr/bin/env python3
"""
HOWL EXPLORATORY: QED Boundary Running Predicts GR Observables?
================================================================
Scan whether QED coupling corrections through soliton boundaries,
parameterized by R2 and R4, can reproduce GR-scale observables
(H0 tension, dark matter ratio, cosmological constant scale).

Null result constrains this parameter set, not the framework.
Future scans with different parameterizations remain open.

Backed by: sin2_theta_w_0.py (9/9), phys24_gap_ratio.py
Platform:  phys24_lib.py (21/21 self-test, 148/148 platform test)
"""

from phys24_lib import *

# ================================================================
# ADDITIONAL CONSTANTS (exploratory, not in library)
# ================================================================

# GR-side observables as Fractions where possible
H0_local_frac  = Fraction(7304, 100)       # 73.04 km/s/Mpc, SH0ES 2022
H0_CMB_frac    = Fraction(6736, 100)       # 67.36 km/s/Mpc, Planck 2018
Omega_DM_frac  = Fraction(2607, 10000)     # 0.2607, Planck 2018
Omega_b_frac   = Fraction(490, 10000)      # 0.0490, Planck 2018
G_N_frac       = Fraction(667430, 10**16)  # 6.67430e-11 m^3/(kg*s^2)
Lambda_obs_frac = Fraction(11056, 10**56)  # 1.1056e-52 m^-2

# Derived
H0_ratio = H0_CMB_frac * Fraction(1, 1) / H0_local_frac  # ~0.9222
DM_baryon = Omega_DM_frac / Omega_b_frac                  # ~5.32
vp_step  = Fraction(1, 1) / (Fraction(12, 1) * R2_f)     # 1/(12*R2) = 1/(3*pi)

# ================================================================
print("=" * 70)
print("QED BOUNDARY RUNNING: CAN QED CORRECTIONS REACH GR?")
print("=" * 70)
print()

# ================================================================
# SECTION 1: QED-SIDE INPUTS
# ================================================================

print("SECTION 1: QED-SIDE INPUTS (from phys24_lib)")
print("-" * 70)
print()
# uses alpha_inv (DATA-4 B1), R2_f (DATA-4 G13), R4_f (DATA-4 G14)
# uses b1_SM (N1), b2_SM (N2), b3_SM (N3), gap_SM (N10), gap_VL (N11)

show("alpha_inv (dimensionless)", f2m(alpha_inv))
show("alpha_em (dimensionless)", f2m(alpha_frac))
show("R2 = pi/4 (dimensionless)", f2m(R2_f))
show("R4 = pi^2/32 (dimensionless)", f2m(R4_f))
show("VP step 1/(12*R2) (dimensionless)", f2m(vp_step))
show("gap_SM = 218/115 (dimensionless)", f2m(gap_SM))
show("gap_VL = 38/27 (dimensionless)", f2m(gap_VL))
show("gap_measured (dimensionless)", f2m(gap_measured))
print()

# Base unit: alpha_em * VP_step = alpha/(3*pi)
base_unit = alpha_frac * vp_step
show("base_unit = alpha/(3*pi) (dimensionless)", f2m(base_unit))
print()

# ================================================================
# SECTION 2: GR-SIDE TARGETS
# ================================================================

print("SECTION 2: GR-SIDE TARGET OBSERVABLES")
print("-" * 70)
print()

show("H0 local (km/s/Mpc)", f2m(H0_local_frac))
show("H0 CMB (km/s/Mpc)", f2m(H0_CMB_frac))
show("H0 ratio CMB/local (dimensionless)", f2m(H0_ratio))

H0_tension_pct = (H0_local_frac - H0_CMB_frac) * Fraction(100, 1) / H0_CMB_frac
show("H0 tension (percent)", f2m(H0_tension_pct))

show("DM/baryon ratio (dimensionless)", f2m(DM_baryon))
show("Omega_DM (dimensionless)", f2m(Omega_DM_frac))
show("Omega_baryon (dimensionless)", f2m(Omega_b_frac))

# Planck scale from Fractions
hbar_mpf = f2m(hbar)
c_mpf = f2m(c)
G_N_mpf = f2m(G_N_frac)
from mpmath import sqrt as msqrt, log as mlog, pi as mpi
M_planck = msqrt(hbar_mpf * c_mpf / G_N_mpf)
L_planck = msqrt(hbar_mpf * G_N_mpf / (c_mpf ** 3))
Lambda_planck = f2m(Lambda_obs_frac) * L_planck ** 2

print()
show("G_Newton (m^3 kg^-1 s^-2)", G_N_mpf)
show("M_Planck (kg)", M_planck)
show("L_Planck (m)", L_planck)
show("Lambda observed (m^-2)", f2m(Lambda_obs_frac))
show("Lambda in Planck units (dimensionless)", Lambda_planck)
show("log10(Lambda_Planck) (dimensionless)", mlog(Lambda_planck, 10))
print()

# ================================================================
# SECTION 3: SCAN — WHAT N AND r REPRODUCE THE TENSION?
# ================================================================

print("SECTION 3: PER-TRANSIT CORRECTION SCAN")
print("-" * 70)
print()
print("  For each boundary count N, compute r such that r^N = H0_CMB/H0_local.")
print("  Then express (1-r) in units of R2, R4, and alpha/(3*pi).")
print()

R2_mpf = f2m(R2_f)
R4_mpf = f2m(R4_f)
ratio_target_mpf = f2m(H0_ratio)
base_mpf = f2m(base_unit)

print("  %8s %14s %14s %14s %14s %14s" %
      ("N_eff", "r_avg", "1-r", "(1-r)/R2", "(1-r)/R4", "(1-r)/base"))
print("  %8s %14s %14s %14s %14s %14s" %
      ("-" * 8, "-" * 14, "-" * 14, "-" * 14, "-" * 14, "-" * 14))

scan_data = []
N_values = [10, 30, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for N_eff in N_values:
    r_avg = ratio_target_mpf ** (mpf(1) / mpf(N_eff))
    omr = 1 - r_avg
    omr_R2 = omr / R2_mpf
    omr_R4 = omr / R4_mpf
    omr_base = omr / base_mpf

    scan_data.append((N_eff, r_avg, omr, omr_R2, omr_R4, omr_base))

    print("  %8d %14s %14s %14s %14s %14s" %
          (N_eff,
           mp.nstr(r_avg, 11),
           mp.nstr(omr, 8),
           mp.nstr(omr_R2, 8),
           mp.nstr(omr_R4, 8),
           mp.nstr(omr_base, 8)))

print()

# ================================================================
# SECTION 4: RATIONAL STRUCTURE IN (1-r)/R2 AND (1-r)/R4
# ================================================================

print("SECTION 4: RATIONAL APPROXIMATION SEARCH")
print("-" * 70)
print()
print("  For each N, find closest p/q (q<=100) to (1-r)/R2 and (1-r)/R4.")
print()

def closest_frac(x_mpf, max_q=100):
    """Find p/q closest to x with q <= max_q. Returns (p, q, dist)."""
    best_p = 0
    best_q = 1
    best_d = abs(x_mpf)
    for q in range(1, max_q + 1):
        p = int(mpf(x_mpf) * q + mpf("0.5"))
        if p > 0:
            d = abs(mpf(x_mpf) - mpf(p) / mpf(q))
            if d < best_d:
                best_p = p
                best_q = q
                best_d = d
    return best_p, best_q, best_d

print("  %8s | %12s %8s %12s | %12s %8s %12s" %
      ("N_eff", "(1-r)/R2", "~p/q", "dist",
       "(1-r)/R4", "~p/q", "dist"))
print("  %8s | %12s %8s %12s | %12s %8s %12s" %
      ("-" * 8, "-" * 12, "-" * 8, "-" * 12,
       "-" * 12, "-" * 8, "-" * 12))

hits_R2 = []
hits_R4 = []

for N_eff, r_avg, omr, omr_R2, omr_R4, omr_base in scan_data:
    p2, q2, d2 = closest_frac(omr_R2)
    p4, q4, d4 = closest_frac(omr_R4)

    flag = ""
    if d2 < mpf("0.001") and q2 <= 50:
        flag = " <-- R2"
        hits_R2.append((N_eff, p2, q2, d2))
    if d4 < mpf("0.001") and q4 <= 50:
        flag = flag + " <-- R4"
        hits_R4.append((N_eff, p4, q4, d4))

    print("  %8d | %12s %4d/%-3d %12s | %12s %4d/%-3d %12s%s" %
          (N_eff,
           mp.nstr(omr_R2, 8), p2, q2, mp.nstr(d2, 6),
           mp.nstr(omr_R4, 8), p4, q4, mp.nstr(d4, 6),
           flag))

print()
if hits_R2:
    print("  R2 HITS (q<=50, dist<0.001):")
    for N, p, q, d in hits_R2:
        print("    N=%d: (1-r)/R2 ~ %d/%d (dist %s)" %
              (N, p, q, mp.nstr(d, 4)))
        print("      -> 1-r = (%d/%d) * pi/4" % (p, q))
else:
    print("  No R2 rational hits at q<=50, dist<0.001")

print()
if hits_R4:
    print("  R4 HITS (q<=50, dist<0.001):")
    for N, p, q, d in hits_R4:
        print("    N=%d: (1-r)/R4 ~ %d/%d (dist %s)" %
              (N, p, q, mp.nstr(d, 4)))
        print("      -> 1-r = (%d/%d) * pi^2/32" % (p, q))
else:
    print("  No R4 rational hits at q<=50, dist<0.001")
print()

# ================================================================
# SECTION 5: VP STEP CONNECTION
# ================================================================

print("SECTION 5: IS (1-r) A MULTIPLE OF alpha/(3*pi)?")
print("-" * 70)
print()

print("  %8s %14s %10s %12s" %
      ("N_eff", "(1-r)/base", "nearest k", "residual"))
print("  %8s %14s %10s %12s" %
      ("-" * 8, "-" * 14, "-" * 10, "-" * 12))

vp_hits = []
for N_eff, r_avg, omr, omr_R2, omr_R4, omr_base in scan_data:
    k_near = int(omr_base + mpf("0.5"))
    residual = abs(omr_base - mpf(k_near))
    flag = ""
    if residual < mpf("0.1") and k_near > 0:
        flag = " <--"
        vp_hits.append((N_eff, k_near, residual))

    print("  %8d %14s %10d %12s%s" %
          (N_eff, mp.nstr(omr_base, 8), k_near, mp.nstr(residual, 6), flag))

print()
if vp_hits:
    print("  VP-STEP HITS:")
    for N, k, res in vp_hits:
        print("    N=%d: (1-r) ~ %d * alpha/(3*pi) (residual %s)" %
              (N, k, mp.nstr(res, 4)))
else:
    print("  No VP-step integer multiples found (residual < 0.1)")
print()

# ================================================================
# SECTION 6: DARK MATTER FROM R2/R4 RATIONALS
# ================================================================

print("SECTION 6: DM/BARYON FROM R2/R4 MULTIPLES")
print("-" * 70)
print()

DM_target = f2m(DM_baryon)
show("Target DM/baryon (dimensionless)", DM_target)
print()

dm_hits = []
for p in range(1, 25):
    for q in range(1, 25):
        pq = Fraction(p, q)
        # Test p/q * R2
        val_R2 = f2m(pq * R2_f)
        d_R2 = abs(val_R2 - DM_target)
        if d_R2 < mpf("0.05"):
            dm_hits.append(("%d/%d * R2" % (p, q), val_R2, d_R2))
        # Test p/q * R4
        val_R4 = f2m(pq * R4_f)
        d_R4 = abs(val_R4 - DM_target)
        if d_R4 < mpf("0.05"):
            dm_hits.append(("%d/%d * R4" % (p, q), val_R4, d_R4))
        # Test p/q * pi
        val_pi = f2m(pq * pi_f)
        d_pi = abs(val_pi - DM_target)
        if d_pi < mpf("0.05"):
            dm_hits.append(("%d/%d * pi" % (p, q), val_pi, d_pi))
        # Test pure rational p/q
        val_pq = f2m(pq)
        d_pq = abs(val_pq - DM_target)
        if d_pq < mpf("0.02"):
            dm_hits.append(("%d/%d" % (p, q), val_pq, d_pq))

dm_hits.sort(key=lambda x: x[2])

if dm_hits:
    print("  %20s %14s %14s" % ("Expression", "Value", "Distance"))
    print("  %20s %14s %14s" % ("-" * 20, "-" * 14, "-" * 14))
    for expr, val, dist in dm_hits[:15]:
        flag = " <--" if dist < mpf("0.01") else ""
        print("  %20s %14s %14s%s" %
              (expr, mp.nstr(val, 8), mp.nstr(dist, 6), flag))
else:
    print("  No DM/baryon hits from R2/R4/pi multiples")
print()

# ================================================================
# SECTION 7: COSMOLOGICAL CONSTANT FROM alpha^N
# ================================================================

print("SECTION 7: LAMBDA FROM POWERS OF alpha")
print("-" * 70)
print()

alpha_mpf = f2m(alpha_frac)
log10_alpha = mlog(alpha_mpf, 10)
log10_Lambda = mlog(Lambda_planck, 10)

show("log10(alpha_em) (dimensionless)", log10_alpha)
show("log10(Lambda_Planck) (dimensionless)", log10_Lambda)
print()

# alpha^N = Lambda requires N = log10(Lambda)/log10(alpha)
N_alpha = log10_Lambda / log10_alpha
show("N for alpha^N = Lambda (dimensionless)", N_alpha)
print()

print("  %6s %14s %14s" % ("N", "log10(alpha^N)", "miss from -122"))
print("  %6s %14s %14s" % ("-" * 6, "-" * 14, "-" * 14))
for N_test in [56, 57, 58, 59]:
    log_val = mpf(N_test) * log10_alpha
    miss = log_val - log10_Lambda
    print("  %6d %14s %14s" %
          (N_test, mp.nstr(log_val, 8), mp.nstr(miss, 6)))

print()

# Loop factor alpha/(4*pi)
loop_f = alpha_mpf / (4 * mpi)
log10_loop = mlog(loop_f, 10)
N_loop = log10_Lambda / log10_loop
show("loop factor alpha/(4pi) (dimensionless)", loop_f)
show("log10(alpha/(4pi)) (dimensionless)", log10_loop)
show("N for (alpha/4pi)^N = Lambda (dimensionless)", N_loop)
print()

print("  %6s %14s %14s" % ("N", "log10((a/4pi)^N)", "miss"))
print("  %6s %14s %14s" % ("-" * 6, "-" * 14, "-" * 14))
for N_test in [32, 33, 34, 35]:
    log_val = mpf(N_test) * log10_loop
    miss = log_val - log10_Lambda
    print("  %6d %14s %14s" %
          (N_test, mp.nstr(log_val, 8), mp.nstr(miss, 6)))

print()

# VP-based: (alpha/(3*pi))^N
log10_base = mlog(base_mpf, 10)
N_base = log10_Lambda / log10_base
show("log10(alpha/(3pi)) (dimensionless)", log10_base)
show("N for (alpha/(3pi))^N = Lambda (dimensionless)", N_base)
print()

print("  %6s %14s %14s" % ("N", "log10((a/3pi)^N)", "miss"))
print("  %6s %14s %14s" % ("-" * 6, "-" * 14, "-" * 14))
for N_test in [38, 39, 40, 41]:
    log_val = mpf(N_test) * log10_base
    miss = log_val - log10_Lambda
    print("  %6d %14s %14s" %
          (N_test, mp.nstr(log_val, 8), mp.nstr(miss, 6)))

print()

# ================================================================
# SECTION 8: DIRECTIONAL H0 FROM OBSERVER POSITION
# ================================================================

print("SECTION 8: DIRECTIONAL H0 FROM GALACTIC POSITION")
print("-" * 70)
print()
print("  Sun at R=8 kpc, z=25 pc above midplane, disk R~15 kpc.")
print("  Schematic boundary counts for different viewing directions.")
print()

# Use N_eff=100 calibration
r100 = ratio_target_mpf ** (mpf(1) / mpf(100))

directions = [
    ("Galactic pole (up)", 2, "Through disk once + halo"),
    ("Galactic pole (down)", 2, "Through disk once + halo"),
    ("Galactic center", 5, "Dense disk + bulge + far side"),
    ("Galactic anticenter", 3, "Sparse outer disk"),
    ("In-plane tangent", 10, "Along spiral arm"),
    ("Toward Virgo cluster", 20, "Halo + local group + Virgo"),
    ("Toward CMB cold spot", 5, "Halo + possible void"),
]

print("  %25s %8s %14s %14s" %
      ("Direction", "N_gal", "r^N", "H0_apparent"))
print("  %25s %8s %14s %14s" %
      ("-" * 25, "-" * 8, "-" * 14, "-" * 14))

for name, N_gal, desc in directions:
    r_gal = r100 ** N_gal
    H0_app = f2m(H0_local_frac) * r_gal
    print("  %25s %8d %14s %14s" %
          (name, N_gal, mp.nstr(r_gal, 8), mp.nstr(H0_app, 6)))
    print("  %25s          %s" % ("", desc))

print()
print("  NOTE: N_gal is schematic. Real counts from galaxy surveys.")
print("  The TESTABLE PREDICTION is directional variation of H0.")
print()

# ================================================================
# CHECKS
# ================================================================

print("=" * 70)
print("CHECKS")
print("=" * 70)
print()

checks = []

chk_exact("H0_ratio is exact Fraction",
          H0_ratio, Fraction(6736, 7304), checks)

chk_exact("DM/baryon is exact Fraction",
          DM_baryon, Fraction(2607, 490), checks)

chk_exact("VP step = 1/(12*R2)",
          vp_step, Fraction(1, 1) / (Fraction(12) * R2_f), checks)

chk_exact("base_unit = alpha * VP_step",
          base_unit, alpha_frac * vp_step, checks)

chk_bool("H0 tension is positive",
         f2m(H0_local_frac) > f2m(H0_CMB_frac),
         "local %s > CMB %s" % (mp.nstr(f2m(H0_local_frac), 6),
                                 mp.nstr(f2m(H0_CMB_frac), 6)),
         checks)

chk_bool("Scan covers N=10 to N=10000",
         len(scan_data) == 10,
         "%d N values scanned" % len(scan_data),
         checks)

chk_bool("DM/baryon target in [5, 6]",
         mpf("5") < DM_target < mpf("6"),
         "DM/baryon = %s" % mp.nstr(DM_target, 6),
         checks)

chk_bool("log10(Lambda_Planck) in [-123, -121]",
         mpf("-123") < mlog(Lambda_planck, 10) < mpf("-121"),
         "log10(Lambda) = %s" % mp.nstr(mlog(Lambda_planck, 10), 6),
         checks)

chk("R2 from library matches pi/4",
    f2m(R2_f), mpi / 4, 99, checks)

chk("R4 from library matches pi^2/32",
    f2m(R4_f), mpi ** 2 / 32, 99, checks)

print()
print_summary(checks)
print()
print("=" * 70)
print("QED BOUNDARY RUNNING SCAN COMPLETE")
print("=" * 70)
