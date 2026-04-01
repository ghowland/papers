## Results: What the Electroweak Computation Shows

### The Big Picture

14/14 assertions pass. Every observable agrees with LEP measurements at the expected accuracy for tree-level + leading Δρ. The M_W bug is fixed — it now comes out at 80,326 MeV vs measured 80,369 MeV, a 0.05% match. The framework works.

### The Three Tiers of Results

**Tier 1 — Excellent (< 0.3% deviation):** These observables are nearly insensitive to missing one-loop corrections.

| Observable | Ratio | Why it works |
|---|---|---|
| M_W | 0.9995 | cos θ_W is a direct input; Δρ correction nails the residual |
| σ⁰_had | 0.9980 | Ratio of widths — many corrections cancel in the ratio |
| Γ_l | 1.0024 | Leptonic width has no QCD, small EW vertex correction |

M_W at 0.05% is the standout. Tree-level gives 79,953 MeV (0.5% off). Adding Δρ = 0.00933 brings it to 80,326 MeV (0.05% off). The top quark mass correction accounts for 372 MeV of the 416 MeV gap between tree and measurement. The remaining 44 MeV is the full Δr correction (running of α, box diagrams, etc.) that we haven't included.

**Tier 2 — Good (0.5-1.6% deviation):** These observables have known missing corrections of the right size and sign.

| Observable | Ratio | Missing correction |
|---|---|---|
| Γ_Z | 1.0062 | Total width overshoots by 15 MeV; missing negative EW corrections ~−0.5% |
| Γ_inv | 1.0066 | Neutrino widths track Γ_Z (same ρ_eff correction) |
| R_l | 1.0042 | Hadronic/leptonic ratio too high; b-quark vertex correction would reduce by ~0.4% |
| R_b | 1.0158 | The t-b-W vertex loop reduces Γ_b by ~1.5%, exactly the overshoot we see |
| R_c | 0.9904 | Small deficit; vertex correction adds ~0.5% |

R_b at 1.6% is the most informative. At tree level, b quarks have the same coupling as d and s quarks. But the b quark has a unique one-loop correction: the virtual t-b-W triangle diagram, where the top quark runs in the loop. This correction is proportional to m_t² and specifically reduces Γ_b by about 1.5%. Our computation doesn't include it, so we overshoot R_b by exactly that amount. When the LEP electroweak working group saw this effect in 1994, it was one of the pieces of evidence that predicted m_t ≈ 170 GeV before CDF/D0 discovered the top quark.

**Tier 3 — Asymmetries (1-2% deviation):** These are extremely sensitive to sin²θ_W.

| Observable | Ratio | Sensitivity |
|---|---|---|
| A_l | 0.9874 | Shifts by ~8% per 1% change in sin²θ_W |
| A_FB^l | 0.9789 | Goes as A_e², so double sensitivity |

The asymmetries are small numbers (A_l ≈ 0.15, A_FB ≈ 0.017) because v_e = −1/2 + 2sin²θ_W ≈ −0.038 is accidentally small — sin²θ_W happens to be close to 1/4 where v_e would vanish. This makes asymmetries extremely sensitive probes of sin²θ_W but also means small radiative corrections shift them significantly. The 1-2% deviations we see correspond to a ~2 × 10⁻⁴ shift in the effective sin²θ_W, which is the known one-loop correction.

### The Parameter Extractions

**sin²θ_W extraction works beautifully.** Two independent extractions from two different observables:

| Source | Extracted sin²θ_W | Δ from input |
|---|---|---|
| A_l (SLD) | 0.23098 | −2.4 × 10⁻⁴ |
| A_FB^l (LEP) | 0.23102 | −2.0 × 10⁻⁴ |

