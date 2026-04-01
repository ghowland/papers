# What the DATA-2 Values Open — Rigorous Assessment

## Method

I'm going through the 107 entries against every paper in the series, asking: does this value, at this precision, enable a computation or test that wasn't possible before? I'll separate what's genuinely new from what's redundant with prior work.

---

## Path 1: The Overconstrained Electroweak Extraction

**What DATA-2 provides:** G_F (8 digits), M_Z (6 digits), sin²θ_W (5 digits), α_s (4 digits), α⁻¹ (12 digits), m_t (5 digits), m_H (5 digits), M_W (6 digits), Γ_Z (5 digits), σ⁰_had (5 digits), R_l (5 digits), R_b (5 digits), A_FB^l (3 digits), A_l (4 digits), N_ν (5 digits).

**What the papers establish:** PHYS-5 computed α running in Fraction arithmetic. PHYS-6 computed Z partial widths, gauge coupling running, electron g-2, muon g-2 QED sector. The infrastructure exists for Fraction computation of electroweak observables.

**What's new:** The LEP observables (σ⁰_had, R_l, R_b, A_FB^l, A_l) are in the database for the first time as Fraction-ready values. The computation chain is:

The Z partial width for fermion f is Γ_f = (G_F M_Z³)/(6π√2) × (v_f² + a_f²) × N_c × (1 + δ_QCD). The vector coupling v_f = T₃_f − 2Q_f sin²θ_W and axial coupling a_f = T₃_f are functions of sin²θ_W with integer quantum numbers T₃ and Q_f. The QCD correction δ_QCD = α_s/π + 1.409(α_s/π)² − 12.77(α_s/π)³ for quarks, zero for leptons.

From this: R_l = Γ_had/Γ_l = [Σ_q N_c(v_q² + a_q²)(1 + δ_QCD)] / [v_l² + a_l²]. This depends on sin²θ_W and α_s. Given the measured R_l = 20.767, we can extract α_s if sin²θ_W is known, or sin²θ_W if α_s is known, or constrain both simultaneously.

The forward-backward asymmetry A_FB^f = (3/4)A_eA_f where A_f = 2v_fa_f/(v_f² + a_f²). This is a pure function of sin²θ_W at tree level — no α_s enters. So A_FB^l = 0.0171 gives an independent extraction of sin²θ_W that doesn't depend on the strong coupling at all.

**Rigor check:** The tree-level formulas give results at the per-mille level. Full one-loop corrections (dominated by Δρ ∝ G_F m_t²) shift things by ~1%. For a first extraction at the precision of the LEP measurements (3-5 sig figs), tree-level plus leading Δρ correction is sufficient. The one-loop Δρ = 3G_F m_t²/(8π²√2) is a Fraction computation — G_F and m_t are in the database, π² = 32R₄ is a MATH-2 pair.

**Yield:** Two independent extractions of sin²θ_W (from R_l and from A_FB^l). One extraction of α_s (from R_l once sin²θ_W is fixed). Comparison to input values tests consistency. Potential parameter derivation: if the extracted values match the inputs, consistency at per-mille level. If not, we've reproduced a known tension or found an error.

**Verdict: HIGH PRIORITY. All inputs ready. Infrastructure exists. Clear deliverable.**

---

## Path 2: Koide at Updated Precision

**What DATA-2 provides:** m_e = 0.51099895069 MeV (11 digits), m_μ = 105.6583755 MeV (10 digits), m_τ = 1776.86 MeV (6 digits). The Koide ratio computed: K = 0.666660511... with CF = [0; 1, 1, 1, 18050, ...].

**What PHYS-8 established:** K = (1 + a²/2)/N at N = 3, a² = 2 gives 2/3. The quadratic for m_τ from exact 2/3 gives m_τ(Koide) = 1776.97 MeV. Tension: 0.91σ.

**What's new with 11-digit m_e:** PHYS-8 used m_e at 8 digits. The quadratic m_τ = f(m_e, m_μ) propagates m_e precision directly. With 3 extra digits on m_e, the predicted m_τ(Koide) becomes more precise — not in its central value (which is dominated by m_μ at 10 digits), but in the confidence of the prediction. Let me think about this more carefully.

The Koide quadratic: s² − 4As + (3B − 2A²) = 0, where A = √m_e + √m_μ and B = m_e + m_μ. The sensitivity to m_e: ∂m_τ/∂m_e involves √m_e in A, and m_e is tiny compared to m_μ (ratio 1:207). So √m_e = 0.71484... contributes to A = 0.71484 + 10.2788 = 10.9937. The 3 extra digits on m_e shift √m_e in the 9th-11th decimal place, which shifts A in the 9th-11th place, which shifts m_τ(Koide) by roughly m_τ × (Δm_e/m_e) × (√m_e/A) ≈ 1777 × 10⁻⁸ × 0.065 ≈ 10⁻⁶ MeV. This is six orders of magnitude below the m_τ measurement uncertainty of ±0.12 MeV. The 3 extra digits on m_e don't change the Koide test at all — m_τ measurement precision is the bottleneck, not m_e.

**What IS useful:** The Koide ratio K = 0.666660511 at 6 sig figs (limited by m_τ at 6 sig figs). The CF a₄ = 18050 quantifies the distance to 2/3. Future m_τ measurements at 7-8 sig figs would change this to K at 7-8 sig figs and the CF partial quotient would either grow (K closer to 2/3) or shrink (K diverging). DATA-2 establishes the current baseline.

