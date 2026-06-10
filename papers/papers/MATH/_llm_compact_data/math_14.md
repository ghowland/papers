# A MATHEMATICAL THEORY OF PROCESSING — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: axioms → states → definitions → reduction → dissolution → boundaries → compression → entropy → theorems → shannon_bridge → misclassifications → open_problems → claims → relationships → sections → decode_legend

# axioms(id|axiom|formal)
A1|A processor operates on exactly one element at a time; this is the definition of an operation, not a limitation|O(p, t) = |{x : active(x, p, t)}| ≤ 1
A2|Every element exists in exactly one of four states relative to processor, goal, and context|S(x, p, g, c) → {∞, 1, 0a, 0e}; mutually exclusive, exhaustive
A3|Action occurs only at state 1; no operation at ∞, 0a, or 0e|S(x, p, g, c) ≠ 1 → no operation on x
A4|Reduction from ∞ to 1 is finite chain terminating at minimum k where actionability predicate satisfied|∃ k : A(rₖ(x), g) = true, k is minimal
A5|Actionability predicate and reduction steps are domain-specific; reduction structure is domain-independent|A and rᵢ unspecified; chain composition, termination, optimality are universal

# states(id|symbol|name|definition|pipeline_cost|example)
ST1|∞|Infinity|Population of elements; multiple present, none selected; processor cannot act on population as population|Pending; capacity reserved for future reduction|Doctor facing 40 symptoms; database query facing 1M rows; radar showing 12 aircraft
ST2|1|One|Single element under active operation; only state where action occurs|Active; pipeline consumed for duration|Surgeon cutting one site; mathematician evaluating one sub-expression
ST3|0a|Zero-absent|Processing dissolved into structure; result produced without pipeline allocation; was once at 1, dissolved through repetition in consistent context; can regress to 1|Zero|Adult hearing native word; experienced driver maintaining lane; mathematician seeing 2+2=4
ST4|0e|Zero-external|Permanently outside processor's operational domain; can observe, cannot act; never was and never will be at 1|Zero; no processing possible|CPU heat generation; speed of light; weather; biological aging; other drivers' decisions

# state_function
# S(x, p, g, c) → {∞, 1, 0a, 0e}
# State is property of relationship among element x, processor p, goal g, context c — not property of element alone
# Same element can be at different states for different processors, goals, or contexts

# formal_definitions(id|symbol|name|definition)
FD1|S(x, p, g, c)|State function|Maps element to one of {∞, 1, 0a, 0e} relative to processor, goal, context
FD2|R(g)|Reduction chain|rₖ ∘ rₖ₋₁ ∘ ... ∘ r₁; terminates at min k where A(rₖ(x), g) = true
FD3|A(rₖ(x), g)|Actionability predicate|Binary: can processor act on current result toward goal g?
FD4|rᵢ|Reduction step|Single transformation: intermediate result → next intermediate result
FD5|R*|Optimal reduction|argmin k such that A(rₖ(x), g) = true ∧ all rᵢ correct
FD6|D(p, t)|Dissolution function|R(g) → 0a over time t through repetition in consistent context
FD7|M(x, p)|Manageability predicate|Binary: can processor p act on element x? M=false → S=0e
FD8|C(w)|Compression function|∞ → 1; packs Infinity of referents into transmissible token w; C⁻¹(w, c) exists
FD9|Hp(x \| p, g, c)|Processing entropy|Work required for processor p to reduce x to actionable 1 for goal g in context c
FD10|Hs|Shannon channel cost|Bits required for reliable transmission per Shannon's theorems
FD11|O(p, t)|Pipeline constraint|At most one active element at any moment

# state_transitions(id|from|to|name|trigger)
TR1|∞|1|Reduction|Pipeline selects element via reduction chain step
TR2|1|∞|Release to pool|Operation complete; element returns to population
TR3|1|0a|Dissolution|Repeated execution in consistent context collapses chain to structure
TR4|0a|1|Cascade promotion|Context change invalidates dissolution conditions
TR5|0a|1|Contextual promotion|Changed stakes or environment demand conscious processing
TR6|0e|0e|Boundary persistence|No transition possible; permanently outside domain
TR7|∞|0a|Mature bypass|Processor so experienced reduction chain dissolved before conscious engagement
TR8|pre-∞|∞|Acquisition|Element enters processor's recognition as discrete entity

