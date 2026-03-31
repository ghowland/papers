const std = @import("std");
const rl = @import("raylib");

const entity_lib = @import("entity.zig");
const skill_set_lib = @import("skill_set.zig");

// My Types
const Text = @import("text.zig").Text;
const Curve = entity_lib.Curve;
const Skill = skill_set_lib.Skill;
const SkillSet = skill_set_lib.SkillSet;
const SkillType = skill_set_lib.SkillType;
const ActionType = skill_set_lib.ActionType;

pub const SelectionMethod = enum(i32) {
    top,
    weighted_random_top3,
    random_reasonable,
};

pub const Consideration = struct {
    // Rule Set to execute.  All rules must pass for the Consideration to be non-0.  If all pass and `score_logic_block_name` is not empty, will run that LB for the score float
    prolog_rule_set_a_id: i32 = -1,
    input_source_name: Text = Text.initEmpty(), //TODO:REMOVE: Switch to rule_set_a_id

    // If not empty, this will be used to execute a Logic Block Stack from game.logic_block.id that return a float for the name
    execute_logic_block_id: i32 = -1,

    // Config
    range: rl.Vector2 = rl.Vector2{ .x = 0, .y = 1 },
    score_weight: f32 = 1,
    curve: Curve = .Linear,
    curve_id: i32 = -1, // game.curve table, if it's a custom Curve
    curve_label: Text = Text.initEmpty(), //TODO: Decom this in favor of curve label?  We should have a custom too...
    score_inverted: bool = false,
    force_min_value: f32 = 0,
    fixed_score: f32 = 0,
    zero_ranges: []rl.Vector2 = &[_]rl.Vector2{},

    // Temp
    temp_score: f32 = 0,

    pub fn init() Consideration {
        return Consideration{
            // .name = name,
            .input_source_name = Text.initEmpty(),
            .force_min_value = 0.0,
            .range = rl.Vector2.init(0.0, 1.0),
            .fixed_score = 0.0,
            .zero_ranges = &[_]rl.Vector2{},
            .curve_label = Text.init("linear"),
            .score_weight = 1.0,
            .score_inverted = false,
            .temp_score = 0.0,
        };
    }

    pub fn calculate(self: *Consideration, input_value: f32) f32 {
        // Check zero ranges
        for (self.zero_ranges) |zero_range| {
            if (input_value >= zero_range.x and input_value <= zero_range.y) {
                self.temp_score = 0.0;
                return 0.0;
            }
        }

        // Normalize to 0-1 based on range
        var normalized = (input_value - self.range.x) / (self.range.y - self.range.x);
        normalized = @max(0.0, @min(1.0, normalized));

        // Apply curve
        const curved = applyCurve(normalized, self.curve_label);

        // Apply weight
        var score = curved * self.score_weight;
        score = @max(0.0, @min(1.0, score));

        // Invert if needed
        if (self.score_inverted) {
            score = 1.0 - score;
        }

        // Apply force minimum
        if (score < self.force_min_value) {
            score = self.force_min_value;
        }

        self.temp_score = score;
        return score;
    }
};

pub const Behavior = struct {
    name: Text = Text.initEmpty(),
    considerations: []Consideration = &[_]Consideration{},
    // If above 0, this is the minimum value for this item, so we have a floor, such as "Idle" or "Default"
    force_min_value: f32 = 0,

    // If selected, we execute this game.logic_block.id.  Logic Block executes before the skill activates
    execute_logic_block_id: i32 = -1,

    // If not None, this Action activate (maps to skill).  If != .None, the requirements must be met, or this skill will always be final_score=0 due to not making activation requirements.  Addititve with logic_block_id
    execute_action: ActionType = .None,

    // Scoring
    temp_score: f32 = 0,
    final_score: f32 = 0,

    pub fn init(name: Text) Behavior {
        return Behavior{
            .name = name,
            .info = Text.initEmpty(),
            .considerations = &[_]Consideration{},
            .temp_score = 0.0,
            .force_min_value = 0.0,
        };
    }

    pub fn calculate(self: *Behavior, input_values: []f32) void {
        var running_score: f32 = 1.0;

        for (self.considerations, 0..) |*consideration, i| {
            const score = consideration.calculate(input_values[i]);

            // If any consideration scores 0, entire behavior scores 0
            if (score == 0.0) {
                self.temp_score = 0.0;
                return;
            }

            running_score *= score;
        }

        // Apply average and fixup formula
        if (self.considerations.len > 0) {
            self.temp_score = averageAndFixup(running_score, self.considerations.len);

            // Apply force minimum
            if (self.temp_score < self.force_min_value) {
                self.temp_score = self.force_min_value;
            }
        } else {
            self.temp_score = 0.0;
        }
    }
};

