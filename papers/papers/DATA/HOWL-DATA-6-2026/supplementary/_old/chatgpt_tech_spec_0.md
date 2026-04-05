# DATA-5 / HOWL Research Runtime Technical Specification
## First-pass master spec for versioned physics data, derivations, experiments, results, and diagrams

Document: `data_5_master_spec_v2_first_pass.md`
Version: 0.1
Date: 2026-04-05
Status: Draft, architecture pass before final object definitions

---

## 1. Purpose

This project defines a JSON-first, versioned research system for HOWL physics work.

The system must support:

- versioned physics data on disk
- executable derivations in Python
- experiments as version-pinned JSON manifests
- results as stored JSON artifacts
- diagrams as planned experiment outputs, not ad hoc scripts
- reuse of prior results in later experiments
- full provenance:
  - which constants were used
  - which versions were used
  - which derivations were used
  - which diagrams were planned and produced
  - which results fed later work

This spec supersedes the old “flat library + standalone demo script” model as the primary architecture.

It does not discard the old libraries. The existing HOWL libraries remain valid as legacy sources and migration inputs. DATA-5 wraps, imports, migrates, and extends them.

---

## 2. System Identity

DATA-5 is not just a library.

It is:

- a physics knowledge store
- a versioned derivation runtime
- an experiment manifest system
- a result provenance system
- a diagram planning and artifact system

The new source of truth is:

1. JSON data on disk
2. versioned Python derivation functions
3. experiment JSON manifests
4. result JSON records
5. diagram artifact records

Papers and notes are downstream outputs of this system.

---

## 3. Conceptual Framework

The system must preserve HOWL’s top-down framing of physics.

### 3.1 Core HOWL concepts to preserve in metadata and phrasing

- values run
- integer rules govern transformations
- domains and boundaries are first-class
- Level 1 = structure from framework
- Level 2 = values supplied by measurement
- Level 3 = predictions / derived outputs
- perturbative domains and non-perturbative walls must be distinguishable
- HOWL terminology and standard physics terminology must both be supported

### 3.2 Terminology rule

The system must support both:

- HOWL language
- standard physics language

Examples:

- `soliton boundary` ↔ `mass threshold / phase boundary`
- `domain` ↔ `energy range with fixed particle content`
- `run` ↔ `RG evolution`
- `integer rule` ↔ `beta coefficient / group-theory structure`

This means stored records should support:
- canonical name
- aliases
- HOWL term
- standard term

This is a metadata requirement, not merely a documentation preference.

---

## 4. Design Principles

### P1. JSON on disk is primary
All persistent data is stored as JSON:
- values
- experiments
- results
- diagram plans/results
- later: programs, catalogs, taxonomies

Python objects are runtime wrappers over JSON, not the master record.

### P2. Python is for execution only
Only executable logic lives in Python:
- derivation functions
- diagram renderers
- loaders
- resolvers
- validators
- experiment runners

### P3. Everything versioned
All versioned entities are append-only:
- values
- derivations
- experiment specs
- possibly diagram renderers

Old versions are never edited out of history.

### P4. Results are reusable inputs
Experiment results are data.
A later experiment may consume:
- constants
- derived values
- prior experiment outputs

### P5. Experiments declare dependencies explicitly
An experiment must declare:
- default version policy
- item-level version overrides
- derivations used
- diagrams planned
- checks expected

### P6. Diagrams are planned artifacts
Diagrams are not ad hoc script outputs.
They are declared in experiment JSON and recorded after production.

### P7. Low-tech Python 3.8
The implementation stays simple:
- Python 3.8+
- plain classes
- plain dicts/lists
- no dataclasses required
- no metaclasses
- no decorators except simple use if needed
- no advanced framework dependencies

### P8. Deterministic execution
Given the same JSON, derivation code, and platform version, the same experiment run must produce the same outputs.

---

## 5. What Is Superseded vs Inherited

## 5.1 Inherited from old script standards

These remain mandatory for executable derivation and diagram code:

- Python 3.8 compatibility
- no `math`
- no floats in the computation chain
- exact arithmetic via `Fraction` wherever the derivation is exact
- `mpf` only at display / numeric-comparison boundary
- `mp.dps = 100` standing precision
- `mp.nstr` for numeric rendering
- deterministic execution
- no hidden exception suppression around core computation
- explicit checks
- explicit units
- Python-only diagram generation

