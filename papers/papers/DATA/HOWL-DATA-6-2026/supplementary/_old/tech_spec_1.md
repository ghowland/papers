# DATA-6 Technical Specification

## Universal Versioned Node Physics System

Document: `data_6_tech_spec_v0.1.md`
Version: 0.1
Date: 2026-04-05
Status: Draft

---

## 1. Purpose and Scope

DATA-6 is a dynamic node-based system for physics research built on integer fraction arithmetic. Every entity in the system — constant, derivation, connection, experiment, result, program, dataset — is a versioned node with a canonical key, a shared metadata envelope, and full provenance.

The access interface is uniform: consumers request a named value at an optional version and receive it regardless of whether the source is a raw constant, a derivation output, or an experiment result. Inputs and outputs are symmetric.

DATA-6 replaces the DATA-5 bootstrap registries and object system with a unified architecture where:

- constants, connections, experiment data, programs, and datasets live in JSON
- derivation functions and connection functions live in Python but are addressable as data
- provenance and versioning are first-order throughout
- all arithmetic preserves exact `fractions.Fraction` values where possible
- no physics constants are hardcoded in executable code — all values come from the registry
- helpers are derivations — if an experiment uses a function, it is a registered versioned derivation node

This is a new kind of system. There is no existing pattern to copy. The architecture is designed to be extensible as understanding grows.

---

## 2. Core Principles

### 2.1 Everything is a versioned node
Every entity has a canonical key and a version. Once a versioned key exists it is never edited in place. Corrections produce new versions.

### 2.2 Inputs and outputs are symmetric
There is no privileged distinction between a raw constant and an experiment output at the access layer. Both are named values. Both are version-pinned. Both carry provenance.

### 2.3 Provenance is first-order
Every value in the system can trace back through which versions of which constants, which derivation function version, which experiment definition, and which prior results produced it. Source papers, session identifiers, and correction histories are recorded.

### 2.4 Integer fraction arithmetic
The system uses `fractions.Fraction` as its primary numeric type. Floating point is never used. `mpmath.mpf` is permitted only at the irrational/numerical boundary (π, √, numerical integration). `mp.dps = 100` minimum. The `math` module is never used. Conversion to float happens ONLY at two boundaries: display (diagrams) and irrational math. Never in the computation chain.

### 2.5 Append-only versioning
All versioned keys follow the pattern `canonical_name_vN` where N is a non-negative integer. Version 0 is the initial registration. New understanding means new version. Old versions are never modified or deleted.

### 2.6 No hardcoded physics constants
All values come from the registry. Derivation functions pull every constant — `G`, `M_sun`, `c`, `epsilon_0`, `sigma_SB`, Bessel zeros, Euler-Mascheroni, everything — from value nodes via the resolver. No `mpf("6.674e-11")` buried in executable code.

### 2.7 Helpers are derivations
There is no separate "helper" category. If an experiment or derivation chain uses a function, that function is a registered versioned derivation node with declared inputs, outputs, and metadata. `R2_area`, `disc_spot`, `wire_resistance`, `vena_contracta` are all derivations.

---

## 3. Common Metadata Envelope

Every node of every type carries these fields. This is the universal schema.

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes | Full versioned key, e.g. `mass_z_boson_v0` |
| `canonical` | string | yes | Key without version suffix, e.g. `mass_z_boson` |
| `version` | int | yes | Version number, 0-based |
| `node_type` | string | yes | One of 8 types (see section 4) |
| `topic` | string | yes | First token of the canonical key |
| `term` | string | yes | Remaining tokens after topic, before version |
| `level` | int or None | yes | 0=geometry, 1=group theory, 2=measured, 3=derived/predicted. None if unknown (must be resolved) |
| `section` | string | no | Grouping: `SI`, `measured`, `electroweak`, `quarks`, `nuclear`, `spectroscopy`, `Q335`, `engineering`, `observational`, `cosmological`, `GUT`, `koide`, `integer_pool`, `beta`, `representation`, `group_theory` |
| `source` | string | yes | Origin reference (table, paper, experiment key, data series) |
| `notes` | string | no | Human-readable context |
| `tags` | list[str] | no | Classification tags for search and filtering |
| `created` | string | no | ISO timestamp of registration |
| `supersedes` | string | no | Key of the version this replaces, if any |
| `legacy_refs` | dict | no | Cross-platform IDs, e.g. `{"data4": "B1", "phys24": "alpha_inv"}` |
| `pitfalls` | list[dict] | no | Documented prior errors, e.g. `{"wrong": "1/a2 = alpha_inv / sin2_tW", "right": "1/a2 = sin2_tW * alpha_inv", "session": "PHYS-30"}` |

