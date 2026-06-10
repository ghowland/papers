# THE SIX STATES OF INFORMATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → cells → failure_modes → misclassifications → responses → transitions → maturity → disciplines → examples → relationships → sections

# principles(id|principle|rationale)
P1|Three intrinsic cardinalities|All information processing operates through Zero (referenced, inoperable), One (single unit of work), Infinity (multiplicity requiring reduction). Not design choices — intrinsic properties on any substrate
P2|Reduction pipeline|Information processing is reduction of Infinity to One, aspiring to Zero. Pipeline: enumerate, filter, score, select. Appears identically across all domains
P3|Manageability is binary|For any element at any moment: system either has operational access or does not. Can write or only read. Actions change it or they don't. Not a spectrum
P4|Six exhaustive cells|3 cardinalities × 2 manageability states = 6 cells. Every element occupies exactly one cell at any time. Nothing exists outside them
P5|Most failures are misclassification|Failures trace not to incompetence within correct cell but to placing element in wrong cell and applying wrong cell's response
P6|Maturity is dissolution trajectory|Operational maturity measured as distribution of elements across cells and accuracy of classification. Progress = dissolving elements toward Zero-by-absence

# cells(id|abbrev|cardinality|manageable|nature|correct_response|goal_state)
C1|M∞|Infinity|yes|Population of operable elements waiting for reduction|Reduce: enumerate, filter, score, select. Move toward One then Zero-by-absence|Dissolve to M0
C2|M1|One|yes|Single element currently being operated on|Execute: act, complete, release. Promote next from Infinity|Complete and release
C3|M0|Zero-by-absence|yes|Dissolved problem handled by structure|Leave alone: trust structure, verify dissolution is genuine|Maintain
C4|U∞|Infinity|no|Unbounded population system cannot control or enumerate|Make architecturally irrelevant: remove anatomy through which population could affect system|Structural irrelevance
C5|U1|One|no|Single dependency system can observe but not control|Build redundancy and contingency: prepare for both availability and loss|Structural resilience
C6|U0|Zero-by-externality|no|Permanent boundary system can never manage|Measure, approximate, build resilient responses. Accept permanence, engineer the response|Structural coping

# failure_modes(id|cell|name|description|symptom|root_cause)
F1|C1|Unreduced accumulation|Manageable population left at Infinity when reduction is possible|Growing backlogs, overwhelm, pipeline saturation|Failure to invest in reduction pipeline
F2|C2|Lingering|Holding element at One beyond completion|Gold-plating, micro-management, perfectionism|Failure to release completed work
F3|C2|Premature release|Releasing from One before work complete|Rework, regression, production defects|Impatience, pressure to show throughput
F4|C3|Regression to One|Re-introducing active management to dissolved problem|Unnecessary approvals, redundant oversight, wasted pipeline|Lack of trust in structure
F5|C3|Premature dissolution|Classifying as Zero when structure incomplete|Silent failures, edge case errors, false confidence|Incomplete automation, partial skill acquisition
F6|C4|Enumeration trap|Attempting to manage unmanageable Infinity through exhaustive listing|Perpetually incomplete coverage, resources consumed without convergence|Misclassification as manageable Infinity
F7|C5|Dependency illusion|Treating observation as control|False sense of security, catastrophic failure when dependency fails|Conflation of monitoring with management
F8|C5|Ignoring|Failing to prepare for dependency loss because it can't be controlled|Total system failure, no contingency|Fatalism, avoidance
F9|C6|Magical thinking|Searching for manageable cause of unmanageable boundary event|Wasted investigation, blame assignment, no improvement|Misclassification as manageable One
F10|C6|Fatalism|Treating response as unmanageable because boundary is|Inaction, no resilience, preventable damage|Conflation of boundary with response

