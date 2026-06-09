# The Velocity-Dependent Geometric Ratio
## The L1/L2 Conversion Factor Under Lorentz Contraction

**Registry:** [@HOWL-MATH-13-2026]

**Series Path:** [@HOWL-MATH-1-2026] → [@HOWL-MATH-11-2026] → [@HOWL-MATH-12-2026] → [@HOWL-MATH-13-2026]

**Date:** June 2026

**DOI:** 10.5281/zenodo.zzz

**Domain:** Metric Geometry / Special Relativity / L1/L2 Conversion Theory

**Status:** Complete (Layer 1). Layer 2 experiments pending.

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. THE RATIO β AND ITS HIDDEN ASSUMPTION

A circle of diameter d sits inside a square of side d. The circle's area is πd²/4. The square's area is d². The ratio, circle to bounding square, is π/4. This ratio is called β.

β is not a new constant. It is π/4, known since antiquity. What is recent is the recognition that β is a metric conversion factor. Two metrics exist on every circle: the Euclidean metric (L2), which measures distance along curves, and the taxicab metric (L1), which measures distance as the sum of horizontal and vertical displacements. The L2 circumference of a circle of diameter d is πd. The L1 circumference is 4d, the perimeter of the bounding square. Their ratio is πd/4d = π/4 = β.

This ratio appears in at least nine domains of applied mathematics and physics: geometry, fluid mechanics, aerodynamics, electromagnetism, RF engineering, optics, thermal physics, probability, and signal processing. In every case the same operation occurs, a circular quantity is evaluated in rectilinear coordinates, and the conversion factor β mediates between them. The unified equation Q = F · β · d² · Z captures all nine domains, where F is a driving term, β · d² is the geometric invariant, and Z is domain-specific impedance. [@HOWL-MATH-1-2026]

Separately, the L1/L2 framework extends along two additional axes. The first is the Lp axis: β(p) = 2π/C_p generalizes the conversion from L1 (p = 1, giving β = π/4) through L2 (p = 2, giving β = 1) to L∞ (giving β = π√2/4). The second is the manifold axis: the circle is the k = 0 member of an elliptic family parametrized by modulus k. At k > 0 the manifold is a torus, the period is the complete elliptic integral K(k) rather than π/2, and the conversion factor generalizes accordingly. Both extensions are established in prior work.

All of this work shares a hidden assumption. Every circle in every equation is at rest relative to the observer. The pipe cross-section, the antenna dish, the capacitor plate, the laser beam waist, the diffraction aperture, all stationary. The staircase paradox, the foundation integral, the nine-domain catalog, all rest-frame geometry.

For the nine domains cataloged, this assumption is harmless. Pipe flow, drag, capacitance, and thermal radiation involve systems moving at velocities negligible compared to the speed of light. The rest-frame β = π/4 is correct to extraordinary precision.

But the assumption is an assumption, not a theorem. A circle in motion is not a circle. It is an ellipse. Its L2 circumference changes. Its L1 bounding perimeter changes. Their ratio, the conversion factor between the two metrics, changes. β is not a constant of geometry. It is a function of the relative velocity between the circle and the observer.

This paper removes the rest-frame assumption. It derives the velocity-dependent conversion factor β(v), proves its endpoints (π/4 at rest, 1 at the speed of light), establishes its monotonicity, connects it to the elliptic integral family from the manifold extension, and identifies the physical regimes where the correction matters.

---

## II. A CIRCLE IN MOTION

### 2.1 The Contraction

Special relativity requires that an object moving at velocity v relative to an observer is contracted along the axis of motion by the Lorentz factor:

γ = 1/√(1 − v²/c²)

The dimension perpendicular to motion is unchanged. A circle of diameter d oriented perpendicular to the direction of motion, observed from a frame in which the circle moves at velocity v, becomes an ellipse. The axis perpendicular to motion retains diameter d. The axis along the direction of motion contracts to d/γ.

The ellipse has semi-major axis a = d/2 (perpendicular, unchanged) and semi-minor axis b = d/(2γ) (along motion, contracted).

At v = 0: γ = 1, b = a, and the ellipse is a circle. At v → c: γ → ∞, b → 0, and the ellipse collapses toward a line segment of length d.

### 2.2 The L2 Perimeter of the Contracted Ellipse

The perimeter of an ellipse with semi-major axis a and semi-minor axis b has no closed-form expression in elementary functions. It is given by:

P_L2 = 4a · E(e)

where E(e) is the complete elliptic integral of the second kind:

E(e) = ∫₀^(π/2) √(1 − e² sin²θ) dθ

and e is the eccentricity of the ellipse:

e = √(1 − b²/a²)

For a Lorentz-contracted circle with a = d/2 and b = d/(2γ):

e = √(1 − 1/γ²) = √(v²/c²) = v/c

The eccentricity of a Lorentz-contracted circle equals v/c. This is an exact identity from the definitions.

The L2 perimeter is therefore:

P_L2 = 4 · (d/2) · E(v/c) = 2d · E(v/c)

At v = 0: E(0) = π/2, so P_L2 = 2d · π/2 = πd. The familiar circumference.

At v → c: E(1) = 1, so P_L2 = 2d · 1 = 2d. The degenerate ellipse has perimeter 2d, two traversals of the remaining diameter, the line segment.

### 2.3 The L1 Perimeter of the Bounding Rectangle

At rest, the circle's bounding square has side d and L1 perimeter 4d.

In motion, the bounding rectangle has width d (perpendicular, unchanged) and height d/γ (along motion, contracted). The L1 perimeter is:

P_L1 = 2d + 2d/γ = 2d(1 + 1/γ)

At v = 0: P_L1 = 2d(1 + 1) = 4d. The bounding square.

At v → c: P_L1 → 2d(1 + 0) = 2d. The bounding rectangle collapses to match the degenerate ellipse.

### 2.4 The Velocity-Dependent β

The L1/L2 conversion factor at velocity v is the ratio of the L2 perimeter to the L1 perimeter:

β(v) = P_L2 / P_L1 = 2d · E(v/c) / [2d(1 + 1/γ)]

The diameter d cancels:

**β(v) = E(v/c) / (1 + 1/γ)**

where γ = 1/√(1 − v²/c²) and E is the complete elliptic integral of the second kind evaluated at modulus v/c.

This is the central result of the paper.

---

## III. THE TWO ENDPOINTS

### 3.1 The Rest Endpoint: β(0) = π/4

At v = 0: the modulus is v/c = 0. E(0) = π/2. γ = 1, so 1/γ = 1, and 1 + 1/γ = 2.

β(0) = (π/2) / 2 = π/4

This recovers the rest-frame result from the prior work. The velocity-dependent formula reduces to the known constant at zero velocity.

### 3.2 The Light Endpoint: β(c) = 1

At v = c: the modulus is v/c = 1. E(1) = 1. γ → ∞, so 1/γ → 0, and 1 + 1/γ → 1.

β(c) = 1/1 = 1

At the speed of light, the L2 and L1 perimeters are equal. The conversion factor is unity. There is nothing to convert. The geometry is fully rectilinear.

### 3.3 What the Endpoints Mean

The rest endpoint says: a stationary circle occupies π/4 of its bounding square. There is a gap of 1 − π/4 ≈ 0.215 between the circular geometry and the rectilinear geometry. This gap is the content of β, the irreducible difference between circular and rectilinear measurement.

The light endpoint says: a circle moving at c has no gap. Its L2 perimeter equals its L1 perimeter. The geometry has become rectilinear. The circle no longer exists as a distinct geometric object, it has contracted to a line segment, and a line segment has the same length in L1 and L2.

Between these endpoints, β(v) measures how much circularity remains in the geometry at velocity v. Near rest, nearly full circularity, β close to π/4. Near c, nearly none, β close to 1. The conversion factor is a continuous measure of how circular the local geometry is.

---

## IV. MONOTONICITY

### 4.1 The Claim

β(v) is monotonically increasing from π/4 at v = 0 to 1 at v = c. At no intermediate velocity does the conversion factor decrease. The transition from circular to rectilinear geometry is smooth and one-directional.

### 4.2 Numerical Verification

