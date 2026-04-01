Let me read the uploaded files first to see what we have from the original MATH-2 and MATH-4 work.Good. Now I have the full Q335 basis numerators, the MATH-2 rational pairs, and the original transcendental hierarchy. Let me review the Koide plan and find the problems.

---

# Revised PHYS-12 Plan: Koide from C₃ Symmetry

## Problems with the Original Plan

**Problem 1: The sign argument is circular.** The plan says λ > 0 gives θ = 0 (aligned phases, all masses equal), λ < 0 gives 120° spacing (maximally separated). But then it just PICKS λ < 0 because that's what gives Koide. The question "why λ < 0 for leptons?" replaces "why a² = 2?" — it's the same gap in different clothes. The plan should acknowledge this explicitly and identify what physical principle determines the sign.

**Problem 2: The amplitude derivation is weak.** The plan lists four candidates for selecting a = √2 (maximum entropy, marginal stability, variational, topological/simplex midpoint). The simplex midpoint argument in Step 2.4 is the strongest but it reduces to "midpoint of the variance range," which is the PHYS-8 reformulation restated geometrically. It doesn't explain WHY the midpoint is selected. The equipartition argument in (iii) — kinetic energy equals potential energy — is the only candidate with physics content, and it needs to be tested explicitly.

**Problem 3: The frustrated XY model is well-studied and the plan doesn't cite what's known.** The frustrated antiferromagnet on a triangle with three continuous spins is a textbook problem. The 120° ground state is known. The fluctuation spectrum around it is known. The plan should state what the established literature gives and identify exactly where the Koide connection is new versus known.

**Problem 4: The quark test conflates two things.** The plan says quarks have a > √2 because their phases are perturbed from 120°. But a > √2 with EXACT 120° spacing gives negative masses, which is unphysical. So either (a) the quark phases aren't at 120° (the plan's hypothesis), or (b) the quarks don't live on the same C₃ potential at all. These are different claims and the plan should distinguish them.

**Problem 5: The phase extraction for quarks is underdetermined.** Given three masses m_u, m_c, m_t, the parametrization √m_k = M(1 + a cos(θ₀ + 2πk/3 + δ_k)) has FIVE free parameters (M, a, θ₀, δ₁, δ₂) for three data points. The system is underdetermined unless we fix some parameters. The plan doesn't address this.

**Problem 6: Missing connection to the Q335 basis.** The plan doesn't use the actual MATH-2/MATH-4 integers at all. Every computation should be in Fraction arithmetic using the Q335 numerators I just read from the uploaded files. Specifically: √2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506 / 2³³⁵. This exact value should appear in the Koide computation.

**Problem 7: Gate 2 is too soft.** The plan says "if NONE of these produces a = √2 from a principle independent of the Koide formula itself, proceed to Phase 3 with the spacing result only." This means Phase 3 runs regardless of whether the amplitude is derived. But Phase 3's quark test only makes sense IF the amplitude derivation works — otherwise we're testing a hypothesis (spacing from C₃) that doesn't predict the amplitude, so it can't predict the quark deviations either.

## Revised Plan

### Phase 0: Establish the Exact Arithmetic Foundation (15 min)

**Step 0.1.** Load the Q335 basis from the uploaded files. Verify the key constants needed:
- π = 219886425873192351011826597043241066194671831922348816817425823313156938749437718695100428743935254314 / 2³³⁵
- √2 = 98983668457552556369912251393641781543489938395170417531517516177599375784349358848602281494773475506 / 2³³⁵
- 2π/3 in Q335: multiply π numerator by 2, use divmod to check properties

**Step 0.2.** Compute cos(2π/3) and sin(2π/3) in Fraction arithmetic using the MATH-2 series for cosine and sine at the rational argument 2π/3. Verify cos(2π/3) = −1/2 (exact rational) and sin(2π/3) = √3/2 (requires √3 Q335 numerator = 121229740294912895234576661752159696642961157181742464717663915473198765686797807393142352785809790154 / 2³³⁵).

**Step 0.3.** Load the measured masses from DATA-2 as exact Fractions:
- m_e = Fraction("51099895069", 10**11) (in MeV, 11 digits)
- m_μ = Fraction("1056583755", 10**7) (in MeV, 10 digits)  
- m_τ = Fraction("177686", 100) (in MeV, 6 digits)

**Assert:** all three are positive rationals with the correct number of significant digits.

### Phase 1: The C₃ Potential — What's Known vs What's New (algebra + verification script)

**Step 1.1.** State what IS known from the frustrated XY model literature:

Three unit vectors on a plane (or equivalently, three angles on a circle) with pairwise antiferromagnetic coupling V = +J Σ cos(φ_i − φ_j), J > 0, have a continuously degenerate ground state manifold. The ground state is any configuration with Σ_k e^{iφ_k} = 0 (zero total "magnetization"). The 120° equally-spaced configuration satisfies this but is not unique — any rotation of the triangle is also a ground state. The ground state energy is V = +J × 3 × (−1/2) = −3J/2.

