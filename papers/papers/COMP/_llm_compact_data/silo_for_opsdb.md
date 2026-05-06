# SILO INFRASTRUCTURE FOR OPSDB — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → subsystems → structures → execution_pipeline → mechanisms → security → distinctions → claims → relationships → section_index → decode_legend
# Source: COMP 1-5 series, filtered for OpsDB-applicable infrastructure. Removed: NUMA threading, Zig memory management, game content systems, rendering, animation, audio, sprite batching, combat, NPCs, equipment slots, field replacement for game domains. Retained: execution model, security model, data-only architecture, state machines, prolog, utility AI, logic blocks, scene isolation, networking, trace system, partial geometric security.

# principles(id|principle|rationale)
P1|Behavior resides in data, not code|Infrastructure compiles once; behavior changes = edit data tables; no recompile, no restart
P2|Universal container — single struct for all managed objects|Difference between entity types is which fields contain data, not type hierarchy
P3|Zero gameplay types in binary|Compiled code = infrastructure only (SM runners, predicate evaluators, utility scorers, effect processors); binary doesn't know what application it runs
P4|Funnel architecture — layered complexity reduction|Each layer filters scope: SM→Prolog→UAI→LogicBlock; separation of concerns through pipeline
P5|Every subsystem consumes same uniform data layout|All subsystems read same column-oriented tables with FK relationships; no special cases; no subsystem-specific formats
P6|Safety by anatomy not policy|Security derives from structural limitation of what system can do, not rules about who can do what
P7|Vocabulary restriction|Execution engine only unifies logic conforming to six defined primitives; no other operations exist
P8|Zero-negotiation I/O|Network and memory ops governed by strict schema alignment; non-conforming data discarded at boundary
P9|Monotonic funnel|All external inputs and internal state changes processed as relational transforms on single deterministic heartbeat
P10|Errors are data outliers not execution faults|Arithmetic exceptions return boundary values; processing heartbeat uninterrupted
P11|Authority is static property of infrastructure|No mechanism to create new primitives or widen path-whitelists at runtime
P12|Shape before meaning|Untrusted input never interpreted as logic, only as geometry
P13|Conform exactly or drop|All ingress data must match predefined memory shape exactly; no recovery, partial acceptance, truncation, or negotiation
P14|Designers create new mechanics without engineers|Not "tweak values" but "create new systems" by cross-wiring existing tables
P15|Marginal cost of new behavior approaches zero|1000th behavior set costs same as 10th; complexity constant because interactions are data relationships not code dependencies
P16|Infrastructure bug = one-time fix protecting all consumers|Shared infrastructure vs per-application vulnerability

# concepts(id|name|category|definition)
C1|Data-only execution|core|Behavior in data structures interpreted by infrastructure; no compilation for behavior changes
C2|Tall-infra|core|Comprehensive infrastructure provides all primitives pre-compiled; application developers compose via data configuration
C3|Hot-swapping|core|Data tables replaced while running; new behavior executes next cycle
C4|The wall|anti-pattern|Boundary where compiled behavior exists somewhere in binary; data-driven preserves it, data-only eliminates it
C5|Semantic repurposing|pattern|Same fields, different meaning via data wiring; infrastructure doesn't care about domain semantics
C6|Geometric security|security|Security model where integrity derives from anatomical limitation via monotonic processing funnel; restricts all state transitions to closed set of six primitives
C7|Partial geometric security|security|Subset of full geometric security; enforces geometric invariants at system ingress only; eliminates buffer overflows, parser confusion, injection while compatible with existing stacks
C8|Relational filter|security|Replaces kernel/user space distinction; all I/O through fixed-size relational schema; geometric shape mismatch = discard
C9|Monotonic heartbeat|mechanism|Single deterministic update pump; all processing occurs on this heartbeat
C10|Vocabulary limitation|security|Actor has access only to whitelist of data paths; six primitives are only available operations; cannot create new primitives or widen whitelist
C11|Structural impossibility|security|Security property achieved through absence of mechanism rather than policy enforcement
C12|Structured tracing|debugging|Per-entity per-cycle decision log; debug in domain terms not memory addresses
C13|Blue/green replay|debugging|Modify rules, replay same cycle with modified rules, compare old vs new decision outcomes
C14|Path-based access control|security|Field paths matched against whitelist patterns; both scene ID and path must pass
C15|Ingress shim|security|Single validation layer per I/O boundary; fixed-shape buffers; copy-or-drop semantics
C16|Multiplicative scoring|pattern|Any consideration=0 → entire behavior=0; fail-fast gating
C17|Fact regeneration|mechanism|Entity facts regenerated every cycle from current state; decisions always use current data
C18|Stack-based bytecode|execution|Logic blocks execute on fixed stack; type-safe, no syntax errors possible
C19|Scene as execution context|abstraction|Isolated context with own entity pool, behavior defs, access control; maps to: tenant, request, process, workflow

