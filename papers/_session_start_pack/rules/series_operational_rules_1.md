# HOWL Series Operational Rules v2

*Include in every paper as a reference section. Governs all MATH, PHYS, and DATA papers.*

*Version: v2, April 6, 2026. Supersedes v1.*

---

## Table R.1: Core Principles

| # | Principle | Rule | Expressed In |
|---|---|---|---|
| R1 | Integers are transformation laws | Every integer in the system maps 1:1 to a gauge group structure constant: beta coefficient, Casimir, Dynkin index, quantum number. No integers appear without group-theoretic provenance. | Every paper |
| R2 | Values run between boundaries | Couplings and masses evolve between soliton boundaries (mass thresholds) according to the integer transformation law active in that domain. Crossing a boundary changes the law by exact rationals. | Every paper |
| R3 | Mass is inertia | Mass IS resistance to acceleration. m appears in F = ma and E = mc². Same quantity. The vortex resists acceleration because redistributing circulating energy requires work. More energy = more resistance = more mass. Tautology, not analogy. | Every paper involving mass |
| R4 | Field is standing pattern is vortex | Three descriptions of one object. The electron is simultaneously a quantum field excitation, a standing wave eigenfunction, and a stable circulating energy pattern. "Vortex" selected because it communicates that the energy circulates, resists disruption, and has quantized structure. | Every paper involving particles |
| R5 | Soliton boundary: integer rules change, values run between | Crossing a soliton boundary changes the integer transformation law. Inside a domain, the coupling runs according to the current law. At the boundary, the law changes by exact rationals (Δb₁, Δb₂, Δb₃). The entire SM energy landscape is domains separated by boundaries, with one blank zone (confinement wall, ~0.3–2 GeV). | Every paper involving running or thresholds |
| R6 | R₂ = π/4 across domains | The 2-ball volume fraction appears in every circular-to-rectilinear conversion. 22 domains confirmed (PHYS-11). Cancels in symmetric ratios. Topological, not dynamical. Three irreducible subgroups. | Papers involving geometric constants |
| R7 | Four levels classify all values | Level 0 = pure geometry/math (π, ζ(3), Bessel zeros). Level 1 = group theory/structural (betas, Casimirs, QED rationals). Level 2 = measured/observational (α⁻¹, sin²θ_W, masses, H₀). Level 3 = derived/predicted (α from a_e, Koide m_τ, Ω_DM from integers). Every value node carries its level. Level 1 law applied to Level 2 measurement produces Level 3 prediction. | Every value |
| R8 | Exact rational arithmetic throughout | Fraction is the primary numeric type. mpf only at the irrational boundary (π, √, exp, log). Float only for display. Q335 = 2³³⁵ basis for transcendentals at 100+ digits. No floating point in the derivation chain. | Every computation |
| R9 | No hardcoded physics constants | Every numerical value consumed by a derivation is read from a versioned value node in the pool by key. Zero physics numbers in executable code. The formula structure lives in the function; the numbers live in the pool. | Every derivation |
| R10 | Every claim backed by experiment with passing comparisons | No assertion without a runnable DATA-6 experiment producing the claimed number, with comparisons evaluated by the runner. Console output is not evidence — result JSON with provenance is evidence. | Every paper |
| R11 | Append-only versioning | All versioned keys follow `canonical_name_vN`. Version 0 is initial registration. New understanding means new version. Old versions are never modified or deleted. Changed data means lost data. | Every node |
| R12 | Falsification is structural | Every program carries kill switches — specific measurements that would falsify the thesis. Every experiment carries comparisons with PASS/FAIL/INFO status. FAIL is data, not a bug. Negative results are findings, not failures. | Every program, every experiment |

---

## Table R.2: The Soliton Boundary Structure

