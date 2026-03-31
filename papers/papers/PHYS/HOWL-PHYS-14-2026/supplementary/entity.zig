const std = @import("std");
const rl = @import("raylib");

const frame_memory = @import("../../frame_memory.zig");

const prolog = @import("prolog.zig");
const skill_set_lib = @import("skill_set.zig");
const content_item = @import("content_item.zig");

const Text = @import("text.zig").Text;
const TextArray = @import("text_array.zig").TextArray;
const Color = @import("color.zig").Color;
const SkillType = skill_set_lib.SkillType;

// const Body2D = @import("body2d.zig").Body2D;

// Stats and Skills and Perks and Traits are all the same.  We put them in different UI, but putting in different enum-struct means cross-concerns, rather than flat
pub const StatType = enum(i32) {
    None = -1,

    // Base
    XP = 900,
    Level,
    Money,
    Hunger,
    Thirst,
    Heat,

    // Core
    Strength = 1000,
    Agility,
    Wit,
    Awareness,
    Charm,

    // Legacy
    Dexterity = 1990,
    Intelligence,
    Constitution,
    Charisma,

    // Core Play Stats
    Health = 2000,
    Stamina,
    Mana,

    // Combat
    Melee = 3000,
    Ranged,
    Magic,
    Defense,
    Blocking,
    Dodge,

    // Crafting
    Smithing = 4000,
    Alchemy,
    Cooking,
    Engineering,
    Enchanting,
    Tailoring,

    // Survival
    Stealth = 5000,
    Lockpicking,
    Hacking,
    Medicine,
    Hunting,
    Foraging,

    // Social
    Persuasion = 6000,
    Intimidation,
    Deception,
    Leadership,
    Trading,
    Diplomacy,

    // Knowledge
    History = 7000,
    Science,
    Technology,
    Nature,
    Arcane,
    Religion,

    // Specialize
    Driving = 8000,
    Piloting,
    Swimming,
    Climbing,
    Athletics,
    Acrobatics,

    // Elemental
    Fire = 9000,
    Ice,
    Water,
    Lightning,
    Earth,
    Wind,
    Light,
    Dark,
    Poison,
    Physical,

    // Regeneration rates
    REGENERATION = 25000,
    Health_Regen_Rate,
    Stamina_Regen_Rate,
    Mana_Regen_Rate,
};

pub const StatEntry = struct {
    stat_type: StatType = .None, // "strength", "hacking", "one_handed", "crop_rotation"
    value: f32 = 10,
    base_value: f32 = 10,

    // Stat Level and Experience
    level: i32 = 0,
    xp: i32 = 0,
};

pub const Curve = enum(i32) {
    Linear = 0,
    InverseLinear,
    Boolean,
    ExponentialDecay,
    StepFunction,
    EaseIn,
    EaseOut,
    EaseInOut,
    EaseOutIn,
    Quadratic,
    Cubic,
    Quartic,
    Quintic,
    Sine,
    Exponential,
    Logarithmic,
    Circular,
    Back,
    Elastic,
    Bounce,
    Sigmoid,
    InverseQuadratic,
    Logit,
    Threshold,
    NormalDistribution,
};

pub const MusicPlaylist = enum(i32) {
    None = -1,

    // SYSTEM MUSIC
    Startup = 1000,
    Main_Menu,
    Loading,
    Credits,
    Game_Over,

    // CHARACTER/SETUP
    Character_Creation = 2000,
    New_Game,
    Tutorial,
    Intro_Cutscene,
    Prologue,

    // EXPLORATION
    Overworld = 3000,
    Town,
    Village,
    City,
    Wilderness,

    // ENVIRONMENTS
    Forest = 4000,
    Desert,
    Ocean,
    Mountains,
    Cave,

    // LOCATIONS
    Tavern = 5000,
    Shop,
    Temple,
    Castle,
    Dungeon,

    // COMBAT
    Battle = 6000,
    Boss_Fight,
    Final_Boss,
    Victory,
    Defeat,

    // STORY MOMENTS
    Dramatic = 7000,
    Sad,
    Romantic,
    Mysterious,
    Suspenseful,

    // TIME/WEATHER
    Day = 8000,
    Night,
    Dawn,
    Dusk,
    Rainy,

    // SEASONS/EVENTS
    Spring = 9000,
    Summer,
    Autumn,
    Winter,
    Festival,

    // SPECIAL
    Stealth = 10000,
    Chase,
    Puzzle,
    Crafting,
    Peaceful,
};

pub const SFXSet = enum(i32) {
    None = -1,
    Default = 0,

    // MOVEMENT
    Footsteps = 1000,
    Running,
    Jumping,
    Landing,
    Climbing,
    Rolling,
    Sliding,
    Dashing,
    Swimming,
    Crawling,

    // MELEE COMBAT
    Sword_Hit = 2000,
    Blunt_Hit,
    Miss,
    Slash,
    Stab,
    Block,
    Parry,
    Clash, // Weapon on weapon
    Critical,
    Execution,

    // RANGED COMBAT
    Bow_Shot = 3000,
    Bow_Draw,
    Gun_Shot,
    Reload,
    Ricochet,
    Whizz, // Going by your ear
    Empty_Click,
    Shell_Eject,
    Charge_Up,
    Release,

    // IMPACT
    Hit_Light = 4000,
    Hit_Heavy,
    Hit_Flesh,
    Hit_Metal,
    Hit_Stone,
    Hit_Wood,
    Hit_Shield,
    Knockback,
    Knockdown,
    Launch,

    // MAGIC
    Cast_Spell = 5000,
    Magic_Hit,
    Enchant,
    Teleport,
    Summon,
    Buff,
    Debuff,
    Heal,
    Drain,
    Dispel,
    Channel_Loop,
    Channel_End,

    // VOICE
    Grunt = 6000,
    Pain,
    Death_Cry,
    Battle_Cry,
    Taunt,
    Laugh,
    Gasp,
    Cough,
    Cheer,

    // INTERACTIONS
    Door_Open = 7000,
    Door_Close,
    Door_Locked,
    Chest_Open,
    Chest_Close,
    Button_Press,
    Lever_Pull,
    Switch_Toggle,
    Valve_Turn,
    Ladder_Grab,

    // ITEM HANDLING
    Pickup = 8000,
    Drop,
    Equip,
    Unequip,
    Consume,
    Throw,
    Catch,
    Craft,
    Upgrade,
    Discard,

    // DESTRUCTION
    Break = 9000,
    Shatter,
    Explode,
    Crash,
    Collapse,
    Crumble,
    Tear,
    Snap,
    Crush,

    // ENVIRONMENT
    Water_Splash = 10000,
    Water_Submerge,
    Water_Emerge,
    Wind_Blow,
    Fire_Crackle,
    Fire_Ignite,
    Fire_Extinguish,
    Thunder,
    Rain,
    Ice_Crack,
    Lava_Bubble,
    Grass_Rustle,
    Sand_Shift,
    Gravel_Crunch,

    // MECHANICAL
    Engine_Start = 11000,
    Engine_Stop,
    Engine_Loop,
    Gear_Shift,
    Hydraulic,
    Pneumatic,
    Electric_Hum,
    Electric_Spark,
    Conveyor,
    Alarm,

    // UI SOUNDS
    Menu_Select = 12000,
    Menu_Back,
    Menu_Open,
    Menu_Close,
    Notification,
    Error,
    Success,
    Warning,
    Confirm,
    Cancel,
    Tick,
    Tock,

    // CREATURE SOUNDS
    Growl = 13000,
    Roar,
    Chirp,
    Howl,
    Hiss,
    Screech,
    Squawk,
    Buzz,
    Slither,
    Chomp,

    // STATE TRANSITIONS
    Spawn = 14000,
    Despawn,
    Transform,
    Power_Up,
    Power_Down,
    Level_Up,
    Checkpoint,
    Respawn,
    Phase_Shift,

    // MUSICAL/RHYTHM
    Beat_Hit = 15000,
    Beat_Miss,
    Combo_Increment,
    Combo_Break,
    Perfect,
    Multiplier,
};

pub const AudioProfile = struct {
    has_audio_system: bool = false, // If false, dont use these
    sfx_set_name: SFXSet = .None, // References SoundSet by name from audio_manager
    music_playlist: MusicPlaylist = .None, // Music category/playlist name
    volume_modifier: f32 = 1.0,
    pitch_modifier: f32 = 1.0,
    music_auto_start: bool = false, // If true, start the music playlist on Entity start
};

pub const WeatherType = enum(i32) {
    None = -1,
    Clear,
    Sunny,
    Cloudy,
    Overcast,
    Rain,
    Snow,
    Hail,
    LightningStorm,
    Fog,
    Sandstorm,
    Windy,
};

pub const WeatherState = struct {
    has_weather_state: bool = false, // If false, dont use these
    weather_type: WeatherType = .Sunny,
    intensity: f32 = 0.0, // 0.0 to 1.0 - Intensity of Weather: 0.2 Snow = Light.  0.5 Snowing.  0.8 = Snowing hard.  1.0 = Blizzard
    transition_time: f32 = 0.0,
};

pub const ReferenceCategory = enum(i32) {
    None = -1,
    Default = 0,

    // ITEMS
    Inventory = 1000,
    Equipment,
    Weapons,
    Armor,
    Consumables,

    // ABILITIES
    Spells = 2000,
    Skills,
    Talents,
    Perks,
    Abilities,

    // SOCIAL
    Factions = 3000,
    Guilds,
    Organizations,
    Contacts,
    Relationships,

    // PROGRESSION
    Quests = 4000,
    Achievements,
    Objectives,
    Missions,
    Tasks,

    // KNOWLEDGE
    Books = 5000,
    Recipes,
    Blueprints,
    Maps,
    Lore,

    // LOCATIONS
    Areas = 6000,
    Regions,
    Dungeons,
    Buildings,
    Landmarks,

    // CREATURES
    Allies = 7000,
    Enemies,
    Companions,
    Pets,
    Summons,

    // RESOURCES
    Materials = 8000,
    Currency,
    Energy,
    Components,
    Supplies,
};

pub const ReferenceList = struct {
    items: []EntityReference = &[_]EntityReference{}, // Entity.id lookup
    counts: []i32 = &[_]i32{},
    category: ReferenceCategory = .None, // "inventory", "spells", "factions", "quests", etc.
};

pub const Requirements = struct {
    has_requirements: bool = false, // If false, dont use these
    min_level: i32 = -1,
    required_stats: []StatEntry = &[_]StatEntry{},
    required_items: ReferenceList = .{},
    required_quests: ReferenceList = .{},
    required_factions: ReferenceList = .{},
    forbidden_quests: ReferenceList = .{},
    forbidden_factions: ReferenceList = .{},
};

pub const Range = struct {
    has_range: bool = false, // If false, dont use these
    min_value: f32 = 0.0,
    max_value: f32 = 0.0,
    radius: f32 = 0.0,
};

pub const NeedType = enum(i32) {
    None = -1,

    // SURVIVAL NEEDS
    Water = 1000,
    Food,
    Air,
    Sleep,
    Shelter,

    // HEALTH NEEDS
    Healing = 2000,
    Medicine,
    Rest,
    Warmth,
    Cleanliness,

    // PLANT NEEDS
    Fertilizer = 3000,
    Sunlight,
    Nutrients,
    Pruning,
    Watering,

    // SOCIAL NEEDS
    Companionship = 4000,
    Communication,
    Affection,
    Recognition,
    Belonging,

    // MENTAL NEEDS
    Stimulation = 5000,
    Entertainment,
    Learning,
    Purpose,
    Achievement,

    // SAFETY NEEDS
    Security = 6000,
    Protection,
    Stability,
    Comfort,
    Privacy,

    // ENERGY NEEDS
    Fuel = 7000,
    Power,
    Charge,
    Maintenance,
    Repair,

    // SPIRITUAL NEEDS
    Faith = 8000,
    Ritual,
    Meditation,
    Connection,
    Transcendence,
};

pub const BenefitType = enum(i32) {
    None = -1,

    // PHYSICAL BENEFITS
    Health = 1000,
    Stamina,
    Strength,
    Speed,
    Endurance,

    // GROWTH BENEFITS
    Growth = 2000,
    Size_Increase,
    Development,
    Maturation,
    Evolution,

    // MENTAL BENEFITS
    Mood = 3000,
    Focus,
    Intelligence,
    Memory,
    Clarity,

    // PERFORMANCE BENEFITS
    Efficiency = 4000,
    Productivity,
    Skill_Gain,
    Experience,
    Learning_Rate,

    // SOCIAL BENEFITS
    Charisma = 5000,
    Reputation,
    Influence,
    Leadership,
    Popularity,

    // MAGICAL BENEFITS
    Mana = 6000,
    Magic_Power,
    Spell_Efficiency,
    Enchantment,
    Arcane_Insight,

    // COMBAT BENEFITS
    Damage = 7000,
    Defense,
    Critical_Chance,
    Accuracy,
    Reflexes,

    // UTILITY BENEFITS
    Longevity = 8000,
    Resistance,
    Immunity,
    Regeneration,
    Adaptation,
};