**What about quarks:** DATA-2 has m_u = 2.16 (3 dig), m_d = 4.70 (3 dig), m_s = 93.5 (3 dig), m_c = 1273 (4 dig), m_b = 4183 (4 dig), m_t = 172570 (5 dig), plus lattice ratios m_c/m_s = 11.783 (5 dig), m_b/m_c = 4.578 (4 dig), m_u/m_d = 0.485 (3 dig).

Computing Koide for up-type quarks (u, c, t): the mass hierarchy is extreme (2.16 : 1273 : 172570, a ratio of 1 : 589 : 79894). The √m values: √2.16 = 1.470, √1273 = 35.68, √172570 = 415.42. Sum of √m = 452.57. Sum of m = 173845.16. Koide ratio = 173845.16 / 452.57² = 173845.16 / 204819.6 = 0.8488.

For down-type (d, s, b): √4.70 = 2.168, √93.5 = 9.670, √4183 = 64.68. Sum of √m = 76.52. Sum of m = 4281.2. Koide = 4281.2 / 76.52² = 4281.2 / 5855.3 = 0.7312.

Lepton Koide: 0.6667 (= 2/3 to 0.001%). Up-type Koide: 0.849. Down-type Koide: 0.731. The quarks are both above 2/3 but by different amounts. The up-type is further from 2/3 than the down-type.

In the general formula (1 + a²/2)/3: up-type gives a² = 2 × (3 × 0.849 − 1) = 2 × 1.547 = 3.09, so a = 1.76. Down-type gives a² = 2 × (3 × 0.731 − 1) = 2 × 1.193 = 2.39, so a = 1.55. Leptons have a = √2 = 1.414. The amplitudes order as: leptons (1.414) < down quarks (1.55) < up quarks (1.76).

**The mixing connection test:** CKM mixing connects up-type to down-type mass eigenstates. The QUESTION from the planning material: does the CKM mixing angle correlate with the Koide deviation from 2/3? Leptons have no mixing and sit at the midpoint (a = √2). Quarks have CKM mixing and sit above the midpoint (a > √2). The ordering is suggestive but the test requires a specific functional relationship.

**Rigor check:** The quark masses at 3-4 sig figs give Koide ratios at 2-3 sig figs. The difference between up-type (0.849) and down-type (0.731) Koide ratios is 0.118, which is well above the uncertainty from quark mass errors (roughly ±0.05 for each). So the ordering is real: up > down > lepton. But connecting this to CKM angles requires a model relating the mass matrix structure to the mixing matrix, which is a theoretical step we haven't taken.

**Verdict: MEDIUM PRIORITY. The quark Koide ratios are computable now and give a real ordering. The mixing connection is testable in principle but requires theoretical work beyond just plugging in numbers.**

---

## Path 3: The Proton-to-Electron Mass Ratio

**What DATA-2 provides:** m_p/m_e = 1836.15267343 at 13 sig figs. Also m_p = 938.27208943 MeV at 11 digits, m_e = 0.51099895069 MeV at 11 digits.

**What the papers establish:** PHYS-1 argues mass is inertia. The proton mass is 99% binding energy from QCD. The ratio m_p/m_e = 1836.153 is therefore a ratio of (QCD binding energy) to (Higgs-generated electron mass) — two fundamentally different mechanisms producing inertia.

**What PSLQ says:** Already tested in the planning material. NULL at maxcoeff 10,000 against the 10-constant transcendental basis. m_p/m_e is not a simple linear combination of {π, e, ln 2, ζ(3), ζ(5), √2, √3, φ}.

**What's genuinely new to try:** The proton mass from dimensional transmutation: m_p ≈ Λ_QCD, where Λ_QCD ≈ M_Z × exp(−2π/(b₀α_s)) = M_Z × exp(−8R₂/(b₀α_s)). With b₀ = 7 (for 6 flavors, from PHYS-5), α_s = 0.1180, M_Z = 91187.6 MeV:

exp(−8R₂/(7 × 0.1180)) = exp(−8 × 0.7854/(0.826)) = exp(−7.607) = 0.000494

M_Z × 0.000494 = 45.1 MeV

This is way off from m_p = 938 MeV because the one-loop formula with b₀ = 7 (all 6 flavors active) isn't the right approximation — you need to match across flavor thresholds. With b₀ = 23/3 (5 flavors below m_t) and running from M_Z down to ~1 GeV where α_s becomes strong, the computation is the VP running from PHYS-5 in reverse. But this is a perturbative estimate of a non-perturbative quantity (Λ_QCD), and it's known to be imprecise by factors of 2-3.

**Rigor check:** The proton mass cannot be computed perturbatively. It requires lattice QCD. Current lattice gives m_p to about 1% (2-3 sig figs). Testing m_p/m_e against the transcendental basis at 13 digits requires computing m_p from first principles at 13 digits, which is decades away. This path is blocked by computational physics limitations, not by our framework.

**Verdict: LOW PRIORITY. The 13-digit ratio is beautiful data but we can't compute either side to matching precision from first principles. Store it, don't compute with it yet.**

---

## Path 4: R∞ as Primary m_e Input

**What DATA-2 provides:** R∞ = 10973731.568157 m⁻¹ at 13 digits. Also α⁻¹ = 137.035999177 at 12 digits.

**What this enables:** R∞ = α²m_ec/(2h). Since h and c are exact in SI, m_e = 2hR∞/(α²c). With R∞ at 13 digits and α at 12 digits, m_e is determined at 12 digits — one better than the direct CODATA mass measurement at 11 digits.

