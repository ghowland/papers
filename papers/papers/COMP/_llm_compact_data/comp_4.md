# GEOMETRIC SECURITY — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → primitives → attack_responses → distinctions → verification_properties → claims → relationships → section_index → decode_legend
# Note: source contains two documents on same topic (technical paper + accessible blueprint); both compacted as unified whole

# principles(id|principle|rationale)
P1|Safety by anatomy, not policy|Security derives from structural limitation of what system can do, not rules about who can do what
P2|Vocabulary restriction|Execution engine only unifies logic conforming to six defined primitives; no other operations exist
P3|Zero-negotiation I/O|Network and memory ops governed by strict schema alignment; non-conforming data discarded at hardware/driver level
P4|Monotonic funnel|All external inputs and internal state changes processed as relational transforms of MemDB on single deterministic heartbeat (Update Pump)
P5|Errors are data outliers not execution faults|Arithmetic exceptions return boundary values (MAX or 0); monotonic heartbeat uninterrupted
P6|Authority is static property of infrastructure|No mechanism to create new primitives or widen path-whitelists at runtime; privilege is structural not granted
P7|No detection — no vocabulary for attack expression|System doesn't detect attacks; it provides no vocabulary through which attack can be expressed

# concepts(id|name|category|definition)
C1|Geometric Security|core|Security model where integrity derives from anatomical limitation via monotonic processing funnel within single-address-space; restricts all state transitions to closed set of six primitives
C2|Relational Filter|mechanism|Replaces kernel/user space distinction; all I/O through fixed-size relational schema; geometric shape mismatch = discard
C3|Monotonic Heartbeat|mechanism|Single deterministic Update Pump; all processing occurs on this heartbeat; no interrupt-driven or asynchronous escape paths
C4|Vocabulary Limitation|mechanism|Actor in scene has access only to whitelist of []i32 data paths; six primitives are only available operations; cannot create new primitives or widen whitelist
C5|Geometric Mismatch|mechanism|Data not conforming to expected fixed shape rejected at hardware/driver level; not truncated, not negotiated — dropped
C6|Wall-less paradox|distinction|No traditional kernel/app partitions (experiential freedom) but trapped by six shapes of the room (ontological constraint); wall moved from fence around data to filter around logic
C7|Room with no windows|metaphor|Solid cube with exactly six shaped holes in ceiling; interaction requires matching shape; room physically lacks anatomy for break-in
C8|Burn dead wood|error_handling|Mathematical errors treated as edge-case math returning boundary values; errors consumed not propagated as faults
C9|SIQL|mechanism|Predicate logic (Prolog-style) providing bit-perfect boolean gating; only bit-perfect unification opens gates
C10|Path whitelist|mechanism|[]i32 array defining accessible data paths per scene actor; scenes physically lack vocabulary to reference paths outside whitelist

