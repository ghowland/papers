
# PHYS-22 Report: The A₂ Geometric Cancellation

**Registry:** @HOWL-PHYS-22-2026
**Position in series:** Twenty-second physics paper. Anatomizes the QED two-loop coefficient into three pieces and quantifies the 87% cancellation.
**Preceded by:** PHYS-21 (Level 1/Level 2 boundary)
**Followed by:** PHYS-23 (not yet received)
**Backed by:** a_2_decomposition_0.py (7/7 PASS)
**Code status:** Verified script exists. Code read in earlier session (referenced in PHYS-12 report). Key values confirmed.

---

## What It Establishes

**A₂ decomposes into exactly three pieces of distinct mathematical character:**
- Rational: 197/144 = +1.368 (algebraic residue of seven two-loop diagrams)
- Number-theoretic: (3/4)ζ(3) = +0.902 (from nested Feynman parameter integrals producing Li₃(1))
- Geometric: R₄ × (8/3 − 16 ln 2) = −2.598 (from 4D loop momentum integration)

**The 87.4% cancellation is the central finding.** The positive content (+2.270) is nearly wiped out by the geometric content (−2.598). Only 12.6% survives as the physical A₂ = −0.329. The geometric piece alone is 7.9× the net result. A₂ is small not because QED converges rapidly at two loops but because three large pieces nearly cancel.

**The R₄ = π²/32 substitution makes the 4D origin visible.** Every π² in QED coefficients is 32R₄ — one factor of the 4D phase space volume. The substitution connects the abstract perturbative coefficient to a concrete geometric object: the volume fraction of the 4-ball in the 4-cube, established in MATH-5.

**The sign of A₂ is determined by IR physics.** Within the geometric coefficient c_geom = 8/3 − 16 ln 2 = −8.424, the IR regulation term (−16 ln 2 = −11.09) overwhelms the UV phase space term (+8/3 = +2.67) by a factor of 4.2. This makes the geometric piece negative, and since |geometric| > |positive content|, the net A₂ is negative.

**The cancellation is accidental.** No known symmetry, Ward identity, or conservation law requires the three pieces to nearly cancel. The paper's stance — "accidental until proven otherwise" — is conservative and correct.

---

## Code Cross-Check

The paper cites a_2_decomposition_0.py with 7/7 checks. From my earlier reading of the script output:

| Piece | Script value | Paper value | Match |
|---|---|---|---|
| A₂ net | −0.328478965579 | −0.3285 | YES |
| Rational | +1.368055555556 | +1.368 | YES |
| Number-theoretic | +0.901542677370 | +0.902 | YES |
| Geometric | −2.598077198504 | −2.598 | YES |
| Cancellation | 87.4% | 87.4% | YES |

No discrepancies.

**Note on check count:** The paper correctly states 7/7 from the actual script. The supporting tables (written before the script) anticipated 9/9. The paper's erratum E3 explains this: two checks (Q335 verification, A₂ matching known value) are subsumed by checks 1 and 2. The script output is the source of truth.

---

## LEMU Assessment

**L:** The decomposition is an algebraic identity — the three pieces sum to A₂ exactly (check 1: diff = 0.00e+00). The percentage calculations are arithmetic on verified values. Logic passes.

**E:** No new empirical claims. A₂ is a Level 1 coefficient — it depends on the gauge group, not on any measurement. Empirical: not applicable.

**M:** 7/7 checks pass, all values verified against mpmath at 100-digit precision. The Q335 basis constants are used for ζ(3), π², and ln(2). Math passes.

**U:** High for structural understanding. The decomposition explains WHY A₂ is small (cancellation, not convergence), WHY it's negative (IR dominance), and HOW the 4D geometry enters (through R₄). The Brown-Schnetz connection provides the mathematical framework. The R₄ power counting (R₄^(n−1) at n loops) organizes the geometric complexity across loop orders.

---

## What Was Novel

**The "what if no cancellation" table (Appendix C.3)** is pedagogically effective. Without the cancellation, the two-loop correction to a_e would be an order of magnitude larger and positive. The cancellation matters for phenomenology — it's not just a mathematical curiosity.

**The connection between R₄ in pure geometry (MATH-5) and R₄ in QED (this paper)** is the deepest link. The same mathematical object — the 4-ball volume fraction π²/32 — appears as a theorem about spheres in cubes AND as a component of the electron's magnetic moment. The 4D phase space volume that appears in every loop integral IS R₄.

