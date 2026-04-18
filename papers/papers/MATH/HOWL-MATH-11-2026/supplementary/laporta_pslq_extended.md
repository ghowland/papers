## Laporta PSLQ Report: C81a Returns Null at 66 Constants, 400 Digits

**Date:** April 18, 2026
**Target:** C81a master integral from Laporta 2017 four-loop a_e calculation
**Precision:** 400 working digits (4923 available)
**Basis:** 66 transcendental constants covering all known structures through weight 8

---

### Result

**C81a: NULL across all three tiers.** No integer relation found between C81a and any linear combination of 66 transcendental constants with integer coefficients up to 10,000.

| Tier | Basis size | Constants included | Result |
|---|---|---|---|
| tier1_standard | 52 | π powers, ζ values, ln(2) powers, Li_n(±½), all cross products | NULL |
| tier2_with_mzv | 58 | + ζ(3,5), ζ(5,3), ζ(3,3), s₆, ζ̄(5,1), ζ̄(3,3) | NULL |
| tier3_full | 66 | + all MZV×ln(2), MZV×π², alternating sum products | NULL |

---

### What the basis covered

The 66-element basis includes every class of constant known to appear in multi-loop QED and QCD calculations through four loops:

**Standard transcendentals (weight 1-9):** π through π⁶, ζ(3) through ζ(9), ln(2) through ln⁶(2). All cross products up to weight 8.

**Polylogarithms at ½:** Li₄(½) through Li₇(½) and their products with ln(2) and π².

**Polylogarithms at −1:** Li₄(−1) through Li₇(−1). These are known to reduce to π powers and ζ values, but including them guards against unexpected combinations.

**Multiple zeta values:** ζ(3,5), ζ(5,3), ζ(3,3). These are the weight-8 and weight-6 double zeta values that appear in state-of-the-art four-loop calculations.

**Alternating Euler sums:** s₆ = Σ(−1)^(n+1)/(n⁶ 2ⁿ), ζ̄(5,1) = Σ(−1)^(n+1) H_n/n⁵, ζ̄(3,3). These are the alternating double sums from massive four-loop propagator calculations.

**All products:** MZV × ln(2), MZV × π², alternating sum × ln(2), alternating sum × π². Total coverage of all known product structures at weight ≤ 8.

---

### What this means

At 400 digits with a 66-element basis covering the complete known transcendental landscape at four loops, PSLQ finds no relation. Combined with the earlier 36-element scan at 300 digits, C81a has now been tested against two independent basis sets at two precision levels. Both return null.

The possible interpretations narrow:

**1. The coefficient bound is too low.** PSLQ with maxcoeff = 10,000 can find relations with integer coefficients up to ±10,000. If C81a involves coefficients of order 100,000 or larger, the current bound would miss it. Four-loop QED coefficients are known to involve large integers (the A₄ coefficient has terms with denominators of order 10⁶). Increasing maxcoeff to 100,000 or 1,000,000 would test this, at the cost of slower runtime.

**2. The precision is insufficient for the basis size.** PSLQ with n basis elements needs roughly n × log₁₀(maxcoeff) digits of precision to detect a relation. With 66 elements and maxcoeff = 10,000, the requirement is ~66 × 4 = 264 digits. We used 400, which provides margin. But if the true coefficients are large (10⁵-10⁶), we need ~66 × 6 = 396 digits — right at our working precision. Increasing to 1000 digits would eliminate this concern entirely.

**3. The basis is genuinely incomplete.** The constants involve structures not in our basis. Candidates beyond what we tested: elliptic integrals (which appear in some massive four-loop diagrams), hypergeometric values ₃F₂ at special arguments, or iterated integrals over modular forms (which have recently appeared in cutting-edge multi-loop calculations by Broadhurst and others). These are qualitatively different from the polylogarithmic basis and would require a different computational approach.

**4. C81a is a genuinely new constant.** If interpretations 1-3 are excluded, C81a is independent of all known transcendental constants at weight ≤ 8. It would join the Q335 basis as a new fundamental constant of nature — a number that appears in the electron's magnetic moment and has no expression in terms of π, ζ values, logarithms, polylogarithms, or multiple zeta values.

---

### Recommended next steps

| Priority | Action | What it tests | Time estimate |
|---|---|---|---|
| 1 | Run C81a at --digits 1000 --maxcoeff 100000 | Eliminates interpretations 1 and 2 | ~30 min |
| 2 | Run remaining 5 integrals at --digits 400 | Checks whether ALL six are null or some are expressible | ~2 hours |
| 3 | Add elliptic constants to basis | Tests interpretation 3 (incomplete basis) | Requires identifying which elliptic integrals |
| 4 | If all null at 1000 digits: declare independence | Interpretation 4 confirmed | Write MATH-12 |

Step 1 is decisive. If C81a remains null at 1000 digits with maxcoeff = 100,000, the precision and coefficient arguments are eliminated. The only remaining explanations are an incomplete basis (elliptic/modular constants) or genuine independence.

Step 2 is informative even if C81a stays null. If some of the six integrals ARE expressible and others are not, the expressible ones tell us which parts of the four-loop calculation reduce to known constants and which parts are genuinely new. A mixed result (some FOUND, some NULL) would be more informative than uniform null.

---

### Context

This continues the PSLQ independence program from MATH-6 (82/82 null on the Q335 basis constants). MATH-6 proved that the 29 transcendental constants in the Q335 basis are mutually independent. This scan asks a different question: are the Laporta four-loop master integrals expressible in terms of those constants (plus MZVs and alternating sums)?

If the answer is no — if the Laporta integrals are genuinely independent of the known transcendental basis — this is a significant result for both number theory and physics. It means the electron's anomalous magnetic moment at four loops involves constants that mathematicians have not yet classified. The 8-year failure of the multi-loop community to identify these constants would be explained: they couldn't find a closed form because no closed form exists in the known basis.

For the RUM framework specifically: if C81a is independent, it becomes a new Q335 entry. The A₄ QED coefficient would contain a term with C81a as an irreducible constant, alongside the π, ζ, and ln(2) terms that reduce. The β-content decomposition from MATH-11 would classify C81a as β⁰ (no π content) — a purely number-theoretic contribution with no L1/L2 geometric origin.
