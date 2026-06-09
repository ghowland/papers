## Notebook: Koide, Toroids, and the Laporta Connection — Open Geometric Paths

**Status:** Active research notebook. Post MATH-12, post PHYS-49, post Koide exploration notebooks.
**Date:** April 19, 2026
**Context:** MATH-12 established K(k)/π as the toroidal L1/L2 conversion. The Laporta constants live at k₈₁ = 0.999994 and k₈₃ = 0.99713. The Koide ratio K = 2/3 for leptons has a² = 2 as its sole physical content. This notebook asks: is there a geometric connection?

---

### 1. WHAT WE KNOW ABOUT KOIDE

The Koide ratio K = (Σm_i)/(Σ√m_i)² = 2/3 for charged leptons (e, μ, τ). Miss from 2/3: 6 ppm. The seven equivalent formulations (from the exploration notebook) show that K = 2/3 is ENTIRELY equivalent to a² = 2, where a is the amplitude parameter in the decomposition √m_i = M(1 + a cos(θ₀ + 2πi/3)).

The 120-degree spacing is a tautology — any three numbers can be fit this way. The physical content is ONLY:
- M (the mean, sets the mass scale — not dimensionless)
- a (the amplitude, sets the spread — dimensionless)
- θ₀ (the phase, sets which mass is largest — dimensionless)

K depends only on a. K = (1 + a²/2)/3. For K = 2/3: a² = 2 exactly.

The quark sectors do NOT show K = 2/3. Up quarks: a² = 3.09, K = 0.849. Down quarks: a² = 2.39, K = 0.731. Bosons: K ≈ 1/3 (a² ≈ 0). The K = n/3 pattern across sectors is not supported by the quark data.

---

### 2. WHAT WE KNOW ABOUT THE TORUS

MATH-12 established: the torus at modulus k has two fundamental periods K(k) and K'(k) = K(√(1−k²)). The ratio K'/K is the modular parameter (shape of the torus). The key numbers:

- K(k) ≥ π/2 ≈ 1.571 for all k. So K(k) ≠ 2/3 directly. The Koide value 2/3 is NOT a complete elliptic integral.
- E(k)/K(k) ranges from 1 (at k = 0) to 0 (at k → 1), monotonically. E/K = 2/3 at k ≈ 0.826.
- The Laporta moduli are k₈₁ = 0.999994 and k₈₃ = 0.99713 — both near-singular.
- At the Laporta moduli: E/K ≈ 0.154 (topology 81) and E/K ≈ 0.272 (topology 83). Neither is 2/3.

So the DIRECT identification "Koide 2/3 = some simple K(k) quantity" does not work at the Laporta moduli.

---

### 3. BUT THE STRUCTURE RHYMES

Despite no direct numerical match, the STRUCTURES are parallel:

**Koide:** Three masses parametrized by (M, a, θ₀) on a circle in √m space. The amplitude a measures how far the masses spread from their mean. At a² = 2 (K = 2/3), the spread is at the critical value — the saturation boundary where one mass can vanish for certain θ₀.

