# PHYS-56 Planning Document — Revision 3

**Registry:** [@HOWL-PHYS-56-2026-PLAN-R3]

**Parent Spec:** PCTRM-1-MASTER-2026

**Supersedes:** PHYS-56 Plan Revisions 1 and 2 (inadequate integration of CD and PHYS-40 content)

**Purpose:** Final plan for PHYS-56 drafting, now integrating PHYS-40 derivation map + Cabibbo Doublet (CD) content alongside DATA-7 experimental baseline

**Date:** April 20, 2026

---

## I. What Revision 3 Integrates Beyond Revision 2

Revision 2 treated the PHYS-55 / DATA-7 experimental baseline but missed the PHYS-40 "You Are Here II" derivation map and the Cabibbo Doublet evidence structure. These are central to the framework and must be integrated into PHYS-56.

**Major additions in Revision 3:**

1. **PHYS-40 derivation map** — 53 derived values from 13 measured inputs, surplus +40, across 8 physics domains connected by 12 crossings

2. **Cabibbo Doublet (CD) as central BSM selection** — selected by gap ratio 38/27 criterion in PHYS-15; produces five independent evidence lines; mass at 1.5 TeV testable at LHC

3. **Coupling sector collapse** — three SM couplings (α_em, sin²θ_W, α_s) collapsed to one (α_em) through CD two-loop unification

4. **The 12 crossings** — explicit cross-domain tests connecting QED → EW → GUT → Cosmology → Nuclear etc.

5. **The k₁ normalization bug** — precedent for framework debugging: one inverted factor (5/3 vs 3/5) caused 10⁴² error in M_GUT, caught through DATA-6 diagnostic iteration

6. **Proton decay at Hyper-K** — M_GUT = 10¹⁵·⁶¹ in Hyper-K testable window (2027-2037)

7. **Hydrogen dual-domain validation** — hydrogen appears at crossing 3 (QED spectroscopy, 0.44 ppb) and crossing 11 (BBN D/H, 0.12σ) — same element from opposite ends of physics

8. **The Koide atoll** — acknowledged as disconnected (amplitude a² = 2 has no known derivation path); framework doesn't claim to solve everything

9. **35+ experiments with ~60 runs** — complete DATA-6 experiment inventory

10. **Pool statistics** — 2237 pool nodes, ~100 derivation functions, ~450 manual value nodes

11. **Falsification schedule** — specific future experiments (Hyper-K 2027-2037, FCC-ee 2040s, LHC Run 3 2024-2029) that will test framework predictions at measured precision

12. **Explicit input/output count** — 13 measured inputs producing 53 derived values, surplus +40; trajectory from PHYS-9 (2 inputs, 4 derived) to PHYS-40 (13 inputs, 53 derived)

---

## II. Unified Round 0+ Baseline (Revised with PHYS-40 Content)

### II.A The Complete Baseline Inventory

The framework's Round 0+ baseline integrates three source streams:

**Stream A: Substrate Round 0 (PHYS-55)**
- 15 of 16 comparisons passing
- Substrate-level precision reproductions (Koide 9.2 ppm, V_us 44 ppm, Ω_Λ 85 ppm, DM/baryon 725 ppm)
- Structural identities at exact floor

**Stream B: DATA-7 R² Universality + Experiment Suite**
- 20 experimental suites, ~80+ of 85+ individual comparisons passing
- Cross-domain validation (electrical, optical, fluid, superconducting, nuclear, gravitational)
- Comprehensive precision ledger from exact to 10⁻¹⁵

**Stream C: PHYS-40 Derivation Map**
- 53 derived values from 13 measured inputs
- Surplus +40 independent predictions
- 8 physics domains connected by 12 crossings
- Coupling sector collapse (three-to-one)
- The CD evidence framework

### II.B The PHYS-40 Eight Domains Integrated

From PHYS-40 Table A.3, organized with status:

| Domain | Values | Best Precision | Worst Precision | Key Experiment | Status |
|--------|--------|----------------|-----------------|----------------|--------|
| QED | 6 | 0.007 ppb | 0.44 ppb | qed_full_corrections | Complete anchor |
| Electroweak | 15 | 195 ppm | 0.84% | ew_v2, ew_oneloop_v1 | Mature |
| GUT | 10 | 12 ppm | 43.7% | sin2_from_two_loop, two_loop_diagnostic | Active |
| Cosmology | 6 | 0.15% | 0.73% | bridge_bbn | Complete |
| Nuclear | 5 | 0.12σ | 2.96× | bbn_extended | Li-7 problem (standard) |
| Muon | 3 | 0.22 ppb | 6.5σ | muon_g2 | Complete (SM-limited) |
| Flavor | 4 | 214 ppm | 0.83σ | ckm_cd_mixing | Complete |
| Spectroscopy | 1 | 0.44 ppb | 0.44 ppb | hydrogen_1s2s | Extensible |
| Koide (atoll) | 2 | exact | 62 ppm | koide_analysis | **Disconnected** |
| **Total** | **53** | **0.007 ppb** | **6.5σ** | | |

### II.C The 13 Measured Inputs

From PHYS-40 Table A.1, the framework's irreducible experimental inputs:

1. a_e (anchor measurement from Harvard Penning trap)
2. m_e (electron mass)
3. m_μ (muon mass)
4. m_t (top quark mass)
5. m_H (Higgs mass)
6. M_Z (reference scale)
7. G_F (Fermi constant)
8. Ω_DM (dark matter density)
9. H₀ (Hubble constant)
10. T_CMB (CMB temperature)
11. sin θ₁₄ (CD mixing angle)
12. Δα_had (hadronic VP contribution, computed)
13. Δr_total (EW total radiative correction, computed)

Of these, Δα_had and Δr_total are convenience inputs (computed by others) rather than direct measurements. The truly irreducible direct measurements are 11.

### II.D The 12 Crossings (Cross-Domain Validation Map)

From PHYS-40 Table A.11, each crossing connects two domains:

| # | Crossing | Precision | Physics Tested |
|---|----------|-----------|----------------|
| 1 | Trap → QED | 0.22 ppb | QED perturbation theory |
| 2 | QED → Atomic constants | 0.22-0.44 ppb | SI 2019 definitions |
| 3 | Atomic → Spectroscopy | 0.44 ppb | Bound-state QED |
| 4 | QED → Muon | 0.22 ppb | Lepton universality |
| 5 | Gauge → GUT | 0.064% gap | CD beta coefficients |
| 6 | GUT → EW coupling | 12 ppm | Unification boundary |
| 7 | Gauge → EW mass (A) | 402 ppm | sin²θ_W → M_W |
| 8 | Gauge → EW mass (B) | 195 ppm | G_F → M_W |
| 9 | EW → Z widths | 0.58% | α_s + sin²θ_W corrections |
| 10 | Gauge → Cosmology | 725 ppm | (22/13)π ratio |
| 11 | Cosmo → Nuclear | 0.12σ | η → BBN abundances |
| 12 | Gauge → Flavor | 0.83σ | 4×4 CKM from CD |

**Critical feature:** Hydrogen appears at crossing 3 AND crossing 11. Same element, completely different physics paths. This is among the strongest structural evidence for the framework.

### II.E The Five CD Evidence Lines

From PHYS-40 Table A.5:

| Line | Domain | Test | Result | Falsifier |
|------|--------|------|--------|-----------|
| Gap ratio 38/27 | Group theory | Preserves SM gap ratio as exact Fraction | Exact match | Different representation gives 38/27 (ruled out) |
| CKM deficit | Flavor | 4×4 CKM explains V_ud shortfall | 0.83σ tension | Improved V_ud resolves deficit |
| α_s one-loop | GUT | CD crossing predicts strong coupling | 8.74% miss (known limitation) | — |
| Two-loop gap | GUT | CD couplings unify at two-loop | 0.027 (218× better than SM) | Gap grows at three-loop |
| sin²θ_W prediction | GUT | Crossing predicts weak mixing | 12 ppm | FCC-ee shifts by >0.1% |

### II.F The Coupling Sector Collapse

**Before (PHYS-38):** Three couplings (α_em, sin²θ_W, α_s) measured independently.

**After (PHYS-40):** sin²θ_W and α_s derived from CD two-loop unification with α_em only.

