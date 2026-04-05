## DATA-6 v0.3 IMPROVEMENT PLAN

*From the master session that built DATA-5, the generator, the compiler, and the corrected master tables.*
*This reviews v0.2 and enumerates what the next version should fix.*

---

### 1. THE TWO-LOOP BUG IS THE BLOCKING ITEM

The tech spec acknowledges it in Section 17.1: two-loop alpha_s shows 10-12% miss instead of the platform's 0.325%. This isn't a design problem — it's a data or code bug. Before anything else in this list matters, this needs to be fixed.

The platform values (37/37 PASS from data_4_derivation_lib.py):
- Two-loop SM bij: alpha_s = 0.11753, miss = 0.397%
- Two-loop full bij: alpha_s = 0.11838, miss = 0.325%

The v0.2 result (Appendix D.3):
- Two-loop SM bij: alpha_s = 0.12995, miss = 10.13%
- Two-loop full bij: alpha_s = 0.13208, miss = 11.93%

Investigation path: compare the db_ij_VL matrix values in `values_two_loop_vl_dbij_v0.json` entry by entry against phys24_lib's `b_ij_SM` and data_4_derivation_lib's `db_ij_VL`. Check whether the Euler integrator is using the same step count and bisection depth. Check whether the b_ij_full = b_ij_SM + db_ij_VL addition is correct element by element. The platform's Euler integrator uses 500 steps and 60 bisections — verify the derivation function matches.

This should be a formal experiment: `experiment_two_loop_investigation_v0.json` with comparisons checking each matrix element individually.

---

### 2. HARDCODED CONSTANTS IN DERIVATION CODE

Section 2.6 says "No hardcoded physics constants." The coupling running renderer hardcodes M_VL = 3 TeV. But the deeper problem is in the derivation functions themselves — I'd bet the Euler integrator has `mp.dps` settings, step counts, or convergence thresholds that aren't value nodes.

Every numerical parameter of every derivation should be a value node:
- `config_euler_step_count_v0` = 500
- `config_euler_bisection_depth_v0` = 60
- `config_euler_convergence_threshold_v0` = "1e-30"
- `config_cd_mass_estimate_gev_v0` = 3000

These are Level 2 choices (could be different), not Level 1 structure. When someone wants to run at 1000 steps or test M_VL = 5 TeV, they create a dataset override, not a code fork.

---

### 3. THE ALIAS MESS

Section 16.2 lists 10 aliases. Two JSON files exist solely to paper over naming disagreements between the exporter and the derivation registry. This is technical debt that makes the system harder to trust.

Fix: pick one canonical name per concept. The rule should be: the derivation registry's input keys ARE the canonical names. The exporter writes those names. No alias files. If a derivation expects `beta_cabibbo_doublet_vectorlike_su2_shift_v0`, that's the canonical key, and the exporter writes that key.

While fixing this, establish a naming convention doc. The current names are inconsistent: some use `cd` abbreviation, some spell out `cabibbo_doublet`. Some use `_derived` suffix for outputs, some don't. Pick conventions, document them, apply uniformly.

---

### 4. MISSING DERIVATIONS (~60 FUNCTIONS)

Section 16.3 says ~60 helper functions from DATA-5 chunks aren't migrated. These are the gravity, soliton, Hubble, boundary, MOND, GPS, muon, Kepler, dwarf, domain, and cross-domain functions. They're needed for two reasons:

First, the soliton gravity and dwarf soliton experiments can't run without them.

Second, the system currently has one experiment definition. A research platform with one experiment isn't a platform — it's a demo. The target is at least three experiments matching the three research programs:
- `experiment_beta_unification_v0` (exists, works)
- `experiment_soliton_gravity_v0` (needs gravity, Kepler, GPS, Hill, process rate, muon derivations)
- `experiment_dwarf_soliton_v0` (needs dwarf purity, FJ/TF, amplification, cosmic ratio derivations)

Each experiment needs its own comparison specs and diagram specs.

---

### 5. OMEGA_DM COMPARISON IS MISLEADING

Appendix D.3 shows Omega_DM at 21.56% miss. This compares (44/169)*R2 = 0.2045 to Planck Omega_DM = 0.2607. But the formula gives the DM density as a function of total matter density — the absolute normalization requires additional physics (baryon density, radiation, curvature). The meaningful comparison is DM/baryon = (22/13)*pi at 0.073% miss.

The experiment JSON should either remove the Omega_DM comparison or change it to `match_mode: "info"` with a note explaining why the absolute value doesn't match. Currently it's INFO, which is correct, but the 21.56% sitting next to the 0.073% gives a false impression of failure.

Better: add a comparison for Omega_DM/Omega_b = DM/baryon, which should match the (22/13)*pi prediction regardless of absolute normalization. And add Omega_b = Omega_DM / [(22/13)*pi] as a derived prediction.

