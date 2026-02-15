//TODO: Add for every scene, they manage their own network packets, can inspect their own network packets
// - A master Network scene will exist, registered to tall infro for incoming DMA drops, and will write into other scene's network packets to update them, so they are VM-like and have full insight

// Network packet structures for Silo OS

// Inbound packet from network device
pub const InboundPacket = struct {
    // Lifecycle
    is_active: bool = false,
    time_received: f32 = 0,

    // Layer 2 (Ethernet)
    src_mac: [6]u8 = [_]u8{0} ** 6,
    dst_mac: [6]u8 = [_]u8{0} ** 6,
    ethertype: u16 = 0,

    // Layer 3 (IP)
    src_ip: u32 = 0,
    dst_ip: u32 = 0,
    protocol: u8 = 0, // TCP=6, UDP=17, ICMP=1
    ttl: u8 = 0,

    // Layer 4 (TCP/UDP)
    src_port: u16 = 0,
    dst_port: u16 = 0,

    // TCP specific
    tcp_seq: u32 = 0,
    tcp_ack: u32 = 0,
    tcp_flags: u8 = 0,
    tcp_window: u16 = 0,

    // Payload
    payload_data: [2048]u8 = [_]u8{0} ** 2048,
    payload_length: u16 = 0,

    // Metadata
    checksum_valid: bool = false,
    fragmented: bool = false,
    owner_scene_id: i32 = -1, // Which scene should process this
};

// Outbound packet to network device
pub const OutboundPacket = struct {
    // Lifecycle
    is_active: bool = false,
    time_queued: f32 = 0,

    // Destination (scene fills these)
    dst_ip: u32 = 0,
    dst_port: u16 = 0,
    protocol: u8 = 6, // Default TCP

    // Source (infrastructure fills these)
    src_ip: u32 = 0,
    src_port: u16 = 0,
    src_mac: [6]u8 = [_]u8{0} ** 6,
    dst_mac: [6]u8 = [_]u8{0} ** 6,

    // TCP specific (scene can set)
    tcp_flags: u8 = 0,
    tcp_seq: u32 = 0,
    tcp_ack: u32 = 0,

    // Payload (scene writes)
    payload_data: [2048]u8 = [_]u8{0} ** 2048,
    payload_length: u16 = 0,

    // Options (scene can configure)
    add_checksum: bool = true,
    ttl: u8 = 64,
    fragment_ok: bool = true,

    // Metadata (infrastructure uses)
    transmit_attempts: u8 = 0,
    last_transmit_time: f32 = 0,
};

// Per-scene network buffers - Each Game
pub const SceneNetworkBuffers = struct {
    // If false, this is not processed.  Can be used for other purposes
    is_active: bool = true,

    // Inbound packets delivered to this scene
    inbound: [1000]InboundPacket = [_]InboundPacket{.{}} ** 1000,

    // Outbound packets queued for transmission
    outbound: [1000]OutboundPacket = [_]OutboundPacket{.{}} ** 1000,

    // Statistics
    inbound_count: u32 = 0,
    outbound_count: u32 = 0,
    inbound_dropped: u32 = 0,
    outbound_dropped: u32 = 0,
};

// Network scene (system scene) global packet buffers - Global System
pub const NetworkSceneBuffers = struct {
    // Raw packets from NIC (before routing to scenes)
    rx_raw: [64]InboundPacket = [_]InboundPacket{.{}} ** 64,

    // Packets ready to transmit to NIC
    tx_ready: [64]OutboundPacket = [_]OutboundPacket{.{}} ** 64,

    // Statistics
    total_rx: u64 = 0,
    total_tx: u64 = 0,
    rx_errors: u32 = 0,
    tx_errors: u32 = 0,
};

// TCP connection state (for stateful protocols)
pub const TCPConnection = struct {
    // Identity
    local_port: u16 = 0,
    remote_ip: u32 = 0,
    remote_port: u16 = 0,

    // State
    state: TCPState = .Closed,

    // Sequence tracking
    send_seq: u32 = 0,
    recv_seq: u32 = 0,
    send_ack: u32 = 0,
    recv_ack: u32 = 0,

    // Window
    send_window: u16 = 65535,
    recv_window: u16 = 65535,

    // Buffers (fixed size, no allocation)
    send_buffer: [8192]u8 = [_]u8{0} ** 8192,
    recv_buffer: [8192]u8 = [_]u8{0} ** 8192,
    send_head: u16 = 0,
    send_tail: u16 = 0,
    recv_head: u16 = 0,
    recv_tail: u16 = 0,

    // Metadata
    is_active: bool = false,
    owner_scene_id: i32 = -1,
    last_activity: f32 = 0,
    retransmit_timeout: f32 = 1.0,
};

pub const TCPState = enum {
    Closed,
    Listen,
    SynSent,
    SynReceived,
    Established,
    FinWait1,
    FinWait2,
    CloseWait,
    Closing,
    LastAck,
    TimeWait,
};

// UDP socket (simpler than TCP)
pub const UDPSocket = struct {
    // Identity
    local_port: u16 = 0,

    // State
    is_active: bool = false,
    owner_scene_id: i32 = -1,

    // Statistics
    packets_sent: u32 = 0,
    packets_received: u32 = 0,
};

// Network scene TCP/UDP tables
pub const NetworkConnectionTables = struct {
    // TCP connections (stateful)
    tcp_connections: [256]TCPConnection = [_]TCPConnection{.{}} ** 256,

    // UDP sockets (stateless)
    udp_sockets: [64]UDPSocket = [_]UDPSocket{.{}} ** 64,
};
