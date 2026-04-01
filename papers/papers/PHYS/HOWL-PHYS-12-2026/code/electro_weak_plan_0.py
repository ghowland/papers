#!/usr/bin/env python3
"""
HOWL Electroweak Overconstrained System — Tree + Leading Δρ
=============================================================

Compute all LEP Z-pole observables from 7 SM inputs in Fraction
arithmetic. Extract sin²θ_W from asymmetries and α_s from R_l.
Compare extracted to input values.

Inputs (DATA-2 Fractions):
  G_F, M_Z, alpha^-1, sin2_thetaW, alpha_s, m_t, m_H

Outputs (13 observables):
  Gamma_l, Gamma_nu, Gamma_had, Gamma_Z, R_l, R_b, R_c,
  sigma0_had, A_FB_l, A_l, N_nu, Gamma_inv, M_W (prediction)

Method: Tree level + leading Δρ correction.
Expected agreement with LEP data: ~1-3%.
"""

from fractions import Fraction
from mpmath import mp, mpf, sqrt as msqrt, pi as mpi

mp.dps = 100

def f2m(f):
    return mpf(f.numerator) / mpf(f.denominator)

# ================================================================
# Q335 BASIS
# ================================================================

Q = 2**335
p_pi = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314
p_sqrt2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506

pi_frac = Fraction(p_pi, Q)
sqrt2_frac = Fraction(p_sqrt2, Q)

# ================================================================
# DATA-2 INPUTS (7 measured rationals)
# ================================================================

G_F     = Fraction(11663788, 10**12)        # 1.1663788e-5 GeV^-2
M_Z     = Fraction(911876, 10)              # 91187.6 MeV
alpha_inv = Fraction(137035999177, 10**9)   # 137.035999177
s2w     = Fraction(23122, 100000)           # sin^2(theta_W) = 0.23122
alpha_s = Fraction(1180, 10000)             # 0.1180
m_t     = Fraction(172570, 1)              # 172570 MeV
m_H     = Fraction(125200, 1)             # 125200 MeV

alpha_em = Fraction(1, 1) / alpha_inv      # ~ 1/137.036

# ================================================================
# DATA-2 MEASURED OBSERVABLES (for comparison)
# ================================================================

meas = {
    'Gamma_Z':    (Fraction(24952, 10),    Fraction(23, 10)),       # 2495.2 ± 2.3 MeV
    'Gamma_l':    (Fraction(83984, 1000),   Fraction(86, 1000)),    # 83.984 ± 0.086 MeV
    'Gamma_inv':  (Fraction(4990, 10),      Fraction(15, 10)),      # 499.0 ± 1.5 MeV
    'sigma0_had': (Fraction(41481, 1000),   Fraction(37, 1000)),    # 41.481 ± 0.037 nb
    'R_l':        (Fraction(20767, 1000),   Fraction(25, 1000)),    # 20.767 ± 0.025
    'R_b':        (Fraction(21629, 100000), Fraction(66, 100000)),  # 0.21629 ± 0.00066
    'R_c':        (Fraction(1721, 10000),   Fraction(30, 10000)),   # 0.1721 ± 0.0030
    'A_FB_l':     (Fraction(171, 10000),    Fraction(10, 10000)),   # 0.0171 ± 0.0010
    'A_l_SLD':    (Fraction(1513, 10000),   Fraction(21, 10000)),   # 0.1513 ± 0.0021
    'N_nu':       (Fraction(29840, 10000),  Fraction(82, 10000)),   # 2.9840 ± 0.0082
    'M_W':        (Fraction(803692, 10),    Fraction(133, 10)),     # 80369.2 ± 13.3 MeV
}

print("=" * 72)
print("HOWL ELECTROWEAK OVERCONSTRAINED SYSTEM")
print("Tree Level + Leading Δρ Correction")
print("=" * 72)
print()

# ================================================================
# STEP 1: FERMION QUANTUM NUMBERS (exact Fractions)
# ================================================================

print("STEP 1: FERMION QUANTUM NUMBERS")
print("-" * 72)
print()

# T3, Q, Nc for each fermion type
fermions = {
    'nu':   {'T3': Fraction(1,2),  'Qf': Fraction(0,1),   'Nc': Fraction(1,1), 'name': 'neutrino',      'ngen': 3},
    'e':    {'T3': Fraction(-1,2), 'Qf': Fraction(-1,1),  'Nc': Fraction(1,1), 'name': 'charged lepton', 'ngen': 3},
    'u':    {'T3': Fraction(1,2),  'Qf': Fraction(2,3),   'Nc': Fraction(3,1), 'name': 'up-type quark',  'ngen': 2},  # u, c (not t — above threshold but we include for Gamma_had)
    'd':    {'T3': Fraction(-1,2), 'Qf': Fraction(-1,3),  'Nc': Fraction(3,1), 'name': 'down-type quark','ngen': 3},
}

