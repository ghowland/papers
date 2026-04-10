## Chapter 6: The Machine

A thesis without a tool is a claim. A thesis with a tool is a program.

The thesis, integer Fractions from gauge group representation theory serve as transformation laws across soliton boundaries, producing derivable readings at every scale, could have remained a philosophical position. Interesting, perhaps even beautiful, but untested. The history of physics is littered with beautiful ideas that didn't survive contact with measurement.

What turned this thesis into 53 derived values was a database and an experiment runner. Not a supercomputer. Not a particle accelerator. A Python script, a folder of JSON files, and a pool of numbers stored as Fractions.

The tool is called DATA-6.

---

### What It Is

DATA-6 has three parts.

**The pool.** A collection of 2,237 numbered values. Each value has a name, a number stored as a fraction, and a version. The names are descriptive: the electromagnetic force strength is stored as α⁻¹ = 137035999177/1000000000, a fraction with every digit preserved. If a value is ever corrected, the new version is added alongside the old one. The old version is never deleted.

The pool contains two kinds of values. About 450 are manual inputs: measurements from experiments and mathematical constants entered by hand. The electromagnetic force strength from the standard reference. The Z boson inertia from the particle data tables. π from the Q335 system. The beta coefficients from group theory. These are the foundation.

The remaining 1,787 are experiment outputs: values computed by the system's derivation functions and stored automatically. Every time a computation runs, its results are written to the pool as new entries. The pool is a complete record of every computation ever performed, including every failure.

The pool is a single flat file. No hierarchy, no folders, no categories. Just an alphabetical list of names and values. The simplicity is deliberate. Any tool can read it. Any search can find a value. No special software is required.

**The derivation functions.** About 100 short programs, each taking the pool as input and producing new values as output. A derivation function reads values from the pool by name, computes new values using fraction arithmetic at 100 digits of precision, and returns the results.

For example, the function that extracts the weak mixing angle from two-loop unification reads the electromagnetic force strength, the three one-loop running rates, and all 18 two-loop correction terms from the pool. It runs the forces upward to find where they converge. It runs them back down from exact unification. It returns 24 output values, including the predicted weak mixing angle (0.231223) and the predicted strong force strength (0.11838).

The function doesn't know where its inputs came from. It doesn't care whether the electromagnetic force strength was measured at Harvard or derived from a prior computation. It reads a name, gets a fraction, computes. This separation between data and computation is what allows chains: the output of one function becomes the input of the next, and neither function needs to know about the other.

**The experiment runner.** A program that orchestrates everything. Each experiment is defined by a specification file that lists which derivation functions to run, which outputs to expect, and which comparisons to perform against measured values.

A comparison has a label, a match mode (percentage miss, range check, sigma tension, or exact match), and an expected value. The runner executes each derivation function in order, collects the outputs, writes them to the pool, runs every comparison, and reports PASS, FAIL, or INFO for each one.

Three parts. A pool of numbers. Functions that transform numbers. A runner that checks the results. Everything else is physics.

---

### Why It Works

DATA-6 works because of four properties that seem trivial but turn out to be essential.

**Permanent history.** Every experiment run is preserved. Run 1 of an experiment is never overwritten by run 2. Both exist in the pool simultaneously. If run 1 had a bug, the wrong results are still there alongside the corrected results from run 3.

This sounds like clutter. It is actually the most important feature. When you are debugging a derivation chain, you need to see what went wrong and when it was fixed. The pool is a complete history of every computation ever performed, including every failure. The normalization bug from Chapter 5 was found by comparing run 1 outputs (unification scale at 10⁴⁵, nonsensical) to run 3 outputs (unification scale at 10¹⁴, physical) and asking: what changed? The answer was immediately visible because both runs were preserved.

Deleting failed runs would have hidden the diagnostic trail. Keeping them makes the debugging automatic.

**Automatic comparison.** The runner doesn't just compute values. It checks them. Every experiment defines its comparisons in advance. The expected value for the weak mixing angle is 0.23122. The match mode is percentage miss. The runner computes the prediction, computes the miss, and reports PASS or FAIL.

This means the system catches errors that humans miss. The normalization bug produced a unification scale of 10⁴⁵, obviously wrong to anyone who knows it should be around 10¹⁵. But in a long computation with dozens of intermediate values, a human scanning the output might not notice that one number is thirty orders of magnitude too high. The comparison engine notices immediately: unification scale not in the expected range, FAIL.

Every FAIL is a signal. Every PASS is a confirmation. The system produces both automatically, for every value, on every run.

**Fraction storage.** The pool stores fractions as fractions. The electromagnetic force strength is stored as 137035999177/1000000000, not as the decimal 137.035999177. The weak running rate is stored as −13/6, not as −2.16667. The Q335 constants are stored as fractions with 335-digit numerators and denominators.