In Fraction arithmetic: m_e = 2 × h_frac × R∞_frac / (α_frac² × c), where h and c are exact integers, R∞_frac is the DATA-2 Fraction, and α_frac is the DATA-2 Fraction for α = 1/137.035999177. Every operation is exact.

**Rigor check:** This IS how CODATA determines m_e. The Rydberg is measured more precisely than the electron mass, and m_e is derived from it using α. We'd be reproducing the CODATA derivation in Fraction arithmetic. It confirms the database is self-consistent but doesn't produce new physics.

**What it enables downstream:** The derived m_e at 12 digits feeds into Koide, g-2, and VP running with one extra digit of precision. As shown in Path 2, this doesn't change the Koide test (m_τ is the bottleneck). For g-2, the electron mass enters through m_e/M_Z in the VP running — one extra digit shifts α⁻¹ by ~10⁻¹² in the 12th decimal place, which is below the 4.3 ppb residual from PHYS-9. So the extra digit doesn't change any existing result.

**Verdict: LOW PRIORITY for physics, but worth doing as a 10-minute consistency check. If m_e derived from R∞ and α disagrees with the direct m_e entry in DATA-2, the database has an error.**

---

## Path 5: The A₂ Coefficient in R₂/R₄ Form

**What DATA-2 provides:** π (105 digits), R₂ = π/4 (105 digits), R₄ = π²/32 (105 digits), ζ(3) (105 digits), ln(2) (105 digits) — all as Q335 integers.

**What PHYS-5/6/9 establish:** A₂ = 197/144 + π²/12 + (3/4)ζ(3) − (π²/2)ln(2). This is computed in Fraction arithmetic.

**The decomposition:** Substituting π² = 32R₄:

A₂ = 197/144 + (3/4)ζ(3) + R₄ × (32/12 − 32 × ln(2)/2)
   = 197/144 + (3/4)ζ(3) + R₄ × (8/3 − 16ln(2))

The rational part: 197/144. The number-theoretic part: (3/4)ζ(3). The geometric part: R₄ × (8/3 − 16ln(2)).

The coefficient of R₄ is (8/3 − 16ln(2)) = 8/3 − 16 × 0.6931... = 2.6667 − 11.090 = −8.424. So the geometric contribution is R₄ × (−8.424) = 0.3084 × (−8.424) = −2.597. The number-theoretic contribution is (3/4) × 1.2021 = 0.9016. The rational contribution is 197/144 = 1.368.

Total: 1.368 + 0.902 − 2.597 = −0.328. Check: A₂ = −0.32848... ✓

**What this reveals:** At 2-loop, the geometric content (R₄ term) is the largest contributor in absolute value and has the opposite sign from the other two. The cancellation between the geometric and non-geometric parts is what makes A₂ small. The geometric content dominates but is partially cancelled.

For A₃ the decomposition is more complex (10 terms, products of transcendentals), but the same separation applies: every π² becomes 32R₄, every π⁴ becomes (32R₄)² = 1024R₄².

**Rigor check:** This is pure algebra. No approximation, no assumption. The DATA-2 Q335 integers for R₄ and ζ(3) make the computation exact. The observation is structural: the geometric and number-theoretic content separate cleanly in the QED coefficients, with the geometric content carried by R₄ and the number-theoretic content by ζ values.

**Connection to amplitudes literature:** The separation of geometric (from phase space integrals) and arithmetic (from Feynman parameter integrals) content in scattering amplitudes is studied by Brown, Schnetz, and others through the Galois coaction on multiple zeta values. The R₂/R₄ decomposition is a specific, physically motivated version of this separation. Stating it explicitly in the HOWL language connects the series to that literature.

**Verdict: MEDIUM PRIORITY. Quick computation (30 min), publishable structural observation. Not a parameter reduction but a clean finding about the anatomy of QED.**

---

## Path 6: The CKM-Mass Relations with Updated Values

**What DATA-2 provides:** sin θ₁₂ = 0.22501 (5 dig), sin θ₂₃ = 0.04182 (4 dig), sin θ₁₃ = 0.003685 (4 dig). Lattice ratios: m_c/m_s = 11.783 (5 dig), m_b/m_c = 4.578 (4 dig), m_u/m_d = 0.485 (3 dig). Individual quarks: m_u = 2.16, m_d = 4.70, m_s = 93.5, m_c = 1273, m_b = 4183, m_t = 172570 MeV.

**What to test:** The classical Cabibbo relation sin θ₁₂ ≈ √(m_d/m_s). With updated values:

√(m_d/m_s) = √(4.70/93.5) = √(0.05027) = 0.2242

sin θ₁₂ = 0.22501

Ratio: 0.22501/0.2242 = 1.004. Match to 0.4%.

Using the lattice ratio m_s/m_ud = 27.23 where m_ud = (m_u + m_d)/2: m_d/m_s = m_d/(m_ud × 27.23/1) ... this needs m_d/m_ud. From m_u/m_d = 0.485: m_ud = m_d(1 + 0.485)/2 = 0.7425 m_d. So m_d/m_s = m_d/(27.23 × 0.7425 m_d) = 1/20.22 = 0.04946. Then √(m_d/m_s) = 0.2224.

That's further off: 0.22501/0.2224 = 1.012, a 1.2% miss. The Cabibbo relation holds at 0.4-1.2% depending on which mass values are used, consistent with it being a leading-order relation with corrections.