# primitives(id|name|geometric_shape|what_it_does|security_property)
PR1|Finite State|The Point|Named identity in pre-defined relational table|Prevents undefined/illegal states; actor is "Alive" or "Dead", cannot be "Half-Dead" or "Running Malicious Code"
PR2|Explicit Transition|The Edge|State changes only across directed edges defined in data schema|If transition path not asserted in logic table, transition physically unreachable by processor; no path Guest→Admin = impossible
PR3|Boolean Condition|The Gate|Predicate logic (SIQL) acts as gate requiring absolute unification with local facts (Howland's Axiom)|Only bit-perfect logic opens gate; no partial matches, no fuzzy bypasses
PR4|Utility Selection|The Shunt|Multiplicative utility curves replace imperative branching|Eliminates if-else jump-table surface area; malicious input contributes number to formula, cannot hijack branch
PR5|Atomic Sequence|The Pipe|Logic blocks executed by atomic stack machine|No indirect jumps, no arbitrary memory pointers, no returns, no hidden pointers
PR6|Bounded Effect|The Curve|Time-bounded envelopes for numerical transformation|All mutations within infrastructure-clamped ranges over specific temporal curve; cannot set Health=-99999 instantly

# attack_responses(id|attack_vector|attack_description|geometric_response|why_blocked)
AR1|Buffer overflow|Packet larger than 2048-byte allocation (e.g. 2049 bytes)|Update Pump drops as geometric violation; data never enters room|InboundPacket struct is fixed geometric requirement of driver; no heap, no adjacent memory to corrupt; undersized also rejected
AR2|Privilege escalation|Low-privilege process tricks system into high-privilege execution|No vocabulary for escalation; six primitives cannot create new primitives or widen path-whitelist|Authority is static infrastructure property; no transition path = physically unreachable
AR3|Data exfiltration|Malicious scene reads data from another scene's sector|Scene's []i32 path whitelist physically lacks vocabulary to reference other sector|To the attacker's scene, target data doesn't exist; no door to knock on
AR4|Divide-by-zero crash|Malicious math intended to crash system|Hardware spec returns MAX or 0; dead wood burned, simulation continues|Errors = data outliers not execution faults; monotonic heartbeat uninterrupted
AR5|Code injection|Function pointer or executable payload in packet data|Fixed-type fields (u8 array); atomic stack machine has no indirect jumps or arbitrary memory pointers|Sequence primitive (Pipe) has no mechanism to execute injected code
AR6|Jump-table hijack|Manipulate branching to reach unintended code paths|Utility Selection replaces imperative branching; execution = mathematical ranking of valid candidates|No if-else jump-table surface; malicious input only contributes number to scoring formula

# distinctions(id|side_a|side_b|key_asymmetry)
D1|Policy-based security (permissions, guards, rules)|Geometric security (anatomical limitation, vocabulary restriction)|Choice vs physiological impossibility
D2|Reactive patching (detect and fix)|Structural invariance (no vocabulary for attack)|Arms race vs permanent closure
D3|Flexible I/O negotiation|Strict geometric alignment (zero-negotiation)|Data negotiated vs data must match shape or dropped
D4|Exception/crash error handling|Boundary clamping (burn dead wood)|System failure vs edge-case math
D5|Large security surface (arbitrary code)|Minimal surface (6 primitives only)|Unbounded attack vocabulary vs closed vocabulary
D6|External observability (debuggers/logs)|Inherent observability (text-observable SIQL)|Bolted-on inspection vs structural transparency
D7|Kernel/user space wall (fence around data)|Relational filter (filter around logic)|Partition-based vs vocabulary-based isolation
D8|Permissions (control who)|Geometry (control what computer can do)|Identity-based vs capability-based

# verification_properties(id|property|how_achieved|traditional_approach)
VP1|Memory integrity (buffer overflow protection)|InboundPacket = fixed geometric driver requirement; no heap; pre-sized relational columns; no adjacent memory to corrupt|Software buffer size checks
VP2|Privilege escalation prevention|No vocabulary for escalation; 6 primitives cannot create primitives or widen whitelists; authority = static infrastructure property|Discretionary/mandatory access control policies
VP3|Resilience to exceptional states|Hardware spec returns boundary values (MAX/0) for arithmetic exceptions; errors = data outliers not execution faults|Exception handling, crash recovery
VP4|Exfiltration prevention|Scene path whitelist ([]i32); scene physically cannot reference paths outside whitelist|Sandboxing, network monitoring
VP5|Code injection prevention|Atomic stack machine; no indirect jumps; no arbitrary memory pointers; fixed-type fields|DEP, ASLR, stack canaries

# claims(id|type|claim|basis)
CL1|axiom|Traditional cybersecurity is failed paradigm of policy over behavior|Layering rules on arbitrary code execution = porous; guard can sleep, window can unlatch
CL2|axiom|Security should be physiological impossibility not policy choice|Geometric constraints make exfiltration and escalation anatomically impossible
CL3|derivation|System provides no vocabulary through which attack can be expressed|Six primitives are closed set; none allow creation of new primitives or widening of whitelists
CL4|reframe|Wall moved from fence around data to filter around logic|Wall-less paradox: experiential freedom within ontological constraint
CL5|axiom|"Nothing else ever happens" is physical law not policy|Monotonic funnel + six primitives = only possible operations; structural invariant
CL6|distinction|Errors are edge-case math not system failures|Boundary clamping keeps heartbeat running; no crash path from math errors
CL7|prescription|Stop controlling who uses computer; start controlling what computer is capable of doing|Shift from identity/permission to vocabulary/geometry
CL8|derivation|Geometric security = shift from reactive patching to structural invariance|Fixed mathematical shapes provide deterministic guarantee of safety

# relationships(from|rel|to)
P1|grounds|C1
P2|grounds|C4
P2|enforces|PR1,PR2,PR3,PR4,PR5,PR6
P3|grounds|C2
P3|grounds|C5
P4|grounds|C3
P5|grounds|C8
P6|grounds|C4
P6|prevents|AR2
P7|derives_from|P2
C1|implements|P1
C2|replaces|D7
C2|mechanism_of|P3
C3|mechanism_of|P4
C4|prevents|AR2
C4|prevents|AR3
C5|prevents|AR1
C6|clarifies|D7
C7|metaphor_for|C1
C8|implements|P5
C9|mechanism_of|PR3
C10|mechanism_of|C4
PR1|prevents|AR5
PR2|prevents|AR2
PR3|gates|PR4
PR4|prevents|AR6
PR5|prevents|AR5
PR6|constrains|AR4
AR1|verified_by|VP1
AR2|verified_by|VP2
AR3|verified_by|VP4
AR4|verified_by|VP3
AR5|verified_by|VP5
D1|grounds|CL2
D2|grounds|CL8
D5|derives_from|P2
D7|clarified_by|C6
CL1|motivates|P1
CL2|grounds|P7
CL5|derives_from|P2,P4
CL7|restates|D8

# section_index(section|title|ids)
# Paper 1 (Technical)
1.1|Abstract|C1,P2,P3,C2
1.2|Technical Context: Monotonic Funnel|C2,C3,P4,P2,P3
1.3|Six Computational Primitives|PR1,PR2,PR3,PR4,PR5,PR6
1.4|Verification: Memory Integrity|VP1,AR1
1.4|Verification: Privilege Escalation|VP2,AR2,C4
1.4|Verification: Exceptional States|VP3,AR4,C8
1.5|Summary of Differentiators|D1,D3,D4,D5,D6
1.6|Conclusion|CL8,CL5
# Paper 2 (Blueprint)
2.1|Abstract|CL1,CL2,P1
2.2|Room with No Windows|C7,D1
2.3|Six Primitives (Proof)|PR1,PR2,PR3,PR4,PR5,PR6
2.4|Real-World Examples|AR1,AR3,AR4
2.5|Wall-Less Paradox|C6,D7,CL4
2.6|Conclusion|CL7,D8,CL5

# decode_legend
id_prefixes: P=principle, C=concept, PR=primitive, AR=attack_response, D=distinction, VP=verification_property, CL=claim
primitive_shapes: Point(State)|Edge(Transition)|Gate(Condition)|Shunt(Selection)|Pipe(Sequence)|Curve(Effect)
claim_types: axiom|derivation|observation|prescription|reframe|distinction
rel_types: grounds|enforces|prevents|derives_from|mechanism_of|replaces|clarifies|metaphor_for|implements|gates|constrains|verified_by|clarified_by|motivates|restates
error_handling: boundary_clamping — arithmetic exceptions return MAX or 0; errors = data outliers not execution faults
io_model: zero-negotiation — data must match fixed geometric shape or dropped at hardware/driver level; no truncation, no partial accept
authority_model: static — []i32 path whitelists; cannot create primitives or widen whitelists at runtime
source_note: two documents compacted as unified whole; section_index uses 1.x for technical paper, 2.x for blueprint
