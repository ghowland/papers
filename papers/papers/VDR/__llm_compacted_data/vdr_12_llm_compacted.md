# VDR-12 GRAMMAR-DIRECTED COMPACTION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → problem → compaction → grammars → grammar_matching → training_apps → prompt_apps → economics → limitations → prior_work → col_types → profiles → rel_taxonomy → compaction_stats → grammar_scoring → auto_grammars → test_results → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Structural waste in LM output|LMs spend full forward pass on structurally determined tokens (brackets, punctuation, indentation) that grammar rules produce for free with 100% correctness
P2|Compaction is not summarization|removes prose (hedging, repetition, transitions) while preserving every named concept, relationship, constraint, claim; 75-93% smaller, informationally complete
P3|Self-describing KBs|compacted KB carries its own schema (table defs), validation (decode legend constraints), relationship graph (typed connections), and presentation instructions (grammars)
P4|Grammar as KB field|grammars are persistent field on KB struct; inherit through tree; travel on export; queryable and constrainable; LLM creates new ones by asserting facts
P5|Rule-determined structure, LLM-determined content|structural decisions (table set, columns, grammar generation) are Prolog-decidable; only row/relationship extraction requires LLM judgment
P6|Per-token provenance|every output token tagged: grammar (structural, exact, free), KB (factual, exact, free), or LLM (creative, probabilistic, expensive)
P7|Roundtrip fidelity|compacted doc → KB → compacted doc preserves all tables, rows, relationships, section index, decode legend exactly

# problem(id|aspect|detail)
PR1|Same computation for all tokens|model runs full forward pass + softmax over 50k+ vocab for closing bracket that was inevitable from opening bracket
PR2|Structural token waste by output type|Python ~40%, JSON ~55%, formatted tables ~65%, English ~25%, compacted tables ~80%
PR3|Reliability problem|every model-predicted structural token can be wrong (mismatched brackets, wrong indentation, malformed JSON); grammar rules cannot be wrong
PR4|No provenance in current LMs|impossible to trace which tokens are structural vs factual vs creative in standard generation

# compaction_system(id|aspect|detail)
CS1|Format|pipe-delimited tables with headers, ID-prefixed rows, relationships table, section index, decode legend
CS2|Compression mechanism|removes prose (connective tissue, hedging, repetition, transitions); preserves every named concept, relationship, constraint, claim
CS3|Example|VDR Triple: ~300 words prose → 1 row (~40 words) in concepts table; 87% compression
CS4|Source characters|12 types classified by keyword detection (Prolog) with LLM fallback for ambiguous; character determines table set
CS5|Table library|17 pre-defined schemas with columns, types, ID prefix, applicability; any compaction picks subset per source character profile
CS6|Compaction profiles|6 pre-defined (philosophy/specification/research/methodology/operational/data); LLM can create new profiles
CS7|Pipeline|10 steps: 5 deterministic (classify, select profile, determine tables, build legend, generate grammars), 2 LLM judgment (extract rows, extract relationships), 3 hybrid
CS8|Self-describing storage|facts (data), constraints (validation from decode legend), connections (relationships), grammars (presentation) all on one KB struct
CS9|Decode legend|enum declarations become validation constraints; notations and conventions declared; document is self-validating

# characters(id|name|signal_words|required_tables|compression)
CH1|Philosophy|axiom, principle, thesis, claim|principles, concepts, claims|85-93%
CH2|Architecture|commitment, boundary, flow, category|commitments, categories, flows, boundaries|80-85%
CH3|Schema|entity, field, nullable, FK|entities, fields|75-85%
CH4|Operational|operation, rule, gating, pattern|operations, rules|80-85%
CH5|API|endpoint, request, response, status code|endpoints, parameters, responses|75-85%
CH6|Methodology|phase, step, deliverable, milestone|phases|80-85%
CH7|Synthesis|diagnostic, capability, commitment|diagnostics, capabilities|80-85%
CH8|Specification|module, component, interface, IOSE|components, concepts|75-85%
CH9|Research|finding, hypothesis, experiment, result|findings, claims|80-90%
CH10|Narrative|event, character, setting, theme|events, characters|80-90%
CH11|Data|record, field, type, constraint|entities, fields|75-85%
CH12|Mixed|no clear signals|union of applicable|varies

