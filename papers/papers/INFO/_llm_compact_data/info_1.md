# MULTI-DIMENSIONAL INFORMATION INDEXING — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → axes → distinctions → claims → examples → rules → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Every information instance carries full metadata|Single-index storage loses source, time, context, intent — causing false contradictions and cognitive dissonance
P2|Temporal specificity|"True when?" must always be answerable; information without timestamps conflicts rather than coexists
P3|Source tracking with reliability pattern|Who said it, what's their track record, what's their bias — tracked over time, not per-instance authority
P4|Intent inference|Why is source telling me this? What do they gain if I believe it?
P5|Verification depth grading|Each instance graded high/medium/low/none based on independent verifiability, not source authority
P6|Context preservation|Conditions that made information true/relevant must be stored; without context, claims are unverifiable
P7|Outcome tracking|Subsequent reality tested predictions; stored as validation metadata on original instance
P8|Data point accumulation|Observations accumulate into valid structural knowledge; 1→outlier, 5→pattern, 20→valid, 50→structural
P9|Temporary network formation|Connect indexed instances for inspection, validate consistency, extract insight, discard network, keep data point
P10|Preserve instances, downweight don't delete|Superseded information stays indexed with updated weight; pattern-matching capability preserved even when specific hypothesis fails

# concepts(id|name|category|definition)
C1|Single-index storage|anti-pattern|Topic→Current_Belief with accept/reject/conflict as only operations; loses all metadata
C2|Multi-dimensional index|core|Information instance stored with content + source + timestamp + emotional_state + inferred_intent + claimed_origin + verification_level + context + assessment + subsequent_validation
C3|Cognitive dissonance|failure_mode|Result of contradictory information in single-index system that forces accept-one-reject-other
C4|Temporal blindness|failure_mode|No timestamp means information from different eras conflicts rather than coexists
C5|Context collapse|failure_mode|Losing situational conditions that made information valid; "is this good or bad?" without parameters
C6|Source amnesia|failure_mode|Losing who said something, their bias, their intent
C7|Binary verification|failure_mode|True/false with no gradation for verification level or context-dependence
C8|Verification level|core|Grading: high (direct experience, documented), medium (industry benchmark, analysis), low (pattern matching, no direct evidence), none (speculation)
C9|Data point accumulation|core|Observations from diverse sources accumulate into structural knowledge; plural of anecdote IS data when properly indexed
C10|Temporary connection network|core|Ad-hoc network formed across indexed instances to test consistency, extract insight, then discarded
C11|Materiality context-dependence|core|Same value has different materiality at different scales — survival vs lifestyle vs extreme range
C12|Lifestyle range|threshold|Financial difference that affects comfort but not existence; contrasted with survival range and extreme range
C13|Compressed heuristics|core|Methods (Scales, Pseudo-Socratic) are compressed from thousands of indexed instances with outcome feedback
C14|Operational definition|core|Demanding concrete specification when terms are vague; "what does 'as-is' mean?" exposes missing metadata
C15|Downweighting|operation|Reducing confidence in instance given better-verified competing instance, without deleting original
C16|Instance superseding|operation|Higher-verification instance takes precedence for specific question while lower-verification instance preserved
C17|Anti-intellectual gatekeeping|anti-pattern|Dismissing accumulated observations as "mere anecdote" regardless of volume, diversity, and verification depth
C18|Information instance|core|Atomic unit of indexed knowledge: content + full metadata envelope

# axes(id|name|low_pole|high_pole|applies_to)
A1|Verification depth|none (speculation)|high (direct experience, outcome-tested)|C8
A2|Temporal specificity|no timestamp (eternal claim)|full timestamp with context|P2
A3|Source reliability|unknown/untracked|pattern-tracked over time with outcomes|P3
A4|Context richness|context-free claim|fully contextualized with situation, pressures, incentives, constraints|P6
A5|Observation accumulation|single anecdote|structural knowledge (50+ diverse observations)|C9
A6|Materiality scale|survival range (determines existence)|extreme range (requires major life restructuring)|C11

