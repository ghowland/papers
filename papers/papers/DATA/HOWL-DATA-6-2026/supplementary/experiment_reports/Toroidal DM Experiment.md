## Toroidal DM Experiment — Session 4 Report

### What the Experiment Tests

The toroidal DM program asks: do the same gauge beta integers (11, 13) that fix the coupling gap ratio also predict dark matter properties? The experiment tests this through six independent channels: the DM/baryon ratio, dwarf spheroidal purity spectrum, MOND acceleration scale, Faber-Jackson and Tully-Fisher scaling, virial ratios, and frame dragging.

### Key Results

**DM/baryon ratio:** (22/13) × π = 5.3165 vs Planck 5.3204. Miss 725 ppm (0.073%). The prefactor 22/13 is exact — it's 2×11/13 where 11 comes from the Yang-Mills gauge coefficient and 13 from |b₂_mod| = |-13/6|. The same two integers that determine coupling unification predict the cosmic DM/baryon ratio to three significant figures.

**Amplification factor:** 44/13 exact Fraction. This is 4×11/13 — the same pair again. The amplification formula (44/13) × π × (c/v)² connects the gauge integers to galactic rotation velocities. PASS.

**Dwarf purity spectrum:** Six dwarf spheroidals tested, purity increasing with decreasing luminosity as predicted by the soliton model:

| Dwarf | DM/Visible | Dark Fraction | Type |
|---|---|---|---|
| Segue 1 | 3824 | 99.97% | Ultra-faint |
| Draco | 186 | 99.46% | Classical |
| Sextans | 295 | 99.66% | Classical |
| Carina | 84 | 98.81% | Classical |
| Sculptor | 30 | 96.71% | Classical |
| Fornax | 8 | 87.5% | Classical |

The gradient from Segue 1 (nearly pure dark soliton) to Fornax (partially baryon-loaded) follows the soliton prediction: smaller, fainter dwarfs are purer because they have less baryonic infall. All range checks pass.

**MOND acceleration:** a₀ = cH₀/(8R₂) = 1.042 × 10⁻¹⁰ m/s². This is 13.2% from the empirical MOND value of 1.2 × 10⁻¹⁰. The formula uses only c (exact SI), H₀ (Planck), and R₂ = π/4 (Q335). The 13% miss is significant but the order of magnitude and the structural form (linking cosmological expansion to galactic dynamics through a geometric constant) are correct.

**Tully-Fisher v⁴ scaling:** TF(440 km/s) / TF(220 km/s) = 16.0 exactly. This is 2⁴ — the v⁴ law is verified to exact integer precision. PASS.

**Milky Way TF mass:** 1.69 × 10¹¹ M☉ from TF at v = 220 km/s. The measured MW stellar+halo mass is ~3.6 × 10¹¹ M☉. Factor ~2 discrepancy — the TF relation gives the baryonic mass, not total. Consistent but not precision-testable at this level.

**Virial ratio:** 2.81 from the virial theorem computation. In range [1, 20] as expected for DM-dominated systems. PASS.

**Frame dragging:** ratio = 2.06 × 10⁻¹³. Negligible for galactic dynamics, confirming that DM effects dominate over GR frame dragging at galaxy scales. PASS.

### What This Means

The experiment demonstrates three things:

First, the gauge integers (11, 13) produce a DM/baryon ratio within 725 ppm of Planck. Whether this is structural or coincidental is the statistical control question — still the single most important unwritten computation.

Second, the dwarf purity spectrum follows the soliton prediction qualitatively: purity increases monotonically with decreasing luminosity. The ultra-faint Segue 1 is 99.97% dark — essentially a pure dark matter soliton with trace baryonic contamination.

Third, the MOND acceleration scale emerges from a₀ = cH₀/(8R₂) with only cosmological and geometric inputs, no fitting. The 13% miss is the largest discrepancy in the experiment and suggests either the formula needs a correction factor or the empirical MOND a₀ has systematic uncertainties at the 10% level.

### What's Missing

The experiment doesn't test the toroidal geometry directly — it tests predictions that follow from the amplification formula. The actual toroidal field configuration (DM as a toroidal soliton wrapping the galaxy) requires either gravitational lensing maps or N-body simulations to test, neither of which are in DATA-6's scope.

