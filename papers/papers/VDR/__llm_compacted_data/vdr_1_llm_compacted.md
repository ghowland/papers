# VDR ARITHMETIC: VALUE, DECIMAL, REMAINDER — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → operations → extensions → boundaries → relationships → sections

# principles(id|principle|rationale)
P1|Remainder is not error|R carries exact unresolved structure that scalar systems discard; it is part of the value
P2|Preserve data, compress shape|No operation may discard remainder; exactness maintained through all operations
P3|Finite trees only|Every valid VDR object has finite depth, finite branching, finite total node count
P4|Recursion only through R|V and D are integers; nesting occurs exclusively in the remainder slot
P5|Exact as written|No valid object depends on approximation, limits, or infinite expansion
P6|Two equality relations|Structural equality (slot-by-slot) and normalized value equality (canonical form comparison) are distinct
P7|The code is the specification|Every claim verified by executable tests; implementation is normative

# concepts(id|name|category|definition)
C1|VDR Triple|core|Ordered triple [V, D, R] — V: integer numerator, D: nonzero integer denominator frame, R: remainder
C2|Value Slot (V)|slot|Arbitrary-precision integer; settled numerator component in the current denominator frame
C3|Denominator Slot (D)|slot|Nonzero arbitrary-precision integer; defines the frame in which V and R are interpreted
C4|Remainder Slot (R)|slot|Exact unresolved structure; atomic integer, composite (integer base + finite ordered list of child VDRs), or functional
C5|Closed Object|state|VDR with R=0; behaves exactly as rational number; scalar projection Π([V,D,0]) = V/D
C6|Active Object|state|VDR with R≠0; carries exact state beyond what the D-frame absorbed
C7|Atomic Remainder|remainder-form|Single integer r
C8|Composite Remainder|remainder-form|Integer base r plus finite ordered list of child VDR triples: r + X₁ + … + Xₙ
C9|Functional Remainder|remainder-form|Python callable f(depth:int)→VDR with name string; expanded via resolve()
C10|Structural Equality (≡s)|equality|Slot-by-slot recursive match of all V, D, R values
C11|Normalized Value Equality (≡n)|equality|Structural equality after normalization; used by Python == operator
C12|Scalar Projection (Π)|operation|Recursive evaluation: Π([V,D,R]) = (V + Π(R))/D for comparison with legacy systems
C13|Denominator-Sensitive Completion|semantics|Remainder is interpreted within parent's denominator frame — divided by D, not added externally
C14|Normalization|procedure|Deterministic canonical form: sign convention → GCD reduction → child normalization → canonical ordering → same-D merge → closed-form preference; idempotent
C15|Lift|operation|Remainder transport operator; rescales R when parent denominator frame changes by factor k
C16|Rebase|operation|Changes top-level denominator while preserving exact value; closed rebase (integer result) or active rebase (mismatch witness)
C17|Mismatch Witness|construction|[S, D, 0] capturing exact part that target denominator could not absorb during active rebase
C18|Denominator Complexity|metric|Tuple (u, s, m): distinct denominators, sum of denominators, count of denominator nodes

# normalization_rules(id|rule|detail)
N1|Sign convention|If D < 0, negate both V and D
N2|GCD reduction|For closed nodes, divide V and D by gcd(|V|, |D|)
N3|Atomic remainder consolidation|All integer contributions at same remainder level combined into single base
N4|Child normalization|Every child normalized before parent (bottom-up)
N5|Canonical child ordering|Children sorted by denominator magnitude, then V, then R structure
N6|Same-denominator child merge|Closed children sharing D are added; zero-sum children removed
N7|Closed-form preference|If entire remainder normalizes to zero, object settles to closed form

# closed_arithmetic(id|operation|formula|identity)
CA1|Addition|[V₁D₂ + V₂D₁, D₁D₂, 0]|[0,1,0]
CA2|Subtraction|[V₁D₂ − V₂D₁, D₁D₂, 0]|—
CA3|Multiplication|[V₁V₂, D₁D₂, 0]|[1,1,0]
CA4|Division (V₂≠0)|[V₁D₂, D₁V₂, 0]|—
# Closed subclass is arithmetically closed under all four ops (excl div by zero)
# Additive inverse of [V,D,0] is [-V,D,0]

# active_arithmetic(id|operation|mechanism)
AA1|Same-D addition|[V₁+V₂, D, R₁⊕R₂] — bases summed, child lists concatenated, then normalized
AA2|Different-D addition|Cross-scale to D₁·D₂ frame; lift(R₁,D₂) + lift(R₂,D₁)
AA3|Active multiplication|Frame D₁·D₂, closed numerator V₁·V₂; remainder captures three cross-terms: V₁·R₂, V₂·R₁, R₁·R₂ (projected)
AA4|Active division (by closed)|Multiply by reciprocal [D₂,V₂,0]
AA5|Active division (by active)|Project divisor to exact rational via Π, invert, multiply; divisor's remainder structure not preserved (v1 compromise)
AA6|Negation|-[V,D,R] = [-V, D, -R]; remainder negation negates base and all children recursively

