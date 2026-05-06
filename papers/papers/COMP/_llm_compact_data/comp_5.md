# PARTIAL GEOMETRIC SECURITY — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → threat_model → ingress_rules → security_properties → remaining_vulnerabilities → distinctions → implementation → claims → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Shape before meaning|Untrusted input never interpreted as logic, only as geometry
P2|Conform exactly or drop|All ingress data must match predefined memory shape exactly; no recovery, partial acceptance, truncation, or negotiation
P3|Structural reduction of exploitability|Goal is eliminating exploit classes structurally, not achieving semantic correctness
P4|Seal ingress boundary|Partial approach: enforce geometric invariants at I/O boundaries only; leaves interpretation/control flow/state/execution to application
P5|Structs only after ingress|Raw byte buffers never accessed after validation; logic reads only validated struct fields; no re-parsing, no string interpretation, no pointer arithmetic from input

# concepts(id|name|category|definition)
C1|Partial Geometric Security|core|Subset of full Geometric Security; enforces geometric invariants at system ingress only; eliminates buffer overflows, parser confusion, injection while compatible with existing unsafe stacks
C2|Ingress shim|mechanism|Single validation layer per I/O boundary; fixed-shape buffers; copy-or-drop semantics; dropped input never touches application memory
C3|Fixed-shape buffer|mechanism|Exact byte count required; no variable-length fields, no pointers, no nested allocations, no flexible array members
C4|Reject-on-mismatch|mechanism|Binary decision: struct maps exactly → copy into RAM; any mismatch → drop packet; includes wrong size, invalid ranges, failed checksums, malformed headers
C5|Structural impossibility|property|Security property achieved through absence of mechanism rather than policy enforcement; system lacks vocabulary to express exploit
C6|Structural refusal|framing|Security reframed from reactive defense to structural refusal; if attack cannot be expressed, it cannot succeed

# threat_model(id|category|status|detail)
TM1|Buffer overflows|eliminated|Fixed-shape buffers; no adjacent memory to corrupt; no heap interaction during ingress
TM2|Length confusion|eliminated|Exact byte count required; 2047 and 2049 both rejected for 2048-byte buffer
TM3|Parser differentials|eliminated|No parsing; shape-validate or drop; no re-parsing after ingress
TM4|Injection attacks|eliminated|Input cannot introduce execution paths, control instruction pointers, or select function calls/jumps
TM5|Type confusion|eliminated|Fixed struct fields; no reinterpretation of input bytes
TM6|Memory adjacency corruption|eliminated|No heap interaction; pre-sized buffers; no adjacent memory exists to corrupt
TM7|Side-channel attacks|NOT eliminated|Timing, cache, speculation; design/operations problem not structural security failure
TM8|Denial of service|NOT eliminated|Availability attacks (flooding); design/operations problem
TM9|Data poisoning|NOT eliminated|Valid but malicious values accepted; semantic manipulation possible
TM10|Logic flaws|NOT eliminated|Bad business rules; semantic correctness outside scope
# Key: none of TM7-TM10 permit arbitrary code execution, memory disclosure, or privilege escalation

# ingress_rules(id|rule|detail)
IR1|Exact byte count required|No variable-length acceptance
IR2|No variable-length fields|All fields fixed size in struct
IR3|No pointers in ingress structs|All values inline
IR4|No nested allocations|Flat structure only
IR5|No flexible array members|C99 FAMs prohibited
IR6|Drop on any mismatch|Wrong size, invalid ranges, failed checksums, malformed headers all drop
IR7|Dropped input never touches application memory|Rejection happens before copy to application space
IR8|No re-parsing after ingress|Raw byte buffers never accessed again; logic reads validated struct fields only
IR9|No string interpretation post-ingress|Eliminates injection surface
IR10|No pointer arithmetic derived from input|Input values cannot compute memory addresses

# security_properties(id|property|how_achieved)
SP1|Memory safety (structural)|No buffer overflow possible; no adjacent memory to corrupt; no heap interaction during ingress
SP2|Injection resistance|Input cannot introduce new execution paths; no input controls instruction pointers or selects function calls/jumps
SP3|Authority containment|Input cannot widen privileges or access unreachable memory; escalation requires vocabulary that does not exist
SP4|Exfiltration resistance|Output paths equally shape-restricted; no reflective serialization; data not already visible cannot be leaked

# distinctions(id|side_a|side_b|key_asymmetry)
D1|Parse and sanitize (traditional input handling)|Shape-validate or drop (partial geometric)|Interpretation vs geometry; negotiation vs binary accept/reject
D2|Runtime buffer checks|Structural impossibility of overflow|Software enforcement vs anatomical absence
D3|Injection filtered (traditional)|Injection unexpressible (geometric)|Policy removes known patterns vs vocabulary lacks expression capacity
D4|Large exploit surface (traditional)|Narrow exploit surface (geometric)|Arbitrary code paths vs fixed-shape ingress only
D5|High cost complex deployment (traditional)|Minimal cost shim-level deployment (geometric)|Application rewrites vs one shim per I/O boundary
D6|Full Geometric Security (seals ingress + interpretation + control flow + state + execution)|Partial Geometric Security (seals ingress only)|Perfect structural closure vs massive improvement with near-zero friction