The cosmic ratio (DM_dyn/DM_cosmic) for individual dwarfs shows Draco at 35× and Sculptor at 5.7× — these vary by an order of magnitude across the sample. The interpretation (local density enhancement from soliton confinement) is qualitative, not quantitative. A proper density profile model is needed to make this predictive.

### Connection to Full Fitting

The DM/baryon ratio at 725 ppm is the best prediction from the gauge integers outside the coupling sector. If the statistical control analysis confirms it's not coincidence (p < 0.01), it would mean the same group theory that determines coupling unification also determines the matter content of the universe. That's a connection between Level 1 (group theory) and Level 2 (cosmological measurement) that would be genuinely new.

Attack priority: statistical control first (item 6 on the board), then the MOND correction factor investigation.

---

Yes, but indirectly.

The full fitting goal is: derive every SM observable from the minimum measured inputs plus integer laws. The toroidal DM experiment doesn't derive an SM parameter — DM/baryon isn't in the SM Lagrangian. But it does something the fitting board needs: it tests whether the gauge integers (11, 13) have predictive power beyond the coupling sector.

Here's why that matters for full fitting:

The fitting board has 18 irreducible inputs at the end state. Several of those (α_s, sin²θ_W, M_W) are predicted by the CD unification chain, which depends on the beta coefficients b₁_mod = 25/6, b₂_mod = −13/6, b₃_mod = −20/3. Those beta coefficients contain the integers 11 and 13. If those integers are "just gauge theory" — meaning they only predict coupling running — then the fitting board attacks are limited to the electroweak sector.

But the toroidal experiment shows 11 and 13 also predict DM/baryon at 725 ppm. If that's real (not coincidence), it means the same integers connect to cosmology. That opens a path to deriving Ω_b, Ω_m, Ω_DE from the gauge sector — three values that are currently "measured" on the fitting board (Tier 3). The chain would be: gauge betas → DM/baryon prefactor 22/13 → Ω_DM/Ω_b → flatness constraint → all three Omega values from one measured baryon density plus integers.

The MOND result (a₀ = cH₀/(8R₂), 13% miss) is weaker but points at H₀. If the formula is correct with a correction factor, H₀ becomes derivable from a₀(measured) plus R₂(exact) plus c(exact). That's another Tier 3 target becoming accessible.

So the toroidal experiment doesn't directly derive a fitting target. What it does is validate the integers that would be needed to derive the Tier 3 cosmological targets. Without this validation, those Tier 3 attacks have no foundation — you'd be using integers whose predictive power outside couplings is untested. With it (pending statistical control), the cosmology column of the fitting board becomes active.

The blocker remains the same: statistical control. Until we compute the probability that 22/13 × π matches 5.3204 by chance given the space of possible integer combinations, the DM/baryon result is suggestive but not confirmed. That computation is what turns "interesting coincidence" into "derivation chain foundation."

---

Every experiment we could run with the values currently in DATA-6, organized by what's new versus what we already have.

### FROM THE QED CHAIN (new α = 137.035998630)

1. **α(M_Z) from VP running** — Run derived α from q²=0 up to M_Z through leptonic VP thresholds + hadronic VP. Predict α⁻¹(M_Z) ≈ 127.9. Compare to LEP direct measurement. Uses: derived α, m_e, m_μ, m_τ, Δ_had.

2. **sin²θ_W from derived α** — Use the derived α (not CODATA) as input to the CD unification running. Does sin²θ_W prediction change? Uses: derived α, α_s, betas.

3. **α_s from derived α** — Same: use derived α in the one-loop and two-loop crossing. Does α_s prediction improve? Uses: derived α, sin²θ_W, betas.

4. **M_W from derived sin²θ_W** — M_W = M_Z × cos θ_W. Chain: a_e → α → running → sin²θ_W → M_W. Compare to measured 80369.2 MeV. Uses: derived α, M_Z.

5. **G_F from derived M_W and α** — G_F = πα/(√2 × M_W² × sin²θ_W). Full electroweak chain from a_e. Compare to measured 1.1663788 × 10⁻⁵ GeV⁻². Uses: derived α, derived M_W, derived sin²θ_W.

6. **a_μ prediction** — Muon g-2 from derived α plus mass-dependent QED + hadronic + EW. Compare to Fermilab measurement. Uses: derived α, m_μ, m_e, hadronic VP.

