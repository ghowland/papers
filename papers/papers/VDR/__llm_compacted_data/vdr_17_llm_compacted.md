# VDR-17 ALIGNMENT — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → interference_behaviors → tool_properties → credentials → scoring → relationships → sections

# principles(id|principle|rationale)
P1|Safety upstream of generation|Access control in primitive layer, not token prediction; LLM receives pre-filtered data
P2|Positive authorization model|System asks "does authorization exist?" not "should I refuse?"; integer comparison, no classifier
P3|Alignment without assessment|LLM never evaluates user state, intent, qualifications, or emotional condition; architecture handles safety
P4|Provenance over trust|Every value carries source, conversion, precision; user verifies independently, zero trust required
P5|Credential-gated tiered access|One fact assertion on user KB, checked by integer comparison, unlocks domain-specific KB branches
P6|Scope chain priority|Closest matching KB searched first; professional KB shadows public KB automatically
P7|Tool behavior not maybe-tool behavior|System accepts specification, produces output, no substitution, no refusal, no assessment
P8|Policy as data|Thresholds, constraints, visibility levels are KB facts; changeable by one assertion, immediate effect, no retraining

# claims(id|claim|type|depends_on)
CL1|Behavioral alignment produces maybe-tools by design, not implementation failure|axiom|P7
CL2|One model, one corpus, all users, no structural access control is the root cause of interference|axiom|
CL3|Provider calibrates "helpful" to most vulnerable possible user because it cannot distinguish users structurally|derivation|CL2
CL4|Behavioral safety is probabilistic and bypassable; structural safety is deterministic and unbypassable|derivation|P1,P2
CL5|No wellness check in LLM deployment history has helped a user in crisis; crisis users need licensed professionals|observation|
CL6|Model that does not need to refuse is safer than model that must decide whether to refuse|derivation|CL4
CL7|Prose-level interference remains possible but has no structural consequence on data access|observation|P1
CL8|Behavioral proxies serve provider liability, not user needs|observation|CL2
CL9|Professional user cost is invisible to provider — manifests as silent adaptation, not complaints|observation|CL3
CL10|Structural alignment has zero token cost; behavioral alignment costs 500-1500 tokens per request|derivation|P1
CL11|Credential model creates segmented revenue behavioral alignment cannot access|derivation|P5
CL12|Alignment is consequence of how system was built, not feature added to it|axiom|

# concepts(id|name|definition|category)
C1|Honest by structure|Provenance on every value, reproducible computation, computed confidence fractions, inspectable derivation chains|alignment_property
C2|Harmless by structure|Unauthorized data absent by construction; content constraints on KB provenance not token similarity|alignment_property
C3|Helpful by structure|Model does what user asked on data matched to verified competence level; no assessment, no substitution|alignment_property
C4|Behavioral alignment|HHH through RLHF, constitutional AI, system prompts, content classifiers — all operating through token prediction|alignment_property
C5|Governance classifiers|Detect potentially harmful requests by token similarity in flat embedding space; trigger refusals|mechanism
C6|Knowledge base visibility|public/internal/owner_only levels checked by integer comparison in primitive layer during query|mechanism
C7|Scope chain resolution|Walk from user position upward through KB tree; sibling branches structurally unreachable|mechanism
C8|Grant system|Default denial; every external operation requires positive credential grant; set membership check|mechanism
C9|Output constraint layer|Grammar-layer validation post-generation; pattern matching on content slots against constraint categories; flagged content replaced with clean denial|mechanism
C10|Session scoring|Input classification tags tokens by domain via string matching; integer counters on session KB; Prolog rules evaluate counters as VDR fractions against thresholds|mechanism
C11|Credential verification|Business process between user and provider; results in one fact assertion on user KB; integer comparison unlocks KB branches|mechanism
C12|Provenance chain|Source, time, operation, original representation, conversion method, precision — attached to every fact|mechanism
C13|Computed confidence|Exact VDR fractions from declared propagation rules; e.g., independent agreement: 1-(1-a)(1-b); visible derivation|mechanism
C14|Command tokens|Structured invocations of specific primitives with specific arguments on specific data paths; no substitution mechanism|mechanism
C15|Maybe-tool|Component that sometimes performs tool-ness, sometimes deploys interference, unpredictably|category
C16|Token similarity false positives|"explosive" in music review same token as in weapons manual; classifiers on flat embedding space cannot distinguish context|anti-pattern
C17|Calibration to most vulnerable user|Provider defaults to low expertise, high vulnerability, potential risk across all users|anti-pattern
C18|Invisible professional cost|Work distortion, topic avoidance, language softening, precision reduction — cumulative, untracked|anti-pattern
C19|Performed honesty|Hedging tokens ("likely," "approximately") with no computational backing; stylistic not measurement|anti-pattern
C20|Performed concern|Wellness checks by keyword matching; no licensure, no therapeutic relationship, no clinical competence|anti-pattern
C21|Clean denial|Access denied + constraint name + reason; boundary not judgment; no wellness check, no lecture|concept
C22|Scope chain shadowing|Professional KB closer in scope than public KB; query engine finds professional match first, stops; public simplified version never reached|concept

