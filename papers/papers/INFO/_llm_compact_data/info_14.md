# BITS AND OPS: A COMPLETE THEORY OF INFORMATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: concepts_in_dependency_order → equations → cardinalities → states → reduction → dissolution → cascades → processing_entropy → optimal_reduction → concurrency_tax → compression → three_term_cost → bit_vs_op → applications → claims → relationships → sections → decode_legend

# This paper is the series capstone: all concepts from 20+ prior papers presented in dependency order as single self-contained document.

# concepts_in_dependency_order(id|order|name|definition|unit|introduced_in)
C1|1|Processor|Any system that transforms information into action; operates on one element at a time; substrate-independent|—|HOWL-COMP-1
C2|2|Op|One irreducible transformation by one processor; universal unit of processing; countable, observable, substrate-independent|count|HOWL-MATH-15
C3|3|Time budget (N)|Maximum duration available for processing; fixed by domain physics; does not negotiate or extend|time|HOWL-MATH-15
C4|4|Fundamental inequality|Σ ops × d̄ ≤ N; total processing bounded by time budget; every mechanism in framework reduces left side|ops×time ≤ time|HOWL-MATH-15
C5|5|Cardinality: Infinity|Population of elements; must be reduced to One before work occurs; processor stalled at Infinity regardless of power|—|HOWL-INFO-11
C6|6|Cardinality: One|Single element under operation; only cardinality where work happens; center to which Zero and Infinity relate|—|HOWL-INFO-11
C7|7|Cardinality: Zero|Outside operational boundary; can observe, cannot act; emits events into system, cannot receive operations|—|HOWL-INFO-11
C8|8|Reduction pipeline|Four-stage mechanism (enumerate→filter→score→select) collapsing Infinity to One; consumes the resource it allocates|ops|HOWL-INFO-12
C9|9|Dissolution|Processing chain collapsing into structure through repetition under consistent conditions; op count → zero; not forgetting but compression into structure|ops eliminated|HOWL-INFO-13
C10|10|State: Infinity|Population awaiting reduction; Hp positive|—|HOWL-INFO-13
C11|11|State: One|Under active operation; Hp positive and being consumed|—|HOWL-INFO-13
C12|12|State: Zero-absent|Dissolved into structure; was once at One; Hp = 0; result produced structurally without pipeline allocation|—|HOWL-INFO-13
C13|13|State: Zero-external|Permanently outside domain; never was at One; Hp undefined; correct response is structural resilience not processing|—|HOWL-INFO-13
C14|14|Validity envelope|Region of context space within which dissolution holds; width determined by practice conditions; narrow practice → narrow envelope|region|HOWL-MATH-16
C15|15|Cascade|Many dissolved elements promoting to One simultaneously when context crosses validity envelopes; severity = promotion count, independent of trigger magnitude|count|HOWL-MATH-16
C16|16|Processing entropy (Hp)|Op count for specific processor on specific element for specific goal in specific context; receiver-dependent unlike Shannon's H|ops|HOWL-INFO-13
C17|17|Optimal reduction (R*)|Minimum correct ops any competent processor requires; floor below which correctness lost, above which ops wasted|ops|HOWL-MATH-15
C18|18|Derivability classes|Classification of R*: Provable (theorem), Boundable (constrained range), Empirical (best observed)|—|HOWL-MATH-20
C19|19|Concurrency tax|Additional ops from execution environment: contention + cascade + coordination + blocking + interleave|ops+time|HOWL-MATH-18
C20|20|Contention graph|Graph of shared resources and competing streams determining tax structure and scaling law|—|HOWL-MATH-18
C21|21|Compression token|Symbol packing many referents into one transmissible unit; language is shared codebook dissolved across population|—|HOWL-INFO-13
C22|22|Compression ratio|Referents per token for given processor; grows with experience (child: 2-3, adult: 15, expert: 50-120)|count|HOWL-INFO-13
C23|23|Three-term cost|Cost(A→B) = Hp(A,encode) + Hs(channel) + Hp(B,decode); Shannon is middle term; endpoints usually dominate|ops+bits+ops|HOWL-MATH-19
C24|24|Dissolution differential|Gap in Hp between sender and receiver for same tokens; predicts communication difficulty|ops|HOWL-MATH-19
C25|25|Layered encoding|Message structured in layers of increasing dissolution infrastructure; each receiver consumes only needed layers|—|HOWL-MATH-19
C26|26|Bit|Shannon's unit: one binary distinction; unit of information in transit|bit|Shannon 1948
C27|27|Processing entropy profile|Vector of Hp across task set; point in metric space; distance = skill gap; trajectory = learning|ops per component|HOWL-MATH-17
C28|28|Skill gap vector|g(p,r) = H(p) − H(r); has magnitude (total size), direction (which tasks), shape (concentrated vs distributed)|ops|HOWL-MATH-17

