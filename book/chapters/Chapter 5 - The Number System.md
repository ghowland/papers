## Chapter 5: The Number System

Every physics textbook opens with measurements. Length in meters. Mass in kilograms. Time in seconds. The numbers are always decimals: the speed of light is 299,792,458 m/s, the electron mass is 9.109 × 10⁻³¹ kg, the gravitational constant is 6.674 × 10⁻¹¹ N·m²/kg².

These are real numbers — points on the continuous number line. They have served physics brilliantly for four centuries. Newtonian mechanics, Maxwell's electrodynamics, Einstein's relativity, quantum mechanics, the Standard Model — all built with real-number arithmetic. Every prediction, every comparison to experiment, every Nobel Prize earned with decimals.

But real numbers have a fatal limitation. They cannot represent structure.

---

### The Problem with Decimals

The Standard Model has three one-loop beta coefficients:

b₁ = 41/10

b₂ = −19/6

b₃ = −7

In decimal, these are:

b₁ = 4.100000000...

b₂ = −3.166666666...

b₃ = −7.000000000...

Look at the decimals. What do you see? Three numbers. One is 4.1, one is −3.167 (rounded), one is −7. They don't look related. They don't suggest any structure. They're just three points on the number line.

Now look at the Fractions. b₁ = 41/10. The 41 counts U(1) charge contributions: each fermion representation contributes a specific amount based on its hypercharge Y, and the sum over all Standard Model fermions plus the Higgs gives 41 in the numerator. The 10 in the denominator comes from the GUT normalization convention. b₂ = −19/6. The −19 comes from −22 (gauge boson self-interaction, the Yang-Mills term −11/3 times 6) plus +4×6/6 (fermion contributions) plus +1 (Higgs contribution). The 6 in the denominator is 2×3, from the SU(2) normalization. b₃ = −7/1. The −7 comes from −11 (Yang-Mills) plus +4 (fermions). No Higgs contribution because the Higgs is colorless.

Every integer in every numerator and denominator has a meaning. The 41 counts particles. The 19 counts particles minus gauge bosons. The 7 counts particles minus gauge bosons with no Higgs. The 10 is a normalization. The 6 is a normalization. The 1 means no normalization needed.

The decimal 4.1 carries none of this. It's a location on the number line. The Fraction 41/10 carries all of it. The integers 41 and 10 are the physics.

---

### Where Equality Lives

Here is the deepest problem with decimals: they cannot express equality.

The gap ratio in the Standard Model is (b₁ − b₂)/(b₂ − b₃). Compute it:

b₁ − b₂ = 41/10 − (−19/6) = 41/10 + 19/6 = 246/60 + 190/60 = 436/60

b₂ − b₃ = −19/6 − (−7) = −19/6 + 7 = −19/6 + 42/6 = 23/6

Gap ratio = (436/60) / (23/6) = (436/60) × (6/23) = 436/230 = 218/115

Every step is exact. The result 218/115 is exact. It equals 218/115 — not approximately, not to twelve decimal places, exactly. The equality is perfect and provable.

Now do it in decimals:

b₁ − b₂ = 4.1 − (−3.16667) = 7.26667

b₂ − b₃ = −3.16667 − (−7) = 3.83333

Gap ratio = 7.26667 / 3.83333 = 1.89565...

Is this equal to 218/115 = 1.89565217391304347826...? It appears to be. But you can never prove it. The decimal representations are infinite. No matter how many digits you compute, there could be a disagreement at the next digit. In decimals, you can only say "these agree to N digits." In Fractions, you can say "these are equal."

This matters because unification is an equality claim. The claim is not "the three couplings approximately converge." The claim is "the three couplings are readings of one coupling at different soliton boundaries, related by exact integer transformation laws." Approximate convergence can happen by accident. Exact convergence from integer arithmetic cannot.

To test exact convergence, you need exact arithmetic. Real numbers don't have it. Fractions do.

---

### The Gauge Group Is Made of Fractions

The gauge group SU(3) × SU(2) × U(1) is not a collection of real numbers. It's a collection of integers.

