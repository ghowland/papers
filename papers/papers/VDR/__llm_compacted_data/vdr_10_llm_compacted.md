# OPERATIONAL FOUNDATIONS AND COMPREHENSIVE BUILTIN SPECIFICATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → IOSE model → operational principles → number types → numeric builtins → integration → relationships → sections

# principles(id|principle|rationale)
P1|Every component is an IOSE node|Inputs, outputs, side effects declared; components compose by connecting typed outputs to inputs; any component black-boxable
P2|Operational principles are enforceable Prolog facts not suggestions|15 principles encoded as ~176 Prolog terms (axioms, facts, rules, constraints) in root.system.oso; always in scope
P3|Numeric stack exposes all tested VDR-1 through VDR-3 capabilities|58 VDR-6 numeric primitives replaced by 173 builtins covering exact closed/active arithmetic, lift/rebase, Q-basis, functional remainders, discrete calculus, full linear algebra, probability, polynomial, finite field, Markov, denominator management, integer fast paths, bit ops
P4|Comprehensive slicing ensures no gaps|Define the whole, slice by operand type into 25 categories, verify no gaps, no overlaps, parts sum to whole
P5|The specification is the blueprint for building the system|IOSE declarations are contracts; principles are building code; builtins are materials

# iose_model(id|aspect|detail)
IO1|IOSE node struct|name, inputs ([]TypedSlot), outputs ([]TypedSlot), side_effects ([]DeclaredEffect), properties ([]Property), category (pure/operational/composite), logic_type (operational_logic/application_logic), description
IO2|Composition|Nodes compose by connecting outputs to inputs; output type must match next input type; side effects accumulate through chain
IO3|Black-boxing|Any composite node viewed from outside has single IOSE interface; from inside decomposes into sub-node network
IO4|Properties|pure, deterministic, bounded, idempotent, commutative, associative, invertible, partial, lossless, lossy — each verifiable
IO5|Validation: type compatibility|Before execution, verify output types match next node's input types through entire chain
IO6|Validation: side effect preview|Before execution, collect all declared side effects; constraint system reviews before execution
IO7|Validation: contract verification|After execution, compare declared vs actual logged side effects; undeclared effects or missing outputs are contract violations

# iose_system_decomposition(id|component|category|logic_type|key_io)
IS1|vdr_llm_prolog_system|composite|operational|In: user_prompt, context, active_kbs → Out: response_text, kb_mutations, direct_data → SE: env_ops, grant_consumption, session_changes
IS2|kb_engine|composite|operational|In: op_type, kb_path, fact_or_query → Out: query_results, success → SE: fact_assert, fact_retract, mutation_log
IS3|prolog_engine|pure|operational|In: query, in_scope_kbs → Out: bindings, success_or_fail → SE: none
IS4|primitive_executor|composite|operational|In: primitive_id, resolved_args → Out: result → SE: per-primitive declared
IS5|environment_manager|composite|operational|In: env_id, op, args, grant → Out: exec_result, exit_code → SE: process, file, network, grant_dec, exec_log
IS6|session_manager|composite|operational|In: operation, session_name → Out: session_state → SE: capture, restore, clear, clone, kill
IS7|command_token_parser|pure|operational|In: raw_token_stream → Out: parsed_commands, text_segments → SE: none
IS8|path_registry|operational|operational|In: dotted_path → Out: integer_id → SE: id_assigned_if_new
IS9|grant_verifier|pure|operational|In: operation, location, user → Out: authorized_or_denied → SE: grant_use_decremented
IS10|constraint_checker|pure|operational|In: constraint_set → Out: violations_list → SE: none
IS11|inference_orchestrator|composite|operational|In: notebook_path, problem → Out: conclusion, confidence → SE: kb_asserts, rules_written, evidence_stored