# lift_rules(id|input_form|formula)
L1|Atomic remainder r|lift(r, k) = kr
L2|Composite remainder|lift(r + X₁+…+Xₙ, k) = kr + lift(X₁,k) + … + lift(Xₙ,k)
L3|Child VDR triple|lift([V,D,R], k) = [kV, D, lift(R,k)] — D preserved, V and R scaled
# Properties: identity at k=1, negation at k=-1, multiplicative composition, distributes over remainder addition, preserves zero

# rebase_rules(id|type|condition|construction)
RB1|Closed rebase|VB/D is integer|[VB/D, B, 0]
RB2|Active rebase|VB/D not integer|N=V·B; Q=N÷D (integer div); S=N mod D; result = [Q, B, [S,D,0] + lift(R,B)]
RB3|Same-D rebase|B=D|Identity
# Preserves value equality, not structural equality; deterministic, finite, exact

# functional_remainder(id|aspect|detail)
FR1|Mechanism|Python function f(depth:int)→VDR; name string for inspectability; optional metadata
FR2|Resolution|resolve(obj, depth=n) expands fn(n), returns concrete VDR; required before projection
FR3|Newton-Raphson|make_newton_fn(name, step_fn); e.g. √2: x_{n+1} = (x_n + 2/x_n)/2; quadratic convergence, exact rational at every depth
FR4|Series|make_series_fn(name, term_fn); e.g. Leibniz π/4, Basel π²/6; every partial sum is exact rational
FR5|Semantics|Each depth is a complete exact value, not an approximation of a limit; no convergence criterion inside VDR

# linear_algebra(id|component|detail)
LA1|Vec|Ordered list of VDR objects; supports +, -, scalar mul, dot product, negation
LA2|Mat|List of equal-dimension row vectors; supports +, -, scalar mul, mat mul, transpose, mat-vec product
LA3|Determinant|Cofactor expansion (O(n!)); exact VDR arithmetic throughout
LA4|Inverse|Adjugate method: A⁻¹ = adj(A)/det(A); every cofactor exact; fails explicitly if det=0
LA5|Solve|Cramer's rule: xⱼ = det(A with col j replaced by b)/det(A); exact throughout
LA6|Rank|Gaussian elimination with exact VDR pivot operations
LA7|Hilbert demo|H×H⁻¹ = I exactly for all tested sizes; inv(inv(H))=H exactly; 40-operation matrix roundtrip zero drift

# discrete_calculus(id|operator|definition)
DC1|Discrete derivative|Dₕf(x) = (f(x+h) − f(x))/h; exact rational for any VDR h
DC2|Nth-order derivative|Repeated application of DC1
DC3|Left Riemann integral|Iₙ(f,a,b) = Σ f(a+kh)·h for k=0..n-1, h=(b-a)/n; exact rational
DC4|Trapezoidal integral|Average of left and right Riemann; O(1/n²) error vs O(1/n) for left Riemann
DC5|Finite difference table|Δⁿ of degree-n polynomial = n!·(leading coeff) exactly; Δⁿ⁺¹ = 0 exactly; no float noise floor
DC6|Relationship to standard calculus|Separate exact system; not numerical approximation of continuous calculus; discrete product/chain rules differ from continuous; each h gives complete exact answer

# boundaries(id|limitation|detail)
B1|No irrational closed triples|√2 is not a closed VDR rational; functional remainder produces exact rationals approaching it
B2|No standard calculus|Limits excluded by design; discrete derivative ≠ derivative; discrete integral ≠ integral
B3|Active division loses structure|Divisor projected to exact rational then inverted; divisor's remainder structure not preserved
B4|Cofactor expansion is O(n!)|Correct but impractical for large matrices; engineering optimization not mathematical limitation
B5|No eigenvalues|Roots of characteristic polynomial generally irrational for n≥3; no native irrational or complex type
B6|Does not replace reals|Exact finite alternative for domains where rational arithmetic and recursive rational refinement suffice

