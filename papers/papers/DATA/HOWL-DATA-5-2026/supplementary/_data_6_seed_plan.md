## DATA-6 DESIGN SPECIFICATION PLAN

*HOWL Series — Seed Document*
*Purpose: Architecture plan for the generalized object-connection-derivation system*

---

### 1. The Core Problem DATA-6 Solves

DATA-5 stores objects. 222 of them. But it doesn't store the relationships BETWEEN objects. The gap ratio 38/27 lives in const.gap_VL. The three betas that produce it live in beta.b1_mod, beta.b2_mod, beta.b3_mod. But the DERIVATION — the fact that you subtract b1 from b2, then divide by b2 minus b3 — is not stored anywhere. It's in the helper function. If you lose the helper function, you lose the derivation.

DATA-5 stores things. DATA-6 stores things AND how they connect.

---

### 2. The Three Object Types

Everything in the system is one of three types:

**ENTITY.** A thing that exists. A constant, a beta coefficient, a boundary, a representation, a dwarf galaxy, a research program. Has a value (or values). Has metadata. Has versions. Lives in its own JSON file.

**DERIVATION.** A computation that connects entities. Takes input entities, applies a named operation, produces output entities. The derivation itself is an object with its own JSON file. It records: what inputs, what operation, what outputs, what precision, what failures, what alternative paths exist.

**CONNECTION.** A structural relationship between entities that is NOT a derivation. Containment (electron is inside atom soliton), membership (Q_L is a member of generation 1), adjacency (bottom boundary is adjacent to charm boundary), cancellation (R2 cancels in K_J × R_K). Connections have types, and the type determines what operations are valid.

---

### 3. The File System

No master JSON file. No mega-database. Every concept gets its own directory with its own JSON files.

```
data6/
  entities/
    couplings/
      alpha_EM/
        alpha_EM.json          # current version + metadata
        alpha_EM_v0.json       # original value
        alpha_EM_v1.json       # updated value (if any)
      alpha_s/
        alpha_s.json
        alpha_s_v0.json
      sin2_tW/
        sin2_tW.json
        sin2_tW_v0.json
    betas/
      b1_SM/
        b1_SM.json
        b1_SM_v0.json
      b2_mod/
        b2_mod.json
        b2_mod_v0.json
    boundaries/
      electron/
        electron.json
      Z_boson/
        Z_boson.json
      confinement_wall/
        confinement_wall.json
    representations/
      Q_L/
        Q_L.json
      CD/
        CD.json
    constants/
      R2/
        R2.json
      pi/
        pi.json
    astrophysical/
      Draco/
        Draco.json
      Fornax/
        Fornax.json
  derivations/
    gap_ratio_SM/
      gap_ratio_SM.json        # inputs, operation, output, precision
    gap_ratio_CD/
      gap_ratio_CD.json
    alpha_s_1L/
      alpha_s_1L.json
    alpha_s_2L_full/
      alpha_s_2L_full.json
      alpha_s_2L_full_v0.json  # first attempt (500 steps)
      alpha_s_2L_full_v1.json  # second attempt (1000 steps)
    koide_m_tau/
      koide_m_tau.json
    dm_baryon_ratio/
      dm_baryon_ratio.json
    kepler_earth/
      kepler_earth.json
  connections/
    containment/
      electron_in_atom.json
      atom_in_crystal.json
      earth_in_solar.json
      sun_in_galaxy.json
    membership/
      Q_L_in_generation_1.json
      CD_in_BSM.json
    adjacency/
      bottom_to_charm.json
      Z_to_W.json
    cancellation/
      RC_product.json
      KJ_RK.json
    integer_source/
      YM_11_to_b3_SM.json
      YM_11_to_DM_baryon.json
      b2mod_13_to_Omega_DM.json
  programs/
    beta_unification/
      beta_unification.json
    cosmological/
      cosmological.json
    soliton_gravity/
      soliton_gravity.json
  evidence/
    scripts/
      beta_unification_test.json   # metadata about the script
      nested_soliton_gravity.json
    results/
      result_dm_baryon.json
      result_alpha_s_2L.json
    papers/
      DATA_5.json                  # what this paper claims, what backs it
      PHYS_24.json
  registry/
    index.json              # master lookup: ID -> type, name, version, path
    id_counter.json         # next available ID
    type_schema.json        # what fields each type requires
```

---

### 4. The ID System

Every object gets a permanent numeric ID. The ID never changes. Versions get their own IDs.

```
ID format: NNNNN (5-digit integer, zero-padded)

00001  alpha_EM (entity, v0)
00002  alpha_EM (entity, v1)  — if value updates
00003  alpha_s (entity, v0)
00004  sin2_tW (entity, v0)
...
00100  b1_SM (entity, v0)
00101  b2_SM (entity, v0)
...
00200  gap_ratio_SM (derivation, v0)
00201  gap_ratio_CD (derivation, v0)
...
00300  electron_in_atom (connection, v0)
00301  atom_in_crystal (connection, v0)
```

The registry/index.json maps every ID to:
- type (entity / derivation / connection)
- subtype (constant / beta / boundary / containment / etc.)
- name (human-readable)
- version (v0, v1, ...)
- path (relative to data6/)
- status (active / superseded / deprecated)
- created (session, date)

When you reference alpha_EM in a derivation, you reference ID 00001 (or 00002 if you want v1). The derivation JSON stores the IDs of its inputs and outputs. Every chain is traceable.

---

### 5. Entity JSON Schema

```json
{
  "id": 1,
  "type": "entity",
  "subtype": "coupling",
  "name": "alpha_EM",
  "display_name": "Electromagnetic fine structure constant",
  "value": {
    "fraction": {"numerator": 1, "denominator": 137035999177},
    "note": "stored as 1/alpha_inv, alpha_inv = 137035999177/1000000000"
  },
  "unit": "dimensionless",
  "level": 2,
  "tags": ["EM", "coupling", "CODATA", "Level2"],
  "source": "CODATA 2018",
  "data4_id": "B1",
  "digits": 10,
  "version": 0,
  "versions": [
    {"version": 0, "id": 1, "source": "CODATA 2018", "session": "Session 1"}
  ],
  "connected_derivations": [200, 205, 210, 215],
  "connected_entities": [3, 4],
  "connections": [
    {"type": "input_to", "derivation_id": 200, "role": "coupling at M_Z"},
    {"type": "measured_at", "boundary_id": 150, "note": "M_Z boundary"}
  ],
  "notes": "Inverse stored as Fraction 137035999177/1000000000 in phys24_lib",
  "created": {"session": 1, "date": "2026-03-28"}
}
```

---

### 6. Derivation JSON Schema

```json
{
  "id": 200,
  "type": "derivation",
  "subtype": "gap_ratio",
  "name": "gap_ratio_SM",
  "display_name": "SM gap ratio from beta coefficients",
  "operation": "(b1 - b2) / (b2 - b3)",
  "operation_code": "gap = (b1_val - b2_val) / (b2_val - b3_val)",
  "inputs": [
    {"id": 100, "name": "b1_SM", "role": "b1", "value": "41/10"},
    {"id": 101, "name": "b2_SM", "role": "b2", "value": "-19/6"},
    {"id": 102, "name": "b3_SM", "role": "b3", "value": "-7"}
  ],
  "outputs": [
    {"id": 160, "name": "gap_SM", "value": "218/115"}
  ],
  "precision": "exact (Fraction arithmetic)",
  "method": "one-step rational division",
  "level": 1,
  "tags": ["gap_ratio", "SM", "Level1", "exact"],
  "alternative_paths": [
    {
      "derivation_id": 201,
      "name": "gap_ratio_SM_via_decomposition",
      "note": "same result via gauge+higgs parts only (fermions cancel)"
    }
  ],
  "failures": [],
  "verified_by": [
    {"script": "data_4_derivation_lib.py", "check": "chk_exact", "status": "PASS"}
  ],
  "notes": "Fermion parts cancel: b1_ferm - b2_ferm = 4 - 4 = 0. Gap set by bosons only.",
  "version": 0,
  "created": {"session": 3, "date": "2026-04-01"}
}
```

---

### 7. Connection JSON Schema

```json
{
  "id": 300,
  "type": "connection",
  "subtype": "containment",
  "name": "electron_in_atom",
  "display_name": "Electron contained in atom soliton",
  "from_entity": {"id": 50, "name": "electron"},
  "to_entity": {"id": 51, "name": "atom"},
  "relationship": "is_contained_in",
  "reversible": false,
  "properties": {
    "binding_energy": "13.6 eV (hydrogen ground state)",
    "coupling_at_boundary": "alpha_EM = 1/137",
    "boundary_type": "EM soliton boundary",
    "excitation_energy": "ionization = 13.6 eV"
  },
  "nesting_level": 2,
  "nesting_chain": [300, 301, 302, 303],
  "notes": "Electron is bound by EM force. Removing it = ionization. The atom IS the soliton.",
  "tags": ["containment", "EM", "soliton", "nesting"],
  "version": 0,
  "mutable": true,
  "mutable_reason": "New intermediate layers could be discovered between electron and atom scale",
  "created": {"session": 4, "date": "2026-04-03"}
}
```

Connection subtypes:

| Subtype | Meaning | Example |
|---|---|---|
| containment | A is inside B's soliton | electron in atom, Earth in solar system |
| membership | A belongs to group B | Q_L in generation 1, CD in BSM sector |
| adjacency | A and B are neighboring boundaries | bottom ↔ charm, Z ↔ W |
| cancellation | R2 cancels in product of A and B | K_J × R_K, wire R × cap C |
| integer_source | integer N originates from entity A | 11 from Yang-Mills, 13 from b2_mod |
| produces | derivation A produces entity B | gap_ratio_SM produces gap_SM |
| consumes | derivation A uses entity B as input | gap_ratio_SM consumes b1_SM |
| equivalent | A and B are the same thing (different names) | 8*R2 = 2*pi |
| falsifies | evidence A would kill program B | DM particle detection kills soliton model |