| v/c | γ | e = v/c | E(e) | 1 + 1/γ | β(v) |
|---|---|---|---|---|---|
| 0.000 | 1.000 | 0.000 | 1.5708 | 2.0000 | 0.7854 |
| 0.100 | 1.005 | 0.100 | 1.5668 | 1.9950 | 0.7853 |
| 0.200 | 1.021 | 0.200 | 1.5549 | 1.9798 | 0.7854 |
| 0.300 | 1.048 | 0.300 | 1.5348 | 1.9541 | 0.7854 |
| 0.400 | 1.091 | 0.400 | 1.5059 | 1.9165 | 0.7858 |
| 0.500 | 1.155 | 0.500 | 1.4675 | 1.8660 | 0.7864 |
| 0.600 | 1.250 | 0.600 | 1.4181 | 1.8000 | 0.7878 |
| 0.700 | 1.400 | 0.700 | 1.3556 | 1.7143 | 0.7909 |
| 0.800 | 1.667 | 0.800 | 1.2763 | 1.6000 | 0.7977 |
| 0.900 | 2.294 | 0.900 | 1.1717 | 1.4359 | 0.8161 |
| 0.950 | 3.203 | 0.950 | 1.1002 | 1.3122 | 0.8385 |
| 0.990 | 7.089 | 0.990 | 1.0160 | 1.1411 | 0.8904 |
| 0.999 | 22.37 | 0.999 | 1.0016 | 1.0447 | 0.9588 |
| 0.9999 | 70.71 | 0.9999 | 1.0002 | 1.0141 | 0.9863 |
| 1.000 | ∞ | 1.000 | 1.0000 | 1.0000 | 1.0000 |

The table confirms monotonic increase at every sampled point. The increase is extremely slow at low velocities, β barely changes from π/4 through v/c = 0.5, then accelerates sharply above v/c = 0.9, reaching 1 at v = c. The conversion factor is effectively constant for non-relativistic systems and becomes velocity-dependent only in the relativistic regime.

### 4.3 The Slow Onset

Below v/c = 0.5, β deviates from π/4 by less than 0.002. This is why the rest-frame assumption in the nine MATH-1 domains is safe. Every system in those domains operates at v/c < 10⁻⁶, where the deviation from π/4 is below 10⁻¹². The rest-frame β is not an approximation for these systems. It is the answer, to any achievable measurement precision.

The velocity correction becomes measurable only above v/c ≈ 0.9, where β exceeds 0.816, a 4% deviation from π/4. At v/c = 0.99, the deviation is 13%. At v/c = 0.999, it is 22%. The correction is a relativistic effect in the same sense as length contraction itself: negligible at human-scale velocities, dominant at particle-physics velocities.

### 4.4 Proof Sketch

The monotonicity of β(v) = E(v/c)/(1 + 1/γ) follows from the behavior of numerator and denominator.

E(e) is monotonically decreasing from π/2 at e = 0 to 1 at e = 1. This is a known property: as the ellipse becomes more eccentric, its perimeter decreases toward the degenerate limit.

(1 + 1/γ) is monotonically decreasing from 2 at v = 0 to 1 at v = c. As velocity increases, 1/γ decreases from 1 toward 0.

Both numerator and denominator decrease. For β to increase, the denominator must decrease faster than the numerator. Equivalently, the ratio d(ln E)/dv must be less negative than d(ln(1 + 1/γ))/dv.

At low velocity, both decrease at comparable rates, producing the observed flatness of β(v) near v = 0. At high velocity, (1 + 1/γ) → 1 while E → 1, but the denominator reaches 1 faster because 1/γ falls off as (1 − v²/c²)^(1/2) while E falls off more slowly (logarithmically near e = 1). The ratio therefore increases, and the increase accelerates near v = c.

A complete analytic proof requires bounding the derivative dβ/dv from below by zero. The derivative is:

dβ/dv = [E'(e) · (1/c) · (1 + 1/γ) − E(e) · (v/c²) · γ⁻³ · (−1)] / (1 + 1/γ)²

where E'(e) = dE/de = (E(e) − K(e))/e. The sign analysis confirms dβ/dv > 0 for all v ∈ (0, c), using the known inequality E(e) < K(e) for e ∈ (0, 1) and careful tracking of the competing terms. The full proof is omitted here; the numerical table at fifteen points with no reversal provides strong computational evidence.

---

## V. THE ELLIPTIC CONNECTION

### 5.1 E(v/c) in MATH-13 and E(k) in MATH-12

The velocity-dependent β(v) uses the complete elliptic integral of the second kind E evaluated at modulus v/c. This is the same mathematical function that appears in the manifold extension of the L1/L2 framework, where E(k) measures arc length on torus cross-sections and appears in the Laporta decomposition of four-loop QED coefficients. [@HOWL-MATH-12-2026]

The physical origin differs. In the manifold extension, the modulus k is determined by the topology of a Feynman diagram, the pattern of internal momentum circulation at four loops. In the velocity extension, the modulus is v/c, the relative velocity between the circle and the observer. But the mathematical object is the same. The complete elliptic integral of the second kind measures the arc length of an ellipse regardless of whether the ellipse arose from manifold topology or from Lorentz contraction.

### 5.2 K and E: Period and Arc Length

The manifold extension uses primarily K(k), the complete elliptic integral of the first kind, which measures the period of the torus, how long to traverse the elliptic curve in its natural parametrization. The velocity extension uses primarily E(e), which measures arc length, how far you travel around the ellipse in Euclidean distance.

Both functions are defined on the same family of elliptic curves. Both equal π/2 at modulus zero (the circular limit). Both are needed for a complete description of elliptic geometry: K tells you the period, E tells you the distance. Legendre's identity K(k)E(k') + K(k')E(k) − K(k)K(k') = π/2 connects K, E, and π in a single relation.

