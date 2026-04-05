# DATA-6 Technical Specification

## Universal Versioned Node Physics System

Document: `data_6_tech_spec_v0.2.md`
Version: 0.2
Date: 2026-04-05
Status: Working Draft — reflects implemented system

---

## 1. Purpose and Scope

DATA-6 is a dynamic node-based system for physics research built on integer fraction arithmetic. Every entity — constant, derivation, connection, experiment, result, program, dataset — is a versioned node with a canonical key, a shared metadata envelope, and full provenance.

The system is implemented and operational. This spec describes what exists, what works, and what remains open.

Current state: 357 value nodes across 20 JSON files, 18 derivation functions, 5 connection functions, 1 experiment definition with 29 comparisons and 3 diagram specs, a generic CLI runner, and a diagram generator. All exact arithmetic checks pass. All derivations execute. All connections resolve.

---

## 2. Core Principles

### 2.1 Everything is a versioned node
Every entity has a canonical key and a version. Once a versioned key exists it is never edited in place. Corrections produce new versions.

### 2.2 Inputs and outputs are symmetric
There is no privileged distinction between a raw constant and an experiment output at the access layer. Both are named values. Both are version-pinned. Both carry provenance.

### 2.3 Provenance is first-order
Every value traces back through which versions of which constants, which derivation function version, which experiment, and which prior results produced it.

### 2.4 Integer fraction arithmetic
`fractions.Fraction` is the primary numeric type. `float` is never used. `mpmath.mpf` is permitted only at the irrational/numerical boundary (pi, sqrt, exp, log, numerical integration). `mp.dps = 100` minimum. The `math` module is never used. Conversion to float happens ONLY at two boundaries: display (diagrams) and irrational math. Never in the computation chain.

### 2.5 Append-only versioning
All versioned keys follow `canonical_name_vN`. Version 0 is the initial registration. New understanding means new version. Old versions are never modified or deleted.

### 2.6 No hardcoded physics constants
All values come from the registry. Derivation functions pull every constant from value nodes via the resolver. No `mpf("6.674e-11")` buried in executable code.

### 2.7 Helpers are derivations
There is no separate "helper" category. If an experiment or derivation chain uses a function, that function is a registered versioned derivation node.

---

## 3. Common Metadata Envelope

Every node of every type carries these fields.

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes | Full versioned key, e.g. `mass_z_boson_v0` |
| `canonical` | string | yes | Key without version suffix |
| `version` | int | yes | 0-based |
| `node_type` | string | yes | One of 8 types |
| `topic` | string | yes | First token of canonical key |
| `term` | string | yes | Remaining tokens after topic |
| `level` | int or None | yes | 0=geometry, 1=group theory, 2=measured, 3=derived/predicted, None=unknown |
| `section` | string | no | Grouping tag |
| `source` | string | yes | Origin reference |
| `notes` | string | no | Human context |
| `tags` | list[str] | no | Classification tags |
| `created` | string | no | ISO timestamp |
| `supersedes` | string | no | Key of version this replaces |
| `legacy_refs` | dict | no | Cross-platform IDs |
| `pitfalls` | list[dict] | no | Documented prior errors |

### 3.1 Level convention

| Level | Meaning | Examples |
|---|---|---|
| 0 | Pure geometry / exact math | R2, pi, e, sqrt2, Bessel zeros, zeta values |
| 1 | Group theory / structural | Beta coefficients, Casimirs, Dynkin indices, gap ratios |
| 2 | Measured / observational | alpha_inv, sin2_tW, alpha_s, masses, H0, dwarf galaxy data |
| 3 | Derived / predicted | alpha_s from unification, Koide m_tau, Omega_DM from integers |
| None | Unknown | Must be resolved |

Level applies to all node types, not just values.

### 3.2 Pitfalls

Any node type can carry pitfalls. Each entry:

```json
{
    "wrong": "1/a2 = alpha_inv / sin2_tW",
    "right": "1/a2 = sin2_tW * alpha_inv",
    "session": "PHYS-30"
}
```

---

## 4. Node Types

The system has 8 node types.

### 4.1 Value

An atomic named fact: a physical constant, a measured parameter, a tabulated number, a classification, an engineering specification, an observational catalog entry, or an experiment output.

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | Fraction / int / str / None | yes | The value itself |
| `value_type` | string | yes | `exact_fraction`, `exact_integer`, `approximate`, `classification`, `deferred` |
| `unit` | string | yes | Physical unit or `dimensionless` |
| `digits` | int | no | Significant figures |
| `uncertainty` | string | no | Uncertainty if applicable |
| `ref` | string | no | Legacy reference for deferred values |

Value type rules:
- `exact_fraction`: value is a `Fraction`. Preferred type.
- `exact_integer`: value is an `int`.
- `approximate`: value is a string containing a plain decimal number. No scientific notation — `"0.0000021969811"` not `"2.1969811e-6"`.
- `classification`: value is a string label.
- `deferred`: value is `None`, `ref` field contains external reference.

### 4.2 Derivation

A versioned executable transformation.

| Field | Type | Required | Description |
|---|---|---|---|
| `callable` | function | yes | Python function |
| `inputs` | list[str] | yes | Canonical keys of required input values |
| `outputs` | list[str] | yes | Canonical keys of produced output values |
| `arithmetic_mode` | string | yes | `exact`, `mixed`, `numeric` |
| `description` | string | yes | What this derivation computes |

Callable contract:

```python
def derivation_name_vN(value_dicts: list[dict]) -> dict:
    return {
        "key": "derivation_name_vN",
        "outputs": {"output_key_vN": value, ...},
        "notes": ""
    }
```

Arithmetic modes:
- `exact`: `Fraction` only.
- `mixed`: `Fraction` for rational steps, `mpf` at irrational boundary.
- `numeric`: numerical methods (Euler integration, bisection). Results stored as approximate strings.