The group SU(N) is defined by N — an integer. SU(3) means 3. SU(2) means 2. U(1) means 1. The structure constants of these groups — the numbers that determine how gauge bosons interact with each other — are integers and simple Fractions. The Casimir operators (which determine coupling strengths) are:

C₂(fundamental of SU(2)) = 3/4

C₂(fundamental of SU(3)) = 4/3

C₂(adjoint of SU(2)) = 2

C₂(adjoint of SU(3)) = 3

All Fractions with single-digit numerators and denominators. The Dynkin index S₂ = 1/2 for the fundamental representation of any SU(N). The dimension of the fundamental representation is N. The dimension of the adjoint representation is N² − 1.

These are not measured numbers. They are mathematical facts. 3/4 is not an approximation — it is the exact value of the quadratic Casimir operator for the fundamental representation of SU(2), derivable from the Lie algebra in a few lines. It will never be revised by future experiments. It will never gain or lose a decimal place. It is 3/4.

The entire beta function machinery is built from these Fractions. When we write b₂ = −19/6, every piece traces to exact group theory:

−11/3 × (C₂(adjoint of SU(2))) = −11/3 × 2 = −22/3 (gauge boson contribution)

+4/3 × n_f × S₂(fundamental) = +4/3 × 3 × 1/2 × (number of doublets) = fermion contribution

+1/3 × S₂(fundamental) = +1/3 × 1/2 = 1/6 (Higgs contribution)

Sum them: −22/3 + 4 + 1/6 = −44/6 + 24/6 + 1/6 = −19/6.

Not one step uses a real number. Not one step uses a decimal. The entire computation lives in the Fractions. The answer −19/6 is exact because every input is exact.

Physics is built on a Fraction foundation. The decimal measurements are readings taken from outside the soliton boundaries. The Fraction structure is the interior — the actual machinery of the transformation laws.

---

### What Happens When You Work in Decimals

Here is a true story from the series.

The GUT normalization factor k₁ converts the U(1) hypercharge coupling to the GUT-normalized coupling. Its value is 3/5 — a Fraction, exact, from the embedding of U(1) in SU(5).

The derivation code computed α₁⁻¹(M_Z) = k₁ × cos²θ_W × α_em⁻¹. The correct answer is 63.21. But someone wrote `k1_inv = 5/3` instead of `k1 = 3/5` and then used `k1_inv` where `k1` should have gone. The result: α₁⁻¹(M_Z) = 175.58 instead of 63.21.

In Fraction arithmetic, this is obvious: 5/3 ≠ 3/5. The numerators and denominators are swapped. Any inspection of the Fraction catches the error.

In decimal arithmetic, 5/3 = 1.6667 and 3/5 = 0.6000. These are just two numbers. If you're reading through a long computation and you see 1.6667, you have to remember whether this particular normalization factor should be greater than or less than 1. There's no structural marker — no numerator, no denominator — to flag the inversion.

The consequence of this one inverted Fraction: M_GUT went from 10¹³·⁸ (correct) to 10⁵⁶ (42 orders of magnitude too high). α_s went from 0.0664 (physical) to −1.0 (non-physical). Every two-loop prediction was nonsensical. The bug persisted for weeks through multiple sessions of computation.

It was found when the experiment system ran a diagnostic with automatic comparisons. The comparisons reported M_GUT not in the expected range [10¹³, 10¹⁵]. The diagnostic traced the error to α₁⁻¹(M_Z) = 175.58, which should have been 63.21. The fix was one line: change `k1_inv` to `k1`.

One inverted Fraction. Weeks of wrong results. Found by automatic comparison, not by human inspection of decimal numbers.

This is not an anecdote about carelessness. It's a structural property of decimal arithmetic. Decimals erase the Fraction structure. When the structure is erased, errors that would be obvious in Fractions become invisible in decimals. The 5/3 vs 3/5 error is trivial in Fractions and catastrophic in decimals.

---

### The QED Series in Fractions

The QED perturbation series — the chain that connects the electron's magnetic moment to the fine structure constant — illustrates the integer structure at its finest.

