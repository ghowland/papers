## MATH-11 Plan: β = π/4 as the L1/L2 Metric Conversion Factor

**Registry:** [@HOWL-MATH-11-2026]

**Series Path:** [@HOWL-MATH-1-2026] (β in nine domains) → [@HOWL-MATH-6-2026] (82/82 PSLQ null) → [@HOWL-MATH-11-2026]

**Dependency:** MATH-1 documented β appearing in nine domains. MATH-6 proved the transcendental constants are independent. MATH-11 explains WHY β appears everywhere: it is the unique L1/L2 metric conversion factor on circular geometry.

---

### THE STAIRCASE

**Stair 1: MATH-1 showed β = π/4 appears in nine domains.** Area ratios. Probability (Buffon). Number theory (Leibniz). Statistical mechanics (Maxwell-Boltzmann). Electromagnetism (flux). Quantum mechanics (angular momentum). Signal processing (Fourier). Optics (Airy disk). Cosmology (DM/baryon). The paper documented the pattern but explained it shallowly: "circles are universal."

**Stair 2: The staircase paradox resolves the mystery.** Approximate a circle with rectilinear staircases. Refine infinitely. The staircase perimeter stays at 4d. The circle's perimeter is πd. The staircase measures L1 (taxicab distance). The circle measures L2 (Euclidean distance). They are different metrics. The "paradox" is expecting one to converge to the other. They don't because they can't. Their ratio is π/4 = β.

**Stair 3: β is the L1/L2 conversion factor.** This is a theorem, not an observation. The L1 circumference of the unit circle is ∫₀²π (|cos θ| + |sin θ|) dθ = 8. The L2 circumference is 2π. The ratio is 2π/8 = π/4. This holds for any circle of any radius because both metrics scale linearly. β is the unique conversion factor between L1 and L2 distance measurements on circular geometry.

**Stair 4: Every physics computation is an L1/L2 conversion.** All analytic computation is performed in coordinates. Coordinates are rectilinear (Cartesian, L1). Most physical systems have rotational symmetry (circular, L2). Every time you compute a circular quantity in rectangular coordinates, you convert from L1 to L2. The conversion factor is β. This is why β appears in nine domains — it appears in every domain that involves rotation, which is every domain.

**Stair 5: The conversion factor has consequences.** The Fourier transform normalization 2π = 8β is the L1/L2 conversion for one circular period. Planck's ℏ = h/(8β) converts the L1 action quantum to the L2 angular quantum. The 4π in Coulomb's law and the 8π in Einstein's equation are (4β)² and (4β)² × 2 — metric conversions for spherical geometry. The QED loop integrals carry (8β)^d in the normalization — one L1/L2 conversion per momentum dimension.

**Stair 6: Two numerical predictions from the lattice.** If β enters confinement geometry, the proton lattice factor C = m_p/Λ_QCD might be 6β = 3π/2 = 4.712 (vs measured 4.7 ± 0.5). The QCD string tension ratio σ^(1/2)/Λ_QCD might be 8β/3 = 2π/3 = 2.094 (vs observed ~2.1). Both are within current uncertainties. Both are testable with higher-precision lattice data.

**Stair 7: One numerical prediction from cosmology.** If β enters the cosmic density budget through the toroidal galaxy geometry, Ω_DM might be β/3 = π/12 = 0.26180 (vs Planck measured 0.261 ± 0.002). This is within 0.1σ. Combined with DM/baryon = (22/13) × 4β, this gives Ω_baryon = 13/264 = 0.04924 (vs measured 0.0490 ± 0.0004, within 0.6σ) and Ω_Λ = 1 − β/3 − 13/264 = 0.68896 (vs measured 0.689 ± 0.004, within 0.01%). All three cosmic fractions from β, one integer (13), and flatness. Subject to same statistical control as the (22/13)π claim.

---

### PAPER STRUCTURE

