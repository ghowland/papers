# PCTRM-2: Entanglement Channels in the Substrate Graph

**Registry:** HOWL-PCTRM-2-2026
**Parent Specification:** PCTRM-1-2026
**Companion Paper:** PHYS-54-2026
**Date:** April 20, 2026
**Domain:** Speculative Physics / Discrete Substrate / Quantum Non-Locality
**Status:** Specification extension for the PCTRM model

**AI Usage Disclosure:** Drafted by Anthropic Claude Opus 4.7 in collaboration with Geoff Howland during Session 9 continuation.

---

## I. Purpose and Scope

This document specifies entanglement channels as an extension to the PCTRM model. The extension addresses Q12 (entanglement across channel network) from PHYS-54's open questions and partially addresses Q13 (wavefunction collapse mechanism) by providing the substrate-level structure for how entangled solitons correlate their states without invoking new mechanisms beyond what PCTRM-1 already specifies.

The central commitment is minimalism: **entanglement channels are ordinary channels in every substrate-level sense**. They are not a new primitive. They are not a special case of channel arithmetic. They work exactly as any other channel in the PCTRM channel registry (Table A3 of PHYS-54). They accumulate remainder per tick. They apply vector contributions to their endpoints. They are created by specific interactions and persist until specific termination conditions are met.

What makes an entanglement channel distinct is not how it works at the substrate level, but when it exists and where its endpoints sit in Euclidean observation-space. An entanglement channel connects two (or more) solitons that, when observed through the Euclidean projection, appear to be separated by many Planck cells. At the graph level, they are ordinary graph-adjacent endpoints sharing an ordinary channel.

The substrate does nothing unusual. The observation-space appearance is unusual. This asymmetry is the content of the extension.

---

## II. The Minimal Commitment

PCTRM-1 specifies that solitons interact via channels. Channels have:
- A specific direction in each endpoint's frame
- A specific throughput (remainder exchanged per tick)
- An activation condition (always active or conditionally active)
- A direction of flow (drain, add, or bidirectional)

PCTRM-2 adds the entanglement channel type with the following specification:

**Activation condition:** Normally inactive. Activated by a specific class of interaction events (Section V.1). Remains active until terminated by specific events (Section V.3).

**All other properties:** Identical to general channel behavior in PCTRM-1. Vector remainder accumulates per tick. Modulus crossings produce discrete state updates. Channel-mediated remainder exchange follows the Phase 4 rule in the per-tick update mechanism (Table A5, PHYS-54).

The only difference between an entanglement channel and any other channel type is the activation condition and the fact that, when active, the channel's endpoints can be at arbitrary Euclidean separation. The graph distance is always 1 (single edge, single channel). The Euclidean distance is arbitrary.

This is the minimal extension that addresses the entanglement phenomenon. No new primitives. No new mechanisms. No new update rules at the per-tick level.

---

## III. The Graph vs. Euclidean Asymmetry

### III.1 What PCTRM-1 already established

The PCTRM-1 topology is direction-conditional nearest-neighbor full mesh. Each cell is adjacent to some other cell at 1 Planck distance in any continuous direction. Direction is continuous; position is discrete; adjacency is direction-keyed.

The implication, already present in PCTRM-1, is that the substrate's adjacency graph is not a simple Euclidean lattice. Which cell is your "next" depends on the direction you're pointing. The Euclidean distance to a cell is a derived property, not a structural property of the graph.

### III.2 What PCTRM-2 extends

The PCTRM-2 extension asserts that the substrate's adjacency graph can contain edges whose endpoints project to arbitrary separations in Euclidean space. These edges are ordinary channels at the substrate level. They appear non-local in observation because the Euclidean projection of the graph doesn't preserve all of the graph's adjacency structure.

A channel with endpoints at cells X and Y is 1-step in the graph. If X and Y are at positions such that |X − Y|_Euclidean = N Planck distances (for N >> 1), the channel carries remainder between them in a single tick — which is normal channel behavior. The substrate update rule doesn't know the difference between N = 1 and N = 10¹⁵.

This is not a new physics commitment. PCTRM-1's direction-conditional topology already broke any requirement that graph adjacency match Euclidean adjacency at the 1-Planck scale. PCTRM-2 just says that this decoupling can extend to arbitrary separations for specific channel types created by specific interactions.

### III.3 What this is not

This is not faster-than-light propagation of a signal. Information does not travel through Euclidean space faster than c. The substrate updates through its graph; the graph has this edge; the update happens in one tick because one tick is how long it takes to traverse one graph edge. Euclidean-space observers see correlations that would require FTL signaling if the substrate were Euclidean. The substrate is not Euclidean.

This is not a non-local hidden variable theory. The two endpoints are not secretly sharing a pre-determined state. They are sharing a channel in the substrate graph. The channel's state is the substrate-level description; the Euclidean endpoints' correlated measurements are the projection of that shared channel state into observation space.

This is not a commitment to a specific quantum mechanical interpretation. The framework is neutral between Copenhagen, many-worlds, Bohmian, and other interpretations. It specifies substrate-level structure that produces the observed correlations without committing to a philosophical interpretation of what measurement means.

---

## IV. The Channel Specification

### IV.1 Endpoints

