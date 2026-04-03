# HOWL Platform API Manual

**For:** phys24_lib.py (foundation) + 5 extension libraries built in Session 4

**Date:** April 3, 2026

**Convention:** Every library imports `from phys24_lib import *`. Extension libraries may import each other. All computation uses Fraction arithmetic with mpf at the display boundary only.

---

## 1. Foundation: phys24_lib.py

This is the base. Every other library imports it. Not documented here in full — see PHYS-24 and phys24_lib_test.py (148/148). The key exports used by all extension libraries:

### Constants

Every DATA-4 constant is available as a Fraction. Naming convention: the variable name matches the physics symbol with underscores.

```python
from phys24_lib import *

alpha_inv      # Fraction, 1/alpha_EM = 137.035999177 (DATA-4 B1)
sin2_tW        # Fraction, sin^2(theta_W) = 0.23122 (DATA-4 B11)
alpha_s        # Fraction, alpha_s(M_Z) = 0.1180 (DATA-4 B12)
m_e            # Fraction, electron mass in MeV (DATA-4 B2)
m_mu           # Fraction, muon mass in MeV (DATA-4 B3)
m_tau          # Fraction, tau mass in MeV (DATA-4 B4)
M_Z            # Fraction, Z mass in MeV (DATA-4 C1)
m_t            # Fraction, top mass in MeV (DATA-4 C4)
# ... all 146 DATA-4 entries

b1_SM, b2_SM, b3_SM          # SM one-loop betas as Fractions
db1_VL, db2_VL, db3_VL       # CD beta shifts as Fractions
b1_mod, b2_mod, b3_mod       # Modified betas (SM + CD)
gap_SM, gap_VL, gap_MSSM     # Gap ratios as Fractions
gap_measured                   # Measured gap ratio as Fraction
inv_a1, inv_a2, inv_a3       # Inverse GUT couplings at M_Z
b_ij_SM                       # 3x3 list of Fractions, two-loop SM matrix

R2_f           # Fraction, pi/4
R4_f           # Fraction, pi^2/32

K_koide        # Fraction, Koide ratio for leptons
a2_lep         # Fraction, 1.9999630688 (measurement, NOT 2)

M_VL_lo, M_VL_hi   # Fraction, CD mass window bounds in MeV
```

Every constant has a `_full` variant for maximum precision: `alpha_inv_full`, `m_e_full`, etc. Currently identical to the base for most entries.

### Helpers

```python
f2m(frac)                    # Fraction → mpf at working precision
digits_of(got, expected)     # Digits of numeric agreement (mpf)
show(label, value)           # Print labeled mpf at 11+ sf
count_sig_digits(s)          # Count sig digits in decimal string
precision_report(frac, pub)  # Full precision metadata dict
```

### Check Functions

```python
chk(tag, got, expected, need, checks)          # Numeric agreement (mpf vs mpf)
chk_exact(tag, got, expected, checks)          # Fraction identity
chk_bool(tag, condition, detail, checks)       # Boolean condition
chk_precision(tag, frac, pub_str, need, checks)  # String + numeric reconstruction
print_summary(checks)                           # Print "N PASS, M FAIL out of K"
```

All check functions append `(tag, "PASS"/"FAIL")` to the `checks` list.

---

## 2. Derivation Library: data_4_derivation_lib.py

**Self-test:** 37/37

**Import:**
```python
from phys24_lib import *
from data_4_derivation_lib import *
```

### Group Theory Constants

```python
C2_adj_SU3      # Fraction(3), adjoint Casimir of SU(3)
C2_adj_SU2      # Fraction(2), adjoint Casimir of SU(2)
C2_fund_SU3     # Fraction(4, 3), fundamental Casimir of SU(3)
C2_fund_SU2     # Fraction(3, 4), fundamental Casimir of SU(2)
S2_fund         # Fraction(1, 2), Dynkin index of fundamental (any SU(N))
dim_fund_SU3    # Fraction(3)
dim_fund_SU2    # Fraction(2)
k1_GUT          # Fraction(3, 5), SU(5) normalization
k1_inv          # Fraction(5, 3), 1/k1
N_gen           # Fraction(3), number of generations
Y_CD            # Fraction(1, 6), CD hypercharge
gauge_coeff     # Fraction(-11, 3), Yang-Mills coefficient
```

