# CLOSED LOOP ARCHITECTURE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → four_lists → cardinality → execution → entity_groups → behavior_sets → insights → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|System specified by four flat lists: EntityGroups, EventSets, EventFlows, EventConstraints|Union of four lists is complete system; no partial views, no diagrams, no projections; readable in afternoon
P2|Specification closed under addition|Adding new component = adding entries to four lists; existing entries unchanged; blast radius bounded to new entries
P3|Cardinalities (Zero/One/Infinity) determine interaction patterns mechanically|Not design decisions; consequences of what the cardinalities are; fan-out, convergence, list-to-list follow automatically
P4|Every behavior traceable through four lists; every gap visible by inspection|EntityGroup with no events = no lifecycle; event with no flows = disconnected; event with no constraint = fires unconditionally
P5|Slicing by what system contains, not by view type|No structural/behavioral/data projections; each list complete from own angle; one artifact per question (what exists, what happens, in what order, under what conditions)

# concepts(id|name|category|definition)
C1|EntityGroup|list_1|Every noun in system with cardinality (Zero/One/Infinity); system's ontology
C2|EventSet|list_2|Every verb tied to owning EntityGroup; carries custom data; group's events = its lifecycle
C3|EventFlow|list_3|Ordering relationships between events; linear, branching, parallel, fan-out, convergence, cyclic; complete behavior
C4|EventConstraint|list_4|Logical conditions evaluated against entity data gating each event; Zero groups test event completion only; One groups query own + cross-group data; Infinity groups bind Self
C5|Cardinality Zero|cardinality|System references concept but no runtime entity; named for specification completeness; can only emit events, never receive operations; defines boundary of what system manages
C6|Cardinality One|cardinality|Exactly one instance for system lifetime; singleton; orchestrator with population-level visibility
C7|Cardinality Infinity|cardinality|Population; members created/destroyed dynamically; passive — all transitions driven by events from singletons or other populations
C8|Behavior set|core|Scored evaluation of multiple actions using utility AI; considerations with inputs normalized [0,1], shaped by curves, weighted, multiplied; zero kills behavior score (hard gate)
C9|Force action|core|Deterministic: state dictates exactly one action; no decision-making; 28 of 37 OS EntityGroups are entirely force_action
C10|Envelope|execution|Time-bounded modifier on entity data; ADSR curve; three event hooks (start, per-frame, end) feeding back into system
C11|Closed loop|execution|Data → evaluation → decision → action → data change → evaluation; both paths (per-entity update, system orchestration) read through same logical evaluation, write through envelopes or direct modification, produce events

# four_lists(id|list|question_answered|entry_shape|completeness_check)
L1|EntityGroups|What exists?|Name + cardinality (Zero/One/Infinity)|Every concept in requirements appears as group; verb without noun = missing group
L2|EventSets|What happens?|Event name + owning group + custom data|Every group has events; every requirement verb appears as event; two events always firing together = one event
L3|EventFlows|In what order?|From event → to event + flow type|Every event in at least one flow; path exists from start to every event; unreachable = error or external entry point
L4|EventConstraints|Under what conditions?|Event + logical conditions on entity data|Every event has constraint; references to nonexistent entity fields = incomplete entity model

# cardinality_interactions(id|from|to|pattern|mechanism|example)
CI1|One|Infinity|Fan-out|Singleton event triggers events on N population members via constraint filtering|Init runlevel determined → Service Start Requested for each service in runlevel
CI2|Infinity|One|Convergence|Specific population member reports to singleton via constraint|Device[root_disk] ready → Kernel Root Filesystem Mounted
CI3|Infinity|Infinity|List-to-list|Both sides filtered by constraint; nested iteration|Device ready triggers corresponding Service start
CI4|Zero|any|Pure event sequencing|No entity data to query; only "did previous event complete?"|BIOS Bootloader Transferred → Bootloader Stage1 Loaded
CI5|One|One|Peer handoff|Sequential phase completion between singletons|Kernel Root Switched → Init Process Started
CI6|Zero|Zero|Ordering only|No entity data on either side|BIOS events in sequence

