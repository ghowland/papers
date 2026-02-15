const std = @import("std");
const rl = @import("raylib");

const entity_lib = @import("entity.zig");
const trace_lib = @import("trace.zig");
const level_data_lib = @import("level_data.zig");
const content_item = @import("content_item.zig");
const prolog = @import("prolog.zig");
const canvas_layout = @import("canvas_layout.zig");
const scene_lib = @import("scene.zig");
const skill_set_lib = @import("skill_set.zig");

// Types
const Vector2 = @import("vector2.zig").Vector2;
const Number = @import("number.zig").Number;
const Text = @import("text.zig").Text;
const TextArray = @import("text_array.zig").TextArray;
const Color = @import("color.zig").Color;

pub const ItemType = enum(i32) {
    None,
    Weapon_Melee,
    Weapon_Ranged,
    Shield,
    Tool,
    Armor,
    Consumable,
    Material,
    Quest,
    Currency,
};

pub const ItemHand = enum(i32) {
    None = -1,
    Left,
    Right,
    Both,
};

pub const WorldItemSkill = struct {
    skill: skill_set_lib.SkillType = .None,
    skill_level: i32 = 0,
    skill_modifier: f32 = 1,
};

//NOTE: Use this by taking all the states of Parent A and B (if exists), to create base_value on manual trigger update
//NOTE: Each implementation (WorldItem, Entity) needs it's own implementation to use "parent" because we use Data Router to map buttons to them by struct name, and the db.table must match
pub const WorldItemScaling = struct {
    // Parent A.  Value = A+B
    parent_a_id: i32 = -1, // First parent entity id (-1 = none)

    scalar_a: f32 = 0, // Multiplied by the curve value
    curve_a: entity_lib.Curve = .Linear,
    curve_a_value: f32 = 1, // 0-1, gets the Curver scalar to multiple scalar_a by parent_id_a's stat base_value

    // Parent B
    parent_b_id: i32 = -1, // Second parent entity id (-1 = none)

    scalar_b: f32 = 0, // Multiplied by the curve value
    curve_b: entity_lib.Curve = .Linear,
    curve_b_value: f32 = 1, // 0-1, gets the Curver scalar to multiple scalar_b by parent_id_b's stat base_value
};

pub const WorldItem = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // Type classification
    item_type: ItemType = .None,
    equipment_slot: entity_lib.EquipmentSlotType = .None, // Where it equips, or .None if not equipment

    // Active Skills.  This is how our Entity's skill is selected
    combat_skill: WorldItemSkill = .{}, // What it does in combat.  When used for Combat
    work_skill: WorldItemSkill = .{}, // What it does for work/utility.  When used for Crafting/Production

    // Passive Skills
    passive_skills: []WorldItemSkill = &[_]WorldItemSkill{},

    // Requirements
    required_skill_level: i32 = 0, // Need skill at this level to use effectively
    two_handed: bool = false,
    force_hand: ItemHand = .None, // ex: Bow forces left hand, same shield, unless content for dual shields, or its attachment, not layer

    // Stacking
    can_stack: bool = false,
    max_stack: i32 = 1,

    // Visual
    sprite_id: i32 = -1,

    // Value in Money stat
    cost: i32 = 0,

    // Our skill base_values with be set by the parent multipliers
    scaling: WorldItemScaling = .{},

    // If false, this is a conceptual item and cant materialize in the game.  It is used as a WorldItemScaling factor
    is_real: bool = true,
};
