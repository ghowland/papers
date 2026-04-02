## HOWL Series Paper Index

**For sessions starting from PHYS-24. You do not need to read these papers. This index tells you what is in each one so you can request a specific paper if your current computation needs depth beyond the lexicon.**

---

### MATH Series (6 papers)

The MATH papers build the arithmetic and analytical infrastructure. They establish the exact integer/rational computation standard and the transcendental constant basis.

**MATH-1: R₂ = π/4 as Universal Geometric Remainder**

Establishes the series method. The factor π/4 is not a curiosity — it is the 2D circular-to-rectilinear conversion that appears in every domain where circular geometry meets integer/rectilinear framing. The paper catalogs its appearance across 9 engineering domains (pipe flow, antenna gain, bearing load, orifice discharge, cable bundling, optical aperture, column buckling, heat conduction, fastener stress) and 9 physics domains (QED coupling α/π, Thomson cross-section, Bohr magneton, cyclotron radiation, blackbody peak, Fresnel zones, quantum conductance, Aharonov-Bohm, Landauer transport). Introduces the decomposition Q = F × β × d² × Z where β = π/4 is the geometric transformation and Z is the domain coordinator. This is the structural grammar for the entire series.

**Request this if:** you need the cross-domain decomposition framework, the R₂ domain catalog, or the Q = F × β × d² × Z architecture.

**MATH-2: Integer Pairs at 100 Digits**

Solves the arithmetic transport problem. Transcendental constants (π, e, ln 2, ζ(3), etc.) are represented as integer numerator / 2^335 denominators, giving 101+ digits of precision in exact rational form. This is the Q335 basis. Every constant in phys24_lib.py traces back to a numerator computed in this paper. Demonstrates that integer-pair arithmetic reproduces mpmath at 100 digits for all 22 core constants. Compression ratio ~50× over the MATH-1 paired-fraction representation.

**Request this if:** you need to understand how the Q335 numerators were computed, want to extend the basis to new constants, or need the series convergence analysis for the generating functions (arctan, arctanh, Newton sqrt, Borwein zeta).

**MATH-3: Extended Basis and the QED Frontier**

Extends the Q335 basis from 22 to 31 constants. Adds: ζ(7), ζ(9), Li₄(1/2) through Li₇(1/2), Catalan's constant, e^π, ln(3), ln(5), and complete elliptic integrals K and E at k² = 1/4, 1/2, 3/4. These are the constants that appear in higher-loop QED and the Brown-Schnetz period decomposition. The elliptic integrals at k² = 3/4 converge slowly — the original computation gave only 65-68 digits; these were recomputed to 100+ digits during the Session 4 platform build using 800 hypergeometric terms.

**Request this if:** you need the extended transcendental basis, are working on A₃ (3-loop QED) decomposition, or need elliptic integral values at rational k².

**MATH-4: The R_n Sequence and Dimensional Remainders**

Defines the dimensional remainder sequence: R₂ = π/4 (2D), R₄ = π²/32 (4D), and the general pattern. R₂ appears in every 2D phase-space or cross-section computation. R₄ appears in every 4D loop integral. The QED perturbation series is an expansion in α/(4R₂) = α/π. The paper establishes that these geometric invariants are not incidental — they encode the relationship between integer-basis computation and curved-space integration in each dimension.

**Request this if:** you need the R_n dimensional hierarchy, the connection between R₄ and loop integrals, or the α/π expansion structure.

**MATH-5: The Shared Execution Basis**

Consolidates the Q335 = 2^335 basis as the canonical computation platform. Demonstrates that all series constants share one denominator, enabling integer addition/subtraction of numerators directly. This is the implementation paper for what phys24_lib.py now provides. Establishes that 335 bits gives 101 decimal digits with room for rounding control.

**Request this if:** you need the bit-depth analysis, the rounding protocol for Q335 encoding, or the compression comparison against earlier MATH-1/MATH-2 representations.

**MATH-6: The 82/82 Independence Record**

The PSLQ consolidation paper. Tests 82 constants against a 20-element transcendental basis with maxcoeff = 10,000. Three categories: physical constants (59 tests, 4-15 digits), dynamical constants like Feigenbaum δ (3 tests, 10-30 digits), and analytical constants including Bessel zeros (10 tests, 100 digits). All 82 return null. The sanity check finds π² = 6ζ(2) as [1, 0, −6]. The Bessel zeros j₁₁, j₀₁, j₁₂ are independent of the entire basis at 100-digit precision — 70 orders of magnitude more discriminating than the SM parameter tests.

