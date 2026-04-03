## Bijection: Session 4 vs phys24_boundaries.py

**Purpose:** Map what I did in Session 4 regarding boundaries, thresholds, and scale traversal against the structured boundary map library.

---

### OVERVIEW

phys24_boundaries.py provides something my Session 4 scripts fundamentally lacked: a traversable map of physical reality organized as a boundary stack. My scripts treated each energy scale as an isolated computation. The boundary library treats the entire energy landscape as a connected structure where crossing a boundary changes the rules — exactly the soliton boundary concept from R5.

---

### THE BOUNDARY STACK vs MY THRESHOLD TREATMENTS

**What boundaries provides:** 17 boundaries from Planck (10¹⁹ GeV) to gravitational dominance (~0.1 m), each with: scale, what changes, coupling values (or None), forces affected, DATA-4 links, papers, and open questions.

**What I did:** Threshold computations in PHYS-27, 30, 34, 35 — but each was standalone.

| Boundary | In boundaries library | What I did in Session 4 |
|---|---|---|
| Planck scale | Full entry with open questions | Mentioned in PHYS-35 addendum (speculative) |
| GUT unification | Full entry, estimated 3.5×10¹⁵ GeV | Computed in PHYS-27/30/34 as L_GUT, never stored |
| CD threshold | Full entry with M_VL window [1.5, 6] TeV | PHYS-35: scanned M_VL from 200–6000 GeV |
| Top quark | Full entry at m_t = 172570 MeV | Never explicitly used as threshold |
| Higgs | Full entry at m_H = 125200 MeV | Never explicitly used as threshold |
| M_Z (electroweak) | Full entry with all coupling values stored | Used as starting scale in every script |
| W boson | Full entry at M_W = 80369.2 MeV | Never explicitly used |
| Bottom quark | Full entry at m_b = 4183 MeV | Never explicitly used |
| Tau lepton | Full entry with Koide note | PHYS-33: Koide prediction at m_tau |
| Charm quark | Full entry at m_c = 1273 MeV | Never explicitly used |
| Confinement wall (upper) | 2000 MeV with perturbativity flag | Noted in papers but never computed |
| Confinement wall (lower) | 300 MeV with f_pi | Noted in papers but never computed |
| Strange quark | Full entry INSIDE confinement wall | Never used |
| Muon | Full entry at m_mu | PHYS-33: Koide input |
| Nuclear binding | 8 MeV with E_D | Never used |
| Electron | Full entry at m_e | PHYS-33: Koide input, PHYS-5 VP reference |
| Atomic / molecular / gravitational | Three macroscopic entries | Never used |

**Key gap:** I traversed the M_Z to M_GUT range extensively but never formalized it as boundary crossings. The boundaries library treats each particle threshold as a named, queryable object. My scripts treated the M_Z → M_GUT run as a continuous integration with no awareness of the intermediate boundaries.

---

### THE TRAVERSAL FUNCTIONS vs MY COMPUTATIONS

**What boundaries provides:**
- `boundaries_between_scales(E_lo, E_hi)` — returns all boundaries crossed
- `traverse(start, end)` — returns report with boundaries, unknowns, open questions
- `print_traversal(start, end)` — human-readable report

**What I did:** Nothing comparable. My scripts computed alpha_s or sin²θ_W as a single integration from M_Z to M_GUT without querying what boundaries were crossed.

| Feature | My scripts | Boundary library |
|---|---|---|
| "What boundaries exist between M_Z and M_GUT?" | Never asked | `boundaries_between_scales(M_Z, 10^19)` |
| "What couplings are unknown at the GUT scale?" | Computed but never catalogued | `traverse()` reports unknown_couplings |
| "What open questions exist along the path?" | In paper text | `traverse()` collects open_questions |
| "Does the CD threshold fall in this range?" | Assumed yes, hardcoded M_VL | Boundary entry with window [1.5, 6] TeV |