# operational_principles(id|principle|summary|enforcement)
OP1|Control is foundation|Operations requires observation (KB queryable) + agency (primitives executable); without control no efficiency possible|Structural — KB + primitives provide both
OP2|Knowability spectrum|Fully knowable (VDR computation, 1/1) → controlled system (Prometheus, 95-98/100) → observed external (API, 50-85/100) → pattern match (LLM, 30/100) → unknowable (0/1)|Encoded as Prolog facts; feeds VDR-9 confidence propagation
OP3|90/9/0.9 priorities|Each tier 10× more important than next; correctness(90) > completeness(9) > speed(0.9) > style(0.09); exact(90) > monitoring(9) > search(0.9) > LLM memory(0.09)|Decision machine producing consistent results regardless of decider
OP4|Personal experience vs hearsay|Self-verified information is high-trust; each link in reporting chain degrades confidence; 6-link chain at 99%/link = 94% effective|Prescription: verify personally when possible; verification upgrades logged
OP5|Data primacy|Data more trustworthy/durable/portable than logic; data survives goal changes; when data and logic conflict, trust data, fix logic; no logic in data store|KB stores facts and rules (inspectable Prolog terms), not stored procedures
OP6|Comprehensive over aggregated|Top-down: define whole, subdivide preserving total, no gaps, no overlaps; aggregated (bottom-up) trends toward inconsistency|IOSE model prevents interface disagreement; builtin spec covers whole space
OP7|Idempotency|f(f(x))=f(x); safe to re-run after failure/interruption; every operation tagged idempotent or not|session_restore: idempotent; kb_assert existing fact: idempotent; counter_inc: NOT idempotent (needs guards)
OP8|One way to do it|Single canonical method per task category; known, documented, tested; shortcuts detected by IOSE (undeclared side effects)|One primitive per operation type; no alternative paths
OP9|Operational vs application logic|Operational: assumes failure, minimal deps, caches locally, resilient (KB engine, Prolog, session manager); application: assumes environment works, exits on failure (user Python scripts)|IOSE declarations tag logic type; operational wraps application and catches failures
OP10|Models for control vs understanding|Control model (KB, data primitives, snapshots): must stay synced with reality; understanding model (LLM context window): approximate, correctable|Data primitives bridge: LLM reads KB (control) instead of remembering (understanding)
OP11|Knowing the present|All monitoring data is aged; delay may be ms or minutes but never zero; system designed for aged data|Evidence freshness tracking: acquisition timestamp + data timestamp + processing time
OP12|Population statistics only|Statistics valid for populations not individuals; confidence 85/100 means ~85% correct across population, any individual may be wrong|Clone drift thresholds population-calibrated
OP13|Force multiplier safety|Automation amplifies both fixes and failures; bad automated process fails repeatedly at scale; stable operator with subtle bug produces uniformly buggy clones|Verify before automating; 90/9/0.9: verification(90) > deployment speed(9)
OP14|Hearsay chain model|Every link in provenance chain degrades effective confidence; product of link confidences; Prometheus metric through 6 links: 0.99^6 ≈ 94%|System tracks chain and computes effective confidence as product
OP15|No logic in data store|KB stores facts and rules (inspectable Prolog terms); no stored procedures, triggers, or inline computation on assertion/retraction|Structural enforcement

# oso_encoding_stats(id|type|count)
OE1|Axioms (non-negotiable)|15
OE2|Facts (knowability levels, source mappings, IOSE declarations, priorities)|~80
OE3|Rules (decision procedures, validation, cascade, conflict resolution)|~60
OE4|Constraints (enforceable)|21
OE5|Total Prolog terms in root.system.oso|~176

# number_type_hierarchy(id|type|representation|purpose|conversion_to_vdr)
NT1|VDR fraction|[V, D, R] triple|Primary exact type; ground truth|Identity
NT2|Integer|[N, 1, 0] equivalent|Counting, indexing, IDs, bit ops; no denominator overhead|Free lossless promotion
NT3|Decimal display|String at declared precision|Human output only; NOT for computation|Lossy view; generating fraction retained
NT4|Q-basis compressed|[p, 2^k, 0]|Transcendental constants; 22 constants as integers over 2^335|Lossless (qbasis IS a fraction)
NT5|Functional remainder|f(depth:int)→VDR callable|Convergent series, Newton iteration; exact rational at each depth|Via fn_resolve at declared depth

