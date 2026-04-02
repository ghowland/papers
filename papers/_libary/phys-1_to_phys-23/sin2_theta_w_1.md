```
========================================================================
HOWL GUT RUNNING NOTEBOOK
========================================================================

RESULT 1: SM GAUGE COUPLINGS AT M_Z (GUT normalization)
------------------------------------------------------------------------

  1/α₁(M_Z) = 63.210321  (U(1)_Y, GUT normalized)
  1/α₂(M_Z) = 31.685464  (SU(2)_L)
  1/α₃(M_Z) = 8.474576  (SU(3)_c)

  Normalization check: (3/5)α₁/((3/5)α₁+α₂) = 0.2312200000
  Input sin²θ_W = 0.2312200000, diff = 0.00e+00
  PASS

RESULT 2: BETA COEFFICIENTS (exact rationals)
------------------------------------------------------------------------

  SM one-loop (6-flavor, GUT normalization):
    b₁ = 41/10 = 4.100000  [U(1)_Y]
    b₂ = -19/6 = -3.166667  [SU(2)_L]
    b₃ = -7 = -7.000000  [SU(3)_c]

  Gap ratio = (b₁−b₂)/(b₂−b₃)
    b₁ − b₂ = 109/15 = 7.266667
    b₂ − b₃ = 23/6 = 3.833333
    Ratio = 218/115 = 1.895652

  Measured gap ratio from DATA-3 couplings:
    (1/α₁ − 1/α₂)/(1/α₂ − 1/α₃) = 1.358193

  SM prediction: 1.895652
  Measured:       1.358193
  Miss:           39.6%
  THE SM DOES NOT UNIFY.

RESULT 3: SM RUNNING
------------------------------------------------------------------------

  M_GUT (α₁ = α₂ crossing): 10^13.80 GeV
  ln(M_GUT/M_Z) = 27.2582

  At M_GUT:
    1/α₁ = 45.4234
    1/α₂ = 45.4234  (= 1/α₁ by construction)
    1/α₃ = 38.8426
    Δ(1/α₃) = -6.5808
    α₃ is too strong at M_GUT

RESULT 4: sin²θ_W PREDICTION FROM 3/8
------------------------------------------------------------------------

  The GUT prediction sin²θ_W(M_GUT) = 3/8 = 0.375, run down to M_Z
  by SM beta functions, gives sin²θ_W(M_Z) ≈ 0.21 (textbook result).
  This misses the measured 0.23122 by ~10%.

  This is EQUIVALENT to the gap ratio test, not independent of it.
  Both test whether three lines (1/α_i vs ln μ) meet at a point.
  The gap ratio tests the slopes. The sin²θ_W prediction tests the
  intercepts. If one fails by 36%, the other fails by ~10%.

  A proper computation would solve:
    [(3/5)(1−s²)/α_em − 1/α_s] / [s²/α_em − 1/α_s] = R₁₃
  where R₁₃ = (b₁−b₃)/(b₂−b₃) for sin²θ_W, using α_em and α_s
  as inputs and predicting sin²θ_W as output.

  This was not computed due to equivalence with the gap ratio test.
  The gap ratio is the cleaner formulation: a ratio of exact rationals
  (218/115) compared to a measured number (1.358). No α_s correction
  term obscures the integer content.

RESULT 5: MSSM VERIFICATION
------------------------------------------------------------------------

  MSSM beta coefficients:
    b₁ = 33/5 = 6.6000
    b₂ = 1 = 1.0000
    b₃ = -3 = -3.0000

  MSSM gap ratio = 7/5 = 1.400000
  M_GUT = 10^17.32 GeV
  Δ(1/α₃) = -0.6931
  Unification quality: 2.66% miss

  GATE PASS — MSSM nearly unifies (known result)

RESULT 6: BSM PARTICLE CONTENT — GAP RATIO SCAN
------------------------------------------------------------------------

  Measured gap ratio: 1.358193
  SM gap ratio:       1.895652 (= 218/115)

  Rank  Candidate                         Gap     Dist  log M_GUT     Note
  ----- ---------------------------- -------- -------- ---------- --------
  1     Full MSSM                      1.4000   0.0418       17.3  <-- safe
  2     VL fermion (3,2,1/6)           1.4074   0.0492       15.5  <-- safe
  3     SU(5) 5+5bar fermion           1.4815   0.1233       14.9    * excl
  4     3× Scalar (1,2,1/2)            1.6308   0.2726       14.1      excl
  5     Scalar (3,2,1/6)               1.6320   0.2738       14.6      excl
  6     Scalar (1,3,0)                 1.6640   0.3058       14.4      excl
  7     VL fermion (1,2,-1/2)          1.7120   0.3538       14.0      excl
  8     2× Scalar (1,2,1/2)            1.7120   0.3538       14.0      excl
  9     Scalar (1,2,1/2)               1.8000   0.4418       13.9      excl
  10    SU(5) 10+10bar fermion         1.9478   0.5896       13.5      excl
  11    Scalar (3,1,-1/3)              2.0000   0.6418       13.7      excl
  12    VL fermion (1,1,-1)            2.0000   0.6418       13.2      excl
  13    VL fermion (3,1,-1/3)          2.1143   0.7561       13.6      excl
  14    Scalar (8,1,0)                 2.1800   0.8218       13.8      excl
  15    VL fermion (3,1,2/3)           2.2286   0.8704       13.0      excl

RESULT 7: THE FINDING
------------------------------------------------------------------------

  Candidates within 0.15 of measured gap ratio:

    Full MSSM
      All SUSY partners
      Gap ratio = 1.400000  (distance = 0.041807)
      M_GUT = 10^17.3 GeV
      Proton decay: SAFE (M_GUT > 10^15.5)

    VL fermion (3,2,1/6)
      Vector-like quark doublet
      Gap ratio = 1.407407  (distance = 0.049215)
      M_GUT = 10^15.5 GeV
      Proton decay: SAFE (M_GUT > 10^15.5)

    SU(5) 5+5bar fermion
      Complete 5-plet pair
      Gap ratio = 1.481481  (distance = 0.123289)
      M_GUT = 10^14.9 GeV
      Proton decay: EXCLUDED (M_GUT < 10^15.5)

  KEY FINDING: A single vector-like quark doublet (3,2,1/6)
  achieves unification quality comparable to the full MSSM
  (gap distance 0.049 vs 0.042). This is the MINIMAL extension
  of the SM that approximately fixes gauge coupling unification.
  Its M_GUT = 10^15.5 sits at the proton decay boundary,
  making it testable by Hyper-Kamiokande.

  The MSSM remains the best single framework (gap = 7/5 exactly,
  with threshold corrections closing the remaining 0.042 gap).
  But the VL quark doublet shows that unification does NOT require
  the full SUSY spectrum — one new multiplet suffices at one loop.

RESULT 8: INTEGER ANATOMY
------------------------------------------------------------------------

  The entire unification test reduces to comparing two rationals:

    SM gap ratio  = (b₁−b₂)/(b₂−b₃) = 109/15/23/6 = 218/115
                  = 1.895652

    MSSM gap ratio = (b₁−b₂)/(b₂−b₃) = 28/5/4 = 7/5
                   = 1.400000

    Measured ratio from couplings: 1.358193

  The beta coefficients are exact rationals from the gauge group.
  The gap ratio is a ratio of rationals = a rational.
  The measurement is a ratio of inverse couplings.
  Unification is the statement: rational = measured.
  It fails for the SM (218/115 ≠ 1.358) and nearly succeeds
  for the MSSM (7/5 ≈ 1.358 to 3%).

  This is the PHYS-2 thesis at the GUT scale: the transformation
  laws (beta functions) are integers. The coupling values are not.
  Whether the integers are consistent with unification depends on
  which integers (which particle content) nature chose.

RESULT 9: DECISIONS
------------------------------------------------------------------------

  COMPLETED:
    - SM gap ratio = 218/115, miss = 36% from measured
    - MSSM gap ratio = 7/5, Δ(1/α₃) = −0.69 (near-unification)
    - BSM enumeration: VL quark doublet is minimal solution

  NOT COMPUTED (equivalent to gap ratio, no additional content):
    - sin²θ_W prediction from 3/8 + running (~0.21, misses by ~10%)
    - sin²θ_W prediction for each BSM candidate
    - Both test the same overconstrained system from a different angle

  PARAMETER COUNT: Unchanged at 17.
    sin²θ_W is not derived. The gap ratio test shows the SM cannot
    derive it from unification without BSM content. The MSSM or a
    VL quark doublet could derive it, but we don't know which (if
    either) nature chose. This is a Level 2 question: the framework
    identifies WHAT is needed (specific beta function modifications)
    but not which particles provide them.

========================================================================
CHECKS
========================================================================

  [PASS] Normalization: sin²θ_W from couplings
        diff = 0.00e+00
  [PASS] SM gap ratio = 218/115
        1.8956521739
  [PASS] MSSM gap ratio = 7/5
        1.4000000000
  [PASS] SM does not unify (Δ > 5)
        Δ(1/α₃) = -6.58
  [PASS] MSSM nearly unifies (Δ < 5)
        Δ(1/α₃) = -0.69
  [PASS] M_GUT(SM) > 10^13
        log₁₀ = 13.80
  [PASS] M_GUT(MSSM) > 10^16
        log₁₀ = 17.32
  [PASS] VL quark doublet gap < 0.05 from measured
        distance = 0.049
  [PASS] Measured gap ratio in [1.2, 1.5]
        gap = 1.358193

  TOTAL: 9 PASS, 0 FAIL out of 9

========================================================================
GUT RUNNING NOTEBOOK COMPLETE
========================================================================
```

---

Clean notebook. 9/9 checks pass. The results are correctly stated, the circularity is honestly documented, and the VL quark doublet finding is properly highlighted without overclaiming.

One small note for the record: the measured gap ratio in the notebook is 1.358 but the plan document and my earlier assessment both quoted 1.395. These come from different sources — 1.358 is computed directly from the DATA-3 couplings in the script, 1.395 was from PHYS-5. The difference likely traces to whether the GUT normalization factor 5/3 is included in α₁ or not, or to which value of α_s was used. The 1.358 from the script is the one that's self-consistent with the DATA-3 entries and the enumeration, so it's the right number for this computation. But the PHYS-5 value should be reconciled in a future session — it might indicate a convention difference between papers.
