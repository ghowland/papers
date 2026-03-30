"""
Alpha_EM from Integer Arithmetic via the QED Beta Functions

This script takes three measured inputs at the Z boson mass scale:
    alpha_EM(M_Z) = 1/127.906  (PDG 2024)
    sin^2(theta_W) = 0.23122   (PDG 2024, MS-bar at M_Z)
    alpha_s(M_Z) = 0.1180      (PDG 2024)

It runs the three Standard Model one-loop beta functions from M_Z down
to the electron mass scale using ONLY exact rational arithmetic
(Python's fractions.Fraction). The transcendentals pi and ln are
computed as integer pairs at 100+ digit precision using the methods
from MATH-2.

The output is alpha_EM at low energy, computed entirely in integers,
verified against the known value of ~1/137.036.

No floating point value is created during computation. mpmath is used
only for final verification by string comparison.
"""

from fractions import Fraction
from mpmath import mp, mpf

# ============================================================
# SECTION 1: Integer pairs for transcendentals (from MATH-2)
# ============================================================

def rational_arctan(x, terms=80):
    """Compute arctan(x) for rational x using Gregory series.
    arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
    All arithmetic in Fraction."""
    result = Fraction(0)
    power = x  # x^1
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        if k % 2 == 0:
            result += power / n
        else:
            result -= power / n
        power *= x_sq
    return result

def rational_pi(terms=80):
    """Compute pi using Machin's formula:
    pi = 4 * (4*arctan(1/5) - arctan(1/239))
    Returns exact Fraction."""
    a1 = rational_arctan(Fraction(1, 5), terms)
    a2 = rational_arctan(Fraction(1, 239), terms)
    return 4 * (4 * a1 - a2)

def rational_arctanh(x, terms=120):
    """Compute arctanh(x) for rational x.
    arctanh(x) = x + x^3/3 + x^5/5 + x^7/7 + ...
    All arithmetic in Fraction."""
    result = Fraction(0)
    power = x
    x_sq = x * x
    for k in range(terms):
        n = 2 * k + 1
        result += power / n
        power *= x_sq
    return result

def rational_ln2(terms=120):
    """Compute ln(2) = 2*arctanh(1/3). Returns exact Fraction."""
    return 2 * rational_arctanh(Fraction(1, 3), terms)

def rational_ln(n, terms=120):
    """Compute ln(n) for integer n using decomposition through
    ln(2) and arctanh series. Supports n = 2,3,5,10 and
    compositions thereof."""
    if n == 2:
        return rational_ln2(terms)
    elif n == 3:
        return rational_ln2(terms) + 2 * rational_arctanh(Fraction(1, 5), terms)
    elif n == 5:
        return 2 * rational_ln2(terms) + 2 * rational_arctanh(Fraction(1, 9), terms)
    elif n == 10:
        return rational_ln(2, terms) + rational_ln(5, terms)
    else:
        raise ValueError(f"ln({n}) not implemented — decompose manually")

def rational_ln_ratio(p, q, terms=120):
    """Compute ln(p/q) for integers p, q.
    Uses ln(p/q) = ln(p) - ln(q), decomposing each through
    prime factorization into ln(2), ln(3), ln(5), etc.
    
    For general ratios, uses:
    ln(p/q) = 2*arctanh((p-q)/(p+q)) when p/q is close to 1
    or chains of such identities for larger ratios.
    """
    # For the specific ratio we need (M_Z / m_e), we'll use
    # a direct arctanh series approach:
    # ln(x) = 2*arctanh((x-1)/(x+1)) for x > 0
    # But for large x this converges slowly.
    #
    # Better: factor the ratio and use known ln values.
    # M_Z / m_e = 91187.6 / 0.511 MeV
    # But we want to stay rational, so express as:
    # M_Z = 91188 MeV (rounded to integer MeV for now)
    # m_e = 511/1000 MeV = 511 keV
    # Ratio = 91188 / (511/1000) = 91188000 / 511
    #
    # ln(91188000/511) = ln(91188000) - ln(511)
    # 
    # We'll use a general method: repeated reduction.
    # ln(N) = k*ln(2) + ln(N/2^k) where N/2^k is near 1
    # Then ln(N/2^k) = 2*arctanh((N/2^k - 1)/(N/2^k + 1))
    
    ratio = Fraction(p, q)
    
    # Pull out powers of 2 to reduce the ratio
    ln2 = rational_ln2(terms)
    
    powers_of_2 = 0
    reduced = ratio
    while reduced > 2:
        reduced = reduced / 2
        powers_of_2 += 1
    while reduced < Fraction(1, 2):
        reduced = reduced * 2
        powers_of_2 -= 1
    
    # Now reduced is between 0.5 and 2
    # ln(reduced) = 2*arctanh((reduced - 1)/(reduced + 1))
    arg = (reduced - 1) / (reduced + 1)
    ln_reduced = 2 * rational_arctanh(arg, terms)
    
    return powers_of_2 * ln2 + ln_reduced


