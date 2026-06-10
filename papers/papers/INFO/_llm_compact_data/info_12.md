# INFORMATION PROCESSING REQUIRES REDUCTION TO CARDINALITY ONE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → pipeline → failure_modes → reducibility_classes → domains → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|All information processing requires reduction of multiplicity to unity|Until N collapses to One, no work occurs; system is stalled regardless of domain or substrate
P2|The reduction pipeline has four stages in fixed logical order|Each stage depends on previous stage's output: enumerate→filter→score→select
P3|Reduction consumes the resource it allocates|CPU scheduler runs on CPU; pilot's attention spent orienting is attention not spent acting; planning time is doing time
P4|Optimal reduction is sufficiently correct One in least time, not most thorough|Sufficiency defined by domain; good-enough now dominates perfect later when situation changes
P5|Zero events invalidate current reduction|External events outside system control change situation, forcing partial or full pipeline re-execution
P6|Pre-computed reductions replace pipeline with lookup|Training, indexes, compilation, habits, pattern recognition all store prior reductions for instant retrieval
P7|Speed of reduction is competitive advantage that compounds|Faster entity injects Zero events into slower entity's pipeline, creating perpetual cardinality thrash
P8|Failure modes are stage-specific and require stage-specific intervention|Treating all reduction failures as same problem leads to wrong-stage interventions
P9|Some N resists reduction as intrinsic property|Unstable, self-referential, combinatorial, undecidable — each class has characteristic pipeline interaction
P10|The pipeline is descriptive not prescriptive|Not a proposed methodology; describes what already happens in every system that must act on one thing from many

# concepts(id|name|category|definition)
C1|Cardinality One|core|The unit of actual work; single operational focus that the system acts upon after reduction
C2|Cardinality Infinity|core|Multiplicity; population of candidates that must be reduced to One before work proceeds
C3|Cardinality Zero|core|What system references but cannot operate on; emits events into system, cannot receive operations
C4|Reduction pipeline|core|Four-stage mechanism (enumerate→filter→score→select) that collapses N to One
C5|Enumeration|pipeline_stage|Making multiplicity explicit and finite; unknown N becomes known N; precondition for all subsequent stages
C6|Filtering|pipeline_stage|Eliminating members not meeting relevance criteria; reduces N to smaller N; bounds scoring work
C7|Scoring|pipeline_stage|Evaluating filtered candidates against weighted considerations; imposes ordering on candidates
C8|Selection|pipeline_stage|Committing highest-scored candidate as One; transition from options to action
C9|Cardinality thrash|failure_mode|System spends more time re-reducing than acting on selected One; reduction overhead exceeds useful work; analogous to memory thrashing
C10|Zero event|core|External event outside system control that changes situation and may invalidate current One
C11|Pre-computed reduction|core|Prior reduction stored for instant retrieval at execution time; lookup replaces computation
C12|Commitment threshold|mechanism|Minimum score differential required to abandon current One; prevents premature re-reduction
C13|Meta-reduction|core|Judgment about how to reduce — which class of N, how much thoroughness, when to trust pre-computed result
C14|Maintenance failure|failure_mode|Internally triggered abandonment of selected One before action completes; distinct from Zero-event disruption
C15|Pipeline exhaustion|failure_mode|Degradation of reduction quality after many successive reductions; decision fatigue
C16|Buridan's paradox|failure_mode|Two candidates score nearly equally; system oscillates unable to select; pipeline stalls at selection despite full information
C17|Wicked problem|reducibility_class|Self-referential N where act of reduction changes the N; understanding problem changes problem
C18|Recognition-primed decision|core|Expert pattern match that replaces full pipeline; Klein's model of how pre-computed reductions fire in experienced practitioners
C19|OODA loop|core|Boyd's Observe-Orient-Decide-Act; maps to enumerate-filter-score-select; central insight is relative speed determines outcome
C20|Sufficiently correct One|core|Good-enough selection that enables action; domain-defined threshold below optimal but above wrong

# pipeline(id|stage|function|input|output|failure_name|failure_character)
PL1|Enumeration|Make multiplicity explicit and finite|Unknown N|Known listable N|Enumeration failure|Correct One never in candidate set; invisible from inside pipeline; most dangerous
PL2|Filtering|Eliminate irrelevant candidates|Known N|Smaller relevant N|Filtering failure (over or under)|Over: correct One discarded prematurely; Under: correct One buried in noise
PL3|Scoring|Evaluate candidates against weighted considerations|Relevant N|Ranked candidates|Scoring failure|Wrong One ranks highest due to miscalibrated weights or missing considerations
PL4|Selection|Commit highest-scored to operational focus|Ranked candidates|One|Selection failure|Cannot commit; oscillation between near-equal candidates; Buridan's paradox