# reduction_properties(id|property|description)
RP1|Steps can be wrong|Incorrect rᵢ moves output away from goal; error is incorrect transformation, not channel noise
RP2|Goal-relative|Same intermediate may be actionable for one goal, still ∞ for another; without goal, no termination condition
RP3|Over-reduction destroys actionability|Compressing beyond minimum discards information needed for action; optimal ≠ maximum compression
RP4|Minimum sufficiency|R* = minimum correct steps to actionability; processing dual of Shannon's source coding theorem
RP5|Domain-independent structure|Chain composition, goal-relative termination, optimality as minimum sufficiency — universal regardless of what processor does

# dissolution_properties(id|property|description)
DP1|Mechanism of maturity|Immature processor: most at ∞ or 1; mature: most routine dissolved to 0a; pipeline free for novel problems
DP2|Has validity conditions|Dissolved under specific assumptions; when conditions violated, element promotes back to 1
DP3|Not forgetting|Forgetting is loss; dissolution is compression of processing into structure producing correct result without scarce resource
DP4|Rate depends on|Repetition count, context consistency, processor characteristics (formalization is open problem)

# cascade(id|component|definition)
CA1|Triggering event|Context change c → c' that initiates cascade
CA2|Formal mechanism|∀x: S(x,p,g,c)=0a ∧ ¬valid(D(x), c') → S(x,p,g,c')=1
CA3|Severity|Count of 0a → 1 promotions; independent of event magnitude
CA4|Pipeline overload|Multiple elements at 1 simultaneously; pipeline handles only 1 (A1); overload when cascade count > 1
CA5|Mitigation|Widen dissolution validity envelopes through training under varied conditions; reduce cascade count for likely events
CA6|Temporal dimension|Novel event cascades on first encounter; response dissolves through its own maturity trajectory; boundary element stays 0e but response to it progresses 1→0a independently

# compression_properties(id|property|description)
CP1|Distinct from reduction|Reduction is lossy/goal-specific (selects one, discards rest); compression preserves population inside token (reversible via C⁻¹)
CP2|Context-dependent decompression|Same token decompresses to different referents in different contexts; "building on fire" vs "you're fired"
CP3|Cost determined by dissolution state|Token at 0a = zero pipeline cost; token at 1 = nonzero cost for decompression; unfamiliar jargon slows comprehension because each undissolved token costs pipeline
CP4|Maturity trajectory|Child's "fire" = low compression (one referent); adult's = high (hundreds); arson investigator's = higher (accelerant patterns, burn direction); ratio grows with experience
CP5|Language is shared codebook dissolved to 0a across population|Conversational-speed communication possible only because tokens are free; if every word required conscious decompression, speech incomprehensible at normal speed
CP6|Civilization consequence|Writing dissolved speaker-presence requirement; printing dissolved scribe requirement; each layer = 0a structure built on prior 0a structure freeing capacity for next unsolved problem

# processing_entropy(id|property|description)
PE1|Hp measures work to reduce x to actionable 1|Property of relationship among element, processor, goal, context — not element alone
PE2|Same Shannon H, different Hp|Same message produces different Hp at different processors; experienced analyst low Hp, new hire high Hp for same report
PE3|Hp = 0 when S = 0a|Element dissolved; no work required
PE4|Hp > 0 when S ∈ {∞, 1}|Work required; value = number and cost of reduction steps
PE5|Hp undefined when S = 0e|Outside domain; processing cannot occur
PE6|Maturity = systematic reduction of Hp toward zero|Each dissolution converts Hp from positive to zero across operational domain

