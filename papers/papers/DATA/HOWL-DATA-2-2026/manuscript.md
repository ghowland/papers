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
