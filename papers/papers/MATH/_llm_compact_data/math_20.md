
# DERIVABILITY CLASSES OF OPTIMAL REDUCTION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: definitions → classes → properties → hierarchy → transitions → domains → training → procedure → relationships → sections

# definitions(id|symbol|name|definition|unit|scope)
D1|R*|Optimal reduction|Minimum correct ops any competent processor requires for reliable execution of task|ops|Class P: exact. Class B: bounded. Class E: estimated
D2|R_lower|Proven lower bound|Minimum ops established by structural argument; no correct execution uses fewer|ops|Class B and P only
D3|R_upper|Proven upper bound|Op count achieved by best known correct method|ops|Class B and P only
D4|R_empirical|Empirical floor estimate|Lowest op count observed from any processor with correct results|ops|All classes; only estimate for Class E
D5|gap(task)|Bound gap|R_upper − R_lower. Structural uncertainty in R*|ops|Class B only; zero for P; undefined for E

# classes(id|name|criterion|certainty|source_of_knowledge|revision_conditions|structural_properties_required)
CL1|Class P (Provable)|R* derivable from task structure by logical argument. Exact value known with certainty before any processor executes|Mathematical proof|Task structure (logical derivation)|Never (theorem is permanent)|P1 ∧ P2 ∧ P3 ∧ P4
CL2|Class B (Boundable)|R* constrained by provable bounds; exact value undetermined. R_lower ≤ R* ≤ R_upper|Proven bounds with gap|Partial task structure + algorithmic upper bounds|Gap narrows with new algorithms or proofs; never widens|Some subset of P1-P4
CL3|Class E (Empirical)|R* known only from observation. No structural bound available. Subject to revision|Best observed; revisable|Processor population measurement|Revises downward when better performer observed|None of P1-P4

# structural_properties(id|property|what_it_enables|test|when_absent|typically_present|typically_absent)
SP1|P1: Enumerable input space|Information-theoretic lower bounds; counting arguments; entropy computation|Can you define set containing all possible inputs? Count or compute information content?|No lower bound from input structure|Computation, mathematics, manufacturing|Medicine, combat, creative arts
SP2|P2: Decidable correctness|Adversary arguments; verification-based lower bounds; crisp R* definition|Given input+output, can finite procedure determine correctness?|R* definition imprecise; adversary can't distinguish correct from incorrect|Computation, mathematics, manufacturing|Medicine (graded), arts (aesthetic), business (multidimensional)
SP3|P3: Bounded information per op|Division argument: total information / per-op bound = minimum ops|Is there maximum information any single op can extract regardless of who performs it?|Experts extract more per op than novices; floor depends on processor dissolution state|Computation (bit per comparison), formal protocols|Medicine (expert glance vs novice exam), aviation (experienced scan vs novice fixation)
SP4|P4: Constructible adversary|Tight lower bounds; worst-case analysis; proof floor applies to all strategies|Can you construct input forcing any correct processor to use ≥ R* ops?|Cannot rule out clever strategies circumventing apparent lower bound|Computation, mathematics|Medicine (no adversarial patient), social domains