**Step 1.2.** State what is NEW in the Koide connection:

The Koide parametrization √m_k = M(1 + a cos(θ₀ + 2πk/3)) is exactly the constraint Σ_k e^{iφ_k} = 0 evaluated at the specific phase angles φ_k = θ₀ + 2πk/3, projected onto the real axis, with an offset M and scale aM. The zero-magnetization condition of the frustrated XY model IS the equal spacing condition of Koide.

This is NOT the same as deriving Koide. It is a REWRITING. The frustrated XY model gives us the spacing for free (from the ground state condition). What it does NOT give: the amplitude a, the overall scale M, or the reason the masses live on such a potential.

**Step 1.3.** Verification script: compute the potential V and its gradient for three phases at 120° spacing. Verify V is stationary. Verify V is the global minimum for J > 0 (antiferromagnetic).

**Gate 1 decision:** This gate always passes — it's a known result. The question is whether the rewriting teaches us anything new. Proceed only if the rewriting reveals a computational prediction not visible in the standard Koide language.

### Phase 2: The Amplitude Question — Honest Inventory

**Step 2.1.** State ALL equivalent formulations of a² = 2 from PHYS-8 and the planning material. These are restatements, not derivations:
- a² = 2 ↔ Koide ratio = 2/3
- a² = 2 ↔ midpoint of [0, 4]
- a² = 2 ↔ CV(√m) = 1
- a² = 2 ↔ Var(√m) = ⟨√m⟩²
- a² = 2 ↔ one mass can vanish (critical amplitude)
- a² = 2 ↔ midpoint of variance range on the mass simplex

**Step 2.2.** Test the ONE candidate with physics content: equipartition.

If the three masses on the circle have a "kinetic" energy proportional to the variance of √m and a "potential" energy proportional to ⟨√m⟩², then equipartition (kinetic = potential) gives Var = ⟨√m⟩², which is a² = 2.

**The computation:** Define T = Σ_k (√m_k − M)² = M²a² Σ cos²(θ_k) = M²a² × 3/2 (at equal spacing). Define U = N × M² = 3M². Then T = U requires M²a² × 3/2 = 3M², giving a² = 2. 

**The problem:** this is algebraically identical to the CV = 1 statement. Calling it "equipartition" doesn't add physics unless we identify WHAT system has a Hamiltonian H = T + U with T = Var(√m) and U proportional to ⟨√m⟩². This requires a specific Lagrangian for the mass-generating sector. We don't have one.

**Step 2.3.** Honest conclusion on amplitude: No derivation of a² = 2 exists that is independent of the Koide formula itself. Every "derivation" is a restatement. The PHYS-8 honesty applies: we know WHAT the constant is (midpoint, critical amplitude, CV = 1, equipartition) but not WHY it takes that value.

**Gate 2 decision:** The amplitude is NOT derived. Record this honestly. Proceed to Phase 3 to test whether the C₃ SPACING prediction (which IS derived from the frustrated XY ground state) has consequences for quarks, independently of the amplitude question.

### Phase 3: The Quark Koide Computation in Fraction Arithmetic (the real test)

**Step 3.1.** Compute the Koide ratio for all three sectors using DATA-2 full-precision masses:

Charged leptons: K(e, μ, τ) from m_e, m_μ, m_τ
Up-type quarks: K(u, c, t) from m_u, m_c, m_t
Down-type quarks: K(d, s, b) from m_d, m_s, m_b

Use Fraction arithmetic for masses, mpmath for square roots at 50 digits, convert back to Fraction.

**Step 3.2.** For each sector, extract the amplitude a from the measured Koide ratio using a² = 2(NK − 1) where K is the Koide ratio and N = 3.

**Step 3.3.** For each sector, extract the three phases φ_k from the masses. Given √m_k = M(1 + a cos(φ_k)):
- M = (Σ√m_k)/3
- a = √(2 Var(√m_k)) / M  (from the variance formula)
- cos(φ_k) = (√m_k/M − 1)/a
- φ_k = arccos((√m_k/M − 1)/a)

This IS determined — three masses give three phases, once M and a are fixed by the sum and variance. No free parameters.

**Step 3.4.** Compute the phase spacings Δφ₁₂ = φ₁ − φ₂, Δφ₂₃ = φ₂ − φ₃, Δφ₃₁ = φ₃ − φ₁ for each sector.

For leptons: expect Δφ ≈ 2π/3 ≈ 2.094 (equal spacing).
For quarks: expect Δφ ≠ 2π/3 (unequal spacing).

**Step 3.5.** Define the phase perturbation δ_k as the deviation from equal spacing: φ_k = 2πk/3 + δ_k (choosing θ₀ to minimize Σδ_k²).

