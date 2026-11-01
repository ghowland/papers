// resource_system.zig - The Resource System struct:  Economy as Gamepay and more.  Total control using Resources
//
// Dependencies:  turn -> exec -> data -> resource_system.zig
//
const std = @import("std");
const platform = @import("../../platform.zig");

const rl = @import("raylib");

const time = @import("../../lib/time.zig");

// Types
const Text = @import("text.zig").Text;
const TextSmall = @import("text_small.zig").TextSmall;
const Vec2 = @import("vec2.zig").Vec2;
const Vec2Int = @import("vec2int.zig").Vec2Int;
const Rect = @import("rect.zig").Rect;
const Curve = @import("entity.zig").Curve;
const Color = @import("color.zig").Color;
const content_item = @import("content_item.zig");
const ContentIcon = content_item.ContentIcon;

// If true, more prints will occur
pub const IsDebug = false;

// Zig Types
const fixed = @import("fixed.zig");
const Fixed = fixed.Fixed;
const Fixed2 = @import("fixed2.zig").Fixed2;
pub const ResourceUnset = fixed.FixedUnset; // Unset: this value is not set

// How many seconds in a Turn, for a Real Time game?  This allows tuning what the Turn Based values mean in a real-time game, and becomes a slider for everything that deals with time in one value
pub var RealTimeTurnInSeconds: f32 = 1.0;

// Resource Group Core - Turn Based gating and whether they are active
const GateDecisionResourceGroup: i32 = 1; // Are they turn based and gated?
const GateDecisionActiveResourceGroup: i32 = 2; // Are they currently active?

// Resource Group Parents - System Builtins usable by all games
const RenderLayerParentResourceGroup: i32 = 3;
const AnimationParentResourceGroup: i32 = 4;
const MaterialParentResourceGroup: i32 = 5;

// -- Enums --

pub const ResourceUsageType = enum(i32) {
    None = -1,
    Player = 0,
    Editor,
    EditorWithUsage,
};

pub const ResourceLinkType = enum(i32) {
    None = -1,
    Resource = 0,
    DataPath,
    ResourceEvent,
    ResourceConversion,
    ResourceConversionSet,
    ResourceSet,
    ResourceStoreFront,
    ResourceTrigger,
    ResourceCalculation,

    // Additional Types
    PrologFlowConfig = 1000,

    // Actors can reference each other in conversion sets, like Relationships
    SceneActorIndex = 2000,

    // Tile Layer: reads and writes tile layer values at entity position
    TileLayer = 3000,
};

// Which phase of the turn produced this transaction
pub const ResourceTransactionPhase = enum(i32) {
    None = -1,
    Upkeep = 0,
    Production,
    EnvelopeTurn,
    EnvelopeNonTurn,
    Trigger,
    Sequence,
    Flow,
    Manual,
};

// Hauling targets
pub const ResourceZone = struct {
    // Allowed Resource Groups are all named, if they are a Parent type, then all their children would be allowed
    resource_group_ids: []i32 = &.{},

    // Tile Rect, we only use the Integer output of Rect (Rect.pos.x.int) to match our tiles
    rect: Rect = .{},

    // Highest wins, given multiple matching zones
    priority: i32 = -1,

    // Visualization Color
    color: Color = Color.YELLOW,
};

pub const ResourceEvent = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    owner_entity_id: i32 = -1,
    target_entity_id: i32 = -1,

    conversion_set_id: i32 = -1,
};

pub const ResourceTrigger = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // Poll configuration
    poll_interval_frames: i32 = 0,
    poll_interval_seconds: f32 = 0,

    // Condition
    condition_resource: ResourceLink = .{},
    condition_min_value: Fixed = 0,
    condition_max_value: Fixed = 0,

    // Event to fire
    resource_event_id: i32 = -1,

    // State
    is_active: bool = true,
    entity_id: i32 = -1,
};

pub const ResourceEnvelope = struct {
    id: i32 = -1,

    owner_entity_id: i32 = -1,
    possessed_by_player_id: i32 = -1, // If a player is possessing the owner, we track it, for full provenance that a player did this themselves vs UAI
    target_entity_ids: []i32 = &[_]i32{},

    conversion_set_id: i32 = -1,

    // Delivery timing
    is_instant: bool = true,
    duration_seconds: f32 = 0, // Real-Time version
    elapsed_seconds: f32 = 0,
    duration_turns: i32 = 0, // Turn based games
    elapsed_turns: i32 = 0,

    // Usage mode
    usage_type: ResourceUsageType = .Player,

    // Scale and Forced
    scale: Fixed = fixed.FIXED_ONE,
    is_forced: bool = false,

    command_success: Text = Text.initEmpty(), // command name to execute on transaction success
    command_failure: Text = Text.initEmpty(), // command name to execute on transaction failure
    equip_instance_id: i32 = -1, // != -1: this envelope requests equip of this inventory instance id
    unequip_slot_group_id: i32 = -1, // != -1: this envelope requests unequip of this slot group

    // If != -1, this Envelope is used to create a Scene Actor next frame, and will be processed in a pre-pass before Entity Logic loops through Actors, so they all exist before
    create_actor_player_id: i32 = -1, // Owner for this Actor is Player, actor will be created with Player as owner, as a pre-pass and then set to is_deleted=True
    create_from_entity_id: i32 = -1, // This is the game.entity.{id} to clone this Entity struct from

    // Can perform any silo function, but Field Operations are a common case, and can be used on Resource Instance values directly, (Grow Shrink), or more commonly through TileData inside LevelDataLayers
    //  Field Operations are 3D aware, and LevelDataLayers all have their above/below links for all layer types (`render_resource_group_id` is data as well as rendered, this is "visualize" not draw)
    execute_author_programs: []i32 = &.{},

    // We dont remove these, we just mark them deleted so they can be repopulated in our scene list later
    is_deleted: bool = true,
};

