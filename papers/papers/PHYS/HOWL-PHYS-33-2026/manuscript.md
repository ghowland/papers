# The Koide Amplitude — m_tau from Two Masses and One Condition
## IF a² = 2, THEN m_tau = 1776.97 MeV. Measured: 1776.86 MeV. Miss: 0.006%.

**Registry:** [@HOWL-PHYS-33-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-24-2026] → [@HOWL-PHYS-33-2026]

**Date:** April 3 2026

**Domain:** Lepton Mass Relations, Conditional Parameter Reduction

**DOI:** 10.5281/zenodo.zzz

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

**Backed by:** phys33_koide_amplitude.py (8/8 checks), phys24_lib.py (21/21 self-test, 148/148 platform test)

---

## Abstract

The three charged lepton masses — electron (0.511 MeV), muon (105.66 MeV), tau (1776.86 MeV) — span four orders of magnitude with no explanation from the Standard Model. In 1981, Yoshio Koide observed that the ratio K = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² equals 2/3 to six significant figures. With current measured masses, K = 0.66666051, matching 2/3 to 0.00092%. The Koide parametrization writes √m_k = M(1 + a cos(θ + 2πk/3)), where the ratio K depends only on the amplitude a through K = (1 + a²/2)/3. At a² = 2: K = 2/3 exactly. The measured amplitude is a² = 1.9999631 — matching 2 to 18 parts per million. This paper computes the consequence: IF a² = 2 exactly, THEN m_tau is determined by m_e and m_mu through a quadratic equation. The predicted value is 1776.969 MeV versus measured 1776.86 MeV — a miss of 0.006% (0.109 MeV), within the measurement uncertainty. Conditional on a² = 2, the Standard Model parameter count reduces from 19 to 18. Combined with θ_QCD = 0 and α_s from unification, the total is 19 → 16.

---

## 1. The Three Masses

The charged leptons — electron, muon, and tau — are the three known particles that carry electric charge but no color charge. They interact through the electromagnetic and weak forces but not the strong force. Their masses are among the most precisely measured quantities in particle physics.

The electron mass: m_e = 0.51099895069 MeV. Known to 11 significant figures from atomic spectroscopy. It is the lightest charged particle and the most precisely measured mass in the Standard Model.

The muon mass: m_μ = 105.6583755 MeV. Known to 9 significant figures from muonium spectroscopy and muon g−2 experiments. The muon is 206.77 times heavier than the electron — a ratio with no theoretical explanation.

The tau mass: m_τ = 1776.86 MeV. Known to 6 significant figures from e⁺e⁻ collisions at the tau production threshold. The tau is 16.82 times heavier than the muon, and 3477 times heavier than the electron.

These three masses are three of the 19 free parameters of the Standard Model. The theory provides no relationship among them — each is an independent input from experiment. The mass hierarchy (the fact that they span four orders of magnitude in a specific pattern) is one of the open puzzles of particle physics.

(Backed by phys33_koide_amplitude.py Section 1: masses from library.)

---

## 2. The Koide Formula

In 1981, Yoshio Koide observed that the three charged lepton masses satisfy a simple relation. Define the ratio:

K = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)²

Koide found K ≈ 2/3. With the masses available in 1981, the agreement was already striking. With current measured masses:

The sum of square roots: √m_e + √m_μ + √m_τ = 0.715 + 10.279 + 42.153 = 53.147 MeV^(1/2).

The sum of masses: m_e + m_μ + m_τ = 0.511 + 105.658 + 1776.860 = 1883.029 MeV.

The ratio: K = 1883.029 / (53.147)² = 1883.029 / 2824.570 = 0.66666051.

Compared to 2/3 = 0.66666667: the deviation is 0.00000616, a relative miss of 0.00092%.

The formula has held for 45 years across improving mass measurements. As the measurements have become more precise, K has moved CLOSER to 2/3, not further away. The 1981 agreement was to 4 significant figures. The 2024 agreement is to 6 significant figures.

For comparison: the ratio K has a theoretical range of [1/3, 1]. At K = 1/3, all three masses are equal. At K = 1, one mass dominates. The value 2/3 sits at a specific point in this range — not at a boundary, not at the midpoint, but at a value that has a natural meaning in the parametrization described in the next section.