# bit_vs_op(id|property|bit_shannon|op_processing)
BO1|Measures|Information in transit|Information under action
BO2|Domain|Channel between processors|Endpoint at processor
BO3|Defined by|One binary distinction|One irreducible transformation
BO4|Receiver-dependent?|No — same bits regardless of receiver|Yes — same element, different ops for different processors
BO5|Zero means|No information (trivial source)|Dissolved — processing happens structurally at zero cost
BO6|Optimization principle|Encode at entropy rate, no fewer bits|Reduce to actionability, no fewer ops
BO7|Over-optimization penalty|Information loss (under-encoding)|Actionability loss (over-reduction)
BO8|Fundamental limit|Channel capacity C (bits/second)|Time budget N / d̄ (ops/period)
BO9|Universal across|All channels regardless of medium|All processors regardless of substrate
BO10|Fungibility|Bit over fiber = bit over copper = bit by mail|Op by CPU = op by surgeon = op by pilot

# cardinalities(id|cardinality|nature|can_emit|can_receive|role|example)
K1|Zero|Outside operational boundary|Yes (one-way)|No|Boundary; defines system character; source of initial events|Weather; speed of light; BIOS; hardware failure physics
K2|One|Unit of work|Yes|Yes|Center; orchestration; all work occurs here|Surgeon operating; CPU executing; pilot engaging
K3|Infinity|Population awaiting reduction|Yes (when promoted)|Yes (when promoted)|Source from which members drawn; passive until promoted|Processes; patients; bugs; radar contacts

# four_states(id|state|cardinality|dissolution|hp|pipeline_cost|correct_response|transitions_to)
ST1|Infinity|Infinity|N/A|Positive|Pending|Reduce: enumerate→filter→score→select|One (via reduction)
ST2|One|One|Active|Positive, being consumed|Active|Execute, complete, release|Zero-absent (dissolution) or Infinity (release)
ST3|Zero-absent|Zero|Dissolved through repetition|Zero|Zero (free)|Trust; leave alone; do not re-introduce management|One (cascade if context crosses validity envelope)
ST4|Zero-external|Zero|N/A (never at One)|Undefined|Zero (impossible)|Build resilience; accept permanence|No transition possible

# reduction_pipeline(id|stage|function|input|output|failure_mode|failure_character)
RP1|Enumerate|Make population explicit and finite|Unknown N|Known listable N|Correct answer not in set|Invisible from inside; most dangerous
RP2|Filter|Eliminate irrelevant candidates|Known N|Smaller N|Over-filter (correct eliminated) or under-filter (overwhelmed)|Over: answer gone; Under: analysis paralysis
RP3|Score|Evaluate against weighted considerations|Relevant N|Ranked candidates|Wrong weights or missing consideration|Correct present but outscored
RP4|Select|Commit highest-scored as One|Ranked candidates|One|Cannot commit; oscillation|Full information, no action; budget consumed