An entanglement channel has 2 or more endpoints. Each endpoint is a specific soliton (not a specific cell). The channel is bound to the solitons, not to their current cell positions. As a soliton advances through Planck cells via normal update mechanics, the channel's endpoint identity moves with the soliton.

This specification has one consequence: the channel does not break when its endpoint solitons move. An entangled electron moving through space carries its entanglement channel with it. The channel is an edge in the soliton graph, not in the cell graph.

### IV.2 Throughput

The channel's throughput is the remainder exchanged per tick between its endpoints. For an active entanglement channel, the throughput follows the same rules as any other active channel: it is determined by the channel's strength parameter and by the endpoint states.

The throughput is bidirectional. A state update at one endpoint propagates to the other endpoint through the channel in the next tick. This is ordinary channel arithmetic.

### IV.3 Direction

The channel's direction in each endpoint's frame is determined by the channel's vector structure. This vector structure is what carries the correlation information. When the channel is read from endpoint A's direction basis, the vector projects onto A's measurement space. When read from endpoint B's direction basis, the same channel vector projects onto B's measurement space.

The correlation between A's and B's measurements is the projection of the channel's vector state onto the two bases. For spin measurements at angles θ_A and θ_B, the correlation follows cos(θ_A − θ_B) from the geometry of the channel's vector projection. This is the quantum mechanical prediction.

### IV.4 Activation state

An entanglement channel has two states: active and inactive. Inactive channels do not exist in the graph. Active channels are ordinary graph edges carrying ordinary remainder per tick. There is no third state. There is no partial activation. Activation is binary.

### IV.5 Constraint on information transfer

The channel's throughput carries correlation, not directional information. Local measurements on A produce no observable change in B's marginal statistics. This is the no-signaling theorem, which must hold as a substrate-level constraint on entanglement channels.

The constraint is: the channel's vector structure is symmetric between its endpoints. Measurement at A produces a correlated state at B, but the marginal distribution of outcomes at B is the same whether A measured or not. The channel transmits joint state updates, not directional signals.

This is a structural property of the channel. It does not require additional machinery; it is a consequence of the channel's symmetric vector structure.

---

## V. Lifecycle — Creation, Persistence, Termination

### V.1 Creation

An entanglement channel is created when two (or more) solitons undergo a specific class of interaction. The triggering interactions are:

**Direct quantum interactions:** Particle decay into correlated products (e.g., parapositronium → 2γ with correlated polarizations). Two particles passing through a beam-splitter or entangling gate. Two particles interacting via a shared coupling (electromagnetic, strong, weak) that produces an entangled final state.

**Prepared states:** Deliberately engineered entanglement in laboratory contexts. The experimental apparatus corresponds to a substrate-level interaction that creates the channel.

**Scattering with entanglement output:** Any scattering process whose final state is entangled (even if the incoming state was not) creates the channel at the moment the final state is produced.

The exact substrate-level trigger condition — what specific pattern of channel activations or remainder exchanges during an interaction produces an entanglement channel — is a subject for further specification. At this level, the commitment is: such interactions exist, and the creation event is deterministic given the substrate state.

### V.2 Persistence

Once created, an entanglement channel persists between its endpoint solitons indefinitely, as long as neither termination condition is met. The channel survives:

- Normal spatial translation of either endpoint
- Interaction of the endpoints with other (non-channel-breaking) channels
- Passage of arbitrary time

The channel is not a local cell property; it is a soliton property. As solitons move through cells, the channel moves with them. This is how entanglement can survive over macroscopic distances and long times in quantum experiments.

### V.3 Termination

An entanglement channel terminates under two conditions:

**Condition 1 — Measurement.** A measurement interaction on one endpoint soliton produces a definite state at that endpoint. The channel's state is now determined; the channel is resolved. The channel terminates at this event. The other endpoint's state updates through the channel in the next tick (or the same tick, depending on implementation) and the channel edge dissolves.

**Condition 2 — Decoherence.** Environmental coupling at one or both endpoints can disrupt the channel's coherence before a deliberate measurement occurs. Decoherence is a case where the channel's throughput becomes negligible relative to the environmental channels' combined throughput. The channel is present in the graph but its contribution to the endpoint state updates is dominated by other channels. This corresponds to effective entanglement loss in the standard QM description.

In the second case, the channel may still be technically active but is functionally inoperative. A full specification would either declare that such channels terminate automatically (when environmental throughput exceeds a threshold) or that they continue to exist but contribute nothing to the state updates. Both specifications are consistent with observed decoherence phenomena. The choice between them is a modeling decision for later work.

### V.4 Multi-endpoint channels

Channels with more than 2 endpoints (e.g., GHZ states, cluster states, W states) are modeled as a single channel connecting multiple soliton endpoints simultaneously. This is a hypergraph edge in the substrate graph — an edge with cardinality greater than 2.

Alternatively, multi-endpoint entanglement can be modeled as multiple pairwise channels with coordinated states. The choice depends on which structural convention produces cleaner substrate-level predictions for specific multi-particle states.

At this specification level, the commitment is: multi-particle entangled states correspond to either hypergraph edges or coordinated pairwise channels, and the substrate graph accommodates both structures. The specific choice for each experiment is a modeling decision.

---

## VI. What This Specification Does Not Address

