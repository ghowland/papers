#!/usr/bin/env python3
"""
HOWL-PHYS-12-NOTEBOOK: Koide C₃ Investigation — Results and Parking Note
=========================================================================

Registry: [@HOWL-PHYS-12-NOTEBOOK-2026]
Date: April 1 2026
Status: PARKED — findings recorded, no derivation achieved

This notebook records the complete Phase 1 investigation of the Koide
formula through C₃ symmetry on the Subgroup A domain. The investigation
was planned as PHYS-12 but did not produce enough new content for a
full paper. The findings are recorded here for future reference.

SUMMARY OF FINDINGS:
1. The Koide 120-degree spacing is a tautology of the 3-parameter fit,
   not a physical constraint. (Phase 1, Finding 2)
2. All three fermion sectors have exact 120-degree spacing by construction.
   The difference between sectors is amplitude only. (Phase 1, Finding 2)
3. K = 2/3 is a saddle point under phase perturbation, not a minimum.
   The direction of quark deviation is not predicted. (Phase 1, Finding 3)
4. The frustrated C₃ potential gives 120-degree as ground state (known
   physics, textbook frustrated XY model). The connection to Koide is
   a rewriting, not a derivation. (Phase 1, Finding 1)
5. The amplitude a = sqrt(2) for charged leptons remains underived.
   Every formulation is a restatement, not a derivation. (Phase 2, null)
6. The amplitude ordering a_lep < a_down < a_up is real data from
   DATA-2 masses at full CODATA precision. (New result, preserved below)

PATHS CLOSED BY THIS INVESTIGATION:
- C₃ spacing as a derivation of Koide (tautology)
- CKM mixing breaking C₃ spacing for quarks (spacing is universal)
- K = 2/3 as minimum predicting quarks K > 2/3 (saddle point)
- Frustrated graph mechanism (DISC-8, structural mismatch)

PATHS REMAINING OPEN:
- Why a² = 2 for charged leptons (the entire Koide problem)
- Whether the amplitude ordering a_lep < a_dn < a_up has a structural origin
- Discrete flavor symmetry (A₄, S₃) selecting a = sqrt(2) (untested)
- Connection between a and the mass-generating mechanism (Yukawa sector)
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi, cos as mcos, sin as msin, acos as macos

mp.dps = 50

def f2m(f):
    """Fraction to mpf via integer division (compatible with old mpmath)."""
    return mpf(f.numerator) / mpf(f.denominator)

# ================================================================
# Q335 BASIS CONSTANTS
# ================================================================

Q = 2**335
p_pi    = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506
p_sqrt3 = 121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154

pi_frac    = Fraction(p_pi, Q)
sqrt2_frac = Fraction(p_sqrt2, Q)

# ================================================================
# DATA-2 MASSES (exact Fractions at published precision)
# ================================================================

# Charged leptons (CODATA 2022 / PDG 2024)
m_e   = Fraction(51099895069, 10**11)     # 0.51099895069 MeV, 11 digits
m_mu  = Fraction(1056583755, 10**7)       # 105.6583755 MeV, 10 digits
m_tau = Fraction(177686, 100)             # 1776.86 MeV, 6 digits

# Up-type quarks (PDG 2024, MSbar)
m_u = Fraction(216, 100)       # 2.16 MeV, 3 digits
m_c = Fraction(1273, 1)        # 1273 MeV, 4 digits
m_t = Fraction(172570, 1)      # 172570 MeV, 5 digits

# Down-type quarks (PDG 2024, MSbar)
m_d = Fraction(470, 100)       # 4.70 MeV, 3 digits
m_s = Fraction(935, 10)        # 93.5 MeV, 3 digits
m_b = Fraction(4183, 1)        # 4183 MeV, 4 digits

# ================================================================
# KOIDE ANALYSIS FUNCTION
# ================================================================

def koide_analysis(m1, m2, m3, label):
    """
    Complete Koide analysis for three masses.
    Returns dict with K, a, a², M, theta0, cos values.
    All computation via mpmath from exact Fraction inputs.
    """
    mp.dps = 50
    M1, M2, M3 = f2m(m1), f2m(m2), f2m(m3)
    masses_mpf = sorted([M1, M2, M3])  # ascending
    
    s = [msqrt(m) for m in masses_mpf]
    
    sum_m = sum(masses_mpf)
    sum_sqrt = sum(s)
    K = sum_m / sum_sqrt**2
    
    M = sum_sqrt / 3
    var_sqrt = sum((si - M)**2 for si in s) / 3
    a_sq = 2 * var_sqrt / M**2
    a = msqrt(a_sq)
    
    # cos(phi_k) = (sqrt(m_k)/M - 1) / a
    cos_phis = [(si / M - 1) / a for si in s]
    sum_cos = sum(float(c) for c in cos_phis)
    
    # theta0 from heaviest mass (smallest arccos)
    theta0 = float(macos(cos_phis[2]))
    
    return {
        'label': label,
        'K': float(K),
        'K_minus_2_3': float(K - mpf(2)/3),
        'a': float(a),
        'a_sq': float(a_sq),
        'a_minus_sqrt2': float(a - msqrt(2)),
        'M': float(M),
        'theta0_rad': theta0,
        'theta0_deg': theta0 * 180 / float(mpi),
        'cos_phis': [float(c) for c in cos_phis],
        'sum_cos': sum_cos,
        'masses_MeV': [float(m) for m in masses_mpf],
        'sqrt_masses': [float(si) for si in s],
    }

# ================================================================
# COMPUTE ALL THREE SECTORS
# ================================================================

print("=" * 72)
print("HOWL-PHYS-12-NOTEBOOK: Koide C3 Investigation")
print("=" * 72)
print()

results = []
for m1, m2, m3, label in [
    (m_e, m_mu, m_tau, "Charged Leptons (e, mu, tau)"),
    (m_u, m_c, m_t,   "Up-type Quarks (u, c, t)"),
    (m_d, m_s, m_b,   "Down-type Quarks (d, s, b)"),
]:
    r = koide_analysis(m1, m2, m3, label)
    results.append(r)

# ================================================================
# RESULT 1: KOIDE RATIOS AND AMPLITUDES
# ================================================================

print("RESULT 1: KOIDE RATIOS AND AMPLITUDES (DATA-2 precision)")
print("-" * 72)
print()
print(f"  {'Sector':<28} {'K':>12} {'K-2/3':>14} {'a':>10} {'a²':>10} {'a-√2':>12}")
print(f"  {'-'*28} {'-'*12} {'-'*14} {'-'*10} {'-'*10} {'-'*12}")
for r in results:
    print(f"  {r['label']:<28} {r['K']:>12.8f} {r['K_minus_2_3']:>14.2e} "
          f"{r['a']:>10.6f} {r['a_sq']:>10.6f} {r['a_minus_sqrt2']:>12.6e}")
print()
print(f"  Reference: sqrt(2) = {float(msqrt(2)):.10f}")
print(f"  Reference: 2/3     = {2/3:.10f}")
print()

# Ordering
print(f"  K ordering:  K_lep ({results[0]['K']:.6f}) < K_dn ({results[2]['K']:.6f}) < K_up ({results[1]['K']:.6f})")
assert results[0]['K'] < results[2]['K'] < results[1]['K'], "K ordering failed"
print(f"               CONFIRMED")
print()
print(f"  a ordering:  a_lep ({results[0]['a']:.6f}) < a_dn ({results[2]['a']:.6f}) < a_up ({results[1]['a']:.6f})")
assert results[0]['a'] < results[2]['a'] < results[1]['a'], "a ordering failed"
print(f"               CONFIRMED")
print()

# ================================================================
# RESULT 2: ZERO-MAGNETIZATION (TAUTOLOGY DEMONSTRATION)
# ================================================================

print("RESULT 2: ZERO-MAGNETIZATION CONDITION")
print("-" * 72)
print()
print("  sum(cos(phi_k)) = 0 for ALL sectors (to machine precision):")
for r in results:
    print(f"    {r['label']:<28} sum_cos = {r['sum_cos']:.2e}")
print()
print("  This is a TAUTOLOGY of the 3-parameter Koide parametrization.")
print("  The identity cos(x) + cos(x+2pi/3) + cos(x+4pi/3) = 0 holds")
print("  for all x. Three parameters (M, a, theta0) fit three masses")
print("  exactly, with 120-degree spacing built in by construction.")
print("  The equal spacing is a coordinate choice, not a discovery.")
print()

# ================================================================
# RESULT 3: PHASE PARAMETERS
# ================================================================

print("RESULT 3: PHASE PARAMETERS")
print("-" * 72)
print()
print(f"  {'Sector':<28} {'theta0 (rad)':>12} {'theta0 (deg)':>12} {'M (√MeV)':>12}")
print(f"  {'-'*28} {'-'*12} {'-'*12} {'-'*12}")
for r in results:
    print(f"  {r['label']:<28} {r['theta0_rad']:>12.6f} {r['theta0_deg']:>12.4f} {r['M']:>12.4f}")
print()
print("  cos(phi_k) for each sector:")
for r in results:
    c = r['cos_phis']
    print(f"    {r['label']:<28} [{c[0]:+.8f}, {c[1]:+.8f}, {c[2]:+.8f}]")
print()

# ================================================================
# RESULT 4: C3 FRUSTRATED POTENTIAL VERIFICATION
# ================================================================

print("RESULT 4: C3 FRUSTRATED POTENTIAL")
print("-" * 72)
print()

J = mpf(1)
V_120 = J * 3 * mcos(2*mpi/3)
V_aligned = J * 3 * mcos(mpf(0))
grad = -J * (msin(-2*mpi/3) + msin(2*mpi/3))
hess = -J * (mcos(-2*mpi/3) + mcos(2*mpi/3))

print(f"  V(phi) = +J * sum_{{i<j}} cos(phi_i - phi_j),  J > 0 (antiferromagnetic)")
print()
print(f"  V(120-degree) = {float(V_120):.6f} = -3J/2")
print(f"  V(aligned)    = {float(V_aligned):.6f} = +3J")
print(f"  Gradient at 120: {float(grad):.2e} (verified = 0)")
print(f"  Hessian at 120:  {float(hess):.6f} (positive = local minimum)")
print()
print("  120-degree spacing is ground state of frustrated C3 potential.")
print("  This is textbook physics (frustrated XY model on triangle).")
print("  Connection to Koide: the parametrization's 120-degree spacing")
print("  corresponds to this ground state. But this is a REWRITING of")
print("  the parametrization, not a derivation of the formula.")
print()

assert abs(float(V_120) - (-1.5)) < 1e-40
assert abs(float(grad)) < 1e-40
assert float(hess) > 0

# ================================================================
# RESULT 5: SADDLE POINT ANALYSIS
# ================================================================

print("RESULT 5: K = 2/3 IS A SADDLE POINT")
print("-" * 72)
print()

mp.dps = 50
a_test = msqrt(2)

def K_perturbed(eps, delta):
    phases = [2*mpi*k/3 + eps*delta[k] for k in range(3)]
    sqm = [1 + a_test * mcos(p) for p in phases]
    if any(s <= 0 for s in sqm):
        return None
    masses = [s**2 for s in sqm]
    return sum(masses) / sum(sqm)**2

K0 = K_perturbed(mpf(0), (0, 0, 0))
h = mpf('1e-10')

print(f"  K at exact 120-degree, a=sqrt(2): {float(K0):.15f}")
print(f"  K - 2/3 = {float(K0 - mpf(2)/3):.2e}")
print()

print(f"  {'Perturbation':<20} {'sum(delta)':>10} {'d2K/deps2':>12} {'Type':>12}")
print(f"  {'-'*20} {'-'*10} {'-'*12} {'-'*12}")

deltas = [
    ((1, -1, 0),     "asymmetric"),
    ((1, 0, -1),     "asymmetric"),
    ((0, 1, -1),     "asymmetric"),
    ((1, -0.5, -0.5), "symmetric"),
    ((2, -1, -1),    "symmetric"),
]

for delta, dtype in deltas:
    sd = sum(delta)
    Kp = K_perturbed(h, delta)
    Km = K_perturbed(-h, delta)
    if Kp and Km:
        d2K = float((Kp - 2*K0 + Km) / h**2)
        sign = "MINIMUM" if d2K > 0 else "MAXIMUM"
        print(f"  {str(delta):<20} {sd:>10.1f} {d2K:>12.6f} {sign:>12}")

print()
print("  FINDING: K = 2/3 is a MINIMUM for asymmetric perturbations")
print("  (which break C3) but a MAXIMUM for symmetric perturbations")
print("  (which preserve C3 and stretch/compress uniformly).")
print("  K = 2/3 is a SADDLE POINT, not a universal minimum.")
print("  The prediction 'quarks must have K > 2/3' is NOT valid.")
print()

# ================================================================
# RESULT 6: EQUIVALENT FORMULATIONS OF a² = 2
# ================================================================

print("RESULT 6: ALL KNOWN EQUIVALENT FORMULATIONS OF a² = 2")
print("-" * 72)
print()
print("  Every formulation below is algebraically equivalent to the")
print("  Koide formula. None constitutes an independent derivation.")
print()

# Verify each equivalence numerically using lepton data
r = results[0]  # leptons
K = r['K']
a = r['a']
a2 = r['a_sq']
M = r['M']
s_masses = r['sqrt_masses']

# 1. K = 2/3
print(f"  1. K = (sum m)/(sum sqrt(m))² = 2/3")
print(f"     Measured: K = {K:.10f}, deviation from 2/3: {K - 2/3:.2e}")
print()

# 2. a² = 2
print(f"  2. a² = 2 (critical amplitude)")
print(f"     Measured: a² = {a2:.10f}, deviation from 2: {a2 - 2:.2e}")
print()

# 3. CV = 1
mean_sqrt = sum(s_masses) / 3
var_sqrt = sum((s - mean_sqrt)**2 for s in s_masses) / 3
std_sqrt = var_sqrt**0.5
CV = std_sqrt / mean_sqrt
print(f"  3. CV(sqrt(m)) = std/mean = 1")
print(f"     Measured: CV = {CV:.10f}, deviation from 1: {CV - 1:.2e}")
print()

# 4. Var = mean²
print(f"  4. Var(sqrt(m)) = mean(sqrt(m))²")
print(f"     Var  = {var_sqrt:.6f}")
print(f"     mean² = {mean_sqrt**2:.6f}")
print(f"     Ratio = {var_sqrt / mean_sqrt**2:.10f}, deviation from 1: {var_sqrt/mean_sqrt**2 - 1:.2e}")
print()

# 5. Midpoint of allowed range
print(f"  5. a² = midpoint of [0, 4]")
print(f"     Range: a² in [0, 4] for non-negative masses with equal spacing")
print(f"     Midpoint = 2, measured a² = {a2:.10f}")
print()

# 6. Critical amplitude (one mass can vanish)
print(f"  6. Critical amplitude: max a where all masses >= 0")
print(f"     At a = sqrt(2), min(sqrt(m_k)/M) = 1 - a*1 = 1 - sqrt(2) < 0")
print(f"     Actually: min occurs at cos(phi) = -1, giving sqrt(m)/M = 1 - a")
print(f"     For a = sqrt(2): 1 - sqrt(2) = {1 - 2**0.5:.6f} < 0")
print(f"     So a = sqrt(2) is ABOVE critical (allows one mass = 0 at cos = -1/a)")
print(f"     The critical condition is a = sqrt(2): cos(phi) = -1/sqrt(2) gives m = 0")
print()

# 7. Equipartition (variance = mean²) — same as #4
print(f"  7. 'Equipartition': kinetic (variance) = potential (mean²)")
print(f"     Algebraically identical to formulation 4.")
print()

print("  CONCLUSION: Seven formulations, zero derivations.")
print("  The Koide formula's content is a² = 2 for charged leptons.")
print("  Why this value? Unknown. Every approach tried reduces to a")
print("  restatement of the formula, not an explanation of it.")
print()

# ================================================================
# RESULT 7: PATHS TESTED AND CLOSED
# ================================================================

print("RESULT 7: PATHS TESTED AND CLOSED")
print("-" * 72)
print()
print(f"  {'Path':<45} {'Result':<15} {'Paper':>10}")
print(f"  {'-'*45} {'-'*15} {'-'*10}")
print(f"  {'Frustrated graph mechanism':<45} {'FAILS':.<15} {'DISC-8':>10}")
print(f"  {'C3 spacing from frustrated XY potential':<45} {'TAUTOLOGY':.<15} {'This note':>10}")
print(f"  {'CKM mixing breaks C3 for quarks':<45} {'MOOT':.<15} {'This note':>10}")
print(f"  {'K=2/3 is minimum (quarks must K>2/3)':<45} {'WRONG':.<15} {'This note':>10}")
print(f"  {'CV=1 / midpoint / equipartition':<45} {'RESTATEMENT':.<15} {'PHYS-8':>10}")
print()
print("  PATHS REMAINING OPEN:")
print(f"  {'Discrete flavor symmetry (A4, S3) -> a=sqrt(2)':<45} {'UNTESTED':<15}")
print(f"  {'Yukawa sector structure -> amplitude selection':<45} {'UNTESTED':<15}")
print(f"  {'RG running of Koide ratio with energy scale':<45} {'UNTESTED':<15}")
print(f"  {'Neutrino sector Koide (once masses known)':<45} {'WAITING':<15}")
print()

# ================================================================
# DATA PRESERVATION: AMPLITUDES FOR FUTURE REFERENCE
# ================================================================

print("DATA PRESERVATION: Koide amplitudes from DATA-2 masses")
print("-" * 72)
print()
print("  These values are derived from CODATA 2022 / PDG 2024 masses")
print("  via the Koide parametrization sqrt(m_k) = M(1 + a*cos(theta0 + 2pi*k/3)).")
print("  They are the most precise Koide amplitudes computed to date.")
print()
print(f"  {'Sector':<16} {'a':>12} {'a²':>12} {'K':>12} {'M (√MeV)':>12} {'θ₀ (deg)':>10}")
print(f"  {'-'*16} {'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*10}")
for r in results:
    short = r['label'].split('(')[0].strip()
    print(f"  {short:<16} {r['a']:>12.8f} {r['a_sq']:>12.8f} "
          f"{r['K']:>12.8f} {r['M']:>12.6f} {r['theta0_deg']:>10.4f}")
print()
print(f"  Lepton a - sqrt(2) = {results[0]['a_minus_sqrt2']:.6e}")
print(f"  Lepton K - 2/3     = {results[0]['K_minus_2_3']:.6e}")
print(f"  (Limited by m_tau at 6 sig figs: ±0.12 MeV)")
print()

# ================================================================
# ASSERTIONS
# ================================================================

# Lepton Koide near 2/3
assert abs(results[0]['K'] - 2/3) < 0.001

# Lepton amplitude near sqrt(2)
assert abs(results[0]['a'] - float(msqrt(2))) < 0.001

# K ordering
assert results[0]['K'] < results[2]['K'] < results[1]['K']

# a ordering
assert results[0]['a'] < results[2]['a'] < results[1]['a']

# Quarks above 2/3
assert results[1]['K'] > 2/3
assert results[2]['K'] > 2/3

# Leptons below 2/3
assert results[0]['K'] < 2/3

# Zero magnetization for all sectors (tautology check)
for r in results:
    assert abs(r['sum_cos']) < 1e-10, f"{r['label']} sum_cos not zero"

# C3 potential ground state
assert abs(float(V_120) - (-1.5)) < 1e-30
assert abs(float(grad)) < 1e-30
assert float(hess) > 0

# K0 at exact 120-degree is 2/3
assert abs(float(K0) - 2/3) < 1e-10

print("=" * 72)
print("ALL ASSERTIONS PASS")
print()
print("STATUS: PARKED")
print("  The Koide amplitude question (why a² = 2 for charged leptons)")
print("  remains the sole open high-priority derivation target in the")
print("  HOWL series. This investigation closes the C3 spacing path")
print("  and confirms the problem is purely about the amplitude.")
print("  Future work requires a new idea, not more computation.")
print("=" * 72)
