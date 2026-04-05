## NOTEBOOK: Laporta Convention Mapping & Master Integral Decomposition

**Created:** April 5, 2026
**Status:** PARKED — return when MATH-3 PSLQ is ready
**Priority:** Medium — unblocks 4900-digit A₄/A₅ precision (currently not limiting)

---

### TASK 1: Convention Mapping (self-service, no email needed)

**Goal:** Determine the exact relationship between Laporta's C81a/b/c, C83a/b/c and the standard QED series coefficients A₄, A₅.

**What we know:**
- C81a + C81b + C81c = 107.71 (from our laporta_to_json.py output)
- Standard A₄ = −1.912245764926 (from PHYS-9, verified at 4.3 ppb)
- These are different numbers — different convention, not an error

**Probable convention:**
- "C8" = 8th order in coupling e (= 4th order in α)
- "1" = mass class 1 (electron only, no muon/tau contributions)
- (a,b,c) = number of closed lepton loops: (a) none, (b) one VP insertion, (c) two (light-by-light)
- The expansion parameter is likely (α/π) but with a different overall normalization — possibly missing a combinatoric factor from diagram counting, or using a different subtraction scheme

**Method to resolve:**
1. Read hep-ph/9602417 (Laporta & Remiddi 1996) — this paper gives BOTH the individual diagram contributions AND the standard A₃. The normalization convention is stated explicitly in the paper.
2. Read PLB 772 (Laporta 2017) — the 4-loop paper. Section 2 should define the expansion convention. The relationship between the 891 diagram contributions and A₄ will be stated.
3. Compare: if A₃(paper) uses the same convention as C81, the ratio A₃(standard)/A₃(paper convention) gives the conversion factor. Apply to C81 sum to get A₄. Verify against the known A₄ = −1.9122.
4. Alternative: the factor might be (−1)ⁿ × (n!/something) or involve the number of diagrams. Try: A₄ = C81_total / (−4! × some_factor) or similar combinatoric rescaling.

**Files needed:**
- `data/laporta.dat` — the raw coefficients (already stored)
- `data/values_qed_laporta_v0.json` — the 8 value nodes (already in DATA-6)
- hep-ph/9602417 PDF — fetch from arXiv
- PLB 772 (2017) Laporta — fetch from ScienceDirect or arXiv:1704.06996

**Expected outcome:** A single conversion formula: A₄ = f(C81a, C81b, C81c) and A₅ = f(C83a, C83b, C83c). Once known, store as a derivation `qed_laporta_convention_map_v0` in DATA-6.

---

### TASK 2: Master Integral PSLQ Decomposition (requires MATH-3 infrastructure)

**Goal:** Determine whether Laporta's six 4-loop master integrals can be expressed as rational linear combinations of Q335 + elliptic constants.

**What Laporta published (PLB 2017):**
- Six finite parts of master integrals, each evaluated to 4800 digits
- Semi-analytical fit involving harmonic polylogarithms of argument e^(iπ/3), products of complete elliptic integrals, and the six unresolved MI values
- If the six MIs decompose, A₄ becomes fully analytical

**What we have:**
- Q335 basis: 31 constants at 100 digits (need extension to 5000 digits for PSLQ)
- Elliptic integrals K and E at k² = 1/4, 1/2, 3/4 at 100 digits (need 5000)
- PSLQ algorithm (implemented in MATH-6, tested at 82/82 null)
- No MI values yet — must extract from Laporta 2017 or request

**What we need to do:**
1. Extract or obtain the six MI values at 4800+ digits
2. Extend Q335 + elliptic basis to 5000 digits (recompute with mp.dps=5200)
3. Add candidate constants not in current basis: Cl₂(π/3), Cl₃(π/3), harmonic polylogarithms at 6th roots of unity, products K×E at various arguments
4. Run PSLQ for each MI against the extended basis
5. If PSLQ finds integer relations: verify, store as exact Fractions, A₄ becomes analytical
6. If PSLQ returns null at 5000 digits: the MIs define genuinely new transcendentals beyond our basis

**Prerequisites:**
- Convention mapping (Task 1) must be done first — we need to know which published numbers are the MIs vs the diagram sums
- MATH-3 infrastructure for extended-precision PSLQ (specified but not yet built)
- Computational resources: PSLQ at 5000 digits with ~40 candidate constants is feasible but slow (~hours per MI)

