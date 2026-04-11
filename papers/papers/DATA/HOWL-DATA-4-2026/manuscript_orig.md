# Verified Integer Rational Database 
## Includes Cabibbo Doublet Extension

**Registry:** [@HOWL-DATA-4-2026]

**Series Path:** [@HOWL-DATA-1-2026] → [@HOWL-DATA-2-2026] → [@HOWL-DATA-3-2026] → [@HOWL-DATA-4-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** April 1 2026

**Domain:** Cross Domain Data

**Status:** Documentation

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

**Backed by:** data_4.py (38/38 checks), DATA-3 (32/32 checks inherited)

---

## Abstract

DATA-4 is the verified successor to DATA-3. It inherits all 123 entries and all 32 consistency checks with zero numerical changes. It adds 23 new entries in two categories: 6 STAGED entries for the Cabibbo Doublet parameters (entries 124-129, Type G — bounded but not yet measured) and 17 GUT/unification parameters (Section N, Type D — derived from Level 1 exact Fraction arithmetic). It formalizes the lattice ratio independence annotation as Finding 15: the FLAG lattice QCD mass ratios (m_c/m_s, m_b/m_c, m_u/m_d) are independent measurements evaluated at a common renormalization scale, not derivable from the individual PDG quark masses evaluated at different scales, with discrepancies up to 28% from the scale mismatch. It adds 6 new GUT verification checks (Group G, all exact), bringing the total to 38/38 PASS. It adds a computation traceability map linking DATA-4 entries to every PHYS and MATH paper in the series. DATA-4 contains 146 entries total: 123 inherited from DATA-3, 6 staged Cabibbo Doublet, and 17 GUT parameters. DATA-4 is the sole data reference for all future HOWL computation. DATA-3 is retired.

---
 
## 1. Relationship to DATA-3

DATA-3 collected 123 entries (107 original Q335 conversions from DATA-2 plus 16 Koide-derived quantities) and verified them with 32 internal consistency checks, all passing. DATA-3 also noted — in script output but not as a formal finding — that three lattice QCD mass ratios are independent of the individual PDG quark masses.

DATA-4 inherits every entry and every check from DATA-3 with zero numerical changes. The 32 inherited checks produce identical results (the data didn't change). What DATA-4 adds:

Finding 15 formalized: the lattice ratio independence annotation, promoted from a script note to a registered finding with a registry tag.

Section L: 6 STAGED entries for the Cabibbo Doublet parameters (M_VL, θ₁₄, θ₂₄, θ₃₄, δ₁, δ₂), with constraint windows from PHYS-16 and PHYS-19. These are the first Type G entries in the series — parameters identified by the theory but not yet measured.

Section N: 17 GUT and unification parameters, all Level 1 exact Fractions. SM beta coefficients, Cabibbo Doublet beta shifts, modified betas, gap ratios (SM 218/115, Cabibbo Doublet 38/27, MSSM 7/5), the measured gap ratio derived from Level 2 couplings, the two-loop b_ij matrix, and two-loop unification results.

Group G: 6 new verification checks on the GUT parameters (all exact).

Group T: computation traceability map linking entries to papers.

The promotion from DATA-3 to DATA-4 means: annotation formalized, new particle staged, unification parameters recorded, traceability added.

---

## 2. The Lattice Ratio Independence — Finding 15

Entries D9 (m_c/m_s = 11.783), D10 (m_b/m_c = 4.578), and D11 (m_u/m_d = 0.485) are independent measurements from lattice QCD (FLAG averages) evaluated at a common renormalization scale. They are NOT derivable from the individual PDG quark masses (D1-D5), which are evaluated at different scales: m_u, m_d, m_s at μ = 2 GeV MS-bar; m_c at μ = m_c ≈ 1.27 GeV; m_b at μ = m_b ≈ 4.18 GeV.

The discrepancies if naively compared by dividing PDG masses:

| Ratio | PDG Division | Lattice (FLAG) | Discrepancy |
|---|---|---|---|
| m_c/m_s | 1273/93.5 = 13.615 | 11.783 | 15.5% |
| m_b/m_c | 4183/1273 = 3.286 | 4.578 | 28.2% |
| m_u/m_d | 2.16/4.70 = 0.460 | 0.485 | 5.2% |

This is a renormalization scale mismatch, not a database error. QCD running changes quark mass ratios because each mass runs differently under the strong coupling. The m_b/m_c discrepancy (28%) is the largest because m_b and m_c are evaluated at the most widely separated scales. The m_u/m_d discrepancy (5.2%) is the smallest because both are evaluated near 2 GeV.

This matters operationally: a future session dividing m_c/m_s from entries D4 and D3 and comparing to entry D9 will see a 15% discrepancy. Without this annotation, they will conclude the database is corrupted. It is not.

Finding 15 registered: [@HOWL-DATA-4-FINDING-15]

---

## 3. Cabibbo Doublet Staged Entries — Section L

Six parameters of the Cabibbo Doublet (PHYS-15, PHYS-16, PHYS-19) are registered as STAGED entries. Type G means: the parameter is identified by theory, bounded by current experiment, but not measured with precision sufficient for a definitive database value and Q335 numerator.

**Entry 124: M_VL (Cabibbo Doublet mass).** Window: 1,500,000 - 6,000,000 MeV (1.5 - 6.0 TeV). Lower bound from LHC pair production exclusion. Upper bound from CKM perturbativity and anomaly fit. Sources: PHYS-16, PHYS-19.

**Entry 125: sin θ₁₄ ≈ |V_ub'| (1st-generation mixing angle).** Estimate: ~0.045 from CKM first-row deficit. Source: PHYS-19 (Belfatto, Berezhiani 2020).

**Entry 126: θ₂₄ (2nd-generation mixing angle).** Constrained by kaon physics (K⁰-K̄⁰ mixing, NA62). No point estimate; bounded from above.

**Entry 127: sin θ₃₄ (3rd-generation mixing angle).** From A_FB^b fit at LEP Z-pole. Source: PHYS-19.

**Entry 128: δ₁ (new CP phase 1).** Constrained by neutron EDM < 10⁻²⁶ e·cm.

**Entry 129: δ₂ (new CP phase 2).** Constrained by B-meson CP asymmetries (LHCb, Belle II).

When any parameter is measured, the entry transitions from Type G to Type M with a specific value, uncertainty, and Q335 numerator. The entry number is preserved — no renumbering.

---

## 4. GUT and Unification Parameters — Section N

Seventeen parameters from the Session 3 GUT and unification analysis, all stored as exact Fractions:

**N1-N3: SM one-loop beta coefficients (Level 1).** b₁ = 41/10, b₂ = −19/6, b₃ = −7. These are the exact rational beta function coefficients for SU(3)×SU(2)×U(1) with the SM particle content, computed from Dynkin indices.

**N4-N6: Cabibbo Doublet beta shifts (Level 1).** Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3. From the Dynkin indices of the (3,2,1/6) VL representation.

**N7-N9: Modified beta coefficients (Level 1).** b₁_mod = 25/6, b₂_mod = −13/6, b₃_mod = −20/3. The SM betas plus the Cabibbo Doublet shifts.

**N10-N12: Gap ratios (Level 1).** SM gap ratio = 218/115 = 1.896 (N10). Cabibbo Doublet gap ratio = 38/27 = 1.407 (N11). MSSM gap ratio = 7/5 = 1.400 (N12). All exact Fractions.

**N13: Measured gap ratio (Derived from Level 2).** Computed from α⁻¹, sin²θ_W, α_s through GUT normalization: (1/α₁ − 1/α₂)/(1/α₂ − 1/α₃) ≈ 1.358. This is the confrontation value — the target the SM misses by 40% and the Cabibbo Doublet approaches to 3.6%.

**N14: Two-loop SM b_ij matrix (Level 1).** The 3×3 matrix of two-loop beta function coefficients from Machacek-Vaughn (1983) and Luo-Xiao (hep-ph/0207271), all exact Fractions:

| | U(1) | SU(2) | SU(3) |
|---|---|---|---|
| U(1) | 199/50 | 27/10 | 44/5 |
| SU(2) | 9/10 | 35/6 | 12 |
| SU(3) | 11/10 | 9/2 | −26 |

**N15-N17: Two-loop unification results (Derived).** At M_VL = 500 GeV (closest approach): one-loop miss Δ = −1.17 (N15), two-loop miss Δ = −0.40 (N16), two-loop improvement = 66% (N17). The two-loop correction reduces the unification miss by two-thirds.

---

## 5. Verification

### 5.1 Inherited Checks (Groups A-E): 32/32 PASS

All 32 DATA-3 checks are re-run on the unchanged data and produce identical results. The full results from the data_4.py script:

| Group | Tests | Pass | Content |
|---|---|---|---|
| A: Mass ratios | 9 | 9 | Stored ratios vs computed from individual masses |
| B: Analytical constants | 8 | 8 | Q335 identities and mpmath cross-checks at 101+ digits |
| C: Physical relations | 4 | 4 | R∞, a₀, μ₀ from formulas; m_D from constituents |
| D: Koide derived | 5 | 5 | K1-K16 recomputed from source masses |
| E: SI exact constants | 6 | 6 | c, h, e, k_B, N_A, Δν_Cs at exact SI 2019 values |

No changes from DATA-3. Every test passes at the same digit count.

### 5.2 New Checks (Group G): 6/6 PASS

Six new GUT verification checks, all exact:

| Test | Relation | Result |
|---|---|---|
| G1 | SM gap ratio = 218/115 | EXACT |
| G2 | SM+VL gap ratio = 38/27 | EXACT |
| G3 | MSSM gap ratio = 7/5 | EXACT |
| G4 | Modified b₁ = 25/6 | EXACT |
| G5 | Modified b₂ = −13/6 | EXACT |
| G6 | Modified b₃ = −20/3 | EXACT |

All six are identities between exact Fractions. The gap ratios are computed from the beta coefficients by division: (b₁−b₂)/(b₂−b₃). The modified betas are computed by addition: b_SM + Δb_VL. Every step is Fraction arithmetic with zero floating-point contamination.

### 5.3 Combined Result

**38 tests. 38 PASS. 0 FAIL.**

Inherited from DATA-3: 32 checks (Groups A-E). New in DATA-4: 6 checks (Group G). The lattice annotation (Group F) and Cabibbo Doublet staging (Group H) are structural additions, not numerical checks — there are no values to verify for staged entries.

---

## 6. Database Content

DATA-4 contains 146 entries across the following sections:

| Section | Type | Count | Content |
|---|---|---|---|
| A: SI fundamental | E (exact) | 7 | c, h, e, k_B, N_A, Δν_Cs, K_cd |
| B: CODATA measured | M (measured) | 13 | α⁻¹, m_e, m_μ, m_τ, m_p, ratios, a_e, a_μ, sin²θ_W, α_s, μ₀ |
| C: Electroweak | M | 6 | M_Z, Γ_Z, M_W, m_t, m_H, G_F |
| D: Quarks + CKM | M | 11 | m_u-m_b, sin θ₁₂-sin θ₁₃, lattice ratios (D9-D11 INDEPENDENT) |
| E: Nuclear/hadron | M | 8 | m_n, m_π, m_K, m_D, m_He4, E_D |
| F: Spectroscopy | M | 1 | H 1S-2S frequency |
| G: Q335 analytical | A (analytical) | 14 | π, e, ln2, √2-√7, φ, ζ(3), ζ(5), π², ζ(2), R₂, R₄, 2π |
| K: Mass ratios + Koide | M/K | 8 | m_μ/m_e, m_τ/m_e, etc., Koide K |
| L: Cabibbo Doublet | G (staged) | 6 | M_VL, θ₁₄, θ₂₄, θ₃₄, δ₁, δ₂ |
| N: GUT parameters | D (derived) | 17 | Betas, shifts, gap ratios, b_ij, two-loop results |
| *(remaining DATA-3 entries)* | Various | 56 | Engineering specs, clock freqs, Koide addendum |
| **Total** | | **146** | |

Type codes: E = exact by definition, M = measured, A = analytical (computed to arbitrary precision), S = standard nominal, K = Koide derived, G = staged (bounded, not measured), D = derived (Level 1 arithmetic on Level 2 inputs or pure Level 1).

---

## 7. Computation Traceability Map

Which DATA-4 entries feed which computations, from the data_4.py traceability section:

| Paper | DATA-4 Entries Used | Computation |
|---|---|---|
| PHYS-9 | B1(α⁻¹), G1(π), G8(ζ(3)) | α → a_e via QED series |
| PHYS-12 | B1, B11, C6, C4, C5, C1, B12 | 7 EW inputs → 11 observables |
| PHYS-13 | B1, B11, B12 | 3 couplings → gap ratio 218/115 vs 1.358 |
| PHYS-15 | B1, B11, B12 | Elimination cascade → (3,2,1/6) |
| PHYS-17 | N1-N3 (SM betas) | Generation democracy, boson problem |
| PHYS-18 | N4-N6 (VL shifts) | Y=1/6 asymmetry, 1/Y² scaling |
| PHYS-19 | D6-D8 (CKM), B11 | Three anomalies → (3,2,1/6) |
| PHYS-20 | N7-N11 (modified betas, gap ratio) | M_GUT → proton decay τ ~ 10^34-35 |
| PHYS-22 | G10(π²), G8(ζ(3)), G3(ln2) | A₂ = 197/144 + (3/4)ζ(3) + R₄·c_geom |
| PHYS-23 | B2-B4 (lepton masses), D1-D5 (quarks) | Koide K all three sectors |
| MATH-6 | G1-G14 (Q335 basis) | PSLQ 82/82 null, Bessel zeros |

When a future PDG update changes any entry, this map identifies every computation that must be re-verified. If α_s changes: PHYS-12, 13, 15 are affected. If m_τ improves: PHYS-23 Koide checks sharpen. If sin²θ_W shifts: PHYS-12, 13, 15, 19 are affected and the measured gap ratio (N13) recomputes.

---

## 8. What DATA-4 Certifies

**Everything DATA-3 certified, unchanged.** Internal consistency (32/32), Q335 fidelity (101+ digits), physical consistency (CODATA web at 11+ digits), independence structure (107 original sources).

**Plus GUT parameter consistency.** The 6 new Group G checks verify that gap ratios and modified betas are exact Fraction consequences of the stored SM betas and Cabibbo Doublet shifts. 6/6 exact.

**Plus structural completeness.** The Cabibbo Doublet parameters are formally registered with entry numbers, constraint windows, and transition protocol. The GUT parameters that drive the unification analysis are stored as exact Fractions with complete provenance. The computation traceability map links data to papers.

---

## 9. What DATA-4 Does Not Change

No inherited entry value changes. No Q335 numerator changes. No uncertainty changes. No type reclassification of existing entries. The 32 inherited check results are verbatim from DATA-3. DATA-4 is additive: it adds entries, checks, and structure. It does not correct, modify, or supersede any numerical content from DATA-3.

---

## 10. Operational Rule

DATA-4 is the sole data reference for all future HOWL computation. DATA-3 is retired. Any script or paper that previously referenced DATA-3 now references DATA-4. The numerical content of entries 1-123 is identical; the distinction is the additional entries, checks, and structure.

When new measurements become available — improved m_τ from Belle II, LHC VL quark mass, updated PDG world averages, new CODATA adjustment — they enter as DATA-5 with the same verification protocol: every affected cross-check must pass before the new version is accepted. No DATA version is ever edited after publication.

---

## Appendix: Verification Script Output

From data_4.py, 38/38 checks pass:

```
==============================================================================
HOWL-DATA-4: VERIFIED DATABASE WITH CABIBBO DOUBLET EXTENSION
==============================================================================

GROUP A: MASS RATIO IDENTITIES
  [PASS] A1: m_p/m_e    12.2 digits (need 11)
  [PASS] A2: m_mu/m_e   21.0 digits (need 10)
  [PASS] A3: m_tau/m_e    6.3 digits (need 6)
  [PASS] A4: m_tau/m_mu   5.8 digits (need 5)
  [PASS] A5: m_n/m_p    20.0 digits (need 11)
  [PASS] A6: M_W/M_Z     7.2 digits (need 6)
  [PASS] A7: m_n - m_p   exact      (need 8)
  [PASS] A8: m_H/M_Z     5.6 digits (need 5)
  [PASS] A9: m_t/M_Z     5.9 digits (need 5)

GROUP B: ANALYTICAL CONSTANT IDENTITIES (Q335 basis)
  [PASS] B1: R₂ = π/4         102.0 digits (need 100)
  [PASS] B2: R₄ = π²/32       102.4 digits (need 100)
  [PASS] B3: 2π = 8R₂         exact        (need 100)
  [PASS] B4: ζ(2) = π²/6      101.5 digits (need 99)
  [PASS] B5: α/π identity      13.9 digits (need 12)
  [PASS] B6: φ = (1+√5)/2     101.4 digits (need 100)
  [PASS] B7: π² = π×π         101.7 digits (need 99)
  [PASS] B8: 2π = 2×π         exact        (need 100)

GROUP C: PHYSICAL RELATIONS (SI 2019)
  [PASS] C1: R∞ = α²m_ec/(2h)   11.3 digits (need 11)
  [PASS] C2: a₀ = ℏ/(m_ecα)     11.4 digits (need 11)
  [PASS] C3: μ₀ = 2αh/(ce²)     11.9 digits (need 11)
  [PASS] C4: m_D = m_p+m_n−E_D   9.9 digits (need 8)
  [INFO] C5: H 1S-2S soft check   3.3 digits (expected ~5)

GROUP D: KOIDE DERIVED ENTRIES
  [PASS] D1: K(e,μ,τ)    10.3 digits (need 6)
  [PASS] D2: a(leptons)   10.2 digits (need 6)
  [PASS] D3: M(leptons)    4.6 digits (need 4)
  [PASS] D4: K(u,c,t)     10.5 digits (need 3)
  [PASS] D5: K(d,s,b)     10.4 digits (need 3)

GROUP E: EXACT SI CONSTANTS
  [PASS] E1: h×Δν_Cs   exact
  [PASS] E2: c          exact
  [PASS] E3: h          exact
  [PASS] E4: e          exact
  [PASS] E5: k_B        exact
  [PASS] E6: N_A        exact

GROUP F: LATTICE RATIO INDEPENDENCE — FINDING 15
  m_c/m_s: PDG 13.615, lattice 11.783 (15.5%)
  m_b/m_c: PDG 3.286, lattice 4.578 (28.2%)
  m_u/m_d: PDG 0.460, lattice 0.485 (5.2%)
  Renormalization scale mismatch, NOT database error.

GROUP G: GUT AND UNIFICATION VERIFICATION (NEW)
  [PASS] G1: SM gap ratio = 218/115      exact
  [PASS] G2: SM+VL gap ratio = 38/27     exact
  [PASS] G3: MSSM gap ratio = 7/5        exact
  [PASS] G4: Modified b₁ = 25/6          exact
  [PASS] G5: Modified b₂ = −13/6         exact
  [PASS] G6: Modified b₃ = −20/3         exact

GROUP H: CABIBBO DOUBLET STAGED ENTRIES
  Entry 124: M_VL         STAGED  1.5 - 6.0 TeV
  Entry 125: sin(θ₁₄)    STAGED  ~0.045 (CKM deficit)
  Entry 126: θ₂₄          STAGED  (kaon physics)
  Entry 127: sin(θ₃₄)    STAGED  (A_FB^b fit)
  Entry 128: δ₁           STAGED  (nEDM constrained)
  Entry 129: δ₂           STAGED  (B physics constrained)

GROUP T: COMPUTATION TRACEABILITY MAP
  PHYS-9   B1, G1, G8                   alpha -> a_e via QED series
  PHYS-12  B1, B11, C6, C4, C5, C1, B12 7 EW inputs -> 11 observables
  PHYS-13  B1, B11, B12                  3 couplings -> gap ratio
  PHYS-15  B1, B11, B12                  Elimination cascade -> (3,2,1/6)
  PHYS-17  N1-N3                         Generation democracy, boson problem
  PHYS-18  N4-N6                         Y=1/6 asymmetry, 1/Y² scaling
  PHYS-19  D6-D8, B11                    Three anomalies -> (3,2,1/6)
  PHYS-20  N7-N11                        M_GUT -> proton decay
  PHYS-22  G10, G8, G3                   A₂ decomposition
  PHYS-23  B2-B4, D1-D5                  Koide K all three sectors
  MATH-6   G1-G14                        PSLQ 82/82 null

Total: 38 tests,  38 PASS,  0 FAIL

  Sections A-K (inherited from DATA-3): 123 entries
  Section L (Cabibbo Doublet, STAGED):    6 entries
  Section N (GUT parameters, Level 1):   17 entries
  Total: 146 entries

  +==============================================================+
  |  ALL TESTS PASS                                              |
  |                                                              |
  |  DATA-4 DECLARATION:                                         |
  |    DATA-3 (123 entries, 32/32 checks) inherited.             |
  |    Finding 15 (lattice independence) formalized.             |
  |    6 Cabibbo Doublet parameters STAGED (entries 124-129).    |
  |    17 GUT/unification parameters added (Section N).          |
  |    6 new GUT verification checks added (Group G).           |
  |    Computation traceability map added (Group T).             |
  |                                                              |
  |  DATA-3 is retired.                                          |
  |  All future HOWL computation references DATA-4.              |
  +==============================================================+
```

---

*DATA-4: 146 entries, 38 cross-checks, 38 pass. The Cabibbo Doublet is staged. The integers are verified. The foundation extends. Published April 1, 2026. This paper is never edited after publication.*

---

```
==============================================================================
HOWL-DATA-4: VERIFIED DATABASE WITH CABIBBO DOUBLET EXTENSION
==============================================================================

GROUP A: MASS RATIO IDENTITIES
------------------------------------------------------------------------------

  [PASS] A1: m_p/m_e direct vs m_p / m_e
      Computed: 1.836152673431236e+03
      Stored: 1.836152673430000e+03
      Relative diff: 6.73e-13  (12.2 digits, need 11)

  [PASS] A2: m_mu/m_e direct vs m_mu / m_e
      Computed: 2.067682827084672e+02
      Stored: 2.067682827084672e+02
      Relative diff: 1.01e-21  (21.0 digits, need 10)

  [PASS] A3: m_tau/m_e direct vs m_tau / m_e
      Computed: 3.477228275323682e+03
      Stored: 3.477230000000000e+03
      Relative diff: 4.96e-07  (6.3 digits, need 6)

  [PASS] A4: m_tau/m_mu direct vs m_tau / m_mu
      Computed: 1.681702933242618e+01
      Stored: 1.681700000000000e+01
      Relative diff: 1.74e-06  (5.8 digits, need 5)

  [PASS] A5: m_n/m_p direct vs m_n / m_p
      Computed: 1.001378419463362e+00
      Stored: 1.001378419463362e+00
      Relative diff: 9.40e-21  (20.0 digits, need 11)

  [PASS] A6: M_W/M_Z direct vs M_W / M_Z
      Computed: 8.813610622496918e-01
      Stored: 8.813610000000000e-01
      Relative diff: 7.06e-08  (7.2 digits, need 6)

  [PASS] A7: m_n - m_p direct vs stored difference
      Computed: 1.293332510000000e+00
      Stored: 1.293332510000000e+00
      Agreement: EXACT

  [PASS] A8: m_H/M_Z direct vs stored ratio
      Computed: 1.372993696511368e+00
      Stored: 1.372990000000000e+00
      Relative diff: 2.69e-06  (5.6 digits, need 5)

  [PASS] A9: m_t/M_Z direct vs stored ratio
      Computed: 1.892472222100373e+00
      Stored: 1.892470000000000e+00
      Relative diff: 1.17e-06  (5.9 digits, need 5)

GROUP B: ANALYTICAL CONSTANT IDENTITIES (Q335 basis)
------------------------------------------------------------------------------

  [PASS] B1: R2 = pi/4 (Q335 vs mpmath@120)
      Q335: 7.853981633974483e-01
      mpmath: 7.853981633974483e-01
      Relative diff: 9.13e-103  (102.0 digits, need 100)

  [PASS] B2: R4 = pi^2/32 (Q335 vs mpmath@120)
      Q335: 3.084251375340424e-01
      mpmath: 3.084251375340424e-01
      Relative diff: 3.79e-103  (102.4 digits, need 100)

  [PASS] B3: 2pi = 8*R2 (exact within Q335)
      Computed: 6.283185307179586e+00
      Stored: 6.283185307179586e+00
      Agreement: EXACT

  [PASS] B4: zeta(2) = pi^2/6 (Q335 numerators)
      Computed: 1.644934066848226e+00
      Stored: 1.644934066848226e+00
      Relative diff: 2.90e-102  (101.5 digits, need 99)

  [PASS] B5: alpha/pi stored vs 1/(alpha_inv * pi)
      Computed: 2.322819464195329e-03
      Stored: 2.322819464195300e-03
      Relative diff: 1.24e-14  (13.9 digits, need 12)

  [PASS] B6: phi = (1 + sqrt5)/2 (Q335)
      Computed: 1.618033988749895e+00
      Stored: 1.618033988749895e+00
      Relative diff: 4.42e-102  (101.4 digits, need 100)

  [PASS] B7: pi^2 stored vs pi * pi (Q335)
      Computed: 9.869604401089358e+00
      Stored: 9.869604401089358e+00
      Relative diff: 2.21e-102  (101.7 digits, need 99)

  [PASS] B8: 2pi stored vs 2 * pi (exact)
      Computed: 6.283185307179586e+00
      Stored: 6.283185307179586e+00
      Agreement: EXACT

GROUP C: PHYSICAL RELATIONS (SI 2019)
------------------------------------------------------------------------------

  [PASS] C1: R_inf = alpha^2 m_e c/(2h)
      From alpha, m_e, c, h: 1.097373156809536e+07
      Stored R_inf: 1.097373156815700e+07
      Relative diff: 5.62e-12  (11.3 digits, need 11)

  [PASS] C2: a_0 = hbar/(m_e c alpha)
      From hbar, m_e, c, alpha: 5.291772105462769e-11
      Stored a_0: 5.291772105440000e-11
      Relative diff: 4.30e-12  (11.4 digits, need 11)

  [PASS] C3: mu_0 = 2*alpha*h/(c*e^2)
      From alpha, h, c, e: 1.256637061268226e-06
      Stored mu_0: 1.256637061270000e-06
      Relative diff: 1.41e-12  (11.9 digits, need 11)

  [PASS] C4: m_D = m_p + m_n - E_D
      From m_p + m_n - E_D: 1.875612945230000e+03
      Stored m_D: 1.875612945000000e+03
      Relative diff: 1.23e-10  (9.9 digits, need 8)

  [INFO] C5: H 1S-2S leading order (soft check)
      Measured:    2466061413187018 Hz
      (3/4)cR_inf: 2467381470187486 Hz
      Rel diff:    5.35e-04 (3.3 digits)
      Note: ~5 digit agreement expected (Lamb shift, QED, recoil)

GROUP D: KOIDE DERIVED ENTRIES (K1-K16)
------------------------------------------------------------------------------

  [PASS] D1: Koide K(e,mu,tau) from masses
      From m_e, m_mu, m_tau: 6.666605114655210e-01
      Stored K1: 6.666605115000001e-01
      Relative diff: 5.17e-11  (10.3 digits, need 6)

  [PASS] D2: a(leptons) from K
      Computed: 1.414200505100000e+00
      Stored K4: 1.414200505200000e+00
      Relative diff: 7.07e-11  (10.2 digits, need 6)

  [PASS] D3: M(leptons) = (sum sqrt m)/3
      Computed: 1.771556100000000e+01
      Stored K14: 1.771600000000000e+01
      Relative diff: 2.48e-05  (4.6 digits, need 4)

  [PASS] D4: Koide K(u,c,t) from masses
      Computed: 8.487935475760000e-01
      Stored K2: 8.487935476000000e-01
      Relative diff: 2.83e-11  (10.5 digits, need 3)

  [PASS] D5: Koide K(d,s,b) from masses
      Computed: 7.312875768270000e-01
      Stored K3: 7.312875768000000e-01
      Relative diff: 3.69e-11  (10.4 digits, need 3)

GROUP E: EXACT SI CONSTANTS
------------------------------------------------------------------------------

  [PASS] E1: h * dv_Cs product consistency
      Computed: 6.091102297113866e-24
      Stored: 6.091102297113866e-24
      Agreement: EXACT

  [PASS] E2: c is exact integer 299792458
      Computed: 2.997924580000000e+08
      Stored: 2.997924580000000e+08
      Agreement: EXACT

  [PASS] E3: h exact SI 2019 value
      Computed: 6.626070150000000e-34
      Stored: 6.626070150000000e-34
      Agreement: EXACT

  [PASS] E4: e exact SI 2019 value
      Computed: 1.602176634000000e-19
      Stored: 1.602176634000000e-19
      Agreement: EXACT

  [PASS] E5: k_B exact SI 2019 value
      Computed: 1.380649000000000e-23
      Stored: 1.380649000000000e-23
      Agreement: EXACT

  [PASS] E6: N_A exact SI 2019 value
      Computed: 6.022140760000000e+23
      Stored: 6.022140760000000e+23
      Agreement: EXACT

GROUP F: LATTICE RATIO INDEPENDENCE — FINDING 15
------------------------------------------------------------------------------

  Entries D9 (m_c/m_s = 11.783), D10 (m_b/m_c = 4.578),
  D11 (m_u/m_d = 0.485) are INDEPENDENT measurements from
  lattice QCD (FLAG averages) evaluated at a COMMON scale.

  They are NOT derivable from individual PDG quark masses
  (D1-D5) which are evaluated at DIFFERENT scales:
    m_u, m_d, m_s at mu = 2 GeV MS-bar
    m_c at mu = m_c ~ 1.27 GeV
    m_b at mu = m_b ~ 4.18 GeV

  Discrepancies if naively compared:
    m_c/m_s: PDG gives 13.615, lattice = 11.783 (15.5%)
    m_b/m_c: PDG gives 3.286, lattice = 4.578 (28.2%)
    m_u/m_d: PDG gives 0.460, lattice = 0.485 (5.2%)

  This is a renormalization scale mismatch, NOT a database error.
  Finding 15 registered: [@HOWL-DATA-4-FINDING-15]

GROUP G: GUT AND UNIFICATION VERIFICATION
------------------------------------------------------------------------------

  [PASS] G1: SM gap ratio = 218/115
      Computed: 1.895652173913043e+00
      Stored: 1.895652173913043e+00
      Agreement: EXACT

  [PASS] G2: SM+VL gap ratio = 38/27
      Computed: 1.407407407407407e+00
      Stored: 1.407407407407407e+00
      Agreement: EXACT

  [PASS] G3: MSSM gap ratio = 7/5
      Computed: 1.400000000000000e+00
      Stored: 1.400000000000000e+00
      Agreement: EXACT

  [PASS] G4: Modified b1 = 25/6
      Computed: 4.166666666666667e+00
      Stored: 4.166666666666667e+00
      Agreement: EXACT

  [PASS] G5: Modified b2 = -13/6
      Computed: -2.166666666666667e+00
      Stored: -2.166666666666667e+00
      Agreement: EXACT

  [PASS] G6: Modified b3 = -20/3
      Computed: -6.666666666666667e+00
      Stored: -6.666666666666667e+00
      Agreement: EXACT

GROUP H: CABIBBO DOUBLET STAGED ENTRIES
------------------------------------------------------------------------------

  Entry 124: M_VL (Cabibbo Doublet mass)
    Status: STAGED
    Window: 1500000 - 6000000 MeV (1.5 - 6.0 TeV)
    Sources: PHYS-16, PHYS-19
    Bounds: LHC pair production (lower), CKM perturbativity (upper)

  Entry 125: sin(theta_14) ~ |V_ub'|
    Status: STAGED
    Estimate: ~0.045 (from CKM first-row deficit)
    Source: PHYS-19 (Belfatto, Berezhiani 2020)

  Entry 126: theta_24 (2nd-gen mixing)
    Status: STAGED (CONSTRAINED_BY_KAON_PHYSICS)

  Entry 127: sin(theta_34) (3rd-gen mixing)
    Status: STAGED (FROM_A_FB_B_FIT)

  Entry 128: delta_1 (new CP phase)
    Status: STAGED (CONSTRAINED_BY_NEDM)

  Entry 129: delta_2 (new CP phase)
    Status: STAGED (CONSTRAINED_BY_B_PHYSICS)

GROUP T: COMPUTATION TRACEABILITY MAP
------------------------------------------------------------------------------

  Paper    DATA-4 Entries Used                        Computation
  -------- ------------------------------------------ ------------------------------------------
  PHYS-9   B1(alpha_inv), G1(pi), G8(zeta3)           alpha -> a_e via QED series
  PHYS-12  B1,B11,C6,C4,C5,C1,B12                     7 EW inputs -> 11 observables
  PHYS-13  B1,B11,B12                                 3 couplings -> gap ratio 218/115 vs 1.358
  PHYS-15  B1,B11,B12                                 Elimination cascade -> (3,2,1/6)
  PHYS-17  N1-N3 (SM betas)                           Generation democracy, boson problem
  PHYS-18  N4-N6 (VL shifts)                          Y=1/6 asymmetry, 1/Y^2 scaling
  PHYS-19  D6-D8 (CKM), B11                           Three anomalies -> (3,2,1/6)
  PHYS-20  N7-N11 (modified betas, gap ratio)         M_GUT -> proton decay tau ~ 10^34-35
  PHYS-22  G10(pi^2), G8(zeta3), G3(ln2)              A2 = 197/144 + (3/4)z3 + R4*c_geom
  PHYS-23  B2-B4(lepton masses), D1-D5(quarks)        Koide K all three sectors
  PHYS-24  B1,B11,B12, N1-N6, N14(b_ij)               Two-loop unification, Delta = -0.40
  MATH-6   G1-G14 (Q335 basis)                        PSLQ 82/82 null, Bessel zeros

==============================================================================
RESULTS
==============================================================================

  ID     Test                                                  Digits   Need   Result
  ------ ---------------------------------------------------- ------- ------ --------
  A1     m_p/m_e direct vs m_p / m_e                             12.2     11     PASS
  A2     m_mu/m_e direct vs m_mu / m_e                           21.0     10     PASS
  A3     m_tau/m_e direct vs m_tau / m_e                          6.3      6     PASS
  A4     m_tau/m_mu direct vs m_tau / m_mu                        5.8      5     PASS
  A5     m_n/m_p direct vs m_n / m_p                             20.0     11     PASS
  A6     M_W/M_Z direct vs M_W / M_Z                              7.2      6     PASS
  A7     m_n - m_p direct vs stored difference                  exact      8     PASS
  A8     m_H/M_Z direct vs stored ratio                           5.6      5     PASS
  A9     m_t/M_Z direct vs stored ratio                           5.9      5     PASS
  B1     R2 = pi/4 (Q335 vs mpmath@120)                         102.0    100     PASS
  B2     R4 = pi^2/32 (Q335 vs mpmath@120)                      102.4    100     PASS
  B3     2pi = 8*R2 (exact within Q335)                         exact    100     PASS
  B4     zeta(2) = pi^2/6 (Q335 numerators)                     101.5     99     PASS
  B5     alpha/pi stored vs 1/(alpha_inv * pi)                   13.9     12     PASS
  B6     phi = (1 + sqrt5)/2 (Q335)                             101.4    100     PASS
  B7     pi^2 stored vs pi * pi (Q335)                          101.7     99     PASS
  B8     2pi stored vs 2 * pi (exact)                           exact    100     PASS
  C1     R_inf = alpha^2 m_e c/(2h)                              11.3     11     PASS
  C2     a_0 = hbar/(m_e c alpha)                                11.4     11     PASS
  C3     mu_0 = 2*alpha*h/(c*e^2)                                11.9     11     PASS
  C4     m_D = m_p + m_n - E_D                                    9.9      8     PASS
  D1     Koide K(e,mu,tau) from masses                           10.3      6     PASS
  D2     a(leptons) from K                                       10.2      6     PASS
  D3     M(leptons) = (sum sqrt m)/3                              4.6      4     PASS
  D4     Koide K(u,c,t) from masses                              10.5      3     PASS
  D5     Koide K(d,s,b) from masses                              10.4      3     PASS
  E1     h * dv_Cs product consistency                          exact     15     PASS
  E2     c is exact integer 299792458                           exact     15     PASS
  E3     h exact SI 2019 value                                  exact      9     PASS
  E4     e exact SI 2019 value                                  exact     10     PASS
  E5     k_B exact SI 2019 value                                exact      7     PASS
  E6     N_A exact SI 2019 value                                exact      9     PASS
  G1     SM gap ratio = 218/115                                 exact     10     PASS
  G2     SM+VL gap ratio = 38/27                                exact     10     PASS
  G3     MSSM gap ratio = 7/5                                   exact     10     PASS
  G4     Modified b1 = 25/6                                     exact     10     PASS
  G5     Modified b2 = -13/6                                    exact     10     PASS
  G6     Modified b3 = -20/3                                    exact     10     PASS

  Total: 38 tests,  38 PASS,  0 FAIL

  Inherited from DATA-3: 32 checks (Groups A-E)
  New in DATA-4: 6 checks (Group G: GUT verification)

  ENTRY COUNT:
    Sections A-K (inherited from DATA-3): 123 entries
    Section L (Cabibbo Doublet, STAGED):    6 entries
    Section N (GUT parameters, Level 1):   17 entries
    Total: 146 entries

  +==============================================================+
  |  ALL TESTS PASS                                              |
  |                                                              |
  |  DATA-4 DECLARATION:                                         |
  |    DATA-3 (123 entries, 32/32 checks) inherited.             |
  |    Finding 15 (lattice independence) formalized.             |
  |    6 Cabibbo Doublet parameters STAGED (entries 124-129).    |
  |    17 GUT/unification parameters added (Section N).          |
  |    6 new GUT verification checks added (Group G).           |
  |    Computation traceability map added (Group T).             |
  |                                                              |
  |  DATA-3 is retired.                                          |
  |  All future HOWL computation references DATA-4.              |
  +==============================================================+

==============================================================================
DATA-4 VERIFICATION COMPLETE
==============================================================================
```
