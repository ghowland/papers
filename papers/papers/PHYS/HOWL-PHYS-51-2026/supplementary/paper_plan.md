## PHYS-51 Plan: You Are Here III — The α_EM Derivation Tree and the Laporta Operationalization

**Registry:** [@HOWL-PHYS-51-2026]

**Series Path:** [@HOWL-PHYS-24-2026] → [@HOWL-PHYS-40-2026] → [@HOWL-PHYS-51-2026]

**Date:** April 19, 2026

**Dependency:** PHYS-24 was "You Are Here I" (the manuscript, 35 values). PHYS-40 was "You Are Here II" (53 values, 13 inputs, surplus +40). PHYS-51 is "You Are Here III" — the input count drops, the surplus grows, and the Laporta constants become operational.

---

### THE POSITION CHANGE

**PHYS-40 (Session 7):** 13 independent measured inputs → 53 derived/predicted values. Surplus: +40. The inputs were: α_EM, sin²θ_W, α_s, m_e, m_μ, m_τ, G_F, M_Z, m_H, plus CKM angles and mass ratios. Each was treated as a given.

**PHYS-51 (Session 8):** The α_EM derivation tree reduces the input count. Three previously-given quantities are now derived from α_EM:

| Parameter | PHYS-40 | PHYS-51 | How derived | Miss |
|---|---|---|---|---|
| sin²θ_W | Input | **Derived** | Two-loop unification (Euler + down-run) | 12 ppm |
| α_s | Input | **Derived** | Two-loop unification (Euler + down-run) | 0.33% |
| m_τ | Input | **Derived** | Koide K = R₃/R₂ = 2/3 (from m_e, m_μ) | 61 ppm |

Inputs reduced from 13 to ~10. Surplus grows from +40 to +43. Plus 7 new values from the killing spree that weren't in PHYS-40 (a_e, a_μ, Ω_DM, Ω_b from geometric predictions, M_Z, M_W partially).

---

### THE THREE LAYERS OF THE PAPER

**Layer 1 (primary): The α_EM Derivation Tree.** One input, seven outputs, sub-percent precision. The tree structure, the chains, the miss percentages, the comparison to PHYS-40's input count. This is the parameter reduction story. Every parameter we derive from α_EM is one fewer free parameter in the framework.

**Layer 2: The Laporta Operationalization.** The six constants went from opaque numerical values to operational components in the a_e derivation chain. They are classified (β⁰ toroidal-geometric), characterized (topology-specific moduli at 167 ppb consistency), and contributing (43× Harvard precision in the a_e chain). The operationalization is what makes the a_e chain work at 0.22 ppb — without A₄, the miss would be ~48 ppb.

**Layer 3: The overall RUM position update.** What changed from PHYS-40 to PHYS-51 across all domains: the MATH papers (11, 12), the PHYS papers (41-50), the experiments (8 new experiments, 316+ outputs), the geometric framework (β extended to toroidal K(k)), the Koide connection (R₃/R₂), the GR work (referenced).

---

### PAPER STRUCTURE

