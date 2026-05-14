# PCTRM Specification Gaps — Completion Document

**Companion to:** PCTRM-1-Master-2026 Planning Document + Macro-Level Coverage Companion

**Purpose:** Enumerate every identified specification gap, pending commitment, and missing derivation target required for PCTRM to reach the complete CODATA table and all confirmed observations. Each item is actionable — it either requires a new commitment in the spec or a derivation within existing mechanisms.

**Status:** Gap inventory for program completion.

---

## I. Structural Commitments Pending Specification

These items require new commitments in the master spec. The mechanisms exist but the specific values or structures have not been declared.

### I.1 Per-Hierarchy-Boundary Moduli

**Location in spec:** Section VII (Dual-Geometry Sectors), Section XI (Mass, Inertia, Higgs)

**What's missing:** The spec commits to mass hierarchy arising from per-hierarchy-boundary modulus generating an indexed family. The topology-specific moduli catalog lists k₈₁ and k₈₃ but states the per-hierarchy-boundary moduli as "family pending specification."

**What's needed:** The complete enumeration of moduli at each hierarchy boundary. Each modulus determines the mass scale at that boundary. Without these, no specific particle mass can be derived from the integer alphabet.

**Scope:** One modulus per hierarchy boundary. The number of boundaries equals the number of distinct mass scales in the Standard Model particle catalog — electron, muon, tau, up, down, strange, charm, bottom, top, W, Z, Higgs. Twelve boundaries minimum, possibly fewer if some share moduli through generation structure.

**Falsification:** Each modulus produces a specific mass prediction. The prediction either matches the CODATA mass value or the modulus is wrong at that boundary.

**Priority:** Critical. This is the single largest gap. The entire mass sector of CODATA is blocked on this.

### I.2 Natural Units to SI Bridge

**Location in spec:** Section II (Cells and Ticks), Section IX (Planck-Scale Locality)

**What's missing:** The spec operates in natural units — cells and ticks. CODATA publishes in SI units — kilograms, meters, seconds, amperes, kelvins, moles, candelas. The derivation chain from integer alphabet through substrate arithmetic to a specific number in specific SI units is not stated.

**What's needed:** An explicit bridging section specifying how dimensional quantities emerge from the dimensionless substrate. The 2019 SI redefinition fixed seven defining constants (c, ℏ, e, k_B, N_A, K_cd, ΔνCs). The spec already has c = 1 cell/tick. The remaining six defining constants need explicit substrate interpretations.

**Specific commitments required:**

- ℏ as one unit of substrate action per tick. The tick is the action quantum. This is implicit in the cell/tick structure but must be stated explicitly with the dimensional bridge to SI joule-seconds.
- Elementary charge e as the electromagnetic channel's unit throughput quantum. Must bridge to SI coulombs.
- Boltzmann constant k_B as the bridge between substrate tick-energy and SI temperature. Must connect thermal channel throughput to kelvins.
- Avogadro constant N_A as a counting number — pure integer, no substrate interpretation needed, but the bridge must state this.
- Cesium hyperfine frequency ΔνCs as a derived substrate prediction — the number of ticks per Cs-133 hyperfine period. This is a specific prediction the spec should make.
- Luminous efficacy K_cd as a human-perceptual quantity outside substrate scope, but the bridge must state this boundary.

**Falsification:** The dimensional bridge either produces consistent SI values across all CODATA entries or it produces contradictions at specific points.

**Priority:** High. Without this bridge, no CODATA comparison is possible in SI units.

### I.3 Charge Quantization from Substrate

**Location in spec:** Section VI (Channels)

**What's missing:** The spec lists electromagnetic channels as "charge-to-charge, always active between charged solitons." The quantization of charge — why charge comes in units of e/3 (quarks) and e (leptons), and why the magnitudes are what they are — is not explicitly committed to.

**What's needed:** The channel structure that forces charge quantization. Specifically: what substrate feature produces fractional quark charges at 1/3 and 2/3, why lepton charges are integer multiples of e, and how the channel structure forbids other charge values.

**Falsification:** The channel structure either produces exactly the observed charge spectrum or it produces charges that don't exist or fails to produce charges that do.

**Priority:** High. Charge quantization is foundational to the entire Standard Model reduction.

### I.4 Color Charge and SU(3) from Channels

