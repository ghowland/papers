## Bijection: Session 4 Scripts vs phys24_structures.py

**Purpose:** Map what I did in Session 4 against the structured representation library. Identify what I had, what I lacked, what I reinvented, and what DATA-5 should adopt.

---

### OVERVIEW

phys24_structures.py provides something my Session 4 scripts never had: a queryable knowledge base. My scripts were standalone computations — they computed from first principles every time, with no memory of what other scripts had done or what the series had established. The structures library organizes the series' accumulated knowledge into searchable objects: representations, particles, thresholds, closed paths, anomalies, experiments, and paper cross-references.

---

### REPRESENTATION OBJECTS

**What structures provides:** `make_rep()` creates a representation dict with all derived properties — Dynkin indices, Casimirs, beta shifts, electric charges — computed automatically from (SU(3)_dim, SU(2)_dim, Y).

**What I did:** Recomputed from scratch in every script.

| Property | My scripts | phys24_structures |
|---|---|---|
| CD beta shifts | Inline in PHYS-26, 28, 30, 32, 34, 35 — recomputed 6 times | `CABIBBO_DOUBLET["db"]` — computed once |
| CD charges | Inline in PHYS-26 | `CABIBBO_DOUBLET["charges"]` = (2/3, −1/3) |
| CD Casimirs | Inline in PHYS-28 | `CABIBBO_DOUBLET["C2_R3"]` = 4/3, `["C2_R2"]` = 3/4 |
| CD Dynkin indices | Inline in PHYS-26, 28 | `CABIBBO_DOUBLET["S2_R3"]` = 1/2, `["S2_R2"]` = 1/2 |
| SM fermion Q_L shifts | Inline in PHYS-32 | `Q_L["db"]` = (1/15, 1, 2/3) |
| SM fermion u_R shifts | Inline in PHYS-32 | `u_R["db"]` = (8/15, 0, 1/3) |
| Higgs shifts | Inline in PHYS-32 | `HIGGS["db"]` = (1/10, 1/6, 0) |

**Key difference:** The structures library distinguishes chiral (Weyl) and vector-like (Dirac) representations with different SU(3) coefficients:

```
Chiral:       db3 = (2/3) * dim(R2) * S2(R3)
Vector-like:  db3 = (1/3) * dim(R2) * S2(R3)
```

My PHYS-32 script used the (2/3) coefficient for SM Weyl fermions and the (1/3) coefficient for the CD VL pair, but computed each inline. The structures library encodes the distinction in the `rep_type` parameter of `make_rep()`. This is cleaner.

**The Weyl counting discrepancy (PHYS-32):** My script noted a factor-of-4 discrepancy between naive Weyl counting (4 triplets × 1/3 = 4/3) and the VL formula result (1/3). The structures library resolves this by having separate coefficient sets for chiral and VL. The structures library's docstring explains: "a VL pair contributes LESS to b3 than a single chiral fermion because the VL formula accounts for the Dirac structure differently. This is NOT a simple factor-of-2 relationship across all groups." This is better documentation than what I had.

---

### GENERATION DEMOCRACY

**What structures provides:** `generation_betas()` sums the five SM multiplet contributions and returns (4/3, 4/3, 4/3). `total_SM_betas()` adds gauge and Higgs to get (41/10, −19/6, −7).

**What I did:**

| Paper | How I got SM betas |
|---|---|
| PHYS-26 | Traced k₁ and Dynkin formulas from SU(5) |
| PHYS-27 | Used library values b1_mod, b2_mod, b3_mod directly |
| PHYS-30 | Used library values directly |
| PHYS-32 | Decomposed b3 into gauge (−11) + fermion (+4) + Higgs (0) inline |

I never computed SM betas from the multiplet census. I either used the library values or decomposed them after the fact. The structures library constructs them from first principles: define each multiplet → sum per generation → multiply by 3 → add gauge and Higgs. This is the derivation chain my scripts should have used.

**Impact:** The structures library's self-test verifies generation democracy (db1 = db2 = db3 = 4/3) from the census. My PHYS-32 verified it from the decomposition. Same result, different direction.

---

### PARTICLE CATALOG

**What structures provides:** `PARTICLE_CATALOG` — 12 SM particles ordered by mass, each with mass variable, DATA-4 entry ID, representation, and threshold type. `particles_at_scale(mu)` returns active particles. `active_fermion_count(mu)` counts quarks.

**What I did:** Nothing comparable. I hardcoded particle lists when needed.

| Feature | My scripts | phys24_structures |
|---|---|---|
| List of particles by mass | Never constructed | `PARTICLE_CATALOG` sorted by mass |
| Active particles at M_Z | Assumed 5 quarks (known) | `active_fermion_count(M_Z)` = 5 (computed) |
| Threshold crossings | Hardcoded in PHYS-35 as M_VL values | `particles_at_scale()` for any energy |
| DATA-4 linkage per particle | None | `data4` field in each catalog entry |

