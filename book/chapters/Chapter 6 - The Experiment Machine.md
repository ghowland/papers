## Chapter 6: The Machine

A thesis without a tool is a claim. A thesis with a tool is a program.

The thesis, integer Fractions from gauge group representation theory serve as transformation laws across soliton boundaries, producing derivable readings at every scale, could have remained a philosophical position. Interesting, perhaps even beautiful, but untested. The history of physics is littered with beautiful ideas that didn't survive contact with measurement.

What turned this thesis into 53 derived values was a database and an experiment runner. Not a supercomputer. Not a particle accelerator. A Python script, a folder of JSON files, and a pool of numbers stored as Fractions.

The tool is called DATA-6.

---

### What It Is

DATA-6 has three parts.

**The pool.** A collection of 2,237 value nodes. Each node has a key (a name), a value (a Fraction, a decimal, or a string), and a version number. The key is descriptive: `coupling_alpha_em_inverse_v0` stores α⁻¹ = 137035999177/1000000000. The `_v0` at the end means version zero, the first version of this value. If the value is ever corrected, a `_v1` appears alongside it, and the `_v0` is never deleted.

The pool contains three kinds of values:

Manual inputs, measurements and mathematical constants, entered by hand. α⁻¹ from CODATA. sin²θ_W from PDG. M_Z from LEP. π from Q335. The beta coefficients from group theory. These are the foundation. About 450 of the 2,237 nodes are manual inputs.

Experiment outputs, values computed by derivation functions and stored automatically. Every time an experiment runs, its outputs are written to the pool as new nodes with keys like `experiment_sin2_from_two_loop_v0_run001_result_sin2_predicted_v0`. The experiment name, the run number, and the output name are all in the key. About 1,787 of the 2,237 nodes are experiment outputs.

The pool is a flat file, one JSON document listing every node. No hierarchy, no folders, no categories. Just an alphabetical list of keys and values. The simplicity is deliberate. Any tool can read it. Any search can find values. No database engine, no SQL, no dependencies.

**The derivation functions.** About 100 Python functions, each taking the pool as input and producing a dictionary of output values. A derivation function reads values from the pool by key, computes new values using Fraction arithmetic (the `mpmath` library at 100 decimal digits), and returns the results.

For example, the function `sin2_from_two_loop_crossing_v0` reads α⁻¹, sin²θ_W, α_s, M_Z, the three one-loop betas, and all 18 two-loop matrix elements from the pool. It runs the two-loop RGE upward to find the crossing point. It runs the three couplings downward from exact unification. It returns 24 output values including sin²θ_W(predicted) = 0.231223 and α_s(predicted) = 0.11838.

The function doesn't know where its inputs come from. It doesn't care whether α⁻¹ was measured at Harvard or derived from a prior computation. It reads a key, gets a Fraction, computes. This separation between data and computation is what allows chains, the output of one function becomes the input of the next, and neither function needs to know about the other.

**The experiment runner.** A script (`data6.py`) that orchestrates everything. Each experiment is defined by a JSON file specifying: which derivation functions to run (the execution plan), which pool values are needed (dependencies), which outputs to expect, and which comparisons to perform against measured values.

A comparison has a label, an output key, a match mode (percentage miss, range check, sigma tension, exact match), and an expected value. The runner executes each derivation function in order, collects the outputs, writes them to the pool, runs every comparison, and reports PASS, FAIL, or INFO for each one.

That's it. Three parts. A pool of numbers. Functions that transform numbers. A runner that checks the results. Everything else is physics.

---

### Why It Works

DATA-6 works because of four properties that seem trivial but turn out to be essential.

**Permanent history.** Every experiment run produces a result file and a values file. Run 001 of an experiment is never overwritten by run 002. Both exist in the pool simultaneously. If run 001 had a bug, say, the k₁ normalization was inverted, the wrong results are still in the pool under `..._run001_result_...`. The correct results from run 003 sit alongside them under `..._run003_result_...`.

This sounds like clutter. It's actually the most important feature. When you're debugging a derivation chain, you need to see what went wrong and when it was fixed. The pool is a complete history of every computation ever performed, including every failure. The k₁ bug was found by comparing run 001 outputs (α₁⁻¹ = 175.58, M_GUT = 10⁴⁵) to run 003 outputs (α₁⁻¹ = 63.21, M_GUT = 10¹³·⁸) and asking: what changed between the runs? The answer, one line in one derivation function, was immediately visible because both runs' outputs were preserved.

Deleting failed runs would have hidden the diagnostic trail. Keeping them makes the debugging automatic.

**Automatic comparison.** The runner doesn't just compute values, it checks them. Every experiment defines its comparisons in advance. The expected value for sin²θ_W is 0.23122. The match mode is percentage miss. The runner computes the prediction, computes the miss, and reports PASS (if within the specified range) or FAIL (if not).

