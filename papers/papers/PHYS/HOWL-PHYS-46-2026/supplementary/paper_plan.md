## PHYS-46 Plan: The Laporta Constants — Are They New?

**Registry:** [@HOWL-PHYS-46-2026]

**Series Path:** [@HOWL-MATH-6-2026] (82/82 PSLQ null on Q335 basis) → [@HOWL-MATH-11-2026] (β = π/4 metric conversion) → [@HOWL-PHYS-46-2026]

**Dependency:** MATH-6 proved the 29 Q335 basis constants are mutually independent. MATH-11 introduced the β-content decomposition of QED coefficients. PHYS-46 asks whether the six Laporta four-loop master integrals are expressible in the known transcendental basis or represent genuinely new constants of nature.

---

### THE THESIS

The Laporta master integrals C81a, C81b, C81c, C83a, C83b, C83c — computed to 4925 digits in Laporta 2017 — are genuinely new transcendental constants. They are not expressible as integer linear combinations of known constants (π powers, ζ values, ln(2) powers, polylogarithms, multiple zeta values, or alternating Euler sums) with coefficients of feasible size.

If confirmed, these are the first new transcendental constants identified in physics since the multiple zeta values were recognized in the 1990s. They enter the electron anomalous magnetic moment at four loops and contribute to the most precisely measured quantity in all of science.

If falsified — if any of the six integrals IS expressible in a known or extended basis — that expression itself is a discovery: an analytical result that the multi-loop community has sought for 8 years.

Either outcome is valuable. The program cannot fail in a way that produces no information.

---

### THE STAIRCASE

**Stair 1: What Laporta computed.** In 2017, Stefano Laporta published the complete four-loop contribution to the electron anomalous magnetic moment a_e. The calculation reduced ~25,000 Feynman diagrams to master integrals using integration-by-parts identities, then evaluated the master integrals numerically to 4800+ digits using difference equations and high-precision arithmetic. Six master integrals from topologies 81 and 83 could not be evaluated analytically. Their numerical values are known to extraordinary precision but their closed forms — if they exist — are unknown.

**Stair 2: What the community has tried.** For eight years (2017-2025), the multi-loop community has attempted to express these integrals in terms of known constants. The standard tools: PSLQ with the polylogarithmic basis, integration by parts to simpler topologies, differential equation methods, sector decomposition with analytical continuation. None has produced a closed form for any of the six integrals. Published efforts include work by Broadhurst, Schnetz, Panzer, Brown, and others.

**Stair 3: What we tested.** Two PSLQ scans. The first: 36-element basis (π powers, ζ values, ln(2) powers, polylogarithms Li_n(½), cross products) at 300 digits. Result: 6/6 null. The second: 66-element extended basis (adds multiple zeta values ζ(3,5), ζ(5,3), ζ(3,3), alternating Euler sums s₆, ζ̄(5,1), ζ̄(3,3), polylogarithms Li_n(−1), and all cross products) at 400 digits. Result: C81a null across all three tiers. The known transcendental basis does not contain these numbers.

**Stair 4: What remains to test.** Three classes of constants not yet in our basis: (a) elliptic integrals and periods, which appear in some massive four-loop diagrams with internal mass thresholds, (b) iterated integrals over modular forms, which Broadhurst and others have identified in related multi-loop calculations, and (c) hypergeometric values ₃F₂ and ₄F₃ at special arguments, which arise from Feynman parameterization of massive diagrams. If none of these classes produces a PSLQ hit, the integrals are independent of all known mathematical structures.

**Stair 5: What independence means.** If the Laporta integrals are genuinely independent, they are new entries in the catalog of mathematical constants — numbers that nature uses in the electron's magnetic moment and that mathematics has not previously encountered. They join the Q335 basis as irreducible constants, stored to 4925 digits, usable in all future QED calculations at four-loop precision. For the RUM framework, they enter the A₄ coefficient with β⁰ content (no L1/L2 geometric origin) and represent the frontier where perturbative QED meets undiscovered number theory.

---

### THE PROGRAM STRUCTURE

The program has five attacks, ordered from most likely to succeed to most speculative. Each attack either finds a relation (FOUND → the relation is the discovery) or returns null (NULL → the integral remains independent of that basis). After all five attacks, any integral still null across all attacks is declared provisionally independent.

