/*
 * IPv4-64 Phase 4: Classify
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Four classification stages:
 *   4a: Connection state
 *   4b: Traffic type
 *   4c: Threat level
 *   4d: Firewall policy
 */

#ifndef _CLASSIFY_P4_
#define _CLASSIFY_P4_

control Classify(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    // ─── 4a: Connection state table ───
    // Bloom filter or exact match on 5-tuple.
    // Populated by transform phase on cookie validation.
    // Garbage-collected by ARM control plane.

    action set_conn_established() {
        meta.conn_class = CONN_ESTABLISHED;
    }

    action set_conn_new() {
        meta.conn_class = CONN_NEW;
    }

    action set_conn_unknown() {
        meta.conn_class = CONN_UNKNOWN;
    }

    table connection_class {
        key = {
            meta.src_addr_64    : exact;
            meta.dst_addr_64    : exact;
            hdr.tcp_64.src_port : exact;
            hdr.tcp_64.dst_port : exact;
            meta.parsed_protocol: exact;
        }
        actions = {
            set_conn_established;
            set_conn_new;
            set_conn_unknown;
        }
        default_action = set_conn_unknown();
        size = 1048576;   // 1M entries, configurable
    }

    // UDP connection class uses same table structure
    // but keyed on UDP ports when TCP is not present
    table connection_class_udp {
        key = {
            meta.src_addr_64     : exact;
            meta.dst_addr_64     : exact;
            hdr.udp_64.src_port  : exact;
            hdr.udp_64.dst_port  : exact;
            meta.parsed_protocol : exact;
        }
        actions = {
            set_conn_established;
            set_conn_new;
            set_conn_unknown;
        }
        default_action = set_conn_unknown();
        size = 262144;    // 256K entries
    }

    // ─── 4b: Traffic type table ───
    // Classifies by destination port and protocol.
    // Populated by operator QoS configuration.

    action set_traffic_class(bit<4> tclass) {
        meta.traffic_class = tclass;
    }

    table traffic_class {
        key = {
            meta.parsed_protocol : exact;
            meta.dst_port_merged : exact;
        }
        actions = {
            set_traffic_class;
        }
        default_action = set_traffic_class(TCLASS_UNCLASSIFIED);
        size = 4096;
    }

    // ─── 4d: Firewall policy table ───
    // Central security policy. Every packet hits this table.
    // Ternary match maps directly to TCAM hardware.

    action fw_permit() {
        meta.fw_permit = true;
        meta.fw_log = false;
    }

    action fw_deny() {
        meta.do_drop = true;
        meta.drop_reason = DROP_FIREWALL_DENY;
        meta.fw_permit = false;
        meta.fw_log = false;
    }

    action fw_rate_limit(bit<32> meter_id) {
        meta.fw_permit = true;
        meta.fw_meter_id = meter_id;
        meta.fw_log = false;
    }

    action fw_permit_log() {
        meta.fw_permit = true;
        meta.fw_log = true;
    }

    action fw_deny_log() {
        meta.do_drop = true;
        meta.drop_reason = DROP_FIREWALL_DENY;
        meta.fw_permit = false;
        meta.fw_log = true;
    }

    action fw_redirect(bit<9> port) {
        meta.fw_permit = true;
        meta.egress_port = port;
        meta.fw_log = false;
    }

    table firewall_policy {
        key = {
            meta.src_addr_64     : ternary;
            meta.dst_addr_64     : ternary;
            meta.src_port_merged : range;
            meta.dst_port_merged : range;
            meta.parsed_protocol : exact;
            meta.conn_class      : exact;
            meta.threat_level    : exact;
        }
        actions = {
            fw_permit;
            fw_deny;
            fw_rate_limit;
            fw_permit_log;
            fw_deny_log;
            fw_redirect;
        }
        default_action = fw_deny();
        size = 16384;     // 16K rules, configurable
    }

    // ─── SYN rate meter ───
    // Applied to NEW connections per source prefix.

    action syn_meter_check(bit<32> meter_id) {
        bit<2> color;
        meter_execute_simple(meter_id, color);
        if (color == METER_RED) {
            meta.do_drop = true;
            meta.drop_reason = DROP_RATE_EXCEEDED;
        }
    }

    table syn_rate_limit {
        key = {
            meta.src_addr_64 : lpm;
        }
        actions = {
            syn_meter_check;
            NoAction;
        }
        default_action = NoAction();
        size = 4096;
    }

    apply {
        if (meta.do_drop) { return; }
        if (!hdr.ipv4_64.isValid()) { return; }

        // ─── Merge port fields for table lookups ───
        // TCP and UDP ports occupy different headers but
        // classification and firewall use a single port field.

        bit<16> src_port_val = 0;
        bit<16> dst_port_val = 0;

        if (meta.has_tcp && hdr.tcp_64.isValid()) {
            src_port_val = hdr.tcp_64.src_port;
            dst_port_val = hdr.tcp_64.dst_port;
        } else if (meta.has_udp && hdr.udp_64.isValid()) {
            src_port_val = hdr.udp_64.src_port;
            dst_port_val = hdr.udp_64.dst_port;
        }

        meta.src_port_merged = src_port_val;
        meta.dst_port_merged = dst_port_val;

        // ─── 4a: Connection state ───

        meta.conn_class = CONN_UNKNOWN;

        if (meta.has_tcp && hdr.tcp_64.isValid()) {
            // Check CV flag first — fast path for established
            if ((hdr.tcp_64.flags & TCP_FLAG_CV) != 0) {
                meta.conn_class = CONN_ESTABLISHED;
            } else if ((hdr.tcp_64.flags & TCP_FLAG_SYN) != 0) {
                meta.conn_class = CONN_NEW;
            } else {
                connection_class.apply();
            }
        } else if (meta.has_udp && hdr.udp_64.isValid()) {
            connection_class_udp.apply();
        }

        // ─── 4b: Traffic type ───

        traffic_class.apply();

        // ─── 4c: Threat level ───

        meta.threat_level = THREAT_NONE;

        if (!meta.svt_valid) {
            if (meta.conn_class == CONN_UNKNOWN) {
                meta.threat_level = THREAT_HIGH;
            } else if (meta.conn_class == CONN_ESTABLISHED) {
                meta.threat_level = THREAT_MEDIUM;
            } else {
                meta.threat_level = THREAT_HIGH;
            }
        } else {
            if (meta.conn_class == CONN_NEW) {
                meta.threat_level = THREAT_LOW;
            } else {
                meta.threat_level = THREAT_NONE;
            }
        }

        // Amplification risk for unvalidated UDP
        if (meta.has_udp && hdr.udp_64.isValid()) {
            if ((hdr.udp_64.udp_flags & UDP_FLAG_VALIDATED) == 0) {
                if (meta.threat_level < THREAT_AMPLIFICATION) {
                    meta.threat_level = THREAT_AMPLIFICATION;
                }
            }
        }

        // ─── 4d: Firewall policy ───

        firewall_policy.apply();

        if (meta.do_drop) { return; }

        // ─── SYN rate limiting ───
        // Applied after firewall permit, only to NEW TCP connections

        if (meta.has_tcp && meta.conn_class == CONN_NEW) {
            if ((hdr.tcp_64.flags & TCP_FLAG_SYN) != 0) {
                syn_rate_limit.apply();
            }
        }
    }
}

#endif
