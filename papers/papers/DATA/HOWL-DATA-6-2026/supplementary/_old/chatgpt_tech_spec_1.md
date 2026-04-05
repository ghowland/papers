```md
# DATA-5 / HOWL Research Runtime Technical Specification
## Updated architecture pass with bootstrap Python registries for values, derivations, and connections

Document: `data_5_master_spec_v2_bootstrap_registry_pass.md`
Version: 0.2
Date: 2026-04-05
Status: Draft, implementation-bridge pass before final JSON object freeze

---

## 1. Purpose of this update

This revision walks the first-pass master spec forward into an executable bootstrap form.

The original architecture remains the target:

1. JSON data on disk
2. versioned Python derivation functions
3. experiment JSON manifests
4. result JSON records
5. diagram artifact records

However, before final JSON schemas are frozen, the system now adopts a bootstrap registry layer in Python for three families:

- values
- derivations
- connections

This update documents that bridge.

The purpose is to allow:

- stable canonical naming now
- versioned executable functions now
- machine-readable registration now
- later export/migration into final JSON records without renaming everything twice

This is not the final storage form.
It is the implementation bridge that preserves the final architecture.

---

## 2. What has now been implemented conceptually

Three first-pass registry scripts now define the runtime bootstrap pattern.

### 2.1 Value registry
Script:
- `data_5_v0_master_value_registry.py`

Role:
- defines canonical value keys
- stores v0 value metadata in one Python registry
- preserves exact `Fraction` values where available
- allows string values for approximate/tabulated results
- allows `ref` for legacy-backed exact constants not yet fully expanded in-table

Primary registry:
- `VALUE_INDEX_V0`

### 2.2 Derivation registry
Script:
- `data_5_v0_master_derivation_registry.py`

Role:
- defines versioned Python derivation functions
- gives all derivations one common call signature
- returns machine-readable output dicts
- registers all derivations centrally

Primary registry:
- `FUNCTION_INDEX_V0`

### 2.3 Connection registry
Script:
- `data_5_v0_master_connection_registry.py`

Role:
- defines versioned Python connection functions
- bundles named values and explicit relation edges
- lets experiments request a versioned “understanding of how things connect”
- makes connections swappable and testable across versions

Primary registry:
- `FUNCTION_INDEX_V0`

---

## 3. Architectural meaning of the new bootstrap layer

This update does not replace the original JSON-first design.

Instead it introduces a temporary but structured bootstrap rule:

### 3.1 Bootstrap rule
Before final JSON schemas are frozen, Python registry scripts are allowed as canonical staging sources for:

- value naming and metadata
- derivation registration
- connection registration

### 3.2 Long-term rule remains unchanged
Final persistent authority remains:

- JSON for stored values, experiments, results, diagrams, domains, boundaries, and catalogs
- Python only for executable logic

### 3.3 Interpretation
Therefore:

- the value registry script is a pre-JSON canonical source
- the derivation registry script is a final-form executable source
- the connection registry script is a final-form executable source
- later export/import tooling will move the value registry into JSON records

---

## 4. Current value registry model

The first-pass value script establishes the naming standard.

## 4.1 Key rule
Each value key:

- is lowercase
- ends in `_v0`
- starts with a single-word topic
- uses longer descriptive names where physics ambiguity exists

Examples:
- `beta_sm_u1_total_v0`
- `coupling_alpha_2_inverse_mz_v0`
- `mass_z_boson_v0`
- `geom_r2_v0`

## 4.2 Registry behavior
The helper `add(...)`:

- validates the key
- enforces uniqueness
- extracts `topic` and `term`
- binds the value into `globals()`
- stores metadata in `VALUE_INDEX_V0`

Each record currently contains:

- `key`
- `topic`
- `term`
- `version`
- `value`
- `unit`
- `source`
- `notes`
- `ref`

## 4.3 Allowed value forms
The current registry supports:

- exact `Fraction`
- integer
- string numeric values
- string classification values
- `None` plus `ref` for deferred legacy-backed values

This is acceptable for the bootstrap pass.
Final JSON typing rules will later separate these more formally.

## 4.4 Scope of current source set
The value registry uses:

- Tables 1–25 as the source set

It intentionally does not encode Tables 26–27 as values, because those are better treated later as:

- verification/status metadata
- level/taxonomy metadata

That is now part of the spec.

---

## 5. Current derivation registry model

Derivations are now explicitly represented as Python functions with one uniform interface.

## 5.1 Function signature rule
All derivation functions use the same signature:

```python
fn(value_dicts)
```

where:

- `value_dicts` is a list of value-entry dicts from `VALUE_INDEX_V0`

## 5.2 Input contract
Each derivation function documents its required inputs in the docstring.

The docstring states:

- the source key in `VALUE_INDEX_V0`
- the local variable name used inside the function

Example pattern:

```python
def coupling_extraction_v0(value_dicts):
    """
    Input bindings from VALUE_INDEX_V0:
    - coupling_alpha_em_inverse_v0 -> alpha_inv
    - coupling_sin2_theta_w_v0 -> sin2_tW
    - coupling_alpha_s_mz_v0 -> alpha_s
    """
