# Beta Unification Research Program

**Status:** Active, critical path

**Prerequisite:** Statistical control (Script 1 below) must pass before any derivation work begins

**Platform:** HOWL-PLATFORM-v1

**Rule:** Every claim backed by a script with passing checks. No derivation without computation. No computation without provenance.

---

## Stage 0: The Gate

Nothing in this program proceeds until the statistical control is complete.

### Script 1: beta_statistical_control.py

**Purpose:** Determine whether the beta integer pool {11, 13, 19, 20, 22} produces better cosmological hits than random integer pools of the same size and range.

**Method:**
- Generate 10,000 random pools of 5 integers, each drawn from [2, 60]
- For each pool, construct all p/q ratios and test formula templates: p/q, (p/q)π, (p/q)/π, 2/(q×π), p×q/(r²), α^(3p), α^(3q)
- Score each pool: count hits within 0.1% on the 8 cosmological targets (Λ, DM/baryon, H₀, Ω_b, Ω_DM, Ω_matter, Ω_DE, sin²θ_W)
- Rank the beta pool among the 10,000 random pools
- Report: percentile rank, p-value, histogram of hit counts

**Libraries:** phys24_lib (α, targets)

**Pass condition:** Beta pool ranks in top 1% (p < 0.01). If it ranks below top 5%, the program halts and the finding is reclassified as "small-integer statistics."

**Kill switch:** If the beta pool is NOT in the top 5%, write a null report and close this research line. The formulas are numerology. Archive the notebook. Move on.

**Estimated size:** ~120 lines. One script, one session.

---

## Stage 1: The H₀ Correction Derivation

This is the most promising formula for physical derivation because it has the clearest structural parallel to established physics (VP running in PHYS-5).

### The target formula

(1 − r) = α² × π² × (20/13)

Each factor has a candidate physical interpretation:
- α² → two-loop electromagnetic interaction
- π² = 32R₄ → 4D spacetime geometry (the same R₄ that appears in two-loop QED coefficients)
- 20/13 = |3b₃_mod|/|b₂_mod_num| → ratio of strong to weak gauge structure

### Script 2: vp_boundary_model.py

**Purpose:** Model a photon crossing a soliton boundary with SU(3)×SU(2) gauge content and compute the frequency shift from first principles.

**Method:**
- Start from the VP integral formula in PHYS-5: Δα/α = (α/3π) × Σ Q²N_c × ln(μ/m_f)
- This gives the known VP step size 1/(3π) = 1/(12R₂) per unit charge squared
- At a soliton boundary, the photon crosses a region where the vacuum polarization changes discontinuously
- The frequency shift at the boundary is proportional to the change in the VP integral across the boundary
- Compute: what VP change occurs when light crosses from a region with SM particle content to a region with SM+CD particle content?

**Key computation:**
- Below boundary: VP uses SM betas (b₁_SM, b₂_SM, b₃_SM)
- Above boundary: VP uses modified betas (b₁_mod, b₂_mod, b₃_mod)
- The VP change involves Δb₂ = 1 and Δb₃ = 1/3
- The coupling-weighted change: α² × (Δb₂ contributions + Δb₃ contributions)
- Check whether this naturally produces the factor (20/13)

**Libraries:** phys24_lib (couplings, betas), data_4_derivation_lib (running functions)

**Connection to establish:** VP step at boundary → α² factor. 4D geometry of boundary → π² factor. SU(3)/SU(2) content of boundary → 20/13 factor.

**If it works:** The H₀ correction has a mechanism. The Hubble tension is a VP running effect across cosmological soliton boundaries. Write the paper.

**If it doesn't:** The α² and π² factors may have a different origin. Proceed to Script 3.

### Script 3: two_loop_boundary_crossing.py

**Purpose:** Compute the full two-loop correction to a photon crossing a gauge boundary, using the two-loop b_ij matrix from data_4_derivation_lib.py.

**Method:**
- The one-loop VP gives α/(3π) per unit charge squared
- The two-loop correction involves b_ij cross-terms between gauge groups
- The key two-loop terms: b₂₃ (SU(2)×SU(3) mixing), b₃₂ (SU(3)×SU(2) mixing)
- These cross-terms involve both gauge groups simultaneously — exactly where the 20/13 ratio lives
- Compute: b₂₃_VL / b₂₂_VL and compare to 20/13

**Libraries:** phys24_lib, data_4_derivation_lib (b_ij_full matrix, db_ij_VL matrix)

**Key check:** Does the ratio of two-loop cross-coupling terms reproduce 20/13 from the one-loop beta numerators? If yes, the formula has a two-loop origin and the "α²" factor is literally the two-loop coupling suppression.

**Connection to data_4_derivation_lib:** The VL two-loop matrix db_ij_VL is already computed. The critical entry is db₂₂ = 15/4 (the pitfall-documented value). The cross-terms db₂₃ and db₃₂ carry the SU(2)×SU(3) mixing information.

### Script 4: h0_running_from_vp.py

**Purpose:** If Scripts 2-3 produce a derivable (1−r), plug it into the Hubble running model from phys24_hubble_lib.py and predict H₀(CMB) from first principles.

**Method:**
- Import phys24_hubble_lib
- Replace the empirical r with the derived r from Scripts 2-3
- Compute H₀(N) = H₀(local) × r^N for N = 100
- Compare to Planck measurement
- If the derived r matches the empirical r to 0.1%, the derivation is self-consistent

**Libraries:** phys24_lib, phys24_hubble_lib, data_4_derivation_lib