### 4.3 Connection

A versioned executable relationship bundle.

| Field | Type | Required | Description |
|---|---|---|---|
| `callable` | function | yes | Python function |
| `inputs` | list[str] | yes | Canonical keys |
| `connection_type` | string | yes | See table below |
| `description` | string | yes | What relationship this captures |

Callable contract:

```python
def connection_name_vN(value_dicts: list[dict]) -> dict:
    return {
        "key": "connection_name_vN",
        "named_values": {"local_name": {...}, ...},
        "edges": [{"from": "a", "to": "b", "relation": "..."}, ...],
        "notes": ""
    }
```

Connection types (extensible):

| Type | Meaning |
|---|---|
| `convergence` | Values converging toward a common point |
| `correction_chain` | Sequential corrections from one state to another |
| `traceability` | Where specific values appear across the system |
| `adjacency` | Which values relate to which |
| `shared_set` | Values shared across programs |
| `boundary` | Values at a physics scale boundary |
| `hierarchy` | Ordered multi-scale relationship |
| `cancellation` | Geometric/algebraic cancellation identity |
| `universal_equation` | Parameterized equation template |
| `anomaly_evidence` | Experimental anomaly linked to quantum numbers |
| `paper_reference` | Cross-reference to published paper |

### 4.4 Experiment

A versioned execution plan.

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string | yes | What this experiment tests |
| `purpose` | string | no | Links to research program |
| `experiment_mode` | string | yes | `standard`, `whatif`, `verification`, `consistency` |
| `dependencies` | dict | yes | Version-pinned requirements |
| `execution_plan` | list[str] | yes | Ordered derivation keys |
| `connections` | list[str] | no | Connection keys to resolve |
| `expected_outputs` | list[str] | yes | Canonical keys this experiment must produce |
| `comparisons` | list[dict] | no | Comparison specifications |
| `diagrams` | list[dict] | no | Diagram specifications |

Dependency declaration:

```json
{
    "dependencies": {
        "values": {"coupling_alpha_em_inverse": 0},
        "derivations": {"coupling_extraction": 0},
        "connections": {"connection_coupling_convergence": 0}
    }
}
```

Current implementation loads all v0 values and ignores version pins. Version enforcement is deferred.

### 4.5 Result

Output record of a completed experiment run.

| Field | Type | Required | Description |
|---|---|---|---|
| `experiment_key` | string | yes | Versioned key of the experiment |
| `outputs` | dict | yes | Map of output key to value |
| `comparison_results` | list[dict] | no | Results of each comparison |
| `execution_log` | list[dict] | no | Ordered record of derivations executed |
| `connections_resolved` | list[str] | no | Connection keys resolved |
| `diagrams_produced` | list[str] | no | Diagram keys generated |
| `timestamp` | string | yes | ISO timestamp |
| `status` | string | yes | `complete`, `partial`, `failed` |
| `summary` | dict | no | Counts of pass/fail/info/skip |

Result outputs become values. A consumer requesting `result_alpha_s_two_loop_full_bij` gets the value from the result, with full provenance.

### 4.6 Program

A research program with thesis, status, and kill switches.

| Field | Type | Required | Description |
|---|---|---|---|
| `thesis` | string | yes | The research hypothesis |
| `status` | string | yes | `ACTIVE`, `PARKED`, `KILLED`, `CONFIRMED` |
| `scripts` | list[dict] | no | Each with `name`, `description`, `stage` |
| `kill_switches` | list[dict] | no | Each with `name`, `condition`, `data_source` |
| `program_connections` | dict | no | Map of program_key to relationship |

### 4.7 Dataset

A lightweight composition spec defining which version of each value to use.

| Field | Type | Required | Description |
|---|---|---|---|
| `base` | string or None | yes | Key of base dataset, or None for root |
| `overrides` | dict | yes | Map of canonical_key to version number |

Not yet implemented in the runner. The root dataset `howl_v0` is implicit — all `_v0` values.

### 4.8 Diagram

A diagram specification embedded in an experiment's `diagrams` list. Rendered by `data_6_diagrams.py`.

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes | Unique key, used as PNG filename |
| `title` | string | yes | Figure title |
| `type` | string | yes | Renderer type (see table) |
| `notes` | string | no | Caption or annotation text |

Type-specific fields vary by renderer:

| Type | Additional fields | What it renders |
|---|---|---|
| `bar` | `categories`, `values_from` | Categorical bar chart with miss% annotations |
| `comparison_table` | `rows` (each with `label`, `predicted`, `measured`) | Horizontal paired bars with miss% |
| `line` | `series`, `source_derivation`, `x_axis`, `y_axis` | Line chart or coupling running curves |

The `line` renderer detects coupling running from the `source_derivation` field and recomputes curves from stored couplings and betas. This is the one place the diagram system does computation — using the same values the experiment used.

---

## 5. Naming and Versioning Rules

### 5.1 Key format

```
{topic}_{term}_v{N}
```

Lowercase, underscore-separated. Topic is a single word. Term is one or more descriptive words.

### 5.2 Topic prefixes

| Prefix | Scope |
|---|---|
| `beta` | Beta function coefficients and shifts |
| `coupling` | Coupling constants and derived coupling values |
| `mass` | Particle and boson masses |
| `gap` | Gap ratios and related values |
| `group` | Group theory constants |
| `rep` | Representation data |
| `geom` | Geometric constants |
| `math` | Mathematical constants |
| `integer` | Integer pool values |
| `koide` | Koide relation data |
| `cosmo` | Cosmological parameters |
| `astro` | Astrophysical constants |
| `eng` | Engineering constants |
| `obs` | Observational catalog entries |
| `si` | SI defined constants |
| `result` | Derivation and experiment outputs |
| `connection` | Connection bundle names |
| `experiment` | Experiment plan names |
| `program` | Research program names |
| `dataset` | Dataset version names |

