========================================================================
HOWL ELECTROWEAK NOTEBOOK
========================================================================

RESULT 1: FULL COMPARISON TABLE (tree + Δρ)
------------------------------------------------------------------------

  Observable         Computed     Measured    Ratio     Status
  -------------- ------------ ------------ -------- ----------
  Γ_l (MeV)           84.1877      83.9840   1.0024  excellent
  Γ_inv (MeV)        502.2920     499.0000   1.0066       good
  Γ_Z (MeV)         2510.6090    2495.2000   1.0062       good
  R_l                 20.8552      20.7670   1.0042  excellent
  R_b                  0.2197       0.2163   1.0158       good
  R_c                  0.1704       0.1721   0.9904       good
  A_FB^l               0.0167       0.0171   0.9789   expected
  A_l (SLD)            0.1494       0.1513   0.9874       good
  σ⁰_had (nb)         41.3987      41.4810   0.9980  excellent
  N_ν (LEP)            2.9080       2.9840   0.9745   expected
  M_W (MeV)        80325.5856   80369.2000   0.9995  excellent

  11/11 within 5% (expected for tree + Δρ)

RESULT 2: PARAMETER EXTRACTIONS
------------------------------------------------------------------------

  sin²θ_W from A_l(SLD):  0.23097801  (input: 0.23122000, Δ = -2.4199e-04)
  sin²θ_W from A_FB^l:    0.23101658  (input: 0.23122000, Δ = -2.0342e-04)
  Two extractions agree:   Δ = 3.9e-05

  α_s from R_l:            0.10425276  (input: 0.11800000, Δ = -1.3747e-02)
  (12% low — expected missing b-quark vertex correction)

RESULT 3: KEY NUMBERS FOR DATA-2 EXTENSION
------------------------------------------------------------------------

  Quantity                                  Value               Source
  ------------------------------ ---------------- --------------------
  Δρ                                   0.00933226     3G_Fm_t²/(8π²√2)
  ρ_eff                                1.00933226               1 + Δρ
  Γ₀ (MeV)                               331.7652       G_FM_Z³/(6π√2)
  δ_QCD                                1.03887169          1+α_s/π+...
  v_e                               -0.0375600000            -1/2+2s²w
  A_e                                0.1493969509      2v_ea_e/(v²+a²)
  M_W tree (MeV)                         79953.38          M_Z√(1-s²w)
  M_W +Δρ (MeV)                          80325.59             ×√(1+Δρ)
  sin²θ_W(eff) from A_l                0.23097801           extraction
  sin²θ_W(eff) from A_FB               0.23101658           extraction
  α_s from R_l (tree+Δρ)               0.10425276           extraction

RESULT 4: INTEGER ANATOMY
------------------------------------------------------------------------

  All coefficients in the computation classified by origin:

  Integer           Value                   Origin                Enters in
  ------------ ---------- ------------------------ ------------------------
  N_c                   3              SU(3) color             quark widths
  T₃                 ±1/2            SU(2) isospin            all couplings
  Q_e                  −1              U(1) charge                      v_e
  Q_u                +2/3              U(1) charge                      v_u
  Q_d                −1/3              U(1) charge                      v_d
  n_ν                   3              generations                    Γ_inv
  n_l                   3              generations                Γ_l total
  n_u                   2        generations (u,c)                    Γ_had
  n_d                   3      generations (d,s,b)                    Γ_had
  6                     6              phase space      Γ₀ = G_FM_Z³/(6π√2)
  3/4                 3/4      angular integration       A_FB = (3/4)A_eA_f
  12                   12              phase space           σ⁰_had formula
  3, 8                3/8            loop counting    Δρ = 3G_Fm_t²/(8π²√2)
  c₁                    1               QCD 1-loop                    δ_QCD
  c₂               365/24      QCD 2-loop rational                    δ_QCD

  Transcendental content: π (phase space), π² and √2 (Δρ)
  Both enter as Q335 exact integers.
  Measured content: G_F, M_Z, α⁻¹, sin²θ_W, α_s, m_t, m_H
  These 7 values are the ONLY non-integer input.

RESULT 5: MISSING CORRECTIONS — WHY RESIDUALS EXIST
------------------------------------------------------------------------

  Observable       Residual              Dominant missing correction
  -------------- ---------- ----------------------------------------
  Γ_l                +0.24%          EW vertex +0.2%, QED FSR +0.17%
  Γ_Z                +0.62%     Sum of all partial width corrections
  R_l                +0.42%    b-quark vertex reduces Γ_had by ~0.4%
  R_b                +1.58%   t-b-W vertex loop reduces Γ_b by ~1.5%
  R_c                −0.96%             Vertex correction adds ~0.5%
  A_l                −1.26%               eff sin²θ shift of ~2×10⁻⁴
  A_FB^l             −2.11%         Goes as A_e², double sensitivity
  σ⁰_had             −0.20%                 Correlated with Γ shifts
  N_ν                −2.55%             Computed Γ_vis 0.6% too high
  M_W                −0.05%  Full Δr (running α, boxes) adds ~40 MeV
  α_s ext.             −12%           Needs full 1-loop EW for Γ_had

  Every residual is explained by known physics not yet included.
  One-loop would reduce all to <0.3%, but the integer anatomy
  is already fully visible at tree + Δρ. The structure is in
  the laws (integers), not in the precision of the residuals.

RESULT 6: DECISIONS
------------------------------------------------------------------------

  COMPLETED: Tree + Δρ electroweak computation, 14/14 checks pass.

  DECLINED: One-loop extension.
    Reason: 3-4 hours to reimplement ZFITTER in Fraction arithmetic.
    Produces no structural finding. Every residual already explained.
    The integer anatomy is complete at tree level. Adding loops adds
    more integers of the same kind from the same gauge group.
    Compare: PHYS-5 (gap ratio), PHYS-6 (confinement wall), PHYS-9
    (g-2 decomposition) each produced a FINDING. One-loop EW would
    confirm 'the SM works at one-loop' — already known.

  OPEN PATHS from this computation:
    - sin²θ_W from 3/8 + RG running (structural question)
    - Gap ratio particle content enumeration (BSM constraint)
    - A₂ coefficient in R₂/R₄ form (anatomy of QED)
    - b-quark vertex correction alone (one diagram, tests R_b)

========================================================================
CHECKS
========================================================================

  [PASS] Γ_l within 1%
  [PASS] Γ_Z within 2%
  [PASS] Γ_inv within 2%
  [PASS] R_l within 1%
  [PASS] R_b within 2%
  [PASS] R_c within 2%
  [PASS] A_FB^l within 5%
  [PASS] A_l within 3%
  [PASS] σ⁰_had within 1%
  [PASS] M_W within 1%
  [PASS] N_ν in [2.5, 3.5]
  [PASS] sin²θ_W extractions agree
  [PASS] A_l extraction converged
  [PASS] R_l extraction converged

  TOTAL: 14 PASS, 0 FAIL out of 14

========================================================================
ELECTROWEAK NOTEBOOK COMPLETE — ALL CHECKS PASS
========================================================================