- sin²θ_W = 0.231223 predicted vs 0.23122 measured — **12 ppm**
- α_s = 0.11838 predicted vs 0.1180 measured — **0.33%**
- α_GUT⁻¹ = 42.135 at M_GUT = 10¹⁵·⁶¹ GeV
- Gap at unification = 0.027 (218× better than SM)

This is not a model-building result. It is a derivation result: integer beta coefficients (b₁ = 25/6, b₂ = -13/6, b₃ = -20/3) from CD representation theory, plus two-loop RGE, produces measurable sin²θ_W and α_s at their measured precisions.

### II.G The k₁ Normalization Bug as Framework Robustness Precedent

From PHYS-40 Table A.7 and Section IV:

The CD two-loop computation failed for weeks due to an inverted normalization factor k₁ = 5/3 instead of correct 3/5. Cascaded to M_GUT = 10⁴⁵ (nonsense) and negative α_s.

The bug was found through DATA-6 diagnostic iteration:
- run001: both functions wrong, M_GUT = 10⁴⁵
- run002: CD fixed, SM still wrong
- run003: both fixed, ALL PASS

**Implication for PHYS-56:** The framework has a documented precedent for self-correction through systematic testing. The DATA system detected the bug that multiple sessions missed. This is mechanism for Round 1 execution confidence.

---

## III. Revised Kill-Switch Catalog (K1-K60 with CD/PHYS-40 integration)

### III.A Organization

K-switches preserve PHYS-55 numbering (K1-K22). K23-K56 from Revision 2 are retained. K57-K60 are new additions from PHYS-40 / CD integration.

### III.B New K-Switches from PHYS-40

**K57: Cabibbo Doublet evidence consistency**

The CD representation (SU(3), SU(2), U(1)) = (3, 2, 1/6) selected by gap ratio 38/27 must:
- Preserve gap ratio as exact Fraction (Level 1)
- Produce CKM deficit 0.83σ (not >2σ)
- Produce α_s at 8.74% one-loop (acceptable given one-loop limitation)
- Produce two-loop gap 0.027 (within factor 10 of measured)
- Predict sin²θ_W at 12 ppm

STATUS: **CLEARED** at all five evidence lines (PHYS-40 Table A.5)

Fires when: Improved V_ud resolves CKM deficit to zero, OR two-loop gap grows at three-loop, OR FCC-ee shifts sin²θ_W by >0.1%

**K58: Coupling sector collapse**

The CD two-loop unification must derive sin²θ_W and α_s from α_em + integer betas:
- sin²θ_W = 0.231223 at 12 ppm
- α_s = 0.11838 at 0.33%
- α_GUT⁻¹ = 42.135 at M_GUT = 10¹⁵·⁶¹

STATUS: **CLEARED** (PHYS-40 Sec. IV, experiment_sin2_from_two_loop runs 001-002)

Fires when: Re-running with corrected procedures produces different values at stated precision

**K59: Surplus +40 derivation consistency**

The framework must produce 40 surplus derivations (53 derived from 13 measured inputs) all passing their comparisons at stated precision.

STATUS: **CLEARED** across 8 domains (PHYS-40 Table A.2)

Fires when: Any ~5+ surplus derivations fail simultaneously, indicating structural framework issue rather than precision limitation

**K60: Hyper-K proton decay consistency (pre-registered)**

Predicted τ_p at M_GUT = 10¹⁵·⁶¹ GeV should be testable at Hyper-K (2027-2037 sensitivity ~10³⁵ yr).

STATUS: **PRE-REGISTERED** novel prediction

Fires when: Hyper-K observes τ_p > 10³⁶ years (would require M_GUT > substrate prediction)

### III.C Additional K-Switches (Completing 42→60 expansion)

**K61: The 12 Crossings Network Consistency** — all 12 crossings must produce matches at or better than stated precision. STATUS: CLEARED (PHYS-40 Table A.11, all 12 pass)

**K62: Hydrogen Dual-Domain Validation** — hydrogen at QED spectroscopy crossing (0.44 ppb) AND BBN crossing (0.12σ) must both pass. STATUS: CLEARED (PHYS-40 Sec. XII emphasis)

