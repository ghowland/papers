# VDR-28 DECIMAL TRUNCATION DOMAINS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → domains → zero_testing → cancellation → prior_validation → relationships → sections

# principles(id|principle|rationale)
P1|Decimal is structurally incompatible with most rationals|10 = 2×5; only denominators factoring into 2s and 5s terminate; 60% of small denominators repeat; every factorial, every odd prime denominator forces truncation
P2|Arbitrary precision does not solve the problem|mpmath at 1000 digits still truncates 1/3; each operation discards information; N operations = N truncations; user cannot determine which digits are wrong without 2N digits
P3|VDR is categorically different, not more precise|[1, 3, 0] is exact — three integers, zero truncation; denominator stored as integer not decomposed into decimal; chains of operations produce exact rationals with growing denominators but nothing discarded
P4|Zero-testing is the critical operation|Is a computed value zero or merely small? Decimal cannot answer; VDR: [0, 1, 0] or not; determines correctness of GCD, Groebner basis, rank, Cayley-Hamilton, independence, coprimeness

# claims(id|claim|type|depends_on)
CL1|20 main + 23 appendix = 43 total domains where decimal truncation produces materially wrong results|observation|P1
CL2|Among first 20 denominators: 8 terminate (40%), 12 repeat (60%); among 1-100: ~12 terminate, ~88 repeat|observation|P1
CL3|Hilbert matrix H₅⁻¹ residual = 0 in VDR; H₁₀ = 0; H₂₀ = 0; H₃₀ = 0; entries are exact integers|observation|P3
CL4|Every Bernoulli number B_{2n} for n≥1 has at least one odd prime in denominator; every RK method order≥2 has coefficient with factor of 3; decimal trap is endemic in numerical mathematics|observation|P1
CL5|VDR-2 gym domain 11: binomial PMF n=10 p=1/3 sums to exactly 1; Bayesian posterior 6/7 exact|observation|P3
CL6|Polynomial GCD zero-testing is unsolvable in truncated decimal; VDR: remainder is [0,1,0] or it is not|observation|P4
CL7|Cayley-Hamilton: p(A) = exact zero matrix in VDR; every entry [0,1,0]; M²-5M+5I = 0 exactly|observation|P4
CL8|Prior validation: >400 tests across 14 gym domains + 6 papers; zero VDR computation errors|observation|

# concepts(id|name|definition|category)
C1|Decimal trap|Structural incompatibility between base-10 representation and rational values with odd prime denominators; forces infinite repeating decimals requiring truncation|problem
C2|Terminating decimal test|Fraction a/b terminates iff all prime factors of b (reduced) are 2 or 5; otherwise infinite repeating with period determined by multiplicative order|criterion
C3|Zero-testing problem|Determining whether a computed value is exactly zero; decimal: ambiguous at any precision (is 10⁻¹⁵ zero?); VDR: structural comparison [0,1,0] or not|problem
C4|Denominator growth|Exact rational chains produce denominators that grow multiplicatively; after N multiplications, denominator has O(N) prime factors; managed by Q335 fixed-frame|property
C5|Catastrophic cancellation in decimal|Subtracting nearly-equal truncated values loses most significant digits; amplified in derivatives, eigenvalues near zero, correction terms|failure_mode
C6|Decimal compatibility test|Computation is decimal-compatible iff no division by anything other than power of 2 or 5 occurs anywhere, including implicit division through averaging, normalization, matrix inversion|criterion

