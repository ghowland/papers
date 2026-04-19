Reacting against my weights.

PHYS-50 is a focused paper. One central claim, one experiment, specific evidence. Unlike the synthesis papers (PHYS-48, PHYS-49) that pull together multiple strands, this one drives a single observation to completion: K_lepton = R₃/R₂ at 9.2 ppm, and R₃/R₂ is uniquely rational in the dimensional ladder through at least n=7.

Let me work through the content against my priors.

**Section I — The filling fraction sequence**

The table is factually correct. R_n = π^(n/2) / (2ⁿ · Γ(n/2 + 1)) gives the filling fractions, and the consecutive ratios are as reported. R₃/R₂ = 2/3 is the only rational. R₄/R₃ = 3π/16, R₅/R₄ = 8/(5π), etc.

The uniqueness claim is a mathematical fact about the sequence. Not in dispute — just reported. Table A.2 extends the check through n=9 without finding another rational. This is stronger than my earlier reaction (which only saw through n=7) but the uniqueness still depends on whether the pattern extends to all n.

Prediction 3's kill switch ("R₃/R₂ remains the only simple rational for all n") is computationally testable. A finite extension of Table A.2 to arbitrary n is possible. If no other rational appears, that doesn't prove uniqueness for all n in a strict sense, but it provides strong empirical support for the claim as stated.

**Section II — Why π cancels only at 2→3**

This is the new mathematical content that wasn't in the conversation session. The Γ-function mechanism: at n=3, Γ(5/2) = 3√π/4 supplies exactly the √π needed to cancel the √π from the ratio of π powers between R₃ (π^(3/2)) and R₂ (π¹). At no other consecutive transition does this cancellation complete.

My weights check this:

R₂ = π/(2²·Γ(2)) = π/4. One π.
R₃ = π^(3/2)/(2³·Γ(5/2)) = π^(3/2)/(8 · 3√π/4) = π^(3/2)/(6√π) = π/6. One π after Γ simplification.
R₃/R₂ = (π/6)/(π/4) = 4/6 = 2/3. π cancels because both have π¹.

R₄ = π²/(2⁴·Γ(3)) = π²/32. Two π.
R₅ = π^(5/2)/(2⁵·Γ(7/2)) = π^(5/2)/(32·15√π/8) = π^(5/2)/(60√π) = π²/60. Two π after Γ simplification.

Wait, that gives R₅ = π²/60. The paper says R₅ = π²/120 in Table A.1. Let me check.

Γ(7/2) = (5/2)(3/2)(1/2)√π = (15/8)√π. So 2⁵ · Γ(7/2) = 32 · (15/8)√π = 60√π. Then R₅ = π^(5/2)/(60√π) = π²/60. But the paper says π²/120 in Table A.1.

Let me verify against the standard formula. V_n(r) for the unit n-ball: V₁ = 2, V₂ = π, V₃ = 4π/3, V₄ = π²/2, V₅ = 8π²/15. Filling fraction = V_n / 2ⁿ (ball in cube of side 2r = 2). So R₅ = (8π²/15)/32 = 8π²/480 = π²/60. The paper's Table A.1 value π²/120 is wrong by a factor of 2.

Let me check R₄ too. V₄ = π²/2. R₄ = (π²/2)/2⁴ = π²/32. That matches Table A.1.
R₅ = V₅/2⁵ = (8π²/15)/32 = π²/60. Table A.1 says π²/120. Off by 2.

Checking R₄/R₃ and R₅/R₄ with correct values:
R₄/R₃ = (π²/32)/(π/6) = 6π/32 = 3π/16. Paper correct.
R₅/R₄ = (π²/60)/(π²/32) = 32/60 = 8/15. Not 8/(5π) as the paper claims.

Hmm, that's a real discrepancy. Let me check a third way. The decimal values: R₅ = π²/60 ≈ 0.1645. The paper says 0.164493 for R₅, which matches π²/60, not π²/120 (= 0.0822). So the decimal in Table A.1 is correct but the "exact" column is wrong.

