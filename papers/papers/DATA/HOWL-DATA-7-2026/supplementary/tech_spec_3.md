# DATA-6 Technical Specification

## Universal Versioned Node Physics System

Document: `data_6_tech_spec_v0.3.md`
Version: 0.3
Date: 2026-04-05
Status: Integrated — reflects implemented system, CLI, and v0.3 improvement plan

---

## 1. Purpose and Scope

DATA-6 is a dynamic node-based system for physics research built on integer fraction arithmetic. Every entity — constant, derivation, connection, experiment, result, program, dataset — is a versioned node with a canonical key, a shared metadata envelope, and full provenance.

The system is implemented and operational. A single CLI entry point `data6.py` provides access to all operations: running experiments, generating diagrams, validating data, compiling views, searching nodes, and inspecting values.

Current state: 357 value nodes across 20 JSON files, 18 derivation functions, 5 connection functions, 1 experiment definition with 29 comparisons and 3 diagram specs, a generic CLI runner, a diagram generator, a schema validator, a manifest indexer, a compiled view generator, and a search/info system. All exact arithmetic checks pass. All derivations execute. All connections resolve.

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

Known pitfalls that should be attached to value nodes:

| Node key | Wrong | Right | Session |
|---|---|---|---|
| coupling_alpha_2_inverse_mz_v0 | alpha_inv / sin2_tW = 593 | sin2_tW * alpha_inv = 31.7 | PHYS-30 |
| beta_modified_u1_total_v0 | 62/15 | 25/6 (same value, cleaner form) | DATA-5 |
| beta_two_loop_sm_bij_su2_su2_v0 | 39/4 (gauge double-count) | 15/4 (fermion only) | PHYS-33 |
| mass_w_boson_v0 | 80379 MeV | 80369.2 MeV (803692/10) | DATA-4 |

---

## 4. Node Types

The system has 8 node types.

### 4.1 Value

An atomic named fact.

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
- `approximate`: value is a string containing a plain decimal number. No scientific notation — `"0.0000021969811"` not `"2.1969811e-6"`. The exporter runs `_normalize_decimal()` on all string values.
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
| `correction_chain` | Sequential corrections |
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

Result outputs become values. A consumer requesting `result_alpha_s_two_loop_full_bij` gets the value from the result with full provenance.

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

The root dataset `howl_v0` is implicit — all `_v0` values. Not yet implemented in the runner. Future: `python data6.py run beta_unification_v0 --dataset alpha_s_high_v0` for what-if experiments.

### 4.8 Diagram

A diagram specification embedded in an experiment's `diagrams` list.

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes | Unique key, used as PNG filename |
| `title` | string | yes | Figure title |
| `type` | string | yes | Renderer type |
| `notes` | string | no | Caption or annotation text |

Renderer types:

| Type | Additional fields | What it renders |
|---|---|---|
| `bar` | `categories`, `values_from` | Categorical bar chart with miss% |
| `comparison_table` | `rows` (each with `label`, `predicted`, `measured`) | Horizontal paired bars with miss% |
| `line` | `series`, `source_derivation`, `x_axis`, `y_axis` | Line chart or coupling running curves |

---

## 5. CLI Interface

### 5.1 Entry point

All operations go through `data6.py`:

```
python data6.py <command> [args]
```

### 5.2 Commands

| Command | Arguments | Description |
|---|---|---|
| `run` | `<experiment>` | Execute experiment, write result JSON |
| `diagram` | `<experiment>` | Generate PNGs from diagram specs |
| `test` | | Run super test (all values + derivations) |
| `validate` | | Check all JSON against node schema |
| `index` | | Rebuild manifest from all JSON files |
| `compile` | | Produce single compiled JSON |
| `list` | `values\|derivations\|connections\|experiments\|results` | List nodes by type |
| `search` | `<query>` | Substring search across all nodes |
| `export` | | Re-run JSON exporter |
| `info` | `<key>` | Print full details for one node |

### 5.3 Command details

**`run`** — Loads experiment JSON, loads all value JSON files, executes derivation plan in order, runs connections, evaluates comparisons, writes result JSON to CWD. Delegates to `data_6_run.py`.

**`diagram`** — Reads experiment JSON for diagram specs, reads result JSON for computed outputs, dispatches to renderers by type, writes PNGs to CWD. Delegates to `data_6_diagrams.py`.

**`test`** — Executes `_data_6_super_test_v0.py`. Loads all values, runs all derivations and connections, checks outputs against expected values. Reports PASS/FAIL/SKIP.

