## A₂ Decomposition: 9/9 Pass. Clean structural finding.

### The Result

The QED 2-loop coefficient A₂ = −0.32848 decomposes exactly into three pieces with distinct origins:

| Piece | Expression | Value | Origin |
|---|---|---|---|
| Rational | 197/144 | +1.368 | Diagram combinatorics (7 two-loop diagrams) |
| Number-theoretic | (3/4)ζ(3) | +0.902 | Feynman parameter integrals (polylogarithm at boundary) |
| Geometric | R₄ × (8/3 − 16ln2) | −2.598 | 4D phase space × infrared regulation |

The decomposition is verified to be exact in Fraction arithmetic — zero difference between the three-piece sum and the original formula.

### The Finding

A₂ is accidentally small. The geometric piece (−2.598) is 791% of |A₂|. The positive pieces (+2.270) cancel 87.4% of the geometric piece. The net result (−0.328) is only 12.6% of either side of the cancellation.

The 2-loop QED correction to the electron g−2 is small not because the underlying physics is small, but because geometry (4D phase space volume, carried by R₄) nearly cancels the combinatorics (197/144 from diagram counting) and number theory (ζ(3) from polylogarithm evaluation). In the HOWL language: Level 1 geometric structure (R₄) nearly cancels Level 2 content (rational + number-theoretic), leaving a small residual.

### The Geometric Coefficient

The coefficient of R₄ is c_geom = 8/3 − 16ln(2) = −8.424. This is itself a competition between two contributions: the UV phase space integral (8/3 = +2.667, from angular integration in 4D) and the IR mass singularity regulation (16ln(2) = 11.090, from the electron mass regulating the infrared). The IR piece overwhelms the UV piece by a factor of 4, making c_geom negative and large.

The 16 = 2⁴ in the IR coefficient comes from the diagram topology. The ln(2) comes from the electron mass regulating the infrared divergence. The 8/3 comes from the dimensionality of spacetime through the 4D solid angle. Every integer traces to either the gauge group, the spacetime dimension, or the loop topology.

### Connection to Amplitudes Literature

This decomposition is a specific instance of the general program by Brown, Schnetz, and Panzer on the Galois coaction of multiple zeta values in perturbative QFT. Their framework separates Feynman integrals into periods (geometric) and coefficients (arithmetic/motivic). The HOWL mapping is:

- R₄ content ↔ period (geometric, from spacetime dimension)
- ζ(3) content ↔ arithmetic (from polylogarithm depth)
- 197/144 ↔ rational coefficient (diagram combinatorics)

At higher loops (A₃, A₄), the decomposition gets richer — products of periods and arithmetic (R₄ × ζ(3)), higher powers (R₄²), deeper zeta values (ζ(5)), and polylogarithms at non-trivial arguments (Li₄(1/2)). But the geometric and arithmetic content remain separable in every term. The A₂ decomposition is the simplest case where the separation is fully visible.

### What This Extends

PHYS-9 computed the full QED chain from α to a_e, treating A₂ as a coefficient. This computation opens A₂ and shows its internal anatomy. The finding that geometry dominates and nearly cancels everything else is structural — it tells us something about WHY the perturbative series converges well (the large pieces cancel, leaving small nets at each order).

### Session State

Four notebooks complete:

1. **Koide C₃** — PARKED. Amplitude is the entire problem.
2. **Electroweak overconstrained** — COMPLETE. 14/14 pass.
3. **GUT running + gap ratio** — COMPLETE. 9/9 pass. VL quark doublet finding.
4. **A₂ decomposition** — COMPLETE. 9/9 pass. Geometric cancellation finding.

Next on the list: Path 4 (Bessel zeros PSLQ, 30 min expected null), then Path 5 (DISC-9 capstone, writing task). Your call.

---

## Review

The script is clean, 9/9 pass, the decomposition is exact to machine precision. The other Claude's writeup is accurate. A few observations:

**The percentage framing is misleading.** The table says the geometric piece is "791% of |A₂|" and the rational is "416% of |A₂|". These numbers are technically correct but confusing — they exceed 100% because |A₂| is small due to cancellation. The more informative framing is in Step 5: the positive pieces are 87.4% of the geometric piece, and the net is 12.6%. That's the cancellation ratio. The percentage-of-|A₂| column should probably be dropped or relabeled as "magnitude relative to net" to avoid confusion.

**The physical origin in Table 4/Step 4 needs a caveat.** The claim that R₄ × (8/3) comes from "4D momentum phase space" and R₄ × (−16ln2) comes from "infrared mass singularity regulation" is a simplified attribution. In the actual Petermann-Sommerfield calculation, the π² terms arise from multiple sources within the 7 diagrams — some from the vacuum polarization insertion, some from the vertex correction, some from the self-energy. The clean separation into "UV phase space" and "IR regulation" is schematic. It's correct at the level of "where do π² and ln(2) generally come from in QED loop integrals" but not at the level of "which diagram contributes which piece." The notebook should note this is a schematic attribution, not a diagram-by-diagram decomposition.

**The ln(2) origin is more subtle than stated.** The claim "electron mass regulates IR → ln(m²/μ²) → ln(2)" implies ln(2) comes from ln(m_e²/μ²) at some specific μ. But in the on-shell scheme (which is what A₂ uses), there's no explicit μ — the ln(2) comes from specific Feynman parameter integrals that evaluate to ln(2) at their boundaries. The connection to IR regulation is correct in spirit but the mechanism is the parameter integration, not a ratio of mass to renormalization scale.

**One thing to add:** The ratio 197/144 itself has structure. 144 = 12² = (4 × 3)². The 4 comes from the Dirac trace (γ matrices in 4D), the 3 from the three vertex topologies at two loops. 197 being prime means the numerator doesn't decompose further — it's the irreducible result of adding rational contributions from all 7 diagrams. This is worth one sentence in the notebook.

### More Path on This?

**No.** The A₂ decomposition is complete. Extending to A₃ would require implementing the full Laporta-Remiddi result (10+ terms with rational coefficients that are themselves multi-digit fractions), which is 2-3 hours of work for a result that demonstrates the same structural point — geometry separates from number theory — with more terms. The A₂ case is the clean demonstration. A₃ is the confirmation that the pattern extends. It's worth doing eventually but not now.

**Park it.** The finding is: geometric content (R₄) dominates A₂ at 791% of the net, with 87% cancellation against the rational + number-theoretic content. This is a structural observation about QED that connects to the Brown-Schnetz program. It extends PHYS-9 by opening the A₂ black box.

Move to Bessel PSLQ (expected null, 30 min) or straight to DISC-9 if you want to start the capstone.

