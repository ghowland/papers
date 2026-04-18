## Review of PHYS-44 Experiment Plan

### What's Right

The five-derivation structure is clean. Each derivation answers a specific question, and they build on each other logically: classify (2) → check frozen scan coverage (3) → scan the hierarchy (4) → isolate K-unique contributions (5), all anchored by the central prediction (1). The experiment reads from the existing pool, adds only 2 new value nodes, and produces 20 comparisons. This follows the DATA-7 workflow correctly.

The sector splitting formula using SM betas instead of CD-modified betas is the right call at laboratory scale. The CD shifts matter at GUT-scale running. At Earth's gravitational potential, you're probing the hierarchy at the laboratory energy scale (~eV to ~GeV), where the SM betas govern the running. The CD betas become relevant only if the hierarchy mapping connects laboratory gravity to GUT-scale energies, which is the κ question. Using SM betas is more conservative and more defensible.

The classification of PHYS-42 tests into D/K/mixed/structural is the most useful output of the experiment. Nobody has done this decomposition before — not because it's hard, but because nobody had the conceptual framework to motivate it. The classification table in derivation 2 is correct for every entry I can verify.

### What Needs Correction

**The |β₃ − β₁| computation is wrong.**

The plan says:

> |β₃ − β₁| = |−7 − 41/10| = |−111/10| = 111/10 = 11.1

Check: −7 − 41/10 = −70/10 − 41/10 = −111/10. That arithmetic is correct. But this is the wrong quantity.

The β coefficients in the pool are the one-loop coefficients for the gauge coupling running: how α_i⁻¹ changes with ln(μ). They describe running along the energy-scale projection of the hierarchy. The sector splitting formula asks: how do readings differ between sectors at a given gravitational depth? This is running along the gravitational projection.

The question is whether the same β coefficients govern both projections. The paper (PHYS-43) assumes they do, via the conversion factor κ. If κ = 1, the gravitational running rate equals the energy-scale running rate. If κ ≪ 1, the gravitational running is suppressed.

The formula ε = κ × |Δβ| × ΔΦ/c² mixes two things: |Δβ| (dimensionless, from the energy-scale RGE) and ΔΦ/c² (dimensionless, from gravity). The product |Δβ| × ΔΦ/c² has a specific dimensional analysis meaning: it is the fractional coupling difference between sectors, per unit of gravitational depth, if the hierarchy mapping is 1:1. The factor κ parameterizes the departure from 1:1.

So the arithmetic is right but the derivation should be explicit about what |β₃ − β₁| means physically: it is the difference in the rate of change of α₃⁻¹ and α₁⁻¹ per unit of hierarchy coordinate, evaluated at the laboratory scale. The derivation should output this quantity with a clear label, not just compute it silently.

**The β coefficients should include GUT normalization for β₁.**

The pool has `beta_sm_u1_total_v0` = 41/10. This is the U(1)_Y beta coefficient with the standard SU(5) GUT normalization factor k₁ = 3/5 already absorbed into the definition. When computing sector differences, you need to be clear about which normalization you're using.

For the sector splitting, the relevant quantity is the difference in how each gauge coupling runs. The coupling α₁ (GUT-normalized) runs with β₁ = 41/10. The coupling α₃ runs with β₃ = −7. These are the correct pool values. The difference |−7 − 41/10| = 111/10 is the correct sector splitting coefficient in the GUT-normalized basis.

But: the optical clock does not measure α₁ (GUT-normalized). It measures α_em (the fine structure constant), which is related to α₁ and α₂ through sin²θ_W. The running of α_em is not β₁ — it is a combination involving both β₁ and β₂. Specifically, α_em⁻¹ = α₁⁻¹/k₁ + α₂⁻¹ at the Z mass (ignoring running between M_Z and laboratory scale, which is tiny).

