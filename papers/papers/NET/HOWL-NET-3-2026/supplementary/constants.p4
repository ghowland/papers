/*
 * IPv4-64 Constants
 * HOWL-NET-3-2026 Reference Implementation
 */

#ifndef _CONSTANTS_P4_
#define _CONSTANTS_P4_

// Protocol version
const bit<4> IPV4_64_VERSION = 0xB;  // Assigned version TBD, using 11
const bit<4> IPV4_LEGACY_VERSION = 0x4;

// IP protocol numbers
const bit<8> PROTO_ICMP = 1;
const bit<8> PROTO_TCP  = 6;
const bit<8> PROTO_UDP  = 17;

// TCP flag bit positions within 16-bit flags field
// Bits 15 (MSB) down to 0 (LSB)
const bit<16> TCP_FLAG_SYN     = 0x8000;
const bit<16> TCP_FLAG_ACK     = 0x4000;
const bit<16> TCP_FLAG_FIN     = 0x2000;
const bit<16> TCP_FLAG_RST     = 0x1000;
const bit<16> TCP_FLAG_PSH     = 0x0800;
const bit<16> TCP_FLAG_URG     = 0x0400;
const bit<16> TCP_FLAG_ECE     = 0x0200;
const bit<16> TCP_FLAG_CWR     = 0x0100;
const bit<16> TCP_FLAG_NS      = 0x0080;
const bit<16> TCP_FLAG_CV      = 0x0040;
const bit<16> TCP_FLAG_SACK_OK = 0x0020;
const bit<16> TCP_FLAG_WS      = 0x0010;
const bit<16> TCP_FLAGS_RESERVED_MASK = 0x000F;

// IP flags bit positions within 4-bit flags field
const bit<4> IP_FLAG_DF = 0x8;
const bit<4> IP_FLAG_MF = 0x4;
const bit<4> IP_FLAGS_RESERVED_MASK = 0x3;

// UDP flags
const bit<8> UDP_FLAG_VALIDATED = 0x01;
const bit<8> UDP_FLAGS_RESERVED_MASK = 0xFE;

// Drop reason codes
const bit<8> DROP_NONE                    = 0x00;
const bit<8> DROP_BAD_VERSION             = 0x01;
const bit<8> DROP_LENGTH_MISMATCH         = 0x02;
const bit<8> DROP_RESERVED_NONZERO        = 0x03;
const bit<8> DROP_TTL_ZERO                = 0x04;
const bit<8> DROP_TTL_EXPIRED             = 0x05;
const bit<8> DROP_INVALID_FLAGS           = 0x06;
const bit<8> DROP_BAD_CHECKSUM            = 0x07;
const bit<8> DROP_UDP_ZERO_CHECKSUM       = 0x08;
const bit<8> DROP_RUNT_FRAGMENT           = 0x09;
const bit<8> DROP_FRAGMENT_OVERLAP        = 0x0A;
const bit<8> DROP_BAD_SVT                 = 0x10;
const bit<8> DROP_BAD_FRAGMENT_TOKEN      = 0x11;
const bit<8> DROP_BAD_COOKIE              = 0x12;
const bit<8> DROP_SYN_COOKIE_NONZERO      = 0x13;
const bit<8> DROP_FIREWALL_DENY           = 0x20;
const bit<8> DROP_NO_ROUTE                = 0x21;
const bit<8> DROP_RATE_EXCEEDED           = 0x22;
const bit<8> DROP_AMPLIFICATION_THROTTLE  = 0x23;
const bit<8> DROP_EXTENDED_ADDR_TO_LEGACY = 0x30;
const bit<8> DROP_FRAG_OFFSET_UNALIGNED   = 0x31;

// Connection class
const bit<2> CONN_UNKNOWN     = 0;
const bit<2> CONN_NEW         = 1;
const bit<2> CONN_ESTABLISHED = 2;

// Traffic class
const bit<4> TCLASS_UNCLASSIFIED = 0;
const bit<4> TCLASS_MANAGEMENT   = 1;
const bit<4> TCLASS_INTERACTIVE  = 2;
const bit<4> TCLASS_BULK         = 3;
const bit<4> TCLASS_REALTIME     = 4;
const bit<4> TCLASS_STORAGE      = 5;

// Threat level
const bit<3> THREAT_NONE              = 0;
const bit<3> THREAT_LOW               = 1;
const bit<3> THREAT_MEDIUM            = 2;
const bit<3> THREAT_HIGH              = 3;
const bit<3> THREAT_AMPLIFICATION     = 4;

// Port type
const bit<1> PORT_TYPE_CORE = 0;
const bit<1> PORT_TYPE_EDGE = 1;

// Meter colors
const bit<2> METER_GREEN  = 0;
const bit<2> METER_YELLOW = 1;
const bit<2> METER_RED    = 2;

// IPv4 TCP option kinds
const bit<8> TCP_OPT_EOL        = 0;
const bit<8> TCP_OPT_NOP        = 1;
const bit<8> TCP_OPT_MSS        = 2;
const bit<8> TCP_OPT_WINDOW     = 3;
const bit<8> TCP_OPT_SACK_PERM  = 4;
const bit<8> TCP_OPT_TIMESTAMP  = 8;

// Fixed header sizes in bytes
const bit<16> IPV4_64_HEADER_SIZE = 32;
const bit<16> TCP_64_HEADER_SIZE  = 24;
const bit<16> UDP_64_HEADER_SIZE  = 10;
const bit<16> IPV4_MIN_HEADER_SIZE = 20;

#endif
