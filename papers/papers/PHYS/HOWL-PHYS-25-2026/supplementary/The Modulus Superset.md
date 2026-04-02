## The Modulus Superset — Soliton Boundaries as Geometric Stages in the Running

**Status:** Active conceptual notebook. Highest-level framing of the Hubble tension within the remainder framework.
**Origin:** Session 4, April 2 2026, post PHYS-15
**Depends on:** PHYS-10/11 (remainder framework, Subgroup B), PHYS-14 (fermion cancellation, domain map), PHYS-5/9 (VP running as prototype), Bessel zero barrier notebook, composite soliton hierarchy notebook

---

### 1. THE CONCEPT

The VP running provides the cleanest example. Between m_e and M_Z, the electromagnetic coupling α runs through a sequence of domains. At each domain boundary (mass threshold), the running rule changes — a new fermion activates and the beta coefficient updates. Between boundaries, the running accumulates logarithmically according to the current rule.

The key structural insight: the running between two thresholds is not just "the coupling changed by some amount." The running WITHIN a domain has internal structure. The VP function R_f(q², m_f²) has a specific shape: it starts at 0 at the threshold, rises logarithmically, and has a specific functional form involving arctanh and the boundary constant 1/3. The shape is determined by the geometry of the VP cloud (spherical, with R₂ content through the 1/(3π) = 1/(12R₂) step size).

Now extend this to the cosmological case. Between two soliton boundaries along a line of sight, light propagates through a domain with specific geometric properties (the interior of a soliton — a galaxy, a cluster, a void, etc.). The correction to H₀ accumulated within that domain has a specific functional form determined by the domain's geometry. The total H₀ correction is the product of all domain contributions — one per domain crossed.

The "modulus superset" concept: each soliton boundary is not just a point where the correction rule changes. It defines a GEOMETRIC STAGE — a domain with internal structure. The boundary's geometry (sphere, torus, irregular) determines what PATTERN the accumulation follows within that domain. The full running from here to the CMB is a sequence of geometric stages, each with its own accumulation pattern, stitched together at the boundaries.

---

### 2. SHELLS WITHIN THE BOUNDARY

The VP function within a single domain (say, between m_e and m_μ) is not featureless. It has structure:

- At the threshold q² = 4m_e², the function turns on (the electron pair-production threshold)
- Just above threshold, R_f rises steeply (the electron is barely relativistic)
- At q² ≫ m_e², R_f approaches its asymptotic logarithmic form (the electron is ultrarelativistic)
- The transition between these regimes happens at q² ~ (few × m_e)², a specific energy scale

This internal structure is the "shells" — specific scales within a domain where the accumulation pattern changes character. The shells are not random. They are determined by the geometry of the fermion's VP cloud and the energy variable.

For soliton boundaries: a galaxy (one domain in the cosmological line of sight) has internal structure. The galaxy's VP-analog would be the redshift accumulation pattern as light traverses from the galaxy's outer boundary through its interior to its inner boundary (or opposite side). The accumulation is not uniform — it has "shells":

- The galaxy's halo (low density, small correction per distance)
- The disk edge (transition to higher density, correction changes character)
- The disk midplane (highest density, maximum correction per distance)
- The bulge/core (different geometry, possibly toroidal circulation effects)
- The far side (mirror of the approach)

Each shell contributes its own rational correction factor determined by its geometry. The total galaxy-crossing correction is the product of all shell corrections. For a spherical galaxy: the shells are concentric spheres, each with R₂-based corrections. For a disk galaxy: the shells are nested tori and planes, with R₄ entering through the disk geometry.

The pattern of shells within a soliton is not random — it is determined by the soliton's mode structure (Chapter 6 of the super notebook). The mode structure produces specific density profiles, which produce specific correction patterns, which produce specific shell sequences. The "non-randomness" is the mode structure manifesting as ordered shells within each geometric stage.

---

### 3. THE COMPOUND DIFFICULTY