# misclassifications(id|actual_cell|misclassified_as|name|description)
MC1|C1|C4|Learned helplessness|Treating reducible population as irreducible. Reduction pipeline needs investment, not abandonment
MC2|C6|C2|Control illusion|Treating permanent boundary as manageable element. Resources spent on attempted management are wasted
MC3|C3|C2|Trust failure|Re-introducing management to dissolved problem. Pipeline capacity freed by dissolution re-consumed
MC4|C2|C3|Premature dissolution|Declaring work complete when structure incomplete. Hidden One wearing Zero label
MC5|C4|C1|Enumeration trap|Attempting to enumerate unbounded population. Pipeline consumes resources without converging
MC6|C5|C2|Dependency illusion|Conflating observation with control. Seeing threat ≠ handling threat

# responses(id|cell|category|action|mechanism|end_state)
RS1|C1|Reduce|Enumerate, filter, score, select|Reduction pipeline|Element promoted to C2
RS2|C1|Automate|Build structural handlers for recurring patterns|Automation, pattern matching, rule engines|Recurring pattern dissolved to C3
RS3|C2|Execute|Act on element with full pipeline attention|Focused work, single-task processing|Work completed, element released
RS4|C2|Release|Demote completed element, promote next|Context switch, pipeline reallocation|Element moves to C3 or returns to C1
RS5|C3|Maintain|Verify dissolution genuine, do not re-introduce management|Periodic structural audit, not active oversight|Continued dissolution
RS6|C3|Trust|Resist urge to regress to active management|Organizational discipline, confidence in structure|Pipeline capacity preserved
RS7|C4|Architectural irrelevance|Remove anatomy through which population could affect system|Geometric Security, vocabulary restriction, structural constraints|Population rendered inexpressible
RS8|C4|Structural commitment|Choose response before Infinity manifests|Pre-computed reductions, default stances|Specific instances made beside the point
RS9|C5|Redundancy|Ensure no single unmanageable dependency is fatal|Multi-provider, alternate routes, diversification|Dependency loss survivable
RS10|C5|Contingency|Prepare response plans for both availability and loss|Runbooks, fallback procedures, pre-negotiated alternatives|Response pre-computed
RS11|C6|Measurement|Observe boundary effects with available instrumentation|Sensors, monitors, statistical sampling|Approximation of boundary state
RS12|C6|Resilience|Build structural responses to boundary effects|Redundancy, graceful degradation, capacity margins|Boundary events survivable
RS13|C6|Acceptance|Recognize permanence of boundary|Organizational and cognitive discipline|Effort directed to manageable responses

# transitions(id|from|to|name|mechanism|direction)
T1|C1|C2|Promotion|Reduction pipeline selects one element|Forward
T2|C2|C1|Demotion (incomplete)|Element released before work complete|Backward (rework risk)
T3|C2|C3|Dissolution|Completed work needs no further attention|Forward (goal state)
T4|C3|C2|Regression|Active management re-introduced|Backward (capacity waste)
T5|C1|C3|Full automation|Entire class dissolved without individual One-processing|Forward (ideal path)
T6|C4|C3|Architectural elimination|System restructured so unmanageable Infinity cannot affect it|Forward (Geometric Security)
T7|C6|C3|Boundary response automation|Response to permanent boundary dissolved into structure|Forward (resilience as structure)
T8|C5|C3|Redundancy dissolution|Contingency and redundancy built into structure|Forward (resilient architecture)
T9|C1|C4|Learned helplessness|System stops attempting reduction|Misclassification
T10|C6|C2|Control illusion|System attempts to manage permanent boundary|Misclassification
T11|C3|C2|Trust failure|System re-introduces management to dissolved problem|Misclassification
T12|C2|C3|Premature dissolution|System declares dissolved before structure complete|Misclassification
T13|C4|C1|Enumeration trap|System attempts to reduce unbounded population|Misclassification
T14|C5|C2|Dependency illusion|System conflates observation with control|Misclassification