**`validate`** — Checks every node in every JSON file against the required schema fields. Value nodes require: key, canonical, version, node_type, value, value_type, unit, level, source. Other nodes require the envelope fields. Reports warnings per node.

**`index`** — Scans all JSON files, classifies each by type, counts nodes, writes `data_6_manifest.json` with filenames, types, node counts, and sizes.

**`compile`** — Produces `data_6_compiled.json` containing all value nodes organized by section, all connection metadata, all programs, all experiments, all results, and derivation/connection registry keys. Single-file ingest for LLM sessions.

**`list`** — Lists nodes by type. Values show key and value. Derivations and connections show key and first line of docstring. Experiments show derivation and comparison counts. Results show status and pass/fail/info counts.

**`search`** — Substring search across all node keys, tags, notes, source, section, description, thesis fields. Returns matches with node type and key.

**`export`** — Re-runs `data_6_export_json.py` to regenerate all value JSON files from platform libraries.

**`info`** — Prints full details for one node by key. Accepts key with or without `_v0` suffix. Searches values, connections, programs, and experiments.

---

## 6. Naming and Versioning Rules

### 6.1 Key format

```
{topic}_{term}_v{N}
```

Lowercase, underscore-separated. Topic is a single word. Term is one or more descriptive words.

### 6.2 Topic prefixes

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
| `config` | Numerical configuration parameters |

### 6.3 File naming

| Pattern | Content |
|---|---|
| `values_{section}_v0.json` | Value nodes by section |
| `experiment_{name}_v0.json` | Experiment specification |
| `result_experiment_{name}_v0.json` | Experiment result |
| `connections_{section}_v0.json` | Connection metadata |
| `programs_v0.json` | Research programs |
| `data_6_manifest.json` | File index |
| `data_6_compiled.json` | Compiled single-file view |

### 6.4 Naming conventions

- Spell out `cabibbo_doublet`, never abbreviate to `cd`
- Use `_derived` suffix consistently on all derivation output keys
- Derivation registry input keys ARE the canonical names — the exporter writes those names

### 6.5 Uniqueness and append-only

No two nodes of any type share the same versioned key. Globally unique. Once a versioned key exists, it is never edited. New understanding means `_v1`, `_v2`.

---

## 7. Dataset Versions

### 7.1 Structure

```json
{
    "key": "dataset_howl_v1",
    "base": "dataset_howl_v0",
    "overrides": {"integer_four_times_yang_mills": 1}
}
```

### 7.2 Rules

- Root dataset `howl_v0` includes all `_v0` values by default.
- Overrides are sparse.
- Chains flatten via the resolver.
- Not yet implemented in the runner.

### 7.3 What-if support

With datasets implemented, what-if experiments become:

```json
{
    "key": "dataset_alpha_s_high_v0",
    "base": "dataset_howl_v0",
    "overrides": {"coupling_alpha_s_mz": 1}
}
```

Run: `python data6.py run beta_unification_v0 --dataset alpha_s_high_v0`

Each what-if is a dataset. Each dataset produces a result. Compare results across datasets.

---

## 8. Universal Access Interface

### 8.1 Value access

```python
get(canonical_key, version=None, dataset=None) -> value_entry
```

### 8.2 Value pool semantics

The value pool is a list of value entry dicts. `_value_map(value_dicts)` builds a flat dict — last entry wins. This is the correct behavior for the runner, where derivation outputs must override stored values. The pool only grows within a run (append-only).

### 8.3 CLI access

`data6.py info <key>` provides single-node lookup. `data6.py search <query>` provides substring search across all nodes. `data6.py list values` provides full inventory.

---

## 9. Resolver

### 9.1 Current implementation

The runner loads all `values_*.json` files into a flat list. No version pinning. No dataset resolution. All v0 values enter the pool. Derivation outputs are appended with `source` set to the derivation key.

### 9.2 Future resolver

Will enforce dependency version pins from the experiment JSON. Will support dataset contexts. Will detect missing keys before execution. Will support literal dependencies for what-if experiments.

---

## 10. Runner

### 10.1 Reference implementation

`data_6_run.py`, accessed via `data6.py run <experiment>`.

### 10.2 Execution flow

1. Find `experiment_{name}.json`
2. Load all `values_*.json` into value pool
3. Execute each derivation in `execution_plan` order
4. After each derivation, merge outputs into the pool
5. Execute each connection in `connections` list
6. Check `expected_outputs` are present
7. Evaluate each comparison in `comparisons`
8. List diagram specs (not rendered — use `data6.py diagram`)
9. Write result JSON to CWD
10. Print summary