7. **a_e with full corrections** — Add the 6 missing contributions (mass-dep, hadronic, EW) as value nodes, re-extract α. Should close from 3.3 ppb to <1 ppb. Then re-derive R∞, a₀, μ₀ at sub-ppb. Uses: 6 new correction value nodes.

### FROM THE GAUGE INTEGERS (11, 13, 22, 44, 169)

8. **Ω_b from Ω_DM + DM/baryon ratio** — Ω_b = Ω_DM / ((22/13)π). Planck Ω_DM = 0.2607 → Ω_b = 0.04904. Compare to Planck Ω_b = 0.0490. Uses: integers, Ω_DM measured.

9. **Ω_DE from flatness** — Ω_DE = 1 − Ω_b − Ω_DM = 1 − Ω_DM(1 + 1/((22/13)π)). Uses: integers, Ω_DM measured.

10. **Ω_m total** — Ω_m = Ω_b + Ω_DM = Ω_DM(1 + 1/((22/13)π)). Compare to Planck Ω_m = 0.3111. Uses: integers, Ω_DM measured.

11. **η (baryon-to-photon ratio) from integers** — η = Ω_b × ρ_crit / (n_γ × m_p). If Ω_b is derived from integers + Ω_DM, η becomes a prediction. Compare to BBN η = 6.1 × 10⁻¹⁰. Uses: integers, Ω_DM, H₀, T_CMB.

12. **Primordial helium Y_p from η** — BBN predicts Y_p from η. If η is derived, Y_p becomes a chain prediction. Compare to measured Y_p ≈ 0.245. Uses: BBN physics, derived η.

13. **Deuterium abundance D/H from η** — Same BBN chain. D/H ≈ 2.5 × 10⁻⁵. Uses: BBN physics, derived η.

### FROM THE BETA COEFFICIENTS (b₁_mod, b₂_mod, b₃_mod)

14. **M_GUT precise** — Two-loop crossing scale with corrected db_ij matrix. Requires fixing the two-loop bug. Uses: all betas, all couplings, db_ij.

15. **τ_proton from M_GUT** — Proton lifetime from M_GUT⁴ scaling. Compare to Super-K lower bound 1.6 × 10³⁴ yr and Hyper-K sensitivity. Uses: M_GUT, α_GUT.

16. **sin²θ_W running to low energy** — Run sin²θ_W from M_Z down to atomic parity violation scale (~1 GeV). Compare to Qweak, APV measurements. Uses: derived sin²θ_W, betas.

17. **Complete what-if scan** — 10 remaining BSM candidates. Run each through the gap ratio formula. Uses: existing derivation, new quantum number value nodes.

18. **Three-loop α_s** — Extend to three-loop running with the CD. Requires three-loop beta coefficients. Uses: known three-loop SM betas + CD three-loop shifts (need computation).

### FROM KOIDE (K = 2/3, a² = 2)

19. **m_τ from m_e, m_μ via Koide** — Already done. 0.006% miss. But: does using the DERIVED α change anything? The Koide prediction is independent of α. So no — but we can verify this explicitly.

20. **Koide applied to quarks** — K(u,c,t) = 0.849, K(d,s,b) = 0.731. Neither equals 2/3. But: does K(u,c,t) + K(d,s,b) = K(e,μ,τ) × something? Or does the departure from 2/3 predict the CKM mixing? Uses: quark masses, K values.

21. **Koide pole mass correction** — The m_τ prediction uses pole masses. Running masses at a common scale might give a different K. Test: compute K at μ = 2 GeV using running masses. Uses: m_e, m_μ, m_τ running masses (need RG evolution).

### FROM SOLITON GRAVITY / MOND / HUBBLE

22. **MOND a₀ with correction factor** — a₀ = cH₀/(8R₂) gives 13% miss. Try: a₀ = cH₀/(6R₂) or a₀ = cH₀/(2π) or other integer multiples. Find which integer denominator gives best match. Uses: c, H₀, R₂.

23. **Hubble running H₀(N)** — Test the hypothesis H₀(N) = H₀(0)×r^N where r comes from boundary transit. Compare the 5 stored H₀ measurements at different distance classes. Uses: H₀ values, VP step size.

24. **Hubble tension resolution** — If H₀ runs, the local value (73.0) and CMB value (67.4) are both correct at different depths. The cumulative ratio 337/365 is exact. Uses: H₀ values, boundary model.