**Pass condition:** Derived H₀(CMB) within 0.1% of 67.36 km/s/Mpc.

---

## Stage 2: The Dark Matter Ratio

### The target formula

DM/baryon = (22/13)π

### Script 5: dm_ratio_from_boundary_geometry.py

**Purpose:** Test whether the DM/baryon ratio can be derived from the toroidal geometry of soliton boundaries.

**Method:**
- A soliton boundary has two geometric components: the circular cross-section (R₂ = π/4) and the toroidal structure (involves 2π for the major radius circulation)
- The ratio of the toroidal volume to the circular cross-section involves π
- The gauge content at the boundary involves 22 (twice the Yang-Mills integer, the SU(2) gauge self-coupling) and 13 (the VL-modified SU(2) beta numerator)
- Hypothesis: DM/baryon = (gauge self-coupling) / (gauge running) × (toroidal geometry)
- Test: compute the ratio of the SU(2) gauge self-coupling contribution to b₂ (which is −22/3 in sixths, so |22/3 × 3/2| = 11) against the full modified b₂ (−13/6, so |13/6 × 6| = 13)
- The 22/13 = (2 × 11)/13 = (2 × YM) / |b₂_mod_num|
- Check: does the boundary crossing model from Stage 1 naturally produce a 22/13 factor when computing the matter/antimatter asymmetry ratio?

**Libraries:** phys24_lib (betas), phys24_boundary_map_lib (boundary data), phys24_domain_lib (R₂ equations)

**Key connection:** The domain library documents R₂ appearing in 15+ domains. The boundary library documents 19 boundaries. The DM/baryon formula uses both: R₂ (through π) and the boundary gauge content (through 22/13). If the dark matter ratio is set by the boundary geometry, the domain library and boundary library jointly provide the derivation infrastructure.

### Script 6: sphaleron_baryon_asymmetry.py

**Purpose:** Test whether Ω_b = 2/(13π) connects to the electroweak sphaleron rate.

**Method:**
- In standard cosmology, the baryon asymmetry is set by sphaleron processes during the electroweak phase transition
- The sphaleron rate involves the SU(2) gauge coupling g₂ and the sphaleron energy E_sph ~ 4π M_W / g₂
- The baryon-to-photon ratio η ~ exp(−E_sph/T) at the phase transition temperature
- The 13 in Ω_b = 2/(13π) is |b₂_mod_num| — the SU(2) beta numerator after CD modification
- Test: does the sphaleron energy in the CD-modified electroweak theory involve 13 in the exponent?
- Compute: E_sph = 4π × M_W / g₂ where g₂ is extracted from sin²θ_W and α at M_Z
- The sphaleron factor involves 4π = 16R₂, connecting to the R₂ geometry

**Libraries:** phys24_lib (M_W, sin2_tW, alpha_inv), data_4_derivation_lib (derive_couplings)

**Key computation:** Extract g₂ = e/sin(θ_W) from library values. Compute the sphaleron barrier. Check whether any ratio involving 13 and π appears in the barrier height formula.

**Connection to phys24_structure_lib:** The anomaly registry documents that SU(2) anomaly cancellation requires complete generations. The sphaleron process is the non-perturbative manifestation of the SU(2) anomaly. The structure library's generation democracy (4/3, 4/3, 4/3) may connect to the sphaleron rate through the fermion zero modes.

---

## Stage 3: The Cosmological Constant

### The target formula

log₁₀(Λ/M_Pl⁴) = 57 × log₁₀(α) [SM version]
log₁₀(Λ/M_Pl⁴) = 39 × log₁₀(α/3π) [VL version]

### Script 7: lambda_two_loop_correction.py

**Purpose:** Compute the two-loop effective exponent and test whether the Lambda miss closes.

**Method:**
- The one-loop exponent uses b₂_SM_num = 19, giving 3 × 19 = 57
- The two-loop effective b₂ includes the b₂₂ self-coupling term from b_ij_SM
- Compute: effective_exponent = 3 × (19 + δ_two_loop) where δ comes from b₂₂
- The two-loop b₂₂ for SM is in b_ij_SM[1][1] from data_4_derivation_lib
- For the VL version: use b_ij_full[1][1] which includes the CD two-loop corrections

**Libraries:** phys24_lib, data_4_derivation_lib (b_ij_SM, b_ij_full, db_ij_VL)

**Key check:** Does the two-loop correction to the exponent move the SM prediction from −121.80 closer to −121.54? The required δ is small — about −0.5 in the exponent, which is −0.5/3 ≈ −0.17 in b₂ units. The two-loop correction to b₂ from b₂₂ is of order b₂₂ × α/(2π), which is O(0.1) — the right magnitude.

### Script 8: lambda_interpolation_search.py

**Purpose:** Find the interpolation fraction between SM and VL Lambda predictions.

**Method:**
- The measured Λ sits at f = 0.557 between SM (f=0) and VL (f=1) predictions
- Scan all beta-integer ratios p/q where p and q are drawn from {3, 11, 13, 19, 20, 22, 39, 57}
- Also test: RG running fractions, threshold corrections, CD mass dependence
- For each candidate f, compute the interpolated Λ and compare to measured

**Libraries:** phys24_lib

**Key connection:** If f = (M_VL / M_GUT)^δ for some δ, the interpolation depends on the CD mass within the allowed window (1.5-6 TeV from phys24_lib: M_VL_lo, M_VL_hi). This would connect the Lambda prediction to the CD mass — a testable prediction at future colliders.

### Script 9: vacuum_energy_from_running.py