# class_p_examples(id|task|domain|R*_proven|proof_technique)
PE1|Comparison-based sort|Computation|⌈log₂(N!)⌉ ≈ N log₂ N|Information-theoretic: N! orderings, 1 bit/comparison
PE2|Search in sorted array|Computation|⌈log₂ N⌉|Information-theoretic: N positions, 1 bit/comparison. Binary search achieves
PE3|Parity of N bits|Computation|N|Adversary: any unread bit could flip answer
PE4|Graph connectivity|Computation|Ω(E) edge checks|Adversary: unexamined edge could disconnect
PE5|Polynomial evaluation|Computation|N multiplications + N additions (Horner's)|Algebraic lower bound
PE6|N-digit addition|Mathematics|N to 2N ops|Structural: must process each digit; carry propagation bounded
PE7|Checklist protocol (medical)|Medicine|Number of checklist items|Each item is independent necessary check; any skipped could be failure

# class_b_examples(id|task|domain|R_lower|R_upper|gap_source|path_to_closing)
BE1|Metric TSP (approximate)|Computation|Ω(N²) read matrix|O(N³) Christofides 1.5×|Unknown if sub-cubic 1.5× exists|Better approximation or tighter lower bounds
BE2|Matrix multiplication|Computation|Ω(N²) read inputs|O(N^2.371) current best|Open whether ω=2 achievable|New algebraic techniques
BE3|Numerical integration (ε accuracy)|Mathematics|Ω(ε^(−1/k)) for k-smooth|O(ε^(−1/k)) optimal quadrature|Function smoothness may be unknown|Adaptive methods; smoothness estimation
BE4|RA diagnosis (ACR criteria)|Medicine|4 checks (minimum for 4-of-7)|7 checks (all criteria)|Per-patient correlation unknown|Bayesian optimal ordering
BE5|Protein structure from sequence|Biology|Ω(N) process sequence|O(N⁴) AlphaFold-class|Physics not fully characterized|Better structural models
BE6|Channel coding at capacity|Information theory|N (process all bits)|O(N log N) polar codes|Encoding/decoding complexity|Better code constructions
BE7|SAT (general)|Computation|Ω(N) read formula|O(2^N) exhaustive|P vs NP|Resolve P vs NP
BE8|Minimum spanning tree|Computation|Ω(E)|O(E α(V)) nearly linear|α(V) factor may or may not be eliminable|Nearly closed

# class_e_examples(id|task|domain|R_empirical|why_not_boundable|properties_missing|variance)
EE1|Undifferentiated chest pain diagnosis|Medicine|5-8 ops (expert)|Symptom space not enumerable; correctness graded; per-op info varies by experience|P1,P2,P3,P4 all absent|5-60 ops (10× range)
EE2|Threat classification (combat)|Aviation|3-4 conscious ops (top pilot)|Tactical space unbounded; correctness context-dependent; info per scan varies|P1,P2,P3 absent|3-15 ops (5× range)
EE3|Novel theorem proof|Mathematics|Varies per theorem|Proof space infinite; minimum length undecidable in general|P4 absent; meta-level undecidability|Unbounded
EE4|Novel bug in unfamiliar codebase|Software|5 ops (expert on familiar patterns)|Codebase space not bounded; bug type unknown; diagnostic info varies|P1,P3 absent|5-40 ops (8× range)
EE5|Recipe optimization|Cooking|7 ops (expert chef)|Quality graded not binary; ingredient interaction space not characterizable|P1,P2 absent|7-30 ops (4× range)
EE6|Emergency triage|Medicine|3-5 ops (experienced nurse)|Presentation space unbounded; severity continuous; per-assessment info varies|P1,P2,P3 absent|3-15 ops (5× range)

# hierarchy(id|claim|mechanism)
H1|P ⊂ B|Every provable floor is trivially a bounded floor with gap=0. Class P is special case of B with complete structural information
H2|B contains results not in P|Tasks with genuine bound gaps where lower and upper bound techniques don't converge. Whether gap is closeable connects to P vs NP
H3|E contains results not in B|Tasks with no structural bounds at all. Whether permanently in E or merely currently in E is often unanswerable
H4|Transitions are directional: E→B→P|Tasks gain structural analysis. Should not reverse — proven bound doesn't become unproven
H5|E→B triggered by discovery of formal structure within task|Biomarkers add criteria. Computational models add bounds. Notation formalizes ad hoc procedures
H6|B→P triggered by closing gap between bounds|Tablebases compute exact answer. Better algorithms meet lower bounds. New proofs tighten lower bounds

# class_transitions(id|task|domain|from|to|trigger|year|mechanism)
CT1|MI diagnosis|Medicine|E|B|Troponin biomarker discovery|1990s|Added formal criterion; established minimum checks
CT2|Chess endgame (≤7 pieces)|Game theory|B|P|Exhaustive tablebase computation|2012|Computed exact R* for all covered positions
CT3|Checkers (complete)|Game theory|B|P|Complete solution computed|2007|Exhaustive backward induction
CT4|Protein structure prediction|Biology|E|B|AlphaFold architecture|2020|Computational upper bound; physics gives lower bound
CT5|Arithmetic operations|Mathematics|E|P|Positional notation with zero|~500 CE|Formalized task structure; made op count derivable
CT6|Sorting|Computation|P (always)|P|Information-theoretic proof|1960s|Task was always P; proof discovered
CT7|Metric TSP approximate|Computation|B (wide)|B (narrower)|Christofides + improvements|1976-present|Better algorithms narrowed gap without closing
CT8|Image classification|Computation|E|B|PAC learning bounds + deep learning|2010s|Structural floor + achievable ceiling established

# domain_classification(id|domain|predominant|P_ratio|B_ratio|E_ratio|P_examples|B_examples|E_examples)
DC1|Computation|P|60|30|10|Sort, search, graph, parity, polynomial|NP-hard optimization, matrix mult, channel coding|Heuristic design, novel problem solving
DC2|Mathematics|Mixed|30|30|40|Polynomial eval, system solving|Optimization, approximation theory|Creative proof, conjecture resolution
DC3|Medicine|E|5|20|75|Algorithmic protocols (ACLS)|Criteria-based diagnosis (RA, sepsis score)|General diagnosis, treatment, prognosis
DC4|Aviation (transport)|Mixed|25|30|45|Checklists, navigation, fuel calc|Approach optimization, separation|Threat assessment, emergency response
DC5|Aviation (combat)|E-heavy|15|20|65|Weapons zones, intercept geometry|Mission planning, fuel management|Threat classification, engagement sequencing
DC6|Software engineering|Mixed|20|35|45|Algorithm implementation|Known-pattern bugs, performance opt|Novel bugs, architecture design, code review
DC7|Manufacturing|B-heavy|25|50|25|Simple assembly (physical actions)|Complex assembly, quality sequencing|Process innovation, novel defect root cause
DC8|Cooking|E|5|15|80|Boiling water (physical minimum)|Baking (chemical constraints)|Recipe optimization, flavor balancing
DC9|ATC|Mixed|15|35|50|Separation calc, comms protocol|Flow optimization, capacity analysis|Dynamic traffic, conflict under uncertainty
DC10|Customer support|E-heavy|10|25|65|Scripted known-issue protocols|Diagnostic trees for known categories|Novel issues, de-escalation
DC11|Education|E-heavy|5|15|80|Test scoring|Curriculum sequencing|Pedagogical strategy, assessment design
DC12|Law|E-heavy|5|20|75|Procedural filing requirements|Evidence evaluation|Case strategy, jury persuasion

# training_implications(id|class|target|assessment|certification|infrastructure_optimality|revision_frequency|expert_infrastructure_gap)
TI1|P|Exact: R* (known value)|Absolute: distance from R* in ops|Rigorous: demonstrate R* or better|Provably optimal: encodes exactly R* operations|Never (unless task changes)|Zero
TI2|B|Range: R_upper toward R_lower|Bounded: position within [R_lower,R_upper]|Bounded: demonstrate R_upper or better|Best-effort: encodes R_upper; may include unnecessary ops|When better algorithms/proofs narrow gap|Small to moderate
TI3|E|Relative: best observed performance|Relative: percentile in population|Normative: demonstrate top-N%|Empirically calibrated: encodes best practice; revision-prone|When better performer observed|Moderate to large

# classification_procedure(id|step|question|yes|no|tool)
CP1|1|Can you formally define space of possible inputs?|Proceed to step 2|Provisional Class E|Attempt formal specification; test countability, entropy
CP2|2|Is output correctness decidable by finite procedure?|Proceed to step 3|Class E (graded/subjective correctness)|Define verification procedure; test if binary
CP3|3|Can you compute minimum information extraction from input to correct output?|Lower bound established; proceed to step 4|Class B if any structural bound; else E|Information-theoretic analysis; counting; adversary
CP4|4|Does known method achieve lower bound from step 3?|Class P (R* = lower = upper)|Proceed to step 5|Compare best known method cost to lower bound
CP5|5|Does known method have quantifiable cost above lower bound?|Class B (gap computable)|Class B with open upper bound|Upper bound from best known algorithm/procedure
# Procedure is conservative: classifies toward E when in doubt. False negatives (P→B, B→E) harmless. False positives (E→P) dangerous

# key_insight(id|claim)
KI1|R* may depend on processor's dissolution state for same task. Expert extracts more information per op than novice. For Class P, R* is processor-independent. For Class E, R* may be inherently processor-relative
KI2|Experts in Class E domains don't know if they're optimal, and neither does anyone else. Best surgeon/pilot/diagnostician defines empirical floor but cannot prove no shorter chain exists
KI3|The parallel P↔P, B↔NP, E↔Undecidable is structural but imperfect. Complexity asks "how hard is the task?" Derivability asks "how hard is it to know how hard the task is?" — different meta-levels
KI4|Mathematics is the domain most likely to generate E→B→P transitions because mathematical research IS the activity of finding formal structure in previously informal territory

# complexity_parallel(id|derivability|complexity|similarity|difference)
XP1|P (Provable)|P (Polynomial)|Both: answer derivable by efficient procedure|Derivability P: one answer per task. Complexity P: per instance
XP2|B (Boundable)|NP|Both: verifiable but not efficiently derivable|Derivability B: bounds from structure. Complexity NP: verification from witness
XP3|E (Empirical)|Undecidable|Both: no general algorithm produces answer|Derivability E: answer exists but isn't derivable. Undecidable: answer may not exist in formal system
XP4|B gap|P vs NP question|Both: whether gap can close is deepest open problem|Derivability gap: per-task. P vs NP: entire class

# open_problems(id|problem|description)
OP1|Formal relationship to complexity classes|Whether formal reduction exists between derivability classes and computational complexity. Information-based complexity theory may bridge
OP2|Class B gap dynamics|Is gap closure rate predictable from task properties? Steady narrowing may signal approaching P. Stable gap may indicate fundamental B−P membership
OP3|Dissolution curve dependence on class|Do Class P tasks dissolve faster than Class E? Known floor enables targeted training → testable prediction
OP4|Meta-derivability|R* of determining R*. For some tasks, whether formal characterization exists may itself be undecidable. Connects to Gödel and halting problem
OP5|Subclasses within E|Not all E tasks equally opaque. Some have weak structural constraints. Degrees of empirical-ness as useful substructure?
OP6|Cross-domain R* comparison|Is "5 ops" in medicine comparable to "5 ops" in software? What normalization required?

# relationships(from|rel|to)
CL1|subset_of|CL2
CL2|contains_not_in|CL1
CL3|contains_not_in|CL2
H4|defines|transition direction E→B→P
SP1|enables|information-theoretic lower bounds
SP2|enables|adversary arguments
SP3|enables|division argument (info/op)
SP4|enables|tight lower bounds
H5|triggers|CT1,CT4,CT5,CT8
H6|triggers|CT2,CT3
KI1|distinguishes|CL1 from CL3 on processor-dependence
KI3|connects|derivability to complexity theory
TI1|derives_from|CL1
TI2|derives_from|CL2
TI3|derives_from|CL3

# section_index(section|title|ids)
1|Two Floors|D1-D5,CL1-CL3
2|Three Classes|CL1-CL3
3|Class P — Provable Floor|SP1-SP4,PE1-PE7
4|Class B — Bounded Floor|BE1-BE8
5|Class E — Empirical Floor|EE1-EE6,KI2
6|Properties Determining Class|SP1-SP4,KI1
7|The Hierarchy|H1-H6,XP1-XP4,KI3
8|Class Transitions|CT1-CT8,H5,H6
9|Domain Classification|DC1-DC12,KI4
10|Training and Assessment|TI1-TI3,KI2
11|Classification Procedure|CP1-CP5
12|Dissolution Infrastructure and Class|TI1-TI3
13|Scope and Open Problems|OP1-OP6

# decode_legend
three_classes: P (provable, exact R* from structure) | B (boundable, R_lower≤R*≤R_upper) | E (empirical, best observed only)
four_properties: P1=enumerable input | P2=decidable correctness | P3=bounded info/op | P4=constructible adversary. All four → P. Some → B. None → E
hierarchy: P⊂B. Transitions E→B→P directional (structural discovery). Never reverse
classification_procedure: formal input? → decidable correctness? → info-theoretic bound? → method achieves bound? Conservative toward E
training_consequence: P=exact target, absolute assessment, provably optimal infrastructure. B=range target, bounded assessment, best-effort infrastructure. E=relative target, population assessment, empirically calibrated infrastructure
key_insight: Class E experts don't know if optimal. Class P experts can be verified as optimal. R* processor-independent for P, potentially processor-relative for E
complexity_parallel: P↔P, B↔NP, E↔Undecidable. Structural but imperfect — operates at different meta-level (cost of knowing the cost)
id_prefixes: D=definition|CL=class|SP=structural_property|PE=class_P_example|BE=class_B_example|EE=class_E_example|H=hierarchy|CT=class_transition|DC=domain_classification|TI=training_implication|CP=classification_procedure|KI=key_insight|XP=complexity_parallel|OP=open_problem
spec_counts: 5 definitions|3 classes|4 structural properties|7 Class P examples|8 Class B examples|6 Class E examples|6 hierarchy claims|8 historical transitions|12 domain classifications|3 training implication sets|5 procedure steps|4 complexity parallels|6 open problems
