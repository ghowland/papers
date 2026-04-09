## MATH-9 Plan: The One-Loop Degeneracy Theorem

**Registry:** [@HOWL-MATH-9-2026]

**Status:** Plan for review

---

### Thesis

The one-loop renormalization group equation for the α₁-α₂ crossing contains zero information about sin²θ_W. The crossing equation reduces algebraically to the identity s = s for any value of sin²θ_W, any particle content, and any GUT normalization. This is not a numerical accident or a fine-tuning problem — it is a structural property of one-loop RGE: the two couplings α₁ and α₂ are both linear functions of sin²θ_W × α_em⁻¹, and their difference eliminates both sin²θ_W and α_em simultaneously, leaving a tautology.

The theorem applies to every BSM model that attempts to predict sin²θ_W from one-loop gauge coupling unification. The prediction is impossible at one loop. Two-loop effects (where the off-diagonal b_ij matrix breaks the proportionality) are required. This result has been known implicitly — no published one-loop GUT prediction of sin²θ_W exists — but the algebraic proof has not been stated explicitly, and the structural reason (linear dependence on sin²θ_W × α_em⁻¹) has not been identified as the mechanism.

---

### Why This Needs a Paper

Three reasons:

**1. The textbook claim is misleading.** GUT textbooks state sin²θ_W = 3/8 at M_GUT and note that running it down to M_Z gives "approximately 0.21" at one loop. This creates the impression that one-loop running predicts sin²θ_W. It doesn't. The 3/8 is the boundary condition at M_GUT, not a prediction. To predict sin²θ_W at M_Z, you need to find M_GUT from the crossing, then run down. The crossing step is where the degeneracy kills the prediction. What textbooks actually do is use the measured sin²θ_W to determine the couplings at M_Z, run them up, and check if they meet — this tests unification but does not predict sin²θ_W.

**2. Three failed computational attempts preceded the proof.** The HOWL series attempted sin²θ_W prediction from one-loop unification three times: iterative feedback (diverged to 10²¹), algebraic three-way crossing (sin²θ_W = 0.43 at M_GUT = 10³²), and self-consistent iteration (converged to trivial solution sin²θ_W = 3/8, L = 0). Each failure was diagnosed separately. The algebraic proof unifies all three failures as consequences of the same structural degeneracy. The paper presents the proof, then shows how each failed attempt maps to a specific pathological behavior of the identity.

**3. The theorem has practical consequences.** Any future BSM model claiming sin²θ_W prediction from gauge coupling unification MUST use two-loop (or higher) running. One-loop predictions of sin²θ_W are structurally impossible, not just numerically imprecise. This is a constraint on the GUT program that should be stated as a theorem, not left as folklore.

---

### The Proof (Core)

Start from standard GUT-normalized couplings at M_Z:

α₁⁻¹(M_Z) = k₁(1 − s)A

α₂⁻¹(M_Z) = sA

where s = sin²θ_W, A = α_em⁻¹, k₁ = 3/5 (GUT normalization).

One-loop running: α_i⁻¹(μ) = α_i⁻¹(M_Z) − (b_i/2π)L, where L = ln(μ/M_Z).

The 1-2 crossing condition: α₁⁻¹(M_GUT) = α₂⁻¹(M_GUT).

This gives: k₁(1−s)A − (b₁/2π)L = sA − (b₂/2π)L

Rearranging: L = 2πA[k₁(1−s) − s] / (b₁ − b₂)

Now attempt to extract s from the crossing. The sin²θ_W formula from the 1-2 crossing is:

s = k₁/(1+k₁) − (1/(2A(1+k₁)))(b₁ − b₂)L

which for k₁ = 3/5 gives s = 3/8 − (5/(8A))(b₁ − b₂)L.

Substitute the expression for L:

s = 3/8 − (5/(8A))(b₁ − b₂) × 2πA[k₁(1−s) − s] / (2π(b₁ − b₂))

The (b₁ − b₂) cancels. The 2π cancels. The A cancels:

s = 3/8 − (5/8)[k₁(1−s) − s]

s = 3/8 − (5/8)[(3/5)(1−s) − s]

s = 3/8 − (5/8)[(3/5) − (3/5)s − s]

s = 3/8 − (5/8)[(3/5) − (8/5)s]

s = 3/8 − (3/8) + s

s = s ∎

The cancellation is complete. No information about s remains. The equation is satisfied for all s.

---

### Generalization

The proof generalizes to arbitrary k₁. For any GUT normalization k₁:

α₁⁻¹ = k₁(1−s)A, α₂⁻¹ = sA

The crossing gives L = 2πA[k₁(1−s) − s]/(b₁ − b₂)

The extraction formula is s = k₁/(1+k₁) − (1/(2A(1+k₁)))(b₁−b₂)L

Substituting: s = k₁/(1+k₁) − (1/(1+k₁))[k₁(1−s) − s]

s = k₁/(1+k₁) − k₁(1−s)/(1+k₁) + s/(1+k₁)

s = [k₁ − k₁ + k₁s + s]/(1+k₁)

s = s(k₁+1)/(1+k₁)

s = s ∎

The identity holds for ALL k₁. It also holds for ANY particle content (the betas cancel). The degeneracy is a property of the linear relationship between α₁⁻¹, α₂⁻¹ and sin²θ_W, not of specific beta values or normalization conventions.

---

### Structure

**Section I: The Claim.** State the theorem: one-loop RGE cannot determine sin²θ_W from the α₁-α₂ crossing. The crossing equation is an identity. One-loop sin²θ_W "predictions" in the GUT literature are actually backward calculations (measured sin²θ_W → couplings → run up → check if they meet).