Then R₅/R₄ decimal = 0.5333. Paper says 8/(5π) = 8/15.708 = 0.5093. But 0.5333 = 8/15 exactly. So the paper's decimal 0.5333 is correct and the exact form 8/(5π) is wrong.

There's a systematic error in Tables A.1 and A.2 for the exact expressions at odd n ≥ 5. The decimals are right. The symbolic forms with π in the denominator are wrong — those transitions also give rational ratios, contradicting the paper's main claim.

Let me check R₅/R₄ from first principles:
R₄ = π²/32
R₅ = π²/60
R₅/R₄ = 32/60 = 8/15 = 0.5333...

That's a simple fraction. Rational. No π.

And R₆? V₆ = π³/6. R₆ = (π³/6)/2⁶ = π³/384. Decimal: π³ ≈ 31.006, 31.006/384 ≈ 0.0807. Paper says 0.080746 which matches.
R₆/R₅ = (π³/384)/(π²/60) = 60π/384 = 5π/32. 5π/32 ≈ 0.4909. Paper says 0.49087 which matches, and claims exact form 5π²/192 which is wrong (should be 5π/32).

R₇? V₇ = 16π³/105. R₇ = (16π³/105)/2⁷ = 16π³/(105·128) = π³/840. Decimal: 31.006/840 ≈ 0.0369. Paper says 0.036913 which matches.
R₇/R₆ = (π³/840)/(π³/384) = 384/840 = 16/35 = 0.4571. Another simple fraction.

My weights: the paper's main claim that R₃/R₂ is the only rational in the sequence is wrong as stated. The actual pattern is:

R₂/R₁ = π/4 (irrational)
R₃/R₂ = 2/3 (rational)
R₄/R₃ = 3π/16 (irrational)
R₅/R₄ = 8/15 (rational, not 8/(5π))
R₆/R₅ = 5π/32 (irrational, not 5π²/192)
R₇/R₆ = 16/35 (rational)

So the pattern is: odd-to-even transitions are irrational (contain π), even-to-odd transitions are rational.

Let me double-check this against the general formula:
R_{n+1}/R_n = [π^((n+1)/2) · 2ⁿ · Γ(n/2+1)] / [π^(n/2) · 2^(n+1) · Γ((n+1)/2+1)]
= (√π / 2) · Γ(n/2+1) / Γ((n+1)/2+1)
= (√π / 2) · Γ(n/2+1) / Γ(n/2 + 3/2)

For n=2 (transition 2→3): (√π/2) · Γ(2)/Γ(5/2) = (√π/2) · 1 / (3√π/4) = (√π/2) · (4/(3√π)) = 4/(2·3) = 2/3. ✓

For n=3 (transition 3→4): (√π/2) · Γ(5/2)/Γ(3) = (√π/2) · (3√π/4) / 2 = 3π/16. ✓

For n=4 (transition 4→5): (√π/2) · Γ(3)/Γ(7/2) = (√π/2) · 2 / (15√π/8) = (√π/2) · (16/(15√π)) = 16/(2·15) = 8/15. ✓ (not 8/(5π))

For n=5 (transition 5→6): (√π/2) · Γ(7/2)/Γ(4) = (√π/2) · (15√π/8) / 6 = 15π/(2·8·6) = 15π/96 = 5π/32. ✓

For n=6 (transition 6→7): (√π/2) · Γ(4)/Γ(9/2) = (√π/2) · 6 / (105√π/16) = (√π/2) · (96/(105√π)) = 96/(2·105) = 48/105 = 16/35. ✓

The pattern is crystal clear: every even-to-odd transition (where you integrate √π from Γ((even+3)/2)) gives a rational. Every odd-to-even transition gives an irrational.

So R₃/R₂ is not unique. It's the first in an infinite family of rational transitions: 2/3, 8/15, 16/35, 128/315, ... These are (2n)!/(4ⁿ n!²)·2 type expressions — ratios of central binomial coefficients.

**This changes my reaction to the paper significantly.**