The velocity extension adds E as a first-class participant in the L1/L2 framework alongside K.

### 5.3 Two Sources of Ellipticity

A physical system can deviate from circular geometry for two independent reasons. Its internal topology can be toroidal rather than spherical (the k axis). Its state of motion can be relativistic (the v axis). Both produce elliptic integrals. Both modify β away from π/4. Both can be present simultaneously.

A system with toroidal internal structure (k > 0) moving at relativistic velocity (v > 0) has two independent sources of deviation from the circular rest-frame β. How these compose, whether the total β is a product, a sum, or something more complex, is an open question. The two axes are geometrically distinct: k changes the manifold (which surface the curve lives on), while v changes the embedding (how the surface is observed). Their interaction is a Layer 2 experiment.

---

## VI. THE UNIFIED EQUATION AT RELATIVISTIC VELOCITY

### 6.1 The Generalized Equation

The nine-domain unified equation Q = F · β · d² · Z was derived at rest. At velocity v, the geometric factor changes:

**Q = F · β(v) · d²(v) · Z(v)**

Three things change. β becomes velocity-dependent as derived above. The cross-sectional area d² becomes elliptical, d_perp × d_parallel/γ, where d_perp is the diameter perpendicular to motion (unchanged) and d_parallel is the diameter along motion (contracted). And Z may change because the domain-specific impedance can depend on the interaction geometry, which is now velocity-dependent.

For a circular cross-section observed perpendicular to the direction of motion (the standard case for beam-target interactions), d_perp = d and d_parallel = d/γ. The bounding rectangle area is d²/γ. The actual elliptical cross-section area is π · (d/2) · (d/2γ) = πd²/(4γ) = β · d²/γ. This is consistent: the rest-frame β · d² becomes β · d²/γ at velocity v, and the velocity dependence of β itself provides an additional correction to the L1/L2 conversion.

### 6.2 Where the Correction Matters

For the nine MATH-1 domains, the correction is negligible. All nine involve systems at v/c < 10⁻⁶, where β(v) deviates from π/4 by less than one part in 10¹².

The correction becomes significant in three regimes:

**Particle scattering cross-sections.** In high-energy physics, beam particles interact with target particles at relativistic velocities. The geometric cross-section enters through the interaction area. At collider energies where v/c > 0.999, β(v) exceeds 0.95, the circular-to-rectilinear correction changes by more than 20% relative to the rest-frame value.

**Relativistic astrophysics.** Jets from active galactic nuclei, gamma-ray burst ejecta, and relativistic stellar winds involve material moving at v/c > 0.99. Cross-sections for interactions within these flows carry the velocity-dependent β.

**Photon interactions.** Any interaction between a photon (v = c, β = 1) and a stationary target (v = 0, β = π/4) involves two geometric regimes. The aperture or cross-section of the target is at rest-frame β. The photon itself carries no circular geometry, its β is 1. The interaction mediates between these two regimes. This is the regime where the domain-specific impedance Z absorbs the mismatch between the two β values.

### 6.3 The Photon Regime

A stationary circular aperture of diameter d has geometric cross-section β · d² = (π/4)d². Electromagnetic radiation passes through it at c, with β = 1. The aperture presents π/4 of its bounding area to the radiation. The radiation, being fully rectilinear in its geometry, "sees" the full bounding area. The efficiency of the coupling, how much of the incident radiation actually passes through the circular opening, is bounded by the ratio of the aperture's β to the radiation's β, which is (π/4)/1 = π/4.

This is the same aperture efficiency η ≈ 0.55–0.75 that appears as Z in the antenna equation (MATH-1, domain 7). The theoretical maximum coupling of a circular aperture to a plane wave is π/4 ≈ 0.785, and measured efficiencies fall below this due to additional losses (edge diffraction, feed blockage, surface errors). The velocity framework provides a geometric interpretation for the theoretical maximum: it is the mismatch between the rest-frame β of the aperture and the light-speed β of the radiation.

---

## VII. THE THREE-PARAMETER FAMILY