### 10.3 Derivation chaining

Derivations may depend on outputs from earlier derivations in the same plan. The runner executes in declared order and merges after each step. The experiment author declares valid order.

### 10.4 Result output

Result JSON written to CWD as `result_experiment_{name}_v0.json`. Contains all derivation outputs, comparison results, execution log, and summary counts.

### 10.5 Pre-flight validation (planned)

Before execution, the runner should:
1. Check all values in `dependencies.values` exist in the pool
2. Check all derivation keys in `execution_plan` exist in the registry
3. Check all connection keys exist in the registry
4. Report all missing items before running
5. If a derivation fails, skip downstream derivations that depend on its outputs

---

## 11. Arithmetic Rules

### 11.1 Hierarchy

1. `fractions.Fraction` — preferred for all exact rational values
2. `int` — acceptable, implicitly `Fraction(n, 1)`
3. `mpmath.mpf` — only at irrational/numerical boundaries
4. `str` — for approximate values with no known exact rational form
5. `float` — never used anywhere in the system

### 11.2 Computation rules

- All exact derivations operate on `Fraction`.
- When a derivation needs pi, sqrt, exp, log: convert to `mpf`, compute, store result as approximate string.
- `mp.dps = 100` minimum.
- `math` module never imported.
- Deterministic execution.

### 11.3 Rendering boundary

Fraction to float conversion happens ONLY at display (diagrams) and irrational math. Never in the computation chain. The diagram library's `to_float()` is the single conversion point for rendering.

### 11.4 JSON serialization

Fraction: `{"_type": "Fraction", "num": "22", "den": "13"}` — numerator and denominator as strings for large Q335 values.

mpf: `{"_type": "mpf", "value": "1.6933077261548"}`

Approximate values: plain decimal strings, never scientific notation. The exporter runs `_normalize_decimal()` to enforce this.

---

## 12. Comparison and Verification Contract

### 12.1 Implemented match modes

| Mode | Fields | Pass condition |
|---|---|---|
| `exact` | `expected` (Fraction/int) | `got == expected` |
| `digits` | `expected` (string), `digits` (int) | N-digit string match via `mp.nstr` |
| `range` | `lo`, `hi` | `lo <= got <= hi` |
| `miss_pct` | `expected` (string) | Always INFO — reports miss% |
| `bool` | `expected` (bool) | `got == expected` |

### 12.2 Deferred match modes

- `rank_first` — asserted value ranks #1 in a list
- `scaling` — power law relationship
- `identity` — mathematical identity to working precision (needed for R2 cancellations, Kepler identities, cross-domain verification)

### 12.3 Comparison result format

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

## 13. Diagram System

### 13.1 Architecture

Diagrams are specified in experiment JSON under `diagrams`. The runner lists them but does not render. The diagram generator `data_6_diagrams.py` reads the specs and produces PNGs, accessed via `data6.py diagram <experiment>`.

### 13.2 Diagram library

`data_6_diagram_lib.py` provides all rendering primitives. No dependency on `phys24_lib`. All values converted internally via `to_float()`. Dark background theme with HOWL color palette.

Key helpers: `dark_fig`, `dark_canvas`, `save_fig`, `bar_chart`, `curve`, `running_curves`, `measurement_band`, `threshold_line`, `data_point`, `measured_diamond`, `result_box`, `note`, `arrow_label`, `legend`, `concentric_shells`, `one_loop_run`.

### 13.3 Renderer types

**`bar`** — Reads `categories` and `values_from`. Looks up values in result outputs, plots bars, annotates miss%.

**`comparison_table`** — Reads `rows` with `label`, `predicted`, `measured`. Horizontal paired bars with miss%.

**`line`** — General line chart or coupling running. Detects coupling running from `source_derivation` and recomputes curves from stored couplings and betas.

### 13.4 Color conventions

Gauge groups: Blue = U(1), Green = SU(2), Red = SU(3). All colors from the library palette. Never redefined.

---

## 14. Correction Cycle

### 14.1 Correcting a constant

1. Register `canonical_key_v1` with corrected value and `supersedes` field
2. Add pitfall entry documenting the error
3. Create new dataset version overriding to v1
4. Re-run affected experiments
5. Old value, old results remain

### 14.2 Correcting a derivation

1. Write `derivation_name_v1` with corrected logic
2. Register with pitfall documentation
3. Update experiments to reference v1
4. Re-run and compare