**Step 3.6.** Compute the "total phase distortion" D = √(Σδ_k²) for each sector. For leptons D ≈ 0 (up to m_τ precision). For quarks D > 0.

**Step 3.7.** Test the correlation: plot D (phase distortion) vs some measure of mixing. For leptons, mixing = 0 (PMNS diagonal in charged sector). For quarks, mixing = some function of CKM angles.

The mixing measure candidates:
- |V_ub|² + |V_cb|² + |V_td|² + |V_ts|² (sum of off-diagonal squared CKM elements)
- sin²θ₁₂ + sin²θ₂₃ + sin²θ₁₃ (sum of mixing angle sines squared)
- The Jarlskog invariant J = Im(V_us V_cb V*_ub V*_cs) ≈ 3.08 × 10⁻⁵

We have three data points (leptons, up-quarks, down-quarks). With three points we can check whether D increases monotonically with mixing but cannot fit a functional relationship.

**Gate 3 decision:** If the ordering is D(leptons) < D(down) < D(up) AND this matches the mixing ordering, the correlation is suggestive. If the ordering doesn't match, the hypothesis is falsified for this specific test. Either way, publish the numbers.

### Phase 4: The Actual New Finding — What C₃ Buys Us

Even without deriving the amplitude, the C₃ spacing gives us one concrete prediction that standard Koide doesn't:

**Prediction:** If the charged lepton mass matrix has an approximate C₃ symmetry (from discrete flavor symmetry), the Koide equal spacing follows from the ground state of the frustrated interaction. Any breaking of C₃ (by mixing) displaces the phases from 120° and changes the Koide ratio away from 2/3. The DIRECTION of displacement (increasing K above 2/3) is predicted: breaking equal spacing while maintaining the constraint Σcos(φ_k) ≈ 0 generically increases the amplitude a above √2, which increases K above 2/3.

**Verify:** compute K for three phases φ_k = 2πk/3 + εδ_k as a function of ε, where δ_k is a fixed perturbation pattern. Show dK/dε > 0 at ε = 0 for generic perturbations. This proves that any departure from equal spacing increases the Koide ratio — which is exactly what the quarks show (K_up = 0.849 > 2/3, K_down = 0.731 > 2/3).

This is a falsifiable prediction: it says quarks should have K > 2/3, never K < 2/3, if the deviation comes from broken C₃. If a quark sector had K < 2/3, the C₃ mechanism would be wrong.

### Phase 5: Write-Up

**If Phase 3 supports the ordering:** PHYS-12 states:
1. The Koide equal spacing is the ground state of the frustrated C₃ interaction (rewriting, not new physics, but connects Koide to established condensed matter)
2. The amplitude a = √2 remains the midpoint/critical value — equivalent to the formula, no independent derivation
3. Quarks deviate from Koide with K > 2/3 for both sectors, consistent with C₃-breaking by CKM mixing
4. The phase distortion correlates with mixing (if it does) or doesn't (if it doesn't) — either way published

**Parameter count:** Still 18 → 17 conditional (same as PHYS-8). The C₃ connection provides a MECHANISM for the spacing but not a derivation of the amplitude. The conditional status is not upgraded.

## Key Differences from Original Plan

1. **Honest about the amplitude.** The original plan had four candidates and implied one might work. This plan says upfront: none of them derive a² = 2 independently of the formula.

2. **Phase extraction is determined.** The original plan had 5 parameters for 3 data points. This plan fixes M and a from the sum and variance, leaving the three phases determined.

3. **Concrete falsifiable prediction.** K > 2/3 for any C₃-broken sector. This is testable with existing data.

4. **Uses Q335 basis.** Every mass enters as a Fraction. √2 enters as the Q335 integer. π/3 computed from the Q335 π numerator.

5. **Gate 2 is hard.** If amplitude isn't derived, we don't pretend otherwise. We proceed with the spacing result only and state the conditional status honestly.

6. **Three data points.** We have exactly three sectors (leptons, up-quarks, down-quarks). We can check ordering but not fit a function. The plan is honest about this limitation.

## Operational Instructions for Executing Claude

1. Start with Phase 0. Load Q335 numerators from the uploaded files. Build all constants as Fraction objects. Assert the 100-digit matches from MATH-4.

2. Phase 1 is algebra verified by script. The C₃ potential stationarity at 120° must be proven by computing gradients and asserting they vanish. The ground state energy must be computed and asserted minimal.

3. Phase 2 ends with an honest null on the amplitude. Document all equivalent formulations. Do not claim a derivation.

4. Phase 3 is the real computation. Every mass from DATA-2. Every square root at 50-digit mpmath precision converted to Fraction. Every Koide ratio, amplitude, and phase spacing computed and reported.

5. Phase 4 computes dK/dε and proves the sign. This is the one new theoretical prediction.

6. Write the paper with every assertion passing. Publish nulls. The spacing mechanism is real (known physics, rewritten). The amplitude is conditional (same as PHYS-8). The quark ordering is data.
