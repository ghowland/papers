import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass

from fractions import Fraction

# ================================================================
# sin²θ_W from 3/8 at GUT scale
#
# Inputs: α_EM(M_Z)⁻¹, α_s(M_Z) — two measured rationals
# Integer content: b₁=41/10, b₂=-19/6, b₃=-7, sin²θ_W(GUT)=3/8
# Output: sin²θ_W(M_Z) — derived
# ================================================================

# Measured inputs (2 rationals from the universe)
alpha_EM_inv_MZ = Fraction(63953, 500)    # 127.906
alpha_s_MZ = Fraction(59, 500)            # 0.1180

# Integer content (from particle counting)
b1 = Fraction(41, 10)    # U(1)_Y, GUT normalization
b2 = Fraction(-19, 6)    # SU(2)
b3 = Fraction(-7, 1)     # SU(3), 6 flavors above m_t

# Derived: α₃⁻¹(M_Z)
alpha3_inv_MZ = Fraction(1) / alpha_s_MZ   # 500/59

# From unification: α₁_GUT = α₂ = α₃ = α_GUT at M_GUT
# Running: α_i⁻¹(M_Z) = α_GUT⁻¹ + b_i · L
# where L = ln(M_GUT/M_Z) / (2π) > 0
#
# α_EM⁻¹(M_Z) = (5/3)·α₁⁻¹(M_Z) + α₂⁻¹(M_Z)
#              = (5/3)·(α_GUT⁻¹ + b₁·L) + (α_GUT⁻¹ + b₂·L)
#              = (8/3)·α_GUT⁻¹ + (5·b₁/3 + b₂)·L
#
# Coefficient of L in α_EM equation:
coeff_L_em = Fraction(5, 3) * b1 + b2
print(f"Coefficient of L in alpha_EM equation: {coeff_L_em} = {float(coeff_L_em)}")
# Should be 11/3

# Two equations:
# (1) (8/3)·α_GUT⁻¹ + (11/3)·L = α_EM⁻¹(M_Z)
# (2) α_GUT⁻¹ + b₃·L = α₃⁻¹(M_Z)
#
# From (2): α_GUT⁻¹ = α₃⁻¹(M_Z) - b₃·L = 500/59 + 7L
# Sub into (1):
# (8/3)·(500/59 + 7L) + (11/3)·L = 63953/500
# 4000/177 + 56L/3 + 11L/3 = 63953/500
# 4000/177 + 67L/3 = 63953/500

coeff_L_total = Fraction(8, 3) * b3 * Fraction(-1) + coeff_L_em
# Wait, let me redo this cleanly.
# From (2): α_GUT⁻¹ = α₃⁻¹ - b₃·L
# Sub into (1): (8/3)·(α₃⁻¹ - b₃·L) + coeff_L_em·L = α_EM⁻¹
# (8/3)·α₃⁻¹ + (-8/3·b₃ + coeff_L_em)·L = α_EM⁻¹

c_L = Fraction(-8, 3) * b3 + coeff_L_em
c_const = Fraction(8, 3) * alpha3_inv_MZ

print(f"Solving for L:")
print(f"  {float(c_const)} + {float(c_L)} * L = {float(alpha_EM_inv_MZ)}")

L = (alpha_EM_inv_MZ - c_const) / c_L

print(f"  L = {float(L):.10f}")
print(f"  L = {L}")
print()

# Recover α_GUT⁻¹
alpha_GUT_inv = alpha3_inv_MZ - b3 * L
print(f"alpha_GUT⁻¹ = {float(alpha_GUT_inv):.6f}")
print()

# Recover the GUT scale
# L = ln(M_GUT/M_Z) / (2π)
# ln(M_GUT/M_Z) = 2π·L
# We don't need this for sin²θ_W, but it's informative
import math
M_Z_MeV = 91187.6
ln_ratio = float(L) * 2 * math.pi
M_GUT_MeV = M_Z_MeV * math.exp(ln_ratio)
print(f"ln(M_GUT/M_Z) = {ln_ratio:.4f}")
print(f"M_GUT = {M_GUT_MeV:.2e} MeV = {M_GUT_MeV/1000:.2e} GeV")
print(f"log10(M_GUT/GeV) = {math.log10(M_GUT_MeV/1000):.2f}")
print()

