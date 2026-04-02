# HOWL Series Operational Rules

*Include in every MATH and PHYS paper as a reference section.*

---

## Table R.1: Core Principles

| # | HOWL Principle | Standard Physics Nomenclature | Relationship | Expressed In |
|---|---|---|---|---|
| R1 | Transformation laws are integers | Beta function coefficients, quantum numbers, Casimirs, Dynkin indices | Bijection: every integer in a HOWL computation maps 1:1 to a gauge group structure constant | Every paper |
| R2 | Values run | Running couplings α_i(μ), running masses m(μ) | Isomorphic: the "run" is the RG flow between fixed points | Every paper |
| R3 | Mass is inertia | Rest mass = resistance to acceleration (Newton), invariant mass = energy in rest frame (Einstein) | Tautology: mass IS inertia, not "related to" inertia. m appears in F = ma and E = mc². Same quantity. | Every paper involving mass thresholds |
| R4 | Field is standing pattern is vortex | Quantum field = standing wave solution of field equation = vortex (series term) | Tautology: three descriptions of the same energy configuration. "Vortex" selected for explanatory and visual power — the energy circulates, resists disruption, and has quantized structure. | Every paper involving particles |
| R5 | Soliton boundary: integer rules on each side, values run between boundaries | Mass thresholds in RG running; phase boundaries in condensed matter; domain walls in field theory | Isomorphic: crossing a soliton boundary changes the integer transformation law. Inside a domain, the coupling runs according to the current law. At the boundary, the law changes by exact rationals (Δb₁, Δb₂, Δb₃). | Every paper involving running or thresholds |
| R6 | Level 1: determined by framework (integers, geometry) | Gauge group structure, representation theory, topological invariants | Bijection: every Level 1 quantity maps to a mathematical theorem about the gauge group or spacetime geometry | Every paper |
| R7 | Level 2: supplied by the universe (measured values) | Coupling constants, masses, mixing angles, CP phases | Bijection: every Level 2 quantity maps to an experimental measurement in DATA-3 | Every paper |
| R8 | R₂ = π/4 across domains | Volume fraction of n-ball in n-cube for n = 2 | Mathematical identity appearing in 9/9 physics domains (PHYS-11) via three irreducible subgroups | Papers involving geometric constants |
| R9 | Exact rational arithmetic throughout | Fraction arithmetic in Python, Q335 = 2³³⁵ basis for transcendentals | Operational rule: no floating point in the derivation chain. Floating point only for display. | Every paper with computation |
| R10 | Every claim backed by script with passing checks | Reproducible computation with if/else verification | Operational rule: no assertion without a runnable script producing the claimed number with verified checks. | Every paper |

---

## Table R.2: The Vortex-Field-Wave Tautology (Expanded)

| Description | What It Emphasizes | Mathematical Object | Example |
|---|---|---|---|
| Quantum field | The operator structure, creation/annihilation | φ(x) operator on Fock space | The electron field ψ(x) |
| Standing wave | The spatial pattern, nodes and antinodes | Eigenfunction of the Hamiltonian | Hydrogen atom orbitals |
| Vortex (HOWL term) | The circulation of energy, resistance to disruption, quantized structure | Topologically stable field configuration | The electron as a stable vortex in the Dirac field |

These are three names for one thing. The electron is simultaneously a quantum field excitation, a standing wave pattern in the Dirac equation, and a vortex of energy that resists acceleration (inertia) and cannot be split (quantized). The series uses "vortex" because it best communicates to humans that the particle is an active, circulating energy pattern — not a static point or an abstract mathematical object.

The connection to inertia: the vortex resists acceleration because redistributing a circulating energy pattern requires work. More energy in the vortex = more resistance = more mass. This is why mass IS inertia — the vortex description makes the identity obvious.

---

## Table R.3: The Soliton Boundary Structure

| Element | HOWL Language | Standard Language | Mathematical Content |
|---|---|---|---|
| Domain | Region between two mass thresholds | Energy range where particle content is fixed | Fixed set of active particles, fixed beta coefficients |
| Boundary | Mass threshold of a particle | Decoupling/activation threshold in RG | Energy μ = m_particle where the particle becomes active |
| Integer rules (outside boundary) | Beta coefficients as exact rationals | One-loop RGE coefficients | b_i = exact Fraction from gauge group |
| Integer rules change at boundary | Δb_i from the new particle | Threshold matching conditions | (Δb₁, Δb₂, Δb₃) from Dynkin indices of the new representation |
| Value run (inside domain) | Coupling runs between boundaries | RG evolution 1/α_i(μ) = 1/α_i(μ₀) − b_i/(2π) × ln(μ/μ₀) | The coupling value at any scale within the domain |
| Frozen vortex (below threshold) | Particle too heavy to excite | Decoupled heavy particle | Particle with mass > current energy scale contributes nothing |
| Active vortex (above threshold) | Particle participates in screening/antiscreening | Light particle in the vacuum polarization | Particle with mass < current energy scale modifies the running |