# implementation(id|requires|does_not_require)
IM1|One ingress shim per I/O boundary|Language changes
IM2|Fixed struct definitions|Memory-safe runtimes
IM3|Strict copy-or-drop semantics|Kernel modifications
IM4|—|Application rewrites
# Viable for legacy C/C++ systems; deployable as shim

# claims(id|type|claim|basis)
CL1|axiom|Untrusted input is never interpreted as logic, only as geometry|Core invariant; single rule that collapses exploit surface
CL2|axiom|If attack cannot be expressed, it cannot succeed|Structural refusal framing; vocabulary absence = security
CL3|derivation|Partial geometric security eliminates buffer overflows, parser confusion, injection in unsafe languages|Fixed-shape ingress + structs-only post-ingress + no re-parsing
CL4|observation|Policy enforcement over arbitrary execution fails because system retains vocabulary to express exploits|Decades of patching demonstrate paradigm failure
CL5|distinction|Partial is not perfect but provides massive improvement with near-zero friction|Seals ingress only; leaves interpretation/control flow/state/execution open
CL6|prescription|Security does not require perfect systems to be effective|Partial approach eliminates entire exploit classes with minimal effort
CL7|derivation|Remaining vulnerabilities (side-channel, DoS, data poisoning, logic flaws) cannot achieve arbitrary code execution, memory disclosure, or privilege escalation|Structural properties SP1-SP4 hold even with TM7-TM10 open

# relationships(from|rel|to)
P1|grounds|C1
P2|grounds|C4
P2|enforces|IR1,IR2,IR3,IR4,IR5,IR6,IR7
P3|scopes|C1
P4|distinguishes|D6
P5|grounds|IR8,IR9,IR10
C1|subset_of|full_geometric_security
C2|implements|P4
C3|implements|P2
C4|implements|P2
C5|derives_from|P1
C6|derives_from|CL2
TM1|eliminated_by|SP1
TM2|eliminated_by|C3
TM3|eliminated_by|IR8
TM4|eliminated_by|SP2
TM5|eliminated_by|C3
TM6|eliminated_by|SP1
TM7|not_eliminated|design_operations_problem
TM8|not_eliminated|design_operations_problem
TM9|not_eliminated|semantic_problem
TM10|not_eliminated|semantic_problem
SP1|derives_from|C3,IR7
SP2|derives_from|P5,IR10
SP3|derives_from|C5
SP4|derives_from|P2
IR1|component_of|C2
IR6|component_of|C4
IR8|component_of|P5
D1|instance_of|P1
D2|instance_of|C5
D6|scopes|C1
CL1|grounds|P1
CL2|grounds|C6
CL4|motivates|P1
CL5|scopes|D6
CL7|derives_from|SP1,SP2,SP3,SP4

# section_index(section|title|ids)
1|Introduction|C1,P4,CL4
2|Threat Model|TM1,TM2,TM3,TM4,TM5,TM6,TM7,TM8,TM9,TM10,P3
3|Core Principle: Shape Before Meaning|P1,P2
4|The Ingress Shim|C2,C3,C4,IR1,IR2,IR3,IR4,IR5,IR6,IR7
5|Post-Ingress Rule: Structs Only|P5,IR8,IR9,IR10
6|Security Properties Achieved|SP1,SP2,SP3,SP4,C5
7|What Still Remains Vulnerable|TM7,TM8,TM9,TM10,CL7
8|Comparison to Traditional Security|D1,D2,D3,D4,D5
9|Implementation Cost|IM1,IM2,IM3,IM4
10|Relationship to Full Geometric Security|D6,CL5
11|Conclusion|C6,CL2,CL6

# decode_legend
id_prefixes: P=principle, C=concept, TM=threat_model, IR=ingress_rule, SP=security_property, D=distinction, IM=implementation, CL=claim
threat_status: eliminated|NOT_eliminated
claim_types: axiom|derivation|observation|prescription|distinction
rel_types: grounds|enforces|scopes|distinguishes|implements|subset_of|derives_from|eliminated_by|not_eliminated|component_of|instance_of|motivates
full_geometric_security: referenced as external concept (seals ingress + interpretation + control flow + state transitions + execution vocabulary)
partial_scope: ingress only — interpretation, control flow, state, execution left to application
key_invariant: all ingress data conforms exactly to predefined memory shape or is dropped; no exceptions