pub const PenaltyType = enum(i32) {
    None = -1,

    // HEALTH PENALTIES
    Health_Loss = 1000,
    Weakness,
    Fatigue,
    Sickness,
    Pain,

    // SEVERE PENALTIES
    Death = 2000,
    Unconsciousness,
    Coma,
    Paralysis,
    Collapse,

    // PLANT PENALTIES
    Wilting = 3000,
    Browning,
    Stunted_Growth,
    Leaf_Drop,
    Root_Rot,

    // MENTAL PENALTIES
    Confusion = 4000,
    Depression,
    Anxiety,
    Madness,
    Memory_Loss,

    // PERFORMANCE PENALTIES
    Slowdown = 5000,
    Clumsiness,
    Reduced_Accuracy,
    Skill_Loss,
    Inefficiency,

    // SOCIAL PENALTIES
    Isolation = 6000,
    Aggression,
    Antisocial,
    Reputation_Loss,
    Hostility,

    // MAGICAL PENALTIES
    Mana_Drain = 7000,
    Spell_Failure,
    Magic_Block,
    Curse,
    Corruption,

    // SYSTEM PENALTIES
    Malfunction = 8000,
    Shutdown,
    Overheating,
    Power_Loss,
    System_Failure,
};

pub const NeedEntry = struct {
    need_type: NeedType = .None, // "water", "food", "healing", "fertilizer", "sleep"
    current_level: f32 = 1.0, // 0.0 = critical, 1.0 = satisfied
    max_level: f32 = 1.0, // Maximum satisfaction level
    decay_rate: f32 = 0.0, // How fast this depletes (per hour/day)
    critical_threshold: f32 = 0.2, // Below this = urgent
    satisfaction_benefit: BenefitType = .None, // "growth", "health", "stamina", "mood"
    benefit_magnitude: f32 = 1.0, // How much benefit when satisfied

    // Timing
    last_satisfied: f32 = 0.0, // Game time when last fulfilled
    next_required: f32 = 0.0, // When this will be critical
    frequency: f32 = 24.0, // Hours between requirements

    // Consequences
    depletion_penalty: PenaltyType = .None, // "health_loss", "death", "wilting"
    penalty_magnitude: f32 = 0.0, // How severe the penalty
};

pub const BiologicalNeeds = struct {
    has_needs: bool = false,

    // SM+Rules for condition states
    condition_state_machine_id: i32 = -1, // "healthy" -> "hungry" -> "starving" -> "dying"
    current_condition_states: EntityStateList = .{}, // Multiple simultaneous conditions

    // Supporting fields (existing)
    needs: []NeedEntry = &[_]NeedEntry{},
    active_needs_count: i32 = 0,
    metabolism_rate: f32 = 1.0,
    stress_level: f32 = 0.0,
    environment_modifier: f32 = 1.0,
};

// === GROUPED SYSTEM STRUCTS ===

pub const MaterialType = enum(i32) {
    None = -1,

    // METALS
    Steel = 1000,
    Iron,
    Bronze,
    Copper,
    Silver,

    // ORGANIC
    Flesh = 2000,
    Bone,
    Leather,
    Cloth,
    Fur,

    // NATURAL
    Wood = 3000,
    Stone,
    Crystal,
    Ice,
    Sand,

    // LIQUIDS
    Water = 4000,
    Oil,
    Blood,
    Acid,
    Lava,

    // SYNTHETIC
    Plastic = 5000,
    Rubber,
    Glass,
    Ceramic,
    Concrete,

    // MAGICAL
    Energy = 6000,
    Ethereal,
    Void,
    Light,
    Shadow,

    // ELEMENTAL
    Fire = 7000,
    Electric,
    Poison,
    Radioactive,
    Cursed,

    // SPECIAL
    Adamantine = 8000,
    Mithril,
    Obsidian,
    Diamond,
    Enchanted,
};

pub const ItemProperties = struct {
    has_item_properties: bool = false,

    // Skill this Item uses
    skill_type: SkillType = .None,
    skill_level: i32 = 0,
    required_skill: SkillType = .None, // Entity must have this skill level to use item
    required_skill_level: i32 = 0, // Entity must have this skill level to use item

    // Secondary Skill: By default this would be 2 effects, but it could also be a secondary effect like M4/M249
    secondary_skill_type: SkillType = .None,
    secondary_skill_level: i32 = 0,
    secondary_always_applied: bool = true,

    // Supporting fields
    weight: f32 = 0.0,
    value: f32 = 0,
    health: f32 = 100,
    rarity: f32 = 1,
    shop_category_id: i32 = -1,
    vendor_flags: f32 = 0,
    for_quest_id: i32 = -1,
    material: MaterialType = .None,

    // SM+Rules for condition degradation
    condition_state_machine_id: i32 = -1, // "pristine" -> "good" -> "worn" -> "damaged" -> "broken"
    current_condition_state: Text = Text.initEmpty(),

    // SM+Rules for rarity evolution
    rarity_state_machine_id: i32 = -1, // "common" -> "uncommon" -> "rare" -> "legendary"
    current_rarity_state: Text = Text.initEmpty(),

    // Condition tracking
    repair_count: i32 = 0,
    enchantment_level: i32 = 0,
};

// For Items and things like that.  Not for Actors
pub const CombatCapabilities = struct {
    has_combat_capabilities: bool = false, // If false, dont use these
    damage: f32 = 0, // Harm potential
    armor_rating: f32 = 0, // Protection value
    attack_speed: f32 = 1.0, // Speed of offensive actions
    range: Range = Range{}, // Distance capabilities
    critical_chance: f32 = 0.0, // Probability of exceptional success
    critical_multiplier: f32 = 1.0, // Magnitude of exceptional success
    resistances: []StatEntry = &[_]StatEntry{}, // Resistance to damage types, effects
};

pub const Communication = struct {
    has_communication: bool = false, // If false, dont use these
    dialogue_tree_id: i32 = -1, // Interactive conversation system
    readable_text_id: i32 = -1, // Static text content
    voice_type_id: i32 = -1, // Audio characteristics
};

pub const EffectType = enum(i32) {
    None = -1,

    // HEALING
    Heal = 1000,
    Regenerate,
    Revive,
    Cure,
    Restore,

    // DAMAGE
    Damage = 2000,
    Poison,
    Burn,
    Freeze,
    Shock,

    // MOVEMENT
    Teleport = 3000,
    Knockback,
    Pull,
    Slow,
    Haste,

    // BUFFS
    Buff = 4000,
    Strengthen,
    Protect,
    Enhance,
    Empower,

    // DEBUFFS
    Debuff = 5000,
    Weaken,
    Blind,
    Stun,
    Silence,

    // TRANSFORMATION
    Transform = 6000,
    Mutate,
    Shapeshift,
    Resize,
    Phase,

    // CONTROL
    Charm = 7000,
    Fear,
    Confuse,
    Sleep,
    Paralyze,

    // TECHNOLOGY
    Hack = 8000,
    Override,
    Scramble,
    Reboot,
    Virus,

    // UTILITY
    Illuminate = 9000,
    Detect,
    Summon,
    Banish,
    Dispel,
};

pub const TargetFilter = enum(i32) {
    None = -1,

    // SELF TARGETING
    Self = 1000,
    SelfArea,
    SelfChain,

    // ALLY TARGETING
    Ally = 2000,
    AllAllies,
    AllyArea,
    AllyChain,
    Party,

    // ENEMY TARGETING
    Enemy = 3000,
    AllEnemies,
    EnemyArea,
    EnemyChain,
    Hostile,

    // UNIVERSAL TARGETING
    All = 4000,
    Everyone,
    Everything,
    AllArea,
    Global,

    // TYPE FILTERING
    Organic = 5000,
    Undead,
    Mechanical,
    Elemental,
    Construct,

    // CONDITION FILTERING
    Living = 6000,
    Dead,
    Wounded,
    Healthy,
    Cursed,

    // RELATIONSHIP FILTERING
    Neutral = 7000,
    Friendly,
    Unfriendly,
    Unknown,
    Faction,

    // DISTANCE FILTERING
    Nearest = 8000,
    Farthest,
    InRange,
    OutOfRange,
    Adjacent,
};

pub const ActionEffect = struct {
    effect_type: EffectType = .None, // "heal", "damage", "teleport", "buff", "hack", "mutate"
    magnitude: f32 = 0.0,
    area: f32 = 0,
    duration: f32 = 0,
    cost: f32 = 0.0,
    target_filter: TargetFilter = .None, // "self", "enemy", "ally", "all", "undead", "organic"
};

pub const EffectsEngine = struct {
    has_effects_engine: bool = false,

    // SM+Rules for status effect chains
    status_state_machine_ids: []i32 = &[_]i32{}, // Multiple active status effects
    current_status_states: EntityStateList = .{}, // "poisoned_light" -> "poisoned_severe" -> "dying"

    // Supporting fields
    action_effects: []ActionEffect = &[_]ActionEffect{},
    stat_modifiers: []StatEntry = &[_]StatEntry{},

    // Effect tracking
    effect_durations: []f32 = &[_]f32{},
    effect_stacks: []i32 = &[_]i32{}, // Stack counts for stackable effects
};

pub const AIBehavior = struct {
    has_ai_behavior: bool = false,

    // SM+Rules for behavioral states (different from entity.state_machine_id)
    behavior_state_machine_id: i32 = -1, // "passive" -> "alert" -> "aggressive" -> "fleeing"
    current_behavior_state: Text = Text.initEmpty(),

    // SM+Rules for morale/panic
    morale_state_machine_id: i32 = -1, // "confident" -> "shaken" -> "panicked" -> "routing"
    current_morale_state: Text = Text.initEmpty(),

    // Supporting fields
    ai_stats: []StatEntry = &[_]StatEntry{},
    max_movement_speed: f32 = 0.0,

    // Behavior tracking
    behavior_triggers: []i32 = &[_]i32{}, // What events triggered behavior change
    last_behavior_change_time: f32 = 0,
};

pub const VisualEffect = enum(i32) {
    None = -1,

    // PARTICLE EFFECTS
    Sparks = 1000,
    Smoke,
    Fire,
    Steam,
    Dust,

    // LIGHTING EFFECTS
    Glow = 2000,
    Flash,
    Flicker,
    Pulse,
    Strobe,

    // MOVEMENT EFFECTS
    Shake = 3000,
    Wobble,
    Float,
    Rotate,
    Bounce,

    // WEATHER EFFECTS
    Rain_Drops = 4000,
    Snow_Fall,
    Wind_Sway,
    Lightning,
    Fog_Drift,

    // MAGIC EFFECTS
    Sparkle = 5000,
    Energy_Aura,
    Portal,
    Teleport_Flash,
    Magic_Circle,

    // WATER EFFECTS
    Ripples = 6000,
    Splash,
    Bubbles,
    Wave,
    Drip,

    // DESTRUCTION EFFECTS
    Explosion = 7000,
    Shatter,
    Crack,
    Crumble,
    Burn,

    // STATUS EFFECTS
    Poison_Cloud = 8000,
    Heal_Aura,
    Shield_Barrier,
    Speed_Trail,
    Frozen_Ice,

    // TILE EFFECTS
    Animated_Tile = 9000,
    Color_Shift,
    Transparency,
    Distortion,
    Overlay,
};

pub const LightingEffect = enum(i32) {
    None = -1,
};

pub const VisualType = enum(i32) {
    None = -1,
    Game, // Entity Pos is in the gameworld
    Canvas, // Entity Pos is 0-1 percent of Canvas
    UI, // Entity Pos is Window pixel
};

pub const VisualSystem = struct {
    visual_type: VisualType = .Game,

    // Content Import ID: Sprites
    content_import_id: i32 = -1,

    // Animation independence
    animation: content_item.ContentAnimation = .None,
    anim_time_start: f32 = 0, // Time we started this animation
    cur_frame: i32 = 0,
    cur_event: content_item.ContentEventType = .None,
    cur_event_handled: bool = false,

    // Our Next Animation, planned
    next_animation: content_item.ContentAnimation = .None,
    next_anim_time_start: f32 = 0, // Time to start the next animation, can include offset from Leader/others, and can be unique animations

    // Canvas or GameRect index, based on `visual_type`
    rect_index: i32 = -1,

    color_tint: Color = Color.WHITE, // Color modification
    visual_effect: VisualEffect = .None, // Special visual effect system //TODO: Can this become an enum?  What should this be?
    light_effect: LightingEffect = .None, // Illumination characteristics
    icon_id: i32 = 0, // UI icon identifier

    // Selection of the visual area
    can_select: bool = true,
    can_move: bool = true,
    can_resize: bool = true,
    is_moving: bool = false,
    is_resizing: bool = false,

    // Procedural material rendering
    global_material_seed: i32 = 0,
};

pub const AccessControl = struct {
    has_access_control: bool = false,

    // SM+Rules for permission chains
    access_state_machine_id: i32 = -1, // "locked" -> "key_found" -> "unlocked" -> "master_access"
    current_access_state: Text = Text.initEmpty(),

    // Supporting fields
    use_requirements: Requirements = Requirements{},
    ownership_entity_id: i32 = -1,
    faction_relations: []StatEntry = &[_]StatEntry{},

    // Track access history
    access_attempts: i32 = 0,
    last_access_time: f32 = 0,
};

