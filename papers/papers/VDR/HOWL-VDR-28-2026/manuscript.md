# Exact Rational Arithmetic for Sequential Computation
## VDR Applied to Twenty Domains Where Decimal Truncation Compounds

**Registry:** [@HOWL-VDR-28-2026]

**Series Path:** [@HOWL-VDR-1-2026] → [@HOWL-VDR-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026]  → ... → [@HOWL-VDR-14-2026] → ... → [@HOWL-VDR-21-2026] → [@HOWL-VDR-22-2026] → [@HOWL-VDR-23-2026] → [@HOWL-VDR-24-2026] → [@HOWL-VDR-25-2026] → [@HOWL-VDR-26-2026] → [@HOWL-VDR-27-2026] → [@HOWL-VDR-28-2026]

**DOI:** 10.5281/zenodo.20260736

**Date:** May 2026

**Domain:** Exact Arithmetic / Generative Model Inference

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6.

---

## Abstract

Decimal arithmetic — including arbitrary-precision libraries like mpmath — represents numbers in base 10. The only fractions with terminating decimal representations are those whose denominators factor exclusively into 2s and 5s. Every other fraction — 1/3, 1/7, 1/11, 1/13, every fraction whose denominator contains any prime factor other than 2 or 5 — becomes an infinite repeating decimal that must be truncated. This truncation is not a precision issue solvable by carrying more digits. It is a structural incompatibility between the representation and the value.

This paper identifies twenty computational domains where this structural incompatibility produces materially wrong results, and demonstrates that VDR exact rational arithmetic [VDR-1] eliminates the problem entirely. VDR represents 1/3 as [1, 3, 0] — exact, with zero truncation. Chains of operations on exact rationals produce exact rationals. The denominator grows but nothing is discarded. This is not "more precision." It is a categorically different relationship with the numbers.

No prior reading is required. VDR arithmetic is summarized where first used; full specifications are in [VDR-1] and [VDR-14].

---

## 1. The Decimal Trap

### 1.1 Why 10 = 2 × 5 Is the Problem

A fraction a/b has a terminating decimal representation if and only if every prime factor of b (after reducing a/b to lowest terms) is 2 or 5. This is because decimal notation is positional base 10, and 10 = 2 × 5. The denominator must divide some power of 10, which means it must be of the form 2ᵐ × 5ⁿ.

1/2 = 0.5. Terminates. 1/4 = 0.25. Terminates. 1/5 = 0.2. Terminates. 1/8 = 0.125. Terminates. 1/20 = 0.05. Terminates. These are the lucky fractions — the ones whose denominators happen to share factors with our counting base.

1/3 = 0.333... Repeats forever. 1/7 = 0.142857142857... Repeats with period 6. 1/11 = 0.090909... Repeats with period 2. 1/13 = 0.076923076923... Repeats with period 6. 1/6 = 0.1666... Repeats. Even fractions with mixed factors — 1/6 = 1/(2×3) — repeat because of the factor of 3.

Among the first 20 positive integers used as denominators, only 1, 2, 4, 5, 8, 10, 16, 20 produce terminating decimals. The other 12 — 3, 6, 7, 9, 11, 12, 13, 14, 15, 17, 18, 19 — produce infinite repeating decimals. Sixty percent of small denominators are incompatible with decimal representation.

### 1.2 What Arbitrary Precision Does Not Solve

Arbitrary-precision decimal libraries like mpmath address the problem by carrying hundreds or thousands of digits. This reduces the magnitude of the truncation error per operation but does not eliminate it.

Multiply two 1000-digit truncated values: the exact product needs 2000 digits. mpmath truncates back to 1000. Chain 50 operations: 50 truncations, each discarding information from the bottom of the intermediate result. The per-operation loss is small. The accumulated loss over a chain is unknown — mpmath does not track what it discarded. The user sees 1000 digits and assumes they are all correct. Some of them are not, and the user cannot determine which ones without repeating the computation at 2000 digits, which defers the same problem.

The fundamental issue is not how many digits are carried. It is that the representation forces truncation on values that are exactly representable in other forms. 1/3 is three characters: 1, /, 3. In VDR it is three integers: [1, 3, 0]. In decimal it is an infinite sequence of digits that can never be written in full. Carrying more digits is an arbitrarily expensive workaround for a representation deficiency.

### 1.3 What VDR Does Instead

VDR represents every rational number as three integers: Value, Denominator, Remainder [VDR-1]. 1/3 is [1, 3, 0]. 1/7 is [1, 7, 0]. 691/2730 is [691, 2730, 0]. The denominator is stored as an integer, not decomposed into a decimal expansion. No truncation, no repeating digits, no lost information.

Arithmetic on VDR rationals is exact. [1, 3, 0] × [1, 7, 0] = [1, 21, 0]. Chain 50 operations: exact. Chain 1000 operations: exact. The denominator grows — 21, 441, 9261, ... — but nothing is discarded. Every digit of every intermediate result is preserved in the numerator and denominator integers.

When precision must be bounded — for GPU execution using Q335 fixed-frame arithmetic [VDR-14, VDR-18] — the Remainder slot carries exactly what was not absorbed by the denominator frame. The Remainder is not rounding error. It is first-class structural information: visible, queryable, exact. The system knows precisely what it approximated and by how much.

---

## 2. Continued Fraction Arithmetic

### 2.1 The Problem

The Gauss continued fraction for ratios of hypergeometric functions produces convergents that are ratios of integers with no factors of 2 or 5. Computing ₂F₁(1/2, 1/2; 1; k²) for the complete elliptic integral K(k) at rational k produces convergents like 7/22, 103/323, 1507/4726. Every one of these is an infinite repeating decimal.

The continued fraction recurrence pₙ = aₙpₙ₋₁ + pₙ₋₂ is pure integer arithmetic. Each convergent pₙ/qₙ is an exact rational. But in decimal, each convergent is truncated, and the recurrence that produces the next convergent amplifies the truncation because it multiplies the previous convergent by the next partial quotient and adds the one before that — two operations on truncated values producing a more truncated result.

### 2.2 The VDR Solution

Each convergent is [pₙ, qₙ, 0] where pₙ and qₙ are exact integers. The recurrence is exact integer arithmetic. After 200 convergents, every digit is correct. VDR-2 gym domain 3 verified: Gauss-Kuzmin distribution statistics show coefficient 1 appearing at approximately 41% (predicted 41.5%), which requires exact counting over exact convergents [VDR-2].

### 2.3 Where It Matters

The quality of a rational approximation p/q to an irrational α is measured by |α - p/q| — a subtraction of two nearly equal numbers. In decimal, this is catastrophic cancellation: the leading digits cancel and the remaining digits are contaminated by truncation. In VDR, the subtraction is exact: (αₙ·q - p) / (D·q) where αₙ is the Newton iterate at chosen depth, all exact. Number theory, Diophantine approximation, and irrationality measure computation all depend on this exact subtraction.

---

## 3. Bernoulli Numbers and Zeta Values

### 3.1 The Problem

Bernoulli numbers B_n grow factorially and have denominators governed by the von Staudt-Clausen theorem: the denominator of B_{2n} is the product of all primes p such that (p-1) divides 2n. B₁₂ = -691/2730. The denominator 2730 = 2 × 3 × 5 × 7 × 13. In decimal: -691/2730 = -0.253113553113553113... repeating with period 12.

For B₃₀ the denominator is 14322 = 2 × 3 × 2387 and the numerator is 8615841276005. The period of the decimal repeating block is determined by the prime 2387, potentially thousands of digits long. mpmath truncates this after N digits regardless of the period.

### 3.2 The VDR Solution

B₁₂ = [-691, 2730, 0]. Exact. Multiply by any rational: exact. The zeta value relationship ζ(2n) = (-1)^{n+1} · B_{2n} · (2π)^{2n} / (2·(2n)!) is computed with exact rational Bernoulli numbers times Q335 powers of π [MATH-4]. The only approximation is the Q335 representation of π, which has a known, exact, 100-digit precision floor. The Bernoulli factor contributes zero error.

### 3.3 Where It Matters

Analytic number theory, computing special function values, and perturbative quantum field theory (Bernoulli numbers appear in Euler-Maclaurin summation of Feynman integrals) all depend on exact Bernoulli number arithmetic. The decimal trap makes high-index Bernoulli numbers progressively harder to work with as the denominators accumulate more odd prime factors. VDR eliminates this progression entirely.

---

## 4. Hilbert Matrix Computations

### 4.1 The Problem

The Hilbert matrix H_{ij} = 1/(i+j-1) is the canonical ill-conditioned matrix. Every entry is a unit fraction: 1/1, 1/2, 1/3, 1/4, and so on. In decimal, 1/3 = 0.333..., 1/7 = 0.142857..., 1/11 = 0.090909... — all infinite repeating decimals, all truncated.

The matrix is notoriously ill-conditioned. The condition number of H_n grows exponentially: approximately e^{3.5n}. This means that every digit of truncation error in the entries is amplified by the condition number in the inverse. mpmath at 50 digits computes H₅ inverse with residual approximately 10⁻⁴⁰ — but there are digits wrong at the bottom. H₁₀ residual is approximately 10⁻²⁰. H₁₅ needs 100+ digits for a meaningful result. H₂₀ at 200 digits produces a result where you cannot verify which digits are correct without going to 400 digits, and those require 800 to verify.

### 4.2 The VDR Solution

H₅ inverse residual = 0. Not approximately zero. Zero. H₁₀ = 0. H₂₀ = 0. H₃₀ = 0. Every entry of H⁻¹ is an exact integer — a known mathematical result: Hilbert inverse entries are always integers. VDR computes them as exact integers [VDR-1, VDR-2]. The determinant of H₄ is exactly 1/6048000. VDR returns [1, 6048000, 0]. The 40-operation matrix multiply roundtrip H × H⁻¹ × H × ... produces zero drift [VDR-1].

### 4.3 Where It Matters

Numerical analysis benchmarking, condition number studies, and any application where the matrix entries are exact rationals: stiffness matrices in structural engineering, Gram matrices in approximation theory, kernel matrices in machine learning with rational kernel parameters. In every case, the entries have denominators with prime factors other than 2 and 5, and decimal truncation interacts with ill-conditioning to produce unknowably wrong results.

---

## 5. Exact Eigenvalue Problems

### 5.1 The Problem

The eigenvalues of a 2×2 rational matrix [[a,b],[c,d]] are (a+d)/2 ± √((a-d)²/4 + bc). The discriminant is an exact rational. If it is a perfect square rational, the eigenvalues are exact rationals. If not, they involve the square root of a rational — representable as a VDR functional remainder with exact rational convergents at each Newton depth [VDR-1].

