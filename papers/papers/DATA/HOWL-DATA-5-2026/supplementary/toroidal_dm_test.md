The script tests every quantitative claim in the notebook:

Naive v²/c² is too small (Section 2): confirmed, O(10⁻⁷) for galaxies
Virial theorem works for spirals (Section 4): confirmed, gives ratio ~5-6
Virial theorem fails for dwarfs (Section 10): confirmed, v²/c² ~ 10⁻⁹ vs DM ratio ~100
Frame dragging is negligible (Section 8): confirmed, O(10⁻¹³) relative to Newtonian
MOND a₀ ~ cH₀/(2π) = cH₀/(8R₂) (Section 6): tested, should be within factor 2
Amplification factor decomposes into beta integers (Section 7): the key finding — A = (44/13)π(c/v)², where 44/13 contains YM=11 and |b₂_mod|=13
Morphology predictions (Section 5): tabulated for thin/thick/elliptical/dwarf/cluster
R₂/R₄ geometry (Section 11): thin vs thick disk geometric ratios computed

The connection to beta unification is the strongest finding: the amplification factor contains 44/13, the same ratio that gives Ω_DM = 44/169 in the cosmic density chain. Run it.

---

**12 PASS, 0 FAIL. Toroidal DM experiment operational.**

The key result from Section 7 is striking: A_reduced = 44/13 to effectively infinite precision (miss = 1.69×10⁻⁹⁹%). That's not a numerical coincidence — it's algebraic. The amplification factor decomposes EXACTLY as:

A = (44/13) × π × (c/v)²

because the script defines DM/baryon = (22/13)π and then solves for A = DM_baryon × 2c²/v², which gives:

A = (22/13)π × 2c²/v² = (44/13) × π × (c/v)²

This is a tautology in the current form — it's the beta unification DM/baryon formula rewritten as an amplification factor. The script correctly identifies this by showing that 44/13 is the same ratio as Ω_DM = 44/169 = (44/13)/13. But the tautology is informative: it says IF the beta unification formula is correct, THEN the boundary amplification factor has this specific decomposition into gauge group integers times geometry times a velocity ratio.

The three honest findings:

**1. The virial theorem works for spirals but not for dwarfs.** Virial ratio for the Milky Way is 2.8 (expected ~6 — right order, factor 2 off due to simplified mass model). For dwarf spheroidals, v²/c² ~ 10⁻⁹ against DM/visible ~ 100. The virial approach fails by 11 orders of magnitude for dwarfs. This is the hardest challenge.

**2. MOND a₀ ≈ cH₀/(8R₂) within 15%.** The acceleration scale that governs dark matter phenomenology connects to the Hubble rate through R₂ = π/4. Whether this is coincidence or structure is an open question — but it uses the same R₂ that appears in 15+ domains documented in phys24_domain_lib.py.

**3. Frame dragging is negligible.** At O(10⁻¹³) relative to Newtonian gravity, GR frame dragging cannot be the dark matter mechanism. Whatever produces the apparent DM, it is not Lense-Thirring precession.

The dwarf spheroidal challenge (Section 10) is correctly identified as the strongest objection. The script does not hide it — it computes the required amplification (1.8×10¹¹) and shows it is 10⁴× larger than for galaxies. This is where the hypothesis is weakest.

---

## Notebook: Toroidal Dark Matter Test — Findings and Analysis

---

### 1. WHAT THIS SCRIPT DOES

The toroidal DM test investigates whether dark matter could be "boundary-amplified inertia of circulation within toroidal solitons" — in series language, whether the apparent missing mass in galaxies and clusters is the geometric contribution of vortex circulation to the gravitational field, amplified through soliton boundary effects.

The script runs 12 checks across 11 sections, testing this hypothesis against observational data. All 12 checks pass, but "PASS" here means the check ran and the condition was met — it does NOT mean the hypothesis is confirmed. Several checks explicitly confirm that the hypothesis FAILS in specific regimes (dwarf spheroidals).

---

### 2. THE CORE HYPOTHESIS IN SERIES LANGUAGE

By R4 (field = standing pattern = vortex), a galaxy is a vortex configuration. The stars orbit in a toroidal pattern (the disk), and the rotation carries energy. By R3 (mass = inertia), this circulating energy has inertia, and inertia gravitates.

The hypothesis: the "dark matter" that we infer from gravitational measurements is actually the inertial contribution of the galactic vortex's circulation — the energy in the pattern itself, not in the visible matter. The boundary amplification is analogous to the proton: 99% of the proton's mass is QCD binding energy (the pattern), only 1% is current quark masses (the "visible matter").

---

### 3. WHAT THE SCRIPT FINDS