**Section II: The Proof.** Present the algebraic proof for general k₁. Ten steps, each exact. The cancellation of (b₁ − b₂), 2π, and A is shown explicitly at each step. The result s = s is unavoidable.

**Section III: Why It's an Identity.** The structural explanation: α₁⁻¹ and α₂⁻¹ are both proportional to A = α_em⁻¹. Their difference eliminates A. But sin²θ_W enters only through the combination sA (for α₂) and k₁(1−s)A (for α₁). When A is eliminated, s goes with it. The two couplings carry exactly one independent piece of information (the combination k₁(1−s)/s = α₂/α₁), and this ratio determines L but not s individually.

An alternative way to see it: at one loop, the three couplings at any scale form a triangle in coupling space. The triangle's shape is determined by the beta ratios (the gap ratio). Changing sin²θ_W doesn't change the shape — it rescales all three couplings simultaneously (through A). The crossing point slides along a line of constant shape. The shape determines L (the crossing scale) but not s (the overall scale factor).

**Section IV: Three Failed Attempts.** Present each attempt from PHYS-39 as a consequence of the identity:

Attempt 1 (iterative): start from s = 3/8, compute L, compute new s. The identity means the "new s" formula returns whatever s you put in. But with numerical noise, the iteration amplifies errors (the formula is s → s + noise, iterated). Result: divergence to 10²¹.

Attempt 2 (algebraic three-way): force α₁ = α₂ = α₃ at one loop. The 1-2 crossing gives the identity (no constraint on s). The 2-3 crossing gives a second equation that does constrain s — but the constraint uses α₃ (which depends on α_s, an independent measurement). The "algebraic" solution sin²θ_W = 0.43 at M_GUT = 10³² is the solution of the 2-3 crossing constraint alone, with the 1-2 crossing providing no additional information. The non-physical result (sin²θ_W too high, M_GUT above Planck) comes from forcing exact three-way meeting at one loop, which overcounts the degrees of freedom.

Attempt 3 (self-consistent): start from s = 3/8, iterate to self-consistency. The identity means EVERY starting s is self-consistent. The iteration converges in one step to whatever you start with. Starting from 3/8 gives 3/8, L = 0, M_GUT = M_Z. The "trivial fixed point" is not a bug — it's the theorem saying the equation has no information.

**Section V: What Two-Loop Fixes.** At two-loop, the RGE becomes:

dα_i⁻¹/dt = −b_i/(2π) − Σ_j b_ij α_j/(8π²)

The off-diagonal terms b_ij couple the three couplings. α₁⁻¹ and α₂⁻¹ are no longer both linear in sA — the α₃-dependent terms break the proportionality. The crossing equation at two-loop contains genuine information about s because the b_ij matrix mixes the three couplings in a way that depends on their individual values, not just their ratio.

The CD two-loop result: sin²θ_W = 0.231223 at 12 ppm. The one-loop result: s = s (identity). The difference is entirely from the b_ij off-diagonal coupling. The 12 ppm prediction is a two-loop effect.

**Section VI: Consequences for GUT Model Building.** Any BSM model claiming to predict sin²θ_W must specify its two-loop beta matrix, not just its one-loop betas. One-loop betas determine whether couplings unify (the gap ratio) and where (M_GUT). They do not determine what value sin²θ_W takes at M_Z. This is a constraint on model evaluation: the gap ratio and M_GUT are one-loop quantities; sin²θ_W is a two-loop quantity. Comparing BSM models on their sin²θ_W predictions requires comparing their b_ij matrices, not their b_i vectors.

---

### Appendix Tables

A.1: The algebraic proof — all ten steps for general k₁, with intermediate expressions

A.2: Three failed attempts — starting conditions, iteration behavior, final result, diagnosis mapped to the identity

A.3: One-loop vs two-loop information content — what each level of the RGE determines

A.4: The b_ij matrix — SM and CD values, showing which off-diagonal entries break the degeneracy

A.5: Published one-loop "predictions" of sin²θ_W — showing that each is actually a backward calculation from measured sin²θ_W, not a forward prediction

---

### What This Paper Does NOT Do

It does not claim the one-loop degeneracy is unknown. GUT practitioners know that one-loop running doesn't precisely predict sin²θ_W — the textbook value "~0.21" is understood to be approximate. What the paper claims is that the imprecision is not numerical (rounding, truncation, approximation) but algebraic (the equation is an identity). The distinction matters: numerical imprecision suggests a better calculation would help. Algebraic identity means no calculation at one loop will ever help. The information is structurally absent.

It does not claim two-loop predictions are exact. The two-loop prediction (12 ppm for CD) still depends on the specific b_ij matrix values. Three-loop corrections would shift the prediction further. The claim is that the transition from "zero information" to "12 ppm prediction" happens at the one-loop to two-loop boundary, and the mechanism is the off-diagonal b_ij coupling.

---

### Estimated Length

Main text: 5-6 pages. The proof is short (one page). The structural explanation is one page. The three failed attempts are one page. The two-loop fix is one page. The consequences are one page. Appendix: 5 tables. One figure: the coupling triangle at one loop showing how rescaling s slides the triangle without changing its shape.

---

### Agreement Request

Is the scope right? The theorem is clean and provable. The connection to the three failed attempts gives it narrative grounding. The consequence for GUT model building gives it broader relevance. Should the paper include the generalization to arbitrary gauge groups (SU(N) × SU(M) × U(1)), or is SU(3) × SU(2) × U(1) sufficient?