**Other CKM-mass relations from the literature:**

sin θ₁₃ ≈ √(m_u/m_t) × sin θ₁₂? √(2.16/172570) × 0.22501 = √(1.252 × 10⁻⁵) × 0.22501 = 0.003539 × 0.22501 = 0.000796. Measured sin θ₁₃ = 0.003685. Off by a factor of 4.6. This relation doesn't work.

sin θ₂₃ ≈ √(m_s/m_b)? √(93.5/4183) = √(0.02236) = 0.1495. Measured sin θ₂₃ = 0.04182. Off by a factor of 3.6. Doesn't work either.

sin θ₂₃ ≈ m_s/m_b? 93.5/4183 = 0.02236. Measured = 0.04182. Off by 1.9×. Closer but still not a match.

**Using lattice ratios more carefully:** sin θ₂₃ vs √(m_c/m_t)? √(1273/172570) = √(0.007377) = 0.08589. Measured = 0.04182. Ratio 0.487 — close to 1/2 but not exact.

**Rigor check:** The CKM-mass relations from the texture-zero literature (Fritzsch, Ramond, Roberts, others) are approximate, and different ansätze give different relations. None works at better than ~10-20% for all three angles simultaneously. The updated DATA-2 values sharpen the comparison but don't change the qualitative picture: the Cabibbo angle has a reasonably good mass relation, the other two don't.

**Verdict: LOW-MEDIUM PRIORITY. The Cabibbo relation sin θ₁₂ ≈ √(m_d/m_s) holds at 0.4-1.2%. The other angles don't have clean mass relations at the precision available. Worth documenting with updated values but not a breakthrough.**

---

## Path 7: Dimensionless Ratios and the Electroweak Scale

**What DATA-2 provides:** M_W/M_Z = 0.88136 (6 dig), m_H/M_Z = 1.37299 (5 dig), m_t/M_Z = 1.89247 (5 dig). Also G_F = 1.1663788 × 10⁻⁵ GeV⁻² (8 dig).

**The electroweak vacuum:** v = (√2 G_F)⁻¹/² = 246.22 GeV. This is the Higgs VEV. In DATA-2 terms: v² = 1/(√2 × G_F) = 1/(√2 × 1.1663788 × 10⁻⁵) = 60623.9 GeV².

The tree-level relation: M_W = gv/2, M_Z = M_W/cosθ_W, m_H = √(2λ) × v, where g is the SU(2) coupling and λ is the Higgs quartic. The ratios M_W/M_Z = cosθ_W and m_H²/(2v²) = λ are fundamental.

From DATA-2: cosθ_W = M_W/M_Z = 0.88136. So sin²θ_W = 1 − cos²θ_W = 1 − 0.7768 = 0.2232. Compare to DATA-2 sin²θ_W = 0.23122 (MSbar). The difference (0.2232 vs 0.2312) is the scheme dependence — the on-shell and MSbar definitions differ by radiative corrections of order α/π ≈ 0.23%.

The Higgs quartic: λ = m_H²/(2v²) = 125200²/(2 × 246220²) = 1.567 × 10¹⁰/(1.212 × 10¹¹) = 0.1293. And the SU(2) coupling: g² = 4M_W²/v² = 4 × 80369²/246220² = 4 × 0.1066 = 0.4263. So g = 0.653.

**The impedance matching test from PHYS-4:** Does λ relate to g'² (hypercharge coupling)? g' = g × tanθ_W = 0.653 × (sinθ_W/cosθ_W) = 0.653 × (0.4810/0.8814) = 0.653 × 0.5459 = 0.3565. So g'² = 0.1271. And λ = 0.1293. Ratio λ/g'² = 1.017. They match to 1.7%.

**Rigor check:** This is a tree-level comparison. Radiative corrections modify both λ(μ) and g'(μ) — they run with energy scale. At the electroweak scale, the running has been computed by many groups. The near-equality λ ≈ g'² at tree level is known in the literature and has been noted by several authors as a possible boundary condition from new physics at high scales. It's not our discovery. But it IS a testable relationship using our Fraction arithmetic, and the DATA-2 values nail it to 1.7%.

**What would make this a finding:** If we could show that the remainder framework (PHYS-10/11) predicts λ = g'² from a structural principle — for instance, if the Higgs self-coupling IS the hypercharge coupling because both are boundary readings of the same geometric quantity. This is speculative and the DISC-9 boundary says Level 2 parameters aren't determined by the framework. But the 1.7% match is striking and worth stating.

**Verdict: MEDIUM PRIORITY. The λ ≈ g'² comparison at 1.7% is a concrete numerical test that takes 10 minutes and produces a definite number. Whether it means anything is uncertain, but the computation is trivial.**

---

## Path 8: Cross-Checking the Database for Internal Consistency

**What DATA-2 provides:** Multiple entries that should satisfy known relationships. These are free consistency checks.

**Tests:**

1. m_p/m_e (entry 102, 13 dig) vs m_p (entry 12, 11 dig) / m_e (entry 9, 11 dig). Should agree to 11 digits.

2. R∞ (entry 14, 13 dig) vs α⁻¹ (entry 8, 12 dig) and m_e (entry 9, 11 dig): R∞ = α²m_ec/(2h). With c and h exact, this is a 3-way consistency check.

3. M_W/M_Z (entry 104, 6 dig) vs M_W (entry 23, 6 dig) / M_Z (entry 21, 6 dig). Should agree exactly.

