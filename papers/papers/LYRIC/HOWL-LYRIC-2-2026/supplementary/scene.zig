const std = @import("std");
const rl = @import("raylib");
const math = std.math;

const entity_lib = @import("entity.zig");
const skill_set_lib = @import("skill_set.zig");
const trace_lib = @import("trace.zig");
const level_data_lib = @import("level_data.zig");
const content_item = @import("content_item.zig");
const prolog = @import("prolog.zig");
const canvas_layout = @import("canvas_layout.zig");
const spawner_lib = @import("spawner.zig");
const progress_course = @import("progress_course.zig");
const ui_element = @import("ui_element.zig");
const networking = @import("networking.zig");

// Types
const Vector2 = @import("vector2.zig").Vector2;
const Number = @import("number.zig").Number;
const Text = @import("text.zig").Text;
const TextArray = @import("text_array.zig").TextArray;

const Entity = entity_lib.Entity;
const EntityTrace = trace_lib.EntityTrace;
const EntityType = entity_lib.EntityType;
const EntitySkill = entity_lib.EntitySkill;
const StatType = entity_lib.StatType;
const SkillType = skill_set_lib.SkillType;
const LevelData = level_data_lib.LevelData;
const ContentAnimation = content_item.ContentAnimation;
const CanvasLayout = canvas_layout.CanvasLayout;
const Curve = entity_lib.Curve;
const ProgressStage = progress_course.ProgressStage;
const ProgressStageType = progress_course.ProgressStageType;
const Spawner = spawner_lib.Spawner;
const UiContainerStack = ui_element.UiContainerStack;
const SceneNetworkBuffers = networking.SceneNetworkBuffers;

pub const SceneRectShader = enum(i32) {
    None,
    Outline,
};

pub const SceneRenderCommand = struct {
    // Entity
    id: i32 = -1, // Image or ContentImport
    entity_id: i32 = -1,
    entity_type: EntityType = .None,

    // Where to source from the image
    rect_source: rl.Rectangle = .{ .x = 0, .y = 0, .width = 0, .height = 0 },

    // Where to draw on the canvas
    rect_dest: rl.Rectangle = .{ .x = 0, .y = 0, .width = 0, .height = 0 },

    // Origin
    origin: rl.Vector2 = .{ .x = 0, .y = 0 },

    // Rotation
    rotation: f32 = 0,

    // Render Direction:  Rotation could change this, or set this directly.  Rendering uses this
    direction: content_item.ContentDirection = .East,

    // Tint
    tint: rl.Color = rl.Color.white,

    // Shader name to use with is image
    shader: SceneRectShader = .None,

    // Actor Data
    scale: f32 = 0,
    anim: ContentAnimation = .None,
    anim_frame: i32 = 0,
    anim_frame_updated_time: f32 = 0,

    // If needs Text
    text: Text = Text.initEmpty(),
};

pub const SceneRender = struct {
    // Render Commands
    render_command_count: i32 = 0, // Current render commands for this frame, we dont free the render commands, we just expand them forever and never free, and use this to limit per frame, so we dont leak
    render_commands: []SceneRenderCommand = &[_]SceneRenderCommand{},

    // Track Actor start/stop index, these are the only things that need to be sorted in our Render list, everything else is sorted on append
    actor_start_index: i32 = -1,
    actor_end_index: i32 = -1,
};

pub const EntityPairDataItem = struct {
    distance: f32 = 0,
    facing_angle: f32 = 0,
    relative_angle: f32 = 0,
    is_in_front: bool = false,
    is_behind: bool = false,
};

pub const EntityPairData = struct {
    items: []EntityPairDataItem = &[_]EntityPairDataItem{},

    // Refined data from all
    closest_actor: i32 = -1,
    dist_closest_actor: f32 = std.math.floatMax(f32),

    closest_human: i32 = -1,
    dist_closest_human: f32 = std.math.floatMax(f32),

    closest_actor_front: i32 = -1,
    dist_closest_actor_front: f32 = std.math.floatMax(f32),

    closest_human_front: i32 = -1,
    dist_closest_human_front: f32 = std.math.floatMax(f32),
};