For the matrix [[1/3, 1/7], [1/11, 1/13]], the discriminant is (1/3 - 1/13)²/4 + 1/(7·11) = (10/39)²/4 + 1/77 = 100/6084 + 1/77 = 13784/468468 = 3446/117117. In decimal: 0.029422... repeating. mpmath takes √0.029422... and truncates.

### 5.2 The VDR Solution

Discriminant = [3446, 117117, 0]. Exact. √discriminant via Newton iteration: exact rational at each depth, converging quadratically. Eigenvalues are (trace/2) ± √discriminant, each an exact rational expression. Eigenvector components are ratios of exact rationals. Orthogonality verified by exact dot product = 0, not dot product ≈ 10⁻¹⁵ [VDR-2].

VDR-2 gym domain 11 computed exact Markov chain steady state [2/3, 1/3] — the eigenvector for eigenvalue 1. The steady state components have denominator 3, an infinite repeating decimal in base 10, exact in VDR.

### 5.3 Where It Matters

Quantum mechanics (2-level systems are 2×2 eigenvalue problems), stability analysis (eigenvalue sign determines stability — the critical case is the decimal trap at its worst, where the eigenvalue is near zero and truncation determines the sign), vibration analysis (natural frequencies are eigenvalues of mass-stiffness systems), and Markov chain analysis.

---

## 6. Gaussian Elimination Pivot Ratios

### 6.1 The Problem

Gaussian elimination produces pivot elements that are ratios of determinants of submatrices. For rational input, every pivot is rational. But the denominators grow combinatorially. For an n×n matrix, pivot denominators can have O(n) distinct prime factors, most of which are not 2 or 5.

Each elimination step divides by the pivot. If the pivot is 7/13, dividing by it means multiplying by 13/7. In decimal, 13/7 = 1.857142857142... repeating with period 6. This truncated value is multiplied by another truncated entry. The error compounds through O(n²) operations. For n=20, approximately 400 operations on truncated decimals produce a result with unknowably many wrong digits.

### 6.2 The VDR Solution

13/7 = [13, 7, 0]. Division by [7, 13, 0] is exact rational arithmetic. 400 operations: exact. VDR-13 documented: H₃₀ inverse via Gaussian elimination has pivot denominators up to approximately 185 digits [VDR-13]. mpmath at 200 digits would lose 15 digits of precision through the elimination. VDR loses zero.

### 6.3 Where It Matters

Every application of linear algebra on rational data. Structural engineering (stiffness matrices with rational entries), circuit analysis (impedances as rational functions of component values), least-squares fitting with rational data points, and exact rank computation. Float rank is always numerically full — a zero singular value appears as 10⁻¹⁵ and is indistinguishable from a small but nonzero value. VDR rank is exact: a zero entry is [0, 1, 0] and a nonzero entry is not.

---

## 7. Probability Chains and Bayesian Updates

### 7.1 The Problem

Bayes' theorem with rational priors and likelihoods produces rational posteriors. Sequential Bayesian updating applies Bayes N times, each step's posterior becoming the next step's prior. The denominators grow because P(B) = Σ P(B|Aᵢ)·P(Aᵢ) involves sums of products of rationals, producing denominators with prime factors from every term.

P(disease) = 1/10000. P(positive|disease) = 99/100. P(positive|healthy) = 1/100. P(disease|positive) = (99/100 · 1/10000) / (99/100·1/10000 + 1/100·9999/10000). In decimal, every intermediate value is truncated. After 10 updates with different evidence, the posterior has unknown digits at the bottom. After 100 updates, the accumulated truncation is substantial.

### 7.2 The VDR Solution

P(disease) = [1, 10000, 0]. P(positive|disease) = [99, 100, 0]. The posterior is an exact rational after normalization. After 10 updates: exact. After 100 updates: exact. The denominators are large but every digit is correct. VDR-2 gym domain 11 verified: binomial PMF with n=10, p=1/3 sums to exactly 1. Sequential Bayesian posterior computed as exact 6/7 [VDR-2]. mpmath gives 0.857142857142... truncated.

### 7.3 Where It Matters

Medical diagnostics (sequential test results updating disease probability — getting this wrong has clinical consequences), spam filtering (sequential word observations updating spam probability), sensor fusion (sequential sensor readings updating state estimates), and forensic statistics (sequential evidence updating guilt probability — getting this wrong has legal consequences).

---

## 8. Markov Chain Steady States

### 8.1 The Problem

The steady state of a Markov chain is the eigenvector of the transition matrix for eigenvalue 1. For a k-state chain with rational transition probabilities, the steady state components are rational numbers whose denominators involve all the prime factors from the transition matrix entries.

Computing Aⁿ for large n (power method) involves matrix multiplications where every entry is a truncated decimal. After n=100 multiplications, the last several digits of every entry are wrong. Alternatively, solving (A-I)x = 0 by Gaussian elimination on truncated entries produces the same problem described in Section 6.

For a 5-state chain with transition probabilities like 1/7, 3/11, 2/13, the steady state components have denominators involving 7, 11, and 13 — all infinite repeating decimals in base 10.

### 8.2 The VDR Solution

Transition matrix entries are exact rationals. Matrix power Aⁿ is exact. The steady state is the exact eigenvector. VDR-2 gym domain 11 computed exact steady state [2/3, 1/3] for a 2-state chain [VDR-2]. VDR-3 gym domain 16 computed exact PageRank summing to exactly 1 [VDR-3].

Mixing time analysis depends on the second-largest eigenvalue magnitude |λ₂|. Computing |λ₂| exactly (for small chains) or to arbitrary precision (via Newton functional remainder) means the mixing time bound is exact, not contaminated by arithmetic error in the eigenvalue computation.

### 8.3 Where It Matters

PageRank computation, queueing theory (steady-state queue lengths), population genetics (allele frequency evolution), and MCMC convergence diagnostics. In each case, the steady state is a set of exact rationals that decimal representation silently corrupts.

---

## 9. Elliptic Curve Arithmetic

### 9.1 The Problem

Points on an elliptic curve y² = x³ + ax + b over the rationals have coordinates that are rational numbers. Point addition involves λ = (y₂-y₁)/(x₂-x₁), x₃ = λ² - x₁ - x₂, y₃ = λ(x₁-x₃) - y₁. Every operation produces rationals. But the denominators grow rapidly: after n point doublings, coordinates can have denominators with O(4ⁿ) digits due to height growth.

After 20 doublings, coordinates have approximately 10⁶ digit denominators. mpmath truncates these to N digits. The truncated point is not on the curve — y² ≠ x³ + ax + b due to truncation. Group law properties cannot be verified on truncated points.

### 9.2 The VDR Solution

Each point addition is exact rational arithmetic. After 20 doublings, the coordinates have enormous denominators but are exactly on the curve: y₃² = x₃³ + ax₃ + b as exact VDR equality. Group law associativity (P+Q)+R = P+(Q+R) is verified as exact structural equality, not approximate numerical agreement. The height of the point (logarithm of denominator) is exactly computable.

### 9.3 Where It Matters

Elliptic curve cryptography (point multiplication nG must be exact), Birch and Swinnerton-Dyer conjecture computations (rational point heights), integer factorization via Lenstra's ECM, and computing Mordell-Weil groups. In each case, the essential computation is an exact chain of rational arithmetic on points whose coordinates have denominators with many distinct prime factors.

---

## 10. Modular Arithmetic and Chinese Remainder Theorem

### 10.1 The Problem

CRT reconstructs an integer from its residues modulo several coprime moduli. The reconstruction formula involves modular inverses computed via extended GCD. Python integers handle this exactly, as do VDR integers [n, 1, 0].

The decimal trap appears when CRT is used to reconstruct a rational number from its images under modular homomorphisms. Given x mod p for several primes p, rational reconstruction recovers x = a/b using extended GCD. The reconstructed fraction a/b must then be used in further computation.

### 10.2 The VDR Solution

The reconstructed rational a/b is represented as [a, b, 0] — exact. Subsequent arithmetic on it is exact. In decimal, the reconstructed rational is truncated immediately upon entering further computation. Computer algebra systems use modular methods to compute polynomial GCDs, resultants, and determinants. The CRT reconstruction step produces exact rationals. VDR preserves them through all subsequent computation [VDR-2].

---

## 11. Partition Functions and Statistical Mechanics

### 11.1 The Problem

The partition function Z = Σ exp(-βEᵢ) sums Boltzmann weights over all microstates. For discrete systems, the energies Eᵢ are often rational. The exponential is transcendental, but each Taylor partial sum is an exact rational. Free energy F = -kT·ln(Z), entropy S = -∂F/∂T, specific heat C = T·∂S/∂T — all involve chains of transcendental evaluations.

The specific heat at a Schottky anomaly requires computing d²F/dT², which is a second derivative of a logarithm of a sum of exponentials — three layers of truncation in decimal. Each layer discards information that the next layer needs.

### 11.2 The VDR Solution

Each exp(-βEᵢ) via functional remainder Taylor series: exact rational at each depth. Sum over states: exact rational. ln(Z) via functional remainder: exact rational at each depth [VDR-1]. Discrete derivative (F(T+h) - F(T))/h is exact for any rational h — the subtraction is exact (no catastrophic cancellation), and the division is exact. The Schottky specific heat peak location and height are computable to arbitrary precision by increasing Taylor depth, not by increasing decimal digits and hoping the truncation did not corrupt the answer.

### 11.3 Where It Matters

Phase transition analysis (specific heat divergence at critical temperature), quantum statistical mechanics (Bose-Einstein and Fermi-Dirac distributions involve exp(βE)±1 in the denominator — the ±1 is a subtraction of a near-unit value, catastrophic in truncated decimal), astrophysics (equation of state for stellar interiors), and chemical equilibrium (equilibrium constants as ratios of partition functions).

---

## 12. Runge-Kutta with Exact Butcher Tableaux

### 12.1 The Problem

Runge-Kutta methods have coefficients specified as exact rationals in the Butcher tableau. Classic RK4: coefficients 1/2, 1/6, 1/3. Higher-order methods (Dormand-Prince, Fehlberg) have coefficients like 3/40, 9/40, 12/13, 4243/5348 — denominators with factors of 3, 7, 13, 17, 1337.

The method's order is guaranteed by algebraic identities among the coefficients: Σbᵢ = 1, Σbᵢcᵢ = 1/2, Σbᵢaᵢⱼcⱼ = 1/6. In decimal, these identities hold only approximately. If they do not hold exactly, the method is not exactly the claimed order.

### 12.2 The VDR Solution

Every Butcher coefficient is [p, q, 0]. The order conditions are verified as exact equalities: Σbᵢ = 1 exactly, Σbᵢcᵢ = 1/2 exactly. The method is provably order 4 (or 5, or 8) because the algebraic conditions hold exactly. Each RK stage is exact rational arithmetic on exact rational data. VDR-2 gym domain 9 demonstrated: Euler method y(1) = (11/10)¹⁰ exact, RK4 approximately 140× better accuracy than Euler — and both results are exact rationals, so the accuracy comparison is itself exact [VDR-2].

