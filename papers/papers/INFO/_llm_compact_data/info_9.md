# ACHIEVING HIGH OUTPUT AND HIGH QUALITY — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → factors → failure_modes → tests → operating_loop → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|High output and high quality are compatible if and only if two factors are jointly satisfied|Neither alone sufficient; both necessary on every piece; no partial credit
P2|Factor one: experience behind the information|Writer must have encountered the thing — attempted, observed, accumulated obstacle-data and lesson-data from contact with reality
P3|Factor two: usable, falsifiable form|Writing must commit to specific claims that admit verification; receiver must be able to act on, test, and build from what's written
P4|Quality is structural: joint satisfaction of both factors on every claim|Not aesthetic judgment; piece satisfies both = quality regardless of genre/length/style; fails either = not quality regardless of effort
P5|Volume bounded by experience availability and form-discipline consistency, not time-per-piece|Separating factor-supply from text-production dissolves the quality-volume tradeoff
P6|The quality-volume tradeoff is artifact of collapsing factor-supply and text-production into single operation|Separate them and two rate-limits no longer compete
P7|Each piece governed independently; no accumulation of factor credit across pieces|Ten good pieces don't earn one bad piece; factors supplied per-piece not per-career
P8|Dilution under pressure is diagnostic: direction of change reveals whether experience was present|Refinement increases specificity; dilution decreases it; dilution reveals missing factor one

# concepts(id|name|category|definition)
C1|Experience-grounded writing|writing_type|Writer has lived the thing; has obstacle-data, lesson-data, specific failures and corrections from direct contact; residue of contact shows in text
C2|Intellectual writing|writing_type|Writer reasoned about thing but did not encounter it; no obstacle-data or lesson-data; may be internally consistent but lacks specificity experience produces
C3|Derivative writing|writing_type|Writer synthesized others' writing; experience is theirs not writer's, diluted through filter; bounded by source material
C4|Experience availability|factor_component|How much writer has encountered across how many domains; supply curve for factor one
C5|Form-discipline consistency|factor_component|How reliably writer applies commitment-and-falsifiability requirements to every output
C6|Payload|core|The experience-grounded observations, obstacles, lessons, mechanisms that exist before writing starts; writing's job is to transmit it, not generate it
C7|Verification substrate|core|What receiver checks claim against; differs by information type but always exists; factual→reality, principles→repeated application, fiction→internal setup, preferences→behavioral record, values→costly action
C8|Commitment|core|Structural willingness to state specific claims that can be wrong; not editorial polish but stance toward content
C9|Hedging|anti-pattern|Qualifying claims to survive any possible state of the world; protective rather than specifying; each hedge individually looks cautious, collectively the piece claims nothing
C10|Fog vocabulary|anti-pattern|Generic terms that decompress to nothing specific: "stakeholders," "participants," "outcomes," "interventions"
C11|Humility performance|anti-pattern|Ritual expression of uncertainty detached from actual confidence; present whether confidence is high or low
C12|Dilution cascade|anti-pattern|Progressive weakening of committed claims across revision under pressure; "X causes Y" → "sometimes" → "in some cases can influence" → "relationship is complex and context-dependent"
C13|Refinement|core|Experience-grounded writer's response to counterexample: specify conditions that distinguish the counterexample, increasing specificity
C14|Text production|operation|Generating words/sentences/paragraphs; separable from factor-supply; can be done by LLM
C15|Factor-supply|operation|Supplying experience and enforcing form-discipline; human's irreplaceable role; rate-limits quality pipeline
C16|Residue of contact|core|What shows up in experience-grounded text: specificity about obstacles, knowledge of exceptions and why, awareness of what would falsify position
C17|Uncommitted claim|anti-pattern|Sentence consistent with any possible state of the world; has claimed nothing; "complex phenomena require nuanced approaches"

# factors(id|factor|what_it_supplies|what_it_cannot_supply|failure_when_absent)
F1|Experience (factor one)|Payload: specific observations, obstacles, lessons, mechanisms, corrections from direct contact|Form, transmission, commitment, falsifiability|Unusable insight (experience without form) or fabrication (form without experience)
F2|Form (factor two)|Transmission: commitment, specificity, falsifiability, verification substrate, actionability|Payload, reality-grounding, obstacle-data, lesson-data|Shaped nothing that passes formal checks but describes nothing real