4. m_μ/m_e (entry 99, 10 dig) vs m_μ (entry 10, 10 dig) / m_e (entry 9, 11 dig). Should agree to 10 digits.

5. Koide ratio (entry 107, 6 dig) vs computation from m_e, m_μ, m_τ (entries 9, 10, 11). Should agree to 6 digits.

6. α/π (entry 75, 12 dig) vs α⁻¹ (entry 8, 12 dig) and π (entry 58, 105 dig). Should agree to 12 digits.

**Why this matters:** If any of these fail, the database has an error and everything downstream is wrong. If all pass, we have a verified foundation. Takes 15 minutes.

**Verdict: HIGHEST PRIORITY. Do this first. A corrupted database invalidates everything.**

---

## Integrated Priority for This Session

1. **Database consistency checks** (15 min) — verify internal relations before computing anything new
2. **Z-pole observable calculator** (2-3 hrs) — the overconstrained extraction, highest-yield new computation
3. **A₂ in R₂/R₄ form** (30 min) — quick structural observation
4. **Quark Koide ratios** (30 min) — establish the up/down/lepton ordering with updated masses
5. **λ vs g'² comparison** (10 min) — quick numerical test of impedance matching

Paths 3, 4, and 6 are lower priority: m_p/m_e is blocked by lattice QCD precision, R∞ → m_e is a consistency check not a new result, and CKM-mass relations don't sharpen beyond what's already known.

---

Let me re-read the key framework rules from the transcript to make sure I have everything loaded before doing my own assessment.Good. I have the full framework loaded. Here is my assessment — I'll go deeper than the other Claude by systematically mapping every paper's rules against the DATA-2 output to find paths they missed.

---

# Open Paths From DATA-1/DATA-2 — Full Assessment

## Agreement with Other Claude