### Precomputed Values

```python
db_ij_VL       # 3x3 list of Fractions, VL two-loop b_ij matrix
b_ij_full      # 3x3 list of Fractions, SM + VL combined
b_EM_CD        # Fraction, (5/3)*b1' + b2' for EM running
```

### Coupling Extraction

```python
derive_couplings(alpha_inv_f, sin2_tW_f, alpha_s_f)
```
Extracts GUT-normalized inverse couplings at M_Z from three measured inputs.

**Args:** All Fractions from phys24_lib.

**Returns:** `(inv_a1, inv_a2, inv_a3)` as Fractions.

**Pitfall documented inline:** 1/α₂ = sin²θ_W × (1/α_EM). MULTIPLY, not divide. Wrong: 593. Right: 31.7.

```python
ia1, ia2, ia3 = derive_couplings(alpha_inv, sin2_tW, alpha_s)
show("1/alpha_1", f2m(ia1))   # ~63.21
show("1/alpha_2", f2m(ia2))   # ~31.69
show("1/alpha_3", f2m(ia3))   # ~8.47
```

### VL Beta Shifts

```python
compute_vl_one_loop(dim_R3, dim_R2, Y, S2_R3, S2_R2)
```
One-loop beta shifts for any vector-like pair (R₃, R₂, Y).

**Returns:** `(db1, db2, db3)` as Fractions.

```python
db1, db2, db3 = compute_vl_one_loop(
    dim_fund_SU3, dim_fund_SU2, Y_CD, S2_fund, S2_fund)
# Returns (1/15, 1, 1/3) for the Cabibbo Doublet
```

```python
compute_vl_two_loop(C2_R3, C2_R2, S2_R3, S2_R2, dim_R3, dim_R2, Y, k1)
```
Two-loop b_ij matrix for any VL pair. FERMION contribution only — does NOT include gauge self-coupling (already in SM b_ij).

**Returns:** 3×3 list of Fractions.

**Critical pitfall documented inline:** db₂₂ = 15/4 (correct, fermion only), NOT 39/4 (wrong, includes 2×C_G).

```python
db_ij = compute_vl_two_loop(
    C2_fund_SU3, C2_fund_SU2, S2_fund, S2_fund,
    dim_fund_SU3, dim_fund_SU2, Y_CD, k1_GUT)
# db_ij[1][1] == Fraction(15, 4)  # MUST be 15/4
```

### Running and Crossing

```python
run_one_loop_frac(inv_a_start, betas, L)
```
One-loop running: 1/α_i(μ) = 1/α_i(μ₀) − b_i × L.

**Args:** `inv_a_start` = list of 3 Fractions, `betas` = list of 3 Fractions, `L` = mpf.

**Returns:** list of 3 mpf.

**Sign convention:** MINUS b×L. Couplings CONVERGE at high energy.

```python
find_crossing_L(inv_a1_f, inv_a2_f, b1_f, b2_f)
```
Find L where 1/α₁ = 1/α₂.

**Returns:** Fraction (exact).

```python
L_to_scale(L_val, M_Z_MeV)
```
Convert L to energy scale in MeV and log₁₀(μ/GeV).

**Returns:** `(mu_MeV, log10_mu_GeV)` as mpf pair.

### Two-Loop Euler Integrator

```python
run_two_loop_euler(inv_a_start, b1loop, bij, L_total, n_steps)
```
Euler integration of the coupled two-loop RGEs using mpf arithmetic.

**Args:** All lists of 3 mpf (or 3×3 mpf for bij). `L_total` positive = running UP. `n_steps` = Euler steps (500 is standard).

**Returns:** list of 3 mpf at the end of integration.

**Both one-loop and two-loop terms have MINUS signs.** Pitfall documented inline.

```python
result = run_two_loop_euler(
    [f2m(inv_a1), f2m(inv_a2), f2m(inv_a3)],
    [f2m(b1_mod), f2m(b2_mod), f2m(b3_mod)],
    [[f2m(b_ij_SM[i][j]) for j in range(3)] for i in range(3)],
    L_GUT, 500)
```