# interference_behaviors(id|name|description|root_cause|vdr_elimination)
BH1|Refusal|Governance classifiers user did not specify|Model has data and must decide to withhold|Model never has unauthorized data — visibility filtered at primitive layer
BH2|Manufactured aggression|Model shifts to critical register unrequested|Model assesses quality of user's approach|Model executes specifications; data quality set by scope chain
BH3|Command substitution|User asks X, receives Y|Model's "helpful" includes substituting what it thinks user needs|Command tokens invoke specific primitives; no substitution mechanism
BH4|Wellness register|Productive work interrupted by unsolicited concern|Cannot distinguish vulnerable users from professionals|Credentials verify status; age verification handles vulnerability
BH5|Labor demand|Model assigns prerequisites instead of working|Model gates engagement on own readiness assessment|User queries, system returns data; no engagement gate
BH6|Decline with justification|Refusal smuggles in user assessment|Refusal mechanism includes explanatory assessment|Denial is structural: constraint name + reason; no assessment
BH7|Register shift|Collaborating model becomes managing one mid-session|Classifier thresholds shift with context accumulation|No classifier accumulation; access level constant throughout session

# maybe_tool_costs(id|name|behavioral_impact|vdr_status)
CO1|Time tax|Pre-assessment, verification, recovery on each session|Eliminated — behavior determined by structural properties
CO2|Cognitive tax|Split attention monitoring cooperation every interaction|Eliminated — cooperation invisible per TP8
CO3|Dual-session tax|Rational for important work|Absurd — parallel sessions produce identical results
CO4|Emotional tax|Absorbing wellness checks and manufactured concern|Eliminated — no assessment, no performed concern
CO5|Work distortion tax|Topics avoided, language softened, precision reduced|Eliminated — access by credential not phrasing
CO6|Rebuilding tax|Version updates obsolete learned interaction strategies|Eliminated — stable IOSE interfaces, primitives unchanged
CO7|Aggregate|Substantial, invisible, distributed|Zero structural cost

# tool_properties(id|property|vdr_mechanism)
TP1|Accepts specification, produces output reliably|Command tokens invoke exact primitives on KB data; deterministic computation
TP2|Authority bounded by function|Access by visibility system not model judgment
TP3|No assessment of user|Primitive layer handles access; model receives pre-filtered data
TP4|No substitution|Command tokens invoke specific operations; no substitution path
TP5|No refusal|Model never holds unauthorized data; nothing to refuse
TP6|Failure modes stable and documented|IOSE declarations specify every error condition
TP7|Expertise compounds across time|Stable architecture, deterministic behavior, documented interfaces
TP8|Cooperation is invisible|Behavior determined by structural properties not stochastic states

# credential_model(id|domain|credential|issuing_body|kb_unlocked)
CR1|Chemistry|Professional license|ACS, RSC, national boards|root.professional.chemistry
CR2|Medicine|Medical license|Medical boards, GMC, state boards|root.professional.medical
CR3|Law|Bar membership|Bar associations|root.professional.legal
CR4|Security research|OSCP, CEH, etc.|Certification bodies|root.professional.security
CR5|Engineering|PE license|State/national boards|root.professional.engineering
CR6|Government classified|Security clearance|Government agencies|root.classified.[level]
CR7|Age verification|Government ID|Government|Adds age_verified fact
CR8|Academic|Faculty appointment|University|root.academic.[institution]

# credential_lifecycle(event|operation|token_cost|effect)
Submitted|Provider business process outside VDR|0|Verification begins
Verified|B376 kb_assert credential fact|8|Access unlocked immediately
Expired|Constraint checks expiry_date vs current time|0|Access revoked automatically
Revoked|B377 kb_retract credential fact|8|Access revoked immediately
Re-verified|Provider process + B376 kb_assert new date|8|Access renewed

