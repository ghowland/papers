**Video 5 Outline: The Number System Physics Should Have Been Using All Along — Fractions Beat Decimals**

---

**Opening — in frame, the core claim (1 minute)**

- This video is about the single innovation in the entire model
- Not a physics innovation, an engineering innovation
- The entire Rational Universe Model runs on one insight: stop converting integers to decimals
- Sounds trivial, it's not, this one change is why everything works

**The problem stated simply (3 minutes)**

- Physics produces integers, the gauge group counts particles, the counts are exact
- 41/10, negative 19/6, negative 7, these are the three running rates
- The 41 counts charge contributions of every particle in the Standard Model
- The denominators come from symmetry normalization
- These fractions are as exact as the number 3
- But the first thing every computation does is convert to decimal
- 41/10 becomes 4.1, which counts nothing, the 41 is gone, the 10 is gone
- Show terminal — here's 41/10 in Python as a Fraction, here's 41/10 as a float, they look similar but they're fundamentally different objects
- The Fraction remembers that it's 41 over 10, you can ask for the numerator and get 41, you can ask for the denominator and get 10
- The float is just a location on the number line, you can't recover the 41 or the 10 from 4.1
- That difference propagates through every computation

**The bread metaphor — make it physical (2 minutes)**

- A grandmother has a loaf with 10 slices and 9 mouths at the table
- She counts in integers, one per mouth, one wrapped in cloth for the person who said they'd eaten enough but hadn't
- Zero remainder, exact distribution, everyone fed
- The accountant says point-three-three-three repeating means the third person bears the cost
- She says I've been dividing bread for 67 years and nobody went without
- The decimal creates a remainder that doesn't exist in the bread
- Physics does the same thing, creates remainders by converting to decimals that don't exist in the integers
- The loss isn't real, it's an artifact of the number system

**Fraction arithmetic in practice (4 minutes)**

- Show terminal — live demonstration of fraction arithmetic
- Start with the three beta coefficients as Fractions
- Compute the gap ratio step by step, show each intermediate result is still a Fraction
- Show that the numerators and denominators carry physical meaning at every step
- 218/115 for the Standard Model, 38/27 with the Cabibbo Doublet
- Show the factorizations: 38 equals 2 times 19, where 19 is the weak force count, 27 equals 3 cubed, the cube of color charges
- Now do the same computation in floating point
- Show terminal — same computation with floats, same intermediate steps
- The results look similar, the decimal representations are close
- But the float result is 1.40740740740741, you can't see that the exact value is 38/27
- The structure is invisible in the decimal, the meaning is erased
- Show terminal — ask the Fraction for its numerator, get 38, ask the float for its numerator, error, it doesn't have one

**Where the precision loss enters (3 minutes)**

- In a short computation the difference is negligible
- But physics derivation chains are long, the QED series has five terms each with multiple transcendental constants
- Each term is an exact rational coefficient times a transcendental
- 197/144 plus 1/12 times pi squared minus 1/2 times pi squared times ln 2 plus 3/4 times zeta 3
- Show terminal — here's the A2 coefficient assembled in exact arithmetic, show each piece
- In floating point each multiplication loses a bit of precision, each addition loses a bit more, by the end of a five loop computation the accumulated error is significant
- In fraction arithmetic the rational coefficients never lose precision, they're exact at every step
- The only imprecision is in the transcendental constants, and that's where Q335 comes in

**Q335 — the engineering solution (4 minutes)**

- Pi is transcendental, proven in 1882, cannot be written as a ratio of integers
- But pi can be computed to any number of digits
- The Planck length is the smallest meaningful distance, knowing pi to 35 digits lets you compute the circumference of the observable universe to within one Planck length
- Q335 uses 335 binary digits, that's 101 decimal digits, 65 digits beyond the Planck threshold
- Show terminal — here's pi in Q335, here's the numerator, it's a 101 digit integer, here's the denominator, 2 to the 335th
- The difference between Q335 pi and true pi is less than 10 to the negative 100
- No experiment theoretically possible could detect the difference
- Show terminal — compute the difference, show it's zero to 100 decimal places
- The denominator being a power of 2 matters for hardware, division by 2 to the 335th is a bit shift, free in silicon
- Every transcendental constant in physics gets the same treatment: zeta 3, zeta 5, ln 2, Catalan constant, elliptic integrals
- Show terminal — here's the Q335 basis, show a few constants, show the precision of each
- 35 constants verified, all exact to 100 plus digits, all stored as integers over 2 to the 335th

