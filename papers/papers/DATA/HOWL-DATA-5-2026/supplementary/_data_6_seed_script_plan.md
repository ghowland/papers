## DATA-6 GENERATOR SCRIPT PLAN

*Script name: `generate_data6.py`*
*Input: 7 platform libraries in current directory*
*Output: complete data6/ directory tree with all JSON files and index*

---

### 1. What the Script Does

One script. Reads all 7 platform libraries. Writes every JSON file. Builds every index. Creates every directory. The script IS the migration from DATA-5 to DATA-6.

It does NOT write the derivation Python modules (those are written by hand — code is not generated from data). It DOES write the derivation_index.json that maps IDs to module.function paths, so the hand-written modules know their IDs.

---

### 2. Execution Order

The script runs in 10 phases. Each phase depends only on previous phases. No circular dependencies.

```
Phase 1:  Create directory structure
Phase 2:  Assign IDs (build the allocation map)
Phase 3:  Write SI constants
Phase 4:  Write Q335 transcendentals
Phase 5:  Write measured constants (couplings, masses, group theory, betas, two-loop, geometric, engineering, astrophysical, hubble)
Phase 6:  Write derived entities (gap ratios, koide, cosmological, representations, boundaries, domains, cancellations, moduli)
Phase 7:  Write connection JSON files
Phase 8:  Write evidence JSON files
Phase 9:  Write program JSON files
Phase 10: Write all index files (entity, derivation, connection, evidence, id_counter)
```

---

### 3. Phase 1: Directory Creation

Create every directory in the tree. Use `os.makedirs(path, exist_ok=True)` for each. The full list from the directory structure document — approximately 85 directories.

No JSON written in this phase. Just empty directories.

---

### 4. Phase 2: ID Allocation

Build a Python dict mapping every object name to its permanent ID. This dict is used by all subsequent phases when writing JSON files and cross-references.

The allocation follows the block plan:

| Block | Range | Content | Source |
|---|---|---|---|
| 1-7 | 1-7 | SI constants | phys24_lib: c, h, e_charge, k_B, N_A, dv_Cs, K_cd |
| 10-19 | 10-19 | Derived couplings | derive_couplings output: inv_a1, inv_a2, inv_a3 |
| 20-29 | 20-29 | Measured couplings | phys24_lib: alpha_inv, sin2_tW, alpha_s |
| 50-99 | 50-99 | Geometric constants | R2, R4, twopi, j01, j11, bessel-derived |
| 100-149 | 100-149 | Group theory | C2_adj/fund, S2_fund, k1_GUT, gauge_coeff, N_gen, per_gen |
| 200-299 | 200-299 | Q335 transcendentals | pi, e, ln2, sqrt2, zeta3, ... all 35+powers |
| 500-549 | 500-549 | Lepton masses | m_e, m_mu, m_tau |
| 550-599 | 550-599 | Quark masses | m_u, m_d, m_s, m_c, m_b, m_t |
| 600-649 | 600-649 | Boson masses | M_Z, M_W, M_H |
| 1000-1008 | 1000-1008 | Beta coefficients | b1_SM, b2_SM, b3_SM, db1-3_VL, b1-3_mod |
| 1020-1049 | 1020-1049 | Two-loop bij matrices | bij_SM 9 entries, dbij_VL 9 entries |
| 1050-1069 | 1050-1069 | Gap ratios + Koide | gap_SM, gap_VL, gap_MSSM, gap_measured, K_koide, a2_lep, m_tau_pred |
| 1070-1079 | 1070-1079 | Cosmological | DM_baryon, Omega_DM, Omega_b, Omega_m, Omega_DE |
| 1100-1105 | 1100-1105 | Representations | Q_L, u_R, d_R, L_L, e_R, CD |
| 1200-1218 | 1200-1218 | Boundaries | 19 boundaries ordered by energy |
| 1300-1322 | 1300-1322 | R2 Domains | 23 domains |
| 1400-1410 | 1400-1410 | Cancellations | 11 R2 cancellation identities |
| 1500-1515 | 1500-1515 | Moduli | 16 moduli |
| 1600-1649 | 1600-1649 | Engineering data | discs, fiber, speakers, AWG, materials, RF, semiconductor, audio, flow |
| 1700-1749 | 1700-1749 | Hubble data | 5 H0 measurements |
| 1800-1849 | 1800-1849 | Astrophysical | G, M_sun, M_earth, AU, dwarfs, galaxy |
| 2000-2199 | 2000-2199 | Derivations | ~160 derivation registry entries |
| 3000-3099 | 3000-3099 | Containment connections | ~13 |
| 3100-3149 | 3100-3149 | Membership connections | ~12 |
| 3200-3249 | 3200-3249 | Adjacency connections | ~14 |
| 3300-3349 | 3300-3349 | Cancellation connections | ~9 |
| 3400-3449 | 3400-3449 | Integer source connections | ~11 |
| 3500-3549 | 3500-3549 | Produces connections | ~9 |
| 3600-3649 | 3600-3649 | Consumes connections | ~10 |
| 3700-3719 | 3700-3719 | Equivalent connections | ~5 |
| 5000-5049 | 5000-5049 | Script evidence | ~17 scripts |
| 5100-5149 | 5100-5149 | Result evidence | ~13 results |
| 5200-5219 | 5200-5219 | Paper evidence | ~4 papers |
| 6000-6002 | 6000-6002 | Research programs | 3 programs |