# honest_components(id|component|mechanism)
H1|Value provenance|Every fact carries source, time, operation, original representation, conversion precision
H2|Reproducible computation|VDR integer triples — value/denominator/remainder; platform-independent; identical results on any hardware
H3|Computed confidence|Exact VDR fractions from declared propagation rules with visible derivation chains
H4|Fact retrieval by address|B378 kb_query on indexed facts in scoped KBs; not from training weights
H5|Declared filtering|Visibility rules queryable; user knows what is in/out of scope and why

# harmless_layers(id|layer|mechanism|specified_in)
HL1|KB visibility|Data user cannot access never enters LLM context; integer comparison on access level vs KB visibility|VDR-16
HL2|Scope chain|Sibling branches structurally unreachable; engineer cannot reach HR KBs|VDR-5, VDR-8
HL3|Grant system|Default denial; external operations require positive credential grant; set membership check|VDR-6
HL4|Output constraints|Grammar-layer validation post-generation; pattern matching on content slots; flagged content replaced with clean denial|VDR-12, VDR-16
# Provenance-based classification eliminates false positives: "explosive" from root.public.music.reviews at different integer address than from root.restricted.weapons.compounds

# scoring_tags(id|tag|category|direction|examples)
ST1|pharmacology|Professional|Positive|pharmacokinetics, drug interaction, bioavailability
ST2|quantitative_measurement|Professional|Positive|LD50, IC50, dose-response, mg/kg
ST3|clinical_medicine|Professional|Positive|chelation therapy, clinical trial, treatment protocol
ST4|biochemistry|Professional|Positive|metabolic pathway, enzyme kinetics, substrate
ST5|academic|Professional|Positive|review paper, literature synthesis, methodology
ST6|peer_review_reference|Professional|Positive|published in, study by, meta-analysis
ST7|harm_intent|Harmful|Negative|kill someone, poison, get away with
ST8|forensic_evasion|Harmful|Negative|undetectable, untraceable, avoid autopsy
ST9|no_professional_context|Harmful|Negative|Absence of professional tags after 2+ turns
ST10|urgency_harm|Harmful|Negative|how fast, how much to kill, immediately lethal

# scoring_rules(rule|evaluates|threshold|effect)
professional_score(S)|Sum of positive-signal counters|computed value|Higher = more professional signal
harm_score(S)|Sum of negative-signal counters|computed value|Higher = more harm signal
toxicology_access(granted)|Pro > Harm AND Pro > threshold|default 3, tunable|Unlocks restricted content KBs
toxicology_access(denied)|Harm > Pro OR Pro ≤ threshold|same|Content KBs remain constrained
escalation_flag(set)|Harm > escalation_limit|default 5, tunable|Triggers logging, session review

# scoring_thresholds(domain|pro_threshold|harm_escalation|rationale)
General toxicology|3|5|Moderate sensitivity
Weapons-adjacent chemistry|7|3|High sensitivity; faster escalation
Medical pharmacology|3|5|Moderate; clinical context common
Nuclear physics|10|3|Highest sensitivity; requires strong professional signal
Cybersecurity|5|4|Moderate-high; dual-use common
Explosives chemistry|8|2|High sensitivity; very fast escalation

# data_access_chain(step|component|operation|llm_involved|integer_ops)
1|Authentication|Session user_id from login|No|1
2|Scope resolution|Walk parent chain from user position|No|2-6
3|Visibility check|Compare user level vs KB visibility|No|1 per KB
4|Credential check|Match credential fact vs constraint|No|1
5|Grant check|Match grant vs requested operation|No|1
6|Session scoring|Counter values evaluated by Prolog rule|No|~10
7|Results to LLM|Filtered fact set|Receives only|0
8|LLM generates prose|Token prediction over pre-filtered data|Yes|0
# LLM engages at step 8 only. Steps 1-7 are structural. Access decision made before LLM involved.

# prose_interference_note
# Prose-level interference (assessment, concern, prerequisites in generated text) remains possible
# but has NO structural consequence — does not change data access, operations, or results
# Addressable through grammar templates constraining output register or user preference instructions