# failure_modes(id|name|stage|character|symptom|consequence|resolution)
F1|Enumeration failure|enumeration|Correct One never in candidate set|System acts confidently on wrong One|Invisible until action produces unexpected results; most dangerous|Improve detection, broaden search, external information sources
F2|Over-filtering|filtering|Correct One discarded prematurely|May notice no remaining candidate is satisfying|Correct One eliminated before scoring|Relax criteria, allow backtracking to pre-filter set
F3|Under-filtering|filtering|Too many candidates pass to scoring|Overwhelm, analysis paralysis, "too many choices"|Scoring stage overwhelmed, cannot reliably distinguish correct One|Establish selection criteria before evaluation, narrow by feasibility
F4|Scoring failure|scoring|Wrong weights or missing considerations|Wrong One selected and acted upon|Correct One present but outscored by inferior candidate|Adjust weights, add missing considerations, change scoring curves
F5|Selection failure|selection|Near-equal scores, no clear winner|Oscillation, inability to commit, delay|No action despite full information; situation may change during oscillation|External commitment mechanism: coin flip, deadline, bias toward action, hierarchical tiebreaker
F6|Maintenance failure|post-selection|Internally triggered re-reduction without external cause|Perpetual re-scoring, abandoned partial actions|Cumulative incompleteness; switching costs compound; side effects from abandoned actions|Commitment threshold; "press the attack"; finish what you start; feature freeze
F7|Cardinality thrash|cross-stage|Zero events arrive faster than pipeline completes|Perpetual partial reduction, never reaches scoring/selection|System oscillates between enumeration and partial filtering; "everything urgent, nothing done"|Reduce Zero event rate: coalescing, batching, blocking, time-blocking; or accelerate pipeline
F8|Pipeline exhaustion|cross-stage|Many successive reductions deplete cognitive resource|Coarser filtering, simpler scoring, impulsive or avoidant selection|Decision quality degrades; each successive One is worse|Reduce decision volume, pre-compute routine decisions, protect pipeline capacity

# reducibility_classes(id|class|character|pipeline_interaction|appropriate_response)
RC1|Stable finite N|Well-structured, predictable|Pipeline executes cleanly and repeatedly|Standard reduction; pre-compute where possible
RC2|Unstable N|Input changes during pipeline execution|Produced One based on N that no longer exists|Pipeline speed: complete reduction before N changes (T < C); or act on acknowledged stale reduction with correction mechanisms
RC3|Self-referential N (wicked)|Act of reduction changes the N|Selecting One restructures remaining N; scores are interdependent|Adaptive management: tentative One, act, observe, re-reduce iteratively; many fast cheap approximate reductions
RC4|Combinatorially explosive N|Candidate space grows exponentially|Pipeline correct but time exceeds practical limit|Approximation: heuristics, greedy algorithms, simulated annealing; accept good-enough One
RC5|Undecidable N|No algorithm can complete reduction in general case|Enumeration cannot complete, no filtering bounds search|Recognize impossibility; redirect effort; do not attempt pipeline

# cost_tradeoff(id|factor|thorough_reduction|fast_reduction)
CT1|Speed|Slow — full pipeline execution|Fast — heuristics, pre-computed, pattern match
CT2|Accuracy|High — correct One more likely|Lower — may select wrong One
CT3|When appropriate|Cost of wrong selection high, cost of delay low|Cost of delay high, cost of wrong selection tolerable
CT4|Examples|Strategic planning, surgical planning, compiler optimization|Air combat, HFT, interrupt handling, conversation