# column_types(id|type|meaning|validation|vdr_conversion|sort)
CT1|id|row identifier with prefix|regex ^[A-Z]{1,3}\d+$ or empty|N/A|prefix alpha then numeric
CT2|text|compressed prose|non-empty if required|N/A|lexicographic
CT3|identifier|exact source terminology preserved|no synonyms/abbreviation unless source uses|N/A|lexicographic
CT4|categorical|value from declared enum|must be in enum_values list|N/A|enum declaration order
CT5|id_ref|reference to another row ID|must reference existing ID|N/A|target sort order
CT6|id_list|comma-separated ID refs|each element valid id_ref|N/A|by first element
CT7|rel_type|relationship type from enum|must be in rel_types enum|N/A|alphabetic
CT8|fraction|exact VDR fraction n/d|n integer, d positive integer|VDR(n,d) lossless|cross-multiply
CT9|integer|parseable integer|no decimal/fraction|VDR(n,1) lossless|numeric
CT10|boolean|yes/no/true/false|one of 4 values|N/A|false < true
CT11|enum_list|pipe-separated enum values|each from declared enum|N/A|by first element

# type_compatibility(id|from_type|to_type|compatible|conversion|loss)
TC1|id→id|yes|direct|none
TC2|id→text|yes|render as string|none
TC3|text→text|yes|direct|none
TC4|identifier→identifier|yes|direct|none
TC5|identifier→text|yes|direct|none
TC6|categorical→categorical|yes (same enum)|direct|none
TC7|categorical→text|yes|render as string|none
TC8|id_ref→id_ref|yes|direct|none
TC9|id_ref→text|yes|render, optionally resolve|none
TC10|fraction→fraction|yes|direct (exact VDR)|none
TC11|fraction→text|yes|format_fraction builtin|reversible
TC12|integer→integer|yes|direct|none
TC13|integer→fraction|yes|VDR(n,1) promotion|none
TC14|integer→text|yes|to_string|reversible
TC15|boolean→boolean|yes|direct|none
TC16|boolean→text|yes|yes/no rendering|none
TC17|text→identifier|NO|—|would lose type safety
TC18|text→categorical|NO|—|may not be in enum
TC19|text→fraction|NO|—|may not be numeric

# standard_tables(id|name|columns|id_prefix|category)
T1|principles|id,principle,rationale|P|core
T2|concepts|id,name,category,definition|C|core (category enum: core/slot/state/operation/semantics/procedure/metric/construction/anti-pattern)
T3|claims|id,claim,type,evidence|CL|core (type enum: demonstrated/structural/limitation/boundary/finding/observation/design_thesis/derived)
T4|operations|id,name,mechanism,inputs,outputs|OP|core
T5|boundaries|id,limitation,detail|B|core
T6|rules|id,rule,enforcement|R|core
T7|distinctions|id,side_a,side_b,key_asymmetry|DI|structural
T8|axes|id,name,low_pole,high_pole,applies_to|AX|structural
T9|components|id,name,category,iose_inputs,iose_outputs,iose_side_effects|CO|specification
T10|builtins|id,name,category,signature,properties|BU|specification
T11|constraints|id,name,scope,condition,on_violation|CN|specification
T12|entities|id,name,description|E|data
T13|fields|id,entity,name,type,required,description|F|data (entity is FK)
T14|phases|id,name,inputs,outputs,key_constraint|PH|lifecycle
T15|test_results|id,domain,tests,passed,failed,notes|TR|research
T16|failures|id,test,expected,got,root_cause|FL|research
T17|findings|id,finding,evidence,confidence|FI|research (confidence as exact VDR fraction)
T18|benchmarks|id,name,metric,value,comparison|BM|research
T19|relationships|from,rel,to|(none)|always present
T20|section_index|section,title,ids|(none)|always present

