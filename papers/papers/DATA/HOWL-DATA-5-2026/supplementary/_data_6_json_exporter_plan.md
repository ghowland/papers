# DATA-6 JSON Export Plan

## What I Read

12 files total:

- `phys24_lib.py` — 146 constants, Q335 basis, helpers, check functions
- `phys24_lib_test.py` — 148-check precision test
- `phys24_structure_lib.py` — representations, particle catalog, anomalies, closed paths, paper cross-refs, DATA-4 map
- `phys24_hubble_lib.py` — H0 measurements, running curve hypothesis, falsification tests
- `phys24_domain_lib.py` — 22 R2 equations, disc/fiber/speaker/wire/RF/semiconductor data, cancellations, BCS
- `phys24_boundary_map_lib.py` — 19 boundaries, 5 forces, scale conversions, traversal
- `phys24_platform_demo.py` — demo showing all libraries together (not exported)
- `demo_cross_domain.py` — cross-domain translation demo (not exported)
- `phys24_platform_diagrams.py` — 8 diagram figures (not exported as data, but diagram specs could be)
- `nested_soliton_gravity.py` — experiment with 11-level hierarchy
- `dwarf_soliton_ground_state.py` — experiment with dwarf catalog
- `beta_unification_test.py` — experiment with 15 cosmological predictions

---

## Export Strategy

### Rule 1: Group by source and topic, not one mega file
Each JSON file is small enough to read in one pass. Versioned filenames.

### Rule 2: Only core values, no defaults
If a field would be a default/placeholder, omit it. Only export what the source code actually contains.

### Rule 3: Derivation functions stay as Python
Callable logic cannot be JSON. Derivation metadata (inputs, outputs, description) can be JSON. The callable is referenced by key.

### Rule 4: Tests become experiment nodes
`phys24_lib_test.py` checks become experiment comparisons with formal match modes.

---

## Export Files — 16 JSON files

### Group 1: Values from `phys24_lib.py`

**File: `values_si_exact_v0.json`**
7 entries. Section A. SI defined constants.
- `c`, `h_planck`, `e_charge`, `k_B`, `N_A`, `dv_Cs`, `K_cd`
- All `value_type: "exact_fraction"`, `level: 0`
- Fraction serialized as `{"_type": "Fraction", "num": ..., "den": ...}`

**File: `values_measured_v0.json`**
13 entries. Section B. CODATA 2022.
- `alpha_inv`, `m_e`, `m_mu`, `m_tau`, `m_p`, `mp_me`, `R_inf`, `a_0`, `a_e`, `a_mu`, `sin2_tW`, `alpha_s`, `mu_0`
- All `level: 2`, with `digits` from the source comments

**File: `values_electroweak_v0.json`**
6 entries. Section C. LEP/PDG.
- `M_Z`, `Gamma_Z`, `M_W`, `m_t`, `m_H`, `G_F`

**File: `values_quarks_ckm_v0.json`**
11 entries. Section D. PDG 2024 / FLAG.
- `m_u` through `mu_md`
- FLAG ratios get `notes` about independence from PDG masses

**File: `values_nuclear_v0.json`**
9 entries. Sections E + F.
- `m_n`, `mn_mp_diff`, `m_pi_p`, `m_pi_0`, `m_K_p`, `m_D`, `m_He4`, `E_D`, `H_1S2S`

**File: `values_q335_v0.json`**
31 entries. Section G. Q335 analytical constants.
- `pi_f` through `E_3qtr_f`
- All `level: 0`, `digits: 100`, `value_type: "exact_fraction"`
- The Fraction numerators are large integers (100+ digits). Serialize as strings in the `num` field to avoid JSON integer limits.
- Include `R2_f`, `R4_f`, `twopi_f` as derived entries with `source` noting the derivation identity (e.g. `"pi_f / 4"`)

**File: `values_ratios_koide_v0.json`**
11 entries. Sections K + Koide.
- Mass ratios: `mmu_me` through `K_koide`
- Koide amplitudes: `a2_lep`, `a2_down`, `a2_up`

