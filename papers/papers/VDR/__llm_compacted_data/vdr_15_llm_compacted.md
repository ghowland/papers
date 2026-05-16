# VDR-15 PROMPT OPTIMIZATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → token_categories → pipeline → token_accounting → crossover → scaling → capability_boundary → use_cases → accuracy → attention_reduction → grammar_economics → clone_economics → workday_economics → relationships → section_index → decode_legend

# principles(id|principle|detail)
P1|80-95% of conventional LM tokens are infrastructure|parsing, state reconstruction, arithmetic, deduction, formatting, hedging — all infrastructure served by primitives/KB/Prolog/grammar at zero LM tokens
P2|LM generates only judgment + prose tokens|judgment: intent recognition, step selection, formalization; prose: natural language for human consumption; command tokens: ~8 LM tokens per primitive invocation
P3|Per-op Q335 cost is structurally irrelevant|Q335 would need to be ~10,000× slower than float per op to break even on single turn; margin grows with conversation length (conventional quadratic, VDR linear)
P4|Conventional cost scales quadratically with conversation length|each turn re-reads all prior history through attention; VDR cost flat per turn (state in KB at integer addresses)
P5|Data volume capability boundary|conventional LM limited to context window; VDR processes arbitrary data volume through primitives (1MB JSON, 10MB documents, 500 positions, 2000 articles) — data never enters token stream
P6|Every token not generated cannot be wrong|structural elimination of error classes: arithmetic, state, formatting, retrieval, deduction, confidence — not statistical improvement but category elimination

# token_categories(id|category|description|conventional_pct|vdr_cost)
TC1|Context re-reading|attention processes all prior turns on every generation step|dominant computational cost|0 (state in KB)
TC2|State reconstruction|"as we discussed earlier..." recapping prior findings|~15%|0 (KB query by integer address)
TC3|Computation|digit-by-digit arithmetic, sorting, filtering via token prediction|~20%|0 (exact primitives)
TC4|Deduction|causal chains written as reasoning prose|~15%|0 (Prolog evaluation)
TC5|Formatting|table pipes, JSON braces, markdown headers, code indentation|~20%|0 (grammar templates)
TC6|Hedging|"approximately," "it appears that" — no computational basis|~10%|0 (exact confidence fractions)
TC7|Judgment|intent recognition, step selection, formalization, assessment|~10%|LM tokens (irreducible)
TC8|Prose|natural language framing, explanations, conclusions|~10%|LM tokens (irreducible)
TC9|Command tokens|structured primitive invocations (~8 LM tokens each)|0% conventional|5-50 calls per prompt = 40-400 tokens

# pipeline(id|stage|mechanism|lm_tokens)
PL1|Input cleanup|typo correction KB + string primitives (B168, B174, B163) + classification KB|0
PL2|Scope resolution|path registry (B351) maps tokens to integer IDs within active scope chain|0
PL3|Data fetching|KB query (B378), dict_get (B229), ring_read (B337), stack_to_list (B327), lru_get (B335)|0
PL4|Grammar parsing|grammar recognizes structural tokens, extracts typed fields into dicts|0
PL5|Context assembly|corrected input + resolved references + fetched data + grammar structure + investigation state → compact typed input|0
PL6|Judgment|LM reads assembled context; intent recognition, step selection, formalization into command tokens/Prolog rules/scripts|LM tokens (core value)
PL7|Output|grammar provides all structural tokens; LM fills content slots with prose; data values render from KB; confidence as exact fraction|LM tokens for prose only

# crossover(id|metric|value|notes)
CR1|Cost of 1 LM token|~10⁶ float operations|full forward pass + softmax over 50k+ vocab
CR2|Cost of 1 Q335 operation|~10³ integer operations|multiplication + divmod on ~100-digit numbers
CR3|Single-token budget in Q335 ops|~1,000-10,000|one LM token buys 1k-10k Q335 operations
CR4|SRE turn: saved tokens|2,790|3,000 conventional − 210 VDR
CR5|SRE turn: primitive ops|~500|comparisons, confidence propagation, counter increments
CR6|Required Q335 slowdown for breakeven|~5,580×|at turn 1; grows to ~200,000× by turn 20
CR7|Actual Q335 slowdown vs float|~100-1,000×|margin of 10-100× on single turn, growing with length

