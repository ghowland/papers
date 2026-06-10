# The Geometry of Dissolution and Fragility
## Predicting Catastrophic Failure from Structural Analysis

**Registry:** [@HOWL-MATH-16-2026]

**Series Path:** [@HOWL-INFO-11-2026] → [@HOWL-INFO-12-2026] → [@HOWL-INFO-13-2026] → [@HOWL-MATH-14-2026] → [@HOWL-MATH-15-2026] → [@HOWL-MATH-16-2026]

**Date:** June 2026

**DOI:** 10.5281/zenodo.20629792

**Domain:** Information Processing Theory / Applied Mathematics

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

### 1. The Phenomenon

A pilot with ten thousand hours flies competently without conscious attention to hundreds of sub-tasks. Airspeed, altitude, heading, engine instruments, radio calls, traffic scanning — each one was once a demanding task requiring full concentration. Through years of repetition in consistent conditions, each collapsed into structure that produces correct results automatically. The pilot's conscious processing pipeline is almost entirely free, available for weather assessment, route planning, communication with passengers, or handling the unexpected.

A bee enters the cockpit.

The pilot swats at it, loses visual reference for two seconds, and suddenly must consciously re-acquire altitude, heading, and attitude simultaneously. Three tasks that cost zero conscious effort moments ago now each demand full processing. The pilot's pipeline handles one task at a time. Three are competing. Performance degrades — not because the pilot forgot anything, but because the context shifted outside the conditions under which those skills became automatic.

This paper concerns the geometry of that fragility.

The vocabulary is small and builds in order. Processing is what any system does when it must act on information. A CPU executing instructions, a surgeon operating, a pilot flying, a manager deciding — each is a processor acting on elements. The irreducible unit of processing is the **op**: one transformation by one processor. A diagnostic question is one op. A mirror glance is one op. A cache lookup is one op. Ops are countable, observable, and universal across domains the way bits are universal across communication channels.

When a processor performs the same operation repeatedly under consistent conditions, the op count required decreases toward zero over time. The mirror check that cost a new driver six ops — locate mirror, focus, scan image, identify objects, assess threat, return gaze — eventually costs zero. The processing chain collapses into structure that produces the correct result without consuming the processor's scarce sequential pipeline. This is **dissolution**. A dissolved task costs zero ops.

The processor's total capacity is bounded by one inequality: total ops multiplied by average op duration must not exceed the available time budget. The time budget is fixed by domain physics — lane tolerance before the guardrail, anesthesia window before risk, request timeout before the client disconnects. Dissolved tasks don't count against the budget. This is what makes expertise powerful: the expert's budget is mostly free because most routine processing has dissolved.

But dissolution has conditions. It occurred under specific circumstances — specific visibility, specific aircraft behavior, specific cockpit configuration. When circumstances change beyond what the dissolution can accommodate, the task promotes back from dissolved to active. It costs ops again. When many tasks promote simultaneously, total ops spike past the time budget and the processor fails.

This is a **cascade**. The number of simultaneous promotions is the severity. The bee is tiny. The cascade is large. The event's magnitude and the cascade's severity are unrelated quantities — severity depends on how many dissolved tasks break, not on what broke them.

The question this paper answers: given knowledge of what a processor has dissolved and under what conditions, can we predict where cascades will be severe before they occur? The answer is yes, and the tool is geometry.

---

### 2. The Dissolution Curve

Every dissolved element was once expensive. Before dissolution, the element cost some number of ops — the first-encounter cost. Through repetition, the cost decreased. After sufficient repetitions under sufficiently consistent conditions, the cost reached zero. Plotting op count against repetitions produces the **dissolution curve** for that element.

The curve has structural constraints that hold regardless of domain. It begins at first-encounter cost, which is the maximum ops the element will ever require from this processor. It decreases monotonically under consistent context — each repetition in stable conditions either reduces the op count or leaves it unchanged. It is bounded below by the **optimal reduction floor**: the minimum ops any competent processor requires for reliable execution of that element. Below the floor, the processor is operating without sufficient verification — not dissolved but blind. The curve approaches zero asymptotically given sufficient repetitions, though the rate of approach varies.

The floor deserves emphasis because it defines two distinct gaps. The gap between current op count and the floor is measurable inefficiency — the processor is spending more ops than necessary and could improve through further practice. The gap between the floor and zero is what dissolution absorbs — the conversion of minimum-competent processing into structural processing that costs nothing.

Three candidate families fit these constraints.

**Exponential decay** predicts that each repetition reduces remaining ops (above the floor) by a fixed fraction. If the first-encounter cost is 20 ops, the floor is 2 ops, and the decay rate is 0.1 per repetition, then after 10 repetitions the cost is approximately 2 + 18(0.9¹⁰) ≈ 8.3 ops. After 20 repetitions, approximately 3.2 ops. After 40, approximately 2.1. The half-life is constant — each additional block of repetitions buys the same proportional improvement. This family implies that training investment has consistent returns regardless of current skill level.

**Power law** predicts that cost decreases as a negative power of repetitions: ops = a × n^(−b) + floor. Early repetitions produce large reductions. Later repetitions produce progressively smaller ones. This family matches the common experience that initial skill acquisition is rapid and later refinement is slow, and it predicts that the final approach to the floor (and from floor to zero) takes disproportionately long.

**Logarithmic decay** predicts cost decreasing as the inverse log of repetitions. Extremely rapid initial dissolution, then a very long tail. This family predicts that a few repetitions capture most of the benefit and that pushing to full dissolution requires orders of magnitude more practice than reaching basic competence.

The distinction between these families is not academic. It determines training investment strategy. Exponential decay says each hour of practice is equally valuable in percentage terms regardless of current skill level. Power law says early hours are disproportionately valuable and late-stage refinement has poor returns. Logarithmic says initial exposure is nearly sufficient and extended practice yields diminishing marginal dissolution.

Available empirical evidence across domains offers guidance. Motor skill acquisition research consistently shows power-law learning curves. Medical diagnostic accuracy over case volume follows a similar pattern — rapid initial improvement followed by slow refinement. Cache hit rates after working set stabilization approximate exponential approach. Programming expertise on a familiar codebase shows power-law characteristics with occasional step changes when new structural insight reorganizes multiple elements simultaneously.

This paper does not resolve the universality question — whether one family holds across all domains with domain-specific parameters, or whether fundamentally different domains produce fundamentally different curve shapes. The structural constraints narrow the candidate space. The empirical evidence favors power law as the default but does not rule out domain-specific deviation. What matters for the remainder of this paper is that the curve exists, has the stated constraints, and is parameterizable. The specific shape affects quantitative predictions about training efficiency but not the geometric framework that follows.

Three parameters characterize any dissolution curve within a given family. **Element complexity** (C₀): the first-encounter op count, determined by the element's intrinsic structure and the processor's initial state. **Context consistency** (κ): a measure of how stable conditions remain across repetitions, bounded between zero (every repetition in different conditions) and one (every repetition in identical conditions). **Processor dissolution rate** (λ): how quickly this processor converts repetitions into op reduction, which may itself depend on prior dissolutions in related domains — a phenomenon sometimes called transfer, where dissolving one element accelerates dissolution of structurally similar elements.

The dissolution curve D(n) for element x, processor p, in context consistency κ is then:

D(n | x, p, κ) = C₀ × f(n, λ, κ) + R*

where f is the family-specific decay function (exponential, power, or logarithmic), n is repetition count, λ is processor dissolution rate, and R* is the optimal reduction floor. Full dissolution occurs when D(n) = 0, meaning f has driven the curve below R* and the floor-to-zero gap has been absorbed into structure.

---

### 3. The Validity Envelope

Every dissolved element has conditions. The pilot's altitude maintenance dissolved under visual flight in calm air in a familiar aircraft. The surgeon's knot tying dissolved under normal tissue tension with standard suture material. The cache entry dissolved under a specific memory access pattern with a specific working set. These conditions define a region in a space of context variables. Inside the region, dissolution holds — the element costs zero ops. Outside the region, it promotes back to active processing.

This region is the **validity envelope** of the dissolved element. It is the central formal object of this paper.

