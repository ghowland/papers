# VDR and Decimal as Parallel Arithmetic Systems

## Abstract

Decimal arithmetic and VDR arithmetic are parallel computational systems serving different purposes. Decimal arithmetic is a positional approximation system optimized for speed, bounded storage, and human readability. VDR arithmetic is an exact fractional-structural system optimized for exact equality, zero drift, and explicit preservation of unresolved structure. Neither replaces the other. They operate in parallel, with different invariants, different costs, and different failure modes. This paper describes the distinction mechanically. Decimal arithmetic hides truncation inside a finite digit budget. VDR exposes representation cost directly through exact integers and denominator growth. Decimal gives fast approximate answers. VDR gives exact fractional answers. The practical conclusion is that VDR should not be understood as an alternative notation for decimal, but as a separate arithmetic substrate running beside it.

## 1. Introduction

Most modern computation uses decimal or binary floating-point arithmetic. Values are stored in finite positional form, arithmetic is performed inside fixed precision, and results are rounded or truncated when they exceed the available digit budget. This is appropriate for most numerical work. It is fast, standardized, and easy to interpret.

But positional arithmetic is not exact once the target value lies outside the system's finite representable set. Repeated operations lose equality. Small errors accumulate. Comparison requires tolerances.

VDR is a different kind of arithmetic system. It represents values as exact integer triples with recursive remainder structure. Closed values are exact fractions. Active values preserve unresolved exact structure instead of discarding it. Functional forms produce exact fractional answers at chosen recursion depth. Fixed-denominator bases such as Q335 allow large families of constants to be carried as exact fractions in a shared frame.

The correct description is not that VDR improves decimal. It is that VDR and decimal are parallel systems.

## 2. Decimal Arithmetic

Decimal arithmetic is a positional digit system. A finite decimal has the form

\[
\pm d_0.d_1d_2\dots d_n \times 10^k
\]

with bounded digit count.

Mechanically, decimal arithmetic works by:
- storing a finite number of digits,
- aligning exponents,
- performing arithmetic in that finite digit window,
- rounding or truncating excess digits.

Its strengths are:
- speed,
- compactness,
- human familiarity,
- straightforward engineering use.

Its limitation is structural:
- many values cannot be represented exactly,
- exact equality is generally not stable under long chains of operations,
- truncation is built into the system.

Decimal arithmetic is therefore an approximation system.

## 3. VDR Arithmetic

VDR represents values as triples

\[
[V, D, R]
\]

where:
- \(V\) is an integer numerator component,
- \(D\) is a nonzero integer denominator frame,
- \(R\) is exact remainder structure.

When \(R = 0\), the object is closed and behaves as an exact fraction:

\[
[V, D, 0] \mapsto V/D
\]

When \(R \neq 0\), the object is active and carries exact unresolved structure that scalar systems would normally discard.

Mechanically, VDR arithmetic works by:
- using arbitrary-precision integers,
- preserving exact fractional state,
- rebasing into new denominator frames without approximation,
- carrying leftover exact structure in the remainder slot,
- optionally resolving recursive generators into exact fractions at chosen depth.

Its strengths are:
- exact equality,
- zero drift,
- explicit provenance of unresolved structure,
- exact fractional outputs.

Its limitation is practical:
- numerators and denominators can grow very large,
- exact operations can become CPU- and memory-intensive.

VDR arithmetic is therefore an exact fraction-structure system.

## 4. Parallel, Not Hierarchical

VDR and decimal should not be placed in a simple hierarchy such as "better" and "worse." They optimize for different invariants.

Decimal preserves:
- bounded storage,
- fast arithmetic,
- standardized approximate output.

VDR preserves:
- exact equality,
- exact fractional value,
- exact structure,
- explicit cost.

So they are parallel systems in the following sense:
- both are valid arithmetic substrates,
- both can support practical computation,
- each makes a different trade between cost and invariance.

Decimal hides cost by fixing precision.
VDR exposes cost by preserving exactness.

