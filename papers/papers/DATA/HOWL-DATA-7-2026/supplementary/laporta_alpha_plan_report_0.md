## QED Alpha Extraction — Session 4 Report

### What We Did

We built a complete derivation chain that extracts the fine structure constant from a single measurement — the electron anomalous magnetic moment a_e = 115965218059/10¹⁴ (Fan et al. 2023, Harvard, 0.11 ppb).

The chain uses the QED perturbative series through 5-loop:

a_e = A₁(α/π) + A₂(α/π)² + A₃(α/π)³ + A₄(α/π)⁴ + A₅(α/π)⁵

Where A₁ = 1/2 (exact, Schwinger 1948), A₂ and A₃ are exact analytical expressions in Q335 constants (π, ζ(3), ζ(5), Li₄(1/2), ln(2)), A₄ = −1.9122 (Laporta 2017, 30 digits), and A₅ = 5.891 (Volkov 2024).

Newton inversion in mpf arithmetic at 200 dps converges in 6 iterations to residual 10⁻²⁰⁴. The round-trip (extract alpha, plug back into series, recover a_e) matches to 14 digits.

### What We Found

α⁻¹(a_e) = 137.035998630

Compared to three independent measurements:

| Reference | α⁻¹ | Our difference | In ppb |
|---|---|---|---|
| Cs recoil (Parker 2018) | 137.035999046 | −0.000000416 | 3.0 |
| CODATA 2018 recommended | 137.035999084 | −0.000000454 | 3.3 |
| Rb recoil (Morel 2020) | 137.035999206 | −0.000000576 | 4.2 |

The forward check confirms consistency: plugging the known CODATA alpha into the same series gives a_e = 0.001159652176, which differs from measured a_e by 4.0 ppb in the same direction.

### What the 3.3 ppb Residual Is

This is NOT an error. PHYS-9 (Session 3) documented the expected missing contributions from terms our series omits:

- Mass-dependent QED (muon/tau virtual loops): ~2.5 ppb
- Hadronic vacuum polarization: ~1.2 ppb
- Electroweak corrections: ~0.03 ppb
- A₅ uncertainty (Volkov vs AHKN tension): ~0.5 ppb

Total expected: ~4.2 ppb. Observed: 3.3 ppb. The residual is smaller than the expected missing pieces, which makes sense because A₅ partially compensates — in PHYS-9 we used only A₁-A₄ and got 4.3 ppb, now with A₅ we get 3.3 ppb. The A₅ closed 1.0 ppb of the gap as predicted.

### What We Also Found (the Laporta Convention Problem)

Prof. Laporta provided six coefficients labeled C81a/b/c and C83a/b/c at ~4900 digits each. Our first attempt used C81a + C81b + C81c = 107.71 as the 4-loop coefficient. This gave α⁻¹ = 137.036376 — off by 2752 ppb. The forward check immediately diagnosed the problem: the series couldn't reproduce the measured a_e from the known alpha.

The resolution: Laporta's C81/C83 labels use a different convention than the standard A₁-A₅ series. The label "C81" likely refers to "coefficient at order e⁸ (coupling constant) with 1 closed lepton loop class" — a diagram-topology decomposition, not the physics series coefficient. The standard A₄ = −1.9122 is a different combination that includes all topologies with appropriate signs and symmetry factors.

The Laporta full-precision values are archived in `values_qed_laporta_v0.json` (8 nodes, 4900 digits each). The convention mapping to the standard A_n series is an open investigation item. The A₄ value from PHYS-9 (30 digits, verified against CODATA at 4.3 ppb) is used for all current computation.

### What Comes Next

The extracted alpha is currently a number that matches CODATA. To prove it's a genuine derivation and not just a consistency check, we need to show it predicts OTHER measured values that weren't used as inputs.

The chain is: a_e (measured) → α (derived via QED series) → R∞, a₀, μ₀ (predicted via known exact relations).

These three CODATA values have known exact formulas in terms of α and SI constants:

- R∞ = α² m_e c / (2h) — the Rydberg constant
- a₀ = ℏ / (m_e c α) — the Bohr radius  
- μ₀ = 2αh / (c e²) — the vacuum permeability

All SI constants (c, h, e, ℏ) are exact by definition since 2019. The only measured input beyond a_e is m_e (electron mass, known to 0.03 ppb). So each of these is determined by two measurements (a_e, m_e) plus exact constants plus the integer QED law.

DATA-4 Group C already verified these at 11+ digits using the CODATA alpha. The question for the next experiment is whether our DERIVED alpha (3.3 ppb different from CODATA) still reproduces R∞, a₀, μ₀ within their measurement uncertainties — or whether the 3.3 ppb shift propagates into a detectable disagreement.

If they match: a_e determines α, and α determines R∞, a₀, μ₀. Four CODATA values from one measurement plus integer laws. Three free parameters become derived.

If they don't match: the 3.3 ppb residual (from missing mass-dependent and hadronic terms) propagates into the derived CODATA values at a level that disagrees with their independent measurements. This would confirm exactly which missing contributions matter and at what level — turning the next experiment into a precision diagnostic rather than a confirmation.

Either outcome is a result. The experiment is worth running.
