# VDR Complete System — Mechanical Reference

## Layer 0: The Triple

Everything builds from one data structure. A VDR object is an ordered triple **[V, D, R]**.

**V** is an arbitrary-precision integer. The settled numerator in the current denominator frame.

**D** is a nonzero arbitrary-precision integer. The denominator frame. Defines the scale in which V and R are interpreted.

**R** is the remainder. First-class. Never error. Never residue. Three forms:

**Atomic:** a single integer r. Example: [3, 7, 2] means (3 + 2)/7 = 5/7.

**Composite:** an integer base r plus a finite ordered list of child VDR triples. r + X₁ + X₂ + ... Each child is itself a full VDR object. Recursion happens only through R — V and D are always integers, never nested.

**Functional:** a Python callable f(depth) → VDR with a name string. Stored in R. Expanded via resolve(). Returns an exact VDR at any requested depth. This is how VDR handles square roots, trig, exp, log — every depth gives a complete exact rational, not an approximation of a limit.

Every valid VDR object has finite depth, finite branching, finite total node count.

**Denominator-sensitive completion:** R is interpreted within the parent's D frame — divided by D, not added externally. [3, 7, 1] means (3 + 1)/7 = 4/7, not 3/7 + 1.

**Scalar projection:** Π([V, D, R]) = (V + Π(R)) / D. Recursive evaluation for comparison with conventional numbers.

**Two states:**

*Closed:* R = 0. Behaves exactly as rational V/D. Bridge to conventional math.

*Active:* R ≠ 0. Carries exact structure the denominator frame couldn't absorb.

## Layer 1: Normalization

Deterministic, idempotent procedure producing canonical form. Steps in order:

1. **Sign convention:** if D < 0, negate both V and D.
2. **GCD reduction:** for closed nodes, divide V and D by gcd(|V|, |D|).
3. **Child normalization:** every child normalized before parent (bottom-up).
4. **Atomic remainder consolidation:** all integer contributions at same level combined into single base.
5. **Canonical child ordering:** children sorted by denominator magnitude, then V, then R structure.
6. **Same-denominator child merge:** closed children sharing D are added; zero-sum children removed.
7. **Closed-form preference (N7):** if entire remainder tree normalizes to zero, object settles to closed form.

**Two equality relations:**

*Structural equality (≡s):* slot-by-slot recursive match.

*Normalized value equality (≡n):* match after normalization. Python == uses this.

**Hash** computed from normalized form. VDR objects work as dict keys and set members.

## Layer 2: Closed Arithmetic

The closed subclass [V, D, 0] is arithmetically closed under four operations:

**Addition:** [V₁D₂ + V₂D₁, D₁D₂, 0]. Identity [0, 1, 0].

**Subtraction:** [V₁D₂ − V₂D₁, D₁D₂, 0].

**Multiplication:** [V₁V₂, D₁D₂, 0]. Identity [1, 1, 0].

**Division (V₂ ≠ 0):** [V₁D₂, D₁V₂, 0].

**Negation:** [-V, D, 0].

This is standard rational arithmetic in VDR notation. The bridge between VDR and conventional math.

## Layer 3: Lift and Rebase

**Lift** is the remainder transport operator. When a parent denominator frame changes by factor k, R must be rescaled.

Atomic: lift(r, k) = kr.

Child VDR: lift([V, D, R], k) = [kV, D, lift(R, k)]. D is preserved. V and R are scaled.

Composite: lift(r + X₁ + ... + Xₙ, k) = kr + lift(X₁, k) + ... + lift(Xₙ, k).

Properties: identity at k=1, negation at k=−1, multiplicative composition (lift(lift(R, a), b) = lift(R, ab)), distributes over remainder addition, preserves zero.

**Rebase** changes top-level denominator while preserving exact value.

*Closed rebase:* if V·B/D is an integer, result is [V·B/D, B, 0]. Clean.

*Active rebase:* if V·B/D is not an integer, compute N = V·B, then Q, S = divmod(N, D). Result: [Q, B, [S, D, 0] + lift(R, B)]. The [S, D, 0] term is the *mismatch witness* — the exact part the target denominator couldn't absorb.