pub const EventType = enum(i32) {
    None = -1,

    // PLAYER EVENTS
    Player_Death = 1000,
    Player_Level_Up,
    Player_Spawn,
    Player_Respawn,
    Player_Teleport,

    // COMBAT EVENTS
    Combat_Start = 2000,
    Combat_End,
    Entity_Death,
    Entity_Damage,
    Critical_Hit,

    // ITEM EVENTS
    Item_Pickup = 3000,
    Item_Drop,
    Item_Use,
    Item_Break,
    Item_Craft,

    // QUEST EVENTS
    Quest_Start = 4000,
    Quest_Complete,
    Quest_Fail,
    Objective_Complete,
    Objective_Update,

    // DIALOGUE EVENTS
    Dialogue_Start = 5000,
    Dialogue_End,
    Choice_Made,
    Relationship_Change,
    Faction_Change,

    // WORLD EVENTS
    Door_Open = 6000,
    Door_Close,
    Lever_Pull,
    Button_Press,
    Trap_Trigger,

    // ENVIRONMENT EVENTS
    Weather_Change = 7000,
    Day_Night_Cycle,
    Season_Change,
    Area_Enter,
    Area_Exit,

    // AUDIO EVENTS
    Music_Start = 8000,
    Music_Stop,
    Sound_Play,
    Voice_Play,
    Audio_Fade,

    // UI EVENTS
    Menu_Open = 9000,
    Menu_Close,
    Inventory_Open,
    Map_Open,
    Settings_Open,

    // SAVE EVENTS
    Game_Save = 10000,
    Game_Load,
    Checkpoint_Reach,
    Auto_Save,
    Quick_Save,

    // CUTSCENE EVENTS
    Cutscene_Start = 11000,
    Cutscene_End,
    Camera_Change,
    Animation_Start,
    Animation_End,

    // SYSTEM EVENTS
    Game_Pause = 12000,
    Game_Resume,
    Game_Quit,
    Level_Load,
    Level_Unload,
};

pub const EntityTimerType = enum(i32) {
    None = -1, // Unspecified
    WallTime, // Real world time
    GameTime, // Game time (can be speed up, or reversed)
};

pub const EntityTimer = struct {
    has_timer: bool = true, // If false, dont use these

    // Is this Timer running?
    is_active: bool = false,

    time_type: EntityTimerType = .WallTime,

    // Time to start, can be in the future
    time_started: f32 = 0.0,

    // How long to last, determines length
    duration: f32 = 0.0,
    duration_input: f32 = 0.0, // Don't change the current duration while we are doing the timer, so store it here if taking user input

    // We track deltaTime accruing here, when >= duration, the timing is done
    elapsed: f32 = 0.0,

    // Visualization
    text_current: Text = Text.initEmpty(),
    text_default: Text = Text.initEmpty(),
    font_id: i32 = 0,
    font_name: Text = Text.initEmpty(),
    font_size: i32 = 500,
    font_color: Color = .{},

    // Simple alarm selection
    //TODO: Move to Event later, but this is good for now for FTT migration
    alarm_id: i32 = 0,

    // If not None, the Entity will process this event after the timer
    event_on_complete: EventType = .None,

    // If not -1, this will execute the specific logic block, on complete
    execute_logic_block_id: i32 = -1,
};

pub const TemporalSystem = struct {
    // SM+Rules for lifecycle stages
    lifecycle_state_machine_id: i32 = -1, // "seed" -> "sprout" -> "mature" -> "fruit" -> "dead"
    current_lifecycle_state: Text = Text.initEmpty(),

    // SM+Rules for seasonal behavior
    seasonal_state_machine_id: i32 = -1, // "spring_active" -> "summer_bloom" -> "fall_harvest" -> "winter_dormant"
    current_seasonal_state: Text = Text.initEmpty(),

    // Supporting fields
    creation_time: f32 = 0.0,
    expiration_time: f32 = 0.0,

    // Lifecycle tracking
    age: f32 = 0,
    lifecycle_stage_duration: f32 = 0,
};

pub const EventSystemItem = struct {
    event: EventType = .None,
    exec_logic_block_id: i32 = -1,
};

pub const EventSystem = struct {
    // If not None, this Event will be processed soon.  We check after each subsystem is run, but handle them generically, so each could have another event in a frame and we handle them all soon
    to_process: content_item.ContentEventType = .None,

    //TODO: Turn this into like 10 events, and thats how many a entity can handle in a single frame, good enough to start and keeps this simple
    events: []EventSystemItem = &[_]EventSystemItem{},
};

pub const PowerSourceType = enum(i32) {
    None = -1,

    // MANUAL POWER
    Manual = 1000,
    HandCrank,
    Pedal,
    Lever,
    Muscle,

    // FUEL BASED
    Wood = 2000,
    Coal,
    Oil,
    Gas,
    Alcohol,

    // ELECTRICAL
    Battery = 3000,
    Generator,
    Solar,
    Wind,
    Water,

    // MAGICAL
    Mana = 4000,
    Crystal,
    Essence,
    Ley_Line,
    Ritual,

    // BIOLOGICAL
    Blood = 5000,
    Life_Force,
    Soul,
    Breath,
    Heat,

    // NUCLEAR
    Uranium = 6000,
    Plutonium,
    Fusion,
    Antimatter,
    Plasma,

    // EXOTIC
    Void = 7000,
    Time,
    Gravity,
    Quantum,
    Dimensional,

    // HYBRID
    Steam = 8000,
    Combustion,
    Kinetic,
    Thermal,
    Magnetic,
};

pub const EnvironmentalSystem = struct {
    has_environmental: bool = false,

    // SM+Rules for weather transitions
    weather_state_machine_id: i32 = -1, // "clear" -> "cloudy" -> "rain" -> "storm" -> "clear"
    current_weather_state: Text = Text.initEmpty(),

    // Supporting fields
    weather_effects: WeatherState = WeatherState{},
    weather_resistance: []StatEntry = &[_]StatEntry{},
    temperature_effects: Range = Range{},

    // Weather tracking
    weather_duration: f32 = 0,
    next_weather_change: f32 = 0,
};

pub const EntitySkill = struct {
    skill: SkillType = .None,

    // Allow upgrading
    level: i32 = 0,
    xp: i32 = 0,
};

pub const SkillSystem = struct {
    has_skills: bool = false,

    // Skill Tree is SM: game.state_machine.id, used for data-only rules for when upgrades can happen, and what the path of progression is
    skill_tree_state_machine_id: i32 = -1, //

    // Base Skills, that are more general case
    skill_set_id: i32 = -1,

    // Unlocked skills
    skills: []EntitySkill = &[_]EntitySkill{},

    // Supporting fields
    skill_points_available: i32 = 0,
    skill_points_spent: i32 = 0,
};

pub const SocialClass = enum(i32) {
    None = -1,

    // LOWER CLASS
    Slave = 1000,
    Serf,
    Peasant,
    Laborer,
    Servant,

    // WORKING CLASS
    Craftsman = 2000,
    Merchant,
    Trader,
    Artisan,
    Shopkeeper,

    // MIDDLE CLASS
    Citizen = 3000,
    Professional,
    Scholar,
    Clerk,
    Officer,

    // UPPER CLASS
    Wealthy = 4000,
    Elite,
    Aristocrat,
    Gentry,
    Landowner,

    // NOBILITY
    Knight = 5000,
    Baron,
    Count,
    Duke,
    Prince,

    // ROYALTY
    King = 6000,
    Queen,
    Emperor,
    Empress,
    Monarch,

    // RELIGIOUS
    Priest = 7000,
    Bishop,
    Cardinal,
    Pope,
    Oracle,

    // SPECIAL
    Outcast = 8000,
    Criminal,
    Exile,
    Refugee,
    Nomad,
};

pub const CulturalSignificance = enum(i32) {
    None = -1,

    // MUNDANE
    Common = 1000,
    Everyday,
    Ordinary,
    Trivial,
    Disposable,

    // PERSONAL
    Sentimental = 2000,
    Family_Heirloom,
    Personal_Item,
    Memento,
    Keepsake,

    // CULTURAL
    Traditional = 3000,
    Ceremonial,
    Ritual_Item,
    Cultural_Symbol,
    Ethnic_Artifact,

    // RELIGIOUS
    Blessed = 4000,
    Holy,
    Sacred,
    Divine,
    Consecrated,

    // HISTORICAL
    Antique = 5000,
    Historical,
    Ancient,
    Archaeological,
    Legendary,

    // POLITICAL
    Royal = 6000,
    State_Symbol,
    Crown_Jewel,
    Diplomatic_Gift,
    Treaty_Item,

    // MYSTICAL
    Cursed = 7000,
    Enchanted,
    Magical,
    Prophetic,
    Forbidden,

    // ULTIMATE
    Relic = 8000,
    Artifact,
    Wonder,
    Mythical,
    World_Changing,
};

pub const SocialSystem = struct {
    has_social_system: bool = false,

    // SM+Rules for relationship progression
    relationship_state_machine_ids: []i32 = &[_]i32{}, // Per faction/character
    current_relationship_states: EntityStateList = .{}, // "stranger" -> "acquaintance" -> "friend" -> "ally"

    // Supporting fields
    reputation_modifier: f32 = 0,
    social_class: SocialClass = .None,
    cultural_significance: CulturalSignificance = .None,

    // Track relationship history
    relationship_events: []i32 = &[_]i32{}, // Event IDs that changed relationships
    faction_standings: []StatEntry = &[_]StatEntry{}, // Reputation values
};

pub const QuestSystem = struct {
    has_quest_system: bool = false,

    // Quest chains are StateMachines
    active_quest_state_machine_ids: []i32 = &[_]i32{},

    // Current states per quest
    current_quest_states: EntityStateList = .{}, // "meet_king", "find_artifact"

    // Supporting fields
    quest_flags: f32 = 0,
    stage_requirements: f32 = 0,
    script_events: ReferenceList = ReferenceList{},
    event_handlers: ReferenceList = ReferenceList{},
    trigger_conditions: Requirements = Requirements{},
};

pub const EntityState = struct {
    name: Text = Text.initEmpty(),
};

pub const EntityStateList = struct {
    items: []EntityState = &[_]EntityState{},
};

pub const DialogueSystem = struct {
    has_dialogue: bool = false,

    // Dialogue trees are StateMachines
    dialogue_state_machine_id: i32 = -1,

    // Current dialogue state
    current_dialogue_state: Text = Text.initEmpty(), // "greeting", "ask_about_goods"

    // Supporting fields
    dialogue_history: EntityStateList = .{}, // States visited this conversation
};

pub const CraftingSystem = struct {
    has_crafting: bool = false,

    // Recipe unlock tree is StateMachine
    recipe_tree_state_machine_id: i32 = -1,

    // Unlocked recipes = current states
    unlocked_recipe_states: EntityStateList = .{}, // "iron_sword", "steel_sword"

    // Supporting fields (already exists)
    crafting_components: ReferenceList = ReferenceList{},
    crafting_recipes: ReferenceList = ReferenceList{},
    durability_loss_rate: f32 = 0.0,
    enchantment_capacity: f32 = 0,
    tech_level: f32 = 1,
    power_source: PowerSourceType = .None,
};

pub const NetworkSystem = struct {
    has_network: bool = false, // If false, dont use these
    network_id: i32 = 0, // Unique network identifier
    sync_flags: f32 = 0, // What properties need synchronization
    authority_entity_id: i32 = -1, // Who controls this object
};

pub const MetaSystem = struct {
    tags: ReferenceList = ReferenceList{}, // Categorization, filtering, searching
    sort_priority: f32 = 0, // How this appears in lists
    accessibility_flags: f32 = 0, // Screen reader, colorblind support
};

pub const TransportSystem = struct {
    has_transport: bool = false,

    // SM+Rules for training/upgrade paths
    training_state_machine_id: i32 = -1, // "wild" -> "tamed" -> "trained" -> "mastered"
    current_training_state: Text = Text.initEmpty(),

    // SM+Rules for upgrade paths
    upgrade_state_machine_id: i32 = -1, // "basic" -> "reinforced" -> "enhanced" -> "legendary"
    current_upgrade_states: EntityStateList = .{},

    // Supporting fields
    vehicle_properties: []StatEntry = &[_]StatEntry{},

    // Training tracking
    training_points: i32 = 0,
    loyalty: f32 = 0,
};

// Tracking Entities for Awareness
pub const TrackEntity = struct {
    entity_id: i32 = -1, // Who/what this entity is focusing on
    entity_follower_index: i32 = -1, //
    distance: f32 = 0.0, // Distance to the target from Entity

    facing_direction: rl.Vector2 = .{},

    last_strike_time: f32 = 0, // Last time we attacked them and hit
    last_hit_time: f32 = 0, // Last time they hit us
    last_miss_time: f32 = 0, // Last time they tried to hit us, and missed
};

pub const AwarenessSystem = struct {
    // Update Rate
    last_updated: f32 = 0,
    update_delay: f32 = 0.2, // seconds

    // Pos as Target
    has_pos_target: bool = false, // Do we have somewhere to go?
    target_pos: rl.Vector2 = rl.Vector2{ .x = 0, .y = 0 }, // Where this entity wants to move

    // Stats
    awareness_radius: f32 = 200.0, // How far this entity can "see"
    front_arc_angle: f32 = 1.57, // Front awareness arc (90 degrees in radians)

    // Distances
    distance_melee: f32 = 50, // Melee is the outside
    distance_ranged: f32 = 170, // Range is the inside
    distance_target: f32 = 2000, // Range to pick a target

    // Search Prolog Ruleset
    search_target_prolog_rule_set_id: i32 = -1,

    // We want to attack this Entity
    target_entity_id: i32 = -1,
    target_entity_dist: f32 = std.math.floatMax(f32), // Distance to the target from Entity

    // We previously attacked this one.  Knowing this stops ping-ponging between 2
    target_entity_last_id: i32 = -1,

    // We want to walk to this entity
    destination_actor_id: i32 = -1,
    destination_actor_dist: f32 = std.math.floatMax(f32),

    // Closest Actor and "Human" in total
    closest_actor_id: i32 = -1,
    closest_actor_dist: f32 = std.math.floatMax(f32),

    closest_human_id: i32 = -1,
    closest_human_dist: f32 = std.math.floatMax(f32),

    // Closest Actor and Human in front of us
    closest_actor_front_id: i32 = -1,
    closest_actor_front_dist: f32 = std.math.floatMax(f32),

    closest_human_front_id: i32 = -1,
    closest_human_front_dist: f32 = std.math.floatMax(f32),

    // Who attacked us last?
    last_attacked_id: i32 = -1,
};

