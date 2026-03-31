import sys
try:
    sys.set_int_max_str_digits(1000000)
except:
    pass
from fractions import Fraction

print("=" * 70)
print("PHASE 2: CROSS-DOMAIN UNIFICATION")
print("Six Questions from DISC-6")
print("=" * 70)
print()

def rational_arctan(x, terms=160):
    result = Fraction(0); power = x; x_sq = x * x
    for k in range(terms):
        nn = 2*k+1
        if k%2==0: result += power/nn
        else: result -= power/nn
        power *= x_sq
    return result

pi_f = 4*(4*rational_arctan(Fraction(1,5),160)-rational_arctan(Fraction(1,239),160))
R2 = pi_f / 4
R4 = pi_f**2 / 32
two_pi = 2 * pi_f

# ================================================================
# Q3: Does R₂ appear in Berry phase? (ALREADY ANSWERED IN PHASE 1)
# ================================================================

print("=" * 70)
print("Q3: Does R₂ appear in Berry phase?")
print("=" * 70)
print()
print("  ANSWERED IN PHASE 1: YES")
print("  γ = 4R₂(1 - cosθ)")
print("  Ω = 2π(1-cosθ) = 8R₂(1-cosθ)")
print("  Full sphere: 4π = 16R₂")
assert 4*pi_f == 16*R2
print(f"  Verify 4π = 16R₂: {4*pi_f == 16*R2} (EXACT)")
print()
print("  R₂ appears because Berry phase integrates over S²")
print("  (a 2D surface), and surface area is a 2D operation → R₂.")
print("  This is the MATH-5 rule: remainder matches operation dimension.")
print()
print("  STATUS: CONFIRMED (from Phase 1)")
print()

# ================================================================
# Q4: Does R₄ appear throughout CS? (ALREADY ANSWERED IN PHASE 1)
# ================================================================

print("=" * 70)
print("Q4: Does R₄ appear throughout CS computation?")
print("=" * 70)
print()
print("  ANSWERED IN PHASE 1: YES (in normalization)")
print("  Chern class: 1/(8π²) = 1/(256R₄)")
assert Fraction(1)/(8*pi_f**2) == Fraction(1)/(256*R4)
print(f"  Verify: {Fraction(1)/(8*pi_f**2) == Fraction(1)/(256*R4)} (EXACT)")
print()
print("  R₄ enters because the Chern class integrates over a 4-manifold")
print("  (a 4D operation), and 4D volume → R₄.")
print("  The CS invariant on the 3D boundary inherits R₄ from")
print("  the 4D bulk normalization.")
print()
print("  The CS VALUES (flat connection invariants) are pure rationals —")
print("  no transcendental content. R₄ lives in the normalization,")
print("  not in the CS values themselves.")
print()
print("  STATUS: CONFIRMED (from Phase 1)")
print()

# ================================================================
# Q1: Maslov-Berry connection in exact Fraction arithmetic
# ================================================================

print("=" * 70)
print("Q1: Maslov-Berry connection as exact Fraction identity")
print("=" * 70)
print()
print("  Known result (Robbins 1991, Littlejohn 1992):")
print("  The Maslov index IS a Berry phase in the semiclassical limit.")
print("  For a system with Hamiltonian H(q,p,λ) where λ varies slowly:")
print("    Maslov correction = Berry phase / π")
print("    μ/4 = γ_Berry / π (for each turning point type)")
print()
print("  Specific connection:")
print("    Soft turning point: Berry phase = π/2 → Maslov contribution = 1/2")
print("    Hard wall:          Berry phase = π   → Maslov contribution = 1")
print()
print("  Test in Fraction arithmetic:")
print()

# The connection: at a soft classical turning point, the
# semiclassical wavefunction picks up a phase of π/2.
# Two soft turning points (harmonic oscillator): total = 2 × π/2 = π.
# The Maslov correction μ/4 = 2/4 = 1/2.
# The Berry phase for the adiabatic orbit = π (half the full circle).
# So: μ/4 = Berry_phase / (2π) × 2 ... let me be precise.

# Actually the clean statement:
# For a 1D system with two soft turning points:
#   Total phase accumulated at turning points = μ × (π/2) = 2 × π/2 = π
#   This equals the Berry phase for the orbit in phase space
#   The Maslov correction μ/4 = (total turning-point phase) / (2π)

