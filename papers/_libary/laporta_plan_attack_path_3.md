## Notebook: Attack 3 — The Combined ζ + Elliptic PSLQ and What It Opens

**Status:** Planning notebook. Pre-computation.
**Date:** April 19, 2026
**Context:** Post PHYS-46 through PHYS-49. Seven experiments, 316 outputs, 65 PASS. The magnitude scan and ζ subtraction have identified WHERE to look. Attack 3 is the definitive test.

---

### 1. WHAT WE KNOW NOW

The magnitude scans and subtraction experiments established suggestive but not definitive evidence:

**From the raw elliptic scan (experiment_laporta_toroidal_v0):** All six Laporta integrals match combinations (p/q) × K(k)^a × E(k)^b to better than 0.006%. But the scan tested 562,500 candidates per integral. Random matches at the 0.002% level are expected. The hits are at the random noise floor. Not conclusive.

**From the ζ subtraction scan (experiment_remainder_elliptic_v0):** Subtracting integer × ζ(3) or ζ(5) from each integral improved the elliptic match by 7-266×. The post-subtraction misses are 0.00001%-0.001% — 10-100× below the random floor. 6/6 improved. This is strongly suggestive but still from a magnitude scan with a large candidate space (20 subtractions × 250,000 elliptic candidates = 5 million per integral).

**What we DON'T have:** A PSLQ relation. PSLQ is definitive — it either finds an exact linear relation with bounded coefficients or proves none exists within those bounds. The 24/24 null against the 66-element polylogarithmic basis proved the integrals are NOT polylogarithmic. But we never tested them against elliptic periods because K(k) and E(k) were not in the basis.

**The gap:** We have the right forms (KE, K³, K, K²/π, E×π) and the right ζ subtractions (2, −5, 2, −3, 4, −2). We have approximate moduli (k = 0.15 to 0.999 from the scan grid). We don't have the EXACT moduli, and we don't have PSLQ confirmation.

---

### 2. WHY ATTACK 3 IS DIFFERENT FROM ATTACKS 1-2

**Attack 1 (PSLQ against polylogarithmic basis):** 66-element basis including π through π⁶, ζ(3) through ζ(9), Li₄ through Li₇, MZVs, alternating Euler sums, and all cross-products. This was the exhaustive polylogarithmic test. 24/24 null. The integrals are not in this basis.

**Attack 2 (PSLQ cross-relations):** 11 pairwise tests checking whether any Laporta integral is a linear combination of others. 11/11 null. The six integrals are mutually independent.

**Attack 3 (PSLQ with ζ + elliptic combined basis):** This is qualitatively different because:

1. The basis includes constants NOT in Attacks 1-2 — specifically K(k) and E(k) at topology-specific moduli.
2. The subtraction experiment tells us WHICH ζ to include (ζ(3), ζ(5)) and WHICH elliptic forms (K, E, K², KE, K³, K/π, K×π, E×π) to prioritize.
3. The moduli k are constrained by the magnitude scan to narrow ranges.
4. A FOUND result would be the first closed-form expression for a Laporta integral — resolving a question open since 2017.

---

### 3. WHAT THE BASIS MUST CONTAIN

The subtraction experiment suggests each Laporta integral has the form:

C_i = n_i × ζ(k_i) + r_i × f(K(k_topo), E(k_topo), π)

where n_i is a small integer, ζ(k_i) is ζ(3) or ζ(5), r_i is a rational p/q with small p and q, f is one of the forms K, E, K², KE, K³, K/π, Kπ, Eπ, K²/π, and k_topo is the topology-specific modulus.

The PSLQ basis for each integral should be:

**Core:** {C_i, 1, ζ(3), ζ(5)}

**Elliptic at modulus k:** {K(k), E(k), K(k)², K(k)E(k), K(k)³, K(k)²E(k)}

**Mixed elliptic-circular:** {K(k)π, E(k)π, K(k)/π, K(k)²/π, E(k)/π}

**Cross products ζ × elliptic:** {ζ(3)K(k), ζ(3)E(k), ζ(5)K(k), ζ(5)E(k)}