I agree with their priority ordering for Paths 1 (EW overconstrained), 2 (Koide updated), 5 (A₂ decomposition), 7 (λ vs g'²), and 8 (consistency checks). Path 8 should indeed go first. I won't repeat their analysis of those paths. Instead I'll focus on what they missed or underweighted.

---

## Path A: The MATH-1 Skeleton Applied to DATA-1 Impedances

Other Claude didn't do this. MATH-1 says every R₂ equation has the skeleton Q = F · R₂ · d² · Z, where Z is domain-specific impedance. DATA-1 catalogued 20+ R₂ equations across engineering domains. The impedances Z have never been extracted and compared.

The impedances from DATA-1:

| Domain | Q = F · R₂ · d² · Z | Z (impedance) | What Z Contains |
|---|---|---|---|
| Pipe flow | Q = v · R₂d² | Z = 1 (velocity is the full drive) | Nothing — pure geometry |
| Orifice | q = C_d · R₂d² · √(2ΔP/ρ) | Z = C_d = π/(π+2) × C_v | Vena contracta (R₂-derived!) × viscous correction |
| Wire resistance | R = ρL/(R₂d²) | Z = ρL (resistivity × length) | Material property |
| Antenna | A_eff = Gλ²/(16R₂) | Z = G (gain) | Integer for ideal dipole, measured for real antennas |
| Gaussian beam | z_R = 4R₂w₀²/λ | Z = 1/λ (wavelength) | Wave property |
| Stefan-Boltzmann | P = σT⁴ · R₂d² · ε | Z = σT⁴ε | Exact SI × temperature⁴ × emissivity |
| Capacitor | C = ε₀R₂d²/t | Z = ε₀/t | Permittivity / gap |
| Fiber mode | A = R₂ · MFD² | Z = 1 | Pure geometry |
| Sound intensity | I = P/(16R₂r²) | Z = P/r² (power/distance²) | Source + distance |

The structural finding: Z is where ALL the measured physics lives. R₂ carries the geometry. F carries the external drive. The SM parameters only enter through Z.

**The orifice is unique.** Its Z = π/(π+2) × C_v, where the leading factor π/(π+2) is itself an R₂ function. This is the only domain where the impedance contains geometric content. In every other domain, Z is either a material property (ρ, ε₀, ε), a coupling (G), or unity. The orifice impedance feeds back into geometry — the fluid's resistance to turning a sharp corner is determined by the geometry of the turn, not by a material constant.

**What to compute:** Extract Z for every R₂ equation in DATA-1. Express each Z in terms of SM parameters where possible. Build the impedance table. Check: are any two impedances from different domains the same function of the same SM parameter? If so, that's a cross-domain connection through the MATH-1 skeleton.

**Yield:** Probably a structural observation, not a parameter reduction. But the impedance table doesn't exist yet and it would complete the MATH-1 program.

---

## Path B: The Remainder Decomposition Applied to LEP Data

PHYS-10 establishes: physical quantity = integer quotient × modulus + remainder. PHYS-11 shows the modulus is 8R₂ × scale for Subgroup A. The DATA-2 conversion gives exact Q335 numerators for the LEP observables.

Nobody has decomposed the LEP observables in the remainder framework.

Take R_l = 20.767. The Q335 numerator has small factor 2⁵. So R_l × 2³³⁵ = 2⁵ × (101-digit cofactor). The quotient-remainder decomposition divmod(R_l_Q335, 8R₂_Q335) would give an integer quotient and a remainder. If R_l lives on an 8R₂ lattice (as all Subgroup A quantities do), the quotient should be an integer related to the number of contributing channels and the remainder should carry the coupling information.

R_l = Γ_had/Γ_l = [N_c × Σ_q(v_q² + a_q²)(1+δ_QCD)] / (v_l² + a_l²). The quantum numbers N_c = 3, T₃, Q_f are integers. The δ_QCD = α_s/π + ... = α_s/(4R₂) + ... So the QCD correction enters as α_s/(4R₂), meaning the remainder after dividing by R₂ carries α_s. This is a concrete computation.

**What to compute:** For each LEP observable, compute divmod(observable_Q335, R₂_Q335). Check whether the quotients are small integers. If they are, the observable sits close to a multiple of R₂, and the remainder is the coupling content.

For R_l ≈ 20.767: R_l/R₂ = 20.767/0.7854 = 26.44. Not an integer. R_l/(8R₂) = 20.767/6.2832 = 3.306. Not an integer either. R_l/(4R₂) = 20.767/3.1416 = 6.61. Not integer.

So R_l doesn't sit on an R₂ lattice. This is expected — R_l is a RATIO of partial widths, and R₂ enters both numerator and denominator, so it cancels. R_l is an R₂-free observable. Same cancellation pattern as R∞.

**Revised approach:** Apply the remainder decomposition not to R_l but to the partial widths themselves. Γ_l = G_F M_Z³/(6π√2) × (v_l² + a_l²) contains 1/π = 1/(4R₂) explicitly. So Γ_l × 4R₂ = G_F M_Z³/(6√2) × (v_l² + a_l²). That product should be R₂-free.

**Yield:** This classifies which EW observables are R₂-dependent (partial widths) and which are R₂-free (ratios of partial widths). The R₂-free observables are the ones with the highest precision — extending the R₂ cancellation theorem from DATA-1 Section 22 to the electroweak sector.

---

## Path C: The Confinement Wall in R₂ Language

PHYS-6 established that the confinement boundary has two faces: above ~2 GeV (perturbative QCD works, VP ratio ≈ 1.0) and below ~2 GeV (confinement reduces VP to 61% of perturbative). The number 0.61 was noted but not connected.

DATA-1 finds: the vena contracta coefficient C_c = π/(π+2) = 0.6108.

The confinement ratio below 2 GeV is ~0.61. The vena contracta for a sharp-edged orifice is π/(π+2) = 0.6108.

**Is this a coincidence?** Almost certainly yes. The confinement ratio is approximate (~0.61, with significant uncertainty from the hadronic VP integral) and the vena contracta is exact (π/(π+2), from potential flow theory). The physical mechanisms are completely different (QCD confinement vs incompressible fluid inertia). The numerical proximity is likely chance.

**But test it anyway.** If the confinement ratio is exactly π/(π+2), that would mean confinement reduces the vacuum polarization to the same fraction that geometry reduces the orifice jet. Both would be "how much of the available area/contribution actually participates when streamlines/color flux can't make sharp turns." Confinement = quarks can't escape the boundary. Vena contracta = fluid can't turn the corner. The structural analogy is: both involve a maximum-angle turn of π/2, and C_c = π/(π+2) is the fraction that survives a π/2 turn.

**What to compute:** Extract the actual hadronic VP ratio below 2 GeV from the PHYS-6 data. Compare to π/(π+2) at the precision available. If the match is better than 1%, it's worth a deeper look. If it's a 10% match, it's noise.

From PHYS-6: below-2-GeV VP = 0.46 × 0.61 in the weighted average. The 0.61 is quoted roughly. The actual e⁺e⁻ → hadrons data (R-ratio) below 2 GeV involves ρ, ω, φ resonances and is messy. The ratio of measured to perturbative is not a single number — it depends on energy. The "0.61" is an effective average weighted by the α running kernel.

**Honest assessment:** Not enough precision to test. The 0.61 from PHYS-6 is a rough average, not a 4-digit number. We'd need the actual R-ratio data point by point and the kernel integral done properly. This is a rabbit hole without enough data to reach a conclusion.

**Verdict: LOW priority. Numerically suggestive, physically unlikely, insufficient precision to test.**

---

## Path D: The Three-Generation Structure Through Koide

PHYS-8 says the Koide formula works because N = 3 objects equally spaced on a circle at 120° in √m space. The denominator 3 IS the generation count. Other Claude computed the quark Koide ratios. But neither Claude asked: what happens if we apply the PHYS-11 classification to the Koide domain?

Koide is: three masses on a circle with period 2π/3 = R₂ × 8/3. The spacing is 2π/3 = (8/3)R₂. This is NOT 8R₂ (the Subgroup A period) — it's 8R₂/3. The factor of 3 is the generation count.

So Koide lives on a phase-periodic domain with modulus (8/3)R₂ instead of 8R₂. In the PHYS-11 language, this is Subgroup A with the modulus divided by the generation count. If there were 4 generations, the Koide analogue would have modulus (8/4)R₂ = 2R₂. For 2 generations, (8/2)R₂ = 4R₂ = π. For N generations, 8R₂/N = 2π/N.

**The PHYS-7 connection:** θ_QCD = 0 from energy minimization of −cos(φ) on the 8R₂ domain. If the Koide domain has modulus 8R₂/3, the ground state of −cos(3φ) on that domain is... also φ = 0. The ground state principle doesn't change. But the EXCITED states differ: on 8R₂, the first excited state is at φ = 8R₂ = 2π (trivial). On 8R₂/3, the first non-trivial stationary point is at φ = 2π/3, which IS the equal spacing.

**This is the derivation path for the equal spacing.** The equal spacing in Koide is the first non-trivial stationary point of a cosine potential on a domain of modulus 8R₂/3. Just as θ_QCD = 0 is the ground state of −cos(θ) on the 8R₂ domain, the 120° spacing is a stationary point of cos(3θ) on the same domain.

**What to compute:** Write the potential V(θ₁, θ₂, θ₃) for three phases on a circle with C₃ symmetry. The ground state has all three at the same point (θ₁ = θ₂ = θ₃ = 0). The first excited state has them equally spaced: θ_k = 2πk/3. Show that the Koide parametrization √m_k = M(1 + a·cos(θ₀ + 2πk/3)) IS the first excited state of such a potential. The amplitude a is then determined by which excited state level — and a = √2 corresponds to a specific energy (the critical amplitude where one mass hits zero).

**Yield:** If this works, it derives the equal spacing from C₃ symmetry on the Subgroup A domain, and the amplitude a = √2 from the criticality condition. That would be the Koide derivation. Two conditional results become one: θ = 0 AND Koide from the same ground-state/excited-state principle applied to different representations of the same group.

**Verdict: HIGH PRIORITY. This is the theoretical path. It requires algebra, not data.**

---

## Path E: The Gap Ratio 218/115 as a Particle Content Constraint

PHYS-5 found the gap ratio (b₁ − b₂)/(b₂ − b₃) = 218/115 = 1.896 (SM prediction) vs 1.395 (measured from coupling convergence). The 36% miss means the SM particle content is incomplete between M_Z and M_GUT.

DATA-2 has all three gauge couplings: α = 1/137.036, α_s = 0.1180, sin²θ_W = 0.23122. From sin²θ_W and α, the SU(2) and U(1) couplings are extractable.

The question PHYS-5 didn't answer: what MINIMAL particle content gives gap ratio 1.395? This is a finite enumeration. Each additional particle contributes (Δb₁, Δb₂, Δb₃) to the beta functions. The contribution depends only on the particle's quantum numbers (representation under SU(3)×SU(2)×U(1)) and its spin.

For a scalar in representation (R₃, R₂, Y): Δb_i = T(R_i)/6. For a Weyl fermion: Δb_i = T(R_i)/3. For a vector: Δb_i = −11T(R_i)/6.

The measured gap ratio constrains: (b₁ + Δb₁ − b₂ − Δb₂)/(b₂ + Δb₂ − b₃ − Δb₃) = 1.395.

**What to compute:** Enumerate all simple extensions (one additional multiplet) and check which gives gap ratio closest to 1.395. The MSSM adds specific partners to every SM particle, giving a well-known prediction. But there may be simpler extensions (one scalar doublet, one vector-like fermion pair) that also work.

This is a PHYS-5 extension using DATA-2 values. The computation is pure Fraction arithmetic — the beta function coefficients are exact rationals.

**Yield:** Either the MSSM is the unique minimal solution, or there are other solutions with fewer particles. Either way, it's a concrete constraint on BSM physics from our framework.

**Verdict: MEDIUM-HIGH PRIORITY. Finite computation, concrete result, extends PHYS-5.**

---

## Path F: The Bessel Zeros in the PSLQ Framework

DATA-2 includes j₁₁ = 3.83171 (first zero of J₁) and j₀₁ = 2.40483 (first zero of J₀) at 105 digits. These enter every diffraction-limited optical system and every fiber optic cutoff calculation.

The 72/72 PSLQ null tested SM parameters against the transcendental basis. It did NOT test Bessel zeros. These are pure mathematical constants that appear in industrial precision equations. Are they algebraically independent of {π, e, ln 2, ζ(3), ζ(5), √2, √3, φ}?

Mathematically, Bessel zeros are known to be transcendental (Siegel, 1929). But algebraic independence from π and the other basis constants is NOT proven. It's expected but unverified. A PSLQ test at 100 digits would either confirm independence (expected null) or find a relation (would be a genuine mathematical discovery).

**What to compute:** Run PSLQ on j₁₁ and j₀₁ against the extended transcendental basis at 100 digits with maxcoeff 10,000. Same protocol as DISC-7. If null, we've extended the independence result to Bessel zeros. If positive, we've discovered a new identity.

**Yield:** Almost certainly null, confirming what's expected. But the computation is cheap (minutes) and the null strengthens the framework. And if it's NOT null, it's a mathematical paper on its own.

**Verdict: MEDIUM PRIORITY. Cheap test, expected null, closes a gap.**

---

## Path G: The BCS Gap as a Framework Cross-Check

DATA-2 has π/e^γ = 1.76388 (BCS gap ratio) at 105 digits, and γ = 0.57722 (Euler-Mascheroni) at 105 digits. The BCS weak-coupling gap matches aluminum at 4 sig figs.

MATH-2 classifies γ as Tier 2 (mathematically defined, computable in principle, not yet computed in HOWL Fraction arithmetic). DATA-2 has it as a Q335 integer. The question: can we verify the Q335 representation of γ against the BCS measurement?

π/e^γ = 1.76388... The BCS prediction for Al: 2Δ₀/(k_BT_c) = 2 × 1.76388 = 3.52757. Measured for Al: 3.528. Agreement to 4 sig figs (0.01% level). This confirms π/e^γ is correct at 4 sig figs.

But we already have π/e^γ at 105 digits from mpmath. The BCS measurement at 4 sig figs adds nothing to the mathematical precision. What it DOES add: confirmation that γ enters physics through a non-QED mechanism (Cooper pairing). The same Euler-Mascheroni constant that appears in the QED vertex correction also appears in condensed matter through a completely different integral (the BCS gap equation).

**What to compute:** Compute π/e^γ in pure Fraction arithmetic using the MATH-2 series for γ (if feasible) or the Q335 integer pair (trivial). Compare to the Q335 representation. This is a 5-minute computation that verifies the Tier 2 classification.

**Yield:** Confirms γ is correctly represented. Not a physics discovery but closes a gap in the verification chain.

**Verdict: LOW PRIORITY but trivially cheap.**

---

## Path H: Neutrino Mixing as Subgroup A Predictions

The planning material notes sin²θ₁₂ ≈ 0.307 (close to 1/3) and sin²θ₂₃ ≈ 0.545 (close to 1/2). Tribimaximal mixing (TBM) predicts exactly 1/3, 1/2, 0 for the three mixing angles.

In the remainder framework: the PMNS mixing angles are phases on [0, π/2]. The Subgroup A modulus is 8R₂ × scale. For phases on [0, π/2], the scale is 1/(4) (since π/2 = 4R₂/1), so the modulus is 8R₂/(4) = 2R₂ = π/2.

On a domain of modulus π/2, equally spaced points at 120° give phases at π/6, π/3, π/2. The squares of sines: sin²(π/6) = 1/4, sin²(π/3) = 3/4, sin²(π/2) = 1. These are NOT the TBM values (1/3, 1/2, 0).

Different approach: the PMNS mixing angles aren't phases in position space — they're parameters of a unitary rotation matrix. The C₃ symmetry approach from A₄ flavor symmetry gives sin²θ₁₂ = 1/3 directly from the group structure, not from a phase-periodic domain.

**Honest assessment:** The remainder framework (Subgroup A) doesn't naturally accommodate mixing angles. Mixing angles parameterize a unitary matrix, not a periodic phase. The connection to Subgroup A would require rewriting the PMNS matrix in a phase-periodic form, which is non-trivial and may not be possible.

**But the DATA-2 continued fractions tell us something.** sin²θ_W = 0.23122 has CF = [0; 4, 3, 12, ...]. The best small approximation is 1/4 at 1 digit and 3/13 at 2 digits. The number 1/4 = sin²(π/6) is a Subgroup A prediction if θ_W is a phase on the 8R₂ domain. The measurement is 0.23122, which is 8% below 1/4. Is this 8% a radiative correction?

At tree level in SU(5): sin²θ_W = 3/8 = 0.375 at the GUT scale. Running down to M_Z gives 0.231. The measured value is 0.23122. So sin²θ_W at M_Z is NOT close to 1/4 by coincidence — it's 3/8 run down by the same RG running from PHYS-5.

**What to compute:** Starting from sin²θ_W(GUT) = 3/8, run the three gauge couplings down using the PHYS-5 beta function infrastructure. Predict sin²θ_W(M_Z) in Fraction arithmetic. Compare to the measured 0.23122.

This IS the sin²θ_W = 3/8 + running path from the planning material. It uses PHYS-5 infrastructure directly. The gap ratio from PHYS-5 (218/115 vs 1.395) already tells us the SM doesn't unify exactly, but the predicted sin²θ_W(M_Z) from 3/8 + SM running is a concrete number.

**Yield:** A predicted sin²θ_W(M_Z) from GUT-scale 3/8, computable in Fraction arithmetic. If it matches the measured 0.23122 to 5 sig figs using SM running, the Weinberg angle is derivable from 3/8 + integers (the beta coefficients). If it doesn't match (expected from the 36% gap ratio miss), the mismatch quantifies how much BSM content is needed.

**Verdict: MEDIUM-HIGH PRIORITY. Uses existing PHYS-5 infrastructure. Concrete prediction.**

---

## Summary: Integrated Priority List

| Rank | Path | Source | Yield | Effort |
|---|---|---|---|---|
| 0 | Database consistency checks | Other Claude Path 8 | Foundation verification | 15 min |
| 1 | EW overconstrained extraction | Other Claude Path 1 | α_s, sin²θ_W derived | 2-3 hrs |
| 2 | Koide from C₃ symmetry on Subgroup A domain | My Path D | POTENTIAL DERIVATION of equal spacing + a²=2 | 1-2 hrs algebra |
| 3 | sin²θ_W from 3/8 + running | My Path H | Concrete GUT prediction in Fraction arithmetic | 1 hr |
| 4 | Gap ratio particle content enumeration | My Path E | Constrains BSM spectrum | 1 hr |
| 5 | A₂ in R₂/R₄ form | Other Claude Path 5 | Structural observation | 30 min |
| 6 | Quark Koide ratios + mixing correlation | Other Claude Path 2 | Establishes ordering | 30 min |
| 7 | Bessel zeros PSLQ | My Path F | Expected null, closes gap | 30 min |
| 8 | Impedance table | My Path A | Completes MATH-1 | 1 hr |
| 9 | λ vs g'² | Other Claude Path 7 | Quick numerical test | 10 min |
| 10 | BCS γ verification | My Path G | Tier 2 cross-check | 5 min |

**Path D (Koide from C₃ on Subgroup A) is the highest-yield theoretical path.** If the equal spacing and critical amplitude both follow from the ground-state/excited-state structure of a C₃-symmetric potential on the 8R₂ domain, then PHYS-7 (θ = 0) and PHYS-8 (Koide) become two instances of the same principle, and the Koide formula is derived rather than assumed. This is the only path on the list with the potential to reduce parameter count.
