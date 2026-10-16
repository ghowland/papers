// hardware_operator.zig — x86-64 hardware operations as typed structs.
//
// Ring 0 direct hardware access.  No HAL.  No abstraction layer.  The
// struct fields ARE the hardware interface.  Reading a field reads
// the hardware.  Writing a field writes the hardware.  The device
// driver operator layer composes these into driver behaviors.
//
// This module covers: CPU cores, interrupts, physical memory,
// DMA, PCI/PCIe, MSI/MSI-X, IOMMU, power states, thermal,
// timers, port IO, MMIO, CPUID, MSRs, cache, TLB, and errors.
//
// Dependencies: fixed.zig, fixed_128.zig

const std = @import("std");

const Text = @import("text.zig").Text;
const TextSmall = @import("text_small.zig").TextSmall;

const fixed = @import("fixed.zig");
const Fixed = fixed.Fixed;
const Fixed2 = @import("fixed2.zig").Fixed2;
const FixedUnset = fixed.FixedUnset;
const FixedUnbounded = fixed.FixedUnbounded;
const FIXED_ONE = fixed.FIXED_ONE;

// ============================================================
// CPU CORE MANAGEMENT
// ============================================================

pub const CoreRole = enum(i32) {
    None = -1,

    // Silo roles
    Orchestrator = 0, // Core 0: interrupts, IO, result installation
    Compute, // Cores 1-N: pure computation, no interrupts
    Dedicated, // Pinned to a specific subsystem (audio, network)
    Parked, // Halted, not scheduled, lowest power
    Reserved, // Reserved for future use, not available
};

pub const CorePowerState = enum(i32) {
    Active = 0, // C0: executing instructions
    Halt, // C1: halted, instant wake
    LightSleep, // C3: caches may flush, fast wake
    DeepSleep, // C6: voltage reduced, slow wake
    Offline, // Fully powered off, requires full init to wake
};

pub const CoreArch = enum(i32) {
    Unknown = -1,
    PerformanceCore = 0, // P-core (Intel hybrid: Golden Cove, etc.)
    EfficiencyCore, // E-core (Intel hybrid: Gracemont, etc.)
    Uniform, // Non-hybrid: all cores identical
};

pub const CoreDescriptor = struct {
    // Identity
    core_id: i32 = -1, // Logical core index (0-based)
    apic_id: i32 = -1, // APIC ID from hardware
    package_id: i32 = -1, // Physical socket
    numa_node: i32 = -1, // NUMA domain

    // Role in Silo
    role: CoreRole = .None,
    arch: CoreArch = .Unknown,

    // Current state
    power_state: CorePowerState = .Active,
    is_online: bool = false,
    is_bsp: bool = false, // Bootstrap processor (first core)

    // Topology
    siblings_mask: u64 = 0, // Bitmask of cores sharing L2
    package_mask: u64 = 0, // Bitmask of cores in same package
    numa_mask: u64 = 0, // Bitmask of cores in same NUMA node

    // Interrupt state
    interrupts_enabled: bool = false, // IF flag
    interrupt_mask: u64 = 0, // Which vectors are masked

    // Performance
    current_frequency_khz: i32 = 0,
    max_frequency_khz: i32 = 0,
    base_frequency_khz: i32 = 0,
    tsc_frequency_khz: i64 = 0,

    // Thermal
    temperature_celsius: i32 = 0,
    thermal_throttled: bool = false,
    tj_max_celsius: i32 = 100,

    // Arena binding (which NUMA-local arena this core uses)
    arena_base_phys: u64 = 0,
    arena_size_bytes: u64 = 0,

    // Statistics
    instructions_retired: u64 = 0,
    cycles_active: u64 = 0,
    cycles_halted: u64 = 0,
    cache_misses_l1: u64 = 0,
    cache_misses_l2: u64 = 0,
    cache_misses_l3: u64 = 0,
    context_switches: u64 = 0, // Should be 0 for compute cores
    interrupts_handled: u64 = 0, // Should be 0 for compute cores
};

pub const MAX_CORES: usize = 256;

pub const CoreTable = struct {
    cores: [MAX_CORES]CoreDescriptor = [_]CoreDescriptor{.{}} ** MAX_CORES,
    core_count: i32 = 0,
    online_count: i32 = 0,
    orchestrator_core: i32 = 0,
    compute_core_count: i32 = 0,

    // Platform
    is_hybrid: bool = false, // Intel Alder Lake+ with P/E cores
    packages: i32 = 0, // Physical sockets
    numa_nodes: i32 = 0, // NUMA domains
};

// ============================================================
// CPUID FEATURE DETECTION
// ============================================================

pub const CpuVendor = enum(i32) {
    Unknown = -1,
    Intel = 0,
    AMD,
    Hygon,
    VIA,
    Zhaoxin,
};

pub const CpuFeatures = struct {
    vendor: CpuVendor = .Unknown,
    brand_string: Text = Text.initEmpty(),
    family: i32 = 0,
    model: i32 = 0,
    stepping: i32 = 0,

    // Instruction set extensions
    has_sse2: bool = false,
    has_sse3: bool = false,
    has_ssse3: bool = false,
    has_sse41: bool = false,
    has_sse42: bool = false,
    has_avx: bool = false,
    has_avx2: bool = false,
    has_avx512f: bool = false,
    has_avx512bw: bool = false,
    has_avx512vl: bool = false,
    has_bmi1: bool = false,
    has_bmi2: bool = false,
    has_popcnt: bool = false,
    has_lzcnt: bool = false,
    has_aes_ni: bool = false,
    has_sha: bool = false,
    has_clmul: bool = false,
    has_f16c: bool = false,
    has_fma: bool = false,
    has_movbe: bool = false,
    has_rdrand: bool = false,
    has_rdseed: bool = false,
    has_cmpxchg16b: bool = false,

    // Memory
    has_clflush: bool = false,
    has_clflushopt: bool = false,
    has_clwb: bool = false,
    has_prefetchw: bool = false,
    has_umip: bool = false,

    // Virtualization and security
    has_vmx: bool = false, // Intel VT-x
    has_svm: bool = false, // AMD-V
    has_smep: bool = false,
    has_smap: bool = false,
    has_nx: bool = false, // NX/XD bit

    // Timer
    has_tsc: bool = false,
    has_tsc_deadline: bool = false,
    has_invariant_tsc: bool = false,
    has_rdtscp: bool = false,

    // Topology
    has_x2apic: bool = false,
    has_apic: bool = false,

    // IOMMU
    has_iommu: bool = false, // Intel VT-d or AMD-Vi

    // Cache
    l1d_size_kb: i32 = 0,
    l1i_size_kb: i32 = 0,
    l2_size_kb: i32 = 0,
    l3_size_kb: i32 = 0,
    cache_line_bytes: i32 = 64,

    // Address widths
    phys_address_bits: i32 = 0,
    virt_address_bits: i32 = 0,

    // Maximum CPUID leaf
    max_basic_leaf: i32 = 0,
    max_extended_leaf: i32 = 0,
};