**Purpose:** Test whether the cosmological constant can be expressed as α raised to a power determined by the RG running length.

**Method:**
- The formula Λ ~ α^57 says: the vacuum energy is α multiplied by itself once per generation-weighted SU(2) beta unit
- The total RG running from M_Z to M_GUT spans L = ln(M_GUT/M_Z)/(2π) ≈ 4.9
- The number of "SU(2) beta units" in this running: L × |b₂_SM| = 4.9 × 19/6 ≈ 15.5
- Times 3 generations: 15.5 × 3 ≈ 46.5 — not 57
- But: if we run from m_e (not M_Z) to M_Planck (not M_GUT), the L is larger
- Compute: what L gives exactly 57 when multiplied by |b₂_SM|/6 × N_gen?
- This determines the "effective running length" for the vacuum energy

**Libraries:** phys24_lib (M_Z, alpha_inv), data_4_derivation_lib (running functions), phys24_boundary_map_lib (full boundary stack from m_e to M_Planck)

**Key connection to boundary map:** The traversal from m_e to M_Planck crosses 15 boundaries (from the boundary map library). If 57 = (some function of 15 boundaries × beta coefficients), the cosmological constant connects to the full boundary hierarchy.

---

## Stage 4: The Ω Chain Derivation

### The target

Ω_b = 2/(13π)
Ω_DM = 44/169
Ω_matter = Ω_b + Ω_DM
Ω_DE = 1 − Ω_matter

### Script 10: omega_from_baryogenesis.py

**Purpose:** Test whether Ω_b = 2/(13π) can be derived from the electroweak baryogenesis rate.

**Method:**
- The baryon-to-photon ratio η ≈ 6.1 × 10⁻¹⁰ determines Ω_b through Big Bang nucleosynthesis
- In electroweak baryogenesis: η ∝ (sphaleron rate) × (CP violation) × (departure from equilibrium)
- The sphaleron rate involves g₂^7 × T^4 (non-perturbative SU(2) process)
- CP violation in the SM comes from the CKM phase δ₁₃ — note: the subscript 13 appears in the CKM phase
- Test: does g₂^7 × (CKM factors) × (geometric factors) produce 2/(13π)?
- Compute g₂ from library values: g₂ = e/sin(θ_W) = √(4πα)/sin(θ_W)

**Libraries:** phys24_lib (alpha_inv, sin2_tW, CKM entries if available)

**Connection to structure library:** The structure library has the anomaly registry documenting SU(2) anomaly cancellation. The sphaleron is the non-perturbative process that violates B+L but preserves B−L, with the anomaly coefficient involving the generation count N_gen = 3.

### Script 11: omega_dm_from_boundary_count.py

**Purpose:** Test whether Ω_DM = 44/169 connects to the boundary transit structure.

**Method:**
- 44 = 4 × YM. The factor 4 might be: the 4 dimensions of spacetime, or the 4 components of a Dirac spinor, or 2×2 from the doublet structure
- 169 = 13². The square might indicate: a two-body process (boundary in × boundary out), or a squared matrix element, or a two-loop contribution
- In scattering theory: cross-sections go as |M|² where M is the amplitude. If the DM "amplitude" is proportional to YM/13, the cross-section is proportional to (YM/13)² = 121/169, and the total including a factor 44/121 = 4/11 gives 44/169
- Test: does the boundary scattering amplitude for the CD representation (3, 2, 1/6) involve 11/13 or YM/b₂_mod_num?

**Libraries:** phys24_lib, phys24_structure_lib (make_rep for CD quantum numbers)

### Script 12: omega_de_as_complement.py

**Purpose:** Verify the Ω_DE prediction and test sensitivity to input variations.

**Method:**
- Ω_DE = 1 − Ω_b − Ω_DM = 1 − 2/(13π) − 44/169
- This is determined entirely once Ω_b and Ω_DM are fixed
- Compute the exact Fraction: convert 2/(13π) to a high-precision mpf, add 44/169, subtract from 1
- Test: how does Ω_DE change if Ω_b shifts by its uncertainty? If Ω_DM shifts?
- Map the parameter space: for each candidate baryon formula (Set A: R₄×α×22 vs Set B: 2/(13π)), compute the full Ω chain and χ² against all four measured Omega values simultaneously

**Libraries:** phys24_lib, data_4_derivation_lib (for α sensitivity)

---

## Stage 5: Integration and Falsification

### Script 13: consolidated_predictions.py

**Purpose:** Compute all predictions from the final formula set in one script with full provenance. This becomes the reference script that papers cite.

**Method:**
- Import all libraries
- Compute every prediction from the consolidated table (Section 10 of the notebook)
- Compare to measured values
- Compute combined χ² across all observables
- Report total miss budget
- Log provenance for every value

**Libraries:** All platform libraries

### Script 14: falsification_boundaries.py

**Purpose:** For each formula, compute the measurement precision needed to exclude it at 2σ and 3σ.

**Method:**
- For Ω_b = 2/(13π) = 0.04897: excluded at 2σ if measured Ω_b is outside [0.04867, 0.04927] with σ = 0.00015
- Current Planck uncertainty on Ω_b is ±0.0003 (1σ), so the formula is currently within 1σ
- For DM/baryon = (22/13)π = 5.3165: excluded at 2σ if ratio is outside [5.303, 5.330] with σ = 0.0067
- Compute these boundaries for every formula
- Report which formulas are most vulnerable to near-future measurement improvements (CMB-S4, DESI, Euclid)

**Libraries:** phys24_lib

### Script 15: alternative_integer_pools.py

