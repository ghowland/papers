// device_driver_operator.zig — Generic device driver composition layer.
//
// Every device driver does the same structural work: discover, claim,
// configure, DMA setup, interrupt install, command submit, completion
// process, error handle, power manage, teardown.  The device type
// determines register offsets and protocol details, but the pattern
// is identical.
//
// A specific driver (e1000e, NVMe, xHCI, HDA) is a set of authored
// rows that bind these generic structs to device-specific values.
// The hardware_operator executes the low-level operations.  This
// layer composes them into driver behaviors.
//
// Dependencies: hardware_operator.zig, fixed.zig

const std = @import("std");

const Text = @import("text.zig").Text;
const TextSmall = @import("text_small.zig").TextSmall;

const fixed = @import("fixed.zig");
const Fixed = fixed.Fixed;
const FixedUnset = fixed.FixedUnset;
const FixedUnbounded = fixed.FixedUnbounded;
const FIXED_ONE = fixed.FIXED_ONE;

const hw = @import("hardware_operator.zig");
const HwOpType = hw.HwOpType;
const HardwareOperation = hw.HardwareOperation;
const HardwareOperationSet = hw.HardwareOperationSet;
const DmaDirection = hw.DmaDirection;
const DmaPurpose = hw.DmaPurpose;
const MemoryCacheability = hw.MemoryCacheability;
const InterruptDeliveryMode = hw.InterruptDeliveryMode;
const InterruptTriggerMode = hw.InterruptTriggerMode;
const PciPowerState = hw.PciPowerState;
const PortWidth = hw.PortWidth;

// ============================================================
// DRIVER IDENTITY AND LIFECYCLE
// ============================================================

pub const DriverClass = enum(i32) {
    None = -1,

    // Storage
    NVMe = 0,
    AHCI, // SATA via AHCI
    VirtIOBlock,
    USBMassStorage,

    // Network
    EthernetIntel, // e1000, e1000e, igb, ixgbe, ice
    EthernetRealtek, // rtl8139, rtl8169
    EthernetBroadcom, // bnx2, tg3
    EthernetVirtIO,
    WiFiIntel, // iwlwifi
    WiFiAtheros,

    // Display
    VGABasic, // VESA/VBE/GOP framebuffer
    IntelGPU, // i915 equivalent
    AMDGpu, // amdgpu equivalent
    VirtIOGPU,

    // Audio
    IntelHDA, // High Definition Audio (Azalia)
    USBAudio,

    // USB Host
    XHCI, // USB 3.x
    EHCI, // USB 2.0
    OHCI, // USB 1.1
    UHCI, // USB 1.1 (Intel)

    // Input
    PS2, // Keyboard and mouse
    USBHIDKeyboard,
    USBHIDMouse,
    USBHIDGamepad,

    // Serial
    UART16550, // COM port
    USBSerial,

    // Platform
    ACPIPlatform,
    PCIBridge,
    ISABridge,

    // Virtual
    VirtIOConsole,
    VirtIONet,
    VirtIOGPU_V,
    VirtIOInput,
};

pub const DriverState = enum(i32) {
    None = -1,
    Discovered = 0, // PCI device found, not yet probed
    Probed, // Device matches a driver, not yet initialized
    Initializing, // Init sequence in progress
    Ready, // Fully operational
    Running, // Actively processing IO
    Suspended, // Power-saved, state retained
    Error, // Error state, needs reset or removal
    Resetting, // Reset in progress
    Removing, // Teardown in progress
    Removed, // Cleaned up, slot reusable
};

pub const DriverDescriptor = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),
    driver_class: DriverClass = .None,

    // PCI match criteria (which devices this driver claims)
    match: DriverMatchCriteria = .{},

    // Current state
    state: DriverState = .None,

    // Bound hardware
    pci_device_id: i32 = -1, // Index into PciDeviceTable
    core_affinity: i32 = -1, // Preferred core for interrupt handling

    // Init/teardown sequences
    init_sequence_id: i32 = -1, // DriverSequence for initialization
    teardown_sequence_id: i32 = -1, // DriverSequence for cleanup
    reset_sequence_id: i32 = -1, // DriverSequence for error recovery
    suspend_sequence_id: i32 = -1, // DriverSequence for power save
    resume_sequence_id: i32 = -1, // DriverSequence for wake

    // Register map
    register_map_id: i32 = -1, // RegisterMap for this device

    // DMA configuration
    dma_config_id: i32 = -1, // DmaConfig for this device

    // Interrupt configuration
    interrupt_config_id: i32 = -1, // InterruptConfig for this device

    // Command interface
    command_interface_id: i32 = -1, // CommandInterface for this device

    // Completion interface
    completion_interface_id: i32 = -1, // CompletionInterface for this device

    // Error handler
    error_handler_id: i32 = -1, // ErrorHandler for this device

    // Power manager
    power_config_id: i32 = -1, // PowerConfig for this device

    // Statistics
    stats_id: i32 = -1, // DriverStats

    // Feature flags (device-specific capabilities discovered at probe)
    feature_flags: u64 = 0,
    max_queues: i32 = 1,
    max_queue_depth: i32 = 256,
    max_transfer_size: u32 = 0,
    max_scatter_gather: i32 = 0,

    // Version
    hardware_version: u32 = 0,
    firmware_version: u32 = 0,

    is_deleted: bool = false,
};

// ============================================================
// PCI MATCH CRITERIA — which devices a driver claims
// ============================================================

pub const MatchType = enum(i32) {
    None = -1,
    VendorDevice = 0, // Match vendor_id + device_id
    VendorClass, // Match vendor_id + class_code + subclass
    ClassOnly, // Match class_code + subclass + prog_if
    VendorAny, // Match vendor_id, any device
    SubsystemMatch, // Match subsystem vendor + subsystem device
    Custom, // Match by a custom predicate set
};

pub const DriverMatchEntry = struct {
    vendor_id: u16 = 0,
    device_id: u16 = 0,
    subsystem_vendor_id: u16 = 0,
    subsystem_device_id: u16 = 0,
    class_code: i32 = -1,
    subclass: i32 = -1,
    prog_if: i32 = -1,
    revision_min: u8 = 0,
    revision_max: u8 = 255,

    // Label for this variant
    variant_name: TextSmall = TextSmall.initEmpty(),
    // Feature flags specific to this variant
    variant_features: u64 = 0,
};