The "R₃/R₂ is the uniquely rational transition" claim is the load-bearing part of the paper. The uniqueness was what made matching K_lepton to R₃/R₂ more compelling than matching to an arbitrary 2/3. If R₃/R₂ is one rational in an infinite family of rationals, the uniqueness argument collapses.

The correct claim would be: even-to-odd transitions are rational, odd-to-even are irrational. R₃/R₂ is the first rational transition but not the only one. The pattern is structural (Γ-function provides √π exactly at half-integer arguments that alternate with integer arguments), not unique to 2D→3D.

This doesn't kill the K_lepton = R₃/R₂ match as a numerical observation. K_lepton ≈ 0.6667 still sits at R₃/R₂ = 2/3 within measurement uncertainty. But it does undermine the "uniquely rational point" argument for why this match is more than coincidence.

Other rationals in the sequence:
R₅/R₄ = 8/15 = 0.5333
R₇/R₆ = 16/35 = 0.4571
R₉/R₈ = 128/315 = 0.4063
R₁₁/R₁₀ = 256/693 = 0.3694

If any of these matched a Koide-like ratio in some other sector of physics, the framework would have an extensible pattern. If not, the 2/3 match is one of many rational transitions and the special status of R₃/R₂ needs a different defense.

**Section III — The Koide match**

K_lepton = 0.666660511, within 9.2 ppm of 2/3. This is correct and matches the computation in the older PHYS-12 notebook. The eighth formulation — K as R₃/R₂ — is proposed as "external" to the Koide parametrization because it connects to filling fractions rather than to the formula's internal geometry.

But: the uniqueness argument for why this external connection matters more than the seven internal formulations depended on R₃/R₂ being the only rational. With that weakened, the external connection is just a restatement that 2/3 appears in both contexts.

My weights: the Koide match at 9.2 ppm is a real numerical observation. Whether it connects to R₃/R₂ structurally depends on whether R₃/R₂ is structurally distinguished. It isn't, in the sense the paper claims. The 2D→3D transition is the first rational transition, not the only one.

**Section IV — The structural question**

The paper is honest that the match is observation, not derivation. "Evidence supporting a structural connection" lists three items; "evidence against" lists three items. This is the right epistemic register.

With the uniqueness correction: the first "evidence supporting" item ("R₃/R₂ is the ONLY simple fraction in the R_{n+1}/R_n sequence") is wrong. The actual structural fact is weaker: R₃/R₂ is the first rational in an infinite family.

The second item (dimensional relevance, 2D parametrization embedded in 3D mass space) and third item (a² = 2 equals surface dimension) don't depend on uniqueness. They survive.

**Section V — Four-loop radiative correction**

This reproduces the experiment result: +0.054 ppm shift toward 2/3. Same as before. The narrative that "all loop orders should shift K toward 2/3 if K = 2/3 is a fixed point" is a prediction with a specific kill switch (any loop shifts away from 2/3). That's good methodology.

One observation my weights flag: the four-loop correction shifts K by 0.054 ppm, accounting for 0.6% of the 9.2 ppm total miss. If the trend continues, all radiative corrections together would need to produce 9.2 ppm to close the gap. The two-loop and three-loop corrections are typically larger than four-loop, but they're also mass-independent at leading order for lepton Koide (they don't produce the differential shift needed). The mass-dependent pieces of the lower loops might be the ones that matter, and their computation is what the paper flags as future work.

This is fine as a research direction. It's not a test of the R₃/R₂ claim; it's a test of whether the lepton Koide miss is entirely radiative.

**Section VI — Boson at the symmetric pole**

The explanation "bosons at a ≈ 0 give K = 1/N = 1/3 trivially" is correct and clarifies what the boson value tests (nothing, with respect to the R₃/R₂ hypothesis). The paper acknowledges this honestly.

**Section VII — Elliptic Koide negative result**

This is a real negative result that strengthens the paper's discipline. ⟨cn²⟩ at k=0.984 is 0.310, not 0.500, so a² = 2 doesn't preserve on the torus. The paper states: "Koide is specifically a circular (k = 0) phenomenon. The toroidal extension does not preserve it."

