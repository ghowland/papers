/*
 * IPv4-64 Internal Metadata
 * HOWL-NET-3-2026 Reference Implementation
 */

#ifndef _METADATA_P4_
#define _METADATA_P4_

struct metadata_t {
    // Concatenated 64-bit addresses for table lookups
    bit<64> src_addr_64;
    bit<64> dst_addr_64;

    // Drop control
    bit<8>  drop_reason;
    bool    do_drop;

    // Packet identification
    bit<8>  parsed_protocol;
    bool    has_tcp;
    bool    has_udp;
    bool    has_icmp;

    // Fragment state
    bool    is_fragment;
    bool    is_first_fragment;

    // SVT verification result
    bool    svt_valid;
    bit<32> egress_svt;

    // Cookie verification result
    bool    cookie_valid;
    bit<3>  cookie_mss_index;
    bit<4>  cookie_window_scale;
    bit<1>  cookie_sack_ok;

    // Classification results
    bit<2>  conn_class;
    bit<4>  traffic_class;
    bit<3>  threat_level;

    // Firewall result
    bool    fw_permit;
    bit<32> fw_meter_id;
    bool    fw_log;

    // Routing result
    bit<16> next_hop_id;
    bit<16> ecmp_group_id;
    bool    use_ecmp;
    bit<9>  egress_port;
    bit<48> next_hop_dst_mac;
    bit<48> next_hop_src_mac;

    // QoS result
    bit<6>  new_dscp;

    // Meter result
    bit<2>  meter_color;

    // Edge conversion
    bool    converted_from_ipv4;
    bool    convert_to_ipv4_on_egress;
    bit<4>  original_ihl;
    bit<16> original_tcp_data_offset;
    bool    legacy_had_sack_permitted;
    bool    legacy_had_window_scale;
    bit<8>  legacy_window_scale_value;
    bit<16> legacy_mss_value;
    bool    legacy_had_mss;

    // Port configuration
    bit<1>  ingress_port_type;
    bit<1>  egress_port_type;

    // Ingress metadata from hardware
    bit<9>  ingress_port;
    bit<48> ingress_timestamp;
    bit<16> packet_length;

    // Hash for ECMP/LAG
    bit<32> flow_hash;
}

#endif
