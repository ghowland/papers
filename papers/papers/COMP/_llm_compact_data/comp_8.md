# SILOSEC PROTOCOL SPECIFICATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → rejected → primitives → wire_format → handshake → data_transmission → invariants → comparisons → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Frozen protocol: version 1, never changes|No negotiation, no upgrades, no version management; if changes needed, fork as SiloSec2 and run parallel
P2|Identity = Ed25519 public key|No certificates, no PKI, no expiration, no renewal; 32-byte permanent identity
P3|Trust On First Use (TOFU)|First contact establishes identity binding; out-of-band verification for high-assurance
P4|One cipher suite: AES-256-GCM, no options|Cipher agility adds complexity for zero security benefit; if AES-256-GCM broken, all crypto is broken
P5|IP layer encryption|Encrypts ALL traffic (TCP/UDP/ICMP/custom) to peer; single handshake per peer not per connection; in 1-process OS, IP layer IS application layer
P6|Silo-only; legacy gets plaintext or rejection|Only Silo machines speak SiloSec; no backward compatibility with TLS/IPSec
P7|Zero external dependencies|All crypto from Zig stdlib (std.crypto); no C code, no binary blobs; ~500 lines total
P8|$200 CPU constraint|Pure software, no hardware crypto required, no proprietary drivers; runs anywhere
P9|Fail-closed: invalid packets silently discarded|No state mutation, no downgrade, no error signaling, no information leakage from invalid input
P10|Mandatory encryption from first packet|No plaintext fallback, no negotiation, no compatibility mode

# concepts(id|name|category|definition)
C1|SiloSec|core|Silo-to-Silo encrypted communication protocol; IP layer; frozen v1; X25519+Ed25519+AES-256-GCM; ~500 lines Zig
C2|Identity|core|Ed25519 public key (32 bytes); permanent; serves as both authentication credential and peer identifier; persisted to disk as /SILO.KEY
C3|Ephemeral keypair|crypto|X25519 keypair generated fresh per handshake; provides forward secrecy; MUST be random, NEVER reused
C4|Shared secret|crypto|32-byte result of X25519 DH exchange; used as AES-256-GCM key; unique per session
C5|Nonce|crypto|12 bytes: 8-byte counter (little-endian) + 4-byte random; MUST NEVER repeat for same key; counter ensures ordering, random prevents collision on reset
C6|Authentication tag|crypto|16-byte GCM tag; detects tampering; fails fast on invalid
C7|Inner IP packet|wire|Complete IP packet (including IP header) encrypted as payload; receiver decrypts and re-processes normally
C8|Peer|runtime|Known Silo endpoint: IP + identity + shared_secret + tx_counter + rx_counter + verified flag
C9|TOFU binding|trust|First contact stores peers[IP] = identity; future connections from that IP MUST match; mismatch = SECURITY ALERT
C10|Cardinality thrash protection|design|Only decrypt from known peers; drop unknown peers immediately; GCM fails fast on invalid tag

# rejected(id|technology|reason|code_size|why_fatal)
RJ1|HTTPS/TLS|~28,500 lines minimum; requires X.509/ASN.1/RSA/PKI infrastructure; certificate authority trust; cipher negotiation|~15,000 lines (BearSSL: 50KB C)|Unauditable; "50kb of C, rejecting, too big"
RJ2|IPSec|~8,000 lines; requires IKEv2 with same RSA/X.509 as TLS; all-or-nothing encryption; debugging nightmare|~8,000 lines|Not simpler than TLS; complexity in different clothes
RJ3|SSH tunnels/proxies|Assumes host OS exists; delegates complexity elsewhere|n/a|Violates premise: Silo IS computing, no host OS to tunnel through
RJ4|Application-layer encryption only|Leaves key exchange unsolved; no authentication; no replay protection; no forward secrecy; manual key management|minimal|Insufficient for secure networking primitive
RJ5|BearSSL|50KB compiled C; 15,000 lines unauditable; binary blob|50KB/15,000 lines|Defeats minimal auditable OS principle

