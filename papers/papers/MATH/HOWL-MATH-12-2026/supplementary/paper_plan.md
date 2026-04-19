## MATH-12 Plan: β⁰ Has Two Geometries — The Toroidal Extension of the L1/L2 Framework

**Registry:** [@HOWL-MATH-12-2026]

**Series Path:** [@HOWL-MATH-11-2026] → [@HOWL-MATH-12-2026]

**Dependency:** MATH-11 established β = π/4 as the L1/L2 spherical conversion. MATH-12 extends: the β⁰ sector (terms without π) also carries geometry — toroidal geometry measured by elliptic periods K(k) rather than circular periods π.

---

### THE THESIS

The L1/L2 metric framework has two conversion factors, not one.

**Spherical conversion:** β = π/4. The ratio of L2 (Euclidean) to L1 (taxicab) distance around a circle. Every π in physics is this conversion applied to a spherical or circular subspace. Produces β², β⁴ terms. Understood since MATH-11.

**Toroidal conversion:** K(k)/π. The ratio of the toroidal period to the circular period. K(k) is the complete elliptic integral of the first kind — the "circumference" of a torus cross-section parametrized by modulus k. When k = 0, K = π/2 and the torus degenerates to a circle (K/π = 1/2). When k → 1, K → ∞ and the torus becomes infinitely elongated.

The β⁰ sector — terms without π — was treated as geometry-free in MATH-11. MATH-12 shows it contains toroidal geometry that doesn't produce π because the torus has a different angular structure than the sphere. The sphere's angular integration gives π. The torus's angular integration gives K(k). Both are geometric. Only one produces π.

---

### WHAT MATH-11 ESTABLISHED (REVIEW)

1. β = π/4 is unique: the only L1/L2 ratio on a unit circle
2. The foundation identity: β = (1/2)∫₀¹ 1/√(x−x²) dx
3. Nine domains where β appears (QED, Fourier, Boltzmann, etc.)
4. The Lp generalization: β(p) interpolates between 1 (L1) and β (L2) and β(∞) = 1/√2 (L∞)
5. The dimension generalization: βₙ = Vₙ/(2r)ⁿ for n-ball in n-cube
6. The A₂ decomposition: 90.4% cancellation between β² and β⁰

MATH-11 left β⁰ unexplored. It said: "these terms carry no angular content." MATH-12 corrects this.

---

### WHAT MATH-12 ADDS

**Section I: The L1/L2 Framework Has a Gap**

MATH-11's classification assumed two categories: terms with π (geometric, from angular integrations) and terms without π (non-geometric, from counting and radial integrations). This is incomplete. A torus has angular structure — you can integrate around it — but the integration doesn't produce π. It produces K(k). The MATH-11 framework missed toroidal geometry because it used π as the sole marker of angular content.

The fix: the marker of angular content is not π specifically but PERIOD INTEGRALS generally. π = 2∫₀¹ 1/√(1−x²) dx is the period of the circle. K(k) = ∫₀¹ 1/√((1−x²)(1−k²x²)) dx is the period of the elliptic curve y² = (1−x²)(1−k²x²). Both are angular periods. The circle produces π. The elliptic curve produces K(k). Both are L1/L2-type conversions — they measure how much the curved path exceeds the straight path.

**Section II: The Toroidal L1/L2 Conversion**

Define β_T(k) = K(k)/π — the toroidal period normalized by the circular period.

Properties:
- β_T(0) = 1/2: degenerate torus = circle. K(0) = π/2, so K/π = 1/2.
- β_T(k) increases monotonically with k
- β_T(1) = ∞: degenerate torus = infinitely elongated
- β_T(k) = β₂(k) in a natural sense: β₂ = π/4 is the 2D spherical conversion, β_T is the 2D toroidal conversion

The spherical β = π/4 ≈ 0.785 is a fixed number. The toroidal β_T(k) is a function of the modulus k — it depends on the shape of the torus. Every torus has its own conversion factor. The sphere has one universal conversion factor.

This is why the Laporta constants are more complex than π: π is one number (one sphere). The Laporta constants involve K at specific moduli (specific tori). Different topologies, different moduli, different K values.

**Section III: The Foundation Identity Extended**

MATH-11's foundation identity: β = (1/2)∫₀¹ 1/√(x − x²) dx.

The toroidal extension: K(k) = ∫₀¹ 1/√((1−x²)(1−k²x²)) dx.