Establishes the methodological conclusion: derivation beats search. Three parameter reductions came from physics (θ_QCD, α↔a_e, Koide conditional). Zero came from PSLQ.

**Request this if:** you need the full PSLQ record, want to run new targeted PSLQ tests (e.g., on Koide amplitudes), or need the independence methodology.

---

### DATA Series (4 papers)

The DATA papers build and certify the measurement database.

**DATA-1: Initial Database (68 entries)**

The first structured constant database. Introduces the entry typing system: Type E (exact/defined), Type M (measured), Type A (analytical). Covers SI fundamentals, CODATA electromagnetic constants, lepton and hadron masses.

**Request this if:** you need the original database design rationale. Otherwise, DATA-4 supersedes everything.

**DATA-2: Extended Database (107 entries) with Koide Addendum**

Extends to quark masses, CKM parameters, electroweak observables. The Koide addendum computes K and a² for all three sectors (leptons, down quarks, up quarks) and stores them as database entries. This is where the a² = 1.9999630688 measurement (not the hypothesis a² = 2) was first recorded.

**Request this if:** you need the Koide sector analysis provenance or the quark mass entry rationale.

**DATA-3: Verified Database (123 entries, 32/32 checks)**

The first fully verified database. Introduces the cross-check framework: mass ratio identities (Group A), Q335 analytical identities (Group B), physical relations from SI constants (Group C), Koide derived quantities (Group D), SI exact constants (Group E). Establishes the dependency topology — which entries are independent measurements, which are derived, which are consistency checks.

Introduces Finding 15: lattice ratio independence. FLAG lattice QCD mass ratios (m_c/m_s = 11.783, m_b/m_c = 4.578, m_u/m_d = 0.485) are independent measurements at a common renormalization scale, NOT derivable from individual PDG quark masses at different scales. Discrepancies up to 28% from scale mismatch. This prevents future sessions from concluding the database is corrupted.

**Request this if:** you need the cross-check framework design, Finding 15 details, or the dependency topology. Otherwise, DATA-4 supersedes.

**DATA-4: Complete Database with Cabibbo Doublet Extension (146 entries, 38/38 checks)**

The current active database. Inherits everything from DATA-3, adds Section L (Cabibbo Doublet staged parameters, entries 124-129, Type G) and Section N (GUT/unification parameters, 17 entries, all exact Fractions). Adds 6 new verification checks (Group G, all exact). Introduces Type G (staged — identified by theory, bounded by experiment, not yet measured). Includes the computation traceability map linking entries to papers.

Every value in phys24_lib.py comes from DATA-4. The library IS the executable form of this database.

**Request this if:** you need the full 146-entry database with all metadata, the traceability map, or the Type G staging protocol. The library already contains all the values — you only need the paper for the documentation and provenance chain.

---

### PHYS Series (23 papers)

The PHYS papers are the physics content of the series. They progress from foundational calibration through electroweak anatomy to the Cabibbo Doublet identification and its experimental consequences.

**PHYS-1: Mass Is Inertia**

Establishes the series vocabulary. Mass is resistance to acceleration (inertia), not a substance. Field excitations are standing patterns (vortices in series terminology). This is the interpretive foundation — it prevents later papers from accidentally treating mass as a property particles "have" rather than a measurable interaction parameter.

**Request this if:** you need the series' physical vocabulary definitions.

**PHYS-2: Couplings Run**

Introduces the running coupling concept in series language. Coupling constants are not constants — they are scale-dependent readings connected by transformation laws (the beta functions). The transformation law is more fundamental than any single reading. This paper establishes that the beta coefficients are Level 1 (framework-determined exact rationals) while the coupling values at any scale are Level 2 (universe-supplied measurements).

**Request this if:** you need the Level 1/Level 2 distinction applied specifically to running couplings.

**PHYS-3: G Is Untested Across Boundaries**

Notes that Newton's gravitational constant G has never been measured across a soliton boundary (phase transition, confinement wall, etc.). All measurements are in the same vacuum domain. This is an observational gap, not a claim that G varies. Establishes the series principle that untested assumptions should be identified explicitly.

**Request this if:** you are working on gravitational measurements or boundary-crossing physics. Otherwise not needed.