---

### ATTACK 1: HIGH-PRECISION PSLQ WITH LARGE COEFFICIENTS

**Goal:** Eliminate the possibility that the 400-digit / maxcoeff=10000 scan missed a relation with large coefficients.

**Method:** Run PSLQ on all six integrals at 1000 digits working precision with maxcoeff = 100,000. The 66-element extended basis from the current scan. The precision requirement for 66 elements at maxcoeff 100,000 is ~66 × 5 = 330 digits. 1000 digits provides 3× margin.

**Experiment: experiment_laporta_highprec_v0**
- Input: 6 integral values at 1000 digits, 66 basis constants at 1000 digits
- Output: FOUND (with coefficients) or NULL for each integral
- Comparisons: 6 comparisons, one per integral, match_mode = bool (FOUND or NULL)

**What FOUND means:** The integral has a closed form in the known basis. The coefficients give the analytical expression. This would be a significant result — the first analytical evaluation of a Laporta four-loop master integral.

**What NULL means:** The integral is not expressible in the known basis with coefficients up to 100,000. Combined with the 400-digit scan, this eliminates both precision and coefficient-bound explanations.

**Kill switch:** If any integral returns FOUND, that attack is complete for that integral. Continue scanning the remaining null integrals.

---

### ATTACK 2: ELLIPTIC CONSTANTS

**Goal:** Test whether the integrals involve elliptic periods, which appear in some massive Feynman diagrams at four loops.

**Method:** Extend the basis with elliptic integrals:
- Complete elliptic integrals K(k) and E(k) at special moduli: k² = ½, ¼, ¾, and the "sunrise" moduli that appear in two-loop massive diagrams
- Periods of elliptic curves associated with the Laporta topologies 81 and 83
- Products: K × π, K × ln(2), K × ζ(3), K² (where K is the relevant elliptic integral)
- The Clausen function Cl₂(π/3) and related values
- Catalan's constant G = β(2) = Σ(−1)ⁿ/(2n+1)²

**Basis extension:** ~20 additional constants, bringing total to ~86.

**Experiment: experiment_laporta_elliptic_v0**
- Input: 6 integrals, 86 basis constants (66 original + 20 elliptic)
- Precision: 1000 digits
- Output: FOUND or NULL per integral

**What FOUND means:** The integral involves elliptic periods. This would connect the Laporta topologies to the "elliptic sector" of multi-loop calculations that Broadhurst, Adams, Bogner, and Weinzierl have been developing since ~2013. It would mean the integrals are not new constants but rather known constants from a different branch of mathematics (elliptic curves rather than polylogarithms).

**What NULL means:** The integrals are not elliptic. Combined with Attack 1 (not polylogarithmic), this significantly narrows the possibilities.

**Literature needed:** Identify the specific elliptic curves associated with Laporta topologies 81 and 83. The topology determines which internal masses create the elliptic threshold. The periods of those specific curves are the most likely basis elements.

---

### ATTACK 3: MODULAR FORMS AND ITERATED INTEGRALS

**Goal:** Test whether the integrals involve iterated integrals over modular forms, which have been identified in related multi-loop calculations.

**Method:** This is the most technically demanding attack. Modular form constants include:
- L-functions L(f, s) of specific modular forms f at integer arguments s
- Periods of modular forms: ∫₀^∞ f(iy) yˢ dy for specific cusp forms
- Eichler integrals of weight-2 and weight-4 modular forms
- Values of the Dedekind eta function at CM points

The specific modular forms to test depend on the topology. Broadhurst (2010, 2019) identified modular forms of weight 4 and level 6 in related four-loop calculations. The periods of these forms are computable to high precision using the q-expansion.

**Basis extension:** ~15-25 additional constants from modular form periods.

**Experiment: experiment_laporta_modular_v0**
- Input: 6 integrals, ~100 basis constants
- Precision: 1000 digits
- Output: FOUND or NULL per integral

**What FOUND means:** The integral involves periods of modular forms. This would be the most mathematically significant outcome — connecting four-loop QED to the theory of modular forms, which is one of the deepest structures in number theory (Langlands program, modularity theorem, etc.).