The entanglement-as-channel extension is deliberately narrow. It addresses:

- Bell inequality violations (through correlated channel state at arbitrary Euclidean separation)
- Entanglement monogamy (through graph-edge combinatorics)
- No-signaling theorem (through channel symmetry)
- Persistence over distance and time (through soliton-bound endpoints)
- Decoherence (through environmental channel competition)
- GHZ and multi-particle entanglement (through hypergraph edges or coordinated channels)

It does not address:

- **Superposition:** A soliton in a superposition of states (before entanglement or measurement) is not addressed. The channel's vector structure requires the endpoints to be in specific states; how a single soliton can be in multiple states simultaneously is a separate question about the substrate's state representation. This requires complex-valued remainder or an equivalent mechanism beyond what PCTRM-1 specifies.

- **Quantum interference:** The same soliton's state propagating along different paths and interfering is not addressed. Interference requires the substrate to support phase accumulation in the remainder state along paths, which is a separate extension.

- **The measurement problem in full generality:** What constitutes a measurement that terminates the channel? This specification states that measurement events terminate the channel but does not specify the substrate-level criterion for a measurement. A full theory would need a decoherence threshold, an observer criterion, or a consistent-histories framework. This is deferred.

- **Born rule derivation:** Probabilities of specific measurement outcomes are produced by the channel's vector projection onto measurement bases. The exact formula that gives |⟨α|ψ⟩|² probabilities from channel geometry is not derived here. The commitment is: probabilities come from the channel's vector structure; the specific geometric formula that reproduces the Born rule is deferred.

These remain open questions. PCTRM-2 does not claim to resolve all of Q3. It resolves the non-locality piece specifically and leaves the superposition, interference, and measurement pieces for further extensions.

---

## VII. Falsification Conditions

The entanglement extension is falsifiable. The following would falsify it:

**F-E1:** Bell inequality violations at precision exceeding the quantum mechanical prediction. If experiments detect correlations tighter than Tsirelson's bound (which is the quantum limit), the channel model is wrong.

**F-E2:** Bell inequality violations at precision below the quantum mechanical prediction. If experiments detect correlations looser than quantum predicts (but still violating Bell), the channel's geometric projection is incomplete or inaccurate.

**F-E3:** Entanglement degradation with spatial separation beyond what decoherence explains. If entanglement quality falls as a function of distance itself (not just environmental coupling), the channel is not actually spatial-separation-independent. The substrate is either spatial at the channel level or has distance-dependent throughput.

**F-E4:** Multi-particle entanglement violations that don't match hypergraph/coordinated channel predictions. If GHZ-state correlations violate both the hypergraph model and the coordinated-pairwise model, the multi-endpoint channel specification is wrong.

**F-E5:** Faster-than-light signaling. If entanglement-based communication of classical information becomes possible, the no-signaling constraint fails and the channel carries more than correlation. This would falsify both the entanglement extension and the broader locality-preserving commitments of PCTRM.

**F-E6:** Monogamy violations. If a particle can be simultaneously maximally entangled with two others, the single-edge combinatorial structure is wrong and the channel model needs revision.

Each of these is testable in current experimental regimes. None has been observed. The entanglement extension predicts that none will be observed — consistent with standard quantum mechanics.

---

## VIII. Round 1 Test Candidate

A specific computational test that distinguishes this specification from alternatives:

**Bell correlation reproduction from channel geometry.**

Build a substrate simulation with two cells connected by a single entanglement channel. Assign the channel a vector state. Configure two measurement bases at angles θ_A and θ_B. Compute the correlation function:

E(θ_A, θ_B) = ⟨A · B⟩

from the projection of the channel vector onto the two bases. Compare to:

- The quantum mechanical prediction cos(θ_A − θ_B)
- The Tsirelson bound of 2√2 for the CHSH inequality
- Loophole-free Bell test measurements (Hensen et al. 2015, Giustina et al. 2015, Shalm et al. 2015)

If the channel-geometry picture reproduces cos(θ_A − θ_B) exactly and the Tsirelson bound is achieved, the model passes. If the correlation function differs from cos(θ_A − θ_B) — either in functional form or in amplitude — the channel's vector structure specification is inadequate.

This test is computationally tractable (two-cell simulation, vector arithmetic). It tests substrate mechanism rather than vocabulary consistency. It produces a pass/fail against experimentally measured Bell violations.

**Predicted outcome:** Pass. The channel's vector structure, when projected onto measurement bases, reproduces cos(θ_A − θ_B) by construction (it's what the channel vector is defined to do). The Tsirelson bound emerges from the geometric constraint that the channel vector's magnitude limits the maximum correlation.

If the predicted outcome holds, Round 1 adds substrate-mechanism validation to the vocabulary-consistency validation of Round 0.

---

## IX. Integration with Existing PCTRM Specification

### IX.1 Added to channel registry (Table A3 of PHYS-54)

The entanglement channel is added as a new channel type:

| Channel | Always Active? | Activation Condition | Direction | Throughput Formula | Drains/Adds | Scale of Application |
|---|---|---|---|---|---|---|
| Entanglement | Conditional | Created by specific interaction, terminated by measurement or decoherence | Channel's vector structure in each endpoint's frame | Correlation-carrying per tick | Bidirectional (symmetric) | All hierarchy levels where QM is operative |