The allocation dict is built as a Python dict `IDS = {}` at the top of the script. Every subsequent phase uses `IDS["alpha_inv"]` to get the numeric ID for cross-references.

---

### 5. Phase 3: SI Constants

Source: phys24_lib.py constants `c_SI`, `h_SI`, `e_SI`, `k_B_SI`, `N_A_SI`, `dv_Cs_SI`, `K_cd_SI`.

For each: write one JSON file to `entities/si_constants/{name}/{name}.json`.

JSON structure:
```
{
  "id": IDS[name],
  "type": "entity",
  "subtype": "si_constant",
  "name": name,
  "value": {"integer": value} or {"fraction": {"numerator": n, "denominator": d}},
  "unit": unit_string,
  "level": 0,
  "tags": ["SI", "exact", "Level0"],
  "source": "SI 2019 (exact definition)",
  "version": 0,
  "created": {"session": 4, "date": "2026-04-04"}
}
```

7 files written.

---

### 6. Phase 4: Q335 Transcendentals

Source: phys24_lib.py Fraction constants `pi_f`, `e_f`, `ln2_f`, `sqrt2_f`, ..., `Cl2_pi3_f`, plus `R2_f`, `R4_f`, `twopi_f`, and the power products `pi2_f`, `pi3_f`, `pi4_f`, `ln2_2_f`, `ln2_4_f`, `zeta2_f`.

For each: write to `entities/q335/{name}/{name}.json`.

Value stored as:
```
"value": {
  "fraction": {
    "numerator": str(frac.numerator),
    "denominator": str(frac.denominator)
  },
  "q335_numerator": str(frac.numerator),
  "note": "p/Q where Q = 2^335, 100-digit precision"
}
```

Numerators are huge integers (100+ digits). Store as strings in JSON to avoid integer overflow in JSON parsers.

Also write geometric constants (R2, R4, twopi) to `entities/geometric/` and bessel zeros (j01, j11) to `entities/geometric/bessel/`.

~40 files written.

---

### 7. Phase 5: Measured Constants

Multiple sources within phys24_lib.py:

**Couplings (3 files):** alpha_inv, sin2_tW, alpha_s. Each is a Fraction. Write to `entities/couplings/`.

**Derived couplings (3 files):** inv_a1, inv_a2, inv_a3. Computed by calling `derive_couplings(alpha_inv, sin2_tW, alpha_s)` from data_4_derivation_lib. Write to `entities/couplings/`. These reference the input IDs.

**Masses (12 files):** m_e through M_H. All Fractions from phys24_lib. Write to `entities/masses/`.

**Group theory (10 files):** C2_adj_SU3, C2_adj_SU2, C2_fund_SU3, C2_fund_SU2, S2_fund, k1_GUT, k1_inv, N_gen, gauge_coeff, per_gen_shift. All Fractions. Write to `entities/group_theory/`.