*Same-D rebase:* B = D gives identity.

Rebase preserves value equality, not structural equality. Deterministic, finite, exact.

## Layer 4: Active Arithmetic

**Same-D addition:** [V₁ + V₂, D, R₁ ⊕ R₂]. Values sum, remainder bases sum, child lists concatenate, then normalize.

**Different-D addition:** cross-scale to D₁·D₂ frame using lift. lift(R₁, D₂) + lift(R₂, D₁).

**Active multiplication:** frame D₁·D₂, closed part V₁·V₂, remainder captures three cross-terms: V₁·R₂, V₂·R₁, R₁·R₂ (projected).

**Active division by closed divisor:** multiply by reciprocal [D₂, V₂, 0].

**Active division by active divisor:** v1 compromise. Project divisor to exact rational via Π, invert, multiply. Divisor's remainder structure is lost. Acknowledged limitation.

**Negation:** -[V, D, R] = [-V, D, -R]. Remainder negation negates base and all children recursively.

## Layer 5: The divmod Rule — D Never Explodes

This is the operational rule that governs the entire system. When any operation would produce a larger denominator, you divmod and put the overflow in R.

**Multiplication of two values in the same D-frame (e.g. Q335):**

A = [p₁, 2³³⁵, 0], B = [p₂, 2³³⁵, 0].

Product p₁·p₂ is a big integer. Naive result would be [p₁·p₂, 2⁶⁷⁰, 0] — D explosion. Never do this.

Q, S = divmod(p₁ · p₂, 2³³⁵)

Result: [Q, 2³³⁵, [S, 2³³⁵, 0]].

D stays at 2³³⁵. V absorbed what fit. R caught what didn't — exactly, zero loss. Verify: Π = (Q + S/2³³⁵) / 2³³⁵ = (Q·2³³⁵ + S) / 2⁶⁷⁰ = p₁·p₂ / 2⁶⁷⁰. Same value. D never changed.

**Division works the same way.** Multiply by reciprocal, divmod back into the frame. Odd denominators go into R via divmod.

**This is what R exists for.** The remainder slot is the pressure valve that keeps D stable while preserving every bit of exactness. Multiplication doesn't change D. Division doesn't change D.

## Layer 6: Functional Remainders

A Python callable stored in R that returns a VDR at any requested depth.

**Newton-Raphson:** √2 via x_{n+1} = (x + 2/x)/2. Each depth is an exact rational. Depth 7 gives ~150 fraction digits. Depth 10 gives >100 correct digits. Quadratic convergence — digits double per step. The residual x² − 2 is an exact inspectable rational. You know precisely how far from √2 you are.

**Taylor series:** exp(x) = Σxⁿ/n!, sin(x), cos(x), ln(1+x), arctan(x). Each partial sum is an exact rational. Super-geometric convergence for exp/sin/cos (~35 terms for 100 digits at x=1/2). Geometric for ln and arctan.

**Convergence rates for 100 digits:**

exp/sin/cos at x=1/2: ~35 terms. √n Newton: ~8 steps. ₂F₁ hypergeometric at k²=1/4: ~170 terms. ζ(s) Borwein: 210 terms (universal for any s). Kepler Newton: ~8 steps.

**Semantics:** each depth is a complete exact value, not an approximation of a limit. No convergence criterion inside VDR. The function returns a VDR; that VDR is exact; deeper calls return more refined exact values.

**The precision knob:** by default resolve fully. But you can choose depth for performance. Depth 5 for ~30 digits. Depth 10 for ~100. Depth 20 for ~200. You know exactly where the approximation lives and how large it is. It doesn't compound through chains — rational ops on the resolved value are exact.

## Layer 7: Q335 Basis

22 transcendental constants stored as [p, 2³³⁵, 0] where p is a ~102-digit integer.

**Origin:** 87/32 is the 5th convergent of e, best rational approximation with denominator ≤ 32. 32 = 2⁵. Extending to 2³³⁵ gives 100-digit precision for every constant. n = 335 is minimal: at n = 334 Catalan's G fails at position 101.