Define **context space**. A context is a collection of conditions under which processing occurs. Each condition is a measurable dimension. For the pilot: visibility (continuous, meters), turbulence intensity (continuous, meters per second), aircraft attitude deviation from nominal (continuous, degrees), cockpit environment anomaly (discrete, normal/abnormal), physiological state (multidimensional — fatigue, stress, workload). For the surgeon: anatomical conformity to expected (continuous, deviation score), bleeding rate (continuous, milliliters per minute), instrument availability (discrete, available/unavailable), team communication quality (continuous, errors per exchange). For the CPU: memory access locality (continuous, working set spread), competing process interference (continuous, cache pressure), input data characteristics (multidimensional, pattern statistics).

Context space is the product of all context dimensions relevant to a given processor and operational domain. A point in context space specifies exact conditions. The processor's current operating conditions map to a single point.

The validity envelope for dissolved element e is the subset of context space:

V(e) = { c ∈ context space : dissolution of e produces correct result at c }

Inside V(e), the element costs zero ops. Outside V(e), the element promotes to active processing at some cost determined by how far outside the envelope the current context lies and how much of the dissolution chain must be reconstructed.

Envelope width along each context dimension is determined by dissolution history. If the pilot dissolved altitude maintenance only in calm air (turbulence between 0 and 1 m/s), the validity envelope extends from 0 to approximately 1 m/s along the turbulence dimension, possibly with some margin from generalization. If the pilot dissolved the same skill across turbulence ranging from 0 to 5 m/s, the envelope extends further. In either case, the envelope does not extend to turbulence levels never encountered during dissolution — you cannot dissolve beyond what you have practiced.

Define **envelope width** w(e, d) for element e along context dimension d:

w(e, d) = measure of V(e) projected onto dimension d

This is the range of conditions along dimension d within which dissolution holds. Total envelope volume is the measure of V(e) in full context space, which for independent dimensions approximates the product of widths:

vol(V(e)) ≈ ∏_d w(e, d)

For dependent dimensions (where context conditions are correlated — high turbulence often accompanies low visibility), the envelope shape in the joint space may be more complex than a hyperrectangle, but the volume remains well-defined as a measure.

The **envelope shape** captures an important asymmetry: a dissolved element may have wide tolerance along one context dimension and narrow tolerance along another. The pilot's altitude maintenance may tolerate wide variation in airspeed but have almost zero tolerance for loss of visual reference. The envelope is elongated along the airspeed dimension and flat along the visual reference dimension. Shape determines which context changes are dangerous — changes along narrow dimensions reach the envelope boundary quickly.

Two factors determine envelope width along a given dimension: **training breadth** (the range of conditions experienced during dissolution) and **generalization margin** (the additional width beyond training range that the dissolution accommodates, which varies by element type and processor). Training breadth sets a lower bound on envelope width. Generalization provides additional width that depends on whether the skill has structural properties that transfer across conditions or is purely condition-specific.

---

### 4. The Cascade Severity Function

At any moment, a processor has a **dissolution inventory**: the set of elements currently at zero ops, each with its validity envelope in context space. The processor also occupies a specific point in context space — the current operating conditions.

Every dissolved element whose envelope contains the current context point remains dissolved. A context change moves the point. Any element whose envelope does not contain the new point promotes to active processing.

The **cascade severity function** S maps context changes to promotion counts:

S(Δc) = |{ e ∈ dissolution inventory : c₀ ∈ V(e) ∧ (c₀ + Δc) ∉ V(e) }|

where c₀ is the current context point, Δc is the context change, and the result is the count of elements that were dissolved at c₀ but are no longer dissolved at c₀ + Δc.

This function is defined over the entire context space and has a definite value at every point. It is the processor's **fragility map** — a scalar field over context space telling you, for every possible context change, how many dissolutions break.

The function has characteristic features that follow from envelope geometry.

**Plateaus** are regions where S is low. Context can change substantially without breaking many dissolutions. Plateaus form where many validity envelopes overlap broadly — many elements remain dissolved across a wide range of conditions. Deep expertise developed under varied conditions creates wide plateaus.

**Cliffs** are regions where S has high gradient — small context changes produce large jumps in promotion count. Cliffs form where many validity envelopes have boundaries that are close together along some context dimension. If a pilot dissolved all cockpit skills under visual flight rules and never under instrument conditions, the transition from visual to instrument conditions is a cliff: many envelopes end at the same boundary, and crossing it promotes many elements simultaneously.

**Ridges** are extended cliff features — continuous surfaces in context space where moving in any perpendicular direction crosses many envelope boundaries. Ridges form when a single context dimension dominates many envelopes — for example, consciousness (awake vs. asleep), primary sensory modality (visual vs. instrument), or fundamental operating mode (peacetime vs. combat).

The cliff/plateau structure is not random. It is determined by the relationship between dissolution history and envelope geometry, which is in turn determined by training conditions. This makes the structure predictable from dissolution inventory analysis and — crucially — engineerable through training design.

---

### 5. Cliff Formation and Catastrophe

A cliff in the cascade severity function corresponds to many validity envelopes sharing a boundary in a narrow region of context space. The mechanism of cliff formation is therefore the mechanism of envelope boundary alignment: many elements dissolved under similar conditions produce similar envelope boundaries.

Consider a pilot who trained exclusively in clear weather. Every skill dissolved under visibility above 5,000 meters and turbulence below 1 m/s. Each dissolved element has an envelope boundary near these values along the visibility and turbulence dimensions. The cascade severity function is low (a plateau) for any context within these ranges — the pilot can handle variation in airspeed, heading, altitude assignment, traffic density, and many other dimensions without breaking dissolutions. But a context change that drops visibility below 5,000 meters or raises turbulence above 1 m/s crosses many envelope boundaries simultaneously. The severity function jumps from near-zero to a count potentially equal to the entire dissolution inventory along those dimensions.

This is a **dissolution cliff**: a region in context space where the gradient of the cascade severity function is large. Formally, define the cliff magnitude at context point c along dimension d:

cliff(c, d) = ∂S/∂d evaluated at c

When this partial derivative is large, small changes along dimension d produce many promotions. The cliff is steep. When it is near zero, the processor is on a plateau along that dimension.

Cliff formation has a direct relationship to catastrophe theory. The cascade severity function can exhibit fold-type behavior: smooth, low-valued across a plateau, then a sudden discontinuous jump at a cliff boundary. True discontinuities arise when many envelopes have identical boundaries — a product of perfectly uniform training conditions. When training conditions are slightly varied, envelope boundaries spread out and the cliff becomes a steep but continuous slope rather than a true discontinuity.

This distinction matters for prediction. A true cliff (discontinuous jump) provides no warning — the processor is fine, then suddenly overwhelmed. A steep slope (continuous but high gradient) provides a narrow warning zone where some elements promote before others, giving the processor a brief interval in which performance degrades but has not yet collapsed.

Define the **cliff width** along dimension d as the distance in context space between the first promotion and the last promotion in a cluster of aligned envelope boundaries:

cliff_width(c, d) = max boundary position − min boundary position for envelopes clustered near c along d

Narrow cliff width (many envelopes with nearly identical boundaries) produces sudden catastrophic cascades. Wide cliff width (envelopes with spread boundaries) produces gradual degradation that may be survivable if the processor recognizes early promotions and responds. Cliff width is directly engineerable through training variation, as detailed in Section 7.

---

### 6. The Fragility Profile

The cascade severity function S is a scalar field over the full context space. For a processor with a dissolution inventory of n elements across a context space of k dimensions, computing S at every point is in general expensive. In practice, the fragility profile — a tractable summary of the processor's vulnerability — captures the operationally relevant structure.

Define the **fragility profile** as the restriction of S to the operationally relevant context space: the region the processor is likely to actually encounter during operation, as opposed to the full theoretical context space.

For the pilot, operationally relevant context space is bounded by conditions that occur in actual flight — visibility from zero to unlimited, turbulence from none to severe, aircraft states from nominal to limit, and so on. Conditions outside this range (zero gravity, underwater, Mach 3) are operationally irrelevant.

Within the relevant region, the fragility profile has three summary statistics that characterize the processor's vulnerability.

