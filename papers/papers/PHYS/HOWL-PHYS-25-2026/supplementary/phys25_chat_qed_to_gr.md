conversation mode:

is there a path to writing a script that tries to make QED rules predict what GR predicts using our phys_24_lib.py and just assuming everything in it is the correct value and your current understanding of methods and inferences, write a python script to make QED generate GR results via the different configurations of perspectively, at different toroidal and sphere etc soliton boundaries through the center, at the edges, all the comibinations, we make it make predictions of what it should see, and match what values we know 

then after we have this script and data we can try to match it against measured cosmos data to see if there are matches, given our  calculated position in the toroid 

then we can see right away if theres a path this way, if not, null result is oK, we have our data for what we could do now and can try again later with different data

---

Yes, there's a path. The library has the exact couplings, beta coefficients, and the VL doublet shifts. The idea is: start from α at M_Z (QED/electroweak, known precisely), run it outward through hypothetical soliton boundary corrections parameterized by the geometry (sphere → R₂, torus → R₄), and see if the accumulated correction at cosmological distances produces numbers that match known GR observables (H₀, the dark matter fraction, the cosmological constant scale).

The script would be exploratory — a systematic scan, not a proof. It tests whether ANY combination of boundary geometry, correction magnitude, and transit count produces numbers in the right ballpark. A null result constrains the framework. A hit motivates deeper computation.

Let me read the library first to know what tools we have.Good — the library has everything we need for the QED side. It doesn't have cosmological constants (G_Newton, H₀, Planck mass), so we'll define those as Fractions from known values. Here's the script:

```python
#!/usr/bin/env python3
"""
qed_predicts_gr.py
===================

Exploratory: Can QED coupling running through soliton boundary
corrections reproduce GR-scale observables?

Method:
  1. Start from alpha at M_Z (QED, exact from phys24_lib)
  2. Define soliton boundary correction per crossing:
     - Sphere: r = 1 - epsilon * R2 * (M/M_ref)^p
     - Torus:  r = 1 - epsilon * R4 * (M/M_ref)^p * f(angle)
  3. Scan epsilon, M_ref, p over reasonable ranges
  4. Compute cumulative correction for various transit counts
  5. Compare to known GR observables:
     - H0 local vs CMB (ratio ~73/67.4 = 1.083)
     - Dark matter fraction (~0.85 in clusters, ~0.27 cosmological)
     - Cosmological constant scale (Lambda ~ 10^-122 in Planck units)

Output: systematic scan results to stdout + summary PNG

Uses phys24_lib.py as the source of truth for all QED constants.
All computation in Fraction arithmetic where possible.
"""

import sys
sys.path.insert(0, '/mnt/user-data/uploads')

try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp, mpf, log as mlog, exp as mexp, pi as mpi, sqrt as msqrt

mp.dps = 50

# Import everything from the library
from phys24_lib import (
    f2m, alpha_inv, alpha_frac, sin2_tW, alpha_s, cos2_tW,
    M_Z, m_e, m_mu, m_tau, m_t, m_p, M_W, G_F, m_H,
    b1_SM, b2_SM, b3_SM, db1_VL, db2_VL, db3_VL,
    b1_mod, b2_mod, b3_mod,
    gap_SM, gap_VL, gap_measured,
    inv_a1, inv_a2, inv_a3,
    alpha_1_GUT, alpha_2_GUT, alpha_3_GUT,
    R2_f, R4_f, pi_f, pi2_f, twopi_f, ln2_f, zeta3_f,
    h_planck, c, e_charge, hbar,
)

print("=" * 78)
print("QED PREDICTS GR: SOLITON BOUNDARY RUNNING SCAN")
print("=" * 78)
print()

# ================================================================
# SECTION 1: ESTABLISH QED-SIDE CONSTANTS (from library)
# ================================================================

print("SECTION 1: QED-SIDE CONSTANTS (from phys24_lib)")
print("-" * 78)
print()

alpha_em_mpf = f2m(alpha_frac)
print(f"  alpha_em        = {mp.nstr(alpha_em_mpf, 12)}")
print(f"  alpha_inv       = {mp.nstr(f2m(alpha_inv), 12)}")
print(f"  sin2_theta_W    = {mp.nstr(f2m(sin2_tW), 8)}")
print(f"  alpha_s(M_Z)    = {mp.nstr(f2m(alpha_s), 6)}")
print(f"  R2 = pi/4       = {mp.nstr(f2m(R2_f), 12)}")
print(f"  R4 = pi^2/32    = {mp.nstr(f2m(R4_f), 12)}")
print(f"  gap_SM (218/115) = {mp.nstr(f2m(gap_SM), 10)}")
print(f"  gap_VL (38/27)   = {mp.nstr(f2m(gap_VL), 10)}")
print(f"  gap_measured     = {mp.nstr(f2m(gap_measured), 10)}")
print()

# VP step size (the QED per-flavor correction rate)
vp_step = Fraction(1, 1) / (Fraction(12) * R2_f)  # 1/(12*R2) = 1/(3*pi)
print(f"  VP step = 1/(12*R2) = 1/(3*pi) = {mp.nstr(f2m(vp_step), 10)}")
print()

# ================================================================
# SECTION 2: GR-SIDE TARGET OBSERVABLES
# ================================================================

print("SECTION 2: GR-SIDE TARGET OBSERVABLES")
print("-" * 78)
print()

# Hubble constant measurements (km/s/Mpc)
H0_local = mpf('73.04')       # SH0ES 2022
H0_CMB   = mpf('67.36')       # Planck 2018
H0_ratio = H0_local / H0_CMB  # ~1.0843
H0_tension_pct = (H0_local - H0_CMB) / H0_CMB * 100

print(f"  H0 (local, SH0ES)   = {H0_local} km/s/Mpc")
print(f"  H0 (CMB, Planck)    = {H0_CMB} km/s/Mpc")
print(f"  H0 ratio            = {mp.nstr(H0_ratio, 6)}")
print(f"  Tension             = {mp.nstr(H0_tension_pct, 4)}%")
print()

# Dark matter fraction
Omega_DM     = mpf('0.2607')   # Planck 2018 cosmological DM fraction
Omega_baryon = mpf('0.0490')   # Planck 2018 baryon fraction
DM_to_baryon = Omega_DM / Omega_baryon  # ~5.32
DM_cluster   = mpf('0.85')    # typical cluster DM fraction

print(f"  Omega_DM (cosmological) = {Omega_DM}")
print(f"  Omega_baryon            = {Omega_baryon}")
print(f"  DM / baryon ratio       = {mp.nstr(DM_to_baryon, 4)}")
print(f"  DM fraction (clusters)  = {DM_cluster}")
print()

# Newton's G (for Planck scale)
G_N_num = Fraction(667430, 10**16)  # 6.67430e-11 m^3/(kg*s^2), 6 sf
G_N_mpf = mpf('6.67430e-11')

# Planck mass, length, time
M_planck = msqrt(f2m(hbar) * f2m(c) / G_N_mpf)  # ~2.176e-8 kg
L_planck = msqrt(f2m(hbar) * G_N_mpf / (f2m(c)**3))  # ~1.616e-35 m

# Cosmological constant in Planck units
Lambda_obs = mpf('1.1056e-52')  # m^-2, from Planck 2018
Lambda_planck = Lambda_obs * L_planck**2  # ~10^-122

print(f"  G_Newton            = {G_N_mpf} m^3/(kg*s^2)")
print(f"  M_Planck            = {mp.nstr(M_planck, 6)} kg")
print(f"  L_Planck            = {mp.nstr(L_planck, 6)} m")
print(f"  Lambda (observed)   = {Lambda_obs} m^-2")
print(f"  Lambda (Planck u.)  = {mp.nstr(Lambda_planck, 4)}")
print(f"  log10(Lambda_Pl)    = {mp.nstr(mlog(Lambda_planck, 10), 5)}")
print()

# ================================================================
# SECTION 3: THE PER-BOUNDARY CORRECTION MODEL
# ================================================================

print("SECTION 3: BOUNDARY CORRECTION MODEL")
print("-" * 78)
print()
print("  Model: at each soliton boundary crossing, the effective")
print("  coupling (or metric) picks up a multiplicative correction:")
print()
print("    r_sphere = 1 - eps * R2 * (M/M_ref)^p")
print("    r_torus  = 1 - eps * R4 * (M/M_ref)^p * f(angle)")
print()
print("  Cumulative over N crossings:")
print("    H0(N) / H0(0) = product of r_i")
print()
print("  For uniform boundary population:")
print("    H0(N) / H0(0) = r_avg^N")
print()

# The key constraint: H0_local/H0_CMB = r_avg^N_eff
# So r_avg = (H0_CMB/H0_local)^(1/N_eff)

print("  CONSTRAINT: H0_CMB / H0_local = r_avg^N_eff")
print()

# ================================================================
# SECTION 4: SCAN OVER BOUNDARY COUNT AND GEOMETRY
# ================================================================

print("SECTION 4: SCAN — WHAT N AND r REPRODUCE THE TENSION?")
print("-" * 78)
print()

R2_mpf = f2m(R2_f)
R4_mpf = f2m(R4_f)
ratio_target = H0_CMB / H0_local  # ~0.9222

print(f"  Target ratio H0_CMB/H0_local = {mp.nstr(ratio_target, 8)}")
print()
print(f"  {'N_eff':>8} {'r_avg':>14} {'1-r':>14} {'1-r in R2':>14} "
      f"{'1-r in R4':>14} {'ln(r)':>14}")
print(f"  {'-'*8} {'-'*14} {'-'*14} {'-'*14} {'-'*14} {'-'*14}")

scan_results = []

for N_eff in [10, 30, 50, 100, 200, 500, 1000, 2000, 5000, 10000]:
    r_avg = ratio_target ** (mpf(1) / N_eff)
    one_minus_r = 1 - r_avg
    # Express 1-r in units of R2 and R4
    omr_in_R2 = one_minus_r / R2_mpf
    omr_in_R4 = one_minus_r / R4_mpf
    ln_r = mlog(r_avg)

    scan_results.append((N_eff, r_avg, one_minus_r, omr_in_R2, omr_in_R4))

    print(f"  {N_eff:>8} {mp.nstr(r_avg, 10):>14} {mp.nstr(one_minus_r, 8):>14} "
          f"{mp.nstr(omr_in_R2, 8):>14} {mp.nstr(omr_in_R4, 8):>14} "
          f"{mp.nstr(ln_r, 8):>14}")

print()
print("  KEY: 1-r in R2 = (1-r)/(pi/4).  If this is a simple rational,")
print("  the correction has clean R2 content.")
print()

# ================================================================
# SECTION 5: CHECK FOR RATIONAL STRUCTURE IN 1-r
# ================================================================

print("SECTION 5: RATIONAL STRUCTURE SEARCH IN 1-r")
print("-" * 78)
print()
print("  For each N_eff, test whether (1-r)/R2 or (1-r)/R4 is")
print("  close to a simple fraction p/q with q <= 1000.")
print()

def closest_fraction(x, max_denom=1000):
    """Find p/q closest to x with q <= max_denom."""
    best_p, best_q, best_dist = 0, 1, abs(float(x))
    for q in range(1, max_denom + 1):
        p = round(float(x) * q)
        if p > 0:
            dist = abs(float(x) - p / q)
            if dist < best_dist:
                best_p, best_q, best_dist = p, q, dist
    return best_p, best_q, best_dist

print(f"  {'N_eff':>8} {'(1-r)/R2':>12} {'~p/q':>10} {'dist':>12} "
      f"{'(1-r)/R4':>12} {'~p/q':>10} {'dist':>12}")
print(f"  {'-'*8} {'-'*12} {'-'*10} {'-'*12} {'-'*12} {'-'*10} {'-'*12}")

interesting_R2 = []
interesting_R4 = []

for N_eff, r_avg, omr, omr_R2, omr_R4 in scan_results:
    p2, q2, d2 = closest_fraction(omr_R2, 1000)
    p4, q4, d4 = closest_fraction(omr_R4, 1000)

    flag2 = " <--" if d2 < 1e-4 and q2 <= 100 else ""
    flag4 = " <--" if d4 < 1e-4 and q4 <= 100 else ""

    if d2 < 1e-3 and q2 <= 100:
        interesting_R2.append((N_eff, p2, q2, d2))
    if d4 < 1e-3 and q4 <= 100:
        interesting_R4.append((N_eff, p4, q4, d4))

    print(f"  {N_eff:>8} {mp.nstr(omr_R2, 8):>12} {p2}/{q2:>6} "
          f"{d2:>12.2e} {mp.nstr(omr_R4, 8):>12} {p4}/{q4:>6} "
          f"{d4:>12.2e}{flag2}{flag4}")

print()
if interesting_R2:
    print("  INTERESTING R2 HITS:")
    for N, p, q, d in interesting_R2:
        print(f"    N={N}: (1-r)/R2 ~ {p}/{q} (dist {d:.2e})")
        # What this means physically
        print(f"      → 1-r = ({p}/{q}) * R2 = ({p}/{q}) * pi/4")
        print(f"      → r = 1 - {p}*pi/(4*{q})")
else:
    print("  No R2 rational hits at q <= 100, dist < 10^-3")

print()
if interesting_R4:
    print("  INTERESTING R4 HITS:")
    for N, p, q, d in interesting_R4:
        print(f"    N={N}: (1-r)/R4 ~ {p}/{q} (dist {d:.2e})")
        print(f"      → 1-r = ({p}/{q}) * R4 = ({p}/{q}) * pi^2/32")
else:
    print("  No R4 rational hits at q <= 100, dist < 10^-3")

print()

# ================================================================
# SECTION 6: THE VP STEP SIZE CONNECTION
# ================================================================

print("SECTION 6: IS THE PER-TRANSIT CORRECTION RELATED TO VP STEP?")
print("-" * 78)
print()

# The VP step size is 1/(3*pi) = 1/(12*R2) per unit charge-squared
# per flavor. If the soliton boundary correction is the SAME mechanism
# as VP running, then:
#   1-r = alpha * Q^2 * 1/(12*R2) * (geometric factor)
# where alpha is the EM coupling, Q is an effective charge, and
# the geometric factor depends on the boundary geometry.

vp_step_mpf = f2m(vp_step)  # 1/(3*pi) ~ 0.1061

print(f"  VP step size = 1/(3*pi) = {mp.nstr(vp_step_mpf, 10)}")
print(f"  alpha_em     = {mp.nstr(alpha_em_mpf, 10)}")
print(f"  alpha * VP_step = {mp.nstr(alpha_em_mpf * vp_step_mpf, 10)}")
print()

# For each N_eff, check if (1-r) = alpha_em * vp_step * k for integer k
print(f"  Test: (1-r) / (alpha_em / (3*pi)) = k ?")
print()

base_unit = alpha_em_mpf * vp_step_mpf  # alpha/(3*pi) ~ 7.74e-4

print(f"  base_unit = alpha/(3*pi) = {mp.nstr(base_unit, 8)}")
print()
print(f"  {'N_eff':>8} {'(1-r)/base':>14} {'nearest k':>10} {'residual':>12}")
print(f"  {'-'*8} {'-'*14} {'-'*10} {'-'*12}")

for N_eff, r_avg, omr, omr_R2, omr_R4 in scan_results:
    ratio_to_base = float(omr) / float(base_unit)
    k_near = round(ratio_to_base)
    residual = abs(ratio_to_base - k_near)

    flag = " <--" if residual < 0.1 and k_near > 0 else ""
    print(f"  {N_eff:>8} {ratio_to_base:>14.6f} {k_near:>10} "
          f"{residual:>12.6f}{flag}")

print()

# ================================================================
# SECTION 7: DARK MATTER AS TOROIDAL CORRECTION
# ================================================================

print("SECTION 7: DARK MATTER FRACTION FROM TOROIDAL CORRECTION")
print("-" * 78)
print()
print("  Hypothesis: the 'dark matter fraction' is the ratio of")
print("  toroidal (R4) boundary correction energy to visible mass.")
print()
print("  If the galactic disk torus has poloidal circulation with")
print("  kinetic energy E_circ, and the boundary amplification is")
print("  A = (some R4-based rational), then:")
print("    M_dark / M_visible = A * E_circ / (M_visible * c^2)")
print()

# Test: can R4-based rationals produce the observed DM fractions?
# DM/baryon ~ 5.32 cosmologically, ~5-6 in clusters

print(f"  Target: DM/baryon = {mp.nstr(DM_to_baryon, 4)}")
print()
print(f"  Test R4 multiples:")
print(f"    1/R4            = {mp.nstr(1/R4_mpf, 6)}")
print(f"    pi^2/(6*R4)     = {mp.nstr(f2m(pi2_f)/(6*R4_mpf), 6)}")
print(f"    2/R4            = {mp.nstr(2/R4_mpf, 6)}")
print()

# Scan: DM_ratio = n * R4 * m / d for small n, m, d
print(f"  Scan: DM/baryon = (p/q) * R4^a * R2^b")
print()

hits_dm = []
for p in range(1, 20):
    for q in range(1, 20):
        # Try: DM/baryon = (p/q) * R4
        val = (p / q) * R4_mpf
        if abs(float(val) - float(DM_to_baryon)) < 0.05:
            hits_dm.append((f"({p}/{q})*R4", val, abs(float(val) - float(DM_to_baryon))))

        # Try: DM/baryon = (p/q) * R2
        val2 = (p / q) * R2_mpf
        if abs(float(val2) - float(DM_to_baryon)) < 0.05:
            hits_dm.append((f"({p}/{q})*R2", val2, abs(float(val2) - float(DM_to_baryon))))

        # Try: DM/baryon = (p/q) * R2 * R4
        val3 = (p / q) * R2_mpf * R4_mpf
        if abs(float(val3) - float(DM_to_baryon)) < 0.05:
            hits_dm.append((f"({p}/{q})*R2*R4", val3, abs(float(val3) - float(DM_to_baryon))))

        # Try: DM/baryon = (p/q) * pi
        val4 = (p / q) * float(mpi)
        if abs(val4 - float(DM_to_baryon)) < 0.05:
            hits_dm.append((f"({p}/{q})*pi", mpf(val4), abs(val4 - float(DM_to_baryon))))

        # Try: DM/baryon = (p/q) alone
        val5 = p / q
        if abs(val5 - float(DM_to_baryon)) < 0.02:
            hits_dm.append((f"{p}/{q}", mpf(val5), abs(val5 - float(DM_to_baryon))))

# Sort by distance
hits_dm.sort(key=lambda x: x[2])

if hits_dm:
    print(f"  {'Expression':>20} {'Value':>12} {'Distance':>12}")
    print(f"  {'-'*20} {'-'*12} {'-'*12}")
    for expr, val, dist in hits_dm[:15]:
        flag = " <--" if dist < 0.01 else ""
        print(f"  {expr:>20} {mp.nstr(val, 6):>12} {dist:>12.6f}{flag}")
else:
    print("  No hits found")

print()

# ================================================================
# SECTION 8: THE COSMOLOGICAL CONSTANT SCALE
# ================================================================

print("SECTION 8: COSMOLOGICAL CONSTANT FROM BOUNDARY RUNNING")
print("-" * 78)
print()
print("  The cosmological constant Lambda ~ 10^-122 in Planck units.")
print("  Test: can this arise from alpha^N for some N?")
print()

# alpha_em^N ~ 10^-122 when N * log10(alpha_em) = -122
# log10(alpha_em) = log10(1/137.036) = -2.137
# N = 122 / 2.137 ~ 57

log10_alpha = mlog(alpha_em_mpf, 10)
N_for_lambda = mpf(-122) / log10_alpha

print(f"  log10(alpha_em) = {mp.nstr(log10_alpha, 8)}")
print(f"  N for alpha^N = 10^-122: N = {mp.nstr(N_for_lambda, 6)}")
print()

# Check nearby integers
for N_test in [56, 57, 58]:
    val = alpha_em_mpf ** N_test
    log_val = mlog(val, 10)
    print(f"  alpha^{N_test} = 10^{mp.nstr(log_val, 6)} "
          f"(target: 10^-122, miss: {mp.nstr(log_val + 122, 4)})")

print()

# Also test: Lambda ~ (alpha / (4*pi))^N  (loop suppression factor)
loop_factor = alpha_em_mpf / (4 * mpi)
log10_loop = mlog(loop_factor, 10)
N_loop = mpf(-122) / log10_loop

print(f"  Loop factor alpha/(4*pi) = {mp.nstr(loop_factor, 8)}")
print(f"  log10(loop factor) = {mp.nstr(log10_loop, 6)}")
print(f"  N for (alpha/4pi)^N = 10^-122: N = {mp.nstr(N_loop, 6)}")
print()

for N_test in [32, 33, 34]:
    val = loop_factor ** N_test
    log_val = mlog(val, 10)
    print(f"  (alpha/4pi)^{N_test} = 10^{mp.nstr(log_val, 6)} "
          f"(target: 10^-122, miss: {mp.nstr(log_val + 122, 4)})")

print()

# Test: VP step size to the power of N
print(f"  VP-step-based: (1/(3*pi))^N = (alpha_em * VP_step)^N ?")
for N_test in [28, 29, 30]:
    val = base_unit ** N_test
    if val > 0:
        log_val = mlog(val, 10)
        print(f"  (alpha/(3pi))^{N_test} = 10^{mp.nstr(log_val, 5)}")

print()

# ================================================================
# SECTION 9: THE GEOMETRY-DEPENDENT PREDICTION TABLE
# ================================================================

print("SECTION 9: PREDICTIONS FROM DIFFERENT BOUNDARY GEOMETRIES")
print("-" * 78)
print()
print("  For each boundary geometry, compute what the cumulative")
print("  correction predicts at various distances.")
print()

# Define canonical boundary types
boundary_types = [
    ("Sphere (R2)", R2_mpf, "R2-based, direction-independent"),
    ("Torus through hole (R4)", R4_mpf, "R4-based, minimum path"),
    ("Torus around ring (R4*2pi)", R4_mpf * 2 * mpi, "R4-based, maximum path"),
    ("Mixed (R2*R4)", R2_mpf * R4_mpf, "product of both"),
    ("VP-like (alpha/(3pi))", base_unit, "same mechanism as VP running"),
]

# For each type, use N_eff=100 (approximate local-to-CMB in sparse direction)
N_eff_test = 100

print(f"  N_eff = {N_eff_test} (approximate boundary count, sparse direction)")
print()
print(f"  {'Boundary type':>30} {'eps unit':>14} {'r = 1-eps':>14} "
      f"{'r^100':>14} {'H0 pred':>10}")
print(f"  {'-'*30} {'-'*14} {'-'*14} {'-'*14} {'-'*10}")

for name, eps_unit, desc in boundary_types:
    # Compute what epsilon gives the right H0 ratio
    # r^100 = H0_CMB/H0_local, so r = (H0_CMB/H0_local)^(1/100)
    r_needed = ratio_target ** (mpf(1) / N_eff_test)
    eps_needed = (1 - r_needed) / eps_unit

    # Now use this epsilon to predict H0 at various N
    r_this = 1 - eps_needed * eps_unit  # should equal r_needed
    r_100 = r_this ** N_eff_test
    H0_pred = H0_local * float(r_100)

    print(f"  {name:>30} {mp.nstr(eps_unit, 8):>14} {mp.nstr(r_this, 10):>14} "
          f"{mp.nstr(r_100, 8):>14} {H0_pred:>10.2f}")
    print(f"  {'':>30} eps = {mp.nstr(eps_needed, 6)} {'':>14} {desc}")
    print()

# ================================================================
# SECTION 10: THE POSITION-IN-TORUS SCAN
# ================================================================

print("SECTION 10: OBSERVER POSITION IN THE GALACTIC TORUS")
print("-" * 78)
print()
print("  The Sun is at R_sun ~ 8 kpc from the galactic center.")
print("  The disk scale height ~ 300 pc. The disk radius ~ 15 kpc.")
print("  Our position in the torus: R_major ~ 8 kpc, z ~ 25 pc above midplane.")
print()

R_disk = mpf('15')    # kpc, approximate disk radius
R_sun  = mpf('8')     # kpc, Sun's distance from center
z_sun  = mpf('0.025') # kpc, Sun's height above midplane
h_disk = mpf('0.3')   # kpc, disk scale height

# The torus parameters
R_major = R_disk / 2    # major radius of the torus approximation
r_minor = h_disk        # minor radius (disk thickness)

# Our fractional position
frac_radial = R_sun / R_disk  # 0.533
frac_vertical = z_sun / h_disk  # 0.083

print(f"  Disk radius:     {R_disk} kpc")
print(f"  Sun radius:      {R_sun} kpc")
print(f"  Sun height:      {z_sun} kpc")
print(f"  Disk height:     {h_disk} kpc")
print(f"  Radial position: {mp.nstr(frac_radial, 4)} of disk radius")
print(f"  Vertical pos:    {mp.nstr(frac_vertical, 4)} of disk height")
print()

# For different viewing angles from our position
print("  Viewing directions and boundary count estimates:")
print()

directions = [
    ("Galactic pole (up)", 0, "Through disk once, then halo once", 2),
    ("Galactic pole (down)", 180, "Through disk once, then halo once", 2),
    ("Galactic center", 90, "Through dense disk, bulge, far disk", 5),
    ("Galactic anticenter", 270, "Through sparse outer disk", 3),
    ("In-plane tangent", 90, "Along spiral arm, many crossings", 10),
    ("Toward Virgo", 45, "Through halo, local group, Virgo", 20),
    ("Toward CMB cold spot", 60, "Through halo + void?", 5),
]

# Use the N_eff=100 r_avg from the scan (for demonstration)
r_avg_100 = ratio_target ** (mpf(1) / 100)

print(f"  {'Direction':>25} {'Galactic N':>12} {'r^N':>12} {'Apparent H0':>12}")
print(f"  {'-'*25} {'-'*12} {'-'*12} {'-'*12}")

for name, angle, desc, N_gal in directions:
    # The galactic correction is just the first few boundaries
    # The cosmological correction is from all boundaries to CMB
    r_gal = r_avg_100 ** N_gal
    H0_apparent = float(H0_local) * float(r_gal)
    print(f"  {name:>25} {N_gal:>12} {mp.nstr(r_gal, 8):>12} "
          f"{H0_apparent:>12.2f}")
    print(f"  {'':>25} {desc}")

print()
print("  NOTE: These are schematic. Real N depends on galaxy survey data.")
print("  The directional variation is the TESTABLE PREDICTION.")
print()

# ================================================================
# SECTION 11: SUMMARY AND ASSESSMENT
# ================================================================

print("=" * 78)
print("SECTION 11: SUMMARY")
print("=" * 78)
print()

print("  WHAT WE TESTED:")
print("  - Per-boundary correction r to explain H0 tension")
print("  - Rational structure of (1-r) in R2 and R4 units")
print("  - VP step size as the correction mechanism")
print("  - Dark matter ratio from R2/R4 multiples")
print("  - Cosmological constant from alpha^N")
print("  - Directional H0 from observer position in torus")
print()

print("  KEY NUMBERS:")
print(f"    For N_eff=100: r = {mp.nstr(r_avg_100, 10)}, "
      f"1-r = {mp.nstr(1-r_avg_100, 6)}")
print(f"    (1-r)/R2 = {mp.nstr((1-r_avg_100)/R2_mpf, 6)}")
print(f"    (1-r)/R4 = {mp.nstr((1-r_avg_100)/R4_mpf, 6)}")
print(f"    (1-r)/(alpha/(3pi)) = {mp.nstr((1-r_avg_100)/base_unit, 6)}")
print()

print("  ASSESSMENT:")
print("    The scan establishes the PARAMETER SPACE.")
print("    For any N_eff in [10, 10000], there exists an r that")
print("    reproduces the H0 tension. This is by construction.")
print()
print("    The QUESTION is whether r has rational structure in R2/R4.")
print("    Check the output above for <-- markers.")
print()
print("    The dark matter and Lambda scans test whether the SAME")
print("    framework (R2/R4 rationals) produces other GR observables.")
print()
print("    NULL RESULT = no rational structure found = framework does")
print("    not connect QED to GR through simple boundary corrections.")
print("    This constrains but does not kill the soliton picture")
print("    (the corrections may be more complex than p/q * R_n).")
print()

print("  MATH GATE STATUS: THIS SCRIPT OPENS IT.")
print("  The numbers are now computed. Check for patterns.")
print()
print("=" * 78)
print("QED PREDICTS GR: SCAN COMPLETE")
print("=" * 78)
```