**File: `values_gut_beta_v0.json`**
~30 entries. Section N + derived betas.
- SM betas: `b1_SM`, `b2_SM`, `b3_SM`
- CD shifts: `db1_VL`, `db2_VL`, `db3_VL`
- Modified betas: `b1_mod`, `b2_mod`, `b3_mod`
- Gap ratios: `gap_SM`, `gap_VL`, `gap_MSSM`, `gap_measured`
- Two-loop SM `b_ij` matrix: 9 entries
- CD parameters: `M_VL_lo`, `M_VL_hi`, `theta14_est`
- Derived couplings: `inv_a1`, `inv_a2`, `inv_a3`, `alpha_em`
- Named constants: `CD_Y`, `casimir_gap`, `hbar`

### Group 2: Values from other libraries

**File: `values_astrophysical_v0.json`**
~15 entries. Constants currently hardcoded across multiple files.
- `G_newton`, `M_sun`, `M_earth`, `M_moon`, `R_earth`, `R_sun`, `AU`, `pc_m`, `c_light` (alias to SI `c`), `sigma_SB`, `tau_mu`, `hbar_c_MeV_fm`
- All `level: 2`, `value_type: "approximate"`, `section: "astrophysical"`

**File: `values_engineering_v0.json`**
~80 entries. From `phys24_domain_lib.py`.
- AWG wire diameters: 12 entries
- Optical disc specs: ~15 entries (5 per format × 3 formats)
- Fiber specs: ~7 entries (SMF-28)
- Speaker specs: 6 entries
- Semiconductor specs: ~5 entries (wafer, EUV, ArF, lattice constant, etc.)
- RF standards: ~7 entries (GPS L1/L2, 5G subcarriers)
- Engineering constants: `CU_RESISTIVITY`, `EPSILON_0`, `C_SOUND_AIR`
- Bessel zeros: `J01`, `J11`
- Euler-Mascheroni: `gamma_EM`
- Sample rates: 4 entries (exact Fractions)
- Just intonation: 7 entries (exact Fractions)
- Storage interfaces, memory standards, baud rates: ~15 entries
- BCS materials: 4 entries
- All with `section: "engineering"` or `section: "observational"`

**File: `values_observational_v0.json`**
~50 entries. From experiment scripts and hubble lib.
- H0 measurements: 5 entries with full metadata (value, uncertainty, year, source, method)
- Dwarf galaxy catalog: 8 classical × ~7 fields + 3 ultra-faint × ~6 fields = ~75 individual values, but group as structured entries (one value node per measurement, keyed like `obs_fornax_sigma_v0`)
- Cosmological targets: `Lambda_log10_measured`, `DM_baryon_measured`, `Omega_b_measured`, `Omega_DM_measured`, etc.

### Group 3: Connections

**File: `connections_v0_meta.json`**
Metadata for all connection types. No callables — those stay in Python.

From `phys24_boundary_map_lib.py`:
- 19 boundary connections, each with `connection_type: "boundary"`, listing scale, forces, couplings, above/below, open questions

From `phys24_domain_lib.py`:
- 22 R2 equation connections with `connection_type: "universal_equation"`, each with equation, Z coordinator, precision
- 7 R2 cancellation connections with `connection_type: "cancellation"`, each with formula, status, remains

From `phys24_structure_lib.py`:
- 7 closed paths with `connection_type: "adjacency"` (killed paths with reason)
- 3 anomaly evidence bundles with `connection_type: "adjacency"`
- Paper cross-reference map (47 entries linking DATA-4 IDs to values)

From `phys24_hubble_lib.py`:
- Structural parallel connection (alpha running ↔ H0 running)
- 6 series connections

From bootstrap connection registry (`data_5_v0_master_connection_registry.py`):
- 5 connections already defined: coupling convergence, gap correction chain, integer network, three programs shared set, object adjacency

### Group 4: Programs

**File: `programs_v0.json`**
3 entries from `data_5_helpers_experiment.py` / `data_5_populate.py`:
- `program_beta_unification_v0`: thesis, status ACTIVE, scripts, kill switches, connections
- `program_toroidal_dm_v0`: thesis, status ACTIVE, scripts, kill switches
- `program_hubble_running_v0`: thesis, status ACTIVE, scripts, kill switches