The full H₀ correction from here to the CMB crosses thousands of soliton boundaries. Each boundary defines a geometric stage with internal shells. Each shell has its own rational correction. The total is the product of all corrections across all shells across all stages.

This is the compound difficulty: even if each individual correction is a simple rational (1/3, 1/(12R₂), etc.), the PRODUCT of thousands of them is not a simple rational. It is a number that PSLQ cannot decompose because:

1. The individual corrections are from DIFFERENT geometric classes (sphere → R₂, torus → R₄, irregular → pure rational?)
2. The corrections MULTIPLY rather than add (the product of R₂-based and R₄-based corrections is neither R₂ nor R₄ alone)
3. The number of boundaries, their types, and their internal shell structures are SPECIFIC to a given line of sight — different directions see different sequences

This is exactly the composite soliton hierarchy problem from the Bessel zero notebook. The individual levels have fractions. The composite does not. Not because the fractions are wrong, but because the COMPOSITION (multiplication across thousands of rational corrections from different geometric classes) produces a transcendental.

But — and this is the crucial point — the RUNNING LAW at each stage is still rational. The per-stage correction is determined by the stage's geometry through exact rational formulas (R₂ for spheres, R₄ for tori, the Dynkin-index-like counting for the correction magnitude). The RULES are rational. The OUTCOME (the product) is transcendental. This is the PHYS-2 thesis: the transformation laws are integers, the values are not.

---

### 4. THE CURVE

The running of H₀ with distance is not a single function — it is a PIECEWISE function, changing character at each boundary. But if the boundaries are dense enough (many solitons along a line of sight), the piecewise function approximates a smooth curve. The VP running provides the template: between m_e and M_Z, the piecewise logarithmic function with threshold jumps approximates a smooth running α⁻¹(μ) curve.

The H₀ curve shape is determined by the DISTRIBUTION of soliton types along the line of sight. If the distribution is:

- **Homogeneous** (same mix of soliton types at all distances): H₀(d) = H₀(0) × r^N where r is the average per-transit correction and N ∝ d. This is the simple exponential model from the Hubble tension notebook.

- **Evolving** (different mix at different distances, because the universe evolved): H₀(d) has a distance-dependent per-transit correction r(d). Young universe (high redshift, CMB era) had different soliton distribution than now. The curve would have different slopes at different distance ranges.

- **Directional** (different soliton distribution in different directions, because of cosmic structure): H₀(θ, φ, d) depends on direction. Through voids: fewer boundaries, less correction, higher H₀. Through filaments: more boundaries, more correction, lower H₀. Through the galactic plane: disk geometry adds R₄ corrections not present in pole directions.

The observed Hubble tension (local H₀ ≈ 73, CMB H₀ ≈ 67.4) corresponds to the distance-averaged curve. The scatter in local measurements corresponds to the directional dependence. The curve's shape encodes the soliton distribution.

---

### 5. THE DATA WE HAVE

What measurements constrain the H₀ running curve? Collecting from known cosmological observations:

**H₀ measurements at different distances (the running curve data points):**

| Method | Effective distance | H₀ (km/s/Mpc) | Uncertainty | Boundary count (est.) |
|---|---|---|---|---|
| SH0ES (local SNe Ia) | ~10-40 Mpc | 73.0 | ±1.0 | ~10-50 |
| H0LiCOW (lensing) | ~100-1000 Mpc | 73.3 | ±1.8 | ~100-500 |
| TRGB (tip of red giant branch) | ~10-30 Mpc | 69.8 | ±1.7 | ~10-40 |
| DES + BAO | ~1000-3000 Mpc | 67.4 | ±1.2 | ~500-2000 |
| Planck CMB | ~14000 Mpc (last scattering) | 67.4 | ±0.5 | ~5000-50000 |

The trend: H₀ decreases monotonically with effective distance (boundary count). This is the Subgroup B signature — monotonic accumulation through discrete boundaries.

**CMB anomalies (directional dependence data):**