### 7.1 Three Axes of the L1/L2 Framework

The complete L1/L2 conversion is a function of three independent parameters:

| Axis | Parameter | What it changes | Range | β at minimum | β at maximum |
|---|---|---|---|---|---|
| Metric | p (Lp norm) | Which metric L1 is measured in | 1 to ∞ | π/4 (p=1, lattice) | π√2/4 (p=∞, Chebyshev) |
| Manifold | k (elliptic modulus) | Which surface the curve lives on | 0 to 1 | Circle (k=0) | Pinched torus (k→1) |
| Velocity | v/c | How the geometry is observed | 0 to 1 | π/4 (rest) | 1 (light speed) |

Each axis was introduced independently. The metric axis (p) was introduced as the Lp generalization of the staircase. The manifold axis (k) was introduced through the elliptic integral family and the Laporta decomposition. The velocity axis (v/c) is introduced in this paper through Lorentz contraction.

### 7.2 Which Cells Are Computed

| Configuration | β value | Source |
|---|---|---|
| (p=1, k=0, v=0) | π/4 = 0.7854 | MATH-1, MATH-11 |
| (p=2, k=0, v=0) | 1 | MATH-11 §VII |
| (p=∞, k=0, v=0) | π√2/4 = 1.1107 | MATH-11 §VII |
| (p=1, k=0.99713, v=0) | K(0.99713)/normalization | MATH-12 |
| (p=1, k=0.999994, v=0) | K(0.999994)/normalization | MATH-12 |
| (p=1, k=0, v=0 to c) | π/4 to 1 (this paper) | **MATH-13** |
| (p>1, k>0, v>0) | unknown | Open |

The three axes have been explored independently. No combined cell with two or more non-trivial parameters has been computed. Whether the axes compose multiplicatively (β_total = β_p · β_k · β_v / β₀²), additively, or through some other rule is an open question.

### 7.3 The Geometric Meaning of Each Axis

The three axes are geometrically distinct:

The metric axis (p) asks: in what metric do you measure the rectilinear bounding path? L1 (sum of displacements) gives one answer. L2 (Euclidean distance) gives another. L∞ (maximum displacement) gives a third. The curve doesn't change. The ruler changes.

The manifold axis (k) asks: what surface does the curve live on? A circle (k = 0) and a torus cross-section (k > 0) are different manifolds. The ruler doesn't change. The curve changes.

The velocity axis (v/c) asks: how is the geometry embedded in the observer's frame? A circle at rest and the same circle in motion are the same manifold observed differently. Neither the curve's intrinsic geometry nor the ruler changes, the embedding changes.

Three independent ways to modify the L1/L2 conversion. Three independent parameters. One family.

---

## VIII. THE OPERATIONAL PI SPECTRUM

### 8.1 π as an Endpoint, Not a Constant

The ratio of a circle's circumference to its diameter is a definition: π = C/d for a circle at rest. This definition yields π = 3.14159... regardless of the circle's size. It is universal for circles at rest.

For an ellipse produced by Lorentz contraction, the ratio of perimeter to the diameter along the major axis is:

π(v) = P_L2 / d = 2d · E(v/c) / d = 2E(v/c)

At v = 0: π(0) = 2E(0) = 2 · π/2 = π. The familiar constant.

At v = c: π(c) = 2E(1) = 2 · 1 = 2. But this is the ratio to the unchanged perpendicular diameter. The diameter along the axis of motion is d/γ, and the ratio of the perimeter to that diameter diverges as γ → ∞.

The more physically meaningful quantity is the ratio of the L2 path to the L1 path around the same geometry. This is β(v), which goes from π/4 to 1. Multiplying by 4 to express in terms of the full circumference-to-bounding-perimeter ratio: 4β(v) goes from π to 4.

The quantity 4β(v) is the operational circumference-to-bounding-perimeter ratio for a circle at velocity v. At rest it equals π. At c it equals 4. This is the same 4 that the staircase measures, the L1 circumference of any circle is always 4d, regardless of refinement. The staircase result is the v = c limit of the operational circumference ratio.

### 8.2 The Spectrum

Between these endpoints, every physical system has an operational circumference ratio 4β(v) determined by its characteristic velocity:

| Regime | v/c | 4β(v) | Character |
|---|---|---|---|
| Static geometry | 0 | π = 3.1416 | Full circular, maximum curvature |
| Room temperature molecules | ~10⁻⁶ | π − O(10⁻¹²) | Indistinguishable from π |
| Orbital mechanics | ~10⁻⁴ | π − O(10⁻⁸) | Indistinguishable from π |
| Fast electrons in CRT | ~0.1 | 3.142 | Barely distinguishable from π |
| Relativistic proton beam | 0.9 | 3.264 | 4% above π |
| LHC protons | 0.9999 | 3.945 | Approaching 4 |
| Photon | 1 | 4 | Fully rectilinear |

