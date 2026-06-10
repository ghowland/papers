# THE RELATIONSHIP OF ZERO, ONE, AND INFINITY IN INFORMATION PROCESSING — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → cardinalities → interaction_patterns → violations → transitions → domains → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Three cardinalities are intrinsic properties of information processing, not organizational tools|Any system processing information must contend with Zero (unreachable), One (unit of work), Infinity (multiplicity requiring reduction); these have fixed natures regardless of domain or substrate
P2|One is the only cardinality at which work occurs|Zero and Infinity defined in relation to One; Zero cannot become One, Infinity must become One before operation; One is center, others describe relationship to center
P3|Infinity is repetition of One|Population has no computational nature independent of members; cannot be operated on "as a population" without reduction through iteration, aggregation, filtering, or abstraction to One
P4|Zero is the boundary of what can become One|Zero entities emit events into system but cannot receive operations; temporal or structural impossibility, not design choice
P5|Interaction patterns are determined mechanically by cardinalities involved|Follow from natures of cardinalities, not design decisions
P6|Unreliable Zero dependencies create decision points|Each dimension of unreliability in unmanaged dependency forces scored evaluation (behavior set) into existence
P7|Cardinality violations produce domain-specific hard problems|Infinity members acting as One without coordination produces consensus, deadlock, bullwhip, split-brain — always with proportional resolution cost
P8|Zero-to-One transitions are architectural phase changes|Redefines system boundary, identity, and relationship to environment; not incremental feature addition

# concepts(id|name|category|definition)
C1|Cardinality One|cardinality|Exactly one instance for system lifetime; singleton; the only mode at which actual work occurs
C2|Cardinality Infinity|cardinality|Population of instances created/destroyed dynamically; must be reduced to One before operation
C3|Cardinality Zero|cardinality|System references concept but has no runtime representation; emits events, cannot receive operations; outside operational boundary
C4|Permanent One|core|Singleton existing from system initialization to shutdown; has population-level visibility; source of iteration that makes Infinity computable
C5|Temporary One|core|Infinity member promoted for duration of an operation; data loaded, state read/modified, subject of computation; bounded promotion then return to population
C6|Temporary One promotion|operation|Loading Infinity member's data into operational focus (registers, conscious attention, variable binding); concrete physical act not metaphor
C7|Population-level visibility|core|Ability to read from population, compare across members, make decisions affecting group; defining characteristic of One; Infinity member acquiring this has become defacto One
C8|Behavior set|core|Scored evaluation of multiple possible actions using weighted considerations; forced into existence by unreliable Zero dependency; CLA's mechanism for non-deterministic decisions
C9|Constraint filtering|mechanism|How One relates to Infinity — specifies properties member must have, runtime resolves which member matches; CLA's fourth list is the promotion mechanism
C10|Fan-out|interaction_pattern|One to Infinity: iterate, promote each matching member to temporary One, operate, demote
C11|Convergence|interaction_pattern|Infinity to One: each member contributes partial result, accumulated into one aggregate that permanent One operates on
C12|Mutual constraint filtering|interaction_pattern|Infinity to Infinity: nested iteration, both sides filtered by constraint to identify participating members
C13|One-way event injection|interaction_pattern|Zero to anything: events flow from Zero into system, no events flow back
C14|Peer handoff|interaction_pattern|One to One: sequential phase completion enabling next singleton; peers, not orchestrator/subordinate
C15|Pure sequencing|interaction_pattern|Zero to Zero: ordering only, no entity data read or written
C16|Cardinality violation|core|System's actual behavior contradicts cardinality declaration; produces resolution costs proportional to number of violating members
C17|Defacto One|violation|Infinity member that has acquired population-level visibility and makes decisions affecting other members; undeclared singleton
C18|Zero-to-One transition|core|Previously unmanaged external dependency becomes internally managed; redefines system boundary; most fundamental architectural transformation
C19|One-to-Zero transition|core|Previously managed internal capability extracted to unmanaged external dependency; microservice extraction pattern
C20|Cardinality thrash|failure_mode|N Infinity members competing for One-ness without coordination; oscillation, overhead, consensus cost