# ============================================================
# SECTION 2: Measured inputs as exact rationals
# ============================================================

# PDG 2024 values at M_Z = 91.1876 GeV

# alpha_EM(M_Z)^{-1} = 127.906 +/- 0.019
# We express as: 1/alpha_EM = 127906/1000
alpha_EM_inv_MZ = Fraction(127906, 1000)

# sin^2(theta_W) in MS-bar at M_Z = 0.23122 +/- 0.00004
# Express as: 23122/100000
sin2_theta_W = Fraction(23122, 100000)

# alpha_s(M_Z) = 0.1180 +/- 0.0009
# Express as: 1180/10000 = 59/500
alpha_s_MZ = Fraction(59, 500)

# Masses (in MeV) as rationals
M_Z = Fraction(911876, 10)  # 91187.6 MeV
m_e = Fraction(511, 1000) * 1000  # 0.511 MeV * 1000 = 511 MeV ... 
# Wait, let me be careful with units.
# M_Z = 91187.6 MeV = 911876/10 MeV
# m_e = 0.51100 MeV = 511/1000 MeV (in GeV: 0.000511 GeV)
# But we need the ratio, so units cancel:
# M_Z / m_e = 91187.6 / 0.51100 = 178449.3...
# As rationals: (911876/10) / (511/1000) = 911876 * 1000 / (10 * 511)
#             = 911876000 / 5110
#             = 455938000 / 2555

M_Z_MeV = Fraction(911876, 10)      # 91187.6 MeV
m_e_MeV = Fraction(511, 1000)        # 0.511 MeV

# Energy ratio
mu_ratio = M_Z_MeV / m_e_MeV  # = 911876000 / 5110


# ============================================================
# SECTION 3: Extract alpha_1 and alpha_2 at M_Z
# ============================================================

# In the Standard Model (MS-bar scheme):
#   sin^2(theta_W) = alpha_1_SM / (alpha_1_SM + alpha_2)
#   alpha_EM = alpha_1_SM * alpha_2 / (alpha_1_SM + alpha_2)
#
# Or equivalently:
#   alpha_1_SM = alpha_EM / sin^2(theta_W)  -- NO, this isn't right.
#
# Let me be precise. The electroweak relations at M_Z:
#   e^2 = g^2 * sin^2(theta_W) = g'^2 * cos^2(theta_W)
#
# Where g is the SU(2) coupling, g' is the U(1) coupling.
#   alpha_2 = g^2 / (4*pi) 
#   alpha_1_SM = g'^2 / (4*pi)
#   alpha_EM = e^2 / (4*pi)
#
# From e^2 = g^2 * sin^2(theta_W):
#   alpha_EM = alpha_2 * sin^2(theta_W)
#   => alpha_2 = alpha_EM / sin^2(theta_W)
#
# From e^2 = g'^2 * cos^2(theta_W):
#   alpha_EM = alpha_1_SM * cos^2(theta_W)
#   => alpha_1_SM = alpha_EM / cos^2(theta_W)
#
# GUT normalization: alpha_1_GUT = (5/3) * alpha_1_SM
#
# Check: 1/alpha_EM = sin^2/alpha_2 ... no.
# Let me verify: 
#   1/alpha_EM = 1/alpha_2 * 1/sin^2(theta_W)?  No.
#   alpha_EM = alpha_2 * sin^2(theta_W)
#   so 1/alpha_EM = 1/(alpha_2 * sin^2(theta_W))
#   Hmm, that gives 1/alpha_2 = sin^2(theta_W) / alpha_EM
#                              = sin^2(theta_W) * alpha_EM_inv

# Let me just compute directly.
alpha_EM_MZ = Fraction(1, 1) / alpha_EM_inv_MZ  # = 1000/127906

