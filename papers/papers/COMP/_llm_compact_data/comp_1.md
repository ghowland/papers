# SILO: TALL-INFRA DATA-ONLY EXECUTION SYSTEM — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → subsystems → structures → execution_pipeline → mechanisms → security_attacks → implementation_phases → performance → limitations → claims → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Behavior resides in data, not code|Infrastructure compiles once; behavior changes = edit data tables, takes effect next frame
P2|Universal container — single struct for all objects|Difference between dragon and chair is which fields have data, not type hierarchy
P3|Wall-less architecture — all fields public|Access control at scene level via path-based rules, not encapsulation
P4|Funnel architecture — layered complexity reduction|Each layer filters scope: SM→Prolog→UAI→LogicBlock, developer thinks only about one layer
P5|No type hierarchy — no inheritance|All entities identical in structure, differ only in populated fields
P6|Geometric security — fixed shapes prevent attack categories|Fixed-size packets, no pointers, no nested allocations, preallocated buffers
P7|Tall-infra — infrastructure provides all primitives|Application developers compose primitives via data configuration, never write infrastructure code
P8|Standalone scenes — isolated execution contexts|Scenes cannot access each other's data unless explicitly permitted via SceneSetItem
P9|Default deny — empty access lists deny all|Both scene ID and path must match for cross-scene access
P10|DSP model — all workloads are pure data transformations|Input array → transform → output array, no shared mutable state
P11|One-time fix — infrastructure bug fix protects all consumers|Contrast: traditional = per-game vulnerability, per-game fix
P12|Preserve data, compress shape|Field replacement relabels semantics without changing underlying data types

# concepts(id|name|category|definition)
C1|Data-only execution|core|Behavior in data structures interpreted by infrastructure; no compilation for behavior changes
C2|Tall-infra|core|Comprehensive infrastructure provides all primitives pre-compiled; marginal cost of new behavior → zero
C3|Hot-swapping|core|Data tables replaced while running; new behavior executes next frame (16.67ms)
C4|Field replacement|mechanism|Semantic relabeling via replacement table; same f32 data, different domain meaning (health→account.balance)
C5|Geometric security|security|Architectural impossibility of attack categories through structural constraints, not runtime checks
C6|Input isolation|security|Network inputs constrained to allowed paths; cannot reach privileged fields
C7|Funnel architecture|pattern|SM→Prolog→UAI→LogicBlock; each layer reduces candidate set
C8|Barrier synchronization|threading|Single sync point per frame; threads run independently start-to-barrier
C9|NUMA-aware placement|threading|Thread scratch memory + entity data allocated in thread's NUMA node; zero cross-NUMA traffic during frame
C10|Path-based access control|security|Field paths matched against whitelist patterns; both scene ID and path must pass
C11|Multiplicative scoring|pattern|Any consideration=0 → entire behavior=0; fail-fast gating
C12|Decision trace|debugging|Per-entity per-frame record of state, scores, logic execution, stat changes
C13|Blue/green frame replay|debugging|Modify rules, replay same frame, compare old vs new decision outcomes
C14|Bag of bits with enforced structure|pattern|Entity structure fixed (all have same fields), interpretation flexible (field replacement)
C15|Natural domains not enforced boundaries|pattern|Multiple SMs on entity share data freely; separation of concerns without coupling
C16|Average-and-fixup|scoring|Compensates multiplicative penalty from many considerations: makeup = (1-score) × (1-1/count) × score
C17|Prolog fact regeneration|mechanism|Entity facts regenerated every frame from current state; decisions always use current data
C18|Stack-based bytecode|execution|Logic blocks execute on 256-value stack; type-safe, Turing-complete, no syntax errors possible
C19|Scene as execution context|abstraction|Game=scene per player, Web=scene per request, DB=scene per query, OS=scene per process