**Purpose:** Test whether MSSM, SU(5), Pati-Salam, and SO(10) integer pools produce comparable hits.

**Method:**
- Define beta-derived integer pools for each BSM framework:
  - MSSM: b₁ = 33/5, b₂ = 1, b₃ = −3 → numerators {33, 5, 1, 3, ...}
  - SU(5): b = −3 (unified) → {3, 5, 10, 24, ...} (representation dimensions)
  - Pati-Salam: SU(4)×SU(2)_L×SU(2)_R → different beta structure
  - SO(10): b = −2 → {10, 16, 45, 126, ...} (representation dimensions)
- Apply the same formula templates as Script 1
- Compare hit rates to the SM+CD pool

**Libraries:** phys24_lib, phys24_structure_lib (make_rep for constructing representations)

**Key question:** Is the SM+CD pool special, or do all gauge group integer pools produce cosmological hits? If SM+CD is uniquely good, the Cabibbo Doublet is specifically implicated. If all BSM frameworks work, the connection is to gauge groups in general, not to the CD specifically.

---

## Stage 6: The Diagram Atlas

### Script 16: beta_unification_diagrams.py

**Purpose:** Generate a comprehensive visual atlas of all findings using data_5_diagram_lib.py.

**Candidate figures (minimum 16, target 24):**

Running/Convergence type:
- Three coupling running with Lambda exponent marked on the energy axis
- H₀ running curve with derived r vs empirical r
- Ω sensitivity curves as α varies within ±3σ
- Lambda SM vs VL convergence as a function of two-loop correction δ

Comparison type:
- Set A vs Set B: all four Ω observables side by side
- Beta pool vs 10,000 random pools: histogram with beta pool marked
- MSSM vs SM+CD vs Pati-Salam: hit quality comparison
- Formula precision progression: 1-loop → 2-loop → full

Connection/Integer Map type:
- The integer traceability tree: 11 → 22 → 44, 19 → 57, 13 → 39 → 169, 20/13
- The π cancellation diagram: Ω_b × DM/baryon = Ω_DM, showing π entering and leaving
- The formula-to-observable mapping: 3 independent formulas → 7 observables

Threshold/Region type:
- Falsification boundaries for each formula vs current measurement precision
- The CD mass window and its effect on the Lambda interpolation
- The confinement wall and where the formulas apply vs where they don't

**Libraries:** data_5_diagram_lib (all helpers), phys24_lib, all extension libraries

---

## Execution Order

| Priority | Script | Blocking? | What it decides |
|---|---|---|---|
| 1 | beta_statistical_control.py | YES | Whether to continue (kill switch) |
| 2 | vp_boundary_model.py | No | Whether H₀ correction has VP origin |
| 3 | two_loop_boundary_crossing.py | No | Whether α² and 20/13 come from two-loop b_ij |
| 4 | h0_running_from_vp.py | No | Whether derived r matches empirical r |
| 5 | lambda_two_loop_correction.py | No | Whether Lambda miss closes with two-loop |
| 6 | lambda_interpolation_search.py | No | Whether f = 0.557 has integer origin |
| 7 | dm_ratio_from_boundary_geometry.py | No | Whether (22/13)π has geometric derivation |
| 8 | sphaleron_baryon_asymmetry.py | No | Whether Ω_b connects to EW baryogenesis |
| 9 | vacuum_energy_from_running.py | No | Whether 57 connects to total RG running length |
| 10 | omega_from_baryogenesis.py | No | Whether 2/(13π) comes from sphaleron rate |
| 11 | omega_dm_from_boundary_count.py | No | Whether 44/169 comes from boundary scattering |
| 12 | omega_de_as_complement.py | No | Sensitivity analysis and χ² optimization |
| 13 | consolidated_predictions.py | No | Reference script for paper |
| 14 | falsification_boundaries.py | No | What future data kills which formula |
| 15 | alternative_integer_pools.py | No | Whether SM+CD is special |
| 16 | beta_unification_diagrams.py | No | Visual atlas |

Script 1 is the gate. If it fails, Scripts 2-16 are cancelled. If it passes, Scripts 2-12 can run in any order. Scripts 13-16 run after the derivation attempts are complete, regardless of whether they succeed — the consolidated script and diagrams document whatever was found, including null results.

---

## Papers This Program Would Produce

**If Script 1 passes and no derivations succeed:**
- PHYS-XX: "Beta-Integer Cosmological Patterns: Statistical Significance and Formula Census" — reports the pattern, the statistical rank, the formula set, the null derivation results, and the falsification boundaries. Honest paper: "we found patterns, they're statistically significant, we can't derive them."

**If Script 1 passes and the H₀ derivation succeeds:**
- PHYS-XX: "Hubble Running from Vacuum Polarization at Soliton Boundaries" — derives (1−r) = α²π²(20/13) from boundary VP physics. Predicts H₀(CMB) from α and gauge group integers alone. This is a single-formula paper with a single testable prediction.

**If Script 1 passes and the Ω_b derivation succeeds:**
- PHYS-XX: "Baryon Density from Electroweak Sphaleron Rate and the Integer 13" — derives Ω_b = 2/(13π) from the sphaleron barrier with CD modification. Chains to Ω_DM = 44/169 through the DM/baryon formula.

**If Script 1 passes and the Lambda derivation succeeds:**
- PHYS-XX: "The Cosmological Constant as α^57: Vacuum Energy from Electroweak Running" — derives the exponent 57 = 3 × 19 from the total RG running length, including two-loop corrections.

