## Chapter 2: Why Nobody Did This Before

Everything in the previous chapter uses known physics.  Everything in this and the coming chapters uses known physics.  This model does not introduce new physics or math, it reorganizes them.

The beta functions are in the textbooks. The QED series coefficients are published. The BBN (Big Bang nucleosynthesis) fitting formulas are standard. The Weinberg relation, the RGE (renormalization group equations), the CKM matrix (Cabibbo-Kobayashi-Maskawa), the Sirlin corrections — all standard. The Bessel functions have been known since 1817. Newton's second law since 1687. Einstein's geodesics since 1915. Solitons since 1834, when John Scott Russell watched a water wave travel two miles down a canal without dispersing and called it "the wave of translation."

Nothing in the derivation chain uses new physics. Not one equation is original. The QED five-loop coefficient A₅ = 5.891 was computed by Volkov in 2019 from Feynman diagrams that Schwinger would have recognized in 1948. The two-loop beta matrix b_ij (the two-loop beta matrix) was computed in the 1980s. The BBN nuclear reaction rates were measured in laboratories in the 1990s. The hydrogen 1S-2S transition was measured to 15 digits in 2011. Every piece was already on the table.

So why didn't anyone assemble them?

Three reasons: the wrong numbers, the wrong names, and the wrong departments.

![53 Derivations Across 8 Domains](../figures/book_13_precision_landscape.png)

---

### The Wrong Numbers

Physics runs on real numbers. Decimal numbers. Floating point. Every measurement is reported as a decimal: the strength of electromagnetism is 0.0072973525693, the weak mixing angle is 0.23122, the gravitational constant is 6.674 × 10⁻¹¹. Every computation uses decimal arithmetic. Every comparison rounds to a certain number of significant figures and reports a percentage miss.

Real numbers built modern physics. They built the Standard Model. They put humans on the Moon and protons through the Large Hadron Collider (LHC). Real numbers work.

But real numbers cannot reach equality. When you compare two decimals, you can say they're close. You can say they match to six digits. But you can never say they're equal — because there's always another digit to check, and you can never check them all.

Take the "gap ratio" — the number that determines whether the three forces (electromagnetic, weak, and strong) converge to a single strength at high energy. You met this ratio in Chapter 1: it comes from dividing one force's running rate against another's, and it tells you whether the three forces meet at a point. In the Standard Model, this ratio is 218/115. With the predicted Cabibbo Doublet, it becomes 38/27. In decimals, these are:

218/115 = 1.89565217391304347826...

38/27 = 1.40740740740740740740...

The decimal representations repeat forever. They never terminate. They're exact as fractions, but as decimals, they're infinite. And infinity is where equality is abandoned.

Here's where it goes wrong. When a physicist computes the gap ratio from measured force strengths, they get something like 1.358192684144844. They compare this to 38/27 = 1.407407... and see a miss of about 3.5%. They note the miss and move on. The miss is larger than the measurement uncertainty, so they conclude the forces don't exactly unify. The standard conclusion in every textbook on grand unification: "the Standard Model gauge couplings do not unify."

But the comparison was done in the wrong number system. The measured number 1.358 is the gap ratio calculated from today's known particles — without the newly predicted Cabibbo Doublet. The predicted number 38/27 is what you get when you include the Cabibbo Doublet in the count. Comparing them directly is like comparing a recipe's predicted cooking time with the actual time when you left out one major ingredient — the numbers won't match because you're not comparing the same thing.

The right comparison is: does the Cabibbo Doublet's ratio (38/27) produce the correct predictions when you work forward from it? Start from 38/27, run the three forces from the unification point back down to laboratory energy, and read off what the weak mixing angle and the strong force strength should be.

That computation gives sin²θ_W = 0.231223. The measured value is 0.23122. They match to 12 parts per million — five significant figures from integer arithmetic.

It gives α_s = 0.11838. The measured value is 0.1180. They match to 0.33%.

These matches are invisible in the decimal representation. You cannot see them by staring at 1.40741 and 1.358. They only appear when you start from the fraction 38/27 — preserving the integers 38 and 27 through every step of the calculation — and derive forward to predictions.

