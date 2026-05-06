# TALL-INFRA DATA-ONLY DEVELOPMENT — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → distinctions → definitions → historical_eras → anti_examples → examples → litmus_test → disciplines → fit → claims → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Zero gameplay types in binary|Compiled code = infrastructure only (SM runners, predicate evaluators, utility scorers, effect processors); binary doesn't know what game it runs
P2|Behavior lives in hot-swappable data tables|SMs, AI curves, logic rules, stat mods, event mappings = table rows; change row = change behavior; no recompile, no restart
P3|Designers invent new mechanics without engineers|Not "tweak values" but "create new systems"; cross-wiring existing tables creates emergent mechanics
P4|Every subsystem consumes same uniform data layout|Rendering, physics, AI, audio, UI, networking, save/load all read same column-oriented tables with FK relationships; no special cases
P5|Marginal cost of new content approaches zero engineering time|1000th behavior set costs same as 10th; complexity constant because interactions are data relationships not code dependencies

# concepts(id|name|category|definition)
C1|Data-driven|historical|Code owns types, data owns numbers; wall between data and behavior preserved
C2|Data-only|core|Binary forgets what a "goblin" is; dataset teaches it every frame; behavior itself becomes data
C3|Tall-infra data-only|core|C2 true across entire vertical stack — renderer to AI to UI to audio — no exceptions
C4|The wall|anti-pattern|Boundary where compiled behavior exists somewhere in binary; moved over decades but never disappeared until data-only
C5|Entity as universal container|pattern|Not a type — uniform struct with optional capability systems; dragon, chair, weather controller, bank account = same struct
C6|State machine as pure topology|pattern|States contain name + behavior set ref + transitions with exit conditions; no behavior code inside; one runner for all domains
C7|Predicate logic as conditions|pattern|Prolog-style rules unified against per-frame fact sets; evaluator doesn't know domain — unifies predicates against facts
C8|Utility AI as behavior scoring|pattern|Behaviors scored not scripted; considerations normalized, curved, multiplied; highest wins; action determined by data refs not compiled code
C9|Logic blocks as effects|pattern|Stack-based bytecode for mutation; runner executes arithmetic + data ops; doesn't know domain
C10|Envelopes as stat transformation|pattern|Time-bounded modifier with curve; processor applies per frame based on elapsed time; stat identity is dataset concern
C11|Semantic repurposing|pattern|Same fields, different meaning via data wiring; health→balance, equipment slot→DB column, combat stats→table statistics
C12|Structured tracing|debugging|Per-entity per-frame decision log; debug in game terms not memory addresses; superior to stack traces
C13|memdb|infrastructure|In-RAM database with O(1) column access; SQLite for persistence not runtime

# distinctions(id|side_a|side_b|key_asymmetry)
D1|Data-driven (code owns types, data owns numbers)|Data-only (binary forgets nouns, dataset teaches each frame)|Wall between data and behavior: present vs eliminated
D2|Tweak values (designer adjusts numbers)|Invent mechanics (designer wires tables to create systems)|Engineering involvement: required vs not required
D3|Type hierarchy (class Dragon : Enemy)|Universal container (same struct, different populated fields)|New entity type: new class vs new row
D4|Imperative conditions (if/else/switch)|Predicate logic (rules unified against facts)|Scalability to multi-entity queries; reusability across domains
D5|Scripted behaviors (code determines action)|Scored behaviors (utility determines action)|Emergence vs authorship; data-only vs compiled
D6|Imperative mutation (direct code writes)|Envelope-based effects (time-bounded curve-driven stat mods)|Automated processing vs manual sequencing
D7|Stack traces (memory addresses)|Structured traces (domain-aware decision queries)|Debugging in code terms vs game terms
D8|Per-project binary (architecture embedded)|Same binary, new dataset (infrastructure reusable)|Multi-project cost: fight old arch vs swap dataset

# definitions(id|term|definition)
DF1|Entity|Universal container struct with optional capability systems; not a type — bag of data references
DF2|State Machine|Graph of named states with conditional transitions; contains no behavior code
DF3|Fact Set|Collection of predicates true for entity this frame; regenerated each update
DF4|Rule|Predicate logic expression (head :- body) evaluated against fact sets
DF5|Consideration|Single input → normalized score via curve; building block of utility AI
DF6|Behavior|Collection of considerations multiplied together; candidate for selection
DF7|Behavior Set|Collection of behaviors; highest score wins
DF8|Logic Block|Stack-based bytecode for data mutation; control flow and arithmetic
DF9|Envelope|Time-bounded stat modifier with curve; automated effect processing
DF10|Trace|Structured log of decisions per entity per frame; domain-aware debugging
DF11|memdb|In-RAM database with O(1) column access; SQLite for persistence