pub const ResourceSequence = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    conversions: []ResourceConversion = &[_]ResourceConversion{},
    current_index: i32 = 0,

    // Advancement
    advance_on_time: bool = false,
    advance_interval_seconds: f32 = 0,
    is_looping: bool = false,
};

//TODO: In scene, we could
pub const ResourceTransaction = struct {
    id: i32 = -1,

    source_entity_id: i32 = -1,
    target_entity_id: i32 = -1,

    conversion_set_id: i32 = -1,

    // Result
    is_valid: bool = false,

    // Failures
    //NOTE: Persisted record: these live on di.allocator.?, never frame memory
    failed_cost_indices: []i32 = &[_]i32{}, //TODO: Change to fixed size, this creates a problem for storage of transactions.  Maybe 10 max is fine, can expand as required, use constant
    failed_requirement_indices: []i32 = &[_]i32{}, //TODO: Change to fixed size, this creates a problem for storage of transactions.  Maybe 10 max is fine, can expand as required, use constant

    // Mode
    usage_type: ResourceUsageType = .Player,

    // Append-only ledger: the walk marker.  We never shrink the list, we
    // find the record with _is_last==true, write the next one, and move the
    // marker.  scene.resource_transaction_last_index caches the position
    _is_last: bool = false,

    phase: ResourceTransactionPhase = .None,
    order: i32 = -1, // monotonic within a turn
    scale: Fixed = fixed.FIXED_ONE,
    is_forced: bool = false,
    is_applied: bool = false, // built-and-inspected vs built-and-submitted
    reason: TextSmall = TextSmall.initEmpty(), // first failing check, empty on pass
    envelope_slot: i32 = -1, // -1 = not from an envelope
    game_frame: i32 = -1,
    game_time: f32 = -1,

    //TODO:DEFERRED: per-group value deltas (before/after).  The conversion set id, scale and is_forced reconstruct the INTENDED movement; these
    //  would record the OBSERVED movement.  Add once a turn has run and we know which shape the UI wants value_deltas: []ResourceValue = &[_]ResourceValue{},

    // If we are deleted, we can be reused after a deep data reset, also we should never be selected or shown, or counted, unless `is_deleted=true` is specified
    //TODO: Enforcing `is_deleted` and `game_id=CurrentGameId` could be really really interesting
    is_deleted: bool = false,
};

pub const ResourceStoreFront = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // game.ui_image.{} - Image for this Store, not the items
    image_id: i32 = -1,

    owner_entity_id: i32 = -1,
    conversion_set_id: i32 = -1, // No resource_group_id, because we use this instead

    // Access control
    is_active: bool = true,
    requires_proximity: bool = false,
    proximity_range: Fixed = 0,
    is_one_time_use: bool = false,

    // Usage mode override
    usage_type: ResourceUsageType = .None,

    // Opens Menu Manager ID and Menu Data Index
    menu_manager_id: i32 = -1, // game.menu_manager
    menu_manager_menu_data_index: i32 = -1, // game.menu_manager.{id}.data_menu_manager.menus[index]
};

pub const ResourceLink = struct {
    group: i32 = -1,
    link_type: ResourceLinkType = .None,
    data_path: Text = Text.initEmpty(),
    record_id: i32 = -1,
    value: Fixed = ResourceUnset,
};