# Vector and axial couplings
for key, f in fermions.items():
    f['vf'] = f['T3'] - 2 * f['Qf'] * s2w
    f['af'] = f['T3']
    f['vf2_af2'] = f['vf']**2 + f['af']**2

print(f"  {'Type':<18} {'T3':>6} {'Q':>6} {'Nc':>4} {'v_f':>12} {'a_f':>8} {'v²+a²':>12}")
print(f"  {'-'*18} {'-'*6} {'-'*6} {'-'*4} {'-'*12} {'-'*8} {'-'*12}")
for key, f in fermions.items():
    print(f"  {f['name']:<18} {float(f['T3']):>6.1f} {float(f['Qf']):>6.2f} "
          f"{int(f['Nc']):>4} {float(f['vf']):>12.8f} {float(f['af']):>8.4f} "
          f"{float(f['vf2_af2']):>12.8f}")
print()

# ================================================================
# STEP 2: LEADING Δρ CORRECTION
# ================================================================

print("STEP 2: LEADING Δρ CORRECTION")
print("-" * 72)
print()

# Δρ = 3 G_F m_t² / (8 π² √2)
# In Fraction: 8π² = 8 × pi_frac² and √2 = sqrt2_frac
# But G_F is in GeV^-2 and m_t in MeV, need consistent units
# G_F in MeV^-2: G_F_MeV = G_F * 10^-6 (since 1 GeV = 1000 MeV, GeV^-2 = 10^6 MeV^-2... no)
# Actually G_F = 1.1663788e-5 GeV^-2 = 1.1663788e-5 / (1000)^2 MeV^-2 = 1.1663788e-11 MeV^-2
# Let's work in GeV throughout
# m_t in GeV:
m_t_GeV = Fraction(172570, 1000)  # 172.570 GeV
M_Z_GeV = Fraction(911876, 10000)  # 91.1876 GeV
m_H_GeV = Fraction(125200, 1000)  # 125.200 GeV

# Δρ = 3 * G_F * m_t² / (8 * π² * √2)
# Use mpmath for the transcendental part, keep structure visible
mp.dps = 50
delta_rho_num = 3 * f2m(G_F) * f2m(m_t_GeV)**2
delta_rho_den = 8 * mpi**2 * msqrt(2)
delta_rho = delta_rho_num / delta_rho_den

print(f"  Δρ = 3·G_F·m_t² / (8π²√2)")
print(f"     = 3 × {float(G_F):.7e} × {float(m_t_GeV):.3f}² / (8 × π² × √2)")
print(f"     = {float(delta_rho_num):.6e} / {float(delta_rho_den):.6f}")
print(f"     = {float(delta_rho):.8f}")
print()

rho_eff = 1 + delta_rho
print(f"  ρ_eff = 1 + Δρ = {float(rho_eff):.8f}")
print()

# ================================================================
# STEP 3: PARTIAL WIDTHS
# ================================================================

print("STEP 3: PARTIAL WIDTHS")
print("-" * 72)
print()

# Prefactor: Γ₀ = G_F · M_Z³ / (6π√2) in GeV
# All in GeV
Gamma0_num = f2m(G_F) * f2m(M_Z_GeV)**3
Gamma0_den = 6 * mpi * msqrt(2)
Gamma0 = Gamma0_num / Gamma0_den  # in GeV

print(f"  Γ₀ = G_F·M_Z³/(6π√2) = {float(Gamma0)*1000:.4f} MeV")
print()

# QCD correction factor for quarks
# δ_QCD = 1 + α_s/π + 1.409(α_s/π)² - 12.77(α_s/π)³
as_over_pi = f2m(alpha_s) / mpi
delta_QCD = 1 + as_over_pi + mpf('1.409') * as_over_pi**2 - mpf('12.77') * as_over_pi**3

print(f"  α_s/π = {float(as_over_pi):.8f}")
print(f"  δ_QCD = 1 + α_s/π + 1.409(α_s/π)² − 12.77(α_s/π)³")
print(f"        = {float(delta_QCD):.8f}")
print()

# Compute each partial width
# Γ_f = Γ₀ × ρ_eff × (v_f² + a_f²) × N_c × δ_QCD(if quark)
# For now treat u,c as 2 generations of up-type and d,s,b as 3 of down-type