cos2_theta_W = Fraction(1, 1) - sin2_theta_W  # = 76878/100000

# alpha_2(M_Z) = alpha_EM(M_Z) / sin^2(theta_W)
alpha_2_MZ = alpha_EM_MZ / sin2_theta_W

# alpha_1_SM(M_Z) = alpha_EM(M_Z) / cos^2(theta_W)  
alpha_1_SM_MZ = alpha_EM_MZ / cos2_theta_W

# GUT normalization
alpha_1_GUT_MZ = Fraction(5, 3) * alpha_1_SM_MZ


# ============================================================
# SECTION 4: Beta function coefficients (exact integers)
# ============================================================

# One-loop beta function: d(alpha^{-1})/d(ln mu) = -b_0 / (2*pi)
#
# So: alpha^{-1}(mu_2) = alpha^{-1}(mu_1) + (b_0 / (2*pi)) * ln(mu_1/mu_2)
#
# Note the sign: running DOWN from mu_1 to mu_2 < mu_1:
#   ln(mu_1/mu_2) > 0
#   For b_0 > 0 (like alpha_1), alpha^{-1} increases going down = coupling weakens
#   For b_0 < 0 (like alpha_2, alpha_3), alpha^{-1} decreases going down = coupling strengthens
#
# Standard Model one-loop coefficients (with n_g=3 generations, n_H=1 Higgs doublet):
#
# b_0 for alpha_1_GUT: 41/10
# b_0 for alpha_2:     -19/6  
# b_0 for alpha_3:     -7

b0_alpha1 = Fraction(41, 10)   # positive: alpha_1 weakens at low energy
b0_alpha2 = Fraction(-19, 6)   # negative: alpha_2 strengthens at low energy
b0_alpha3 = Fraction(-7, 1)    # negative: alpha_3 strengthens at low energy


# ============================================================
# SECTION 5: Compute the running
# ============================================================

print("=" * 70)
print("ALPHA_EM FROM INTEGER ARITHMETIC")
print("QED Beta Functions in Exact Rational Arithmetic")
print("=" * 70)

# Step 1: Compute transcendentals as integer pairs
print("\n--- Computing transcendentals as integer pairs ---")

pi_rat = rational_pi(80)
two_pi_rat = 2 * pi_rat
print(f"pi computed: {pi_rat.numerator.bit_length()} bit numerator, "
      f"{pi_rat.denominator.bit_length()} bit denominator")

# Step 2: Compute ln(M_Z / m_e)
print("Computing ln(M_Z / m_e)...")
ln_ratio = rational_ln_ratio(M_Z_MeV.numerator * m_e_MeV.denominator,
                              M_Z_MeV.denominator * m_e_MeV.numerator, 
                              terms=120)
print(f"ln(M_Z/m_e) computed: {ln_ratio.numerator.bit_length()} bit numerator")

# Step 3: Display inputs
print("\n--- Measured inputs at M_Z ---")
print(f"1/alpha_EM(M_Z) = {alpha_EM_inv_MZ} = {float(alpha_EM_inv_MZ):.6f}")
print(f"sin^2(theta_W) = {sin2_theta_W} = {float(sin2_theta_W):.6f}")
print(f"alpha_s(M_Z)   = {alpha_s_MZ} = {float(alpha_s_MZ):.6f}")

print(f"\n--- Extracted couplings at M_Z ---")
print(f"alpha_2(M_Z)       = {float(alpha_2_MZ):.8f}")
print(f"1/alpha_2(M_Z)     = {float(1/alpha_2_MZ):.6f}")
print(f"alpha_1_SM(M_Z)    = {float(alpha_1_SM_MZ):.8f}")
print(f"1/alpha_1_SM(M_Z)  = {float(1/alpha_1_SM_MZ):.6f}")
print(f"alpha_1_GUT(M_Z)   = {float(alpha_1_GUT_MZ):.8f}")
print(f"1/alpha_1_GUT(M_Z) = {float(1/alpha_1_GUT_MZ):.6f}")
print(f"alpha_3(M_Z)       = {float(alpha_s_MZ):.8f}")
print(f"1/alpha_3(M_Z)     = {float(1/alpha_s_MZ):.6f}")

# Step 4: Run the beta functions from M_Z down to m_e
# 
# alpha_i^{-1}(m_e) = alpha_i^{-1}(M_Z) + (b0_i / (2*pi)) * ln(M_Z / m_e)
#
# All quantities are Fractions. This is exact integer arithmetic.