pub const ResourceConversion = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // Conversion endpoints
    from: ResourceLink = .{},
    to: ResourceLink = .{},
    from_value: Fixed = 0,
    to_value: Fixed = 0,

    // If true, this is a Set, and not an Add.
    is_set: bool = false,
    from_value_resource_group_id: i32 = -1, // Set come from `from` side resource_group_id
    to_value_resource_group_id: i32 = -1, // Set come from `to` side resource_group_id

    // Parent scaling: game.resource_conversion.{parent_a}
    parent_a: i32 = -1,
    parent_b: i32 = -1,
    scale_a: Fixed = fixed.FIXED_ONE,
    scale_b: Fixed = fixed.FIXED_ONE,
    total_scale: Fixed = fixed.FIXED_ONE,

    // Curve
    curve: Curve = .Linear,
    default_value_curve_value: Fixed = fixed.FIXED_HALF,

    // Spawn a Entity as an Actor for this Player.  Everything the Entity needs is already on it, all it needs is to set `Entity.owned_by_player_index` to the Player index
    create_from_entity_id: i32 = -1,

    // If !=-1, this will trigger an Event on successful completion.  This is also used in MenuManager when a menu item goes from enabled==false to true, so we alert the player of UI changes
    trigger_resource_event_id: i32 = -1,

    // Directional constraints
    is_only_increasing: bool = false,
    is_bidirectional: bool = false,
    bidirectional_reverse_scale: Fixed = fixed.FIXED_ONE,

    // Sequence membership
    sequence_index: i32 = -1,

    // Set membership
    resource_conversion_set_id: i32 = -1,

    // UAI Consideration Minimum Value, allows us to set default Conversions, even if it scores 0, it will be given this minimum value
    consideration_min_value: Fixed = 0,
    // Allows us to have areas in the Range that are 0s, giving us the ability to set dead zones.  It's an override system
    consideration_zero_ranges: []Fixed2 = &[_]Fixed2{},
};

pub const ResourceConversionSet = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // This is how we sort ConversionSets, we use ResourceGroups, because then we only have 1 labeling mechanism.
    resource_group_id: i32 = -1,

    // If not -1, we clone any missing costs or requirements
    clone_missing_values_from_id: i32 = -1,

    costs: []ResourceConversion = &[_]ResourceConversion{},
    requirements: []ResourceConversion = &[_]ResourceConversion{},

    // Utility AI Considations, for treating a Conversion Set as an action (Behavior), so we can put them all together and test it
    considerations: []ResourceConsideration = &.{},
    force_min_value: Fixed = 0, // This is the minimum value this item can be, allowing it to be a default.  Even if it's considerations are 0, it will be this value, as the minimum

    // Duration: Time or Turns.  Allows conversion sets to translate into game time for visualization and delay
    duration_time: f32 = content_item.F32Unset, // If !=F32Unset, this is how many seconds conversion set requires to complete.  If F32Unset, this is instant
    duration_turns: i32 = -1, // If !=1, this is how many turns this conversion set requires to complete.  If ==-1, this is instant
    animation_resource_group: i32 = -1, // If !=-1, Animation Group to perform this ConversionSet for the duration must exist on Entity for this Conversion Set to trigger, and plays for duration.  If ==-1, no anim
    //NOTE: If false, and the "Interaction" can be done at a distance, an Archer could fire an arrow at the ContentFrame, hitting it causing this to be triggerable from a distance (Exploding Barrel)
    animation_in_tile: bool = true, // If true, the actor moves into this tile and animates (Bed, Cow on Grass).  If false, the actor animations to it's interaction distance and animates (Workbench, Tree)

    //TODO: This is not the correct way to handle this, placeholder, the data format will be different, maybe a list, or to a struct, im not sure yet, placeholder on the concept.  It needs to handle N, fan out
    success_silo_operation_id: i32 = -1,
    failure_silo_operation_id: i32 = -1,

    // If !=-1, this ConversionSet is based on this Goal, and when the Goal is active (UAI), then this Conversion Set becomes a candidate for the Goal's action (UAI)
    resource_goal_id: i32 = -1,

    // If true, this can be assigned by a Player to `Entity.ai_job_resource_conversion_set_ids`
    is_actor_job: bool = false,
};

