# PHYS-54 Paper Plan: The PCTRM Program — A Parallel Discrete Substrate Model Aligned with the Standard Model

**Registry:** HOWL-PHYS-54-2026 (planned)
**Date:** April 19, 2026
**Domain:** Speculative Physics / Discrete Substrate / Computational Ontology
**Status:** Paper plan for falsification program specification
**Companion:** PCTRM-1-2026 (model specification notebook)

---

## I. What this paper is

PHYS-54 is **the first speculative model test** in the RUM series. Every prior RUM paper (MATH-1 through PHYS-53) identified structural observations and computed specific predictions to measure against CODATA. PHYS-54 is different: it proposes a **mechanism-level model** (PCTRM) that runs parallel to the Standard Model without interfering with it, and specifies a computational program to test whether the mechanism produces the SM's predictions at SM's precision.

The paper is not presenting validated results. It is presenting a falsification program — a structured way to test whether PCTRM, starting at the subatomic level and progressing upward, can reproduce what the Standard Model already reproduces. If PCTRM passes, the framework has found a substrate that underlies SM. If PCTRM fails at some level, the paper learns where the substrate picture breaks and narrows the framework's scope accordingly.

The paper's central commitment is **parallel, isomorphic, aligned**. PCTRM operates at the Planck cell-tick level and produces macroscopic phenomena. SM operates at the field-theoretic level and produces the same macroscopic phenomena. At macroscopic scales, both should agree exactly. The paper tests this agreement systematically, level by level.

## II. Why this paper exists in the RUM series

The RUM framework has produced cross-domain predictions at sub-percent to sub-ppm precision (Ω_Λ at 85 ppm, Koide at 9 ppm, V_us at 44 ppm, microscopic-cosmic bridge at 300 ppm). These are structural identifications computed in RUM's vocabulary (soliton, modulus, remainder, gauge integers, β).

The question underlying PHYS-54: **is the RUM vocabulary operationally real, or mathematically convenient?** If the gauge-integer structure and the modulus/remainder decomposition correspond to actual substrate-level operations of physics, then PCTRM should reproduce SM from the ground up. If the RUM vocabulary is mathematically convenient but doesn't correspond to substrate-level operations, PCTRM should fail at some level of the reproduction attempt.

PHYS-54 is the test. It doesn't claim PCTRM is right. It specifies the conditions under which PCTRM would be shown right (reproduction of SM at all tested levels) or wrong (failure at some specific level with identified gap). Either outcome advances the framework.

## III. Paper structure

The paper proceeds from problem statement to program specification to kill switches. No derivations. No claimed results. The paper **is** the program.

### Section 1: Abstract