# maturity(id|level|m_inf|m1|m0|u_classification|defining_characteristic)
MAT1|Immature|High: most elements unreduced|Scattered: pipeline thrashing|Low: few dissolved|Poor: confused across all unmanageable cells|Everything urgent, nothing dissolved
MAT2|Developing|Moderate: some being reduced|Focused: defined processes|Growing: some routine automated|Improving: some correctly identified|Processes exist but consume attention
MAT3|Mature|Low: most routine dissolved|Efficient: novel problems only|High: most routine structural|Accurate: architectural not enumerative responses|Pipeline free for novel challenges
MAT4|Wise|Minimal: only genuinely new|Precise: highest-leverage One|Comprehensive: verified not premature|Correct under pressure: classification holds during crisis|Classification accuracy maintained under pressure

# disciplines(id|discipline|primary_cell|core_activity)
D1|Operations|C1→C2→C3|Moving classes of work from active management to structural dissolution
D2|Automation|C2→C3|Converting active work into dormant structure
D3|Security|C4|Making unbounded uncontrollable threat populations architecturally irrelevant
D4|Resilience Engineering|C6|Building structural responses to permanent boundaries
D5|Risk Management|C5|Preparing for loss of singular uncontrollable dependencies
D6|Decision-Making|C1→C2|Reducing manageable Infinity to manageable One via pipeline
D7|Capacity Planning|C6+C1|Sizing resources against uncontrollable demand and manageable fleet
D8|Incident Response|C6→C2|Promoting boundary event effects to manageable One
D9|Monitoring|C6+C5|Observing unmanageable elements to inform manageable responses
D10|Project Management|C1→C2→C3|Converting backlog into completed deliverables
D11|Training/Education|C1→C2→C3|Converting unknown skills into unconscious competence
D12|Quality Assurance|C1+C4|Reducing manageable test cases, making untestable space irrelevant
D13|Strategic Planning|C5+C4+C1|Classifying dependencies, building resilience, reducing actionable items

# decision_tree(step|question|yes|no)
DT1|Can your actions change this element?|Manageable → DT2|Unmanageable → DT5
DT2|More than one instance requiring attention?|C1 (M∞)|→ DT3
DT3|Currently receiving active attention and work?|C2 (M1)|→ DT4
DT4|Requires no attention because structure handles it?|C3 (M0)|Revisit DT2: likely C1 with one member
DT5|Multiple instances/variants you cannot control?|C4 (U∞)|→ DT6
DT6|Single identifiable dependency, observable not controllable?|C5 (U1)|→ DT7
DT7|Permanent physical/temporal/systemic boundary no effort changes?|C6 (U0)|Revisit DT1: reassess manageability

# historical_transitions(id|era|element|from|to|mechanism)
HT1|Pre-alphabet|Written vocabulary|C1|C3|Alphabet reduced infinity of logograms to ~26 composable letters
HT2|Pre-numerals|Arithmetic methods|C1|C3|Positional notation with zero dissolved per-scale procedures
HT3|Pre-plumbing|Household water procurement|C1|C3|Municipal water systems dissolved daily water-fetching
HT4|Pre-sewage|Household waste disposal|C1|C3|Municipal sewage dissolved daily waste management
HT5|Pre-refrigeration|Food preservation|C1|C3|Mechanical refrigeration dissolved salting/smoking/pickling
HT6|Pre-interchangeable parts|Weapon repair|C2|C3|Standardized parts dissolved hand-fitting
HT7|Pre-automatic transmission|Gear selection|C2|C3|Automatic transmission dissolved conscious gear management
HT8|Pre-GPS|Route navigation|C2|C3|GPS dissolved map-reading as active cognitive task
HT9|Pre-elevator automation|Vertical transport|C2|C3|Automatic elevators dissolved elevator operator occupation
HT10|Pre-containerization|Cargo handling|C1|C3|Standardized container dissolved per-item handling procedures
HT11|Pre-germ theory|Disease explanations|C1 misclassified C4|C1 correct|Germ theory made disease manageable Infinity with unifying mechanism
HT12|Pre-Newton|Terrestrial/celestial motion|C1 (two separate)|C1 (one, one law)|Universal gravitation unified two populations under one equation
HT13|Pre-time zones|Cross-location time coordination|C1|C3|Standard time zones dissolved active time-conversion
HT14|1930s dust bowl|Plains climate variability|C6 misclassified stable|C6 correctly classified, too late|Drought revealed climate was unmanageable boundary
HT15|Autonomous driving|Vehicle control input|C6 (driver as externality)|C2 (system-managed)|Driver transitioning from Zero-by-externality to system-managed One