pub const MAX_MATCH_ENTRIES: usize = 32;

pub const DriverMatchCriteria = struct {
    match_type: MatchType = .VendorDevice,
    entries: [MAX_MATCH_ENTRIES]DriverMatchEntry = [_]DriverMatchEntry{.{}} ** MAX_MATCH_ENTRIES,
    entry_count: i32 = 0,
};

// ============================================================
// REGISTER MAP — device register definitions
// ============================================================

pub const RegisterAccess = enum(i32) {
    ReadOnly = 0,
    WriteOnly,
    ReadWrite,
    ReadClear, // Read clears the register (status registers)
    ReadWriteClear, // Write-1-to-clear bits
    WriteOnce, // Can only be written once (lock registers)
};

pub const RegisterWidth = enum(i32) {
    Bits8 = 0,
    Bits16,
    Bits32,
    Bits64,
};

pub const RegisterSpace = enum(i32) {
    MMIO = 0, // Memory-mapped IO (via BAR)
    PortIO, // x86 port IO
    PciConfig, // PCI configuration space
    MSR, // Model-specific register
};

pub const RegisterField = struct {
    name: TextSmall = TextSmall.initEmpty(),
    bit_offset: i32 = 0,
    bit_width: i32 = 1,
    is_reserved: bool = false,

    // Semantic
    default_value: u64 = 0,
    reset_value: u64 = 0,

    // Named values for this field (enum-like)
    named_values: [8]RegisterNamedValue = [_]RegisterNamedValue{.{}} ** 8,
    named_value_count: i32 = 0,
};

pub const RegisterNamedValue = struct {
    name: TextSmall = TextSmall.initEmpty(),
    value: u64 = 0,
};

pub const MAX_REGISTER_FIELDS: usize = 32;

pub const RegisterDefinition = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    // Location
    space: RegisterSpace = .MMIO,
    bar_index: i32 = 0, // Which BAR for MMIO
    offset: u32 = 0, // Offset from BAR base / port base / config offset
    width: RegisterWidth = .Bits32,
    access: RegisterAccess = .ReadWrite,

    // Fields within the register
    fields: [MAX_REGISTER_FIELDS]RegisterField = [_]RegisterField{.{}} ** MAX_REGISTER_FIELDS,
    field_count: i32 = 0,

    // Reset behavior
    reset_value: u64 = 0,
    requires_write_flush: bool = false, // Read-back after write to ensure completion
    write_delay_ns: i32 = 0, // Minimum delay after write before next access

    // Volatile: value can change without software write (status, counters)
    is_volatile: bool = false,

    // Array: this register repeats at a stride (per-queue registers)
    array_count: i32 = 1,
    array_stride: u32 = 0,
};

pub const MAX_REGISTERS: usize = 512;

pub const RegisterMap = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    registers: [MAX_REGISTERS]RegisterDefinition = [_]RegisterDefinition{.{}} ** MAX_REGISTERS,
    register_count: i32 = 0,

    // BAR mappings (resolved at init from PCI BARs)
    bar_virt_bases: [6]u64 = [_]u64{0} ** 6,
    bar_sizes: [6]u64 = [_]u64{0} ** 6,
    bar_mapped: [6]bool = [_]bool{false} ** 6,

    // Port IO base (for legacy devices)
    port_base: u16 = 0,

    is_deleted: bool = false,
};

// ============================================================
// REGISTER OPERATION — typed read/write/modify on registers
// ============================================================

pub const RegOpType = enum(i32) {
    None = -1,

    // Basic access
    Read = 0,
    Write,
    ReadField, // Read a named field within a register
    WriteField, // Write a named field
    SetBits, // OR mask into register
    ClearBits, // AND ~mask into register
    ToggleBits, // XOR mask
    TestBits, // Test if bits are set, result in result_bool

    // Read-modify-write
    ModifyField, // Read, change one field, write back
    MaskedWrite, // Write only bits in mask, preserve others

    // Polling
    PollUntilSet, // Read until specified bits are set
    PollUntilClear, // Read until specified bits are clear
    PollUntilValue, // Read until register equals value
    PollTimeout, // Poll with timeout, report failure

    // Array access (per-queue registers)
    ReadIndexed, // Read register[index]
    WriteIndexed, // Write register[index]
    ModifyFieldIndexed, // Modify field in register[index]

    // Bulk
    ReadAll, // Read all registers in map (snapshot)
    WriteSequence, // Write a sequence of register values
    RestoreSnapshot, // Write all registers from snapshot

    // Barrier
    ReadBarrier, // Memory fence before next read
    WriteBarrier, // Memory fence before next write
    FullBarrier, // Full memory fence
    FlushWrites, // Flush write-combining buffers
};

pub const RegisterOperation = struct {
    id: i32 = -1,
    op: RegOpType = .None,

    // Which register (by index in RegisterMap)
    register_index: i32 = -1,
    // Or by name (resolved at execution)
    register_name: TextSmall = TextSmall.initEmpty(),

    // Which field (by index in register's fields)
    field_index: i32 = -1,
    field_name: TextSmall = TextSmall.initEmpty(),

    // Array index (for per-queue registers)
    array_index: i32 = 0,

    // Value to write / mask / compare
    value: u64 = 0,
    mask: u64 = 0,

    // Polling
    poll_interval_ns: i32 = 100,
    poll_timeout_us: i32 = 1000,
    poll_expected_value: u64 = 0,

    // Result (written by executor)
    result_value: u64 = 0,
    result_bool: bool = false,
    result_timed_out: bool = false,

    // Delay after this operation
    post_delay_ns: i32 = 0,

    // Condition: skip this operation unless a previous result matches
    condition_op_index: i32 = -1, // Index in parent set
    condition_match_value: u64 = 0,
    condition_match_mask: u64 = 0xFFFFFFFFFFFFFFFF,
    condition_invert: bool = false,

    is_deleted: bool = false,
};

pub const RegisterOperationSet = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    operations: []RegisterOperation = &.{},
    stop_on_error: bool = true,
    stop_on_timeout: bool = true,

    is_deleted: bool = false,
};

// ============================================================
// DMA RING CONFIGURATION — generic ring buffer setup
// ============================================================

pub const RingType = enum(i32) {
    None = -1,
    SubmissionQueue = 0, // Driver writes, device reads (commands)
    CompletionQueue, // Device writes, driver reads (completions)
    TransmitRing, // Driver writes, NIC reads (tx packets)
    ReceiveRing, // NIC writes, driver reads (rx packets)
    TransferRing, // USB: bidirectional transfer descriptors
    EventRing, // USB: event notifications
    CommandRing, // USB: host commands
};

