# Working Document: CKM Mixing Angles from Quark Inertia Ratios

## Status: NOTEBOOK — Not Published, Not in Series

## Purpose: Complete state capture for future session pickup

---

## I. THE OBSERVATION

Three CKM mixing angles correspond to square roots of quark inertia ratios:

| CKM angle | Relation | Computed | Measured | Precision |
|---|---|---|---|---|
| sin θ₁₂ = 0.2253 | √(m_d/m_s) | 0.2236 | 0.2253 | −0.75% |
| sin θ₂₃ = 0.0412 | √(m_u/m_c) | 0.04124 | 0.0412 | +0.10% |
| sin θ₁₃ = 0.00350 | √(m_u/m_t) | 0.003537 | 0.00350 | +1.05% |

All three match within quark mass uncertainties. Tension is ~0σ for all three because quark mass uncertainties dominate at 10–20%.

---

## II. THE PATTERN

- θ₁₂ (1st–2nd generation mixing): **down-type** inertia ratio, m_d/m_s
- θ₂₃ (2nd–3rd generation mixing): **up-type** inertia ratio, m_u/m_c
- θ₁₃ (1st–3rd generation mixing): **up-type** inertia ratio, m_u/m_t

The pattern is mixed: down-type for θ₁₂, up-type for θ₂₃ and θ₁₃. This is NOT the standard Fritzsch pattern (which uses same-sector adjacent-generation ratios throughout).

**Standard Fritzsch (all down-type) FAILS:**

| Fritzsch prediction | Value | vs measured | Status |
|---|---|---|---|
| sin θ₁₂ = √(m_d/m_s) | 0.2236 | sin12 = 0.2253 | Works (−0.75%) |
| sin θ₂₃ = √(m_s/m_b) | 0.1495 | sin23 = 0.0412 | FAILS (+263%) |
| sin θ₁₃ = √(m_d/m_b) | 0.0334 | sin13 = 0.00350 | FAILS (+855%) |

Our cross-sector pattern works where standard Fritzsch fails.

---

## III. INDEPENDENCE ANALYSIS

Relations 2 and 3 share m_u in the numerator:

sin θ₁₃ / sin θ₂₃ = √(m_u/m_t) / √(m_u/m_c) = √(m_c/m_t)

Check: sin₁₃/sin₂₃ = 0.08495 versus √(m_c/m_t) = 0.08576. Difference: −0.94%.

Therefore only TWO relations are independent:
1. sin θ₁₂ = √(m_d/m_s) — down-type constraint
2. sin θ₂₃ = √(m_u/m_c) — up-type constraint

The third (sin θ₁₃ = √(m_u/m_t)) is a consistency check, not a new constraint.

**Parameter reduction: 17 → 15** (two CKM angles determined by quark masses, δ_CP remains free).

---

## IV. THE PRECISION FLOOR

This observation is fundamentally different from Koide and θ_QCD:

| Result | Match precision | Input precision | Tension |
|---|---|---|---|
| θ_QCD = 0 | Exact | 10⁻¹⁰ | — (exact by measurement) |
| Koide m_τ | 0.0009% | 6–10 sig fig | 0.91σ |
| sin θ₁₂ = √(m_d/m_s) | 0.75% | ~10% (m_d) | 0.11σ |
| sin θ₂₃ = √(m_u/m_c) | 0.10% | ~20% (m_u) | ~0σ |
| sin θ₁₃ = √(m_u/m_t) | 1.05% | ~20% (m_u) | ~0σ |

The quark mass uncertainties (~10–20% for light quarks) make all three CKM-mass relations ~0σ. We cannot distinguish "exact" from "10% off" from "coincidence" with current data. The relations could be exact or could be approximate and we have no way to tell until quark mass measurements improve dramatically.

Koide is testable because lepton masses are known to 6–10 significant figures. The CKM-mass relations are not currently testable at precision because quark masses are known to 1–2 significant figures for light quarks.

---

## V. WHAT IS NOT KNOWN

**Literature status:** The GST relation sin θ_C = √(m_d/m_s) is known since 1960. The specific identification sin θ₂₃ = √(m_u/m_c) (rather than √(m_s/m_b)) is characteristic of certain texture-zero models where the up-type Yukawa matrix carries the texture zeros. Whether the specific three-relation mixed pattern (down for θ₁₂, up for θ₂₃, up for θ₁₃) has been stated as a unified observation is unknown. **A literature search of the texture-zero literature (Fritzsch 1977, Ramond-Roberts-Ross 1993, others) is required before any paper is written.**

**Structural explanation for the mixed pattern:** Why does θ₁₂ use down-type quarks while θ₂₃ and θ₁₃ use up-type? The soliton/inertia framework from PHYS-1 does not currently distinguish up-type from down-type in a way that would predict this. No derivation exists.

**Why the lightest quark appears as numerator in each relation:** The pattern is always √(lightest / heavier) within one charge sector. The lightest up-type quark (u) appears in both up-type relations. The lightest down-type quark (d) appears in the down-type relation. Why the lightest quark of each sector plays this role is not derived.

---

## VI. THE INERTIA FRAMING

