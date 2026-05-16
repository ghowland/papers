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

# VDR Q335 Remainder Nesting Gym — Part 2: Functional Remainder Compositions

## Conventions (continued)

D = 2³³⁵. Functional remainders are Python callables `f(depth) → VDR` stored in R. They compose with Q335 frame arithmetic. All gym entries build on G01–G20.


## G21: Functional Remainder as Lazy Square Root

**Problem:** √7 as a functional remainder, then use it in arithmetic.

```python
def sqrt7(depth):
    x = VDR(3, 1, 0)  # initial guess, 3² = 9 ≈ 7
    for _ in range(depth):
        x = (x + VDR(7,1,0) / x) / VDR(2,1,0)
    return x

r = VDR(0, 1, FnRemainder(sqrt7, "√7"))
```

At depth 0: x = 3/1. At depth 1: (3 + 7/3)/2 = 8/3. At depth 5: exact rational with ~32 correct digits. At depth 7: ~128 digits. Each is an exact rational, not an approximation.

**Now compose:** eigenvalue of [[1,2],[3,4]] is (5 + √33)/2.

```python
def sqrt33(depth):
    x = VDR(6, 1, 0)
    for _ in range(depth):
        x = (x + VDR(33,1,0) / x) / VDR(2,1,0)
    return x

def eigenvalue_plus(depth):
    s = sqrt33(depth)
    return (VDR(5,1,0) + s) / VDR(2,1,0)

lambda1 = VDR(0, 1, FnRemainder(eigenvalue_plus, "λ₊([[1,2],[3,4]])"))
```

Resolve at depth 7, project to Q335:
```python
val = resolve(lambda1, depth=7)  # exact rational, ~128 correct digits
p_lambda = round(val.to_fraction() * D)
q335_lambda = VDR(p_lambda, D, 0)
```

The eigenvalue is now a Q335 integer, ready for matrix operations in the Q335 frame. The functional remainder computed it. The Q335 projection captured it. Integer arithmetic continues.


## G22: Twiddle Table as Functional Remainder Factory

**Problem:** Build the twiddle table for N-point FFT using functional remainders, then freeze to Q335.

```python
def make_twiddle(k, N):
    """Returns (cos_fn, sin_fn) functional remainder pair for ω_N^k"""
    angle_num = -2 * k  # -2πk/N, carry the π separately
    angle_den = N
    
    def cos_fn(depth):
        # Taylor series for cos(2πk/N) to `depth` terms
        # Each term is exact rational (powers of (2πk/N)²)
        # π² at each depth via newton or Q335
        pi2 = resolve(sqrt_pi2_fn, depth)  # or use Q335 p(π²)
        angle2 = VDR(4 * k * k, N * N, 0) * pi2  # (2πk/N)²
        result = VDR(1, 1, 0)
        term = VDR(1, 1, 0)
        for n in range(1, depth + 1):
            term = -term * angle2 / VDR(2*n*(2*n-1), 1, 0)
            result = result + term
        return result
    
    def sin_fn(depth):
        # Same structure, odd powers
        pi_val = resolve(pi_fn, depth)
        angle = VDR(2 * k, N, 0) * pi_val
        result = angle
        term = angle
        angle2 = angle * angle
        for n in range(1, depth + 1):
            term = -term * angle2 / VDR((2*n+1)*(2*n), 1, 0)
            result = result + term
        return result
    
    return (
        VDR(0, 1, FnRemainder(cos_fn, f"cos(2π·{k}/{N})")),
        VDR(0, 1, FnRemainder(sin_fn, f"sin(2π·{k}/{N})"))
    )

# Build table for N=8
twiddles = [make_twiddle(k, 8) for k in range(4)]
```

Each twiddle factor exists as a pair of functional remainders. At resolution time, each resolves to an exact rational. Project to Q335:

```python
def freeze_twiddle(fn_pair, depth=10):
    c = resolve(fn_pair[0], depth)
    s = resolve(fn_pair[1], depth)
    return (
        VDR(round(c.to_fraction() * D), D, 0),
        VDR(round(s.to_fraction() * D), D, 0)
    )

q335_twiddles = [freeze_twiddle(t) for t in twiddles]
```

Computed once, stored as integers, used forever. The functional remainder is the derivation. The Q335 integer is the operational form. Both are VDR objects.


## G23: Composed Rotations via Functional Remainders

**Problem:** Apply three sequential rotations to a vector, each at an irrational angle, track exactness.

```python
def rotation_matrix(angle_fn, name):
    """2D rotation matrix from angular functional remainder"""
    def mat_fn(depth):
        c = resolve(angle_fn, depth)  # cos
        s = resolve(angle_fn, depth)  # sin (separate fn)
        # returns Mat([[c, -s], [s, c]])
        return mat
    return FnRemainder(mat_fn, name)

# Three rotations: by √2 radians, by π/7 radians, by ln(3) radians
R1 = rotation_matrix(sqrt2_cos, "rot(√2)")
R2 = rotation_matrix(pi_over_7_cos, "rot(π/7)")
R3 = rotation_matrix(ln3_cos, "rot(ln3)")
```

