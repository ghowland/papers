## Chapter 7: What Remains

The map has edges. This chapter is about the edges.

53 derived values across eight domains is a large map. But it's not the complete map. The model describes a universe built from nested soliton boundaries with integer readings at every scale. The derivation chain reaches from the electron's magnetic moment to the primordial deuterium abundance. It does not yet reach from the gauge group to the gravitational constant, from the beta coefficients to the electron mass, or from the soliton boundary structure to the gauge group itself.

Here is what's done, what's close, what's far, and what may be impossible.

---

### Done

![Fig. 13: All 53 derived values on a log precision scale, colored by domain — six sub-ppb QED values at left, spanning five orders of magnitude to nuclear and muon results at right.](./figures/book_13_precision_landscape.png)

**The QED chain.** Complete. a_e → α → R∞ → a₀ → μ₀ → f(1S-2S). Six sub-ppb values following α-power scaling. Limited by hadronic light-by-light uncertainty (0.14 ppb) and the a_e measurement (0.11 ppb). Improving either requires experimental advances outside the framework — better lattice QCD calculations or a new Penning trap measurement. The derivation itself is finished. There is nothing more to compute here with current inputs.

**The cosmology-nuclear chain.** Complete. Gauge integers (11, 13) → (22/13)π → Ω_b → η₁₀ → D/H, Y_p, He-3, Li-7. Four primordial abundances from two integers and π. Three match within measurement uncertainty. One reproduces the lithium problem. The BBN physics is standard. The fitting formulas are published. The chain is computed and verified. Extending it would mean adding Li-6, Be-7, or updating the nuclear reaction rates — incremental improvements, not structural advances.

**The electroweak sector.** Mature. M_W from two paths (195 ppm and 402 ppm), consistency at 207 ppm. Γ_Z and six partial widths. R_l. sin²θ_eff. N_gen = 3. The sector uses sin²θ_W and α_s as inputs — both now derivable from two-loop unification. The next step (re-running with derived inputs) requires zero new code. It's ready. It hasn't been done yet only because the sessions focused on other targets first.

**The coupling sector collapse.** Done. sin²θ_W = 0.231223 (12 ppm). α_s = 0.11838 (0.33%). Both from α_em plus CD integer betas. The three SM couplings collapse to one. The two-loop RGE, the crossing finder, the backward integration, the forward check — all verified, reproducible, in the pool.

**The CD evidence.** Five lines, five domains, all passing. Gap ratio 38/27 (exact). CKM deficit 0.83σ. α_s one-loop 8.74%. Two-loop gap 0.027 (218× better than SM). sin²θ_W 12 ppm. The CD is the most tested BSM candidate in the framework.

**The spectroscopy bridge.** Done. f(1S-2S) at 0.44 ppb. The scaling method absorbs all QED corrections. The error budget is 99.998% from the R∞ residual. Extensible to deuterium 1S-2S, He⁺ 1S-2S, and other transitions using the same R∞.

---

### Close

![Fig. 6: Proton lifetime scales as M_GUT⁴ — SM is excluded by Super-K, CD sits in the Hyper-K sensitivity window (2027-2037), the most concrete falsifiable prediction.](./figures/book_06_proton_decay.png)

These are computations where all inputs exist in the pool, the physics is standard, and the derivation function hasn't been written yet. Each could be done in an afternoon.

**M_W from derived sin²θ_W.** The existing `experiment_ew_oneloop_v1` computes M_W from measured sin²θ_W. Feeding it the derived sin²θ_W = 0.231223 instead of measured 0.23122 requires changing one input. The result should be M_W within ~1 MeV of the current 80,337 MeV. This is the simplest cascade step — it validates that the coupling sector collapse propagates correctly into the mass sector.

**Proton lifetime from M_GUT.** M_GUT = 10¹⁵·⁶¹ is in the pool. α_GUT = 1/42.135 is in the pool. The proton matrix element |α_H|² = 0.012 GeV³ is in the pool. The formula τ_p ∝ M_GUT⁴/(α_GUT² m_p⁵ |α_H|²) is one line. The result lands in the Hyper-K sensitivity window (10³⁴-10³⁵ years). This is the most concrete falsifiable prediction of the framework: Hyper-K starts taking data in 2027.