The entire SM energy landscape from m_e to M_GUT is a sequence of domains (with integer rules) separated by boundaries (where the rules change by exact rationals). One domain — the confinement wall (~0.3-2 GeV) — has no perturbative rules. This is where α_s → O(1) and the perturbative soliton picture breaks down.

---

## Table R.4: The Beta Function as Universal Transformation Law

| Domain | What Transforms | Transformation Law | Integer Content | Exceptions |
|---|---|---|---|---|
| QED (PHYS-5) | α_em(μ) across energy scales | b_em = −(4/3)ΣQ²N_c over active fermions | Q² and N_c from gauge group | Below confinement: non-perturbative |
| Electroweak (PHYS-12) | G_F, M_Z, sin²θ_W → 11 observables | Integers from SU(3)×SU(2)×U(1): T₃, Q_f, N_c, n_gen | All coefficients traceable to gauge group | Tree + Δρ level; full one-loop adds more integers |
| QCD (PHYS-6) | α_s(μ) across energy scales | b₃ = −11 + (2/3)n_f | 11 from Yang-Mills, 2/3 per flavor | Below Λ_QCD: confinement, non-perturbative |
| Unification (PHYS-13) | Three couplings running toward convergence | b₁ = 41/10, b₂ = −19/6, b₃ = −7 | Every integer from representation content | One-loop; two-loop adds known corrections |
| Koide (PHYS-8) | Three masses → amplitude and phase | K = (1 + a²/2)/3 | a² = 2 for leptons (Level 2, not derived) | Spacing is tautological (PHYS-23) |
| QED coefficients (PHYS-9, PHYS-22) | α → a_e via perturbative series | A₁ = 1/2, A₂ = −0.3285, A₃ = 1.1812 | Rational + ζ values + R₄ per loop | A₄+ involves elliptic integrals (MATH-3 wall) |
| VP screening (PHYS-5) | Bare charge → dressed charge | Δα = (α/3π)ΣQ²N_c × ln(μ/m_f) | Q², N_c, the 3 in 3π | Below confinement: use measured R-ratio data |

The beta function is not specific to one domain. It IS the transformation law. In every domain where perturbation theory applies, the coupling changes across energy scales according to exact rational coefficients determined by the gauge group and the active particle content. The values run. The rules are integers.

Exception: the confinement wall. Below ~2 GeV, α_s ~ O(1) and the perturbative beta function fails. This is the one domain in the entire 0 → M_GUT range where integer rules do not apply. PHYS-6 characterized this wall. The map marks it blank.

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
| Level 1 | Structure from framework | Bijection | Maps to mathematical theorems |
| Level 2 | Value from measurement | Bijection | Maps to DATA-3 entries |
| Gap ratio | (b₁−b₂)/(b₂−b₃) | Definition | Ratio of exact rationals |
| Generation democracy | Δb₁ = Δb₂ = Δb₃ per complete generation | Theorem | From SU(5) anomaly cancellation |
| Boson problem | Gap ratio set by gauge + Higgs only | Theorem | Fermions cancel exactly |
| Q335 | 2³³⁵ integer rational basis | Definition | Denominator for all transcendentals |
| R₂ | π/4 = 2-ball remainder | Mathematical identity | Volume fraction of disk in square |
| R₄ | π²/32 = 4-ball remainder | Mathematical identity | Volume fraction of 4-ball in 4-cube |
| Cabibbo Doublet | (3,2,1/6) vector-like quark doublet | Named entity | Integer-forced, named for Cabibbo angle anomaly |
| Confinement wall | Λ_QCD boundary / non-perturbative QCD | Isomorphic | The blank zone in the map |
| DATA-3 | Verified integer rational database | Definition | 123 entries, 32/32 checks |

---

## Table R.6: What Goes in Every Paper

| Element | Content | Purpose |
|---|---|---|
| Series header | HOWL Series, paper number, date, domain, status | Identification |
| Operational rules reference | "This paper follows HOWL operational rules (Table R.1-R.6)" | Stability across papers |
| DATA-3 reference | "All measured values from DATA-3 (32/32 consistency checks)" | Data provenance |
| Script reference | "Backed by [script name], [N/N] checks pass" | Computational provenance |
| Level 1 / Level 2 classification | Every result classified as Level 1 or Level 2 | Boundary maintenance |
| Self-containment | Every concept needed for comprehension explained within the paper | Accessibility |
| Non-claims section | What the paper does NOT claim | Prevents overclaiming |
| Seeds section | What future computations this paper enables | Forward linkage |

---

*These rules apply to every MATH and PHYS paper in the HOWL series. They encode the physical principles, naming conventions, and operational standards that maintain consistency across papers and sessions. A future session reading any HOWL paper will encounter these rules and operate within them.*
