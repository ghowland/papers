/*
 * IPv4-64 Main Program
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Seven-phase packet lifecycle:
 *   Phase 1: Parse
 *   Phase 2: Validate
 *   Phase 3: Authenticate
 *   Phase 4: Classify
 *   Phase 5: Route and Balance
 *   Phase 6: Transform
 *   Phase 7: Emit
 *
 * Plus edge conversion for IPv4 interoperability.
 *
 * Target: V1Model architecture (BMv2 reference, portable to
 *         BlueField-3 DOCA, Pensando Elba, Intel E2100,
 *         Xilinx Alveo SN1000 with appropriate architecture mapping)
 */

#include <core.p4>
#include <v1model.p4>

#include "constants.p4"
#include "headers.p4"
#include "metadata.p4"
#include "externs.p4"
#include "counters.p4"
#include "port_config.p4"
#include "convert_ingress.p4"
#include "convert_egress.p4"
#include "validate.p4"
#include "authenticate.p4"
#include "classify.p4"
#include "route_balance.p4"
#include "transform.p4"
#include "deparser.p4"

// ─── Additional metadata fields referenced by classify ───
// These are merged port values used by traffic_class and firewall tables.
// Declared here because they augment the metadata struct.

struct connection_digest_t {
    bit<64> src_addr;
    bit<64> dst_addr;
    bit<16> src_port;
    bit<16> dst_port;
    bit<8>  protocol;
}

// Digest type IDs for ARM control plane
const bit<32> DIGEST_CONNECTION_INSERT = 1;
const bit<32> DIGEST_CONNECTION_FIN    = 2;
const bit<32> DIGEST_CONNECTION_RST    = 3;

// Mirror session for firewall logging
const bit<32> FW_LOG_MIRROR_SESSION = 100;

// ════════════════════════════════════════════════════════════
//  INGRESS PIPELINE
// ════════════════════════════════════════════════════════════

control IPv4_64_Ingress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    // Instantiate all phase controls
    PortConfigIngress()  port_config_in;
    ConvertIngress()     convert_in;
    Validate()           validate;
    Authenticate()       authenticate;
    Classify()           classify;
    RouteBalance()       route_balance;
    Transform()          transform;

    apply {

        // ─── Port configuration ───
        // Determines if this is a core or edge port.
        // Edge ports accept IPv4 and trigger conversion.
        // Core ports accept only IPv4-64.
        port_config_in.apply(hdr, meta, std_meta);
        if (meta.do_drop) { mark_to_drop(std_meta); return; }

        // ─── Edge conversion (IPv4 → IPv4-64) ───
        // Runs only for IPv4 packets on edge ports.
        // After this point, the packet is IPv4-64 regardless of origin.
        convert_in.apply(hdr, meta, std_meta);
        if (meta.do_drop) { mark_to_drop(std_meta); return; }

        // ─── Phase 2: Validate ───
        // Fixed-offset field checks. Any failure → silent drop.
        validate.apply(hdr, meta, std_meta);
        if (meta.do_drop) {
            update_counters_drop();
            mark_to_drop(std_meta);
            return;
        }

        // ─── Phase 3: Authenticate ───
        // SVT verification, Fragment Token, Retry Cookie.
        authenticate.apply(hdr, meta, std_meta);
        if (meta.do_drop) {
            update_counters_drop();
            mark_to_drop(std_meta);
            return;
        }

        // ─── Phase 4: Classify ───
        // Connection state, traffic type, threat level, firewall policy.
        classify.apply(hdr, meta, std_meta);
        if (meta.do_drop) {
            update_counters_drop();
            mark_to_drop(std_meta);
            return;
        }

        // ─── Phase 5: Route and Balance ───
        // LPM lookup, ECMP, LAG, weighted balancing.
        route_balance.apply(hdr, meta, std_meta);
        if (meta.do_drop) {
            update_counters_drop();
            mark_to_drop(std_meta);
            return;
        }

        // ─── Phase 6: Transform ───
        // TTL, SVT stamp, MAC, QoS, metering, connection tracking, accounting.
        transform.apply(hdr, meta, std_meta);
        // Transform handles its own drop and counter logic internally.
    }
}