# writing_corners(id|corner|output|quality|missing_factor|examples)
W1|High output, low quality|High|Low|Factor one (experience) and/or factor two (form)|Content farms, unsupervised LLM output, institutional schedule-driven publication, commentary synthesizing commentary
W2|Low output, high quality|Low|High|Neither missing but text-production bottlenecked|Serious author with book every few years; careful researcher with one paper per decade
W3|High output, high quality|High|High|Neither — both factors present on every piece|Broadly experienced writer with form-discipline using LLM for text production under factor enforcement

# failure_modes(id|name|factors_present|character|signature|remedy)
FM1|Unusable insight|F1 present, F2 absent|Experience real but no committed claims; payload stays with writer|"More going on than people realize; it's complicated; pay attention to specifics"|Learn committed form; state what you know specifically
FM2|Usable-shaped fabrication|F2 present, F1 absent|Specific, committed, falsifiable claims from reasoning not observation; passes form checks, fails empirical contact|Blueberry-flight: perfect form, zero experience behind it|Acquire experience or stop writing about topic
FM3|Derivative synthesis|F1 absent, F2 variable|Synthesized others' writing; bounded by source material; gaps appear when readers apply to reality|Read ten papers, synthesized, added framing, published|Encounter the thing directly
FM4|Hedging cascade|F1 variable, F2 absent|Every claim qualified; piece survives any state of world|"May," "could," "sometimes," "in some cases," "to some extent" on every claim|Commit or delete; run Popper test per sentence
FM5|Fog vocabulary|F1 variable, F2 absent|Generic terms throughout; appears to be about something but no specific referent|"Stakeholders," "participants," "outcomes," "interventions"|Replace with specific nouns that refer to specific things
FM6|Humility performance|F1 variable, F2 absent|Ritual uncertainty detached from actual confidence|"I might be wrong but perhaps X could be Y though of course I could be mistaken"|Delete ritual; calibrate actual confidence; state it
FM7|Dilution cascade|F1 absent (revealed by pressure)|Progressive weakening under revision pressure; specificity decreases at each step|"X causes Y" → "complex and context-dependent"|Go back to original claim; if experience-grounded, refine (specify conditions); if not, delete
FM8|Missing both|F1 absent, F2 absent|Intellectual content hedged into unfalsifiability; sounds authoritative, says nothing specific|"Results suggest that in some cases the intervention may contribute to improved outcomes among certain participants"|Rebuild from scratch with both factors or abandon
FM9|Confident fabrication with protective hedges|F1 absent, F2 partially present|Form-only fabrication with just enough hedges to survive empirical test|"Blueberries may contribute to enhanced awareness at dawn in coastal environments"|Recognize as fabrication; delete

# experience_test(id|question|what_it_checks|pass_indicator|fail_indicator)
ET1|Did you attempt the thing?|Direct encounter vs reading/reasoning about it|Clear yes with no ambiguity|"Sort of, in a way, partially" = no
ET2|What specific obstacles did you encounter?|Obstacle-data from direct contact|Three specific obstacles that couldn't be generated from reasoning alone|Generic or imagined obstacles
ET3|What specific lessons did you accumulate?|Corrections from obstacles|Specific corrections ("hydration under 65%, add water not knead harder")|Abstract lessons ("learned to be patient")
ET4|Can you answer follow-ups beyond the page?|Whether piece compresses more than writer knows|Answers from knowledge that didn't fit in piece|Answers from on-the-spot reasoning; at edge of knowledge
ET5|Would a practitioner recognize your description?|Whether domain expert engages substantively|Substantive engagement: agree, disagree, refine, extend|Polite confusion: don't know what to say

