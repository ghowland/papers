# THE GEOMETRY OF DISSOLUTION AND FRAGILITY — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: definitions → dissolution_curve → validity_envelope → cascade_severity → cliffs → fragility_profile → training → prediction → computation → open_problems → relationships → sections

# definitions(id|symbol|name|definition|unit)
D1|D(n\|x,p,κ)|Dissolution curve|Op count for element x by processor p after n repetitions at context consistency κ. D(n) = C₀ × f(n,λ,κ) + R*|ops
D2|C₀|First-encounter cost|Maximum op count at n=0; intrinsic to element-processor pair|ops
D3|R*|Optimal reduction floor|Minimum ops any competent processor requires for reliable execution. Below = blind, not dissolved|ops
D4|κ|Context consistency|Stability of conditions across repetitions. κ∈[0,1] where 1 = identical every repetition|dimensionless
D5|λ|Processor dissolution rate|Rate processor converts repetitions into op reduction. May depend on prior related dissolutions (transfer)|ops/repetition
D6|V(e)|Validity envelope|Subset of context space within which dissolution of element e produces correct result at zero ops|region in context space
D7|w(e,d)|Envelope width|Measure of V(e) projected onto context dimension d|dimension units
D8|vol(V(e))|Envelope volume|Measure of V(e) in full context space. For independent dimensions ≈ ∏ᵈ w(e,d)|product of dimension units
D9|S(Δc)|Cascade severity function|Count of dissolved elements whose envelopes do not contain post-change context point. S(Δc) = \|{e : c₀∈V(e) ∧ (c₀+Δc)∉V(e)}\||count (promotions)
D10|cliff(c,d)|Cliff magnitude|∂S/∂d at context point c. Rate of promotion count increase per unit change along d|promotions/unit
D11|cliff_width(c,d)|Cliff width|Distance between first and last envelope boundary in cluster along d near c|dimension units
D12|breadth(d)|Training breadth|Range of conditions experienced during dissolution along dimension d. Lower bound on envelope width|dimension units
D13|coverage|Training coverage|Fraction of operationally relevant context space within training region|dimensionless [0,1]
D14|fragility ratio|Fragility ratio|max cascade count / recovery capacity. >1 = non-survivable worst case|dimensionless

# principles(id|principle|rationale)
P1|Dissolution has conditions — validity envelopes define where dissolution holds|Pilot dissolved altitude maintenance under visual flight in calm air in familiar aircraft. Outside those conditions, task promotes back to active
P2|Cascade severity depends on cliff geometry, not trigger identity|Bee in cockpit and instrument flicker crossing same envelope boundaries produce same cascade count. Severity is property of cliff, not trigger
P3|Cliffs form where many envelope boundaries align|Uniform training → identical boundaries → discontinuous cliff. Varied training → spread boundaries → graded slope with warning
P4|Training is engineering of the fragility profile|Envelope geometry determined by dissolution conditions. Training conditions → envelope width → cliff location → cascade severity. All engineerable
P5|Most dangerous phase is mature-to-expert transition|Large dissolution inventory (high potential cascade) but some envelopes still narrow (cliffs present). Highly capable under normal conditions, vulnerable to novel conditions
P6|Plateau conceals cliff at its edge|Processor operating on plateau performs excellently — no indication of cliff. Only structural analysis reveals vulnerability. Why experts can fly beautifully for years then fail catastrophically

# dissolution_curve(id|attribute|description)
DC1|Structural constraints|Starts at C₀ (max). Monotonically non-increasing under consistent context. Bounded below by R* until floor-to-zero transition. Approaches zero asymptotically
DC2|Two distinct gaps|Current-to-R* = measurable inefficiency (improvable). R*-to-zero = what dissolution absorbs (competent → structural)
DC3|Three parameters|C₀ (element complexity), κ (context consistency), λ (processor dissolution rate)