# subsystems(id|name|role|key_properties)
SS1|Entity|Universal container for all objects|Single struct, ~2KB, 20+ optional systems, field replacement, up to 14 state machines
SS2|StateMachine|Pure topology — states + transitions|No behavior logic inside; references behavior_set_id; event/rule/duration transitions
SS3|Prolog|Declarative rule engine|Terms (atom/variable/number/entity/vector2/rectangle), facts generated per frame, unification-based
SS4|UtilityAI|Multiplicative behavior scoring|Considerations with curves, weights, inversion; behavior sets with selection methods
SS5|LogicBlock|Stack-based bytecode execution|~100+ block types; control flow, math, logic, data access; path-based field read/write
SS6|Thread|NUMA-aware parallel execution|WorkBatch distribution, CPU affinity, per-NUMA scratch memory, barrier sync
SS7|Scene|Isolated execution context|Own entity pool, behavior defs, network buffers, time; access via SceneSetItem whitelist
SS8|Networking|Fixed-shape packet processing|2048-byte payload, no pointers, no nested alloc; network scene mediates all NIC access
SS9|Trace|First-class debugging|Per-entity per-frame: state before/after, all behavior scores + consideration scores, logic execution, stat diffs

# structures(id|subsystem_id|name|essential_fields)
ST1|SS1|Entity|id:i32, entity_type:EntityType, name:Text, state_machine_id:i32, state:Text, anim_state_machine_id:i32, anim_state:Text, transform:EntityTransform, visual:VisualSystem, movement:MovementSystem, character:CharacterSystem, combat:CombatCapabilities, container:ContainerSystem, audio:AudioProfile, behavior:AIBehavior, network:NetworkSystem, input:InputSystem, silo_field_replacement_id:i32, is_active:bool, is_deleted:bool
ST2|SS2|StateMachine|id:i32, name:Text, states:[]StateMachineState, prolog_rule_set_a_id:i32, prolog_rule_set_b_id:i32
ST3|SS2|StateMachineState|name:Text, is_entry_state:bool, behavior_set_id:i32, transitions:[]StateMachineTransition, force_action:ActionType
ST4|SS2|StateMachineTransition|to:Text, exit_on_event:ContentEventType, exit_condition_rule_name:Text, duration_min:f32, delete_entity:bool
ST5|SS3|Term|type:TermType(atom/variable/number/entity/vector2/rectangle), atom:Text, variable:Text, number:f32, index:i32, vec2:Vector2, rect:Rectangle
ST6|SS3|Fact|predicate:Text, args:[]Term
ST7|SS3|Rule|head:Text, body:[]Fact
ST8|SS3|KnowledgeBase|fact_set:FactSet, rule_set:RuleSet, entity_index:i32
ST9|SS4|Consideration|prolog_rule_set_a_id:i32, execute_logic_block_id:i32, range:Vector2, score_weight:f32, curve:Curve, score_inverted:bool
ST10|SS4|Behavior|name:Text, considerations:[]Consideration, execute_logic_block_id:i32, execute_action:ActionType, force_min_value:f32, temp_score:f32
ST11|SS4|BehaviorSet|name:Text, behaviors:[]Behavior, selection_method:SelectionMethod(top/weighted_random_top3/random_reasonable)
ST12|SS5|LogicBlock|type:BlockType, text:Text, value_int:i32, value_float:f32
ST13|SS6|WorkBatch|data_start_index:i32, data_count:i32, workload_type:WorkloadType, input_data_path:Text, input_data_ptr:?[*]u8, input_stride:i32, output_data_path:Text, output_data_ptr:?[*]u8, output_stride:i32
ST14|SS6|Thread|id:i32, cpu_core_id:i32, memory_domain:MemoryDomain, work_batches:[]WorkBatch, scratch_memory_ptr:?[*]u8
ST15|SS6|FrameCoordinator|current_frame:i32, thread_ids:[]i32, threads_completed:[]bool, frame_budget_ms:f32
ST16|SS7|Scene|id:i32, name:Text, actors:[]Entity, levels:[]LevelData, state_machines:[]StateMachine, behavior_sets:[]BehaviorSet, prolog_rule_sets:[]RuleSet, logic_blocks:[]LogicBlockStack, network:SceneNetworkBuffers, game_time:f32, game_frame:i32, delta_time:f32, silo_field_replacement_id:i32
ST17|SS7|SceneSetItem|scene_id:i32, is_maximized:bool, is_minimized:bool, is_floating:bool, floating_rect:Rectangle, z_order:i32, is_focused:bool, update_speed:f32, update_speed_minimized:f32, allow_read_scene_ids:[]i32, allow_write_scene_ids:[]i32, allow_write_paths:[]TextArray, allow_read_paths:[]TextArray
ST18|SS8|InboundPacket|src_mac:[6]u8, dst_mac:[6]u8, ethertype:u16, src_ip:u32, dst_ip:u32, protocol:u8, ttl:u8, src_port:u16, dst_port:u16, tcp_seq:u32, tcp_ack:u32, tcp_flags:u8, payload_data:[2048]u8, payload_length:u16, checksum_valid:bool, owner_scene_id:i32
ST19|SS8|NetworkSceneBuffers|rx_raw:[64]InboundPacket, tx_ready:[64]OutboundPacket
ST20|SS8|SceneNetworkBuffers|inbound:[1000]InboundPacket, outbound:[1000]OutboundPacket
ST21|SS9|EntityTrace|entity_id:i32, frame:i32, state_before:Text, state_after:Text, behavior_set_name:Text, behaviors_scored:[]BehaviorScore, behavior_selected_index:i32, logic_blocks_executed:[]LogicBlockExecution, stats_before:[]StatSnapshot, stats_after:[]StatSnapshot, events_received:[]ContentEventType
ST22|SS9|BehaviorScore|behavior_name:Text, final_score:f32, consideration_scores:[]f32
ST23|SS9|LogicBlockExecution|block_type:BlockType, inputs:[]Value, output:Value, timestamp:f32

