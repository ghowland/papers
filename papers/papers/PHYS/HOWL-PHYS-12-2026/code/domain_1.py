#!/usr/bin/env python3
"""
Precision Dimensionless Constants from the Hard Sciences
=========================================================

Beyond physics: what do the other sciences measure precisely?
Which of their constants are dimensionless, unexplained, and
measured to enough precision to test against the transcendental basis?
"""

from mpmath import mp, mpf, pi as mpi, log as mlog, zeta, sqrt as msq, e as me
mp.dps = 50

print("=" * 75)
print("PRECISION DIMENSIONLESS CONSTANTS: THE HARD SCIENCES")
print("=" * 75)
print()

# ================================================================
# CATEGORY 1: TURBULENCE & FLUID MECHANICS
# ================================================================

print("CATEGORY 1: TURBULENCE / FLUID MECHANICS")
print()
print("| Constant                  | Value         | Precision | Derived? |")
print("|---------------------------|---------------|-----------|----------|")
print("| von Kármán κ              | 0.40 ± 0.02   | 5%        | NO       |")
print("| Kolmogorov C_K            | 1.5 ± 0.1     | 7%        | NO       |")
print("| Smagorinsky C_S           | 0.1-0.2       | ~50%      | NO       |")
print("| Re_crit (pipe)            | ~2300         | ~10%      | NO       |")
print("| Re_crit (flat plate)      | ~5×10⁵        | ~20%      | NO       |")
print("| Drag coeff sphere Re=0    | 24/Re (exact) | exact     | YES      |")
print("| Stokes drag               | 6π (exact)    | exact     | YES      |")
print()
print("  VERDICT: Too imprecise for PSLQ (need 10+ digits).")
print("  The unexplained constants (κ, C_K, Re_crit) are known")
print("  to only 2-3 significant figures. Can't test meaningfully.")
print()

# ================================================================
# CATEGORY 2: CHEMISTRY — MOLECULAR SPECTROSCOPY
# ================================================================

print("CATEGORY 2: CHEMISTRY / MOLECULAR SPECTROSCOPY")
print()

# Molecular constants measured to high precision
# These are fundamentally derived from α, m_e/m_p, and nuclear physics
print("| Constant                        | Value              | Precision | Derived from   |")
print("|---------------------------------|--------------------|-----------|----------------|")
print("| H₂ dissociation energy          | 36118.0696(4) cm⁻¹| 1.1e-8    | α, m_e/m_p     |")
print("| H₂ vibration freq ν₁            | 4161.166 cm⁻¹     | 1e-6      | α, m_e/m_p     |")
print("| CO rotation const B₀            | 57635.968 MHz      | 1e-7      | α, m_e/m_p,m_C |")
print("| N₂ dissociation                 | 78714 cm⁻¹         | ~0.01%    | α, nuclear     |")
print()
print("  VERDICT: High precision available but all DERIVED from α and")
print("  nuclear masses. These don't contain new free parameters.")
print("  Testing them tests many-body quantum chemistry, not SM constants.")
print()

# ================================================================
# CATEGORY 3: CRYSTALLOGRAPHY
# ================================================================

print("CATEGORY 3: CRYSTALLOGRAPHY / MATERIALS")
print()
print("| Constant                  | Value            | Precision | Derived? |")
print("|---------------------------|------------------|-----------|----------|")
print("| Si lattice constant       | 5.43102064(14) Å | 2.6e-8    | Yes (α)  |")
print("| Ge lattice constant       | 5.65735 Å        | ~1e-5     | Yes (α)  |")
print("| c/a ratio hcp metals      | ~1.633           | varies    | geometry |")
print("| ideal c/a (hcp)           | √(8/3)=1.6330..  | exact     | YES      |")
print("| Au c/a actual             | 1.0000 (fcc)     | exact     | symmetry |")
print()

# The ideal c/a ratio for hexagonal close packing
ca_ideal = msq(mpf(8)/3)
print(f"  Ideal hcp c/a = √(8/3) = {float(ca_ideal):.10f}")
print(f"  = 2√(2/3) = 2×{float(msq(mpf(2)/3)):.10f}")
print()