---

### 6. CONTAINMENT AND HIERARCHY CONNECTIONS

The v0.2 system has 5 connection functions. None of them capture the soliton nesting hierarchy. The connections_v0.json has 92 connection metadata entries (boundaries, forces, R2 equations, cancellations, closed paths, anomalies) but these are static data, not executable connection functions.

The containment chain (quark → proton → nucleus → atom → crystal → geological → Earth → solar → galaxy → cluster → cosmological) should be a connection function that:
- Resolves coupling GM/(rc²) at each level from astrophysical value nodes
- Computes escape velocity at each boundary
- Returns the full hierarchy with edges between adjacent levels
- Allows insertion of new levels (the mutable nesting requirement)

Same for the R2 cancellation chain — should be an executable connection that verifies each cancellation numerically from the value pool, not a static list.

---

### 7. THE RUNNER NEEDS PRE-FLIGHT VALIDATION

Currently the runner just starts executing. If derivation 5 needs an output from derivation 3 that failed, derivation 5 also fails and you get cascading errors. The runner should:

1. Before execution, build the dependency DAG from declared inputs/outputs
2. Check that all required input values exist in the pool
3. Detect cycles
4. Warn about missing dependencies before running anything
5. If a derivation fails, skip all downstream derivations that depend on its outputs (not just the immediate next one)

This doesn't require topological sort of the execution plan (the experiment author declares valid order). It just requires a pre-flight check that the declared order is consistent with the declared inputs/outputs.

---

### 8. RESULT VERSIONING

Section 18.9 notes this is undecided. Currently results overwrite: `result_experiment_beta_unification_v0.json`. If you run twice, the first result is gone.

Fix: append a run counter or short timestamp hash. `result_experiment_beta_unification_v0_run001.json`. Keep the latest as a symlink or a `_latest` alias. Old results are never deleted (append-only principle).

---

### 9. THE PITFALL SYSTEM IS UNDERUSED

The pitfall mechanism is documented in Section 3.2 but I see no evidence of pitfalls actually being attached to nodes in the JSON files. The known pitfalls from our work:

- `coupling_alpha_2_inverse_mz_v0`: wrong = "alpha_inv / sin2_tW", right = "sin2_tW * alpha_inv"
- `beta_modified_u1_total_v0`: wrong = "62/15", right = "25/6" (same value, wrong Fraction form in some docs)
- `values_two_loop_vl_dbij_v0` [1][1]: wrong = "39/4", right = "15/4" (fermion only, no gauge double-count)
- `mass_w_boson_v0`: wrong = "80379 MeV" (some sessions), right = "80369.2 MeV" (phys24_lib: 803692/10)

Every one of these should be a pitfall entry on the relevant value node. The point of the pitfall system is that a new session reading the JSON immediately sees the trap before falling into it.

---

### 10. Removed, advice here not wanted

Nothing to change.

---

### 11. Removed, advice here not wanted

Nothing to change.

---

### 12. MISSING VALUE CATEGORIES

The value inventory has 357 nodes but is missing some categories that exist in our generator:

- **Moduli** (16 values in our system): R2 as filling fraction, vena contracta, BCS gap, Fourier/Gaussian normalizations. These are structural constants that connect domains.
- **Boundary metadata**: The boundaries exist in connections_v0.json as static data, but not as proper value nodes with scale_MeV, known/unknown, forces_affected. Each boundary should be a value node so derivations can reference boundary scales by key.
- **Dwarf galaxy core radii**: The observational data has M_vis, sigma, r_h, M_dyn but some entries are missing r_core which the DATA-5 soliton analysis uses.

---

### 13. CONNECTION FUNCTION OUTPUTS AREN'T IN THE POOL

Derivation outputs get merged into the value pool (line ~180 of the runner). Connection outputs don't. The runner calls the connection function, prints the result, and moves on. If a connection computes something useful (like the integer network traceability chain), that computed data isn't available to later comparisons or diagrams.

Fix: connection functions should optionally produce `named_values` that get merged into the pool, same as derivation outputs. The connection result already has a `named_values` field — just append those to the pool after resolution.

---

### 14. NO DATASET SUPPORT YET

Sections 4.7 and 6 describe datasets but they're not implemented. The practical consequence: you can't run "what if alpha_s were 0.1190 instead of 0.1180?" without editing a JSON file. With datasets, you'd create:

```json
{
    "key": "dataset_alpha_s_high_v0",
    "base": "dataset_howl_v0",
    "overrides": {"coupling_alpha_s_strong_mz": {"version": 1, "value": "59.5/500"}}
}
```

And run: `python data_6_run.py beta_unification_v0 --dataset alpha_s_high_v0`