# execution_paths(id|path|description)
EP1|Per-entity update (Path A)|State machine evaluates transitions via logical rules against entity data → new state → force_action or behavior set (utility AI) → winning behavior → action → skill chain → envelopes → entity data modified → events produced → loop
EP2|System orchestration (Path B)|Events fire when constraints pass → flows determine next events → events carry custom data → trigger state transitions, create envelopes, spawn entities, modify state → loop

# os_entity_groups(id|name|cardinality|events|behavior_set|notes)
G1|BIOS|Zero|5|—|Pre-OS; no runtime entity
G2|Bootloader|Zero|7|—|Pre-OS; no runtime entity
G3|Kernel|One|13|—|force_action; 7 states; Unloaded→Panic
G4|Init System|One|15|—|force_action; 8 states; orchestrates boot
G5|Memory Manager|One|11|MemoryPressureResponse|5 behaviors: DoNothing/Compact/Reclaim/SwapOut/OOM
G6|Scheduler|One|8|SchedulingDecision|5 behaviors: Continue/Preempt/Rebalance/Migrate/AdjustPriority
G7|VFS|One|8|—|force_action
G8|Network Stack|One|8|CongestionResponse|4 behaviors: ReduceWindow/DropLowPriority/RetransmitCritical/Reset
G9|Display Server|One|8|—|force_action
G10|Audio Mixer|One|8|—|force_action
G11|Device Manager|One|8|—|force_action
G12|Swap Manager|One|8|SwapPressureResponse|4 behaviors: DoNothing/Defragment/AlertMemMgr/Deactivate
G13|Firewall|One|6|—|force_action
G14|DNS Resolver|One|7|—|force_action
G15|Session Manager|One|8|—|force_action
G16|System Logger|One|7|LogPressureResponse|4 behaviors: DoNothing/Flush/Rotate/Forward
G17|Package Manager|One|7|—|force_action
G18|Process|Infinity|16|—|force_action; Created→Terminated lifecycle
G19|Thread|Infinity|11|—|force_action
G20|File|Infinity|9|—|force_action
G21|Filesystem Mount|Infinity|9|—|force_action
G22|Network Connection|Infinity|12|ConnectionHealth|5 behaviors: DoNothing/ReduceWindow/Retransmit/Close/Reset
G23|User Account|Infinity|8|—|force_action
G24|User Session|Infinity|14|SessionIdleResponse|4 behaviors: DoNothing/Dim/Lock/Suspend (only user-facing behavior set)
G25|Device|Infinity|12|DeviceErrorRecovery|4 behaviors: Reset/Suspend/Remove/EscalateToKernel
G26|Kernel Module|Infinity|6|—|force_action
G27|Service|Infinity|14|ServiceHealthMonitor|5 behaviors: DoNothing/Reload/Restart/Escalate/Stop
G28|Window|Infinity|11|—|force_action
G29|Network Interface|Infinity|9|—|force_action
G30|Permission Rule|Infinity|4|—|force_action
G31|Timer|Infinity|4|—|force_action
G32|Signal|Infinity|5|—|force_action
G33|Pipe|Infinity|6|—|force_action
G34|Shared Memory Region|Infinity|5|—|force_action
G35|Environment Variable Set|Infinity|4|—|force_action
G36|Cron Job|Infinity|5|—|force_action
G37|Log Entry|Infinity|5|—|force_action
# Summary: 2 Zero, 15 One, 20 Infinity = 37 total