### 5.3 File naming

JSON value files: `values_{section}_v0.json`
Experiment files: `experiment_{name}_v0.json`
Result files: `result_experiment_{name}_v0.json`
Connection files: `connections_{section}_v0.json`
Program files: `programs_v0.json`

### 5.4 Uniqueness

No two nodes of any type share the same versioned key. Globally unique.

### 5.5 Append-only

Once a versioned key exists, it is never edited. New understanding means `_v1`, `_v2`.

---

## 6. Dataset Versions

### 6.1 Structure

```json
{
    "key": "dataset_howl_v1",
    "base": "dataset_howl_v0",
    "overrides": {"integer_four_times_yang_mills": 1}
}
```

### 6.2 Rules

- Root dataset `howl_v0` includes all `_v0` values by default.
- Overrides are sparse.
- Chains flatten via the resolver.
- Not yet implemented in the runner.

---

## 7. Universal Access Interface

### 7.1 Value access

```python
get(canonical_key, version=None, dataset=None) -> value_entry
```

Current implementation: `_value_map(value_dicts)` builds a flat dict from the value pool. Last entry wins — no duplicate errors. This is the correct behavior for the runner, where derivation outputs must override stored values.

### 7.2 Value pool semantics

The value pool is a list of value entry dicts. When a derivation runs, its outputs are appended as new entries. Later derivations see the latest value for any key. This is append-only within a run — the pool only grows.

---

## 8. Resolver

### 8.1 Current implementation

The runner loads all `values_*.json` files into a flat list. No version pinning. No dataset resolution. All v0 values enter the pool. Derivation outputs are appended with `source` set to the derivation key.

### 8.2 Future resolver

Will enforce dependency version pins from the experiment JSON. Will support dataset contexts. Will detect missing keys before execution.

---

## 9. Runner

### 9.1 Reference implementation

`data_6_run.py` — generic CLI runner.

```
python data_6_run.py beta_unification_v0
```

### 9.2 Execution flow

1. Find `experiment_{name}.json`
2. Load all `values_*.json` into value pool
3. Execute each derivation in `execution_plan` order
4. After each derivation, merge outputs into the pool
5. Execute each connection in `connections` list
6. Check `expected_outputs` are present
7. Evaluate each comparison in `comparisons`
8. List diagram specs (not rendered — use `data_6_diagrams.py`)
9. Write result JSON to CWD
10. Print summary

### 9.3 Derivation chaining

Derivations may depend on outputs from earlier derivations in the same plan. The runner executes in declared order and merges after each step. The experiment author declares valid order.

### 9.4 Result output

Result JSON written to CWD as `result_experiment_{name}_v0.json`. Contains all derivation outputs, comparison results, execution log, and summary counts. Serialized with `_serialize_default` for Fraction values.

---

## 10. Arithmetic Rules

### 10.1 Hierarchy

1. `fractions.Fraction` — preferred for all exact rational values
2. `int` — acceptable, implicitly `Fraction(n, 1)`
3. `mpmath.mpf` — only at irrational/numerical boundaries
4. `str` — for approximate values with no known exact rational form
5. `float` — never used anywhere in the system

### 10.2 Computation rules

- All exact derivations operate on `Fraction`.
- When a derivation needs pi, sqrt, exp, log: convert to `mpf`, compute, store result as approximate string.
- `mp.dps = 100` minimum.
- `math` module never imported.
- Deterministic execution.

### 10.3 Rendering boundary

Fraction to float conversion happens ONLY at display (diagrams) and irrational math. Never in the computation chain. The diagram library's `to_float()` is the single conversion point for rendering.

### 10.4 JSON serialization

Fraction: `{"_type": "Fraction", "num": "22", "den": "13"}` — numerator and denominator as strings for large Q335 values.

mpf: `{"_type": "mpf", "value": "1.6933077261548"}`

Approximate values: plain decimal strings, never scientific notation. `"0.0000021969811"` not `"2.1969811e-6"`. The exporter runs `_normalize_decimal()` on all string values.

---

## 11. Comparison and Verification Contract

### 11.1 Implemented match modes

| Mode | Fields | Pass condition |
|---|---|---|
| `exact` | `expected` (Fraction/int) | `got == expected` |
| `digits` | `expected` (string), `digits` (int) | N-digit string match via `mp.nstr` |
| `range` | `lo`, `hi` | `lo <= got <= hi` |
| `miss_pct` | `expected` (string) | Always INFO — reports miss% |
| `bool` | `expected` (bool) | `got == expected` |

### 11.2 Deferred match modes

These were specified in v0.1 but not yet needed:
- `rank_first` — asserted value ranks #1 in a list
- `scaling` — power law relationship
- `identity` — mathematical identity to working precision

### 11.3 Comparison result format

```json
{
    "label": "Pure gauge gap = 2",
    "output_key": "gap_pure_gauge_ratio_derived_v0",
    "match_mode": "exact",
    "status": "PASS",
    "detail": "exact match",
    "reference_source": "group_theory"
}
```

Status values: `PASS`, `FAIL`, `INFO`, `SKIP`.

---

## 12. Diagram System

### 12.1 Architecture

Diagrams are specified declaratively in experiment JSON under the `diagrams` key. The runner lists them but does not render them. The diagram generator `data_6_diagrams.py` reads the specs and produces PNGs.

```
python data_6_diagrams.py beta_unification_v0
```

### 12.2 Diagram library

`data_6_diagram_lib.py` provides all rendering primitives. No dependency on `phys24_lib`. All values converted internally via `to_float()`. Dark background theme with HOWL color palette.