# architecture_stack(id|layer|role|key_property)
AS1|Entity|Universal container|Uniform struct; optional systems; 20+ capability fields; same struct for all object types
AS2|State Machine|Pure topology|Name + behavior_set ref + transitions w/ exit conditions + optional forced actions; one runner for all domains
AS3|Predicate Logic|Industrial-strength conditions|Prolog-style rules; per-frame fact generation; domain-agnostic unification
AS4|Utility AI|Behavior scoring|Considerations: input → normalize → curve → weight → multiply; highest score wins; data refs determine action
AS5|Logic Blocks|Stack-based effects|Bytecode interpreter; arithmetic + data ops; DrGet/DrSet paths; domain-agnostic
AS6|Envelopes|Automated stat transformation|source_entity_id, target_entity_id, stat (i32), modifier, curve, time_start, time_end; processor applies per frame

# historical_eras(id|era|engines|data_was|code_was|wall)
HE1|1990s|Quake, Half-Life|sounds, models, textures|AI routines, weapon behavior, level triggers|yes
HE2|2000s|Unreal, Unity|meshes, prefabs, material params|gameplay classes, damage calcs, quest logic|yes
HE3|2010s|Stingray, Overwatch ECS|entities, component values|AI behaviors, hero abilities, system logic|yes
HE4|2020s|Bevy, Unity DOTS|component columns, archetype defs|systems that process components|yes
# Pattern: wall moved over decades but never disappeared; compiled behavior always present somewhere

# anti_examples(id|system|claim|reality|wall_location)
AE1|Unity ScriptableObjects|Data in SOs = data-driven|class Goblin : MonoBehaviour with Attack() methods still compiled|New enemy types require new classes
AE2|Unreal Data Tables|Data Tables for everything|Damage calcs + quest branches + AI task nodes = Blueprint or C++|New mechanics require new nodes
AE3|Overwatch ECS|Pure ECS, all data in components|Hero-specific systems with compiled logic (Reinhardt charge, Tracer blink, Mercy resurrect)|New heroes require new systems
AE4|Factorio Prototypes|Everything in prototype data|Combat AI, train pathfinding, electric network solving = compiled; prototypes define what exists, code defines how|New transport types require new code

# examples(id|name|what_demonstrates|how)
EX1|Dragon boss in four rows|Full boss via data only|entity row (name+SM ref) + state_machine row (phases) + behavior_set row (attacks) + stat row (health); binary processes generic SM, scores generic behaviors, applies generic envelopes
EX2|Equipment slot as DB column|Semantic repurposing|slot_type=Backpack, world_item_id→bank_balance row, count=balance amount, health_max=insurance cap, health=current coverage; bank UI sums count×value; no code change
EX3|Weather + morale + crafting|Three domains, one runner|Weather (sunny→stormy), morale (confident→broken), crafting (locked→mastered) all use same SM runner + utility scoring; semantics differ by data wiring only

# litmus_test(id|question|fail_means)
LT1|Can designer add "living market economy" without engineering?|Wall present
LT2|Can stat.health be repurposed as "bank account balance" with zero code change?|Wall present
LT3|Can you swap every texture, sound, and behavioral rule while executable runs?|Wall present
LT4|Does compiled binary know any noun (goblin, sword, quest, fireball) exists?|Wall present
# Any "no" = wall present; may be data-driven, not data-only

# disciplines(id|discipline|description)
DS1|Data-relational thinking|Everything is FKs and columns; a "dragon" is a row referencing other rows
DS2|Predicate logic|Conditions are rules unified against facts, not if/else chains
DS3|Utility curve design|Behaviors emerge from scored considerations, not scripted sequences
DS4|Envelope-based effects|Modifications are time-bounded stat transformations, not imperative mutations
DS5|Trace-driven debugging|Problems are queries over decision history, not breakpoints in code

# fit(id|category|context|assessment)
FT1|strong|Live service games with continuous content updates|Marginal content cost → zero
FT2|strong|Multi-SKU studios amortizing infra across projects|Same binary, new dataset
FT3|strong|Heavy modding support|All behavior in swappable tables
FT4|strong|Large content volume (100s enemy types, 1000s items)|Complexity constant
FT5|strong|Long dev cycles where requirements change|No compiled behavior to refactor
FT6|weak|Game jams|No time to build infrastructure
FT7|weak|Prototypes|Exploration over architecture
FT8|weak|Single-ship small team fixed scope|Infrastructure cost not amortized
FT9|weak|Games requiring hand-tuned compiled code paths|Performance ceiling from indirection

# productivity(id|metric|traditional|tall_infra_data_only)
PR1|New enemy type|Code + data + test|Data only
PR2|New mechanic|Design + code + iterate|Data wiring
PR3|Balance pass|Rebuild or hot-reload values|Hot-swap tables
PR4|Multi-project reuse|Fight old architecture|Same binary, new dataset
PR5|Live service patch|Risk regression in compiled behavior|Zero code risk

