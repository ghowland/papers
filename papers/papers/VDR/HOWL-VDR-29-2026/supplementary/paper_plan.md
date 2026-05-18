### The Decimal Trap: Why 10 = 2×5 Corrupts Everything

The fundamental problem: decimal arithmetic (including mpmath at arbitrary precision) represents numbers in base 10. The only fractions with terminating decimal representations are those whose denominators factor into only 2s and 5s. Everything else — 1/3, 1/7, 1/11, 1/13, every fraction with a prime factor other than 2 or 5 in the denominator — becomes an infinite repeating decimal that must be truncated.

mpmath handles this by carrying hundreds or thousands of digits. But truncation is truncation regardless of how many digits you carry. Multiply two 1000-digit truncated values and the result needs 2000 digits to be exact — but mpmath truncates back to 1000. Chain 50 operations and you've lost digits from the bottom of every intermediate result. The loss is small per operation but it compounds, and critically, it's invisible — mpmath doesn't track what it threw away.

VDR represents 1/3 as [1, 3, 0]. Exact. 1/7 as [1, 7, 0]. Exact. Multiply them: [1, 21, 0]. Exact. Chain 50 operations: exact. The denominator grows but nothing is discarded. When precision must be bounded (Q335), the remainder slot carries exactly what was not absorbed — visible, queryable, exact.

Here are the domains where this distinction between "many digits" and "exact" produces materially different results.

---

### 1. Continued Fraction Arithmetic

**The problem:** The Gauss continued fraction for ratios of hypergeometric functions produces convergents that are ratios of integers with no factors of 2 or 5. Computing ₂F₁(1/2, 1/2; 1; k²) for the complete elliptic integral K(k) at rational k produces convergents like 7/22, 103/323, 1507/4726. Every one of these is an infinite repeating decimal.

**mpmath:** Truncates each convergent to N digits. Multiplying convergent n by convergent n+1 to compute the next produces a result truncated to N digits. After 200 convergents, the accumulated truncation has consumed digits from the bottom — the last few digits of the result are wrong, and you don't know how many.

**VDR:** Each convergent is [p, q, 0] where p and q are exact integers. The recurrence pₙ = aₙpₙ₋₁ + pₙ₋₂ is exact integer arithmetic. After 200 convergents, every digit is correct. The Gauss-Kuzmin distribution statistics (VDR-2 gym 3) verified coefficient 1 appears at ~41% (predicted 41.5%) — this requires exact counting over exact convergents.

**Where it matters:** Number theory, Diophantine approximation, computing irrationality measures. The quality of a rational approximation p/q to an irrational α is measured by |α - p/q| — a subtraction of two nearly-equal numbers. In decimal, this is catastrophic cancellation. In VDR, it's exact: (αₙ·q - p) / (D·q) where αₙ is the Newton iterate, all exact.

---

### 2. Bernoulli Numbers and Zeta Values

**The problem:** Bernoulli numbers B_n grow factorially and have denominators governed by the von Staudt-Clausen theorem: the denominator of B_{2n} is the product of all primes p such that (p-1)|2n. B₁₂ = -691/2730. The denominator 2730 = 2·3·5·7·13. In decimal: -691/2730 = -0.253113553113553113... repeating with period 12.

**mpmath:** Represents B₁₂ as -0.25311355311355311... truncated to N digits. Multiply B₁₂ by (2π)¹² / 12! to compute ζ(12) and the truncation of B₁₂ contaminates the result. For B₃₀ the denominator is 14322 = 2·3·2387 and the numerator is 8615841276005. The fraction is exact; its decimal representation repeats with a period determined by 2387 (a prime), potentially thousands of digits.

**VDR:** B₁₂ = [−691, 2730, 0]. Multiply by any rational: exact. The product B₁₂ · (2π)¹²/12! uses Q335 for π¹² and exact rational for the Bernoulli factor. No digit is lost. The zeta value relationship ζ(2n) = (-1)^{n+1} · B_{2n} · (2π)^{2n} / (2·(2n)!) is computed with exact rational Bernoulli numbers times Q335 powers of π. The only approximation is the Q335 representation of π, which has a known, exact, 100-digit floor.

