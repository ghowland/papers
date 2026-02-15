// Will go into `game.thread` per game, and will track the actual thread usage per game.  Can multithread and track per N games, switch games and the threads can change
//
// Threads can run all the time on data, save state and start again on reload/restart, picking up where they left off, like doing Steam Delpoyments or whatever
//

const std = @import("std");
const rl = @import("raylib");

// My Types
const Text = @import("text.zig").Text;

// ============================================================================
// THREAD SYSTEM - Pure Data Structures
// ============================================================================

pub const WorkloadType = enum(i32) {
    None = -1,

    // Physics transformations
    IntegrateVelocity = 1000, // pos + vel*dt → new_pos
    ApplyForces, // forces → accelerations → velocities
    DetectCollisions, // AABB checks → collision pairs
    ResolveCollisions, // collision pairs → impulses → velocities

    // AI transformations
    UpdateAwareness = 2000, // entity positions → awareness cache
    EvaluateUtilityAI, // awareness + stats → behavior scores
    ExecuteStateMachine, // current state + rules → next state
    RunPrologQuery, // facts + rules → query results
    ExecuteLogicBlocks, // block rows + inputs → outputs

    // Rendering transformations
    BuildSpriteBatch = 3000, // entity pos + sprite → render batch
    SortRenderBatch, // render batch → depth-sorted batch
    UploadToGPU, // sorted batch → GPU buffers

    // Database transformations
    ScanTable = 4000, // table rows → filtered rows
    JoinTables, // table A + table B → joined rows
    ApplyAggregates, // rows → aggregated results

    // HTTP transformations
    ParseRequests = 5000, // raw bytes → parsed requests
    RouteRequests, // requests → handler assignments
    ExecuteHandlers, // requests + handlers → responses
    SerializeResponses, // responses → raw bytes

    // Network transformations
    DecodePackets = 6000, // raw packets → structured data
    EncodePackets, // structured data → raw packets
    UpdateSockets, // socket state → new socket state

    // Generic transformations
    MapTransform = 7000, // input array → output array (1-to-1)
    FilterTransform, // input array → subset (predicate)
    ReduceTransform, // input array → single value (fold)

    // Cymatic
    CalculateCymaticPressure = 8000, // Computes the Laplacian of the field
    UpdateFlowCohesion, // Computes the curl/circulation
    ResolveSubstrate, // Compares pressure vs yield_strength and flips SVDAG bits
};

pub const MemoryDomain = enum(i32) {
    NumaNode0 = 0,
    NumaNode1 = 1,
    NumaNode2 = 2,
    NumaNode3 = 3,
    GPU = 100,
    SharedCPU = 200,
};

pub const DeviceType = enum(i32) {
    CPU = 0,
    GPU = 1,
    DMA = 2, // Direct memory access engine
};

// Work batch - what to process
pub const WorkBatch = struct {
    // Data range to process (entities, rows, packets, etc.)
    data_start_index: i32 = 0,
    data_count: i32 = 0,

    // What transformation to apply
    workload_type: WorkloadType = .None,

    // Input data location (DR path or direct pointer)
    input_data_path: Text = Text.initEmpty(), // e.g. "game.actor.pos"
    input_data_ptr: ?[*]u8 = null, // Direct memory if already located
    input_stride: i32 = 0, // Bytes between elements

    // Output data location
    output_data_path: Text = Text.initEmpty(), // e.g. "game.actor.new_pos"
    output_data_ptr: ?[*]u8 = null,
    output_stride: i32 = 0,

    // Secondary inputs (e.g. forces, rules, awareness data)
    aux_data_path_a: Text = Text.initEmpty(),
    aux_data_ptr_a: ?[*]u8 = null,
    aux_data_path_b: Text = Text.initEmpty(),
    aux_data_ptr_b: ?[*]u8 = null,

    // Processing state
    is_complete: bool = false,
    progress: i32 = 0, // For partial completion tracking
};

// Thread coordination
pub const Thread = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    // Hardware mapping
    device_type: DeviceType = .CPU,
    cpu_core_id: i32 = -1, // Which physical core (0-N)
    gpu_compute_unit_id: i32 = -1, // Which GPU compute unit
    memory_domain: MemoryDomain = .SharedCPU,

    // Work queue for this thread
    work_batches: []WorkBatch = &[_]WorkBatch{},
    current_batch_index: i32 = 0,

    // Performance tracking
    frames_processed: i32 = 0,
    total_elements_processed: i64 = 0,
    total_cycles: i64 = 0,

    // Status
    is_active: bool = true,
    is_waiting: bool = false,
    wait_on_thread_id: i32 = -1, // Blocking on another thread?

    // Memory arena for this thread (pinned to NUMA domain)
    scratch_memory_ptr: ?[*]u8 = null,
    scratch_memory_size: i32 = 0,
    scratch_memory_used: i32 = 0,
};