**PHYS-4: The Test Program**

Outlines what the series intends to test computationally. A roadmap paper. Largely superseded by PHYS-24's work queue.

**Request this if:** you need the original motivation for specific computation targets. Otherwise PHYS-24 Section 16 supersedes.

**PHYS-5: α Running at 0.02 ppm**

First hard computational result. Demonstrates electromagnetic coupling running in exact rational arithmetic using vacuum polarization. Reproduces the known α(M_Z) from α(0) using the Fraction computation chain. Establishes that the series arithmetic standard actually works for real physics computation, not just constant tabulation.

**Request this if:** you need the vacuum polarization computation framework, or are working on α_EM running for the boundary-law program.

**PHYS-6: Confinement Two-Face**

Corrects and refines PHYS-5. The confinement region (~0.3-2 GeV) is not a single wall but has two faces: the outside/perturbative face where α_s is still tractable, and the inside/resonant/hadronic face where perturbation theory breaks down. The series treats this as a soliton boundary with distinct inside and outside readings. Establishes the kernel-dependence principle: what you see depends on which side of the boundary you observe from.

**Request this if:** you are working near the confinement scale or need the two-face boundary concept.

**PHYS-7: θ_QCD = 0 and the First Parameter Reduction (19 → 18)**

Reframes the strong CP problem. θ_QCD = 0 is the energy minimum of the QCD vacuum — it requires no axion or other mechanism because the ground state of the integer-topological system is θ = 0. This eliminates one free parameter. The series treats this as confirmed: 19 → 18.

**Request this if:** you need the θ_QCD = 0 argument or the parameter reduction chain.

**PHYS-8: Koide Decomposition and the Conditional Parameter Reduction (18 → 17)**

Decomposes the Koide formula. K = (1+a²/2)/3 is the PHYS-8 identity — the Koide ratio depends on the amplitude a only, not on the phase θ₀ or the scale M. At a² = 2, K = 2/3 exactly. This conditional reduces the parameter count by 1 (m_τ predicted from m_e and m_μ) but only IF a² = 2 is eventually derived from physics. The Koide prediction for m_τ is 1776.97 MeV, 0.91σ from the PDG value 1776.86 MeV.

**Request this if:** you need the Koide decomposition, the PHYS-8 identity, or the conditional parameter reduction logic.

**PHYS-9: The Electromagnetic Integer Chain (α → a_e at 4.3 ppb)**

Demonstrates that the entire electromagnetic measurement chain — from α through QED perturbation theory to the electron anomalous magnetic moment a_e — can be expressed as an integer transformation chain. The 4-loop QED prediction of α⁻¹ from a_e matches CODATA to 4.3 parts per billion. This is the series' strongest demonstration that integer/rational arithmetic captures real physics at frontier precision.

**Request this if:** you need the QED perturbative chain, the α↔a_e connection, or the A₂/A₃ coefficient structure.

**PHYS-10: Quotient and Remainder as Observable**

Promotes the quotient/remainder decomposition from a mathematical convenience to an explicit series principle. When a physical quantity is divided by a geometric invariant (like R₂ = π/4), both the integer quotient and the fractional remainder carry physical information. This paper establishes the vocabulary used in later domain classification.

**Request this if:** you need the quotient/remainder framework or are extending the domain classification.

**PHYS-11: Nine Domains, Three Subgroups**

The R₂ domain classification. Surveys 9 engineering and 9 physics domains where R₂ = π/4 appears, classifies them by the role R₂ plays (geometric conversion, phase-space measure, impedance matching), and identifies three structural subgroups. This is the comprehensive evidence base for R₂ universality.

**Request this if:** you need the full 18-domain catalog or the subgroup classification.

**PHYS-12: Electroweak Integer Anatomy**

Brings the electroweak sector into the integer decomposition framework. Reconstructs M_W, M_Z, the Weinberg angle, and the Fermi constant in exact rational arithmetic. Identifies the integer/rational structure underlying electroweak symmetry breaking. Establishes the computational infrastructure that later papers (PHYS-16, PHYS-19) use for Cabibbo Doublet electroweak effects.

**Request this if:** you need the electroweak Fraction computation framework, or are computing S/T parameters, Z-b-b corrections, or CKM extensions.

**PHYS-13: The Gap Ratio (SM Does Not Unify)**