# Now compute sin²θ_W(M_Z) from the individual couplings
alpha1_inv_MZ = alpha_GUT_inv + b1 * L
alpha2_inv_MZ = alpha_GUT_inv + b2 * L

print(f"At M_Z:")
print(f"  alpha_1_GUT⁻¹ = {float(alpha1_inv_MZ):.6f}")
print(f"  alpha_2⁻¹     = {float(alpha2_inv_MZ):.6f}")
print(f"  alpha_3⁻¹     = {float(alpha3_inv_MZ):.6f}")
print()

# sin²θ_W = α₁_SM / (α₁_SM + α₂)
# α₁_SM = (3/5)·α₁_GUT
# sin²θ_W = (3/5)·α₁_GUT / ((3/5)·α₁_GUT + α₂)
# = 1 / (1 + (5/3)·α₂/α₁_GUT)
# = 1 / (1 + (5/3)·α₁_GUT⁻¹/α₂⁻¹)  ... no
# Better: sin²θ_W = g'²/(g²+g'²) = α₁_SM/(α₁_SM + α₂)
# In terms of inverses:
# sin²θ_W = α₂⁻¹ / ((3/5)·α₁_GUT⁻¹ + α₂⁻¹)  ... no
# 
# Let me be careful.
# α₁_SM = (3/5)·α₁_GUT
# sin²θ_W = α₁_SM / (α₁_SM + α₂)
# In terms of inverses: 
# 1/sin²θ_W = 1 + α₂/α₁_SM = 1 + α₁_SM⁻¹/α₂⁻¹
# = 1 + (5/3)·α₁_GUT⁻¹ / α₂⁻¹
#
# Actually the simplest:
# sin²θ_W = 3·α₂⁻¹ / (3·α₂⁻¹ + 5·α₁_GUT⁻¹)

sin2_tW = Fraction(3) * alpha2_inv_MZ / (Fraction(3) * alpha2_inv_MZ + Fraction(5) * alpha1_inv_MZ)

print(f"sin²θ_W(M_Z) = {float(sin2_tW):.8f}")
print(f"PDG measured:   0.23122")
print(f"Difference:     {float(sin2_tW) - 0.23122:+.5f}")
print(f"Relative:       {(float(sin2_tW)/0.23122 - 1)*100:+.2f}%")
print()

# Cross-check: α_EM⁻¹ from components
alpha_EM_inv_check = Fraction(5, 3) * alpha1_inv_MZ + alpha2_inv_MZ
print(f"Cross-check: α_EM⁻¹(M_Z) = {float(alpha_EM_inv_check):.6f} (input: {float(alpha_EM_inv_MZ):.6f})")
print()

# What sin²θ_W is at the GUT scale
sin2_GUT = Fraction(3) * alpha_GUT_inv / (Fraction(3) * alpha_GUT_inv + Fraction(5) * alpha_GUT_inv)
print(f"sin²θ_W(GUT) = {float(sin2_GUT)} = {sin2_GUT} (should be 3/8)")
print()

# The result
print("=" * 60)
print("RESULT")
print("=" * 60)
print()
print(f"  INPUT:")
print(f"    α_EM(M_Z)⁻¹ = {alpha_EM_inv_MZ} (measured)")
print(f"    α_s(M_Z)     = {alpha_s_MZ} (measured)")
print(f"    sin²θ_W(GUT) = 3/8 (integer, SU(5) charge counting)")
print(f"    b₁ = {b1}, b₂ = {b2}, b₃ = {b3} (integers, particle counting)")
print()
print(f"  OUTPUT:")
print(f"    sin²θ_W(M_Z) = {float(sin2_tW):.8f}")
print(f"    PDG 2024:       0.23122 ± 0.00003")
print(f"    Difference:     {float(sin2_tW) - 0.23122:+.6f}")
print(f"    Relative:       {(float(sin2_tW)/0.23122 - 1)*100:+.3f}%")
print()
print(f"  All intermediate values are Fraction: {isinstance(sin2_tW, Fraction)}")
print(f"  sin²θ_W = {sin2_tW}")
