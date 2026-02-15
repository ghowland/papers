const std = @import("std");
const rl = @import("raylib");

const entity_lib = @import("entity.zig");
const trace_lib = @import("trace.zig");
const level_data_lib = @import("level_data.zig");
const content_item = @import("content_item.zig");
const prolog = @import("prolog.zig");
const canvas_layout = @import("canvas_layout.zig");
const scene_lib = @import("scene.zig");

// Types
const Vector2 = @import("vector2.zig").Vector2;
const Number = @import("number.zig").Number;
const Text = @import("text.zig").Text;
const TextArray = @import("text_array.zig").TextArray;
const Color = @import("color.zig").Color;

const Entity = entity_lib.Entity;
const ActionSkillStatEnvelope = scene_lib.ActionSkillStatEnvelope;
const EntityTrace = trace_lib.EntityTrace;
const EntityType = entity_lib.EntityType;
const StatType = entity_lib.StatType;
const Curve = entity_lib.Curve;

pub const ActionType = enum(i32) {
    None,
    Idle,

    // Basic combat
    __COMBAT__,
    Strike = 1000, // Strike (Hand is separate info)
    Block, // Raise shield/parry
    Dodge, // Evasive move
    Kick,

    // Movement
    __MOVEMENT__,
    Move = 2000, // Walk/run - Input direction needed
    MoveToTarget, // Move to target

    // Ranged
    __RANGED__,
    Shoot = 3000, // Bow, gun, throw
    Reload, // Reload ranged weapon
    Aim, // Precision aiming

    // Reactions
    __REACTION__,
    Hit = 4000,
    Die,
    Dead,

    // Hand actions
    __MANUAL_ACTIONS__,
    PickUp = 5000, // Pick up item
    Push, // Push object
    Pull, // Pull object
    Throw, // Throw held item

    // Interact
    __INTERACT__,
    Interact = 6000, // Generic use/interact
    Open, // Open door/chest
    Close, // Close door/chest
    Activate, // Pull lever, press button

    // Social
    __SOCIAL__,
    Dialogue = 7000, // Initiate dialogue
    Gesture, // Emote/signal
    Bark,

    // Special
    __CAST__,
    Cast = 8000, // Magic casting
    Consume, // Eat/drink
    Craft, // Crafting action

    // Stances
    __STANCE__,
    StanceChange = 9000, // Switch combat stance
    WeaponsReady, // Toggle weapons_ready

    // Context-specific
    __CONTEXTUAL__,
    Mount = 10000, // Mount vehicle/creature
    Dismount,
};

pub const SkillType = enum(i32) {
    None = -1,

    // Rections: This is to Unify the Skill-Action system as being 1-way to do everything, even if it doesn't make sense.  These make sense as Actions, but I need a way to look them up:  Actions come from Skills
    __REACTION__ = 900,
    Hit,
    Die,
    Death,

    // Movement
    __MOVE__ = 1000,
    Idle,
    Walk,
    Run,
    Sprint,
    Climb,
    Slide,
    Jump,
    Crouch,
    CrouchWalk,
    Prone,
    Crawl,
    Swim,

    // Offense: Melee
    __MELEE__ = 2000,
    Strike,
    Kick,
    Grapple,
    Parry,
    Backstab,
    CastMelee,

    // Offense: Ranged
    __RANGED__ = 3000,
    Shoot,
    Throw,
    Reload,
    CastRanged,

    // Defense
    __DEFENSE__ = 4000,
    Block,
    Dodge,
    Roll,
    Dash,
    TakeCover,

    // Social
    __SOCIAL__ = 5000,
    Talk,
    Trade,
    Gift,
    Taunt,
    Command,

    // Survival
    __SURVIVAL__ = 6000,
    Heal,
    Clean,
    Burn,
    Bandage,
    Surgery,
    Resurrect,
    Track,
    Navigate,
    Dying, // In the process of Dying
    Dead, // Dead

    // Investigate
    __INVESTIGATE__ = 7000,
    Examine,
    Search,
    Appraise,
    DetectTrap,
    DetectPoison,
    DetectMagic,

    // Craft
    __CRAFT__ = 8000,
    Smithing,
    Brewing,
    Cooking,
    Construct,
    Repair,
    Upgrade,
    Enchant,
    Disenchant,
    Tanning,
    Smelting,
    Hack,
    Carve,

    // Gather
    __GRATHER__ = 9000,
    Mine,
    Chop,
    Pick,
    Fish,
    Harvest,
    Dig,
    PickLock,
    DisarmTrap,

    // Stealth
    __STEALTH__ = 10000,
    Hide,
    Pickpocket,
    Distract,
    Disguise,

    // Utility
    __UTILITY__ = 11000,
    Lock,
    Unlock,
    Push,
    Pull,
    Lift,
    Carry,
    Drop,
    ThrowItem,
    Activate,
    Deactivate,
    FlipSwitch,

    // Elemental
    __ELEMENTAL__ = 12000,
    Fire,
    Ice,
    Water,
    Air,
    Gravity,
    Electricity,
    Poison,
    Light,
    Dark,
    Psychic,
    Spirit,

    // Vehicle or Mount
    __VEHICLE__ = 13000,
    Mount,
    Dismount,
    Drive,
    Accelerate,
    Brake,
    Eject,
    Boost,

    // System
    __SYSTEM__ = 55000,
    Respawn,
    FastTravel,
    QuickSave,
    QuickLoad,
    Pause,
    MenuOpen,
    Screenshot,
    Record,
};

