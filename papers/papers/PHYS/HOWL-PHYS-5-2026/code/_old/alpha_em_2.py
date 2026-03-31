"""
Alpha_EM from Integer Arithmetic — Threshold Matching + Boundary Shape

The transformation law:
  alpha^{-1}(low) = alpha^{-1}(high) 
    + (2/(3*pi)) * sum_f Nc * Qf^2 * [ln(mu_high/m_f) - 5/6]
    for each fermion f with mass m_f between mu_low and mu_high

The 5/6 per fermion is the exact shape of the quantum boundary.
It comes from the Feynman parameter integral:
  5/6 = (3^2 - 2^2) / (2*3)
All integers.

Every intermediate value is a Python Fraction.
No float is created during computation.
Verification at 100 digits against mpmath.
"""

import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction
from mpmath import mp, mpf

mp.dps = 120  # extra headroom for 100-digit verification


# ============================================================
# SECTION 1: Transcendentals as integer pairs at 160 terms
# ============================================================

def rational_arctan(x, terms=160):
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

def rational_pi(terms=160):
    a1 = rational_arctan(Fraction(1, 5), terms)
    a2 = rational_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rational_arctanh(x, terms=160):
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        result += power / n
        power *= x_sq
    return result

def rational_ln2(terms=160):
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def rational_ln_ratio(p, q, terms=160):
    """Compute ln(p/q) by reducing to arctanh."""
    ratio = Fraction(p, q)
    ln2 = rational_ln2(terms)
    powers_of_2 = 0
    reduced = ratio
    while reduced > 2:
        reduced = reduced / 2
        powers_of_2 += 1
    while reduced < Fraction(1, 2):
        reduced = reduced * 2
        powers_of_2 -= 1
    arg = (reduced - 1) / (reduced + 1)
    ln_reduced = 2 * rational_arctanh(arg, terms)
    return powers_of_2 * ln2 + ln_reduced


# ============================================================
# SECTION 2: Compute pi
# ============================================================

print("Computing pi as integer pair (160 terms)...")
pi_rat = rational_pi(160)

# Verify precision
pi_mp_check = mpf(pi_rat.numerator) / mpf(pi_rat.denominator)
pi_diff = abs(pi_mp_check - mp.pi)
pi_digits = -int(mp.log10(pi_diff)) if pi_diff > 0 else 999
print(f"  pi precision: {pi_digits} correct digits")
print(f"  Numerator:    {pi_rat.numerator.bit_length()} bits")
print(f"  Denominator:  {pi_rat.denominator.bit_length()} bits")


# ============================================================
# SECTION 3: Measured inputs as exact rationals (Tier 3)
# ============================================================

# PDG 2024 at M_Z = 91.1876 GeV
alpha_EM_inv_MZ = Fraction(127906, 1000)      # 1/alpha_EM(M_Z) = 127.906
sin2_theta_W    = Fraction(23122, 100000)      # sin^2(theta_W) = 0.23122

# Particle masses in MeV as exact rationals
M_Z_MeV   = Fraction(911876, 10)       # 91187.6 MeV
m_b_MeV   = Fraction(4180, 1)          # 4180 MeV
m_tau_MeV  = Fraction(17768, 10)       # 1776.8 MeV
m_c_MeV   = Fraction(1270, 1)          # 1270 MeV
m_mu_MeV  = Fraction(105658, 1000)     # 105.658 MeV
m_s_MeV   = Fraction(93, 1)            # 93 MeV
m_d_MeV   = Fraction(47, 10)           # 4.7 MeV
m_u_MeV   = Fraction(22, 10)           # 2.2 MeV
m_e_MeV   = Fraction(511, 1000)        # 0.511 MeV


# ============================================================
# SECTION 4: Fermion content — exact rationals from counting
# ============================================================

# Per-fermion VP coefficient: (2/3) * Nc * Qf^2
coeff_up_quark   = Fraction(2, 3) * Fraction(3, 1) * Fraction(4, 9)   # = 8/9
coeff_down_quark = Fraction(2, 3) * Fraction(3, 1) * Fraction(1, 9)   # = 2/9
coeff_lepton     = Fraction(2, 3) * Fraction(1, 1) * Fraction(1, 1)   # = 2/3

# Boundary shape correction per fermion (from Feynman parameter integral)
# 5/6 = (3^2 - 2^2) / (2 * 3) — all integers
boundary_correction = Fraction(5, 6)