**What DATA-5 should adopt:** The particle catalog is valuable for future scripts that need to know what's active at a given scale. My PHYS-35 threshold investigation would have been cleaner with this.

---

### ENERGY DOMAINS

**What structures provides:** `ENERGY_DOMAINS` — 5 named domains from QED low through electroweak scale, with energy ranges, descriptions, and perturbativity flags.

**What I did:** Described domains in paper text (PHYS-35 addendum soliton boundary map) but never in code.

| My soliton boundary map | Structures ENERGY_DOMAINS |
|---|---|
| M_Z to M_GUT described in prose | 5 domains from 0 to m_t in code |
| Confinement wall noted at 0.3–2 GeV | "Confinement wall" domain with perturbative=False |
| CD boundary discussed at length | NOT included (CD is in STAGED section, not domain list) |
| M_GUT and beyond described | NOT included (stops at m_t) |

**Gap:** The structures library stops at the electroweak scale. It does not include the CD boundary, the GUT domain, or the Planck boundary. My PHYS-35 addendum goes further but is prose, not code. DATA-5 should extend ENERGY_DOMAINS through M_GUT, including the CD boundary with the PHYS-35 finding that the step-function threshold is inadequate.

---

### GUT COMPLETION

**What structures provides:** `GUT_PARTICLES` dict with X/Y bosons, color triplet Higgs, Sigma octet, and Sigma triplet. Each has representation data, beta shifts, and threshold coefficients.

**What I did:** Computed these in PHYS-29 inline.

| GUT particle | My PHYS-29 | Structures library |
|---|---|---|
| Color triplet Higgs | C_T = −1/12, db = (1/15, 0, 1/12) | Same values |
| Sigma octet | db3 = 1/2 | Same |
| Sigma triplet | db2 = 1/3 | Same |
| X, Y bosons | Mentioned but not computed | Representation (3,2,5/6) stored |

**Match:** The threshold coefficients are identical. The structures library stores them as properties of the GUT particle objects rather than as standalone variables. This is a design choice — DATA-5 can do either.

---

### DATA-4 CROSS-REFERENCE MAP

**What structures provides:** `DATA4_MAP` — complete dict mapping every DATA-4 entry ID to its variable name, value, type code, unit, and digit count. `lookup_data4("B1")` returns the alpha_inv entry. `entries_by_type("E")` returns all exact constants.

**What I did:** Referenced DATA-4 entry IDs in comments but had no programmatic lookup.

**The entry ID issue:** The structures library uses the CORRECT DATA-4 IDs (B1, B11, B12, C1, etc.). My DATA-5 spec v1 renumbered them (B2 for alpha_s instead of B12). The structures library is correct; my spec was wrong. This was fixed in the corrections spec.

**What DATA-5 should adopt:** The DATA4_MAP is exactly what's needed for traceability. Every value links to its source. The lookup functions make it queryable.

---

### PAPER CROSS-REFERENCE AND CLOSED PATHS

**What structures provides:** `PAPER_TOPICS` dict mapping paper numbers to one-line descriptions. `papers_about("koide")` searches. `CLOSED_PATHS` dict with 7 dead ends. `ANOMALIES` dict with 3 experimental anomalies. `EXPERIMENTS` dict with 3 upcoming tests.

**What I did:** Described all of this in paper prose and in the DATA-5 spec, but never in queryable code.

| Feature | My Session 4 | Structures library |
|---|---|---|
| Paper summaries | In plans and summaries | `PAPER_TOPICS` dict |
| Searchable by keyword | No | `papers_about("gap ratio")` → PHYS-13 |
| Closed paths | Mentioned in papers | `CLOSED_PATHS` with kill reason and paper |
| Track B parking | PHYS-31 decision | Not in structures (pre-Session 4) |
| Anomaly evidence | Discussed in plans | `ANOMALIES` dict with sigma, resolution, experiment |
| Experimental timeline | Not tracked | `EXPERIMENTS` dict with status and dates |

**What needs updating for DATA-5:** The structures library predates Session 4. It needs:
- Papers PHYS-25 through PHYS-35 added to `PAPER_TOPICS`
- Track B parking added to `CLOSED_PATHS`
- No new anomalies (none discovered in Session 4)
- Experimental timeline unchanged

---

### THE CRITICAL DIFFERENCE: CHIRAL vs VL COEFFICIENTS

The structures library's `make_rep()` has a subtle but important difference from my inline computations.

**For SU(3):**
```
Chiral (Weyl):     db3 = (2/3) * dim(R2) * S2(R3)
Vector-like (VL):  db3 = (1/3) * dim(R2) * S2(R3)
```

**For SU(2):**
```
Chiral:     db2 = (2/3) * dim(R3) * S2(R2)
Vector-like: db2 = (2/3) * dim(R3) * S2(R2)   [SAME]
```