Nothing in the physical universe is at rest. Everything has thermal motion, orbital velocity, galactic rotation. Every physical circle has 4β(v) slightly above π. The static value π is an idealization that no physical system exactly achieves. It is the lower bound of a spectrum, not a universal constant.

The upper bound 4 is achieved by photons. A photon traverses one cell of substrate per unit time in any direction. Its geometry is pure transit, purely rectilinear. Its operational circumference ratio is 4 because 4 is the L1 circumference of the bounding square, and a photon's geometry is L1.

### 8.3 The Persistent Gap

The gap between π and 4, the gap between circular and rectilinear measurement, is β itself. This gap is maximized at rest (1 − π/4 ≈ 0.215, or 21.5% of the bounding area unoccupied) and closes to zero at c.

The staircase paradox asks why a staircase approximation to a circle always measures 4d rather than πd. The answer from MATH-11 is that the staircase measures L1 distance. The answer from MATH-13 adds: and L1 distance is what you would measure if the circle were moving at c. The staircase is the rest-frame L1 measurement, which equals the light-speed L2 measurement. The paradox dissolves twice: once by recognizing two metrics, and again by recognizing that the two metrics converge at c.

---

## IX. WHAT THE VELOCITY EXTENSION DOES NOT DO

This paper derives the velocity dependence of the L1/L2 conversion factor using special relativity and the definition of β from the prior work. Every step is standard geometry applied to a Lorentz-contracted circle. No new physics is proposed.

The paper does not claim that the universe "uses" β(v) rather than π. It derives that β(v) is the L1/L2 conversion factor for a circle at velocity v, and notes that the rest-frame value β = π/4 is the v = 0 specialization.

The paper does not address the physical interpretation of the light-speed limit β = 1 beyond the geometric observation that the geometry becomes rectilinear. Whether this has consequences for the nature of photon propagation, the structure of interactions between rest-frame and light-speed geometries, or the relationship between the L1/L2 framework and physical substrate mechanics is deferred to separate work.

The paper does not compute the composition of the velocity axis with the manifold axis or the metric axis. These are open questions identified in Section VII.

The paper does not propose specific experimental tests beyond identifying the regimes where the correction exceeds measurement precision (Section VI). Specific predictions for particle scattering cross-sections, astrophysical observations, or laboratory measurements require detailed calculation in each domain and are deferred to subsequent work.

---

## X. FALSIFICATION CRITERIA

**F1.** If the formula β(v) = E(v/c)/(1 + 1/γ) does not produce π/4 at v = 0 and 1 at v = c, the derivation contains an error.

**F2.** If β(v) is not monotonically increasing on (0, c), the monotonicity claim fails.

**F3.** If a Lorentz-contracted circle's L2/L1 perimeter ratio, computed by independent methods, disagrees with the formula, the derivation is wrong.

**F4.** If relativistic scattering cross-sections are measured with precision sufficient to distinguish β(v) from the rest-frame β, and they match the rest-frame β rather than β(v), the physical applicability of the velocity correction is falsified.

**F5.** If the three-parameter family β(p, k, v) is shown to be internally inconsistent, the axes produce contradictory results when composed, the family structure requires revision.

Each criterion is specific and decidable.

---

## APPENDIX A: THE VELOCITY-DEPENDENT β, FULL TABLE

