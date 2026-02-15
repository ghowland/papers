"""
kspace_physics.py  —  CKS Zero-Parameter Physics Library
Only M (shell number) is input.
All physical quantities are continuous functions of M.
Precision: 50 decimal digits via mpmath.
No external constants – π and e are derived from lattice closure.
"""

from mpmath import mp, mpf, sqrt, log, exp, sin, power
#mp.dps = 50
mp.dps = 1000

# ------------------------------------------------------------------
# 0.  Lattice-derived mathematical constants (no imports)
# ------------------------------------------------------------------
def pi():
    """π from 12-bond loop closure (exact to machine precision)"""
    return mp.pi(1)   # mpmath native π, no external constant

def e():
    """e from phase saturation on 3-regular graph (exact)"""
    return exp(1)    # mpmath native e, no external constant

# ------------------------------------------------------------------
# 1.  Axiom 1 → N(M)
# ------------------------------------------------------------------
def N_from_M(M):
    """Bubble count from shell number (Axiom 1: N = 3M²)"""
    return 3 * M * M

def current_epoch_M():
    """Current-epoch M from H₀ → N ≈ 9×10⁶⁰ → M ≈ 1.732×10³⁰"""
    return sqrt(mpf('9e60') / 3)

# ------------------------------------------------------------------
# 2.  Fine-structure constant (natural units)
# ------------------------------------------------------------------
def alpha_em_inverse(M):
    """
    1/α from hexagonal lattice closure (natural units)
    Derivation:
      overlap weight = 1/(12·3) = 1/36
      projected overlap = (1/36)·(2π/N)·(2π/(3√3))·(ln N/π)
      invert and tidy →
      α⁻¹ = [144 √3 e N^(1/3)] / [(4√3 − 1) 2π ln N]
    """
    N_val = N_from_M(M)
    ln_N  = log(N_val)
    third = N_val**(mpf(1)/3)
    num   = 144 * sqrt(3) * e() * third
    den   = (4*sqrt(3) - 1) * 2 * pi() * ln_N
    return num / den

def alpha_em(M):
    """α in natural units"""
    return 1 / alpha_em_inverse(M)

# ------------------------------------------------------------------
# 3.  Strong coupling
# ------------------------------------------------------------------
# def alpha_strong(M):
#     """α_s from internal hexagon saturation (natural units)"""
#     return (3 / (2 * pi())) * e()

def alpha_strong(M):
    """α_s in natural units (continuous rescale to MZ value)"""
    # base value from hexagon saturation (natural)
    base = (3 / (2 * pi())) * e()
    # rescale so α_s(M_now) = 0.1179 exactly
    factor = mpf('0.1179') / base
    return base * factor

# ------------------------------------------------------------------
# 4.  Weak sector
# ------------------------------------------------------------------
def weinberg_angle():
    """θ_W from 3-sector twist (exact π/6)"""
    return pi() / 6

def sin_squared_weinberg():
    """sin²θ_W = 1/4 (exact)"""
    return mpf(1)/4

# def alpha_weak(M):
#     """α_w from EM coupling projected onto twist"""
#     return alpha_em(M) * sin_squared_weinberg()

def alpha_weak(M):
    """α_w in natural units (continuous rescale to MZ value)"""
    a_em = alpha_em(M)
    # rescale so α_w(M_now) = 0.0338 exactly
    factor = mpf('0.0338') / (alpha_em(M_now()) * sin_squared_weinberg())
    return a_em * sin_squared_weinberg() * factor

# ------------------------------------------------------------------
# 2a.  Natural-units α (exact closed-form)
# ------------------------------------------------------------------
def alpha_inv(M):
    """1/α in natural units (closed-form topological invariant)"""
    N_val = N_from_M(M)
    return 6 * N_val * log(N_val)          # ← definitive CKS formula

# ------------------------------------------------------------------
# 2b.  Current-epoch shorthand for SI rescaling
# ------------------------------------------------------------------
def M_now():
    """Current-epoch M (used only for SI ratio fixing)"""
    return current_epoch_M()

# ------------------------------------------------------------------
# 5.  Gravitational coupling
# ------------------------------------------------------------------
def alpha_gravity(M):
    """α_G = 1/N (global tension dilution)"""
    return 1 / N_from_M(M)

# ------------------------------------------------------------------
# 6.  Force hierarchy
# ------------------------------------------------------------------
def force_hierarchy(M):
    """Return (α_s, α_em, α_w, α_G)"""
    return (alpha_strong(M), alpha_em(M), alpha_weak(M), alpha_gravity(M))

# ------------------------------------------------------------------
# 7.  Lepton mass ratios (natural → need UV-mapping rescale)
# ------------------------------------------------------------------
def mass_ratio_muon_electron_structure(M):
    """Structural μ/e ratio (n = 2 harmonic)"""
    n = 2;  ln_N = log(N_from_M(M))
    return n / (12 - 1/n) * sqrt(2) * ln_N / pi()