# concurrency_tax_components(id|component|mechanism|affects_ops|affects_duration|scales_with)
TX1|Contention|Resource held by other stream|No|Yes (inflated by wait)|Resource utilization ρ; nonlinear as ρ→1
TX2|Cascade|Other stream invalidates dissolution|Yes (promoted elements)|No|Coupling × activity rate × inventory
TX3|Coordination|Managing concurrent access|Yes (overhead ops)|No|Shared resources × access frequency × protocol cost
TX4|Blocking|Pipeline idle on critical resource|No|N/A (no op)|Critical resource utilization; hold times
TX5|Interleave|Deciding which stream to service|Yes (decision ops)|No|Ready streams; decision complexity

# derivability_classes(id|class|r_star_status|knowledge_source|example)
DC1|P (Provable)|Exact value, proven theorem|Task structure|Sorting (N log N); binary search (log N); parity (N)
DC2|B (Boundable)|Range: R_lower ≤ R* ≤ R_upper|Structural bounds|TSP approximation; criteria-based diagnosis
DC3|E (Empirical)|Best observed; revisable|Expert population measurement|Medical diagnosis; tactical combat; novel debugging

# dissolution_examples(id|domain|element|first_encounter_ops|dissolved_ops|time_to_dissolve)
DE1|Driving|Mirror check|6|0|6-12 months
DE2|Medicine|Classic pneumonia diagnosis|40-60|0|Years
DE3|Software|Navigate familiar codebase|25-40|0|Months
DE4|Aviation|Instrument cross-check|8-12|0|Months (hundreds of hours)
DE5|Language|Native word recognition|3-5 per word|0|2-5 years (childhood)
DE6|Computation|Memory access (cached)|~200 cycles|~4 cycles|One access (hardware)
DE7|Computation|Branch prediction|~15-20 cycles (mispredict)|0 (correct predict)|Pattern training period
DE8|Mathematics|Solving 3x+7=22|10-15 steps|0 (instant)|Months-years (hundreds of problems)
DE9|Manufacturing|Assembly operation|3× expert time|Near zero conscious ops|Weeks-months
DE10|Music|Scale on instrument|10+ ops per note|0 (fluid)|Months-years (thousands of reps)
DE11|Cooking|Knife technique|15-20|0 (continuous flow)|Weeks-months (hundreds of reps)
DE12|Customer support|Known issue resolution|12|0 (pattern match)|Weeks-months (hundreds of tickets)

# cascade_examples(id|trigger|magnitude|promotions|severity|outcome|insight)
CE1|Bee in cockpit|Negligible|3 (altitude, heading, attitude)|High|Lane departure likely|Tiny trigger, large cascade
CE2|Thunderclap|Large|1 (calm assumption)|Low|Momentary startle, rapid recovery|Large trigger, small cascade
CE3|CPU context switch|1 instruction|Hundreds of cache entries|High|Latency spike; cascade cost 100× direct cost|Direct cost tiny; cascade dominates
CE4|Codebase refactor|Medium|6-15 navigation patterns|High|60-80% productivity drop for weeks|Dissolved codebase knowledge invalidated
CE5|Surgeon announcement|Small (one sentence)|3-5 (dissection plan, spatial model)|Moderate-high|Procedure time extends|Information event cascades through dissolved plan
CE6|Phone notification while driving|Small|2-3 (lane, speed, following distance)|Moderate|Elevated accident risk 15-30 sec|Dissolved driving skills temporarily promoted
CE7|Team reorganization|Large|8-15 per person × team size|Very high|Sustained productivity drop|Each person's dissolved org navigation breaks
CE8|Language immersion (new country)|Large|20-50 communication patterns|Very high|Communication failure for weeks|Entire dissolved codebook invalidated