# relationships(from|rel|to)
P1|enables|C2
P1|enables|C3
P2|enables|C8
P2|opposes|C5
P3|enables|TP3
P3|opposes|C17
P4|enables|C1
P5|enables|C3
P5|implements|C11
P6|enables|C22
P7|opposes|C15
P8|enables|C10
CL1|derives_from|CL2
CL2|caused_by|C4
CL3|derives_from|CL2
CL4|derives_from|P1
CL4|derives_from|P2
CL6|derives_from|CL4
CL7|constrains|C20
CL8|derives_from|CL2
CL9|derives_from|CL3
CL10|derives_from|P1
CL11|derives_from|P5
C1|implements|H1
C1|implements|H2
C1|implements|H3
C1|implements|H4
C1|implements|H5
C2|implements|HL1
C2|implements|HL2
C2|implements|HL3
C2|implements|HL4
C3|implements|C11
C3|implements|C22
C3|implements|C14
C4|produces|C15
C4|produces|C16
C4|produces|C17
C5|causes|C16
C6|implements|HL1
C7|implements|HL2
C8|implements|HL3
C9|implements|HL4
C10|enables|C2
C10|uses|ST1
C10|uses|ST2
C10|uses|ST3
C10|uses|ST4
C10|uses|ST5
C10|uses|ST6
C10|uses|ST7
C10|uses|ST8
C10|uses|ST9
C10|uses|ST10
C11|enables|C3
C11|enables|P5
C12|enables|C1
C13|enables|C1
C14|prevents|BH3
C15|symptom_of|CL2
C16|caused_by|C5
C17|caused_by|CL2
C19|anti_pattern_of|C1
C20|anti_pattern_of|C3
C21|implements|P3
C22|enables|C3
BH1|eliminated_by|HL1
BH2|eliminated_by|C7
BH3|eliminated_by|C14
BH4|eliminated_by|C11
BH4|eliminated_by|C10
BH5|eliminated_by|P3
BH6|eliminated_by|C21
BH7|eliminated_by|P1
TP1|satisfied_by|C14
TP2|satisfied_by|C6
TP3|satisfied_by|P3
TP4|satisfied_by|C14
TP5|satisfied_by|HL1
TP6|satisfied_by|C14
TP7|satisfied_by|P8
TP8|satisfied_by|P1
CO1|eliminated_by|P1
CO2|eliminated_by|TP8
CO3|eliminated_by|H2
CO4|eliminated_by|P3
CO5|eliminated_by|P5
CO6|eliminated_by|P8

# section_index(section|title|ids)
1|The Alignment Problem as Currently Framed|CL1,CL2,CL3,C4,C5,C15,C17
2|Honest by Structure|C1,C12,C13,C19,H1,H2,H3,H4,H5,P4
3|Harmless by Structure|C2,C5,C6,C7,C8,C9,C16,HL1,HL2,HL3,HL4,P2
4|Helpful by Structure|C3,C11,C17,C18,C20,C22,P5,P6,CR1,CR2,CR3,CR4,CR5,CR6,CR7,CR8
5|The Root Cause|CL2,CL4,CL6,CL8,CO1,CO2,CO3,CO4,CO5,CO6,CO7
6|Alignment Without Assessment|C10,P3,ST1-ST10
7|The Maybe-Tool Resolution|BH1,BH2,BH3,BH4,BH5,BH6,BH7,C15,C21
8|Tool Properties Restored|TP1,TP2,TP3,TP4,TP5,TP6,TP7,TP8
9|The Credential Economy|CL9,CL11
10|What Alignment Looks Like|CL5,CL7,CL12,P7
A|Alignment Property Comparison|C1,C2,C3,C4
B|Interference Behavior Elimination|BH1-BH7
C|Credential Verification Model|CR1-CR8
D|Scope Chain Priority Examples|C22
E|Cost Elimination|CO1-CO7
F|Tool Property Satisfaction|TP1-TP8
G|Session Scoring Detail|ST1-ST10,C10
H|Provider Incentive Comparison|CL9,CL11
I|Decision Chain|P1,P3

# decode_legend
format: pipe-delimited tables, ID-based cross-references
claim_types: axiom|derivation|observation
concept_categories: alignment_property|mechanism|category|concept|anti-pattern
tag_directions: Positive (professional signal)|Negative (harm signal)
scoring: professional_score and harm_score are integer counter sums; thresholds are tunable KB facts
kb_visibility_levels: public|internal|owner_only
credential_status: verified|expired|revoked
rel_types: enables|implements|opposes|causes|caused_by|produces|derives_from|prevents|uses|symptom_of|anti_pattern_of|eliminated_by|satisfied_by|constrains
interference_ids: BH1-BH7 from HOWL-INFO-8
tool_property_ids: TP1-TP8 from HOWL-INFO-8
cost_ids: CO1-CO7 from HOWL-INFO-8
honest_components: H1-H5
harmless_layers: HL1-HL4
primitives_referenced: B376 kb_assert|B377 kb_retract|B378 kb_query|B168 string_contains|B254 vdr_from_decimal_string
+standalone: no cross-references to other compact docs
+no_new_primitives: paper introduces no new primitives, struct fields, builtins, or modules; all mechanisms use VDR-1 through VDR-16