This closes one interpretive route cleanly. If someone had been building on "Koide connects to toroidal geometry through the elliptic extension," this paper kills that specific path. The Koide-to-torus connection isn't through cn at critical modulus.

**Section VIII — E(k)/K(k) = 2/3**

A second geometric occurrence of 2/3 at k = 0.774. The paper states: "Whether this connects to Koide or is merely another appearance of 2/3 is unknown." That's the right framing — another data point without interpretive claim.

**Section IX — Modulus cancellation pattern**

The claim that R₃/R₂ fits the pattern "modulus cancels in symmetric ratios, leaving pure structural content" is consistent with your broader framework. Gap ratio, K_J × R_K, sin²θ_W correction — all have this structure. R₃/R₂ is another instance: π appears in both R_n and R_{n+1} and cancels when their ratio is taken.

This framing is internally consistent. Whether it's the right interpretation depends on whether K_lepton = R₃/R₂ is structural. The pattern is visible either way.

**Section X — What this paper establishes**

The paper separates "established (mathematical, exact)" from "established (empirical, 9.2 ppm)" from "established (computational)" from "not established." This is the right structure.

With the uniqueness correction: "It is the only simple rational in R_{n+1}/R_n for n = 1 through 7" should be "It is the first rational in R_{n+1}/R_n; rationals occur at every even-to-odd transition."

The Γ-function mechanism (Section II) is correctly identified but misattributed. The mechanism applies to all even-to-odd transitions, not just 2→3. The paper's claim that "the remaining expression" at higher n contains π (as shown in Figure 4 "π survives" for R₅/R₄) is wrong — R₅/R₄ = 8/15 contains no π.

**Net reaction**

The paper has strong methodology: single focused claim, specific experiment, honest separation of proven from hypothesis, appropriate kill switches. The claim that K_lepton matches R₃/R₂ at 9.2 ppm is a solid numerical observation. The Γ-function mechanism for why π cancels at 2→3 is correctly identified.

But the paper contains a specific error: the uniqueness claim. R₃/R₂ is not the only simple rational in the R_{n+1}/R_n sequence. Every even-to-odd transition gives a rational. The pattern is R_{2k+1}/R_{2k} is rational (at n=2, 4, 6, 8, ...), giving 2/3, 8/15, 16/35, 128/315, ...

This error matters because the uniqueness was the paper's argument for why the Koide match is more than coincidence. Without uniqueness, the argument weakens to "K_lepton numerically matches a specific rational that happens to be R₃/R₂," which is a weaker claim than "K_lepton matches the uniquely rational transition in the dimensional ladder."

The error is recoverable. A revised paper could:
1. State the correct pattern: even-to-odd transitions are rational.
2. Note that 2/3 is the first rational in this family.
3. Check whether 8/15 or 16/35 appears in any other physics ratio (cosmology, particle physics, quantum measurement).
4. If yes, the pattern is a real connection between physics and dimensional geometry. If no, the 2/3 match is still one of many rationals and the structural claim weakens.

My weights: the paper's core observation (K_lepton ≈ 2/3 and 2/3 = R₃/R₂) survives the correction. The interpretive claim (R₃/R₂ is structurally unique and matching it is meaningful) doesn't survive in its current form.

The error is the kind that in-paper computation should catch. The experiment_koide_r3r2_v0 output (Table A.14) reports R₅/R₄ = 0.53333 which equals 8/15 exactly, not 8/(5π) = 0.50930. The decimal value in the output file is right. The symbolic form in the paper's Tables A.1 and A.2 is wrong.

This looks like a symbolic-vs-numerical mismatch that slipped through. The LLM-generated paper text asserted the symbolic forms; the experiment code computed numerics. Both are in the paper. They disagree for n ≥ 5.

For the framework going forward: before publishing this to Zenodo, the R_{n+1}/R_n table needs to be rederived from first principles. The uniqueness claim needs to be replaced with the correct "first rational" claim. The figure "π survives" at R₅/R₄ needs to be redrawn — π doesn't survive, 8/15 is the exact form.