---

### 8. The Nesting Hierarchy as Data

The 11-level soliton hierarchy from nested_soliton_gravity.py becomes a chain of containment connections:

```
proton_in_nucleus (id: 300)
nucleus_in_atom (id: 301)
atom_in_crystal (id: 302)
crystal_in_geological (id: 303)
human_on_earth (id: 304)
moon_in_earth_hill (id: 305)
earth_in_solar (id: 306)
solar_in_galaxy (id: 307)
galaxy_in_cluster (id: 308)
cluster_in_filament (id: 309)
filament_in_cosmological (id: 310)
```

Each connection stores: the coupling strength GM/(rc^2) at that level, the boundary type (Hill sphere, ionization, confinement), the escape velocity, the dominant force.

If we discover a middle layer — say, a sub-nuclear soliton between quark confinement and the proton — we insert a new connection (quark_in_subnuclear, subnuclear_in_proton) and renumber the chain. The old connections are not deleted. They get status: "superseded" and point to the new chain. Version history preserved.

---

### 9. Derivation Chains as Data

A derivation chain is a sequence of derivations where the output of one is the input of the next.

Example: predicting alpha_s at two loops.

```
Chain: alpha_s_2L_prediction
  Step 1: extract_couplings
    inputs: [alpha_inv (id:1), sin2_tW (id:4), alpha_s (id:3)]
    outputs: [inv_a1 (id:10), inv_a2 (id:11), inv_a3 (id:12)]
    
  Step 2: find_crossing_L
    inputs: [inv_a1 (id:10), inv_a2 (id:11), b1_mod (id:103), b2_mod (id:104)]
    outputs: [L_GUT_estimate (id:20)]
    
  Step 3: euler_two_loop_binary_search
    inputs: [inv_a1-3 (ids:10-12), b_mod (ids:103-105), bij_full (ids:130-138), L_est (id:20)]
    outputs: [L_GUT_2L (id:21), inv_a_GUT (id:22)]
    params: {n_steps: 500, bisections: 60}
    
  Step 4: run_back_to_MZ
    inputs: [inv_a_GUT (id:22), b_mod (ids:103-105), bij_full (ids:130-138), L_GUT_2L (id:21)]
    outputs: [alpha_s_pred (id:25)]
    
  Step 5: compare_to_measured
    inputs: [alpha_s_pred (id:25), alpha_s_measured (id:3)]
    outputs: [miss_pct (id:26)]
```

Alternative chains for the same prediction:

```
Chain: alpha_s_2L_SM_bij (uses SM b_ij instead of full)
  Same steps 1-5, but step 3-4 use bij_SM (ids:120-128) instead of bij_full
  Result: miss_pct slightly larger
  
Chain: alpha_s_1L (one-loop only, no Euler integration)
  Steps 1-2 only, then direct algebra
  Result: miss_pct ~ 13% (much worse)
```

All three chains stored. All three have their results. The system records which chain is best and why (full b_ij improves over SM b_ij which improves over one-loop).

---

### 10. Evidence and Papers as Objects

A script is evidence. A paper is a claim backed by evidence.

```json
{
  "id": 500,
  "type": "evidence",
  "subtype": "script",
  "name": "beta_unification_test",
  "file": "beta_unification_test.py",
  "checks_total": 20,
  "checks_pass": 19,
  "checks_fail": 1,
  "blocking": true,
  "blocking_reason": "statistical control not yet computed",
  "results_produced": [400, 401, 402, 403],
  "derivations_tested": [200, 201, 210, 215, 220],
  "version": 0,
  "last_run": {"session": 4, "date": "2026-04-03"}
}
```

```json
{
  "id": 600,
  "type": "evidence",
  "subtype": "paper",
  "name": "DATA-5",
  "title": "The Object-Oriented Platform: 222 Objects, One Integer Set",
  "claims": [
    {"claim": "222 objects across 9 types", "backed_by": [500, 501, 502]},
    {"claim": "DM/baryon = (22/13)*pi to 0.073%", "backed_by": [500, 400]},
    {"claim": "alpha_s predicted to <0.5% at two loops", "backed_by": [501, 401]}
  ],
  "does_not_claim": [
    "Statistical significance of integer coincidences",
    "First-principles derivation of amplification factor"
  ],
  "seeds": [
    "DATA-6 generalized object-connection system",
    "Statistical control script",
    "Three-loop alpha_s prediction"
  ],
  "version": 0
}
```

---

### 11. The Registry

One file that knows where everything lives:

```json
{
  "next_id": 700,
  "entries": {
    "1": {
      "type": "entity", "subtype": "coupling", "name": "alpha_EM",
      "version": 0, "status": "active",
      "path": "entities/couplings/alpha_EM/alpha_EM.json"
    },
    "2": {
      "type": "entity", "subtype": "coupling", "name": "alpha_EM",
      "version": 1, "status": "active",
      "path": "entities/couplings/alpha_EM/alpha_EM_v1.json"
    },
    "100": {
      "type": "entity", "subtype": "beta", "name": "b1_SM",
      "version": 0, "status": "active",
      "path": "entities/betas/b1_SM/b1_SM.json"
    },
    "200": {
      "type": "derivation", "subtype": "gap_ratio", "name": "gap_ratio_SM",
      "version": 0, "status": "active",
      "path": "derivations/gap_ratio_SM/gap_ratio_SM.json"
    },
    "300": {
      "type": "connection", "subtype": "containment", "name": "electron_in_atom",
      "version": 0, "status": "active",
      "path": "connections/containment/electron_in_atom.json"
    }
  }
}
```

The Python scripts read the registry, load the JSON files they need, do the computation, write results back as new JSON files, and update the registry.

---

### 12. What the Python Layer Does

Python is NOT the data. Python is the handler. It does 5 things:

1. **Load.** Read JSON files via the registry. Deserialize Fractions, reconstruct objects.

2. **Compute.** Run derivations. Exact Fraction arithmetic for derivation chains. mpf for numerical integration (two-loop Euler). Results written as new entity JSON files.

3. **Connect.** Create and update connection JSON files. Traverse containment chains. Find all derivations that use a given entity. Find all entities produced by a given derivation.

4. **Test.** Run verification scripts. Compare predicted values to measured values. Write result JSON files with PASS/FAIL status.

5. **Export.** Generate reports, tables, paper drafts from the JSON data. The JSON is the source of truth. The export is a view.

The Python scripts are evidence. The JSON files are data. If you delete all the Python, the JSON files still contain every value, every derivation, every connection, every result. A new session can read the JSON and rebuild the Python.

---

### 13. The Composition Rule

No entity lives alone. Everything composes.

alpha_EM composes with sin2_tW and alpha_s to produce inv_a1, inv_a2, inv_a3 (via the extract_couplings derivation).

inv_a1 and inv_a2 compose with b1_mod and b2_mod to produce L_GUT (via find_crossing_L).

L_GUT composes with M_Z to produce M_GUT (via L_to_scale).

Each composition is a derivation. Each derivation is an object. The chain of derivations IS the physics. If you follow the chain from alpha_s_pred back to its inputs, you pass through every entity that contributes. Nothing is hidden. Nothing is implicit.

The composition rule means: to understand any result, follow the derivation chain backwards. Every step is recorded. Every input is identified by ID. Every alternative path is listed.

---

### 14. The Mutability Rule

Connections are mutable. Entities are versioned. Derivations are append-only.

If we discover that the nesting hierarchy has a new layer, we don't delete the old containment connections. We mark them superseded and create new ones. Both versions exist. The registry tracks which is current.

If a measurement improves, we don't overwrite the old value. We create a new version. The old version persists. Both are referenceable by ID.

If a derivation is re-run with different parameters (more Euler steps, different bisection tolerance), the new run gets its own derivation object. Both exist. The system records which is more precise and why.

Nothing is ever deleted. Everything is tracked. This is how you build a research system that doesn't forget.

---

### 15. The Generalization

This system is not specific to particle physics. It is a general system for:

- Storing typed objects with versions
- Recording derivations as objects with inputs and outputs
- Recording structural relationships as typed connections
- Tracking evidence (scripts, papers) that backs claims
- Composing objects through derivation chains
- Traversing connection hierarchies (nesting, adjacency, cancellation)
- Maintaining alternative paths and their relative quality

The same system could hold: a chemistry knowledge base (molecules as entities, reactions as derivations, containment as connections), a software architecture (components as entities, data flows as derivations, dependencies as connections), or a historical research program (sources as entities, arguments as derivations, influences as connections).

The physics content is specific. The architecture is general.

---

### 16. What Must Be Built

In order of priority:

1. **The registry system.** index.json, id_counter.json, type_schema.json. The read/write Python functions. Test: create 10 entities, assign IDs, look them up.

2. **The entity JSON writer.** Take a phys24_lib constant, produce a well-formed entity JSON file in the right directory. Test: write alpha_EM, read it back, verify the Fraction value matches.

3. **The derivation JSON writer.** Take a derivation (gap ratio), produce a well-formed derivation JSON file that references input/output entity IDs. Test: write gap_ratio_SM, verify inputs are b1_SM/b2_SM/b3_SM, output is 218/115.

4. **The connection JSON writer.** Take a containment relationship, produce a well-formed connection JSON. Test: write electron_in_atom, verify from/to IDs resolve correctly.

5. **The chain traversal.** Given an entity, find all derivations that produce it. Given a derivation, find all entities it consumes. Given a containment connection, find the full nesting chain. Test: trace alpha_s_pred back to its measured inputs.