# primitives(id|primitive|zig_path|purpose|properties)
PR1|X25519|std.crypto.dh.X25519|Ephemeral key exchange for forward secrecy|128-bit security; constant-time; 32-byte keys; ~50,000 ops/sec on $200 CPU
PR2|Ed25519|std.crypto.sign.Ed25519|Peer authentication and identity|128-bit security; constant-time; 32-byte public keys; 64-byte signatures; deterministic
PR3|AES-256-GCM|std.crypto.aead.aes_gcm.Aes256Gcm|Authenticated encryption of data packets|256-bit key; 12-byte nonce; 16-byte auth tag; detects tampering; HW accel ~10Gbps, SW ~1Gbps

# wire_format(id|component|size|contents)
WF1|IPv4 header|20 bytes|Standard; protocol field = 99 (reserved/experimental)
WF2|SiloSec header|48 bytes|Version (1 byte, always 0x01) + Type (1 byte) + Reserved (2 bytes) + Sender Identity (32 bytes, Ed25519 pubkey) + Nonce (12 bytes)
WF3|Encrypted payload|variable|Complete inner IP packet encrypted with AES-256-GCM
WF4|Authentication tag|16 bytes|GCM auth tag
# Packet types: 0x01=HANDSHAKE_INIT, 0x02=HANDSHAKE_RESPONSE, 0x03=DATA
# Total overhead: 84 bytes per packet (outer IP 20 + SiloSec header 48 + auth tag 16)
# Effective inner MTU: 1416 bytes (1500 - 84); TCP/UDP payload: 1396 bytes (1416 - 20 inner IP)

# handshake(id|step|actor|action|payload)
HS1|Generate ephemeral|Alice|X25519 keygen → secret_A, public_A|—
HS2|Sign ephemeral|Alice|Ed25519_sign(public_A ∥ Bob_IP, identity_A) → sig_A|Including peer_IP prevents replay across connections
HS3|Send INIT|Alice→Bob|HANDSHAKE_INIT packet|identity_A (in header) + public_A (32 bytes) + sig_A (64 bytes) = 96 bytes unencrypted
HS4|Verify signature|Bob|Ed25519_verify(sig_A, public_A ∥ Bob_IP, identity_A)|Reject if invalid
HS5|Generate ephemeral|Bob|X25519 keygen → secret_B, public_B|—
HS6|Compute shared secret|Bob|X25519_DH(secret_B, public_A) → shared|—
HS7|Sign ephemeral|Bob|Ed25519_sign(public_B ∥ Alice_IP, identity_B) → sig_B|—
HS8|Send RESPONSE|Bob→Alice|HANDSHAKE_RESPONSE packet|identity_B (in header) + public_B (32 bytes) + sig_B (64 bytes) = 96 bytes unencrypted
HS9|Verify signature|Alice|Ed25519_verify(sig_B, public_B ∥ Alice_IP, identity_B)|Reject if invalid
HS10|Compute shared secret|Alice|X25519_DH(secret_A, public_B) → shared|Same shared secret as Bob computed
# Result: both sides have shared_secret (32 bytes) + peer_identity (32 bytes); authenticated forward-secret channel

# security_properties(id|property|mechanism|what_it_prevents)
SP1|Mutual authentication|Both parties sign ephemeral key with identity key|Impersonation
SP2|Forward secrecy|Ephemeral X25519 keys per session; compromise of long-term keys doesn't reveal past traffic|Past traffic decryption after key compromise
SP3|Replay protection (handshake)|Signatures include peer IP; ephemeral keys are random|Cross-connection replay
SP4|Replay protection (data)|Nonce uniqueness (counter + random); GCM auth fails on reuse|Packet replay
SP5|MITM protection|Attacker cannot forge Ed25519 signatures; TOFU binds identity to IP|Man-in-the-middle (after first contact)
SP6|Tamper detection|GCM authentication tag; any bit flip detected|Packet modification

# threat_model(id|scope|items)
TM1|In scope|Eavesdropping (passive); packet tampering (active); replay attacks; impersonation
TM2|Out of scope|Physical machine access; side-channel attacks (timing, power); quantum computers (breaks X25519/Ed25519 in 20+ years)

