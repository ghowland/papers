/*
 * IPv4-64 Port Configuration
 * HOWL-NET-3-2026 Reference Implementation
 *
 * Each port is either core (native IPv4-64) or edge (IPv4 conversion).
 * Ingress port type determines whether IPv4 conversion runs.
 * Egress port type determines whether IPv4-64 → IPv4 conversion runs.
 */

#ifndef _PORT_CONFIG_P4_
#define _PORT_CONFIG_P4_

control PortConfigIngress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    action set_port_core() {
        meta.ingress_port_type = PORT_TYPE_CORE;
    }

    action set_port_edge() {
        meta.ingress_port_type = PORT_TYPE_EDGE;
    }

    table port_config_ingress {
        key = {
            std_meta.ingress_port : exact;
        }
        actions = {
            set_port_core;
            set_port_edge;
        }
        default_action = set_port_edge();  // Safe default: treat as edge
        size = 512;
    }

    apply {
        port_config_ingress.apply();

        // If edge port received an IPv4 packet, conversion is needed.
        // If core port received an IPv4 packet, drop it — core ports
        // only accept IPv4-64.

        if (meta.converted_from_ipv4) {
            if (meta.ingress_port_type == PORT_TYPE_CORE) {
                // IPv4 packet on core port: protocol violation
                meta.do_drop = true;
                meta.drop_reason = DROP_BAD_VERSION;
                return;
            }
            // Edge port: conversion will proceed in ConvertIngress
        }
    }
}

control PortConfigEgress(
    inout headers_t hdr,
    inout metadata_t meta,
    inout standard_metadata_t std_meta
) {

    action set_egress_core() {
        meta.egress_port_type = PORT_TYPE_CORE;
        meta.convert_to_ipv4_on_egress = false;
    }

    action set_egress_edge() {
        meta.egress_port_type = PORT_TYPE_EDGE;
        meta.convert_to_ipv4_on_egress = true;
    }

    table port_config_egress {
        key = {
            std_meta.egress_spec : exact;
        }
        actions = {
            set_egress_core;
            set_egress_edge;
        }
        default_action = set_egress_edge();  // Safe default
        size = 512;
    }

    apply {
        port_config_egress.apply();
    }
}

#endif
