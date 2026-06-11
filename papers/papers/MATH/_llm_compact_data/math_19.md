
# THE MATHEMATICS OF PROCESSING-AWARE COMMUNICATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → definitions → cost_equation → compression → dissolution_differential → redundancy → optimization → heterogeneous → layered → applications → civilization → open_problems → claims → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Every communication has three independent additive costs: sender encoding, channel transmission, receiver decoding|Shannon formalized middle term; endpoint terms dominate most real communication; optimizing channel alone is insufficient
P2|Shannon recovered as special case when both endpoint terms are zero|Expert-to-expert with shared dissolved vocabulary; only channel cost remains
P3|Receiver decoding cost is the critical term Shannon excluded and the one that dominates|Junior developer 45 min on unfamiliar API is paying ops not bits; student 3 hours on textbook chapter is paying ops
P4|Dissolution differential between sender and receiver predicts communication difficulty before message sent|Expert cannot feel cost of dissolved terms; structural consequence of dissolution, not empathy failure
P5|Redundancy in processing = dissolution infrastructure: extra words reduce receiver decompression cost|Shannon-redundant (no information added) but processing-efficient (reduces receiver ops); not waste
P6|Optimal message length increases with dissolution differential|Larger gap → more infrastructure needed → longer message; not verbosity but optimal encoding for high-Hp receiver
P7|No single linear encoding optimizes for heterogeneous audience|Expert finds it verbose, novice finds it terse; both correct; dissolution differential between most and least expert prevents single optimum
P8|Layered encoding solves heterogeneous audience: each receiver consumes only layers they need|Expert reads base layer (minimal); novice reads all layers (maximum infrastructure); approaches per-receiver optimum

