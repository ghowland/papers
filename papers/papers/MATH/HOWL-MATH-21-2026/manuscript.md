# The Representation Problem: 0.999... as Engineering Convention, Not Mathematical Identity
## A Critique of 0.999... = 1 from Representation Theory and Type Consistency

**Registry:** [@HOWL-MATH-21-2026]

**Date:** June 2026

**DOI:** 10.5281/zenodo.23491537

**Domain:** Foundations of Mathematics / Mathematical Representation Theory / Philosophy of Mathematics

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The standard mathematical claim that 0.999... = 1 is widely accepted and supported by multiple proof methods within real analysis. This paper argues that the claim is not a valid equality in the strict sense that mathematics defines equality. Instead, it is a type coercion between a base-dependent series function and a base-independent number. The limit convention that resolves the gap between these two objects is an engineering solution to a deficiency in base-10 positional encoding. It is not a mathematical property derivable from first principles. The paper further argues that positional notation itself embeds base-10 assumptions into all bases, making cross-base verification of such claims circular.

## 1. Introduction

The statement 0.999... = 1 is one of the most frequently discussed identities in mathematics. It is taught at the undergraduate level, supported by proofs from algebra, geometric series, and the construction of the real numbers via Dedekind cuts or Cauchy sequences. The mathematical community treats it as settled.

This paper does not dispute that the series represented by 0.999... converges to 1 under the standard definitions of real analysis. It does dispute that this convergence constitutes an equality in the sense that mathematics requires. Specifically, the paper identifies three problems with the standard treatment:

First, 0.999... is not a number. It is a notation for a function, specifically a convergent infinite series. The equals sign between it and 1 performs an evaluation, not a comparison of two objects of the same type.

Second, the notation 0.999... is base-dependent. It cannot be expressed in bases below 10. A valid mathematical identity must hold independent of representation. This one does not.

Third, the convention that closes the gap between the series and the number is self-referential. The real number system defines the limit, and then uses that limit definition to declare that no residual exists. The system validates its own lossy conversion using its own rules.

## 2. Numbers and Representations

A foundational requirement of any mathematical object that qualifies as a number is that it must exist independent of its representation. The number that English calls "three" and Roman notation writes as III and binary writes as 11 is the same number in all cases. The representation changes. The number does not.

This requirement implies that any valid statement about numbers must remain valid when the numbers involved are translated to a different representation system. If a statement can only be expressed in one base and becomes meaningless or inexpressible in another, then the statement is about the representation, not about the numbers.

The notation 0.999... uses the digit 9. In any base below 10, the digit 9 does not exist. Base 7 uses digits 0 through 6. Base 3 uses digits 0 through 2. Base 2 uses digits 0 and 1. The string 0.999... is not merely difficult to translate into these bases. It is impossible to write. The notation has no meaning outside of bases where 9 is a valid digit.

The number 1, by contrast, is writable in every base. It is the multiplicative identity. It requires no encoding system to define it and no series to evaluate it. It is a complete, self-contained mathematical object.

If 0.999... were a number, it would be expressible in all bases. It is not. Therefore it is not a number. It is a base-10 encoding artifact.

## 3. Functions and Numbers Are Distinct Types

A decimal representation in any base is a polynomial series. Each digit is a coefficient, and each position corresponds to a power of the reciprocal of the base. In base 10, the notation 0.999... represents:

9 × 10⁻¹ + 9 × 10⁻² + 9 × 10⁻³ + ...

This is a function. Specifically, it is an infinite series, which is a specific type of function that maps the natural numbers to partial sums and defines its value as the limit of those partial sums. The value of the function, when evaluated, is 1. But the function itself is not the number 1 any more than a recipe is a meal.

The real number system's decimal notation is, in effect, an anonymous Taylor series rooted in the prime factors of the base. For base 10, those factors are 2 and 5. Every decimal expansion is a computation expressed in terms of these factors. The representation carries the factors of its base into every value it encodes.

The number 1 has no such dependency. It is defined as the multiplicative identity: the unique number such that for all numbers x, 1 × x = x. This definition requires no base, no series, and no factors.

When the equals sign appears between 0.999... and 1, it connects two objects of different types. One is a function expressed in a base-dependent encoding. The other is a base-independent number. The operation being performed is evaluation, not comparison. This is a type coercion, and calling it equality obscures the mechanical difference between the two sides.

## 4. The Limit Convention as Engineering Patch

The standard justification for 0.999... = 1 relies on the epsilon-delta definition of a limit. The argument is as follows: for any positive real number ε, there exists a finite number of terms in the series such that the partial sum is within ε of 1. Since no positive ε can separate 0.999... from 1, no real number lies between them, and therefore they are equal.

This argument is valid within the rules of real analysis. But it is also circular. The real number system defines what qualifies as a valid ε. It defines what convergence means. And it then uses those definitions to declare that the residual left by its own representation system does not exist. The system is auditing itself and finding no problems.

The residual is real in the mechanical sense. The series 0.9, 0.99, 0.999 never reaches 1 at any finite step. At every step, a gap exists. The limit convention declares that because the gap can be made arbitrarily small, it is zero. But "arbitrarily small" and "zero" are not the same concept. The first is a property of a sequence. The second is a specific value. The convention equates them, and this equation is a design decision, not a derivation.

Egyptian fractions demonstrate that the problem is artificial. In the Egyptian fraction system, the value 1/3 is represented exactly as 1/3. There is no base, no series, no repeating expansion, and no limit needed. The value is written directly as a ratio of two integers. The problem that 0.999... addresses — the inability to finitely represent 1/3 in decimal notation — does not exist in systems that do not use positional encoding. The problem is created by base 10, and the limit convention is the patch that base 10 requires to handle the problem it created.

## 5. The Base-10 Colonization of All Bases

A subtle but critical issue undermines all cross-base arguments about positional notation. When mathematicians write a value in base 3, they write it using the symbols and conventions of base 10. The notation "0.1 in base 3" uses the base-10 digit symbols 0 and 1, the base-10 decimal point, and the base-10 positional convention of reading left to right with decreasing powers.

This is not base-3 arithmetic. It is a base-10 transcription of a base-3 concept. The digit 1 in "0.1 base 3" is a base-10 symbol that means "one unit of 3⁻¹." The positional framework, the digit symbols, and the notation are all imported from base 10. Base 3 has no independent written form in standard mathematical practice.

This means that arguments which claim to demonstrate base-independence by rewriting values in other bases are circular. They never leave base 10. They use base 10 to write about base 3, and then claim that the result validates base-10 conventions. Every positional base, as notated in standard mathematics, is a dialect of base 10.

Non-positional systems escape this dependency. Egyptian fractions use ratios of integers. Roman numerals use additive and subtractive symbol combinations. Tally marks use unary counting. None of these systems inherit the structure of base 10, and none of them produce the problem that 0.999... exists to solve.

The dominance of base-10 notation in mathematical writing creates an illusion of universality. Statements that appear to be about numbers are often about base-10 encoding. The claim 0.999... = 1 is one such statement.