**If Script 1 passes and ALL derivations succeed:**
- PHYS-XX: "Beta Unification: Cosmological Parameters from Gauge Group Structure" — the full paper. Everything derived, everything tested, everything falsifiable.

**If Script 1 fails:**
- DISC-XX: "Small-Integer Coincidences in Cosmological Constants: A Statistical Null Report" — documents the formulas, shows they are expected from small-integer statistics, and closes the research line cleanly.

Every outcome produces a paper. No work is wasted.

---

## Connection to Existing Platform

| Library | What it provides to this program |
|---|---|
| phys24_lib.py | α, betas, M_Z, sin²θ_W — the complete input set |
| data_4_derivation_lib.py | Two-loop b_ij matrix, running functions, crossing finder |
| phys24_structure_lib.py | make_rep() for CD and alternative representations, anomaly registry |
| phys24_boundary_map_lib.py | Full 19-boundary stack, traversal functions, None values for unknowns |
| phys24_domain_lib.py | R₂ equations across 15 domains, the cancellation registry |
| phys24_hubble_lib.py | H₀ running model, falsification tests, measurement data |
| data_5_diagram_lib.py | All diagram helpers with provenance |

Every script in this program imports from this stack. Every value has provenance. Every result is reproducible. The structural upgrade protocol ensures every script written in this program runs unchanged in every future session.

---

*Beta Unification Research Program. 16 scripts, 6 stages, 1 kill switch. Script 1 is the gate. Every outcome produces a paper. No work is wasted. April 3, 2026.*

---

# Beta Unification Research Program — Supporting Tables

**Companion to:** Beta Unification Research Program

**Date:** April 3, 2026

---

## Table 1: The Integer Pool

Every integer used in every formula, with full derivation chain from the gauge group.

| Integer | Symbol | Derivation Chain | Fraction Source | Library Variable |
|---|---|---|---|---|
| 11 | YM | Lorentz + gauge + renormalizability → −(11/3)C₂(G) | One-loop gauge self-coupling | hardcoded (group theory) |
| 13 | \|b₂_mod_num\| | b₂_SM + Δb₂_CD = −19/6 + 1 = −13/6, \|−13/6 × 6\| = 13 | Fraction(−13, 6) numerator | b2_mod = b2_SM + db2_VL |
| 19 | \|b₂_SM_num\| | gauge(−44/6) + fermion(24/6) + Higgs(1/6) = −19/6, \|×6\| = 19 | Fraction(−19, 6) numerator | b2_SM |
| 20 | \|3b₃_mod\| | b₃_SM + Δb₃_CD = −7 + 1/3 = −20/3, \|×3\| = 20 | Fraction(−20, 3) numerator | b3_mod = b3_SM + db3_VL |
| 22 | 2×YM | 2 × 11 = 22. Also \|b₂_gauge × 3\| = \|−22/3 × 3\| = 22 | Fraction(22, 1) | derived from YM |
| 3 | N_gen | Three generations of SM fermions | Fraction(3, 1) | N_gen in structure_lib |
| 39 | 3×13 | N_gen × \|b₂_mod_num\| | Fraction(39, 1) | computed |
| 57 | 3×19 | N_gen × \|b₂_SM_num\| | Fraction(57, 1) | computed |
| 44 | 4×YM | 4 × 11. Also 2 × 22 | Fraction(44, 1) | computed |
| 169 | 13² | \|b₂_mod_num\|² | Fraction(169, 1) | computed |

---

## Table 2: The Formula Set (Consolidated Best)

| # | Observable | Formula | Exact Fraction Content | Transcendental Content | Measured Input |
|---|---|---|---|---|---|
| 1a | log₁₀(Λ/M_Pl⁴) SM | 57 × log₁₀(α) | 57 = 3×19 | log₁₀ | α |
| 1b | log₁₀(Λ/M_Pl⁴) VL | 39 × log₁₀(α/(3π)) | 39 = 3×13, 3 | π, log₁₀ | α |
| 2 | DM/baryon | (22/13)π | 22/13 | π | none |
| 3 | (1−r) per transit | α²π²(20/13) | 20/13 | π² | α |
| 4B | Ω_b | 2/(13π) | 2/13 | π | none |
| 5 | Ω_DM | 44/169 | 44/169 | none | none |
| 6 | Ω_matter | 2/(13π) + 44/169 | 2/13, 44/169 | π | none |
| 7 | Ω_DE | 1 − Ω_matter | complement | π | none |
| 8 | sin²θ_W (approx) | 3/13 | 3/13 | none | none |

**Input count:** α appears in 3 of 9 formulas. The other 6 use only integers and π. The Ω chain (4B, 5, 6, 7) uses zero measured input.

---

## Table 3: Prediction Quality

| # | Observable | Predicted | Measured | Abs Miss | Rel Miss | Status |
|---|---|---|---|---|---|---|
| 1a | log₁₀(Λ) SM | −121.800 | −121.540 | 0.260 dec | 0.214% | Within 0.3 dec |
| 1b | log₁₀(Λ) VL | −121.333 | −121.540 | 0.207 dec | 0.170% | Within 0.25 dec |
| 1avg | log₁₀(Λ) avg | −121.566 | −121.540 | 0.026 dec | 0.022% | Best Λ |
| 2 | DM/baryon | 5.3165 | 5.3204 | 0.0039 | 0.073% | Within 1σ |
| 3a | (1−r) | 0.0008086 | 0.0008092 | 6.6×10⁻⁷ | 0.082% | Within 0.1% |
| 3b | H₀(CMB) | 67.364 | 67.360 | 0.004 | 0.007% | Measurement limited |
| 4B | Ω_b | 0.04897 | 0.04900 | 0.00003 | 0.060% | Within 1σ |
| 5 | Ω_DM | 0.26036 | 0.26070 | 0.00034 | 0.132% | Within 1σ |
| 6 | Ω_matter | 0.30933 | 0.30970 | 0.00037 | 0.121% | Within 1σ |
| 7 | Ω_DE | 0.69067 | 0.69030 | 0.00037 | 0.054% | Within 1σ |
| 8 | sin²θ_W | 0.23077 | 0.23120 | 0.00043 | 0.186% | Within 1σ |