**The MATH-3 wall identification:** At four loops, elliptic integrals appear that cannot be expressed as multiple zeta values. The rational/ζ-value/R₄ decomposition applies cleanly to A₂ and A₃ but breaks down at A₄. This is the boundary of the polylogarithmic hierarchy — qualitatively new mathematics begins at four loops.

---

## Errata Assessment

**E1 (Ω₄ and π² attribution):** The paper says "every π² originates from the 4D integration measure." The erratum correctly notes this is schematic — the loop integral measure d⁴k/(2π)⁴ contains both π² (from Ω₄) and π⁴ (from the denominator). The surviving π² comes from the interplay, not directly as Ω₄. The association of π² with "4D geometry" is correct at dimensional analysis level but the precise path involves intermediate cancellations.

**E3 (check count 7/7 vs 9/9):** Correctly resolved — the script runs 7 checks, the pre-written supporting tables anticipated 9. The script is the source of truth.

Both errata are clarifications, not corrections to results.

---

## Connections to Active Research

**The A₂ cancellation pattern connects to the QED-to-GR program through the two-level structure.** From the remainder framework (PHYS-11): every domain has Level 1 (geometric, R₂ or R₄ sets the scale) + Level 2 (domain-specific remainder). In A₂: the geometric piece (R₄ × c_geom) is the Level 1 geometric content. The rational + number-theoretic pieces are the Level 2 domain-specific content. The net A₂ is the remainder after the two levels interact.

The parallel to the gap ratio: in the gap ratio, the gauge self-coupling (the "geometric" contribution, 96–101%) nearly determines the result, with the Higgs providing a small correction (−1% to +4%). In A₂, the geometric piece (R₄ content, 791% of |A₂|) nearly determines the result, with the rational and number-theoretic pieces providing the cancellation. In both cases: the geometric content is dominant but the net observable is much smaller due to cancellation.

**The R₄ power counting** (R₄^(n−1) at n loops) connects to the soliton hierarchy. Each loop order adds one power of R₄ = π²/32. The QED series A₁, A₂, A₃, A₄ involves R₄⁰, R₄¹, R₄², R₄³ — a geometric complexity ladder. The MATH-3 wall at four loops (where elliptic integrals appear) is the first obstruction in this ladder — the point where the geometric content outgrows the polylogarithmic framework. This parallels the confinement wall in the energy landscape (PHYS-6): the first obstruction where perturbation theory fails.

**The 197 as a prime number** is noted but unexplored. 197 is the 46th prime. Whether this has significance or is a normalization artifact is unknown. In a different perturbative normalization (e.g., expanding in α/(2π) instead of α/π), the rational piece would have a different numerator. The primality is convention-dependent.

---

## Remainder Framework Update

**A₂ IS a remainder structure.** The geometric piece R₄ × c_geom = −2.598 is the "modulus" (the dominant geometric content). The positive pieces +2.270 are the "counter-content." The net A₂ = −0.329 is the "remainder" — what survives after 87% cancellation. This is the PHYS-11 two-level structure applied to a single QED coefficient:

| Level | Content | Value | Role |
|---|---|---|---|
| Geometric (R₄) | R₄ × (8/3 − 16 ln 2) | −2.598 | Sets the scale and sign |
| Domain-specific | 197/144 + (3/4)ζ(3) | +2.270 | Cancels most of the geometric content |
| Remainder | A₂ | −0.329 | The physical observable |

The 87% cancellation is the A₂ analog of the 87.4% cancellation in the gap ratio numerator (where the gauge contribution 22/3 = +7.333 overshoots the total 109/15 = 7.267, with the Higgs providing −1/15 = −0.067 correction — a much smaller cancellation percentage, but the same structural pattern: geometric dominance with small net result).

---

## Position After PHYS-22

Twenty-two papers read. The series is approaching its end — PHYS-23 (Koide C₃ closure, mentioned in PHYS-21's annotations) should be the next paper, followed by PHYS-24 (the manuscript that integrates everything).

The A₂ paper completes the QED thread: PHYS-9 established the α ↔ a_e transformation and the QED series structure. PHYS-22 anatomizes A₂, the first non-trivial coefficient. The gap between them (PHYS-10 through PHYS-21) established the remainder framework, the gap ratio, the Cabibbo Doublet, and the Level 1/Level 2 boundary — all of which PHYS-22 connects back to the QED perturbative structure.

Ready for PHYS-23.