This is the ceiling of decimal arithmetic. In decimals, 38/27 looks the same as 1.407 or 1.4074 or 1.40741. The structure is erased. You can't see that the numerator is 38 = 2 × 19 or that the denominator is 27 = 3³. Those integers have physical meaning — 19 is the weak force beta coefficient from the Standard Model, 3³ is the cube of the number of color charges — but the decimal 1.40741 carries none of that. It's just a location on the number line. The meaning is gone.

Physics missed the integer structure because it was looking at the decimals, and decimals have no structure, and cannot preserve equality.

---

### The Fraction Path

The path to unification starts from integers and works outward.

The three forces of the Standard Model — electromagnetic, weak, and strong — are organized by a mathematical structure called the gauge group. The gauge group is not a theory or a guess. It is the proven symmetry structure of particle interactions, and everything it produces is exact — not measured, not approximated, but calculated from the mathematics of symmetry the way you calculate that a cube has six faces.  Every number the gauge group produces is an integer or a ratio of integers.

The gauge group determines three numbers called "one-loop beta coefficients" — which are the "running rates" of the three forces. The running rate is how fast a force's strength changes as you zoom in — it's the speed of the running reading, and each force has its own.

These running rates are: b₁ = 41/10, b₂ = −19/6, b₃ = −7. They are exact integer fractions. The 41 in b₁ counts the charge contributions of every particle in the Standard Model — each quark, each lepton, the Higgs boson. The 19 in b₂ counts the weak force contributions. The 7 in b₃ counts the strong force contributions. Every numerator is an integer because it counts particles. Every denominator is an integer because it comes from the symmetry structure's normalization. These fractions are as exact as the number 3 — they are consequences of mathematical structure, not measurements.

From these three fractions, you can compute the "gap ratio" — the number that tells you whether the three forces converge. The computation is pure fraction arithmetic: subtract one beta from another, divide by a different subtraction, simplify. Every step is exact. Nothing is rounded. Nothing is approximated. The result for the Standard Model is:

Gap ratio (SM) = 218/115

Two integers. The entire particle content of the Standard Model — every quark, every lepton, every boson — compressed into two numbers.

Now we add the predicted Cabibbo Doublet (CD) particle. Its three small fractional shifts (1/15, 1, 1/3) modify the three betas. The same fraction arithmetic, the same exact steps, produces:

Gap ratio (CD) = 38/27

Two smaller integers. The Standard Model plus one particle, compressed into two numbers. The computation never left the integers. At no point did we convert to decimals, lose precision, round, truncate, or approximate. The fractions flowed from one formula to the next as fractions. The numerators and denominators carried physical meaning at every step — 38 = 2 × 19, where 19 is the Standard Model weak force count; 27 = 3³, the cube of the number of color charges.

This is why unification was missed. The standard approach in physics is: measure the force strengths as decimals, run them as decimals, check if they meet as decimals. They don't meet — because the running accumulates rounding errors, and because the comparison uses floating-point arithmetic, and because the gap is computed as a decimal and compared to zero. The integer structure is 38/27, not 1.40741. That 38/27 integer fraction structure lives below the resolution of the decimal approach. The decimals results can't show it.

The integer fraction approach is different. Start from exact integer betas. Compute the gap ratio as an exact fraction. Identify which new particle produces an exact fraction gap ratio with small, meaningful integers. Derive the predictions from that fraction. Compare to measurement only at the final step — the one place where decimals enter. At that point, the predictions match to 12 parts per million.

The decimals obscure it. The fractions reveal it.

![Fractions show precision or equality that Epsilon and Renormalization obscure](../figures/book_16_fraction_structure.png)

---

### Transcendentals

There's an obvious objection: what about π? What about ζ(3) = 1.202...? These irrational and transcendental numbers appear everywhere in physics — in the QED series coefficients, in the area of a circle, in the dark matter ratio (22/13)π. If the goal is integer arithmetic, how do you handle numbers that aren't integers?

The answer is Q335.

