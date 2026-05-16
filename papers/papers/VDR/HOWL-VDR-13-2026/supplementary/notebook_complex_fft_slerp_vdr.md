# VDR Notebook: Denominator Preservation, Complex Pairs, and Integer-Domain Transforms

## 1. The Q335 Multiplication Problem

The current papers handle multiplication of two Q335 constants like this:

```
[p₁, 2³³⁵, 0] × [p₂, 2³³⁵, 0] = [p₁·p₂, 2⁶⁷⁰, 0]
```

Then they project back to 2³³⁵ by right-shifting 335 bits and rounding. This is the one place in all three papers where VDR voluntarily discards information. It's a concession to scalar thinking — the assumption that the result must live in the same flat frame as the inputs.

But VDR already has the mechanism to avoid this. The remainder slot exists precisely to carry what the denominator frame cannot absorb.

Perform the integer division of p₁·p₂ by 2³³⁵:

```
p₁·p₂ = q·2³³⁵ + s,  where 0 ≤ s < 2³³⁵
```

Then the exact result, staying in the Q335 frame, is:

```
[q, 2³³⁵, [s, 2³³⁵, 0]]
```

Verify by scalar projection: Π = (q + s/2³³⁵) / 2³³⁵ = (q·2³³⁵ + s) / 2⁶⁷⁰ = p₁·p₂ / 2⁶⁷⁰. Identical to the closed form. Zero information lost. The top-level denominator stays 2³³⁵. The remainder is itself a Q335 closed object carrying the lower bits.

This generalizes. If you multiply three Q335 values, the product p₁·p₂·p₃ lives over 2¹⁰⁰⁵. Divide repeatedly by 2³³⁵:

```
p₁·p₂·p₃ = q₁·2³³⁵ + s₁  (first layer)
s₁ = ... (already a Q335-scale integer, nests as remainder)
```

The result is a VDR tree of depth proportional to the number of multiplications, each level a Q335 object. The denominator never changes. The tree grows instead. Depth is the cost — not precision loss.


## 2. Q335 Division via Remainder Nesting

Division reveals the pattern even more clearly.

```
[p₁, 2³³⁵, 0] / [p₂, 2³³⁵, 0]
```

By closed arithmetic: [p₁·2³³⁵, 2³³⁵·p₂, 0] = [p₁·2³³⁵, p₂·2³³⁵, 0]. The 2³³⁵ cancels from GCD reduction, leaving [p₁, p₂, 0]. But p₂ is a ~102-digit integer with odd factors. We've left the Q335 frame entirely.

Instead, perform integer division of p₁ by p₂:

```
p₁ = q·p₂ + s,  where 0 ≤ s < p₂
```

This gives [q, 1, [s, p₂, 0]]. Now rebase the whole object into the 2³³⁵ frame:

```
[q·2³³⁵, 2³³⁵, [s, p₂, 0] lifted by 2³³⁵]
```

The remainder [s, p₂, 0] carries the exact residual of the division. The top-level frame stays Q335. The odd denominator p₂ is confined to the remainder slot — it doesn't infect the working frame.

This is the VDR native way to handle division. The papers' AA5 compromise (project divisor to scalar, lose structure) is unnecessary when the divisor is a Q335 constant, because the structure being "lost" is just the lower-precision bits, and those are exactly what R preserves.


## 3. Denominator Growth as a General Problem

Denominator growth isn't specific to Q335 or to chaos. It's the fundamental cost of exact rational arithmetic. Every multiplication of two rationals a/b × c/d produces a denominator b·d. After n multiplications starting from denominators of size D, the denominator is potentially D^(2^n) in the worst case (repeated squaring) or D^n in the chain case.

The conventional response is: reduce by GCD at every step. This helps when factors cancel (and in many practical cases they do), but it cannot help when they don't — which is exactly the chaotic dynamics case where denominators grow exponentially because no cancellation occurs.

VDR's remainder nesting offers a different response: don't let the denominator grow. Pick a working frame D (such as 2³³⁵). Every operation that would push the result out of that frame instead deposits the overflow into R. The denominator stays fixed. The tree grows.

This transforms the problem from "denominators explode" to "trees deepen." The information is the same — you cannot avoid representing the information content of the exact result. But the representation changes from a single enormous fraction to a tree of bounded-denominator nodes.

The key question is whether this tree representation enables operations that the flat fraction does not. For linear operations (addition, subtraction, scalar multiplication), the answer is yes — same-frame addition is just integer addition at the top level, with remainder combination that stays within the frame. For nonlinear operations (multiplication of two active objects, comparison), the tree must be traversed, and the cost reappears.

But the cost reappears as tree depth, which can be managed — pruned, lazily evaluated, or bounded by precision policy. A 200-digit flat denominator offers no such handles.


## 4. Complex Numbers as VDR Pairs

A complex number z = a + bi is two real components with the algebraic rule i² = -1. There is no mystery to encode. A VDR complex number is an ordered pair of VDR objects:

```
z = (A, B)   where A = Re(z), B = Im(z), both VDR triples
```

This is not a new type. It's a convention on a pair of existing objects. The arithmetic follows directly:

**Addition:** (A₁, B₁) + (A₂, B₂) = (A₁ + A₂, B₁ + B₂). Two VDR additions.