# tofu_limitations(id|scenario|consequence|mitigation)
TF1|MITM on first contact|Eve intercepts first connection; Alice stores Eve's identity as Bob's; Eve can MITM all traffic|Out-of-band identity verification (in person, phone)
TF2|Acceptable because|Gaming between friends; small trusted networks; not replacing TLS for anonymous web browsing|Use case is peer-to-peer among known parties

# v2_invariants(id|invariant|rules|guarantee)
IV1|Fail-closed|Any non-conforming packet silently discarded; no state mutation, downgrade, error signaling, or information leakage|No invalid packet causes side effects
IV2|Mandatory encryption|All Silo-to-Silo encrypted from first packet; no plaintext fallback/negotiation/compatibility|Plaintext Silo-to-Silo never accepted
IV3|Monotonic counters|All wire counters strictly monotonic; never reused; no rollback; no wraparound|Replay, reflection, state regression detectable and rejected
IV4|Windowed acceptance|Packets accepted only within strict forward-only receive window; below or above rejected; window advances only on valid|Replay outside window rejected with bounded memory and constant-time
IV5|Epoch isolation|Each packet belongs to exactly one crypto epoch; epoch change = key change; old epoch packets invalid immediately; no grace periods|Key reuse, cross-epoch replay, mixed-state decryption impossible
IV6|Rekey bounding|Rekey after N packets or T time (whichever smaller); either side may request; excessive rekey = hostile|Exposure from compromised keys bounded in time and packet count
IV7|State continuity (echoed counter)|Endpoints maintain internal session counter; cryptographically protected; peer echoes expected counter in encrypted payload; mismatch → drop|Desynchronization, reflection, mid-path interference detected immediately
IV8|Stateless handshake (SYN-cookie)|No unverified packet causes unbounded state allocation; initial handshakes statelessly verifiable; state allocated only after bidirectional proof|Handshake DoS bounded and predictable
IV9|Flow binding (5-tuple)|All wire security state bound to (src IP, dst IP, src port, dst port, protocol); no migration across flows; flow change = new session|Cross-flow injection and session confusion impossible
IV10|Downgrade resistance|No negotiation; no feature fallback; no partial enablement|Attacker cannot force plaintext, legacy modes, or reduced protections
IV11|Resource bounding|Bounded memory per flow; bounded CPU per packet; constant-time rejection|Wire security not a DoS vector
IV12|Silent failure|No error packets; no logging on hot paths; no recovery signaling|Failure doesn't leak information or amplify attacks

# v2_non_guarantees
# SiloSec wire security does NOT guarantee: peer identity verification, peer trustworthiness, authorization correctness, traffic analysis resistance, protection against compromised endpoints
# These concerns belong above the wire layer

# comparisons(id|vs|silosec_advantage|silosec_limitation)
CM1|TLS 1.3|~500 vs ~15,000 lines; no certificates; no cipher negotiation; all IP traffic not just TCP; frozen version|Not suitable for anonymous web browsing; TOFU not PKI
CM2|IPSec|16x less code; no IKEv2 complexity; no certificate infrastructure; single cipher; actually auditable; designed for 1-process OS|No NAT traversal; no SA management
CM3|WireGuard|Simpler (~500 vs ~4,000 lines); no pre-shared keys; no config files; identity = public key|WireGuard better for VPN, NAT traversal, mobile roaming

# implementation_files(id|file|purpose)
IM1|silosec.zig|Main SiloSec: init, handshake, encrypt/decrypt, peer management, persistence
IM2|ip.zig|IP layer with protocol 99 hook; processDecryptedPacket callback
IM3|net.zig|Network core
IM4|kernel.zig|Initialization; identity load/generate

# network_stack_layers
# Application → Transport (TCP/UDP) → SiloSec (encrypt/decrypt) → Internet (IP/ICMP) → Link (Ethernet/ARP) → Hardware
# SiloSec transparent to upper layers; TCP/UDP don't know encryption exists