// ============================================================
// MSR (Model-Specific Register) ACCESS
// ============================================================

pub const MsrAccess = struct {
    msr_address: u32 = 0,
    value: u64 = 0,
    core_id: i32 = -1, // Which core to read/write on

    // Well-known MSR addresses
    pub const IA32_APIC_BASE: u32 = 0x1B;
    pub const IA32_FEATURE_CONTROL: u32 = 0x3A;
    pub const IA32_TSC: u32 = 0x10;
    pub const IA32_MTRR_DEF_TYPE: u32 = 0x2FF;
    pub const IA32_PAT: u32 = 0x277;
    pub const IA32_EFER: u32 = 0xC0000080;
    pub const IA32_STAR: u32 = 0xC0000081;
    pub const IA32_LSTAR: u32 = 0xC0000082;
    pub const IA32_FMASK: u32 = 0xC0000084;
    pub const IA32_FS_BASE: u32 = 0xC0000100;
    pub const IA32_GS_BASE: u32 = 0xC0000101;
    pub const IA32_KERNEL_GS_BASE: u32 = 0xC0000102;
    pub const IA32_TSC_AUX: u32 = 0xC0000103;
    pub const IA32_MISC_ENABLE: u32 = 0x1A0;
    pub const IA32_PERF_STATUS: u32 = 0x198;
    pub const IA32_PERF_CTL: u32 = 0x199;
    pub const IA32_THERM_STATUS: u32 = 0x19C;
    pub const IA32_THERM_INTERRUPT: u32 = 0x19B;
    pub const IA32_PACKAGE_THERM_STATUS: u32 = 0x1B1;
    pub const IA32_HWP_REQUEST: u32 = 0x774;
    pub const IA32_HWP_STATUS: u32 = 0x777;
    pub const IA32_ENERGY_PERF_BIAS: u32 = 0x1B0;
    pub const IA32_MCG_CAP: u32 = 0x179;
    pub const IA32_MCG_STATUS: u32 = 0x17A;
    pub const IA32_MC0_CTL: u32 = 0x400;
    pub const IA32_MC0_STATUS: u32 = 0x401;
};

// ============================================================
// INTERRUPT MANAGEMENT
// ============================================================

pub const InterruptType = enum(i32) {
    None = -1,

    // Exceptions (0-31)
    DivideError = 0,
    Debug = 1,
    NMI = 2,
    Breakpoint = 3,
    Overflow = 4,
    BoundRange = 5,
    InvalidOpcode = 6,
    DeviceNotAvail = 7,
    DoubleFault = 8,
    InvalidTSS = 10,
    SegmentNotPresent = 11,
    StackFault = 12,
    GeneralProtection = 13,
    PageFault = 14,
    X87Float = 16,
    AlignmentCheck = 17,
    MachineCheck = 18,
    SIMDFloat = 19,

    // Hardware IRQs (mapped to vectors 32+)
    Timer = 32,
    Keyboard = 33,
    Cascade = 34,
    COM2 = 35,
    COM1 = 36,
    LPT2 = 37,
    Floppy = 38,
    LPT1 = 39,
    RTC = 40,
    ACPI = 41,
    Mouse = 44,
    FPU = 45,
    PrimaryATA = 46,
    SecondaryATA = 47,

    // MSI/MSI-X (vectors 48-255)
    MSIBase = 48,

    // Software-defined
    IPIReschedule = 240,
    IPIFlushTLB = 241,
    IPIStop = 242,
    Spurious = 255,
};

pub const InterruptDeliveryMode = enum(i32) {
    Fixed = 0,
    LowestPriority,
    SMI,
    NMI,
    Init,
    StartUp,
    ExtINT,
};

pub const InterruptTriggerMode = enum(i32) {
    Edge = 0,
    Level,
};

pub const InterruptPolarity = enum(i32) {
    ActiveHigh = 0,
    ActiveLow,
};

pub const InterruptDescriptor = struct {
    vector: i32 = -1,
    interrupt_type: InterruptType = .None,

    // Routing
    target_core: i32 = 0, // Which core receives this interrupt
    delivery_mode: InterruptDeliveryMode = .Fixed,
    trigger_mode: InterruptTriggerMode = .Edge,
    polarity: InterruptPolarity = .ActiveHigh,

    // State
    is_masked: bool = true,
    is_active: bool = false,
    pending: bool = false,

    // Handler
    handler_address: u64 = 0,
    ist_index: i32 = 0, // Interrupt Stack Table entry (0 = no IST)

    // Statistics
    fire_count: u64 = 0,
    last_fire_tsc: u64 = 0,
    total_handling_cycles: u64 = 0,
    max_handling_cycles: u64 = 0,
};

pub const MAX_VECTORS: usize = 256;