```

This is now the first-pass executable input contract.

## 5.3 Output contract
Each derivation returns a plain dict with:

- `key`
- `outputs`
- `notes`

Example shape:

```python
{
  "key": "coupling_extraction_v0",
  "outputs": {
    "coupling_alpha_em_v0": ...,
    "coupling_alpha_1_inverse_gut_normalized_mz_v0": ...,
    "coupling_alpha_2_inverse_mz_v0": ...,
    "coupling_alpha_3_inverse_mz_v0": ...
  },
  "notes": ""
}
```

## 5.4 Registration rule
All derivation callables are registered in:

```python
FUNCTION_INDEX_V0 = {
    "coupling_extraction_v0": coupling_extraction_v0,
    ...
}
```

This is the current machine-readable derivation registry.

## 5.5 Arithmetic rule
The derivation script preserves the original arithmetic policy:

- `Fraction` where exact
- `mpf` only at irrational/numeric boundary
- `mp.dps = 100`
- no `math`
- deterministic execution

---

## 6. Current connection registry model

Connections are now introduced as a distinct executable family.

## 6.1 Purpose of connections
A connection is not the same thing as:

- a stored value
- a physics derivation
- an experiment result

A connection is a versioned, executable relationship bundle that:

- requests a set of values
- binds them to stable names
- returns the explicit relationships among them

This lets the system encode “what connects to what” as a versioned object.

## 6.2 Why connections matter
This supports a new capability:

- experiments can request a connection set
- connection sets can be version-pinned
- later revised understandings can be compared directly

This is important for HOWL because many claims are not single derived numbers, but structured adjacency/traceability statements.

## 6.3 Function signature rule
All connection functions use the same signature as derivations:

```python
fn(value_dicts)
```

## 6.4 Input contract
Like derivations, each connection function documents required bindings in its docstring.

## 6.5 Output contract
Each connection function returns:

- `key`
- `named_values`
- `edges`
- `notes`

Example shape:

```python
{
  "key": "connection_integer_network_v0",
  "named_values": {
    "ym_11": {...},
    "b2_abs_13": {...}
  },
  "edges": [
    {"from": "ym_11", "to": "dm_prefactor", "relation": "numerator_source"}
  ],
  "notes": ""
}
```

## 6.6 Registration rule
Connection functions are also registered in a module-level:

```python
FUNCTION_INDEX_V0 = {}
```

This mirrors the derivation pattern exactly.

---

## 7. New executable object family: connections

The original first-pass spec did not fully define connections as a first-class executable family.
This update adds them.

## 7.1 Definition
A connection is a versioned executable object that returns a structured relationship map over named values.

## 7.2 Conceptual role
Connections sit between:

- raw values
- derived outputs
- semantic/query layers

They are especially useful for:

- coupling convergence bundles
- integer traceability maps
- shared-program integer sets
- adjacency maps
- connection tables extracted from master notes

## 7.3 Persistence target
In the final system, connection execution outputs may be:

- embedded in result records
- cached as JSON artifacts
- referenced by experiments as resolved semantic bundles

The exact final JSON object type is not frozen yet.

---

## 8. How this fits the original experiment system

The original plan said experiments declare dependencies explicitly.
This update extends that rule.

Experiments may now declare dependencies on:

- values
- prior results
- derivations
- diagram renderers
- connections

Example direction:

```json
"dependencies": {
  "values": {
    "coupling_alpha_em_inverse": 0
  },
  "derivations": {
    "coupling_extraction": 0
  },
  "connections": {
    "connection_coupling_convergence": 0
  }
}
```

Resolution semantics are the same:

1. item override if present
2. experiment default version if present
3. latest otherwise

This means connection bundles are swappable research assumptions, just like derivations.

---

## 9. Bootstrap naming and versioning rules

## 9.1 Shared executable naming rule
For both derivations and connections:

- lowercase only
- explicit version suffix
- current implemented form uses `_v0`

Examples:
- `coupling_extraction_v0`
- `gap_sm_ratio_v0`
- `connection_gap_correction_chain_v0`
- `connection_integer_network_v0`

## 9.2 Alias rule for later runtime
The current bootstrap scripts use explicit `_v0` keys only.
Later runtime layers may add aliases such as:

- `coupling_extraction`
- `connection_integer_network`

pointing to the latest version.

## 9.3 Append-only rule
Once a versioned key exists, it is never edited in place.
New understanding means new version:

- `..._v1`
- `..._v2`

This now applies equally to:

- values
- derivations
- connections

---

## 10. Immediate implementation conventions now in force

The following conventions are now part of the working spec.

## 10.1 Uniform callable signature
All executable registry families use:

```python
fn(value_dicts)
```

## 10.2 Docstring binding contract
Each executable function must declare:

- the value keys it expects
- the local names they bind to

## 10.3 Plain dict returns
No framework objects are required.
Executable functions return plain dicts.

## 10.4 Module-level central registry
Each registry module exposes a single central index.

For values:
- `VALUE_INDEX_V0`

For derivations:
- `FUNCTION_INDEX_V0`

For connections:
- `FUNCTION_INDEX_V0`

A later metadata index may be added beside each callable index.

---

## 11. Recommended next metadata layer

The current scripts register callables and values successfully, but the next pass should add explicit metadata registries.

Recommended additions:

### 11.1 For derivations
Add:
- `DERIVATION_INDEX_V0`

Each entry should contain:
- `key`
- `version`
- `inputs`
- `outputs`
- `description`
- `tags`
- `arithmetic_mode`
- `notes`

### 11.2 For connections
Add:
- `CONNECTION_INDEX_V0`

Each entry should contain:
- `key`
- `version`
- `inputs`
- `named_outputs`
- `connection_type`
- `description`
- `tags`
- `notes`

This preserves the architecture from the original spec while keeping the implementation plain.

---

## 12. Status of JSON relative to the new scripts

This point is important.

## 12.1 Values
Values are currently staged in Python for naming stability and later export.
They are not yet in final JSON value-record form.

## 12.2 Derivations
Derivations are already in their correct final medium:
- executable Python code

They still need final metadata and resolver integration.

## 12.3 Connections
Connections are also appropriately Python-executable.
They still need final metadata and experiment integration.

## 12.4 Conclusion
So the current state is:

- values: bootstrap Python now, JSON later
- derivations: Python now and later
- connections: Python now and later
- experiments/results/diagrams: still planned in JSON

This is consistent with the original architecture if treated as a staged transition.

---

## 13. Updated object-family picture

The working DATA-5 system now has these practical families:

### Persistent / target-persistent
- values
- experiments
- results
- diagrams
- domains
- boundaries
- catalogs

### Executable
- derivations
- diagram renderers
- connections
- resolvers
- runners
- checks

### Bootstrap-only staging
- Python value registry as pre-JSON canonical import source

---

## 14. Immediate open questions after this update

This update resolves the executable pattern for derivations and connections, but leaves these next decisions open:

1. Should connection outputs be persisted as standalone JSON artifacts, or only embedded in result records?

2. Should values continue to use scalar flattened keys in final JSON, or should some families become structured records with generated scalar aliases?

3. Should derivations and connections share one metadata schema family, or remain separate but parallel?

4. Should experiments request connections directly, or request them through execution-plan steps like derivations?

5. Should there be explicit “semantic bundle” support distinct from “connection”, or is connection the correct final name?

---

## 15. Updated summary

This update moves DATA-5 from architecture-only planning into a bootstrap executable form.

What now exists conceptually is:

- a first-pass canonical value registry in Python:
  - `data_5_v0_master_value_registry.py`
  - `VALUE_INDEX_V0`

- a first-pass canonical derivation registry in Python:
  - `data_5_v0_master_derivation_registry.py`
  - versioned functions with common signature
  - `FUNCTION_INDEX_V0`

- a first-pass canonical connection registry in Python:
  - `data_5_v0_master_connection_registry.py`
  - versioned connection bundles with named values and edges
  - `FUNCTION_INDEX_V0`

This preserves the original DATA-5 commitments while adding a practical bridge:

- stable naming now
- executable derivations now
- executable connection maps now
- future JSON migration later
- experiment pinning across values, derivations, and connections

The system is still walking toward the final form, but it now has a concrete executable registry model rather than only a conceptual one.
```
