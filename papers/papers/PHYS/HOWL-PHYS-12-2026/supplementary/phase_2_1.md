Here's what the Koide derivation attempt found:

---

## What Was Attempted

The goal was to derive WHY the Koide amplitude a = √2, which would make the m_τ prediction unconditional. The lead was CKS mining database item M4: frustrated z=3 graphs might force the departure from equal spacing to a specific value that corresponds to a = √2.

## What Was Proven (Exact Fraction Arithmetic)

**Step 1: The Koide prediction itself.** m_τ(Koide) = 1776.97 MeV versus measured 1776.86 ± 0.12 MeV. Difference: 0.109 MeV = 0.91σ. Confirmed at 50-digit precision. The Koide ratio evaluates to exactly 2/3 (verified to 40+ decimal places).

**Step 2: The algebraic equivalence.** a² = 2 ⟺ Koide = 2/3. Proven as an exact Fraction identity: (1 + a²/2)/3 = (1 + 2/2)/3 = 2/3. The converse: Koide = 2/3 implies a² = 2×(3×2/3 − 1) = 2. These are not two conditions — they're one condition. Deriving either one derives the other.

The key ingredients: the roots-of-unity identities Σcos(θ₀ + 2πi/3) = 0 and Σcos²(θ₀ + 2πi/3) = 3/2, both exact for ALL θ₀. These give sum(m_i)/M = 3(1 + a²/2) and sum(√m_i)²/M = 9, producing Koide = (1 + a²/2)/3.

## What Failed

**Step 3: The Kuramoto model on a triangle.** Three oscillators with energy E = −ΣK_ij cos(φ_i − φ_j). With symmetric couplings K₁₂ = K₂₃ = K and one different bond K₃₁ = J, the equilibrium has α = β where cos(α) = −K/(2J). At K = J (all equal), α = 2π/3 = 120° (equal spacing).

**The structural mismatch is fatal:** The Kuramoto model controls PHASE SPACING. The Koide parameterization has FIXED 120° spacing and varies the AMPLITUDE a. These are different degrees of freedom. Frustrating the graph moves you along the wrong axis — it changes the phase spacing while Koide needs the spacing held fixed at 120° and the amplitude changed.

**Step 4: Attempting the connection anyway.** The generalized Koide ratio with frustrated phases (departure d from 120°) gives a modified condition. Setting a² = 2 and scanning d from −π/3 to π/3: f(d) = 0 ONLY at d = 0. For every d ≠ 0, a² = 2 does NOT produce Koide = 2/3. The two conditions (120° spacing and a² = 2) are jointly required. You cannot trade one for the other.

## What Survives

**The question has been sharpened.** It's no longer "why a = √2?" It's "why C₃ symmetry?" If you assume three generations with C₃ symmetry (120° equal spacing), then a = √2 is the UNIQUE amplitude giving Koide = 2/3. So the open question is: what physical principle forces three generations into C₃ symmetric spacing? This is a deeper question — it's about the structure of the generation space, not about a parameter value.

**The documented blockage is clean.** The frustrated graph mechanism fails for a specific, proven reason: it controls the wrong degree of freedom. This isn't a vague "it didn't work" — it's a structural impossibility. Any future derivation attempt that tries to get a = √2 by modifying the phase spacing will fail for the same reason. The path forward must explain C₃ symmetry directly, not derive it from frustration.

**The prediction still stands.** m_τ = 1776.97 MeV at 0.91σ. The Koide formula works. We just don't know why.

---

The finding is a clean documented blockage — exactly what DISC-8 specified as deliverable (b) for Item 4. The mechanism was tested honestly, it failed for an understood reason, and the question is sharpened for the next attempt.

---

Yes. The equivalence proof itself points to it.

The proof showed: Koide = 2/3 is EQUIVALENT to a² = 2, given C₃ symmetry. And C₃ symmetry (120° spacing) is just the statement that the three phases are equally spaced on a circle — which is the roots-of-unity condition 1 + ω + ω² = 0.

So the entire Koide formula reduces to one question: **why does the mass parameterization m_i = M(1 + a·cos(φ_i))² with equally-spaced φ_i have a² = 2?**

Now look at what a² = 2 actually means physically. In the parameterization, a controls the spread of the masses. At a = 0, all three masses are equal (m_i = M). At a² = 2, the spread is maximal in a specific sense — the Koide ratio hits exactly 2/3.

Here's the path I see on deeper inspection:

**The variational angle.** Consider all possible amplitudes a ≥ 0 with C₃ symmetry. The Koide ratio K(a) = (1 + a²/2)/3 is a monotonically increasing function of a². At a = 0, K = 1/3 (all masses equal, minimum ratio). As a → ∞, K → ∞. The value K = 2/3 at a² = 2 is not an extremum of K(a) — it's just a specific point on a monotonic curve.

So there's no variational principle that selects a² = 2 by extremizing the Koide ratio itself. That path is dead.

