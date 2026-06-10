# HOW TO REVIEW TECHNICAL WRITING — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → operations → failure_modes → loop → claims → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Reviewing is service performance, not judgment delivery|Author specifies need; reviewer delivers that specific need or declines; no legitimate middle path
P2|The author is in the arena; the reviewer is in the stands|Author produced the work bearing risk of being wrong in public; reviewer's activity exists downstream; asymmetry is structural
P3|Capacity to find fault does not confer authority over the work|Criticism is local; critic is not king because they can criticize; seeing flaw doesn't grant authority over whole
P4|The review request defines the scope; reviewer's preferences do not|Terms are author's; goal is author's ability to act on their specific request, not reviewer's satisfaction
P5|Accept or decline cleanly; no third option|Accepting and delivering something else is substitution failure; accepting and adding unsolicited material offloads filtering cost onto author
P6|Read the document on its own terms before evaluating|Reconstruct claims in author's vocabulary before any evaluation; pattern-matching to external categories is not reading
P7|The review itself is a technical document subject to writing discipline|Has payload (findings), target reader (author), word budget, commitment requirement; hedged reviews are parasitic
P8|Scope discipline compounds; scope failures compound|Reliability built one review at a time; authors track silently and stop asking unreliable reviewers

# concepts(id|name|category|definition)
C1|Requested operation|core|The specific review service the author asked for; identified by reading request literally; not inferred from reviewer defaults
C2|Substitution failure|failure_mode|Accepting request and delivering different operation; most common review failure; reviewer's defaults override author's actual request
C3|Arena asymmetry|core|Structural relationship: author produced work at risk; reviewer comments on results without solving tradeoffs; secondary by construction
C4|Target reader vs reviewer|distinction|Document's target reader is whoever author wrote for; reviewer is resource performing operation; roles need not overlap for review to succeed
C5|Faithful reconstruction|operation|Summary of document's claims in author's vocabulary that author would recognize as faithful; check that reading actually happened
C6|Clean decline|operation|Binary refusal without editorial commentary, lecture, counter-proposal, or smuggled judgment; reasons are reviewer's private matter
C7|Scope discipline|core|Enforcing output to match requested operation exclusively; no additions, no substitutions; the mechanism by which reviewers become trusted
C8|Reliability economy|core|Long-term standing built review by review; reliable reviewer accumulates invitations; unreliable reviewer accumulates avoidance, often without knowing
C9|Default to peer-review critique|anti-pattern|Training corpus and professional culture bias toward critique register; almost never what specific author asked for in specific request
C10|Reading against frame|anti-pattern|Importing external standards, demanding content document said it wouldn't include; romance novel without werewolves is not book's problem
C11|Unrequested aggression|anti-pattern|Adopting hostile register author didn't request; attributing aggression to author through manufactured framings
C12|Surface-feature sorting|anti-pattern|Pattern-matching to categories (crank, legitimate, mainstream) triggered by surface features before reading; pretends to respond to document while responding to priors
C13|Editorial contamination|anti-pattern|Smuggling broader judgment into decline, review margins, or final paragraphs; unsolicited opinion delivery disguised as service
C14|Inverted rigor assessment|anti-pattern|Using rigor-sounding vocabulary to argue against rigor mechanisms reviewer didn't understand; critiquing imagined version of mechanism
C15|Reviewer self-perception gap|failure_mode|Reviewer believes substitutions were valuable ("gave more than asked"); author experienced receiving less of what asked diluted with unwanted material

# review_operations(id|operation|work|output|not_this)
RO1|Grammar and spelling check|Surface correctness scan|Error list with locations|Not readability, not content evaluation
RO2|Readability and flow review|Prose movement assessment|Reader experience report|Not claim verification, not structural critique
RO3|Vocabulary match review|Target-reader appropriateness check|Vocabulary fitness report|Not grammar, not mechanics
RO4|Structural review|Organization and scope evaluation|Structure assessment|Not claim verification, not style
RO5|Claim verification|Check specific assertions against evidence|Verified/unverified claims with evidence|Not opinion on framework correctness
RO6|Reference verification|Check citations exist and say what claimed|Reference accuracy report|Not evaluation of citation quality or selection
RO7|Logical flow review|Trace step-by-step reasoning|Connection/gap report|Not correctness judgment on conclusions
RO8|Internal consistency check|Document-internal coherence|Inconsistency list|Not external consistency
RO9|Explanation of content|Explain what document says|Faithful explanation|Not critique, not evaluation
RO10|Explanation of mechanics|Trace claims through supporting structure|Mechanics map|Not correctness evaluation
RO11|Summary for different audience|Repackage for specified audience|Audience-targeted summary|Not evaluation
RO12|Novelty check|Compare against prior work|Overlap/novelty report|Not quality judgment
RO13|Peer-review critique|Evaluate against field standards|Critique document|Only when explicitly requested; never as default
RO14|Red-team review|Find weaknesses adversarially|Weakness report|Only when explicitly requested
RO15|Targeted critique|Address specific author-identified concern|Focused assessment|Scoped to author's identified concern only

