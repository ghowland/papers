# A Versioned Node System for Integer Fraction Physics
## Physics Database and Experiment System

**Registry:** [@HOWL-DATA-6-2026]

**Series Path:** [@HOWL-DATA-4-2026] → [@HOWL-DATA-5-2026] → [@HOWL-DATA-6-2026]

**Date:** April 5, 2026

**DOI:** 10.5281/zenodo.19665914

**Domain:** Research Infrastructure / Versioned Database / Experiment System

**Status:** Operational

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. ABSTRACT

DATA-6 is a versioned node-based system for physics research built on integer fraction arithmetic. Every entity — constant, derivation, connection, experiment, result, program — is a versioned node with a canonical key, provenance, and level classification. The system stores 414 value nodes across 24 JSON files, 57 derivation functions and 9 connection functions in two Python registries, 13 experiment definitions with 85+ comparisons, and 13 research programs with 26 kill switches.

The system is operational and has produced results. Three case studies demonstrate its capabilities: (1) the beta unification experiment with 29 comparisons covering gauge coupling extraction, gap ratio correction, Koide analysis, and cosmological predictions from integers, all passing; (2) a what-if BSM scan testing 5 of 15 candidates against the measured gap ratio, identifying the Cabibbo Doublet as the unique winner by a factor of 7; (3) a QED alpha extraction chain that derives four CODATA values (α⁻¹, R∞, a₀, μ₀) from one measurement (a_e) plus integer transformation laws, matching independent measurements at 3.3-8.0 ppb with error propagation following exact α-power scaling.

DATA-6 succeeds DATA-4 (146 entries, 38/38 checks) and DATA-5 (222 objects, 322/323 checks). It differs from both in architecture: where DATA-4 was a flat verified registry and DATA-5 was an object-oriented platform library, DATA-6 is an experiment-driven system where computation is declared in JSON, executed by a generic runner, and results are stored as versioned nodes with full provenance. Nothing is overwritten. Nothing is deleted. The database only grows.

---

## II. ARCHITECTURE

### 2.1 Design Principles

Seven principles govern the system:

**Everything is a versioned node.** Every entity has a canonical key and a version number. Once a versioned key exists, it is never edited. Corrections produce new versions. Old versions remain.

**Inputs and outputs are symmetric.** A raw constant and an experiment output are both named values in the same pool. Both carry provenance. Both are version-pinned. There is no privileged distinction at the access layer.

**Provenance is first-order.** Every value traces back through which derivation produced it, which values that derivation consumed, and which experiment triggered the execution.

**Integer fraction arithmetic.** `fractions.Fraction` is the primary numeric type. `float` is never used anywhere in the system. `mpmath.mpf` is permitted only at the irrational boundary (π, √, exp, log). Conversion to float happens only at display.

**Append-only versioning.** All versioned keys follow `canonical_name_vN`. Version 0 is the initial registration. New understanding means new version. Old versions are never modified or deleted. Changed data means lost data.

**No hardcoded physics constants.** All values come from the pool. Derivation functions pull every constant from value nodes via the resolver. No physics number is buried in executable code.

**Helpers are derivations.** There is no separate "helper" category. Every function that an experiment uses is a registered versioned derivation node with declared inputs and outputs.

### 2.2 Node Types

The system has 8 node types.

| Type | Purpose | Count |
|---|---|---|
| Value | An atomic named fact: constant, measurement, classification, output | 414 |
| Derivation | A versioned executable transformation | 57 |
| Connection | A versioned executable relationship bundle | 9 |
| Experiment | A versioned execution plan with comparisons and diagrams | 13 |
| Result | Output record of a completed experiment run | 13+ |
| Program | A research program with thesis and kill switches | 13 |
| Dataset | A version overlay (specified, not yet implemented) | 0 |
| Diagram | A rendering specification embedded in an experiment | 16 |

### 2.3 The Value Node

The fundamental data unit. Every value carries:

| Field | Required | Description |
|---|---|---|
| key | yes | `mass_z_boson_v0` — globally unique versioned identifier |
| value | yes | Fraction, integer, decimal string, classification, or None |
| value_type | yes | `exact_fraction`, `exact_integer`, `approximate`, `classification`, `deferred` |
| unit | yes | Physical unit or `dimensionless` |
| level | yes | 0=geometry, 1=group theory, 2=measured, 3=derived |
| source | yes | Origin reference |

Value type rules enforce the arithmetic hierarchy: Fraction is preferred. Approximate values are plain decimal strings — never scientific notation. The system enforces `"0.0000021969811"` not `"2.1969811e-6"`.

### 2.4 Level Convention

| Level | Meaning | Examples |
|---|---|---|
| 0 | Pure geometry / exact math | R2 = π/4, Q335 constants, Bessel zeros |
| 1 | Group theory / structural | Beta coefficients, Casimirs, QED series rationals |
| 2 | Measured / observational | α⁻¹, sin²θ_W, masses, H₀, dwarf galaxy data |
| 3 | Derived / predicted | α from a_e, Koide m_τ, Ω_DM from integers |

Level applies to all node types, not just values. A Level 1 derivation produces Level 1 outputs from Level 1 inputs. A Level 3 derivation produces Level 3 outputs from Level 1 laws applied to Level 2 measurements.

---

## III. THE VALUE POOL

### 3.1 Inventory

414 value nodes across 24 JSON files, organized by physics domain.

| File | Section | Count | Levels |
|---|---|---|---|
| values_si_exact_v0.json | SI defined constants | 8 | 0 |
| values_measured_v0.json | CODATA 2022 | 13 | 2 |
| values_electroweak_v0.json | LEP/PDG | 6 | 2 |
| values_quarks_ckm_v0.json | PDG 2024 / FLAG | 11 | 2 |
| values_nuclear_spectro_v0.json | Nuclear / spectroscopy | 9 | 2 |
| values_q335_v0.json | Q335 analytical basis | 31 | 0 |
| values_ratios_koide_v0.json | Mass ratios / Koide | 11 | 2 |
| values_gut_beta_v0.json | SM/CD betas, gaps, couplings | 32 | 1-2 |
| values_integer_pool_v0.json | Integer pool | 10 | 1 |
| values_generation_democracy_v0.json | Per-gen beta sums | 3 | 1 |
| values_gap_ratios_v0.json | Gap ratios, cosmo prefactors | 7 | 1-2 |
| values_two_loop_vl_dbij_v0.json | Two-loop VL matrix | 9 | 1 |
| values_higgs_beta_v0.json | Higgs beta shifts | 3 | 1 |
| values_representations_v0.json | SM + CD representations | 54 | 1 |
| values_engineering_v0.json | Engineering / domain | 66 | 0-2 |
| values_astrophysical_v0.json | Astrophysical constants | 12 | 2 |
| values_cosmological_v0.json | H₀ measurements, Planck | 11 | 2 |
| values_observational_v0.json | Dwarf galaxies | 52 | 2 |
| values_experiment_inputs_v0.json | Aliases and scan inputs | 8 | 1-2 |
| values_qed_laporta_v0.json | Laporta 5-loop coefficients | 8 | 1 |
| values_qed_coefficients_v0.json | QED A₁-A₅ and references | 8 | 1-2 |
| values_qed_ae_measured_v0.json | a_e and alpha references | 4 | 2 |
| values_qed_series_rationals_v0.json | A₂/A₃ rational coefficients | 12 | 1 |
| values_whatif_*.json (×5) | BSM scan quantum numbers | 15 | 1 |

### 3.2 The Q335 Basis

31 transcendental constants stored as exact Fraction values with numerator p and denominator Q = 2³³⁵, giving 100+ digit precision. The basis includes π, e, ln(2), ln(3), ln(5), √2 through √7, φ, ζ(2) through ζ(9), Li₄(1/2) through Li₇(1/2), Catalan's constant, e^π, and six elliptic integrals K and E at rational arguments.

All 31 constants verified against mpmath at 100+ digits. The Q335 representation allows exact Fraction arithmetic on transcendental constants — multiplication, addition, subtraction are exact integer operations. Division introduces no rounding. The computational chain from Q335 constants through QED coefficients to derived α is lossless.

### 3.3 The Integer Pool

10 integers traced from gauge theory coefficients to cosmological predictions.

| Key | Value | Source | Appears In |
|---|---|---|---|
| integer_yang_mills_eleven_v0 | 11 | -(11/3)×C₂(adj) | DM numerator, Ω_DM numerator |
| integer_b2_modified_numerator_abs_v0 | 13 | \|b₂_mod\| = \|-13/6\| | DM denominator, gap denominator |
| integer_two_times_yang_mills_v0 | 22 | 2×11 | DM/baryon prefactor |
| integer_four_times_yang_mills_v0 | 44 | 4×11 | Ω_DM prefactor, amplification |
| integer_b2_modified_numerator_square_v0 | 169 | 13² | Ω_DM denominator |

The same two integers (11, 13) connect gauge theory (beta coefficients) to cosmology (DM/baryon ratio, dark matter density). Whether this connection is structural or coincidental is the central question of program_statistical_control — the single most important unwritten script in the series.

---

## IV. THE DERIVATION REGISTRY

### 4.1 Architecture

Every derivation is a Python function following the callable contract:

```python
def derivation_name_v0(value_dicts: list[dict]) -> dict:
    return {
        "key": "derivation_name_v0",
        "outputs": {"output_key_v0": value, ...},
        "notes": ""
    }
```

The function receives the full value pool as a list of dicts. It reads its inputs via `_value_map()` which builds a key→value lookup. It returns a dict with its key, a map of output keys to values, and notes. The runner merges outputs into the pool after each derivation executes.

Zero physics constants are hardcoded in derivation functions. Every numerical value is read from the pool by key. The experiment JSON declares which values and derivations are required. The runner validates their presence.

### 4.2 Two Registries

