# THE SCALES METHOD — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → components → algorithm → applications → limitations → relationships → sections

# principles(id|principle|rationale)
P1|Materiality-first assessment|Distinguish materially impactful from merely relevant. Higher bar than "is this relevant?" — prevents analysis paralysis, false equivalence, wasted effort on non-material factors
P2|Quantify scope after establishing materiality|After boolean materiality determination, ask what percentage of cases are materially affected and whether that percentage is non-negligible. Prevents overgeneralizing from edge cases
P3|Multi-dimensional weighted synthesis|Simultaneously evaluate multiple factors with context-dependent weights. Optimize across weighted dimensions rather than satisfying constraints sequentially
P4|Probabilistic rather than binary conclusions|Express conclusions as weighted likelihoods — "likely true," "extremely low chance," "10-15% material impact." Honest representation of uncertainty with room for revision
P5|Fruit of the plant validation|When stated goals exist, observed outcomes align, intermediate steps are consistent, and no simpler explanation fits — hypothesis gains weight even without direct proof. Outcome-based reality check
P6|Proper baseline selection|Material impact depends on comparison point. Compare against actual status quo, not hypothetical ideal. Wrong baseline produces wrong materiality assessment

# components(id|name|definition|function)
K1|Materiality threshold|Threshold function: impact → {material, non-material}. Material iff changes outcome significantly, affects non-negligible percentage, cannot be easily mitigated, alters decision space|Primary filter — reduces cognitive load by eliminating non-material factors early
K2|Scope quantification|Percentage-based assessment of material factors. <5% likely negligible, 5-20% minor concern, 20-50% significant, 50-80% major, >80% critical|Converts vague concerns to specific numbers. Prevents treating 5% concerns as 95% concerns
K3|Weight assignment|Context-dependent weights on factors determined by goals, constraints, risk tolerance. Same factor has different weight in different contexts. Dynamic adjustment as context evolves|Enables trade-off navigation — low-weight factors sacrificed for high-weight gains
K4|Fruit of the plant|Hypothesis strength = consistency(goals, outcomes) × consistency(intermediate steps, both) × (1/simplicity of alternatives). Accept as likely operative if above threshold|Catches elegant-but-wrong theories. Validates without direct proof. Reality check on theoretical reasoning
K5|Comparison baseline|The reference point against which impact is measured. Must be actual status quo, not hypothetical ideal|Wrong baseline produces systematically wrong materiality assessments

# algorithm(id|step|action|output)
A1|Decompose|Break complex situation into component factors. Identify all relevant dimensions|Factor list
A2|Assess materiality|For each factor: does this materially impact the outcome? Use threshold function, not "has some effect"|Material factors filtered from non-material
A3|Quantify scope|For material factors: what percentage of cases affected? Is percentage non-negligible?|Percentage-based impact assessment
A4|Weight factors|Assign weights based on context and goals. Consider interaction effects between factors|Weighted factor set
A5|Synthesize|Calculate weighted assessment across all material factors. Generate probabilistic conclusion|Overall assessment (usually probabilistic, not binary)
A6|Validate|Check fruit of the plant — do outcomes match? Do conclusion's implications match reality? Adjust weights if inconsistencies detected|Validated or revised conclusion

# applications(id|context|method_applied|before|after|mechanism)
AP1|AI safety framework criticism|Explicit materiality assessment of five criticisms|60-75% material impact (framework compromised)|10-15% material impact (framework viable)|Two corrections: (1) credentialed bad actors already have knowledge → material impact = 0%. (2) Compare against actual status quo not ideal → framework is improvement
AP2|Credentialed bad actor error|Materiality reframing|"Framework increases risk by giving experts access"|"Experts already possess knowledge, AI is just another reference source. Material impact = 0%"|Logical error: framework doesn't grant new capabilities. Problem is "malicious" not the credential
AP3|Layered access system design|Multi-dimensional weighted optimization|Binary credentialed/not|Weighted multi-dimensional space: depth (0-N levels) × competence (demonstrated) × credentials (formal/practical) × topics (unrestricted count)|Optimized across universal access + safety + flexibility + competence simultaneously
AP4|Double-ended exponential (maxim creation)|Decomposition + scale assessment|"AIs aren't creative enough"|Compression (10^n experiences → 10^3 phrases) × validation (evoke meaning across 10^m people) = compound exponential = computationally intractable|Probabilistic conclusion: "extremely low chance" not "impossible"
AP5|Norm MacDonald analysis|Multi-dimensional weighted character assessment|"Funny comedian who played dumb"|Linguistic intelligence + character consistency (kayfabe) + delivery mechanism (Yogi-style) + audience effect (felt they thought of it themselves) = modern jester with plausible deniability|Fruit of the plant: speculation itself is "Norm-shaped" — unprovable ambiguity
AP6|CEO communication strategy|Trade-off optimization across weighted factors|Technical precision in language|Drop tech language, use cross-domain analogies (sports, physics). Sacrifice jargon for understanding|Validated by 25 years successful application. Structural isomorphism > surface similarity
AP7|Adaptive depth matching|Continuous weighted signal evaluation|Fixed depth for all users|User signals (terminology +1, concept application +2, edge cases +1, novel connections +2) → weighted sum → estimated competence → appropriate depth. Struggle detection = negative weight → backtrack to prerequisite|Dynamic re-weighting as conversation progresses