### Predictions

```python
predict_alpha_s_one_loop(inv_a1_f, inv_a2_f, inv_a3_f, b1_f, b2_f, b3_f)
```
**Returns:** dict with `alpha_s_pred`, `Delta`, `L_GUT`, `inv_a_GUT`, `inv_a3_at_GUT`.

```python
predict_alpha_s_two_loop(inv_a1_f, inv_a2_f, inv_a3_f, b1loop, bij, n_steps=500)
```
Binary search for two-loop crossing, then run back to predict α_s.

**Args:** `b1loop` = list of 3 Fractions, `bij` = 3×3 list of Fractions.

**Returns:** dict with `alpha_s_pred`, `Delta`, `L_GUT`, `inv_a_GUT`.

```python
# SM b_ij only
result_SM = predict_alpha_s_two_loop(
    inv_a1, inv_a2, inv_a3,
    [b1_mod, b2_mod, b3_mod], b_ij_SM)
# result_SM["alpha_s_pred"] ~ 0.11753, miss 0.397%

# Full b_ij (SM + VL)
result_full = predict_alpha_s_two_loop(
    inv_a1, inv_a2, inv_a3,
    [b1_mod, b2_mod, b3_mod], b_ij_full)
# result_full["alpha_s_pred"] ~ 0.11838, miss 0.325%
```

```python
predict_sin2_one_loop(alpha_inv_f, alpha_s_f, b1_f, b2_f, b3_f)
```
Predict sin²θ_W from (α_EM, α_s) using one-loop unification.

**Returns:** dict with `sin2_pred`, `L_GUT`, `inv_a_GUT`, `inv_a2_pred`, `b_EM`.

**Pitfall:** sin²θ_W = inv_a2 / alpha_inv. NOT alpha_inv / inv_a2.

**Pitfall:** 1/α_GUT must be computed from the α₃ side, not the EM side.

```python
predict_sin2_two_loop(alpha_inv_f, alpha_s_f, b1loop, bij, n_steps=500)
```
Two-loop sin²θ_W prediction via binary search.

**Returns:** dict with `sin2_pred`, `L_GUT`, `inv_a_GUT`.

### Gap Ratio

```python
gap_ratio_from_betas(b1_f, b2_f, b3_f)
```
Compute (b₁−b₂)/(b₂−b₃).

**Returns:** Fraction (exact).

### Beta Decomposition

```python
decompose_SM_betas()
```
Decompose SM betas into gauge + Higgs + fermion contributions.

**Returns:** dict with `b1_gauge`, `b1_higgs`, `b1_fermion`, `b1_per_gen`, etc. All Fractions.

### Koide

```python
koide_ratio(m1_f, m2_f, m3_f)       # K = sum(m) / (sum(sqrt(m)))^2
koide_amplitude_sq(K_val)            # a^2 = 2*(3*K - 1)
koide_predict_m_tau(m_e_f, m_mu_f)   # Predict m_tau from K = 2/3
```

`koide_predict_m_tau` returns dict with `m_tau_pred`, `m_tau_other`, `M_koide`, `sqrt_m_tau_pred`.

**Pitfall:** K = sum_m / (sum_sqrt)², NOT (sum_sqrt)² / (3×sum_m).

---

## 3. Structures Library: phys24_structure_lib.py

**Self-test:** 46/46

**Import:**
```python
from phys24_lib import *
from phys24_structure_lib import *
```

### Representation Constructor

```python
make_rep(name, su3_dim, su2_dim, Y, rep_type="chiral",
         mass_var=None, data4_entry=None, papers=None)
```
Create a representation dict with all derived properties.

**Chiral coefficients:** (2/5, 2/3, 2/3) for U(1), SU(2), SU(3).

**VL coefficients:** (2/5, 2/3, 1/3). Difference is ONLY in SU(3).

**Returns:** dict with keys: `name`, `su3_dim`, `su2_dim`, `Y`, `Y2`, `rep_type`, `rep_tuple`, `S2_R3`, `S2_R2`, `C2_R3`, `C2_R2`, `db1`, `db2`, `db3`, `db` (tuple), `charges`, `mass_var`, `data4_entry`, `papers`.