# equations(id|name|formula|meaning|scope)
EQ1|Fundamental inequality|Σ ops × d̄ ≤ N|Total processing bounded by time budget; every mechanism reduces left side|Universal
EQ2|Three-term cost|Cost(A→B) = Hp(A,encode) + Hs + Hp(B,decode)|Total communication spans both frameworks; Shannon is middle term|Universal
EQ3|Processing entropy|Hp(x \| p,g,c)|Op count for specific processor, element, goal, context; receiver-dependent|Per tuple
EQ4|Dissolution curve|D(n \| x,p,κ) = C₀ × f(n,λ,κ) + R*|Op count decreasing over repetitions toward floor|Per element-processor pair
EQ5|Cascade severity|S(Δc) = \|{e : c₀ ∈ V(e) ∧ (c₀+Δc) ∉ V(e)}\||Count of elements whose envelopes don't contain new context|Per processor inventory
EQ6|Concurrency tax|tax(s,G) = contention + cascade + coordination + blocking + interleave|Total overhead derivable from contention graph|Per stream in graph
EQ7|Processor distance|d₂(p,q) = √(Σᵢ(Hp(tᵢ)−Hq(tᵢ))²)|Euclidean distance between processing entropy profiles|Per processor pair
EQ8|Skill gap vector|g(p,r) = H(p) − H(r)|Per-task cost difference; magnitude + direction|Per processor-reference pair
EQ9|Dissolution efficiency|η(word,B) = −ΔHp(B) / ΔHs|Receiver cost reduction per unit channel cost|Per word-receiver pair
EQ10|Throughput|N / (d̄ × H̄p)|Units completed per period; increases as Hp decreases through dissolution|Per processor

# applications(id|domain|primary_contribution|key_mechanism|measurable)
AP1|System specification|Four flat lists (CLA)|Cardinality determines interaction patterns; closed under addition|Entry count; completeness; gaps
AP2|Performance engineering|Fundamental inequality; dissolution|Reduce ops not speed; dissolve routine to free budget|Op count; dissolution curve; throughput
AP3|Training design|Dissolution curves; validity envelopes; derivability|Target R*; widen envelopes via varied practice|Op count over reps; envelope width; cascade count
AP4|Expertise assessment|Processing entropy profiles; metric space|Distance = skill difference; direction = specific gaps|Profile distance; gap magnitude; closure rate
AP5|Communication design|Three-term cost; dissolution differential; layered encoding|Minimize total cost; add infrastructure where differential high|Total cost per receiver; differential per token
AP6|Documentation quality|Hp minimization across reader population|Quality = content/cost; layered for heterogeneous audiences|Reader time; lookup rate; completion; comprehension
AP7|API design|Hp per consumer; layered surface|Consistent conventions dissolve; progressive disclosure|Consumer ops per call; error rate; time to first success
AP8|Organizational design|Contention graph; concurrency tax|Topology determines tax scaling; optimal team size computable|Tax per member; marginal tax; throughput vs size
AP9|Failure prediction|Cascade severity; fragility profile|Predict cascade from inventory + envelopes before event|Max cascade; cliff locations; plateau coverage
AP10|Reliability engineering|Zero-external classification; structural resilience|Classify boundaries; build resilience not control|Misclassification rate; response coverage

# series_map(id|paper|title|core_contribution)
SM1|HOWL-COMP-1-10|Execution pipeline and architecture|Runtime; entity system; state machines; utility AI; envelopes
SM2|HOWL-COMP-11|Name Driven Development|Name every state change before coding; enum as architecture
SM3|HOWL-COMP-12|Closed Loop Architecture|Four flat lists; EntityGroups with cardinality; closed under addition
SM4|HOWL-INFO-11|Zero, One, and Infinity|Three cardinalities as intrinsic; interaction patterns; violations
SM5|HOWL-INFO-12|Reduction to Cardinality One|Four-stage pipeline; pipeline cost; pre-computed reductions; OODA
SM6|HOWL-INFO-13|Six States / Math Theory|Manageability axis; state function; dissolution; Hp; the op
SM7|HOWL-MATH-15|Measurement Theory|Op as unit; fundamental inequality; throughput; dissolution trajectories
SM8|HOWL-MATH-16|Geometry of Dissolution and Fragility|Validity envelopes; cascade severity; cliff/plateau; training as envelope engineering
SM9|HOWL-MATH-17|Processing Entropy as Metric Space|Profiles; processor/task distance; matrix factorization; skill gap; trajectories
SM10|HOWL-MATH-18|Concurrency Tax from System Structure|Contention graph; five components; architectural motifs; Brooks's Law
SM11|HOWL-MATH-19|Processing-Aware Communication|Three-term cost; dissolution differential; redundancy as infrastructure; layered encoding
SM12|HOWL-MATH-20|Derivability Classes|R* classification: provable, boundable, empirical
SM13|HOWL-INFO-14|Bits and Ops (this paper)|Complete framework in dependency order; capstone