# axioms(id|axiom)
A1|VDR is ordered triple [V,D,R]; V∈ℤ, D∈ℤ\{0}, R∈valid remainder
A2|Exactly three slots; no recursion in V or D
A3|Remainder: atomic integer r, or composite r + X₁+…+Xₙ (each Xᵢ valid VDR, n finite)
A4|Nested VDR only in remainder slot
A5|Finite: depth, branching, total node count
A6|Exact as written; no approximation, limits, or infinite expansion
A7|Closed form [V,D,0] has scalar core V/D
A8|R≠0 means active; remainder is exact structure, not error
A9|Globally closed iff all remainders in entire tree are zero
A10|Remainder preserves integer exactness at every level
A11|Negative V, D, and atomic remainder all valid
A12|Validity does not require normalization
A13|Immediate child VDRs in remainder should have pairwise distinct denominators in normalized form
A14|Duplicate-denominator siblings may be merged by reduction
A15|Every valid object finitely inspectable
A16|Every primitive operation terminates on valid inputs
A17|Set of valid terminating VDR objects is countable
A18|Infinity is not valid VDR; may not appear as hidden completion logic
A19|Terminating VDR representation preferred over nonterminating conventional representation inside system
A20|Remainder interpreted as exact residual structure, not physical quantity
A21|Domain-specific interpretations may map VDR to physical semantics if foundational axioms preserved

# implementation(id|aspect|detail)
IM1|Language|Python 3.8+, no required external dependencies beyond stdlib
IM2|Core module|vdr.py — VDR, Remainder, normalization, equality, closed arithmetic, rebase, lift, projection
IM3|Active mul module|active_mul.py — active multiplication and division
IM4|Functional module|fn.py — FnRemainder, resolve, discrete calculus
IM5|LinAlg module|linalg.py — Vec, Mat, parser, JSON serialization, LaTeX export
IM6|Export module|export.py — lossy decimal/float export boundary
IM7|Optional dep|mpmath for arbitrary-precision decimal export; without it, manual long division from exact Fraction
IM8|Operators|+ - * / == != < <= > >= -x abs(x) float(x) hash(x)
IM9|Hash|Computed from normalized form; VDR works as dict keys and set members

# related_work(id|system|distinction_from_vdr)
RW1|Exact rational arithmetic (Fraction, GMP, FLINT)|VDR closed core isomorphic; contribution is remainder slot + functional extension
RW2|Computer algebra systems (Mathematica, Sage, SymPy)|CAS uses expression trees + rewrite rules; VDR uses fixed three-slot form with structural identity
RW3|Exact real arithmetic (iRRAM, ERA, RealLib)|Lazy intervals with demand-driven precision; VDR produces exact rationals per step, no intervals
RW4|Continued fractions|Not tree-structured, no general remainder slot, no functional extension
RW5|Posit/unum arithmetic|Better approximation per bit; VDR targets exact arithmetic, not better approximation
RW6|Finite differences theory|Established math; VDR provides exact computational substrate eliminating float noise floor

# claims(id|claim|type|depends)
CL1|Zero drift over arbitrary rational operation chains|demonstrated|P1,P2
CL2|Exact matrix inversion of ill-conditioned matrices where float fails|demonstrated|LA4,LA7
CL3|Recursive construction of irrationals where every expansion step is exact|demonstrated|FR3,FR4,FR5
CL4|Discrete calculus operators exact at every step size|demonstrated|DC1,DC3
CL5|Closed subclass arithmetically closed under four operations|structural|CA1,CA2,CA3,CA4
CL6|Normalization is deterministic, finite, idempotent|structural|C14
CL7|Lift composes multiplicatively: lift(lift(R,a),b) = lift(R,ab)|structural|C15
CL8|Rebase preserves value equality, not structural equality|structural|C16
CL9|Active division is v1 compromise — divisor remainder structure lost|limitation|AA5,B3
CL10|VDR does not replace real numbers or continuous calculus|boundary|B2,B6

# benchmark_data(id|test|parameter|result)
BD1|Return-to-origin|200 ops, start 1/7, step 1/13|VDR error=0; float error≈2.78e-16
BD2|Return-to-origin|2000 ops|VDR error=0; float error≈1e-15
BD3|Hilbert 3×3 residual|H×H⁻¹ max off-diag|VDR=0; float≈1e-16
BD4|Hilbert 4×4 residual|H×H⁻¹ max off-diag|VDR=0; float≈1e-13
BD5|Hilbert 5×5 residual|H×H⁻¹ max off-diag|VDR=0; float≈1e-9
BD6|Hilbert 4×4 det|exact|1/6048000
BD7|Hilbert 4×4 inverse|all entries|exact integers (16,-120,240,-140 / -120,1200,-2700,1680 / 240,-2700,6480,-4200 / -140,1680,-4200,2800)
BD8|Matrix roundtrip|40 matrix multiplications|exact recovery, zero drift
BD9|Newton √2 depth 7|fraction digits ~150|x²−2 = 1/(1.22×10⁹⁷)
BD10|Newton √2 convergence|correct digits double per step|quadratic: 0,1,3,6,12,24,48,>100
BD11|Discrete deriv x² at x=3 h=1/1000|exact|6001/1000
BD12|Left Riemann ∫x² [0,1] n=10|exact|57/200
BD13|Trapz ∫x² [0,1] n=100|exact|6667/20000
BD14|Δ³(x³) at integer points|exact|[6,6]
BD15|Δ⁴(x³) at integer points|exact|[0]