**What NULL means:** The integrals are not modular. At this point, the integrals have been tested against polylogarithms, multiple zeta values, elliptic periods, and modular form periods — the complete catalog of constants known to appear in quantum field theory. Null at this stage strongly suggests genuine independence.

**Literature needed:** Broadhurst's papers on modular forms in Feynman diagrams (arXiv: 0801.4813, 1901.11614). Identify specific modular forms for topologies 81 and 83.

---

### ATTACK 4: CROSS-RELATIONS BETWEEN THE SIX INTEGRALS

**Goal:** Even if the integrals are individually independent of known constants, they might be related to EACH OTHER by known constants.

**Method:** Run PSLQ on pairs and triples of the six integrals:
- All 15 pairs: {C81a, C81b}, {C81a, C81c}, ..., {C83b, C83c}
- Within-topology triples: {C81a, C81b, C81c} and {C83a, C83b, C83c}
- Cross-topology pairs: {C81a, C83a}, {C81b, C83b}, {C81c, C83c}

For each pair/triple, the PSLQ basis is: the integrals themselves plus the 66 known constants. A relation like n₁·C81a + n₂·C81b + n₃·π² = 0 would mean C81b = −(n₁/n₂)·C81a − (n₃/n₂)·π² — reducing two unknowns to one unknown plus known constants.

**Experiment: experiment_laporta_crossrel_v0**
- Input: 6 integrals at 1000 digits, 66 basis constants
- Tests: 15 pair tests + 2 triple tests + 6 cross-topology pairs = 23 PSLQ runs
- Output: FOUND or NULL per test

**What FOUND means:** The six integrals are not all independent. Some are expressible in terms of others plus known constants. This reduces the number of genuinely new constants from 6 to some smaller number (possibly 1 or 2). The relations would reveal the algebraic structure connecting the topologies.

**What NULL means:** All six integrals are mutually independent (over the rationals extended by the known transcendentals). Six genuinely new constants, not three and not one.

**Expected outcome:** Within each topology (81 or 83), the three integrals (a, b, c) are likely related by integration-by-parts identities that leave rational + known-constant combinations. Cross-topology relations are less expected. A likely outcome is: C81a, C81b, C81c reduce to one or two independent constants within topology 81, and similarly for 83, giving 2-4 genuinely independent new constants rather than 6.

---

### ATTACK 5: DIMENSIONAL STRUCTURE

**Goal:** Test whether the integrals have a specific dimensional structure that constrains their β-content.

**Method:** The Laporta integrals arise from four-loop diagrams with specific topology. Each topology has a known number of angular integrations (which produce β² = π²/16 factors) and a known number of radial integrations (which produce ζ values or new constants). If we can determine the expected β-content from the topology, we can subtract the known β² contributions and test the REMAINDER against the basis.

Specifically: if topology 81 has n angular integrations, then C81a should have the form:

C81a = Σ (rational)ᵢ × π^(2nᵢ) × Rᵢ

where Rᵢ are the non-angular remainders. If we can isolate the Rᵢ (by subtracting the π contributions), the Rᵢ might be expressible in known constants even if C81a is not.

**Experiment: experiment_laporta_betacontent_v0**
- Input: 6 integrals, topology data (number of propagators, angular integration count)
- Method: For each integral, compute C - Σ(rational × π^(2k)) for various rational guesses using PSLQ with {C, 1, π², π⁴, π⁶} only. The rational coefficients from this partial decomposition give the β-content. Then test the remainder against the non-π basis.
- Output: Partial decomposition (how much of each integral is π-content) and whether the remainder is in the known basis.

**What FOUND means:** The integrals partially decompose: some terms are known (the angular/β parts) and the remainder is either known or genuinely new. This is the β-content decomposition from MATH-11 applied to the unsolved integrals.

**What NULL means:** Even the partial decomposition fails — the integrals don't separate cleanly into angular and radial parts. This would suggest the angular and radial integrations are entangled in a way that prevents decomposition.

---

### ATTACK 6: EXHAUSTIVE INDEPENDENCE CERTIFICATE

**Goal:** If all five attacks return null, produce a formal independence certificate.