That's about 20 basis elements per modulus per integral. PSLQ with 20 elements needs precision roughly 20 × (digits per coefficient). At maxcoeff 1000, that's 20 × 3 = 60 digits minimum. At maxcoeff 10,000, that's 20 × 4 = 80 digits. We have 4925 digits. Precision is not the bottleneck.

**The bottleneck is the modulus k.** K(k) changes continuously with k. PSLQ tests a SPECIFIC set of constants. If we put K(0.60) in the basis but the true modulus is k = 0.5973, PSLQ returns null — not because the integral isn't elliptic but because we guessed the wrong k. The magnitude scan gives approximate moduli (to 2-3 significant figures from a 25-point grid). We need the exact modulus.

---

### 4. THE MODULUS PROBLEM

This is the central difficulty. The modulus k for each topology is determined by the Feynman diagram's internal mass and momentum structure. For the sunrise integral (two loops), the modulus is known analytically: k² = (m₁ + m₂ + m₃ − s)(m₁ + m₂ − m₃ + s)(m₁ − m₂ + m₃ + s)(−m₁ + m₂ + m₃ + s) / (16 m₁ m₂ m₃ s), where m_i are the propagator masses and s is the external momentum. For the four-loop topologies 81 and 83, no such formula has been published.

**Three approaches to the modulus:**

**Approach A: Literature search.** Adams, Bogner, and Weinzierl have computed elliptic moduli for specific Feynman topologies at two and three loops. Bloch, Kerr, and Vanhove have related Feynman integrals to periods of elliptic curves over specific number fields. If anyone has identified the elliptic curves for topologies 81 and 83, the modulus is known. This is a literature research task, not a computation.

**Approach B: Numerical modulus extraction.** Use the magnitude scan results to narrow the modulus range, then do a fine grid search. The scan found best matches at k = 0.60 (C81a, KE form) and k = 0.35 (C83a, K² form) — but these are from a coarse 25-point grid. A fine search over k = 0.55 to 0.65 in steps of 0.0001 for topology 81, and k = 0.30 to 0.40 for topology 83, would refine the modulus to 4 significant figures. Then PSLQ with K(k_refined) has a chance.

**Approach C: Modulus from the subtraction.** After subtracting the ζ content, the post-subtraction remainder should be a pure elliptic expression. For C81c + 2ζ(5), the best match was K at some k with miss 0.0000208%. At this precision, the modulus is determined: solve K(k) = (C81c + 2ζ(5)) × (q/p) for k. The miss of 0.00002% means we know k to 5-6 significant figures from the scan. At 4925 digits of C81c, we could extract k to thousands of digits — IF the form is correct.

**Approach C is the most powerful.** If we ASSUME the subtraction experiment identified the correct form (e.g., C81c + 2ζ(5) ≈ (1/18) × K(k₈₁)), then k₈₁ is determined by k₈₁ = K⁻¹(18 × (C81c + 2ζ(5))). We can compute this k to arbitrary precision from the 4925-digit value of C81c. Then we put K(k₈₁) into the PSLQ basis and test. If FOUND: the form is confirmed and the modulus is exact. If NULL: the form was wrong and we try the next candidate.

---

### 5. THE ATTACK 3 PROCEDURE

**Step 1: Extract candidate moduli from the subtraction results.**

For each integral, the subtraction experiment identified a ζ integer and a post-subtraction elliptic form. Use the post-subtraction value and the form to solve for k:

| Integral | Subtraction | Form | Equation for k |
|---|---|---|---|
| C81a | +2ζ(3) | K×π | K(k) = (C81a + 2ζ(3)) / (rational × π) |
| C81b | −5ζ(5) | K³ | K(k) = [(C81b − 5ζ(5)) / rational]^(1/3) |
| C81c | +2ζ(5) | K | K(k) = (C81c + 2ζ(5)) × rational |
| C83a | −3ζ(3) | K²/π | K(k) = [(C83a − 3ζ(3)) × π / rational]^(1/2) |
| C83b | +4ζ(3) | E×π | E(k) = (C83b + 4ζ(3)) / (rational × π) |
| C83c | −2ζ(5) | K³ | K(k) = [(C83c − 2ζ(5)) / rational]^(1/3) |