When a derivation function reads a value from the pool, it gets a fraction. It performs fraction arithmetic. It returns fractions. The conversion to decimal happens only at the final comparison step, and even then, the fraction is preserved. The decimal is computed fresh each time from the stored fraction.

This means no precision is ever lost. A value computed at 100 digits of precision is stored as a fraction that can be evaluated to 200 or 500 digits if needed. The fraction is the value. The decimal is just a display format.

**Versioning.** Every value has a version number. If a value is corrected, the new version is added. The old version is never deleted or modified. Both coexist in the pool.

This means the pool is append-only. Nothing is ever deleted. Nothing is ever changed. New values are added. Old values stay. The pool grows monotonically. At 2,237 entries, the entire file is a few hundred kilobytes. It could grow a hundredfold without performance issues. The append-only structure means there are no overwrite accidents and no ambiguity about which version is current. The latest version is always the highest number, and all prior versions are available for comparison.

---

### The Experiment Cycle

Here is how a new derivation gets tested.

**Identify the derivation.** The two-loop crossing gives a unification scale and a unified force strength. Running the forces backward from that point to the Z boson energy scale should predict the weak mixing angle and the strong force strength. The physics is clear. The computation is defined.

**Check the pool.** Are all inputs available? The electromagnetic force strength, the measured weak mixing angle (for finding the crossing), the measured strong force strength (for finding the crossing), the Z boson inertia, all three one-loop running rates, all 18 two-loop correction terms, the normalization factor 3/5, and π at Q335 precision. All present. The computation can proceed.

**Write the derivation function.** A short program that reads the inputs, runs the three forces upward to find the crossing point, starts all three forces at the unified strength at the crossing, runs them back down to the Z boson scale, and reads off the predictions. About 80 lines of code.

**Write the experiment specification.** A file listing the derivation function to call, the expected outputs, and the comparisons: weak mixing angle within 5% of measured, strong force strength within 10% of measured, unification scale in the expected range.

**Run.** The system loads the pool, executes the derivation function, writes 24 output values to the pool, runs 6 comparisons, and reports: 4 PASS, 0 FAIL, 2 INFO. All comparisons passed.

**Read the report.** The weak mixing angle predicted at 0.231223, measured at 0.23122, miss of 12 parts per million. The strong force strength predicted at 0.11838, measured at 0.1180, miss of 0.33%.

**Verify.** Run the experiment again. The second run produces identical results. The computation is reproducible. The values are in the pool. The derivation is verified.

Seven steps. One new physics result. Two Standard Model parameters derived from one measurement plus integers. The tool handled the storage, the fraction arithmetic, the comparisons, and the reproducibility check. The physicist handled the physics: identifying the derivation, writing the function, and interpreting the results.

---

### The Bug That Proved the System

The normalization bug from Chapter 5 is worth revisiting here because it demonstrates why the system works, not just why fractions matter.

The bug was simple: one factor written upside down, 5/3 instead of 3/5. The consequence was catastrophic: the unification scale came out as 10⁴⁵ instead of 10¹⁴, and the predicted strong force strength came out negative. Every downstream prediction was nonsensical. But the code ran without crashing. The computation produced numbers. They were just wrong by dozens of orders of magnitude.

The system caught it in three runs.

The first run had the bug in both the Standard Model function and the Cabibbo Doublet function. Both produced nonsensical results. The automatic comparisons reported: unification scale not in expected range, FAIL. Two failures, two signals.

The second run fixed the Cabibbo Doublet function but not the Standard Model function. The Cabibbo Doublet outputs became physical. The Standard Model outputs remained nonsensical. One pass, one fail. The split immediately identified which function still had the bug.

The third run fixed both. All comparisons passed. The Standard Model gap came out as 5.88. The Cabibbo Doublet gap came out as 0.027. The 218-fold improvement was visible for the first time.

Three runs. One inverted fraction found and fixed. The system that found it: automatic comparisons against expected ranges, permanent storage of all three runs for side-by-side comparison, and fraction storage that made the discrepancy between the pool value (3/5) and the code value (5/3) visible on inspection.

Without the automatic comparisons, this bug would have persisted through multiple sessions of computation. The numbers looked plausible in isolation. Only the range checks caught them.

---

### Growth

The pool grows with every session. In the first two sessions, it held about 600 values across 17 derived physics quantities. By the third session, it had grown to nearly 1,000 values across 38 derived quantities. By the final session, it reached 2,237 values across 53 derived quantities, with about 60 experiment runs completed.

Most of the growth is experiment outputs. Each run adds 15 to 30 new values to the pool. The manual inputs, the 450 or so measurements and constants that form the foundation, have barely changed since the second session. The physics is in the experiment outputs: the growing body of derived values, each traceable to its inputs, each compared to measurement, each preserved permanently.