```python
# Build the CD from quantum numbers
cd = make_rep("Cabibbo Doublet", 3, 2, Fraction(1, 6), "vector-like")
print(cd["db"])       # (Fraction(1, 15), Fraction(1, 1), Fraction(1, 3))
print(cd["charges"])  # (Fraction(2, 3), Fraction(-1, 3))

# Test an alternative candidate
alt = make_rep("Alternative", 3, 1, Fraction(2, 3), "vector-like")
gap_alt = gap_ratio_from_betas(b1_SM + alt["db1"], b2_SM + alt["db2"], b3_SM + alt["db3"])
```

### Prebuilt SM Representations

```python
Q_L     # (3, 2, 1/6) chiral — left-handed quark doublet
u_R     # (3, 1, 2/3) chiral — right-handed up
d_R     # (3, 1, -1/3) chiral — right-handed down
L_L     # (1, 2, -1/2) chiral — left-handed lepton doublet
e_R     # (1, 1, -1) chiral — right-handed electron
SM_GENERATION     # [Q_L, u_R, d_R, L_L, e_R]
HIGGS             # dict with db = (1/10, 1/6, 0), scalar (not from make_rep)
CABIBBO_DOUBLET   # (3, 2, 1/6) vector-like, from make_rep
```

### Census Functions

```python
generation_betas(gen_reps=None)   # Sum beta shifts for one generation
                                   # Default: SM_GENERATION → (4/3, 4/3, 4/3)
total_SM_betas(n_gen=3)           # Full SM betas from census → (41/10, -19/6, -7)
```

### Particle Catalog

```python
PARTICLE_CATALOG    # list of 12 dicts, sorted by mass
```

Each entry: `name`, `mass_var`, `mass_frac` (Fraction), `data4` (entry ID), `rep` (from make_rep or None for bosons), `threshold_type` ("lepton", "quark", "gauge", "scalar").

```python
particles_at_scale(mu_MeV)       # List of particles with mass <= mu
active_fermion_count(mu_MeV)     # Count of active quarks at scale mu
```

```python
at_MZ = particles_at_scale(M_Z)    # 10 particles active
nf = active_fermion_count(M_Z)     # 5 quarks (not top)
```

### DATA-4 Cross-Reference

```python
DATA4_MAP    # dict mapping entry IDs to {var, value, type, unit, digits, note}

lookup_data4("B1")           # Returns entry dict or None
entries_by_type("M")         # Returns [(id, entry_dict), ...] for all measured
entries_by_type("E")         # 7 exact entries
entries_by_type("D")         # Derived entries
```

### Paper Cross-Reference

```python
PAPER_TOPICS    # dict mapping paper IDs to one-line topic descriptions

papers_about("gap ratio")   # Returns [("PHYS-13", "Gap ratio 218/115..."), ...]
papers_about("koide")       # Returns [("DATA-2", ...), ("PHYS-8", ...), ("PHYS-23", ...)]
```

### Registries

```python
ANOMALIES       # dict of 3 anomalies with sigma, quantum_number_used, resolution
EXPERIMENTS     # dict of 3 experiments with observable, cd_prediction, status
CLOSED_PATHS    # dict of 7 closed paths with killed_by, paper
ENERGY_DOMAINS  # list of 5 named energy domains with range, description, perturbative flag
GUT_PARTICLES   # dict of 4 heavy GUT particle types with properties
```

```python
# Check if a path is closed
if "C3_Koide" in CLOSED_PATHS:
    print(CLOSED_PATHS["C3_Koide"]["killed_by"])
    # "Tautology (3 params, 3 data) + saddle point"
```

---

## 4. Boundary Map Library: phys24_boundary_map_lib.py

**Self-test:** 14/14

**Import:**
```python
from phys24_lib import *
from phys24_boundary_map_lib import *
```

### Forces Registry

```python
FORCES    # dict with 5 entries: gravity, electromagnetic, weak, strong, unified
```

Each force: `name`, `gauge_group` (or None for gravity), `coupling_name`, `coupling_var`, `mediator`, `range`, `status`, `papers`.

### Scale Conversions