pub const RingDescriptorFormat = enum(i32) {
    None = -1,
    NVMeSubmission = 0, // 64-byte NVMe submission queue entry
    NVMeCompletion, // 16-byte NVMe completion queue entry
    E1000Tx, // 16-byte e1000 transmit descriptor
    E1000Rx, // 16-byte e1000 receive descriptor
    IxgbeTx, // 16-byte ixgbe advanced transmit
    IxgbeRx, // 16-byte ixgbe advanced receive
    XhciTRB, // 16-byte xHCI transfer request block
    XhciEvent, // 16-byte xHCI event
    HDABdl, // 8-byte HDA buffer descriptor list entry
    VirtIODesc, // 16-byte virtio descriptor
    VirtIOAvail, // Virtio available ring entry
    VirtIOUsed, // Virtio used ring entry
    Generic, // Custom layout defined by fields
};

pub const RingDescriptorField = struct {
    name: TextSmall = TextSmall.initEmpty(),
    byte_offset: i32 = 0,
    bit_offset: i32 = 0,
    bit_width: i32 = 0,
    is_address: bool = false, // This field holds a physical address
    is_length: bool = false, // This field holds a transfer length
    is_status: bool = false, // This field holds completion status
    is_flags: bool = false, // This field holds control flags
    is_command: bool = false, // This field holds a command opcode
    is_id: bool = false, // This field holds a request identifier
};

pub const MAX_DESCRIPTOR_FIELDS: usize = 16;

pub const RingConfig = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),
    ring_type: RingType = .None,

    // Size
    entry_count: i32 = 256,
    entry_size_bytes: i32 = 64, // Per descriptor

    // Descriptor format
    format: RingDescriptorFormat = .None,
    fields: [MAX_DESCRIPTOR_FIELDS]RingDescriptorField = [_]RingDescriptorField{.{}} ** MAX_DESCRIPTOR_FIELDS,
    field_count: i32 = 0,

    // DMA buffer
    dma_id: i32 = -1, // DmaDescriptor in hardware_operator

    // Doorbell: how the driver notifies the device of new entries
    doorbell_register_index: i32 = -1, // In RegisterMap
    doorbell_register_name: TextSmall = TextSmall.initEmpty(),
    doorbell_array_index: i32 = 0, // For per-queue doorbells

    // Head/tail tracking
    // For submission: driver writes tail, device reads tail, advances head
    // For completion: device writes tail, driver reads tail, advances head
    head_register_index: i32 = -1,
    tail_register_index: i32 = -1,
    driver_owns_tail: bool = true, // true for submission, false for completion

    // Interrupt coalescing
    interrupt_vector: i32 = -1,
    coalesce_count: i32 = 0, // Interrupt after N completions
    coalesce_timeout_us: i32 = 0, // Interrupt after N microseconds

    // Alignment requirements
    base_alignment: u32 = 4096, // Physical address alignment
    entry_alignment: u32 = 0, // Per-entry alignment (0 = packed)

    // Phase bit (NVMe, xHCI use phase bits for ownership tracking)
    uses_phase_bit: bool = false,
    phase_bit_offset: i32 = 0, // Bit position in the status/flags field

    is_deleted: bool = false,
};

pub const MAX_RINGS: usize = 64;

pub const DmaRingTable = struct {
    rings: [MAX_RINGS]RingConfig = [_]RingConfig{.{}} ** MAX_RINGS,
    ring_count: i32 = 0,
};

// ============================================================
// COMMAND INTERFACE — submit work to the device
// ============================================================

pub const CommandType = enum(i32) {
    None = -1,

    // Storage
    StorageRead = 0,
    StorageWrite,
    StorageFlush,
    StorageTrim,
    StorageIdentify,
    StorageGetFeatures,
    StorageSetFeatures,
    StorageGetLogPage,
    StorageFormatNVM,
    StorageSecuritySend,
    StorageSecurityReceive,

    // Network
    NetTransmit = 100,
    NetReceivePost, // Post receive buffers
    NetSetMACFilter,
    NetSetPromiscuous,
    NetSetMulticast,
    NetSetVLAN,
    NetGetLinkStatus,
    NetSetLinkSpeed,
    NetSetMTU,
    NetGetStatistics,
    NetReset,
    NetEnableRx,
    NetDisableRx,
    NetEnableTx,
    NetDisableTx,

    // USB
    USBControlTransfer = 200,
    USBBulkTransfer,
    USBInterruptTransfer,
    USBIsochronousTransfer,
    USBGetDescriptor,
    USBSetConfiguration,
    USBSetInterface,
    USBSetAddress,
    USBResetPort,
    USBEnableSlot,
    USBDisableSlot,
    USBAddressDevice,
    USBEvaluateContext,

    // Audio
    AudioSetStream = 300,
    AudioStartStream,
    AudioStopStream,
    AudioSetFormat,
    AudioSetVolume,
    AudioGetPosition,
    AudioSetCodecVerb,
    AudioGetCodecResponse,

    // Display
    DisplaySetMode = 400,
    DisplayFlip,
    DisplaySetCursor,
    DisplayMoveCursor,
    DisplaySetGamma,
    DisplayEnableOutput,
    DisplayDisableOutput,

    // Generic
    GenericCommand = 500,
    GenericVendorSpecific,
};