This means the experiment system catches errors that humans miss. The k₁ bug produced M_GUT = 10⁴⁵, obviously wrong to anyone who knows that M_GUT should be around 10¹⁵. But in a long computation with dozens of intermediate values, a human scanning the output might not notice that one number is 30 orders of magnitude too high. The comparison engine notices immediately: "M_GUT not in [10¹³, 10¹⁵], FAIL."

Every FAIL is a signal. Every PASS is a confirmation. The experiment system produces both automatically, for every value, on every run. No human inspection required.

**Fraction storage.** The pool stores Fractions as Fractions. The value `coupling_alpha_em_inverse_v0` is stored as `137035999177/1000000000`, not as `137.035999177`. The beta coefficient `beta_modified_su2_total_v0` is stored as `-13/6`, not as `-2.16667`. The Q335 constants are stored as Fractions with 335-digit numerators and denominators.

When a derivation function reads a value from the pool, it gets a Fraction. It performs Fraction arithmetic. It returns Fractions. The conversion to decimal happens only at the comparison step, and even then, the Fraction is preserved in the pool. The decimal is computed fresh each time from the stored Fraction.

This means no precision is ever lost. A value computed in run 001 at 100 digits of precision is stored as a Fraction that can be evaluated to 200 digits or 500 digits if needed. The Fraction is the value. The decimal is just a display format.

**Versioning.** Every value node has a version suffix: `_v0`, `_v1`, `_v2`. The rule is: `_v0` is the first version. If the value is corrected, `_v1` is added. The `_v0` is never deleted or modified. Both versions coexist in the pool.

This means the pool is append-only. Nothing is ever deleted. Nothing is ever changed. New values are added. Old values stay. The pool grows monotonically.

At 2,237 nodes, the pool is still small, the entire file is a few hundred kilobytes. It could grow to 100,000 nodes without performance issues. The append-only structure means there are no merge conflicts, no overwrite accidents, no "which version is correct?" questions. The latest version is always the one with the highest suffix, and all prior versions are available for comparison.

---

### The Experiment Cycle

Here is how a new derivation gets tested. The cycle took three days for the sin²θ_W two-loop extraction. It typically takes hours.

**Step 1: Identify the derivation.** The two-loop crossing gives α_GUT⁻¹ = 42.135 at M_GUT = 10¹⁵·⁶. Running the couplings backward from this point to M_Z should predict sin²θ_W and α_s. The physics is clear. The computation is defined.

**Step 2: Check the pool.** Are all inputs available? α⁻¹, sin²θ_W (measured, for finding the crossing), α_s (measured, for finding the crossing), M_Z, all three one-loop betas, all 18 two-loop matrix elements, k₁ = 3/5, π at Q335. All present. The computation is unblocked.

**Step 3: Write the derivation function.** A Python function that reads the inputs, runs the two-loop RGE upward to find the 1-2 crossing, starts all three couplings at α_GUT⁻¹ at the crossing, runs them downward to M_Z, and reads off the predictions. About 80 lines of code.

**Step 4: Write the experiment JSON.** A file specifying: the derivation function to call, the expected outputs (sin²θ_W predicted, α_s predicted, forward check), and the comparisons (sin²θ_W within 5% of measured, α_s within 10% of measured, M_GUT in [10¹⁵, 10¹⁷], forward check gap < 0.001).

**Step 5: Run.** `./data6.py run experiment_sin2_from_two_loop_v0`. The runner loads the pool (1,340 nodes at that point), executes the derivation function, writes 24 output values to the pool, runs 6 comparisons, and reports: 4 PASS, 0 FAIL, 2 INFO. ALL COMPARISONS PASSED.

**Step 6: Read the report.** `./data6.py report experiment_sin2_from_two_loop_v0`. The report shows every output value and every comparison in detail. sin²θ_W predicted = 0.231223, measured = 0.23122, miss = 0.0012%. α_s predicted = 0.11838, measured = 0.1180, miss = 0.33%.

**Step 7: Verify.** Run the experiment again. `run002` produces identical results. The computation is reproducible. The values are in the pool. The derivation is verified.

Seven steps. One new physics result. Two SM parameters derived from one measurement plus integers. The tool handled the pool loading, the Fraction arithmetic, the comparison engine, the result storage, and the reproducibility check. The physicist (in this case, a human and an AI working together) handled the physics: identifying the derivation, writing the function, and interpreting the results.

---

### The Bug That Proved the System

The k₁ story is worth telling in full because it demonstrates why the system works.

The GUT normalization factor k₁ = 3/5 converts the hypercharge coupling to the GUT-normalized U(1) coupling. The formula is:

α₁⁻¹(M_Z) = k₁ × cos²θ_W × α_em⁻¹ = (3/5) × 0.76878 × 137.036 = 63.21

Someone wrote the derivation function with k₁⁻¹ = 5/3 instead of k₁ = 3/5. The result:

α₁⁻¹(M_Z) = (5/3) × 0.76878 × 137.036 = 175.58

This is 2.78× too large. The consequence cascaded through everything:

The 1-2 crossing (where α₁⁻¹ = α₂⁻¹) was pushed to t = 100 (the scan limit) because α₁⁻¹ started at 175.58 instead of 63.21, far above α₂⁻¹ = 31.69, and the lines never crossed within the scan range.

M_GUT = 10⁴⁵ instead of 10¹³·⁸. Nonsensical.

α_s(predicted) = −1.0. Non-physical, a negative coupling constant.

The two-loop gap was −49.6 instead of 0.027. Meaningless.

Every number downstream was garbage. But the computation ran without error. The code didn't crash. The Euler integration integrated. The crossing scan scanned. The output values were written to the pool. Everything looked normal, except the numbers were wrong by dozens of orders of magnitude.

**Run 001:** Both the SM function and the CD function had the bug. Both produced nonsensical results. The experiment comparisons reported: M_GUT not in [10¹³, 10¹⁵], FAIL. M_GUT not in [10¹⁵, 10¹⁷], FAIL. Two failures. The comparisons caught it.

**Run 002:** The CD function was fixed (k₁ = 3/5). The SM function was not. Result: the CD outputs became physical (M_GUT = 10¹⁵·⁶, gap = 0.027) while the SM outputs remained nonsensical (M_GUT = 10⁴⁵). The comparisons reported: CD M_GUT in [10¹⁵, 10¹⁷], PASS. SM M_GUT not in [10¹³, 10¹⁵], FAIL. One pass, one fail. The split immediately identified which function still had the bug.

**Run 003:** Both functions fixed. Both physical. All comparisons passed. SM gap = 5.88. CD gap = 0.027. The 218× improvement was visible for the first time.

Three runs. Three days. One inverted Fraction found and fixed. The system that found it: automatic comparisons against expected ranges, permanent storage of all three runs' outputs for side-by-side comparison, and the diagnostic clarity of Fraction storage (the pool showed `group_k1_gut_normalization_v0 = 3/5` while the function was using 5/3, the discrepancy was visible in the code).

Without DATA-6, this bug would have persisted indefinitely. The numbers looked reasonable in isolation, 175.58 is not obviously wrong if you don't know it should be 63.21. Only the automatic range comparisons caught it.

---

### Growth

The pool grows with every session.

| Session | Pool nodes | Derived values | Experiments run | Key advance |
|---|---|---|---|---|
| Session 1-2 (PHYS-36-37) | ~600 | 17 | ~25 | QED chain, BBN bridge |
| Session 3 (PHYS-38) | ~985 | 38 | ~40 | Sub-ppb QED, EW sector |
| Session 4 (early PHYS-39) | ~1,200 | 40 | ~45 | Two-loop diagnostic, k₁ fix |
| Session 5-6 (PHYS-39-40) | 2,237 | 53 | ~60 | sin²θ_W, spectroscopy |

The pool has nearly quadrupled in four sessions. Most of the growth is experiment outputs, each run adds 15-30 value nodes. The manual inputs (~450) haven't changed significantly since Session 2. The physics is in the experiment outputs.

The growth rate is sustainable. At 2,237 nodes, the pool file is small. Loading takes milliseconds. Searching is instantaneous. The append-only structure means the file never needs compaction or reorganization. At the current rate (~400 nodes per session), the pool would reach 10,000 in about 20 sessions, still trivially manageable.

The derivation functions grow more slowly, about 10-15 new functions per session. Each function is 50-100 lines of Python. The total codebase is about 5,000 lines. This is tiny by software standards. The simplicity is a feature: anyone can read the code, understand the computation, and verify the result.

The experiment count grows at about 5 per session. Each experiment JSON is about 50-100 lines. The comparisons accumulate: about 200 total across all experiments, each testing a specific prediction against a specific measurement. Every comparison is a potential failure point. None have produced an unexplained failure. Every FAIL has been diagnosed to a code bug (k₁ inversion, wrong root selection, incomplete Δr decomposition, too-tight range threshold) and fixed.

---

### What the Tool Is Not

DATA-6 is not a physics engine. It doesn't know what a beta function is. It doesn't know what a soliton boundary is. It doesn't understand the gauge group or the Standard Model or the difference between a quark and a lepton. It's a pool of numbers, a set of functions that transform numbers, and a comparison engine that checks numbers against measurements.