# execution_pipeline(id|layer|question|input|output)
EP1|1-StateMachine|What am I doing overall?|All possible behaviors|Behaviors valid in current state
EP2|2-Prolog|Are preconditions met?|State-valid behaviors|Precondition-satisfied behaviors
EP3|3-UtilityAI|Which behavior scores highest?|Satisfied behaviors|Single winning behavior
EP4|4-LogicBlock|How do I execute this?|Winning behavior|Field modifications on entity
EP5|5-Envelopes|Apply stat transformations (DSP)|Modified fields|Final frame values
# Shortcuts: force_action on state bypasses UAI; exit_on_event bypasses Prolog; exit_condition_rule_name uses Prolog only

# mechanisms(id|subsystem_id|name|description)
M1|SS2|Event-based transition|exit_on_event fires → immediate transition; external triggers
M2|SS2|Rule-based transition|exit_condition_rule_name evaluated every frame via Prolog; condition-based
M3|SS2|Duration-based transition|duration_min = minimum time in state before any transition allowed
M4|SS2|Combined transition|All conditions (event AND rule AND duration) must satisfy simultaneously
M5|SS2|Force action|force_action on state skips UAI, executes action directly
M6|SS2|Multiple SMs per entity|Up to 14 independent SMs (behavior, animation, audio, network, UI); coordinate via shared entity fields, no direct coupling
M7|SS3|Fact generation|Every frame: entity state → facts (entity_type, in_state, has_target, target_distance, health_critical, health_low, has_weapon, at_position)
M8|SS3|Unification|Variable binding: has_target(X) matches has_target(42) → X=42; subsequent facts use binding
M9|SS3|Three use sites|State machine transitions, UAI consideration gating, logic block conditions
M10|SS4|Multiplicative scoring|running_score starts 1.0; each consideration multiplied in; any 0 → total 0
M11|SS4|Consideration pipeline|Check prolog rule (fail→0) → get input value (logic block or direct stat) → normalize to [0,1] → apply curve → apply weight → invert if flagged → multiply into running score
M12|SS4|Average-and-fixup|mod_factor = 1-(1/count); makeup = (1-score)×mod_factor; final = score + makeup×score
M13|SS4|Selection methods|top (deterministic), weighted_random_top3 (70%/25%/5% top 3), random_reasonable
M14|SS4|Adding behaviors|Add entry to behavior set data table; no code changes; new behavior competes fairly via scoring
M15|SS5|Stack machine|256-value stack; blocks push/pop typed values; control flow via If/While/ForEach with skip-to-matching
M16|SS5|Path-based data access|DrGetFloat("character.health") resolves at runtime; field replacement checked if silo_field_replacement_id set
M17|SS5|Type safety without compilation|Each block type has fixed input/output types; UI shows only compatible blocks for current stack state
M18|SS5|Runtime never crashes|Invalid paths → default values; math ops clamp/saturate; array access bounds-checked
M19|SS5|Cross-system calls|ExecutePrologQuery→bool, ExecuteLogicBlockStack→value, ApplyDamage→envelope, TriggerEvent→state transition
M20|SS6|Work distribution|Entity array divided by thread count; each thread gets exclusive range; no overlap
M21|SS6|NUMA placement|Cores mapped to NUMA nodes; scratch memory allocated in local node; entity data duplicated per node (input copied local, output written local, merged after barrier)
M22|SS6|Barrier sync|Single sync point per frame; all threads run to completion independently; O(cores) cost for O(entities/cores) work
M23|SS6|No contention design|No locks (exclusive ranges), no sharing (single-thread entity ownership), no context switches (run to completion), NUMA local
M24|SS7|Cross-scene enforcement|sceneCanWrite checks: from_scene in allow_write_scene_ids AND path matches allow_write_paths pattern; both must pass
M25|SS8|Packet flow|NIC→NetworkScene(rx_raw)→validate→route by dst_port→check access→decode→write allowed paths only→game scene
M26|SS8|Malicious input handling|Bad values (NaN, MAX_FLOAT) accepted to input fields → Prolog validation rule fails next frame → behavior scores 0 → entity ignores input → overwritten next frame
M27|SS9|Trace capture|Every entity every frame: state before/after, all behavior scores with per-consideration breakdown, logic block execution with timestamps, stat diffs
M28|SS9|Blue/green replay|Pause at frame → examine trace → modify rules → replay same frame with modified rules → compare old vs new decisions → accept or reject
M29|SS1|Field replacement|silo_field_replacement_id references table mapping paths to alternative labels; same data types, different UI presentation; enables domain repurposing without infrastructure changes