Plus experiment timeline from `phys24_structure_lib.py`:
- `Hyper-K`, `HL-LHC`, `Belle_II` as program-adjacent nodes

### Group 5: Derivation metadata

**File: `derivations_v0_meta.json`**
Metadata only — callables stay in Python.

From `data_5_v0_master_derivation_registry.py` (18 derivations):
- Each entry: `key`, `inputs` (list of canonical keys), `outputs` (list of canonical keys), `arithmetic_mode`, `output_type`, `description`

From `data_4_derivation_lib.py` (~15 functions):
- `derive_couplings`, `compute_vl_one_loop`, `compute_vl_two_loop`, `run_one_loop_frac`, `find_crossing_L`, `gap_ratio_from_betas`, `predict_alpha_s_one_loop`, `predict_alpha_s_two_loop`, `predict_sin2_one_loop`, `predict_sin2_two_loop`, `koide_ratio`, `koide_amplitude_sq`, `koide_predict_m_tau`, `decompose_SM_betas`

From domain helpers (~20 functions):
- `R2_area`, `airy_resolution`, `disc_spot`, `fiber_mode_area`, `fiber_V_number`, `wire_resistance`, `circular_capacitance`, `pipe_flow`, `orifice_flow`, `helmholtz_freq`, `sound_intensity`, `thermal_radiation`, `fourier_norm`, `gaussian_norm`, `gaussian_peak`, `bcs_gap`, `fspl_dB`, `antenna_area`, `litho_resolution`, `rayleigh_loss`

From boundary/gravity helpers (~15 functions):
- `grav_coupling`, `binding_fraction`, `escape_velocity`, `hill_sphere`, `kepler_period`, `process_rate_ratio`, `gps_correction`, `muon_observed_lifetime`, `twin_paradox`, `ds_squared`, `mond_a0`, `mond_transition_radius`

From experiment helpers (~10 functions):
- `dm_baryon_ratio`, `omega_dm`, `omega_b`, `omega_matter`, `omega_de`, `amplification_factor`, `virial_ratio`, `frame_dragging`, `dwarf_purity`, `faber_jackson`, `tully_fisher`

Pure math (~5 functions):
- `casimir_adj`, `casimir_fund`, `dynkin_fund`, `yang_mills_coefficient`, `gauge_beta`

Total: ~80 derivation metadata entries.

### Group 6: Experiment specifications

**File: `experiments_v0.json`**
From the three experiment scripts, each becomes an experiment node:

`experiment_beta_unification_v0`:
- `purpose`: "PHYS series beta unification"
- `experiment_mode`: "standard"
- `dependencies`: alpha, beta integers, R2, R4
- `execution_plan`: ordered list of derivation keys for all 6 formulas
- `comparisons`: 15+ entries comparing predictions against cosmological measurements, each with `match_mode`, `reference_value`, `reference_source: "measured"`, threshold

`experiment_nested_soliton_gravity_v0`:
- `purpose`: "Gravity as nested soliton ground state"
- `experiment_mode`: "standard"
- `dependencies`: astrophysical constants, R2, boundary stack
- `execution_plan`: coupling hierarchy, binding fractions, Hill spheres, Kepler, process rates
- `comparisons`: ~10 entries (Kepler periods, GPS correction, coupling inequalities)

`experiment_dwarf_soliton_v0`:
- `purpose`: "Dwarf spheroidals as pure solitons"
- `experiment_mode`: "standard"
- `dependencies`: dwarf catalog, beta integers, DM ratio
- `execution_plan`: purity spectrum, FJ/TF, core scaling
- `comparisons`: ~8 entries

From `phys24_lib_test.py`:
`experiment_platform_precision_v0`:
- `experiment_mode`: "verification"
- 148 comparisons covering all value groups
- Each comparison: output key, match mode (`exact` or `digits`), reference value, precision digits needed

---

## What Does NOT Get Exported

- Demo scripts (`phys24_platform_demo.py`, `demo_cross_domain.py`) — these are demonstrations, not data
- Diagram generation code (`phys24_platform_diagrams.py`) — the rendering logic stays Python. The provenance log pattern informs how diagram derivations work, but the matplotlib code isn't data
- Check/test infrastructure functions (`chk`, `chk_exact`, `chk_bool`, `print_summary`) — these become the comparison contract in the runner, not standalone exports
- `_full` aliases from `phys24_lib.py` — these are Python-side convenience. In DATA-6, each value has one entry. The `_full` pattern is replaced by the `digits` field