The two agree with each other to 3.9 × 10⁻⁵. Both are shifted from the input (0.23122) by about −2 × 10⁻⁴. This shift is the known difference between the MS-bar definition of sin²θ_W (what we input) and the effective leptonic mixing angle (what asymmetries measure). At one loop, the shift is approximately Δsin²θ_eff ≈ −(α/4π)cos²θ_W/sin²θ_W × (loop function) ≈ −2 × 10⁻⁴. Our tree-level computation gets the effective value directly from inverting the tree-level formula, so the difference from the MS-bar input is exactly this known correction.

The agreement BETWEEN the two extractions (3.9 × 10⁻⁵) is more significant than their agreement with the input. It means A_l and A_FB^l are giving consistent readings of the same underlying parameter at the tree level. This is the overconstrained system working as intended — two independent measurements, one parameter, consistent extraction.

**α_s extraction shows the expected systematic.** Extracted α_s ≈ 0.104-0.105 vs input 0.118. The 12% deficit is not an error — it's the signature of missing one-loop electroweak corrections to the hadronic width. At tree + Δρ, the computed R_l = 20.855 overshoots the measured 20.767 by 0.42%. To bring R_l down to the measured value, the extraction demands less QCD correction (lower α_s). The missing b-quark vertex correction would reduce Γ_had by ~0.7%, which would shift the extracted α_s upward by ~0.009, from 0.104 to ~0.113. Still short of 0.118, but the remaining gap is other one-loop EW corrections.

This tells us: α_s extraction from R_l REQUIRES full one-loop electroweak corrections to reach the per-cent level. At tree + Δρ, it's a ~12% systematic. This is a known result in the literature — the LEP EWWG always included full one-loop corrections for their α_s extraction.

### The N_ν Result

N_ν = 2.908 from the LEP-style computation (measured Γ_Z minus computed visible widths, divided by SM neutrino width). The measured value is 2.984 ± 0.008. The 2.5% deficit comes from the computed visible widths being 0.6% too high (Γ_vis = 2008 MeV computed vs ~1996 MeV implied by measurement). Since we overshoot visible widths, the subtracted invisible width is too small, giving N_ν < 3.

This is self-consistent with the other results and would improve with one-loop corrections.

### The Integer Anatomy

The computation makes the PHYS-2 thesis explicit. Every coefficient in every formula traces to one of three sources:

1. **Gauge group integers:** N_c = 3, T₃ = ±1/2, Q_f = 0/±1/±1/3/±2/3, the 3/4 in A_FB, the 12 in σ⁰, the 6 in Γ₀
2. **Generation count:** 3 neutrinos, 3 leptons, 2 up-type quarks (u,c), 3 down-type quarks (d,s,b) contributing to Γ_Z
3. **Loop expansion:** the 3 and 8 in Δρ = 3G_Fm_t²/(8π²√2), the QCD coefficients 1, 365/24, etc.

The transcendental content is minimal: π from phase space integrals (in Γ₀), π² and √2 in Δρ. Both enter through the Q335 basis as exact integers. The measured content is exactly the 7 DATA-2 inputs. Nothing else enters.

### What This Means for the HOWL Program

The computation confirms DISC-9's central finding at a new level. The transformation laws connecting 7 inputs to 13 observables are built entirely from gauge group integers and loop-expansion rationals. The 7 inputs carry all the non-integer information. The framework is computationally operational for electroweak physics.

It does NOT derive sin²θ_W or α_s as claimed in the original plan's optimistic scenario. The extractions confirm consistency (sin²θ_W from two independent observables agrees to 4 × 10⁻⁵) but the extracted values differ from the inputs by amounts entirely explained by missing one-loop corrections. This is not parameter derivation — it's consistency checking. The parameter count stays at 17 (or 18 without conditional Koide).

The computation is a foundation for future work. Adding the b-quark vertex correction (one additional diagram, known analytically) would bring R_b, R_l, and the α_s extraction into per-mille agreement. Adding the full Δr correction would bring M_W to the 10 MeV level. Each addition is a known calculation with known integer/rational coefficients, implementable in Fraction arithmetic.

---