Q335 is the name for a specific representation of transcendental constants as exact rational numbers at 335 decimal digits of precision. The idea is simple. π is transcendental — it cannot be expressed as a ratio of integers. But π can be computed to any desired number of decimal places. At 335 digits, π is known to a precision of 10⁻³³⁵. The Planck length — the smallest meaningful distance in physics — corresponds to a precision of about 10⁻³⁵. So 335 digits is 300 orders of magnitude more precise than any physical measurement could ever require.

The Q335 representation stores π as a Fraction with a numerator and denominator each having about 335 digits. This Fraction is not equal to π — nothing rational is equal to π — but it differs from π by less than 10⁻³³⁵. For every physical computation, this difference is zero. Not approximately zero. Operationally zero. No experiment, no measurement, no observation could ever detect the difference.

The same approach works for every transcendental that appears in physics: ζ(3), ζ(5), ln(2), the Catalan constant, the elliptic integrals. Each is stored as a Q335 Fraction. Each is exact to 300 orders of magnitude beyond Planck precision. Each flows through the Fraction arithmetic without rounding, without truncation, without loss.

The QED two-loop coefficient A₂ is a closed-form expression in rational numbers, π², ln(2), and ζ(3). In decimal, A₂ = −0.3285.... In Q335 Fraction arithmetic, A₂ is:

A₂ = 197/144 + (1/12)π² − (1/2)π²ln(2) + (3/4)ζ(3)

Each term is a product of a rational coefficient (197/144, 1/12, −1/2, 3/4) and a Q335 transcendental (1, π², π²ln(2), ζ(3)). The result is a Q335 Fraction with 335 digits of precision. Exact enough. More than exact enough. Exact enough to verify that the QED series, evaluated in Fraction arithmetic, reproduces the measured electron anomalous magnetic moment to 12 digits when compared to the rubidium recoil measurement of α.

The Q335 approach is not a philosophical statement about whether π is "really" rational. It's an engineering decision. Physics needs numbers with enough precision to test predictions against measurement. 335 digits is enough. The Fraction arithmetic preserves all integer structure through every computation. The transcendentals are handled at operationally infinite precision. The result is a number system where every value is traceable — every numerator and denominator carries physical meaning from the gauge group through the derivation chain to the final prediction.

This is what makes the 12 ppm sin²θ_W prediction possible. The computation starts from integer betas (25/6, −13/6, −20/3), runs through Fraction arithmetic with Q335 transcendentals, and arrives at sin²θ_W = 0.231223 — a number that matches measurement to five significant figures. No rounding error contributed to the miss. No floating-point comparison missed a crossing. The 12 ppm miss is physical — it comes from the 0.027 gap at the unification scale, not from numerical noise.

### Transcendentals

There's an obvious objection: what about π? What about other irrational constants like:

- ζ(3) - a specific number from the Riemann zeta function, approximately 1.202, that appears throughout quantum calculations
- ln(2) - the natural logarithm of 2, approximately 0.693
    
These numbers appear everywhere in physics. They appear in the area of a circle, in the QED series coefficients, in the dark matter ratio (22/13)π. They are transcendental or irrational. They cannot be written as a ratio of integers. If the goal is integer arithmetic, how do you handle numbers that aren't integers?

This is my single innovation in this entire system, and it is not a physics or mathematical innovation, it is an engineering one.  If π and other transcendentals are infinite series, and so cannot be computed into an exact value, what if we make integer fractions so large that they match π and others to 100 decimal digits?

The result is an engineering decision called Q335.  Q335 is 2^335 as the common denominator for all large integer transcendental values.

Starting with the simplest problem: π is transcendental. No ratio of integers equals π. That is a mathematical theorem, proven in 1882, and nothing in this book challenges it. But π can be computed to any desired number of digits. And there is a precision beyond which no physical measurement could ever tell the difference between the true π and a very good fraction.

That precision threshold is set by the Planck length, the smallest meaningful distance in physics, approximately 10⁻³⁵ meters. Knowing π to 35 digits would let you compute the circumference of the observable universe to within one Planck length. 35 decimal digits exhausts all of physical reality.