# type_dispatch(id|aspect|detail)
TD1|Automatic selection|System selects computation path by operand types; two integers use fast path; integer+fraction promotes; two same-exponent Q-basis use integer addition
TD2|Transparent to LLM|LLM issues "add these two numbers"; system picks fastest exact path
TD3|Conversion boundaries|Every type conversion has declared boundary: source, target, method, exact error bound; lossless (integer→fraction: error 0) or lossy (fraction→decimal: bounded error logged as provenance fact)

# numeric_builtins_summary(id|subcategory|count|key_builtins)
NB01|Closed arithmetic|8|add, sub, mul, div, neg, abs, pow, reciprocal
NB02|Active arithmetic|5|active_add_same_d, active_add_diff_d, active_mul, active_div_closed, active_div_active (v1 compromise)
NB03|Structure operations|3|lift, rebase, scalar_projection
NB04|Comparison|10|compare, equal, less_than, less_or_equal, min, max, sign, is_zero, is_positive, is_negative
NB05|Rounding and extraction|11|floor, ceil, round, truncate, numerator, denominator, is_integer, is_closed, is_active, simplify, denom_complexity
NB06|Number theory|13|gcd, lcm, mod, exact_int_div, mod_pow, mod_inv, extended_gcd, is_prime, factorial, binomial, fibonacci, euler_totient, chinese_remainder
NB07|List aggregates|8|sum, product, mean, weighted_sum, dot_product, sum_of_squares, harmonic_sum, alternating_sum
NB08|Q-basis operations|7|qbasis_add, qbasis_sub, qbasis_mul (with error bound), qbasis_scalar_mul, qbasis_to_fraction, qbasis_get_constant, qbasis_precision_bits
NB09|Functional remainder|8|fn_sqrt, fn_exp, fn_log, fn_sin, fn_cos, fn_resolve, fn_make_newton, fn_make_series
NB10|Discrete calculus|6|discrete_derivative, discrete_derivative_nth, left_riemann, trapezoidal, finite_diff_table, richardson_extrapolation
NB11|Linear algebra|24|vec: new/dim/get/add/sub/scale/dot/norm_sq/neg (9); mat: new/dims/get/add/mul/scale/transpose/matvec/det/inv/solve/rank/identity/trace/pow (15); plus gram_schmidt
NB12|Probability and statistics|16|mean, variance, median, percentile, mode, prob_normalize, prob_is_valid, prob_entropy_terms, prob_cdf, prob_expected, prob_bayes, prob_joint, prob_marginal, prob_conditional, softmax, softmax_surrogate
NB13|Conversion boundaries|11|from_integer, from_decimal_string, from_ratio_string, to_decimal_string, to_percentage, to_scientific, to_mixed, to/from_continued_fraction, to_egyptian, format_fraction
NB14|Polynomial|8|poly_eval, poly_add, poly_mul, poly_div, poly_gcd, poly_derivative, poly_integral, poly_lagrange
NB15|Finite field|4|gf_add, gf_mul, gf_inv, gf_pow
NB16|Markov|3|markov_steady_state, markov_step, markov_n_steps
NB17|Graph math|2|adjacency_matrix_power, pagerank_exact
NB18|Integer fast path|13|int_add/sub/mul/div/mod/pow/abs/sign/min/max/clamp/range/exact_div
NB19|Bit operations|8|bit_and/or/xor/not/shift_left/shift_right/popcount/bit_width
NB20|Denominator management|5|denom_bits, denom_digits, reproject_qbasis, budget_check, precision_state
# Total numeric: 173 builtins

# revised_builtin_counts(id|category_group|count|source)
RC1|Pure non-numeric|207|VDR-6 + VDR-8 (text, collections, sets, mappings, conversion, time, identity, graphs, logic, KB, data primitives, path/mount, session)
RC2|Pure numeric|197|VDR-10 (173 numeric + 24 linear algebra reclassified)
RC3|Operational|44|VDR-6 (filesystem, compilation, execution, linting, network, process)
RC4|Total|448|25 categories

# builtin_classification(id|classification|count|percentage)
BC1|Pure, deterministic, bounded|392|87.5%
BC2|Pure, deterministic, partial (may fail on some inputs)|12|2.7%
BC3|Operational (requires grant)|44|9.8%