**Location in spec:** Section XIV (Standard Model Reduction)

**What's missing:** The spec commits to "gauge group U(1) × SU(2) × SU(3) from channel type enumeration" but the explicit enumeration producing SU(3) is not provided. How do three color charges emerge from the channel primitive? What substrate structure forces exactly three colors, not two or four?

**What's needed:** The channel-counting argument that forces the strong channel to have exactly three internal states, and why those states combine as they do (color singlets for hadrons, color confinement preventing isolated color charge).

**Falsification:** The channel enumeration either forces exactly three colors with the correct combination rules or it doesn't.

**Priority:** High. This is the mechanism behind confinement, which the spec claims via toroidal gluon flux tubes, but the color structure underneath those tubes needs explicit specification.

### I.5 Spin from Dual-Geometry

**Location in spec:** Section VII (Dual-Geometry Sectors), Section XIII (QM Derivation)

**What's missing:** The coverage audit marks spin as "C-PI" — covered by parallel isomorphism, with dual-geometry sectors providing the mechanism route. The specific mechanism is not stated. How does the dual-geometry structure produce half-integer spin for fermions and integer spin for bosons? What substrate feature distinguishes them?

**What's needed:** The explicit connection between the spherical/toroidal sector structure and spin. The toroidal sector is cyclic — it wraps. A full wrap versus a half wrap could distinguish integer from half-integer spin. The spec needs to commit to this or an alternative mechanism and show that it produces exactly the observed spin spectrum.

**Falsification:** The mechanism either produces spin-0, spin-1/2, spin-1, spin-3/2, and spin-2 with the correct statistics (Bose-Einstein for integer, Fermi-Dirac for half-integer) or it doesn't.

**Priority:** High. Spin-statistics is foundational to all of quantum mechanics and the Standard Model.

---

## II. Explicit CODATA Derivation Targets

These items have mechanisms in the spec but require explicit derivation work. Each is a specific CODATA value that the integer alphabet must produce.

### II.1 Electromagnetic Constants

| Constant | CODATA Symbol | Status | Derivation Path |
|---|---|---|---|
| Fine structure constant | α | Priority downstream | From hierarchy configuration via integer alphabet |
| Fine structure constant inverse | α⁻¹ ≈ 137.036 | Priority downstream | Must emerge as integer-alphabet expression |
| Elementary charge | e | Pending SI bridge | Channel unit throughput quantum |
| Vacuum permittivity | ε₀ | Pending SI bridge | Follows from α, e, ℏ, c |
| Vacuum permeability | μ₀ | Pending SI bridge | Follows from ε₀ and c |
| Impedance of free space | Z₀ | Follows from μ₀, ε₀ | Derived |
| Bohr magneton | μ_B | Follows from e, ℏ, m_e | Derived |
| Nuclear magneton | μ_N | Follows from e, ℏ, m_p | Derived |

**Key derivation:** α from the integer alphabet is the single most important electromagnetic derivation. Everything else cascades from it.

### II.2 Mass Constants

| Constant | CODATA Symbol | Status | Blocked On |
|---|---|---|---|
| Electron mass | m_e | Pending | Per-hierarchy-boundary modulus (I.1) |
| Muon mass | m_μ | Pending | Per-hierarchy-boundary modulus (I.1) |
| Tau mass | m_τ | Pending | Per-hierarchy-boundary modulus (I.1) |
| Proton mass | m_p | Pending | Per-hierarchy-boundary modulus (I.1) + toroidal content (99%) |
| Neutron mass | m_n | Pending | m_p + mass difference derivation |
| Up quark mass | m_u | Pending | Per-hierarchy-boundary modulus (I.1) |
| Down quark mass | m_d | Pending | Per-hierarchy-boundary modulus (I.1) |
| Strange quark mass | m_s | Pending | Per-hierarchy-boundary modulus (I.1) |
| Charm quark mass | m_c | Pending | Per-hierarchy-boundary modulus (I.1) |
| Bottom quark mass | m_b | Pending | Per-hierarchy-boundary modulus (I.1) |
| Top quark mass | m_t | Pending | Per-hierarchy-boundary modulus (I.1) |
| W boson mass | M_W | Pending | Per-hierarchy-boundary modulus (I.1) |
| Z boson mass | M_Z | Pending | Per-hierarchy-boundary modulus (I.1) |
| Higgs boson mass | M_H | Pending | Per-hierarchy-boundary modulus (I.1) |
| Proton-electron mass ratio | m_p/m_e | Pending | Ratio may be derivable before absolute masses |
| Muon-electron mass ratio | m_μ/m_e | Pending | 206.768... from hierarchy structure |
| Neutron-proton mass difference | m_n - m_p | Pending | Channel arithmetic |