# subsystems(id|name|role|key_properties)
SS1|Entity|Universal container for all managed objects|Single struct; optional systems; same struct for all object types regardless of domain
SS2|StateMachine|Pure topology — states + transitions|No behavior logic inside; references behavior_set_id; event/rule/duration transitions; one runner for all domains
SS3|Prolog|Declarative rule engine|Terms (atom/variable/number/entity); facts generated per cycle; unification-based evaluation; domain-agnostic
SS4|UtilityAI|Multiplicative behavior scoring|Considerations with curves, weights, inversion; behavior sets with selection methods; scores not scripts
SS5|LogicBlock|Stack-based bytecode execution|~100+ block types; control flow, math, logic, data access; path-based field read/write; domain-agnostic
SS6|Scene|Isolated execution context|Own entity pool, behavior defs, network buffers; access via SceneSetItem whitelist; default deny
SS7|Networking|Fixed-shape packet processing|Fixed-size payload, no pointers, no nested alloc; mediating scene handles all I/O
SS8|Trace|First-class debugging|Per-entity per-cycle: state before/after, all behavior scores + consideration scores, logic execution, stat diffs

# execution_pipeline(id|layer|question|input|output)
EP1|1-StateMachine|What state is this entity in?|All possible behaviors|Behaviors valid in current state
EP2|2-Prolog|Are preconditions met?|State-valid behaviors|Precondition-satisfied behaviors
EP3|3-UtilityAI|Which behavior scores highest?|Satisfied behaviors|Single winning behavior
EP4|4-LogicBlock|How do I execute this?|Winning behavior|Field modifications on entity
# Shortcuts: force_action on state bypasses UAI; exit_on_event bypasses Prolog; exit_condition_rule_name uses Prolog only

# mechanisms(id|subsystem_id|name|description)
M1|SS2|Event-based transition|exit_on_event fires → immediate transition; external triggers
M2|SS2|Rule-based transition|exit_condition_rule_name evaluated every cycle via Prolog; condition-based
M3|SS2|Duration-based transition|duration_min = minimum time in state before any transition allowed
M4|SS2|Combined transition|All conditions (event AND rule AND duration) must satisfy simultaneously
M5|SS2|Force action|force_action on state skips UAI, executes action directly
M6|SS2|Multiple SMs per entity|Up to 14 independent SMs per entity; coordinate via shared entity fields, no direct coupling
M7|SS3|Fact generation|Every cycle: entity state → facts (entity_type, in_state, has properties, stat thresholds, relationships)
M8|SS3|Unification|Variable binding: predicate(X) matches predicate(42) → X=42; subsequent facts use binding
M9|SS3|Three use sites|State machine transitions, UAI consideration gating, logic block conditions
M10|SS4|Multiplicative scoring|running_score starts 1.0; each consideration multiplied in; any 0 → total 0
M11|SS4|Consideration pipeline|Check prolog rule (fail→0) → get input value → normalize to [0,1] → apply curve → apply weight → invert if flagged → multiply into running score
M12|SS4|Average-and-fixup|Compensates multiplicative penalty from many considerations: makeup = (1-score) × (1-1/count) × score
M13|SS4|Selection methods|top (deterministic), weighted_random_top3 (70%/25%/5%), random_reasonable
M14|SS4|Adding behaviors|Add entry to behavior set data table; no code changes; new behavior competes fairly via scoring
M15|SS5|Stack machine|Fixed stack; blocks push/pop typed values; control flow via If/While/ForEach with skip-to-matching
M16|SS5|Path-based data access|DrGetFloat("field.path") resolves at runtime; field access via string paths
M17|SS5|Type safety without compilation|Each block type has fixed input/output types; editor shows only compatible blocks for current stack state
M18|SS5|Runtime never crashes|Invalid paths → default values; math ops clamp/saturate; array access bounds-checked
M19|SS5|Cross-system calls|ExecutePrologQuery→bool, ExecuteLogicBlockStack→value, TriggerEvent→state transition
M20|SS6|Cross-scene enforcement|sceneCanWrite checks: from_scene in allow_write_scene_ids AND path matches allow_write_paths pattern; both must pass
M21|SS6|Default deny|Empty access lists deny all access; both scene ID and path whitelist must pass
M22|SS7|Packet flow|Ingress→MediatingScene→validate→route→check access→decode→write allowed paths only→target scene
M23|SS7|Malicious input handling|Bad values accepted to input fields → validation rules fail next cycle → behavior scores 0 → entity ignores input → overwritten next cycle
M24|SS8|Trace capture|Every entity every cycle: state before/after, all behavior scores with per-consideration breakdown, logic execution with timestamps, stat diffs
M25|SS8|Blue/green replay|Pause at cycle → examine trace → modify rules → replay same cycle with modified rules → compare decisions → accept or reject