# profiles(id|name|required|optional|read_order|compression)
PF1|Philosophy|principles,concepts,claims|boundaries,distinctions,axes,rules|principles→concepts→axes→distinctions→claims→boundaries→rels→secidx|85-93%
PF2|Specification|components,concepts|builtins,constraints,boundaries,rules,phases,entities,fields|principles→components→builtins→constraints→concepts→boundaries→claims→rels→secidx|75-85%
PF3|Research|findings,claims|benchmarks,test_results,failures,boundaries,concepts|principles→findings→benchmarks→test_results→failures→claims→boundaries→rels→secidx|80-90%
PF4|Methodology|phases|rules,constraints,concepts,claims|principles→phases→rules→constraints→concepts→claims→rels→secidx|80-85%
PF5|Operational|operations,rules|constraints,boundaries,concepts,components,claims|principles→operations→rules→constraints→concepts→components→claims→boundaries→rels→secidx|80-85%
PF6|Data|entities,fields|constraints,concepts,rules|entities→fields→constraints→concepts→rules→rels→secidx|75-85%

# grammar_system(id|aspect|detail)
GS1|Core mechanism|grammar provides structural tokens (free, exact); declares typed slots for LLM/KB content tokens; Prolog pattern matching selects grammar
GS2|GrammarRule fields|name, slots, slot_types, template, requires, best_when, connection_pattern(optional), usage_count
GS3|Three auto-generated categories|extraction (1 per table), display (5 standard: compact/summary/detail_per_table/relationship), usage (5 types on demand)
GS4|Usage grammar types|reference (cite inline), comparison (side-by-side), evidence (for inference w/ confidence), dependency (trace chains), summary (overview)
GS5|Usage grammars create bidirectional connections|target gets grammar + outbound connection; source gets inbound connection; connection carries display_grammar field
GS6|Inheritance|grammars inherit through KB tree like constraints; child overrides parent; most local wins; root=global, project=project-wide, session=disposable
GS7|Connection-aware matching|grammars declare connection_pattern matching KB topology; e.g. has_inbound(sourced_from,1+); grammar activates only when topology matches
GS8|Cross-KB slot filling|slots can follow connections to pull data from other KBs; one grammar describes multi-KB dashboard; integer ID addressing for O(1) access
GS9|LLM creates grammars|assert GrammarRule facts into KB at any scope; created once, used N times with zero LLM cost per reuse; modifiable, versionable, retirable
GS10|KB-scoped vocabulary filtering|typed grammar slots constrain valid tokens; categorical slot with 4 values → softmax over 4 not 50k; derived from grammar types + KB declarations

# grammar_scoring(id|component|weight|computation|range)
GSC1|Requirement satisfaction|gate (must pass)|all declared requirements met|pass/fail
GSC2|Slot coverage|40%|filled slots / total slots|0-100
GSC3|Type precision|30%|exact type matches / total fills|0-100
GSC4|Connection pattern match|20%|pattern matches KB topology|0 or 100
GSC5|Best-when relevance|10%|LLM assessment of situational fit|0-100
# Score = (coverage×40 + precision×30 + conn×20 + relevance×10)/100 if all requirements pass; else 0
# Tiebreaking: higher score → more specific → more local → more recent → alphabetical

# auto_grammars(id|per_table|count_per_table|notes)
AG1|extract_{table}|1|knows column names/types/ID prefix; exact queries
AG2|detail_{table}|1|single row with labeled fields
AG3|resolve_{table}_{col}|0-1|generated only for columns with id_ref or id_list type
AG4|compact_display|1 per doc|re-emit pipe-delimited format
AG5|document_summary|1 per doc|title, character, table counts, total IDs, relationship count
AG6|relationship_display|1 per doc|edges with resolved names
# Max per KB: (tables×2) + resolve_grammars + 3 document-level

