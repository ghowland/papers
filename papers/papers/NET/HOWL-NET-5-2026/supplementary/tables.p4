/*
 * IPv4-64 Table Summary
 * HOWL-NET-3-2026 Reference Implementation
 *
 * This file does not define tables (they are defined in their
 * respective phase modules). It provides the merged port metadata
 * fields referenced by classify and route_balance, and documents
 * the table inventory for the control plane.
 *
 * Table Inventory (for control plane integration):
 *
 * Phase 1:
 *   port_config          — port_config.p4
 *     Key: ingress_port (exact)
 *     Populated by: operator configuration
 *
 * Phase 4:
 *   connection_class     — classify.p4
 *     Key: 5-tuple (exact)
 *     Populated by: P4 pipeline (cookie validation) + ARM GC
 *
 *   connection_class_udp — classify.p4
 *     Key: 5-tuple (exact)
 *     Populated by: ARM control plane
 *
 *   traffic_class        — classify.p4
 *     Key: protocol + dst_port (exact)
 *     Populated by: operator QoS configuration
 *
 *   firewall_policy      — classify.p4
 *     Key: src/dst prefix + ports + proto + class + threat (ternary)
 *     Populated by: security policy manager
 *
 *   syn_rate_limit       — classify.p4
 *     Key: src_addr_64 (LPM)
 *     Populated by: operator configuration
 *
 * Phase 5:
 *   ipv4_64_lpm          — route_balance.p4
 *     Key: dst_addr_64 (LPM)
 *     Populated by: BGP agent
 *
 *   ecmp_group           — route_balance.p4
 *     Key: group_id (exact)
 *     Populated by: routing agent / traffic engineering
 *
 *   weighted_ecmp        — route_balance.p4
 *     Key: group_id (exact)
 *     Populated by: routing agent / traffic engineering
 *
 *   next_hop             — route_balance.p4
 *     Key: hop_id (exact)
 *     Populated by: routing agent + ARP resolution
 *
 *   lag_group            — route_balance.p4
 *     Key: group_id (exact)
 *     Populated by: operator configuration
 *
 * Phase 6:
 *   qos_marking          — transform.p4
 *     Key: class + threat + conn_class (exact)
 *     Populated by: operator QoS configuration
 *
 * Phase 7:
 *   egress_port_type     — port_config.p4
 *     Key: egress_port (exact)
 *     Populated by: operator configuration
 */

#ifndef _TABLES_P4_
#define _TABLES_P4_

// This file is intentionally declarative.
// All table definitions live in their phase modules.
// This file exists for documentation and control plane reference.

#endif