# formal_definitions(id|symbol|name|definition|unit)
FD1|Hp(A, encode)|Sender encoding cost|Ops sender executes to transform internal state into transmissible symbols|ops
FD2|Hs(channel)|Channel cost|Bits required for reliable transmission (Shannon's domain)|bits
FD3|Hp(B, decode)|Receiver decoding cost|Ops receiver executes to transform symbols into actionable understanding|ops
FD4|Cost(A→B)|Total communication cost|Hp(A,encode) + Hs(channel) + Hp(B,decode)|ops+bits+ops
FD5|C / C⁻¹|Compression / decompression|C: referent_space → token (many-to-one); C⁻¹: (token,context) → referent (context-dependent)|—
FD6|ratio(token,p)|Compression ratio|Count of referents processor p can decompress from token across all contexts; grows with experience|count
FD7|decomp(token,p,ctx)|Decompression cost|Hp(p, decode(token,ctx)); zero when dissolved, positive when unfamiliar|ops
FD8|Δ(A,B,tokens)|Dissolution differential|Σₜ [Hp(B,decode(t)) − Hp(A,decode(t))]; total cost gap sender-to-receiver|ops
FD9|redundancy(msg)|Explanatory redundancy|Hs(message) − Hs(minimal_encoding); bits beyond Shannon-optimal|bits
FD10|η(word,B)|Dissolution efficiency|−ΔHp(B,decode) / ΔHs; receiver cost reduction per unit channel cost|ops/bit
FD11|η_audience(word)|Audience-weighted efficiency|Σᵢ max(0, −ΔHp(Bᵢ)) / ΔHs; total receiver cost reduction per channel cost|ops/bit
FD12|encoding*|Optimal encoding|argmin_e {Hp(A,encode(e)) + Hs(e) + Hp(B,decode(e))}|—
FD13|alignment(A,B,token)|Codebook alignment|Jaccard similarity of referent sets: \|R_A∩R_B\| / \|R_A∪R_B\||[0,1]
FD14|Q(doc,readers)|Documentation quality|content_transmitted / [Hs(doc) + Σᵢ Hp(readerᵢ,decode(doc))]|content/cost
FD15|E(teacher,student,t)|Teaching effectiveness|−dHp(student,domain) / dt_teaching; dissolution rate during teaching|ops/time
FD16|Q(API,consumers)|API quality|functionality_accessed / Σᵢ Σⱼ Hp(consumerᵢ,invoke(callⱼ)) × freq(callⱼ)|functionality/ops
FD17|ratio(token,p,t)|Compression maturity|Referents decompressible at time t; grows with experience|count
FD18|benefit(layered)|Layering benefit|Cost(linear_optimal) − Cost(layered_optimal); zero when audience homogeneous|ops+bits

# three_term_cost(id|scenario|hp_encode|hs_channel|hp_decode|dominant|shannon_sufficient)
TC1|Expert→Expert (shared domain)|~0 (dissolved)|Fixed|~0 (dissolved)|Channel|Yes — both dissolved
TC2|Expert→Novice|~0|Fixed|High (5-10 ops per undissolved token)|Receiver decode|No — receiver dominates 10-100×
TC3|Novice→Expert|High|Fixed|~0|Sender encode|No — sender dominates
TC4|Novice→Novice|High|Fixed|High|Both endpoints|No — both high
TC5|Expert→Mixed audience|~0|Fixed|Σᵢ Hp(Bᵢ) varies widely|Sum of receiver terms|No — scales with heterogeneity
TC6|Machine→Machine (APIs)|~0 (compiled)|Fixed|~0 (compiled)|Channel|Yes — closest to Shannon's model
TC7|Teacher→Student (over lesson)|Moderate (adapting)|Increases|Decreasing (dissolving)|Shifts receiver→channel|Initially no; approaches yes as student dissolves

# compression_properties(id|property|description)
CP1|Language works by compression|Single word packs many referents into one token; "fire" compresses combustion, termination, weapon discharge, etc.
CP2|Decompression is context-dependent|Same token → different referents by context; "fire" in building vs boardroom vs rifle range
CP3|Compression ratio grows with experience|Child's "fire" = 2-3 referents; adult = 12-18; firefighter = 40-60; arson investigator = 80-120
CP4|Dissolved tokens cost zero|Fluent speakers process 150 wpm because common vocabulary decompression is dissolved; if each word cost 1 op, pipeline saturated before meaning processed
CP5|Undissolved tokens are processing tax|Each unfamiliar term costs pipeline ops; sentence full of jargon = Infinity of Ones competing for pipeline

# dissolution_differential(id|communication_type|typical_differential_ops|high_diff_tokens|intervention)
DD1|Senior architect → junior developer|150-400 per page|System-specific names, architecture patterns, team conventions|Glossary; architecture decision records; onboarding docs
DD2|Specialist physician → patient|200-500 per consultation|All medical jargon; anatomical references; probabilistic language|Plain language; analogies; diagrams; teach-back
DD3|Professor → undergraduate|100-300 per lecture|Newly introduced terms; everyday words used technically|Definitions at first use; examples; prerequisite review
DD4|API documentation → new consumer|50-150 per endpoint|Naming conventions; auth patterns; error codes|Quick-start guide; code examples; playground
DD5|Cross-team Slack|30-80 per thread|Team acronyms; project code names; implicit past decisions|Expand acronyms; context links; avoid assumed knowledge
DD6|Regulatory text → public|300-600 per page|Latin phrases; defined terms; cross-references|Plain language summary; layered with simplified overview
DD7|Research paper → adjacent field|80-200 per paper|Method names; assumed baseline; in-group references|Extended intro; cross-field analogies; explicit methodology
DD8|Parent → child|Varies by age|Any unencountered word; abstract temporal/causal concepts|Simplified vocabulary; concrete examples; repetition

# dissolution_infrastructure_types(id|type|mechanism|typical_efficiency_ops_per_bit|best_for)
DI1|Inline definition|Define term at point of first use|3-8|Single unfamiliar term
DI2|Example|Concrete instance of abstract concept|5-15|Abstract concepts; pattern illustration
DI3|Analogy|Map unfamiliar concept to familiar one|8-20|Structural concepts; cross-domain communication
DI4|Diagram|Visual representation of structure/process|10-30|Spatial relationships; process flows
DI5|Code example|Executable demonstration|5-25|API usage; algorithm illustration
DI6|Prerequisite review|Brief coverage of assumed background|2-5|Heterogeneous audiences; strict prerequisite chains
DI7|Glossary|Collected definitions by reference|1-3 per lookup|Reference; ongoing use; heterogeneous audiences
DI8|Summary/TL;DR|Compressed overview|2-6|Time-constrained; assessing relevance
DI9|Worked solution|Step-by-step demonstration|8-15|Procedural knowledge; math/algorithmic
DI10|FAQ|Common questions with answers|3-8|Known confusion points; recurring support

# optimization_surface(id|region|character|when_optimal)
OS1|Expert-shorthand minimum|Max compressed; all jargon, no explanation; min Hs, min Hp(A), max Hp(B) for novice|Receiver is expert peer with same vocabulary
OS2|Verbose-tutorial maximum|Everything from first principles; max Hs, moderate Hp(A), min Hp(B) for novice; high total|Never optimal (channel term too large)
OS3|Processing-optimal saddle|Dissolved vocabulary where receiver has it; infrastructure where needed; omit where channel cost exceeds benefit|Between extremes; minimizes Hp(A)+Hs+Hp(B)

# heterogeneous_audience(id|composition|strategy|length_vs_expert_optimal)
HA1|All experts (homogeneous)|Compressed shorthand|1× (expert-optimal = overall optimal)
HA2|All novices (homogeneous)|Full tutorial; maximum infrastructure|5-15×
HA3|Experts + novices (bimodal)|Layered: compressed base + expandable infrastructure|2-4×
HA4|Continuous spread (uniform)|Layered with multiple tiers; progressive disclosure|3-8×
HA5|Mostly experts, few novices|Compressed with linked glossary/appendix|1.2-2×
HA6|Mostly novices, few experts|Expanded with expert fast-paths|4-10× with skip navigation
HA7|Multiple domains (cross-functional)|Domain-specific sections with shared overview|2-5×
HA8|Unknown audience|Layered with broad coverage; progressive disclosure at every level|3-6× (hedge)

# layered_encoding_implementations(id|medium|base_layer_expert|second_layer|third_layer_novice|navigation)
LE1|Technical documentation|Compressed reference; API signatures; terse|Conceptual explanations; usage examples; patterns|Tutorials; prerequisites; glossary; step-by-step|TOC with difficulty markers
LE2|Web documentation|Collapsed/minimal default|Expandable sections; tooltips; inline examples|Linked tutorials; video; interactive playgrounds|Expand/collapse; progressive disclosure
LE3|Academic paper|Abstract + results; equations; compressed methodology|Extended intro; worked examples; methodology detail|Background; notation guide; appendix; supplementary|Paper structure itself layered
LE4|API design|Simple calls with good defaults; minimal params|Configuration objects; option params; builders|Tutorials; cookbooks; REPL; migration guides|Signature simplicity → config depth → doc depth
LE5|User interface|Primary buttons; dissolved conventions|Tooltips; contextual help; onboarding|Help docs; tutorial mode; walkthroughs; support|Hover → click → navigate
LE6|Email/message|Subject line (one sentence)|First paragraph (key content + action)|Full body (context, reasoning, background)|Scanning: subject → para → body
LE7|Codebase|Function signatures + type system|Inline comments; doc-comments|Architecture docs; README; contribution guide|Code → comments → documentation
LE8|Presentation|Slide title + key insight|Verbal explanation|Q&A; handout; recorded lecture; office hours|Time-based; Q&A as demand-driven

# documentation_quality_metrics(id|metric|measures|relationship_to_cost)
QM1|Time on page|Total reading + decompression time|Proxy for Hs + Hp(B,decode)
QM2|Definition lookup rate|Frequency navigating to glossary/external|Direct per-token decompression cost; failed dissolution
QM3|Completion rate|Fraction reaching end|Total cost vs time budget; incomplete = exceeded budget
QM4|Comprehension score|Accuracy after reading|Inverse of residual Hp(B) after decoding
QM5|Return visits|Revisit frequency|Incomplete dissolution per visit
QM6|Time to first action|Reading through actionability|Total cost from decode through reduction to actionable One
QM7|Search-after-reading rate|Post-read searches|Content missing dissolution infrastructure for specific tokens
QM8|Reader satisfaction|Subjective assessment|Perceived cost-to-value ratio

# teaching_phases(id|phase|student_state|optimal_encoding|infrastructure_needed|trajectory)
TP1|Opening/motivation|Baseline; topic undissolved|Connect to dissolved prior knowledge; familiar vocabulary only|Maximum|Stable or slight decrease
TP2|First concept introduction|Baseline for new concept|Define explicitly; single concept per unit; immediate example|High|Decreasing; first concept dissolving
TP3|Building on first concept|First partially dissolved|Use first as token; introduce second using first as scaffold|Moderate|Accelerating decrease
TP4|Mid-lesson acceleration|Several dissolved; building blocks available|Increase density; use dissolved freely; shorter examples|Decreasing|Steep decrease; dissolution cascade
TP5|Practice/application|Concepts introduced; dissolution in progress|Shift to exercises; student generates; errors reveal gaps|Minimal from teacher|Decreasing through practice
TP6|Consolidation|Most at low decompression cost|Compressed restatement; connect to broader context|Minimal; summary uses dissolved tokens|Stable near zero

# api_design_patterns(id|pattern|mechanism|receiver_cost_effect)
AP1|Consistent naming (get_X, create_X)|Convention dissolves once; applies everywhere|Low: pattern dissolved; new endpoints decompressible
AP2|Predictable parameter ordering|Convention dissolves once|Low: invocation becomes structural
AP3|Descriptive error types|Taxonomy dissolves once; each error meaningful|Low: error handling dissolved
AP4|Sensible defaults|Common case zero configuration|Very low for common case
AP5|Progressive disclosure|Layered surface; consume needed complexity|Optimal per consumer
AP6|Code examples in docs|Executable dissolution infrastructure|Low: copy-paste-modify path
AP7|Interactive playground/REPL|Zero-cost experimentation; self-directed dissolution|Very low: practice-based dissolution
AP8|Backward compatibility|Existing dissolved invocations remain valid|Zero for existing; prevents dissolution cascade

# codebook_alignment_levels(id|level|character|effect|detection)
AL1|1.0 (perfect)|Identical decompression for all tokens|Communication succeeds; minimal cost|N/A
AL2|0.8-0.99 (high)|Most aligned; few misaligned|Mostly succeeds; occasional misunderstanding|Surfaces during implementation
AL3|0.5-0.8 (moderate)|Many partially aligned|Partial success; significant clarification needed|Frequent clarification requests
AL4|0.2-0.5 (low)|Few aligned; most decompress differently|Largely fails; both think they understand but reach different conclusions|Actions don't match intent; discovered downstream
AL5|0.0-0.2 (minimal)|Almost none aligned|Fails entirely or dangerous misunderstanding; receiver confident in wrong interpretation|Catastrophic downstream failure
# Most dangerous: low alignment where decompression fires automatically to wrong referent — invisible, confident, wrong

# compression_ratio_examples(id|token|processor|ratio|decompression_cost)
CR1|"fire"|3-year-old child|2-3|Zero for known; undefined for others
CR2|"fire"|General adult|12-18|Zero for common; 1-2 ops for rare
CR3|"fire"|Firefighter|40-60|Zero for professional referents
CR4|"fire"|Arson investigator|80-120|Zero for professional referents
CR5|"buffer"|Non-technical adult|1-2|Zero
CR6|"buffer"|Junior developer|4-6|Zero common; 2-3 ops systems concepts
CR7|"buffer"|Systems programmer|15-25|Zero for all
CR8|"normal"|General public|3-5|Zero for "typical"; 2-3 ops technical
CR9|"normal"|Mathematician|8-12|Zero; context resolves instantly
CR10|"normal"|Physician|6-10|Zero; clinical context resolves

# civilization_dissolution_stack(id|era|innovation|what_dissolved|cost_change)
CS1|~3000 BCE|Writing|Speaker-presence requirement|Sender encodes once; persistent channel; receiver pays per read
CS2|~1500 BCE|Alphabet|Infinite logograms|26 composable letters; reduced learning cost
CS3|~500 CE|Positional notation with zero|Per-scale arithmetic procedures|Arithmetic dissolved into notation manipulation
CS4|~1450|Printing press|Per-copy scribe encoding|Dramatically reduced per-copy channel cost
CS5|~1880|Standard time zones|Active cross-location time conversion|Eliminated 3-5 ops per cross-region communication
CS6|~1956|Shipping containers|Per-cargo handling procedures|Dissolved loading/unloading to mechanical operation
CS7|~1970|Internet protocols (TCP/IP)|Per-network communication procedures|Dissolved network boundary crossing
CS8|~1990|World Wide Web|Per-document distribution procedure|Dissolved publishing to upload
CS9|~2000|Search engines|Per-query information location|Reduced information-finding from hours to seconds
CS10|~2010|Smartphones|Per-task device selection|Dissolved tool selection for communication/navigation/reference
CS11|~2020|LLMs|Per-domain expert consultation|Reduced domain-entry cost; partial dissolution infrastructure for arbitrary domains
# Pattern: compression token or infrastructure created once → dissolved across population → freed pipeline for next unsolved problem
# Rate of civilizational progress bounded by rate dissolution infrastructure created and dissolved across populations

# open_problems(id|problem|description)
OP1|Dissolution state estimation|How accurately senders estimate receiver state; how error propagates to total cost; how to improve estimation
OP2|Dynamic teaching optimization|Whether optimal teaching sequences have domain-independent properties; curriculum principles beyond topological sort
OP3|Multi-channel optimization|Joint optimization across text, diagrams, speech, gesture, code; choosing which content on which channel
OP4|Compression ratio ceiling|What determines max referents per token; total domain referents, structural connectivity, processor memory
OP5|Network dissolution dynamics|How shared vocabulary spreads through communities; jargon adoption tipping points; standard emergence
OP6|Total cost measurement protocols|Standardized procedures for measuring each term; composition time, message length, comprehension time/accuracy

# claims(id|claim|type|depends_on)
CL1|For most real-world communication, endpoint processing costs dominate Shannon's channel cost|observation|P1,P3,TC2
CL2|Shannon's framework is recovered as special case when Hp=0 at both endpoints|derivation|P2,FD4
CL3|Expert underestimates receiver cost because dissolved skill is invisible to introspection; structural not empathic failure|derivation|P4,FD8
CL4|Optimal message length increases with dissolution differential; not verbosity but mathematical optimum|derivation|P6,FD12
CL5|No single linear encoding optimizes for heterogeneous audience; layered encoding is the solution|derivation|P7,P8
CL6|Documentation quality is measurable property of document-reader population relationship, not opinion|derivation|FD14,QM1-QM8
CL7|Teaching is communication where goal is changing receiver's dissolution state; optimal encoding is time-varying|derivation|FD15,TP1-TP6
CL8|API quality = functionality per op of consumer processing; consistent conventions dissolve once, apply everywhere|derivation|FD16,AP1-AP8
CL9|Low codebook alignment is most dangerous communication failure: invisible, confident, wrong|observation|AL4,AL5
CL10|Civilization is accumulated stack of dissolution infrastructure and shared compression codebooks|derivation|CS1-CS11
CL11|Every word should have positive dissolution efficiency for target reader; zero or negative efficiency words should be removed|derivation|P5,FD10
CL12|The art of clear writing formalized: optimize total three-term cost, not channel cost alone|derivation|P1,FD12,OS3

# rules(id|rule|rationale)
R1|Estimate receiver dissolution state before encoding; tokens contributing most to differential are where communication will break|Dissolution differential predicts difficulty; intervention follows from identification
R2|Replace high-differential tokens with lower alternatives or add dissolution infrastructure|Increases Hs but reduces Hp(B,decode); worthwhile when differential is large
R3|Every word should have positive dissolution efficiency for target reader population|Words with zero or negative efficiency waste channel without reducing processing cost
R4|For heterogeneous audiences, use layered encoding: base layer compressed, subsequent layers add infrastructure|Each receiver consumes only needed layers; approaches per-receiver optimum
R5|Measure documentation quality through reader processing cost proxies, not opinion|Time on page, lookup rate, completion rate, comprehension score, time to first action
R6|In teaching, adjust encoding in real time based on estimated student dissolution state|Expand when Hp high; compress when concepts dissolve; dynamic optimization
R7|In API design, consistent conventions dissolve once and reduce per-endpoint consumer cost|Naming, parameter ordering, error taxonomy, sensible defaults all reduce receiver Hp
R8|Distinguish high decompression cost (hard but correct) from low alignment (easy but wrong)|High cost → work hard, arrive at intended meaning; low alignment → decompress confidently to wrong meaning

# relationships(from|rel|to)
P1|defines|FD4
P2|recovers|shannon_framework
P3|identifies|FD3_as_dominant
P4|defines|FD8
P5|reframes|redundancy_as_infrastructure
P6|derives_from|FD8,FD12
P7|motivates|P8
P8|solves|P7
FD4|decomposes_to|FD1,FD2,FD3
FD5|enables|FD6,FD7
FD6|grows_with|experience
FD8|predicts|communication_difficulty
FD9|measures|channel_beyond_minimum
FD10|evaluates|DI1-DI10
FD11|extends|FD10_to_audiences
FD12|minimizes|FD4
FD13|detects|AL4,AL5
FD14|formalizes|documentation_quality
FD15|formalizes|teaching_effectiveness
FD16|formalizes|api_quality
OS3|minimizes|FD4
CL1|grounds|P3
CL2|connects|shannon,processing_framework
CL3|derives_from|P4
CL5|derives_from|P7,P8
CL9|identified_by|FD13
CL10|generalized_from|CS1-CS11

# section_index(section|title|ids)
1|The Problem Shannon Solved and Didn't|P1,P2,P3,CL1,CL2
2|The Three-Term Cost Equation|FD1-FD4,TC1-TC7
3|Compression and Decompression|FD5-FD7,CP1-CP5,CR1-CR10
4|The Dissolution Differential|P4,FD8,DD1-DD8,CL3
5|Redundancy as Dissolution Infrastructure|P5,FD9-FD11,DI1-DI10,CL11
6|The Optimization Surface|FD12,OS1-OS3,P6,CL4,CL12
7|The Heterogeneous Audience|P7,HA1-HA8,FD11
8|Layered Encoding|P8,FD18,LE1-LE8,CL5
9|Documentation Quality|FD14,QM1-QM8,CL6
10|Teaching Effectiveness|FD15,TP1-TP6,CL7
11|API Design|FD16,AP1-AP8,CL8
12|Compression Ratio Dynamics|FD17,FD13,AL1-AL5,CL9
13|Civilization as Accumulated Dissolution|CS1-CS11,CL10
14|Scope and Open Problems|OP1-OP6

# decode_legend
three_term_cost: Hp(A,encode) + Hs(channel) + Hp(B,decode); independent, additive; Shannon = special case when endpoints zero
compression: C: referent_space → token (many-to-one); C⁻¹: (token,context) → referent; ratio grows with experience
dissolution_differential: Σₜ [Hp(B,decode(t)) − Hp(A,decode(t))]; predicts difficulty; tokens contributing most = breakdown points
dissolution_efficiency: η = −ΔHp(B) / ΔHs; ops saved per bit added; positive = worthwhile, zero = waste, negative = harmful
optimal_encoding: argmin total cost; between expert-shorthand (min Hs) and verbose-tutorial (min Hp(B)); processing-optimal saddle
layered_encoding: base(expert-compressed) + layers(progressive infrastructure); each receiver consumes needed layers only
codebook_alignment: Jaccard similarity of referent sets; 1.0=perfect, 0.0=total mismatch; low alignment = invisible confident wrong decompression
documentation_quality: content_transmitted / total_cost; reader-relative; measurable through processing cost proxies
teaching: communication where goal = change receiver dissolution state; optimal encoding time-varying; concept ordering = topological sort by dissolution efficiency
api_quality: functionality / Σ(consumer_ops × frequency); consistent conventions dissolve once, reduce per-endpoint cost
civilization: accumulated stack of dissolution infrastructure; each layer freed pipeline for next unsolved problem; progress rate bounded by dissolution infrastructure creation rate
claim_types: observation|derivation
rel_types: defines|recovers|identifies|reframes|derives_from|motivates|solves|decomposes_to|enables|grows_with|predicts|measures|evaluates|extends|minimizes|formalizes|grounds|connects|identified_by|generalized_from
builds_on: HOWL-MATH-14-2026 (processing entropy), HOWL-MATH-17-2026 (metric space) — not cross-referenced; noted for provenance only
+standalone: this doc self-contained