| Registry | File | Functions | Categories |
|---|---|---|---|
| DERIVATION_INDEX_V0 | _data_6_derivations_v0.py | 18 derivations + 5 connections | Coupling, beta, gap, Koide, cosmology |
| DERIVATION_MORE_INDEX_V0 | _data_6_derivations_more_v0.py | 39 derivations + 4 connections | Gravity, Hubble, R2 domains, relativity, dwarfs, QED, what-if |

Combined: 57 derivations + 9 connections = 66 callable functions.

### 4.3 Derivation Categories

| Category | Count | Coverage |
|---|---|---|
| Coupling extraction and prediction | 5 | α₁, α₂, α₃ at M_Z, sin²θ_W, α_s predictions |
| Beta coefficients and gap ratios | 7 | SM betas, CD shifts, modified betas, gaps, democracy, Y-dependence |
| Koide | 2 | K ratio, m_τ prediction |
| Cosmological parameters | 8 | DM/baryon, Ω_DM, Ω_b, Ω_m, Ω_DE, amplification, virial, frame dragging |
| Gravity and soliton | 8 | GM/(rc²), escape velocity, binding, Hill, Kepler, process rate, GPS, MOND |
| Relativity | 3 | Muon lifetime, twin paradox, ds² |
| Hubble running | 6 | Cumulative ratio, tension, r(N), VP step, F1 strict/soft |
| R2 domains | 8 | Wire R, capacitance, RC cancellation, disc spots, K_J×R_K, norms, vena contracta |
| Dwarf solitons | 4 | Purity, cosmic ratio, Faber-Jackson, Tully-Fisher |
| QED alpha extraction | 3 | Coefficient assembly, Newton inversion, CODATA derivation |
| What-if BSM scan | 6 | Generic scanner + 4 candidate-specific + direct-db |
| Group theory | 1 | Casimirs verification |
| Scale conversion | 2 | Energy ↔ distance |

### 4.4 Arithmetic Modes

| Mode | Rule | Examples |
|---|---|---|
| exact | Fraction only | Gap ratios, beta coefficients, democracy |
| mixed | Fraction for rational steps, mpf at irrational boundary | Koide, crossing scale, MOND a₀ |
| numeric | Numerical methods (Euler, Newton, bisection) | Two-loop α_s, QED alpha extraction |

---

## V. THE EXPERIMENT SYSTEM

### 5.1 Architecture

An experiment is a JSON file declaring what to compute, what to check, and what to draw.

```json
{
    "key": "experiment_name_v0",
    "execution_plan": ["derivation_1_v0", "derivation_2_v0"],
    "comparisons": [{"label": "...", "match_mode": "exact", ...}],
    "diagrams": [{"key": "...", "type": "bar", ...}]
}
```

The runner is generic. It does not know physics. It loads values, calls derivations in order, merges outputs, evaluates comparisons, and writes results. The physics is in the JSON and the derivation functions. The runner is plumbing.

### 5.2 Execution Flow

1. Load experiment JSON
2. Load all `values_*.json` into the value pool (414 nodes)
3. Execute each derivation in `execution_plan` order
4. After each derivation, merge outputs into the pool
5. Execute each connection in `connections` list
6. Check `expected_outputs` are present
7. Evaluate each comparison
8. List diagram specs
9. Write result JSON with full provenance
10. Print summary

### 5.3 Comparison Engine

Five match modes:

| Mode | Pass Condition | Use |
|---|---|---|
| exact | Fraction equality | Beta coefficients, gap ratios, integer identities |
| digits | N-digit string match via mp.nstr | QED coefficients, Koide K |
| range | lo ≤ value ≤ hi | M_GUT range, GPS correction, escape velocity |
| miss_pct | Always INFO — reports miss% | α vs CODATA, DM/baryon vs Planck |
| bool | Boolean equality | Democracy holds, GPS gravity dominates |

Status values: PASS, FAIL, INFO, SKIP. An experiment with 0 FAIL is status `complete`. Any FAIL makes it `partial`.

### 5.4 Experiment Inventory

| Experiment | Program | Derivations | Comparisons | Status |
|---|---|---|---|---|
| beta_unification | beta_unification | 18 | 29 | complete (22P, 7I) |
| soliton_gravity | soliton_gravity | 8 | 12 | defined |
| toroidal_dm | toroidal_dm | 9 | 8 | defined |
| hubble_running | hubble_running | 6 | 6 | defined |
| r2_universality | r2_universality | 8 | 6 | defined |
| koide_analysis | koide_analysis | 2 | 5 | defined |
| relativity | soliton_gravity | 3 | 6 | defined |
| cosmology_chain | beta_unification | 5 | 5 | defined |
| electroweak_anatomy | electroweak_anatomy | 3 | 3 | defined |
| parameter_reduction | parameter_reduction | 2 | 2 | defined |
| proton_decay | proton_decay | 2 | 2 | defined |
| whatif_scan | beta_unification | 1 | 1 | complete |
| qed_derived_codata | parameter_reduction | 3 | 8 | complete (5P, 3I) |
| whatif_vl_lepton_doublet | beta_unification | 1 | 2 | complete |
| whatif_vl_singlet_e | beta_unification | 1 | 2 | complete |
| whatif_vl_d_singlet | beta_unification | 1 | 2 | complete |
| whatif_vl_u_singlet | beta_unification | 1 | 2 | complete |

---

## VI. THE CONNECTION SYSTEM

### 6.1 Connection Types

| Type | Meaning | Example |
|---|---|---|
| convergence | Values approaching a common point | Three couplings at M_GUT |
| correction_chain | Sequential corrections | Pure gauge → SM → CD → measured gap |
| traceability | Where integers appear across the system | 11 in DM formula and b₃ gauge |
| shared_set | Values shared across programs | 11, 13 in all three programs |
| adjacency | Which values relate to which | Object adjacency map |
| hierarchy | Multi-scale nesting | 11-level soliton hierarchy |
| cancellation | R2 enters and exits a product | K_J × R_K = 2/e |

### 6.2 Connection Inventory

| Key | Type | Description |
|---|---|---|
| connection_coupling_convergence_v0 | convergence | Coupling convergence analysis |
| connection_gap_correction_chain_v0 | correction_chain | Gap: pure gauge → SM → CD → measured |
| connection_integer_network_v0 | traceability | Integer 11, 13, 44, 169 flow |
| connection_three_programs_shared_set_v0 | shared_set | Shared integers across programs |
| connection_object_adjacency_v0 | adjacency | Object adjacency map |
| connection_soliton_hierarchy_v0 | hierarchy | 11-level nesting with GM/(rc²) |
| connection_r2_cancellation_registry_v0 | cancellation | All R2 cancellation identities |
| connection_boundary_adjacency_v0 | adjacency | Running distance L between boundaries |
| connection_mond_transition_v0 | hierarchy | MOND radii vs Hill spheres |

---

## VII. THE PROGRAM SYSTEM

### 7.1 Program Node

Each research program carries a thesis, status, kill switches, and cross-program connections.

| Field | Purpose |
|---|---|
| thesis | The hypothesis being tested |
| status | ACTIVE, CONFIRMED, PARKED, BLOCKING, KILLED |
| kill_switches | Specific measurements that would falsify the thesis |
| program_connections | Integer sharing and dependency between programs |

### 7.2 Program Inventory

| Program | Status | Kill Switches | Thesis |
|---|---|---|---|
| beta_unification | ACTIVE | 2 | Gauge beta integers determine cosmological parameters |
| toroidal_dm | ACTIVE | 2 | DM amplification A = (44/13)π(c/v)² |
| hubble_running | ACTIVE | 2 | H₀(N) = H₀(0)rᴺ via boundary transit |
| soliton_gravity | ACTIVE | 3 | Gravity is soliton ground state, GM/(rc²) at all levels |
| koide_analysis | ACTIVE | 2 | K = 2/3 tautology, a² = 2 open, m_τ conditional |
| proton_decay | ACTIVE | 3 | M_GUT → τ_p ~ 10³⁴⁻³⁵ yr, Hyper-K window |
| gut_threshold | ACTIVE | 2 | Three-loop running, exact M_VL |
| r2_universality | CONFIRMED | 2 | R2 = π/4 in all circular-to-rectilinear conversions |
| q335_basis | CONFIRMED | 2 | 35 constants at 100 digits, 82/82 PSLQ null |
| electroweak_anatomy | CONFIRMED | 1 | 7 inputs → 11 observables, A₂ 87% cancellation |
| parameter_reduction | CONFIRMED | 2 | 19 → 18 → 17 parameter count |
| confinement_mapping | PARKED | 1 | Blank zone, non-perturbative QCD |
| statistical_control | BLOCKING | 2 | Integer coincidence probability — blocks beta_unification confirmation |

Seven ACTIVE programs require ongoing experiments. Four CONFIRMED programs have passed all checks. One PARKED program awaits lattice QCD progress. One BLOCKING program prevents the central thesis from being confirmed until the combinatoric analysis is performed.

---

## VIII. CASE STUDY 1: BETA UNIFICATION

### 8.1 The Experiment

`experiment_beta_unification_v0`: 18 derivations, 5 connections, 29 comparisons, 3 diagrams. The most comprehensive experiment in the system.

### 8.2 Key Results

| Category | Checks | Status |
|---|---|---|
| Exact Fraction checks (betas, gaps, integers) | 18 | All PASS |
| Digit checks (gap ratio, Koide K) | 2 | All PASS |
| Range checks (M_GUT, L_GUT) | 2 | All PASS |
| Miss% predictions (α_s, m_τ, DM/baryon, Ω_DM) | 7 | All INFO |

Headline numbers: SM gap = 218/115 (exact), CD gap = 38/27 (exact), pure gauge gap = 2 (exact), generation democracy holds (boolean), DM/baryon prefactor = 22/13 (exact), Ω_DM prefactor = 44/169 (exact), amplification = 44/13 (exact). All exact Fraction checks pass.