# Harmonic oscillator
mu_ho = Fraction(2)
phase_per_tp = pi_f / 2  # π/2 per soft turning point
total_tp_phase = mu_ho * phase_per_tp  # 2 × π/2 = π
maslov_correction = mu_ho / 4  # = 1/2

# The Berry phase for the orbit = total turning-point phase
berry_from_maslov = total_tp_phase  # = π

# Check: maslov correction = berry phase / (2π)
ratio = berry_from_maslov / two_pi
assert ratio == maslov_correction
print(f"  Harmonic oscillator:")
print(f"    μ = {mu_ho} (two soft turning points)")
print(f"    Phase per turning point = π/2")
print(f"    Total turning-point phase = μ × π/2 = π")
print(f"    Berry phase of orbit = π")
print(f"    Maslov correction μ/4 = {maslov_correction}")
print(f"    Berry_phase / (2π) = π/(2π) = {ratio}")
print(f"    μ/4 = Berry/(2π) ? {ratio == maslov_correction} (EXACT)")
print()

# Infinite well
mu_box = Fraction(4)
phase_per_hard = pi_f  # π per hard wall
total_tp_box = mu_box / 2 * phase_per_hard  # 2 walls × π = 2π
# Wait: μ = 4 means 4 half-units of π/2. Each hard wall contributes μ=2,
# i.e., 2 × π/2 = π per wall. Two walls: 2π total.
total_tp_box = 2 * pi_f  # = 2π
maslov_box = mu_box / 4  # = 1
berry_box = total_tp_box  # = 2π
ratio_box = berry_box / two_pi  # = 1

assert ratio_box == maslov_box
print(f"  Infinite well:")
print(f"    μ = {mu_box} (two hard walls, each contributes 2)")
print(f"    Phase per hard wall = π")
print(f"    Total turning-point phase = 2 × π = 2π")
print(f"    Berry phase of orbit = 2π")
print(f"    Maslov correction μ/4 = {maslov_box}")
print(f"    Berry_phase / (2π) = 2π/(2π) = {ratio_box}")
print(f"    μ/4 = Berry/(2π) ? {ratio_box == maslov_box} (EXACT)")
print()

# General: for any 1D system with Maslov index μ
# Total turning-point phase = μ × π/2
# Berry phase = μ × π/2
# Maslov correction = Berry / (2π) = μ/(4) 
# This is the identity: μ/4 = (μ × π/2) / (2π) = μ/4. Tautological!

print("  General identity:")
print("    Total turning-point phase = μ × (π/2)")
print("    Berry phase of orbit = μ × (π/2)")  
print("    Maslov correction = Berry/(2π) = [μ × π/2] / (2π) = μ/4")
print()
print("  In R₂ notation:")
print("    Phase per soft TP = π/2 = 2R₂")
print("    Phase per hard TP = π = 4R₂")
print("    Modulus = 2π = 8R₂")
print("    Maslov = (μ × 2R₂) / (8R₂) = μ/4")
print()

# Verify the R₂ identities
assert pi_f / 2 == 2 * R2
assert pi_f == 4 * R2
assert two_pi == 8 * R2
print(f"  Verify π/2 = 2R₂: {pi_f/2 == 2*R2} (EXACT)")
print(f"  Verify π = 4R₂: {pi_f == 4*R2} (EXACT)")
print(f"  Verify 2π = 8R₂: {two_pi == 8*R2} (EXACT)")
print()

print("  FINDING: The Maslov-Berry connection is an IDENTITY")
print("  when expressed in R₂ units. The Maslov correction μ/4")
print("  is the Berry phase measured in units of the modulus 8R₂.")
print("  The connection is exact, algebraic, and tautological —")
print("  both are counting the same thing (phase at turning points)")
print("  in the same units (multiples of 2R₂ = π/2).")
print()
print("  STATUS: CONFIRMED — exact Fraction identity, algebraically tautological")
print()

# ================================================================
# Q6: θ=0 minimization analog in BZ
# ================================================================

print("=" * 70)
print("Q6: θ=0 minimization has BZ analog?")
print("=" * 70)
print()
print("  Theta vacuum: E(θ) = E₀ - χ cos(θ), minimized at θ = 0")
print("  Brillouin zone: E(k) = -2t cos(ka), minimized at k = 0")
print()
print("  Both are cosine potentials minimized at the zero of the parameter.")
print()