pub const EntityActorType = enum(i32) {
    None = -1,
    Player,

    HOSTILE = 10000,
    Monster,
    MonsterCaptain,
    MonsterBoss,
    MonsterBossMini,

    // Different NPC types that will have their own State Machine assignments by Type
    NEUTRAL = 20000,
    Civilian,
    Guard,
    Important,
    Aristocrat,

    FRIENDLY = 30000,
    Companion,
    Pet,
};

pub const EntityType = enum(i32) {
    None = -1, // Will not do anything in the scene, is removed from "Release" scenes, but kept in "Debug" scenes, and can fill in notes and generics (size), and later change their type and fill in data
    Actor, // Actors live in the world, and have a body, but may not collide with anything, and may be kinetic instead of dynamic
    Terrain, // Actors walk on this, and there can be levels to it.  Also, we paint with a LayerPalette, because in one game we had 72 levels have have different palettes (snow, ocean, house) and auto-tiles (beach, city street, dirt road, river bacnd, forest path)

    //
    UI = 5000,
    UiText,
    UiImage,

    // Spatial
    SPATIAL = 9000,
    Building,
    Room,

    // Physical Objects
    PHYSICAL = 10000,
    Container, // Chests, drawers, pockets - has inventory system, can be locked, trapped, hidden, or require tools to open
    Pickup, // Items that can be collected into inventory - coins, keys, food, weapons, tools, books, quest items
    Furniture, // Tables, chairs, beds - can be interacted with (sit, sleep, hide under), may have attached containers
    Door, // Portals between areas - can be locked, require keys, have different open/close states, connect to other doors
    Window, // Visual barriers that can be broken, climbed through, or provide line of sight without passage
    Lever, // Mechanical switches that change world state - open doors, move platforms, activate traps, control lights
    Button, // Pressure or touch activated triggers - floor plates, wall buttons, can be temporary or permanent activation
    Rope, // Climbable connections between areas - can break under weight, burn, or be cut, creates dynamic navigation paths

    // Interactive Systems
    INTERACTION = 20000,
    Ladder, // Vertical movement system - can be damaged, have missing rungs, or be retractable
    Platform, // Moving surfaces - elevators, conveyor belts, rotating platforms, can be controlled or automatic
    Trap, // Hidden dangers - spike pits, poison darts, explosive mines, can be disarmed or triggered
    Light, // Illumination source - torches, lanterns, magic lights, affects stealth and visibility systems
    Fire, // Destructive element - campfires, braziers, spreading flames, can cook food, burn objects, provide warmth
    Water, // Liquid barriers - rivers, pools, wells, can be crossed, dived in, or used for cleaning/drinking

    // Information Systems
    INFORMATION = 30000,
    Sign, // Readable text displays - road signs, shop names, warnings, can be in different languages or codes
    Book, // Detailed information containers - lore, maps, recipes, spells, can be rare or common knowledge
    Note, // Short messages - letters, journals, graffiti, can provide clues or backstory
    Map, // Navigation aids - world maps, floor plans, treasure maps, can be incomplete or misleading
    Terminal, // Electronic information systems - computers, kiosks, control panels, require hacking or passwords

    // Economic Systems
    ECONOMIC_SYSTEMS = 40000,
    Vendor, // NPCs that buy/sell items - shopkeepers, traders, have specific inventory and pricing rules
    Bank, // Storage for player currency - can earn interest, be robbed, have withdrawal limits
    CraftingStation, // Tool for creating items - forge, alchemy table, workbench, requires materials and recipes
    Resource, // Raw materials in world - ore veins, herb patches, lumber trees, regenerate over time

    // Transportation
    TRANSPORTATION = 50000,
    Vehicle, // Player-controlled transport - cars, boats, horses, can break down, need fuel, have different speeds
    Mount, // Rideable creatures - horses, dragons, motorcycles, have loyalty/training systems, unique abilities
    FastTravel, // Quick movement points - waypoints, teleporters, train stations, may cost resources or have prerequisites

    // Combat Systems
    COMBAT_SYSTEMS = 60000,
    Weapon, // Combat tools - swords, guns, magic staffs, have durability, enchantments, skill requirements
    Armor, // Protective gear - helmets, shields, full suits, affect movement speed and stealth
    Projectile, // Ranged attack objects - arrows, bullets, magic missiles, affected by physics and materials
    Cover, // Tactical protection - walls, barrels, sandbags, can be destroyed or moved

    // Stealth Systems
    STEALTH = 70000,
    Shadow, // Darkness areas for hiding - under stairs, behind objects, affected by light sources and time of day
    Noise, // Sound-generating objects - creaky floors, rattling chains, can alert or distract NPCs
    Camera, // Surveillance systems - security cameras, guard towers, magic scrying, have detection ranges and blind spots
    Alarm, // Alert systems - bells, horns, magic wards, trigger when stealth is broken

    // Environmental Systems
    ENVIRONMENTAL = 80000,
    Weather, // Atmospheric conditions - rain, snow, wind, affect visibility, movement, and NPC behavior
    Temperature, // Thermal zones - hot/cold areas, require appropriate gear, affect stamina and health
    Poison, // Toxic areas - gas clouds, contaminated water, require protection or cause damage over time
    Magic, // Supernatural zones - mana wells, cursed areas, teleportation circles, have unique interaction rules

    // Social Systems
    SOCIAL = 90000,
    Crowd, // Groups of background NPCs - market crowds, protesters, party guests, create social stealth opportunities
    Faction, // Organized groups with shared goals - guilds, gangs, religions, have reputation and quest systems
    Relationship, // Social connections between NPCs - family, friends, enemies, affect dialogue and quest availability

    // Quest Systems
    QUEST = 100000,
    Objective, // Mission markers in world - rescue targets, delivery points, investigation sites
    Clue, // Evidence for investigations - bloodstains, footprints, dropped items, reveal information when examined
    Barrier, // Quest-gated obstacles - locked areas, story barriers, require progression to pass

    // AI Behavior
    AI_BEHAVIOR = 110000,
    Patrol, // NPC movement paths - guard routes, animal territories, can be predictable or randomized
    Schedule, // Time-based NPC activities - work shifts, daily routines, seasonal changes
    Territory, // Area ownership by NPCs - personal space, defended zones, trespassing consequences

    // Physics Objects
    PHYSICAL_SECONDARY = 120000,
    Debris, // Destructible clutter - crates, barrels, glass, can hide items or create temporary cover
    Liquid, // Flowing substances - oil spills, blood trails, magic potions, create temporary effects on terrain
    Gas, // Airborne substances - smoke, fog, toxic clouds, affect visibility and breathing

    // Network elements
    Network_Firewall_Rule = 130000,
    Network_Route,
    Network_Backend,
    Network_CDN_Cache,
    Network_NAT_Entry,
    Network_VPN_Tunnel,
    Network_HTTP_Proxy,
    Network_DNS_Entry,
    Network_IDS_Signature,
    Network_RateLimit,

    // Meta Systems
    META = 500000,
    Spawn, // Entity creation points - monster generators, item respawn locations, can be disabled or modified
    Trigger, // Event activation zones - cutscene triggers, level transitions, state change areas
    Sensor, // Detection systems - motion sensors, pressure plates, magic detection, feed information to other systems
    Effect, // Visual/audio feedback - particle effects, sound zones, screen filters, provide atmospheric feedback
    Waypoint, // Navigation assistance - path markers, destination guides, can be player-placed or world-generated
};

//NOTE: Use this by taking all the states of Parent A and B (if exists), to create base_value on manual trigger update
//NOTE: Each implementation (WorldItem, Entity) needs it's own implementation to use "parent" because we use Data Router to map buttons to them by struct name, and the db.table must match
pub const EntityScaling = struct {
    // Parent A.  Value = A+B
    parent_a_id: i32 = -1, // First parent entity id (-1 = none)

    scalar_a: f32 = 0, // Multiplied by the curve value
    curve_a: Curve = .Linear,
    curve_a_value: f32 = 1, // 0-1, gets the Curver scalar to multiple scalar_a by parent_id_a's stat base_value

    // Parent B
    parent_b_id: i32 = -1, // Second parent entity id (-1 = none)

    scalar_b: f32 = 0, // Multiplied by the curve value
    curve_b: Curve = .Linear,
    curve_b_value: f32 = 1, // 0-1, gets the Curver scalar to multiple scalar_b by parent_id_b's stat base_value
};

//NOTE: This is a convenience system, it is not required, but it makes things easier to have a subset for games
pub const CharacterSystem = struct {
    // In base currency units of the game world.  If this is an Actor, this is their "liquid asset worth", if this is an non-Actor (Item, Building, other thing that can be bought (ex: not a "wild flower on a mountain")) then money is the base cost of the item, before adjustments for whatever are needed.  We baseline the game in the same currency for all monies
    money: StatEntry = .{},

    // Core Life Stats
    health: StatEntry = .{},
    stamina: StatEntry = .{},

    // Code Ability Stats
    strength: StatEntry = .{},
    agility: StatEntry = .{},
    wit: StatEntry = .{},
    awareness: StatEntry = .{},
    charm: StatEntry = .{},

    // Progression
    xp: StatEntry = .{},
    level: StatEntry = .{},

    // Simple Needs
    hunger: StatEntry = .{},
    thirst: StatEntry = .{},
    heat: StatEntry = .{},

    // Custom Stats
    stats: []StatEntry = &[_]StatEntry{},

    // Scaling all the stats at once
    scaling: EntityScaling = .{},

    // Combat
    is_weapon_equipped: bool = false,
    weapon_item_index: i32 = -1,
};

pub const RenderData = struct {
    // Order for rendering.  This is often first done by Pass, such as TerrainBase, or ActorBase, but then is often done by Y position, so y1 renders first if y1<y2, so that y2 covers it
    z_order: i32 = 0,
    render_layer: content_item.ContentRenderLayer = .None,
    // Where it will render on the Canvas
    canvas_rect: rl.Rectangle = .{},

    // The Render Command that created this in our Scene
    render_command_index: i32 = -1,

    // Update execution times
    duration_update: f32 = 0,
    duration_update_facts: f32 = 0,
};