### 14.3 Kill switch triggers

Experiment result triggers kill condition on associated program. Program status changes to `KILLED`. Kill switch record updated. Program node preserved.

---

## 15. Storage and File Organization

### 15.1 Layout

All files in one flat directory. The manifest (`data_6_manifest.json`) serves as the index. No subdirectories needed at current scale.

### 15.2 Current files

**Value JSON (20 files, 357 nodes):**

| File | Count | Content |
|---|---|---|
| values_si_exact_v0.json | 7 | SI defined constants |
| values_measured_v0.json | 13 | CODATA 2022 |
| values_electroweak_v0.json | 6 | LEP/PDG |
| values_quarks_ckm_v0.json | 11 | PDG 2024 / FLAG |
| values_nuclear_spectro_v0.json | 9 | Nuclear / spectroscopy |
| values_q335_v0.json | 31 | Q335 analytical basis |
| values_ratios_koide_v0.json | 11 | Mass ratios / Koide |
| values_gut_beta_v0.json | 32 | SM/CD betas, gaps, couplings |
| values_integer_pool_v0.json | 10 | Integer pool |
| values_generation_democracy_v0.json | 3 | Per-gen beta sums |
| values_gap_ratios_v0.json | 7 | Gap ratios, cosmo prefactors |
| values_two_loop_vl_dbij_v0.json | 9 | Two-loop VL matrix |
| values_rep_aliases_v0.json | 7 | CD representation aliases |
| values_beta_aliases_v0.json | 3 | CD beta shift aliases |
| values_higgs_beta_v0.json | 3 | Higgs beta shifts |
| values_representations_v0.json | 54 | SM + CD representations |
| values_engineering_v0.json | 66 | Engineering / domain |
| values_astrophysical_v0.json | 12 | Astrophysical constants |
| values_cosmological_v0.json | 11 | H0, Planck parameters |
| values_observational_v0.json | 52 | Dwarf galaxies |

**Other JSON:**

| File | Content |
|---|---|
| connections_v0.json | 63 connection nodes |
| connections_papers_v0.json | 29 paper cross-references |
| programs_v0.json | 3 research programs |
| experiment_beta_unification_v0.json | Experiment spec |
| result_experiment_beta_unification_v0.json | Experiment result |
| data_6_manifest.json | File index |
| data_6_compiled.json | Compiled view |

**Python:**

| File | Role |
|---|---|
| data6.py | CLI entry point / router |
| data_6_run.py | Experiment runner |
| data_6_diagrams.py | Diagram generator |
| data_6_diagram_lib.py | Diagram helper library |
| _data_6_derivations_v0.py | 18 derivations + 5 connections |
| _data_6_super_test_v0.py | Super test |
| data_6_export_json.py | JSON exporter |

---

## 16. Registry

### 16.1 Derivation registry (18 functions)

| Key | Arithmetic | Description |
|---|---|---|
| coupling_extraction_v0 | exact | GUT-normalized couplings at M_Z |
| gap_measured_ratio_v0 | exact | Measured gap from inverse couplings |
| gap_sm_ratio_v0 | exact | SM gap from beta coefficients |
| gauge_pure_gap_v0 | exact | Pure gauge gap from Casimirs |
| beta_sm_coefficients_v0 | exact | SM betas from group theory |
| beta_cabibbo_doublet_shifts_v0 | exact | VL one-loop beta shifts |
| beta_modified_and_cd_gap_ratio_v0 | exact | SM + CD modified betas and gap |
| generation_democracy_v0 | exact | Per-gen shifts are equal |
| beta_double_action_mechanism_v0 | mixed | CD double action analysis |
| beta_y_dependence_family_v0 | exact | Gap as function of hypercharge |
| crossing_one_loop_scale_v0 | mixed | One-loop GUT crossing scale |
| coupling_one_loop_alpha_s_prediction_v0 | mixed | One-loop alpha_s prediction |
| coupling_two_loop_alpha_s_euler_v0 | numeric | Two-loop Euler integration |
| koide_ratio_v0 | mixed | Koide ratio from lepton masses |
| koide_tau_prediction_v0 | mixed | Predict m_tau from K = 2/3 |
| cosmo_dm_baryon_ratio_v0 | mixed | DM/baryon from beta integers |
| cosmo_omega_dm_v0 | mixed | Omega_DM from beta integers |
| cosmo_amplification_factor_decomposition_v0 | exact | DM amplification decomposition |

### 16.2 Connection registry (5 functions)