# new_modules(id|module|purpose)
NM1|iose_registry.py|IOSE declaration storage, validation, query
NM2|oso_principles.py|Operational engineering KB loading (axioms, facts, rules, constraints)
NM3|numeric_dispatch.py|Type hierarchy, automatic promotion, fast-path selection
# 37 existing + 3 new = 40 total modules

# iose_side_effect_taxonomy(id|effect|category|reversible|requires_grant)
SE01|kb_fact_added|KB state|Yes (retract)|No
SE02|kb_fact_removed|KB state|Yes (re-assert)|No
SE03|mutation_logged|KB metadata|No (append-only)|No
SE04|scope_changed|Context state|Yes (switch back)|No
SE05|constraint_activated/suspended|KB state|Yes (toggle)|No
SE06|primitive_created|KB live state|Yes (destroy)|No
SE07|counter_mutated|KB live state|Depends (set=yes, inc=no)|No
SE08|lru/queue/stack/ring/bitset_mutated|KB live state|Varies|No
SE09|live_state_captured/overwritten/cleared|Session|Varies|No
SE10|clone_created/destroyed|Session|Created=yes(kill), destroyed=no|No
SE11|file operations|Filesystem|Varies|Yes
SE12|cpu_used|Computation|No|Yes
SE13|process_created/terminated|Process|Created=yes(kill)|Yes
SE14|network_request|Network|No|Yes
SE15|grant_use_decremented|Authorization|No|Inherent
SE16|mount_created/removed|Path structure|Yes|Conditional
SE17|connection_added/removed|KB structure|Yes|No
SE18|id_assigned|Path registry|No (permanent)|No

# falsification_criteria(id|criterion|test_method)
FC1|IOSE declaration mismatch|Component produces undeclared side effect, fails to produce declared output, or accepts undeclared input type
FC2|Principle encoding error|Priority system recommends lower-priority action when higher available; given correct inputs
FC3|Numeric builtin incorrect result|Any VDR-1 through VDR-3 invariant violated; 705 existing tests have produced zero
FC4|Conversion boundary error exceeds bound|Converted value differs from source by more than declared max_error
FC5|Type dispatch correctness|Dispatch selects path producing different result than canonical VDR path for same inputs
FC6|Specification gap|Operation LLM needs not covered by any of 448 builtins or composable from them
FC7|Category overlap|Same operation defined in two categories with potentially different behavior

# claims(id|claim|type)
CL1|System specified in IOSE is buildable, testable, and maintainable|engineering_thesis
CL2|IOSE declarations are contracts ensuring pieces fit together|structural
CL3|Operational principles as enforceable Prolog produce consistent decisions regardless of decider|behavioral
CL4|173 numeric builtins expose full VDR-1 through VDR-3 tested capability|completeness
CL5|448 builtins across 25 categories comprehensively slice the operation space with no gaps|comprehensiveness
CL6|The specification is the blueprint; principles are building code; mathematics is material|architectural_metaphor

# relationships(from|rel|to)
IO1-IO7|define|interface model for all components
IS1-IS11|decompose|system into IOSE nodes
OP1-OP15|govern|all system decisions
OE1-OE5|encode|OP1-OP15 as Prolog
NT1-NT5|form|number type hierarchy
TD1-TD3|dispatch|operations to fastest exact path
NB01-NB20|expose|VDR-1 through VDR-3 capabilities as builtins
IO5|validates|command token chains before execution
IO6|previews|side effects for constraint review
IO7|verifies|contracts after execution
OP2|feeds|VDR-9 confidence propagation
OP3|governs|evidence acquisition priority, lifecycle tradeoffs, prompt-time response
OP5|enforces|KB stores data not logic
OP6|prevents|aggregated inconsistency during implementation
OP7|enables|safe automation and clone recycling
OP13|requires|verification before automation
TD3|logs|conversion boundaries as provenance facts
NB01-NB05|implement|VDR-1 core arithmetic
NB06|implements|VDR-2 Gym 1, 6, 12 capabilities
NB08|implements|MATH-4 Q335 operations
NB09|implements|VDR-1 functional remainders + VDR-4 exact softmax foundation
NB10|implements|VDR-1 discrete calculus
NB11|implements|VDR-1 linear algebra + VDR-2 Hilbert demonstrations
NB14-NB17|implement|VDR-2/3 domain-specific gym capabilities