Key helpers: `dark_fig`, `dark_canvas`, `save_fig`, `bar_chart`, `curve`, `running_curves`, `measurement_band`, `threshold_line`, `data_point`, `measured_diamond`, `result_box`, `note`, `arrow_label`, `legend`, `concentric_shells`, `one_loop_run`.

### 12.3 Renderer types

**`bar`** — Categorical bar chart. Reads `categories` and `values_from` (list of output keys). Looks up values in result outputs, converts to float, plots bars. Annotates miss% relative to last bar (assumed measured).

**`comparison_table`** — Horizontal paired bars (predicted vs measured). Reads `rows`, each with `label`, `predicted` (output key), `measured` (string value). Computes and annotates miss% on each row.

**`line`** — General line chart or coupling running. If `source_derivation` contains "coupling" or title contains "running", dispatches to the coupling running renderer which pulls couplings and betas from the value pool and recomputes curves via `one_loop_run`.

### 12.4 Coupling running renderer

Special-cased because the derivation stores only final alpha_s values, not the full curve data. The renderer pulls `coupling_alpha_1_inverse_gut_normalized_mz_v0`, `coupling_alpha_2_inverse_mz_v0`, `coupling_alpha_3_inverse_mz_v0` and both SM and modified betas from the value pool. Plots SM running as dashed, CD running as solid with threshold at M_VL = 3 TeV. Marks M_Z, M_VL, M_GUT as vertical landmarks.

### 12.5 Color conventions

Gauge groups: Blue = U(1), Green = SU(2), Red = SU(3). All colors from the library palette. Never redefined by renderers.

### 12.6 Output

PNGs saved to CWD with filenames from the diagram `key` field. Provenance logged for every value consumed.

---

## 13. Correction Cycle

### 13.1 Correcting a constant

1. Register `canonical_key_v1` with corrected value and `supersedes` field
2. Add pitfall entry documenting the error
3. Create new dataset version overriding to v1
4. Re-run affected experiments
5. Old value, old results remain

### 13.2 Correcting a derivation

1. Write `derivation_name_v1` with corrected logic
2. Register with pitfall documentation
3. Update experiments to reference v1
4. Re-run and compare

### 13.3 Kill switch triggers

Experiment result triggers kill condition on associated program. Program status changes to `KILLED`. Kill switch record updated. Program node preserved with falsification evidence.

---

## 14. Storage and File Organization

### 14.1 Actual layout

All files in one flat directory:

```
values_si_exact_v0.json
values_measured_v0.json
values_electroweak_v0.json
values_quarks_ckm_v0.json
values_nuclear_spectro_v0.json
values_q335_v0.json
values_ratios_koide_v0.json
values_gut_beta_v0.json
values_integer_pool_v0.json
values_generation_democracy_v0.json
values_gap_ratios_v0.json
values_two_loop_vl_dbij_v0.json
values_rep_aliases_v0.json
values_beta_aliases_v0.json
values_higgs_beta_v0.json
values_representations_v0.json
values_engineering_v0.json
values_astrophysical_v0.json
values_cosmological_v0.json
values_observational_v0.json
connections_v0.json
connections_papers_v0.json
programs_v0.json
experiment_beta_unification_v0.json
result_experiment_beta_unification_v0.json
_data_6_derivations_v0.py
_data_6_super_test_v0.py
data_6_run.py
data_6_diagrams.py
data_6_diagram_lib.py
data_6_export_json.py
```

### 14.2 What lives in JSON

Value nodes, experiment nodes, result nodes, program nodes, connection metadata.

### 14.3 What lives in Python

Derivation callables, connection callables, runner, diagram generator, diagram library, exporter, test.

### 14.4 Future organization

The flat layout works at current scale (357 nodes, 20 files). When it grows, organize into subdirectories: `values/`, `experiments/`, `results/`, `derivations/`, `connections/`, `programs/`.

---

## 15. Registry

### 15.1 Derivation registry

```python
DERIVATION_INDEX_V0 = {
    "coupling_extraction_v0": coupling_extraction_v0,
    "gap_measured_ratio_v0": gap_measured_ratio_v0,
    "gap_sm_ratio_v0": gap_sm_ratio_v0,
    "gauge_pure_gap_v0": gauge_pure_gap_v0,
    "beta_sm_coefficients_v0": beta_sm_coefficients_v0,
    "beta_cabibbo_doublet_shifts_v0": beta_cabibbo_doublet_shifts_v0,
    "beta_modified_and_cd_gap_ratio_v0": beta_modified_and_cd_gap_ratio_v0,
    "generation_democracy_v0": generation_democracy_v0,
    "beta_double_action_mechanism_v0": beta_double_action_mechanism_v0,
    "beta_y_dependence_family_v0": beta_y_dependence_family_v0,
    "crossing_one_loop_scale_v0": crossing_one_loop_scale_v0,
    "coupling_one_loop_alpha_s_prediction_v0": coupling_one_loop_alpha_s_prediction_v0,
    "coupling_two_loop_alpha_s_euler_v0": coupling_two_loop_alpha_s_euler_v0,
    "koide_ratio_v0": koide_ratio_v0,
    "koide_tau_prediction_v0": koide_tau_prediction_v0,
    "cosmo_dm_baryon_ratio_v0": cosmo_dm_baryon_ratio_v0,
    "cosmo_omega_dm_v0": cosmo_omega_dm_v0,
    "cosmo_amplification_factor_decomposition_v0": cosmo_amplification_factor_decomposition_v0,
}
```

### 15.2 Connection registry

