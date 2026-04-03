## Notebook: The Modulus and Remainder — Complete Tracking Through Session 4

---

### 1. WHERE THIS STARTS

The series begins with R₂ = π/4. This is the remainder when you inscribe a circle in a square. The circle has area πr² = π(d/2)² = (π/4)d². The square has area d². The ratio is π/4. The remainder — what the square has that the circle doesn't — is 1 − π/4 = (4−π)/4.

But the series doesn't use "remainder" to mean "what's left over." It uses R₂ to mean the FRACTION of the square that the circle FILLS. R₂ = π/4 ≈ 0.7854. The circle fills 78.54% of its bounding square. This is the geometric conversion factor between circular and rectilinear geometry.

MATH-1 established that this same fraction appears in every domain where circular geometry meets rectilinear measurement: pipe flow, wire resistance, speaker cones, optical disc spots, antenna apertures, fiber modes, semiconductor wafers, capacitor plates, thermal radiation, sound intensity, drag force, orifice flow, lithography, Gaussian beams, Helmholtz resonance. Twenty-two equations documented. All use R₂ × d² for the circular area expressed in terms of the rectilinear bounding dimension d.

R₄ = π²/32 extends this to four dimensions. It is the volume fraction of the 4-ball in the 4-cube. R₄/R₂ = π/8. The pattern continues: Rₙ = (π^(n/2))/(2ⁿ × Γ(n/2 + 1)) for even n.

This is the starting point. The modulus/remainder concept develops from here through the entire series.

---

### 2. THE MODULUS IN GAUGE COUPLING RUNNING

Every gauge coupling runs according to:

1/α_i(μ₂) = 1/α_i(μ₁) − b_i × ln(μ₂/μ₁)/(2π)

The 2π in the denominator is 8R₂. This is the same geometric constant appearing in a completely different context — the virtual loop integral in quantum field theory. The loop is a closed circular path in momentum space. The 2π is the circumference of the unit circle. The factor 1/(2π) = 1/(8R₂) is the geometric conversion from the circular loop integral to the linear coupling change.

In MATH-1 language: Q = F × β × d² × Z becomes Δ(1/α) = ln(μ₂/μ₁) × (1/(8R₂)) × 1 × b_i. The "area" d² = 1 (dimensionless — the loop is in momentum space, not position space). The coordinator Z = b_i (the integer rule). The geometric factor β = 1/(8R₂) = 1/(2π). The driver F = ln(μ₂/μ₁).

The modulus here is R₂ acting as the conversion between the circular topology of the loop integral and the linear change in the coupling. Without R₂, you can't convert from loops to running. The 2π is not a convention — it is the geometry of the circle entering the physics through the loop.

---

### 3. THE MODULUS IN THE GAP RATIO

The gap ratio is (b₁ − b₂)/(b₂ − b₃). This is a ratio of differences of beta coefficients. The beta coefficients contain R₂ implicitly (through the loop integral normalization), but in the gap ratio, R₂ CANCELS. The gap ratio is a pure integer ratio: 218/115 for the SM, 38/27 for the CD.

This is the first R₂ cancellation in the gauge coupling context. The gap ratio is R₂-free because it is a RATIO of quantities that each contain R₂ in the same position. Like wire resistance × capacitance = ρε₀L/t (R₂ cancels), the gap ratio takes the R₂ out by dividing.

What remains after R₂ cancels is the pure integer content — the numerators and denominators that trace to the gauge group structure. 218 = 2 × 109. 115 = 5 × 23. 38 = 2 × 19. 27 = 3³. The gap ratio lives in the integer world because the geometric modulus has been divided out.

The measured gap ratio (1.358) is computed from measured couplings (α_EM, sin²θ_W, α_s) — Level 2 values. The theoretical gap ratios (218/115, 38/27) are Level 1 — computed from the gauge group integers. The comparison between them (SM: 40% miss, CD: 3.6% miss) is the comparison between the geometric modulus of the universe (measured couplings) and the integer structure (group theory). The gap ratio is where the modulus meets the integers.

---

### 4. THE MODULUS IN SIN²θ_W

sin²θ_W is the fraction of the electroweak coupling that goes into the weak sector. At tree level (GUT scale): sin²θ_W = 3/8 = 0.375. This is a pure Fraction — Level 1, determined by the SU(5) embedding geometry. No R₂.

Running from M_GUT to M_Z changes this to 0.22845 (one-loop) or 0.23133 (two-loop). The running carries R₂ through the loop integrals. The CORRECTION to sin²θ_W is:

Δsin²θ_W = 3/8 − sin²θ_W(M_Z) = 3/8 − 0.23133 = 0.14367

At one loop, this correction is exactly 15/104:

3/8 − 3/13 = (39 − 24)/104 = 15/104 = 0.14423

The 3/13 comes from N_gen/|b₂' numerator| = 3/13. This is another pure Fraction — the number of generations divided by the absolute value of the modified SU(2) beta numerator. No R₂.