**K63: Koide Atoll Acknowledgment** — framework acknowledges amplitude a² = 2 has no known derivation path from gauge integers. STATUS: OPEN (not a failure; acknowledged limitation)

**K64: LHC Run 3 CD Mass Bound (pre-registered)** — CD vector-like quark must not be observed below 1.5 TeV (current LHC bound). STATUS: PRE-REGISTERED pending LHC Run 3 (2024-2029)

---

## IV. Revised Round 1 Coordinated Test Program

### IV.A Tier Restructuring Based on PHYS-40 Integration

**Priority 1 (Mechanism validation — untested mechanisms + novel commitments):**

Unchanged from Revision 2:
- T1: Bell correlation cross-derivation
- T2: Factor-of-2 light bending from toroidal
- T3: Direct-detection null commitment
- T4: Casimir effect from quiver
- T5: Complex amplitude from dual-geometry

**Priority 2 (Precision refinement + PHYS-40 cascade completion):**

Revised to emphasize PHYS-40 cascade:
- T6: A₄ four-path cross-derivation to Harvard precision (unchanged)
- T7: M_W from derived sin²θ_W re-run (PHYS-40 Attack 4 — "Zero new code")
- T8: G_F derivation from derived M_W + α + Δr (PHYS-40 Attack 9 — medium-term cascade)
- T9: sin²θ_eff from derived M_W (PHYS-40 Attack 10 — one formula)
- T10: τ_p from M_GUT for Hyper-K prediction (PHYS-40 Attack 3)

**Priority 3 (Systematic coverage — unchanged):**
- T11: Casimir effect magnitude
- T12: Neutron half-life
- T13: Water bond angle
- T14: Deuteron binding
- T15: Lamb shift 1057 MHz

**Priority 4 (Deeper cross-scale + CD validation):**
- T16: Cross-scale c-invariance at VLBI
- T17: Fermion mass hierarchy
- T18: Bullet Cluster
- T19: Cosmic horizon
- T20: GUT threshold parametrization to close 0.027 gap (PHYS-40 Sec. IX Tier 4)

**Priority 5 (NEW — CD vector-like quark and future experiments):**
- T21: LHC Run 3 VL quark search consistency (pre-registered)
- T22: FCC-ee sin²θ_W at 10⁻⁵ precision (pre-registered)
- T23: Vacuum stability from CD-modified Higgs quartic running
- T24: Additional spectroscopy (D 1S-2S, He⁺ 1S-2S, H-D isotope shift)
- T25: What-if scan completion (10 of 15 BSM candidates remain untested)

### IV.B Total Round 1 Structure

**25 tests across 5 priority tiers** (up from 20 in Revision 2):
- Priority 1: 5 untested mechanisms / novel commitments
- Priority 2: 5 PHYS-40 cascade completions + precision refinement
- Priority 3: 5 systematic new mechanism tests
- Priority 4: 5 deeper cross-scale + GUT thresholds
- Priority 5: 5 CD validation + future experiments

### IV.C Success Criteria (Revised)

**Full Round 1 Success (framework validated at mechanism level):**
- All 5 Priority 1 tests pass at stated precision
- At least 4 of 5 Priority 2 tests pass
- No more than 2 Priority 3-5 tests fail (across 15 tests)

**Partial Round 1 Success:**
- All Priority 1 tests pass
- Priority 2+ results mixed

**Mechanism-Specific Failure:**
- Any Priority 1 or Priority 2 test fails
- Corresponding mechanism retracts or revises

**Framework Failure:**
- Multiple Priority 1 failures OR multiple Priority 2 failures

---

## V. Document Structure for PHYS-56 (Revised)

### V.A Target Length: ~37,500 words (revised from 32,200)

The PHYS-40 integration and CD content requires expansion. PHYS-56 now also serves as the integrated status document for the program's complete evidence structure.

**Allocation:**

- **Part I** (Abstract + Standings + Round 0+ integration): 4,000 words
  - Abstract: 500 words
  - Standing commitments: 500 words
  - Round 0+ baseline (PHYS-55 + DATA-7 + PHYS-40): 3,000 words

