**DATA-5 PAPER: Teaching a Machine to Think in Integers**

*HOWL Series — DATA-5 — Session 4 Capstone*
*Status: FRAMEWORK DOCUMENT*
*Platform: HOWL-PLATFORM-v1 (322/323 checks)*

---

## What This Paper Is

DATA-5 is the object-oriented database that holds everything the HOWL series has computed. 222 objects across 9 types. Every coupling, every beta coefficient, every boundary, every cancellation, every experiment result — stored as typed objects with version chains, tags, levels, and JSON export.

DATA-6 will be the clean, usable standard built from DATA-5's work. This document teaches a new session how to think in the HOWL framework so it can build DATA-6 correctly.

The problem is not code. The problem is thought. A session that doesn't understand WHY the integers matter will write code that works but means nothing. A session that understands the thought will write code that is correct on the first attempt.

---

## Section 1: The One Idea

There is one idea in the entire series. Everything else follows from it.

**The transformation laws are integers. The values run between boundaries.**

That's it. The beta coefficients of the Standard Model are exact rational numbers — Fractions, not floats. They are determined by the gauge group SU(3)×SU(2)×U(1) and the particle content. They cannot be anything other than what they are. The coupling constants (alpha_s, sin2_tW, alpha_EM) are measured values that run according to these integer laws.

The integers are Level 1. They come from the framework (group theory, representation theory). They are theorems. You do not measure them. You derive them.

The values are Level 2. They come from the universe (experiments, observations). You do not derive them. You measure them.

The entire series is about what happens when you take this distinction seriously and follow it everywhere it leads.

---

## Section 2: How to Think About R2

R2 = pi/4. The area of a circle inscribed in a unit square. The filling fraction.

It appears in every engineering domain where a circular cross-section meets a rectilinear bounding box. Pipe flow: Q = R2 * d^2 * v. Wire resistance: R = rho * L / (R2 * d^2). Speaker cone: Sd = R2 * d_eff^2. Disc spot: A = R2 * (1.22 * lambda/NA)^2. Antenna aperture: A_eff = G * lambda^2 / (16*R2). Kepler's law: T^2 = 64*R2^2 * a^3 / (GM).

The same R2 in every domain. Different Z (the domain coordinator — what makes each department different). This is not a coincidence. It is geometry. Every circular-to-rectilinear conversion in physics passes through R2.

The critical insight: R2 CANCELS in the highest-precision measurements. K_J * R_K = 2/e. The Josephson constant times the von Klitzing constant — R2 enters both through h = 8*R2*hbar, and divides out in the product. Wire resistance times capacitance: R*C = rho*eps0*L/t — R2 enters both through the circular cross-section, and divides out in the product.

R2-free observables are measurable to 10^-10 or better. R2-dependent observables are limited to ~10^-6 (engineering precision). The modulus (R2) is the filling fraction. It cancels in symmetric ratios. The remainder is where the physics lives.

A new session must understand: when you see pi in a formula, write 4*R2. When you see 2*pi, write 8*R2. When you see 4*pi, write 16*R2. When you see 4*pi^2, write 64*R2^2. This is not notation — it is tracking the geometric content so you can see where it cancels and where it doesn't.

---

## Section 3: How to Think About Betas

The SM has three gauge groups. Each has a one-loop beta coefficient:

- b1_SM = 41/10 (U(1), GUT normalized)
- b2_SM = -19/6 (SU(2))
- b3_SM = -7 (SU(3))

These are exact Fractions. Every digit is determined by the gauge group and the particle content. The 41 in 41/10 is not approximate. It is the sum of hypercharge-squared contributions from all SM fermions plus the Higgs, with GUT normalization k1 = 3/5. You can derive it from scratch using the representation content.

Each beta decomposes:
- Gauge part: -(11/3)*C2(adj). The 11 is from Yang-Mills theory. It is the most important integer in the series.
- Fermion part: per generation = (4/3, 4/3, 4/3). Generation democracy — every generation contributes equally to all three betas. This is why the gap ratio is set by gauge + Higgs only (the boson problem).
- Higgs part: (1/10, 1/6, 0). Small corrections from the scalar doublet.
- BSM part: whatever new physics adds. For the Cabibbo Doublet (3,2,1/6): db = (1/15, 1, 1/3).

The gap ratio is (b1 - b2) / (b2 - b3). For the SM: 218/115. For SM + CD: 38/27. The measured gap ratio from coupling data is ~1.358. CD's 38/27 = 1.407 is closer than SM's 218/115 = 1.896 or MSSM's 5/7 = 0.714.