| Element | HOWL Language | Standard Language | Mathematical Content |
|---|---|---|---|
| Domain | Region between two mass thresholds | Energy range where particle content is fixed | Fixed set of active particles, fixed beta coefficients |
| Boundary | Mass threshold of a particle | Decoupling/activation threshold in RG | Energy μ = m_particle where the particle becomes active |
| Integer rules (inside domain) | Beta coefficients as exact rationals | One-loop RGE coefficients | b_i = exact Fraction from gauge group |
| Integer rules change at boundary | Δb_i from the new particle | Threshold matching conditions | (Δb₁, Δb₂, Δb₃) from Dynkin indices of the new representation |
| Value run (inside domain) | Coupling runs between boundaries | RG evolution 1/α_i(μ) = 1/α_i(μ₀) − b_i/(2π) × ln(μ/μ₀) | The coupling value at any scale within the domain |
| Frozen vortex (below threshold) | Particle too heavy to excite | Decoupled heavy particle | Mass > current energy: contributes nothing |
| Active vortex (above threshold) | Particle participates in screening/antiscreening | Light particle in vacuum polarization | Mass < current energy: modifies the running |
| Confinement wall | The blank zone, ~0.3–2 GeV | Non-perturbative QCD, α_s ~ O(1) | No perturbative integer rules. Map marks it blank. |

---

## Table R.3: The Beta Function as Universal Transformation Law

| Domain | What Transforms | Transformation Law | Integer Content | Exception |
|---|---|---|---|---|
| QED (PHYS-5) | α_em(μ) across energy scales | b_em = −(4/3)ΣQ²N_c over active fermions | Q² and N_c from gauge group | Below confinement |
| Electroweak (PHYS-12) | G_F, M_Z, sin²θ_W → 11 observables | Integers from SU(3)×SU(2)×U(1): T₃, Q_f, N_c, n_gen | All coefficients traceable to gauge group | Tree + corrections |
| QCD (PHYS-6) | α_s(μ) across energy scales | b₃ = −11 + (2/3)n_f | 11 from Yang-Mills, 2/3 per flavor | Below Λ_QCD |
| Unification (PHYS-13) | Three couplings toward convergence | b₁ = 41/10, b₂ = −19/6, b₃ = −7 | Every integer from representation content | Two-loop adds corrections |
| Koide (PHYS-8) | Three masses → amplitude and phase | K = (1 + a²/2)/3 | a² = 2 for leptons (Level 2) | Spacing is tautological (PHYS-23) |
| QED coefficients (PHYS-9, 36) | α → a_e via perturbative series | A₁ = 1/2, A₂ = −0.3285, A₃ = 1.1812 | Rational + ζ values per loop | A₄+ involves elliptic integrals (MATH-3 wall) |
| VP screening (PHYS-5) | Bare charge → dressed charge | Δα = (α/3π)ΣQ²N_c × ln(μ/m_f) | Q², N_c, the 3 in 3π | Below confinement: use R-ratio data |

The beta function is not specific to one domain. It IS the transformation law. The values run. The rules are integers.

---

## Table R.4: The Vortex-Field-Wave Tautology

| Description | What It Emphasizes | Mathematical Object | Example |
|---|---|---|---|
| Quantum field | Operator structure, creation/annihilation | φ(x) operator on Fock space | The electron field ψ(x) |
| Standing wave | Spatial pattern, nodes and antinodes | Eigenfunction of the Hamiltonian | Hydrogen atom orbitals |
| Vortex (HOWL term) | Circulation of energy, resistance to disruption, quantized structure | Topologically stable field configuration | The electron as a stable vortex in the Dirac field |

These are three names for one thing. The connection to inertia: the vortex resists acceleration because redistributing a circulating energy pattern requires work. More energy in the vortex = more resistance = more mass. This is why mass IS inertia — the vortex description makes the identity obvious.

---

## Table R.5: Nomenclature Mapping