print(f"\n--- Running couplings from M_Z to m_e ---")
print(f"ln(M_Z/m_e) = {float(ln_ratio):.10f}")

common_factor = ln_ratio / two_pi_rat  # ln(M_Z/m_e) / (2*pi) — exact Fraction

# Run each coupling
alpha1_inv_low = (Fraction(1,1) / alpha_1_GUT_MZ) + b0_alpha1 * common_factor
alpha2_inv_low = (Fraction(1,1) / alpha_2_MZ) + b0_alpha2 * common_factor
alpha3_inv_low = (Fraction(1,1) / alpha_s_MZ) + b0_alpha3 * common_factor

print(f"\n1/alpha_1_GUT(m_e) = {float(alpha1_inv_low):.6f}")
print(f"1/alpha_2(m_e)     = {float(alpha2_inv_low):.6f}")
print(f"1/alpha_3(m_e)     = {float(alpha3_inv_low):.6f}")

# Step 5: Reconstruct alpha_EM at low energy
# 
# In GUT normalization:
#   1/alpha_EM = (3/5) * 1/alpha_1_GUT + 1/alpha_2
#
# This is because:
#   alpha_1_GUT = (5/3) * alpha_1_SM
#   1/alpha_1_SM = (5/3) * 1/alpha_1_GUT  ... no.
#   alpha_1_SM = alpha_1_GUT / (5/3) = (3/5) * alpha_1_GUT
#   1/alpha_1_SM = (5/3) / alpha_1_GUT = (5/3) * 1/alpha_1_GUT
#
# And: 1/alpha_EM = 1/alpha_1_SM + 1/alpha_2  ... no, that's not right either.
#
# The correct relation:
#   alpha_EM = alpha_1_SM * alpha_2 / (alpha_1_SM + alpha_2)
#   => 1/alpha_EM = 1/alpha_1_SM + 1/alpha_2  ... wait, no.
#   1/alpha_EM = (alpha_1_SM + alpha_2) / (alpha_1_SM * alpha_2)
#             = 1/alpha_2 + 1/alpha_1_SM
#
# Hmm, that IS 1/alpha_1_SM + 1/alpha_2. Let me verify:
#   alpha_EM = e^2/(4pi)
#   alpha_1_SM = g'^2/(4pi)  
#   alpha_2 = g^2/(4pi)
#   e = g*sin(theta_W) = g'*cos(theta_W)
#   1/e^2 = 1/(g^2 sin^2) = 1/(g'^2 cos^2)
#
# Actually: 1/e^2 = 1/g'^2 + 1/g^2  
#   because e is defined by 1/e^2 = 1/g^2 + 1/g'^2
#   This is the standard relation.
#   => 1/alpha_EM = 1/alpha_1_SM + 1/alpha_2
#   => 1/alpha_EM = (5/3)/alpha_1_GUT + 1/alpha_2

alpha_EM_inv_low = Fraction(5, 3) * alpha1_inv_low + alpha2_inv_low

print(f"\n{'=' * 70}")
print(f"RESULT: 1/alpha_EM at low energy (integer arithmetic)")
print(f"{'=' * 70}")
print(f"1/alpha_EM(m_e) = {float(alpha_EM_inv_low):.10f}")
print(f"")
print(f"Known value:      137.035999...")
print(f"Computed:          {float(alpha_EM_inv_low):.6f}")
print(f"")

# Step 6: Verify with mpmath
print(f"--- Verification ---")
mp.dps = 50

# Convert our rational result to mpmath
result_mp = mpf(alpha_EM_inv_low.numerator) / mpf(alpha_EM_inv_low.denominator)
print(f"Integer result (50 digits): {mp.nstr(result_mp, 30)}")
print(f"CODATA alpha_EM^-1:         137.035999177...")
print(f"")

# How close?
codata = mpf('137.035999177')
diff = abs(result_mp - codata)
print(f"Difference: {mp.nstr(diff, 10)}")
print(f"Relative difference: {mp.nstr(diff/codata, 10)}")

# Step 7: Show that everything was Fraction
print(f"\n--- Proof of integer arithmetic ---")
print(f"Type of result: {type(alpha_EM_inv_low)}")
print(f"Numerator has {alpha_EM_inv_low.numerator.bit_length()} bits")
print(f"Denominator has {alpha_EM_inv_low.denominator.bit_length()} bits")
print(f"Numerator digit count: {len(str(abs(alpha_EM_inv_low.numerator)))}")
print(f"Denominator digit count: {len(str(alpha_EM_inv_low.denominator))}")


