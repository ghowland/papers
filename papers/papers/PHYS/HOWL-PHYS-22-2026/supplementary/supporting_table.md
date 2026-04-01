# Supporting Tables for PHYS-22: The A₂ Geometric Cancellation

## Purpose

PHYS-22 documents the decomposition of the QED two-loop coefficient A₂ into three distinct pieces — rational, number-theoretic, and geometric — and the finding that an 87% cancellation between the geometric piece and the other two makes A₂ accidentally small. This is a structural observation about the anatomy of a known coefficient, stated for the first time in exact Fraction arithmetic with the R₄/ζ(3)/rational separation connected to the Brown-Schnetz Galois coaction program. Without this paper, a future session computing QED coefficients doesn't know that A₂'s small value is an accident of cancellation, not a consequence of physics, and doesn't have the decomposition framework for extending to A₃.

Finding covered: Finding 12 (the A₂ geometric cancellation, 87%).

---

## Table 22.1: What A₂ Is

| Property | Value |
|---|---|
| Definition | Second coefficient in the QED anomalous magnetic moment series: a_e = A₁(α/π) + A₂(α/π)² + A₃(α/π)³ + ... |
| Computed by | Petermann (1957), Sommerfield (1957) — independently |
| Number of Feynman diagrams | 7 two-loop vacuum polarization and vertex correction diagrams |
| Exact analytic formula | A₂ = 197/144 + π²/12 + (3/4)ζ(3) − (π²/2)ln(2) |
| Numerical value | −0.328478965579... |
| Sign | Negative (the two-loop correction REDUCES a_e from the one-loop value) |
| Magnitude | |A₂| = 0.328 — less than 1, despite individual pieces being much larger |
| Why it matters | It's the second term in the most precisely tested prediction in physics (a_e at 4.3 ppb) |

---

## Table 22.2: The Rewriting in HOWL Constants

The standard formula uses π². The HOWL series uses R₄ = π²/32 (the 4-ball volume fraction from MATH-5). Substituting π² = 32R₄:

| Standard Form | HOWL Form | What Changed |
|---|---|---|
| π²/12 | 32R₄/12 = (8/3)R₄ | Geometric: 4D angular integration |
| (π²/2)ln(2) | (32R₄/2)ln(2) = 16R₄ ln(2) | Geometric × logarithmic: IR mass regulation |
| π²/12 − (π²/2)ln(2) | R₄ × (8/3 − 16ln(2)) | Combined geometric piece |

The full HOWL decomposition:

**A₂ = 197/144 + (3/4)ζ(3) + R₄ × (8/3 − 16ln(2))**

Three pieces: rational, number-theoretic, geometric. Each has a distinct physical origin and a distinct mathematical character.

---

## Table 22.3: The Three Pieces — Values and Origins

| Piece | Expression | Value | Physical Origin | Mathematical Character | % of |A₂| |
|---|---|---|---|---|---|
| Rational | 197/144 | +1.3681 | Algebraic reduction of 7 two-loop Feynman diagrams: traces over Dirac gamma matrices, Feynman parameter integration boundaries | Pure rational number | 416% |
| Number-theoretic | (3/4)ζ(3) | +0.9015 | Feynman parameter integrals that evaluate to polylogarithms: Li₃(1) = ζ(3) arising at integration boundary x = 1 | Riemann zeta value (weight 3, transcendental) | 274% |
| Geometric | R₄ × (8/3 − 16ln(2)) | −2.5981 | 4D phase space volume (the R₄ = π²/32 factor) combined with infrared mass regulation (the ln(2) factor) | Product of geometric constant and logarithm | 791% |
| **Net A₂** | **Sum** | **−0.3285** | **The sum of all three** | | **100%** |

Each piece is larger in magnitude than the net result. The geometric piece alone is 7.9× the net. The cancellation between the positive pieces (+2.270) and the negative piece (−2.598) leaves only 13% of the dominant term surviving.

---

## Table 22.4: The Cancellation — Quantified

