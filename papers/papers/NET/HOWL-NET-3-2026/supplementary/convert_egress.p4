/*
 * IPv4-64 IPv4 Edge Egress Conversion
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Converts IPv4-64 packets back to IPv4 at edge ports.
 * Produces a clean 20-byte IPv4 header (no options).
 * Produces a clean 20-byte TCP header (no options).
 * Produces a clean 8-byte UDP header.
 *
 * Called in Phase 7 before deparser, after all transforms.
 */

#ifndef _CONVERT_EGRESS_P4_
#define _CONVERT_EGRESS_P4_

control ConvertEgress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    apply {
        // Only convert if egress port is configured as edge
        if (!meta.convert_to_ipv4_on_egress) { return; }
        if (!hdr.ipv4_64.isValid()) { return; }

        // ─── Address range check ───
        // Upper 32 bits must be zero for IPv4 compatibility.
        // Extended addresses cannot be sent to IPv4 networks.

        if (hdr.ipv4_64.src_addr_upper != 0
            || hdr.ipv4_64.dst_addr_upper != 0) {
            meta.do_drop = true;
            meta.drop_reason = DROP_EXTENDED_ADDR_TO_LEGACY;
            update_counters_ipv4_egress_ext_drop();
            mark_to_drop(std_meta);
            return;
        }

        // ─── Build IPv4 legacy header ───

        hdr.ipv4_legacy.setValid();

        hdr.ipv4_legacy.version = IPV4_LEGACY_VERSION;
        hdr.ipv4_legacy.ihl = 5;  // 20 bytes, no options

        // Direct field copies
        hdr.ipv4_legacy.dscp = hdr.ipv4_64.dscp;
        hdr.ipv4_legacy.ecn  = hdr.ipv4_64.ecn;
        hdr.ipv4_legacy.ttl  = hdr.ipv4_64.ttl;
        hdr.ipv4_legacy.protocol = hdr.ipv4_64.protocol;
        hdr.ipv4_legacy.identification = hdr.ipv4_64.identification;

        // Total length: payload_length + 20-byte IPv4 header
        hdr.ipv4_legacy.total_length = hdr.ipv4_64.payload_length
                                     + IPV4_MIN_HEADER_SIZE;

        // Flags: IPv4-64 4 bits (DF, MF, res, res) → IPv4 3 bits (res, DF, MF)
        bit<3> legacy_flags = 0;
        if ((hdr.ipv4_64.flags & IP_FLAG_DF) != 0) {
            legacy_flags = legacy_flags | 0x2;  // DF
        }
        if ((hdr.ipv4_64.flags & IP_FLAG_MF) != 0) {
            legacy_flags = legacy_flags | 0x1;  // MF
        }
        hdr.ipv4_legacy.flags = legacy_flags;

        // Fragment offset: convert from 256-byte units to 8-byte units
        // Multiply by 32
        hdr.ipv4_legacy.fragment_offset =
            (bit<13>)hdr.ipv4_64.fragment_offset * 32;

        // Address mapping: lower 32 bits
        hdr.ipv4_legacy.src_addr = hdr.ipv4_64.src_addr_lower;
        hdr.ipv4_legacy.dst_addr = hdr.ipv4_64.dst_addr_lower;

        // Header checksum: compute fresh
        ipv4_checksum_compute(hdr.ipv4_legacy, hdr.ipv4_legacy.header_checksum);

        // ─── Invalidate IPv4-64 header ───
        hdr.ipv4_64.setInvalid();

        // ─── TCP egress conversion ───

        if (meta.has_tcp && hdr.tcp_64.isValid()) {

            hdr.tcp_legacy.setValid();

            // Direct field copies
            hdr.tcp_legacy.src_port    = hdr.tcp_64.src_port;
            hdr.tcp_legacy.dst_port    = hdr.tcp_64.dst_port;
            hdr.tcp_legacy.seq_num     = hdr.tcp_64.seq_num;
            hdr.tcp_legacy.ack_num     = hdr.tcp_64.ack_num;
            hdr.tcp_legacy.window_size = hdr.tcp_64.window_size;

            // Data offset: 5 (20 bytes, no options)
            hdr.tcp_legacy.data_offset = 5;
            hdr.tcp_legacy.legacy_reserved = 0;

            // Urgent pointer: zero (URG data not preserved through conversion)
            hdr.tcp_legacy.urgent_ptr = 0;

            // Flags: extract 9 standard flags from IPv4-64 16-bit field
            // Discard CV, SACK-OK, WS (IPv4 TCP has no equivalent)
            bit<16> f64 = hdr.tcp_64.flags;
            bit<8> legacy_tcp_flags = 0;

            // FIN (IPv4-64 bit 13) → legacy bit 0
            if ((f64 & TCP_FLAG_FIN) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x01; }
            // SYN (IPv4-64 bit 15) → legacy bit 1
            if ((f64 & TCP_FLAG_SYN) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x02; }
            // RST (IPv4-64 bit 12) → legacy bit 2
            if ((f64 & TCP_FLAG_RST) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x04; }
            // PSH (IPv4-64 bit 11) → legacy bit 3
            if ((f64 & TCP_FLAG_PSH) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x08; }
            // ACK (IPv4-64 bit 14) → legacy bit 4
            if ((f64 & TCP_FLAG_ACK) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x10; }
            // URG (IPv4-64 bit 10) → legacy bit 5
            if ((f64 & TCP_FLAG_URG) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x20; }
            // ECE (IPv4-64 bit 9) → legacy bit 6
            if ((f64 & TCP_FLAG_ECE) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x40; }
            // CWR (IPv4-64 bit 8) → legacy bit 7
            if ((f64 & TCP_FLAG_CWR) != 0) { legacy_tcp_flags = legacy_tcp_flags | 0x80; }

            hdr.tcp_legacy.flags = legacy_tcp_flags;

            // NS flag → legacy reserved bit 0
            if ((f64 & TCP_FLAG_NS) != 0) {
                hdr.tcp_legacy.legacy_reserved = 0x1;
            }

            // Checksum: recompute over IPv4 pseudo-header
            bit<16> tcp_seg_len = hdr.ipv4_legacy.total_length
                                - IPV4_MIN_HEADER_SIZE;
            tcp_checksum_ipv4(
                hdr.ipv4_legacy.src_addr,
                hdr.ipv4_legacy.dst_addr,
                PROTO_TCP,
                tcp_seg_len,
                hdr.tcp_legacy,
                hdr.tcp_legacy.checksum
            );

            // Invalidate IPv4-64 TCP
            hdr.tcp_64.setInvalid();
        }

        // ─── UDP egress conversion ───

        if (meta.has_udp && hdr.udp_64.isValid()) {

            hdr.udp_legacy.setValid();

            // Direct field copies
            hdr.udp_legacy.src_port = hdr.udp_64.src_port;
            hdr.udp_legacy.dst_port = hdr.udp_64.dst_port;

            // Length: subtract 2 bytes (remove flags + reserved)
            hdr.udp_legacy.length = hdr.udp_64.length - 2;

            // Checksum: recompute over IPv4 pseudo-header
            bit<16> udp_seg_len = hdr.ipv4_legacy.total_length
                                - IPV4_MIN_HEADER_SIZE;
            udp_checksum_ipv4(
                hdr.ipv4_legacy.src_addr,
                hdr.ipv4_legacy.dst_addr,
                PROTO_UDP,
                udp_seg_len,
                hdr.udp_legacy,
                hdr.udp_legacy.checksum
            );

            // Invalidate IPv4-64 UDP
            hdr.udp_64.setInvalid();
        }

        // ─── Update ethertype ───
        hdr.ethernet.ether_type = ETHERTYPE_IPV4;

        // ─── Egress counter ───
        update_counters_ipv4_egress();
    }
}

#endif