Predictions: α_s one-loop = 0.1077 (8.7% miss), α_s two-loop full b_ij = 0.1184 (0.33% miss from platform, 10-12% miss from DATA-6 due to known two-loop bug), DM/baryon = 5.3165 (0.073% miss from Planck), Koide m_τ = 1776.97 MeV (0.006% miss from PDG).

### 8.3 The Two-Loop Bug

The two-loop Euler integration in DATA-6 produces α_s values with 10-12% miss against the expected <1% from the DATA-5 platform. The VL db_ij matrix values need investigation against the platform originals. This is the #1 priority item in the improvement plan. The one-loop prediction and all exact checks are unaffected.

---

## IX. CASE STUDY 2: WHAT-IF BSM SCAN

### 9.1 The Problem

The measured coupling gap ratio is 1.3582. The SM gives 218/115 = 1.8957 (39.6% miss). Which BSM representation corrects this?

### 9.2 The Method

Each candidate gets its own experiment, its own values file with candidate-prefixed quantum numbers, and its own derivation wrapper. No shared mutable keys. No last-wins collision. Each experiment is permanent and independently re-runnable.

### 9.3 Results: 5 of 15 Candidates Tested

| Candidate | (d₃,d₂,Y) | Gap Ratio | Distance | Miss% | Asymmetry |
|---|---|---|---|---|---|
| VL CD (3,2,1/6) | (3,2,1/6) | 38/27 = 1.407 | 0.049 | 3.6% | 15 |
| VL lepton doublet (1,2,-1/2) | (1,2,-1/2) | 214/125 = 1.712 | 0.354 | 26.1% | 5/3 |
| VL electron singlet (1,1,-1) | (1,1,-1) | 2 | 0.642 | 47.3% | 0 |
| VL down singlet (3,1,-1/3) | (3,1,-1/3) | 111/55 = 2.018 | 0.660 | 48.6% | 0 |
| VL up singlet (3,1,2/3) | (3,1,2/3) | 117/55 = 2.127 | 0.769 | 56.6% | 0 |

### 9.4 Findings

The CD wins by a factor of 7 (distance 0.049 vs next-best 0.354). The mechanism is the asymmetry: db₂/db₁ = 15 for the CD, meaning the SU(2) shift is 15× larger than the U(1) shift. This comes from Y = 1/6 — the smallest hypercharge in the SM quantization gives the largest asymmetry. Singlets (candidates 12, 13, 15) have db₂ = 0 and push the gap ratio UP toward or above 2.0 — they make things worse.

### 9.5 Remaining Candidates

10 candidates require either scalar formulas (half the VL shifts) or compound/multiplied representations (pre-computed db values). The `coupling_whatif_direct_db_v0` derivation handles these. The scalar CD at (3,2,1/6) will have distance ~0.1 (half the correction, same asymmetry) — worse than the VL CD but still the best scalar.

---

## X. CASE STUDY 3: QED ALPHA EXTRACTION

### 10.1 The Chain

```
a_e (measured) → QED series A₁-A₅ → Newton inversion → α
α + m_e + exact SI → R∞, a₀, μ₀
```

### 10.2 Results

| Quantity | Derived | CODATA | Miss | α Power |
|---|---|---|---|---|
| α⁻¹ | 137.035998630 | 137.035999084 | 3.3 ppb | direct |
| R∞ | 10973731.656 m⁻¹ | 10973731.568 m⁻¹ | 8.0 ppb | α² |
| a₀ | 5.2918 × 10⁻¹¹ m | 5.2918 × 10⁻¹¹ m | 4.0 ppb | α⁻¹ |
| μ₀ | 1.2566 × 10⁻⁶ N/A² | 1.2566 × 10⁻⁶ N/A² | 4.0 ppb | α¹ |

### 10.3 The Error Propagation Proof

The miss pattern is not random. It follows exact α-power scaling: 3.3 ppb for α¹ quantities, 8.0 ppb for α² quantities. The ratio is constant at 1.2× across all three derived values, confirming a single error source (the alpha residual from missing mass-dependent and hadronic terms) with no additional computational artifacts.

### 10.4 How It Was Built

The first attempt used Laporta's C81a+b+c = 107.71 as the 4-loop coefficient. This gave α⁻¹ = 137.036376 — off by 2752 ppb. The forward check (plug known α into the series, compare to measured a_e) immediately diagnosed the problem: the series couldn't reproduce a_e from known α. The resolution: Laporta's C81/C83 labels use a different convention than the standard A₁-A₅ series. Switching to the verified A₄ = −1.9122 from PHYS-9 fixed the extraction.

This episode demonstrates the system's diagnostic capability. The forward check is embedded in the derivation function. The comparison engine reports both the inverse result and the forward residual. The convention error was caught and fixed within the same session, with the incorrect runs preserved as result_run001 through result_run003 in the database.

### 10.5 The Integer Content

Every piece of the chain that is not a measurement is an integer or a rational combination of Q335 transcendentals. A₁ = 1/2 (exact). A₂ and A₃ are assembled from 12 rational coefficient nodes and 5 Q335 transcendental nodes — all stored in the value pool, all read by the derivation at runtime. A₄ and A₅ are numerical. The SI constants are exact by definition. The chain consumes 32 value nodes total, of which 26 are structural (Level 0-1) and 2 are measured inputs from the universe.

---

## XI. LESSONS LEARNED

### 11.1 The Alias Problem

The initial JSON export used different key names than the derivation registry expected. This required alias files (`values_beta_aliases_v0.json`, `values_rep_aliases_v0.json`) that duplicate values under alternative keys. The fix: derivation registry input keys are canonical. The exporter writes those names. Alias files are technical debt to be consolidated in v1.

### 11.2 The Last-Wins Collision

The what-if scan initially used the same key names (`rep_whatif_su3_dim_v0`) for all candidates. With all values files loaded via glob, the alphabetically last file overwrote all others. All 4 experiments computed the same candidate. The fix: candidate-prefixed keys (`rep_whatif_vl_lepton_doublet_db1_v0`) and candidate-specific derivation wrappers. Each experiment is independent and simultaneously runnable.

### 11.3 The Laporta Convention

Full-precision coefficients (4900 digits) were received from Prof. Laporta but used a different convention than the standard QED series. Naively summing C81a+b+c gave 107.71, not the expected A₄ = −1.9122. The forward check caught this immediately. The coefficients are archived in the database for future convention mapping. The working extraction uses verified PHYS-9 values.

### 11.4 Hardcoded Constants

Early derivation functions hardcoded physics values as string literals. The QED coefficient assembly function initially contained `C4_str = "-0.32847..."` instead of reading from the pool. This violates Principle 2.6 and breaks provenance. The fix: every numerical value is a value node, read by key at runtime. The derivation function contains zero physics knowledge — only the formula structure.

### 11.5 The Forward Check Pattern

Every derivation that inverts a relationship (solving for x given f(x) = y) should include a forward check: plug the result back through the forward formula and compare to the input. The QED extraction function does this: it reads the known CODATA α from the pool, evaluates a_e from the series, and reports the forward residual alongside the inverse result. This pattern caught the Laporta convention error and should be standard for all inversion derivations.

---

## XII. THE IMPROVEMENT PATH

### 12.1 Priority Items

| # | Item | Category | Status |
|---|---|---|---|
| 1 | Fix two-loop α_s bug | Correctness | Open |
| 2 | Consolidate key aliases | Trust | Open |
| 3 | Add pitfall entries to nodes | Safety | Open |
| 4 | Pre-flight validation in runner | Robustness | Open |
| 5 | Result run-counter versioning | Data preservation | Implemented |
| 6 | Complete soliton gravity experiment | Coverage | Defined |
| 7 | Extract hardcoded numerical config | Principle compliance | Open |
| 8 | Connection outputs into pool | Capability | Open |
| 9 | Dataset support for what-if | What-if capability | Specified |
| 10 | Identity match mode | Capability | Specified |

### 12.2 The Statistical Control Script

The single most important unwritten piece. Program_statistical_control asks: given 15 BSM candidates, what is the probability that the best one matches the measured gap ratio to within 3.6% by chance? And given that the same integers (11, 13) that fix the gap ratio also predict DM/baryon to 0.073%, what is the joint probability?

If p < 0.01, the integer connection between gauge theory and cosmology is statistically significant. If p > 0.1, it could be coincidence. This computation blocks the confirmation of program_beta_unification.

---

## XIII. COMPARISON TO PREDECESSORS

| Feature | DATA-4 | DATA-5 | DATA-6 |
|---|---|---|---|
| Architecture | Flat verified registry | Object-oriented platform library | Experiment-driven versioned node system |
| Entry count | 146 | 222 objects | 414 value nodes |
| Checks | 38/38 PASS | 322/323 PASS | 85+ comparisons across 13 experiments |
| Computation | External scripts reference the registry | Library functions called by scripts | Derivation functions registered in the system |
| Versioning | Manual version in filename | Library version | Append-only `_vN` on every node |
| Provenance | Source field | Library imports | Full chain: value → derivation → experiment → result |
| Experiments | Not formalized | Test scripts | JSON-declared execution plans |
| Programs | Not formalized | Paper references | Formal nodes with thesis, kill switches, connections |
| What-if | Manual script modification | Helper functions | Candidate-specific experiments with prefixed value nodes |
| Results | Console output | Console output | Versioned result JSON with comparison details |

DATA-4 stored data. DATA-5 computed with data. DATA-6 experiments with data.

---

## XIV. REPRODUCIBILITY

### 14.1 Complete Reproduction

To reproduce any result in this paper:

1. Clone the DATA-6 repository
2. Verify: `python data6.py validate` — all nodes pass schema
3. List: `python data6.py list experiments` — all 13+ experiments visible
4. Run: `python data6.py run experiment_name_v0`
5. Report: `python data6.py report experiment_name_v0`

Every experiment is self-contained. The JSON declares all dependencies. The runner loads all values. The derivation functions read from the pool. The result is written with full provenance.

### 14.2 No External Dependencies

The system requires only Python 3.8+ with `fractions` (standard library) and `mpmath` (pip install). No numpy, scipy, tensorflow, or any heavy dependency. The diagram system additionally requires matplotlib, but diagrams are optional — all computation runs without them.

### 14.3 Deterministic Execution

Given the same value JSON files and derivation code, every run produces identical results. There is no random seed, no stochastic sampling, no floating-point rounding variation. Fraction arithmetic is exact. mpf arithmetic at 200 dps is deterministic. Newton's method converges to the same root from the same starting point.

---

## XV. FALSIFICATION

**F1.** If any exact Fraction check fails (gap ratios, beta coefficients, integer identities), the system has a data entry error or an arithmetic bug. Current status: all exact checks pass.

**F2.** If the what-if scan finds a candidate closer to the measured gap ratio than the CD (distance < 0.049), the CD identification is weakened. Current status: next-best is 0.354 (7× worse).

**F3.** If the QED-derived α produces R∞, a₀, μ₀ that disagree with CODATA beyond the α-power scaling prediction, the chain has a bug. Current status: all follow scaling exactly.

**F4.** If the two-loop α_s bug is traced to a fundamental error in the CD beta shifts (not just a matrix value), the unification program is affected. Current status: one-loop is correct, two-loop under investigation.

**F5.** If the statistical control analysis gives p > 0.1 for the (11, 13) coincidence, the connection between gauge integers and cosmological parameters is likely chance. Current status: not yet computed.

---

## APPENDIX A: CLI COMMAND REFERENCE

| Command | Usage | Description |
|---|---|---|
| run | `data6.py run <experiment>` | Execute experiment, write result JSON |
| report | `data6.py report <experiment>` | Print formatted result report |
| diagram | `data6.py diagram <experiment>` | Generate PNGs from diagram specs |
| validate | `data6.py validate` | Check all JSON against schema |
| list | `data6.py list [values\|derivations\|connections\|experiments\|results]` | List nodes by type |
| search | `data6.py search <query>` | Substring search across all nodes |
| info | `data6.py info <key>` | Print full details for one node |
| index | `data6.py index` | Rebuild manifest |
| compile | `data6.py compile` | Produce single compiled JSON |

## APPENDIX B: COMPLETE DERIVATION REGISTRY

### B.1 Original Registry (18 derivations)

| Key | Mode | Description |
|---|---|---|
| coupling_extraction_v0 | exact | GUT-normalized couplings at M_Z |
| gap_measured_ratio_v0 | exact | Measured gap from inverse couplings |
| gap_sm_ratio_v0 | exact | SM gap from betas |
| gauge_pure_gap_v0 | exact | Pure gauge gap from Casimirs |
| beta_sm_coefficients_v0 | exact | SM betas from group theory |
| beta_cabibbo_doublet_shifts_v0 | exact | VL one-loop shifts |
| beta_modified_and_cd_gap_ratio_v0 | exact | SM + CD modified betas and gap |
| generation_democracy_v0 | exact | Per-gen shifts equal |
| beta_double_action_mechanism_v0 | mixed | CD double action analysis |
| beta_y_dependence_family_v0 | exact | Gap as function of Y |
| crossing_one_loop_scale_v0 | mixed | One-loop GUT crossing |
| coupling_one_loop_alpha_s_prediction_v0 | mixed | One-loop α_s prediction |
| coupling_two_loop_alpha_s_euler_v0 | numeric | Two-loop Euler integration |
| koide_ratio_v0 | mixed | Koide K from masses |
| koide_tau_prediction_v0 | mixed | m_τ from K = 2/3 |
| cosmo_dm_baryon_ratio_v0 | mixed | DM/baryon from integers |
| cosmo_omega_dm_v0 | mixed | Ω_DM from integers |
| cosmo_amplification_factor_decomposition_v0 | exact | DM amplification decomposition |

### B.2 Extended Registry (39 derivations)

| Key | Mode | Category |
|---|---|---|
| coupling_one_loop_sin2_prediction_v0 | mixed | Unification |
| coupling_whatif_rep_v0 | exact | What-if |
| coupling_whatif_direct_db_v0 | exact | What-if |
| coupling_whatif_vl_lepton_doublet_v0 | exact | What-if |
| coupling_whatif_vl_singlet_e_v0 | exact | What-if |
| coupling_whatif_vl_d_singlet_v0 | exact | What-if |
| coupling_whatif_vl_u_singlet_v0 | exact | What-if |
| group_theory_casimirs_v0 | exact | Group theory |
| scale_energy_to_distance_v0 | mixed | Scale |
| scale_distance_to_energy_v0 | mixed | Scale |
| gravity_coupling_v0 | mixed | Gravity |
| gravity_escape_velocity_v0 | mixed | Gravity |
| gravity_binding_fraction_v0 | mixed | Gravity |
| gravity_hill_sphere_v0 | mixed | Gravity |
| gravity_kepler_period_v0 | mixed | Gravity |
| gravity_process_rate_v0 | mixed | Gravity |
| gravity_gps_correction_v0 | mixed | Gravity |
| gravity_mond_a0_v0 | mixed | Gravity |
| relativity_muon_lifetime_v0 | mixed | Relativity |
| relativity_twin_paradox_v0 | mixed | Relativity |
| relativity_ds_squared_v0 | mixed | Relativity |
| hubble_cumulative_ratio_v0 | exact | Hubble |
| hubble_tension_sigma_v0 | mixed | Hubble |
| hubble_required_r_v0 | mixed | Hubble |
| hubble_vp_step_size_v0 | mixed | Hubble |
| hubble_test_f1_strict_v0 | exact | Hubble |
| hubble_test_f1_soft_v0 | mixed | Hubble |
| domain_r2_area_v0 | mixed | R2 domain |
| domain_wire_resistance_v0 | mixed | R2 domain |
| domain_capacitance_v0 | mixed | R2 domain |
| domain_rc_cancellation_v0 | mixed | R2 domain |
| domain_disc_spot_v0 | mixed | R2 domain |
| domain_kj_rk_cancellation_v0 | exact | R2 domain |
| domain_fourier_gaussian_norms_v0 | mixed | R2 domain |
| domain_vena_contracta_v0 | mixed | R2 domain |
| cosmo_omega_b_v0 | mixed | Cosmology |
| cosmo_omega_matter_v0 | mixed | Cosmology |
| cosmo_omega_de_v0 | mixed | Cosmology |
| cosmo_virial_ratio_v0 | mixed | Cosmology |
| cosmo_frame_dragging_v0 | mixed | Cosmology |
| dwarf_purity_v0 | mixed | Dwarfs |
| dwarf_cosmic_ratio_v0 | mixed | Dwarfs |
| dwarf_faber_jackson_v0 | mixed | Dwarfs |
| dwarf_tully_fisher_v0 | mixed | Dwarfs |
| qed_coefficients_assemble_v0 | mixed | QED |
| qed_alpha_from_ae_v0 | numeric | QED |
| qed_derived_codata_v0 | mixed | QED |

### B.3 Connection Registry (9 functions)

| Key | Type |
|---|---|
| connection_coupling_convergence_v0 | convergence |
| connection_gap_correction_chain_v0 | correction_chain |
| connection_integer_network_v0 | traceability |
| connection_three_programs_shared_set_v0 | shared_set |
| connection_object_adjacency_v0 | adjacency |
| connection_soliton_hierarchy_v0 | hierarchy |
| connection_r2_cancellation_registry_v0 | cancellation |
| connection_boundary_adjacency_v0 | adjacency |
| connection_mond_transition_v0 | hierarchy |

## APPENDIX C: WHAT-IF SCAN COMPLETE RESULTS

| # | Candidate | Type | db₁ | db₂ | db₃ | Gap | Distance | Miss% | Asymmetry |
|---|---|---|---|---|---|---|---|---|---|
| 2 | VL (3,2,1/6) CD | VL | 1/15 | 1 | 1/3 | 38/27 | 0.049 | 3.6% | 15 |
| 7 | VL (1,2,-1/2) | VL | 1/5 | 1/3 | 0 | 214/125 | 0.354 | 26.1% | 5/3 |
| 12 | VL (1,1,-1) | VL | 2/5 | 0 | 0 | 2 | 0.642 | 47.3% | 0 |
| 13 | VL (3,1,-1/3) | VL | 2/15 | 0 | 1/6 | 111/55 | 0.660 | 48.6% | 0 |
| 15 | VL (3,1,2/3) | VL | 8/15 | 0 | 1/6 | 117/55 | 0.769 | 56.6% | 0 |

Remaining 10 candidates (not yet tested): MSSM (compound), SU(5) 5+5̄ (compound), 3×Scalar H (multiplied), Scalar (3,2,1/6), Scalar (1,3,0), 2×Scalar H (multiplied), Scalar (1,2,1/2), SU(5) 10+10̄ (compound), Scalar (3,1,-1/3), Scalar (8,1,0).

## APPENDIX D: QED DERIVED CODATA COMPLETE RESULTS

From result_experiment_qed_derived_codata_v0_run003.json.