**Section 2 — The naive kinetic energy is too small.**
v²/c² = 5.4×10⁻⁷ for galactic rotation at 220 km/s. To produce DM/baryon ≈ 5.3, you need an amplification factor of ~2×10⁷. The naive "rotation has inertia" argument fails by 7 orders of magnitude. This is honest and correct — it establishes that any toroidal explanation needs a mechanism beyond simple kinetic energy.

**Section 3 — Required amplification far exceeds proton analogy.**
The proton amplification (binding/quark mass) is ~99×. The galactic amplification needed is ~2×10⁷. The galaxy would need a boundary effect 200,000× stronger than the proton's. This is a serious problem for the analogy. The script states this clearly.

**Section 4 — Virial theorem works for spirals (roughly).**
The virial mass M_virial = Rv²/G gives ~1.7×10¹¹ solar masses for the Milky Way, against ~6×10¹⁰ visible. The ratio is 2.8, expected ~6.25 for 84% DM. Right order of magnitude, factor of 2 off from the simplified mass model. This is the strongest positive result — the virial approach naturally produces a "missing mass" from the kinetic energy budget without new physics.

**Section 5 — Morphology predictions and the dwarf problem.**
Spirals, ellipticals, and clusters all have v²/c² ~ 10⁻⁷ to 10⁻⁵ with DM fractions of 80-90%. Dwarf spheroidals have v²/c² ~ 10⁻⁹ but DM fractions of 99%. The virial approach fails for dwarfs by 11 orders of magnitude. The script identifies this as "the strongest challenge" — correctly.

**Section 6 — MOND a₀ connects to R₂.**
The MOND acceleration scale a₀ ≈ 1.2×10⁻¹⁰ m/s² is within 15% of cH₀/(2π) = cH₀/(8R₂). This connects the dark matter phenomenology to the Hubble expansion through R₂ = π/4 — the same geometric constant appearing in 22+ domains. Whether this is coincidence or structure is genuinely open. The R₂ rewriting (a₀ ≈ cH₀/(8R₂)) is a tautology (8R₂ = 2π), but it places the coincidence within the series' geometric framework.

**Section 7 — The beta unification connection.**
The amplification factor decomposes as A = (44/13) × π × (c/v)². The miss is 10⁻⁹⁹% — because this is algebraically exact. The script defines DM/baryon = (22/13)π and solves for A, so the decomposition is a tautology: A = (22/13)π × 2(c/v)² = (44/13)π(c/v)². The old-Claude analysis correctly identifies this as a tautology. The integers 44 and 13 come from the beta unification DM formula, not from any independent dark matter physics.

**Section 8 — Frame dragging is negligible.**
At 2×10⁻¹³ of Newtonian gravity, Lense-Thirring precession is not the mechanism. This rules out one specific GR effect as the amplification source.

**Section 11 — Geometric volume ratio.**
Thin disk torus volume / sphere volume ≈ 0.002, giving a geometric DM/visible ratio of ~530 for the thin disk. This overshoots the cosmic ratio of 5.3 by 100×. The thick disk (R/r = 15) gives ~48, closer to the right order. The pure geometry argument overshoots.

---

### 4. WHAT IS SOLID

Three findings are computationally verified and physically grounded:

**A. The virial theorem naturally produces "missing mass" for spirals and clusters.** This is textbook physics — not a new finding — but it confirms that the kinetic energy budget of a self-gravitating system contributes to the total gravitational field. The virial ratio of ~3 for the Milky Way (against expected ~6) is the right ballpark given the simplified mass model.

**B. Frame dragging is not the mechanism.** At 10⁻¹³, GR rotation effects are irrelevant. Whatever dark matter is, it is not frame dragging.

**C. MOND a₀ ≈ cH₀/(8R₂) within 15%.** This is an observed numerical coincidence documented by Milgrom and others. The R₂ framing is cosmetic (8R₂ = 2π) but places it in the series' geometric framework. The coincidence is real and unexplained.

---

### 5. WHAT IS A TAUTOLOGY

**The Section 7 "key finding."** The amplification factor A = (44/13)π(c/v)² is algebraically identical to the input DM/baryon = (22/13)π rewritten as an amplification over v²/c². The integers 44 and 13 come from the beta unification formula, not from independent dark matter observations. Old-Claude correctly identifies this. The decomposition is informative only IF the beta unification DM formula is independently validated — which it is not (Track B was PARKED by PHYS-31 with p = 0.81).

**The geometric ratio.** Comparing torus volume to sphere volume gives a "DM/visible" ratio, but this assumes visible matter fills a torus while DM fills a sphere. This is the standard halo model assumption restated in geometric language, not a derivation.

---

### 6. WHAT FAILS