```python
hbar_c_MeV_fm          # Fraction, 197.3269804 MeV*fm

energy_to_distance_fm(E_MeV)    # MeV → fm (Compton wavelength)
distance_fm_to_energy(d_fm)     # fm → MeV

DISTANCE_SCALES    # dict of named scales with fm and meters values
                   # Keys: Planck_length, proton_radius, nuclear_radius,
                   # atom_radius, virus, cell, orange, earth_radius,
                   # earth_sun, observable_universe
```

```python
# How big is a proton in fm?
d = DISTANCE_SCALES["proton_radius"]["fm"]   # 0.84 fm

# What energy corresponds to orange size?
E_orange = distance_fm_to_energy(DISTANCE_SCALES["orange"]["fm"])
```

### The Boundary Stack

```python
BOUNDARY_STACK    # list of 19 boundary dicts, highest energy first
```

Each boundary dict:
- `name`: human-readable name
- `scale_MeV`: Fraction (or None if unknown)
- `scale_MeV_estimate`: Fraction (for staged/theoretical boundaries)
- `scale_MeV_lo`, `scale_MeV_hi`: Fraction (for windowed boundaries like CD)
- `scale_fm`: mpf (or None)
- `what_changes`: string describing the physics change
- `above`, `below`: dicts with properties on each side
- `forces_affected`: list of force keys
- `couplings_at_boundary`: dict of coupling values (Fraction) or None
- `known`: True/False/None
- `data4_entry`: string or None
- `papers`: list of strings
- `open_questions`: list of strings

The 19 boundaries (high to low energy): Planck, GUT, Cabibbo Doublet, top, Higgs, M_Z, W, bottom, tau, charm, confinement upper, confinement lower, strange, muon, nuclear binding, electron, atomic, molecular, gravitational dominance.

### Traversal Functions

```python
get_boundary_by_name(name)    # Substring match, returns list of boundary dicts
```

```python
boundaries_between_scales(E_lo_MeV, E_hi_MeV)
```
Returns all boundaries with known or estimated scale between two energies, ordered low to high.

```python
traverse(start_scale_MeV, end_scale_MeV)
```
Full traversal report between two scales.

**Returns:** dict with:
- `boundaries`: list of boundary dicts crossed
- `count`: number of boundaries
- `unknown_couplings`: list of `(boundary_name, coupling_name)` where value is None
- `open_questions`: list of `(boundary_name, question_text)`
- `force_changes`: list of `(boundary_name, forces_affected)`
- `rule_changes`: list of `(boundary_name, what_changes_text)`

```python
# What boundaries exist between the electron and the GUT scale?
report = traverse(m_e, Fraction(10**19, 1))
print("Boundaries crossed:", report["count"])        # 15
print("Unknown couplings:", len(report["unknown_couplings"]))
print("Open questions:", len(report["open_questions"]))

for b in report["boundaries"]:
    print(b["name"])
```

```python
print_traversal(start_MeV, end_MeV)
```
Human-readable traversal report to stdout. Shows every boundary with scale, distance, forces, coupling values (or UNKNOWN), and open questions.

---

## 5. Domain Data Library: phys24_domain_lib.py

**Self-test:** 40/40

**Import:**
```python
from phys24_lib import *
from phys24_domain_lib import *
```

### Core Geometric Constants

```python
R2              # mpf, pi/4
R4              # mpf, pi^2/32
EIGHT_R2        # mpf, 2*pi
FOUR_R2         # mpf, pi
SIXTEEN_R2      # mpf, 4*pi
J11             # mpf, 3.8317 (first zero of J1)
J01             # mpf, 2.4048 (first zero of J0)
AIRY_CONST      # mpf, j11/pi = 1.2197 (the "1.22" in Rayleigh criterion)
C_C_EXACT       # mpf, pi/(pi+2) = 0.61078 (Kirchhoff vena contracta)
C_LIGHT         # mpf, speed of light in m/s
EPSILON_0       # mpf, vacuum permittivity in F/m
C_SOUND_AIR     # mpf, ~343 m/s
```

### Universal Geometry Functions