## 6. Cross-Base Inconsistency

A mathematical identity must be expressible and verifiable in any valid representation system. The identity 1 + 1 = 2 can be written in every base, every numeral system, and every notation. It is a statement about numbers, and it survives all translations.

The statement 0.999... = 1 cannot be written in base 7, base 3, base 2, or any base below 10. The digit 9 does not exist in those systems. The statement is not translatable. It is imprisoned within the representation system that created it.

One might argue that equivalent statements exist in other bases. In base 2, the analogous claim would be 0.111... = 1. In base 3, it would be 0.222... = 1. Each base has its own version of the repeating-digit-approaching-1 phenomenon. But these are different statements about different series in different encoding systems. They share a structural pattern, but they are not the same identity. The convergence of 0.111... in base 2 is a statement about powers of 1/2. The convergence of 0.999... in base 10 is a statement about powers of 1/10. They involve different functions with different factors.

The fact that every positional base produces its own version of this problem confirms that the problem belongs to positional encoding itself, not to the numbers. The problem is systemic to the method of representation. And a problem that is systemic to a representation method is not a property of numbers.

The inability to escape base-10 notation even when writing other bases, as discussed in the previous section, further conceals this failure. The apparent universality of the repeating-decimal phenomenon is an artifact of always viewing other bases through the lens of base 10.

## 7. Renormalization as Precedent

The standard objection to the notation 0.000...1 is that it is not a valid real number because no natural number index exists for the final digit. This objection treats infinity as an impassable boundary. No digit can be placed after infinitely many digits because there is no position after infinity.

However, mathematics and physics do not consistently maintain this boundary. Renormalization in quantum field theory is a procedure that directly manipulates infinite quantities. Calculations in quantum electrodynamics produce infinite integrals. Rather than declaring these infinities impassable, physicists subtract infinite counterterms to extract finite, physically meaningful results. The predictions that emerge from this process are among the most precisely verified in all of science.

The residual represented by 0.000...1 is structurally analogous to a renormalization counterterm. It is the quantity that, if acknowledged and added, would make the conversion from the series 0.999... to the number 1 exact rather than conventional. The limit definition absorbs this quantity by declaring it zero. Renormalization absorbs analogous quantities by subtracting them explicitly.

The difference in treatment is a choice, not a necessity. Mathematics chooses to treat the residual as nonexistent. Physics chooses to treat analogous residuals as real and manipulable. Both approaches produce consistent results within their own frameworks. But the mathematical choice is not the only valid one, and its validity rests on convention rather than on a proof that the residual does not exist.

## 8. Implications

The argument presented here does not claim that repeating decimals are useless or that the limit definition is wrong. The limit definition is a powerful and productive tool. It enables calculus, analysis, and the entire framework of continuous mathematics. Its operational value is not in question.

What is in question is the ontological status of the claim. Repeating decimals are function notations. They describe series. They are operationally useful because evaluating those series produces numbers, and those numbers can be used in further computation. But treating the notation itself as a number, rather than as a function that produces a number, is a category error that the conventions of real analysis have papered over.

The distinction between evaluation and equality should be made explicit. When a mathematician writes 0.999... = 1, the notation should be understood as: "the series denoted by 0.999... evaluates to 1." This is a true and useful statement. But it is not the same as saying two numbers are equal, because only one number is present.

Formal notation could accommodate this distinction. A different symbol for evaluation, as opposed to equality, would make the type conversion visible rather than implicit. Programming languages maintain this distinction rigorously. The expression f(x) = 5 means either assignment or assertion depending on context, and the two are never confused because the language forces clarity. Mathematical notation does not enforce this clarity, and the result is a category of claims that appear to be about numbers but are about encodings.

## 9. Conclusion

The statement 0.999... = 1 is a valid evaluation. The series denoted by 0.999... converges to the number 1 under the standard definitions of real analysis. This paper does not dispute the convergence.

This paper disputes that the convergence constitutes an equality. The left side of the equation is a base-dependent function. The right side is a base-independent number. The equals sign performs a type coercion that mathematics does not formally acknowledge. The convention that closes the gap is an engineering solution to a deficiency in base-10 positional encoding, not a mathematical property derivable from axioms about numbers.

The dominance of base-10 notation in mathematical writing conceals the base-dependency of this claim. The inability to express the claim in bases below 10, combined with the fact that all positional bases are written using base-10 conventions, creates a circular validation structure. The claim appears universal because the notation system that produced it is used to examine it.

A rigorous treatment of mathematics should distinguish between numbers and the functions that produce them, between equality and evaluation, and between properties of numbers and properties of their encodings. The statement 0.999... = 1 conflates all three distinctions. Acknowledging this does not weaken mathematics. It strengthens it by making its conventions visible rather than implicit.

---

# A Standard Challenge to the 0.999... Problem
## Five Standard Objections to the Representation Problem, Exposed Through Base Translation

---

## Abstract

The paper [@HOWL-MATH-21-2026] argues that the standard mathematical claim 0.999... = 1 is a valid evaluation, not a mathematical equality. The claim is that the left side is a base-dependent series function and the right side is a base-independent number, and that the equals sign performs a type coercion between them.

A trained mathematician will raise predictable objections to this argument. These objections follow directly from standard education in real analysis. This companion paper identifies the five strongest forms of these objections, states each one fully, and tests each one by translating the claim into base 7. The test is mechanical: if 0.999... = 1 is equality in the sense that mathematics defines equality, then the same values must appear under the same rules in any base. No objection survives this test.

This paper does not introduce new theory. It traces the path from standard objection to retraction, so that a reader who arrives at [@HOWL-MATH-21-2026] with the standard objections can follow the argument that resolves each one.

---

## 1. Purpose and Method

A reader trained in real analysis will approach [@HOWL-MATH-21-2026] with a specific set of objections. These objections are not errors in reasoning. They follow directly from the definitions and conventions taught in undergraduate and graduate mathematics. They are the correct responses within the framework of real analysis.

This paper takes five such objections, states each in its strongest form, and applies a single test to each one. The test is base translation. The claim 0.999... = 1 is translated into base 7, and the objection is re-evaluated in that base. Base 7 is selected because it is large enough to perform readable arithmetic and small enough that the digit 9 does not exist within it.

The test applies a principle that mathematics itself requires: a valid statement about numbers must hold independent of representation. If a claim is about numbers, it must produce the same values in all bases. If it produces different values in different bases, the claim is about the representation, not about the numbers.

Each objection is evaluated on a single criterion: does it survive translation into base 7 with the same values, the same objects, and the same operations? If it does, the objection stands. If it does not, the objection fails.

---

## 2. Defining Circularity in This Context

[@HOWL-MATH-21-2026] uses the word "circular" to describe the relationship between the real number system and its treatment of repeating decimals. This word will be the first point of resistance for most readers. In formal logic, "circular reasoning" means using the conclusion as a premise. The epsilon-delta proof of the convergence of 0.999... does not do this. The proof is valid deduction.