pub const CommandDescriptor = struct {
    id: i32 = -1,
    command_type: CommandType = .None,

    // Which submission ring to use
    ring_id: i32 = -1,

    // Command-specific opcode (written to the descriptor's command field)
    opcode: u32 = 0,

    // Data transfer
    data_dma_id: i32 = -1, // DMA buffer for transfer data
    data_phys_addr: u64 = 0,
    data_length: u32 = 0,
    data_offset: u64 = 0, // LBA for storage, offset for others

    // Scatter-gather list
    sg_entries: [16]ScatterGatherEntry = [_]ScatterGatherEntry{.{}} ** 16,
    sg_count: i32 = 0,

    // Command-specific parameters
    param0: u64 = 0,
    param1: u64 = 0,
    param2: u64 = 0,
    param3: u64 = 0,
    param_flags: u32 = 0,

    // Network-specific
    net_packet_length: u16 = 0,
    net_checksum_offload: bool = false,
    net_tso_enable: bool = false,
    net_tso_mss: u16 = 0,
    net_vlan_tag: u16 = 0,
    net_vlan_insert: bool = false,

    // USB-specific
    usb_endpoint: u8 = 0,
    usb_device_slot: i32 = -1,
    usb_request_type: u8 = 0,
    usb_request: u8 = 0,
    usb_value: u16 = 0,
    usb_index: u16 = 0,

    // Audio-specific
    audio_stream_id: i32 = -1,
    audio_codec_node: i32 = 0,
    audio_verb: u32 = 0,
    audio_sample_rate: i32 = 44100,
    audio_channels: i32 = 2,
    audio_bits_per_sample: i32 = 16,

    // Tracking
    tag: u32 = 0, // Unique ID to match completion
    is_barrier: bool = false, // Force ordering with previous commands
    timeout_us: i32 = 0, // 0 = no timeout
    priority: i32 = 0, // Higher = more urgent

    // State
    is_submitted: bool = false,
    is_completed: bool = false,
    submit_tsc: u64 = 0,
    complete_tsc: u64 = 0,
};

pub const ScatterGatherEntry = struct {
    phys_addr: u64 = 0,
    length: u32 = 0,
    is_last: bool = false,
};

pub const MAX_PENDING_COMMANDS: usize = 1024;

pub const CommandInterface = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    // Command pool
    commands: [MAX_PENDING_COMMANDS]CommandDescriptor = [_]CommandDescriptor{.{}} ** MAX_PENDING_COMMANDS,
    next_tag: u32 = 1,

    // Queue management
    submission_ring_ids: [16]i32 = [_]i32{-1} ** 16,
    queue_count: i32 = 1,

    // Build sequence: register ops to assemble a descriptor in the ring
    build_sequence_id: i32 = -1, // RegisterOperationSet that writes fields

    // Submit sequence: register ops to ring the doorbell
    submit_sequence_id: i32 = -1, // RegisterOperationSet that writes tail

    // Statistics
    commands_submitted: u64 = 0,
    commands_completed: u64 = 0,
    commands_failed: u64 = 0,
    commands_timed_out: u64 = 0,
    bytes_transferred: u64 = 0,

    is_deleted: bool = false,
};

// ============================================================
// COMPLETION INTERFACE — process device responses
// ============================================================

pub const CompletionStatus = enum(i32) {
    None = -1,
    Success = 0,
    DataError, // CRC error, ECC error
    DeviceError, // Device internal error
    Timeout, // Command timed out
    Aborted, // Command was aborted
    Overflow, // Buffer overflow
    Underrun, // Buffer underrun (audio)
    LinkDown, // Network link lost
    MediaError, // Storage media error
    ProtocolError, // Protocol violation
    Unsupported, // Command not supported
    InvalidField, // Invalid parameter in command
    PowerLoss, // Write failed due to power loss
    ShortTransfer, // USB: less data than requested
    Stall, // USB: endpoint stalled
    Babble, // USB: device sent too much data
};

pub const CompletionEntry = struct {
    tag: u32 = 0, // Matches CommandDescriptor.tag
    status: CompletionStatus = .None,
    status_raw: u32 = 0, // Device-specific raw status

    // Transfer result
    bytes_transferred: u32 = 0,
    residual: u32 = 0, // Bytes NOT transferred (short transfer)

    // Device-specific results
    result0: u64 = 0,
    result1: u64 = 0,

    // Network-specific
    net_rx_length: u16 = 0,
    net_rx_checksum_valid: bool = false,
    net_rx_vlan_tag: u16 = 0,
    net_rx_vlan_stripped: bool = false,
    net_rx_rss_hash: u32 = 0,

    // Timestamp
    completion_tsc: u64 = 0,

    // Phase bit
    phase: bool = false,

    is_valid: bool = false,
};

pub const MAX_COMPLETIONS_PER_POLL: usize = 64;

pub const CompletionInterface = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    // Completion ring
    completion_ring_ids: [16]i32 = [_]i32{-1} ** 16,
    queue_count: i32 = 1,

    // Parse sequence: register ops to read completion entries
    parse_sequence_id: i32 = -1, // RegisterOperationSet that reads fields

    // Advance sequence: register ops to advance the completion head
    advance_sequence_id: i32 = -1, // RegisterOperationSet that writes head

    // Status mapping: device-specific raw status to CompletionStatus
    status_map: [32]StatusMapEntry = [_]StatusMapEntry{.{}} ** 32,
    status_map_count: i32 = 0,

    // Callback routing: what to do when a completion arrives
    success_action_id: i32 = -1, // DriverAction
    error_action_id: i32 = -1,
    timeout_action_id: i32 = -1,

    // Coalescing state
    completions_pending: i32 = 0,
    last_poll_tsc: u64 = 0,

    // Statistics
    completions_processed: u64 = 0,
    errors_total: u64 = 0,
    timeouts_total: u64 = 0,

    is_deleted: bool = false,
};

pub const StatusMapEntry = struct {
    raw_status: u32 = 0,
    raw_mask: u32 = 0xFFFFFFFF,
    mapped_status: CompletionStatus = .None,
    is_fatal: bool = false,
    error_message: TextSmall = TextSmall.initEmpty(),
};

// ============================================================
// ERROR HANDLER — device error detection and recovery
// ============================================================

pub const ErrorAction = enum(i32) {
    None = -1,
    Log = 0, // Log and continue
    Retry, // Retry the failed command
    ResetQueue, // Reset the affected queue
    ResetDevice, // Full device reset
    DisableDevice, // Mark device offline
    Escalate, // Report to hardware error log
    Ignore, // Suppress the error
    FailCommand, // Fail the command to the caller
    FlushQueue, // Flush all pending commands on the queue
    SwitchQueue, // Move work to a different queue
};

pub const ErrorRecoveryStep = struct {
    action: ErrorAction = .None,

    // For Retry
    max_retries: i32 = 3,
    retry_delay_us: i32 = 1000,
    backoff_multiplier: i32 = 2, // Exponential backoff

    // For ResetQueue / ResetDevice
    reset_sequence_id: i32 = -1, // RegisterOperationSet

    // For SwitchQueue
    alternate_queue: i32 = -1,

    // Condition: only execute if error matches
    match_status: CompletionStatus = .None, // .None = any status
    match_consecutive_count: i32 = 0, // Only after N consecutive same errors

    // Escalation: if this step fails, try next
    next_step_index: i32 = -1,
};