**Multiplication:** (A₁, B₁) · (A₂, B₂) = (A₁A₂ - B₁B₂, A₁B₂ + A₂B₁). Four VDR multiplications, one subtraction, one addition.

**Conjugate:** (A, B)* = (A, -B). Negate B using AA6 (remainder negation).

**Modulus squared:** |z|² = A² + B². Two VDR multiplications and one addition. Result is a single VDR object (real).

**Inverse:** z⁻¹ = z*/|z|². Conjugate divided by modulus squared. Division of each component by the real value |z|².

All of these are compositions of existing VDR operations. If A and B are Q335 objects, the products stay in the Q335 frame via remainder nesting (Section 1). If they're general VDR active objects, the active arithmetic rules from VDR-1 apply unchanged.

The reason the VDR-3 papers list complex numbers as "unimplemented" and "engineering work" is exactly this: there's no mathematical obstacle, just the need to define the pair convention and implement the four operations as compositions. It doesn't block anything in principle — it blocks things in the codebase.


## 5. Roots of Unity and the Twiddle Factor Table

The DFT of length N requires the Nth roots of unity: ω_N^k = e^(-2πik/N) = cos(2πk/N) - i·sin(2πk/N).

For each k and N, cos(2πk/N) and sin(2πk/N) are specific real numbers. Many are algebraic at small N:

```
N=2: ω = -1                    → (-1, 0) exact closed VDR
N=4: ω = -i, ω² = -1, ω³ = i  → all components in {-1, 0, 1}
N=8: involves ±1/√2            → Q335 projection or functional remainder
```

For general N, the trig values are computed via their Taylor series (convergent, rational coefficients) and projected to Q335:

```
cos(2πk/N) = Σ (-1)^n (2πk/N)^(2n) / (2n)!
```

Each partial sum is a rational number (since 2πk/N is represented as a Q335 value, and the series coefficients are rational). At depth d, you have an exact rational approximation. Project to Q335 and you have a twiddle factor pair (cos component, sin component) as two Q335 integers.

For a length-N DFT, you need N/2 distinct twiddle factors (by symmetry). Each is a pair of Q335 integers. Total storage: N integers of ~102 digits each. For N = 1024, that's about 105K digits — trivial.

The twiddle table is computed once. After that, the entire FFT is integer arithmetic in the Q335 frame.


## 6. FFT as Integer Butterfly Operations

The radix-2 FFT butterfly is:

```
X_even = A + W·B
X_odd  = A - W·B
```

where A and B are complex values (VDR pairs) and W is a twiddle factor (VDR pair).

With VDR complex multiplication from Section 4:

```
W·B = (W_re · B_re - W_im · B_im,  W_re · B_im + W_im · B_re)
```

Four Q335 integer multiplications, each producing a ~204-digit product, integer-divided by 2³³⁵ with remainder nested. Then two Q335 integer additions for the even output, two subtractions for the odd output.

Per butterfly: 4 multiplications + 4 additions/subtractions on each of real and imaginary parts. All integer operations. All in the Q335 frame. Remainders nest at each multiplication, adding one tree level per butterfly stage.

An N-point FFT has log₂(N) stages, each with N/2 butterflies. For N = 1024: 10 stages × 512 butterflies = 5120 butterflies. Each butterfly's multiplications add at most one remainder level. After 10 stages, the deepest remainder tree is 10 levels — each node a Q335 integer. The top-level denominator is still 2³³⁵.

If you only need the top-level precision (100 digits), you can prune the tree at any point. If you need full exactness, the tree is there. This is the precision knob that float FFT lacks — float FFT silently accumulates rounding at every butterfly, with no mechanism to recover what was lost.


## 7. Slerp via Functional Remainders

Spherical linear interpolation between two unit quaternions q₀ and q₁ at parameter t:

```
slerp(q₀, q₁, t) = sin((1-t)θ)/sin(θ) · q₀ + sin(tθ)/sin(θ) · q₁
```

where θ = arccos(q₀ · q₁).

A quaternion is four real components — four VDR objects. The dot product q₀ · q₁ is a sum of four VDR multiplications: a single VDR value.

arccos is computed as a functional remainder. The Taylor series for arccos(x) around x = 0 has rational coefficients (involving central binomial coefficients divided by powers of 4). At depth d, you get an exact rational. For arccos near 1 (small angles), use the identity arccos(x) = 2·arcsin(√((1-x)/2)) and the arcsin series instead, which converges faster there.

sin of a rational argument: Taylor series, rational coefficients, exact rational at every depth. sin(tθ) where t is rational and θ is a functional remainder: compose the two series. Each evaluation depth gives an exact rational for the sine.

The division sin(tθ)/sin(θ) is a ratio of two functional remainders evaluated at the same depth. At any given depth, both are exact rationals, so the division is exact rational division.

The entire slerp, at any evaluation depth, is four rational linear combinations of the input quaternion components. The trig functions never leave the VDR framework — they exist as functional remainders that produce exact rationals on demand.

For an LLM system using rotary position embeddings (RoPE), slerp between position encodings is this same structure. The rotation angles are rational multiples of a base frequency, the sines and cosines are Q335 projections or functional remainders, and the interpolation parameter t is rational. The entire rotation stays in integer arithmetic.