## 5. Equality

This is the clearest divergence.

In decimal arithmetic, equality is fragile under repeated operations because representation is approximate. One often replaces equality with tolerance:

\[
|x-y| < \varepsilon
\]

In VDR, closed arithmetic preserves exact equality directly. If an operation chain is algebraically reversible, the original value is recovered exactly.

So:
- decimal often treats equality as approximate closeness,
- VDR treats equality as exact recoverability.

This is not a small implementation detail. It is a foundational distinction between the two systems.

## 6. Representation of Cost

Decimal makes representation cost mostly invisible:
- digit budget is fixed,
- overflow and underflow are handled by range limits,
- truncation happens silently or routinely.

VDR makes representation cost visible:
- denominator growth is explicit,
- numerator growth is explicit,
- recursive expansion depth is explicit,
- exactness cost appears as larger integers and slower arithmetic.

This matters most in nonlinear iteration and chaos. Decimal gives a fast stream of approximate values while silently losing information. VDR preserves the information and pays the full combinatorial cost.

So the systems differ not only in result quality but in how honestly they expose computational burden.

## 7. Non-Rational Targets

Decimal handles non-rational targets by printing approximations.
VDR handles them by producing exact fractions to chosen depth or chosen basis.

For example:
- decimal stores a finite approximation of \(\pi\),
- VDR may store a fixed exact fraction in a shared denominator basis such as Q335,
- or generate deeper exact fractions through recursive series or Newton-style expansion.

In both cases the target is approached operationally.
The difference is:
- decimal stores approximate digits,
- VDR stores exact fractions.

So VDR is not a decimal variant.
It is a separate method for finite access to non-rational mathematics.

## 8. Where Decimal Dominates

Decimal is better suited when:
- speed matters more than exact equality,
- bounded precision is acceptable,
- outputs are intended for human consumption,
- the computation is large-scale and approximate by nature,
- floating scientific workloads dominate.

This is why decimal and floating systems remain essential.

## 9. Where VDR Dominates

VDR is better suited when:
- exact fractional answers are required,
- equality must survive long operation chains,
- modular or rational structure matters,
- denominators and provenance are meaningful,
- approximation noise would corrupt discrete structure.

This includes many exact or semi-exact domains:
- rational algebra,
- number theory,
- combinatorics,
- cryptography,
- exact probability,
- exact geometry predicates,
- exact discrete calculus.

## 10. The Shared Boundary

Both systems encounter the same deep practical boundary:
computation becomes expensive when the information content of the target grows rapidly.

For decimal, this appears as:
- precision exhaustion,
- rounding drift,
- unstable significance.

For VDR, this appears as:
- denominator explosion,
- integer growth,
- CPU and memory cost.

So the difference is not that one has limitations and the other does not.
The difference is how those limitations are paid:
- decimal pays by discarding information,
- VDR pays by preserving it.

## 11. Q335 as a Parallel Basis

A fixed shared denominator basis such as Q335 makes the parallelism especially clear.

In decimal:
- a transcendental constant is carried as finite digits.

In Q335-VDR:
- the same constant is carried as an exact integer over \(2^{335}\).

Arithmetic then becomes:
- decimal: finite-digit positional operations,
- VDR-Q335: integer operations in a common denominator frame.

These are plainly parallel strategies for the same engineering task:
finite computation with values not natively closed in small rational form.

## 12. Conclusion

VDR and decimal are best understood as parallel arithmetic systems.

Decimal is:
- positional,
- bounded,
- approximate,
- fast.

VDR is:
- fractional-structural,
- exact,
- explicit about cost,
- slower when values become large.

Decimal is not a defective version of VDR.
VDR is not a slower notation for decimal.
They are different substrates built around different priorities.

The right practical view is coexistence:
- use decimal when bounded approximation is the right tool,
- use VDR when exact fractional answers and equality preservation matter more than speed.

In that sense, VDR stands beside decimal, not beneath it and not above it, as a parallel arithmetic system with its own proper domain.
