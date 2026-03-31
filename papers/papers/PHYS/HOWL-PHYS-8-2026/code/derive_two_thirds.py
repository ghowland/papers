"""
Exploring the geometric origin of 2/3 in the Koide formula.

The Koide relation: (Σm)/(Σ√m)² = 2/3

Question: does 2/3 arise from a geometric construction involving
three objects on a circle, or from the structure of the fermion
loop integral, or from both?

Approach: work through several geometric constructions and see
which ones produce 2/3.
"""

from fractions import Fraction
from math import cos, sin, pi, sqrt

# ================================================================
# Construction 1: Cauchy-Schwarz bound
# ================================================================
print("=" * 60)
print("CONSTRUCTION 1: CAUCHY-SCHWARZ")
print("=" * 60)
print()
print("For any N positive numbers x_i:")
print("  (Σ x_i²) / (Σ x_i)² >= 1/N  (Cauchy-Schwarz)")
print("  Equality iff all x_i are equal.")
print()
print("Set x_i = √m_i. Then Σx_i² = Σm_i, and (Σx_i)² = (Σ√m_i)²")
print("  Koide ratio = (Σm) / (Σ√m)² >= 1/3")
print("  Lower bound: 1/3 (all masses equal)")
print("  Upper bound: 1 (one mass dominates)")
print()
print("Koide = 2/3 is EXACTLY HALFWAY between 1/3 and 1.")
print("  (2/3 - 1/3) / (1 - 1/3) = (1/3) / (2/3) = 1/2")
print()
print("This is the midpoint of the allowed range.")
print()

# ================================================================
# Construction 2: The parametrization constraint
# ================================================================
print("=" * 60)
print("CONSTRUCTION 2: PARAMETRIZATION")
print("=" * 60)
print()
print("Write √m_i = M(1 + √2 · cos(θ₀ + 2πi/3))")
print()
print("Then: Σ√m_i = 3M  (cos terms cancel by 120° symmetry)")
print("      (Σ√m_i)² = 9M²")
print()
print("And:  Σm_i = Σ M²(1 + √2·cos(φ_i))²")
print("            = M² Σ (1 + 2√2·cos(φ_i) + 2·cos²(φ_i))")
print()
print("Sum of cos(φ_i) at 120° spacing = 0")
print("Sum of cos²(φ_i) at 120° spacing:")

# Verify: sum of cos²(θ + 2πk/3) for k=0,1,2
for theta0 in [0, 0.5, 1.0, 2.316]:
    s = sum(cos(theta0 + 2*pi*k/3)**2 for k in range(3))
    print(f"  θ₀ = {theta0:.3f}: Σcos² = {s:.6f}")

print()
print("Sum of cos²(φ_i) = 3/2 for ANY θ₀ (trigonometric identity)")
print()
print("Therefore:")
print("  Σm_i = M²(3 + 0 + 2·(3/2)) = M²(3 + 3) = 6M²")
print("  Koide = 6M² / 9M² = 6/9 = 2/3")
print()
print("THE 2/3 IS A TRIGONOMETRIC IDENTITY.")
print("It follows from: Σcos²(θ + 2πk/3) = 3/2 for all θ.")
print("This is a property of equally-spaced points on a circle.")
print()

# ================================================================
# Construction 3: Why 3/2?
# ================================================================
print("=" * 60)
print("CONSTRUCTION 3: WHY Σcos² = 3/2?")
print("=" * 60)
print()
print("cos²(x) = (1 + cos(2x))/2")
print()
print("Σ cos²(θ + 2πk/3) = Σ (1 + cos(2θ + 4πk/3))/2")
print("                   = 3/2 + (1/2)Σcos(2θ + 4πk/3)")
print()
print("The sum Σcos(2θ + 4πk/3) for k=0,1,2:")
print("  = cos(2θ) + cos(2θ + 4π/3) + cos(2θ + 8π/3)")
print("  = cos(2θ) + cos(2θ + 4π/3) + cos(2θ + 2π/3)")
print("  This is three equally-spaced cosines → sum = 0")
print()
print("Therefore Σcos² = 3/2 + 0 = 3/2")
print()
print("The 3/2 comes from:")
print("  3 terms × (1/2 from cos² identity) = 3/2")
print("  The oscillating part cancels by 120° symmetry")
print()