# claims(id|claim|type|depends_on)
CL1|Information does two things: moves (bits) and gets acted on (ops); Shannon formalized movement; this framework formalizes action|framing|C2,C26
CL2|Together bits and ops cover everything information does; Shannon not superseded but completed|framing|CL1,EQ2
CL3|Processor constraint (one element at a time) is definition of operation, not limitation; parallelism = multiple processors each constrained|axiom|C1,C2
CL4|The only lever is reducing total ops; time budget is the wall; every mechanism in framework serves this|derivation|C3,C4,EQ1
CL5|Three cardinalities are intrinsic properties not design categories; interaction patterns are mechanical consequences|axiom|K1,K2,K3
CL6|Dissolution is the central mechanism: explains expertise, caching, compilation, muscle memory, habit, pattern recognition, fluency|derivation|C9,DE1-DE12
CL7|Cascade severity is count of simultaneous promotions, independent of trigger magnitude; small events can cause catastrophic failures|derivation|C15,CE1-CE8
CL8|Processing entropy is receiver-dependent unlike Shannon entropy; same element, different Hp for different processors|distinction|C16,BO4
CL9|R* parallels Shannon's source coding theorem: reduce to actionability, no fewer ops; below floor = guessing, above = waste|derivation|C17,BO6
CL10|Concurrency tax is derivable from contention graph topology; star = steep divergent, partitioned = bounded, hierarchical = logarithmic|derivation|C19,C20,TX1-TX5
CL11|Language works because compression codebook dissolved to zero across population; civilization is accumulated dissolution infrastructure|derivation|C21,C22
CL12|For most real communication, endpoint processing costs dominate Shannon's channel cost; Shannon optimized the cheapest term|observation|C23,EQ2
CL13|Expert underestimates receiver cost because dissolved skill invisible to introspection; structural not empathic failure|derivation|C24
CL14|No single encoding optimizes for heterogeneous audience; layered encoding approaches per-receiver optimum|derivation|C25

# rules(id|rule|rationale)
R1|Reduce ops, not increase speed; only lever against time budget wall|Fundamental inequality: Σ ops × d̄ ≤ N; d̄ generally fixed; reduce ops
R2|Classify elements into four states before acting|Misclassification produces named failures; correct state determines correct response
R3|Dissolve routine through repetition under varied conditions|Converts active ops to structural zero-cost; varied practice widens validity envelopes
R4|Measure disruption by cascade count, not trigger magnitude|Severity = promotion count; intervention targets envelope width not event prevention
R5|Minimize three-term total cost, not channel cost alone|Endpoint terms usually dominate; add dissolution infrastructure where differential high
R6|Use layered encoding for heterogeneous audiences|Each receiver consumes needed layers only; approaches per-receiver optimum
R7|Never attempt to manage Zero-external elements; build resilience|RAID doesn't prevent failure, makes it survivable; farmer builds cisterns
R8|Target R* in training; know which derivability class applies|Provable: exact target; Boundable: range; Empirical: match best observed