# enumerations(id|name|values)
EN1|TermType|atom, variable, number, entity, vector2, rectangle
EN2|Curve|Linear, InverseLinear, Quadratic, Exponential, Sigmoid, Boolean, ~20+ total
EN3|SelectionMethod|top, weighted_random_top3, random_reasonable
EN4|MemoryDomain|NumaNode0, NumaNode1, NumaNode2, NumaNode3, GPU, SharedCPU
EN5|BlockType categories|ControlFlow (If/ElseIf/Else/While/ForEach @1000+), Statements (SetValue*/Log/ExecuteCommand @10000+), Reporters (GetValue*/DrGet* @1000000+), Math (Add/Multiply/Clamp/Sin/Vec2* @1003000+), Logic (And/Or/Equal/Less @1002000+); ~100+ total
EN6|WorkloadType|IntegrateVelocity, UpdateAwareness, EvaluateUtilityAI, ExecuteStateMachine, BuildSpriteBatch, ~30+ total

# security_attacks(id|attack|result|why_blocked)
SA1|Buffer overflow (send 4096 bytes)|Packet rejected at NIC level|Fixed 2048-byte payload; size mismatch drops before software
SA2|Code injection (function pointer in payload)|Copied as u8 data, never executed|Field type is u8 array, not function pointer
SA3|Write to health|Path blocked|"actors.0.character.health" not in allow_write_paths
SA4|Read other player data|No read mechanism in input path|Cannot trigger outbound packet with arbitrary data
SA5|Data exfiltration|Game scene cannot write to network.outbound|Not in allow_write_paths for game scene
SA6|Privilege escalation|Path blocked|"is_dev_mode" not in allow_write_paths
SA7|Malicious input values (NaN, MAX_FLOAT)|Accepted to input fields, ignored next frame|Prolog validation fails → behavior scores 0 → entity continues previous behavior → overwritten next frame
# Attacker controls: packet contents (2048 bytes), valid checksum, correct port
# Attacker cannot: crash game (NaN handled), corrupt state (only input fields writable), persist malicious state (overwritten), escalate, exfiltrate