# cardinalities(id|cardinality|nature|can_emit_events|can_receive_operations|population_visibility|computational_role)
K1|Zero|Outside operational boundary|yes|no|n/a|Boundary; source of initial events; defines system character; coping with Zero is what system exists to do
K2|One|Unit of work|yes|yes|yes — reads from Infinity populations|Center; orchestration; iteration source; all work occurs here
K3|Infinity|Repetition of One|yes (as temporary One)|yes (when promoted to temporary One)|no — only self-scoped|Population; source from which members drawn for evaluation; passive until promoted

# interaction_patterns(id|from|to|pattern|mechanism|examples)
IP1|One|Infinity|Fan-out|Iterate: for each matching member, promote to temporary One, operate, demote|OS init starting services; TCP checking segments for retransmission; ECU calculating per-cylinder injection
IP2|Infinity|One|Convergence|Each member temporarily promoted, data extracted, aggregated into single value One operates on|Init waiting for all mounts; TCP reassembling segments; definite integral F(b)-F(a)
IP3|Infinity|Infinity|Mutual constraint filtering|Nested iteration: for each match in A, for each match in B, one operation on pair|Device-to-service mapping; process creating pipe from pool
IP4|Zero|any|One-way event injection|Event flows from Zero into system; no event flows back|BIOS emits POST; remote host emits SYN; driver presses brake; training corpus emitted examples
IP5|One|One|Peer handoff|One completes phase, enables other to begin; sequential, not orchestration|Kernel root switch enables Init; Init DNS config enables Display Server
IP6|Zero|Zero|Pure sequencing|Prior event completed is only possible constraint; no entity data|BIOS transfers control to Bootloader

# zero_properties(id|property|explanation)
Z1|Can only emit events, never receive them|Outside operational boundary; system cannot cause things to happen to Zero entities
Z2|Thinnest constraints|Often just "true" or "previous event completed" because no entity data to query
Z3|Source of initial events|Every system begins with unconstrainable event from Zero group; system cannot cause its own starting condition
Z4|Defines system character|Coping with what cannot be controlled is what the system exists to do
Z5|Each unreliable dimension forces a behavior set|Unpredictable input prevents deterministic response; scored evaluation required

# violation_consequences(id|violation|domain|manifestation|resolution_mechanism|cost)
V1|N nodes each acting as One in peer network|Distributed systems|Consensus problem; competing orchestration with no coordination|Raft, Paxos, PBFT — elect which Infinity member gets to be One per decision round|Message overhead, latency, leadership election, split-brain risk
V2|Mining/validating nodes each acting as One|Blockchain|N entities competing for right to be One|Proof of work, proof of stake|Energy expenditure proportional to competition; deliberately expensive for unambiguous resolution
V3|Two threads promoting same resource to temporary One|Concurrent programming|Race condition|Mutex serializes promotions; lock-free algorithms|Lock contention, deadlock risk, algorithm complexity
V4|Supply chain nodes making independent inventory decisions|Logistics|Bullwhip effect — small demand fluctuations amplify upstream|Vendor-managed inventory, demand signal sharing, collaborative planning|Inventory oscillation, waste, stockouts
V5|Designated One fails|High availability|System must promote Infinity member to One|Leader election; temporarily re-introduces violation|Unavailability during election; bounded-cost resolution engineering