## 8. Modular Structure and Remainder Nesting

VDR's remainder slot is structurally a modular residue system. When you compute `p₁·p₂ = q·2³³⁵ + s`, the value q is the quotient mod 2³³⁵ and s is the residue. The VDR triple `[q, 2³³⁵, [s, 2³³⁵, 0]]` is literally the quotient-remainder decomposition, nested into the recursive structure.

This connects to several things simultaneously:

**Modular arithmetic proper.** GF(p) operations in coding theory (VDR-3, Gym 18) are already remainder operations. Hamming codes, CRT, RSA — all operate on integer residues mod some modulus. VDR performs these natively because its core operations are integer operations. The Q335 frame with remainder nesting is a weighted positional system in base 2³³⁵, where each "digit" is a Q335 integer and the "position" is the remainder depth.

**Continued fractions.** A continued fraction [a₀; a₁, a₂, ...] is a nested quotient-remainder structure: x = a₀ + 1/(a₁ + 1/(a₂ + ...)). This is a VDR tree where each level performs a division and nests the residual. The VDR-2 gym on continued fractions (Gym 03) already demonstrated exact roundtrip conversion. The connection isn't metaphorical — CF representation is a specific case of VDR remainder nesting where each denominator frame is determined by the CF coefficient.

**Chinese Remainder Theorem.** CRT reconstructs a value from its residues mod coprime moduli. A VDR object with composite remainder children at different denominators is carrying the same information — the value decomposed across multiple denominator frames. Normalization rule N6 (same-denominator child merge) is the analogue of combining residues within a single modulus. The pairwise-distinct-denominator axiom A13 is the structural reflection of CRT's coprimality requirement.

**Residue number systems.** In hardware, residue number systems represent integers as tuples of residues mod chosen moduli, enabling parallel addition and multiplication. VDR's composite remainder with multiple children at different denominators is the exact same idea lifted to rational arithmetic — each child carries the value's projection onto a different denominator frame, and same-D children merge.

The pattern is: modular arithmetic, continued fractions, CRT, RNS, and VDR remainder nesting are all manifestations of the same structural principle — decompose a value into what a given frame absorbs and what it doesn't, then recurse on the residual. VDR's contribution is making this recursive and carrying it as a first-class part of the value, rather than discarding it (float) or requiring reconstruction (CRT/RNS).


## 9. Putting It Together: What This Solves

Of the four open problems:

**Complex number extension.** Not a mathematical problem. VDR complex numbers are pairs of VDR objects with four composed operations. The FFT follows from complex arithmetic plus a precomputed twiddle table of Q335 pairs. DFT, eigenvalues (for 2×2 and cases with rational eigenvalues), and complex roots of polynomials all become available. The only implementation work is defining the pair type and the four operations.

**Gaussian elimination.** Orthogonal to this notebook. It's a straightforward implementation of exact rational row reduction using VDR arithmetic. The pivot operations are VDR divisions (which work), the row operations are VDR linear combinations (which work). The obstacle is engineering effort, not design. Would bring matrix operations from O(n!) to O(n³).

**Max-flow BFS.** A bug fix. Not discussed here.

**Denominator growth.** This is the one this notebook directly addresses. The Q335 remainder nesting pattern — keep the working frame fixed, nest overflow into R — transforms denominator explosion into tree deepening. For the chaotic dynamics case (logistic map, denominator growing as 2^n digits), each step adds one remainder level instead of doubling the denominator size. The information content is the same, but the structure is manageable: prunable, lazily evaluable, and bounded by precision policy.

The untested question from VDR-2 FW2 — "functional remainder representing n logistic steps without materializing intermediate fractions" — becomes concrete in this framework. A functional remainder f(depth) could compute the nth iterate of the logistic map at a given precision depth, producing a Q335 object at each depth without building the full remainder tree. The tree exists implicitly in the function. Each call returns an exact rational. The denominator never grows beyond 2³³⁵.

This doesn't make chaos cheap. The information-theoretic cost is real. But it makes chaos *representable* within the VDR framework without abandoning the fixed-frame discipline, and it gives the precision knob that lets you choose how much of that cost to pay.

---

# VDR Q335 Remainder Nesting Gym

## Conventions

D = 2³³⁵ throughout. All values are `[p, D, 0]` or `[q, D, [s, D, 0]]` with possible deeper nesting. `p(x)` means the Q335 numerator for constant x. Remainder is never residual — it is first-class structure.


## G01: Multiplication Preserving Frame

**Problem:** Compute π·e in Q335 without leaving the frame.

```
p(π)·p(e) = P  (a ~204-digit integer)
P = q·D + s,  0 ≤ s < D
Result: [q, D, [s, D, 0]]
```

Verify: Π = (q + s/D) / D = (qD + s) / D² = P / D² = p(π)·p(e) / D². Exact.

**Problem:** Compute π²·ln(2).

Option A — use precomputed p(π²):
```
p(π²)·p(ln2) = P₁ = q₁·D + s₁
Result: [q₁, D, [s₁, D, 0]]
```

Option B — compute from p(π):
```
p(π)² = P₀ = q₀·D + s₀        → π² as [q₀, D, [s₀, D, 0]]
```
Now multiply this active object by [p(ln2), D, 0]. Top-level V contribution: q₀·p(ln2). Remainder contribution: s₀·p(ln2)/D. Each multiplication nests one level. Two multiplications, two levels max.