**The operational difference:** The boundary library makes the STRUCTURE of the computation visible. My scripts embedded the structure implicitly in the integration code. A future session reading my scripts must infer where boundaries are. A future session using the boundary library can query them.

---

### THE FORCES REGISTRY vs MY FORCE DESCRIPTIONS

**What boundaries provides:** `FORCES` dict with 5 forces: gravity, electromagnetic, weak, strong, unified. Each has gauge group, coupling name, mediator, range, status, and paper links.

**What I did:**

| Force | In boundaries library | What I said in papers |
|---|---|---|
| Gravity | "classical only — no verified quantum description" | PHYS-35 addendum: "gravity through the vortex — inertia determines gravitational coupling" |
| Electromagnetic | "complete QFT, tested to 4.3 ppb" | Referenced in PHYS-27/34 via alpha_EM |
| Weak | "complete QFT, broken by Higgs" | Referenced via sin²θ_W |
| Strong | "complete QFT, non-perturbative below ~2 GeV" | Referenced via alpha_s, confinement wall noted |
| Unified | "hypothetical — CD predicts M_GUT ~ 10^15.5 GeV" | Computed in PHYS-27/30/34, never catalogued as a force |

**Match:** The boundary library's force registry is accurate and consistent with my Session 4 work. The gravity entry correctly notes "G untested across any soliton boundary" — which is exactly what PHYS-3 established.

---

### THE CD BOUNDARY — CRITICAL COMPARISON

The boundary library has a CD threshold entry with:
- M_VL window: [1.5, 6] TeV
- Above: betas = (25/6, −13/6, −20/3), gap = 38/27
- Below: betas = (41/10, −19/6, −7), gap = 218/115
- Open questions: "What is M_VL exactly? Sharp or smooth? Mixing angles?"

**What I found in PHYS-35 that CHANGES this boundary:**

| Property | Boundary library (pre-Session 4) | PHYS-35 finding |
|---|---|---|
| Threshold type | Sharp step function at M_VL | Step function is 12× WORSE than no threshold |
| CD active below M_VL | No (frozen vortex) | Yes (geometric overlaps persist at all scales) |
| Best prediction method | SM below M_VL, CD above | CD betas from M_Z — no threshold |
| Open question: sharp or smooth? | Listed as open | Answered: smooth is even worse than sharp |
| PHYS-35 addendum | Not anticipated | "Frozen vortex" model needs revision |

**DATA-5 must update this boundary.** The PHYS-35 finding changes the physical interpretation:

```
OLD (boundary library): 
  Below M_VL: SM betas only. CD is frozen.
  
NEW (after PHYS-35):
  Below M_VL: CD cannot be excited as a real particle,
  but geometric overlaps persist. No-threshold gives 12× 
  better predictions. Step function is a poor approximation.
  The boundary is about EXCITATION, not EXISTENCE.
```

This is the single most important correction from Session 4 to the boundary library.

---

### THE CONFINEMENT WALL vs MY TREATMENT

**What boundaries provides:** Two boundaries — upper face (2 GeV) and lower face (300 MeV) — marking the non-perturbative zone where integer beta rules cease to apply.

**What I did:** Mentioned in paper text and in the soliton boundary map (PHYS-35 addendum), but never treated computationally because none of my scripts operated below 2 GeV.

**Match:** The boundary library's confinement wall treatment is correct and consistent with my descriptions. The note that the strange quark threshold is INSIDE the wall is important — the library correctly flags that perturbative beta running doesn't apply there.

---

### THE SCALE CONVERSIONS vs MY COMPUTATIONS

**What boundaries provides:** `energy_to_distance_fm()` and `distance_fm_to_energy()` using ℏc = 197.33 MeV·fm. Plus `DISTANCE_SCALES` dict with landmarks from Planck length to observable universe.

**What I did:** Never converted between energy and distance. All my computations stayed in energy units (MeV or GeV, via L = ln(μ/M_Z)/(2π)).