# zero_to_one_transitions(id|domain|what_transitions|from_state|to_state|architectural_consequence)
T1|Automotive|Driver|Zero (car receives steering/throttle/brake as external events)|One (car manages driving function internally)|Entire flow structure changes; one-way reception becomes closed loop perceive-plan-act-perceive
T2|Computing|Server infrastructure|Zero (application connects but doesn't manage)|One (application provisions, scales, manages infrastructure)|Client-server to cloud computing
T3|Web|Content|Zero (server serves fixed files)|One (application generates content dynamically)|Static pages to web applications
T4|Languages|Grammar|Zero (compiler implements fixed language definition)|One (workbench manages grammar as mutable runtime entity)|Compiled languages to language workbenches
T5|Databases|Database Engine|Zero (application connects to external server)|One (application contains and manages storage engine)|Traditional to embedded databases
T6|Architecture|Monolith component|One (managed internally)|Zero (external service, referenced but not managed)|One-to-Zero: microservice extraction; gained independence, lost direct management

# domains(id|domain|zero_groups|one_groups|infinity_groups|behavior_sets|notes)
D1|Operating system|BIOS, Bootloader|Kernel, Init, Memory Manager, Scheduler + 11 others (15 total)|Processes, Threads, Pages, Files + 16 others (20 total)|~9 (resource pressure responses)|9 autonomous decision points of 37 entity groups
D2|TCP|Remote Host, Network Medium, Application Layer|TCP Stack|Segments, Connections|5+ (congestion control, RTO, receive window, delayed ACK, Nagle)|Network medium has multiple unreliability dimensions (loss, reorder, duplicate, corrupt, delay)
D3|Automobile|Driver, Road Surface, Weather|ECU|Cylinders, Sensors|6-8 (ABS, traction control, etc.)|Three unreliable Zero groups
D4|LLM token prediction|Training Corpus, Human Intent, Language Rules|Attention Mechanism|Attention Heads, Tokens|1 (sampling strategy); at temperature 0 collapses to deterministic argmax|Zero unreliability absorbed into weights during training
D5|Navicat database GUI|Database Server, User|Application|Queries, Results|~3|Fewest behavior sets; Database Server relatively reliable; User unreliability is sequencing not data
D6|Hospital|Disease, Patient Arrival patterns|Hospital Administration|Patients, Doctors, Beds|Triage, ED staffing, antibiotic selection, bed management|Bed management structurally identical to OS memory manager
D7|Classroom|Curriculum, Student comprehension|Teacher|Students|Pacing, classroom management, reteaching decisions|Behavior sets at unreliable Zero dependencies (student understanding unpredictable)
D8|Supply chain|Customer Demand, Supplier internals|Logistics Coordinator/Warehouse|Shipments, Inventory|Inventory management (reorder, expedite, discount, write-off)|Pressure response structurally identical to OS memory manager
D9|Calculus|Theorems (Fundamental Theorem, power rule)|Integrand function|Infinitesimal slices (dx)|n/a|Fan-out (One to Infinity slices) then convergence (accumulate to One sum); differentiation/integration are inverse fan-out/convergence

# claims(id|claim|type|depends_on)
CL1|Three cardinalities are intrinsic properties of information processing, not architectural tools|axiom|P1
CL2|One is not a cardinality among peers; it is the center, the other two describe relationship to center|axiom|P2
CL3|Infinity as computational concept is One with a loop around it|derivation|P3,C5,C10
CL4|Passivity of Infinity populations is consequence of what Infinity is, not a design pattern|derivation|P3,C7
CL5|A member that acquires population-level visibility has become One whether or not specification acknowledges this|derivation|C7,C17
CL6|Entire execution of any system is permanent One generating stream of temporary Ones from Infinity populations|derivation|P2,C4,C5
CL7|Zero defines system character more than any other cardinality; coping with uncontrollable is what system exists to do|axiom|P4,Z4
CL8|Number and character of behavior sets predictable from unreliable Zero dependencies|derivation|P6,C8
CL9|When Infinity member violates nature by assuming One-ness, system must pay resolution cost proportional to number of simultaneous claimants|derivation|P7,C16
CL10|Leader-based architectures simpler and faster than peer-based because they align runtime with cardinality natures|derivation|P7,C4,C17
CL11|Every security mechanism is a constraint on events from Zero-cardinality groups|derivation|P4,Z1
CL12|Ignoring cardinalities does not eliminate them; it produces the specific classes of problems each domain considers hardest|axiom|P1,P7
CL13|No domain-specific training required to identify these properties; procedure is mechanical|observation|P1,P5
CL14|Context switching cost is cost of transferring physical state of One-ness from one entity to another|derivation|C4,C5,C6
CL15|Cache locality is hardware manifestation of temporary One promotion; optimized for assumption next promotion is near previous|derivation|C6
CL16|Locking and concurrency control are mechanisms for serializing conflicting promotions to temporary One|derivation|C6,V3
CL17|High availability is engineering of rapid bounded-cost cardinality violation resolution when permanent One fails|derivation|V5,P7

# rules(id|rule|rationale)
R1|Enumerate Zero groups to enumerate attack surface|Every security mechanism constrains Zero events; gap in constraints = unprotected boundary
R2|Count behavior sets against unreliable Zero dependency dimensions|Fewer = missing decision point (handling unpredictable input deterministically); more = unnecessary complexity
R3|Distinguish permanent One from temporary One for concurrency clarity|Permanent Ones are coordination points; temporary One promotions are contention points
R4|Identify Infinity members acting as defacto One|Predicts where coordination costs concentrate; enables targeted resolution mechanism design
R5|Prefer designated One (leader) over peer competition when viable|Aligns runtime with cardinality natures; avoids violation resolution costs; tradeoff is single point of failure
R6|Recognize Zero-to-One transitions as boundary redefinitions|Not incremental; requires reconsidering every flow/constraint referencing formerly-Zero group

# relationships(from|rel|to)
P1|defines|K1,K2,K3
P2|defines|C1,C4,C5
P3|defines|C2
P4|defines|C3
P5|determines|IP1,IP2,IP3,IP4,IP5,IP6
P6|derives_from|Z5,C8
P7|derives_from|C16,C17
P8|defines|T1,T2,T3,T4,T5,T6
C1|instance_of|K2
C2|instance_of|K3
C3|instance_of|K1
C4|subtype_of|C1
C5|subtype_of|C1
C5|promoted_from|C2
C6|mechanism_for|C5
C7|defining_property_of|C4
C7|violation_when_acquired_by|C2
C8|caused_by|Z5
C9|mechanism_for|C6
C10|pattern_of|IP1
C11|pattern_of|IP2
C12|pattern_of|IP3
C13|pattern_of|IP4
C14|pattern_of|IP5
C15|pattern_of|IP6
C16|produces|C20
C17|instance_of|C16
C18|redefines|system_boundary
C19|inverse_of|C18
K1|emits_events_to|K2
K2|iterates_over|K3
K3|reduced_to|K2
V1|instance_of|C16
V2|instance_of|C16
V3|instance_of|C16
V4|instance_of|C16
V5|consequence_of|C4
CL3|derives_from|P3
CL6|derives_from|P2,C4,C5
CL8|derives_from|P6
CL9|derives_from|P7
CL10|derives_from|CL9
CL11|derives_from|P4
CL14|explains|context_switching
CL15|explains|cache_locality
CL16|explains|concurrency_control
CL17|explains|high_availability
R1|implements|CL11
R2|implements|CL8
R3|implements|CL6
R4|implements|CL9
R5|implements|CL10
R6|implements|P8

# section_index(section|title|ids)
1|The Three Cardinalities|P1,K1,K2,K3,CL1,CL12
2|One Is the Unit of Work|P2,C1,C4,C5,C6,CL2,CL6
3|Infinity Is Repetition of One|P3,C2,C5,C7,C10,C11,C12,CL3,CL4
4|Permanent One and Temporary One|C4,C5,C6,C7,C9,CL6,CL14,CL15,CL16
5|Zero Is the Boundary|P4,C3,Z1,Z2,Z3,Z4,CL7
6|The Fixed Interaction Patterns|P5,IP1,IP2,IP3,IP4,IP5,IP6
7|Unreliable Zero Creates Decision Points|P6,C8,Z5,CL8,R2
8|The Cardinality Violation Principle|P7,C16,C17,C20,V1,V2,V3,V4,V5,CL9,CL10,CL17,R4,R5
9|Zero-to-One Transitions|P8,C18,C19,T1,T2,T3,T4,T5,T6,R6
10|Cross-Domain Universality|D1,D2,D3,D4,D5,D6,D7,D8,D9,CL13
11|Implications|R1,R2,R3,R4,R5,CL11

# decode_legend
cardinalities: Zero|One|Infinity
cardinality_natures: Zero=boundary(emit-only)|One=unit-of-work(population-visible)|Infinity=repetition(passive-until-promoted)
one_subtypes: permanent(system-lifetime singleton)|temporary(promoted Infinity member, bounded duration)
interaction_patterns: fan-out|convergence|mutual_constraint_filtering|one-way_event_injection|peer_handoff|pure_sequencing
violation_types: Infinity-acting-as-One|conflicting-temporary-One-promotions|designated-One-failure
transition_types: Zero-to-One(boundary-moves-inward)|One-to-Zero(boundary-moves-outward)
behavior_set: scored evaluation of alternatives forced by unreliable Zero dependency; CLA mechanism
claim_types: axiom|derivation|observation
rel_types: defines|determines|derives_from|instance_of|subtype_of|promoted_from|mechanism_for|defining_property_of|violation_when_acquired_by|caused_by|pattern_of|produces|inverse_of|redefines|consequence_of|emits_events_to|iterates_over|reduced_to|explains|implements
CLA_ref: Closed Loop Architecture from [@HOWL-COMP-12-2026] (not cross-referenced; noted for provenance only)
+standalone: this doc self-contained
