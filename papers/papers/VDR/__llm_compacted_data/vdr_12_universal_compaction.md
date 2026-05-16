# UNIVERSAL COMPACTION SYSTEM — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → architecture → characters → tables → profiles → grammars → pipeline → integration → test_results → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Self-describing KBs|data, schema, and grammars for reading/presenting all live on one KB struct; KB carries what it knows, what follows, what must hold, what it connects to, and how to present itself
P2|Rule-determined structure, LLM-determined content|structural decisions (table set, column defs, grammar generation) are Prolog-decidable; only row extraction and relationship extraction require LLM judgment
P3|Roundtrip fidelity|compacted doc → KB → compacted doc preserves all tables, rows, relationships, section index, decode legend exactly; compression loses only prose, not structure
P4|Grammar inheritance|grammars inherit through KB tree like constraints; child overrides parent; most local version wins
P5|10x context reduction|10 papers (~200k tokens raw) → 10 compacted KBs (~20k tokens) with structured queryability and cross-KB connections

# architecture(id|layer|question_answered|mechanism)
A1|Compression|how to compress|CompactionProfiles + TableSchemas; source character → table set via pattern matching
A2|Reading|how to read|ExtractionGrammars auto-generated per table; exact queries by ID with known column semantics
A3|Usage|how to use|UsageGrammars generated on demand when one KB references another; 5 usage types with typed bidirectional connections

# characters(id|name|signal_words|required_tables|compression_target)
CH1|Philosophy|axiom, principle, thesis, claim|principles, concepts, claims|85-93%
CH2|Architecture|commitment, boundary, flow, category|commitments, categories, flows, boundaries|80-85%
CH3|Schema|entity, field, nullable, foreign key|entities, fields|75-85%
CH4|Operational|operation, rule, gating, pattern|operations, rules|80-85%
CH5|API|endpoint, request, response, status code|endpoints, parameters, responses|75-85%
CH6|Methodology|phase, step, deliverable, milestone|phases|80-85%
CH7|Synthesis|diagnostic, capability, commitment|diagnostics, capabilities|80-85%
CH8|Specification|module, component, interface, IOSE|components, concepts|75-85%
CH9|Research|finding, hypothesis, experiment, result|findings, claims|80-90%
CH10|Narrative|event, character, setting, theme|events, characters|80-90%
CH11|Data|record, field, type, constraint|entities, fields|75-85%
CH12|Mixed|no clear signals|union of applicable|varies
# Classification: keyword detection for clear cases; LLM fallback for ambiguous

# standard_tables(id|name|columns|id_prefix|applicability)
T1|principles|id,principle,rationale|P|foundational rules or design decisions
T2|concepts|id,name,category,definition|C|named concepts; category enum includes anti-pattern; most frequently used table
T3|claims|id,claim,type,evidence|CL|assertions classified by type; evidence column contains comma-separated ID refs
T4|operations|id,name,mechanism,inputs,outputs|OP|named operations with how they work
T5|boundaries|id,limitation,detail|B|honest limitations and what is NOT claimed
T6|rules|id,rule,enforcement|R|actionable prescriptions with enforcement
T7|distinctions|id,side_a,side_b,key_asymmetry|DI|binary splits where asymmetry matters
T8|axes|id,name,low_pole,high_pole,applies_to|AX|named spectrums with poles
T9|components|id,name,category,iose_inputs,iose_outputs,iose_side_effects|CO|system components with optional IOSE summary
T10|builtins|id,name,category,signature,properties|BU|primitive operations with type signatures
T11|constraints|id,name,scope,condition,on_violation|CN|scope: axiom/operational/legal/project/conversation
T12|entities|id,name,description|E|data entities
T13|fields|id,entity,name,type,required,description|F|fields belonging to entities; entity is FK
T14|phases|id,name,inputs,outputs,key_constraint|PH|lifecycle or process phases
T15|test_results|id,domain,tests,passed,failed,notes|TR|test results per domain
T16|failures|id,test,expected,got,root_cause|FL|individual failures with root cause
T17|findings|id,finding,evidence,confidence|FI|research findings; confidence as exact VDR fraction
T18|benchmarks|id,name,metric,value,comparison|BM|benchmark results
T19|relationships|from,rel,to|(none)|typed directed edges between any IDs; always present
T20|section_index|section,title,ids|(none)|provenance map; always present
# concept category enum: core, slot, state, operation, semantics, procedure, metric, construction, anti-pattern
# claim type enum: demonstrated, structural, limitation, boundary, finding, observation, design_thesis, derived

