# VDR-SOFTMAX-1 Technical Specification
## Exact and Fixed-Precision Softmax in VDR Arithmetic

## Abstract

This document specifies what would be required to implement softmax within the VDR arithmetic system. Softmax is not naturally native to exact rational arithmetic because it depends on exponentials and normalization over exponentials. VDR can still support softmax in two valid ways: recursive exact-fraction evaluation to chosen depth, or fixed-basis exact-fraction embedding to chosen precision. This specification defines the algorithms, data flow, precision policies, invariants, performance costs, and recommended engineering options. The conclusion is that softmax in VDR is possible and coherent, but should be treated as an engineered exact-fraction procedure rather than a primitive closed arithmetic operation.

---

## 1. Purpose

Softmax is central to modern machine learning and sequence models. Standard softmax is:

\[
\operatorname{softmax}(z_i)
=
\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

In float-based systems this is implemented numerically with exponentials, subtraction of the maximum for stability, and approximate division.

In VDR, the goal is different:
- no hidden float
- no hidden approximation
- exact fractional outputs at every chosen precision boundary
- explicit and inspectable cost

This document describes what must exist in order to support softmax over VDR values.

---

## 2. What Makes Softmax Difficult in VDR

Closed VDR arithmetic is exact rational arithmetic.
Softmax requires:
- exponentiation of general rational inputs
- summation of non-rational values
- reciprocal normalization

The key issue is not division. Division is already exact in VDR.
The issue is the exponential:
\[
e^x
\]
for general rational \(x\), which is not rational.

So softmax requires one of two engineering strategies:

1. represent each \(e^{z_i}\) by an exact fraction produced at chosen depth
2. represent each \(e^{z_i}\) by an exact fraction in a fixed denominator basis

Both are valid for VDR’s stated goals.

---

## 3. Scope of the Problem

Given an input vector:
\[
z = (z_1, z_2, \dots, z_n)
\]
where each \(z_i\) is a VDR object, we need to compute a vector:
\[
s = (s_1, \dots, s_n)
\]
such that:
\[
s_i = \frac{\exp(z_i)}{\sum_j \exp(z_j)}
\]

Desired properties:
- every \(s_i\) is a VDR closed object
- \(\sum_i s_i = 1\) exactly in the chosen representation
- all outputs are positive
- identical inputs give identical outputs
- larger logits produce larger outputs
- no float arithmetic appears internally

---

## 4. Softmax Modes

There are three possible implementation modes.

### 4.1 Recursive Exact-Fraction Softmax

Each exponential is evaluated by an exact rational recursion, typically a truncated Taylor series, continued fraction, or rational minimax scheme.

Example:
\[
e^x \approx \sum_{k=0}^N \frac{x^k}{k!}
\]

At fixed \(N\), this is an exact rational number if \(x\) is rational.

Then:
- compute all \(E_i = \mathrm{exp\_approx}(z_i, N)\) as exact fractions
- compute \(S = \sum_i E_i\)
- return \(E_i / S\)

Advantages:
- exact rational outputs
- transparent approximation depth
- no imported constants required

Costs:
- denominator and numerator growth can become large
- repeated powers and factorial denominators are expensive
- large logits require many terms unless range reduction is used

### 4.2 Fixed-Basis Softmax

Each exponential is evaluated to a fixed precision basis such as:
\[
[p_i, 2^k, 0]
\]

Then:
- all exponentials are exact fractions in the common basis
- the sum is exact
- division returns exact rational outputs

Advantages:
- common denominator simplifies accumulation
- operationally close to Q335-style engineering
- easier to optimize

Costs:
- requires a chosen precision floor
- nonlinear identities depend on basis quality
- re-evaluation at higher precision needs a larger basis

### 4.3 Rational Surrogate Softmax

Replace softmax by a rational positive normalization:

\[
\tilde{s}_i = \frac{g(z_i)}{\sum_j g(z_j)}
\]

where \(g\) is chosen to be:
- positive
- monotone
- exactly rational on rational inputs

Examples:
- \(g(x) = (x+c)^2\) on a bounded shifted domain
- \(g(x) = 1 + x + x^2/2\) when logits are range-controlled
- exact polynomial attention kernels

Advantages:
- entirely native to VDR
- no transcendental machinery required
- much cheaper

Cost:
- it is not standard exponential softmax

For exact VDR-native architectures, this may be the best design.

---

## 5. Required Core Components

To do standard softmax in VDR, the system must provide the following.

### 5.1 Exact Fractional Exponential Evaluation

A function:

```python
vdr_exp(x: VDR, mode="series", depth=N) -> VDR
```

or:

```python
vdr_exp_qbasis(x: VDR, bits=K) -> VDR
```

This must:
- accept a VDR input
- return a closed VDR fraction
- never return a float
- expose its precision control parameter

### 5.2 Range Reduction

Standard exponential evaluation is much more efficient if the argument is reduced.

Use:
\[
e^x = 2^m e^r
\]
where:
- \(m\) is an integer
- \(r\) lies in a small interval such as \([-\ln 2/2, \ln 2/2]\)

This requires:
- exact comparison
- exact subtraction
- a rational approximation or basis representation for \(\ln 2\)

Range reduction is strongly recommended.
Without it, series depth becomes impractical for moderate logits.

### 5.3 Exact Summation

This is already available:
- exact VDR addition of closed fractions

### 5.4 Exact Reciprocal

Also already available:
- exact division by a nonzero VDR closed object

### 5.5 Vector API

A softmax implementation should operate on `Vec`:

```python
vdr_softmax(logits: Vec, mode="series", depth=20) -> Vec
```

---

## 6. Stability Policy

Standard float softmax subtracts the maximum logit:
\[
s_i = \frac{e^{z_i - z_{\max}}}{\sum_j e^{z_j - z_{\max}}}
\]

This is also valid in VDR and should be retained, not because of float overflow, but because it sharply reduces exponential growth cost.

Required step:
- compute exact maximum by comparison
- subtract from all logits exactly
- exponentiate only shifted logits

This ensures:
- one output denominator scale dominates less
- fewer series terms needed
- fixed-basis exponentials remain better conditioned

So VDR softmax should still use max-shift stabilization.

---

## 7. Series-Based Exponential Specification

### 7.1 Basic Formula

For rational \(x\):
\[
\exp_N(x) = \sum_{k=0}^N \frac{x^k}{k!}
\]

Each term is exact if \(x\) is exact.

### 7.2 Required API

```python
def vdr_exp_series(x: VDR, depth: int) -> VDR:
    ...
```

Behavior:
- `depth=0` returns 1
- `depth=N` returns the exact fraction of the \(N\)-term partial sum

### 7.3 Precision Interpretation

The system must not claim this is exact \(e^x\).
It should claim:
- exact fraction equal to the chosen truncation

This matches VDR’s existing engineering philosophy.

### 7.4 Error Metadata

Optional but recommended:
- attach metadata or external report indicating truncation remainder bound

For example, for \(x \le 0\) after max-shift:
\[
R_{N+1}(x) \le \frac{|x|^{N+1}}{(N+1)!}
\]

This gives an explicit precision certificate.

---

## 8. Fixed-Basis Exponential Specification

### 8.1 Required API

```python
def vdr_exp_qbasis(x: VDR, bits: int) -> VDR:
    ...
```

Returns:
\[
[p, 2^k, 0]
\]
or another standard basis.

### 8.2 Internal Method

Possible implementations:
- evaluate series internally to higher precision, then round once into basis
- use binary splitting
- use rational minimax approximation on reduced range
- use table lookup plus range reduction

### 8.3 Output Guarantee

The output is:
- an exact fraction in the chosen basis
- representing \(e^x\) to the target precision floor

This is not exact transcendental arithmetic.
It is exact fixed-precision fractional embedding.

---

## 9. Softmax Normalization Invariant

After computing exponentials \(E_i\), define:
\[
S = \sum_i E_i
\]
and:
\[
s_i = E_i / S
\]

Then in VDR:
- each \(s_i\) is exact as a fraction
- \(\sum_i s_i = 1\) exactly

This is a major advantage over float softmax:
- output probabilities sum to exactly 1 in the chosen representation

So once the exponential stage is handled, normalization is straightforward and exact.

---

## 10. Monotonicity and Order Preservation

The implementation should preserve:
- if \(z_i > z_j\), then approximately \(s_i > s_j\)

This is automatic if:
- the exponential approximation is monotone on the relevant range
- or the surrogate kernel is monotone

Therefore any chosen approximation method must be tested for monotonicity over the intended logit interval.

This is especially important for rational surrogate softmax.

---

## 11. Required Engineering Decisions

To implement softmax in VDR, the project must choose:

### 11.1 Standard mode
One of:
- `series`
- `qbasis`
- `surrogate`

### 11.2 Precision control
One of:
- depth \(N\)
- denominator basis size \(2^k\)
- surrogate polynomial degree

### 11.3 Range policy
One of:
- no range reduction
- max-shift only
- max-shift plus \(\ln 2\)-based binary reduction

### 11.4 Export semantics
Decide whether the API returns:
- only the softmax vector
- softmax vector plus diagnostics
- softmax vector plus error-bound metadata

---

## 12. Computational Cost

### 12.1 Series cost

For each logit:
- compute powers \(x^k\)
- divide by \(k!\)
- sum terms

This causes:
- repeated exact multiplication
- denominator growth
- expensive large-integer accumulation

Cost grows with:
- vector length
- logit magnitude
- target precision depth

### 12.2 Fixed-basis cost

Costs are lower if all exponentials land in a shared denominator basis, but still include:
- basis generation
- range reduction
- high-precision internal exponential evaluation

### 12.3 Normalization cost

Relatively cheap:
- one exact sum
- \(n\) exact divisions

So the exponential stage is the main cost center.

---

## 13. Recommended First Implementation

The most realistic first implementation is:

1. exact max-shift
2. range-limited Taylor or Padé exponential
3. exact closed-fraction exponentials
4. exact normalization

API:

```python
def vdr_softmax(logits: Vec, depth: int = 16) -> Vec:
    ...
```

Algorithm:
1. compute \(m = \max_i z_i\)
2. set \(u_i = z_i - m\)
3. compute \(E_i = \exp_N(u_i)\) exactly
4. compute \(S = \sum_i E_i\)
5. return \(E_i / S\)

This gives:
- exact fractions
- exact sum-to-one
- no floats
- explicit depth parameter

---

## 14. Better Long-Term Implementation

Long-term, the preferred engineering design is likely:

- fixed-basis exponentials over \(2^k\)
- max-shift stabilization
- rational table/range reduction
- exact normalization back into closed VDR fractions

This is more suitable for ML-scale use because:
- denominator handling is more regular
- hardware optimization is easier
- repeated softmax calls are cheaper

---

## 15. Rational Surrogate Alternative

For VDR-native model design, a rational surrogate may be better than standard softmax.

Define:
\[
s_i = \frac{(z_i - m + c)^2}{\sum_j (z_j - m + c)^2}
\]
with \(c\) chosen large enough so all numerators are positive on the working domain.

Benefits:
- fully native to exact rational arithmetic
- exact positivity
- exact sum-to-one
- exact differentiability except at chosen piecewise points if needed
- no transcendental overhead

This may be the most practical VDR attention normalization for large systems.

---

## 16. Test Requirements

A valid VDR softmax implementation should be tested for:

1. exact output sum:
\[
\sum_i s_i = 1
\]

2. positivity:
\[
s_i > 0
\]

3. permutation consistency

4. monotonicity with respect to logits

5. equal logits produce equal probabilities

6. peakedness: large logit gap gives dominant probability

7. reproducibility: repeated calls give identical VDR outputs

8. precision convergence: deeper `depth` or larger basis improves agreement with reference

---

## 17. Proposed Module Surface

Suggested file:

```text
vdr/softmax.py
```

Suggested API:

```python
def vdr_exp_series(x: VDR, depth: int) -> VDR
def vdr_exp_pade(x: VDR, order: int) -> VDR
def vdr_exp_qbasis(x: VDR, bits: int) -> VDR
def vdr_softmax(logits: Vec, mode: str = "series", depth: int = 16) -> Vec
def vdr_softmax_qbasis(logits: Vec, bits: int = 128) -> Vec
def vdr_softmax_surrogate(
    logits: Vec, kernel: str = "square_shift", c: VDR = VDR(4)
) -> Vec
```

---

## 18. Boundary Statement

Implementing softmax in VDR requires:
- a non-native exponential stage,
- explicit precision policy,
- exact normalization over engineered exponential values.

This is not a defect.
It is exactly analogous to the way VDR already handles other non-rational targets:
- by exact fractional construction,
- not by hidden float approximation.

The real cost is:
- CPU time,
- numerator/denominator growth,
- basis management if fixed precision is used.

---

## 19. Conclusion

Softmax in VDR is possible, but it is not primitive.
It must be implemented as an engineered exact-fraction procedure.

There are three valid routes:
- recursive exact-fraction exponential evaluation,
- fixed-basis exact-fraction embedding,
- rational surrogate normalization.

For strict fidelity to standard ML, recursive or fixed-basis exponential softmax is appropriate.
For native VDR architectures, rational surrogate softmax may be the better design.

In all cases, once exponentials or positive kernel values are available as exact fractions, the normalization step is exact and straightforward. The resulting probability vector sums to exactly 1, which is a notable advantage over floating-point implementations.

If you want, I can next write:
1. the actual `vdr/softmax.py` code scaffold,
2. a rational-softmax proposal for VDR transformers,
3. or a VDR-native attention spec that avoids exponentials entirely.