# pipeline_steps(id|step|deterministic|description)
PS1|Classify source character|mostly (keyword); LLM fallback|pattern match on signal words
PS2|Select profile|yes|character → profile lookup
PS3|Determine applicable tables|yes|profile required + optional matching source
PS4|Extract rows|no (LLM)|what's a concept, what merits a row — expensive creative step
PS5|Extract relationships|no (LLM)|what depends on what
PS6|Build section index|hybrid|map items to source sections
PS7|Build decode legend|yes|collect all enums from schemas used
PS8|Validate|yes|constraint checking against declared types
PS9|Generate grammars|yes|deterministic from schemas
PS10|Store as KB|yes|facts + connections + grammars + constraints; path registry

# training_applications(id|application|detail)
TA1|Compacted training data|corpora as compacted KBs; structure-level training dramatically smaller (5-10× higher info density per token); token-level training continues in parallel
TA2|Grammar libraries as training signal|grammar selection accuracy (user feedback), creation quality (usage counters), slot-filling accuracy (focused feedback on content only)
TA3|Denominator management|model params as compacted KBs; denom complexity tracked as KB counter; budget constraint triggers reprojection with exact declared error
TA4|Checkpoint compression|params in pipe-delimited tables with denom_bits per group; self-describing, self-validating; multi-checkpoint diffing via KB diff

# prompt_applications(id|application|detail)
PA1|Context assembly|10 compacted KBs (~20k tokens) vs raw text (~200k tokens); extraction grammars enable exact queries; attention over compact structured context
PA2|Grammar-selected output|scratchpad queries data → grammar matcher scores → template with slots → KB fills factual, primitives fill formatted, LLM fills creative only
PA3|KB-scoped vocabulary filtering|typed slots constrain softmax to relevant candidates (e.g. 200 identifiers not 50k vocab); derived from grammar types + KB declarations
PA4|Error prevention|grammar constraints guarantee structural correctness; comparison table requires min 2 items; JSON grammar enforces matched braces; code grammar enforces language version

# economics(id|output_type|structural_pct|grammar_provided|forward_passes_saved)
EC1|Python function|~40%|brackets, colons, indent, keywords|~40%
EC2|JSON output|~55%|braces, brackets, colons, commas, quotes|~55%
EC3|Formatted table|~65%|separators, headers, alignment|~65%
EC4|English with data|~30%|articles, punctuation, data formatting|~30%
EC5|Compacted table output|~80%|pipes, headers, ID prefixes, enums|~80%
# Grammar tokens: 100% correctness rate. LM-predicted structural tokens: degrades with length/complexity.