## 5.2 Superseded

These old rules are replaced:

- “scripts are the source of truth”
- “every workflow unit is a standalone demonstration script”
- “scripts do not create files”
- “diagrams are ad hoc Python outputs”
- mandatory wildcard import from `phys24_lib`

## 5.3 Replacement model

Replacements are:

- experiment JSON is the execution manifest
- result JSON is the persistent output record
- derivation modules are reusable indexed code
- diagram plans are part of experiments
- diagrams are generated from experiment data through registered renderers

---

## 6. High-Level Architecture

The system has four main layers.

## 6.1 Stored data layer
JSON files on disk for:
- values
- experiments
- results
- diagrams
- catalogs
- future program metadata

## 6.2 Executable derivation layer
Python modules containing versioned derivation functions.

## 6.3 Executable diagram layer
Python modules containing versioned diagram renderer functions.

## 6.4 Runtime orchestration layer
Python code that:
- loads JSON
- resolves version requests
- fetches inputs
- runs derivations
- executes checks
- writes results
- generates diagrams
- stores provenance

---

## 7. Persistent Data Domains

This first-pass spec defines the persistent domains, even though final object/class definitions are not frozen yet.

## 7.1 Value records
Versioned numeric or symbolic data items.

Examples:
- physical constants
- measured parameters
- exact geometric values
- group-theory integers/rationals
- reusable experiment outputs

## 7.2 Derivation records
Metadata describing executable derivations.

The executable function itself lives in Python, but its identity and metadata must be machine-readable.

## 7.3 Experiment records
JSON manifests describing:
- goal
- dependencies
- versions
- derivations to run
- checks
- planned diagrams

## 7.4 Result records
JSON records of actual experiment execution:
- resolved inputs
- versions used
- outputs produced
- checks passed/failed
- diagrams generated

## 7.5 Diagram plan records
Declared inside an experiment or stored separately by reference.
These specify intended visual outputs.

## 7.6 Diagram artifact records
Produced after execution.
These record:
- output path
- status
- variables used
- renderer version used

---

## 8. Provisional Object Model

Final Python object classes are not yet frozen. For now the required conceptual records are:

- `ValueRecord`
- `DerivationRecord`
- `ExperimentRecord`
- `ResultRecord`
- `DiagramPlan`
- `DiagramArtifact`
- `BoundaryRecord`
- `DomainRecord`
- `RepresentationRecord`
- `ResearchProgramRecord`

The exact class split may change, but the required fields and behaviors in this spec do not depend on final class names.

---

## 9. Storage Model

## 9.1 JSON-first rule

All persistent non-code artifacts must exist as JSON files on disk.

Python may load these into objects, but the JSON is authoritative.

## 9.2 Recommended directory layout

```text
DATA/
  HOWL-DATA-5-2026/
    code/
      data_5_runtime.py
      data_5_loader.py
      data_5_resolver.py
      data_5_runner.py
      data_5_checks.py
      data_5_json.py
      data_5_migrate.py

      derivations/
        qed_v0.py
        qed_v1.py
        ew_v0.py
        gut_v0.py
        domain_v0.py

      diagrams/
        running_v0.py
        mass_spectrum_v0.py
        domain_map_v0.py

      legacy/
        phys24_lib.py
        data_4_derivation_lib.py
        phys24_structure_lib.py
        phys24_boundary_map_lib.py
        phys24_domain_lib.py
        phys24_hubble_lib.py

    data/
      values/
        constants.json
        measured.json
        derived_values.json
        results_as_values.json

      experiments/
        experiment.beta_unification_scan_001.json
        experiment.qed_running_test_001.json

      results/
        result.beta_unification_scan_001.json
        result.qed_running_test_001.json

      catalogs/
        tags.json
        aliases.json
        namespaces.json
        object_index.json

      domains/
        boundaries.json
        domains.json
        representations.json

      programs/
        program.beta_unification.json

    artifacts/
      experiments/
        beta_unification_scan_001/
          running_couplings.png
          gap_scan.png
```

This layout is provisional, but the separation is mandatory:
- code in Python
- persistent records in JSON
- rendered artifacts in artifacts paths

---

## 10. Identity and Namespace Rules

## 10.1 Object ID rule
Every persistent record must have a stable lowercase `obj_id`.