Each equation gives k to the precision of C_i (4925 digits) minus a few digits for the inversion. This gives candidate moduli at ~4920-digit precision.

**Critical check:** Do the three integrals within topology 81 give the SAME k? Do the three integrals within topology 83 give the SAME k? If yes: the modulus is topology-specific (one k per topology), and the three integrals within each topology are different elliptic forms at the same modulus. If no: either the forms are wrong, or each integral has its own modulus (which would mean the topology is more complex than a simple torus).

**Step 2: Build the PSLQ basis at each candidate modulus.**

For topology 81 (assuming k₈₁ from Step 1):

Basis = {C81a, 1, ζ(3), ζ(5), K(k₈₁), E(k₈₁), K², KE, K³, K²E, Kπ, Eπ, K/π, K²/π, ζ(3)K, ζ(3)E, ζ(5)K, ζ(5)E, π, π²}

About 20 elements. Compute each to 1000 digits (more than enough for PSLQ at maxcoeff 10,000).

Run PSLQ on {C81a, basis elements}.

**Step 3: Interpret results.**

FOUND with small coefficients (≤ 100): The integral has a closed form. Report the relation. Verify by computing both sides to 4925 digits.

FOUND with large coefficients (> 100): Possible spurious relation from over-fitting. Verify independently.

NULL at maxcoeff 10,000: The integral is not in this basis at this modulus. Either the modulus is wrong, or the form is more complex (e.g., involves higher products K⁴, K²E², or derivatives of K/E with respect to k).

**Step 4: If topology-consistent k found, reduce the constant count.**

If all three integrals within topology 81 are expressible in terms of K(k₈₁) and E(k₈₁), then the three integrals C81a, C81b, C81c are NOT independent — they are three different rational combinations of two transcendentals (K and E at a shared modulus). The six "independent" Laporta constants reduce to four: K₈₁, E₈₁, K₈₃, E₈₃. Or possibly fewer if the two topologies share a modulus.

This would be a major result: the six opaque constants become four (or two) understood constants at identified moduli. The Q335 basis gains specific, named entries rather than six opaque numbers.

---

### 6. WHAT ATTACK 3 OPENS UP IF SUCCESSFUL

**6a. Closed forms for Laporta integrals.** The first closed-form expressions for four-loop master integrals. Currently known to 4925 digits but with no analytical formula. A closed form would be a significant result in mathematical physics, independent of the HOWL framework.

**6b. The Q335 basis becomes richer.** Instead of six opaque entries, the basis gains elliptic periods at specific moduli. These moduli connect to the Feynman diagram topology — they are computable from the diagram structure, not free parameters. The basis becomes: Q335 polylogarithmic constants + elliptic periods at Feynman-determined moduli.

**6c. The A₄ decomposition becomes computable.** With closed forms for the Laporta integrals, and with the rational coefficients c₁-c₆ from Laporta 2017, the full three-layer decomposition of A₄ is computable. The spherical modulus, the number-theoretic remainder, and the toroidal remainder can be separated. The cancellation percentage at four loops can be computed. The cancellation staircase extends to loop 4.

**6d. The ζ + elliptic layering is confirmed.** The subtraction experiment suggested C_i = n × ζ + r × f(K, E). If PSLQ confirms this exact structure, the two-layer remainder is not a scan artifact — it is the actual mathematical structure of four-loop QED. Number theory and toroidal geometry are literally ADDED together in each integral.

**6e. The modulus identifies the elliptic curve.** Each modulus k determines an elliptic curve y² = x(x − 1)(x − k²). This curve is a specific mathematical object with known invariants (j-invariant, conductor, discriminant). Identifying the curve for each topology connects four-loop QED to algebraic geometry. The question "what elliptic curve is QED computing at four loops?" has a specific answer.

**6f. Higher-loop predictions.** If topologies 81 and 83 produce elliptic integrals at specific moduli, the question becomes: which five-loop topologies produce which integrals? The genus progression (sphere → torus → higher genus?) is testable. If five-loop topologies produce hyperelliptic periods, the pattern continues. If they produce more elliptic periods at new moduli, the pattern is different — each loop adds new tori rather than higher genus.