pub const InterruptTable = struct {
    descriptors: [MAX_VECTORS]InterruptDescriptor = [_]InterruptDescriptor{.{}} ** MAX_VECTORS,

    // APIC state
    apic_base_phys: u64 = 0,
    apic_base_virt: u64 = 0,
    is_x2apic: bool = false,
    apic_id: i32 = 0,

    // EOI tracking
    last_vector_serviced: i32 = -1,
    eoi_count: u64 = 0,

    // NMI state
    nmi_pending: bool = false,
    nmi_count: u64 = 0,

    // IPI state
    ipi_sent_count: u64 = 0,
    ipi_received_count: u64 = 0,
};

// ============================================================
// IO APIC
// ============================================================

pub const IoApicDescriptor = struct {
    id: i32 = -1,
    base_phys: u64 = 0,
    base_virt: u64 = 0,
    gsi_base: i32 = 0, // Global System Interrupt base
    max_redirection_entries: i32 = 0,

    // Redirection entries (IRQ routing)
    redirections: [24]IoApicRedirection = [_]IoApicRedirection{.{}} ** 24,
};

pub const IoApicRedirection = struct {
    vector: i32 = 0,
    delivery_mode: InterruptDeliveryMode = .Fixed,
    dest_mode: IoApicDestMode = .Physical,
    polarity: InterruptPolarity = .ActiveHigh,
    trigger_mode: InterruptTriggerMode = .Edge,
    is_masked: bool = true,
    destination: i32 = 0, // APIC ID or logical destination
};

pub const IoApicDestMode = enum(i32) {
    Physical = 0,
    Logical,
};

pub const MAX_IO_APICS: usize = 8;

pub const IoApicTable = struct {
    io_apics: [MAX_IO_APICS]IoApicDescriptor = [_]IoApicDescriptor{.{}} ** MAX_IO_APICS,
    count: i32 = 0,
};

// ============================================================
// PHYSICAL MEMORY MAP
// ============================================================

pub const MemoryRegionType = enum(i32) {
    None = -1,
    Usable = 0, // Free RAM
    Reserved, // BIOS/firmware reserved
    ACPI_Reclaimable, // ACPI tables, reclaimable after parsing
    ACPI_NVS, // ACPI non-volatile storage
    BadMemory, // Defective
    Kernel, // Silo binary loaded here
    FrameBuffer, // Display memory
    MMIO, // Memory-mapped IO device registers
    DMABuffer, // Pre-allocated DMA buffers
    Arena, // Core-pinned NUMA arena
    MemDB, // MemDB persistent storage
    ScratchPool, // Shared scratch allocation pool
    NetworkBuffer, // NIC DMA ring buffers
    NVMeBuffer, // NVMe DMA buffers
    PageTable, // Page tables (minimal, identity map)
    Stack, // Per-core kernel stacks
    IST, // Interrupt Stack Table entries
};

pub const MemoryCacheability = enum(i32) {
    Uncacheable = 0, // UC: device MMIO
    WriteCombining, // WC: framebuffer, streaming writes
    WriteThrough, // WT: rarely used
    WriteProtect, // WP: read-cached, write-through
    WriteBack, // WB: normal RAM
};

pub const MemoryRegion = struct {
    id: i32 = -1,
    region_type: MemoryRegionType = .None,
    phys_start: u64 = 0,
    phys_end: u64 = 0,
    size_bytes: u64 = 0,

    // Cacheability (set via MTRR or PAT)
    cacheability: MemoryCacheability = .WriteBack,

    // NUMA affinity
    numa_node: i32 = -1,

    // Ownership
    owner_core: i32 = -1, // For arenas: which core owns this
    owner_device: i32 = -1, // For MMIO/DMA: which PCI device

    // State
    is_allocated: bool = false,
    is_locked: bool = false, // Cannot be reclaimed

    // Label
    label: TextSmall = TextSmall.initEmpty(),
};

pub const MAX_MEMORY_REGIONS: usize = 512;

pub const PhysicalMemoryMap = struct {
    regions: [MAX_MEMORY_REGIONS]MemoryRegion = [_]MemoryRegion{.{}} ** MAX_MEMORY_REGIONS,
    region_count: i32 = 0,

    // Summary
    total_bytes: u64 = 0,
    usable_bytes: u64 = 0,
    reserved_bytes: u64 = 0,
    arena_bytes: u64 = 0,
    memdb_bytes: u64 = 0,
    dma_bytes: u64 = 0,
    mmio_bytes: u64 = 0,

    // MTRR state
    mtrr_count: i32 = 0,
    mtrr_entries: [16]MtrrEntry = [_]MtrrEntry{.{}} ** 16,
};

pub const MtrrEntry = struct {
    phys_base: u64 = 0,
    phys_mask: u64 = 0,
    region_type: MemoryCacheability = .WriteBack,
    is_valid: bool = false,
};

// ============================================================
// DMA MANAGEMENT
// ============================================================

pub const DmaDirection = enum(i32) {
    None = -1,
    ToDevice = 0, // RAM → device
    FromDevice, // Device → RAM
    Bidirectional,
};

pub const DmaDescriptor = struct {
    id: i32 = -1,

    // Physical addresses (device reads these directly)
    phys_addr: u64 = 0,
    size_bytes: u64 = 0,

    // Direction
    direction: DmaDirection = .None,

    // Owner
    device_id: i32 = -1, // PCI device that uses this buffer
    purpose: DmaPurpose = .None,

    // Ring buffer state (for NIC and NVMe)
    ring_head: u32 = 0,
    ring_tail: u32 = 0,
    ring_size: u32 = 0,
    entry_size: u32 = 0,

    // State
    is_active: bool = false,
    is_coherent: bool = true, // CPU cache coherent with device
    needs_sync: bool = false, // Requires explicit cache flush/invalidate

    // Statistics
    bytes_transferred: u64 = 0,
    transfer_count: u64 = 0,
    error_count: u64 = 0,
    last_transfer_tsc: u64 = 0,
};