**Note on mass ratios:** Dimensionless mass ratios may be derivable from the integer alphabet before the SI bridge is complete. Ratios don't require dimensional units. This could be a productive intermediate step — derive all mass ratios first, then anchor to SI through one absolute mass plus the SI bridge.

### II.3 Electroweak Constants

| Constant | CODATA Symbol | Status | Derivation Path |
|---|---|---|---|
| Weak mixing angle | sin²θ_W | Not listed in spec | Must emerge from channel type enumeration |
| Fermi coupling constant | G_F | Not listed in spec | Weak channel throughput at low energy |
| W boson width | Γ_W | Downstream | Weak channel decay arithmetic |
| Z boson width | Γ_Z | Downstream | Weak channel decay arithmetic |
| Higgs boson width | Γ_H | Downstream | Channel decay arithmetic |

**Gap:** sin²θ_W and G_F should be explicitly listed as derivation targets in Section XIV. They are core electroweak parameters that the spec's channel enumeration must produce.

### II.4 Strong Interaction Constants

| Constant | CODATA Symbol | Status | Derivation Path |
|---|---|---|---|
| Strong coupling constant | α_s(M_Z) | Not explicitly listed | Channel-coupling scaling at Z mass scale |
| QCD scale parameter | Λ_QCD | Downstream | From α_s running |
| Proton charge radius | r_p | Downstream | Toroidal content of proton channel structure |
| Proton magnetic moment | μ_p | Downstream | Toroidal sector at proton scale |
| Neutron magnetic moment | μ_n | Downstream | Toroidal sector at neutron scale |
| Pion mass | m_π | Downstream | Strong channel arithmetic |
| Pion decay constant | f_π | Downstream | Strong channel decay |

**Gap:** α_s(M_Z) should be an explicit high-priority derivation target. The proton charge radius is particularly important given the proton radius puzzle — the spec's toroidal content mechanism may resolve the muonic hydrogen discrepancy.

### II.5 Gravitational Constants

| Constant | CODATA Symbol | Status | Derivation Path |
|---|---|---|---|
| Gravitational constant | G | Not listed | Hierarchy-local drain channel throughput |
| Planck mass | m_P | Follows from G, ℏ, c | Derived once G is derived |
| Planck length | l_P | Follows from G, ℏ, c | = 1 cell in Earth hierarchy |
| Planck time | t_P | Follows from G, ℏ, c | = 1 tick in Earth hierarchy |
| Planck temperature | T_P | Follows from m_P, k_B | Derived |

**Gap:** G is conspicuously absent from the derivation target list. The spec's framework has a specific structural claim about G — it's hierarchy-local, not universal, which explains why terrestrial measurements don't converge. This claim should be made explicit, and the predicted value of G in the Earth hierarchy should be a derivation target with a falsification condition. If the framework can predict G more precisely than experiment has measured it, that is a strong novel prediction.

### II.6 Anomalous Magnetic Moments

| Constant | Status | Derivation Path |
|---|---|---|
| Electron g-2 (a_e) | High priority listed | Dual-geometry decomposition: spherical π terms + toroidal elliptic terms |
| Muon g-2 (a_μ) | High priority listed | Dual-geometry decomposition with 22 MeV crossover |
| Tau g-2 (a_τ) | Downstream | Same decomposition at tau scale |

**Note:** The muon g-2 has a current tension between the Brookhaven/Fermilab experimental average and the SM prediction (with lattice QCD and dispersive approaches disagreeing). The spec's dual-geometry decomposition claims a different mechanism that may produce a different prediction. This should be stated as an explicit novel-prediction opportunity in the spec.

### II.7 Mixing Matrix Elements