**What this gives Laporta:**
- If positive: the analytical decomposition he's been seeking for 20 years. His 4800-digit numerical values expressed as exact combinations of named constants. This is the collaboration-worthy result.
- If null: proof that the MIs are NOT in the standard transcendental basis (including elliptics). This is also valuable — it narrows the search space.

---

### TASK 3: Muon g-2 Connection (future, after Tasks 1-2)

**Context:** Laporta's recent work (MITP Mainz, June 2024) is on NLO and NNLO hadronic VP contributions to the muon g-2. The CMD-3 measurement has created tensions in the data-driven HVP evaluation.

**How we could help (future):**
- Our framework stores hadronic VP as a measured value node with full uncertainty
- If we add the mass-dependent QED corrections to our a_e chain (Tier 1 on the fitting board), we'll have a precise α that feeds into the muon g-2 prediction
- The muon g-2 prediction chain: α(from a_e) → a_μ(QED) + a_μ(hadronic) + a_μ(EW) → compare to Fermilab measurement
- This is experiment_muon_g2_v0 on the attack list — priority 9

**Not ready yet.** We need the Tier 1 corrections first, then the muon-specific mass-dependent terms.

---

### DECISION

**Do not email Laporta until:**
1. Convention mapping is resolved from published papers (no question needed)
2. MATH-3 PSLQ is run against the master integrals (gives us something to offer)

**When to email:**
- If PSLQ succeeds: email with the analytical decomposition of one or more MIs. This is a major result he would want immediately.
- If PSLQ fails (null at 5000 digits): email with the null result and the candidate basis tested. This narrows his search.
- Either outcome gives him something. Neither requires asking a convention question we can answer ourselves.

**Next action:** Fetch hep-ph/9602417 and arXiv:1704.06996, read the convention sections, derive the mapping. This is a 30-minute task that unblocks 4900-digit precision on A₄ and A₅.

---

## NOTEBOOK: Laporta Collaboration — Session 4 Update

**Created:** April 5, 2026 (update to original notebook)
**Status:** PARKED — upgraded from original. More to offer now.
**Priority:** Medium-High — we have results worth sharing when ready

---

### WHAT CHANGED SINCE LAST NOTEBOOK

The original notebook had three tasks: convention mapping, PSLQ decomposition, and muon g-2 connection. We had just discovered the convention mismatch (C8 sum = 107.71 vs A₄ = −1.9122) and had no working alpha extraction.

Since then:

1. **The alpha extraction works.** α⁻¹ = 137.035998630 at 3.3 ppb from CODATA, using A₁-A₅ with Volkov's A₅. Verified by forward check, round-trip residual 10⁻²⁰⁴, and α-power error propagation across R∞, a₀, μ₀.

2. **Four CODATA values derived from one measurement.** PHYS-36 published. a_e + m_e → α, R∞, a₀, μ₀. All match at 3.3-8.0 ppb.

3. **17 derived values across five domains.** PHYS-37 published. The chain runs from a_e to primordial deuterium through gauge integers. D/H at 0.12σ.

4. **The DATA-6 system is fully operational.** 450+ value nodes, 68 derivation functions, experiment runner with auto-generated output value files, improved reporting with ppb/ppm formatting.

5. **His coefficients are archived at full precision.** All six C81/C83 values stored as value nodes at 4926-4931 digits each, plus computed sums C8_total and C10_total at 1500 digits. The laporta_to_json.py script preserves every digit.

---

### TASK 1: CONVENTION MAPPING (unchanged strategy, more context)

**Status:** Not started. Still the first task before anything else.