Option A is cheaper. Precomputed powers exist for this reason.


## G02: Division Preserving Frame

**Problem:** Compute π/e.

```
p(π) = q·p(e) + s,  0 ≤ s < p(e)
π/e = [q, 1, [s, p(e), 0]]
```

Rebase to D-frame:
```
[q·D, D, rebase([s, p(e), 0], D)]
```

The remainder [s, p(e), 0] carries the exact fractional part. p(e) is odd (it's a ~102-digit integer from the projection), so it sits in R with its odd denominator confined there. The working frame stays D = 2³³⁵.

**Problem:** Compute ζ(3)/π².

```
p(ζ3) = q·p(π²) + s
Result top: [q, 1, [s, p(π²), 0]]
Rebase to D: [q·D, D, [s·D, p(π²), 0]]
```

Scalar check: Π = (qD + sD/p(π²)) / D = q + s/p(π²) = (q·p(π²) + s)/p(π²) = p(ζ3)/p(π²). Correct.


## G03: Chain of Multiplications

**Problem:** Compute π⁴ from scratch as π·π·π·π, tracking remainder depth.

```
Step 1: p(π)² = q₁·D + s₁        → [q₁, D, [s₁, D, 0]]           depth 1
Step 2: need to square the result
```

Squaring [q₁, D, R₁] where R₁ = [s₁, D, 0]:

Active multiplication (AA3): frame D², closed numerator q₁², three cross-terms in remainder. But we want to stay in frame D, not D².

Alternative: compute q₁² and handle the cross-terms within D-frame.

```
q₁² = q₂·D + s₂                  → top level squared
2·q₁·Π(R₁) = 2·q₁·s₁/D          → cross-term, exact rational
Π(R₁)² = s₁²/D²                  → small, nests deeper

Full numerator over D²: q₁²·D² + 2·q₁·s₁·D + s₁²
                      = (q₁²·D + 2·q₁·s₁)·D + s₁²

Divide by D: let T = q₁²·D + 2·q₁·s₁, then T = q₃·D + s₃
Divide s₁² by D: s₁² = q₄·D + s₄

Result: [q₃, D, [s₃ + q₄, D, [s₄, D, 0]]]    depth 2
```

Pattern: each multiplication adds at most one remainder level. After 3 multiplications (π⁴): depth ≤ 3. After n multiplications: depth ≤ n. Denominator is always D.


## G04: Linear Combination (A₂ Coefficient)

**Problem:** A₂ = 197/144 + π²/12 + 3ζ(3)/4 − (π²/2)·ln(2)

Each term is a rational coefficient times a Q335 constant. The rational coefficients have odd factors (144 = 2⁴·3², 12 = 2²·3).

```
Term 1: 197/144 → [197, 144, 0], no Q335 needed, exact closed
Term 2: p(π²) / 12 → integer division: p(π²) = q·12 + s → [q, D, [s, 12, 0]]
         but 12 = 4·3, so shift: p(π²) >> 2 = q', remainder s' < 4
         then divide q' by 3: q' = q''·3 + s''
         Result: [q'', D/4, [s'', 3, [s', D, 0]]]
```

Simpler approach — keep everything over D and handle the rational coefficient:

```
π²/12: the value is p(π²)/(12·D). Multiply numerator and denominator:
       = p(π²)·(D/12) / D... no, D/12 isn't integer since D = 2³³⁵ and 12 has factor 3.
```

This is where the odd-factor issue (AR4, LM4) arises. Two strategies:

**Strategy A (hybrid denominator):** carry as [p(π²), 12·D, 0]. The denominator 12·D = 3·4·D = 3·2³³⁷. The factor 3 is explicit. Addition with other terms requires LCD.

**Strategy B (nested remainder):** 
```
p(π²) = 12·q + s,  s ∈ {0,...,11}
π²/12 as VDR: [q, D, [s, 12·D, 0]]
```

Strategy B keeps the top level in D-frame. The odd factor 3 is confined to the remainder's denominator. For the full A₂ sum, the top-level terms (all over D) add as integers. The remainders collect and normalize.

```
A₂ top-level ≈ 197_rebased + q₂ + q₃ - q₄    (integer arithmetic)
A₂ remainder = collection of [s_i, c_i·D, 0] children with small odd denominators
```

The QED coefficient is an integer plus a small structured remainder. The 100-digit precision lives in the integer. The remainder carries exact sub-precision structure.


## G05: Complex Multiplication

**Problem:** (3 + 4i)·(1 + 2i) using VDR pairs.

```
A = ([3,1,0], [4,1,0])
B = ([1,1,0], [2,1,0])

Re: 3·1 - 4·2 = 3 - 8 = -5
Im: 3·2 + 4·1 = 6 + 4 = 10

Result: ([-5,1,0], [10,1,0])
```

Exact, trivial, all closed. Now with Q335 constants:

**Problem:** (π + ei)·(ln2 + √2·i)

```
Re: p(π)·p(ln2) - p(e)·p(√2)    two products, one subtraction
Im: p(π)·p(√2) + p(e)·p(ln2)    two products, one addition
```

Each product via G01: `p·p = q·D + s`, giving [q, D, [s, D, 0]].

```
Re product 1: p(π)·p(ln2) = q₁·D + s₁
Re product 2: p(e)·p(√2)  = q₂·D + s₂
Re result: [(q₁ - q₂), D, [(s₁ - s₂), D, 0]]
```

If s₁ - s₂ < 0, normalize: borrow 1 from top V, add D to remainder. Standard carry arithmetic on the VDR tree. The complex multiply is four G01-style operations plus two integer add/subs. Frame stays D throughout.


## G06: DFT Butterfly

**Problem:** One radix-2 butterfly with twiddle factor W = ω₈¹ = cos(π/4) - i·sin(π/4) = (1/√2)(1 - i).

```
W = ([p(1/√2), D, 0], [-p(1/√2), D, 0])
```

where p(1/√2) = p(√2)/2 (right-shift by 1, since D = 2³³⁵, this is exact: [p(√2), 2·D, 0] = [p(√2)/2, D, 0] if p(√2) is even, otherwise [p(√2)>>1, D, [(p(√2) mod 2), 2·D, 0]]).

Given inputs A = (A_re, A_im) and B = (B_re, B_im):

```
W·B:
  Re = p(1/√2)·B_re - (-p(1/√2))·B_im = p(1/√2)·(B_re + B_im)
  Im = p(1/√2)·B_im + (-p(1/√2))·B_re = p(1/√2)·(B_im - B_re)

X_even = A + W·B:  (A_re + Re(W·B),  A_im + Im(W·B))
X_odd  = A - W·B:  (A_re - Re(W·B),  A_im - Im(W·B))
```

Two multiplications instead of four (the 1/√2 factor is common). Each multiplication is G01-style, producing one remainder level. Additions are integer ops at the top level. One butterfly, one remainder level, frame preserved.

After log₂(N) = 10 stages for N = 1024: remainder depth ≤ 10. Each node is a Q335 integer. The entire 1024-point FFT lives in integer arithmetic with 10-deep remainder trees.


## G07: Inverse FFT and Parseval Check

**Problem:** Verify IFFT(FFT(x)) = x for a 4-point signal.

```
x = ([1,D,0], [2,D,0], [3,D,0], [4,D,0])   (real signal, Q335 frame)
```

4-point DFT twiddle factors: ω₄⁰ = 1, ω₄¹ = -i, ω₄² = -1, ω₄³ = i. All components in {-1, 0, 1}. No Q335 projection needed — exact closed VDR.

```
X[0] = 1 + 2 + 3 + 4 = 10
X[1] = 1 + 2·(-i) + 3·(-1) + 4·(i) = (1-3) + (-2+4)i = -2 + 2i
X[2] = 1 + 2·(-1) + 3·(1) + 4·(-1) = -2
X[3] = 1 + 2·(i) + 3·(-1) + 4·(-i) = -2 - 2i
```

All integer. IFFT divides by N = 4 and conjugates twiddles. Every intermediate value is exact. Roundtrip is exact by construction — no float butterfly error to accumulate.

**Parseval:** |X[0]|² + |X[1]|² + |X[2]|² + |X[3]|² = 100 + 8 + 4 + 8 = 120 = 4·(1 + 4 + 9 + 16) = 4·30. Exact.


## G08: 2×2 Eigenvalues

**Problem:** Find eigenvalues of M = [[3,1],[1,3]].

Characteristic polynomial: (3-λ)² - 1 = λ² - 6λ + 8 = (λ-2)(λ-4).

Eigenvalues: 2 and 4. Rational. VDR handles this exactly as closed objects.

**Problem:** M = [[0,-1],[1,0]] (rotation by π/2).

Characteristic polynomial: λ² + 1 = 0. Eigenvalues: ±i.

As VDR complex pairs: λ₁ = ([0,1,0], [1,1,0]), λ₂ = ([0,1,0], [-1,1,0]). Exact.

**Problem:** M = [[2,1],[0,2]]. Repeated eigenvalue λ = 2, defective.

Characteristic polynomial: (2-λ)² = 0. Single eigenvalue [2,1,0] with algebraic multiplicity 2. Eigenvector computation involves (M - 2I) = [[0,1],[0,0]], null space spanned by (1,0). All exact integer operations.

**Problem:** M = [[1,2],[3,4]]. Eigenvalues (5 ± √33)/2.

√33 is irrational. As functional remainder: Newton iteration x_{n+1} = (x_n + 33/x_n)/2 starting from x₀ = 6. Each step exact rational, quadratic convergence. Eigenvalue at depth d: [(5 + x_d)/2, 1, functional_remainder]. Or Q335: p(√33) computed once, eigenvalue as Q335 arithmetic.


## G09: Quaternion Rotation

**Problem:** Rotate vector v = (1, 0, 0) by 90° around the z-axis using quaternion q = cos(45°) + sin(45°)·k.

```
cos(π/4) = sin(π/4) = 1/√2

q = (p(1/√2)/D, 0, 0, p(1/√2)/D)   as (w, x, y, z) components over D
```

Quaternion rotation: v' = q·v·q⁻¹. For unit quaternion, q⁻¹ = q*.

```
v as quaternion: (0, 1, 0, 0) — exact integer, closed

q·v: quaternion multiplication, 16 component multiplies, all integer
(q·v)·q*: another 16 component multiplies

Result should be (0, 0, 1, 0) — rotated to y-axis
```

Each component multiply involving p(1/√2) uses G01: product mod D goes to V, remainder nests. After two quaternion multiplications, remainder depth ≤ 2. The result's real-part (w) and the components should collapse: top-level integers giving 0, 0, 1, 0 plus a remainder tree. If the remainder tree sums to zero (it should, since the exact answer is integer), normalization collapses it to closed form.

This is the key test: does exact quaternion rotation of an axis-aligned vector return an axis-aligned vector exactly? With float, you get (0, ε, 1-δ, ε). With VDR, the remainder tree must cancel to zero. If it does, closed-form preference (N7) fires and you get the exact integer result.


## G10: Slerp Between Two Quaternions

**Problem:** Slerp between q₀ = (1, 0, 0, 0) (identity) and q₁ = (0, 0, 0, 1) (180° around z) at t = 1/2.

```
q₀·q₁ = cos(θ) → w-component of q₀*·q₁ = 0 → θ = π/2
```

slerp(q₀, q₁, 1/2):
```
sin((1/2)·π/2) / sin(π/2) · q₀ + sin((1/2)·π/2) / sin(π/2) · q₁
= sin(π/4) / 1 · q₀ + sin(π/4) / 1 · q₁
= (1/√2)·(1,0,0,0) + (1/√2)·(0,0,0,1)
= (1/√2, 0, 0, 1/√2)
```

This is a 90° rotation around z. All coefficients are 1/√2 = Q335 value. Exact. The denominators sin(π/2) = 1 (closed, no division issue). The numerators sin(π/4) = 1/√2 (Q335 projection).

**Harder case:** t = 1/3, θ = π/3 (60° between quaternions).

```
sin((2/3)·π/3) / sin(π/3)  and  sin((1/3)·π/3) / sin(π/3)
= sin(2π/9) / sin(π/3)     and  sin(π/9) / sin(π/3)
```

sin(π/3) = √3/2 — Q335 as p(√3)/2. sin(π/9) and sin(2π/9) — no closed forms. These are functional remainders: Taylor series of sin at rational multiples of π, each depth giving an exact rational. The division by sin(π/3) is G02-style division. At any evaluation depth, the slerp coefficients are exact rationals. The quaternion result is four exact rational components.


## G11: RoPE (Rotary Position Embedding)

**Problem:** Apply rotary position embedding to a 4-dimensional vector at position m with base frequency θ₀ = 10000.

RoPE applies 2D rotations in pairs: dimensions (0,1) rotate by mθ₀, dimensions (2,3) rotate by mθ₁, where θ_k = 1/10000^(2k/d).

For d = 4: θ₀ = 1/10000^0 = 1, θ₁ = 1/10000^(1/2) = 1/100.

At position m = 7:
```
Angle for dims (0,1): 7·1 = 7 radians
Angle for dims (2,3): 7/100 radians
```

cos(7) and sin(7): functional remainders (Taylor series at x = 7). At depth d, exact rational. Project to Q335.

cos(7/100) and sin(7/100): Taylor series converges fast (small argument). At 20 terms, hundreds of correct digits.

```
[x₀', x₁'] = [x₀·cos(7) - x₁·sin(7),  x₀·sin(7) + x₁·cos(7)]
[x₂', x₃'] = [x₂·cos(7/100) - x₃·sin(7/100),  x₂·sin(7/100) + x₃·cos(7/100)]
```

Each is a 2D rotation = complex multiplication. If x₀, x₁ are Q335 integers and cos(7), sin(7) are Q335 projections, each product is G01, each rotation is G05. Two complex multiplications for the full RoPE application.

The point: every position embedding in an integer-based LLM is exact. No drift across sequence positions. Position 1 and position 100000 have the same arithmetic precision. Float-based RoPE accumulates error at large positions — VDR does not.


## G12: Modular Reduction as Remainder Nesting

**Problem:** Compute 7¹⁰⁰ mod 13.

```
7¹ mod 13 = 7         → [0, 1, [7, 13, 0]]
7² = 49 = 3·13 + 10   → [3, 1, [10, 13, 0]] but we only need the remainder
7² mod 13 = 10
```

By Fermat's little theorem: 7¹² ≡ 1 (mod 13). So 7¹⁰⁰ = 7^(12·8 + 4) = (7¹²)⁸ · 7⁴ ≡ 1⁸ · 7⁴ (mod 13).

7⁴ = 2401 = 184·13 + 9. So 7¹⁰⁰ mod 13 = 9.

VDR representation: [184, 1, [9, 13, 0]]. The remainder [9, 13, 0] is the modular residue. It's not something left over — it's the answer.

The VDR object [184, 1, [9, 13, 0]] carries both the quotient (184 = 2401/13 floored) and the modular residue (9) as first-class structure. Discarding V and keeping R gives modular arithmetic. Keeping both gives exact division.


## G13: CRT as Multi-Denominator Remainder

**Problem:** Solve x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).

