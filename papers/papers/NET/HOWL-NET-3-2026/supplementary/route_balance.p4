/*
 * IPv4-64 Phase 5: Route and Balance
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Longest prefix match on 64-bit destination address.
 * ECMP and LAG selection using flow_label + 5-tuple hash.
 * Weighted balancing for graceful link draining.
 */

#ifndef _ROUTE_BALANCE_P4_
#define _ROUTE_BALANCE_P4_

control RouteBalance(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    // ─── 5a: Route lookup ───

    action route_direct(bit<16> nhop_id) {
        meta.next_hop_id = nhop_id;
        meta.use_ecmp = false;
    }

    action route_ecmp(bit<16> group_id) {
        meta.ecmp_group_id = group_id;
        meta.use_ecmp = true;
    }

    action route_drop() {
        meta.do_drop = true;
        meta.drop_reason = DROP_NO_ROUTE;
    }

    table ipv4_64_lpm {
        key = {
            meta.dst_addr_64 : lpm;
        }
        actions = {
            route_direct;
            route_ecmp;
            route_drop;
        }
        default_action = route_drop();
        size = 524288;    // 512K routes, configurable
    }

    // ─── 5b: ECMP group ───

    action ecmp_select(bit<16> member_count, bit<16> base_nhop_id) {
        // member_index = flow_hash % member_count
        // next_hop_id = base_nhop_id + member_index
        bit<16> member_index = (bit<16>)(meta.flow_hash % (bit<32>)member_count);
        meta.next_hop_id = base_nhop_id + member_index;
    }

    table ecmp_group {
        key = {
            meta.ecmp_group_id : exact;
        }
        actions = {
            ecmp_select;
        }
        size = 4096;
    }

    // ─── 5c: Weighted ECMP ───
    // For graceful draining. Members with weight 0 receive no new flows.
    // This table is an alternative to ecmp_group.
    // The control plane installs entries in one or the other.

    action weighted_select(
        bit<16> total_weight,
        bit<16> member_0_weight, bit<16> member_0_nhop,
        bit<16> member_1_weight, bit<16> member_1_nhop,
        bit<16> member_2_weight, bit<16> member_2_nhop,
        bit<16> member_3_weight, bit<16> member_3_nhop
    ) {
        bit<16> hash_mod = (bit<16>)(meta.flow_hash % (bit<32>)total_weight);

        // Walk weight ranges
        if (hash_mod < member_0_weight) {
            meta.next_hop_id = member_0_nhop;
        } else if (hash_mod < member_0_weight + member_1_weight) {
            meta.next_hop_id = member_1_nhop;
        } else if (hash_mod < member_0_weight + member_1_weight
                              + member_2_weight) {
            meta.next_hop_id = member_2_nhop;
        } else {
            meta.next_hop_id = member_3_nhop;
        }
    }

    table weighted_ecmp {
        key = {
            meta.ecmp_group_id : exact;
        }
        actions = {
            weighted_select;
        }
        size = 1024;
    }

    // ─── 5d: Next hop resolution ───

    action set_nexthop(bit<9> port, bit<48> dst_mac, bit<48> src_mac) {
        meta.egress_port = port;
        meta.next_hop_dst_mac = dst_mac;
        meta.next_hop_src_mac = src_mac;
    }

    action set_nexthop_lag(bit<16> lag_id) {
        // LAG selection uses same flow_hash as ECMP
        // Resolved in lag_group table below
        meta.ecmp_group_id = lag_id;  // Reuse field for LAG lookup
    }

    table next_hop {
        key = {
            meta.next_hop_id : exact;
        }
        actions = {
            set_nexthop;
            set_nexthop_lag;
        }
        size = 16384;
    }

    // ─── 5e: LAG group ───

    action lag_select(bit<16> port_count, bit<9> base_port) {
        bit<16> port_index = (bit<16>)(meta.flow_hash % (bit<32>)port_count);
        meta.egress_port = base_port + (bit<9>)port_index;
    }

    table lag_group {
        key = {
            meta.ecmp_group_id : exact;
        }
        actions = {
            lag_select;
        }
        size = 256;
    }

    apply {
        if (meta.do_drop) { return; }
        if (!hdr.ipv4_64.isValid()) { return; }

        // ─── Compute flow hash ───
        // Used by ECMP and LAG for consistent path selection.
        // Inputs: src_addr_64 ++ dst_addr_64 ++ flow_label
        //         ++ protocol ++ src_port ++ dst_port

        bit<192> hash_input = meta.src_addr_64
                              ++ meta.dst_addr_64
                              ++ (bit<32>)hdr.ipv4_64.flow_label
                              ++ (bit<24>)0
                              ++ hdr.ipv4_64.protocol
                              ++ (bit<16>)meta.src_port_merged
                              ++ (bit<16>)meta.dst_port_merged;

        hash_crc32(hash_input, meta.flow_hash);

        // ─── Route lookup ───

        ipv4_64_lpm.apply();

        if (meta.do_drop) { return; }

        // ─── ECMP resolution ───

        if (meta.use_ecmp) {
            // Try weighted first. If no entry, fall back to standard.
            if (!weighted_ecmp.apply().hit) {
                ecmp_group.apply();
            }
        }

        // ─── Next hop resolution ───

        next_hop.apply();

        // ─── LAG resolution ───
        // If next_hop returned a LAG action, resolve the physical port.
        // The set_nexthop_lag action reuses ecmp_group_id for the LAG ID.
        // A real implementation would use a separate metadata field
        // or check the action type. This reference uses a second
        // table apply which is harmless if next_hop resolved directly.

        // Only apply LAG if egress_port was not directly set
        if (meta.egress_port == 0) {
            lag_group.apply();
        }

        // Set egress port on standard metadata
        std_meta.egress_spec = meta.egress_port;
    }
}

#endif
