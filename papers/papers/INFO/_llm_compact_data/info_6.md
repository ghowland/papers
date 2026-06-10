# HOW TO WRITE TECHNICAL DOCUMENTS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → failure_modes → operating_loop → relationships → sections

# principles(id|principle|rationale)
P1|Technical writing is upload|Transfer of a specific thing from writer's head into target reader's head using words as lossy medium. Upload is the test. Everything else is prelude or pretext
P2|Writer bears responsibility for upload|Reader's job is to decode what arrives. Writer's job is to design what arrives so it can be decoded. Upload failure is writer's failure. Blaming reader is abandonment of job
P3|No payload means no writing is possible|If no specific thing exists in writer's head, only text production that looks like writing. Root failure underneath every other failure
P4|Words are compressions pointing to reader's existing dictionary|Word does not carry meaning — triggers retrieval of whatever reader already has associated. Writer controls what's sent, reader controls what's received. Match depends on shared dictionary
P5|There is no neutral content|Every word either deposits payload or wastes budget. Length and payload often inversely related. Low-value words poison attention for subsequent high-value words
P6|Commitment transfers risk correctly|From reader's ability to use text → writer's reputation for accuracy. Uncommitted writer cannot be wrong but absence of wrongness is absence of content. Reader should not bear cost of writer's cowardice

# concepts(id|name|definition|category)
K1|Payload|The specific thing to be installed in reader's head. A claim, model, set of operations, or body of knowledge reader will possess after reading and did not possess before. Not a topic or subject area|core
K2|Target reader|Specific head with specific prior knowledge, vocabulary, reasons for reading. Imagined concretely enough to make word-choice decisions. One primary target, secondary targets get explicit allocated portions|core
K3|Dictionary|Reader's existing compressed referents. Specialist has rich entries; non-specialist has empty slots or vague impressions. Decompression variance: specific referents carry better than abstract ones|medium
K4|Lossy medium|Words are near-total compression of referents. Match between encoding and decoding depends on shared dictionary. No amount of skill eliminates loss — minimize it by choosing compressions target can decompress|medium
K5|Vocabulary matching|Bidirectional operation: specialist words to non-specialist = capacity exceeded, empty slots. Common-word unpacking to specialist = capacity wasted, credibility damaged. Match to target's dictionary, not writer's habitual register|technique
K6|Commitment|Writer's judgment committed to page in form specific enough to be right or wrong. Popper's criterion: what state of world would make this false? If nothing, sentence claims nothing|technique
K7|Budget discipline|Writer has word count, reader has attention and working memory. Both finite. Cut every word that doesn't deposit payload. Shorter document with same payload transmits better|technique
K8|Preflight simulation|Simulate target reader hitting each sentence. Writer's own reading worthless — they decompress from original referent, not from text alone. Detect where text fails to transmit before publication|technique
K9|Master document|Authoritative version written to ideal target without dilution. Derivatives for other audiences are downstream products with explicit trade-offs. Master keeps derivatives honest|technique
K10|Feedback filtering|Filter question: does acting on this improve transfer to intended target? If yes, incorporate. If no, discard regardless of reviewer seniority or social pressure. Reviewer satisfaction ≠ target transfer|technique
K11|Platforms in document structure|Explicit "you should now have X" markers at transitions. Delegates assessment loop to reader. Makes document self-auditing. Readers repair misunderstanding at checkpoint instead of propagating it|technique
K12|Examples as compression-failure detectors|Reader whose decompression went wrong fails the example depending on correct decompression. Without examples, wrong decompressions propagate undetected through rest of document|technique

# failure_modes(id|name|violates|description|mechanism)
FM1|Hedging|K6|Sentence refuses to be falsifiable. Reader receives no claim. Most common failure, most institutionally rewarded — hedged sentences cannot embarrass publisher|"Results suggest intervention may have contributed to improved outcomes in some participants" — consistent with any state of world
FM2|Fog vocabulary|K5|Bag-of-everyone words that decompress to nothing specific. "Participants," "individuals," "stakeholders," "users." Writer avoids committing to who or what|"Individual" is no one. "John" is a specific person. Fog produces blank where specific referent should be
FM3|Fancy vocabulary|K5|Specialist words used when common words carry payload. Register-membership performance rather than transmission. Reader either fails to decompress or notices performance|"Interlocutor" when "speaker" works. "Utilize" when "use" works. Attention extracted, less returned than common vocabulary
FM4|Humility performance|K6|Ritual self-deprecation replacing claim. Humility detached from reality — present regardless of actual confidence. Four humility tokens and no claim|"I might be wrong but perhaps X could be Y in certain cases though of course I could easily be mistaken"
FM5|Numbers around vagueness|K6|Quantitative precision in easy parts (counts), fog in load-bearing parts (outcomes). Appears rigorous from numbers, actual claim unfalsifiable|"24 of 34 participants received moderate benefits" — numerator precise, "moderate benefits" soft
FM6|Padding|K7|Words added because document felt too short, reviewer asked for more, template required length. Each word dilutes payload density and exhausts reader attention|25,000-word versions of seven-word truths. Writer can defend every sentence, document still fails