Solution: x = 23 (mod 105).

VDR representation of x/105:
```
23 = 0·105 + 23
[0, 1, [23, 105, 0]]
```

But 105 = 3·5·7. The composite remainder can decompose into children with coprime denominators:

```
23 mod 3 = 2:  [7, 1, [2, 3, 0]]   (23 = 7·3 + 2)
23 mod 5 = 3:  [4, 1, [3, 5, 0]]   (23 = 4·5 + 3)
23 mod 7 = 2:  [3, 1, [2, 7, 0]]   (23 = 3·7 + 2)
```

These three remainder children at denominators 3, 5, 7 carry the CRT residues. Axiom A13 (pairwise distinct denominators) holds. The VDR normalization can reconstruct the composite from the components, and CRT reconstruction builds the composite from the residues. Same operation, different direction.


## G14: Chaotic Map with Bounded Frame

**Problem:** Logistic map x_{n+1} = 4x_n(1-x_n) starting at x₀ = 1/3, five steps, in Q335 frame.

```
x₀ = p(1/3) over D,  where p(1/3) = round(D/3)

x₁ = 4·x₀·(1-x₀) = 4·(1/3)·(2/3) = 8/9
   In Q335: 4·p(1/3)·(D - p(1/3)) = P₁
   P₁ = q₁·D + s₁ → [q₁, D, [s₁, D, 0]]

x₂ = 4·x₁·(1-x₁) = 4·(8/9)·(1/9) = 32/81
   In Q335: need to multiply the active result by (D - active result)
   This involves active multiplication (AA3)
   Remainder depth grows by 1
```