widths = {}

# Neutrinos: 3 generations, no QCD, Nc=1
Gamma_nu_single = Gamma0 * rho_eff * f2m(fermions['nu']['vf2_af2']) * 1 * 1
Gamma_inv = 3 * Gamma_nu_single
widths['Gamma_nu'] = Gamma_nu_single
widths['Gamma_inv'] = Gamma_inv

# Charged leptons: 3 generations, no QCD, Nc=1
Gamma_l_single = Gamma0 * rho_eff * f2m(fermions['e']['vf2_af2']) * 1 * 1
Gamma_l_total = 3 * Gamma_l_single
widths['Gamma_l'] = Gamma_l_single

# Up-type quarks: u and c (2 generations), Nc=3, QCD correction
Gamma_u_single = Gamma0 * rho_eff * f2m(fermions['u']['vf2_af2']) * 3 * delta_QCD
Gamma_u_total = 2 * Gamma_u_single

# Down-type quarks: d, s, b (3 generations), Nc=3, QCD correction
Gamma_d_single = Gamma0 * rho_eff * f2m(fermions['d']['vf2_af2']) * 3 * delta_QCD
Gamma_d_total = 3 * Gamma_d_single

# Hadronic width
Gamma_had = Gamma_u_total + Gamma_d_total
widths['Gamma_had'] = Gamma_had

# Total width
Gamma_Z = Gamma_inv + Gamma_l_total + Gamma_had
widths['Gamma_Z'] = Gamma_Z

# Convert to MeV for display
print(f"  PARTIAL WIDTHS (Tree + Δρ):")
print(f"  {'Channel':<20} {'Computed (MeV)':>14} {'LEP (MeV)':>14} {'Ratio':>8}")
print(f"  {'-'*20} {'-'*14} {'-'*14} {'-'*8}")

pw_table = [
    ('Γ_ν (single)',    Gamma_nu_single, None),
    ('Γ_inv (3ν)',      Gamma_inv,       'Gamma_inv'),
    ('Γ_l (single)',    Gamma_l_single,  'Gamma_l'),
    ('Γ_l (3 leptons)', Gamma_l_total,   None),
    ('Γ_u (single)',    Gamma_u_single,  None),
    ('Γ_u (u+c)',       Gamma_u_total,   None),
    ('Γ_d (single)',    Gamma_d_single,  None),
    ('Γ_d (d+s+b)',     Gamma_d_total,   None),
    ('Γ_had',           Gamma_had,       None),
    ('Γ_Z (total)',     Gamma_Z,         'Gamma_Z'),
]

for name, val, mkey in pw_table:
    comp_MeV = float(val) * 1000
    if mkey and mkey in meas:
        lep_MeV = float(meas[mkey][0])
        ratio = comp_MeV / lep_MeV
        print(f"  {name:<20} {comp_MeV:>14.2f} {lep_MeV:>14.2f} {ratio:>8.4f}")
    else:
        print(f"  {name:<20} {comp_MeV:>14.2f} {'—':>14}")
print()

# ================================================================
# STEP 4: RATIOS AND ASYMMETRIES
# ================================================================

print("STEP 4: RATIOS AND ASYMMETRIES")
print("-" * 72)
print()

# R_l = Gamma_had / Gamma_l
R_l_comp = Gamma_had / Gamma_l_single
print(f"  R_l = Γ_had/Γ_l = {float(R_l_comp):.6f}")
print(f"  LEP measured:      {float(meas['R_l'][0]):.6f}")
print(f"  Ratio:             {float(R_l_comp)/float(meas['R_l'][0]):.6f}")
print()

# R_b = Gamma_bb / Gamma_had
# Gamma_bb = Gamma_d_single (b quark contribution, same coupling as d,s)
# At tree level R_b = (v_b² + a_b²) / [2(v_u² + a_u²) + 3(v_d² + a_d²)]
vf2af2_u = f2m(fermions['u']['vf2_af2'])
vf2af2_d = f2m(fermions['d']['vf2_af2'])
R_b_comp = vf2af2_d / (2 * vf2af2_u + 3 * vf2af2_d)
print(f"  R_b = Γ_bb/Γ_had = {float(R_b_comp):.6f}")
print(f"  LEP measured:      {float(meas['R_b'][0]):.6f}")
print(f"  Ratio:             {float(R_b_comp)/float(meas['R_b'][0]):.6f}")
print()