# form_test(id|question|what_it_checks|pass_indicator|fail_indicator)
FT1|What state of world would make this false?|Falsifiability per sentence|Specific state identified for each sentence|No state would; sentence claims nothing
FT2|What would receiver do to check this?|Verification substrate availability|Substrate identified and accessible to reader|No way for reader to check
FT3|Does each hedge specify real conditions or protect you?|Legitimate vs protective hedging|Hedge replaceable with specific condition|Hedge cannot be replaced with condition; it's protective
FT4|If receiver acted on this paragraph, what would they do differently?|Actionability per paragraph|Specific change in knowledge, skill, belief, or action|Nothing specific; paragraph is furniture
FT5|Can someone summarize your position in one sentence you'd recognize?|Thesis clarity and commitment|Writer's summary matches reader's summary|Summaries diverge or piece resists compression to one sentence

# operating_loop(id|phase|action|timing)
OL1|Before writing|Confirm factor one: name thing encountered, state obstacles and lessons; if cannot → don't write piece|5 minutes; produces specifics or reveals abstractions
OL2|During writing|Enforce factor two live: every sentence specific enough to be false; no fog, no ritual humility, no protective hedging|Concurrent with drafting; harder to fix post-hoc than to write committed from start
OL3|After writing|Run experience test (ET1-ET5) and form test (FT1-FT5) on draft|Before piece goes out
OL4|Under LLM assistance|Human supplies payload and enforces discipline on every LLM draft; LLM handles text production; human checking rate bounds quality pipeline|Per-draft enforcement; not automated
OL5|Across pieces|Maintain both factors on every output independently; no factor credit accumulation|Per-piece, indefinitely

# claims(id|claim|type|depends_on)
CL1|Quality and volume do not trade off; they trade off against missing factors|axiom|P1,P5,P6
CL2|The quality-volume tradeoff is artifact of collapsing factor-supply and text-production into one operation by one human|derivation|P5,P6,C14,C15
CL3|Time-per-piece is not the quality variable; presence of both factors is|derivation|P4,P5
CL4|Experience-grounded writing's volume bounded by experience availability, which for broadly experienced writers doesn't run out quickly|derivation|P5,C4
CL5|Derivative writing bounded in volume by source material; runs out or starts repeating|derivation|C3
CL6|LLM cannot supply experience or enforce discipline on its own output; drifts toward hedging, synthesis, uncommitment|observation|C14,C15
CL7|Deficit in either factor cannot be compensated by excess of the other; factors are orthogonal|axiom|P1,P4
CL8|Direction of change under pressure is diagnostic: refinement increases specificity, dilution decreases it|derivation|P8,C12,C13
CL9|A paper whose current thesis is one you would not have bothered to write is endpoint of dilution retreat|derivation|C12
CL10|Writers with deep craft have always done this implicitly; what's novel is naming factors explicitly and showing joint necessity/sufficiency|observation|P1
CL11|Risk of commitment is asymmetric: committed writer can be wrong and corrected (information); hedged writer claims nothing (no information)|derivation|C8,C9
CL12|Verification substrate exists for every information type; none is exempt|axiom|C7
CL13|Form-discipline is structural commitment built from start, not editorial polish applied at end|derivation|P3,C8
CL14|Volume without experience collapses in one generation of pressure as every piece dilutes|derivation|P8,C12
CL15|Human checking rate bounds quality of LLM-assisted pipeline; most writers check faster than they type so pipeline exceeds solo output|derivation|C14,C15,OL4

# rules(id|rule|rationale)
R1|Confirm experience before drafting; if cannot name obstacles and lessons in 5 minutes, don't write|Missing experience cannot be added through research during draft; produces derivative synthesis with texture of experience
R2|Enforce commitment live during drafting, not post-hoc|Hedging patterns are sticky; harder to edit uncommitted prose into committed than to write committed from start
R3|Run Popper test on every sentence: what state of world makes this false?|Sentences surviving all possible states have claimed nothing; rewrite or delete
R4|For each hedge, attempt replacement with specific condition|If replaceable → refine (legitimate); if not → delete (protective)
R5|Under pressure, check direction of change: increasing specificity = refinement, decreasing = dilution|Dilution reveals missing factor one; remedy is acquire experience or delete piece, not polish diluted version
R6|Under LLM assistance, human supplies payload and enforces discipline on every draft|LLM handles text production; human checking bounds quality; division stable only if human does both parts
R7|Missing experience → acquire or abandon; missing form → commit or delete; missing both → rebuild from scratch|Each deficit has specific remedy; wrong remedy (more revision, more research, more polish) doesn't address either factor
R8|No factor credit across pieces; each piece must independently satisfy both|Ten good pieces don't earn one bad piece

