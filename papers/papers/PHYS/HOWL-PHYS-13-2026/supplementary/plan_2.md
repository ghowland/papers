## Paths Forward from DATA-3

**Path 1: sin²θ_W from 3/8 + Running**
Priority: HIGH. Effort: 1-2 hours.

The SU(5) GUT predicts sin²θ_W = 3/8 = 0.375 at the unification scale. The one-loop beta functions run the three gauge couplings from M_GUT down to M_Z. The beta coefficients are exact rationals from the gauge group: b₁ = 41/10, b₂ = −19/6, b₃ = −7. The running uses ln(M_GUT/M_Z) as a single parameter. PHYS-5 already built the infrastructure for coupling running in Fraction arithmetic.

This computation produces a concrete number: the SM prediction of sin²θ_W(M_Z) from the GUT boundary condition 3/8. The one-loop SM result is ~0.207, which misses the measured 0.23122. The SIZE of the miss quantifies exactly how much threshold corrections or BSM content is needed. This connects directly to the gap ratio 218/115 vs 1.395 from PHYS-5 — the same unification failure seen from a different angle.

Why high priority: uses existing infrastructure, produces a falsifiable number, pairs naturally with Path 2, and extends PHYS-5 into new territory. The integer content (beta coefficients from the gauge group) is exactly the kind of structure HOWL is designed to expose.

**Path 2: Gap Ratio Particle Content Enumeration**
Priority: HIGH. Effort: 1-2 hours.

PHYS-5 found (b₁−b₂)/(b₂−b₃) = 218/115 for the SM versus 1.395 from measured coupling convergence. What minimal BSM particle content shifts the ratio to 1.395?

Each new multiplet in representation (R₃, R₂, Y) contributes known rationals (Δb₁, Δb₂, Δb₃). A scalar SU(2) doublet contributes (1/10, 1/6, 0). A vector-like quark doublet contributes different rationals. Enumerate all single-multiplet extensions with dimension ≤ 10 under each gauge factor and check which gives a gap ratio within 1% of 1.395. The MSSM answer (complete superpartner spectrum) is known to approximately unify — does anything simpler work?

This is a finite search over a bounded set of quantum number assignments. Every computation is exact rational arithmetic. The output is a table: each candidate BSM multiplet and its predicted gap ratio.

Why high priority: pairs with Path 1 (same physics, complementary questions). Path 1 asks "how badly does the SM miss?" Path 2 asks "what fixes it?" Together they form a coherent extension of PHYS-5 into gauge unification.

**Path 3: A₂ in R₂/R₄ Form**
Priority: MEDIUM. Effort: 30 minutes.

The QED 2-loop coefficient A₂ = 197/144 + π²/12 + (3/4)ζ(3) − (π²/2)ln(2). Substituting π² = 32R₄:

A₂ = 197/144 + (3/4)ζ(3) + R₄(8/3 − 16 ln 2)

The geometric content (R₄ term) contributes −2.60. The number-theoretic content (ζ(3) term) contributes +0.90. The rational part contributes +1.37. Total: −0.328. The geometric piece dominates in magnitude and has opposite sign — there's a large cancellation between geometry and number theory that makes A₂ small.

This is a 10-line computation in Fraction arithmetic using the Q335 numerators from DATA-3. The decomposition connects to the Brown-Schnetz program on Galois coactions in perturbative QFT, where the separation of geometric (period) content from arithmetic (motivic) content is studied systematically. Stating the decomposition in the HOWL language makes the connection explicit.

Why medium priority: quick, clean, publishable as a structural observation, but not a parameter reduction. It's a finding about the anatomy of QED, not about the Standard Model's free parameters.

**Path 4: Bessel Zeros PSLQ**
Priority: MEDIUM. Effort: 30 minutes.

DATA-3 contains j₁₁ = 3.83171 and j₀₁ = 2.40483 at 105 digits. These enter every diffraction pattern and fiber optic cutoff. The 72/72 PSLQ null from DISC-6-9 tested SM parameters against the transcendental basis but did NOT test Bessel zeros.

