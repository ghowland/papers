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