# curve_families(id|family|form|half_life|training_implication|best_fit_domains)
CF1|Exponential decay|C₀×e^(−λn)+R*|Constant: ln(2)/λ|Each training hour equally valuable in percentage terms|Cache hit rates, hardware adaptation, some procedural skills
CF2|Power law|C₀×n^(−b)+R*|Increases with n|Early hours disproportionately valuable; late refinement poor returns|Motor skills, medical diagnostics, programming expertise — most human skill domains
CF3|Logarithmic|C₀×(1−k×ln(n+1))+R*|Increases rapidly|Initial exposure nearly sufficient; extended practice diminishing|Vocabulary recognition, simple reflex conditioning

# validity_envelope(id|concept|definition)
VE1|Context space|Product of all measurable context dimensions relevant to processor and domain. Point in context space = exact conditions
VE2|Envelope determination|Width along each dimension determined by dissolution history. Cannot dissolve beyond what practiced. Width ≥ training breadth + generalization margin
VE3|Envelope shape asymmetry|May have wide tolerance on one dimension, narrow on another. Altitude maintenance may tolerate wide airspeed variation but near-zero tolerance for visual reference loss
VE4|Width factors|Training breadth (lower bound on width) + generalization margin (additional width beyond training range, varies by element type and processor)

# cascade_severity(id|concept|description)
CS1|Dissolution inventory|Set of elements currently at zero ops, each with validity envelope in context space
CS2|Context change → promotions|Moving point in context space. Elements whose envelopes don't contain new point promote to active processing
CS3|Fragility map|S is scalar field over entire context space — for every possible context change, how many dissolutions break

# topology(id|feature|definition|formation_mechanism|implication)
TP1|Plateau|Region where S is low. Context changes substantially without breaking many dissolutions|Many envelopes overlap broadly — wide training under varied conditions|Safe operating region. Expert's normal domain
TP2|Cliff|Region where S has high gradient — small changes produce many promotions|Many envelopes share boundaries in narrow region. Product of uniform training conditions|Specific vulnerability. Catastrophic if narrow (no warning). Gradual if wide (some warning)
TP3|Ridge|Extended cliff in context space — moving perpendicular in any direction crosses many boundaries|Single context dimension dominates many envelopes (consciousness, sensory modality, operating mode)|Mode boundary. Crossing promotes many elements simultaneously

# cliff_patterns(id|pattern|cause|width|character|mitigation)
CP1|Uniform training cliff|All dissolution under identical conditions; all envelopes share one boundary|Near zero (discontinuous)|Catastrophic simultaneous; no warning|Introduce progressive variation during training
CP2|Mode boundary cliff|Binary context dimension separates operating modes; dissolutions cluster on one side|Width of transition zone|Near-simultaneous mode-specific promotions|Train across mode boundary; dissolve in both modes
CP3|Capacity boundary cliff|Dissolution valid up to resource capacity limit; exceeding promotes all capacity-dependent elements|Narrow (hard limits)|Sharp at boundary; all excess promote together|Manage working set within capacity; tier dissolution
CP4|Dependency cliff|Multiple dissolutions depend on single element remaining dissolved; its promotion cascades to dependents|Width of root element's boundary|Chain reaction: root promotes, dependents follow|Widen root's envelope; cross-train dependents with varied root states
CP5|Gradual degradation slope|Varied training → spread boundaries|Wide (range of training variation)|Sequential promotion; processor has time to compensate|Already mitigated — slope width IS the mitigation
CP6|Compound cliff|Multiple dimensions change simultaneously; cliff in joint space not visible in any single dimension|Varies|Triggered by combination individually within envelope but jointly outside|Train under combined conditions; dissolve in joint context space

# fragility_profile(id|component|definition|units)
FP1|Dissolution inventory size|Count of elements at zero ops|count
FP2|Maximum cascade count|max S over operationally relevant context space|count (promotions)
FP3|Plateau coverage|Fraction of relevant context space where S ≤ threshold|dimensionless [0,1]
FP4|Cliff inventory|Set of (region, dimension, gradient, width) tuples per cliff|structured
FP5|Recovery capacity|Max promotions per time unit processor can restabilize without exceeding budget: (N/d̄ − baseline ops) / ops per recovery|promotions/time
FP6|Fragility ratio|max cascade count / recovery capacity. >1 = non-survivable worst case|dimensionless