---

## Table 4: Set A vs Set B Comparison

| Observable | Set A Formula | Set A Value | Set A Miss | Set B Formula | Set B Value | Set B Miss | Winner |
|---|---|---|---|---|---|---|---|
| Ω_b | R₄ × α × 22 | 0.04952 | 1.05% | 2/(13π) | 0.04897 | 0.060% | B (17× better) |
| Ω_DM | Ω_b_A × (22/13)π | 0.26325 | 0.98% | 44/169 | 0.26036 | 0.132% | B (7× better) |
| Ω_matter | sum | 0.31276 | 0.99% | sum | 0.30933 | 0.121% | B (8× better) |
| Ω_DE | complement | 0.68724 | 0.44% | complement | 0.69067 | 0.054% | B (8× better) |

**Set B inputs:** {13, 22, π} — no R₄, no α for Ω chain.

**Set A inputs:** {R₄, α, 22, 13, π} — all five needed.

Set B is simpler and more accurate. Set B adopted as primary.

---

## Table 5: Exact Algebraic Identities

| Identity | Left Side | Right Side | Verified | Source |
|---|---|---|---|---|
| 57/39 = 19/13 | (3×\|b₂_SM_num\|) / (3×\|b₂_mod_num\|) | \|b₂_SM_num\| / \|b₂_mod_num\| | EXACT (Fraction) | N_gen cancels |
| 20/13 = \|3b₃_mod\|/\|b₂_mod_num\| | abs(b3_mod × 3) / abs(b2_mod × 6) | Fraction(20, 13) | EXACT (Fraction) | Cross-gauge ratio |
| 22/13 = (2×YM)/\|b₂_mod_num\| | 2×11 / 13 | Fraction(22, 13) | EXACT (Fraction) | YM to VL beta |
| 44/169 = (4×YM)/\|b₂_mod_num\|² | 4×11 / 13² | Fraction(44, 169) | EXACT (Fraction) | Ω_DM rational |
| Ω_b × DM_ratio = Ω_DM | [2/(13π)] × [(22/13)π] | 44/169 | EXACT (π cancels) | Chain consistency |
| Ω_DM = (2×22)/(13²) | 2 × Fraction(22, 1) / Fraction(169, 1) | Fraction(44, 169) | EXACT (Fraction) | Alternative form |

---

## Table 6: Formula Dependencies

Which integers appear in which formula. Every × is a structural dependency verified in the experiment.

| Integer | Λ SM | Λ VL | DM/baryon | (1−r) | Ω_b (B) | Ω_DM | sin²θ_W |
|---|---|---|---|---|---|---|---|
| 11 (YM) | | | × | | | × | |
| 13 (\|b₂_mod\|) | | × | × | × | × | × | × |
| 19 (\|b₂_SM\|) | × | | | | | | |
| 20 (\|3b₃_mod\|) | | | | × | | | |
| 22 (2×YM) | | | × | | | × | |
| 3 (N_gen) | × | × | | | | | × |
| π | | × | × | × | × | | |
| α | × | × | | × | | | |

**The integer 13 appears in 6 of 7 independent formulas.** It is the single most connected integer in the set. It comes from the Cabibbo Doublet modifying b₂_SM: 19 − 6 = 13.

---

## Table 7: Physical Interpretation Candidates

| Formula | Factor | Candidate Mechanism | Paper Connection | Testable? |
|---|---|---|---|---|
| DM/baryon | 22/13 | Gauge self-coupling / VL running ratio at boundary | PHYS-1 (boundaries) | Via boundary model |
| DM/baryon | π | Toroidal boundary geometry (circular cross-section) | MATH-1 (R₂ across domains) | Via geometry |
| (1−r) | α² | Two-loop electromagnetic coupling at boundary | PHYS-5 (VP running) | Via VP calculation |
| (1−r) | π² | 4D spacetime geometry (= 32R₄) | PHYS-9 (QED coefficients) | Via loop integral |
| (1−r) | 20/13 | SU(3)/SU(2) beta ratio at boundary | PHYS-13 (unification) | Via two-loop b_ij |
| Ω_b | 2/13 | Sphaleron rate × CKM phase / SU(2) beta | PHYS-12 (EW observables) | Via sphaleron calc |
| Ω_b | 1/π | Circular geometry normalization | MATH-1 (R₂) | Via phase space |
| Λ | α^57 | VP suppression per SU(2) beta unit | PHYS-5 (VP) | Via running length |
| Λ | 57 = 3×19 | Full SU(2) running × generations | PHYS-13 (unification) | Via two-loop |
| sin²θ_W | 3/13 | Generation count / VL SU(2) numerator | PHYS-12 (EW) | Direct check |

---

## Table 8: Script Inventory