# Actual c/a ratios for hcp metals — deviations from ideal
hcp_metals = {
    'Be':  1.568, 'Mg': 1.624, 'Ti': 1.588, 'Co': 1.623,
    'Zn':  1.856, 'Zr': 1.593, 'Cd': 1.886, 'Hf': 1.581,
}
print(f"  {'Metal':<6} {'c/a':>8} {'c/a - ideal':>12} {'Ratio to ideal':>14}")
for metal, ca in hcp_metals.items():
    dev = ca - float(ca_ideal)
    ratio = ca / float(ca_ideal)
    print(f"  {metal:<6} {ca:>8.3f} {dev:>12.4f} {ratio:>14.6f}")

print()
print("  VERDICT: The deviations from ideal are determined by")
print("  electronic structure (d-orbital filling, spin-orbit coupling)")
print("  which depends on α and nuclear charges. Material-specific,")
print("  not SM free parameters.")
print()

# ================================================================
# CATEGORY 4: MATHEMATICAL CONSTANTS (pure math)
# ================================================================

print("CATEGORY 4: MATHEMATICAL CONSTANTS")
print()
print("  These are not measured — they are computed to arbitrary precision.")
print("  But some ratios between them are unexplained.")
print()

# Feigenbaum constants (universal in chaos theory)
delta_F = mpf('4.669201609102990671853203820466')  # Feigenbaum δ
alpha_F = mpf('2.502907875095892822283902873218')  # Feigenbaum α

print(f"  Feigenbaum δ = {delta_F}")
print(f"  Feigenbaum α = {alpha_F}")
print()

# Test these against our basis
pool = [
    ("1", mpf(1)), ("pi", mpi), ("pi^2", mpi**2), ("e", me),
    ("ln2", mlog(2)), ("sqrt2", msq(2)), ("sqrt3", msq(3)),
    ("phi", (1+msq(5))/2), ("zeta3", zeta(3)), ("zeta5", zeta(5)),
]

print("  PSLQ: Feigenbaum δ against 10-constant basis")
for maxc in [100, 1000]:
    vec = [delta_F] + [v for _, v in pool]
    result = mp.pslq(vec, maxcoeff=maxc)
    if result and result[0] != 0:
        terms = [f"({result[i+1]})*{n}" for i,(n,_) in enumerate(pool) if result[i+1]!=0]
        print(f"    maxcoeff={maxc}: HIT — {result[0]}*δ + {' + '.join(terms)} = 0")
    else:
        print(f"    maxcoeff={maxc}: null")

print()
print("  PSLQ: Feigenbaum α against 10-constant basis")
for maxc in [100, 1000]:
    vec = [alpha_F] + [v for _, v in pool]
    result = mp.pslq(vec, maxcoeff=maxc)
    if result and result[0] != 0:
        terms = [f"({result[i+1]})*{n}" for i,(n,_) in enumerate(pool) if result[i+1]!=0]
        print(f"    maxcoeff={maxc}: HIT — {result[0]}*α + {' + '.join(terms)} = 0")
    else:
        print(f"    maxcoeff={maxc}: null")

print()

# ================================================================
# CATEGORY 5: COSMOLOGY
# ================================================================

print("CATEGORY 5: COSMOLOGY")
print()
print("| Constant                  | Value           | Precision | Free param? |")
print("|---------------------------|-----------------|-----------|-------------|")
print("| Hubble H₀                | 67.4 ± 0.5 km/s/Mpc| 0.7%   | YES         |")
print("| CMB temperature T₀       | 2.72548 ± 0.00057 K| 0.02%   | YES         |")
print("| Baryon density Ω_b h²    | 0.02237 ± 0.00015 | 0.7%    | YES         |")
print("| DM density Ω_c h²        | 0.1200 ± 0.0012   | 1%      | YES         |")
print("| Spectral index n_s       | 0.9649 ± 0.0042   | 0.4%    | YES         |")
print("| Amplitude ln(10¹⁰A_s)   | 3.044 ± 0.014     | 0.5%    | YES         |")
print()
print("  VERDICT: These ARE free parameters (cosmological, not SM).")
print("  Precision: 2-4 significant figures. Marginal for PSLQ.")
print("  But Ω_c h² = 0.1200 ± 0.0012 is suspiciously close to α_s!")
print()

omega_c = mpf('0.1200')
alpha_s = mpf('0.1180')
print(f"  Ω_c h² = {omega_c}")
print(f"  α_s    = {alpha_s}")
print(f"  Ratio: {float(omega_c/alpha_s):.6f}")
print(f"  Difference: {float(omega_c - alpha_s):.4f}")
print(f"  Both ~0.12. Coincidence at 2% level. Not meaningful")
print(f"  without a physical mechanism linking DM density to QCD.")
print()