```python
CONNECTION_INDEX_V0 = {
    "connection_coupling_convergence_v0": connection_coupling_convergence_v0,
    "connection_gap_correction_chain_v0": connection_gap_correction_chain_v0,
    "connection_integer_network_v0": connection_integer_network_v0,
    "connection_three_programs_shared_set_v0": connection_three_programs_shared_set_v0,
    "connection_object_adjacency_v0": connection_object_adjacency_v0,
}
```

---

## 16. Migration Status

### 16.1 Completed

- 146 constants from `phys24_lib.py` exported to JSON value nodes
- 18 derivation functions migrated to `_data_6_derivations_v0.py`
- 5 connection functions migrated to `_data_6_derivations_v0.py`
- All representations from `phys24_structure_lib.py` exported
- All engineering data from `phys24_domain_lib.py` exported
- All observational data (dwarf galaxies, H0 measurements) exported
- All boundaries, forces, closed paths, anomalies exported as connection nodes
- 3 research programs exported
- Paper cross-references exported
- Integer pool values exported
- Generation democracy sums exported
- Gap ratios exported
- Higgs beta shifts exported
- Two-loop VL db_ij matrix exported

### 16.2 Key aliases

Some values exist under two keys due to naming differences between the exporter and the derivation registry:

| Exporter key | Derivation expects |
|---|---|
| `beta_cabibbo_doublet_u1_shift_v0` | `beta_cabibbo_doublet_vectorlike_u1_shift_v0` |
| `beta_cabibbo_doublet_su2_shift_v0` | `beta_cabibbo_doublet_vectorlike_su2_shift_v0` |
| `beta_cabibbo_doublet_su3_shift_v0` | `beta_cabibbo_doublet_vectorlike_su3_shift_v0` |
| `rep_cd_su3_dim_v0` | `rep_cabibbo_doublet_su3_dim_v0` |
| `rep_cd_su2_dim_v0` | `rep_cabibbo_doublet_su2_dim_v0` |
| `rep_cd_hypercharge_v0` | `rep_cabibbo_doublet_y_v0` |

Both forms are currently exported via alias files (`values_beta_aliases_v0.json`, `values_rep_aliases_v0.json`). Should be consolidated in v1 — pick one canonical name and update all references.

### 16.3 Not yet migrated

- ~60 domain/boundary/gravity/experiment helper functions from DATA-5 chunks
- Experiment definitions for soliton gravity and dwarf soliton experiments
- Diagram renderers as formal derivation nodes
- Self-test migration to formal experiment nodes (148 checks from `phys24_lib_test.py`)

---

## 17. Known Issues and Debt

### 17.1 Two-loop alpha_s predictions

The two-loop Euler integration produces alpha_s values with 10-12% miss against measured 0.1180, compared to the expected <1% miss from the DATA-5 platform. The VL db_ij matrix values in `values_two_loop_vl_dbij_v0.json` need investigation against the platform library. The one-loop prediction (8.74% miss) is correct.

### 17.2 Missing initial exports

The initial JSON export missed several value categories that the derivation functions required. These were added as supplemental files: `values_integer_pool_v0.json`, `values_generation_democracy_v0.json`, `values_gap_ratios_v0.json`, `values_two_loop_vl_dbij_v0.json`, `values_rep_aliases_v0.json`, `values_beta_aliases_v0.json`, `values_higgs_beta_v0.json`. A clean v1 export should consolidate these into fewer files.

### 17.3 No version pinning

The runner ignores dependency version declarations in the experiment JSON. It loads all v0 values. This is adequate for single-version operation but must be implemented for multi-version experiments and dataset support.

### 17.4 Diagram renderer limitations

The coupling running renderer hardcodes M_VL = 3 TeV. This should come from the value pool (`cd_mass_lower_bound_v0` or similar). The comparison table renderer does not handle values with very different scales well — all bars on the same axis.

### 17.5 Scientific notation guard

The `_normalize_decimal()` function in the exporter converts scientific notation strings to plain decimal. This is a safety net, not a substitute for writing correct values in the first place. All approximate values should be authored as plain decimals.

---

## 18. Open Design Decisions

1. **Dataset chaining depth** — No limit currently. Add limit when datasets are implemented.
2. **JSON Schema validation** — Python-side validation only. JSON Schema as a hardening step later.
3. **Search indexing** — Linear scan. Index when scale demands it.
4. **Version pinning enforcement** — Runner should validate dependency versions before execution.
5. **Key alias consolidation** — Pick canonical names, update all references, remove alias files.
6. **Two-loop db_ij investigation** — Compare exported matrix values against platform library originals.
7. **Diagram as standalone node type** — Currently embedded in experiment JSON. May warrant its own node type and JSON files when diagram count grows.
8. **Automatic DAG resolution** — Manual execution order for now. Topological sort from declared inputs/outputs is a future enhancement.
9. **Result versioning** — Current format: `result_experiment_{name}_v0.json`. Run counter or timestamp hash for re-runs not yet decided.

---

## 19. Summary

DATA-6 is operational. The system implements:

- 8 node types covering the full research cycle
- 357 value nodes across 20 JSON files
- 18 derivation functions and 5 connection functions in a single Python registry
- a generic CLI experiment runner that reads experiment JSON and writes result JSON
- a diagram generator that reads diagram specs from experiment JSON and produces PNGs
- integer fraction arithmetic throughout, with mpf only at the irrational boundary
- no hardcoded physics constants in any executable code
- formal comparison contracts with 5 match modes
- full provenance from every output back to its source values

All exact arithmetic checks pass. All derivations execute. All connections resolve. The two-loop numerical predictions have a known accuracy issue under investigation. The architecture supports versioned corrections, dataset overlays, and experiment chaining — these features are specified but not yet implemented in the runner.

---

*End of data_6_tech_spec_v0.2.md. This spec describes a working system.*

---

## Appendix A: Value Node Inventory