# critical_pitfalls(id|pitfall|wrong|correct|consequence_of_wrong)
CP1|Nonce management|Pure random every time (may repeat)|Counter (u64 LE) + random (4 bytes); counter increments per packet|GCM nonce reuse leaks plaintext XOR (catastrophic)
CP2|Encrypt scope|UDP payload only|Complete inner IP packet including headers|Leaks IP addresses, ports, packet sizes, timing
CP3|Identity verification|Skip header.sender_id check|Verify header.sender_id == peer.identity on every packet|Attacker can send packets with spoofed identity
CP4|Ephemeral key reuse|Fixed or reused ephemeral secret|New random ephemeral every handshake|Broken forward secrecy
CP5|Error handling|Send error packets; log on hot path|Silent drop; no error signaling|Information leakage; oracle attacks; DoS via log flooding

# errors(id|error|meaning|response)
ER1|UnknownPeer|No handshake with this IP|Initiate handshake if trusted; reject if not
ER2|IdentityMismatch|Sender identity doesn't match known peer|SECURITY ALERT — possible MITM
ER3|DecryptionFailed|GCM auth tag verification failed|Drop silently (likely tampered)
ER4|SignatureInvalid|Ed25519 signature invalid|Reject handshake (possible attack)
ER5|HandshakeFailed|Handshake protocol error|Drop; do not allocate state
ER6|PayloadTooLarge|Payload exceeds MTU|Fragment or reject

# dos_mitigations(id|attack|mitigation)
DM1|Handshake flooding|Rate limit per source IP; drop if CPU > 80%; proof-of-work (future)
DM2|Ciphertext flooding|Only decrypt from known peers; drop unknown immediately; GCM fails fast on invalid tag

# future_enhancements(id|feature|note)
FE1|Identity rotation|Generate new, notify peers, grace period for old
FE2|Peer discovery protocol|LAN multicast announcement; TOFU confirmation
FE3|Replay protection window|Sliding window of recent nonces
FE4|Performance monitoring|Stats struct: handshakes, packets, bytes, failures
FE5|Multi-path support|Same peer reachable via multiple IPs; same shared_secret
# All future; NOT v1; keep v1 simple

# claims(id|claim|type|depends_on)
CL1|In 1-process OS where kernel IS application, SiloSec can operate at IP layer without kernel integration|derivation|P5,P8
CL2|We only need to encrypt Silo-to-Silo; legacy gets plain HTTP or nothing|axiom|P6
CL3|Zig stdlib contains all necessary primitives; zero external dependencies|observation|P7,PR1,PR2,PR3
CL4|Cipher agility adds complexity for zero security benefit|axiom|P4
CL5|IPSec is not simpler than TLS; complexity dressed in different clothes|observation|RJ2
CL6|~500 lines of auditable Zig replaces ~28,500 lines of TLS or ~8,000 lines of IPSec|observation|P7,CM1,CM2
CL7|SiloSec wire security guarantees: accepted packets are fresh, correctly ordered, cryptographically valid for current epoch, bound to single flow, part of continuous verifiable session state; all others dropped without side effects|derivation|IV1-IV12
CL8|TOFU is acceptable for Silo use case (gaming, small trusted networks, not anonymous web)|boundary|TF1,TF2

# rules(id|rule|rationale)
R1|Nonce = counter (u64 LE) + random (4 bytes); counter increments every packet|GCM security proof requires nonce uniqueness; reuse is catastrophic
R2|Encrypt complete inner IP packet including headers|Encrypting payload only leaks addresses, ports, sizes, timing
R3|Verify sender identity on every DATA packet|header.sender_id must match stored peer.identity; prevents spoofing
R4|Generate fresh random ephemeral keypair for every handshake|Reusing ephemeral keys breaks forward secrecy
R5|Handle errors silently: no error packets, no hot-path logging|Prevents oracle attacks, information leakage, DoS via log flooding
R6|Only decrypt packets from known peers; drop unknown immediately|Prevents CPU exhaustion from ciphertext flooding
R7|Sign ephemeral key with peer_IP included in message|Prevents handshake replay across different connections
R8|Store ephemeral secret during pending handshake; needed to complete DH on response|Losing ephemeral secret = cannot compute shared secret
R9|Protocol is frozen at v1; changes require new protocol (SiloSec2)|Simpler than in-band version negotiation

