## DATA-3 Verification Results

32/32 tests pass. The database is clean.

### What Was Tested

Six groups covering every testable internal relation in the 123-entry database.

**Group A (9 tests): Mass ratios.** Every stored ratio entry (m_p/m_e, m_μ/m_e, m_τ/m_e, m_τ/m_μ, m_n/m_p, M_W/M_Z, m_n−m_p, m_H/M_Z, m_t/M_Z) was recomputed from the individual mass entries and compared. All agree to at or above the precision of the least-precise input. The best: m_n/m_p at 20 digits (both inputs at 11 digits, so the ratio has margin). The tightest: m_τ/m_μ at 5.8 digits against a 5-digit requirement (limited by m_τ at 6 sig figs).

**Group B (8 tests): Analytical constants.** The Q335 numerators were cross-checked against each other and against mpmath at 120-digit precision. R₂ = π/4 agrees to 102 digits. R₄ = π²/32 agrees to 102.4 digits. ζ(2) = π²/6 agrees to 101.5 digits. φ = (1+√5)/2 agrees to 101.4 digits. Three tests are exactly zero difference (2π = 8R₂, 2π = 2×π, both by construction). The Q335 basis is internally consistent at the full 101-digit capacity.

**Group C (4 tests + 1 soft): Physical relations.** These test whether the stored values of derived quantities match their defining formulas using other stored values. R∞ = α²m_ec/(2h) agrees to 11.3 digits (need 11). a₀ = ℏ/(m_ec α) agrees to 11.4 digits (need 11). μ₀ = 2αh/(ce²) agrees to 11.9 digits (need 11). m_D = m_p + m_n − E_D agrees to 9.9 digits (need 8). The H 1S-2S soft check gives 3.3 digits at leading order, consistent with the known ~500 ppm QED/Lamb shift corrections.

**Group D (5 tests): Koide entries.** All 16 Koide-derived entries (K1-K16) were recomputed from the source masses. The Koide ratios agree to 10+ digits for all three sectors. The amplitude and scale parameters agree to 4-10 digits, all above their required precision floors.

**Group E (6 tests): SI exact constants.** All seven SI defining constants (c, h, e, k_B, N_A, Δν_Cs) are confirmed to be stored at their exact SI 2019 values. Every comparison is exactly zero.

**Group F (annotation): Lattice ratios.** The lattice mass ratios (m_c/m_s = 11.783, m_b/m_c = 4.578, m_u/m_d = 0.485) are documented as INDEPENDENT data that cannot be cross-checked against the PDG individual quark masses. The discrepancy (up to 28%) is not a database error — it's the renormalization scale mismatch between PDG masses (evaluated at different scales: m_s at 2 GeV, m_c at m_c, m_b at m_b) and lattice ratios (evaluated at a common scale). This is a real finding from the consistency check: entries 41-43 are independent measurements, not derived quantities.

### What This Means

The database has no corruption. Every value that CAN be cross-checked IS consistent to the expected precision. The one genuine structural finding — lattice ratios are independent of PDG individual masses — is documented as an annotation, not a fix.

DATA-2 is promoted to DATA-3. All 123 entries carry forward unchanged. The verification script and its output become the DATA-3 certificate of consistency. All future HOWL computation references DATA-3.