The composed rotation R3·R2·R1 applied to v = (1, 0):

```python
def composed_rotation(depth):
    m1 = resolve(R1, depth)  # exact rational 2x2 matrix
    m2 = resolve(R2, depth)
    m3 = resolve(R3, depth)
    return m3 * m2 * m1 * Vec([VDR(1,1,0), VDR(0,1,0)])

result = VDR(0, 1, FnRemainder(composed_rotation, "R3·R2·R1·(1,0)"))
```

At any depth, resolving gives the exact rational vector. No drift between the three multiplications — each is exact rational matrix-vector multiply. The functional remainder defers the computation until precision is needed. The total rotation angle √2 + π/7 + ln(3) is itself representable as a functional remainder sum.


## G24: IIR Filter with Irrational Coefficients

**Problem:** IIR filter y[n] = (√2/2)·y[n-1] + x[n], impulse response.

The coefficient √2/2 = 1/√2 is irrational. As Q335: p(1/√2).

```python
def iir_response(N):
    """Compute first N samples of impulse response in Q335 frame"""
    coeff = VDR(p_inv_sqrt2, D, 0)  # Q335 for 1/√2
    y = VDR(0, D, 0)
    results = []
    for n in range(N):
        x_n = VDR(D, D, 0) if n == 0 else VDR(0, D, 0)  # unit impulse
        y = coeff * y + x_n  # G01 multiplication + addition
        results.append(y)
    return results
```

y[0] = 1. y[1] = 1/√2. y[2] = 1/2. y[3] = 1/(2√2). y[n] = (1/√2)^n.

Each step multiplies by Q335 1/√2 — one G01 operation, one remainder level. After 20 steps: remainder depth 20, denominator still D. The output y[20] = (1/√2)^20 = 1/1024 = exact closed rational. The remainder tree should collapse (normalization rule N7) because the exact answer is rational.

This is a test of the system's ability to detect when an irrational coefficient raised to an integer power produces a rational result. (1/√2)^20 = 2^(-10) = 1/1024. If the remainder nesting collapses to closed form, the system has effectively discovered this algebraic identity through computation.

**Functional remainder version:**

```python
def iir_at_n(coeff_fn):
    def response(depth):
        c = resolve(coeff_fn, depth)  # exact rational for 1/√2 at this depth
        # c^n is exact rational power of an exact rational
        return c  # for single-step; chain for n steps
    return FnRemainder(response, "IIR(1/√2)")
```

The functional remainder defers the power computation. At depth d, the Newton iterate for √2 gives a rational r_d, and (1/r_d)^20 is an exact rational. As d→∞ through integer steps, this rational approaches 1/1024 and at sufficient depth the numerator and denominator will be exact powers of 2, collapsing.


## G25: Bayesian Update with Transcendental Prior

**Problem:** Prior P(H) = 1/e, likelihood P(D|H) = π/4, P(D|¬H) = 1/3. Posterior?

```
P(H|D) = P(D|H)·P(H) / [P(D|H)·P(H) + P(D|¬H)·P(¬H)]
```

```python
prior = VDR(p_inv_e, D, 0)           # 1/e as Q335
not_prior = VDR(D - p_inv_e, D, 0)   # 1 - 1/e as Q335
likelihood = VDR(p_pi_over_4, D, 0)  # π/4 as Q335
alt_like = VDR(1, 3, 0)              # 1/3 exact closed

numerator = likelihood * prior        # G01: Q335 × Q335, depth 1
alt_term = alt_like * not_prior        # closed × Q335, stays Q335 frame
denominator = numerator + alt_term     # addition in D-frame

posterior = numerator / denominator    # G02: division, remainder nests
```

The posterior P(H|D) is an exact VDR object with Q335 frame and remainder nesting. It is not an approximation of Bayes' theorem — it is Bayes' theorem computed in integer arithmetic with the irrational prior and likelihood captured as Q335 integers. The remainder carries the exact sub-100-digit structure.

Verify: posterior must be in (0, 1). The top-level V/D ratio gives 100-digit confidence. The remainder refines.

**Sequential update:** apply Bayes 10 times with the same likelihood. Each update is one G01 multiply and one G02 divide. After 10 updates: remainder depth ≤ 20 (each update contributes one multiply depth and one divide depth). The posterior converges toward 0 or 1 as evidence accumulates, and the VDR object tracks the exact trajectory.


## G26: Polynomial Evaluation with Horner and Functional Coefficients

**Problem:** Evaluate p(x) = πx³ - ex² + √2·x - ln(3) at x = 1/7.

```python
def horner_eval(depth):
    pi = resolve(pi_fn, depth)
    e = resolve(e_fn, depth)
    s2 = resolve(sqrt2_fn, depth)
    ln3 = resolve(ln3_fn, depth)
    x = VDR(1, 7, 0)
    
    # Horner: ((π·x - e)·x + √2)·x - ln(3)
    result = pi
    result = result * x - e
    result = result * x + s2
    result = result * x - ln3
    return result

p_at_1_7 = VDR(0, 1, FnRemainder(horner_eval, "p(1/7)"))
```