**Betas (9 files):** b1_SM, b2_SM, b3_SM, db1_VL, db2_VL, db3_VL, b1_mod, b2_mod, b3_mod. Each with decomposition fields (gauge_part, fermion_part, higgs_part, bsm_part). Source: phys24_lib for SM and VL, computed for mod. Write to `entities/betas/`.

Beta JSON includes decomposition:
```
"decomposition": {
  "gauge": {"numerator": N, "denominator": D},
  "fermion": {"numerator": N, "denominator": D},
  "higgs": {"numerator": N, "denominator": D},
  "bsm": null or {"numerator": N, "denominator": D}
}
```

**Two-loop bij (18 files):** 9 SM entries from phys24_lib `b_ij_SM`, 9 VL entries from data_4_derivation_lib `db_ij_VL`. All Fractions. Write to `entities/two_loop/`.

**Engineering data (~30 files):** OPTICAL_DISCS (3), FIBER_OPTICS (1), SPEAKERS (6), AWG_DATA (12), materials (4), RF (3), semiconductor (3), audio (2), flow (3). Source: phys24_domain_lib data dicts. Write to `entities/engineering/` subdirectories. Values stored as `{"mpf": "string_value"}`.

**Hubble data (5 files):** H0_MEASUREMENTS from phys24_hubble_lib. Each with H0 Fraction, uncertainty Fraction, distance_class, source. Write to `entities/hubble/`.

**Astrophysical (~15 files):** G_newton, M_sun, M_earth, M_moon, R_earth, R_sun, AU, pc, R_GPS, v_GPS, tau_mu, hbar_c_MeV_fm, galaxy params. Source: mpf string constants from the experiment scripts. Write to `entities/astrophysical/`.

**Dwarf galaxies (11 files):** DWARFS (8) and ULTRA_FAINTS (3) from dwarf_soliton_ground_state.py data. Each with M_vis, sigma, r_h, M_dyn, r_core. Write to `entities/astrophysical/dwarfs/`.

~120 files written in this phase.

---

### 8. Phase 6: Derived Entities

**Gap ratios (4 files):** gap_SM (218/115), gap_VL (38/27), gap_MSSM (5/7), gap_measured. Computed from betas in phase 5. Write to `entities/gap_ratios/`. Each references the beta IDs used to compute it.

**Koide (3 files):** K_koide, a2_lep, m_tau_pred. Computed from lepton masses. Write to `entities/koide/`.

**Cosmological (5 files):** DM_baryon_ratio, Omega_DM, Omega_b, Omega_matter, Omega_DE. Computed from beta integers and R2. Write to `entities/cosmological/`. Each references the beta and R2 IDs.

**Representations (6 files):** Q_L, u_R, d_R, L_L, e_R, CD. Source: phys24_structure_lib `make_rep()` or manual from known quantum numbers. Each stores (su3_dim, su2_dim, Y, rep_type, db1, db2, db3, charges). Write to `entities/representations/`.

**Boundaries (19 files):** From phys24_boundary_map_lib boundary data. Each stores scale_MeV, known, what_changes, forces_affected, couplings dict, open_questions list. Write to `entities/boundaries/`.

**R2 Domains (23 files):** From phys24_domain_lib R2_EQUATIONS list. Each stores equation, coordinator_Z, precision, data1_section. Write to `entities/domains/`.

**Cancellations (11 files):** From phys24_domain_lib R2_CANCELLATIONS and the modulus notebook. Each stores formula, status, remains, precision. Write to `entities/cancellations/`.

**Moduli (16 files):** R2, R4, alpha, sin2, alpha_s, K_koide, gap_SM, gap_VL, vena_contracta, bcs_gap, Omega_DM, DM_baryon, 1_minus_r, fourier, gaussian, kepler. Each stores value, level, interpretation. Write to `entities/moduli/`.

~90 files written in this phase.

---

### 9. Phase 7: Connections

Build connection JSON files from the structural relationships.

**Containment (13 files):** The soliton nesting hierarchy. Hard-coded list of (from_name, to_name) pairs with properties (coupling, boundary_type, escape_velocity). Each references entity IDs for from and to. Write to `connections/containment/`.