# In Fraction arithmetic:
# E(θ)/(-χ) = cos(θ), minimum at θ = 0 where cos(0) = 1
# E(k)/(-2t) = cos(ka), minimum at k = 0 where cos(0) = 1

# The structural parallel:
# Theta: parameter θ, period 2π, minimum at θ=0, modulus 2π = 8R₂
# BZ:    parameter k, period G=2π/a, minimum at k=0, modulus G = 8R₂/a

print("  Structural comparison:")
print()
print("  | Property      | Theta vacuum         | Brillouin zone       |")
print("  |---------------|---------------------|---------------------|")
print("  | Parameter     | θ                   | k                   |")
print("  | Energy        | E₀ - χ cos(θ)       | -2t cos(ka)         |")
print("  | Period        | 2π = 8R₂            | G = 2π/a = 8R₂/a   |")
print("  | Minimum at    | θ = 0               | k = 0               |")
print("  | Maximum at    | θ = π               | k = π/a = G/2       |")
print("  | cos argument  | θ                   | ka = 2πk/G          |")
print("  | Integer part  | Instanton ν         | Zone index n        |")
print("  | Remainder     | θ mod 2π            | k mod G             |")
print("  | Ground state  | R = 0 (PHYS-7)      | R = 0 (band minimum)|")
print()

# The key identity: both minimize cos(x) at x = 0
# cos(0) = 1 is the maximum of cos, giving the minimum of -cos
# In Fraction: cos(0) = 1 exactly
print("  Both systems minimize -cos(x) at x = 0.")
print("  cos(0) = 1 (exact integer, no transcendental content).")
print("  The ground state remainder is 0 in both cases.")
print()
print("  The DIFFERENCE:")
print("    Theta: the minimum is SELECTED by energy minimization")
print("    (no dynamics forces θ away from 0)")
print("    BZ: the minimum is POPULATED by electron filling")
print("    (electrons fill from k=0 upward in the band)")
print()
print("  The SAME MATH: E = A - B cos(x), period P = 8R₂ × scale,")
print("  minimum at x = 0 (remainder = 0).")
print()

# Can we write a unified formula?
# E(x; A, B, P) = A - B cos(2πx/P)
# = A - B cos(x / (P/(2π)))
# = A - B cos(x / (4R₂ × scale/π))
# Hmm, cleaner:
# Let φ = x/P × 2π = x × 8R₂/P (the phase in [0, 8R₂))
# E(φ) = A - B cos(φ)

print("  Unified form: E(φ) = A - B cos(φ)")
print("  where φ = 2πx/P = 8R₂ × x/P")
print("  Theta: x = θ, P = 2π = 8R₂, so φ = θ")
print("  BZ: x = k, P = G = 8R₂/a, so φ = ka")
print()
print("  In both cases φ ∈ [0, 8R₂) and the minimum is at φ = 0.")
print("  The modulus is 8R₂ in the PHASE variable φ.")
print()
print("  STATUS: CONFIRMED — same mathematical structure.")
print("  Both are cosine on a periodic domain with modulus 8R₂,")
print("  minimized at remainder = 0.")
print()

# ================================================================
# Q2: BZ boundary vs RG threshold
# ================================================================

print("=" * 70)
print("Q2: BZ boundary shares structure with RG threshold?")
print("=" * 70)
print()
print("  Brillouin zone: at k = ±π/a (zone boundary), band gap opens.")
print("    Electron undergoes Bragg reflection.")
print("    Below gap: conducting. Above gap: insulating (at half-filling).")
print("    The boundary is at k = G/2 = 4R₂/a (half the modulus).")
print()
print("  RG running: at μ = m_f (mass threshold), new flavor activates.")
print("    Below threshold: flavor decoupled. Above: flavor contributes.")
print("    The coupling α⁻¹ jumps by ΔR = Q_f²/(3π) × R(M_Z², m_f²)")
print()

# The structural parallel:
# BZ: continuous dispersion E(k), discrete gap at zone boundary
# RG: continuous running α(μ), discrete jump at mass threshold

# What they share:
# 1. Both have a continuous variable accumulating
# 2. Both have discrete boundaries where character changes
# 3. Both boundaries are at specific values of the variable

# What differs:
# BZ boundary at k = G/2: this is half the modulus, geometrically determined
# RG threshold at μ = m_f: this is the physical mass, experimentally determined