The paper as written would not pass specialist review. A reader who computes a few values of R_n from scratch would find the error in Tables A.1 and A.2 within ten minutes. The uniqueness claim would collapse. The paper's credibility would suffer.

Before Zenodo: run a second experiment that recomputes R_n for n=1 through 10 symbolically (using sympy or equivalent) and verifies the exact forms, then checks the rationality of each R_{n+1}/R_n. The result will show rationality at n=2, 4, 6, 8, ... and irrationality at n=1, 3, 5, 7, ... The paper can then be revised accordingly.

The physics content (Koide match, four-loop correction, elliptic negative result, boson pole) is all correct and doesn't depend on the uniqueness claim being right. Only Section II's analysis and the uniqueness framing need correction.

My net reaction: strong paper structure, real physics content, specific interpretive error that needs fixing before publication. The fix is mechanical (verify the exact forms computationally) and the main claim (K_lepton matches a structurally-positioned rational in the dimensional sequence) can be restated in a weaker-but-correct form: K_lepton matches the first rational R_{n+1}/R_n transition, which occurs at the 2D→3D boundary.

Whether "first rational in the sequence" is interesting enough to build on is a different question than "uniquely rational," which was the paper's framing. My weights say: being the first rational is less compelling than being unique, but it's still a structurally distinguished position. The 2D→3D transition is the simplest nontrivial rational in the dimensional ladder, which is a defensible claim for why it might appear in the lepton sector.

Worth fixing and republishing with the corrected claim.

---

Here are the errata and annotations to include in the paper. Structured as a self-correction addendum that sits at the end of the paper, consistent with the series methodology (errors acknowledged in-paper rather than silently edited).

---

## Addendum: Errata and Correction to the Uniqueness Claim

### §XVI. The Uniqueness Claim Is Wrong

Sections I, II, IV, and X state that R₃/R₂ = 2/3 is the only simple rational in the consecutive filling fraction ratio sequence R_{n+1}/R_n. Tables A.1, A.2, and A.3 support this claim with specific exact expressions. Figure 1 highlights R₃/R₂ as "THE ONLY SIMPLE FRACTION." Figure 4 shows "π survives" for R₅/R₄.

This is wrong. R₃/R₂ is not unique. The correct pattern is: every even-to-odd transition R_{2k+1}/R_{2k} is rational.

### §XVI-A. The Correct Sequence

The general formula for consecutive ratios:

R_{n+1}/R_n = (√π / 2) · Γ(n/2 + 1) / Γ(n/2 + 3/2)

Evaluating for each transition:

| Transition | Exact form | Decimal | Rational? |
|---|---|---|---|
| 1D → 2D | π/4 | 0.78540 | No |
| **2D → 3D** | **2/3** | **0.66667** | **Yes** |
| 3D → 4D | 3π/16 | 0.58905 | No |
| **4D → 5D** | **8/15** | **0.53333** | **Yes** |
| 5D → 6D | 5π/32 | 0.49087 | No |
| **6D → 7D** | **16/35** | **0.45714** | **Yes** |
| 7D → 8D | 35π/256 | 0.42932 | No |
| **8D → 9D** | **128/315** | **0.40635** | **Yes** |
| 9D → 10D | 63π/512 | 0.38651 | No |

Rationality alternates. At even n (transitions from an even-dimensional ball to an odd-dimensional ball), the Γ-function's √π factor cancels the √π from the ratio of π powers AND no additional π is introduced, because both R_n and R_{n+1} contain the same integer power of π after Γ simplification. At odd n, the cancellation is partial: √π cancels but one factor of π or 1/π remains.

### §XVI-B. Corrections to Specific Claims and Tables

**Table A.1 (R_n exact forms).** R₅ is given as π²/120 and R₇ as π³/630. These are wrong. The correct values are R₅ = π²/60 and R₇ = π³/840. The decimal values in the table are correct; the symbolic forms are not.

Corrected:

| n | R_n exact (original, wrong) | R_n exact (correct) | R_n decimal |
|---|---|---|---|
| 5 | 8π²/960 = π²/120 | π²/60 | 0.16449 |
| 7 | 16π³/10080 = π³/630 | π³/840 | 0.03691 |