pub const DmaPurpose = enum(i32) {
    None = -1,
    NicRx = 0, // Network receive
    NicTx, // Network transmit
    NvmeSubmission, // NVMe submission queue
    NvmeCompletion, // NVMe completion queue
    NvmeData, // NVMe data transfer
    AudioPlayback, // Audio DMA buffer
    AudioCapture,
    USBTransfer, // USB host controller
    GPUCommand, // GPU command buffer
    GPUFrameBuffer, // GPU display buffer
    Custom, // Device-specific
};

pub const MAX_DMA_DESCRIPTORS: usize = 128;

pub const DmaTable = struct {
    descriptors: [MAX_DMA_DESCRIPTORS]DmaDescriptor = [_]DmaDescriptor{.{}} ** MAX_DMA_DESCRIPTORS,
    count: i32 = 0,

    // IOMMU state (Intel VT-d or AMD-Vi)
    iommu_enabled: bool = false,
    iommu_base_phys: u64 = 0,
    iommu_base_virt: u64 = 0,

    // Pre-allocated contiguous DMA pools
    pool_32bit_base: u64 = 0, // Below 4GB for legacy devices
    pool_32bit_size: u64 = 0,
    pool_64bit_base: u64 = 0, // Anywhere for modern devices
    pool_64bit_size: u64 = 0,
};

// ============================================================
// PCI / PCIe DEVICE ENUMERATION
// ============================================================

pub const PciDeviceClass = enum(i32) {
    Unknown = -1,
    Unclassified = 0,
    MassStorage = 1,
    Network = 2,
    Display = 3,
    Multimedia = 4,
    Memory = 5,
    Bridge = 6,
    Communication = 7,
    SystemPeripheral = 8,
    Input = 9,
    Docking = 10,
    Processor = 11,
    SerialBus = 12,
    Wireless = 13,
    Intelligent = 14,
    Satellite = 15,
    Encryption = 16,
    SignalProcessing = 17,
};

pub const PciBarType = enum(i32) {
    None = -1,
    Memory32 = 0,
    Memory64,
    IO,
};

pub const PciBar = struct {
    bar_index: i32 = -1,
    bar_type: PciBarType = .None,
    phys_base: u64 = 0,
    size_bytes: u64 = 0,
    is_prefetchable: bool = false,
    is_mapped: bool = false,
    virt_base: u64 = 0, // If mapped to virtual address space
};

pub const PciCapability = enum(i32) {
    None = -1,
    PowerManagement = 0x01,
    AGP = 0x02,
    MSI = 0x05,
    PCIeBridge = 0x06,
    Vendor = 0x09,
    PCIe = 0x10,
    MSIX = 0x11,
    SATA = 0x12,
};

pub const PciMsiState = struct {
    is_enabled: bool = false,
    is_msix: bool = false, // MSI-X vs MSI

    // MSI
    msi_vector_base: i32 = -1,
    msi_vector_count: i32 = 0,
    msi_address: u64 = 0,
    msi_data: u32 = 0,

    // MSI-X
    msix_table_bar: i32 = -1,
    msix_table_offset: u32 = 0,
    msix_table_size: i32 = 0,
    msix_pba_bar: i32 = -1,
    msix_pba_offset: u32 = 0,
};

pub const PciPowerState = enum(i32) {
    D0 = 0, // Fully on
    D1, // Light sleep
    D2, // Deeper sleep
    D3hot, // Software off, power on
    D3cold, // Power off
};

pub const PciDevice = struct {
    // Identity
    id: i32 = -1,
    bus: i32 = 0,
    device: i32 = 0,
    function: i32 = 0,

    // PCI config space
    vendor_id: u16 = 0,
    device_id: u16 = 0,
    subsystem_vendor_id: u16 = 0,
    subsystem_device_id: u16 = 0,
    revision_id: u8 = 0,

    // Classification
    class_code: PciDeviceClass = .Unknown,
    subclass: u8 = 0,
    prog_if: u8 = 0,
    header_type: u8 = 0,

    // BARs (Base Address Registers)
    bars: [6]PciBar = [_]PciBar{.{}} ** 6,

    // Interrupt
    interrupt_line: u8 = 0,
    interrupt_pin: u8 = 0,
    msi: PciMsiState = .{},

    // Power
    power_state: PciPowerState = .D0,
    supports_d1: bool = false,
    supports_d2: bool = false,
    supports_pme: bool = false,

    // PCIe specific
    is_pcie: bool = false,
    pcie_link_speed: PcieLinkSpeed = .None,
    pcie_link_width: i32 = 0, // x1, x2, x4, x8, x16
    pcie_max_speed: PcieLinkSpeed = .None,
    pcie_max_width: i32 = 0,

    // Capabilities
    capabilities: [16]PciCapability = [_]PciCapability{.None} ** 16,
    capability_count: i32 = 0,

    // Driver binding
    driver_id: i32 = -1, // device_driver_operator binding
    is_claimed: bool = false,

    // Label
    label: TextSmall = TextSmall.initEmpty(),

    // State
    is_present: bool = false,
    is_enabled: bool = false,
    has_error: bool = false,
    error_status: u32 = 0,
};

pub const PcieLinkSpeed = enum(i32) {
    None = -1,
    Gen1_2_5GT = 0, // 2.5 GT/s
    Gen2_5GT, // 5 GT/s
    Gen3_8GT, // 8 GT/s
    Gen4_16GT, // 16 GT/s
    Gen5_32GT, // 32 GT/s
    Gen6_64GT, // 64 GT/s
};

pub const MAX_PCI_DEVICES: usize = 256;

pub const PciDeviceTable = struct {
    devices: [MAX_PCI_DEVICES]PciDevice = [_]PciDevice{.{}} ** MAX_PCI_DEVICES,
    device_count: i32 = 0,

    // ECAM (Enhanced Configuration Access Mechanism) for PCIe
    ecam_base_phys: u64 = 0,
    ecam_base_virt: u64 = 0,
    ecam_bus_start: i32 = 0,
    ecam_bus_end: i32 = 0,

    // Legacy PCI config access
    config_address_port: u16 = 0xCF8,
    config_data_port: u16 = 0xCFC,
};

// ============================================================
// TIMER AND CLOCK
// ============================================================

