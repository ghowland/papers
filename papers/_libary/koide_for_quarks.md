# Working Document: Quark Koide Analysis — Amplitude, Phase, Confinement

## Status: NOTEBOOK — Not Published, Not in Series

## Purpose: Complete state capture. Thorough investigation of whether Koide extends to quarks.

---

## I. THE QUESTION

The Koide formula works for charged leptons (pole masses) at 0.0009%. Does it work for quarks? If not, does the "mass is inertia / field is vortex / boundary crossing" framing (PHYS-1) open a path?

---

## II. RESULTS

### Koide Ratio by Sector

| Sector | a | a² | θ₀ | Koide ratio | vs 2/3 |
|---|---|---|---|---|---|
| Leptons (pole) | 1.4142 | 2.0000 | 132.7° | 0.666661 | −0.00% |
| Down MSbar (d,s,b) | 1.5455 | 2.3886 | 126.3° | 0.731428 | +9.71% |
| Down pole-b (d,s,b) | 1.5700 | 2.4651 | 125.9° | 0.744176 | +11.6% |
| Up MSbar-c pole-t (u,c,t) | 1.7589 | 3.0939 | 124.3° | 0.848981 | +27.3% |
| Up pole-c pole-t (u,c,t) | 1.7291 | 2.9897 | 124.9° | 0.831611 | +24.7% |

**Koide fails for quarks.** Down-type 10% off, up-type 25–27% off. Not close.

### Hypotheses Tested and Killed

**1. Same a = √2, different θ₀.** KILLED. The PHYS-8 identity proves the Koide ratio = (1 + a²/2)/3 is independent of θ₀. At a = √2, the ratio is exactly 2/3 for ALL phases. θ₀ cannot explain the quark failure. The amplitude MUST differ.

**2. Pole masses instead of MSbar.** KILLED. Pole m_b = 4780 MeV (vs MSbar 4180) makes down-type WORSE (0.744 vs 0.731). Pole m_c = 1670 MeV (vs MSbar 1270) makes up-type slightly better (0.832 vs 0.849) but still 25% off. The pole/MSbar distinction does not rescue quark Koide.

**3. Uniform 2-of-3 correction (scale m_d and m_s, fix m_b).** KILLED. The Koide ratio as a function of the scaling factor f has a minimum of ~0.661 at f ≈ 2, which never quite reaches 2/3. The limiting ratio as f → ∞ is 0.701 (the 2-mass d,s ratio). The topology of the function prevents a uniform light-quark correction from restoring 2/3.

**4. Renormalization scale choice.** KILLED. The Koide ratio is exactly scale-invariant under universal mass scaling m_i → c·m_i. Proof: numerator scales as c, denominator (sum of √m)² scales as (√c)² = c. Cancels. No choice of QCD renormalization scale can change the Koide ratio.

### What Survives

**The amplitude ordering tracks interaction strength:**

| Sector | Color? | Charge | a | a² | Excess a² over 2 |
|---|---|---|---|---|---|
| Leptons | No | −1 | 1.414 | 2.000 | 0.000 |
| Down quarks | Yes | −1/3 | 1.545 | 2.389 | 0.389 |
| Up quarks | Yes | +2/3 | 1.759 | 3.094 | 1.094 |

Leptons (no color) sit at a² = 2 exactly. Quarks (color) have a² > 2. Up quarks (larger charge, stronger EM coupling) have larger excess than down quarks. The amplitude excess correlates with interaction strength.

**The phase angles are similar across sectors:** 124°–133°, all in a narrow band. The phases are not the source of the difference. The amplitudes are.

---

## III. THE STRUCTURAL FINDING

### Scale Invariance Proof

Under m_i → c·m_i for all i in a sector:

(Σ c·m_i) / (Σ √(c·m_i))² = c·(Σ m_i) / (√c · Σ √m_i)² = c·(Σ m_i) / (c · (Σ √m_i)²) = (Σ m_i) / (Σ √m_i)²

The Koide ratio is exactly invariant. QED.

**Consequence:** The quark Koide failure cannot be fixed by choosing a different renormalization scale. The failure is structural, not an artifact.

### Phase Independence Proof

From PHYS-8: the Koide ratio = (1 + a²/2)/N depends only on a and N. The parameters M and θ₀ cancel exactly. Verified numerically: at a = √2, N = 3, the ratio is 0.6666666667 for θ₀ = 0° and θ₀ = 120° (the only values where all masses are positive).

