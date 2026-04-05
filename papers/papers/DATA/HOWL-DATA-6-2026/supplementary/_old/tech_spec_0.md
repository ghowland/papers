# DATA-6 Technical Specification
## Universal Versioned Node Physics System

Document: `data_6_tech_spec_v0.md`
Version: 0.0
Date: 2026-04-05
Status: Draft

---

## 1. Purpose

DATA-6 is a dynamic node-based system for physics research built on integer fraction arithmetic.

Every entity in the system — constant, derivation, connection, experiment, result — is a versioned node with a canonical key, a shared metadata envelope, and full provenance. The access interface is uniform: consumers request a named value at an optional version and receive it regardless of whether the source is a raw constant, a derivation output, or an experiment result.

DATA-6 replaces the DATA-5 bootstrap registries with a unified architecture where:

- constants, connections, and experiment data live in JSON
- derivation functions and connection functions live in Python but are addressable as data
- provenance and versioning are first-order throughout
- all arithmetic preserves exact `fractions.Fraction` values where possible

---

## 2. Core Principles

### 2.1 Everything is a versioned node
Every entity has a canonical key and a version. Once a versioned key exists it is never edited in place. Corrections produce new versions.

### 2.2 Inputs and outputs are symmetric
There is no privileged distinction between a raw constant and an experiment output at the access layer. Both are named values. Both are version-pinned. Both carry provenance.

### 2.3 Provenance is first-order
Every value in the system can trace back through which versions of which constants, which derivation function version, which experiment definition, and which prior results produced it.

### 2.4 Integer fraction arithmetic
The system uses `fractions.Fraction` as its primary numeric type. Floating point is never used. `mpmath.mpf` is permitted only at the irrational/numerical boundary (π, √, numerical integration). `mp.dps = 100` minimum. The `math` module is never used.

### 2.5 Append-only versioning
All versioned keys follow the pattern `canonical_name_vN` where N is a non-negative integer. Version 0 is the initial registration. New understanding means new version. Old versions are never modified or deleted.

---

## 3. Node Types

The system has five node types. All share a common metadata envelope. Each type adds type-specific fields.

### 3.1 Common metadata envelope

Every node carries:

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes | Full versioned key, e.g. `mass_z_boson_v0` |
| `canonical` | string | yes | Key without version suffix, e.g. `mass_z_boson` |
| `version` | int | yes | Version number, e.g. `0` |
| `node_type` | string | yes | One of: `value`, `derivation`, `connection`, `experiment`, `result` |
| `topic` | string | yes | First token of the canonical key |
| `term` | string | yes | Remaining tokens after topic, before version |
| `source` | string | yes | Origin reference (table, paper, experiment key) |
| `notes` | string | no | Human-readable context |
| `created` | string | no | ISO timestamp of registration |
| `tags` | list[str] | no | Classification tags |
| `supersedes` | string | no | Key of the version this replaces, if any |

### 3.2 Value nodes

A value node is an atomic named fact: a physical constant, a measured parameter, a tabulated number, or a classification.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | Fraction / int / str / None | yes | The value itself |
| `value_type` | string | yes | One of: `exact_fraction`, `exact_integer`, `approximate`, `classification`, `deferred` |
| `unit` | string | yes | Physical unit or `dimensionless` |
| `ref` | string | no | Legacy platform reference for deferred values |
| `uncertainty` | string | no | Uncertainty specification if applicable |

**Value type rules:**

- `exact_fraction`: value is a `Fraction`. This is the preferred type.
- `exact_integer`: value is an `int`. Stored as-is, convertible to `Fraction(n, 1)`.
- `approximate`: value is a string containing a decimal number. Used when exact rational form is not known or not meaningful.
- `classification`: value is a string label, e.g. `"chiral"`, `"near_k_two_thirds"`.
- `deferred`: value is `None`, `ref` field contains a reference to an external source. Used for irrational constants (π, R2) pending resolution.

### 3.3 Derivation nodes