This is the "what-if" scan capability from DATA-5's chunk 1 (`whatif_rep`, `whatif_scan`), but formalized. Each what-if is a dataset. Each dataset produces a result. You compare results across datasets.

---

### 15. PROVENANCE CHAIN ISN'T QUERYABLE

Every value has a `source` field. Derivation outputs get `source: "coupling_extraction_v0"`. But you can't ask "what values did coupling_extraction_v0 consume?" without reading the derivation's `inputs` list. And you can't ask "what derivations consumed alpha_inv?" without scanning all derivation input lists.

A post-run provenance index would fix this:
```json
{
    "alpha_inv_v0": {
        "consumed_by": ["coupling_extraction_v0"],
        "produced_by": "phys24_lib (CODATA 2022)"
    },
    "coupling_alpha_1_inverse_gut_normalized_mz_derived_v0": {
        "consumed_by": ["gap_measured_ratio_v0", "crossing_one_loop_scale_v0"],
        "produced_by": "coupling_extraction_v0"
    }
}
```

The runner has all the information to build this — it knows what each derivation consumed and produced. Just needs to write it.

---

### 16. JSON SCHEMA VALIDATION

Section 18.2 defers this. It should happen in v0.3. Every value node must have: key, canonical, version, node_type, value, value_type, unit, level, source. The runner should validate every loaded node against the schema before execution. Invalid nodes should be warnings (not crashes) with the node key and the missing field.

A `data_6_validate.py` script that checks all JSON files against the schema, reports issues, and exits 0/1 would catch data entry errors before they become runtime failures.

---

### 17. COMPARISON ENGINE NEEDS "IDENTITY" MODE

The deferred match modes in Section 11.2 include `identity` — verify a mathematical identity to working precision. This is needed for:
- 64*R2² = 4*pi² (Kepler identity, verified to 20 digits in our tests)
- 8*R2 = 2*pi (exact within Q335)
- K_J * R_K = 2/e (R2 cancellation)
- Wire R * Cap C = rho*eps0*L/t (cross-domain cancellation)

These aren't "expected value" checks — they're two-sided identities where both sides are computed from the value pool. The comparison spec should be:
```json
{
    "label": "Kepler identity",
    "match_mode": "identity",
    "lhs_expr": "64 * R2^2",
    "rhs_expr": "4 * pi^2",
    "digits": 20
}
```

This requires an expression evaluator, which is a bigger piece of work. But even a limited version that handles multiply/power/add of value pool entries would cover the important cases.

---

### 18. THE FLAT LAYOUT WORKS BUT NEEDS AN INDEX

Section 14.4 says to organize into subdirectories when it grows. I disagree — flat is fine, but it needs a manifest. A `data_6_manifest.json` that lists every file, its type, its node count, and its last-modified timestamp. The runner reads the manifest instead of globbing. The manifest is regenerated by a `data_6_index.py` script whenever files change.

This is better than subdirectories because:
- One glob vs many globs
- The manifest IS the index
- You can check the manifest into version control and see diffs
- No path-encoding-in-keys problem

---

### 19. MERGE OUR COMPILED VIEW

The `compile_data6.py` from our session produces a single `data6_compiled.json` with everything organized by layer. This is valuable for LLM ingestion — drop one file into context, the LLM has the full knowledge base. The v0.2 system should have a compiler that produces this view from its flat files.

The compiled view should include: all value nodes organized by section, all connection metadata, all program nodes, the derivation registry (function signatures and IO, not code), the experiment comparison results, and the integer pool traceability.

---

### 20. PRIORITY ORDER

| Priority | Item | Why |
|----------|------|-----|
| 1 | Fix two-loop bug (#1) | Correctness. Everything else is pointless if predictions are wrong. |
| 2 | Remove aliases (#3) | Trust. Aliases make the system look unreliable. |
| 3 | Add pitfalls to nodes (#9) | Safety. New sessions need to see the traps. |
| 4 | Omega_DM comparison fix (#5) | Accuracy. Misleading miss% damages credibility. |
| 5 | Pre-flight validation (#7) | Robustness. Cascading failures waste time. |
| 6 | Result versioning (#8) | Data preservation. Append-only means append-only. |
| 7 | Add soliton gravity experiment (#4) | Coverage. Three programs need three experiments. |
| 8 | Extract hardcoded constants (#2) | Principle compliance. The spec says no hardcoded constants. |
| 9 | Containment connections (#6) | Completeness. The hierarchy IS the physics. |
| 10 | Compiled view (#19) | Usability. LLM sessions need the single-file ingest. |
| 11-20 | Everything else | Important but not blocking. |

---

*This plan assumes the flat layout stays. No directory reorganization. No new node types. Just fix what's broken, add what's missing, and make the existing architecture deliver on its own promises.*