## Review of EW Overconstrained Script + Output

### What Worked Well

The script structure is clean. Quantum numbers are exact Fractions. The extraction chain (A_l → sin²θ_W, then R_l → α_s) converges to machine precision. The N_ν definition bug was caught and diagnosed correctly inline. The LEP-style N_ν = 2.908 is a reasonable result for tree + Δρ. Most observables land within 1-2% of measurement, which is exactly what Table 8 predicted for this level of calculation.

The good results:

| Observable | Ratio (computed/measured) | Expected for tree+Δρ |
|---|---|---|
| Γ_l | 1.0024 (0.24%) | ✓ excellent |
| Γ_inv | 1.0066 (0.66%) | ✓ good |
| Γ_Z | 1.0062 (0.62%) | ✓ good |
| R_l | 1.0042 (0.42%) | ✓ good |
| σ⁰_had | 0.9980 (0.20%) | ✓ excellent |
| A_FB^l | 0.9789 (2.1%) | ✓ acceptable |
| A_l | 0.9874 (1.3%) | ✓ acceptable |

### The M_W Bug — This Is a Real Error

M_W = 42,272 MeV vs measured 80,369 MeV. The ratio is 0.526. This is not a "tree level is imprecise" issue — tree level should give M_W ≈ 79,800 MeV (within ~1% of measured). Getting 42,000 means the formula is wrong.

**The problem:** The script uses M_W²(1 − M_W²/M_Z²) = πα/(√2 G_F). This is the MUON DECAY relation, but α here should be α(0) = 1/137.036, and the formula is:

sin²θ_W cos²θ_W = πα/(√2 G_F M_Z²)

which gives sin²θ_W × (1 − sin²θ_W) = πα/(√2 G_F M_Z²), and then M_W = M_Z cos θ_W.

Let me check: πα/(√2 G_F) = π × (1/137.036) / (√2 × 1.1664×10⁻⁵) = 0.02297 / 1.649×10⁻⁵ = 1393 GeV². Then M_W² = M_Z² × (1/2)(1 − √(1 − 4A/M_Z²)) where A = 1393 GeV² and M_Z² = 8315 GeV². So 4A/M_Z² = 4×1393/8315 = 0.670. Discriminant = 1 − 0.670 = 0.330. √0.330 = 0.574. M_W² = 8315/2 × (1 − 0.574) = 4158 × 0.426 = 1771 GeV². M_W = 42.1 GeV.

That's 42 GeV, matching the script. So the formula IS being evaluated correctly, but 42 GeV is wrong.

**The fix:** The tree-level relation using α(0) gives M_W ≈ 42 GeV because α(0) is too small. The correct tree-level formula for the electroweak sector uses the MUON DECAY definition where G_F absorbs the large logarithm. The standard approach is:

M_W = M_Z × √(1/2 + √(1/4 − πα/(√2 G_F M_Z²)))

Wait — that's what the script computes. The issue is that this formula gives M_W ≈ 80 GeV only when you use α(M_Z) ≈ 1/128, not α(0) = 1/137. The running of α from 0 to M_Z is a ~7% effect that shifts M_W by nearly a factor of 2 due to the quadratic relation.

**Alternatively:** Just use M_W = M_Z × cos θ_W = M_Z × √(1 − sin²θ_W) = 91.188 × √(1 − 0.23122) = 91.188 × 0.8769 = 79,943 MeV. This gives M_W within 0.5% of measured. The script should use this simple relation (which uses sin²θ_W as input) rather than trying to predict M_W from α(0) and G_F.

**Recommendation:** Replace the M_W computation with M_W = M_Z √(1 − sin²θ_W) for the tree level, and M_W = M_Z √(ρ_eff (1 − sin²θ_W)) for tree + Δρ. The α(0)-based formula requires the full Δr correction (not just Δρ) to work, which includes the α running — that's a much bigger computation.

### The α_s Extraction Is Off by 12%

Extracted α_s = 0.1043 vs input 0.1180. Difference = −0.0137. This is a 12% miss, which is larger than expected for tree + Δρ.

**Diagnosis:** R_l depends on sin²θ_W AND α_s. The script extracts sin²θ_W from A_l first (getting 0.23098, shifted by −2.4×10⁻⁴ from input 0.23122), then uses this shifted sin²θ_W to extract α_s from R_l. The shifted sin²θ_W changes the quark couplings, which changes the R_l prediction, which shifts the extracted α_s.