# section_index(section|title|ids)
1|Context and Purpose|what exists (VDR-1 through VDR-9), what's missing (no IOSE, no principles, incomplete numeric)
2|The IOSE System Model|IO1-IO7,IS1-IS11
3|Operational Engineering Principles|OP1-OP15,OE1-OE5
4|The Number Type Hierarchy|NT1-NT5,TD1-TD3
5|VDR Exact Arithmetic Builtins|NB01-NB05
6|Number Theory Builtins|NB06
7|Q-Basis Transcendental Operations|NB08
8|Functional Remainder Operations|NB09
9|Discrete Calculus Builtins|NB10
10|Linear Algebra Builtins|NB11
11|Probability and Statistics Builtins|NB12
12|Domain-Specific Mathematics|NB14-NB17
13|Integer Fast Path and Bit Operations|NB18-NB19
14|Denominator Management|NB20
15|Comprehensive Builtin Specification|RC1-RC4,BC1-BC3,P4
16|How the Three Components Integrate|IOSE+principles+builtins working together
17|Falsification Criteria|FC1-FC7
18|Implementation Priority|18 phases from IOSE registry through integration testing
A|IOSE Declaration Registry|IS1-IS11 expanded, property definitions, side effect taxonomy
B|Operational Principle Cross-Reference|principles applied by system phase, conflict resolution, encoding statistics
C|Number Type Conversion Matrix|all type-to-type conversions with lossless/lossy, error bounds, external source conversion paths
D|VDR Arithmetic Invariant Test Matrix|closed invariants (17 types), active invariants (8 types), normalization invariants (7 types)
E|VDR Gym Results Mapped to Builtins|which builtins each of 23 gym domains exercises, coverage by category
F|Denominator Growth Reference|growth by operation type, empirical training estimates, reprojection error bounds by Q-basis exponent
G|Builtin Dependency Graph|foundational builtins (9, no dependencies), dependency chains, composition paths
H|IOSE Validation Test Plan|type compatibility, side effect preview, contract verification tests
I|Numeric Builtin Count Reconciliation|VDR-6 58 → VDR-10 173 delta breakdown, full system 448
J|OSO Concept to VDR-LLM-Prolog Mapping|43 OSO concepts mapped to system manifestations
K|Implementation Phase Dependencies|dependency graph, what exists vs what needs building per phase
L|Cumulative Statistics|40 modules, 448 builtins, 25 KB struct fields, ~2665 planned tests

# decode_legend
IOSE: Inputs/Outputs/Side-Effects — the universal interface model for all components
node_categories: pure (no side effects) | operational (side effects, requires grant) | composite (decomposes into sub-nodes)
logic_types: operational_logic (assumes failure, handles it) | application_logic (assumes environment works, exits on failure)
properties: pure|deterministic|bounded|idempotent|commutative|associative|invertible|partial|lossless|lossy
number_types: vdr_fraction (primary) | integer (fast path) | decimal_display (lossy view) | qbasis (compressed transcendental) | functional_remainder (convergent series)
knowability: fully_knowable(1/1) | controlled_system(95-98/100) | observed_external(50-85/100) | pattern_match(30/100) | unknowable(0/1)
priority_system: 90/9/0.9 — each tier 10× more important than next
oso_encoding: axioms(15) + facts(~80) + rules(~60) + constraints(21) = ~176 Prolog terms
claim_types: engineering_thesis|structural|behavioral|completeness|comprehensiveness|architectural_metaphor
rel_types: define|decompose|govern|encode|form|dispatch|expose|validate|preview|verify|feed|enforce|prevent|enable|require|log|implement
revised_totals: 448 builtins (404 pure + 44 operational) across 25 categories; 40 modules; 25 KB struct fields; ~2665 planned tests