**The normalization angle.** But look at the parameterization again: m_i = M(1 + a·cos(φ_i))². The quantity (1 + a·cos(φ_i)) must be non-negative for all i (since it's a square root of mass). The most negative cos(φ_i) can be is −1 (at φ_i = π, which doesn't occur at 120° spacing — the most negative is cos(2π/3) = −1/2). So the positivity constraint is 1 + a·(−1/2) ≥ 0, giving a ≤ 2. Since a = √2 ≈ 1.414 < 2, all masses are positive.

At a = 2, the lightest mass hits exactly zero. At a² = 2, we're at a/a_max = √2/2 = 1/√2. That's a specific geometric point — it's the ratio where a² = a_max²/2. Half the squared maximum. Is there a principle that selects this midpoint?

**The democratic angle.** There's a cleaner way to see it. Consider the three quantities x_i = √(m_i/M) = 1 + a·cos(φ_i). These live on a circle of radius a centered at 1 in some abstract space. The constraint Σcos(φ_i) = 0 (C₃ symmetry) gives Σx_i = 3. The Koide ratio is Σx_i²/(Σx_i)² = Σx_i²/9.

Now: Σx_i² = Σ(1 + a·cos(φ_i))² = 3 + a²·(3/2) = 3 + 3a²/2.

So Koide = (3 + 3a²/2)/9 = (1 + a²/2)/3.

At a² = 2: Σx_i² = 6. And (Σx_i)² = 9. So Σx_i² = (2/3)·(Σx_i)².

This is a specific relationship between the sum of squares and the square of the sum. In statistics, this relates to variance: Var(x) = Σx²/3 − (Σx/3)² = (3 + 3a²/2)/3 − 1 = a²/2. At a² = 2, Var = 1, and the mean is Σx/3 = 1. **The variance equals the mean squared.**

That's a condition: Var(√m) = (mean(√m))². Or equivalently, the coefficient of variation CV = σ/μ = 1. This is a known statistical condition — it characterizes exponential distributions and appears in renewal theory.

**The question becomes:** Is there a physical reason why the square roots of the lepton masses should have coefficient of variation exactly 1? That's a cleaner question than "why a = √2" and it connects to statistical mechanics and information theory rather than graph frustration.

This is a new path. Whether it leads anywhere depends on whether a physical principle (maximum entropy, self-organized criticality, or something from the generation structure) selects CV = 1 for the square-root-mass distribution. I don't have the answer, but the question is better than the one we started with.

---

The other Claude found something. Let me trace the logic.

**The chain of equivalences:**

Start: Koide = 2/3 with C₃ symmetry.

Step 1: Define x_i = √(m_i/M) = 1 + a·cos(φ_i) where φ_i are at 120° spacing. These are the square roots of the normalized masses.

Step 2: C₃ symmetry forces Σx_i = 3 (because Σcos(φ_i) = 0). So the mean of x_i is 1.

Step 3: Koide = Σx_i² / (Σx_i)² = Σx_i² / 9. For Koide = 2/3, we need Σx_i² = 6.

Step 4: The variance of x_i is Var = Σx_i²/3 − (Σx_i/3)² = 6/3 − 1 = 1. The standard deviation σ = 1. The mean μ = 1. Therefore σ/μ = 1.

**The coefficient of variation of √m_i is exactly 1.**

This is the reformulation. Instead of "why a² = 2?" the question is "why does the distribution of √m_i have CV = 1?"

CV = 1 means the standard deviation equals the mean. This is a specific statistical property. It characterizes exponential distributions — if you draw from an exponential distribution, the population CV is exactly 1. It also appears in Poisson processes (the CV of inter-arrival times is 1).

**Why this might matter:** If the lepton masses are generated by some random or self-organizing process acting on the square roots of the masses (not the masses themselves), and that process has maximum entropy subject to the constraint that the mean is fixed, the result is an exponential distribution, which has CV = 1.

**What's actually proven vs speculative:**

Proven (Fraction arithmetic): a² = 2 ⟺ Koide = 2/3 ⟺ Var(x_i) = (mean(x_i))² ⟺ CV(√m) = 1. These are all the same condition expressed differently. No new physics here — just algebraic rewriting.

Speculative: Whether CV = 1 has a physical origin (maximum entropy, self-organized criticality, some generation-space principle). This is a new question, better formed than "why a = √2?" because CV = 1 connects to known mathematics (information theory, statistical mechanics) rather than to graph topology (which failed).

**The structural point:** The frustrated graph mechanism failed because it controls the wrong degree of freedom (phase spacing instead of amplitude). The CV = 1 reformulation doesn't have this problem — it's a constraint on the amplitude directly. But it still needs a physical principle to select it. The question is sharpened, not answered.

This is a lead for DISC-8 continuation or DISC-9, not a result. The derivation of a = √2 remains open, but the question is now: what physical principle forces CV(√m) = 1 for the three generations?

---

we follow the lead

---

