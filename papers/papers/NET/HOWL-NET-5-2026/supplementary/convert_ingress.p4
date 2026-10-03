/*
 * IPv4-64 IPv4 Edge Ingress Conversion
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Converts IPv4 packets to IPv4-64 at edge ports.
 * Strips IP options and TCP options.
 * Computes flow label, fragment token, and checksums.
 *
 * Called after parser, before Phase 2 validate.
 */

#ifndef _CONVERT_INGRESS_P4_
#define _CONVERT_INGRESS_P4_

control ConvertIngress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    apply {
        // Only process packets parsed as IPv4 legacy
        if (!meta.converted_from_ipv4) { return; }
        if (!hdr.ipv4_legacy.isValid()) { return; }

        // ─── Fragment offset alignment check ───
        // IPv4: 13 bits in 8-byte units
        // IPv4-64: 8 bits in 256-byte units
        // Conversion: (offset * 8) must be divisible by 256
        // Equivalent: offset must be divisible by 32

        bit<13> frag_ofs = hdr.ipv4_legacy.fragment_offset;

        if (frag_ofs != 0) {
            if ((frag_ofs % 32) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_FRAG_OFFSET_UNALIGNED;
                update_counters_frag_unaligned();
                return;
            }
        }

        // ─── Build IPv4-64 header ───

        hdr.ipv4_64.setValid();

        // Version
        hdr.ipv4_64.version = IPV4_64_VERSION;

        // Direct field copies
        hdr.ipv4_64.dscp = hdr.ipv4_legacy.dscp;
        hdr.ipv4_64.ecn  = hdr.ipv4_legacy.ecn;
        hdr.ipv4_64.ttl  = hdr.ipv4_legacy.ttl;
        hdr.ipv4_64.protocol = hdr.ipv4_legacy.protocol;
        hdr.ipv4_64.identification = hdr.ipv4_legacy.identification;

        // Flags: IPv4 has 3 bits (reserved, DF, MF)
        // IPv4-64 has 4 bits (DF, MF, reserved, reserved)
        bit<4> new_flags = 0;
        if ((hdr.ipv4_legacy.flags & 0x2) != 0) {  // DF
            new_flags = new_flags | IP_FLAG_DF;
        }
        if ((hdr.ipv4_legacy.flags & 0x1) != 0) {  // MF
            new_flags = new_flags | IP_FLAG_MF;
        }
        hdr.ipv4_64.flags = new_flags;

        // Payload length: IPv4 total_length - (IHL * 4)
        bit<16> ipv4_header_bytes = (bit<16>)hdr.ipv4_legacy.ihl * 4;
        hdr.ipv4_64.payload_length = hdr.ipv4_legacy.total_length
                                   - ipv4_header_bytes;

        // Fragment offset: convert from 8-byte units to 256-byte units
        hdr.ipv4_64.fragment_offset = (bit<8>)(frag_ofs / 32);

        // Address mapping: upper 32 bits zero, lower 32 bits = IPv4 address
        hdr.ipv4_64.src_addr_upper = 0;
        hdr.ipv4_64.src_addr_lower = hdr.ipv4_legacy.src_addr;
        hdr.ipv4_64.dst_addr_upper = 0;
        hdr.ipv4_64.dst_addr_lower = hdr.ipv4_legacy.dst_addr;

        // Concatenate for metadata
        meta.src_addr_64 = (bit<64>)hdr.ipv4_legacy.src_addr;
        meta.dst_addr_64 = (bit<64>)hdr.ipv4_legacy.dst_addr;

        // SVT: set to zero. Edge router stamps in Phase 6.
        hdr.ipv4_64.svt = 0;

        // Fragment detection
        meta.is_fragment = (new_flags & IP_FLAG_MF) != 0
                        || hdr.ipv4_64.fragment_offset != 0;
        meta.is_first_fragment = (new_flags & IP_FLAG_MF) != 0
                              && hdr.ipv4_64.fragment_offset == 0;

        // Fragment token: compute for fragmented packets
        if (meta.is_fragment) {
            bit<64> frag_key;
            fragment_get_secret(frag_key);

            bit<144> frag_data = hdr.ipv4_64.identification
                                 ++ meta.src_addr_64
                                 ++ meta.dst_addr_64;
            bit<16> frag_token;
            siphash_2_4(frag_key, frag_data, frag_token);
            hdr.ipv4_64.fragment_token = frag_token;
        } else {
            hdr.ipv4_64.fragment_token = 0;
        }

        // ─── Flow label: compute from 5-tuple ───
        // IPv4 has no flow label. Hash the 5-tuple to generate one
        // so ECMP works on converted traffic.

        bit<16> sport = 0;
        bit<16> dport = 0;

        if (meta.has_tcp && hdr.tcp_legacy.isValid()) {
            sport = hdr.tcp_legacy.src_port;
            dport = hdr.tcp_legacy.dst_port;
        } else if (meta.has_udp && hdr.udp_legacy.isValid()) {
            sport = hdr.udp_legacy.src_port;
            dport = hdr.udp_legacy.dst_port;
        }

        bit<192> flow_hash_input = meta.src_addr_64
                                   ++ meta.dst_addr_64
                                   ++ (bit<32>)0
                                   ++ (bit<24>)0
                                   ++ hdr.ipv4_legacy.protocol
                                   ++ sport
                                   ++ dport;
        bit<32> flow_hash_result;
        hash_crc32(flow_hash_input, flow_hash_result);
        hdr.ipv4_64.flow_label = flow_hash_result[19:0];

        // ─── IP options: stripped ───
        // Count for monitoring
        if (hdr.ipv4_options.isValid()) {
            update_counters_ipv4_options();
            hdr.ipv4_options.setInvalid();
        }

        // ─── Invalidate legacy IP header ───
        hdr.ipv4_legacy.setInvalid();

        // ─── TCP conversion ───

        if (meta.has_tcp && hdr.tcp_legacy.isValid()) {

            hdr.tcp_64.setValid();

            // Direct field copies
            hdr.tcp_64.src_port    = hdr.tcp_legacy.src_port;
            hdr.tcp_64.dst_port    = hdr.tcp_legacy.dst_port;
            hdr.tcp_64.seq_num     = hdr.tcp_legacy.seq_num;
            hdr.tcp_64.ack_num     = hdr.tcp_legacy.ack_num;
            hdr.tcp_64.window_size = hdr.tcp_legacy.window_size;

            // Flags: copy 9 standard flags from legacy 8-bit flags field
            // Legacy flags byte: CWR ECE URG ACK PSH RST SYN FIN
            // Map to IPv4-64 16-bit flags field positions
            bit<16> new_tcp_flags = 0;

            bit<8> lf = hdr.tcp_legacy.flags;

            // SYN (legacy bit 1) → IPv4-64 bit 15
            if ((lf & 0x02) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_SYN; }
            // ACK (legacy bit 4) → IPv4-64 bit 14
            if ((lf & 0x10) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_ACK; }
            // FIN (legacy bit 0) → IPv4-64 bit 13
            if ((lf & 0x01) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_FIN; }
            // RST (legacy bit 2) → IPv4-64 bit 12
            if ((lf & 0x04) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_RST; }
            // PSH (legacy bit 3) → IPv4-64 bit 11
            if ((lf & 0x08) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_PSH; }
            // URG (legacy bit 5) → IPv4-64 bit 10
            if ((lf & 0x20) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_URG; }
            // ECE (legacy bit 6) → IPv4-64 bit 9
            if ((lf & 0x40) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_ECE; }
            // CWR (legacy bit 7) → IPv4-64 bit 8
            if ((lf & 0x80) != 0) { new_tcp_flags = new_tcp_flags | TCP_FLAG_CWR; }

            // NS from legacy reserved field bit 0
            if ((hdr.tcp_legacy.legacy_reserved & 0x1) != 0) {
                new_tcp_flags = new_tcp_flags | TCP_FLAG_NS;
            }

            // CV = 0 (not validated)
            // SACK-OK from option scan
            if (meta.legacy_had_sack_permitted) {
                new_tcp_flags = new_tcp_flags | TCP_FLAG_SACK_OK;
            }
            // WS from option scan
            if (meta.legacy_had_window_scale) {
                new_tcp_flags = new_tcp_flags | TCP_FLAG_WS;
            }

            hdr.tcp_64.flags = new_tcp_flags;

            // Retry cookie: zero (IPv4 has no cookie)
            hdr.tcp_64.retry_cookie = 0;

            // Checksum: recompute over IPv4-64 pseudo-header
            bit<16> tcp_seg_len = hdr.ipv4_64.payload_length;
            tcp_checksum_ipv4_64(
                meta.src_addr_64,
                meta.dst_addr_64,
                PROTO_TCP,
                tcp_seg_len,
                hdr.tcp_64,
                hdr.tcp_64.checksum
            );

            // Invalidate legacy TCP
            hdr.tcp_legacy.setInvalid();
            if (hdr.tcp_options.isValid()) {
                hdr.tcp_options.setInvalid();
            }
        }

        // ─── UDP conversion ───

        if (meta.has_udp && hdr.udp_legacy.isValid()) {

            hdr.udp_64.setValid();

            // Direct field copies
            hdr.udp_64.src_port = hdr.udp_legacy.src_port;
            hdr.udp_64.dst_port = hdr.udp_legacy.dst_port;

            // Length: add 2 bytes for new flags + reserved fields
            hdr.udp_64.length = hdr.udp_legacy.length + 2;

            // Flags: Validated = 0, reserved = 0
            hdr.udp_64.udp_flags = 0;
            hdr.udp_64.reserved = 0;

            // Checksum: recompute over IPv4-64 pseudo-header
            // If IPv4 checksum was zero (optional), compute a real one
            if (hdr.udp_legacy.checksum == 0) {
                update_counters_udp_zero_cksum();
            }

            bit<16> udp_seg_len = hdr.ipv4_64.payload_length;
            udp_checksum_ipv4_64(
                meta.src_addr_64,
                meta.dst_addr_64,
                PROTO_UDP,
                udp_seg_len,
                hdr.udp_64,
                hdr.udp_64.checksum
            );

            // Invalidate legacy UDP
            hdr.udp_legacy.setInvalid();
        }

        // ─── Update ethertype ───
        hdr.ethernet.ether_type = ETHERTYPE_IPV4_64;

        // ─── Conversion counter ───
        update_counters_ipv4_ingress();

        // ─── Update parsed protocol metadata ───
        meta.parsed_protocol = hdr.ipv4_64.protocol;
    }
}

#endif