At laboratory energies, α_em is effectively frozen — it doesn't run between 1 eV and 1 GeV at any measurable level. So the "electromagnetic sector running rate" relevant to the clock is not β₁ but rather the effective β_em at laboratory scale, which is approximately zero (α_em changes by ~1% from atomic scale to Z mass, which is negligible compared to α_s changing by a factor of ~2 over the same range).

This matters for the prediction. If the electromagnetic sector has effective β_em ≈ 0 at laboratory scale, and the strong sector has β₃ = −7, then the sector difference is |−7 − 0| = 7, not 111/10 = 11.1. The prediction changes by about 40%.

The derivation should compute both: the formal |β₃ − β₁| from pool values (for the energy-scale running comparison) and the effective |β₃_eff − β_em_eff| at laboratory scale (for the actual clock comparison). The second is the physically relevant quantity for the prediction. The first is the quantity that connects to the GUT-scale chain.

Actually, let me reconsider this. The sector splitting is not about running at laboratory scale. It is about how readings change across a gravitational boundary. The hypothesis is that the gravitational boundary acts like an energy-scale boundary — crossing ΔΦ/c² in gravity is analogous to crossing Δ(ln μ) in energy. The β coefficients tell you how couplings change per unit of ln μ. The sector splitting formula says: they also tell you how couplings change per unit of Φ/c², up to the conversion factor κ.

In this interpretation, you want the full β coefficients, not the laboratory-scale effective running. The laboratory-scale running is small because you're looking at a tiny energy range. But the gravitational "running" is looking at a different projection of the hierarchy altogether. The β coefficients are structural — they are properties of the representation content, not of the energy scale. They are the same Fractions at every scale: 41/10 and −7 everywhere from 1 eV to M_GUT.

So: use the full β coefficients from the pool. The |β₃ − β₁| = 111/10 is correct. The subtlety about effective running is a distraction — the hypothesis is that the full structural β difference governs the gravitational sector splitting, regardless of the energy scale at which you probe.

The derivation should note this explicitly and output both for comparison: the structural |Δβ| and the effective running difference at laboratory scale. They are different numbers and the experiment will determine which (if either) is relevant.

**Derivation 2 classification has a subtle error with Mercury.**

The plan classifies Mercury perihelion as "D — Geometric curvature (formula is static)." This is correct as a classification of the prediction formula. But there is a subtlety: the formula δω = 6πGM/(ac²(1−e²)) gives the precession per orbit. An orbit is a temporal concept — it requires ticking. You cannot have "per orbit" without ticks.

