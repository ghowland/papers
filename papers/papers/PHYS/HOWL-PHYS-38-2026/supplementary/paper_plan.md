Let me check what PHYS-37 covered to know the boundary.That's a massive transcript. I have what I need. PHYS-37 covered 17 derived values through the bridge experiments (bridges 1-10) and one-loop EW corrections (v0 and v1). Everything since then is new material for PHYS-38.

## PHYS-38 Paper Plan

**Title:** "Precision Frontier: 38 Derived Values from Sub-ppb QED to the Lithium Problem"

**Registry:** [@HOWL-PHYS-38-2026]

**Series Path:** PHYS-9 → PHYS-36 → PHYS-37 → PHYS-38

---

### What's New Since PHYS-37

PHYS-37 ended at 17 derived values. This session added 21 more through 5 experiments covering 4 attack paths:

| Path | Experiment | New Values | Key Result |
|---|---|---|---|
| Path 1 (EW v2) | `experiment_ew_v2_v0` | 11 | M_W from G_F at 195 ppm, all Z partial widths, R_l, N_gen |
| Path 2 (QED corrections) | `experiment_qed_full_corrections_v0` | 4 improved | α at 0.22 ppb (18× improvement), 12-digit Rb agreement |
| Path 3 (Muon g-2) | `experiment_muon_g2_v0` | 3 | 6.5σ anomaly reproduced, hadronic VP dominates |
| Path 4 (BBN extended) | `experiment_bbn_extended_v0` | 3 | Lithium problem at 2.96×, He-3 at 0.36σ |
| Path 5 (CKM from CD) | `experiment_ckm_cd_mixing_v0` | 4 | First-row deficit at 0.83σ, 4×4 unitarity |

---

### Proposed Structure

**§I. Abstract** — 38 values, 7 domains, sub-ppb to percent precision. Five new experiments since PHYS-37. α improved 18× to 0.22 ppb. M_W from two independent paths agreeing to 207 ppm. Muon g-2 anomaly reproduced. Lithium problem reproduced. CKM deficit explained by CD at 0.83σ.

**§II. The EW v2 Experiment — G_F as Input** — Flipped logic. Published Δr = 0.03692 (Stål/Weiglein/Zeune 2015). M_W from Sirlin relation at 195 ppm. sin²θ_eff from on-shell M_W at 0.24%. All 11 Z partial widths. R_l = 20.82 (0.27%). N_gen = 3.0 exact. M_W consistency: two paths agree to 207 ppm. The Δr story: decomposition failed (remainder wrong), total Δr from published value worked.

**§III. Sub-ppb QED — The 18× Improvement** — Seven published corrections (mass-dependent, hadronic, electroweak) totaling 4.872 × 10⁻¹² subtracted from measured a_e. Newton reinversion. α⁻¹ = 137.035999207 — 12-digit agreement with Rb recoil (0.007 ppb). R∞ at 0.44 ppb. α-power scaling preserved. The uncertainty budget shifts from our code to published corrections.

**§IV. The Muon g-2 Prediction** — α from §III feeds into a_μ(QED). Sum with hadronic and EW published corrections. a_μ(SM) = 116591741 × 10⁻¹¹. Fermilab: 116592059. Difference: 318 × 10⁻¹¹. Tension: 6.5σ. The alpha shift from our correction: −0.025 × 10⁻¹¹ — negligible. The anomaly is hadronic, not QED. CMD-3 / lattice tension discussed.

**§V. BBN Extended — Four Primordial Elements** — Same η₁₀ = 6.09 from gauge integers now predicts four elements. D/H at 0.12σ (prior). Y_p at 0.94σ (prior). He-3 at 0.36σ (new). Li-7 at 2.96× (new — the lithium problem). η required for Li-7 (1.40) incompatible with our η (6.09) — rules out η adjustment. Connection to primordial chemistry: H₂, HD, LiH formation from BBN products.

**§VI. CKM from the Cabibbo Doublet** — First connection between the CD and flavor physics. sin²θ₁₄ = 0.002025 vs measured deficit 0.00152 (0.83σ). V_ud from 4×4 unitarity at 264 ppm. Cabibbo angle shift 56 × 10⁻⁶. 4×4 unitarity sum 1.00050 (residual < 0.001). Three independent lines of CD evidence: gap ratio (exact), CKM deficit (0.83σ), coupling convergence (1.2%).

**§VII. The Complete Inventory** — All 38 derived values in one table. Precision distribution: 4 at sub-ppb, 8 at sub-permille, 10 at sub-percent, 3 at percent, 2 exact, 4 conditional, 3 anomalies (muon g-2, lithium, CKM overshoot). Seven physics domains.

**§VIII. The Connected Graph** — Updated island map. The continent now spans QED → EW → gauge → cosmology → nuclear → muon → flavor. Koide still floats. The graph has 38 nodes and ~25 edges. Every path that standard physics gets right, our chain gets right. Every anomaly standard physics has, our chain reproduces.

**§IX. What We Learned About the Experiment System** — The 5-run convergence on the QED corrections (wrong readers, classification nodes). The Δr decomposition failure and recovery. The R_l definition fix. The methodology for building experiments: search pool → write values → write experiment → write derivations → run → report. This is the DATA-6 development specification in action.

**§X. Falsification Update** — Updated criteria from PHYS-37 plus new ones. M_W two-path consistency at 207 ppm (PASS). Muon g-2 anomaly from standard hadronic inputs (correct behavior). Lithium problem from standard BBN (correct behavior). CKM deficit from CD (0.83σ, consistent).

**§XI. Forward Paths** — What remains from the 8-path attack plan. Path 6 (proton decay), Path 7 (two-loop α_s fix), Path 8 (Hubble running). Statistical control computation still blocking. Laporta convention mapping still parked.

---

### Key Tables

1. Complete 38-value inventory with domain, precision, source chain
2. PHYS-37 → PHYS-38 delta: what changed (17 → 38)
3. EW iteration history: tree → v0 → v1 → v2 for M_W, Γ_Z, G_F
4. QED corrections breakdown: 7 corrections with magnitudes and uncertainty budget
5. Muon g-2 budget: QED + hadronic + EW = SM prediction vs Fermilab
6. BBN scorecard: four elements, one η, three agreements, one problem
7. CKM 4×4 matrix structure with all mixing angles
8. Experiment run inventory: 5 experiments, run counts, derivation counts
9. Input accounting: 15 measured → 38 derived (23 more outputs than inputs)
10. Precision distribution by band

### Key Figures (8)

| Fig | Content | Type |
|---|---|---|
| 1 | α before/after corrections: 3.99 ppb → 0.22 ppb, with Rb/Cs/CODATA positions | Comparison |
| 2 | M_W from two paths converging on measured value | Convergence |
| 3 | Muon g-2 budget: stacked bar showing QED + had + EW vs measurement | Bar |
| 4 | BBN four elements: D/H, Y_p, He-3 (agree), Li-7 (problem) | Threshold/Region |
| 5 | CKM 4×4 unitarity: 3×3 deficit + sin²θ₁₄ = 1.00050 | Connection map |
| 6 | Precision landscape: 38 values on log scale (updated from PHYS-37) | Scale |
| 7 | Complete derivation graph: 7 domains connected | Progression |
| 8 | Identity card: 38 values, 7 domains, 15 inputs | Identity |

### Depends On

PHYS-36 (QED 5-loop), PHYS-37 (17 values, 5 domains), DATA-6 (experiment system)

### Data

5 experiments, 16 derivation functions, ~870 value nodes, 38 derived values