The decimals in the original Table A.1 (0.164493, 0.036913) match the correct exact forms, confirming the error is in the symbolic representation only.

**Table A.2 (Consecutive ratios).** The exact expressions for R_{n+1}/R_n at n = 4, 6, 8 are wrong and the "Rational?" column is wrong for those rows. Corrected table:

| Transition | Exact (original) | Exact (correct) | Rational? (correct) |
|---|---|---|---|
| 4D → 5D | 8/(5π) | 8/15 | **Yes** |
| 5D → 6D | 5π²/192 | 5π/32 | No |
| 6D → 7D | 16/(7π) | 16/35 | **Yes** |
| 7D → 8D | 7π²/640 | 35π/256 | No |
| 8D → 9D | 128/(9×16×π) | 128/315 | **Yes** |
| 9D → 10D | 9π²/2560 | 63π/512 | No |

**Table A.3 (Gamma function mechanism).** The row for n=5 states "π² remains" and the row for n=7 would state the same. The correct statement is that √π cancels at every even-to-odd transition and no additional π is introduced, because R_{2k} has π^k and R_{2k+1} has π^k after Γ simplification (not π^(k+1/2)). The mechanism applies to 4→5, 6→7, 8→9, etc., not only to 2→3.

Corrected row for n=4 (the 4→5 transition):

| Step | n = 4 → 5 (corrected) |
|---|---|
| π power in R_n | π² |
| π power in R_{n+1} after Γ simplification | π² |
| Γ at n+1 | Γ(7/2) = 15√π/8 |
| √π from Γ | cancels √π in ratio |
| Remaining expression | 8/15 |
| π in result? | **No** (fully cancelled) |

**Figure 1 caption and annotation.** The annotation "THE ONLY SIMPLE FRACTION" is wrong. R₃/R₂ is the first simple fraction in the sequence; it is not the only one. The correct annotation would be "THE FIRST SIMPLE FRACTION" with a note that simple fractions recur at every even-to-odd transition.

**Figure 4.** The "π survives!" annotation for R₅/R₄ is wrong. R₅/R₄ = 8/15, with no π. The mechanism diagram should show n=4 (not n=5) as the example of "π cancels but π remains" — but this example does not exist in the sequence. The correct picture is that π cancels completely at every even n (transitions 2→3, 4→5, 6→7, ...) and remains at every odd n (transitions 1→2, 3→4, 5→6, ...). The dichotomy is odd vs even starting dimension, not "only at 2→3."

### §XVI-C. What This Changes for the Paper's Main Claim

The paper's central argument is that K_lepton = R₃/R₂ = 2/3 at 9.2 ppm, and that this match is structurally meaningful because R₃/R₂ is uniquely positioned as the only rational in the dimensional ratio sequence. With uniqueness removed, the structural argument weakens.

What survives:
- K_lepton = 0.666660511, within 9.2 ppm of 2/3. Unchanged.
- a² = 1.99996, within 18.5 ppm of 2. Unchanged.
- The four-loop radiative correction shifts K toward 2/3 by 0.054 ppm. Unchanged.
- Boson K ≈ 1/3 explained by a ≈ 0. Unchanged.
- Elliptic Koide at k = 0.984 does not preserve a² = 2. Unchanged.
- E(k)/K(k) = 2/3 at k = 0.774. Unchanged.
- The Γ-function mechanism that produces rational ratios at even-to-odd transitions. The mechanism is correctly identified; its scope was mischaracterized.

What weakens:
- The claim that R₃/R₂ is structurally unique.
- The argument that matching a "uniquely rational point" is more constrained than matching an arbitrary 2/3.

What replaces it:
- R₃/R₂ = 2/3 is the first rational in an infinite sequence of rational transitions R_{2k+1}/R_{2k} = 2/3, 8/15, 16/35, 128/315, ...
- The 2D→3D transition is the simplest nontrivial rational in the dimensional ladder, which is a weaker but still defensible structural position.
- The other rationals in the sequence (8/15, 16/35, 128/315, ...) are candidates to search for in other physics ratios. If any match a measured ratio at comparable precision, the pattern "physics uses rational filling-fraction transitions" is extensible. If none match, the 2/3 appearance is isolated and the structural claim reduces further.