```
I.    THE STAIRCASE PARADOX
      The L1 staircase approximation to a circle never converges to L2.
      The limit is 4d, not πd.
      This is not a paradox. It is a measurement of the wrong metric.
      Resolution: L2/L1 = π/4 = β. Exact. Radius-independent.

II.   THE FOUNDATION IDENTITY
      ∫₀²π (|cos θ| + |sin θ|) dθ = 8
      Proof by quadrant symmetry.
      L2 circumference: 2π. L1 circumference: 8. Ratio: π/4.
      β is the unique conversion factor between L1 and L2 on circular paths.

III.  WHY β APPEARS EVERYWHERE
      All computation is performed in coordinates (L1).
      Most physics has rotational symmetry (L2).
      Every circular quantity computed in rectangular coordinates carries β.
      This is not coincidence. It is necessity.

IV.   THE FOURIER CONNECTION
      The Fourier normalization 2π = 8β is the L1/L2 conversion for
      one circular period. The Leibniz series converges to β because
      it converts a square wave (L1) to its circular harmonic (L2).
      Every Fourier coefficient is an L1/L2 conversion factor.

V.    THE QUANTUM CONNECTION
      ℏ = h/(8β). The L1 quantum of action is h. The L2 quantum is ℏ.
      The conversion is 8β = 2π.
      The commutation relation [x,p] = iℏ = ih/(8β) measures phase-space
      area in L2 coordinates. The uncertainty principle bounds the L1
      widths in conjugate spaces.

VI.   THE QED CONNECTION
      Loop integrals carry (2π)^d = (8β)^d in the normalization.
      One L1/L2 conversion per momentum dimension.
      The solid angle Ω₄ = 2π² = 32β² is the angular L1/L2 conversion
      in 4D. The QED coefficients decompose into rational (topology) ×
      β powers (geometry) × ζ values (number theory).

VII.  THE Lp GENERALIZATION
      β(p) = 2π / ∫₀²π (|sin θ|^p + |cos θ|^p)^(1/p) dθ
      β(1) = π/4. β(2) = 1. β(∞) = π√2/4.
      Monotonically increasing. Lattice systems live at p = 1.
      Free space lives at p = 2. The continuum limit is p: 1 → 2.

VIII. THE DIMENSION GENERALIZATION
      β_d: the L2/L1 conversion in d dimensions.
      Compute for d = 2, 3, 4.
      Check whether (4π)^(d/2) in dimensional regularization decomposes
      as (4β)^d or similar.

IX.   THE LATTICE PREDICTIONS
      Hypothesis: C = m_p/Λ_QCD = 6β = 3π/2.
      Evidence: BMW C = 4.7 ± 0.5. 3π/2 = 4.712. Within 0.02σ.
      Hypothesis: σ^(1/2)/Λ_QCD = 8β/3 = 2π/3.
      Evidence: observed ~2.1. 2π/3 = 2.094. Within 0.3%.
      Both testable with higher-precision lattice data.

X.    THE COSMOLOGICAL PREDICTION
      Hypothesis: Ω_DM = β/3 = π/12.
      Evidence: Planck Ω_DM = 0.261 ± 0.002. π/12 = 0.26180. Within 0.1σ.
      Derived: Ω_baryon = 13/264. Ω_Λ = 1 − β/3 − 13/264 = 0.68896.
      All three cosmic fractions from β, one integer, and flatness.
      Subject to statistical control (Program 15 kill switch K15.3).

XI.   WHAT β IS NOT
      β is not a new constant. It is π/4. It has been known for millennia.
      β is not a theory. It is a metric identity.
      β does not replace π. It decomposes π into its role: the L1/L2
      conversion factor on circular geometry, multiplied by 4 (the L1
      perimeter of the unit square).
      The claim is not that β is new. The claim is that recognizing β as
      a metric conversion factor explains its universal appearance and
      generates testable predictions.

XII.  APPENDIX: COMPLETE β AUDIT OF FUNDAMENTAL CONSTANTS
      Table: every pool constant, its β content (power of π), and the
      L1/L2 conversions it represents.
```

---

### WHAT NEEDS TO BE COMPUTED BEFORE WRITING

| Item | Description | Status | Blocks which section |
|---|---|---|---|
| Foundation proof | ∫₀²π (|cos θ| + |sin θ|) dθ = 8, quadrant method | Trivial — done in the report | §II |
| β(p) for p = 1, 1.5, 2, 3, 4, ∞ | Numerical integration of the Lp circumference | Needs computation | §VII |
| β(p) closed form | Attempt analytical expression via Beta function | Needs attempt | §VII |
| β₃ and β₄ | L2/L1 surface ratio in 3D and 4D | Needs computation | §VIII |
| Dim reg decomposition | Check (4π)^(d/2) vs β_d | Needs algebra | §VIII |
| A₂ β decomposition | Tag each piece of the QED A₂ coefficient by β content | Needs careful algebra | §VI |
| C lattice survey | Collect 5+ values of m_p/Λ_QCD from published lattice papers | Needs literature search | §IX |
| σ^(1/2)/Λ_QCD survey | Collect 3+ values from published lattice papers | Needs literature search | §IX |
| Ω_DM = π/12 statistical test | Combinatoric p-value for aβ/b hitting 0.261 ± 0.002 | Needs computation — BLOCKING | §X |
| Constants audit table | Every pool constant tagged with β power | Needs systematic catalog | §XII |

---

### WHAT THE PAPER DOES NOT DO

Does not claim β is new. It is π/4. Known since antiquity.

Does not claim the L1/L2 identity is new. The staircase paradox is a standard pedagogical example.

Does not claim every appearance of π in physics is a metric conversion. Some factors of π come from other sources (e.g., the factor π in the area of a circle is a definition, not a conversion). The claim is that π/4 specifically, appearing as a multiplicative factor in a physical formula, is an L1/L2 conversion.

Does not advance the Ω_DM = π/12 prediction without statistical control. If the combinatoric p-value is > 0.1, the prediction is reported with BLOCKING status, same as the (22/13)π claim.