When k = 0: the integrand becomes 1/√(1−x²), and K(0) = π/2 = 2β. The torus degenerates to a circle. The toroidal integral reduces to the spherical integral.

The relationship: set x = sin θ in both integrals. β comes from ∫dθ over a circle. K(k) comes from ∫dθ/√(1−k²sin²θ) over an ellipse. The ellipse is the cross-section of the torus. The k parameter measures the eccentricity of the cross-section.

β is the SPECIAL CASE k = 0 of the general toroidal period K(k)/2. The L1/L2 framework isn't two separate conversion factors — it's ONE family parametrized by k. At k = 0: spherical (β). At k > 0: toroidal (K(k)/2).

**Section IV: The β⁰ Subcategory Split**

With the extended framework, β⁰ splits:

Number-theoretic β⁰: rational numbers, ζ(n), Li_n(½), MZVs. These arise from RADIAL integrations — momentum magnitudes, not angles. No angular period of any kind (circular or elliptic). Genuinely geometry-free.

Toroidal-geometric β⁰: elliptic periods K(k), E(k) at specific moduli. These arise from ANGULAR integrations on tori — the same type of integration that produces π on a sphere, but on a different manifold. Geometric, but not spherical.

The classification by π power (β⁰, β², β⁴) is a spherical classification. It detects spherical angular content but is blind to toroidal angular content. MATH-12 adds the toroidal axis.

**Section V: Evidence — The Cancellation Staircase**

The data from experiment_beta_content_a3_v0 and experiment_math11_beta_metric_v0:

| Loop | β⁰ (non-spherical) | β² (one spherical) | β⁴ (two spherical) | Cancellation |
|---|---|---|---|---|
| 1 | 100% | 0% | 0% | 0% |
| 2 | 46.6% | 53.4% | 0% | 90.4% |
| 3 | 51.3% | 24.7% | 24.0% | 99.5% |
| 4 | >51% (includes toroidal) | ? | ? | ? |

At loops 1-3, the β⁰ sector is entirely number-theoretic (layer 1). The cancellation between β⁰ and β² tightens by ~10 pp per loop. At loop 4, toroidal content enters β⁰ for the first time. The cancellation breaks because the toroidal constants cannot participate in algebraic cancellation with spherical constants.

**Section VI: Evidence — The Control Experiment**

The A₂ β⁰ remainder matches elliptic forms 2.05× better than the A₂ β² modulus. Same scan parameters, same candidate count, similar target magnitudes.

This is the L1/L2 framework's prediction: the remainder (β⁰) has toroidal affinity because it contains geometric content that the spherical classification can't see. The modulus (β²) has spherical affinity because it IS the spherical content. The control confirms the framework.

**Section VII: Evidence — The ζ Subtraction**

Each Laporta integral decomposes as ζ piece + elliptic piece. Removing the ζ (number-theoretic β⁰, layer 1) reveals the elliptic (toroidal-geometric β⁰, layer 2) with 7-266× improvement. 6/6 improved.

In L1/L2 language: the integral contains both radial content (ζ from momentum magnitude integrations) and toroidal angular content (K, E from angular integrations on the torus). Subtracting the radial content isolates the angular content. The angular content matches elliptic forms at 12-1200 ppb.

**Section VIII: Evidence — Topology-Specific Moduli**

Three integrals within topology 81 yield k₈₁ = 0.999994 at 167 ppb consistency. Three within topology 83 yield k₈₃ = 0.99713 at 25 ppm consistency.

In L1/L2 language: each Feynman diagram topology determines a specific torus (specific k). The modulus is a property of the diagram, not of the integral. All three master integrals from the same topology share the same torus. This is the analog of how all spherical integrals share the same sphere (same π).

**Section IX: The Complete L1/L2 Conversion Table**

| Geometry | Manifold | Period integral | Conversion factor | Produces | QED presence |
|---|---|---|---|---|---|
| Circular | S¹ | ∫dθ = 2π | β = π/4 | π powers | All loops |
| Spherical | S² | ∫∫sinθ dθdφ = 4π | 4β² = π²/4 | π² | Loops 2+ |
| Toroidal (k) | T² | ∫dθ/√(1−k²sin²θ) = K(k) | β_T(k) = K(k)/π | K(k) | Loop 4+ |

The table shows the L1/L2 framework is a FAMILY of conversions indexed by topology. The circular and spherical conversions are k = 0 specializations. The toroidal conversion is the general case.

**Section X: The Muon Sees the Torus**