After 5 steps: remainder depth ≤ 5. Each level is a Q335-scale integer. The denominator is always D = 2³³⁵. Compare: in bare Fraction arithmetic, x₅ has denominator 9^(2⁵) = 9³² ≈ 10³⁰ digits. In Q335 frame: 5 levels × ~102 digits per level ≈ 510 digits of structured information. Same information, different shape.

The remainder tree at depth 5 carries exactly the information that the 10³⁰-digit denominator carried. But it's decomposed into manageable pieces. And if you only need 100-digit precision, you read the top level and stop.


## G15: Periodic Orbit Detection

**Problem:** Tent map on x₀ = 1/7, detect period.

```
T(x) = 2x if x < 1/2, else 2(1-x)

x₀ = 1/7     < 1/2 → x₁ = 2/7
x₁ = 2/7     < 1/2 → x₂ = 4/7
x₂ = 4/7     > 1/2 → x₃ = 2(1-4/7) = 6/7
x₃ = 6/7     > 1/2 → x₄ = 2(1-6/7) = 2/7 = x₁
```

Period 3 (cycle: 2/7 → 4/7 → 6/7 → 2/7). Denominator stays 7 forever. In Q335 frame: p(1/7) = round(D/7), and the orbit visits p(2/7), p(4/7), p(6/7) cyclically. All Q335 integers. No remainder nesting needed — the map is piecewise linear with rational coefficients, and 1/7 generates a finite orbit.