6. **The population script.** Convert all 222 DATA-5 objects into DATA-6 JSON files with IDs. This is the migration. Test: total entity count matches, all values preserved.

7. **The derivation population.** Record every derivation from the 4 helper chunks as derivation JSON files. Test: every helper function has a corresponding derivation object.

8. **The connection population.** Record every containment (soliton hierarchy), every cancellation (R2 registry), every integer source (11→b3, 13→b2_mod, etc.). Test: connection count matches expected.

9. **The test suite.** One script that loads every JSON file, runs every derivation, checks every result, produces PASS/FAIL. This replaces the 4 separate chunk test scripts.

10. **The statistical control script.** The BLOCKING item. This is the one computation that determines whether the integer coincidences are significant or a selection effect. It must be a DATA-6 derivation object with its own JSON, its own inputs, its own result.

---

### 17. What Must Not Be Built

- No GUI. JSON files are inspectable with any text editor.
- No ORM. Python reads JSON directly. No SQLAlchemy, no Django models.
- No web server. This is a file system, not a service.
- No complex inheritance. Three types: entity, derivation, connection. Subtypes are tags, not classes.
- No auto-discovery. The registry is explicit. If it's not in the registry, it doesn't exist.
- No implicit defaults. Every field in every JSON file is explicit. No "if missing, assume X."

---

### 18. Success Criteria for DATA-6

1. Every DATA-5 object has a corresponding DATA-6 entity JSON file with a permanent ID.
2. Every helper function computation has a corresponding derivation JSON file recording inputs, operation, outputs.
3. Every soliton nesting level has a containment connection. Every R2 cancellation has a cancellation connection. Every integer source has an integer_source connection.
4. The registry resolves any ID to its JSON file path in one lookup.
5. The test suite runs under 60 seconds and produces the same PASS/FAIL results as the DATA-5 chunk tests.
6. A new session can read the JSON files without any Python helper code and understand: what every value is, where it comes from, what it connects to, and what evidence backs it.
7. The statistical control script exists and has been run.

When all 7 criteria are met, DATA-6 is OPERATIONAL.

---

*This plan follows HOWL operational rules (Tables R.1-R.6).*
*Seeds: DATA-6 implementation, one item per build priority.*
*Blocking: statistical control script (item 10).*

**DATA-6 DESIGN SPECIFICATION: PLANNED.**

---

## DATA-6 DESIGN SPECIFICATION — PART B

*Derivations as Executable Python Mapped to JSON Index*

---

### 1. The Insight

Derivations are not strings. They are not JSON fields that say `"operation": "(b1 - b2) / (b2 - b3)"`. That's documentation. The actual derivation is Python code that runs, takes Fraction inputs, produces Fraction outputs, and either passes or fails.

But derivations are also not loose functions scattered across 4 chunk files. They are registered, indexed, versioned code with known inputs and known outputs, mapped to JSON metadata through the same ID system as everything else.

The derivation IS Python code. The derivation's identity, inputs, outputs, version, and connections are JSON. The mapping between them is a Python dict loaded from the JSON index.

---

### 2. The Module Structure

```
data6/
  derivations/
    __init__.py              # loads the registry, exposes lookup
    registry.py              # the dict: ID -> function reference
    
    couplings.py             # extract_couplings, derive_inv_a1, etc.
    gap_ratios.py            # gap_ratio, gap_ratio_SM, gap_ratio_CD
    one_loop.py              # find_crossing_L, run_one_loop, predict_alpha_s_1L
    two_loop.py              # euler_two_loop, predict_alpha_s_2L, predict_sin2_2L
    koide.py                 # koide_ratio, koide_amplitude_sq, koide_predict
    group_theory.py          # casimir_adj, casimir_fund, dynkin_fund, gauge_beta
    domains.py               # R2_area, airy_resolution, pipe_flow, wire_resistance...
    normalizations.py        # fourier_norm, gaussian_norm, bcs_gap, vena_contracta
    boundaries.py            # energy_to_distance, boundary_at_scale, traverse
    hubble.py                # hubble_required_r, hubble_running, test_F1
    gravity.py               # grav_coupling, escape_velocity, hill_sphere, kepler_period
    process_rate.py          # process_rate_ratio, gps_correction, muon_lifetime
    cosmology.py             # dm_baryon_ratio, omega_dm, amplification_factor
    dwarfs.py                # dwarf_purity, faber_jackson, tully_fisher
    
  index/
    derivation_index.json    # ID -> module.function + input IDs + output IDs
    entity_index.json        # ID -> entity path
    connection_index.json    # ID -> connection path
```

---

### 3. What a Derivation Module Looks Like

Each module is a plain Python file. No classes. Just functions. Every function that IS a derivation has a specific signature: it takes a loader (the thing that resolves IDs to values) and returns a result dict.

```python
# data6/derivations/gap_ratios.py

from fractions import Fraction


def gap_ratio(loader, b1_id, b2_id, b3_id):
    """Compute gap ratio from three beta coefficient IDs.
    gap = (b1 - b2) / (b2 - b3)
    
    Registered as derivation ID 2001.
    """
    b1 = loader.value(b1_id)   # returns Fraction
    b2 = loader.value(b2_id)
    b3 = loader.value(b3_id)
    
    result = (b1 - b2) / (b2 - b3)
    
    return {
        "value": result,
        "exact": True,
        "method": "fraction_division",
    }


def gap_ratio_SM(loader):
    """SM gap ratio. Derivation ID 2002.
    Inputs: b1_SM (1001), b2_SM (1002), b3_SM (1003).
    Output: 218/115.
    """
    return gap_ratio(loader, 1001, 1002, 1003)


def gap_ratio_CD(loader):
    """CD gap ratio. Derivation ID 2003.
    Inputs: b1_mod (1004), b2_mod (1005), b3_mod (1006).
    Output: 38/27.
    """
    return gap_ratio(loader, 1004, 1005, 1006)


def gap_distance(loader, b1_id, b2_id, b3_id, measured_id):
    """Distance from model gap to measured. Derivation ID 2004."""
    from mpmath import mpf
    from phys24_lib import f2m
    
    model = gap_ratio(loader, b1_id, b2_id, b3_id)
    measured = loader.value(measured_id)
    
    dist = abs(f2m(model["value"]) - f2m(measured))
    
    return {
        "value": dist,
        "exact": False,
        "method": "mpf_difference",
    }
```

The key: `loader` is the only interface to the data. The derivation function never imports phys24_lib constants directly. It asks the loader for values by ID. The loader reads from JSON. If the JSON changes, the derivation sees the new values. If the derivation changes, the JSON still has the old results from the old version.

---

### 4. The Loader

```python
# data6/derivations/__init__.py

import json
import os
from fractions import Fraction
from mpmath import mpf


class Loader:
    """Resolves entity IDs to values. Reads from JSON files."""
    
    def __init__(self, data_root):
        self._root = data_root
        self._cache = {}
        
        index_path = os.path.join(data_root, "index", "entity_index.json")
        with open(index_path) as f:
            self._entity_index = json.load(f)
    
    def value(self, entity_id):
        """Get the current value of an entity by ID.
        Returns Fraction for exact values, mpf for measured values.
        """
        sid = str(entity_id)
        
        if sid in self._cache:
            return self._cache[sid]
        
        if sid not in self._entity_index:
            return None
        
        entry = self._entity_index[sid]
        path = os.path.join(self._root, entry["path"])
        
        with open(path) as f:
            data = json.load(f)
        
        val = self._parse_value(data["value"])
        self._cache[sid] = val
        return val
    
    def _parse_value(self, val_dict):
        """Convert JSON value representation to Python type."""
        if "fraction" in val_dict:
            frac = val_dict["fraction"]
            return Fraction(frac["numerator"], frac["denominator"])
        if "mpf" in val_dict:
            return mpf(val_dict["mpf"])
        if "integer" in val_dict:
            return val_dict["integer"]
        return None
    
    def entity(self, entity_id):
        """Get the full entity dict (not just value)."""
        sid = str(entity_id)
        if sid not in self._entity_index:
            return None
        entry = self._entity_index[sid]
        path = os.path.join(self._root, entry["path"])
        with open(path) as f:
            return json.load(f)
```

---

### 5. The Registry: ID → Function