# scaling(id|turn|conventional_cumulative|vdr_cumulative|ratio)
SL1|1|6,000 (3k gen + 3k attn)|260|23:1
SL2|5|60,000|1,300|46:1
SL3|10|195,000|2,600|75:1
SL4|20|690,000|5,200|133:1
SL5|50|3,900,000|13,000|300:1
SL6|100|15,300,000|26,000|588:1
# Conventional: quadratic (each turn re-reads all prior). VDR: linear (each turn costs same fixed amount). Ratio grows continuously.

# quality_scaling(id|turn|conventional_accuracy|vdr_accuracy)
QS1|1|baseline|baseline
QS2|5|slight degradation|improved (5 turns of findings in KB)
QS3|10|noticeable degradation|further improved
QS4|20|significant degradation|full investigation accumulated
QS5|50|severe degradation|mature knowledge base
QS6|100|unreliable|comprehensive knowledge base
# Curves move in opposite directions: conventional degrades, VDR improves.

# capability_boundary(id|data_type|size|token_equiv|conventional|vdr|mechanism)
CB1|JSON metrics|1 MB|~300k tokens|cannot load|routine|B424 fetch + B246 parse
CB2|Document (docx)|10 MB|~2.5M tokens|cannot load|routine|B391 read + B410 script parse
CB3|CSV dataset|5 MB|~1.2M tokens|cannot load|routine|B391 read + B248 parse
CB4|Code repository|200 files|~500k tokens|cannot hold simultaneously|routine|B405 tree + B391 per-file
CB5|Knowledge base|2,000 articles|~5M tokens|cannot search|routine|B404 glob + indexed KB query
CB6|Portfolio|500 positions|~25k tokens|overflows useful context|routine|B248 parse + VDR primitives
CB7|Correlation matrix|500×500|cannot compute|exact|B082 vec_dot + B085 mat_new
CB8|Time series trend|90 days × 50 series|cannot process all|exact|B070 discrete derivative
CB9|Cross-reference|2,000 documents|cannot hold|constant-time|B380 kb_query_across

# use_cases(id|case|conventional_tokens|vdr_tokens|reduction|conventional_quality|vdr_quality)
UC1|SRE incident (5 turns)|15,000|210|98.6%|degrading with context length|constant; exact metrics; 90/100 confidence
UC2|Legal contract review (10 turns)|30,000|1,130|96.2%|loses cross-references|full cross-ref via KB connections
UC3|Medical synthesis (40 papers)|80,000|4,740|94.1%|misses distant contradictions|exact stats; all contradictions via Prolog
UC4|Codebase migration (200 files)|100,000 (partial)|6,700 (complete)|93.3%|partial with regressions|complete with test verification
UC5|Financial portfolio (500 positions)|15,000 (partial)|600|96.0%|approximate arithmetic|exact arithmetic; zero drift
UC6|Customer support (per query)|500|150|70.0%|training data recall|indexed KB query with provenance
UC7|Academic grading (150 essays)|200,000 (partial)|57,230 (complete)|71.4%|inconsistent; rubric drift|consistent; clean rubric per essay

# use_case_token_breakdown(id|case|state_recon|computation|deduction|formatting|hedging|command_tokens|judgment|prose)
TB1|SRE (conventional)|2,250|3,000|2,250|3,000|1,500|0|1,500|1,500
TB2|SRE (VDR)|0|0|0|0|0|80|50+20|60
TB3|Financial (conventional)|0|5,000|0|3,000|1,000|0|500|500 (+ 5k data parsing)
TB4|Financial (VDR)|0|0|0|0|0|200|100|300
TB5|Grading (conventional)|30,000 rubric|0|0|40,000|0|0|45,000|20,000 (+ 65k consistency overhead)
TB6|Grading (VDR)|0|0|0|0|0|200|45,000|12,000 (+ 30 script)

# error_elimination(id|error_class|conventional_source|conventional_rate|vdr_mechanism|vdr_rate)
EE1|Arithmetic|digit prediction|~2-5% per op; compounds|exact integer primitives (B001-B008, B139-B159)|0
EE2|State loss|attention dilution over conversation|~3-5% per turn cumulative|KB persistence at integer addresses (B378)|0
EE3|Formatting|structural token prediction|~3-10% per response|grammar templates|0
EE4|Retrieval|attention over training data|~5% fabrication risk|KB query by integer address|0
EE5|Deduction|reasoning chain prose|~10% per 5-step chain|Prolog evaluation (structural unification)|0
EE6|Confidence|hedging language (no computational basis)|100% imprecise|exact VDR fraction from propagation rules|0 (exact fraction)
# Remaining error surface: LM judgment only (intent recognition, step selection, prose) — LM's strongest tasks.

