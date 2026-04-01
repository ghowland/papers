# HOWL-DATA-3: Database Consistency Verification

## Purpose

DATA-2 contains 123 entries (107 original + 16 Koide-derived). Many entries are related by known physical or mathematical identities. If the database is self-consistent, every identity holds to the precision of the least-precise input. If any identity fails, either an entry is wrong or the precision metadata is wrong. Either way, everything downstream is suspect until the failure is resolved.

DATA-3 is the verified database. It runs every testable internal relation, fixes any inconsistencies found, and becomes the sole reference for all future HOWL computation. DATA-2 is retired.

## Method

For each consistency relation:
1. Compute the left side from DATA-2 entries
2. Compute the right side from DATA-2 entries
3. Compare: relative difference |L − R| / |R|
4. Check: is the relative difference below 10^(−N) where N = min(source digits of all inputs)?
5. PASS if yes, FAIL if no

All computation in Fraction arithmetic. Square roots via mpmath at 50 digits converted back to Fraction for comparison. No floating point in the comparison logic.

## The Tests

### Group A: Mass Ratio Identities

**A1: m_p/m_e (direct) vs m_p / m_e (computed)**
- Direct entry: m_p/m_e = 1836.15267343 (13 sig figs)
- Computed: m_p(11 dig) / m_e(11 dig)
- Expected agreement: 11 digits (limited by m_p and m_e)
- This tests whether the ratio entry is consistent with the individual masses

**A2: m_μ/m_e (direct) vs m_μ / m_e (computed)**
- Direct entry: m_μ/m_e = 206.768282708 (10 sig figs, but entered from full-precision 200-digit value)
- Computed: m_μ(10 dig) / m_e(11 dig)
- Expected agreement: 10 digits

**A3: m_τ/m_e (direct) vs m_τ / m_e (computed)**
- Direct: 3477.23 (6 dig)
- Computed: m_τ(6 dig) / m_e(11 dig)
- Expected agreement: 6 digits

**A4: m_τ/m_μ (direct) vs m_τ / m_μ (computed)**
- Direct: 16.8170 (6 dig)
- Computed: m_τ(6 dig) / m_μ(10 dig)
- Expected agreement: 6 digits

**A5: m_n/m_p (direct) vs m_n / m_p (computed)**
- Direct: 1.00137841946 (11 dig)
- Computed: m_n(11 dig) / m_p(11 dig)
- Expected agreement: 11 digits

**A6: M_W/M_Z (direct) vs M_W / M_Z (computed)**
- Direct: 0.881361 (6 dig)
- Computed: M_W(6 dig) / M_Z(6 dig)
- Expected agreement: 6 digits

**A7: m_n − m_p (direct) vs m_n − m_p (computed)**
- Direct: 1.29333251 MeV (8 dig)
- Computed: m_n(11 dig) − m_p(11 dig)
- Expected agreement: 8 digits

### Group B: Derived Analytical Constants

**B1: R₂ vs π/4**
- R₂ entry vs π entry / 4
- Both at 105 digits
- Expected agreement: 101 digits (Q335 precision)

**B2: R₄ vs π²/32**
- R₄ entry vs π² entry / 32
- Expected agreement: 101 digits

**B3: 2π vs 8R₂**
- 2π entry vs 8 × R₂ entry
- Expected agreement: 101 digits

**B4: ζ(2) vs π²/6**
- ζ(2) entry vs π² / 6
- Expected agreement: 101 digits (but ζ(2) = π²/6 is exact, so this tests the Q335 numerators directly)

**B5: α/π (direct) vs α⁻¹ and π**
- Direct: α/π entry (12 dig)
- Computed: 1/(α⁻¹ × π)
- Expected agreement: 12 digits

**B6: φ vs (1 + √5)/2**
- φ entry vs (1 + √5 entry) / 2
- Expected agreement: 101 digits

### Group C: Physical Relations

**C1: R∞ vs α, m_e, c, h**
- R∞ = α² m_e c / (2h)
- R∞ entry: 10973731.568157 m⁻¹ (13 dig)
- α from α⁻¹ entry (12 dig), m_e (11 dig), c (exact), h (exact)
- Expected agreement: 11 digits (limited by m_e)
- This is HOW CODATA determines m_e, so it should be exact to the published precision