# fragility_evolution(id|stage|inventory|envelopes|max_cascade|plateau_coverage|characterization)
FE1|Developing|Low (few dissolved)|Narrow|Low (few things to break)|Low (many things still cost active ops)|Limited capability, limited fragility
FE2|Mature|Large|Mixed (some wide, some narrow)|High (many things could break)|High (most operational context safe)|High capability, unresolved fragilities — MOST DANGEROUS TRANSITION PHASE
FE3|Expert|Large|Wide|Moderate (wide envelopes keep most changes within)|High|High capability, cliffs far from operational center

# training_as_engineering(id|parameter|definition|effect_on_fragility|optimization)
TE1|Training breadth|Range of conditions experienced per dimension|Directly determines minimum envelope width|Cover operationally relevant range; concentrate on narrowest current envelopes
TE2|Training coverage|Fraction of relevant space within training region|High = most operational reality within envelopes|Weight toward high-likelihood + high-consequence regions
TE3|Cliff smoothing|Deliberate context variation to prevent aligned boundaries|Transforms step function in S to ramp. Width = range of boundary positions|Target cliff width = processor's recovery capacity. Wider = waste. Narrower = catastrophic
TE4|Depth vs breadth tradeoff|Repetitions on same condition vs new condition|Early: depth (elements need to dissolve at all). Late: breadth (envelopes need widening)|Shift allocation from depth to breadth as dissolution matures
TE5|Combined condition exposure|Multiple dimensions vary simultaneously|Dissolves in joint space; prevents compound cliffs CP6|After individual dimensions adequately covered
TE6|Recovery practice|Deliberate cascade induction and recovery|Dissolves cascade recovery itself; meta-dissolution|Practice recovery from common cascade scenarios
TE7|Transfer element identification|Elements sharing structural similarity enabling cross-dissolution|Dissolving high-transfer elements accelerates related dissolutions via increased λ|Prioritize high-transfer elements early

# minimax_problem(id|description)
MM1|Given: target dissolution inventory, operationally relevant context space, training time budget T, dissolution curve D(n) per element
MM2|Find: distribution of training conditions across context space that minimizes max S over relevant space, subject to total training time ≤ T
MM3|Properties: not uniform (weight by likelihood × consequence); depth-first then breadth; diminishing returns on cliff smoothing past recovery capacity

# structural_prediction(id|step|action|output)
SP1|Dissolution inventory audit|Enumerate dissolved elements. Estimate validity envelope boundaries per dimension from training records, performance testing, self-report|Set of elements annotated with envelopes in context space
SP2|Fragility analysis|Compute cascade severity function from inventory. Identify cliff locations where many boundaries cluster per dimension|Cliff inventory: location, dimensions, magnitude, width per cliff
SP3|Risk assessment|Cross-reference cliffs against operational context space. Compute probability operational changes cross each cliff|Relevant cliffs ranked by probability × severity
SP4|Training prescription|For each relevant cliff exceeding threshold: specify context variation needed to widen envelopes and smooth cliff|Set of (element, dimension, target training range) tuples

# computation_test_case(id|system|dissolved_element|first_cost|dissolved_cost|envelope_dimensions|cascade_trigger|cliff_location)
CT1|CPU cache|Cached memory value|~200 cycles (main memory)|~4 cycles (L1)|Working set size; access recency; associativity; coherency|Context switch; working set expansion; competing cache pressure|L1/L2/L3 capacity boundaries (near-zero width, binary eviction)
CT2|Branch predictor|Predicted branch direction|~15-20 cycles (flush+refetch)|0 cycles|Branch history stability; input data characteristics; path consistency|Workload change; input data change; phase transition|Branch entropy threshold (narrow, sharp degradation)
CT3|TLB|Virtual-to-physical mapping|~200 cycles (page walk)|~1 cycle|Page access recency; TLB capacity; address stability|Context switch; large allocation; address reorganization|TLB capacity boundary (near-zero width, binary miss)
CT4|Prefetcher|Anticipated memory access|~200 cycles (demand miss)|~4 cycles (prefetched to L1)|Pattern regularity; stride consistency; queue depth|Pattern change; stride break; random burst|Stride regularity threshold (moderate width, gradual degradation)
# Context switch is canonical computational cascade: direct cost small (register save/restore), cascade cost dominates (cache + branch + TLB + prefetch invalidation)

