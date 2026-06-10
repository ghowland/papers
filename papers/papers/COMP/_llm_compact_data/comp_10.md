# TALL-INFRA DATA-ONLY EXECUTION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → stack → wall_history → pipeline → completion_checklist → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Software layer is completable like hardware, not ongoing like applications|Infrastructure is engineering problem not research problem; finite scope defined by maximal requirements domain
P2|All software is data transformation|Every program is a pipeline: data enters, flows through stages, gets transformed, goes somewhere; CPU is data transformation machine (Acton)
P3|Data-only execution eliminates the wall between data and compiled behavior|Binary contains zero domain types, zero behavioral logic; dataset teaches binary everything every frame
P4|Games are maximal requirements domain|Real-time rendering+animation+audio+input+AI+physics+networking+UI simultaneously within 16.67ms frame budget; anything simpler is subset already covered
P5|One and only one implementation per capability|When bug fixed, fixed everywhere permanently; no versions, no APIs, no dependencies; structural guarantee not policy
P6|Scene is application, SceneSet is operating system|Binary is kernel; scenes are processes; SceneSetManager is scheduler+compositor; inter-scene is permission-gated IPC
P7|Field replacement makes architecture domain-independent|Same f32 field labeled health or revenue; same envelope pipeline processes both; semantics entirely in data labels not code
P8|Logic blocks are finite miscellaneous drawer|Like CPU ISA byte-swap instructions; discovered empirically through shipped applications; convergence signal: new primitives per app approaches zero
P9|Three finite engineering layers support two infinite creative layers|Hardware+firmware+software completable; applications+services ongoing forever tied to human goals

# concepts(id|name|category|definition)
C1|The wall|core|Boundary between data and compiled behavior in any system; moved steadily over 30 years but never disappeared until data-only
C2|Data-driven development|distinction|Code owns types, data owns numbers; programmer writes class Sword with compiled attack logic, designer adjusts damage values; wall is present
C3|Data-only execution|core|Binary forgets all domain nouns; dataset defines everything via entity rows referencing state machines, behavior sets, skills, envelopes; wall is absent
C4|Tall-infra|core|The complete data-only infrastructure binary; processes arbitrary data transformations; converges to finished artifact
C5|Field replacement|mechanism|Table remapping field labels to domain terms; scene carries default replacement ID; individual entities can override; character.health.value displays as inside_account.last_month.revenue; zero code change
C6|Scene|runtime|Isolated execution context with own entity pool, state machines, behavior sets, Prolog rules, time tracking, delta time, field_replacement_id
C7|SceneSetItem|runtime|Process container wrapping scene; controls windowing (maximize/minimize/float/z-order/focus), time scaling (update_speed), permissions (read/write scene IDs + paths)
C8|SceneSetManager|runtime|Window manager + process scheduler; manages all active scenes; multiple apps coexist in same binary
C9|SceneToSceneActorClone|mechanism|Cross-scene entity data subscription filtered by path globs at configurable frame rate; enables tools observing running apps without write access
C10|Logic blocks|core|Stack-based bytecode interpreter (~100+ block types); handles ~5% of behavior not fitting standard pipeline; cannot crash (invalid paths → defaults, math clamps/saturates, bounds-checked, fixed I/O types)
C11|Envelope|core|Time-bounded stat modification with curve (attack/sustain/release); DSP metaphor; sword strike, poison, shield buff, healing potion are all parameterizations of same pipeline
C12|Universal container|core|Every entity has same struct; fixed-size fields; domain meaning comes from field replacement labels not compiled types
C13|Completion signal|core|New logic block types per shipped application approaches zero; composition replaces extension; drawer is full; binary scope finalized
C14|Bottom-up development|anti-pattern|Starting from code primitives trying to build toward data flow; pipeline buried under implementation decisions; doesn't scale
C15|Top-down development|core|Start from pipeline: what data enters, what stages, what connections, what comes out; code serves pipeline not reverse

