/*
 * IPv4-64 Phase 3: Authenticate
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Three independent authentication operations:
 *   3a: Source Validation Token
 *   3b: Fragment Token
 *   3c: Retry Cookie
 */

#ifndef _AUTHENTICATE_P4_
#define _AUTHENTICATE_P4_

control Authenticate(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    apply {
        if (meta.do_drop) { return; }
        if (!hdr.ipv4_64.isValid()) { return; }

        // ─── 3a: Source Validation Token ───

        bit<128> svt_key_current;
        bit<32>  svt_epoch_current;
        bit<128> svt_key_previous;
        bit<32>  svt_epoch_previous;
        bit<32>  svt_computed;

        svt_get_key(0, svt_key_current, svt_epoch_current);
        svt_get_key(1, svt_key_previous, svt_epoch_previous);

        // Build HMAC input: src_addr_64 (64 bits) ++ epoch (32 bits) = 96 bits
        bit<96> svt_data_current = meta.src_addr_64
                                   ++ svt_epoch_current;

        hmac_sha256_32(svt_key_current, svt_data_current, svt_computed);

        if (svt_computed == hdr.ipv4_64.svt) {
            meta.svt_valid = true;
        } else {
            // Try previous epoch
            bit<96> svt_data_previous = meta.src_addr_64
                                        ++ svt_epoch_previous;
            hmac_sha256_32(svt_key_previous, svt_data_previous, svt_computed);

            if (svt_computed == hdr.ipv4_64.svt) {
                meta.svt_valid = true;
            } else {
                meta.svt_valid = false;
                // Do not drop here. SVT result feeds into
                // Phase 4 threat classification. The operator's
                // firewall policy determines the action.
            }
        }

        // ─── 3b: Fragment Token ───

        if (meta.is_fragment) {
            bit<64>  frag_key;
            bit<16>  frag_computed;

            fragment_get_secret(frag_key);

            // Build SipHash input:
            // identification (16) ++ src_addr_64 (64) ++ dst_addr_64 (64) = 144 bits
            bit<144> frag_data = hdr.ipv4_64.identification
                                 ++ meta.src_addr_64
                                 ++ meta.dst_addr_64;

            siphash_2_4(frag_key, frag_data, frag_computed);

            if (frag_computed != hdr.ipv4_64.fragment_token) {
                meta.do_drop = true;
                meta.drop_reason = DROP_BAD_FRAGMENT_TOKEN;
                return;
            }
        }

        // ─── 3c: Retry Cookie ───

        if (meta.has_tcp && hdr.tcp_64.isValid()) {
            bit<16> tcp_flags = hdr.tcp_64.flags;

            // Cookie verification applies to ACK packets
            // where CV is not yet set (completing handshake)
            bool is_ack = (tcp_flags & TCP_FLAG_ACK) != 0;
            bool is_syn = (tcp_flags & TCP_FLAG_SYN) != 0;
            bool is_cv  = (tcp_flags & TCP_FLAG_CV)  != 0;

            if (is_ack && !is_syn && !is_cv
                && hdr.tcp_64.retry_cookie != 0) {

                bit<128> cookie_key;
                bit<32>  cookie_timestamp;
                cookie_get_secret(cookie_key, cookie_timestamp);

                // Build HMAC input:
                // src_addr_64 (64) ++ src_port (16) ++ dst_port (16) ++ timestamp (32) = 128 bits
                bit<128> cookie_data = meta.src_addr_64
                                       ++ (bit<32>)hdr.tcp_64.src_port
                                          ++ (bit<32>)hdr.tcp_64.dst_port
                                       ++ cookie_timestamp;

                bit<56> cookie_computed;
                hmac_sha256_56(cookie_key, cookie_data, cookie_computed);

                // Upper 56 bits of cookie must match
                bit<56> cookie_upper = hdr.tcp_64.retry_cookie[63:8];

                if (cookie_computed == cookie_upper) {
                    meta.cookie_valid = true;

                    // Decode lower 8 bits
                    meta.cookie_mss_index =
                        hdr.tcp_64.retry_cookie[7:5];
                    meta.cookie_window_scale =
                        hdr.tcp_64.retry_cookie[4:1];
                    meta.cookie_sack_ok =
                        hdr.tcp_64.retry_cookie[0:0];
                } else {
                    meta.do_drop = true;
                    meta.drop_reason = DROP_BAD_COOKIE;
                    return;
                }
            }
        }
    }
}

#endif