**A₁ = 1/2.** The one-loop Schwinger result (1948). One Feynman diagram. One vertex correction. The answer is the simplest possible Fraction: one-half. Julian Schwinger computed it on a few pages. It is the most famous single calculation in quantum field theory.

**A₂.** The two-loop result. Computed by Petermann in 1957, completed by Sommerfield. Seven Feynman diagrams. The answer is:

A₂ = 197/144 + (1/12)π² − (1/2)π²ln(2) + (3/4)ζ(3)

Four terms. Each term is a rational coefficient (197/144, 1/12, −1/2, 3/4) multiplied by a transcendental constant (1, π², π²ln(2), ζ(3)). The rational coefficients are exact Fractions from Feynman diagram combinatorics. The transcendentals come from the loop integrals.

Look at the rational coefficients: 197/144, 1/12, −1/2, 3/4. The denominators are 144 = 12², 12, 2, 4. They come from the symmetry factors of the Feynman diagrams. The numerators — 197, 1, −1, 3 — count specific combinations of propagators and vertices. Every integer has a diagrammatic origin.

**A₃.** The three-loop result. Computed by Laporta and Remiddi in 1996 from 72 Feynman diagrams. The answer involves rationals, π², π⁴, ζ(3), ζ(5), π²ζ(3), Li₄(1/2), and π²ln(2). Each with an exact rational coefficient. The rational part alone is 28259/5184. The 28259 counts specific diagram topologies. The 5184 = 72² is the square of the number of diagrams.

**A₄.** The four-loop result. Computed by Laporta in 2017 after a decade of effort. 891 Feynman diagrams. The numerical result is A₄ = −1.91225... computed to 4,900 decimal digits. The exact analytical form involves hundreds of transcendental constants — a vast but finite sum of rational coefficients times products of π, ζ(n), Li_n(1/2), and other known constants. Every coefficient is a Fraction. Every transcendental is a known function evaluated at a known point.

**A₅.** The five-loop result. Computed by Volkov in 2019. 12,672 Feynman diagrams. A₅ = 5.891 ± 0.010. The uncertainty is from numerical evaluation of the diagrams, not from unknown physics. The exact analytical form exists in principle but has not been fully reduced.

The pattern: at every loop order, the QED coefficient is a sum of rational Fractions times transcendental constants. The Fractions come from Feynman diagram combinatorics. The transcendentals come from loop integrals. Both are exact. The only approximation enters at four and five loops where the analytical reduction is incomplete and the transcendentals are evaluated numerically.

In our computation, A₁ through A₃ are stored as exact Fraction expressions in Q335 arithmetic. A₄ and A₅ are stored as high-precision decimals (4,900 and 4 digits respectively). The entire series is evaluated in Fraction arithmetic through three loops, then in Q335 decimal arithmetic for the last two loops. The result — α⁻¹ = 137.035999207 — has its precision limited by A₅ (the least precisely known coefficient) and by the hadronic corrections (the least precisely known non-QED contribution), not by arithmetic.

---

### Q335: The Engineering Solution for Transcendentals

π is irrational. It cannot be written as a Fraction. This is a theorem (Lindemann 1882), not an approximation. No ratio of integers equals π. Period.

But physics needs π. It appears in every area formula, every angular integration, every Fourier transform, every coupling constant running. If the goal is Fraction arithmetic, π is a problem.

The solution is Q335. Store π as a Fraction with 335 digits in both numerator and denominator. This Fraction differs from the true π by less than 10⁻³³⁵.

How small is 10⁻³³⁵? The observable universe is about 10²⁶ meters across. The Planck length — the smallest meaningful distance in physics — is about 10⁻³⁵ meters. The ratio is 10⁶¹. Knowing π to 63 digits would let you compute the circumference of the observable universe to Planck-length precision.

Q335 has 335 digits. That's 272 digits beyond Planck precision. It's not just more precise than any measurement could ever require. It's more precise than the concept of measurement could ever require. The difference between Q335-π and true-π is smaller than the ratio of the Planck length to the observable universe raised to the fifth power.