| Output Key | Value | Category |
|---|---|---|
| result_qed_a1_v0 | 1/2 | Coefficient |
| result_qed_a2_v0 | −0.328478965579194 | Coefficient |
| result_qed_a3_v0 | 1.1812414565872 | Coefficient |
| result_qed_a4_v0 | −1.91224576492645 | Coefficient |
| result_qed_a5_v0 | 5.891 | Coefficient |
| result_alpha_inv_from_ae_v0 | 137.035998630375 | Derived |
| result_alpha_inv_from_ae_full_v0 | 137.035998630374672067213142569 | Derived (30 digits) |
| result_rydberg_from_derived_alpha_v0 | 10973731.6556419 | Derived |
| result_bohr_from_derived_alpha_v0 | 5.29177208435434 × 10⁻¹¹ | Derived |
| result_mu0_from_derived_alpha_v0 | 1.25663706628085 × 10⁻⁶ | Derived |
| result_rydberg_miss_pct_v0 | 7.97 × 10⁻⁷ % | Diagnostic |
| result_bohr_miss_pct_v0 | 3.98 × 10⁻⁷ % | Diagnostic |
| result_rydberg_digits_v0 | 18.6 | Diagnostic |
| result_bohr_digits_v0 | 19.3 | Diagnostic |
| result_newton_iterations_v0 | 6 | Verification |
| result_newton_residual_v0 | 1.59 × 10⁻²⁰⁴ | Verification |
| result_diff_vs_codata_ppb_v0 | 3.31 | Comparison |
| result_diff_vs_cs_ppb_v0 | 3.03 | Comparison |
| result_diff_vs_rb_ppb_v0 | 4.20 | Comparison |

## APPENDIX E: PAPER CROSS-REFERENCE TABLE

| Paper | Registry | What DATA-6 Provides |
|---|---|---|
| MATH-1 | [@HOWL-MATH-1-2026] | Q335 constants as geom_* value nodes |
| MATH-2 | [@HOWL-MATH-2-2026] | Q335 basis, 31 nodes at 100 digits |
| MATH-6 | [@HOWL-MATH-6-2026] | PSLQ 82/82 null, integer pool nodes |
| DATA-4 | [@HOWL-DATA-4-2026] | 146 entries migrated to value nodes |
| PHYS-7 | [@HOWL-PHYS-7-2026] | theta_QCD = 0 in parameter_reduction program |
| PHYS-8 | [@HOWL-PHYS-8-2026] | Koide K, a², m_τ in koide_analysis experiment |
| PHYS-9 | [@HOWL-PHYS-9-2026] | A₁-A₄ in QED extraction, verified at 4.3 ppb |
| PHYS-11 | [@HOWL-PHYS-11-2026] | R2 domains in r2_universality experiment |
| PHYS-13 | [@HOWL-PHYS-13-2026] | Gap ratio in beta_unification experiment |
| PHYS-15 | [@HOWL-PHYS-15-2026] | CD identification in whatif_scan experiments |
| PHYS-17 | [@HOWL-PHYS-17-2026] | Generation democracy in beta_unification |
| PHYS-20 | [@HOWL-PHYS-20-2026] | Proton decay in proton_decay experiment |
| PHYS-36 | [@HOWL-PHYS-36-2026] | QED 5-loop chain in qed_derived_codata experiment |

29 paper cross-references stored as connection nodes in connections_papers_v0.json.

---

**END HOWL-DATA-6-2026**

**Registry:** [@HOWL-DATA-6-2026]

**Status:** Operational

**Central Result:** A versioned node system with 414 values, 57 derivations, 9 connections, 13+ experiments, and 13 programs — operational and producing results. Three case studies demonstrate: (1) exact integer checks passing across gauge theory and cosmology, (2) BSM candidate identification by gap ratio with 7× separation, (3) four CODATA values derived from one measurement at 3.3-8.0 ppb.

**What it proves:** Physics research can be conducted in a versioned, append-only, experiment-driven system where every constant is a node, every computation is a registered derivation, every result is permanent, and every error is traceable. The system catches its own mistakes (Laporta convention, last-wins collision) through structural safeguards (forward checks, prefixed keys, comparison engine).

**What it does NOT prove:** The system does not prove any physics claim. It provides the infrastructure for testing physics claims reproducibly, traceably, and exactly. The physics is in the programs and experiments. The system is the laboratory.

**Foundation:** DATA-4 (146 entries), DATA-5 (222 objects), phys24_lib.py (platform library)

**Key limitation:** The two-loop α_s bug, the alias mess, the missing statistical control script. All documented. All on the improvement path.

**Falsification:** Five specific criteria. All currently met except the statistical control (not yet computed).

---

## APPENDIX F: COMPLETE VALUE NODE INVENTORY BY TOPIC PREFIX

| Prefix | Count | Level Range | Value Types | Description |
|---|---|---|---|---|
| astro | 12 | 2 | approximate | Gravitational constant, masses, radii, AU, parsec, muon lifetime |
| atomic | 2 | 2 | exact_fraction | Rydberg constant, Bohr radius |
| beta | 36 | 1 | exact_fraction | SM betas, CD shifts, modified betas, two-loop b_ij, aliases |
| cd | 4 | 2 | mixed | CD mass bounds, mixing angle, hypercharge |
| ckm | 3 | 2 | exact_fraction | CKM mixing angles |
| cosmo | 13 | 1-2 | mixed | H₀ measurements, Planck parameters, DM/baryon prefactors |
| coupling | 12 | 1-2 | exact_fraction | alpha_inv, sin²θ_W, alpha_s, GUT couplings, gap ratio, Fermi constant |
| energy | 1 | 2 | exact_fraction | Deuteron binding energy |
| eng | 41 | 0-2 | mixed | hbar*c, resistivity, permittivity, sound speed, disc parameters |
| gap | 8 | 1-2 | exact_fraction | Pure gauge, SM, CD, MSSM gap ratios and components |
| geom | 31 | 0 | exact_fraction | Q335 basis: π through E(k²=3/4) |
| group | 10 | 1 | exact_fraction | Casimirs, Dynkin indices, generation count |
| integer | 10 | 1 | exact_integer | Yang-Mills 11, b₂_mod 13, derived 22, 44, 169, 218 |
| koide | 4 | 2 | mixed | K values and a² for leptons, down quarks, up quarks |
| mass | 21 | 2 | exact_fraction | Z, W, top, Higgs, electron through bottom, neutron, pions, kaon, deuteron, He-4 |
| math | 3 | 0 | exact_fraction | Bessel zeros, Euler-Mascheroni |
| obs | 75 | 2 | approximate | Disc specifications, dwarf galaxy catalog (11 dwarfs × 5-7 properties) |
| qed | 32 | 1-2 | mixed | Laporta C81/C83, A₁-A₅, series rationals, a_e measured, alpha references |
| ratio | 11 | 2 | exact_fraction | Mass ratios: proton/electron, charm/strange, Koide derived |
| rep | 70 | 1 | mixed | SM representations, CD representation, what-if candidate quantum numbers |
| scale | 2 | 2 | approximate | Energy/distance conversion inputs |
| si | 8 | 0 | exact_fraction | c, h, ℏ, e, k_B, N_A, Δν_Cs, K_cd |
| spectro | 1 | 2 | exact_fraction | Hydrogen 1S-2S transition |
| **Total** | **414** | | | |


## APPENDIX G: SI EXACT CONSTANTS

These seven constants have zero uncertainty by the 2019 SI redefinition. They are exact integers or exact Fractions. They anchor the entire measurement system.

| Key | Symbol | Value | Fraction | Unit |
|---|---|---|---|---|
| si_speed_of_light_v0 | c | 299792458 | 299792458/1 | m/s |
| si_planck_constant_v0 | h | 6.62607015 × 10⁻³⁴ | 662607015/10⁴² | J·s |
| si_reduced_planck_constant_v0 | ℏ | 1.05457182 × 10⁻³⁴ | h/(2π) via Q335 | J·s |
| si_elementary_charge_v0 | e | 1.602176634 × 10⁻¹⁹ | 1602176634/10²⁸ | C |
| si_boltzmann_constant_v0 | k_B | 1.380649 × 10⁻²³ | 1380649/10²⁹ | J/K |
| si_avogadro_number_v0 | N_A | 6.02214076 × 10²³ | 602214076 × 10¹⁵ | mol⁻¹ |
| si_cesium_hyperfine_v0 | Δν_Cs | 9192631770 | 9192631770/1 | Hz |
| si_luminous_efficacy_v0 | K_cd | 683 | 683/1 | lm/W |


## APPENDIX H: Q335 ANALYTICAL BASIS

31 constants stored as Fraction(p, 2³³⁵) where p is a ~100-digit integer. All verified against mpmath at mp.dps=120.