pub const FormationType = enum(i32) {
    None = -1,

    // BASIC FORMATIONS
    Single = 0, // Just the leader, no formation
    Pair = 1, // Leader + 1 follower side by side
    Triangle = 2, // 3 units, leader front
    Square = 4, // 4 units in square
    Circle = 5, // Ring around leader

    // MILITARY - FIRE TEAM (4-6 units)
    FIRE_TEAM = 1000,
    Wedge, // V-formation, leader at point
    Echelon_Right, // Diagonal right stairs
    Echelon_Left, // Diagonal left stairs
    File, // Single column
    Staggered_Column, // Alternating left/right column

    // MILITARY - SQUAD (8-12 units)
    SQUAD = 2000,
    Line_Abreast, // Horizontal line, all units side by side
    Vee_Formation, // Wide V, leader at point
    Diamond, // Diamond shape, leader front
    Arrowhead, // Narrow V, penetration formation
    Double_Column, // Two parallel columns

    // MILITARY - PLATOON (20-40 units)
    PLATOON = 3000,
    Company_Column, // Multiple squads in column
    Company_Line, // Multiple squads in line
    Company_Wedge, // Large scale wedge
    Box_Formation, // Hollow square for defense
    Flying_Wedge, // Concentrated spearhead

    // MILITARY - COMPANY/BATTALION (100+ units)
    LARGE_UNIT = 4000,
    Phalanx, // Dense rectangular formation
    Shield_Wall, // Overlapping shields, defensive line
    Testudo, // Turtle formation, shields overhead
    Pike_Square, // Anti-cavalry square
    Three_Ranks, // Front, middle, rear firing lines
    Hollow_Square, // Center protected by perimeter

    // TACTICAL COMBAT
    TACTICAL = 5000,
    Cover_Formation, // Units behind cover points
    Bounding_Overwatch, // Leap-frog advance
    L_Shaped_Ambush, // Two-sided attack position
    Envelopment, // Flanking crescent
    Pincer, // Two-pronged encirclement

    // RPG PARTY (3-6 units)
    RPG_PARTY = 6000,
    Tank_Lead, // Tank front, ranged back
    Mage_Center, // Casters protected in middle
    Healer_Rear, // Support in back rank
    Skirmish_Line, // Spread out for AOE avoidance
    Protect_VIP, // Ring around key character
    Two_One_Two, // Front line 2, mid 1, back 2

    // TACTICAL RPG (TRPG) - Grid Based
    TRPG = 7000,
    Checkerboard, // Alternating positions for movement
    Diagonal_Line, // Diagonal across battlefield
    Castle_Defense, // Units guarding choke points
    Pincer_Advance, // Split forces converge
    Cavalry_Wings, // Fast units on flanks

    // ACTION/BRAWLER
    ACTION = 8000,
    Boss_Circle, // Surround single target
    Hit_And_Run, // Scattered harass positions
    Combo_Chain, // Sequential attack positions
    Juggle_Position, // Setup for air combos
    Wall_Pin, // Force enemy against obstacle

    // METROIDVANIA/PLATFORMER
    METROIDVANIA = 9000,
    Platform_Stack, // Vertical arrangement
    Layered_Depth, // Front/mid/back plane positions
    Patrol_Route, // Following path points
    Ceiling_Walkers, // Units on upper surfaces
    Shadow_Trail, // Following exact player path

    // STRATEGY/RTS (Starcraft, Age of Empires)
    RTS = 10000,
    Ball_Formation, // Clumped for speed
    Concave, // Curved line for surface area
    Split_Groups, // Multiple control groups
    Arc_Formation, // Semi-circle for surround
    Loose_Scatter, // Spread vs AOE

    // BASE BUILDING/COLONY SIM (RimWorld, Dwarf Fortress)
    COLONY = 11000,
    Work_Station_Ring, // Workers around central point
    Hauler_Chain, // Line for passing items
    Guard_Posts, // Sentries at key locations
    Patrol_Path, // Walking predefined route
    Panic_Room, // Converge to safe area
    Fire_Brigade, // Line to water source

    // SWARM/HORDE
    SWARM = 12000,
    Zerg_Rush, // Chaotic mass advance
    Flocking, // Boid-like natural movement
    Wave_Pattern, // Surging forward in waves
    Engulf, // Surround and overwhelm
    Scatter_Regroup, // Break and reform

    // NAVAL/SPACE
    FLEET = 13000,
    Line_Of_Battle, // Broadside formation
    Column_Line, // Follow the leader
    Screen_Formation, // Smaller ships protect capital ships
    Carrier_Group, // Ring around carrier/flagship
    Destroyer_Screen, // Anti-sub/fighter perimeter

    // AERIAL/FLYING
    AERIAL = 14000,
    V_Flight, // Bird migration pattern
    Vic_Formation, // 3 aircraft, leader front
    Finger_Four, // 4 aircraft, 2x2 pairs
    Combat_Spread, // Wide spacing for dogfight
    Trail_Formation, // Single file flight

    // MOUNTED/CAVALRY
    MOUNTED = 15000,
    Charge_Line, // Horizontal for shock
    Wedge_Charge, // Penetration cavalry
    Caracole, // Rotate through for ranged
    Cantabrian_Circle, // Continuous wheeling attack

    // STEALTH/INFILTRATION
    STEALTH = 16000,
    Shadow_Follow, // Stay in leader's shadow
    Scattered_Blend, // Mix with civilians/environment
    Overwatch_Pairs, // Buddy system coverage
    Sequential_Entry, // Timed separate infiltration

    // CEREMONIAL/NON-COMBAT
    CEREMONIAL = 17000,
    Parade_Line, // Formal line for display
    Honor_Guard, // Flanking VIP
    Procession, // Ordered march
    Escort_Formation, // Protection diamond

    // VEHICLE FORMATIONS
    VEHICLE = 18000,
    Convoy_Column, // Road march
    Herringbone, // Off-road defensive
    Coil, // Circular perimeter defense
    Wedge_Advance, // Armor spearhead

    // CREATURE/MONSTER SPECIFIC
    CREATURE = 19000,
    Pack_Hunt, // Wolves/raptors surround
    Alpha_Led, // Leader front, pack follows
    Swarm_Cloud, // Insects/bats diffuse mass
    Serpent_Trail, // Long following line
    Nest_Defense, // Radial from center point

    // MOBA/TEAM FIGHTER
    MOBA = 20000,
    Lane_Push, // 3 lanes, distributed
    Gank_Formation, // Converge from fog
    Teamfight_Engage, // Frontline/backline split
    Split_Push, // Divide pressure
    Siege_Position, // Structured tower attack

    // BULLET HELL/DANMAKU
    DANMAKU = 21000,
    Spiral_Pattern, // Rotating spiral
    Radial_Burst, // Outward explosion
    Stream_Pattern, // Directed beam
    Random_Spread, // Chaotic fill
    Aimed_Cluster, // Tracking group

    // PUZZLE/COOPERATIVE
    PUZZLE = 22000,
    Weight_Plates, // Positioned on switches
    Relay_Chain, // Sequential activation
    Simultaneous_Trigger, // All at once activation
    Path_Blockers, // Obstruction pattern

    // RACING/CHASE
    RACING = 23000,
    Drafting_Line, // Follow for speed boost
    Blocking_Wall, // Prevent passing
    Slingshot_Setup, // Boost preparation
    Pack_Racing, // Tight group advantage

    // BOSS MECHANICS
    BOSS = 24000,
    Boss_Core_Shield, // Core protected by orbiting shields
    Boss_Weakpoint_Circle, // Vulnerable spots around perimeter
    Boss_Phase_Segments, // Destructible parts unlock phases
    Boss_Rotating_Barrier, // Spinning shield gaps
    Boss_Tentacle_Ring, // Radial appendages from center
    Boss_Twin_Cores, // Two vulnerable points, must destroy both
    Boss_Nested_Shells, // Layers peel away sequentially
    Boss_Detach_Swarm, // Parts break off and attack independently
    Boss_Reconstruct, // Segments reform after damage window
    Boss_Clockwork_Arms, // Mechanical limbs at cardinal points

    // MULTI-STAGE BOSS
    BOSS_MULTISTAGE = 25000,
    Stage_Add_Segments, // Grows more parts each phase
    Stage_Shed_Armor, // Loses protection, gains speed
    Stage_Split_Form, // Divides into multiple entities
    Stage_Merge_Minions, // Absorbs adds for power
    Stage_Mode_Shift, // Ranged → Melee → Mixed
    Stage_Desperation, // Final phase, all parts active
    Stage_Resurrection, // Reforms with new configuration
    Stage_Inverse_Form, // Inside-out, reverse weak points

    // MINION SPAWNING PATTERNS
    MINION_SPAWN = 26000,
    Spawn_Portal_Ring, // Portals around arena edge
    Spawn_Boss_Birth, // Emerge from boss body
    Spawn_Ground_Eruption, // Rise from floor in pattern
    Spawn_Ceiling_Drop, // Fall from above
    Spawn_Wave_Sequential, // Timed waves from sides
    Spawn_Reinforcement_Arc, // Support arrives from rear
    Spawn_Teleport_Random, // Appear in safe zones
    Spawn_Carrier_Deploy, // Released from transport unit

    // ELITE/CHAMPION FORMATIONS
    ELITE = 27000,
    Elite_Bodyguard_Diamond, // Elites protect mini-boss
    Elite_Champion_Pair, // Two elites coordinate
    Elite_Herald_Advance, // Elite leads trash mob wave
    Elite_Support_Triangle, // Elite buffs/heals adds
    Elite_Sniper_Overwatch, // Elite on high ground, adds below
    Elite_Berserker_Charge, // Elite rush, adds follow
    Elite_Summoner_Center, // Elite spawns adds around self
    Elite_Tank_Wall, // Elites block, adds flank

    // RAID/DUNGEON MECHANICS
    RAID = 28000,
    Add_Spawn_Timer, // Periodic reinforcements
    Tank_Spank_Swap, // Dual threats, split attention
    Burn_Phase_Stack, // Damage race before wipe
    Interrupt_Priority, // Key casts must be stopped
    Add_Control_Burn, // Kill adds vs ignore decision
    Spread_Mechanic, // Distance required between units
    Stack_Mechanic, // Group up for shared defense
    Gauntlet_Constant, // Continuous add stream

    // XCOM/TACTICS ENEMY GROUPS
    XCOM = 29000,
    Pod_Activation, // Groups patrol, alert together
    Overwatch_Trap, // Enemy firing line setup
    Flanking_Pairs, // Two units coordinate flanks
    High_Ground_Sniper, // One elevated, others ground
    Suppression_Advance, // Cover fire while moving
    Grenadier_Cluster, // Explosive unit protected
    Mind_Control_Screen, // Controller behind meatshields
    Melee_Rush_Ranged, // Mixed engagement distances

    // HALO COVENANT TACTICS
    HALO = 30000,
    Grunt_Swarm, // Weak units flood forward
    Elite_Led_Lance, // Elite + grunts standard group
    Jackal_Shield_Wall, // Shield bearers front
    Hunter_Pair, // Always come in twos
    Brute_Pack_Alpha, // Pack leader + subordinates
    Engineer_Float_Repair, // Support unit stays back/above
    Ghost_Strafe_Pattern, // Vehicle harassment
    Wraith_Artillery_Guard, // Heavy unit with escort

    // STARSHIP TROOPERS / SWARM
    BUG_SWARM = 31000,
    Warrior_Wave, // Basic rush en masse
    Tanker_Spray_Center, // AOE unit protected by warriors
    Hopper_Sky_Rain, // Aerial units dive bomb
    Brain_Bug_Guarded, // VIP surrounded by elites
    Plasma_Bug_Artillery, // Long range with meat shields
    Tunnel_Network_Spawn, // Emerge from multiple holes
    Infinite_Reinforcement, // Continuous spawn pressure

    // TOWER DEFENSE WAVES
    TD_WAVE = 32000,
    Fast_Rush, // Speed focused early pressure
    Tank_Slow_March, // High HP crawl
    Flying_Bypass, // Ignore ground defenses
    Split_Path_Force, // Divide player attention
    Boss_Escort, // Big unit with support
    Cloaked_Infiltrator, // Stealth units slip through
    Shield_Regenerate, // Heal while moving
    Zigzag_Dodge, // Erratic movement pattern

    // SOULS-LIKE ENCOUNTERS
    SOULSLIKE = 33000,
    Ambush_Spawn_Behind, // Appear in cleared area
    Patrol_Alert_Chain, // One alerts nearby groups
    Gank_Squad_Surround, // Coordinated multi-attack
    Fake_Death_Resurrect, // Enemy plays dead, rises
    Mimic_Trap_Position, // Disguised until approached
    Archer_Snipe_Ledge, // Ranged from unreachable spot
    Dual_Boss_Arena, // Two bosses, shared health pool
    NPC_Invader_Hunt, // AI tracks player aggressively

    // EXTRACTION/SURVIVAL
    EXTRACTION = 34000,
    Perimeter_Collapse, // Circle closes with enemies
    Exfil_Block_Formation, // Guard extraction point
    Stalker_Shadow_Follow, // Enemies track at distance
    Horde_Night_Surge, // Timed massive wave
    Supply_Drop_Contest, // Enemy converge on loot
    Reinforcement_Helicopter, // Enemies deploy from vehicle
    Hunter_Killer_Team, // Elite squad hunts player
    Time_Pressure_Spawn, // Spawn rate increases over time

    // MECH/KAIJU SCALE
    GIANT = 35000,
    Limb_Disable_Target, // Destroy arms/legs individually
    Chest_Core_Expose, // Armor breaks to reveal heart
    Shoulder_Cannon_Mount, // Weapon systems as followers
    Tail_Sweep_Pattern, // Rear attack appendage
    Wing_Segment_Shield, // Flying boss with destructible wings
    Head_Beam_Attack, // Face-mounted weapon
    Leg_Joint_Weakpoint, // Topple by destroying supports
    Back_Reactor_Vent, // Must circle to hit weak spot

    // FIGHTING GAME PATTERNS
    FIGHTING = 36000,
    Assist_Character_Call, // Teammate appears for combo
    Clone_Shadow_Army, // Copies of main character
    Puppet_Master_Control, // One controls multiple units
    Stance_Formation_Shift, // Changes attack pattern by position
    Super_Armor_Charge, // Follower tanks hits for setup
    Corner_Pressure_Trap, // Force player into corner
    Throw_Tech_Position, // Grab setup formation
    Okizeme_Wakeup_Cover, // Pressure on player recovery

    // RHYTHM/MUSIC COMBAT
    RHYTHM = 37000,
    Beat_Sync_Spawn, // Enemies arrive on musical beats
    Measure_Wave_Pattern, // Groups per musical phrase
    Tempo_Change_Speed, // Formation speed matches BPM
    Harmony_Multi_Layer, // Multiple simultaneous patterns
    Crescendo_Intensity, // Building add density
    Rest_Safe_Window, // Breaks in musical structure
    Chord_Simultaneous, // Multiple units exact timing

    // PUZZLE BOSS MECHANICS
    PUZZLE_BOSS = 38000,
    Color_Match_Weakness, // Must use correct element followers
    Symbol_Sequence_Attack, // Followers form solution pattern
    Mirror_Reflect_Formation, // Copy boss pattern to damage
    Pillar_Activate_Ring, // Followers on pressure plates
    Beam_Redirect_Chain, // Followers form light puzzle
    Weight_Balance_Scale, // Distribute followers evenly
    Tether_Distance_Maintain, // Keep specific spacing
    Rotation_Align_Gears, // Mechanical positioning puzzle

    // CARD GAME INSPIRED
    DECK_BATTLE = 39000,
    Summon_Hand_Formation, // Deploy cards as followers
    Mana_Cost_Limit, // Total power level restricted
    Sacrifice_Tribute, // Destroy follower for power
    Evolution_Chain, // Followers merge/upgrade
    Draw_Phase_Spawn, // Periodic reinforcement
    Graveyard_Resurrect, // Return defeated followers
    Mulligan_Reposition, // Shuffle formation randomly
    Combo_Chain_Activate, // Sequential follower abilities

    // ASYMMETRIC MULTIPLAYER
    ASYM_PVP = 40000,
    Monster_Player_Minions, // One player controls boss + adds
    Evolve_Hunt_Pattern, // Monster gains power, hunters coordinate
    Left_4_Dead_Director, // AI spawns based on player position
    Spy_Blend_NPCs, // Player hides among AI
    Predator_Cloak_Stalk, // Invisible with thermal vision
    Jason_Voorhees_Teleport, // Appear near isolated targets
    Killer_Hook_Carry, // Transport downed players
    Survivor_Rescue_Formation, // Team must coordinate save
};