# five_layer_stack(id|layer|status|nature|changes_when)
LS1|Hardware|Done (settled)|Finite engineering|Improvements optional refinements not functional necessities; 2015 server can do everything 2025 server does
LS2|Firmware|Done (settled)|Finite engineering|Changes only when hardware changes
LS3|Software|Completable|Finite engineering|Tall-infra binary has finite scope; can be built, tested, finished, closed
LS4|Applications|Ongoing forever|Infinite creative|Tied to human goals; change daily; datasets interpreted by infrastructure
LS5|Services|Ongoing forever|Infinite creative|Applications that communicate; structurally identical to applications

# wall_history(id|era|data_owned|code_owned|example)
WH1|1990s (Quake, Half-Life)|Textures, sounds, 3D models, level geometry|AI routines, weapon behavior, level triggers|New enemy type → write C, recompile
WH2|2000s (Unreal, Unity)|Meshes, prefabs, material params, editor properties|Gameplay classes, damage calculations, quest logic|New mechanic → write C++/C#, recompile
WH3|2010s (Stingray, Overwatch ECS)|Components as pure data (position, health, velocity)|Systems processing components (hero-specific logic)|New hero → write new system, recompile
WH4|2020s (Bevy, Unity DOTS)|Column-oriented component storage, archetype queries|Systems still compiled Rust/C#|Behavior still in code
WH5|Data-only|Everything: entities, state machines, behaviors, skills, envelopes, field replacements|Nothing domain-specific; only generic infrastructure|New anything → edit dataset, zero recompile

# dsp_pipeline(id|layer|question|function|mechanism)
PL1|State Machine|"What am I doing overall?"|Pure topology: named states with transitions; references behavior set; exit conditions via events, durations, Prolog rules|Determines which behaviors available by selecting active behavior set
PL2|Prolog|"Are preconditions met?"|Predicate logic evaluating rules against facts regenerated every frame from entity state; unification without domain knowledge|Gates behaviors: can_melee requires has_target, distance check, etc.
PL3|Utility AI|"Which behavior scores highest?"|Multiplicative scoring; considerations normalized [0,1] shaped by curves, weighted, multiplied; zero kills entire score (hard gate)|More considerations → lower score but more specific; specificity self-balancing through math
PL4|Logic Blocks|"How do I execute this?"|Stack-based bytecode (~100+ types); reads/writes entity fields via runtime-resolved paths; cannot crash|Handles ~5% not fitting standard flow; miscellaneous drawer
PL5|Envelopes|"Apply stat transformations"|Time-bounded modifications with curves (attack/sustain/release); applies modifier to target stat shaped by curve over duration at tick rate|DSP core: sword=immediate tick, poison=periodic, buff=continuous, potion=instant; same pipeline different params

# data_only_test(id|question|wall_present_if)
DT1|Can designer add living market economy without engineering?|Engineering must write code
DT2|Can stat.health be repurposed as bank_account.balance with zero code change?|Repurposing requires code changes
DT3|Can every texture, sound, and behavioral rule be swapped while executable runs?|Any behavioral change requires recompilation
DT4|Does compiled binary know any domain noun exists?|"goblin," "sword," "quest" appear as types/enums/string comparisons in source

# completion_checklist(id|capability|nature|bounded_why)
CC1|Rendering|Sprite layers, frame sets, bone-point attachments, render layers, camera|Bounded set of 2D operations; 3D extends with more data not more code
CC2|Animation|Frame sequences with events triggering gameplay effects|Content frames in sequence with frame events into envelope pipeline
CC3|Audio|Sounds triggered by state/animation/field changes; spatial; mixing|Bounded operations on audio buffers
CC4|Input|Gamepads, keyboards, mice, touch → input events → entity data paths via binding tables|Pipeline doesn't care what generated event
CC5|UI and Layout|Declarative rules producing positioned sized rectangles; box model; flex/grid; scroll; input routing|What browser layout engine does, as data-driven rules
CC6|Text Editing|Cursor position (i32), selection range (two i32s), keyboard events, multi-line, syntax highlighting, copy/paste|Bounded operations; once implemented covers chat input to code editors
CC7|State Management|State machine evaluation, transitions, forced actions|Core pipeline
CC8|AI Decision-Making|Prolog rules, utility scoring, behavior selection|Core pipeline
CC9|Physics and Collision|Velocity integration, spatial queries, detection and response|Bounded algorithms on entity transform data
CC10|Networking|Fixed-size packets, path-based routing, permission-gated; wire format via logic blocks|Transport is infrastructure; format is data config
CC11|Threading|NUMA-aware work distribution, exclusive entity ranges per thread, barrier sync|No locks, no contention, no shared mutable state during frame
CC12|Serialization|Fixed structs serialize trivially|No object graphs, no pointer chasing, no schema versioning
CC13|Debugging and Tracing|Per-entity per-frame structured traces; all scores with breakdowns; blue/green frame replay|Query in domain terms not memory addresses
CC14|Query and Live Editing|Path-based query against runtime data tree; set statements; auto-refresh|Dev tool and runtime speak same language
CC15|Tooling|Tools are scenes built on same infrastructure they inspect|Running alongside application they observe

