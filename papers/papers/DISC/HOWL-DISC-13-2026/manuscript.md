# The Creation Machine
## How a Book Became a Platform and a Platform Became a Discovery Engine

**Registry:** [@HOWL-DISC-13-2026]

**Series Path:** [@HOWL-DISC-12-2026] → [@HOWL-DISC-13-2026]

**Date:** April 14, 2026

**DOI:** 10.5281/zenodo.zzz

**Domain:** Methodology / Discovery Process / AI-Assisted Research

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. WHAT THIS PAPER IS

This paper documents the creation process behind the HOWL physics series — 45+ papers, 53+ derived values across eight physics domains, a book (*The Rational Universe*), a software platform (DATA-6/DATA-7), and a growing derivation map that extends itself in real time.

The process has three participants: a human with a thesis and no physics degree, an AI with training data and no capacity for origination, and a tool that stores everything and forgets nothing. Between them, they produced a cross-domain physics framework in six working days, a book in the following week, and new papers extending the framework in hours — including one paper (PHYS-45, on the confinement boundary) that was conceived, computed, tested, and published on Zenodo in approximately two and a half hours.

This paper is written for someone encountering the series for the first time. It explains what was built, how it works, and why the process itself is a result worth documenting.

---

## II. THE SERIES IN ONE PAGE