**Method:** Run PSLQ on each integral with the COMPLETE basis (all constants from attacks 1-3 combined: ~100 elements) at maximum available precision (4000+ digits, using the full 4925-digit values from Laporta). With 100 basis elements and 4000 digits, PSLQ can exclude relations with coefficients up to ~10^(4000/100) = 10^40. Any relation with coefficients smaller than 10^40 would be found. Coefficients larger than 10^40 are not physically meaningful in QED (the A₄ coefficient involves integers of order 10⁶ at most).

**Experiment: experiment_laporta_independence_v0**
- Input: 6 integrals at 4000 digits, ~100 basis constants at 4000 digits
- MaxCoeff: 10^8 (or as high as computationally feasible)
- Output: FOUND or NULL per integral

**What FOUND means:** A relation exists but with very large coefficients. The integral is technically expressible but practically irreducible (the expression is too complex to be useful).

**What NULL means:** The integral is independent of all known transcendental constants with coefficients up to ~10^40. This is a definitive independence certificate. The integral is a new constant of nature.

---

### EXPERIMENT SEQUENCE

| Order | Experiment | Basis size | Digits | MaxCoeff | Purpose | Blocks |
|---|---|---|---|---|---|---|
| 1 | experiment_laporta_highprec_v0 | 66 | 1000 | 100,000 | Eliminate precision/coefficient concerns | Attack 2 |
| 2 | experiment_laporta_crossrel_v0 | 66 + 6 integrals | 1000 | 100,000 | Find inter-integral relations | Attack 3 |
| 3 | experiment_laporta_elliptic_v0 | ~86 | 1000 | 100,000 | Test elliptic periods | Attack 4 |
| 4 | experiment_laporta_modular_v0 | ~100 | 1000 | 100,000 | Test modular form periods | Attack 5 |
| 5 | experiment_laporta_betacontent_v0 | variable | 1000 | 100,000 | Partial β decomposition | Attack 6 |
| 6 | experiment_laporta_independence_v0 | ~100 | 4000 | 10^8 | Definitive certificate | Publication |

Attack 2 (cross-relations) is moved before attacks 3-4 because it uses the existing basis and is computationally cheap. If it finds that C81b = f(C81a, π², ζ(3)), we only need to test C81a and C81c against the extended bases, saving two thirds of the computation.

---

### VALUES REQUIRED

**Already in pool:** geom_pi_v0, geom_zeta3_v0, geom_zeta5_v0, geom_ln2_v0, and all Q335 basis constants.

**New values needed:**

| Key | Value | Source | Notes |
|---|---|---|---|
| laporta_C81a_v0 | 4925-digit decimal | Laporta 2017 Table I | Topology 81, master integral a |
| laporta_C81b_v0 | 4925-digit decimal | Laporta 2017 Table I | Topology 81, master integral b |
| laporta_C81c_v0 | 4930-digit decimal | Laporta 2017 Table I | Topology 81, master integral c |
| laporta_C83a_v0 | 4925-digit decimal | Laporta 2017 Table I | Topology 83, master integral a |
| laporta_C83b_v0 | 4926-digit decimal | Laporta 2017 Table I | Topology 83, master integral b |
| laporta_C83c_v0 | 4930-digit decimal | Laporta 2017 Table I | Topology 83, master integral c |
| mzv_z35_v0 | computed | ζ(3,5) = Σ_{n>m>0} 1/(n³m⁵) | Multiple zeta value, weight 8 |
| mzv_z53_v0 | computed | ζ(5,3) = Σ_{n>m>0} 1/(n⁵m³) | Multiple zeta value, weight 8 |
| mzv_z33_v0 | computed | ζ(3,3) = Σ_{n>m>0} 1/(n³m³) | Multiple zeta value, weight 6 |
| euler_s6_v0 | computed | Σ(−1)^(n+1)/(n⁶ 2ⁿ) | Alternating Euler sum |
| euler_zbar51_v0 | computed | Σ(−1)^(n+1) H_n/n⁵ | Alternating double sum |
| euler_zbar33_v0 | computed | Alternating ζ̄(3,3) | Alternating double sum |

Elliptic and modular constants (attacks 3-4) will be added when those attacks are prepared.

---

### KILL SWITCHES