# completion_methodology(id|step|purpose)
CM1|Build games first|Games impose maximal requirements; if infra handles real-time action game at 60fps with headroom, handles anything simpler
CM2|Prove generalization (10+ apps across domains)|Each exercises infrastructure in different combinations; reveals missing primitives and boundary cases
CM3|Fix all bugs|Surface area finite; each subsystem bounded; bug count converges to zero
CM4|Verify performance and security|Threading >95% per core; NUMA-aware; geometric security (fixed-shape structs, constrained fields, path-based access); worst case = values clamped, bounded behavior
CM5|Close the binary|Infrastructure complete; instruction set fixed; no more primitives; binary becomes infrastructure like CPU

# security_model(id|property|mechanism)
SM1|Geometric security|Fixed-shape structs, constrained fields, path-based access control
SM2|Worst case bounded|Developer's mistake, designer's error, attacker's packet → values clamped to min/max, processed through pipeline, bounded behavior
SM3|Cannot crash|Invalid paths return defaults; math clamps/saturates; array bounds-checked; fixed I/O types
SM4|Cannot escalate|No pointer sharing; no arbitrary memory access; scene isolation
SM5|Per-infrastructure not per-application|Bug fixed once protects all consumers; one vulnerability surface not thousands

# claims(id|claim|type|depends_on)
CL1|Software layer has a completion condition; like hardware and firmware, it can be built, tested, finished, and closed|axiom|P1,P4
CL2|The wall between data and compiled behavior moved over 30 years but never disappeared until data-only architecture|observation|C1,WH1-WH5
CL3|Data-only is distinct from data-driven; data-driven preserves the wall, data-only eliminates it|distinction|C2,C3,DT1-DT4
CL4|Every item on completion checklist is bounded engineering task; none are open research problems; none grow with application complexity|derivation|CC1-CC15,P4
CL5|The 10,001st application does not change the binary, any more than the 10,001st program changes the x86 instruction set|derivation|P1,CM5
CL6|What requires 20,000 lines of compiled code in traditional engine requires ~500 lines of data configuration in tall-infra|observation|C3,P3
CL7|Dataset failures can be wrong but cannot break; misalignment not crash; debugging via structured trace not stack trace|derivation|C10,SM2,SM3
CL8|The software industry spent 50 years treating a finite problem as infinite because infrastructure and application logic were never separated cleanly|reframe|P1,C1
CL9|Logic block convergence is empirically observable: new primitives per application decays toward zero|observation|C13,P8
CL10|One implementation per capability eliminates dependency hell, version conflicts, per-application vulnerabilities|derivation|P5
CL11|Binary is literally an operating system: kernel=binary, processes=scenes, scheduler=SceneSetManager, IPC=permission-gated cross-scene access|derivation|P6,C6,C7,C8
CL12|Activity that remains after completion is dataset authoring: creative activity tied to human goals, not software development|derivation|P1,LS4,LS5

