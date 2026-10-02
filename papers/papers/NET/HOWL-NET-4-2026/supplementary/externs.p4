/*
 * IPv4-64 Extern Declarations
 * HOWL-NET-3-2026 Reference Implementation
 *
 * These externs are provided by the target platform.
 * The declarations define the interface. The implementation
 * is hardware-specific (DPA cores, MPUs, FPGA blocks, or ARM).
 */

#ifndef _EXTERNS_P4_
#define _EXTERNS_P4_

// HMAC-SHA256 computation
// Returns truncated 32-bit or 56-bit result depending on use
extern void hmac_sha256_32(
    in  bit<128> key,
    in  bit<96>  data,      // src_addr_64 (64) ++ epoch (32)
    out bit<32>  result
);

// HMAC-SHA256 for Retry Cookie (56-bit truncation)
extern void hmac_sha256_56(
    in  bit<128> key,
    in  bit<128> data,      // src_addr_64 ++ src_port ++ dst_port ++ timestamp
    out bit<56>  result
);

// SipHash-2-4 computation for Fragment Token
extern void siphash_2_4(
    in  bit<64>  key,
    in  bit<144> data,      // identification (16) ++ src_addr_64 (64) ++ dst_addr_64 (64)
    out bit<16>  result
);

// CRC32 hash for ECMP and LAG selection
extern void hash_crc32(
    in  bit<192> data,      // src_addr_64 ++ dst_addr_64 ++ flow_label ++ proto ++ ports
    out bit<32>  result
);

// Two-rate three-color meter (RFC 2698)
extern void meter_execute(
    in  bit<32> meter_id,
    out bit<2>  color       // 0=green, 1=yellow, 2=red
);

// Single-rate two-color meter
extern void meter_execute_simple(
    in  bit<32> meter_id,
    out bit<2>  color       // 0=green, 2=red
);

// Counter increment
extern void counter_increment(
    in bit<32> counter_id,
    in bit<32> increment_value
);

// IPv4 header checksum computation (for egress conversion)
extern void ipv4_checksum_compute(
    in  ipv4_legacy_h hdr,
    out bit<16>        result
);

// TCP checksum computation over IPv4-64 pseudo-header
extern void tcp_checksum_ipv4_64(
    in  bit<64>  src_addr,
    in  bit<64>  dst_addr,
    in  bit<8>   protocol,
    in  bit<16>  segment_length,
    in  tcp_64_h tcp_hdr,
    out bit<16>  result
);

// TCP checksum computation over IPv4 legacy pseudo-header
extern void tcp_checksum_ipv4(
    in  bit<32>       src_addr,
    in  bit<32>       dst_addr,
    in  bit<8>        protocol,
    in  bit<16>       segment_length,
    in  tcp_legacy_h  tcp_hdr,
    out bit<16>       result
);

// UDP checksum computation over IPv4-64 pseudo-header
extern void udp_checksum_ipv4_64(
    in  bit<64>  src_addr,
    in  bit<64>  dst_addr,
    in  bit<8>   protocol,
    in  bit<16>  segment_length,
    in  udp_64_h udp_hdr,
    out bit<16>  result
);

// UDP checksum computation over IPv4 legacy pseudo-header
extern void udp_checksum_ipv4(
    in  bit<32>       src_addr,
    in  bit<32>       dst_addr,
    in  bit<8>        protocol,
    in  bit<16>       segment_length,
    in  udp_legacy_h  udp_hdr,
    out bit<16>       result
);

// SVT key store — holds current and previous epoch secrets
// Populated by control plane
extern void svt_get_key(
    in  bit<1>   epoch_index,   // 0 = current, 1 = previous
    out bit<128> key,
    out bit<32>  epoch_counter
);

// Retry Cookie server secret
extern void cookie_get_secret(
    out bit<128> key,
    out bit<32>  timestamp_window
);

// Fragment connection secret
extern void fragment_get_secret(
    out bit<64> key
);

#endif
