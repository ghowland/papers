const std = @import("std");
const rl = @import("raylib");
const clay = @import("zclay");

const frame_memory = @import("../../frame_memory.zig");

const entity_lib = @import("entity.zig");
const prolog = @import("prolog.zig");
const scene_lib = @import("scene.zig");
const level_data_lib = @import("level_data.zig");

// My Types
const Color = @import("color.zig").Color;
const Vector2 = @import("vector2.zig").Vector2;
const Rect = @import("rect.zig").Rect;
const Number = @import("number.zig").Number;
const Text = @import("text.zig").Text;

const Entity = entity_lib.Entity;
const EntityTransform = entity_lib.EntityTransform;
const TrackEntity = entity_lib.TrackEntity;
const LevelData = level_data_lib.LevelData;

// Term types in prolog expressions
pub const TermType = enum(i32) {
    atom, // Literal value: "entity_5", "combat"
    variable, // Variable to bind: "X", "Target"
    number, // Numeric value: 25.0, 100
    list, // List of terms: [?X, ?Y, ?Z]
    vector2, // Point spatial tests
    rectangle, // Box spatial tests
    circle, // Radial spatial tests.  Uses vec2 as center and number as radius
    level_data,
    entity,
    transform,
};

// A single term in a fact, rule, or query
pub const Term = struct {
    type: TermType = .atom,

    // Value storage (one active based on type)
    atom: Text = Text.initEmpty(),
    variable: Text = Text.initEmpty(),
    number: f32 = 0.0,
    // Index for level_data/actor/ui/fx
    index: i32 = -1,
    // Spatial
    rect: rl.Rectangle = .{},
    vec2: rl.Vector2 = .{}, // Vector2 point, and Circle center
    transform: EntityTransform = .{},
    // List
    list: []Term = &[_]Term{},
    list_is_frame: bool = false,

    pub fn initAtom(value: Text) Term {
        return Term{
            .type = .atom,
            .atom = value,
        };
    }

    pub fn initAtomRaw(value: []const u8) Term {
        return Term{
            .type = .atom,
            .atom = Text.init(value),
        };
    }

    pub fn initVariable(name: Text) Term {
        return Term{
            .type = .variable,
            .variable = name,
        };
    }

    pub fn initVariableRaw(name: []const u8) Term {
        return Term{
            .type = .variable,
            .variable = Text.init(name),
        };
    }

    pub fn initNumber(value: f32) Term {
        return Term{
            .type = .number,
            .number = value,
        };
    }

    pub fn initVec2(value: rl.Vector2) Term {
        return Term{
            .type = .vector2,
            .vec2 = value,
        };
    }

    pub fn initRect(value: rl.Rectangle) Term {
        return Term{
            .type = .rectangle,
            .rect = value,
        };
    }

    pub fn initTransform(value: rl.Rectangle) Term {
        return Term{
            .type = .transform,
            .transform = value,
        };
    }

    pub fn initList(list: []Term, is_frame: bool) Term {
        return Term{
            .type = .list,
            .list = list,
            .list_is_frame = is_frame,
        };
    }

    pub fn equals(self: *const Term, other: *const Term) bool {
        if (self.type != other.type) return false;

        return switch (self.type) {
            .atom => self.atom.equals(other.atom),
            .variable => self.variable.equals(other.variable),
            .number => self.number == other.number,
            .list => false, // Lists not compared for now
            .vector2 => Vector2.fromRaylib(self.vec2).equalsFloat(Vector2.fromRaylib(other.vec2)),
            .rectangle => Rect.fromRaylib(self.rect).equals(Rect.fromRaylib(other.rect)),
            .circle => Vector2.fromRaylib(self.vec2).equalsFloat(Vector2.fromRaylib(other.vec2)) and self.number == other.number,
            .level_data => self.index == other.index and self.index != -1,
            .entity => self.index == other.index and self.index != -1,
            .transform => self.transform.pos.equals(other.transform.pos) == 0, //TODO: Simplified
        };
    }

    pub fn toText(self: *const Term) ![]const u8 {
        const text = switch (self.type) {
            .atom => try Text.formatFrame("Atom: {s}", .{self.atom.toText()}), // Literal value: "entity_5", "combat"
            .variable => try Text.formatFrame("Var: {s}", .{self.variable.toText()}), // Variable to bind: "X", "Target"
            .number => try Text.formatFrame("Num: {}", .{self.number}), // Numeric value: 25.0, 100
            .vector2 => try Text.formatFrame("Vec2: {},{}", .{ self.vec2.x, self.vec2.y }), // Point spatial tests
            .rectangle => try Text.formatFrame("Rect: {},{} {},{}", .{ self.rect.x, self.rect.y, self.rect.width, self.rect.height }), // Box spatial tests
            .circle => try Text.formatFrame("Circle: {},{}  R: {}", .{ self.vec2.x, self.vec2.y, self.number }), // Radial spatial tests.  Uses vec2 as center and number as radius
            .level_data => try Text.formatFrame("Level: {}", .{self.index}),
            .entity => try Text.formatFrame("Entity: {}", .{self.index}),
            .list => try Text.formatFrame("List: TBD...", .{}), // List of terms: [?X, ?Y, ?Z]
            .transform => try Text.formatFrame("Transform2: {}: {}:  Pos: {}, {}", .{
                self.transform.id,
                self.transform.follower_index,
                self.transform.pos.x,
                self.transform.pos.y,
            }),
        };

        return text.toText();
    }
};