**The PSLQ null — derivation beats search (2 minutes)**

- Before settling on Q335 I tested whether any compact integer relations exist between the transcendental constants
- PSLQ is an algorithm that searches for integer linear relations between real numbers
- If pi and zeta 3 and ln 2 were secretly related by some simple integer formula, PSLQ would find it
- Show terminal — the PSLQ results if available, or describe them
- 82 tests, zero relations found, all null
- The transcendental constants are independent, there's no shortcut, no hidden integer formula connecting them
- Derivation beats search, you compute them to high precision and store them, you don't find a magic relation
- This is published as MATH-6, the 82/82 independence record

**The computation pipeline — how it all flows (3 minutes)**

- Show terminal — walk through a complete derivation pipeline
- Inputs enter as exact Fractions from the value pool, show a few entries with their types
- The computation proceeds in Fraction arithmetic, show an intermediate step
- Transcendental constants enter as Q335 Fractions, show one being loaded
- The entire chain runs without a single decimal, show the running computation
- At the very end, the final result is converted to a decimal string for comparison against the measured value
- Show terminal — here's the final output, here's the measured value, here's the digit by digit comparison
- The decimal is the test, the fraction is the physics
- Every step is traceable, every value has provenance, every intermediate result is inspectable
- Show terminal — use data7.py info on a result value, show the source, the type, the tags

**The type system — exact versus approximate (2 minutes)**

- Every value in the pool is typed as either exact_fraction or approximate
- Show terminal — data7.py info on an exact value, show value_type exact_fraction, show the Fraction representation
- Show terminal — data7.py info on an approximate value, show value_type approximate, show it's a decimal with a source
- The type tells you at every point in the pipeline whether you're working with an exact integer ratio or a measured approximation
- When a derivation fails, you can trace back and find exactly where exact stops and approximate begins
- The hadronic VP delta, 220393 over 50000, typed exact_fraction because the fraction is exact, the value it represents carries uncertainty of plus or minus 0.010
- The system distinguishes between a fraction that is exact and a value that is exact, those are different things
- This level of type discipline doesn't exist anywhere in standard physics computation

**What the number system reveals (2 minutes)**

- When you preserve the integers, patterns become visible that decimals hide
- The gap ratio 38/27 is invisible as 1.40741 but obvious as a fraction
- The QED coefficient A2 decomposes into rational plus number-theoretic plus geometric pieces with 87 percent cancellation, invisible in decimals, obvious in fractions
- The beta coefficients tell you exactly how many particles contribute to each force, invisible in decimals, obvious in fractions
- The number system isn't neutral, it's a lens, decimals are a blurry lens that works well enough for calculation, fractions are a sharp lens that reveals structure
- Physics chose the blurry lens 400 years ago and never switched
- This model switched, everything followed

**Close — in frame, talking to camera (1 minute)**

- The single innovation: don't convert integers to decimals until the last step
- Q335 handles the transcendentals at 65 orders of magnitude beyond physical reality
- The type system tracks exact versus approximate through every computation
- The decimal is the test, the fraction is the physics
- This isn't a philosophical argument about the nature of numbers
- It's an engineering decision that produces 15 digit matches and 253 passing comparisons
- The grandmother knew, every crumb is bread, you don't throw away the remainder because the remainder is the piece someone needs
- Next week: I built a test suite for physics and everything passed
- Links in pinned comment, check the numbers

---

**Estimated runtime: 25 to 30 minutes**

This is the most terminal-heavy video in the series. Almost every section has a live demonstration. The viewer watches fraction arithmetic happening in real time, sees the difference between Fraction and float objects, sees Q335 pi computed and compared, sees the derivation pipeline flowing from input to output without a single decimal until the final step. This is the video where the methodology becomes tangible, where the viewer sees the tool doing the work.

The arc moves from problem through insight through implementation through consequence. The bread metaphor grounds it in intuition. The live arithmetic proves it works. The type system shows the discipline. The closing connects back to what the viewer cares about: 253 comparisons pass because the number system preserves the information that matters.