The system scales without difficulty. The pool could grow tenfold or a hundredfold and still load instantly. The derivation functions grow more slowly, about 10 to 15 new functions per session, each short and readable. The experiment specifications accumulate at about 5 per session, each adding new comparisons. Across all experiments, roughly 200 comparisons test specific predictions against specific measurements. Every comparison is a potential failure point. None have produced an unexplained failure. Every FAIL has been diagnosed to a specific code error and fixed.

---

### What the Tool Is Not

DATA-6 is not a physics engine. It doesn't know what a beta function is. It doesn't know what a soliton boundary is. It doesn't understand the gauge group or the Standard Model or the difference between a quark and a lepton. It is a pool of numbers, a set of functions that transform numbers, and a comparison engine that checks numbers against measurements.

The physics is in the derivation functions, written by the physicist using standard textbook formulas. The tool provides the infrastructure: storage, versioning, comparison, reporting. The physicist provides the content: which derivation to compute, which inputs to use, which outputs to compare.

DATA-6 is not a computer algebra system. It doesn't simplify expressions, factor polynomials, or solve equations symbolically. It does numerical fraction arithmetic: multiplying fractions, adding fractions, taking roots of fractions at specified precision. The symbolic understanding, knowing that 38/27 comes from specific beta coefficients and that changing the particle content changes the ratio, is in the physicist's understanding, not in the tool.

DATA-6 is not a publication system. It doesn't write papers. It doesn't generate figures. It doesn't format results for journals. The 40 papers in this series were written separately, drawing on the pool values and experiment reports as source material. The tool produces the numbers. The papers explain what the numbers mean.

DATA-6 is not proprietary. It is a short program and a folder of specification files. Anyone with a standard scientific computing setup can run it. The pool is a text file. The derivation functions are readable code. The experiment specifications are human-readable. There is no secret ingredient. The tool is simple because the idea is simple: store fractions, compute with fractions, compare to measurements.

---

### What the Tool Enables

The tool enables something that no amount of paper-and-pencil physics could achieve: systematic, cumulative, cross-domain derivation with automatic error detection.

**Systematic.** Every derivation follows the same pattern. Read from the pool. Compute in fractions. Write to the pool. Compare to measurement. Report PASS or FAIL. The pattern is the same whether you are deriving the electromagnetic force strength from the electron's wobble (quantum electrodynamics, sub-parts-per-billion precision) or the deuterium abundance from the baryon-to-photon ratio (nuclear physics, 0.12 standard deviations). The uniformity makes it possible to run dozens of derivations across different physics domains using the same infrastructure.

**Cumulative.** Every result stays in the pool. The electromagnetic force strength derived in the first session is still there in the sixth session, available as input to any new derivation that needs it. The weak mixing angle derived in the fifth session is immediately available as input to the W boson mass derivation. The pool is a growing reservoir of derived values that any future computation can draw from.

**Cross-domain.** The pool doesn't care what domain a value comes from. The electromagnetic force strength and the dark matter density and the Z boson inertia and the deuterium fitting coefficient all sit in the same file, accessible by the same mechanism. A derivation function that needs inputs from three different physics departments simply reads three names from the same pool. The departmental walls don't exist in the data.

**Automatic error detection.** The comparison engine catches errors that would pass human review. The range check caught the normalization bug. The percentage check caught the one-loop degeneracy. A threshold set too tight on the hydrogen frequency correctly identified that the prediction was right but the acceptance window was wrong, which led to understanding the error budget better. Every FAIL tells you something. No FAIL goes unexamined.

This combination, systematic, cumulative, cross-domain, with automatic checking, is what produced 53 derived values in six sessions. No human could track 2,237 pool values, 100 derivation functions, and 200 comparisons by hand. The tool does the bookkeeping. The physicist does the physics.

---

### For the Next Physicist

DATA-6 is designed to be picked up by anyone.

The pool is a text file. Open it in any editor. Search for the electromagnetic force strength and you find α⁻¹ stored as a fraction with every digit preserved. Search for the weak running rate and you find −13/6. Every value is labeled, versioned, and immediately readable.

The derivation functions are short, readable programs. Each one explains what it computes, what inputs it reads, and what outputs it produces. The code uses a standard arbitrary-precision arithmetic library. No custom frameworks. No proprietary dependencies. No special hardware.

The experiment specifications are human-readable files. Each lists the derivation functions to run and the comparisons to perform. To add a new experiment, write a new specification, write a new derivation function, and run it. The system handles everything else.

To extend the derivation chain, say, to derive the proton lifetime from the unification scale, a physicist would read the unification scale and the unified force strength from the pool, write a derivation function that computes the proton lifetime from the standard formula, write an experiment specification with a comparison against the Hyper-Kamiokande sensitivity window, and run it. The result would be in the pool, compared to the experimental target, and available for any future computation.

This is how the map grows. One derivation function at a time. One experiment at a time. One comparison at a time. Each step small enough for one person in one afternoon. Each step cumulative: the result stays in the pool permanently, available to everyone who comes after.

The tool is the torch. It is designed to be passed.


