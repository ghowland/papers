## Supporting Appendix Tables for PHYS-31

---

### TABLE 31.1: THE POOL COMPARISON — BETA vs RANDOM

| Property | Beta pool | Random pool (typical) |
|---|---|---|
| Size | 15 | 15 |
| Range | [1, 41] | [1, 50] (conservative) |
| Source | Beta function coefficients | Uniform random sample |
| Selection | Determined by physics | No selection |
| Score (hits out of 8) | 6 | 6.2 (mean) |
| Percentile | 81st (from bottom) | 50th (by definition) |
| σ deviation | −0.24 | 0 |

The beta pool is indistinguishable from a random pool. Its score of 6 is slightly below the random mean. No statistical test can distinguish it from chance.

---

### TABLE 31.2: THE FORMULA TEMPLATE — WHAT WAS TESTED

| Formula type | Expression | Count per pool | Example |
|---|---|---|---|
| Ratio × π^b | (p/q) × π^b, p≠q | 15×14×5 = 1,050 | (22/13) × π |
| Single × π^b | p × π^b | 15×5 = 75 | 7 × π⁻¹ |
| Ratio × π^b × α | (p/q) × π^b × α | 1,050 | (38/3) × π² × α |
| Single × π^b × α | p × π^b × α | 75 | 13 × π × α |
| **Total** | | **~2,250** | |

Five π powers: π⁻² ≈ 0.101, π⁻¹ ≈ 0.318, π⁰ = 1, π¹ ≈ 3.142, π² ≈ 9.870.
The α multiplier: α = 1/137.036 ≈ 0.00730.
Value range covered: ~0.001 to ~2,000 (six orders of magnitude).

---

### TABLE 31.3: THE EXPECTED HIT RATE — BACK OF ENVELOPE

| Target | Value | Tolerance | Band width | Candidates in band (est.) | P(hit) |
|---|---|---|---|---|---|
| DM/baryon | 5.320 | 0.5% | 0.053 | ~3 | ~95% |
| Ω_b × 100 | 4.93 | 1.0% | 0.099 | ~5 | ~99% |
| Ω_DM × 100 | 26.4 | 1.0% | 0.528 | ~8 | ~99% |
| H₀ ratio | 0.9189 | 1.0% | 0.018 | ~3 | ~95% |
| sin²θ_W | 0.23122 | 0.5% | 0.0023 | ~1 | ~60% |
| n_s | 0.965 | 0.5% | 0.010 | ~2 | ~85% |
| log₁₀(Λ) | −121.54 | 0.3% | 0.729 | ~1 | ~50% |
| α_s | 0.1180 | 1.0% | 0.0024 | ~2 | ~85% |
| **Expected total** | | | | | **~6.7 hits** |

The observed random mean of 6.2 is consistent with this estimate. The two hardest targets (sin²θ_W at 0.5% tolerance and log₁₀(Λ) at 0.3%) are the two that the beta pool also misses (n_s and log₁₀(Λ)).

---

### TABLE 31.4: THE P-VALUE CONVERGENCE

| Trials completed | Pools ≥ 6 hits | p-value (running) | Converged? |
|---|---|---|---|
| 1,000 | ~808 | ~0.808 | Within 2% of final |
| 2,000 | 1,611 | 0.806 | Yes |
| 4,000 | 3,230 | 0.808 | Yes |
| 6,000 | 4,882 | 0.814 | Yes |
| 8,000 | 6,498 | 0.812 | Yes |
| 10,000 | 8,128 | **0.813** | **Final** |

The p-value stabilized by 2,000 trials. The remaining 8,000 trials confirmed the estimate to ±0.5%. A run of 10,000 is well beyond the convergence threshold.

---

### TABLE 31.5: THE SCORE DISTRIBUTION — DETAILED

| Score | Count | Fraction | Cumulative ≥ score | Cumulative % |
|---|---|---|---|---|
| 3 | 22 | 0.22% | 10,000 | 100.0% |
| 4 | 275 | 2.75% | 9,978 | 99.8% |
| 5 | 1,575 | 15.75% | 9,703 | 97.0% |
| **6** | **3,987** | **39.87%** | **8,128** | **81.3%** |
| 7 | 4,141 | 41.41% | 4,141 | 41.4% |
| 8 | 0 | 0.00% | 0 | 0.0% |

No pool hit all 8 targets. The two hardest targets (n_s at 0.5% and log₁₀(Λ) at 0.3%) are responsible: they are missed by most pools including the beta pool. The modal score is 7 — the most common outcome for random pools is to hit 7 of 8 targets.

---

### TABLE 31.6: WHAT MAKES EACH TARGET EASY OR HARD