pub const TimerSource = enum(i32) {
    None = -1,
    TSC = 0, // Time Stamp Counter (preferred)
    HPET, // High Precision Event Timer
    APIC, // Local APIC timer
    PIT, // Programmable Interval Timer (legacy, 8254)
    ACPI_PM, // ACPI Power Management Timer
};

pub const TimerMode = enum(i32) {
    OneShot = 0,
    Periodic,
    TSCDeadline, // TSC deadline mode (APIC)
};

pub const TimerDescriptor = struct {
    id: i32 = -1,
    source: TimerSource = .None,
    mode: TimerMode = .Periodic,

    // Configuration
    frequency_hz: u64 = 0,
    period_ns: u64 = 0,
    divisor: u32 = 0,

    // TSC
    tsc_frequency_hz: u64 = 0,
    tsc_at_boot: u64 = 0,
    tsc_is_invariant: bool = false,

    // HPET
    hpet_base_phys: u64 = 0,
    hpet_base_virt: u64 = 0,
    hpet_period_femtoseconds: u64 = 0,
    hpet_counter_size: i32 = 0, // 32 or 64 bit

    // APIC timer
    apic_initial_count: u32 = 0,
    apic_current_count: u32 = 0,
    apic_divide_config: u32 = 0,

    // PIT (legacy)
    pit_channel: i32 = 0,
    pit_reload_value: u16 = 0,

    // State
    is_active: bool = false,
    interrupt_vector: i32 = -1,

    // Calibration
    is_calibrated: bool = false,
    calibration_error_ppm: i32 = 0,
};

pub const TimerTable = struct {
    timers: [8]TimerDescriptor = [_]TimerDescriptor{.{}} ** 8,
    timer_count: i32 = 0,

    // Selected source for time_fixed.zig
    primary_source: TimerSource = .TSC,
    tsc_khz: u64 = 0,

    // Boot timestamp (TSC value at Silo start)
    boot_tsc: u64 = 0,
    boot_wall_ns: i128 = 0,
};

// ============================================================
// PORT IO
// ============================================================

pub const PortWidth = enum(i32) {
    Byte = 0, // 8-bit
    Word, // 16-bit
    Dword, // 32-bit
};

pub const PortIoRequest = struct {
    port: u16 = 0,
    width: PortWidth = .Byte,
    value: u32 = 0,
    is_write: bool = false,
};

// Well-known port ranges
pub const PortRanges = struct {
    pub const PCI_CONFIG_ADDR: u16 = 0xCF8;
    pub const PCI_CONFIG_DATA: u16 = 0xCFC;
    pub const PIT_CHANNEL_0: u16 = 0x40;
    pub const PIT_COMMAND: u16 = 0x43;
    pub const PS2_DATA: u16 = 0x60;
    pub const PS2_STATUS: u16 = 0x64;
    pub const RTC_ADDR: u16 = 0x70;
    pub const RTC_DATA: u16 = 0x71;
    pub const PIC1_CMD: u16 = 0x20;
    pub const PIC1_DATA: u16 = 0x21;
    pub const PIC2_CMD: u16 = 0xA0;
    pub const PIC2_DATA: u16 = 0xA1;
    pub const COM1: u16 = 0x3F8;
    pub const COM2: u16 = 0x2F8;
    pub const COM3: u16 = 0x3E8;
    pub const COM4: u16 = 0x2E8;
    pub const ACPI_PM_TMR: u16 = 0x408;
};

// ============================================================
// MMIO REGION MANAGEMENT
// ============================================================

pub const MmioRegion = struct {
    id: i32 = -1,

    // Physical location
    phys_base: u64 = 0,
    size_bytes: u64 = 0,

    // Mapping
    virt_base: u64 = 0,
    is_mapped: bool = false,

    // Cacheability
    cacheability: MemoryCacheability = .Uncacheable,

    // Owner
    device_id: i32 = -1, // PCI device
    bar_index: i32 = -1, // Which BAR this came from

    // Access control
    is_read_only: bool = false,
    requires_alignment: i32 = 0, // Minimum access alignment in bytes

    // Label
    label: TextSmall = TextSmall.initEmpty(),
};

pub const MAX_MMIO_REGIONS: usize = 128;

pub const MmioTable = struct {
    regions: [MAX_MMIO_REGIONS]MmioRegion = [_]MmioRegion{.{}} ** MAX_MMIO_REGIONS,
    count: i32 = 0,
};

// ============================================================
// CACHE AND TLB CONTROL
// ============================================================

pub const CacheOperation = enum(i32) {
    None = -1,

    // Per-address
    FlushLine = 0, // CLFLUSH: flush and invalidate
    FlushLineOpt, // CLFLUSHOPT: optimized flush
    WriteBackLine, // CLWB: write back without invalidate
    Prefetch, // PREFETCH: bring into cache
    PrefetchNTA, // PREFETCHNTA: non-temporal, skip cache levels
    PrefetchT0, // PREFETCHT0: to all levels
    PrefetchT1, // PREFETCHT1: to L2 and above
    PrefetchT2, // PREFETCHT2: to L3 and above

    // Whole-cache
    WriteBackAll, // WBINVD: write back and invalidate all
    InvalidateAll, // INVD: invalidate all (no writeback — dangerous)

    // Non-temporal store fence
    StoreFence, // SFENCE
    LoadFence, // LFENCE
    MemoryFence, // MFENCE

    // Write combining flush
    WriteCombiningFlush, // Flush write combining buffers
};

pub const CacheRequest = struct {
    operation: CacheOperation = .None,
    address: u64 = 0, // For per-address operations
    size_bytes: u64 = 0, // Range to operate on
    core_id: i32 = -1, // Which core (-1 = current)
};

pub const TlbOperation = enum(i32) {
    None = -1,
    FlushAll = 0, // Flush entire TLB
    FlushPage, // INVLPG: flush single page
    FlushRange, // Flush range of pages
    FlushASID, // Flush by address space ID
    FlushGlobal, // Flush including global entries
};