This script does the following:

**Section 1-2:** Loads all QED constants from phys24_lib (exact Fractions) and defines GR-side target observables (H₀, dark matter fraction, cosmological constant).

**Section 3-4:** For each hypothetical boundary count N (10 to 10,000), computes the per-transit correction r that would reproduce the H₀ tension. This is the calibration step.

**Section 5:** Tests whether (1−r)/R₂ or (1−r)/R₄ is close to a simple fraction p/q. This is the rational structure search — if the correction has clean geometric content, it should be a simple rational times R₂ or R₄.

**Section 6:** Tests whether the per-transit correction is related to the VP step size α/(3π). If the soliton boundary correction uses the same mechanism as vacuum polarization, the correction should be a small integer multiple of α/(3π).

**Section 7:** Scans whether the dark matter ratio (~5.32) can be expressed as a simple rational times R₂, R₄, π, or R₂×R₄.

**Section 8:** Tests whether the cosmological constant scale (10⁻¹²²) can arise from α^N or (α/4π)^N for some integer N. This tests whether the hierarchy between QED and cosmological scales is a power of the QED coupling.

**Section 9:** For each boundary geometry type (sphere, torus through hole, torus around ring, mixed), computes what ε would be needed and what H₀ it predicts.

**Section 10:** Uses our known position in the galactic disk (R_sun = 8 kpc, z = 25 pc above midplane) to predict directional H₀ variation from different viewing angles.

**Section 11:** Summary and assessment. If any `<--` markers appear in the scan, those are candidate rational structures worth investigating. If none appear, it's a null result that constrains the framework.

---

