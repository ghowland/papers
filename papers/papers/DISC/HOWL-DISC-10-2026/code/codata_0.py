#!/usr/bin/env python3
"""
CODATA Constants Mapped to Nine Remainder Domains
===================================================

For each domain: which CODATA constants appear, at what precision,
and what dimensionless ratios can be formed from them?

This is the extraction we DIDN'T do — populating the domain
equations with real measured values instead of unit placeholders.
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msq, pi as mpi, log as mlog

mp.dps = 50

print("=" * 75)
print("CODATA 2022 CONSTANTS MAPPED TO NINE REMAINDER DOMAINS")
print("=" * 75)
print()

# ================================================================
# CODATA 2022 EXACT (SI-defined) CONSTANTS
# ================================================================

print("TIER 1: EXACT SI-DEFINED CONSTANTS")
print()

exact = {
    'c':     299792458,                    # m/s
    'h':     mpf('6.62607015e-34'),        # J·Hz⁻¹
    'hbar':  mpf('1.054571817e-34'),       # J·s (exact: h/2π)
    'e':     mpf('1.602176634e-19'),       # C
    'k_B':   mpf('1.380649e-23'),          # J/K
    'N_A':   mpf('6.02214076e23'),         # mol⁻¹
}

print("  c     = 299792458 m/s (exact)")
print("  h     = 6.62607015e-34 J·Hz⁻¹ (exact)")
print("  hbar  = 1.054571817...e-34 J·s (exact = h/(2π))")
print("  e     = 1.602176634e-19 C (exact)")
print()

# ================================================================
# CODATA 2022 MEASURED CONSTANTS (with uncertainties)
# ================================================================

print("TIER 2: CODATA 2022 MEASURED CONSTANTS")
print()

measured = {
    'alpha_inv':  (mpf('137.035999177'),   mpf('0.000000021'),  '1.6e-10'),
    'm_e':        (mpf('9.1093837139e-31'), mpf('0.0000000028e-31'), '3.1e-10'),
    'm_e_MeV':    (mpf('0.51099895069'),   mpf('0.00000000016'),  '3.1e-10'),
    'm_mu_MeV':   (mpf('105.6583755'),     mpf('0.0000023'),      '2.2e-8'),
    'm_tau_MeV':  (mpf('1776.86'),         mpf('0.12'),            '6.8e-5'),
    'm_p':        (mpf('1.67262192595e-27'), mpf('0.00000000052e-27'), '3.1e-10'),
    'm_p_m_e':    (mpf('1836.15267343'),   mpf('0.00000032'),      '1.7e-11'),
    'R_inf':      (mpf('10973731.568157'),  mpf('0.000012'),       '1.1e-12'),
    'a_0':        (mpf('5.29177210544e-11'), mpf('0.00000000082e-11'), '1.6e-10'),
    'K_J':        (mpf('483597.8484e9'),    mpf(0),                 'exact'),
    'R_K':        (mpf('25812.80745'),      mpf(0),                 'exact'),
    'mu_0':       (mpf('1.25663706127e-6'), mpf('0.00000000020e-6'), '1.6e-10'),
    'eps_0':      (mpf('8.8541878188e-12'), mpf('0.0000000014e-12'), '1.6e-10'),
}

print(f"  {'Constant':<16} {'Value':>24} {'Uncert':>14} {'Rel (ppb)':>10}")
print(f"  {'-'*16} {'-'*24} {'-'*14} {'-'*10}")
for name, (val, unc, rel) in measured.items():
    print(f"  {name:<16} {mp.nstr(val,12):>24} {mp.nstr(unc,4):>14} {rel:>10}")

print()

# ================================================================
# DOMAIN-BY-DOMAIN MAPPING
# ================================================================

alpha_inv = measured['alpha_inv'][0]
alpha = 1 / alpha_inv
m_e = measured['m_e_MeV'][0]
m_mu = measured['m_mu_MeV'][0]
m_tau = measured['m_tau_MeV'][0]
m_p_m_e = measured['m_p_m_e'][0]
R_inf = measured['R_inf'][0]
a_0 = measured['a_0'][0]

print("=" * 75)
print("DOMAIN 1: THETA VACUUM")
print("=" * 75)
print()
print("  E(θ) = E₀ - χ_top cos(θ)")
print("  CODATA constants involved: NONE directly.")
print("  θ_QCD = 0 is derived from topology, not from measured constants.")
print("  The topological susceptibility χ_top ~ (180 MeV)⁴ is from lattice QCD,")
print("  not a CODATA constant.")
print()
print("  Dimensionless ratios: none. This domain is parameter-free.")
print()

print("=" * 75)
print("DOMAIN 2: RG RUNNING")
print("=" * 75)
print()
print("  α⁻¹(μ) = α⁻¹(m_e) + (1/3π) Σ Q_f² ln(μ²/m_f²)")
print()
print("  CODATA constants:")
print(f"    α⁻¹         = {alpha_inv} ± {measured['alpha_inv'][1]}")
print(f"    m_e          = {m_e} MeV ± {measured['m_e_MeV'][1]}")
print(f"    m_μ          = {m_mu} MeV ± {measured['m_mu_MeV'][1]}")
print(f"    m_τ          = {m_tau} MeV ± {measured['m_tau_MeV'][1]}")
print()

# Dimensionless ratios from this domain
m_mu_m_e = m_mu / m_e
m_tau_m_e = m_tau / m_e
m_tau_m_mu = m_tau / m_mu

print("  Dimensionless ratios (from CODATA):")
print(f"    m_μ/m_e  = {m_mu_m_e}")
print(f"    m_τ/m_e  = {m_tau_m_e}")
print(f"    m_τ/m_μ  = {m_tau_m_mu}")
print()

# The VP running steps
# Each threshold contributes (Q²/3π) × ln(μ²/m_f²)
# Between m_e and m_μ: Δα⁻¹ = (1/3π) × ln(m_μ²/m_e²)
step_e_to_mu = mlog(m_mu**2 / m_e**2) / (3 * mpi)
step_mu_to_tau = mlog(m_tau**2 / m_mu**2) / (3 * mpi)
total_lep = step_e_to_mu + step_mu_to_tau

print("  VP running steps (leptonic, Q=1):")
print(f"    m_e → m_μ:  Δα⁻¹ = (1/3π)ln(m_μ²/m_e²) = {float(step_e_to_mu):.8f}")
print(f"    m_μ → m_τ:  Δα⁻¹ = (1/3π)ln(m_τ²/m_μ²) = {float(step_mu_to_tau):.8f}")
print(f"    Total leptonic:                              {float(total_lep):.8f}")
print()

# What α⁻¹ would be at m_τ with just leptonic running
alpha_inv_at_tau = alpha_inv - total_lep  # running DOWN from infinity
print(f"  α⁻¹ at m_τ (leptonic only): {float(alpha_inv - total_lep):.6f}")
print(f"  (This is NOT α⁻¹(m_τ) — hadronic VP not included)")
print()

print("=" * 75)
print("DOMAIN 3: BOHR-SOMMERFELD")
print("=" * 75)
print()
print("  E_n = ℏω(n + 1/2) for harmonic oscillator")
print("  E_n = n²π²ℏ²/(2mL²) for particle in box")
print()
print("  CODATA constants for HYDROGEN (the real BS system):")
print(f"    R_∞     = {R_inf} m⁻¹ ± {measured['R_inf'][1]}")
print(f"    a_0     = {a_0} m ± {measured['a_0'][1]}")
print(f"    α⁻¹     = {alpha_inv}")
print(f"    m_p/m_e = {m_p_m_e}")
print()

# Hydrogen energy levels: E_n = -R_∞ hc / n² = -α² m_e c² / (2n²)
# The Rydberg: R_∞ = α² m_e c / (2h) = α² / (4π a_0)
# Bohr radius: a_0 = ℏ/(m_e c α) = 1/(α m_e c / ℏ)

# Dimensionless ratios
# E_n / (m_e c²) = -α² / (2n²)
# This is a RATIO of the hydrogen binding energy to the electron rest mass
# It depends on α alone (a free parameter)

for n in [1, 2, 3, 4]:
    E_ratio = -alpha**2 / (2 * n**2)
    print(f"    E_{n}/(m_e c²) = -α²/(2×{n}²) = {float(E_ratio):.12f}")

print()
print("  The hydrogen energies depend on exactly ONE free parameter: α.")
print("  The BS decomposition: E_n = modulus × (n + remainder)")
print("  gives modulus = α² m_e c² / 2 = R_∞ hc (depends on α)")
print("  and remainder = 0 (for hydrogen, the BS correction is in n).")
print()

print("=" * 75)
print("DOMAIN 4: BERRY PHASE")
print("=" * 75)
print()
print("  γ = 4R₂(1 - cosθ) for spin-1/2 in rotating B field")
print()
print("  CODATA constants: NONE for the geometric phase itself.")
print("  Berry phase depends on the geometry of parameter space,")
print("  not on any measured constant.")
print()
print("  However: the QUANTUM HALL EFFECT connects Berry phase to α.")
print("  Hall conductance σ_xy = (e²/h) × C where C is the Chern number.")
print(f"  e²/h = 1/R_K = {float(1/measured['R_K'][0]):.10e} S")
print(f"  R_K = h/e² = {measured['R_K'][0]} Ω (exact in SI)")
print()
print("  The quantized Hall conductance is e²/h per Landau level.")
print("  This is exact — it depends on NO free parameters (e and h are defined).")
print()

print("=" * 75)
print("DOMAIN 5: BRILLOUIN ZONE")
print("=" * 75)
print()
print("  E(k) = -2t cos(ka), G = 2π/a")
print()
print("  CODATA constants for REAL MATERIALS:")
print(f"    Silicon lattice: a = 5.43102064 Å (from CODATA d₂₂₀)")
print(f"    a_0 = {a_0} m (Bohr radius, sets atomic scale)")
print()
print("  The lattice constant a is material-specific, not a fundamental constant.")
print("  The hopping parameter t depends on the material's electronic structure.")
print("  No SM free parameter enters the BZ structure directly.")
print()
print("  However: the lattice constant in terms of Bohr radii")
print(f"    a_Si / a_0 = {float(mpf('5.43102064e-10') / a_0):.6f}")
print("  This ratio depends on α (through a_0) and on silicon's atomic physics.")
print()

print("=" * 75)
print("DOMAIN 6: CHERN-SIMONS")
print("=" * 75)
print()
print("  CS(A) mod Z, normalization 1/(8π²) = 1/(256R₄)")
print()
print("  CODATA constants: NONE for the CS invariant itself.")
print("  CS values for flat connections are pure rationals.")
print()
print("  The CONNECTION to SM: the QCD coupling g enters the instanton action")
print("  S = 8π²/g² = 256R₄/g² where g² = 4πα_s.")
print(f"    α_s(M_Z) = 0.1180 ± 0.0009 (from PDG, not CODATA)")
print(f"    g² = 4πα_s = {float(4*mpi*mpf('0.1180')):.6f}")
print(f"    S = 256R₄/g² = {float(256*mpi**2/32 / (4*mpi*mpf('0.1180'))):.4f}")
print()

print("=" * 75)
print("DOMAIN 7: AHARONOV-BOHM")
print("=" * 75)
print()
print("  δφ = 2πΦ/Φ₀ where Φ₀ = h/e")
print()
print("  CODATA constants:")
print(f"    Φ₀ = h/e = {float(exact['h']/exact['e']):.10e} Wb")
print("    (This is EXACT in SI — both h and e are defined.)")
print()
print("  The AB phase depends on the enclosed flux Φ,")
print("  which is an experimental parameter, not a free SM constant.")
print("  No SM free parameter enters.")
print()

print("=" * 75)
print("DOMAIN 8: FLUX QUANTIZATION")
print("=" * 75)
print()
print("  Φ = nΦ₀/2 where Φ₀/2 = h/(2e)")
print()
print("  CODATA constants:")
print(f"    Φ₀/2 = h/(2e) = {float(exact['h']/(2*exact['e'])):.10e} Wb")
print("    (EXACT in SI)")
print()
print("  No SM free parameter. The flux quantum is a ratio of defined constants.")
print()

print("=" * 75)
print("DOMAIN 9: AC JOSEPHSON")
print("=" * 75)
print()
print("  f_J = 2eV/h, K_J = 2e/h")
print()
print("  CODATA constants:")
print(f"    K_J = 2e/h = {float(2*exact['e']/exact['h']):.4f} Hz/V")
print("    (EXACT in SI)")
print()
print("  The Josephson constant is a ratio of defined constants.")
print("  The frequency depends on the applied voltage V (experimental, not SM).")
print("  No SM free parameter enters.")
print()

# ================================================================
# SUMMARY: WHICH DOMAINS ACCESS SM FREE PARAMETERS?
# ================================================================

print("=" * 75)
print("SUMMARY: SM FREE PARAMETERS BY DOMAIN")
print("=" * 75)
print()

print("| Domain          | SM free params accessed | CODATA precision | New ratios? |")
print("|-----------------|----------------------|------------------|-------------|")
print("| 1. Theta vacuum | None (topological)    | N/A              | No          |")
print("| 2. RG running   | α, m_e, m_μ, m_τ     | 0.16-68 ppm      | YES (steps) |")
print("| 3. Bohr-Sommer. | α (through R_∞, a_0)  | 0.16 ppb         | YES (E_n/m_ec²)|")
print("| 4. Berry phase  | None (geometric)      | N/A              | No          |")
print("| 5. Brillouin    | None (material-spec.)  | N/A              | No          |")
print("| 6. Chern-Simons | α_s (through g²)      | 0.76%            | YES (S_inst)|")
print("| 7. Aharonov-Bohm| None (Φ experimental) | N/A              | No          |")
print("| 8. Flux quant.  | None (exact SI)       | N/A              | No          |")
print("| 9. AC Josephson | None (exact SI)       | N/A              | No          |")
print()
print("FINDING: Only 3 of 9 domains access SM free parameters:")
print("  Domain 2 (RG): α and lepton masses")
print("  Domain 3 (BS): α alone (through hydrogen)")
print("  Domain 6 (CS): α_s (through instanton action)")
print()
print("The other 6 domains are either topological (theta vacuum),")
print("geometric (Berry phase), material-specific (BZ), or exact SI")
print("(AB, flux, Josephson). They contain NO SM free parameters.")
print()
print("This explains why the domain extractions didn't help with")
print("parameter reduction: most domains don't contain the parameters.")
print("The parameters live in Domain 2 (RG running) and Domain 6 (CS),")
print("which is where PHYS-5, PHYS-9, and the search program already looked.")
print()

# ================================================================
# THE DIMENSIONLESS RATIOS WE CAN FORM
# ================================================================

print("=" * 75)
print("DIMENSIONLESS RATIOS FROM CODATA (by domain)")
print("=" * 75)
print()

print("DOMAIN 2 (RG running):")
print()
print("  Lepton mass ratios (CODATA 2022):")
print(f"    m_μ/m_e   = {float(m_mu/m_e):.10f}  (± {float(measured['m_mu_MeV'][1]/m_e):.6f})")
print(f"    m_τ/m_e   = {float(m_tau/m_e):.6f}  (± {float(measured['m_tau_MeV'][1]/m_e):.4f})")
print(f"    m_τ/m_μ   = {float(m_tau/m_mu):.8f}  (± {float(measured['m_tau_MeV'][1]/m_mu):.6f})")
print()

print("  VP running steps (dimensionless):")
print(f"    Δα⁻¹(m_e→m_μ)  = {float(step_e_to_mu):.10f}")
print(f"    Δα⁻¹(m_μ→m_τ)  = {float(step_mu_to_tau):.10f}")
print(f"    Ratio of steps  = {float(step_e_to_mu/step_mu_to_tau):.8f}")
print()

print("  Log mass ratios (appear in VP steps):")
print(f"    ln(m_μ/m_e)  = {float(mlog(m_mu/m_e)):.10f}")
print(f"    ln(m_τ/m_μ)  = {float(mlog(m_tau/m_mu)):.10f}")
print(f"    ln(m_τ/m_e)  = {float(mlog(m_tau/m_e)):.10f}")
print()

print("DOMAIN 3 (Bohr-Sommerfeld / Hydrogen):")
print()
print(f"    α           = {float(alpha):.12e}")
print(f"    α²          = {float(alpha**2):.12e}")
print(f"    α²/2        = {float(alpha**2/2):.12e} (E_1/m_ec²)")
print(f"    m_p/m_e     = {float(m_p_m_e):.10f}")
print(f"    Reduced mass correction: m_e/(m_e+m_p) = 1/(1+m_e/m_p)")
print(f"                = {float(1/(1+1/m_p_m_e)):.12f}")
print()

print("DOMAIN 6 (Chern-Simons / Instanton):")
print()
alpha_s = mpf('0.1180')
g2 = 4 * mpi * alpha_s
S_inst = 8 * mpi**2 / g2
print(f"    α_s         = {alpha_s} ± 0.0009")
print(f"    g²=4πα_s    = {float(g2):.8f}")
print(f"    S=8π²/g²    = {float(S_inst):.6f}")
print(f"    S/(2π)      = {float(S_inst/(2*mpi)):.6f}")
print(f"    S/256       = {float(S_inst/256):.8f} (= R₄/g²)")
print()

# ================================================================
# THE KEY QUESTION
# ================================================================

print("=" * 75)
print("ASSESSMENT")
print("=" * 75)
print()
print("We ALREADY used the high-precision CODATA data where it matters:")
print("  - PHYS-5/9: α from a_e using CODATA m_e, m_μ, m_τ")
print("  - PHYS-10: α⁻¹ = 137.035999177 (CODATA 2022)")
print("  - Modular search: all 17 SM targets at CODATA precision")
print()
print("What we DIDN'T do: extract real physical quantities from")
print("each domain using CODATA inputs. But the table above shows")
print("WHY we didn't: 6 of 9 domains have NO SM free parameters.")
print("They use exact SI constants or material-specific quantities.")
print()
print("The SM parameters concentrate in Domain 2 (RG running)")
print("and Domain 6 (CS/instanton). These are exactly the domains")
print("where we already did the most work (PHYS-5, PHYS-9, PHYS-10).")
print()
print("CONCLUSION: Populating the domains with CODATA values confirms")
print("what DISC-9 argues — the framework structure is independent of")
print("parameter values. Most domains don't even CONTAIN the parameters.")
print("The parameters live in the running (Domain 2) and the coupling")
print("(Domain 6), which is where the search already looked and returned null.")