| JSON File | Section | Count | Level | Value Types |
|---|---|---|---|---|
| values_si_exact_v0.json | SI defined constants | 7 | 0 | exact_fraction |
| values_measured_v0.json | CODATA 2022 | 13 | 2 | exact_fraction |
| values_electroweak_v0.json | LEP/PDG | 6 | 2 | exact_fraction |
| values_quarks_ckm_v0.json | PDG 2024 / FLAG | 11 | 2 | exact_fraction |
| values_nuclear_spectro_v0.json | Nuclear / spectroscopy | 9 | 2 | exact_fraction |
| values_q335_v0.json | Q335 analytical basis | 31 | 0 | exact_fraction |
| values_ratios_koide_v0.json | Mass ratios / Koide | 11 | 2 | mixed |
| values_gut_beta_v0.json | SM/CD betas, gaps, couplings | 32 | 1-2 | exact_fraction |
| values_integer_pool_v0.json | Integer pool | 10 | 1 | exact_integer |
| values_generation_democracy_v0.json | Per-gen beta sums | 3 | 1 | exact_fraction |
| values_gap_ratios_v0.json | Gap ratios, cosmo prefactors | 7 | 1-2 | exact_fraction |
| values_two_loop_vl_dbij_v0.json | Two-loop VL matrix | 9 | 1 | exact_fraction |
| values_rep_aliases_v0.json | CD representation aliases | 7 | 1 | mixed |
| values_beta_aliases_v0.json | CD beta shift aliases | 3 | 1 | exact_fraction |
| values_higgs_beta_v0.json | Higgs beta shifts | 3 | 1 | exact_fraction |
| values_representations_v0.json | SM + CD representations | 54 | 1 | mixed |
| values_engineering_v0.json | Engineering / domain data | 66 | 0-2 | mixed |
| values_astrophysical_v0.json | Astrophysical constants | 12 | 2 | approximate |
| values_cosmological_v0.json | H0 measurements, Planck | 11 | 2 | approximate |
| values_observational_v0.json | Dwarf galaxies | 52 | 2 | approximate |
| **TOTAL** | | **357** | | |

---

## Appendix B: Derivation Registry

| Key | Inputs | Outputs | Arithmetic | Description |
|---|---|---|---|---|
| coupling_extraction_v0 | alpha_inv, sin2_tW, alpha_s | alpha_em, cos2_tW, inv_a1, inv_a2, inv_a3 | exact | Extract GUT-normalized couplings at M_Z |
| gap_measured_ratio_v0 | inv_a1, inv_a2, inv_a3 | numerator, denominator, ratio, numeric | exact | Measured gap ratio from inverse couplings |
| gap_sm_ratio_v0 | b1_SM, b2_SM, b3_SM | numerator, denominator, ratio, numeric | exact | SM gap ratio from beta coefficients |
| gauge_pure_gap_v0 | c2_su2, c2_su3 | numerator, denominator, ratio, casimir_form | exact | Pure gauge gap from adjoint Casimirs |
| beta_sm_coefficients_v0 | c2_su2, c2_su3, n_gen, gen_db sums, higgs_db | gauge, fermion, total for U(1)/SU(2)/SU(3) | exact | Derive SM betas from group theory |
| beta_cabibbo_doublet_shifts_v0 | d3, d2, Y, s2_fund | db1, db2, db3 | exact | VL one-loop beta shifts from CD rep |
| beta_modified_and_cd_gap_ratio_v0 | SM betas, CD shifts | modified betas, CD gap ratio | exact | SM + CD modified betas and gap |
| generation_democracy_v0 | gen_db1, gen_db2, gen_db3 | gap_num, gap_den, independent_bool | exact | Verify per-gen shifts are equal |
| beta_double_action_mechanism_v0 | CD shifts, SM gap num/den | deltas, change%, asymmetry | mixed | Analyze CD double action on gap |
| beta_y_dependence_family_v0 | Y | coefficients, formula, gap at Y | exact | Gap ratio as function of hypercharge |
| crossing_one_loop_scale_v0 | inv_a1, inv_a2, b1_mod, b2_mod, M_Z | L_GUT, log10_M_GUT | mixed | One-loop GUT crossing scale |
| coupling_one_loop_alpha_s_prediction_v0 | inv_a1, inv_a2, modified betas, alpha_s | alpha_s predicted, miss% | mixed | One-loop alpha_s from CD unification |
| coupling_two_loop_alpha_s_euler_v0 | inv couplings, modified betas, SM bij, VL dbij, alpha_s | alpha_s SM/full, miss%, L_GUT, inv_gut | numeric | Two-loop Euler integration with binary search |
| koide_ratio_v0 | m_e, m_mu, m_tau | K, a^2, a^2-2 | mixed | Koide ratio from lepton masses |
| koide_tau_prediction_v0 | m_e, m_mu | m_tau predicted | mixed | Predict m_tau assuming K = 2/3 |
| cosmo_dm_baryon_ratio_v0 | 2*YM, |b2_mod_num| | prefactor, predicted | mixed | DM/baryon from beta integers |
| cosmo_omega_dm_v0 | 4*YM, |b2_mod_num|^2 | prefactor, predicted | mixed | Omega_DM from beta integers and R2 |
| cosmo_amplification_factor_decomposition_v0 | 4*YM, |b2_mod_num| | reduced factor, formula | exact | DM amplification factor decomposition |

---

## Appendix C: Connection Registry