// A fact: predicate with arguments
pub const Fact = struct {
    predicate: Text = Text.initEmpty(),
    args: []Term = &[_]Term{},

    pub fn init(predicate: Text, args: []Term) Fact {
        return Fact{
            .predicate = predicate,
            .args = args,
        };
    }

    pub fn initEmpty(predicate: Text) Fact {
        return Fact{
            .predicate = predicate,
            .args = &[_]Term{},
        };
    }

    pub fn toText(self: Fact) ![]const u8 {
        var output = try Text.formatFrame("Fact: {s}  Args: ", .{self.predicate.toText()});
        for (self.args) |arg| {
            output.appendRaw(try arg.toText());
            output.appendRaw(", ");
        }
        return output.toText();
    }
};

// A rule: head :- body1, body2, body3
pub const Rule = struct {
    head: Text = Text.initEmpty(),
    body: []Fact = &[_]Fact{},

    pub fn init(head: Text, body: []Fact) Rule {
        return Rule{
            .head = head,
            .body = body,
        };
    }

    pub fn initSimple(head: Text) Rule {
        return Rule{
            .head = head,
            .body = &[_]Fact{},
        };
    }
};

// For Entities, we can keep this as a custom Record per entity, and save and change it separately
pub const FactSet = struct {
    name: Text = Text.initEmpty(),
    facts: []Fact = &[_]Fact{},

    pub fn init(facts: []Fact) FactSet {
        return FactSet{
            .facts = facts,
        };
    }
};

// For creating rules, we use this, and then we combine this and FactSet.facts to make the KnowledgeBase.facts/rules
pub const RuleSet = struct {
    name: Text = Text.initEmpty(),
    rules: []Rule = &[_]Rule{},

    pub fn init(rules: []Rule) RuleSet {
        return RuleSet{
            .rules = rules,
        };
    }
};

pub const KnowledgeBase = struct {
    name: Text = Text.initEmpty(),
    fact_set: FactSet = .{},
    rule_set: RuleSet = .{},

    // Entity and Scene info, so we can pass a KB and always reference anything inside it
    scene_id: i32 = -1,
    entity_prolog_term_type: prolog.TermType = .entity,
    entity_index: i32 = -1,

    pub fn init(fact_set: FactSet, rule_set: RuleSet) KnowledgeBase {
        return KnowledgeBase{
            .fact_set = fact_set,
            .rule_set = rule_set,
        };
    }

    pub fn initFull(fact_set: FactSet, rule_set: RuleSet, name: Text) KnowledgeBase {
        return KnowledgeBase{
            .name = name,
            .fact_set = fact_set,
            .rule_set = rule_set,
        };
    }

    pub fn getEntity(self: *KnowledgeBase, scene: *scene_lib.Scene, entityTermType: prolog.TermType, entityIndex: i32) ?Entity {
        _ = self;

        switch (entityTermType) {
            .level_data => {
                if (entityIndex >= scene.fact_set_levels.len) return null;

                return scene.levels[entityIndex];
            },
            .entity => {
                if (entityIndex >= scene.fact_set_actors.len) return null;

                return scene.actors[entityIndex];
            },
            else => {},
        }

        return null;
    }
};