This confirms VDR-2's finding (CH6): periodic rational orbits under chaotic maps are free. The denominator doesn't grow because the orbit is finite. VDR detects periodicity by exact equality comparison — something float cannot do because it drifts off the cycle.


## G16: Gram-Schmidt with Complex Vectors

**Problem:** Orthogonalize v₁ = (1+i, 2) and v₂ = (3, 1-i) using Gram-Schmidt with VDR complex arithmetic.

All components as VDR pairs. Inner product: ⟨u, v⟩ = Σ u_k* · v_k (conjugate-linear in first argument).

```
⟨v₁, v₁⟩ = (1-i)(1+i) + 2·2 = 2 + 4 = 6     (real, closed)
⟨v₁, v₂⟩ = (1-i)·3 + 2·(1-i) = 3-3i + 2-2i = 5-5i

proj = ⟨v₁,v₂⟩/⟨v₁,v₁⟩ · v₁ = (5-5i)/6 · (1+i, 2)

(5-5i)(1+i)/6 = (5+5i-5i-5i²)/6 = (5+5)/6 = 10/6 = 5/3
(5-5i)·2/6 = (10-10i)/6 = (5-5i)/3

u₂ = v₂ - proj·v₁ = (3, 1-i) - (5/3, (5-5i)/3)
   = (4/3, (-2+2i)/3)
```

Verify orthogonality: ⟨u₂, v₁⟩ = (4/3)*(1+i) + ((-2-2i)/3)·2 = (4+4i)/3 + (-4-4i)/3 = 0. Exact.

Every step is rational arithmetic on VDR pairs. The division by 6 produces exact rationals (no remainder nesting needed here since 5/6 and 5/3 are exact). The orthogonality check gives exactly zero, not ε.


## G17: Discrete Fourier Transform of Rational Signal

**Problem:** 4-point DFT of x = (1/3, 1/7, 1/11, 1/13).

```
X[k] = Σ x[n]·ω₄^(-nk)

ω₄ = e^(-2πi/4) = -i

X[0] = 1/3 + 1/7 + 1/11 + 1/13
     = (1001 + 429 + 273 + 231) / 3003
     = 1934/3003

X[1] = 1/3 + 1/7·(i) + 1/11·(-1) + 1/13·(-i)
     = (1/3 - 1/11) + (1/7 - 1/13)i
     = 8/33 + 6/91·i

X[2] = 1/3 - 1/7 + 1/11 - 1/13
     = (1/3 + 1/11) - (1/7 + 1/13)
     = 14/33 - 20/91
     = (14·91 - 20·33) / (33·91)
     = (1274 - 660) / 3003
     = 614/3003

X[3] = conjugate of X[1] (real input) = 8/33 - 6/91·i
```