| Constant | Status | Derivation Path |
|---|---|---|
| CKM V_us | Claimed 9/40 | Integer channel ratio — needs derivation |
| CKM V_cb | Claimed 1/24 | Integer channel ratio — needs derivation |
| CKM V_ub | Not listed | Integer channel ratio |
| CKM V_td | Not listed | Integer channel ratio |
| CKM V_ts | Not listed | Integer channel ratio |
| CKM V_tb | Not listed | Integer channel ratio |
| CKM V_ud | Not listed | Follows from unitarity if V_us and V_ub are derived |
| CKM V_cs | Not listed | Follows from unitarity |
| CKM V_cd | Not listed | Follows from unitarity |
| Jarlskog invariant J | Not listed | CP violation magnitude from CKM |
| PMNS θ₁₂ | Listed as high priority | Neutrino mixing from weak channel arithmetic |
| PMNS θ₂₃ | Listed as high priority | Neutrino mixing |
| PMNS θ₁₃ | Listed as high priority | Neutrino mixing |
| PMNS δ_CP | Not listed | Neutrino CP phase |
| Neutrino mass differences | Not listed | Δm²₂₁ and Δm²₃₂ from channel arithmetic |

**Gap:** The full CKM matrix has nine elements (four independent parameters plus unitarity constraints). The spec claims two. All nine should be listed as derivation targets, with unitarity serving as an internal consistency check. The PMNS matrix similarly needs all parameters listed, including the CP-violating phase δ_CP and the two Majorana phases if neutrinos are Majorana.

**Gap:** Neutrino mass squared differences are among the most precisely measured neutrino parameters and should be explicit derivation targets. Whether neutrinos are Dirac or Majorana is a commitment the spec should make.

### II.8 Cosmological Parameters

| Constant | Status | Derivation Path |
|---|---|---|
| Ω_b | Derived: 13/264 | Complete — BBN experiment confirms |
| Ω_DM | Derived: π/12 | Complete |
| Ω_Λ | Derived: (251-22π)/264 | Complete |
| H₀ | Partially derived: 12/11 ratio | Absolute value needs derivation |
| DM/baryon ratio | Derived: 22π/13 | Complete |
| σ₈ (matter fluctuation amplitude) | Not listed | Downstream from structure formation |
| n_s (scalar spectral index) | Not listed | Early-universe channel dynamics |
| τ (optical depth to reionization) | Not listed | Downstream |
| Σm_ν (neutrino mass sum) | Not listed | Follows from neutrino mass derivation |
| r (tensor-to-scalar ratio) | Not listed | Primordial GW amplitude |
| Age of the universe | Not listed | Follows from H₀ and expansion history |
| CMB temperature T₀ | Not listed | Should be derivable from substrate |
| Baryon-to-photon ratio η | Derived | BBN experiment confirms |
| Primordial He-4 abundance Y_p | Derived | BBN experiment, 1.5% miss |
| Primordial D/H | Derived | BBN experiment, 0.14% miss |
| N_eff (effective neutrino number) | Derived: 2.71 | 10.9% miss vs standard 3.044 — tension to resolve |

**Gap:** The absolute value of H₀ (not just the ratio between measurement methods) should be a derivation target. The CMB temperature today (2.7255 K) should be derivable from the substrate's early-universe dynamics plus expansion. The scalar spectral index n_s is a high-precision CMB measurement that the framework should predict.

**Tension:** N_eff derived as 2.71 versus standard 3.044 is a 10.9% miss. This is either a genuine prediction (fewer effective neutrino species than standard assumption) or a derivation error. The spec should commit: is 2.71 the prediction, or is this a known issue in the current derivation? If it's the prediction, it's a falsifiable novel claim. If it's a known issue, the resolution path should be stated.

### II.9 Nuclear and Hadronic Constants

| Constant | Status | Derivation Path |
|---|---|---|
| Deuteron mass | Not listed | Nuclear channel arithmetic |
| Deuteron binding energy | Not listed | Strong residual channel |
| Triton mass | Not listed | Nuclear channel arithmetic |
| Helion mass | Not listed | Nuclear channel arithmetic |
| Alpha particle mass | Not listed | Nuclear channel arithmetic |
| Nuclear magnetic moments | Not listed | Toroidal sector content |
| Deuteron magnetic moment | Not listed | Toroidal sector |
| Nuclear charge radii | Not listed | Channel structure |
| Semi-empirical mass formula coefficients | Not listed | Strong channel averaging |
| Magic numbers (2, 8, 20, 28, 50, 82, 126) | Not listed | Channel closure at nuclear scale |