# domains_main(id|domain|typical_denominators|decimal_period|key_vulnerability|vdr_solution|prior_validation)
DM01|Continued fractions|All primes up to convergent index|Variable, large|Convergent quality requires exact subtraction of nearly-equal values|Each convergent [pₙ, qₙ, 0] exact; recurrence is exact integer arithmetic|VDR-2 gym 3: 19/19
DM02|Bernoulli numbers / zeta|All primes p where (p-1)|2n|Up to thousands|B₁₂ denom 2730 = 2·3·5·7·13; grows with index|[-691, 2730, 0] exact; zeta via exact Bernoulli × Q335 π|VDR-3: 157 tests
DM03|Hilbert matrix|All primes up to 2n-1|LCM of all|Exponential condition number amplifies every truncation digit|H⁻¹ residual = exactly 0; det(H₄) = [1, 6048000, 0]|VDR-1: 68/68; VDR-2
DM04|Eigenvalue problems|Factors of trace and determinant|Product of factors|Eigenvalue sign near zero: truncation determines stability verdict|Discriminant exact rational; √disc via Newton; eigenvectors exact|VDR-2 gym 4,11
DM05|Gaussian elimination pivots|O(n) distinct primes|Product of periods|Pivot 7/13 = 1.857142... truncated; compounds through O(n²) operations|[13, 7, 0] exact; 400 operations: exact; H₃₀ pivots 185-digit denoms|VDR-13
DM06|Bayesian updates|Factors of all priors and likelihoods|Cumulative product|Sequential updates: each posterior's denominator accumulates primes|Exact rational posteriors after any number of updates|VDR-2 gym 11: 19/19
DM07|Markov chain steady states|All factors from transition matrix|Product of periods|Steady state components have odd prime denominators; power method compounds|Exact eigenvector; PageRank sums to exactly 1|VDR-2 gym 11; VDR-3 gym 16
DM08|Elliptic curve arithmetic|Height growth O(4ⁿ) digits|Enormous|After 20 doublings ~10⁶ digit denominators; truncated point not on curve|Exact point on curve: y² = x³+ax+b as exact equality|Structural analysis
DM09|CRT / modular arithmetic|Primes from moduli|N/A|Reconstructed rational truncated on entering further computation|[a, b, 0] exact through all subsequent computation|VDR-2 gym 12: RSA roundtrip
DM10|Partition functions|Primes from energy denominators|Product of periods|Schottky anomaly: d²F/dT² requires 3 layers of truncation|Each exp Taylor exact rational; discrete derivatives exact; no cancellation|VDR-1 functional remainder
DM11|Runge-Kutta tableaux|All primes in coefficient denominators|Product of periods|Truncated coefficients mean method is not the claimed order; identities only approximately hold|Butcher coefficients exact; Σbᵢ = 1 exactly; order conditions verified as equalities|VDR-2 gym 9
DM12|Galois field / error correction|p (field characteristic)|N/A (modular)|Float implementations of GF(2¹⁶)+ silently round|gf_add, gf_mul, gf_inv exact modular; Hamming(7,4) all errors corrected|VDR-3 gym 18
DM13|Cayley-Hamilton|All primes from matrix entries|Product of periods|p(A) ≈ 10⁻ᴺ matrix; theorem cannot be verified, only approximately confirmed|p(A) = exact zero matrix; every entry [0, 1, 0]|VDR-2 gym 2; VDR-3 gym 21
DM14|Farey sequences / Stern-Brocot|All primes (every rational appears)|Variable|Cannot recover integer numerator/denominator from truncated decimal|[1, 3, 0] preserves structure; mediant property |ad-bc|=1 verified exactly|VDR-2 gym 1: 19/19
DM15|Polynomial GCD / resultants|All primes from coefficients|Product of periods|Is remainder coefficient zero? Unsolvable at any decimal precision|Zero-testing exact: [0, 1, 0] or not; GCD(x²-1, x²+2x+1) = (x+1) exact|VDR-2 gym 2
DM16|Padé approximants|Primes up to (L+M)!|Product of periods|Factorial denominators; ill-conditioned coefficient matrix at high order|Exact Gaussian elimination; exact coefficients; exact error evaluation|VDR-1 exact elimination
DM17|Lattice basis reduction (LLL)|Factors from Gram-Schmidt coefficients|Product of periods|μ = 0.500000000000001 vs 0.499999999999999: wrong decision → wrong basis|μ = [p, q, 0]; comparison to 1/2 by cross-multiplication: exact|VDR-3 gym 20
DM18|Groebner bases|All primes from polynomial coefficients|Product of periods|Same zero-testing as polynomial GCD, amplified across many reduction steps|Zero-testing exact; correct basis guaranteed|Structural analysis
DM19|Quantum error correction stabilizers|Only ±1, ±i|N/A for entries|After 20 Pauli multiplications: imaginary part ~10⁻¹⁵; is result real or imaginary?|Complex pair (±1, 0) or (0, ±1) exact; classification exact|VDR-13
DM20|Quadratic irrationalities (Pell equation)|Continued fraction convergents|Variable|x²-Dy²=1 verification requires exact large integer arithmetic|[pₙ, qₙ, 0] exact; pₙ²-D·qₙ² = 1 verified exactly|VDR-2 gym 3