# cumulative_error(id|case|operations|conventional_error_prob|vdr_error_prob)
CE1|SRE (35 ops)|20 comparisons + 5 aggregations + 10 retrievals|~73%|0% (all primitive)
CE2|Legal (80 ops)|50 retrievals + 10 arithmetic + 20 cross-refs|~99%+|0% (all primitive)
CE3|Financial (1025 ops)|500 muls + 500 comparisons + 25 aggregations|effectively 100%|0% (all primitive)
CE4|Grading (300+ ops)|150 retrievals + 150 sums + statistics|effectively 100%|0% (all primitive)

# attention_reduction(id|function|conventional_load|vdr_load|mechanism)
AT1|Relevance determination|full context window|pre-scoped by KB tree|lexical scoping
AT2|Fact retrieval|search across all positions|not needed|integer-addressed KB query
AT3|State tracking|implicit across history|not needed|persistent KB fields
AT4|Relationship mapping|inferred from co-occurrence|not needed|typed connections
AT5|Importance weighting|learned from training|not needed|exact confidence fractions
AT6|Intent recognition|user message + full context|user message + structured summary|pre-parsed, pre-typed input
AT7|Step selection|full reasoning over context|selection from known primitives|low-entropy reference selection

# attention_mechanisms(id|mechanism|transcendentals|vdr_native|suitability_reduced_load)
AM1|SM1 Taylor softmax|yes|via Q335 fn_remainder|overqualified
AM2|SM2 rational surrogate|no|fully native|well-matched (preferred for GPU)
AM3|SM4 Padé approximant|no|fully native|well-matched
AM4|AT4 linear attention|no|fully native if kernel polynomial/ReLU|simplest option
AM5|AT5 surrogate-weighted|no|fully native|well-matched for pre-structured input

# grammar_savings(id|format|structural_pct|tokens_saved_typical|error_eliminated)
GS1|JSON (20 fields)|55%|110 of 200|mismatched braces, missing commas, unclosed strings
GS2|Markdown table (20 rows)|60%|300 of 500|misaligned columns, missing pipes
GS3|CSV (50 rows)|50%|200 of 400|unescaped commas, inconsistent quoting
GS4|Code (30 lines)|40%|120 of 300|missing semicolons, mismatched brackets
GS5|Structured prose|25%|500 of 2,000|formatting inconsistencies
GS6|Incident report|50%|400 of 800|template deviations

# grammar_amortization(id|grammar|definition_cost|savings_per_use|break_even|typical_uses)
GA1|JSON object|15 tokens|110 tokens|1st use|10+/session
GA2|Markdown table|12|30/row|1st use|5+ tables
GA3|Feedback template|20|60|1st use|150 (per student)
GA4|Incident report|25|400|1st use|reused across incidents
GA5|API response|15|80|1st use|100+ queries
# All grammars break even on first use. Persist in KB tree. Inherit through scope.

# vocab_constraint(id|slot_type|full_vocab|constrained|softmax_reduction|error_reduction)
VC1|Boolean|50,000+|2|25,000×|~99.99%
VC2|Enum (4 values)|50,000+|4|12,500×|~99.99%
VC3|KB identifier (200)|50,000+|200|250×|~99.6%
VC4|Numeric (3 digits)|50,000+|1,000|50×|~98%
VC5|Free text|50,000+|50,000+|1×|baseline

# clone_economics(id|aspect|detail)
CL1|Drift elimination|each clone operates within optimal range (early conversation); infrastructure overhead per turn stays at turn-1 level throughout
CL2|Lifecycle overhead|40 tokens per clone lifecycle (snapshot + spawn + checks + kill + respawn); 0.38% of 50-turn clone budget
CL3|Knowledge accumulation|4 clones × 50 turns = 200 turns: 103 persistent facts accumulated; conventional at turn 200: 600k+ tokens processed with severe degradation
CL4|Quality monotonic|each successive clone starts fresh but has all prior persistent facts at integer addresses; knowledge grows, LM stays fresh