**What DATA-5 should adopt:** The scale conversion is useful for the boundary map's distance column and for making the physics intuitive. My PHYS-35 addendum discusses "the CD field exists at all scales" — having the distance equivalents makes this concrete (the CD's Compton wavelength at M_VL = 500 GeV is ~0.4 fm, inside the proton).

---

### WHAT THE BOUNDARY LIBRARY HAS THAT MY SCRIPTS LACKED

| Feature | Impact |
|---|---|
| Named, queryable boundaries | A future session can ask "what changes at M_Z?" |
| Coupling values AT each boundary | The M_Z entry stores all three inverse couplings |
| None markers for unknowns | The GUT and Planck entries honestly mark what's unknown |
| Open questions per boundary | Documented research directions at each scale |
| Force registry with status | Tracks which forces have complete QFT and which don't |
| Traversal functions | Can ask "what do I cross between A and B?" |
| Distance scale equivalents | Makes energy scales physically intuitive |
| Confinement wall as two boundaries | Upper face (perturbative breakdown) and lower face (hadronic regime) separately named |
| Macroscopic boundaries (atomic, molecular, gravitational) | Extends the map beyond particle physics |

---

### WHAT MY SESSION 4 FOUND THAT THE BOUNDARY LIBRARY NEEDS

| Finding | Boundary affected | Required update |
|---|---|---|
| No-threshold advantage = 12× | CD boundary | Add PHYS-35 finding, revise "frozen vortex" model |
| Soft threshold is worse | CD boundary | Add to open questions: "smooth transition makes predictions worse" |
| Two-loop sin²θ_W overshoots 3/13 | GUT boundary | Add PHYS-34 finding: 2L overshoots, within method uncertainty |
| Minimal SU(5) disfavored | GUT boundary | Add PHYS-29 finding: M_X/M = 23,228 |
| α_s = 0.11838 (0.33% miss) | M_Z boundary | Add prediction to coupling values |
| sin²θ_W = 0.23133 (0.048% miss) | M_Z boundary | Add prediction |
| Koide m_tau = 1776.97 (0.006%) | Tau boundary | Add prediction |
| Track B parked (p = 0.81) | — | Add to closed paths (not a boundary, but a path closure) |
| b₃' = −20/3 decomposed | — | Add to CD boundary metadata |
| VL db_ij (9 Fractions) | CD boundary | Add two-loop data |

---

### THE THREE-LIBRARY → DATA-5 MERGE FOR BOUNDARIES

The boundary library integrates with derivations and structures:

```
BOUNDARY STACK boundary at M_Z
  → STRUCTURES: PARTICLE_CATALOG lists what's active
  → DERIVATIONS: derive_couplings() extracts 1/α₁, 1/α₂ from stored values
  → BOUNDARIES: couplings_at_boundary stores the results

BOUNDARY STACK boundary at CD threshold
  → STRUCTURES: CABIBBO_DOUBLET object with (3,2,1/6) properties
  → DERIVATIONS: compute_vl_one_loop() gives (1/15, 1, 1/3)
  → BOUNDARIES: above/below betas stored, PHYS-35 finding appended

BOUNDARY STACK traversal M_Z → M_GUT
  → DERIVATIONS: run_two_loop_euler() integrates the coupled RGEs
  → BOUNDARIES: traverse() reports boundaries crossed, unknowns, questions
  → STRUCTURES: GUT_PARTICLES provides threshold coefficients
```

DATA-5 merges these three into one queryable platform. The boundary stack becomes a section of data5.py, with traversal functions, the PHYS-35 corrections, and all Session 4 predictions filled in.

---

*End of bijection. The boundary library provides the traversable map my Session 4 scripts lacked. The critical update: PHYS-35 changes the CD boundary from "frozen vortex below M_VL" to "geometric overlaps persist at all scales — step function is 12× worse." The M_Z boundary needs Session 4 predictions added. The GUT boundary needs PHYS-29 and PHYS-34 findings. DATA-5 merges boundaries with derivations and structures into one queryable platform.*