// ════════════════════════════════════════════════════════════
//  EGRESS PIPELINE
// ════════════════════════════════════════════════════════════

control IPv4_64_Egress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    // Egress port configuration and conversion
    PortConfigEgress()  port_config_out;
    ConvertEgress()     convert_out;

    apply {

        // ─── Egress port type ───
        // Determines if this egress port needs IPv4 conversion.
        port_config_out.apply(hdr, meta, std_meta);

        // ─── Edge conversion (IPv4-64 → IPv4) ───
        // Runs only for IPv4-64 packets on edge egress ports.
        convert_out.apply(hdr, meta, std_meta);
    }
}

// ════════════════════════════════════════════════════════════
//  CHECKSUM VERIFICATION (ingress)
// ════════════════════════════════════════════════════════════

control IPv4_64_VerifyChecksum(
    inout headers_t hdr,
    inout metadata_t meta
) {
    apply {
        // IPv4-64 has no header checksum to verify.
        // Transport checksums are verified in Phase 2 (validate).
        //
        // For IPv4 legacy packets, the header checksum is verified
        // here before conversion. If invalid, the packet is dropped
        // before it enters the pipeline.

        if (hdr.ipv4_legacy.isValid()) {
            verify_checksum(
                hdr.ipv4_legacy.isValid(),
                {
                    hdr.ipv4_legacy.version,
                    hdr.ipv4_legacy.ihl,
                    hdr.ipv4_legacy.dscp,
                    hdr.ipv4_legacy.ecn,
                    hdr.ipv4_legacy.total_length,
                    hdr.ipv4_legacy.identification,
                    hdr.ipv4_legacy.flags,
                    hdr.ipv4_legacy.fragment_offset,
                    hdr.ipv4_legacy.ttl,
                    hdr.ipv4_legacy.protocol,
                    hdr.ipv4_legacy.src_addr,
                    hdr.ipv4_legacy.dst_addr
                },
                hdr.ipv4_legacy.header_checksum,
                HashAlgorithm.csum16
            );
        }
    }
}

// ════════════════════════════════════════════════════════════
//  CHECKSUM COMPUTATION (egress)
// ════════════════════════════════════════════════════════════

control IPv4_64_ComputeChecksum(
    inout headers_t hdr,
    inout metadata_t meta
) {
    apply {
        // IPv4-64 has no header checksum to compute.
        //
        // For IPv4 legacy egress (edge conversion), the header
        // checksum is computed by ConvertEgress using the
        // ipv4_checksum_compute extern.
        //
        // Transport checksums are computed by the conversion
        // modules using their respective extern calls.

        // If egress conversion produced a legacy header, update it
        if (hdr.ipv4_legacy.isValid()) {
            update_checksum(
                hdr.ipv4_legacy.isValid(),
                {
                    hdr.ipv4_legacy.version,
                    hdr.ipv4_legacy.ihl,
                    hdr.ipv4_legacy.dscp,
                    hdr.ipv4_legacy.ecn,
                    hdr.ipv4_legacy.total_length,
                    hdr.ipv4_legacy.identification,
                    hdr.ipv4_legacy.flags,
                    hdr.ipv4_legacy.fragment_offset,
                    hdr.ipv4_legacy.ttl,
                    hdr.ipv4_legacy.protocol,
                    hdr.ipv4_legacy.src_addr,
                    hdr.ipv4_legacy.dst_addr
                },
                hdr.ipv4_legacy.header_checksum,
                HashAlgorithm.csum16
            );
        }
    }
}

// ════════════════════════════════════════════════════════════
//  V1MODEL SWITCH INSTANTIATION
// ════════════════════════════════════════════════════════════

V1Switch(
    IPv4_64_Parser(),
    IPv4_64_VerifyChecksum(),
    IPv4_64_Ingress(),
    IPv4_64_Egress(),
    IPv4_64_ComputeChecksum(),
    IPv4_64_Deparser()
) main;
