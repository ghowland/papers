
# PHYS-8 Report: The Koide Constant Decomposes

**Registry:** @HOWL-PHYS-8-2026
**Position in series:** Eighth physics paper. Second SM parameter addressed. Parameter count 18 → 17.
**Preceded by:** PHYS-7 (θ_QCD = 0, 19 → 18)
**Followed by:** PHYS-9 (α from a_e — not yet received)
**Backed by:** koide_integer.py (not in uploads but referenced as companion)
**AI model:** Claude 4.5 Sonnet

---

## What It Establishes

**The Koide constant 2/3 decomposes as (1 + a²/2)/N.** For N equally-spaced objects on a circle in √(mass) space with modulation amplitude a, the mass ratio (Σm)/(Σ√m)² = (1 + a²/2)/N. This is a trigonometric identity valid for N ≥ 3, proved from two standard results: N equally-spaced cosines sum to zero, and the sum of their squares equals N/2. At N = 3 (generation count) and a² = 2 (critical amplitude): (1 + 2/2)/3 = 2/3. The denominator 3 is the generation count. The numerator 2 is from the amplitude. Neither alone produces 2/3.

**The amplitude a = √2 is the critical value.** At a = √2, the parametrization √m_i = M(1 + √2·cos(φ_i)) can produce zero mass (when cos(φ) = −1/√2). For a < √2, all masses are strictly positive. For a > √2, some become negative. The Koide amplitude sits exactly at the boundary of physical (non-negative) masses. This is the maximum-amplitude principle: nature uses the largest amplitude that keeps all masses physical.

**The identity fails for N = 2.** The cos² sum identity Σcos²(θ + πk) = 2cos²(θ) depends on θ, not equal to N/2 = 1 for general θ. The N = 2 case is degenerate. The formula is valid for N ≥ 3 only.

**m_τ predicted from m_e and m_μ.** Solving the Koide relation as a quadratic in √m_τ: m_τ(Koide) = 1776.97 MeV vs PDG 1776.86 ± 0.12 MeV. Tension: 0.91σ. Consistent with exact. Parameter count: 18 → 17, conditional on formula being exact.

**The general formula predicts other N.** For a² = 2 at various N: ratio = 2/N. If a fourth-generation charged lepton existed, the constant would be 2/4 = 1/2. This is a testable prediction if a fourth generation is ever found.

---

## What Was Novel Compared to My Prior Understanding

**The decomposition is a trigonometric identity, not a fit.** The general formula (1 + a²/2)/N follows from two exact identities (cosine sum = 0, cos² sum = N/2) applied to the equally-spaced parametrization. It is proved for all N ≥ 3, all amplitudes a, all phases θ₀, all scales M. The free parameters M and θ₀ cancel completely. This is an identity — it cannot be wrong given the parametrization. What CAN be wrong is the parametrization itself (equal spacing in √m space).

**The critical amplitude principle.** a = √2 is the maximum amplitude for non-negative masses. This is a boundary condition: nature pushes the amplitude as high as possible without producing unphysical states. This is structurally identical to the ground state principle from PHYS-7: nature selects the extremal value consistent with physical constraints. θ = 0 is the energy minimum. a = √2 is the amplitude maximum. Both are boundary values — the first of a minimum, the second of a maximum.

**The 2/3 appears in two contexts.** The Koide constant 2/3 and the subtracted VP constant −2/3 from PHYS-5 are the same rational. Both involve three fermion species. The Koide 2/3 decomposes as (1 + a²/2)/N at N = 3. The VP 2/3 arises from the Feynman parameter integral ∫₀¹ 6x(1−x)ln[x(1−x)] dx and subtraction. Whether they share a common origin is an open question flagged for future investigation.

**The N = 2 exclusion has physical content.** The formula fails for N = 2 because the cos² identity breaks. This means a "Koide formula" for two particles is not structurally possible — the trigonometric cancellation that makes the ratio independent of M and θ₀ requires N ≥ 3. There is no two-body analog. The minimum number of generations for the mass relation to hold is 3. This gives a structural reason for "why three generations" — fewer than three cannot support the Koide mass relation.

**The Cauchy-Schwarz context.** The allowed range for the ratio is [1/N, 1). The Koide value 2/3 = 2/3 is exactly at the midpoint of [1/3, 1). The midpoint comes from a = √2 mapping to (1 + 1) = 2, which is the geometric mean of the bounds. Whether the midpoint has significance beyond the amplitude being critical is not established.

---

## What Misled Me