For every physical computation, Q335-π equals π. Not approximately. Operationally. No experiment, no calculation, no theoretical argument could ever distinguish them. The difference is below the noise floor of reality itself.

The same approach works for every transcendental in physics:

ζ(3) = 1.202056903... (appears in A₂, A₃, and throughout QCD)

ζ(5) = 1.036927755... (appears in A₃)

ln(2) = 0.693147180... (appears in A₂, A₃, Li₄)

The Catalan constant G = 0.915965594...

Elliptic integrals K(m) and E(m)

Each is stored as a Q335 Fraction. Each flows through the Fraction arithmetic without rounding, without truncation, without loss of the integer structure in the rational coefficients that multiply them.

The result is a number system that is:

Exact for all rational numbers (Fractions with integer numerators and denominators)

Operationally exact for all transcendentals (Q335 representation, 272 digits beyond Planck)

Structure-preserving (numerators and denominators carry physical meaning at every step)

Self-checking (errors like 5/3 vs 3/5 are visible in the Fraction representation)

This is the number system that makes unification visible. Not because it's philosophically superior to real numbers. Because it preserves the integer structure that real numbers erase, and the integer structure is where the physics lives.

---

### Why Real Numbers Built the Modern World

This chapter could sound like an attack on real numbers. It isn't. Real numbers are humanity's greatest mathematical tool.

Calculus — the foundation of all modern science and engineering — requires real numbers. Limits, derivatives, integrals — all defined on the continuous real line. Newton's mechanics, Maxwell's equations, Einstein's field equations — all formulated in real-number calculus. Quantum mechanics — wave functions are complex-valued functions on real-number spaces.

Real numbers work because physics is continuous. The electromagnetic field doesn't jump from one value to another — it varies smoothly. Particles don't teleport — they move along continuous trajectories (or in quantum mechanics, their probability amplitudes evolve continuously). Spacetime doesn't have gaps — it's a continuous manifold.

For computing trajectories, fields, probabilities, and forces, real numbers are the right tool. Nothing in this book suggests replacing calculus with Fraction arithmetic. The differential equations of physics are real-number equations and they should stay that way.

What Fraction arithmetic replaces is the bookkeeping. The parameters of the Standard Model — the coupling constants, the mixing angles, the beta coefficients — are the bookkeeping layer. They tell you which equation to use and with what values. The beta coefficient b₂ = −19/6 appears as a parameter in the RGE differential equation. The equation itself is real-number calculus. The parameter is a Fraction.

The insight is that the parameters carry integer structure, and working with them as decimals erases that structure. You can solve the RGE with b₂ = −3.16667 and get the right answer (to six-digit precision). Or you can solve it with b₂ = −19/6 and get the right answer (to infinite precision in the parameter), and also know that the 19 counts particles and the 6 counts normalizations, and that changing the particle content changes the 19 by specific integer amounts determined by representation theory.

The real numbers do the calculus. The Fractions do the counting. Both are needed. The error was using real numbers for both.

---

### The Ceiling

Real-number physics has a ceiling. The ceiling is not computational — modern computers handle 64-bit floating point, which gives 15-16 significant digits. The ceiling is structural.

In real-number physics, the three coupling constants at M_Z are three points on the number line: 63.21, 31.69, and 8.47 (the inverse couplings). These three points don't look special. They don't suggest 38/27. They don't suggest (22/13)π. They don't suggest anything — they're just three numbers.

To see the structure, you have to compute the gap ratio as a Fraction and recognize 218/115. Then you have to ask: what BSM representation changes 218/115 to a simpler Fraction? Then you have to enumerate all representations and find that only (3, 2, 1/6) gives 38/27. Then you have to compute the consequences of 38/27 through the entire derivation chain and compare to measurements.

Every step after the first requires Fraction arithmetic. The first step — recognizing that the gap ratio is an interesting number — was done in real numbers by people who happened to notice that the SM couplings "almost" unify. But "almost" in real numbers is a vague statement. In Fractions, it's precise: the gap ratio is 218/115, and it becomes 38/27 with one specific representation.