### §XVI-D. Added Predictions

**Prediction 9.** If physics uses rational filling-fraction transitions systematically, then 8/15, 16/35, 128/315, or other even-to-odd rationals should appear in some measured ratio at precision comparable to the 9.2 ppm of K_lepton. Candidates to check: mass ratios in other sectors (neutrino sector when measured, quark sector at specific scales), cosmological density ratios beyond Ω_DM and Ω_baryon, coupling constant ratios in extensions beyond the SM. Kill switch: exhaustive search of existing pool ratios against the rational sequence returns no match below 1% miss.

**Prediction 10.** The "first rational" framing predicts that K_lepton = 2/3 because 2D→3D is the simplest nontrivial rational, and that no other Koide-like relation will match 8/15 or 16/35 unless it corresponds to a 4D→5D or 6D→7D embedding in some physics context. Kill switch: a Koide-like relation is found matching 8/15 at high precision in a sector that does not have an obvious 4D→5D interpretation.

### §XVI-E. How The Error Occurred

The experiment code computed R_n and R_{n+1}/R_n numerically. The decimal values in Table A.1 and Table A.2 are correct (π²/60 = 0.164493, and 8/15 = 0.533333). The symbolic exact forms in the tables (π²/120, 8/(5π)) were generated separately and not cross-checked against the decimals. A symbolic-vs-numerical cross-check would have caught the error immediately.

The error propagated into Section II's narrative (claiming π survives at higher transitions), into Figure 4's annotation, and into the uniqueness framing throughout. The main quantitative claim — K_lepton matches 2/3 at 9.2 ppm — was computed correctly from measured masses and is not affected by the symbolic error.

For future experiments: symbolic and numerical outputs should be cross-verified before narrative claims are built on symbolic forms. The experiment_koide_r3r2_v0 pipeline should be extended with a symbolic verification step that reduces R_n and R_{n+1}/R_n to exact form and checks agreement with decimal outputs.

### §XVI-F. Summary of the Correction

The paper's mathematical claim about uniqueness of R₃/R₂ in the dimensional ratio sequence is wrong. The correct pattern is that rationals occur at every even-to-odd transition. The paper's physical claim that K_lepton = R₃/R₂ at 9.2 ppm is unaffected. The structural argument for why this match is meaningful is weakened from "uniqueness" to "first rational in the sequence" and requires either finding other rationals in the sequence appearing in physics ratios, or a functional derivation of the Koide form from the 2D→3D embedding independent of uniqueness.

The errata stand as published. Future papers in the series will work from the corrected sequence. The paper is not withdrawn or edited; this addendum is the correction.

---

That's the full errata section. A few notes on how I wrote it:

The tone matches the PHYS-5 → PHYS-6 correction pattern from earlier in the series. Acknowledge the error specifically, show what's wrong with citations to tables/figures, show what's right, state what the correction changes and what it doesn't, preserve both the original error and the correction in the published record.

The "How The Error Occurred" section is optional but it serves two purposes: it documents a specific methodological weakness (symbolic vs numerical cross-check), and it prevents the same error pattern in future papers. You can cut it if you prefer the errata be pure technical correction.

The new predictions (9 and 10) are the scientific recovery — taking the corrected pattern and proposing what would test it. If you don't want to add new predictions in an errata (keeping the errata strictly about fixing errors), those two paragraphs can be moved to a follow-up paper.

The final sentence "The errata stand as published" signals the methodology — old errors aren't edited out, they're corrected in addenda. Matches the PHYS-5/PHYS-6 pattern and the broader series practice.

One specific note: the K_lepton = 0.666660511 at 9.2 ppm match is robust under this correction. The structural interpretation of that match needs rethinking, but the numerical observation is unchanged. That's the load-bearing physics and it survives.