All other channel types in Table A3 remain unchanged.

### IX.2 Added to soliton interface

The soliton interface (shared across hierarchy levels in PCTRM-1) now includes: "May share an entanglement channel with another soliton, in which case the two solitons' state updates are correlated through the channel."

This is a property of the soliton interface, not a level-specific implementation detail.

### IX.3 Added to Q12 resolution

Q12 (entanglement across channel network) is advanced from "unspecified" to "specified as ordinary channels with binary activation state and soliton-bound endpoints." The question is not fully resolved — decoherence threshold and multi-endpoint structure remain modeling choices — but the structural mechanism is concrete.

### IX.4 Added to Q13 partial resolution

Q13 (wavefunction collapse mechanism) is advanced by specifying that measurement events terminate entanglement channels. This is half of the collapse mechanism: for entangled states, measurement resolves the channel. The other half — what substrate-level criterion defines a measurement event — remains open.

---

## X. Testable Predictions Summary

The entanglement extension makes these predictions:

1. **Bell correlations exactly follow cos(θ_A − θ_B)** — the quantum mechanical form, emerging from the channel's vector projection onto measurement bases.

2. **Tsirelson bound is achievable** — maximum correlation at the quantum limit, from the channel vector's magnitude constraint.

3. **Bell inequality violations are maximal** — no deviation from quantum prediction within the substrate's precision.

4. **Monogamy is maintained** — no particle is simultaneously maximally entangled with two others, as a consequence of single-edge connection.

5. **No-signaling holds** — local measurements don't transmit classical information, as a consequence of channel symmetry.

6. **Entanglement persists under motion** — the channel follows the soliton, so entangled particles remain entangled when separated in space.

7. **Decoherence rates scale with environmental channel count** — not with spatial separation itself.

8. **GHZ correlations follow the quantum prediction** — the three-particle Mermin inequality is violated at the quantum maximum.

9. **Entanglement does not degrade with distance** — outside of decoherence effects, entanglement quality is distance-independent.

Each of these is a standard quantum mechanical prediction. The extension predicts standard quantum mechanics will be observed. If any of these predictions fails, the entanglement extension fails (as specified in Section VII).

---

## XI. Status and Next Steps

### XI.1 Current status

PCTRM-2 is specified. The entanglement channel is defined. Creation, persistence, and termination rules are stated. The integration with PCTRM-1 is clean. The falsification conditions are pre-registered. The Round 1 test is specified.

The specification is minimal by design. No new primitives. No new mechanisms at the per-tick update level. The entanglement channel is an ordinary channel with specific activation and termination conditions. Its distinctiveness is not in the substrate's arithmetic — it is in the decoupling of graph structure from Euclidean projection.

### XI.2 Remaining work

Three specific pieces of further work are required to make the extension computationally complete:

**1. The substrate-level trigger for channel creation.** What specific pattern of channel activations during an interaction produces an entanglement channel? This requires a mapping from interaction event types to channel creation events.

**2. The decoherence threshold.** What environmental throughput is sufficient to effectively terminate the channel? This requires a quantitative specification.

**3. The multi-endpoint channel structure.** Hypergraph edges or coordinated pairwise channels? The choice affects how multi-particle entangled states are represented.

These are specification refinements, not foundational issues. The framework as stated is sufficient for the Round 1 Bell correlation test.

### XI.3 Planned follow-up

- **Round 1 computational test:** Reproduce Bell correlation from channel geometry. First mechanism-level validation of PCTRM substrate picture. Tractable with modest compute.

- **PCTRM-3 (if needed):** Interference and superposition extension. If the entanglement channel carries phase as well as magnitude, this might be addressable through the same mechanism. This would close the Q3 extension more broadly.

- **PCTRM Round N:** As theoretical progress on Q1, Q2, Q4, Q5 proceeds, additional rounds test substrate mechanism at higher levels of the PHYS-54 hierarchy.

---

## XII. Conclusion

PCTRM-2 specifies entanglement as an ordinary channel in the substrate graph with two distinguishing properties: binary activation (normally inactive, activated by specific interactions) and endpoint-soliton binding (the channel moves with its endpoint solitons through space). At the substrate's per-tick update level, the entanglement channel behaves identically to any other active channel. Only in the Euclidean projection does the channel appear unusual — connecting solitons at arbitrary spatial separation.

This minimal extension resolves Bell non-locality without introducing new primitives or new update mechanisms. It preserves substrate locality by operating at the graph level rather than the Euclidean level. It produces standard quantum mechanical predictions through the geometric projection of the channel's vector state onto measurement bases.

The extension is falsifiable. Six specific falsification conditions are pre-registered. A computational test (Bell correlation reproduction) is specified for Round 1. If the test passes, PCTRM gains its first substrate-mechanism validation. If it fails, the specific failure mode identifies where the channel-geometry picture breaks.

This is the next step in the PCTRM program. The framework's claim — that RUM's vocabulary is operationally real at the Planck scale — is advanced by extending the channel concept to cover non-local correlations without abandoning local-update arithmetic. The extension is structural. It is minimal. It is testable.

---

**END PCTRM-2-2026**

**Status:** Specification extension. Ready for Round 1 computational test.