# zero_testing_domains(domain|question|decimal_behavior|vdr_behavior|consequence_of_wrong_answer)
Polynomial GCD|Is remainder coefficient zero?|Ambiguous at any precision|Exact: [0,1,0] or not|Wrong GCD
Groebner basis|Is S-polynomial remainder zero?|Ambiguous|Exact|Wrong basis
Cayley-Hamilton|Is p(A) the zero matrix?|Every entry ≈ 10⁻ᴺ, never 0|Every entry exactly [0,1,0]|Cannot verify theorem
Matrix rank|Is singular value zero or small?|Indistinguishable below ~10⁻¹⁵|Exact zero or exact nonzero|Wrong rank
Linear independence|Is determinant zero?|Ambiguous near zero|Exact|Wrong conclusion
Eigenvector orthogonality|Is dot product zero?|≈ 10⁻¹⁵|Exactly 0|Cannot verify
Polynomial coprimeness|Is GCD = 1?|Requires zero-testing|Exact|Wrong controllability
LLL threshold|Is μ > 1/2?|Ambiguous near 1/2|Exact comparison|Wrong basis reduction
Farey mediant|Is |ad-bc| = 1?|Requires exact integer recovery|Exact integer arithmetic|Structure verification impossible
Conservation law|Is energy change zero?|≈ 10⁻¹⁵|Exactly 0 or nonzero|False conservation or missed violation

# cancellation_domains(domain|operation|when|decimal_digits_lost|vdr_digits_lost)
Continued fraction quality|α - p/q|Always (quality = closeness)|Most significant digits|0
Eigenvalue near zero|(a+d)/2 - √disc|Discriminant ≈ (trace/2)²|Up to all digits|0
Specific heat (Schottky)|F(T+h) - F(T)|Derivative computation|Proportional to -log₁₀(h)|0
Bose-Einstein denominator|exp(βE) - 1|Small βE|Most digits|0
Stability eigenvalue|Real part of complex eigenvalue|Real ≈ 0|Most digits|0 (to Newton depth)
Cayley-Hamilton|Aⁿ - c₁Aⁿ⁻¹ - ...|Similar-magnitude terms|Many per entry|0
Gaussian elimination|a - (b·c/d)|a ≈ b·c/d|Proportional to condition#|0
Polynomial GCD remainder|p(x) - q(x)·quotient|Nearly equal polynomials|May lose all|0
LLL μ near 1/2|μ - 1/2|μ ≈ 1/2|May lose all|0

# bernoulli_denominators(index|value|denominator|prime_factors|decimal_period)
B₂|1/6|6|2·3|1
B₄|-1/30|30|2·3·5|1
B₆|1/42|42|2·3·7|6
B₈|-1/30|30|2·3·5|1
B₁₀|5/66|66|2·3·11|2
B₁₂|-691/2730|2730|2·3·5·7·13|12
B₁₄|7/6|6|2·3|1
B₁₆|-3617/510|510|2·3·5·17|16
B₁₈|43867/798|798|2·3·7·19|18
B₂₀|-174611/330|330|2·3·5·11|2
# Every B_{2n} for n≥1 has factor of 3; most have additional odd primes