# clone_accumulation(id|clone|turns|persistent_facts_added|total_available)
CA1|Clone 1|50|35|35
CA2|Clone 2|50|28|63
CA3|Clone 3|50|22|85
CA4|Clone 4|50|18|103
# Total: 200 turns, 42,000 LM tokens, 103 provenance-tagged facts. Conventional: 600k+ tokens, severe degradation.

# command_token_entropy(id|mode|vocab_size|bits_per_token|tokens_per_action|error_free_prob)
EN1|Command token|~300 names + ~200 paths|~6 avg|~8|~99.2%
EN2|JSON function call|50,000+|~15.6|~30|~86.0%
EN3|Free-form code|50,000+|~15.6|~50|~60.5%
EN4|Natural language reasoning|50,000+|~15.6|~100|~13.3%
# Command tokens: 10× lower entropy than JSON, 16× lower than natural language. Lowest error probability.

# context_utilization(id|turn|conventional_total|conventional_available_pct|vdr_total|vdr_available_pct|efficiency_ratio)
CU1|1|5,000|40%|800|50%|1.25×
CU2|5|18,000|10%|1,000|45%|4.5×
CU3|10|33,000|4.5%|1,200|40%|8.9×
CU4|20|63,000|2.4%|1,500|33%|13.8×
CU5|50|153,000|saturated (0%)|1,500|33%|∞
# Conventional saturates — context fills with own prior output. VDR never saturates.

# primitive_cost_tiers(id|tier|int_ops|examples|pct_of_448)
PT1|Trivial (1-3)|1-3|counter inc, lock check, bitset test, dict_get|~28%
PT2|Light (4-10)|4-10|VDR add, compare, string contains, list filter step, kb_query match|~35%
PT3|Medium (10-100)|10-100|VDR multiply, sort, gcd|~25%
PT4|Heavy (100-10k)|100-10k|matrix multiply, determinant, softmax, discrete derivative|~10%
PT5|Intensive (10k+)|10k+|matrix inverse (large), deep fn_sqrt, correlation matrix, DFT|~2%
# Every primitive costs less than 1 LM token equivalent. Most cost <0.001 tokens.

# workday_economics(id|domain|conventional_daily|vdr_daily|ratio|highest_ratio_task|lowest_ratio_task)
WD1|SRE|640,000|26,000|24.6:1|postmortem (120:1)|ad-hoc query (5:1)
WD2|Legal|152,000|11,690|13.0:1|contract review (26.5:1)|memo drafting (3:1)
WD3|Research|156,000|10,740|14.5:1|synthesis (16.9:1)|report drafting (3.3:1)
WD4|Development|130,000|19,675|6.6:1|migration (14.9:1)|feature impl (2.5:1)
WD5|Finance|200,000|15,000|13.3:1|portfolio analysis (25:1)|commentary (3:1)
WD6|Education|250,000|60,000|4.2:1|statistics (∞)|essay grading (3.5:1)
WD7|Support|50,000|8,000|6.3:1|setup (2500:1 amortized)|KB query (3.3:1)
# Pattern: data/computation/state tasks → 10:1 to 100:1+. Prose generation tasks → 2:1 to 4:1. Floor never below 2:1 (grammar always saves structural tokens).

# data_primitive_memory(id|primitive|capacity|bytes|notes)
DM1|Counter|1 value|16|i64 + bounds
DM2|Lock|1 flag|24|bool + holder + timestamp
DM3|Queue|64 entries|2,048|bounded FIFO
DM4|Stack|32 entries|1,024|bounded LIFO
DM5|LRU Cache|128 entries|8,192|key + value + timestamp
DM6|Ring Buffer|90 entries|2,880|overwrites oldest
DM7|Bitset|256 bits|32|packed bits
# SRE incident full live state: ~21 KB (12 primitives). Snapshot ~25 KB. Conventional context equivalent: ~240 KB (60k tokens).

# snapshot_sizes(id|use_case|active_kbs|data_prims|snapshot_kb|conventional_equiv_kb)
SS1|SRE incident|5|12|~25|~240
SS2|Legal contract|8|6|~15|~120
SS3|Medical synthesis|42|8|~40|~320
SS4|Codebase migration|205|10|~180|~400
SS5|Financial portfolio|10|6|~50|~60
SS6|Support KB|3|4|~8|~2
SS7|Academic grading|155|8|~120|~800
# Snapshots 3-7× smaller than conventional context; contain typed queryable state not raw tokens.