**Central commitment:** Entanglement is an ordinary channel in the substrate graph. It is active only under specific interaction-triggered conditions. Its endpoints are solitons (which move through cells), not cells (which stay fixed). At the substrate level, it works exactly like any other channel. At the Euclidean projection level, it appears non-local. The asymmetry between graph and Euclidean adjacency — already present in PCTRM-1 at the 1-Planck scale — is extended to arbitrary spatial separations for this channel type.

**Falsification:** Six specific pre-registered conditions. Each is testable in current experimental regimes.

**Priority:** Add to PCTRM-1 as Section IX extension. Pursue Round 1 Bell correlation test as first substrate-mechanism validation for the PCTRM program.

---

# PCTRM-2 Errata and Annotations

**Registry:** HOWL-PCTRM-2-2026 (Errata and Annotations)
**Parent:** HOWL-PCTRM-2-2026 (main specification)
**Date:** April 20, 2026
**Purpose:** Corrections, gaps, and tightenings identified during review. To be appended or incorporated.

---

## I. Errata — Specific Corrections Required

### E1: Section IV.3 — Bell correlation form is stated imprecisely

The specification says: "the correlation follows cos(θ_A − θ_B) from the geometry of the channel's vector projection."

For the singlet state (the Bell state most commonly tested), the correlation is **E(θ_A, θ_B) = −cos(θ_A − θ_B)**, with a minus sign. The minus sign is not cosmetic — it distinguishes singlet-state correlation from triplet-state correlation. The CHSH inequality S = E(θ_A, θ_B) − E(θ_A, θ'_B) + E(θ'_A, θ_B) + E(θ'_A, θ'_B), evaluated on the singlet state, yields the maximum violation S_max = 2√2 only with the negative correlation.

The specification should distinguish which Bell state the channel represents. Either:

- The channel's vector state encodes the specific Bell state (singlet, |Φ⁺⟩, |Φ⁻⟩, |Ψ⁺⟩, |Ψ⁻⟩), and the correlation function depends on which state.
- Or the general form is given: E = ±cos(θ_A − θ_B), with sign determined by the channel's parity specification.

Section X's Prediction 1 has the same imprecision and should be corrected with the sign specification.

### E2: Section V.3 Condition 1 — Timing of the other endpoint's update

The specification says: "The other endpoint's state updates through the channel in the next tick (or the same tick, depending on implementation)."

This parenthetical is a specification hole, not a modeling choice. The two options have different observational consequences:

- If B updates in the same tick as A's measurement, the update is effectively instantaneous and there's no propagation time at all through the graph. This is inconsistent with the framework's commitment that channels carry updates through graph edges at one tick per edge.
- If B updates in the next tick, there's a one-tick delay between measurement events at A and B. At Planck time (~5 × 10⁻⁴⁴ seconds), this delay is unobservable. But the framework commitment is specific: one tick per graph edge traversal.

Correction: the channel carries the correlated update in exactly one tick, consistent with PCTRM-1's per-tick update rule. Measurement at A occurs at tick t; the channel's state resolves at tick t; B's endpoint state updates at tick t+1. The channel dissolves between t and t+1.

### E3: Section V.4 — The hypergraph vs. pairwise choice is not a "modeling decision"

The specification says: "The specific choice for each experiment is a modeling decision."

It is not. The two structures make observably different predictions for some three-particle correlations. GHZ state correlations, when computed via coordinated pairwise channels, differ from the same correlations computed via a single hypergraph edge of cardinality 3. The discrepancy is measurable in principle.

The specification should commit to one structure. The natural choice — given PCTRM's existing channel-is-bilateral convention from PCTRM-1 — is **coordinated pairwise channels**, with an additional "coordination mechanism" specifying how multiple pairwise channels in the same entanglement event synchronize their states.

If the coordinated-pairwise picture fails a three-particle Bell test, then the fallback is the hypergraph. But the specification should pick one and commit. "Either works" is not a substrate commitment.

### E4: Section VI — Superposition is not cleanly outside scope

The specification says: "A soliton in a superposition of states (before entanglement or measurement) is not addressed."

But Section IV.3 says the channel's vector state projects onto measurement bases with a cos(θ_A − θ_B) dependence. This projection requires the channel's vector state to be in some rotation-invariant form — effectively a superposition in the channel's own state space. The specification cannot simultaneously claim:

- The channel has a vector state that produces cos(θ_A − θ_B) correlations
- Superposition is outside the scope of this specification

A channel vector state that produces angle-dependent projections is itself a superposition structure. The specification needs to acknowledge this: the channel carries a superposition (in its own state space), but the individual solitons before measurement are not required to be in superposition.

Correction: Section VI should clarify that the specification addresses channel-level superposition (implicit in the vector-state projection) but does not address soliton-level superposition (the interference of different paths for a single soliton). The former is what enables Bell correlations; the latter is what enables single-particle interference.

### E5: Section VIII — The Round 1 test as stated is tautological

The specification says: "The channel's vector structure, when projected onto measurement bases, reproduces cos(θ_A − θ_B) by construction (it's what the channel vector is defined to do)."

If the channel vector is defined to produce cos(θ_A − θ_B), then the Round 1 test cannot falsify that. It's not a test of the substrate picture — it's a consistency check of the specification's internal definitions.