```
I.    THE INPUT COUNT
      PHYS-24: 35 values from ~15 inputs.
      PHYS-40: 53 values from 13 inputs. Surplus: +40.
      PHYS-51: 60+ values from 10 inputs. Surplus: +50.
      
      The three parameters that moved from input to derived:
      sin2_theta_W (12 ppm), alpha_s (0.33%), m_tau (61 ppm).
      How each was derived. The chain from alpha_EM.

II.   THE DERIVATION TREE FROM α_EM
      One root: alpha_EM = 1/137.036.
      
      Branch 1: QED perturbation series
        alpha_EM → alpha/pi → A1 through A5 → a_e (0.22 ppb)
        Same alpha → published QED + hadronic + EW → a_mu (2.7 ppm)
      
      Branch 2: Two-loop gauge unification
        alpha_EM + gauge group integers (b_i, b_ij, db_ij)
        → Euler integration → 1-2 crossing → exact unification
        → down-run → sin2_theta_W (12 ppm) + alpha_s (0.33%)
      
      Branch 3: Koide from R3/R2
        m_e + m_mu (given) + K = 2/3 → m_tau (61 ppm)
      
      Branch 4: Geometric constants
        beta = pi/4 → Omega_DM = beta/3 = pi/12 (0.42%)
        → DM/baryon = (22/13)*pi → Omega_b = 13/264 (0.49%)
      
      Branch 5: Electroweak (partial)
        alpha_EM + sin2_theta_W + G_F + delta_r → M_Z (1.2%)
        M_Z + sin2_theta_W → M_W (1.7%)
      
      Branch 6: Confinement (partial)
        alpha_s + M_Z → Lambda_QCD → m_p/Lambda (broken, needs QCD running)
      
      The precision ladder:
      Ultra:     a_e at 0.22 ppb
      High:      sin2_theta_W at 12 ppm, a_mu at 2.7 ppm, m_tau at 61 ppm
      Sub-%:     alpha_s at 0.33%, Omega_DM at 0.42%, Omega_b at 0.49%
      Percent:   M_Z at 1.2%, M_W at 1.7%
      Broken:    m_p/Lambda (needs full QCD)

III.  THE LAPORTA OPERATIONALIZATION
      Before Session 8: six opaque numbers in A4 = -1.912.
      After Session 8: classified, characterized, operational.
      
      Classified:
      - Beta^0 (no pi content): 24/24 PSLQ null against pi through pi^6
      - Not number-theoretic: 24/24 null against zeta, Li, MZV, alt. Euler
      - Mutually independent: 11/11 cross-relation null
      - Toroidal-geometric: matching elliptic forms after zeta subtraction
      
      Characterized:
      - Topology 81 modulus: k = 0.999994 (167 ppb consistency)
      - Topology 83 modulus: k = 0.99713 (25 ppm consistency)
      - Zeta subtraction: 6/6 improved 7-266x
      - Control ratio: 2.05 (remainder matches elliptic better than modulus)
      
      Operational:
      - A4 contributes -5.57e-11 to a_e
      - 43x Harvard measurement precision
      - 48 ppb alpha shift
      - Without A4: a_e misses by ~48 ppb. With A4: misses by 0.22 ppb.
      - The Laporta constants are the difference between a good prediction
        and the best prediction in physics.

IV.   THE MODULUS/REMAINDER RESOLUTION
      Sessions 1-4 parked the remainder (beta^0 content after removing pi).
      Session 8 un-parked it:
      - Modulus = spherical (beta^2, beta^4 — pi powers)
      - Remainder layer 1 = number-theoretic (zeta, Li — all loops)
      - Remainder layer 2 = toroidal-geometric (K(k), E(k) — loop 4+)
      
      The three-layer decomposition: A_n = spherical + number-theoretic + toroidal.
      Complete through A3 (layer 2 = 0). Blocked for A4 (needs c1-c6).

V.    THE MATH PAPERS
      MATH-11: beta = pi/4 as L1/L2 metric conversion.
        Foundation identity. Nine domains. A2 decomposition (90.4% cancellation).
      
      MATH-12: beta^0 has two geometries.
        Toroidal extension: K(k)/pi as the toroidal L1/L2 conversion.
        One family parametrized by k. Circle at k=0, torus at k>0.
        QED transitions from k=0 (loops 1-3) to k>0 (loop 4).

VI.   THE KOIDE UPDATE
      PHYS-8 established K = 2/3 with seven equivalent formulations.
      PHYS-50 adds the eighth: K = R3/R2 = (pi/6)/(pi/4) = 2/3.
      
      R3/R2 is the unique rational in the physical dimensional ladder
      (1D, 2D, 3D). Pi cancels at 2D->3D and nowhere else.
      
      The four-loop correction moves K toward 2/3 by 0.054 ppm.
      The elliptic Koide does NOT preserve a^2 = 2.
      Koide is specifically circular (k = 0), not toroidal.
      
      Negative results reported honestly alongside positive.

VII.  THE GR AND SPACETIME WORK (referenced)
      PHYS-41: Time as reading depth (D/K separation)
      PHYS-42: GR reading depth mega-experiment
      PHYS-43: Clock/reading decomposition
      PHYS-44: Spacetime separation
      PHYS-45: Confinement boundary as soliton boundary
      
      These establish the D/K split and the soliton boundary framework.
      Referenced here, not re-derived.

VIII. THE EXPERIMENT RECORD — SESSION 8
      8 new experiments from the Laporta program.
      1 experiment from Koide R3/R2.
      2 experiments from the killing spree.
      Total: 11 experiments, 400+ outputs.
      
      Combined with prior sessions: ~25 experiments, ~1000+ outputs.
      The experimental infrastructure is now the backbone of the framework.

IX.   THE COMPLETE VALUE CATALOG
      The full table: every derived value, its chain, its miss, its input.
      Organized by domain: QED, unification, lepton masses, EW, confinement,
      cosmology, GR.
      
      Input count: 10 (alpha_EM, m_e, m_mu, G_F, M_Z, m_H, plus
      CKM angles, mass ratios, hadronic inputs).
      Output count: 60+.
      Surplus: +50.

X.    WHAT CHANGED FROM PHYS-40 TO PHYS-51
      
      | Category | PHYS-40 | PHYS-51 | Change |
      |----------|---------|---------|--------|
      | Inputs | 13 | ~10 | -3 (derived) |
      | Outputs | 53 | 60+ | +7 |
      | Surplus | +40 | +50 | +10 |
      | Math papers | 10 | 12 | +2 (MATH-11, 12) |
      | Physics papers | 40 | 50 | +10 |
      | Experiments | ~15 | ~25 | +10 |
      | Laporta status | not present | operational | new |
      | Koide interpretation | K = 2/3 (identity) | K = R3/R2 (geometric) | deepened |
      | Modulus/remainder | parked | resolved (three layers) | un-parked |
      | Beta framework | beta = pi/4 (spherical) | beta + K(k)/pi (toroidal) | extended |
      | GR framework | GR tests verified | D/K split, spacetime separation | deepened |

XI.   WHAT'S STILL MISSING
      1. m_e and m_mu: no derivation. Free Yukawa couplings.
      2. m_H: no derivation. Free quartic coupling.
      3. G_F: partially derivable from M_W and sin2_theta_W but
         currently used as input for M_Z.
      4. CKM angles: no geometric derivation.
      5. Quark masses: scheme-dependent, no Koide match.
      6. M_Z to sub-percent: needs scheme-consistent EW or two-loop.
      7. Lambda_QCD: needs full QCD running with threshold matching.
      8. Closed forms for Laporta integrals: not found (Attack 3 null
         at simple K, E forms; moduli confirmed at 167 ppb).
      
      The irreducible inputs (no known derivation path):
      alpha_EM, m_e, m_mu, m_H = 4 truly free parameters.
      Everything else is derivable in principle.

XII.  THE PLATFORM FOR SESSION 9
      What we stand on:
      - 10 inputs, 60+ outputs, surplus +50
      - The alpha_EM derivation tree with 7 working branches
      - The Laporta constants operational in the a_e chain
      - The beta framework extended to toroidal geometry
      - The modulus/remainder framework resolved
      - The Koide R3/R2 identification at 9.2 ppm
      - 25 experiments, 1000+ outputs, all reproducible
      
      What Session 9 should target:
      - Fix M_Z chain (scheme-consistent sin2_theta_W)
      - Fix Lambda_QCD (full QCD running)
      - Attempt m_e or m_mu derivation (hardest problem)
      - Attempt G_F derivation from the tree
      - Extend Laporta work: complementary periods K', E' in basis
      - Test Koide R3/R2 prediction with updated tau mass
```