**6g. The dual geometry becomes computational.** With explicit moduli, the toroidal contribution to any QED observable is computable from the modulus + rational coefficients. The mass-dependent toroidal scaling (m/mₑ)² can be computed for any lepton at any loop order, not just estimated. The crossover mass (43 mₑ) can be computed precisely.

---

### 7. WHAT ATTACK 3 OPENS UP IF IT FAILS

**7a. The simple elliptic hypothesis fails.** If PSLQ returns 6/6 null against the combined ζ + elliptic basis at the topology-extracted moduli, the integrals are not simple combinations of K and E. This doesn't mean they're not geometric — they could involve:

- **Incomplete elliptic integrals** F(φ, k) and E(φ, k) at specific amplitudes φ ≠ π/2
- **Elliptic polylogarithms** ELi_n(x; k) — a recently developed function class
- **Periods of higher-dimensional varieties** — not tori but K3 surfaces or Calabi-Yau manifolds
- **Modular forms** — functions of τ = iK'/K rather than K directly
- **Iterated integrals of modular forms** — the cutting edge of Feynman integral computation

Each of these is a different kind of "non-spherical geometry." A null result doesn't kill the dual geometry hypothesis — it refines it. The toroidal sector might be more complex than simple elliptic periods.

**7b. The subtraction integers are wrong.** The ζ subtraction scan tested n from −5 to +5. If the true integer is outside this range, the subtraction identified the wrong ζ piece, leading to the wrong post-subtraction remainder, leading to the wrong modulus extraction. Attack 3 at the wrong modulus returns null. The fix: extend the ζ scan to n = ±20 and re-extract moduli.

**7c. The moduli are not topology-specific.** If the three integrals within topology 81 give three DIFFERENT moduli from Step 1, the topology does not have a single elliptic curve. Each integral might involve a different curve, or the integrals might involve the DERIVATIVE of K with respect to k (a different transcendental), or the relationship might be more complex than C = ζ + elliptic.

---

### 8. PRACTICAL REQUIREMENTS

**Precision:** 4925 digits available for each Laporta integral. PSLQ with 20-element basis needs ~100 digits minimum. We have 50× more than enough. Precision is not a constraint.

**Computation:** PSLQ at 20 elements × 1000 digits takes seconds in mpmath. The bottleneck is not PSLQ itself but the modulus extraction (Step 1) and the consistency check (do three integrals give the same k within each topology?).

**Software:** mpmath PSLQ, mpmath ellipk/ellipe for computing K and E at arbitrary precision, Newton's method for inverting K(k) = target.

**Data needed:** The six Laporta integrals at 4925 digits (in pool: laporta_C81a_v0 through laporta_C83c_v0). ζ(3) and ζ(5) at 1000+ digits (computable from mpmath). The rational p/q values from the subtraction scan (in experiment results).

**What we DON'T need from external sources:** No literature lookup required for the computation itself. The modulus is extracted from our own data. If we want to VERIFY the modulus against the Feynman diagram structure, that requires understanding the specific propagator routing of topologies 81 and 83 — but that's verification, not computation.

---

### 9. THE DERIVATION CHAIN

Attack 3 is three derivation functions:

**laporta_modulus_extraction_v0:** For each integral, use the subtraction result (ζ integer + elliptic form + rational p/q) to solve for the modulus k. Check consistency: do the three integrals within each topology give the same k? Report k to maximum available precision. Flag if inconsistent.

**laporta_pslq_elliptic_v0:** For each integral, build the combined ζ + elliptic basis at the extracted modulus. Run PSLQ at maxcoeff 1000, then 10,000. Report FOUND or NULL for each. If FOUND, verify by computing both sides to 4925 digits.

**laporta_closed_form_v0:** If any FOUND results, assemble the closed-form expression. Verify it reproduces the integral to all 4925 digits. Compute the A₄ decomposition using the closed forms and the rational coefficients c₁-c₆ (if available). Report the three-layer decomposition of A₄.

---