// Treat as Worker Threads for the Entity to accomplish things and show the player
pub const FollowerInstance = struct {
    is_active: bool = false,
    follower_index: i32 = -1,

    // Lifetime
    started: f32 = -1,
    duration: f32 = -1, // If -1, forever, otherwise will become is_active=false after duration
    started_frame: i32 = 0, // Frame number this started playing
    duration_frames: i32 = -1, // If > 0, this is the number of frames until we set `is_active=false`, so that we can base these on animations

    // Ring Buffer Type
    ring_buffer_type: EntityType = .None,
    ring_buffer_type_actor: EntityActorType = .None,

    // Visual rendering - uses same ContentItem system as leader
    content_import_id: i32 = -1, // Reference to game.content_import

    // Formation Index, which formation position do we use?
    formation_index: i32 = 0,

    // Which unit are we in this formation?  Can use unit to determine offset from the formation position or precedence
    formation_unit: i32 = 0,

    // Where follower is
    transform: EntityTransform = .{},

    // Where follow is trying to go
    target: EntityTarget = .{},

    // Animation independence
    animation: content_item.ContentAnimation = .None,
    anim_time_start: f32 = 0, // Time we started this animation
    cur_frame: i32 = 0,
    cur_event: content_item.ContentEventType = .None,
    cur_event_handled: bool = false,

    // Our Next Animation, planned
    next_animation: content_item.ContentAnimation = .None,
    next_anim_time_start: f32 = 0, // Time to start the next animation, can include offset from Leader/others, and can be unique animations

    // Optional independent direction
    direction: content_item.ContentDirection = .East, // Can face differently than leader

    // Stats: Most basic only
    health: i32 = 0,
    stamina: i32 = 0,
    power_level: i32 = 0,

    // Text and Size for a Rect
    text: Text = Text.initEmpty(),
    font_id: i32 = 0,
    font_size: i32 = 22,
    size: rl.Vector2 = .{}, // Used for Text Rect, if we want by rect size instead of font_size

    // Awareness
    last_hit_by: TrackEntity = .{},
    working_with_entity: TrackEntity = .{},
};

pub const FormationRect = struct {
    is_active: bool = false,

    rect: rl.Rectangle = .{},

    // Size of each unit
    unit_size: f32 = 1,

    // Calculated (cached for performance)
    cols: i32 = 0,
    rows: i32 = 0,
    units_that_fit: i32 = 0,

    pub fn init(rect: rl.Rectangle, unit_size: f32) FormationRect {
        const cols = @max(1, @as(i32, @intFromFloat(rect.width / unit_size)));
        const rows = @max(1, @as(i32, @intFromFloat(rect.height / unit_size)));

        return FormationRect{
            .rect = rect,
            .unit_size = unit_size,
            .cols = cols,
            .rows = rows,
            .units_that_fit = cols * rows,
        };
    }

    pub fn getPosition(self: FormationRect, index: i32) rl.Vector2 {
        const row = @divTrunc(index, self.cols);
        const col = @mod(index, self.cols);

        // Center each unit in its cell
        const offset_x = @as(f32, @floatFromInt(col)) * self.unit_size + self.unit_size * 0.5;
        const offset_y = @as(f32, @floatFromInt(row)) * self.unit_size + self.unit_size * 0.5;

        return rl.Vector2{
            .x = self.rect.x + offset_x,
            .y = self.rect.y + offset_y,
        };
    }

    pub fn unitCount(self: FormationRect) i32 {
        return self.units_that_fit;
    }

    pub fn setRect(self: *FormationRect, new_rect: rl.Rectangle) void {
        self.rect = new_rect;
        self.cols = @max(1, @as(i32, @intFromFloat(new_rect.width / self.unit_size)));
        self.rows = @max(1, @as(i32, @intFromFloat(new_rect.height / self.unit_size)));
        self.units_that_fit = self.cols * self.rows;
    }

    // Get formation center for regiment positioning
    pub fn getCenter(self: FormationRect) rl.Vector2 {
        return rl.Vector2{
            .x = self.rect.x + self.rect.width * 0.5,
            .y = self.rect.y + self.rect.height * 0.5,
        };
    }
};

pub const FollowerSystem = struct {
    has_followers: bool = false,

    //TODO: Implement the fixed size arrays for massive CPU perf, no more allocates, and 100 precache is 30-300KB, depending
    follower_count: i32 = 0,
    followers: [100]FollowerInstance = [_]FollowerInstance{.{}} ** 100,

    // Offsets from the Leader Entity, which select the locations around the Leader.  May change based on direction, or not, up to the game
    formation: [10]FormationRect = [_]FormationRect{.{}} ** 10,
};

pub const MovementSpeedType = enum(i32) {
    None, // Guaranteed zero movement.  Idle could be changed, None cant
    Idle,
    Walk,
    Run,
    Sprint,
    Crouch,
    Crawl,
};

pub const MovementSystem = struct {
    // Speed at different modes
    speed_idle: f32 = 0,
    speed_walk: f32 = 30,
    speed_run: f32 = 70,
    speed_sprint: f32 = 150,
    speed_crouch: f32 = 20,
    speed_crawl: f32 = 10,

    // Distance for Walk and Run.  If it's greatern than this, actor runs, is less, they walk.  Approaching the target
    distance_for_run: f32 = 90,

    // Distance to Melee and Ranged
    distance_melee: f32 = 64,
    distance_range: f32 = 320,

    // Modifiers
    speed_modifier_terrain: f32 = 1.0, // 0.5 = half speed in mud
    speed_modifier_health: f32 = 1.0, // Scales with health percent
    speed_modifier_encumbrance: f32 = 1.0,
    speed_modifier_buffs: f32 = 1.0,
};

pub const EntityTransform = struct {
    // This is the Index of the entity in it's specify EntityType pool.  Not used for game.entity, which isn't an active Entity.  Only Scene actors get updates
    //NOTE: If this is the `Entity.transform`, then it will be set based on the `Entity.id`id_type`
    id: i32 = -1,
    follower_index: i32 = -1,

    // Attachment option: Mounts
    parent_id: i32 = -1,
    parent_follower_index: i32 = -1,

    // Pixel World position
    pos: rl.Vector2 = rl.Vector2{ .x = 0, .y = 0 },
    size: rl.Vector2 = rl.Vector2{ .x = 0, .y = 0 }, // Used for CanvasRect, and informational for GameRect
    // This is a helper-height.  We are 2d and 3d calculations are much more difficult, so we stay 2d, but maybe times height is useful.  Isometric, buildings, counters, jumping, but stay pos 2d with helper
    height: f32 = 0,
    // Scaling
    scale: f32 = 1,
    scale_display: f32 = 1, // Real scale is: `scale * scaleDisplay`, so that we can use `scaleDisplay` as an effect value, like run a biased sin wave to oscillate it 10%

    // Lerp factor and Physics
    follow_speed: f32 = 5.0,
    direction: rl.Vector2 = .{}, // We multiple movement speed by this, and it creates the velocity/acceleration
    velocity: rl.Vector2 = .{},
    acceleration: rl.Vector2 = .{},
    rotation: f32 = 0,
    rotation_velocity: f32 = 0,
    rotation_locked: bool = true, // No physics
    mass: f32 = 1,

    // This is the current speed the Entity is moving, in terms of Locomotion
    speed_type: MovementSpeedType = .None,

    // Display
    render_direction: content_item.ContentDirection = .East,

    // Order for rendering.  This is often first done by Pass, such as TerrainBase, or ActorBase, but then is often done by Y position, so y1 renders first if y1<y2, so that y2 covers it
    z_order: i32 = 0,
    render_layer: content_item.ContentRenderLayer = .None,

    // Where it rendered on the canvas.  All zero if this did not render.  Actual render position, even if clipped, if it rendered
    after_canvas_rect: rl.Rectangle = .{},

    pub fn update(self: *EntityTransform, deltaTime: f32) !void {
        // Update velocity-based movement (for FX particles)
        self.pos.x += self.velocity.x * deltaTime;
        self.pos.y += self.velocity.y * deltaTime;

        // Update acceleration if present
        self.velocity.x += self.acceleration.x * deltaTime;
        self.velocity.y += self.acceleration.y * deltaTime;
    }
};

pub const EntityTargetHandler = enum(i32) {
    None = -1, // Manual handling
    MoveTo, // Move to exact position
    MoveToMelee, // Move within range to Melee
    MoveToRanged, // Move within range to Ranged
};

pub const EntityTarget = struct {
    has_target: bool = false,

    handler: EntityTargetHandler = .MoveToMelee,

    // Entity is our Target
    entity_id: i32 = -1,
    entity_follower_index: i32 = -1,

    // Auto Targeting:  Only activates if `entity_id == -1`
    auto_target_type: EntityType = .None,
    auto_target_actor_type: EntityActorType = .None,

    // World Position, not an Entity
    has_pos_target: bool = false, // We don't want this by default, we can return null if no entity or pos
    pos: rl.Vector2 = rl.Vector2{ .x = 0, .y = 0 },
    height: f32 = 0,

    // 0 is exact position, but we can go negative or positive away from 0 for swing: -1-0-1
    target_track_looseness: f32 = 0,
};

pub const EquipmentSlotType = enum(i32) {
    None = -1,

    // Biped
    Head = 0,
    Hair,
    Eyes,
    Nose,
    Ears,
    Mouth,
    Neck,
    Torso,
    ArmLeft,
    ArmRight,
    HandLeft,
    HandRight,
    HandBoth, // Dual handed wielding
    Finger, // Ring
    Groin,
    Hips,
    Legs,
    Knees,
    Shins,
    Feet,

    // Gear
    Ammo = 1000,
    Hat,
    Backpack,
    Cape,
    Satchel,
    Pouch,

    // Monster
    Claw = 5000,
    Tail,
    Orifice,
    Eye,
    Ear,
    Wing,
    Horn,
};

pub const EquipmentSlot = struct {
    // Slot Type: What is this inventory attaching onto?  HandRight?  Hips?  Feet?  Head?  The equipment goes somewhere.  Special types like Backpack, Hat, Ammo.  All inclusive, generally
    slot_type: EquipmentSlotType = .None,
    invoked_by_action: skill_set_lib.ActionType = .None, // Strike, Cast, None (None or passive)

    world_item_id: i32 = -1, // What is the slot?  -1 = nothing
    can_stack: bool = false,
    count: i32 = 0, // Stack count, if possible (arrows)

    // Monk Hand, Priest Hand, Bruce Lee Leg
    default_world_item_id: i32 = -1,

    // Has Health, can injure this area?  Example: shot in HandRight, Legs
    health_max: i32 = 0, // If over 0, this area has health
    health: i32 = 0, // Current health
};

pub const InventoryItem = struct {
    is_active: bool = false, // If false, this Inventory slot is not used, and can take a new item.  Player can get 500, and normal NPCs like 20 fixed size

    world_item_id: i32 = -1, //
    can_stack: bool = false, // DUPE-DATA: We set from the world item, but we keep here so its local and dont need rechecks
    count: i32 = 0, // Stack count, if possible (arrows, currency, pebbles)
};

pub const ContainerSystem = struct {
    has_container_system: bool = false,

    // SM+Rules for container upgrades
    upgrade_state_machine_id: i32 = -1, // "unlocked" -> "locked" -> "lock_broken" -> "smashed"
    current_upgrade_state: Text = Text.initEmpty(),

    // Equipment
    equipment_slots: []EquipmentSlot = &[_]EquipmentSlot{},

    // Are Weapons out?  Matters in some games, will hide/show, and people can react
    weapons_ready: bool = false,

    // Inventory
    inventory: []InventoryItem = &[_]InventoryItem{},
    inventory_capacity: f32 = 0,
    carry_capacity: f32 = 0,

    // Upgrade tracking
    upgrade_level: i32 = 0,
    special_slots_unlocked: i32 = 0,
};

pub const InputPlayerGamepad = struct {
    is_active: bool = false,
};

pub const InputPlayerMouse = struct {
    is_active: bool = false,
};

pub const InputPlayerKeyboard = struct {
    is_active: bool = false,
};

pub const InputPlayerUiEvents = struct {
    is_active: bool = false,
};

pub const Date = struct {
    year: i32 = -1,
    month: i32 = -1,
    day: i32 = -1,
};

pub const ServerEntitySnapshot = struct {
    id: i32 = -1,
    follower_index: i32 = -1,

    transform: EntityTransform = .{}, // pos, velocity, rotation
    character: CharacterSystem = .{}, // health, stamina, etc.

    // What are they doing?
    state: Text = Text.initEmpty(),
    state_time_start: f32 = -1,

    // If they have a behavior, what is the name, for informational purposes.  Can be
    behavior_name: Text = Text.initEmpty(),
    behavior_time_start: f32 = -1,

    // Action
    action: skill_set_lib.ActionType = .None,
    action_time_start: f32 = -1,
};