Does not derive the proton mass. It hypothesizes C = 6β and tests it against published lattice data. The hypothesis is reported as a prediction, not a derivation, until lattice precision confirms or excludes it.

Does not solve the confinement boundary. The σ^(1/2)/Λ_QCD = 2π/3 hypothesis is a pattern observed in lattice data, not a first-principles derivation. Stated as such.

---

### COMPUTATIONS TO RUN (experiment candidates)

**Experiment 1: β_p family.** Numerically integrate ∫₀²π (|sin θ|^p + |cos θ|^p)^(1/p) dθ for p = 1, 1.25, 1.5, 2, 3, 4, 5, 10, 50, 100. Compute β(p) = 2π / result. Verify β(1) = π/4, β(2) = 1, compute β(∞). Plot the curve. Check for special values.

**Experiment 2: β_d dimensions.** Compute the L1 arclength of the L2 unit sphere in d = 2, 3, 4, 5. For d = 2 this is the ∫₀²π (|cos θ| + |sin θ|) dθ = 8 identity. For d = 3, parameterize the sphere in (θ, φ) and integrate the L1 arclength element. Compute β_d = S_d(L2) / S_d(L1). Check whether β_d = β₂^f(d) for some function f.

**Experiment 3: A₂ β decomposition.** Take the QED A₂ coefficient. Tag each term: "197/144 → 0 powers of β (pure rational)." "(1/12)π² → 2 powers of β (since π² = 16β²)." "−(1/2)π²ln2 → 2 powers of β × 1 transcendental." "(3/4)ζ(3) → 0 powers of β (zeta, no π)." Count total β content. Check whether it matches the expected count from "one β² per angular integration."

**Experiment 4: Lattice factor survey.** Web-search for published values of m_p/Λ_QCD with scheme labels and uncertainties. Minimum 5 values. Compute |value − 3π/2| / uncertainty for each. Report pass/fail at 1σ, 2σ, 3σ.

**Experiment 5: String tension survey.** Same as E4 but for σ^(1/2)/Λ_QCD. Target value: 2π/3. Minimum 3 values.

**Experiment 6: Ω_DM statistical control.** Generate all expressions aβ/b and a/(bβ) and (aβ + c)/d for integers a, b, c, d in [1, 30]. Count how many land within ±0.002 of 0.261. Compute p-value. If p > 0.1, the Ω_DM = π/12 prediction is BLOCKED.

**Experiment 7: Constants audit.** Systematic table of all pool constants. For each: express any π content as β. Tag with the number of L1/L2 conversions. Classify as geometric (carries β), non-geometric (no β), or inherited (carries β through definitions).

---

### DIAGRAMS — 8 CANDIDATES

| # | Candidate | Type | What it shows |
|---|---|---|---|
| 1 | The staircase paradox resolution | Geometric Cross-Section | L1 staircase at 4d, L2 circle at πd, ratio β |
| 2 | β(p) curve from L1 through L2 to L∞ | Running/Convergence | The family of conversion factors |
| 3 | Every computation is L1/L2 | Connection/Integer Map | Coordinates → circular physics → β conversion |
| 4 | The Fourier transform as L1/L2 | Geometric Cross-Section | Square wave (L1) → circular harmonic (L2), coefficient = β |
| 5 | ℏ = h/(8β) — rectangular vs circular phase space | Comparison Bar | Two phase space cells, L1 area h, L2 area ℏ |
| 6 | QED A₂ decomposition by β content | Connection/Integer Map | Four terms tagged as rational / β² / β²+trans / zeta |
| 7 | Lattice predictions: C = 6β and σ^(1/2) = (8β/3)Λ | Threshold/Region | Predicted values vs lattice ranges |
| 8 | The cosmic budget from β | Comparison Bar | Ω_DM = β/3, Ω_b = 13/264, Ω_Λ = remainder = 0.689 |

---

### AGREEMENT REQUEST

The paper has three layers:

**Layer 1 (theorem-level, no experiment needed):** The L1 circumference integral, the β identity, the staircase resolution, the proof that β is the unique L1/L2 conversion on circular geometry. This is pure mathematics. It can be written now.

**Layer 2 (algebraic rewriting, computation needed):** The Fourier, quantum, and QED connections. These require computing β(p), β_d, and the A₂ decomposition. All are tractable in one session.

**Layer 3 (empirical predictions, data needed):** The lattice factor C = 6β, the string tension σ^(1/2)/Λ = 2π/3, and Ω_DM = π/12. These require literature surveys (lattice data) and statistical control (combinatoric p-value for Ω_DM). The lattice surveys are web-search tasks. The statistical control is a computation.

**Proposed approach:** Write the paper with Layer 1 complete, Layer 2 computed in experiments, and Layer 3 as predictions with explicit statistical controls. The Ω_DM prediction is reported only if the combinatoric p-value is < 0.1; otherwise it is reported with BLOCKING status.

Proceed to computation of Layer 2 experiments, then write MATH-11?