Run PSLQ on j₁₁ and j₀₁ against the extended transcendental basis {π, e, ln 2, √2, √3, φ, ζ(3), ζ(5), ...} at 100 digits with maxcoeff 10000. Same protocol as DISC-7. Bessel zeros are known transcendental (Siegel 1929) but algebraic independence from π is not proven.

Expected result: null. But at 100 digits with maxcoeff 10000, a null is a strong statement. If positive (a relation exists), it's a mathematical discovery publishable independently of HOWL.

Why medium priority: cheap test, expected null, closes a gap in the independence results. Doesn't advance the physics but completes the mathematical foundation.

**Path 5: Write DISC-9 Capstone**
Priority: MEDIUM. Effort: 2-3 hours.

The boundary paper: Level 1 (structure determined by geometry) versus Level 2 (parameter values supplied by the universe). This is the intellectual capstone of the 20-paper series.

Evidence for the boundary: R₂ in 9/9 physics domains (PHYS-11), three irreducible subgroups, θ_QCD = 0 derived (PHYS-7), Koide conditional (PHYS-8), α from a_e at 4.3 ppb (PHYS-9), 72/72 PSLQ null (DISC-6-8), DATA-2/3 multi-base null, DATA-3 lattice ratio independence, EW overconstrained system showing integer transformation laws with measured-value inputs.

The paper states what geometry determines (which R_n appears, moduli, ground states, transformation law coefficients) and what it doesn't (coupling values, masses, mixing angles). The boundary IS the result.

Why medium priority: the content is ready and the picture is stable. But it's a writing task, not a computation. It doesn't produce new findings — it organizes existing ones. Should be written when the computational paths are exhausted.

**Path 6: Database Consistency for EW Computation**
Priority: LOW-MEDIUM. Effort: 30 minutes.

The EW overconstrained computation (14/14 pass) used DATA-2 inputs. Now that DATA-3 is declared, rerun the EW computation referencing DATA-3 explicitly and verify all 14 checks still pass. This is a formality — the numbers are identical — but it closes the provenance chain: DATA-3 → EW computation → results.

Why low-medium: pure bookkeeping, no new physics. Do it when writing up the EW paper.

**Path 7: Full Δr for M_W**
Priority: LOW. Effort: 3-4 hours.

Replace Δρ with the full radiative correction Δr = Δα − (cos²θ/sin²θ)Δρ + remainder. The Δα part is the running of α from 0 to M_Z, already computed in PHYS-5. This would bring M_W from 0.05% to ~0.01%, matching experimental precision. But as argued previously, this is an epicycle — it polishes an existing result without revealing new structure.

Why low: the tree + Δρ computation already proved the point. The integer anatomy is visible. Adding one-loop corrections adds more integers from the same gauge group. No new structural finding expected.

**Path 8: Neutrino Mixing Angles**
Priority: LOW. Effort: 1 hour.

The PMNS mixing angles (sin²θ₁₂ ≈ 0.307, sin²θ₂₃ ≈ 0.545, sin²θ₁₃ ≈ 0.022) are close to tribimaximal values (1/3, 1/2, 0). Test these against the transcendental basis at their published precision (2-3 sig figs). The precision is too low for meaningful PSLQ, but the proximity to simple fractions can be quantified using continued fractions.

Why low: 2-3 sig fig precision makes any pattern search weak. The proximity to 1/3 and 1/2 is known and has been extensively studied in the flavor symmetry literature (A₄, S₄ groups). We'd be documenting what's known, not finding anything new.

## Recommended Sequence

1. **Paths 1+2 together** — sin²θ_W from 3/8 + running, then gap ratio enumeration. Same physics, paired naturally. Produces concrete numbers that extend PHYS-5. (2-3 hours)
2. **Path 3** — A₂ decomposition. Quick, independent, can be done in a break between larger computations. (30 min)
3. **Path 4** — Bessel PSLQ. Also quick and independent. (30 min)
4. **Path 5** — DISC-9 capstone. When the computational paths are done and the picture is final. (2-3 hours)
5. Paths 6-8 as time permits or as needed for completeness.