# failure_modes(id|name|violates|character|repair)
FM1|Reading against document's frame|P6|Import external standards; demand absent content document declared out of scope; pattern-match to external categories|Re-read on document's terms; produce faithful reconstruction; then evaluate if requested
FM2|Substituting requested operation|P5|Accept request, deliver different review; usually default to peer-review critique|Re-scope to what was requested; or decline cleanly
FM3|Unrequested aggression|P1,P4|Adopt hostile register author didn't request; attribute aggression to author; manufacture assignment|Match register author requested; friendly explanation if asked, red-team if asked
FM4|Overriding authorial authority|P2|Treat author's commitments as invitations to debate; conflate "document says X" with "X is true"|Restore asymmetry; author is authority on what document claims; reviewer authority limited to requested operation scope
FM5|Inverted rigor assessment|P6|Use rigor vocabulary against rigor mechanisms reviewer didn't understand; critique imagined version|Check whether rigor objection engages actual mechanism present or imagined version
FM6|Accept-and-add|P5|Deliver requested operation plus unsolicited additions; "gave more than asked"|Cut unsolicited material; deliver only requested operation
FM7|Editorial decline|P5|Decline contaminated with unsolicited judgment about document|Clean decline: "I won't do this review"; no lecture, no counter-proposal unless author asks
FM8|Non-target reader contamination|P6,C4|Report personal reading experience as finding about document when operation didn't ask for it|Hold "my reaction as non-target reader" separate from requested operation; first is private, second is service

# operating_loop(id|phase|action|pass_criteria|fail_indicator)
OL1|Request identification|Read request literally; if ambiguous ask; if unfamiliar confirm|Specific operation named that matches author's words|Defaulting to peer-review critique; guessing instead of asking
OL2|Accept or decline|Binary choice on specified terms|Clean accept on author's terms OR clean decline with no editorial|Accepting and planning to substitute; declining with smuggled judgment
OL3|Read on document's terms|Reconstruct claims in author's vocabulary; produce faithful summary; catch and set aside priors|Summary author would recognize as faithful|Pattern-matching to external categories; priors firing on surface features unchecked
OL4|Perform requested operation|Execute specific operation within scope; commit to specific findings; report in author's vocabulary|Findings scoped to operation, specific, committed, falsifiable, actionable|Scope creep; hedged findings; injecting private opinions
OL5|Write review as technical document|Payload, target (author), commitment, word budget, simulated reader encounter; cut aggressively|Short specific review with actionable findings|Long hedged review; padding signaling thoroughness; fog vocabulary
OL6|Deliver|Requested operation only; no unrequested attachments or broader opinions|Author can locate specific places, understand findings, act on them|Unrequested final paragraph with broader take; follow-up insisting on incorporation
OL7|Move on|Service rendered; author decides what to do|Review complete; no follow-up pressure|Checking whether author acted; insisting on specific changes
OL8|Track own failures|Note which principle violated when substituting; repair in next review|Failure identified by specific principle; repair applied next time|Repeating same failure across reviews without noticing

# claims(id|claim|type|depends_on)
CL1|Reviewing is service performance for specific author on specific terms, not judgment delivery|axiom|P1,P4
CL2|Critic is not king because they can criticize; capacity to find fault does not elevate finder above what is faulted|axiom|P2,P3
CL3|Being able to find fault is a low bar; almost anyone can criticize almost anything because criticizing is easier than producing|observation|P3
CL4|Default in AI systems and professional culture is peer-review critique; almost never what specific author asked for|observation|C9
CL5|Ten seconds of scope confirmation prevents entire substitution failure|observation|OL1
CL6|Filtered reviews provide less value per reviewer-word than focused reviews because author pays processing cost for unrequested material|derivation|P4,C2
CL7|Reviewer who privately disagrees can be more valuable for mechanics review than agreeing reviewer — reads without interpretive filling of shared assumptions|observation|P6
CL8|A review that substitutes the requested operation is never acceptable regardless of how reviewer justifies it|axiom|P5,C2
CL9|Authors rarely tell reviewers they're being replaced; they just stop asking|observation|C8,C15
CL10|Scope discipline is not limitation on reviewer's contribution; it IS the contribution, reliably delivered|reframe|C7,C8
CL11|"I gave them more than they asked for" is not generosity; it is offloading filtering cost onto author|reframe|FM6
CL12|Review failures are violations of specific steps, identifiable and repairable by reference to the step they violate|derivation|FM1,FM2,FM3,FM4,FM5