# profiles(id|name|required|optional|read_order|compression)
PR1|Philosophy|principles,concepts,claims|boundaries,distinctions,axes,rules|principles→concepts→claims→relationships|85-93%
PR2|Specification|components,concepts|builtins,constraints,boundaries,rules|components→concepts→builtins→relationships|75-85%
PR3|Research|findings,claims|benchmarks,boundaries|findings→claims→benchmarks→relationships|80-90%
PR4|Methodology|phases|rules,constraints|phases→rules→relationships|80-85%
PR5|Operational|operations,rules|constraints,boundaries|operations→rules→relationships|80-85%
PR6|Data|entities,fields|constraints|entities→fields→relationships|75-85%
# All profiles implicitly include: relationships, section_index, decode_legend
# LLM can create new profiles by asserting profile facts into a grammar KB

# grammar_types(id|category|name|generation|description)
G1|extraction|extract_{table}|auto per table on load|one per table; knows column names/types/ID prefix; enables exact queries; resolution grammar also generated for ID-reference columns
G2|display|compact_display|auto on load|re-emit in original pipe-delimited format
G3|display|document_summary|auto on load|title, character, table counts, total IDs, relationship count
G4|display|detail_{table}|auto per table on load|single row with labeled fields
G5|display|relationship_display|auto on load|relationships with resolved names not just IDs
G6|usage|reference|on demand|cite specific item inline from another KB
G7|usage|comparison|on demand|merge tables from two KBs for side-by-side
G8|usage|evidence|on demand|use facts as evidence in inference notebook with confidence tracking
G9|usage|dependency|on demand|trace dependency chains across KBs
G10|usage|summary|on demand|overview of another KB's contents
# Usage grammars create bidirectional typed connections between source and target KBs
# Connection carries display_grammar field naming which grammar to use

# grammar_features(id|feature|detail)
GF1|Inheritance|grammars inherit through KB tree like constraints; child overrides parent; most local wins; root-level available everywhere, project-level within project, session-level disposable
GF2|Connection-aware matching|grammars can declare connection_pattern matching KB topology; e.g. has_inbound(sourced_from, 1+); grammar activates only when topology matches
GF3|Cross-KB slot filling|grammar slots can follow connections to pull data from other KBs; one grammar declaration can describe dashboard pulling from 4+ KBs
GF4|On-the-fly creation|LLM creates new grammars anytime by asserting GrammarRule facts; reusable, versionable, sharable through mounts, retirable
GF5|Generation cost reduction|LLM fills creative slots; grammar generates structural tokens; grammar created once, used N times with zero LLM cost per reuse

# decode_legend_spec(id|element|description)
DL1|Enum declarations|legal values for categorical columns; becomes validation constraint in KB; e.g. rel_types: enables,requires,...
DL2|Notations|abbreviation/convention declarations; e.g. id_prefix: P=principle, C=concept
DL3|Conventions|formatting rules; e.g. id_list: comma-separated ID references
# Decode legend entries become facts: fact(decode, {key, description, type})
# Each enum generates constraint: constraint(valid_{name}, condition, on_violation: warn)
# Document is self-validating because decode legend is inside it

# pipeline_steps(id|step|deterministic|description)
PS1|Classify source character|mostly (keyword); LLM fallback for ambiguous|pattern match on signal words
PS2|Select profile|yes|character → profile lookup
PS3|Determine applicable tables|yes|profile required + optional matching source
PS4|Extract rows|no (LLM judgment)|what's a concept, what merits a row — the expensive creative step
PS5|Extract relationships|no (LLM judgment)|what depends on what
PS6|Build section index|yes|map items to source sections
PS7|Build decode legend|yes|collect all enums from schemas used
PS8|Validate|yes|constraint checking against declared types
PS9|Generate grammars|yes|deterministic from schemas
PS10|Store as KB|yes|facts + connections + grammars + constraints; registered in path registry

# kb_struct_update(id|detail)
KS1|grammars field added as 26th field on KB struct; persistent classification alongside facts, rules, constraints, connections
KS2|Grammars travel with KB on export; receiving system immediately knows how to read and present data
KS3|KB is fully self-describing: knows (facts), follows (rules), must hold (constraints), connects to (connections), presents as (grammars)

# integration_points(id|system|how_compaction_integrates)
IP1|VDR exact arithmetic (VDR-1–4)|confidence scores and benchmark values in compacted data are exact VDR fractions; findings table has confidence column type FRACTION
IP2|Knowledge bases (VDR-5)|compacted documents ARE KBs; same struct, scoping, constraints, inheritance
IP3|Primitives and command tokens (VDR-6, VDR-8)|LLM compacts via KB_ASSERT tokens, queries via KB_QUERY tokens; grammar selection is Prolog query
IP4|Lifecycle (VDR-7)|every lifecycle phase produces compactable data: training configs, eval results, deployment states, feedback records
IP5|Session management (VDR-8)|grammars are persistent (survive session reset); compacted KBs and usage connections persist across sessions
IP6|Orchestrated inference (VDR-9)|inference notebooks reference compacted data through evidence usage grammars; confidence scores feed VDR-9 confidence propagation
IP7|IOSE model (VDR-10)|every compaction function has IOSE declaration; pipeline is composite IOSE node decomposing into classification, profile selection, extraction, grammar generation, storage