**Gap:** Nuclear structure is a significant body of precision data that the spec doesn't explicitly target. The magic numbers are particularly interesting — they're integers, and the framework's integer alphabet should either produce them or explain them from channel closure structure. This is a natural fit for the framework and should be listed.

### II.10 Precision QED Tests

| Constant | Status | Derivation Path |
|---|---|---|
| Lamb shift (hydrogen 2S-2P) | C-PI in coverage audit | Toroidal QED contribution |
| Hydrogen 1S-2S transition frequency | Not listed | Atomic scale derivation |
| Hydrogen hyperfine splitting | Not listed | Toroidal magnetic interaction |
| Positronium ground state hyperfine | Not listed | Pure QED system |
| Muonium hyperfine splitting | Not listed | QED + muon mass |
| Rydberg constant R_∞ | Not listed | Follows from α, m_e, c, ℏ |
| Bohr radius a₀ | Not listed | Follows from α, m_e, ℏ |
| Classical electron radius r_e | Not listed | Follows from α, m_e, c, ℏ |
| Electron Compton wavelength | Not listed | Follows from m_e, ℏ, c |
| Thomson cross section | Not listed | Follows from r_e |

**Note:** Many of these are derived quantities — they follow algebraically from α, particle masses, ℏ, and c. Once those fundamentals are derived, these cascade automatically. But the hydrogen 1S-2S transition frequency is measured to 15 significant figures. It is the most precisely measured quantity in physics. The framework should explicitly target it as the ultimate precision test.

---

## III. Mechanism Clarifications Needed

These items have mechanisms in the spec that need sharpening to produce specific predictions.

### III.1 Neutrino Mass Structure

**What's missing:** The spec covers neutrino oscillation via weak-channel arithmetic but does not commit to: whether neutrinos are Dirac or Majorana particles, absolute neutrino masses (not just differences), the mass ordering (normal or inverted hierarchy), and whether a sterile neutrino exists.

**What's needed:** Explicit commitments on each. The channel structure should force one option per question. If the substrate produces Dirac neutrinos, say so. If it forces normal ordering, say so. These are falsifiable predictions.

### III.2 Strong CP and θ Parameter

**What's missing:** We discussed this — θ = 0 because the vacuum is the ground state. The spec should state this explicitly as a commitment and derive θ = 0 from the substrate, not just assert it. The mechanism — ground state has no CP-violating phase in the strong sector — needs to be made rigorous enough that it's falsifiable. Specifically: does the substrate predict no axion? If θ = 0 is structural, the axion doesn't exist. That's a prediction.

**What's needed:** Explicit statement: θ = 0 from substrate ground state structure. Explicit consequence: no axion. Falsification: if an axion is detected, this commitment fails.

### III.3 Proton Lifetime

**What's missing:** The Standard Model predicts proton stability. Grand unified theories predict proton decay with lifetimes around 10³⁴-10³⁶ years. Super-Kamiokande has measured no decay, with limits above 10³⁴ years. The spec should commit: does the substrate predict absolute proton stability or eventual decay? The soliton framework — proton as a self-sustaining pattern extracting from the quiver — needs to answer whether the pattern is eternally stable or has a finite lifetime.

**What's needed:** Explicit commitment on proton stability. If stable, this is consistent with current observations and diverges from GUT predictions. If unstable, a lifetime prediction.

### III.4 Baryon Asymmetry Mechanism

**What's missing:** Listed as "downstream" in the coverage audit. The spec covers antimatter and CP violation but doesn't specify the mechanism that produced the observed matter-antimatter asymmetry in the early universe. The Sakharov conditions (baryon number violation, C and CP violation, departure from thermal equilibrium) need substrate equivalents.

**What's needed:** The specific channel dynamics in the early universe that produced the asymmetry. This connects to the CPT/antimatter coverage and the early-universe dynamics in Section XV.

### III.5 Vacuum Energy and the Cosmological Constant Problem

**What's missing:** The BBN experiment output shows `result_cc_problem_ratio_v0: 3.94e+54`. The standard cosmological constant problem is a mismatch of ~10¹²². The spec's ratio is ~10⁵⁴, which is a different number. The spec should explicitly address: does the framework dissolve the cosmological constant problem entirely (the 10¹²² was a type error between incompatible formalisms, as we discussed), and what does the 10⁵⁴ ratio represent in the framework?

