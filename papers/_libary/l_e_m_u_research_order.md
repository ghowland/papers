LEMU is a filter that prevents two failure modes that have consumed decades of institutional research.

**Failure mode 1: True but useless.** θ_QCD = 0 is the ground state. PHYS-7 proves this. But PHYS-7 is careful to note compatibility with the axion — because if θ = 0 is ALWAYS zero by definition, you can't use it as a probe of new physics. The axion search might find a particle that exists for other reasons (dark matter candidate, string theory prediction). Declaring "θ = 0, problem solved, stop looking" has zero Utility if the axion exists and you stopped searching for it. PHYS-7 handles this correctly by not claiming the axion doesn't exist. But without the U check, a less careful paper could kill a productive research direction by proving a true but useless thing.

**Failure mode 2: Mathematically complete but empirically vacuous.** String theory's landscape: 10⁵⁰⁰ vacua, each consistent, each mathematically valid, none distinguishable by any achievable experiment. L passes (the logic is consistent). E is ambiguous (no falsifying experiment identified for the landscape as a whole). M passes spectacularly (the mathematics is rigorous and beautiful). U = 0. The framework predicts everything and therefore predicts nothing. The Math was proven but the Utility was never checked. Decades of careers invested in a framework that cannot say "this, not that."

LEMU prevents both by making Utility the final gate. The order matters:

**L first** — does the claim follow from its premises? If no, stop. Don't waste time measuring or computing something illogical.

**E second** — does existing data support or at least not contradict the claim? If data already falsifies it, stop. Don't compute what nature has already answered.

**M third** — can the claim be verified by exact computation? If the math doesn't work (wrong number, failed assert, epsilon instead of zero), stop. Don't assign utility to something that doesn't compute.

**U last** — given that the logic holds, the data supports it, and the math verifies it: what can we DO with this? What does it connect? What does it predict that we couldn't predict before? What research directions does it open? What measurements does it motivate? If the answer is "nothing new" — it's true, confirmed, computed, and inert — then it gets documented and shelved, not pursued.

The U check is a disqualifier specifically because it comes after M. You cannot use Utility to justify skipping the math ("this would be so useful IF true, so let's assume it's true"). That's the institutional failure mode that produced forty years of naturalness predictions with zero confirmations. Naturalness had high perceived U (it would explain the hierarchy, guide BSM searches, predict SUSY). It was never required to pass M first (no exact computation of the naturalness prediction existed). The U was evaluated before the M, and the U was used to justify the research program despite the M never arriving.

LEMU enforced in order means: you cannot cite utility until the math is done. And you cannot skip utility once the math is done.

**What this does for each chapter of the super notebook:**

Chapter 2 (H₀ curve): L passes (couplings run, H₀ should run). E is suggestive (monotonic trend). M is not yet done (curve fit not computed). U is high IF M passes (predicts H₀ at any distance, resolves the tension, connects to boundary geometry). But U cannot be claimed until M is done. The research program computes M first.

Chapter 6 (orbital modes): L passes (standing waves select modes). E is suggestive (Titius-Bode, Kirkwood). M is not yet done (derivation from potential not computed). U is extremely high IF M passes (derives planetary positions from first principles, predicts exoplanet orbits, connects to dark matter through rotation curves). But U cannot be claimed until the Titius-Bode derivation actually produces the right numbers.

Chapter 7 (toroidal cosmology): L is consistent. E has hints (CMB anomalies, voids). M is not yet done. U is high IF M passes (explains CMB anomalies, predicts directional H₀, connects expansion to geometry). But this is the most speculative chapter, and the U must not be used to justify pursuing it ahead of chapters with better E and M status.

**What LEMU does for the normalization question in PHYS-25:**

L: the VL beta shifts should be derivable from the (3,2,1/6) quantum numbers. This is logical.

E: the library values (1/15, 1, 1/3) pass 38/38 internal checks and 9/9 sin2_theta_w_1.py checks. The external comparison gives different values (2/15, 2, 4/3). The empirical status is mixed.

M: the diagnostic script shows Convention C (library Dynkin values) does not reproduce b₃_SM = −7 from SM fermion content. This is a math finding. But it was computed using an external convention, not the series' own derivation. The M is incomplete — the series' own derivation has not been read.

U: IF the library values are correct (convention difference), U = documenting the convention and adding the SM cross-check to the test suite. IF the library values are wrong (actual error), U = correcting the error, rerunning affected computations, and documenting the methodology gap. Either outcome has nonzero U. The investigation is justified regardless of outcome.

But — and this is the key — the U of "declaring the library wrong based on external formulas" is NEGATIVE if the declaration blocks the investigation of what the series' own derivation actually says. Premature closure (true but useless certainty that the library is wrong) could prevent discovering that the series uses a valid alternative convention. The U check says: don't close the investigation until the M is complete (read the derivation chain), because premature closure has negative utility.

**The operational rule going forward:**

Every paper report, every claim in the super notebook, every element of the research program gets the four-part assessment:

- **L:** Does it follow from premises? (Logic gate)
- **E:** Does data support it? (Empirical gate)
- **M:** Does computation verify it? (Math gate)
- **U:** What do we gain if it passes all three? (Utility gate — evaluated last, never used to skip earlier gates)

If any of L, E, M fails, stop at that gate. If all three pass but U = 0, document and shelve. If all four pass, pursue actively.