**Maximum cascade count**: max S over the operationally relevant context space. This is the worst case — the largest number of simultaneous promotions the processor can experience under operationally realistic conditions.

**Cliff inventory**: the set of (context region, dimension, gradient magnitude, cliff width) tuples identifying every cliff in the operationally relevant space. This is the enumeration of specific vulnerabilities.

**Plateau coverage**: the fraction of operationally relevant context space where S is below a threshold value (one promotion, for instance). This measures how much of operational reality the processor can handle without cascade.

These three quantities — worst case, specific vulnerabilities, and safe operating region — are the fragility profile. They are computable from the dissolution inventory and validity envelopes, and they provide the basis for predicting cascade severity before cascades occur.

The fragility profile changes over time as the processor dissolves new elements and as existing envelopes widen through varied experience. A developing processor has a low dissolution inventory (few elements dissolved) with narrow envelopes — low maximum cascade count (few things to break) but also low plateau coverage (many things still cost active ops). A mature processor has a large dissolution inventory with varied envelope widths — high potential maximum cascade count (many things could break) but also high plateau coverage (most operational context is safe). An expert processor has a large dissolution inventory with wide envelopes — moderate maximum cascade count (envelopes are wide enough that most context changes stay within them) and high plateau coverage.

This produces a counterintuitive prediction: the most dangerous phase of processor development is the transition from mature to expert. The dissolution inventory is large (high potential cascade count) but some envelopes are still narrow (cliffs present). The processor is highly capable under normal conditions but has unresolved fragilities that the broad dissolution inventory makes potentially severe.

---

### 7. Training as Envelope Engineering

If dissolution fragility is determined by envelope geometry, and envelope geometry is determined by dissolution conditions, then training is engineering of the fragility profile. This section formalizes the relationship.

**Training breadth** along a context dimension d is the range of conditions experienced during dissolution practice:

breadth(d) = max(conditions experienced along d) − min(conditions experienced along d)

Envelope width is bounded below by training breadth — you cannot dissolve wider than you have practiced — and may exceed it by a generalization margin that depends on the element's structural properties.

**Training coverage** is the fraction of operationally relevant context space that falls within the training region:

coverage = vol(training region ∩ relevant space) / vol(relevant space)

High coverage means the processor has trained under conditions spanning most of what operational reality will present. Low coverage means substantial regions of operational reality lie outside training conditions and therefore outside validity envelopes.

**Cliff smoothing** is the deliberate introduction of context variation during training to prevent many envelopes from sharing identical boundaries. If the pilot trains altitude maintenance under five different turbulence levels evenly spaced from 0 to 5 m/s, the five dissolution processes produce five validity envelopes with slightly different boundaries along the turbulence dimension. No single turbulence value simultaneously exceeds all five envelopes. The cliff along that dimension is replaced by a graded slope — some elements promote before others, giving the processor warning and reducing peak cascade count.

Formally, cliff smoothing transforms a step function in S (many elements promoting at one boundary) into a ramp function (elements promoting sequentially across a range). The cliff width increases from near-zero (identical boundaries) to the range of boundary positions across the varied training instances.

The **training optimization problem** can now be stated precisely. Given:

- A target dissolution inventory (which elements should be dissolved)
- The operationally relevant context space (what conditions the processor will face)
- A training time budget T (bounded by the fundamental inequality — training ops compete with operational ops for pipeline capacity)
- A dissolution curve model D(n | x, p, κ) for each element

Find the distribution of training conditions across context space that minimizes the maximum cascade count across the operationally relevant space, subject to the constraint that total training time does not exceed T.

This is a minimax problem: minimize the maximum of S over the relevant context space, using the distribution of training contexts as the control variable. The structure of the problem has several properties.

First, uniform distribution of training conditions across the relevant context space is not optimal when the relevant space has regions of higher operational likelihood. More training time should be allocated to regions the processor is more likely to encounter, weighted by consequence of failure in those regions.

Second, there is a tradeoff between dissolution depth and dissolution breadth. Each repetition can be allocated to a new context condition (broadening envelopes) or to a repeated condition (deepening dissolution along the existing curve). Early in training, depth is more important — elements need to dissolve at all. Late in training, breadth dominates — elements are dissolved but envelopes need widening.

Third, cliff smoothing has diminishing returns. Once the cliff width along a dimension exceeds the time-budget capacity to handle sequential promotions (the processor can recover from one or two promotions before the next occurs), further smoothing provides marginal benefit. The target cliff width is determined by the processor's recovery rate — how quickly it can restabilize a promoted element.

---

### 8. Structural Prediction

The formal apparatus now supports prediction of cascade severity from structural analysis, without requiring the cascade to occur.

**Step 1: Dissolution inventory audit.** Enumerate dissolved elements. For each, estimate validity envelope boundaries per context dimension. Sources: training records (what conditions the processor has experienced), performance testing under controlled context variation (where does dissolution break?), or self-report (under what conditions does this skill feel automatic versus effortful?). The output is a data structure: a set of elements, each annotated with an envelope in context space.

**Step 2: Fragility analysis.** Compute the cascade severity function from the inventory. For each context dimension, identify cliff locations (regions where many envelope boundaries cluster). Compute the cliff inventory: for each cliff, its location in context space, the dimensions along which it runs, its magnitude (how many elements promote), and its width (how spread the boundaries are).