The circularity identified in [@HOWL-MATH-21-2026] is not a logical fallacy. It is definitional self-containment. The structure is as follows:

Real analysis defines positional notation as the standard method of representing numbers. Positional notation in any base produces repeating decimals for values whose denominators have prime factors not shared by the base. This is a deficiency of positional encoding. Real analysis then defines limits as the method for resolving this deficiency. The limit definition uses the axioms of real analysis — completeness, the ordered field properties, the epsilon-delta framework — to declare that the residual left by the repeating decimal equals zero.

The system that created the problem is the same system that provides the solution. The solution uses rules that exist only within that system.

Other mathematical frameworks do not exhibit this structure. Egyptian fractions represent 1/3 exactly as 1/3 — a ratio of two integers. No positional encoding is used. No repeating expansion is produced. No limit is required. The problem that real analysis solves with the limit convention does not exist in Egyptian fractions because Egyptian fractions do not create the problem.

Finitist mathematics does not accept completed infinities. The series 0.999... as a finished infinite object is not a valid construction in finitist mathematics. Constructive mathematics requires that existence be demonstrated by construction, and the "completion" of an infinite series is not a construction in the constructive sense.

The claim 0.999... = 1 is true within real analysis. It is not true in Egyptian fractions, where the problem does not arise. It is not constructible in finitist mathematics, where completed infinity is not accepted. The claim is a property of the framework of real analysis, not a property of numbers. This is what [@HOWL-MATH-21-2026] means by "circular": the framework produces the problem, defines the rules for resolving the problem, and then uses those rules to declare the resolution exact. The claim is valid only within the system that was designed to make it valid.

---

## 3. The Five Objections

The following five objections represent the strongest standard responses to [@HOWL-MATH-21-2026]. Each is stated in the form a trained mathematician would use.

**Objection 1: Value Independence.** The notation 0.999... is base-dependent, but the value it denotes is not. The number exists independent of its representation. The notation is not the number.

**Objection 2: Same Real Number.** Both sides of the equation denote the same real number. In the real numbers, a convergent series is defined as its limit. The series and the limit are not two objects. They are one object. There is no type difference.

**Objection 3: Valid Deduction.** The epsilon-delta proof is valid deduction within a formal system. This is how all axiomatic systems work. Peano arithmetic defines natural numbers and proves theorems about them. This is not circular. It is deduction.

**Objection 4: The Theorem Is Base-Independent.** The theorem that a non-negative real number less than every positive real number equals zero is valid and base-independent. It does not reference any base. The paper's claim that "arbitrarily small" and "zero" are conflated is a mischaracterization of the theorem.

**Objection 5: Symbol Reuse.** When mathematicians write values in base 7, they use symbols that also appear in base 10. This is symbol reuse. The meaning of a digit is defined by its base context. Shared glyphs do not create conceptual dependency.

---

## 4. The Base-7 Test

The test applied to each objection is base translation. The logic of the test is as follows.

Equality in mathematics means identity. If A = B, then A and B are the same object. The same object cannot have different properties in different representations. It can have different notations, but the object itself — its value, its components, its structure — must be invariant.

The number 1 is invariant across all bases. In base 10, it is 1. In base 7, it is 1. In base 2, it is 1. In Roman numerals, it is I. No computation is required to verify this. The object is the same everywhere.

If 0.999... is a number equal to 1, then translating it into base 7 must produce the same values under the same rules. The coefficients, the partial sums, and the gaps must be the same objects written in a different notation. If they are different objects — different coefficients, different partial sums, different gaps — then the translation has not preserved the object. It has produced a different computation that arrives at the same result. A different computation that arrives at the same result is an evaluation, not an identity.

---

## 5. Objection 1 — Value Independence

**The objection:** The notation 0.999... is base-dependent, but the value it denotes is not. The value exists independent of representation. The notation is a way of writing the number, not the number itself.

**The test:** Reconstruct the value denoted by 0.999... in base 7.

The series represented by 0.999... in base 10 is:

9 × 10⁻¹ + 9 × 10⁻² + 9 × 10⁻³ + ...

In base 7, the digit 9 does not exist. The numeral 9 in base 7 is 12 (one group of 7 plus 2 units). The numeral 10 in base 7 is 13 (one group of 7 plus 3 units). The series in base 7 becomes:

12 × 13⁻¹ + 12 × 13⁻² + 12 × 13⁻³ + ...

This is a valid series. It can be evaluated. Its limit is 1. But it is no longer a repeating single-digit decimal. The compact notation "0.999..." — the form that makes the series look like a number written in positional notation — has disappeared. What remains is a multi-digit arithmetic expression. The visual form that suggested the left side was a number, rather than a computation, does not survive the base change.

The number 1, by contrast, requires no conversion. It is 1 in base 7. No series. No multi-digit coefficients. No evaluation required.

The value is base-independent. The objection is correct on this point. But the objection claims more than this. It claims that the notation is just a way of writing the number. In base 7, the notation does not write a number. It writes a computation. The identification of the notation with the number depends on base-10 encoding, which presents the computation in a form that resembles a positional decimal value. Remove the base-10 encoding, and the computation is exposed.

**Result:** The value is base-independent. The identification of the notation with the value is base-dependent. The objection fails to distinguish between these two claims.

---

## 6. Objection 2 — Same Real Number

**The objection:** Both sides of the equation denote the same real number. A convergent series is defined as its limit. There is no type difference between a convergent series and its limit. They are the same object.

**The test:** Perform the operation 1/3 × 3 in base 7 and compare the intermediate values to the same operation in base 10.

In base 10: 1/3 = 0.333... Multiply by 3: 0.333... × 3 = 0.999...

In base 7: 1/3 = 0.222... (repeating, since 7 divided by 3 gives quotient 2 with remainder 1, repeating). Multiply by 3: 3 × 2 = 6 in each position, so 0.222... × 3 = 0.666...

The partial sums in base 10 are: 0.9, 0.99, 0.999, 0.9999, ...

The partial sums in base 7 are: 6/7, 48/49, 342/343, 2400/2401, ...

These are different numbers at every step. The first partial sum in base 10 is 9/10. The first partial sum in base 7 is 6/7. These are not the same number written in different notation. They are different numbers. 9/10 ≠ 6/7.

The gap between the partial sum and 1 in base 10 at step n is 10⁻ⁿ. The gap in base 7 at step n is 7⁻ⁿ. These are different gaps at every step. 1/10 ≠ 1/7.

If both sides of 0.999... = 1 were the same number, then translating the left side into base 7 would produce the same intermediate values in different notation. It does not. It produces different values at every stage. The only thing shared between the base-10 and base-7 computations is the final evaluated limit.

Two computations that share no intermediate values but arrive at the same output are two different computations. They are not two notations for the same object. The equals sign between the series and the number 1 reports the output of a computation. This is evaluation.

**Result:** The intermediate values are different in every base. Only the final output is the same. The objection that both sides are the same real number fails the base-7 test.