# relationships(from|rel|to)
C1|constrained_by|C2
C2|bounded_by|C4
C3|defines_wall|C4
C4|governs|all_processing
C5|reduced_by|C8
C6|where_work_occurs|C2
C7|boundary_of|C6
C8|transforms|C5_to_C6
C9|transforms|C11_to_C12
C9|mechanism_of|expertise
C14|determines_width_of|C9
C15|caused_by|C14_violation
C16|measures|C2_cost
C16|extends|C26
C17|floor_of|C16
C18|classifies|C17
C19|inflates|C16
C20|determines|C19
C21|enables|language
C22|grows_with|experience
C23|composes|C16_and_C26
C24|predicts|communication_difficulty
C25|solves|heterogeneous_audience
C26|measures|transmission_cost
C27|collects|C16_across_tasks
C28|computed_from|C27
EQ1|governs|C4
EQ2|composes|EQ3_and_shannon
CL1|defines|paper_scope
CL2|unifies|C26_and_C2

# section_index(section|title|ids)
1|Two Halves of One Subject|CL1,CL2,C26,C2
2|Processing|C1,CL3
3|The Op|C2,BO1-BO10
4|The Time Budget|C3,C4,EQ1,CL4
5|Three Cardinalities|K1,K2,K3,C5,C6,C7,CL5
6|Reduction|C8,RP1-RP4
7|Dissolution|C9,DE1-DE12,CL6
8|Four States|ST1-ST4,C10-C13
9|Dissolution Has Conditions|C14,C15,CE1-CE8,CL7
10|Processing Entropy|C16,C27,CL8
11|Optimal Reduction|C17,C18,DC1-DC3,CL9
12|The Concurrency Tax|C19,C20,TX1-TX5,CL10
13|Compression and Language|C21,C22,CL11
14|The Three-Term Cost|C23,C24,C25,EQ2,CL12,CL13,CL14
15|Bits and Ops|CL1,CL2,BO1-BO10

# decode_legend
two_units: bit (Shannon, information in transit) | op (this framework, information under action)
fundamental_inequality: Σ ops × d̄ ≤ N; every mechanism reduces left side
cardinalities: Zero(boundary,emit-only)|One(unit-of-work)|Infinity(population,must-reduce)
four_states: Infinity(pending)|One(active)|Zero-absent(dissolved,Hp=0)|Zero-external(permanent,Hp=undefined)
reduction: enumerate→filter→score→select; consumes the resource it allocates
dissolution: repetition under consistent conditions → op count → zero; not forgetting but structural compression
validity_envelope: region in context space where dissolution holds; width = practice variety
cascade: context crosses envelopes → simultaneous 0a→1 promotions; severity = count, independent of trigger magnitude
processing_entropy: Hp(x|p,g,c) = ops; receiver-dependent; zero = dissolved; undefined = zero-external
optimal_reduction: R* = minimum correct ops; provable|boundable|empirical; dual of Shannon source coding
concurrency_tax: contention+cascade+coordination+blocking+interleave; derivable from contention graph topology
compression: token packs referents; ratio grows with experience; language = shared codebook dissolved across population
three_term_cost: Hp(A,encode)+Hs(channel)+Hp(B,decode); Shannon = special case when endpoints zero; endpoints usually dominate
dissolution_differential: Σ[Hp(B)−Hp(A)] per token; predicts difficulty; expert cannot feel it (structural invisibility)
layered_encoding: base(expert)+layers(progressive infrastructure); solves heterogeneous audience
profile: vector of Hp across tasks; point in metric space; distance = skill gap; trajectory = learning
applications: system spec|performance|training|assessment|communication|docs|API|org design|failure prediction|reliability
claim_types: framing|axiom|derivation|distinction|observation
rel_types: constrained_by|bounded_by|defines_wall|governs|reduced_by|where_work_occurs|boundary_of|transforms|mechanism_of|determines_width_of|caused_by|measures|extends|floor_of|classifies|inflates|determines|enables|grows_with|composes|predicts|solves|collects|computed_from|defines|unifies
paper_role: series capstone; all concepts from 20+ papers in dependency order; self-contained
+standalone: this doc self-contained
