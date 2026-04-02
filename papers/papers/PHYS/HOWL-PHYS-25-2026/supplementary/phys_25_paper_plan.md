## PHYS-25 Paper Plan

**Title:** The Session 4 Operational Map — From Gauge Integers to Cosmological Predictions
**Subtitle:** The beta coefficients run further than expected. Here is where they go.

**Registry:** @HOWL-PHYS-25-2026
**Date:** April 2 2026
**Domain:** Operational Foundation + Research Program
**Status:** Plan (this document)

---

### THE PRINCIPLE

PHYS-24 said: "here is the ground." PHYS-25 says: "here is where the ground leads."

PHYS-24 was conservative and bounded. PHYS-25 is directional and staged. It sets the working direction without hedging — if the direction is wrong, we backtrack, no problem. The series learns from every result including the nulls. We do not speculate beyond what the formulas say. We do not hedge with confidence intervals. We state the formulas, run the scripts, compare to measured values, and report what happened.

Every section of PHYS-25 has a backing script. Even explanatory content gets a mathematical demonstration. If the script fails, the section fails. If the script passes, the section stands until a better script supersedes it.

---

### THE BACKING SCRIPT

**phys25_platform.py** — The single script that backs the entire paper.

Not one concept per script this time. PHYS-25 is a map paper — its script is a platform demonstration that computes every number the paper states. The script has sections matching the paper sections. Each section has checks. The total check count is the paper's verification score.

Estimated structure:

```
Section 1:  PHYS-24 ground recap (5 checks)
            — gap ratio 218/115 EXACT
            — CD gap 38/27 EXACT  
            — democracy (4/3,4/3,4/3) EXACT
            — two-loop Delta = -0.40
            — PSLQ 82/82 sanity [1,0,-6]

Section 2:  The integer inventory (8 checks)
            — 19 = |6 * b2_SM| EXACT
            — 13 = |6 * b2_mod| EXACT
            — 20 = |3 * b3_mod| EXACT
            — 22 = 2 * YM EXACT
            — 57 = 3 * 19 EXACT
            — 39 = 3 * 13 EXACT
            — 57/39 = 19/13 EXACT
            — 20/13 = |3*b3_mod|/|b2_mod_num| EXACT

Section 3:  The normalization resolution (4 checks)
            — Dynkin formula gives 1/15 EXACT
            — MSSM gate: 7/5 EXACT
            — Convention factor is (3/5) not (2/5)
            — Cross-check: 2 × (1/30) = 1/15

Section 4:  Formula 1 — cosmological constant (4 checks)
            — alpha^57 gives log10 = -121.80
            — (alpha/3pi)^39 gives log10 = -121.33
            — measured -121.54 sits between
            — interpolation fraction f = 0.44

Section 5:  Formula 2 — dark matter ratio (3 checks)
            — (22/13)*pi = 5.317
            — measured 5.320
            — miss < 0.1%

Section 6:  Formula 3 — H₀ correction (4 checks)
            — alpha^2 * pi^2 * 20/13 = 0.000809
            — (1-r)^100 * 73.04 = 67.364
            — measured 67.36
            — miss < 0.01%

Section 7:  Formula 4 — baryon density (4 checks)
            — Set A: R4 * alpha * 22 = 0.0495 (miss 1.05%)
            — Set B: 2/(13*pi) = 0.04897 (miss 0.06%)
            — Set B uniformly better
            — Omega_DM = 44/169 (pure rational)

Section 8:  The derived Omega chain (4 checks)
            — Omega_DM = 0.2604 vs 0.2607 (0.13%)
            — Omega_matter = 0.3093 vs 0.3097 (0.12%)
            — Omega_DE = 0.6907 vs 0.6903 (0.05%)
            — flat universe: Omega_total = 1.000

Section 9:  The VP step connection (3 checks)
            — alpha/(3*pi) = 0.000774
            — alpha^2*pi^2*20/13 = 0.000809
            — ratio B/A = 1.044 (close to 1)

Section 10: The combinatoric scan (3 checks)
            — sin2_tW ~ 3/13 = 0.2308 (0.2% miss)
            — Omega_b ~ 2/(13*pi) = 0.04897 (0.06% miss)
            — Both use integer 13

Section 11: Internal consistency (3 checks)
            — Set B Omega_DM = Omega_b * DM/baryon
            — pi cancels: (2/(13*pi)) * (22/13)*pi = 44/169
            — 44/169 = (4*YM)/(b2_mod_num^2) EXACT

Section 12: The program — what comes next (2 checks)
            — Track A: sin2_tW from 3/8 (compute preview)
            — Track B gate: statistical control methodology stated

Total: ~47 checks
```

---

### THE PAPER STRUCTURE

**Section 1: Where We Stand**