# R_c = Gamma_cc / Gamma_had
R_c_comp = vf2af2_u / (2 * vf2af2_u + 3 * vf2af2_d)
print(f"  R_c = Γ_cc/Γ_had = {float(R_c_comp):.6f}")
print(f"  LEP measured:      {float(meas['R_c'][0]):.6f}")
print(f"  Ratio:             {float(R_c_comp)/float(meas['R_c'][0]):.6f}")
print()

# A_f = 2*v_f*a_f / (v_f² + a_f²)
def A_f_func(vf, af):
    return 2 * vf * af / (vf**2 + af**2)

A_e = A_f_func(f2m(fermions['e']['vf']), f2m(fermions['e']['af']))
A_u = A_f_func(f2m(fermions['u']['vf']), f2m(fermions['u']['af']))
A_d = A_f_func(f2m(fermions['d']['vf']), f2m(fermions['d']['af']))

print(f"  A_e = 2v_ea_e/(v_e²+a_e²) = {float(A_e):.8f}")
print(f"  A_u = {float(A_u):.8f}")
print(f"  A_d = {float(A_d):.8f}")
print()

# A_FB^l = (3/4) * A_e² (lepton forward-backward asymmetry)
# Since A_FB^(0,f) = (3/4) * A_e * A_f, and for f=e: A_FB^l = (3/4)*A_e²
A_FB_l_comp = mpf(3)/4 * A_e**2
print(f"  A_FB^l = (3/4)·A_e² = {float(A_FB_l_comp):.8f}")
print(f"  LEP measured:         {float(meas['A_FB_l'][0]):.8f}")
print(f"  Ratio:                {float(A_FB_l_comp)/float(meas['A_FB_l'][0]):.6f}")
print()

# A_l (= A_e at tree level)
print(f"  A_l = A_e = {float(A_e):.8f}")
print(f"  SLD measured: {float(meas['A_l_SLD'][0]):.8f}")
print(f"  Ratio:        {float(A_e)/float(meas['A_l_SLD'][0]):.6f}")
print()

# N_nu = Gamma_inv / Gamma_l
N_nu_comp = Gamma_inv / Gamma_l_single
print(f"  N_ν = Γ_inv/Γ_l = {float(N_nu_comp):.6f}")
print(f"  LEP measured:     {float(meas['N_nu'][0]):.6f}")
print(f"  Ratio:            {float(N_nu_comp)/float(meas['N_nu'][0]):.6f}")
print()

# sigma0_had = 12π Γ_e Γ_had / (M_Z² Γ_Z²)
# In nanobarns: need conversion. 1 GeV^-2 = 0.3894e6 nb
GeV2_to_nb = mpf('0.3893793656e6')  # exact conversion: hbar²c² in GeV² nb
sigma0_num = 12 * mpi * Gamma_l_single * Gamma_had
sigma0_den = f2m(M_Z_GeV)**2 * Gamma_Z**2
sigma0_comp = sigma0_num / sigma0_den * GeV2_to_nb
print(f"  σ⁰_had = 12π·Γ_e·Γ_had/(M_Z²·Γ_Z²) = {float(sigma0_comp):.4f} nb")
print(f"  LEP measured:                           {float(meas['sigma0_had'][0]):.4f} nb")
print(f"  Ratio:                                  {float(sigma0_comp)/float(meas['sigma0_had'][0]):.6f}")
print()

# M_W prediction (tree level): M_W² (1 - M_W²/M_Z²) = π·α/(√2·G_F)
# Solve: M_W² - M_W⁴/M_Z² = π·α/(√2·G_F)
# Let x = M_W², A = π·α/(√2·G_F), B = M_Z²
# x - x²/B = A  =>  x²/B - x + A = 0  =>  x = (B/2)(1 - sqrt(1 - 4A/B))
A_mw = mpi * f2m(alpha_em) / (msqrt(2) * f2m(G_F))
B_mw = f2m(M_Z_GeV)**2
discriminant = 1 - 4 * A_mw / B_mw
M_W_sq = (B_mw / 2) * (1 - msqrt(discriminant))
M_W_pred = msqrt(M_W_sq)  # in GeV
M_W_pred_MeV = M_W_pred * 1000

print(f"  M_W prediction (tree level):")
print(f"    M_W² (1 - M_W²/M_Z²) = πα/(√2·G_F)")
print(f"    M_W = {float(M_W_pred_MeV):.2f} MeV")
print(f"    Measured: {float(meas['M_W'][0]):.2f} MeV")
print(f"    Ratio: {float(M_W_pred_MeV)/float(meas['M_W'][0]):.6f}")
print()

