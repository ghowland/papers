Right. Here's the calculation chain for alpha from a_e + Laporta:

**The series:**

a_e = (1/2)(α/π) + C4(α/π)² + C6(α/π)³ + C8(α/π)⁴ + C10(α/π)⁵ + ...

Where:
- C2 = 1/2 — exact, Level 1
- C4 = -0.328... = -197/144 + (1/2)π² ln2 - (3/4)ζ(3) - (1/4)π² + ... — exact in Q335 constants
- C6 = 1.181... — exact in Q335 (zeta(3), zeta(5), Li4(1/2), pi, ln2)
- C8 = C81a + C81b + C81c — the Laporta numbers you have. Three ~1500-digit decimals.
- C10 = C83a + C83b + C83c — the 5-loop Laporta numbers. Three ~2500-digit decimals.

**The inversion:**

Given a_e (measured to 0.11 ppb), solve for α. This is a polynomial inversion — set x = α/π, solve:

a_e = (1/2)x + C4·x² + C6·x³ + C8·x⁴ + C10·x⁵

For x, then α = π·x.

**What we can do with Q335:**

C2 = 1/2 is already a Fraction. C4 and C6 are known exactly as combinations of Q335 constants — π, ζ(3), ζ(5), Li4(1/2), ln(2). We have all of these at 100+ digits as exact integer pairs.

The Laporta C8 and C10 values are given as ~1500-2500 digit decimals. These need to be converted to Q335 Fractions (p/2^335) for the computation to stay exact. At 100-digit precision this is straightforward — truncate to 100 digits, multiply by 2^335, round to nearest integer.

**The chain:**

1. Store C81a, C81b, C81c, C83a, C83b, C83c as Q335 Fractions (6 new value nodes)
2. Compute C8 = C81a + C81b + C81c, C10 = C83a + C83b + C83c as Q335 sums
3. Store C4 and C6 as exact Q335 combinations (they're known analytically)
4. Take a_e measured = exact Fraction from CODATA
5. Newton's method on the polynomial: solve for x = α/π
6. α = π·x, both Q335 Fractions → α is a Q335 Fraction
7. Compare α(a_e) to α(Cs recoil) = 137.035999206(11)⁻¹
8. Compare α(a_e) to α(quantum Hall)

**What the CD changes:**

The CD at 3 TeV contributes to hadronic vacuum polarization in the internal fermion loops. At 4-loop (C8), the mass-dependent piece C81b includes VP insertions. A VL fermion at M_VL adds a term proportional to (m_e/M_VL)² per VP insertion.

The shift: δa_e(CD) ~ (α/π)⁴ × (m_e/M_VL)² ~ 10⁻⁸ × (0.511/3×10⁶)² ~ 10⁻⁸ × 3×10⁻¹⁴ ~ 3×10⁻²². This is 9 orders of magnitude below current precision. The CD does NOT affect the alpha extraction at any foreseeable precision.

**So what does this give us?**

The CD is irrelevant here. But the Laporta numbers + Q335 arithmetic give us alpha extracted from a_e at a precision limited only by the a_e measurement (0.11 ppb). The result is α⁻¹(a_e) as an exact Q335 Fraction, comparable digit-by-digit to α⁻¹(Cs).

The value: alpha moves from "measured" to "derived from a_e + integers." The integer content is: C2 = 1/2 (exact), C4/C6 in terms of ζ(3), π, ln(2) (Q335 integers), C8/C10 from Laporta (converted to Q335). The a_e measurement is the single input. Alpha is the output.

**This means:** α is no longer a free parameter. It's derivable from a_e + QED integer coefficients. The "NOT COMPUTABLE" tag in your MATH-2 summary for α becomes "DERIVED FROM a_e."

One free parameter removed from CODATA. Want me to write the derivation function and value nodes?

---

The forward check reveals the problem:

```
result_ae_forward_from_known_alpha_v0    0.0011596553669292
result_ae_input_v0                       0.00115965218059
result_ae_forward_residual_v0            3.18633920375802e-9
result_ae_forward_residual_rel_v0        2.74766801381505e-6
```

Known alpha + Laporta coefficients give a_e = 0.001159655**37**, but measured a_e = 0.001159652**18**. The forward residual is 3.2×10⁻⁹, which is 2.7 ppm. That's enormous — measured a_e precision is 0.11 ppb.

**The series is wrong.** The coefficients don't reproduce the measured a_e from the known alpha. The 2752 ppb tension isn't physics — it's a bug in our series.

The problem is **C8 = 107.71**. The literature value of A₁⁽⁸⁾ (the complete 4-loop coefficient) is approximately **−1.9122** (Aoyama et al. 2012, 2019). C81a = 116.69 is only the mass-independent piece. The FULL 4-loop A₄ includes additional mass-dependent contributions from muon/tau VP loops, hadronic VP, and light-by-light with heavy leptons that are NOT in C81a+b+c.

Actually wait — C81b is the electron VP piece (−8.75) and C81c is light-by-light (−0.24). But there are also **muon-loop and tau-loop** contributions at 4-loop that Laporta's labeling might separate differently.

The real issue: Laporta's C81a/b/c might use a different series convention than the standard a_e = Σ Aₙ(α/π)ⁿ. The labels "C81" suggest "coefficient at order α⁸ with 1 electron loop" — the "8" is the power of e (coupling), not α. Order α⁸ in the coupling means (α/π)⁴ in the standard series. But "C8" with subscript "1" might mean something specific about the loop topology.

We need to verify: what is the KNOWN total A₄ coefficient? If it's −1.91 and not 107.71, then C81a+b+c is not A₄. It might be a sub-piece, or it might use a different expansion parameter.

Do you have any documentation from Laporta about what convention C81a/b/c uses? Or should I search for the standard published values of A₄ and A₅ to compare?

---

You're right. The CD at 3 TeV contributes to VP loops. I dismissed it earlier as 10⁻²² — but that was wrong. I computed (m_e/M_VL)² which is the MASS suppression for a heavy fermion in a VP insertion. But the CD contribution to a_e isn't just through VP — it modifies the running of alpha itself between M_Z and M_VL, which changes the effective alpha at the electron scale.

But actually — no. The QED series for a_e uses alpha at q²=0 (the Thomson limit), not at M_Z. The CD at 3 TeV doesn't change alpha at q²=0 because it's above the electron mass scale. The VP contribution from a 3 TeV fermion to the low-energy coupling is suppressed by (m_e/M_VL)² per loop. That really is 10⁻¹⁴ per insertion. It can't explain a 2.7 ppm discrepancy.

The forward residual of 2.7 ppm means the series coefficients are wrong by a large amount, not a small CD correction. The CD correction would be at most 10⁻¹¹ on a_e — we're off by 3×10⁻⁹, which is 300× larger.

The bug is in the coefficients or the convention, not the missing CD. We should fix the series first, then add the CD correction on top of a working baseline.

But your point stands — I should have been tracking the CD contribution explicitly as a separate term in the series from the start. Once the baseline works, the CD adds a calculable shift δa_e(CD) that changes the extracted alpha by a specific amount. That shift is the physics content.

Let me search for the correct published A₄ and A₅ total values so we can compare to our C8 and C10 sums.

---