pub const BehaviorSet = struct {
    name: Text = Text.initEmpty(),
    behaviors: []Behavior = &[_]Behavior{},
    selection_method: SelectionMethod = .top,

    pub fn init(name: Text, behaviors: []Behavior, selection_method: SelectionMethod) BehaviorSet {
        return BehaviorSet{
            .name = name,
            .behaviors = behaviors,
            .selection_method = selection_method,
        };
    }

    pub fn determineBehavior(self: *BehaviorSet, input_values: [][]f32) usize {
        // Calculate all behaviors
        for (self.behaviors, 0..) |*behavior, i| {
            behavior.calculate(input_values[i]);
        }

        // Find top 3 scores
        var top_indices = [3]usize{ 0, 0, 0 };
        var top_scores = [3]f32{ -1.0, -1.0, -1.0 };

        for (self.behaviors, 0..) |behavior, i| {
            if (behavior.temp_score > top_scores[0]) {
                top_scores[2] = top_scores[1];
                top_indices[2] = top_indices[1];
                top_scores[1] = top_scores[0];
                top_indices[1] = top_indices[0];
                top_scores[0] = behavior.temp_score;
                top_indices[0] = i;
            } else if (behavior.temp_score > top_scores[1]) {
                top_scores[2] = top_scores[1];
                top_indices[2] = top_indices[1];
                top_scores[1] = behavior.temp_score;
                top_indices[1] = i;
            } else if (behavior.temp_score > top_scores[2]) {
                top_scores[2] = behavior.temp_score;
                top_indices[2] = i;
            }
        }

        // Select based on method
        return switch (self.selection_method) {
            .top => top_indices[0],
            .weighted_random_top3 => blk: {
                if (self.behaviors.len < 3) {
                    break :blk top_indices[0];
                }
                const rand_val = std.crypto.random.float(f32);
                if (rand_val < 0.70) {
                    break :blk top_indices[0];
                } else if (rand_val < 0.95) {
                    break :blk top_indices[1];
                } else {
                    break :blk top_indices[2];
                }
            },
            .random_reasonable => top_indices[0],
        };
    }
};

// Utility functions

pub fn averageAndFixup(running_score: f32, consideration_count: usize) f32 {
    if (consideration_count == 0) return 0.0;

    const count_f: f32 = @floatFromInt(consideration_count);
    const mod_factor = 1.0 - (1.0 / count_f);
    const makeup_value = (1.0 - running_score) * mod_factor;
    const final_score = running_score + (makeup_value * running_score);

    return final_score;
}

pub fn applyCurve(t: f32, curve_label: Text) f32 {
    if (curve_label.equalsRaw("linear")) {
        return t;
    } else if (curve_label.equalsRaw("quadratic")) {
        return t * t;
    } else if (curve_label.equalsRaw("exponential")) {
        return (std.math.exp(t) - 1.0) / (std.math.e - 1.0);
    } else if (curve_label.equalsRaw("sigmoid")) {
        return 1.0 / (1.0 + std.math.exp(-10.0 * (t - 0.5)));
    } else if (curve_label.equalsRaw("bell")) {
        const x = (t - 0.5) * 4.0;
        return std.math.exp(-x * x);
    }

    return t; // Default linear
}

// Example usage
pub fn example() BehaviorSet {
    // Create a consideration for health
    var health_consideration = Consideration.init(Text.init("health_check"));
    health_consideration.input_source_name = Text.init("health");
    health_consideration.range = rl.Vector2.init(0.0, 100.0);
    health_consideration.curve_label = Text.init("linear");
    health_consideration.score_weight = 1.0;

    // Create a consideration for distance to enemy
    var distance_consideration = Consideration.init(Text.init("distance_check"));
    distance_consideration.input_source_name = Text.init("distance");
    distance_consideration.range = rl.Vector2.init(0.0, 50.0);
    distance_consideration.curve_label = Text.init("exponential");
    distance_consideration.score_weight = 1.5;

    // Create considerations array
    var considerations = [_]Consideration{ health_consideration, distance_consideration };

    // Create a behavior
    var attack_behavior = Behavior.init(Text.init("attack"));
    attack_behavior.considerations = &considerations;
    attack_behavior.force_min_value = 0.1;

    // Create a flee behavior
    var flee_consideration = Consideration.init(Text.init("health_low"));
    flee_consideration.input_source_name = Text.init("health");
    flee_consideration.range = rl.Vector2.init(0.0, 100.0);
    flee_consideration.curve_label = Text.init("linear");
    flee_consideration.score_inverted = true; // Low health = high score

    var flee_considerations = [_]Consideration{flee_consideration};

    var flee_behavior = Behavior.init(Text.init("flee"));
    flee_behavior.considerations = &flee_considerations;

    // Create behavior set
    var behaviors = [_]Behavior{ attack_behavior, flee_behavior };

    var behavior_set = BehaviorSet.init(Text.init("combat_ai"), &behaviors, .weighted_random_top3);

    // Simulate input values
    var attack_inputs = [_]f32{ 80.0, 10.0 }; // health=80, distance=10
    var flee_inputs = [_]f32{20.0}; // health=20

    var all_inputs = [_][]f32{ &attack_inputs, &flee_inputs };

    // Determine best behavior
    const chosen_index = behavior_set.determineBehavior(&all_inputs);
    const chosen_behavior = behavior_set.behaviors[chosen_index];

    std.debug.print("Chosen behavior: {s} with score: {d:.3}\n", .{ chosen_behavior.name.toText(), chosen_behavior.temp_score });

    // Print all scores
    std.debug.print("\nAll behavior scores:\n", .{});
    for (behavior_set.behaviors) |behavior| {
        std.debug.print("  {s}: {d:.3}\n", .{ behavior.name.toText(), behavior.temp_score });
    }

    return behavior_set;
}