# With Δρ correction: replace α → α/(1-Δρ) in the M_W formula
# Actually the correction enters as: M_W² sin²θ = πα/(√2·G_F·(1-Δr))
# where Δr ≈ Δρ - (α/π)×... For leading order, use 1-Δr ≈ 1-Δρ
A_mw_corr = mpi * f2m(alpha_em) / (msqrt(2) * f2m(G_F) * (1 - delta_rho))
disc_corr = 1 - 4 * A_mw_corr / B_mw
M_W_sq_corr = (B_mw / 2) * (1 - msqrt(disc_corr))
M_W_corr = msqrt(M_W_sq_corr) * 1000

print(f"  M_W with Δρ correction:")
print(f"    M_W = {float(M_W_corr):.2f} MeV")
print(f"    Measured: {float(meas['M_W'][0]):.2f} MeV")
print(f"    Ratio: {float(M_W_corr)/float(meas['M_W'][0]):.6f}")
print()

# ================================================================
# STEP 5: PARAMETER EXTRACTION
# ================================================================

print("=" * 72)
print("STEP 5: PARAMETER EXTRACTION")
print("=" * 72)
print()

# EXTRACT sin²θ_W from A_l (SLD measurement)
# A_l = 2*v_l*a_l/(v_l²+a_l²) where v_l = -1/2 + 2*s2w, a_l = -1/2
# A_l = 2*(-1/2+2s)(−1/2) / ((-1/2+2s)²+(1/2)²)
# A_l = -(−1/2+2s) / ((-1/2+2s)² + 1/4)
# Let x = 2*s2w - 1/2 (= v_l with sign)
# Then A_l = -x*(-1/2) * 2 / (x² + 1/4) = x/(x²+1/4)
# Wait: v_l = -1/2 + 2*s2w, a_l = -1/2
# A_l = 2*v_l*a_l/(v_l²+a_l²) = 2*(-1/2+2s)*(-1/2) / ((-1/2+2s)²+1/4)
#     = (-1/2+2s)*(-1) / ((-1/2+2s)²+1/4)
#     = (1/2-2s) / ((1/2-2s)² + 1/4)
# Let u = 1/2 - 2s  (note u = -v_l)
# A_l = u / (u² + 1/4)

# From A_l(SLD) = 0.1513, solve for s2w numerically
# Use Newton's method
print("  EXTRACTING sin²θ_W from A_l(SLD) = 0.1513")
print()

A_l_meas = f2m(meas['A_l_SLD'][0])

def A_l_from_s2w(s):
    """Compute A_l from sin²θ_W."""
    u = mpf(1)/2 - 2*s
    return u / (u**2 + mpf(1)/4)

def dA_l_ds2w(s):
    """Derivative dA_l/d(sin²θ_W)."""
    u = mpf(1)/2 - 2*s
    # A = u/(u²+1/4), du/ds = -2
    # dA/du = (u²+1/4 - 2u²)/(u²+1/4)² = (1/4-u²)/(u²+1/4)²
    # dA/ds = dA/du * du/ds = -2*(1/4-u²)/(u²+1/4)²
    return -2*(mpf(1)/4 - u**2) / (u**2 + mpf(1)/4)**2

# Newton iteration starting from input s2w
s2w_extract = f2m(s2w)  # start at input value
for i in range(20):
    A_val = A_l_from_s2w(s2w_extract)
    dA = dA_l_ds2w(s2w_extract)
    correction = (A_val - A_l_meas) / dA
    s2w_extract -= correction
    if abs(float(correction)) < 1e-15:
        break

A_check = A_l_from_s2w(s2w_extract)
print(f"  Extracted sin²θ_W = {float(s2w_extract):.8f}")
print(f"  Input sin²θ_W     = {float(s2w):.8f}")
print(f"  Difference         = {float(s2w_extract - f2m(s2w)):.6e}")
print(f"  Verification: A_l(extracted) = {float(A_check):.8f} vs measured {float(A_l_meas):.8f}")
print()

# EXTRACT sin²θ_W from A_FB_l = 0.0171
print("  EXTRACTING sin²θ_W from A_FB^l = 0.0171")
print()

A_FB_meas = f2m(meas['A_FB_l'][0])

def A_FB_from_s2w(s):
    A_e_val = A_l_from_s2w(s)
    return mpf(3)/4 * A_e_val**2

s2w_from_AFB = f2m(s2w)
for i in range(20):
    AFB_val = A_FB_from_s2w(s2w_from_AFB)
    # Numerical derivative
    h = mpf('1e-10')
    dAFB = (A_FB_from_s2w(s2w_from_AFB + h) - A_FB_from_s2w(s2w_from_AFB - h)) / (2*h)
    correction = (AFB_val - A_FB_meas) / dAFB
    s2w_from_AFB -= correction
    if abs(float(correction)) < 1e-15:
        break