# domains(id|domain|enumeration|filtering|scoring|selection|pre_computed|zero_events|failure_examples)
D1|CPU scheduling|Run queue populated|Ready-state processes only|Priority, time-since-last-run, interactivity, IO completion|Highest composite score runs|O(1) scheduler for normal load|Hardware interrupts|Batch job over interactive process (scoring failure)
D2|Fighter pilot (OODA)|Instruments/senses register battlespace|Stable background ignored, changes attended|Proximity, aspect angle, weapons capability, tactical priority|Commit to engagement|Trained scenario library; pattern recognition replaces pipeline|Missile warning, new contacts|Undetected bandit (enumeration failure); fixation on closest contact (scoring failure)
D3|Human cognition|Sensory cortices preprocess 11M bits/sec|Attentional networks flag salience|Prefrontal cortex biases toward task-relevant|Conscious awareness: ~50 bits/sec|Habits, expert intuition|Phone calls, notifications, interruptions|Inattentional blindness (filtering); change blindness (enumeration reset); decision fatigue (exhaustion)
D4|Medicine|Symptom gathering, history, labs, imaging|Tests eliminate candidate diagnoses|Prevalence, fit, severity weighting|Working diagnosis for treatment|Expert pattern recognition of symptom clusters|New symptoms, unexpected test results|Anchoring bias (selection); premature closure (filtering); availability bias (scoring)
D5|Jurisprudence|Discovery: all potentially relevant evidence|Admissibility rulings: rules of evidence|Argument and testimony: weighting evidence|Jury verdict: One judgment|Precedent; standard jury instructions|New evidence, witness recantation|Mistrial (selection failure); appeal (pipeline structural defect claim)
D6|Orchestra|N musicians producing N sound streams|Score specifies which instruments when|Conductor balances dynamics, tempo, expression|One coherent musical expression|Musical score is pre-computed reduction by composer|Musician rushing/dragging (voluntary compliance)|Poorly rehearsed = constant re-reduction; audience judges reduction quality
D7|TCP congestion|Packet loss rate, RTT, buffer occupancy sampled|Irrelevant signals filtered|Window adjustment scored by loss, RTT deviation, ECN|One congestion window setting|Steady-state algorithms for stable links|Packet loss events|Lossy link = cardinality thrash; never sustains throughput-producing One
D8|Market competition|Observe market conditions|Identify relevant signals|Evaluate strategic options|Commit to action|Lean startup: build-measure-learn as speed-of-reduction|Competitor actions, market shifts|Slow cycle = building for moved-on markets
D9|Evolution|Environmental signals registered|Sensory processing filters relevant|Organism evaluates response options|Selected response executed|Reflex arcs: pre-computed and hardwired; reduction performed once in evolutionary time|Predator appearance, environmental change|Slow reduction = caught by predator
D10|Software request handling|Parse request components|Route to matching handlers|Score by specificity and priority|Execute One handler|Compiled routing tables, cached resolutions|Request spikes, malformed input|Latency = reduction pipeline time

# claims(id|claim|type|depends_on)
CL1|Information processing is the specific physical act of reducing multiplicity to unity|axiom|P1
CL2|A CPU has one program counter; a human has one focus of conscious attention; a pilot has one adversary in gunsight — One is universal|observation|P1,C1
CL3|The four pipeline stages appear in same order across every domain because each depends on previous output|derivation|P2,PL1,PL2,PL3,PL4
CL4|Enumeration failure is the most dangerous because invisible from inside the pipeline|derivation|F1,PL1
CL5|A good decision now beats a perfect decision later because the perfect decision is optimized for a situation that no longer exists|derivation|P4,P7
CL6|Boyd's central insight: speed of loop relative to adversary determines outcome, not quality of any single decision|observation|C19,P7
CL7|Faster entity injects Zero events into slower entity's pipeline, creating perpetual cardinality thrash|derivation|P7,C10,C9
CL8|Expert intuition is library of pre-computed reductions; experts cannot articulate reasoning because reasoning happened during training not during decision|derivation|C18,C11,P6
CL9|Novice-to-expert progression is progressive accumulation of pre-computed reductions; competence-to-mastery is refinement of meta-judgment about when to trust them|derivation|C11,C13,P6
CL10|Overwhelm is subjective experience of N that resists reduction; intervention is structural (enumerate, filter, group, commit) not motivational|reframe|C2,C4
CL11|Tradeoff of pre-computed reductions is staleness; stored One was correct for N that existed when computed|derivation|C11,P6
CL12|The pipeline is descriptive of what already happens, not prescriptive methodology imposed on diverse domains|axiom|P10
CL13|Agile, adaptive strategy, iterative treatment, experimental science are formalized responses to irreducible N|observation|RC3,RC2
CL14|Structure aids reduction; unstructured N of 20 more overwhelming than structured N of 50 grouped into 5 categories|derivation|CL10
CL15|Natural selection is, among other things, selection for speed of cardinality reduction|derivation|P7,D9
CL16|Conversational competence is speed-quality balance of reduction pipeline in real time|observation|P4,P7
CL17|Human brain: 11M bits/sec sensory input to ~50 bits/sec conscious processing is most dramatic reduction pipeline in any known system|observation|D3