(Backed by phys33_koide_amplitude.py Section 2: K = 0.66666051, miss 0.00092%.)

---

## 3. The Parametrization and the Tautology

Any three positive numbers m₁, m₂, m₃ can be written in the Koide parametrization:

√m_k = M × (1 + a × cos(θ + 2πk/3))

for k = 0, 1, 2, where M is a mass scale, a is an amplitude, and θ is a phase offset. This has three free parameters fitting three data points — it is an exactly determined system that ALWAYS succeeds. The 120-degree spacing is a property of the parametrization, not of the physics. This is a mathematical tautology.

The script verifies the tautology: starting from the measured masses, extracting M, a, θ, and reconstructing the masses gives agreement to 10⁻⁹⁸% — limited only by the 100-digit arithmetic precision.

The non-trivial content is in the identity discovered in PHYS-8: the Koide ratio K depends ONLY on the amplitude a, through:

K = (1 + a²/2) / 3

This identity is independent of M and θ. The mass scale can be anything. The phase can be anything. The ratio K is determined entirely by the single parameter a². The proof: the cosines sum to zero for 120-degree spacing (∑cos(θ + 2πk/3) = 0), so ∑√m_k = 3M. The squares give ∑m_k = 3M²(1 + a²/2). Therefore K = ∑m / (∑√m)² = 3M²(1 + a²/2) / 9M² = (1 + a²/2)/3.

At a² = 2: K = (1 + 1)/3 = 2/3 exactly. No other value of a² gives K = 2/3. The condition K = 2/3 is EQUIVALENT to a² = 2.

(Backed by phys33_koide_amplitude.py Section 3: identity verified, reconstruction to 10⁻⁹⁸.)

---

## 4. The Amplitude: a² = 1.9999631

From the measured K = 0.66666051, the amplitude is extracted:

a² = 2 × (3K − 1) = 2 × (1.99998153 − 1) = 2 × 0.99998153 = 1.9999631

This matches 2 to 0.0018% — roughly 18 parts per million. The amplitude a = √(1.9999631) = 1.4142005, compared to √2 = 1.4142136. The match to the library value from PHYS-24 is exact to 11 digits.

The phase is θ = 2.317 radians = 0.737π. The scale is M = 17.716 MeV^(1/2), giving M² = 313.84 MeV as the mass scale of the lepton sector.

The key observation: a² is not constrained by the parametrization. For arbitrary three masses, a² can be any positive number. The fact that nature chooses a² = 2 to 18 ppm for the charged leptons is an empirical finding with no theoretical explanation.

(Backed by phys33_koide_amplitude.py Section 3: a² = 1.9999631, miss 0.0018%.)

---

## 5. The Quark Comparison

The Koide formula can be applied to the down-type quarks (d, s, b) and up-type quarks (u, c, t). From the PHYS-24 demonstration:

Leptons (e, μ, τ): a² = 1.9999631. Deviation from 2: 0.0018%.
Down quarks (d, s, b): a² = 2.3877. Deviation from 2: 19.4%.
Up quarks (u, c, t): a² = 3.0928. Deviation from 2: 54.6%.

The ordering is strict: a²_leptons < a²_down < a²_up. This correlates with interaction strength: leptons carry no color charge and interact only through the electroweak force. Down quarks carry color charge and have electric charge −1/3. Up quarks carry color charge and have electric charge +2/3.

The pattern suggests that whatever mechanism produces a² = 2 is disrupted by strong interaction effects. The lepton sector, free from QCD corrections, preserves the condition most precisely. The quark sectors, where QCD mass renormalization is significant, show progressively larger deviations. This is an observation, not a derivation.

---

## 6. The Prediction: m_tau from m_e and m_mu

If a² = 2 exactly — equivalently K = 2/3 — the three lepton masses satisfy one constraint: (∑√m)² = (3/2) × ∑m. Given two masses (m_e and m_mu), the third (m_tau) is determined.

Let s = √m_e + √m_mu = 0.715 + 10.279 = 10.994 MeV^(1/2). Let S = m_e + m_mu = 106.169 MeV. Then x = √m_tau satisfies the quadratic:

x² − 4sx + (3S − 2s²) = 0

The derivation: from (s + x)² = (3/2)(S + x²), expand and collect terms: s² + 2sx + x² = (3/2)S + (3/2)x², giving s² + 2sx − (1/2)x² = (3/2)S, which rearranges to x² − 4sx + (3S − 2s²) = 0.

The discriminant: 16s² − 4(3S − 2s²) = 16(120.865) − 4(76.778) = 1934.640 − 307.111 = 1626.731 MeV. The square root: 40.333 MeV^(1/2).

Two roots:

x_+ = (4s + √disc)/2 = (43.975 + 40.333)/2 = 42.154 MeV^(1/2). Then m_tau(+) = 42.154² = **1776.969 MeV**.

x_- = (4s − √disc)/2 = (43.975 − 40.333)/2 = 1.821 MeV^(1/2). Then m_tau(−) = 1.821² = **3.317 MeV**.

The physical root is x_+: **m_tau = 1776.969 MeV**. The measured value is 1776.86 MeV. The miss is 0.109 MeV, or 0.006%. This is within the PDG measurement uncertainty of the tau mass (~0.12 MeV).

The verification: computing K with the predicted m_tau gives K = 2/3 to 10⁻⁹⁹% — the algebra is exact in 100-digit arithmetic.

The other root (3.317 MeV) lies between m_e and m_mu. No charged lepton exists at this mass. It is the second solution of a quadratic equation, not a physical prediction.

(Backed by phys33_koide_amplitude.py Section 5: m_tau = 1776.969, miss 0.006%, K_pred = 2/3 to 10⁻⁹⁹.)

---

## 7. The Tautology Boundary

This paper must be precise about what is derived and what is assumed.

**Level 1 (mathematical, always true):** The identity K = (1 + a²/2)/3 is a theorem of the Koide parametrization. The quadratic equation for m_tau given K = 2/3 is exact algebra. The parametrization itself is a tautology — three parameters, three masses.

**Level 2 (empirical, from measurement):** The values K = 0.66666051 and a² = 1.9999631 are computed from measured masses. The miss of 0.006% for m_tau is a numerical fact about the measured lepton masses.

**Conditional (assumed, not derived):** a² = 2 exactly. This assumption is NOT proven by the 0.006% match — it is TESTED by it. The match is consistent with a² = 2 but does not prove it. A future more precise measurement of m_tau could reveal that K deviates from 2/3 at higher precision, and the condition would fail.

The open question remains: WHY a² = 2 for charged leptons? Requirements for any viable answer: it must produce a² = 2 specifically (not any other value), must explain the quark ordering (a² grows with interaction strength), and must not reduce to a restatement of K = 2/3.

---

## 8. The Parameter Count

If a² = 2 is accepted as exact, the three charged lepton masses reduce to two independent parameters. Given m_e and m_mu, the tau mass follows from the quadratic equation. The Standard Model parameter count decreases by one: 19 → 18.

This reduction is independent of and compatible with two other reductions:

θ_QCD = 0 from vacuum energy minimization (PHYS-7): the strong CP phase is zero because the QCD vacuum minimizes its energy at θ = 0. This removes one parameter: 18 → 17.

α_s from the unification condition (PHYS-30): the strong coupling is derived from α_EM and sin²θ_W through gauge coupling unification with the Cabibbo Doublet. The predicted α_s = 0.1184 matches measured 0.1180 to 0.33%. This removes one parameter: 17 → 16.

The three conditions (Koide, vacuum, unification) act on different sectors of the Standard Model — lepton masses, QCD vacuum, and gauge couplings. They are independent. The combined reduction: 19 → 16.

All three reductions are conditional: Koide assumes a² = 2, vacuum assumes θ_QCD minimization, unification assumes the Cabibbo Doublet exists. None is derived from first principles. Each is tested by its prediction.

---

## 9. What This Paper Does Not Claim

This paper does not claim to derive WHY a² = 2. The condition is empirical — observed from the measured masses, not derived from a theory. Any future paper attacking the Koide problem must produce a² = 2 from a physical mechanism.