pub const MAX_RECOVERY_STEPS: usize = 16;

pub const ErrorHandler = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    // Recovery steps, tried in order until one succeeds
    steps: [MAX_RECOVERY_STEPS]ErrorRecoveryStep = [_]ErrorRecoveryStep{.{}} ** MAX_RECOVERY_STEPS,
    step_count: i32 = 0,

    // Thresholds
    max_errors_per_second: i32 = 100, // Above this, disable device
    max_total_errors: u64 = 10000, // Lifetime limit before disable
    max_consecutive_errors: i32 = 10, // Consecutive failures before reset

    // Watchdog: device must produce a completion within this time
    watchdog_timeout_us: i32 = 0, // 0 = disabled
    watchdog_action: ErrorAction = .ResetDevice,

    // Health tracking
    errors_this_second: i32 = 0,
    consecutive_errors: i32 = 0,
    total_errors: u64 = 0,
    total_resets: u32 = 0,
    last_error_tsc: u64 = 0,
    last_reset_tsc: u64 = 0,
    is_healthy: bool = true,

    // Link state monitoring (network)
    link_down_action: ErrorAction = .Log,
    link_down_count: u32 = 0,
    last_link_change_tsc: u64 = 0,

    is_deleted: bool = false,
};

// ============================================================
// POWER CONFIGURATION — device power state management
// ============================================================

pub const DevicePowerPolicy = enum(i32) {
    AlwaysOn = 0, // Never power save
    IdleSuspend, // Suspend after idle timeout
    AggressiveSave, // Minimize power at all times
    PerformanceFirst, // Power save only when completely idle
};

pub const PowerConfig = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    policy: DevicePowerPolicy = .AlwaysOn,

    // Idle detection
    idle_timeout_ms: i32 = 5000, // Time without IO before suspend
    idle_threshold_ops: i32 = 0, // Ops/sec below this = idle

    // Power state transitions
    suspend_sequence_id: i32 = -1, // RegisterOperationSet
    resume_sequence_id: i32 = -1,
    d3_hot_sequence_id: i32 = -1,
    d0_restore_sequence_id: i32 = -1,

    // Wake events
    wake_on_interrupt: bool = false,
    wake_on_io: bool = true,
    wake_on_link: bool = false, // WoL for network

    // PME (PCI Power Management Event)
    supports_pme: bool = false,
    pme_enabled: bool = false,

    // Current state
    current_pci_power: PciPowerState = .D0,
    last_active_tsc: u64 = 0,
    resume_latency_us: i32 = 0,

    // Statistics
    suspend_count: u64 = 0,
    resume_count: u64 = 0,
    time_in_d0_us: u64 = 0,
    time_in_d3_us: u64 = 0,

    is_deleted: bool = false,
};

// ============================================================
// INTERRUPT CONFIGURATION — per-driver interrupt setup
// ============================================================

pub const InterruptMode = enum(i32) {
    None = -1,
    LegacyINTx = 0, // Legacy PCI interrupt pin
    MSI, // Message Signaled Interrupts
    MSIX, // MSI-X (per-queue vectors)
    Polling, // No interrupts, poll completions
};

pub const InterruptHandler = struct {
    vector: i32 = -1,
    target_core: i32 = 0,

    // What to do when this interrupt fires
    // Check these completion queues
    poll_completion_ids: [8]i32 = [_]i32{-1} ** 8,
    poll_count: i32 = 0,

    // Or run this register operation set (clear status, etc.)
    handler_sequence_id: i32 = -1,

    // Coalescing
    coalesce_count: i32 = 0,
    coalesce_timeout_us: i32 = 0,

    // Statistics
    fire_count: u64 = 0,
    spurious_count: u64 = 0,
    handling_cycles_total: u64 = 0,
    handling_cycles_max: u64 = 0,
};

pub const MAX_INTERRUPT_HANDLERS: usize = 32;

pub const InterruptConfig = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    mode: InterruptMode = .MSIX,

    // Handlers per vector
    handlers: [MAX_INTERRUPT_HANDLERS]InterruptHandler = [_]InterruptHandler{.{}} ** MAX_INTERRUPT_HANDLERS,
    handler_count: i32 = 0,

    // Setup sequences
    enable_sequence_id: i32 = -1, // RegisterOperationSet to enable interrupts
    disable_sequence_id: i32 = -1,
    mask_sequence_id: i32 = -1, // Mask individual vectors
    unmask_sequence_id: i32 = -1,
    ack_sequence_id: i32 = -1, // Acknowledge / clear interrupt

    // Affinity: spread vectors across cores
    spread_across_cores: bool = true,
    preferred_cores: [16]i32 = [_]i32{-1} ** 16,
    preferred_core_count: i32 = 0,

    // Polling fallback
    poll_interval_us: i32 = 100, // For polling mode
    adaptive_coalescing: bool = false, // Adjust coalescing based on load

    is_deleted: bool = false,
};

// ============================================================
// DRIVER SEQUENCE — ordered steps for init/teardown/reset
// ============================================================

pub const DriverStepType = enum(i32) {
    None = -1,

    // PCI operations
    PciEnable = 0,
    PciDisable,
    PciEnableBusMaster,
    PciMapBar,
    PciUnmapBar,
    PciSetPowerState,

    // Register operations
    RegisterOps = 100, // Run a RegisterOperationSet

    // DMA operations
    AllocateDmaBuffer = 200,
    FreeDmaBuffer,
    SetupRing,
    TeardownRing,

    // Interrupt operations
    SetupInterrupts = 300,
    TeardownInterrupts,
    EnableInterrupts,
    DisableInterrupts,

    // Device-specific
    WaitForReady = 400, // Poll a status register
    SoftReset, // Write reset bit, wait for ready
    HardReset, // PCI FLR or similar
    LoadFirmware, // DMA firmware to device
    IdentifyDevice, // Read device capabilities
    NegotiateFeatures, // VirtIO feature negotiation
    ConfigureDevice, // Set operational parameters

    // Queue operations
    CreateQueue = 500,
    DestroyQueue,
    EnableQueue,
    DisableQueue,

    // Timing
    Delay = 600, // Wait N microseconds
    Barrier, // Memory barrier

    // Control flow
    ConditionalSkip = 700, // Skip next N steps if condition fails
    GotoStep, // Jump to step index
    RepeatUntil, // Repeat previous N steps until condition

    // Logging
    LogMessage = 800,
    LogRegisterDump,
};