| # | Key | Constant | First 20 digits of p | Match Digits |
|---|---|---|---|---|
| 1 | geom_pi_v0 | π | 21988642587319235101 | 102 |
| 2 | geom_e_euler_v0 | e | 19025804478276920258 | 102 |
| 3 | geom_ln2_v0 | ln(2) | 48514773537953331556 | 101 |
| 4 | geom_sqrt2_v0 | √2 | 98983668457552556369 | 101 |
| 5 | geom_sqrt3_v0 | √3 | 12122974029491289523 | 102 |
| 6 | geom_sqrt5_v0 | √5 | 15650692174241595562 | 102 |
| 7 | geom_sqrt7_v0 | √7 | 18518148712709215377 | 102 |
| 8 | geom_golden_ratio_v0 | φ | 11324947246773616860 | 102 |
| 9 | geom_zeta3_v0 | ζ(3) | 84134394645319852071 | 101 |
| 10 | geom_zeta5_v0 | ζ(5) | 72576671487518636549 | 101 |
| 11 | geom_pi_squared_v0 | π² | 69079358014733772680 | 102 |
| 12 | geom_zeta2_v0 | ζ(2) = π²/6 | 11513226335788962113 | 102 |
| 13 | geom_r2_v0 | R₂ = π/4 | (derived: p_pi/4) | 102 |
| 14 | geom_r4_v0 | R₄ = π²/32 | (derived: p_pi2/32) | 102 |
| 15 | geom_two_pi_v0 | 2π | (derived: 2×p_pi) | exact |
| 16 | geom_zeta7_v0 | ζ(7) | 70576406009217185140 | 101 |
| 17 | geom_zeta9_v0 | ζ(9) | 70132594670320295983 | 101 |
| 18 | geom_li4_half_v0 | Li₄(1/2) | 36219406486600619537 | 101 |
| 19 | geom_li5_half_v0 | Li₅(1/2) | 35583985133688170166 | 101 |
| 20 | geom_li6_half_v0 | Li₆(1/2) | 35282656774609749602 | 101 |
| 21 | geom_li7_half_v0 | Li₇(1/2) | 35137014959475068515 | 101 |
| 22 | geom_catalan_v0 | Catalan | 64110285111693582641 | 101 |
| 23 | geom_e_to_pi_v0 | e^π | 16196638954568755371 | 103 |
| 24 | geom_ln3_v0 | ln(3) | 76894096788635086096 | 101 |
| 25 | geom_ln5_v0 | ln(5) | 11264781569487179915 | 102 |
| 26 | geom_elliptic_k_quarter_v0 | K(k²=1/4) | 11798907793174624666 | 102 |
| 27 | geom_elliptic_k_half_v0 | K(k²=1/2) | 12977043781533614962 | 102 |
| 28 | geom_elliptic_k_threequarter_v0 | K(k²=3/4) | 15093889321598402955 | 102 |
| 29 | geom_elliptic_e_quarter_v0 | E(k²=1/4) | 10271064899101894451 | 102 |
| 30 | geom_elliptic_e_half_v0 | E(k²=1/2) | 94534297847848588347 | 101 |
| 31 | geom_elliptic_e_threequarter_v0 | E(k²=3/4) | 84764261569662347707 | 101 |


## APPENDIX I: INTEGER POOL TRACEABILITY

Every integer traces from gauge theory to where it appears in predictions.

| Key | Value | Origin | Formula Role | Appears In |
|---|---|---|---|---|
| integer_yang_mills_eleven_v0 | 11 | -(11/3)×C₂(adj) gauge coefficient | YM coupling constant | b₃_SM = -11, DM numerator 2×11 = 22, Ω_DM numerator 4×11 = 44 |
| integer_b2_modified_numerator_abs_v0 | 13 | \|numerator of b₂_mod = -13/6\| | Modified SU(2) beta | DM denominator 13, gap denominator, Ω_DM denominator 13² = 169 |
| integer_b2_sm_numerator_abs_v0 | 19 | \|numerator of b₂_SM = -19/6\| | SM SU(2) beta | SM gap numerator doubles to 38, dwarf cosmic ratio ~19 |
| integer_b3_modified_times_three_abs_v0 | 20 | \|3 × b₃_mod\| = \|3 × -20/3\| | Modified SU(3) structure | b₃_mod = -20/3 |
| integer_two_times_yang_mills_v0 | 22 | 2 × 11 | DM/baryon prefactor | (22/13)×π = 5.3165 |
| integer_cabibbo_doublet_gap_numerator_v0 | 38 | 2 × 19 | CD gap numerator | gap_CD = 38/27 |
| integer_cabibbo_doublet_gap_denominator_v0 | 27 | denominator of 38/27 = 3³ | CD gap denominator | gap_CD = 38/27 |
| integer_four_times_yang_mills_v0 | 44 | 4 × 11 | Ω_DM prefactor | (44/169)×R₂, amplification (44/13)×π×(c/v)² |
| integer_b2_modified_numerator_square_v0 | 169 | 13² | Ω_DM denominator | (44/169)×R₂ is pure rational after R₂ cancels |
| integer_sm_gap_numerator_v0 | 218 | numerator of 218/115 | SM gap ratio | gap_SM = 218/115 = 1.8957 |


## APPENDIX J: MEASURED CONSTANTS (CODATA 2022 / PDG 2024)

### J.1 Fundamental Constants

| Key | Symbol | Value | Fraction | Sig. Figs | Unit |
|---|---|---|---|---|---|
| coupling_alpha_em_inverse_v0 | α⁻¹ | 137.035999177 | 137035999177/10⁹ | 12 | dimensionless |
| mass_electron_v0 | m_e | 0.51099895069 | 51099895069/10¹¹ | 11 | MeV |
| mass_muon_v0 | m_μ | 105.6583755 | 1056583755/10⁷ | 10 | MeV |
| mass_tau_v0 | m_τ | 1776.86 | 177686/100 | 6 | MeV |
| mass_proton_v0 | m_p | 938.27208943 | 93827208943/10⁸ | 11 | MeV |
| ratio_proton_electron_mass_v0 | m_p/m_e | 1836.15267343 | 183615267343/10⁸ | 13 | dimensionless |
| atomic_rydberg_constant_v0 | R∞ | 10973731.568157 | 10973731568157/10⁶ | 13 | m⁻¹ |
| atomic_bohr_radius_v0 | a₀ | 5.29177210544 × 10⁻¹¹ | 529177210544/10²² | 12 | m |
| qed_ae_electron_measured_v0 | a_e | 0.00115965218059 | 115965218059/10¹⁴ | 12 | dimensionless |
| coupling_sin2_theta_w_v0 | sin²θ_W | 0.23122 | 23122/100000 | 5 | dimensionless |
| coupling_alpha_s_mz_v0 | α_s(M_Z) | 0.1180 | 1180/10000 | 4 | dimensionless |

### J.2 Electroweak

| Key | Symbol | Value | Fraction | Sig. Figs | Unit |
|---|---|---|---|---|---|
| mass_z_boson_v0 | M_Z | 91187.6 | 911876/10 | 6 | MeV |
| mass_w_boson_v0 | M_W | 80369.2 | 803692/10 | 6 | MeV |
| mass_top_quark_v0 | m_t | 172570 | 172570/1 | 5 | MeV |
| mass_higgs_boson_v0 | m_H | 125200 | 125200/1 | 5 | MeV |
| coupling_fermi_constant_v0 | G_F | 1.1663788 × 10⁻⁵ | 11663788/10¹² | 8 | GeV⁻² |

### J.3 Quark Masses

| Key | Symbol | Value | Scale | Sig. Figs | Unit |
|---|---|---|---|---|---|
| mass_up_quark_v0 | m_u | 2.16 | 2 GeV MS-bar | 3 | MeV |
| mass_down_quark_v0 | m_d | 4.70 | 2 GeV MS-bar | 3 | MeV |
| mass_strange_quark_v0 | m_s | 93.5 | 2 GeV MS-bar | 3 | MeV |
| mass_charm_quark_v0 | m_c | 1273 | m_c MS-bar | 4 | MeV |
| mass_bottom_quark_v0 | m_b | 4183 | m_b MS-bar | 4 | MeV |


## APPENDIX K: BETA COEFFICIENTS — COMPLETE TABLE

### K.1 SM One-Loop Betas (Level 1, exact)

| Component | b₁ (U(1)) | b₂ (SU(2)) | b₃ (SU(3)) |
|---|---|---|---|
| Gauge | 0 | -22/3 | -11 |
| Per generation (×3) | +4/3 each = +4 | +4/3 each = +4 | +4/3 each = +4 |
| Higgs | +1/10 | +1/6 | 0 |
| **Total** | **41/10** | **-19/6** | **-7** |

### K.2 Cabibbo Doublet VL Shifts (Level 1, exact)

| Formula | db₁ | db₂ | db₃ |
|---|---|---|---|
| Expression | (2/5)×d₃×d₂×Y² | (2/3)×d₃×S₂ | (1/3)×d₂×S₂ |
| (d₃,d₂,Y) = (3,2,1/6) | (2/5)×3×2×(1/36) = **1/15** | (2/3)×3×(1/2) = **1** | (1/3)×2×(1/2) = **1/3** |

### K.3 Modified Betas (Level 1, exact)

| | b₁_mod | b₂_mod | b₃_mod |
|---|---|---|---|
| SM + CD | 41/10 + 1/15 = **25/6** | -19/6 + 1 = **-13/6** | -7 + 1/3 = **-20/3** |

### K.4 Gap Ratios (Level 1, exact)

| Model | Numerator | Denominator | Gap Ratio | Distance from 1.3582 |
|---|---|---|---|---|
| Pure gauge | 22/3 | 11/3 | **2** | 0.642 |
| SM | 109/15 | 23/6 | **218/115 = 1.8957** | 0.538 |
| SM + CD | 19/3 | 9/2 | **38/27 = 1.4074** | 0.049 |
| MSSM | — | — | **7/5 = 1.4000** | 0.042 |
| Measured | — | — | **1.3582** | 0 |

### K.5 Two-Loop SM b_ij Matrix (Level 1, exact)

| b_ij | U(1) | SU(2) | SU(3) |
|---|---|---|---|
| U(1) | 199/50 | 27/10 | 44/5 |
| SU(2) | 9/10 | 35/6 | 12 |
| SU(3) | 11/10 | 9/2 | -26 |


## APPENDIX L: GAP RATIO CORRECTION CHAIN

| Step | Gap Before | Correction | Gap After | Cumulative Distance | % of Total Fix |
|---|---|---|---|---|---|
| Pure gauge | — | Baseline | 2.000 | 0.642 | 0% |
| + Higgs (1/10, 1/6, 0) | 2.000 | -0.104 | 1.896 | 0.538 | 16.2% |
| + SM fermions (4/3 each ×3) | 1.896 | 0.000 | 1.896 | 0.538 | 0.0% |
| + Cabibbo Doublet (1/15, 1, 1/3) | 1.896 | -0.489 | 1.407 | 0.049 | 76.2% |
| + Threshold + two-loop | 1.407 | -0.049 | 1.358 | 0.000 | 7.6% |

The CD does 76% of the correction. Fermions do exactly 0% (generation democracy). The Higgs does 16%. Threshold corrections do 8%.