# ================================================================
# CATEGORY 6: ASTROPHYSICS / NUCLEAR
# ================================================================

print("CATEGORY 6: NUCLEAR PHYSICS / ASTROPHYSICS")
print()
print("| Constant                   | Value          | Precision | Status    |")
print("|----------------------------|----------------|-----------|-----------|")
print("| Proton-to-electron mass    | 1836.15267343  | 1.7e-11   | CODATA    |")
print("| Neutron-proton mass diff   | 1.29333236(46) MeV| 3.6e-7  | CODATA    |")
print("| Deuteron binding energy    | 2.22456614(42) MeV| 1.9e-7  | CODATA    |")
print("| Helium-4 binding/nucleon   | 7.07392 MeV    | 1e-5      | Nuclear   |")
print("| Triple-alpha resonance     | 7.6542(12) MeV | 1.6e-4    | Nuclear   |")
print()

# The proton-electron mass ratio is THE most precisely known mass ratio
m_p_m_e = mpf('1836.15267343')
print(f"  m_p/m_e = {m_p_m_e} (11 significant figures)")
print()

# PSLQ on m_p/m_e
print("  PSLQ: m_p/m_e against 10-constant basis")
for maxc in [1000, 10000]:
    vec = [m_p_m_e] + [v for _, v in pool]
    result = mp.pslq(vec, maxcoeff=maxc)
    if result and result[0] != 0:
        terms = [f"({result[i+1]})*{n}" for i,(n,_) in enumerate(pool) if result[i+1]!=0]
        print(f"    maxcoeff={maxc}: HIT — {result[0]}*m_p/m_e + {' + '.join(terms)} = 0")
    else:
        print(f"    maxcoeff={maxc}: null")

print()

# Neutron-proton mass difference as fraction of proton mass
mn_mp = mpf('1.29333236') / mpf('938.272089')  # MeV / MeV
print(f"  (m_n - m_p)/m_p = {float(mn_mp):.10e}")
print(f"  This determines: beta decay, nucleosynthesis, existence of atoms")
print(f"  It depends on: m_d - m_u (quark mass difference) + QED + QCD")
print()

# ================================================================
# SUMMARY
# ================================================================

print("=" * 75)
print("SUMMARY: WHAT THE HARD SCIENCES OFFER")
print("=" * 75)
print()
print("| Category          | Precision  | New free params? | Testable? |")
print("|-------------------|------------|------------------|-----------|")
print("| Turbulence        | 2-3 digits | No (emergent)    | NO        |")
print("| Molecular spectra | 6-8 digits | No (from α)      | Redundant |")
print("| Crystallography   | 5-8 digits | No (from α, Z)   | Redundant |")
print("| Math constants    | arbitrary  | N/A (not physics) | YES *     |")
print("| Cosmology         | 2-4 digits | YES (6 params)   | Marginal  |")
print("| Nuclear physics   | 7-11 digits| Partially (m_q)  | YES       |")
print()
print("* Feigenbaum constants: PSLQ null against our basis")
print()
print("THREE GENUINELY NEW THINGS TO TEST:")
print()
print("  1. m_p/m_e = 1836.153 (11 digits, PSLQ null at maxcoeff 10000)")
print("     This is the most precise mass ratio in physics.")
print("     It depends on QCD (proton mass) and QED (electron mass).")
print("     It's NOT a simple function of transcendentals.")
print()
print("  2. Cosmological parameters (Ω_b, Ω_c, n_s, H₀, T₀)")
print("     These ARE free parameters, different from SM's 18.")
print("     Precision is marginal (2-4 digits) but improving.")
print("     The CMB temperature T₀ = 2.72548 K is the most precise.")
print()
print("  3. Nuclear binding energies (deuteron: 2.224566 MeV)")
print("     These depend on quark masses and α_s through QCD.")
print("     They're derived quantities but the derivation is")
print("     from lattice QCD — a different path than perturbative QED.")
print()
print("BOTTOM LINE:")
print("  The hard sciences outside physics offer mostly DERIVED quantities")
print("  (from α and nuclear charges) at insufficient precision.")
print("  The exceptions are cosmological parameters (new free params,")
print("  low precision) and nuclear masses (high precision, but")
print("  derived from QCD which we already tested through α_s).")
print()
print("  The von Kármán constant and other turbulence parameters")
print("  are intriguing UNKNOWNS but at 2-3 digit precision,")
print("  PSLQ and modular search cannot operate.")