A derivation node is a versioned executable transformation that consumes named values and produces new named values.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `callable` | function | yes | The Python function implementing the derivation |
| `inputs` | list[str] | yes | Canonical keys of required input values |
| `outputs` | list[str] | yes | Canonical keys of produced output values |
| `arithmetic_mode` | string | yes | One of: `exact`, `mixed`, `numeric` |
| `description` | string | yes | What this derivation computes |

**Callable contract:**

All derivation functions use the signature:

```python
def derivation_name_vN(value_dicts: list[dict]) -> dict
```

Where the return dict contains:

```python
{
    "key": "derivation_name_vN",
    "outputs": {
        "output_canonical_key_vN": value,
        ...
    },
    "notes": ""
}
```

**Arithmetic mode:**

- `exact`: all computation uses `Fraction` only. No mpf.
- `mixed`: `Fraction` for rational steps, `mpf` at irrational boundary.
- `numeric`: numerical methods (integration, root finding). Results stored as approximate strings.

### 3.4 Connection nodes

A connection node is a versioned executable relationship bundle that pulls named values and returns a structured map of how they relate.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `callable` | function | yes | The Python function implementing the connection |
| `inputs` | list[str] | yes | Canonical keys of required input values |
| `connection_type` | string | yes | Category: `convergence`, `correction_chain`, `traceability`, `adjacency`, `shared_set` |
| `description` | string | yes | What relationship this connection captures |

**Callable contract:**

Same signature as derivations:

```python
def connection_name_vN(value_dicts: list[dict]) -> dict
```

Return dict contains:

```python
{
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

**Connections do not derive new physics.** They organize existing values into stable named structures with explicit relationship edges. They are versioned views, not computations.

### 3.5 Experiment nodes

An experiment node is a versioned execution plan that declares its dependencies, the derivations to run, the outputs to produce, and the diagrams to generate.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string | yes | What this experiment tests or produces |
| `dependencies` | dict | yes | Version-pinned requirements (see below) |
| `execution_plan` | list[str] | yes | Ordered list of derivation keys to execute |
| `expected_outputs` | list[str] | yes | Canonical keys of values this experiment should produce |
| `diagrams` | list[str] | no | Diagram renderer keys to invoke |
| `connections` | list[str] | no | Connection keys to resolve as part of this experiment |

**Dependency declaration:**

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
        }
    }
}
```

**Dependency resolution order:**

1. Item-level version pin if specified
2. Experiment-level default version if specified
3. Latest version otherwise

**Result references:**

An experiment can depend on outputs from other experiments. The dependency declaration specifies the experiment key, its version, and which output keys to import. These outputs enter the value pool with the same interface as raw constants.

### 3.6 Result nodes

A result node is the output record of a completed experiment run.

Type-specific fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `experiment_key` | string | yes | Versioned key of the experiment that produced this result |
| `outputs` | dict | yes | Map of canonical output key to value |
| `resolved_dependencies` | dict | yes | Exact versions of all inputs that were used |
| `execution_log` | list[str] | no | Ordered record of derivations executed |
| `diagrams_produced` | list[str] | no | Keys of diagrams generated |
| `connections_resolved` | list[str] | no | Keys of connections that were resolved |
| `timestamp` | string | yes | ISO timestamp of execution |
| `status` | string | yes | One of: `complete`, `partial`, `failed` |

**Result outputs become values.** Each output in a result record is accessible through the universal value interface. A consumer requesting `result_alpha_s_two_loop_full_bij` at a version gets the value from the corresponding experiment result, with full provenance.

---

## 4. Naming Rules

### 4.1 Key format

All keys are lowercase, underscore-separated, with a version suffix:

```
{topic}_{term}_v{N}
```

- `topic`: single word, first token. Groups related items.
- `term`: one or more descriptive words. Longer names where physics ambiguity exists.
- `v{N}`: version suffix. `v0` for initial, `v1` for first correction, etc.

Examples:

```
mass_z_boson_v0
coupling_alpha_em_inverse_v0
beta_modified_su2_total_v0
connection_gap_correction_chain_v0
experiment_coupling_convergence_test_v0
```

### 4.2 Canonical keys

The canonical key is the key without the version suffix:

```
mass_z_boson
coupling_alpha_em_inverse
connection_gap_correction_chain
```

Canonical keys are used in dependency declarations and output references. The resolver maps them to specific versioned keys.

### 4.3 Topic prefixes

Current topic families:

| Prefix | Scope |
|---|---|
| `beta` | Beta function coefficients and shifts |
| `coupling` | Coupling constants and derived coupling values |
| `mass` | Particle and boson masses |
| `gap` | Gap ratios and related values |
| `group` | Group theory constants |
| `rep` | Representation data |
| `geom` | Geometric constants (π, R2, R4) |
| `integer` | Integer pool values |
| `koide` | Koide relation data |
| `cosmo` | Cosmological parameters |
| `result` | Derivation and experiment output values |
| `connection` | Connection bundle names |
| `experiment` | Experiment plan names |

### 4.4 Uniqueness

No two nodes of any type may share the same versioned key. The key is globally unique across all node types.

---

## 5. Dataset Versions

A dataset version is a lightweight composition spec that defines which version of each value to use.

### 5.1 Structure

```json
{
    "dataset": "howl_v1",
    "base": "howl_v0",
    "overrides": {
        "integer_four_times_yang_mills": 1
    },
    "notes": "Corrected yang-mills multiple from table 16 review."
}
```

### 5.2 Resolution

```
resolve(dataset_version):
    start with all values from base dataset
    apply overrides: for each canonical key, use the specified version
    strip version suffixes from keys
    return flat dict of canonical_key -> value
```

### 5.3 Rules

- The base dataset `howl_v0` includes all `_v0` values by default.
- Overrides are sparse: only changed values are listed.
- Overrides can chain: `howl_v2` can base on `howl_v1` which bases on `howl_v0`.
- The resolver flattens the chain and applies overrides in order.
- The resolved dataset is a frozen snapshot: every canonical key maps to exactly one versioned value.

### 5.4 Provenance

A resolved dataset records:

```json
{
    "dataset": "howl_v1",
    "resolved": {
        "mass_z_boson": {"version": 0, "key": "mass_z_boson_v0"},
        "integer_four_times_yang_mills": {"version": 1, "key": "integer_four_times_yang_mills_v1"},
        ...
    }
}
```

This is the provenance anchor for any experiment run against this dataset.

---

## 6. The Universal Access Interface

### 6.1 Principle

All named values are accessed through one interface regardless of origin:

```python
get(canonical_key, version=None, dataset=None) -> value_entry
```

- If `version` is specified: return that exact version.
- If `dataset` is specified: return the version pinned by that dataset.
- If neither: return the latest version.

### 6.2 Value entry

The returned entry is always a dict with the common metadata envelope plus the value:

```python
{
    "key": "mass_z_boson_v0",
    "canonical": "mass_z_boson",
    "version": 0,
    "node_type": "value",
    "value": Fraction(911876, 10),
    "value_type": "exact_fraction",
    "unit": "MeV",
    "source": "corrected master table 11",
    ...
}
```

### 6.3 Experiment outputs as values

When an experiment result produces `result_alpha_s_two_loop_full_bij`, that output is registered as a value node with:

- `source`: the experiment key that produced it
- `node_type`: `value` (it is now an atomic fact)
- provenance metadata linking back to the experiment and its resolved dependencies

The consumer sees no difference between this and a raw constant.

---

## 7. The Resolver

The resolver is the component that prepares inputs for derivations, connections, and experiments.

### 7.1 Responsibilities

1. Accept a dependency declaration (list of canonical keys with optional version pins)
2. Resolve each key to a specific versioned value entry
3. Handle dataset-level defaults
4. Handle experiment result references (fetch outputs from prior experiment results)
5. Return a flat list of value entry dicts suitable for passing to `fn(value_dicts)`

### 7.2 Resolution order

For each requested canonical key:

1. If the dependency declaration specifies a version: use that version
2. If a dataset context is active: use the dataset's pinned version
3. Otherwise: use the latest registered version

### 7.3 Error handling