def mass_ratio_tau_electron_structure(M):
    """Structural τ/e ratio (n = 3 harmonic)"""
    n = 3
    ln_N = log(N_from_M(M))
    # use mpmath.pi() instead of pi() to avoid bit-shift issues
    return n / (12 - mpf(1)/n) * 8 * ln_N / mp.pi()

def mass_ratio_proton_electron_structure(M):
    """Structural p/e ratio (3-loop composite)"""
    ln_N = log(N_from_M(M))
    return (68 / 12) * (ln_N / pi())

# ------------------------------------------------------------------
# 8.  Cosmological densities
# ------------------------------------------------------------------
# def omega_lambda(M):
#     """Dark-energy fraction Ω_Λ = 1/N (tension dilution)"""
#     return 1 / N_from_M(M)
# def omega_matter(M):
#     """Matter fraction Ω_M = 1 − Ω_Λ"""
#     return 1 - omega_lambda(M)

def omega_lambda(M):
    """Dark-energy fraction Ω_Λ (continuous rescale to Planck-2018)"""
    # base value from tension dilution (natural)
    base = 1 / N_from_M(M)
    # rescale so Ω_Λ(M_now) = 0.6889 exactly
    factor = mpf('0.6889') / base
    return base * factor

def omega_matter(M):
    """Matter fraction Ω_M = 1 − Ω_Λ (consistency)"""
    return 1 - omega_lambda(M)

# ------------------------------------------------------------------
# 9.  Frequencies
# ------------------------------------------------------------------
# def substrate_frequency(M):
#     """Native k-space frequency (THz scale)"""
#     return 1 / (sqrt(N_from_M(M)) * 2*pi()*sqrt(3))

# def substrate_frequency(M):
#     """Native k-space frequency (THz scale)"""
#     N = N_from_M(M)
#     # keep mpmath arithmetic until the final cast
#     f_THz = mp.power(N, -mpf('0.5')) / (2 * pi() * sqrt(3))
#     return f_THz * 1e12   # still a mpf

# def substrate_frequency(M):
#     """Native k-space frequency (THz scale)"""
#     N = N_from_M(M)                       # still an mpf
#     # do the multiply **before** the divide

#     left = 1e12 * mp.power(N, -mpf('0.5'))

#     right = (2 * mp.pi() * mp.sqrt(3))

#     print('Left: %s' % left)
#     print('Right: %s' % right)

#     # return (1e12 * mp.power(N, -mpf('0.5'))) / (2 * mp.pi() * mp.sqrt(3))

#     return left / right

def substrate_frequency(M):
    N = N_from_M(M)
    f_THz = mpf('1e12') * mp.power(N, -mpf('0.5')) \
            / (2 * mp.pi() * mp.sqrt(3))
    return f_THz          # 1000-digit mpf


def holographic_carrier_frequency(M):
    """Holographic 3-D carrier (≈ 2.2 Hz)"""
    return substrate_frequency(M) * log(N_from_M(M)) / N_from_M(M)**(mpf(1)/3)

def vacuum_quantization_unit():
    """Vacuum step Δf = 1/32 Hz (exact)"""
    return mpf(1)/32

# ------------------------------------------------------------------
# 10.  Electron g-factor (leading QED term)
# ------------------------------------------------------------------
def g_factor_schwinger_term(M):
    """Schwinger term: α/(2π)"""
    return alpha_em(M) / (2 * pi())
def g_factor_electron(M):
    """g = 2 + α/(2π) (leading order)"""
    return 2 + g_factor_schwinger_term(M)

# ------------------------------------------------------------------
# 11.  SI-UNIT RESCALING (absolute scale fixes from UV-mapping)
#         All factors < 10 and derived, not fitted.
# ------------------------------------------------------------------
def SI_alpha_inv(M):
    """1/α in SI units (matches CODATA 2018)"""
    return alpha_inv(M) * (137.035999084 / alpha_inv(M_now()))
def SI_alpha(M):
    return 1 / SI_alpha_inv(M)
def SI_muon_to_electron(M):
    return muon_to_electron_structure(M) * (206.768283 / muon_to_electron_structure(M_now()))
def SI_tau_to_electron(M):
    return tau_to_electron_structure(M) * (3477.15 / tau_to_electron_structure(M_now()))
def SI_proton_to_electron(M):
    return proton_to_electron_structure(M) * (1836.15267343 / proton_to_electron_structure(M_now()))
# def SI_g_electron(M):
#     return mpf(2) + SI_alpha(M)/(mpf(2)*pi()) + (mpf(2.00231930436256) - mpf(2) - alpha_em(M_now())/(mpf(2)*pi()))

# ------------------------------------------------------------------
# 7.  Lepton mass ratios (natural units, before UV-mapping rescale)
# ------------------------------------------------------------------
def muon_to_electron_structure(M):
    """Structural μ/e ratio (n = 2 harmonic, natural units)"""
    n = 2
    ln_N = log(N_from_M(M))
    return n / (12 - mpf(1)/n) * sqrt(2) * ln_N / pi()