# theorems(id|name|statement|proof_basis)
T1|Throughput Bound|Processor throughput bounded by ratio of 0a elements to total elements in operational domain|A1 (pipeline constraint); 0a elements produce results structurally without pipeline; throughput max as 0a ratio → 1
T2|Cascade Severity Independence|Disruption severity = count of 0a→1 promotions, independent of event magnitude|Cascade definition; A1 (overload when multiple at 1); small bee invalidating many dissolutions > large noise invalidating few
T3|Optimal Reduction|R* = min correct steps to actionability; processing dual of Shannon's source coding theorem|A4; shorter fails actionability; longer wastes capacity or destroys actionability through over-reduction
T4|Communication Cost Composition|Cost(A→B) = Hp(A, encoding) + Hs(channel) + Hp(B, decoding); Shannon recovered when Hp=0 at both endpoints|Processing entropy + Shannon's framework; independent cost terms across three pipeline stages

# shannon_bridge(id|property|shannon_channel|processing_endpoint)
SB1|Fundamental measure|H = −Σ p(x) log p(x)|Hp(x \| p, g, c)
SB2|Measures|Uncertainty in source|Work to reduce to actionable One
SB3|Property of|Source statistics (receiver-independent)|Relationship of element, processor, goal, context (receiver-dependent)
SB4|Optimization principle|Encode at entropy rate, no less|Reduce to actionability, no further
SB5|Error source|Noise in channel (external, imposed by medium)|Incorrect transformation in reduction chain (internal, produced by processor)
SB6|Optimal point|Minimum bits for reliable transmission|Minimum steps for actionable result
SB7|Over-optimization penalty|Information loss from under-encoding|Actionability loss from over-reduction
SB8|Scope|Source→Encoder→Channel→Decoder→Destination (middle)|Source processing and Destination processing (endpoints)
SB9|Composability|Cost = Hs|Cost = Hp(A) + Hs + Hp(B)
SB10|Zero state|N/A|0a: dissolved to structure, cost=0
SB11|Boundary state|N/A|0e: outside domain, processing impossible

# compression_vs_reduction(id|property|reduction_R|compression_C)
CR1|Operation|∞ →* 1(g)|∞ → 1
CR2|Lossy/Reversible|Lossy; selects one, discards rest|Reversible; C⁻¹(w,c) exists
CR3|Goal-dependent|Yes; termination by A(rₖ,g)|No; goal-independent
CR4|Purpose|Enable action by processor|Enable transmission between processors
CR5|Over-application|Destroys actionability|Destroys referent space; ambiguity irrecoverable
CR6|Maturity trajectory|Chain dissolves to 0a through repetition|Token dissolves to 0a at receiver through familiarity

# misclassifications(id|actual|treated_as|failure_name|example)
MC1|∞ (manageable)|∞ (unmanageable)|Learned helplessness|"We can't automate deploys" when deploys are documentable sequences
MC2|0e|1 (manageable)|Control illusion|Manager writing reports to reduce physics-dictated hardware failure rate
MC3|0a|1|Trust failure / regression|Adding manual approval to fully automated deployment pipeline
MC4|1|0a|Premature dissolution|Declaring feature "done" with known unaddressed edge cases
MC5|∞ (unmanageable)|∞ (manageable)|Enumeration trap|Writing firewall rule for every possible attack vector
MC6|0e|1 (manageable)|Dependency illusion|Building monitoring dashboard for upstream API believing dependency is "handled"

# maturity_stages(id|stage|state_distribution|hp_profile|pipeline_state)
MS1|Immature|Most at ∞, some at 1|Hp high across domain|Saturated; competing reductions overwhelm capacity
MS2|Developing|Some at 1 (stable), most at ∞|Hp decreasing for routine|Committed; organized but fully allocated
MS3|Mature|Most routine at 0a, novel at ∞ or 1|Hp ≈ 0 routine, >0 novel only|Available; capacity free for novel problems
MS4|Wise|Same as mature + accurate classification under pressure|Hp stable under disruption; cascade count minimized|Resilient; pipeline available during disruption