### 3.1 Level convention

| Level | Meaning | Examples |
|---|---|---|
| 0 | Pure geometry / exact math | R2, π, e, √2, Bessel zeros, zeta values |
| 1 | Group theory / structural | Beta coefficients, Casimirs, Dynkin indices, gap ratios |
| 2 | Measured / observational | α⁻¹, sin²θ_W, α_s, masses, H0, dwarf galaxy data |
| 3 | Derived / predicted | α_s from unification, Koide m_τ, Ω_DM from integers |
| None | Unknown | Must be resolved — not a permanent state |

Level applies to all node types, not just values. A level-1 derivation operates on group theory constants. A level-2 experiment uses measured inputs. This enables cross-type queries like "show me everything at level 2."

### 3.2 Pitfalls

Any node type can carry pitfalls. A derivation might document a sign convention error. A value might document a correction history. A connection might document an edge that was wrong. Each pitfall entry contains:

```json
{
    "wrong": "description of the error",
    "right": "description of the correction",
    "session": "PHYS-28 iteration 2",
    "date": "2026-04-03"
}
```

---

## 4. Node Types

The system has 8 node types. All share the common metadata envelope. Each adds type-specific fields.

### 4.1 Value

An atomic named fact: a physical constant, a measured parameter, a tabulated number, a classification, an engineering specification, an observational catalog entry, or an experiment output.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | Fraction / int / str / None | yes | The value itself |
| `value_type` | string | yes | One of: `exact_fraction`, `exact_integer`, `approximate`, `classification`, `deferred` |
| `unit` | string | yes | Physical unit or `dimensionless` |
| `digits` | int | no | Number of significant figures that are meaningful |
| `uncertainty` | string | no | Uncertainty specification if applicable |
| `ref` | string | no | Legacy platform reference for deferred values |

Value type rules:

- `exact_fraction`: value is a `Fraction`. Preferred type.
- `exact_integer`: value is an `int`. Convertible to `Fraction(n, 1)`.
- `approximate`: value is a string containing a decimal number. Used when exact rational form is not known.
- `classification`: value is a string label, e.g. `"chiral"`, `"near_k_two_thirds"`.
- `deferred`: value is `None`, `ref` field contains a reference to an external source. Used for irrational constants pending resolution.

All values that were previously hardcoded in helper functions — `G`, `M_sun`, `epsilon_0`, `sigma_SB`, `c`, `tau_mu`, `hbar_c_MeV_fm`, Bessel zeros `j01` and `j11`, Euler-Mascheroni `gamma_EM`, etc. — are value nodes.

All observational catalogs — dwarf galaxy data, disc specs, fiber specs, speaker specs, wire gauges, just intonation ratios, sample rates — are value nodes with appropriate `section` tags.

### 4.2 Derivation

A versioned executable transformation that consumes named values and produces new named values. This includes everything previously called a "helper function."

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `callable` | function | yes | The Python function |
| `inputs` | list[str] | yes | Canonical keys of required input values |
| `outputs` | list[str] | yes | Canonical keys of produced output values |
| `arithmetic_mode` | string | yes | One of: `exact`, `mixed`, `numeric` |
| `output_type` | string | yes | One of: `numeric`, `verification`, `display`, `diagram` |
| `description` | string | yes | What this derivation computes |
| `depends_on_values` | bool | yes | False for pure-math derivations (e.g. `casimir_adj`) that take no registry values |

Callable contract:

```python
def derivation_name_vN(value_dicts: list[dict]) -> dict:
    return {
        "key": "derivation_name_vN",
        "outputs": {
            "output_canonical_key_vN": value,
            ...
        },
        "notes": ""
    }
```

Arithmetic modes:

- `exact`: all computation uses `Fraction` only. No mpf.
- `mixed`: `Fraction` for rational steps, `mpf` at irrational boundary (π, √, exp, log).
- `numeric`: numerical methods (Euler integration, bisection, root finding). Results stored as approximate strings.

Output types:

- `numeric`: produces numeric values (most derivations).
- `verification`: produces a pass/fail result comparing two computation paths.
- `display`: produces formatted text output (replaces `show_*` functions).
- `diagram`: produces a visual artifact (matplotlib figure, SVG, etc.).

### 4.3 Connection

A versioned executable relationship bundle that pulls named values and returns a structured map of how they relate.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `callable` | function | yes | The Python function |
| `inputs` | list[str] | yes | Canonical keys of required input values |
| `connection_type` | string | yes | See connection type table below |
| `description` | string | yes | What relationship this connection captures |