Q335 uses 335 base-2 digits. That is 65 decimal digits beyond the Planck threshold. The difference between Q335's stored fraction for π and the true π is smaller than anything the universe can distinguish. Not approximately smaller. Fundamentally smaller. No experiment ever built or theoretically possible could detect the difference. This is what "operationally zero" means: the difference exists mathematically but has no physical observable.  This is the single innovation in this model, and it is an engineering innovation to operationalize transcendentals.

The Q335 representation stores π as a fraction with a numerator and denominator each about 101 decimal digits long. This fraction is not equal to π. But it differs from π by less than 10⁻¹⁰⁰. For every physical computation, it is π as far as any physics system can handle the precision of π.

The same approach works for every transcendental and irrational number that appears in physics: ζ(3), ζ(5), ln(2), the Catalan constant, the elliptic integrals. Each is stored as a Q335 fraction. Each is exact to 65 orders of magnitude beyond the Planck threshold. Each flows through the fraction arithmetic without rounding, without truncation, without losing the integer structure of the rational coefficients that multiply them.

Here is what this looks like in practice. The QED two-loop coefficient A₂ (one of the numbers in the chain from the electron's magnetic moment to the fine structure constant) is:

A₂ = 197/144 + (1/12)π² − (1/2)π²ln(2) + (3/4)ζ(3)

Four terms. Each term is a rational coefficient (197/144, 1/12, −1/2, 3/4) multiplied by a transcendental constant (1, π², π²ln(2), ζ(3)). Every rational coefficient is an integer fraction from the physics. Every transcendental is stored at 335 base-2 digits (Q335). The computation never touches a decimal until the final comparison against measurement. The integer structure of the rational coefficients is preserved through every step, and the result is precision matching to the 100th decimal digit for all transcendentals.

The Q335 approach is not a philosophical statement about whether π is "really" rational, π is not rational and cannot be made rational. It is an engineering decision that solves a specific problem: how do you do fraction arithmetic when some of the numbers aren't clear fractions and never end (infinite series)? The answer is that you store them at a precision so far beyond physical measured reality that the distinction between "exact" and "operationally exact at 65 decimal orders of magnitude beyond Planck" has no meaning for physics.

This is what makes the entire derivation chain possible in integer fractions. The computation starts from integer betas (25/6, −13/6, −20/3), runs through fraction arithmetic with Q335 converted transcendentals, and arrives at sin²θ_W = 0.231223, a number that matches measurement to five significant figures. No rounding error contributed to the miss. No floating-point comparison missed a crossing. The 12 parts per million miss is physical. It comes from the 0.027 gap at the unification scale, not from numerical noise. The number system is clean. The miss is real physics, and knowing that it is real physics is itself a result.  This model accepts all results, and uses them for further derivations or places where more precise measurements are required to progress.

---

### The Wrong Names

The second reason nobody unified physics before is language.

Physics has four fundamental forces: electromagnetic, weak nuclear, strong nuclear, and gravitational. This statement appears in every textbook, every popular science book, every university lecture. It's been the organizing principle of physics since the 1970s.

It's wrong. Not factually wrong — the four interactions exist and are different — but organizationally wrong. Calling them "four forces" makes them sound like four separate things. Four mechanisms. Four explanations needed. The goal of unification becomes: find one force that explains the other three. Find a Theory of Everything that contains all four forces as special cases.

But the forces aren't separate things. They're readings of the same thing at different boundaries.

The electromagnetic coupling α reads 1/137 at low energy. It reads 1/128 at the Z boson mass. It reads 1/42 at the GUT scale. These aren't three different forces. They're one coupling that gives different readings at different soliton boundaries — the atomic boundary, the electroweak boundary, the unification boundary.

The strong coupling α_s reads 0.118 at the Z mass. It reads ~1 at the confinement scale (~1 GeV). It reads 1/42 at the GUT scale (the same 1/42 as the electromagnetic coupling — that's what unification means). Again, not two different forces. One coupling, two readings, two boundaries.

The weak mixing angle sin²θ_W — which determines the relative strength of the electromagnetic and weak interactions — is not a separate parameter. It's a reading that follows from the same unification point. At the GUT scale, sin²θ_W = 3/8 exactly. At low energy, it reads 0.231. The running from 3/8 to 0.231 is determined by the same beta coefficients that determine the coupling running. One number, one boundary transition, one derivation.

The names "electromagnetic force" and "weak force" were assigned before the electroweak unification of the 1960s. Weinberg, Salam, and Glashow showed they're the same force, but the names persisted. We still teach them as separate forces in separate chapters. We still fund separate experimental programs to study them. We still assign separate faculty positions for them.

The names "strong force" and "electroweak force" were distinguished before the GUT program of the 1970s. The GUT program showed they could be unified, but the proof was incomplete — the couplings didn't quite meet — so the unification was filed as "promising but unfinished" and the separate names persisted.

The name "gravity" was distinguished from the other three before anyone tried to include it in the gauge framework. General relativity is formulated as geometry (curved spacetime), not as a gauge theory (connections on a fiber bundle). The mathematical frameworks look different, so they got different names, and the different names made people think they needed different unification strategies.

The Rectification of Names says: stop. These are all readings. The electromagnetic reading and the strong reading and the weak reading are all readings of gauge couplings at different soliton boundaries. The gravitational reading is a reading at the planetary/stellar/galactic soliton boundary. They're not four forces. They're one thing — boundary readings of a nested soliton structure — that gives different values depending on which boundary you're reading from.

Once you see them as readings, the unification isn't a grand theoretical achievement to be discovered. It's an accounting exercise to be performed. Which readings come from which boundaries? Which integers determine the running? Which Fractions connect the values at different scales? The answers are in the gauge group, and the gauge group is known.

---

### The Wrong Departments

![Eight Domains](../figures/book_07_eight_domains.png)

The third reason is institutional.

Physics is organized into departments. Particle physics. Nuclear physics. Atomic physics. Condensed matter. Astrophysics. Cosmology. Each department has its own journals, its own conferences, its own language, its own conventions.

The beta functions live in particle physics. The BBN fitting formulas live in cosmology. The hydrogen spectroscopy lives in atomic physics. The Z boson width lives in high-energy experimental physics. The QED series coefficients live in mathematical physics. The CKM matrix lives in flavor physics.

Nobody put them together because they belong to different departments.

The derivation chain in Chapter 1 — from gauge integers to deuterium — crosses five departments: mathematical physics (beta coefficients), particle physics (coupling extraction), cosmology (dark matter ratio, baryon density), nuclear physics (BBN), and observational astronomy (quasar absorption spectra). No single physicist sits in all five departments. No single journal publishes papers spanning all five fields. No single conference program has sessions on QED series coefficients and on primordial deuterium abundance.

The chain from the electron magnetic moment to the hydrogen 1S-2S frequency crosses three departments: experimental particle physics (Penning trap measurements), mathematical physics (QED perturbation theory), and atomic physics (precision spectroscopy). The electron g-2 is measured at Harvard. The QED series is computed at RIKEN. The hydrogen spectroscopy is measured at Garching. Three groups on three continents, each world-class in their field, each unaware that their results are connected by a single derivation chain that produces 0.007 ppb agreement.

They're unaware because the connection crosses departmental lines. The electron g-2 paper cites QED theory papers. The QED theory papers cite mathematical physics papers. The hydrogen spectroscopy papers cite atomic theory papers. But the electron g-2 paper does not cite the hydrogen spectroscopy paper, because they're in different fields. The connection — that the same α extracted from a_e determines R∞ which determines f(1S-2S) — is implicit in the physics but invisible in the citation network.

The dark matter ratio (22/13)π connects gauge theory to cosmology. But gauge theorists don't read cosmology papers about Ω_DM/Ω_b, and cosmologists don't read gauge theory papers about one-loop beta coefficients. The connection has been sitting in the data for decades. The 22 was computed in the 1970s (it's twice the Yang-Mills coefficient). The 13 was implicit in every BSM model that modified b₂. The dark matter ratio was measured by WMAP in 2003 and refined by Planck in 2015. Nobody multiplied (22/13) by π and compared to 5.320 because nobody working on beta coefficients was also working on Ω_DM.

The departmental boundaries are real and they serve a purpose — specialization produces depth. But they also produce blind spots. The blind spot here was that the integer structure of the gauge group connects to the chemical composition of the universe through a chain of standard physics that crosses five department boundaries. Each link in the chain is textbook material in its own department. The chain itself was invisible because nobody had jurisdiction over the whole thing.

![Eight Domains](../figures/book_12_hydrogen_two_path.png)

---

### The Ceiling

![Fig. 14: Unification gap on log scale — CD (0.027) is 218× better than SM (5.88) and 19× better than MSSM (~0.5), with 3 new parameters vs 105.](../figures/book_14_gap_comparison.png)

There's a deeper reason, beneath the wrong numbers and wrong names and wrong departments. It's the assumption that unification requires new physics.

The Grand Unified Theory program of the 1970s established the expectation: to unify the forces, you need new particles, new symmetries, new dynamics at high energy scales. Supersymmetry adds 105 new parameters. String theory adds 10 dimensions. SO(10) adds enormous Higgs representations. The expectation was that unification is hard because the new physics at the GUT scale is complicated and unknown.

What if unification is easy because the new physics at the GUT scale is one particle?

The Cabibbo Doublet — one vector-like quark doublet with quantum numbers (3, 2, 1/6) — shifts the three beta coefficients by (1/15, 1, 1/3). That's three numbers: one-fifteenth, one, and one-third. Three small Fractions. Three exact integers in the numerators. One particle.

With that one particle, the gap ratio becomes 38/27 (exact). The unification scale rises from 10¹³·⁸ to 10¹⁵·⁶ (into the proton decay testability window). The three couplings converge within 0.064% at two-loop. sin²θ_W is predicted to 12 ppm. α_s is predicted to 0.33%. The dark matter ratio is (22/13)π. The deuterium abundance matches at 0.12σ.

53 derived values. 40 surplus tests. One additional particle.

The assumption that unification requires enormous new physics was wrong. The Standard Model was already 99% of the way there. The missing piece was one representation, selected not by theoretical preference but by the integer structure of the gap ratio — the only representation that preserves the gap ratio as an exact Fraction.

Nobody found this before because they were looking for a Theory of Everything. They were looking for new forces, new dimensions, new symmetries. They were looking for the Lagrangian of the universe. What was actually needed was one particle and the willingness to take the integers seriously.

---

### What Changed

What changed was not the physics. What changed was the method.

Instead of starting from a grand theory and working down to predictions, the work started from the integers and worked outward to comparisons. Instead of proposing a Lagrangian, it proposed a representation and tested its consequences across every domain that standard physics could reach.

Instead of working in one department, it crossed all of them. The same derivation chain touched QED, electroweak physics, gauge theory, cosmology, nuclear physics, atomic physics, and precision spectroscopy. Each crossing was a test. Each test could have failed. None did.

Instead of using decimal arithmetic, it used Fraction arithmetic. Every integer in every beta coefficient was preserved through every computation. No rounding errors. No floating-point comparisons. No lost structure.

Instead of working on paper, it used a versioned database of 2,237 value nodes — every Fraction, every measurement, every intermediate result stored, tracked, and testable. The experiment system ran derivation functions against the pool, compared outputs to measurements, and reported PASS or FAIL for every comparison automatically. Bugs were found by the comparisons, not by intuition. The k₁ normalization bug — one inverted factor that made all two-loop predictions wrong for weeks — was found by the experiment system in three diagnostic runs.

The physics was already there. The integers were already there. The measurements were already there. What was missing was the method: start from integers, work in Fractions, cross all departments, test everything against measurement, iterate.

That's what this book describes. Not new physics. New organization. The Rectification of Names applied to the entire Standard Model, producing 53 derived values across eight physics domains from 13 measurements and integer arithmetic.

The universe was always rational. We were just using the wrong number system to see it.