# distinctions(id|side_a|side_b|key_asymmetry)
D1|Single-index storage|Multi-dimensional indexing|Multi-dimensional preserves metadata enabling coexistence of contextually-valid contradictions
D2|Accept/reject binary|Verification-graded assessment|Graded assessment allows partial confidence and context-dependent validity
D3|Overwrite old with new|Preserve old, index new alongside|Preservation retains pattern-matching value and decision-learning context
D4|"Is this true?"|"Under what conditions, from what source, at what verification level?"|Second form is answerable and actionable; first is often meaningless
D5|Authority-based acceptance|Verification-depth assessment|Verification depth tracks independent testability, not social authority
D6|Contradiction (same claim, two values)|Contextual coexistence (two instances, different contexts)|Proper indexing dissolves apparent contradictions into contextual validity

# claims(id|claim|type|depends_on)
CL1|Assuming one correct assessment across all time and context is the core error of single-index thinking|axiom|C1,C4,C5
CL2|Cognitive dissonance is a storage format problem, not an information problem|reframe|C3,C1
CL3|"The plural of anecdote isn't data" is anti-intellectual gatekeeping|reframe|C9,C17
CL4|Once you observe all 50 US states exist, you have complete structural knowledge — no statistical sampling needed|observation|P8
CL5|Outcome consistency correlates with verification depth|derivation|C8,P7
CL6|Multi-dimensional indexing habit was forced by environments that punished single-index thinking|observation|P8
CL7|Information wants to connect; treating it as static, source-less, context-free, time-invariant is mistreating its nature|axiom|C2
CL8|43 years direct experience with outcome feedback is vastly more valid than most published studies for domain-specific knowledge|claim|P8,C8
CL9|Methods emerged as compressed heuristics from thousands of indexed instances|derivation|C13,P8
CL10|Multi-dimensional indexing is cognitively expensive but becomes reflexive through practice|observation|P8

# rules(id|rule|enforcement|rationale)
R1|For each new information piece, ask 7 metadata questions|source, timestamp, context, intent, claimed origin, verification level, future validation|Ensures full indexing rather than single-index storage
R2|Never treat temporal information as eternal|Always attach timestamp and conditions to claims|Prevents temporal blindness (C4)
R3|Never lose source metadata|Track who said it, their track record, their bias|Prevents source amnesia (C6)
R4|Demand operational definitions for vague terms|Ask "what does X mean?" when specification is ambiguous|Prevents context collapse (C5), exposes missing metadata
R5|Downweight rather than delete superseded instances|Keep original with updated weight; preserve pattern-matching capability|Retains learning context and transferable observations
R6|Form temporary networks to validate, then discard|Connect relevant instances, check consistency, extract insight, dispose of network|Enables assessment without permanent structural commitment
R7|Track verification level explicitly|Distinguish direct experience from benchmarks from pattern matching from speculation|Prevents false confidence from low-verification sources
R8|Adjust confidence to verification depth|High-verification instances override low-verification for specific claims|Prevents equal weighting of unequal evidence

# examples(id|setup|lesson|illustrates)
E1|Taliban assessed as allies (1985), enemies (2001), negotiating partners (2021) by same source (US foreign policy establishment)|No contradiction when properly indexed — each assessment contextually valid at its timestamp with different geopolitical context|D1,D6,P2,P6
E2|Practitioner hypothesized Norm MacDonald influenced Unfrozen Caveman Lawyer; timeline evidence showed character predated Norm at SNL by 2 years|Original instance downweighted, not deleted; pattern-matching observation preserved as valid capability; specific hypothesis superseded by higher-verification evidence|C15,C16,P10,R5
E3|AI estimated support costs $50-70K; practitioner corrected to $30-40K based on 25 years hiring experience|Error was contextual, not just numeric — AI assumed high-end tech worker, actual work is email handling with AI assistance; high-verification (direct experience) superseded low-verification (cached benchmark)|C8,D5,P5,R7
E4|"As-is" term in challenge scenario lacked operational definition; practitioner demanded specification|Vague terms hide missing metadata; operational definition exposes what work is actually required, enabling verification|C14,R4,C5
E5|$2M/2yr vs $800K/1yr assessed as "lifestyle range" not "extreme"|Same dollar difference has different materiality at different scales; context (survival vs lifestyle vs extreme) determines significance|C11,C12,A6
E6|Practitioner tracks that customer says they'll pay vs actually pays as different verification levels|Stated intent (low verification) vs demonstrated behavior (high verification) require separate indexing|C8,A1,R7