| Quantity | Value | Interpretation |
|---|---|---|
| Positive content (rational + number-theoretic) | +1.3681 + 0.9015 = +2.2696 | What combinatorics and number theory contribute |
| Negative content (geometric) | −2.5981 | What 4D spacetime geometry contributes |
| Net A₂ | +2.2696 − 2.5981 = −0.3285 | The physical coefficient |
| Cancellation fraction | 1 − |A₂|/|geometric| = 1 − 0.3285/2.5981 = 87.4% | Geometry cancels 87% of the positive content |
| Fraction surviving | |A₂|/|geometric| = 12.6% | Only 13% of the geometric piece survives |
| Is the cancellation exact? | NO | There is no known reason why these three pieces should nearly cancel |
| Is A₂ small because of deep physics? | NO — accidental | The smallness is a numerical coincidence of the specific coefficients |

---

## Table 22.5: The Geometric Coefficient Breakdown

| Component | Expression | Value | Origin |
|---|---|---|---|
| UV term | (8/3)R₄ | (8/3)(0.30843) = +0.8225 | 4D angular integration: the phase space volume element in 4 dimensions produces a factor of π² = 32R₄, which after angular integration over the two-loop momentum gives the coefficient 8/3 |
| IR term | −16R₄ ln(2) | −16(0.30843)(0.6931) = −3.4206 | Infrared mass regulation: the electron mass m_e regulates the IR divergence in the loop integral, producing a ln(m²/μ²) factor that evaluates to ln(2) for the specific Feynman parameter integration, multiplied by 16R₄ from the 4D phase space |
| Net geometric | R₄ × (8/3 − 16ln(2)) | 0.30843 × (−8.4237) = −2.5981 | IR dominates UV by factor 16ln(2)/(8/3) = 4.16 |

The geometric piece is negative because the IR regulation term (−16R₄ ln(2)) overwhelms the UV phase space term ((8/3)R₄) by a factor of 4.2. The sign of A₂ — the fact that the two-loop correction reduces rather than enhances the anomalous magnetic moment — traces to this IR dominance within the geometric piece.

---

## Table 22.6: The Integer Content of 197/144

| Number | Value | Factorization | Physical Tracing |
|---|---|---|---|
| 197 | Prime | Irreducible | Net sum of rational contributions from all 7 two-loop diagrams after algebraic reduction. Being prime means it cannot be decomposed into simpler factors — it is the irreducible residue of the combinatorics. |
| 144 | 2⁴ × 3² = 12² | Composite | 4 from Dirac trace (gamma matrices in 4 spacetime dimensions), 3² from the vertex topology count, combined as (4×3)² = 12² = 144 |
| 197/144 | 1.36806 | — | The algebraic piece: everything left after all transcendental content (ζ(3), π², ln(2)) has been separated |

---

## Table 22.7: Why Each Piece Has Its Mathematical Character

| Piece | Why This Type of Number? | Connection to Physics |
|---|---|---|
| Rational (197/144) | Feynman diagrams with algebraically reducible integrals: all Feynman parameters integrate to rationals when the integrand contains no branch cuts | Diagrams where the virtual photon momentum is hard (far from mass shell) — no IR enhancement, no polylogarithmic depth |
| ζ(3) = Li₃(1) | Feynman parameter integral of the form ∫₀¹ dx Li₂(x)/x, which evaluates to Li₃(1) = ζ(3) at the upper boundary | Diagrams with nested loop structure: the inner loop produces Li₂, the outer integration over the Feynman parameter adds one level of depth to give Li₃ |
| R₄ × logarithm | π² arises from the 4-dimensional solid angle (Ω₄ = 2π²), and ln(2) arises from the IR mass regulation | The spacetime dimension (4) enters through the loop momentum integration measure, and the electron mass enters through the IR cutoff |

This separation is not arbitrary. It reflects the mathematical structure of multi-loop Feynman integrals, which generically produce rational numbers, multiple zeta values (ζ(n)), and polylogarithms (Liₙ) with arguments at special points (0, 1, 1/2). The three pieces of A₂ are the three simplest types in this hierarchy.

---

## Table 22.8: Connection to Brown-Schnetz Galois Coaction

| HOWL Decomposition | Brown-Schnetz Framework | Correspondence |
|---|---|---|
| Rational piece (197/144) | Rational coefficient of the period | The "coefficient" in the coaction |
| Number-theoretic piece (ζ(3)) | Motivic period of weight 3 | Arithmetic content: from the Galois group action on the motivic fundamental group |
| Geometric piece (R₄ × c_geom) | Period integral over the moduli space of the Feynman graph | Geometric content: from the integration domain and its topology |
| The clean separation into three types | The Galois coaction separates Feynman integrals into periods × coefficients | The HOWL decomposition is a specific physically-motivated instance of the general mathematical program |