The pivotal paper. Defines the gap ratio (b₁−b₂)/(b₂−b₃) = 218/115 for the SM. Computes the measured gap ratio from the three couplings at M_Z: 1.358. The 40% miss means the SM does not unify at one loop. This is exact Fraction arithmetic — the miss is not a rounding error. Establishes the gap ratio as the central diagnostic for BSM physics.

**Request this if:** you need the gap ratio derivation, the GUT normalization (the 5/3 factor for U(1)), or the measured gap ratio computation from α⁻¹, sin²θ_W, α_s.

**PHYS-14: The Enumeration**

Systematic enumeration of BSM candidates that could fix the gap ratio. Tests all minimal single-multiplet extensions of the SM by their effect on the gap ratio. 15 candidates enumerated, most eliminated by gap ratio, perturbativity, or anomaly freedom. This is the elimination cascade that produces the Cabibbo Doublet.

**Request this if:** you need the full elimination cascade, the list of all tested representations, or the elimination criteria.

**PHYS-15: The Cabibbo Doublet Identification**

The paper that names and specifies the surviving candidate: (3,2,1/6) vector-like quark doublet. Gap ratio 38/27 = 1.407. Derives the beta shifts from Dynkin index formulas. Shows the Y = 1/6 asymmetry mechanism (Δb₂/Δb₁ = 15). Computes M_GUT = 10^15.5 GeV. First appearance of the Cabibbo Doublet as a named series object.

**Request this if:** you need the Dynkin index derivation, the asymmetry mechanism, or the M_GUT computation.

**PHYS-16: The Cabibbo Doublet Specification**

Full dossier. Representation, quantum numbers, beta shifts, gap ratio, M_GUT, mass window, mixing structure, parameter count (+6), DATA-4 entry numbers. Separates Level 1 properties (fixed by group theory) from Level 2 properties (staged, awaiting measurement). This is the reference document for the Cabibbo Doublet.

**Request this if:** you need the complete CD specification, the 6-parameter list, or the Level 1/Level 2 property separation.

**PHYS-17: Generation Democracy and the Boson Problem**

The explanatory paper. Decomposes SM betas into gauge + Higgs + fermion contributions. Shows that complete fermion generations contribute (4/3, 4/3, 4/3) — identical across all three gauge groups. Fermions are invisible to the gap ratio: their contribution to both numerator and denominator is exactly zero. The SM unification failure is therefore a boson problem. The pure-gauge gap ratio is the Casimir ratio C₂(SU(2))/(C₂(SU(3))−C₂(SU(2))) = 2. The Higgs shifts this from 2 to 218/115.

**Request this if:** you need the beta decomposition by source, the generation democracy proof, or the boson problem explanation.

**PHYS-18: The Unified Transformation Map**

Maps the full transformation structure of the SM: which quantities are transformation laws (Level 1), which are readings (Level 2), how they connect. A structural organization paper.

**Request this if:** you need the full transformation map of SM parameters.

**PHYS-19: Independent Anomaly Evidence for the Cabibbo Doublet**

Documents three experimental anomalies that independently point to (3,2,1/6): CKM first-row unitarity deficit at 2.5-4σ (uses weak doublet quantum number), LEP A_FB^b at ~3σ (uses color + weak), Higgs signal strength excess at ~2σ (uses color triplet). Each anomaly uses a different quantum number of the CD. No shared data, methods, or citations between the gap ratio path and the anomaly path. The independence verification in Appendix D is the key section.

**Request this if:** you need the anomaly evidence details, the independence verification, or the specific experimental references for each anomaly.

**PHYS-20: The Proton Decay Test**

Converts M_GUT to a proton lifetime prediction. τ ∝ M_GUT⁴ gives τ ~ 10^34-35 yr for the CD in minimal SU(5), versus τ ~ 10^37 yr for the MSSM. Super-K bound: τ > 2.4 × 10^34 yr. Hyper-K 20-year sensitivity: ~10^35 yr. The 10^7 ratio in lifetime from a 0.007 difference in gap ratio (38/27 vs 7/5) is the decisive discriminator. Binary outcome: Hyper-K detection confirms CD over MSSM; Hyper-K null at τ > 10^35 excludes minimal SU(5) completion but CD itself survives.

**Request this if:** you need the proton decay calculation, the Hyper-K sensitivity analysis, or the model-dependence assessment.