# rules(id|rule|rationale)
R1|Build games first to discover maximal requirements|Games stress all subsystems simultaneously; anything simpler is subset
R2|Ship multiple apps with zero logic blocks before allowing any|Proves pipeline completeness; forces data-flow thinking; prevents escape hatch dependency
R3|Discover logic block types empirically through shipped apps, not speculatively|Convergence signal observable only through real usage
R4|Field replacement makes any domain accessible with zero code change|Same struct fields serve game and business through labels only
R5|One implementation per capability; when fixed, fixed everywhere permanently|No versions, no APIs, no dependencies; structural guarantee
R6|Close the binary when logic block convergence reaches zero|No more primitives, no more compiled functions; binary is finished infrastructure

# relationships(from|rel|to)
P1|defines|LS3
P2|grounds|P3
P3|eliminates|C1
P4|selects|maximal_requirements
P5|enabled_by|P3
P6|enabled_by|P3
P7|enables|domain_independence
P8|converges_toward|completion
P9|structures|LS1-LS5
C1|present_in|WH1,WH2,WH3,WH4
C1|absent_in|WH5
C2|preserves|C1
C3|eliminates|C1
C4|implements|P3
C5|implements|P7
C6|implements|P6
C7|wraps|C6
C8|manages|C7
C10|handles|remaining_5_percent
C11|core_of|PL5
C12|enables|C5
C13|signals|completion
C14|contrasted_with|C15
PL1|feeds|PL2
PL2|gates|PL3
PL3|selects|PL4
PL4|triggers|PL5
PL5|applies_to|C12
DT1|tests|C3
DT2|tests|C3
DT3|tests|C3
DT4|tests|C3
CM1|prereq_of|CM2
CM2|prereq_of|CM3
CM3|prereq_of|CM4
CM4|prereq_of|CM5
CL1|grounds|P1
CL2|supports|P3
CL4|supports|CL1
CL5|derives_from|CM5
CL8|reframes|software_industry
CL9|supports|P8
CL11|derives_from|P6
SM1|enabled_by|C12
SM2|enabled_by|C10
SM5|enabled_by|P5

# section_index(section|title|ids)
1|The Five-Layer Stack|LS1-LS5,P9
2|All Software Is Data Transformation|P2,C14,C15
3|The Wall|C1,C2,WH1-WH5,CL2
4|Data-Only Execution Defined|P3,C3,DT1-DT4,CL3
5|The DSP Architecture|PL1-PL5,C11
6|Scene as Application, SceneSet as OS|P6,P7,C5,C6,C7,C8,C9,C12,CL11
7|The Completion Checklist|P4,CC1-CC15,CL4
8|Logic Blocks as Miscellaneous Drawer|P8,C10,C13,CL9,R2,R3
9|One and Only One Implementation|P5,CL10,R5
10|The Completion Condition|CM1-CM5,P1,CL1,CL5,R6
11|The End of Software|CL8,CL12,LS1-LS5

# decode_legend
stack_layers: hardware(done)|firmware(done)|software(completable)|applications(ongoing)|services(ongoing)
wall_status: present(code owns verbs)|absent(data owns everything)
pipeline_layers: state_machine→prolog→utility_ai→logic_blocks→envelopes
data_only_vs_data_driven: data-driven=code owns types, data owns numbers; data-only=binary has zero domain types
field_replacement: relabeling universal struct fields to domain terms; zero code change
scene_model: scene=process, SceneSetItem=process container, SceneSetManager=scheduler+compositor
logic_block_convergence: new types per shipped app → 0 = completion signal
security_model: geometric(fixed-shape)|bounded(clamp/saturate)|cannot_crash|cannot_escalate|one_vulnerability_surface
completion_methodology: games_first→generalize(10+ apps)→fix_bugs→verify_perf_security→close_binary
category_values: core|mechanism|runtime|distinction|anti-pattern
claim_types: axiom|derivation|observation|distinction|reframe
rel_types: defines|grounds|eliminates|selects|enabled_by|enables|converges_toward|structures|present_in|absent_in|preserves|implements|wraps|manages|handles|core_of|signals|contrasted_with|feeds|gates|triggers|applies_to|tests|prereq_of|supports|derives_from|reframes
+standalone: this doc self-contained
