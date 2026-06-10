# The Geometry of Dissolution and Fragility
## Predicting Catastrophic Failure from Structural Analysis

**Registry:** [@HOWL-MATH-16-2026]

**Series Path:** [@HOWL-INFO-11-2026] → [@HOWL-INFO-12-2026] → [@HOWL-INFO-13-2026] → [@HOWL-MATH-14-2026] → [@HOWL-MATH-15-2026] → [@HOWL-MATH-16-2026]

**Date:** June 2026

**DOI:** 10.5281/zenodo.zzz

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