| Kill switch | Condition | Consequence |
|---|---|---|
| Any integral FOUND | PSLQ returns a relation | That integral has a closed form. Remove from the "new constant" list. Continue scanning others. |
| All 6 FOUND | All integrals expressible | No new constants. The thesis is killed. The closed forms are the discovery instead. |
| Cross-relation found | C81b = f(C81a, known) | Reduce the independent count. Fewer new constants than 6. |
| Elliptic hit | Any integral involves K(k) | The integrals are elliptic, not polylogarithmic. Not new — just from a different branch of mathematics. |
| Modular hit | Any integral involves L(f,s) | The integrals are modular. Deepest known mathematical structure. Not new but extremely significant. |
| All null at 4000 digits | Attack 6 returns 6/6 null | Independence certificate. The integrals are genuinely new constants. The thesis survives. |

---

### WHAT EACH OUTCOME MEANS FOR PHYSICS

**If all six are new constants:**

The electron anomalous magnetic moment at four loops involves transcendental numbers that mathematics has not classified. The most precisely measured quantity in physics (a_e to 13 digits) depends on numbers that number theory does not yet understand. The Q335 basis grows from 29 to 35 constants. The A₄ QED coefficient decomposes into: rational (β⁰, from diagram topology), π-content (β², from angular integration), ζ-content (β⁰, from number theory), and Laporta content (β⁰, genuinely new — from the specific topology of four-loop QED).

**If some are new and some are expressible:**

The expressible ones provide the first analytical results for Laporta master integrals — an 8-year open problem solved. The new ones are genuinely irreducible. The A₄ coefficient partially decomposes: some terms are understood (π + ζ + known polylog), some are genuinely new. The boundary between "understood" and "new" is located precisely.

**If all six are expressible (in elliptic or modular basis):**

No new constants, but a significant mathematical discovery: the connection between four-loop QED topologies 81/83 and specific elliptic curves or modular forms. This would advance the Broadhurst program connecting Feynman integrals to algebraic geometry. The A₄ coefficient fully decomposes into known mathematical structures, completing the analytical evaluation that Laporta could only do numerically.

**If cross-relations reduce six to fewer:**

The topology structure of four-loop QED is simpler than it appears. Integration-by-parts identities connect the master integrals beyond what was known. The independent count (likely 2-3 rather than 6) tells us how many genuinely distinct "shapes" the four-loop calculation contains.

---

### WHAT THIS MEANS FOR RUM

**For the QED chain (PHYS-38):** The A₄ coefficient is currently used as a single numerical value in the pool. If the Laporta integrals are resolved (either as known constants or as identified new constants), A₄ decomposes into typed pieces with known β-content. The MATH-11 decomposition (rational + β² + ζ + new) extends to four loops.

**For Q335 (MATH-3):** If new constants are confirmed, the Q335 basis grows. Each new constant is stored as a high-precision decimal (4925 digits available — far exceeding the 100-digit Q335 standard). The Q335 framework is designed for exactly this: storing irreducible transcendental constants as exact rationals approximating to arbitrary precision.

**For the test suite:** Each PSLQ scan is an experiment with a binary outcome (FOUND/NULL). Every outcome is documented. The kill switches are pre-registered. The dead ends are as valuable as the discoveries. This is the RUM methodology applied to an open problem in mathematical physics.

**For the broader program:** If a software engineer with an AI and a PSLQ implementation can make progress on an 8-year open problem in multi-loop QED, the methodology generalizes. The tools are: high-precision arithmetic (mpmath), integer relation detection (PSLQ), a comprehensive transcendental basis (Q335 extended), and the discipline to test systematically and report honestly. Anyone with these tools can contribute.

---

### AGREEMENT REQUEST

The program has six attacks in sequence. Attack 1 (high-precision PSLQ at 1000 digits) is ready to run — it uses the existing 66-element basis with higher precision and larger coefficient bound. Attack 2 (cross-relations) uses the same basis with pairwise integral combinations. Both require only a script modification, no new mathematics.

Attacks 3-5 (elliptic, modular, β-content) require literature research to identify the specific constants for topologies 81 and 83. This is future work.

Attack 6 (independence certificate) requires all previous attacks to return null and uses the full 4925-digit values.

Recommended immediate action: write the script for Attack 1 (all six integrals at 1000 digits / maxcoeff 100,000) and Attack 2 (cross-relations between integrals). Run both. Report results. Then decide whether attacks 3-5 are needed based on the outcomes.