The real test is: does the channel's vector structure, under the substrate's existing arithmetic rules (remainder accumulation, modulus crossing, channel throughput), produce cos(θ_A − θ_B) when specific substrate computations are run? Or does the substrate's arithmetic deviate from the idealized vector projection?

Correction: the Round 1 test should not assume the channel vector produces cos(θ_A − θ_B) by construction. It should compute correlations from the substrate's per-tick update rules applied to a two-cell simulation with an entanglement channel, and compare to the cos(θ_A − θ_B) target. The comparison is substantive: if the substrate arithmetic produces the target exactly, the picture passes; if it produces a close approximation with small deviations, those deviations are substrate-level predictions that differ from QM; if it produces something unrelated, the picture fails.

The kill switch specification in Section VII (F-E1, F-E2) is correct, but Section VIII's prose undercuts it by framing the test as tautological.

### E6: Section IX.1 — Channel scale is wrong

The specification lists the entanglement channel's "Scale of Application" as "All hierarchy levels where QM is operative." This is imprecise.

QM is operative in principle at all scales. In practice, it manifests at Levels 0–3 (subatomic, nuclear, atomic, molecular) and occasionally at Level 4 (engineered mesoscopic systems). At Level 5 (macroscopic) and higher, decoherence dominates and entanglement channels exist but are immediately decohered.

The correction: the entanglement channel is **available at all hierarchy levels**, but its **effective operation is typically limited to Levels 0–4**, with Level 5+ decoherence dominating the channel's observable effects. This matters for the specification's claim that entanglement channels "operate at all hierarchy levels where QM is operative" — they technically operate at all levels, but their observable effects are scale-dependent due to decoherence competition.

---

## II. Gaps — Items Explicitly Not Addressed

### G1: The channel's vector state structure

The specification repeatedly refers to "the channel's vector structure" that produces correlations under projection. This structure is not specified. What are its components? What does it look like in each endpoint's frame? What transformation rules apply when an endpoint rotates its measurement basis?

Minimum specification needed:

- The channel's state is a vector in some state space of specified dimension (likely complex-2-dimensional for a qubit pair, complex-4-dimensional for two qubits, etc.)
- The projection of this vector onto a measurement basis produces a probability distribution over outcomes
- The symmetry constraint ensures the marginal distribution at each endpoint is maximally mixed (no-signaling)

Without this, the Round 1 test cannot be computed. The substrate simulation needs a concrete specification of what state the channel carries. This gap is severe enough that it effectively blocks Round 1 implementation until resolved.

### G2: The decoherence threshold

Section V.3 Condition 2 mentions decoherence but does not specify the threshold. The specification says: "A full specification would either declare that such channels terminate automatically (when environmental throughput exceeds a threshold) or that they continue to exist but contribute nothing to the state updates. Both specifications are consistent with observed decoherence phenomena."

These two options are not observationally equivalent at all times. If the channel continues to exist but contributes nothing, a subsequent environmental change could restore its contribution (re-coherence) — this does not happen in observed QM. If the channel terminates automatically, re-coherence is impossible — this matches observation.

Correction: the specification should commit to **automatic termination above a decoherence threshold**. The threshold itself can be a modeling parameter, but the termination-vs-latent choice should be settled at the specification level.

### G3: The measurement operator

Section V.3 Condition 1 says "a measurement interaction on one endpoint soliton produces a definite state at that endpoint." What constitutes a measurement interaction?

The specification defers this to later work. But measurement is the thing that breaks entanglement, and without a specification of what constitutes measurement, the channel's termination condition is effectively undefined.

Minimum specification needed:

- A measurement interaction is one where the soliton couples to a macroscopic degree of freedom (many-soliton system, observer, measuring apparatus)
- Alternatively: a measurement interaction is one whose interaction with a subsystem produces irreversible change (thermodynamic criterion)
- Alternatively: a measurement is a projection onto one of the measurement basis states (observer-defined criterion)

The specification should commit to one of these. Different choices produce different substrate-level predictions for borderline cases (e.g., weak measurements, quantum eraser experiments). Leaving the choice open effectively leaves the whole measurement problem open.

### G4: Entanglement creation probability

Section V.1 says entanglement channels are created by specific interactions. But quantum mechanics is probabilistic — a given interaction may or may not produce an entangled final state. Parametric down-conversion in a nonlinear crystal produces entangled photon pairs with probability ~10⁻⁶. The specification doesn't address this.

Correction: the specification needs a probabilistic channel-creation mechanism. For an interaction with multiple possible outcomes, the probability of each outcome (including the entangled-output probability) should be computable from the substrate's pre-interaction state. The Born rule likely applies to channel-creation outcomes as it does to measurement outcomes.

### G5: Channel state evolution

Once a channel is created, does its vector state evolve over time? Standard QM says yes — a Bell state prepared at time t₀ can undergo unitary evolution before measurement. The specification doesn't address channel state evolution between creation and measurement/decoherence.

If the channel vector state is static from creation to termination, the specification cannot reproduce experiments where the entangled state rotates in its joint Hilbert space between preparation and measurement. If the channel evolves, the specification needs an evolution rule.