pub const DriverStep = struct {
    id: i32 = -1,
    step_type: DriverStepType = .None,
    name: TextSmall = TextSmall.initEmpty(),

    // PCI
    bar_index: i32 = -1,
    pci_power_state: PciPowerState = .D0,

    // Register operations
    register_op_set_id: i32 = -1,

    // DMA
    dma_size_bytes: u64 = 0,
    dma_direction: DmaDirection = .None,
    dma_purpose: DmaPurpose = .None,
    dma_alignment: u32 = 4096,
    dma_below_4gb: bool = false, // Legacy device requirement
    dma_result_id_var: i32 = -1, // Store allocated DMA id

    // Ring setup
    ring_config_id: i32 = -1,
    ring_queue_index: i32 = 0,

    // Interrupt
    interrupt_config_id: i32 = -1,

    // Wait / poll
    wait_register_index: i32 = -1,
    wait_register_name: TextSmall = TextSmall.initEmpty(),
    wait_mask: u64 = 0,
    wait_expected: u64 = 0,
    wait_timeout_us: i32 = 1000000, // 1 second default
    wait_poll_interval_us: i32 = 100,

    // Reset
    reset_register_index: i32 = -1,
    reset_register_name: TextSmall = TextSmall.initEmpty(),
    reset_bit_mask: u64 = 0,
    reset_wait_us: i32 = 10000,

    // Firmware
    firmware_dma_id: i32 = -1,
    firmware_size: u32 = 0,

    // Feature negotiation (VirtIO)
    feature_bits_required: u64 = 0,
    feature_bits_optional: u64 = 0,
    feature_bits_result_var: i32 = -1,

    // Queue creation
    queue_index: i32 = 0,
    queue_depth: i32 = 256,
    queue_submission_ring_id: i32 = -1,
    queue_completion_ring_id: i32 = -1,

    // Timing
    delay_us: i32 = 0,

    // Control flow
    condition_register_index: i32 = -1,
    condition_mask: u64 = 0,
    condition_expected: u64 = 0,
    condition_invert: bool = false,
    skip_count: i32 = 1,
    goto_step: i32 = -1,
    repeat_count: i32 = -1, // -1 = until condition
    repeat_from_step: i32 = -1,

    // Logging
    log_message: TextSmall = TextSmall.initEmpty(),

    // Result
    result_success: bool = false,
    result_error_message: TextSmall = TextSmall.initEmpty(),

    is_deleted: bool = false,
};

pub const MAX_SEQUENCE_STEPS: usize = 128;

pub const DriverSequence = struct {
    id: i32 = -1,
    name: TextSmall = TextSmall.initEmpty(),

    steps: [MAX_SEQUENCE_STEPS]DriverStep = [_]DriverStep{.{}} ** MAX_SEQUENCE_STEPS,
    step_count: i32 = 0,

    // Stop on first failure
    stop_on_error: bool = true,

    // Local variables (for storing intermediate results)
    local_vars: [16]DriverLocalVar = [_]DriverLocalVar{.{}} ** 16,
    local_var_count: i32 = 0,

    is_deleted: bool = false,
};

pub const DriverLocalVar = struct {
    name: TextSmall = TextSmall.initEmpty(),
    value_u64: u64 = 0,
    value_i32: i32 = 0,
    value_bool: bool = false,
};

// ============================================================
// DRIVER ACTION — what to do when events occur at runtime
// ============================================================

pub const DriverActionType = enum(i32) {
    None = -1,

    // Completion handling
    DeliverToScene = 0, // Write to SceneNetworkBuffers (networking.zig)
    DeliverToAudioBuffer, // Write to audio playback buffer
    DeliverToFrameBuffer, // Write to display framebuffer
    DeliverToInputBuffer, // Write to RawInputBuffer
    DeliverToStorageResult, // Complete a storage read
    DeliverToMemDB, // Write result to a MemDB record

    // Refill
    PostReceiveBuffers = 100, // Refill NIC receive ring
    PostTransferBuffers, // Refill USB transfer ring
    PostAudioBuffers, // Refill audio stream buffers

    // State update
    UpdateLinkStatus = 200, // Network link up/down
    UpdateDeviceStats, // Read hardware counters
    UpdatePowerState, // Power state changed

    // Error
    HandleError = 300, // Invoke ErrorHandler
    HandleWatchdog, // Watchdog timeout
    HandleLinkChange, // Link state transition

    // Custom
    RunRegisterOps = 400, // Execute a RegisterOperationSet
    RunHardwareOps, // Execute a HardwareOperationSet
    EmitSignalChannel, // Write to a signal channel
    WriteResourceValue, // Write to a resource value
    FireTrigger, // Fire a CrossSystemTrigger
};

pub const DriverAction = struct {
    id: i32 = -1,
    action_type: DriverActionType = .None,
    name: TextSmall = TextSmall.initEmpty(),

    // Scene delivery
    target_scene_id: i32 = -1,

    // Register/hardware ops
    register_op_set_id: i32 = -1,
    hardware_op_set_id: i32 = -1,

    // Signal/resource
    signal_channel_id: i32 = -1,
    resource_group_id: i32 = -1,
    signal_value: Fixed = 0,

    // Trigger
    trigger_id: i32 = -1,

    // Buffer management
    refill_ring_id: i32 = -1,
    refill_batch_size: i32 = 16,

    // Stat registers to read
    stat_registers: [16]i32 = [_]i32{-1} ** 16,
    stat_register_count: i32 = 0,

    // Condition
    condition_register_index: i32 = -1,
    condition_mask: u64 = 0,
    condition_expected: u64 = 0,

    is_deleted: bool = false,
};

pub const MAX_DRIVER_ACTIONS: usize = 64;

pub const DriverActionTable = struct {
    actions: [MAX_DRIVER_ACTIONS]DriverAction = [_]DriverAction{.{}} ** MAX_DRIVER_ACTIONS,
    action_count: i32 = 0,
};

// ============================================================
// DEVICE PROFILE — complete device specification as data
// ============================================================

// A device profile is the complete authored specification for one
// type of hardware device.  It contains everything needed to drive
// the device: match criteria, register map, DMA layout, command
// format, completion format, error handling, power management,
// and all init/teardown/runtime sequences.
//
// Loading a device profile into a DriverDescriptor and binding
// it to a PCI device produces a working driver with no code.

