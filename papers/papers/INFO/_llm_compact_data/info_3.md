# THE PSEUDO-SOCRATIC METHOD — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → modes → loop → state_indicators → response_strategies → contrasts → applications → requirements → limitations → theory → claims → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Continuous state assessment ("you are here")|Before proceeding, assess what concepts are solid/shaky, what connections made, what assumptions operative, what gaps exist, what resistance present; GPS in conceptual space
P2|Adaptive information delivery based on assessed state|Information delivered based on where interlocutor actually is, not assumed progression; recalibrates continuously from response patterns
P3|Verification before progression|No advancement without verifying current understanding; each conceptual layer must be solid before building next
P4|Flexible communication modes|Use whatever form serves current need: statements, questions, corrections, examples, silence; not locked to questions-only like classical Socratic
P5|Surfs current reality|Dynamic navigation of conceptual space toward goals (convergent) or emergent discoveries (divergent); optimal path depends on current state

# concepts(id|name|category|definition)
C1|State assessment|core|Evaluating interlocutor's current comprehension: solid concepts, logical connections, operative assumptions, reasoning gaps, resistance/confusion
C2|Convergent mode|mode|Navigate toward specific destination (understanding, agreement); assess baseline, identify gaps to goal, close highest-priority gap, verify, iterate
C3|Divergent mode|mode|Explore solution space without predetermined destination; establish position, identify directions, apply utility function, take highest-value path, reassess
C4|Backfilling|operation|When gap detected, identify specific missing prerequisite, deliver it, re-verify original concept before advancing
C5|Reframing|operation|When resistance detected, acknowledge concern, explore source, find alternative path or framing; sometimes pause and return later
C6|Utility function|core|In divergent mode, what constitutes "good" outcomes; team/interlocutor's preferences that guide path selection at each branch point
C7|Verification|operation|Checking understanding through: application to novel examples, explanation in own words, prediction of system behavior, edge case questions
C8|Conceptual space navigation|core|Method treats understanding as a space with positions; each response reveals position; practitioner navigates toward destination (convergent) or explores optimally (divergent)

# modes(id|mode|objective|process|example)
M1|Convergent|Navigate toward specific destination|1. Assess baseline → 2. Identify gaps to goal → 3. Deliver to close highest-priority gap → 4. Verify → 5. Reassess and iterate|Explaining database indexing strategy; teaching recursion; stakeholder alignment
M2|Divergent|Explore solution space, optimize for utility|1. Establish position → 2. Identify available directions → 3. Apply utility function → 4. Take highest-value path → 5. Reassess from new position and iterate|Designing notification system; brainstorming novel approaches; design exploration

# assessment_loop(id|step|action)
AL1|Deliver|Provide information or ask question
AL2|Observe|Receive response
AL3|Analyze|Assess comprehension level, logical coherence, gap locations, misconceptions, readiness for next concept
AL4|Determine|Choose optimal next move: advance (solid), clarify (confused), backfill (gaps), reframe (resistance)
AL5|Execute|Perform chosen move
AL6|Return|Loop to AL1

# state_indicators(id|state|indicators)
SI1|Solid understanding|Correct application to new examples; asking about edge cases; accurate predictions; connecting to related concepts independently
SI2|Gaps|Hesitation/uncertainty; correct vocabulary but incorrect application; inability to answer "what happens if..."; contradictions between statements
SI3|Confusion|Asking about prerequisites; responses missing question's intent; requests for reframing/examples; silence or "I don't understand"
SI4|Resistance|Pushback not rooted in confusion; disagreement with approach; unwillingness to proceed on current path

# response_strategies(id|for_state|strategy)
RS1|Solid understanding|Advance to next concept; introduce complexity or edge cases; connect to broader context
RS2|Gaps|Identify specific missing prerequisite; backfill that prerequisite; re-verify original concept
RS3|Confusion|Provide concrete example; reframe using different analogy; simplify abstraction level; ask diagnostic questions to locate confusion source
RS4|Resistance|Acknowledge concern; explore source of resistance; reframe approach or find alternative path; sometimes pause and return later