| HOWL Term | Standard Term | Mapping Type | Notes |
|---|---|---|---|
| Vortex | Particle / field excitation | Tautology | Three descriptions of same object |
| Inertia | Mass | Tautology | Mass IS inertia, not "proportional to" |
| Soliton boundary | Mass threshold / phase boundary | Isomorphic | Integer rules change at boundary |
| Domain | Energy range with fixed particle content | Isomorphic | Between consecutive thresholds |
| Run | RG running / RG evolution | Isomorphic | Coupling value changes within domain |
| Integer rule | Beta coefficient / quantum number | Bijection | 1:1 map to gauge group mathematics |
| Gap ratio | (b₁−b₂)/(b₂−b₃) | Definition | Exact rational from betas |
| Generation democracy | Δb₁ = Δb₂ = Δb₃ per complete generation | Theorem | Fermions cancel in gap ratio |
| Boson problem | Gap ratio set by gauge + Higgs only | Theorem | From generation democracy |
| Cabibbo Doublet | (3,2,1/6) vector-like quark doublet | Named entity | Integer-forced BSM candidate |
| Confinement wall | Λ_QCD non-perturbative boundary | Isomorphic | The blank zone in the map |
| Q335 | 2³³⁵ integer rational basis | Definition | 100-digit transcendentals as exact Fractions |
| R₂ | π/4 = 2-ball volume fraction | Mathematical identity | Disk in square |
| DATA-6 | Versioned node experiment system | Definition | 414+ values, 61+ derivations, 17+ experiments |

---

## Table R.6: The DATA-6 System

| Component | What It Is | Count | Rule |
|---|---|---|---|
| Value node | An atomic named fact with key, value, type, level, source | 414+ | Every physics number is a value node. No exceptions. |
| Derivation | A versioned callable function reading from pool, returning outputs | 61+ | Follows the callable contract (R.8). Zero hardcoded constants. |
| Connection | A relationship bundle across values or domains | 9 | Hierarchy, convergence, cancellation, traceability, adjacency |
| Experiment | A JSON spec declaring execution plan, comparisons, diagrams | 17+ | Self-contained. Runner is generic. Physics is in JSON and functions. |
| Result | Output record of a completed experiment run | 10+ | Versioned as `_runNNN`. Immutable once written. |
| Program | A research thesis with kill switches and connections | 13 | Status: ACTIVE, CONFIRMED, PARKED, BLOCKING, KILLED |
| Dataset | A version overlay for what-if scans | 0 (specified) | Candidate-prefixed keys prevent last-wins collision |
| Diagram | A rendering spec embedded in an experiment | 16+ | Produced by `data6.py diagram`, not by hand |

---

## Table R.7: The Session Workflow

| Phase | What Happens | Output | Rule |
|---|---|---|---|
| **1. Review** | Read prior transcripts, check pool state with `data6.py search` and `data6.py info`, identify what exists and what's missing | Pool state inventory, gap list | No code until review is complete |
| **2. Plan** | Design the experiment: derivations, value nodes, comparisons, expected results (including expected failures) | Written plan with tables | State the physics question and what each outcome means |
| **3. Agreement** | Present the plan. Wait for explicit agreement. Identify pitfalls. Check for key collisions, convention traps. | Explicit agreement from human | Never write code before agreement |
| **4. Code** | Write: (a) value node JSON, (b) experiment JSON, (c) derivation functions, (d) registry additions. All in chat. | Pasteable code blocks | Targeted work only — no changes beyond what's requested |
| **5. Run** | Human runs `data6.py run experiment_name_v0`. Paste output. Fix bugs if any. | Experiment result | Fix only what's broken. Preserve working code. |
| **6. Report** | Write full experiment report: results table, what passes mean, what failures mean, what survives, what's ruled out, forward path | Report in chat | Negative results get full reports. FAIL is a finding. |
| **7. Paper** | After all experiments complete: paper → appendix tables → 20 diagram candidates → top 8 selected → diagram script | Paper, appendices, script | Paper is written AFTER experiments, not before |

---

## Table R.8: Derivation Contract