The ceiling of real numbers is the inability to see this structure. The numbers 1.896 and 1.407 don't look related. The Fractions 218/115 and 38/27 do — they share the same algebraic origin (the gap ratio formula) with different particle content. The structure is in the Fractions. The decimals are the shadow cast on the number line.

Physics hit this ceiling decades ago. The Standard Model was completed in the 1970s. The coupling constants were measured to high precision by the 1990s. The gap ratio was computed and found to be "close to but not exactly" unifying. The conclusion was: the Standard Model doesn't unify, and new physics (SUSY, extra dimensions, etc.) is needed to close the gap.

The correct conclusion was: the Standard Model doesn't unify in decimal arithmetic, and one additional Fraction (the CD's contribution) closes the gap exactly. The difference between these two conclusions is the difference between 40 years of searching for supersymmetric partners that don't exist and one computation in Fraction arithmetic that produces 53 correct predictions.

The wrong number system led to the wrong conclusion. The wrong conclusion led to the wrong search. The wrong search consumed billions of dollars and decades of effort.

Fraction arithmetic costs nothing. It runs on the same computers. It uses the same physics. It just keeps the integers visible.

---

### The Path Through

Here is how the number system works in practice.

**Step 1: Store all gauge group data as Fractions.** Every beta coefficient, every Casimir, every Dynkin index, every representation dimension, every hypercharge. These are all exact Fractions from group theory. Store them with exact integer numerators and denominators. Never convert to decimal.

**Step 2: Store all transcendentals as Q335.** π, ζ(3), ζ(5), ln(2), and every other irrational constant that appears in loop calculations. Store each as a Fraction with 335-digit numerator and denominator. This preserves Fraction arithmetic through every computation involving transcendentals.

**Step 3: Store all measurements as Fractions.** α_em⁻¹ = 137035999177/1000000000. sin²θ_W = 23122/100000. α_s = 59/500. M_Z = 455938/5 MeV. Each measurement, stored as a Fraction with the precision of the measurement in the denominator.

**Step 4: Compute everything in Fraction arithmetic.** The gap ratio, the crossing scale, the coupling predictions, the mass predictions, the spectroscopic predictions. Every intermediate result is a Fraction. Every numerator and denominator carries physical meaning.

**Step 5: Convert to decimal only at the final comparison.** When the derivation chain produces a prediction (say, sin²θ_W = 0.231223) and you want to compare to measurement (0.23122), convert to decimal at that point. Report the miss in ppm or percentage. The miss is the only decimal number in the chain.

This approach preserves all integer structure through the entire computation. The k₁ = 3/5 vs 5/3 error is impossible because you never write 0.6000 or 1.6667 — you write 3/5 or 5/3 and the Fraction is self-documenting. The gap ratio is 38/27, not 1.40741 — and you can see that changing the CD to a different representation would change the 38 and the 27 by specific integer amounts.

The pool — the database of 2,237 value nodes — stores everything this way. Fractions are Fractions. Transcendentals are Q335 Fractions. Measurements are Fractions with measured precision. The derivation functions operate on Fractions and produce Fractions. The experiment comparisons convert to decimal at the last step.

This is why the series can track 53 derived values with full traceability. Every value has a derivation chain. Every chain is made of Fraction operations. Every Fraction carries its integers. The integers carry the physics. Nothing is lost.

---

### What the Reader Should Take Away

You don't need to do Fraction arithmetic yourself. You don't need to memorize 41/10 or 38/27 or the Q335 representation of π. What you need to understand is this:

The universe runs on integers. The gauge group is defined by the integers 3, 2, and 1. The beta coefficients are Fractions whose numerators count particles and whose denominators count normalizations. The transformation laws between soliton boundaries are determined by these Fractions. The readings at each boundary — the coupling constants, the mixing angles, the mass ratios — are determined by running the Fractions through exact arithmetic.

Real numbers are the shadow of this integer structure projected onto the continuous number line. The shadow is useful — it's what we measure, what we compute with, what we compare to experiment. But the structure is in the integers, and you can only see it if you work in Fractions.

The model works — 53 derived values matching measurement across eight domains — because it works in the integers. The integers are the physics. Everything else is a reading.