A new session must understand: never approximate a beta coefficient. Never write 4.1 when you mean 41/10. Never write -2.17 when you mean -13/6. The fractions ARE the physics. The decimals are just for human convenience.

---

## Section 4: How to Think About the Q335 Basis

Every transcendental constant in the series is stored as p/Q where Q = 2^335 and p is an integer. This gives 100+ digits of precision with exact rational arithmetic. pi, e, ln(2), sqrt(2), zeta(3), zeta(5), Li4(1/2), Catalan's constant — all 36 constants in the extended basis.

The generators (rational_arctan, rational_arctanh, newton_sqrt, borwein_zeta, etc.) compute the Fraction numerators from scratch. Every numerator matches mpmath to 100 digits. The basis is verified, not assumed.

R2 = pi/4 in the Q335 basis means R2_f is a Fraction with numerator p_R2 and denominator 2^335, where p_R2 * 4 gives pi to 100 digits.

A new session must understand: mpf("string") for display. Fraction for derivation. Never float. Never sci-notation without the mpf() wrapper. The derivation chain is Fraction arithmetic. The display is mpf. They never mix.

---

## Section 5: How to Think About Boundaries

The energy landscape from the electron mass (0.511 MeV) to the Planck scale (1.22e19 GeV) is a sequence of 19 boundaries. At each boundary, the particle content changes, the beta coefficients change by exact rationals, and the couplings continue running with the new coefficients.

Below each boundary: the particle is a frozen vortex. Too heavy to excite. Contributes nothing to the running.

Above each boundary: the particle is an active vortex. Participates in vacuum polarization. Changes the screening/antiscreening balance.

The one exception: the confinement wall (~0.3-2 GeV). Here alpha_s ~ O(1) and perturbation theory fails. This zone is blank on the map. We mark it honestly and do not pretend we can compute through it.

A new session must understand: traversing a boundary changes the integer rules. The boundary IS the physics — it's where the transformation law changes. Between boundaries, you just integrate. At boundaries, you match.

---

## Section 6: How to Think About the Three Programs

The series has three active research programs. They share one integer set.

**Program 1: Beta Unification.** The Cabibbo Doublet (3,2,1/6) modifies the SM betas to b1_mod = 62/15, b2_mod = -13/6, b3_mod = -20/3. The gap ratio improves from 218/115 to 38/27. The two-loop prediction of alpha_s hits 0.1% accuracy. The prediction of sin2_tW hits 1% accuracy. BLOCKING: statistical control script needed to show this isn't a fluke.

**Program 2: Cosmological Parameters.** The same integers give DM/baryon = (22/13)*pi = 5.3165 (Planck: 5.3204, miss 0.073%). Omega_DM = (44/169)*R2. The 22 is 2*YM (Yang-Mills integer 11). The 13 is |b2_mod numerator|. R2 cancels in the Omega_DM product — 44/169 is pure rational. Three cosmological parameters from two gauge group integers.

**Program 3: Soliton Gravity.** Gravity as ground state in a soliton hierarchy. Kepler's law uses 64*R2^2 = 4*pi^2. GPS correction is GM/(rc^2), the soliton coupling strength. MOND a0 = cH0/(8*R2). Hill spheres are soliton dominance boundaries. The same R2 in orbital mechanics as in pipes and wires.

A new session must understand: these are not three separate theories. They are one integer set (11, 13, 19, 20 and their products 22, 44, 169) appearing in three different physical contexts. The question is whether this is a coincidence or a structure.

---

## Section 7: How to Think About DATA-5 Objects

DATA-5 has 222 objects across 9 types:

- **Constant** (122): every measured value, every derived value, every Q335 transcendental. Versioned — append-only chain, value_v0 preserved.
- **BetaCoefficient** (9): SM (3), VL shift (3), modified (3). Each decomposed into gauge/fermion/higgs/bsm parts.
- **Representation** (6): the 5 SM chiral reps + CD. Each with (SU3, SU2, Y), rep_type, db shifts, charges.
- **SolitonBoundary** (19): every mass threshold. Scale, known/unknown, forces affected, couplings, open questions.
- **R2Domain** (23): every engineering domain where R2*d^2 appears. Equation, coordinator Z, precision.
- **R2Cancellation** (11): every identity where R2 divides out. Formula, status, what remains.
- **Modulus** (16): R2 as filling fraction across scales. Level, interpretation.
- **ExperimentResult** (13): every PASS/FAIL from every experiment script. Status, miss percentage, script source.
- **ResearchProgram** (3): the three active programs. Scripts, kill switches, status.