**Where it matters:** Analytic number theory, computing special function values, perturbative quantum field theory (Bernoulli numbers appear in Euler-Maclaurin summation of Feynman integrals).

---

### 3. Hilbert Matrix Computations

**The problem:** The Hilbert matrix H_{ij} = 1/(i+j-1) is the canonical ill-conditioned matrix. Every entry is a unit fraction: 1/1, 1/2, 1/3, 1/4, ... In decimal, 1/3 = 0.333..., 1/7 = 0.142857142857..., 1/11 = 0.090909... All infinite repeating decimals, all truncated.

**mpmath at 50 digits:** H₅ inverse residual ~10⁻⁴⁰. Looks exact but isn't — there are digits wrong at the bottom. H₁₀ inverse residual ~10⁻²⁰. H₁₅: mpmath needs 100+ digits to get a meaningful answer, and the result still has unknown digits wrong at the bottom. H₂₀: mpmath at 200 digits produces a result where you cannot verify which digits are correct without going to 400 digits, and then you can't verify those without 800.

**VDR:** H₅ inverse residual = 0. Not approximately zero. Zero. H₁₀ residual = 0. H₂₀ residual = 0. H₃₀ residual = 0. Every entry of H⁻¹ is an exact integer (a known result: Hilbert inverse entries are always integers). VDR computes them as exact integers. The determinant of H₄ is exactly 1/6048000. VDR returns [1, 6048000, 0]. mpmath returns 0.00000016534391534391534... truncated, and you have to trust that the truncation didn't corrupt the last digits.

**Where it matters:** Numerical analysis benchmarking, condition number studies, any application where the matrix entries are exact rationals (stiffness matrices in structural engineering, Gram matrices in approximation theory, kernel matrices in machine learning with rational kernel parameters).

---

### 4. Exact Eigenvalue Problems (2×2 and Rational Characteristic Polynomials)

**The problem:** The eigenvalues of a 2×2 rational matrix [[a,b],[c,d]] are (a+d)/2 ± √((a-d)²/4 + bc). The discriminant (a-d)²/4 + bc is an exact rational. If it's a perfect square rational, the eigenvalues are exact rationals. If not, they involve √ of a rational — representable as a VDR functional remainder.

**mpmath:** Computes the discriminant as a decimal, takes a decimal square root, adds/subtracts decimal halves. Each step truncates. The eigenvalues are truncated decimals. For the matrix [[1/3, 1/7],[1/11, 1/13]], the discriminant is (1/3 - 1/13)²/4 + 1/(7·11) = (10/39)²/4 + 1/77 = 100/6084 + 1/77 = 7700/468468 + 6084/468468 = 13784/468468 = 3446/117117. In decimal: 0.029422... repeating. mpmath takes √0.029422... and truncates.

**VDR:** Discriminant = [3446, 117117, 0]. Exact. √discriminant via Newton: exact rational at each depth, converging quadratically. Eigenvalues are (trace/2) ± √discriminant, each an exact rational expression. The eigenvector components are ratios of exact rationals. Orthogonality of eigenvectors verified by exact dot product = 0, not dot product ≈ 10⁻¹⁵.

**Where it matters:** Quantum mechanics (2-level systems are 2×2 eigenvalue problems), stability analysis (eigenvalue sign determines stability), vibration analysis (natural frequencies are eigenvalues of mass-stiffness system), Markov chain analysis (steady state is the eigenvector for eigenvalue 1 — VDR-2 gym 11 computed exact steady state [2/3, 1/3]).

---

### 5. Gaussian Elimination Pivot Ratios

**The problem:** Gaussian elimination produces pivot elements that are ratios of determinants of submatrices. For rational input, every pivot is rational. But the denominators grow combinatorially. For an n×n rational matrix, pivot denominators can have O(n) prime factors, most of which are not 2 or 5.

**mpmath:** Each elimination step divides by the pivot. If the pivot is 7/13, dividing by it means multiplying by 13/7. In decimal, 13/7 = 1.857142857142... repeating. Truncation. Multiply the truncated result by another entry whose decimal was also truncated. The error compounds through O(n²) operations. For n=20, that's ~400 operations on truncated decimals.

