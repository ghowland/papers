# GEOMETRIC SECURITY (COMP-4 + COMP-5) — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → six_primitives → security_properties → partial_geo → comparison → relationships → sections

# principles(id|principle|rationale)
P1|Safety by anatomy not policy|Security derives from structural limitation of what the system can express; no vocabulary for attacks means no attacks possible
P2|Vocabulary restriction|Execution engine only unifies logic conforming to six defined primitives; no mechanism to create new primitives or widen capabilities
P3|Shape before meaning|Untrusted input is never interpreted as logic, only as geometry; must conform exactly to predefined memory shape or be dropped
P4|Monotonic funnel|All external inputs and internal state changes processed as relational transforms through fixed-size relational filter; replaces kernel/user space distinction
P5|Errors are data outliers not execution faults|Arithmetic exceptions (divide-by-zero) return defined boundary values; monotonic heartbeat remains uninterrupted
P6|Partial geometric security is immediately deployable|Sealing ingress boundary alone eliminates entire exploit classes; works in unsafe languages (C/C++) as a shim without language changes, kernel mods, or rewrites

# claims(id|claim|type|depends_on)
CL1|Buffer overflow is structurally impossible — no adjacent memory exists to corrupt, no heap during ingress|derivation|P3,SP1
CL2|Privilege escalation requires vocabulary that does not exist; authority is static property of infrastructure|derivation|P2,SP3
CL3|System cannot enter undefined states — all states are named identities in predefined relational tables|derivation|PR1
CL4|If transition path not asserted in logic table, transition is physically unreachable by processor|derivation|PR2
CL5|Partial geometric security does not eliminate: side-channel attacks, denial of service, logic flaws, data poisoning, semantic manipulation|observation|
CL6|None of the remaining vulnerabilities in partial model permit arbitrary code execution, memory disclosure, or privilege escalation|derivation|CL5,P3

