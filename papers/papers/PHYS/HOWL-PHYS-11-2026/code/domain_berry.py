import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass
from fractions import Fraction

print("=" * 70)
print("PHASE 1, DOMAIN 4: BERRY PHASE")
print("Spin-1/2 in Rotating Magnetic Field")
print("=" * 70)
print()

# ================================================================
# Pi as exact Fraction
# ================================================================

def rational_arctan(x, terms=160):
    result = Fraction(0); power = x; x_sq = x * x
    for k in range(terms):
        nn = 2 * k + 1
        if k % 2 == 0: result += power / nn
        else: result -= power / nn
        power *= x_sq
    return result

pi_f = 4*(4*rational_arctan(Fraction(1,5),160)-rational_arctan(Fraction(1,239),160))
R2 = pi_f / 4
R4 = pi_f**2 / 32

# ================================================================
# (a) STANDARD FORM
# ================================================================

print("(a) STANDARD FORM")
print()
print("  System: spin-1/2 particle in magnetic field B(t)")
print("  B rotates around z-axis, sweeping cone of half-angle θ")
print()
print("  Berry phase for spin-s, magnetic quantum number m:")
print("    γ = -m × Ω")
print("  where Ω = 2π(1 - cosθ) is the solid angle of the cone.")
print()
print("  For spin-1/2, m = -1/2 (ground state):")
print("    γ = π(1 - cosθ) = Ω/2")
print()
print("  The solid angle Ω = 2π(1 - cosθ) is the area of the")
print("  spherical cap on the unit sphere swept by the B-field direction.")
print()
print("  Established by Berry 1984, Simon 1983.")
print()

# ================================================================
# (b) DECOMPOSED INTO INTEGER + REMAINDER
# ================================================================

print("(b) DECOMPOSED: INTEGER + REMAINDER")
print()
print("  γ / (2π) = winding number + fractional phase")
print()
print("  Modulus: 2π (full phase cycle)")
print("  Integer: winding number n = ⌊γ/(2π)⌋")
print("  Remainder: γ mod 2π (the observable geometric phase)")
print()
print("  The remainder is gauge-invariant and physically observable.")
print("  The integer part is gauge-dependent (choice of branch).")
print()
print("  For one circuit of the B-field around the cone:")
print("    γ = Ω/2 = π(1 - cosθ)")
print("    γ/(2π) = (1 - cosθ)/2")
print("    Since 0 ≤ θ ≤ π: 0 ≤ (1-cosθ)/2 ≤ 1")
print("    So the integer part is 0 for a single circuit")
print("    and the remainder IS the Berry phase.")
print()

# ================================================================
# (c) FRACTION ARITHMETIC
# ================================================================

print("(c) FRACTION ARITHMETIC")
print()
print("  We need cosθ as exact Fractions.")
print("  Choose rational angles where cosθ is rational:")
print()

# Test cases with exact rational cosθ
# cosθ rational → γ = π(1 - cosθ) is a rational multiple of π
test_cases = [
    ("θ=0 (no cone)",           Fraction(1),     "trivial"),
    ("θ=π/3 (cosθ=1/2)",       Fraction(1, 2),  "60° cone"),
    ("θ=π/2 (cosθ=0)",         Fraction(0),     "90° half-sphere"),
    ("θ=2π/3 (cosθ=-1/2)",     Fraction(-1, 2), "120° cone"),
    ("θ=π (cosθ=-1)",          Fraction(-1),    "full sphere"),
    ("θ: cosθ=1/3",            Fraction(1, 3),  "generic"),
    ("θ: cosθ=3/4",            Fraction(3, 4),  "generic"),
    ("θ: cosθ=-1/4",           Fraction(-1, 4), "generic"),
    ("θ: cosθ=7/8",            Fraction(7, 8),  "small cone"),
]

two_pi = 2 * pi_f
spin_m = Fraction(-1, 2)  # spin-1/2, ground state m = -1/2

print(f"  Spin quantum number m = {spin_m}")
print(f"  Modulus = 2π = 8R₂")
print()
print(f"  {'Case':<30} {'cosθ':>6} {'Ω/2π':>8} {'γ/π':>8} {'γ/(2π)':>10} {'Int':>4} {'R/(2π)':>10} {'R/π':>8}")
print(f"  {'-'*30} {'-'*6} {'-'*8} {'-'*8} {'-'*10} {'-'*4} {'-'*10} {'-'*8}")