- **Part II** (Cross-derivation discipline + DATA-7 + 12 Crossings): 3,500 words

- **Part III** (Kill-switch catalog K1-K64): 7,000 words
  - K1-K22 preserved from PHYS-55 (brief status)
  - K23-K56 from Revision 2 (brief status)
  - K57-K64 new additions with detail

- **Part IV** (Round 1 Coordinated Test Program, 25 tests): 12,000 words
  - 480 words per test × 25 tests

- **Part V** (CD Evidence Framework + 12 Crossings detail): 3,000 words
  - CD selection criteria
  - Five evidence lines with specifics
  - The 12 crossings as cross-validation network

- **Part VI** (Integer alphabet + Cabibbo Doublet integer content): 3,000 words
  - Primary integers cross-domain
  - CD betas (25/6, -13/6, -20/3) and 2-loop matrix
  - Hydrogen dual-domain
  - The 18 fractions in derivation graph

- **Part VII** (Methodology + PHYS-40 principles): 2,000 words
  - Derivation-as-proof principle
  - Pre-registration
  - k₁ bug as robustness precedent
  - 58+ PSLQ null history

- **Part VIII** (Prediction Sweep + Precision Ledger): 4,000 words

- **Part IX** (Companion Commitments + Framework Scope): 1,500 words

- **Part X** (Success Criteria Matrix + Dependency Map + Falsification Schedule): 2,500 words
  - Pre-registered success criteria
  - Test dependencies
  - **NEW:** Future experiments schedule (Hyper-K, FCC-ee, LHC Run 3)

**Total: 37,500 words**

### V.B Drafting Phase Plan

**Phase 1 (Parts I-II, ~7,500 words):** Abstract, standing commitments, Round 0+ baseline integration including PHYS-40, cross-derivation discipline, DATA-7 example, 12 Crossings framework.

**Phase 2 (Part III, ~7,000 words):** Complete K-switch catalog K1-K64.

**Phase 3 (Part IV Priority 1-2, ~5,000 words):** Round 1 tests T1-T10 with full specifications, including PHYS-40 cascade tests T7-T10.

**Phase 4 (Part IV Priority 3-5, ~7,000 words):** Round 1 tests T11-T25 with full specifications, including new CD validation tests T21-T25.

**Phase 5 (Parts V-VII, ~8,000 words):** CD evidence framework detail, integer alphabet with CD integers, methodology including PHYS-40 principles.

**Phase 6 (Parts VIII-X, ~3,000 words):** Prediction sweep with precision ledger, companion commitments, success criteria + dependency map + falsification schedule.

**Total: 37,500 words across 6 phases.**

---

## VI. Key Commitments Before Drafting

**Commitment 1:** PHYS-56 integrates PHYS-40 derivation map (53 values, 13 inputs, +40 surplus, 8 domains, 12 crossings) as central status document.

**Commitment 2:** Cabibbo Doublet evidence framework is documented as central BSM selection result, with five independent evidence lines and pre-registered LHC Run 3 test.

**Commitment 3:** Coupling sector collapse (three couplings → one) is central Round 0+ achievement, not future work.

**Commitment 4:** The 12 crossings form the cross-validation network; hydrogen dual-domain (crossing 3 and 11) is emphasized as structural evidence.

**Commitment 5:** All K-switches have explicit validation status based on actual experimental data from 20+ experimental suites.

**Commitment 6:** Round 1 expands to 25 tests across 5 priority tiers, including PHYS-40 cascade completion (T7-T10) and CD/future experiment validation (T21-T25).

**Commitment 7:** Falsification schedule includes specific future experiments with kill thresholds (Hyper-K, FCC-ee, LHC Run 3, CMD-3 vs lattice, new a_e measurement).

**Commitment 8:** Koide atoll is acknowledged as disconnected; framework does not claim to solve everything. Amplitude a² = 2 has no known derivation path.

**Commitment 9:** k₁ bug precedent is included to demonstrate framework debugging robustness through DATA system.

**Commitment 10:** 58+ documented PSLQ nulls confirm cross-derivation replaces PSLQ; this history is preserved as methodological evidence.