| Element | Requirement |
|---|---|
| Signature | `def derivation_name_v0(value_dicts: list[dict]) -> dict` |
| Input reading | `vm = _value_map(value_dicts)` then `_frac(vm, key)` for Fractions, `_mpf_val(vm, key)` for approximate, `_get(vm, key)` for raw values or prior derivation outputs |
| Output format | `{"key": "derivation_name_v0", "outputs": {"result_key_v0": value, ...}, "notes": "..."}` |
| Arithmetic | Fraction for rational steps. mpf at irrational boundary. `_f2m()` to convert Fraction to mpf. `_approx()` for output formatting. |
| Precision | `mp.dps = 50` (or higher) inside the function. Save and restore `old_dps` at exit. |
| Hardcoded values | Zero. Every number from the pool by key. |
| Forward check | Any derivation that inverts a relationship (solving for x given f(x) = y) must plug the result back through the forward formula and compare. |
| Registration | Added to `DERIVATION_MORE_INDEX_V0` with category comment. Categories A through T (and growing). |

---

## Table R.9: Experiment JSON Structure

| Field | Required | Content |
|---|---|---|
| `key` | yes | `experiment_name_v0` — must NOT contain the substring `_run` |
| `canonical` | yes | `experiment_name` without version |
| `node_type` | yes | `"experiment"` |
| `description` | yes | What the experiment tests. Include speculation warnings where appropriate. |
| `purpose` | yes | Which program this serves (`program_name_v0`) |
| `dependencies.values` | yes | All value nodes consumed, as `{"canonical": version}` |
| `dependencies.derivations` | yes | All derivation functions called |
| `execution_plan` | yes | Ordered list of versioned derivation keys |
| `comparisons` | yes | List of checks: label, output_key, match_mode, expected/lo/hi |
| `diagrams` | optional | Rendering specs for `data6.py diagram` |

**Comparison modes:** `exact` (Fraction equality), `digits` (N-digit string match), `range` (lo ≤ value ≤ hi), `miss_pct` (always INFO — reports miss%), `bool` (boolean equality).

**Status values:** PASS, FAIL, INFO, SKIP. Zero FAIL = complete. Any FAIL = partial. INFO is informational — records the number, does not judge.

---

## Table R.10: Paper Writing Rules

| Rule | Content |
|---|---|
| Written after experiments | The paper reports experiment results. Never written before the experiments run. |
| Self-contained | Every concept needed for comprehension explained within the paper. |
| Level classification | Every derived result classified as Level 0/1/2/3. The boundary between framework and universe is explicit. |
| Non-claims section | Every paper states what it does NOT claim. |
| Falsification criteria | Every paper lists specific conditions that would falsify its results. |
| Input accounting | How many measured inputs, how many derived outputs, the surplus. |
| Appendix tables | Detailed results in numbered tables (A.1, A.2, ...). Physics-focused, not code-focused. |
| Diagrams | 8 per paper. Follow D1-D17. 20 candidates, top 8 by score, at least 4 different types from the approved list. |
| Series header | HOWL Series, paper number, date, domain, status, AI usage disclosure. |
| DATA-6 reference | Experiment key, run number, timestamp. Full reproducibility chain. |

---

## Table R.11: Diagram Rules (Summary)