//TODO: How do a do a reference to content_import_id from the Group here, can have "Content Import ID" as a known group name, and just hard code that.  Is that good enough, or do I need more?
pub const ResourceValue = struct {
    group: i32 = -1,
    value: Fixed = ResourceUnset,

    // Min antd Max values, if Unset, the bound is not enforced
    limit: Fixed2 = .{ .x = 0, .y = ResourceUnset },

    // The limit.x floor will be authored directly, but the Max of a resource is often a group value itself.  Instead of having a separate lookup, we can set the limit.y directly per update from our group_id
    max_resource_group_id: i32 = -1, //TODO: Not yet implemented

    // If we have a valid min and max, then the value is sampled from between the limit using this curve.  ex: val=7, min=0, max=10, curve=Linear so output is 7.  If it was Logarithmic, the value would be higher
    limit_curve: Curve = .Linear,

    // game.resource_calculation.{id}.data_resource_calculation is ResourceCalculation.  If this is not -1, then the value is the result of the calculation * calculation_scale, worked through `limit_curve`
    //      When calculation is in use, `value` is the cache this `game_frame`
    resource_calculation_id: i32 = -1,
    resource_calculation_scale: Fixed = fixed.FIXED_ONE, // Scale the calculation result.  We could have 3 different "weapons" using the same calculation, but they scale it 0.7, 1.0, 2.5 giving different results
    resource_calculation_game_frame: i32 = -1, // If this is not the current game_frame, we re-calculate and store in `value`.  If it is, we use `value` as the cache

    // This is an Inventory multiplier.  If this is a ResoureValue in Entity.inventory_resources, then we can use this to count arrows of the same props, so we dont need to have N of them
    stack_size: i32 = 1, //TODO: This is not wired into the resource_engine system yet

    // Mark the Game Frame when updated, if it's the same value, dont update unless `forced=true` option was presented
    updated_game_time: f32 = -1, // Game Time is seconds since the game started, advancing through deltaTime, not wall time.  So pausing the game freezes game_time, making this consistent in nature //TODO: -> Fixed

    pub fn isUnset(self: ResourceValue) bool {
        if (self.value == ResourceUnset) return true;
        return false;
    }

    pub fn isTrue(self: ResourceValue) bool {
        if (self.value == fixed.FIXED_ONE) return true;
        return false;
    }

    //NOTE: No `force` concept to update the timer, it updates when the value changes, so setting it every frame to the same thing never counts as an update, it has to change value
    pub fn setBool(self: *ResourceValue, value: bool, game_time: f32) void {
        if (value) {
            // If this wasn't 1, then update it, if the value is changing
            if (self.value != fixed.FIXED_ONE) self.updated_game_time = game_time;

            // Always Update the Value
            self.value = fixed.FIXED_ONE;
        } else {
            // If this wasn't 0, then update it, if the value is changing or we are forcing the update
            if (self.value != 0) self.updated_game_time = game_time;

            // Always Update the Value
            self.value = 0;
        }
    }

    //NOTE: No `force` concept to update the timer, it updates when the value changes, so setting it every frame to the same thing never counts as an update, it has to change value
    pub fn setValue(self: *ResourceValue, value: Fixed, game_time: f32) void {
        // If the value is changing, then update it, if the value is changing
        if (self.value != value) self.updated_game_time = game_time;

        // Always Update the Value
        self.value = value;
    }
};

pub const ResourceCalculationItem = struct {
    // Find this Resource Groups value
    resource_group: i32 = -1,

    // If true, this Calculation Item does not use `resource_group`, and instead uses a random value between the limit.  If Unset, then unbounded
    is_random_value: bool = false,
    is_random_integer: bool = false, // If true, then only integer values are returned, in the f32 format

    // If not -1, this only looks for the `resource_group`, if it matches this slot index, so we can look for `Damage` but only from "Right Arm" slot
    inventory_slot_resource_group_id: i32 = -1,

    // This scales the resource_group.value we find, so we can change it at every point
    scale_value: Fixed = fixed.FIXED_ONE,

    // This is the min/max for the value, we can bound it again here, but by default we do not bound it
    limit: Fixed2 = .{ .x = ResourceUnset, .y = ResourceUnset },
    limit_curve: Curve = .Linear, // Like ResourceValue, this can also make the use a different curve for our limit, giving us more control over the outcomes in every element of the calculation

    raw_value: Fixed = ResourceUnset,

    // If this is the Base or Modifier lists, this is "value * -1" if this is in BaseScale or ModifierScale, this is "1 / value", which allows subtraction and division
    invert: bool = false,

    // Remainder after scale_value.  Group first, literal fallback - the same first-non-(-1)-match rule as everywhere else
    modulo_resource_group: i32 = -1,
    modulo_raw_value: Fixed = ResourceUnset,

    // Clamp against a live value instead of a literal.  -1 falls back to
    // limit.x / limit.y.  "Cap at my HP Max" stops being a hardcoded number
    limit_min_resource_group: i32 = -1,
    limit_max_resource_group: i32 = -1,

    // If true, the resource_group will be summed over all the owning player's entities that have these resource groups, so this becomes a sum calculation item
    is_player_sum: bool = true, //NOTE: By default, this should be true and we look at all our Actor's resources

    // If not Unset, only include actors within this Fixed distance from the owning actor (uses scene.actor_pair_data)
    nearby_actor_radius: Fixed = fixed.FixedUnset, //TODO: Not implemented yet, use `Scene.actor_pair_data`
};

// This allows us to compose values in a complex outcome with simple primitives, so that understanding it is not the same as an equation, it is the same everywhere in the game and becomes fluent natively
pub const ResourceCalculation = struct {
    // By default, any unset value in a Calculation is just skipped for adding/scaling, but if this is true, then any unset causes the calculation result to be unset
    //      This enables writing equations and allowing elements to simply be missing while getting valid results, and also allows making the entire calculation unset, because missing anything makes it invalid
    any_unset_returns_unset: bool = false,

    // Base is the original value, so like: 5.  We think of this as the original number
    base: []ResourceCalculationItem = &.{},
    // This allows us to scale the base in its own calculation, before we add the mod
    base_scale: []ResourceCalculationItem = &.{},

    // Modifier is what changes that value:  (5 * 1) + (-1 * 1) => 4.  We think of this as changing the original number based on parameters
    modifier: []ResourceCalculationItem = &.{},
    // This allows us to scale the modifier in its own calculation, before we add to the scaled base
    modifier_scale: []ResourceCalculationItem = &.{},

    // If True, floor the results
    floor_result: bool = false,
};