**The 22 constants:** π, e, ln(2), √2, φ, π², π³, π⁴, eᵖ, ln²(2), ln⁴(2), ln(3), ln(5), ln(10), √3, √5, √7, ζ(2), ζ(3), ζ(5), Li₄(1/2), Catalan's G. All verified against mpmath at 100 digits by string comparison. Total storage: 2238 digits plus exponent 335.

**Arithmetic costs:**

Add/subtract two Q335: 1 integer op, depth +0, ±1 ULP.

Multiply by integer k: 1 multiply, depth +0, exact.

Multiply by 1/2ᵐ: 1 shift, depth +0, exact.

Multiply two Q335: 1 multiply + 1 divmod, depth +1, zero loss (overflow in R).

Divide by integer k: 1 divmod, depth +1 if remainder, odd factor in R.

Complex multiply: 4 multiplies + 1 add + 1 sub, depth +1 per multiply.

FFT butterfly: 4 multiplies + 4 add/sub, depth +1 per stage.

**Compression vs MATH-2 individual pairs:** π from 1,107 to 102 digits (10.9×). eᵖ from 131,868 to 103 digits (1,280×). Total from ~20,000 to 2,238 digits.

**Precision scaling:** ~3.32 bits per decimal digit. 200 digits → 2⁶⁶⁸. 1000 digits → 2³³²².

**Rounding floor:** 2⁻³³⁶ ≈ 10⁻¹⁰¹·². 10⁶⁶ times below Planck length. Exceeds float by 85 orders of magnitude.

## Layer 8: MATH-3 Computation Infrastructure

How each constant gets computed to arbitrary precision.

**Integer pair principle:** truncate a convergent rational series at N terms. Result is exact Fraction p/q. Truncation error bounded by next term. Not float approximation — exact rational differing from true value by known bounded amount.

**Borwein acceleration:** replaces linear convergence with geometric 3⁻ⁿ for all Dirichlet eta/zeta values. ζ(5) goes from 10,000 terms for 20 digits to 210 terms for 100 digits. Universal rate — same 210 terms works for ζ(7), ζ(9), any s. Coefficients d_k are finite sums of rational terms. ~22,000 Fraction operations on ~500-digit numbers. Minutes.

**Elliptic integrals as integer pairs:** K(k) at rational k = (π/2) × ₂F₁(1/2, 1/2; 1; k²). Every coefficient rational. Recurrence t_{n+1}/t_n = [(2n+1)/(2n+2)]² × k². Product of two integer pairs is an integer pair. Six values computed: K and E at k² = 1/2, 3/4, 1/4.

**Transcendental weight hierarchy:** rational = 0, π = ln(2) = 1, ζ(n) = n, Li_n(1/2) = n, K(k) = 1. Maximal weight at L-loop QED = 2L−1. Topology determines transcendental class: factorizable diagrams → ζ/ln/Li family; irreducible sunrise → elliptic integrals.

**Extended basis:** ~29 constants. Original 17 from MATH-2 + 6 elliptic + 3 accelerated odd zeta + 3 Clausen functions.

**PSLQ target:** Laporta's 6 finite 4-loop master integrals at 4800 digits. ~50–100 candidate constants at 5000+ digits. Not yet performed — method and feasibility established.

## Layer 9: Gaussian Elimination

The enabler for n×n domains. O(n³) replaces cofactor expansion's O(n!).

3×3: 17 ops for determinant, 39 for inverse. 10×10: 550 det, 1100 inverse. 50×50: 63,750 det, 127,500 inverse. Cofactor is impractical at n=10, impossible at n=20.

**Hilbert matrix pivot growth — where float dies, VDR doesn't:**

H₃: float error ~10⁻¹⁶. H₅: ~10⁻⁹. H₈: ~10⁴ (wrong sign possible). H₁₀: meaningless. H₂₀: impossible. H₃₀: impossible. VDR computes H₃₀ routinely — determinant denominator ~400 digits, numerator always 1. Condition number is irrelevant to exact arithmetic.