Callable contract:

```python
def connection_name_vN(value_dicts: list[dict]) -> dict:
    return {
        "key": "connection_name_vN",
        "named_values": {
            "local_name": {
                "var_name": "local_name",
                "source_key": "full_versioned_key",
                "value": ...,
                "value_text": "...",
                "unit": "...",
                ...
            },
            ...
        },
        "edges": [
            {"from": "local_name_a", "to": "local_name_b", "relation": "relation_type"},
            ...
        ],
        "notes": ""
    }
```

Connection types (extensible):

| Type | Meaning | Example |
|---|---|---|
| `convergence` | Values converging toward a common point | Coupling convergence at GUT scale |
| `correction_chain` | Sequential corrections from one state to another | Pure gauge → SM → CD gap correction |
| `traceability` | Where specific values appear across the system | Integer 11 appearing in beta, DM, amplification |
| `adjacency` | Which values relate to which | Object adjacency map |
| `shared_set` | Values shared across programs | Three programs sharing integer set |
| `boundary` | Values at a physics scale boundary | M_Z boundary with couplings, above/below properties |
| `hierarchy` | Ordered multi-scale relationship | Soliton nesting hierarchy, boundary stack |
| `cancellation` | Geometric/algebraic cancellation identity | R2 cancelling in R*C product, K_J*R_K = 2/e |
| `universal_equation` | Parameterized equation template | Q = F * R2 * d² * Z across 23 domains |

This list is extensible. New connection types are added as understanding grows.

Connections do not derive new physics. They organize existing values into stable named structures with explicit relationship edges. They are versioned views, not computations.

### 4.4 Experiment

A versioned execution plan that declares dependencies, derivations to run, outputs to produce, comparisons to make, and diagrams to generate.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string | yes | What this experiment tests or produces |
| `purpose` | string | no | Links to research program, e.g. `"PHYS-42 paper"` |
| `experiment_mode` | string | yes | One of: `standard`, `whatif`, `verification`, `consistency` |
| `dependencies` | dict | yes | Version-pinned requirements (see below) |
| `execution_plan` | list[str] | yes | Ordered list of derivation keys to execute |
| `expected_outputs` | list[str] | yes | Canonical keys of values this experiment should produce |
| `comparisons` | list[dict] | no | Comparison specifications (see section 11) |
| `diagrams` | list[str] | no | Diagram renderer derivation keys |
| `connections` | list[str] | no | Connection keys to resolve |

Experiment modes:

- `standard`: normal experiment — run derivations, produce outputs, compare against measurements.
- `whatif`: creates a temporary value overlay (not persisted unless promoted). Tests hypothetical inputs like arbitrary BSM representations.
- `verification`: compares outputs against independently computed reference values. Validates that the system reproduces known results.
- `consistency`: verifies that the same value computed through different derivation paths agrees. Cross-domain R2 consistency, cross-library validation.

Dependency declaration:

```json
{
    "dependencies": {
        "values": {
            "coupling_alpha_em_inverse": 0,
            "mass_z_boson": "latest"
        },
        "derivations": {
            "coupling_extraction": 0
        },
        "connections": {
            "connection_coupling_convergence": 0
        },
        "results": {
            "experiment_ABC": {
                "version": 3,
                "outputs": ["result_alpha_s_two_loop_full_bij"]
            }
        },
        "literals": {
            "custom_b1": {"value": "Fraction(25, 6)", "unit": "dimensionless"},
            "custom_b2": {"value": "Fraction(-13, 6)", "unit": "dimensionless"}
        }
    }
}
```

Dependency resolution order:

1. Literal values if specified (for whatif experiments)
2. Item-level version pin if specified
3. Dataset-level version pin if a dataset context is active
4. Latest version otherwise

### 4.5 Result

The output record of a completed experiment run.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `experiment_key` | string | yes | Versioned key of the experiment that produced this |
| `outputs` | dict | yes | Map of canonical output key to value |
| `resolved_dependencies` | dict | yes | Exact versions of all inputs used |
| `comparison_results` | list[dict] | no | Results of each comparison (see section 11) |
| `execution_log` | list[str] | no | Ordered record of derivations executed |
| `diagrams_produced` | list[str] | no | Keys of diagrams generated |
| `connections_resolved` | list[str] | no | Keys of connections resolved |
| `provenance_values` | list[str] | no | Every value key consumed (for diagram provenance) |
| `timestamp` | string | yes | ISO timestamp of execution |
| `status` | string | yes | One of: `complete`, `partial`, `failed` |