**Membership (12 files):** Representations in generations, betas in sets. Each references the member entity ID and the group it belongs to. Write to `connections/membership/`.

**Adjacency (14 files):** Boundary pairs that are neighbors in the energy stack. Iterate through the sorted boundary list, create one connection per adjacent pair. Write to `connections/adjacency/`.

**Cancellation (9 files):** Which R2 cancellations connect which entities. Each references the cancellation entity and the entities whose product cancels. Write to `connections/cancellation/`.

**Integer source (11 files):** Which integers originate from which entities. 11→gauge_coeff, 11→b3_SM, 13→b2_mod, etc. Write to `connections/integer_source/`.

**Produces (9 files):** Which derivations produce which entities. Maps derivation IDs to output entity IDs. Write to `connections/produces/`.

**Consumes (10 files):** Which derivations consume which entities. Maps derivation IDs to input entity IDs. Write to `connections/consumes/`.

**Equivalent (5 files):** 4R2=pi, 8R2=2pi, 16R2=4pi, 64R2^2=4pi^2, vena_contracta=pi/(pi+2). Write to `connections/equivalent/`.

~83 files written.

---

### 10. Phase 8: Evidence

**Script evidence (17 files):** One per test/experiment script. Each stores: file name, checks_total, checks_pass, checks_fail, blocking status, derivations tested. The counts come from the known test results in the DATA-5 paper. Write to `evidence/scripts/`.

**Result evidence (13 files):** One per experiment result. Each stores: status (PASS/FAIL), predicted value, measured value, miss_pct, script that produced it, derivation ID that computed it. Write to `evidence/results/`.

**Paper evidence (4 files):** DATA-5, DATA-5 appendix, PHYS-24, alignment doc. Each stores: claims list, evidence backing each claim, does_not_claim, seeds. Write to `evidence/papers/`.

~34 files written.

---

### 11. Phase 9: Programs

**3 files:** beta_unification.json, cosmological.json, soliton_gravity.json. Each stores: thesis, status, scripts (IDs), kill_switches, blocking items, derivation_chain (ordered list of derivation IDs used by this program). Write to `programs/`.

Also write `derivation_chain.json` for each program — the ordered sequence of derivation IDs that constitutes the program's computational pipeline.

Also write `blocking.json` for beta_unification — the status of the statistical control script.

~9 files written.

---

### 12. Phase 10: Index Files

**entity_index.json:** Iterate over every entity JSON written in phases 3-6. For each, record: ID, type, subtype, name, version, status, path. This is the master entity lookup.

**derivation_index.json:** Write the full derivation registry. For each of the ~160 derivation functions: ID, name, module path, function name, input IDs, output IDs, method, level, pitfalls, version, status. This is built from a hard-coded table in the script that maps every helper function to its IO.

**connection_index.json:** Iterate over every connection JSON written in phase 7. For each: ID, type, subtype, name, from_id, to_id, path.

**evidence_index.json:** Iterate over every evidence JSON written in phase 8. For each: ID, type, subtype, name, path, status.

**id_counter.json:** `{"next_id": max_id_used + 1}`.

**type_schema.json:** The required fields for each type/subtype. Hard-coded from the schemas in the design spec.

6 files written.

---

### 13. Helper Functions Within the Script

The script needs these internal helpers:

**`write_json(path, data)`:** Write a dict to a JSON file with 2-space indent, ensure parent dirs exist.

**`fraction_to_json(frac)`:** Convert a Python Fraction to `{"numerator": str(n), "denominator": str(d)}`. Uses strings for large Q335 numerators.

**`mpf_to_json(val)`:** Convert an mpf value to `{"mpf": mp.nstr(val, 50)}`. 50 digits for storage.

**`value_to_json(val)`:** Dispatch: if Fraction → fraction_to_json, if mpf → mpf_to_json, if int → `{"integer": val}`.

**`make_entity(id, subtype, name, value, unit, level, tags, source, **extra)`:** Build the full entity dict with all required fields plus any extras.

**`make_derivation_entry(id, name, module, function, inputs, outputs, method, **extra)`:** Build a derivation index entry.