// ResourceObligation — Actor-to-actor conditional resource transfer through relationships.
//
// An obligation binds an actor to a response when a connected actor meets a condition.
// The beneficiary is identified by relationship label (Connection resource group and value),
// not by entity ID.  This allows obligations to follow relationship types: "owe your Lord"
// rather than "owe entity 47".
//
// The condition conversion set's requirements are evaluated against the beneficiary.
// If all requirements pass, the owning actor must execute the response conversion set.
// If the condition conversion set is -1, the obligation is always active (standing tax, tithe).
//
// Compliance is tracked as a resource group value on the owning actor (1 success, 0 failure).
// Success and failure fire resource events, enabling reputation changes, relationship damage,
// or cascading obligations.
//
// Examples:
//   Vassal tax:        beneficiary=Lord(40),    condition=-1 (always),        response=transfer gold
//   Military levy:     beneficiary=Lord(40),    condition=is_at_war,           response=commit units
//   Defensive pact:    beneficiary=Lord(40),    condition=is_under_attack,     response=mobilize defense
//   Social defense:    beneficiary=Lord(40),    condition=is_challenged,       response=spend influence
//   Family support:    beneficiary=Family(900), condition=is_starving,         response=transfer food
//   Tithe:             beneficiary=Priest(50),  condition=-1 (always),         response=transfer gold
pub const ResourceObligation = struct {
    // The obligation type: game.resource_group.{id} (ex: MilitaryLevy, Tithe, DefensePact, SocialDefense)
    resource_group_id: i32 = -1,

    // Beneficiary: the actor connected to the owning actor through this relationship
    //  resource_group_id selects the connection group (ex: 900 = ConnectionType), value selects the label (ex: 40 = Lord)
    //  If value is FixedUnset, the obligation applies to all actors in this connection group
    beneficiary_resource_group_id: i32 = -1,
    beneficiary_resource_group_value: Fixed = ResourceUnset,

    // Condition: game.resource_conversion_set.{id}.requirements evaluated against the beneficiary.  If all pass, the obligation is active
    //  If == -1, always active (standing tax, tithe)
    condition_conversion_set_id: i32 = -1,

    // Response: the conversion set the owning actor must execute when the condition passes
    response_conversion_set_id: i32 = -1,

    // Failure: event fired when the owning actor cannot meet the response conversion set costs or requirements
    failure_resource_event_id: i32 = -1,

    // Success: event fired on fulfillment
    success_resource_event_id: i32 = -1,

    // Compliance: game.resource_group.{id} on the owning actor, written to 1 on success, 0 on failure
    compliance_resource_group_id: i32 = -1,

    // Priority among obligations on the same actor.  Highest evaluated first when resources are scarce
    priority: i32 = 0,
};

pub const ResourceSet = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),
    name_short: Text = Text.initEmpty(),

    // If not -1, we clone any missing defaults, conversion_set_ids, labels and ensure inventory_slot_resource_group_id is aligned.  Allows authoring N of things that keep the structure but can have different values
    clone_missing_values_from_id: i32 = -1,

    // Default values any ResourceInstance starts with when created from the ResourceSet, they may change from there or not
    defaults: []ResourceValue = &[_]ResourceValue{},

    // What conversion sets apply to this Resource Set
    conversion_set_ids: []i32 = &[_]i32{},

    // What Resource Oblications apply to this Resource Set, we create them in ResourceInstance, like the defaults to values
    obligation_ids: []i32 = &[_]i32{},

    // Labels to apply to this Resource Set, allows both a Text and Index representation of discrete states from the resource values
    labels: []ResourceLabel = &[_]ResourceLabel{},

    // If this set goes into Entity.inventory_resources, then it can be equipped on an Entity, or and this gates on 1 Set equipped in this slot group id at a time.
    inventory_slot_resource_group_id: i32 = -1,

    // Because an Entity has this ResourceSet, we can assign them PrologFlowConfig IDs that they should execute for their Conext (game_id, scene_id, actor_index) every turn (or turn period in real-time)
    prolog_flow_config_ids: []i32 = &.{},
};

pub const ResourceInstanceObligation = struct {
    // game.resource_obligation.{id}.data_resource_obligation
    resource_obligation_id: i32 = -1,

    // How often this obligation is evaluated in game time (Fixed seconds).  If 0, every turn
    period: Fixed = 0,

    // Last time the condition was evaluated
    last_checked_game_time: Fixed = ResourceUnset,

    // Last time the obligation was fulfilled
    last_fulfilled_game_time: Fixed = ResourceUnset,

    // Last time the obligation was failed
    last_failed_game_time: Fixed = ResourceUnset,

    // Lifetime counters for reputation and history
    fulfilled_count: i32 = 0,
    failed_count: i32 = 0,

    // Current compliance state: FIXED_ONE = fulfilled, 0 = failed, ResourceUnset = not yet evaluated
    compliance_value: Fixed = ResourceUnset,

    // Scale the response conversion set for this instance
    response_scale: Fixed = fixed.FIXED_ONE,
};