**G_F from derived couplings.** The Fermi constant G_F is currently an input (used in M_W path B). If M_W is derived from sin²θ_W (path A), then G_F can be derived from M_W + α + sin²θ_W via the Sirlin relation. This converts G_F from input to output, increasing the surplus by 2. The derivation uses the same Δr_total already in the pool.

**sin²θ_eff from M_W.** The effective weak mixing angle at the Z pole — sin²θ_eff = κ_Z × sin²θ_W(on-shell) — is a one-formula conversion from the on-shell value. κ_Z = 1.0353 is in the pool. One multiplication. One more derived value.

**Additional spectroscopy.** Deuterium 1S-2S uses the same R∞ scaling with the deuteron reduced mass factor. He⁺ 1S-2S uses Z² = 4 scaling. The hydrogen-deuterium isotope shift uses the mass ratio only (R∞ cancels in the difference, so the shift is independent of the α precision). Each is one derivation function, one experiment JSON, one comparison. Three or four more sub-ppb values from existing infrastructure.

**Complete what-if scan.** 5 of 15 BSM candidate representations have been tested. 10 remain. Each requires pre-computing the beta shifts (Δb₁, Δb₂, Δb₃) from the representation quantum numbers, creating one values file and one experiment JSON, and running the gap ratio computation. The CD is the only candidate that produces an exact Fraction gap ratio with small integers. Completing the scan would strengthen this uniqueness claim from "5 of 15 tested" to "15 of 15 tested, only CD passes."

All of these are one-session tasks. None require new physics. None require new mathematical tools. They require writing derivation functions, creating experiment JSONs, running them, and reading the reports. The infrastructure is in place. The inputs are in the pool. The physics is textbook.

---

### Medium Distance

These require new derivation infrastructure but no new physics. Each is a defined computation with known formulas that hasn't been implemented in DATA-6 yet.

**GUT threshold corrections.** The 0.027 two-loop gap is not zero. Closing it exactly requires parametrizing the heavy GUT particle mass splitting — the ratios M_X/M_GUT and M_T/M_GUT, where M_X and M_T are the masses of the heavy gauge bosons and colored Higgs triplet in the SU(5) completion.

The Langacker-Polonsky formulas (1993) express the threshold corrections as:

δ_i = (b_i^heavy / 2π) × ln(M_heavy/M_GUT)

where b_i^heavy are the beta coefficients of the heavy particles. The gap of 0.027 determines the required threshold correction: δ₃ − δ_GUT = −0.027. This constrains the heavy particle mass ratios.

The computation is standard GUT physics. The formulas are published. The constraint is one equation with two unknowns (two mass ratios), so it determines a curve in parameter space, not a unique point. But the curve tells you: what mass spectrum does the GUT completion need to have? If the required spectrum is natural (all heavy particles near M_GUT), the CD model is viable. If it requires extreme fine-tuning (mass ratios of 10¹⁰ or more), the model is stressed.

Given that the gap is only 0.027 out of α_GUT⁻¹ = 42.135 (0.064%), the required threshold correction is tiny. This strongly suggests a nearly degenerate spectrum — all heavy particles near the same mass. Minimal fine-tuning. The computation would confirm this quantitatively.

**Vacuum stability.** The Higgs quartic coupling λ runs with energy. In the SM, λ decreases with energy and may cross zero around 10¹⁰-10¹² GeV — meaning the electroweak vacuum is metastable (it could tunnel to a lower-energy state, but the lifetime is longer than the age of the universe).

The CD modifies the running of λ through the VL quark Yukawa coupling. If the CD mass is ~3 TeV, its Yukawa coupling contributes to the λ running at all scales above 3 TeV. Depending on the Yukawa value, this either stabilizes the vacuum (λ stays positive up to M_GUT) or destabilizes it further.

The computation requires: the Higgs quartic running equation (known), the CD Yukawa coupling (a free parameter, but constrained by the CD mass), and the two-loop corrections (known for the SM, need to be extended for the CD). The output is a prediction: for CD mass = 3 TeV, is the vacuum stable? The answer is testable against the measured m_H = 125.2 GeV.

**α(M_Z) from first principles.** Currently, α(M_Z) = 1/127.95 is used as a measured input. It should be derivable from α(0) = 1/137.036 by running α from zero energy to M_Z using the vacuum polarization:

α(M_Z)⁻¹ = α(0)⁻¹ − Δα_lep − Δα_had − Δα_top

The leptonic part Δα_lep = 0.03150 is computable from QED (known masses, known coupling). The hadronic part Δα_had = 0.02766 is the bottleneck — it requires either dispersive analysis of e⁺e⁻ → hadrons data or lattice QCD computation. Both are active research areas with improving precision.

The current attempt in DATA-6 gives α(M_Z)⁻¹ = 128.93, missing the measured 127.95 by 0.76%. The miss comes from an incomplete Δα sum. Completing it requires either adding higher-order terms or using the lattice QCD result for Δα_had directly.

**Three-loop sin²θ_W.** The current prediction (12 ppm) uses two-loop running. Three-loop beta coefficients are known for the SM. The CD's three-loop contribution would need to be computed (a defined calculation in perturbative QFT, not an open problem). The three-loop running would either improve the prediction (smaller miss) or worsen it (larger miss). Either outcome is informative — it tests whether the two-loop result is a convergent approximation or a lucky cancellation.

---

### Far

These require either significant theoretical work or new experimental inputs that don't yet exist.

**The mass hierarchy.** Why is the electron mass 0.511 MeV? Why is the muon 207 times heavier? Why is the top quark 340,000 times heavier than the electron? The Standard Model doesn't explain the fermion mass hierarchy — the masses are free parameters, measured but not derived.

The soliton boundary framework says: each fermion is a vortex pattern at a specific scale. Different patterns have different inertia. The electron is the simplest vortex (lowest energy, least structure). The muon is a more complex vortex (higher energy, more internal structure). The top quark is the most complex (highest energy, most internal circulation).

But saying "different patterns have different inertia" is not a computation. To actually derive m_e = 0.511 MeV from the soliton boundary structure, you would need:

A mathematical description of the soliton boundary (what equation does it satisfy? what are the boundary conditions?)

A solution for the ground state (the lightest stable vortex pattern)

A calculation of the ground state's inertia (the resistance of the pattern to acceleration)

An identification of this inertia with the electron mass

None of these steps are done. The soliton boundary equation is not written down. The ground state is not computed. The inertia is not calculated. This is the deepest open problem in the framework — and it may be the deepest open problem in physics.

The Koide formula — K = 2/3, predicting m_τ from m_e and m_μ at 62 ppm — hints that the mass hierarchy has structure. The charged lepton masses satisfy a specific algebraic relation that involves the integer 2/3 and an amplitude parameter a² ≈ 2. If a² = 2 exactly, m_τ = 1776.97 MeV. Measured: 1776.86 MeV. The miss is 62 ppm.

But the Koide formula is an observation, not a derivation. Why K = 2/3? Why a² ≈ 2? The formula floats as an unconnected island (the atoll) in the derivation map. Connecting it to the mainland — deriving K and a from the soliton boundary structure — would be a major advance. It hasn't been done because the soliton boundary structure isn't mathematically defined.

**The neutrino sector.** Neutrinos have mass — we know this from neutrino oscillations (Nobel Prize 2015). But the masses are tiny (< 0.1 eV, at least a million times lighter than the electron) and the pattern of mixing (the PMNS matrix) is very different from the quark mixing pattern (the CKM matrix). Quarks mix by small angles (the Cabibbo angle is 13°). Neutrinos mix by large angles (θ₁₂ ≈ 34°, θ₂₃ ≈ 49°).

The framework has nothing to say about neutrino masses yet. The Cabibbo Doublet is in the quark sector — it doesn't directly affect the lepton sector. Neutrino masses might come from a see-saw mechanism (requiring right-handed neutrinos at the GUT scale), from radiative corrections, or from some other mechanism. Each would leave a different imprint on the integer structure.