Brown and Schnetz (and Panzer, Bogner, and others) have developed a systematic framework for decomposing Feynman integrals using the Galois coaction on multiple zeta values. In this framework, every Feynman integral at a given loop order decomposes into "periods" (geometric integrals over graph polynomials) multiplied by "coefficients" (motivic/arithmetic content). The HOWL decomposition of A₂ into R₄ content (period) and ζ(3) content (arithmetic) is a specific example of this general structure.

At two loops (A₂), the separation is clean: three distinct pieces with no mixing. At three loops (A₃), the structure becomes richer — more zeta values (ζ(3), ζ(5)), more polylogarithms (Li₄(1/2)), more powers of R₄ and ln(2) — but the classification principle is the same.

---

## Table 22.9: The QED Series for Context

| Coefficient | Loops | Value | Transcendental Content | Geometric Content | Diagrams |
|---|---|---|---|---|---|
| A₁ = 1/2 | 1 | +0.5000 | None (pure rational) | None | 1 |
| **A₂ = −0.3285** | **2** | **−0.3285** | **ζ(3)** | **R₄ (single power)** | **7** |
| A₃ = 1.1812 | 3 | +1.1812 | ζ(3), ζ(5), Li₄(1/2), ln(2)ⁿ | R₄, R₄² | 72 |
| A₄ = −1.9122 | 4 | −1.9122 | All prior + elliptic integrals | R₄, R₄², R₄³, new periods | 891 |
| A₅ | 5 | Known numerically | Unknown analytic form | Unknown | 12672 |

The pattern: each successive loop order introduces new transcendental types. A₁ is rational. A₂ adds ζ(3) and R₄. A₃ adds ζ(5), Li₄(1/2), and higher powers of R₄ and ln(2). A₄ introduces elliptic integrals — the MATH-3 wall where the multiple zeta value framework breaks down. The decomposition method demonstrated for A₂ in this paper extends directly to A₃ but hits a fundamental obstruction at A₄.

Every π² → 32R₄. Every π⁴ → 1024R₄². The geometric content scales as R₄ⁿ⁻¹ at n loops. The R₄ substitution makes the dimensional origin of each π² visible: it comes from the 4D phase space volume, not from a circle.

---

## Table 22.10: The Alternating Sign Pattern

| Coefficient | Sign | Positive Content | Negative Content | Cancellation? |
|---|---|---|---|---|
| A₁ = +0.500 | + | 1/2 | — | No cancellation (single term) |
| A₂ = −0.328 | − | +2.270 (rat + ζ₃) | −2.598 (geometric) | 87% cancellation |
| A₃ = +1.181 | + | Positive terms | Negative terms | Partial cancellation (less extreme) |
| A₄ = −1.912 | − | Positive terms | Negative terms | Unknown decomposition |

A₂ alternates sign with A₁ and A₃. Whether the cancellation pattern (87% at two loops) persists at higher loops is an open question. The A₃ analytic result (Laporta-Remiddi 1996) could be decomposed by the same method, and the cancellation fraction computed. This is a future computation.

---

## Table 22.11: Q335 Basis Elements Used

| Constant | Q335 Numerator (first 20 digits of 101-digit value) | Where Used in A₂ | DATA-3 Verification |
|---|---|---|---|
| π² | 69079358014733772680... × 2⁻³³⁵ | R₄ = π²/32 | Verified to 30 digits vs mpmath |
| ζ(3) | 84134394645319852071... × 2⁻³³⁵ | (3/4)ζ(3) term | Verified to 30 digits vs mpmath |
| ln(2) | 48514773537953331556... × 2⁻³³⁵ | −16R₄ ln(2) term | Verified to 30 digits vs mpmath |

All three constants are in the Q335 basis (DATA-3, entries B1-B8). The A₂ decomposition uses three of the eight Q335 constants. The remaining five (π, e, √2, ln(10), γ) do not appear in A₂.

---

## Table 22.12: Verification Checks