pub const SkillModifierType = enum(i32) {
    Additive,
    Multiplicative,
    Override,
    Max,
};

pub const SkillDurationRefreshType = enum(i32) {
    Blocked, // Cant activate yet, wait until finished
    Set, // Set the arg value, overwriting any existing value
    Accumulate, // Add the arg value to the existing value
};

pub const SkillTargetingMode = enum(i32) {
    None,
    SingleTarget, // Click target
    Self, // Always self
    GroundTarget, // Click position, AoE at position
    DirectionCone, // Face direction, cone
    DirectionLine, // Face direction, line
    NearestEnemy, // Auto-target closest
    LowestHealthAlly, // Auto-target weakest ally
    Radius, // All within radius
};

pub const SkillLevelBlending = enum(i32) {
    None = -1,
    Closest, // Closest 2 levels together (if size is 2)
    FurthestPair, // Furthest 2 levels together (if size is 2)
    SpectrumSampleThree, // 0th, middle and last levels used (if size is 3)
};

pub const SkillTargetDetail = enum(i32) {
    None = -1,

    // Hit Location
    Head = 1000,
    ArmLeft,
    ArmRight,
    Torso,
    Hips,
    LegLeft,
    LegRight,
    FootLeft,
    FootRight,
    HandLeft,
    HandRight,

    // Hit Location: Special
    Eyes = 2000,
    Ears,
    Mouth,
    Jaw,
    Temple,
    Neck,
    Throat,
    Clavicle,
    ArmPit,
    SolarPlexus,
    Groin,
    Knees,
    Shins,
    MetaTarsals,
    Shoulder,
    Elbow,
    Wrist,
    Finger,
    Thumb,

    // Vehicle: Car
    Tire = 5000,
    Windshield,

    // Vehicle: Airplane
    Wing = 6000,
    Propeller,
    Engine,
    Flaps,
    Elevator,
    StabilizerVerticalS,
    StabilizerHorizontal,
    Spoiler,
    Cockpit,
    Fueselage,
    Winglet,
    Rudder,
    Slats,

    // etc
    ETC = 20000,
};

pub const SkillVisualEffect = enum(i32) {
    None = -1,
    Hidden,
    Blurred,
    BlurredRadial,
    ColorFilter,
    Bloom,
};

pub const SkillAudioEffect = enum(i32) {
    None = -1,
    Silent,
    Distortion,
    PitchShift,
    EqaulizeFilter,
    Ducking,
};

pub const SkillAudioPlayback = enum(i32) {
    None = -1,
    OneShot,
    Looping,
    Randomized,
};

pub const SkillPostEffect = enum(i32) {
    None = -1,
    Darkened,
    Brightened,
    Blurred,
    TransitionSwipe, // Render 2 canvases together, and make them change sizes vertically or horizontally.  Use fixed size UiElement sliding, and screen size layout from right-to-left for 0th on horizontal
    TransitionBlend, // Render 2 canvases at the same time and blend them together at a given amount each
};

pub const SkillCommandType = enum(i32) {
    None = -1,
    ExecuteLogicBlock,
    SpawnEntity,
    SpawnEntityFollower,
    ApplySkillEffect,
    RemoveSkillEffect,
    RemoveAllSkillEffects,
    RemoveAllNegativeSkillEffects,
    RemoveAllPositiveSkillEffects,
    RemoveAllMixedSkillEffects,
};