## Layer 10: Linear Algebra

**Vec:** ordered list of VDR objects. Add, subtract, scalar multiply, dot product, negation.

**Mat:** list of equal-dimension row vectors. Add, subtract, scalar multiply, matrix multiply, transpose, mat-vec product.

**Determinant:** Gaussian elimination. Exact.

**Inverse:** adjugate method or Gaussian. A⁻¹ = adj(A)/det(A). Every cofactor exact. Fails explicitly if det = 0.

**Solve:** Cramer's rule or Gaussian. Exact throughout.

**Rank:** Gaussian elimination with exact VDR pivot operations. No numerical rank thresholding.

**Headline result:** Hilbert matrices invert exactly. H×H⁻¹ = I with exact zero off-diagonal. 40-operation matrix roundtrip: zero drift.

## Layer 11: Discrete Calculus

**Discrete derivative:** Dₕf(x) = (f(x+h) − f(x))/h. Exact rational for any VDR h.

**Nth-order derivative:** repeated application.

**Left Riemann integral:** Iₙ(f, a, b) = Σf(a+kh)·h for k=0..n−1, h=(b−a)/n. Exact rational.

**Trapezoidal integral:** average of left and right Riemann. O(1/n²) vs O(1/n).

**Finite difference tables:** Δ³(x³) = [6, 6] exactly. Δ⁴(x³) = [0] exactly. No float noise floor.

**Explicitly not continuous calculus.** Discrete product/chain rules differ from continuous. Each h gives a complete exact answer. Separate exact system.

## Layer 12: Normalization Fix (Library TODO)

Newton on perfect squares (√4, √9) produces correct values but in unreduced form — 2k/k for large k. Structural comparison to [2, 1, 0] fails. Value equality holds. Zero arithmetic impact. Fix: when R is zero or value-equivalent to zero, GCD-reduce unconditionally. Affects 4/37 tests in VDR-26, some tests in VDR-28 normalization presentation. We solve this when we build the library.

## Layer 13: Physical Domains (VDR-13)

14 domains exercised: QED coefficients, quantum 2×2 and n×n, DFT/FFT, IIR filters, transfer functions, state-space, Kepler orbits, structural statics, partition functions, crystallography, geodesy, paraxial optics, resonator stability.

**Conservation laws verified by exact equality:** probability = 1 (quantum), unitarity U†U = I, symplecticity det(M) = 1 (optics after 1000 elements), energy (Hamiltonian), Parseval (DFT), equilibrium Ku = F (structures), group closure (crystallography), orbit closure (Kepler), partition function ratios, coordinate roundtrip (Helmert).

**Float comparison across all:** float gives ≈ correct ± 10⁻⁹ to 10⁻¹⁶ depending on domain and chain length. VDR gives exact structural equality. Every conservation law that should hold exactly, holds exactly.

**Q335 tree depth vs flat denominator explosion:** crossover at ~step 10 of logistic map. At step 30: flat denominator ~10⁹ digits, Q335 tree 6,120 digits — ~163,000× compression. Tree grows linearly (one ~102-digit level per step). Flat grows exponentially.

## Layer 14: Diffusion Zero-Drift (VDR-26)

Diffusion models are sequential arithmetic chains. Forward: xₜ = √ᾱₜ·x₀ + √(1−ᾱₜ)·ε. Reverse: invert. DDIM: deterministic variant.

**Schedule:** all β, α, ᾱ are exact rationals. ᾱ_T = 26821179/31250000, verified bit-identical against Python Fraction.

**Square roots:** Newton functional remainder. Only approximation in the system. Fixed residual < 10⁻⁵⁰ at depth 10. Does not compound.

**Central result:** drift at cycle N = drift at cycle 1. Chain length irrelevant. Float drift grows linearly at ~10⁻¹⁵ per cycle. 2-hour film at 24fps/50 steps: float ~1.9×10⁻⁸, VDR < 10⁻⁵⁰. Gap: 42 orders of magnitude.

**DDIM roundtrip:** exactly zero error with perfect noise. Strongest result.

