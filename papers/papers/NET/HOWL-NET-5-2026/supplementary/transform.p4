/*
 * IPv4-64 Phase 6: Transform
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Modifies packet for egress:
 *   TTL decrement
 *   SVT stamping
 *   MAC rewrite
 *   QoS marking
 *   Metering
 *   Connection tracking update
 *   Accounting
 */

#ifndef _TRANSFORM_P4_
#define _TRANSFORM_P4_

control Transform(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    // ─── QoS marking table ───

    action set_qos(bit<6> dscp_val) {
        meta.new_dscp = dscp_val;
    }

    table qos_marking {
        key = {
            meta.traffic_class : exact;
            meta.threat_level  : exact;
            meta.conn_class    : exact;
        }
        actions = {
            set_qos;
        }
        default_action = set_qos(0);
        size = 256;
    }

    apply {
        if (meta.do_drop) {
            // Final drop accounting
            update_counters_drop();

            // SVT accounting even on drop
            if (meta.svt_valid) {
                update_counters_svt_pass();
            } else {
                update_counters_svt_fail();
            }

            // Mark for drop in standard metadata
            mark_to_drop(std_meta);
            return;
        }

        if (!hdr.ipv4_64.isValid()) { return; }

        // ─── 6a: TTL decrement ───

        hdr.ipv4_64.ttl = hdr.ipv4_64.ttl - 1;

        if (hdr.ipv4_64.ttl == 0) {
            meta.do_drop = true;
            meta.drop_reason = DROP_TTL_EXPIRED;
            update_counters_drop();
            mark_to_drop(std_meta);
            return;
        }

        // No header checksum recomputation.
        // IPv4-64 has no header checksum.
        // This is where IPv4 spends 10-30 addition operations per packet.

        // ─── 6b: SVT stamping ───
        // Stamp outgoing packets that originate from or transit this network.
        // The edge router stamps converted IPv4 packets.
        // Transit routers re-stamp if configured for re-stamping mode.

        bit<128> local_svt_key;
        bit<32>  local_svt_epoch;
        svt_get_key(0, local_svt_key, local_svt_epoch);

        bit<96> svt_stamp_data = meta.src_addr_64 ++ local_svt_epoch;
        bit<32> svt_stamp_result;
        hmac_sha256_32(local_svt_key, svt_stamp_data, svt_stamp_result);

        hdr.ipv4_64.svt = svt_stamp_result;

        // ─── 6c: MAC rewrite ───

        hdr.ethernet.dst_mac = meta.next_hop_dst_mac;
        hdr.ethernet.src_mac = meta.next_hop_src_mac;

        // ─── 6d: QoS marking ───

        qos_marking.apply();
        hdr.ipv4_64.dscp = meta.new_dscp;

        // ECN: if meter marks yellow and packet is ECN-capable,
        // set CE (Congestion Experienced) bits
        // ECN-capable = ecn field is 01 or 10
        // CE = ecn field set to 11

        // ─── 6e: Metering ───

        // Firewall rate-limit meter
        if (meta.fw_meter_id != 0) {
            bit<2> fw_color;
            meter_firewall.execute_meter(
                (bit<32>)meta.fw_meter_id,
                fw_color
            );
            meta.meter_color = fw_color;

            if (fw_color == METER_RED) {
                meta.do_drop = true;
                meta.drop_reason = DROP_RATE_EXCEEDED;
                update_counters_drop();
                mark_to_drop(std_meta);
                return;
            }

            if (fw_color == METER_YELLOW) {
                // Mark ECN CE if ECN-capable
                if (hdr.ipv4_64.ecn == 1 || hdr.ipv4_64.ecn == 2) {
                    hdr.ipv4_64.ecn = 3;  // CE
                }
            }
        }

        // UDP unvalidated meter
        if (meta.has_udp && hdr.udp_64.isValid()) {
            if ((hdr.udp_64.udp_flags & UDP_FLAG_VALIDATED) == 0) {
                bit<2> udp_color;
                meter_udp_unvalidated.execute_meter(0, udp_color);

                if (udp_color == METER_RED) {
                    meta.do_drop = true;
                    meta.drop_reason = DROP_AMPLIFICATION_THROTTLE;
                    update_counters_drop();
                    mark_to_drop(std_meta);
                    return;
                }
            }
        }

        // ─── 6f: Connection tracking update ───

        if (meta.has_tcp && hdr.tcp_64.isValid()) {
            bit<16> tcp_flags = hdr.tcp_64.flags;

            // Cookie just validated: set CV flag, insert connection
            if (meta.cookie_valid) {
                hdr.tcp_64.flags = tcp_flags | TCP_FLAG_CV;
                update_counters_cookie_pass();

                // Connection insertion into the connection_class table
                // is performed via a digest sent to the ARM control plane.
                // The ARM control plane inserts the 5-tuple entry.
                // P4 does not support direct table insertion from the
                // data plane on most targets. The digest mechanism
                // is target-specific.
                //
                // digest<connection_digest_t>(
                //     DIGEST_CONNECTION_INSERT,
                //     {
                //         meta.src_addr_64,
                //         meta.dst_addr_64,
                //         hdr.tcp_64.src_port,
                //         hdr.tcp_64.dst_port,
                //         meta.parsed_protocol
                //     }
                // );
            }

            // FIN on established connection: notify ARM for timed removal
            if ((tcp_flags & TCP_FLAG_FIN) != 0
                && meta.conn_class == CONN_ESTABLISHED) {
                // digest<connection_digest_t>(
                //     DIGEST_CONNECTION_FIN,
                //     {
                //         meta.src_addr_64,
                //         meta.dst_addr_64,
                //         hdr.tcp_64.src_port,
                //         hdr.tcp_64.dst_port,
                //         meta.parsed_protocol
                //     }
                // );
            }

            // RST on established connection: notify ARM for immediate removal
            if ((tcp_flags & TCP_FLAG_RST) != 0
                && meta.conn_class == CONN_ESTABLISHED) {
                // digest<connection_digest_t>(
                //     DIGEST_CONNECTION_RST,
                //     {
                //         meta.src_addr_64,
                //         meta.dst_addr_64,
                //         hdr.tcp_64.src_port,
                //         hdr.tcp_64.dst_port,
                //         meta.parsed_protocol
                //     }
                // );
            }
        }

        // ─── 6g: Accounting ───

        // SVT result accounting
        if (meta.svt_valid) {
            update_counters_svt_pass();
        } else {
            update_counters_svt_fail();
        }

        // Per-port and per-class counters
        update_counters_permit();

        // Firewall logging
        if (meta.fw_log) {
            // Logging is target-specific. On most platforms,
            // a clone or digest sends the packet metadata
            // to the ARM cores for syslog/telemetry export.
            //
            // clone3(CloneType.I2E, FW_LOG_MIRROR_SESSION, meta);
        }
    }
}

#endif