pub const TlbRequest = struct {
    operation: TlbOperation = .None,
    address: u64 = 0, // For page/range flush
    page_count: u64 = 0, // For range flush
    asid: u16 = 0, // For ASID flush
    core_id: i32 = -1, // Which core (-1 = current, -2 = all via IPI)
};

// ============================================================
// POWER MANAGEMENT
// ============================================================

pub const SystemPowerState = enum(i32) {
    S0_Working = 0, // Fully on
    S1_Standby, // CPU stopped, RAM refreshed
    S3_Suspend, // RAM retained, everything else off
    S4_Hibernate, // State saved to disk, power off
    S5_SoftOff, // Power off, PSU standby
    G3_MechOff, // No power at all
};

pub const PowerDomain = enum(i32) {
    None = -1,
    CPU = 0,
    Package,
    DRAM,
    GPU,
    Platform,
};

pub const PowerState = struct {
    // Current system state
    system_state: SystemPowerState = .S0_Working,

    // Per-domain power measurement (from RAPL on Intel, similar on AMD)
    cpu_power_mw: i32 = 0,
    package_power_mw: i32 = 0,
    dram_power_mw: i32 = 0,

    // Power limits
    tdp_mw: i32 = 0,
    pl1_mw: i32 = 0, // Long-term power limit
    pl2_mw: i32 = 0, // Short-term power limit (turbo)
    pl1_time_window_ms: i32 = 0,
    pl2_time_window_ms: i32 = 0,

    // Battery (if applicable — laptop Silo)
    has_battery: bool = false,
    battery_percent: i32 = 0,
    battery_charging: bool = false,
    battery_time_remaining_min: i32 = 0,
    battery_mwh_full: i32 = 0,
    battery_mwh_now: i32 = 0,

    // Thermal
    package_temp_celsius: i32 = 0,
    is_throttled: bool = false,
    throttle_reason: ThrottleReason = .None,
};

pub const ThrottleReason = enum(i32) {
    None = 0,
    Thermal, // TJ max reached
    PowerLimit, // PL1 or PL2 exceeded
    CurrentLimit, // Current draw too high
    VoltageLimit, // Voltage regulator limit
    ExternalPROCHOT, // External throttle signal
};

// ============================================================
// HARDWARE ERROR REPORTING
// ============================================================

pub const HardwareErrorSeverity = enum(i32) {
    None = -1,
    Corrected = 0, // Hardware corrected, no data loss
    Recoverable, // Software can recover
    Fatal, // System must halt
    Informational, // Advisory
};

pub const HardwareErrorSource = enum(i32) {
    None = -1,
    CPU = 0,
    Memory,
    PCIe,
    NVMe,
    Network,
    Thermal,
    Power,
    Platform,
};

pub const HardwareError = struct {
    id: i32 = -1,
    severity: HardwareErrorSeverity = .None,
    source: HardwareErrorSource = .None,

    // CPU machine check
    mce_bank: i32 = -1,
    mce_status: u64 = 0,
    mce_addr: u64 = 0,
    mce_misc: u64 = 0,

    // PCIe AER (Advanced Error Reporting)
    aer_uncorrectable_status: u32 = 0,
    aer_correctable_status: u32 = 0,
    aer_header_log: [4]u32 = [_]u32{0} ** 4,

    // Memory ECC
    ecc_syndrome: u32 = 0,
    ecc_row: i32 = -1,
    ecc_column: i32 = -1,
    ecc_bank: i32 = -1,
    ecc_rank: i32 = -1,
    ecc_dimm: i32 = -1,
    ecc_phys_addr: u64 = 0,

    // NVMe
    nvme_status_code: u16 = 0,
    nvme_status_type: u8 = 0,

    // Context
    core_id: i32 = -1,
    device_id: i32 = -1,
    timestamp_tsc: u64 = 0,
    error_count: u32 = 0,

    // Description
    message: Text = Text.initEmpty(),
};

pub const MAX_HARDWARE_ERRORS: usize = 256;

pub const HardwareErrorLog = struct {
    errors: [MAX_HARDWARE_ERRORS]HardwareError = [_]HardwareError{.{}} ** MAX_HARDWARE_ERRORS,
    write_index: i32 = 0,
    total_count: u64 = 0,
    corrected_count: u64 = 0,
    fatal_count: u64 = 0,

    // MCE state
    mce_enabled: bool = false,
    mce_bank_count: i32 = 0,
    last_mce_tsc: u64 = 0,
};

// ============================================================
// ACPI TABLES
// ============================================================

pub const AcpiTableType = enum(i32) {
    None = -1,
    RSDP = 0,
    RSDT,
    XSDT,
    MADT, // Multiple APIC Description Table
    FADT, // Fixed ACPI Description Table
    HPET, // High Precision Event Timer
    MCFG, // PCI Express ECAM
    SRAT, // System Resource Affinity Table (NUMA)
    SLIT, // System Locality Information Table (NUMA distances)
    DMAR, // DMA Remapping (Intel VT-d)
    IVRS, // IO Virtualization Reporting Structure (AMD-Vi)
    BGRT, // Boot Graphics Resource Table
    BERT, // Boot Error Record Table
    EINJ, // Error Injection
    ERST, // Error Record Serialization
    WAET, // Windows ACPI Emulated Timer (useful even on non-Windows)
};

pub const AcpiTableRef = struct {
    table_type: AcpiTableType = .None,
    phys_addr: u64 = 0,
    virt_addr: u64 = 0,
    length: u32 = 0,
    revision: u8 = 0,
    is_valid: bool = false,
    checksum_ok: bool = false,
};

pub const MAX_ACPI_TABLES: usize = 32;