Allowed characters:
- lowercase letters
- digits
- underscores
- dots

Examples:
- `value.const.alpha_inv`
- `value.result.beta_fit.alpha_s`
- `derivation.gut_gap_ratio`
- `experiment.beta_unification_scan_001`
- `result.beta_unification_scan_001`
- `boundary.mz`
- `domain.qed_perturbative`
- `diagram.running_couplings`

## 10.2 Alias rule
A record may also have aliases.

Examples:
- current derivation alias: `qed_alpha_em`
- specific version key: `qed_alpha_em_v0`

Aliases never replace canonical IDs.

## 10.3 Slug rule
All generated IDs and keys must be normalized by one shared sanitizer function.
No ad hoc string replacement logic is allowed in multiple places.

---

## 11. Versioning Model

## 11.1 General rule
Version chains are append-only.

Once a version exists, it is never:
- deleted
- edited in place
- renumbered

## 11.2 Value versioning
A value record contains:
- version 0 as original
- later versions appended
- current version equals latest by default

Typical semantics:
- `v0` = original imported or first accepted value
- `v1`, `v2`, ... = later updates or corrections
- latest alias returns highest version

## 11.3 Derivation versioning
Each derivation function has:
- explicit versioned key: `topic_name_v0`
- current alias: `topic_name`

The alias must point to the highest available version.

## 11.4 Experiment versioning
Experiments may themselves version over time if the spec changes.
At minimum, each experiment record must have:
- unique experiment ID
- experiment schema version
- execution version or revision number if rerun under changed settings

## 11.5 Result versioning
Results are immutable execution artifacts.
A rerun with changed dependencies should produce a new result record, not overwrite the old one.

---

## 12. Version Resolution Rules

An experiment must support both:
- a general default version policy
- item-level overrides

## 12.1 Resolution order

For any requested dependency:

1. If item-specific version is provided, use that.
2. Else if experiment default version is provided, use that.
3. Else use latest.

## 12.2 `None` / `null`
If the experiment default version is `null`, this means:
- use latest unless overridden

If an item version is `null`, this means:
- use latest for that item even if a default version is set

## 12.3 Scope of versioning
This resolution model applies to:
- values
- prior results used as inputs
- derivations
- diagram renderers if versioned explicitly

---

## 13. Value Record Specification

This is a provisional first-pass schema.

## 13.1 Required fields

```json
{
  "obj_id": "value.const.alpha_inv",
  "obj_type": "value",
  "name": "1/alpha",
  "category": "constant",
  "tags": ["EM", "coupling", "Level2", "CODATA"],
  "unit": "dimensionless",
  "versions": [
    {
      "version": 0,
      "value": "137035999177/1000000000",
      "value_type": "Fraction",
      "source": "CODATA 2022",
      "session": 4,
      "date": "2026-04-03",
      "uncertainty": null,
      "notes": ""
    }
  ],
  "current_version": 0
}
```

## 13.2 Required behavior

A value record must support:
- latest lookup
- specific-version lookup
- source/provenance per version
- classification tags
- unit
- exact storage of rational values as strings

## 13.3 Reusable results as values
If a result output becomes a reusable input later, it must be either:
- stored as a value record directly, or
- exposed through a uniform resolver that can fetch result outputs exactly like values

From the experiment runner’s point of view, both must be resolvable through one interface.

---

## 14. Derivation Registry Specification

## 14.1 Purpose
Derivations are executable Python functions with explicit machine-readable metadata.

Function code lives in Python.
Metadata may live:
- in Python dictionaries inside the same module, or
- in JSON plus Python linkage

First pass recommendation: keep metadata with the Python module.

## 14.2 Naming rule
All derivation keys use lowercase snake case.

Versioned form:
- `topic_name_v0`
- `topic_name_v1`

Latest alias:
- `topic_name`

## 14.3 Module grouping rule
All derivations for a given module version live together in one file.

Example:
- `gut_v0.py` contains all `gut_*_v0` derivations
- `gut_v1.py` contains all `gut_*_v1` derivations

## 14.4 Required indexes in each derivation module

```python
FUNCTION_INDEX = {}
DERIVATION_INDEX = {}
```

### `FUNCTION_INDEX`
Maps text key to callable.

### `DERIVATION_INDEX`
Maps text key to metadata dict.