Every DFT coefficient is an exact rational (real and imaginary parts). The twiddle factors at N = 4 are in {1, -1, i, -i}, so no Q335 projection needed. For N = 8 you'd need 1/√2 (Q335). For general N, the twiddle table is precomputed Q335 pairs. The DFT of any rational signal over any N is exact VDR arithmetic — complex pairs with Q335 remainder nesting at each butterfly.

**Parseval check:** Σ|x[n]|² = 1/9 + 1/49 + 1/121 + 1/169. Σ|X[k]|²/N should equal the same. Both sides exact rationals, verifiable by VDR closed arithmetic.


## G18: Modulus of Complex VDR

**Problem:** |π + ei|²

```
|z|² = Re² + Im² = π² + e²
     = p(π)² + p(e)² over D²
```

p(π)² = q₁·D + s₁, p(e)² = q₂·D + s₂.

```
Sum: (q₁+q₂)·D + (s₁+s₂)
If s₁+s₂ ≥ D: carry → [(q₁+q₂+1), D, [s₁+s₂-D, D, 0]]
If s₁+s₂ < D: [(q₁+q₂), D, [s₁+s₂, D, 0]]
```

Frame stays D. Remainder is first-class. |z|² is a single VDR object (real) at depth 1.

For |z| itself: square root via Newton functional remainder. x_{n+1} = (x_n + |z|²/x_n)/2. Each depth exact rational. Never need to leave integer arithmetic.


## G19: Transfer Function Evaluation (Control Theory)

**Problem:** H(s) = 1/(s² + 3s + 2) evaluated at s = iω for ω = 1 (frequency response).

```
s = i → s² = -1

H(i) = 1/((-1) + 3i + 2) = 1/(1 + 3i)

Rationalize: (1 - 3i) / (1 + 9) = (1 - 3i)/10
```

VDR: H(i) = ([1, 10, 0], [-3, 10, 0]). Exact closed. Magnitude squared: (1 + 9)/100 = 1/10. Phase: arctan(-3/1) as functional remainder.

For ω = π/4 (irrational frequency):
```
s = iπ/4 → s² = -π²/16

H(iπ/4) = 1/(-π²/16 + 3iπ/4 + 2) = 1/((2 - π²/16) + 3πi/4)
```

Denominator is complex with Q335 components. Rationalize by conjugate multiplication — all G05-style complex arithmetic. Result is a VDR complex pair with Q335 components and remainder nesting from the multiplications.


## G20: Residue Number System Correspondence

**Problem:** Represent 1000 in RNS with moduli {7, 11, 13} and show VDR equivalence.

```
1000 mod 7  = 6    (1000 = 142·7 + 6)
1000 mod 11 = 10   (1000 = 90·11 + 10)
1000 mod 13 = 12   (1000 = 76·13 + 12)

RNS tuple: (6, 10, 12)
```

VDR composite remainder with three children:
```
[quotient₁, 1, [6, 7, 0] + [10, 11, 0] + [12, 13, 0]]
```

Axiom A13 holds: denominators 7, 11, 13 are pairwise distinct (and coprime). The three children carry the RNS residues. CRT reconstructs 1000 from (6, 10, 12) mod (7, 11, 13). VDR normalization performs the equivalent merge.

**Addition in RNS:** 1000 + 500.
```
500 mod 7 = 3, mod 11 = 5, mod 13 = 6
Sum: (6+3 mod 7, 10+5 mod 11, 12+6 mod 13) = (2, 4, 5)
```
Each channel adds independently — parallel. VDR: same-D children merge (N6), and modular reduction within each denominator frame. The structural parallel is exact.


---

## Summary of Patterns Observed

**Frame preservation.** Every operation keeps D = 2³³⁵ at the top level. Multiplications nest one remainder level. Divisions confine odd denominators to R. Linear combinations are integer ops.

**Depth as cost.** Where flat Fraction arithmetic grows denominators, Q335 remainder nesting grows tree depth. After n multiplications: depth n, denominator D. The information content is identical. The structure is manageable.

**Complex as pairs.** No new type needed. Complex multiplication is four real multiplications (G01) plus two additions. FFT butterflies compose from this. Twiddle factors are precomputed Q335 pairs. The entire DFT is integer arithmetic with bounded-depth remainder trees.

**Modular structure is remainder structure.** CRT residues, RNS channels, and VDR remainder children at coprime denominators are the same mathematical object viewed from different angles. VDR makes this explicit and recursive.

**Periodic orbits are free, chaotic orbits are deep.** The tent map on 1/7 never nests. The logistic map nests one level per step. Both are exact. The cost difference is structural, visible, and manageable by precision policy.

**Functional remainders bridge the gap.** Where exact closed forms don't exist (√33, sin(7), arccos), functional remainders produce exact rationals at every depth. Q335 projection captures the result as an integer. The two mechanisms compose: functional remainder computes, Q335 captures, integer arithmetic continues.

---