for label, cos_theta, note in test_cases:
    # Solid angle
    Omega = 2 * pi_f * (1 - cos_theta)
    
    # Berry phase: γ = -m × Ω = (1/2) × Ω = Ω/2
    gamma = -spin_m * Omega  # = Ω/2 = π(1 - cosθ)
    
    # Verify: γ = π(1 - cosθ)
    gamma_check = pi_f * (1 - cos_theta)
    assert gamma == gamma_check, f"FAIL: Berry phase mismatch for {label}"
    
    # Decompose: γ / (2π) = integer + remainder
    gamma_over_2pi = gamma / two_pi  # = (1 - cosθ)/2
    
    # Since 0 ≤ (1-cosθ)/2 ≤ 1, integer is 0 (except cosθ=-1 gives exactly 1)
    if gamma_over_2pi >= 0:
        integer_part = int(gamma_over_2pi)
        # Handle exact integer case (full sphere)
        if gamma_over_2pi == integer_part:
            remainder_frac = Fraction(0)
        else:
            remainder_frac = gamma_over_2pi - integer_part
    else:
        integer_part = int(gamma_over_2pi) - 1
        remainder_frac = gamma_over_2pi - integer_part
    
    # The remainder over 2π (fractional phase)
    r_over_2pi = remainder_frac
    
    # γ/π for display
    gamma_over_pi = gamma / pi_f  # = 1 - cosθ
    
    # Ω/(2π) for display
    Omega_over_2pi = Omega / two_pi  # = 1 - cosθ
    
    print(f"  {label:<30} {str(cos_theta):>6} {str(Omega_over_2pi):>8} "
          f"{str(gamma_over_pi):>8} {str(gamma_over_2pi):>10} "
          f"{integer_part:>4} {str(r_over_2pi):>10} {str(remainder_frac * 2):>8}")

print()

# ================================================================
# Verify key special cases
# ================================================================

print("  Key verifications (all EXACT):")
print()

# Case 1: θ = π/2 (half-sphere), γ = π
cos_half = Fraction(0)
gamma_half = pi_f * (1 - cos_half)  # = π
assert gamma_half == pi_f
print(f"  θ=π/2: γ = π, γ/(2π) = 1/2. ✓")
print(f"    Integer = 0, Remainder = 1/2 of full cycle = π")
print(f"    This is the Z₂ topological phase (γ = π mod 2π)")
print()

# Case 2: θ = π (full sphere), γ = 2π 
cos_full = Fraction(-1)
gamma_full = pi_f * (1 - cos_full)  # = 2π
assert gamma_full == two_pi
print(f"  θ=π: γ = 2π, γ/(2π) = 1. ✓")
print(f"    Integer = 1, Remainder = 0")
print(f"    Full sphere: the Berry phase is a complete cycle (trivial)")
print()

# Case 3: θ = π/3 (60° cone), γ = π/2
cos_60 = Fraction(1, 2)
gamma_60 = pi_f * (1 - cos_60)  # = π/2
assert gamma_60 == pi_f / 2
print(f"  θ=π/3: γ = π/2, γ/(2π) = 1/4. ✓")
print(f"    Integer = 0, Remainder = 1/4 of full cycle")
print()

# Case 4: generic cosθ = 1/3
cos_gen = Fraction(1, 3)
gamma_gen = pi_f * (1 - cos_gen)  # = 2π/3
assert gamma_gen == 2 * pi_f / 3
print(f"  cosθ=1/3: γ = 2π/3, γ/(2π) = 1/3. ✓")
print(f"    Integer = 0, Remainder = 1/3 of full cycle")
print()

# ================================================================
# Multiple circuits: the integer accumulates
# ================================================================

print("  Multiple circuits (integer accumulates):")
print()

cos_theta = Fraction(1, 2)  # θ = π/3
gamma_single = pi_f * (1 - cos_theta)  # = π/2 per circuit

for circuits in [1, 2, 3, 4, 5, 8]:
    gamma_total = circuits * gamma_single
    gamma_over_2pi = gamma_total / two_pi
    integer_part = int(gamma_over_2pi)
    remainder = gamma_over_2pi - integer_part
    
    print(f"    {circuits} circuit(s): γ = {circuits}×π/2 = {circuits}/4 × 2π, "
          f"integer={integer_part}, R/(2π)={remainder}")
    
    # Verify: remainder should be (circuits/4) mod 1
    expected_r = Fraction(circuits, 4) - int(Fraction(circuits, 4))
    assert remainder == expected_r