pub const ActionSkillStatEnvelope = struct {
    // If false, dont use.  Can have arrays and ignore/replace deleted to reuse mem
    is_deleted: bool = false,

    // Is a "On Cast" envelope type?  If true, then it stays the same throughout the duration, despite any math set up for change.  If not, then the change math is respected
    is_on_cast_type: bool = false,

    // This is unique, all actions are unique (wraps over at max i32), so that we know this specific ID, and can compare if we need to disambiguate or match
    //NOTE: Can have multiple envelopes if they affect more than 1 stat
    global_action_id: i32 = -1,

    // Entity and Stat affected
    source_entity_id: i32 = -1,

    // Entity who initiated the action, such as the summoner who summoned `source_entity_id` and gets rewards
    instigator_entity_id: i32 = -1,

    // Target information
    target: entity_lib.EntityTarget = .{},

    // All targets, including the selected/closest target in `target_entity_id` which is included in this list, unordered
    group_target_entity_ids: []i32 = &[_]i32{},

    // Skill used and Stat affected.  We make 1 envelope for every stat affected, so they can have different envelopes, time out differently.  They have same global_action_id
    skill: SkillType = .None,
    stat: StatType = .None,

    // Lifetime.  If instant, this is the same as time_start, and will only be processed 1 frame, but we let every actor react to it
    time_start: f32 = -1,
    time_end: f32 = -1,

    // If turn based, use this
    turn_start: i32 = -1,
    turn_end: i32 = -1,

    // Cancellation, if the caster/doer dies.  For magic yes, not if burning oil
    cancel_on_source_unconscious: bool = true,
    cancel_on_instigator_unconscious: bool = false,

    // Execution Priority: Highest is first.  Determine the order envelopes are processed each update per Entity involved
    execution_priority: i32 = 0,

    // If not .None, this will trigger an Event with the Entity (ex: Hit, Die, Death)
    force_transition_by_event: content_item.ContentEventType = .None,

    // Value
    modifier: f32 = 0,
    modifier_type: skill_set_lib.SkillModifierType = .Additive,
    curve: Curve = .Linear, // Curve is 0-1 based on the (time_end-time_start)
    modifier_logic_block_id: i32 = -1, // Custom modifier from code
};

pub const ObjectRectType = enum(i32) {
    None = -1,

    SpawnArea = 1000,
    SpawnPoint, // Only spawn at the Pos, not in the Area
};

pub const ObjectRect = struct {
    rect_type: ObjectRectType = .None,

    pos: rl.Vector2 = .{},
    size: rl.Vector2 = .{},
    scale: f32 = 1,

    // Content
    content_import_id: i32 = -1,

    // If we have a DB entry (game.object.?  not sure yet.  world_item_id?)
    game_entity_id: i32 = -1,

    // Owner Entity
    owner_entity_id: i32 = -1,

    // Controller for this Entity.  It will update() and do things
    controller_entity_id: i32 = -1,
};