# math_as_instance(id|concept|mathematical_manifestation)
MI1|Infinity|Expression with multiple terms/operators; multiple sub-expressions awaiting evaluation
MI2|Reduction pipeline|Order of operations; predefined priority determining which sub-expression reaches 1 first
MI3|One|Single sub-expression under evaluation; one operation (two operands + one operator → one result)
MI4|Zero-absent|Proven theorem; memorized identity; dissolved notation (dx); axiom (accepted structural, never proved)
MI5|Zero-external|None; mathematics is purely manageable domain; only domain where framework collapses to three states
MI6|Dissolution of notation|dx dissolves centuries of infinitesimal debate into symbol; good notation converts processing from 1 to 0a
MI7|Processing entropy differential|Expert sees 3x+7=22, knows x=5 (Hp≈0); student works steps subtract 7, divide 3 (Hp>0); same expression, different Hp

# open_problems(id|problem|shannon_analog|direction)
OP1|Dissolution rate|Learning rate in coding theory|Formalize as function of repetition count, context variance, chain complexity
OP2|Inter-processor optimization|Source-channel separation theorem|Joint optimization of Hp(sender) + Hs + Hp(receiver)
OP3|Processing error correction|Error-correcting codes|Different mechanisms for internal (processor) vs external (channel) error
OP4|Processor network composition|Network information theory|Cascade propagation, dissolution dependencies between coupled processors
OP5|Compression ratio dynamics|Adaptive source coding|Formalize ratio as function of experience and domain exposure
OP6|Dissolution validity envelopes|No direct Shannon analog|Formalize conditions with measurable boundaries; cascade count as function of envelope width
OP7|Goal interaction|Multi-user information theory|Goal multiplexing on single pipeline; shared reduction sub-chains
OP8|Pre-Infinity formalization|No Shannon analog (assumes source exists)|Define acquisition as transition from outside state space to ∞

# claims(id|claim|type|depends_on)
CL1|Processing, like transmission, has mathematical structure universal across domains and substrates|axiom|A1-A5
CL2|Shannon formalized information movement; this paper proposes mathematics of information action|framing|SB1-SB11
CL3|All processors share common mathematics regardless of what they process, paralleling Shannon's proof that all channels share common mathematics regardless of physical medium|axiom|CL1
CL4|R* is processing dual of Shannon's source coding theorem: reduce to actionability, no further|derivation|T3,SB4,SB6,SB7
CL5|Disruption severity determined by cascade count (0a→1 promotions), independent of event magnitude|derivation|T2,CA3
CL6|Mathematics is an instance of the framework, not the source of it; the only domain with no 0e elements|observation|MI1-MI7
CL7|Language works because compression codebook is dissolved to 0a across population; if every word cost pipeline, speech incomprehensible|derivation|CP3,CP5
CL8|Shannon recovered as special case when Hp=0 at both endpoints|derivation|T4
CL9|Optimizing channel is necessary but not sufficient; dashboard delivering data to untrained operator is channel-optimal, processing-suboptimal|derivation|T4,PE2
CL10|Civilization is accumulated consequence of compression tokens dissolved to 0a across populations|derivation|CP6
CL11|Paper does not replace Shannon; extends framework to territory Shannon explicitly excluded (processing endpoints)|framing|SB8
CL12|Paper does not define goals, reduction steps, correctness, or actionability thresholds; power lies in universality exclusion enables|scope|A5

# rules(id|rule|rationale)
R1|Classify elements into four states before attempting action|Misclassification produces specific named failures (MC1-MC6); correct classification determines correct response
R2|Never attempt to manage 0e elements; engineer processor's own structure to survive boundary effects|RAID doesn't prevent disk failure, makes it survivable; farmer builds cisterns; sailor carries auxiliary propulsion
R3|Reduce to actionability, no further (R*)|Over-reduction destroys actionability; under-reduction prevents action; minimum sufficiency is optimal
R4|Measure disruption by cascade count, not event magnitude|Small event invalidating many dissolutions more severe than large event invalidating few; intervention targets dissolution validity width
R5|Maturity = systematic dissolution of Hp toward zero across operational domain|Each dissolution frees pipeline capacity; invest in dissolving routine so pipeline available for novel
R6|When both endpoints share dissolved codebook, total communication cost equals Shannon's channel cost only|Processing terms vanish; optimize Hp when differential is large, not just Hs