print(f"  Extracted sin²θ_W = {float(s2w_from_AFB):.8f}")
print(f"  Input sin²θ_W     = {float(s2w):.8f}")
print(f"  Difference         = {float(s2w_from_AFB - f2m(s2w)):.6e}")
print()

# EXTRACT α_s from R_l using the sin²θ_W extracted from A_l
print("  EXTRACTING α_s from R_l = 20.767 (using extracted sin²θ_W)")
print()

R_l_meas = f2m(meas['R_l'][0])
s2w_use = s2w_extract  # use the A_l extraction

def R_l_from_alpha_s(a_s, s2w_val):
    """Compute R_l from alpha_s and sin²θ_W."""
    v_u = mpf(1)/2 - 4*s2w_val/3
    a_u = mpf(1)/2
    v_d = -mpf(1)/2 + 2*s2w_val/3
    a_d = -mpf(1)/2
    v_e = -mpf(1)/2 + 2*s2w_val
    a_e = -mpf(1)/2
    
    vf2af2_u_val = v_u**2 + a_u**2
    vf2af2_d_val = v_d**2 + a_d**2
    vf2af2_e_val = v_e**2 + a_e**2
    
    asp = a_s / mpi
    dqcd = 1 + asp + mpf('1.409') * asp**2 - mpf('12.77') * asp**3
    
    gamma_had_rel = (2 * vf2af2_u_val + 3 * vf2af2_d_val) * 3 * dqcd
    gamma_l_rel = vf2af2_e_val
    
    return gamma_had_rel / gamma_l_rel

# Newton iteration for alpha_s
as_extract = f2m(alpha_s)
for i in range(20):
    R_val = R_l_from_alpha_s(as_extract, s2w_use)
    h = mpf('1e-10')
    dR = (R_l_from_alpha_s(as_extract + h, s2w_use) - R_l_from_alpha_s(as_extract - h, s2w_use)) / (2*h)
    correction = (R_val - R_l_meas) / dR
    as_extract -= correction
    if abs(float(correction)) < 1e-15:
        break

R_check = R_l_from_alpha_s(as_extract, s2w_use)
print(f"  Extracted α_s     = {float(as_extract):.8f}")
print(f"  Input α_s         = {float(alpha_s):.8f}")
print(f"  Difference         = {float(as_extract - f2m(alpha_s)):.6e}")
print(f"  Verification: R_l(extracted) = {float(R_check):.6f} vs measured {float(R_l_meas):.6f}")
print()

# ================================================================
# STEP 6: FULL COMPARISON TABLE
# ================================================================

print("=" * 72)
print("STEP 6: FULL COMPARISON TABLE")
print("=" * 72)
print()

obs_table = [
    ('Γ_l (MeV)',      float(Gamma_l_single)*1000, float(meas['Gamma_l'][0]),     float(meas['Gamma_l'][1])),
    ('Γ_inv (MeV)',     float(Gamma_inv)*1000,      float(meas['Gamma_inv'][0]),   float(meas['Gamma_inv'][1])),
    ('Γ_Z (MeV)',       float(Gamma_Z)*1000,        float(meas['Gamma_Z'][0]),     float(meas['Gamma_Z'][1])),
    ('R_l',             float(R_l_comp),             float(meas['R_l'][0]),         float(meas['R_l'][1])),
    ('R_b',             float(R_b_comp),             float(meas['R_b'][0]),         float(meas['R_b'][1])),
    ('R_c',             float(R_c_comp),             float(meas['R_c'][0]),         float(meas['R_c'][1])),
    ('A_FB^l',          float(A_FB_l_comp),          float(meas['A_FB_l'][0]),      float(meas['A_FB_l'][1])),
    ('A_l (SLD)',       float(A_e),                  float(meas['A_l_SLD'][0]),     float(meas['A_l_SLD'][1])),
    ('N_ν',             float(N_nu_comp),            float(meas['N_nu'][0]),        float(meas['N_nu'][1])),
    ('σ⁰_had (nb)',     float(sigma0_comp),          float(meas['sigma0_had'][0]),  float(meas['sigma0_had'][1])),
    ('M_W (MeV)',       float(M_W_corr),             float(meas['M_W'][0]),         float(meas['M_W'][1])),
]