//NOTE: ResourceInstance is compositional, when you equip a weapon, you just put the resource instance on your Entity.resources list
pub const ResourceInstance = struct {
    // Unique ID, we just increment this, so we can reference it
    id: i32 = -1,

    // This determines the Resource Set this instance copies any defaults from.  If any new ones are added, they will be imported into the ResourceInstance, it also contains the PrologFlowConfig IDs to execute
    resource_set_id: i32 = -1,

    // Values are named capabilities, and if you have `Damage` you deal damage, if you have `Elemental Fire` it becomes burning damage.  Everything is composition with calculations and resources
    //NOTE: Even content_import_id is expressed here, so equipping an item gives the information for rendering it to the screen, and if it doesnt exist, it doesnt get rendered, with order specified
    values: []ResourceValue = &[_]ResourceValue{},

    // Obligations that must be performed by Resource Group (ex: "Connection" parent groups: family, vassals, subjects)
    obligations: []ResourceInstanceObligation = &.{},

    // If not -1, this Instance is in our Inventory, Entity.inventory_resources[x].id==id, and we have equipped it here, and will need to copy the data back when we unequip it, as it may have changed values
    //NOTE: Note, only 1 resource group ID is allowed per Entity.resources, but in Inventory, they can be N.  Can use `ResourceValue.stack_size default = 1` to stack N items at a time
    inventory_slot_resource_group_id: i32 = -1,

    // If this is Entity.resources, this refers to the Entity.inventory_resources[x].id==equipped_id.  If this is Entity.inventory_resources, this refers to the Entity.resources[x].id==equipped_id
    equipped_id: i32 = -1,

    // This resource instance is related to a specific actor.  This should be Relationship status, debt/credit, or anything else related to a specific actor
    relation_to_actor_index: i32 = -1, //TODO: Implement
};

// ResourceLabel — Conditional label assignment through resource evaluation.
//
// Evaluates a ResourceConversionSet's requirements against an entity.  If all requirements pass, writes the label i32 to the target resource.
//
// Multiple ResourceLabels sharing the same target form a switch:
// evaluated in id order, first match wins.
//
// Example — health condition:
//   id=0, name="Near-Death",  label=0, target=stats.HealthCondition, cs=50 (Health 0-10)
//   id=1, name="Crippled",    label=1, target=stats.HealthCondition, cs=51 (Health 11-25)
//   id=2, name="Injured",     label=2, target=stats.HealthCondition, cs=52 (Health 26-60)
//   id=3, name="Healthy",     label=3, target=stats.HealthCondition, cs=53 (Health 61-100)
//
// Example — complex multi-resource condition:
//   id=0, name="Special",     label=99, target=stats.Title, cs=54 (cs 54 requirements: Money >= 100, Chicken >= 1, Duck_On_Fire >= 1)
//
// The label i32 is itself a resource value — queryable by Prolog, usable in conversion set requirements, gatable by StoreFronts.  "This quest requires Crippled" is just a requirement: HealthCondition == 1.
// No match writes -1 to target.
//NOTE: ResourceLabel is also the Status, we dont need ResourceStatus, because that is what Label provides, and it can be used just like that.  Dead?  Healthy?  Crippled?  Its a state, tracked here.  A sensor
pub const ResourceLabel = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    label: i32 = -1,
    image_id: i32 = -1, // game.ui_image.{}, can swap the image with the Label //TODO:REMOVE, ContentIcon is better

    // Visual Representation.  This can be used on ContentItem tileset flatten from a Resource Group tile layer which we attach this Label to, and now we are using this frame on the compressed tile map visually
    //  Ex: Grass has values: Tiny=<2, Short=<4, Medium=<8, Long=<10 and we show different grass heigthts visually.  ContentIcon can be a single frame or animation, including an auto-tile system
    icon: ContentIcon = .{},

    sound_event_id: i32 = -1, // If != -1, play this sound event when this label activates

    target: ResourceLink = .{},
    conversion_set_id: i32 = -1,
    resource_group_id: i32 = -1, // This can represent a Resource
};

pub const ResourceGoalLevelLayerItem = struct {
    // The resource group that identifies the LevelTileLayer to read, matched against render_resource_group_id or data_resource_group_id
    resource_group_id: i32 = -1,

    // If true, this is per Player (layer.owned_by_player_id must match), if false, this is a shared layer
    is_per_player: bool = true,

    // Calculation
    is_fitness_highest: bool = true, // Highest non-unset value
    is_fitness_lowest: bool = false, // Lowest non-unset value

    // Take the value and scale it.  We add all the ResourceGoalLevelLayerItem.  Can use to attract/repel with 1/-1 scales
    value_scale: Fixed = fixed.FIXED_ONE,

    // If true, use the lowest values, not the highest of the level layer as our tile selection
    target_inverse: bool = false,

    // Tile distance between valid nodes, so we dont group them together, otherwise the spatial will all group in one place instead of being tactically useful and distributed across different tiles and map areas
    tile_distance_between_pos_candidate: i32 = 3,
};