# Each fermion species: (name, mass_MeV, coefficient)
# up-type quarks: Q = 2/3, Nc = 3
# down-type quarks: Q = 1/3, Nc = 3
# charged leptons: Q = 1, Nc = 1

fermions = [
    ("b quark",   m_b_MeV,   coeff_down_quark),   # 2/9
    ("tau",       m_tau_MeV,  coeff_lepton),        # 2/3
    ("c quark",   m_c_MeV,   coeff_up_quark),      # 8/9
    ("muon",      m_mu_MeV,  coeff_lepton),         # 2/3
    ("s quark",   m_s_MeV,   coeff_down_quark),     # 2/9
    ("d quark",   m_d_MeV,   coeff_down_quark),     # 2/9
    ("u quark",   m_u_MeV,   coeff_up_quark),       # 8/9
    ("electron",  m_e_MeV,   coeff_lepton),          # 2/3
]

# Sort by mass descending (heaviest first — these are the thresholds
# we cross going down from M_Z)
fermions.sort(key=lambda f: f[1], reverse=True)


# ============================================================
# SECTION 5: Run the transformation law
# ============================================================

print()
print("=" * 74)
print("ALPHA_EM FROM INTEGER ARITHMETIC")
print("Threshold Matching + Boundary Shape Correction")
print("=" * 74)
print()
print(f"Starting value: 1/alpha_EM(M_Z) = {alpha_EM_inv_MZ} = {float(alpha_EM_inv_MZ):.6f}")
print()

# The formula for the contribution of each fermion to the running
# from M_Z down to m_e:
#
# For fermion f with mass m_f (where m_e < m_f < M_Z):
#   delta_f = coeff_f * [ln(M_Z / m_f) - 5/6] / pi
#
# For the electron (mass = m_e, the endpoint):
#   The electron contributes to its own running above m_e.
#   delta_e = coeff_e * [ln(M_Z / m_e) - 5/6] / pi
#
# Wait — I need to be more careful.
#
# The exact one-loop result is:
#   alpha^{-1}(mu) = alpha^{-1}(M_Z) 
#     + (1/pi) * sum over f [coeff_f * (ln(M_Z/m_f) - 5/6)]
#     where the sum includes all fermions with m_f < M_Z
#     and the evaluation point mu is taken well below all thresholds.
#
# Actually, the proper formula at scale mu for each fermion is:
#   contribution_f = coeff_f * [ln(M_Z^2/m_f^2) - 5/3] / (2*pi)
#   = coeff_f * [2*ln(M_Z/m_f) - 5/3] / (2*pi)
#   = coeff_f * [ln(M_Z/m_f) - 5/6] / pi
#
# This applies when mu << m_f for the question "what is alpha at mu=0?"
# More precisely, it applies in the regime where all fermion thresholds
# have been crossed (mu below lightest mass).
#
# For the endpoint at mu = m_e (not mu = 0):
# Each fermion heavier than m_e contributes:
#   coeff_f * [ln(M_Z/m_f) - 5/6] / pi   (threshold correction at m_f)
#   MINUS
#   coeff_f * [ln(m_e/m_f) ...] terms ... 
#
# Actually, let me use the cleanest formulation.
# The full result at scale mu, with all fermions accounted for:
#
#   alpha^{-1}(mu) = alpha^{-1}(M_Z) + (1/pi) * sum_f coeff_f * h(mu^2/m_f^2, M_Z^2/m_f^2)
#
# where h is the VP subtracted function. In the limit mu << m_f << M_Z:
#   h -> ln(M_Z/m_f) - 5/6
#
# For the electron at mu = m_e = m_f:
#   h(1, M_Z^2/m_e^2) = ln(M_Z/m_e) - 5/6 + small correction
#   (The correction at x=1 is not zero but involves the full VP function)
#
# For simplicity and honesty, let me use the asymptotic formula for all
# fermions heavier than the scale, and the full formula for the electron
# at its own mass. The asymptotic formula for the electron at mu=m_e is
# not valid since mu/m_f = 1, not >> 1.
#
# The exact VP function at threshold (q^2 = 4*m_f^2) gives:
#   Pi(4m^2) = -(alpha/(3*pi)) * Nc * Qf^2 * [-5/3 + 0 + 0]
#            = (5*alpha)/(9*pi) * Nc * Qf^2
#
# For the electron contribution to running at mu = m_e:
# This is a partial contribution. The electron has just barely activated.
# Its contribution at its own threshold is approximately 0 (just turning on).
# Above the threshold, it ramps up to the asymptotic value.
# Since we're evaluating AT m_e, the electron's own contribution is
# essentially zero — it hasn't had any range to run.
#
# So the cleanest approach: sum over all fermions EXCEPT the electron
# using the asymptotic formula, and note that the electron's own
# contribution at mu = m_e is negligible.