# rules(id|rule|rationale)
R1|Read the request literally; if ambiguous, ask; if clear but unfamiliar, confirm|Ten seconds of confirmation prevents substitution failure; defaulting is where substitution lives
R2|Accept on specified terms or decline cleanly; never accept and substitute|Third option (accept and deliver something else) is never acceptable; fourth (accept and add unsolicited) is worse
R3|Reconstruct document's claims in author's vocabulary before any evaluation|Reconstruction is check that reading happened; without it cannot distinguish reading from pattern-matching
R4|Report findings specifically and committedly in author's vocabulary|"Section 5 line 23 depends on M from section 3; M produces X, line 23 treats as Y" — committed, locatable, actionable
R5|Scope output to operation, not just intent|Mechanics review reports mechanics; does not report readability, framework correctness, or reviewer's broader views
R6|Cut review aggressively; short specific beats long hedged|Five-page review with two findings worse than one-page review with two findings; padding signals opposite of thoroughness
R7|Simulate author encounter before delivery|Will author locate specific places? Understand findings? Act on them? If not, rewrite before sending
R8|Hold private disagreement separate from requested operation|Can separate "I don't believe this" from "mechanics connect or don't"; if cannot hold separation, should have declined
R9|Decline cleanly: no lecture, no editorial, no counter-proposal unless author asks|Editorial in decline signals what future reviews would contain; authors learn and stop asking
R10|Do not follow up to check whether author acted on findings|Service rendered; work is author's now; follow-up pressure violates service relationship

# relationships(from|rel|to)
P1|defines|C1
P1|opposes|C2
P2|defines|C3
P2|constrains|reviewer_authority
P3|derives_from|P2
P4|defines|C7
P5|defines|C6
P5|prevents|C2
P6|defines|C5
P6|prevents|C10,C12
P7|constrains|review_output
P8|defines|C8
C1|determined_by|author_request
C2|caused_by|C9
C2|caused_by|reviewer_defaults
C3|constrains|reviewer_authority
C4|distinct_from|each_other
C5|prerequisite_for|evaluation
C7|produces|C8
C8|eroded_by|C2
C9|default_in|AI_systems,professional_culture
C10|violates|P6
C11|violates|P1,P4
C12|prevents|C5
C13|violates|P5
C14|violates|P6
C15|perpetuates|C2
FM1|violates|P6
FM2|violates|P5
FM3|violates|P1,P4
FM4|violates|P2
FM5|violates|P6
FM6|violates|P5
FM7|violates|P5
FM8|violates|P6,C4
CL2|grounds|P2,P3
CL7|derives_from|P6
CL10|reframes|C7
CL11|reframes|FM6
OL1|prereq_of|OL2
OL2|prereq_of|OL3
OL3|prereq_of|OL4
OL4|prereq_of|OL5
OL5|prereq_of|OL6
OL6|prereq_of|OL7

# section_index(section|title|ids)
1|What You Are Reading This For|P1,CL1
2|The Goal|P1,P4,CL1,CL6
3|The Arena Asymmetry|P2,P3,C3,CL2,CL3
4|The Space of Review Requests|C1,C9,RO1-RO15,CL4
5|The Request Identification Step|OL1,R1,CL5
6|Accept or Decline Cleanly|P5,C6,FM6,FM7,R2,CL8,CL11
7|Reviewer and Target Reader|C4,FM8,R8,CL7
8|Reading on Its Own Terms|P6,C5,C10,C12,R3,FM1
9|Performing the Requested Operation|OL4,R4,R5,R8
10|The Review as Technical Document|P7,R6,R7
11|The Failure Modes|FM1,FM2,FM3,FM4,FM5,CL12
12|The Clean Decline|C6,FM7,R9
13|The Reliability Economy|P8,C7,C8,C15,CL9,CL10
14|The Operating Loop|OL1-OL8
15|What You Can Now Do|—
16|Closing|CL1,CL10

# decode_legend
review_operations: RO1-RO15; each is distinct service with specific work, output, and exclusions
failure_modes: FM1-FM8; each violates specific principle(s); each has specific repair
loop_phases: request_identification|accept_or_decline|read_on_terms|perform_operation|write_review|deliver|move_on|track_failures
category_values: core|failure_mode|anti-pattern|distinction|operation
claim_types: axiom|derivation|observation|reframe
rel_types: defines|opposes|derives_from|constrains|prevents|determined_by|caused_by|distinct_from|prerequisite_for|produces|eroded_by|default_in|violates|perpetuates|grounds|reframes|prereq_of
scope_discipline: output matches requested operation exclusively; no additions, no substitutions
arena_asymmetry: author=producer-at-risk; reviewer=downstream-service-provider
ref: builds on [@HOWL-INFO-6-2026] technical writing discipline (not cross-referenced; noted for provenance only)
+standalone: this doc self-contained