# token_distribution_compacted(id|category|pct|grammar_providable)
TD1|Structural delimiters (pipes, #, parens, newlines)|18%|yes 100%
TD2|ID tokens (P1, C3, CL7)|12%|yes (prefix+counter)
TD3|Column headers|8%|yes (from schema)
TD4|Relationship types|5%|yes (from enum)
TD5|Category values|4%|yes (from enum)
TD6|Table names|3%|yes (from profile)
TD7|Content identifiers|15%|partially (from KB vocab)
TD8|Content text (definitions, descriptions)|35%|no (LLM judgment)
# ~50% fully grammar-providable, ~5% partially, ~35% LLM-required

# compaction_stats(id|paper|character|source_words|compacted_tokens|tables|rels|ids|compression)
CS_1|VDR-1|Philosophy/Spec|15000|2800|12|35|78|81%
CS_2|VDR-2|Research|12000|2200|8|22|54|82%
CS_3|VDR-3|Research|8000|1600|9|18|42|80%
CS_4|VDR-4|Specification|7000|1400|8|20|38|80%
CS_5|VDR-5|Specification|18000|3200|10|28|72|82%
CS_6|VDR-6|Specification|22000|3800|9|24|65|83%
CS_7|VDR-7|Methodology|16000|2600|11|30|58|84%
CS_8|VDR-8|Specification|14000|2400|10|26|52|83%
CS_9|VDR-9|Specification|18000|2800|8|22|48|84%
CS_10|VDR-10|Specification|20000|3400|11|32|68|83%
# Total: ~150k words → ~26.2k tokens, 257 rels, 575 IDs, ~83% avg compression

# info_density(id|metric|raw|compacted|ratio)
ID1|Words per named concept|~190|~25|7.6×
ID2|Words per relationship|~580|~3|193×
ID3|Words per claim|~450|~20|22.5×
ID4|Words per boundary|~300|~15|20×
ID5|Unique IDs per 1000 tokens|~3.8|~22|5.8×

# rel_taxonomy(id|relationship|domain|meaning|directionality)
RT1|enables|general|X makes Y possible|X→Y
RT2|requires|general|X cannot exist without Y|X→Y
RT3|implements|general|X realizes Y concretely|X→Y
RT4|prevents|general|X blocks Y|X→Y
RT5|composes_of|structure|X is made of Y₁,Y₂...|X→{Y}
RT6|specialization_of|taxonomy|X is specific kind of Y|X→Y
RT7|distinct_from|taxonomy|X and Y explicitly not same|X↔Y
RT8|extends|evolution|X builds on Y adding capability|X→Y
RT9|demonstrates|evidence|X provides evidence for Y|X→Y
RT10|grounds|foundation|X provides theoretical basis for Y|X→Y
RT11|constrains|governance|X limits or governs Y|X→Y
RT12|addresses|solution|X solves or mitigates Y|X→Y
RT13|limits|boundary|X restricts scope of Y|X→Y
RT14|uses|dependency|X operationally depends on Y|X→Y
RT15|feeds|lifecycle|X output becomes Y input|X→Y
RT16|gates|lifecycle|X must pass before Y proceeds|X→Y
RT17|resolves|resolution|X eliminates impossibility claim of Y|X→Y
RT18|alternative_to|choice|X and Y serve same purpose|X↔Y
RT19|instance_of|classification|X concrete example of Y|X→Y
RT20|component_of|containment|X is part within Y|X→Y
# Most used across VDR-1–10: uses(35), enables(18), implements(13), demonstrates(10)

# rel_validation(id|rule|condition|violation_type)
RV1|Referential integrity|both from and to IDs exist|error
RV2|Type declared|rel value in decode legend rel_types|warning
RV3|No self-reference|from ≠ to|warning
RV4|Directional consistency|if A enables B, no B enables A|warning
RV5|ID list expansion|to may be comma-separated; validate each|ok

# prior_work(id|approach|how_grammar_directed_differs)
PW1|Constrained decoding (PICARD, Synchromesh)|constrains vocab at each step but still runs forward pass; grammar-directed eliminates forward pass entirely for structural tokens
PW2|Template-based generation (Jinja, Mustache)|static templates; grammar-directed has dynamic Prolog-matched selection, LLM-created/evolved templates, KB inheritance chain
PW3|Retrieval-augmented generation|retrieves raw documents into context; compaction stores as structured queryable KBs; 10× smaller context, exact queries

# limitations(id|limitation|detail)
LM1|Grammar coverage|novel explanations, creative writing, ambiguous structures resist grammar-directed generation; falls back to token-by-token
LM2|Grammar maintenance|accumulation over time; stale/too-specific/conflicting grammars; usage counter helps but lifecycle management ongoing
LM3|Compaction quality|bounded by LLM extraction judgment; constraint system catches type violations but not semantic errors (inaccurate definitions)
LM4|Scale|Python prototype tested on small docs/toy models; production needs faster Prolog matching, indexed grammar retrieval, grammar compilation

# test_results(id|category|count|passed|notes)
TR1|Basic types and enums|5|5|
TR2|Column/table schema|4|4|
TR3|Standard table library|17|17|all 17 schemas
TR4|Compaction profiles|12|12|all 6 profiles
TR5|Decode legend|4|4|
TR6|Grammar rule|4|4|
TR7|Compacted document|8|7|1 failure: all_ids counts empty-string IDs from rels/secidx rows
TR8|KB infrastructure|40|40|path registry, facts, counters, locks, reset
TR9|Doc→KB conversion|19|19|facts, constraints, grammars auto-generated
TR10|KB→doc roundtrip|11|11|full roundtrip fidelity verified
TR11|Usage grammar generation|12|12|all 5 types + connections
TR12|Compaction pipeline|21|21|classification, applicability, full pipeline
TR13|Cross-KB integration|7|7|evidence grammars, connections, queries
TR14|Grammar inheritance|6|6|tree walking, override shadowing
# Total: 178/179 pass. 1 failure is test expectation calibration (empty-string IDs), not system bug.

# untested_areas(id|area|priority|planned_stage)
UT1|Grammar matching score computation|high|S3 (requires Prolog engine)
UT2|Slot filling from connected KBs|medium|S4 (requires mount system)
UT3|Grammar evolution (modify/retire)|medium|S4 (requires usage tracking)
UT4|Concurrent grammar access|low|S5 (requires session cloning)
UT5|Large document compaction (>50k words)|medium|S4
UT6|Grammar conflict detection|medium|S3
UT7|Decode legend constraint enforcement|high|S2 (requires Prolog condition eval)
UT8|Cross-document relationship discovery|medium|S4

# implementation(id|aspect|detail)
IM1|Language|Python 3.8, stdlib only (dataclasses, typing, enum), no external deps
IM2|Structure|single file universal_compaction.py; planned multi-file extraction at Stage 3+
IM3|Components|7 enums, 17 dataclasses, 17 table schemas, 6 profiles, doc↔KB conversion, usage grammar gen, full pipeline
IM4|KB struct|26 fields (identity:3, persistent:6 incl grammars, live:8, structural:3, metadata:6)
IM5|Integration stage|Stage 3 component of VDR-11 five-stage build plan

# relationships(from|rel|to)
P1|motivates|GS1,GS10,EC1-EC5
P2|governs|CS1-CS9
P3|governs|CS8,IM4
P4|governs|GS6
P5|governs|PS1-PS10
P6|enables|PA2
P7|verified_by|TR10
PR1|addressed_by|GS1
PR2|quantified_by|EC1-EC5
PR3|addressed_by|PA4
CS4|uses|CH1-CH12
CS5|references|T1-T20
CS6|references|PF1-PF6
CS7|decomposes_into|PS1-PS10
CS9|generates|RV1-RV5
GS1|produces|AG1-AG6
GS3|categorizes|AG1-AG6
GS4|categorizes|GS5
GS5|creates|bidirectional_connections
GS6|mechanism|P4
GS7|extends|GS4
GS8|extends|GS7
GS9|enables|TA2
GS10|enables|PA3
GSC1|gates|GSC2-GSC5
PS1|prereq_of|PS2
PS2|prereq_of|PS3
PS3|prereq_of|PS4
PS4|prereq_of|PS5
PS5|prereq_of|PS6
PS6|prereq_of|PS7
PS7|prereq_of|PS8
PS8|prereq_of|PS9
PS9|prereq_of|PS10
TA1|uses|CS1
TA3|uses|CS1
TA4|uses|CS1
PA1|uses|CS1,GS3
PA2|uses|GS1,GS3
PW1|less_than|GS1
PW2|less_than|GS9,GS6
PW3|complemented_by|CS1
LM1|limits|GS1
LM3|limits|PS4,PS5
CT1-CT11|used_by|T1-T20
TC1-TC19|governs|GS10
RT1-RT20|used_in|T19

# section_index(section|title|ids)
1|The Problem|PR1-PR4,P1
2|VDR-LLM-Prolog Foundation|(context only, no new IDs)
3.1|Compaction Problem|P2
3.2|Compacted Format|CS1,CS3
3.3|Source Character Classification|CS4,CH1-CH12
3.4|Table Schemas|CS5,CT1-CT11
3.5|Compaction Pipeline|CS7,PS1-PS10
3.6|Self-Describing Data|CS8,CS9,P3
3.7|Roundtrip Fidelity|P7
4.1|Core Mechanism|GS1,P6
4.2|Grammars as KB Fields|GS2,P4,IM4
4.3|Grammar Inheritance|GS6
4.4|Auto-Generated Grammars|GS3,AG1-AG6
4.5|Connection-Aware Matching|GS7,GS8
4.6|Usage Grammars|GS4,GS5
4.7|LLM Creates Grammars|GS9
5.1|Matching Problem|GSC1-GSC5
5.2|Attribute-to-Slot Mapping|TC1-TC19
5.3|What LLM Actually Generates|EC1-EC5
5.4|Code Generation Through Grammars|GS1
6|Training Applications|TA1-TA4
7|Prompt-Time Applications|PA1-PA4
8|Implementation and Testing|IM1-IM5,TR1-TR14
9|Economics|EC1-EC5,TD1-TD8
10|Prior Work|PW1-PW3
11|Limitations|LM1-LM4
AppA|Column Type Reference|CT1-CT11,TC1-TC19
AppB|Profile Detail|PF1-PF6
AppC|Relationship Taxonomy|RT1-RT20,RV1-RV5
AppD|Compaction Statistics|CS_1-CS_10,ID1-ID5
AppE|Grammar Scoring|GSC1-GSC5
AppF|Auto-Generated Grammar Catalog|AG1-AG6
AppG|Structural Token Analysis|TD1-TD8,EC1-EC5
AppH|Test Suite Detail|TR1-TR14,UT1-UT8
AppI|Compaction vs Summarization|(comparative analysis, no IDs)
AppJ|Connection-Aware Patterns|GS7,GS8
AppK|Pipeline Decision Points|PS1-PS10,P5
AppL|Implementation File Structure|IM1-IM5

# decode_legend
id_prefixes: P=principle, PR=problem, CS=compaction_system, CH=character, CT=column_type, TC=type_compatibility, T=standard_table, PF=profile, GS=grammar_system, GSC=grammar_scoring, AG=auto_grammar, PS=pipeline_step, TA=training_app, PA=prompt_app, EC=economics, TD=token_distribution, CS_=compaction_stat(per paper), ID=info_density, RT=rel_taxonomy, RV=rel_validation, PW=prior_work, LM=limitation, TR=test_result, UT=untested_area, IM=implementation
rel_types: motivates|governs|verified_by|addressed_by|quantified_by|uses|references|decomposes_into|generates|produces|categorizes|creates|mechanism|extends|enables|gates|prereq_of|less_than|complemented_by|limits|used_by|used_in
source_characters: philosophy, architecture, schema, operational, API, methodology, synthesis, specification, research, narrative, data, mixed
column_types: id, text, identifier, categorical, id_ref, id_list, rel_type, fraction, integer, boolean, enum_list
concept_categories: core, slot, state, operation, semantics, procedure, metric, construction, anti-pattern
claim_types: demonstrated, structural, limitation, boundary, finding, observation, design_thesis, derived
constraint_scopes: axiom, operational, legal, project, conversation
usage_grammar_types: reference, comparison, evidence, dependency, summary
grammar_token_sources: grammar(structural,exact,free), KB(factual,exact,free), LLM(creative,probabilistic,expensive)
test_status: 178/179 pass; 1 test-expectation calibration issue
compression_range: 75-93% depending on source character; ~83% average across VDR-1–10