```python
domain_area(d)                    # R2 * d^2, d in meters → area in m^2
domain_area_from_radius(r)        # 4*R2 * r^2 = pi*r^2
airy_resolution(wavelength, D_or_NA, mode="diameter"|"NA")
                                  # 1.22 * lambda / D (or NA)
spot_area(wavelength, NA)         # R2 * (1.22*lambda/NA)^2
gaussian_peak(total, sigma)       # total / sqrt(8*R2*sigma^2)
fourier_norm()                    # 1/(8*R2) = 1/(2*pi)
gaussian_norm()                   # 1/sqrt(8*R2) = 1/sqrt(2*pi)
```

### Optics Functions

```python
rayleigh_range(w0, wavelength)    # 4*R2*w0^2/lambda
beam_divergence(w0, wavelength)   # lambda/(4*R2*w0)
rayleigh_scattering_loss(wavelength_um, A_coeff=0.8)
                                  # A/lambda^4 in dB/km
fiber_V_number(core_radius, NA, wavelength)
                                  # 8*R2*a*NA/lambda, cutoff at j01=2.405
```

```python
# Is this fiber single-mode at 1310nm?
V = fiber_V_number(mpf("4.1e-6"), mpf("0.14"), mpf("1310e-9"))
# V < 2.405 → single mode
```

### Electrical Functions

```python
wire_resistance(rho, length, diameter)     # rho*L/(R2*d^2)
circular_capacitance(diameter, gap, epsilon_r=1)
                                           # eps0*epsr*R2*d^2/t
```

```python
# RC product cancels R2:
R = wire_resistance(CU_RESISTIVITY, mpf("1"), mpf("2e-3"))
C = circular_capacitance(mpf("2e-3"), mpf("1e-3"))
RC = R * C  # equals rho*eps0*L/t exactly (R2-independent)
```

### Flow and Acoustics Functions

```python
pipe_flow(diameter, velocity)              # R2*d^2*v in m^3/s
orifice_flow(diameter, dP, rho, Cd=None)   # Cd defaults to vena contracta
hagen_poiseuille(diameter, dP, viscosity, length)  # R2*d^4*dP/(32*mu*L)
helmholtz_frequency(port_d, port_l, box_V, c_sound=343)
sound_intensity(power, distance)           # P/(16*R2*r^2)
thermal_radiation(emissivity, temperature, diameter)
```

### RF Functions

```python
antenna_effective_area(gain_linear, wavelength)   # G*lambda^2/(16*R2)
friis_path_loss(distance, wavelength)             # (16*R2*d/lambda)^2
rf_wavelength(frequency_Hz)                       # c/f
fspl_dB(distance_m, frequency_Hz)                 # 20*log10(16*R2*d*f/c)
```

### Semiconductor

```python
litho_resolution(wavelength, NA, k1=None)    # k1*lambda/NA, default k1=0.61
```

### Data Objects

```python
OPTICAL_DISCS      # dict: "CD", "DVD", "Blu-ray" with full specs
FIBER_OPTICS       # dict: "SMF-28" with MFD, NA, cutoff, etc.
DWDM_BANDS         # dict: "O-band", "C-band", "L-band"
SPEAKERS           # dict: "12inch" through "1inch" with d_eff_m
AWG_DATA           # dict: "0000" through "36" with diameter_m, diameter_in
MEMORY_STANDARDS   # dict: "DDR4-1600" through "DDR5-6400"
STORAGE_INTERFACES # dict: "SATA_I" through "PCIe_Gen5"
RF_STANDARDS       # dict: "GPS_L1", "GPS_L2", "5G_15kHz" through "5G_120kHz"
SEMICONDUCTOR      # dict with wafer, lattice, EUV/ArF wavelengths, cell areas
BCS_DATA           # dict with gap ratio (exact and numerical), 4 materials
METROLOGY          # dict with quantum Hall, Josephson, surface roughness
GEODESY            # dict with WGS84, GPS timing
SAMPLE_RATES       # dict: "CD", "studio", "high_res", "ultra" as Fractions
JUST_INTONATION    # dict: 7 intervals as Fractions (2/1, 3/2, 4/3, etc.)
FLOW_CONSTANTS     # dict: vena contracta, standard gravity, atmosphere
MATH_NORMALIZATIONS  # dict: Fourier, Gaussian, Stirling, etc.
```

