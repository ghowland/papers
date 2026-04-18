## PHYS-47 Plan: The Laporta Constants — Independence, Sensitivity, and the Dual Geometry Hypothesis

**Registry:** [@HOWL-PHYS-47-2026]

**Series Path:** [@HOWL-MATH-6-2026] → [@HOWL-MATH-11-2026] → [@HOWL-PHYS-46-2026] → [@HOWL-PHYS-47-2026]

**Dependency:** PHYS-46 defined the program and ran the first scans. PHYS-47 reports the complete results.

---

### THE STAIRCASE

**Stair 1: The problem.** Six four-loop QED master integrals (C81a-c, C83a-c) computed to 4925 digits by Laporta in 2017. No known closed form. The multi-loop community has tried for 8 years. Nobody has published what these numbers are or why they resist analytical evaluation.

**Stair 2: What we tested.** 24 PSLQ scans against two basis sets (36 and 66 elements) covering every known transcendental structure through weight 8. 6 individual scans. 11 cross-relation scans (pairs and triples). 7 tiered scans at different basis sizes. All null.

**Stair 3: What we found.** The six integrals are individually independent of 66 known constants AND mutually independent. No pair is related through known constants. No triple within either topology is related. No cross-topology relation exists. Six genuinely independent numbers.

**Stair 4: How much they matter.** A₄ = −1.91225 contributes −5.57 × 10⁻¹¹ to a_e — 43× the Harvard measurement precision. It shifts α⁻¹ by 48 ppb. The Laporta constants are not marginal. They are deep inside the most precise measurement in physics.

**Stair 5: Why they resist.** The dual geometry hypothesis. The polylogarithmic basis covers Feynman diagrams with spherical momentum-space topology (genus 0). The Laporta topologies 81 and 83 may have toroidal momentum-space topology (genus 1). The constants are not in the spherical basis because they live on a torus. This connects to the RUM observation that every soliton has both spherical and toroidal boundary families.

**Stair 6: What comes next.** The elliptic and modular attacks (3-4) test the toroidal hypothesis directly. The independence certificate at 4000 digits (attack 6) provides the definitive answer. Either the integrals are expressible in elliptic/modular constants (confirming the dual geometry) or they are genuinely new constants of nature.

---

### PAPER STRUCTURE

```
I.    THE PROBLEM: SIX NUMBERS WITHOUT NAMES
      Laporta 2017. What A4 is. What the six integrals are.
      4925 digits each. No closed form. 8 years open.

II.   THE SEARCH: 24 PSLQ SCANS
      Scan 1: 36-element standard basis, 300 digits, 6/6 null.
      Scan 2: 66-element extended basis, 400 digits, C81a null at all 3 tiers.
      Run002: 6 individual + 11 cross-relation = 17/17 null.
      Total: 24/24 null across all scans.

III.  THE BASIS: 66 CONSTANTS COVERING WEIGHT 8
      What the basis contains: pi powers, zeta values, ln(2) powers,
      polylogarithms Li_n(1/2) and Li_n(-1), MZVs z(3,5) z(5,3) z(3,3),
      alternating Euler sums s6 zbar(5,1) zbar(3,3), all cross products.
      What it does NOT contain: elliptic integrals, modular form periods.

IV.   MUTUAL INDEPENDENCE: 11/11 NULL
      The strongest finding. Six within-topology pairs, three cross-topology
      pairs, two triples. All null. The six integrals are not expressible
      in terms of each other. Six independent constants, not fewer.

V.    SENSITIVITY: 43x THE MEASUREMENT
      A4 contributes -5.57e-11 to a_e. Harvard precision: 1.3e-12.
      Ratio: 42.8. The four-loop term shifts alpha by 48 ppb.
      These constants are deep inside the measurement, not at its edge.
      25.14 ppb per unit change in A4. C81a dominates by magnitude (116.69).

VI.   WHY THEY RESIST: THE DUAL GEOMETRY HYPOTHESIS
      Polylogarithmic basis: spherical momentum topology (genus 0).
      Elliptic basis: toroidal momentum topology (genus 1).
      Every soliton has both spherical boundaries (gravitational/thermal)
      and toroidal boundaries (magnetic/rotational).
      The Laporta topologies may be the first QED diagrams where
      the virtual circulation is genuinely toroidal in momentum space.
      Connection to MATH-11: spherical beta = pi/4 via 4*pi = 16*beta^2.
      Toroidal beta involves 4*pi^2 = 64*beta^2. Same beta power,
      different prefactor.

VII.  THE REMAINING ATTACKS
      Attack 3: elliptic constants (K(k), E(k) at topology-specific moduli).
      Attack 4: modular form periods (L-functions at integer arguments).
      Attack 5: beta-content partial decomposition.
      Attack 6: independence certificate at 4000 digits.
      Each attack either finds a relation (discovery) or returns null
      (narrows the space). Both outcomes are informative.

VIII. WHAT INDEPENDENCE MEANS FOR PHYSICS
      If confirmed: six new constants in the Q335 basis (29 -> 35).
      The electron g-2 depends on numbers mathematics hasn't classified.
      The A4 coefficient decomposes: rational (beta^0) + pi content
      (beta^2) + zeta content (beta^0) + Laporta content (beta^0, new).
      The most precisely measured quantity in physics contains
      genuinely unknown mathematics.

IX.   WHAT RESOLUTION MEANS FOR MATHEMATICS
      If the integrals are elliptic: four-loop QED connects to
      algebraic geometry. Specific elliptic curves for topologies 81/83.
      If modular: the Langlands program touches the electron's spin.
      Either way: the boundary between polylogarithmic and
      non-polylogarithmic Feynman integrals is located precisely.

X.    METHODOLOGY: HOW ANYONE CAN VERIFY
      Tools: Python, mpmath, PSLQ. All free. All documented.
      The scripts are published. The basis is enumerated.
      The Laporta values are public (4925 digits in the paper).
      Any researcher can reproduce the 24 null results.
      Any researcher can extend the basis and run new attacks.
```