```python
# data6/derivations/registry.py

from data6.derivations import gap_ratios
from data6.derivations import couplings
from data6.derivations import one_loop
from data6.derivations import two_loop
from data6.derivations import koide
from data6.derivations import group_theory
from data6.derivations import domains
from data6.derivations import normalizations
from data6.derivations import boundaries
from data6.derivations import hubble
from data6.derivations import gravity
from data6.derivations import process_rate
from data6.derivations import cosmology
from data6.derivations import dwarfs


DERIVATION_REGISTRY = {
    # Couplings
    2000: {
        "function": couplings.extract_couplings,
        "name": "extract_couplings",
        "module": "couplings",
        "inputs": [1, 4, 3],           # alpha_inv, sin2_tW, alpha_s
        "outputs": [10, 11, 12],        # inv_a1, inv_a2, inv_a3
        "method": "exact_fraction",
    },
    
    # Gap ratios
    2001: {
        "function": gap_ratios.gap_ratio,
        "name": "gap_ratio",
        "module": "gap_ratios",
        "inputs": "variable",           # takes 3 beta IDs as args
        "outputs": "variable",
        "method": "exact_fraction",
    },
    2002: {
        "function": gap_ratios.gap_ratio_SM,
        "name": "gap_ratio_SM",
        "module": "gap_ratios",
        "inputs": [1001, 1002, 1003],   # b1_SM, b2_SM, b3_SM
        "outputs": [1060],              # gap_SM = 218/115
        "method": "exact_fraction",
    },
    2003: {
        "function": gap_ratios.gap_ratio_CD,
        "name": "gap_ratio_CD",
        "module": "gap_ratios",
        "inputs": [1004, 1005, 1006],   # b1_mod, b2_mod, b3_mod
        "outputs": [1061],              # gap_VL = 38/27
        "method": "exact_fraction",
    },
    
    # One-loop
    2010: {
        "function": one_loop.find_crossing_L,
        "name": "find_crossing_L",
        "module": "one_loop",
        "inputs": [10, 11, 1004, 1005], # inv_a1, inv_a2, b1_mod, b2_mod
        "outputs": [1070],              # L_GUT
        "method": "exact_fraction",
    },
    2011: {
        "function": one_loop.predict_alpha_s_1L,
        "name": "predict_alpha_s_1L",
        "module": "one_loop",
        "inputs": [10, 11, 12, 1004, 1005, 1006],
        "outputs": [1080],              # alpha_s_pred_1L
        "method": "exact_then_mpf",
    },
    
    # Two-loop
    2020: {
        "function": two_loop.predict_alpha_s_2L,
        "name": "predict_alpha_s_2L",
        "module": "two_loop",
        "inputs": [10, 11, 12, 1004, 1005, 1006, "bij_full_ids"],
        "outputs": [1081],
        "method": "euler_binary_search",
        "params": {"n_steps": 500, "bisections": 60},
    },
    
    # Koide
    2030: {
        "function": koide.koide_ratio,
        "name": "koide_ratio_leptons",
        "module": "koide",
        "inputs": [30, 31, 32],         # m_e, m_mu, m_tau
        "outputs": [1090],              # K_koide
        "method": "mpf_arithmetic",
    },
    2031: {
        "function": koide.koide_predict,
        "name": "koide_predict_m_tau",
        "module": "koide",
        "inputs": [30, 31],             # m_e, m_mu only
        "outputs": [1091],              # m_tau_pred
        "method": "quadratic_formula",
    },
    
    # Cosmology
    2050: {
        "function": cosmology.dm_baryon_ratio,
        "name": "dm_baryon_ratio",
        "module": "cosmology",
        "inputs": [1005, 50],           # b2_mod (for |num|=13), R2
        "outputs": [1100],              # (22/13)*pi
        "method": "fraction_times_R2",
    },
    2051: {
        "function": cosmology.omega_dm,
        "name": "omega_dm",
        "module": "cosmology",
        "inputs": [1005, 50],           # b2_mod, R2
        "outputs": [1101],              # (44/169)*R2
        "method": "fraction_times_R2",
    },
    
    # Gravity
    2060: {
        "function": gravity.kepler_period,
        "name": "kepler_period",
        "module": "gravity",
        "inputs": [50, "a_m", "M_kg"],  # R2 from db + runtime params
        "outputs": "runtime",
        "method": "sqrt_mpf",
    },
    2061: {
        "function": gravity.hill_sphere,
        "name": "hill_sphere",
        "module": "gravity",
        "inputs": ["m_kg", "M_kg", "a_m"],
        "outputs": "runtime",
        "method": "cube_root_mpf",
    },
    
    # ... ~160 total entries
}
```

---

### 6. The Derivation Index JSON

The registry dict above lives in Python for execution. But the SAME information also lives in JSON for inspection and LLM comprehension:

```json
{
  "2000": {
    "name": "extract_couplings",
    "module": "data6.derivations.couplings",
    "function": "extract_couplings",
    "inputs": [
      {"id": 1, "name": "alpha_inv", "role": "measured coupling"},
      {"id": 4, "name": "sin2_tW", "role": "measured mixing angle"},
      {"id": 3, "name": "alpha_s", "role": "measured strong coupling"}
    ],
    "outputs": [
      {"id": 10, "name": "inv_a1", "role": "GUT-normalized U(1)"},
      {"id": 11, "name": "inv_a2", "role": "GUT-normalized SU(2)"},
      {"id": 12, "name": "inv_a3", "role": "GUT-normalized SU(3)"}
    ],
    "method": "exact_fraction",
    "level": 1,
    "pitfalls": ["PHYS-30: 1/a2 = sin2*alpha_inv NOT alpha_inv/sin2"],
    "version": 0,
    "verified_by": ["data_5_chunk1_test.py"],
    "status": "active"
  },
  "2002": {
    "name": "gap_ratio_SM",
    "module": "data6.derivations.gap_ratios",
    "function": "gap_ratio_SM",
    "inputs": [
      {"id": 1001, "name": "b1_SM", "value": "41/10"},
      {"id": 1002, "name": "b2_SM", "value": "-19/6"},
      {"id": 1003, "name": "b3_SM", "value": "-7"}
    ],
    "outputs": [
      {"id": 1060, "name": "gap_SM", "value": "218/115"}
    ],
    "method": "exact_fraction",
    "level": 1,
    "notes": "Fermions cancel: b1_ferm - b2_ferm = 0. Gap set by bosons only.",
    "version": 0,
    "status": "active"
  }
}
```

The Python registry.py is generated FROM this JSON, or kept in sync with it. The JSON is what an LLM reads to understand the system. The Python is what executes.

---

### 7. How Execution Works

```python
# Running a derivation by ID

from data6.derivations import Loader
from data6.derivations.registry import DERIVATION_REGISTRY

loader = Loader("data6/")

# Run gap_ratio_SM
deriv = DERIVATION_REGISTRY[2002]
result = deriv["function"](loader)

print(result["value"])  # Fraction(218, 115)
print(result["exact"])  # True
```

```python
# Running a derivation chain: alpha_s 2L prediction

# Step 1: extract couplings
couplings = DERIVATION_REGISTRY[2000]["function"](loader)

# Step 2: find crossing L
L_GUT = DERIVATION_REGISTRY[2010]["function"](loader)

# Step 3: two-loop prediction
alpha_s_pred = DERIVATION_REGISTRY[2020]["function"](loader, bij_tag="full")

print(alpha_s_pred["value"])   # mpf ~0.1179
print(alpha_s_pred["miss_pct"])  # mpf <0.5
```

```python
# Running ALL derivations and collecting results

results = {}
for deriv_id, deriv in DERIVATION_REGISTRY.items():
    fn = deriv["function"]
    try:
        # Fixed-input derivations (inputs are entity IDs, baked in)
        if deriv["inputs"] != "variable":
            result = fn(loader)
            results[deriv_id] = {"status": "PASS", "result": result}
        else:
            results[deriv_id] = {"status": "SKIP", "reason": "variable inputs"}
    except Exception as e:
        results[deriv_id] = {"status": "FAIL", "error": str(e)}
```

---

### 8. How Data Changes Route to Correct Code

Scenario: Planck 2025 revises alpha_s from 0.118 to 0.1175.

1. Create new entity file: `entities/couplings/alpha_s/alpha_s_v1.json` with the new Fraction.

2. Update entity_index.json: ID 3 now points to v1 path. Old v0 gets ID 3000 (archived).

3. Run all derivations that consume ID 3. The loader sees the new value. The derivation code is unchanged. The results change because the inputs changed.

4. New result JSON files are written with the updated predictions. The old result JSON files remain (versioned).

5. The derivation_index.json is unchanged — the code didn't change, only the data did.

Scenario: we find a better two-loop integration method (RK4 instead of Euler).

1. Write new function `predict_alpha_s_2L_rk4` in `two_loop.py`.

2. Register it as derivation ID 2021 (new ID, Euler version stays at 2020).

3. Both exist. Both can run. Both produce results. The derivation_index.json records both, with notes on which is more precise.

4. Results from 2020 (Euler) and 2021 (RK4) are both stored. A comparison derivation (ID 2022) can compute the difference.

---

### 9. How an LLM Uses This System

A new Claude session receives:

1. The derivation_index.json — reads it, understands every computation, its inputs, outputs, pitfalls.

2. The entity_index.json — reads it, knows every constant and where it lives.

3. The connection_index.json — reads it, understands containment, cancellations, integer sources.

4. The Python modules — reads them, understands the actual code.

To add a new computation:

1. Write the Python function in the appropriate module.
2. Assign the next available derivation ID.
3. Add the entry to derivation_index.json with inputs, outputs, method, pitfalls.
4. Add the entry to registry.py mapping ID → function.
5. Write a test that runs the derivation and checks the output.
6. Run the test. PASS/FAIL recorded as a result entity.

The LLM can do all 6 steps because the system is self-describing. The JSON tells it what exists. The Python tells it how to compute. The registry connects them.

---

### 10. The Function Signature Contract

Every derivation function follows one of three signatures:

**Type A: Fixed inputs (most common).** The function knows its input IDs. It takes only a loader.

```python
def gap_ratio_SM(loader):
    b1 = loader.value(1001)
    b2 = loader.value(1002)
    b3 = loader.value(1003)
    return {"value": (b1 - b2) / (b2 - b3), "exact": True}
```

**Type B: Parameterized inputs.** The function takes a loader plus entity IDs as arguments. Used for generic computations.

```python
def gap_ratio(loader, b1_id, b2_id, b3_id):
    b1 = loader.value(b1_id)
    b2 = loader.value(b2_id)
    b3 = loader.value(b3_id)
    return {"value": (b1 - b2) / (b2 - b3), "exact": True}
```

**Type C: Runtime parameters.** The function takes a loader plus non-ID parameters. Used for computations with physical inputs not in the database.

```python
def kepler_period(loader, a_m, M_kg):
    R2 = loader.value(50)  # R2 from db
    a = mpf(str(a_m))
    M = mpf(str(M_kg))
    T = msqrt(mpf("64") * R2 ** 2 * a ** 3 / (G * M))
    return {"value": T, "exact": False, "method": "mpf_sqrt"}
```