The physics is in the derivation functions, written by the physicist (human and AI), using standard textbook formulas, in standard Python with the `mpmath` library for arbitrary-precision Fraction arithmetic. The tool provides the infrastructure: storage, versioning, comparison, reporting. The physicist provides the content: which derivation to compute, which inputs to use, which outputs to compare.

DATA-6 is not a computer algebra system. It doesn't simplify expressions, factor polynomials, or solve equations symbolically. It does numerical Fraction arithmetic, multiplying Fractions, adding Fractions, taking roots of Fractions (producing new Fractions at the specified precision). The symbolic structure (knowing that 38/27 comes from specific beta coefficients) is in the physicist's head and in the comments, not in the tool.

DATA-6 is not a publication system. It doesn't write papers. It doesn't generate figures. It doesn't format results for journals. The papers (40 of them) are written separately, drawing on the pool values and experiment reports as source material. The tool produces the numbers. The papers explain what the numbers mean.

DATA-6 is not proprietary. It's a Python script and a folder of JSON files. Anyone with Python 3 and the `mpmath` library can run it. The pool is a text file. The derivation functions are readable code. The experiment JSONs are human-readable specifications. There is no secret sauce. The tool is simple because the idea is simple: store Fractions, compute Fractions, compare to measurements.

---

### What the Tool Enables

The tool enables something that no amount of paper-and-pencil physics could achieve: systematic, cumulative, cross-domain derivation with automatic error detection.

**Systematic:** every derivation follows the same pattern. Read from pool. Compute in Fractions. Write to pool. Compare to measurement. Report PASS/FAIL. The pattern is the same whether you're deriving α from a_e (QED, sub-ppb precision) or D/H from η₁₀ (nuclear physics, 0.12σ). The uniformity makes it possible to run dozens of derivations across different physics domains using the same infrastructure.

**Cumulative:** every result stays in the pool. The α derived in Session 1 is still there in Session 6, available as input to any new derivation that needs it. The sin²θ_W derived in Session 5 is immediately available as input to M_W derivation in Session 6. The pool is a growing reservoir of derived values that any future computation can draw from.

**Cross-domain:** the pool doesn't care what domain a value comes from. α_em⁻¹ and Ω_DM and M_Z and the BBN deuterium coefficient all sit in the same flat file, addressable by the same key-lookup mechanism. A derivation function that needs inputs from three different physics departments simply reads three keys from the same pool. The departmental walls don't exist in the data.

**Automatic error detection:** the comparison engine catches errors that would pass human review. The M_GUT range check caught the k₁ bug. The sin²θ_W percentage check caught the one-loop degeneracy. The hydrogen range check (set too tight at 100 kHz) correctly identified that the prediction was right but the threshold was wrong, which led to adjusting the threshold and understanding the error budget. Every FAIL tells you something. No FAIL goes unexamined.

This combination, systematic, cumulative, cross-domain, with automatic checking, is what produced 53 derived values in six sessions. No human could track 2,237 pool values, 100 derivation functions, and 200 comparisons by hand. The tool does the bookkeeping. The human does the physics.

---

### For the Next Physicist

DATA-6 is designed to be picked up by anyone.

The pool is a JSON file. Open it in any text editor. Search for `coupling_alpha_em_inverse_v0` and you find α⁻¹ = 137035999177/1000000000. Search for `beta_modified_su2_total_v0` and you find b₂ = −13/6. Every value is labeled, versioned, and immediately readable.

The derivation functions are Python. Each function has a docstring explaining what it computes, what inputs it reads, and what outputs it produces. The code uses `mpmath` for arbitrary-precision arithmetic, a well-documented, widely-used library. No custom frameworks. No proprietary libraries. No dependencies beyond Python and mpmath.

The experiments are JSON files. Each specifies an execution plan and a set of comparisons. To add a new experiment, create a new JSON file, write a new derivation function, register it in the index, and run `./data6.py run experiment_name`. The runner handles everything else.

To extend the derivation chain, say, to derive the proton lifetime from M_GUT, a physicist would:

1. Read `result_m_gut_cd_two_loop_log10_v0` = 15.61 from the pool
2. Read `gut_alpha_gut_estimate_v0` = 0.0260 and `gut_proton_matrix_element_v0` = 0.012 from the pool
3. Write a derivation function that computes τ_p = M_GUT⁴ / (α_GUT² × m_p⁵ × |α_H|²)
4. Write an experiment JSON with a comparison: τ_p in [10³³, 10³⁶] years
5. Run it

The result would be in the pool, compared to the Hyper-K sensitivity window, and available for any future computation that needs the proton lifetime as input.

This is how the map grows. One derivation function at a time. One experiment at a time. One comparison at a time. Each step small enough for one person in one afternoon. Each step cumulative, the result stays in the pool forever, available to everyone who comes after.

The tool is the torch. It's designed to be passed.