At each depth, all four coefficients are exact rationals, x = 1/7 is exact closed, and Horner's method performs 3 multiplications and 3 additions — all exact rational. The result at any depth is exact. The functional remainder wraps the whole evaluation, deferring coefficient precision until needed.

**Freeze to Q335:**
```python
val = resolve(p_at_1_7, depth=10)  # ~1024 correct digits for coefficients
p_result = round(val.to_fraction() * D)
q335_result = VDR(p_result, D, 0)
```

One Q335 integer captures the polynomial evaluation. The derivation (Horner + functional coefficients) is in the history. The operational value is an integer.


## G27: Determinant via Functional Remainder

**Problem:** det(M) where M has entries involving √2 and π, without materializing the full cofactor expansion until precision is needed.

```python
def lazy_det(matrix_fn):
    """Wrap determinant computation in a functional remainder"""
    def det_fn(depth):
        # Resolve each matrix entry at this depth
        M = resolve_matrix(matrix_fn, depth)
        # Cofactor expansion — all exact rational at this depth
        return M.det()
    return FnRemainder(det_fn, f"det(M)")

M_fn = lambda depth: Mat([
    [resolve(sqrt2_fn, depth), VDR(1,1,0)],
    [VDR(3,1,0), resolve(pi_fn, depth)]
])

det_M = VDR(0, 1, lazy_det(M_fn))
```

At depth 7: √2 and π are rationals with ~128 correct digits. det = √2·π - 3. Exact rational at every depth. The determinant is lazy — not computed until resolved. For a 10×10 matrix with transcendental entries, this defers the O(n!) cofactor cost until you actually need the value, and then computes it at exactly the precision you request.

**Compose:** Use det_M in Cramer's rule to solve a linear system.

```python
def cramers_x1(depth):
    d = resolve(det_M, depth)
    # Replace column 1 with RHS, compute det of modified matrix
    d1 = resolve(lazy_det(M1_fn), depth)
    return d1 / d  # exact rational division

x1 = VDR(0, 1, FnRemainder(cramers_x1, "x₁ via Cramer"))
```

The entire linear solve is a functional remainder. No precision is committed until resolution. The depth parameter flows through the determinant computations, the matrix entry resolutions, and the final division — all at the same depth, all exact rational.


## G28: Power Series Composition

**Problem:** Compute exp(sin(x)) at x = 1/5 using composed functional remainders.

```python
def sin_series(x):
    def fn(depth):
        result = VDR(0, 1, 0)
        term = x  # first term
        x2 = x * x
        for n in range(depth):
            result = result + term
            term = -term * x2 / VDR((2*n+2)*(2*n+3), 1, 0)
        return result
    return FnRemainder(fn, f"sin({x})")

def exp_series(x_fn):
    def fn(depth):
        x = resolve(x_fn, depth)  # sin(1/5) at this depth — exact rational
        result = VDR(1, 1, 0)
        term = VDR(1, 1, 0)
        for n in range(1, depth + 1):
            term = term * x / VDR(n, 1, 0)
            result = result + term
        return result
    return FnRemainder(fn, "exp(sin(x))")

exp_sin_1_5 = VDR(0, 1, exp_series(sin_series(VDR(1, 5, 0))))
```

The outer functional remainder (exp) calls the inner one (sin) at the same depth. At depth 10: sin(1/5) computed to 10 terms (exact rational), then exp of that rational computed to 10 terms (exact rational). The composition is exact at every depth. No floating-point intermediate anywhere.

**Freeze to Q335:**
```python
val = resolve(exp_sin_1_5, depth=15)
p_result = round(val.to_fraction() * D)
# Single Q335 integer representing exp(sin(1/5)) to 100+ digits
```


## G29: Discrete Convolution with Q335 Kernel

**Problem:** Convolve signal x = [1/3, 1/7, 1/11] with kernel h = [π/4, √2/2] in Q335 frame.

```python
# Signal as Q335
x = [VDR(p_1_3, D, 0), VDR(p_1_7, D, 0), VDR(p_1_11, D, 0)]
h = [VDR(p_pi_4, D, 0), VDR(p_inv_sqrt2, D, 0)]

# Convolution y[n] = Σ x[k]·h[n-k]
# y has length 3 + 2 - 1 = 4
y = [VDR(0, D, 0)] * 4
for k in range(3):
    for j in range(2):
        y[k+j] = y[k+j] + x[k] * h[j]  # G01 multiply + add
```