| Key | Type | Edges | Description |
|---|---|---|---|
| connection_coupling_convergence_v0 | convergence | 7 | Coupling convergence analysis |
| connection_gap_correction_chain_v0 | correction_chain | 3 | Pure gauge → SM → CD → measured |
| connection_integer_network_v0 | traceability | 5 | Integer 11, 13, 44, 169 traceability |
| connection_three_programs_shared_set_v0 | shared_set | 5 | Shared integers across programs |
| connection_object_adjacency_v0 | adjacency | 5 | Object adjacency map |

---

## 17. Migration Status

### 17.1 Completed

- 146 constants from `phys24_lib.py`
- 18 derivation functions
- 5 connection functions
- All representations, engineering data, observational data
- All boundaries, forces, closed paths, anomalies
- 3 research programs, paper cross-references
- Integer pool, generation democracy, gap ratios, Higgs betas, two-loop VL matrix

### 17.2 Key aliases (to consolidate)

| Exporter key | Derivation key |
|---|---|
| beta_cabibbo_doublet_u1_shift_v0 | beta_cabibbo_doublet_vectorlike_u1_shift_v0 |
| beta_cabibbo_doublet_su2_shift_v0 | beta_cabibbo_doublet_vectorlike_su2_shift_v0 |
| beta_cabibbo_doublet_su3_shift_v0 | beta_cabibbo_doublet_vectorlike_su3_shift_v0 |
| rep_cd_su3_dim_v0 | rep_cabibbo_doublet_su3_dim_v0 |
| rep_cd_su2_dim_v0 | rep_cabibbo_doublet_su2_dim_v0 |
| rep_cd_hypercharge_v0 | rep_cabibbo_doublet_y_v0 |

Fix: derivation registry keys are canonical. Update exporter. Delete alias files.

### 17.3 Not yet migrated

- ~60 domain/boundary/gravity/experiment helper functions
- Soliton gravity and dwarf soliton experiment definitions
- Self-test migration to formal experiment nodes (148 checks)
- Containment hierarchy as executable connection

---

## 18. Known Issues

### 18.1 Two-loop accuracy

Two-loop Euler integration shows 10-12% miss vs expected <1%. Requires investigation of db_ij matrix values and Euler step count against platform originals.

### 18.2 Hardcoded numerical parameters

The Euler integrator contains step counts and convergence thresholds that should be value nodes:

| Parameter | Current value | Proposed key |
|---|---|---|
| Euler steps | 4000 | config_euler_step_count_v0 |
| Bisection depth | 60 | config_bisection_depth_v0 |
| CD mass estimate | 3000 GeV | config_cd_mass_estimate_gev_v0 |

### 18.3 Connection outputs not in pool

The runner discards connection `named_values` after printing. Should merge into the pool for downstream use.

### 18.4 Result overwriting

Results overwrite on re-run. Should append a run counter: `result_experiment_beta_unification_v0_run001.json`.

---

## 19. Improvement Priorities

| Priority | Item | Category |
|---|---|---|
| 1 | Two-loop investigation | Correctness |
| 2 | Alias consolidation | Trust |
| 3 | Pitfall entries on nodes | Safety |
| 4 | Pre-flight validation | Robustness |
| 5 | Result versioning | Data preservation |
| 6 | Missing experiments (soliton, dwarf) | Coverage |
| 7 | Hardcoded constants to value nodes | Principle compliance |
| 8 | Connection outputs into pool | Capability |
| 9 | Missing value categories (moduli, boundary scales) | Completeness |
| 10 | Schema validation in runner | Robustness |
| 11 | Identity match mode | Capability |
| 12 | Provenance index | Provenance |
| 13 | Dataset support in runner | What-if capability |

---

## 20. Summary

DATA-6 is operational. The system implements:

- 8 node types covering the full research cycle
- 357 value nodes across 20 JSON files
- 18 derivation functions and 5 connection functions
- a CLI entry point with 10 commands (`data6.py`)
- a generic experiment runner reading from experiment JSON
- a diagram generator reading diagram specs and producing PNGs
- a schema validator, manifest indexer, compiled view generator, and search system
- integer fraction arithmetic throughout with mpf only at the irrational boundary
- no hardcoded physics constants in executable code
- formal comparison contracts with 5 match modes
- full provenance from every output back to its source values

All exact arithmetic checks pass. All derivations execute. All connections resolve. The two-loop numerical predictions have a known accuracy issue under investigation. The architecture supports versioned corrections, dataset overlays, and experiment chaining — these features are specified and will be implemented as the system grows.