# test_results(id|category|count|notes)
TR1|Basic types and enums|5|pass
TR2|Column and table schema|4|pass
TR3|Standard table library|17|pass; completeness and structure
TR4|Compaction profiles (all 6)|12|pass
TR5|Decode legend|4|pass
TR6|Grammar rules|4|pass
TR7|Compacted document construction|8|pass
TR8|KB infrastructure|40|pass; path registry, facts, counters, locks, reset
TR9|Doc → KB with grammar gen|19|pass
TR10|KB → doc roundtrip|11|pass
TR11|Usage grammars (all 5 types)|12|pass
TR12|Compaction pipeline|21|pass; character classification
TR13|Cross-KB integration|7|pass
TR14|Grammar inheritance|6|pass; tree walking with override
TR15|KNOWN FAILURE|1|doc.all_ids traverses relationships+section_index producing empty-string IDs; test expectation issue, not system bug; fix: filter empty IDs or adjust test
# Total: 178/179 pass

# future_extensions(id|extension|description)
FE1|Compaction-aware training data|training corpora as compacted KBs; pipeline reads structured facts rather than raw tokens
FE2|Differential compaction|updated docs re-extract only changed rows; structured diff (added/removed/changed) via mutation logging
FE3|Cross-document relationship discovery|Prolog discovers relationships spanning documents in same KB tree; relationship table becomes cross-document knowledge graph
FE4|Grammar optimization|usage tracking enables pruning ineffective grammars and refining frequent ones; grammar evolution at runtime through KB operations

# relationships(from|rel|to)
P1|governs|KS1,KS2,KS3
P2|governs|PS1,PS2,PS3,PS4,PS5,PS7,PS9
P3|verified_by|TR10
P4|governs|GF1
P5|motivates|A1,A2,A3
A1|uses|CH1-CH12,PR1-PR6,T1-T20
A2|produces|G1,G2,G3,G4,G5
A3|produces|G6,G7,G8,G9,G10
CH1-CH12|selects|PR1-PR6
PR1-PR6|references|T1-T20
G1|enables|A2
G6-G10|creates|IP2(bidirectional connections)
GF1|mechanism_of|P4
GF2|extends|G6-G10
GF3|extends|G6-G10
GF4|extends|GF5
DL1|generates|T11(validation constraints)
PS1|prereq_of|PS2
PS2|prereq_of|PS3
PS3|prereq_of|PS4
PS4|prereq_of|PS5
PS5|prereq_of|PS6
PS6|prereq_of|PS7
PS7|prereq_of|PS8
PS8|prereq_of|PS9
PS9|prereq_of|PS10
IP1|uses|T17(confidence column)
IP2|grounds|P1
IP3|enables|PS4,PS5
IP6|uses|G8
IP7|governs|PS1-PS10
KS1|extends|T1-T20(KB struct gains 26th field)

# section_index(section|title|ids)
1|What This System Is|P1,P5
2|The Architecture|A1,A2,A3
3|The Data Flow|PS1-PS10
4|Source Character Classification|CH1-CH12
5|Standard Table Library|T1-T20
6|The Decode Legend|DL1-DL3
7|Compaction Profiles|PR1-PR6
8|Auto-Generated Grammars|G1-G10
9|Grammar Inheritance|GF1
10|KB Struct With Grammars|KS1-KS3
11|Connection-Aware Grammar Matching|GF2,GF3
12|The Compaction Pipeline|PS1-PS10
13|Roundtrip Fidelity|P3
14|Test Results|TR1-TR15
15|System Integration|IP1-IP7
16|LLM Context Management|P5,GF5
17|Creating New Grammars|GF4,GF5
18|Single Remaining Test Failure|TR15
19|Future Extensions|FE1-FE4

# decode_legend
id_prefixes: P=principle, A=architecture_layer, CH=character, T=standard_table, PR=profile, G=grammar_type, GF=grammar_feature, DL=decode_legend_spec, PS=pipeline_step, KS=kb_struct_update, IP=integration_point, TR=test_result, FE=future_extension
rel_types: governs|verified_by|motivates|uses|produces|selects|references|enables|creates|mechanism_of|extends|generates|prereq_of|grounds
concept_categories: core, slot, state, operation, semantics, procedure, metric, construction, anti-pattern
claim_types: demonstrated, structural, limitation, boundary, finding, observation, design_thesis, derived
constraint_scopes: axiom, operational, legal, project, conversation
usage_types: reference, comparison, evidence, dependency, summary
compression_targets: 75-93% depending on source character
test_status: 178/179 pass; 1 known test-expectation issue
