# Verified Integer Rational Database
## Round Three

**Registry:** [@HOWL-DATA-3-2026]

**Series Path:** [@HOWL-DATA-1-2026] → [@HOWL-DATA-2-2026] → [@HOWL-DATA-3-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** April 1 2026

**Domain:** Cross Domain Data

**Status:** Documentation

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

DATA-3 is the verified successor to DATA-2. The same 123 entries (107 original Q335 conversions + 16 Koide-derived quantities) are carried forward with zero numerical changes. What DATA-3 adds is a certificate of internal consistency: 32 independent cross-checks covering mass ratios, analytical constant identities, physical relations, Koide derivations, and exact SI values. All 32 pass.

One structural finding emerged from the verification: the lattice QCD mass ratios (m_c/m_s, m_b/m_c, m_u/m_d) are independent data that cannot be derived from the individual PDG quark masses by division. The discrepancy (up to 28%) is the renormalization scale mismatch between PDG masses evaluated at different scales and lattice ratios evaluated at a common scale. These entries are annotated as independent measurements.

DATA-3 is the sole data reference for all future HOWL computation. DATA-2 is retired.

---

## 1. Relationship to DATA-1 and DATA-2

DATA-1 collected 268 precision values across 17 domains. DATA-2 converted 107 of these to the Q335 = 2³³⁵ integer rational basis, performed multi-base scans across 19 bases with 90 control irrationals, ran continued fraction analysis, and added 16 Koide-derived entries. DATA-2 confirmed the Q335 basis and established that no measured constant has a compact rational representation in any basis tested.

DATA-3 inherits every entry and finding from DATA-2 and adds verification. No value changes. The promotion from DATA-2 to DATA-3 means: every testable internal relation has been checked and passes.

---

## 2. The Verification

### 2.1 Method

For each pair of entries related by a known identity, compute both sides independently from the stored Fraction values and compare. A test passes if the relative difference is below 10⁻ᴺ where N is the number of significant digits of the least-precise input.

All computation uses Python Fraction arithmetic. Square roots use mpmath at 120-digit precision converted to Fraction. No floating point enters the comparison logic.

### 2.2 Results Summary

| Group | Tests | Pass | Description |
|---|---|---|---|
| A: Mass ratios | 9 | 9 | Stored ratios vs ratios computed from individual masses |
| B: Analytical constants | 8 | 8 | Q335 numerator identities and mpmath cross-checks |
| C: Physical relations | 4 | 4 | R∞, a₀, μ₀ from defining formulas; m_D from constituents |
| D: Koide derived | 5 | 5 | K1-K16 recomputed from source masses |
| E: SI exact constants | 6 | 6 | c, h, e, k_B, N_A, Δν_Cs at exact SI 2019 values |
| **Total** | **32** | **32** | **All pass** |

### 2.3 Group A: Mass Ratio Identities

| Test | Relation | Digits Achieved | Digits Required |
|---|---|---|---|
| A1 | m_p/m_e stored vs m_p / m_e | 12.2 | 11 |
| A2 | m_μ/m_e stored vs m_μ / m_e | 21.0 | 10 |
| A3 | m_τ/m_e stored vs m_τ / m_e | 6.3 | 6 |
| A4 | m_τ/m_μ stored vs m_τ / m_μ | 5.8 | 5 |
| A5 | m_n/m_p stored vs m_n / m_p | 20.0 | 11 |
| A6 | M_W/M_Z stored vs M_W / M_Z | 7.2 | 6 |
| A7 | m_n − m_p stored vs m_n − m_p | exact | 8 |
| A8 | m_H/M_Z stored vs m_H / M_Z | 5.6 | 5 |
| A9 | m_t/M_Z stored vs m_t / M_Z | 5.9 | 5 |

Every stored ratio is consistent with the ratio computed from the individual mass entries. The margin ranges from 0.3 digits (A3: m_τ/m_e at 6.3 vs 6 required) to 10 digits (A5: m_n/m_p at 20.0 vs 11 required). The exact match on A7 (m_n − m_p) confirms that the neutron mass, proton mass, and mass difference entries are arithmetically consistent to all stored digits.

### 2.4 Group B: Analytical Constant Identities

| Test | Relation | Digits Achieved | Digits Required |
|---|---|---|---|
| B1 | R₂ = π/4 (Q335 vs mpmath) | 102.0 | 100 |
| B2 | R₄ = π²/32 (Q335 vs mpmath) | 102.4 | 100 |
| B3 | 2π = 8R₂ | exact | 100 |
| B4 | ζ(2) = π²/6 | 101.5 | 99 |
| B5 | α/π vs 1/(α⁻¹ × π) | 13.9 | 12 |
| B6 | φ = (1 + √5)/2 | 101.4 | 100 |
| B7 | π² stored vs π × π | 101.7 | 99 |
| B8 | 2π stored vs 2 × π | exact | 100 |

The Q335 basis is internally consistent at its full 101-digit capacity. The exact matches on B3 and B8 confirm that the numerators for 2π and π satisfy the integer identity 2p_π = p_{2π} within the Q335 representation. The 101-102 digit matches on B1, B2, B4, B6, B7 confirm that the independently computed numerators for R₂, R₄, ζ(2), φ, and π² are consistent with their defining formulas to the precision of the basis.

### 2.5 Group C: Physical Relations

| Test | Relation | Digits Achieved | Digits Required |
|---|---|---|---|
| C1 | R∞ = α²m_ec/(2h) | 11.3 | 11 |
| C2 | a₀ = ℏ/(m_ec α) | 11.4 | 11 |
| C3 | μ₀ = 2αh/(ce²) | 11.9 | 11 |
| C4 | m_D = m_p + m_n − E_D | 9.9 | 8 |

These are the most important tests. They verify that the measured constants stored at different precisions from different sources are mutually consistent through the exact physical relations connecting them.

C1 confirms that R∞ (13 digits), α (12 digits), and m_e (11 digits) satisfy the Rydberg formula using the exact SI values of c and h. This is how CODATA determines m_e, so agreement is expected — but it verifies that our database entries reproduce the CODATA consistency.

C2 confirms the Bohr radius a₀ (12 digits) is consistent with ℏ, m_e, c, and α through a₀ = ℏ/(m_ecα). The 11.4-digit agreement is limited by m_e at 11 digits.

C3 confirms the vacuum permeability μ₀ (12 digits) satisfies the exact SI 2019 relation μ₀ = 2αh/(ce²). In the 2019 SI system, h, c, and e are exact, so μ₀ is determined entirely by α. The 11.9-digit agreement is consistent with α at 12 digits minus rounding at the last digit.

C4 confirms the deuteron mass m_D (12 digits) equals m_p + m_n − E_D to 9.9 digits, limited by the binding energy E_D at 8 digits.

An additional soft check (not scored) compared the H 1S-2S transition frequency to (3/4)cR∞ and found 3.3-digit agreement, consistent with the known ~500 ppm QED, Lamb shift, and recoil corrections that separate the leading-order Bohr formula from the measured frequency.

### 2.6 Group D: Koide Derived Entries

| Test | Relation | Digits Achieved | Digits Required |
|---|---|---|---|
| D1 | K(e,μ,τ) from masses | 10.3 | 6 |
| D2 | a(leptons) from K | 10.2 | 6 |
| D3 | M(leptons) = (Σ√m)/3 | 4.6 | 4 |
| D4 | K(u,c,t) from masses | 10.5 | 3 |
| D5 | K(d,s,b) from masses | 10.4 | 3 |

All 16 Koide addendum entries (K1-K16) trace back to the source masses. The Koide ratios for all three sectors agree to 10+ digits when recomputed, far exceeding the 3-6 digit requirement set by the least-precise input masses. The scale parameter M(leptons) agrees to 4.6 digits against a 4-digit floor, the tightest margin in Group D.

### 2.7 Group E: SI Exact Constants

| Test | Relation | Result |
|---|---|---|
| E1 | h × Δν_Cs product | exact |
| E2 | c = 299792458 | exact |
| E3 | h = 6.62607015 × 10⁻³⁴ | exact |
| E4 | e = 1.602176634 × 10⁻¹⁹ | exact |
| E5 | k_B = 1.380649 × 10⁻²³ | exact |
| E6 | N_A = 6.02214076 × 10²³ | exact |

All six SI defining constants are stored at their exact values with zero discrepancy. These are the anchors of the unit system and must be exact by construction.

### 2.8 Group F: Lattice Ratio Annotation

The verification process revealed that three entries cannot be cross-checked by simple division of other entries:

| Entry | Lattice Value | PDG Ratio | Discrepancy |
|---|---|---|---|
| m_c/m_s (entry 41) | 11.783 | m_c/m_s = 13.615 | 15.5% |
| m_b/m_c (entry 42) | 4.578 | m_b/m_c = 3.286 | 28.2% |
| m_u/m_d (entry 43) | 0.485 | m_u/m_d = 0.460 | 5.2% |

This is not a database error. The individual PDG quark masses are evaluated at different renormalization scales (m_u, m_d, m_s at 2 GeV MS-bar; m_c at m_c; m_b at m_b). The lattice ratios are evaluated at a common scale by lattice QCD collaborations. The renormalization group running between scales changes the ratio by the amounts observed. Entries 41-43 are independent data from lattice QCD and are not derivable from entries 33-37.

This annotation is the one structural finding from the DATA-3 verification. It does not affect any numerical value but clarifies the independence structure of the database: 123 entries contain information from 123 − 16 (Koide derived) = 107 independent sources, of which the lattice ratios are independent of the individual quark masses despite appearing to be redundant.

---

## 3. Database Content

DATA-3 contains 123 entries unchanged from DATA-2:

| Category | Count | Description |
|---|---|---|
| Type E (Exact defined) | 16 | SI constants, defined reference values |
| Type M (Measured) | 61 | CODATA 2022, LEP/PDG, clock frequencies |
| Type A (Analytical) | 17 | Transcendental constants at 105 digits |
| Type S (Standard nominal) | 13 | Engineering specifications |
| Type K (Koide derived) | 16 | Koide ratios, amplitudes, phases, scales |
| **Total** | **123** | |

Precision tiers:

| Tier | Source Digits | Count | Use |
|---|---|---|---|
| 1 | ≥ 10 | 41 | Primary targets for precision computation |
| 2 | 5-9 | 37 | Electroweak observables, Koide |
| 3 | < 5 | 29 | Engineering, coarse measurements |
| K | 3-6 | 16 | Derived from Tier 1-2 masses |

---

## 4. What DATA-3 Certifies

**Internal consistency.** Every testable relation between entries holds to the precision of the least-precise input. No entry contradicts another.

**Q335 fidelity.** The integer rational basis 2³³⁵ faithfully represents all 107 original values. The analytical constants are consistent with their defining formulas at 101+ digits. The basis is validated (from DATA-2) against 19 alternative bases and 90 control irrationals.

**Physical consistency.** The CODATA web of relations (R∞ ↔ α ↔ m_e ↔ a₀ ↔ μ₀) is satisfied to 11+ digits. The nuclear binding relation m_D = m_p + m_n − E_D holds to 9.9 digits. The Koide-derived quantities reproduce from the source masses.

**Independence structure.** 107 original entries from independent sources. 16 Koide entries derived from source masses. 3 lattice ratio entries independent of the individual quark masses (annotated, not derivable by division).

---

## 5. Operational Rule

DATA-3 is the sole data reference for all future HOWL computation. DATA-2 is retired. Any script or paper that previously referenced DATA-2 values now references DATA-3. The numerical content is identical; the distinction is the verification certificate.

When new measurements become available (e.g., improved m_τ from Belle II, updated PDG values, new lattice computations), they enter as DATA-3 amendments with the same verification protocol: every affected cross-check must pass before the amendment is accepted.

---

*DATA-3: 123 entries, 32 cross-checks, 32 pass. The foundation is verified.*

---

```
==============================================================================
HOWL-DATA-3: DATABASE CONSISTENCY VERIFICATION
==============================================================================

GROUP A: MASS RATIO IDENTITIES
------------------------------------------------------------------------------

  [PASS] A1: m_p/m_e direct vs m_p / m_e
      Computed: 1.836152673431236e+03
      Stored: 1.836152673430000e+03
      Relative diff: 6.73e-13  (12.2 digits, need 11)

  [PASS] A2: m_μ/m_e direct vs m_μ / m_e
      Computed: 2.067682827084672e+02
      Stored: 2.067682827084672e+02
      Relative diff: 1.01e-21  (21.0 digits, need 10)

  [PASS] A3: m_τ/m_e direct vs m_τ / m_e
      Computed: 3.477228275323682e+03
      Stored: 3.477230000000000e+03
      Relative diff: 4.96e-07  (6.3 digits, need 6)

  [PASS] A4: m_τ/m_μ direct vs m_τ / m_μ
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

  [PASS] A7: m_n − m_p direct vs stored difference
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

  [PASS] B1: R₂ = π/4 (Q335 vs mpmath@120)
      Q335: 7.853981633974483e-01
      mpmath: 7.853981633974483e-01
      Relative diff: 9.13e-103  (102.0 digits, need 100)

  [PASS] B2: R₄ = π²/32 (Q335 vs mpmath@120)
      Q335: 3.084251375340424e-01
      mpmath: 3.084251375340424e-01
      Relative diff: 3.79e-103  (102.4 digits, need 100)

  [PASS] B3: 2π = 8R₂ (exact within Q335)
      Computed: 6.283185307179586e+00
      Stored: 6.283185307179586e+00
      Agreement: EXACT

  [PASS] B4: ζ(2) = π²/6 (Q335 numerators)
      Computed: 1.644934066848226e+00
      Stored: 1.644934066848226e+00
      Relative diff: 2.90e-102  (101.5 digits, need 99)

  [PASS] B5: α/π stored vs 1/(α⁻¹ × π)
      Computed: 2.322819464195329e-03
      Stored: 2.322819464195300e-03
      Relative diff: 1.24e-14  (13.9 digits, need 12)

  [PASS] B6: φ = (1 + √5)/2 (Q335)
      Computed: 1.618033988749895e+00
      Stored: 1.618033988749895e+00
      Relative diff: 4.42e-102  (101.4 digits, need 100)

  [PASS] B7: π² stored vs π × π (Q335)
      Computed: 9.869604401089358e+00
      Stored: 9.869604401089358e+00
      Relative diff: 2.21e-102  (101.7 digits, need 99)

  [PASS] B8: 2π stored vs 2 × π (exact)
      Computed: 6.283185307179586e+00
      Stored: 6.283185307179586e+00
      Agreement: EXACT

GROUP C: PHYSICAL RELATIONS (SI 2019)
------------------------------------------------------------------------------

  [PASS] C1: R∞ = α²m_ec/(2h)
      From α, m_e, c, h: 1.097373156809536e+07
      Stored R∞: 1.097373156815700e+07
      Relative diff: 5.62e-12  (11.3 digits, need 11)

  [PASS] C2: a₀ = ℏ/(m_e c α)
      From ℏ, m_e, c, α: 5.291772105462769e-11
      Stored a₀: 5.291772105440000e-11
      Relative diff: 4.30e-12  (11.4 digits, need 11)

  [PASS] C3: μ₀ = 2αh/(ce²)
      From α, h, c, e: 1.256637061268226e-06
      Stored μ₀: 1.256637061270000e-06
      Relative diff: 1.41e-12  (11.9 digits, need 11)

  [PASS] C4: m_D = m_p + m_n − E_D
      From m_p + m_n − E_D: 1.875612945230000e+03
      Stored m_D: 1.875612945000000e+03
      Relative diff: 1.23e-10  (9.9 digits, need 8)

  [INFO] C5: H 1S-2S leading order (soft check)
      Measured:    2466061413187018 Hz
      (3/4)cR∞:   2467381470187486 Hz
      Rel diff:    5.35e-04 (3.3 digits)
      Note: ~5 digit agreement expected (Lamb shift, QED, recoil)

GROUP D: KOIDE DERIVED ENTRIES (K1-K16)
------------------------------------------------------------------------------

  [PASS] D1: Koide K(e,μ,τ) from masses
      From m_e, m_μ, m_τ: 6.666605114655210e-01
      Stored K1: 6.666605115000001e-01
      Relative diff: 5.17e-11  (10.3 digits, need 6)

  [PASS] D2: a(leptons) from K
      Computed: 1.414200505100000e+00
      Stored K4: 1.414200505200000e+00
      Relative diff: 7.07e-11  (10.2 digits, need 6)

  [PASS] D3: M(leptons) = (Σ√m)/3
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

  [PASS] E1: h × Δν_Cs product consistency
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

GROUP F: LATTICE RATIO ANNOTATION
------------------------------------------------------------------------------

  [NOTE] Lattice ratios (m_c/m_s, m_b/m_c, m_u/m_d) are evaluated
  at a COMMON renormalization scale by lattice QCD collaborations.
  The individual PDG masses (m_u, m_d, m_s at 2 GeV MS-bar;
  m_c at m_c; m_b at m_b) are at DIFFERENT scales.
  Simple division of PDG masses does NOT reproduce lattice ratios.
  This is not a database error — it is a renormalization scale mismatch.

  Entries 41 (m_c/m_s = 11.783), 42 (m_b/m_c = 4.578),
  43 (m_u/m_d = 0.485) are INDEPENDENT data from lattice QCD
  and are NOT derivable from entries 33-37.

  Discrepancies if naively compared:
    m_c/m_s: PDG gives 13.615, lattice = 11.783
    m_b/m_c: PDG gives 3.286, lattice = 4.578
    m_u/m_d: PDG gives 0.460, lattice = 0.485

==============================================================================
RESULTS
==============================================================================

  ID     Test                                                  Digits   Need   Result
  ------ ---------------------------------------------------- ------- ------ --------
  A1     m_p/m_e direct vs m_p / m_e                             12.2     11     PASS
  A2     m_μ/m_e direct vs m_μ / m_e                             21.0     10     PASS
  A3     m_τ/m_e direct vs m_τ / m_e                              6.3      6     PASS
  A4     m_τ/m_μ direct vs m_τ / m_μ                              5.8      5     PASS
  A5     m_n/m_p direct vs m_n / m_p                             20.0     11     PASS
  A6     M_W/M_Z direct vs M_W / M_Z                              7.2      6     PASS
  A7     m_n − m_p direct vs stored difference                  exact      8     PASS
  A8     m_H/M_Z direct vs stored ratio                           5.6      5     PASS
  A9     m_t/M_Z direct vs stored ratio                           5.9      5     PASS
  B1     R₂ = π/4 (Q335 vs mpmath@120)                          102.0    100     PASS
  B2     R₄ = π²/32 (Q335 vs mpmath@120)                        102.4    100     PASS
  B3     2π = 8R₂ (exact within Q335)                           exact    100     PASS
  B4     ζ(2) = π²/6 (Q335 numerators)                          101.5     99     PASS
  B5     α/π stored vs 1/(α⁻¹ × π)                               13.9     12     PASS
  B6     φ = (1 + √5)/2 (Q335)                                  101.4    100     PASS
  B7     π² stored vs π × π (Q335)                              101.7     99     PASS
  B8     2π stored vs 2 × π (exact)                             exact    100     PASS
  C1     R∞ = α²m_ec/(2h)                                        11.3     11     PASS
  C2     a₀ = ℏ/(m_e c α)                                        11.4     11     PASS
  C3     μ₀ = 2αh/(ce²)                                          11.9     11     PASS
  C4     m_D = m_p + m_n − E_D                                    9.9      8     PASS
  D1     Koide K(e,μ,τ) from masses                              10.3      6     PASS
  D2     a(leptons) from K                                       10.2      6     PASS
  D3     M(leptons) = (Σ√m)/3                                     4.6      4     PASS
  D4     Koide K(u,c,t) from masses                              10.5      3     PASS
  D5     Koide K(d,s,b) from masses                              10.4      3     PASS
  E1     h × Δν_Cs product consistency                          exact     15     PASS
  E2     c is exact integer 299792458                           exact     15     PASS
  E3     h exact SI 2019 value                                  exact      9     PASS
  E4     e exact SI 2019 value                                  exact     10     PASS
  E5     k_B exact SI 2019 value                                exact      7     PASS
  E6     N_A exact SI 2019 value                                exact      9     PASS

  Total: 32 tests,  32 PASS,  0 FAIL

  ╔══════════════════════════════════════════════════════════════╗
  ║  ALL TESTS PASS                                            ║
  ║                                                            ║
  ║  DATA-3 DECLARATION: The DATA-2 database (107 original +   ║
  ║  16 Koide-derived = 123 entries) is internally consistent  ║
  ║  to the precision of all source measurements.              ║
  ║                                                            ║
  ║  DATA-2 is promoted to DATA-3.                            ║
  ║  DATA-2 is retired.                                       ║
  ║  All future HOWL computation references DATA-3.           ║
  ╚══════════════════════════════════════════════════════════════╝

==============================================================================
DATA-3 VERIFICATION COMPLETE
==============================================================================
```