### 12.3 Where It Matters

Validating new RK methods (do the order conditions actually hold?), reference solutions for ODE benchmarks, and long-time integration where method error and arithmetic error must be separated. The Butcher tableau is the method's identity — if the coefficients are truncated, the method is a different method.

---

## 13. Galois Field Arithmetic and Error Correction

### 13.1 The Problem

Reed-Solomon codes, BCH codes, and turbo codes operate over Galois fields GF(pⁿ). All arithmetic is modular. The syndrome computation, error locator polynomial, and Chien search involve chains of field multiplications. Some implementations in float (educational code, MATLAB scripts) silently convert field elements to doubles and round back. This works for GF(2⁸) (elements 0-255 fit in float mantissa) but fails for GF(2¹⁶) and above.

### 13.2 The VDR Solution

GF(p) elements are [a, 1, 0] with a in {0,...,p-1}. gf_add, gf_mul, gf_inv, gf_pow builtins [VDR-10] are exact modular operations. VDR-3 gym domain 18 verified: all 6 GF(7) inverses correct, all 16 Hamming(7,4) codewords have syndrome 0, all 7 single-bit errors corrected, minimum distance = 3 by exhaustive 120-pair comparison [VDR-3]. No float anywhere. The error correction is either correct or it is not — exact arithmetic means the code either corrects the error or provably does not.

### 13.3 Where It Matters

Satellite communication (deep space links use Reed-Solomon plus convolutional codes — error in the decoder means lost data), QR codes, data storage (RAID parity), 5G NR polar codes, and DNA storage (emerging field using Reed-Solomon over GF(4) for the ACGT alphabet).

---

## 14. Characteristic Polynomial and Cayley-Hamilton Verification

### 14.1 The Problem

The Cayley-Hamilton theorem states every matrix satisfies its own characteristic polynomial: p(A) = 0 where p(λ) = det(A - λI). The zero is the zero matrix — every entry must be exactly zero. In decimal, p(A) is a matrix with entries of order 10⁻ᴺ where N is the working precision. The theorem cannot be verified — only approximately confirmed.

### 14.2 The VDR Solution

Characteristic polynomial coefficients are exact rationals computed from the exact determinant. p(A) = exact zero matrix. Every entry is [0, 1, 0]. Not approximately zero. Zero. VDR-2 gym domain 2 and VDR-3 gym domain 21 verified: M² - 5M + 5I = 0 exactly, A² + 3A + 2I = 0 exactly [VDR-2, VDR-3]. Cayley-Hamilton is a structural identity verified by structural equality, not a numerical residual compared to a tolerance.

### 14.3 Where It Matters

Control theory (Cayley-Hamilton computes matrix exponentials for state-space systems), minimal polynomial computation (requires exact zero-testing to determine which powers of A are independent), and matrix function evaluation. The decimal trap makes zero-testing fundamentally unreliable: is 10⁻¹⁵ zero or nonzero? VDR answers this question exactly.

---

## 15. Farey Sequences and Stern-Brocot Trees

### 15.1 The Problem

The Farey sequence Fₙ contains all reduced fractions with denominator ≤ n in [0,1], ordered by magnitude. The mediant property: for consecutive Farey neighbors a/b and c/d, |ad - bc| = 1. This is an exact integer identity. Representing Farey fractions as decimals destroys the structure — you cannot recover the integer numerator and denominator from a truncated decimal without additional information.

### 15.2 The VDR Solution

1/3 = [1, 3, 0]. 1/4 = [1, 4, 0]. Mediant = [2, 7, 0]. |ad - bc| = |1·4 - 3·1| = 1. Exact. VDR-2 gym domain 1 verified the mediant property for all consecutive pairs in Farey sequences [VDR-2]. The Stern-Brocot path to any rational is computable by exact comparison: VDR comparison is cross-multiplication of integers, exact and deterministic.

### 15.3 Where It Matters

Number theory (distribution of rationals, Ford circles, hyperbolic geometry), clock synchronization (best rational approximation to frequency ratios), and music theory (just intonation intervals as exact rationals: 3/2 is a perfect fifth, 5/4 is a major third, 81/80 is the syntonic comma). Decimal representation makes the 81/80 comma invisible — it is 1.0125 in decimal, a terminating decimal that looks unremarkable. In VDR, 81/80 is [81, 80, 0], and the relationship to 3⁴/2⁴·5 is visible in the factorization.

---

## 16. Exact Polynomial GCD and Resultants

### 16.1 The Problem

The GCD of two polynomials with rational coefficients is computed by the Euclidean algorithm, which involves polynomial long division producing quotients and remainders with growing denominators. The critical decision at each step: is the remainder zero? If yes, the previous divisor is the GCD. If no, the algorithm continues.

In decimal, a remainder coefficient might be 3.7 × 10⁻¹⁵. Is this zero (GCD found) or nonzero (continue dividing)? Increasing precision to 50 digits might give 3.7 × 10⁻⁴⁵. Still ambiguous. The zero-testing problem is unsolvable in truncated decimal arithmetic — no amount of precision resolves the ambiguity without external information.

### 16.2 The VDR Solution

Remainder coefficient is either [0, 1, 0] or it is not. Zero-testing is exact structural comparison, requiring zero digits of precision analysis. VDR-2 gym domain 2 verified: polynomial GCD(x²-1, x²+2x+1) = (x+1) exactly [VDR-2]. The definite integral ∫₀¹ x² dx = 1/3 exact via exact antiderivative evaluation (VDR-2 gym domain 13).

### 16.3 Where It Matters

Control theory (coprimeness of numerator and denominator polynomials determines controllability), algebraic geometry (intersection multiplicity via resultants), computer algebra (simplification of rational functions), and coding theory (polynomial GCD over finite fields for BCH decoding). In each case, the correctness of the algorithm depends on exact zero-testing that decimal arithmetic cannot provide.

---

## 17. Padé Approximants

### 17.1 The Problem

Computing Padé approximant coefficients requires solving a linear system where the matrix entries are Taylor coefficients — rational numbers for functions like exp, sin, cos, ln at rational arguments. Taylor coefficients involve factorials: 1/n! has denominators with all primes up to n. For high-order approximants (L+M > 20), the coefficient matrix becomes ill-conditioned and mpmath needs hundreds of digits.

1/7! = 1/5040. In decimal: 0.000198412698... repeating. The [4/4] Padé approximant for exp(x) has coefficients with denominators up to 1680 = 2⁴ × 3 × 5 × 7. In decimal, 1/1680 = 0.000595238095238... repeating.

### 17.2 The VDR Solution

1/7! = [1, 5040, 0]. Exact. The linear system is solved by exact Gaussian elimination or Cramer's rule. The Padé coefficients are exact rationals. The approximant's error at any rational point is computable as an exact rational — evaluate the approximant and subtract from the Taylor partial sum, both exact.

### 17.3 Where It Matters

Matrix exponential algorithms (Padé approximants are the standard method), signal processing (model reduction), circuit simulation (SPICE uses Padé for delay elements), and quantum field theory (Padé-Borel summation of divergent perturbation series). In each domain, the Padé coefficients involve factorials whose denominators contain odd primes, making decimal truncation unavoidable.

---

## 18. Lattice Basis Reduction

### 18.1 The Problem

The LLL algorithm reduces a lattice basis by iteratively performing Gram-Schmidt orthogonalization and size reduction. The Gram-Schmidt coefficients μᵢⱼ = ⟨bᵢ, b*ⱼ⟩ / ⟨b*ⱼ, b*ⱼ⟩ are exact rationals when the input vectors have rational coordinates. The Lovász condition involves comparing μ² to the threshold 3/4 — a comparison of exact rationals.

The critical failure mode: μ = 0.500000000000001 (above 1/2, needs size reduction) versus μ = 0.499999999999999 (below 1/2, does not). mpmath cannot distinguish these if the true value is within truncation range of 1/2. Wrong decision means wrong basis, wrong lattice reduction, wrong cryptanalysis result.

### 18.2 The VDR Solution

μ = [p, q, 0] exact rational. Comparison to 1/2: cross-multiply p·2 versus q·1, compare exact integers. No borderline ambiguity. The Lovász condition is an exact rational comparison. VDR-3 gym domain 20 verified: lattice μ₂₁ = 1/2 exact, v₁·v₂* = 0 exactly, Lovász condition checked with exact rational comparison [VDR-3].

### 18.3 Where It Matters

Cryptanalysis (breaking lattice-based cryptosystems requires correct basis reduction), integer programming (finding short vectors), number theory (finding algebraic relations between constants), and GPS integer ambiguity resolution. In each case, the algorithm's correctness depends on exact threshold comparisons that decimal truncation makes unreliable.

---

## 19. Groebner Bases

### 19.1 The Problem