**What's needed:** Explicit statement on the cosmological constant problem's status in PCTRM. If dissolved (as the type-error argument suggests), state this as a commitment. The 10⁵⁴ ratio needs interpretation.

---

## IV. Novel Predictions the Spec Should Register

Items where the framework produces predictions that differ from the Standard Model or current consensus. These are the highest-value items for the program because they're independently testable.

### IV.1 Predictions That Differ from SM

| Prediction | PCTRM Value | SM/Consensus Value | Testable By |
|---|---|---|---|
| N_eff | 2.71 (current derivation) | 3.044 | CMB Stage-4 experiments |
| θ (strong CP) | Exactly 0, structurally | 0 observed, mechanism unknown | Axion searches (null result predicted) |
| Proton stability | Commit needed | SM: stable; GUTs: ~10³⁴ yr | Hyper-Kamiokande |
| H₀ tension | 12/11 structural ratio | Unknown resolution | Future precision measurements |
| Muon g-2 | Dual-geometry prediction (pending) | SM: tension with experiment | Comparison to Fermilab/J-PARC |
| G variability | Hierarchy-local, not universal | Universal constant | Precision G measurements at L1/L2 |
| Dark matter | Not particles | Particles (WIMPs, axions, etc.) | Direct detection experiments (null predicted) |
| Neutrino nature | Commit needed | Unknown | Neutrinoless double beta decay |

**Gap:** Each of these should be stated as a pre-registered prediction in the spec with explicit falsification conditions. The dark matter prediction is particularly strong — if PCTRM says dark matter is toroidal-flow Higgs response and not particles, then every direct detection experiment should return null. That's a clean, falsifiable, ongoing prediction.

### IV.2 Precision Predictions Where Framework May Exceed SM

| Quantity | Why PCTRM Might Do Better | Status |
|---|---|---|
| G | Framework explains measurement scatter; may predict value more precisely than experiments agree | Pending derivation |
| Proton radius | Dual-geometry may resolve muonic hydrogen puzzle | Pending derivation |
| Lithium-7 abundance | BBN derivation reproduces standard tension — may identify resolution path | Tension confirmed, resolution pending |
| Y_p (primordial helium) | 1.5% miss in current derivation — may improve with refined BBN chain | Derivation refinement |

---

## V. Structural Completeness Checklist

For the spec to be complete against all confirmed observations, every item below must be either derived, committed with a derivation path, or explicitly placed out of scope.

### V.1 Fundamental Constants (22 items)

- [ ] Fine structure constant α
- [ ] Strong coupling constant α_s(M_Z)
- [ ] Weak mixing angle sin²θ_W
- [ ] Fermi coupling constant G_F
- [ ] Gravitational constant G
- [ ] Electron mass m_e
- [ ] Muon mass m_μ
- [ ] Tau mass m_τ
- [ ] Up quark mass m_u
- [ ] Down quark mass m_d
- [ ] Strange quark mass m_s
- [ ] Charm quark mass m_c
- [ ] Bottom quark mass m_b
- [ ] Top quark mass m_t
- [ ] W boson mass M_W
- [ ] Z boson mass M_Z
- [ ] Higgs boson mass M_H
- [ ] CKM matrix (4 independent parameters)
- [ ] PMNS matrix (6 independent parameters)
- [ ] Neutrino mass squared differences (2)
- [ ] Strong CP parameter θ
- [ ] Cosmological constant Λ

### V.2 Cosmological Parameters (12 items)

- [x] Ω_b (derived: 13/264)
- [x] Ω_DM (derived: π/12)
- [x] Ω_Λ (derived: (251-22π)/264)
- [x] DM/baryon ratio (derived: 22π/13)
- [x] Baryon-to-photon ratio η (derived)
- [ ] H₀ absolute value
- [ ] CMB temperature T₀
- [ ] Scalar spectral index n_s
- [ ] Tensor-to-scalar ratio r
- [ ] Optical depth τ
- [ ] Age of the universe
- [x] N_eff (derived: 2.71 — tension with 3.044 to resolve or commit)

### V.3 Precision QED (6 items)

- [ ] Electron anomalous magnetic moment a_e
- [ ] Muon anomalous magnetic moment a_μ
- [ ] Hydrogen 1S-2S transition frequency
- [ ] Hydrogen ground state hyperfine splitting
- [ ] Lamb shift
- [ ] Rydberg constant R_∞