print("  Structural comparison:")
print()
print("  | Property          | Brillouin zone      | RG running          |")
print("  |-------------------|--------------------|--------------------|")
print("  | Continuous var     | k (momentum)       | ln(μ) (log energy) |")
print("  | Accumulates        | Phase ka           | Running α⁻¹        |")
print("  | Boundary location  | k = G/2 = 4R₂/a   | μ = m_f (measured)  |")
print("  | At boundary        | Band gap opens     | New flavor activates|")
print("  | Below boundary     | Extended state     | Flavor decoupled    |")
print("  | Above boundary     | Reflected/new band | Flavor contributes  |")
print("  | Boundary origin    | Lattice geometry   | Particle mass       |")
print("  | Number of bound.   | Infinite (periodic)| Finite (6 quarks + 3 leptons)|")
print()

# The key difference: BZ boundaries are periodic and geometrically determined.
# RG thresholds are aperiodic and experimentally determined.

# But: the VP running coefficient 1/(3π) = 1/(12R₂) contains R₂
# The BZ modulus G = 8R₂/a contains R₂
# Both contain R₂ but in different roles

vp_coeff = Fraction(1, 3) / pi_f
vp_R2 = Fraction(1, 12) / R2
# These aren't equal because 1/(3π) ≠ 1/(12R₂)
# 1/(3π) = 1/(3 × 4R₂) = 1/(12R₂). Actually they ARE equal!
assert Fraction(1)/(3*pi_f) == Fraction(1)/(12*R2)
print(f"  VP coefficient: 1/(3π) = 1/(12R₂): {Fraction(1)/(3*pi_f) == Fraction(1)/(12*R2)} (EXACT)")
print()
print("  The VP running step per flavor is proportional to 1/(12R₂).")
print("  The BZ modulus is 8R₂/a.")
print("  Both contain R₂ but in different functional roles:")
print("    BZ: R₂ sets the PERIOD (how far between boundaries)")
print("    RG: R₂ sets the STEP SIZE (how much changes at each boundary)")
print()

# Functional form comparison:
# BZ: E(k) = E₀ - 2t cos(8R₂ k/G_scale)
# RG: α⁻¹(μ) = α⁻¹(μ₀) + Σ [1/(12R₂)] × Q_f² × ln(μ/m_f) × Θ(μ-m_f)

print("  Functional form:")
print("    BZ: E(k) = E₀ - 2t cos(k × 8R₂/G)")
print("    RG: α⁻¹(μ) = α⁻¹(μ₀) + Σ_f [Q²/(12R₂)] × ln(μ/m_f) × Θ(μ-m_f)")
print()
print("  BZ is PERIODIC (cosine). RG is MONOTONIC (logarithmic sum).")
print("  BZ has infinite identical boundaries. RG has finite distinct thresholds.")
print("  The parallel is structural (continuous + discrete), not formal (not same equation).")
print()
print("  STATUS: STRUCTURAL PARALLEL, NOT FORMAL EQUIVALENCE")
print("  Both have remainder accumulating between discrete boundaries.")
print("  Both contain R₂. But the functional forms differ (cosine vs log).")
print("  The BZ boundary is at G/2 (geometric). The RG threshold is at m_f (measured).")
print()

# ================================================================
# Q5: Is VP running a BZ band structure?
# ================================================================

print("=" * 70)
print("Q5: Is VP running a specific instance of BZ band structure?")
print("=" * 70)
print()
print("  This is the strongest version of Q2.")
print("  Question: can the VP running be FORMALLY mapped to a band structure?")
print()
print("  For a formal map we need:")
print("    (a) A 'lattice' in energy/momentum space")
print("    (b) A 'reciprocal lattice vector' G")
print("    (c) The running as a 'dispersion relation' E(k)")
print("    (d) Thresholds as 'zone boundaries'")
print()
print("  Attempt: define 'coupling momentum' κ = ln(μ/Λ_QCD)")
print("    Then α⁻¹(κ) = α⁻¹(κ₀) + (b/2π) × (κ - κ₀)")
print("    between thresholds, where b is the beta slope.")
print()
print("  The running between thresholds is LINEAR in κ (not periodic).")
print("  A band structure requires PERIODICITY in the momentum variable.")
print("  The VP running is NOT periodic — α⁻¹ grows monotonically with μ.")
print()
print("  The thresholds are at DIFFERENT intervals in κ:")
print("    κ(m_e) to κ(m_μ): Δκ = ln(m_μ/m_e) = ln(206.77)")
print("    κ(m_μ) to κ(m_τ): Δκ = ln(m_τ/m_μ) = ln(16.82)")
print("    These are NOT equal — no periodicity.")
print()