# error_correction_patterns(id|error_type|practitioner_correction|scales_mechanism)
EC1|Logical error in materiality|"Malicious structural engineer" — I claimed framework increased risk|Experts already have knowledge. Material impact = 0%. Dismissed as non-material|Materiality threshold exposes that relevant ≠ materially impactful
EC2|Wrong comparison baseline|I compared framework against ideal secure system|Compare against actual current AI behavior: unpredictable blocking, session termination, zero security benefit, significant friction|Proper baseline selection changes entire assessment
EC3|Overgeneralization of impact|60-75% material impact claimed|After corrections: 10-15% material impact. Distinction critical — "viable with caveats" vs "fundamentally flawed"|Percentage quantification prevents treating edge cases as general

# limitations(id|limitation|mitigation)
LM1|Subjectivity in weight assignment|Explicit articulation of weights/thresholds. Fruit of the plant validation. Willingness to revise based on outcomes
LM2|Requires domain knowledge for materiality assessment|Practitioner corrects assessments. Pseudo-Socratic questioning exposes gaps. Collaborative application leverages combined knowledge
LM3|Fruit of the plant can mislead (correlation ≠ causation)|Probabilistic conclusions ("likely" not "definitely"). Multiple consistency checks. Acknowledgment of uncertainty
LM4|Materiality threshold may dismiss later-important factors|Context-dependent thresholds. Explicit about efficiency trade-off. Revisit if fruit doesn't match expectations

# characteristics(id|characteristic|description|contrast)
CH1|Non-binary assessment|Weighted likelihood, degrees of materiality, optimization across dimensions|Not true/false, relevant/irrelevant, good/bad
CH2|Context-dependent weights|Same factor has different weight in different contexts. Dynamic adjustment|Not fixed scoring rubric
CH3|Probabilistic conclusions|"Likely true," "low probability," "extremely low chance"|Not "definitely" or "impossible"
CH4|Outcome validation built in|Fruit of the plant consistency checking. Revise weights based on results|Not purely theoretical — maintains empirical grounding
CH5|Rapid convergence under correction|Explicit materiality + quantification exposes errors efficiently. Two corrections: 60-75% → 10-15%|Not iterative polishing — structural diagnosis
CH6|Self-applicable|Can assess its own materiality, scope, and effectiveness using its own method|Meta-consistent

# development_hypothesis(id|claim|evidence)
DH1|Method emerged from decades of professional necessity|Infrastructure ops requires: materiality (critical vs non-critical failures), quantification (% users affected), weighting (multiple constraints), validation (fixes actually work)
DH2|Entrepreneurship reinforced the method|Market sizing = scope quantification. Trade-offs = weighted optimization. Product-market fit = fruit of the plant
DH3|Communication adaptation demonstrates meta-awareness|Consciously optimizing communication strategy across weighted dimensions (audience knowledge, transfer goal, mechanisms, preservation) = systematized evaluation methodology
DH4|Method is implicitly teachable through application|Practitioner taught method by requesting materiality ratings, correcting assessments, reframing baselines, demonstrating validation. Transferable without explicit theory instruction

# relationships(from|rel|to)
P1|grounds|K1
P2|grounds|K2
P3|grounds|K3
P4|grounds|CH1,CH3
P5|grounds|K4
P6|grounds|K5
K1|feeds|A2
K2|feeds|A3
K3|feeds|A4
K4|feeds|A6
K5|feeds|A2
A1|enables|A2
A2|enables|A3
A3|enables|A4
A4|enables|A5
A5|enables|A6
A6|may_revise|A4
AP1|demonstrates|A1-A6
AP2|demonstrates|K1,EC1
AP3|demonstrates|P3,K3
AP4|demonstrates|P4,CH3
AP5|demonstrates|K4,CH3
AP6|demonstrates|K3,K4
EC1|demonstrates|K1
EC2|demonstrates|K5
EC3|demonstrates|K2

# section_index(section|title|ids)
1|Introduction|P1,P2,K1,K2
2|Core Principles|P1-P6,K1-K5
3|Application: Material Impact Analysis|AP1,AP2,EC1,EC2,EC3
4|Application: Layered Access Proposal|AP3
5|Application: Adaptive Depth Matching|AP7
6|Application: Maxim Creation Analysis|AP4
7|Application: Norm MacDonald Analysis|AP5
8|Communication Strategy|AP6,DH3
9|Theoretical Framework|A1-A6,K1-K5
10|Comparison With Other Frameworks|CH1-CH6
11|Applications Summary|AP1-AP7
12|Distinctive Features|CH1-CH6
13|Effectiveness Evidence|EC1-EC3,CH5
14|Inferred Development|DH1-DH4
15|Limitations|LM1-LM4
16|Synthesis: Why It Works|CH5,K1,K2,K4
17|Meta-Characteristics|CH6,DH4
18|Practical Application Guide|A1-A6
19|Conclusion|P1-P6

# decode_legend
materiality_scale: <5% negligible|5-20% minor|20-50% significant|50-80% major|>80% critical
algorithm_steps: decompose → assess materiality → quantify scope → weight → synthesize → validate
signal_weights_example: terminology +1|concept application +2|edge cases +1|novel connections +2|struggle -2
rel_types: grounds|feeds|enables|may_revise|demonstrates
id_prefixes: P=principle|K=component|A=algorithm_step|AP=application|EC=error_correction|LM=limitation|CH=characteristic|DH=development_hypothesis
core_quote: "typically a case is either 'impacted' or 'not materially impacted', so it becomes boolean, and then the question becomes, 'what percent is materially impacted, and is that percentage non-negligible?'"
fruit_of_the_plant: when goals exist + outcomes align + steps consistent + no simpler explanation → hypothesis gains weight without direct proof