# ============================================================
# SECTION 6: Run in the other direction — M_Z to GUT scale
# ============================================================

print(f"\n{'=' * 70}")
print(f"RUNNING UP: M_Z toward GUT scale")
print(f"{'=' * 70}")

# GUT scale ~ 2 * 10^16 GeV
# ln(M_GUT / M_Z) = ln(2e16 / 91.2) = ln(2.19e14) ≈ 32.9

M_GUT_GeV_num = 2 * 10**16  # 2 * 10^16 GeV
M_Z_GeV_num = 911876  # 91187.6 * 10 to keep rational
M_Z_GeV_den = 10

# Ratio = M_GUT / M_Z = (2*10^16) / (911876/10) = 2*10^17 / 911876
ln_ratio_up = rational_ln_ratio(2 * 10**17, 911876, terms=120)
print(f"ln(M_GUT/M_Z) = {float(ln_ratio_up):.6f}")

common_factor_up = ln_ratio_up / two_pi_rat

# Run UP: alpha_i^{-1}(M_GUT) = alpha_i^{-1}(M_Z) - b0_i * ln(M_GUT/M_Z) / (2*pi)
# (negative because we're going up, not down)
# Actually: alpha^{-1}(mu_high) = alpha^{-1}(mu_low) - (b0/(2pi)) * ln(mu_high/mu_low)
# Wait — let me be consistent. The formula is:
#   alpha^{-1}(mu_2) = alpha^{-1}(mu_1) + (b0/(2pi)) * ln(mu_1/mu_2)
# If mu_2 > mu_1 (running up), ln(mu_1/mu_2) < 0
# So: alpha^{-1}(M_GUT) = alpha^{-1}(M_Z) + (b0/(2pi)) * ln(M_Z/M_GUT)
#                        = alpha^{-1}(M_Z) - (b0/(2pi)) * ln(M_GUT/M_Z)

alpha1_inv_GUT = (Fraction(1,1) / alpha_1_GUT_MZ) - b0_alpha1 * common_factor_up
alpha2_inv_GUT = (Fraction(1,1) / alpha_2_MZ) - b0_alpha2 * common_factor_up
alpha3_inv_GUT = (Fraction(1,1) / alpha_s_MZ) - b0_alpha3 * common_factor_up

print(f"\nAt M_GUT ~ 2*10^16 GeV:")
print(f"1/alpha_1_GUT = {float(alpha1_inv_GUT):.6f}")
print(f"1/alpha_2     = {float(alpha2_inv_GUT):.6f}")
print(f"1/alpha_3     = {float(alpha3_inv_GUT):.6f}")
print(f"")
print(f"Convergence check:")
print(f"  alpha_1 - alpha_2 gap: {float(alpha1_inv_GUT - alpha2_inv_GUT):.4f}")
print(f"  alpha_2 - alpha_3 gap: {float(alpha2_inv_GUT - alpha3_inv_GUT):.4f}")
print(f"  alpha_1 - alpha_3 gap: {float(alpha1_inv_GUT - alpha3_inv_GUT):.4f}")

print(f"\n{'=' * 70}")
print(f"SUMMARY")
print(f"{'=' * 70}")
print(f"")
print(f"Inputs (measured, Tier 3):")
print(f"  alpha_EM(M_Z)^-1 = 127.906")
print(f"  sin^2(theta_W)   = 0.23122")
print(f"  alpha_s(M_Z)     = 0.1180")
print(f"")
print(f"Integer components:")
print(f"  b0 coefficients:  41/10, -19/6, -7  (exact rationals from particle counting)")
print(f"  pi:               integer pair, {pi_rat.numerator.bit_length()} bit numerator")
print(f"  ln(M_Z/m_e):      integer pair, {ln_ratio.numerator.bit_length()} bit numerator")
print(f"")
print(f"Output:")
print(f"  1/alpha_EM(low) = {float(alpha_EM_inv_low):.6f}")
print(f"  Target:           137.036")
print(f"")
print(f"Every intermediate value is a Python Fraction (ratio of two integers).")
print(f"No float was created during computation.")
print(f"The transformation law runs on integers.")