The mass-dependent four-loop corrections scale as (m/mₑ)². For the electron: toroidal sector is 0.054% of universal. For the muon: 2304%. The crossover is at 43 mₑ ≈ 22 MeV.

In L1/L2 language: the probe mass determines how strongly the particle couples to the toroidal conversion factor. A light particle (electron) doesn't resolve the torus — it sees only the spherical average (β). A heavy particle (muon) resolves the torus — it sees β_T(k) directly. The mass sets the resolution scale.

**Section XI: What MATH-11 Got Wrong**

MATH-11 stated: "terms without π carry no angular content." This is corrected to: "terms without π carry no SPHERICAL angular content. They may carry TOROIDAL angular content through K(k)."

MATH-11's classification (β⁰, β², β⁴) is correct as a spherical classification. It is incomplete as a geometric classification. The complete classification has two axes: spherical β power (counting π) and toroidal β_T content (counting K(k)).

The correction does not invalidate MATH-11. It extends it. Every result in MATH-11 (the foundation identity, the nine domains, the Lp generalization, the A₂ decomposition) remains correct. MATH-12 adds the second axis.

**Section XII: Predictions**

1. The A₃ β⁰ remainder's match to KE at k = 0.99 (1.8 ppm) is real — the toroidal structure is already embryonic at three loops. Testable: does the A₃ remainder enter derivation chains that reach measured values?

2. The toroidal conversion β_T(k) should appear in other domains beyond QED wherever toroidal topology exists: magnetic confinement (tokamak geometry), flux tubes in QCD, the galactic disk. The conversion factor K(k)/π should appear in the same structural position that β = π/4 occupies for spherical domains.

3. At five loops, new moduli should appear from new topologies. Each topology defines a k, and K(k) at that modulus enters the coefficient. The number of independent elliptic moduli should grow with loop order.

4. The near-singular moduli (k₈₁ = 0.999994, k₈₃ = 0.99713) should be derivable from the Feynman diagram propagator structure. The modulus is not a free parameter — it is computed from the diagram. A derivation chain from diagram topology to k to K(k) to A₄ contribution would close the loop.

---

### PAPER STRUCTURE

```
I.     The Gap in MATH-11
II.    The Toroidal L1/L2 Conversion: β_T(k) = K(k)/π
III.   The Foundation Identity Extended
IV.    β⁰ Splits: Number-Theoretic vs Toroidal-Geometric
V.     The Cancellation Staircase (data)
VI.    The Control Experiment (data)
VII.   The ζ Subtraction (data)
VIII.  Topology-Specific Moduli at 167 ppb (data)
IX.    The Complete L1/L2 Conversion Table
X.     The Muon Sees the Torus (data)
XI.    What MATH-11 Got Wrong
XII.   Predictions
```

---

### WHAT NEEDS TO BE COMPUTED

Nothing. All data from existing experiments. The paper is mathematical framework applied to already-computed results.

---

### APPENDIX TABLES — 12

| Table | Content |
|---|---|
| A.1 | The L1/L2 conversion family: circle, sphere, torus |
| A.2 | β_T(k) values at key moduli (0, 0.5, 0.9, 0.99, 0.999, 0.999994) |
| A.3 | The β⁰ subcategory taxonomy with examples |
| A.4 | A₂ three-layer decomposition (modulus, layer 1, layer 2) |
| A.5 | A₃ three-layer decomposition |
| A.6 | The cancellation staircase with three-layer context |
| A.7 | Control experiment: remainder vs modulus elliptic affinity |
| A.8 | ζ subtraction results: 6 integrals, improvements |
| A.9 | Topology-specific moduli: k₈₁, k₈₃, consistency spreads |
| A.10 | Electron vs muon: spherical vs toroidal dominance |
| A.11 | The L1/L2 family across physics domains |
| A.12 | Predictions and kill switches |

---

### AGREEMENT REQUEST

MATH-12 is a mathematics paper, not a physics paper. It extends the L1/L2 framework (MATH-11) with a second conversion factor (toroidal K(k)/π) and uses physics data (QED coefficients, Laporta constants, muon/electron scaling) as evidence. No new computation. All results from eight completed experiments.

The core mathematical contribution: β = π/4 and β_T(k) = K(k)/π are members of the same family of L1/L2 conversions, parametrized by the modulus k. At k = 0: sphere. At k > 0: torus. The QED perturbation series transitions from k = 0 (loops 1-3) to k > 0 (loop 4) — a geometric phase transition in the L1/L2 framework.