# behavior_sets(id|group|name|type|consideration_count|behavior_count|considerations_summary)
BS1|G5|MemoryPressureResponse|pressure|4|5|FreePageRatio(InverseLinear), SwapUsageRatio(Quadratic), AllocationFailureRate(Exponential), PageFaultRate(Linear)
BS2|G6|SchedulingDecision|resource|5|5|RunQueueLength(Linear), CPULoadImbalance(Quadratic), TimeSlice(Linear), InteractiveWaiting(Step), RealTimePending(Step)
BS3|G8|CongestionResponse|pressure|4|4|PacketDropRate(Exponential), RetransmitRate(Quadratic), BufferOccupancy(Linear), ActiveConnections(Linear)
BS4|G12|SwapPressureResponse|pressure|4|4|SwapUsageRatio(Quadratic), SwapIORate(Exponential), FreeSwapPages(InverseLinear), MemoryPressureLevel(Linear)
BS5|G16|LogPressureResponse|pressure|4|4|BufferOccupancy(Quadratic), LogRate(Linear), DiskSpaceRemaining(InverseLinear), CriticalEntryPending(Step)
BS6|G22|ConnectionHealth|pressure|4|5|RTT(Quadratic), PacketLossRate(Exponential), WindowUtilization(Linear), IdleTime(Linear)
BS7|G24|SessionIdleResponse|user-facing|4|4|IdleTime(Linear), BatteryLevel(InverseLinear), ActiveProcessCount(Linear), UnsavedWork(Step)
BS8|G27|ServiceHealthMonitor|health|5|5|HealthCheckResult(Step), MemoryUsage(Quadratic), CPUUsage(Linear), RestartCount(Exponential), DependencyHealth(Step)
BS9|G25|DeviceErrorRecovery|recovery|4|4|ErrorCount(Linear), ErrorRate(Exponential), TimeSinceLastReset(InverseLinear), DeviceCriticality(Step)
# Total: 38 considerations, 41 behaviors across 9 behavior sets

# specification_summary
# EntityGroups: 37 (2 Zero + 15 One + 20 Infinity)
# Events: 311
# Flows: 349 (291 intra-group + 58 inter-group)
# Constraints: 311
# Total specification entries: ~1,008
# States: ~155 across all groups
# Actions: ~220 across all groups
# Behavior sets: 9 (28 groups entirely deterministic)

# insights(id|insight|evidence)
IN1|OS has exactly 9 autonomous decision points; everything else is deterministic sequencing|9 behavior sets out of 37 EntityGroups; 28 groups entirely force_action
IN2|Almost all decision-making is resource pressure response|Memory pressure, swap pressure, congestion, log buffer, connection health, device error recovery — ratio-of-capacity measurements
IN3|Only user-facing decision is session idle policy|1 of 9 behavior sets (SessionIdleResponse); rest are internal resource management
IN4|Fundamental pattern: 15 singletons orchestrating 20 populations|One-to-Infinity fan-out is the dominant interaction; populations are passive
IN5|Populations are passive; complexity does not scale with entity count|Process, Thread, File, etc. all purely reactive; million processes not complex, one scheduler is complex
IN6|Failure handling structurally identical to normal operation|Failed states use same state machine, same flow/constraint mechanism, same utility AI; no separate error architecture
IN7|Inter-group flows expose actual dependency architecture|Fan-out from Init to Services/Devices; convergence from Devices to Kernel; invisible in source code, explicit in flow list
IN8|Cross-group constraints are where coupling lives|Every inter-group dependency visible as constraint entry; enumerable and auditable
IN9|Zero-cardinality groups are real architectural components|BIOS/Bootloader are first-class specification members with events and flows, without fake runtime entities
IN10|Compression effect: Infinity cardinality replaces per-instance naming with generic lifecycle on population|9 unique service names → 3 generic event types on population; cardinality does the naming work

# claims(id|claim|type|depends_on)
CL1|Four flat lists specify a complete operating system in ~1,008 entries readable in an afternoon|observation|P1
CL2|Specification is closed under addition: new components add entries without modifying existing ones|axiom|P2
CL3|Cardinalities determine interaction patterns mechanically, not by design decision|derivation|P3,CI1-CI6
CL4|An OS is overwhelmingly sequencing (getting things in right order), not deciding what to do|derivation|IN1,IN2
CL5|The intelligence of an OS is pressure management|derivation|IN2,BS1-BS9
CL6|Populations are passive; all transitions driven externally; complexity is in the singletons not the populations|derivation|IN5
CL7|Failure is just another state with transitions and constraints; receives same completeness guarantee as success|derivation|IN6
CL8|Adding Bluetooth = adding entries to four lists; none of existing 37 groups, 311 events, 349 flows, 311 constraints change|derivation|P2
CL9|CLA extends NDD by adding EntityGroups with cardinality, flows, constraints, and machine-readable structure|derivation|P1
CL10|Progress tracking is counting: events with implemented actions vs events without|derivation|P4