pub const SkillCommandEvent = struct {
    // The Command Event to execute
    command_event_type: SkillCommandType = .ApplySkillEffect,

    // Arg types and their values.  Commands can use as they want
    //TODO:DEFERRED:VALIDATION: Doing validation here is a different level, and I dont even want to plan it now.  It will over-complicate things immediately.  Deferred
    float_args: []f32 = &[_]f32{},
    int_args: []i32 = &[_]i32{},
    bool_args: []i32 = &[_]i32{}, // 0=False, 1=True.  Can't use bools with my system, too hard to change it right now.  Considered it 1 less data type to manage, and only 1 more conversion.  Deal
    text_args: []TextArray = &[_]TextArray{},

    // Special Data enums, using @enumFromInt(value)
    target_detail_args: []i32 = &[_]i32{}, // @enumFromInt(SkillTargetDetail)
    fx_visual_args: []i32 = &[_]i32{}, // @enumFromInt(SkillVisualEffect)
    fx_post_args: []i32 = &[_]i32{}, // @enumFromInt(SkillPostEffect)
    fx_audio_args: []i32 = &[_]i32{}, // @enumFromInt(SkillAudioEffect)
    fx_audio_playback_args: []i32 = &[_]i32{}, // @enumFromInt(SkillAudioPlayback)
};

pub const SkillCost = struct {
    pay_with_stat: StatType = .None, // This is the Stat we use to pay for this skill (ex: Stamina, Mana)
    cost: f32 = -1, // This is how much we must pay for this stat
    cost_period: f32 = 0, // If 0, cost is immediate.  If >0, cost is paid every N seconds or turn
};

pub const SkillEffect = struct {
    stat_affected: StatType = .None, // What is being changed?
    base_modifier: f32 = 0,
    base_modifier_type: SkillModifierType = .Additive,

    multiplier: f32 = 1.0,
    multiplier_type: SkillModifierType = .Additive,
    curve: Curve = .Linear,
    logic_block_id: i32 = -1, // game.logic_block.#
};

//NOTE: Use this by taking all the states of Parent A and B (if exists), to create base_value on manual trigger update
//NOTE: Each implementation (WorldItem, Entity) needs it's own implementation to use "parent" because we use Data Router to map buttons to them by struct name, and the db.table must match
pub const SkillLevelInfoScaling = struct {
    // Parent A.  Value = A+B
    parent_a_id: SkillType = .None, // First parent entity id (-1 = none)
    parent_a_level_index: i32 = 0,

    scalar_a: f32 = 0, // Multiplied by the curve value
    curve_a: Curve = .Linear,
    curve_a_value: f32 = 1, // 0-1, gets the Curver scalar to multiple scalar_a by parent_id_a's stat base_value

    // Parent B
    parent_b_id: SkillType = .None, // Second parent entity id (-1 = none)
    parent_b_level_index: i32 = 0,

    scalar_b: f32 = 0, // Multiplied by the curve value
    curve_b: Curve = .Linear,
    curve_b_value: f32 = 1, // 0-1, gets the Curver scalar to multiple scalar_b by parent_id_b's stat base_value
};

pub const SkillLevelAddFollower = struct {
    content_import_id: i32 = -1, // Fire, lightning, bees visual
    duration: f32 = 0, // If 0, then lasts duration of the Envelope, else this is a timer
};