The correction 15/104 is the MODULUS of the running — the total change accumulated over the entire M_Z → M_GUT range through 14 decades of energy. This modulus is R₂-free (it's a ratio of quantities each containing R₂). The integers 15 and 104 trace to the gauge group: 15 = 3 × 5 (generations × GUT normalization), 104 = 8 × 13 (crossing condition × CD SU(2) beta).

PHYS-34 found that the two-loop correction overshoots 3/13, giving sin²θ_W = 0.23133 > 0.23077 = 3/13 > 0.23122 (measured). The overshoot is 0.048% — within method uncertainty. The modulus at two loops is slightly different from the one-loop modulus because the two-loop terms carry additional R₂ factors (each two-loop b_ij entry is multiplied by α_j/(4π) = α_j/(16R₂)).

The hierarchy: tree-level sin²θ_W = 3/8 (pure Fraction, no R₂) → one-loop correction 15/104 (pure Fraction, R₂ cancels in ratio) → two-loop correction (small, carries R₂ through α_j/(16R₂)).

---

### 5. THE MODULUS IN THE BETA DECOMPOSITION

PHYS-32 decomposed b₃' = −20/3 into constituents:

- Gauge: −11 (from (11/3) × C₂(adj SU(3)) = (11/3) × 3)
- Fermion: +4 (from 3 generations × 4/3)
- Higgs: 0 (SU(3) singlet)
- CD: +1/3 (Dynkin formula)

Numerator sum: −33 + 12 + 0 + 1 = −20. Denominator: 3.

Each constituent is a Fraction. The gauge contribution −11 is an integer. The fermion contribution 4 is an integer. The CD contribution 1/3 is a Fraction. The Higgs contribution 0 is trivially exact.

These numbers are MODULI of the gauge group geometry. The 11 in the gauge contribution is the Yang-Mills one-loop coefficient — it appears because the SU(N) adjoint representation has a specific geometric structure (the Lie algebra) that produces exactly (11/3) × N when contracted through the loop integral. The 11 is not arbitrary — it comes from the trace over adjoint generators, which counts the degrees of freedom of the gauge field weighted by their coupling structure.

The 4/3 per generation is the fermion modulus — it counts how many colored Weyl fermions exist per generation (4: two in Q_L doublet, one u_R, one d_R) weighted by the Dynkin index (1/2) and the fermion coefficient (2/3). The 4/3 = (4 × 1/2 × 2/3) = (Weyl count × S₂ × coefficient).

The 1/3 for the CD is the VL modulus — (1/3) × dim(SU(2)) × S₂(fund SU(3)) = (1/3) × 2 × (1/2) = 1/3. The coefficient 1/3 (instead of 2/3 for chiral) is the VL pair's specific geometric structure: the Dirac pairing changes how the SU(3) index enters.

Every one of these numbers is a geometric modulus — a fraction that measures how much a specific representation "fills" the available gauge structure, analogous to R₂ measuring how much a circle fills its bounding square.

---

### 6. THE MODULUS IN THE KOIDE FORMULA

The Koide ratio K = sum_m / (sum_sqrt_m)² = 2/3 for leptons. This is a dimensionless ratio that measures the "shape" of the mass spectrum. K = 2/3 corresponds to a² = 2, where a is the amplitude parameter in the Koide decomposition.

The formula K = (1 + a²/2)/3 is a pure identity — it holds for ANY three numbers parameterized by (M, a, θ). The value K = 2/3 is special because it corresponds to a² = 2, which means the mass spectrum has a specific geometric shape: the three masses are distributed on a circle in √m space with a specific amplitude relative to the mean.

Think of it this way: three masses (m_e, m_mu, m_tau) define three points in √m space. Their mean is M = (√m_e + √m_mu + √m_tau)/3. Their deviation from the mean is parameterized by amplitude a and phase θ. The Koide formula says: the amplitude squared is exactly 2.

a² = 2 is a modulus. It measures how "spread out" the lepton masses are relative to their mean. If a² = 0, all three masses would be equal (m_e = m_mu = m_tau). If a² = 3, one mass would be zero. a² = 2 is in between — the masses are spread significantly but none is zero.

The REMAINDER in the Koide context: K = 2/3 means sum_m = (2/3)(sum_sqrt)². The remaining 1/3 is the "Koide deficit" — the amount by which the sum of masses falls short of (sum_sqrt)². This deficit is what makes the masses unequal. If K = 1 (no deficit), all masses would be equal. If K = 1/3 (maximum deficit), one mass would dominate.

PHYS-33 used K = 2/3 to predict m_tau = 1776.97 MeV from m_e and m_mu. Miss: 0.006% from measured 1776.86 MeV. The modulus a² = 2 is precise enough to predict the tau mass within experimental uncertainty. The other quadratic root (3.317 MeV) is the "shadow solution" — the mass that would give the same K = 2/3 with the same m_e and m_mu.

The Koide modulus (a² = 2) is Level 2 — it is measured, not derived. The series does not know WHY a² = 2 for leptons (a² = 2.39 for down quarks, a² = 3.09 for up quarks). If a derivation existed, it would reduce the parameter count by 1 (from 18 to 17, conditional). The modulus is observed but unexplained.

---

### 7. THE MODULUS IN THE TWO-LOOP b_ij MATRIX

The nine entries of the VL db_ij matrix are:

```
7/15    1/15    16/135
1/30    15/4    8/3
1/45    1        40/9
```

Each entry is a Fraction. Each is a geometric modulus — it measures how much the CD's (3,2,1/6) representation couples the i-th gauge group to the j-th gauge group at two loops.

The diagonal entries (7/15, 15/4, 40/9) measure self-coupling amplification — how much the CD's presence in gauge group i modifies the two-loop running of gauge group i through its own Casimir. The off-diagonal entries (1/15, 16/135, 1/30, 8/3, 1/45, 1) measure cross-coupling — how the CD's charge under gauge group j modifies the running of gauge group i.

The CRITICAL pitfall (N3) was about the diagonal modulus: the full Machacek-Vaughn diagonal is 2C_G + (10/3)C_R, but the 2C_G is the gauge self-coupling already in the SM b_ij. Adding a new fermion adds ONLY (10/3)C_R. The wrong modulus (39/4 = 2×2 + (10/3)×(3/4)×3) includes the gauge piece twice. The correct modulus (15/4 = (10/3)×(1/2)×3×(3/4)) counts only the fermion piece.

This is a modulus error — using the wrong geometric fraction for the representation's contribution. The series learned: the modulus of a new particle's contribution is NOT the full coupling formula; it is the INCREMENTAL coupling, because the gauge self-coupling is already accounted for.

---

### 8. THE MODULUS IN THE NO-THRESHOLD FINDING

PHYS-35 found that the no-threshold configuration (CD betas from M_Z, R₂-weighted running everywhere) outperforms the step-function threshold by 12×. The step function sets the CD's geometric modulus to zero below M_VL and to its full value above M_VL.

In modulus language: the step function rounds the CD's contribution from "suppressed" to "zero" below the inertia scale. The suppression factor is (μ/M_VL)², which for μ = 91 GeV and M_VL = 500 GeV is (91/500)² ≈ 0.033. The CD's modulus at M_Z is not zero — it is 3.3% of its full value. The step function rounds 3.3% to 0%. The no-threshold rounds it to 100%. The data says 100% is 12× closer to reality than 0%.

The remainder in the threshold context: the "decoupling remainder" is 1 − (μ/M_VL)², the fraction of the CD's contribution that is suppressed below threshold. At M_Z, this remainder is 96.7% — almost all of the CD's contribution is "missing" according to the suppression formula. The step function sets the remainder to 100% (full suppression). The no-threshold sets it to 0% (no suppression). The truth is between them but much closer to 0%.

The PHYS-35 addendum reframes this in vortex language: the CD's geometric overlaps with the gauge configurations are topological properties — moduli of the representation embedding. These moduli do not depend on energy. The CD is a (3,2,1/6) at every scale. Its Dynkin indices are 1/2 at every scale. Its hypercharge is 1/6 at every scale. The modulus is the SAME at M_Z as at M_GUT. What changes at M_VL is the excitation threshold — the energy cost to produce a real CD particle. But the geometric modulus (the representation's coupling to the gauge fields) is scale-independent.

This is the deepest statement about moduli in the series: the geometric modulus of a vortex is a property of its topology, not of the available energy. The running changes the coupling VALUES (Level 2), but the integer RULES (Level 1) — the moduli — are fixed by the representation.

---

### 9. THE MODULUS IN R₂ CANCELLATIONS

The cross-domain demo documents 7 R₂ cancellation identities. The pattern: when you take a RATIO of two R₂-containing quantities, R₂ cancels if both quantities have R₂ in the same structural position.

Wire resistance: R = ρL/(R₂d²). Capacitance: C = ε₀R₂d²/t. Product: RC = ρε₀L/t. R₂ cancels.

Josephson constant × von Klitzing constant: K_J × R_K = (2e/h)(h/e²) = 2/e. R₂ cancels (it enters through h = 2πℏ in both).

The MODULUS cancels in ratios where it appears symmetrically. What remains is the non-geometric physics — resistivity, permittivity, charge, length. The modulus is the geometric conversion factor; the remainder after cancellation is the physical content.