// Where do we go with this Goal?
pub const ResourceGoalTarget = struct {
    // If true, we process the matrix of options.  If false, there is to target, so skip processing
    has_target: bool = false,

    // There are only 2 target types: Actor and Tile.  We are either seeking an Actor, or a Tile
    is_target_actor: bool = true,

    // If != -1, we will use the level layer item to select where to move to a tile
    use_level_layer_index: i32 = -1,

    // Actor has this Resource Group.  We will search for the closest to the searching actor
    has_resource_group_id: i32 = -1,

    // Tile has this Resource Conversion Set.  We will search for the closest to the searching actor
    has_resource_conversion_set_id: i32 = -1,

    // If != -1, only seeking for this specific player
    player_index_by_resource_group_id: i32 = -1, //TODO: From resource_group var

    // If true, any player is used
    is_any_player: bool = false,

    // If true, must be from the same player.  If false, this is only different Player.  The "any" case is `is_any_player`
    is_same_player: bool = false,

    // If true, must be in the `Player.enemies` list
    is_enemy_player: bool = false, //TODO: Not wired up yet

    // If true, must be in the `Player.allies` list
    is_ally_player: bool = false, //TODO: Not wired up yet

    // If true, must NOT be in the `Player.allies` or `Player.enemies` list
    is_neutral_player: bool = false, //TODO: Not wired up yet

    // Is a specific Entity
    is_entity_id: i32 = -1,
};

// What do we do with this goal?  We run a conversion set,
pub const AnimationEventResponse = struct {
    // The event to respond to (ex. .EndAnim, .Strike, .Die, .Death, .Hit, .Touch, .Shoot, .Bump)
    event: content_item.ContentEventType = .EndAnim, // .EndAnim is the catch-all, even though .Strike may be the most common

    // The animation to match (resource_group_id, e.g. 200=Idle, 201=Walk, 204=StrikeRight)
    animation_resource_group_id: i32 = -1,

    // The conversion set to run
    resource_conversion_set_id: i32 = -1,

    // Ex: The strike event would explicitly select “Impact” vs “Scrape” vs “Destruction” interaction type on the MaterialSoundMap, and the material at the target tile would select the pool. The chain: goal outcome → animation response → interaction type → material at tile → sound pool → sound file
    interaction_resource_group_id: i32 = -1,

    // If true, the the Resource Target is given the `From` field position, and self is given `To` field.  If false, the reverse, Target is `To` and self is `From` in the Conversion Set
    is_from_target: bool = true,
};

pub const ResourceGoalOutcome = struct {
    // The Actor performing the goal plays this animation.  The events on the animation can be handled by animation_responses, or the force vars, and we could also force and not have an anim.  All possible
    //  (ex: 200=Idle, 201=Walk, 207=Jump, 211=Death, 212=Dead, 204=StrikeRight, 213=Interact)
    actor_animation_resource_group_id: i32 = -1,

    // If `actor_animation!=.None`, and that animation has an event, like .StrikeRight or .EndAnim (all have .EndAnim), then these can respond to that animation by running a conversion set
    actor_animation_responses: []AnimationEventResponse = &.{},

    // Always run on outcome frame, regardless of animation: The conversion set to run
    always_run_resource_conversion_set_id: i32 = -1,

    // Always run on outcome frame, regardless of animation:: If true, the the Resource Target is given the `From` field position, and self is given `To` field.  If false, the reverse, Target is `To` and self is `From` in the Conversion Set
    always_run_is_from_target: bool = true,
};

pub const ResourceConsideration = struct {
    // This calculation is our consideration source, which we put through the range, weight, curve, etc
    score_resource_calculation_id: i32 = -1,

    range: Fixed2 = Fixed2{ .x = 0, .y = fixed.FIXED_ONE },
    score_weight: Fixed = fixed.FIXED_ONE,

    curve: Curve = .Linear,
    score_inverted: bool = false,

    force_min_value: Fixed = ResourceUnset,
    fixed_score: Fixed = ResourceUnset,

    zero_ranges: []Fixed2 = &[_]Fixed2{},
};

