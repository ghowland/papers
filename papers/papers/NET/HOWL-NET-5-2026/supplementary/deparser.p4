/*
 * IPv4-64 Deparser (Phase 7: Emit)
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Serializes headers to wire format.
 * Emits either IPv4-64 or IPv4 legacy headers depending
 * on egress port configuration.
 *
 * All emitted headers are fixed length.
 * No padding, no length computation, no option serialization.
 */

#ifndef _DEPARSER_P4_
#define _DEPARSER_P4_

control IPv4_64_Deparser(
    packet_out pkt,
    in headers_t hdr
) {

    apply {
        // Ethernet is always emitted
        pkt.emit(hdr.ethernet);

        // ─── IPv4-64 native path ───
        // Emitted when egress port is core (no conversion)
        // or when packet was never converted to IPv4 legacy

        pkt.emit(hdr.ipv4_64);       // 32 bytes if valid, nothing if invalid
        pkt.emit(hdr.tcp_64);        // 24 bytes if valid
        pkt.emit(hdr.udp_64);        // 10 bytes if valid

        // ─── IPv4 legacy path ───
        // Emitted when egress port is edge and conversion occurred
        // ConvertEgress invalidated ipv4_64/tcp_64/udp_64
        // and validated ipv4_legacy/tcp_legacy/udp_legacy

        pkt.emit(hdr.ipv4_legacy);   // 20 bytes if valid, nothing if invalid
        pkt.emit(hdr.tcp_legacy);    // 20 bytes if valid
        pkt.emit(hdr.udp_legacy);    // 8 bytes if valid

        // ─── ICMP ───
        // Same header format in both paths
        pkt.emit(hdr.icmp);          // 8 bytes if valid

        // Payload follows automatically.
        // The packet_out appends remaining unparsed bytes.
    }
}

#endif