---

*End of data_6_tech_spec_v0.3.md. This spec describes a working system with a clear improvement path.*

---

## Addendum: Modulus and Remainder Values

### M1. Definition

A modulus value is a structural constant arising from geometric or algebraic remainder operations. These are exact values — typically Fraction — that appear across multiple independent domains. They are first-class data, not derived artifacts.

The canonical example is R2 = pi/4, which is simultaneously a filling fraction, a vena contracta coefficient, a Fourier normalization, and a coupling running remainder. The value is one thing. Its appearances across domains are connections.

### M2. Storage

File: `values_moduli_v0.json`

Topic prefix: `mod`

Level: 0 (pure geometry / exact math)

### M3. Naming

```
mod_{name}_v0
```

Examples:

| Key | Value | Identity | Domains |
|---|---|---|---|
| mod_r2_v0 | pi/4 | Circle-to-square filling fraction | pipes, wires, discs, speakers, fibers, semiconductors, gauge running |
| mod_r4_v0 | pi^2/32 | Second-order remainder | thermal radiation, Gaussian normalization |
| mod_eight_r2_v0 | 2*pi | 8 * R2 | Fourier, angular, Kepler |
| mod_vena_contracta_v0 | pi/(pi+2) | Orifice contraction coefficient | fluid flow |
| mod_bcs_gap_ratio_v0 | pi * e^(-gamma) | BCS weak-coupling gap | superconductivity |
| mod_fourier_circle_v0 | 1/(2*pi) | Fourier normalization | signal processing, quantum mechanics |
| mod_gaussian_peak_v0 | 1/sqrt(2*pi) | Gaussian peak normalization | statistics, quantum |
| mod_airy_first_zero_v0 | 1.22 * lambda/D | Airy resolution limit | optics, lithography |
| mod_boltzmann_fourth_v0 | pi^2/60 | Stefan-Boltzmann integrand | thermal radiation |
| mod_coulomb_sphere_v0 | 1/(4*pi) | Coulomb normalization | electrostatics |

### M4. Relationship to geom_ values

The `geom_` prefix holds the raw mathematical constants (pi, e, sqrt2, zeta values). The `mod_` prefix holds the specific remainder/modulus forms that appear in physics equations. Some overlap:

- `geom_r2_v0` and `mod_r2_v0` are the same value (pi/4)
- `geom_r4_v0` and `mod_r4_v0` are the same value (pi^2/32)

Resolution: `geom_` entries are the Q335 analytical basis — the raw constants at 100-digit precision. `mod_` entries are the physics-facing forms with domain context in their tags and notes. The value is identical. The metadata differs. A `mod_` entry may carry `legacy_refs` pointing to its `geom_` counterpart.

Alternatively, if duplication is unacceptable: keep only `geom_` for the raw constant, and make `mod_` entries reference them via the `ref` field with `value_type: "deferred"`. The resolver fills in the value from the `geom_` entry. This avoids storing the same Fraction twice.

### M5. Connection to R2 domains

Each modulus value that appears in an R2 equation is linked by a connection node with `connection_type: "universal_equation"`. The connection says "this modulus appears in this domain with this coordinator Z." The modulus is the value. The domain appearance is the connection. They are separate nodes.

### M6. Topic prefix table update

Add to Section 6.2:

| Prefix | Scope |
|---|---|
| `mod` | Modulus and remainder values — structural constants from geometric/algebraic remainders |

---

*End of modulus addendum. Moduli are Level 0 exact values with their own section, distinguished from raw geometric constants by physics-facing metadata.*

---

**Gaps between working system and v0.3 spec:**

1. **Alias consolidation** — spec says derivation keys are canonical, exporter writes those names, delete alias files. Not done. Two alias files still exist.

2. **Pitfall entries** — spec lists 4 known pitfalls that should be on value nodes. None are in the exported JSON.

3. **Moduli values** — spec defines `values_moduli_v0.json` with `mod_` prefix. File doesn't exist.

4. **Config value nodes** — spec says Euler step count, bisection depth, CD mass estimate should be value nodes. They're hardcoded in derivation code.

5. **Pre-flight validation in runner** — spec Section 10.5 describes dependency checking before execution. Runner just starts executing.

6. **Result versioning** — spec says append run counter. Runner overwrites `result_experiment_*.json`.

7. **Connection outputs into pool** — spec Section 18.3 says merge `named_values` into pool. Runner discards them.

