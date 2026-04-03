## PHYS-33 Paper Plan

**Title:** The Koide Amplitude — m_tau from Two Masses and One Condition
**Subtitle:** IF a² = 2, THEN m_tau = 1776.97 MeV. Measured: 1776.86 MeV. Miss: 0.006%.

**Registry:** @HOWL-PHYS-33-2026
**Date:** April 3 2026
**Domain:** Lepton Mass Relations, Conditional Parameter Reduction

---

### WHAT THE SCRIPT TELLS US

The script computes the Koide formula K = sum_m / (sum_sqrt)² for the three charged lepton masses, extracts the amplitude parameter a² from the identity K = (1 + a²/2)/3, and predicts m_tau from m_e and m_mu conditional on K = 2/3 exactly.

Results from the output:

1. K = 0.66666051 vs 2/3 = 0.66666667. Miss: 0.00092%.
2. a² = 1.9999631 vs 2. Miss: 0.0018%.
3. The parametrization sqrt(m_k) = M(1 + a cos(θ + 2πk/3)) reconstructs all three masses to 10⁻⁹⁸% — the tautology is verified (3 parameters, 3 data points, exact fit).
4. Setting K = 2/3 exactly and solving for m_tau: the quadratic x² − 4sx + (3S − 2s²) = 0 gives two roots. The physical root: m_tau = 1776.969 MeV. Measured: 1776.86 MeV. Miss: 0.006% (0.109 MeV).
5. The predicted m_tau satisfies K = 2/3 to 10⁻⁹⁹% — essentially exact in 100-digit arithmetic.
6. The other quadratic root: m = 3.317 MeV. Not a known particle.
7. The phase θ = 0.737π radians. The scale M = 17.72 MeV^(1/2).

---

### WHAT THE PAPER MUST EXPLAIN

A reader who has never seen any HOWL paper needs:

1. **What the Koide formula is:** An empirical relation among the three charged lepton masses discovered by Yoshio Koide in 1981. The ratio K = (m_e + m_mu + m_tau) / (√m_e + √m_mu + √m_tau)² equals 2/3 to six significant figures. No theoretical derivation exists.

2. **What the parametrization is:** Any three positive masses can be written as sqrt(m_k) = M(1 + a cos(θ + 2πk/3)) with three parameters (M, a, θ). This is a tautology — 3 parameters fit 3 data points exactly. The non-trivial content is that K depends ONLY on a, through K = (1 + a²/2)/3. K = 2/3 when a² = 2. The phase θ determines which masses, but the ratio K is phase-independent.

3. **What the conditional claim is:** IF a² = 2 exactly, THEN m_tau is a function of m_e and m_mu. Given the measured electron and muon masses, the tau mass follows from a quadratic equation. The predicted value (1776.97 MeV) matches the measured value (1776.86 MeV) to 0.006%.

4. **What this does NOT explain:** WHY a² = 2. The paper computes the consequence of the condition, not its origin. The condition is empirical. The parameter reduction (19 → 18) is contingent on the condition holding.

---

### THE PAPER STRUCTURE

**Section 1: The Three Masses**

The charged leptons — electron, muon, tau — have masses spanning four orders of magnitude: 0.511 MeV, 105.66 MeV, 1776.86 MeV. These three masses are three of the 19 free parameters of the Standard Model, determined by experiment. The mass hierarchy (m_tau/m_e ≈ 3477) is unexplained — the Standard Model provides no relationship among them.

In 1981, Yoshio Koide observed that the ratio K = (m_e + m_mu + m_tau) / (√m_e + √m_mu + √m_tau)² is remarkably close to 2/3. With current measured masses, K = 0.66666051 — matching 2/3 to 0.00092%. This is far more precise than the individual mass measurements warrant and suggests a structural relationship.

Script backing: Section 1 (masses from library), Section 2 (K computed, miss 0.00092%).

---

**Section 2: The Parametrization and the Tautology**

The Koide parametrization writes the square root of each mass as sqrt(m_k) = M × (1 + a × cos(θ + 2πk/3)) for k = 0, 1, 2. This has three free parameters: M (the mass scale), a (the amplitude), and θ (the phase offset). Three parameters fitting three data points is an exactly determined system. It ALWAYS succeeds for any three positive masses. This is a mathematical tautology, not physics.

The script verifies the tautology: the reconstruction recovers all three masses to 10⁻⁹⁸% precision — limited only by the 100-digit arithmetic.

The non-trivial content: the ratio K depends ONLY on the amplitude a, through the identity K = (1 + a²/2)/3. This identity is independent of M and θ. The mass scale and the phase can be anything — K is determined by a alone. At a² = 2: K = (1 + 1)/3 = 2/3 exactly.

Script backing: Section 3 (identity verified), Section 4 (reconstruction to 10⁻⁹⁸%).

---

**Section 3: The Amplitude a² = 2**

From the measured K = 0.66666051, the amplitude is a² = 2(3K − 1) = 1.9999631. This misses 2 by 0.0018% — roughly 18 parts per million. The amplitude a = 1.41420 compared to √2 = 1.41421.

The measured a² matches the library value from PHYS-24 exactly (11 digits). The quark sectors show larger deviations: a²(down quarks) = 2.39, a²(up quarks) = 3.09. The lepton sector is special — only for leptons does a² ≈ 2 hold at the parts-per-million level.

Script backing: Section 3 (a² = 1.9999631, miss 0.0018%, matches library).

---

**Section 4: The Prediction — m_tau from m_e and m_mu**