**`make_connection(id, subtype, name, from_id, to_id, relationship, properties, **extra)`:** Build a connection dict.

**`make_evidence(id, subtype, name, **extra)`:** Build an evidence dict.

---

### 14. Import Map

The script imports from these platform libraries:

```python
from phys24_lib import *                    # all constants, f2m, chk_exact etc.
from data_4_derivation_lib import (
    derive_couplings, decompose_SM_betas,
    db_ij_VL, b_ij_full, b_ij_SM,
    C2_adj_SU3, C2_adj_SU2, C2_fund_SU3, C2_fund_SU2,
    S2_fund, k1_GUT, k1_inv, N_gen, gauge_coeff,
    gap_ratio_from_betas, koide_ratio, koide_predict_m_tau,
)
from phys24_structure_lib import (
    make_rep, generation_betas, total_SM_betas,
)
from phys24_boundary_map_lib import (
    BOUNDARY_MAP,  # or however boundaries are stored
)
from phys24_domain_lib import (
    R2_EQUATIONS, R2_CANCELLATIONS,
    OPTICAL_DISCS, FIBER_OPTICS, SPEAKERS,
    AWG_DATA, CU_RESISTIVITY,
    SEMICONDUCTOR, RF_STANDARDS, SAMPLE_RATES,
    JUST_INTONATION, BCS_DATA, FLOW_CONSTANTS,
    MEMORY_STANDARDS, STORAGE_INTERFACES, GEODESY,
    MATH_NORMALIZATIONS, METROLOGY,
)
from phys24_hubble_lib import (
    H0_MEASUREMENTS, H0_ORDERED,
)
```

---

### 15. Verification

After all phases complete, the script runs a self-check:

1. Count files written per directory. Print totals.
2. Load entity_index.json, verify every path exists on disk.
3. Load derivation_index.json, verify count matches expected ~160.
4. Load connection_index.json, verify every from_id and to_id exist in entity_index.
5. Spot-check 10 entity values: load the JSON, parse the value, compare to phys24_lib.
6. Print summary: total files, total IDs assigned, any errors.

---

### 16. Output Summary

| Phase | Files | Content |
|---|---|---|
| 1 | 0 (dirs only) | ~85 directories |
| 2 | 0 (memory only) | IDS dict with ~350 entries |
| 3 | 7 | SI constants |
| 4 | ~40 | Q335 transcendentals + geometric |
| 5 | ~120 | Measured constants, betas, engineering, astro |
| 6 | ~90 | Derived entities, boundaries, domains |
| 7 | ~83 | All connection types |
| 8 | ~34 | Scripts, results, papers |
| 9 | ~9 | Programs + chains + blocking |
| 10 | 6 | All index files |
| **Total** | **~389** | **Complete DATA-6 file system** |

---

### 17. What the Script Does NOT Do

- Does not write derivation Python modules (hand-written).
- Does not write display scripts (hand-written).
- Does not write test scripts (hand-written).
- Does not write documentation (hand-written).
- Does not run any derivations — it only records what the derivations ARE (inputs, outputs, method). The actual computation happens when the derivation modules are executed.
- Does not validate physics — it transcribes from the platform libraries. The platform libraries are already verified (322/323).

---

### 18. Single-File Execution

```
python generate_data6.py

Expected output:
  Phase 1: Created 85 directories
  Phase 2: Allocated 350 IDs (max ID: 6002)
  Phase 3: Wrote 7 SI constants
  Phase 4: Wrote 40 Q335 transcendentals
  Phase 5: Wrote 120 measured constants
  Phase 6: Wrote 90 derived entities
  Phase 7: Wrote 83 connections
  Phase 8: Wrote 34 evidence files
  Phase 9: Wrote 9 program files
  Phase 10: Wrote 6 index files
  
  VERIFICATION:
    Entity index: 350 entries, all paths exist
    Derivation index: 160 entries
    Connection index: 83 entries, all IDs resolve
    Spot checks: 10/10 values match phys24_lib
  
  TOTAL: 389 files written to data6/
  generate_data6.py: COMPLETE
```

---

*This plan is complete. Next prompt: write the script.*