print(f"  {'Observable':<16} {'Computed':>12} {'Measured':>12} {'Ratio':>8} {'Pull (σ)':>10}")
print(f"  {'-'*16} {'-'*12} {'-'*12} {'-'*8} {'-'*10}")
for name, comp, mval, unc in obs_table:
    ratio = comp / mval if mval != 0 else 0
    pull = (comp - mval) / unc if unc != 0 else 0
    print(f"  {name:<16} {comp:>12.4f} {mval:>12.4f} {ratio:>8.4f} {pull:>10.1f}")

print()

# ================================================================
# STEP 7: EXTRACTION SUMMARY
# ================================================================

print("=" * 72)
print("STEP 7: EXTRACTION SUMMARY")
print("=" * 72)
print()

print(f"  {'Parameter':<20} {'Input':>12} {'From A_l':>12} {'From A_FB':>12} {'From R_l':>12}")
print(f"  {'-'*20} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")
print(f"  {'sin²θ_W':<20} {float(s2w):>12.8f} {float(s2w_extract):>12.8f} {float(s2w_from_AFB):>12.8f} {'—':>12}")
print(f"  {'α_s':<20} {float(alpha_s):>12.8f} {'—':>12} {'—':>12} {float(as_extract):>12.8f}")
print()

print(f"  sin²θ_W consistency:")
print(f"    Input:              {float(s2w):.8f}")
print(f"    From A_l(SLD):      {float(s2w_extract):.8f}  (Δ = {float(s2w_extract-f2m(s2w)):+.6e})")
print(f"    From A_FB^l:        {float(s2w_from_AFB):.8f}  (Δ = {float(s2w_from_AFB-f2m(s2w)):+.6e})")
print()
print(f"  α_s from R_l:         {float(as_extract):.8f}  (Δ = {float(as_extract-f2m(alpha_s)):+.6e})")
print()

# ================================================================
# CHECKS (non-halting — print PASS/FAIL, always run to end)
# ================================================================

print("=" * 72)
print("DIAGNOSTIC CHECKS")
print("=" * 72)
print()

# Debug N_nu
print(f"  DEBUG: N_nu computed = {float(N_nu_comp):.6f}")
print(f"  DEBUG: Gamma_nu_single (GeV) = {float(Gamma_nu_single):.8e}")
print(f"  DEBUG: Gamma_l_single (GeV)  = {float(Gamma_l_single):.8e}")
print(f"  DEBUG: Gamma_inv (GeV)       = {float(Gamma_inv):.8e}")
print(f"  DEBUG: v_nu²+a_nu² = {float(f2m(fermions['nu']['vf2_af2'])):.8f}")
print(f"  DEBUG: v_e²+a_e²   = {float(f2m(fermions['e']['vf2_af2'])):.8f}")
print(f"  DEBUG: ratio (nu/e) = {float(f2m(fermions['nu']['vf2_af2'])/f2m(fermions['e']['vf2_af2'])):.8f}")
print()

# N_nu ~ 6 means Gamma_l is too small by ~2x or Gamma_inv too large.
# The issue is likely that Gamma_l_single is one lepton flavor but
# N_nu = Gamma_inv / Gamma_l_single_SM where the SM prediction for
# one neutrino flavor is used. Let's check: LEP defines
# N_nu = Gamma_inv / Gamma_nu_SM, NOT Gamma_inv / Gamma_l.
# Our N_nu_comp = Gamma_inv / Gamma_l_single = 3*Gamma_nu / Gamma_l
# = 3 * (v_nu²+a_nu²) / (v_e²+a_e²)
# v_nu²+a_nu² = 1/4+1/4 = 1/2
# v_e²+a_e² = (−0.0376)²+(0.5)² = 0.00141 + 0.25 = 0.2514
# ratio = 3 * 0.5 / 0.2514 = 5.97  <-- matches the 5.97 we see!
#
# FIX: LEP N_nu = Gamma_inv / Gamma_nu_SM (single neutrino width)
# So N_nu = Gamma_inv / Gamma_nu_single = 3*Gamma_nu / Gamma_nu = 3

N_nu_correct = Gamma_inv / Gamma_nu_single
print(f"  CORRECTED N_ν = Γ_inv / Γ_ν(SM) = {float(N_nu_correct):.6f}")
print(f"  (Previous was Γ_inv/Γ_l which gives {float(N_nu_comp):.4f} — wrong definition)")
print()
print(f"  But N_nu = 3 exactly by construction (we put in 3 neutrinos).")
print(f"  The LEP measurement N_nu = 2.984 ± 0.008 is significant because")
print(f"  it uses MEASURED Gamma_inv and SM-PREDICTED Gamma_nu.")
print(f"  To reproduce, we need: N_nu = (Gamma_Z_meas - Gamma_had_comp - 3*Gamma_l_comp) / Gamma_nu_comp")
print()