**VDR:** 13/7 = [13, 7, 0]. Division by [7, 13, 0] produces [13, 7, 0] · [D, V, 0]. Exact. 400 operations: exact. The final result has large denominators but zero truncation error. VDR-13 documented: H₃₀ inverse via Gaussian elimination has pivot denominators up to ~185 digits. mpmath at 200 digits would lose 15 digits of precision through the elimination. VDR loses zero.

**Where it matters:** Every application of linear algebra on rational data. Structural engineering (stiffness matrices with rational entries), circuit analysis (impedances as rational functions of component values), least-squares fitting with rational data points, exact rank computation (float rank is always full; VDR rank is exact).

---

### 6. Modular Arithmetic and Chinese Remainder Theorem

**The problem:** CRT reconstructs an integer from its residues modulo several coprime moduli. The reconstruction formula involves modular inverses: x = Σ aᵢ · Mᵢ · (Mᵢ⁻¹ mod mᵢ) where Mᵢ = M/mᵢ and M = ∏mᵢ. The modular inverse Mᵢ⁻¹ mod mᵢ is computed via extended GCD. The intermediate products Mᵢ · (Mᵢ⁻¹ mod mᵢ) are exact integers that can be astronomically large.

**mpmath:** Doesn't apply — mpmath is floating point, not modular arithmetic. But Python integers handle this exactly, as do VDR integers [n, 1, 0].

**Where VDR adds value beyond raw integers:** When CRT is used to reconstruct a rational number from its images under modular homomorphisms. Rational reconstruction from modular images: given x mod p for several primes p, reconstruct x = a/b. The reconstruction involves extended GCD and rational number recovery. VDR represents the reconstructed a/b as [a, b, 0] exactly, and subsequent arithmetic on the reconstructed value is exact. In decimal, the reconstructed rational is truncated immediately.

**Where it matters:** Computer algebra systems use modular methods to compute GCDs of polynomials, resultants, and determinants. The CRT reconstruction step produces exact rationals. Performing further computation on these rationals in decimal truncates them. VDR preserves them.

---

### 7. Probability Chains and Bayesian Updates

**The problem:** Bayes' theorem: P(A|B) = P(B|A)·P(A) / P(B). With rational priors and likelihoods, the posterior is rational. Sequential Bayesian updating applies Bayes N times, each step's posterior becoming the next step's prior. The denominators grow because P(B) = Σ P(B|Aᵢ)·P(Aᵢ) involves sums of products of rationals, producing denominators with prime factors from every term.

**mpmath:** P(disease) = 1/10000 = 0.0001. P(positive|disease) = 99/100 = 0.99. P(positive|healthy) = 1/100 = 0.01. P(disease|positive) = (0.99 · 0.0001) / (0.99·0.0001 + 0.01·0.9999) = 0.0000099/0.010098. In decimal: 0.00098029... Each subsequent update multiplies these truncated decimals. After 10 updates with different evidence, the accumulated truncation means the posterior probability has unknown digits at the bottom.

**VDR:** P(disease) = [1, 10000, 0]. P(positive|disease) = [99, 100, 0]. Posterior = [99, 1009800, 0] after normalization. Exact. After 10 updates: exact. After 100 updates: exact. The denominators are large but every digit is correct. VDR-2 gym 11 verified: binomial PMF with n=10, p=1/3 sums to exactly 1. Sequential Bayesian posterior computed as exact 6/7. mpmath would give 0.857142857142... truncated.

**Where it matters:** Medical diagnostics (sequential test results updating disease probability), spam filtering (sequential word observations updating spam probability), sensor fusion (sequential sensor readings updating state estimate), forensic statistics (sequential evidence updating guilt probability — getting this wrong has legal consequences).

---

### 8. Markov Chain Steady States and Mixing Times

**The problem:** The steady state of a Markov chain is the eigenvector of the transition matrix for eigenvalue 1. For a k-state chain with rational transition probabilities, the steady state components are rational numbers whose denominators involve all the prime factors from the transition matrix.