This is the same pattern as the gap ratio: R₂ enters through the loop integrals in each beta coefficient, but the gap ratio divides b₁−b₂ by b₂−b₃, and R₂ cancels, leaving pure integers.

And it is the same pattern as the Koide formula: K = sum_m/(sum_sqrt)² cancels the mass dimension, leaving a pure dimensionless modulus (2/3). The "geometric" content (the √m parameterization) divides out, leaving the shape parameter.

The series tracks three levels of modulus:

1. **R₂ = π/4** — the 2D circular-to-rectilinear modulus, appears in 22+ domains
2. **Integer Fractions (b_i, Δb_i, gap ratios)** — the gauge group moduli, appear in coupling running
3. **Koide a² = 2** — the mass spectrum modulus, appears in lepton masses

Each modulus measures how much of one geometric structure "fills" another. R₂ measures circle-in-square. The beta coefficients measure representation-in-gauge-group. Koide a² measures spread-in-mass-space.

---

### 10. THE MODULUS IN THE PROTON MASS

The proton's mass is 938.3 MeV. The current quark masses (u + u + d) total about 9.4 MeV — 1% of the proton mass. The remaining 99% is QCD binding energy — the energy of the confined gluon field and the kinetic energy of the quarks bouncing inside the confinement boundary.

The modulus here is the ratio: visible constituent mass / total mass = 1%. The remainder: pattern energy / total mass = 99%. The proton is a system where the geometric structure (the confined field pattern) dominates the inertia. The quarks are trace constituents in a vortex whose inertia is determined by the confinement geometry.

The confinement scale Λ_QCD is set by the integer b₃ = −7 through the running:

Λ_QCD = M_Z × exp(−2π/(b₃ × α_s(M_Z)))

The 2π = 8R₂ appears again. The confinement scale — which sets the proton mass — is determined by the integer modulus b₃ = −7 acting through the geometric modulus R₂ on the measured coupling α_s. The proton mass is literally: an integer (−7) × a geometric constant (R₂) × a measured value (α_s) → a mass scale (Λ_QCD) → the proton's inertia.

The decomposition of b₃ = −7 from PHYS-32: gauge (−11) + fermion (+4) + Higgs (0). The gauge modulus (−11) dominates. The Yang-Mills coefficient 11/3 times the adjoint Casimir 3 gives 11 — the geometric measure of how strongly the SU(3) gauge field antiscreens. This antiscreening is what produces confinement, which is what produces the proton mass, which is 99% of the visible mass of the universe.

The chain: R₂ (geometry) × 11 (Yang-Mills modulus) × 3 (SU(3) Casimir modulus) → b₃_gauge = −11 → confinement → proton mass → visible universe mass.

---

### 11. THE MODULUS IN THE GENERATION DEMOCRACY

PHYS-17 established generation democracy: each complete SM generation contributes (4/3, 4/3, 4/3) to the beta coefficients. The three values are equal. This means the fermion contribution to the gap ratio is zero: (4/3 − 4/3)/(4/3 − 4/3) = 0/0 (indeterminate). The gap ratio is set entirely by the gauge and Higgs contributions — the "boson problem."

The modulus 4/3 per generation is the fermion geometric fraction — how much one generation "fills" the available beta function space. The fact that this modulus is the SAME for all three gauge groups is generation democracy. The fact that EQUAL moduli cancel in ratios is the same R₂ cancellation pattern: when the modulus appears symmetrically, it divides out.

The boson problem says: the gap ratio (which determines unification quality) depends only on the bosonic moduli (gauge: −22/3 for SU(2), −11 for SU(3); Higgs: 1/6 for SU(2), 0 for SU(3)). The fermion modulus, despite dominating the individual betas in absolute value, contributes NOTHING to the ratio.

This is structurally identical to R₂ cancellation in RC circuits. The resistance has R₂ in the denominator. The capacitance has R₂ in the numerator. The product RC has no R₂. The geometric modulus is present in each piece but cancels in the combination. What remains is the non-geometric content: ρ, ε₀, L, t for circuits; gauge and Higgs structure for the gap ratio.

---

### 12. THE MODULUS IN THE CD'S Y = 1/6

The CD's hypercharge Y = 1/6 is the smallest hypercharge of any representation that modifies the gap ratio sufficiently for unification. PHYS-18 documented the 1/Y² scaling: the U(1) beta shift scales as Y², so Y = 1/6 gives Δb₁ = (2/5) × 3 × 2 × (1/36) = 1/15. This is tiny — the smallest one-loop shift. But the SU(2) shift (Δb₂ = 1) and SU(3) shift (Δb₃ = 1/3) are not Y-dependent and are much larger.

The hypercharge 1/6 is a modulus — it measures the CD's geometric overlap with the U(1) gauge configuration. The CD "fills" 1/36 of the U(1)² coupling space (Y² = 1/36). For comparison, the electron has Y = −1, filling 1/1 = 100%. The CD fills 2.8% of the electron's U(1) coupling.

The asymmetry between the CD's gauge couplings (Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3) reflects the different moduli of the (3,2,1/6) representation in each gauge group:

- SU(3): the CD is a fundamental triplet. It fills S₂ = 1/2 of the SU(3) Dynkin space. Large modulus.
- SU(2): the CD is a fundamental doublet. It fills S₂ = 1/2 of the SU(2) Dynkin space. Large modulus.
- U(1): the CD has Y = 1/6. It fills Y² = 1/36 of the U(1)² space. Tiny modulus.

The moduli (1/2, 1/2, 1/36) get multiplied by different coefficients (1/3, 2/3, 2/5) and different dimensions (2, 3, 6) to produce the shifts (1/3, 1, 1/15). The representation's geometric fractions, weighted by the group theory coefficients, determine how much the CD modifies each running.

---

### 13. THE MODULUS IN THE UNIFICATION PREDICTION

The α_s prediction chain: measured (α_EM, sin²θ_W) → extracted (1/α₁, 1/α₂) → running to M_GUT → predicted 1/α₃ → α_s.

At each step, a modulus enters:

**Extraction:** 1/α₂ = sin²θ_W × (1/α_EM). The modulus sin²θ_W converts the EM coupling into the weak coupling. It is the fraction of the EM coupling that goes to SU(2). Pitfall N1 was getting this modulus inverted (dividing instead of multiplying).

**Running:** 1/α_i(M_GUT) = 1/α_i(M_Z) − b_i × L. The modulus b_i scales the running per unit L. Different gauge groups run at different rates because their moduli (betas) are different.

**Crossing:** L_GUT = (1/α₁ − 1/α₂)/(b₁ − b₂). The crossing point depends on the RATIO of coupling differences to beta differences. R₂ cancels (present in both numerator and denominator through the loop integral normalization).

**Prediction:** α_s = 1/(1/α₃_predicted). The predicted coupling depends on how far 1/α₃ ran from its GUT starting point. The modulus b₃ determines the rate. The GUT starting point depends on where 1/α₁ and 1/α₂ crossed.