However, the formula itself does not use time. It uses spatial quantities (GM, a, e, c) and produces an angle (radians per orbit, where "per orbit" is dimensionless because it's per 2π radians of orbital phase). The precession rate is a geometric property of the orbit, not a temporal evolution. The orbit's shape is determined by the spatial curvature. The precession is what happens when you trace the orbit through the curved space. You can trace an orbit in frozen time — it is a closed curve in configuration space, and the precession is a geometric property of that curve.

So the classification is correct: Mercury is D. But the derivation should note that "per orbit" is a spatial concept (one loop around the closed curve), not a temporal concept (one period of elapsed time). The experiment's documentation should make this distinction explicit because it illustrates the D/K decomposition: the orbit's geometry is D, the time to traverse it is K, but the precession rate (angle per loop) is pure D.

**Derivation 3 has a conceptual issue with "D-complete given τ_rest as input."**

The plan says muon dilation is "D-complete given τ_rest as input." This is technically correct but conceptually misleading. The muon rest lifetime τ_rest is a K-quantity — it is how many ticks the muon survives. By importing it as an input, you are importing K information into the frozen scan. The frozen scan is then not purely spatial — it uses a measured temporal quantity.

The honest classification: muon dilation requires both D and K. The D component is γ (computed from the spatial trajectory). The K component is τ_rest (measured temporal quantity). The prediction τ_lab = γ × τ_rest is a D × K product.

The derivation should classify this as "mixed" rather than "D-complete given input." The whole point of the decomposition is to separate D and K. If you allow importing K quantities as inputs, every test becomes "D-complete given enough K inputs," which defeats the purpose.

The correct statement: muon dilation is the clearest example of a D × K product. It is the test that demonstrates the two components work together. The Lorentz factor γ is the D factor (how much the reading changes at that velocity). The rest lifetime is the K factor (how many ticks are available). The lab lifetime is their product. Neither factor alone predicts the observation.

**Derivation 5 should compute the D/K decomposition of each PHYS-42 result, not just the K-unique contribution.**

The plan says derivation 5 "isolates the K-unique contribution." But the more useful computation is the full decomposition: for each test, what fraction of the observed quantity comes from D and what fraction from K?

For GPS: D contribution = +45.85 μs/day (gravitational shift). K contribution = −7.21 μs/day (velocity shift). D fraction = 45.85/(45.85 + 7.21) = 86.4%. K fraction = 13.6%. (Note: the fractions don't quite add because the signs differ — the net is D − |K|.)

For muon: D contribution = γ ≈ 15.8 (reading depth factor). K contribution = τ_rest ≈ 2.197 μs (tick budget). These are multiplicative, not additive, so "fraction" is not the right decomposition. Instead: the observed lab lifetime depends on D through γ and on K through τ_rest. Changing D (different velocity) changes the prediction. Changing K (different particle with different lifetime) changes the prediction. Both are independently measurable.

For SN Ia: D contribution = the reading depth at the emission epoch (determines the photon frequency). K contribution = the number of ticks between emission and observation (determines the stretching). The stretch factor (1+z) is purely K — it is the ratio of scale factors at two different tick counts. The spectral features are D — they encode the emission reading depth.

The derivation should output the D component and K component for every test where the decomposition is meaningful, not just flag which tests need K. This gives the reader a quantitative sense of how much each component contributes at each level of the hierarchy.

**The connection between ε_sector and existing EP violation bounds needs attention.**

The plan mentions existing EP tests (MICROSCOPE at 10⁻¹⁵, LLR at 10⁻¹³) but does not compute whether the predicted sector splitting is consistent with these bounds. If ε_sector(κ=1) = 1.2 × 10⁻¹², this is LARGER than the MICROSCOPE WEP bound of 10⁻¹⁵.

But this is not a contradiction, because MICROSCOPE tests free fall (WEP), not clock rates (EEP). WEP says: different materials fall at the same rate. EEP says: different clocks at the same potential tick at the same rate. These are different tests. MICROSCOPE dropped titanium and platinum — both probe the electromagnetic sector (their masses are dominated by nuclear binding, but the free fall test compares gravitational coupling, not clock rates). A sector splitting in clock rates does not imply a sector splitting in free fall rates, because free fall couples to total energy (all sectors combined), not to individual sector readings.

However, the derivation should compute and output the WEP prediction from the sector splitting model. If the splitting is in the readings (coupling strengths at different depths), does it produce a WEP violation? The answer depends on whether the gravitational coupling (which determines free fall) is sector-blind or sector-dependent. In standard GR, the gravitational coupling is universal (equivalence principle). In the D-sector scenario, the gravitational coupling may be the SUM of all sector readings, which is sector-blind even though individual readings are sector-dependent. The derivation should check this explicitly: compute the predicted WEP violation (if any) and compare to the MICROSCOPE bound.

If the D-sector scenario predicts WEP violation at a level above 10⁻¹⁵, it is already ruled out by MICROSCOPE. If it predicts no WEP violation (because gravity couples to the sum of readings, not individual readings), then the sector splitting is a purely EEP effect — measurable in clocks but not in free fall. This distinction is important and the experiment should document it.

**The "spacetime doesn't exist as a unified thing" claim needs hedging.**

The plan says:

> Spacetime doesn't exist as a unified thing. There is space (the soliton hierarchy, navigable by readings) and there is the clock (the Planck tick, monotonically incrementing). They are not woven together into a 4D manifold.

This is the RUM interpretive claim. It is not established by the experiment. The experiment computes predictions that are consistent with this claim, but every prediction is also consistent with standard GR (where spacetime IS a unified 4D manifold). The experiment cannot distinguish the two interpretations — only Test 1 (nuclear vs optical clock) can, and that test requires future hardware.

The experiment plan should state this clearly: the decomposition into D and K is an analytical tool within the RUM framework. It organizes the PHYS-42 results into two categories. It makes a prediction (sector splitting) that is testable. But the decomposition itself is not proven by the experiment — it is tested by the experiment. If all 20 comparisons PASS, it means the decomposition is self-consistent. It does not mean spacetime is not a unified manifold.

The language should be: "the experiment tests whether the D/K decomposition is internally consistent and produces a testable prediction." Not: "the experiment proves that spacetime is two things."

---

### Specific Corrections to the Experiment Plan

**Correction 1: β difference.**

Use |β₃ − β₁| = |−7 − 41/10| = 111/10 = 11.1 as the structural coefficient (from pool). Also compute and output the effective coupling difference at laboratory scale for comparison. Note explicitly that the SM betas are used, not CD-modified, because the clock comparison probes the laboratory energy scale.

But also note the PHYS-43 paper used the CD betas and got |β₃ − β₁| = |−20/3 − 25/6| = 65/6 = 10.833. The derivation should output BOTH and explain the difference: SM betas are the physical running rates at laboratory scale. CD betas are the physical running rates if the Cabibbo Doublet exists. At laboratory energies (far below the CD mass), the SM betas govern. The CD betas govern at scales above the CD threshold. The sector splitting at Earth's potential probes the laboratory scale, so SM betas are correct.

Wait — I need to reconsider this more carefully. The sector splitting formula is:

ε = κ × |Δβ| × ΔΦ/c²

This says: the fractional frequency difference between two clocks scales with the β difference. But WHICH β difference? The β coefficients describe how couplings run with energy. The gravitational potential ΔΦ/c² is not an energy. The formula assumes that ΔΦ/c² maps to an energy-scale change via κ.

If κ maps Φ/c² to ln(μ/μ₀), then ε = |Δβ| × κ × ΔΦ/c² is the coupling difference that would result from running the couplings by an amount κ × ΔΦ/c² in ln μ.

At any energy scale, the β coefficients are the same (at one-loop — they are constants). So it does not matter whether you use SM or CD betas, because the one-loop β coefficients don't depend on the energy scale at which you evaluate them. They are structural constants of the representation content.

BUT: if the CD exists as a real particle with mass M_CD, then below M_CD, the effective β coefficients are the SM values, and above M_CD, they are the CD-modified values. The CD is "integrated out" below its mass. At laboratory energies (eV to GeV), the effective betas are SM. At GUT energies (10¹⁵ GeV), the effective betas are CD-modified.

So: the choice depends on what energy scale the gravitational hierarchy mapping connects to. If κ maps Earth's Φ/c² to an energy scale below M_CD, use SM betas. If above, use CD betas. Since we don't know M_CD (lower bound ~few hundred GeV from LHC), and since Earth's Φ/c² ~ 10⁻⁹ presumably maps to a very low energy scale, SM betas are the safe choice.

The derivation should output both predictions (SM and CD betas) and let the future measurement distinguish them. If the measured ε matches the SM β difference, the hierarchy mapping connects gravity to low-energy running. If it matches the CD β difference, the mapping connects to high-energy running. Both outcomes would be extraordinary.

**Correction 2: Add WEP consistency check.**

Add a computation to derivation 1: given the predicted sector splitting ε, compute the predicted WEP violation (if any). The WEP tests whether different materials fall at the same rate. If the gravitational coupling is the sum of all sector readings (g = Σ g_sector), and the sector readings differ by ε, then two materials with different sector composition (e.g., nuclear vs electromagnetic binding energy fractions) would experience different g. Compute Δg/g for titanium vs platinum (the MICROSCOPE pair) and compare to the MICROSCOPE bound of 10⁻¹⁵.

If the predicted Δg/g exceeds 10⁻¹⁵, the D-sector scenario with κ near 1 is already constrained by MICROSCOPE. The derivation should output the MICROSCOPE-compatible range of κ.

**Correction 3: Fix muon classification.**

Change muon dilation from "D-complete given τ_rest as input" to "mixed D×K." The derivation should output the D component (γ) and the K component (τ_rest) separately and note that the observation is their product.

**Correction 4: Expand derivation 5.**

For each test, output the D component and K component separately (where applicable), not just the K-unique contribution. The D/K ratio at each hierarchy level is a primary result of the experiment.

**Correction 5: Add PHYS-43 consistency check.**

The experiment should verify internal consistency with PHYS-43: the sector splitting computed here (from SM betas) should be compared to the PHYS-43 prediction (from CD betas). The ratio of the two predictions is |111/10| / |65/6| = (111 × 6) / (10 × 65) = 666/650 = 1.025. They differ by 2.5%. This is a small difference but the derivation should compute and output it, because the future measurement will determine which set of betas is relevant.

---

### The Deeper Conceptual Issue

The other Claude's plan uses language like "spacetime doesn't exist as a unified thing" and "the Minkowski metric is actually two things." These are strong metaphysical claims. The experiment does not test them. The experiment tests whether the D/K decomposition is internally consistent and produces a measurable prediction.

Here is what I think the correct framing is, based on having worked through 42 papers of this framework:

**The D/K decomposition is an analytical tool, not an ontological claim.** It says: take the GR dilation formula, which everyone agrees works, and decompose it into two parts. One part (D) is spatial structure — the readings at each depth of the hierarchy. The other part (K) is temporal process — the ticking that allows things to happen. This decomposition is always possible (any formula with spatial and temporal inputs can be decomposed this way). The question is whether the decomposition is USEFUL — whether it reveals structure that the unified treatment hides.

**The sector splitting is where the decomposition becomes physical.** If D is sector-dependent (different β coefficients for different force sectors), the decomposition predicts something that the unified treatment does not: nuclear and optical clocks disagree. This is a physical prediction, not a vocabulary change. It turns the analytical decomposition into a testable hypothesis.

**The classification of PHYS-42 tests into D/K/mixed is where the decomposition becomes informative.** Even without sector splitting, knowing that 9 of 18 tests are pure-D (computable from frozen geometry) and 3 are K-required (need ticking) organizes the results in a way that the unified treatment doesn't. It shows that most of GR is geometry, not dynamics. The dynamic part (velocity, lifetime, expansion) is a minority of the evidence.

**The experiment's value is the prediction and the classification, not the metaphysics.** Whether "spacetime is one thing" or "spacetime is two things" is philosophy. Whether nuclear clocks and optical clocks agree at 10⁻¹⁸ is physics. The experiment should lead with the physics and let the philosophy follow from the data.

---

### Summary of Recommended Changes

1. Compute sector splitting with BOTH SM and CD betas, output both, note the 2.5% difference
2. Add WEP consistency check against MICROSCOPE bound
3. Reclassify muon as mixed D×K, not D-complete
4. Expand derivation 5 to output D/K decomposition for all tests, not just K-unique
5. Add PHYS-43 consistency check (SM vs CD β ratio)
6. Hedge the "spacetime is two things" language — the experiment tests the decomposition, it doesn't prove the ontology
7. Note explicitly that Mercury "per orbit" is a spatial concept (per 2π radians of orbital phase), reinforcing the D classification
8. Note that the β coefficients are structural constants (same at all energy scales at one-loop) so SM vs CD distinction is about whether the CD is integrated out, not about energy-dependent β

The experiment structure (5 derivations, 20 comparisons) is right. The values needed (2 new nodes) are right. The connection to the pool is right. The corrections above refine the physics content without changing the structure.