# conversion_boundary(id|source_type|example|exact|max_error|provenance)
CV1|Terminating decimal|"3.14"|yes (314/100)|0|source:decimal, error:0
CV2|Integer string|"4017"|yes (4017/1)|0|source:integer, error:0
CV3|Currency|"$2,500,000.00"|yes|0|source:currency, error:0
CV4|Scientific notation|"2.78e-16"|yes|0|source:scientific, error:0
CV5|Prometheus gauge|"0.847"|yes (847/1000)|0|source:prometheus, error:0
CV6|Float-origin|"3.141592653589793"|to source precision|±5×10⁻¹⁶|source:float64, error:5e-16
# Every conversion logged as KB fact. Operations on exact values produce exact results. Float-origin values have bounded tracked error.

# prolog_composition_economics(id|composed_op|components|formalize_cost|conventional_equiv|reuses|amortized_cost)
PC1|Steady-state entropy|markov_steady + entropy_terms|25 tokens|200+|5+|5 tokens/use
PC2|Weighted anomaly score|mean + sub + abs + div|30|150+|20+|1.5
PC3|SLA breach projection|ring_read + derivative + mul + compare|35|300+|50+|0.7
PC4|Contradiction detection|kb_query + sign + less_than|40|250+|40+|1.0
PC5|Migration classifier|split + filter + group_by|25|180+|200+|0.125
# Rules at org level reused 10,000+ times → 0.0025 tokens/use. Conventional re-derives from scratch every time.

# builtin_patterns(id|pattern|builtins|base_tokens|per_item_tokens|use_cases)
BP1|Data ingestion|B391/B424 → B246/B248 → B254 → B376|32 base + 16/value|—|all use cases
BP2|Filter-sort-aggregate|B198 → B202 → B187 → B047/B049 → B233|40 total|—|SRE metrics, portfolio, support, grading
BP3|Hypothesis-test|B376(rule) → B378(query) → B003/B002(confidence) → B376(finding) → B298(counter)|60 per hypothesis|—|SRE, medical, decision analysis
BP4|Document processing|B391 → B410(script, 30 tokens once) → B246 → B236 → B229/section → LM judgment → B233|80 base + 16/section|varies for judgment|legal, grading, document review
BP5|Correlation-join|B378 + B378 → B198+B196 → B017/pair → B208 → B202|56 base + 8/comparison|—|SRE deployment correlation, medical contradictions

# grant_budgets(id|use_case|grants_issued|grants_consumed|logged_facts)
GB1|SRE incident|105|23|23
GB2|Legal contract|15|8|8
GB3|Medical synthesis|200|82|82
GB4|Codebase migration|1,500|620|620
GB5|Financial portfolio|615|510|510
GB6|Support KB setup|2,500|2,003|2,003
GB7|Academic grading|505|305|305
# Every grant consumption = logged KB fact. Full operational audit trail.

# relationships(from|rel|to)
P1|quantified_by|TC1-TC6
P2|defines|TC7-TC9
P3|demonstrated_by|CR1-CR7
P4|demonstrated_by|SL1-SL6
P5|demonstrated_by|CB1-CB9
P6|demonstrated_by|EE1-EE6,CE1-CE4
PL1-PL5|eliminates|TC1-TC6
PL6-PL7|produces|TC7-TC9
CR4|margin_grows_via|SL1-SL6
QS1-QS6|opposite_direction_to|SL1-SL6(conventional degrades, VDR improves)
UC1-UC7|demonstrates|P1,P2,P5,P6
TB1-TB6|decomposes|UC1,UC5,UC7
EE1-EE6|follows_from|P6
AT1-AT7|reduced_by|PL1-PL5
AM1-AM5|enabled_by|AT1-AT7(reduced workload)
GS1-GS6|quantifies|P1(formatting elimination)
GA1-GA5|demonstrates|grammar amortization (break even on first use)
VC1-VC5|quantifies|AM2-AM5(constrained softmax)
CL1-CL4|enables|QS1-QS6(quality monotonic increase)
CA1-CA4|demonstrates|CL3(knowledge accumulation)
EN1-EN4|quantifies|TC9(command token efficiency)
CU1-CU5|demonstrates|P4(context saturation divergence)
PT1-PT5|supports|CR3(primitive cost << 1 LM token)
WD1-WD7|aggregates|UC1-UC7(workday scale)
PC1-PC5|demonstrates|Prolog composition economics
BP1-BP5|patterns_for|UC1-UC7
SS1-SS7|supports|CL2(snapshot sizes trivial)