# cascade_examples(id|scenario|trigger|magnitude|dimensions_changed|promotions|total_cascade_ops|budget|exceeded)
CX1|Bee in cockpit|Insect|Negligible|Cockpit environment; visual reference|3 (altitude, heading, attitude)|10-16|1-2s at cruise|Yes 1.5-3×
CX2|Instrument failure (IMC)|Gyro tumble|Moderate|Primary instrument; scan pattern|4-6|20-40|Varies by phase|Yes if IMC
CX3|Server traffic spike 10×|Load event|Large|Request rate; auto-scaling limit|2 + N×contention|2 promotions + N×100 cycles|500ms/request|Yes
CX4|Unexpected surgical anatomy|Variant|Small|Anatomical conformity; spatial model|3|2-3× op rate + blocking|Anesthesia tolerance|Expert within; novice risk
CX5|New codebase (developer)|Assignment|N/A|Codebase; tooling; conventions|8-15|80-150|Sprint (weeks)|No but 60-80% throughput drop
CX6|Cache flush (CPU)|Full invalidation|Small (1 instruction)|Cache state: warm→cold|Hundreds-thousands|Thousands inflated accesses|μs-ms|Yes, latency spike
CX7|Language immersion|Country change|Large|Language; cultural conventions|20-50|200-500 sustained|Real-time conversation|Yes for conversation

# envelope_interactions(id|pattern|description|consequence)
EI1|Positive coupling|Dissolving A widens B's envelope (A provides structural context B depends on)|Efficient: double benefit. A is high-priority training target
EI2|Negative coupling|A's dissolved behavior assumes conditions conflicting with B under context change|Dangerous: A's dissolution creates hidden fragility in B
EI3|Dependency chain|B's dissolution depends on A being dissolved (A is sub-operation of B)|Training order matters: dissolve dependencies first
EI4|Shared boundary|A and B dissolved under same conditions; both fail at same boundary|Cliff amplification. Mitigate by varied training per element independently
EI5|Compensatory|B remaining dissolved partially substitutes for A's function when A promotes|Graceful degradation. Robust architecture has compensatory pairs for critical functions
EI6|Cascade chain|A's promotion changes context, violating B's envelope. B's promotion may violate C's|Amplification: small trigger → inventory-wide cascade. Chains of length 2 common, 3+ rare but catastrophic

# cascade_chains(id|length|description|frequency|amplification)
CH1|1 (simple)|Trigger promotes elements directly; no secondary|Most common|None
CH2|2 (coupled)|Promoted element's state change violates another's envelope|Common in tightly coupled systems|Moderate
CH3|3+ (chain reaction)|Secondary promotions trigger tertiary; propagation through inventory|Rare but catastrophic|High
CH4|∞ (runaway)|Chain includes cycle; promotions sustain themselves. Terminates only by external intervention or inventory exhaustion|Theoretical; rare in practice|Total

# predictions(id|prediction|testable_by)
PR1|Cascade severity independence — different triggers crossing same cliff produce same cascade count|Measure counts across triggers producing identical context changes
PR2|Training variation superiority — varied conditions produce lower max cascade than fixed, for same total time|Compare fragility profiles across matched cohorts
PR3|Training breadth bounds envelope width — envelope ≥ training range; dissolution breaks at or shortly beyond boundary|Measure dissolution maintenance under progressive context variation
PR4|Cliff location tracks training boundaries — cliffs cluster at edges of what was practiced|Map cascade counts across systematic context variation
PR5|Expertise increases both capability AND potential fragility — expert has higher max cascade under novel conditions|Compare max cascade between expert and intermediate under equivalent novel conditions
PR6|Cliff smoothing has computable optimal point — optimal width = processor's recovery capacity|Measure outcomes for cliff widths above and below recovery threshold