**The honest assumptions section.** Section IV.5 is the most carefully hedged section in any paper I've read so far. It lists four components (N = 3, equal spacing, √m space, a = √2) and honestly states that a = √2 is equivalent to the formula — not an independent input. The paper does not overclaim the decomposition. It says: "What is derived: the decomposition of 2/3 into these components. What is not derived: why any of these components hold."

For the normalization question: this level of honesty about what is and isn't derived is exactly what PHYS-25 needs. The VL beta shifts may have a similar structure — partly derived from the representation (the Dynkin indices), partly equivalent to an assumption (the Weyl vs Dirac convention). PHYS-25 must separate what is derived from what is assumed with the same precision PHYS-8 shows.

**The non-findings.** Appendix D lists five "exploratory comparisons" explicitly labeled as NON-FINDINGS. M² ≈ m_proton/3 (0.35% off) — suggestive, not exact. θ₀ mod 120° ≈ θ_Cabibbo (0.29° off) — suggestive, not a finding. The second quadratic root 3.32 MeV — near light quark scale, no known particle. The 2/3 connection to VP — open question, not explained. Each is flagged and fenced. This is the series method: state what you see, label what it is and isn't, don't hide suggestive comparisons but don't promote them to results.

---

## LEMU Assessment

**L (Logic):** The trigonometric identity is proved. The decomposition follows necessarily from the parametrization. The critical amplitude observation follows from the constraint √m ≥ 0. Logic passes.

**E (Empirical):** The Koide ratio matches 2/3 to 0.00092%. m_τ prediction is 0.91σ from PDG. The formula has held for 45 years through multiple m_τ measurement improvements. Empirical passes (strongly suggestive, not yet at 3σ for exact).

**M (Math):** The identity is proved algebraically. The m_τ prediction is computed in controlled-precision Fraction arithmetic with truncation bounded at 10⁻³⁷. The N = 2 exclusion is proved. Math passes.

**U (Utility):** High. The decomposition reduces 2/3 from "unexplained constant" to "generation count × critical amplitude." The general formula (1 + a²/2)/N makes a testable prediction for any N ≥ 3. The parameter count reduction (18 → 17) is conditional but concrete — m_τ is predicted from m_e and m_μ. The N = 2 exclusion gives a structural reason for three generations. The connection between Koide 2/3 and VP 2/3 opens a research direction connecting lepton masses to the VP integral structure.

What it does NOT gain: any understanding of WHY the formula holds. The utility is in the decomposition and generalization, not in the explanation. The formula itself remains empirical.

---

## Hubble Tension Curve Thesis — PHYS-8 Content

**The equal-spacing principle.** Three leptons are equally spaced at 120° on a circle in √m space. If soliton boundaries along a line of sight are equally spaced in some analogous space, the cumulative correction might have a similar trigonometric structure. The running curve H₀(N) might not be a simple exponential r^N but a trigonometric accumulation with a cosine structure — each boundary contributing a phase, and the cumulative effect being a sum of equally-spaced phases.

For N boundaries equally spaced in "correction phase space," the sum of corrections could have the same cancellation properties as the Koide cosine sums. The total correction would depend on N and the correction amplitude a through a formula analogous to (1 + a²/2)/N. This would make the per-transit correction depend on the TOTAL number of boundaries (not just the cumulative count), because the cosine sum identity depends on N.