# operating_loop(id|phase|action|checkpoint)
OL1|Before writing|Confirm specific payload — state in one sentence. Confirm target — one primary reader, construct ideal if no demographic fits|If payload unstatable in one sentence: stop. If target still vague: stop. Downstream decisions unmakeable
OL2|During writing|Choose vocabulary against target's dictionary. Commit to falsifiable claims. Cut non-payload words. Build platforms for reader self-audit. Include examples as compression-failure detectors|Every sentence: what state of world makes this false? Every word: does it deposit payload?
OL3|After writing|Simulate target reader's encounter sentence by sentence. Revise where simulation shows failure. Own reading worthless — dictionary fills in what text omits|Draft writer finds clear ≠ draft reader finds clear. Simulation detects gap
OL4|In review|Filter feedback against target. One test per piece of feedback: does acting on this improve transfer to target? Discard if no, regardless of source|Saying no to reasonable-sounding feedback is part of discipline
OL5|Across documents|Maintain master for specialized targets. Produce derivatives deliberately with trade-offs acknowledged. Master is reference, derivatives are projections|Readership loss on masters is cost of fidelity. 50 readers who build > 50,000 who skim

# diagnostic_questions(id|question|pass|fail)
DQ1|What should reader be able to do/decide/believe after reading that they couldn't before?|Concrete answer|Vague ("understand better," "be informed," "have context")
DQ2|What specific thing is supposed to end up in reader's head?|Specific claim, model, operations, or knowledge|Topic or subject area ("databases," "the new API")
DQ3|What does target reader already know? What words do they have compressed?|Specific answers about prior knowledge and vocabulary|"The audience" or "users" — no specificity
DQ4|For each sentence: what state of world would make this false?|Specific falsifying condition exists|Nothing would — sentence claims nothing
DQ5|For each word: does it deposit payload?|Yes — contributes to upload|No — padding, hedging, performance, decoration
DQ6|Does acting on this feedback improve transfer to intended target?|Yes — incorporate|No — discard regardless of source

# relationships(from|rel|to)
P1|defines|K1,K2,K4
P2|assigns|responsibility to writer
P3|grounds|K1
P4|explains|K3,K4
P5|grounds|K7
P6|grounds|K6
K1|prerequisite_for|all downstream steps
K2|prerequisite_for|K5
K3|determines|K5
K4|constrains|P1
K5|repairs|FM2,FM3
K6|repairs|FM1,FM4,FM5
K7|repairs|FM6
K8|compensates_for|K4
K9|anchors|derivatives
K10|protects|K1 from reviewer drift
K11|delegates|assessment to reader
K12|detects|decompression failure
FM1|violates|K6
FM2|violates|K5
FM3|violates|K5
FM4|violates|K6
FM5|violates|K6
FM6|violates|K7

# section_index(section|title|ids)
1|What You Are Reading This For|—
2|The Goal|P1,P2
3|The Payload|P3,K1,DQ1,DQ2
4|The Target|K2,DQ3
5|The Medium|P4,K3,K4
6|Vocabulary Matching|K5,FM2,FM3
7|Commitment|P6,K6,FM1,FM4
8|The Failure Modes|FM1-FM6
9|Budget Discipline|P5,K7,FM6
10|Preflight Simulation|K8,K11,K12
11|Feedback Filtering|K10
12|The Master Document|K9
13|The Operating Loop|OL1-OL5
14|What You Can Now Do|—
15|Closing|P1

# decode_legend
categories: core|medium|technique
failure_mechanism: each failure violates a specific platform — repair by reference to violated platform
rel_types: defines|assigns|grounds|explains|determines|constrains|repairs|compensates_for|anchors|protects|delegates|detects|violates|prerequisite_for
id_prefixes: P=principle|K=concept|FM=failure_mode|OL=operating_loop_phase|DQ=diagnostic_question
loop_nature: not checklist completed once — practice run every time. With repetition, steps compress into integrated act. Diagnosis = "which step broke?"
master_vs_derivative: master optimizes fidelity to target. Derivative optimizes reach with explicit trade-offs. Neither replaces other