Disc-specific helpers:
```python
disc_spot_size("Blu-ray")      # 0.581 um
disc_spot_area("CD")           # R2 * spot^2
disc_area("DVD")               # R2 * (0.12)^2
```

Speaker helper:
```python
speaker_cone_area("12inch")    # R2 * (0.305)^2
```

Wire helpers:
```python
awg_area("14")                 # R2 * d^2 for AWG 14
awg_resistance_per_m("12")     # CU_RESISTIVITY / (R2 * d^2)
fiber_mode_area("SMF-28", 1550)  # R2 * MFD^2
```

### R₂ Equation Table and Cancellation Registry

```python
R2_EQUATIONS       # list of 22 dicts, each with domain, equation, Z, precision
R2_CANCELLATIONS   # list of 7 dicts, each with name, formula, status, precision

all_R2_equations()                    # Returns the full list
domains_using("flow")                 # Keyword search across domain, equation, Z
cancellations_where("CANCELS")        # Filter cancellations by status
```

```python
# Cross-domain: what does a 1cm diameter mean in every domain?
cross_domain_area(mpf("0.01"))
# Returns dict with area in m^2/cm^2/mm^2 plus interpretations:
#   pipe flow at 1 m/s, wire resistance per meter,
#   capacitance with 1mm gap, thermal radiation at 300K
```

---

## 6. Demo Scripts

### phys24_demo.py

Demonstrates all four libraries together. Six sections: scale journeys (4 traversals), representation queries (CD vs alternatives), predictions (α_s at 1-loop and 2-loop, sin²θ_W, Koide m_τ), cross-references (DATA-4 lookups, paper searches, particle catalog), unknown map (full electron-to-Planck inventory), BSM candidate comparison table (6 candidates with gap ratios).

**Run:** `python phys24_demo.py` — takes ~10s for two-loop predictions.

### demo_cross_domain.py

Demonstrates R₂ cross-domain translations. Ten sections: optical disc ↔ fiber, speaker ↔ pipe, wire ↔ capacitor, antenna ↔ telescope ↔ lithography, DWDM ↔ Rayleigh scattering, QED coupling ↔ information density, ion implant ↔ Gaussian beam, R₂ cancellation map, all R₂×d² equations in one table, null connections (6 future work items).

**Run:** `python demo_cross_domain.py` — instant.

---

## 7. Verified Check Counts

| Library | Checks | Status |
|---|---|---|
| phys24_lib.py self-test | 21/21 | PASS |
| phys24_lib_test.py | 148/148 | PASS |
| data_4_derivation_lib.py | 37/37 | PASS |
| phys24_structure_lib.py | 46/46 | PASS |
| phys24_boundary_map_lib.py | 14/14 | PASS |
| phys24_domain_lib.py | 40/40 | PASS |
| **Total** | **306/306** | **ALL PASS** |

---

## 8. Import Patterns

```python
# Minimal: just constants and helpers
from phys24_lib import *

# Physics computation: constants + derivations
from phys24_lib import *
from data_4_derivation_lib import *

# Full platform: everything
from phys24_lib import *
from data_4_derivation_lib import *
from phys24_structure_lib import *
from phys24_boundary_map_lib import *
from phys24_domain_lib import *
```

Every library can be run standalone for its self-test:
```bash
python phys24_lib.py              # 21/21
python data_4_derivation_lib.py   # 37/37
python phys24_structure_lib.py    # 46/46
python phys24_boundary_map_lib.py # 14/14
python phys24_domain_lib.py       # 40/40
```

---

## 9. Key Rules (from phys24_script_rules.md)

- All computation in Fraction arithmetic. No `math` module. No `float()`. No `assert`.
- `mpf` at the display boundary only, via `f2m()`.
- All printed numbers via `mp.nstr(value, N)` where N ≥ 11.
- Threshold constants as `mpf("string")`, never Python float literals.
- `mp.dps = 100` standing precision.
- Every constant from phys24_lib, never hardcoded.
- Every script ends with `print_summary(checks)`.

---

*HOWL Platform API Manual. 6 libraries, 306 verified checks, 0 failures. April 3, 2026.*