- Missing key: raise with the canonical key name
- Missing version: raise with the key and requested version
- Circular experiment dependencies: detect and raise before execution

---

## 8. The Runner

The runner executes experiments.

### 8.1 Execution flow

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
    6. Generate diagrams if specified
    7. Create and store the result node
    8. Register result outputs as new value nodes
```

### 8.2 DAG execution

Derivations in the execution plan may depend on outputs from earlier derivations in the same plan. The runner executes them in declared order and merges outputs after each step. The experiment author is responsible for declaring a valid execution order.

A future version may add automatic topological sorting based on the metadata-declared inputs and outputs.

### 8.3 Result registration

After successful execution, each output value is registered as a new value node with:

- `key`: the output canonical key with the experiment's version suffix
- `source`: the experiment key
- `node_type`: `value`
- full provenance linking to the experiment's resolved dependencies

---

## 9. The Correction Cycle

### 9.1 Correcting a constant

1. Identify the error in `canonical_key_v0`
2. Register `canonical_key_v1` with the corrected value
3. Create a new dataset version that overrides `canonical_key` to version 1
4. Re-run affected experiments against the new dataset
5. Compare results

The old value, old dataset, old experiment results all remain. Nothing is deleted.

### 9.2 Correcting a derivation

1. Identify the error in `derivation_name_v0`
2. Write `derivation_name_v1` with corrected logic
3. Register the new derivation node
4. Create or update experiments to reference `derivation_name` at version 1
5. Re-run and compare

### 9.3 Correcting a connection

Same pattern as derivations. New version, new registration, re-resolve.

### 9.4 Reforming an experiment

1. `experiment_ABC_v0` produced results
2. New understanding leads to `experiment_ABC_v1` with different dependencies or execution plan
3. Run `experiment_ABC_v1`, get new results
4. Both result sets exist, both are accessible, both carry full provenance

### 9.5 Discovering new connections

Experiment results may reveal new relationships. These become:

- New connection functions (`connection_new_relationship_v0`)
- Registered as connection nodes
- Available for future experiments to depend on

---

## 10. Storage

### 10.1 What lives in JSON

- Value nodes (exported from Python bootstrap or registered directly)
- Experiment nodes (plans, dependency declarations)
- Result nodes (outputs, provenance, execution logs)
- Dataset version specs (base + overrides)
- Connection outputs (cached resolved bundles, optionally)

### 10.2 What lives in Python

- Derivation callables (executable logic, versioned)
- Connection callables (executable logic, versioned)
- Derivation metadata registry (`DERIVATION_INDEX`)
- Connection metadata registry (`CONNECTION_INDEX`)
- Resolver implementation
- Runner implementation
- Helper functions (`_frac`, `_mpf`, `_need`, etc.)

### 10.3 What bridges both

- Derivation and connection nodes have metadata in JSON and callables in Python
- The metadata (inputs, outputs, description, tags) is JSON-serializable
- The callable is referenced by key and loaded from the Python registry at runtime

### 10.4 File organization

```
data_6/
    values/
        values_v0.json          # All v0 value nodes
        values_v1.json          # v1 overrides only
    derivations/
        derivations_v0.py       # All v0 derivation callables
        derivations_v0_meta.json # Metadata for v0 derivations
    connections/
        connections_v0.py       # All v0 connection callables
        connections_v0_meta.json # Metadata for v0 connections
    experiments/
        experiment_ABC_v0.json  # Experiment plan
    results/
        experiment_ABC_v0_run_001.json  # Result record
    datasets/
        howl_v0.json            # Base dataset spec
        howl_v1.json            # Override dataset spec
    lib/
        resolver.py
        runner.py
        registry.py             # Universal node registry
        types.py                # Shared helpers, Fraction utilities
