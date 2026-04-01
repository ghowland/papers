# Working Document: sin²θ_W from 3/8 at GUT Scale — Running with Integer Coefficients

## Status: NOTEBOOK — Not Published, Not in Series

## Purpose: Complete state capture for future session pickup

---

## I. THE CALCULATION

Starting from sin²θ_W = 3/8 at the scale where α₁ = α₂ (SU(5) charge counting), run down to M_Z using one-loop SM beta functions.

### Inputs

| Input | Value | Type |
|---|---|---|
| α_EM(M_Z)⁻¹ | 63953/500 = 127.906 | Measured rational |
| α_s(M_Z) | 59/500 = 0.1180 | Measured rational |
| sin²θ_W(GUT) | 3/8 | Integer (SU(5) charge counting) |
| b₁ | 41/10 | Integer (particle counting, GUT normalization) |
| b₂ | −19/6 | Integer (particle counting) |
| b₃ | −7 | Integer (particle counting) |

### Version 1: Forced Three-Way Unification

Force α₁ = α₂ = α₃ at one scale. Two equations (α_EM and α₃ at M_Z), two unknowns (α_GUT⁻¹ and L = ln(M_GUT/M_Z)/(2π)).

**Result:** sin²θ_W(M_Z) = 0.2076. PDG: 0.23122. **Miss: −10.2%.** The SM particle content doesn't produce unification — same wall as the gap ratio.

### Version 2: The Linear Formula

Don't force three-way unification. Express sin²θ_W(M_Z) as a function of L_X (the α₁ = α₂ crossing scale parameter), using only α_EM(M_Z) as input.

Key identity: the denominator coefficient 5·B₁ + 3·B₂ vanishes exactly, where B₁ = b₁ − 11/8 = 109/40 and B₂ = b₂ − 11/8 = −109/24. This gives:

5·(109/40) + 3·(−109/24) = 109·(1/8 − 1/8) = 0

This is not dynamical — it's a consequence of α_EM⁻¹ = (5/3)·α₁⁻¹ + α₂⁻¹. The denominator in sin²θ_W is proportional to α_EM⁻¹ regardless of L.

**Result: sin²θ_W is exactly linear in L_X:**

**sin²θ_W(M_Z) = 3/8 − (109/72) · L_X / α_EM⁻¹(M_Z)**

where L_X = ln(μ_X/M_Z)/(2π) and μ_X is the α₁ = α₂ crossing scale.

### Version 3: What L_X reproduces the measurement?

L_X = 4.049 gives sin²θ_W = 0.23122, corresponding to μ_X = 10^13.01 GeV. At this crossing scale, if α₃ also unified there, α_s(M_Z) would be 0.071 — 40% below measured 0.1180. The gap ratio problem again.

---

## II. THE INTEGER CONTENT

| Integer | Origin | Role |
|---|---|---|
| 3/8 | SU(5) charge assignments: 3/(3+5) | GUT-scale sin²θ_W |
| 109 | 15·(b₁ − b₂) = 15·(218/30) | Running coefficient |
| 218 | Gap ratio numerator (PHYS-5) | = 2 × 109 |
| 115 | Gap ratio denominator (PHYS-5) | = (b₂ − b₃)·30 |
| 72 | = 8 × 9 = 8 × 3² | Denominator in running coefficient |

The number 109 appears as b₁ − b₂ in natural units (specifically, 109/15 = b₁ − b₂ exactly). It connects to the gap ratio: the gap ratio numerator 218 = 2 × 109. The running of sin²θ_W from 3/8 and the gap ratio between couplings are controlled by the same integer.

---

## III. WHY THIS PATH IS BLOCKED

The formula sin²θ_W = 3/8 − (109/72)·L/α_EM⁻¹ has one free parameter: L_X, the log-distance from M_Z to the α₁ = α₂ crossing scale. L_X is not determined by SM physics alone. Determining it requires either:

(a) A measurement of sin²θ_W (circular — that's what we're trying to derive)
(b) A measurement of α_s plus forced three-way unification (gives 10% miss — SM doesn't unify)
(c) Knowledge of the GUT-scale physics that determines the crossing scale (beyond SM)

The 3/8 is real structure from SU(5) charge counting. The running coefficient 109/72 is real structure from SM particle counting. But the crossing scale encodes physics beyond the SM. Without it, sin²θ_W(M_Z) is not derivable from 3/8 + SM running alone.

**This is the same wall as the gap ratio.** The gap ratio 218/115 ≠ measured 1.395 because the SM particle content is incomplete. The sin²θ_W running requires the crossing scale, which requires the complete particle content. Both problems are the same problem.

---

## IV. WHAT WOULD UNBLOCK THIS

(a) If the complete GUT particle content were known, the crossing scale would be determined and sin²θ_W(M_Z) would follow from 3/8 + running. This is the standard GUT prediction — it works in SUSY SU(5) where the three couplings do approximately unify.

(b) If a second integer relation determined L_X — for example, if L_X = some rational multiple of α_EM⁻¹ — then sin²θ_W would be fully determined by integers. No such relation is currently known.

(c) If the gap ratio could be derived from integer structure (predicting 1.395 from counting), that would simultaneously determine the crossing scale and sin²θ_W. This is equivalent to knowing the complete particle content.

---

## V. NUMERICAL RESULTS FOR FUTURE REFERENCE

```
Version 1 (forced unification):
  L = 4.7152, M_GUT = 6.71e14 GeV
  alpha_GUT_inv = 41.48
  sin2_tW(M_Z) = 0.2076 (10.2% below PDG)

Version 2 (linear formula):
  sin2_tW = 3/8 - (109/72) * L_X / alpha_EM_inv
  Denominator coefficient = 0 (identity)
  L_X = 4.049 reproduces PDG sin2_tW = 0.23122
  Crossing scale at L_X = 4.049: mu_X = 1.02e13 GeV

At L_X = 4.049 (PDG-matching):
  alpha_X_inv = 42.40
  If alpha_3 also unifies: alpha_s = 0.071 (40% below measured)
```

---

## VI. SCRIPT

`sin2tw_from_gut.py` — in /home/claude/. Not in outputs (notebook entry).

---

## VII. TAGS FOR FUTURE RETRIEVAL

- sin squared theta W, weak mixing angle, Weinberg angle
- 3/8, SU(5), GUT prediction, charge counting
- 109, gap ratio, 218/115, beta function slopes
- Linear running formula, vanishing denominator identity
- Crossing scale, alpha_1 = alpha_2, L_X parameter
- Blocked by: crossing scale not determined in SM
- Same wall as gap ratio — incomplete particle content

---

**END WORKING DOCUMENT**

**Status:** Notebook entry. Not in series. Not published.
**Finding:** sin²θ_W = 3/8 − (109/72)·L/α_EM⁻¹ with integer coefficients. The formula is exact at one loop but has one free parameter (crossing scale) not determined by SM physics.
**Blocked by:** The crossing scale requires GUT-scale physics (complete particle content). Same wall as the gap ratio.
**Pickup instructions:** Load this document. If the gap ratio problem is solved (complete particle content determined), this immediately gives sin²θ_W as a derived parameter.

---