pub const Scene = struct {
    // Display name
    name: Text = Text.initEmpty(),

    is_paused: bool = false,

    // Explicitly track the Progression of the game for the Player's experience.  Determines SpawnGroups spawned
    progression: ProgressStageType = .SinglesSparse,
    progression_progress: f32 = 0, // 0-1, when we reach 1, we bump `progression` to the next stage

    // Levels
    levels: []LevelData = &[_]LevelData{},

    // Actors
    actors: []Entity = &[_]Entity{},

    // Canvas Layout
    layouts: []CanvasLayout = &.{},

    // We only have 1 layout active at once, if -1 none are active
    active_layout: i32 = -1,

    // Simple objects.  Trees or whatever we want to have graphics and be able to interact with, but dont need updates or much info.  Stationary
    objects: []ObjectRect = &[_]ObjectRect{},

    // Spawner.  Has N groups
    spawner: Spawner = .{},

    // All our render data, sealed in a struct so its not a mess in list
    render: SceneRender = .{},

    // Trace
    trace_actors: []EntityTrace = &[_]EntityTrace{},

    // Fact Sets
    fact_set_levels: []prolog.FactSet = &[_]prolog.FactSet{},
    fact_set_actors: []prolog.FactSet = &[_]prolog.FactSet{},

    // Entity Pair Data
    actor_pair_data: []EntityPairData = &[_]EntityPairData{},

    // All Actor Effects still alive during this frame or turn
    action_envelopes: [20]ActionSkillStatEnvelope = [_]ActionSkillStatEnvelope{.{}} ** 20, //TODO: Make bigger after testing.  1000 or 2000 maybe, oversized
    next_global_action_id: i32 = 0,

    // // Scene Networking
    // network: SceneNetworkBuffers = .{},

    // Canvas Bounding Box
    canvas_bbox: rl.Rectangle = .{},

    // UI Container Stack
    ui_stack: UiContainerStack = .{},

    // UI Command - Will create UiElements for the Canvas section in Data Browser, or the full screen in real game
    ui_command: Text = Text.initEmpty(),

    // Time and Frame
    game_time: f32 = 0,
    game_frame: i32 = 0,
    game_time_ui: f32 = 0,

    // Deterministic frame Random Seed
    game_seed: i32 = 0,

    // Are we in dev mode?  If so, player can change anything in the scene, but not other scenes with this InputPlayer.auth_token, they will need a different token for a different scene
    //TODO: Local player login can be an optional restriction to using Silo, with screen lock optional as well, default off and default 20 minutes.
    is_dev_mode: bool = false,
    is_network_dev_mode: bool = false, // If true, this allows dev level players

    // 3D Renderer, if false 2D
    is_3d: bool = false,

    // If not -1, we replace fields like "Entity.character.heath" with "InsideAccount.last_month.revenue", and now the user sees that.  Entity can override this, if they have their own valid replacement id
    silo_field_replacement_id: i32 = -1,

    // Canonical update Delta Time, everything should use this, so that we can check pause and force to 0 and all systems will use it
    delta_time: f32 = 0,
    delta_time_ui: f32 = 0, // Always updates, even if we set `delta_time=0` because we are paused, UI will keep a delta_time
};

pub const SceneToSceneActorClone = struct {
    // From scene
    from_scene_id: i32 = -1,

    // From actor ID (not index)
    from_actor_id: i32 = -1,

    // To an actor in our scene
    to_actor_id: i32 = -1,

    // Every N frames.  If 1, every frame.  If 0, never.  If more than 1, every N frames
    every_n_frames: i32 = 1,

    // If any exist, only copy data paths that match these globs.  Positive filter, not negative.  Only matches will copy
    child_path_filter: []TextArray = &[_]TextArray{},
};

//NOTE: This becomes an OS and Window manager.  Multiple games = multiple apps, at once.  Apps can be floating tools, and access everything, including inspecting whats going on under the mouse in scene_id
pub const SceneSetItem = struct {
    // game.scene.`scene_id`
    scene_id: i32 = -1,

    is_maximized: bool = true, // Using the full Scene.canvas_bbox.  `update_speed` used for Scene.update(deltaTime * update_speed)
    is_minimized: bool = false, // Is hidden, doesnt render.  May update depending on `update_speed_minimized`
    show_minimized_button: bool = false, // If minimized, should we show a button at the selected border to bring this window back?
    is_floating: bool = false, // If true, render into the float_rect inside canvas_bbox
    floating_rect: rl.Rectangle = .{},

    // 1 = Full speed.  This is: deltaTime * update_speed for this Scene.update(deltaTime)
    update_speed: f32 = 1,
    update_speed_minimized: f32 = 0,

    // Rendering, Input, Move and Resize
    z_order: i32 = 0, // which floating window is on top
    is_focused: bool = false, // receives input
    drag_handle_rect: rl.Rectangle = .{}, // for window dragging, if size==0,0, cant drag
    resizable: bool = false, // can user resize floating_rect

    // Which scenes can read and write to this scene?  By default, no one.  In Silo OS mode, we allow the Network Entity to read and write into our network bufferent
    allow_read_scene_ids: []i32 = &[_]i32{},
    allow_write_scene_ids: []i32 = &[_]i32{},
    // Scene data child-paths that are allowed to use for read and write.  Consider: write: `actors.input.players`.  Positive matches only, if we dont match and any cases exist, denied
    allow_write_paths: []TextArray = &[_]TextArray{},
    allow_read_paths: []TextArray = &[_]TextArray{},

    // Clone from Scene
    clone_from_scene_actors: []SceneToSceneActorClone = &[_]SceneToSceneActorClone{},
};

pub const SceneSetManager = struct {
    items: []SceneSetItem = &[_]SceneSetItem{},
};