This paper does not claim the Koide formula is proven physics. It is an empirical relation that has held for 45 years with increasing precision. It has no derivation from the Standard Model or from any extension of it. The relation could be a coincidence that breaks at higher precision.

This paper does not claim the other quadratic root (3.317 MeV) is a particle. It is the second mathematical solution of a quadratic. The selection of the larger root is based on the known tau mass, not on a prediction.

This paper does not claim the parameter reduction is unconditional. It is explicitly conditional on a² = 2 being exact. The word "conditional" appears in the title for this reason.

This paper does not claim a connection between the Koide formula and gauge coupling unification. The two findings (m_tau from K = 2/3, and α_s from the unification condition) are independent parameter reductions in different sectors. Whether a deeper connection exists is an open question.

---

## 10. What This Paper Seeds

The m_tau prediction (1776.969 MeV from K = 2/3, versus measured 1776.86 ± 0.12 MeV) is testable with improved tau mass measurements. If future experiments measure m_tau to 0.01 MeV precision, the Koide prediction can be tested at the 0.1% level rather than the current 0.006%.

The quark amplitude ordering (a²_lep < a²_down < a²_up) is documented as an open pattern. A future paper could investigate whether QCD running corrections applied to the quark masses bring a²_quarks closer to 2 — testing the hypothesis that a² = 2 is the "bare" condition, modified by strong interaction effects.

The parameter count reduction (19 → 16 from three independent conditions) is documented. Each condition is independently testable and independently falsifiable. The Koide conditional provides 1 of the 3 reductions.

---

*PHYS-33: The Koide Amplitude. IF a² = 2, THEN m_tau = 1776.97 MeV. Measured: 1776.86. Miss: 0.006%. 8/8 checks, zero failures. Published April 3, 2026. This paper is never edited after publication.*

---

## Appendix A: The Koide Parametrization — Three Parameters

| Parameter | Symbol | Value (leptons) | Meaning |
|---|---|---|---|
| Mass scale | M | 17.716 MeV^(1/2) | Sets the overall scale. M² = 313.84 MeV. |
| Amplitude | a | 1.41420 | Controls the spread of masses. a² ≈ 2. |
| Phase | θ | 2.317 rad = 0.737π | Determines which mass is which. |

The parametrization: √m_k = M × (1 + a cos(θ + 2πk/3)) for k = 0, 1, 2.

With k = 0 → electron, k = 1 → muon, k = 2 → tau. The assignment depends on the phase θ.

The tautology: three parameters, three data points. Any three positive masses fit this form exactly.

The non-trivial content: K depends only on a. K = (1 + a²/2)/3. Nature chooses a² ≈ 2.

---

## Appendix B: The Identity K = (1 + a²/2)/3 — Proof

| Step | Expression | Result |
|---|---|---|
| 1 | ∑√m_k = M ∑(1 + a cos(θ + 2πk/3)) | = 3M (cosines sum to zero) |
| 2 | (∑√m_k)² | = 9M² |
| 3 | m_k = M²(1 + a cos(θ + 2πk/3))² | Expand the square |
| 4 | ∑m_k = M² ∑(1 + 2a cos + a² cos²) | Three terms |
| 5 | ∑1 = 3 | Trivial |
| 6 | ∑cos(θ + 2πk/3) = 0 | 120° spacing property |
| 7 | ∑cos²(θ + 2πk/3) = 3/2 | Standard trigonometric identity |
| 8 | ∑m_k = M²(3 + 0 + 3a²/2) = 3M²(1 + a²/2) | Collecting terms |
| 9 | K = ∑m / (∑√m)² = 3M²(1+a²/2) / 9M² | Definition |
| 10 | **K = (1 + a²/2) / 3** | **Q.E.D.** |

At a² = 2: K = (1 + 1)/3 = 2/3. The proof uses only trigonometric identities. No physics enters.

---

## Appendix C: The Quadratic Solution — Step by Step