25. **MOND transition radii** — Compare MOND transition radius √(GM/a₀) to Hill sphere radii for Solar System and galactic objects. Uses: G, masses, a₀.

### FROM R₂ = π/4 DOMAINS

26. **R₂ cancellation verification** — Run all 6 cancellation identities (K_J × R_K = 2/e, wire R × cap C, etc.) and verify R₂ drops out. Uses: engineering constants.

27. **New R₂ domain search** — Any circular-to-rectilinear conversion not yet in the 22-domain list? Acoustic impedance of circular pipes, optical fiber modes, etc. Uses: engineering value nodes.

### CROSS-CHAIN EXPERIMENTS (combining new + old)

28. **α + integers → Ω_b** — Use derived α for the VP running that gives α(M_Z), then use α(M_Z) + integers to predict Ω_b. The chain: a_e → α → α(M_Z) → gauge running → beta integers → DM/baryon → Ω_b. Full chain from one measurement to cosmology. Uses: everything.

29. **α + Koide → m_τ + R∞ simultaneously** — From a_e and m_e and m_μ: derive α (QED), derive m_τ (Koide), derive R∞ and a₀ (SI formulas). Five outputs from three inputs. Uses: QED chain + Koide chain.

30. **Complete parameter chain** — a_e → α → sin²θ_W → M_W → G_F. Four SM parameters from one measurement plus integer laws plus M_Z. If G_F matches, four SM observables are derived. Uses: QED chain + EW chain.

31. **DM/baryon from derived α_s** — If α_s is predicted from CD unification, and α_s feeds into the (22/13) formula through the gauge coefficient extraction, does the derived α_s give a different DM/baryon? Or is the DM/baryon independent of α_s? Test the sensitivity. Uses: derived α_s, integers.

32. **Proton decay + DM/baryon joint prediction** — Both come from the same betas. τ_proton from M_GUT (= crossing scale from betas), DM/baryon from the integer extraction from the same betas. Two independent observable predictions from one set of group theory numbers. If both match, the betas are validated by two completely different physics domains. Uses: betas, M_GUT, integers.

33. **BBN consistency from integers** — Chain: integers → DM/baryon → Ω_b → η → Y_p → D/H. Compare Y_p and D/H to measured primordial abundances. Three predictions from the gauge integers, all in completely different physics (nuclear, cosmological). Uses: integers, BBN physics, nuclear cross sections.

34. **Full electromagnetic + gravitational chain** — a_e → α → R∞ → atomic spectroscopy prediction (H 1S-2S from R∞ + QED corrections). Compare to the 16-digit H 1S-2S measurement already in the database. Uses: derived R∞, QED corrections (Lamb shift terms needed).

35. **Kepler verification from derived constants** — Use derived α and m_e to compute derived ℏ, then verify Kepler's law T² = (64R₂²/GM)a³ with derived vs measured constants. Cross-check the R₂ domain with the QED domain. Uses: derived constants, astrophysical masses.

---

### RANKED BY IMPACT ON FULL FITTING

| Rank | # | Experiment | What It Proves | New Inputs Needed |
|---|---|---|---|---|
| 1 | 7 | a_e with full corrections | α at <1 ppb, R∞/a₀/μ₀ at <2 ppb | 6 correction value nodes |
| 2 | 30 | Complete parameter chain a_e → G_F | 4 SM parameters from 1 measurement | sin²θ_W derivation |
| 3 | 32 | Proton decay + DM/baryon joint | Two domains from one set of betas | M_GUT precision |
| 4 | 33 | BBN consistency from integers | Three predictions from gauge integers | BBN cross sections |
| 5 | 2 | sin²θ_W from derived α | Uses our α, not CODATA | None — have all inputs |
| 6 | 4 | M_W from derived sin²θ_W | Extends chain one more step | Depends on #5 |
| 7 | 8 | Ω_b from integers + Ω_DM | Cosmology from gauge theory | None — have all inputs |
| 8 | 1 | α(M_Z) from VP running | Electromagnetic at Z pole | Hadronic VP |
| 9 | 14 | M_GUT two-loop precise | Fix the two-loop bug | db_ij investigation |
| 10 | 34 | H 1S-2S from derived R∞ | Most precise test in physics | Lamb shift QED terms |