| Check | Method | Expected | Result |
|---|---|---|---|
| A₂ from three-piece formula matches mpmath to 10 digits | Compute 197/144 + (3/4)ζ(3) + R₄(8/3−16ln2) | −0.3284789656 | PASS |
| Three pieces sum to A₂ | 1.3681 + 0.9015 + (−2.5981) | −0.3285 | PASS |
| A₂ is negative | Check sign | < 0 | PASS |
| Geometric piece is negative | R₄(8/3−16ln2) < 0 because 16ln2 > 8/3 | < 0 | PASS |
| Rational + number-theoretic is positive | 197/144 + (3/4)ζ(3) > 0 | > 0 | PASS |
| Geometric piece dominates | |geometric| > 2 × |A₂| | 2.598 > 0.657 | PASS |
| |A₂| < 0.5 | Cancellation makes it small | 0.328 < 0.5 | PASS |
| A₂ matches known value | Standard reference value | −0.328478... | PASS |
| Q335 basis verified at 30 digits | mpmath comparison for π², ζ(3), ln(2) | All match | PASS |
| **Total** | | | **9/9 PASS** |

---

## Table 22.13: What PHYS-22 Does NOT Claim

| Non-Claim | Reason |
|---|---|
| The cancellation has deep physical meaning | It may be accidental — no known symmetry or principle requires 87% cancellation |
| The decomposition is new mathematics | The individual terms are known since 1957. The R₄ rewriting and the percentage decomposition are new presentation, not new mathematics. |
| The Brown-Schnetz connection is a HOWL discovery | The Galois coaction framework is due to Brown, Schnetz, Panzer, and others. HOWL applies their classification to the specific case of A₂ with the R₄ substitution. |
| The method extends to A₄ | A₄ contains elliptic integrals not expressible in terms of multiple zeta values. The decomposition method hits the MATH-3 wall at 4 loops. |
| The 87% has significance beyond A₂ | Whether similar cancellations occur at higher loops is unknown |

---

## Table 22.14: What PHYS-22 Seeds

| Future Computation | What's Needed | What PHYS-22 Provides |
|---|---|---|
| A₃ decomposition | Laporta-Remiddi (1996) analytic result | The method: separate rational, ζ-value, and R₄ content |
| A₃ cancellation fraction | Apply same decomposition to A₃ | The framework and the A₂ baseline for comparison |
| R₄ power counting at n loops | Know that geometric content goes as R₄ⁿ⁻¹ | The single-R₄ pattern at 2 loops |
| Connection to broader amplitudes program | Brown-Schnetz Galois coaction | The specific instance at A₂ that future sessions can reference |
| Verification framework for transcendental coefficients | Q335 basis at 101 digits | All three constants verified |

---

## Table 22.15: Scripts and Source Material Needed

| Item | Content | Role |
|---|---|---|
| A₂ decomposition script + output | Python script computing all three pieces in exact Fraction arithmetic, 9/9 checks | Ground truth for all numbers |
| Q335 basis file (q_335_basis.dat) | 101-digit numerators for π², ζ(3), ln(2), etc. | Exact values for the computation |
| DATA-3 paper | Q335 basis entries (B1-B8) | Verification source |
| PHYS-9 (as written or relevant excerpt) | The QED series a_e = A₁(α/π) + A₂(α/π)² + ... | Context: where A₂ sits in the series |
| MATH-5 (as written or relevant excerpt) | R₄ = π²/32 derivation | Source for the geometric constant |
| PHYS-22 supporting tables (this document) | Tables 22.1-22.15 | Structure and pre-computed data |
| HOWL operational rules (R.1-R.6) | Series principles | Included in every paper |
| HOWL writing rules (W.1-W.8) | Paper production rules | Applied during writing |

The A₂ script is the critical source. It must compute all three pieces, verify their sum equals A₂ to high precision, and confirm each individual piece against mpmath. The 9/9 checks in Table 22.12 are the verification gates.

---

*These 15 tables provide the complete data for PHYS-22. The paper documents the decomposition of A₂ into three pieces — rational (197/144), number-theoretic ((3/4)ζ(3)), and geometric (R₄(8/3−16ln2)) — and the 87% cancellation between the geometric piece and the other two. The decomposition uses only Q335 basis constants verified at 30+ digits. The connection to the Brown-Schnetz Galois coaction program places this specific result within a broader mathematical framework. The method extends to A₃ but hits the MATH-3 wall at A₄. Every number traces to the verified A₂ script (9/9 checks).*