# concepts(id|name|definition|category)
C1|Geometric security|Security model where integrity is invariant of system geometry — computational vocabulary limited to six primitives, I/O through fixed geometric shapes|model
C2|Relational filter|Replaces kernel/user space distinction; strict schema alignment governs all I/O; data not conforming to expected geometric shape discarded at hardware/driver level|mechanism
C3|Update pump|Single deterministic heartbeat processing all inputs and state changes as relational transforms of memory-mapped database (MemDB)|mechanism
C4|Zero-negotiation I/O|Network and memory operations governed by strict schema alignment; no recovery path, partial acceptance, truncation, or negotiation|mechanism
C5|Monotonic heartbeat|Continuous uninterruptible execution cycle; errors treated as edge-case math not system failures; boundary clamping instead of exception/crash|property
C6|Partial geometric security|Subset enforcing geometric invariants at ingress boundary only; eliminates buffer overflow, injection, parser confusion while remaining compatible with existing stacks|model
C7|Ingress shim|Fixed-size struct buffers at I/O boundary; exact byte count required; no variable-length fields, no pointers, no nested allocations; reject-on-mismatch is binary|mechanism
C8|Wall-less paradox|No traditional kernel/app partitions, but freedom is experiential not ontological — wall moved from fence around data to filter around logic; trapped by six shapes|concept
C9|SIQL|Predicate logic acting as boolean gate; movement through funnel requires absolute unification with local facts (Howland's Axiom)|mechanism

# six_primitives(id|name|shape_metaphor|definition|security_function)
PR1|Finite State|The Point|State as named identity in predefined relational table; cannot enter undefined or illegal states|Prevents undefined state execution
PR2|Explicit Transition|The Edge|State changes only across directed edges defined in data schema; undefined transitions physically unreachable|Eliminates arbitrary control flow
PR3|Boolean Condition|The Gate|SIQL predicate logic requiring absolute unification with local facts to permit passage|Prevents unauthorized state transitions
PR4|Utility Selection|The Shunt|Multiplicative utility curves replace if-else branching; execution path is mathematical ranking of all valid candidates|Eliminates jump-table attack surface
PR5|Atomic Sequence|The Pipe|Atomic stack machine with no indirect jumps, no returns, no arbitrary memory pointers|Prevents code injection and ROP
PR6|Bounded Effect|The Curve|Time-bounded envelopes clamp all mutations to infrastructure-defined ranges over temporal curves|Prevents instant state corruption

# security_properties(id|property|mechanism|attack_eliminated)
SP1|Memory integrity|InboundPacket is fixed geometric requirement of driver; oversized/undersized packets rejected as geometric mismatch by DMA/Update Pump; no heap in traditional sense — pre-sized relational columns|Buffer overflow, memory adjacency corruption
SP2|Injection resistance|Input cannot introduce new execution paths, control instruction pointers, or select function calls; six primitives are only available operations|Code injection, ROP, arbitrary code execution
SP3|Authority containment|Actor only has access to whitelist of data paths; no primitive allows creation of new primitives or widening of path whitelist|Privilege escalation
SP4|Exfiltration resistance|Output paths equally shape-restricted; no reflective serialization; data not already visible cannot be leaked|Data exfiltration
SP5|Arithmetic resilience|Divide-by-zero returns MAX or 0; errors are data outliers not execution faults|Crash-inducing math exploits

# partial_vs_full(aspect|full_geometric|partial_geometric)
Ingress sealed|Yes|Yes
Interpretation sealed|Yes|No
Control flow sealed|Yes|No
State transitions sealed|Yes|No
Execution vocabulary sealed|Yes|No
Buffer overflow eliminated|Yes|Yes
Injection eliminated|Yes|Yes
Privilege escalation eliminated|Yes|Yes
Exfiltration eliminated|Yes|Yes (output shape-restricted)
Side-channel protection|N/A (different concern)|No
Logic flaw protection|No|No
Requires language changes|Yes (full Silo)|No
Requires kernel modifications|Yes|No
Deployable as shim|No (full architecture)|Yes
Compatible with C/C++|No (requires Silo)|Yes

# ingress_shim_spec(rule|description)
Fixed-size buffers|All ingress through fixed-size structs; exact byte count required
No variable fields|No variable-length fields, no pointers, no nested allocations, no flexible array members
Binary reject|Exact struct map → copy into RAM; any mismatch → drop packet; includes wrong size, invalid ranges, failed checksums, malformed headers
No re-parsing|After ingress, raw byte buffers never accessed again; logic reads only validated struct fields
No string interpretation|No re-parsing, no pointer arithmetic derived from input
Dropped input isolation|Dropped input never touches application memory

# partial_threat_model(category|addressed|not_addressed)
Buffer overflows|Yes|—
Length confusion|Yes|—
Parser differentials|Yes|—
Injection attacks|Yes|—
Type confusion|Yes|—
Memory adjacency corruption|Yes|—
Side-channel attacks|—|Not addressed (timing, cache, speculation)
Denial of service|—|Not addressed (availability)
Logic flaws|—|Not addressed (semantic correctness)
Data poisoning|—|Not addressed (valid but malicious values)

# comparison(vector|traditional|geometric_full|geometric_partial)
Integrity enforcement|Policy-based (permissions)|Anatomical (vocabulary limit)|Structural at ingress (shape validation)
Error handling|Exception/crash|Boundary clamping|Boundary clamping at ingress
Security surface|Large (arbitrary code)|Minimal (6 primitives)|Narrow (shape-validated structs)
I/O processing|Flexible negotiation|Strict geometric alignment|Strict geometric alignment at boundary
Buffer safety|Runtime checks|Structural impossibility|Structural impossibility
Injection|Filtered|Unexpressible|Unexpressible
Exploit surface|Large|Minimal|Narrow
Deployability|N/A|Full architecture required|Shim-level, minimal cost
Observability|External (debuggers/logs)|Inherent (text-observable SIQL)|Partial (struct validation observable)

# implementation_cost(requirement|partial_geo|full_geo)
Ingress shim per I/O boundary|Yes|Yes (integrated)
Fixed struct definitions|Yes|Yes (relational columns)
Copy-or-drop semantics|Yes|Yes (Update Pump)
Language changes|No|Yes
Memory-safe runtimes|No|Yes (Silo runtime)
Kernel modifications|No|Yes (replaces kernel)
Application rewrites|No|Yes (full Silo port)

# relationships(from|rel|to)
P1|grounds|C1
P1|grounds|C6
P2|implements|PR1
P2|implements|PR2
P2|implements|PR3
P2|implements|PR4
P2|implements|PR5
P2|implements|PR6
P3|implements|C7
P3|implements|C4
P4|implements|C2
P4|implements|C3
P5|implements|SP5
P5|implements|C5
P6|enables|C6
P6|enables|C7
C1|contains|PR1
C1|contains|PR2
C1|contains|PR3
C1|contains|PR4
C1|contains|PR5
C1|contains|PR6
C1|superset_of|C6
C2|implements|P4
C3|implements|C5
C4|implements|P3
C6|subset_of|C1
C6|implements|C7
C7|enables|SP1
C7|enables|SP2
C7|enables|SP3
C7|enables|SP4
C8|describes|C2
C9|implements|PR3
PR1|prevents|CL3
PR2|prevents|CL4
PR4|eliminates|jump-table attack surface
PR5|prevents|SP2
PR6|prevents|SP5
SP1|eliminates|buffer overflow
SP2|eliminates|code injection
SP3|eliminates|privilege escalation
SP4|eliminates|data exfiltration
CL5|constrains|C6
CL6|derives_from|CL5

# section_index(section|title|ids|source)
1|Abstract|C1,P1|COMP-4
2|Monotonic Funnel|C2,C3,C4,P4|COMP-4
3|Six Primitives|PR1-PR6,P2|COMP-4
4|Security Properties|SP1-SP5,CL1-CL4|COMP-4
5|Summary/Differentiators|comparison|COMP-4
Abstract|Partial Geometric Security|C6,P6,P3|COMP-5
2|Threat Model|partial_threat_model,CL5,CL6|COMP-5
3|Shape Before Meaning|P3,C7|COMP-5
4|Ingress Shim|C7,ingress_shim_spec|COMP-5
5|Post-Ingress Rule|no re-parsing|COMP-5
6|Security Properties Achieved|SP1-SP4 (partial context)|COMP-5
7|What Remains Vulnerable|CL5,CL6|COMP-5
8|Comparison|comparison|COMP-5
9|Implementation Cost|implementation_cost|COMP-5
10|Relationship to Full|partial_vs_full|COMP-5

# decode_legend
format: pipe-delimited tables, ID-based cross-references
source_papers: COMP-4 (Geometric Security — full model) + COMP-5 (Partial Geometric Security — ingress-only)
parent_framework: HOWL-COMP-1-2026 (Silo architecture)
six_primitives: PR1 State|PR2 Transition|PR3 Condition|PR4 Selection|PR5 Sequence|PR6 Effect
security_model: full = all six primitives + sealed execution; partial = ingress shape validation only
key_mechanism_full: relational filter replaces kernel/user space; update pump as monotonic heartbeat; SIQL predicate logic
key_mechanism_partial: fixed-size struct buffers at I/O boundary; binary reject-on-mismatch; no re-parsing post-ingress
attack_classes_eliminated: buffer overflow|injection|privilege escalation|exfiltration|parser confusion|type confusion|length confusion
attack_classes_not_addressed_partial: side-channel|DoS|logic flaws|data poisoning|semantic manipulation
wall_less_paradox: no kernel/app partition but constrained by six shapes; freedom is experiential not ontological
partial_deployability: shim-level; no language changes, no kernel mods, no rewrites; works in C/C++
rel_types: grounds|implements|contains|superset_of|subset_of|enables|prevents|eliminates|describes|constrains|derives_from
+standalone: no cross-references to other compact docs