# domain_examples(id|cell|domain|element|description)
DE1|C1|Kitchen|Dirty dishes after party|Population of messes, each accessible and cleanable
DE2|C1|Operations|Alert queue|Population of alerts, each investigable
DE3|C1|Air traffic|Radar contacts|Population of aircraft, continuously reduced
DE4|C1|Education|Untaught curriculum|Population of topics, each learnable
DE5|C1|Medicine|ED waiting room|Population of patients awaiting triage
DE6|C2|Locksmithing|Current pin being set|Single element under direct operation
DE7|C2|Surgery|Current patient on table|Single patient, all pipeline allocated
DE8|C2|Software|Function being written|Single unit under active development
DE9|C2|Conversation|Current sentence spoken|Single thought, full conscious pipeline
DE10|C2|Cooking|Onion being diced|Single ingredient under knife
DE11|C3|Household|Working plumbing|Water/waste handled structurally
DE12|C3|Driving|Lane keeping familiar road|Dissolved to unconscious competence
DE13|C3|Operations|Automated cert renewal|Renews without human involvement
DE14|C3|Civilization|Clean water infrastructure|Water procurement dissolved structurally
DE15|C3|Manufacturing|Interchangeable parts|Hand-fitting dissolved by standardization
DE16|C4|Security|All possible cyberattacks|Unbounded, unenumerable, self-modifying
DE17|C4|Business|All possible competitor moves|Unbounded competitive landscape
DE18|C4|Sports|All possible penalty kick placements|Effectively infinite, unenumerable in time
DE19|C4|Anxiety|All possible future misfortunes|Unbounded, self-generating
DE20|C4|Legal|All possible lawsuits|Unbounded litigation exposure
DE21|C5|Sailing|The wind|Perfectly observable, completely uncontrollable
DE22|C5|Startup|Single large customer|Observable satisfaction, uncontrollable decisions
DE23|C5|Medicine|Pending biopsy result|Binary outcome, fully determined, outside control
DE24|C5|Operations|Single cloud provider|Observable status, uncontrollable reliability
DE25|C5|Commuting|Single bridge on route|Observable, uncontrollable closures
DE26|C6|Farming|Weather/precipitation|Permanent physical boundary
DE27|C6|Computing|Speed of light (latency)|Defines minimum latency between locations
DE28|C6|Operations|Hardware degradation|Disks fail on physics' schedule
DE29|C6|Biology|Aging|Manageable responses but unmanageable boundary
DE30|C6|Operations|Monitoring data aging|All measurements of past, never present

# key_claims(id|claim|type)
KC1|Flow state is sustained uninterrupted manageable One — pipeline running smoothly, no competing promotions|reframe
KC2|Overwhelm is not about amount of work but about unreduced Infinity. Picking one item shifts cardinality and dissolves overwhelm|reframe
KC3|Observation and control are different operations. Dashboards show failure happening, do not prevent it|distinction
KC4|A problem has a solution. A boundary has a response|distinction
KC5|Premature Zero-by-absence is a hidden One wearing a Zero label|axiom
KC6|Unmanageable does not mean ignorable. Cannot change the thing but can change response to the thing|axiom
KC7|Adding more enumeration effort to unmanageable Infinity does not proportionally improve outcomes — practical test for unmanageability|observation
KC8|When unmanageable One fails, blast radius is total — no population to absorb loss|derivation
KC9|Wisdom is accuracy of classification under pressure|definition
KC10|The six cells unify security, operations, resilience, risk, automation, and decision-making as one coordinate system|axiom