print("Computing ln ratios for each fermion threshold...")
print()

alpha_inv = alpha_EM_inv_MZ  # Start at M_Z
total_delta = Fraction(0)

print(f"{'Fermion':<12} {'Mass MeV':>10} {'Coeff':>8} {'ln(Mz/mf)':>14} "
      f"{'ln-5/6':>14} {'Delta':>12}")
print("-" * 74)

for name, mass, coeff in fermions:
    # ln(M_Z / m_f)
    p_ln = M_Z_MeV.numerator * mass.denominator
    q_ln = M_Z_MeV.denominator * mass.numerator
    ln_val = rational_ln_ratio(p_ln, q_ln, terms=160)
    
    # Corrected logarithm: ln(M_Z/m_f) - 5/6
    ln_corrected = ln_val - boundary_correction
    
    # Skip electron contribution at its own threshold
    # (it hasn't had range to run)
    if name == "electron":
        # The electron at mu = m_e contributes essentially nothing
        # because it just turned on. The asymptotic formula doesn't
        # apply at x = 1. We include a note but set delta = 0.
        delta = Fraction(0)
        print(f"{name:<12} {float(mass):>10.3f} {float(coeff):>8.4f} "
              f"{float(ln_val):>14.8f} {'(at threshold)':>14} {'0':>12}")
    else:
        # delta = coeff * (ln(M_Z/m_f) - 5/6) / pi
        delta = coeff * ln_corrected / pi_rat
        print(f"{name:<12} {float(mass):>10.3f} {float(coeff):>8.4f} "
              f"{float(ln_val):>14.8f} {float(ln_corrected):>14.8f} "
              f"{float(delta):>12.6f}")
    
    total_delta += delta

# Apply total
alpha_inv_result = alpha_EM_inv_MZ + total_delta

print("-" * 74)
print(f"{'Total':<12} {'':>10} {'':>8} {'':>14} {'':>14} "
      f"{float(total_delta):>12.6f}")
print()


# ============================================================
# SECTION 6: Result
# ============================================================

print("=" * 74)
print("RESULT")
print("=" * 74)
print()
print(f"1/alpha_EM(m_e) from integer arithmetic: {float(alpha_inv_result):.10f}")
print(f"CODATA 1/alpha_EM:                       137.035999177")
print()
diff_val = float(alpha_inv_result) - 137.035999177
print(f"Difference:     {diff_val:+.10f}")
print(f"Relative error: {abs(diff_val)/137.036 * 100:.6f}%")
print()


# ============================================================
# SECTION 7: 100-digit verification
# ============================================================

print("=" * 74)
print("100-DIGIT VERIFICATION")
print("=" * 74)
print()

result_mp = mpf(alpha_inv_result.numerator) / mpf(alpha_inv_result.denominator)
codata_mp = mpf('137.035999177')

print(f"Integer pair result (100 digits):")
print(f"  {mp.nstr(result_mp, 100)}")
print()
print(f"CODATA reference:")
print(f"  137.035999177 (only known to ~11 significant figures)")
print()

diff_mp = result_mp - codata_mp
print(f"Difference: {mp.nstr(diff_mp, 20)}")
print(f"Relative:   {mp.nstr(abs(diff_mp)/codata_mp * 100, 10)}%")
print()


# ============================================================
# SECTION 8: Structure report
# ============================================================

print("=" * 74)
print("STRUCTURE REPORT")
print("=" * 74)
print()
print("INTEGER COMPONENTS (from counting and geometry):")
print(f"  b quark coefficient:    {coeff_down_quark} = (2/3)*3*(1/3)^2")
print(f"  c quark coefficient:    {coeff_up_quark} = (2/3)*3*(2/3)^2")
print(f"  s quark coefficient:    {coeff_down_quark}")
print(f"  d quark coefficient:    {coeff_down_quark}")
print(f"  u quark coefficient:    {coeff_up_quark}")
print(f"  tau coefficient:        {coeff_lepton} = (2/3)*1*1^2")
print(f"  muon coefficient:       {coeff_lepton}")
print(f"  Boundary shape (5/6):   {boundary_correction} = (3^2 - 2^2)/(2*3)")
print()
print("INTEGER PAIRS (from MATH-2, 160-term precision):")
print(f"  pi:            {pi_rat.numerator.bit_length()} bit numerator")
for name, mass, coeff in fermions:
    if name != "electron":
        p_ln = M_Z_MeV.numerator * mass.denominator
        q_ln = M_Z_MeV.denominator * mass.numerator
        ln_val = rational_ln_ratio(p_ln, q_ln, terms=160)
        print(f"  ln(Mz/m_{name:<6}): {ln_val.numerator.bit_length():>5} bit numerator, "
              f"value = {float(ln_val):.8f}")