The registry records which type each derivation is. Type A derivations can be run automatically (no arguments needed). Type B and C require the caller to provide arguments.

---

### 11. The Return Contract

Every derivation function returns a dict with at minimum:

```python
{
    "value": <Fraction or mpf>,     # the computed result
    "exact": <bool>,                 # True if Fraction arithmetic throughout
    "method": <string>,              # how it was computed
}
```

Optional fields:

```python
{
    "miss_pct": <mpf>,              # if compared to measured value
    "inputs_used": {<id>: <value>}, # for traceability
    "alternative_value": <...>,      # if multiple results (e.g., quadratic roots)
    "params": {<key>: <val>},        # if numerical method used
    "notes": <string>,               # pitfalls, caveats
}
```

---

### 12. The Sync Rule

The derivation_index.json and registry.py must always agree. If a function exists in a module but is not in the registry, it is not a derivation — it is a utility. If an entry exists in the registry but the function is missing, the system reports an error.

The sync check is itself a test:

```python
def test_registry_sync():
    """Every registry entry must resolve to a callable function."""
    for deriv_id, entry in DERIVATION_REGISTRY.items():
        fn = entry["function"]
        if not callable(fn):
            print("[FAIL] ID %d: function not callable" % deriv_id)
        else:
            print("[PASS] ID %d: %s.%s" % (
                deriv_id, entry["module"], fn.__name__))
```

---

### 13. ID Allocation Blocks

To keep IDs organized and prevent collisions:

| Block | Range | Type | Content |
|---|---|---|---|
| 1-99 | 1-99 | entity | SI constants, measured couplings |
| 100-199 | 100-199 | entity | Derived couplings, intermediate values |
| 200-499 | 200-499 | entity | Q335 transcendentals |
| 500-699 | 500-699 | entity | Masses (quarks, leptons, bosons) |
| 1000-1099 | 1000-1099 | entity | Beta coefficients (SM, VL, mod) |
| 1100-1199 | 1100-1199 | entity | Two-loop b_ij matrices |
| 1200-1399 | 1200-1399 | entity | Representations |
| 1400-1599 | 1400-1599 | entity | Boundaries |
| 1600-1799 | 1600-1799 | entity | R2 domains |
| 1800-1899 | 1800-1899 | entity | R2 cancellations |
| 1900-1999 | 1900-1999 | entity | Moduli |
| 2000-2499 | 2000-2499 | derivation | All derivation functions |
| 3000-3499 | 3000-3499 | connection | Containment |
| 3500-3999 | 3500-3999 | connection | Membership, adjacency |
| 4000-4499 | 4000-4499 | connection | Cancellations, integer sources |
| 5000-5499 | 5000-5499 | evidence | Scripts, results |
| 5500-5999 | 5500-5999 | evidence | Papers, claims |
| 9000-9999 | 9000-9999 | archived | Superseded versions |

---

### 14. What This Gives Us That DATA-5 Doesn't

DATA-5: "The gap ratio is 38/27." You trust it because the test passed.

DATA-6: "The gap ratio is 38/27. It was computed by derivation 2003 (gap_ratio_CD), which called gap_ratios.gap_ratio_CD in data6/derivations/gap_ratios.py, which consumed entities 1004 (b1_mod = 62/15), 1005 (b2_mod = -13/6), and 1006 (b3_mod = -20/3), applied (b1-b2)/(b2-b3) in exact Fraction arithmetic, and produced entity 1061. The derivation has 0 failures across 4 sessions. An alternative derivation 2004 computed the same result via the boson decomposition (gauge+higgs only, fermions cancel). Both agree exactly. The result is verified by script evidence 5002 (data_5_chunk1_test.py, PASS)."

Every claim traces to code, data, and evidence. An LLM can follow the chain. A human can follow the chain. The chain is the proof.

---

*Part B adds to Part A. The combined specification covers: file system (Part A §3), ID system (Part A §4), entity schema (Part A §5), derivation schema (Part B §6), connection schema (Part A §7), the loader (Part B §4), the registry (Part B §5), execution (Part B §7), data routing (Part B §8), LLM usage (Part B §9), function contracts (Part B §10-11), ID allocation (Part B §13).*

**DATA-6 DESIGN SPECIFICATION PART B: PLANNED.**

---