pub const SkillLevelInfo = struct {
    level: i32 = 0,

    // Activation Animation and Speed
    animation: content_item.ContentAnimation = .Idle,
    speed_type: entity_lib.MovementSpeedType = .Idle,

    // If true, will move away from Target, instead of toward the target
    invert_direction: bool = false,

    // Targeting
    targeting_mode: SkillTargetingMode = .SingleTarget,
    targeting_radius: f32 = 300,
    targeting_angle: f32 = 90, // For cones
    targeting_range: f32 = 150,

    duration_time: f32 = -1, // For time-based effects
    duration_turns: i32 = -1, // For turn-based effects

    // How do we handle getting activated when we already have duration?
    refresh_duration_method: SkillDurationRefreshType = .Blocked,

    // Conditional Rule Set.  Entity has to pass this Condition to be able to be targetted with this Skill
    condition_prolog_rule_set_a_id: i32 = -1,
    condition_name: Text = Text.initEmpty(),
    condition_logic_block_id: i32 = -1, // game.logic_block.#

    // If it succeeds, what logic block should be run to do whatever needs to be done that isnt part of the system.  Launch custom UI or play an event sound
    effect_logic_block_id: i32 = -1, // game.logic_block.#

    // If 0, this is continuous.  Otherwise this is a "Ticker", and every N seconds, this will be applied
    update_tick: f32 = 0,

    // Animation binding
    animation_id: i32 = -1, // game.animation.id
    lock_movement_during_animation: bool = true,
    lock_rotation_during_animation: bool = false,
    can_cancel_animation: bool = false,

    // Follower on Envelope
    create_follower: SkillLevelAddFollower = .{},

    // Range requirements
    min_range: f32 = 50,
    max_range: f32 = 100, // 0 = infinite
    requires_line_of_sight: bool = true,

    // Dynamic cooldown
    cooldown_reduction_on_success: f32 = 0,
    cooldown_reduction_on_kill: f32 = 0,
    cooldown_reset_on_condition_logic_block_id: i32 = -1,

    // Cost per the cost_stat
    cost: i32 = 0,
    cooldown: f32 = 0,
    can_stack: bool = true, // Can these effects compound?
    override_priority: i32 = 0, // If it can't stack, the highest priority will be the one used

    // Costs: All must be paid.  AND not OR.  Can be multiplied by LB to modify for special cases
    costs: []SkillCost = &[_]SkillCost{},
    cost_multiplier_logic_block_id: i32 = -1, // Can increase or decrease costs

    // Charging
    is_chargeable: bool = false,
    charge_time_min: f32 = 0,
    charge_time_max: f32 = 3,
    charge_power_curve: Curve = .Linear,

    // "Do I land this?" (hit chance)
    success: SkillEffect = .{},
    failure_logic_block_id: i32 = -1, // game.logic_block.#

    // "How hard does it hit?" (damage/effect magnitude)
    intensity: SkillEffect = .{},

    // "How much does target resist?" (from attacker's perspective)
    target_defense: SkillEffect = .{},

    // Immunity modifier
    immunity: SkillEffect = .{},

    // Remove modifier
    remove: SkillEffect = .{},

    // Grant modifier
    grant: SkillEffect = .{},

    // Charge system
    use_charges: bool = false,
    max_charges: i32 = 1,
    charge_regen_time: f32 = 0, // Seconds per charge

    // Combo requirements
    requires_recent_skill: SkillType = .None,
    requires_recent_skill_window: f32 = 0, // Seconds

    // Interruption
    can_be_interrupted: bool = true,
    interrupt_on_damage: bool = false,
    interrupt_on_stun: bool = true,
    interrupt_on_movement: bool = false,

    // Scaling
    scaling: SkillLevelInfoScaling = .{},

    // Preview FX
    preview_visual_effect: i32 = -1, // Show while targeting
    preview_radius_color: Color = .{},
    preview_cone_color: Color = .{},

    // FX
    fx_visual: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillVisualEffect)
    fx_visual_post: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillPostEffect)
    fx_audio: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillAudioEffect)
    fx_audio_playback: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillAudioPlayback)
};

pub const SkillItem = struct {
    // Skill to Modify
    //NOTE: Skills are more encyclodepic.  Everything I have has to be represented as a Skill, this is the source of truth for how we do animations and stuff, all can be leveled up.  Actors have Skills
    skill_type: SkillType = .None,

    // If not None, this activates via on Action, and doesn't use the EquipmentSlot method.  We check for EqipmentSlots first, and if not found, we check the skills for this Action match
    invoked_by_action: ActionType = .None,

    // Block this Skill from being used
    immunity_skill_type: SkillType = .None,

    // Remove an Effect on the Entity
    remove_skill_type: SkillType = .None,

    // Grant new abilities
    grant_skill_type: SkillType = .None,

    // Refuse to Execute this skill if the Entity has either these active or passive skills
    refuse_execute_if_has_active_skills: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillType)
    refuse_execute_if_has_passive_skills: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillType)

    // Level Blending
    use_level_blending: bool = false,
    level_blending_type: SkillLevelBlending = .Closest,
    level_blending_curve: Curve = .Cubic,
    level_blending_include_size: i32 = 2,

    // Target Detail
    target_detail: SkillTargetDetail = .None,

    // Are they invulnerable during this skill?  ex: Hit, can't keep hitting them while they are animating this
    is_invulnerable: bool = false,

    // Can this skill be interrupted?
    can_interrupt: bool = true,

    // FX
    fx_visual: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillVisualEffect)
    fx_visual_post: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillPostEffect)
    fx_audio: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillAudioEffect)
    fx_audio_playback: []i32 = &[_]i32{}, // i32 -> @enumFromInt(SkillAudioPlayback)

    // Levels for all our Skill types
    levels: []SkillLevelInfo = &[_]SkillLevelInfo{},

    // Execute commands by event label and lists of args
    execute_command_event: []SkillCommandEvent = &[_]SkillCommandEvent{},
};

//NOTE: Use in place of the GAS-Tags concept of effect tagged hierarchically (Status.Debuff.Poison.Fire)
pub const SkillSet = struct {
    name: Text = Text.initEmpty(),

    // Skills
    skills: []SkillItem = &[_]SkillItem{},

    // Sub-Skills
    children: []SkillSet = &[_]SkillSet{},
};