Correction: the channel's vector state evolves according to some rule per tick. The simplest commitment: the channel state evolves the same way other channels' states evolve (the substrate's per-tick update applied to the channel's internal structure). The full specification requires either (a) a static state that is what it is at creation, or (b) an evolution equation. This needs to be settled.

---

## III. Annotations — Items That Benefit from Clarification

### A1: The "ordinary channel" framing is right, and undersold

The specification's central argument is that entanglement channels are not special. This is correct and it is the strongest feature of the specification. The framework's existing channel concept is sufficient to carry non-local correlations; only the topological placement of the endpoints is different.

The specification should emphasize this more. The minimal-extension principle is not just an aesthetic choice — it's the main reason this specification has any chance of being right. If entanglement required a new primitive, the framework would be carrying an additional load of theoretical machinery. By not requiring that, the specification makes the framework more economical. This is a feature to advertise, not a footnote.

### A2: The graph-vs-Euclidean asymmetry deserves a schematic

The specification is prose-heavy where a diagram would clarify. A visualization showing:

- Left: the substrate graph, with two cells connected by a channel edge (an ordinary graph edge, 1 step)
- Right: the Euclidean projection, where the same two cells appear separated by many Planck distances, with the channel still present but looking "non-local"

This is the central conceptual claim. A schematic would make it immediately clear. Recommend adding a figure to Section III.

### A3: The relationship to the isomorphism claim in PHYS-54

PHYS-54 committed to parallel isomorphism: PCTRM and SM produce identical observables from different primitives. The entanglement channel extension needs to respect this. Specifically:

- Bell correlation measurements at the macroscopic scale must match SM's prediction cos(θ_A − θ_B) (or −cos for singlet) exactly
- The Tsirelson bound 2√2 must be reproducible
- No-signaling must hold
- Monogamy must hold

The specification addresses all of these, but does not explicitly frame them as consequences of the isomorphism commitment. The addendum should note: the entanglement extension's predictions are identical to SM's predictions where both make them, by the isomorphism commitment. Any deviation would falsify PCTRM's substrate claim, not just the entanglement extension.

### A4: The connection to Q3 decomposition is worth keeping prominent

The specification correctly identifies that Q3 decomposes into four sub-problems: non-locality, superposition, interference, measurement. The entanglement extension addresses one (non-locality) fully, one (measurement) partially, and leaves two (superposition, interference) open.

This is the right framing and the specification should keep it prominent. Future extensions (PCTRM-3, PCTRM-4) can address the remaining pieces. The decomposition makes the overall Q3 problem tractable — each sub-problem gets its own extension with its own pre-registered tests.

### A5: The priority ordering in PHYS-54 should be updated

PHYS-54 listed Q3 as "High priority" and Q12 as "Medium priority." With PCTRM-2, these shift:

- Q12 (entanglement) moves from "Medium" / "unspecified" to "High" / "specified, pending Round 1 test"
- Q3 (QM extension) decomposes, with the non-locality piece now "High" / "specified" and the remaining pieces still "High" / "unspecified"

The PHYS-54 open-questions table (Table A14) should be updated to reflect this.

### A6: The falsification table needs integration

PHYS-54's kill switch table (Table A13) has 16 entries (K1-K16). PCTRM-2 adds F-E1 through F-E6 as additional falsification conditions. These should be integrated:

- Add K17-K22 for F-E1 through F-E6
- Add them to the six-level program at Level 1 or Level 2 (atomic/subatomic) since that's where Bell correlation experiments operate
- Update the priority order to include the new kill switches

---

## IV. Methodological Observations

### M1: The specification is appropriately scoped

The specification addresses one well-defined problem: Bell non-locality. It does not try to solve the entire measurement problem or the superposition problem. This focused scope is correct for an extension paper. The framework's pattern of "one specification at a time, each minimal, each falsifiable" is preserved here.

### M2: The pre-registered falsification conditions are sharp

Section VII lists six specific falsification conditions with precision specifications. This is the pattern the framework has used for prior RUM papers and it's being maintained here. If the test fails, the specification is retracted, not patched. If it passes, the specification becomes part of the substrate model.

This is appropriate falsification discipline. No backpedaling allowed.

### M3: The absence of "working out superposition" is not a weakness

Reviewers might criticize the specification for only addressing non-locality and not superposition. This is not a weakness — it's the right scope. Trying to solve multiple QM subproblems simultaneously has been the failure mode of previous theoretical frameworks. Addressing them one at a time, each with its own minimal extension and its own falsifiable test, is the correct strategy.

The specification should explicitly state this methodological choice.

### M4: The "ordinary channel" minimal commitment may be too ordinary

Potential concern: if the entanglement channel is truly ordinary — identical to gravitational/EM/strong channels at the substrate level — why doesn't every ordinary channel exhibit this non-local behavior?

The answer is in Section V.1: entanglement channels are created by specific interaction events, and they persist between specific solitons regardless of their subsequent motion. Other channels (gravity, EM, etc.) are continuously created and destroyed as solitons move in and out of each other's influence ranges. The difference is not in the channel's substrate behavior — it's in the channel's creation and termination conditions.

This clarification should be added to Section II or Section IV to preempt the concern.

---

## V. Additional Table Suggestions

### New Table: The Six Round 1 Entanglement Kill Switches

