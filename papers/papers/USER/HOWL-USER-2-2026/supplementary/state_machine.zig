const std = @import("std");

const prolog = @import("prolog.zig");
const entity = @import("entity.zig");
const content_item = @import("content_item.zig");
const skill_set_lib = @import("skill_set.zig");

// Types
const Text = @import("text.zig").Text;

pub const StateMachineTransition = struct {
    // Transition to this State.name
    to: Text = Text.initEmpty(),

    // If true, we exit when we see this event
    exit_on_event: content_item.ContentEventType = .None,

    // All elements of the Rule must pass for this Transition to occur.  If the rules passes, this transition will occur.  Uses Rule by name
    exit_condition_rule_name: Text = Text.initEmpty(),

    // Shortest time allowed in this state before transition.  Normally 0, but we may want to insert a delay here
    duration_min: f32 = 0,

    // Delete Entity with this transition
    delete_entity: bool = false,
};

pub const StateMachineState = struct {
    name: Text = Text.initEmpty(),

    // If True, this is the entry state from ".", dont bother creating transitions for it, just enter the first state we find marked as Entry state, or make a "." state, either way
    is_entry_state: bool = false,

    // Behavior Set to score through UAI, and then execute the top choice.  The State directly controls execution possibility, and by nesting, make it scalable.  Clone or create new, all things can scale
    behavior_set_id: i32 = -1,

    // Transitions to other
    transitions: []StateMachineTransition = &[_]StateMachineTransition{},

    // If not .None, when an Entity has an Event, it will change to this state immediately
    force_transition_to_on_event: content_item.ContentEventType = .None,

    // If not .None, then this State will force this skill, and will not peform Behavior Set checks.  Skips Behavior Sets and Logic Blocks, and just runs this skill to keep it simple and skill-envl.-stat-based
    //NOTE: Action -> EquipmentSlot -> WorldItem -> CombatSkill -> SkillItem -> SkillLevel -> Data:Animation/Speed/etc
    force_action: skill_set_lib.ActionType = .None,

    // If not empty, this is a Data State Machine (ex: Skill Tree), and we have can visualize it
    data_path: Text = Text.initEmpty(),

    // //TODO:MUSIC: Make the music and atmoshperic and environment and crowd effects (tavert, crickets, goblin camp)
    // music_track
    // atmopshere_track
    // environment_track
    // crowd_track
};

pub const StateMachine = struct {
    id: i32 = -1, // game.state_machine.id, in the struct so we never lose it
    name: Text = Text.initEmpty(), // game.state_machine.name, we keep this updated automatically like `id`

    //TODO: Converting from TextArray to a custom list, it's too hard to deal with TextArray now, fix it up later when I can spend time on it.
    states: []StateMachineState = &[_]StateMachineState{},

    can_stop: bool = false, // Convention is "." in AnyEntry and "!" is stop.  Most SMs cant stop, this is just to codify the difference

    // Rule Set to reference for `Transition.exit_condition_rule_name`
    prolog_rule_set_a_id: i32 = -1,
    prolog_rule_set_b_id: i32 = -1, // Optional, for testing alternative Rule Sets
};