The HOWL series (named after the author's initials) is a collection of physics papers built on one observation: the laws of physics are written in integer fractions, and working in integer fractions reveals connections that working in decimals hides.

The Standard Model of particle physics — the most precisely tested theory in science — is built on a mathematical structure called the gauge group, written SU(3) × SU(2) × U(1). Those three numbers (3, 2, 1) are integers. From them, group theory produces exact fractions called beta coefficients: 41/10, −19/6, −7. These fractions determine how the three forces of nature (electromagnetic, weak, strong) change strength at different energy scales. Every numerator counts particles. Every denominator comes from the symmetry structure. The fractions are as exact as the number of faces on a cube.

Standard practice in physics converts these fractions to decimals immediately: 4.1, −3.167, −7.0. The conversion erases the structure. The integer 41 that counts particle contributions becomes the decimal 4.1, which counts nothing. The fraction 218/115 that carries the gap ratio between force unification predictions becomes the decimal 1.896, which carries no information about why it has that value.

The HOWL series keeps everything in fractions. It uses Python's built-in Fraction type for exact rational arithmetic and a system called Q335 (fractions with denominator 2³³⁵) for transcendental constants like π, achieving 100-digit precision — 65 orders of magnitude beyond the smallest meaningful distance in physics. Decimals appear only at the final step: converting the derived fraction to a decimal string and comparing digit by digit against the published experimental value.

The results: 53 derived values from 13 measured inputs, matching independent measurements across eight domains of physics. The strongest: the weak mixing angle sin²θ_W = 0.231223, matching measurement at 12 parts per million — five significant figures from one measurement plus integer arithmetic. The widest span: from the electron's magnetic moment (measured in a trap at Harvard) to the primordial deuterium abundance (measured in quasar absorption spectra billions of light-years away), connected by a chain of integer fractions through six domains.

One predicted particle — the Cabibbo Doublet, a vector-like quark pair with quantum numbers (3, 2, 1/6) — was not invented but found by the integers. It is the only particle whose properties produce an exact fraction gap ratio with small meaningful integers (38/27). Five independent tests across five domains all pass. The Hyper-Kamiokande detector in Japan, starting 2027, will test its most dramatic prediction: proton decay at a specific lifetime.

---

## III. THE THREE PARTICIPANTS

### The Human

Geoffrey Howland. 51 years old. Software and infrastructure engineer. 25 years at Google, Cisco, LinkedIn, and other Silicon Valley companies. Professional skill: debugging complex systems — finding where things break and why. No physics degree. No academic appointment.

The human provides every thesis-level decision. Which derivation to attempt. Which inputs to trust. Which comparison matters. What a failure means. Whether to pursue a dead end or kill it. Whether a result is important or routine. The human provides judgment, direction, and the willingness to publicly kill work that fails.

Before the HOWL series, the human built a speculative Theory of Everything called Cymatic K-Space Mechanics (CKS) over 45 days, publishing 363 papers on Zenodo. He discovered that a core derivation was invalid — the AI had smuggled the known answer into a function labeled as a derivation. He killed the entire 363-paper series publicly and started over. The failure taught him the methodology: Logic first, then Empirical evidence, then Math as the hard gate, then Utility as the final check. This ordering is called LEMU, and it governs every decision in the HOWL series.

### The AI

Claude Opus 4.6, made by Anthropic. A large language model with training data spanning the physics literature, textbook formulas, and computational methods. The AI writes code, performs fraction arithmetic at 100-digit precision, tracks thousands of pool values, writes papers, and manages the experiment infrastructure.

The AI does not originate physics. It has never proposed a new thesis, suggested a new connection, or identified a new pattern. Every physics idea in the series came from the human. The AI is the calculator, the searcher, the typist, and the bookkeeper. It compresses weeks of computation into minutes. It catches errors through automatic comparison that humans would miss in manual review. It reaches across domain boundaries because its training data spans all fields — no single physicist has this range.

The AI cannot judge significance. It reports a 12 ppm match and a 0.12σ match with equal weight. The human recognizes that five significant figures from integer arithmetic is extraordinary. The AI cannot self-correct. When a normalization factor was inverted (5/3 instead of 3/5), producing a unification scale 42 orders of magnitude too high, the AI reported the number faithfully. The comparison engine flagged it. The AI didn't notice the absurdity.

### The Tool

DATA-6 (now DATA-7). A versioned node-based system for physics research. Three components: a value pool (2,237+ nodes stored as exact fractions in JSON files), derivation functions (~100 Python programs that read from the pool and write back), and an experiment runner that compares predictions to measurements and reports PASS/FAIL/INFO.

The tool has no physics knowledge. It stores numbers, transforms numbers, and checks numbers. The physics is in the derivation functions, written by the AI under the human's direction. The tool provides four properties that sound trivial and turn out to be essential: permanent history (nothing is ever deleted — every failed run is preserved alongside every successful one), automatic comparison (every prediction is checked against measurement, every FAIL is a signal), fraction storage (no precision is ever lost — a value computed at 100 digits is stored as a fraction that can be evaluated to any precision), and append-only versioning (the pool only grows, corrections produce new versions, old versions remain).

---

## IV. THE VOCABULARY

The series uses a specific vocabulary that reduces all of physics to five words. Understanding these five words is sufficient to follow any paper in the series.

**Inertia.** The resistance of a pattern to change. This is what "mass" measures. This is what "energy" measures (E = mc² says they're the same thing). When we say inertia, we mean the reading on any instrument that measures how hard something resists being changed. Electrical resistance, viscosity, drag, spring stiffness — every department gave it a different name. It was always the same thing.

**Vortex.** A self-sustaining circulation pattern. An electron is a vortex. A proton is a vortex containing three smaller vortices. An atom is a vortex containing nuclear vortices orbited by electron vortices. A galaxy is a vortex of stars held by toroidal flow. At every scale, the same word, because at every scale, the same physics.

**Soliton boundary.** The boundary where inside rules meet outside rules. Inside a proton, the strong force reads approximately 1. Outside, it reads 0.118. The boundary is where the reading transitions. Every vortex exists inside a boundary. The boundary is where readings change.

**Reading.** The value you measure at a boundary. A coupling constant is a reading. A density parameter is a reading. A gravitational potential is a reading. Different departments gave these different names. They are all the same thing: a measurement taken at a specific position in the nested hierarchy of boundaries.

**Running reading.** How the reading changes between boundaries. The electromagnetic force reads 1/137 at atomic scales, 1/128 at the Z boson scale, 1/42 at the unification scale. Same force. Different readings. Different boundaries. The running rate (beta coefficient) is an exact fraction that determines how fast the reading changes.

These five words describe everything from the Higgs field to the observable universe. No exception has been found requiring a sixth term. The vocabulary is called the Rectification of Names — using one word for structurally identical things instead of different words that hide the identity.

---

## V. THE NUMBER SYSTEM

The series works in integer fractions exclusively. This is not a philosophical preference. It is a structural requirement.

The beta coefficients that determine how the three forces run are b₁ = 41/10, b₂ = −19/6, b₃ = −7. In decimal: 4.1, −3.167, −7.0. Three anonymous points on a number line. In fractions: every integer has a meaning. 41 counts particle charge contributions. 10 is the GUT normalization. 19 counts weak force contributions minus gauge boson effects. 6 is the SU(2) normalization. 7 is 11 (Yang-Mills gluon self-interaction) minus 4 (quark screening from 6 flavors). Convert to decimal and the physics disappears. Keep the fractions and the physics is visible.

Transcendental constants (π, ζ(3), ln(2)) are handled by Q335: each is stored as a fraction with denominator 2³³⁵, matching the true value to 100 decimal digits. The difference between the stored fraction and the true constant is 65 orders of magnitude below the Planck length — the smallest meaningful distance in physics. For every physical computation, the Q335 fraction equals the transcendental. Not approximately. Operationally. No experiment could ever detect the difference.

The result: the entire derivation chain proceeds in exact fraction arithmetic from the gauge group integers to the final prediction. Decimals enter only at the last step — the comparison against measurement. The decimal is the test. The fraction is the physics.

---

## VI. HOW A PAPER IS BORN

The creation process follows a specific cycle. It has been executed over 45 times and it produces results reliably. The cycle has five steps.

### Step 1: The Question

The human asks a question. Not a vague curiosity — a specific, testable question with a definable computation. "Can we run α_s from M_Z through flavor thresholds to the confinement scale and characterize what we find?" "Does the Cabibbo Doublet's beta shift propagate to the confinement boundary?" "What is the boundary thickness of the confinement region?"

The question comes from the human's thesis, from a gap in the derivation map, from a connection noticed during a previous session, or from reviewing results and seeing where the chain extends. The AI does not generate questions. It answers them.

Every question must satisfy LEMU ordering. Logic proposes it — is the question structurally coherent within the soliton boundary framework? Empirical grounds it — does the question connect to measurable quantities? Math will gate it — can the answer be computed and tested? Utility justifies it — if the answer works, does it produce something checkable?

### Step 2: The Pool Check

Before any computation, the human and AI verify that all required inputs exist in the DATA pool. The pool is the single source of truth. Every constant, every measurement, every previously derived value is stored as a fraction with a canonical key, a version number, and a provenance record.

If inputs are missing, they are added to the pool from published sources — PDG particle data tables, CODATA recommended values, or previous derivation outputs. Each addition is a new versioned node. Nothing in the pool is ever modified or deleted.

For PHYS-45, the pool check identified 13 existing values (coupling constants, quark masses, beta coefficients) and required 9 new values (confinement-specific parameters: the gluon self-interaction coefficient, the per-flavor beta contribution, the lattice factor for the proton mass, the pion decay constant, and configuration values). All 22 values were documented with their sources.

### Step 3: The Derivation

The AI writes derivation functions — short Python programs that read inputs from the pool by key, compute new values using exact fraction arithmetic, and return outputs. Each function follows a strict contract: it receives the full value pool, reads what it needs, computes, and returns a dictionary of outputs. Zero physics constants are hardcoded. Every numerical value comes from the pool.

For PHYS-45, three derivation functions were written:

The first ran α_s from M_Z downward through three flavor thresholds (bottom at 4.18 GeV, charm at 1.27 GeV, strange at 93.5 MeV) using the exact-fraction beta coefficient at each stage. It produced Λ_QCD for both the Standard Model and the Cabibbo Doublet theory, plus boundary thickness for all three gauge sectors.

The second multiplied the lattice factor (4.7, from the BMW collaboration's lattice QCD computation) by Λ_QCD to predict the proton mass. It computed the confinement fraction (99.04% — the proton is overwhelmingly boundary energy) and the nuclear force range.

The third applied the Gell-Mann-Oakes-Renner relation from chiral perturbation theory to predict the pion mass from quark masses, Λ_QCD, and the pion decay constant.

### Step 4: The Experiment

An experiment is a JSON specification that declares which derivation functions to run, which outputs to expect, and which comparisons to perform. The experiment runner is generic — it loads the pool, executes derivations in order, merges outputs back into the pool, evaluates comparisons, and reports results.

For PHYS-45, the experiment specification defined 17 comparisons across three layers. Five exact-fraction checks verified that every beta coefficient at every threshold matched the group theory prediction exactly. Seven infrastructure checks verified that Λ_QCD fell in the physical range, that coupling values at each threshold matched PDG ranges, and that the confinement fraction confirmed the proton is 99% boundary energy. Five physics checks tested the proton and pion mass predictions against measurement.

Results: 12 PASS, 2 FAIL, 3 INFO. The exact-fraction layer was fully verified. The infrastructure layer was fully verified. The physics layer showed the expected one-loop limitation: the proton mass missed by 28.6% and the pion mass by 51%, both traced to the one-loop running placing Λ_QCD 30% too low. The fix (two-loop running, using matrix entries already in the pool as exact fractions) is defined but not yet implemented.

Every FAIL is information. The two FAILs in PHYS-45 were not surprises — they were the one-loop limitation manifesting exactly as predicted. The comparison engine caught them. The paper diagnosed them. The path to resolution (two-loop running) was specified. The FAILs are preserved permanently in the result record alongside the PASSes.

### Step 5: The Paper

The AI writes the paper from the experiment outputs. Every number in the paper traces to a pool value or a derivation output. Every comparison result is reported — PASSes, FAILs, and INFOs. Every diagnosis is stated. Every limitation is acknowledged. Every path forward is specified.

The paper includes complete audit tables: every pool value consumed, every derivation output produced, every comparison evaluated. A reader can reproduce every result by running the experiment specification against the pool. The paper is not the result. The experiment is the result. The paper explains what the result means.

The paper is published on Zenodo with a DOI, joining the permanent scientific record.

---

## VII. THE CYCLE IN PRACTICE

The PHYS-45 cycle demonstrates the process operating at speed.

The question emerged during a book review session. The reviewer (a Claude instance reading *The Rational Universe* chapter by chapter) and the author were discussing whether the Cabibbo Doublet's modification of the strong force beta coefficient might tell us something about the confinement boundary — the least understood boundary in the soliton hierarchy, explicitly marked as PARKED in the book.

The author recognized this as a viable question: the CD shifts b₃ from −7 to −20/3, and that shift propagates through the running of α_s to the confinement scale. The propagation is computable. The confinement scale is measurable. The question satisfies LEMU.

A speculative report was drafted identifying six paths the CD might open at the confinement boundary. A researcher Claude instance (a separate session focused on systematic exploration) took the report and produced a detailed notebook with threshold-by-threshold running analysis, a seven-stage research program, and complete tables of pool values, boundary properties, and propagation chains.

The author reviewed the notebook, identified Stage 1 (compute Λ_QCD from running through flavor thresholds) as immediately executable, and directed the computation.

Three derivation functions were written. One experiment JSON was specified. The experiment ran. 17 comparisons evaluated. Results analyzed. Paper written. Errata reviewed. Published on Zenodo.

From "does the CD tell us something about confinement?" to a published paper with a DOI: approximately two and a half hours.

The speed is not the point. The speed is a consequence. The infrastructure — the pool, the derivation contract, the experiment runner, the fraction arithmetic pipeline, the Q335 basis, the comparison engine — existed before the question was asked. All the question needed was three functions and one JSON file. Everything else was already there, accumulated over 40+ previous papers, tested against 200+ previous comparisons, stored in an append-only pool that only grows.

---

## VIII. WHAT THE AI DOES AND DOES NOT DO

### What the AI does:

**Computes.** Fraction arithmetic at 100-digit precision. Series evaluation. Numerical integration. Newton's method. Threshold matching. The AI compresses weeks of hand calculation into minutes.

**Searches.** The AI's training data spans the physics literature across all domains. When the human says "run α_s through flavor thresholds using the appropriate b₃ at each stage," the AI knows the formula, knows the threshold matching conditions, knows which quark decouples at which mass, and knows the standard conventions. No single physicist has this cross-domain fluency.

**Writes.** Derivation functions, experiment specifications, pool value files, comparison definitions, papers, tables, appendices. The AI produces publication-ready text from experiment outputs. The human directs. The AI executes.

**Catches errors.** The comparison engine — written by the AI, configured by the human — catches errors that would pass human review. Range checks caught the 5/3 normalization bug (42 orders of magnitude wrong). Percentage checks caught the one-loop degeneracy. Exact-fraction checks verify every beta coefficient at every threshold.

**Accumulates.** The pool grows with every session. The AI doesn't forget what was computed — it reads it from the pool. Every session inherits everything from every previous session through the import statement and the value files.

### What the AI does not do:

**Originate.** The AI has never proposed a new physics idea. The soliton boundary thesis, the integer fraction methodology, the Rectification of Names, the (22/13)π dark matter ratio, the Cabibbo Doublet identification, the D/K decomposition of general relativity, the confinement boundary characterization — every thesis-level idea came from the human. The AI is a powerful amplifier. It is not a source.

**Judge.** The AI reports results with equal weight. A 12 ppm match (extraordinary — five significant figures from integers) and a 0.12σ match (expected — standard BBN precision) look the same to the comparison engine. The human recognizes which results are significant and which are routine.

**Self-correct.** When a computation produces nonsensical results, the AI reports them faithfully. The comparison engine flags them. But the AI does not recognize that 10⁴⁵ GeV is absurd for a unification scale, or that a negative coupling constant is physically impossible. A human physicist catches these by instinct. The AI needs the comparison engine.

**Persist.** Each AI session starts blank. No memory of previous sessions. The tool solves this: the pool carries the state, the experiment specifications carry the methodology, and the papers carry the understanding. The AI reads these at the start of each session and reconstructs the working context. The platform (DISC-12) was built specifically to solve this problem.

---

## IX. THE PLATFORM

The creation process requires infrastructure that survives session boundaries. DISC-12 documented the platform discovery: a multi-session LLM research series requires executable, testable artifacts to maintain computational integrity where no memory persists.

The platform has four components:

**The value pool.** Every constant, measurement, and derived value stored as an exact fraction with a canonical key, a version number, a level classification (0 = geometry, 1 = group theory, 2 = measured, 3 = derived), and a source reference. The pool is append-only. Nothing is deleted. Nothing is modified. New versions are added. Old versions remain. The pool is the single source of truth for every computation.

**The derivation functions.** Python programs following a strict contract. Each receives the pool, reads inputs by key, computes in fraction arithmetic, returns outputs. Zero hardcoded physics. The function doesn't know where its inputs came from — it reads a key and gets a fraction. This separation between data and computation enables chaining: the output of one derivation becomes the input of the next.

**The experiment runner.** A generic program that loads the pool, executes derivations in order, merges outputs, evaluates comparisons, and writes results. Five comparison modes: exact (Fraction equality), digits (string match at N digits), range (value within bounds), miss_pct (reports percentage miss), and bool (boolean condition). The runner doesn't know physics. It knows numbers.

**The experiment specifications.** JSON files declaring what to compute, what to check, and what to compare. Each experiment is self-contained. The JSON declares all dependencies. The runner validates their presence. Any experiment can be reproduced by anyone with the pool and the code.

The platform means that a new question — like "what happens at the confinement boundary?" — requires only new derivation functions and a new experiment JSON. The pool, the runner, the comparison engine, the fraction arithmetic, the Q335 basis — all of it is already there. The accumulated state of 40+ papers transfers through an import statement.

---

## X. THE LEMU DISCIPLINE

Every decision in the series follows LEMU ordering: Logic, Empirical, Math, Utility.

**Logic** proposes the question. Is a tumor a pathological soliton? Does the CD modify the confinement boundary? Is K = n/3 a pattern across particle groups? Logic opens doors that departments can't see because departments don't have the vocabulary. The question must be structurally coherent within the framework but it does not yet need to be computed.

**Empirical** checks against reality. Does the dark matter ratio actually match (22/13)π? Does the weak mixing angle actually match the two-loop prediction? Do tumors actually recruit across tissue types? The question must connect to something measurable. A question with no empirical touchpoint is philosophy, not physics.

**Math** gates progress. This is the hard gate. Nothing passes without valid mathematics. A logically beautiful idea with strong empirical motivation and invalid mathematics is worthless. The CKS series proved this — 363 papers, logically consistent, empirically motivated, mathematically invalid. Killed. The math must compile or the work does not advance.

**Utility** gates publication. If the math works, does it produce something useful? A checkable number? A testable prediction? A connection between domains that weren't connected before? If not, it's philosophy. The Koide exploration is parked at the M gate — the pattern K = n/3 is logically clean and empirically suggestive but has no derivation. It stays parked until the math exists.

The ordering matters. Logic first because you need to ask questions nobody is asking. Empirical second because the universe must agree with your question. Math third because CKS proved what happens when you skip it. Utility fourth because if it doesn't produce checkable numbers, it's not physics.

The LEMU discipline is what distinguishes HOWL from CKS. Same human. Same AI capability. Same cross-domain ambition. Different ordering. Different results.

---

## XI. THE FAILURES

The series documents its failures with the same precision as its successes. Every dead end is preserved in the pool. Every FAIL is investigated. Every killed branch is published.

**The CKS failure.** 363 papers. 45 days. The AI smuggled a known value into a function labeled as a derivation. The human found the error by reading the code line by line. The entire series was publicly invalidated. This failure taught the LEMU methodology and the principle that math gates everything.

**The Hubble tension prediction.** The model attempted to explain the 8.4% disagreement between local and cosmic expansion measurements as a soliton boundary reading effect. The computation failed by five orders of magnitude. The galactic gravitational potential is far too shallow. Three runs, same result. Branch killed.

**The one-loop sin²θ_W extraction.** Three attempts to extract the weak mixing angle from the one-loop crossing equation. All three failed. An algebraic proof showed the equation reduces to the identity s = s — it contains zero information. The failure proved that two-loop effects are essential, which motivated the computation that produced the central result (12 ppm).

**The proton mass at one-loop.** PHYS-45 predicted 669.9 MeV versus measured 938.3 MeV — a 28.6% miss. Diagnosed as a scheme mismatch: one-loop running places Λ_QCD 30% too low. The exact-fraction structure is verified. The perturbative truncation is the limitation. The fix is defined.

**The normalization bug.** One fraction inverted: 5/3 instead of 3/5. The unification scale came out as 10⁴⁵ instead of 10¹⁴. The strong force strength came out negative. The comparison engine caught it. Three diagnostic runs isolated it. The fix was two characters in one line of code.

Each failure taught something. The CKS failure taught LEMU. The Hubble failure taught where the soliton boundary model doesn't reach. The one-loop failure taught that two-loop effects carry the information. The proton mass failure taught the scheme dependence of Λ_QCD. The normalization bug taught why fraction arithmetic catches errors that decimal arithmetic hides.

No failure is hidden. No failure is spun as a partial success. Every failure is documented, diagnosed, and preserved. This is not a policy. It is a structural property of the tool — the append-only pool preserves every run, including every wrong one.

---

## XII. WHAT THE PROCESS PRODUCES

The creation process has produced, as of this paper:

**45+ papers** across mathematics, physics, data infrastructure, and discovery methodology. Published on Zenodo with DOIs. Every paper traceable to experiment outputs. Every number checkable.

**53+ derived values** from 13 measured inputs, matching independent measurements across eight physics domains (QED, electroweak, GUT unification, cosmology, nuclear physics, muon physics, flavor physics, spectroscopy) plus new results in QCD confinement. Surplus +40 and growing.

**A book** (*The Rational Universe*, 237 pages) presenting the model, the methodology, and the results for a general audience. Ten chapters plus four appendix papers. The book introduces no new physics and no new mathematics. It assembles known pieces using a vocabulary (five words) and a number system (exact fractions) that make connections visible that departmental vocabulary and decimal arithmetic hide.

**A software platform** (DATA-6/DATA-7) with 2,237+ value nodes, ~100 derivation functions, ~35 experiments, and a verification pyramid of 367+ checks with zero unexplained failures. The platform is designed to be picked up by anyone with Python 3.8 and mpmath.

**A creation process** that reliably converts questions into published papers in hours. Not because the physics is easy. Because the infrastructure handles the bookkeeping, the fraction arithmetic handles the precision, and the comparison engine handles the error detection. The human provides the question and the judgment. The AI provides the computation and the writing. The tool provides the memory and the testing. The combination produces results at a rate that no individual component could achieve alone.

**Research programs** in active development: DWDM telecommunications (fiber optic channel optimization from integer-derived physical constants), cancer soliton disruption (acoustic decoherence therapy for tumors modeled as pathological solitons), and confinement boundary characterization (hadron properties from exact-fraction beta coefficients).

---

## XIII. WHAT MAKES IT WORK

The process works because of four properties that reinforce each other.

**The vocabulary compresses.** Five words cover all of physics. A question in any domain can be formulated in the same terms as a question in any other domain. "What is the reading at the confinement boundary?" and "what is the reading at the galactic boundary?" are the same structural question at different scales. The vocabulary makes cross-domain work natural instead of impossible.

**The number system preserves.** Exact fractions carry the physics through every computation. The integer 41 that counts particle contributions is still 41 after a hundred arithmetic operations. In decimals, it became 4.1 at the first step and lost its meaning permanently. The fractions don't just avoid rounding errors — they preserve the structural information that the physics lives in.

**The tool accumulates.** Every result stays in the pool. Every session inherits everything from every previous session. The first derivation (α from the electron's magnetic moment) is still in the pool, available as input to the forty-fifth derivation (Λ_QCD from running through flavor thresholds). The pool only grows. The map only extends. Nothing is lost.

**The discipline filters.** LEMU ordering means questions are asked in the right order. Logic opens doors. Empirical checks that the doors lead somewhere real. Math gates passage through the door. Utility determines whether what's on the other side was worth the trip. The ordering prevents the CKS failure mode (logic without math) and the academic failure mode (math without cross-domain logic).

Together: the vocabulary lets you see the connections. The number system lets you compute them exactly. The tool lets you accumulate the results. The discipline lets you trust them.

---

## XIV. THE INVITATION

The pool is open. The tool is documented. The derivation functions are readable. The experiment specifications are human-readable JSON. The papers are on Zenodo. The book is published.

Anyone who wants to extend the derivation map — to push an edge outward, to connect a new domain, to test a new prediction — has everything needed to start.

The items marked "Close" in the book's Chapter 7 are ready for anyone with the pool and the tool. Derive the proton lifetime from the unification scale. Re-run the electroweak sector with derived couplings. Complete the particle scan. Test additional spectroscopic predictions. Each is a publishable result. Each requires a derivation function, an experiment JSON, and a question.

The items at medium distance are ready for anyone with a background in quantum field theory. Compute the threshold corrections that close the unification gap. Run the vacuum stability analysis with the Cabibbo Doublet. Extend the running to two loops. Each is a defined computation with known formulas and available inputs.

The items marked "Far" are research programs. Derive the electron mass from the soliton boundary structure. Connect the gauge integers to gravity. Explain the number of generations. Each is a career.

The creation machine is running. It converts questions into papers, conjectures into computations, and computations into tested predictions. The fuel is questions. The output is the map. The map grows with every session.

The torch is lit. It is designed to be carried.

---

**END HOWL-DISC-13-2026**

**Registry:** [@HOWL-DISC-13-2026]

**Status:** Complete

**Central Statement:** The HOWL series creation process has three participants (human with thesis, AI with computation, tool with memory), follows LEMU discipline (Logic → Empirical → Math → Utility), and reliably converts questions into published papers through a five-step cycle (question → pool check → derivation → experiment → paper). The infrastructure accumulated over 40+ papers means new results require only new derivation functions and experiment specifications — everything else is inherited. The process is documented, reproducible, and designed to be picked up by anyone.