The prediction quality (0.33% miss) measures how well the integer moduli (b₁' = 25/6, b₂' = −13/6, b₃' = −20/3) combined with the measured moduli (α_EM, sin²θ_W) reproduce the independent measurement (α_s). The 0.33% miss is the REMAINDER — the part not captured by the one-loop + two-loop integer structure. This remainder could come from three-loop corrections, threshold effects, or physics beyond the current framework.

---

### 14. THE MODULUS IN THE SOLITON BOUNDARY

R5 says: crossing a soliton boundary changes the integer transformation law. The integer rules are moduli — they measure the geometric structure of the active vortex content. At each boundary, the moduli change by exact rational increments (Δb₁, Δb₂, Δb₃).

The complete boundary stack from phys24_boundaries.py is a sequence of modulus changes:

- Below m_e: no charged vortexes active. Moduli = 0 for EM running.
- At m_e: electron activates. EM modulus changes by −4/3 × Q² × N_c = −4/3 × 1 × 1.
- At m_mu: muon activates. EM modulus changes by another −4/3.
- Confinement wall: moduli undefined (non-perturbative).
- At m_c, m_b, m_t: quark thresholds. SU(3) modulus changes by +2/3 per flavor.
- At M_VL: CD activates. Moduli change by (1/15, 1, 1/3).
- At M_GUT: three moduli merge into one (unification).

Each boundary is a MODULUS CHANGE. The running between boundaries uses the current moduli. The running is smooth (R₂-weighted); the modulus changes are discrete (exact Fractions).

The PHYS-35 finding says: for the CD boundary, the modulus change should not be discrete. The CD's geometric overlap (its modulus) is a topological property that exists at all scales. The step-function boundary rounds the below-threshold modulus from "suppressed" to "zero." The no-threshold configuration uses the full modulus everywhere. The 12× improvement says the full modulus is a better approximation than zero.

In series language: the soliton boundary at M_VL is a boundary for EXCITATION (you can produce a real CD above M_VL), not for MODULUS (the CD's geometric coupling to the gauge groups exists at all scales). The modulus is a property of the vortex topology. The excitation threshold is a property of the vortex inertia (R3). These are different things.

---

### 15. THE MODULUS IN THE R₂ CANCELLATION REGISTRY

The cross-domain demo tracks 7 R₂ cancellation identities. The pattern, generalized:

When two quantities each containing the geometric modulus R₂ are combined in a ratio or product where R₂ appears in both numerator and denominator, R₂ cancels. What remains is the non-geometric physical content.

This is a general principle: MODULI CANCEL IN SYMMETRIC RATIOS.

Instances tracked in the series:

| Cancellation | Modulus that cancels | What remains |
|---|---|---|
| RC = ρε₀L/t | R₂ (circular area) | Material properties |
| K_J × R_K = 2/e | 2π = 8R₂ (in h) | Pure charge ratio |
| G₀ × R_K = 2 | 2π = 8R₂ (in h) | Pure number |
| Gap ratio 218/115 | 1/(2π) in each beta | Pure integers |
| Fermion gap = 0/0 | 4/3 per gen (democracy) | Boson structure |
| Koide K = 2/3 | Mass dimension (√m param) | Shape parameter a² |
| sin²θ_W correction 15/104 | R₂ in running | Pure group theory Fractions |

The principle: the modulus enters through the geometry of the computation (circular cross-sections, loop integrals, mass parameterizations). It cancels when you form ratios that are purely about the STRUCTURE (integers, shapes, relationships). The modulus is the bridge between geometry and measurement. The remainder after cancellation is the physics.

---

### 16. THE MODULUS HIERARCHY

The series has identified moduli at multiple scales:

**Level 0: Pure geometry.** R₂ = π/4 (2D), R₄ = π²/32 (4D). These are mathematical constants — volume fractions of n-balls in n-cubes. They are exact, transcendental, and universal. They enter every computation that involves circular or spherical geometry.

**Level 1: Group theory.** Beta coefficients (41/10, −19/6, −7), Casimirs (4/3, 3/4, 3, 2), Dynkin indices (1/2), dimensions (3, 2), hypercharges (1/6, 2/3, −1/3, −1/2, −1). These are exact rational numbers determined by the gauge group structure. They enter every computation that involves representations of SU(3)×SU(2)×U(1).

**Level 2: Measured parameters.** α_EM, sin²θ_W, α_s, the quark and lepton masses, the CKM angles. These are the moduli supplied by the universe. They enter every computation that connects theory to observation.

**Level 3: Derived ratios.** The gap ratio, the Koide K, the sin²θ_W correction, the α_s prediction. These are combinations of Level 0, 1, and 2 moduli. In these combinations, some moduli cancel (R₂, generation democracy) and others remain (the integers, the measurements).

The hierarchy:
- Level 0 moduli are the same in every domain (R₂ in pipes, wires, loops).
- Level 1 moduli are the same in every computation within one gauge group (b₃ = −7 in all SU(3) running).
- Level 2 moduli are the same at one energy scale (α_s = 0.1180 at M_Z).
- Level 3 moduli are the output — the predictions that test the framework.

---

### 17. THE MODULUS AND THE VORTEX FRAMEWORK

The PHYS-35 addendum introduces the vortex view: everything is vortexes (R4), mass is inertia (R3), boundaries change the integer rules (R5). In this framework, every modulus is a property of a vortex's geometric embedding:

- R₂ = the modulus of circular geometry (the vortex IS circular — energy circulates)
- b_i = the modulus of the vortex's coupling to gauge group i (determined by representation)
- Δb_i = the modulus change when a new vortex activates at a boundary
- K = 2/3 = the modulus of the lepton mass spectrum (the shape of the three-vortex system)
- sin²θ_W = the modulus of the EW mixing (the fraction of EM coupling in SU(2))

Every modulus measures an OVERLAP — how much one geometric structure fits within another. R₂ measures circle-in-square. Beta coefficients measure representation-in-gauge-group. sin²θ_W measures weak-in-electromagnetic. Koide K measures mass-spread-in-mass-space.

The vortex framework says: these are all the same kind of thing. A vortex has a geometry. The geometry determines how it overlaps with other vortexes. The overlap is the modulus. The modulus determines the physics.

---

### 18. THE MODULUS AND THE NO-THRESHOLD PRINCIPLE

The deepest insight from Session 4: the modulus of a vortex is a topological property that does not depend on energy. The CD is a (3,2,1/6) at every scale. Its moduli (Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3) are properties of its representation, not of the available energy.

The step-function threshold says: below M_VL, the moduli are zero. Above M_VL, the moduli are their full values. This is a MODULUS DISCONTINUITY at the boundary.

The no-threshold configuration says: the moduli are their full values everywhere. No discontinuity.

The data says: no discontinuity gives 12× better predictions.

The interpretation: moduli do not have discontinuities. They are topological invariants of the vortex embedding. The boundary at M_VL is an INERTIA threshold (the energy cost to excite the vortex), not a MODULUS threshold (the geometric coupling to gauge fields). Inertia changes at the boundary. The modulus does not.

This is the series' strongest statement about moduli: they are continuous, topological, scale-independent properties of vortex geometry. They determine the integer rules. They cancel in symmetric ratios. They are the bridge between the mathematical structure (Level 0/1) and the physical measurements (Level 2). And they do not switch off at energy thresholds.

---

### 19. WHAT DATA-5 SHOULD CAPTURE

Every modulus tracked in the series:

| Modulus | Value | Type | Where it appears |
|---|---|---|---|
| R₂ | π/4 | Level 0 | 22+ engineering domains, loop integrals |
| R₄ | π²/32 | Level 0 | QED loop corrections, 4D geometry |
| b₁_SM | 41/10 | Level 1 | U(1) running |
| b₂_SM | −19/6 | Level 1 | SU(2) running |
| b₃_SM | −7 | Level 1 | SU(3) running, confinement scale |
| Δb₁_CD | 1/15 | Level 1 | CD U(1) modulus |
| Δb₂_CD | 1 | Level 1 | CD SU(2) modulus |
| Δb₃_CD | 1/3 | Level 1 | CD SU(3) modulus |
| 11 | 11 | Level 1 | Yang-Mills coefficient |
| 4/3 | 4/3 | Level 1 | Generation democracy modulus |
| 3/5 | 3/5 | Level 1 | GUT normalization modulus (k₁) |
| 1/2 | 1/2 | Level 1 | Dynkin index (fundamental of any SU(N)) |
| 4/3, 3/4 | — | Level 1 | Fundamental Casimirs SU(3), SU(2) |
| 1/6 | 1/6 | Level 1 | CD hypercharge |
| K = 2/3 | 2/3 | Level 1 (identity) / Level 2 (value) | Koide lepton modulus |
| a² = 2 | 2 | Level 2 | Koide amplitude modulus |
| sin²θ_W | 0.23122 | Level 2 | EW mixing modulus |
| 3/8 | 3/8 | Level 1 | Tree-level sin²θ_W |
| 3/13 | 3/13 | Level 1 (conditional) | One-loop sin²θ_W limit |
| 15/104 | 15/104 | Level 1 | sin²θ_W running modulus |
| 218/115 | 218/115 | Level 1 | SM gap ratio |
| 38/27 | 38/27 | Level 1 | CD gap ratio |
| 9 VL b_ij entries | (table) | Level 1 | Two-loop cross-coupling moduli |
| C_T = −1/12 | −1/12 | Level 1 | Triplet Higgs threshold modulus |
| C_Sigma = −1/6 | −1/6 | Level 1 | Sigma threshold modulus |

Plus the 7 R₂ cancellation identities, plus the observation that moduli are topological (scale-independent) per the no-threshold finding.

---

### 20. THE UNIFYING PRINCIPLE

Across the entire series, from MATH-1 through PHYS-35:

**A modulus is the fraction of one geometric structure that fits within another.**

R₂ = π/4: the fraction of the square filled by its inscribed circle.
b₃ = −7: the net fraction of the SU(3) coupling space filled by all active vortexes.
Δb₂ = 1: the fraction of the SU(2) coupling space filled by the CD vortex.
K = 2/3: the fraction of the mass-sum space filled by the root-mass-sum squared.
sin²θ_W = 0.231: the fraction of the EM coupling space filled by the weak coupling.

Every modulus is a FILLING FRACTION. Every remainder is what's LEFT. The physics lives in the interplay between what fills and what remains. The integer rules determine the filling. The measured values determine the scale. The moduli — the geometric fractions — are the bridge between them.

The no-threshold finding says: the filling fractions do not depend on energy. They are topological properties of the vortex geometry. A (3,2,1/6) vortex fills 1/15 of the U(1) beta space, 1 of the SU(2) beta space, and 1/3 of the SU(3) beta space — at every energy, at every scale, always. The only thing that changes at a threshold is whether you can EXCITE the vortex. The filling fraction — the modulus — is permanent.

This is what R₂ taught the series from the beginning: π/4 is the same in pipes, wires, speakers, discs, antennas, fibers, wafers, beams, and loop integrals. The modulus is universal. The coordinator Z (velocity, resistivity, beta coefficient) is what makes each domain different. The modulus is what makes them the same.

---

*End of notebook. The modulus concept threads through the entire series: R₂ as the universal geometric conversion, beta coefficients as gauge group filling fractions, Koide K as mass spectrum shape, sin²θ_W as electroweak mixing fraction, and the no-threshold finding as the statement that moduli are topological and scale-independent. DATA-5 should store every identified modulus with its Level classification, its cancellation behavior, and its connection to the vortex framework.*

---

## Supporting Appendix Tables for: The Modulus and Remainder

---

### TABLE MR.1: THE R₂ FAMILY — GEOMETRIC FILLING FRACTIONS BY DIMENSION

| n | Rₙ | Exact form | Decimal | Meaning | Series use |
|---|---|---|---|---|---|
| 1 | R₁ = 1 | 1 | 1.0 | Line fills its bounding line | Trivial |
| 2 | R₂ = π/4 | π/4 | 0.78540 | Circle fills bounding square | 22+ domains, loop integrals |
| 3 | R₃ = π/6 | π/6 | 0.52360 | Sphere fills bounding cube | Volume calculations |
| 4 | R₄ = π²/32 | π²/32 | 0.30843 | 4-ball fills 4-cube | QED loop corrections |
| 5 | R₅ = π²/60 | π²/60 | 0.16449 | 5-ball fills 5-cube | Not used in series |
| 6 | R₆ = π³/384 | π³/384 | 0.08075 | 6-ball fills 6-cube | Not used in series |

General formula: Rₙ = (π^(n/2))/(2ⁿ × Γ(n/2 + 1)) for even n.

Key ratios: R₄/R₂ = π/8. R₆/R₄ = π/12. Each step multiplies by π/(4+2k).

---

### TABLE MR.2: THE 22 R₂ EQUATIONS — MODULUS IN ENGINEERING DOMAINS

| # | Domain | Equation | Coordinator Z | R₂ role | Precision |
|---|---|---|---|---|---|
| 1 | Pipe flow | Q = R₂d²v | velocity v | Area conversion | 0.05% |
| 2 | Drag force | F = ½ρv²R₂d²Cₐ | drag coeff Cₐ | Frontal area | 1% |
| 3 | Orifice flow | q = CₐR₂d²√(2ΔP/ρ) | discharge Cₐ | Orifice area | 0.5% |
| 4 | Capacitor | C = ε₀R₂d²/t | permittivity ε | Plate area | pF |
| 5 | Poynting flux | P = SR₂d² | irradiance S | Beam cross-section | 0.1 dB |
| 6 | Antenna aperture | A = ηR₂D² | efficiency η | Dish area | Calibrated |
| 7 | Beam cross-section | A = R₂d² | none (pure geometry) | Direct area | μm |
| 8 | Thermal radiation | Q = εσT⁴R₂d² | emissivity ε | Radiating area | 1% |
| 9 | Sound intensity | I = P/(16R₂r²) | 1/r² spreading | Spherical shell area | 0.5 dB |
| 10 | Wire resistance | R = ρL/(R₂d²) | resistivity ρ | Conductor area | 0.1% |
| 11 | Speaker cone | Sₐ = R₂d²_eff | none (pure geometry) | Cone area | 5% |
| 12 | Fiber mode | A = R₂MFD² | mode confinement | Mode area | 5% |
| 13 | Disc spot | A = R₂(1.22λ/NA)² | diffraction | Spot area | Standard |
| 14 | Wafer area | A = R₂D² | none (pure geometry) | Wafer area | Exact |
| 15 | Gaussian beam | A = R₂w₀² | beam parameter | Waist area | μm |
| 16 | Hagen-Poiseuille | Q = R₂d⁴ΔP/(32μL) | viscosity μ | Pipe area × d² | 1% |
| 17 | Ion implant | N = dose/√(8R₂σ²)exp(..) | straggle σ | Gaussian norm | 5% |
| 18 | Helmholtz resonance | f = (c/(8R₂))√(R₂d²/(lV)) | port geometry | Port area + normalization | 2 Hz |
| 19 | Airy diffraction | θ = j₁₁/(4R₂)λ/D | Bessel zero j₁₁ | Circular aperture | Fundamental |
| 20 | Rayleigh scattering | σ ~ (8R₂/λ)⁴r⁶ | polarizability | Scattering cross-section | 0.8 dB/km/μm⁴ |
| 21 | Free-space path loss | FSPL = (16R₂d/λ)² | distance/wavelength | Spherical spreading | Link budget |
| 22 | Radar cross-section | σ = 16R₂A²/λ² | plate area A | Scattering area | RCS |
| **23** | **Gauge coupling running** | **Δ(1/αᵢ) = bᵢL/(8R₂)** | **beta coefficient bᵢ** | **Loop integral** | **0.33% (α_s)** |

Equation #23 added by Session 4. The loop integral normalization 1/(2π) = 1/(8R₂) is the same geometric conversion factor.

---

### TABLE MR.3: R₂ CANCELLATION REGISTRY

| # | Product or ratio | Formula | R₂ status | What remains | Precision |
|---|---|---|---|---|---|
| 1 | Wire R × Capacitor C | ρL/(R₂d²) × ε₀R₂d²/t | CANCELS | ρε₀L/t | Derived |
| 2 | K_J × R_K | (2e/h)(h/e²) | CANCELS | 2/e | 10⁻⁸ |
| 3 | G₀ × R_K | (2e²/h)(h/e²) | CANCELS | 2 | Exact |
| 4 | Rydberg R_∞ | α²m_ec/(2h) | CANCELS | Via 2h = 16R₂ℏ | 13 digits |
| 5 | a₀ × α | ℏ/(m_ec) | CANCELS | Compton/2π | 12 digits |
| 6 | Hartree energy | m_ec²α² | R₂-FREE | No R₂ enters | 10 digits |
| 7 | Φ₀²/R_K | h²/e² × e²/h | REAPPEARS | h (contains 2π) | Exact |
| **8** | **Gap ratio** | **(b₁−b₂)/(b₂−b₃)** | **CANCELS** | **Pure integers** | **Exact** |
| **9** | **Fermion gap** | **(4/3−4/3)/(4/3−4/3)** | **CANCELS** | **0/0 (boson problem)** | **Exact** |
| **10** | **sin²θ_W correction** | **3/8 − 3/13** | **CANCELS** | **15/104** | **Exact** |

Items 8–10 added by Session 4. The pattern: R₂ (or the generation democracy modulus 4/3) cancels in symmetric ratios, leaving pure integer content.

---

### TABLE MR.4: LEVEL 0 MODULI — PURE GEOMETRY

| Modulus | Value | Fraction | Transcendental? | Where it enters |
|---|---|---|---|---|
| R₂ | π/4 | Fraction(p_pi, Q)/4 | Yes (π) | Every circular-to-rectilinear conversion |
| R₄ | π²/32 | Fraction(p_pi2, Q)/32 | Yes (π²) | QED two-loop, 4D geometry |
| 2π = 8R₂ | 6.28318... | 8 × R₂ | Yes | Loop integral normalization, Fourier |
| 4π = 16R₂ | 12.56637... | 16 × R₂ | Yes | Solid angle, 4π steradians |
| j₁₁ = 3.832 | 3.83171... | Bessel zero | Yes | Airy diffraction, fiber cutoff |
| j₀₁ = 2.405 | 2.40483... | Bessel zero | Yes | Fiber single-mode cutoff |
| C_c = π/(π+2) | 0.61102... | 4R₂/(4R₂+2) | Yes | Vena contracta |
| 1/√(2π) = 1/√(8R₂) | 0.39894... | Gaussian norm | Yes | Probability, statistics |

These moduli are universal — they appear identically in every domain. They are Level 0 because they derive from pure mathematics, not from any physical theory.

---

### TABLE MR.5: LEVEL 1 MODULI — GAUGE GROUP STRUCTURE

| Modulus | Value | Fraction | Origin | First appears | Papers |
|---|---|---|---|---|---|
| b₁_SM | 41/10 | Fraction(41, 10) | U(1) hypercharge sum | PHYS-13 | 26, 27, 30, 34 |
| b₂_SM | −19/6 | Fraction(-19, 6) | SU(2) gauge + fermion + Higgs | PHYS-13 | 26, 27, 30, 32, 34 |
| b₃_SM | −7 | Fraction(-7, 1) | SU(3) gauge + fermion | PHYS-13 | 26, 30, 32 |
| Δb₁_CD | 1/15 | Fraction(1, 15) | (2/5)×3×2×(1/36) | PHYS-15 | 26, 28, 30, 34 |
| Δb₂_CD | 1 | Fraction(1, 1) | (2/3)×3×(1/2) | PHYS-15 | 26, 28, 30, 34 |
| Δb₃_CD | 1/3 | Fraction(1, 3) | (1/3)×2×(1/2) | PHYS-15 | 26, 28, 30, 32 |
| b₁' = b₁+Δb₁ | 25/6 | Fraction(25, 6) | Modified U(1) | PHYS-26 | 27, 30, 34 |
| b₂' = b₂+Δb₂ | −13/6 | Fraction(-13, 6) | Modified SU(2) | PHYS-26 | 27, 30, 34 |
| b₃' = b₃+Δb₃ | −20/3 | Fraction(-20, 3) | Modified SU(3) | PHYS-26 | 30, 32 |
| k₁ | 3/5 | Fraction(3, 5) | SU(5) normalization | PHYS-26 | 27, 34 |
| k₁⁻¹ | 5/3 | Fraction(5, 3) | 1/k₁ | PHYS-26 | 27, 34 |
| S₂(fund) | 1/2 | Fraction(1, 2) | Dynkin index | PHYS-26 | 28, 32 |
| C₂(fund SU(3)) | 4/3 | Fraction(4, 3) | (N²−1)/(2N) at N=3 | PHYS-28 | 32 |
| C₂(fund SU(2)) | 3/4 | Fraction(3, 4) | (N²−1)/(2N) at N=2 | PHYS-28 | 32 |
| C₂(adj SU(3)) | 3 | Fraction(3, 1) | N at N=3 | PHYS-32 | 32 |
| C₂(adj SU(2)) | 2 | Fraction(2, 1) | N at N=2 | PHYS-32 | 32 |
| 11/3 | 11/3 | Fraction(11, 3) | Yang-Mills one-loop coefficient | PHYS-32 | 32 |
| 4/3 per gen | 4/3 | Fraction(4, 3) | Generation democracy | PHYS-17 | 32 |
| Y_CD | 1/6 | Fraction(1, 6) | CD hypercharge | PHYS-15 | 18, 26, 28 |
| N_gen | 3 | Fraction(3, 1) | Generation count | PHYS-17 | 26, 32 |

All exact Fractions. All determined by the gauge group SU(3)×SU(2)×U(1) and the particle content. No measurement needed.

---

### TABLE MR.6: LEVEL 1 MODULI — DERIVED RATIOS

| Modulus | Value | Fraction | Derivation | Papers |
|---|---|---|---|---|
| Gap ratio (SM) | 218/115 | Fraction(218, 115) | (b₁−b₂)/(b₂−b₃) | PHYS-13 |
| Gap ratio (CD) | 38/27 | Fraction(38, 27) | (b₁'−b₂')/(b₂'−b₃') | PHYS-13 |
| Gap ratio (MSSM) | 7/5 | Fraction(7, 5) | Convention check | PHYS-26 |
| sin²θ_W (tree) | 3/8 | Fraction(3, 8) | SU(5) at M_GUT | PHYS-27 |
| sin²θ_W (1-loop limit) | 3/13 | Fraction(3, 13) | N_gen/\|b₂' num\| | PHYS-27 |
| Running correction | 15/104 | Fraction(15, 104) | 3/8 − 3/13 | PHYS-27 |
| b_EM (CD) | 43/9 | Fraction(43, 9) | (5/3)b₁' + b₂' | PHYS-34 |
| C_T | −1/12 | Fraction(-1, 12) | Triplet Higgs threshold | PHYS-29 |
| C_Sigma | −1/6 | Fraction(-1, 6) | Sigma combined threshold | PHYS-29 |
| C_total | −1/4 | Fraction(-1, 4) | C_T + C_Sigma | PHYS-29 |
| n_f(crit) for SU(3) | 33/4 | Fraction(33, 4) | b₃ = 0 at n_f = 33/4 | PHYS-32 |

All exact. All derivable from Level 1 inputs. R₂ cancels in every ratio.

---

### TABLE MR.7: LEVEL 2 MODULI — MEASURED PARAMETERS

| Modulus | Value | DATA-4 ID | Unit | Digits | Role |
|---|---|---|---|---|---|
| α_EM⁻¹ | 137.036 | B1 | dimensionless | 12 | EM coupling scale |
| sin²θ_W | 0.23122 | B11 | dimensionless | 5 | EW mixing fraction |
| α_s | 0.1180 | B12 | dimensionless | 4 | Strong coupling scale |
| m_e | 0.51100 MeV | B2 | MeV | 11 | Lightest charged vortex |
| m_mu | 105.658 MeV | B3 | MeV | 10 | Second charged lepton |
| m_tau | 1776.86 MeV | B4 | MeV | 6 | Third charged lepton |
| K(leptons) | 0.66666 | K8 | dimensionless | 10 | Koide shape parameter |
| a²(leptons) | 1.99996 | — | dimensionless | 5 | Koide amplitude squared |
| M_Z | 91187.6 MeV | C1 | MeV | 6 | EW scale reference |

These are the moduli the universe supplies. Each enters the computation chain at specific points. Each is a filling fraction: sin²θ_W is the weak fraction of EM; α_s is the strong coupling fraction; K is the mass-sum fraction.

---

### TABLE MR.8: LEVEL 3 MODULI — PREDICTIONS (DERIVED FROM LEVELS 0+1+2)

| Prediction | Value | Miss from measured | Moduli used | Paper |
|---|---|---|---|---|
| α_s (1-loop, no thresh) | 0.10769 | 8.74% | b₁', b₂', b₃', α_EM, sin²θ_W | PHYS-30 |
| α_s (2-loop SM b_ij) | 0.11753 | 0.40% | + SM b_ij | PHYS-30 |
| α_s (2-loop full b_ij) | 0.11838 | **0.33%** | + VL db_ij | PHYS-30 |
| sin²θ_W (1-loop) | 0.22845 | 1.20% | b₁', b₂', b₃', α_EM, α_s | PHYS-27 |
| sin²θ_W (2-loop SM) | 0.23108 | 0.060% | + SM b_ij | PHYS-34 |
| sin²θ_W (2-loop full) | 0.23133 | **0.048%** | + VL db_ij | PHYS-34 |
| m_tau (Koide, K=2/3) | 1776.97 MeV | **0.006%** | m_e, m_mu, K=2/3 | PHYS-33 |
| Δ (1-loop, M_VL=500) | −1.17 | — | One-loop miss | PHYS-28 |
| Δ (2-loop, full b_ij) | −0.04 | — | Near-zero (no-thresh) | PHYS-30 |

The miss is the REMAINDER — the fraction not captured by the integer moduli acting through the geometric moduli on the measured inputs.

---

### TABLE MR.9: THE BETA DECOMPOSITION AS MODULUS ACCOUNTING

**SU(3): b₃' = −20/3**

| Constituent | Modulus value | Fraction | × denom 3 | Physical origin |
|---|---|---|---|---|
| Gauge | −11 | Fraction(-11) | −33 | (11/3) × C₂(adj) = (11/3) × 3 |
| Fermion (3 gen) | +4 | Fraction(4) | +12 | 3 × (4/3) from 4 Weyl triplets per gen |
| Higgs | 0 | Fraction(0) | 0 | SU(3) singlet |
| CD | +1/3 | Fraction(1, 3) | +1 | VL formula: (1/3)×2×(1/2) |
| **Total numerator** | | | **−20** | −33 + 12 + 0 + 1 |
| **b₃'** | **−20/3** | **Fraction(-20, 3)** | | |

**SU(2): b₂' = −13/6**

| Constituent | Modulus value | Fraction | × denom 6 | Physical origin |
|---|---|---|---|---|
| Gauge | −22/3 | Fraction(-22, 3) | −44 | (11/3) × C₂(adj) = (11/3) × 2 |
| Fermion (3 gen) | +4 | Fraction(4) | +24 | 3 × (4/3) from 4 Weyl doublets per gen |
| Higgs | +1/6 | Fraction(1, 6) | +1 | (1/3) × S₂(fund) = (1/3) × (1/2) |
| CD | +1 | Fraction(1) | +6 | VL formula: (2/3)×3×(1/2) |
| **Total numerator** | | | **−13** | −44 + 24 + 1 + 6 |
| **b₂'** | **−13/6** | **Fraction(-13, 6)** | | |

Each constituent is a geometric modulus — a filling fraction weighted by its group theory coefficients.

---

### TABLE MR.10: THE VL TWO-LOOP MATRIX — NINE CROSS-COUPLING MODULI

| Entry | Fraction | Decimal | Formula | What it measures |
|---|---|---|---|---|
| db₁₁ | 7/15 | 0.467 | (10/3)×S₁×(C₂(3)+C₂(2)+k₁Y²) | CD self-coupling in U(1) |
| db₁₂ | 1/15 | 0.067 | (4/3)×S₁×C₂(2) | CD cross-coupling U(1)←SU(2) |
| db₁₃ | 16/135 | 0.119 | (4/3)×S₁×C₂(3) | CD cross-coupling U(1)←SU(3) |
| db₂₁ | 1/30 | 0.033 | (4/3)×S₂(2)×d₃×k₁Y² | CD cross-coupling SU(2)←U(1) |
| db₂₂ | 15/4 | 3.750 | (10/3)×S₂(2)×d₃×C₂(2) | CD self-coupling in SU(2) |
| db₂₃ | 8/3 | 2.667 | (4/3)×S₂(2)×d₃×C₂(3) | CD cross-coupling SU(2)←SU(3) |
| db₃₁ | 1/45 | 0.022 | (4/3)×S₂(3)×d₂×k₁Y² | CD cross-coupling SU(3)←U(1) |
| db₃₂ | 1 | 1.000 | (4/3)×S₂(3)×d₂×C₂(2) | CD cross-coupling SU(3)←SU(2) |
| db₃₃ | 40/9 | 4.444 | (10/3)×S₂(3)×d₂×C₂(3) | CD self-coupling in SU(3) |

Pitfall N3: db₂₂ = 15/4 (fermion only), NOT 39/4 (with gauge 2C_G). The gauge self-coupling modulus is already in SM b_ij.

---

### TABLE MR.11: MODULUS CANCELLATION PATTERNS

| Pattern | Where observed | Modulus that cancels | What survives |
|---|---|---|---|
| R₂ in ratio of circular areas | RC product, K_J×R_K | R₂ = π/4 | Material/charge constants |
| 2π = 8R₂ in ratio of loop quantities | Gap ratio, sin²θ_W correction | 1/(2π) in each beta | Pure integer Fractions |
| 4/3 per gen in gap numerator and denominator | Boson problem | Generation democracy modulus | Gauge + Higgs structure |
| Mass dimension in Koide K | K = sum_m/(sum_√m)² | [MeV] dimension | Dimensionless shape a² |
| (c/v)² in amplification | Toroidal DM decomposition | Velocity ratio | (22/13)π (Track B, PARKED) |

The universal rule: when a modulus appears in both numerator and denominator of a ratio, it cancels, revealing the non-geometric content underneath.

---

### TABLE MR.12: THE MODULUS HIERARCHY

| Level | Name | Content | Examples | Determined by |
|---|---|---|---|---|
| 0 | Pure geometry | Transcendental constants from n-ball/n-cube ratios | R₂ = π/4, R₄ = π²/32, j₁₁ = 3.832 | Mathematics |
| 1 | Group theory | Exact Fractions from gauge group representations | b₃ = −7, Δb₂ = 1, k₁ = 3/5, 218/115 | SU(3)×SU(2)×U(1) structure |
| 2 | Measured parameters | Values supplied by the universe | α_EM, sin²θ_W, α_s, lepton masses | Experiment |
| 3 | Predictions | Combinations of L0+L1+L2 | α_s = 0.11838, sin²θ_W = 0.23133 | Computation |

Level 0 is the same in all domains. Level 1 is the same in all computations within one gauge theory. Level 2 is the same at one energy scale. Level 3 is the test output.

---

### TABLE MR.13: THE NO-THRESHOLD PRINCIPLE — MODULUS vs INERTIA

| Property | At μ < M_VL | At μ > M_VL | Scale-dependent? |
|---|---|---|---|
| CD representation (3,2,1/6) | (3,2,1/6) | (3,2,1/6) | **NO** — topological |
| Δb₁ = 1/15 | 1/15 | 1/15 | **NO** — topological |
| Δb₂ = 1 | 1 | 1 | **NO** — topological |
| Δb₃ = 1/3 | 1/3 | 1/3 | **NO** — topological |
| S₂(fund) = 1/2 | 1/2 | 1/2 | **NO** — topological |
| Y = 1/6 | 1/6 | 1/6 | **NO** — topological |
| Can produce real CD particle? | No | Yes | **YES** — energy-dependent |
| Virtual contribution to running | Suppressed by (μ/M_VL)² | Full | **YES** — energy-dependent |
| Step-function approximation | Sets modulus to 0 | Sets modulus to full | Creates artificial discontinuity |
| No-threshold treatment | Uses full modulus | Uses full modulus | No discontinuity → 12× better |

The modulus is the geometric filling fraction. The inertia is the excitation cost. PHYS-35 says: treat the modulus as continuous. Only the inertia has a threshold.

---

### TABLE MR.14: MODULUS TRACKING ACROSS THE FULL DERIVATION CHAIN

| Step | Input moduli | Operation | Output | R₂ present? |
|---|---|---|---|---|
| 1. Extract couplings | α_EM (L2), sin²θ_W (L2) | 1/α₂ = sin²θ_W × α_EM⁻¹ | 1/α₁, 1/α₂ | No (ratio) |
| 2. One-loop crossing | 1/α₁, 1/α₂ (L2), b₁', b₂' (L1) | L_GUT = (1/α₁−1/α₂)/(b₁'−b₂') | L_GUT | No (ratio) |
| 3. One-loop running | L_GUT, b₃' (L1), 1/(2π) (L0) | 1/α₃(GUT) = 1/α₃(M_Z) − b₃'L | 1/α₃ at GUT | Yes — via L = ln(μ/M_Z)/(8R₂) |
| 4. Two-loop correction | b_ij (L1), α_j (L2), 1/(4π) (L0) | d(1/αᵢ)/dL += −b_ij×α_j/(16R₂) | Corrected 1/αᵢ | Yes — via 1/(16R₂) |
| 5. GUT crossing | 1/α₁=1/α₂ at L_GUT | Average → 1/α_GUT | 1/α_GUT | R₂ cancels in crossing condition |
| 6. Back-run | 1/α_GUT, b₃', b_ij | Run from GUT to M_Z | Predicted 1/α₃ | Yes |
| 7. Extract α_s | 1/α₃_predicted | α_s = 1/(1/α₃) | α_s = 0.11838 | R₂ divides out in final ratio |
| 8. Compare | α_s_pred vs α_s_meas | Miss = \|pred−meas\|/meas | 0.33% | The REMAINDER |

The remainder (0.33%) is what the Level 0+1+2 moduli do not capture. It could come from three-loop corrections (more R₂ factors), threshold effects (modulus discontinuity — which PHYS-35 shows is a poor approximation), or physics beyond the current framework.

---

*End of supporting tables. 14 tables tracking the modulus concept across the series: from R₂ as geometric filling fraction through Level 1 gauge group moduli to Level 3 predictions. The key principle: moduli are topological properties of vortex geometry, they cancel in symmetric ratios, and they do not switch off at energy thresholds.*