**For U(1):**
```
Chiral:     db1 = (2/5) * dim(R3) * dim(R2) * Y²
Vector-like: db1 = (2/5) * dim(R3) * dim(R2) * Y²   [SAME]
```

The asymmetry: chiral and VL give the SAME result for U(1) and SU(2), but DIFFERENT for SU(3). The VL SU(3) coefficient is half the chiral coefficient (1/3 vs 2/3).

My PHYS-32 script noted this discrepancy as the "Weyl counting factor of 4" issue. The structures library's docstring resolves it: the VL formula accounts for the Dirac structure differently in SU(3). The chiral formula counts each Weyl fermion's contribution at (2/3)×S₂. The VL formula uses (1/3)×dim(R₂)×S₂ for the complete pair, which gives a DIFFERENT result because it includes the Dirac mass pairing.

**Verification:** SM generation (5 chiral Weyl) gives per-gen betas (4/3, 4/3, 4/3):
- Q_L: db3 = (2/3)×2×(1/2) = 2/3
- u_R: db3 = (2/3)×1×(1/2) = 1/3
- d_R: db3 = (2/3)×1×(1/2) = 1/3
- L_L: db3 = 0 (singlet)
- e_R: db3 = 0 (singlet)
- Total: 2/3 + 1/3 + 1/3 = 4/3 ✓

CD VL pair (3,2,1/6): db3 = (1/3)×2×(1/2) = 1/3 ✓

The structures library's `make_rep()` correctly dispatches on `rep_type`. This is the cleanest resolution of the PHYS-32 Weyl counting issue.

---

### WHAT DATA-5 SHOULD ADOPT FROM STRUCTURES

| Feature | Adopt? | Notes |
|---|---|---|
| `make_rep()` with chiral/VL dispatch | **YES** | Resolves Weyl counting cleanly |
| SM_GENERATION list | **YES** | Canonical multiplet census |
| CABIBBO_DOUBLET object | **YES** | Single source of truth for all CD properties |
| HIGGS object | **YES** | Needed for decomposition |
| `generation_betas()` | **YES** | Derives (4/3, 4/3, 4/3) from census |
| `total_SM_betas()` | **YES** | Derives (41/10, −19/6, −7) from parts |
| PARTICLE_CATALOG | **YES** | Mass-ordered, DATA-4 linked |
| `particles_at_scale()` | **YES** | Useful for threshold investigations |
| ENERGY_DOMAINS | **YES, extended** | Add CD boundary and GUT domain |
| GUT_PARTICLES | **YES** | Threshold coefficients for PHYS-29 |
| DATA4_MAP | **YES** | Complete traceability |
| `lookup_data4()` | **YES** | Queryable by entry ID |
| PAPER_TOPICS | **YES, extended** | Add PHYS-25 through PHYS-35 |
| CLOSED_PATHS | **YES, extended** | Add Track B parking |
| ANOMALIES | **YES** | Unchanged |
| EXPERIMENTS | **YES** | Unchanged |

---

### WHAT STRUCTURES LACKS THAT DATA-5 NEEDS

| Missing from structures | Source | Needed for |
|---|---|---|
| Two-loop b_ij objects per representation | PHYS-28 / derivations lib | Two-loop running |
| Derivation functions | derivations lib | Computing predictions |
| Pitfall documentation | Session 4 experience | Preventing errors |
| Prediction values | PHYS-30, 34, 33 | Recording results |
| Koide functions | derivations lib | Mass predictions |
| No-threshold finding | PHYS-35 | Threshold physics |
| Session 4 paper entries in PAPER_TOPICS | This session | Completeness |

---

### THE THREE-LIBRARY ARCHITECTURE

The bijection reveals that DATA-5 should integrate three existing libraries:

```
phys24_lib.py          → Constants, helpers, check functions
phys24_derivations.py  → Derivation functions, group theory, predictions
phys24_structures.py   → Representations, catalogs, cross-references, closed paths
```

DATA-5 merges all three into one library (data5.py) plus a speed utility (data5_fast.py):

```
data5.py = phys24_lib (all constants, helpers)
         + phys24_derivations (all functions, pitfalls)
         + phys24_structures (all objects, catalogs, cross-refs)
         + Session 4 additions (new values, new papers, new closed paths)

data5_fast.py = Float-speed utilities (Euler, scan, Monte Carlo)
```

The inheritance is strict: every value from phys24_lib, every function from derivations, every object from structures appears in data5.py unchanged. New content from PHYS-25 through PHYS-35 is added. Nothing is removed.

---

*End of bijection. The structures library provides the organizational layer my Session 4 scripts lacked: queryable representations, mass-ordered particle catalogs, energy domain maps, DATA-4 cross-references, paper search, closed paths, and anomaly registries. DATA-5 merges this with the derivation functions and the constant library into one unified platform. The chiral/VL coefficient distinction in `make_rep()` cleanly resolves the PHYS-32 Weyl counting issue.*