8. **Dataset support** — spec Sections 4.7 and 7 describe datasets and `--dataset` CLI flag. Not implemented.

9. **Manifest** — spec says `data6.py index` writes `data_6_manifest.json`. Command exists in router but hasn't been run to verify.

10. **Compiled view** — same as above, `data6.py compile` exists but hasn't been verified against spec format.

11. **Missing experiments** — spec says 3 programs need 3 experiments. Only `beta_unification_v0` exists.

12. **Missing derivations** — spec says ~60 helper functions not migrated. Still true.

13. **`mod` prefix** — not in the actual topic prefix table in the exporter or derivation registry.

14. **Identity match mode** — spec lists it as deferred but needed. Not implemented.

15. **Provenance index** — spec describes post-run provenance JSON. Runner doesn't write it.

16. **Validate command** — exists in router but hasn't been tested against actual JSON files to confirm all nodes pass.

Items 1-3 are data fixes. Items 4-8 are code changes. Items 9-10 need verification. Items 11-15 are future work.

---

## Addendum: Output Version Resolution

### V1. Principle

When a derivation produces an output, the runner checks whether that canonical key already exists in the registry. The output is not blindly appended. The version is determined by comparison.

### V2. Rules

| Condition | Action | Result key |
|---|---|---|
| Key does not exist in registry | Register as v0 | `output_key_v0` |
| Key exists, value is identical | Reuse existing version | `output_key_v0` (no new node) |
| Key exists, value differs | Register as next version | `output_key_v1` with `supersedes: "output_key_v0"` |

### V3. Identity comparison

"Identical" means:
- For `Fraction`: numerator and denominator are equal
- For `int`: integer equality
- For `str` (approximate): string equality of the plain decimal representation
- For `bool`: boolean equality

No tolerance. No rounding. If two Fraction values are mathematically equal but stored in different reduced forms, `Fraction` handles normalization automatically.

### V4. Version bumping

When a new version is created:
- The new node carries `supersedes: "output_key_vN"` pointing to the version it replaces
- The new node carries a pitfall entry if the change was a correction, or a notes entry if the change was from updated inputs
- The old version remains in the registry — never deleted
- The result JSON records `"output_key": {"version": 1, "previous_version": 0, "changed": true}`

When the value is unchanged:
- No new node is created
- The result JSON records `"output_key": {"version": 0, "changed": false}`

### V5. Result output manifest

The result JSON gains a new field `output_versions`:

```json
{
    "output_versions": {
        "coupling_alpha_em_v0": {"version": 0, "changed": false},
        "gap_pure_gauge_ratio_derived_v0": {"version": 0, "changed": false},
        "result_alpha_s_two_loop_full_bij_v1": {"version": 1, "changed": true, "previous": 0}
    }
}
```

This is the provenance record showing exactly what changed and what didn't in each run.

### V6. Runner implementation

After each derivation executes:

```
for each output_key, output_value in derivation.outputs:
    existing = registry.find(canonical_key)
    if existing is None:
        register as v0
    elif existing.value == output_value:
        record unchanged, reuse version
    else:
        register as v(existing.version + 1) with supersedes
        record changed
    append to working pool
```

### V7. Interaction with datasets

When a dataset override pins a value to a specific version, and a derivation produces a different value for the same key, the derivation output takes precedence within the experiment run but does NOT override the dataset pin in the registry. The new version is registered alongside the pinned version. The result records both the dataset-pinned version and the derivation-produced version.

---

*End of output version resolution addendum. Same value = same version. Different value = new version. Nothing is deleted. The result records what changed.*

---

## Addendum: Output Version Resolution

### V1. Principle

When a derivation produces an output, the runner checks whether that canonical key already exists in the registry. The output is not blindly appended. The version is determined by comparison.

### V2. Rules

| Condition | Action | Result key |
|---|---|---|
| Key does not exist in registry | Register as v0 | `output_key_v0` |
| Key exists, value is identical | Reuse existing version | `output_key_v0` (no new node) |
| Key exists, value differs | Register as next version | `output_key_v1` with `supersedes: "output_key_v0"` |

### V3. Identity comparison

"Identical" means:
- For `Fraction`: numerator and denominator are equal
- For `int`: integer equality
- For `str` (approximate): string equality of the plain decimal representation
- For `bool`: boolean equality

No tolerance. No rounding. If two Fraction values are mathematically equal but stored in different reduced forms, `Fraction` handles normalization automatically.

### V4. Version bumping