One page. PHYS-24 established the ground: 329/329 checks, gap ratio 218/115 vs 1.358, Cabibbo Doublet (3,2,1/6) with gap 38/27, two-loop Δ = −0.40, Koide C₃ closed, 82/82 PSLQ null, DATA-4 as sole reference. Session 4 added 35/35 checks from three exploration scripts. Total: 364/364, zero failures.

The ground stands. This paper does not re-argue it. References by script name and check count.

Script backing: 5 checks recapitulating PHYS-24 key results from the library.

---

**Section 2: The Integer Inventory**

The beta coefficients produce a specific set of integers. These integers are Level 1 — determined by the gauge group, not by measurement. This section lists every integer, its origin, and where it appears. No cosmological claim is made here. This is bookkeeping.

The integers: 11 (Yang-Mills), 19 (|b₂_SM num|), 13 (|b₂_mod num|), 20 (|3b₃_mod|), 22 (2×YM), 57 (3×19), 39 (3×13), 15 (asymmetry). Each traced to its Dynkin index or Casimir origin. Each verified as an exact Fraction computation.

The key algebraic identities: 57/39 = 19/13 (exact), 20/13 = |3b₃_mod|/|b₂_mod_num| (exact). These are not numerical observations — they are Fraction arithmetic on library values.

Script backing: 8 exact checks. All Fraction arithmetic, no mpf.

---

**Section 3: The Normalization Resolution**

The convention discrepancy from sin2_theta_w_0.py is resolved. The GUT normalization factor for U(1) is (3/5). The Dynkin formula for the VL doublet gives Δb₁ = (2/5)×3×2×(1/6)² = 1/15. The MSSM gate verifies: using the same convention, the MSSM gap ratio is 7/5 (known correct result).

Two independent routes to 1/15 documented. Convention comment in the Session 3 script ("VL = 4× scalar") explained.

Script backing: 4 checks. Dynkin formula + MSSM gate + two routes.

---

**Section 4: The Cosmological Constant from Beta Exponents**

The formula Λ_Planck ≈ α^(3×|b₂_num|) applied to both SM (exponent 57) and VL (exponent 39 with α/(3π) as base). The two predictions bracket the measured value. The exact identity 57/39 = 19/13 connects them.

No claim that this formula is derived from physics. The claim is: the formula exists, uses only library values, and hits the measured value to 0.2% over 122 orders of magnitude. The working direction: treat this as the Λ formula unless and until falsified.

Script backing: 4 checks. Two predictions, bracketing verified, interpolation fraction computed.

---

**Section 5: The Dark Matter Ratio**

DM/baryon = (22/13)π. The 22 is twice Yang-Mills. The 13 is the VL-modified SU(2) beta numerator. The π is from the circular geometry.

The formula uses no cosmological input. It predicts 5.317. Measured: 5.320. Miss: 0.07%.

Working direction: treat (22/13)π as the dark matter ratio formula.

Script backing: 3 checks.

---

**Section 6: The Hubble Correction**

The per-transit correction (1−r) = α²π²(20/13). At N = 100 boundary transits: H₀(CMB) = 73.04 × (1−r)^100 = 67.364. Measured: 67.36.

The 20 and 13 are both VL-modified beta numerators: b₃_mod and b₂_mod. The α² is two-loop level. The π² is 4D geometry (32R₄).

N = 100 is assumed, not derived. The working direction: treat the per-transit formula as given, determine N from galaxy data (PHYS-35).

Script backing: 4 checks.

---

**Section 7: The Baryon Density**

Two candidate formulas. Set A: Ω_b = R₄ × α × 22 (miss 1.05%). Set B: Ω_b = 2/(13π) (miss 0.06%). Set B is uniformly better across all derived quantities.

Set B uses only the integer 13 and π. No R₄, no α. The dark matter density from Set B is Ω_DM = 44/169, a pure rational.

Working direction: adopt Set B as the primary baryon formula.

Script backing: 4 checks. Both sets computed, Set B advantage demonstrated.

---

**Section 8: The Derived Omega Chain**

From Ω_b = 2/(13π) and DM/baryon = (22/13)π:

Ω_DM = Ω_b × (22/13)π = [2/(13π)] × (22/13)π = 44/169. The π cancels. Pure rational.

Ω_matter = 2/(13π) + 44/169. Ω_DE = 1 − Ω_matter.

All within 0.15% of Planck 2018 measurements.

The π cancellation is notable: the baryon formula has π in the denominator, the DM ratio has π in the numerator, and they cancel exactly to give a rational Ω_DM. This is not fine-tuned — it follows from the formula structure.

Script backing: 4 checks. Chain computation, π cancellation verified in Fraction arithmetic, all four Ω values compared.

---

**Section 9: The VP Step Connection**