# performance_notes(id|note)
PN1|Measured: 200 entities × 100 followers × 60fps = 20,000 transforms/frame, unoptimized
PN2|All data in RAM (memdb), O(1) column access
PN3|Prolog unification over small fact sets = cheap; utility scoring = arithmetic; envelope processing = fixed array iteration
PN4|Indirection cost negligible vs rendering and physics
PN5|Optimization target: 10,000+ entities with 100 followers each
PN6|SQLite = persistence layer, not runtime layer; dirty/new rows serialized on demand

# claims(id|type|claim|basis)
CL1|axiom|Binary should contain zero gameplay types — infrastructure only|Eliminates wall between data and behavior
CL2|axiom|Behavior is data, not code|Dataset teaches binary every frame what exists and how things behave
CL3|observation|Every major engine era claimed data-driven while preserving compiled behavior|Historical analysis: Quake through Unity DOTS all have wall
CL4|derivation|Marginal cost of new content → zero engineering time|All semantics in table rows; no code changes for new content
CL5|prescription|All four litmus test questions must pass for data-only qualification|Any "no" = wall present
CL6|observation|20,000 transforms/frame at 60fps unoptimized|Working system, not theoretical
CL7|reframe|Infrastructure cost is front-loaded; productivity multiplier is permanent|Amortization argument for tall-infra investment
CL8|distinction|Data-driven = faster tuning (30 years); data-only = faster content creation|Wall present vs wall eliminated
CL9|axiom|Compiled executable never learns what a dragon is|Runs SMs, evaluates predicates, scores utilities, applies envelopes; dataset is the game

# relationships(from|rel|to)
C1|evolved_into|C2
C2|specialization_of|C3
C4|present_in|C1
C4|absent_from|C2
C4|absent_from|C3
P1|grounds|C2
P2|enables|C11
P3|derives_from|C11
P4|enforces|AS1,AS2,AS3,AS4,AS5,AS6
P5|derives_from|P2
C5|implements|AS1
C6|implements|AS2
C7|implements|AS3
C8|implements|AS4
C9|implements|AS5
C10|implements|AS6
C11|enables|EX2
C11|enables|EX3
C12|implements|D7
C13|enables|PN2
D1|clarifies|CL8
D3|instance_of|P1
D5|instance_of|P2
AE1|violates|P1
AE2|violates|P1
AE3|violates|P1
AE4|violates|P1
HE1|instance_of|C4
HE2|instance_of|C4
HE3|instance_of|C4
HE4|instance_of|C4
EX1|demonstrates|P1
EX2|demonstrates|C11
EX3|demonstrates|P4
LT1|tests|P3
LT2|tests|C11
LT3|tests|P2
LT4|tests|P1
DS1|required_by|C5
DS2|required_by|C7
DS3|required_by|C8
DS4|required_by|C10
DS5|required_by|C12
FT1|benefits_from|P5
FT2|benefits_from|D8
FT6|limited_by|CL7
CL1|grounds|P1
CL2|grounds|P2
CL3|supports|D1
CL4|derives_from|P5
CL9|restates|P1

# section_index(section|title|ids)
1|Core Distinction|C1,C2,C3,D1
2|Historical Context|HE1,HE2,HE3,HE4,C4,CL3
3|Definition: Tall-Infra Data-Only|P1,P2,P3,P4,CL1,CL2,CL5
4|Architecture Stack|AS1,AS2,AS3,AS4,AS5,AS6,C5,C6,C7,C8,C9,C10,C13
5|Dragon Boss Example|EX1
6|Equipment Slot Example|EX2,C11
7|Weather/Morale/Crafting Example|EX3
8|Anti-Examples|AE1,AE2,AE3,AE4
9|Litmus Test|LT1,LT2,LT3,LT4
10|Debugging and Observability|C12,D7,DS5
11|Performance|PN1,PN2,PN3,PN4,PN5,PN6,CL6
12|Productivity Implications|P5,PR1,PR2,PR3,PR4,PR5,CL4,CL7
13|Learning Curve|DS1,DS2,DS3,DS4,DS5
14|When to Use This|FT1,FT2,FT3,FT4,FT5,FT6,FT7,FT8,FT9
15|Conclusion|CL8,CL9
A|Glossary|DF1,DF2,DF3,DF4,DF5,DF6,DF7,DF8,DF9,DF10,DF11

# decode_legend
id_prefixes: P=principle, C=concept, D=distinction, DF=definition, AS=architecture_stack_layer, HE=historical_era, AE=anti_example, EX=example, LT=litmus_test, DS=discipline, FT=fit, PR=productivity, PN=performance_note, CL=claim
claim_types: axiom|derivation|observation|prescription|reframe|distinction
rel_types: evolved_into|specialization_of|present_in|absent_from|grounds|enables|derives_from|enforces|implements|clarifies|instance_of|violates|demonstrates|tests|required_by|benefits_from|limited_by|supports|restates
category_values: core|historical|anti-pattern|pattern|debugging|infrastructure
fit_categories: strong|weak
wall: present|absent — the central diagnostic of the paper; "wall" = compiled behavior existing somewhere in binary