If a² = 2 exactly (K = 2/3), the three masses satisfy: (sum_sqrt)² = (3/2) × sum_m. With s = √m_e + √m_mu and S = m_e + m_mu known from measurement, √m_tau satisfies the quadratic:

x² − 4sx + (3S − 2s²) = 0

This has two roots: x_+ = 42.154 MeV^(1/2) giving m_tau(+) = 1776.969 MeV, and x_- = 1.821 MeV^(1/2) giving m_tau(-) = 3.317 MeV.

The physical root: m_tau = 1776.969 MeV. Measured: 1776.86 MeV. Miss: 0.006% (0.109 MeV). The prediction is within the measurement uncertainty of m_tau (~0.12 MeV from PDG).

The verification: computing K with the predicted m_tau gives K = 2/3 to 10⁻⁹⁹% — essentially exact, confirming the algebra.

The other root (3.317 MeV) lies between m_e and m_mu. No charged lepton exists at this mass. It is the mathematical second solution of a quadratic, not a physical prediction.

Script backing: Section 5 (all values, quadratic solved, K verified to 10⁻⁹⁹).

---

**Section 5: The Tautology Boundary**

The paper must be clear about what is proven and what is assumed.

PROVEN (Level 1): The identity K = (1 + a²/2)/3 is a mathematical theorem. It holds for any three positive masses in the Koide parametrization. The quadratic solution for m_tau given K = 2/3 is exact algebra.

MEASURED (Level 2): K = 0.66666051 from the three measured masses. a² = 1.9999631 from K. The miss of 0.006% for m_tau.

ASSUMED (conditional): a² = 2 exactly. This is an empirical observation with no theoretical derivation. The paper documents its consequence (m_tau = 1776.97 MeV) but does not claim to derive it.

The distinction matters: the 120-degree spacing in the parametrization is a tautology (always works for 3 masses). The amplitude a² = 2 is not a tautology — it is a specific numerical claim about nature. The open question is WHY a² = 2 for leptons.

---

**Section 6: The Quark Comparison**

The Koide formula can be applied to the down-type quarks (d, s, b) and up-type quarks (u, c, t). The results from PHYS-24: a²(down) = 2.388, a²(up) = 3.093. Both deviate significantly from 2. The ordering a²_lep < a²_down < a²_up correlates with interaction strength — leptons (no color charge) are closest to a² = 2, down quarks (color + charge −1/3) are next, up quarks (color + charge +2/3) are furthest.

This ordering suggests that whatever mechanism produces a² = 2 is disrupted by strong interaction effects. The lepton sector, free from QCD, preserves the condition most precisely. This is an observation, not a derivation.

---

**Section 7: The Parameter Count**

If a² = 2 is accepted as exact, m_tau follows from m_e and m_mu. The three charged lepton masses reduce to two independent parameters. The Standard Model parameter count: 19 → 18.

Combined with θ_QCD = 0 from vacuum energy minimization: 18 → 17.
Combined with α_s from the unification condition (PHYS-30): 17 → 16.

Total: 19 → 16. Three parameters derived from conditions rather than measured independently. The reductions are from three independent conditions: Koide (lepton masses), QCD vacuum (θ_QCD), and unification (gauge couplings).

---

**Section 8: What This Paper Does Not Claim**

This paper does not claim to derive WHY a² = 2. The condition is empirical. Any future paper attacking the Koide problem must produce a² = 2 from a physical mechanism, explain the quark ordering, and not reduce to a restatement of K = 2/3.

This paper does not claim the Koide formula is proven physics. It is an empirical observation that has held for 45 years and has become MORE precise as mass measurements improve, but it has no theoretical derivation.

This paper does not claim the other quadratic root (3.317 MeV) is a particle prediction. It is the second mathematical solution of a quadratic equation. The physical selection of the larger root is based on the known tau mass.

This paper does not claim the parameter reduction is unconditional. It is explicitly conditional on a² = 2 being exact. If a² deviates from 2 at higher precision, the reduction fails.

---

**Section 9: What This Paper Seeds**

The Koide conditional is independent of the unification program (Track A). It reduces the parameter count by a different mechanism — a mass relation among leptons, not a coupling relation among gauge forces. The two reductions are compatible and additive.

The open question (WHY a² = 2) is documented. Requirements for any future answer: must produce a² = 2 specifically, must explain the quark ordering, must not reduce to K = 2/3 restated.

The other quadratic root (3.317 MeV) is documented. If a particle at this mass were ever discovered, it would be a spectacular confirmation.

---

### THE APPENDICES

**Appendix A:** The Koide parametrization — the three parameters M, a, θ with derivation
**Appendix B:** The PHYS-8 identity K = (1 + a²/2)/3 — algebraic proof
**Appendix C:** The quadratic solution — step by step
**Appendix D:** The three sectors compared — leptons, down quarks, up quarks
**Appendix E:** Sensitivity analysis — how input uncertainties propagate
**Appendix F:** Verification summary (8/8 PASS)

---

### ESTIMATED LENGTH

Body: 9 sections, approximately 4500 words.
Appendices: 6 tables, approximately 1200 words.
Total: approximately 5700 words.

---

### THE ONE-SENTENCE SUMMARY

PHYS-33 says: the Koide amplitude a² = 1.9999631 matches 2 to 18 parts per million, and conditional on a² = 2 exactly, the tau mass is predicted from the electron and muon masses as m_tau = 1776.97 MeV versus measured 1776.86 MeV — a miss of 0.006% (0.109 MeV), within the measurement uncertainty, reducing the SM parameter count from 19 to 18.