**C2: a₀ vs α and R∞**
- a₀ = 1/(4π R∞ α) (Bohr radius from Rydberg and α... actually a₀ = α/(4π R∞))
- More precisely: a₀ = ℏ/(m_e c α) = h/(2π m_e c α)
- Or equivalently: R∞ = α/(4π a₀) → a₀ = α/(4π R∞)
- a₀ entry: 5.29177210544 × 10⁻¹¹ m (12 dig)
- Expected agreement: 12 digits

**C3: μ₀ vs α, h, c, e**
- μ₀ = 2αh/(ce²) (exact relation in SI 2019, since h, c, e are exact)
- μ₀ entry: 1.25663706127 × 10⁻⁶ (12 dig)
- α from α⁻¹ (12 dig)
- Expected agreement: 12 digits

**C4: G_F relation (Fermi constant vs electroweak parameters)**
- At tree level: G_F/√2 = g²/(8M_W²) = πα/(2M_W² sin²θ_W)
- This involves the on-shell vs MS-bar scheme difference, so tree-level agreement is ~0.1-1%
- Test: G_F vs πα/(2√2 M_W² sin²θ_W) — expect agreement at ~1% (scheme dependent)
- This is a SOFT check, not an exact identity

### Group D: Koide Derived Entries (K1-K16)

**D1: K1 (Koide ratio) vs computation from m_e, m_μ, m_τ**
- K1 = 0.6666605115 (6 sig figs)
- Computed: (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)²
- Expected agreement: 6 digits (limited by m_τ)

**D2: K4 (a_leptons) vs computation from K1**
- K4 = 1.4142005052
- Computed: √(2 × (3 × K1 − 1))
- Expected agreement: 6 digits

**D3: K2, K3 (quark Koide ratios) vs quark masses**
- Same formula as D1 applied to (u,c,t) and (d,s,b)
- Expected agreement: 3 digits (limited by light quark masses)

**D4: K14, K15, K16 (scale parameters M) vs masses**
- M = (√m₁ + √m₂ + √m₃)/3
- Expected agreement: per sector precision

### Group E: Exact Defined Constants

**E1: N_A × k_B = R (gas constant)**
- R = 8.314462618... J/(mol·K) (exact in SI 2019)
- N_A (exact) × k_B (exact) should give exact R
- This tests whether our N_A and k_B entries are consistent with SI 2019

**E2: c × Δν_Cs relation to meter**
- The meter is defined via c and the second (via Δν_Cs), so c × (1/Δν_Cs) gives a length
- Not directly testable without the meter definition chain, skip this

**E3: h × Δν_Cs = defined energy**
- h × Δν_Cs = 6.62607015e-34 × 9192631770 = exact
- Compute and verify the product

### Group F: Cross-Checks Between Sections

**F1: m_D vs 2m_p − E_D (approximately)**
- Deuteron mass ≈ m_p + m_n − E_D (binding energy)
- m_D entry: 1875.61294500 MeV (12 dig)
- Computed: m_p + m_n − E_D = 938.27208943 + 939.56542194 − 2.22456614
- = 1875.61294523 MeV
- Expected agreement: 8 digits (limited by E_D at 8 dig)

**F2: m_He4 vs 2m_p + 2m_n − E_He4**
- We don't have E_He4 (He-4 binding energy) as a separate entry
- Skip unless we can compute it

**F3: H 1S-2S vs R∞**
- H 1S-2S = (3/4) × 2 × c × R∞ × (1 + corrections)
- At leading order: ν(1S-2S) = c R∞ (1 − 1/4) × 2 = (3/2) c R∞
- (3/2) × 299792458 × 10973731.568157 = ... should be close to 2466061413187018 Hz
- The Lamb shift, hyperfine, recoil, QED corrections modify this. Soft check at ~ppm level.

## Output Format

For each test:
```
  [PASS/FAIL] Test ID: Description
    Left:  value (source)
    Right: value (source)
    Relative difference: X.XXe-YY
    Required: < 1e-N (from N = min precision)
    Status: PASS/FAIL
```

If any FAIL: diagnose, fix the entry, document the fix.

Final output: verified entry count, any corrections applied, and the DATA-3 declaration.

## Fixes Applied (to be filled during execution)

Any entry that fails a consistency check is corrected here with:
- Which entry was wrong
- What the old value was
- What the new value is
- Which relation determined the correction
- The propagation: which downstream values change

## DATA-3 Declaration

After all tests pass (with any corrections applied): DATA-3 is the verified database with N entries, all internally consistent to the precision of their source measurements. All future HOWL computation references DATA-3. DATA-2 is retired.