# contrasts(id|method|structure|goal|limitation|vs_pseudo_socratic)
CT1|Classical Socratic|Teacher asks questions, student answers, contradictions exposed|Reveal ignorance, prompt self-discovery|Can feel adversarial; doesn't adapt to actual state|Pseudo-Socratic uses statements+questions, builds rather than exposes, adapts to state
CT2|Standard lecture|Linear delivery, periodic assessment|Transfer knowledge expert→learner|Proceeds regardless of comprehension|Pseudo-Socratic adapts delivery to assessed state continuously
CT3|Cognitive apprenticeship|Scaffolding and fading|Model expert thinking|Focus on modeling not adaptive path-finding|Pseudo-Socratic focuses on adaptive path-finding based on current state
CT4|Guided discovery learning|Structured activities for active construction|Learner constructs knowledge|Often uses fixed structured activities|Pseudo-Socratic is more free-form and adaptive
CT5|Adaptive learning systems|Algorithmic branching based on learner state|Adapt to learner|Follows algorithmic branching|Pseudo-Socratic involves human judgment about conceptual readiness

# applications(id|domain|advantage|example)
AP1|Technical education|Adapts to background; identifies misconceptions early; builds on solid foundations; prevents advancing with shaky understanding|Teaching distributed consensus by first assessing understanding of network failures
AP2|Stakeholder alignment|Identifies divergent mental models early; ensures shared foundation; surfaces disagreements; creates shared vocabulary|Aligning engineering/product/business on API design
AP3|Debugging and troubleshooting|Systematically eliminates possibilities; verifies assumptions at each step; prevents wild goose chases|Diagnosing production performance by assessing what's checked, identifying investigation gaps
AP4|Design exploration|Doesn't impose solutions; systematically evaluates based on actual constraints; surfaces trade-offs; enables emergent solutions|Designing product feature through adaptive questioning
AP5|Conflict resolution|Identifies disagreement source (facts vs values vs assumptions); creates common foundation; separates agreed from disputed|Two engineers arguing over architecture — discovering they optimize for different constraints

# requirements(id|type|category|items)
RQ1|Practitioner|Essential|Assess comprehension state from responses; deep domain understanding; flexibility to adapt; patience to backfill; skill in targeted questions/examples
RQ2|Practitioner|Helpful|Multiple explanatory frameworks for same concept; detect resistance vs confusion vs disagreement; pacing calibration through experience
RQ3|Interlocutor|Minimal|Willingness to engage; honesty about understanding
RQ4|Interlocutor|Helpful|Curiosity; comfort with iterative refinement; willingness to have assumptions challenged
RQ5|Context|Works well|Complex multi-layer topics; time for iterative exchange; shared understanding valuable
RQ6|Context|Works poorly|Simple information transfer; no interaction possible; hostile/uncooperative interlocutor

# limitations(id|concern|response|mitigation)
L1|Slower than direct explanation?|For simple topics yes; for complex topics often faster by preventing backtracking from foundational misunderstandings|Match method to topic complexity
L2|Could be used to manipulate?|Yes, any effective communication technique can be misused; designed for collaborative truth-finding|Transparency about process; focus on verifiable reasoning; acknowledge when values not facts discussed
L3|Doesn't scale to large groups|Correct; works one-on-one or small group (5-10)|Train others; document common paths; hybrid lecture+breakout approach
L4|Expert blind spots (curse of knowledge)|Practitioner may misjudge novice state|Explicit verification questions; encourage interlocutor to ask for clarification; calibrate by working with actual novices

# convergent_implementation(id|step|action)
CI1|Establish destination|What does successful understanding look like? What concepts must be solid? What connections must be made?
CI2|Assess starting position|What does interlocutor already know? What misconceptions exist? Learning style preference?
CI3|Identify critical path|Prerequisite concepts needed? Introduction order? Minimum viable concept set?
CI4|Execute loop|Deliver next concept → verify → assess state → adapt → repeat
CI5|Verify destination|Can they apply to novel examples? Explain in own words? Predict system behavior?

# divergent_implementation(id|step|action)
DI1|Establish starting context|What's known? What constraints exist? What's the utility function?
DI2|Identify available directions|What options possible from current state? What information helps evaluate them?
DI3|Explore highest-value path|Which direction promising per utility function? Implications? New options opened?
DI4|Reassess and iterate|From new position what's available? Continue or pivot? What updates evaluation?
DI5|Recognize convergence|Solution satisfying constraints found? Explored sufficiently for confidence? Further exploration likely to yield better?