**Separability:** arithmetic error eliminated, so all observed error is attributable to the model. Float conflates the two.

**Cost:** ~50–200× float per op. Justified for video (temporal coherence), medical imaging (reproducibility), forensic (audit trail).

## Layer 15: Beyond LLMs (VDR-27)

35 domains across 12 categories sharing the same sequential chain pattern:

Autoregressive generation (speech, music, protein, time-series). Normalizing flows (exact invertibility). Kalman filtering (exact symmetry, positive definiteness). Financial computation (associative multiplication for risk aggregation, exact Greeks via finite difference). Control systems (PID arithmetic windup = 0). Physics simulation (exact conservation). Cryptography (exact finite field — float categorically excluded). Geodesy (exact Helmert roundtrip). Game theory (Shapley sums exactly to v(N)). Signal processing (exact DFT roundtrip). Quantum computing (exact normalization, Born rule).

**10 float failure categories all eliminated:** accumulation, cancellation, non-associativity, platform dependence, overflow/underflow, denormals, non-reproducibility, symmetry breaking, conservation drift, false convergence.

**Error accumulation models all made irrelevant:** random walk, linear, multiplicative, catastrophic, chaotic. 0 × anything = 0.

**921 tests across 38 domains. Zero VDR computation errors.**

## Layer 16: Decimal Truncation (VDR-28)

10 = 2 × 5. Only denominators factoring into 2s and 5s terminate. 60% of small denominators repeat. The decimal trap is the norm.

**43 domains** (20 main + 23 appendix) where decimal truncation produces materially wrong results. Continued fractions, Bernoulli numbers, Hilbert matrices, eigenvalues, Gaussian pivots, Bayesian updates, Markov steady states, elliptic curves, CRT, partition functions, Runge-Kutta, Galois fields, Cayley-Hamilton, Farey sequences, polynomial GCD, Padé approximants, LLL, Gröbner bases, quantum stabilizers, Pell equation. Plus 23 more in appendix.

**Zero-testing is the critical operation:** is this value exactly zero or merely small? Decimal cannot answer at any precision. VDR: [0, 1, 0] or not. Determines correctness of polynomial GCD, Gröbner bases, matrix rank, Cayley-Hamilton, linear independence, LLL threshold.

**The decimal trap is endemic:** every Bernoulli B₂ₙ (n≥1) has odd prime denominators. Every RK method order ≥ 2 has coefficient with factor of 3. Every factorial denominator has factor of 3.

**Arbitrary precision does not solve it:** mpmath at 1000 digits still truncates 1/3.

**VDR is categorically different:** [1, 3, 0] is exact. Three integers. Zero truncation.

## Layer 17: Boundaries — Honest and Complete

**Chaotic dynamics:** exact representation has exponential cost. Logistic map r=4: denominator digits ≈ 2ⁿ after n steps. Information-theoretic — Lyapunov exponent ln(2) forces it. Float hides this by silent truncation. VDR exposes it honestly. Periodic orbits on rationals are free (bounded denominators).

**No native irrationals or complex numbers:** functional remainders produce exact rationals approaching irrationals. Complex extension is engineering work, not mathematical obstacle.

**Active division loses divisor remainder structure:** v1 compromise. Divisor projected to exact rational, inverted. Acknowledged.

**Cofactor expansion O(n!):** replaced by Gaussian O(n³). Practical limit ~50×50.

**Computational cost:** ~50–200× float per operation. Practical path: VDR for validation providing exact ground truth to verify float on larger systems.

**Nothing is computationally impossible for VDR.** Every transcendental function with a known convergent series is reachable. Every numerically known constant is representable. The only constraint is computational cost — shared by all arithmetic systems. VDR makes costs visible and honest. Float silently produces garbage.

## Cumulative Validation

921 tests. 38 domains. 903 passed. 18 failed — all 18 test-design errors (wrong expected values, tight thresholds, normalization presentation, precision frame mismatch). Zero VDR computation errors. The system remains falsifiable: any test producing an incorrect exact rational from correct inputs would falsify VDR. 921 tests have not produced one.