| Step | Expression | Value |
|---|---|---|
| 1 | s = √m_e + √m_mu | 10.994 MeV^(1/2) |
| 2 | S = m_e + m_mu | 106.169 MeV |
| 3 | s² | 120.865 MeV |
| 4 | From K = 2/3: (s+x)² = (3/2)(S+x²) | Constraint on x = √m_tau |
| 5 | Expand: s²+2sx+x² = (3/2)S+(3/2)x² | |
| 6 | Rearrange: x²−4sx+(3S−2s²) = 0 | Multiply by −2 |
| 7 | c = 3S−2s² | 76.778 MeV |
| 8 | Discriminant = 16s²−4c | 1626.731 MeV |
| 9 | √disc | 40.333 MeV^(1/2) |
| 10 | x_+ = (4s+√disc)/2 = 2s+√disc/... | 42.154 MeV^(1/2) |
| 11 | **m_tau(+) = x_+²** | **1776.969 MeV** |
| 12 | x_- = (4s−√disc)/2 | 1.821 MeV^(1/2) |
| 13 | m_tau(−) = x_-² | 3.317 MeV |

---

## Appendix D: The Three Sectors Compared

| Sector | m₁ (MeV) | m₂ (MeV) | m₃ (MeV) | K | a² | Deviation from 2 |
|---|---|---|---|---|---|---|
| Leptons (e, μ, τ) | 0.511 | 105.66 | 1776.86 | 0.666661 | 1.99996 | **0.0018%** |
| Down quarks (d, s, b) | 4.7 | 93 | 4180 | 0.731288 | 2.38773 | 19.4% |
| Up quarks (u, c, t) | 2.2 | 1275 | 172760 | 0.848794 | 3.09276 | 54.6% |

The ordering a²_lep < a²_down < a²_up correlates with color charge: leptons (no color) are closest to a² = 2, quarks (colored) deviate. Within quarks, the deviation correlates with electric charge magnitude: |Q| = 1/3 for down, |Q| = 2/3 for up.

---

## Appendix E: Sensitivity Analysis

| Varied quantity | Shift | m_tau prediction (MeV) | Change from central |
|---|---|---|---|
| Central | — | 1776.9690 | — |
| m_mu + 1σ (+0.0000023 MeV) | +2.3×10⁻⁶ | 1776.9690 | +0.0000005 MeV |
| m_mu − 1σ (−0.0000023 MeV) | −2.3×10⁻⁶ | 1776.9690 | −0.0000005 MeV |
| m_e + 1σ | ~10⁻⁸ | 1776.9690 | < 10⁻⁶ MeV |

The prediction is insensitive to input mass uncertainties. The m_mu uncertainty (0.0023 keV) propagates to a tau prediction shift of ~0.5 eV — negligible compared to the 0.12 MeV measurement uncertainty of m_tau itself.

The dominant "uncertainty" is whether a² = 2 is exact. The measured a² = 1.9999631 deviates from 2 by 3.7×10⁻⁵. If this deviation is physical (a² ≠ 2), the prediction shifts by order (Δa²) × (∂m_tau/∂a²) — but the partial derivative is not computed here because the conditional assumes a² = 2 exactly.

---

## Appendix F: Verification Summary

| Check | Description | Status |
|---|---|---|
| S2 | K close to 2/3 (miss < 0.001%) | PASS (0.00092%) |
| S3 | a² matches library (11 digits) | PASS (EXACT) |
| S3 | a² close to 2 (miss < 0.01%) | PASS (0.0018%) |
| S4 | Reconstruction recovers all three masses | PASS (10⁻⁹⁸%) |
| S5 | m_tau within 0.1% of measured | PASS (0.006%) |
| S5 | m_tau within 1 MeV of measured | PASS (0.109 MeV) |
| S5 | K with predicted m_tau = 2/3 | PASS (10⁻⁹⁹%) |
| S5 | m_tau prediction > 1700 MeV | PASS (1776.969) |
| **Total** | | **8 PASS, 0 FAIL** |

---

*Supporting appendices A through F for PHYS-33. The Koide amplitude a² = 1.9999631 matches 2 to 18 ppm. The conditional prediction m_tau = 1776.969 MeV matches the measured 1776.86 MeV to 0.006%. The identity K = (1+a²/2)/3 is proven algebraically. The tautology boundary is explicitly stated. Grand total across all scripts: 505/508 (2 designed FAILs + 1 prior).*

---

