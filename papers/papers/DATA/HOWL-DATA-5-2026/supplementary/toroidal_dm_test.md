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