| Target | Value | Tolerance | Easy or hard? | Why |
|---|---|---|---|---|
| DM/baryon | 5.320 | 0.5% | Easy | Near π (3.14) and 2π (6.28), many ratios × π land nearby |
| Ω_b × 100 | 4.93 | 1.0% | Easy | Near π (3.14) to 2π (6.28) range, wide tolerance |
| Ω_DM × 100 | 26.4 | 1.0% | Easy | Many p × π or (p/q) × π² formulas in this range |
| H₀ ratio | 0.9189 | 1.0% | Easy | Near 1, many ratios near unity, wide tolerance |
| sin²θ_W | 0.23122 | 0.5% | Medium | Small value, tight tolerance, but many ratios in [0.2, 0.3] |
| n_s | 0.965 | 0.5% | Hard | Very close to 1, tight tolerance, need ratio near 0.965/π^b |
| log₁₀(Λ) | −121.54 | 0.3% | Hard | Negative, large magnitude, tightest tolerance, products needed |
| α_s | 0.1180 | 1.0% | Medium | Small value but wide tolerance compensates |

The two misses for the beta pool (n_s and log₁₀(Λ)) are the two hardest targets. This is not a property of the beta integers — most random pools also miss these two.

---

### TABLE 31.7: THE BETA POOL HITS — QUALITY COMPARISON TO RANDOM

| Target | Beta miss (%) | Random mean miss (%) | Beta rank among random | Beta special? |
|---|---|---|---|---|
| DM/baryon | 0.065 | ~0.15 (est.) | Top 20% | Slightly good |
| Ω_b × 100 | 0.097 | ~0.3 (est.) | Top 10% | Good |
| Ω_DM × 100 | 0.834 | ~0.4 (est.) | Bottom 50% | Poor |
| H₀ ratio | 0.721 | ~0.4 (est.) | Bottom 50% | Poor |
| sin²θ_W | 0.195 | ~0.2 (est.) | Average | Typical |
| α_s | 0.091 | ~0.3 (est.) | Top 20% | Good |

The beta pool has some excellent individual hits (DM/baryon at 0.065%, α_s at 0.091%) but also some poor ones (Ω_DM at 0.83%, H₀ ratio at 0.72%). Averaged across all targets, the quality is unremarkable. The overall hit COUNT (6) is below the random mean (6.2).

---

### TABLE 31.8: THE TWO TYPES OF sin²θ_W EVIDENCE

| Property | Track A (running) | Track B (formula) |
|---|---|---|
| Formula | RGE solution from M_GUT to M_Z | 3/13 = 0.2308 |
| Method | Solve differential equation | Integer ratio match |
| Inputs | α_EM, α_s, CD betas | Beta integers 3 and 13 |
| Result | sin²θ_W = 0.22845 (1-loop) | sin²θ_W ≈ 0.2308 |
| Miss | 1.20% | 0.20% |
| Testable by Monte Carlo? | No (unique prediction) | **Yes (this paper)** |
| Survived p = 0.81? | **Yes (not tested)** | **No (parked)** |
| Physical mechanism | Coupling running | None identified |
| Free parameters | 0 (M_GUT from crossing) | 0 (direct ratio) |
| Statistical significance | Unique prediction, not a scan | p = 0.81 (not significant) |

The Track A sin²θ_W prediction and the Track B 3/13 formula happen to predict similar values (0.228 vs 0.231), but they are fundamentally different types of evidence. Track A survives the statistical test because it was never vulnerable to it.

---

### TABLE 31.9: THE THREE SIGNIFICANCE THRESHOLDS

| Threshold | p-value | Meaning | Track B status | Observed? |
|---|---|---|---|---|
| High confidence | p < 0.01 | Top 1% — beta integers are special | PROMOTED | No (p = 0.81) |
| Marginal | 0.01 ≤ p < 0.05 | Top 5% — proceed with caution | ACTIVE | No |
| Not significant | p ≥ 0.05 | Random integers equally good | PARKED | **Yes** |

The gate was set BEFORE the test (PHYS-25 paper program). The threshold p < 0.05 is the standard statistical significance criterion. The result p = 0.81 is not a borderline case — it is decisively above the threshold.

---

### TABLE 31.10: THE LESSON — DYNAMICS vs NUMEROLOGY

| Feature | Dynamics (Track A) | Numerology (Track B) |
|---|---|---|
| What is tested | Does the RGE predict α_s correctly? | Do beta integers match cosmological values? |
| Search space | 1 prediction per observable | ~2,250 formulas per pool |
| False positive risk | Low (unique prediction) | High (combinatorial explosion) |
| Control test | Compare prediction to measurement | Monte Carlo with random pools |
| Result for CD | α_s within 1σ (0.33% miss) | 6/8 hits, p = 0.81 (not significant) |
| Status | **Validated** | **Parked** |
| Why different | One theory → one number | Many formulas → many numbers |

