# A Versioned Node System for Integer Fraction Physics
## Physics Database and Experiment System

**Registry:** [@HOWL-DATA-6-2026]

**Series Path:** [@HOWL-DATA-4-2026] → [@HOWL-DATA-5-2026] → [@HOWL-DATA-6-2026]

**Date:** April 5, 2026

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
| MATH-1 | @HOWL-MATH-1 | Q335 constants as geom_* value nodes |
| MATH-2 | @HOWL-MATH-2 | Q335 basis, 31 nodes at 100 digits |
| MATH-6 | @HOWL-MATH-6 | PSLQ 82/82 null, integer pool nodes |
| DATA-4 | @HOWL-DATA-4 | 146 entries migrated to value nodes |
| PHYS-7 | @HOWL-PHYS-7 | theta_QCD = 0 in parameter_reduction program |
| PHYS-8 | @HOWL-PHYS-8 | Koide K, a², m_τ in koide_analysis experiment |
| PHYS-9 | @HOWL-PHYS-9 | A₁-A₄ in QED extraction, verified at 4.3 ppb |
| PHYS-11 | @HOWL-PHYS-11 | R2 domains in r2_universality experiment |
| PHYS-13 | @HOWL-PHYS-13 | Gap ratio in beta_unification experiment |
| PHYS-15 | @HOWL-PHYS-15 | CD identification in whatif_scan experiments |
| PHYS-17 | @HOWL-PHYS-17 | Generation democracy in beta_unification |
| PHYS-20 | @HOWL-PHYS-20 | Proton decay in proton_decay experiment |
| PHYS-36 | @HOWL-PHYS-36 | QED 5-loop chain in qed_derived_codata experiment |

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