In the PHYS-1 framework, mass is inertia — resistance to acceleration of a coherent vortex pattern. The CKM-mass relations in this language:

Each CKM mixing angle between generations is the square root of an inertia ratio — the lightest quark pattern's resistance divided by a heavier quark pattern's resistance, within one charge sector.

- θ₁₂: How much the lightest down-type vortex (d) resists compared to the next heavier (s)
- θ₂₃: How much the lightest up-type vortex (u) resists compared to the next heavier (c)
- θ₁₃: How much the lightest up-type vortex (u) resists compared to the heaviest (t)

The mixing strength between generations is determined by how different the patterns' inertias are. Larger inertia ratios (lighter/heavier further apart) give smaller mixing angles. This is physically intuitive: patterns with very different resistances mix weakly.

---

## VII. NUMERICAL RESULTS FOR FUTURE REFERENCE

```
Quark inertias (MSbar at 2 GeV, all Fraction):
  m_u = 54/25 = 2.16 MeV (unc +0.49/-0.26, ~20%)
  m_d = 467/100 = 4.67 MeV (unc +0.48/-0.17, ~10%)
  m_s = 467/5 = 93.4 MeV (unc +8.6/-3.4, ~9%)
  m_c = 1270 MeV (unc ±20, ~1.6%)
  m_b = 4180 MeV (unc +30/-20, ~0.6%)
  m_t = 172690 MeV (unc ±300, ~0.2%)

CKM angles (all Fraction):
  sin12 = 2253/10000 = 0.2253 (unc ±0.0007)
  sin23 = 103/2500 = 0.0412 (unc ±0.0008)
  sin13 = 7/2000 = 0.00350 (unc ±0.00014)

Computed ratios (all Fraction, controlled-precision sqrt):
  sqrt(m_d/m_s) = 0.223607
  sqrt(m_u/m_c) = 0.041241
  sqrt(m_u/m_t) = 0.003537
  sqrt(m_c/m_t) = 0.085757

Consistency check:
  sin13/sin23 = 0.084951 vs sqrt(m_c/m_t) = 0.085757 (-0.94%)
```

---

## VIII. SCRIPT

`gst_extended.py` — all inputs Fraction, controlled-precision sqrt, tests all three relations plus independence check and Fritzsch comparison. In /home/claude/. Not in outputs (notebook entry, not deliverable).

---

## IX. SCORECARD

| Result | Status | Paper | Reduction |
|---|---|---|---|
| θ_QCD = 0 | Derived (ground state) | PHYS-7 | 19 → 18 |
| Koide constant = 2/N_gen | Derived (trig identity) | PHYS-8 | 18 → 17 (conditional) |
| λ ≈ g'² | Observation (1.0%) | Notebook | 17 → 16 (blocked — no derivation) |
| CKM from mass ratios | Observation (0–1%) | Notebook | 17 → 15 (blocked — precision floor + no derivation) |

Confirmed reductions: 19 → 18 (θ = 0).
Conditional reductions: 18 → 17 (Koide, 0.91σ consistent).
Blocked leads: 17 → 15 (CKM-mass, precision floor), 17 → 16 (λ = g'², no derivation).

---

## X. WHAT WOULD UNBLOCK THESE

**CKM-mass relations → paper:** Either (a) literature search confirms the mixed pattern is novel AND a structural derivation of the mixed up/down pattern is found, or (b) lattice QCD improves light quark mass precision to ~1%, making the relations testable at Koide-level precision.

**λ = g'² → paper:** Either (a) the impedance matching condition is derived rigorously from the soliton boundary framework, or (b) a full one-loop on-shell computation confirms the relation at sub-percent after corrections.

Both leads are real. Both are blocked by specific, identifiable obstacles. Both have clear paths to resolution. Neither is ready for publication.

---

## XI. TAGS FOR FUTURE RETRIEVAL

- Gatto-Sartori-Tonin, Cabibbo angle, CKM matrix, quark mixing
- sin theta_12 = sqrt(m_d/m_s), sin theta_23 = sqrt(m_u/m_c), sin theta_13 = sqrt(m_u/m_t)
- Mixed pattern: down-type for theta_12, up-type for theta_23 and theta_13
- Fritzsch texture zeros, up-type texture, cross-sector pattern
- Independence: two constraints, third is consistency check
- Precision floor: quark masses at 10-20% prevent precision test
- Literature search needed: texture-zero models 1977-2000
- Parameter reduction: 17 → 15 if exact
- PHYS-1 inertia framing: mixing angle = sqrt(inertia ratio)

---

**END WORKING DOCUMENT**

**Status:** Notebook entry. Not in series. Not published.
**Blocked by:** Quark mass precision floor (~10-20%), unknown literature status, no structural derivation of mixed up/down pattern.
**Pickup instructions:** Load this document plus PHYS-1, PHYS-7, PHYS-8. The three-relation pattern is the content. Literature search for the specific mixed pattern is the first step before any paper. If novel, the parameter reduction 17 → 15 and the Fritzsch comparison are the paper. If known, we have nothing to add beyond the integer arithmetic computation.