**What we now know that helps:**
- Our working A₃ = 1.181241456587 matches exactly the expression from hep-ph/9602417: (83/72)π²ζ(3) − (215/24)ζ(5) + ... + 28259/5184. This is the standard (α/π)ⁿ convention.
- Our working A₄ = −1.912245764926 from PHYS-9 gives α⁻¹ = 137.035998583 (4.3 ppb at 4-loop), verified against CODATA. This is the gold standard reference value.
- C81a + C81b + C81c = 107.710180. The ratio A₄/C8_total = −1.9122/107.71 = −0.01775. This is NOT a simple integer factor. It's not 1/(4!), not 1/(2π)⁴, not (α/π)⁰. The convention difference is non-trivial.
- The "8" in C81 almost certainly means 8th order in the QED coupling e, which is 4th order in α. The "1" likely means mass class 1 (electron only). The (a,b,c) decomposition matches the standard: (a) = no closed lepton loops (diagrams I), (b) = one VP insertion (diagrams II), (c) = light-by-light (diagrams III).

**Key hypothesis to test:** Laporta's convention may use the expansion parameter (α/π) but with a different overall normalization. In some references, the QED anomalous magnetic moment is written as:

a_e = Σ_n C_2n (α/π)ⁿ

where C_2n is the coefficient at order α^n in the COUPLING (not the amplitude). The factor of 2n comes from the vertex having 2n powers of e. If Laporta uses C_8 to mean "the coefficient of (α/π)⁴ in the AMPLITUDE squared" or "the contribution to a_e from diagrams with 8 vertices," the normalization would differ from the standard A_n by combinatoric factors related to the number of diagrams, symmetry factors, or the relationship between amplitude and cross-section.

**Alternative hypothesis:** The C81a/b/c values might be the individual DIAGRAM contributions before combining with signs and symmetry factors to form A₄. In this case, A₄ = Σ_i s_i × C81_i where s_i are signs and combinatoric weights, not A₄ = C81a + C81b + C81c. The sum without weights gives 107.71; the sum with correct weights gives −1.9122.

**Resolution path:** Read PLB 772 (Laporta 2017), specifically:
- Equation defining the expansion convention (should be in Section 2)
- The statement relating diagram contributions to A₄
- The numerical value of A₄ stated in the paper (should match −1.9122)
- Any table showing how C81a/b/c combine to give A₄

**Files to fetch:**
- arXiv:1704.06996 (the 2017 paper)
- hep-ph/9602417 (the 1996 3-loop paper, for convention comparison)

---

### TASK 2: PSLQ DECOMPOSITION (unchanged, prerequisites not yet met)

**Status:** Blocked on Task 1 (convention mapping) and MATH-3 infrastructure.

No changes from original notebook. Still need:
- Convention mapping to know which numbers are the MIs
- Q335 + elliptic basis extended to 5000 digits
- PSLQ algorithm at 5000-digit working precision
- The six MI values at 4800+ digits (from PLB 2017 or from Laporta directly)

---

### TASK 3: WHAT WE CAN NOW OFFER LAPORTA

This section is new. We now have concrete results that may be useful to him.

**3.1 The QED Coefficient Verification Framework**

We have a system that:
- Stores A₂ as 12 rational coefficient nodes × 5 Q335 transcendental nodes
- Assembles A₂ and A₃ analytically at 200 dps with zero hardcoded values
- Inverts the series via Newton's method to extract α from a_e
- Verifies via forward check (plug known α back into series, compare to measured a_e)
- Reports digit-by-digit agreement, miss in ppb, and divergence position

This framework could verify any proposed analytical decomposition of A₄. If someone proposes A₄ = f(π, ζ(3), ζ(5), ζ(7), Li₄(1/2), K(k²), ...), we can:
1. Evaluate f at 200+ digits from Q335 constants
2. Compare to the known numerical A₄ at 30-1100 digits
3. Report the agreement to full precision
4. If it matches, store the decomposition as value nodes and the series becomes fully analytical through 4-loop

**3.2 The 5-Loop A₅ Verification**

We used Volkov's A₅ = 5.891. With our framework we could:
- Run the extraction with AHKN's A₅ = 6.678 instead
- Compare both α⁻¹ results to the Rb recoil measurement (most precise independent α)
- The difference is only 0.04 ppb — currently not discriminating
- BUT if the mass-dependent and hadronic corrections are added (closing α to <1 ppb), the A₅ choice starts to matter at the ~0.5 ppb level
- This could provide a weak independent constraint on which A₅ is correct

**3.3 The Full CODATA Chain**