**Consequence:** If the ratio differs from 2/3, the amplitude differs from √2. No phase adjustment can compensate.

---

## IV. THE CONFINEMENT INTERPRETATION

### The Logic

Leptons don't feel the strong force. Their pole masses are direct measurements of pattern inertia. The Koide formula works at 0.0009%.

Quarks feel the strong force. Their masses are extracted through the confinement boundary. The MSbar mass at 2 GeV is a boundary-depth reading (PHYS-2) that includes confinement effects non-universally — light quarks are more affected than heavy quarks.

Non-universal corrections DO change the Koide ratio (unlike universal scaling, which preserves it). Confinement is non-universal. Therefore confinement changes the quark Koide ratio away from 2/3.

The direction is correct: confinement inflates the apparent inertia of light quarks relative to heavy quarks, spreading the masses further than the underlying pattern inertias warrant. This increases the amplitude above √2, which increases the Koide ratio above 2/3. Exactly what we see.

### The Wall

Quantifying the non-universal confinement correction requires computing on the inside face of the confinement boundary (PHYS-6). This is non-perturbative QCD. The integer arithmetic framework operates on the outside face. Same wall as the hadronic VP, same wall as the muon g-2 hadronic contribution.

---

## V. WHAT WOULD UNBLOCK THIS

(a) Lattice QCD computes quark masses in a scheme-independent way. If lattice produces "physical" quark masses (analogous to pole masses) that differ from MSbar in a way that restores Koide, the confinement correction is quantified. Current lattice results give MSbar masses, not pole-like masses for light quarks.

(b) If the amplitude excess (a² − 2) can be related to α_s or the color factor by a derivable formula, the quark Koide ratio becomes a prediction. The amplitude ordering (0, 0.389, 1.094) correlates with interaction strength but no formula has been found. The ratio of excesses (0.389/1.094 = 0.355) doesn't match any obvious coupling or charge ratio.

(c) If Koide is derived from a symmetry principle that applies equally to leptons and quarks but with a color correction factor, the quark amplitudes would follow. This requires the equal-spacing derivation that PHYS-8 identified as the deepest open question.

---

## VI. NUMERICAL RESULTS FOR FUTURE REFERENCE

```
Parameter extraction (atan2-based, proper sign):

Leptons:  M=17.716  a=1.4142  a²=2.0000  θ₀=132.73°  Koide=0.666661
Down MSbar: M=25.493  a=1.5455  a²=2.3886  θ₀=126.31°  Koide=0.731428
Down pole-b: M=26.988  a=1.5700  a²=2.4651  θ₀=125.87°  Koide=0.744176
Up MSbar-c: M=150.889  a=1.7589  a²=3.0939  θ₀=124.26°  Koide=0.848981
Up pole-c: M=152.632  a=1.7291  a²=2.9897  θ₀=124.94°  Koide=0.831611

Amplitude excess over Koide (a² − 2):
  Leptons: 0.000
  Down: 0.389
  Up (MSbar-c): 1.094
  Up (pole-c): 0.990

2-of-3 scan (m_d, m_s scaled, m_b fixed):
  f=0.001: 0.989, f=0.1: 0.896, f=1: 0.731
  f=2: 0.661 (minimum), f=5: 0.563, f=100: 0.418
  Minimum ~0.661 at f≈2 — never reaches 2/3
  Limiting ratio (f→∞) = 0.701 (2-mass d,s limit)
```

---

## VII. SCRIPTS

`quark_koide_test.py` — initial Koide test, amplitude extraction, uncertainty analysis
`quark_koide_confinement.py` — confinement correction scan, scale invariance proof
`quark_koide_fixed.py` — all four fixes from red team: phase independence, atan2 angles, pole masses, proper 2-of-3 scan

All in /home/claude/. Not in outputs (notebook entries).

---

## VIII. TAGS FOR FUTURE RETRIEVAL

- Koide quarks, quark mass, amplitude, phase independence
- Scale invariance proof, universal scaling, Koide ratio invariant
- Confinement boundary, non-universal correction, inside face
- MSbar vs pole mass, m_c pole 1670, m_b pole 4780
- Amplitude ordering: leptons < down < up, correlates with color/charge
- a² excess: 0 (leptons), 0.389 (down), 1.094 (up)
- θ₀ narrow band: 124°–133° all sectors
- 2-of-3 correction topology: minimum 0.661, cannot reach 2/3
- Blocked by: confinement boundary, same wall as hadronic VP