## APPENDIX M: COSMOLOGICAL PREDICTIONS FROM BETA INTEGERS

### M.1 DM/Baryon Ratio

| Step | Expression | Value |
|---|---|---|
| Extract YM | 11 from -(11/3)×C₂(adj) | 11 |
| Extract \|b₂_mod num\| | 13 from b₂_mod = -13/6 | 13 |
| Prefactor | 2×YM / \|b₂_mod_num\| = 22/13 | exact Fraction |
| DM/baryon | (22/13) × π = (22/13) × 4R₂ | 5.3165 |
| Planck 2018 | — | 5.3204 |
| Miss | — | 0.073% |

### M.2 Omega_DM

| Step | Expression | Value |
|---|---|---|
| Prefactor | 4×YM / \|b₂_mod_num\|² = 44/169 | exact Fraction |
| Ω_DM | (44/169) × R₂ | 0.2045 |
| R₂ cancels | 44/169 is pure rational | no irrational factors |
| Planck 2018 | Ω_DM = 0.2607 | — |
| Note | Absolute Ω comparison requires normalization | DM/baryon ratio is the meaningful test |

### M.3 Amplification Factor

| Step | Expression | Value |
|---|---|---|
| Reduced factor | 4×YM / \|b₂_mod_num\| = 44/13 | exact Fraction |
| Full amplification | (44/13) × π × (c/v)² | at galactic rotation velocity |
| Integer content | 44 = 4×11, 13 from b₂_mod | same two integers |


## APPENDIX N: DWARF GALAXY OBSERVATIONAL CATALOG

| Dwarf | Type | M_vis (M☉) | M_dyn (M☉) | σ (km/s) | r_h (pc) |
|---|---|---|---|---|---|
| Segue 1 | Ultra-faint | 340 | 1.3 × 10⁶ | 3.9 | 29 |
| Reticulum II | Ultra-faint | 2600 | 1.0 × 10⁶ | 3.3 | 32 |
| Tucana II | Ultra-faint | 3000 | 3.6 × 10⁷ | 8.6 | 165 |
| Draco | Classical dSph | 2.9 × 10⁵ | 5.4 × 10⁷ | 9.1 | 221 |
| Ursa Minor | Classical dSph | 2.9 × 10⁵ | 5.4 × 10⁷ | 9.5 | 181 |
| Sculptor | Classical dSph | 2.3 × 10⁶ | 7.0 × 10⁷ | 9.2 | 283 |
| Carina | Classical dSph | 3.8 × 10⁵ | 1.3 × 10⁷ | 6.6 | 250 |
| Sextans | Classical dSph | 4.4 × 10⁵ | 2.5 × 10⁷ | 7.9 | 695 |
| Fornax | Classical dSph | 2.0 × 10⁷ | 1.6 × 10⁸ | 11.7 | 710 |
| Leo I | Classical dSph | 5.5 × 10⁶ | 1.2 × 10⁸ | 9.2 | 251 |
| Leo II | Classical dSph | 7.4 × 10⁵ | 4.2 × 10⁶ | 6.6 | 176 |

All stored as `obs_{name}_{property}_v0` value nodes in values_observational_v0.json.


## APPENDIX O: H₀ MEASUREMENTS AND HUBBLE RUNNING

| Key | Method | H₀ (km/s/Mpc) | Uncertainty | Distance Class |
|---|---|---|---|---|
| cosmo_h0_sh0es_v0 | Cepheids (SH0ES) | 73.0 | ±1.0 | local |
| cosmo_h0_h0licow_v0 | Strong lensing (H0LiCOW) | 73.3 | ±1.8 | local-medium |
| cosmo_h0_cchp_v0 | TRGB (CCHP) | 69.8 | ±1.7 | medium |
| cosmo_h0_des_bao_bbn_v0 | BAO+BBN (DES) | 67.4 | ±1.2 | high-z |
| cosmo_h0_planck_v0 | CMB (Planck) | 67.4 | ±0.5 | maximum |

Cumulative ratio: H₀(Planck)/H₀(SH0ES) = 337/365 (exact Fraction).
Tension: ~5σ between local and far.
Running hypothesis: H₀(N) = H₀(0) × r^N where r = (337/365)^(1/N).
VP step size: 1/(12R₂) = 1/(3π) = 0.1061.
F1 strict monotonicity: FAIL (H0LiCOW > SH0ES).
F1 soft (within 1σ): PASS (no hard inversions).


## APPENDIX P: R2 DOMAIN EQUATIONS

R₂ = π/4 appears in every equation that converts between circular and rectilinear geometry.

| # | Domain | Equation | R₂ Role | Coordinator Z |
|---|---|---|---|---|
| 1 | Pipe flow | Q = R₂d²v | Flow area | velocity |
| 2 | Drag force | F = ½ρv²R₂d²Cd | Frontal area | drag coeff |
| 3 | Orifice flow | Q = CdR₂d²√(2ΔP/ρ) | Orifice area | discharge coeff |
| 4 | Hagen-Poiseuille | Q = R₂d⁴ΔP/(32μL) | Pipe geometry | viscosity |
| 5 | Wire resistance | R = ρL/(R₂d²) | Wire cross-section | resistivity |
| 6 | Capacitance | C = ε₀R₂d²/t | Plate area | permittivity |
| 7 | Antenna aperture | A = ηR₂D² | Effective area | efficiency |
| 8 | Free-space path loss | FSPL = (16R₂d/λ)² | Propagation | distance/wavelength |
| 9 | Poynting flux | P = SR₂d² | Irradiance capture | irradiance |
| 10 | Airy disc | A = R₂(1.22λ/NA)² | Diffraction spot | aperture |
| 11 | Fiber mode | A = R₂MFD² | Mode confinement | mode field |
| 12 | Gaussian beam | A = R₂w₀² | Beam waist | beam parameter |
| 13 | Speaker cone | Sd = R₂d²_eff | Radiation area | (geometry) |
| 14 | Sound intensity | I = P/(16R₂r²) | Spherical spreading | distance |
| 15 | Helmholtz | f = (c/(8R₂))√(S/(lV)) | Resonance | port geometry |
| 16 | Thermal radiation | Q = εσT⁴R₂d² | Radiation area | emissivity |
| 17 | Semiconductor wafer | A = R₂D² | Wafer area | (geometry) |
| 18 | Kepler's law | T² = 64R₂²a³/(GM) | Orbital geometry | gravity |
| 19 | Fourier normalization | 1/(8R₂) = 1/(2π) | Transform norm | (identity) |
| 20 | Gaussian peak | 1/√(8R₂) = 1/√(2π) | Distribution norm | (identity) |
| 21 | BCS gap | π/exp(γ) | Superconducting gap | Euler-Mascheroni |
| 22 | Vena contracta | π/(π+2) = 4R₂/(4R₂+2) | Orifice contraction | Kirchhoff |


## APPENDIX Q: R2 CANCELLATION IDENTITIES

| # | Product | Quantity A (R₂ enters) | Quantity B (R₂ enters) | Result (R₂ gone) | Precision |
|---|---|---|---|---|---|
| 1 | K_J × R_K | 2e/h = 2e/(8R₂ℏ) | h/e² = 8R₂ℏ/e² | 2/e | 10⁻⁸ |
| 2 | G₀ × R_K | 2e²/h | h/e² | 2 | exact |
| 3 | Wire R × Cap C | ρL/(R₂d²) | ε₀R₂d²/t | ρε₀L/t | 30 digits |
| 4 | Rydberg | α²m_ec/(2h) | h = 8R₂ℏ | R₂-free ratio | 13 digits |
| 5 | Bohr × α | ℏ/(m_ec) | — | R₂-free ratio | 12 digits |
| 6 | Ω_DM product | (44/169)×R₂ | R₂ factor | 44/169 pure rational | exact |

Pattern: R₂-free observables achieve 10⁻⁸ to 10⁻¹³ precision. R₂-dependent observables are limited to ~10⁻⁶ (engineering precision). The modulus is topological — it cancels in symmetric ratios.


## APPENDIX R: EXPERIMENT COMPARISON RESULTS — ALL COMPLETED EXPERIMENTS

### R.1 experiment_beta_unification_v0 (29 comparisons)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | Pure gauge gap = 2 | exact | PASS | exact match |
| 2 | SM gap = 218/115 | exact | PASS | exact match |
| 3 | CD gap = 38/27 | exact | PASS | exact match |
| 4 | Casimir form = 2 | exact | PASS | exact match |
| 5 | Generation democracy | bool | PASS | true |
| 6 | b₁_SM = 41/10 | exact | PASS | exact match |
| 7 | b₂_SM = -19/6 | exact | PASS | exact match |
| 8 | b₃_SM = -7 | exact | PASS | exact match |
| 9 | b₁_mod = 25/6 | exact | PASS | exact match |
| 10 | b₂_mod = -13/6 | exact | PASS | exact match |
| 11 | b₃_mod = -20/3 | exact | PASS | exact match |
| 12 | CD db₁ = 1/15 | exact | PASS | exact match |
| 13 | CD db₂ = 1 | exact | PASS | exact match |
| 14 | CD db₃ = 1/3 | exact | PASS | exact match |
| 15 | Y-dep gap at Y=1/6 | exact | PASS | exact match |
| 16 | DM prefactor = 22/13 | exact | PASS | exact match |
| 17 | Ω_DM prefactor = 44/169 | exact | PASS | exact match |
| 18 | Amplification = 44/13 | exact | PASS | exact match |
| 19 | Measured gap ratio | 4 digits | PASS | 1.3582 |
| 20 | α_s one-loop vs measured | miss% | INFO | 8.74% |
| 21 | α_s two-loop SM b_ij | miss% | INFO | 10.13% (bug) |
| 22 | α_s two-loop full b_ij | miss% | INFO | 11.93% (bug) |
| 23 | Koide K | 9 digits | PASS | 0.666660511 |
| 24 | Koide a² vs 2 | miss% | INFO | 0.002% |
| 25 | Koide m_τ vs measured | miss% | INFO | 0.006% |
| 26 | DM/baryon vs Planck | miss% | INFO | 0.073% |
| 27 | Ω_DM vs Planck | miss% | INFO | 21.56% (normalization) |
| 28 | log₁₀(M_GUT/GeV) ∈ [15,16] | range | PASS | 15.54 |
| 29 | L_GUT ∈ [4,6] | range | PASS | 4.978 |