# open_problems(id|problem|description)
OP1|Dissolution curve shape|Which family holds across domains? Requires systematic measurement: op counts over controlled repetitions with controlled κ
OP2|Generalization margin|How much wider than training breadth? Governed by what properties? Formal model needed
OP3|Envelope interaction|This paper treats envelopes independently. Cross-element effects (positive/negative coupling) need formal treatment
OP4|Context dimension identification|Which environmental factors affect dissolution validity? Methodology for systematic identification needed
OP5|Cascade recovery dynamics|Recovery priority and sequencing under cascade. Extends from prediction to active cascade management
OP6|Minimax training closed form|Requires knowing curve family + generalization margin + envelope interactions. Approximate solutions feasible under simplifying assumptions

# relationships(from|rel|to)
P1|defines|D6
P2|derives_from|D9 geometry
P3|explains|CP1-CP6
P4|grounds|TE1-TE7,SP1-SP4
P5|derives_from|FE2
P6|derives_from|TP1,TP2
D1|parameterized_by|D2,D4,D5
D1|bounded_by|D3
D6|determines|D9
D9|produces|TP1,TP2,TP3
TP2|formed_by|CP1-CP6
FP2|compared_against|FP5 to produce D14
SP1|feeds|SP2
SP2|feeds|SP3
SP3|feeds|SP4
EI6|produces|CH2-CH4
CT1|instance_of|D6 in computation
PR1|tests|P2
PR2|tests|P4
PR4|tests|P3

# section_index(section|title|ids)
1|The Phenomenon|P1,P6,D9
2|The Dissolution Curve|D1-D5,DC1-DC2,CF1-CF3
3|The Validity Envelope|D6-D8,VE1-VE4
4|The Cascade Severity Function|D9,CS1-CS3,TP1-TP3
5|Cliff Formation and Catastrophe|D10-D11,CP1-CP6,P3
6|The Fragility Profile|FP1-FP6,FE1-FE3,P5
7|Training as Envelope Engineering|TE1-TE7,MM1-MM3,P4
8|Structural Prediction|SP1-SP4,P6
9|Computational Dissolution|CT1-CT4
10|Cross-Domain Predictions|PR1-PR6,P2
11|Scope and Open Problems|OP1-OP6

# decode_legend
core_equation: D(n|x,p,κ) = C₀ × f(n,λ,κ) + R* (dissolution curve)
envelope: V(e) = {c ∈ context space : dissolution of e correct at c}
severity: S(Δc) = |{e : c₀∈V(e) ∧ (c₀+Δc)∉V(e)}| (count of broken dissolutions)
cliff: ∂S/∂d = rate of promotion increase per unit context change
fragility_ratio: max cascade / recovery capacity. >1 = non-survivable
training_optimization: minimax over S with training distribution as control variable. Target cliff width = recovery capacity
curve_families: exponential (constant returns)|power law (diminishing returns, most human skills)|logarithmic (rapid initial, long tail)
topology: plateau (safe, wide envelope overlap)|cliff (dangerous, aligned boundaries)|ridge (extended cliff along mode boundary)
prediction_methodology: inventory audit → fragility analysis → risk assessment → training prescription
id_prefixes: D=definition|P=principle|DC=dissolution_curve|CF=curve_family|VE=validity_envelope|CS=cascade_severity|TP=topology|CP=cliff_pattern|FP=fragility_profile|FE=fragility_evolution|TE=training|MM=minimax|SP=structural_prediction|CT=computation|CX=cascade_example|EI=envelope_interaction|CH=cascade_chain|PR=prediction|OP=open_problem
spec_counts: 14 formal definitions|3 curve families|5 curve constraints|6 cliff patterns|9 fragility components|6 envelope interactions|4 cascade chain types|6 testable predictions|6 open problems|10 cross-domain comparisons|4 computational systems|10 cascade examples|10 training parameters