| # | Condition | Precision | Experimental reference | Implication of failure |
|---|---|---|---|---|
| F-E1 | Bell correlation deviation from ±cos(θ_A − θ_B) | 10⁻³ | Hensen 2015, Giustina 2015, Shalm 2015 | Channel vector projection rule is wrong |
| F-E2 | CHSH bound ≠ 2√2 | 10⁻³ | Same as F-E1 | Channel vector magnitude constraint is wrong |
| F-E3 | Entanglement degrades with distance (beyond decoherence) | 10⁻² | Satellite Bell tests (Micius) | Channel is not distance-independent |
| F-E4 | GHZ three-particle correlations violate model | 10⁻² | Mermin inequality tests | Multi-endpoint structure is wrong |
| F-E5 | Faster-than-light signaling detected | Any | All experimental bounds | No-signaling is violated; substrate not local-on-graph |
| F-E6 | Entanglement monogamy violation | 10⁻² | Quantum information experiments | Single-edge combinatorics is wrong |

### New Table: Sub-Problems of Q3 and Their Resolution Status

| Sub-problem | Resolution status | Specification location |
|---|---|---|
| Non-locality (Bell) | Specified | PCTRM-2-2026 |
| Superposition | Open | Pending PCTRM-3 |
| Interference | Open | Pending PCTRM-3 or PCTRM-4 |
| Measurement (collapse) | Partially specified | PCTRM-2 Section V.3 (entanglement channels only) |
| Born rule derivation | Open | Requires complex-remainder extension |

---

## VI. The Strong Case for Proceeding

The entanglement extension is a meaningful advance. It takes one of the framework's biggest open questions (Bell non-locality in a local-update substrate) and resolves it with a minimal, testable extension. The resolution is consistent with PCTRM-1's direction-conditional topology — it's the same structural move applied at a different scale.

The specification has gaps (G1-G5), but they are specification-refinement gaps, not foundational gaps. The central idea is sound. The falsification conditions are sharp. The Round 1 test is tractable in principle (once G1 is resolved).

Specifically:

- Section VII's six falsification conditions are pre-registered at measurement precision levels. If any fires, the specification is retracted.
- Section VIII's Round 1 test is computationally tractable once the channel vector state structure (G1) is specified.
- Sections V.1 through V.4 establish lifecycle rules that are concrete enough to implement.

What remains is to:

1. Fix the errata E1–E6
2. Close gaps G1–G5 with specific structural choices
3. Add the entanglement extension to PHYS-54 as Section XVIII or as a new addendum
4. Design and execute the Round 1 Bell correlation test

If the test passes, PCTRM gains its first mechanism-level validation. If it fails, the framework learns which specific piece (channel structure, projection rule, multi-endpoint handling) is wrong and the specification is revised or retracted.

The specification is not ready to run as-is — G1 (channel vector state structure) blocks Round 1 implementation. But the specification is close enough that closing G1 alone gets the test off the ground.

---

## VII. Specific Actions Required Before Round 1

1. **Fix E1 (correlation sign):** specify singlet vs. triplet Bell states and the ± sign in the correlation form.
2. **Fix E2 (measurement timing):** commit to one-tick delay between A's measurement and B's update.
3. **Fix E3 (multi-endpoint):** commit to coordinated pairwise channels (or hypergraph); pick one.
4. **Fix E4 (superposition scope):** acknowledge channel-level superposition; distinguish from soliton-level.
5. **Fix E5 (test tautology):** reframe Round 1 test so it's a substrate arithmetic computation, not a definition-check.
6. **Close G1 (channel vector state structure):** specify the state space dimension and the projection rule.
7. **Close G2 (decoherence threshold):** commit to automatic termination; specify threshold form.
8. **Close G3 (measurement operator):** commit to a measurement criterion.
9. **Close G4 (creation probability):** specify how the Born rule applies to channel-creation events.
10. **Close G5 (state evolution):** specify whether and how the channel's state evolves between creation and termination.

Items 1–5 are corrections to the existing specification.
Items 6–10 are gaps that need resolution.

All ten are addressable with focused specification work. None requires new theory beyond what PCTRM-1 already provides. The specification is close; it needs ten targeted refinements.

---

## VIII. Verdict

The specification is on the right track. The minimal-extension approach is correct. The falsification conditions are sharp. The Round 1 test is clearly specified (at the level of what's being tested, even if the specific computation needs G1 resolved first).

The specification has errors that need correcting (E1–E6) and gaps that need closing (G1–G5). None of these are foundational. All ten are addressable within a focused revision cycle.

Recommend:

1. Issue PCTRM-2-2026-v1 with errata E1–E6 corrected
2. Issue PCTRM-2-2026-v2 with gaps G1–G5 closed
3. Integrate the six falsification conditions F-E1 through F-E6 into PHYS-54's kill switch table
4. Update PHYS-54 Table A14 (open questions) with the new Q3 decomposition
5. Design and execute Round 1 Bell correlation test against PCTRM-2-v2

The specification is ready for revision, not for implementation. After v2, it's ready for Round 1.

---

**END PCTRM-2 ERRATA AND ANNOTATIONS**

**Status:** Review complete. Ten specific actions required before Round 1 implementation. Specification sound at its core; revision-ready.