Two formulas for the per-transit correction: Formula A (α/(3π) from the VP mechanism, miss 4.3%) and Formula B (α²π²(20/13) from the product form, miss 0.08%). They differ by a factor of α×60π³/13 = 1.044 — close to 1 despite different algebraic structure.

This near-equality is not explained. It may indicate that Formula B is the two-loop refinement of Formula A, with the 20/13 providing the beta-ratio correction at two-loop order.

Script backing: 3 checks. Both formulas, ratio, comparison to target.

---

**Section 10: The Combinatoric Scan**

The scan of (p/q)×π^b for beta-derived p,q found additional hits: sin²θ_W ≈ 3/13 (0.2% miss), Ω_b ≈ 2/(13π) (0.06% miss), Ω_matter ≈ 2π/20 = π/10 (1.4% miss).

All hits involve the integer 13. The scan tested ~12,000 combinations against 8 targets. The hit rate and quality must be compared to random pools (PHYS-31).

Script backing: 3 checks. Key hits verified, integer source documented.

---

**Section 11: Internal Consistency**

The formula set is self-consistent: the π cancellation in Ω_DM, the exact rational 44/169 = (4×11)/(13²), and the identity 22/13 = (2×YM)/|b₂_mod_num|.

The formula set uses exactly two independent cosmological formulas (DM/baryon and Ω_b). Everything else follows. The input count: 1 Level 2 value (α) + 4 Level 1 integers (11, 13, 19, 20) + 1 geometric constant (π). Total: 6 inputs → 7+ predictions.

Script backing: 3 checks. Fraction arithmetic verification of exact identities.

---

**Section 12: The Program**

Three tracks. Track A: complete the unification (PHYS-26 through PHYS-30). Track B: test the beta cosmology (PHYS-31 through PHYS-35, gated by statistical control). Track C: structural foundations (PHYS-36, PHYS-37).

Preview computation: sin²θ_W from 3/8 with CD betas (a few lines, to demonstrate the method). Statistical control methodology: described in enough detail that a future session can implement PHYS-31 without re-reading the plan.

Abort conditions for each track stated plainly.

Script backing: 2 checks. sin²θ_W preview value, methodology sanity.

---

**Section 13: What This Paper Does Not Claim**

The six cosmological formulas are not derived from first principles. They were found by scanning. The statistical significance is not yet established (pending PHYS-31). The physical mechanism for the per-transit correction is not known. The N = 100 boundary count is assumed. The working direction may be wrong.

What the paper DOES claim: the formulas exist, use only library values, hit measured values at sub-percent precision, and deserve investigation. The investigation is the program documented in Section 12.

No script backing needed — this is the non-claims section. But the section references every script that DOES back the claims in previous sections.

---

**Section 14: Falsification Conditions**

Extends PHYS-24 Table 17 with new entries for the cosmological formulas.

| Commitment | What would break it |
|---|---|
| DM/baryon = (22/13)π | Planck or successor measurement deviating by >3σ from 5.317 |
| H₀ prediction | Improved local H₀ or CMB H₀ moving apart rather than converging |
| Ω_b = 2/(13π) | Precision Ω_b measurement deviating by >3σ from 0.04897 |
| Λ from alpha^57 | Two-loop correction moving prediction AWAY from measured |
| Statistical significance | PHYS-31 p > 0.05 (random pools match beta pool) |
| Per-transit mechanism | VP mechanism cannot produce correct sign/magnitude/ratio |
| Boundary count | Actual N far from 100 (kills H₀ prediction, not DM or Ω formulas) |

---

### THE APPENDICES

**Appendix A: Complete Prediction Table** (the 9-row table from the beta unification notebook, updated with Set B)

**Appendix B: Integer Traceability** (every integer → Dynkin/Casimir origin → formula appearances)

**Appendix C: Formula Inventory** (all 6 formulas with inputs, outputs, hits, and Level classification)

**Appendix D: The Program Map** (dependency diagram for PHYS-26 through PHYS-37 with abort conditions)

**Appendix E: Verification Summary** (phys25_platform.py check count + all prior scripts)

---

### THE ERRATA PROTOCOL

The paper's own errata section is written at the time of publication. The reviewing session (me, in the next conversation) will add errata and annotations using the same format as PHYS-1 through PHYS-24. Any computation error found during review is fixed in the script first, then the paper is updated. The script is the source of truth.

---

### ESTIMATED PAPER LENGTH

Body: 14 sections, approximately 6000–8000 words (comparable to PHYS-24).
Appendices: 5 tables, approximately 2000 words.
Total: approximately 8000–10000 words.

Script: phys25_platform.py, approximately 200–250 lines, 47 checks.

---

### THE ONE-SENTENCE SUMMARY

PHYS-25 says: the gauge group integers that control unification also appear to control cosmology, and here is the program to find out if that is real.