# rules(id|rule|rationale|applies_to)
R1|Diagnose failure by pipeline stage before intervening|Wrong-stage intervention wastes effort and may worsen correct-stage function|All failure modes
R2|Pre-compute reductions where N is stable and predictable|Replaces expensive runtime pipeline with instant lookup|RC1, any stable sub-domain
R3|Filter early at the boundary before expensive scoring|Bounds scoring work; rejects irrelevant candidates cheaply|PL2,PL3
R4|Use heuristics for sufficiently correct One when cost of delay exceeds cost of wrong selection|Perfect One computed against stale situation is worse than good-enough One now|CT3,CT4,P4
R5|Protect pipeline from Zero-event disruption via coalescing, batching, blocking|Ensures interval between disruptions exceeds pipeline completion time (I > T)|C9,C10,F7
R6|Design commitment mechanisms to prevent premature re-reduction|Once One selected and action begun, do not re-reduce unless score differential exceeds threshold or Zero event forces|C12,F6
R7|When T cannot be less than C, act on acknowledged stale reduction with correction mechanisms|Waiting for current N means never acting; build re-evaluation triggers and rollback|RC2
R8|Recognize irreducibility class early|Prevents wasted effort on pipeline that cannot produce result; redirects to appropriate response|RC3,RC4,RC5,C13
R9|Structure N to aid reduction|Group, categorize, externalize; reduces effective scoring cardinality|CL10,CL14
R10|Maintain meta-judgment about when pre-computed reductions apply|Always trusting = rigidity; never trusting = inexperience; mastery is knowing when to invoke full pipeline|C13,CL9

# relationships(from|rel|to)
P1|defines|C1
P1|defines|C2
P2|defines|C4
P3|constrains|C4
P4|defines|C20
P5|defines|C10
P6|defines|C11
P7|derives_from|C19
P8|defines|F1,F2,F3,F4,F5,F6
P9|defines|RC1,RC2,RC3,RC4,RC5
C2|reduced_by|C4
C4|produces|C1
C4|composes|C5,C6,C7,C8
C5|prereq_of|C6
C6|prereq_of|C7
C7|prereq_of|C8
C8|produces|C1
C10|invalidates|C1
C10|forces|C4
C9|caused_by|C10
C11|replaces|C4
C11|tradeoff|staleness
C12|prevents|C14
C13|determines|C4
C14|distinct_from|C10
C15|instance_of|P3
C16|instance_of|F5
C17|instance_of|RC3
C18|instance_of|C11
C19|maps_to|C4
F1|caused_by|C5
F2|caused_by|C6
F3|caused_by|C6
F4|caused_by|C7
F5|caused_by|C8
F6|caused_by|C12
F7|caused_by|C10
F8|caused_by|P3
RC2|mitigated_by|pipeline_speed
RC3|mitigated_by|adaptive_management
RC4|mitigated_by|approximation
RC5|requires|redirect_effort
CL5|grounds|P4
CL6|grounds|P7
CL7|derives_from|P7,C10
CL8|explains|C18
CL9|explains|C13
CL10|reframes|overwhelm
R1|implements|P8
R2|implements|P6
R3|optimizes|PL2
R4|implements|P4
R5|prevents|C9
R6|prevents|C14
R7|implements|RC2
R8|implements|P9
R9|implements|CL14
R10|implements|C13

# section_index(section|title|ids)
1|The Claim|P1,C1,C2,C3,CL1,CL2
2|The Reduction Pipeline|P2,C4,C5,C6,C7,C8,PL1,PL2,PL3,PL4,C16,CL3
3|The Cost of Reduction|P3,P4,C20,CT1,CT2,CT3,CT4,CL5
4|Zero Events as Reduction Invalidation|P5,C10,C9,F7,R5,CL7
5|Failure Modes of Reduction|P8,F1,F2,F3,F4,F5,F6,F8,C14,C12,C15,CL4,R1,R6
6|Speed of Reduction as Competitive Advantage|P7,C19,CL5,CL6,CL7,CL15,CL16,D8,D9
7|Pre-computed Reductions|P6,C11,C18,CL8,CL9,CL11,R2,R10
8|The Threshold of Reducibility|P9,RC1,RC2,RC3,RC4,RC5,C17,R8
9|Universality of the Reduction Requirement|D1,D2,D3,D4,D5,D6,D7,D10,CL12,CL17
10|Implications|CL10,CL13,CL14,R1,R2,R3,R4,R5,R6,R9

# decode_legend
pipeline_stages: enumeration|filtering|scoring|selection
failure_stages: enumeration|filtering(over/under)|scoring|selection|maintenance|cardinality_thrash|exhaustion
reducibility_classes: stable_finite|unstable|self_referential(wicked)|combinatorial(NP-hard)|undecidable
category_values: core|pipeline_stage|failure_mode|mechanism|reducibility_class
claim_types: axiom|derivation|observation|reframe
rel_types: defines|constrains|produces|composes|prereq_of|invalidates|forces|caused_by|replaces|prevents|instance_of|maps_to|mitigated_by|requires|grounds|derives_from|explains|reframes|implements|optimizes|distinct_from|determines|reduced_by|tradeoff
cost_factors: speed|accuracy|when_appropriate|examples
verification_ref: preceding paper [@HOWL-INFO-11-2026] established Zero/One/Infinity as intrinsic cardinalities (not cross-referenced; noted for provenance only)
+standalone: this doc self-contained