## 14.5 Required derivation metadata fields

Each derivation metadata entry must provide:

- `key`
- `version`
- `module`
- `function_name`
- `inputs`
- `outputs`
- `description`
- `tags`
- `units_out`
- `arithmetic_mode`
- `requires`
- `valid_domains`
- `invalid_domains`
- `notes`

Example:

```python
DERIVATION_INDEX = {
    "qed_alpha_em_v0": {
        "key": "qed_alpha_em_v0",
        "version": 0,
        "module": "derivations.qed_v0",
        "function_name": "qed_alpha_em_v0",
        "inputs": ["value.const.alpha_inv"],
        "outputs": ["value.derived.alpha_em"],
        "description": "Compute alpha_em from inverse alpha",
        "tags": ["QED", "EM", "Level2"],
        "units_out": {"value.derived.alpha_em": "dimensionless"},
        "arithmetic_mode": "fraction_exact",
        "requires": [],
        "valid_domains": [],
        "invalid_domains": [],
        "notes": ""
    }
}
```

## 14.6 Input contract
A derivation must declare all required inputs explicitly.
It must not assume wildcard globals from a platform library.

Inputs are resolved by key through the runtime.

## 14.7 Output contract
A derivation must declare its output keys explicitly.
If it emits multiple values, those keys must be declared and stable.

---

## 15. Diagram Renderer Registry Specification

Diagrams follow the same indexing model as derivations.

## 15.1 Required indexes

```python
DIAGRAM_FUNCTION_INDEX = {}
DIAGRAM_INDEX = {}
```

## 15.2 Naming rule
Versioned:
- `running_couplings_v0`

Latest alias:
- `running_couplings`

## 15.3 Required diagram metadata fields

- `key`
- `version`
- `module`
- `function_name`
- `variables`
- `description`
- `diagram_type`
- `default_title`
- `default_units`
- `output_format`
- `notes`

## 15.4 Diagram function contract
A diagram renderer must:
- accept resolved variables and metadata
- produce declared output files
- return machine-readable artifact info
- not hardcode experiment-specific descriptions if they are supplied in JSON

The renderer defines how to plot.
The experiment JSON defines what to plot.

---

## 16. Experiment Record Specification

Experiments are central objects in the new architecture.

## 16.1 Experiment purpose
An experiment record declares:
- what question is being tested
- what derivations are used
- what data dependencies are used
- what versions are pinned
- what checks are expected
- what diagrams are desired

## 16.2 Required top-level fields

```json
{
  "obj_id": "experiment.beta_unification_scan_001",
  "obj_type": "experiment",
  "name": "Beta unification scan",
  "status": "ACTIVE",
  "thesis": "Test whether modified one-loop running improves coupling convergence.",
  "goals": [
    "Compute one-loop running with specified inputs",
    "Measure gap ratios",
    "Generate coupling running plots"
  ],
  "howl_principles": ["R1", "R2", "R5", "R9"],
  "default_version": null,
  "dependencies": {
    "values": {},
    "results": {},
    "derivations": {}
  },
  "execution_plan": [],
  "checks": [],
  "diagram_goals": [],
  "non_claims": [],
  "seeds": [],
  "notes": ""
}
```

## 16.3 Dependency section
The experiment must separately list:
- values
- prior results
- derivations
- optionally diagram renderers if pinning is needed

Example:

```json
"dependencies": {
  "values": {
    "value.const.alpha_inv": 0,
    "value.const.sin2_tW": null
  },
  "results": {
    "result.previous_scan.alpha_s_fit": 2
  },
  "derivations": {
    "gut_running": null,
    "gut_gap_ratio": 1
  },
  "diagram_renderers": {
    "running_couplings": null
  }
}
```

## 16.4 Execution plan
Experiments need an ordered execution plan, since some outputs become later inputs.

Each step should specify:
- step ID
- derivation key
- explicit inputs if overriding metadata defaults
- output binding names
- notes

## 16.5 Checks
Checks must be declared as structured data, not only printed output.

Check types should include:
- exact equality
- approximate agreement
- boolean condition
- precision reconstruction

This preserves the old script discipline in structured form.

## 16.6 Diagram goals
An experiment must be able to declare planned diagrams.

Each diagram goal should specify:
- diagram ID
- goal
- renderer key
- variables required
- title
- description
- output path
- formats