---

## 6.5. The Notation Problem in the Base-7 Test

The previous section described 1/3 in base 7 as "0.222... (repeating)." This description must be examined.

The notation "0.222..." uses the digit 2, the decimal point, and the ellipsis convention to indicate repetition. All three of these elements are base-10 notational apparatus. The digit 2 is a base-10 glyph. The decimal point is a base-10 convention for separating the integer part from the fractional part in positional notation. The ellipsis "..." is a base-10 convention for indicating an infinite repeating pattern.

Base 7 does not have its own native written form in standard mathematical practice. There is no base-7 decimal point. There is no base-7 digit set that is visually or conceptually independent of base 10. Every tool used to write "0.222... in base 7" is borrowed from base 10.

This creates a problem for the test itself. The base-7 test is intended to verify whether the claim 0.999... = 1 holds independent of base-10 representation. But the test cannot be conducted without base-10 representation. The comparison between base 10 and base 7 is written entirely in base-10 notation. The base-7 values are transcribed into base-10 format in order to be examined.

This does not invalidate the results of Section 6. The intermediate values are different numbers regardless of how they are written. 6/7 and 9/10 are different values, and this can be verified by any method, including non-positional representations. But the fact that the test itself cannot escape base-10 notation is the first visible instance of the dependency that [@HOWL-MATH-21-2026] identifies in Section 5. The dependency is so complete that even an argument designed to test for base independence must be conducted within base-10 notation.

---

## 7. Objection 3 — Valid Deduction

**The objection:** The epsilon-delta proof is valid deduction within a formal system. This is how all axiomatic systems work. Peano arithmetic defines natural numbers and then proves theorems about them. Calling this circular is a misuse of the term.

**The test:** Evaluate what the proof actually proves, then determine whether other mathematical frameworks produce the same problem or require the same proof.

The epsilon-delta proof demonstrates the following: for every ε > 0, there exists a natural number N such that for all n > N, the distance between the partial sum of the series and the number 1 is less than ε. Since no positive real number can separate the series from 1, the limit of the series equals 1.

This proof is valid deduction. It is not a logical fallacy. The objection is correct on this point, and [@HOWL-MATH-21-2026] uses the word "circular" imprecisely if it is taken to mean a formal logical error.

However, the proof proves that a series evaluates to a value. It takes a function (the series), applies the limit definition, and outputs a number (1). The operation performed by the proof is evaluation: function in, number out.

The objection states that this is how all axiomatic systems work. This claim can be tested. Do other mathematical frameworks produce the same problem and require the same proof?

Egyptian fractions represent 1/3 as 1/3. The representation is exact. No series is generated. No limit is required. No epsilon-delta proof is needed. The problem that the epsilon-delta proof solves — the infinite residual left by a repeating positional decimal — does not exist in Egyptian fractions. It does not exist because Egyptian fractions do not use positional encoding.

Finitist mathematics does not accept completed infinities. The infinite series 9/10 + 9/100 + 9/1000 + ... as a finished object is not a valid construction under finitist axioms. The claim that the series "equals" anything requires the series to exist as a completed totality. Finitist mathematics does not grant this.

Constructive mathematics requires existence to be demonstrated by explicit construction. The "completion" of an infinite series — the step where infinitely many terms are treated as a finished object whose limit can be taken — is not a construction. It is a declaration licensed by the axioms of classical real analysis.

The epsilon-delta proof is valid within real analysis. It is not valid in Egyptian fraction arithmetic, where the problem does not arise. It is not constructible in finitist mathematics, where the series cannot be completed. It is not valid in constructive mathematics, where the limit operation is not a construction.

The proof is valid deduction. But it is deduction within a specific framework, and the framework is the one that produces the problem the proof resolves. Other frameworks do not produce the problem. The proof's validity is not universal. It is local to the system that requires it.

This is the definitional circularity described in Section 2. The framework creates the problem (repeating decimals from positional encoding), defines the tool for resolving the problem (limits), and uses that tool to declare the resolution exact. The proof is valid. But it proves evaluation within a specific system, not equality as a universal property of numbers.

**Result:** The proof is valid deduction. It is not a logical fallacy. But it proves evaluation, not equality, and its validity is local to a framework that both creates and resolves the problem. The objection is correct about the proof's validity and wrong about what the proof establishes.

---

## 8. Objection 4 — The Theorem Is Base-Independent

**The objection:** The theorem that a non-negative real number less than every positive real number equals zero is valid and base-independent. It does not reference any base. The original paper's claim that "arbitrarily small" and "zero" are conflated is a mischaracterization.

**The test:** Accept that the theorem is base-independent, then examine whether the objects the theorem operates on are base-independent.

The theorem is base-independent. Its statement and proof do not reference any base. This is correct.

In base 10, the theorem operates on the following objects. The partial sums are 0.9, 0.99, 0.999, and so on. The gaps between each partial sum and 1 are 0.1, 0.01, 0.001, and so on. The theorem takes these gaps, confirms that for every ε > 0 a gap smaller than ε exists, and concludes that the limit of the gaps is 0.

In base 7, the theorem operates on different objects. The partial sums are 6/7, 48/49, 342/343, and so on. The gaps are 1/7, 1/49, 1/343, and so on. The theorem takes these gaps, confirms the same convergence property, and concludes the same result.

The theorem is the same. The objects it operates on are entirely different. Different partial sums. Different gaps. Different convergence rates. The theorem accepts base-dependent inputs and produces a base-independent output.

This is the definition of evaluation. A function that accepts different inputs in different contexts and produces a consistent output is performing a computation. The theorem is the evaluation mechanism. It converts base-dependent series into base-independent values.

The objection is correct that the theorem is base-independent. But this does not support the claim that 0.999... = 1 is an equality. It supports the claim that a base-independent evaluation mechanism exists and produces consistent results. The mechanism is valid. The operation it performs is evaluation, not comparison of two identical objects.

**Result:** The theorem is base-independent. The objects it operates on are base-dependent. The theorem is an evaluation mechanism, not a proof of identity. The objection correctly identifies the theorem's validity and incorrectly concludes that this validity establishes equality.

---

## 9. Objection 5 — Symbol Reuse

**The objection:** When mathematicians write values in base 7, they use symbols that also appear in base 10. This is symbol reuse. The digit 6 in base 7 means "six units," and six units exist as a quantity independent of base 10. Shared glyphs do not create conceptual dependency.

**The test:** Express base-7 quantities without using base-10 notation, symbols, or natural language rooted in base 10.

The digit "6" in base 7 means six units. But "six" is a word from natural languages that developed their number words around base-10 counting. The glyph "6" is a Hindu-Arabic numeral designed for base-10 positional notation. The concept "six units" is expressed here using a base-10 word and a base-10 symbol.

The objection claims that the quantity six units exists independent of base 10. This is true. Six objects in a group is a quantity that exists whether or not base 10 exists. But the claim is not about whether the quantity exists. The claim is about whether the quantity can be expressed independently of base 10.