```

---

## 11. Registry

### 11.1 Universal node registry

A single registry holds all nodes of all types:

```python
REGISTRY = {
    "mass_z_boson_v0": { ... },           # value node
    "coupling_extraction_v0": { ... },     # derivation node
    "connection_integer_network_v0": { ... }, # connection node
    "experiment_ABC_v0": { ... },          # experiment node
    "experiment_ABC_v0_run_001": { ... },  # result node
}
```

All nodes share the common metadata envelope. Type-specific fields are present according to `node_type`.

### 11.2 Type-specific indexes

For convenience and performance, the registry maintains type-filtered views:

```python
VALUE_INDEX = {}        # all value nodes
DERIVATION_INDEX = {}   # all derivation nodes
CONNECTION_INDEX = {}   # all connection nodes
EXPERIMENT_INDEX = {}   # all experiment nodes
RESULT_INDEX = {}       # all result nodes
```

These are projections of the universal registry, not independent stores.

### 11.3 Registration

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

## 12. Arithmetic Rules

### 12.1 Hierarchy

1. `fractions.Fraction` — preferred for all exact rational values
2. `int` — acceptable, implicitly `Fraction(n, 1)` when used in computation
3. `mpmath.mpf` — only at irrational/numerical boundaries
4. `str` — for approximate values that have no known exact rational form
5. `float` — never used anywhere in the system

### 12.2 Computation rules

- All exact derivations operate on `Fraction` values
- When a derivation needs π, √, exp, log: convert `Fraction` to `mpf`, compute, store result as approximate string
- `mp.dps = 100` minimum for all mpf computation
- The `math` module is never imported or used
- Deterministic execution: same inputs always produce same outputs

### 12.3 Display

- `Fraction` values display as `"numerator/denominator"`
- `mpf` results display via `mp.nstr(value, N)` where N is specified per output
- Approximate string values display as-is

---

## 13. Migration from DATA-5

### 13.1 Values

- `VALUE_INDEX_V0` entries from `data_5_v0_master_value_registry.py` are exported to `values/values_v0.json`
- Each entry gains the full common metadata envelope
- `value_type` field is inferred from the Python type of the value
- The `add()` helper is replaced by `register()` in the universal registry

### 13.2 Derivations

- Functions from `data_5_v0_master_derivation_registry.py` move to `derivations/derivations_v0.py`
- Metadata is extracted from docstrings and registered in `derivations_v0_meta.json`
- `FUNCTION_INDEX_V0` is replaced by registration in the universal registry with `node_type: "derivation"`

### 13.3 Connections

- Functions from `data_5_v0_master_connection_registry.py` move to `connections/connections_v0.py`
- Same metadata extraction and registration pattern as derivations

### 13.4 Helper functions

- `_value_map`, `_need`, `_frac`, `_mpf`, `_mp_str` move to `lib/types.py`
- Shared across all derivation and connection modules

---

## 14. Open Design Decisions

These items are identified but not yet frozen:

1. **Diagram nodes**: Should diagram renderers be a sixth node type, or are they a subtype of derivation that produces visual output instead of numeric output?

2. **Connection output persistence**: Should resolved connection bundles be cached as standalone JSON artifacts, or only embedded in result records?

3. **Automatic DAG resolution**: Should the runner topologically sort derivation execution plans automatically, or require the experiment author to declare valid order?

4. **Dataset version chaining depth**: Should there be a limit on how many levels of base/override chaining are allowed?

5. **Concurrency**: Should experiment runs be parallelizable when their derivation DAGs have independent branches?

6. **Schema validation**: Should JSON schemas (JSON Schema or similar) be defined for each node type, or is Python-side validation sufficient for now?

7. **Experiment result versioning**: When the same experiment is re-run with the same inputs, should the result key include a run counter, a timestamp hash, or both?

---

## 15. Summary

DATA-6 is a universal versioned node system where:

- every entity is a node with a canonical key, version, and metadata envelope
- five node types cover the full research cycle: values, derivations, connections, experiments, results
- inputs and outputs are symmetric: experiment results become values accessible through the same interface as raw constants
- dataset versions are lightweight overlay specs enabling sparse corrections without copying
- provenance tracks the complete dependency chain from any output back to its sources
- integer fraction arithmetic (`fractions.Fraction`) is the primary numeric type throughout
- all versioned keys are append-only and immutable once registered
- the resolver provides uniform access, the runner executes experiments, and the correction cycle enables iterative refinement without losing history