# rules(id|rule|rationale)
R1|Write EntityGroups first: name every noun, assign cardinality|Cardinality determines all interaction patterns; must be decided before events
R2|Write EventSets second: extract every verb-noun pair, assign to owning group|Events are the lifecycle; groups without events have no lifecycle
R3|Write EventFlows third: declare ordering within and between groups|Flows are the behavior; unreachable events are specification errors or external entry points
R4|Write EventConstraints fourth: declare conditions for every event|Constraints make every dependency explicit; references to nonexistent fields reveal incomplete entity model
R5|Check completeness mechanically at each step|Group without events, event without flows, event without constraint — each is diagnosable gap
R6|Estimation is per-event, not per-module|Each event is bounded, independently testable unit of functionality

# relationships(from|rel|to)
P1|defines|L1,L2,L3,L4
P2|defines|closedness_property
P3|determines|CI1,CI2,CI3,CI4,CI5,CI6
P4|enables|mechanical_completeness_checking
P5|contrasts_with|projection_based_methods
L1|prereq_of|L2
L2|prereq_of|L3
L3|prereq_of|L4
C1|populated_by|C2
C2|ordered_by|C3
C3|gated_by|C4
C5|constrains|CI4,CI6
C6|constrains|CI1,CI2,CI5
C7|constrains|CI1,CI2,CI3
C8|used_by|BS1-BS9
C9|used_by|28_deterministic_groups
C10|implements|action_output
C11|connects|EP1,EP2
EP1|uses|C8,C9,C10
EP2|uses|C3,C4
IN1|derives_from|BS1-BS9
IN4|derives_from|G1-G37
IN5|derives_from|G18-G37
IN6|enabled_by|C11
CL2|demonstrated_by|CL8
CL3|demonstrated_by|CI1-CI6
CL4|demonstrated_by|IN1

# section_index(section|title|ids)
1|The Problem With Partial Views|P1,P5
2|The Four Lists|L1,L2,L3,L4,C1,C2,C3,C4,P4
3|Cardinality as Architecture|P3,C5,C6,C7,CI1-CI6,CL3
4|The Execution Pipeline|EP1,EP2,C8,C9,C10,C11
5|Worked Example: The Operating System|—
6|List 1: What Exists|G1-G37,IN4,IN9,IN10
7|List 2: What Happens|C2,IN10
8|List 3: In What Order|C3,CI1-CI6,IN7
9|List 4: Under What Conditions|C4,IN8
10|States Actions and Decision Points|C8,C9,BS1-BS9,IN1,IN2,IN3
11|What the Specification Reveals|IN1-IN10,CL4-CL7
12|Closedness|P2,CL2,CL8
13|The Specification-Execution Bridge|EP1,EP2
14|Relationship to NDD|CL9
15|How to Use CLA|R1-R6,CL10
16|Boundaries|—
17|Conclusion|CL1
Appendix|Supporting Tables|G1-G37(full events),BS1-BS9(full considerations+behaviors),all flows,all constraints

# decode_legend
four_lists: EntityGroups(nouns+cardinality)|EventSets(verbs+data)|EventFlows(ordering)|EventConstraints(conditions)
cardinalities: Zero(boundary,emit-only)|One(singleton,orchestrator)|Infinity(population,passive)
interaction_patterns: fan-out(One→Infinity)|convergence(Infinity→One)|list-to-list(Infinity→Infinity)|event-sequencing(Zero→any)|peer-handoff(One→One)|ordering-only(Zero→Zero)
flow_types: linear|branching|parallel|fan-out|convergence|cyclic
action_types: force_action(deterministic)|behavior_set(utility AI scored)
behavior_set_types: pressure|resource|health|recovery|user-facing
curve_types: Linear|InverseLinear|Quadratic|Exponential|Step
entity_group_counts: 2 Zero + 15 One + 20 Infinity = 37
spec_counts: 311 events + 349 flows + 311 constraints = ~1,008 entries
behavior_set_counts: 9 sets, 38 considerations, 41 behaviors
os_ratio: 15 singletons orchestrating 20 populations; 9 decision points; 28 deterministic groups
claim_types: axiom|derivation|observation
rel_types: defines|determines|enables|contrasts_with|prereq_of|populated_by|ordered_by|gated_by|constrains|used_by|implements|connects|uses|derives_from|demonstrated_by|enabled_by
NDD_ref: Name Driven Development [@HOWL-COMP-11-2026] (not cross-referenced; noted for provenance only)
+standalone: this doc self-contained