To test this: write the quantity six units in base-7 native notation. Base 7 does not have native notation. There is no base-7 writing system. There is no base-7 digit set that was developed independently of Hindu-Arabic base-10 numerals. There is no base-7 decimal point. There is no base-7 word for "six" that does not derive from a base-10 language.

Tally marks could represent six units as six marks. This is base-independent. Roman numerals represent it as VI. Egyptian notation represents it with six unit strokes. These systems are independent of base 10. But none of them are positional, and none of them produce repeating decimals. The problem that 0.999... exists to solve does not arise in any notation system that is independent of base 10.

Every positional base, as written in standard mathematical practice, borrows its symbols, its decimal point, its positional convention, and its notational framework from base 10. A mathematician writing "0.222... in base 7" is using base-10 notation to transcribe a base-7 concept. The transcription is not a translation into an independent system. It is a dialect of base 10 applied to a different modulus.

The objection states that shared glyphs do not create conceptual dependency. But the dependency extends beyond glyphs. It includes the decimal point, the positional convention, the ellipsis for repetition, the left-to-right reading order, and the natural language used to describe the quantities. No aspect of the base-7 representation is independent of base 10 as practiced in standard mathematics.

**Result:** The quantity exists independent of base 10. The notation does not. Every tool used to write base-7 values is borrowed from base 10. The objection correctly identifies that the quantity is independent but fails to demonstrate that the representation is independent. Since the original paper's claim is about representation, not about the existence of quantities, the objection does not address the claim.

---

## 10. Conclusion

Five standard objections to [@HOWL-MATH-21-2026] were tested by translating the claim 0.999... = 1 into base 7. Each objection was stated in its strongest form. Each was evaluated on whether it survived the translation with the same values, the same objects, and the same operations.

No objection survived.

Objection 1 correctly identified that the value is base-independent, but the identification of the notation with the value is base-dependent. In base 7, the notation does not resemble a number. It resembles a computation.

Objection 2 correctly identified that both sides denote the same real number by definition, but the intermediate values — partial sums, gaps, convergence rates — are different in every base. Only the final evaluated output is the same. This is the signature of evaluation, not identity.

Objection 3 correctly identified that the epsilon-delta proof is valid deduction, but the proof proves evaluation of a series to a value. Other mathematical frameworks do not produce the problem that the proof resolves. The proof's validity is local to the framework that both creates and resolves the problem.

Objection 4 correctly identified that the convergence theorem is base-independent, but the objects the theorem operates on are entirely base-dependent. The theorem is the evaluation mechanism that converts base-dependent series into base-independent values.

Objection 5 correctly identified that quantities exist independent of base 10, but no notation for positional bases exists independent of base 10 in standard mathematical practice. The dependency is not glyph-level. It is structural.

Each objection contains a valid observation. Each observation is insufficient to counter the central claim of [@HOWL-MATH-21-2026]. The claim 0.999... = 1 is a valid evaluation. The series denoted by 0.999... evaluates to 1 under the rules of real analysis. This evaluation is operationally useful and mathematically productive. It enables calculus, continuous mathematics, and the applied sciences that depend on them.

It is not equality. Equality requires that both sides be the same object. The left side is a different object in every base. The right side is the same object in every base. A relationship where one side changes and the other does not is not identity. It is evaluation, and the distinction matters.

---

## Addendum A: Clarification on Alternative Frameworks (Section 7)

Section 7 of this paper cites Egyptian fractions, finitist mathematics, and constructive mathematics as frameworks that do not produce the repeating decimal problem. A reader may object that these frameworks are not equivalent replacements for real analysis. Egyptian fractions cannot represent irrational numbers. Finitist mathematics rejects completed infinities, which disables large portions of analysis. Constructive mathematics imposes requirements on existence proofs that exclude standard results.

This objection is correct in its observations and wrong in its conclusion. The paper does not propose these frameworks as replacements for real analysis. It cites them for a single purpose: to demonstrate that the repeating decimal problem is not universal to mathematics. It is specific to frameworks that combine positional encoding with completed infinities.

Real analysis is operationally powerful. It enables calculus, continuous mathematics, and the applied sciences. The paper does not dispute this. The paper identifies one specific limitation: when real analysis uses positional encoding to represent values whose denominators have prime factors not shared by the base, it produces infinite series that require a limit convention to close the gap to the represented value. This limit convention declares epsilon equivalence to be equality. The declaration is a design choice internal to the framework.

The alternative frameworks are not cited because they are better. They are cited because they do not make this particular design choice, and therefore do not produce this particular problem. The problem is framework-specific. This is sufficient for the paper's claim.

---

## Addendum B: Revised Argument on Notational Dependency (Section 9)

Section 9 of this paper argues that base-7 notation is dependent on base-10 conventions. The original text extended this argument to natural language, claiming that the word "six" is base-10 dependent. This claim is historically false. The quantity six predates base 10. Humans counted to six before Hindu-Arabic numerals existed. The English word "six" derives from Proto-Indo-European, which had no positional number system. The quantity and the word for it are base-independent.

The dependency is not at the level of the digit or the word. It is at the level of the positional framework.

The digit 6 means six units in every context. This is base-independent. But the string 0.6 in base 7 means 6 × 7⁻¹. The string 0.06 in base 7 means 6 × 7⁻². The string 0.006 in base 7 means 6 × 7⁻³. In base 10, the same strings mean 6 × 10⁻¹, 6 × 10⁻², and 6 × 10⁻³. The digit is the same in all cases. The value it represents changes because the positional framework assigns a different power based on the base.

The decimal point, the zero padding, the left-to-right positional convention, and the rule that each position represents a successive negative power of the base are all base-10 conventions applied to a base-7 context. Base 7 has no independent notation for fractional positional values. The string "0.006 in base 7" is a base-10 transcription of a base-7 concept. It uses base-10 structure to express a base-7 value.

This cannot be resolved by choosing different symbols. The dependency is not in the glyphs. It is in the positional framework itself: the decimal point, the positional assignment of powers, and the convention that a digit's value is the product of its face value and its positional power. This framework was developed for base 10 and is applied to all other bases without modification. No base other than 10 has an independently developed positional notation system in standard mathematical practice.

The digit as a quantity is base-independent. The digit as a positional coefficient is base-dependent. Repeating decimals are constructed entirely from positional coefficients. Therefore repeating decimals are base-dependent constructions, and statements about them are statements about positional encoding, not about numbers.

The original Section 9 argument about structural notation dependency stands. The natural language argument is withdrawn.

---

## Addendum C: Historical Note on Framework Trade-offs

A reader familiar with the scope of real analysis may object to the use of Egyptian fractions as a counterexample. The objection takes the following form: Egyptian fractions are a limited system that cannot represent irrational numbers, cannot perform the operations that real analysis enables, and therefore cannot be compared to real analysis as a framework for reasoning about numbers.

This objection applies a standard selectively.

