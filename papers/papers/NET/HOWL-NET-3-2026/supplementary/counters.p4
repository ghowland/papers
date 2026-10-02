/*
 * IPv4-64 Counter and Meter Definitions
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Counters are read by the telemetry agent on the ARM cores.
 * Meters are configured by the control plane and applied
 * by the transform phase.
 */

#ifndef _COUNTERS_P4_
#define _COUNTERS_P4_

// ─── Packet and byte counters ───

// Per egress port: bytes and packets
counter(512, CounterType.bytes_and_packets) ctr_per_port;

// Per traffic class: packets
counter(16, CounterType.packets) ctr_per_class;

// Per drop reason: packets
counter(256, CounterType.packets) ctr_per_drop_reason;

// Per route prefix: bytes
// Indexed by route table entry index, not by prefix value.
// The control plane maps entry index to prefix.
counter(524288, CounterType.bytes) ctr_per_prefix;

// Per source prefix: SYN packets (for flood detection)
// Indexed by a hash of the source prefix.
counter(65536, CounterType.packets) ctr_per_source_syn;

// ─── Authentication counters (global) ───

counter(1, CounterType.packets) ctr_svt_pass;
counter(1, CounterType.packets) ctr_svt_fail;
counter(1, CounterType.packets) ctr_cookie_pass;
counter(1, CounterType.packets) ctr_cookie_fail;

// ─── Edge conversion counters (global) ───

counter(1, CounterType.packets) ctr_ipv4_ingress_converted;
counter(1, CounterType.packets) ctr_ipv4_ingress_dropped;
counter(1, CounterType.packets) ctr_ipv4_options_stripped;
counter(1, CounterType.packets) ctr_ipv4_egress_converted;
counter(1, CounterType.packets) ctr_ipv4_egress_ext_dropped;
counter(1, CounterType.packets) ctr_frag_offset_unaligned;
counter(1, CounterType.packets) ctr_udp_zero_cksum_computed;

// ─── Meters ───

// Firewall rate-limit meter (two-rate three-color)
// Indexed by meter_id from firewall_policy action.
meter(16384, MeterType.bytes) meter_firewall;

// UDP unvalidated meter (single-rate two-color)
// Single global meter for all unvalidated UDP traffic.
// In production, may be per-source-prefix.
meter(1, MeterType.bytes) meter_udp_unvalidated;

// SYN rate meter (single-rate two-color)
// Per source prefix, indexed by syn_rate_limit table.
meter(4096, MeterType.packets) meter_syn_rate;

// ─── Helper actions for counter updates ───
// Called from transform phase after all decisions are final.

action update_counters_permit() {
    ctr_per_port.count((bit<32>)std_meta.egress_spec);
    ctr_per_class.count((bit<32>)meta.traffic_class);
}

action update_counters_drop() {
    ctr_per_drop_reason.count((bit<32>)meta.drop_reason);
}

action update_counters_svt_pass() {
    ctr_svt_pass.count(0);
}

action update_counters_svt_fail() {
    ctr_svt_fail.count(0);
}

action update_counters_cookie_pass() {
    ctr_cookie_pass.count(0);
}

action update_counters_cookie_fail() {
    ctr_cookie_fail.count(0);
}

action update_counters_ipv4_ingress() {
    ctr_ipv4_ingress_converted.count(0);
}

action update_counters_ipv4_options() {
    ctr_ipv4_options_stripped.count(0);
}

action update_counters_ipv4_egress() {
    ctr_ipv4_egress_converted.count(0);
}

action update_counters_ipv4_egress_ext_drop() {
    ctr_ipv4_egress_ext_dropped.count(0);
}

action update_counters_frag_unaligned() {
    ctr_frag_offset_unaligned.count(0);
}

action update_counters_udp_zero_cksum() {
    ctr_udp_zero_cksum_computed.count(0);
}

#endif