// Players have goals, and we can determine what their goals should be now based on
pub const ResourceGoal = struct {
    // game.resource_goal.{id}
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // If != -1, this points to the game.resource_group.{id} which is the label for this reason, and can be used in calculations and conversion sets, and instances of resource sets
    reason_resource_group_id: i32 = -1,

    // If == -1, always active.  If >=0 this goes to game.resource_calculation to determine if the rule is active.  If the result is >=0, the rule is active and the value is the score, which we use in Utility AI
    is_active_resource_calculation_id: i32 = -1,

    // What should they build, if anything?
    //TODO: Now that ResourceConversionSet has `resource_goal_id` to set up the 1:N (Goal:Sets) we can use the Goal as our UAI point to get our Conversion Set considerations as actions for the Goal
    //      That means we can remove these fields later once this is implemented, because Goal is not tied to 1 Conversion Set
    build_resource_set_id: i32 = -1, //TODO: Do we remove this too? or does it stay using the CSets as UAI Behaviors?  Head maps definitely stay, and reason_resource_group_id is concept.  Is this needed?
    build_conversion_set_id: i32 = -1,

    // Per Player, which level layer do we use for this goal?
    level_layer_items: []ResourceGoalLevelLayerItem = &.{},

    // How to target an Actor or Tile for this goal
    target: ResourceGoalTarget = .{},

    // Outcome
    outcome: ResourceGoalOutcome = .{},

    // Utility AI Considations, for treating a Conversion Set as an action (Behavior), so we can put them all together and test it
    considerations: []ResourceConsideration = &.{},

    force_min_value: Fixed = 0, // This is the minimum value this item can be, allowing it to be a default.  Even if it's considerations are 0, it will be this value, as the minimum
};

pub const ResourceGroupLanguage = struct {
    language_id: i32 = -1,
    display: Text = Text.initEmpty(),
    short: Text = Text.initEmpty(),
};

pub const ResourceGroup = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),
    short_name: Text = Text.initEmpty(),

    // game.content_item.{id} is inside, with Animation and Direction, you can do a lot.  Directional icons: ex: Stocks are Going Up/Down with different arrows, Left/Right could be events that flash/bounce
    icon: ContentIcon = .{},

    // UI Theme Panel: game.ui_theme.{game_ui_theme_id}.data_ui_theme.panels{id}
    theme_panel_id: i32 = -1,

    display_type: i32 = -1, // Could have N display types in any given situation
    sort_order: i32 = -1, // How high is this group sorted currently?

    // Language Translation
    languages: []ResourceGroupLanguage = &[_]ResourceGroupLanguage{},
};

// A Standing Order is a surplus target the colony maintains: (per_actor_value * population) + surplus_value.
//  The colony works the conversion set until the counted resource group meets the computed target, then stops.  Population changes move the target automatically, so the player never re-does the math
pub const ResourceStandingOrder = struct {
    // Clones game.resource_standing_order.{id}.id, for DB record reference
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // Is this order currently being worked?  Player can pause without deleting.  Position in the parent list is the priority, there is no priority number
    is_active: bool = true,

    // The production recipe.  Costs are the ingredients consumed, requirements gate whether work can happen at all (power, skill, materials in range)
    conversion_set_id: i32 = -1,

    // What we count toward the target.  The target is met when the Player's total of this group >= computed target value
    target_resource_group_id: i32 = -1,

    // Target rule: (per_actor_value * population) + surplus_value.  Set per_actor_value=0 and surplus_value=50 for a pure flat target
    per_actor_value: Fixed = 0,
    surplus_value: Fixed = 0,

    // Population scope for per_actor_value.  If -1, All Colonists.  Otherwise only actors assigned to this Job are counted
    //  Authored default comes from the owner Entity (Weapons Rack defaults to Warriors), player can change it on this instance
    population_job_resource_group_id: i32 = -1,

    // Hysteresis so production doesn't flicker at the boundary.  Work resumes when the counted total drops below (target * resume_below_percent).  1.0 = resume immediately on any deficit
    resume_below_percent: Fixed = fixed.FIXED_ONE,

    // If !=-1, then this order is only enabled if the Player's resources are valid against this conversion set
    enable_resource_conversion_set_id: i32 = -1,

    // If !=-1 and valid, then if this is shown (enabled), then it is shown but disabled
    disable_resource_conversion_set_id: i32 = -1,

    // If !=-1, this will trigger an Event when the target is first met, so the player sees the order complete without watching it
    trigger_resource_event_id: i32 = -1,

    // We dont remove these, we just mark them deleted so they can be repopulated in our list later
    is_deleted: bool = false,
};

// -- Editor --

// What are we editing?  Must always be something, never None
pub const ResourceEditorType = enum(i32) {
    ResourceGroup,
    ResourceSet,
    ResourceGoal,
    ResourceConversionSet,
    ResourceCalculation,
    ResourceStoreFront,
    ResourceSequence,
    ResourceEvent,
    ResourceTrigger,
};

pub const ResourceEditor = struct {
    editor_type: ResourceEditorType = .ResourceGroup,

    filter_record: Text = Text.initEmpty(),

    // If true, we use the From/To Resource group, if False we ignore it and only filter on the From resource group
    use_from_resource_group: bool = false,
    use_to_resource_group: bool = false,

    // 2 Levels of Resource Groups: Category (Parents), and Groups
    from_category_resource_group_id: i32 = -1, // From Category
    from_resource_group_id: i32 = -1, // From Group

    to_category_resource_group_id: i32 = -1, // To Category
    to_resource_group_id: i32 = -1, // To Group
};

pub fn isUnset(value: Fixed) bool {
    // If equal, true
    if (value == ResourceUnset) return true;

    return false;
}