Egyptian fractions were a practical system for physical division. They represented values as sums of distinct unit fractions. Their domain was the distribution of goods: bread, land, resources. They did not have modulus. They did not need it. They were not computing sqrt(2). They did not claim to represent all values. They represented the values their domain required, and they represented those values exactly.

Egyptian fractions gave up irrational numbers because their domain did not require them. This is a trade-off appropriate to the system's purpose.

Real analysis is a practical solution to physics and continuous mathematics. It represents all real values, including irrationals, through positional encoding and limit conventions. Its scope is vastly greater than Egyptian fractions. But its positional encoding cannot finitely represent all rational values. When the denominator of a rational value has prime factors not shared by the base, the encoding produces an infinite repeating series. The limit convention closes the gap between the series and the value by declaring epsilon equivalence to be equality.

Real analysis gives up strict equality in these cases in favor of epsilon equivalence because its positional encoding cannot finitely represent all values. This is a trade-off appropriate to the system's purpose.

Both systems make a trade-off. Egyptian fractions give up scope. Real analysis gives up strict equality in specific cases. Neither system is complete in all domains. The difference is not in the existence of the trade-off. The difference is in the acknowledgment of it.

Egyptian fractions do not claim their representations cover all values. The system's limitations are visible and stated. Real analysis declares epsilon equivalence to be equality through the limit convention. The system's limitation in these specific cases is not visible. It is concealed by a notational convention that uses the equals sign for an operation that is mechanically an evaluation, not a comparison of identical objects.

The reader who dismisses Egyptian fractions as limited while defending real analysis as complete is applying different standards to the same structural issue. Both frameworks have design choices that constrain what they can represent exactly. The original paper identifies one such constraint in real analysis. The constraint is real, the trade-off is real, and the terminology used to describe the result of that trade-off — "equality" rather than "evaluation" — is imprecise.

---

## Addendum D: What the Distinction Means

The preceding sections of this paper and its companion identify a mechanical difference between two operations that mathematical notation represents with a single symbol. This addendum states the full scope of the claim and its consequences.

---

**D.1. Scope**

This paper does not dispute that the series denoted by 0.999... converges to 1 under the standard definitions of real analysis. It does not claim that the limit definition is wrong. It does not claim that calculus, continuous mathematics, or the applied sciences that depend on them are invalidated. It does not propose an alternative number system.

The paper identifies one problem: the equals sign in mathematical notation performs two mechanically distinct operations, and the notation does not distinguish between them.

---

**D.2. Two Operations**

The first operation is identity. In the equation 1 + 1 = 2, both sides refer to the same object in every representation system. In base 10, the left side is 1 + 1 and the right side is 2. In base 7, the left side is 1 + 1 and the right side is 2. In base 2, the left side is 1 + 1 and the right side is 10. The objects on both sides are preserved under translation. The numbers are the same. The operations on them are the same. Only the glyphs change. The equals sign reports that the left side and the right side are the same object.

The second operation is evaluation. In the equation 0.999... = 1, the left side is a series defined in base 10 with coefficient 9 and base 10. In base 7, the analogous statement is 0.666... = 1, which is a different series with coefficient 6 and base 7. The left side is a different function with different inputs in every base. The right side is the same object in every base. The equals sign does not report that the left side and the right side are the same object. It reports that the left side, when evaluated, produces the right side.

These two operations have different mechanical properties. Identity preserves both sides under translation. Evaluation preserves only the output.

---

**D.3. The Operational Test**

The distinction between identity and evaluation can be tested mechanically. Translate both sides of an equation into a different base.

If both sides are preserved — the same objects, the same operations, the same values at every intermediate step — the equation is identity.

If the left side is replaced by a different function with different coefficients, different partial sums, and different gaps, and only the final output is invariant, the equation is evaluation.

The equation 1 + 1 = 2 passes the identity test in every base. The equation 0.999... = 1 fails the identity test in every base other than 10. In base 7, the left side becomes a different series. In base 2, it becomes a different series. In every base, the left side is a different computation. In every base, the right side is the same number. This is the mechanical signature of evaluation.

---

**D.4. What Changes**

If the distinction between identity and evaluation were adopted in mathematical notation, no theorem would change. No proof would be invalidated. No computation would produce a different result. Every result that real analysis has produced would remain valid.

What would change is visibility. The mechanical difference between identity and evaluation currently exists in the structure of the mathematics. It is detectable by the operational test described in D.3. It is not reflected in the notation. The equals sign conceals a type conversion that occurs every time a convergent series is equated with its limit.

Making the distinction explicit in notation would make the type conversion visible. A reader would see that the left side of the equation is a function being evaluated, not a number being compared. The operation would be described accurately rather than described with a symbol that implies a different operation.

---

**D.5. What the Limit Convention Is**

The limit convention is an evaluation mechanism. It takes a convergent series as input and produces a number as output. It is licensed by the completeness axiom of the real number system. It is valid within that system. It is operationally essential to calculus, analysis, and every domain of mathematics and science that depends on continuous functions.

It is not a proof that two objects are identical. It is a procedure that converts one type of object — a function — into another type of object — a number. The conversion is well-defined, consistent, and productive. It is also a conversion, and the notation should reflect this.

---

**D.6. The Precision Claim**

The series denoted by 0.999... evaluates to 1. This is a true and useful statement. The limit convention that produces this result is valid and essential.

Calling this result "equality" is imprecise. The left side is not the same object as the right side. It is a different object in every base. It becomes the right side only after evaluation. The relationship between the series and the number is the relationship between an input and an output, not between two names for the same thing.

Calling this result "evaluation" is precise. It describes what the limit convention mechanically does. It does not diminish the convention's validity or utility. It labels the operation accurately.

This paper asks mathematics to label its own operations with the same precision it demands of its theorems. The distinction between identity and evaluation exists in the structure of the mathematics. It should exist in the notation.

---

# Addendum E: The Base Transposition Problem
## Non-Integer Bases and the Structural Limits of Positional Encoding

---

## E.1. Purpose

The preceding sections of this paper and its companion [@HOWL-MATH-21-2026] identify a base-10 dependency in positional encoding and in the notation used to write mathematical values. This addendum tests a deeper assumption: that any valid number can serve as a base for positional encoding, and that any base can be transposed to any other base.

This assumption underlies the claim that positional encoding is a universal method of representing numbers. If the assumption holds, then positional encoding is a general tool that works for all bases and all values, and its conventions — including the limit convention that resolves repeating decimals — are universal features of number representation. If the assumption fails, then positional encoding is a constrained system that works within specific boundaries, and its conventions are engineering solutions to problems created by those constraints.

Three non-integer bases are tested. Each is transposed to base 3. The test determines whether the base can be finitely defined in the target base, whether the transposition arithmetic can be performed within the target base, and whether the result is a functional positional encoding system.

---

## E.2. The Assumption

Positional encoding is treated in standard mathematical practice as a universal method. The method is as follows: choose a base b greater than 1. Define a digit set of symbols from 0 to some maximum value determined by the base. Represent any value as a series of coefficients multiplied by powers of b. The integer part uses non-negative powers. The fractional part uses negative powers. The value is the sum of the series.