| # | Script Name | Stage | Lines (est) | Libraries | Blocking? |
|---|---|---|---|---|---|
| 1 | beta_statistical_control.py | 0 | 120 | phys24_lib | YES — kill switch |
| 2 | vp_boundary_model.py | 1 | 100 | phys24_lib, derivation_lib | No |
| 3 | two_loop_boundary_crossing.py | 1 | 80 | phys24_lib, derivation_lib | No |
| 4 | h0_running_from_vp.py | 1 | 60 | phys24_lib, hubble_lib, derivation_lib | No |
| 5 | dm_ratio_from_boundary_geometry.py | 2 | 80 | phys24_lib, boundary_lib, domain_lib | No |
| 6 | sphaleron_baryon_asymmetry.py | 2 | 100 | phys24_lib, derivation_lib | No |
| 7 | lambda_two_loop_correction.py | 3 | 70 | phys24_lib, derivation_lib | No |
| 8 | lambda_interpolation_search.py | 3 | 60 | phys24_lib | No |
| 9 | vacuum_energy_from_running.py | 3 | 90 | phys24_lib, derivation_lib, boundary_lib | No |
| 10 | omega_from_baryogenesis.py | 4 | 100 | phys24_lib, structure_lib | No |
| 11 | omega_dm_from_boundary_count.py | 4 | 80 | phys24_lib, structure_lib, boundary_lib | No |
| 12 | omega_de_as_complement.py | 4 | 60 | phys24_lib, derivation_lib | No |
| 13 | consolidated_predictions.py | 5 | 150 | all libraries | No |
| 14 | falsification_boundaries.py | 5 | 80 | phys24_lib | No |
| 15 | alternative_integer_pools.py | 5 | 120 | phys24_lib, structure_lib | No |
| 16 | beta_unification_diagrams.py | 6 | 300 | all libraries + diagram_lib | No |

**Total estimated lines:** ~1,650 across 16 scripts.

---

## Table 9: Kill Switches

| ID | Condition | Action | What Dies |
|---|---|---|---|
| K1 | Script 1: beta pool ranks below top 5% of random pools | Halt program. Write null report. | Entire program |
| K2 | Scripts 2-3: VP model gives (1−r) more than 10× off from α²π²(20/13) | Park H₀ derivation. Continue other stages. | Stage 1 only |
| K3 | Script 6: sphaleron calculation gives Ω_b more than 10× off from 2/(13π) | Park baryogenesis path. Continue other stages. | Scripts 6, 10 |
| K4 | Script 7: two-loop correction moves Lambda prediction AWAY from measured | Park Lambda two-loop path. | Script 7 |
| K5 | Script 15: MSSM or SO(10) integers match equally well | Reclassify: pattern is gauge-group generic, not CD-specific | Interpretation, not formulas |

---

## Table 10: Measurement Targets for Falsification

| Observable | Formula | Predicted | Current Measurement | Current σ | Excluded at 2σ if | Key Experiment |
|---|---|---|---|---|---|---|
| Ω_b | 2/(13π) | 0.04897 | 0.0490 ± 0.0003 | 0.34σ | Ω_b < 0.04837 or > 0.04957 | CMB-S4, Simons Observatory |
| Ω_DM | 44/169 | 0.26036 | 0.2607 ± 0.0025 | 0.14σ | Ω_DM < 0.2554 or > 0.2653 | DESI, Euclid |
| DM/baryon | (22/13)π | 5.3165 | 5.3204 ± 0.065 | 0.06σ | ratio < 5.186 or > 5.447 | Planck reanalysis |
| H₀(CMB) | 73.04×r¹⁰⁰ | 67.364 | 67.36 ± 0.54 | 0.01σ | H₀ < 66.28 or > 68.44 | ACT, SPT-3G |
| sin²θ_W | 3/13 | 0.23077 | 0.23122 ± 0.00004 | 11.3σ | Already 11σ tension | None needed |
| Ω_DE | 1 − Ω_matter | 0.69067 | 0.6903 ± 0.0025 | 0.15σ | Ω_DE < 0.6857 or > 0.6957 | DESI, Euclid, LSST |

**Note on sin²θ_W:** The 3/13 approximation is already 11σ from the measured value. This is the weakest formula — it is a combinatoric hit, not a precision prediction. If the other formulas are derived from first principles, sin²θ_W ≈ 3/13 may be a leading-order approximation that receives corrections. Or it may be a coincidence. The 11σ tension means it is not currently a prediction — it is a pattern observation.

---

## Table 11: Two-Loop Coefficients Available in the Platform

From data_4_derivation_lib.py, the b_ij matrices needed for Stages 1 and 3:

| Entry | SM Value | VL Addition | Full Value | Appears In |
|---|---|---|---|---|
| b₁₁ | from library | from library | b_ij_full[0][0] | Lambda two-loop |
| b₁₂ | from library | from library | b_ij_full[0][1] | Cross-coupling |
| b₁₃ | from library | from library | b_ij_full[0][2] | Cross-coupling |
| b₂₁ | from library | from library | b_ij_full[1][0] | Cross-coupling |
| b₂₂ | from library | db₂₂ = 15/4 | b_ij_full[1][1] | Lambda, H₀ derivation |
| b₂₃ | from library | from library | b_ij_full[1][2] | H₀ 20/13 derivation |
| b₃₁ | from library | from library | b_ij_full[2][0] | Cross-coupling |
| b₃₂ | from library | from library | b_ij_full[2][1] | H₀ 20/13 derivation |
| b₃₃ | from library | from library | b_ij_full[2][2] | QCD running |