# integration(id|method|connection_to_framework)
I1|Scales Method|Evaluates using indexed metadata: materiality depends on context (C11), verification depth (C8), timestamp, comparison baseline
I2|Pseudo-Socratic Method|Communicates using indexed metadata: assesses audience state (what they know, source, confidence, gaps), adapts delivery to verification need
I3|Scales + Pseudo-Socratic unified|Scales evaluates on multi-dimensional index; Pseudo-Socratic communicates using index metadata; together = collaborative reasoning under uncertainty

# boundaries(id|boundary|reason|when_single_index_suffices)
B1|Cognitive load is high|Tracking metadata alongside content requires continuous context assessment|Becomes reflexive with practice (43 years observed)
B2|Communication to single-index thinkers is hard|"It depends" sounds wishy-washy; "both can be true" sounds contradictory; "verification levels" sounds pedantic|Practitioner developed translation strategies (CEO analogies, cross-domain translation)
B3|Not all information needs full indexing|Stable facts (math, physics), low-stakes info (restaurant preferences), single reliable source (personal memories) don't benefit|Most valuable for complex multi-source, time-varying, high-stakes domains

# metadata_schema
# The paper defines the following instance structure:
# content|source|timestamp|source_emotional_state|inferred_intent|claimed_origin|verification_level|context(geopolitical,economic,institutional,constraints)|my_assessment_at_time|subsequent_validation

# relationships(from|rel|to)
C1|causes|C3
C1|causes|C4
C1|causes|C5
C1|causes|C6
C1|causes|C7
C2|prevents|C3
C2|prevents|C4
C2|prevents|C5
C2|prevents|C6
C2|prevents|C7
P1|defines|C2
P2|prevents|C4
P3|prevents|C6
P4|component_of|C2
P5|defines|C8
P6|prevents|C5
P7|enables|CL5
P8|grounds|C9
P8|grounds|CL8
P9|defines|C10
P10|defines|C15
C8|enables|R7
C8|enables|R8
C9|opposes|C17
C10|implements|P9
C11|requires|P6
C13|derives_from|P8
C14|prevents|C5
C15|implements|P10
C16|requires|C8
C18|instance_of|C2
I1|operates_on|C2
I2|operates_on|C2
I3|composes|I1
I3|composes|I2
R5|implements|P10
R6|implements|P9
D1|core_distinction_of|C2
CL2|reframes|C3
CL3|reframes|C17
E1|illustrates|D6
E2|illustrates|C15
E3|illustrates|D5
E4|illustrates|C14
E5|illustrates|C11
B1|limits|C2
B3|limits|C2

# section_index(section|title|ids)
1|The Single-Index Problem|C1,C3,C4,C5,C6,C7,CL1,E1
2|Multi-Dimensional Information Indexing|C2,C18,P1,P2,P3,P4,P5,P6,P7,C8
3|Observable Applications in Session|E1,E2,E3,E4,E5,E6,C14,C15,C16
4|Comparison Single-Index vs Multi-Dimensional|D1,D2,D3,D4,D5,D6
5|Data Point Accumulation Principle|P8,C9,C10,P9,CL3,CL4,C17
6|Integration With the Methods|I1,I2,I3,C11,C13
7|Practical Implementation|R1,R2,R3,R4,R5,R6,R7,R8
8|Professional Context and Method Development|CL6,CL8,CL9,CL10
9|Implications and Applications|—
10|Limitations and Boundaries|B1,B2,B3
11|Conclusion|CL7

# decode_legend
verification_levels: high|medium|low|none
category_values: core|anti-pattern|failure_mode|threshold|operation
claim_types: axiom|derivation|observation|prescription|reframe|claim
rel_types: causes|prevents|defines|component_of|enables|grounds|opposes|implements|requires|instance_of|operates_on|composes|core_distinction_of|reframes|illustrates|limits|derives_from
threshold_ranges: survival_range|lifestyle_range|extreme_range
methods_referenced: Scales Method|Pseudo-Socratic Method (defined in separate papers, not cross-referenced)
+standalone: this doc self-contained, no cross-refs to other compact docs