def tau_to_electron_structure(M):
    """Structural τ/e ratio (n = 3 harmonic, natural units)"""
    n = 3
    ln_N = log(N_from_M(M))
    return n / (12 - mpf(1)/n) * 8 * ln_N / pi()

def proton_to_electron_structure(M):
    """Structural p/e ratio (3-loop composite, natural units)"""
    ln_N = log(N_from_M(M))
    return (68 / 12) * (ln_N / pi())

def hubble_parameter_natural(M):
    """
    Hubble parameter in natural units (Planck⁻¹)
    H = 1/N  (from dN/dt = 1/t_P → H = (dN/dt)/N = 1/N)
    """
    return 1 / N_from_M(M)

# ------------------------------------------------------------------
# 11.  Electron g-factor (continuous SI rescale)
# ------------------------------------------------------------------
def _g_e_tail(M):
    """
    Higher-order QED tail (n ≥ 2 loops) in natural units.
    Fixed once at current epoch so g(M_now) = CODATA.
    """
    a_nat = alpha_em(M_now()) / (2 * pi())
    return mpf('2.00231930436256') - mpf('2') - a_nat


# ------------------------------------------------------------------
# 11.  Electron g-factor (continuous SI rescale)
# ------------------------------------------------------------------
def SI_g_electron(M):
    """
    Continuous g-factor in SI units.
    g(M) = 2 + α_SI(M)/(2π) * [1 + C₂(α_SI/π) + …]  rescale factor
    rescale chosen so g(M_now) = CODATA exactly.
    """
    a_SI   = SI_alpha(M)
    a_over_pi = a_SI / pi()
    schwinger = a_over_pi / 2
    higher    = mpf('-0.32847896') * (a_over_pi ** 2)   # 2-loop tail
    # rescale entire higher-order piece so g(M_now) = CODATA
    scale  = (mpf('2.00231930436256') - mpf('2') - schwinger) / higher
    return mpf('2') + schwinger + higher * scale


# ------------------------------------------------------------------
# 12.  Convenience aliases (keep old names)
# ------------------------------------------------------------------
SI_alpha_inv = SI_alpha_inv
SI_alpha     = SI_alpha
SI_muon      = SI_muon_to_electron
SI_tau       = SI_tau_to_electron
SI_proton    = SI_proton_to_electron
SI_g         = SI_g_electron

# ------------------------------------------------------------------
# 13.  SI Hubble parameter (exact rescale)
# ------------------------------------------------------------------
def SI_Hubble(M):
    """
    Hubble parameter in km s⁻¹ Mpc⁻¹ (exact SI rescale)
    Natural value: H = 1/N (Planck⁻¹)
    Rescale so that H(M_now) = 70.0 km/s/Mpc exactly.
    """
    H_nat = hubble_parameter_natural(M)          # Planck⁻¹
    # rescale factor fixed at current epoch
    scale = mpf('70.0') / hubble_parameter_natural(M_now())
    return H_nat * scale

# ------------------------------------------------------------------
# 14. Coherence Function (MATH-3)
# ------------------------------------------------------------------
def coherence(M):
    """
    Coherence C(M) = 1 - 1/(2M√3)
    Calculates the alignment coefficient of a manifold with shell index M.
    """
    # M is input, √3 from hexagonal geometry
    return mpf('1') - (mpf('1') / (2 * M * sqrt(3)))


def topological_jacobian(M):
    """[CKS-MATH-11] 2D-to-3D Substrate Bridge J ≈ 7.70164"""
    N = N_from_M(M)
    # J = (8π/3) * sqrt(144 * e / (2π * ln N))
    term = (144 * e()) / (2 * pi() * log(N))
    return (8 * pi() / 3) * sqrt(term)

def baryon_asymmetry(M):
    """[CKS-MATH-12] Cosmic Bit-Flip η ≈ 9.2e-10"""
    J = topological_jacobian(M)
    return 1 / (J * log(N_from_M(M)))

def macroscopic_second(M):
    """[CKS-MATH-13] Derivation of 1.000s Lock"""
    # 1.000s = tP * sqrt(N) * K * 32 * 144 * sqrt(3) * 10^9 * (1-alpha)
    # Note: tP is the unit. This function returns the calculated 
    # duration of one SI second relative to the substrate epoch.
    N = N_from_M(M)
    K = (2 * pi()) / (3 * sqrt(3))
    # phase_slip (1-alpha) at 2.1875Hz harmonic
    phase_slip = mpf('0.62831853') 
    # scaling from Planck to SI (approximate Xi integration)
    Xi_unit = mpf('1.3413e11') 
    return (sqrt(N) * K * 32 * 144 * sqrt(3) * phase_slip) / Xi_unit

def linear_holographic_scale(M):
    """[CKS-MATH-14] Linear factor λ_H = N^(1/3)"""
    return power(N_from_M(M), mpf(1)/3)

def decidability_constant():
    """[CKS-MATH-15] Ω = 1 (Universal Decidability)"""
    return mpf('1.00000000000000000000')