Each `x[k] * h[j]` is a Q335 × Q335 multiplication (G01), producing depth 1. The accumulated sums stay at depth 1 (addition doesn't deepen). Output: 4 Q335 values at depth 1.

**Now do it via DFT:** zero-pad both to length 4, DFT each (G17 style), pointwise complex multiply (G05), IDFT. Same result, more butterflies, same depth bound. The DFT path demonstrates that VDR convolution via FFT gives the same exact result as direct convolution — something float FFT convolution does not guarantee due to butterfly rounding.


## G30: Functional Remainder Wrapping Matrix Exponential

**Problem:** e^(At) for A = [[-1, 0],[0, -2]], t = 1/3.

Eigenvalues are -1 and -2 (rational, diagonal matrix). e^(At) = diag(e^(-1/3), e^(-2/3)).

```python
def mat_exp_diag(A_diag, t):
    """Matrix exponential for diagonal matrix via functional remainder"""
    def fn(depth):
        entries = []
        for lam in A_diag:
            # exp(λt) as Taylor series at this depth
            lt = lam * t
            result = VDR(1, 1, 0)
            term = VDR(1, 1, 0)
            for n in range(1, depth + 1):
                term = term * lt / VDR(n, 1, 0)
                result = result + term
            entries.append(result)
        return Mat.diag(entries)
    return FnRemainder(fn, f"exp(A·{t})")

eAt = mat_exp_diag([VDR(-1,1,0), VDR(-2,1,0)], VDR(1,3,0))
```

At depth 15: e^(-1/3) and e^(-2/3) each computed to 15 Taylor terms. Each term involves (−1/3)^n / n! — exact rational with denominator 3^n · n!. The matrix exponential is a 2×2 diagonal of exact rationals.

**Non-diagonal case:** A = [[0, 1],[-1, 0]] (rotation). e^(At) = [[cos(t), sin(t)],[-sin(t), cos(t)]]. Each entry is a trig functional remainder (G22 style). At t = 1/3, cos(1/3) and sin(1/3) are Taylor series with rational coefficients — exact rational at every depth.

```python
def mat_exp_rotation(t):
    def fn(depth):
        c = cos_series(t, depth)  # exact rational
        s = sin_series(t, depth)  # exact rational
        return Mat([[c, s], [-s, c]])
    return FnRemainder(fn, f"exp(rot·{t})")
```

The functional remainder wraps the matrix. Resolve at any depth to get the exact rational rotation matrix. Multiply matrices at the same depth — exact. Chain 100 rotations — still exact at each depth.


## G31: Fixed-Frame Logistic Map via Functional Remainder

**Problem:** The denominator growth problem from VDR-2 FW2. Logistic map r = 4, x₀ = 1/3, represent n steps without materializing intermediate denominators.

```python
def logistic_fn(x0, r, n_steps):
    """Functional remainder: nth iterate of logistic map"""
    def fn(depth):
        # At this depth, compute x0 to `depth` precision
        # then iterate n_steps times in exact rational arithmetic
        x = x0
        r_vdr = VDR(r, 1, 0)
        for _ in range(n_steps):
            x = r_vdr * x * (VDR(1,1,0) - x)
        return x
    return FnRemainder(fn, f"logistic({x0}, r={r}, n={n_steps})")

# x₅ of logistic map
x5 = VDR(0, 1, logistic_fn(VDR(1,3,0), 4, 5))
```

Wait — this still materializes the intermediate fractions inside the functional remainder. The denominators still grow as 3^(2^5) = 3^32 inside `fn`. The functional remainder wraps it but doesn't compress it.

**Actual compression requires a different approach:**

```python
def logistic_q335(x0_q335, r, n_steps):
    """Logistic map staying in Q335 frame, remainder nesting absorbs growth"""
    x = x0_q335
    r_q = VDR(r * D, D, 0)  # r=4 as Q335
    one = VDR(D, D, 0)       # 1 as Q335
    for _ in range(n_steps):
        one_minus_x = one - x       # integer subtraction, stays D-frame
        rx = r_q * x                 # G01: Q335 × Q335 → depth +1
        x = rx * one_minus_x         # G01: active × Q335 → depth +1
        # At this point, x has remainder depth = 2 * step
    return x

x5 = logistic_q335(VDR(p_1_3, D, 0), 4, 5)
# x5 has remainder depth 10, denominator D throughout
```

After 5 steps: depth 10. After 15 steps: depth 30. Each node is a Q335 integer. Total information: 30 × ~102 digits ≈ 3060 digits. Compare flat Fraction: denominator has 3^(2^15) ≈ 10^15600 digits. The Q335 tree is 5000× more compact for the same exact value.

The compression comes from the frame discipline: instead of letting the denominator explode, each multiplication truncates to the D-frame and nests the remainder. The tree stores the same information in structured form.

**But is the tree value actually equal to the flat Fraction value?**

Yes. Each nesting step is exact: qD + s = p₁p₂ exactly. The scalar projection Π of the depth-10 tree equals p₁p₂/D² at each multiplication, which equals the exact flat Fraction. The tree is a different representation of the same exact value. No information is lost — it's rearranged.

**Precision policy:** If you only need 100 digits, read the top level. If you need 200 digits, read two levels. Each level gives ~100 additional digits (since each Q335 integer is ~102 digits). Precision is proportional to tree depth read, not tree depth stored.


## G32: Signal Energy via Parseval with Mixed Types

**Problem:** Signal x[n] with rational samples and Q335 filter coefficients. Verify Parseval identity.

```python
# Time-domain energy
x = [VDR(1,3,0), VDR(2,7,0), VDR(5,11,0), VDR(3,13,0)]  # rational
energy_time = sum(xi * xi for xi in x)  # exact closed rational

# Frequency domain: DFT via G17, all exact
X = dft_4(x)  # list of VDR complex pairs
energy_freq = sum(abs2(Xk) for Xk in X) / VDR(4,1,0)  # |X[k]|²/N

# These must be equal
assert energy_time == energy_freq  # exact equality, not ≈
```

Now filter with h = [p(π/4)/D, p(1/√2)/D] (Q335 coefficients):

```python
y = convolve(x, h)  # G29 — Q335 × rational at each step
# Each y[n] has Q335 frame with depth-1 remainder from the multiplications
# Energy of y in time domain: sum of y[n]², each y[n] active
energy_y_time = sum(yi * yi for yi in y)  # active × active, depth grows

# Frequency domain: Y[k] = X[k]·H[k], pointwise complex multiply
H = dft(h, N=len(y))  # DFT of filter
Y = [complex_mul(Xk, Hk) for Xk, Hk in zip(X_padded, H)]
energy_y_freq = sum(abs2(Yk) for Yk in Y) / VDR(len(y), 1, 0)

# Parseval: these must be equal
# Both are VDR active objects — equality checked after normalization
assert normalize(energy_y_time) == normalize(energy_y_freq)
```

The test verifies that Parseval's identity holds exactly through the entire pipeline: rational signal → Q335 filter → convolution → DFT → energy comparison. Float would give agreement to ~15 digits. VDR gives structural equality after normalization — the remainder trees are identical.


## G33: Functional Remainder as Lazy Inverse

**Problem:** Defer matrix inversion until needed, at requested precision.

```python
def lazy_inverse(mat_fn, name):
    def fn(depth):
        M = resolve(mat_fn, depth)  # exact rational matrix at this depth
        d = M.det()                  # exact rational
        if d == VDR(0,1,0):
            raise ValueError("Singular matrix")
        return M.adjugate() / d      # exact rational matrix
    return FnRemainder(fn, f"inv({name})")

# Hilbert 4×4 with one transcendental entry
def H4_modified(depth):
    H = hilbert(4)                         # standard rational Hilbert
    H[0][0] = resolve(pi_fn, depth) / VDR(4,1,0)  # replace H[0][0] = 1 with π/4
    return H

H4_inv = lazy_inverse(H4_modified, "H₄_mod")

# Not computed yet. Just a functional remainder.
# Resolve when needed:
M_inv = resolve(H4_inv, depth=10)  # exact rational 4×4 at ~1024-digit precision
```

**Compose:** solve Ax = b by lazy_inverse(A) · b.

```python
def lazy_solve(mat_fn, b_fn, name):
    def fn(depth):
        A_inv = resolve(lazy_inverse(mat_fn, "A"), depth)
        b = resolve(b_fn, depth)
        return A_inv * b  # exact rational matrix-vector multiply
    return FnRemainder(fn, f"solve({name})")
```

The entire solve chain — matrix entry resolution, determinant, adjugate, inversion, matrix-vector product — is deferred until `resolve(fn, depth)` is called. The depth parameter propagates through every sub-computation. One depth value controls precision everywhere.


## G34: Wavelet Transform with Q335 Coefficients

**Problem:** Haar wavelet on signal [π, e, √2, ln(3)] — all Q335 values.

```python
x = [VDR(p_pi, D, 0), VDR(p_e, D, 0), VDR(p_sqrt2, D, 0), VDR(p_ln3, D, 0)]

# Haar forward: averages and differences
avg = [(x[0]+x[1]) * VDR(D,2*D,0), (x[2]+x[3]) * VDR(D,2*D,0)]  # /2 via shift
det = [(x[0]-x[1]) * VDR(D,2*D,0), (x[2]-x[3]) * VDR(D,2*D,0)]

# Level 2
avg2 = [(avg[0]+avg[1]) * VDR(D,2*D,0)]
det2 = [(avg[0]-avg[1]) * VDR(D,2*D,0)]
```

Division by 2 is a right-shift in the Q335 frame: if p is even, p/2 is exact with no remainder. If p is odd, [p>>1, D, [1, 2*D, 0]] — one bit of remainder. Haar wavelet on Q335 values produces Q335 values with at most 1-bit remainder at each level.

**Inverse:** reconstruct from coefficients. avg[0] = avg2[0] + det2[0], avg[1] = avg2[0] - det2[0], etc. Integer addition/subtraction. Perfect reconstruction if the forward/inverse paths use the same bit-level rounding — which they do, because VDR carries the remainder explicitly.

VDR-3 Gym 22 demonstrated this for integer signals. This extends to Q335 signals with the same perfect reconstruction guarantee, because the remainder nesting captures the half-bit lost in each /2 operation.


## G35: Functional Remainder Composition Chain

**Problem:** Build f(x) = exp(√(sin(x) + 1)) at x = 1/4, as a chain of functional remainders.

```python
def compose(outer_fn, inner_fn, name):
    """Generic function composition as functional remainder"""
    def fn(depth):
        inner_val = resolve(inner_fn, depth)
        return resolve_with_input(outer_fn, inner_val, depth)
    return FnRemainder(fn, name)

sin_1_4 = sin_series_fn(VDR(1, 4, 0))           # sin(1/4) — fn remainder
plus_one = lambda_fn(sin_1_4, lambda v: v + VDR(1,1,0))  # sin(1/4) + 1
sqrt_val = newton_sqrt_fn(plus_one)               # √(sin(1/4) + 1)
result = exp_series_fn(sqrt_val)                   # exp(√(sin(1/4) + 1))
```

Four levels of functional remainder composition. At depth d:
1. sin(1/4) computed to d Taylor terms → exact rational
2. Add 1 → exact rational
3. √ of that rational via d Newton steps → exact rational
4. exp of that rational via d Taylor terms → exact rational

Each level produces an exact rational. The levels compose through `resolve`. Total cost at depth d: O(d) Taylor terms × O(d) Newton iterations × O(d) more Taylor terms. Cubic in d. But d = 10 gives ~1000 correct digits for the sin, ~1024 correct digits for √, and ~100+ for exp (depending on convergence rate). More than sufficient for Q335 projection.

```python
val = resolve(result, depth=12)
p_result = round(val.to_fraction() * D)
# exp(√(sin(1/4) + 1)) as a single Q335 integer
```


## Summary of Compositions

| Gym | Operation | Inputs | Mechanism | Output |
|-----|-----------|--------|-----------|--------|
| G21 | √ via Newton | integer | functional remainder | Q335 |
| G22 | twiddle table | angle | fn remainder → freeze | Q335 pairs |
| G23 | chained rotations | fn remainders | compose at same depth | fn remainder |
| G24 | IIR filter | Q335 coeff | G01 multiply chain | Q335 depth-n |
| G25 | Bayes update | Q335 prior/likelihood | G01 × G02 | Q335 active |
| G26 | Horner eval | fn remainder coeffs | resolve + rational ops | fn remainder → Q335 |
| G27 | lazy det | fn remainder matrix | deferred cofactor | fn remainder |
| G28 | series composition | fn(fn(x)) | nested resolve | fn remainder → Q335 |
| G29 | convolution | Q335 signal × kernel | G01 multiply chain | Q335 depth-1 |
| G30 | matrix exp | diagonal/rotation | Taylor fn remainder | fn remainder |
| G31 | logistic map | Q335 frame | G01 per step, depth grows | Q335 depth-2n |
| G32 | Parseval verify | mixed rational + Q335 | DFT + energy | exact equality |
| G33 | lazy inverse | fn remainder matrix | deferred adjugate/det | fn remainder |
| G34 | Haar wavelet | Q335 signal | shift + remainder | Q335 depth-1 |
| G35 | 4-level compose | sin→+1→√→exp | chained fn remainders | fn remainder → Q335 |

The pattern across all compositions: functional remainders defer computation, Q335 captures results as integers, remainder nesting preserves exactness within a fixed frame, and depth is the universal cost currency. Every operation composes with every other because they all speak the same language — exact rationals at a requested depth, projected into a shared integer frame when needed for arithmetic.

---

# VDR Builtin Function Registry

Each builtin is a factory that returns a `FnRemainder`. All take VDR arguments and produce VDR at each depth. IOSE = Input, Output, Side effects, Edge cases.

---

**B01: sqrt(n)**
- I: VDR integer n ≥ 0
- O: √n as exact rational at each depth via Newton x_{k+1} = (x_k + n/x_k)/2
- S: Pure
- E: n=0 → closed [0,1,0]. n negative → error. Perfect squares collapse to closed at sufficient depth.

**B02: exp(x)**
- I: VDR rational x
- O: eˣ via Taylor Σ xⁿ/n! truncated at depth terms
- S: Pure
- E: x=0 → closed [1,1,0]. Large |x| needs more depth for same precision.

**B03: sin(x)**
- I: VDR rational x
- O: sin(x) via Taylor odd series truncated at depth terms
- S: Pure
- E: x=0 → closed [0,1,0].

**B04: cos(x)**
- I: VDR rational x
- O: cos(x) via Taylor even series truncated at depth terms
- S: Pure
- E: x=0 → closed [1,1,0].

**B05: ln(x)**
- I: VDR rational x > 0
- O: ln(x). Near 1: series ln(1+t). General x: reduce via ln(x) = ln(a·2^k) = ln(a) + k·ln(2) with ln(2) from Q335 or arctanh series.
- S: Pure
- E: x ≤ 0 → error. x=1 → closed [0,1,0]. x = power of 2 → k·ln(2).

**B06: arctan(x)**
- I: VDR rational x
- O: arctan(x) via Taylor for |x| ≤ 1, identity reduction arctan(x) = π/2 - arctan(1/x) for |x| > 1
- S: Pure
- E: x=0 → closed [0,1,0]. x=1 → π/4.

**B07: arcsin(x)**
- I: VDR rational x, |x| ≤ 1
- O: arcsin(x) via Taylor with central binomial coefficients
- S: Pure
- E: |x| > 1 → error. x=0 → closed [0,1,0].

**B08: arccos(x)**
- I: VDR rational x, |x| ≤ 1
- O: π/2 - arcsin(x). Composes const_pi and B07.
- S: Pure
- E: x=1 → closed [0,1,0]. x=0 → π/2.

**B09: power(base, n)**
- I: VDR base, integer n
- O: base^n via repeated squaring
- S: Pure
- E: base=0, n<0 → error. n=0 → closed [1,1,0].

**B10: nth_root(x, q)**
- I: VDR rational x > 0, integer q > 0
- O: x^(1/q) via generalized Newton x_{k+1} = ((q-1)·x_k + x/x_k^(q-1))/q
- S: Pure
- E: x ≤ 0 with even q → error. q=1 → identity. q=2 → equivalent to B01.

**B11: const_pi()**
- I: none
- O: π via Machin-type arctangent identity, exact rational at each depth
- S: Pure
- E: none

**B12: const_e()**
- I: none
- O: e via Σ 1/n!, exact rational at each depth
- S: Pure
- E: none

**B13: zeta(s)**
- I: integer s ≥ 2
- O: ζ(s) via Borwein acceleration for odd s, closed-form identity for even s
- S: Pure
- E: s=1 → error (pole). s < 1 → unsupported.

**B14: polylog(n, x)**
- I: integer n ≥ 1, VDR rational x with |x| ≤ 1
- O: Li_n(x) = Σ xᵏ/kⁿ truncated at depth terms
- S: Pure
- E: x=1 → ζ(n) via B13. x=0 → closed [0,1,0].

**B15: elliptic_k(k)**
- I: VDR rational k with 0 ≤ k² < 1
- O: K(k) = (π/2)·₂F₁(1/2,1/2;1;k²) via hypergeometric recurrence
- S: Pure
- E: k=0 → π/2. k²≥1 → error.

**B16: elliptic_e(k)**
- I: VDR rational k with 0 ≤ k² < 1
- O: E(k) = (π/2)·₂F₁(-1/2,1/2;1;k²) via hypergeometric recurrence
- S: Pure
- E: k=0 → π/2.

**B17: hypergeometric_2f1(a, b, c, x)**
- I: VDR rationals a, b, c, x with |x| < 1, c not non-positive integer
- O: ₂F₁(a,b;c;x) via term recurrence, truncated at depth
- S: Pure
- E: |x| ≥ 1 → convergence issues. c ∈ {0,-1,-2,...} → error.

**B18: taylor(coeff_fn, x)**
- I: callable coeff_fn(n) → VDR, VDR rational x
- O: Σ coeff_fn(n)·xⁿ truncated at depth terms
- S: Pure iff coeff_fn is pure
- E: Convergence depends on series and x.

**B19: compose(f, g)**
- I: two FnRemainder builtins f, g
- O: f(g(x)) — resolves g at depth, passes result to f at same depth
- S: Pure iff both f and g are pure
- E: Type mismatch if g output is outside f input domain.

**B20: freeze(fn, depth)**
- I: FnRemainder fn, integer depth
- O: Q335 closed object — resolves fn at depth, projects to [round(val·D), D, 0]
- S: Pure. Lossy below 100-digit floor by design. One-way: Q335 → FnRemainder not recoverable.
- E: Insufficient depth for desired precision returns valid but less precise Q335 integer.

**B21: complex_pair(re_fn, im_fn)**
- I: two FnRemainders or VDR objects for real and imaginary parts
- O: VDR complex pair (re, im) supporting complex arithmetic (add, mul, conj, abs2)
- S: Pure
- E: Either component may be closed, active, or functional independently.

**B22: complex_mul(z1, z2)**
- I: two VDR complex pairs
- O: (a₁a₂ - b₁b₂, a₁b₂ + a₂b₁) as VDR complex pair
- S: Pure
- E: If both components closed, result is closed.

**B23: complex_inv(z)**
- I: VDR complex pair z = (a, b)
- O: (a, -b) / (a² + b²) as VDR complex pair
- S: Pure
- E: a² + b² = 0 → error (z = 0).

**B24: twiddle(k, N)**
- I: integers k, N
- O: VDR complex pair (cos(2πk/N), -sin(2πk/N)) via B04, B03 composed with const_pi
- S: Pure
- E: N=0 → error. k=0 → (1, 0) closed. N=4 → components in {-1,0,1} closed.

**B25: dft(signal, N)**
- I: list of VDR objects (or complex pairs), integer N
- O: list of N VDR complex pairs, each computed via twiddle multiplication and summation
- S: Pure
- E: N=1 → identity. Signal length < N → zero-padded.

**B26: slerp(q0, q1, t)**
- I: two unit quaternions as 4-tuples of VDR, VDR rational t ∈ [0,1]
- O: interpolated quaternion via sin-weighted combination. sin/arccos via B03, B08.
- S: Pure
- E: q0 = q1 → return q0. q0 = -q1 → great circle ambiguity, undefined. t=0 → q0. t=1 → q1.

**B27: quaternion_mul(q1, q2)**
- I: two quaternions as 4-tuples of VDR
- O: Hamilton product as 4-tuple of VDR, 16 component multiplies reduced to standard formula
- S: Pure
- E: All closed inputs → closed output.

**B28: mod(a, m)**
- I: VDR integer a, VDR integer m > 0
- O: VDR remainder [0, 1, [r, m, 0]] where r = a mod m, carrying both quotient and remainder as structure
- S: Pure
- E: m = 0 → error. a = 0 → [0, 1, [0, m, 0]].

**B29: crt(residues, moduli)**
- I: list of VDR integers (residues), list of VDR integers (moduli), pairwise coprime
- O: VDR object with composite remainder children at each modulus, reconstructable to unique solution mod product
- S: Pure
- E: Non-coprime moduli → error. Empty lists → error.

**B30: logistic_step(x, r)**
- I: VDR x in Q335 frame, VDR rational r
- O: r·x·(1-x) in Q335 frame with remainder nesting (G01 multiply, depth +2)
- S: Pure
- E: x outside [0,1] → mathematically valid but orbit may escape.

**B31: iterate(step_fn, x0, n)**
- I: FnRemainder or callable step_fn, VDR initial x0, integer n ≥ 0
- O: n-fold application of step_fn to x0, each step in Q335 frame with remainder nesting
- S: Pure
- E: n=0 → x0. step_fn must accept and return VDR.

**B32: detect_period(step_fn, x0, max_steps)**
- I: callable step_fn, VDR initial x0, integer max_steps
- O: VDR integer period length, or closed [0,1,0] if no period found within max_steps. Uses exact equality (normalized) at each step — no epsilon.
- S: Pure
- E: Aperiodic orbit within max_steps → returns 0. Floyd or Brent cycle detection on exact VDR equality.

**B33: horner(coeffs, x)**
- I: list of VDR coefficients [a₀, a₁, ..., aₙ] (ascending degree), VDR rational x
- O: a₀ + a₁x + ... + aₙxⁿ via Horner's method, exact rational
- S: Pure
- E: Empty coeffs → closed [0,1,0]. Coefficients may be closed, active, or functional (resolved at evaluation).

**B34: haar_forward(signal)**
- I: list of VDR objects, length power of 2
- O: list of VDR objects — Haar wavelet coefficients. Averages via integer add + right-shift, differences via integer sub + right-shift, remainder nesting for odd numerators.
- S: Pure
- E: Length not power of 2 → error. Length 1 → identity.

**B35: haar_inverse(coeffs)**
- I: list of VDR Haar coefficients
- O: reconstructed signal, exact inverse of B34. Perfect reconstruction including remainder structure.
- S: Pure
- E: Same length constraint as B34.

**B36: convolve(x, h)**
- I: two lists of VDR objects
- O: list of VDR objects, length len(x)+len(h)-1, each element via direct summation of products
- S: Pure
- E: Either list empty → empty result.

**B37: mat_fn(entry_fn, rows, cols)**
- I: callable entry_fn(i,j) → VDR or FnRemainder, integers rows, cols
- O: lazy matrix — entries not computed until resolved. Supports det, inverse, mul via deferred evaluation.
- S: Pure iff entry_fn is pure
- E: rows or cols ≤ 0 → error.

**B38: transfer_fn(num_coeffs, den_coeffs, s)**
- I: numerator and denominator polynomial coefficients as VDR lists, VDR complex pair s
- O: H(s) = N(s)/D(s) as VDR complex pair, polynomials evaluated via B33, division via B23
- S: Pure
- E: D(s) = 0 → pole, error.

**B39: borwein_eta(s, n)**
- I: integer s ≥ 2, integer n (number of acceleration terms)
- O: Dirichlet eta η(s) via Borwein weighted sum with rational d_k coefficients, exact rational
- S: Pure
- E: s = 1 → conditional convergence, slower. n determines precision: 3^(-n) error bound.

**B40: resolve_to_depth(fn, depth)**
- I: FnRemainder fn, integer depth ≥ 0
- O: concrete VDR object — the exact rational result of fn(depth)
- S: Pure
- E: depth=0 → initial guess / first term. Negative depth → error.

---

## Dependency Graph

```
const_pi (B11) ← arctan (B06)
const_e (B12) ← exp (B02) at x=1
zeta (B13) ← borwein_eta (B39) + const_pi (B11) for even s
elliptic_k (B15) ← hypergeometric_2f1 (B17) + const_pi (B11)
elliptic_e (B16) ← hypergeometric_2f1 (B17) + const_pi (B11)
arccos (B08) ← const_pi (B11) + arcsin (B07)
polylog (B14) ← zeta (B13) at x=1
twiddle (B24) ← cos (B04) + sin (B03) + const_pi (B11)
dft (B25) ← twiddle (B24) + complex_mul (B22)
slerp (B26) ← sin (B03) + arccos (B08) + quaternion_mul (B27)
transfer_fn (B38) ← horner (B33) + complex_inv (B23)
compose (B19) ← resolve_to_depth (B40)
freeze (B20) ← resolve_to_depth (B40)
iterate (B31) ← any step_fn
detect_period (B32) ← iterate (B31) + normalized equality
```

All leaf builtins (B01–B05, B09, B28) depend only on VDR core arithmetic. Everything else composes from these.
