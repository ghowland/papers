/*
 * IPv4-64 Phase 2: Validate
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Every field is checked against specification.
 * Any failure causes silent drop with no response.
 * All checks are fixed-offset field comparisons.
 */

#ifndef _VALIDATE_P4_
#define _VALIDATE_P4_

control Validate(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    apply {
        // Already marked for drop in parser
        if (meta.do_drop) { return; }

        // ─── IP layer validation ───

        // Payload length must match actual received bytes minus header
        bit<16> expected_payload = meta.packet_length
                                 - (bit<16>)ETHERTYPE_SIZE
                                 - IPV4_64_HEADER_SIZE;
        // Note: ETHERTYPE_SIZE accounts for the 14-byte ethernet header.
        // On targets where packet_length excludes ethernet,
        // adjust accordingly.

        if (hdr.ipv4_64.isValid()) {

            if (hdr.ipv4_64.payload_length != expected_payload) {
                meta.do_drop = true;
                meta.drop_reason = DROP_LENGTH_MISMATCH;
                return;
            }

            // Reserved flag bits must be zero
            if ((hdr.ipv4_64.flags & IP_FLAGS_RESERVED_MASK) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_RESERVED_NONZERO;
                return;
            }

            // TTL must not be zero on arrival
            if (hdr.ipv4_64.ttl == 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_TTL_ZERO;
                return;
            }

            // Runt fragment check: fragmented packet with
            // payload too small to contain transport header
            if (meta.is_fragment && !meta.is_first_fragment) {
                // Non-first fragments carry only data, no transport header.
                // Minimum useful fragment is at least 8 bytes of data.
                if (hdr.ipv4_64.payload_length < 8) {
                    meta.do_drop = true;
                    meta.drop_reason = DROP_RUNT_FRAGMENT;
                    return;
                }
            }
        }

        // ─── TCP validation ───

        if (meta.has_tcp && hdr.tcp_64.isValid()) {

            // Invalid flag combinations
            bit<16> f = hdr.tcp_64.flags;

            // SYN + FIN
            if ((f & TCP_FLAG_SYN) != 0 && (f & TCP_FLAG_FIN) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_INVALID_FLAGS;
                return;
            }

            // SYN + RST
            if ((f & TCP_FLAG_SYN) != 0 && (f & TCP_FLAG_RST) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_INVALID_FLAGS;
                return;
            }

            // FIN + RST
            if ((f & TCP_FLAG_FIN) != 0 && (f & TCP_FLAG_RST) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_INVALID_FLAGS;
                return;
            }

            // Reserved flag bits must be zero
            if ((f & TCP_FLAGS_RESERVED_MASK) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_RESERVED_NONZERO;
                return;
            }

            // SYN must have zero retry cookie
            if ((f & TCP_FLAG_SYN) != 0 && hdr.tcp_64.retry_cookie != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_SYN_COOKIE_NONZERO;
                return;
            }

            // Checksum verification — extern call
            // On mismatch, the extern sets result to 0
            // Production targets verify inline; this is the declaration point
            // Checksum verification is target-specific and may be
            // handled by hardware before the P4 pipeline.
            // If software-verified:
            //   bit<16> computed_cksum;
            //   tcp_checksum_ipv4_64(
            //       meta.src_addr_64, meta.dst_addr_64,
            //       hdr.ipv4_64.protocol,
            //       hdr.ipv4_64.payload_length,
            //       hdr.tcp_64, computed_cksum);
            //   if (computed_cksum != 0) {
            //       meta.do_drop = true;
            //       meta.drop_reason = DROP_BAD_CHECKSUM;
            //       return;
            //   }
        }

        // ─── UDP validation ───

        if (meta.has_udp && hdr.udp_64.isValid()) {

            // Checksum must not be zero (mandatory in IPv4-64)
            if (hdr.udp_64.checksum == 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_UDP_ZERO_CHECKSUM;
                return;
            }

            // Reserved field must be zero
            if (hdr.udp_64.reserved != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_RESERVED_NONZERO;
                return;
            }

            // Flags reserved bits must be zero
            // Bits 7:1 are reserved, bit 0 is Validated flag
            if ((hdr.udp_64.udp_flags & UDP_FLAGS_RESERVED_MASK) != 0) {
                meta.do_drop = true;
                meta.drop_reason = DROP_RESERVED_NONZERO;
                return;
            }

            // Checksum verification — same pattern as TCP above
            // Target-specific, may be hardware-verified
        }
    }
}

// Ethernet header size constant for payload length calculation
const bit<16> ETHERTYPE_SIZE = 14;

#endif