| Key | Type | Named Values | Edges | Description |
|---|---|---|---|---|
| connection_coupling_convergence_v0 | convergence | inv_a1, inv_a2, inv_a3, b1_mod, b2_mod, b3_mod, gap_measured, gap_cd | 7 | Coupling convergence analysis |
| connection_gap_correction_chain_v0 | correction_chain | gap_pure, gap_sm, gap_cd, gap_measured | 3 | Gap ratio correction: pure gauge → SM → CD → measured |
| connection_integer_network_v0 | traceability | ym_11, b2_abs_13, four_ym, dm_prefactor, omega_prefactor, gap_cd | 5 | Integer traceability: 11, 13, 44, 169 |
| connection_three_programs_shared_set_v0 | shared_set | ym_11, b2_abs_13, r2, b2_sm_19, gap_num_38, gap_den_27 | 5 | Shared integer set across three programs |
| connection_object_adjacency_v0 | adjacency | alpha_inv, sin2_tW, alpha_s, b2_mod, ym_11, r2, koide_k | 5 | First-pass object adjacency map |

---

## Appendix D: Experiment Comparison Results

From `experiment_beta_unification_v0`, run date 2026-04-05.

### D.1 Exact checks (all PASS)

| Label | Output key | Expected | Status |
|---|---|---|---|
| Pure gauge gap = 2 | gap_pure_gauge_ratio_derived_v0 | 2/1 | PASS |
| SM gap = 218/115 | gap_sm_ratio_derived_v0 | 218/115 | PASS |
| CD gap = 38/27 | gap_sm_cabibbo_doublet_ratio_derived_v0 | 38/27 | PASS |
| Casimir form = 2 | gap_pure_gauge_casimir_form_v0 | 2/1 | PASS |
| Generation democracy | generation_democracy_independent_of_n_gen_v0 | true | PASS |
| b1_SM = 41/10 | beta_sm_u1_total_derived_v0 | 41/10 | PASS |
| b2_SM = -19/6 | beta_sm_su2_total_derived_v0 | -19/6 | PASS |
| b3_SM = -7 | beta_sm_su3_total_derived_v0 | -7/1 | PASS |
| b1_mod = 25/6 | beta_modified_u1_total_derived_v0 | 25/6 | PASS |
| b2_mod = -13/6 | beta_modified_su2_total_derived_v0 | -13/6 | PASS |
| b3_mod = -20/3 | beta_modified_su3_total_derived_v0 | -20/3 | PASS |
| CD db1 = 1/15 | beta_cabibbo_doublet_vectorlike_u1_shift_derived_v0 | 1/15 | PASS |
| CD db2 = 1 | beta_cabibbo_doublet_vectorlike_su2_shift_derived_v0 | 1/1 | PASS |
| CD db3 = 1/3 | beta_cabibbo_doublet_vectorlike_su3_shift_derived_v0 | 1/3 | PASS |
| Y-dep gap at Y=1/6 | beta_y_dependence_gap_at_input_y_v0 | 38/27 | PASS |
| DM prefactor = 22/13 | cosmo_dm_to_baryon_ratio_prefactor_derived_v0 | 22/13 | PASS |
| Omega_DM prefactor = 44/169 | cosmo_omega_dm_r2_prefactor_derived_v0 | 44/169 | PASS |
| Amplification = 44/13 | cosmo_amplification_reduced_factor_v0 | 44/13 | PASS |

### D.2 Digit and range checks

| Label | Output key | Mode | Got | Status |
|---|---|---|---|---|
| Measured gap ratio | gap_measured_ratio_numeric_v0 | 4 digits | 1.35819 | PASS |
| Koide K | koide_charged_leptons_k_derived_v0 | 9 digits | 0.666660511 | PASS |
| log10(M_GUT/GeV) | result_m_gut_one_loop_..._v0 | range [15,16] | 15.5426 | PASS |
| L_GUT | result_l_gut_one_loop_..._v0 | range [4,6] | 4.97761 | PASS |

### D.3 Prediction miss% (INFO)

| Label | Predicted | Measured | Miss% |
|---|---|---|---|
| alpha_s one-loop | 0.10768641 | 0.1180 | 8.74% |
| alpha_s two-loop SM bij | 0.12995016 | 0.1180 | 10.13% |
| alpha_s two-loop full bij | 0.13207943 | 0.1180 | 11.93% |
| Koide a^2 vs 2 | 1.9999631 | 2.0 | 0.001847% |
| Koide m_tau vs measured | 1776.969 | 1776.86 | 0.006136% |
| DM/baryon vs Planck | 5.3165414 | 5.3204 | 0.07252% |
| Omega_DM vs Planck | 0.20448236 | 0.2607 | 21.56% |

### D.4 Summary

| Category | Count |
|---|---|
| PASS | 22 |
| FAIL | 0 |
| INFO | 7 |
| SKIP | 0 |
| Total | 29 |

---

## Appendix E: Key Alias Map

Values exported under two keys for derivation compatibility. To be consolidated in v1.

| Alias file | Exporter key | Derivation key | Value |
|---|---|---|---|
| values_beta_aliases_v0.json | beta_cabibbo_doublet_u1_shift_v0 | beta_cabibbo_doublet_vectorlike_u1_shift_v0 | 1/15 |
| values_beta_aliases_v0.json | beta_cabibbo_doublet_su2_shift_v0 | beta_cabibbo_doublet_vectorlike_su2_shift_v0 | 1 |
| values_beta_aliases_v0.json | beta_cabibbo_doublet_su3_shift_v0 | beta_cabibbo_doublet_vectorlike_su3_shift_v0 | 1/3 |
| values_rep_aliases_v0.json | rep_cd_su3_dim_v0 | rep_cabibbo_doublet_su3_dim_v0 | 3 |
| values_rep_aliases_v0.json | rep_cd_su2_dim_v0 | rep_cabibbo_doublet_su2_dim_v0 | 2 |
| values_rep_aliases_v0.json | rep_cd_hypercharge_v0 | rep_cabibbo_doublet_y_v0 | 1/6 |
| values_rep_aliases_v0.json | rep_cd_type_v0 | rep_cabibbo_doublet_type_v0 | vector_like |
| values_rep_aliases_v0.json | rep_cd_db1_v0 | rep_cabibbo_doublet_db1_v0 | 1/15 |
| values_rep_aliases_v0.json | rep_cd_db2_v0 | rep_cabibbo_doublet_db2_v0 | 1 |
| values_rep_aliases_v0.json | rep_cd_db3_v0 | rep_cabibbo_doublet_db3_v0 | 1/3 |