| Rule | Content |
|---|---|
| D1-D3 | One script per paper, 8 PNG figures, written in chat after paper is complete. 20 candidates enumerated, top 8 selected. |
| D4 | Diagrams show what text cannot: curves, scales, geometries, thresholds, connections. If a table or sentence is equally clear, it is NOT a diagram. |
| D5 | 8 approved types: Running/Convergence, Scale/Landscape, Threshold/Region, Geometric Cross-Section, Connection/Integer Map, Comparison Bar, Progression/Sequence, Identity Card (max 1 per paper) |
| D6 | Prohibited: program flowcharts, survival box lists, verification ledgers, text-in-boxes, success/failure bar charts, generic motivational graphics |
| D7-D9 | Dark background (#0a0a12), standard palette (GOLD/SILVER/CYAN/MAG/BLUE/GREEN/RED/ORANGE/WHITE/DIM/PURPLE), 180 DPI, tight bounding box, 2× default margins |
| D10 | Geometric diagrams use matplotlib.patches. Labels outside features with leader lines. |
| D14 | Score: +2 curve/geometry, +2 impossible in text, +1 quantitative, +1 cross-section, −2 table-as-image, −2 flowchart, −1 repeat from prior paper |
| D15 | Placement table with markdown for each figure. Captions self-contained. |
| D16-D17 | No text outside axis limits. No `transform` with negative y. Arrows point from text to data. Measurement bands as nested axhspan. Log scales need labeled landmarks. |

Full rules in `diagram_script_rules.md`.

---

## Table R.12: Program and Falsification

| Status | Meaning | Action |
|---|---|---|
| ACTIVE | Experiments ongoing, thesis under test | Run next experiment on the attack path |
| CONFIRMED | All kill switches survived, all experiments pass | Document in paper. No further experiments needed. |
| PARKED | Blocked by external dependency | Note the blocker. Revisit when blocker resolves. |
| BLOCKING | This program must complete before another can be confirmed | Highest priority. The gate dependency is explicit. |
| KILLED | A kill switch was triggered | Document the negative result. Branch is dead. Parent program may survive if other branches remain. |

**Kill switch protocol:** When a comparison triggers FAIL on a kill-switch condition, the branch is marked KILLED. The FAIL result is permanent. The result JSON is never deleted. The finding is documented in the report and the paper.

**Negative results are findings.** An experiment showing N < 1 for the VP step is as valuable as one showing 12-digit agreement for α. Both constrain the theory. Both get full reports. Both go in the paper.

---

## Table R.13: Pitfall Registry

| # | Pitfall | What Went Wrong | Prevention Rule |
|---|---|---|---|
| 1 | Coupling inversion | 1/α₂ = α_inv/sin²θ vs sin²θ × α_inv (19× wrong) | Verify coupling extraction against PDG table |
| 2 | Last-wins collision | All what-if candidates overwrite same key | Candidate-prefixed keys, independent experiments |
| 3 | Laporta convention | C81 sum ≠ A₄ (different convention, 2752 ppb wrong) | Forward check on every inversion derivation |
| 4 | `_run` in experiment key | Runner splits on `_run` for result numbering | Never use `_run` as substring in experiment keys |
| 5 | Float in derivation | Hardcoded `0.23122` instead of pool read | `_frac(vm, key)` for every constant |
| 6 | SH0ES duplicate | `cosmo_h0_sh0es_v0` (Fraction) vs `cosmo_h0_shoes_v0` (approximate) | Use Fraction version. Check with `data6.py search` before coding. |
| 7 | Negative y annotations | `transform=ax.get_xaxis_transform()` with negative y balloons PNG | All annotations inside axis limits, data coordinates only |
| 8 | b_ij double-count | Gauge + fermion double-counted in two-loop matrix (10% α_s error) | Two-loop b_ij = fermion contribution only, not gauge + fermion |
| 9 | Mass W value | 80379 vs 80369.2 MeV (old vs current PDG) | Always verify against current PDG before registering |
| 10 | MSSM gap inversion | 5/7 = 0.714 stored instead of 7/5 = 1.400 | Verify gap ratio > 1 for all models (pure gauge gap = 2 is the baseline) |

---

*These rules apply to every paper in the HOWL series. They encode the physics principles, the operational workflow, the system architecture, the vocabulary, and the lessons learned from practice. Tables R.1–R.5 are physics. Tables R.6–R.9 are system. Tables R.10–R.11 are papers and diagrams. Tables R.12–R.13 are falsification and safety. All are operational. None are optional.*

*Full diagram rules: `diagram_script_rules.md` (D1-D17)*

*Full system documentation: DATA-6 paper (Appendices A-V)*