# relationships(from|rel|to)
A1|defines|ST2
A1|constrains|pipeline_to_one
A2|defines|ST1,ST2,ST3,ST4
A3|constrains|action_to_ST2
A4|defines|FD2,FD5
A5|scopes|universality
ST1|reduced_by|TR1
ST2|dissolves_to|TR3
ST3|promotes_to|TR4,TR5
ST4|permanent|TR6
FD2|composed_of|FD4
FD2|terminates_at|FD3
FD5|optimizes|FD2
FD6|converts|FD2_to_ST3
FD7|classifies|ST4
FD8|distinct_from|FD2
FD9|measures|reduction_work
T1|derives_from|A1,FD6
T2|derives_from|CA2,A1
T3|derives_from|A4,RP3,RP4
T4|composes|FD9,FD10
T4|recovers|shannon_as_special_case
CL4|parallels|shannon_source_coding
CL6|demonstrates|MI1-MI7
CL7|derives_from|CP3,CP5
CL8|derives_from|T4
RP4|dual_of|shannon_source_coding
CP1|distinct_from|FD2
MC1|misclassifies|ST1
MC2|misclassifies|ST4
MC3|misclassifies|ST3
MC4|misclassifies|ST2
CA3|independent_of|event_magnitude
PE1|extends|SB1
PE2|demonstrates|receiver_dependence

# section_index(section|title|ids)
1|Shannon's Boundary|CL2,CL11,SB8
2|The Processing Constraint|A1
3|The Four States|A2,A3,ST1-ST4,FD1
4|Reduction|A4,A5,FD2-FD5,RP1-RP5,CL4
5|Dissolution|FD6,DP1-DP4,TR3
6|Boundaries|FD7,ST4,R2
7|Mathematics as Instance|MI1-MI7,CL6
8|The Cascade|CA1-CA6,T2,TR4,CL5
9|Compression|FD8,CP1-CP6,CR1-CR6,CL7,CL10
10|Processing Entropy|FD9,PE1-PE6,MS1-MS4
11|The Bridge to Shannon|T4,SB1-SB11,CL8,CL9
12|Theorems|T1-T4
13|Scope and Exclusions|CL12,OP1-OP8

# decode_legend
states: ∞(Infinity/population)|1(One/under-operation)|0a(Zero-absent/dissolved)|0e(Zero-external/boundary)
state_function: S(x, p, g, c) → {∞, 1, 0a, 0e}; property of relationship among all four variables
pipeline_constraint: O(p,t) ≤ 1; one active element at any moment
reduction: R(g) = rₖ ∘ ... ∘ r₁; terminates at min k where A(rₖ(x),g)=true
optimal_reduction: R* = argmin k (correct steps to actionability); dual of Shannon source coding
dissolution: D(p,t): R(g) → 0a; has validity conditions; can regress via cascade
compression: C(w): ∞ → 1 with C⁻¹(w,c); preserves population in token; distinct from lossy reduction
processing_entropy: Hp(x|p,g,c); 0 at 0a, >0 at {∞,1}, undefined at 0e; receiver-dependent (unlike Shannon H)
communication_cost: Hp(A) + Hs + Hp(B); Shannon recovered when Hp=0 at both endpoints
cascade: context change invalidating dissolution conditions → 0a→1 promotions → severity = count independent of event magnitude
maturity: immature(saturated) → developing(committed) → mature(available) → wise(resilient)
misclassification_types: learned_helplessness|control_illusion|trust_failure|premature_dissolution|enumeration_trap|dependency_illusion
claim_types: axiom|derivation|observation|framing|scope
rel_types: defines|constrains|reduced_by|dissolves_to|promotes_to|permanent|composed_of|terminates_at|optimizes|converts|classifies|distinct_from|measures|derives_from|composes|recovers|parallels|demonstrates|dual_of|misclassifies|independent_of|extends|scopes
shannon_scope: Source→Encoder→Channel→Decoder→Destination (middle three); this paper covers endpoints
math_unique: only domain with no 0e elements; framework collapses to three states
+standalone: this doc self-contained