pub const DeviceProfile = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),
    driver_class: DriverClass = .None,

    // Match
    match: DriverMatchCriteria = .{},

    // Register map
    register_map: RegisterMap = .{},

    // DMA rings
    ring_configs: [MAX_RINGS]RingConfig = [_]RingConfig{.{}} ** MAX_RINGS,
    ring_count: i32 = 0,

    // Sequences
    init_sequence: DriverSequence = .{},
    teardown_sequence: DriverSequence = .{},
    reset_sequence: DriverSequence = .{},
    suspend_sequence: DriverSequence = .{},
    resume_sequence: DriverSequence = .{},

    // Register operation sets (reusable across sequences and actions)
    register_op_sets: [64]RegisterOperationSet = [_]RegisterOperationSet{.{}} ** 64,
    register_op_set_count: i32 = 0,

    // Command interface
    command_interface: CommandInterface = .{},

    // Completion interface
    completion_interface: CompletionInterface = .{},

    // Interrupt configuration
    interrupt_config: InterruptConfig = .{},

    // Error handler
    error_handler: ErrorHandler = .{},

    // Power configuration
    power_config: PowerConfig = .{},

    // Runtime actions
    actions: DriverActionTable = .{},

    // Device-specific capabilities and limits
    max_queues: i32 = 1,
    max_queue_depth: i32 = 256,
    max_transfer_size: u32 = 0,
    max_scatter_gather: i32 = 0,
    supports_msi: bool = false,
    supports_msix: bool = false,
    supports_64bit_dma: bool = true,
    requires_alignment: u32 = 0,

    // Documentation
    description: Text = Text.initEmpty(),

    is_deleted: bool = false,
};

// ============================================================
// DRIVER TABLE — all active drivers
// ============================================================

pub const MAX_DRIVERS: usize = 64;

pub const DriverTable = struct {
    drivers: [MAX_DRIVERS]DriverDescriptor = [_]DriverDescriptor{.{}} ** MAX_DRIVERS,
    driver_count: i32 = 0,

    // Device profiles (templates for driver creation)
    profiles: [MAX_DRIVERS]DeviceProfile = [_]DeviceProfile{.{}} ** MAX_DRIVERS,
    profile_count: i32 = 0,

    // Probe order (by class priority)
    probe_order: [MAX_DRIVERS]i32 = [_]i32{-1} ** MAX_DRIVERS,
    probe_count: i32 = 0,
};

// ============================================================
// DRIVER STATISTICS — per-driver runtime metrics
// ============================================================

pub const DriverStats = struct {
    id: i32 = -1,
    driver_id: i32 = -1,

    // IO statistics
    ops_submitted: u64 = 0,
    ops_completed: u64 = 0,
    ops_failed: u64 = 0,
    ops_retried: u64 = 0,
    bytes_read: u64 = 0,
    bytes_written: u64 = 0,

    // Latency (in TSC ticks)
    latency_min: u64 = 0xFFFFFFFFFFFFFFFF,
    latency_max: u64 = 0,
    latency_total: u64 = 0,
    latency_count: u64 = 0,

    // Throughput (bytes per second, sampled)
    throughput_read_bps: u64 = 0,
    throughput_write_bps: u64 = 0,
    throughput_sample_tsc: u64 = 0,
    throughput_sample_bytes_read: u64 = 0,
    throughput_sample_bytes_written: u64 = 0,

    // Queue depths
    current_queue_depth: i32 = 0,
    max_queue_depth: i32 = 0,

    // Interrupts
    interrupts_total: u64 = 0,
    interrupts_per_second: u64 = 0,
    spurious_interrupts: u64 = 0,

    // Errors
    errors_total: u64 = 0,
    errors_corrected: u64 = 0,
    errors_fatal: u64 = 0,
    resets_total: u32 = 0,

    // Power
    time_active_us: u64 = 0,
    time_suspended_us: u64 = 0,
    suspend_count: u64 = 0,

    // DMA
    dma_map_count: u64 = 0,
    dma_unmap_count: u64 = 0,
    dma_errors: u64 = 0,

    // Network-specific
    net_packets_rx: u64 = 0,
    net_packets_tx: u64 = 0,
    net_bytes_rx: u64 = 0,
    net_bytes_tx: u64 = 0,
    net_rx_dropped: u64 = 0,
    net_tx_dropped: u64 = 0,
    net_rx_errors: u64 = 0,
    net_tx_errors: u64 = 0,
    net_collisions: u64 = 0,
    net_link_up: bool = false,
    net_link_speed_mbps: i32 = 0,

    // Storage-specific
    storage_sectors_read: u64 = 0,
    storage_sectors_written: u64 = 0,
    storage_iops_read: u64 = 0,
    storage_iops_write: u64 = 0,

    // Audio-specific
    audio_underruns: u64 = 0,
    audio_overruns: u64 = 0,
    audio_position_current: u64 = 0,

    // USB-specific
    usb_stalls: u64 = 0,
    usb_babbles: u64 = 0,
    usb_short_transfers: u64 = 0,
};

// ============================================================
// DRIVER OPERATION — one action on a driver
// ============================================================