**mpmath:** Compute Aⁿ for large n and read off any row (power method). Each matrix multiplication truncates every entry's decimal. After n=100 multiplications: the last several digits of every entry are wrong. Or compute the eigenvector by solving (A-I)x = 0 — Gaussian elimination on a matrix whose entries are truncated decimals.

**VDR:** Transition matrix has rational entries. Matrix power Aⁿ is exact rational arithmetic. The steady state is the exact eigenvector. VDR-2 gym 11 computed exact steady state [2/3, 1/3] for a 2-state chain. For a 5-state chain with transition probabilities like 1/7, 3/11, 2/13, the steady state components have denominators involving 7, 11, 13 — all infinite repeating decimals in base 10, all exact in VDR.

**Mixing time analysis:** How many steps until Aⁿ is close to the steady-state matrix? The mixing time depends on the second-largest eigenvalue magnitude |λ₂|. Computing |λ₂| exactly (for 2×2 chains) or to arbitrary precision (via Newton functional remainder for larger chains) means the mixing time bound is exact, not contaminated by arithmetic error in the eigenvalue computation.

**Where it matters:** PageRank (the original Google algorithm is exact Markov steady state — VDR-3 gym 16 computed exact PageRank summing to exactly 1), queueing theory (steady-state queue lengths), population genetics (allele frequency evolution), MCMC convergence diagnostics.

---

### 9. Elliptic Curve Arithmetic

**The problem:** Points on an elliptic curve y² = x³ + ax + b over the rationals have coordinates that are rational numbers. Point addition involves: λ = (y₂-y₁)/(x₂-x₁), x₃ = λ² - x₁ - x₂, y₃ = λ(x₁-x₃) - y₁. Every operation produces rationals. But the denominators grow rapidly: after n point doublings, coordinates can have denominators with O(4ⁿ) digits due to the height growth of rational points.

**mpmath:** Each point addition truncates the coordinates. After 20 doublings, the coordinates have ~10⁶ digit denominators that mpmath truncates to N digits. The truncated point is not on the curve — y² ≠ x³ + ax + b due to truncation. You can't verify group law properties on truncated points.

**VDR:** Each point addition is exact rational arithmetic. After 20 doublings, the coordinates have enormous denominators but are exactly on the curve: y₃² = x₃³ + ax₃ + b as exact VDR equality. Group law associativity (P+Q)+R = P+(Q+R) verified as exact structural equality, not approximate numerical agreement. The height of the point (log of denominator) is exactly computable.