**The dwarf spheroidal problem.** v²/c² ≈ 10⁻⁹ with DM/visible ≈ 100. The virial approach requires an amplification of 1.8×10¹¹ — 10,000× larger than for galaxies. The script offers four possible resolutions (tidal stripping, different soliton type, type-dependent amplification, actual particle DM) but does not resolve the problem. This is the honest state of the hypothesis.

**The boundary amplification has no derivation.** The proton analogy suggests boundary effects can amplify inertia (99× for the proton), but the galactic amplification of ~10⁷ is qualitatively different. No first-principles calculation produces this factor. The script states this clearly.

---

### 7. CONNECTION TO SESSION 4

**Track B status.** The DM/baryon = (22/13)π formula is Track B, which PHYS-31 parked with p = 0.81 (81% of random 15-integer pools score ≥6/8 on cosmological formula hits). The beta integers are not special for cosmological formulas. This does NOT mean the formula is wrong — it means the integers don't preferentially appear in cosmological contexts more than random integers do.

**The toroidal DM test inherits Track B's status.** The Section 7 finding depends entirely on DM/baryon = (22/13)π. If Track B is parked, the Section 7 finding is parked with it. The script does not acknowledge this explicitly.

**What survives Track B parking.** Sections 2-5 (naive kinetic energy, amplification requirements, virial theorem, morphology) are independent of Track B — they test the toroidal hypothesis against observations using standard physics. Section 6 (MOND a₀) is also independent. Section 7 (beta unification connection) depends on Track B.

---

### 8. WHAT DATA-5 SHOULD STORE

| Item | Type | Status | Storage |
|---|---|---|---|
| v²/c² at galactic scales | Observational parameter | Verified | Store as reference |
| Virial ratio for Milky Way (~2.8) | Computed from standard physics | Verified | Store as derived |
| MOND a₀ ≈ cH₀/(8R₂) ratio (~1.15) | Numerical coincidence | Observed | Store with "unexplained" tag |
| Frame dragging / Newtonian (~10⁻¹³) | Computed from GR | Verified | Store as derived |
| DM/baryon = (22/13)π | Track B formula | PARKED (p = 0.81) | Store with PARKED status |
| A = (44/13)π(c/v)² decomposition | Tautology from Track B | PARKED (depends on Track B) | Store with PARKED + TAUTOLOGY status |
| Dwarf spheroidal challenge | Falsification test | ACTIVE (hypothesis fails here) | Store as open challenge |

---

### 9. WHAT THE SCRIPT DOES WELL

The script is honest. It identifies the dwarf spheroidal problem as the strongest challenge. It computes the frame dragging and shows it is negligible. It shows the naive kinetic energy is too small. It correctly identifies the Section 7 decomposition as depending on the Track B formula. The 12/12 PASS checks are not claiming the hypothesis is confirmed — they are testing specific computational conditions and reporting results. The script's STATUS is "ACTIVE INVESTIGATION" not "CONFIRMED."

---

### 10. WHAT THE SCRIPT DOES NOT DO

The script does not derive the amplification factor from first principles. It does not explain why the virial approach works for spirals but fails for dwarfs. It does not compute circulation survival in the Bullet Cluster. It does not test the hypothesis against CMB power spectrum constraints. These are listed as open challenges.

The script also does not connect to the PHYS-35 no-threshold finding. The no-threshold result says the CD vortex's geometric overlaps persist at all scales — could this have implications for how gravitational effects of circulation persist across scales? The script does not explore this.

---

### 11. STATUS SUMMARY

| Test | Result | Implication |
|---|---|---|
| Naive v²/c² | Too small by 10⁷ | Amplification required |
| Virial (spirals) | Works, ratio ~3 | Standard physics explains most of spiral DM |
| Virial (dwarfs) | Fails by 10¹¹ | Hypothesis breaks here |
| Frame dragging | Negligible (10⁻¹³) | Not the mechanism |
| MOND a₀ ≈ cH₀/(8R₂) | Within 15% | Unexplained coincidence |
| Beta unification A = (44/13)π(c/v)² | Algebraic tautology | Depends on Track B (PARKED) |
| Geometric volume | Overshoots 100× (thin) | Pure geometry insufficient |

**Overall assessment:** The toroidal DM hypothesis is a framework, not a theory. It has one strong positive (virial works for spirals), one interesting coincidence (MOND a₀), one identified tautology (beta connection), and one major failure (dwarfs). The hypothesis is neither confirmed nor ruled out — it is constrained.

---

*End of notebook. The toroidal DM experiment is an active investigation with 12/12 computational checks passing. The strongest finding is the virial theorem's natural "missing mass" for spirals. The strongest challenge is dwarf spheroidals. The beta unification connection (Section 7) is a tautology that inherits Track B's PARKED status. DATA-5 should store the verified computations (virial, frame dragging, MOND coincidence) and tag the Track B-dependent results as PARKED.*

---