pub const InputPlayer = struct {
    name: Text = Text.initEmpty(),

    // Input data
    mouse: InputPlayerMouse = .{},
    keyboard: InputPlayerKeyboard = .{},
    gamepad: InputPlayerGamepad = .{},
    ui_events: InputPlayerUiEvents = .{},

    // Identity
    email: Text = Text.initEmpty(),
    auth_token: Text = Text.initEmpty(),
    auth_token_last: Text = Text.initEmpty(),
    last_auth_time: f32 = -1,
    last_auth_rotation_time: f32 = -1, // Last time we rotated `auth_token`

    // Details
    is_human: bool = false, // Prove it
    is_human_time: f32 = -1, // Timestamp for updating `is_human`
    date_of_birth: Date = .{}, // For age verification, if required
    is_verified: bool = false, // Assume not verified, toggle after verification
    use_verification_service: bool = false, // If true, use external 3rd party verification service, specified in infra helper data table `game.identity_management`

    // Update
    client_frame: i32 = -1, // For lag compensation
    client_time: f32 = -1,

    // Client Info
    client_ip_address_port: Text = Text.initEmpty(), // Track for matching packets.  If the IP changes, we revalidate the auth_token, and update and store last for reference
    client_ip_address_port_last: Text = Text.initEmpty(), // History for the transition to new ip-port

    // If true, this user can edit the entire scene if `scene.is_network_dev_mode==true`
    is_dev: bool = false,
    //NOTE: When we do Mods, they will usre this same sort of start/end ID for their indexes for all values, but deferring the for now
    // Dev Content IDs Offset from `InputSytem.dev_content_id_start`, this means they work in normal dev mode from `InputSytem.dev_content_id_start+dev_content_offset_id_start` and `InputSytem.dev_content_id_start+mod_content_offset_start_id+dev_content_offset_id_start` if its a mod
    dev_content_offset_id_start: i32 = -1, // Start of their game.content_id.# range for their, also for game.image.# and any other dev input, like quest lines, anything.  New records go into their range
    dev_content_offset_id_end: i32 = -1, // End of their range
    dev_update_allow: prolog.RuleSet = .{}, // Only allow updates that match this ruleset
    dev_update_disallow: prolog.RuleSet = .{}, // Disllow updates that match this ruleset.  Sometimes cognitively easiery to think one way or the other, its a not(), but cognition matters
    dev_working_on_mod_id: i32 = -1, // If this is a mod, this is the registered ID.  Any new records will be created as the next in the range set available for any table
};

pub const InputSystem = struct {
    // For non-collaborative development (Release/Debug games), players can only send their InputPlayer data over in NIC, everything else is ignored because its game-mode
    //NOTE: For dev mode, network data can update any scene sub-path.  All sub-scene (game.scene.#._data_scene.*) is available for update in this mode.  In game-mode, only `*.input.players.(my_player_index)`
    players: []InputPlayer = &[_]InputPlayer{}, // Can have local multiplayer easily by just assigning gamepad.0 and gamepad.1 and keyboard.0, etc

    // Server Update
    server_frame: i32 = -1,
    server_time: f32 = -1,
    server_entities: []ServerEntitySnapshot = &[_]ServerEntitySnapshot{},

    // // Emails that are approved for dev access.  If their email address passes the validation process, or they already have the auth_token that's valid, then we give them dev access
    // //NOTE: This is a simple early implementation and not a final implementation.  Consider this stubbed, and current out of scope even for the current projects
    // dev_email_list: TextArray = .{},

    // Owner global control.  Dev rules cant override this, we Continue before we check them if data update record or field, or sub-path matches this, or by value, or any other prolog logic with memdb access via SiQL
    owner_only: prolog.RuleSet = .{}, // Disllow updates that match this ruleset.  Sometimes cognitively easiery to think one way or the other, its a not(), but cognition matters

    // What is the development content range?
    dev_content_id_start: i32 = -1, // Start of their game.content_id.# range for their, also for game.image.# and any other dev input, like quest lines, anything.  New records go into their range
    dev_content_id_end: i32 = -1, // End of their range
};

pub const ModRegistration = struct {
    // Display name
    name: Text = Text.initEmpty(),

    // Mod ID
    id: i32 = -1, // Registered ID

    // Mod Identity
    token: Text = Text.initEmpty(), // Unique token for this mod
    token_last: Text = Text.initEmpty(), // Last Unique token for this mod
    token_last_update_time: f32 = -1, // Last time we changed `token`

    // // Who can work on this Mod?
    // dev_email_list: TextArray = .{},

    // Mod Content range, ids across all tables belong to this registered mod.  Offset from `InputSytem.dev_content_id_start`
    mod_content_offset_id_start: i32 = -1, // Start of their game.content_id.# range for their, also for game.image.# and any other mod input, like quest lines, anything.  New records go into their range
    mod_content_offset_id_end: i32 = -1, // End of their range

    is_deleted: bool = false,
};

pub const ModSystem = struct {
    is_active: bool = false, //TODO: Deferred until after networking.  Get that working before mods
    mods: []ModRegistration = &[_]ModRegistration{},
};

// Network coordination metadata - defines WHO can update WHAT and HOW OFTEN
// This is pure data configuration, no code execution
// Different genres use different patterns

// Genre-specific presets (convenience patterns)
pub const NetworkGenrePreset = enum(i32) {
    None = 0,

    // MMO patterns
    MMO_PlayerCharacter = 100,
    MMO_NPC = 101,
    MMO_Monster = 102,
    MMO_WorldObject = 103,
    MMO_Projectile = 104,

    // Fighting game patterns
    Fighting_LocalPlayer = 200,
    Fighting_RemotePlayer = 201,
    Fighting_Projectile = 202,
    Fighting_Stage = 203,

    // RTS patterns
    RTS_Unit = 300,
    RTS_Building = 301,
    RTS_Projectile = 302,
    RTS_Resource = 303,
    RTS_FogOfWar = 304,

    // FPS patterns
    FPS_LocalPlayer = 400,
    FPS_RemotePlayer = 401,
    FPS_Weapon = 402,
    FPS_Projectile = 403,
    FPS_PickupItem = 404,

    // MOBA patterns
    MOBA_Hero = 500,
    MOBA_Creep = 501,
    MOBA_Tower = 502,
    MOBA_Ability = 503,

    // Battle Royale patterns
    BR_Player = 600,
    BR_LootItem = 601,
    BR_Vehicle = 602,
    BR_SafeZone = 603,

    // Racing patterns
    Racing_LocalCar = 700,
    Racing_RemoteCar = 701,
    Racing_Track = 702,
    Racing_Checkpoint = 703,

    // Turn-based patterns
    TurnBased_Unit = 800,
    TurnBased_Board = 801,
    TurnBased_TurnMarker = 802,
};

pub const NetworkUpdateSystem = struct {
    // Is this entity networked at all?
    is_networked: bool = false,

    // Authority model
    authority: NetworkAuthority = .{},

    // Update frequency control
    update_rate: NetworkUpdateRate = .{},

    // What data gets sent
    sync_config: NetworkSyncConfig = .{},

    // Prediction/smoothing settings
    prediction: NetworkPrediction = .{},

    // Ownership tracking
    ownership: NetworkOwnership = .{},

    // Genre-specific patterns
    genre_preset: NetworkGenrePreset = .None,
};

// Who has authority over which parts of this entity
pub const NetworkAuthority = struct {
    // Authority models
    model: NetworkAuthorityModel = .ServerAuthoritative,

    // Per-subsystem authority overrides
    transform_authority: NetworkAuthoritySource = .Server,
    character_authority: NetworkAuthoritySource = .Server,
    visual_authority: NetworkAuthoritySource = .Client, // Animation blending client-side
    movement_authority: NetworkAuthoritySource = .Server,
    combat_authority: NetworkAuthoritySource = .Server,
    input_authority: NetworkAuthoritySource = .Owner, // Only owner can update input

    // Special cases
    allow_client_prediction: bool = true, // Can client predict movement?
    server_reconciliation: bool = true, // Does server send corrections?
    validate_client_state: bool = true, // Should server validate?
};

pub const NetworkAuthorityModel = enum(i32) {
    None = 0, // Not networked
    ServerAuthoritative = 1, // Server owns all state (MMO, RTS)
    ClientAuthoritative = 2, // Client owns their entities (P2P fighting game)
    Hybrid = 3, // Mixed authority (RTS: units=server, camera=client)
    LockstepDeterministic = 4, // All clients run same simulation (RTS)
    OwnerAuthoritative = 5, // Owner has authority, server validates (action games)
};

pub const NetworkAuthoritySource = enum(i32) {
    Server = 0, // Server is authoritative
    Client = 1, // Any client can update (rare)
    Owner = 2, // Owning client is authoritative
    Shared = 3, // Both can update, last-write-wins
    ReadOnly = 4, // Computed locally, never sent
};

// How often this entity sends/receives updates
pub const NetworkUpdateRate = struct {
    // Send rate (from authority)
    send_rate_hz: f32 = 20, // Updates per second
    send_only_on_change: bool = true, // Only send if changed?
    send_minimum_delta: f32 = 0.01, // Minimum change to trigger send

    // Receive rate (interpolation target)
    interpolation_period_ms: f32 = 100, // How long to interpolate

    // Priority-based rate adjustment
    priority: NetworkPriority = .Normal,

    // Distance-based LOD
    use_distance_lod: bool = false,
    lod_near_rate_hz: f32 = 60, // Close entities: 60fps
    lod_mid_rate_hz: f32 = 20, // Mid distance: 20fps
    lod_far_rate_hz: f32 = 5, // Far entities: 5fps
    lod_near_distance: f32 = 100,
    lod_mid_distance: f32 = 500,
};

pub const NetworkPriority = enum(i32) {
    Critical = 0, // Player entities, always max rate
    High = 1, // Important NPCs, projectiles
    Normal = 2, // Regular entities
    Low = 3, // Decorative, far away
    Minimal = 4, // Nearly static, rare updates
};

// What data to synchronize
pub const NetworkSyncConfig = struct {
    // Transform
    sync_position: bool = true,
    sync_rotation: bool = true,
    sync_scale: bool = false,
    sync_velocity: bool = false, // Send velocity for interpolation?

    // Character stats
    sync_health: bool = true,
    sync_stamina: bool = false,
    sync_all_stats: bool = false, // Or just visible ones?

    // State
    sync_state_machine_state: bool = true,
    sync_animation_state: bool = true,

    // Input (owner → server)
    sync_input: bool = false, // Is this a player-controlled entity?

    // Combat
    sync_damage_events: bool = true, // Send discrete events?
    sync_active_effects: bool = true,

    // Compression
    quantize_position: bool = true, // 16-bit instead of 32-bit floats?
    quantize_rotation: bool = true, // Quaternion compression?
    delta_compression: bool = true, // Only send changes?

    // Relevance
    use_relevance_filtering: bool = true, // Only send to nearby clients?
    relevance_radius: f32 = 1000, // How far to send?
};

// Prediction and smoothing settings
pub const NetworkPrediction = struct {
    // Client-side prediction
    prediction_mode: NetworkPredictionMode = .None,

    // Smoothing/interpolation
    smoothing_mode: NetworkSmoothingMode = .Interpolation,
    smoothing_factor: f32 = 0.3, // Lerp factor (0-1)

    // Extrapolation (when no updates arrive)
    allow_extrapolation: bool = false,
    max_extrapolation_time_ms: f32 = 500,

    // Correction handling
    correction_mode: NetworkCorrectionMode = .Smooth,
    correction_threshold: f32 = 50, // Distance before correction
    correction_speed: f32 = 5, // How fast to correct

    // Lag compensation (server-side rewind)
    enable_lag_compensation: bool = false,
    max_rewind_time_ms: f32 = 150,
};

pub const NetworkPredictionMode = enum(i32) {
    None = 0, // No prediction, wait for server
    Basic = 1, // Predict own movement only
    Full = 2, // Predict physics and other entities
    Deterministic = 3, // Run full simulation locally (RTS)
};

pub const NetworkSmoothingMode = enum(i32) {
    None = 0, // Snap to server position
    Interpolation = 1, // Smooth between updates
    Extrapolation = 2, // Predict forward from last update
    Hybrid = 3, // Interpolate normally, extrapolate if delayed
};

pub const NetworkCorrectionMode = enum(i32) {
    Snap = 0, // Immediately jump to correct position
    Smooth = 1, // Lerp to correct position
    Blend = 2, // Gradually blend correction over time
    Ignore = 3, // Trust client completely (fighting games)
};

// Ownership and replication
pub const NetworkOwnership = struct {
    // Who owns this entity?
    owner_type: NetworkOwnerType = .Server,
    owner_player_id: i32 = -1, // If player-owned
    owner_scene_id: i32 = -1, // If owned by specific scene

    // Ownership transfer
    allow_ownership_transfer: bool = false,
    transfer_on_proximity: bool = false, // RTS: transfer to nearest player?

    // Replication
    replicate_to: NetworkReplicateTo = .All,
    replicate_to_team_only: bool = false,
    replicate_to_owner_only: bool = false,

    // Persistence
    persist_across_sessions: bool = false, // Save to database?
    destroy_on_owner_disconnect: bool = true,
};

pub const NetworkOwnerType = enum(i32) {
    Server = 0, // Server owns (NPCs, world objects)
    Player = 1, // Player owns (player character)
    Shared = 2, // No single owner (shared world state)
    Scene = 3, // Owned by a specific scene (scene-local entity)
};

pub const NetworkReplicateTo = enum(i32) {
    None = 0, // Don't send to anyone (local only)
    Owner = 1, // Only to owner
    Team = 2, // Only to team members
    All = 3, // To all connected clients
    Nearby = 4, // Only to nearby clients (within relevance_radius)
    Interest = 5, // Custom interest management (observers list)
};