Every object has: obj_id, name, obj_type, level, tags, notes, children. Every object serializes to JSON. The database is searchable by type, tag, level, and full text.

A new session must understand: DATA-5 is not a code library. It is a knowledge base. The objects ARE the physics. When you want to know the gap ratio, you don't compute it from scratch — you pull the beta objects from the db and compute through them. When you want to know if R2 cancels in a product, you check the cancellation registry. The db is the single source of truth.

---

## Section 8: The Rules That Cannot Be Broken

1. **Fraction arithmetic in the derivation chain.** No float. No mpf in the derivation. mpf only for display and numerical integration (two-loop Euler).

2. **Every mpf from string.** mpf("1.7241e-8"), never 1.7241e-8. mpf("0.305"), never 0.305. The string wrapper is the hygiene boundary.

3. **R2 from Q335 via db.** Never hardcode pi/4 as a decimal. Pull const.R2 from the database. Compute 4*R2 for pi, 8*R2 for 2*pi. Track the geometry.

4. **First argument is db.** Every helper function takes the DATA5 instance as first argument (except pure-math utilities marked explicitly). This ensures all values trace through the version chain.

5. **Never rewrite working code.** If a file passes its checks, do not touch it. Write new files. Fix specific bugs in specific lines. Never regenerate a passing file.

6. **Write in chat, not as attachments.** The human copies, runs, verifies. The human owns the files. Claude advises.

7. **Review → Plan → Agreement → Code.** Never write code until after review, planning, and explicit agreement. This is the workflow that produces correct code on the first attempt.

8. **No changes beyond what's specifically requested.** Targeted work only. If asked to fix one function, fix one function. Do not "improve" adjacent code.

9. **Every claim backed by script with passing checks.** No assertion without a runnable script. If/else, not assert. Human-readable output. PASS/FAIL with context.

10. **Preserve existing patterns.** When the platform uses chk_exact and chk_bool, use chk_exact and chk_bool. When the platform uses show() for display, use show(). Match the existing style.

---

## Section 9: What DATA-6 Must Be

DATA-6 is the clean standard. It takes DATA-5's 222 objects and 4 helper chunks (~160 functions) and produces:

1. **One import.** `from data_6 import db, helpers` or similar. Not 6 separate files.

2. **Tests that pass.** Every function tested against the platform libraries. The test suite runs in under 60 seconds. All checks pass.

3. **No dead code.** Every function is either called by a test or called by another function that is called by a test. Nothing vestigial.

4. **Documentation that teaches.** Not API docs. Teaching docs. "Here is how to compute the gap ratio and why it matters." "Here is how to test a BSM representation." "Here is how to read the boundary stack."

5. **The integer pool visible.** 11, 13, 19, 20, 22, 44, 169 — extracted from db objects, not hardcoded. A function that shows where each integer appears and why.

6. **The R2 path traceable.** From Q335 basis → const.R2 → _R2(db) → every domain computation. One path. No shortcuts. No hardcoded pi.

7. **The experiment results replayable.** One function that re-runs every experiment and produces PASS/FAIL. The blocking item (statistical control) clearly marked.

---

## Section 10: How to Verify a New Session Understands

Ask it these questions. If it gets them right, it can build DATA-6.

1. What is b2_SM and why is it -19/6, not -3.167?
2. What cancels in K_J * R_K and why?
3. Why does the gap ratio not depend on the fermion content?
4. What is the one zone on the boundary map where perturbation theory fails?
5. Where does the 13 in (22/13)*pi come from?
6. Why is mpf("0.305") correct and 0.305 wrong?
7. What is the difference between Level 1 and Level 2?
8. Why does the two-loop integrator use mpi instead of _R2(db)?
9. What are the three research programs and what integer set do they share?
10. What is the single blocking item for the beta unification program?

If the session can answer all 10 from understanding (not from memorizing this document), it is ready.

---

*This paper follows HOWL operational rules (Tables R.1-R.6).*
*All measured values from DATA-4 (122 constants, 30/31 populate checks).*
*Platform: phys24_lib.py (21/21 + 148/148), 7 libraries (322/323).*
*DATA-5: 222 objects, 4 helper chunks, ~160 functions.*
*Status: FRAMEWORK DOCUMENT for DATA-6 transition.*