**Where it matters:** Elliptic curve cryptography (point multiplication nG must be exact), Birch and Swinnerton-Dyer conjecture computations (rational point heights), integer factorization via elliptic curves (Lenstra's ECM), computing Mordell-Weil groups.

---

### 10. Partition Functions and Statistical Mechanics

**The problem:** The partition function Z = Σ exp(-βEᵢ) sums Boltzmann weights over all microstates. For discrete systems, the energies Eᵢ are often rational (in natural units). exp(-βEᵢ) for rational β and Eᵢ is transcendental — but via Taylor series, each partial sum is an exact rational. Free energy F = -kT·ln(Z), entropy S = -∂F/∂T, specific heat C = T·∂S/∂T — all involve chains of transcendental evaluations.

**mpmath:** exp(-β·E) at each state is a truncated decimal. Sum N states: N truncations accumulated. Take ln of the sum: truncation of a truncation. Differentiate numerically: subtract two nearly-equal truncated values (catastrophic cancellation). The specific heat of a 2-state system at the Schottky anomaly involves computing d²F/dT², which is a second derivative of a log of a sum of exponentials — three layers of truncation.

**VDR:** Each exp(-βEᵢ) via functional remainder Taylor series: exact rational at each depth. Sum over states: exact rational. ln(Z) via functional remainder: exact rational at each depth. Discrete derivative (VDR-1 discrete calculus): (F(T+h) - F(T))/h is exact for any rational h. No catastrophic cancellation because the subtraction is exact. The Schottky specific heat peak location and height are computable to arbitrary precision by increasing Taylor depth — not by increasing decimal digits and hoping the truncation doesn't corrupt the answer.

**Where it matters:** Phase transition analysis (specific heat divergence at critical temperature), quantum statistical mechanics (Bose-Einstein and Fermi-Dirac distributions involve exp(βE)±1 in the denominator — the ±1 is a subtraction of a near-unit value, catastrophic in float), astrophysics (equation of state for stellar interiors), chemical equilibrium (equilibrium constants as ratios of partition functions).

---

### 11. Runge-Kutta with Exact Butcher Tableaux

**The problem:** Runge-Kutta methods have coefficients specified as exact rationals in the Butcher tableau. Classic RK4: coefficients 1/2, 1/6, 1/3. These are exact rationals with factors of 2 and 3 in denominators. Higher-order methods (Dormand-Prince, Fehlberg) have coefficients like 1/5, 1/10, 3/40, 9/40, 1/8, 12/13, 1/12, 4243/5348 — denominators with factors of 3, 5, 7, 13, 17, 1337.

**mpmath:** 1/3 = 0.333... truncated. 3/40 = 0.075 (terminates — lucky, 40 = 2³·5). But 9/40 · f(t + 3/40·h) involves multiplying 0.075·h (exact) by f evaluated at a point computed with truncated coefficients. The Butcher tableau's order conditions are algebraic identities among the coefficients: Σbᵢ = 1, Σbᵢcᵢ = 1/2, Σbᵢaᵢⱼcⱼ = 1/6. In decimal, these identities hold only approximately. The method's order is guaranteed by these identities — if they don't hold exactly, the method isn't exactly order 4.

**VDR:** Every Butcher coefficient is [p, q, 0]. The order conditions Σbᵢ = 1 verified as exact equality. Σbᵢcᵢ = 1/2 exact. The method is provably order 4 (or 5, or 8) because the algebraic conditions hold exactly. Each RK stage is exact rational arithmetic on exact rational data. VDR-2 gym 9 demonstrated: Euler method y(1) = (11/10)¹⁰ exact, RK4 approximately 140× better accuracy than Euler — and both results are exact rationals, so the accuracy comparison is itself exact.

**Where it matters:** Validating new RK methods (do the order conditions actually hold?), reference solutions for ODE benchmarks, long-time integration where method error and arithmetic error must be separated.

---

### 12. Galois Field Arithmetic and Error Correction

**The problem:** Reed-Solomon codes, BCH codes, and turbo codes operate over Galois fields GF(p^n). All arithmetic is modular: addition and multiplication mod an irreducible polynomial. The coefficients are integers mod p. No fractions, no decimals — but the syndrome computation, error locator polynomial, and Chien search involve chains of field multiplications where each step's output feeds the next.

**mpmath:** Irrelevant — Galois field arithmetic is integer modular arithmetic. But implementations in float (some MATLAB code, some educational implementations) silently convert field elements to doubles, perform arithmetic, and round back. This works for GF(2⁸) (elements 0-255 fit in float mantissa) but fails for GF(2¹⁶) and above where integer values exceed float precision.

**VDR:** GF(p) elements are [a, 1, 0] with a in {0,...,p-1}. gf_add, gf_mul, gf_inv, gf_pow (VDR-10 builtins) are exact modular operations. VDR-3 gym 18 verified: all 6 GF(7) inverses correct, all 16 Hamming(7,4) codewords have syndrome 0, all 7 single-bit errors corrected, minimum distance = 3 by exhaustive 120-pair comparison. No float anywhere. The error correction is either correct or it isn't — exact arithmetic means the code either corrects the error or provably doesn't.

**Where it matters:** Satellite communication (deep space links use Reed-Solomon + convolutional codes — error in the decoder means lost data), QR codes, data storage (RAID parity), 5G NR polar codes, DNA storage (emerging field using Reed-Solomon over GF(4) for ACGT alphabet).

---

### 13. Characteristic Polynomial and Cayley-Hamilton Verification

**The problem:** The Cayley-Hamilton theorem states every matrix satisfies its own characteristic polynomial: if p(λ) = det(A - λI) = λⁿ - c₁λⁿ⁻¹ - ... - cₙ, then p(A) = 0. The zero here is the zero matrix — every entry must be exactly zero.

**mpmath:** Compute characteristic polynomial coefficients as truncated decimals. Evaluate p(A) = Aⁿ - c₁Aⁿ⁻¹ - ... - cₙI. Each matrix power involves multiplications of truncated entries. The result is not the zero matrix — it's a matrix with entries ~10⁻(N-something) where N is the working precision. You can't verify Cayley-Hamilton; you can only verify that p(A) is "small."

**VDR:** Characteristic polynomial coefficients are exact rationals (computed from exact determinant). p(A) = exact zero matrix. Every entry is VDR(0, 1, 0). Not approximately zero. Zero. VDR-2 gym 2 and VDR-3 gym 21 verified: M² - 5M + 5I = 0 exactly, A² + 3A + 2I = 0 exactly. This is a structural identity verified by structural equality, not a numerical residual compared to a tolerance.

**Where it matters:** Control theory (Cayley-Hamilton is used to compute matrix exponentials for state-space systems), minimal polynomial computation (exact Cayley-Hamilton tells you the characteristic polynomial annihilates A; the minimal polynomial divides it — finding it requires exact zero-testing), matrix function evaluation (f(A) via polynomial representation requires knowing exactly which powers of A are independent).

---

### 14. Farey Sequences and Stern-Brocot Trees

**The problem:** The Farey sequence Fₙ contains all reduced fractions with denominator ≤ n in [0,1], ordered by size. The mediant property: for consecutive Farey neighbors a/b and c/d, |ad - bc| = 1. This is an exact integer identity. The Stern-Brocot tree organizes all positive rationals as a binary tree where each node is the mediant of its ancestors.

**mpmath:** Representing Farey fractions as decimals destroys the structure. 1/3 = 0.333... and 1/4 = 0.25 are consecutive in F₄. The mediant is (1+1)/(3+4) = 2/7 = 0.285714... Computing |1·4 - 3·1| = |4-3| = 1 requires exact integer arithmetic on the numerators and denominators. In decimal, you'd need to recover the fraction from the decimal — lossy and fragile.

**VDR:** 1/3 = [1, 3, 0]. 1/4 = [1, 4, 0]. Mediant = [2, 7, 0]. |ad - bc| = |1·4 - 3·1| = 1. Exact. VDR-2 gym 1 verified the mediant property for all consecutive pairs in Farey sequences. The Stern-Brocot path to any rational is computable by exact comparison: is the target less than, equal to, or greater than the current node? VDR comparison is exact (cross-multiply and compare integers). Decimal comparison of 355/113 vs π requires knowing how many digits of each to trust.

**Where it matters:** Number theory (distribution of rationals, Ford circles, hyperbolic geometry), clock synchronization (best rational approximation to frequency ratios), music theory (just intonation intervals as exact rationals — 3/2 is a perfect fifth, 5/4 is a major third, 81/80 is the syntonic comma).

---

### 15. Exact Polynomial GCD and Resultants

**The problem:** The GCD of two polynomials with rational coefficients is a polynomial with rational coefficients. The Euclidean algorithm for polynomial GCD involves polynomial long division, which produces quotients and remainders with rational coefficients whose denominators grow at each step. The resultant of two polynomials is a determinant of the Sylvester matrix — an integer linear combination of products of coefficients.

**mpmath:** Polynomial division of (x² - 1) by (x² + 2x + 1): quotient 1, remainder -2x - 2. In decimal with irrational or high-denominator rational coefficients, each division step truncates. After several GCD steps, the remainder might be a polynomial with coefficients like 10⁻¹⁵ — is this zero (polynomials are coprime) or a truncation artifact? You can't tell.

**VDR:** Division of [1,0,-1] by [1,2,1]: quotient [1], remainder [-2,-2]. Exact. The GCD is [1,1] (representing x+1). VDR-2 gym 2 verified: poly GCD(x²-1, x²+2x+1) = (x+1) exactly. No tolerance needed. A remainder coefficient is either zero or it isn't. The question "are these polynomials coprime?" has an exact yes/no answer.

**Where it matters:** Control theory (coprimeness of numerator and denominator polynomials determines controllability), algebraic geometry (intersection multiplicity via resultants), computer algebra (simplification of rational functions), coding theory (polynomial GCD over finite fields for BCH decoding).

---

### 16. Padé Approximants

**The problem:** A Padé approximant [L/M] to a function f(x) matches the Taylor series through order L+M. Computing the coefficients requires solving a linear system where the matrix entries are Taylor coefficients — rational numbers for functions like exp, sin, cos, ln at rational arguments. The resulting Padé coefficients are rationals whose denominators involve all the prime factors from the Taylor coefficients (factorials produce primes up to L+M).

**mpmath:** Taylor coefficients 1/n! become truncated decimals. 1/7! = 1/5040 = 0.000198412698... The linear system solve on these truncated values produces Padé coefficients that are approximately correct. For high-order Padé approximants (L+M > 20), the coefficient matrix becomes ill-conditioned and mpmath needs hundreds of digits to get correct coefficients.

**VDR:** 1/7! = [1, 5040, 0]. Exact. The linear system is solved by exact Gaussian elimination or Cramer's rule. The Padé coefficients are exact rationals. The approximant's error at any rational point is computable as an exact rational (evaluate the approximant and subtract from the Taylor partial sum — both exact). For exp(x), the [4/4] Padé approximant has coefficients involving denominators up to 1680 = 2⁴·3·5·7. In decimal, 1/1680 = 0.000595238095238... repeating. In VDR: [1, 1680, 0].

**Where it matters:** Numerical methods (Padé approximants are the basis for many matrix exponential algorithms), signal processing (model reduction via Padé), circuit simulation (SPICE uses Padé for delay elements), quantum field theory (Padé-Borel summation of divergent perturbation series).

---

### 17. Exact Integration of Rational Functions

**The problem:** The integral of a rational function p(x)/q(x) is computed by partial fraction decomposition followed by integration of each term. PFD requires factoring q(x), which produces roots that may be rational. For each rational root r, the corresponding partial fraction has the form A/(x-r). Integrating gives A·ln(x-r). But computing A requires evaluating p(r)/q'(r) — division of polynomials evaluated at a rational point.

**mpmath:** If r = 3/7, evaluating p(3/7) involves substituting 0.428571... into polynomial coefficients and multiplying truncated decimals. The residue A = p(3/7)/q'(3/7) is a ratio of two truncated values — potentially catastrophic if they're nearly equal.

**VDR:** r = [3, 7, 0]. p(3/7) evaluated by Horner's method: each multiply-and-add is exact rational arithmetic. q'(3/7) similarly. A = p(r)/q'(r) is exact rational. VDR-2 gym 13 verified: PFD of 1/((x-1)(x-2)) = -1/(x-1) + 1/(x-2) exactly. The definite integral ∫₀¹ x² dx = 1/3 exact via exact antiderivative evaluation.

**Where it matters:** Symbolic computation (exact integration is the foundation of computer algebra), physics (Feynman parameter integrals are often rational function integrals), probability (moment generating functions involve integrals of rational functions times exponentials), control theory (inverse Laplace transforms via partial fractions).

---

### 18. Lattice Basis Reduction (LLL Algorithm)

**The problem:** The LLL algorithm reduces a lattice basis by iteratively performing Gram-Schmidt orthogonalization and size reduction. The Gram-Schmidt coefficients μᵢⱼ = <bᵢ, b*ⱼ> / <b*ⱼ, b*ⱼ> are exact rationals when the input vectors have rational coordinates. The Lovász condition ||b*ₖ||² ≥ (3/4 - μ²ₖ,ₖ₋₁) ||b*ₖ₋₁||² involves comparing exact rationals.

**mpmath:** Gram-Schmidt coefficients truncated to N digits. The Lovász condition comparison is on truncated values. A coefficient μ = 0.500000000000001 (above 1/2, needs size reduction) vs μ = 0.499999999999999 (below 1/2, doesn't) — mpmath can't distinguish these if the true value is within truncation range of 1/2. Wrong decision means wrong basis, wrong lattice reduction, wrong cryptanalysis result.

**VDR:** μ = [p, q, 0] exact rational. Comparison to 1/2: cross-multiply p·2 vs q·1, compare exact integers. The Lovász condition is an exact rational comparison. No borderline ambiguity. VDR-3 gym 20 verified: lattice μ₂₁ = 1/2 exact, v₁·v₂* = 0 exactly, Lovász condition checked with exact rational comparison.

**Where it matters:** Cryptanalysis (breaking lattice-based cryptosystems requires LLL or BKZ with correct basis reduction), integer programming (lattice reduction for finding short vectors), number theory (finding algebraic relations between constants), GPS (integer ambiguity resolution uses lattice reduction).

---

### 19. Groebner Bases

**The problem:** Groebner basis computation (Buchberger's algorithm) involves polynomial division with remainder over multivariate polynomials. Each S-polynomial computation and reduction step produces new polynomials with rational coefficients whose denominators grow. The critical decision at each step: is the remainder zero? If yes, the S-polynomial reduces to zero and the pair is processed. If no, the remainder is added to the basis.

**mpmath:** Polynomial coefficients as truncated decimals. After many reduction steps, a remainder coefficient might be 3.7 × 10⁻¹⁵. Is this zero (reduction succeeds) or nonzero (new basis element)? With mpmath at 50 digits, it might be 3.7 × 10⁻⁴⁵. Still can't tell. Increasing precision doesn't solve the zero-testing problem — it just moves the ambiguity to smaller magnitudes.

**VDR:** Remainder coefficient is either [0, 1, 0] or it isn't. Zero-testing is exact structural comparison. The Groebner basis computation terminates with the correct basis, not an approximately-correct basis that might have extra elements (from nonzero remainders that should have been zero) or missing elements (from zero remainders that should have been nonzero).

**Where it matters:** Algebraic geometry (ideal membership testing, variety computation), robotics (solving polynomial systems for inverse kinematics), coding theory (decoding algebraic codes), statistics (design of experiments, algebraic statistics).

---

### 20. Quantum Error Correction Stabilizer Codes

**The problem:** Stabilizer codes for quantum error correction are defined by Pauli group elements — tensor products of I, X, Y, Z matrices. The stabilizer group generators are products of these matrices. Checking code properties (distance, transversality) requires computing products of Pauli matrices and checking if results are ±I or ±iI. The entries are from {0, ±1, ±i}.

**mpmath:** Represents i as 0 + 1.0j. Multiplying many Pauli matrices in float: (0+1j)·(0+1j) = -1+0j in exact arithmetic, but float gives -1+1.2e-16j. After 20 matrix multiplications, the imaginary part of what should be a real number is ~10⁻¹⁵. Is the result ±I (real) or ±iI (imaginary)? Float can't tell for borderline cases.

**VDR:** i represented as a pair of VDR values (0, 1). Multiplication: (0+1i)·(0+1i) = (-1, 0). Exact. After 20 multiplications: exact. The result is either (±1, 0) (real, meaning ±I) or (0, ±1) (imaginary, meaning ±iI). Exact classification. VDR-13 verified Pauli algebra: σ_x² = I, σ_x·σ_y = iσ_z as exact structural equalities. Code distance computation requires checking if a Pauli operator commutes with all stabilizers — commutation is exact comparison of matrix products, not approximate.

**Where it matters:** Designing quantum error correcting codes, verifying fault-tolerance thresholds, topological code analysis (surface codes, color codes), magic state distillation protocols.

---

### The Unifying Principle

Every domain above contains the same structural vulnerability: a computation chain where intermediate values have denominators with prime factors other than 2 and 5, forcing decimal/mpmath truncation at every step. VDR's representation [V, D, 0] carries the exact denominator — whether it's 3, 7, 13, 5040, 117117, or a 200-digit product of primes — as an exact integer. No truncation, no repeating decimal, no lost digits. The denominator grows but nothing is discarded. This is not "more precision" — it is a categorically different relationship with the numbers. mpmath says "I have 1000 digits, which is probably enough." VDR says "I have the exact answer."