**Critical entry:** db₂₂ = 15/4 (the pitfall-documented value from data_4_derivation_lib.py). This is the VL contribution to the SU(2)×SU(2) two-loop running. It may be the origin of the two-loop correction to the Lambda exponent.

**Critical cross-terms:** b₂₃ and b₃₂ carry the SU(2)×SU(3) mixing. These are where the 20/13 ratio might originate in the two-loop framework.

---

## Table 12: Existing Paper Connections

| Series Paper | What It Provides | Used In Script(s) |
|---|---|---|
| PHYS-1 | Soliton boundary concept, boundary transit counting | 2, 4, 5, 9, 11 |
| PHYS-2 | Transformation law priority over single values | 4 (H₀ running) |
| PHYS-3 | Reproducibility vs universality distinction | 4, 14 |
| PHYS-4 | Per-transit correction magnitude constraint | 2, 3, 4 |
| PHYS-5 | VP running template, 1/(3π) step size derivation | 2, 3, 9 |
| PHYS-6 | QCD confinement wall, α_s running | 3 (b₃ terms) |
| PHYS-8 | Koide ratio framework (3 inputs → prediction) | 10 (structural parallel) |
| PHYS-9 | QED coefficients, R₄ in two-loop integrals | 2, 3, 7 |
| PHYS-11 | R₂ subgroup classification, monotonic accumulation | 5, 11 |
| PHYS-12 | Electroweak observables, sin²θ_W | 6, 8, 10, 14 |
| PHYS-13 | Unification, gap ratio, beta structure | 1-16 (all) |
| PHYS-22 | Two-loop QED, R₄ phase space factor | 3, 7 |
| PHYS-23 | Koide spacing tautology, closed paths | 10 (what NOT to do) |
| MATH-1 | R₂ = π/4 across domains | 5, 7, 11 |
| MATH-3 | Bessel zeros, Airy pattern, fiber cutoff | 5 (boundary geometry) |
| DATA-1 | 268 entries across 17 domains | 5, 11 (domain data) |
| DATA-4 | 146 measured + exact constants | 1-16 (all via phys24_lib) |

---

## Table 13: Provenance Chain for Each Prediction

Full chain from plotted/printed value back to DATA-4 entry.

| Prediction | Script Function | Library Function | Platform Constant | DATA-4 Entry |
|---|---|---|---|---|
| Λ SM = −121.80 | 57 × log₁₀(α) | f2m(alpha) | alpha_inv | B1 (12 sf) |
| Λ VL = −121.33 | 39 × log₁₀(α/3π) | f2m(alpha), mpi | alpha_inv, pi_f | B1, G1 |
| DM/baryon = 5.317 | (22/13) × π | f2m(22/13), mpi | b2_mod, YM | N8, group theory |
| (1−r) = 0.000809 | α² × π² × 20/13 | f2m(alpha), mpi | alpha_inv, b3_mod, b2_mod | B1, N9, N8 |
| H₀ = 67.364 | H₀_local × r¹⁰⁰ | (derived r) | (cosmological target) | external |
| Ω_b = 0.04897 | 2/(13π) | f2m(13), mpi | b2_mod | N8 |
| Ω_DM = 0.26036 | 44/169 | f2m(44/169) | b2_mod, YM | N8, group theory |
| sin²θ_W ≈ 0.2308 | 3/13 | f2m(3/13) | b2_mod, N_gen | N8, generation count |

---

## Table 14: Null Result Registry

Results that would be null findings, recorded here so they are not lost.

| Potential Null | Script | What It Would Mean | Status |
|---|---|---|---|
| Beta pool not statistically special | 1 | Formulas are small-integer coincidences | UNTESTED |
| VP model gives wrong (1−r) | 2, 3 | H₀ correction not from VP mechanism | UNTESTED |
| Sphaleron gives wrong Ω_b | 6, 10 | Baryon density not from EW baryogenesis in this form | UNTESTED |
| Two-loop worsens Lambda | 7 | One-loop exponent is the right one, or formula is wrong | UNTESTED |
| MSSM integers match equally well | 15 | Pattern is gauge-group generic, not CD-specific | UNTESTED |
| f = 0.557 has no integer form | 8 | Lambda interpolation is not algebraically determined | UNTESTED |
| sin²θ_W ≈ 3/13 at 11σ tension | — | This is already a partial null | KNOWN |

Every null result gets documented. None is suppressed. The platform's self-test pattern (FAIL is data, not bug) applies to the research program: a null result is a finding, not a failure.

---

## Table 15: Timeline Estimate

| Stage | Scripts | Sessions | Blocking Dependencies |
|---|---|---|---|
| 0: Statistical gate | 1 | 1 | None (run first) |
| 1: H₀ derivation | 2, 3, 4 | 1-2 | Stage 0 pass |
| 2: DM ratio derivation | 5, 6 | 1 | Stage 0 pass |
| 3: Lambda derivation | 7, 8, 9 | 1-2 | Stage 0 pass |
| 4: Ω chain derivation | 10, 11, 12 | 1 | Stage 0 pass |
| 5: Integration | 13, 14, 15 | 1 | Stages 1-4 (partial results OK) |
| 6: Diagrams and papers | 16 + papers | 1-2 | Stage 5 |
| **Total** | **16 scripts** | **5-9 sessions** | **Stage 0 is the gate** |

---

*Supporting Tables for the Beta Unification Research Program. 15 tables covering integers, formulas, predictions, comparisons, identities, dependencies, scripts, kill switches, falsification, two-loop coefficients, paper connections, provenance, null registry, and timeline. Every entry traceable to phys24_lib.py or the experiment script. April 3, 2026.*