pub const AcpiTables = struct {
    tables: [MAX_ACPI_TABLES]AcpiTableRef = [_]AcpiTableRef{.{}} ** MAX_ACPI_TABLES,
    table_count: i32 = 0,

    // RSDP location
    rsdp_phys: u64 = 0,
    acpi_revision: u8 = 0, // 0 = ACPI 1.0, 2+ = ACPI 2.0+
    is_xsdt: bool = false, // Use 64-bit XSDT vs 32-bit RSDT

    // FADT power management
    pm_timer_port: u16 = 0,
    pm1a_evt_port: u16 = 0,
    pm1b_evt_port: u16 = 0,
    pm1a_cnt_port: u16 = 0,
    pm1b_cnt_port: u16 = 0,
    slp_typa_s5: u8 = 0,
    slp_typb_s5: u8 = 0,
    sci_interrupt: u16 = 0,
    century_register: u8 = 0,

    // SRAT NUMA
    numa_node_count: i32 = 0,
    numa_distances: [16 * 16]u8 = [_]u8{0} ** (16 * 16), // 16x16 SLIT matrix
};

// ============================================================
// DISPLAY / FRAMEBUFFER
// ============================================================

pub const PixelFormat = enum(i32) {
    Unknown = -1,
    RGB888 = 0, // 24-bit RGB, no alpha
    BGRA8888, // 32-bit BGRA (most common for UEFI/GOP)
    RGBA8888, // 32-bit RGBA
    BGR888, // 24-bit BGR
    RGB565, // 16-bit packed
};

pub const FrameBufferInfo = struct {
    phys_base: u64 = 0,
    virt_base: u64 = 0,
    size_bytes: u64 = 0,

    width: i32 = 0,
    height: i32 = 0,
    pitch: i32 = 0, // Bytes per scanline (may include padding)
    bpp: i32 = 32, // Bits per pixel
    pixel_format: PixelFormat = .BGRA8888,

    // Double buffering
    front_buffer_offset: u64 = 0,
    back_buffer_offset: u64 = 0,
    is_double_buffered: bool = false,

    // Vsync
    refresh_rate_hz: i32 = 60,
    vsync_enabled: bool = true,
    frames_presented: u64 = 0,
    last_vsync_tsc: u64 = 0,

    // Mode setting
    is_mode_set: bool = false,
    requested_width: i32 = 1920,
    requested_height: i32 = 1080,
    requested_refresh: i32 = 60,
};

// ============================================================
// INPUT DEVICES (raw, pre-driver)
// ============================================================

pub const RawInputType = enum(i32) {
    None = -1,
    PS2Keyboard = 0,
    PS2Mouse,
    USBKeyboard,
    USBMouse,
    USBGamepad,
    USBTablet, // Absolute positioning (touchscreen, wacom)
};

pub const RawInputEvent = struct {
    input_type: RawInputType = .None,
    timestamp_tsc: u64 = 0,

    // Keyboard
    scancode: u16 = 0,
    is_keydown: bool = false,
    is_extended: bool = false,

    // Mouse
    mouse_dx: i16 = 0,
    mouse_dy: i16 = 0,
    mouse_dz: i16 = 0, // Scroll wheel
    mouse_buttons: u8 = 0, // Bitmask: bit0=left, bit1=right, bit2=middle

    // Gamepad
    gamepad_id: i32 = -1,
    gamepad_axis: [8]i16 = [_]i16{0} ** 8,
    gamepad_buttons: u32 = 0,

    // Tablet (absolute)
    tablet_x: i32 = 0,
    tablet_y: i32 = 0,
    tablet_pressure: u16 = 0,
};

pub const RAW_INPUT_BUFFER_SIZE: usize = 256;

pub const RawInputBuffer = struct {
    events: [RAW_INPUT_BUFFER_SIZE]RawInputEvent = [_]RawInputEvent{.{}} ** RAW_INPUT_BUFFER_SIZE,
    write_index: u32 = 0,
    read_index: u32 = 0,
    overflow_count: u64 = 0,
};

// ============================================================
// HARDWARE OPERATION — one action on hardware
// ============================================================

pub const HwOpType = enum(i32) {
    None = -1,

    // Core operations
    CoreEnable = 0,
    CoreDisable,
    CoreSetRole,
    CoreSetPowerState,
    CoreSendIPI,
    CoreReadTSC,
    CoreHalt,
    CoreEnableInterrupts,
    CoreDisableInterrupts,

    // MSR operations
    MsrRead = 100,
    MsrWrite,

    // CPUID
    CpuidQuery = 150,

    // Interrupt operations
    InterruptEnable = 200,
    InterruptDisable,
    InterruptSetVector,
    InterruptSetHandler,
    InterruptSendEOI,
    InterruptSetPriority,
    IoApicSetRedirection,

    // Memory operations
    MemoryMapRegion = 300,
    MemoryUnmapRegion,
    MemorySetCacheability,
    MemoryAllocateDMA,
    MemoryFreeDMA,
    MemoryFence,

    // DMA operations
    DmaStart = 400,
    DmaStop,
    DmaSync,
    DmaSetRingHead,
    DmaSetRingTail,
    DmaReset,

    // PCI operations
    PciConfigRead = 500,
    PciConfigWrite,
    PciEnableDevice,
    PciDisableDevice,
    PciEnableBusMaster,
    PciDisableBusMaster,
    PciEnableMSI,
    PciDisableMSI,
    PciEnableMSIX,
    PciDisableMSIX,
    PciSetPowerState,
    PciBarMap,
    PciBarUnmap,
    PciScanBus,

    // Timer operations
    TimerStart = 600,
    TimerStop,
    TimerSetFrequency,
    TimerSetMode,
    TimerCalibrate,
    TimerReadCounter,

    // Port IO
    PortRead = 700,
    PortWrite,

    // MMIO
    MmioRead8 = 800,
    MmioRead16,
    MmioRead32,
    MmioRead64,
    MmioWrite8,
    MmioWrite16,
    MmioWrite32,
    MmioWrite64,

    // Cache and TLB
    CacheFlush = 900,
    CacheInvalidate,
    CacheWriteBack,
    CachePrefetch,
    TlbFlush,
    TlbFlushPage,

    // Power
    PowerSetState = 1000,
    PowerReadRAPL,
    PowerSetTurbo,
    PowerSetPowerLimit,
    PowerReadBattery,
    PowerShutdown,
    PowerReboot,

    // Error handling
    ErrorReadMCE = 1100,
    ErrorClearMCE,
    ErrorReadAER,
    ErrorClearAER,
    ErrorInject,

    // Framebuffer
    FBSetMode = 1200,
    FBSwapBuffers,
    FBSetVsync,
    FBPresent,

    // Input
    InputPollPS2 = 1300,
    InputResetPS2,
    InputSetLEDs,

    // ACPI
    AcpiParseTable = 1400,
    AcpiEnable,
    AcpiDisable,
    AcpiSleep,
    AcpiWake,

    // IOMMU
    IommuEnable = 1500,
    IommuDisable,
    IommuMapDevice,
    IommuUnmapDevice,
    IommuFlush,
};