- Quadrupole-octupole alignment ("axis of evil"): the lowest CMB multipoles are aligned along a specific axis. In the soliton framework: this axis could be the direction through the local toroidal soliton (galactic disk plane), where the R₄ correction pattern is strongest.

- CMB cold spot: a ~5° region with anomalously low temperature in the southern sky. Could be a void (anti-boundary, r > 1?) along that line of sight, producing an excess correction.

- Hemispherical asymmetry: the CMB is slightly different in the north vs south ecliptic hemispheres. Could reflect the directional dependence of the soliton boundary distribution.

Each anomaly is a potential directional fingerprint of the soliton distribution. None has been analyzed in the soliton framework. All are established observations with no consensus explanation.

**Galaxy distribution data (the soliton census):**

- Galaxy surveys (SDSS, DES, DESI): provide 3D maps of galaxy positions and redshifts. Each galaxy is a soliton. The distribution of solitons along any line of sight is computable from these surveys.

- Void catalogs: identified voids in the galaxy distribution. Each void is an anti-boundary region.

- Filament maps: identified cosmic filaments. Each filament is a high-density boundary region.

The data to compute the per-direction soliton boundary count N(θ, φ, d) EXISTS in current galaxy surveys. The computation has not been done because nobody has framed it as a boundary-transit problem.

---

### 6. THE ALGORITHM

If the soliton framework is correct, the H₀ running curve is computable:

**Input:** Galaxy survey data (positions, morphologies, masses) along a specific line of sight.

**Step 1:** For each galaxy (soliton) along the line of sight, classify its geometry: spherical (elliptical galaxy → R₂ correction), toroidal (disk galaxy → R₄ correction), irregular (dwarf irregular → pure rational correction?).

**Step 2:** For each galaxy, compute the per-transit correction r_i from its geometry, mass, and the angle of transit (through the disk plane vs through the halo for a disk galaxy).

**Step 3:** The cumulative correction at distance d is: H₀(d) = H₀(local) × Π_i r_i, where the product is over all galaxies with distance < d along that line of sight.

**Step 4:** Compare the predicted H₀(d) curve to the measured data points from different distance indicators.

The critical unknown: the per-transit correction formula r(geometry, mass, angle). This is the "A₁ of the H₀ transformation law" from the PHYS-9 report — the fundamental quantity that the entire framework needs. If the correction is R₂-based for spherical boundaries: r = 1 − ε × R₂ × (M/M_ref) for some small ε and reference mass M_ref. If R₄-based for toroidal: r = 1 − ε × R₄ × (M/M_ref) × f(angle). The functional form is constrained by the geometry but the magnitude ε is unknown.

**The calibration:** Use the SH0ES local measurement (H₀ ≈ 73, through ~10-50 boundaries) and the Planck CMB measurement (H₀ ≈ 67.4, through ~thousands of boundaries) as the two endpoints. Fit ε from the ratio: (73/67.4)^(1/N_effective) = r_average. For N_effective ~ 100: r ≈ 0.9992. For N_effective ~ 1000: r ≈ 0.99992. The per-transit correction is tiny — sub-part-per-thousand — which is why the effect only appears cumulatively over cosmological distances.

---

### 7. THE PREDICTION STRUCTURE

If the algorithm works, it makes several testable predictions:

**P1.** H₀ measured through known voids should be HIGHER than H₀ measured through known filaments at the same distance. Voids have fewer boundaries (fewer corrections). Filaments have more boundaries (more corrections). The difference should be quantitative: ΔH₀/H₀ ≈ (N_filament − N_void) × (1 − r).

**P2.** H₀ measured along the galactic plane should differ from H₀ measured toward the galactic poles. The galactic disk adds a toroidal correction (R₄-based) to all lines of sight through the plane, absent for pole lines of sight. The magnitude is one boundary's correction (the Milky Way itself), so the effect is of order (1 − r) ~ 10⁻⁴ — possibly detectable with next-generation measurements.