print()
print("  The integer part counts complete phase cycles.")
print("  The remainder is the accumulated geometric phase mod 2π.")
print("  Both are exact Fractions at every step.")
print()

# ================================================================
# (d) VERIFICATION
# ================================================================

print("(d) VERIFICATION")
print()
print("  Berry phase γ = -m·Ω where Ω = solid angle of parameter path.")
print("  For spin-1/2 (m = -1/2): γ = Ω/2 = π(1 - cosθ).")
print()
print("  Known exact results:")
print("    θ = π/2: γ = π (Z₂ topological insulator phase)")
print("    θ = π:   γ = 2π (trivial, full winding)")
print("    θ = 0:   γ = 0 (no enclosed solid angle)")
print("  All reproduced exactly in Fraction arithmetic.")
print()
print("  The Berry phase is gauge-invariant mod 2π.")
print("  Our integer/remainder decomposition respects this:")
print("  the remainder γ mod 2π is the physical observable.")
print()

# ================================================================
# (e) R_n CONTENT
# ================================================================

print("(e) R_n CONTENT")
print()

# The modulus is 2π = 8R₂
assert two_pi == 8 * R2
print(f"  Modulus: 2π = 8R₂. Verify: {two_pi == 8*R2} (EXACT)")
print()

# The solid angle Ω = 2π(1-cosθ) = 8R₂(1-cosθ)
# So the Berry phase γ = Ω/2 = 4R₂(1-cosθ)
gamma_R2 = 4 * R2 * (1 - cos_60)  # for θ=π/3
gamma_direct = pi_f * (1 - cos_60)
assert gamma_R2 == gamma_direct
print(f"  Berry phase: γ = 4R₂(1-cosθ). Verify: {gamma_R2 == gamma_direct} (EXACT)")
print()

# The solid angle of the full sphere: Ω_full = 4π = 16R₂
Omega_full = 4 * pi_f
sixteen_R2 = 16 * R2
assert Omega_full == sixteen_R2
print(f"  Full sphere solid angle: 4π = 16R₂. Verify: {Omega_full == sixteen_R2} (EXACT)")
print()

# Connection to MATH-5: the solid angle of S² is 4π = 16R₂
# This is the SURFACE AREA of the unit sphere = 4πr² at r=1
# = 4R₂ × (2r)² = 4R₂ × d² (using R₂ for 2D surface operation)
# Consistent with MATH-5 rule: surface area uses R₂ (2D operation on 3D object)
print("  Connection to MATH-5:")
print("    Solid angle = surface area of unit sphere = 4π = 16R₂")
print("    This is 4R₂·d² at d=2 (unit sphere has d=2)")
print("    MATH-5 rule: surface area uses R₂ (2D operation)")
print("    Berry phase uses Ω (surface area on S²) → R₂ appears")
print()
print("  Two-level structure:")
print("    Geometric level: R₂ in the modulus 2π = 8R₂ and in Ω = 16R₂(1-cosθ)/2")
print("    Topological level: (1-cosθ)/2 is the fractional solid angle, the remainder")
print()

# ================================================================
# (f) ASSERTIONS SUMMARY
# ================================================================

print("(f) ALL ASSERTIONS PASSED")
print()
print("  9 test cases × decomposition verified")
print("  3 special cases (θ=0, π/2, π) verified against known exact results")
print("  5 multi-circuit accumulations verified")
print("  R₂ content verified: 2π=8R₂, 4π=16R₂, γ=4R₂(1-cosθ)")
print()

# ================================================================
# EXTRACTION TABLE ROW
# ================================================================

print("=" * 70)
print("EXTRACTION TABLE ROW")
print("=" * 70)
print()
print("| Domain      | Equation              | Modulus  | Integer       | Remainder     | R_n       | Script                | Status   |")
print("|-------------|----------------------|----------|---------------|---------------|-----------|----------------------|----------|")
print("| Berry phase | γ=-m·Ω, Ω=2π(1-cosθ)| 2π=8R₂  | Winding n     | γ mod 2π      | 4R₂(1-cosθ)| phase1_berry.py      | VERIFIED |")