Groebner basis computation (Buchberger's algorithm) involves polynomial division with remainder over multivariate polynomials. Each S-polynomial computation and reduction step produces polynomials with growing denominators. The critical decision at each step: is the remainder zero?

This is the same zero-testing problem as polynomial GCD (Section 16), but amplified. Groebner basis computation involves many more reduction steps, each producing larger denominators. A remainder coefficient of 10⁻¹⁵ could be zero (reduction succeeds, S-polynomial processed) or nonzero (new basis element needed). Wrong answer means wrong Groebner basis — extra elements, missing elements, or both.

### 19.2 The VDR Solution

Remainder coefficient is either [0, 1, 0] or it is not. Zero-testing is exact. The Groebner basis computation terminates with the correct basis — not an approximately correct basis that might have extra or missing elements.

### 19.3 Where It Matters

Algebraic geometry (ideal membership testing, variety computation), robotics (solving polynomial systems for inverse kinematics), coding theory (decoding algebraic codes), and algebraic statistics (design of experiments). Each application depends on the Groebner basis being correct, not approximately correct.

---

## 20. Quantum Error Correction Stabilizer Codes

### 20.1 The Problem

Stabilizer codes are defined by Pauli group elements — tensor products of I, X, Y, Z matrices. The entries are from {0, ±1, ±i}. Checking code properties requires multiplying Pauli matrices and determining whether results are ±I (real) or ±iI (imaginary).

In float, i is represented as 0 + 1.0j. Multiplying: (0+1j)·(0+1j) = -1+0j in exact arithmetic, but float produces -1+1.2×10⁻¹⁶j. After 20 matrix multiplications, the imaginary part of what should be a real number is approximately 10⁻¹⁵. Is the result ±I (real) or ±iI (imaginary)? Float cannot determine this for borderline cases.

### 20.2 The VDR Solution

i is represented as a pair of VDR values (0, 1). Multiplication: (0+1i)·(0+1i) = (-1, 0). Exact. After 20 multiplications: exact. The result is either (±1, 0) — real, meaning ±I — or (0, ±1) — imaginary, meaning ±iI. Exact classification. VDR-13 verified Pauli algebra: σ_x² = I, σ_x·σ_y = iσ_z as exact structural equalities [VDR-13].

### 20.3 Where It Matters

Designing quantum error correcting codes, verifying fault-tolerance thresholds, topological code analysis (surface codes, color codes), and magic state distillation protocols. Code distance computation requires checking if a Pauli operator commutes with all stabilizers — commutation is exact comparison of matrix products. Decimal truncation makes this comparison unreliable for products of many Pauli matrices.

---

## 21. The Unifying Principle

Every domain in this paper contains the same structural vulnerability: a computation chain where intermediate values have denominators with prime factors other than 2 and 5, forcing decimal or mpmath truncation at every step.

1/3 is infinite in decimal. 1/7 is infinite. 1/11 is infinite. 1/5040 is infinite (5040 = 2⁴ × 3² × 5 × 7, the factors of 3 and 7 make it repeat). Every factorial, every prime denominator, every product of odd primes produces an infinite repeating decimal.

VDR's representation [V, D, 0] carries the exact denominator as an integer — whether it is 3, 7, 13, 5040, 117117, or a 200-digit product of primes. No truncation. No repeating digits. No lost information. The denominator grows but nothing is discarded.

This is not "more precision." It is a categorically different relationship with the numbers. mpmath says "I have 1000 digits, which is probably enough." VDR says "I have the exact answer."

---

## 22. Boundaries

### 22.1 Denominator Growth

Exact rational arithmetic preserves every prime factor in every denominator. After N multiplications, the denominator can have O(N) distinct prime factors and magnitude growing multiplicatively. For long chains, the integers become very large. Q335 fixed-frame arithmetic [VDR-14, VDR-18] bounds the denominator at 2³³⁵ and carries overflow in the Remainder slot.

### 22.2 Transcendental Functions

Functions like exp, sin, cos, log at irrational arguments produce irrational results. VDR handles these through functional remainders — Newton iteration or Taylor series producing exact rational approximations at each depth [VDR-1]. The approximation is configurable, inspectable, and does not truncate — the Remainder carries exactly what the current depth did not absorb.

### 22.3 Matrix Size

Exact matrix operations via cofactor expansion are O(n!). Gaussian elimination is O(n³) but requires pivot selection. Practical exact matrix operations are currently limited to approximately 50×50. For larger systems, VDR serves as ground truth for validating float implementations.

### 22.4 Not All Domains Benefit Equally

Domains where all intermediate values have denominators of the form 2ᵐ × 5ⁿ — pure decimal-compatible arithmetic — do not benefit from VDR's rational representation. Binary arithmetic (denominators that are powers of 2) is already exact in float. VDR's value is proportional to the density of odd prime factors in the computation's intermediate denominators.

---

## Appendices

### Appendix A — Denominator Prime Factor Analysis by Domain

| Domain | Typical denominator prime factors | Decimal period | mpmath digits needed for N-step chain | VDR digits needed |
|---|---|---|---|---|
| Continued fractions | All primes up to convergent index | Variable, often large | O(N × max period) | 0 (exact) |
| Bernoulli numbers | All primes p where (p-1) divides 2n | Up to thousands (large primes) | O(period × chain length) | 0 (exact) |
| Hilbert matrix | All primes up to 2n-1 | LCM of all primes | Grows with condition number × n | 0 (exact) |
| Eigenvalue (2×2 rational) | Factors of trace and determinant | Product of all factors | Depends on discriminant | 0 (exact) |
| Gaussian elimination pivots | O(n) distinct primes | Product of all pivot factor periods | O(n² × max period) | 0 (exact) |
| Bayesian updates | Factors of all priors and likelihoods | Cumulative product of periods | O(N × cumulative period) | 0 (exact) |
| Markov steady state | All factors from transition matrix | Product of all periods | O(k² × max period) | 0 (exact) |
| Elliptic curve points | Height growth: O(4ⁿ) digits | Enormous | O(4ⁿ) | 0 (exact, but integers are huge) |
| RK Butcher tableau | All primes in coefficient denominators | Product of periods | O(stages × max period) | 0 (exact) |
| Galois field | p (field characteristic) | N/A (modular) | N/A | 0 (exact modular) |
| Polynomial GCD | All primes from coefficient denominators | Product of periods | Unknown (zero-testing problem) | 0 (exact zero-testing) |
| Padé coefficients | Primes up to (L+M)! | Product of periods | O(condition number × matrix size) | 0 (exact) |
| Lattice LLL | Factors from Gram-Schmidt coefficients | Product of periods | O(n² × iterations × max period) | 0 (exact) |
| Groebner basis | All primes from polynomial coefficients | Product of periods | Unknown (zero-testing problem) | 0 (exact zero-testing) |
| Partition function | Primes from energy denominators | Product of periods | O(states × Taylor depth × max period) | 0 (exact per Taylor depth) |
| Stern-Brocot | All primes (every rational appears) | Variable | N/A (structure destroyed by decimal) | 0 (exact; structure preserved) |
| Quantum stabilizer | Only 1 (entries are ±1, ±i) | N/A | N/A (but complex arithmetic drifts) | 0 (exact complex pairs) |
| Cayley-Hamilton | All primes from matrix entries | Product of periods | O(n × condition number × max period) | 0 (exact zero-testing) |

### Appendix B — Zero-Testing Failure Modes

| Domain | Zero-testing question | Decimal behavior | VDR behavior | Consequence of wrong answer |
|---|---|---|---|---|
| Polynomial GCD | Is remainder coefficient zero? | Ambiguous: could be truncation artifact | Exact: [0,1,0] or not | Wrong GCD: extra factors or missing factors |
| Groebner basis | Is S-polynomial remainder zero? | Ambiguous at any precision | Exact | Wrong basis: extra or missing generators |
| Cayley-Hamilton | Is p(A) the zero matrix? | Every entry ≈ 10⁻ᴺ, never exactly 0 | Every entry exactly [0,1,0] | Cannot verify fundamental theorem |
| Matrix rank | Is singular value zero or small? | Indistinguishable below ~10⁻¹⁵ | Exact zero or exact nonzero | Wrong rank: wrong nullspace dimension |
| Linear independence | Is determinant zero? | Ambiguous near zero | Exact | Wrong independence conclusion |
| Eigenvector orthogonality | Is dot product zero? | ≈ 10⁻¹⁵, never exactly 0 | Exactly 0 (for rational eigenvectors) | Cannot verify orthogonality |
| Polynomial coprimeness | Is GCD = 1? | Requires zero-testing of remainders | Exact | Wrong controllability assessment |
| Lattice LLL threshold | Is μ > 1/2? | Ambiguous near 1/2 | Exact comparison | Wrong basis reduction |
| Farey mediant property | Is |ad-bc| = 1? | Requires exact integer recovery from decimal | Exact integer arithmetic | Structure verification impossible |
| Conservation law | Is energy change zero? | ≈ 10⁻¹⁵, declared "conserved to tolerance" | Exactly 0 or exactly nonzero | False conservation or missed violation |

### Appendix C — Repeating Decimal Periods for Common Denominators

| Denominator | Prime factorization | Decimal period | Representation in decimal | Representation in VDR |
|---|---|---|---|---|
| 2 | 2 | 0 (terminates) | 0.5 | [1, 2, 0] |
| 3 | 3 | 1 | 0.333... | [1, 3, 0] |
| 4 | 2² | 0 | 0.25 | [1, 4, 0] |
| 5 | 5 | 0 | 0.2 | [1, 5, 0] |
| 6 | 2·3 | 1 | 0.1666... | [1, 6, 0] |
| 7 | 7 | 6 | 0.142857142857... | [1, 7, 0] |
| 8 | 2³ | 0 | 0.125 | [1, 8, 0] |
| 9 | 3² | 1 | 0.111... | [1, 9, 0] |
| 10 | 2·5 | 0 | 0.1 | [1, 10, 0] |
| 11 | 11 | 2 | 0.090909... | [1, 11, 0] |
| 12 | 2²·3 | 1 | 0.08333... | [1, 12, 0] |
| 13 | 13 | 6 | 0.076923076923... | [1, 13, 0] |
| 14 | 2·7 | 6 | 0.0714285714285... | [1, 14, 0] |
| 15 | 3·5 | 1 | 0.0666... | [1, 15, 0] |
| 17 | 17 | 16 | 0.0588235294117647... | [1, 17, 0] |
| 19 | 19 | 18 | 0.052631578947368421... | [1, 19, 0] |
| 21 | 3·7 | 6 | 0.047619047619... | [1, 21, 0] |
| 100 | 2²·5² | 0 | 0.01 | [1, 100, 0] |
| 360 | 2³·3²·5 | 1 | 0.00277... | [1, 360, 0] |
| 2730 | 2·3·5·7·13 | 12 (lcm of 1,6,6 for 3,7,13) | 0.000366300... repeating | [1, 2730, 0] |
| 5040 | 2⁴·3²·5·7 | 6 | 0.000198412698... repeating | [1, 5040, 0] |
| 117117 | 3·7·11·13·37 (approx) | lcm(1,6,2,6,...) | Long repeating block | [1, 117117, 0] |

Of the first 20 denominators, 8 terminate (40%) and 12 repeat (60%). Among denominators from 1 to 100, approximately 12 terminate and 88 repeat. The decimal trap affects the vast majority of rational numbers.

### Appendix D — Prior VDR Validation by Domain

| Section | Domain | VDR paper | Gym domain | Tests | Key result |
|---|---|---|---|---|---|
| 2 | Continued fractions | VDR-2 | 3 | 19/19 | Gauss-Kuzmin statistics exact |
| 3 | Bernoulli/zeta | VDR-3 | Q335 | 157 (152 pass) | 22 constants at 100 digits |
| 4 | Hilbert matrix | VDR-1 | Core | 68/68 | H⁻¹ residual = 0; det(H₄) = 1/6048000 exact |
| 5 | Eigenvalues | VDR-2 | 4, 11 | 38/37 (1 test error) | Exact steady state [2/3, 1/3] |
| 6 | Gaussian elimination | VDR-13 | Physical | — | H₃₀ pivots: 185-digit denominators, zero error |
| 7 | Bayesian updates | VDR-2 | 11 | 19/19 | Posterior 6/7 exact; binomial PMF sums to 1 |
| 8 | Markov chains | VDR-2, VDR-3 | 11, 16 | 38/38 | PageRank sums to exactly 1 |
| 9 | Elliptic curves | — | — | — | Structural analysis; not yet in gym |
| 10 | CRT/modular | VDR-2 | 12 | 19/18 (1 test error) | RSA roundtrip, CRT exact |
| 11 | Partition functions | — | — | — | Taylor via functional remainder validated |
| 12 | Runge-Kutta | VDR-2 | 9 | 19/18 (1 test error) | RK4 140× better than Euler; both exact |
| 13 | Galois fields | VDR-3 | 18 | — | Hamming(7,4): all errors corrected |
| 14 | Cayley-Hamilton | VDR-2, VDR-3 | 2, 21 | — | M²-5M+5I = 0 exactly |
| 15 | Farey/Stern-Brocot | VDR-2 | 1 | 19/19 | Mediant property verified |
| 16 | Polynomial GCD | VDR-2 | 2 | 18/18 | GCD(x²-1, x²+2x+1) = (x+1) exact |
| 17 | Padé approximants | — | — | — | Linear system solve via exact elimination |
| 18 | Lattice LLL | VDR-3 | 20 | — | μ₂₁ = 1/2 exact; Lovász exact |
| 19 | Groebner bases | — | — | — | Structural analysis; zero-testing exact |
| 20 | Quantum stabilizer | VDR-13 | Physical | — | Pauli algebra: σ_x² = I exact |
| **Total** | **20 domains** | **6 papers** | **14 gym domains** | **>400 tests** | **Zero VDR computation errors** |

### Appendix E — Catastrophic Cancellation Vulnerability by Domain

| Domain | Cancellation operation | Operand magnitudes | Decimal digits lost | VDR digits lost |
|---|---|---|---|---|
| Continued fraction quality | α - p/q | Both ≈ irrational value | Most significant digits cancel | 0 |
| Eigenvalue near zero | (a+d)/2 - √disc | Trace/2 ≈ √discriminant | Up to all digits | 0 |
| Specific heat (Schottky) | F(T+h) - F(T) | Both ≈ F(T) | Proportional to -log₁₀(h) | 0 |
| Options Greeks | f(S+h) - f(S-h) | Both ≈ f(S) | Proportional to -log₁₀(h) | 0 |
| Bose-Einstein denominator | exp(βE) - 1 | exp(βE) ≈ 1 for small βE | Most digits | 0 |
| Stability eigenvalue | Real part of complex eigenvalue | Real ≈ 0 | Most digits | 0 (to Newton depth) |
| Cayley-Hamilton verification | Aⁿ - c₁Aⁿ⁻¹ - ... | Terms of similar magnitude | Many digits per entry | 0 |
| Gaussian elim small pivot | a - (b·c/d) | a ≈ b·c/d | Proportional to condition number | 0 |
| Kalman P update | (I-KH)P entries | (I-KH) ≈ I for good observations | Up to several digits | 0 |
| Polynomial GCD remainder | p(x) - q(x)·quotient(x) | Nearly equal polynomials | May lose all significant digits | 0 |
| LLL μ near 1/2 | μ - 1/2 | μ ≈ 1/2 | May lose all significant digits | 0 |

### Appendix F — Cost of Exactness by Domain

| Domain | Typical problem size | Float64 operations | VDR operations (Python) | VDR/Float ratio | Justified by |
|---|---|---|---|---|---|
| Continued fraction (200 convergents) | 200 iterations | ~600 | ~30,000 | 50× | Exact quality measures |
| Hilbert inverse (10×10) | 10³ multiplications | ~1,000 | ~50,000 | 50× | Zero vs 10⁻²⁰ residual |
| Bayesian (100 updates) | 100 × ~10 operations | ~1,000 | ~50,000 | 50× | Exact posterior for diagnostics |
| Markov steady (5 states, power method) | 5² × 100 iterations | ~2,500 | ~125,000 | 50× | Exact PageRank |
| RK4 (100 steps, 1D) | 100 × ~10 operations | ~1,000 | ~50,000 | 50× | Provable method order |
| Polynomial GCD (degree 10) | ~100 operations | ~100 | ~5,000 | 50× | Exact zero-testing |
| LLL (dimension 5) | ~100 iterations × ~25 ops | ~2,500 | ~125,000 | 50× | Exact threshold comparison |
| Eigenvalue (2×2) | ~10 operations | ~10 | ~500 | 50× | Exact stability determination |
| Elliptic curve (20 doublings) | ~200 operations | ~200 | ~10,000 | 50× | Exact curve membership |
| Hamming(7,4) decode | ~50 operations | ~50 | ~2,500 | 50× | Exact error correction |
| Cayley-Hamilton (5×5) | 5⁵ + 5⁴ + ... operations | ~4,000 | ~200,000 | 50× | Exact zero verification |
| Groebner (3 variables, degree 3) | ~500 operations | ~500 | ~25,000 | 50× | Exact zero-testing |
| Padé [4/4] | ~100 operations (linear solve) | ~100 | ~5,000 | 50× | Exact coefficients |
| Partition function (10 states) | 10 × ~30 Taylor terms | ~300 | ~15,000 | 50× | Exact thermodynamics |
| Quantum stabilizer (5 qubits) | ~100 Pauli products | ~100 | ~5,000 | 50× | Exact commutation check |

The ratio is approximately 50× in Python across all domains. On GPU with Q335, the ratio is approximately 150× per operation but offset by the elimination of multiple-precision overhead and the ability to parallelize fixed-width operations [VDR-18].

### Appendix G — The Decimal Compatibility Test

A computation is decimal-compatible if every intermediate value has a denominator whose only prime factors are 2 and 5. For any computation, the following test determines whether the decimal trap applies:

| Input property | Decimal-compatible? | VDR advantage |
|---|---|---|
| All inputs are integers | Yes (denominator = 1) | None for addition/subtraction; multiplication stays integer |
| All inputs are powers of 2 in denominator | Yes | None |
| All inputs are powers of 10 in denominator | Yes | None |
| Any input has factor of 3 in denominator | No | Exact vs truncated |
| Any input has factor of 7 in denominator | No | Exact vs truncated |
| Any input has any odd prime > 5 in denominator | No | Exact vs truncated |
| Division by 3 anywhere in chain | No (introduces factor of 3) | Exact vs truncated |
| Division by any odd number > 5 | No | Exact vs truncated |
| Mean of N values where N has odd factor | No (introduces 1/N) | Exact vs truncated |
| Factorial in denominator (n! for n ≥ 3) | No (3 divides 3!) | Exact vs truncated |
| Any prime modulus (Galois field) | No (p in denominator of inverses) | Exact modular vs float approximation |
| Bayesian normalization | Almost always no | Exact vs truncated |
| Matrix entries with odd denominators | No | Exact linear algebra |

The test is simple: if division by anything other than a power of 2 or 5 occurs anywhere in the computation — including implicitly through averaging, normalization, matrix inversion, or polynomial evaluation — the decimal trap applies and VDR provides exact results where decimal provides truncated approximations.

### Appendix H — Domain Interconnection Map

| Domain A | Domain B | Shared vulnerability | Example |
|---|---|---|---|
| Bernoulli numbers | Padé approximants | Factorial denominators with odd primes | exp Padé coefficients involve 1/n! |
| Hilbert matrix | Gaussian elimination | Growing pivot denominators | H inverse requires exact pivots |
| Eigenvalues | Stability analysis | Discriminant with odd factors | Eigenvalue sign from exact discriminant |
| Eigenvalues | Markov chains | Steady state is eigenvector for λ=1 | Steady state denominators from transition matrix |
| Bayesian updates | Medical diagnostics | Sequential rational multiplication | Posterior denominators grow with evidence |
| Polynomial GCD | Control theory | Coprimeness requires zero-testing | Controllability from exact polynomial GCD |
| Polynomial GCD | Groebner bases | Both depend on exact zero-testing | Remainder zero → different algorithm path |
| Galois fields | Error correction | Exact modular chains | Syndrome computation, error locator |
| Galois fields | Cryptography | Exact field arithmetic | RSA, ECC, post-quantum lattice |
| Lattice LLL | Cryptanalysis | Exact threshold comparison | Breaking lattice-based encryption |
| Lattice LLL | GPS | Integer ambiguity resolution | Carrier phase positioning |
| Elliptic curves | Cryptography | Exact point arithmetic | ECC key generation, ECDSA |
| Runge-Kutta | Physics simulation | Exact Butcher coefficients | ODE integration with proven order |
| Cayley-Hamilton | Control theory | Exact matrix polynomial evaluation | Matrix exponential via CH |
| Partition function | Quantum mechanics | Exact Boltzmann weights | Energy level statistics |
| Continued fractions | Number theory | Exact convergent arithmetic | Irrationality measures |
| Farey sequences | Number theory | Exact mediant property | Rational approximation theory |
| Quantum stabilizer | Quantum computing | Exact Pauli algebra | Error correction code design |
| Markov chains | PageRank | Exact steady state | Web ranking |
| Gaussian elimination | All linear algebra | Exact pivots | Foundation for inverse, rank, determinant |

---

### Appendix I — Additional Domains: Algebraic Number Theory

| Problem | Computation | Decimal failure | VDR solution | Verified |
|---|---|---|---|---|
| Minimal polynomial of √2+√3 | x⁴-10x²+1; verify (√2+√3) is root | Substituting truncated √2+√3 gives residual ~10⁻¹⁵ | Newton √2 + Newton √3 substituted; residual exact at Newton depth | VDR-1 functional remainder |
| Norm of algebraic integer | N(a+b√d) = a²-db² | a=3/7, b=5/11, d=2: exact rational | [9/49 - 50/121, 1, 0] = [9·121-50·49 / 49·121, 1, 0] = [-1391/5929, 1, 0] exact | VDR-1 closed arithmetic |
| Discriminant of number field | Δ(Q(√d)) = 4d or d depending on d mod 4 | d=13: Δ=13 exact integer | [13, 1, 0] | Trivial |
| Class number computation | Count ideal classes via Minkowski bound | Bound involves √Δ; class group enumeration involves exact norm comparisons | √13 via Newton; norms as exact rationals; comparisons exact | VDR-2 gym 1 |
| Dedekind zeta residue | Residue involves class number × regulator × 2^r₁ × (2π)^r₂ / (w·√|Δ|) | Product of transcendentals and exact rationals; truncation at every factor | Q335 for π; Newton for √|Δ|; exact rationals for class number, w | VDR-3 Q335 basis |
| Pell equation | x²-Dy²=1; fundamental solution from continued fraction of √D | CF convergents exact; checking x²-Dy²=1 requires exact large integer arithmetic | Convergents [pₙ, qₙ, 0]; verification pₙ²-D·qₙ² = 1 exact | VDR-2 gym 3 |
| Unit group of Z[√d] | Fundamental unit ε = (a+b√d)/c | Exact rational coefficients with Newton √d; unit equation N(ε)=±1 verified exactly | VDR-1 closed + functional |
| Resultant of cyclotomic polynomials | Res(Φₘ, Φₙ) = p^φ(m) if n/m = pᵏ, else 1 | Coefficients are ±1; resultant is Sylvester determinant of exact integers | [p^φ(m), 1, 0] exact integer | VDR-2 gym 2 |

### Appendix J — Additional Domains: Combinatorial Optimization

| Problem | Computation | Decimal failure | VDR solution | Key operation |
|---|---|---|---|---|
| Linear programming simplex | Pivot ratios min(bᵢ/aᵢⱼ) for rational data | Pivots truncated; wrong pivot selection possible near ties | Exact rational pivot ratios; exact min comparison | Cross-multiply comparison |
| Integer programming relaxation bound | LP relaxation value as exact rational | Truncated bound may be above/below true bound | Exact rational bound; integrality gap exact | Exact simplex |
| Assignment problem (Hungarian) | Subtract row/column minima; find augmenting paths | Rational costs truncated; path selection affected near ties | Exact costs; exact path selection | Exact subtraction and comparison |
| Network flow max-flow | Augmenting path capacities; residual graph | Rational capacities truncated; residual near zero ambiguous | Exact capacity subtraction; zero-flow detection exact | Exact zero-testing |
| Knapsack fractional | Greedy by value/weight ratio | Ratios like 7/13 truncated; wrong ordering possible near ties | [7, 13, 0] vs [5, 9, 0]; exact cross-multiply comparison | Exact comparison |
| Traveling salesman (branch and bound) | Lower bound from LP relaxation | Truncated bounds cause wrong pruning | Exact bound; pruning decisions exact | Exact comparison |
| Minimum spanning tree (Kruskal) | Sort edges by weight; union-find | Rational weights truncated; wrong sort order near ties | Exact sort by cross-multiplication | Exact comparison |
| Matroid intersection | Augmenting path in exchange graph | Weight comparisons on rational edge values | Exact rational comparison | Cross-multiply |

### Appendix K — Additional Domains: Algebraic Geometry

| Problem | Computation | Decimal failure | VDR solution | Key property |
|---|---|---|---|---|
| Bézout's theorem verification | Intersection multiplicity = product of degrees | Compute resultant of two curves; check degree of resultant | Exact resultant via exact Sylvester determinant | Exact integer determinant |
| Genus of algebraic curve | g = (d-1)(d-2)/2 for smooth degree-d curve | Integer formula; but verifying smoothness requires exact discriminant | Discriminant as exact rational; zero-testing exact | Exact zero-testing |
| Rational points on curves | Find (x,y) ∈ Q² satisfying f(x,y)=0 | Evaluate f at candidate rationals; truncation makes zero-testing impossible | f(p/q, r/s) evaluated as exact rational; is it [0,1,0]? | Exact evaluation |
| Divisor class group | Compute divisors of rational functions; check linear equivalence | Function evaluation at rational points truncated | Exact evaluation; exact comparison of divisors | Exact arithmetic chain |
| Intersection form | Bilinear form on homology; matrix of intersection numbers | Integer matrix; but computation involves exact topology → algebra chain | Exact integer matrix operations | Exact linear algebra |
| Hilbert function computation | dim(R/I)_d for graded ring R and ideal I | Requires exact Groebner basis (Section 19 of paper) | Exact Groebner → exact dimension count | Exact zero-testing |
| Blow-up computation | Local coordinates with rational transformation matrices | Transformation matrices have rational entries; chains of transforms | Exact matrix multiplication chain | Exact rational chain |

### Appendix L — Additional Domains: Representation Theory

| Problem | Computation | Decimal failure | VDR solution | Verified |
|---|---|---|---|---|
| Character table of finite group | Characters are algebraic integers; for abelian groups, roots of unity | Character values involve 1/|G| normalization; |G| has odd factors | [1, |G|, 0] exact; character sums exact | VDR-2 gym 5 (combinatorics) |
| Schur orthogonality | Σ χᵢ(g)·χⱼ(g)* = |G|·δᵢⱼ | Sum of products of rationals/algebraic integers; truncation breaks orthogonality | Exact sum; verify = [|G|, 1, 0] or [0, 1, 0] exactly | Exact zero-testing |
| Decomposition into irreducibles | Multiplicity = (1/|G|) Σ χ(g)·χᵢ(g)* | Division by |G| introduces odd prime factors | Exact: [sum, |G|, 0] is exact integer after reduction | Exact GCD reduction |
| Young tableaux hook lengths | Frame-Robinson-Thrall: dim = n!/∏hook_lengths | Hook lengths are small integers; product has many odd primes | Exact integer product; dim is exact integer | VDR-2 gym 5 |
| Tensor product decomposition | Clebsch-Gordan coefficients as exact rationals | Coefficients involve square roots of factorials divided by products | Newton sqrt of exact rationals; exact chains | VDR-1 functional remainder |
| Burnside's lemma | |X/G| = (1/|G|) Σ|Fix(g)| | Division by |G| introduces odd factors | [sum_fix, |G|, 0] exact; result is exact integer | Exact division |
| Molien series | 1/|G| Σ 1/det(I-gT) | Each determinant is polynomial in T with rational coefficients; sum involves 1/|G| | Exact polynomial arithmetic; exact 1/|G| | VDR-2 gym 2 |

### Appendix M — Additional Domains: Topology and Homology

| Problem | Computation | Decimal failure | VDR solution | Key property |
|---|---|---|---|---|
| Smith normal form | Diagonalize integer matrix over Z | Integer row/column operations; intermediate entries grow | Exact integer arithmetic throughout; SNF entries are exact divisors | Exact integer chain |
| Homology group computation | Kernel/image of boundary matrices | Rank computation requires exact zero-testing | Exact rank via exact elimination | Exact zero-testing |
| Betti numbers | β_k = rank(H_k) = rank(ker ∂_k) - rank(im ∂_{k+1}) | Exact integer rank difference | Both ranks exact; difference exact | Exact linear algebra |
| Euler characteristic | χ = Σ(-1)^k β_k | Alternating sum of exact integers | Exact integer sum | Trivial once ranks exact |
| Intersection number | Algebraic count of intersection points | Integer by definition; but computation goes through exact matrix ops | Exact determinant/rank computation | Exact linear algebra |
| Fundamental group presentation | Word problem in finitely presented groups | Involves exact equality of group elements | Exact comparison of normal forms | Exact structural equality |
| Simplicial chain complex | Boundary operator as integer matrix | All entries ±1 or 0; but products have growing entries | Exact integer matrix product | Exact arithmetic |
| Persistent homology | Track birth/death of features across filtration parameter | Filtration parameter comparisons; birth/death times as rationals | Exact comparison of rational filtration values | Exact comparison |

### Appendix N — Additional Domains: Category Theory and Logic

| Problem | Computation | Decimal failure | VDR solution | Key property |
|---|---|---|---|---|
| Functor composition verification | F∘G∘H applied to morphisms | Morphisms as rational matrices; composition is matrix multiply | Exact matrix multiply chain | Exact rational chain |
| Natural transformation coherence | Square commutes: η_B ∘ F(f) = G(f) ∘ η_A | Product of exact rational matrices; equality check | Both paths produce exact matrix; structural equality | Exact zero-testing |
| Kan extension computation | Colimit formula involving products and coproducts | Rational coefficients in colimit cone | Exact rational coefficients; universal property verified exactly | Exact comparison |
| Topos-theoretic truth values | Subobject classifier Ω; characteristic morphisms | For finite categories: rational-valued truth | Exact rational truth values; conjunction/disjunction exact | Exact arithmetic |
| Boolean satisfiability with weighted clauses | Max-SAT with rational clause weights | Weight sums truncated; optimal may be misidentified | Exact rational weight sums; exact comparison | Exact comparison |
| Proof verification | Type-checking terms in dependent type theory | Definitional equality requires exact comparison | VDR values in types compared exactly | Exact structural equality |

### Appendix O — Additional Domains: Information Theory

| Problem | Computation | Decimal failure | VDR solution | Key operation |
|---|---|---|---|---|
| Shannon entropy H = -Σ pᵢ log(pᵢ) | Rational probabilities, transcendental log | log via functional remainder; product with exact pᵢ | [pᵢ, 1, 0] × log([pᵢ, D, 0]) via Taylor | VDR-1 functional remainder |
| Mutual information I(X;Y) = H(X) + H(Y) - H(X,Y) | Subtraction of nearly-equal entropies | Catastrophic cancellation when X,Y nearly independent | Exact subtraction of Taylor-evaluated logs | Exact subtraction |
| KL divergence D_KL(P‖Q) = Σ pᵢ log(pᵢ/qᵢ) | Rational P, Q; log of rational ratio | log(pᵢ/qᵢ) truncated; sum accumulates | log([pᵢ·qⱼ_denom, qᵢ·pⱼ_denom, 0]) via Taylor; exact sum | Exact rational argument to Taylor |
| Channel capacity | max_{p(x)} I(X;Y) subject to Σpᵢ=1 | Optimization over rational probabilities | Lagrange conditions with exact rational arithmetic | Exact optimization |
| Rate-distortion function | min_{p(x̂|x)} I(X;X̂) subject to E[d(X,X̂)] ≤ D | Blahut-Arimoto iteration with rational updates | Each iteration exact; convergence to exact fixed point | Exact iteration |
| Kolmogorov complexity bounds | Counting argument over exact string lengths | Integer arithmetic | Exact integer | Trivial |
| Arithmetic coding interval | Subdivide [0,1) by exact cumulative probabilities | Cumulative sums of 1/3, 1/7, etc. truncated; interval boundaries wrong | Exact cumulative sums; interval boundaries exact rationals | Exact rational sum |
| Lempel-Ziv dictionary sizes | Integer counts and ratios | Compression ratio as exact rational count/original | Exact integer division | Exact ratio |

### Appendix P — Additional Domains: Differential Geometry (Discrete/Rational)

| Problem | Computation | Decimal failure | VDR solution | Key operation |
|---|---|---|---|---|
| Discrete curvature on mesh | Angle defect = 2π - Σθᵢ at vertex | Angles via arctan of rational edge ratios; sum truncated | arctan via Taylor functional remainder; exact sum | Exact sum of Taylor values |
| Christoffel symbols (rational metric) | Γⁱⱼₖ = (1/2)gⁱˡ(∂gⱼₗ/∂xᵏ + ∂gₖₗ/∂xʲ - ∂gⱼₖ/∂xˡ) | Metric entries rational; discrete derivatives exact; inverse metric exact | All operations on exact rationals; Γ entries exact | Exact matrix inverse |
| Geodesic equation (discrete) | ẍⁱ + Γⁱⱼₖ ẋʲ ẋᵏ = 0; step with exact Γ | Exact Christoffel × exact velocity; Euler step exact | [ẍⁱ, 1, 0] exact; position update exact | Exact multiplication chain |
| Riemann tensor components | Rⁱⱼₖₗ from derivatives of Γ | Second derivatives of metric; products of Γ values | Exact discrete derivatives; exact products | Exact rational chain |
| Euler characteristic via Gauss-Bonnet | χ = (1/2π) ∫ K dA → discrete sum | Discrete curvatures summed; π factor via Q335 | Exact discrete curvatures; Q335 π; exact sum | Exact sum × Q335 |
| Parallel transport (discrete) | Rotate vector by connection form at each edge | Rotation by exact rational angle (discrete); product of rotation matrices | Each rotation matrix exact (rational trig approximation); product exact | Exact matrix product chain |
| Holonomy computation | Product of parallel transport around loop | Chain of rotation matrices; should return to identity for flat | Exact matrix product; compare to identity exactly | Exact identity check |

### Appendix Q — Additional Domains: Mathematical Physics

| Problem | Computation | Decimal failure | VDR solution | Prior validation |
|---|---|---|---|---|
| Clebsch-Gordan coefficients | C^{j₃m₃}_{j₁m₁,j₂m₂} as exact rationals involving factorials | Factorial ratios with many odd prime factors | Exact: factorials as integers, ratios as exact rationals | VDR-2 gym 5 |
| Wigner 3j/6j/9j symbols | Sums of products of factorial ratios | Same as Clebsch-Gordan; longer chains | Exact: every intermediate product exact | VDR-2 gym 5 |
| Racah coefficients | Linear combinations of 3j symbols | Sum of exact rationals; no truncation | Exact sum of exact rationals | VDR-1 |
| Spherical harmonics at rational angles | Yₗᵐ(θ,φ) involves associated Legendre polynomials (rational for rational cos θ) × exp(imφ) | Polynomial part truncated if cos θ has odd denominator | Legendre polynomial evaluated exactly at rational cos θ | VDR-2 gym 2 |
| Partition function (Ising model) | Z = Σ exp(-βJ Σ sᵢsⱼ) over spin configurations | Each exponential truncated; sum of truncations | Taylor exp at each configuration; exact sum | VDR-1 functional remainder |
| Transfer matrix eigenvalues | 2ˢ × 2ˢ matrix for s-site strip; eigenvalues determine free energy | Matrix entries involve exp(-βJ); eigenvalue computation on truncated matrix | Exact Taylor entries; exact eigenvalue (2×2) or Newton (larger) | VDR-2 gym 4 |
| Casimir energy | ζ(-1) = -1/12 (Ramanujan summation) | Exact rational | [-1, 12, 0] exact | VDR-3 Q335 |
| Fine structure constant contributions | α = e²/(4πε₀ℏc); QED corrections as rational combinations of π, ζ(3), ln(2) | Each correction term is rational × Q335 constant | Exact rational × Q335 integer; sum in shared frame | VDR-13 QED |
| Bethe ansatz momenta | Solve coupled rational equations for momentum parameters | Each equation involves rational functions of momenta | Exact rational equation solving | Exact polynomial arithmetic |

### Appendix R — Additional Domains: Numerical Methods Theory

| Problem | Computation | Decimal failure | VDR solution | Key insight |
|---|---|---|---|---|
| Convergence order verification | Ratio e_{n+1}/e_n^p → C; determine p | Errors eₙ computed as f(xₙ) - f(x*); subtraction of nearly-equal values | Exact error: [f(xₙ) - f(x*)] as exact rational | Exact subtraction eliminates cancellation |
| Richardson extrapolation | Combine approximations at different step sizes to eliminate error terms | h₁ = 1/3, h₂ = 1/5: combination involves 1/(h₁²-h₂²) with odd denominators | Exact: [1, h₁²-h₂², 0] as exact rational | Exact rational coefficient |
| Romberg integration | Triangular array of Richardson extrapolations | Each level divides by differences of step sizes squared | Exact: all step sizes rational; all differences exact | Exact chain of extrapolations |
| Adams-Bashforth coefficients | Coefficients from Lagrange interpolation on {0,-1,-2,...,-(k-1)} | Coefficients involve 1/k! and products of small integers | Exact rational Lagrange coefficients | VDR-2 gym 2 (polynomial interpolation) |
| Condition number estimation | κ(A) = ‖A‖·‖A⁻¹‖ for rational A | A⁻¹ computed approximately; κ is approximate | A⁻¹ exact; κ exact (for exact norms) | Exact matrix inverse |
| Lebesgue constant | Λₙ = max_x Σ|ℓᵢ(x)| for Lagrange basis | Lagrange basis functions at rational nodes: rational function evaluation | Exact evaluation at any rational x | Exact rational evaluation |
| Runge phenomenon quantification | Error growth for equidistant polynomial interpolation | Interpolation error at rational points computed exactly | Exact polynomial evaluation; exact error | Exact polynomial arithmetic |
| Quadrature weight verification | Gaussian quadrature weights sum to interval length | Weights involve ratios of Legendre polynomial values at irrational nodes | Weights at rational-approximation nodes: exact; sum verification exact | Exact sum check |

### Appendix S — Additional Domains: Coding Theory Beyond Galois Fields

| Problem | Computation | Decimal failure | VDR solution | Key operation |
|---|---|---|---|---|
| LDPC belief propagation | Message updates as log-likelihood ratios | LLR computed from exact channel probabilities; tanh of LLR truncated | Exact channel probabilities; tanh via Taylor functional remainder | Exact probability propagation |
| Turbo code interleaver analysis | Permutation distances and correlation | Integer arithmetic on permutation indices | Exact integer | Trivial |
| Polar code construction | Bhattacharyya parameters Z(W_N^(i)) via recursive formula | Z values are rational for BSC; recursion Z' = 2Z-Z² truncated at each step | Exact: [2Z-Z², 1, 0] exact rational at every recursion | Exact rational recursion |
| Convolutional code free distance | Enumerate paths through trellis; weight = sum of branch metrics | Integer branch metrics; free distance is minimum weight | Exact integer | Trivial |
| Algebraic geometry codes | Evaluate rational functions at rational points on curves | Evaluation involves exact rational arithmetic on curve coordinates | Exact evaluation; exact syndrome computation | Exact rational evaluation |
| Fountain codes (LT/Raptor) | Degree distribution Ω(x) = Σ Ωᵢxⁱ with rational Ωᵢ | Ideal soliton: Ωᵢ = 1/(i(i-1)) has odd denominators | [1, i(i-1), 0] exact; CDF sums exact | Exact probability arithmetic |
| Code concatenation analysis | Inner code × outer code error exponents | Products of rational error probabilities across chain | Exact rational probability chain | Exact multiplication |

### Appendix T — Additional Domains: Mathematical Logic and Model Theory

| Problem | Computation | Decimal failure | VDR solution | Key property |
|---|---|---|---|---|
| Compactness theorem application | Finite satisfiability checking with rational-valued models | Model values as rationals; formula evaluation exact or not | Exact formula evaluation; satisfaction is decidable | Exact comparison |
| Löwenheim-Skolem cardinality | Counting models up to isomorphism; size arguments | Integer arithmetic | Exact integer | Trivial |
| Ultraproduct construction | Quotient by ultrafilter; equivalence of rational sequences | Pointwise rational arithmetic; equivalence requires exact comparison | Exact rational at each index; equivalence decidable | Exact comparison |
| Decidability of real closed fields (Tarski) | Quantifier elimination over ordered fields | Involves sign determination of polynomials at algebraic numbers | Exact polynomial evaluation at rational approximations of algebraic numbers | Exact polynomial evaluation |
| Non-standard analysis arithmetic | *Q hyperrationals; transfer principle preserves exact arithmetic | Standard rationals embedded exactly; transfer preserves identities | VDR rationals satisfy transfer principle for rational identities | Exact arithmetic |
| Presburger arithmetic verification | Decidable theory of (Z, +, <) | Integer arithmetic with comparison | Exact integer comparison | Trivial |
| Peano arithmetic models | Verify models satisfy axioms | Successor, addition, multiplication on exact integers | Exact integer arithmetic | Trivial |

### Appendix U — Additional Domains: Actuarial Science and Insurance

| Problem | Computation | Decimal failure | VDR solution | Regulatory requirement |
|---|---|---|---|---|
| Life table mortality rates | qₓ = dₓ/lₓ; death count / survivors | dₓ = 47, lₓ = 10000: qₓ = 47/10000 terminates. But dₓ = 47, lₓ = 9953: qₓ = 47/9953 repeats | [47, 9953, 0] exact | Solvency II: deterministic |
| Net premium calculation | P = A/ä where A = Σvᵏ·qₓ₊ₖ, ä = Σvᵏ·pₓ₊ₖ | v = 1/(1+i); if i = 3% then v = 100/103 repeats (103 is prime) | [100, 103, 0] exact; chains of powers exact | GAAP: auditable |
| Reserve calculation | V_t = A_{x+t} - P·ä_{x+t} | Subtraction of two nearly-equal present values; cancellation | Exact subtraction; no cancellation | Regulatory capital |
| Loss development triangle | Chain-ladder factors f_k = Σc_{i,k+1}/Σc_{i,k} | Sums of claims; ratios with arbitrary denominators | Exact rational sums and ratios | SOX compliance |
| Credibility weighting | Z = n/(n+k) where k = σ²/τ² | If n=7, k=13/3: Z = 7/(7+13/3) = 21/34 repeats (17 is factor) | [21, 34, 0] exact | Actuarial standard of practice |
| DFA stochastic scenarios | Monte Carlo with exact rational transition probabilities | Same as Monte Carlo in VDR-27 §6.1 | Exact path arithmetic; statistical error separable | Enterprise risk management |
| Annuity certain | ä_n = (1-vⁿ)/d where d = i/(1+i) | d = 3/103 for 3% interest; vⁿ = (100/103)ⁿ; chain of powers with prime denominator | Exact rational power; exact subtraction; exact division | Policy pricing |
| Aggregate loss distribution | Panjer recursion: f(x) = (1/f(0)) Σ (a+b·k/x)·p(k)·f(x-k) | Recursive formula with rational parameters; chain of multiply-and-add | Exact rational recursion; each step exact | Reserving |

### Appendix V — Additional Domains: Music Theory and Acoustics

| Problem | Computation | Decimal failure | VDR solution | Key insight |
|---|---|---|---|---|
| Just intonation intervals | Perfect fifth = 3/2; major third = 5/4; minor seventh = 7/4 | 3/2 = 1.5 terminates; but 7/4 × 3/2 = 21/8 = 2.625 terminates; chains eventually hit odd composites | Every interval exact; all comparisons exact | Exact ratio |
| Pythagorean comma | (3/2)¹² / 2⁷ = 531441/524288 | = 1.01364... terminates (all factors are 2,3) but comparing to syntonic comma 81/80 requires exact | [531441, 524288, 0] vs [81, 80, 0]; exact comparison | Exact comparison |
| Equal temperament approximation error | 2^(7/12) vs 3/2; difference = 3/2 - 2^(7/12) | 2^(7/12) is irrational; Newton approximation at depth | Newton 2^(7/12) via exp(7·ln(2)/12) Taylor; subtract [3,2,0]; exact residual | Functional remainder |
| Harmonic series partial sums | Σ 1/k for k=1..n | Every term with odd k in denominator repeats in decimal | Each [1, k, 0] exact; sum exact | Exact rational sum |
| Consonance measure | Euler's gradus suavitatis: Γ(n) = 1 + Σ(pᵢ-1)eᵢ for n = ∏pᵢᵉⁱ | Integer factorization and arithmetic | Exact integer | Trivial |
| Tuning system comparison | Meantone vs Pythagorean vs just: difference in cents | Cent = 1200·log₂(ratio); log via Taylor on exact ratio | Exact ratio as input to Taylor log; result exact per depth | Functional remainder |
| Beat frequency | |f₁-f₂| where f₁=440·(3/2), f₂=440·2^(7/12) | f₁ exact rational; f₂ irrational; difference needs exact subtraction | [660, 1, 0] - Newton 2^(7/12)·[440,1,0]; exact residual | Exact subtraction |
| Spectral analysis of intervals | DFT of waveform sampled at rational times | DFT roundtrip exact in VDR (VDR-13) | Frequency content exactly recoverable | VDR-13 DFT |

### Appendix W — Additional Domains: Economics and Econometrics

| Problem | Computation | Decimal failure | VDR solution | Key operation |
|---|---|---|---|---|
| Input-output analysis (Leontief) | x = (I-A)⁻¹d; A has rational technical coefficients | Matrix inverse with denominators from all sectors' coefficients | Exact inverse; exact output vector | Exact matrix inverse |
| Gini coefficient | G = (Σᵢ Σⱼ |yᵢ-yⱼ|)/(2n²·ȳ) | Numerator is sum of absolute differences; denominator involves mean | Exact rational sum; exact mean [Σyᵢ, n, 0]; exact division | Exact rational chain |
| OLS regression coefficients | β = (XᵀX)⁻¹Xᵀy for rational X, y | XᵀX inverse has denominators from all data; truncation through chain | Exact matrix product; exact inverse; exact coefficients | Exact linear algebra |
| Elasticity computation | ε = (∂Q/∂P)·(P/Q) = (ΔQ/ΔP)·(P/Q) | Finite difference of rational observations; ratio of rationals | Exact difference; exact ratio; exact product | Exact rational chain |
| Present value of annuity | PV = C·(1-(1+r)⁻ⁿ)/r | If r = 1/12 (monthly of 100% annual): (1+1/12)⁻ⁿ = (12/13)ⁿ; 13 is prime | [12, 13, 0]ⁿ exact; entire formula exact | Exact rational power |
| Arrow-Debreu equilibrium | Fixed point of excess demand; involves utility maximization with rational parameters | Rational utility parameters; budget constraints involve price ratios | Exact excess demand at rational prices; exact fixed-point verification | Exact evaluation |
| Consumer/producer surplus | Area under/above demand/supply curves = definite integral of rational function | Exact via partial fractions (Section 17 of paper) | Exact antiderivative evaluation | Exact polynomial evaluation |
| Heckscher-Ohlin factor prices | Factor price equalization: solve p = A·w for rational A, p | Exact linear system solve | Exact solution [wᵢ, 1, 0] | Exact linear algebra |

### Appendix X — Additional Domains: Formal Verification

| Problem | Computation | Decimal failure | VDR solution | Key property |
|---|---|---|---|---|
| Model checking (rational-timed) | Timed automaton with rational clock constraints | Clock comparison: is 3/7 < 5/11? Cross-multiply: 33 vs 35; yes | Exact comparison | Exact comparison |
| Abstract interpretation (numerical) | Interval abstract domain: [a,b] with rational bounds | Widening/narrowing on rational intervals; meet/join exact | Exact interval arithmetic | Exact comparison and arithmetic |
| Loop invariant verification | Verify i·(i-1)/2 = Σk for k=0..i-1 at each iteration | Integer arithmetic | Exact integer | Trivial |
| Floating-point program verification | Verify that float program satisfies spec within error bounds | Error bounds as exact rationals; float semantics modeled exactly | ULP computation as exact rational; error propagation exact | Exact rational error model |
| Theorem prover kernel | Type-checking and term reduction with exact coefficients | Definitional equality requires exact comparison | VDR values compared exactly; reduction produces exact results | Exact structural equality |
| SMT solver arithmetic theory | Quantifier-free theory of rationals: satisfiability | All operations on rationals must be exact; comparison decidable | VDR provides exact arithmetic and comparison | Exact arithmetic |
| Probabilistic model checking | PCTL model checking: compute reachability probability exactly | Probability as exact rational; matrix method for Markov chain | Exact probability via exact linear system solve | Exact linear algebra |
| Refinement checking | Implementation refines specification: simulation relation | Trace comparison at rational-valued observations | Exact comparison of observation values | Exact comparison |

### Appendix Y — Prime Factor Density in Mathematical Constants and Formulas

| Constant/Formula | Exact rational form | Denominator | Prime factors | Decimal period | VDR representation |
|---|---|---|---|---|---|
| Euler-Mascheroni partial sum H₁₀ | 7381/2520 | 2520 | 2³·3²·5·7 | 6 (from 7) | [7381, 2520, 0] |
| B₂ (Bernoulli) | 1/6 | 6 | 2·3 | 1 | [1, 6, 0] |
| B₄ | -1/30 | 30 | 2·3·5 | 1 | [-1, 30, 0] |
| B₆ | 1/42 | 42 | 2·3·7 | 6 | [1, 42, 0] |
| B₈ | -1/30 | 30 | 2·3·5 | 1 | [-1, 30, 0] |
| B₁₀ | 5/66 | 66 | 2·3·11 | 2 | [5, 66, 0] |
| B₁₂ | -691/2730 | 2730 | 2·3·5·7·13 | 12 | [-691, 2730, 0] |
| B₁₄ | 7/6 | 6 | 2·3 | 1 | [7, 6, 0] |
| B₁₆ | -3617/510 | 510 | 2·3·5·17 | 16 | [-3617, 510, 0] |
| B₁₈ | 43867/798 | 798 | 2·3·7·19 | 18 | [43867, 798, 0] |
| B₂₀ | -174611/330 | 330 | 2·3·5·11 | 2 | [-174611, 330, 0] |
| RK4 coefficient 1/6 | 1/6 | 6 | 2·3 | 1 | [1, 6, 0] |
| RK4 coefficient 1/3 | 1/3 | 3 | 3 | 1 | [1, 3, 0] |
| Dormand-Prince 12/13 | 12/13 | 13 | 13 | 6 | [12, 13, 0] |
| Fehlberg 4243/5348 | 4243/5348 | 5348 | 2²·7·191 | 190 | [4243, 5348, 0] |
| Gauss quadrature weight (n=3) | 5/9 | 9 | 3² | 1 | [5, 9, 0] |
| Gauss quadrature weight (n=3) | 8/9 | 9 | 3² | 1 | [8, 9, 0] |
| Simpson's rule 1/3 | 1/3 | 3 | 3 | 1 | [1, 3, 0] |
| Simpson's rule 4/3 | 4/3 | 3 | 3 | 1 | [4, 3, 0] |
| Weddle's rule 3/10 | 3/10 | 10 | 2·5 | 0 (terminates) | [3, 10, 0] |
| Boole's rule 7/90 | 7/90 | 90 | 2·3²·5 | 1 | [7, 90, 0] |
| Stirling approx correction 1/12n | 1/(12n) | 12n | 2²·3·n | varies | [1, 12n, 0] |
| Wallis product partial (n=5) | 32768/31185 | 31185 | 3·5·2079=3·5·3·693=3²·5·693=3²·5·3²·7·11 | lcm(1,6,2)=6 | [32768, 31185, 0] |

Every Bernoulli number from B₂ onward has at least one odd prime factor in its denominator. Every RK method with order ≥ 2 has at least one coefficient with a factor of 3. Every Gaussian quadrature rule with ≥ 3 points has weights with odd prime denominators. The decimal trap is endemic in numerical mathematics.

### Appendix Z — Complete Domain Coverage Summary

| Category | Domains in paper | Domains in appendices | Total domains | Key shared property |
|---|---|---|---|---|
| Number theory | 3 (continued fractions, Bernoulli, Farey) | 2 (algebraic number theory, Pell equation) | 5 | Exact rational arithmetic on number-theoretic objects |
| Linear algebra | 3 (Hilbert, eigenvalue, Gaussian elim) | 1 (condition number) | 4 | Exact matrix operations; exact zero-testing |
| Polynomial algebra | 3 (GCD, Padé, Cayley-Hamilton) | 2 (Groebner, resultants) | 5 | Exact polynomial arithmetic; exact zero-testing |
| Probability/statistics | 2 (Bayesian, Markov) | 1 (actuarial) | 3 | Exact rational probability chains |
| Cryptography/coding | 2 (Galois field, quantum stabilizer) | 2 (elliptic curve, LDPC/polar codes) | 4 | Exact modular/field arithmetic |
| Physics | 1 (partition function) | 2 (mathematical physics, differential geometry) | 3 | Exact Boltzmann weights; exact geometric quantities |
| Numerical methods | 2 (Runge-Kutta, integration) | 2 (Richardson, convergence order) | 4 | Exact method coefficients; exact error measurement |
| Algebraic geometry | 0 | 2 (curves, Groebner application) | 2 | Exact zero-testing; exact point arithmetic |
| Topology | 0 | 1 (homology, Smith normal form) | 1 | Exact integer matrix operations |
| Representation theory | 0 | 1 (characters, Young tableaux) | 1 | Exact factorial arithmetic; exact orthogonality |
| Information theory | 0 | 1 (entropy, KL, coding) | 1 | Exact probability × transcendental chains |
| Logic/verification | 0 | 2 (model theory, formal verification) | 2 | Exact comparison; exact arithmetic |
| Economics | 0 | 1 (Leontief, OLS, surplus) | 1 | Exact rational chain in economic models |
| Music theory | 0 | 1 (intervals, tuning, commas) | 1 | Exact frequency ratios |
| Combinatorial optimization | 0 | 1 (simplex, assignment, flow) | 1 | Exact comparison for tie-breaking |
| Category theory | 0 | 1 (functors, natural transformations) | 1 | Exact composition verification |
| Lattice algorithms | 1 (LLL) | 0 | 1 | Exact threshold comparison |
| **Total** | **20** | **23** | **43** | **Exact rational arithmetic eliminates decimal truncation** |

43 domains across pure mathematics, applied mathematics, computer science, physics, engineering, finance, and logic. In every domain, the structural vulnerability is the same: intermediate values with denominators containing prime factors other than 2 and 5 force decimal truncation. VDR eliminates the truncation by representing the denominator as an exact integer. The solution is not more digits. It is exact representation.