# implementation_phases(id|phase|approx_lines|components|validates)
IP1|Minimum viable system|500|Entity (100), simple SM (50), single behavior set (75), basic logic blocks (200), single-threaded loop (100)|Entity updates, SM transitions, behaviors execute, logic blocks modify entity
IP2|Add Prolog|325|Core structures (150), entity fact generation (100), SM transition integration (50), UAI consideration integration (25)|Rules match facts, SM uses rules, UAI uses rules for gating
IP3|Add parallel execution|450|Work distribution (200), thread workers (150), barrier sync (100)|Work distributed evenly, threads independent, barrier waits, results correct, >90% CPU utilization
IP4|Add scene isolation|250|Scene structure (100), SceneSetItem access control (100), enforcement (50)|Default deny, explicit whitelist required, path matching correct
IP5|Add network security|450|Fixed packet structures (150), network scene (200), firewall integration (100)|No overflow, only allowed paths writable, game scenes cannot access NIC, malicious input contained

# performance(id|metric|value|conditions)
PF1|Single-threaded frame time|32ms|10K entities, 3 states, 3 behaviors × 2 considerations, 10 logic blocks avg
PF2|8-thread frame time|4.2ms|Same workload; 238 FPS; 760% CPU (95%/core); 7.6x speedup
PF3|16-thread frame time|2.1ms|Same workload; 476 FPS; 1520% CPU (95%/core); 15.2x speedup
PF4|Scaling efficiency|>95% linear|Tested to 64 cores: 6080% utilization
PF5|Per-frame breakdown (16 threads)|Work distribution 0.05ms, entity updates 1.50ms (SM 0.30 + Prolog 0.40 + UAI 0.50 + LB 0.30), barrier 0.10ms, render prep 0.45ms = 2.10ms total|87% headroom at 60 FPS
PF6|Memory per entity|~3KB|Entity struct ~2KB + trace 1 frame ~1KB
PF7|Memory shared data|~2MB|20 SMs ~100KB + 50 behavior sets ~500KB + 30 rule sets ~200KB + 100 LB stacks ~1MB
PF8|Total memory|~32MB|10K entities + all behavior data
PF9|Hot-swap latency|16.67ms|One frame; edit data table → save → next frame loads new data
PF10|Hardware tested|AMD Ryzen 9 5950X|16 cores, 64GB RAM
# Bottlenecks: Prolog evaluation (complex rules w/ deep recursion); cache misses (entity spatial locality); barrier overhead (marginal)
# Optimizations: Prolog depth limit 5 + cache common queries (0.40→0.25ms); sort entities by screen-space position (1.50→1.20ms)

# limitations(id|limitation|detail)
LM1|2D only|3D requires additional visual systems (skeletal anim, materials, lighting); same architecture, more Entity.visual data
LM2|Prolog performance|Degrades with >100 rules per query; no indexing; naïve unification
LM3|Fixed buffer sizes|All buffers preallocated; configurable but not dynamic; tradeoff performance vs flexibility
LM4|No garbage collection|Manual memory management; entities reused via is_deleted flag, not freed

# claims(id|type|claim|basis)
CL1|axiom|Behavior should reside in data, not compiled code|Eliminates 30s-5min iteration loop
CL2|axiom|Single universal container preferable to type hierarchy|Difference is populated fields, not types
CL3|derivation|Marginal cost of new behavior approaches zero engineering time|Tall-infra provides all primitives; add behavior = add data entry
CL4|observation|95%+ CPU utilization per core achieved|No locks, no sharing, no context switches, NUMA local
CL5|derivation|Geometric security = architectural impossibility of privilege escalation|Fixed-size packets + path-based access = cannot overflow, inject, or escalate
CL6|prescription|Start with 500-line MVS, validate each layer, expand incrementally|Implementation phases IP1-IP5
CL7|observation|Minutes-to-hours saved per bug via trace system|Traditional: reproduce→recompile→guess; Silo: query trace→see chain→modify rule→replay
CL8|reframe|Scene = execution context applicable to any domain|Game/Web/DB/OS all map to scene model
CL9|axiom|Axioms first, data only, ship faster|Core philosophy of tall-infra data-only execution
CL10|derivation|Infrastructure bug = one-time fix protecting all consumers|Shared infrastructure vs per-application vulnerability
CL11|observation|Frame time 4-8ms for 10K entities allows 60 FPS with 87% headroom|Measured on Ryzen 9 5950X, 16 threads
CL12|distinction|Can write wrong logic, cannot crash|Runtime returns defaults for invalid paths; math clamps; bounds-checked