This method is presented as base-independent. The choice of b is arbitrary. Any valid number greater than 1 should work. The resulting representations should be transposable between any two bases through arithmetic conversion. The values represented are numbers, and numbers are base-independent, so the system should be universal.

This assumption is rarely tested against non-integer bases. Standard mathematical practice uses integer bases almost exclusively: base 10, base 2, base 8, base 16, and occasionally others. Non-integer bases are discussed in specialized contexts but are not part of standard education or standard notation. The assumption of universality rests on a narrow range of tested cases.

This addendum tests the assumption against three cases selected to expose different failure modes.

---

## E.3. The Three Test Cases

Three bases are selected. Each tests a different aspect of the universality assumption.

**Base 6/7.** A rational number less than 1. This tests whether all rational numbers greater than zero qualify as bases for positional encoding. The value 6/7 is a valid number. If positional encoding is universal, it should function as a base.

**Base 13/7.** A rational number greater than 1 that is not an integer. This tests whether non-integer rational bases can be defined and transposed to an independent integer base. The value 13/7 is greater than 1 and should produce convergent positional powers.

**Base 1.1.** A non-integer value expressed in base-10 positional notation. This is the decimal value 11/10. This tests whether a base defined using base-10 positional notation can be transposed to a base that does not share the prime factors of 10.

All transpositions target base 3. Base 3 is selected because it shares no prime factors with 10 (the base in which 1.1 is natively expressed) and does not contain 7 as a factor (which would trivially simplify the 13/7 and 6/7 cases). Base 3 is independent of both the source bases and the notation system used to define them.

---

## E.4. Base 6/7 — Eliminated Mechanically

Base 6/7 is less than 1. In positional encoding, each position after the radix point represents a successive negative power of the base. For a base b, the first fractional position represents b⁻¹, the second represents b⁻², and so on.

For base 6/7:

(6/7)⁻¹ = 7/6

(6/7)⁻² = 49/36

(6/7)⁻³ = 343/216

The powers grow rather than shrink. Each successive fractional position represents a larger value than the previous one. The series of positional values diverges. A digit placed in the third fractional position contributes a larger quantity than a digit placed in the second fractional position. This is the opposite of what positional encoding requires. Fractional representation depends on each successive position contributing a smaller quantity so that the series converges.

No transposition is attempted because the base does not function as a positional encoding system at all. The failure is not in the transposition. The failure is in the base itself. Positional encoding requires bases greater than 1. This is a structural constraint of the method.

This constraint is rarely stated explicitly. Textbooks define positional encoding with a base b and proceed with integer examples. The requirement that b must be greater than 1 is implicit in the convergence of the geometric series but is not typically identified as a limitation of the method. It is a limitation. Not all valid numbers can serve as bases. The set of valid bases is a proper subset of the positive reals.

---

## E.5. Base 13/7 — The Base Becomes an Infinite Series

13/7 is greater than 1. Its value in base 10 is approximately 1.857. The positional powers converge:

(13/7)⁻¹ = 7/13 ≈ 0.538

(13/7)⁻² = 49/169 ≈ 0.290

(13/7)⁻³ = 343/2197 ≈ 0.156

The system is mechanically functional. The digit set contains 0 and 1, since the integer part of the base is 1. Values can be represented as series of coefficients from this digit set multiplied by powers of 13/7.

Transpose this base to base 3.

In base 3, the integer 13 is 111 (one unit of 9, one unit of 3, one unit of 1). The integer 7 is 21 (two units of 3, one unit of 1). The base can be expressed as the fraction 111/21 in base 3. This fraction is a finite, exact representation. No limit is needed to state the base as a ratio.

However, positional encoding does not use ratios. It uses positional decimals. To use base 13/7 within the positional encoding system, the base must be expressible as a positional value in the target base. This requires computing the positional expansion of 13/7 in base 3.

The computation proceeds by long division:

13 divided by 7: integer part is 1, remainder 6.

6 × 3 = 18. 18 divided by 7 = 2, remainder 4.

4 × 3 = 12. 12 divided by 7 = 1, remainder 5.

5 × 3 = 15. 15 divided by 7 = 2, remainder 1.

1 × 3 = 3. 3 divided by 7 = 0, remainder 3.

3 × 3 = 9. 9 divided by 7 = 1, remainder 2.

2 × 3 = 6. 6 divided by 7 = 0, remainder 6.

The remainder 6 appeared at the first step. The cycle repeats. The expansion of 13/7 in base-3 positional notation is:

1.212010212010... repeating with period 6.

The base itself is a repeating decimal in base 3. It cannot be finitely expressed in base-3 positional notation. To define this base in base 3 using positional encoding, you must complete an infinite repeating series. Completing that series requires the limit convention. The evaluation mechanism is needed to define the base itself before any values are written in that base.

This creates a recursive dependency. The base requires evaluation to define. Values written in the base require evaluation to compute. The limit convention is not a tool applied once to resolve a repeating decimal within an established base. It is a tool required at the foundational level to establish the base itself.

---

## E.6. Base 1.1 — Three Compounding Failures

1.1 in base 10 is the fraction 11/10. It is greater than 1. The positional powers converge:

(11/10)⁻¹ = 10/11 ≈ 0.909

(11/10)⁻² = 100/121 ≈ 0.826

(11/10)⁻³ = 1000/1331 ≈ 0.751

The system is mechanically functional. The digit set contains 0 and 1. Values can be represented as series of coefficients multiplied by powers of 11/10.

Transpose this base to base 3.

In base 3, the integer 11 is 102 (one unit of 9, zero units of 3, two units of 1). The integer 10 is 101 (one unit of 9, zero units of 3, one unit of 1). The base can be expressed as the fraction 102/101 in base 3.

Compute the positional expansion of 11/10 in base 3:

11 divided by 10: integer part is 1, remainder 1.

1 × 3 = 3. 3 divided by 10 = 0, remainder 3.

3 × 3 = 9. 9 divided by 10 = 0, remainder 9.

9 × 3 = 27. 27 divided by 10 = 2, remainder 7.

7 × 3 = 21. 21 divided by 10 = 2, remainder 1.

The remainder 1 appeared at the first fractional step. The cycle repeats. The expansion of 11/10 in base-3 positional notation is:

1.00220022... repeating with period 4.

The base is a repeating decimal in base 3. Three distinct problems compound in this case.

**First: the base requires evaluation to define.** The positional expansion of 11/10 in base 3 is infinite. The limit convention is required to complete the definition of the base. As with base 13/7, the evaluation mechanism is needed at the foundational level.

**Second: the convergence rate is impractical.** The base 11/10 is close to 1. Each positional power reduces the contribution by approximately 9 percent. For comparison, base 3 reduces each contribution by 67 percent per position. In base 11/10, ten fractional positions contribute values ranging from 0.909 down to approximately 0.385. One hundred positions are needed before the positional contribution drops below 0.0001. Any practical representation of a value in base 11/10 requires digit strings orders of magnitude longer than the same value in an integer base. The system is mechanically valid and practically unusable.