### 10. WHAT CHANGES IN THE FRAMEWORK

**If 6/6 FOUND (best case):**

The Q335 basis gains 2-4 elliptic period entries (K₈₁, E₈₁, K₈₃, E₈₃ or fewer if moduli coincide). The six Laporta constants reduce to rational combinations of these periods plus ζ values. The A₄ three-layer decomposition is computable. The dual geometry hypothesis is confirmed at four loops. The modulus/remainder framework is complete at both the conceptual level (PHYS-49) and the computational level (closed forms).

**If 3-5 FOUND (partial success):**

Some integrals have closed forms, others don't. The ones that don't may need more complex forms (elliptic polylogarithms, modular forms). The partial success still identifies the moduli for the successful integrals and provides closed forms that the community can verify. The framework is partially complete.

**If 0/6 FOUND (null):**

The simple elliptic hypothesis fails. The integrals may involve more complex structures. The magnitude scan matches and subtraction improvements are reinterpreted as approximate coincidences or as indicators of more complex structure. The dual geometry hypothesis is not killed (the β⁰ classification and the mass scaling are independent of the elliptic question) but the toroidal identification weakens. The next step is to test elliptic polylogarithms or modular forms as the basis.

---

### 11. THE CONSISTENCY TEST IS THE CRITICAL GATE

Before running PSLQ, the consistency check in Step 1 is the make-or-break test. If the three integrals within topology 81 give the SAME modulus k₈₁ (to within the precision of the subtraction scan), the elliptic hypothesis is strongly supported even before PSLQ runs. The probability that three random numbers, after subtracting different ζ values and matching different elliptic forms, all yield the same k is extremely small.

If they give DIFFERENT moduli, the hypothesis needs revision. The topology might involve multiple elliptic curves, or the subtraction integers might be wrong, or the forms might be wrong.

The consistency test is computable now, with existing pool data, without any external input. It requires only the modulus extraction computation (Step 1) and a comparison of the three k values within each topology.

This is the first thing Attack 3 should compute. If the moduli are consistent, proceed to PSLQ. If not, diagnose why and revise the subtraction scan before wasting PSLQ on the wrong moduli.

---

### 12. TIMELINE AND DEPENDENCIES

**Can start immediately:** Modulus extraction (Step 1) and consistency check. All data in pool. No external dependency.

**Blocked on nothing computational:** PSLQ, elliptic function evaluation, Newton inversion — all available in mpmath. The computation is straightforward once the moduli are extracted.

**Blocked on c₁-c₆ for the A₄ decomposition:** The rational coefficients that determine how each Laporta integral enters A₄ are in Laporta's 2017 paper. Extracting them requires reading the paper. This blocks the full three-layer decomposition of A₄ but does NOT block the closed-form search for the individual integrals.

**Timeline estimate:** The consistency check and PSLQ for all six integrals could be done in one session. The modulus extraction is a single derivation function. The PSLQ is a single derivation function. The interpretation is immediate — FOUND or NULL is unambiguous.

---

### 13. THE PRIZE

If Attack 3 succeeds, the following statements become proven:

1. The Laporta integrals are NOT opaque numerical constants. They are specific combinations of ζ values and elliptic periods at Feynman-determined moduli.

2. Four-loop QED computes periods of specific elliptic curves. The curves are identified. The moduli are exact.

3. The QED perturbation series undergoes a verified geometric phase transition at four loops. Loops 1-3 compute polylogarithmic periods (genus 0). Loop 4 computes elliptic periods (genus 1).

4. The modulus/remainder framework has a complete computational implementation: every QED coefficient through four loops decomposes into spherical modulus + number-theoretic remainder + toroidal remainder, with all three pieces expressed in closed form.

5. The most precisely measured quantity in physics (a_e, 13 digits) depends on the periods of two specific elliptic curves. The curves are named. The moduli are known. The coefficients are exact.

This is the difference between "suggestive" and "proven." The magnitude scans are suggestive. Attack 3 is the proof.

---

**End of notebook. Status: ready to execute. No external dependencies for the core computation. The consistency check is the critical gate. If consistent moduli are found, PSLQ follows immediately.**