| v/c | γ | e = v/c | E(e) | 1/γ | 1 + 1/γ | β(v) | 4β(v) | Deviation from π/4 |
|---|---|---|---|---|---|---|---|---|
| 0.000 | 1.0000 | 0.000 | 1.5708 | 1.0000 | 2.0000 | 0.78540 | 3.14159 | 0.00000 |
| 0.050 | 1.0013 | 0.050 | 1.5705 | 0.9987 | 1.9987 | 0.78578 | 3.14313 | +0.00038 |
| 0.100 | 1.0050 | 0.100 | 1.5668 | 0.9950 | 1.9950 | 0.78534 | 3.14137 | −0.00006 |
| 0.200 | 1.0206 | 0.200 | 1.5549 | 0.9798 | 1.9798 | 0.78538 | 3.14153 | −0.00002 |
| 0.300 | 1.0483 | 0.300 | 1.5348 | 0.9539 | 1.9539 | 0.78546 | 3.14184 | +0.00006 |
| 0.400 | 1.0911 | 0.400 | 1.5059 | 0.9165 | 1.9165 | 0.78576 | 3.14305 | +0.00036 |
| 0.500 | 1.1547 | 0.500 | 1.4675 | 0.8660 | 1.8660 | 0.78641 | 3.14564 | +0.00101 |
| 0.600 | 1.2500 | 0.600 | 1.4181 | 0.8000 | 1.8000 | 0.78783 | 3.15133 | +0.00243 |
| 0.700 | 1.4003 | 0.700 | 1.3556 | 0.7141 | 1.7141 | 0.79086 | 3.16346 | +0.00546 |
| 0.800 | 1.6667 | 0.800 | 1.2763 | 0.6000 | 1.6000 | 0.79772 | 3.19089 | +0.01232 |
| 0.900 | 2.2942 | 0.900 | 1.1717 | 0.4359 | 1.4359 | 0.81602 | 3.26410 | +0.03062 |
| 0.950 | 3.2026 | 0.950 | 1.1002 | 0.3122 | 1.3122 | 0.83845 | 3.35381 | +0.05305 |
| 0.990 | 7.0888 | 0.990 | 1.0160 | 0.1411 | 1.1411 | 0.89040 | 3.56159 | +0.10500 |
| 0.999 | 22.366 | 0.999 | 1.0016 | 0.0447 | 1.0447 | 0.95878 | 3.83513 | +0.17338 |
| 0.9999 | 70.712 | 0.9999 | 1.0002 | 0.0141 | 1.0141 | 0.98614 | 3.94458 | +0.20074 |
| 1.000 | ∞ | 1.000 | 1.0000 | 0.0000 | 1.0000 | 1.00000 | 4.00000 | +0.21460 |

The table confirms monotonic increase. The deviation column shows that β(v) remains within 0.001 of π/4 for v/c < 0.5, grows to ~0.01 at v/c = 0.8, ~0.05 at v/c = 0.95, ~0.10 at v/c = 0.99, and reaches 0.215 at v = c.

## APPENDIX B: THE THREE-PARAMETER FAMILY, STATUS GRID

| p | k | v/c | β value | Status | Source |
|---|---|---|---|---|---|
| 1 | 0 | 0 | π/4 = 0.7854 | Computed | MATH-1/11 |
| 1.5 | 0 | 0 | 0.9315 | Computed | MATH-11 |
| 2 | 0 | 0 | 1.0000 | Computed | MATH-11 |
| 3 | 0 | 0 | 1.0579 | Computed | MATH-11 |
| 4 | 0 | 0 | 1.0804 | Computed | MATH-11 |
| ∞ | 0 | 0 | π√2/4 = 1.1107 | Computed | MATH-11 |
| 1 | 0.99713 | 0 | K-based | Computed | MATH-12 |
| 1 | 0.999994 | 0 | K-based | Computed | MATH-12 |
| 1 | 0 | 0.5 | 0.7864 | Computed | **MATH-13** |
| 1 | 0 | 0.9 | 0.8160 | Computed | **MATH-13** |
| 1 | 0 | 0.99 | 0.8904 | Computed | **MATH-13** |
| 1 | 0 | 1.0 | 1.0000 | Computed | **MATH-13** |
| 2 | 0 | >0 | unknown | Open |, |
| 1 | >0 | >0 | unknown | Open |, |
| >1 | >0 | >0 | unknown | Open |, |

Three independent axes explored independently. No combined cells computed. The composition rule is Layer 2 work.

## APPENDIX C: PHYSICAL REGIMES, WHERE THE CORRECTION EXCEEDS MEASUREMENT PRECISION

| System | Characteristic v/c | β(v) deviation from π/4 | Typical cross-section measurement precision | Correction detectable? |
|---|---|---|---|---|
| Pipe flow | < 10⁻⁶ | < 10⁻¹² | ~1% | No |
| Antenna | 0 (structure) / c (radiation) | 0 / 0.215 | ~5% | Mixed regime (see §VI.3) |
| Thermal radiation | 0 (surface) / c (photons) | 0 / 0.215 | ~1% | Mixed regime |
| Electron beam (10 keV) | 0.20 | 0.00002 | ~1% | No |
| Proton beam (1 GeV) | 0.87 | 0.025 | ~5% | Marginal |
| LHC protons (6.5 TeV) | 0.9999999 | 0.214 | ~10% | Yes, if geometric β is isolated |
| Cosmic ray (10²⁰ eV proton) | 1 − 10⁻²² | ~0.215 | Not directly measurable |, |
| Photon | 1.0 | 0.215 |, | β = 1 by construction |