---

## 17. Result Record Specification

A result record is the immutable output of executing an experiment.

## 17.1 Required contents

A result record must include:

- result ID
- source experiment ID
- execution timestamp/session
- experiment revision used
- all resolved dependency versions
- derivation versions used
- values actually used
- outputs generated
- checks and statuses
- diagram artifacts and statuses
- overall pass/fail status

## 17.2 Resolved provenance requirement
The result record must preserve the exact dependency graph actually used at runtime.

Not just:
- “used alpha_inv”

but:
- “used `value.const.alpha_inv` version 0 from source CODATA 2022”

Not just:
- “used gut_running”

but:
- “used `gut_running_v1` from module `derivations.gut_v1`”

## 17.3 Reuse requirement
A result output must be addressable later as an input dependency.

---

## 18. Diagram Plan and Artifact Specification

## 18.1 Diagram plan
A diagram plan belongs to the experiment spec and declares intent.

Minimum fields:
- `diagram_id`
- `goal`
- `renderer`
- `variables`
- `title`
- `description`
- `output_path`
- `formats`

## 18.2 Diagram artifact
A diagram artifact belongs to the result record and declares what was actually produced.

Minimum fields:
- `diagram_id`
- `status`
- `renderer_resolved`
- `output_path`
- `variables_used`
- `description`
- `notes`

## 18.3 Description source rule
Diagram descriptions come from experiment/diagram JSON, not ad hoc code comments inside plotting scripts.

---

## 19. Runtime Resolution and Execution Flow

## 19.1 Boot sequence
The runtime must:

1. load catalogs and JSON records
2. load derivation indexes
3. load diagram indexes
4. build runtime resolver maps
5. validate referential integrity

## 19.2 Experiment execution sequence

1. load experiment JSON
2. resolve all declared dependencies by version
3. validate availability of required derivations
4. execute derivation plan in order
5. collect outputs
6. run structured checks
7. generate planned diagrams
8. write result JSON
9. optionally publish selected outputs as reusable values

## 19.3 Resolver requirement
There must be one central resolver API for:
- values
- result outputs
- derivations
- diagram renderers

This prevents fragmented lookup logic.

---

## 20. Arithmetic and Precision Rules

These are mandatory for executable code.

## 20.1 Exact chain
Exact derivations use:
- `Fraction` in
- `Fraction` out

## 20.2 Display / comparison boundary
Convert to `mpf` only when:
- printing
- doing approximate numeric checks
- comparing to mpf references

## 20.3 Precision
- standing precision: `mp.dps = 100`
- temporary higher precision allowed with save/restore

## 20.4 Prohibitions
Core code must not use:
- `math`
- float literals in the computation chain
- hidden coercion to float
- ad hoc local copies of constants that belong in stored data

---

## 21. Check System

The old script check philosophy remains, but checks become structured records.

## 21.1 Required check types
- `exact`
- `numeric`
- `bool`
- `precision`

## 21.2 Check record fields
Each check record should include:
- `tag`
- `check_type`
- `status`
- `got`
- `expected`
- `need`
- `detail`

## 21.3 Console output
The runner may still print a human-readable summary, but the canonical check output is JSON in the result record.

---

## 22. Domain and Boundary Semantics

The architecture must support domain-sensitive derivations.

## 22.1 Domains
A domain is a region where the active content and transformation law are fixed.

## 22.2 Boundaries
A boundary is a threshold where the transformation law changes.

## 22.3 Non-perturbative walls
The system must support explicit invalid regions such as the confinement wall.

This matters for:
- derivation validity metadata
- experiment scope statements
- result caveats
- diagram annotations

---

## 23. Metadata and Taxonomy

The following metadata families are required across the system.

## 23.1 Classification metadata
- `level_class`
- `theory_status`
- `perturbative_status`
- `domain_role`

## 23.2 Vocabulary metadata
- `howl_term`
- `standard_term`
- `aliases`

## 23.3 Search metadata
- `tags`
- `notes`
- `related_ids`

## 23.4 Provenance metadata
- `source`
- `session`
- `date`
- `derived_from`
- `used_by`

---

## 24. Compatibility with Legacy HOWL Libraries

## 24.1 Legacy libraries remain valid
Files like:
- `phys24_lib.py`
- `phys24_structure_lib.py`
- `phys24_boundary_map_lib.py`
- `phys24_domain_lib.py`