# relationships(from|rel|to)
P1|requires|P2,P3
P1|defines|P4
P4|defines|W3
P5|derives_from|P6
P5|bounded_by|C4,C5
P6|reframes|quality_volume_tradeoff
P7|constrains|all_output
P8|diagnostic_for|C12,C13
C1|satisfies|F1
C2|fails|F1
C3|fails|F1
C4|bounds|P5
C5|bounds|P5
C6|supplied_by|F1
C6|transmitted_by|F2
C7|required_by|F2
C8|component_of|F2
C9|opposes|C8
C10|opposes|C8
C11|opposes|C8
C12|caused_by|F1_absent
C12|revealed_by|external_pressure
C13|requires|F1
C13|opposes|C12
C14|separable_from|C15
C15|rate_limits|W3
C16|produced_by|C1
C17|instance_of|C9
FM1|caused_by|F2_absent
FM2|caused_by|F1_absent
FM3|caused_by|F1_absent
FM4|caused_by|F2_absent
FM7|caused_by|F1_absent
FM8|caused_by|F1_absent,F2_absent
W1|caused_by|F1_absent
W2|caused_by|text_production_bottleneck
W3|enabled_by|F1,F2,C14
CL1|reframes|standard_assumption
CL2|explains|CL1
CL7|constrains|remedies
CL8|implements|P8
CL11|grounds|C8
R1|implements|OL1
R2|implements|OL2
R3|implements|FT1
R4|implements|FT3
R5|implements|P8
R6|implements|OL4
R7|implements|CL7
R8|implements|P7

# section_index(section|title|ids)
1|What You Are Reading This For|P1,CL1
2|The Two Standard Corners|W1,W2,P6,CL2
3|Factor One: Experience|P2,C1,C2,C3,C4,C6,C16,F1
4|Factor Two: Form|P3,C7,C8,C9,C10,C11,C17,F2,CL11,CL12
5|Why Neither Alone Sufficient|CL7,FM1,FM2
6|The Joint Condition|P4,W3
7|The Volume Compatibility|P5,P6,C14,C15,CL2,CL3,CL4,CL5,CL6,CL15
8|Failure Mode Taxonomy|FM1,FM2,FM3,FM4,FM5,FM6,FM7,FM8,FM9
9|The Dilution Cascade|P8,C12,C13,CL8,CL9,CL14,R5
10|The Experience Test|ET1,ET2,ET3,ET4,ET5,R1
11|The Form Test|FT1,FT2,FT3,FT4,FT5,R2,R3,R4
12|The Operating Loop|OL1,OL2,OL3,OL4,OL5,R6,R7,R8
13|Closing|CL1,CL10,P7

# decode_legend
factors: F1(experience)|F2(form) — jointly necessary and sufficient for quality
writing_types: experience-grounded|intellectual|derivative
corners: high-output-low-quality|low-output-high-quality|high-output-high-quality
category_values: core|writing_type|factor_component|operation|anti-pattern
claim_types: axiom|derivation|observation
failure_modes: FM1-FM9 keyed to which factor(s) absent
test_types: experience_test(ET1-ET5)|form_test(FT1-FT5)
loop_phases: before(confirm F1)|during(enforce F2)|after(run both tests)|LLM(maintain both roles)|across(per-piece independence)
hedge_types: legitimate(specifies real condition, increases accuracy)|protective(survives all states, decreases commitment)
dilution_direction: refinement(specificity increases under pressure, F1 present)|dilution(specificity decreases under pressure, F1 absent)
rel_types: requires|defines|derives_from|bounded_by|reframes|constrains|diagnostic_for|satisfies|fails|supplied_by|transmitted_by|required_by|component_of|opposes|caused_by|revealed_by|separable_from|rate_limits|produced_by|instance_of|enabled_by|explains|grounds|implements
+standalone: this doc self-contained