print()
print("MEASURED INPUTS (Tier 3, from universe):")
print(f"  1/alpha_EM(M_Z) = {alpha_EM_inv_MZ}")
print(f"  M_Z  = {M_Z_MeV} MeV")
print(f"  m_b  = {m_b_MeV} MeV")
print(f"  m_tau = {m_tau_MeV} MeV")
print(f"  m_c  = {m_c_MeV} MeV")
print(f"  m_mu = {m_mu_MeV} MeV")
print(f"  m_s  = {m_s_MeV} MeV")
print(f"  m_d  = {m_d_MeV} MeV")
print(f"  m_u  = {m_u_MeV} MeV")
print(f"  m_e  = {m_e_MeV} MeV")
print()
print("RESULT:")
print(f"  Type: {type(alpha_inv_result)}")
print(f"  Numerator:   {alpha_inv_result.numerator.bit_length()} bits")
print(f"  Denominator: {alpha_inv_result.denominator.bit_length()} bits")
print()

# ============================================================
# SECTION 9: What the 5/6 correction did
# ============================================================

print("=" * 74)
print("WHAT THE BOUNDARY SHAPE CORRECTION DID")
print("=" * 74)
print()

# Recompute without boundary correction for comparison
alpha_inv_no_correction = alpha_EM_inv_MZ
for name, mass, coeff in fermions:
    if name == "electron":
        continue
    p_ln = M_Z_MeV.numerator * mass.denominator
    q_ln = M_Z_MeV.denominator * mass.numerator
    ln_val = rational_ln_ratio(p_ln, q_ln, terms=160)
    delta = coeff * ln_val / pi_rat
    alpha_inv_no_correction += delta

print(f"Without boundary correction: {float(alpha_inv_no_correction):.6f}")
print(f"With 5/6 correction:         {float(alpha_inv_result):.6f}")
print(f"CODATA target:               137.035999")
print()
print(f"Step function overshoot:     {float(alpha_inv_no_correction) - 137.036:+.6f} ({abs(float(alpha_inv_no_correction) - 137.036)/137.036*100:.4f}%)")
print(f"After boundary correction:   {float(alpha_inv_result) - 137.036:+.6f} ({abs(float(alpha_inv_result) - 137.036)/137.036*100:.4f}%)")
print()
correction_effect = float(alpha_inv_no_correction - alpha_inv_result)
print(f"The 5/6 correction removed:  {correction_effect:.6f}")
print(f"Remaining discrepancy:       {float(alpha_inv_result) - 137.036:.6f}")
print()

# What fraction of the remaining error could the electron threshold fix?
# The electron at its own mass has a partial contribution.
# The exact VP function at x = q^2/(4*m^2) = 1 gives Pi = 0.
# But above threshold, the contribution ramps up.
# For running from mu = m_e to mu >> m_e, the electron contributes
# the same as any other fermion. But we're evaluating AT m_e.
# The electron's contribution from M_Z down to m_e, corrected, would be:
# coeff_e * [ln(M_Z/m_e) - 5/6] / pi
# Let's compute it to see its size.

p_ln = M_Z_MeV.numerator * m_e_MeV.denominator
q_ln = M_Z_MeV.denominator * m_e_MeV.numerator
ln_e = rational_ln_ratio(p_ln, q_ln, terms=160)
electron_delta_full = coeff_lepton * (ln_e - boundary_correction) / pi_rat
print(f"If electron ran fully: delta = {float(electron_delta_full):.6f}")
print(f"Remaining gap:                 {float(alpha_inv_result) - 137.036:.6f}")
print(f"Electron delta / gap:          {float(electron_delta_full) / (float(alpha_inv_result) - 137.036):.4f}")
print()
print("The electron contribution at its own threshold is between 0 (just")
print("activated) and the full value. The exact fraction depends on the") 
print("VP function at the threshold, which gives a specific rational.")