# distinctions(id|side_a|side_b|key_asymmetry)
D1|Traditional (compile behavior into code)|Silo (behavior in data tables)|Iteration: 30s-5min vs 16ms (next frame)
D2|Type hierarchy (Dragon extends Entity)|Universal container (same struct, different fields populated)|No runtime type checking needed; infrastructure processes all identically
D3|Encapsulation (getters/setters)|Wall-less (all fields public)|Access control moved to scene level, not entity level
D4|Imperative conditions|Declarative Prolog rules|Reusable across SM/UAI/LB; composable; hot-swappable; introspectable
D5|Traditional threading (locks, contention)|Silo threading (exclusive ranges, barrier only)|8 cores: ~600% vs ~760% utilization
D6|Per-game security fixes|One-time infrastructure fix|Shared infra vulnerability fixed once protects all consumers
D7|Breakpoint debugging|Decision trace + frame replay|See complete decision chain per entity per frame; modify rules and replay
D8|ECS (behavior in compiled systems)|Silo (behavior in data tables)|Both cache-friendly + parallel; Silo hot-swaps everything
D9|Behavior trees (priority-based)|Utility AI (score-based)|BT: well-understood patterns; UAI: emergent behavior, rapid iteration
D10|Sandboxing (runtime isolation)|Geometric security (structural impossibility)|Fixed shapes prevent attack categories architecturally

# validation_checklist(id|test|criteria)
VC1|Hot-swap|Modify behavior set while running → takes effect next frame (16ms)
VC2|Scalability|Add new behavior to set → existing behaviors unaffected
VC3|Trace|Query trace for specific frame/entity → complete decision chain visible
VC4|Parallel|8 cores → >90% utilization per core
VC5|Isolation|Scene A cannot read Scene B without explicit permission
VC6|Security|Network packet cannot write to non-whitelisted path
VC7|Field replacement|Change silo_field_replacement_id → UI labels change
VC8|Performance|10K entities update in <10ms per frame

# relationships(from|rel|to)
P1|grounds|C1
P2|grounds|C14
P3|enables|C10
P4|grounds|C7
P5|grounds|D2
P6|grounds|C5
P7|grounds|C2
P7|enables|CL3
P8|grounds|C19
P9|enforces|M24
P10|grounds|C8
P11|grounds|CL10
P12|enables|C4
C1|enables|C3
C2|enables|CL3
C3|requires|P1
C4|implements|P12
C5|implements|P6
C5|prevents|SA1
C5|prevents|SA2
C5|prevents|SA6
C6|implements|C5
C7|composes|EP1,EP2,EP3,EP4
C8|implements|P10
C9|enables|CL4
C10|enforces|P8
C11|enables|M10
C12|enables|CL7
C13|enables|D7
C14|enables|C4
C17|enables|M8
C18|implements|SS5
SS1|component_of|EP1
SS2|implements|EP1
SS3|implements|EP2
SS4|implements|EP3
SS5|implements|EP4
SS6|enables|PF4
SS7|implements|P8
SS8|implements|C5
SS9|implements|C12
M1|mechanism_of|SS2
M2|mechanism_of|SS2
M3|mechanism_of|SS2
M5|mechanism_of|SS2
M6|mechanism_of|SS2
M7|mechanism_of|SS3
M8|mechanism_of|SS3
M10|mechanism_of|SS4
M11|mechanism_of|SS4
M12|mechanism_of|SS4
M14|derives_from|C3
M15|mechanism_of|SS5
M16|mechanism_of|SS5
M17|mechanism_of|SS5
M18|implements|CL12
M20|mechanism_of|SS6
M21|mechanism_of|SS6
M22|mechanism_of|SS6
M23|enables|PF4
M24|mechanism_of|SS7
M25|mechanism_of|SS8
M26|mechanism_of|SS8
M27|mechanism_of|SS9
M28|mechanism_of|SS9
M29|mechanism_of|SS1
EP1|gates|EP2
EP2|gates|EP3
EP3|gates|EP4
SA1|blocked_by|ST18
SA2|blocked_by|ST18
SA3|blocked_by|M24
SA4|blocked_by|M25
SA5|blocked_by|M24
SA6|blocked_by|M24
SA7|mitigated_by|C17
IP1|prereq_of|IP2
IP2|prereq_of|IP3
IP3|prereq_of|IP4
IP4|prereq_of|IP5
LM2|constrains|SS3
LM3|constrains|SS8
D1|instance_of|P1
D4|instance_of|P4
D5|instance_of|P10