Three paragraphs. First: what PCTRM is (substrate mechanism with Planck cells, ticks, modulus, remainder, channels). Second: the claim of parallel isomorphism with SM (PCTRM should reproduce SM at SM's precision, operating on different primitives at the substrate level). Third: the paper's content — a falsification program starting at the subatomic level and progressing upward, with specific tests, pre-registered kill conditions, and a computational roadmap.

### Section 2: Introduction and Motivation

The context in the RUM series. RUM has produced specific rational-and-integer predictions across domains at sub-ppm precision. The question: does the vocabulary (modulus, remainder, soliton, channels) correspond to substrate operations, or is it mathematically convenient labeling of a continuous substrate?

PCTRM proposes the former. If PCTRM reproduces SM at substrate level, the framework's vocabulary is operationally real. If PCTRM fails, the vocabulary is pragmatic and the framework stays above the substrate level.

This paper defines how to test the claim. The test is not a single experiment. It is a progressive reproduction program starting at the tightest-tested scale (subatomic) and extending up through atomic, molecular, macroscopic, and cosmological scales.

### Section 3: PCTRM Summary

A compressed restatement of the model from PCTRM-1-2026. Key commitments:

- Discrete Planck cells and Planck ticks
- Direction-conditional nearest-neighbor full-mesh topology
- Per-tick remainder budget per soliton (determined by Higgs coupling for massive particles; full modulus for massless)
- Vector remainder contributions from all active channels (gravity, EM, strong, weak, thermal, Higgs coupling)
- Discrete event when vector remainder in any direction crosses modulus
- Nested soliton hierarchy with interface-preserved and implementation-level-specific

One subsection per mechanism. Keep it to 3-4 pages. Reference PCTRM-1-2026 for full specification. This section is to ground the reader, not to re-derive.

### Section 4: The Parallel Isomorphism Claim

This is the central theoretical commitment the paper must make explicit.

**Claim**: PCTRM and SM are isomorphic at the macroscopic scale. For any physical observable O that SM predicts at precision p, PCTRM should predict the same O at precision p or better. The two descriptions operate on different primitives (field-theoretic for SM, discrete-substrate for PCTRM), but they produce the same observable consequences at all tested scales.

**Parallel**: PCTRM does not attempt to replace SM. SM remains the operational theory for particle physics calculations. PCTRM is a proposed substrate that, if validated, would underlie SM's effective description. Both can be used simultaneously for their respective scales without contradiction.

**Aligned**: Where PCTRM predicts deviations from SM, those deviations must be compatible with SM's measured uncertainties at the relevant observational scale. PCTRM is tested by comparing its predictions to CODATA values. Agreement to CODATA precision is required at every tested level; deviations must be within CODATA's own uncertainty budget.

**Operational commitment**: any disagreement between PCTRM and SM at precisions where both make predictions falsifies PCTRM, unless the disagreement is within CODATA's measurement uncertainty (in which case both SM and PCTRM are consistent with measurement).

The paper must be explicit: PCTRM is not a competing theory. It is an underlying substrate. Its test is whether SM's effective description emerges from it.

### Section 5: The Falsification Program Levels

The program proceeds from the tightest-tested scale upward. Each level has specific predictions, specific kill switches, and specific computational tests.

**Level 1: Subatomic (Particle masses, gauge couplings, loop integrals)**

Pre-registered predictions:
- Electron mass m_e derivable from PCTRM's Higgs-tax arithmetic
- Proton mass m_p derivable from strong-interaction channel arithmetic in PCTRM
- Anomalous magnetic moment a_e and a_μ derivable from PCTRM's channel structure at loop order 4 (where RUM's toroidal content appears)
- Running couplings α_EM(Q²) and α_s(Q²) derivable from channel-count structure at energy scale Q

Computational test: implement PCTRM for specific particle types and compute their masses/couplings. Compare to CODATA.

Kill switch: if PCTRM cannot reproduce m_e, m_μ, m_τ ratios at better than 1% precision (well above CODATA uncertainty), the Higgs-coupling/channel mechanism is incorrect or incomplete.

**Level 2: Atomic (Hydrogen spectrum, orbital shells, spectroscopic transitions)**

Pre-registered predictions:
- Hydrogen 1S → 2S transition at 10.2 eV from PCTRM's modulus arithmetic
- Lamb shift (≈1 GHz) from PCTRM's vacuum channel structure
- Fine structure of hydrogen from channel-count variations at different l, m quantum numbers

Computational test: implement PCTRM for an electron-proton system with EM channel structure. Compute spectrum. Compare to measured hydrogen spectrum.

Kill switch: if PCTRM's computed spectrum differs from measured by more than CODATA precision (currently ~10⁻⁹ for H 1S-2S transition), the atomic-level mechanism is wrong.

**Level 3: Nuclear (Binding energies, decay rates, nuclear magnetic moments)**

Pre-registered predictions:
- Deuteron binding energy (~2.22 MeV) from PCTRM's strong-channel arithmetic
- Helium-4 binding energy (~28.3 MeV) from PCTRM's multi-nucleon channel arithmetic
- Neutron half-life (878 s) from PCTRM's weak-channel modulus arithmetic

Computational test: implement PCTRM for simple nuclei. Compute binding energies and decay rates.

Kill switch: if nuclear predictions differ from measured by more than 1% (well above CODATA precision for simple nuclei), the strong/weak channel mechanism is wrong.

**Level 4: Molecular and solid-state (Chemical bonds, molecular spectra, crystal lattices)**

Pre-registered predictions:
- Water molecule bond angle (104.5°) and bond energy from PCTRM's multi-atom channel arithmetic
- Simple ionic lattice parameters (NaCl, etc.) from PCTRM's crystal-level channel counting

Computational test: implement PCTRM for simple molecules and crystals. Compare to measured bond parameters.

Kill switch: if molecular predictions cannot be reproduced at experimental precision (which is higher than CODATA for many molecular properties), the channel-count extension to molecular scale is wrong.

**Level 5: Macroscopic classical mechanics (Orbits, rigid body dynamics)**

