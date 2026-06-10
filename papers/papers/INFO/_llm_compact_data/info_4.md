# HOWLAND'S AXIOM OF INFORMATION LOCALITY — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: axiom → concepts → formula → examples → related → claims → relationships → sections → decode_legend

# axiom
# "For a unique set of information, if a decision needs to be made and accuracy is critical, all non-local data is invalid."

# concepts(id|name|category|definition)
C1|Unique Information Set (UIS)|core|Any state abstracted into single entity; could be physical unit at moment in time, or physical unit across lifespan; nothing anonymous, nothing random; particular local set of information with population size of one
C2|Accuracy-Critical (AC)|condition|Decision about UIS must provide highest chances to succeed with specified goals, yielding best results possible under realities of the situation; error is not acceptable
C3|Local-Data-Only (LDO)|property|Problem where only data inside the stated unique set is valid; non-local (external) data is invalid for decision-making
C4|Non-local data|core|Anything not inside the stated unique set; includes statistical data about populations, manufacturing defect rates, external benchmarks; may be statistically significant for populations but does not describe exact state of this single unit's single instance
C5|Local data|core|Information contained within the unique set as defined by how you are looking at the problem; for physical objects maximum available in "now" moment; for computer data self-contained and equivalent across snapshots
C6|Problem framing determines locality|core|What is local vs non-local depends on how you define the problem; problem definition determines information set boundary
C7|Physical vs non-physical data distinction|core|Physical objects: local data maximal at "now" moment (can look for data, then related data); non-physical (computer data): self-contained, snapshot equivalence across time
C8|Population-of-one|core|When treating something as UIS, population size is one; all state data is unique and local to that single unit's single instance; no external data can determine anything about it

# formula
# Given UIS, if AC is True, then LDO is True.
# Variables: UIS (Unique Information Set) | AC (Accuracy-Critical) | LDO (Local-Data-Only)

# examples(id|scenario|why_LDO)
E1|Driving and encountering an obstacle|Only local data (road surface, obstacle position, vehicle state, driver state right now) valid for immediate decision; population statistics about obstacles irrelevant to this specific encounter
E2|Walking up stairs and missing the step|Your specific body position, momentum, stair geometry right now; average stair dimensions irrelevant
E3|Rotating disk drive intermittently performs slowly|This drive's specific physical and magnetic state now; manufacturing defect rates for this model don't describe this drive's actual state
E4|Adding feature to existing source code|This specific codebase's current state; how other codebases implemented similar features is non-local
E5|Continuing to type mid-sentence|Current sentence context, intended meaning right now; statistical word frequencies don't determine correct next word for this specific sentence
E6|Choosing software for a project|This project's specific requirements, constraints, team; general software reviews are non-local to this project's unique state
E7|Basketball shot angle and force|This specific moment's body position, distance, wind, fatigue; average shooting statistics don't determine correct force for this shot

# related_concepts(id|concept|relationship_to_axiom)
RC1|"The Map Is Not The Territory" (Korzybski)|Maps (non-local abstractions) are not the territory (local reality); overlapping but axiom specifies when map is invalid (UIS + AC)
RC2|Ecological Fallacy (statistics)|Applying population-level statistics to individual; axiom formalizes when this is invalid (when accuracy is critical for unique set)

# claims(id|claim|type|depends_on)
CL1|For unique set of information where accuracy is critical, all non-local data is invalid|axiom|C1,C2,C3
CL2|This is a gap in collective understanding; obvious from common sense but lost when switching to intellectual/statistical mechanisms|observation|CL1
CL3|Intellectual tools lack mechanism for separating local-data-only problems from problems where non-local data is valid|observation|CL2
CL4|Statistics take into account acceptable error; when error is not acceptable, statistics are invalid for the specific decision|derivation|C2,C4
CL5|Non-local data is not invalidated for all uses — only for accuracy-critical decisions about unique sets|boundary|CL1
CL6|Statistics valid for: large-enough populations, non-accuracy-critical decisions, or when only small amounts of local data collected|boundary|CL4,CL5
CL7|People routinely ignore local data in favor of non-local data for local-data-only problems, causing real problems daily|observation|CL1
CL8|Most correctly named "Boundary Constraint" rather than Axiom or Law|observation|CL1

# rules(id|rule|rationale)
R1|When population is one and accuracy is critical, use only local data|Non-local data cannot describe exact state of single unit's single instance
R2|Problem framing determines what counts as local|Changing how you look at problem changes information set boundary; must be explicit about what UIS contains
R3|Non-local data valid when accuracy is not critical or population is large enough|Axiom does not invalidate statistics generally; only for UIS + AC conditions
R4|Maximum local data for physical objects is at "now" moment|Can actually look for data and follow to related data; historical moments have less available local data

# relationships(from|rel|to)
C1|condition_for|CL1
C2|condition_for|CL1
C1|combined_with|C2
CL1|produces|C3
C4|invalidated_by|CL1
C5|required_by|CL1
C6|determines|C5
C6|determines|C4
C7|constrains|C5
C8|grounds|CL1
RC1|overlaps_with|CL1
RC2|overlaps_with|CL1
CL4|derives_from|C2
CL5|bounds|CL1
CL6|bounds|CL4
R1|implements|CL1
R2|implements|C6
R3|implements|CL5

# section_index(section|title|ids)
Axiom|The Axiom|CL1
Definitions|Definitions|C1,C2,C3,C4,C5,C6,C7,C8
Formula|Formula|CL1
Examples|Examples|E1,E2,E3,E4,E5,E6,E7
Related|Related Concepts|RC1,RC2
Background|Background|CL2,CL3,CL7,CL8,CL5,CL6

# decode_legend
variables: UIS (Unique Information Set) | AC (Accuracy-Critical) | LDO (Local-Data-Only)
formula: Given UIS, if AC then LDO
category_values: core|condition|property|boundary
claim_types: axiom|derivation|observation|boundary
rel_types: condition_for|combined_with|produces|invalidated_by|required_by|determines|constrains|grounds|overlaps_with|derives_from|bounds|implements
locality_boundary: determined by problem framing; physical objects maximal at "now"; non-physical data self-contained
naming: author prefers "Boundary Constraint" as most correct; "Local-Data-Only problem" as working label
+standalone: this doc self-contained