# section_index(section|title|ids)
1|The Token Cost Problem|P1,TC1-TC9
2|The Prompt Flow|PL1-PL7
3|Token Accounting|P2,TC7-TC9
4|The Crossover Calculation|P3,CR1-CR7
5|Conversation Length Scaling|P4,SL1-SL6,QS1-QS6
6|The Capability Boundary|P5,CB1-CB9
7|Use Case Demonstrations|UC1-UC7,TB1-TB6
8|Accuracy by Construction|P6,EE1-EE6,CE1-CE4
9|The Attention Reduction|AT1-AT7,AM1-AM5
10|Grammar as Token Eliminator|GS1-GS6,GA1-GA5,VC1-VC5
11|The Disposable Clone Advantage|CL1-CL4,CA1-CA4
12|Cumulative Token Economics|WD1-WD7
AppA|Token Cost Comparison Tables|UC1-UC7,TB1-TB6
AppB|Crossover Analysis|CR1-CR7,SL1-SL6
AppC|Builtin Call Patterns|BP1-BP5
AppD|Grammar Savings Quantification|GS1-GS6,GA1-GA5,VC1-VC5
AppE|Attention Mechanism Comparison|AT1-AT7,AM1-AM5
AppF|Capability Boundary Cases|CB1-CB9
AppG|Conversation Length Scaling Data|SL1-SL6,QS1-QS6
AppH|Primitive Cost Classification|PT1-PT5
AppI|Data Primitive Memory|DM1-DM7,SS1-SS7
AppJ|Command Token Entropy|EN1-EN4
AppK|Context Window Utilization|CU1-CU5
AppL|Grammar Amortization|GA1-GA5
AppM|Prolog Rule Composition|PC1-PC5
AppN|Conversion Boundary Precision|CV1-CV6
AppO|Grant Budget per Use Case|GB1-GB7
AppP|Disposable Clone Lifecycle|CL1-CL4,CA1-CA4
AppQ|Operational Environment Cost|BP4(scripts written once, executed N times)
AppR|Knowability Impact on Token Cost|CF sources × verification cost
AppS|Token Flow Diagrams|PL1-PL7(conventional accumulates, VDR flat)
AppT|Error Class Elimination Matrix|EE1-EE6,CE1-CE4
AppU|KB Tree Depth and Query Cost|integer ops per query << 1 LM token
AppV|Format-Specific Token Savings|GS1-GS6 decomposed
AppW|Cross-Paper Validation|507 domain tests + 198 LM tests + 178 compaction tests = 0 VDR errors
AppX|Workday Economics Extended|WD1-WD7 decomposed by task

# decode_legend
id_prefixes: P=principle, TC=token_category, PL=pipeline, CR=crossover, SL=scaling, QS=quality_scaling, CB=capability_boundary, UC=use_case, TB=token_breakdown, EE=error_elimination, CE=cumulative_error, AT=attention_reduction, AM=attention_mechanism, GS=grammar_savings, GA=grammar_amortization, VC=vocab_constraint, CL=clone_economics, CA=clone_accumulation, EN=entropy, CU=context_utilization, PT=primitive_cost_tier, WD=workday, DM=data_primitive_memory, SS=snapshot_size, CV=conversion_boundary, PC=prolog_composition, BP=builtin_pattern, GB=grant_budget
token_accounting: total = judgment + command; infrastructure = 0; conventional: total = judgment + infrastructure (infrastructure dominates 80-95%)
reduction_range: 70-98.6% across 7 use cases; floor never below 2:1 (grammar always saves structural tokens)
scaling: conventional O(n²) with turns (quadratic attention); VDR O(n) (flat per turn); ratio grows continuously
capability: data enters through primitives not token stream; arbitrary volume; context window never consumed by data
accuracy: 6 error classes structurally eliminated; remaining surface = LM judgment only (strongest tasks)
crossover: Q335 needs ~10,000× slower than float to break even at turn 1; margin grows with conversation length
clone_model: 40 tokens overhead per lifecycle; knowledge accumulates monotonically; LM stays permanently fresh
paper_status: introduces no new primitives, builtins, struct fields, or modules; pattern-of-use analysis over existing VDR-1 through VDR-14 specification