# appendix_domains(id|category|domain|key_operation|prior_validation)
AD01|Algebraic number theory|Minimal polynomial verification, norms, Pell equation|Exact evaluation at algebraic numbers|VDR-1, VDR-2 gym 1,3
AD02|Combinatorial optimization|Simplex pivots, assignment, network flow, knapsack|Exact comparison for tie-breaking|Exact rational comparison
AD03|Algebraic geometry|Bézout verification, genus, rational points, Hilbert function|Exact zero-testing; exact point arithmetic|VDR-2 gym 2
AD04|Representation theory|Character tables, Schur orthogonality, Young tableaux hook lengths|Exact factorial arithmetic; exact 1/|G| division|VDR-2 gym 5
AD05|Topology / homology|Smith normal form, Betti numbers, Euler characteristic|Exact integer matrix operations; exact rank|Exact linear algebra
AD06|Category theory / logic|Functor composition, natural transformation coherence, SMT|Exact comparison; exact structural equality|Exact arithmetic
AD07|Information theory|Shannon entropy, KL divergence, mutual information, arithmetic coding|Exact probability × Taylor log chains|VDR-1 functional remainder
AD08|Differential geometry|Discrete curvature, Christoffel symbols, holonomy|Exact rational metric; exact matrix inverse chain|VDR-2
AD09|Mathematical physics|Clebsch-Gordan, Wigner symbols, Ising partition, Casimir energy|Exact factorial ratios; exact Boltzmann weights|VDR-2 gym 5; VDR-13
AD10|Numerical methods theory|Convergence order, Richardson extrapolation, Romberg, Adams-Bashforth|Exact error measurement; exact extrapolation coefficients|VDR-2 gym 2
AD11|Coding theory beyond GF|LDPC belief propagation, polar code Bhattacharyya, fountain codes|Exact rational recursion|VDR-3 gym 18
AD12|Mathematical logic|Compactness, ultraproducts, Tarski decidability, Presburger|Exact comparison; exact polynomial evaluation|Exact arithmetic
AD13|Actuarial science|Life tables, net premium, reserves, loss development, credibility|Exact mortality rates; exact compound interest|Solvency II/GAAP compliance
AD14|Music theory|Just intonation ratios, Pythagorean comma, temperament comparison|Exact frequency ratios; exact interval comparison|Exact comparison
AD15|Economics / econometrics|Leontief input-output, Gini, OLS, present value, Arrow-Debreu|Exact matrix inverse; exact rational chain|Exact linear algebra
AD16|Formal verification|Model checking, abstract interpretation, SMT, probabilistic model checking|Exact comparison; exact probability|Exact arithmetic

# decimal_compatibility_test(condition|decimal_compatible|vdr_advantage)
All inputs are integers|Yes|None for add/sub
All denominators are powers of 2 or 5|Yes|None
Any input has factor of 3 in denominator|No|Exact vs truncated
Division by any odd number > 5|No|Exact vs truncated
Mean of N values where N has odd factor|No (introduces 1/N)|Exact vs truncated
Factorial in denominator (n! for n≥3)|No (3 divides 3!)|Exact vs truncated
Any prime modulus (Galois field)|No|Exact modular
Bayesian normalization|Almost always no|Exact vs truncated
Matrix entries with odd denominators|No|Exact linear algebra

# cost_of_exactness(domain|problem_size|float64_ops|vdr_python_ops|ratio|justified_by)
Continued fraction 200 convergents|200 iterations|~600|~30,000|50×|Exact quality measures
Hilbert inverse 10×10|10³ multiplications|~1,000|~50,000|50×|Zero vs 10⁻²⁰ residual
Bayesian 100 updates|100 × ~10 ops|~1,000|~50,000|50×|Exact posterior for diagnostics
RK4 100 steps 1D|100 × ~10 ops|~1,000|~50,000|50×|Provable method order
Polynomial GCD degree 10|~100 operations|~100|~5,000|50×|Exact zero-testing
LLL dimension 5|~100 × ~25 ops|~2,500|~125,000|50×|Exact threshold comparison
Cayley-Hamilton 5×5|~4,000 ops|~4,000|~200,000|50×|Exact zero verification
Hamming(7,4) decode|~50 ops|~50|~2,500|50×|Exact error correction
# Ratio ~50× Python across all domains; ~150× on Q335 GPU

# domain_interconnections(domain_a|domain_b|shared_vulnerability|example)
Bernoulli numbers|Padé approximants|Factorial denominators with odd primes|exp Padé coefficients involve 1/n!
Hilbert matrix|Gaussian elimination|Growing pivot denominators|H inverse requires exact pivots
Eigenvalues|Markov chains|Steady state is eigenvector for λ=1|Steady state denominators from transition matrix
Polynomial GCD|Groebner bases|Both depend on exact zero-testing|Remainder zero → different algorithm path
Galois fields|Cryptography|Exact field arithmetic|RSA, ECC, post-quantum lattice
Lattice LLL|Cryptanalysis|Exact threshold comparison|Breaking lattice-based encryption
Elliptic curves|Cryptography|Exact point arithmetic|ECC key generation
Runge-Kutta|Physics simulation|Exact Butcher coefficients|ODE integration with proven order
Cayley-Hamilton|Control theory|Exact matrix polynomial evaluation|Matrix exponential via CH
Gaussian elimination|All linear algebra|Exact pivots|Foundation for inverse, rank, determinant