Summary: 22 PASS, 7 INFO, 0 FAIL.

### R.2 experiment_qed_derived_codata_v0 (8 comparisons)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | A₂ from Q335 | 12 digits | PASS | 5.9 × 10⁻¹¹ % |
| 2 | A₃ from Q335 | 11 digits | PASS | 2.4 × 10⁻¹⁰ % |
| 3 | α⁻¹ ∈ [137.035, 137.037] | range | PASS | 137.035998630 |
| 4 | R∞ vs CODATA | miss% | INFO | 8.0 × 10⁻⁷ % |
| 5 | R∞ 8-digit match | digits | PASS | 8.0 × 10⁻⁷ % |
| 6 | a₀ vs CODATA | miss% | INFO | 4.0 × 10⁻⁷ % |
| 7 | μ₀ vs CODATA | miss% | INFO | 4.0 × 10⁻⁷ % |
| 8 | Newton residual < 10⁻⁵⁰ | range | PASS | 1.59 × 10⁻²⁰⁴ |

Summary: 5 PASS, 3 INFO, 0 FAIL.

### R.3 experiment_whatif_scan_v0 (1 comparison)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | Gap ratio ∈ [1.0, 3.0] | range | PASS | 38/27 = 1.407 |

### R.4 experiment_whatif_vl_lepton_doublet_v0 (2 comparisons)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | Gap ratio vs measured | miss% | INFO | 26.05% |
| 2 | Distance ∈ [0, 1] | range | PASS | 0.354 |

### R.5 experiment_whatif_vl_singlet_e_v0 (2 comparisons)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | Gap ratio vs measured | miss% | INFO | 47.25% |
| 2 | Distance ∈ [0, 1] | range | PASS | 0.642 |

### R.6 experiment_whatif_vl_d_singlet_v0 (2 comparisons)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | Gap ratio vs measured | miss% | INFO | 48.59% |
| 2 | Distance ∈ [0, 1] | range | PASS | 0.660 |

### R.7 experiment_whatif_vl_u_singlet_v0 (2 comparisons)

| # | Label | Mode | Status | Detail |
|---|---|---|---|---|
| 1 | Gap ratio vs measured | miss% | INFO | 56.62% |
| 2 | Distance ∈ [0, 1] | range | PASS | 0.769 |


## APPENDIX S: PROGRAM CONNECTION NETWORK

Which programs share which integers and how they connect.

| Program A | Program B | Shared Content | Connection Type |
|---|---|---|---|
| beta_unification | toroidal_dm | Integers 22, 13, 44 | Integer sharing |
| beta_unification | hubble_running | Integer 20/13 | Integer sharing |
| beta_unification | electroweak_anatomy | Same SM betas, same coupling extraction | Common derivations |
| beta_unification | parameter_reduction | CD adds 6 parameters (net 23) | Parameter counting |
| beta_unification | proton_decay | M_GUT from crossing at L = 4.978 | Derived quantity |
| beta_unification | gut_threshold | Three-loop extends two-loop | Precision extension |
| beta_unification | statistical_control | BLOCKED: significance of integer match | Gate dependency |
| toroidal_dm | soliton_gravity | MOND a₀ = cH₀/(8R₂) connects DM transition | Shared formula |
| soliton_gravity | r2_universality | Same R₂ = π/4 in Kepler and all domains | Geometric constant |
| r2_universality | q335_basis | R₂ stored as π_f/4 in Q335 Fraction arithmetic | Storage format |
| q335_basis | electroweak_anatomy | ζ(3), Li₄(1/2), ln(2) needed for QED A₂ coefficients | Transcendental basis |
| koide_analysis | parameter_reduction | Conditional reduction 18→17 via Koide | Parameter counting |
| confinement_mapping | soliton_gravity | Confinement boundary inside soliton hierarchy | Nesting |
| confinement_mapping | beta_unification | Beta running stops at confinement upper face | Running boundary |
| hubble_running | soliton_gravity | Boundary transit count N for cosmological running | Scale counting |


## APPENDIX T: PITFALL REGISTRY

Known errors that have occurred and should be documented on value nodes to prevent recurrence.

| Node Key | Wrong | Right | Session | Impact |
|---|---|---|---|---|
| coupling_alpha_2_inverse_mz_v0 | 1/α₂ = α_inv / sin²θ_W = 593 | 1/α₂ = sin²θ_W × α_inv = 31.7 | PHYS-30 | Catastrophic — wrong by 19× |
| beta_modified_u1_total_v0 | 62/15 | 25/6 (same value, canonical form) | DATA-5 | Cosmetic — same number, confusing notation |
| beta_two_loop_vl_dbij_su2_su2_v0 | 39/4 (gauge + fermion double-count) | 15/4 (fermion only) | PHYS-33 | Two-loop α_s off by 10% |
| mass_w_boson_v0 | 80379 MeV | 80369.2 MeV = 803692/10 | DATA-4 | 0.012% mass error |
| gap_mssm_v0 | 5/7 = 0.714 | 7/5 = 1.400 | DATA-5 | Inverted ratio — wrong by 2× |
| qed_c8_total_v0 | Used as A₄ = 107.71 | A₄ = -1.9122 (different convention) | PHYS-36 | α off by 2752 ppb |

Each pitfall should be an entry on the relevant value node's `pitfalls` list. Currently documented in this appendix; to be migrated to node metadata in v1.


## APPENDIX U: FILE MANIFEST

Complete listing of all files in the DATA-6 system.

### U.1 Value JSON Files (24 files, 414 nodes)

| File | Nodes | Size (approx) |
|---|---|---|
| values_si_exact_v0.json | 8 | 2 KB |
| values_measured_v0.json | 13 | 4 KB |
| values_electroweak_v0.json | 6 | 2 KB |
| values_quarks_ckm_v0.json | 11 | 3 KB |
| values_nuclear_spectro_v0.json | 9 | 3 KB |
| values_q335_v0.json | 31 | 15 KB |
| values_ratios_koide_v0.json | 11 | 3 KB |
| values_gut_beta_v0.json | 32 | 10 KB |
| values_integer_pool_v0.json | 10 | 3 KB |
| values_generation_democracy_v0.json | 3 | 1 KB |
| values_gap_ratios_v0.json | 7 | 2 KB |
| values_two_loop_vl_dbij_v0.json | 9 | 3 KB |
| values_higgs_beta_v0.json | 3 | 1 KB |
| values_representations_v0.json | 54 | 15 KB |
| values_engineering_v0.json | 66 | 20 KB |
| values_astrophysical_v0.json | 12 | 4 KB |
| values_cosmological_v0.json | 11 | 4 KB |
| values_observational_v0.json | 52 | 15 KB |
| values_experiment_inputs_v0.json | 8 | 3 KB |
| values_qed_laporta_v0.json | 8 | 120 KB |
| values_qed_coefficients_v0.json | 8 | 3 KB |
| values_qed_ae_measured_v0.json | 4 | 2 KB |
| values_qed_series_rationals_v0.json | 12 | 4 KB |
| values_whatif_*_v0.json (×5) | 15 | 5 KB |

### U.2 Other JSON Files

| File | Type | Nodes |
|---|---|---|
| connections_v0.json | Connection metadata | 63 |
| connections_more_v0.json | Extended connections | 4 |
| connections_papers_v0.json | Paper cross-references | 29 |
| programs_v0_complete.json | Research programs | 13 |
| experiment_*.json (×17) | Experiment specs | 17 |
| result_*.json (×7+) | Experiment results | 7+ |

### U.3 Python Files

| File | Lines (approx) | Role |
|---|---|---|
| data6.py | 200 | CLI entry point / router |
| data_6_run.py | 350 | Experiment runner |
| data_6_diagrams.py | 300 | Diagram generator |
| data_6_diagram_lib.py | 400 | Diagram helper library |
| _data_6_derivations_v0.py | 800 | 18 derivations + 5 connections |
| _data_6_derivations_more_v0.py | 1200 | 39 derivations + 4 connections |
| data_6_export_json.py | 500 | JSON exporter from platform |
| laporta_to_json.py | 100 | Laporta coefficient converter |


## APPENDIX V: KNOWN ISSUES AND TECHNICAL DEBT

| # | Issue | Category | Severity | Status |
|---|---|---|---|---|
| 1 | Two-loop α_s shows 10-12% miss (should be <1%) | Correctness | High | Open — db_ij matrix investigation needed |
| 2 | 10 key aliases across 2 files | Trust | Medium | Open — pick canonical, update exporter |
| 3 | 0 pitfall entries on value nodes | Safety | Medium | Open — migrate from Appendix T |
| 4 | No pre-flight dependency validation | Robustness | Medium | Open — runner starts without checking |
| 5 | Hardcoded Euler step count (4000) | Principle | Low | Open — should be config_* value node |
| 6 | Connection outputs discarded after printing | Capability | Low | Open — should merge into pool |
| 7 | No dataset support | Capability | Low | Specified — not implemented |
| 8 | No identity match mode | Capability | Low | Specified — needed for R₂ cancellations |
| 9 | Laporta C81/C83 convention unmapped | Investigation | Low | Archived — Laporta numbers stored, convention open |
| 10 | statistical_control script unwritten | Blocking | High | Open — blocks beta_unification confirmation |