# Recompute N_nu the LEP way: use measured Gamma_Z, computed hadronic and leptonic
Gamma_Z_meas_GeV = f2m(meas['Gamma_Z'][0]) / 1000  # convert MeV to GeV
Gamma_vis_comp = Gamma_had + 3 * Gamma_l_single
Gamma_inv_from_meas = Gamma_Z_meas_GeV - Gamma_vis_comp  # "measured" invisible from subtraction
N_nu_lep_way = Gamma_inv_from_meas / Gamma_nu_single

print(f"  LEP-style N_ν = (Γ_Z^meas − Γ_had^comp − 3Γ_l^comp) / Γ_ν^comp")
print(f"    Γ_Z measured     = {float(Gamma_Z_meas_GeV)*1000:.2f} MeV")
print(f"    Γ_vis computed   = {float(Gamma_vis_comp)*1000:.2f} MeV")
print(f"    Γ_inv (by subtr) = {float(Gamma_inv_from_meas)*1000:.2f} MeV")
print(f"    Γ_ν (SM, single) = {float(Gamma_nu_single)*1000:.4f} MeV")
print(f"    N_ν              = {float(N_nu_lep_way):.4f}")
print(f"    LEP measured     = {float(meas['N_nu'][0]):.4f}")
print()

checks = []

def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    checks.append((name, status))
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")

# Width checks
Gamma_l_ratio = float(Gamma_l_single)*1000 / float(meas['Gamma_l'][0])
Gamma_Z_ratio = float(Gamma_Z)*1000 / float(meas['Gamma_Z'][0])
Gamma_inv_ratio = float(Gamma_inv)*1000 / float(meas['Gamma_inv'][0])

check("Γ_l within 10%", 0.90 < Gamma_l_ratio < 1.10,
      f"ratio = {Gamma_l_ratio:.4f}")
check("Γ_Z within 15%", 0.85 < Gamma_Z_ratio < 1.15,
      f"ratio = {Gamma_Z_ratio:.4f}")
check("Γ_inv within 10%", 0.90 < Gamma_inv_ratio < 1.10,
      f"ratio = {Gamma_inv_ratio:.4f}")

# Ratio checks
R_l_ratio = float(R_l_comp) / float(meas['R_l'][0])
check("R_l within 10%", 0.90 < R_l_ratio < 1.10,
      f"ratio = {R_l_ratio:.4f}")

R_b_ratio = float(R_b_comp) / float(meas['R_b'][0])
check("R_b within 10%", 0.90 < R_b_ratio < 1.10,
      f"ratio = {R_b_ratio:.4f}")

# Asymmetry checks
A_FB_ratio = float(A_FB_l_comp) / float(meas['A_FB_l'][0])
check("A_FB^l within 50%", 0.50 < A_FB_ratio < 1.50,
      f"ratio = {A_FB_ratio:.4f}")

A_l_ratio = float(A_e) / float(meas['A_l_SLD'][0])
check("A_l within 20%", 0.80 < A_l_ratio < 1.20,
      f"ratio = {A_l_ratio:.4f}")

# M_W check
M_W_ratio = float(M_W_corr) / float(meas['M_W'][0])
check("M_W within 5%", 0.95 < M_W_ratio < 1.05,
      f"ratio = {M_W_ratio:.4f}")

# Extraction convergence
check("A_l extraction converged", abs(float(A_check) - float(A_l_meas)) < 1e-8,
      f"residual = {abs(float(A_check) - float(A_l_meas)):.2e}")
check("R_l extraction converged", abs(float(R_check) - float(R_l_meas)) < 1e-8,
      f"residual = {abs(float(R_check) - float(R_l_meas)):.2e}")

# N_nu LEP-style check
if float(N_nu_lep_way) > 0:
    check("N_ν (LEP-style) reasonable", 2.0 < float(N_nu_lep_way) < 5.0,
          f"N_ν = {float(N_nu_lep_way):.4f}")
else:
    check("N_ν (LEP-style) positive", False,
          f"N_ν = {float(N_nu_lep_way):.4f} — negative, comp widths exceed measured Γ_Z")

print()
n_pass = sum(1 for _, s in checks if s == "PASS")
n_fail = sum(1 for _, s in checks if s == "FAIL")
print(f"  TOTAL: {n_pass} PASS, {n_fail} FAIL out of {len(checks)}")
print()

print("=" * 72)
print("SCRIPT COMPLETE")
print("=" * 72)
