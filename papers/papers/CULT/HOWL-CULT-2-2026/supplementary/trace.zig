const std = @import("std");
const Text = @import("text.zig").Text;
const TextArray = @import("text_array.zig").TextArray;
const Vector2 = @import("vector2.zig").Vector2;
const logic_block = @import("logic_block.zig");
const utility_ai = @import("utility_ai.zig");
const state_machine = @import("state_machine.zig");
const prolog = @import("prolog.zig");
const entity_lib = @import("entity.zig");

pub const TraceType = enum(i32) {
    none = 0,

    STATE_MACHINE = 1000,
    state,
    state_transition,
    state_transition_rule,

    UTILITY_AI = 2000,
    behavior_set,
    behavior_score,
    behavior_selection,
    consideration,
    consideration_rule,

    LOGIC_BLOCK = 3000,
    block_stack,
    block_stack_result,
    block_condition, // If/Else path desicisions
    block_rule,
    block_execute_command,
    block_execute_function,
    block_execute_block,
    block_loop_start, // Index count for each loop.  Can open and close the loop as needed

    FUNCTIONS = 5000,
    set_dr, // Show path where change was made, we can link to see the new values, dont need to show old, but if I want to do that keep Blue/Green facts, and I can always see the Before facts
    set_entity_fact, // Change a current Blue/Green fact in the non-derived data
};

// pub const PrologRuleEvaluationResult = struct {
//     success: bool = false,
//     message: Text = Text.initEmpty(),
// };

// pub const PrologRuleEvaluation = struct {
//     rule_name: Text = Text.initEmpty(),
//     match_percent: f32 = 0, // 4/5 terms match = 0.80.  1.0 is required for acceptance, but 0.8 tell us its "close", which is useful for rule tuning
//     term_match_results: []PrologRuleEvaluationResult = &[_]PrologRuleEvaluationResult{}, // Results match to Term indexes, dont need to store Terms
// };

// pub const TrackStateTransition = struct {
//     to_state: Text = Text.initEmpty(),
//     can_transition: bool = false,

//     rules: prolog.RuleSet = .{},
//     rules_b: prolog.RuleSet = .{},
// };

// pub const TraceState = struct {
//     state: Text = Text.initEmpty(),
//     start_time: f32 = 0,
//     start_frame: i32 = 0,

//     transitions: []state_machine.StateMachineTransition = &[_]state_machine.StateMachineTransition{},
// };

// pub const TraceBlockContext = struct {
//     entity_id: i32 = -1,
//     frame: u32 = 0,
//     delta_time: f32 = 0,

//     // Navigation
//     current_row_index: i32 = 0,
//     skip_to_row_index: i32 = -1,
//     error_message: Text = Text.init(""),
// };

// pub const TraceBlock = struct {
//     // Row identity
//     logic_block_id: i32 = -1,
//     block_row_id: i32 = -1,
//     block_row_type: logic_block.BlockType = .Log,
//     row_index: usize = 0,
//     indent_level: usize = 0,

//     // Stack reference
//     stack_id: i32 = -1,
//     stack_name: Text = Text.initEmpty(),

//     // Timing
//     time_start: f32 = 0,
//     time_end: f32 = 0,

//     // Input resolution
//     inputs: []logic_block.BlockInput = &[_]logic_block.BlockInput{},

//     // Result value (what the row produced)
//     result_value: logic_block.BlockValue = .{},

//     // Variable state (snapshot after execution)
//     variables_after: []logic_block.BlockValue = &[_]logic_block.BlockValue{},

//     // Control flow
//     has_condition_result: bool = false,
//     // For if/while/else_if
//     condition_result: bool = false,

//     // Child row IDs that executed
//     child_rows_executed: []i32 = &[_]i32{},

//     // Execution context at this point
//     context: TraceBlockContext = .{},
// };

pub const TraceEntry = struct {
    type: TraceType = .none,
    time_start: f32 = -1,

    success: bool = false,
    message: Text = .{},
    value: f32 = 0, // 0/1 boolean, and float results

    // // state_machine_instance: state_machine.StateMachineInstance = .{},
    // state: TraceState = .{},
    // considerations: []utility_ai.Consideration = &[_]utility_ai.Consideration{},
    // behaviors: []utility_ai.Behavior = &[_]utility_ai.Behavior{},
    // blocks: []TraceBlock = &[_]TraceBlock{},
};

// 1 Update, stored in data.trace.# (entity_id)
pub const EntityTrace = struct {
    entity_id: i32 = -1, // Index of the Entity in it's slot

    time_start: f32 = -1, // First execution duration uses this, from this to first time_start
    time_end: f32 = -1, // Last execution duration uses this, from previous time_start

    // We use `entity_trace.TraceList_*` which is std.array_list.Managed, and then toOwnedSlice() into this after the update, so this is updated once per update()
    items: []TraceEntry = &[_]TraceEntry{},
};