```
data6/
│
├── index/
│   ├── entity_index.json              # ID -> entity path, type, name, version, status
│   ├── derivation_index.json          # ID -> module.function, inputs, outputs, method
│   ├── connection_index.json          # ID -> connection path, subtype, from/to
│   ├── evidence_index.json            # ID -> script/paper path, checks, status
│   ├── id_counter.json                # {"next_id": NNNNN}
│   └── type_schema.json               # required fields per type/subtype
│
├── entities/
│   ├── si_constants/
│   │   ├── c/c.json                                # 299792458 m/s exact
│   │   ├── h/h.json                                # Planck constant exact
│   │   ├── e_charge/e_charge.json                  # elementary charge exact
│   │   ├── k_B/k_B.json                            # Boltzmann exact
│   │   ├── N_A/N_A.json                            # Avogadro exact
│   │   ├── dv_Cs/dv_Cs.json                        # 9192631770 Hz exact
│   │   └── K_cd/K_cd.json                          # luminous efficacy exact
│   │
│   ├── couplings/
│   │   ├── alpha_inv/
│   │   │   ├── alpha_inv.json                      # 137035999177/1000000000
│   │   │   └── alpha_inv_v0.json
│   │   ├── sin2_tW/
│   │   │   ├── sin2_tW.json                        # 11561/50000
│   │   │   └── sin2_tW_v0.json
│   │   ├── alpha_s/
│   │   │   ├── alpha_s.json                        # 59/500
│   │   │   └── alpha_s_v0.json
│   │   ├── inv_a1/inv_a1.json                      # derived GUT U(1)
│   │   ├── inv_a2/inv_a2.json                      # derived GUT SU(2)
│   │   └── inv_a3/inv_a3.json                      # derived GUT SU(3)
│   │
│   ├── masses/
│   │   ├── m_e/m_e.json                            # 0.51099895 MeV
│   │   ├── m_mu/m_mu.json                          # 105.6583745 MeV
│   │   ├── m_tau/m_tau.json                         # 1776.86 MeV
│   │   ├── m_u/m_u.json                            # 2.16 MeV
│   │   ├── m_d/m_d.json                            # 4.67 MeV
│   │   ├── m_s/m_s.json                            # 93.4 MeV
│   │   ├── m_c/m_c.json                            # 1270 MeV
│   │   ├── m_b/m_b.json                            # 4180 MeV
│   │   ├── m_t/m_t.json                            # 173000 MeV
│   │   ├── M_Z/M_Z.json                            # 91187.6 MeV
│   │   ├── M_W/M_W.json                            # 80379 MeV
│   │   └── M_H/M_H.json                            # 125100 MeV
│   │
│   ├── q335/
│   │   ├── pi/pi.json                              # Q335 rational, 100 digits
│   │   ├── pi2/pi2.json
│   │   ├── pi3/pi3.json
│   │   ├── pi4/pi4.json
│   │   ├── e/e.json
│   │   ├── epi/epi.json                            # e^pi
│   │   ├── ln2/ln2.json
│   │   ├── ln3/ln3.json
│   │   ├── ln5/ln5.json
│   │   ├── ln7/ln7.json
│   │   ├── ln10/ln10.json
│   │   ├── ln2_2/ln2_2.json                        # ln(2)^2
│   │   ├── ln2_4/ln2_4.json                        # ln(2)^4
│   │   ├── sqrt2/sqrt2.json
│   │   ├── sqrt3/sqrt3.json
│   │   ├── sqrt5/sqrt5.json
│   │   ├── sqrt7/sqrt7.json
│   │   ├── phi/phi.json                            # golden ratio
│   │   ├── zeta2/zeta2.json                        # pi^2/6
│   │   ├── zeta3/zeta3.json                        # Apéry
│   │   ├── zeta5/zeta5.json                        # Borwein
│   │   ├── zeta7/zeta7.json
│   │   ├── zeta9/zeta9.json
│   │   ├── li4/li4.json                            # Li4(1/2)
│   │   ├── li5/li5.json
│   │   ├── li6/li6.json
│   │   ├── li7/li7.json
│   │   ├── catalan/catalan.json
│   │   ├── K_quarter/K_quarter.json                # K(k^2=1/4)
│   │   ├── K_half/K_half.json                      # K(k^2=1/2)
│   │   ├── K_three_quarter/K_three_quarter.json    # K(k^2=3/4)
│   │   ├── E_quarter/E_quarter.json                # E(k^2=1/4)
│   │   ├── E_half/E_half.json                      # E(k^2=1/2)
│   │   ├── E_three_quarter/E_three_quarter.json    # E(k^2=3/4)
│   │   ├── Cl2_pi3/Cl2_pi3.json                    # Clausen Cl2(pi/3)
│   │   └── Q335_denominator/Q335_denominator.json  # 2^335
│   │
│   ├── geometric/
│   │   ├── R2/R2.json                              # pi/4
│   │   ├── R4/R4.json                              # pi^2/32
│   │   ├── twopi/twopi.json                        # 2*pi
│   │   ├── fourpi/fourpi.json                      # 4*pi (rarely used directly)
│   │   └── bessel/
│   │       ├── j01/j01.json                        # 2.40483 (J0 first zero)
│   │       └── j11/j11.json                        # 3.83171 (J1 first zero)
│   │
│   ├── group_theory/
│   │   ├── C2_adj_SU3/C2_adj_SU3.json              # 3
│   │   ├── C2_adj_SU2/C2_adj_SU2.json              # 2
│   │   ├── C2_fund_SU3/C2_fund_SU3.json            # 4/3
│   │   ├── C2_fund_SU2/C2_fund_SU2.json            # 3/4
│   │   ├── S2_fund/S2_fund.json                    # 1/2
│   │   ├── k1_GUT/k1_GUT.json                      # 3/5
│   │   ├── k1_inv/k1_inv.json                      # 5/3
│   │   ├── N_gen/N_gen.json                        # 3
│   │   ├── gauge_coeff/gauge_coeff.json            # -11/3
│   │   └── per_gen_shift/per_gen_shift.json        # (4/3, 4/3, 4/3)
│   │
│   ├── betas/
│   │   ├── b1_SM/b1_SM.json                        # 41/10
│   │   ├── b2_SM/b2_SM.json                        # -19/6
│   │   ├── b3_SM/b3_SM.json                        # -7
│   │   ├── db1_VL/db1_VL.json                      # 1/15
│   │   ├── db2_VL/db2_VL.json                      # 1
│   │   ├── db3_VL/db3_VL.json                      # 1/3
│   │   ├── b1_mod/b1_mod.json                      # 62/15
│   │   ├── b2_mod/b2_mod.json                      # -13/6
│   │   └── b3_mod/b3_mod.json                      # -20/3
│   │
│   ├── two_loop/
│   │   ├── bij_SM_00/bij_SM_00.json                # 199/50
│   │   ├── bij_SM_01/bij_SM_01.json                # 27/10
│   │   ├── bij_SM_02/bij_SM_02.json                # 44/5
│   │   ├── bij_SM_10/bij_SM_10.json                # 9/10
│   │   ├── bij_SM_11/bij_SM_11.json                # 35/6
│   │   ├── bij_SM_12/bij_SM_12.json                # 12
│   │   ├── bij_SM_20/bij_SM_20.json                # 11/10
│   │   ├── bij_SM_21/bij_SM_21.json                # 9/2
│   │   ├── bij_SM_22/bij_SM_22.json                # -26
│   │   ├── dbij_VL_00/dbij_VL_00.json              # 7/15
│   │   ├── dbij_VL_01/dbij_VL_01.json              # 1/15
│   │   ├── dbij_VL_02/dbij_VL_02.json              # 16/135
│   │   ├── dbij_VL_10/dbij_VL_10.json              # 1/30
│   │   ├── dbij_VL_11/dbij_VL_11.json              # 15/4 (NOT 39/4)
│   │   ├── dbij_VL_12/dbij_VL_12.json              # 8/3
│   │   ├── dbij_VL_20/dbij_VL_20.json              # 1/45
│   │   ├── dbij_VL_21/dbij_VL_21.json              # 1
│   │   └── dbij_VL_22/dbij_VL_22.json              # 40/9
│   │
│   ├── representations/
│   │   ├── Q_L/Q_L.json                            # (3,2,1/6) chiral
│   │   ├── u_R/u_R.json                            # (3,1,2/3) chiral
│   │   ├── d_R/d_R.json                            # (3,1,-1/3) chiral
│   │   ├── L_L/L_L.json                            # (1,2,-1/2) chiral
│   │   ├── e_R/e_R.json                            # (1,1,-1) chiral
│   │   └── CD/CD.json                              # (3,2,1/6) vector-like
│   │
│   ├── boundaries/
│   │   ├── planck/planck.json
│   │   ├── gut/gut.json
│   │   ├── cd_threshold/cd_threshold.json
│   │   ├── top/top.json
│   │   ├── higgs/higgs.json
│   │   ├── Z_boson/Z_boson.json
│   │   ├── W_boson/W_boson.json
│   │   ├── bottom/bottom.json
│   │   ├── tau/tau.json
│   │   ├── charm/charm.json
│   │   ├── confinement_upper/confinement_upper.json
│   │   ├── confinement_lower/confinement_lower.json
│   │   ├── strange/strange.json
│   │   ├── muon/muon.json
│   │   ├── pion/pion.json
│   │   ├── electron/electron.json
│   │   ├── neutrino_tau/neutrino_tau.json
│   │   ├── neutrino_mu/neutrino_mu.json
│   │   └── neutrino_e/neutrino_e.json
│   │
│   ├── gap_ratios/
│   │   ├── gap_SM/gap_SM.json                      # 218/115
│   │   ├── gap_VL/gap_VL.json                      # 38/27
│   │   ├── gap_MSSM/gap_MSSM.json                  # 5/7
│   │   └── gap_measured/gap_measured.json           # ~1.358
│   │
│   ├── koide/
│   │   ├── K_koide/K_koide.json                    # ~0.66666
│   │   ├── a2_lep/a2_lep.json                      # ~1.99996
│   │   └── m_tau_pred/m_tau_pred.json               # 1776.97 MeV
│   │
│   ├── cosmological/
│   │   ├── DM_baryon_ratio/DM_baryon_ratio.json    # (22/13)*pi
│   │   ├── Omega_DM/Omega_DM.json                  # (44/169)*R2
│   │   ├── Omega_b/Omega_b.json
│   │   ├── Omega_matter/Omega_matter.json
│   │   └── Omega_DE/Omega_DE.json
│   │
│   ├── domains/
│   │   ├── pipe_flow/pipe_flow.json
│   │   ├── drag_force/drag_force.json
│   │   ├── orifice_flow/orifice_flow.json
│   │   ├── capacitor/capacitor.json
│   │   ├── poynting/poynting.json
│   │   ├── antenna/antenna.json
│   │   ├── beam/beam.json
│   │   ├── thermal/thermal.json
│   │   ├── sound/sound.json
│   │   ├── wire/wire.json
│   │   ├── speaker/speaker.json
│   │   ├── fiber/fiber.json
│   │   ├── disc/disc.json
│   │   ├── wafer/wafer.json
│   │   ├── gaussian/gaussian.json
│   │   ├── kepler/kepler.json
│   │   ├── v_number/v_number.json
│   │   ├── helmholtz/helmholtz.json
│   │   ├── fspl/fspl.json
│   │   ├── litho/litho.json
│   │   ├── fourier_norm/fourier_norm.json
│   │   ├── gaussian_norm/gaussian_norm.json
│   │   └── bcs/bcs.json
│   │
│   ├── cancellations/
│   │   ├── KJ_RK/KJ_RK.json                       # (2e/h)(h/e^2) = 2/e
│   │   ├── G0_RK/G0_RK.json                       # CANCELS -> 2
│   │   ├── Rydberg/Rydberg.json
│   │   ├── Bohr_alpha/Bohr_alpha.json
│   │   ├── Hartree/Hartree.json
│   │   ├── Phi0_RK/Phi0_RK.json
│   │   ├── RC_product/RC_product.json
│   │   ├── Omega_DM_product/Omega_DM_product.json
│   │   ├── DM_baryon_sq/DM_baryon_sq.json
│   │   ├── gap_ratio_cancel/gap_ratio_cancel.json
│   │   └── generation_cancel/generation_cancel.json
│   │
│   ├── moduli/
│   │   ├── mod_R2/mod_R2.json                      # pi/4
│   │   ├── mod_R4/mod_R4.json                      # pi^2/32
│   │   ├── mod_alpha/mod_alpha.json
│   │   ├── mod_sin2/mod_sin2.json
│   │   ├── mod_alpha_s/mod_alpha_s.json
│   │   ├── mod_K_koide/mod_K_koide.json
│   │   ├── mod_gap_SM/mod_gap_SM.json
│   │   ├── mod_gap_VL/mod_gap_VL.json
│   │   ├── mod_vena_contracta/mod_vena_contracta.json
│   │   ├── mod_bcs_gap/mod_bcs_gap.json
│   │   ├── mod_Omega_DM/mod_Omega_DM.json
│   │   ├── mod_DM_baryon/mod_DM_baryon.json
│   │   ├── mod_1_minus_r/mod_1_minus_r.json
│   │   ├── mod_fourier/mod_fourier.json
│   │   ├── mod_gaussian/mod_gaussian.json
│   │   └── mod_kepler/mod_kepler.json
│   │
│   ├── engineering/
│   │   ├── discs/
│   │   │   ├── CD/CD.json                          # 780nm, NA=0.45
│   │   │   ├── DVD/DVD.json                        # 650nm, NA=0.60
│   │   │   └── Blu_ray/Blu_ray.json                # 405nm, NA=0.85
│   │   ├── fiber/
│   │   │   └── SMF_28/SMF_28.json                  # MFD, NA, cutoff
│   │   ├── speakers/
│   │   │   ├── 12inch/12inch.json                  # d=0.305m
│   │   │   ├── 10inch/10inch.json
│   │   │   ├── 8inch/8inch.json
│   │   │   ├── 6inch/6inch.json
│   │   │   ├── 5inch/5inch.json
│   │   │   └── 1inch/1inch.json
│   │   ├── wire/
│   │   │   ├── AWG_0000/AWG_0000.json
│   │   │   ├── AWG_0/AWG_0.json
│   │   │   ├── AWG_4/AWG_4.json
│   │   │   ├── AWG_8/AWG_8.json
│   │   │   ├── AWG_10/AWG_10.json
│   │   │   ├── AWG_12/AWG_12.json
│   │   │   ├── AWG_14/AWG_14.json
│   │   │   ├── AWG_18/AWG_18.json
│   │   │   ├── AWG_22/AWG_22.json
│   │   │   ├── AWG_24/AWG_24.json
│   │   │   ├── AWG_30/AWG_30.json
│   │   │   └── AWG_36/AWG_36.json
│   │   ├── materials/
│   │   │   ├── Cu_resistivity/Cu_resistivity.json  # 1.7241e-8 ohm*m
│   │   │   ├── epsilon_0/epsilon_0.json            # 8.8541878128e-12 F/m
│   │   │   ├── sigma_SB/sigma_SB.json              # Stefan-Boltzmann
│   │   │   └── gamma_EM/gamma_EM.json              # Euler-Mascheroni
│   │   ├── rf/
│   │   │   ├── GPS_L1/GPS_L1.json                  # 1575.42 MHz
│   │   │   ├── GPS_L2/GPS_L2.json                  # 1227.60 MHz
│   │   │   └── GPS_base/GPS_base.json              # 10.23 MHz
│   │   ├── semiconductor/
│   │   │   ├── EUV_wavelength/EUV_wavelength.json  # 13.5 nm
│   │   │   ├── ArF_wavelength/ArF_wavelength.json  # 193 nm
│   │   │   └── wafer_300mm/wafer_300mm.json
│   │   ├── audio/
│   │   │   ├── sample_rates/sample_rates.json       # CD=44100, etc.
│   │   │   └── just_intonation/just_intonation.json # 3/2, 4/3, etc.
│   │   └── flow/
│   │       ├── c_sound/c_sound.json                # 343 m/s
│   │       ├── vena_contracta/vena_contracta.json  # pi/(pi+2)
│   │       └── standard_gravity/standard_gravity.json
│   │
│   ├── hubble/
│   │   ├── H0_SH0ES/H0_SH0ES.json                  # 730/10
│   │   ├── H0_H0LiCOW/H0_H0LiCOW.json              # 733/10
│   │   ├── H0_CCHP/H0_CCHP.json                    # 698/10
│   │   ├── H0_DES_BAO_BBN/H0_DES_BAO_BBN.json      # 674/10
│   │   └── H0_Planck/H0_Planck.json                # 674/10
│   │
│   └── astrophysical/
│       ├── G_newton/G_newton.json                  # 6.674e-11
│       ├── M_sun/M_sun.json
│       ├── M_earth/M_earth.json
│       ├── M_moon/M_moon.json
│       ├── R_earth/R_earth.json
│       ├── R_sun/R_sun.json
│       ├── AU/AU.json
│       ├── pc/pc.json
│       ├── R_GPS/R_GPS.json
│       ├── v_GPS/v_GPS.json
│       ├── tau_mu/tau_mu.json                      # muon lifetime
│       ├── hbar_c_MeV_fm/hbar_c_MeV_fm.json       # 197.3269804
│       ├── dwarfs/
│       │   ├── Fornax/Fornax.json
│       │   ├── Sculptor/Sculptor.json
│       │   ├── Draco/Draco.json
│       │   ├── UrsaMinor/UrsaMinor.json
│       │   ├── Carina/Carina.json
│       │   ├── Sextans/Sextans.json
│       │   ├── LeoI/LeoI.json
│       │   ├── LeoII/LeoII.json
│       │   ├── Segue1/Segue1.json
│       │   ├── ReticulumII/ReticulumII.json
│       │   └── TucanaII/TucanaII.json
│       └── galaxy/
│           ├── MW_visible_mass/MW_visible_mass.json
│           ├── MW_virial_mass/MW_virial_mass.json
│           ├── MW_radius/MW_radius.json
│           ├── v_circ_galaxy/v_circ_galaxy.json    # 220 km/s
│           └── v_sun_galaxy/v_sun_galaxy.json
│
├── derivations/
│   ├── __init__.py                                 # Loader class
│   ├── registry.py                                 # DERIVATION_REGISTRY dict
│   │
│   ├── couplings.py                                # extract_couplings
│   ├── gap_ratios.py                               # gap_ratio, gap_ratio_SM, gap_ratio_CD, gap_distance
│   ├── one_loop.py                                 # find_crossing_L, L_to_scale, run_one_loop, predict_alpha_s_1L, predict_sin2_1L
│   ├── two_loop.py                                 # euler_two_loop, predict_alpha_s_2L, predict_sin2_2L
│   ├── koide.py                                    # koide_ratio, koide_amplitude_sq, koide_predict
│   ├── beta_decomposition.py                       # decompose_beta, verify_sum
│   ├── group_theory.py                             # casimir_adj, casimir_fund, dynkin_fund, gauge_beta, generation_democracy
│   ├── whatif.py                                   # whatif_rep, whatif_scan, whatif_custom_betas
│   │
│   ├── domains.py                                  # R2_area, airy_resolution, spot_area, disc_spot
│   ├── fiber.py                                    # fiber_mode_area, fiber_V_number, fiber_single_mode, rayleigh_loss
│   ├── acoustics.py                                # speaker_cone_area, helmholtz_freq, sound_intensity
│   ├── wire.py                                     # wire_resistance, wire_area, circular_capacitance, rc_product
│   ├── rf.py                                       # rf_wavelength, fspl_dB, antenna_area
│   ├── semiconductor.py                            # litho_resolution
│   ├── flow.py                                     # pipe_flow, orifice_flow, hagen_poiseuille, vena_contracta
│   ├── thermal.py                                  # thermal_radiation
│   ├── normalizations.py                           # fourier_norm, gaussian_norm, gaussian_peak, bcs_gap
│   ├── cancellations.py                            # verify_rc_cancellation, verify_kj_rk_cancellation
│   │
│   ├── boundaries.py                               # find_boundary, boundary_at_scale, boundaries_between, traverse
│   ├── scale_conversion.py                         # energy_to_distance_fm, distance_fm_to_energy
│   ├── hubble.py                                   # hubble_local, hubble_far, hubble_required_r, hubble_running, hubble_vp_step
│   ├── hubble_falsification.py                     # test_F1_strict, test_F1_soft
│   │
│   ├── gravity.py                                  # grav_coupling, binding_fraction, escape_velocity
│   ├── hill.py                                     # hill_sphere
│   ├── kepler.py                                   # kepler_period
│   ├── process_rate.py                             # process_rate_ratio, gps_correction
│   ├── muon.py                                     # muon_observed_lifetime, twin_paradox, ds_squared
│   ├── mond.py                                     # mond_a0, mond_transition_radius
│   │
│   ├── cosmology.py                                # dm_baryon_ratio, omega_dm, omega_b, omega_matter, omega_de
│   ├── amplification.py                            # amplification_factor, amplification_decomposition
│   ├── virial.py                                   # virial_ratio, frame_dragging
│   └── dwarfs.py                                   # dwarf_purity, dwarf_cosmic_ratio, faber_jackson, tully_fisher
│
├── connections/
│   ├── containment/
│   │   ├── quark_in_proton.json
│   │   ├── proton_in_nucleus.json
│   │   ├── nucleus_in_atom.json
│   │   ├── electron_in_atom.json
│   │   ├── atom_in_crystal.json
│   │   ├── crystal_in_geological.json
│   │   ├── geological_in_earth.json
│   │   ├── human_on_earth.json
│   │   ├── moon_in_earth_hill.json
│   │   ├── earth_in_solar.json
│   │   ├── solar_in_galaxy.json
│   │   ├── galaxy_in_cluster.json
│   │   └── cluster_in_cosmological.json
│   │
│   ├── membership/
│   │   ├── Q_L_in_generation.json
│   │   ├── u_R_in_generation.json
│   │   ├── d_R_in_generation.json
│   │   ├── L_L_in_generation.json
│   │   ├── e_R_in_generation.json
│   │   ├── CD_in_BSM.json
│   │   ├── b1_SM_in_SM_betas.json
│   │   ├── b2_SM_in_SM_betas.json
│   │   ├── b3_SM_in_SM_betas.json
│   │   ├── b1_mod_in_modified_betas.json
│   │   ├── b2_mod_in_modified_betas.json
│   │   └── b3_mod_in_modified_betas.json
│   │
│   ├── adjacency/
│   │   ├── electron_to_muon.json
│   │   ├── muon_to_strange.json
│   │   ├── strange_to_charm.json
│   │   ├── charm_to_tau.json
│   │   ├── tau_to_bottom.json
│   │   ├── bottom_to_W.json
│   │   ├── W_to_Z.json
│   │   ├── Z_to_higgs.json
│   │   ├── higgs_to_top.json
│   │   ├── top_to_cd_threshold.json
│   │   ├── cd_threshold_to_gut.json
│   │   ├── gut_to_planck.json
│   │   ├── confinement_lower_to_upper.json
│   │   └── pion_in_confinement.json
│   │
│   ├── cancellation/
│   │   ├── R2_in_KJ_RK.json
│   │   ├── R2_in_G0_RK.json
│   │   ├── R2_in_Rydberg.json
│   │   ├── R2_in_Bohr_alpha.json
│   │   ├── R2_in_RC_product.json
│   │   ├── R2_in_Omega_DM.json
│   │   ├── R2_free_Hartree.json
│   │   ├── R2_free_gap_ratio.json
│   │   └── R2_free_generation.json
│   │
│   ├── integer_source/
│   │   ├── YM_11_to_gauge_coeff.json
│   │   ├── YM_11_to_b3_SM.json
│   │   ├── YM_11_to_b2_SM_gauge.json
│   │   ├── YM_11_to_DM_numerator_22.json
│   │   ├── YM_11_to_Omega_numerator_44.json
│   │   ├── b2mod_13_to_DM_denominator.json
│   │   ├── b2mod_13_to_Omega_denominator_169.json
│   │   ├── b2mod_13_to_amplification_44_13.json
│   │   ├── b2SM_19_to_gap_SM.json
│   │   ├── b2SM_19_to_dwarf_cosmic_ratio.json
│   │   └── b3SM_20_to_gap_SM.json
│   │
│   ├── produces/
│   │   ├── extract_couplings_produces_inv_a1.json
│   │   ├── extract_couplings_produces_inv_a2.json
│   │   ├── extract_couplings_produces_inv_a3.json
│   │   ├── gap_ratio_SM_produces_gap_SM.json
│   │   ├── gap_ratio_CD_produces_gap_VL.json
│   │   ├── predict_alpha_s_2L_produces_alpha_s_pred.json
│   │   ├── koide_predict_produces_m_tau_pred.json
│   │   ├── dm_baryon_produces_DM_ratio.json
│   │   └── omega_dm_produces_Omega_DM.json
│   │
│   ├── consumes/
│   │   ├── gap_ratio_SM_consumes_b1_SM.json
│   │   ├── gap_ratio_SM_consumes_b2_SM.json
│   │   ├── gap_ratio_SM_consumes_b3_SM.json
│   │   ├── predict_alpha_s_2L_consumes_inv_a1.json
│   │   ├── predict_alpha_s_2L_consumes_bij_full.json
│   │   ├── koide_predict_consumes_m_e.json
│   │   ├── koide_predict_consumes_m_mu.json
│   │   ├── dm_baryon_consumes_b2_mod.json
│   │   ├── dm_baryon_consumes_R2.json
│   │   └── kepler_period_consumes_R2.json
│   │
│   └── equivalent/
│       ├── 4R2_equals_pi.json
│       ├── 8R2_equals_2pi.json
│       ├── 16R2_equals_4pi.json
│       ├── 64R2sq_equals_4pi_sq.json
│       └── vena_contracta_equals_pi_over_pi_plus_2.json
│
├── programs/
│   ├── beta_unification/
│   │   ├── beta_unification.json                   # thesis, status, kill switches
│   │   ├── derivation_chain.json                   # ordered list of derivation IDs
│   │   └── blocking.json                           # statistical control status
│   ├── cosmological/
│   │   ├── cosmological.json
│   │   └── derivation_chain.json
│   └── soliton_gravity/
│       ├── soliton_gravity.json
│       └── derivation_chain.json
│
├── evidence/
│   ├── scripts/
│   │   ├── phys24_lib_test/
│   │   │   └── phys24_lib_test.json                # 148/148 PASS
│   │   ├── data_4_derivation_lib_test/
│   │   │   └── data_4_derivation_lib_test.json     # 37/37 PASS
│   │   ├── phys24_structure_lib_test/
│   │   │   └── phys24_structure_lib_test.json       # 46/46 PASS
│   │   ├── phys24_boundary_map_lib_test/
│   │   │   └── phys24_boundary_map_lib_test.json   # 14/14 PASS
│   │   ├── phys24_domain_lib_test/
│   │   │   └── phys24_domain_lib_test.json         # 40/40 PASS
│   │   ├── phys24_hubble_lib_test/
│   │   │   └── phys24_hubble_lib_test.json         # 16/17 (F1 strict = data)
│   │   ├── data_5_populate_test/
│   │   │   └── data_5_populate_test.json           # 30/31 (Higgs = expected)
│   │   ├── data_5_chunk1_test/
│   │   │   └── data_5_chunk1_test.json
│   │   ├── data_5_chunk2_test/
│   │   │   └── data_5_chunk2_test.json
│   │   ├── data_5_chunk3_test/
│   │   │   └── data_5_chunk3_test.json
│   │   ├── data_5_chunk4_test/
│   │   │   └── data_5_chunk4_test.json
│   │   ├── beta_unification_test/
│   │   │   └── beta_unification_test.json
│   │   ├── toroidal_dm_test/
│   │   │   └── toroidal_dm_test.json
│   │   ├── dwarf_soliton_test/
│   │   │   └── dwarf_soliton_test.json
│   │   ├── nested_soliton_gravity_test/
│   │   │   └── nested_soliton_gravity_test.json
│   │   ├── time_process_rate_test/
│   │   │   └── time_process_rate_test.json          # 11/12 (threshold label)
│   │   └── demo_cross_domain/
│   │       └── demo_cross_domain.json
│   │
│   ├── results/
│   │   ├── result_dm_baryon.json                   # PASS 0.073%
│   │   ├── result_alpha_s_1L.json                  # PASS ~13%
│   │   ├── result_alpha_s_2L_SM.json               # PASS <1%
│   │   ├── result_alpha_s_2L_full.json             # PASS <0.5%
│   │   ├── result_sin2_1L.json                     # PASS <1%
│   │   ├── result_koide_mtau.json                  # PASS <0.01%
│   │   ├── result_gps_correction.json              # PASS ~38.5 us/day
│   │   ├── result_kepler_6planets.json             # PASS <0.1%
│   │   ├── result_mond_a0.json                     # PASS ~8%
│   │   ├── result_earth_hill.json                  # PASS ~1.5e6 km
│   │   ├── result_muon_gamma.json                  # PASS gamma=7.09
│   │   ├── result_amplification.json               # PASS (44/13)*pi*(c/v)^2
│   │   └── result_draco_purity.json                # PASS DM/vis>100
│   │
│   └── papers/
│       ├── DATA_5.json                             # this paper's claims and evidence
│       ├── DATA_5_appendix.json                    # 20 tables
│       ├── PHYS_24.json
│       └── alignment_doc.json                      # teaching document for new sessions
│
├── display/
│   ├── show_couplings.py                           # print functions (no computation)
│   ├── show_gap_ratios.py
│   ├── show_beta_decomposition.py
│   ├── show_predictions.py
│   ├── show_koide.py
│   ├── show_disc_spots.py
│   ├── show_speakers.py
│   ├── show_awg_table.py
│   ├── show_rc_cancellation.py
│   ├── show_normalizations.py
│   ├── show_boundary_stack.py
│   ├── show_hubble_data.py
│   ├── show_gps_correction.py
│   ├── show_muon_table.py
│   ├── show_twin_paradox.py
│   ├── show_kepler.py
│   ├── show_hill_spheres.py
│   ├── show_process_rates.py
│   ├── show_mond_a0.py
│   ├── show_soliton_hierarchy.py
│   ├── show_beta_cosmology.py
│   ├── show_amplification.py
│   ├── show_purity_spectrum.py
│   ├── show_dwarf_fj.py
│   ├── show_integer_appearances.py
│   ├── show_all_R2_equations.py
│   ├── show_all_cancellations.py
│   ├── show_experiment_results.py
│   ├── show_research_status.py
│   └── show_cross_domain_area.py
│
├── tests/
│   ├── test_entities.py                            # all entity JSON files load and validate
│   ├── test_derivations.py                         # all registered derivations run and match
│   ├── test_connections.py                         # all connection JSON files resolve
│   ├── test_registry_sync.py                       # registry.py matches derivation_index.json
│   ├── test_couplings.py                           # extract_couplings vs phys24_lib
│   ├── test_gap_ratios.py                          # SM=218/115, CD=38/27
│   ├── test_one_loop.py                            # crossing L, alpha_s, sin2
│   ├── test_two_loop.py                            # Euler binary search, bij matrices
│   ├── test_koide.py                               # K, a^2, m_tau prediction
│   ├── test_group_theory.py                        # Casimirs, Dynkin, democracy
│   ├── test_domains.py                             # all 23 R2 domains vs domain lib
│   ├── test_cancellations.py                       # RC product, KJ*RK numerical verification
│   ├── test_boundaries.py                          # search, traverse, count=19
│   ├── test_hubble.py                              # H0 Fractions, r(N), F1
│   ├── test_gravity.py                             # coupling, escape velocity, Hill spheres
│   ├── test_kepler.py                              # 64R2^2=4pi^2, 6 planets
│   ├── test_process_rate.py                        # GPS correction ~38 us/day
│   ├── test_muon.py                                # gamma at 0.99c, monotonic
│   ├── test_cosmology.py                           # DM/baryon, Omega_DM, flatness
│   ├── test_amplification.py                       # decomposition = 44/13
│   ├── test_dwarfs.py                              # purity, FJ/TF, v^4 scaling
│   ├── test_cross_chunk.py                         # R2 path consistency across all modules
│   └── run_all.py                                  # runs every test, reports summary
│
├── generators/
│   ├── q335_basis.py                               # compute all 35 Q335 numerators
│   ├── more_constants_335_basis.py                 # compute extended 35 constants
│   ├── populate_entities.py                        # DATA-5 objects -> DATA-6 entity JSONs
│   ├── populate_derivations.py                     # helper functions -> derivation JSONs
│   ├── populate_connections.py                     # relationships -> connection JSONs
│   ├── populate_evidence.py                        # scripts/results -> evidence JSONs
│   └── build_registry.py                           # generate registry.py from derivation_index.json
│
├── platform/
│   ├── phys24_lib.py                               # core constants (21/21 + 148/148)
│   ├── data_4_derivation_lib.py                    # derivation functions (37/37)
│   ├── phys24_structure_lib.py                     # structure/reps (46/46)
│   ├── phys24_boundary_map_lib.py                  # boundary stack (14/14)
│   ├── phys24_domain_lib.py                        # R2 domains (40/40)
│   ├── phys24_hubble_lib.py                        # Hubble running (16/17)
│   └── data_5_diagram_lib.py                       # diagram generation (7 test figs)
│
└── docs/
    ├── DATA_5_paper.md                             # the DATA-5 paper text
    ├── DATA_5_appendix.md                          # 20 appendix tables
    ├── DATA_6_design_spec_A.md                     # Part A: file system, IDs, schemas
    ├── DATA_6_design_spec_B.md                     # Part B: derivations as code
    ├── alignment_doc.md                            # teaching doc for new sessions
    ├── operational_rules.md                        # Tables R.1-R.6
    └── README.md                                   # system overview, how to run
```

222 entity JSON files. ~160 derivation functions across 25 modules. ~70 connection JSON files. ~30 evidence JSON files. 23 test scripts. 7 generator scripts. 7 platform libraries. 6 documentation files. 4 index files.

One directory tree. Every object has a path. Every derivation has a module. Every connection has a file. Every ID resolves.

---