# relationships(from|rel|to)
P1|grounds|P4
P2|implements|P1
P3|grounds|P4
P4|derives_from|P1,P3
P5|derives_from|P4
P6|derives_from|P4
C1|reduces_to|C2
C2|dissolves_to|C3
C1|dissolves_to|C3
C4|eliminates_to|C3
C5|dissolves_to|C3
C6|dissolves_to|C3
P2|operates_on|C1
F1|symptom_of|C1
F2|symptom_of|C2
F3|symptom_of|C2
F4|symptom_of|C3
F5|symptom_of|C3
F6|symptom_of|C4
F7|symptom_of|C5
F8|symptom_of|C5
F9|symptom_of|C6
F10|symptom_of|C6
MC1|misclassifies|C1 as C4
MC2|misclassifies|C6 as C2
MC3|misclassifies|C3 as C2
MC4|misclassifies|C2 as C3
MC5|misclassifies|C4 as C1
MC6|misclassifies|C5 as C2
RS7|implements|KC3
KC1|reframes|C2
KC2|reframes|C1
KC4|distinguishes|C6 from C2
KC5|defines|F5
KC8|distinguishes|C5 from C1
KC9|defines|MAT4
KC10|unifies|D1-D13
D3|references|RS7

# section_index(section|title|ids)
1|Two Properties, Six States|P1,P2,P3,P4,P5
2|Manageable Infinity|C1,F1,KC2
3|Manageable One|C2,F2,F3,KC1
4|Manageable Zero-by-Absence|C3,F4,F5,KC5
5|Unmanageable Infinity|C4,F6,KC7
6|Unmanageable One|C5,F7,F8,KC3,KC6,KC8
7|Unmanageable Zero-by-Externality|C6,F9,F10,KC4
8|Misclassification|MC1-MC6
9|Maturity Progression|MAT1-MAT4,P6,KC9
10|Implications|D1-D13,KC10
A|Table A: Six-Cell Grid|C1-C6
B|Table B: Failure Modes|F1-F10
C|Table C: Misclassification Patterns|MC1-MC6
D|Table D: Correct Responses|RS1-RS13
E|Table E: Cell Transitions|T1-T14
F|Table F: Domain Examples|DE1-DE30
G|Table G: Unified Discipline Mapping|D1-D13
H|Table H: Maturity Assessment|MAT1-MAT4
I|Table I: Decision Tree|DT1-DT7
J|Table J: Historical Transitions|HT1-HT15
K|Table K: Specification Summary|—

# decode_legend
cardinality_values: Zero|One|Infinity
manageability_values: yes (manageable)|no (unmanageable)
cell_abbrevs: M∞=manageable Infinity|M1=manageable One|M0=manageable Zero-by-absence|U∞=unmanageable Infinity|U1=unmanageable One|U0=unmanageable Zero-by-externality
claim_types: axiom|derivation|observation|prescription|reframe|distinction|definition
transition_directions: Forward (progress)|Backward (rework/waste)|Misclassification (failure)
rel_types: grounds|implements|derives_from|reduces_to|dissolves_to|eliminates_to|operates_on|symptom_of|misclassifies|reframes|distinguishes|defines|unifies|references
maturity_levels: Immature|Developing|Mature|Wise
id_prefixes: P=principle|C=cell|F=failure_mode|MC=misclassification|RS=response|T=transition|MAT=maturity|D=discipline|DT=decision_tree_step|HT=historical_transition|DE=domain_example|KC=key_claim
spec_counts: 3 cardinalities|2 manageability values|6 cells|10 failure modes|6 misclassifications|13 response categories|8 forward transitions|6 misclassification transitions|4 maturity levels|13 disciplines|30 domain examples|15 historical transitions|7 decision tree steps|10 key claims