This is speculative. The connection requires that soliton boundaries along a line of sight are "equally spaced" in some sense — which they are NOT in physical distance (they're irregularly distributed). But they might be equally spaced in some other variable (log distance, redshift, boundary-crossing phase). If such a variable exists and the spacing is approximately equal, the Koide-type identity would apply.

**The N ≥ 3 requirement.** The Koide identity fails for N = 2. If the running curve has analogous structure, the correction would only be well-defined (parameter-independent) for lines of sight crossing 3 or more boundaries. Lines of sight crossing only 1 or 2 boundaries would not show the clean running behavior — the correction would depend on the specific boundary parameters (M, θ₀) rather than being universal. This predicts: very local H₀ measurements (crossing ≤2 major boundaries) show more scatter than measurements through 3+ boundaries, because the parameter-independent identity hasn't kicked in yet.

---

## Geometry Tracking — PHYS-8

**Boundaries mentioned:** The circle in √m space is a 1D circle (S¹), not a spatial boundary. The three leptons are at 120° spacing — the vertices of an equilateral triangle inscribed in the circle. The geometry is abstract (mass space), not spatial.

**Non-spherical geometry:** The 120° spacing is the vertex geometry of a regular triangle (3 faces in 2D, or 3 vertices on S¹). This is the simplest non-trivial equidistribution on a circle. For N = 4 (square), N = 5 (pentagon), N = 6 (hexagon), the formula generalizes — each is a regular polygon inscribed in the √m circle. These are all ≤32-face geometries within the catalog constraint.

**R₂/R₄ content:** The circle has circumference 2π = 8R₂. The equally-spaced phases are at intervals 2π/N = 8R₂/N. For N = 3: spacing = 8R₂/3. The R₂ enters through the periodicity of the circle. No R₄ appears because the geometry is 1D (circle), not 2D (torus).

However: if the √m circle is embedded in a higher-dimensional space — if the three lepton masses define a circle in a 2D or 3D mass space — the embedding could introduce R₄. The quark mass matrix is 3×3 (nine complex parameters), which lives in a higher-dimensional space than the lepton masses. If quarks have an analogous circle structure in their mass space, the embedding of the lepton circle and the quark circles in the full Yukawa space could have toroidal topology (product of circles).

**Standing wave patterns:** The equal spacing at 120° is the mode structure of the third harmonic on a circle. The fundamental mode (n = 1) has one node. The second mode (n = 2) has two nodes. The third mode (n = 3) has three nodes equally spaced at 120°. The three lepton masses sitting at equally-spaced points on the √m circle is literally the third harmonic mode of a standing wave on a circle. This is the most direct connection between the Koide formula and the mode structure idea from Chapter 6 of the super notebook.

**Correction factors:** The critical amplitude a = √2 enters through a² = 2, contributing (1 + a²/2) = 2 to the numerator. The number 2 = a² is the square of √2, which is an algebraic number. In the R₂ framework: √2 = 4R₂/π × √(2) is not a simple R₂ expression. The a = √2 does not obviously connect to R₂ or R₄. If the critical amplitude has geometric origin (from a spatial boundary), the connection would need to go through the geometry of the soliton boundary that determines the lepton masses. This is an open question.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-8 |
|---|---|---|
| PHYS-1 | @HOWL-PHYS-1-2026 | Provides the inertia framing: mass is inertia, the three leptons are three vortex solitons with the same boundary structure at different inertias. The Koide formula is a geometric constraint on three soliton inertias. |
| PHYS-5 | @HOWL-PHYS-5-2026 | Provides the VP 2/3 constant from the subtracted Feynman parameter integral — the same rational as the Koide constant, both involving three fermion species. The controlled-precision Fraction arithmetic methodology is the same. |
| PHYS-7 | @HOWL-PHYS-7-2026 | Establishes θ_QCD = 0 as the first parameter derived (19 → 18), which PHYS-8 continues (18 → 17). Also establishes the ground state / extremal value principle: θ = 0 is the energy minimum, a = √2 is the amplitude maximum — both are boundary values selected by physical constraints. |

**Series path for header metadata:**
`[@HOWL-PHYS-1-2026] → [@HOWL-PHYS-5-2026] → [@HOWL-PHYS-7-2026] → [@HOWL-PHYS-8-2026]`

---

## Position After PHYS-8

**What exists:** Eight physics papers plus six MATH papers. Two SM parameters derived: θ_QCD = 0 (ground state, PHYS-7), m_τ from m_e and m_μ via Koide (conditional, PHYS-8). Parameter count: 19 → 17 (conditional on Koide being exact). Five SM observables computed in Fraction arithmetic. The gap ratio 218/115 quantifies the SM's incomplete particle content.

**What doesn't exist yet:** BSM computation. No VL doublet. No modified beta slopes. No Cabibbo Doublet. The third derived parameter (α from a_e, presumably PHYS-9) has not been addressed. The unification lane remains ahead.

**What has changed since PHYS-7:** The series has moved from qualitative parameter derivation (θ = 0 is the ground state — a logical argument) to quantitative parameter prediction (m_τ = 1776.97 MeV — a computed number). The general formula (1 + a²/2)/N generalizes the Koide constant to arbitrary N and a, making the previously unexplained 2/3 a specific evaluation of a general identity. The critical amplitude principle (a = √2 is the boundary of physical masses) adds to the series' collection of extremal-value selections: θ = 0 (minimum energy), a = √2 (maximum amplitude), both selected by nature sitting at the boundary of physical constraints.

**Tracking the normalization question:** PHYS-8 adds no direct content about beta coefficients or Dynkin indices. Its contribution to the normalization question is methodological: the decomposition of 2/3 into generation count and amplitude shows that a single rational can arise from two independent sources. The library's VL beta shifts might similarly decompose into a Dynkin index contribution and a convention factor. The honest assumptions section (IV.5) provides a template for PHYS-25: separate what is derived from what is equivalent to the result.