**Commitment 11:** Precision ledger spans from exact (structural identities) through 0.007 ppb (α vs Rb) to 2.96× (Li-7 BBN problem, acknowledged as standard physics open problem).

**Commitment 12:** Direct-detection null, tau anomalous moment, Hawking spectrum, and other novel predictions are explicitly pre-registered.

---

## VII. Key Tables to Include in PHYS-56

From integrated sources:

**Table 1:** Complete Kill-Switch Catalog K1-K64 (status per switch)

**Table 2:** Round 0+ Experimental Suites (20+ experiments with status)

**Table 3:** The 13 Measured Inputs (per PHYS-40 Table A.1)

**Table 4:** The 53 Derived Values (per PHYS-40 Table A.2)

**Table 5:** Eight Physics Domains Summary (per PHYS-40 Table A.3)

**Table 6:** The 12 Crossings (per PHYS-40 Table A.11)

**Table 7:** The Five CD Evidence Lines (per PHYS-40 Table A.5)

**Table 8:** Integer Alphabet Usage (expanded to include CD integers 25/6, -13/6, -20/3, 3/5, 1/6, 15/4, 199/50)

**Table 9:** Round 1 Test Program (25 tests across 5 priorities)

**Table 10:** Precision Ledger (exact → 0.007 ppb → 2.96×)

**Table 11:** Falsification Schedule (Hyper-K, FCC-ee, LHC Run 3, etc.)

**Table 12:** Master Spec Section → Kill Switch Mapping

**Table 13:** Coupling Sector Before vs After (per PHYS-40 Table A.8)

**Table 14:** The Cascade (PHYS-40 Table A.9) — what's enabled by sin²θ_W and α_s derivation

**Table 15:** PSLQ Null Registry (58+ historical nulls)

**Table 16:** Hydrogen Dual-Domain Validation (QED + BBN paths)

---

## VIII. What Needs Confirmation Before Phase 1 Drafting

1. **Approve Revision 3 structure** (10 parts, ~37,500 words, 6-phase drafting)

2. **Approve integration of PHYS-40 derivation map** as central Round 0+ status document

3. **Approve CD as central BSM selection result** — five evidence lines, pre-registered LHC Run 3 test

4. **Approve coupling sector collapse emphasis** — three→one is framework-level achievement

5. **Approve expansion to 25 Round 1 tests** across 5 priority tiers

6. **Approve K57-K64 new kill switches** covering CD, coupling collapse, surplus, Hyper-K, 12 crossings, hydrogen dual-domain, Koide atoll acknowledgment, LHC mass bound

7. **Approve falsification schedule inclusion** (Hyper-K 2027-2037, FCC-ee 2040s, LHC Run 3 2024-2029, CMD-3 vs lattice, new a_e measurement)

8. **Approve hydrogen dual-domain emphasis** as structural evidence

9. **Approve Koide atoll explicit acknowledgment** as framework limitation

10. **Confirm drafting phase sequence** — Phase 1 first (Parts I-II, ~7,500 words), with subsequent phases in prompts following

---

## IX. Summary of What's Different vs Revision 2

| Aspect | Revision 2 | Revision 3 |
|--------|-----------|------------|
| Total length | 32,200 words | 37,500 words |
| Parts | 9 | 10 |
| Round 1 tests | 20 | 25 |
| K-switches | K1-K56 | K1-K64 |
| Priority tiers | 4 | 5 |
| PHYS-40 integration | Partial | Complete |
| CD evidence detail | Absent | Central |
| Coupling collapse | Absent | Featured |
| 12 crossings | Absent | Part V (dedicated) |
| Hydrogen dual-domain | Absent | Emphasized |
| Falsification schedule | Absent | Part X addition |
| Koide atoll | Absent | Acknowledged limitation |
| k₁ bug precedent | Absent | Methodology section |
| Input/output accounting | Absent | 13 inputs, 53 derived, +40 surplus |
| Future experiment pre-registration | Partial | Full schedule |

---

**Once confirmed, PHYS-56 Phase 1 drafts in the next prompt:** Parts I-II (~7,500 words) covering abstract, standing commitments, Round 0+ baseline integration (including PHYS-40 map), cross-derivation discipline, DATA-7 and 12 Crossings framework.