pub fn applyGenrePreset(network: *NetworkUpdateSystem) void {
    switch (network.genre_preset) {
        .None => {},

        // MMO: Server-authoritative, frequent updates
        .MMO_PlayerCharacter => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.authority.input_authority = .Owner;
            network.authority.allow_client_prediction = true;
            network.authority.server_reconciliation = true;
            network.update_rate.send_rate_hz = 20;
            network.update_rate.priority = .Critical;
            network.sync_config.sync_position = true;
            network.sync_config.sync_health = true;
            network.sync_config.sync_input = true;
            network.prediction.prediction_mode = .Basic;
            network.prediction.smoothing_mode = .Interpolation;
            network.ownership.owner_type = .Player;
            network.ownership.destroy_on_owner_disconnect = true;
        },

        .MMO_NPC => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.update_rate.send_rate_hz = 10;
            network.update_rate.priority = .Normal;
            network.update_rate.use_distance_lod = true;
            network.sync_config.sync_position = true;
            network.sync_config.sync_health = true;
            network.prediction.smoothing_mode = .Interpolation;
            network.ownership.owner_type = .Server;
            network.ownership.replicate_to = .Nearby;
        },

        // Fighting: Lockstep deterministic, no prediction
        .Fighting_LocalPlayer => {
            network.is_networked = true;
            network.authority.model = .LockstepDeterministic;
            network.authority.input_authority = .Owner;
            network.update_rate.send_rate_hz = 60; // Fighting games need 60fps
            network.update_rate.priority = .Critical;
            network.sync_config.sync_input = true;
            network.sync_config.sync_position = false; // Deterministic = no state sync
            network.prediction.prediction_mode = .Deterministic;
            network.prediction.correction_mode = .Ignore; // Trust simulation
            network.ownership.owner_type = .Player;
        },

        .Fighting_RemotePlayer => {
            network.is_networked = true;
            network.authority.model = .LockstepDeterministic;
            network.update_rate.send_rate_hz = 60;
            network.update_rate.priority = .Critical;
            network.sync_config.sync_input = false; // Receive only
            network.prediction.prediction_mode = .Deterministic;
            network.ownership.owner_type = .Player;
        },

        // RTS: Lockstep for units, server validates
        .RTS_Unit => {
            network.is_networked = true;
            network.authority.model = .LockstepDeterministic;
            network.authority.server_reconciliation = true; // Server validates
            network.update_rate.send_rate_hz = 10;
            network.update_rate.send_only_on_change = true;
            network.sync_config.sync_position = false; // Deterministic
            network.sync_config.delta_compression = true;
            network.prediction.prediction_mode = .Deterministic;
            network.ownership.owner_type = .Player;
            network.ownership.allow_ownership_transfer = true;
        },

        .RTS_Building => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.update_rate.send_rate_hz = 1; // Buildings rarely change
            network.update_rate.send_only_on_change = true;
            network.sync_config.sync_position = false; // Static
            network.sync_config.sync_health = true;
            network.ownership.owner_type = .Player;
            network.ownership.persist_across_sessions = true;
        },

        // FPS: Client prediction with server correction
        .FPS_LocalPlayer => {
            network.is_networked = true;
            network.authority.model = .OwnerAuthoritative;
            network.authority.input_authority = .Owner;
            network.authority.allow_client_prediction = true;
            network.authority.server_reconciliation = true;
            network.update_rate.send_rate_hz = 60;
            network.update_rate.priority = .Critical;
            network.sync_config.sync_position = true;
            network.sync_config.sync_velocity = true;
            network.sync_config.sync_input = true;
            network.prediction.prediction_mode = .Full;
            network.prediction.enable_lag_compensation = true;
            network.prediction.correction_mode = .Blend;
            network.ownership.owner_type = .Player;
        },

        .FPS_RemotePlayer => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.update_rate.send_rate_hz = 20;
            network.update_rate.priority = .High;
            network.sync_config.sync_position = true;
            network.sync_config.sync_velocity = true;
            network.prediction.smoothing_mode = .Hybrid;
            network.prediction.allow_extrapolation = true;
            network.ownership.owner_type = .Player;
        },

        .FPS_Projectile => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.update_rate.send_rate_hz = 30;
            network.update_rate.priority = .High;
            network.sync_config.sync_position = true;
            network.sync_config.sync_velocity = true;
            network.prediction.smoothing_mode = .Extrapolation;
            network.ownership.owner_type = .Server;
            network.ownership.destroy_on_owner_disconnect = false;
        },

        // MOBA: Hybrid (movement=server, abilities=immediate)
        .MOBA_Hero => {
            network.is_networked = true;
            network.authority.model = .Hybrid;
            network.authority.transform_authority = .Server;
            network.authority.combat_authority = .Server;
            network.authority.input_authority = .Owner;
            network.update_rate.send_rate_hz = 20;
            network.update_rate.priority = .Critical;
            network.sync_config.sync_position = true;
            network.sync_config.sync_health = true;
            network.sync_config.sync_active_effects = true;
            network.prediction.prediction_mode = .Basic;
            network.ownership.owner_type = .Player;
            network.ownership.replicate_to = .All;
        },

        // Battle Royale: LOD-based updates, relevance filtering
        .BR_Player => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.authority.input_authority = .Owner;
            network.update_rate.send_rate_hz = 20;
            network.update_rate.priority = .Critical;
            network.update_rate.use_distance_lod = true;
            network.update_rate.lod_near_rate_hz = 30;
            network.update_rate.lod_far_rate_hz = 2;
            network.sync_config.use_relevance_filtering = true;
            network.sync_config.relevance_radius = 500;
            network.prediction.prediction_mode = .Basic;
            network.ownership.owner_type = .Player;
            network.ownership.replicate_to = .Nearby;
        },

        // Racing: High tick rate, velocity sync
        .Racing_LocalCar => {
            network.is_networked = true;
            network.authority.model = .OwnerAuthoritative;
            network.authority.input_authority = .Owner;
            network.update_rate.send_rate_hz = 60;
            network.update_rate.priority = .Critical;
            network.sync_config.sync_position = true;
            network.sync_config.sync_velocity = true;
            network.sync_config.sync_rotation = true;
            network.prediction.prediction_mode = .Full;
            network.prediction.smoothing_mode = .Hybrid;
            network.ownership.owner_type = .Player;
        },

        // Turn-based: Low tick rate, state sync only
        .TurnBased_Unit => {
            network.is_networked = true;
            network.authority.model = .ServerAuthoritative;
            network.update_rate.send_rate_hz = 1; // Only on turn change
            network.update_rate.send_only_on_change = true;
            network.sync_config.sync_position = true;
            network.sync_config.sync_health = true;
            network.prediction.prediction_mode = .None;
            network.ownership.owner_type = .Server;
            network.ownership.persist_across_sessions = true;
        },

        else => {},
    }
}

pub const EntityAction = struct {
    // What action performing now
    action: skill_set_lib.ActionType = .None,

    // Is it complete?
    is_complete: bool = false,

    // Time start/stop
    time_start: f32 = -1,
    time_end: ?f32 = null,

    // Frame start/stop
    frame_start: i32 = -1,
    frame_end: ?i32 = null,

    // How many Envelopes did this create?  Going from 0 to 1 is the big one, but we can track more
    envelope_count: i32 = 0,

    // Track the last event for visibility, we dont use this
    last_event: content_item.ContentEventType = .None,
};

//NOTE: Use []EntityReference instead of []i32, for the complete case
pub const EntityReference = struct {
    entity_id: i32 = -1,
    follower_index: i32 = -1,
};

// Anything in the game world.  Things outside the game world: UI, Input Mapping, system stuff, etc
pub const Entity = struct {
    // This is the Index of the entity in it's specify EntityType pool.  Not used for game.entity, which isn't an active Entity.  Only Scene actors get updates
    id: i32 = -1,

    // If true, this Entity gets extra debugging
    debug: bool = false,

    // This will sync back to game.entity.#, so it can be loaded and saved as an instance into data.level
    //NOTE: When we create a game.scene, we will have `actors.#` array, and can put N of the same `game.entity.#` in the list, this is not a problem to have duplicates in the scene
    from_entity_id: i32 = -1,

    // Index of the scene.spawners.#, if not -1
    spawned_from: i32 = -1,

    // How this Entity will act: it's Type
    entity_type: EntityType = .None,
    entity_actor_type: EntityActorType = .None,

    name: Text = Text.initEmpty(),

    // What Faction is this entity in?  game.faction.#
    faction_combat_id: i32 = -1, // Who does this Entity fight and defend?
    faction_work_id: i32 = -1, // What work does this Entity do?  Day time
    faction_home_id: i32 = -1, // Where does this Entity sleep?  Night time

    // Entity State Machine and State
    //TODO: State Machine should be a link to the State Machine table, and I should be able to Drop Down, and also just to a new tab with it.  "Open New Tab to Path"
    state_machine_id: i32 = -1, // Name of the State Machine to use, which is known and has all the states needed for this (ex: "Actor", "Tree", "Building", "Car")
    state: Text = Text.init("."), // Current state in the state machine

    // What is this actor doing now?  Maps to a Skill
    action: EntityAction = .{},
    // current_action: skill_set_lib.ActionType = .None, // What action performing now

    // Animation State Machine is separate, so we dont have to deal with that complexity in a single machine.  This is computed after the Entity is updated, using the Entity FactSet
    anim_state_machine_id: i32 = -1, // Name of the Anim State Machine to use, which is known and has all the states needed for this (ex: "Idle", "Walk", "AttackLeft", "Run")
    anim_state: Text = Text.init("."), // Current Anim state in the Anim state machine

    // Pos, Size, Height, Scale, Z-Order, Render Layer, and keeps record of where we were last rendered, or all zeroes if not rendered (clipped)
    transform: EntityTransform = .{},

    // Systems
    visual: VisualSystem = .{}, // Appearance and rendering
    target: EntityTarget = .{}, // Target for Movement or combat
    movement: MovementSystem = .{}, // Movement
    awareness: AwarenessSystem = .{}, // Actor closest to me, distance, target actor ids, cache for immediate checking into values instead of calculating in Utility test
    character: CharacterSystem = .{}, // Character: Stats, Money, character stuff
    follower: FollowerSystem = .{}, // Followers - Look like Entities, but only calculate offsets for format.  LERP them into position
    skill: SkillSystem = .{}, // Learning, teaching, and adaptation
    combat: CombatCapabilities = .{}, // All combat-related functionality
    container: ContainerSystem = .{}, // Storage and inventory capabilities
    event: EventSystem = .{}, // Event Mapping: Events to Logic Blocks
    audio: AudioProfile = .{}, // Sound effects, music, voice
    communication: Communication = .{}, // Information display and interaction
    effects: EffectsEngine = .{}, // Causing changes and modifications
    behavior: AIBehavior = .{}, // Intelligence and autonomous actions
    temporal: TemporalSystem = .{}, // Time-based properties
    environment: EnvironmentalSystem = .{}, // Weather and environmental interactions
    social: SocialSystem = .{}, // Reputation and social dynamics
    quest: QuestSystem = .{}, // Story progression and events
    dialogue: DialogueSystem = .{}, // Story progression and events
    crafting: CraftingSystem = .{}, // Story progression and events
    network: NetworkSystem = .{}, // Multiplayer and synchronization
    transport: TransportSystem = .{}, // Movement and teleportation
    needs: BiologicalNeeds = .{}, // Needs water, heaing, etc.
    item: ItemProperties = .{}, // Economic/gameplay item characteristics
    access: AccessControl = .{}, // Requirements and permissions
    meta: MetaSystem = .{}, // System metadata and utilities
    timer: EntityTimer = .{},
    input: InputSystem = .{}, // Input Mapper -> Entity local.  Prolog inspectable, serializable, time-travel blue-green
    //TODO: Uncomment once I'm ready to start doing network stuff, its all laid out for the tall infra to be written for the current data at the time.  I expect more refinement before implementation
    // network_update_system: NetworkUpdateSystem = .{}, // How network data updates handled between clients and server
    // mod_system: ModSystem = .{},
    render: RenderData = .{},

    //TODO: Write a struct that has all the data I need to track Body2D withany any of their anyopaque non-serializable data, and then I can restruct physics while serializing
    // body2d: Body2D = .{}, // Handles all physics: transform, velocity, forces, collision ---- //PROBLEM: has anyopaque, cant be serialized //SOLUTION: Use `transform`, it has everything needed to pipe it

    // // Troubleshooting.  Always set the position when we knew everything had worked out (successful ops), and then we can reset here if nav-lock problems
    // last_known_good_transform: EntityTransform = .{}, //TODO: This uses too much screen space for now
    // // When we Init, we set `tranform=init_transform` allowing us to have a Spawn point.  `transform` change change and be in any value, and we know how to reset the level
    // init_transform: EntityTransform = .{}, //TODO: Do this with in Init SM State

    // If not -1, we replace fields like "Entity.character.heath" with "InsideAccount.last_month.revenue", and now the user sees that
    silo_field_replacement_id: i32 = -1,

    // Is this Entity active?  If false, we dont run update(), but it's not deleted
    is_active: bool = true,

    // Delete this item, and leave it in the array, so we dont have to reorganize or free memory, just use from a new Entity if requested later.  Whack all the data during a LoadAll-Reset-Event
    //NOTE: Default is true, because we create more than we use, so all new items need to set this to false to claim their territory
    is_deleted: bool = true,
};
