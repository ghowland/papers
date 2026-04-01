# DATA-2: What It Is and What It Tells Us

## What Was Built

A database of 107 precision values — every number the HOWL series touches — converted into the Q335 integer rational basis. Each value v becomes a single integer numerator (round(v × 2³³⁵)) over the shared denominator 2³³⁵. The reconstruction is verified against the original to all source digits. 17 entries reconstruct with exactly zero error (integers and terminating decimals). The rest reconstruct with relative errors 60-100 orders of magnitude below their measurement uncertainty.

The database covers seven sections: SI defined constants (7 entries, all exact), measured fundamental constants (13 entries, CODATA 2022), electroweak observables (12 entries, LEP/PDG), quark masses and CKM (11 entries including lattice ratios), nuclear and hadron masses (8 entries), atomic spectroscopy and clocks (6 entries), analytical constants (17 entries at 105 digits), defined reference values (9 entries), optical disc specs (10 entries), fiber optic data (4 entries), and dimensionless mass ratios (9 entries).

This is the complete numerical foundation for every computation going forward. Every value is a Fraction. Every operation is exact integer arithmetic.

## What Was Tested

Three tests beyond the conversion itself.

**Test 1: Q335 factorization.** For each numerator, extract all prime factors ≤ 997 and measure the remaining cofactor. Result: every measured fundamental constant has a cofactor of 89-106 digits — essentially the full numerator. Small-prime extraction pulls out at most a handful of factors (2² from m_p/m_e, 2 × 11² × 13 × 47 from a_e) and leaves a number indistinguishable from a random 100-digit integer. The measured constants have no compact Q335 representation.

The five fully-factored entries (m_s, m_c, m_b, A4 = 440 Hz, CD sample rate = 44100 Hz) are all either human-defined integers or quark masses at 3-4 sig figs where the last digit carries uncertainty of ±4 to ±8. A different measurement would give different primes. These factorizations are artifacts of notation, not physics.

**Test 2: Multi-base scan.** The same conversion repeated in 19 bases — primes 2 through 37 plus composites 6, 10, 12, 30, 42, 60, 210. For each entry in each base, the cofactor size is recorded and the "best base" identified.

Base 10 wins for 33 of 54 tested entries (61%). This is entirely a notation artifact: every measured value is published as a terminating decimal, so multiplying by 10¹⁰⁰ gives zero waste by construction. It tells us what journals use for notation, not what the universe prefers.

Composite bases (60⁵⁰, 210³⁸) show systematic improvement over single-prime bases: 13-15 fewer digits in the cofactor on average. R₂ = π/4 shows the largest improvement in base 60 (23 digits). π shows the largest improvement in base 210 (21 digits).

**Test 3: Control test.** 90 generic irrationals (√primes, ∛primes, ln primes, log ratios, Bessel/Airy/erfc/Gamma values) through the same multi-base scan. Result: z-scores of 0.77 (base 60) and 1.80 (base 210). Neither exceeds 2. The physics constants show the same composite-base improvement as generic irrationals. The effect is a mathematical property of composite denominators (more small prime factors create more opportunities for partial cancellation), not a signal from physics.

**Continued fraction analysis.** No measured fundamental constant has an anomalously large partial quotient or a suspiciously good small-denominator rational approximation. α⁻¹ has CF = [137; 27, 1, 3, 1, 1, 18, ...] — the "famous" 137 is just the integer part, nothing special in the CF structure. m_p/m_e has CF = [1836; 6, 1, 1, 4, ...] — generic.

The one notable CF result: the Koide ratio K = 0.666660511... has CF = [0; 1, 1, 1, 18050, ...]. The partial quotient a₄ = 18050 is anomalously large, encoding the fact that the convergent 2/3 approximates K to one part in 108,000. This is the CF quantification of the Koide formula's precision. If m_τ measurements improve and K stays at 2/3, that partial quotient grows. If K deviates, it shrinks. The CF is the natural language for tracking Koide over time.

## What It Means

Three things are now established at the level of the numbers themselves.

**The Q335 basis is validated.** No alternative base reveals structure that Q335 hides. The control test kills the composite-base signal. The choice of 2³³⁵ — made in MATH-4 for computational convenience — is confirmed as having no physics disadvantage relative to any other base tested.

**The measured constants are structureless in every representation tested.** This extends the DISC-9 boundary. The 72/72 PSLQ null showed no linear combinations with the transcendental basis. DATA-2 shows no compact rational representations in any of 19 bases, no anomalous CF structure, and no small-prime factorization patterns. The Level 2 parameters are as structureless as random numbers in the rational number system.

**The transport is exact.** Every value in the database can be loaded as a Python Fraction and operated on with zero rounding error to the full source precision. This is the operational foundation: any computation this session — Z-pole observables, Koide rechecks, overconstrained extractions — draws from this database with guaranteed exactness.

## What I Notice

The m_e entry uses 0.51099895069 MeV at 11 digits. That's the CODATA 2022 value. The precision fix from the planning material is already done — the previous session's 8-digit value has been updated. Similarly, sin θ₁₂ = 0.22501 (PDG 2024), sin θ₂₃ = 0.04182, sin θ₁₃ = 0.003685 — all updated. The lattice ratios m_c/m_s = 11.783, m_b/m_c = 4.578, m_u/m_d = 0.485 are included. The precision updates from the planning material appear to be incorporated.

The LEP observables are loaded: σ⁰_had = 41.481 nb, R_l = 20.767, R_b = 0.21629, A_FB^l = 0.0171, A_l = 0.1513, N_ν = 2.9840, G_F, M_Z, Γ_Z, M_W, m_t, m_H. These are the inputs AND targets for the overconstrained electroweak computation.

The Koide ratio is computed from the updated masses: K = 0.666660511... The CF a₄ = 18050 gives the distance to 2/3 = 0.666666... The difference K − 2/3 = −0.0000061... at 6 sig figs, consistent with the 0.91σ tension from PHYS-8.

The database is ready. What do you want to compute first?