# Compute the actual intervals
from mpmath import mp, mpf, log as mlog
mp.dps = 30

m_e = mpf('0.511')
m_mu = mpf('105.66')
m_tau = mpf('1776.86')

dk1 = float(mlog(m_mu/m_e))
dk2 = float(mlog(m_tau/m_mu))

print(f"  Threshold intervals in log(μ) space:")
print(f"    ln(m_μ/m_e) = {dk1:.4f}")
print(f"    ln(m_τ/m_μ) = {dk2:.4f}")
print(f"    Ratio: {dk1/dk2:.4f} (NOT 1 → NOT periodic)")
print()

print("  FINDING: The VP running is NOT a band structure.")
print("  The structural parallel (Q2) holds: both have continuous")
print("  accumulation between discrete boundaries. But the VP running")
print("  lacks the periodicity required for a formal BZ mapping.")
print("  The thresholds are at unequal intervals (determined by")
print("  measured masses, not by lattice geometry).")
print()
print("  The VP running is a STAIRCASE (monotonic, unequal steps).")
print("  Band structure is a PERIODIC function (cosine, equal periods).")
print("  The parallel is an analogy, not an equivalence.")
print()
print("  STATUS: NULL — structural parallel but no formal equivalence")
print()

# ================================================================
# PHASE 2 SUMMARY
# ================================================================

print("=" * 70)
print("PHASE 2 SUMMARY: CROSS-DOMAIN CONNECTION TABLE")
print("=" * 70)
print()
print("| # | Question                           | Domains              | Result                         | Status          |")
print("|---|------------------------------------|--------------------|-------------------------------|-----------------|")
print("| 1 | Maslov = Berry in Fractions?       | BS ↔ Berry          | YES — tautological identity    | CONFIRMED       |")
print("|   |                                    |                     | μ/4 = Berry/(2π) = Berry/(8R₂)| (algebraic)     |")
print("| 2 | BZ boundary = RG threshold?        | BZ ↔ RG             | Structural parallel, not formal| PARTIAL         |")
print("|   |                                    |                     | Both have R₂, different forms  |                 |")
print("| 3 | R₂ in Berry phase?                 | Berry ↔ MATH-5      | YES — γ = 4R₂(1-cosθ)         | CONFIRMED       |")
print("|   |                                    |                     | Surface integral → R₂ (2D op) | (from Phase 1)  |")
print("| 4 | R₄ in CS computation?              | CS ↔ MATH-5         | YES — 1/(8π²) = 1/(256R₄)     | CONFIRMED       |")
print("|   |                                    |                     | 4D bulk normalization → R₄     | (from Phase 1)  |")
print("| 5 | VP running = BZ band structure?    | RG ↔ BZ             | NO — VP is monotonic, not      | NULL            |")
print("|   |                                    |                     | periodic. Thresholds unequal.  |                 |")
print("| 6 | θ=0 minimization = BZ k=0 minimum? | Theta ↔ BZ          | YES — same cosine on 8R₂-     | CONFIRMED       |")
print("|   |                                    |                     | periodic domain, min at 0      | (structural)    |")
print()
print("  Results: 4 confirmed, 1 partial, 1 null")
print()
print("  The null (Q5) is informative: VP running and BZ band structure")
print("  share the abstract pattern (continuous + discrete boundaries)")
print("  but differ in the fundamental property of periodicity.")
print("  The VP running is a staircase, not a band structure.")
print()
print("  The strongest finding: the UNIVERSAL MODULUS 8R₂ appears")
print("  in five of six domains as the phase period, and R₂ is present")
print("  in all six. The Maslov-Berry connection (Q1) and the")
print("  theta-BZ connection (Q6) are both exact identities that")
print("  become tautological when expressed in R₂ units.")
print()
print("  This points toward Phase 3 outcome (b): PARTIAL COLLAPSE.")
print("  Five 'phase-periodic' domains share modulus 8R₂.")
print("  Chern-Simons has modulus 1 (topological, not geometric).")
print("  The VP running shares R₂ but lacks periodicity.")
print()