**PHYS-21: The Level 1 / Level 2 Boundary**

The epistemological framework paper. Assembles the complete boundary map: what is Level 1 (framework-determined), what is Level 2 (universe-supplied), what is Derived. Documents the extension to unobserved particles — the CD is the first time Level 1 arithmetic identifies a particle whose Level 2 properties are not yet confirmed. Historical precedent: charm (GIM 1970 → discovery 1974), W/Z (Weinberg 1967 → discovery 1983), Higgs (BEH 1964 → discovery 2012). Section 9 (What Level 1 Cannot Do) is the guardrail: six explicit limits.

**Request this if:** you need the Level 1/Level 2 classification system, the historical precedent analysis, or the explicit limits on Level 1 claims.

**PHYS-22: The A₂ Geometric Cancellation**

Full standalone treatment of the QED 2-loop coefficient. A₂ = 197/144 + (3/4)ζ(3) + R₄×(8/3 − 16ln2) = −0.3285. Three pieces of distinct mathematical character: rational (diagram combinatorics), number-theoretic (polylogarithm integrals), geometric (4D phase space via R₄). The positive pieces (+2.270) cancel against the geometric piece (−2.598) by 87%. A₂ is small because geometry nearly cancels arithmetic — no known symmetry requires the cancellation. Connection to Brown-Schnetz period decomposition. Seeds the A₃ decomposition.

**Request this if:** you need the A₂ three-piece decomposition, the R₄ connection to loop integrals, or the Brown-Schnetz period framework for extending to higher loops.

**PHYS-23: The Koide C₃ Closure**

Kills the C₃ route to Koide with a double kill. Kill 1 (tautology): the 120° spacing in √m_k = M(1 + a cos(θ₀ + 2πk/3)) is automatic — 3 parameters fitting 3 data points always succeeds. Kill 2 (saddle): K = 2/3 is a saddle point under phase perturbation at a = √2, not a minimum. The C₃ potential does not select K = 2/3. Reformulation catalog: K = 2/3, a = √2, CV(√m) = 1, Var = Mean², midpoint, democratic matrix — all algebraically equivalent, none a derivation. Three-sector data confirms only leptons satisfy K ≈ 2/3. The open problem is sharply stated: derive a² = 2 from physics.

**Request this if:** you need the tautology proof, the saddle point demonstration, the reformulation catalog, or are attempting a new approach to the Koide amplitude.

---

### DISC Series (1 paper)

**DISC-11: Session 3 Capstone**

Complete inventory of all Session 3 work. 98 checks across 6 scripts, all pass. Lists every paper, every script, every finding, every open question. The Session 4 task list in Section 14 is the operational predecessor to this handoff document. PHYS-24 supersedes DISC-11 as the reference document, but DISC-11 has more operational detail about the Session 3 working process.

**Request this if:** you need the complete Session 3 process history or the original Session 4 task list.

---

### Quick Lookup: Which Paper Has What

| If you need... | Request... |
|---|---|
| R₂ = π/4 domain catalog | MATH-1 |
| Q335 numerator computation | MATH-2 |
| Extended basis (elliptic, polylog) | MATH-3 |
| R_n dimensional hierarchy | MATH-4 |
| PSLQ methodology and 82/82 record | MATH-6 |
| Full 146-entry database with metadata | DATA-4 |
| Lattice ratio independence (Finding 15) | DATA-3 or DATA-4 |
| α_EM running infrastructure | PHYS-5 |
| Confinement boundary structure | PHYS-6 |
| θ_QCD = 0 parameter reduction | PHYS-7 |
| Koide decomposition and PHYS-8 identity | PHYS-8 |
| QED integer chain (α → a_e) | PHYS-9 |
| Electroweak Fraction framework | PHYS-12 |
| Gap ratio definition and SM failure | PHYS-13 |
| BSM elimination cascade | PHYS-14 |
| Cabibbo Doublet identification | PHYS-15 |
| Cabibbo Doublet full specification | PHYS-16 |
| Generation democracy and boson problem | PHYS-17 |
| Three anomalies and independence | PHYS-19 |
| Proton decay prediction and Hyper-K | PHYS-20 |
| Level 1 / Level 2 epistemology | PHYS-21 |
| A₂ three-piece decomposition | PHYS-22 |
| Koide C₃ closure (tautology + saddle) | PHYS-23 |
| Everything in one document | PHYS-24 |