---

## Appendix F: Diagram Specifications

From `experiment_beta_unification_v0`.

| Key | Type | Title | Data sources |
|---|---|---|---|
| diagram_coupling_running_v0 | line | Gauge coupling running with Cabibbo Doublet | inv_a1/a2/a3, SM betas, modified betas, L_GUT |
| diagram_gap_correction_bar_v0 | bar | Gap ratio correction chain | gap_pure_gauge, gap_sm, gap_cd, gap_measured |
| diagram_cosmological_predictions_v0 | comparison_table | Cosmological predictions from beta integers | DM/baryon, Omega_DM, alpha_s (1L/2L), m_tau Koide |

---

## Appendix G: Integer Pool Traceability

Every integer in the pool traces back to gauge theory coefficients.

| Key | Value | Source | Appears in |
|---|---|---|---|
| integer_yang_mills_eleven_v0 | 11 | -(11/3)*C2(adj) gauge coefficient | DM formula numerator, boundary count |
| integer_b2_modified_numerator_abs_v0 | 13 | |numerator of b2_mod = -13/6| | DM denominator, gap denominator, Omega denominator |
| integer_b2_sm_numerator_abs_v0 | 19 | |numerator of b2_SM = -19/6| | SM gap numerator doubles to 38 |
| integer_b3_modified_times_three_abs_v0 | 20 | |3 * b3_mod| = |3 * -20/3| | Modified SU(3) structure |
| integer_two_times_yang_mills_v0 | 22 | 2 * 11 | DM/baryon prefactor numerator: (22/13)*pi |
| integer_cabibbo_doublet_gap_numerator_v0 | 38 | 2 * 19 | CD gap ratio numerator: 38/27 |
| integer_cabibbo_doublet_gap_denominator_v0 | 27 | denominator of 38/27 | CD gap ratio denominator |
| integer_four_times_yang_mills_v0 | 44 | 4 * 11 | Omega_DM prefactor numerator: (44/169)*R2, amplification: (44/13)*pi*(c/v)^2 |
| integer_b2_modified_numerator_square_v0 | 169 | 13^2 | Omega_DM prefactor denominator: 44/169 |
| integer_sm_gap_numerator_v0 | 218 | numerator of 218/115 | SM gap ratio |

---

## Appendix H: Connection Node Inventory

From `connections_v0.json` and `connections_papers_v0.json`.

| Category | Count | Source |
|---|---|---|
| R2 universal equations | 22 | phys24_domain_lib.py |
| R2 cancellations | 7 | phys24_domain_lib.py |
| Boundary stack | 19 | phys24_boundary_map_lib.py |
| Forces | 5 | phys24_boundary_map_lib.py |
| Closed paths (KILLED) | 7 | phys24_structure_lib.py |
| Anomaly evidence | 3 | phys24_structure_lib.py |
| Paper cross-references | 29 | phys24_structure_lib.py |
| **Total** | **92** | |

---

## Appendix I: Q335 Analytical Constants

All stored as exact `Fraction` values with 100+ digit precision. Numerators serialized as strings in JSON to avoid integer limits.

| Key | Identity | Digits |
|---|---|---|
| geom_pi_v0 | pi | 100 |
| geom_e_euler_v0 | e | 100 |
| geom_ln2_v0 | ln(2) | 100 |
| geom_sqrt2_v0 | sqrt(2) | 100 |
| geom_sqrt3_v0 | sqrt(3) | 100 |
| geom_sqrt5_v0 | sqrt(5) | 100 |
| geom_sqrt7_v0 | sqrt(7) | 100 |
| geom_golden_ratio_v0 | (1+sqrt(5))/2 | 100 |
| geom_zeta3_v0 | zeta(3) | 100 |
| geom_zeta5_v0 | zeta(5) | 100 |
| geom_pi_squared_v0 | pi^2 | 100 |
| geom_zeta2_v0 | pi^2/6 | 100 |
| geom_r2_v0 | pi/4 | 100 |
| geom_r4_v0 | pi^2/32 | 100 |
| geom_two_pi_v0 | 2*pi | 100 |
| geom_zeta7_v0 | zeta(7) | 100 |
| geom_zeta9_v0 | zeta(9) | 100 |
| geom_li4_half_v0 | Li4(1/2) | 100 |
| geom_li5_half_v0 | Li5(1/2) | 100 |
| geom_li6_half_v0 | Li6(1/2) | 100 |
| geom_li7_half_v0 | Li7(1/2) | 100 |
| geom_catalan_v0 | Catalan's constant | 100 |
| geom_e_to_pi_v0 | e^pi | 100 |
| geom_ln3_v0 | ln(3) | 100 |
| geom_ln5_v0 | ln(5) | 100 |
| geom_elliptic_k_quarter_v0 | K(k^2=1/4) | 100 |
| geom_elliptic_k_half_v0 | K(k^2=1/2) | 100 |
| geom_elliptic_k_threequarter_v0 | K(k^2=3/4) | 100 |
| geom_elliptic_e_quarter_v0 | E(k^2=1/4) | 100 |
| geom_elliptic_e_half_v0 | E(k^2=1/2) | 100 |
| geom_elliptic_e_threequarter_v0 | E(k^2=3/4) | 100 |

---

*End of appendices. 9 tables covering the complete DATA-6 system inventory.*