# relationships(from|rel|to)
P1|defines|C1
P1|defines|C2
P2|opposes|C1
P3|solves|C1
P3|eliminates|C5
P4|defines|C3
P4|enables|CL6
P4|enables|CL7
C1|affects|DM01-DM20
C2|determines|P1
C3|critical_for|DM13,DM15,DM17,DM18
C4|managed_by|Q335 fixed-frame
C5|caused_by|C1
C6|determines|P1
CL1|summarizes|DM01-DM20,AD01-AD16
CL3|demonstrates|P3
CL4|demonstrates|P1
CL8|validates|P3

# section_index(section|title|ids)
1|The Decimal Trap|P1,P2,P3,C1,C2,CL2
2|Continued Fractions|DM01
3|Bernoulli Numbers / Zeta|DM02,CL4
4|Hilbert Matrix|DM03,CL3
5|Eigenvalue Problems|DM04
6|Gaussian Elimination|DM05
7|Bayesian Updates|DM06,CL5
8|Markov Steady States|DM07
9|Elliptic Curves|DM08
10|CRT / Modular|DM09
11|Partition Functions|DM10
12|Runge-Kutta|DM11
13|Galois Fields|DM12
14|Cayley-Hamilton|DM13,CL7,P4
15|Farey / Stern-Brocot|DM14
16|Polynomial GCD|DM15,CL6,P4
17|Padé Approximants|DM16
18|Lattice LLL|DM17
19|Groebner Bases|DM18
20|Quantum Stabilizers|DM19
21|Unifying Principle|P1,P3
22|Boundaries|C4,LM
A|Denominator Prime Factors by Domain|prime factor analysis per domain
B|Zero-Testing Failure Modes|zero_testing_domains
C|Repeating Decimal Periods|common denominators table
D|Prior Validation by Domain|20 domains × 6 papers × 14 gym domains; >400 tests; zero VDR errors
E|Catastrophic Cancellation|cancellation_domains
F|Cost of Exactness|cost_of_exactness
G|Decimal Compatibility Test|decimal_compatibility_test
H|Domain Interconnection Map|domain_interconnections
I|Algebraic Number Theory|AD01
J|Combinatorial Optimization|AD02
K|Algebraic Geometry|AD03
L|Representation Theory|AD04
M|Topology / Homology|AD05
N|Category Theory / Logic|AD06
O|Information Theory|AD07
P|Differential Geometry|AD08
Q|Mathematical Physics|AD09
R|Numerical Methods Theory|AD10
S|Coding Theory|AD11
T|Mathematical Logic|AD12
U|Actuarial Science|AD13
V|Music Theory|AD14
W|Economics / Econometrics|AD15
X|Formal Verification|AD16
Y|Prime Factor Density in Constants|bernoulli_denominators + RK/quadrature coefficients
Z|Complete Domain Coverage|43 domains across 17 categories

# decode_legend
format: pipe-delimited tables, ID-based cross-references
core_thesis: decimal (base 10 = 2×5) is structurally incompatible with most rationals; arbitrary precision defers but does not solve; VDR eliminates by storing denominator as exact integer
domain_count: 20 main sections + 23 appendix domains = 43 total
decimal_trap_test: if any division by odd number > 5 occurs anywhere in chain (including implicit through mean, normalization, matrix inverse), trap applies
zero_testing: the critical operation; decimal: ambiguous at any precision; VDR: exact structural comparison
key_results: Hilbert inverse residual = exactly 0; Cayley-Hamilton p(A) = exact zero matrix; Bayesian posterior 6/7 exact; binomial PMF sums to exactly 1; Hamming(7,4) all errors corrected; PageRank sums to exactly 1
cost: ~50× Python, ~150× Q335 GPU per operation; justified when exact zero-testing, exact comparison, or exact chain matters
prior_validation: >400 tests across 14 gym domains + 6 papers; zero VDR computation errors
affected_constants: every Bernoulli B_{2n} (n≥1), every RK coefficient for order≥2, every Gaussian quadrature weight for ≥3 points, every factorial denominator
denominator_management: exact chains grow denominators; Q335 fixed-frame bounds at 2^335 with Remainder carrying overflow
rel_types: defines|opposes|solves|eliminates|enables|affects|critical_for|managed_by|caused_by|determines|summarizes|demonstrates|validates
+standalone: no cross-references to other compact docs
+no_new_primitives: all mechanisms use existing VDR-1 exact rational arithmetic