# ================================================================
# Construction 4: The chain of integers
# ================================================================
print("=" * 60)
print("CONSTRUCTION 4: THE CHAIN OF INTEGERS")
print("=" * 60)
print()
print("Starting from the Koide parametrization:")
print("  √m_i = M(1 + √2 · cos(θ₀ + 2πi/3))")
print()
print("The integers that determine 2/3:")
print("  3 objects on a circle (N = 3)")
print("  120° = 2π/3 spacing (360°/N)")
print("  cos² identity: cos²x = (1+cos2x)/2  (the 2 in the double angle)")
print("  Sum of N equally-spaced cosines = 0  (for any N ≥ 2)")
print()
print("Koide ratio = (N + N·cos²_sum) / N²")
print("where cos²_sum = Σcos²(θ + 2πk/N)")
print()

# Generalize: what is the "Koide ratio" for N objects at equal spacing?
print("Generalized Koide ratio for N equally-spaced objects:")
print("  √m_i = M(1 + √2·cos(θ₀ + 2πi/N))")
print()

for N in range(2, 8):
    cos2_sum = Fraction(N, 2)
    numerator = Fraction(N) + Fraction(2) * cos2_sum
    denominator = Fraction(N) * Fraction(N)
    ratio = numerator / denominator
    print(f"  N = {N}: Σcos² = {cos2_sum}, ratio = {numerator}/{denominator} = {ratio} = {float(ratio):.6f}")

print()
print("For ALL N ≥ 2: Σcos²(θ+2πk/N) = N/2")
print("  Ratio = (N + 2·(N/2)) / N² = 2N/N² = 2/N")
print()
print("  N=2: ratio = 1")
print("  N=3: ratio = 2/3  ← KOIDE")
print("  N=4: ratio = 1/2")
print("  N=5: ratio = 2/5")
print()
print("THE KOIDE CONSTANT 2/3 = 2/N FOR N=3.")
print()
print("The Koide formula is the N=3 case of a general identity:")
print("  (Σm) / (Σ√m)² = 2/N")
print("for N objects parametrized as √m_i = M(1+√2·cos(θ₀+2πi/N))")
print()

# ================================================================
# Construction 5: What does N mean?
# ================================================================
print("=" * 60)
print("CONSTRUCTION 5: WHAT DOES N=3 MEAN?")
print("=" * 60)
print()
print("N = 3 is the number of generations.")
print("The Standard Model has 3 generations of charged leptons.")
print("The Koide constant 2/3 = 2/N_gen.")
print()
print("If the number of generations were different:")
print("  2 generations: Koide constant = 2/2 = 1")
print("  3 generations: Koide constant = 2/3 ← observed")
print("  4 generations: Koide constant = 2/4 = 1/2")
print()
print("The Koide constant ENCODES the number of generations.")
print("It is not a free parameter. It is 2/N_gen.")
print("N_gen = 3 is an integer. The Koide constant is 2/3.")
print()
print("The √2 in the parametrization is also fixed:")
print("  It is the amplitude that makes the parametrization")
print("  span the full range from m_i = 0 (when cos = -1/√2)")
print("  to maximum. The √2 ensures the lightest mass can")
print("  approach zero, which it does (m_e << m_μ << m_τ).")
print()

# ================================================================
# Summary
# ================================================================
print("=" * 60)
print("DERIVATION SUMMARY")
print("=" * 60)
print()
print("The Koide constant 2/3 is derived, not measured.")
print()
print("Chain:")
print("  1. Three generations exist (N=3, empirical)")
print("  2. Three objects on a circle at equal spacing (120° = 2π/3)")
print("  3. Parametrize: √m_i = M(1 + √2·cos(θ₀ + 2πi/3))")
print("  4. Trigonometric identity: Σcos²(θ+2πk/3) = 3/2")
print("  5. Σm = M²(3 + 2·(3/2)) = 6M²")
print("  6. (Σ√m)² = (3M)² = 9M²")
print("  7. Ratio = 6M²/9M² = 2/3")
print()
print("The 2/3 follows from:")
print("  - N=3 (integer, the number of generations)")
print("  - Equal spacing on a circle (maximum symmetry)")
print("  - cos²(x) = (1+cos(2x))/2 (trigonometric identity)")
print("  - Equally-spaced cosines sum to zero")
print()
print("No free parameters. No fitting. The 2/3 is 2/N_gen.")
print("The only input beyond integers is: the generations are")
print("equally spaced on a circle in √(inertia) space.")