// Frame coordination - barrier synchronization
pub const FrameCoordinator = struct {
    current_frame: i32 = 0,

    // All threads that must complete before frame advances
    thread_ids: []i32 = &[_]i32{},
    threads_completed: []bool = &[_]bool{},

    // Frame timing
    frame_start_time: f32 = 0,
    frame_budget_ms: f32 = 16.67, // 60 FPS

    // Work distribution strategy
    auto_balance_loads: bool = true,
    prefer_cache_locality: bool = true,
    prefer_numa_locality: bool = true,
};

// Work assignment - how to split work across threads
pub const WorkDistribution = struct {
    name: Text = Text.initEmpty(),

    // What data to process
    data_path: Text = Text.initEmpty(), // e.g. "game.actor"
    data_count: i32 = 0, // Total elements

    // How to split it
    batch_size: i32 = 64, // Elements per batch (cache-line sized)
    thread_count: i32 = 8, // How many threads
    thread_ids: []i32 = &[_]i32{}, // Which threads to use

    // What to do
    workload_type: WorkloadType = .None,

    // Input/output paths
    input_paths: []Text = &[_]Text{},
    output_paths: []Text = &[_]Text{},
    aux_paths: []Text = &[_]Text{},

    // Memory placement hints
    prefer_memory_domain: MemoryDomain = .SharedCPU,
    require_contiguous: bool = true, // Must be cache-friendly
};

// Example instantiation for physics update
pub fn examplePhysicsWorkload() WorkDistribution {
    return WorkDistribution{
        .name = Text.init("physics_update"),
        .data_path = Text.init("game.actor"),
        .data_count = 10000,
        .batch_size = 256, // 256 actors per thread
        .thread_count = 8,
        .thread_ids = &[_]i32{ 0, 1, 2, 3, 4, 5, 6, 7 },
        .workload_type = .IntegrateVelocity,
        .input_paths = &[_]Text{
            Text.init("game.actor.pos"),
            Text.init("game.actor.vel"),
        },
        .output_paths = &[_]Text{
            Text.init("game.actor.new_pos"),
        },
        .prefer_memory_domain = .NumaNode0,
        .require_contiguous = true,
    };
}

// Example instantiation for AI update
pub fn exampleAIWorkload() WorkDistribution {
    return WorkDistribution{
        .name = Text.init("ai_update"),
        .data_path = Text.init("game.actor"),
        .data_count = 1000,
        .batch_size = 125, // 1000 / 8 threads
        .thread_count = 8,
        .thread_ids = &[_]i32{ 0, 1, 2, 3, 4, 5, 6, 7 },
        .workload_type = .EvaluateUtilityAI,
        .input_paths = &[_]Text{
            Text.init("game.actor.awareness"),
            Text.init("game.actor.ai_behavior"),
        },
        .output_paths = &[_]Text{
            Text.init("game.actor.current_behavior_score"),
        },
        .aux_paths = &[_]Text{
            Text.init("game.behavior_set"), // Shared lookup data
        },
        .prefer_memory_domain = .NumaNode0,
        .require_contiguous = true,
    };
}

// Example instantiation for GPU rendering
pub fn exampleGPURenderWorkload() WorkDistribution {
    return WorkDistribution{
        .name = Text.init("gpu_render"),
        .data_path = Text.init("game.actor"),
        .data_count = 100000,
        .batch_size = 100000, // Entire batch to GPU
        .thread_count = 1,
        .thread_ids = &[_]i32{16}, // GPU thread
        .workload_type = .BuildSpriteBatch,
        .input_paths = &[_]Text{
            Text.init("game.actor.pos"),
            Text.init("game.actor.visual_system.content_import_id"),
        },
        .output_paths = &[_]Text{
            Text.init("gpu.sprite_batch"),
        },
        .prefer_memory_domain = .GPU,
        .require_contiguous = true,
    };
}

// Example instantiation for database scan
pub fn exampleDatabaseWorkload() WorkDistribution {
    return WorkDistribution{
        .name = Text.init("db_table_scan"),
        .data_path = Text.init("db.table.users"),
        .data_count = 1000000,
        .batch_size = 125000, // 125k rows per thread
        .thread_count = 8,
        .thread_ids = &[_]i32{ 8, 9, 10, 11, 12, 13, 14, 15 },
        .workload_type = .ScanTable,
        .input_paths = &[_]Text{
            Text.init("db.table.users.row_data"),
        },
        .output_paths = &[_]Text{
            Text.init("db.query_result.filtered_indices"),
        },
        .prefer_memory_domain = .NumaNode1,
        .require_contiguous = true,
    };
}