# six_primitives(id|name|shape|what_it_does|security_property)
SP1|Finite State|Point|Named identity in pre-defined relational table|Prevents undefined/illegal states
SP2|Explicit Transition|Edge|State changes only across directed edges in data schema|If transition path not asserted, physically unreachable
SP3|Boolean Condition|Gate|Predicate logic acts as gate requiring absolute unification with local facts|Only bit-perfect logic opens gate
SP4|Utility Selection|Shunt|Multiplicative utility curves replace imperative branching|Eliminates if-else jump-table surface; malicious input contributes number to formula, cannot hijack branch
SP5|Atomic Sequence|Pipe|Logic blocks executed by atomic stack machine|No indirect jumps, no arbitrary memory pointers
SP6|Bounded Effect|Curve|Time-bounded transformations within infrastructure-clamped ranges|All mutations within clamped ranges over temporal curve

# security_threats(id|threat|status|how_addressed)
ST1|Buffer overflow|eliminated (full+partial)|Fixed-shape buffers; no adjacent memory to corrupt; no heap interaction during ingress; undersized also rejected
ST2|Privilege escalation|eliminated (full)|No vocabulary; six primitives cannot create primitives or widen whitelists; authority = static infrastructure
ST3|Code injection|eliminated (full+partial)|Fixed-type fields; atomic stack machine has no indirect jumps; input never interpreted as logic
ST4|Data exfiltration|eliminated (full)|Scene path whitelist; scene physically cannot reference paths outside whitelist
ST5|Jump-table hijack|eliminated (full)|Utility selection replaces imperative branching; no if-else surface
ST6|Divide-by-zero crash|eliminated (full)|Hardware spec returns boundary values; errors = data outliers not execution faults
ST7|Parser differentials|eliminated (partial)|No parsing; shape-validate or drop; no re-parsing after ingress
ST8|Length confusion|eliminated (partial)|Exact byte count required; both over and under rejected
ST9|Type confusion|eliminated (partial)|Fixed struct fields; no reinterpretation of input bytes
ST10|Side-channel attacks|NOT eliminated|Timing, cache, speculation; design/operations problem
ST11|Denial of service|NOT eliminated|Availability attacks; design/operations problem
ST12|Data poisoning|NOT eliminated|Valid but malicious values; semantic problem; mitigated by prolog validation rules scoring 0 next cycle
ST13|Logic flaws|NOT eliminated|Bad business rules; outside structural security scope

# partial_geometric_security(id|rule|detail)
PG1|Exact byte count required|No variable-length acceptance at ingress
PG2|No variable-length fields|All fields fixed size in struct
PG3|No pointers in ingress structs|All values inline
PG4|No nested allocations|Flat structure only
PG5|No flexible array members|Prohibited at ingress
PG6|Drop on any mismatch|Wrong size, invalid ranges, failed checksums, malformed headers
PG7|Dropped input never touches application memory|Rejection before copy to application space
PG8|No re-parsing after ingress|Logic reads validated struct fields only
PG9|No string interpretation post-ingress|Eliminates injection surface
PG10|No pointer arithmetic from input|Input values cannot compute memory addresses
# Partial geometric security = deployable as shim on existing systems including Go; no language changes required

# scene_access_control(id|field|purpose)
SA1|allow_read_scene_ids|[]i32 whitelist of scenes that may read this scene's data
SA2|allow_write_scene_ids|[]i32 whitelist of scenes that may write to this scene's data
SA3|allow_read_paths|[]TextArray glob patterns for readable field paths
SA4|allow_write_paths|[]TextArray glob patterns for writable field paths
# Default deny: empty lists = no access. Both scene ID and path pattern must pass.

# litmus_test(id|question|fail_means)
LT1|Can a configurator add new workflow behavior without engineering?|Wall present
LT2|Can a stat field be repurposed for a different domain with zero code change?|Wall present
LT3|Can you swap every behavioral rule while the executable keeps running?|Wall present
LT4|Does the compiled binary know any domain noun exists?|Wall present