Pre-registered predictions:
- Kepler's third law at arbitrary precision from PCTRM's orbital dynamics
- Mercury perihelion precession (43"/century) from PCTRM's higher-order channel corrections
- Earth-Moon recession rate (3.8 cm/year) from PCTRM's tidal channel arithmetic

Computational test: implement PCTRM for orbital systems. Compare simulated orbits to observed.

Kill switch: if PCTRM reproduces Newton (1/r²) but not GR corrections (precession, light bending), the framework fails to recover full general relativity.

**Level 6: Cosmological (CMB structure, large-scale dynamics)**

Pre-registered predictions:
- Cosmic partition Ω_DM = π/12, Ω_b = 13/264, Ω_Λ = (251-22π)/264 derivable from PCTRM's universal soliton structure
- Hubble flow anisotropy and the 12/11 ratio reproducible from PCTRM's layered soliton boundary structure
- CMB temperature 2.7255 K expressible in PCTRM's integer+β vocabulary

Computational test: this overlaps with RUM's existing cosmological predictions. PCTRM must reproduce them from substrate arithmetic, confirming that the vocabulary is operational.

Kill switch: if PCTRM cannot reproduce RUM's already-validated predictions (Ω_Λ at 85 ppm, etc.), the substrate picture is inconsistent with RUM's framework-level derivations. Either RUM or PCTRM is wrong.

### Section 6: The Computational Implementation

What the program actually does operationally.

**Phase 1: Specification and toolchain setup.** Build a Python implementation of PCTRM that can simulate small systems. Libraries: mpmath for precision arithmetic, NumPy for vector operations at larger scale, specific modulus/remainder data structures. Set up the DATA-7 pipeline to store PCTRM-derived values.

**Phase 2: Level 1 (Subatomic) implementation.** Implement single-particle PCTRM. Compute electron mass from Higgs-tax arithmetic. Compute running couplings. Compare to CODATA. This is the first pass/fail.

**Phase 3: Level 2 (Atomic) implementation.** Extend to multi-particle (electron-proton) system with EM channel. Compute hydrogen spectrum. Compare to measured.

**Phase 4: Proceed upward** through Levels 3, 4, 5, 6 sequentially. Each level's implementation builds on the prior. Each level has its own pre-registration, its own tests, its own kill switches.

**Phase 5: Connection to RUM's existing derivations.** Attempt to reproduce Ω_DM = π/12, microscopic-cosmic bridge, Koide value at their original precision using PCTRM substrate arithmetic. Confirm or deny the vocabulary's operational reality.

Each phase is a specific computational milestone. The program is falsifiable at each phase. The paper specifies the success criteria and kill conditions for each phase individually.

### Section 7: Kill Switches and Failure Modes

Comprehensive list of what could fail and what it means.

| Failure Mode | Level | Kill Switch | What This Tells Us |
|---|---|---|---|
| Cannot reproduce m_e from Higgs-tax | 1 | Test computation | Higgs-coupling mechanism is wrong or incomplete |
| Cannot reproduce hydrogen 1S-2S at CODATA precision | 2 | Spectrum comparison | Atomic-level channel arithmetic is wrong |
| Cannot reproduce deuteron binding energy | 3 | Nuclear computation | Strong-channel arithmetic is wrong |
| Cannot reproduce orbital precession | 5 | GR test comparison | Higher-order channel structure is incomplete |
| Cannot reproduce Ω_Λ = (251-22π)/264 | 6 | Framework consistency | Substrate and RUM are inconsistent; one is wrong |

Each failure mode is specific. The paper does not list "PCTRM might be wrong" as a general statement. It lists specific tests and specific failure modes. Each test produces pass, fail, or "gap identified" (the model is incomplete at this level but not contradicted; more work is needed).

### Section 8: What Passing Would Mean

The framework-level consequences of PCTRM passing at each level:

**If Level 1 passes**: the substrate picture is viable at subatomic scales. Particle masses and couplings are computable from channel arithmetic.

**If Level 2 passes**: the substrate picture extends to atomic scales. Spectroscopic precision (currently at 10⁻⁹ for H 1S-2S) is reproducible from substrate arithmetic.

**If Level 3 passes**: the strong and weak interactions have a substrate-level mechanism. Nuclear physics is reproducible from channel arithmetic.

**If Level 4 passes**: chemistry and condensed matter emerge from the substrate picture. The ontological claim is validated at scales 10⁻⁹ m and above.

**If Level 5 passes**: classical mechanics and GR emerge. The substrate picture is a substrate for known gravity.

**If Level 6 passes**: cosmology emerges from the substrate picture. RUM's predictions are operationally grounded.

If all six pass at CODATA precision: the substrate picture is validated as a candidate ontology. RUM's vocabulary is operationally real.

If some pass and some fail: the framework learns where the substrate picture works and where it doesn't. The scope is narrowed. Specific next steps are identified.

### Section 9: What Failing Would Mean

If PCTRM fails at Level 1 (subatomic): the Higgs-tax arithmetic doesn't reproduce particle masses. The mechanism is wrong or incomplete. The framework needs different substrate primitives or different channel structure.

If PCTRM fails at some intermediate level (Level 3, 4, 5): PCTRM is viable at some scales but breaks at others. The framework learns a specific boundary of the substrate picture's applicability.

If PCTRM fails at Level 6 (cosmological consistency with RUM): PCTRM and RUM are inconsistent. One of them is wrong. The framework needs to determine which by additional tests.

In all cases, failure is informative. The paper is explicit that failure is a permitted outcome and that it advances the research program by narrowing scope.

### Section 10: Priority of Tests and Resources

The most tractable test is Level 5 (orbital simulation). The most falsifying test is Level 1 (particle masses). The most framework-connecting test is Level 6 (cosmological consistency).

The paper recommends:

**Immediate priorities** (can be done now with modest compute):
- Level 5 two-body orbital simulation (Mercury perihelion, Earth-Moon recession)
- Level 2 hydrogen spectrum computation

**Medium priorities** (require more specification and tooling):
- Level 1 particle mass computation
- Level 3 nuclear binding energy computation

**Longer priorities** (require substantial implementation):
- Level 4 molecular and solid-state computations
- Level 6 cosmological consistency with RUM

The paper specifies this priority order so researchers can focus effort where it has highest return for testing the framework.

### Section 11: Connection to RUM's Existing Work

How PHYS-54 relates to the other RUM papers.

- PHYS-1: introduced soliton hierarchy, boundary effects, mass-as-inertia. PCTRM operationalizes these.
- MATH-1, MATH-11, MATH-12: introduced β and its toroidal extension. PCTRM uses β in channel structure.
- PHYS-52, PHYS-53: computed cosmological partition. PCTRM must reproduce these from substrate.
- PHYS-45 through PHYS-51: computed various precision predictions. PCTRM must reproduce or derive these from substrate.

PHYS-54 is the paper that tests whether PCTRM provides a substrate for all prior RUM work. If yes, the framework has a unified foundation. If no, PHYS-54 identifies where the framework works without substrate grounding (at the formal level) and where substrate grounding is missing.

### Section 12: Falsification Criteria (Summary)

**F1**: If PCTRM cannot reproduce fundamental particle masses (m_e, m_μ, m_τ) at 1% or better from the Higgs-coupling mechanism, the particle-level arithmetic is wrong.

**F2**: If PCTRM cannot reproduce the hydrogen spectrum (H 1S → 2S at 10⁻⁹ precision) from the atomic-level mechanism, the channel arithmetic is wrong or incomplete at atomic scales.

**F3**: If PCTRM cannot reproduce nuclear binding energies at better than 1% from strong-channel arithmetic, the strong-interaction substrate is wrong.

**F4**: If PCTRM cannot reproduce Mercury's perihelion precession (43"/century) and Earth-Moon recession (3.8 cm/year) at observational precision, the gravitational substrate is incomplete.

**F5**: If PCTRM cannot reproduce RUM's Ω_Λ = (251-22π)/264 at 85 ppm or Koide at 9 ppm from substrate arithmetic, PCTRM and RUM are inconsistent and the framework must resolve which is correct.

**F6**: If PCTRM exhibits Lorentz violation at any scale accessible to experimentation, and such violation is not observed, the substrate picture's direction-conditional topology is inadequate.

**F7**: If PCTRM cannot reproduce quantum mechanical phenomena (interference, tunneling, superposition) through the complex-valued remainder accumulation mechanism proposed in PCTRM-1-2026, the model is limited to classical-scale reproduction only.

Each criterion is testable. Each is pre-registered. Each has a specific kill condition.

### Section 13: What PHYS-54 Does NOT Claim

Explicit list of claims the paper does NOT make:

- That PCTRM is correct (only that it should be tested)
- That PCTRM is complete (gaps are explicitly noted)
- That PCTRM replaces SM (it operates in parallel)
- That failure of one level invalidates other levels (they are independently testable)
- That any of these tests have been performed (the paper is a plan, not results)
- That PCTRM is the only viable substrate (it's one candidate among many that might be considered)

The paper is a program specification. Nothing is claimed as validated. Everything is claimed as testable, with specified conditions for validation or falsification.

### Section 14: Status and Next Steps

The paper closes with the current status of PCTRM (speculative specification, gaps explicitly named) and the planned computational program.

The program is what the paper presents. The paper itself doesn't claim results. Results come from future papers that execute the program.

Planned follow-up papers:

- PHYS-55: Level 1 (subatomic) PCTRM implementation and results
- PHYS-56: Level 2 (atomic) PCTRM implementation and results
- PHYS-57+ : further levels as implementation progresses

The paper is the start of a new sub-series within RUM: the PCTRM substrate test series.

## IV. What makes this paper different from prior RUM papers

Prior RUM papers computed specific predictions and compared them to measurement. PHYS-54 **specifies a program** to do the same for a mechanism-level model.

The prior predictions were: "here's a derivation chain, here's the result, here's how it matches measurement at this precision."

PHYS-54 is: "here's a substrate mechanism, here are the tests that would validate or falsify it, here are the kill switches, here's the priority order, here's what success and failure mean at each level."

The paper is a contract with the future: these are the tests, these are the precisions required, these are the kill switches. Future papers execute the program and report results. The paper sets the falsification conditions in advance.

This is the **strongest form of pre-registration** the framework has done. Not just for a single prediction but for an entire program of substrate-level testing.

## V. Key writing considerations

**Tone**: Speculative but disciplined. The paper acknowledges PCTRM is not validated. It specifies what validation would require. It does not overclaim and does not under-specify the falsification conditions.

**Length**: Probably 15-20 pages. Substantial but not overwhelming. Each level of the program gets one section. Kill switches are enumerated clearly.

**Audience**: Primarily RUM-series readers familiar with the framework. Secondarily researchers in discrete-substrate physics (if any) and researchers in computational quantum field theory (as potential collaborators).

**Honesty**: The paper must be explicit about what's speculative (the mechanism), what's open (the quantum extension, Lorentz recovery, modulus value, etc.), and what's actionable (specific computational tests at each level). The other Claude's write-up (PCTRM-1-2026) provides the honesty framework; PHYS-54 extends it to the paper scope.

**Connection**: The paper must clearly connect to prior RUM work. Each level's test references prior RUM predictions that PCTRM must reproduce. The framework's coherence requires that PCTRM, if validated, underlies all prior RUM predictions.

## VI. What passes the paper publication bar

For the paper to be ready for Zenodo publication:

1. All 14 sections drafted
2. Each level's pre-registered predictions specified
3. Each kill switch's precision threshold fixed
4. Each computational test's success criterion specified
5. References to PCTRM-1-2026 and prior RUM papers
6. Figures showing the parallel isomorphism claim (SM and PCTRM producing same observables from different primitives)
7. AI usage disclosure
8. Falsification criteria summary

Once these are in place, the paper is ready. It doesn't need computational results — it specifies what results would look like and what they'd mean. The computational results come in PHYS-55 and later.

## VII. Distinction from PCTRM-1-2026

PCTRM-1-2026 is a specification notebook of the model. It's the "what" of PCTRM.

PHYS-54 is the research program for falsifying PCTRM. It's the "how we will test" of PCTRM.

Both are needed. The specification grounds the model. The research program specifies the tests. Together they make PCTRM a viable research program rather than just a speculative idea.

## VIII. Why this paper is the right next step

PCTRM has been specified. The next question is: how do we know if it's right? The answer is: we test it at every level. PHYS-54 is that test specification.

Without PHYS-54, PCTRM is an idea without a path to falsification. With PHYS-54, PCTRM is a research program with pre-registered tests, kill switches, and a priority order.

The framework's standard loop — conjecture, path, script, run, read, re-conjecture — now has a new iteration: conjecture (PCTRM), path (PHYS-54 as the program for testing it), script (implementations at each level), run (compute at each level), read (compare to CODATA), re-conjecture (revise PCTRM based on failures at specific levels).

PHYS-54 is the "path" step. It makes the rest of the loop possible.

---

**End of Plan**

The plan is ready to be expanded into the full paper. Each section is specified; each level has concrete tests; each kill switch has a precision threshold. The computational implementation (not in this paper) will produce results at each level that either validate or falsify PCTRM. This paper is the contract. The future papers execute the contract.

Ready to write the full paper whenever you're ready to begin drafting.