When a new version is created:
- The new node carries `supersedes: "output_key_vN"` pointing to the version it replaces
- The new node carries a pitfall entry if the change was a correction, or a notes entry if the change was from updated inputs
- The old version remains in the registry — never deleted
- The result JSON records `"output_key": {"version": 1, "previous_version": 0, "changed": true}`

When the value is unchanged:
- No new node is created
- The result JSON records `"output_key": {"version": 0, "changed": false}`

### V5. Result output manifest

The result JSON gains a new field `output_versions`:

```json
{
    "output_versions": {
        "coupling_alpha_em_v0": {"version": 0, "changed": false},
        "gap_pure_gauge_ratio_derived_v0": {"version": 0, "changed": false},
        "result_alpha_s_two_loop_full_bij_v1": {"version": 1, "changed": true, "previous": 0}
    }
}
```

This is the provenance record showing exactly what changed and what didn't in each run.

### V6. Runner implementation

After each derivation executes:

```
for each output_key, output_value in derivation.outputs:
    existing = registry.find(canonical_key)
    if existing is None:
        register as v0
    elif existing.value == output_value:
        record unchanged, reuse version
    else:
        register as v(existing.version + 1) with supersedes
        record changed
    append to working pool
```

### V7. Interaction with datasets

When a dataset override pins a value to a specific version, and a derivation produces a different value for the same key, the derivation output takes precedence within the experiment run but does NOT override the dataset pin in the registry. The new version is registered alongside the pinned version. The result records both the dataset-pinned version and the derivation-produced version.

---

*End of output version resolution addendum. Same value = same version. Different value = new version. Nothing is deleted. The result records what changed.*

---

## Addendum: Failed Output Versioning

### F1. Principle

Output version bumping only occurs when the experiment completes with status `complete` — all comparisons pass or are INFO. If any comparison fails, the outputs are preserved for investigation but never registered as canonical versions.

### F2. Rules

| Experiment status | Output key format | Registered in registry | Can supersede |
|---|---|---|---|
| `complete` (0 failures) | `output_key_v1` | yes | yes |
| `partial` (1+ failures) | `output_key_failed_v0` | yes, as failed | no |
| `failed` (execution error) | `output_key_failed_v0` | yes, as failed | no |

### F3. Failed output nodes

A failed output node carries:
- `key`: `output_key_failed_v0` (or `_failed_v1` if multiple failed runs)
- `node_type`: `value`
- `value_type`: same as normal
- `source`: the experiment key
- `status`: `failed`
- `notes`: reason for failure — which comparisons failed and by how much

Failed outputs are searchable, inspectable, and preserved. They are never returned by the resolver when a derivation or experiment requests the canonical key. The `_failed_` infix prevents accidental consumption.

### F4. Version bump gating

The runner's post-execution flow becomes:

```
1. Execute all derivations, collect outputs
2. Run all comparisons
3. Count failures

If failures == 0:
    For each output:
        Compare against registry
        Same value -> reuse version
        Different value -> register as next version with supersedes
    Status: complete

If failures > 0:
    For each output:
        Register as output_key_failed_vN
        Do NOT supersede any existing version
    Status: partial
```

### F5. Result JSON

The result JSON records the gating decision:

```json
{
    "status": "partial",
    "failure_count": 2,
    "version_bump_gated": true,
    "output_versions": {
        "coupling_alpha_em_failed_v0": {"version": 0, "changed": true, "gated": true},
        "gap_pure_gauge_ratio_derived_failed_v0": {"version": 0, "changed": true, "gated": true}
    }
}
```

When the experiment passes:

```json
{
    "status": "complete",
    "failure_count": 0,
    "version_bump_gated": false,
    "output_versions": {
        "coupling_alpha_em_v0": {"version": 0, "changed": false},
        "result_alpha_s_two_loop_full_bij_v1": {"version": 1, "changed": true, "previous": 0}
    }
}
```

### F6. Investigating failures

Failed outputs are available for investigation:

```
python data6.py search failed
python data6.py info result_alpha_s_two_loop_full_bij_failed_v0
```

The failed value, the experiment that produced it, and the comparison that failed are all preserved and linked. A researcher can compare the failed value against the canonical value to understand the discrepancy.

### F7. Re-running after fixes

After fixing the cause of failure, re-run the experiment. If it now passes, the outputs register as canonical versions. The failed outputs remain in the registry as historical evidence of the investigation path.

---

*End of failed output versioning addendum. Passing experiments bump versions. Failing experiments save data with `_failed_` infix. Failed outputs never squash real values.*