The neutrino sector is far because it requires new value nodes (neutrino masses, PMNS mixing angles), new derivation functions (whatever mechanism generates the masses), and possibly new theoretical structure (the see-saw mechanism involves physics at 10¹⁴-10¹⁶ GeV that hasn't been worked into the framework).

**Gravity from integers.** The gravitational constant G = 6.674 × 10⁻¹¹ N·m²/kg² is measured but not derived. The model says G is a soliton boundary reading at the Earth's Hill sphere scale, analogous to how α is a reading at the atomic scale. But the analogy is not a computation.

To derive G from integers, you would need to identify which soliton boundary produces the gravitational reading, which integer Fractions determine the reading, and how the reading runs with scale (the gravitational analog of the RGE beta function). General relativity provides the framework (Einstein's field equations relate the geometry of spacetime to the energy-momentum content), but the connection between the gauge integers and the gravitational sector is not established.

The dark matter ratio (22/13)π being correct to 725 ppm is the first hint of a connection — the gauge integers predict a gravitational-scale observable. But going from "the DM ratio involves gauge integers" to "G is derivable from the same integers" requires bridging the gap between the gauge sector (QFT on flat spacetime) and the gravitational sector (curved spacetime dynamics). This is the gauge-gravity connection — one of the central unsolved problems in theoretical physics.

---

### Possibly Impossible

Some things may be beyond the reach of any framework built on the current mathematical structures.

**The gauge group itself.** Why SU(3) × SU(2) × U(1)? Why these three numbers — 3, 2, 1 — and not others? The Standard Model takes the gauge group as given. GUT models embed it in larger groups (SU(5), SO(10), E₆) but don't explain why the larger group exists either.

The soliton boundary framework says: the gauge group describes the symmetries of the quantum vacuum — the ways in which the vacuum can sustain disturbances. But it doesn't explain why the vacuum has these symmetries and not others. This is like asking "why does space have three dimensions?" — it may have an answer, or it may be a brute fact about the universe.

If the gauge group is derivable, it would have to come from the soliton boundary structure at the deepest level — the mathematical properties of self-sustaining patterns in the vacuum would have to uniquely determine SU(3) × SU(2) × U(1) as the only consistent set of symmetries. This is a beautiful idea. It has no known mathematical formulation.

**The number of generations.** Why three? Three generations of quarks and leptons, with identical quantum numbers but different masses. The number three is measured (from the Z invisible width: N_gen = 3.00 ± 0.01). It is not derived.

The framework can compute consequences of three generations (the beta coefficients assume n_f = 3 families). But it cannot explain why n_f = 3 rather than 4 or 17 or infinity. The number of generations is an integer — it should be derivable from integer structure. But no derivation exists.

One speculative connection: the Koide formula uses a C₃ symmetry — cyclic symmetry of three objects. If the three generations are related by a discrete symmetry of the soliton boundary structure, the number three might come from the geometry. But "might come from" is not a derivation.

**The cosmological constant.** Why is the vacuum energy 10⁻¹²² in Planck units? The framework says: it's the ground state reading of the outermost soliton boundary, and it's small because the boundary is large. But this qualitative argument doesn't produce the number. Deriving Λ = 5.88 × 10⁻³⁰ g/cm³ from integers would require understanding the vacuum structure at a level that nobody — in any framework — has achieved.

The cosmological constant problem is often called "the worst prediction in physics" because naïve quantum field theory predicts a vacuum energy 10¹²⁰ times larger than observed. The soliton boundary model doesn't solve this problem. It reframes it — the vacuum energy is a boundary reading, not a sum of zero-point energies — but the reframing doesn't produce a number.

---

### The Map with Edges

![Fig. 7: The complete derivation graph — eight physics domains connected by twelve crossings, hydrogen at both ends, Koide atoll floating disconnected, surplus +40.](./figures/book_07_eight_domains.png)

Here is the honest map. Solid lines are computed and verified. Dashed lines are close (inputs available, physics known, computation not yet performed). Dotted lines are far (theoretical work needed). Absent lines are possibly impossible (no known mathematical path).

```
COMPUTED (solid)
├── a_e → α → R∞ → a₀, μ₀ → f(1S-2S)          0.007-0.44 ppb
├── Gauge integers → (22/13)π → Ω_b → η → D/H    725 ppm to 0.12σ
├── CD betas → gap 38/27 → M_GUT → α_GUT          exact to 0.064%
├── Two-loop crossing → sin²θ_W, α_s               12 ppm, 0.33%
├── sin²θ_W + M_Z → M_W, Γ_Z, widths, R_l         195 ppm to 0.84%
├── CD → 4×4 CKM → unitarity deficit               0.83σ
├── α → a_μ(QED) → SM total → 6.5σ anomaly         reproduced
└── Koide K=2/3 → m_τ                              62 ppm (atoll)

CLOSE (dashed)
├── M_W from derived sin²θ_W                       zero new code
├── τ_p from M_GUT                                 one formula
├── G_F from derived M_W                           one derivation
├── sin²θ_eff from M_W                             one formula
├── D, He⁺ spectroscopy from R∞                    same scaling
└── Complete what-if scan                          10 candidates

MEDIUM (dotted)
├── GUT thresholds (close 0.027 gap)               Langacker-Polonsky
├── Vacuum stability (m_H from λ running)          CD Yukawa needed
├── α(M_Z) from VP running                        lattice Δα_had
└── Three-loop sin²θ_W                            three-loop CD betas

FAR (distant)
├── Mass hierarchy (m_e, m_μ, m_τ, m_t...)        soliton ground state
├── Neutrino masses and mixing                     see-saw or radiative
├── G from integers                                gauge-gravity bridge
└── Koide bridge (a² = 2 from soliton structure)  unknown path

POSSIBLY IMPOSSIBLE
├── Why SU(3) × SU(2) × U(1)?                     deepest structure
├── Why three generations?                         generation symmetry
└── Cosmological constant from integers            vacuum structure
```

---

### What the Edges Mean

The edges are not failures. They're the boundary of the explored territory.

Every map has edges. The early maps of the world had edges labeled "here be dragons." The dragons weren't real — they were place holders for ignorance. The edge of the map meant "we haven't been here yet," not "nothing exists here."

The derivation map is the same. The edge at the mass hierarchy means "we don't know how to derive m_e from integers yet." It doesn't mean it can't be done. It means the soliton boundary structure — the mathematical equation that describes self-sustaining patterns in the quantum vacuum — hasn't been written down, let alone solved. Writing it down is a theoretical problem. Solving it is a computational problem. Both are hard. Neither is impossible.

The edge at gravity means "we don't know how to connect the gauge integers to the gravitational reading." It doesn't mean the connection doesn't exist. The dark matter ratio (22/13)π connects gauge integers to a gravitational-scale observable at 725 ppm. The connection is there. The computation is not.

The edge at the gauge group itself means "we don't know why SU(3) × SU(2) × U(1)." This might be the deepest question in physics. It might have an answer within the soliton framework (the boundary structure uniquely determines the symmetry group). It might have an answer outside any current framework. It might be a brute fact — the universe just has this symmetry, and asking why is like asking why there's something rather than nothing.

The model doesn't need to answer every question to be correct. Newton's mechanics was correct for 200 years before Einstein extended it. Einstein's relativity is correct but doesn't explain quantum mechanics. Quantum mechanics is correct but doesn't explain gravity. Each framework has edges. The edges don't invalidate the interior.

The interior of this map — 53 derived values across eight domains, surplus +40, every test passing — is solid. The edges are where the next work begins.

---

### The Invitation

This chapter is an invitation.

The "close" items are ready for anyone with Python, mpmath, and the DATA-6 pool. Derive the proton lifetime. Re-run the EW sector with derived sin²θ_W. Complete the what-if scan. Test additional spectroscopic predictions. Each is a publishable result. Each requires an afternoon of work with the existing tool.

The "medium" items are ready for anyone with a background in perturbative QFT or lattice QCD. Compute the GUT threshold corrections. Run the vacuum stability analysis. Extend the VP running to three loops. Each is a defined calculation with known formulas and available inputs.

The "far" items are research programs. Derive the electron mass from the soliton boundary structure. Connect the gauge integers to G. Explain the number of generations. Each is a career's worth of work — or more.

The "possibly impossible" items are the deep questions. Why this gauge group? Why three generations? Why this vacuum energy? These may be answerable. They may not. Attempting them is what theoretical physics is for.

The pool is open. The tool is documented. The derivation functions are readable code. The experiments are JSON files. The map is drawn with its edges clearly marked. Anyone who wants to extend the map — to push an edge outward, to connect a new domain, to test a new prediction — has everything needed to start.

The torch is lit. It's designed to be carried.