The fundamental distinction: Track A makes one prediction per observable with zero free parameters. Track B scans thousands of formulas and selects the best match. The look-elsewhere effect kills Track B.

---

### TABLE 31.11: THE FORMULA SPACE STRUCTURE

| π power | Value | Ratio range covered | Example targets in range |
|---|---|---|---|
| π⁻² | 0.101 | Ratios × 0.101 → [0.002, 4.1] | α_s (0.118), sin²θ_W (0.231) |
| π⁻¹ | 0.318 | Ratios × 0.318 → [0.008, 13.0] | DM/baryon (5.32), Ω_b (4.93) |
| π⁰ | 1.000 | Ratios × 1 → [0.024, 41] | Ω_DM (26.4), n_s (0.965) |
| π¹ | 3.142 | Ratios × 3.142 → [0.076, 129] | log₁₀Λ (121.54) |
| π² | 9.870 | Ratios × 9.870 → [0.24, 405] | — |
| + α multiplier | ×0.00730 | All of above shifted down ×137 | H₀ ratio (0.919) via large × α |

Every target falls within the coverage of at least two π-power tiers. The α multiplier extends coverage to values that would otherwise require tiny ratios. The formula space blankets the target range.

---

### TABLE 31.12: TRACK B PAPERS — NOW PARKED

| Paper | Title | Was gated by | Status |
|---|---|---|---|
| PHYS-32 | Set B Omegas | PHYS-31 (p < 0.05) | **PARKED** |
| PHYS-33 | Λ Interpolation | PHYS-31 (p < 0.05) | **PARKED** |
| PHYS-34 | Per-Transit Mechanism | PHYS-31 (p < 0.05) | **PARKED** |
| PHYS-35 | Boundary Count | PHYS-31 (p < 0.05) | **PARKED** |

All four Track B papers were contingent on the gate. The gate fires at p = 0.81. None will be written.

---

### TABLE 31.13: THE COMPLETE RESEARCH PROGRAM — UPDATED STATUS

| Track | Papers | Status | Basis |
|---|---|---|---|
| Track A: Unification | PHYS-26 through PHYS-30 | **COMPLETE** | 63/64 checks, α_s within 1σ |
| Track B: Cosmology | PHYS-31 (gate), PHYS-32–35 | **PARKED** | p = 0.81, gate fires |
| Track C: Structure | PHYS-36 through PHYS-40 | **INDEPENDENT** | Not gated by Track B |

Track A is the primary result of the series. Track B is a documented null. Track C proceeds on its own merits.

---

### TABLE 31.14: CUMULATIVE VERIFICATION

| Script | Checks | Status | Paper |
|---|---|---|---|
| phys31_statistical_control.py | **9/10** | **1 FAIL (gate)** | **This paper** |
| phys30_alpha_s.py | 9/9 | PASS | PHYS-30 |
| phys29_gut_thresholds.py | 10/11 | 1 abort | PHYS-29 |
| phys28_vl_twoloop.py | 11/11 | PASS | PHYS-28 |
| phys27_sin2tw.py | 13/13 | PASS | PHYS-27 |
| phys26_normalization.py | 20/20 | ALL EXACT | PHYS-26 |
| phys25_platform.py | 47/47 | PASS | PHYS-25 |
| beta_unification_test.py | 15/15 | PASS | Beta cosmology |
| qed_predicts_gr.py + scan2 | 20/20 | PASS | QED-to-GR |
| phys24_lib.py + test | 169/169 | PASS | Platform |
| 8 PHYS-24 demo scripts | 62/62 | PASS | PHYS-24 |
| 6 Session 3 scripts | 98/98 | PASS | Session 3 |
| **Grand total** | **483/486** | **2 designed FAIL + 1 prior** | **Complete series** |

The two designed FAILs: PHYS-29 abort (minimal SU(5) disfavored) and PHYS-31 gate (Track B parked). Both are features of the abort/gate system, not script errors.

---

**End of supporting appendix tables for PHYS-31. 14 tables. The null result is fully characterized: p = 0.81, the beta integers score 6/8 hits which is below the random mean of 6.2, and 81% of random pools do equally well. The distinction between Track A (dynamics, validated) and Track B (numerology, parked) is documented with explicit evidence. The formula space analysis explains WHY random pools succeed. Grand total: 483/486, two designed failures plus one prior.**