### V.4 Nuclear and Hadronic (8 items)

- [ ] Proton charge radius r_p
- [ ] Proton magnetic moment μ_p
- [ ] Neutron magnetic moment μ_n
- [ ] Deuteron binding energy
- [ ] Nuclear magic numbers
- [ ] Pion mass m_π
- [ ] Pion decay constant f_π
- [ ] Neutron lifetime τ_n

### V.5 BBN Abundances (5 items)

- [x] Primordial deuterium D/H (derived: 0.14% miss)
- [x] Primordial helium-4 Y_p (derived: 1.5% miss)
- [ ] Primordial helium-3
- [x] Primordial lithium-7 (tension reproduced)
- [ ] Primordial lithium-6

### V.6 Structural Commitments (6 items)

- [ ] Per-hierarchy-boundary moduli (Section I.1 above)
- [ ] Natural-to-SI bridge (Section I.2 above)
- [ ] Charge quantization mechanism (Section I.3 above)
- [ ] Color charge / SU(3) derivation (Section I.4 above)
- [ ] Spin from dual-geometry (Section I.5 above)
- [ ] Neutrino Dirac/Majorana commitment (Section III.1 above)

### V.7 Novel Predictions to Pre-Register (8 items)

- [ ] No axion (from θ = 0 structurally)
- [ ] No dark matter particles (from toroidal-flow mechanism)
- [ ] G hierarchy-local prediction
- [ ] N_eff commitment (2.71 or revised)
- [ ] Proton stability commitment
- [ ] Neutrino mass ordering commitment
- [ ] Muon g-2 dual-geometry prediction
- [ ] Proton radius dual-geometry prediction

---

## VI. Derivation Priority Ordering

Ordered by what unblocks the most downstream work.

**Phase 1 — Unblock the mass sector:**
1. Per-hierarchy-boundary moduli specification
2. Electron mass from integer alphabet
3. All mass ratios from hierarchy structure
4. Koide K = 2/3 explicit derivation

**Phase 2 — Unblock electroweak:**
5. Fine structure constant α from integer alphabet
6. Weak mixing angle sin²θ_W from channel enumeration
7. Fermi coupling constant G_F
8. W, Z, Higgs masses from moduli

**Phase 3 — Unblock strong sector:**
9. Strong coupling α_s(M_Z)
10. Pion mass and decay constant
11. Proton charge radius
12. Nuclear magnetic moments

**Phase 4 — Complete mixing matrices:**
13. Full CKM matrix (all nine elements)
14. Full PMNS matrix (all parameters)
15. Neutrino mass squared differences
16. CP violation magnitudes

**Phase 5 — Precision QED:**
17. Electron g-2 dual-geometry derivation
18. Muon g-2 dual-geometry derivation
19. Lamb shift
20. Hydrogen 1S-2S

**Phase 6 — Gravitational sector:**
21. G from hierarchy configuration
22. H₀ absolute value
23. Age of the universe

**Phase 7 — Cosmological precision:**
24. CMB temperature
25. Scalar spectral index
26. Complete BBN chain (He-3, Li-6)

**Phase 8 — Novel predictions:**
27. Pre-register all items from Section IV
28. Identify additional novel predictions from completed derivations
29. Design experimental tests for strongest novel predictions

**Phase 9 — SI bridge and publication:**
30. Complete natural-to-SI dimensional bridge
31. Generate full CODATA comparison table
32. Document every derivation in reproducible Python with integer-alphabet-only inputs

---

## VII. Completion Criterion

The spec is complete against all confirmed observations when:

Every item in Section V checklists is either checked (derived with integer-alphabet-only Python code matching CODATA to measurement precision) or explicitly committed with a stated falsification condition.

Every structural commitment in Section I is specified with explicit values.

Every novel prediction in Section IV is pre-registered with explicit falsification conditions.

The SI bridge produces consistent dimensional values across all derived quantities.

The full CODATA table can be generated from a single execution of the derivation chain starting from the integer alphabet, with no external inputs.

At that point, the infrastructure layer of physics is closed. The ongoing layer — new experiments, new materials, new engineering applications — runs on top of the closed substrate, the same way applications run on the software binary and runners run on the OpsDB schema.

---

**End of Completion Document.**