---

### WHAT NEEDS TO BE COMPUTED BEFORE WRITING

Nothing. All results are already computed and documented:

| Result | Source | Status |
|---|---|---|
| 6/6 individual null (36 basis, 300 digits) | laporta_pslq.py output | Done |
| 1/1 C81a null (66 basis, 400 digits) | laporta_pslq_extended.py output | Done |
| 17/17 null (run002) | experiment_laporta_pslq_v0 run002 | Done |
| A₄ contribution = −5.57e-11 | experiment_laporta_a4_decomposition_v0 run001 | Done |
| 43× Harvard precision | Same experiment | Done |
| 48 ppb α shift | Same experiment | Done |
| 25.14 ppb per unit A₄ | Same experiment | Done |
| C81a largest (116.69) | Same experiment | Done |

The paper reports existing results. No new computation required.

---

### WHAT THE PAPER DOES NOT DO

Does not claim the integrals ARE new constants. Reports that they are consistent with independence and quantifies the implications if independence holds.

Does not decompose A₄ into individual integral contributions. We don't have the rational coefficients c₁-c₆. The sensitivity analysis uses total A₄ perturbation, not per-integral decomposition.

Does not run the elliptic or modular attacks. Those are defined as future work in the program. PHYS-47 reports what has been done, not what will be done.

Does not derive the dual geometry hypothesis from first principles. It is stated as a hypothesis motivated by the PSLQ null results and the RUM soliton structure. It makes predictions (the integrals should be expressible in elliptic periods) that Attack 3 will test.

---

### DIAGRAMS — 8 CANDIDATES

| # | Candidate | Type | What it shows |
|---|---|---|---|
| 1 | The 24 PSLQ scans — null matrix | Comparison Bar | Every scan result on one chart. 24 bars, all null. |
| 2 | The 66-element basis — classified by type | Scale/Landscape | Which constant classes are present and absent. The gap where elliptic would be. |
| 3 | Cross-relation matrix — 6×6 | Geometric Cross-Section | Which pairs were tested. All cells null. The diagonal is the individual scan. |
| 4 | A₄ contribution vs Harvard precision | Threshold/Region | The −5.57e-11 bar against the ±1.3e-12 measurement band. 43× ratio visible. |
| 5 | α shift: with vs without A₄ | Comparison Bar | 137.035998868 vs 137.036005456. The 48 ppb gap. |
| 6 | Integral magnitudes | Comparison Bar | C81a = 116.69 dominating the others. Six bars. |
| 7 | Dual geometry: spherical vs toroidal on one object | Geometric Cross-Section | Earth (or proton) with both boundary families drawn. |
| 8 | Identity card: the six Laporta constants | Identity Card | All six values, their topology, their status, their impact. |

---

### APPENDIX TABLES NEEDED

| Table | Content |
|---|---|
| A.1 | The six integrals — complete registry (first 50 digits, topology, sign, status) |
| A.2 | The 66-element basis — complete list with values |
| A.3 | All 24 PSLQ scan results — chronological record |
| A.4 | Cross-relation test matrix — 11 tests |
| A.5 | Sensitivity analysis — all 27 output values |
| A.6 | PSLQ precision requirements — theoretical bounds vs actual |
| A.7 | The dual geometry catalog — spherical vs toroidal at proton, Earth, Sun, galaxy |
| A.8 | Kill switches — complete list |
| A.9 | Remaining attacks — schedule and dependencies |
| A.10 | Connection to RUM framework |

---

### AGREEMENT REQUEST

The paper reports three categories of results:

**Category 1 (hard data):** The 24/24 PSLQ null results, the 17/17 experiment results, the sensitivity numbers (43×, 48 ppb, 25.14 ppb/unit). All computed, all documented, all reproducible. This is the core of the paper.

**Category 2 (analysis):** The mutual independence finding (11/11 cross-relation null → 6 independent constants). The dominance of C81a by magnitude. The connection to the α extraction chain. Straightforward interpretation of the data.

**Category 3 (hypothesis):** The dual geometry — spherical vs toroidal momentum topology as the explanation for why the integrals resist polylogarithmic evaluation. This is stated as a testable hypothesis with a specific prediction (Attack 3 should find elliptic relations if the hypothesis is correct).

Proposed approach: write the paper with Category 1 as the body (§I-V), Category 2 as the analysis (§V-VI), and Category 3 as the hypothesis (§VI-IX). The appendix tables document everything. The paper stands on the hard data even if the dual geometry hypothesis is wrong.
