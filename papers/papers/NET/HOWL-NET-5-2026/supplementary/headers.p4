/*
 * IPv4-64 Header Definitions
 * HOWL-NET-3-2026 Reference Implementation
 */

#ifndef _HEADERS_P4_
#define _HEADERS_P4_

// Ethernet
header ethernet_h {
    bit<48> dst_mac;
    bit<48> src_mac;
    bit<16> ether_type;
}

// IPv4-64 IP header — 32 bytes fixed
header ipv4_64_h {
    bit<4>  version;
    bit<6>  dscp;
    bit<2>  ecn;
    bit<4>  flags;
    bit<16> payload_length;
    bit<20> flow_label;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> identification;
    bit<16> fragment_token;
    bit<8>  fragment_offset;
    bit<32> svt;
    bit<32> src_addr_upper;
    bit<32> src_addr_lower;
    bit<32> dst_addr_upper;
    bit<32> dst_addr_lower;
}

// IPv4-64 TCP header — 24 bytes fixed
header tcp_64_h {
    bit<16> src_port;
    bit<16> dst_port;
    bit<32> seq_num;
    bit<32> ack_num;
    bit<16> flags;
    bit<16> window_size;
    bit<16> checksum;
    bit<64> retry_cookie;
}

// IPv4-64 UDP header — 10 bytes fixed
header udp_64_h {
    bit<16> src_port;
    bit<16> dst_port;
    bit<16> length;
    bit<16> checksum;
    bit<8>  udp_flags;
    bit<8>  reserved;
}

// ICMP header — 8 bytes
header icmp_h {
    bit<8>  msg_type;
    bit<8>  code;
    bit<16> checksum;
    bit<32> body;
}

// IPv4 legacy IP header — 20 bytes minimum
header ipv4_legacy_h {
    bit<4>  version;
    bit<4>  ihl;
    bit<6>  dscp;
    bit<2>  ecn;
    bit<16> total_length;
    bit<16> identification;
    bit<3>  flags;
    bit<13> fragment_offset;
    bit<8>  ttl;
    bit<8>  protocol;
    bit<16> header_checksum;
    bit<32> src_addr;
    bit<32> dst_addr;
}

// IPv4 legacy options — up to 40 bytes
// Extracted as raw bytes, not parsed field by field
header ipv4_options_h {
    varbit<320> data;
}

// IPv4 legacy TCP header — 20 bytes minimum
header tcp_legacy_h {
    bit<16> src_port;
    bit<16> dst_port;
    bit<32> seq_num;
    bit<32> ack_num;
    bit<4>  data_offset;
    bit<4>  legacy_reserved;
    bit<8>  flags;
    bit<16> window_size;
    bit<16> checksum;
    bit<16> urgent_ptr;
}

// IPv4 legacy TCP options — up to 40 bytes
header tcp_options_h {
    varbit<320> data;
}

// IPv4 legacy UDP header — 8 bytes fixed
header udp_legacy_h {
    bit<16> src_port;
    bit<16> dst_port;
    bit<16> length;
    bit<16> checksum;
}

// Collected headers struct
struct headers_t {
    ethernet_h      ethernet;
    ipv4_64_h       ipv4_64;
    tcp_64_h        tcp_64;
    udp_64_h        udp_64;
    icmp_h          icmp;
    ipv4_legacy_h   ipv4_legacy;
    ipv4_options_h  ipv4_options;
    tcp_legacy_h    tcp_legacy;
    tcp_options_h   tcp_options;
    udp_legacy_h    udp_legacy;
}

// Ethertype for IPv4-64 — TBD, using experimental range
const bit<16> ETHERTYPE_IPV4_64 = 0x0864;
const bit<16> ETHERTYPE_IPV4    = 0x0800;

#endif