Result outputs become values. Each output in a result record is accessible through the universal value interface. A consumer requesting `result_alpha_s_two_loop_full_bij` at a version gets the value from the corresponding experiment result, with full provenance.

### 4.6 Program

A research program with thesis, status, kill switches, scripts, and inter-program connections.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `thesis` | string | yes | The research hypothesis |
| `status` | string | yes | One of: `ACTIVE`, `PARKED`, `KILLED`, `CONFIRMED` |
| `scripts` | list[dict] | no | Each with `name`, `description`, `stage` |
| `kill_switches` | list[dict] | no | Each with `name`, `condition`, `data_source` |
| `program_connections` | dict | no | Map of program_key to relationship description |

Status meanings:

- `ACTIVE`: under investigation.
- `PARKED`: paused, not killed. May resume.
- `KILLED`: falsified by a kill switch trigger. Do not reopen without new evidence.
- `CONFIRMED`: verified by independent test.

Kill switches are falsification conditions. If an experiment result triggers a kill condition, the program status changes to `KILLED`. The kill switch records which experiment and which result triggered it.

Programs group experiments. An experiment's `purpose` field links back to a program key.

### 4.7 Dataset

A lightweight composition spec that defines which version of each value to use.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `base` | string or None | yes | Key of the base dataset, or None for root |
| `overrides` | dict | yes | Map of canonical_key to version number |

Datasets are nodes in the registry. They are versioned and append-only. The root dataset `howl_v0` includes all `_v0` values by default.

---

## 5. Naming and Versioning Rules

### 5.1 Key format

All keys are lowercase, underscore-separated, with a version suffix:

```
{topic}_{term}_v{N}
```

- `topic`: single word, first token. Groups related items.
- `term`: one or more descriptive words. Longer names where physics ambiguity exists.
- `v{N}`: version suffix. `v0` for initial, `v1` for first correction, etc.

### 5.2 Topic prefixes

| Prefix | Scope |
|---|---|
| `beta` | Beta function coefficients and shifts |
| `coupling` | Coupling constants and derived coupling values |
| `mass` | Particle and boson masses |
| `gap` | Gap ratios and related values |
| `group` | Group theory constants |
| `rep` | Representation data |
| `geom` | Geometric constants (π, R2, R4) |
| `math` | Mathematical constants (Bessel zeros, Euler-Mascheroni, zeta values) |
| `integer` | Integer pool values |
| `koide` | Koide relation data |
| `cosmo` | Cosmological parameters |
| `astro` | Astrophysical constants (G, M_sun, etc.) |
| `eng` | Engineering constants (resistivity, permittivity, etc.) |
| `obs` | Observational catalog entries (dwarf galaxies, disc specs, etc.) |
| `result` | Derivation and experiment output values |
| `connection` | Connection bundle names |
| `experiment` | Experiment plan names |
| `program` | Research program names |
| `dataset` | Dataset version names |
| `style` | Rendering style/palette constants |

### 5.3 Canonical keys

The canonical key is the key without the version suffix. Used in dependency declarations and output references. The resolver maps canonical keys to specific versioned keys.

### 5.4 Uniqueness

No two nodes of any type may share the same versioned key. The key is globally unique across all node types.

### 5.5 Append-only rule

Once a versioned key exists, it is never edited in place. New understanding means new version: `_v1`, `_v2`. This applies equally to all 8 node types.

---

## 6. Dataset Versions

### 6.1 Structure

```json
{
    "key": "dataset_howl_v1",
    "node_type": "dataset",
    "base": "dataset_howl_v0",
    "overrides": {
        "integer_four_times_yang_mills": 1
    },
    "notes": "Corrected yang-mills multiple from table 16 review."
}
```

### 6.2 Resolution

```
resolve(dataset_version):
    start with all values from base dataset
    apply overrides: for each canonical key, use the specified version
    strip version suffixes from keys
    return flat dict of canonical_key -> value_entry
```

### 6.3 Rules

- The root dataset `dataset_howl_v0` includes all `_v0` values by default.
- Overrides are sparse: only changed values are listed.
- Overrides can chain: `howl_v2` bases on `howl_v1` which bases on `howl_v0`.
- The resolver flattens the chain and applies overrides in order.
- The resolved dataset is a frozen snapshot: every canonical key maps to exactly one versioned value.

### 6.4 Provenance

A resolved dataset records the full manifest:

```json
{
    "dataset": "dataset_howl_v1",
    "resolved": {
        "mass_z_boson": {"version": 0, "key": "mass_z_boson_v0"},
        "integer_four_times_yang_mills": {"version": 1, "key": "integer_four_times_yang_mills_v1"}
    }
}
```