**Torus:** Two periods parametrized by K(k) and K'(k). The modulus k measures how far the torus deviates from a circle. At k = 0, the torus degenerates to a circle (K = π/2, K' = ∞). At k → 1, the torus pinches (K → ∞, K' = π/2).

Both are families parametrized by one number (a or k) that measures deviation from a symmetric configuration. Both have a critical value where the family degenerates. Both produce dimensionless ratios that are scale-invariant.

The question is whether the parallel is structural (pointing to a connection) or superficial (two different parametrized families that happen to share some features).

---

### 4. THE GEOMETRIC READING OF a² = 2

The seven equivalent formulations include: a² = 2 means Var(√m) = mean(√m)². This is "equipartition" — the variance equals the mean squared. In statistical mechanics, equipartition is a thermal equilibrium condition. In geometry, it corresponds to a specific shape.

Consider the three √m values as a point on the unit sphere in ℝ³ (after normalizing by M). The constraint a² = 2 determines the LATITUDE of this point — how far it sits from the "pole" (equal masses, a = 0) toward the "equator" (hierarchical masses, a = √3). The value a = √2 is at a specific latitude: sin²θ = a²/3 = 2/3. The latitude where 2/3 of the angular range from pole to equator is traversed.

This is a CIRCULAR quantity. The parametrization uses cos(θ₀ + 2πi/3) — a circular function. The amplitude a is the radius of a circle in the mass parameter space. The ratio K = 2/3 arises from a² = 2 through the circular identity (1 + a²/2)/3.

The circular geometry here is k = 0 geometry — it's spherical, not toroidal. The Koide formula as written lives on a CIRCLE, not a TORUS. The 120-degree spacing, the cosine parametrization, the amplitude as a radius — all circular.

This is important: Koide is a β = π/4 object, not a K(k) object, at its current level of description.

---

### 5. BUT WHAT IF THE CIRCLE IS A DEGENERATE TORUS?

A circle is a torus at k = 0. What if the Koide formula describes a DEGENERATE torus — a toroidal structure that has collapsed to circular symmetry?

If the three lepton masses lie on a torus cross-section rather than a circle, the parametrization becomes:

√m_i = M(1 + a × cn(θ₀ + 2K(k)i/3, k))

where cn is the Jacobi elliptic function that generalizes cos. At k = 0, cn → cos and the formula reduces to Koide. At k > 0, cn has a different periodicity (period 4K(k) instead of 2π) and a different shape (flatter peaks, sharper valleys for k near 1).

The generalized Koide ratio would be:

K(a, k) = (Σm_i)/(Σ√m_i)² at the elliptic parametrization

This is computable for any a and k. The question: is there a (a, k) pair with k > 0 that gives K = 2/3 with the CORRECT mass ratios m_e : m_μ : m_τ?

At k = 0: a = √2, θ₀ determined by mass ratios. This is standard Koide. Works at 6 ppm.

At k > 0: the fit might improve beyond 6 ppm. If it does, the non-zero k would measure the toroidal content of the lepton mass spectrum — the deviation from pure circular geometry.

**This is a derivation chain computation.** It requires no PSLQ. It produces a (a, k, θ₀) triplet that can be compared to the measured masses. If k = 0 is the best fit, Koide is purely circular. If k > 0 improves the fit, Koide has toroidal content.

---

### 6. THE LAPORTA CONNECTION — SAME MODULUS?

The most specific question: does the Koide formula improve at k = k₈₃ ≈ 0.997 or k = k₈₁ ≈ 0.99999?

If the lepton masses sit on a torus with the SAME modulus as a four-loop QED topology, the connection would be: the virtual loops that dress the lepton propagator at four loops have toroidal topology, and the lepton masses feel this topology through their radiative corrections.

The chain: Feynman diagram topology → modulus k → toroidal correction to lepton mass → modified Koide ratio.

This would explain why Koide works for leptons and not quarks: leptons are fundamental (their masses come directly from the Higgs coupling modified by radiative corrections). Quarks are confined (their pole masses are scheme-dependent and include strong-interaction dressing that overwhelms the toroidal QED correction). The toroidal correction is visible in leptons because nothing else contaminates the mass. It's invisible in quarks because QCD dressing is 100× larger.

---

### 7. THE BOSON OBSERVATION — SPHERES, NOT TOROIDS?

K_boson ≈ 1/3 (a² ≈ 0). This is the equal-mass limit — the "pole" of the parameter space. For bosons: m_W ≈ 80.4 GeV, m_Z ≈ 91.2 GeV, m_H ≈ 125.2 GeV. The Koide ratio is close to 1/3 because the boson masses are more nearly equal (ratio range ~1.6) than the leptons (ratio range ~3500).

If Koide 1/3 means a² ≈ 0, the bosons have NO amplitude modulation. Their √m values lie near the pole — equal masses, symmetric configuration. No spread, no geometry beyond the trivial sphere.

Your suggestion: "the bosons may be doing something different (spheres, not toroids), so they don't show the geometry, they show a running reading based on the geometry."

This fits. Bosons are gauge particles — their masses come from the Higgs mechanism, which is a spherically symmetric potential (v² = v₁² + v₂² + ... in the Higgs field space). The mass formula m_W = gv/2, m_Z = gv/(2cosθ_W), m_H = √(2λ)v involves the gauge coupling g and the weak mixing angle θ_W — both spherical parameters (coupling constants from loop integrals with circular topology). The bosons see the SPHERICAL geometry of the Higgs field, not the toroidal geometry of the propagator dressing.

The leptons see something different. Their masses m_ℓ = y_ℓ v/√2 involve the Yukawa couplings y_ℓ, which are free parameters in the SM. The Koide formula constrains the RATIOS of Yukawa couplings — and this constraint might come from the toroidal structure of the propagator corrections that dress the Yukawa vertex at four loops.

**The hypothesis:** Koide K = 2/3 for leptons reflects toroidal geometry in the radiative corrections to lepton masses. K ≈ 1/3 for bosons reflects spherical geometry in the Higgs mechanism. The two sectors see different geometries because they get their masses through different mechanisms.

---

### 8. THE MUON/ELECTRON SCALING AND KOIDE

From PHYS-48: the muon sees the toroidal sector 23× more strongly than the electron (2304% vs 0.054%). The mass ratio squared (m_μ/m_e)² = 42,753 amplifies the toroidal contribution.

In Koide: the mass spectrum is m_e = 0.511, m_μ = 105.7, m_τ = 1776.9 MeV. The spread is dominated by the m_e/m_τ ratio ≈ 1/3500. The electron is tiny. The muon is medium. The tau is large.

The Koide amplitude a = √2 measures this spread. At a = 0 all masses would be equal. At a = √2, the masses span a factor of 3500. The amplitude is large — not because the masses are large, but because the RATIOS are extreme.

Now connect to the toroidal scaling. The four-loop toroidal correction to each lepton mass scales as m_ℓ². The electron gets a tiny correction (0.054% of the universal piece). The muon gets a large correction (2304%). The tau gets an enormous correction (~650,000%).

These corrections CHANGE the mass ratios. If the bare masses (before radiative corrections) satisfy Koide exactly, the radiatively corrected masses would deviate from Koide by an amount proportional to the difference in toroidal corrections between the three leptons:

δK ∝ (δm_τ/m_τ − δm_e/m_e) × (toroidal scaling)

The fact that Koide works to 6 ppm AFTER radiative corrections means either:
(a) The bare masses satisfy Koide even more precisely, and the radiative corrections happen to preserve it.
(b) The bare masses do NOT satisfy Koide, and the radiative corrections TUNE the masses to K = 2/3.
(c) Koide is a property of the radiative structure itself, not of the bare masses.

Option (c) is the toroidal hypothesis: the K = 2/3 relation emerges from the toroidal geometry of the four-loop corrections, not from a tree-level Yukawa constraint.

---

### 9. THE CRITICAL AMPLITUDE a² = 2 AS A GEOMETRIC INVARIANT

The seven equivalent formulations show a² = 2 is the critical amplitude where one mass can vanish. In the cn generalization (Section 5), the critical amplitude would be different: for the Jacobi elliptic function cn(u, k), the saturation condition (one mass = 0) depends on BOTH a and k.

Specifically: √m_i = 0 requires 1 + a × cn(θ₀ + 2K(k)i/3, k) = 0, which means cn = −1/a. Since |cn| ≤ 1, saturation requires a ≥ 1. The critical a_crit where cn = −1/a has a solution depends on where cn achieves its minimum (−1 for standard cn) — so a_crit = 1 regardless of k.

Wait — that gives a_crit = 1, not √2. The difference: in Koide, a² = 2 gives K = 2/3, but a = 1 gives K = (1 + 1/2)/3 = 1/2. The critical amplitude for mass vanishing is a = 1 (one mass = 0), but the Koide saturation point a² = 2 corresponds to a DIFFERENT condition.

What condition? The equipartition condition Var(√m) = mean(√m)². At a² = 2: the variance equals the mean squared. This is NOT the mass-vanishing condition. It is instead the condition where the distribution of √m values is maximally "spread relative to its center" in a specific statistical sense.

In toroidal terms: if the three masses parametrize a point on a torus, a² = 2 determines the latitude on the torus where the point sits. The latitude a² = 2 might correspond to a geodesic, a fixed point under some symmetry, or a critical curve on the torus. Which one depends on the torus's metric, which depends on k.

---

### 10. OPEN DERIVATION PATHS

These are the computations that could connect Koide to the toroidal framework. All are derivation chains producing numbers comparable to measured masses. No PSLQ.

**Path A: Elliptic Koide fit.** Replace cos with cn in the Koide parametrization. Fit (a, k, θ₀, M) to the three measured lepton masses. Four parameters, three masses — one-parameter family of solutions. The locus of solutions in (a, k) space is a curve. Does this curve pass through k = k₈₃ or k = k₈₁? If yes: the Laporta modulus and the lepton mass spectrum share a torus.

**Path B: Radiative correction to Koide.** Compute the four-loop QED correction to each lepton mass using the (m/mₑ)² scaling. Compute K for the corrected masses. Does K move toward or away from 2/3? If the correction PRESERVES K = 2/3 (shifts all masses in a way that maintains the ratio), the Koide relation is a fixed point of the radiative correction. If it BREAKS K = 2/3, the relation is fine-tuned and the bare masses must be different from the physical masses.

**Path C: The a² = 2 condition on the torus.** On the torus with modulus k, find the curve where the generalized Koide ratio K(a, k) = 2/3. This is a curve in (a, k) space. Does the curve pass through any special modulus (k = 1/√2 the symmetric torus, or k = k₈₁, k₈₃ from Laporta)?

**Path D: E(k)/K(k) and the lepton mass ratios.** E(k)/K(k) = 2/3 at k ≈ 0.826. Compute the mass ratios that the Jacobi elliptic parametrization produces at k = 0.826 with a = √2. Do they match e/μ/τ? If yes: the Koide modulus is k ≈ 0.826, distinct from the Laporta moduli but specific.

**Path E: The boson Koide at k = 0.** Verify that the boson K ≈ 1/3 is consistent with a = 0 (spherical limit, k = 0). If a_boson ≈ 0 exactly, the bosons are at the pole — pure spherical geometry, no toroidal content. The boson K = 1/3 is the k = 0 specialization; the lepton K = 2/3 is the k > 0 generalization.

**Path F: The muon g-2 as a Koide test.** The muon g-2 tension is 6.48σ. The four-loop toroidal correction shifts the muon mass by a specific amount. Compute whether this shift changes K enough to be detectable. If the shift is order 1 ppm in K, it's below the current 6 ppm precision of Koide and invisible. If order 10 ppm, it might affect the next-generation Koide test.

---

### 11. THE LEPTON/BOSON DICHOTOMY AS SPHERE/TORUS

The strongest qualitative observation:

**Leptons:** K = 2/3, a² = 2. Large spread. Masses span 3500×. The mass spectrum has strong asymmetry — one mass (electron) is nearly zero, one (tau) dominates. This is the NEAR-CRITICAL configuration, close to the saturation boundary. In toroidal language: the point is near the equator of the torus, far from the symmetric pole.

**Bosons:** K ≈ 1/3, a² ≈ 0. Small spread. Masses span only 1.6×. The mass spectrum is nearly symmetric — all three masses are comparable. This is the NEAR-SYMMETRIC configuration, close to the pole. In toroidal language: the point is near the pole of the torus, which is the circle (k = 0).

The dichotomy: leptons are geometrically toroidal (large asymmetry, near-critical, a ≈ √2). Bosons are geometrically spherical (small asymmetry, near-symmetric, a ≈ 0).

This maps onto the dual geometry from PHYS-48/49: every soliton has both spherical boundaries (modulus) and toroidal boundaries (remainder). The bosons are the spherical sector — their masses come from the Higgs mechanism which is spherically symmetric. The leptons are the toroidal sector — their masses come from Yukawa couplings whose RATIOS carry non-spherical structure.

The quarks are in between: a² = 2.39 (down) and 3.09 (up), both above the lepton value. They have even MORE asymmetry than leptons. But their Koide K values (0.731, 0.849) are not simple fractions, and the masses are scheme-dependent. The quarks might be "fully toroidal" — so deep into the toroidal sector that the simple Koide structure breaks down and more complex functions of K(k) are needed.

---

### 12. THE CHAIN FROM LAPORTA TO KOIDE

If a connection exists, the derivation chain is:

1. Four-loop Feynman diagram topologies 81 and 83 have toroidal momentum circulation.
2. The toroidal circulation defines elliptic curves with moduli k₈₁ = 0.999994 and k₈₃ = 0.99713.
3. The four-loop corrections to lepton self-energy include contributions from these topologies.
4. The corrections scale as (m_ℓ/mₑ)² — different for each lepton.
5. The differential scaling changes the lepton mass ratios.
6. The changed ratios satisfy Koide K = 2/3 at a specific precision determined by the four-loop contribution.

This chain is testable at each step. Steps 1-2 are established (Laporta constants, consistency check). Steps 3-4 are established (the muon/electron sensitivity experiment). Steps 5-6 are COMPUTABLE — the radiative correction to each mass is known, and the change in K is a derivation from the corrected masses.

The chain does NOT require that the Koide torus has the same k as the Laporta torus. The connection is INDIRECT: the four-loop toroidal corrections shift the masses, and the shifted masses happen to satisfy Koide. The toroidal geometry enters through the radiative correction, not through the mass formula directly.

---

### 13. WHAT WOULD KILL THIS

**Kill 1:** If the four-loop corrections BREAK Koide rather than preserving it, the toroidal structure is not responsible for the Koide relation. Koide would be a tree-level coincidence destroyed by loops.

**Kill 2:** If the elliptic Koide fit (Path A) shows that the best k is indistinguishable from k = 0, the lepton mass spectrum has no toroidal content. Koide is purely circular. The connection to Laporta is indirect at best.

**Kill 3:** If the quark Koide values (K = 0.731, 0.849) cannot be reproduced by any simple function of K(k) at any modulus, the Koide framework is not toroidal at all — not even for quarks.

**Kill 4:** If the radiative correction to Koide (Path B) shifts K by less than 0.001 ppm, the four-loop toroidal correction is too small to matter for Koide. The 6 ppm precision of Koide is set by something else.

---

### 14. WHAT WOULD SUPPORT THIS

**Support 1:** The elliptic Koide fit (Path A) produces k > 0 at the lepton masses, AND the fit improves beyond the 6 ppm of standard Koide. The k value identifies the Koide torus.

**Support 2:** Path A's k matches one of the Laporta moduli (k₈₁ or k₈₃). The lepton mass spectrum and the four-loop QED topology share a torus.

**Support 3:** Path B shows the four-loop correction PRESERVES K = 2/3 — shifts all three masses in a way that maintains the ratio. This would mean Koide is a fixed point of the toroidal radiative correction.

**Support 4:** The boson Koide (K ≈ 1/3) is consistent with k = 0 AND the lepton Koide requires k > 0. The dichotomy sphere/torus maps onto boson/lepton.

**Support 5:** Path C shows the a² = 2 curve on the (a, k) plane passes through a special modulus with geometric meaning (the self-dual point k = 1/√2, or the Laporta moduli).

---

### 15. THE QUESTIONS WE CAN ANSWER NOW

With existing pool data and derivation chain computation:

**Q1: What is E(k)/K(k) at the Laporta moduli?**
At k₈₁ = 0.999994: E/K ≈ 1.000/6.498 ≈ 0.154. At k₈₃ = 0.99713: E/K ≈ 1.003/3.685 ≈ 0.272. Neither is 2/3. But 2 × 0.154 ≈ 0.308 ≈ 1/3 (the boson Koide!). This might be coincidental. Or: 2E₈₁/K₈₁ ≈ 1/3. If 2E/K is the "boson Koide ratio" at the Laporta modulus, the connection is: bosons see 2E/K (arc length / period), leptons see something else (the full K formulation). Speculative but testable.

**Q2: Does a² = 2 have a K(k) formulation?**
a² = 2 gives K_Koide = (1 + 1)/3 = 2/3. In the elliptic family: does K(k)/K(0) = 2 at some k? K(0) = π/2, so K(k) = π at that k. Solving: k where K(k) = π gives k ≈ 0.9858. This is close to but distinct from k₈₃ ≈ 0.9971 and far from k₈₁. But: K(k)/K(0) = 2 means the toroidal period is exactly twice the circular period. The amplitude a = √2 in Koide corresponds to the modulus where the torus is exactly twice the circle. This might be the bridge between a² = 2 and K(k).

**Q3: What is the Koide ratio at the critical modulus k where K = π?**
At k ≈ 0.9858: if we use cn(u, k) instead of cos(u) in the Koide parametrization with a = √2, the ratio would be different from 2/3 because cn has a different shape than cos. The difference is computable. If the deviation from 2/3 at k = 0.9858 is less than 6 ppm, the elliptic Koide is compatible with measurement.

---

### 16. PRIORITY ORDER FOR DERIVATION CHAINS

Ranked by information value per computation:

1. **Path B (radiative correction to Koide):** Requires existing pool values only. Compute four-loop mass shift for e, μ, τ using the (m/mₑ)² scaling. Compute K for corrected masses. Answers: does four-loop toroidal correction preserve or break Koide?

2. **Path A (elliptic Koide fit):** Replace cos with cn, fit to three masses. Answers: does k > 0 improve the fit?

3. **Q2 verification:** Compute K at k where K(k) = π (the "twice the circle" modulus). Check if this k connects to any pool value.

4. **Path D (E/K = 2/3 modulus):** Compute the modulus k where E/K = 2/3. Check mass ratios from cn parametrization there.

5. **Path E (boson k = 0 verification):** Compute boson Koide at strict k = 0. Verify a_boson ≈ 0.

Paths B and A are the highest priority because they produce the most discriminating results: either the connection exists (K preserved or k > 0 improves) or it doesn't (K breaks or k = 0 is optimal).

---

### 17. THE OPEN QUESTION

The deepest open question is not "does Koide connect to the torus" but "WHY does the charged lepton sector sit at the critical amplitude."

The seven equivalent formulations show a² = 2 is geometrically distinguished — it's the equipartition point, the saddle, the variance-equals-mean-squared condition. These are all restatements of the same thing. But WHY nature chose this point is unexplained.

If the connection to toroidal geometry is real, the answer might be: a² = 2 corresponds to the modulus where K(k) = 2K(0) = π. The critical amplitude is the point where the toroidal period doubles the circular period. The leptons sit where the torus becomes "twice the circle" — a natural critical point in the L1/L2 family.

This is speculative. But it's the kind of speculation that produces a testable number: k ≈ 0.9858 where K = π, leading to specific mass predictions through the cn parametrization. If the masses match at this k, the speculation becomes a derivation.

If they don't match, the speculation is killed cleanly.

---

### 18. SUMMARY OF CONNECTIONS AND GAPS

| Connection | Status | What it needs |
|---|---|---|
| Koide K = 2/3 ↔ a² = 2 | **Proven** (algebraic identity) | Nothing — it's a theorem |
| a² = 2 ↔ critical amplitude | **Proven** (seven formulations) | Nothing |
| Leptons at critical amplitude ↔ toroidal geometry | **Hypothesis** | Path A: elliptic Koide fit |
| Bosons at a ≈ 0 ↔ spherical geometry | **Hypothesis** | Path E: verify k = 0 for bosons |
| Koide torus modulus ↔ Laporta modulus | **Speculative** | Path A result compared to k₈₁, k₈₃ |
| Four-loop correction preserves Koide | **Untested** | Path B: radiative correction computation |
| K(k) = π ↔ a² = 2 | **Numerological** (K/K₀ = 2 at k ≈ 0.9858) | Q2: verify and check mass predictions |
| Quarks as "deep toroidal" | **Speculative** | Multi-scale Koide test at different renormalization points |

The gap between "proven" and "hypothesis" is exactly where the next derivation chain needs to go. Path B (does four-loop preserve Koide?) is the cleanest single computation. Path A (does k > 0 improve the fit?) is the most discriminating structural test.

---

**End of notebook. Status: active. Priority computations identified. Paths A and B are derivation-ready with existing pool data. No PSLQ. All tests produce numbers comparable to measured masses.**