# section_index(section|title|ids)
1|Introduction|P1,P7,C1,C2,C3,C7,CL1,CL9
2|Entity - Universal Container|P2,P3,P5,SS1,ST1,C4,C14,C15,M6,M29,D2,D3
3|Execution Path - Funnel Architecture|P4,C7,EP1,EP2,EP3,EP4,EP5
4|State Machines - Pure Topology|SS2,ST2,ST3,ST4,M1,M2,M3,M4,M5,M6
5|Prolog - Declarative Logic|SS3,ST5,ST6,ST7,ST8,C17,M7,M8,M9,D4
6|Utility AI - Multiplicative Scoring|SS4,ST9,ST10,ST11,C11,C16,EN2,EN3,M10,M11,M12,M13,M14
7|Logic Blocks - Stack-Based Bytecode|SS5,ST12,C18,EN5,M15,M16,M17,M18,M19,CL12
8|Parallel Execution - NUMA Threading|SS6,ST13,ST14,ST15,C8,C9,EN4,EN6,M20,M21,M22,M23,P10,D5
9|Scene Isolation and Access Control|SS7,ST16,ST17,P8,P9,C10,C19,M24
10|Network Security - Geometric Input Isolation|SS8,ST18,ST19,ST20,C5,C6,P6,P11,M25,M26,SA1,SA2,SA3,SA4,SA5,SA6,SA7,D6,D10
11|Trace System - Debugging|SS9,ST21,ST22,ST23,C12,C13,M27,M28,D7,CL7
12|Implementation Guide|IP1,IP2,IP3,IP4,IP5,VC1,VC2,VC3,VC4,VC5,VC6,VC7,VC8
13|Performance Characteristics|PF1,PF2,PF3,PF4,PF5,PF6,PF7,PF8,PF9,PF10,CL11
14|Limitations and Future Work|LM1,LM2,LM3,LM4
15|Comparison to Existing Systems|D1,D5,D8,D9
16|Conclusion|CL3,CL5,CL8,CL9

# decode_legend
id_prefixes: P=principle, C=concept, SS=subsystem, ST=structure, EP=execution_pipeline_layer, M=mechanism, SA=security_attack, IP=implementation_phase, PF=performance, LM=limitation, CL=claim, D=distinction, EN=enumeration, VC=validation_check
claim_types: axiom|derivation|observation|prescription|reframe|distinction
rel_types: grounds|enables|requires|implements|prevents|enforces|composes|component_of|mechanism_of|derives_from|gates|blocked_by|mitigated_by|prereq_of|constrains|instance_of
category_values: core|mechanism|security|threading|pattern|debugging|execution|abstraction|scoring
selection_methods: top|weighted_random_top3|random_reasonable
curve_types: Linear|InverseLinear|Quadratic|Exponential|Sigmoid|Boolean|~20+
block_categories: ControlFlow(@1000+)|Statements(@10000+)|Reporters(@1000000+)|Math(@1003000+)|Logic(@1002000+)
memory_domains: NumaNode0-3|GPU|SharedCPU
notation: ~=approximate, →=maps_to/produces, []=array, ?=optional_pointer, fk:=foreign_key_reference