---

## Export Implementation Plan

### Step 1: Write the value exporter
One Python script that imports `phys24_lib.py` and writes the 8 value JSON files. For each constant:
- Extract `key` (map from Python variable name to DATA-6 canonical key using a hand-written mapping table)
- Extract `value` (Fraction → serialized, int → as-is, mpf → string)
- Extract `value_type` (inferred from Python type)
- Extract `unit`, `level`, `digits`, `source`, `section` from the DATA-4 map and section comments
- Write JSON with `_json_default` handler for Fraction

The mapping table is the core work. ~200 entries mapping `alpha_inv` → `coupling_alpha_em_inverse`, `m_e` → `mass_electron`, etc. This is a one-time manual mapping that establishes the canonical names.

### Step 2: Write the engineering/observational exporter
Separate script that imports `phys24_domain_lib.py`, `phys24_hubble_lib.py`, and experiment scripts. Writes `values_engineering_v0.json`, `values_observational_v0.json`, `values_astrophysical_v0.json`.

### Step 3: Write the connection exporter
Script that imports `phys24_boundary_map_lib.py`, `phys24_domain_lib.py`, `phys24_structure_lib.py`. Writes `connections_v0_meta.json`. Each boundary, R2 equation, cancellation, closed path, anomaly becomes a connection metadata entry.

### Step 4: Write the derivation metadata exporter
Script that reads docstrings from all derivation functions, extracts input/output keys, and writes `derivations_v0_meta.json`. This is semi-automated — docstrings have the binding declarations, but the output keys need to be extracted from the return dicts.

### Step 5: Write the experiment exporter
Script that reads the three experiment scripts and the platform test, creates experiment node JSON with dependency declarations and comparison lists.

### Step 6: Write the program exporter
Script that exports the 3 research programs from `data_5_populate.py`.

---

## Spec v0.2 Additions Identified

From reading these files, the following items need to go into the spec v0.2:

1. **Structured value entries.** Some values are naturally grouped (dwarf galaxy = 7 fields per galaxy, disc format = 5 fields per format). The spec needs to decide: flat keys (`obs_fornax_sigma_v0`, `obs_fornax_mass_visible_v0`) or structured entries with a parent key. I recommend flat keys with a shared `section` and `topic` prefix for queryability.

2. **Paper cross-reference as connection type.** `PAPER_TOPICS` and the `papers` field on many objects. Add `connection_type: "paper_reference"`.

3. **Closed paths as program status.** The 7 `CLOSED_PATHS` are essentially programs with `status: "KILLED"`. They should be program nodes.

4. **Anomaly evidence as connection type.** The 3 anomalies linking quantum numbers to experimental observations. Add `connection_type: "anomaly_evidence"`.

5. **Experiment timeline.** `Hyper-K`, `HL-LHC`, `Belle_II` with predictions and decisive dates. These could be program nodes or a new `connection_type: "experimental_timeline"`.

6. **`precision_convention` field.** From `phys24_lib.py`'s header: `foo` = working precision, `foo_full` = maximum precision. In DATA-6, each value has one entry with the full precision. The convention is captured by the `digits` field.

7. **Energy landscape as connection.** The 5 `ENERGY_DOMAINS` from `phys24_structure_lib.py` are connections with `connection_type: "boundary"` but defined by energy range rather than single scale.

---

## Execution Order

1. Value mapping table (manual, ~200 entries) — this is the foundation
2. Value exporter script → 8 JSON files
3. Engineering/observational exporter → 3 JSON files
4. Connection exporter → 1 JSON file
5. Program exporter → 1 JSON file
6. Derivation metadata exporter → 1 JSON file
7. Experiment exporter → 1 JSON file
8. Verify: load all JSON, count entries, spot-check values against library

Total: ~16 JSON files, ~500 value nodes, ~80 derivation metadata entries, ~60 connection entries, 3 program nodes, 4 experiment nodes.

Ready for corrections before I write the exporter code.