**Third: the base is a base-10 artifact.** The notation "1.1" is a base-10 positional expression. The digit 1 after the decimal point means 1 × 10⁻¹. This notation has no finite positional form in base 3. It has no finite positional form in any base that does not share the prime factors of 10 (2 and 5). The base is defined using the encoding system of base 10 and cannot be finitely restated in positional notation in most other bases. The base is not a number that happens to be written in base 10. It is a value whose finite positional expression exists only in bases compatible with 10.

---

## E.7. The Computation Dependency

A problem common to all transpositions in the preceding sections must be stated explicitly. The long division used to compute the positional expansion of each base in base 3 produces intermediate values that exceed the base-3 digit set.

Base 3 uses digits 0, 1, and 2. No value greater than 2 can be represented by a single base-3 digit.

In the transposition of 13/7 to base 3, the long division produces intermediate values of 6, 18, 12, 15, 9. None of these are base-3 quantities. The value 18, for example, requires three digits in base 3 (200). The value 6 requires two digits (20). These intermediate values appear in the steps of the division algorithm but cannot be expressed as single quantities within the base-3 digit set.

In the transposition of 11/10 to base 3, the intermediate values include 3, 9, 27, 21. The value 27 in base 3 is 1000. The value 9 is 100. These are multi-digit base-3 values that cannot be handled as single-digit quantities in the division algorithm.

The long division algorithm, as performed, uses base-10 arithmetic. The multiplication steps (6 × 3 = 18, 9 × 3 = 27) are base-10 computations. The division steps (18 divided by 7 = 2 remainder 4) are base-10 operations. The results are then transcribed into base-3 digit sequences.

The transposition does not occur between the source base and base 3 directly. It occurs from the source base through base-10 arithmetic to base 3. Base 10 is the computational intermediary. The transposition is not independent of base 10 even when neither the source base nor the target base is base 10.

To perform the transposition in base-3 arithmetic natively would require a long division algorithm that operates on multi-digit base-3 values at each step. This is possible in principle. Multi-digit arithmetic is well-defined in any base. But the standard practice of writing and performing the computation uses base-10 arithmetic throughout and then expresses the output in base-3 notation. The base-10 dependency is not in the result. It is in the process of computing the result.

---

## E.8. What the Tests Reveal

The three test cases expose four structural constraints of positional encoding.

**Constraint 1: Bases must be greater than 1.** Bases less than 1 produce divergent positional powers. The fractional positions grow instead of shrinking. Positional encoding cannot represent fractional values in a base less than 1. This excludes all positive reals between 0 and 1 from serving as bases. The set of valid bases is not the full set of positive reals. It is a proper subset.

**Constraint 2: Non-integer bases cannot be finitely defined in all integer bases.** A non-integer rational base, when expressed in positional notation in an integer base that does not share its denominator's factors, produces a repeating decimal. The base itself requires the limit convention to define. The evaluation mechanism is needed not at the level of values within a base but at the level of defining the base. This is a recursive dependency: evaluation is needed to define the system within which further evaluation occurs.

**Constraint 3: The arithmetic of transposition may exceed the target base's digit set.** The long division algorithm for computing a positional expansion in a target base produces intermediate values that may require more digits than the target base provides for a single position. The computation must be performed in a base with a sufficient digit set and the results transcribed to the target base. The computation is not performed within the target base. It is performed through a base with a larger digit set.

**Constraint 4: Base 10 serves as the universal intermediary.** In standard mathematical practice, the base with the sufficient digit set is always base 10. The notation is base 10. The arithmetic is base 10. The digit symbols are base 10. The transposition between any two bases routes through base 10 at the level of the computation itself, not just at the level of writing the result. Base 10 is not a neutral choice of notation. It is a structural dependency embedded in the arithmetic of base transposition.

---

## E.9. The Missing Tools

The constraints identified in the preceding section are not solved problems presented here as open questions. They are unsolved problems that are invisible in standard practice.

No notation exists for non-integer bases that does not depend on an integer base to define them. A non-integer base can be expressed as a ratio of two integers (13/7, 11/10), which is a finite, exact representation. But positional encoding does not use ratios. It uses positional expansions. The positional expansion of a non-integer base in a target integer base may be infinite. No convention exists for defining a base using a representation that requires the evaluation mechanism the base is supposed to support.

No method exists in standard practice for performing base transposition arithmetic entirely within the target base when intermediate values exceed its digit set. The algorithm is well-defined in principle — multi-digit arithmetic works in any base — but the standard practice of performing the computation in base 10 and transcribing the results conceals the fact that the computation has not been performed in the target base. No standard notation or pedagogy supports performing the transposition natively.

No framework exists for positional encoding that is genuinely base-independent. Every positional base borrows its notation from base 10. Every non-integer base may require evaluation to define in the target base. Every transposition computation in standard practice routes through base 10. The system is presented as universal but functions within a specific set of constraints centered on base 10.

These problems are not visible in standard practice because standard practice operates within the boundaries where the system works: integer bases greater than 1, with all notation and arithmetic in base 10. The problems become visible only when the assumption of universality is tested against cases the system was not designed to handle. The three test cases in this addendum are such cases. They are valid numbers used as bases and transposed to a valid target base. The system fails at the level of defining the base, at the level of performing the arithmetic, and at the level of writing the results.

---

## E.10. Connection to the Original Claim

The original paper [@HOWL-MATH-21-2026] identifies a specific problem: the equals sign in 0.999... = 1 performs evaluation, not equality. The left side is a base-dependent series. The right side is a base-independent number. The limit convention converts one to the other. This conversion is valid and useful but is not equality in the strict sense.

This addendum identifies the same problem at a deeper level. The limit convention is not only used to resolve repeating decimals within an established base. It is used to define non-integer bases themselves when those bases are expressed in positional notation in a target base. The evaluation mechanism operates at the foundational level of the encoding system, not just at the level of individual values.

The base-10 dependency identified in [@HOWL-MATH-21-2026] is not limited to notation. It extends to the arithmetic of transposition. The computation required to convert between bases routes through base 10 in standard practice. The intermediate values in the computation exceed the digit sets of small target bases and must be handled in a base with a larger digit set. In practice, that base is always base 10.

The assumption that positional encoding is universal — that any base is valid and any base is transposable to any other — is false in the general case. It holds for integer bases greater than 1, with the caveat that all notation and arithmetic are conducted through base 10. It fails for bases less than 1, which are mechanically excluded. It fails for non-integer bases, which may require infinite series to define in the target base. And even where it holds, the computation is not base-independent. It is dependent on base 10 at every level.

The 0.999... problem is the surface-level symptom. The structural limitations of positional encoding — constrained valid bases, recursive evaluation dependencies, computation routing through base 10 — are the underlying condition. The original paper identifies the symptom. This addendum identifies the condition. They are the same problem at different depths.

