The library gives you:
Data: 5 H₀ measurements with full metadata, uncertainties, sources, distance classes, and effective_N = None for all (honest unknowns).
Model: H0_running(H0_0, r, N) computes H₀ at any transit count. extract_r and required_r compute the per-transit correction. fit_running_curve fits the two-parameter model to any set of measurements with assigned N values.
Falsification tests: F1 (monotonicity), F2 (rational r), F3 (chi²/dof), F4 (intermediate distinctness) — all as callable functions returning (passed, details).
Structural parallel: VP step size 1/(3π) for direct comparison to the H₀ per-transit correction at any N.
Scanning: scan_rational_candidates checks if 1−r at any N is close to a simple fraction with R₂-related denominators.
Every None is an honest hole. The library is a tool for testing, not a claim that the hypothesis is correct. Run it.

---

The F1 failure is real and informative. H0LiCOW (73.3) is higher than SH0ES (73.0). The monotonicity test correctly catches this.

This is not a bug — it's the hypothesis meeting data. Two interpretations:

**Interpretation A:** SH0ES and H0LiCOW are at effectively the same distance class (both "local"), and the 0.3 difference is within their combined uncertainties (±1.0 and ±1.8 overlap completely). The monotonicity test is too strict — it should allow for measurement uncertainty.

**Interpretation B:** The ordering is genuinely non-monotonic, which is evidence against the simple running curve.

The honest response: modify the F1 test to account for uncertainties, and add a strict version that doesn't. Both are informative.

Replace the F1 test in the self-test section with:

```python
    # F1 strict: raw values
    H0_ordered_values = [H0_MEASUREMENTS[k]["H0"] for k in H0_ORDERED]
    f1_strict, f1_strict_detail = test_F1_monotonic(H0_ordered_values)
    chk_bool("F1 strict: raw H0 monotonically decreasing",
             f1_strict, f1_strict_detail, checks)

    # F1 soft: within 1-sigma bands, consistent with monotonic?
    # SH0ES and H0LiCOW overlap at 1 sigma (73.0±1.0 vs 73.3±1.8)
    bands_consistent = True
    for i in range(len(H0_ORDERED) - 1):
        m_near = H0_MEASUREMENTS[H0_ORDERED[i]]
        m_far = H0_MEASUREMENTS[H0_ORDERED[i + 1]]
        upper_far = f2m(m_far["H0"] + m_far["uncertainty"])
        lower_near = f2m(m_near["H0"] - m_near["uncertainty"])
        if upper_far > lower_near:
            pass  # bands overlap or far < near — consistent
        # only fails if far is ABOVE near even at 1 sigma
    # Real test: is far+1sigma > near-1sigma for any adjacent pair
    # where far > near in central value?
    soft_violations = []
    for i in range(len(H0_ORDERED) - 1):
        m_near = H0_MEASUREMENTS[H0_ORDERED[i]]
        m_far = H0_MEASUREMENTS[H0_ORDERED[i + 1]]
        if f2m(m_far["H0"]) > f2m(m_near["H0"]):
            lower_far = f2m(m_far["H0"] - m_far["uncertainty"])
            upper_near = f2m(m_near["H0"] + m_near["uncertainty"])
            if lower_far > upper_near:
                soft_violations.append("%s > %s even at 1 sigma" % (
                    H0_ORDERED[i+1], H0_ORDERED[i]))
    f1_soft = len(soft_violations) == 0
    chk_bool("F1 soft: monotonic within 1-sigma uncertainties",
             f1_soft,
             "violations: %s" % (soft_violations if soft_violations else "none — bands overlap"),
             checks)
```

This gives you two F1 tests: strict (raw values, currently FAIL because 73.3 > 73.0) and soft (within uncertainties, should PASS because the bands overlap). Both results are informative. The strict failure tells you SH0ES and H0LiCOW may be in the same distance class, not ordered. The soft pass tells you the data is consistent with monotonicity within measurement precision.

The chi²/dof = 6.98 from the example fit also confirms what the notebook predicted: the guessed N assignments are wrong. Real N values from structure catalogs are the primary data gap. The library correctly identifies this.

15/16 with one physically meaningful failure is the right state for a hypothesis library. The FAIL is data, not a bug.

---