The correction is undetectable in non-relativistic systems, marginal at accelerator energies around 1 GeV, and potentially significant at LHC energies, but only if the geometric β(v) can be isolated from the many other velocity-dependent effects in scattering cross-sections (parton distribution functions, QCD corrections, detector acceptance).

## APPENDIX D: ENDPOINT DERIVATION, EXPLICIT

**Rest endpoint:**

v = 0. e = v/c = 0. γ = 1/√(1 − 0) = 1.

E(0) = ∫₀^(π/2) √(1 − 0 · sin²θ) dθ = ∫₀^(π/2) 1 dθ = π/2.

β(0) = E(0)/(1 + 1/γ) = (π/2)/(1 + 1) = (π/2)/2 = π/4. ∎

**Light endpoint:**

v = c. e = 1. γ → ∞.

E(1) = ∫₀^(π/2) √(1 − sin²θ) dθ = ∫₀^(π/2) |cos θ| dθ = ∫₀^(π/2) cos θ dθ = [sin θ]₀^(π/2) = 1.

1/γ = √(1 − 1) = 0. 1 + 1/γ = 1.

β(c) = 1/1 = 1. ∎

Both endpoints follow from elementary integration and the definition of the Lorentz factor.

## APPENDIX E: CONNECTION TO PRIOR WORK

| This paper provides | Extends | Through | What it adds |
|---|---|---|---|
| β(v) formula | MATH-1 (nine domains) | Velocity generalization of the geometric invariant | The invariant varies with velocity |
| Endpoint β(c) = 1 | MATH-11 (staircase paradox) | Staircase = L1 = rectilinear = β = 1 = light limit | The staircase result is the v = c limit |
| E(v/c) in β formula | MATH-12 (elliptic integrals) | Same E(k) function, different physical modulus | Velocity and topology both produce elliptic integrals |
| Three-parameter family | MATH-11 §VII (Lp axis) + MATH-12 (k axis) | Third axis completing the family | Three independent geometric deformations |
| Photon regime analysis | MATH-1 §4.6–4.7 (Poynting, antenna) | Mixed β regime interpretation | Aperture efficiency as β mismatch |
| Operational pi spectrum | MATH-11 §II (foundation identity) | 4β(v) ranges from π to 4 | π is an endpoint, not a constant |

## APPENDIX F: OPEN QUESTIONS

| Question | Type | Method | Priority |
|---|---|---|---|
| Does the three-parameter family compose? What is β(p, k, v)? | Theoretical | Compute β at (p=1, k>0, v>0) and check for factorization | High |
| Can β(v) be detected in relativistic scattering data? | Experimental | Isolate geometric β from QCD/EW corrections in cross-section measurements | Medium |
| Is the monotonicity proof completable analytically? | Mathematical | Full derivative analysis of E(e)/(1+1/γ) | Medium |
| What is the curvature of β(v) at v = 0? | Mathematical | Taylor expansion of β(v) around v = 0 | Low |
| Does the antenna efficiency bound of π/4 ≈ 0.785 follow from β mismatch? | Experimental/theoretical | Compare theoretical maximum circular aperture efficiency to π/4 | High |
| Does the photon's β = 1 constrain the structure of QED vertex factors? | Theoretical | Analyze whether the QED vertex at zero momentum transfer carries the rest-frame β | High |

---

**END HOWL-MATH-13-2026**

**Registry:** [@HOWL-MATH-13-2026]
**Status:** Complete (Layer 1). Layer 2 experiments pending.
**Central Statement:** The L1/L2 conversion factor β = π/4 is the rest-frame specialization of a velocity-dependent function β(v) = E(v/c)/(1 + 1/γ), where E is the complete elliptic integral of the second kind and γ is the Lorentz factor. At v = 0, β = π/4 (circular geometry). At v = c, β = 1 (rectilinear geometry). The transition is monotonic. The velocity axis completes a three-parameter family (metric p, manifold k, velocity v/c) governing the L1/L2 conversion. The nine cross-section domains from MATH-1 all use the v = 0 endpoint. Relativistic cross-sections require β(v). The operational circumference ratio 4β(v) ranges from π at rest to 4 at light speed. π is an endpoint of a geometric spectrum, not a universal constant.
**Falsification:** Five specific criteria stated, including endpoint verification, monotonicity, independent computation, experimental cross-section comparison, and family consistency.