This is the provenance anchor for any experiment run against this dataset.

---

## 7. Universal Access Interface

### 7.1 Value access

All named values are accessed through one interface regardless of origin:

```python
get(canonical_key, version=None, dataset=None) -> value_entry
```

- If `version` is specified: return that exact version.
- If `dataset` is specified: return the version pinned by that dataset.
- If neither: return the latest version.

### 7.2 Value entry format

The returned entry is always a dict with the common metadata envelope plus the value:

```python
{
    "key": "mass_z_boson_v0",
    "canonical": "mass_z_boson",
    "version": 0,
    "node_type": "value",
    "level": 2,
    "value": Fraction(911876, 10),
    "value_type": "exact_fraction",
    "unit": "MeV",
    "source": "corrected master table 11",
    ...
}
```

### 7.3 Experiment outputs as values

When an experiment result produces `result_alpha_s_two_loop_full_bij`, that output is registered as a value node with `source` set to the experiment key and provenance linking back to the experiment and its resolved dependencies. The consumer sees no difference between this and a raw constant.

### 7.4 Free-text search

```python
search(query) -> list[node]
```

Checks key, canonical, name, tags, notes, source, and topic fields. Substring match, case-insensitive. Returns all matching nodes of any type.

### 7.5 One-line display

Every node type implements a one-line summary format for quick scanning. The format varies by type but always includes the key, a compact value representation, and the most important metadata.

---

## 8. Resolver

The resolver prepares inputs for derivations, connections, and experiments.

### 8.1 Responsibilities

1. Accept a dependency declaration (canonical keys with optional version pins)
2. Resolve each key to a specific versioned value entry
3. Handle dataset-level defaults
4. Handle literal dependencies (values specified directly, not from registry)
5. Handle experiment result references (fetch outputs from prior results)
6. Return a flat list of value entry dicts suitable for `fn(value_dicts)`

### 8.2 Resolution order

For each requested canonical key:

1. If a literal value is specified in the dependency declaration: use that
2. If the dependency declaration specifies a version: use that version
3. If a dataset context is active: use the dataset's pinned version
4. Otherwise: use the latest registered version

### 8.3 Error handling

- Missing key: raise with the canonical key name
- Missing version: raise with the key and requested version
- Circular experiment dependencies: detect and raise before execution

---

## 9. Runner

The runner executes experiments.

### 9.1 Execution flow

```
run(experiment_key):
    1. Load the experiment node
    2. Resolve all dependencies via the resolver
    3. For each derivation in execution_plan (in order):
        a. Collect resolved inputs
        b. Execute the derivation callable
        c. Merge outputs into the working value pool
    4. For each connection in the connections list:
        a. Resolve and execute the connection callable
        b. Attach the connection result to the result record
    5. Collect expected outputs from the working value pool
    6. Execute comparisons (see section 11)
    7. Generate diagrams if specified
    8. Create and store the result node
    9. Register result outputs as new value nodes
    10. Check kill switches on associated program (if any)
```

### 9.2 DAG execution

Derivations in the execution plan may depend on outputs from earlier derivations in the same plan. The runner executes them in declared order and merges outputs after each step. The experiment author is responsible for declaring a valid execution order.

A future version may add automatic topological sorting based on declared inputs and outputs.

### 9.3 Result registration

After successful execution, each output value is registered as a new value node with:

- `key`: constructed from experiment key and output name
- `source`: the experiment key
- `node_type`: `value`
- full provenance linking to the experiment's resolved dependencies

### 9.4 Kill switch evaluation

After execution, if the experiment has a `purpose` linking to a program, the runner checks whether any comparison result triggers a kill switch condition on that program. If triggered, the program's status is changed to `KILLED` with a reference to the triggering experiment and result.

---

## 10. Arithmetic Rules

### 10.1 Hierarchy

1. `fractions.Fraction` — preferred for all exact rational values
2. `int` — acceptable, implicitly `Fraction(n, 1)` when used in computation
3. `mpmath.mpf` — only at irrational/numerical boundaries
4. `str` — for approximate values with no known exact rational form
5. `float` — never used anywhere in the system

### 10.2 Computation rules

- All exact derivations operate on `Fraction` values
- When a derivation needs π, √, exp, log: convert `Fraction` to `mpf`, compute, store result as approximate string
- `mp.dps = 100` minimum for all mpf computation
- The `math` module is never imported or used
- Deterministic execution: same inputs always produce same outputs

### 10.3 Rendering boundary rule

Conversion from `Fraction` to `float` or `mpf` happens ONLY at:

- Display/diagram rendering (matplotlib, formatted output)
- Irrational math (π, √, exp, log, numerical integration)

Never in the computation chain between derivations. If derivation A outputs a `Fraction` and derivation B consumes it, the value stays `Fraction` throughout.

### 10.4 Display formats

- `Fraction` values display as `"numerator/denominator"`
- `mpf` results display via `mp.nstr(value, N)` where N is specified per output
- Approximate string values display as-is

### 10.5 JSON serialization

`Fraction` values serialize as:

```json
{"_type": "Fraction", "num": 22, "den": 13}
```

`mpf` values serialize as:

```json
{"_type": "mpf", "value": "1.6933077261548"}
```

---

## 11. Comparison and Verification Contract

Every experiment that compares outputs against reference values uses a formal comparison contract.

### 11.1 Comparison specification

Each entry in an experiment's `comparisons` list contains:

| Field | Type | Required | Description |
|---|---|---|---|
| `output_key` | string | yes | Canonical key of the output to compare |
| `match_mode` | string | yes | How to compare (see below) |
| `reference_value` | varies | yes | The expected value |
| `reference_source` | string | yes | Where the reference came from |
| `precision_digits` | int | conditional | For `digits` mode |
| `threshold_ppm` | number | conditional | For `range` mode |
| `bounds` | list[2] | conditional | For `range` mode, `[lo, hi]` |
| `scaling_exponent` | number | conditional | For `scaling` mode |

### 11.2 Match modes

| Mode | Meaning | Pass condition |
|---|---|---|
| `exact` | Fraction equality | `got == expected` |
| `digits` | mpf string comparison at N significant digits | `mp.nstr(got, N) == mp.nstr(expected, N)` |
| `range` | Value within bounds or within ppm threshold | `lo <= got <= hi` or `abs(got - expected) / expected < threshold` |
| `rank_first` | Asserted value must rank #1 in a sorted output list | Closest candidate to target |
| `scaling` | Power law relationship holds between two input/output pairs | `output_ratio == input_ratio ** exponent` |
| `identity` | Mathematical identity holds to working precision | `abs(lhs - rhs) < 1e-30` |

### 11.3 Reference sources

| Source | Meaning |
|---|---|
| `exact_value` | A known exact value (Fraction) |
| `measured` | An experimental measurement with uncertainty |
| `library_computation` | Independently computed by a platform library |
| `prior_experiment` | Output from a previous experiment run |
| `identity` | Mathematical identity that must hold |

### 11.4 Comparison result

Each comparison produces:

```python
{
    "output_key": "result_alpha_s_two_loop_full_bij",
    "match_mode": "digits",
    "status": "PASS",
    "expected": "0.11838",
    "got": "0.11838",
    "deviation_ppm": 0.0,
    "deviation_pct": "0.0",
    "precision_digits": 5,
    "details": "5-digit match"
}
```

This replaces the ad-hoc `chk_exact`, `chk_close`, `chk_bool` pattern from DATA-5 with a formal, machine-readable contract.

---

## 12. Correction Cycle

### 12.1 Correcting a constant

1. Identify the error in `canonical_key_v0`
2. Register `canonical_key_v1` with the corrected value and `supersedes: "canonical_key_v0"`
3. Add a pitfall entry to the v1 node documenting the error
4. Create a new dataset version that overrides `canonical_key` to version 1
5. Re-run affected experiments against the new dataset
6. Compare results

The old value, old dataset, and old experiment results all remain. Nothing is deleted.

### 12.2 Correcting a derivation

1. Identify the error in `derivation_name_v0`
2. Write `derivation_name_v1` with corrected logic
3. Register the new derivation node with pitfall documentation
4. Create or update experiments to reference `derivation_name` at version 1
5. Re-run and compare

### 12.3 Correcting a connection

Same pattern as derivations. New version, new registration, re-resolve.

### 12.4 Reforming an experiment

1. `experiment_ABC_v0` produced results
2. New understanding leads to `experiment_ABC_v1` with different dependencies or execution plan
3. Run `experiment_ABC_v1`, get new results
4. Both result sets exist, both are accessible, both carry full provenance

### 12.5 Discovering new connections

Experiment results may reveal new relationships. These become new connection functions (`connection_new_relationship_v0`), registered as connection nodes, available for future experiments.

### 12.6 Kill switch triggers

An experiment result may trigger a kill switch on a research program. The trigger pathway:

1. Experiment runs and produces comparison results
2. Runner evaluates kill switch conditions on the associated program
3. If a condition is met, program status changes to `KILLED`
4. The kill switch record is updated with the triggering experiment key and timestamp
5. The program node is not deleted — its history and the falsification evidence are preserved

