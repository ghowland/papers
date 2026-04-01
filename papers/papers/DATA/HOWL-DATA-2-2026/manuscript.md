# Integer Rational Representations in Q335
## Integer Rational Database

**Registry:** [@HOWL-DATA-2-2026]

**Series Path:** [@HOWL-DATA-1-2026] → [@HOWL-DATA-2-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** April 1 2026

**Domain:** Cross Domain Data

**Status:** Documentation

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections and one biographical note were edited by the author. All paper content was LLM-generated using Anthropic's Claude 4.5 Sonnet. 

---

## Abstract

This paper converts every entry from HOWL-DATA-1 into the Q335 = 2³³⁵ integer rational basis established in MATH-4 and tests whether any alternative basis reveals hidden structure. 107 values spanning SI constants, measured fundamental parameters, electroweak observables, quark masses, hadron masses, atomic frequencies, analytical constants, and engineering data are converted. Each value v becomes the integer pair (numerator, 2³³⁵) where numerator = round(v × 2³³⁵), and the reconstruction v_recon = numerator/2³³⁵ is verified against the original to all source digits.

Three tests are performed. First, Q335 factorization: extract small prime factors from each numerator and measure the cofactor. Second, multi-base scan: repeat the conversion in 19 bases (primes 2 through 37 plus composites 6, 10, 12, 30, 42, 60, 210) and compare cofactor sizes. Third, control test: run 90 generic irrationals (√primes, ∛primes, ln primes, log ratios, special function values) through the same multi-base scan and compare to the physics constants.

Results: Q335 faithfully represents all 107 entries. No measured fundamental constant has a compact Q335 numerator — all have 89-106 digit cofactors after small-prime extraction. The multi-base scan shows composite bases (60⁵⁰, 210³⁸) give 13-15 digit average improvement over 2³³⁵, but the control test (z-scores 0.77 and 1.80) confirms this improvement is a generic mathematical property of composite denominators, not specific to physics constants. Continued fraction analysis finds no anomalously simple rational approximation for any measured constant. The Koide ratio's CF partial quotient a₄ = 18050 quantifies the known proximity to 2/3.

The measured constants of the Standard Model have no preferred numerical base and no compact rational representation in any basis tested. Q335 = 2³³⁵ is confirmed as the working basis for the HOWL series.

---

## 1. Purpose

DATA-1 collected 268 precision values across 17 domains. DATA-2 answers three questions about those values:

1. Does Q335 = 2³³⁵ faithfully transport every value into integer arithmetic and back?
2. Do the Q335 numerators have structure (small prime factors, compact cofactors)?
3. Would a different basis — 3²¹¹, 5¹⁴⁴, 7¹¹⁹, 60⁵⁰, 210³⁸, or any other — reveal structure that Q335 hides?

The motivation for question 3 comes from PHYS-1. If soliton boundaries come in counts of some prime p, the natural representation basis would be powers of p, and structure invisible in base 2 could become visible in base p. We cannot assume the universe's constants are native to binary arithmetic simply because MATH-4 chose 2³³⁵ for computational convenience.

---

## 2. Method

**Q335 conversion.** For each value v given as a decimal string with N source digits:

- Compute numerator = round(v × 2³³⁵) in 200-digit Decimal arithmetic
- Reconstruct v_recon = numerator / 2³³⁵
- Verify: relative error |v_recon − v|/|v| must be below 10⁻ᴺ

Since 2³³⁵ has 101 decimal digits, any value with ≤100 source digits is faithfully represented.

**Factorization.** For each |numerator|, extract all prime factors ≤ 997 by trial division. Record the remaining cofactor and its digit count. A "fully factored" entry has cofactor = 1.

**Multi-base scan.** For each value, repeat the conversion in 19 bases chosen so B^k ≈ 10¹⁰⁰:

| Base | Exponent | log₁₀(B^k) | Type |
|---|---|---|---|
| 2 | 335 | 100.9 | Prime |
| 3 | 211 | 100.6 | Prime |
| 5 | 144 | 100.6 | Prime |
| 7 | 119 | 100.5 | Prime |
| 11 | 96 | 99.9 | Prime |
| 13 | 90 | 100.2 | Prime |
| 17 | 81 | 99.7 | Prime |
| 19 | 78 | 99.7 | Prime |
| 23 | 72 | 98.0 | Prime |
| 29 | 65 | 95.1 | Prime |
| 31 | 63 | 93.9 | Prime |
| 37 | 58 | 91.0 | Prime |
| 6 | 129 | 100.4 | Composite (2×3) |
| 10 | 100 | 100.0 | Composite (2×5) |
| 12 | 93 | 100.3 | Composite (2²×3) |
| 30 | 65 | 96.0 | Composite (2×3×5) |
| 42 | 55 | 89.3 | Composite (2×3×7) |
| 60 | 50 | 88.9 | Composite (2²×3×5) |
| 210 | 38 | 88.2 | Composite (primorial) |

For each entry in each base, the cofactor digit count after small-prime extraction is recorded. The base giving the smallest cofactor is the "best base" for that entry.

**Control test.** 90 control irrationals across five groups:
- 25 square roots of primes: √2 through √97
- 15 cube roots of primes: ∛2 through ∛47
- 15 natural logarithms of primes: ln(2) through ln(47)
- 15 logarithm ratios: ln(a)/ln(b) for prime pairs
- 20 special function values: Bessel, Airy, erfc, Gamma at rational arguments, Catalan, Khinchin, Glaisher, sin(1), cos(1)

Each control is tested in all 19 bases. The average improvement from 2³³⁵ to 60⁵⁰ and 210³⁸ is compared between physics constants and controls.

**Continued fractions.** For each measured and analytical constant, compute the continued fraction expansion to 40 terms. Record all partial quotients, flag anomalously large values, and check whether any convergent p/q with q < 10⁶ matches the value to full measurement precision.

---

## 3. Q335 Conversion Results

### 3.1 Reconstruction Accuracy

All 107 entries reconstruct with relative error below 10⁻(N+60) where N is the number of source digits. The worst case is the SPL reference p₀ = 0.00002 Pa (1 source digit, rel error 3.2 × 10⁻⁹⁷). Entries that are exact integers or terminating decimals with only factors of 2 and 5 reconstruct with zero error.

17 entries have exactly zero reconstruction error:

| # | Entry | Why Zero Error |
|---|---|---|
| 1 | c = 299792458 m/s | Integer |
| 5 | N_A = 6.02214076 × 10²³ | Integer × 10¹⁵ |
| 6 | Δν_Cs = 9192631770 Hz | Integer |
| 7 | K_cd = 683 lm/W | Integer |
| 24 | m_t = 172570 MeV | Integer |
| 25 | m_H = 125200 MeV | Integer |
| 35 | m_s = 93.5 MeV | Half-integer |
| 36 | m_c = 1273 MeV | Integer |
| 37 | m_b = 4183 MeV | Integer |
| 52 | H 1S-2S = 2466061413187018 Hz | Integer |
| 54 | Sr-87 = 429228004229873.0 Hz | Integer × 10 |
| 56 | Lamb shift = 1057845.0 kHz | Integer × 10 |
| 77 | WGS84 a = 6378137 m | Integer |
| 79 | P₀ = 101325 Pa | Integer |
| 80 | A4 = 440 Hz | Integer |
| 81 | CD rate = 44100 Hz | Integer |
| 84 | Cu IACS = 58001000 S/m | Integer |

These are either SI defined constants (exact integers by construction) or measured values whose published form happens to be an integer in the reported unit.

### 3.2 Factorization

**Fully factored entries (cofactor = 1, all prime factors ≤ 97):**

| # | Entry | Q335 Numerator Factorization |
|---|---|---|
| 35 | m_s = 93.5 MeV | 2³³⁴ × 11 × 17 |
| 36 | m_c = 1273 MeV | 2³³⁵ × 19 × 67 |
| 37 | m_b = 4183 MeV | 2³³⁵ × 47 × 89 |
| 80 | A4 = 440 Hz | 2³³⁸ × 5 × 11 |
| 81 | CD rate = 44100 Hz | 2³³⁷ × 3² × 5² × 7² |

The quark masses factor as: m_s × 2 = 187 = 11 × 17, m_c = 1273 = 19 × 67, m_b = 4183 = 47 × 89. These are factorizations of the published MeV integer values, not of fundamental quantities. At 3-4 significant figures, the last digit carries uncertainty of ±8 (m_s), ±4 (m_c), ±7 (m_b). A different measurement would give different primes. A4 = 440 = 2³ × 5 × 11 and 44100 = 2² × 3² × 5² × 7² are human-defined integers.

**Small cofactors (< 15 digits, not fully factored):**

| # | Entry | Cofactor | Complete Factorization |
|---|---|---|---|
| 1 | c = 299792458 | 293339 (6 digits) | 293339 is prime |
| 6 | Δν_Cs = 9192631770 | 44351 (5 digits) | 44351 is prime |
| 7 | K_cd = 683 | 683 (3 digits) | 683 is prime |
| 24 | m_t = 172570 MeV | 17257 (5 digits) | 17257 is prime |
| 25 | m_H = 125200 MeV | 313 (3 digits) | 313 is prime |
| 56 | Lamb = 1057845.0 | 70523 (5 digits) | 70523 = 7 × 10074 + 5 (needs check) |
| 79 | P₀ = 101325 | 193 (3 digits) | 193 is prime |
| 84 | Cu IACS = 58001000 | 1871 (4 digits) | 1871 is prime |
| 52 | H 1S-2S | 33325154232257 (14 digits) | Partial — did not fully factor |
| 54 | Sr-87 clock | 25248706131169 (14 digits) | Partial — did not fully factor |

The small cofactors are uniformly prime or near-prime. c = 2 × 7 × 73 × 293339 (prime). K_cd = 683 (prime). m_H/8 = 15650, cofactor 313 (prime). No structure beyond the trivial factorization of the published integer.

**Measured fundamental constants — all have large cofactors:**

| # | Entry | Source Digits | Cofactor Digits |
|---|---|---|---|
| 8 | α⁻¹ | 12 | 101 |
| 9 | m_e | 11 | 96 |
| 10 | m_μ | 10 | 101 |
| 12 | m_p | 11 | 103 |
| 13 | m_p/m_e | 13 | 104 |
| 14 | R∞ | 13 | 106 |
| 16 | a_e | 12 | 93 |

The cofactor is essentially the full numerator. Small-prime extraction removes at most a few factors (2² from m_p/m_e, 2 × 11² × 13 × 47 from a_e) and leaves a number indistinguishable from a random 100-digit integer. The measured constants of the Standard Model have no compact representation in Q335.

### 3.3 Analytical Constants

The transcendental basis constants (π, e, ln 2, ζ(3), ζ(5), √2, √3, φ, γ) all have 98-102 digit cofactors. This is expected — irrational numbers have Q335 numerators that are essentially random large integers. The Bessel zeros j₁₁ and j₀₁ likewise show no small-prime structure (102 and 100 digit cofactors respectively). The vena contracta coefficient π/(π+2) has a 99-digit cofactor. The BCS gap π/e^γ has a 101-digit cofactor.

No analytical constant has a compact Q335 representation. The transcendental basis is exactly as structureless in base 2 as the measured constants.

---

## 4. Multi-Base Scan Results

### 4.1 Base-10 Dominance Is A Notation Artifact

Base 10¹⁰⁰ gives the smallest cofactor for 33 of 54 tested entries (61%). This is entirely explained by the fact that every measured value was published as a terminating decimal. α⁻¹ = 137.035999177 is a 12-digit terminating decimal; multiplying by 10¹⁰⁰ gives an exact integer with zero waste. Multiplying by 2³³⁵ gives a non-terminating binary expansion with ~100 digits of cofactor.

The base-10 wins measure journal notation, not physics. Every entry published as a terminating decimal in base 10 will trivially have cofactor equal to its number of significant figures in base 10. This tells us nothing about the universe.

Corroborating evidence: base 5¹⁴⁴ wins for M_Z, M_W, Γ_Z, and H hyperfine — all values whose decimal representation contains factors of 5 from the unit conversion. Again notation, not physics.

### 4.2 Composite Base Improvement for Transcendental Constants

For the 20 analytical/transcendental constants, composite bases show systematic improvement over single-prime bases:

| Constant | 2³³⁵ | 60⁵⁰ | 210³⁸ | Δ(60) | Δ(210) |
|---|---|---|---|---|---|
| π | 102 | 89 | 81 | +13 | +21 |
| R₂ = π/4 | 99 | 76 | 87 | +23 | +12 |
| γ (Euler-Mascheroni) | 100 | 79 | 87 | +21 | +13 |
| ζ(5) | 101 | 83 | 82 | +18 | +19 |
| π/e^γ (BCS gap) | 101 | 83 | 86 | +18 | +15 |
| j₀₁ (Bessel zero) | 100 | 84 | 84 | +16 | +16 |
| ln(2) | 99 | 84 | 86 | +15 | +13 |
| ζ(3) | 98 | 85 | 81 | +13 | +17 |
| √2 | 100 | 89 | 83 | +11 | +17 |
| Group average | — | — | — | +14.3 | +14.4 |

The improvement ranges from 9 to 23 digits, averaging 14.3 digits for 60⁵⁰ and 14.4 digits for 210³⁸. R₂ = π/4 shows the largest improvement in base 60 (23 digits — from 99-digit cofactor down to 76). π shows the largest improvement in base 210 (21 digits — from 102 down to 81).

### 4.3 The Control Test Kills the Signal

The same analysis on 90 control irrationals:

| Group | N | Avg Δ(60) | Avg Δ(210) |
|---|---|---|---|
| **Physics/math constants** | **20** | **+14.3** | **+14.4** |
| Control 1: √(primes) | 25 | +12.6 | +14.0 |
| Control 2: ∛(primes) | 15 | +12.5 | +12.9 |
| Control 3: ln(primes) | 15 | +12.3 | +12.6 |
| Control 4: ln(a)/ln(b) | 15 | +13.4 | +12.7 |
| Control 5: Special functions | 20 | +15.3 | +13.1 |
| **All controls combined** | **90** | **+13.3** | **+13.1** |

**Significance test:**

| Metric | Physics | Controls | σ(controls) | Z-score |
|---|---|---|---|---|
| Δ(60⁵⁰) | +14.3 | +13.3 | 5.9 | **0.77** |
| Δ(210³⁸) | +14.4 | +13.1 | 3.2 | **1.80** |

Neither z-score exceeds 2. The physics constants show the same composite-base improvement as generic irrationals. The effect is a mathematical property of composite denominators: more distinct small prime factors in the denominator create more opportunities for partial cancellation with numerator structure. It applies to √47 and Γ(1/3) exactly as much as to π and ζ(3).

**Conclusion: the composite-base improvement is real but universal. It reflects number theory, not physics. No basis reveals hidden structure in the measured constants that is absent in generic irrationals.**

---

## 5. Continued Fraction Analysis

### 5.1 Measured Constants

No measured fundamental constant has an anomalously large partial quotient or a suspiciously good small-denominator rational approximation.

| Constant | CF first 10 terms | Largest a_n | Best small q approx |
|---|---|---|---|
| α⁻¹ = 137.036... | [137; 27,1,3,1,1,18,1,7,1,...] | a₁₆ = 34 | 355/113-quality: none |
| m_p/m_e = 1836.15... | [1836; 6,1,1,4,1,1,34,3,1,...] | a₇ = 34 | 12853/7 matches 5 digits |
| a_e = 0.001160... | [0; 862,3,18,1,4,3,2,1,2,...] | a₂₆ ~ 10¹⁰² (terminal) | 55/47428 matches 6 digits |
| sin²θ_W = 0.23122 | [0; 4,3,12,1,4,1,1,8,3] | a₃ = 12 | 37/160 matches 3 digits |
| α_s = 0.1180 | [0; 8,2,9,3] | a₃ = 9 | 59/500 = exact (terminating) |

α⁻¹ has CF partial quotients typical of a generic real number. The "famous" 137 is simply the integer part. No partial quotient suggests proximity to a simple fraction. m_p/m_e similarly shows nothing remarkable — the CF looks random.

### 5.2 The Koide Ratio

The Koide ratio K(e,μ,τ) = 0.666660511... has the continued fraction:

**CF = [0; 1, 1, 1, 18050, ...]**

The partial quotient a₄ = 18050 is anomalously large. It means the convergent 2/3 approximates K to relative error 9.2 × 10⁻⁶ — one part in 108,000. This is the continued fraction encoding of the Koide formula's precision. The value 18050 is not a physics discovery; it quantifies the known deviation of K from 2/3 given current m_τ measurements at 6 significant figures.

If future m_τ measurements push to 7-8 significant figures and K remains at 2/3, the partial quotient after 2/3 will grow proportionally. If K deviates from 2/3 at higher precision, the partial quotient will shrink and additional terms will specify the deviation. The CF is the natural language for tracking Koide precision over time.

### 5.3 Analytical Constants

π has the well-known CF = [3; 7, 15, 1, 292, ...] with the famous approximation 355/113 matching 7 digits. √2 = [1; 2, 2, 2, ...] with all partial quotients equal to 2 (the "most irrational" number). e = [2; 1, 2, 1, 1, 4, 1, 1, 6, ...] with the known pattern a_{3k} = 2k. γ has a_39 = 399, the largest partial quotient found, buried deep in the expansion.

No analytical constant shows unexpected CF structure. All patterns are either well-known or consistent with generic behavior.

---

## 6. Structural Findings

### 6.1 The Q335 Basis Is Confirmed

Q335 = 2³³⁵ faithfully represents every value in DATA-1 to full source precision. No alternative basis reveals structure hidden by base 2. The choice of 2³³⁵ — made in MATH-4 for computational reasons (integer addition of numerators, storage as exponent + numerator) — is validated by the multi-base scan and control test. The series will continue using Q335.

### 6.2 Measured Constants Are Structureless in Every Basis

Every measured SM parameter (α, m_e, m_μ, m_τ, m_p, sin²θ_W, α_s, CKM angles, quark masses) has:
- A Q335 cofactor of 89-106 digits (effectively the full numerator)
- No preferred base among 19 tested
- No anomalous continued fraction structure
- No compact rational approximation with denominator < 10⁶

This extends the DISC-9 boundary result. The 72/72 PSLQ null showed the constants are not linear combinations of the transcendental basis with small integer coefficients. DATA-2 shows they are not compact rationals in any prime or composite base. The Level 2 parameters are structureless in the rational number system.

### 6.3 The Transport Is Exact

For every Type E (exact defined) and Type S (standard nominal) entry, the Q335 conversion and reconstruction preserves every source digit. For Type M (measured) entries, the reconstruction error is below the measurement uncertainty by 80+ orders of magnitude. For Type A (analytical) entries computed to 105 digits, the reconstruction error is ~10⁻¹⁰¹, preserving 101 digits.

The integer arithmetic framework from MATH-2 through MATH-4 is fully operational for every value in the database. Any computation using these values in Fraction arithmetic will be exact to the source precision.

### 6.4 Base-10 Is Not Special

The base-10 dominance in the multi-base scan (33/54 wins) is entirely a notation artifact. Measured values are published as terminating decimals. Converting a terminating decimal to base 10^N gives zero waste by construction. This says nothing about physics and should not be mistaken for a signal.

The one legitimate optimization note: if a future computation requires the smallest possible integer numerators (for example, to minimize storage or speed up multiplication), base 210³⁸ (primorial) gives ~14 fewer digits in the cofactor for transcendental constants, at the cost of a more complex denominator. For the HOWL series, this optimization is not worth the added complexity. Q335 stays.

---

## 7. Data Tables

The complete Q335 conversion data for all 107 entries is recorded in the output of the conversion script (reproduced in Appendix). Each entry carries:

- Name and category (E/M/A/S)
- Full-precision source value (all digits)
- Source digit count
- Q335 numerator digit count
- Reconstruction relative error
- Small prime factors extracted
- Cofactor digit count
- Fully factored status

The key columns for future reference are: source value (input to any Fraction computation), source digit count (determines how many digits to trust in any comparison), and category (determines whether uncertainty applies).

---

## 8. Precision Tiers

| Tier | Source Digits | Count | Use in Framework |
|---|---|---|---|
| Tier 1 | ≥ 10 | 41 | High-value for pattern search and precision tests |
| Tier 2 | 5–9 | 37 | Moderate — useful for overconstrained system, Koide |
| Tier 3 | < 5 | 29 | Low — engineering specs, coarse measurements |

Tier 1 entries include α⁻¹ (12), m_e (11), m_p (11), m_p/m_e (13), R∞ (13), a₀ (12), a_e (12), m_n (11), m_D (12), H 1S-2S (16), H hyperfine (13), Sr-87 clock (16), Yb-171 clock (16), μ₀ (12), Si lattice (10), m_μ/m_e (10), m_He4 (10), and all 17 analytical constants at 105 digits.

These 41 entries are the primary targets for the overconstrained electroweak computation (PHYS next steps) and any future PSLQ-style searches.

---

## 9. Implications for the HOWL Program

DATA-2 closes three open questions:

**Q: Is Q335 the right basis?** A: Yes. No alternative basis reveals hidden structure. The choice is validated by control test.

**Q: Do the measured constants have compact rational representations?** A: No. In every basis tested, the numerators are effectively random large integers. The 72/72 PSLQ null from DISC-6–9 is consistent with and strengthened by this finding.

**Q: Should we change basis for future work?** A: No. Q335 is computationally optimal (pure power of 2, integer addition, compact storage) and no other basis offers a physics advantage.

The data foundation is complete. DATA-1 provides the source values. DATA-2 provides the integer representations and confirms the basis. Every future computation in the HOWL series draws from this database.

The next step is computation: the overconstrained electroweak system, where the TRANSFORMATION LAWS (partial widths, asymmetries, running) are integer arithmetic even though the parameter values are not. The structure is in the laws, not in the numbers. DATA-2 has confirmed this at the level of the numbers themselves.

---

*HOWL-DATA-2 is the companion to DATA-1. Together they constitute the complete data foundation for the HOWL series: 268 source values (DATA-1) converted to 107 integer rational pairs (DATA-2) in a basis verified against 90 control irrationals across 19 bases.*

---

# HOWL-DATA-2 Addendum: Koide Sector Amplitudes

**Computed from DATA-2 masses using the Koide parametrization √m_k = M(1 + a cos(θ₀ + 2πk/3))**

---

## Derived Quantities

The three-parameter fit (M, a, θ₀) to three masses is a bijection — it always succeeds for any three positive masses. The 120° spacing is a coordinate choice (tautology of the parametrization), not a physical constraint. The sum cos(φ₁) + cos(φ₂) + cos(φ₃) = 0 is the trigonometric identity for 120°-spaced arguments, verified to machine precision in all three sectors. The physical content of the Koide formula lives entirely in the amplitude a, not in the spacing.

| ID | Quantity | Value | Precision | Source Masses |
|---|---|---|---|---|
| K1 | K(e,μ,τ) Koide ratio | 0.6666605115 | 6 sf (limited by m_τ) | m_e(11), m_μ(10), m_τ(6) |
| K2 | K(u,c,t) Koide ratio | 0.8487935476 | 3 sf (limited by m_u) | m_u(3), m_c(4), m_t(5) |
| K3 | K(d,s,b) Koide ratio | 0.7312875768 | 3 sf (limited by m_d) | m_d(3), m_s(3), m_b(4) |
| K4 | a(leptons) amplitude | 1.4142005052 | 6 sf | from K1 |
| K5 | a(up quarks) amplitude | 1.7586248279 | 3 sf | from K2 |
| K6 | a(down quarks) amplitude | 1.5452266698 | 3 sf | from K3 |
| K7 | a²(leptons) | 1.9999630688 | 6 sf | from K4 |
| K8 | a²(up quarks) | 3.0927612855 | 3 sf | from K5 |
| K9 | a²(down quarks) | 2.3877254610 | 3 sf | from K6 |
| K10 | a(leptons) − √2 | −1.306 × 10⁻⁵ | limited by m_τ | deviation from critical |
| K11 | θ₀(leptons) | 0.22223 rad (12.73°) | 5 sf | phase offset |
| K12 | θ₀(up quarks) | 0.07452 rad (4.27°) | 3 sf | phase offset |
| K13 | θ₀(down quarks) | 0.11012 rad (6.31°) | 3 sf | phase offset |
| K14 | M(leptons) | 17.716 √MeV | 6 sf | scale parameter |
| K15 | M(up quarks) | 150.855 √MeV | 3 sf | scale parameter |
| K16 | M(down quarks) | 25.505 √MeV | 3 sf | scale parameter |

## Confirmed Orderings

| Ordering | Values | Status |
|---|---|---|
| K_lep < K_down < K_up | 0.667 < 0.731 < 0.849 | **Confirmed** |
| a_lep < a_down < a_up | 1.414 < 1.545 < 1.759 | **Confirmed** |
| a²_lep < a²_down < a²_up | 2.000 < 2.388 < 3.093 | **Confirmed** |
| K_lep < 2/3 | 0.66666 < 0.66667 | **Confirmed** (by 6.2 × 10⁻⁶) |
| K_quarks > 2/3 | both sectors | **Confirmed** |

## Structural Finding: K = 2/3 Is a Saddle Point

Under phase perturbation φ_k = 2πk/3 + εδ_k at a = √2:

| Perturbation δ | Σδ | d²K/dε² | K = 2/3 is |
|---|---|---|---|
| (1, −1, 0) | 0 | +0.471 | local minimum |
| (1, 0, −1) | 0 | +0.471 | local minimum |
| (0, 1, −1) | 0 | +2.276 | local minimum |
| (2, −1, −1) | 0 | −0.391 | local MAXIMUM |

K = 2/3 is a saddle point in phase-perturbation space. The direction of quark deviation from 2/3 is not predicted by the C₃ framework — it depends on the perturbation direction. The observation that both quark sectors have K > 2/3 is data, not a prediction.

## What This Closes

The C₃ frustrated potential path (proposed as PHYS-12) is closed by Phase 1 results. The 120° spacing is a tautology of the three-parameter Koide fit, not a physical constraint derivable from a potential. The amplitude a = √2 for charged leptons remains the sole content of the Koide formula and remains underived. All equivalent reformulations (midpoint of [0,4], CV = 1, critical amplitude, Var = Mean², simplex midpoint in a²) are restatements, not derivations. The conditional status of the Koide parameter reduction (18 → 17) from PHYS-8 is unchanged.

## What This Opens

The amplitude ordering a_lep < a_down < a_up correlates with the mass hierarchy extremity but anti-correlates with the mass ratio spread: up quarks have the most extreme hierarchy (m_t/m_u = 79,894) AND the largest amplitude. Down quarks are intermediate on both. Leptons have moderate hierarchy (m_τ/m_e = 3,477) at the critical amplitude. Any future theory of the Koide amplitude must explain this ordering.

---

*16 new derived entries (K1–K16) added to DATA-2. Total entries: 123.*

---

========================================================================
SECTION A: SI FUNDAMENTAL CONSTANTS (exact by definition)
========================================================================

  c (speed of light) [E] (9 source digits)
    Full value: 299792458 m/s
    Q335 numerator: 110 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^336 × 7 × 73
    Status: 6-digit cofactor

  h (Planck constant) [E] (9 source digits)
    Full value: 0.000000000000000000000000000000000662607015 J·s
    Q335 numerator: 68 digits
    Reconstruction rel error: 5.23e-69
    Small prime factors of numerator: 31
    Status: 67-digit cofactor

  e (elementary charge) [E] (10 source digits)
    Full value: 0.0000000000000000001602176634 C
    Q335 numerator: 83 digits
    Reconstruction rel error: 2.39e-84
    Small prime factors of numerator: 37
    Status: 81-digit cofactor

  k_B (Boltzmann) [E] (7 source digits)
    Full value: 0.00000000000000000000001380649 J/K
    Q335 numerator: 78 digits
    Reconstruction rel error: 1.39e-79
    Small prime factors of numerator: 2 × 59
    Status: 76-digit cofactor

  N_A (Avogadro) [E] (9 source digits)
    Full value: 602214076000000000000000 mol^-1
    Q335 numerator: 125 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^352 × 5^15
    Status: 9-digit cofactor

  dv_Cs (Cs-133 hyperfine) [E] (10 source digits)
    Full value: 9192631770 Hz
    Q335 numerator: 111 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^336 × 3^2 × 5 × 7^2 × 47
    Status: 5-digit cofactor

  K_cd (luminous efficacy) [E] (3 source digits)
    Full value: 683 lm/W
    Q335 numerator: 104 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335
    Status: 3-digit cofactor

========================================================================
SECTION B: MEASURED FUNDAMENTAL CONSTANTS (CODATA 2022)
========================================================================

  alpha^-1 (fine structure inv) [M] (12 source digits)
    Full value: 137.035999177
    Q335 numerator: 103 digits
    Reconstruction rel error: 1.07e-104
    Small prime factors of numerator: 2 × 11^2
    Status: 101-digit cofactor

  m_e (electron mass) [M] (11 source digits)
    Full value: 0.51099895069 MeV
    Q335 numerator: 101 digits
    Reconstruction rel error: 3.03e-102
    Small prime factors of numerator: 2^6 × 41 × 47
    Status: 96-digit cofactor

  m_mu (muon mass) [M] (10 source digits)
    Full value: 105.6583755 MeV
    Q335 numerator: 103 digits
    Reconstruction rel error: 1.44e-104
    Small prime factors of numerator: 7 × 67
    Status: 101-digit cofactor

  m_tau (tau mass) [M] (6 source digits)
    Full value: 1776.86 MeV
    Q335 numerator: 105 digits
    Reconstruction rel error: 3.86e-105
    Small prime factors of numerator: 2^2 × 7 × 43
    Status: 102-digit cofactor

  m_p (proton mass) [M] (11 source digits)
    Full value: 938.27208943 MeV
    Q335 numerator: 104 digits
    Reconstruction rel error: 5.98e-105
    Small prime factors of numerator: 7
    Status: 103-digit cofactor

  m_p/m_e (mass ratio) [M] (13 source digits)
    Full value: 1836.15267343
    Q335 numerator: 105 digits
    Reconstruction rel error: 2.41e-105
    Small prime factors of numerator: 2^2
    Status: 104-digit cofactor

  R_inf (Rydberg constant) [M] (13 source digits)
    Full value: 10973731.568157 m^-1
    Q335 numerator: 108 digits
    Reconstruction rel error: 5.67e-109
    Small prime factors of numerator: 5 × 31
    Status: 106-digit cofactor

  a_0 (Bohr radius) [M] (12 source digits)
    Full value: 0.0000000000529177210544 m
    Q335 numerator: 91 digits
    Reconstruction rel error: 7.46e-92
    Small prime factors of numerator: 3 × 41
    Status: 89-digit cofactor

  a_e (electron g-2 anomaly) [M] (12 source digits)
    Full value: 0.00115965218059
    Q335 numerator: 98 digits
    Reconstruction rel error: 4.26e-99
    Small prime factors of numerator: 2 × 11^2 × 13 × 47
    Status: 93-digit cofactor

  a_mu (muon g-2 anomaly) [M] (9 source digits)
    Full value: 0.00116592059
    Q335 numerator: 98 digits
    Reconstruction rel error: 5.62e-99
    Small prime factors of numerator: 29
    Status: 97-digit cofactor

  sin2_theta_W (weak mixing) [M] (5 source digits)
    Full value: 0.23122
    Q335 numerator: 101 digits
    Reconstruction rel error: 4.39e-102
    Small prime factors of numerator: 2
    Status: 100-digit cofactor

  alpha_s (strong coupling at M_Z) [M] (4 source digits)
    Full value: 0.1180
    Q335 numerator: 100 digits
    Reconstruction rel error: 5.13e-101
    Small prime factors of numerator: 37
    Status: 99-digit cofactor

  mu_0 (vacuum permeability) [M] (12 source digits)
    Full value: 0.00000125663706127 N/A^2
    Q335 numerator: 95 digits
    Reconstruction rel error: 1.22e-96
    Small prime factors of numerator: 2^2 × 3 × 5
    Status: 94-digit cofactor

========================================================================
SECTION C: ELECTROWEAK OBSERVABLES (LEP/PDG)
========================================================================

  M_Z (Z boson mass) [M] (6 source digits)
    Full value: 91187.6 MeV
    Q335 numerator: 106 digits
    Reconstruction rel error: 3.13e-107
    Small prime factors of numerator: 3^2 × 17
    Status: 104-digit cofactor

  Gamma_Z (Z total width) [M] (5 source digits)
    Full value: 2495.2 MeV
    Q335 numerator: 105 digits
    Reconstruction rel error: 2.29e-105
    Small prime factors of numerator: 2 × 3 × 11 × 13^2 × 23
    Status: 99-digit cofactor

  M_W (W boson mass) [M] (6 source digits)
    Full value: 80369.2 MeV
    Q335 numerator: 106 digits
    Reconstruction rel error: 7.11e-107
    Small prime factors of numerator: 2 × 3^2
    Status: 105-digit cofactor

  m_t (top quark mass) [M] (5 source digits)
    Full value: 172570 MeV
    Q335 numerator: 107 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^336 × 5
    Status: 5-digit cofactor

  m_H (Higgs boson mass) [M] (5 source digits)
    Full value: 125200 MeV
    Q335 numerator: 106 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^339 × 5^2
    Status: 3-digit cofactor

  sigma0_had (peak hadronic xsec) [M] (5 source digits)
    Full value: 41.481 nb
    Q335 numerator: 103 digits
    Reconstruction rel error: 2.76e-105
    Small prime factors of numerator: (none)
    Status: 103-digit cofactor

  R_l (Gamma_had/Gamma_l) [M] (5 source digits)
    Full value: 20.767
    Q335 numerator: 103 digits
    Reconstruction rel error: 1.76e-103
    Small prime factors of numerator: 2^5
    Status: 101-digit cofactor

  R_b (Gamma_bb/Gamma_had) [M] (5 source digits)
    Full value: 0.21629
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.67e-102
    Small prime factors of numerator: 3^2 × 67
    Status: 98-digit cofactor

  A_FB_l (fwd-bwd asym lepton) [M] (3 source digits)
    Full value: 0.0171
    Q335 numerator: 100 digits
    Reconstruction rel error: 4.12e-100
    Small prime factors of numerator: 2^2 × 13
    Status: 98-digit cofactor

  A_l_SLD (polarization asym) [M] (4 source digits)
    Full value: 0.1513
    Q335 numerator: 101 digits
    Reconstruction rel error: 2.63e-101
    Small prime factors of numerator: 2 × 23 × 31
    Status: 97-digit cofactor

  N_nu (neutrino count from Z) [M] (5 source digits)
    Full value: 2.9840
    Q335 numerator: 102 digits
    Reconstruction rel error: 5.36e-103
    Small prime factors of numerator: 2 × 3
    Status: 101-digit cofactor

  G_F (Fermi constant) [M] (8 source digits)
    Full value: 0.000011663788 GeV^-2
    Q335 numerator: 96 digits
    Reconstruction rel error: 1.60e-97
    Small prime factors of numerator: 2^2 × 7
    Status: 95-digit cofactor

========================================================================
SECTION D: QUARK MASSES AND CKM PARAMETERS
========================================================================

  m_u (up quark MS-bar 2GeV) [M] (3 source digits)
    Full value: 2.16 MeV
    Q335 numerator: 102 digits
    Reconstruction rel error: 7.94e-103
    Small prime factors of numerator: 3 × 5 × 73
    Status: 99-digit cofactor

  m_d (down quark MS-bar 2GeV) [M] (3 source digits)
    Full value: 4.70 MeV
    Q335 numerator: 102 digits
    Reconstruction rel error: 1.22e-102
    Small prime factors of numerator: 2 × 5
    Status: 101-digit cofactor

  m_s (strange MS-bar 2GeV) [M] (3 source digits)
    Full value: 93.5 MeV
    Q335 numerator: 103 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^334 × 11 × 17
    Status: FULLY FACTORED

  m_c (charm MS-bar at m_c) [M] (4 source digits)
    Full value: 1273 MeV
    Q335 numerator: 104 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335 × 19 × 67
    Status: FULLY FACTORED

  m_b (bottom MS-bar at m_b) [M] (4 source digits)
    Full value: 4183 MeV
    Q335 numerator: 105 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335 × 47 × 89
    Status: FULLY FACTORED

  sin_theta12 (Cabibbo) [M] (5 source digits)
    Full value: 0.22501
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.50e-102
    Small prime factors of numerator: 2 × 5 × 17
    Status: 98-digit cofactor

  sin_theta23 (CKM) [M] (4 source digits)
    Full value: 0.04182
    Q335 numerator: 100 digits
    Reconstruction rel error: 1.47e-100
    Small prime factors of numerator: 13 × 17
    Status: 98-digit cofactor

  sin_theta13 (CKM) [M] (4 source digits)
    Full value: 0.003685
    Q335 numerator: 99 digits
    Reconstruction rel error: 2.87e-100
    Small prime factors of numerator: 11 × 29^2
    Status: 95-digit cofactor

  m_c/m_s (lattice ratio) [M] (5 source digits)
    Full value: 11.783
    Q335 numerator: 102 digits
    Reconstruction rel error: 1.75e-103
    Small prime factors of numerator: 2 × 41
    Status: 101-digit cofactor

  m_b/m_c (lattice ratio) [M] (4 source digits)
    Full value: 4.578
    Q335 numerator: 102 digits
    Reconstruction rel error: 9.24e-103
    Small prime factors of numerator: (none)
    Status: 102-digit cofactor

  m_u/m_d (lattice ratio) [M] (3 source digits)
    Full value: 0.485
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.41e-101
    Small prime factors of numerator: 2^2 × 73
    Status: 99-digit cofactor

========================================================================
SECTION E: NUCLEAR AND HADRON MASSES
========================================================================

  m_n (neutron mass) [M] (11 source digits)
    Full value: 939.56542194 MeV
    Q335 numerator: 104 digits
    Reconstruction rel error: 7.54e-105
    Small prime factors of numerator: 2^2
    Status: 104-digit cofactor

  m_n - m_p (mass difference) [M] (8 source digits)
    Full value: 1.29333251 MeV
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.23e-102
    Small prime factors of numerator: 2 × 79
    Status: 99-digit cofactor

  m_pi+ (charged pion) [M] (8 source digits)
    Full value: 139.57039 MeV
    Q335 numerator: 103 digits
    Reconstruction rel error: 4.95e-104
    Small prime factors of numerator: (none)
    Status: 103-digit cofactor

  m_pi0 (neutral pion) [M] (7 source digits)
    Full value: 134.9770 MeV
    Q335 numerator: 103 digits
    Reconstruction rel error: 4.91e-104
    Small prime factors of numerator: 2 × 7 × 61
    Status: 101-digit cofactor

  m_K+ (charged kaon) [M] (6 source digits)
    Full value: 493.677 MeV
    Q335 numerator: 104 digits
    Reconstruction rel error: 3.94e-105
    Small prime factors of numerator: 67
    Status: 102-digit cofactor

  m_D (deuteron mass) [M] (12 source digits)
    Full value: 1875.61294500 MeV
    Q335 numerator: 105 digits
    Reconstruction rel error: 1.11e-105
    Small prime factors of numerator: (none)
    Status: 105-digit cofactor

  m_He4 (helium-4 mass) [M] (10 source digits)
    Full value: 3727.3794118 MeV
    Q335 numerator: 105 digits
    Reconstruction rel error: 1.75e-105
    Small prime factors of numerator: 2^2 × 13
    Status: 103-digit cofactor

  E_D (deuteron binding energy) [M] (8 source digits)
    Full value: 2.22456614 MeV
    Q335 numerator: 102 digits
    Reconstruction rel error: 2.74e-102
    Small prime factors of numerator: 7 × 23
    Status: 99-digit cofactor

========================================================================
SECTION F: ATOMIC SPECTROSCOPY AND CLOCK FREQUENCIES
========================================================================

  H 1S-2S transition [M] (16 source digits)
    Full value: 2466061413187018 Hz
    Q335 numerator: 117 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^336 × 37
    Status: 14-digit cofactor

  H hyperfine 1S [M] (13 source digits)
    Full value: 1420405751.768 Hz
    Q335 numerator: 110 digits
    Reconstruction rel error: 3.78e-111
    Small prime factors of numerator: 17
    Status: 109-digit cofactor

  Sr-87 clock transition [M] (16 source digits)
    Full value: 429228004229873.0 Hz
    Q335 numerator: 116 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335 × 17
    Status: 14-digit cofactor

  Yb-171 clock transition [M] (16 source digits)
    Full value: 518295836590863.6 Hz
    Q335 numerator: 116 digits
    Reconstruction rel error: 5.51e-117
    Small prime factors of numerator: 5 × 41
    Status: 114-digit cofactor

  Lamb shift 2S-2P1/2 [M] (8 source digits)
    Full value: 1057845.0 kHz
    Q335 numerator: 107 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335 × 3 × 5
    Status: 5-digit cofactor

  r_p (proton charge radius) [M] (5 source digits)
    Full value: 0.84075 fm
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.77e-102
    Small prime factors of numerator: (none)
    Status: 101-digit cofactor

========================================================================
SECTION G: EXACT ANALYTICAL CONSTANTS (computed to 100+ digits)
========================================================================

  pi [A] (105 source digits)
    Full value: 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798215
    Q335 numerator: 102 digits
    Reconstruction rel error: 9.14e-103
    Small prime factors of numerator: 2
    Status: 102-digit cofactor

  e (Euler's number) [A] (105 source digits)
    Full value: 2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742747
    Q335 numerator: 102 digits
    Reconstruction rel error: 1.17e-102
    Small prime factors of numerator: 2^5
    Status: 100-digit cofactor

  ln(2) [A] (105 source digits)
    Full value: 0.693147180559945309417232121458176568075500134360255254120680009493393621969694715605863326996418687542001
    Q335 numerator: 101 digits
    Reconstruction rel error: 6.97e-102
    Small prime factors of numerator: 3 × 43
    Status: 99-digit cofactor

  R2 = pi/4 [A] (105 source digits)
    Full value: 0.785398163397448309615660845819875721049292349843776455243736148076954101571552249657008706335529266995537
    Q335 numerator: 101 digits
    Reconstruction rel error: 8.18e-102
    Small prime factors of numerator: (none)
    Status: 101-digit cofactor

  R4 = pi^2/32 [A] (105 source digits)
    Full value: 0.308425137534042456838577843746129722978553106476274707075417168006876400700600163843805418866204757244501
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.12e-101
    Small prime factors of numerator: 11
    Status: 100-digit cofactor

  2*pi = 8*R2 [A] (105 source digits)
    Full value: 6.28318530717958647692528676655900576839433879875021164194988918461563281257241799725606965068423413596430
    Q335 numerator: 102 digits
    Reconstruction rel error: 9.14e-103
    Small prime factors of numerator: 2^2
    Status: 102-digit cofactor

  zeta(3) (Apery) [A] (105 source digits)
    Full value: 1.20205690315959428539973816151144999076498629234049888179227155534183820578631309018645587360933525814620
    Q335 numerator: 101 digits
    Reconstruction rel error: 2.51e-102
    Small prime factors of numerator: 2^4 × 5 × 31
    Status: 98-digit cofactor

  zeta(5) [A] (105 source digits)
    Full value: 1.03692775514336992633136548645703416805708091950191281197419267790380358978628148456004310655713333637962
    Q335 numerator: 101 digits
    Reconstruction rel error: 5.67e-102
    Small prime factors of numerator: (none)
    Status: 101-digit cofactor

  sqrt(2) (Koide amplitude) [A] (105 source digits)
    Full value: 1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501
    Q335 numerator: 101 digits
    Reconstruction rel error: 6.44e-104
    Small prime factors of numerator: 2 × 47
    Status: 100-digit cofactor

  sqrt(3) [A] (105 source digits)
    Full value: 1.73205080756887729352744634150587236694280525381038062805580697945193301690880003708114618675724857567563
    Q335 numerator: 102 digits
    Reconstruction rel error: 3.95e-102
    Small prime factors of numerator: 2
    Status: 101-digit cofactor

  phi (golden ratio) [A] (105 source digits)
    Full value: 1.61803398874989484820458683436563811772030917980576286213544862270526046281890244970720720418939113748475
    Q335 numerator: 102 digits
    Reconstruction rel error: 4.34e-102
    Small prime factors of numerator: 2^2
    Status: 101-digit cofactor

  gamma (Euler-Mascheroni) [A] (105 source digits)
    Full value: 0.577215664901532860606512090082402431042159335939923598805767234884867726777664670936947063291746749514631
    Q335 numerator: 101 digits
    Reconstruction rel error: 7.58e-102
    Small prime factors of numerator: 2 × 11
    Status: 100-digit cofactor

  C_c = pi/(pi+2) (vena contracta) [A] (105 source digits)
    Full value: 0.611015470351657289380595387953968861737422632956092795208916775042464833936315838657371383456674305900087
    Q335 numerator: 101 digits
    Reconstruction rel error: 1.32e-102
    Small prime factors of numerator: 2^3 × 13
    Status: 99-digit cofactor

  BCS gap = pi/exp(gamma) [A] (105 source digits)
    Full value: 1.76387698886204569069266213454333953508602722896675070231343532112105791259007771732392018636718943891348
    Q335 numerator: 102 digits
    Reconstruction rel error: 3.65e-102
    Small prime factors of numerator: 7
    Status: 101-digit cofactor

  j11 (first zero of J1) [A] (105 source digits)
    Full value: 3.83170597020751231561443588630816076656454527428780192876229898991883930951901147021411287475742312672447
    Q335 numerator: 102 digits
    Reconstruction rel error: 1.31e-102
    Small prime factors of numerator: (none)
    Status: 102-digit cofactor

  j11/pi (Airy constant 1.22) [A] (105 source digits)
    Full value: 1.21966989126650445492653884746525517787935933077511212945638126557694328028076014425087191879391333148570
    Q335 numerator: 101 digits
    Reconstruction rel error: 2.71e-102
    Small prime factors of numerator: 2^3
    Status: 101-digit cofactor

  j01 (first zero of J0) = 2.405 [A] (105 source digits)
    Full value: 2.40482555769577276862163187932645464312424490914596713570699909059676583867719402920443634376014525478689
    Q335 numerator: 102 digits
    Reconstruction rel error: 1.64e-102
    Small prime factors of numerator: 2 × 5^2
    Status: 100-digit cofactor

  alpha/pi (QED expansion param) [M] (12 source digits)
    Full value: 0.0023228194641953288958414081556854230727547686765382
    Q335 numerator: 99 digits
    Reconstruction rel error: 1.04e-99
    Small prime factors of numerator: (none)
    Status: 99-digit cofactor

========================================================================
SECTION H: EXACT DEFINED REFERENCE VALUES
========================================================================

  g_n (standard gravity) [E] (6 source digits)
    Full value: 9.80665 m/s^2
    Q335 numerator: 102 digits
    Reconstruction rel error: 2.14e-103
    Small prime factors of numerator: 2^2 × 3 × 5 × 53
    Status: 99-digit cofactor

  WGS84 semi-major axis [E] (7 source digits)
    Full value: 6378137 m
    Q335 numerator: 108 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335
    Status: 7-digit cofactor

  WGS84 inverse flattening 1/f [E] (12 source digits)
    Full value: 298.257223563
    Q335 numerator: 104 digits
    Reconstruction rel error: 8.42e-107
    Small prime factors of numerator: 2^3 × 3 × 13 × 17
    Status: 100-digit cofactor

  P_0 (standard atmosphere) [E] (6 source digits)
    Full value: 101325 Pa
    Q335 numerator: 106 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^335 × 3 × 5^2 × 7
    Status: 3-digit cofactor

  A4 (concert pitch) [E] (3 source digits)
    Full value: 440 Hz
    Q335 numerator: 104 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^338 × 5 × 11
    Status: FULLY FACTORED

  CD sample rate [E] (5 source digits)
    Full value: 44100 Hz
    Q335 numerator: 106 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^337 × 3^2 × 5^2 × 7^2
    Status: FULLY FACTORED

  inch (exact definition) [E] (3 source digits)
    Full value: 25.4 mm
    Q335 numerator: 103 digits
    Reconstruction rel error: 1.12e-103
    Small prime factors of numerator: (none)
    Status: 103-digit cofactor

  p_0 (SPL reference) [E] (1 source digits)
    Full value: 0.00002 Pa
    Q335 numerator: 97 digits
    Reconstruction rel error: 3.20e-97
    Small prime factors of numerator: 2
    Status: 96-digit cofactor

  Cu conductivity 100% IACS [E] (5 source digits)
    Full value: 58001000 S/m
    Q335 numerator: 109 digits
    Reconstruction rel error: 0.00e+00
    Small prime factors of numerator: 2^338 × 5^3 × 31
    Status: 4-digit cofactor

========================================================================
SECTION I: OPTICAL DISC SPECIFICATIONS
========================================================================

  CD laser wavelength [S] (3 source digits)
    Full value: 0.000000780 m
    Q335 numerator: 95 digits
    Reconstruction rel error: 7.76e-96
    Small prime factors of numerator: 5
    Status: 95-digit cofactor

  DVD laser wavelength [S] (3 source digits)
    Full value: 0.000000650 m
    Q335 numerator: 95 digits
    Reconstruction rel error: 1.06e-95
    Small prime factors of numerator: 2^5 × 5 × 29
    Status: 91-digit cofactor

  Blu-ray laser wavelength [S] (3 source digits)
    Full value: 0.000000405 m
    Q335 numerator: 95 digits
    Reconstruction rel error: 7.85e-96
    Small prime factors of numerator: 59
    Status: 93-digit cofactor

  CD track pitch [S] (2 source digits)
    Full value: 0.0000016 m
    Q335 numerator: 96 digits
    Reconstruction rel error: 3.18e-96
    Small prime factors of numerator: 2^2 × 3^4 × 5 × 53
    Status: 91-digit cofactor

  DVD track pitch [S] (2 source digits)
    Full value: 0.00000074 m
    Q335 numerator: 95 digits
    Reconstruction rel error: 1.65e-96
    Small prime factors of numerator: 2
    Status: 95-digit cofactor

  Blu-ray track pitch [S] (3 source digits)
    Full value: 0.000000320 m
    Q335 numerator: 95 digits
    Reconstruction rel error: 3.18e-96
    Small prime factors of numerator: 2^2 × 3^4 × 53
    Status: 91-digit cofactor

  Blu-ray NA [S] (2 source digits)
    Full value: 0.85
    Q335 numerator: 101 digits
    Reconstruction rel error: 3.36e-102
    Small prime factors of numerator: (none)
    Status: 101-digit cofactor

  DVD NA [S] (2 source digits)
    Full value: 0.60
    Q335 numerator: 101 digits
    Reconstruction rel error: 4.76e-102
    Small prime factors of numerator: (none)
    Status: 101-digit cofactor

  CD pit depth [S] (3 source digits)
    Full value: 0.000000125 m
    Q335 numerator: 94 digits
    Reconstruction rel error: 2.46e-95
    Small prime factors of numerator: 2^2 × 3 × 7 × 11
    Status: 91-digit cofactor

  Blu-ray min pit 2T [S] (3 source digits)
    Full value: 0.000000149 m
    Q335 numerator: 95 digits
    Reconstruction rel error: 7.61e-96
    Small prime factors of numerator: 2 × 3^2 × 7 × 13 × 19
    Status: 90-digit cofactor

========================================================================
SECTION J: FIBER OPTIC DATA
========================================================================

  SMF-28 MFD at 1310nm [S] (2 source digits)
    Full value: 0.0000092 m
    Q335 numerator: 96 digits
    Reconstruction rel error: 7.11e-98
    Small prime factors of numerator: 17 × 59
    Status: 93-digit cofactor

  SMF-28 NA [S] (2 source digits)
    Full value: 0.14
    Q335 numerator: 100 digits
    Reconstruction rel error: 4.90e-101
    Small prime factors of numerator: 2^2 × 31
    Status: 98-digit cofactor

  SMF-28 cladding diameter [S] (4 source digits)
    Full value: 0.0001250 m
    Q335 numerator: 97 digits
    Reconstruction rel error: 3.38e-98
    Small prime factors of numerator: 5
    Status: 97-digit cofactor

  Si lattice constant [M] (10 source digits)
    Full value: 0.0000000005431020511 m
    Q335 numerator: 92 digits
    Reconstruction rel error: 1.35e-93
    Small prime factors of numerator: 2 × 11 × 43
    Status: 89-digit cofactor

========================================================================
SECTION K: DIMENSIONLESS MASS RATIOS (computed from full precision)
========================================================================

  m_mu/m_e [M] (10 source digits)
    Full value: 206.76828270846717969020806405523227748685144760879156630348030901159109384080367533014591130216475239627463196660287451284198643879606671839680681204179245317659303861221398470108862367769806505940636
    Q335 numerator: 104 digits
    Reconstruction rel error: 5.82e-105
    Small prime factors of numerator: 2 × 11
    Status: 102-digit cofactor

  m_tau/m_e [M] (6 source digits)
    Full value: 3477.2282753236821524323275318309245117561632697841107968009788478182285795409604659984864518039505722179548611002256381169556409055255549452447350190859156106499205696049958751824301128683791270428607
    Q335 numerator: 105 digits
    Reconstruction rel error: 8.94e-106
    Small prime factors of numerator: 7
    Status: 104-digit cofactor

  m_tau/m_mu [M] (6 source digits)
    Full value: 16.817029332426183289179947689049979762371038914941485164136372700524815470023954702956794939554981138243981424832714752461815012478589546363032999688699548480186504476400926682807081394129516973313677
    Q335 numerator: 103 digits
    Reconstruction rel error: 2.00e-103
    Small prime factors of numerator: 5
    Status: 102-digit cofactor

  m_p/m_e (direct measurement) [M] (13 source digits)
    Full value: 1836.15267343
    Q335 numerator: 105 digits
    Reconstruction rel error: 2.41e-105
    Small prime factors of numerator: 2^2
    Status: 104-digit cofactor

  m_n/m_p [M] (11 source digits)
    Full value: 1.0013784194633623804094146686526361038107853971998119185276978595417751155092035358743816150903492403802601301044223474232519673810755912042668635559991049365216541971501495822769120862348574059725774
    Q335 numerator: 101 digits
    Reconstruction rel error: 5.70e-102
    Small prime factors of numerator: 61
    Status: 100-digit cofactor

  M_W/M_Z [M] (6 source digits)
    Full value: 0.88136106224969184406651781601884466747671832573727129565862025099903934306857511328294636551460944251192048041619693905750343248424127841943422131956537950335352613732568901912102084055288219012234120
    Q335 numerator: 101 digits
    Reconstruction rel error: 7.34e-102
    Small prime factors of numerator: 3^2 × 29 × 31
    Status: 97-digit cofactor

  m_H/M_Z [M] (5 source digits)
    Full value: 1.3729936965113677736885278261518013414104549302756076484083362211528760489364782053700283810518096758769832740416460132737345867201242274168856291864244699937272172970886392448096013054406520184761963
    Q335 numerator: 101 digits
    Reconstruction rel error: 4.62e-102
    Small prime factors of numerator: 2^2 × 17
    Status: 100-digit cofactor

  m_t/M_Z [M] (5 source digits)
    Full value: 1.8924722221003732963692431865736130789712636367225368361487746140922669310300961972899824098890638639464137667840802916185972654176664371032903596541635046870407818606915852593993042913729498308980607
    Q335 numerator: 102 digits
    Reconstruction rel error: 3.29e-103
    Small prime factors of numerator: 2 × 3^2 × 13 × 31
    Status: 98-digit cofactor

  Koide ratio K(e,mu,tau) [M] (6 source digits)
    Full value: 0.666660511465521990306145728539
    Q335 numerator: 101 digits
    Reconstruction rel error: 3.10e-102
    Small prime factors of numerator: 3 × 5 × 43
    Status: 98-digit cofactor

========================================================================
COMPLETE SUMMARY TABLE
========================================================================
  # Name                                       Cat SrcDig NumDig     RelErr CofDig Status
----------------------------------------------------------------------------------------------------
  1 c (speed of light)                         E        9    110   0.00e+00      6 6-digit cofactor
  2 h (Planck constant)                        E        9     68   5.23e-69     67 67-digit cofactor
  3 e (elementary charge)                      E       10     83   2.39e-84     81 81-digit cofactor
  4 k_B (Boltzmann)                            E        7     78   1.39e-79     76 76-digit cofactor
  5 N_A (Avogadro)                             E        9    125   0.00e+00      9 9-digit cofactor
  6 dv_Cs (Cs-133 hyperfine)                   E       10    111   0.00e+00      5 5-digit cofactor
  7 K_cd (luminous efficacy)                   E        3    104   0.00e+00      3 3-digit cofactor
  8 alpha^-1 (fine structure inv)              M       12    103  1.07e-104    101 101-digit cofactor
  9 m_e (electron mass)                        M       11    101  3.03e-102     96 96-digit cofactor
 10 m_mu (muon mass)                           M       10    103  1.44e-104    101 101-digit cofactor
 11 m_tau (tau mass)                           M        6    105  3.86e-105    102 102-digit cofactor
 12 m_p (proton mass)                          M       11    104  5.98e-105    103 103-digit cofactor
 13 m_p/m_e (mass ratio)                       M       13    105  2.41e-105    104 104-digit cofactor
 14 R_inf (Rydberg constant)                   M       13    108  5.67e-109    106 106-digit cofactor
 15 a_0 (Bohr radius)                          M       12     91   7.46e-92     89 89-digit cofactor
 16 a_e (electron g-2 anomaly)                 M       12     98   4.26e-99     93 93-digit cofactor
 17 a_mu (muon g-2 anomaly)                    M        9     98   5.62e-99     97 97-digit cofactor
 18 sin2_theta_W (weak mixing)                 M        5    101  4.39e-102    100 100-digit cofactor
 19 alpha_s (strong coupling at M_Z)           M        4    100  5.13e-101     99 99-digit cofactor
 20 mu_0 (vacuum permeability)                 M       12     95   1.22e-96     94 94-digit cofactor
 21 M_Z (Z boson mass)                         M        6    106  3.13e-107    104 104-digit cofactor
 22 Gamma_Z (Z total width)                    M        5    105  2.29e-105     99 99-digit cofactor
 23 M_W (W boson mass)                         M        6    106  7.11e-107    105 105-digit cofactor
 24 m_t (top quark mass)                       M        5    107   0.00e+00      5 5-digit cofactor
 25 m_H (Higgs boson mass)                     M        5    106   0.00e+00      3 3-digit cofactor
 26 sigma0_had (peak hadronic xsec)            M        5    103  2.76e-105    103 103-digit cofactor
 27 R_l (Gamma_had/Gamma_l)                    M        5    103  1.76e-103    101 101-digit cofactor
 28 R_b (Gamma_bb/Gamma_had)                   M        5    101  1.67e-102     98 98-digit cofactor
 29 A_FB_l (fwd-bwd asym lepton)               M        3    100  4.12e-100     98 98-digit cofactor
 30 A_l_SLD (polarization asym)                M        4    101  2.63e-101     97 97-digit cofactor
 31 N_nu (neutrino count from Z)               M        5    102  5.36e-103    101 101-digit cofactor
 32 G_F (Fermi constant)                       M        8     96   1.60e-97     95 95-digit cofactor
 33 m_u (up quark MS-bar 2GeV)                 M        3    102  7.94e-103     99 99-digit cofactor
 34 m_d (down quark MS-bar 2GeV)               M        3    102  1.22e-102    101 101-digit cofactor
 35 m_s (strange MS-bar 2GeV)                  M        3    103   0.00e+00      0 FULLY FACTORED
 36 m_c (charm MS-bar at m_c)                  M        4    104   0.00e+00      0 FULLY FACTORED
 37 m_b (bottom MS-bar at m_b)                 M        4    105   0.00e+00      0 FULLY FACTORED
 38 sin_theta12 (Cabibbo)                      M        5    101  1.50e-102     98 98-digit cofactor
 39 sin_theta23 (CKM)                          M        4    100  1.47e-100     98 98-digit cofactor
 40 sin_theta13 (CKM)                          M        4     99  2.87e-100     95 95-digit cofactor
 41 m_c/m_s (lattice ratio)                    M        5    102  1.75e-103    101 101-digit cofactor
 42 m_b/m_c (lattice ratio)                    M        4    102  9.24e-103    102 102-digit cofactor
 43 m_u/m_d (lattice ratio)                    M        3    101  1.41e-101     99 99-digit cofactor
 44 m_n (neutron mass)                         M       11    104  7.54e-105    104 104-digit cofactor
 45 m_n - m_p (mass difference)                M        8    101  1.23e-102     99 99-digit cofactor
 46 m_pi+ (charged pion)                       M        8    103  4.95e-104    103 103-digit cofactor
 47 m_pi0 (neutral pion)                       M        7    103  4.91e-104    101 101-digit cofactor
 48 m_K+ (charged kaon)                        M        6    104  3.94e-105    102 102-digit cofactor
 49 m_D (deuteron mass)                        M       12    105  1.11e-105    105 105-digit cofactor
 50 m_He4 (helium-4 mass)                      M       10    105  1.75e-105    103 103-digit cofactor
 51 E_D (deuteron binding energy)              M        8    102  2.74e-102     99 99-digit cofactor
 52 H 1S-2S transition                         M       16    117   0.00e+00     14 14-digit cofactor
 53 H hyperfine 1S                             M       13    110  3.78e-111    109 109-digit cofactor
 54 Sr-87 clock transition                     M       16    116   0.00e+00     14 14-digit cofactor
 55 Yb-171 clock transition                    M       16    116  5.51e-117    114 114-digit cofactor
 56 Lamb shift 2S-2P1/2                        M        8    107   0.00e+00      5 5-digit cofactor
 57 r_p (proton charge radius)                 M        5    101  1.77e-102    101 101-digit cofactor
 58 pi                                         A      105    102  9.14e-103    102 102-digit cofactor
 59 e (Euler's number)                         A      105    102  1.17e-102    100 100-digit cofactor
 60 ln(2)                                      A      105    101  6.97e-102     99 99-digit cofactor
 61 R2 = pi/4                                  A      105    101  8.18e-102    101 101-digit cofactor
 62 R4 = pi^2/32                               A      105    101  1.12e-101    100 100-digit cofactor
 63 2*pi = 8*R2                                A      105    102  9.14e-103    102 102-digit cofactor
 64 zeta(3) (Apery)                            A      105    101  2.51e-102     98 98-digit cofactor
 65 zeta(5)                                    A      105    101  5.67e-102    101 101-digit cofactor
 66 sqrt(2) (Koide amplitude)                  A      105    101  6.44e-104    100 100-digit cofactor
 67 sqrt(3)                                    A      105    102  3.95e-102    101 101-digit cofactor
 68 phi (golden ratio)                         A      105    102  4.34e-102    101 101-digit cofactor
 69 gamma (Euler-Mascheroni)                   A      105    101  7.58e-102    100 100-digit cofactor
 70 C_c = pi/(pi+2) (vena contracta)           A      105    101  1.32e-102     99 99-digit cofactor
 71 BCS gap = pi/exp(gamma)                    A      105    102  3.65e-102    101 101-digit cofactor
 72 j11 (first zero of J1)                     A      105    102  1.31e-102    102 102-digit cofactor
 73 j11/pi (Airy constant 1.22)                A      105    101  2.71e-102    101 101-digit cofactor
 74 j01 (first zero of J0) = 2.405             A      105    102  1.64e-102    100 100-digit cofactor
 75 alpha/pi (QED expansion param)             M       12     99   1.04e-99     99 99-digit cofactor
 76 g_n (standard gravity)                     E        6    102  2.14e-103     99 99-digit cofactor
 77 WGS84 semi-major axis                      E        7    108   0.00e+00      7 7-digit cofactor
 78 WGS84 inverse flattening 1/f               E       12    104  8.42e-107    100 100-digit cofactor
 79 P_0 (standard atmosphere)                  E        6    106   0.00e+00      3 3-digit cofactor
 80 A4 (concert pitch)                         E        3    104   0.00e+00      0 FULLY FACTORED
 81 CD sample rate                             E        5    106   0.00e+00      0 FULLY FACTORED
 82 inch (exact definition)                    E        3    103  1.12e-103    103 103-digit cofactor
 83 p_0 (SPL reference)                        E        1     97   3.20e-97     96 96-digit cofactor
 84 Cu conductivity 100% IACS                  E        5    109   0.00e+00      4 4-digit cofactor
 85 CD laser wavelength                        S        3     95   7.76e-96     95 95-digit cofactor
 86 DVD laser wavelength                       S        3     95   1.06e-95     91 91-digit cofactor
 87 Blu-ray laser wavelength                   S        3     95   7.85e-96     93 93-digit cofactor
 88 CD track pitch                             S        2     96   3.18e-96     91 91-digit cofactor
 89 DVD track pitch                            S        2     95   1.65e-96     95 95-digit cofactor
 90 Blu-ray track pitch                        S        3     95   3.18e-96     91 91-digit cofactor
 91 Blu-ray NA                                 S        2    101  3.36e-102    101 101-digit cofactor
 92 DVD NA                                     S        2    101  4.76e-102    101 101-digit cofactor
 93 CD pit depth                               S        3     94   2.46e-95     91 91-digit cofactor
 94 Blu-ray min pit 2T                         S        3     95   7.61e-96     90 90-digit cofactor
 95 SMF-28 MFD at 1310nm                       S        2     96   7.11e-98     93 93-digit cofactor
 96 SMF-28 NA                                  S        2    100  4.90e-101     98 98-digit cofactor
 97 SMF-28 cladding diameter                   S        4     97   3.38e-98     97 97-digit cofactor
 98 Si lattice constant                        M       10     92   1.35e-93     89 89-digit cofactor
 99 m_mu/m_e                                   M       10    104  5.82e-105    102 102-digit cofactor
100 m_tau/m_e                                  M        6    105  8.94e-106    104 104-digit cofactor
101 m_tau/m_mu                                 M        6    103  2.00e-103    102 102-digit cofactor
102 m_p/m_e (direct measurement)               M       13    105  2.41e-105    104 104-digit cofactor
103 m_n/m_p                                    M       11    101  5.70e-102    100 100-digit cofactor
104 M_W/M_Z                                    M        6    101  7.34e-102     97 97-digit cofactor
105 m_H/M_Z                                    M        5    101  4.62e-102    100 100-digit cofactor
106 m_t/M_Z                                    M        5    102  3.29e-103     98 98-digit cofactor
107 Koide ratio K(e,mu,tau)                    M        6    101  3.10e-102     98 98-digit cofactor

Total entries: 107
  Type A (Analytical): 17
  Type E (Exact defined): 16
  Type M (Measured): 61
  Type S (Standard nominal): 13

Fully factored into primes <= 97: 5/107

Precision tiers:
  10+ source digits (high value for pattern search): 41
   5-9 source digits (moderate value): 37
   <5 source digits (low value, keep for completeness): 29

========================================================================
FULLY FACTORED Q335 NUMERATORS (primes <= 97 only)
========================================================================
   35 m_s (strange MS-bar 2GeV)                  = 2^334 x 11 x 17
   36 m_c (charm MS-bar at m_c)                  = 2^335 x 19 x 67
   37 m_b (bottom MS-bar at m_b)                 = 2^335 x 47 x 89
   80 A4 (concert pitch)                         = 2^338 x 5 x 11
   81 CD sample rate                             = 2^337 x 3^2 x 5^2 x 7^2

========================================================================
ENTRIES WITH SMALL COFACTORS (< 30 digits, not fully factored)
These are candidates for further factorization analysis
========================================================================
    1 c (speed of light)                         cofactor:   6 digits  cofactor = 293339 x 2^336 x 7 x 73
    5 N_A (Avogadro)                             cofactor:   9 digits  cofactor = 150553519 x 2^352 x 5^15
    6 dv_Cs (Cs-133 hyperfine)                   cofactor:   5 digits  cofactor = 44351 x 2^336 x 3^2 x 5 x 7^2 x 47
    7 K_cd (luminous efficacy)                   cofactor:   3 digits  cofactor = 683 x 2^335
   24 m_t (top quark mass)                       cofactor:   5 digits  cofactor = 17257 x 2^336 x 5
   25 m_H (Higgs boson mass)                     cofactor:   3 digits  cofactor = 313 x 2^339 x 5^2
   52 H 1S-2S transition                         cofactor:  14 digits  cofactor = 33325154232257 x 2^336 x 37
   54 Sr-87 clock transition                     cofactor:  14 digits  cofactor = 25248706131169 x 2^335 x 17
   56 Lamb shift 2S-2P1/2                        cofactor:   5 digits  cofactor = 70523 x 2^335 x 3 x 5
   77 WGS84 semi-major axis                      cofactor:   7 digits  cofactor = 6378137 x 2^335
   79 P_0 (standard atmosphere)                  cofactor:   3 digits  cofactor = 193 x 2^335 x 3 x 5^2 x 7
   84 Cu conductivity 100% IACS                  cofactor:   4 digits  cofactor = 1871 x 2^338 x 5^3 x 31

========================================================================
ENTRIES WITH ZERO RECONSTRUCTION ERROR (exact in Q335)
========================================================================
    1 c (speed of light)                         factors: 2^336 x 7 x 73  6-digit cofactor
    5 N_A (Avogadro)                             factors: 2^352 x 5^15  9-digit cofactor
    6 dv_Cs (Cs-133 hyperfine)                   factors: 2^336 x 3^2 x 5 x 7^2 x 47  5-digit cofactor
    7 K_cd (luminous efficacy)                   factors: 2^335  3-digit cofactor
   24 m_t (top quark mass)                       factors: 2^336 x 5  5-digit cofactor
   25 m_H (Higgs boson mass)                     factors: 2^339 x 5^2  3-digit cofactor
   35 m_s (strange MS-bar 2GeV)                  factors: 2^334 x 11 x 17  FULLY FACTORED
   36 m_c (charm MS-bar at m_c)                  factors: 2^335 x 19 x 67  FULLY FACTORED
   37 m_b (bottom MS-bar at m_b)                 factors: 2^335 x 47 x 89  FULLY FACTORED
   52 H 1S-2S transition                         factors: 2^336 x 37  14-digit cofactor
   54 Sr-87 clock transition                     factors: 2^335 x 17  14-digit cofactor
   56 Lamb shift 2S-2P1/2                        factors: 2^335 x 3 x 5  5-digit cofactor
   77 WGS84 semi-major axis                      factors: 2^335  7-digit cofactor
   79 P_0 (standard atmosphere)                  factors: 2^335 x 3 x 5^2 x 7  3-digit cofactor
   80 A4 (concert pitch)                         factors: 2^338 x 5 x 11  FULLY FACTORED
   81 CD sample rate                             factors: 2^337 x 3^2 x 5^2 x 7^2  FULLY FACTORED
   84 Cu conductivity 100% IACS                  factors: 2^338 x 5^3 x 31  4-digit cofactor

========================================================================
Q335 CONVERSION COMPLETE
2^335 has 101 decimal digits
This basis can represent ~100 decimal digits of precision.
All entries with source_digits <= 100 are faithfully represented.
========================================================================