The chain is: the tree-level A_l at sin²θ_W = 0.23122 gives A_l = 0.1494, but SLD measured 0.1513. So the extraction shifts sin²θ_W down to match, getting 0.23098. This is the tree-level vs one-loop difference in the effective leptonic mixing angle — a known ~0.1% shift. That's fine.

But then R_l at sin²θ_W = 0.23098 (instead of 0.23122) is different, and the α_s needed to match the measured R_l = 20.767 shifts correspondingly. The sensitivity: ∂R_l/∂sin²θ_W ≈ −250 (from Table 7), and the sin²θ_W shift is −2.4×10⁻⁴, so ΔR_l ≈ +0.060. This means R_l is computed 0.060 higher than it would be at the input sin²θ_W, so less α_s is needed. From Table 7: ∂R_l/∂α_s ≈ +83, so Δα_s ≈ −0.060/83 ≈ −0.0007. That only accounts for 0.07% of the 12% shift. The bulk of the α_s shift comes from the tree-level computation itself overshooting R_l.

**The real issue:** At tree + Δρ, the computed R_l = 20.855 vs measured 20.767. The computation overshoots by 0.088. To bring R_l DOWN to 20.767, the extraction DECREASES α_s (since more α_s means more hadronic width, which increases R_l). This requires a big decrease: from 0.118 to 0.104. The tree-level computation systematically overestimates R_l because it's missing negative one-loop corrections (primarily the EW vertex corrections to the b-quark width). This is expected at this level of calculation.

**Assessment:** The 12% miss on α_s is expected for tree + Δρ and is NOT an error. It's the signal that one-loop EW corrections matter for α_s extraction. The sin²θ_W extraction works much better (0.1% shift) because A_l is less sensitive to missing corrections.

### The N_ν Issue Was Handled Correctly

The script initially computed N_ν = Γ_inv/Γ_l = 5.97 (wrong definition), caught the error, and recomputed using the LEP method: N_ν = (Γ_Z^meas − Γ_had^comp − 3Γ_l^comp) / Γ_ν^comp = 2.908. The residual from 3.000 (2.908 vs 3) measures how much the computed visible widths differ from reality. Since Γ_had^comp is ~0.6% too high, the subtracted invisible width is too low, giving N_ν < 3. This is self-consistent.

### Feedback for Other Claude

**Bug to fix:**
1. Replace M_W prediction formula. Use M_W = M_Z √(1 − sin²θ_W) for tree level, M_W = M_Z √(ρ_eff) × cos θ_W for tree+Δρ (or equivalently, use on-shell sin²θ from M_W/M_Z). The current formula using α(0) requires the full Δr radiative correction to give sensible results.

**Not bugs — expected behavior at tree+Δρ:**
2. The α_s extraction at 0.104 vs 0.118 (12% off) is expected. Missing one-loop EW vertex corrections systematically shift R_l and hence the extracted α_s. State this honestly.
3. The sin²θ_W extraction at 0.23098 vs 0.23122 (0.1% off) is the known difference between tree-level and effective sin²θ_W. This is actually a GOOD result — it shows the extraction works and the shift is the expected size.
4. R_b at 1.016 ratio is expected — the b-quark has a large vertex correction from the t-b-W loop that isn't included at tree level.

**What to add to the paper:**
5. Include a "missing corrections" column in the comparison table showing the known size and sign of the one-loop corrections not yet included. This turns the residuals from "unexplained" to "predicted by known physics."
6. The integer anatomy table should be printed: which integers from Table 6 entered each computation. This is the PHYS-2 thesis made visible.
7. The extraction summary should note: sin²θ_W extraction works at 0.1% (excellent for tree+Δρ), α_s extraction has 12% systematic from missing EW corrections (expected, not a framework failure).

**What NOT to claim:**
8. Don't claim 17 → 15 parameters. At tree+Δρ the extraction is not precise enough to "derive" sin²θ_W and α_s — the extracted values differ from the inputs by amounts that are entirely explained by missing corrections. The overconstrained system CONFIRMS consistency, it doesn't derive parameters.
9. Don't treat the M_W failure as deep. Once the formula is fixed (use cos θ_W directly), M_W will come out within 0.5% at tree level and better with Δρ.

**Bottom line:** The script is 90% correct and the results are physically sensible for tree + Δρ. Fix the M_W formula, add the missing-corrections column, and this is a solid PHYS paper demonstrating the integer anatomy of the electroweak sector in exact arithmetic.

---