# theory_connections(id|theory|connection)
TH1|Zone of Proximal Development (Vygotsky)|"You are here" assessment continuously identifies ZPD; method operates within it
TH2|Constructivist Learning Theory|Knowledge actively constructed by learner; practitioner facilitates by providing materials adapted to current cognitive structure
TH3|Bayesian Reasoning|Each response is evidence about interlocutor's mental model; practitioner updates belief about state; informs next delivery choice
TH4|State Space Search|Divergent mode resembles heuristic search through problem space; utility functions guide selection; path emerges from local optimization

# claims(id|claim|type|depends_on)
CL1|Optimal communication path depends on current comprehension state, not assumed progression|axiom|P1,P2
CL2|Method is not designed to control or manipulate but to efficiently navigate conceptual space|axiom|P5
CL3|Verification before progression prevents wasted effort on material interlocutor isn't ready to integrate|derivation|P3
CL4|Flexible communication modes (statements, questions, corrections, examples, silence) serve better than questions-only|derivation|P4,CT1
CL5|For complex topics, adaptive method often faster than direct explanation by preventing backtracking from foundational misunderstandings|observation|L1,P3
CL6|Conflict resolution often reveals disagreement was based on miscommunication, not genuine disagreement|observation|AP5
CL7|In divergent mode, solution emerges from collaborative exploration guided by utility function, not imposed by expert|derivation|C3,C6

# rules(id|rule|rationale)
R1|Assess before delivering; never advance without verification|Building on shaky foundation requires later backtracking; verification is cheaper than repair
R2|Deliver information only when interlocutor is ready to integrate it|Premature delivery wastes effort and may create misconceptions
R3|Use whatever communication form serves current need|Questions-only is artificial constraint; statements, corrections, examples, silence each serve specific states
R4|In convergent mode, close highest-priority gap first|Gap priority determines learning efficiency; prerequisites before extensions
R5|In divergent mode, let utility function guide path selection|Practitioner provides trade-off information at branch points; team's preferences determine direction
R6|When resistance appears, explore source before pushing through|Resistance may signal genuine disagreement, not confusion; different responses needed

# relationships(from|rel|to)
P1|defines|C1
P1|enables|P2
P2|depends_on|P1
P3|constrains|P2
P4|enables|P2
P5|defines|C8
C1|drives|AL3
C2|instance_of|C8
C3|instance_of|C8
C4|response_to|SI2
C5|response_to|SI4
C6|guides|C3
C7|implements|P3
SI1|triggers|RS1
SI2|triggers|RS2
SI3|triggers|RS3
SI4|triggers|RS4
M1|implemented_by|CI1,CI2,CI3,CI4,CI5
M2|implemented_by|DI1,DI2,DI3,DI4,DI5
CT1|contrasted_with|P4
CT2|contrasted_with|P2
TH1|grounds|P1
TH2|grounds|P2
TH3|models|AL3
TH4|models|C3
CL1|grounds|P1,P2
CL5|derives_from|P3
AP5|demonstrates|CL6

# section_index(section|title|ids)
1|Introduction|P5
2|Core Principles|P1,P2,P3,P4
3|Contrast With Classical Methods|CT1,CT2
4|Two Primary Modes|M1,M2,C2,C3
5|Convergent Example (Database Indexing)|M1
6|Divergent Example (Notification System)|M2,C6
7|Operational Mechanics|AL1-AL6,SI1-SI4,RS1-RS4
8|Applications|AP1,AP2,AP3,AP4,AP5
9|Comparison With Related Methods|CT3,CT4,CT5
10|Effectiveness Factors|RQ1-RQ6
11|Limitations|L1,L2,L3,L4
12|Theoretical Foundations|TH1,TH2,TH3,TH4
13|Practical Implementation|CI1-CI5,DI1-DI5
14|Teaching Recursion Example|M1,P1,P3,C4
15|Conclusion|CL1,CL5

# decode_legend
modes: convergent(toward destination)|divergent(explore solution space)
states: solid|gaps|confusion|resistance
responses: advance|backfill|clarify/reframe|explore_resistance
loop: deliver→observe→analyze→determine→execute→return
category_values: core|mode|operation
claim_types: axiom|derivation|observation
requirement_types: essential|helpful|minimal
context_fitness: works_well|works_poorly
rel_types: defines|enables|depends_on|constrains|drives|instance_of|response_to|guides|implements|triggers|implemented_by|contrasted_with|grounds|models|derives_from|demonstrates
+standalone: this doc self-contained