pub const HardwareOperation = struct {
    id: i32 = -1,
    op: HwOpType = .None,

    // Target identification
    core_id: i32 = -1,
    device_id: i32 = -1, // PCI device index
    vector: i32 = -1, // Interrupt vector
    region_id: i32 = -1, // Memory/MMIO region
    dma_id: i32 = -1, // DMA descriptor
    timer_id: i32 = -1, // Timer
    bar_index: i32 = -1, // PCI BAR

    // Values (by operation)
    value_u8: u8 = 0,
    value_u16: u16 = 0,
    value_u32: u32 = 0,
    value_u64: u64 = 0,
    value_i32: i32 = 0,
    value_bool: bool = false,

    // Address (for port IO, MMIO, memory mapping)
    address: u64 = 0,
    size: u64 = 0,

    // MSR
    msr_address: u32 = 0,

    // Port IO
    port: u16 = 0,
    port_width: PortWidth = .Byte,

    // Memory
    cacheability: MemoryCacheability = .WriteBack,
    dma_direction: DmaDirection = .None,
    dma_purpose: DmaPurpose = .None,

    // Interrupt
    delivery_mode: InterruptDeliveryMode = .Fixed,
    trigger_mode: InterruptTriggerMode = .Edge,
    polarity: InterruptPolarity = .ActiveHigh,
    handler_address: u64 = 0,
    ist_index: i32 = 0,

    // Power
    power_state: PciPowerState = .D0,
    core_power_state: CorePowerState = .Active,
    system_power_state: SystemPowerState = .S0_Working,

    // Framebuffer
    fb_width: i32 = 0,
    fb_height: i32 = 0,
    fb_refresh: i32 = 60,

    // PCI config
    config_offset: u16 = 0,

    // Role assignment
    core_role: CoreRole = .None,

    // Timer
    timer_source: TimerSource = .None,
    timer_mode: TimerMode = .Periodic,
    timer_frequency_hz: u64 = 0,

    // Cache/TLB
    cache_op: CacheOperation = .None,
    tlb_op: TlbOperation = .None,
    page_count: u64 = 0,

    // IOMMU
    iommu_domain: i32 = -1,

    // Result (written by executor)
    result_u64: u64 = 0,
    result_bool: bool = false,
    result_error: HardwareErrorSeverity = .None,
    result_message: TextSmall = TextSmall.initEmpty(),

    is_deleted: bool = false,
};

pub const HardwareOperationSet = struct {
    id: i32 = -1,
    name: Text = Text.initEmpty(),

    operations: []HardwareOperation = &.{},
    stop_on_error: bool = true,

    is_deleted: bool = false,
};

// ============================================================
// HARDWARE STATE — complete machine snapshot
// ============================================================

pub const HardwareState = struct {
    // CPU
    cpu_features: CpuFeatures = .{},
    cores: CoreTable = .{},

    // Interrupts
    interrupts: InterruptTable = .{},
    io_apics: IoApicTable = .{},

    // Memory
    memory_map: PhysicalMemoryMap = .{},
    mmio: MmioTable = .{},

    // DMA
    dma: DmaTable = .{},

    // PCI/PCIe
    pci: PciDeviceTable = .{},

    // Timers
    timers: TimerTable = .{},

    // Power
    power: PowerState = .{},

    // Errors
    errors: HardwareErrorLog = .{},

    // ACPI
    acpi: AcpiTables = .{},

    // Display
    framebuffer: FrameBufferInfo = .{},

    // Input
    input: RawInputBuffer = .{},

    // Boot state
    boot_complete: bool = false,
    boot_time_ms: i32 = 0,
    uptime_seconds: u64 = 0,
};

// ============================================================
// HARDWARE MONITOR — runtime diagnostics
// ============================================================

pub const HardwareMonitor = struct {
    // Per-core stats
    core_temperatures: [MAX_CORES]i32 = [_]i32{0} ** MAX_CORES,
    core_frequencies: [MAX_CORES]i32 = [_]i32{0} ** MAX_CORES,
    core_utilizations: [MAX_CORES]i32 = [_]i32{0} ** MAX_CORES,

    // Memory
    total_ram_mb: i32 = 0,
    used_ram_mb: i32 = 0,
    arena_used_mb: i32 = 0,
    memdb_used_mb: i32 = 0,

    // DMA throughput
    nic_rx_bytes_per_sec: u64 = 0,
    nic_tx_bytes_per_sec: u64 = 0,
    nvme_read_bytes_per_sec: u64 = 0,
    nvme_write_bytes_per_sec: u64 = 0,

    // PCIe
    pcie_errors: u32 = 0,

    // Power
    package_power_mw: i32 = 0,
    dram_power_mw: i32 = 0,
    total_power_mw: i32 = 0,

    // Thermal
    max_core_temp: i32 = 0,
    is_throttled: bool = false,

    // Errors
    corrected_errors_total: u64 = 0,
    uncorrected_errors_total: u64 = 0,

    // Uptime
    uptime_seconds: u64 = 0,
    frames_total: u64 = 0,

    // Interrupt stats
    interrupts_per_second: u64 = 0,
    ipi_per_second: u64 = 0,

    // Sample interval
    last_sample_tsc: u64 = 0,
};