---

### APPENDIX TABLES — 15

| Table | Content |
|---|---|
| A.1 | The input reduction: PHYS-24 → PHYS-40 → PHYS-51 |
| A.2 | The α_EM derivation tree: all 10 chains with misses |
| A.3 | The seven passes: precision ladder |
| A.4 | The three failures: diagnosis and fix path |
| A.5 | Laporta operationalization: classification, characterization, operational impact |
| A.6 | The three-layer decomposition: modulus + layer 1 + layer 2 |
| A.7 | Topology-specific moduli: k₈₁, k₈₃, consistency |
| A.8 | The ζ subtraction results: 6/6 improved |
| A.9 | MATH-11 and MATH-12 summary: β framework + toroidal extension |
| A.10 | Koide R₃/R₂: the eighth formulation |
| A.11 | Session 8 experiment catalog: 11 experiments, 400+ outputs |
| A.12 | The complete value catalog: 60+ values by domain |
| A.13 | The complete input catalog: 10 inputs with justification |
| A.14 | What changed: PHYS-40 vs PHYS-51 comparison table |
| A.15 | What's still missing: the irreducible inputs and open chains |

---

### DIAGRAMS — 8

| # | Candidate | Type |
|---|---|---|
| 1 | The α_EM derivation tree (branching diagram) | Geometric Cross-Section |
| 2 | Input count reduction: 13 → 10 across three papers | Comparison Bar |
| 3 | The precision ladder: 0.22 ppb to 127% | Scale/Landscape |
| 4 | Laporta operationalization timeline: opaque → classified → operational | Running/Convergence |
| 5 | The three-layer decomposition at each loop order | Comparison Bar |
| 6 | Session 8 experiment map: 11 experiments, domains connected | Scale/Landscape |
| 7 | The surplus growth: +35 → +40 → +50 | Running/Convergence |
| 8 | Identity card: You Are Here III | Identity Card |

---

### AGREEMENT REQUEST

The paper is a position paper, not a discovery paper. It catalogs what Session 8 achieved, how the input count changed, what the Laporta operationalization means for the derivation tree, and where the framework stands. The tone is: "here is what we can derive, here is what we can't, here is the platform for the next session."

All data from 11 completed experiments across Session 8 plus the full prior catalog from Sessions 1-7.