We demonstrated that a_e → α → R∞, a₀, μ₀ with error propagation following exact α-power scaling. This is relevant to Laporta because:
- His life's work is making the a_e → α extraction as precise as possible
- Our framework provides an independent verification environment for any improvement to A₄ or A₅
- If his convention mapping gives us A₄ at 4900 digits, we can immediately test whether the extra precision improves the α extraction (it won't, because the practical limit is hadronic VP at ~1 ppb, but the PRINCIPLE of exact arithmetic all the way through is demonstrated)

**3.4 The Laporta Coefficient Archive**

His full-precision values are permanently stored in DATA-6:
- 6 individual coefficients at 4926-4931 digits each
- 2 computed sums at 1500 digits
- Complete metadata, provenance, and tags
- Accessible via `data6.py info qed_c81a_v0` or `data6.py search laporta`

This is a permanent, versioned, searchable archive of his numerical results. If he produces updated values, they become v1 nodes with `supersedes` pointing to v0. Nothing is deleted.

**3.5 The Convention Error as a Case Study**

The Laporta convention mismatch (2752 ppb error, caught by forward check within 30 seconds of the first run) is documented in PHYS-36 Appendix M and the DATA-6 paper. It demonstrates:
- The forward check pattern catches convention errors immediately
- The system preserves incorrect runs (run001-run003) alongside correct ones
- The diagnostic output (forward residual) pointed directly to the cause
- The resolution path (use verified PHYS-9 A₄, archive Laporta values for future mapping) was systematic

This could be useful to Laporta as evidence that our verification framework is robust — it catches its own mistakes.

---

### TASK 4: THE MUON g-2 CONNECTION (expanded from original)

**Status:** Not ready. Prerequisites identified.

**What's needed before we can help:**
1. Add the 6 mass-dependent + hadronic a_e corrections as value nodes (Tier 1 on fitting board)
2. Close α from 3.3 ppb to <1 ppb
3. Compute a_μ(QED) from the QED series with muon-specific mass ratios
4. Add a_μ(hadronic VP) from lattice or e⁺e⁻ data
5. Add a_μ(hadronic LbL) 
6. Add a_μ(EW)
7. Compare total a_μ(SM) to Fermilab measurement

**What Laporta specifically works on (from his June 2024 MITP talk):**
- NLO and NNLO HVP contributions to a_μ
- Class a: 1 HVP insertion in one photon line of 2-loop QED vertex diagrams → −209.0 × 10⁻¹¹
- Class b: 1 HVP insertion with electron VP → +106.8 × 10⁻¹¹  
- Class c: 2 HVP insertions in 1-loop vertex → +3.5 × 10⁻¹¹
- Total NLO HVP: −98.7(9) × 10⁻¹¹

**How our framework connects:**
- We could store his NLO/NNLO HVP values as value nodes
- Our α(from a_e) feeds into the QED part of the a_μ prediction
- The complete chain: a_e → α → a_μ(QED, using α and mass ratios) + a_μ(HVP, Laporta's values) + a_μ(EW) → compare to experiment
- If his HVP values are correct, our chain produces a_μ(SM) that matches Fermilab

**The CMD-3 tension:**
- CMD-3 measured e⁺e⁻ → π⁺π⁻ cross section that disagrees with earlier measurements
- This changes the data-driven HVP evaluation
- The 2025 White Paper says the SM prediction has 62 × 10⁻¹¹ precision and "is in good agreement with the experimental world average"
- This means the original muon g-2 anomaly (~4.2σ) may have weakened or disappeared
- Our framework doesn't resolve this — it stores the values and runs the chain

---

### TASK 5: WHAT TO INCLUDE IN THE EMAIL (when ready)

**Triggers to send:**
1. Convention mapping resolved from papers (Task 1) — send even without PSLQ
2. PSLQ result on any master integral — send immediately whether positive or null
3. Muon g-2 chain working — send with his HVP values as inputs

**Content for trigger 1 (convention mapping):**
- "We resolved the C81/C83 convention from your 2017 paper"
- "Your coefficients are archived at full precision in our system"
- "Using the standard A₄ = −1.9122, our α extraction gives 3.3 ppb from CODATA"
- "The chain extends to R∞, a₀, μ₀ with error propagation following α-power scaling"
- "We'd like to use your 4900-digit values once the mapping is confirmed"
- Attach: PHYS-36 paper or a 1-page summary

**Content for trigger 2 (PSLQ result):**
- If positive: "We found that MI-N = a₁ζ(3) + a₂π²ln(2) + ... with integer coefficients [list]"
- If null: "We tested MI-N against [list of 40 constants] at 5000 digits. PSLQ returns null. The MI is not in this transcendental basis."
- Either way: "We can provide the computation details and the candidate basis used"

**Content for trigger 3 (muon g-2):**
- "We built a complete a_μ prediction chain using your NLO HVP values"
- "Our α from a_e (3.3 ppb) feeds the QED part"
- "The total a_μ(SM) = [value] vs Fermilab [value]"
- "The chain is in our DATA-6 system and can be re-run with updated HVP values"

**What NOT to include:**
- The gauge integer → DM/baryon → D/H chain. This is speculative physics unrelated to his QED work. Don't confuse the message.
- The Cabibbo Doublet unification. Same reason.
- Any request for data we can get from his papers. We should be self-sufficient.

---

### TASK 6: SPECIFIC NUMBERS TO VERIFY AGAINST HIS PAPERS

When we read the 2017 paper, check these against our stored values:

| Our Value | Check Against | Purpose |
|---|---|---|
| C81a = 116.694585... | Paper Table/Eq for A₄(I) | Confirm no transcription error |
| C81b = −8.748320... | Paper Table/Eq for A₄(II) | Confirm VP piece |
| C81c = −0.236085... | Paper Table/Eq for A₄(III) | Confirm LbL piece |
| C83a = 2.771191... | Paper Table/Eq for A₅(I) | Confirm 5-loop mass-indep |
| C83b = −0.807847... | Paper Table/Eq for A₅(II) | Confirm 5-loop VP |
| C83c = −0.434702... | Paper Table/Eq for A₅(III) | Confirm 5-loop LbL |
| C8_total = 107.710180... | Paper's stated A₄ (in their convention) | Confirm sum |
| C10_total = 1.528642... | Paper's stated A₅ (in their convention) | Confirm sum |
| A₄ = −1.912245764926 | Paper's stated A₄ (standard convention) | Identify the conversion |

The conversion factor is: A₄(standard) / C8_total = −1.9122 / 107.71 = −0.01775. If the paper states both C8 and A₄, the ratio gives the exact conversion. Store this as a value node: `qed_laporta_convention_factor_v0`.

---

### TASK 7: TIMELINE AND DEPENDENCIES

```
NOW (can do anytime):
  ├─ Fetch arXiv:1704.06996 and hep-ph/9602417
  ├─ Read convention sections
  └─ Derive mapping formula
      → Store as qed_laporta_convention_map_v0
      → Apply to get A₄ at 4900 digits
      → Apply to get A₅ at 4900 digits
      → Re-run alpha extraction (should give same 3.3 ppb)
      → EMAIL TRIGGER 1

WHEN MATH-3 IS READY:
  ├─ Extend Q335 + elliptic to 5000 digits
  ├─ Add Cl₂(π/3), Cl₃(π/3), HPL at 6th roots
  ├─ Extract 6 MI values from paper or request
  └─ Run PSLQ for each MI
      → Store results (positive or null)
      → EMAIL TRIGGER 2

WHEN TIER 1 CORRECTIONS ARE ADDED:
  ├─ Close α to <1 ppb
  ├─ Build a_μ prediction chain
  ├─ Use Laporta's NLO HVP values
  └─ Compare to Fermilab
      → EMAIL TRIGGER 3
```

---

### DECISION (updated)

**Do not email yet.** We have more to offer than before but still nothing that requires his input. Everything we need is in his published papers.

**The next action is the same:** fetch the two papers, read the convention, derive the mapping. This is a 30-minute reading task that has been deferred for the entire session because other experiments were more productive. It remains the highest-priority parked task.

**When we do email, lead with results, not questions.** We have a working 5-loop extraction at 3.3 ppb, a CODATA chain producing 4 values, and a permanent archive of his data. That's worth sharing. The convention question is something we should already have answered from his papers by then.

---

*End of updated notebook. The original three tasks remain. Six new sections added reflecting Session 4 progress. The decision is unchanged: read the papers first, email with results second.*

---