# relationships(from|rel|to)
C1|composes_of|C2,C3,C4
C4|takes_form|C7,C8,C9
C5|specialization_of|C1
C6|specialization_of|C1
C5|requires|C4 being zero
C6|requires|C4 being nonzero
C10|distinct_from|C11
C11|requires|C14
C12|enables|comparison with legacy systems
C13|constrains|C4 interpretation
C15|enables|C16
C17|component_of|RB2
CA1|implements|closed addition
CA2|implements|closed subtraction
CA3|implements|closed multiplication
CA4|implements|closed division
AA1|extends|CA1
AA2|extends|CA1
AA3|extends|CA3
AA4|extends|CA4
AA5|extends|CA4
AA5|exhibits|B3
FR1|specialization_of|C9
FR2|enables|C12 for functional remainders
FR3|instance_of|FR1
FR4|instance_of|FR1
FR5|distinct_from|convergence framework
LA3|uses|CA3,CA2
LA4|uses|LA3
LA5|uses|LA3
LA7|demonstrates|CL2
DC1|uses|CA1,CA2,CA4
DC3|uses|CA3,CA1
CL1|demonstrated_by|BD1,BD2
CL2|demonstrated_by|BD3,BD4,BD5,BD7
CL3|demonstrated_by|BD9,BD10
CL4|demonstrated_by|BD11,BD12,BD13
P1|grounds|C6,C13
P4|constrains|C1
P5|grounds|A6
B1|limits|FR3,FR4
B4|limits|LA3
B5|limits|LA2

# section_index(section|title|ids)
1|The Problem: Equality Lost|P1,P2,CL1
2|The Triple|C1,C2,C3,C4,C7,C8,P3,P4
3|Closed Objects and Rational Arithmetic|C5,CA1,CA2,CA3,CA4,CL5
4|Active Objects and the Remainder|C6,C13,P1
5|Equality and Normalization|C10,C11,C14,N1,N2,N3,N4,N5,N6,N7,CL6
6|Lift and Rebase|C15,C16,C17,L1,L2,L3,RB1,RB2,RB3,CL7,CL8
7|Active Arithmetic|AA1,AA2,AA3,AA4,AA5,AA6,CL9
8|Linear Algebra|LA1,LA2,LA3,LA4,LA5,LA6,LA7,CL2
9|Functions in the Remainder Slot|C9,FR1,FR2,FR3,FR4,FR5,CL3
10|Discrete Calculus|DC1,DC2,DC3,DC4,DC5,DC6,CL4
11|Boundaries and Honest Limitations|B1,B2,B3,B4,B5,B6,CL10
12|Implementation|IM1,IM2,IM3,IM4,IM5,IM6,IM7,IM8,IM9
13|Related Work|RW1,RW2,RW3,RW4,RW5,RW6
14|Conclusion|CL1,CL2,CL3,CL4
A|Axioms|A1-A21
B|Python API Reference|IM8 and method/function listings
C|Worked Examples|CA1-CA4,RB1,RB2,AA1,FR3,DC1,DC3
D|Benchmark Data|BD1-BD15
E|Normalization Examples|N1,N2
F|Closed Arithmetic Tables|CA1,CA2,CA3,CA4
G|Rebase Tables|RB1,RB2
H|Lift Tables|L1,L2,L3,CL7
I|Active Arithmetic Tables|AA1,AA2,AA3,AA4,AA5,AA6
J|Equality Tables|C10,C11
K|Structural Metrics|C18
L|Newton-Raphson Detail|FR3,BD9,BD10
M|Discrete Calculus Detail|DC1,DC2,DC3,DC4,DC5
N|Series Partial Sums|FR4
O|Hilbert Matrix Detail|LA7,BD3-BD7
P|Validity and Error|A1-A5
Q|JSON Serialization|IM5
R|LaTeX Export|IM5

# decode_legend
slots: V=value(integer) | D=denominator(nonzero integer) | R=remainder
remainder_forms: atomic(integer) | composite(base + children) | functional(callable)
states: closed(R=0) | active(R≠0)
equality: ≡s=structural | ≡n=normalized_value
projection: Π([V,D,R]) = (V + Π(R))/D
claim_types: demonstrated | structural | limitation | boundary
rel_types: composes_of|takes_form|specialization_of|requires|distinct_from|enables|constrains|component_of|implements|extends|exhibits|instance_of|uses|demonstrates|demonstrated_by|grounds|limits
category_values: core|slot|state|remainder-form|equality|operation|semantics|procedure|metric|construction