**Step 3: Risk assessment.** Cross-reference the cliff inventory against the operationally relevant context space. Cliffs that lie within operationally relevant conditions are real vulnerabilities. Cliffs outside operational reality (the pilot's cliff at zero gravity) are irrelevant. For each relevant cliff, compute the probability that operational context changes will cross it, given the distribution of context conditions in the operational environment.

**Step 4: Training prescription.** For each relevant cliff exceeding a severity threshold, specify the context variation needed during additional training to widen the relevant envelopes and smooth the cliff. The prescription is a set of (element, context dimension, target training range) tuples that, when executed, reduce the maximum cascade count in the operationally relevant space.

This four-step process connects dissolution geometry to the practical disciplines of training design, certification testing, and risk management. The dissolution inventory audit is a formalized version of what experienced instructors do informally when assessing a student's readiness. The fragility analysis makes the assessment rigorous and communicable. The training prescription makes remediation targeted rather than generic.

A critical property of this process is that it identifies vulnerabilities that are invisible during normal operation. A processor operating on a plateau performs excellently — all dissolved elements are producing correct results at zero cost. The plateau provides no indication of the cliff at its edge. Only the structural analysis reveals the cliff's existence and location. This is why expert pilots can fly beautifully for years and then fail catastrophically when a novel condition crosses an unidentified cliff — the plateau concealed the fragility.

---

### 9. Computational Dissolution as Test Case

The formalism applies to any processor, but computational systems offer precise measurability that makes them the ideal test case. Every quantity defined in this paper is directly observable with existing instrumentation.

**CPU cache as dissolution.** A memory access that has been cached has dissolved from a chain costing approximately 200 cycles (main memory access) to a lookup costing approximately 4 cycles (L1 cache hit). The dissolution occurred through repetition — the same memory location was accessed multiple times, and the cache hardware stored the result structurally.

The validity envelope of a cached entry is the region of access-pattern space where the cached value remains valid. It has clear dimensions: the entry remains valid as long as no other access evicts it (capacity constraint), no other processor modifies it (coherency constraint), and the access pattern continues to reference it (locality constraint).

A context switch changes the operating context. Another process runs, accesses different memory locations, and evicts cached entries. The returning process finds its dissolved memory accesses promoted back to active — each now costs 200 cycles instead of 4. The cascade count is the number of cache misses on return. This is directly measurable with hardware performance counters.

The dissolution inventory is the set of cached entries. The validity envelopes are computable from cache geometry (associativity, capacity, eviction policy). Context changes (other processes, interrupt handlers, system calls) have predictable effects on which envelopes are violated. The cascade severity function is therefore computable from cache state and workload characteristics.

Cliffs in the computational context space are predictable. A working set that fits in L1 cache has a cliff at the L1 capacity boundary — any context change that pushes the working set beyond L1 size promotes all excess entries simultaneously, and each promotion inflates access cost by 50x (from 4 cycles to 200). The cliff is sharp because cache eviction is all-or-nothing for each entry, and many entries may share the same vulnerability to capacity pressure.

**Branch prediction as dissolution with envelopes.** A correctly predicted branch has dissolved to zero pipeline stall ops. The branch predictor learned the pattern through repetition (the branch went the same direction many times) and now provides the correct prediction structurally.

The validity envelope extends along the branch-behavior dimension — the prediction holds as long as the branch continues to behave as trained. A change in input data characteristics can shift branch behavior, invalidating predictions for many branches simultaneously. The resulting misprediction spike is a cascade, measurable in pipeline stalls per instruction.

**Context switch as cascade event.** The context switch is the canonical computational cascade. Direct cost: the ops to save and restore register state (small, fixed). Cascade cost: the cache entries invalidated plus branch predictions invalidated plus TLB entries invalidated plus prefetch predictions invalidated. The total cost of a context switch is dominated by cascade recovery, not by the direct switch operation. This is why context switch benchmarks that measure only register save/restore dramatically underestimate true cost — they measure the direct ops and miss the cascade.

The fragility profile of a computational process is computable from its cache footprint, branch behavior entropy, memory access pattern, and the contention topology of the system it runs on. Current performance engineering practice already approximates this analysis informally. This paper provides the formal framework that unifies cache optimization, branch prediction analysis, working set management, and context switch cost estimation as instances of a single geometric apparatus: dissolution inventory, validity envelopes, and the cascade severity function.

---

### 10. Cross-Domain Predictions

The formalism produces testable predictions that are not domain-specific. Each follows from the geometric structure and should hold for any processor — biological, computational, organizational, or otherwise.

**Prediction 1: Cascade severity independence.** Two different triggering events that cross the same cliff in context space produce the same cascade count. The bee in the cockpit and a brief electrical flicker that causes the same instruments to blank for two seconds should produce equivalent cascade severity if they cross the same envelope boundaries. Severity is a property of cliff geometry, not trigger identity. Testable by measuring cascade counts across different triggers that produce the same context change.

**Prediction 2: Training variation superiority.** Training under varied conditions produces measurably lower maximum cascade counts than training under fixed conditions, for the same total training time. A pilot trained in three weather conditions for 100 hours each should have lower peak cascade severity than a pilot trained in one weather condition for 300 hours, despite identical total training investment. Testable by comparing fragility profiles across matched training cohorts with varied versus fixed conditions.

**Prediction 3: Training breadth bounds envelope width.** The validity envelope along any context dimension is bounded below by the range of conditions experienced during training. No processor dissolves wider than it has practiced, though generalization may provide additional margin beyond training range. The margin is bounded and element-specific. Testable by measuring dissolution maintenance under context conditions progressively beyond training range.

**Prediction 4: Cliff location tracks training boundaries.** Cliffs in the cascade severity function cluster at the boundaries of training conditions. The processor is most fragile at the edges of what it has practiced. A pilot trained in visibility down to 3,000 meters has a cliff near 3,000 meters along the visibility dimension, regardless of what other skills are dissolved. Testable by mapping cascade counts across systematic context variation and comparing cliff locations to known training boundaries.

**Prediction 5: Expertise increases both capability and potential fragility.** A processor with a large dissolution inventory has more free pipeline capacity (high capability) and more elements that can promote simultaneously (high potential cascade count). The expert is both more capable under normal conditions and more vulnerable to novel conditions than the intermediate practitioner who has fewer dissolved elements. This is not a paradox — the expert's cliffs are typically further from operational center (wider envelopes) — but the potential severity when a cliff is crossed is larger. Testable by comparing maximum cascade counts between expert and intermediate practitioners under identical novel conditions.

**Prediction 6: Cliff smoothing has a computable optimal point.** Beyond the cliff width at which the processor can recover from sequential promotions (one at a time, restabilizing before the next), additional smoothing provides no operational benefit. The optimal cliff width equals the processor's recovery capacity — how many sequential promotions it can absorb without exceeding the time budget. Wider smoothing wastes training time. Narrower risks catastrophic simultaneous promotion. Testable by measuring cascade recovery rate and comparing operational outcomes for cliff widths above and below the recovery-capacity threshold.

---

### 11. Scope and Open Problems

This paper introduces the validity envelope, the cascade severity function, and the cliff/plateau topology as formal objects. It provides a structural prediction methodology (inventory audit, fragility analysis, risk assessment, training prescription) and grounds the formalism in computational systems where every quantity is measurable. It states six cross-domain predictions.

The following remain open.

**Dissolution curve shape.** The curve family (exponential, power law, logarithmic) is constrained but not resolved. The paper assumes any monotonically decreasing curve approaching zero. Resolving the family requires systematic empirical measurement across domains — op counts over controlled repetition counts with controlled context consistency. The measurement methodology exists; the data collection is the gap.

**Generalization margin.** Envelope width exceeds training breadth by some margin that depends on element structure and processor characteristics. The existence of generalization is well-documented across domains (skill transfer, cache prefetch beyond observed patterns, pattern recognition beyond trained examples). A formal model of generalization margin — how much wider than training breadth, and governed by what properties — would strengthen envelope predictions.

**Envelope interaction.** This paper treats each dissolved element's envelope independently. In practice, envelopes may interact — dissolving one element may widen or narrow the envelope of another. A pilot who dissolves instrument flying may widen the envelopes of all navigation skills along the visibility dimension. A formal treatment of envelope interaction would capture these cross-element effects.

**Context dimension identification.** This paper assumes context dimensions are known. In practice, identifying the relevant dimensions of context space for a given processor and domain is itself a non-trivial problem. A methodology for systematic context dimension identification — determining which environmental factors affect dissolution validity — would extend the practical reach of the framework.

**Cascade recovery dynamics.** The paper treats promotion as binary (dissolved or not) and recovery as a cost (ops to restabilize). In practice, recovery from cascade has its own dynamics — some promoted elements can be quickly restabilized while others require extended reconstruction. A model of recovery priority and sequencing under cascade would extend the framework from prediction to active cascade management.

**The minimax training optimization in closed form.** The training optimization problem is stated precisely as a minimax over the cascade severity function with training distribution as the control variable. A general closed-form solution would require knowing the dissolution curve family, the generalization margin model, and the envelope interaction structure. Approximate solutions may be feasible for specific curve families under simplifying assumptions about envelope independence.

Each of these open problems has sufficient structural constraints from this paper to be a well-defined investigation with clear success criteria. The formal objects introduced here — the dissolution curve, the validity envelope, the cascade severity function, and the fragility profile — provide the coordinate system within which these investigations can proceed.

---

# Appendix: Supporting Tables

## HOWL-MATH-16-2026

---

### Table A: Formal Definitions

| Symbol | Name | Definition | Unit | Domain |
|--------|------|-----------|------|--------|
| D(n \| x, p, κ) | Dissolution curve | Op count for element x by processor p after n repetitions at context consistency κ | ops | Universal |
| C₀ | First-encounter cost | Maximum op count at n = 0; intrinsic to element-processor pair | ops | Universal |
| R* | Optimal reduction floor | Minimum ops any competent processor requires for reliable execution of element x | ops | Element-specific |
| κ | Context consistency | Stability of conditions across repetitions; κ ∈ [0, 1] where 1 = identical conditions every repetition | dimensionless | Universal |
| λ | Processor dissolution rate | Rate at which processor converts repetitions into op reduction; may depend on prior related dissolutions | ops/repetition | Processor-specific |
| V(e) | Validity envelope | Subset of context space within which dissolution of element e produces correct result at zero ops | region in context space | Element-specific |
| w(e, d) | Envelope width | Measure of V(e) projected onto context dimension d | dimension units | Element-dimension pair |
| vol(V(e)) | Envelope volume | Measure of V(e) in full context space | product of dimension units | Element-specific |
| S(Δc) | Cascade severity function | Count of dissolved elements whose envelopes do not contain the post-change context point | count (promotions) | Processor-state-specific |
| cliff(c, d) | Cliff magnitude | Partial derivative ∂S/∂d at context point c; rate of promotion count increase per unit change along d | promotions/dimension unit | Location-specific |
| cliff_width(c, d) | Cliff width | Distance between first and last envelope boundary in a cluster along dimension d near point c | dimension units | Location-specific |
| breadth(d) | Training breadth | Range of conditions experienced during dissolution along context dimension d | dimension units | Training-specific |
| coverage | Training coverage | Fraction of operationally relevant context space within training region | dimensionless, [0, 1] | Training-specific |

---

### Table B: Dissolution Curve Families

| Family | Functional Form | Half-Life | Early Behavior | Late Behavior | Training Investment Implication | Best-Fit Domains |
|--------|----------------|-----------|----------------|---------------|-------------------------------|-------------------|
| Exponential decay | C₀ × e^(−λn) + R* | Constant: ln(2)/λ | Moderate initial drop | Steady proportional decrease | Each training hour equally valuable in percentage terms regardless of current level | Cache hit rates; hardware adaptation; some procedural skills |
| Power law | C₀ × n^(−b) + R* | Increases with n | Rapid initial drop | Very slow refinement; long tail | Early hours disproportionately valuable; late refinement has poor returns | Motor skill acquisition; medical diagnostics; programming expertise; most human skill domains |
| Logarithmic | C₀ × (1 − k×ln(n+1)) + R* | Increases rapidly | Extremely rapid initial drop | Nearly flat; marginal returns | Initial exposure nearly sufficient; extended practice yields diminishing dissolution | Vocabulary recognition; simple reflex conditioning |

**Structural constraints common to all families:**
- D(0) = C₀ (starts at first-encounter cost)
- D(n) monotonically non-increasing for κ > 0 (consistent context reduces or maintains cost)
- D(n) ≥ R* until floor-to-zero transition (cannot dissolve below competence floor prematurely)
- lim(n→∞) D(n) = 0 (sufficient repetition in consistent context yields full dissolution)
- ∂D/∂κ < 0 for fixed n (higher consistency accelerates dissolution)

---

### Table C: Context Dimensions by Domain

| Domain | Dimension | Type | Range | Measurable By | Typical Envelope Width (Expert) | Typical Envelope Width (Novice) |
|--------|-----------|------|-------|---------------|-------------------------------|-------------------------------|
| Aviation | Visibility | Continuous (meters) | 0 – unlimited | Meteorological instruments | 0 – unlimited (instrument-rated) | 5,000m – unlimited |
| Aviation | Turbulence intensity | Continuous (m/s) | 0 – 25 | Accelerometers, pilot report | 0 – 15 (moderate-severe) | 0 – 3 (light only) |
| Aviation | Aircraft type familiarity | Discrete (type count) | 1 – N types | Training records | 3–5 types | 1 type |
| Aviation | Physiological state (fatigue) | Continuous (hours awake) | 0 – 36+ | Self-report, actigraphy | 0 – 20 (managed fatigue) | 0 – 12 |
| Surgery | Anatomical conformity | Continuous (deviation score) | 0 – 1 (normal to extreme variant) | Imaging, direct observation | 0 – 0.7 | 0 – 0.2 |
| Surgery | Bleeding rate | Continuous (mL/min) | 0 – 500+ | Suction measurement | 0 – 200 | 0 – 50 |
| Surgery | Team composition familiarity | Discrete (known/unknown) | 0 – 1 | — | Tolerates unfamiliar team | Requires familiar team |
| Surgery | Instrument availability | Discrete (available/substitute/absent) | 3 levels | — | Can improvise with substitutes | Requires standard set |
| Computation | Working set size | Continuous (bytes) | 0 – memory limit | Performance counters | Up to L3 capacity (managed) | Must fit L1 for performance |
| Computation | Access pattern locality | Continuous (stride variance) | 0 – address space | Performance counters | Tolerates moderate scatter | Requires sequential access |
| Computation | Cache pressure from competitors | Continuous (eviction rate) | 0 – total capacity/tick | Performance counters | Tolerable to moderate pressure | Near-zero pressure required |
| Computation | Branch behavior entropy | Continuous (bits/branch) | 0 – 1 | Branch predictor statistics | Low entropy (predictable) | Must be near-deterministic |
| Driving | Road familiarity | Discrete (known/unknown) | 2 levels | — | Tolerates unfamiliar routes | Requires familiar route |
| Driving | Traffic density | Continuous (vehicles/km) | 0 – gridlock | Traffic sensors, observation | 0 – high density | 0 – moderate density |
| Driving | Weather (visibility + traction) | Multidimensional | Clear to severe | Meteorological, road sensors | Clear to moderate rain/snow | Clear to light rain only |
| Driving | Cockpit distraction level | Continuous (interrupts/min) | 0 – high | Observation, event logging | 0 – moderate (managed) | 0 – near-zero required |
| Medicine | Presentation typicality | Continuous (deviation from classic) | 0 – 1 | Clinical assessment | 0 – 0.6 (atypical recognized) | 0 – 0.15 (textbook only) |
| Medicine | Patient communication clarity | Continuous (information quality) | 0 – 1 | — | Tolerates poor historian | Requires clear historian |
| Medicine | Time pressure | Continuous (minutes available) | 0 – unlimited | Clock, triage category | Effective under 5-minute constraint | Requires 20+ minutes |
| Medicine | Comorbidity count | Discrete (count) | 0 – 10+ | Chart review | 0 – 6 (complex patients) | 0 – 1 (simple presentations) |

---

### Table D: Cascade Severity Examples

| Scenario | Trigger | Trigger Magnitude | Context Change (dimensions) | Dissolved Elements Promoted | Recovery Ops Per Element | Total Cascade Ops | Time Budget | Budget Exceeded? |
|----------|---------|-------------------|----------------------------|---------------------------|-------------------------|-------------------|-------------|-----------------|
| Bee in cockpit | Insect | Negligible | Cockpit environment: normal → abnormal; visual reference: continuous → interrupted | 3 (altitude, heading, attitude) | 3–5 each | 10–16 | 1–2s at cruise speed | Yes (1.5–3×) |
| Instrument failure | Gyro tumble | Moderate | Primary instrument: available → failed; scan pattern: standard → partial panel | 4–6 (attitude, heading, turn coordination, instrument cross-check, approach tracking) | 4–8 each | 20–40 | Varies by phase of flight | Yes if in IMC; No if VMC |
| Server traffic spike (10×) | Load event | Large | Request rate: normal → 10×; auto-scaling: within limits → at config ceiling | 2 (auto-scaling, alert routing) | N × contention per request + 5–10 engineer context switch ops | 2 promotions + N×100 cycle inflation | 500ms per request | Yes, mass timeouts |
| Unexpected surgical anatomy | Anatomical variant | Small (one structure displaced) | Anatomical conformity: expected → variant; spatial model: valid → invalid | 3 (dissection plane, spatial orientation, monitoring pattern) | 3–4 ops/step (was 1) + 5–8 spatial rebuild + 3–5 communication ops | 2–3× op rate for affected portion + 5–10 min blocking for imaging | Anesthesia tolerance window | Within budget if expert, risk if novice |
| New codebase (developer) | Assignment change | N/A (planned) | Codebase familiarity: high → zero; tooling: customized → default; team conventions: known → unknown | 8–15 (navigation, naming conventions, build process, test patterns, debug strategies, code review norms, deployment, monitoring) | 5–15 each | 80–150 | Sprint duration | No (budget is weeks), but throughput drops 60–80% |
| Unfamiliar car (driver) | Rental pickup | Small | Vehicle: familiar → unfamiliar; control positions: known → unknown; mirror positions: calibrated → uncalibrated | 4–6 (mirror check, turn signal, wiper/washer, gear position, braking feel, blind spot geometry) | 2–4 each | 10–20 | First 30 minutes of driving | Usually no, but elevated risk during dissolution recovery |
| Power outage (household) | Grid failure | Large | Electricity: available → absent | 5–15 depending on automation level (lighting, heating/cooling, refrigeration, communication, cooking, water pressure, security, entertainment) | 1–5 each (finding alternatives) | 10–50 | Varies by criticality | Partially; critical functions (light, heat) have short budgets |
| Key team member departure | Resignation | Moderate | Team knowledge: distributed → concentrated; process: shared → gaps | 3–8 (code ownership, institutional memory, relationship management, process knowledge, decision precedent) | 10–30 each (documentation, retraining, redistribution) | 50–150 | Weeks to months | Usually no, but throughput degradation sustained |
| Cache flush (CPU) | Full invalidation | Small (one instruction) | Cache state: warm → cold | Hundreds to thousands of cached entries | 50–200× latency inflation per access | Thousands of inflated-cost accesses | Microseconds to milliseconds | Yes, visible as latency spike |
| Language immersion (traveler) | Country change | Large | Language: native → foreign; cultural conventions: dissolved → unknown | 20–50 (greetings, requests, reading signs, understanding announcements, social norms, transaction protocols, navigation, humor) | 5–20 each | 200–500 sustained ops | Real-time conversation speed | Yes for conversation; no for untimed tasks |

---

### Table E: Cliff Formation Patterns

| Pattern | Cause | Cliff Width | Cascade Character | Example | Mitigation |
|---------|-------|-------------|-------------------|---------|------------|
| Uniform training cliff | All dissolution under identical conditions; all envelopes share one boundary | Near zero (discontinuous) | Catastrophic simultaneous promotion; no warning | Pilot trained only in clear weather; first encounter with IMC promotes all weather-dependent dissolutions at once | Introduce progressive weather variation during training |
| Mode boundary cliff | Binary context dimension separates two operating modes; dissolutions cluster on one side | Width of transition zone between modes | Near-simultaneous promotion of mode-specific dissolutions | Day/night transition for driver; all daytime visual dissolutions promote at dusk | Train across mode boundary; dissolve in both modes |
| Capacity boundary cliff | Dissolution valid up to resource capacity limit; exceeding limit promotes all capacity-dependent elements | Narrow (capacity limits are hard) | Sharp promotion at capacity boundary; all elements exceeding capacity promote together | L1 cache capacity exceeded; all excess entries promoted simultaneously at 50× cost inflation | Manage working set to stay within capacity; tier dissolution across cache levels |
| Dependency cliff | Multiple dissolutions depend on single element remaining dissolved; that element's promotion cascades to dependents | Width of root element's envelope boundary | Chain reaction: root promotes, dependents follow | Lead surgeon's composure dissolves team's communication patterns; surgeon stress promotes own skills AND team coordination | Widen root element's envelope; cross-train dependents with varied root element states |
| Gradual degradation slope | Training under varied conditions; envelope boundaries spread across range | Wide (range of training variation) | Sequential promotion; elements break one at a time across the range; processor has time to compensate | Pilot trained across turbulence 0–8 m/s; at 10 m/s some skills promote, at 12 more, at 15 most; gradual workload increase | Already mitigated by training variation; slope width is the mitigation |
| Compound cliff | Multiple context dimensions change simultaneously; cliff exists in joint space not visible in any single dimension | Varies | Promotions triggered by combination of conditions that are individually within envelope but jointly outside it | Light turbulence + moderate fatigue + unfamiliar aircraft type; each alone is within envelope; combination crosses joint boundary | Train under combined conditions; dissolution in joint context space not just per-dimension |

---

### Table F: Fragility Profile Components

| Component | Definition | Computation Method | Interpretation | Units |
|-----------|-----------|-------------------|----------------|-------|
| Dissolution inventory size | Count of elements at zero ops | Enumerate dissolved elements | Larger = more capability, more potential cascade severity | count |
| Maximum cascade count | max S(Δc) over operationally relevant context space | Compute S at cliff locations; take maximum | Worst-case simultaneous promotions under realistic conditions | count (promotions) |
| Mean cascade count | Average S across operationally relevant context space weighted by context probability | Integrate S × P(context) over relevant space | Expected promotions per random context change | count (promotions) |
| Plateau coverage | Fraction of relevant context space where S ≤ threshold (e.g., 1 promotion) | Measure { c : S(c) ≤ threshold } / measure(relevant space) | How much of operational reality is safe from significant cascade | dimensionless, [0, 1] |
| Cliff count | Number of distinct cliffs in relevant context space | Identify regions where gradient of S exceeds threshold | Number of specific vulnerabilities | count |
| Mean cliff width | Average width of cliffs across all cliffs in inventory | Average cliff_width(c, d) across cliff inventory | Narrower = more catastrophic per cliff; wider = more gradual | dimension units |
| Dominant cliff dimension | Context dimension along which the steepest cliff runs | argmax_d { max_c cliff(c, d) } | Which type of context change is most dangerous | dimension identity |
| Recovery capacity | Maximum promotions per time unit that processor can restabilize without exceeding budget | (N/d̄ − baseline ops) / ops per recovery | How many simultaneous promotions are survivable | promotions/time unit |
| Fragility ratio | Maximum cascade count / recovery capacity | Division | Values > 1 indicate non-survivable worst case; < 1 survivable | dimensionless |

---

### Table G: Dissolution Infrastructure and Envelope Effects

| Infrastructure | Domain | Elements Affected | Op Reduction | Envelope Effect | Cascade Surface Effect |
|---------------|--------|-------------------|-------------|-----------------|----------------------|
| Clinical checklist | Medicine | Diagnostic enumeration and filtering | Eliminates 5–15 enumeration ops | Widens envelope along presentation typicality dimension; checklist compensates for atypical presentations | Reduces cascade surface: fewer elements to promote because checklist maintains structural correctness outside natural envelope |
| IDE autocomplete | Software | Token composition, API recall | 1–3 ops per completion | Widens envelope along codebase familiarity dimension; autocomplete compensates for unfamiliar APIs | Minimal cascade surface effect; promotes gracefully (autocomplete fails, developer types manually) |
| Type system / linter | Software | Error detection, type correctness | Eliminates entire debug chains for caught error classes | Widens envelope along code complexity dimension; type system catches errors processor would miss under cognitive load | Reduces cascade surface: errors that would promote debugging chains are caught structurally |
| Jigs and fixtures | Manufacturing | Part orientation, positioning, alignment | 2–4 ops per part | Widens envelope along part variation dimension; jig accommodates tolerance range | Reduces cascade: part variation that would break hand-positioning dissolution is absorbed by jig |
| Mise en place | Cooking | Ingredient measurement, preparation, sequencing | Reduces cooking chain 30–50% | Widens envelope along time pressure and complexity dimensions; pre-prepared ingredients decouple preparation from execution | Reduces cascade: unexpected timing changes don't cascade into ingredient preparation failures |
| Adaptive cruise control | Driving | Speed management, following distance | Eliminates 2–3 ops continuously | Narrows envelope in one dimension (system availability — if ACC fails, skills may not be dissolved) while widening in others (traffic density, fatigue) | Mixed: removes elements from cascade surface but adds new dependency cliff at system-failure boundary |
| Pre-computed weapons zones | Aviation | Engagement geometry computation | 5–8 ops reduced to 1 lookup | Widens envelope along tactical scenario dimension; covers geometries pilot hasn't personally computed | Reduces cascade surface for engagement decisions; dependency cliff if display system fails |
| Cache hierarchy | Computation | Memory access latency | 50–200× cost reduction per access | Widens envelope along access pattern dimension (prefetch tolerates some non-locality) | Creates capacity-boundary cliff: dissolution valid only while working set fits cache tier |
| Branch predictor | Computation | Pipeline stall avoidance | Eliminates stall ops for predicted branches | Widens envelope along execution pattern stability dimension | Creates misprediction cascade on workload change; recovery is pipeline flush (small, bounded) |
| Pre-flight checklist | Aviation | Aircraft configuration verification | Eliminates 10–20 configuration check ops | Widens envelope along aircraft state dimension; catches configurations that would break in-flight dissolutions | Reduces cascade surface by ensuring starting context is within envelope boundaries |
| Standard operating procedures | Organizations | Decision processes, escalation paths, communication protocols | Varies; typically 5–15 ops per covered scenario | Widens envelope along personnel variation dimension; SOP works regardless of who executes | Reduces cascade on personnel change; dependency cliff if SOP becomes outdated |
| Pattern libraries (software) | Software | Architectural decisions, component design | 10–30 ops per design decision | Widens envelope along problem variation dimension; known patterns cover problem space | Reduces cascade on requirement change for covered patterns; no effect on novel requirements |

---

### Table H: Training Design Parameters

| Parameter | Definition | Measurement | Effect on Fragility Profile | Optimization Direction |
|-----------|-----------|-------------|---------------------------|----------------------|
| Total training time | Hours allocated to dissolution practice | Clock hours | More time = more elements dissolved + wider envelopes; diminishing returns per element after power-law knee | Allocate to highest-impact elements first (largest C₀ or narrowest current envelopes) |
| Repetition count per element | Number of practice iterations for specific element | Count | Drives position on dissolution curve; early repetitions highest value (power law) | Target R* before broadening; full dissolution only for highest-frequency elements |
| Context variation range | Span of conditions experienced during practice per dimension | Max − min of training conditions per dimension | Directly determines minimum envelope width | Cover operationally relevant range; concentrate on dimensions with narrowest current envelopes |
| Context variation distribution | How training conditions are distributed within the range | Statistical distribution of training contexts | Uniform = even cliff smoothing; concentrated at edges = wider envelopes but potential internal gaps | Slightly edge-weighted to maximize envelope width; some interior samples to prevent mid-range gaps |
| Interleaving | Whether different elements are practiced in alternating sequence or blocked | Practice schedule structure | Interleaving slows individual dissolution curves but widens envelopes and reduces cliff alignment across elements | Interleave for operational robustness; block for rapid initial dissolution of critical elements |
| Combined condition exposure | Whether multiple context dimensions vary simultaneously during practice | Training scenario design | Combined variation dissolves in joint context space; prevents compound cliffs (Table E) | Include combined conditions after individual dimensions adequately covered |
| Stress inoculation level | Degree of physiological/cognitive stress during training | Physiological measures, workload metrics | Widens envelope along stress/fatigue dimensions; prevents cliff at stress boundary | Progressive increase; excessive stress impairs dissolution (high stress → low κ → slow curve) |
| Transfer element identification | Which elements share structural similarity enabling cross-dissolution | Structural analysis of element relationships | Dissolving transfer elements first accelerates dissolution of related elements via increased λ | Identify and prioritize high-transfer elements early in training sequence |
| Dissolution verification frequency | How often dissolution is tested under varied conditions | Test schedule | Identifies envelope boundaries before operational encounter; catches premature dissolution | Regular testing at and beyond envelope boundaries; more frequent for safety-critical elements |
| Recovery practice | Deliberate cascade induction and recovery during training | Scenario injection | Dissolves cascade recovery itself; lowers recovery ops; widens recovery-specific envelopes | Practice recovery from common cascade scenarios; builds meta-dissolution of the recovery process |

---

### Table I: Computational Dissolution Measurement

| Quantity | CPU Cache | Branch Predictor | TLB | Prefetcher |
|----------|----------|-----------------|-----|------------|
| Dissolved element | Cached memory value | Predicted branch direction | Virtual-to-physical page mapping | Anticipated memory access |
| First-encounter cost | ~200 cycles (main memory) | ~15–20 cycles (pipeline flush + refetch) | ~200 cycles (page table walk) | ~200 cycles (demand miss) |
| Dissolved cost | ~4 cycles (L1 hit) | 0 cycles (correct prediction) | ~1 cycle (TLB hit) | ~4 cycles (prefetched to L1) |
| Validity envelope dimensions | Working set size; access recency; associativity contention; coherency state | Branch history stability; input data characteristics; execution path consistency | Page access recency; TLB capacity; process virtual address stability | Access pattern regularity; stride consistency; prefetch queue depth |
| Cascade trigger | Context switch; working set expansion; competing process cache pressure | Workload change; input data change; phase transition in algorithm | Context switch; large allocation; address space reorganization | Access pattern change; stride break; random access burst |
| Cascade measurement | Cache miss count (hardware counter: LLC-load-misses) | Branch misprediction count (hardware counter: branch-misses) | TLB miss count (hardware counter: dTLB-load-misses) | Prefetch miss or useless prefetch count |
| Recovery cost per element | 50–200× latency inflation (4 cycles → 200 cycles per access) | 15–20 cycles pipeline penalty per misprediction | ~200 cycles per page table walk | Variable; depends on memory latency and prefetch lead time |
| Cliff location | L1/L2/L3 capacity boundaries; associativity saturation point | Branch entropy threshold where predictor accuracy drops; phase boundary in execution | TLB capacity boundary; large page vs small page threshold | Stride regularity threshold; sequential-to-random access transition |
| Cliff width | Near zero (cache eviction is binary per line) | Narrow (predictor accuracy degrades sharply past entropy threshold) | Near zero (TLB miss is binary per page) | Moderate (prefetcher degrades gradually as pattern weakens) |
| Dissolution infrastructure | Cache hierarchy (L1→L2→L3); prefetch; cache partitioning | Branch predictor training; profile-guided optimization; likely/unlikely hints | Huge pages; TLB prefetch; PCID (process context ID preserving TLB across switches) | Software prefetch instructions; access pattern restructuring; data layout optimization |

---

### Table J: Envelope Interaction Patterns

| Pattern | Description | Mechanism | Example | Consequence |
|---------|------------|-----------|---------|-------------|
| Positive coupling | Dissolving element A widens envelope of element B | A provides structural context that B depends on; A's dissolution stabilizes B's operating conditions | Dissolving instrument scan pattern widens envelope of heading maintenance (scan provides heading information structurally) | Efficient: dissolving A yields double benefit; A is high-priority training target |
| Negative coupling | Dissolving element A narrows envelope of element B | A's dissolved behavior assumes conditions that conflict with B under context change | Dissolving aggressive lane-change behavior narrows envelope of defensive following distance (aggressive assumptions conflict with defensive requirements under traffic density change) | Dangerous: A's dissolution creates hidden fragility in B; cliff in B tracks A's dissolution |
| Dependency chain | Element B's dissolution depends on element A being dissolved | B's processing chain includes A as a sub-operation; B cannot dissolve while A still costs ops | Surgical knot tying (B) cannot dissolve until instrument handling (A) is dissolved; A's ops are part of B's chain | Training order matters: dissolve dependencies first; dependency chain defines minimum training sequence |
| Shared boundary | Elements A and B have envelope boundaries at same location in context space | A and B dissolved under same conditions; both fail at same context boundary | All clear-weather flight skills share visibility boundary; crossing it promotes A and B simultaneously | Cliff amplification: shared boundaries increase cliff magnitude; varied training conditions for each element independently smooths the shared cliff |
| Compensatory | Element A's promotion is partially offset by element B remaining dissolved | B's dissolved output partially substitutes for A's function | GPS (B) remaining dissolved partially compensates for map-reading (A) promoting under stress; GPS provides position information A would have provided | Graceful degradation: compensatory elements reduce effective cascade count; robust architecture has compensatory pairs for critical functions |
| Cascade chain | Element A's promotion changes context such that element B's envelope is violated | A's promotion is itself a context change along a dimension B is sensitive to | Lead surgeon's composure (A) promotes under stress; loss of composure changes team communication context; team coordination (B) promotes as a result | Amplification: one promotion triggers another; cascade count exceeds initial trigger count; chains can propagate through dissolution inventory |

---

### Table K: Prediction Testing Specifications

| Prediction | Independent Variable | Dependent Variable | Measurement Method | Control Requirements | Expected Result | Falsification Criteria |
|-----------|---------------------|-------------------|-------------------|---------------------|-----------------|----------------------|
| 1. Severity independence | Trigger identity (different events producing same context change) | Cascade count | Count promotions (ops returning to active) after each trigger | Same processor, same dissolution state, same resulting context change vector | Equal cascade counts across different triggers | Cascade counts differ significantly for triggers producing identical context changes |
| 2. Training variation superiority | Training condition distribution (varied vs fixed) | Maximum cascade count across operational context space | Measure cascade counts under systematic context variation; take maximum | Matched total training time; matched element set; matched processor cohorts | Varied-condition cohort has lower maximum cascade count | Fixed-condition cohort matches or beats varied-condition cohort in maximum cascade count |
| 3. Breadth bounds width | Training range along context dimension | Envelope width along same dimension | Measure dissolution maintenance under progressive context variation beyond training range | Single dimension varied; all others held constant; dissolution verified before testing | Envelope width ≥ training breadth; dissolution breaks at or shortly beyond training range boundary | Dissolution maintained far beyond training range (generalization margin >> training breadth) |
| 4. Cliff location tracks training | Training boundary locations per dimension | Cliff locations in cascade severity function | Map cascade counts across systematic context variation; identify steep gradients | Known training boundaries; systematic context sweep | Cliffs cluster at or near training boundaries | Cliffs appear at locations unrelated to training boundaries |
| 5. Expertise increases potential fragility | Dissolution inventory size (expert vs intermediate) | Maximum cascade count under novel conditions | Measure cascade counts under conditions outside both cohorts' training | Novel conditions equally distant from both cohorts' training boundaries | Expert has higher maximum cascade count than intermediate under equivalent novel conditions | Intermediate matches or exceeds expert in maximum cascade count under novel conditions |
| 6. Optimal cliff width | Cliff width (controlled via training variation) | Operational cascade survival rate | Measure performance maintenance across cliff-crossing context changes for varied cliff widths | Controlled cliff widths; matched cascade magnitudes; measured recovery capacity | Survival rate plateaus at cliff width ≈ recovery capacity; no further improvement beyond | Survival rate continues improving linearly with cliff width well beyond recovery capacity |

---

### Table L: Cross-Domain Fragility Comparison

| Domain | Typical Dissolution Inventory Size | Typical Context Dimensions | Dominant Cliff Dimension | Typical Maximum Cascade Count | Typical Time Budget | Fragility Ratio (max cascade / recovery capacity) | Primary Mitigation Strategy |
|--------|-----------------------------------|--------------------------|------------------------|------------------------------|--------------------|-------------------------------------------------|---------------------------|
| Aviation (transport) | 200–500 elements | 8–12 | Weather/visibility mode boundary | 15–40 | Seconds (flight critical) to minutes (non-critical) | 2–5× (high; mitigated by crew resource management) | Simulator training across weather conditions; crew redundancy |
| Aviation (combat) | 300–600 elements | 10–15 | Threat environment transition (peacetime → engagement) | 20–50 | Sub-second (weapons employment) to seconds (tactical) | 3–8× (very high; mitigated by training intensity) | High-fidelity simulation; progressive threat exposure; wingman redundancy |
| Surgery | 150–300 elements | 6–10 | Anatomical variant / unexpected pathology | 10–25 | Minutes (per step) to hours (procedure) | 1–3× (moderate; mitigated by team and pausing) | Cadaver lab variation; simulation; team communication protocols |
| Driving | 50–150 elements | 5–8 | Weather + road surface mode boundary | 5–15 | 0.5–2 seconds (lane/collision) | 1.5–4× (high; limited mitigation available) | Progressive weather exposure; advanced driver training |
| Software engineering | 100–400 elements | 6–10 | Codebase/stack change | 8–15 | Hours to days (project timeline) | 0.3–0.8× (usually survivable; budget is long) | Onboarding documentation; pair programming; broad technology exposure |
| Medicine (emergency) | 200–500 elements | 8–12 | Atypical presentation / rare condition | 10–30 | Minutes (critical) to hours (stable) | 1.5–4× (high for critical; mitigated by protocols) | Case variety exposure; simulation; clinical checklists; team-based care |
| Cooking (professional) | 80–200 elements | 4–7 | Equipment failure / ingredient substitution | 5–12 | Seconds (timing-critical) to minutes (per dish) | 0.5–2× (moderate; recoverable for most failures) | Cross-training on equipment; ingredient flexibility practice; mise en place |
| Air traffic control | 150–400 elements | 6–10 | Traffic volume spike / system degradation | 10–25 | Seconds (separation) to minutes (flow management) | 2–5× (high; mitigated by sector splitting and coordination) | Progressive traffic load training; system failure simulation; team coordination |
| Manufacturing | 50–150 elements | 4–8 | Material change / machine malfunction | 5–15 | Seconds (per operation) to minutes (per unit) | 0.5–2× (moderate; jigs and procedures absorb variation) | Material variety exposure; machine cross-training; SOP development |
| Customer support | 30–80 elements | 3–6 | Product change / policy change / system outage | 3–10 | Minutes per ticket | 0.3–1× (usually survivable) | Cross-product training; knowledge base maintenance; escalation paths |

---

### Table M: Cascade Chain Analysis

| Chain Length | Description | Frequency | Severity Amplification | Example | Detection Method |
|-------------|-------------|-----------|----------------------|---------|-----------------|
| 1 (simple) | Trigger promotes elements directly; no secondary promotions | Most common | None; cascade count = directly promoted elements | Turbulence promotes altitude and heading maintenance | Direct envelope boundary analysis |
| 2 (coupled) | Promoted element's state change itself changes context, violating another element's envelope | Common in tightly coupled systems | Moderate; total count = direct + secondary promotions | Surgeon stress (direct) → promotes composure → team communication context changes → promotes team coordination (secondary) | Envelope interaction analysis (Table J cascade chain pattern) |
| 3+ (chain reaction) | Secondary promotions trigger tertiary promotions; propagation through dissolution inventory | Rare but catastrophic when it occurs | High; can amplify small trigger to inventory-wide cascade | Cache miss (direct) → increased memory latency → pipeline stall → branch predictor invalidation → further cache eviction from speculative execution cleanup | Graph analysis of envelope dependency relationships; identify cycles |
| Infinite (runaway) | Cascade chain includes cycle; promotions sustain themselves indefinitely | Theoretical concern; rare in practice due to pipeline exhaustion (processor stops attempting dissolution recovery) | Total; entire dissolution inventory eventually promotes | Organizational: key departure → knowledge gaps → errors → more departures → more gaps (turnover spiral) | Cycle detection in envelope dependency graph; presence of positive feedback in cascade chain |

**Cascade chain termination conditions:**
- Chain terminates when no promoted element's state change falls outside any remaining dissolved element's envelope
- Chain terminates when processor pipeline is fully consumed (no capacity to attempt further dissolution recovery)
- Chain terminates when processor abandons dissolution recovery and switches to fully conscious processing of all active elements
- Runaway chains terminate only through external intervention or exhaustion of the dissolution inventory

---

### Table N: Specification Summary

| Metric | Count |
|--------|-------|
| Formal definitions | 14 |
| Dissolution curve families | 3 |
| Dissolution curve structural constraints | 5 |
| Dissolution curve parameters | 3 (C₀, κ, λ) |
| Context dimensions catalogued | 20 (across 5 domains) |
| Cascade severity examples | 10 |
| Cliff formation patterns | 6 |
| Fragility profile components | 9 |
| Dissolution infrastructure examples | 12 |
| Training design parameters | 10 |
| Computational dissolution quantities | 4 systems × 10 properties |
| Envelope interaction patterns | 6 |
| Testable predictions | 6 |
| Cross-domain fragility comparisons | 10 domains |
| Cascade chain length categories | 4 |
| Structural prediction steps | 4 (audit, analysis, assessment, prescription) |
| Open problems | 6 |

---

### Key Equations Summary

**Dissolution curve:**
D(n | x, p, κ) = C₀ × f(n, λ, κ) + R*

**Validity envelope:**
V(e) = { c ∈ context space : dissolution of e produces correct result at c }

**Envelope width:**
w(e, d) = measure of V(e) projected onto dimension d

**Cascade severity function:**
S(Δc) = |{ e ∈ dissolution inventory : c₀ ∈ V(e) ∧ (c₀ + Δc) ∉ V(e) }|

**Cliff magnitude:**
cliff(c, d) = ∂S/∂d evaluated at c

**Fundamental inequality (from prior work, referenced throughout):**
Σ ops × d̄ ≤ N

**Fragility ratio:**
fragility ratio = max cascade count / recovery capacity

**Training coverage:**
coverage = vol(training region ∩ relevant space) / vol(relevant space)