---

## 13. Storage and File Organization

### 13.1 What lives in JSON

- Value nodes (constants, measurements, engineering data, observational catalogs)
- Experiment nodes (plans, dependency declarations)
- Result nodes (outputs, provenance, comparison results)
- Dataset version specs (base + overrides)
- Program nodes (thesis, status, kill switches)
- Connection metadata (inputs, description, connection_type)
- Derivation metadata (inputs, outputs, description, arithmetic_mode)

### 13.2 What lives in Python

- Derivation callables (executable logic, versioned)
- Connection callables (executable logic, versioned)
- Resolver implementation
- Runner implementation
- Helper functions (`_frac`, `_mpf`, `_need`, `_value_map`, etc.)

### 13.3 What bridges both

Derivation and connection nodes have metadata in JSON and callables in Python. The metadata (inputs, outputs, description, tags) is JSON-serializable. The callable is referenced by key and loaded from the Python registry at runtime.

### 13.4 File organization

```
data_6/
    values/
        values_v0.json              # All v0 value nodes
        values_v1.json              # v1 overrides only
        values_engineering.json     # Engineering constants
        values_observational.json   # Observational catalogs
        values_astrophysical.json   # G, M_sun, etc.
        values_mathematical.json    # Bessel zeros, gamma_EM, etc.
    derivations/
        derivations_v0.py           # All v0 derivation callables
        derivations_v0_meta.json    # Metadata for v0 derivations
        derivations_domain_v0.py    # Domain/engineering derivations
        derivations_domain_v0_meta.json
    connections/
        connections_v0.py           # All v0 connection callables
        connections_v0_meta.json    # Metadata for v0 connections
    experiments/
        experiment_coupling_convergence_v0.json
        experiment_beta_cosmology_v0.json
        experiment_cross_domain_consistency_v0.json
    results/
        experiment_coupling_convergence_v0_run_001.json
    programs/
        program_beta_unification_v0.json
        program_toroidal_dm_v0.json
        program_hubble_running_v0.json
    datasets/
        dataset_howl_v0.json
        dataset_howl_v1.json
    lib/
        resolver.py
        runner.py
        registry.py                 # Universal node registry
        types.py                    # Fraction utilities, _frac, _mpf, _need
        search.py                   # Free-text search
        serialize.py                # JSON serialization with Fraction/mpf support
```

---

## 14. Registry

### 14.1 Universal node registry

A single registry holds all nodes of all types:

```python
REGISTRY = {
    "mass_z_boson_v0": { ... },                    # value
    "coupling_extraction_v0": { ... },              # derivation
    "connection_integer_network_v0": { ... },       # connection
    "experiment_coupling_convergence_v0": { ... },  # experiment
    "experiment_coupling_convergence_v0_run_001": { ... }, # result
    "program_beta_unification_v0": { ... },         # program
    "dataset_howl_v0": { ... },                     # dataset
}
```

### 14.2 Type-filtered indexes

For convenience and performance, the registry maintains type-filtered views:

```python
VALUE_INDEX = {}
DERIVATION_INDEX = {}
CONNECTION_INDEX = {}
EXPERIMENT_INDEX = {}
RESULT_INDEX = {}
PROGRAM_INDEX = {}
DATASET_INDEX = {}
```

These are projections of the universal registry, not independent stores.

### 14.3 Registration

```python
def register(node: dict) -> None:
    validate_envelope(node)
    validate_type_specific(node)
    key = node["key"]
    if key in REGISTRY:
        raise ValueError("Duplicate key: %s" % key)
    REGISTRY[key] = node
    TYPE_INDEXES[node["node_type"]][key] = node
```

---

## 15. Migration from DATA-5

### 15.1 Value migration

- `VALUE_INDEX_V0` entries from `data_5_v0_master_value_registry.py` export to `values/values_v0.json`
- Each entry gains the full common metadata envelope
- `value_type` is inferred from the Python type of the value
- The `add()` helper is replaced by `register()` in the universal registry

### 15.2 Derivation migration

- Functions from `data_5_v0_master_derivation_registry.py` move to `derivations/derivations_v0.py`
- Metadata is extracted from docstrings and registered in `derivations_v0_meta.json`
- `FUNCTION_INDEX_V0` is replaced by registration in the universal registry

### 15.3 Connection migration

- Functions from `data_5_v0_master_connection_registry.py` move to `connections/connections_v0.py`
- Same metadata extraction and registration pattern as derivations

### 15.4 Helper function migration

All helper functions from chunks 1-4 become registered derivation nodes:

- `extract_couplings` → `derivation_coupling_extraction_v0`
- `R2_area` → `derivation_r2_area_v0`
- `disc_spot` → `derivation_disc_spot_v0`
- `wire_resistance` → `derivation_wire_resistance_v0`
- `dm_baryon_ratio` → `derivation_dm_baryon_ratio_v0`
- etc.

### 15.5 Hardcoded constant migration

All constants buried in helper functions become value nodes:

- `_G` → `astro_gravitational_constant_v0`
- `_M_sun` → `astro_mass_sun_v0`
- `_c` → `eng_speed_of_light_v0` (or use existing SI value)
- `_EPSILON_0` → `eng_vacuum_permittivity_v0`
- `_SIGMA_SB` → `eng_stefan_boltzmann_v0`
- `_CU_RHO` → `eng_copper_resistivity_v0`
- `_J11` → `math_bessel_j1_first_zero_v0`
- `_J01` → `math_bessel_j0_first_zero_v0`
- `_GAMMA_EM` → `math_euler_mascheroni_v0`
- `_hbar_c_MeV_fm` → `eng_hbar_c_mev_fm_v0`
- `_tau_mu` → `mass_muon_lifetime_v0`

### 15.6 Observational catalog migration

All hardcoded data dicts become value nodes:

- `DWARFS["Fornax"]["M_vis"]` → `obs_fornax_mass_visible_v0`
- `DISC_DATA["CD"]["lambda_m"]` → `obs_cd_disc_wavelength_v0`
- `FIBER_DATA["SMF-28"]["MFD_1550_m"]` → `obs_smf28_mfd_1550_v0`
- `SPEAKER_DATA["12inch"]["d_eff_m"]` → `obs_speaker_12inch_deff_v0`
- `AWG["12"]` → `eng_awg_12_diameter_v0`

### 15.7 Domain class collapse

DATA-5's 9 domain classes collapse into DATA-6's 8 node types:

| DATA-5 class | DATA-6 node type | Notes |
|---|---|---|
| Constant | value | Direct mapping |
| BetaCoefficient | value | Decomposition becomes connection edges |
| Representation | value (multiple) | One value per quantum number |
| SolitonBoundary | connection | `connection_type: "boundary"` |
| R2Domain | connection | `connection_type: "universal_equation"` |
| R2Cancellation | connection | `connection_type: "cancellation"` |
| Modulus | value | With appropriate level |
| ExperimentResult | result | Direct mapping |
| ResearchProgram | program | Direct mapping |

### 15.8 Self-test migration

All self-tests from DATA-5 (chunk 1-4 tests, object tests, populate tests) become experiment nodes with `experiment_mode: "verification"` and formal comparison contracts.

---

## 16. Open Design Decisions

1. **Diagram output format**: Should diagram renderers produce files (PNG), inline artifacts (SVG), or both? The provenance_values list on results handles traceability either way.

2. **Automatic DAG resolution**: Should the runner topologically sort derivation execution plans automatically from declared inputs/outputs, or require the experiment author to declare valid order? Manual for now, automatic later.

3. **Dataset chaining depth**: Should there be a limit on how many levels of base/override chaining are allowed? No limit for now, but the resolver logs chain depth.

4. **Schema validation**: Should JSON Schema definitions be created for each node type, or is Python-side validation sufficient? Python-side for now, JSON Schema as a later hardening step.

5. **Result key format**: When the same experiment runs multiple times, should the result key include a run counter (`_run_001`), a timestamp hash, or both? Run counter for now.

6. **Search indexing**: Should `search()` maintain an inverted index for performance, or scan linearly? Linear scan is fine for the current scale. Index when it matters.

---

## 17. Summary

DATA-6 is a universal versioned node system where:

- 8 node types cover the full research cycle: values, derivations, connections, experiments, results, programs, datasets
- every entity is a node with a canonical key, version, level, and metadata envelope
- inputs and outputs are symmetric: experiment results become values accessible through the same interface as raw constants
- dataset versions are lightweight overlay specs enabling sparse corrections without copying
- provenance tracks the complete dependency chain from any output back to its sources
- integer fraction arithmetic (`fractions.Fraction`) is the primary numeric type throughout
- no physics constants are hardcoded in executable code
- helpers are derivations — everything executable is registered, versioned, and traceable
- comparison and verification is a formal contract with defined match modes
- the system is extensible — connection types, experiment modes, and node metadata grow as understanding grows
- all versioned keys are append-only and immutable once registered
- the resolver provides uniform access, the runner executes experiments, and the correction cycle enables iterative refinement without losing history