pub const DriverOpType = enum(i32) {
    None = -1,

    // Lifecycle
    Probe = 0, // Match PCI device to a profile
    Init, // Run init sequence
    Start, // Begin accepting commands
    Stop, // Stop accepting commands
    Reset, // Run reset sequence
    Suspend, // Run suspend sequence
    Resume, // Run resume sequence
    Remove, // Run teardown sequence

    // Command submission
    SubmitCommand = 100, // Submit one command
    SubmitBatch, // Submit N commands
    FlushQueue, // Flush pending commands
    AbortCommand, // Cancel a pending command
    AbortAll, // Cancel all pending commands

    // Completion processing
    PollCompletions = 200, // Check for completed commands
    ProcessCompletion, // Handle one completion
    DrainCompletions, // Process all pending completions

    // Configuration
    SetFeature = 300, // Set a device feature
    GetFeature, // Query a device feature
    SetParameter, // Set an operational parameter
    GetParameter, // Query an operational parameter
    NegotiateFeatures, // VirtIO feature negotiation

    // Register access (through the driver's register map)
    ReadRegister = 400,
    WriteRegister,
    ReadRegisterField,
    WriteRegisterField,
    PollRegister,
    DumpRegisters, // Read all registers

    // DMA management
    AllocBuffer = 500,
    FreeBuffer,
    MapBuffer,
    UnmapBuffer,
    SyncBuffer,

    // Interrupt management
    EnableInterrupts = 600,
    DisableInterrupts,
    MaskVector,
    UnmaskVector,
    SetCoalescing,
    SetAffinity,

    // Power management
    SetPowerPolicy = 700,
    ForcePowerState,
    WakeDevice,

    // Statistics
    ReadStats = 800,
    ResetStats,
    SampleThroughput,

    // Error handling
    CheckHealth = 900,
    ClearErrors,
    InjectError, // Testing: simulate a device error

    // Firmware
    LoadFirmware = 1000,
    GetFirmwareVersion,

    // Network-specific
    NetSetMAC = 1100,
    NetSetPromiscuous,
    NetSetMTU,
    NetGetLinkStatus,
    NetSetVLAN,
    NetAddMulticast,
    NetRemoveMulticast,

    // Storage-specific
    StorageIdentify = 1200,
    StorageGetSMART,
    StorageTrim,
    StorageFormat,
    StorageSecureErase,

    // Audio-specific
    AudioSetFormat = 1300,
    AudioStartStream,
    AudioStopStream,
    AudioGetPosition,
    AudioSetVolume,
    AudioSetRoute,

    // USB-specific
    USBEnumeratePort = 1400,
    USBResetPort,
    USBSetAddress,
    USBGetDescriptor,
    USBSetConfiguration,
    USBClearStall,
};

pub const DriverOperation = struct {
    id: i32 = -1,
    op: DriverOpType = .None,

    // Target driver
    driver_id: i32 = -1,

    // Command submission
    command: CommandDescriptor = .{},
    batch_commands: []CommandDescriptor = &.{},
    command_tag: u32 = 0,

    // Queue selection
    queue_index: i32 = 0,

    // Register access
    register_name: TextSmall = TextSmall.initEmpty(),
    register_index: i32 = -1,
    field_name: TextSmall = TextSmall.initEmpty(),
    field_index: i32 = -1,
    register_value: u64 = 0,
    register_mask: u64 = 0,
    register_array_index: i32 = 0,

    // DMA
    buffer_size: u64 = 0,
    buffer_direction: DmaDirection = .None,
    buffer_purpose: DmaPurpose = .None,
    buffer_dma_id: i32 = -1,

    // Interrupt
    interrupt_vector: i32 = -1,
    coalesce_count: i32 = 0,
    coalesce_timeout_us: i32 = 0,
    affinity_core: i32 = -1,

    // Power
    power_policy: hw.CorePowerState = .Active,
    pci_power_state: PciPowerState = .D0,

    // Feature/parameter
    feature_id: u32 = 0,
    parameter_id: u32 = 0,
    feature_value: u64 = 0,

    // Network
    mac_address: [6]u8 = [_]u8{0} ** 6,
    mtu: u16 = 1500,
    vlan_id: u16 = 0,
    promiscuous: bool = false,

    // Audio
    audio_stream_id: i32 = -1,
    audio_sample_rate: i32 = 44100,
    audio_channels: i32 = 2,
    audio_bit_depth: i32 = 16,
    audio_volume: Fixed = FIXED_ONE,

    // USB
    usb_port: i32 = -1,
    usb_address: u8 = 0,
    usb_endpoint: u8 = 0,
    usb_descriptor_type: u8 = 0,
    usb_descriptor_index: u8 = 0,
    usb_configuration: u8 = 0,

    // Firmware
    firmware_data_dma_id: i32 = -1,
    firmware_size: u32 = 0,

    // Polling
    poll_timeout_us: i32 = 0,
    poll_max_completions: i32 = 64,

    // Result
    result_u64: u64 = 0,
    result_i32: i32 = 0,
    result_bool: bool = false,
    result_status: CompletionStatus = .None,
    result_error: TextSmall = TextSmall.initEmpty(),

    is_deleted: bool = false,
};

pub const DriverOperationSet = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    operations: []DriverOperation = &.{},
    stop_on_error: bool = true,

    is_deleted: bool = false,
};

// ============================================================
// DEVICE TEMPLATE LIBRARY — pre-authored device profiles
// ============================================================

pub const DeviceTemplateType = enum(i32) {
    Custom = 0,

    // Network
    Intel_E1000,
    Intel_E1000E,
    Intel_IGB,
    Intel_IXGBE,
    Intel_ICE,
    Realtek_RTL8139,
    Realtek_RTL8169,
    Broadcom_TG3,
    VirtIO_Net,

    // Storage
    NVMe_Generic,
    AHCI_Generic,
    VirtIO_Block,

    // USB
    XHCI_Generic,
    EHCI_Generic,

    // Audio
    Intel_HDA,
    USB_Audio_Generic,

    // Display
    VGA_Framebuffer,
    VirtIO_GPU,

    // Input
    PS2_Keyboard,
    PS2_Mouse,
    USB_HID_Generic,

    // Serial
    UART_16550,
    USB_Serial_Generic,
};

pub const DeviceTemplate = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),
    template_type: DeviceTemplateType = .Custom,

    // The complete device profile
    profile: DeviceProfile = .{},

    // Description
    description: Text = Text.initEmpty(),

    // Hardware this has been tested on
    tested_hardware: [16]TextSmall = [_]TextSmall{TextSmall.initEmpty()} ** 16,
    tested_count: i32 = 0,

    is_deleted: bool = false,
};

// ============================================================
// DRIVER MONITOR — runtime diagnostics for all drivers
// ============================================================

pub const DriverMonitor = struct {
    // Per-driver stats
    driver_stats: [MAX_DRIVERS]DriverStats = [_]DriverStats{.{}} ** MAX_DRIVERS,

    // System-wide
    total_interrupts_per_second: u64 = 0,
    total_dma_bytes_per_second: u64 = 0,
    total_commands_per_second: u64 = 0,
    total_errors_per_second: u64 = 0,

    // Device health summary
    devices_healthy: i32 = 0,
    devices_degraded: i32 = 0,
    devices_failed: i32 = 0,
    devices_suspended: i32 = 0,

    // Last probe results
    devices_discovered: i32 = 0,
    devices_claimed: i32 = 0,
    devices_unclaimed: i32 = 0,

    // Timing
    last_sample_tsc: u64 = 0,
    sample_interval_us: i32 = 1000000, // 1 second
};