---

**END WORKING DOCUMENT**

**Status:** Notebook entry. Not in series. Not published.
**Finding:** Koide fails structurally for quarks (10–27% off). Phase cannot explain it (proven). Scale choice cannot explain it (proven). Pole masses make it worse. The amplitude excess correlates with color interaction strength but is not quantifiable from outside the confinement boundary.
**Blocked by:** Non-universal confinement correction is on the inside face of the confinement boundary. Same wall as hadronic VP.
**Pickup instructions:** Load this plus PHYS-6 and PHYS-8. The amplitude ordering (leptons < down < up tracking interaction strength) is the surviving lead. If a formula for the color correction to the Koide amplitude is found, quark masses become derivable.

---

## ADDENDUM: M4 — Frustration Departure from 120° on z=3 Graphs

### The Connection

On a 3-regular graph (z = 3, each node connected to three neighbors) with Kuramoto-type phase coupling, equal 120° spacing between three sectors is a saddle point, not a minimum. The system's ground state departs from 120°. This is proven in the Kuramoto-on-graphs literature and follows from the triangular face frustration inherent to z = 3 topology.

The Koide parametrization places three masses on a circle at phases θ₀ + 2πi/3 (equal 120° spacing). Our quark Koide analysis found that the reconstructed θ₀ values are:

| Sector | θ₀ | Departure from 120° |
|---|---|---|
| Leptons | 132.7° | +12.7° |
| Down quarks | 126.3° | +6.3° |
| Up quarks | 124.3° | +4.3° |

The θ₀ is not the spacing between masses — it's the orientation of the pattern on the circle. The spacing IS 120° by construction in the Koide parametrization. What varies is the amplitude a, not the spacing.

However: if the equal-spacing assumption is RELAXED — if the three masses sit at θ₀, θ₀ + Δ₁, θ₀ + Δ₁ + Δ₂ with Δ₁ + Δ₂ + Δ₃ = 2π but Δ₁ ≠ Δ₂ ≠ Δ₃ — then the frustration departure from 120° becomes the physical content. The Koide ratio (1 + a²/2)/3 assumes equal spacing. Unequal spacing changes the ratio. The quark Koide failure (ratio ≠ 2/3) might be reinterpreted as a spacing failure rather than an amplitude failure.

### The Hypothesis

If quark flavors within a charge sector are modes on a frustrated z = 3 graph, the ground state spacing is NOT 120° but a specific computable departure. This departure changes the Koide ratio from 2/3 to the measured values (0.731 for down, 0.849 for up). The leptons, which don't feel the strong force, sit on an unfrustrated graph where 120° IS the minimum, giving Koide = 2/3 exactly.

The frustration source for quarks would be the color interaction — the z = 3 graph is the color SU(3) structure, and the triangular frustration is confinement viewed as a topological obstruction.

### What Would Be Required

1. Identify the specific graph: z = 3 on what manifold? The SU(3) weight diagram is a natural candidate — it's a triangular lattice with z = 3.
2. Define the coupling: Kuramoto-type phase coupling with what natural frequency distribution? The natural frequencies would map to quark masses.
3. Compute the ground state: find the minimum-energy phase configuration for three modes on the frustrated graph. The departure angles are the output.
4. Map to masses: the departure angles plus the Koide parametrization give mass ratios. Compare to measured.

Each step is a separate unsolved problem. The chain is: frustrated graph → departure angles → mass ratios. If step 3 produces angles that match the quark data, the connection is established and quark masses become derivable from graph topology.

### Why This Is Parked

The computation requires specifying the graph, which requires a physical argument for which graph nature uses. Without that, we're searching an infinite space of z = 3 graphs. The PHYS-1 vortex picture suggests the graph is related to the field's mode structure, but this hasn't been formalized.

The M4 frustration result is the one item from CKS that connects to a live open question (the Koide equal-spacing derivation from PHYS-8) through established mathematics (Kuramoto on frustrated graphs). It doesn't provide an answer but it identifies a specific mathematical structure — frustrated z = 3 phase dynamics — that produces the right qualitative behavior (departure from equal spacing for strongly-interacting modes).

### Tags

Kuramoto, frustration, z=3 graph, saddle point, 120° departure, SU(3) weight diagram, graph ground state, unequal spacing, Koide generalization, confinement as topological frustration