**P3.** The H₀ running curve should flatten at large distances (high N), because the per-transit correction is multiplicative and the product converges. At N → ∞, H₀(∞) = H₀(local) × r^∞ → 0 (if r < 1) or H₀(local) × finite limit (if r approaches 1 for distant, evolved solitons). The CMB value 67.4 may already be near the asymptote.

**P4.** Gravitational wave standard sirens (from LIGO/Virgo/KAGRA) provide H₀ measurements independent of the electromagnetic distance ladder. If the soliton correction affects electromagnetic propagation but not gravitational wave propagation (because gravitational waves couple to geometry, not to the soliton boundary's electromagnetic structure), gravitational wave H₀ should match the LOCAL electromagnetic H₀ regardless of distance. This would be a kill test: if GW H₀ also shows the running curve, the correction affects spacetime itself (not just EM propagation).

**P5.** The "shells" within a single galaxy crossing should produce frequency-dependent corrections if the correction has a spectral component (wavelength-dependent interaction with the soliton boundary). This would manifest as a distance-dependent spectral distortion — different from standard dust reddening in its functional form (the soliton correction would be geometric, the dust correction is exponential in column density). Current spectral data from SNe Ia might already constrain this.

---

### 8. LEMU ASSESSMENT

**L (Logic):** The framework follows from established premises: couplings run between thresholds (PHYS-5/9), boundaries modify the running rules (PHYS-14 domain map), each boundary type has specific geometry (soliton taxonomy), the correction pattern depends on the geometry (R₂ for spheres, R₄ for tori). Logic passes as an extension of established principles.

**E (Empirical):** The H₀ tension is observed. The monotonic trend with distance is observed (approximately). The CMB anomalies are observed. Galaxy survey data exists. But: no computation of the per-direction boundary count has been done. No fit of the per-transit correction has been attempted. The curve has not been compared to data. Empirical status: consistent with observations but not yet tested.

**M (Math):** Not computed. The per-transit correction formula r(geometry, mass, angle) is unknown. The boundary census N(θ, φ, d) has not been extracted from galaxy surveys. The curve fit has not been performed. Math gate: OPEN. This is the critical barrier. Everything else is framework — the math is where the framework becomes a testable prediction.

**U (Utility):** Extremely high IF the math passes. It would: unify the Hubble tension with the remainder framework, connect cosmological observations to particle physics infrastructure (same R₂/R₄ framework), explain the CMB anomalies as directional boundary effects, predict H₀ for any line of sight from galaxy survey data, and provide a testable alternative to dark energy modifications. If the math fails (the curve doesn't fit, the per-transit correction is unphysical, the directional predictions are wrong): the framework is falsified for cosmological applications while remaining valid for its particle physics domains.

---

### 9. THE CONNECTION TO THE CONVENTION DISCREPANCY

At first glance, the Hubble tension notebook has nothing to do with the normalization question about VL beta shifts. But there is a structural parallel:

The VL beta shift question: is the per-multiplet correction to the beta function 2× or 4× the scalar base value? The answer depends on convention (real vs complex scalar). The physical test (gap ratio) selects the correct convention.

The H₀ per-transit question: what is the per-boundary correction to H₀? The answer depends on the boundary geometry (sphere vs torus, R₂ vs R₄). The physical test (H₀ running curve) selects the correct correction formula.

In both cases: the RULE is rational (beta coefficient from Dynkin indices, per-transit correction from geometry). The CONVENTION determines which rational applies. The PHYSICAL TEST selects between conventions.

The lesson from the VL convention resolution: the convention comment was wrong, the values were right, and the physical test (gap ratio 38/27 close to measured) confirmed the values. For the H₀ curve: we don't yet know the values, and we don't yet have the physical test (the curve fit). But the STRUCTURE is the same: rational rules, convention-dependent application, physical test as arbiter.

---

**End of notebook. Status: active conceptual framework. Math gate OPEN — the per-transit correction formula is the critical unknown. Data exists but has not been processed in this framework. Predictions P1-P5 are testable with current or near-future data. Updated: Session 4, April 2 2026.**