remain operational and are not replaced.

## 24.2 New role of legacy libraries
They become:
- migration sources
- cross-check references
- legacy derivation support
- compatibility layer inputs

## 24.3 Migration rule
Migration/import code should use normal module imports such as:

```python
import phys24_lib as p24
```

not wildcard imports inside functions.

## 24.4 Backward compatibility
Old flat scripts may continue to run.
New architecture does not break them.
But new primary work should target:
- JSON records
- derivation registries
- experiment manifests

---

## 25. Query and Search Requirements

The runtime must support query operations across stored records and runtime metadata.

Minimum required queries:

- get record by `obj_id`
- get value by key and version
- get latest derivation by alias
- get derivation by versioned key
- search by tag
- search by level
- search by domain/boundary role
- list experiments using a given value version
- list results produced from a given experiment
- list diagrams produced by an experiment

A reverse-usage query is especially important:
- “which experiments used `value.const.alpha_inv` version 0?”

That is one of the main reasons for explicit provenance.

---

## 26. Export and Serialization

## 26.1 JSON is native, not export-only
Unlike the old spec, JSON is not just an export format.
It is the canonical storage format.

## 26.2 Stable keys
Persistent schema keys must be append-only where practical:
- fields are added, not renamed away
- old fields retained for compatibility

## 26.3 Artifact path rule
Stored relative paths must be project-relative, not machine-absolute.

---

## 27. Implementation Guidance

## 27.1 Runtime style
Keep implementation plain and obvious:
- plain classes or dict wrappers
- module-level indexes
- explicit loaders
- explicit resolver functions
- no ORM
- no framework

## 27.2 Index maintenance
Any runtime index must be built centrally and recursively from loaded records.
No partial immediate-child-only indexing.

## 27.3 Validation
The system must validate:
- duplicate IDs
- broken references
- missing derivation keys
- missing value versions
- invalid experiment dependency declarations
- diagram plans referring to absent variables/renderers

---

## 28. Recommended Initial Build Phases

## Phase 1: Core JSON runtime
- JSON loader
- value store
- resolver
- version resolution
- result writing
- basic checks

## Phase 2: Derivation system
- derivation module registry
- execution plan runner
- structured outputs
- dependency trace recording

## Phase 3: Experiment system
- experiment schema
- check schema
- default and override version policies
- reusable result input support

## Phase 4: Diagram system
- diagram renderer registry
- diagram plan execution
- artifact records
- path tracking

## Phase 5: Physics-semantic layer
- boundary/domain records
- validity rules
- taxonomy catalogs
- HOWL/standard terminology mapping

## Phase 6: Legacy migration
- import constants from old libs
- import existing boundaries/domains/reps
- cross-verify old experiment outputs

---

## 29. Non-Goals for This Pass

This spec does not yet freeze:

- final Python class names
- final JSON filenames
- final namespace prefixes
- final category taxonomy for all derivations
- final object split between “value” and “result-as-value”
- final publication/export layers beyond JSON

Those will be resolved after the data objects are defined.

---

## 30. Immediate Open Questions for Next Step

These are the main unresolved design points:

1. Final persistent object taxonomy
- exactly which JSON object types are first-class?

2. Value/result unification
- should reusable results be promoted into the same value schema, or remain separate but resolver-compatible?

3. Derivation category taxonomy
- what are the correct domain/topic namespaces for all derivations?

4. Experiment execution plan shape
- how explicit should step wiring be versus inferred from derivation metadata?

5. Diagram renderer versioning
- should diagrams use the same alias/version rules as derivations? Recommended answer: yes.

6. Boundary/domain data structure
- should these be independent records or specialized value-linked records?

7. Catalog strategy
- one global index JSON vs runtime-built index only?

---

## 31. Summary

This first-pass spec defines the project as a JSON-first, versioned HOWL research runtime.

Core commitments are:

- persistent JSON records for data, experiments, results, and diagram plans
- Python-only executable derivations and diagrams
- append-only version chains
- explicit experiment dependency pinning
- reusable results as future inputs
- structured provenance
- deterministic exact-arithmetic execution
- support for both HOWL and standard physics terminology
- domains and boundaries as first-class semantic objects

The system is no longer “a better flat library.”
It is a versioned research operating system for physics work.

