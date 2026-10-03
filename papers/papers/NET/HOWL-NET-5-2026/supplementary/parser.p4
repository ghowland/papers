/*
 * IPv4-64 Parser
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Three states for native IPv4-64.
 * Additional states for IPv4 legacy edge conversion.
 * Variable-length parsing exists only in the legacy path.
 */

#ifndef _PARSER_P4_
#define _PARSER_P4_

parser IPv4_64_Parser(
    packet_in pkt,
    out headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    state start {
        pkt.extract(hdr.ethernet);
        meta.do_drop = false;
        meta.drop_reason = DROP_NONE;
        meta.converted_from_ipv4 = false;
        meta.has_tcp = false;
        meta.has_udp = false;
        meta.has_icmp = false;
        meta.is_fragment = false;
        meta.svt_valid = false;
        meta.cookie_valid = false;
        meta.fw_permit = false;
        meta.use_ecmp = false;
        meta.convert_to_ipv4_on_egress = false;
        meta.ingress_port = std_meta.ingress_port;
        meta.packet_length = std_meta.packet_length;

        transition select(hdr.ethernet.ether_type) {
            ETHERTYPE_IPV4_64 : parse_ipv4_64;
            ETHERTYPE_IPV4    : parse_ipv4_legacy;
            default           : accept;
        }
    }

    // ─── Native IPv4-64 path ───

    state parse_ipv4_64 {
        pkt.extract(hdr.ipv4_64);

        // Version check — earliest possible reject
        if (hdr.ipv4_64.version != IPV4_64_VERSION) {
            meta.do_drop = true;
            meta.drop_reason = DROP_BAD_VERSION;
            transition accept;
        }

        meta.parsed_protocol = hdr.ipv4_64.protocol;

        // Concatenate addresses for table lookups
        meta.src_addr_64 = hdr.ipv4_64.src_addr_upper
                           ++ hdr.ipv4_64.src_addr_lower;
        meta.dst_addr_64 = hdr.ipv4_64.dst_addr_upper
                           ++ hdr.ipv4_64.dst_addr_lower;

        // Fragment detection
        meta.is_fragment = (hdr.ipv4_64.flags & IP_FLAG_MF) != 0
                        || hdr.ipv4_64.fragment_offset != 0;
        meta.is_first_fragment = (hdr.ipv4_64.flags & IP_FLAG_MF) != 0
                              && hdr.ipv4_64.fragment_offset == 0;

        transition select(hdr.ipv4_64.protocol) {
            PROTO_TCP  : parse_tcp_64;
            PROTO_UDP  : parse_udp_64;
            PROTO_ICMP : parse_icmp;
            default    : accept;
        }
    }

    state parse_tcp_64 {
        pkt.extract(hdr.tcp_64);
        meta.has_tcp = true;
        transition accept;
    }

    state parse_udp_64 {
        pkt.extract(hdr.udp_64);
        meta.has_udp = true;
        transition accept;
    }

    state parse_icmp {
        pkt.extract(hdr.icmp);
        meta.has_icmp = true;
        transition accept;
    }

    // ─── IPv4 legacy path (edge ports only) ───

    state parse_ipv4_legacy {
        pkt.extract(hdr.ipv4_legacy);

        if (hdr.ipv4_legacy.version != IPV4_LEGACY_VERSION) {
            meta.do_drop = true;
            meta.drop_reason = DROP_BAD_VERSION;
            transition accept;
        }

        meta.original_ihl = hdr.ipv4_legacy.ihl;
        meta.parsed_protocol = hdr.ipv4_legacy.protocol;
        meta.converted_from_ipv4 = true;

        // Extract options if IHL > 5
        transition select(hdr.ipv4_legacy.ihl) {
            5       : parse_ipv4_legacy_transport;
            default : parse_ipv4_legacy_options;
        }
    }

    state parse_ipv4_legacy_options {
        // Extract variable-length options
        // Length = (IHL - 5) * 32 bits
        bit<32> opt_len = ((bit<32>)hdr.ipv4_legacy.ihl - 5) * 32;
        pkt.extract(hdr.ipv4_options, opt_len);
        transition parse_ipv4_legacy_transport;
    }

    state parse_ipv4_legacy_transport {
        transition select(hdr.ipv4_legacy.protocol) {
            PROTO_TCP  : parse_tcp_legacy;
            PROTO_UDP  : parse_udp_legacy;
            PROTO_ICMP : parse_icmp;
            default    : accept;
        }
    }

    state parse_tcp_legacy {
        pkt.extract(hdr.tcp_legacy);
        meta.has_tcp = true;
        meta.original_tcp_data_offset = (bit<16>)hdr.tcp_legacy.data_offset;

        // Extract TCP options if data_offset > 5
        transition select(hdr.tcp_legacy.data_offset) {
            5       : accept;
            default : parse_tcp_legacy_options;
        }
    }

    state parse_tcp_legacy_options {
        bit<32> tcp_opt_len = ((bit<32>)hdr.tcp_legacy.data_offset - 5) * 32;
        pkt.extract(hdr.tcp_options, tcp_opt_len);

        // Scan options for SACK-Permitted, Window Scale, MSS
        // This is a sequential scan of the variable-length option bytes.
        // In production, this is implemented as an extern or
        // unrolled for a maximum of 40 bytes (10 iterations of 4-byte words).
        //
        // The scan sets metadata flags:
        //   meta.legacy_had_sack_permitted
        //   meta.legacy_had_window_scale
        //   meta.legacy_window_scale_value
        //   meta.legacy_had_mss
        //   meta.legacy_mss_value
        //
        // Implementation note: P4 does not natively support
        // iterating over varbit fields. The target platform provides
        // this as an extern or the implementer unrolls the scan
        // for the known maximum option length (40 bytes).
        //
        // For this reference implementation, the option scan
        // is declared as a placeholder. A production implementation
        // replaces this with platform-specific option extraction.

        meta.legacy_had_sack_permitted = false;
        meta.legacy_had_window_scale = false;
        meta.legacy_window_scale_value = 0;
        meta.legacy_had_mss = false;
        meta.legacy_mss_value = 0;

        transition accept;
    }

    state parse_udp_legacy {
        pkt.extract(hdr.udp_legacy);
        meta.has_udp = true;
        transition accept;
    }
}

#endif