# distinctions(id|side_a|side_b|key_asymmetry)
D1|Data-driven (code owns types, data owns numbers)|Data-only (binary forgets nouns, dataset teaches each cycle)|Wall between data and behavior: present vs eliminated
D2|Policy-based security (permissions, guards, rules)|Geometric security (anatomical limitation, vocabulary restriction)|Choice vs physiological impossibility
D3|Reactive patching (detect and fix)|Structural invariance (no vocabulary for attack)|Arms race vs permanent closure
D4|Parse and sanitize|Shape-validate or drop|Negotiation vs binary accept/reject
D5|Imperative conditions (if/else/switch)|Predicate logic (rules unified against facts)|Scalability, reusability, hot-swappability
D6|Scripted behaviors (code determines action)|Scored behaviors (utility determines action)|Emergence vs authorship; data-only vs compiled
D7|Stack traces (memory addresses)|Structured traces (domain-aware decision queries)|Debug in code terms vs application terms
D8|Per-application security fixes|One-time infrastructure fix|Shared infra vulnerability fixed once protects all consumers
D9|Exception/crash error handling|Boundary clamping (burn dead wood)|System failure vs edge-case math
D10|Large security surface (arbitrary code)|Minimal surface (6 primitives)|Unbounded attack vocabulary vs closed vocabulary
D11|Full geometric security (seals ingress+interpretation+control+state+execution)|Partial geometric security (seals ingress only)|Perfect closure vs massive improvement with near-zero friction
D12|Kernel/user space wall (fence around data)|Relational filter (filter around logic)|Partition-based vs vocabulary-based isolation

# implementation_notes(id|note)
IN1|Execution pipeline (SM→Prolog→UAI→LogicBlock) is domain-agnostic; same runner processes any entity type
IN2|State machines contain no behavior logic; they reference behavior sets; one runner function walks all state graphs
IN3|Prolog rules reusable across SM transitions, UAI considerations, and logic block conditions
IN4|Adding new behavior = add data rows to behavior set; no code changes; new behavior competes fairly via scoring
IN5|Scene isolation maps directly to tenant isolation, request isolation, workflow isolation
IN6|Partial geometric security deployable as Go shim on I/O boundaries; no language changes needed
IN7|Trace system enables debugging in application domain terms; "why did entity X transition?" = query trace, see complete decision chain
IN8|All behavior hot-swappable: state machines, prolog rules, behavior sets, logic blocks; changes take effect next cycle
IN9|Can write wrong logic, cannot crash; runtime returns defaults for invalid paths, math clamps, bounds-checked
IN10|Wall-less paradox: no traditional partitions between infrastructure and application, but trapped by six primitive shapes; wall moved from fence around data to filter around logic

# claims(id|type|claim|basis)
CL1|axiom|Binary should contain zero application-domain types — infrastructure only|Eliminates wall between data and behavior
CL2|axiom|Behavior is data, not code|Dataset teaches binary every cycle what exists and how everything behaves
CL3|derivation|Marginal cost of new behavior → zero engineering time|All semantics in table rows; no code changes for new behavior
CL4|axiom|Security should be physiological impossibility not policy choice|Geometric constraints make exfiltration and escalation anatomically impossible
CL5|derivation|System provides no vocabulary through which attack can be expressed|Six primitives are closed set; none allow creation of new primitives or widening of whitelists
CL6|axiom|"Nothing else ever happens" is physical law not policy|Monotonic funnel + six primitives = only possible operations
CL7|derivation|Partial geometric security eliminates buffer overflows, parser confusion, injection in any language|Fixed-shape ingress + structs-only post-ingress + no re-parsing
CL8|prescription|Security does not require perfect systems to be effective|Partial approach eliminates entire exploit classes with minimal effort
CL9|observation|Infrastructure cost is front-loaded; productivity multiplier is permanent|Amortization argument for tall-infra investment
CL10|distinction|Data-driven = faster tuning; data-only = faster behavior creation|Wall present vs wall eliminated
CL11|axiom|If attack cannot be expressed, it cannot succeed|Structural refusal; vocabulary absence = security
CL12|derivation|Infrastructure bug fix protects all consumers simultaneously|Shared infrastructure vs per-application vulnerability