# relationships(from|rel|to)
P1|defines|C1
P2|defines|C2
P3|defines|C9
P4|selects|PR3
P5|determines|WF1,WF2,WF3
P6|constrains|C1
P7|selects|PR1,PR2,PR3
P9|defines|IV1,IV12
P10|defines|IV2
PR1|used_in|HS1,HS5,HS6,HS10
PR2|used_in|HS2,HS4,HS7,HS9
PR3|used_in|WF3,WF4
C2|authenticated_by|PR2
C3|exchanged_via|PR1
C3|provides|SP2
C4|derived_from|C3
C5|critical_for|PR3
C7|encrypted_by|PR3
C9|vulnerable_to|TF1
SP1|provided_by|PR2
SP2|provided_by|C3
SP3|provided_by|R7
SP4|provided_by|C5
SP5|provided_by|PR2,C9
SP6|provided_by|C6
IV1|implements|P9
IV2|implements|P10
IV3|prevents|replay
IV5|prevents|key_reuse
IV8|prevents|handshake_DoS
IV10|implements|P4
RJ1|rejected_for|P7,P8
RJ2|rejected_for|P7
RJ3|rejected_for|silo_is_computing
RJ4|rejected_for|insufficient_security
RJ5|rejected_for|P7
CP1|violates|R1
CP2|violates|R2
CP3|violates|R3
CP4|violates|R4
CP5|violates|R5

# section_index(section|title|ids)
Philosophy|Philosophy and Motivation|P1-P10,CL1,CL2,CL3
Rejected|What We Rejected|RJ1-RJ5,CL5
Protocol Design|Core Design|P1,P2,P3,P4,P5,P6
Primitives|Cryptographic Primitives|PR1,PR2,PR3
Wire Format|Wire Format|WF1-WF4
Handshake|Handshake Protocol|HS1-HS10,SP1-SP6
Data Transmission|Data Transmission|C5,C7,R1,R2
Implementation|Implementation Guide|IM1-IM4,CP1-CP5,ER1-ER6
Integration|Silo OS Integration|network_stack_layers
Security|Security Considerations|TM1,TM2,TF1,TF2,DM1,DM2,SP1-SP6
V2 Invariants|Wire-Security Invariants|IV1-IV12
Comparisons|Comparison to Alternatives|CM1-CM3
Future|Future Enhancements|FE1-FE5

# decode_legend
packet_types: 0x01=HANDSHAKE_INIT|0x02=HANDSHAKE_RESPONSE|0x03=DATA
ip_protocol: 99 (reserved/experimental)
crypto_suite: X25519(key exchange)+Ed25519(authentication)+AES-256-GCM(encryption) — all from std.crypto
nonce_format: bytes[0:8]=counter(u64 LE)+bytes[8:12]=random(u32)
wire_overhead: 84 bytes (outer IP 20 + SiloSec header 48 + auth tag 16)
effective_mtu: inner IP 1416 bytes; TCP/UDP payload 1396 bytes
trust_model: TOFU — first contact binds identity to IP; out-of-band verification for high assurance
forward_secrecy: ephemeral X25519 per session; long-term key compromise doesn't reveal past traffic
error_philosophy: silent drop; no error packets; no hot-path logging
version_philosophy: frozen v1; changes = new protocol (SiloSec2)
category_values: core|crypto|wire|runtime|trust|design|failure_mode
claim_types: axiom|derivation|observation|boundary
rel_types: defines|selects|determines|constrains|used_in|authenticated_by|exchanged_via|provides|derived_from|critical_for|encrypted_by|vulnerable_to|provided_by|implements|prevents|rejected_for|violates
v2_scope: wire-security only; identity/trust/authorization/policy explicitly out of scope
+standalone: this doc self-contained