# relationships(from|rel|to)
P1|grounds|C1
P2|grounds|SS1
P3|grounds|C1
P4|grounds|EP1,EP2,EP3,EP4
P5|enforces|SS1,SS2,SS3,SS4,SS5
P6|grounds|C6
P7|grounds|C10
P7|enforces|SP1,SP2,SP3,SP4,SP5,SP6
P8|grounds|C8
P9|grounds|C9
P10|grounds|ST6
P11|prevents|ST2
P12|grounds|C7
P13|grounds|C15
P14|derives_from|C5
P15|derives_from|P1
P16|grounds|CL12
C1|enables|C3
C2|enables|CL3
C4|absent_from|C1
C5|enables|C19
C6|implements|P6
C7|subset_of|C6
C8|replaces|D12
C9|mechanism_of|P9
C10|prevents|ST2,ST4
C11|derives_from|P6
C12|implements|SS8
C13|implements|SS8
C14|enforces|SS6
C15|implements|P13
C16|enables|M10
C17|enables|M8
C18|implements|SS5
C19|maps_to|SS6
SS1|input_to|EP1
SS2|implements|EP1
SS3|implements|EP2
SS4|implements|EP3
SS5|implements|EP4
SS6|implements|P11
SS7|implements|C6
SS8|implements|C12
SP1|prevents|ST3
SP2|prevents|ST2
SP3|gates|SP4
SP4|prevents|ST5
SP5|prevents|ST3
SP6|constrains|ST6
M1|mechanism_of|SS2
M2|mechanism_of|SS2
M3|mechanism_of|SS2
M5|mechanism_of|SS2
M7|mechanism_of|SS3
M8|mechanism_of|SS3
M10|mechanism_of|SS4
M11|mechanism_of|SS4
M14|derives_from|C3
M15|mechanism_of|SS5
M16|mechanism_of|SS5
M18|implements|CL9
M20|mechanism_of|SS6
M22|mechanism_of|SS7
M24|mechanism_of|SS8
M25|mechanism_of|SS8
EP1|gates|EP2
EP2|gates|EP3
EP3|gates|EP4
D1|clarifies|CL10
D2|grounds|CL4
D3|grounds|CL5
D11|scopes|C7
LT1|tests|P14
LT2|tests|C5
LT3|tests|P1
LT4|tests|P3

# source_index(source_paper|what_retained|what_removed)
COMP-1|Entity container (de-gamed), execution pipeline, state machines, prolog, utility AI, logic blocks, scene isolation + access control, networking security model, trace system, performance model (non-NUMA)|NUMA core mapping, Zig memory management, rendering/sprites, animation SMs, audio, combat systems, equipment slots, game-domain field replacement examples, game-specific workload types (IntegrateVelocity, BuildSpriteBatch)
COMP-2|Data-only vs data-driven distinction, architecture stack definitions, litmus test, anti-examples, semantic repurposing concept, productivity model, learning disciplines|Game-specific examples (dragon boss, weather/morale/crafting as game systems), game engine comparisons (Unity/Unreal/Bevy/Overwatch), game-specific fit analysis
COMP-3|Not provided in source documents|N/A
COMP-4|Six computational primitives, geometric security model, attack surface analysis, verification properties, wall-less paradox, room-with-no-windows metaphor|None removed (security model is domain-agnostic)
COMP-5|Partial geometric security model, threat model, ingress shim, post-ingress rules, security properties, implementation cost analysis|None removed (partial security model is domain-agnostic and language-agnostic)

# decode_legend
id_prefixes: P=principle, C=concept, SS=subsystem, EP=execution_pipeline_layer, M=mechanism, SP=six_primitive, ST=security_threat, PG=partial_geometric_rule, SA=scene_access, LT=litmus_test, D=distinction, IN=implementation_note, CL=claim
primitive_shapes: Point(State)|Edge(Transition)|Gate(Condition)|Shunt(Selection)|Pipe(Sequence)|Curve(Effect)
claim_types: axiom|derivation|observation|prescription|distinction
threat_status: eliminated(full)|eliminated(partial)|eliminated(full+partial)|NOT_eliminated
rel_types: grounds|enables|enforces|implements|prevents|derives_from|subset_of|replaces|mechanism_of|gates|input_to|maps_to|clarifies|scopes|tests|constrains|absent_from
scene_model: scene = isolated execution context; maps to tenant/request/process/workflow in non-game domains
partial_scope: ingress only — seals I/O boundary; compatible with Go and any other language; deployable as shim
authority_model: static — path whitelists; cannot create primitives or widen whitelists at runtime
error_handling: boundary_clamping — exceptions return boundary values; errors = data outliers not execution faults
de_gaming_note: all game-specific content (rendering, animation, audio, combat, equipment, NUMA threading, Zig memory) removed; retained infrastructure is domain-agnostic and applicable to any data-only execution system including OpsDB
