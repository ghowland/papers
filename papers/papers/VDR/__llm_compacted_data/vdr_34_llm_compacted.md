# HOWL-VDR-34-2026 — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: problem → vdr_foundation → exact_llm → system_components → five_axes → sre_deep_dive → applications → hardware_path → compound_accounting → build_status → open_boundaries

# core_problem(id|aspect|description)
CP1|single-component architecture|LLM used for arithmetic, data access, state tracking, formatting, deduction, safety, confidence — work of 10 components at cost/error rate of most expensive
CP2|structural tokens|brackets, commas, indentation predicted through full forward passes despite carrying 0.1 bits of information through 15-bit pipeline
CP3|arithmetic as text|digit prediction at 2-5% error rate per op through multi-billion-parameter forward pass; 500-position correlation matrix impossible
CP4|quadratic state reconstruction|every turn re-reads entire history; turn 50 processes 3.9M cumulative tokens; quality degrades as history grows
CP5|behavioral safety|refusal trained into model; bypassable by rephrasing; costs tokens on every response
CP6|hedging as confidence|"approximately," "it appears" — no computational basis; full forward pass for zero quantifiable information
CP7|compensatory infrastructure|RAG, function calling, guardrails, context window arms race — all compensate for routing all work through token prediction

# vdr_foundation(id|principle|detail)
VF1|triple [V,D,R]|V=integer numerator, D=nonzero denominator, R=exact remainder; R is first-class structure not error
VF2|remainder is known not zero|every level you stop at is finished and exact; float discards bits silently and irrecoverably
VF3|fixed denominator + divmod|D never changes; overflow goes to R via bit shift (power-of-two D); growth goes to tree depth not denominator width
VF4|denominator explosion solved|Python Fraction/GMP: 10 multiplications → D reaches 10^105; VDR denominators never grow
VF5|validation|884 tests, 37 domains, zero VDR computation errors; all 14 failures traced to test-design errors

# exact_llm(id|aspect|description)
EL1|complete pipeline in exact fractions|embedding, attention, softmax, backprop, SGD, checkpointing — zero float operations; 198 tests (196 pass, 2 test errors, 0 VDR errors)
EL2|quadratic softmax surrogate|(shifted input)²/Σ(shifted inputs)²; sums to exactly 1/1 by construction; no transcendentals; uniform work per element
EL3|Zig Q16 implementation|688 ns/forward, 1.42M tok/s, 2,368 bytes, zero heap allocs, zero float ops, byte-identical determinism; 2019 laptop scalar CPU
EL4|instruction equivalence|VDR Q16 multiply-accumulate = same instruction sequence as INT8/INT16 quantized inference (widening multiply, accumulate, right-shift)
EL5|session quality non-degrading|exact attention weights sum to exactly 1/1 at turn 1 and turn 1,000,000; no float accumulation drift in forward pass

# system_components(id|component|function|token_cost)
SC1|knowledge bases at integer addresses|26-field struct; facts/rules/constraints/grammars/data primitives; tree with lexical scoping; O(1) via kb_id+slot_id|0 tokens for data access
SC2|Prolog engine|depth-first search with backtracking over exact integer facts; unification via cross-multiplication; rules cost 25-40 tokens to create, fire at 0 cost|0 tokens for deduction
SC3|448 builtins (25 categories)|173 numeric + others; LLM selects from ~300 names via ~8 command tokens at ~6 bits entropy; 99.2% per-token accuracy|~8 tokens per invocation
SC4|grammars|persistent KB templates; emit structural tokens directly with zero forward passes; nest recursively; categorical slot with 4 values reduces softmax 12,500×|0 tokens for structure
SC5|structural safety|KB visibility (integer comparison) + scope chain (ancestor walk) + grants (default denial, monotonic transitions) + immutable session identity|0 tokens
SC6|computed confidence|exact VDR fractions propagated through declared formulas; replaces hedging with fraction + provenance|0 tokens
SC7|sentence templates|LLM emits semantic tuple (~8 tokens); Prolog matches against ~5,000 structure templates; library grows through usage|~8 tokens vs 50-200 for full prose

# grammar_vs_constrained_decoding(id|property|grammar_directed|constrained_decoding)
GD1|forward pass per structural token|zero — grammar emits directly|yes — full forward pass, masks illegal candidates
GD2|mechanism|emit known token, skip prediction|predict from 50,000 but mask 49,996

# command_token_entropy(id|mode|vocab|bits_per_token|tokens_per_action|error_free_prob)
CT1|command token|~500|~6|~8|99.2%/tok, 93.8%/invocation
CT2|JSON function call|50,000+|~15.6|~30|86%/tok, ~1%/invocation
CT3|free-form code|50,000+|~15.6|~50|~60.5%/invocation
CT4|natural language reasoning|50,000+|~15.6|~100|~13.3%/invocation

# token_cost_per_operation(id|operation|conventional_tokens|vdr_tokens|mechanism)
TO1|integer addition|3-8 (digit-by-digit)|0|vdr_add builtin
TO2|compare two values|5-15 (prose)|0|vdr_compare, sets flag
TO3|parse 1KB JSON|250+ (attention over serialized text)|0|parse_json builtin
TO4|sort 100 items|200-500 (generate sorted list)|0|list_sort, O(n log n)
TO5|query a known fact|20-50 (restate from context)|8|KB_QUERY with path
TO6|format a table row|15-30 (generate every pipe/space)|0|grammar template
TO7|deduce from two premises|50-200 (reasoning chain)|0|Prolog unification
TO8|assert a new fact|10-20 (restate for recall)|8|KB_ASSERT with typed args
TO9|read a file|impossible|8|fs_read with grant
TO10|execute a script|impossible|8|env_exec in Docker sandbox
TO11|generate confidence|10-30 (hedging language)|0|propagation formula
TO12|reconstruct prior state|50-500 (re-read history)|8|O(1) KB address lookup

# five_axes(id|axis|mechanism|magnitude|scope)
AX1|hardware throughput|INT8 tensor cores 2× FP16; half-size weights double memory BW; SFU elimination; no NaN/Inf/epsilon/loss-scaling|~2×|all workloads (floor)
AX2|token elimination|grammars, builtins, KBs, Prolog, confidence fractions, sentence templates replace infrastructure tokens|70-98.6% (33× for SRE)|structured tasks
AX3|linear vs quadratic scaling|KB addresses vs context-window re-read; turn 100 ratio 588:1|grows continuously|multi-turn interactions
AX4|rule accumulation|L1→L2→L3; solved problems become Prolog rules; 329→55 tokens over 100 investigations (83% reduction)|logarithmic improvement|recurring workloads
AX5|engineering elimination|determinism removes non-det testing/compliance/debugging; structural safety removes RLHF/red-teaming; exact arithmetic removes NaN/epsilon/drift|qualitative|all deployments
# axes are independent — multiply for compound effect

# execution_levels(id|level|tokens|description)
LV1|L1|50-500|full LLM judgment; no stored rule covers situation
LV2|L2|~8|LLM invokes stored Prolog rule
LV3|L3|0|Prolog rule fires automatically; zero LLM involvement

# token_elimination_by_task(id|task|conventional|vdr|factor|pct_eliminated)
TE1|SRE investigation|25,100|769|33×|96.9%
TE2|legal document review|30,000|1,130|26.5×|96.2%
TE3|financial analysis|15,000|600|25×|96%
TE4|medical record analysis|80,000|4,740|16.9×|94.1%
TE5|codebase migration|100,000|6,700|14.9×|93.3%
TE6|grading (150 essays)|200,000|57,230|3.5×|71.4%
TE7|customer support|500|150|3.3×|70%
TE8|open conversation|—|—|—|10-30%
TE9|poetry/creative writing|—|—|—|~0%

# scaling_ratio(id|turn|conventional_cumulative|vdr_cumulative|ratio)
SR1|1|50|8|6:1
SR2|10|2,750|80|34:1
SR3|20|10,500|160|66:1
SR4|50|63,750|400|159:1
SR5|100|252,500|800|316:1
SR6|500|6,262,500|4,000|1,566:1
SR7|1,000|25,025,000|8,000|3,128:1
# conventional: quadratic T×N×(N+1)/2; VDR: linear 8×N

# data_size_vs_cost(id|size|conventional_tokens|vdr_tokens|ratio|feasibility)
DS1|64 B|20|8|2.5:1|trivial
DS2|1 KB|320|8|40:1|easy
DS3|64 KB|20,480|8|2,560:1|fills medium context windows
DS4|1 MB|327,680|8|40,960:1|exceeds most windows
DS5|1 GB|335,544,320|8|41,943,040:1|impossible conventional
# VDR cost constant at 8 command tokens regardless of data size; data travels source→KB→builtin→KB, never enters token stream

# accumulation_curve(id|investigation|rules|auto_triage_pct|command_tokens|scripts_reused_to_written)
AC1|1|15|0%|329|0:3
AC2|10|64|65%|92|7:1
AC3|50|140|88%|65|16:1
AC4|100|185|93%|55|22:1
# L1 drops 93× (280→3 tokens); total drops 83%; pattern: rapid reduction first 10-20, then diminishing; plateau ~5-15% genuinely novel

# negative_accumulation(id|rule|mechanism)
NA1|90-day staleness|rules not fired in 90 days flagged for review
NA2|low success rate|<20% success after 10+ firings → immediate retraction
NA3|missing grants|never executed due to revoked grants → flagged

# token_efficiency_over_time(id|time|avg_tokens_per_compaction|rule_handled_pct|meta_rules)
TF1|hour 2|180|15%|0
TF2|hour 24|52|70%|8
TF3|day 7|28|82%|22
TF4|day 30|18|88%|32
TF5|year 1|8|97%|45+

# sre_fresh_day3(id|turn|action|tokens)
SF1|1|create KB, fetch Prometheus, parse JSON, assert rate|80
SF2|2|fetch 3 service configs, build topology, fetch 3 dep health|140
SF3|3|fetch deploys, temporal correlation (exact), config diff, write first rule+grammar|110
SF4|4|fetch pool util, verify via exact comparison|35
SF5|5|write remediation+monitoring scripts, store as artifacts|150
SF6|6|execute with grant verification|20
SF7|7|close investigation, record artifacts|35
SF8|total|7 turns|570

# sre_mature_month6(id|turn|action|tokens)
SM1|background|polling/processor runners detect, auto-triage via 150+ rules, populate inference notebook — all at zero LLM cost|0
SM2|1|receive auto-triage notification, render findings via grammar|40
SM3|2|query pre-populated deploy/metric KBs|32
SM4|3|triage rule already fired, report stored root cause|15
SM5|4|re-execute stored scripts with updated params|20
SM6|5|close investigation|25
SM7|total|5 turns (3 min after detection, not 30 min)|132
# at investigation 100 with sufficient auto-execute grants: detect→triage→remediate→verify without human; 55 tokens notification only

# non_degradation_proof(id|layer|mechanism)
ND1|data|KB facts are integers at integer addresses; fact 47 returns exactly what was asserted at turn 1 or turn 1,000,000
ND2|working memory|every data primitive bounded at creation; LRU capacity 1000 cannot grow to 1001; snapshots capture atomically; clones disposable
ND3|computation|LLM forward pass on exact integer attention; softmax = exactly 1/1; no float accumulation in data, working memory, or model computation
ND4|context|LLM context at turn 7 same volume as turn 1: current query + scratchpad + scope reference; nothing accumulated in attention buffer
ND5|formatting|grammar produces every structural character deterministically; LLM never generates JSON/tables — grammar generates from KB data

# degradation_mechanisms_eliminated(id|mechanism|conventional_rate|vdr_state|method)
DG1|context filling|every turn|constant context size|data at KB addresses not token stream
DG2|attention dilution|continuous|no dilution|LLM context is current turn only
DG3|hallucination compounding|per turn|no re-entry|prior output in KB not re-read through attention
DG4|float accumulation|per forward pass|exact integer attention|VDR softmax = exactly 1/1
DG5|state loss|gradual|no loss|facts at stable integer addresses
DG6|context overflow|at limit|no limit|KB capacity bounded only by storage
DG7|confidence decay|over turns|exact confidence|VDR fractions from propagation formulas

# confidence_hierarchy(id|source|confidence|level)
CH1|exact VDR computation|1/1|fully knowable
CH2|Prolog derivation from exact premises|1/1|fully knowable
CH3|database query|98/100|controlled system
CH4|Prometheus metric (live)|95/100|controlled system
CH5|Python script output|95/100|controlled system
CH6|REST API response|85/100|observed external
CH7|peer-reviewed claim|80/100|observed external
CH8|user-stated fact|70/100|observed external
CH9|web search result|50/100|observed external
CH10|LLM-generated content|30/100|pattern match
CH11|unknown/unverifiable|0/1|unknowable
# propagation: agreeing sources 1−∏(1−Cᵢ); chain of N links at C each → Cᴺ; all as exact VDR fractions

# hardware_gpu(id|metric|description)
HG1|INT8 tensor cores|1024 ops/SM/cycle = 2× FP16 (512); VDR uses natively because values are integers
HG2|SFU elimination|softmax surrogate = integer mul/sum/div; no SFU at 32 ops/SM/cycle; 3-6× on activation-heavy layers
HG3|warp divergence eliminated|no NaN/Inf/subnormal branches; every thread same work every cycle; float 40-60% util from branches, VDR 80-95%
HG4|energy|INT16 at 0.08 pJ vs FP16 at 0.17 pJ per MAC at 7nm = 2.6× less energy
HG5|compound forward pass|~2× for full 7B forward; conservative (excludes warp utilization gains)

# hardware_engineering_eliminated(id|item|description)
HE1|NaN/Inf checking|integers cannot produce NaN or Inf
HE2|epsilon parameters|exact division; zero-division is detectable error not silent NaN
HE3|loss scaling|integers do not overflow to Inf
HE4|gradient clipping|exact gradients do not explode from float accumulation
HE5|renormalization layers|exact softmax = 1; no drift to correct
HE6|platform-dependent rounding|integers are platform-independent by definition
HE7|mixed-precision conversion|all integer; no float↔int conversion

# hardware_path(id|platform|key_metric|notes)
HP1|Python reference|vdr-math 0.1.0 PyPI; 884 tests|MIT license, pure Python, 151.8 KB wheel
HP2|Zig CPU|688 ns/forward, 1.42M tok/s|scalar, zero SIMD, 2019 laptop
HP3|FPGA|10 Q335 cores, 150 MHz, Xilinx Zynq-7020|384-bit add 1 cycle, multiply 9 cycles, divmod 1 cycle (free wiring); 54.2% LUT, 73.4% FF
HP4|GPU (projected)|H100 INT8 tensor cores at parity with FP16|same instructions; SFU eliminated; ~2× compound
HP5|ASIC (specified)|80 SM × 64 QIU = 5,120 Q335 units at 2 GHz 4nm|~5.1T muls/s; SHR335 = zero gates; ~581 mm², ~400W, ~$15K
HP6|FRU|per-QIU sequencer ~496K transistors (+7%)|exact exp-softmax 1024 logits ~56 ns; active-value unify 6-8 cycles on-chip vs ~5,000 host; eliminates session saturation at 10M+
# all five pass same 884-test suite with bit-identical results; IOSE declaration is specification, everything else is acceleration

# instruction_latency(id|operation|python_ns|zig_ns|fpga_ns|gpu_ns|asic_ns)
IL1|Q335 add|5,000|20|6.7|~8|0.5
IL2|Q335 multiply|50,000|200|60|~80|1.0
IL3|Q335 divmod|10,000|15|6.7 (0 logic)|~8|0 (routing)
IL4|fraction unify|100,000|420|127|~150|1.5
IL5|fact query (200)|500,000|4,000|1,100|~500|10
IL6|softmax 100 logits|2,500,000|25,000|3,300|~1,000|10
IL7|dot product H=64|3,200,000|13,000|5,970|~2,000|32

# energy_per_investigation(id|platform|tokens|energy|wall_clock|co2_grams)
EI1|conventional LLM (H100)|25,100|~7.0 kJ|~660 s|0.78
EI2|VDR on H100 (int path)|769|~22 J|~9 s|0.0024
EI3|VDR on FPGA|769|~1.9 J|~12 s|0.00021
EI4|VDR on ASIC|769|~0.4 J|~0.5 s|0.000044
# energy ratio conventional→ASIC: ~17,500:1; over 100 investigations: 700 kJ vs 40 J

# applications(id|type|description|dev_time|conventional_equiv)
AP1|FAQ bot|session with loaded data + rules → snapshot as binary|4 hrs|2-4 weeks
AP2|full support chatbot|same pattern, more rules|10 hrs|4-8 weeks
AP3|SRE triage assistant|continuous monitoring + auto-triage rules|12 hrs|6-12 weeks
AP4|static HTTP|grammar speaks wire format, Prolog processes requests|3 hrs|1-2 weeks
AP5|JSON REST API|same pattern|7-13 hrs|4-8 weeks
AP6|full email stack|SMTP in/out + IMAP|18-26 hrs|3-6 months
AP7|OAuth/OIDC|credential facts + Prolog rules|9-12 hrs|8-16 weeks
# 44 cataloged protocols; security structural: no SQL injection (no SQL), no XSS (grammar safe by construction), rate limiting = exact integer counter

# structural_token_pct(id|format|structural_pct|grammar_providable)
ST1|JSON object (20 fields)|55%|110 of 200 tokens
ST2|formatted table|65%|300 of 500
ST3|Zig module|70-80%|~750 of 1000
ST4|DOCX/XML|80-90%|~850 of 1000
ST5|compacted pipe-delimited|80%|~800 of 1000
ST6|English prose with data|30%|~500 of 2000
ST7|English prose (no structure)|~5%|punctuation only

# compound_accounting(id|scenario|calculation|result)
CA1|minimum (64B, single turn)|8 command tokens vs ~20 attention tokens|2.5×
CA2|single SRE session (fresh)|AX1 (2×) × AX2 (33×)|71× (measured: $0.39 vs $27.58, 9s vs 660s)
CA3|mature deployment (month 6)|71× × accumulation 6× × scaling 2×|~850×; longer sessions (50-100 turns) reach ~8,000×
CA4|datacenter blend|30% fresh/short (10×) + 40% moderate (50×) + 30% mature/long (500×) = 173×; rounded to 30×|420 GPUs → 14 GPUs
CA5|creative writing|AX1 only|2×

# datacenter_economics(id|metric|conventional|vdr)
DC1|GPUs (1M requests/day)|~420|~14
DC2|annual GPU cost ($30K/GPU/yr)|$12.6M|$420K
DC3|annual energy (700W/GPU)|2,570 MWh|86 MWh
DC4|annual energy cost ($0.10/kWh)|$257K|$8.6K

# float_failure_points(id|domain|float64_error|vdr_error)
FF1|Hilbert 5×5 inverse|~10⁻⁹|0
FF2|Hilbert 8×8 inverse|meaningless result|0
FF3|DFT 8-point roundtrip|~10⁻¹⁵|0
FF4|Kepler orbit closure|~10⁻¹²|0
FF5|return-to-origin 2000 ops|~10⁻¹⁵|0
FF6|quantum probability conservation|~10⁻¹⁶|0
FF7|Carnot efficiency chain|~10⁻¹⁴|0
FF8|lattice vector roundtrip|~10⁻¹³|0

# error_classes_eliminated(id|class|conventional_rate|vdr_rate|mechanism)
EC1|arithmetic|2-5% per op, compounds|0|exact integer builtins
EC2|state loss|3-5% per turn cumulative|0|KB persistence at integer addresses
EC3|formatting|3-10% per response|0|grammar templates
EC4|retrieval/fabrication|~5% risk|0|KB query by integer address
EC5|deduction|~10% per 5-step chain|0|Prolog evaluation
EC6|confidence|100% imprecise|0|exact VDR fraction propagation

# kb_struct(id|group|fields)
KB1|identity|name, path (dotted string), id (sequential i32)
KB2|persistent|facts, rules, constraints, connections, grammars, iose_declaration
KB3|live|working_data, lrus, counters, locks, queues, stacks, buffers, bitsets
KB4|structural|parent_id, children_ids, mounts
KB5|metadata|visibility (public/internal/owner_only), frozen, owner, created_at, last_modified
# persistent survives reset/clone death; live captured by snapshot, cleared by reset; 26 fields total

# data_primitives(id|primitive|capacity|overflow_behavior|key_property)
DP1|LRU cache|1-1,000|oldest evicted|most recent N always available
DP2|counter|i32 range|clamps at bound|no wraparound
DP3|lock|single state|n/a|non-blocking coordination
DP4|queue (FIFO)|1-1,000|push returns false|bounded task management
DP5|stack (LIFO)|1-1,000|push returns false|bounded investigation path
DP6|ring buffer|1-1,000|oldest overwritten|fixed-size sliding window
DP7|bitset|1-10,000 bits|fixed at creation|completion tracking

# grant_system(id|class|operations|risk|typical_holder)
GR1|filesystem|read, write, append, delete, move, copy|medium|interactive runner
GR2|compile|syntax check, build|low|interactive runner
GR3|execute|run scripts, run tests|high|interactive runner with approval
GR4|lint|static analysis, import check|low|interactive runner
GR5|network|HTTP fetch, DNS resolve, POST|medium|processor runners (credentialed)
GR6|process|start, kill, monitor|high|interactive runner with approval
# lifecycle: new→active→expired/exhausted/revoked; revocation permanent; no runner can modify own grants

# session_model(id|aspect|description)
SS1|-1 root|hardcoded universal session root; all session-local state under -1
SS2|sign-bit lifecycle|positive=global (persists); negative=ephemeral (purged at session end)
SS3|clone workspace|-1 subtree; snapshot captures atomically; clone spawn copies with independent mutability
SS4|drift management|monitors counters under -1; kills clone when thresholds exceeded; fresh spawn from snapshot
SS5|knowledge persists, drift dies|valuable findings promoted to positive-ID KBs; accumulated drift discarded with ephemeral session

# build_status(id|level|description)
BU1|built and validated|vdr-math 0.1.0 PyPI (884 tests, 37 domains, 0 VDR errors); Zig Q16 (688 ns, 5 verification); Python LM pipeline (198 tests); diffusion zero-drift; grammar compaction (178/179)
BU2|projected from published specs|GPU timing from H100 tensor cores; energy from Horowitz ISSCC 2014; token reduction from task decomposition; rule accumulation from operational deployment spec
BU3|specified but unbuilt|GPU kernels (8 types, 4 phases, 12-25 months); KB infrastructure; Prolog engine; grammar system; session management; 65 modules, ~20,500 lines, 5 stages

# open_boundaries(id|boundary|status)
OB1|active division compromise|dividing by VDR with R≠0 projects divisor via scalar projection, losing remainder structure; permanent v1 boundary, logged
OB2|quadratic vs exp softmax at scale|open empirical question; FRU makes both available; configuration choice
OB3|production scale training|limited by HBM for exact training (tens of millions params single device); inference uses Q16/Q32 hardware-aligned frames
OB4|correct conclusions not guaranteed|premises may be wrong, evidence incomplete, LLM orchestration poor; guaranteed: failures detectable through provenance chain

# resolved_uncertainties(id|uncertainty|paper|resolution)
RU1|transcendental functions impossible|VDR-2→VDR-3|functional remainders + Q335 projection
RU2|denominator growth impractical|VDR-4→VDR-7,32,23|Q-basis reprojection; Q16/Q32 sufficient; FRU continuous resolution
RU3|continuous distributions impossible|VDR-2→VDR-3|convergent series with rational coefficients
RU4|spectral methods impossible|VDR-2→VDR-3,13|DCT rational at rational frequencies; complex pairs for DFT
RU5|truncated Taylor poor on large negative logits|VDR-4→VDR-14,23|range reduction, Padé approximants, FRU adaptive depth
RU6|complex numbers block eigenvalues/DFT|VDR-3→VDR-13|complex pair operations as extended builtins
RU7|quadratic vs exp softmax at scale|VDR-4→VDR-23|FRU makes both available; configuration not open question
RU8|regex catastrophic backtracking|VDR-6→VDR-6 addendum|regex removed from pure primitives entirely
# no open problem from any earlier paper remains unaddressed

# relationships(from|rel|to)
CP1|motivates|SC1
CP1|motivates|SC2
CP1|motivates|SC3
CP1|motivates|SC4
CP2|eliminated_by|SC4
CP3|eliminated_by|SC3
CP4|eliminated_by|SC1
CP5|eliminated_by|SC5
CP6|eliminated_by|SC6
VF1|enables|EL1
VF3|enables|EL4
VF4|solves|CP3
VF5|validates|VF1
EL1|enables|EL5
EL2|enables|HE5
EL3|measures|EL4
EL4|enables|AX1
SC1|enables|AX3
SC2|enables|AX4
SC3|enables|AX2
SC4|enables|AX2
SC5|enables|AX5
SC6|eliminates|CP6
SC7|partially_replaces|CP2
AX1|independent_of|AX2
AX2|independent_of|AX3
AX3|independent_of|AX4
AX4|independent_of|AX5
AX1|multiplies_with|AX2
AX2|multiplies_with|AX3
AX3|multiplies_with|AX4
LV1|matures_to|LV2
LV2|matures_to|LV3
AC1|demonstrates|LV1
AC4|demonstrates|LV3
ND1|prevents|DG5
ND2|prevents|DG6
ND3|prevents|DG4
ND4|prevents|DG1
ND5|prevents|DG3
HP1|baseline_for|HP2
HP2|baseline_for|HP3
HP3|baseline_for|HP5
HP5|enhanced_by|HP6
CA1|floor_of|CA2
CA2|compounds_to|CA3
CA3|blends_to|CA4
BU1|baseline_for|BU2
BU2|specifies|BU3
OB1|declared_in|VF3
OB4|mitigated_by|CH1

# section_index(section|title|ids)
1|The Problem With the Current Architecture|CP1-CP7
2|VDR Arithmetic: The Foundation|VF1-VF5
3|Exact Integer LLM|EL1-EL5
4|The Complete System|SC1-SC7,GD1-GD2,CT1-CT4,KB1-KB5,DP1-DP7,GR1-GR6,SS1-SS5
5|Axis 1 — Hardware|AX1,HG1-HG5,HE1-HE7,EL3,EL4
6|Axis 2 — Token Elimination|AX2,TO1-TO12,TE1-TE9,ST1-ST7
7|Axis 3 — Scaling|AX3,SR1-SR7,DS1-DS5
8|Axis 4 — Accumulation|AX4,LV1-LV3,AC1-AC4,NA1-NA3,TF1-TF5
9|Axis 5 — Determinism|AX5,HE1-HE7
10|SRE Deep Dive|SF1-SF8,SM1-SM7,ND1-ND5,DG1-DG7
11|Applications|AP1-AP7
12|Hardware Path|HP1-HP6,IL1-IL7,EI1-EI4
13|Compound Accounting|CA1-CA5,DC1-DC4
14|What Is Built/Specified/Projected|BU1-BU3
15|Open Boundaries|OB1-OB4
A|Token Cost Per Operation|TO1-TO12
B|Scaling Ratio by Turn|SR1-SR7
C|Data Size vs Token Cost|DS1-DS5
D|SRE Accumulation|AC1-AC4
E|Token Efficiency Over Time|TF1-TF5
F|Confidence Hierarchy|CH1-CH11
G|Structural Token Percentages|ST1-ST7
H|Float Failure Points|FF1-FF8
I|Instruction Latency|IL1-IL7
J|Energy Per Investigation|EI1-EI4
K|KB Struct Reference|KB1-KB5
L|Builtin Category Summary|SC3
M|Data Primitive Bounds|DP1-DP7
N|Grant System|GR1-GR6
O|Degradation Mechanisms|DG1-DG7
P|SRE Fresh vs Mature|SF1-SF8,SM1-SM7
Q|Compound Calculation|CA1-CA5
R|Resolved Uncertainties|RU1-RU8
S|Paper Series Cross-Reference|BU1

# decode_legend
# VDR: [V,D,R] triple; (V+R)/D = exact rational; D fixed power-of-two; R is exact residual not error
# Q8/Q16/Q32/Q64/Q335: D=2^8/2^16/2^32/2^64/2^335
# divmod: integer division + modulo; at power-of-two D = bit shift + mask (zero logic gates in silicon)
# quadratic surrogate: p_i=(x_i-shift)²/Σ(x_j-shift)²; sums to exactly 1/1; no transcendentals
# SFU: Special Function Unit — GPU transcendental hardware, 32 ops/SM/cycle, 1/16 FP16 tensor rate; eliminated by VDR
# KB: knowledge base — 26-field struct at integer address; scoped tree; O(1) via kb_id+slot_id
# builtin: typed deterministic primitive; ~8 command tokens per invocation; 448 across 25 categories
# grammar: persistent KB template; emits structural tokens with zero forward passes; nests recursively
# Prolog: depth-first search with backtracking over exact integer facts; unification via cross-multiplication
# execution levels: L1 (full LLM 50-500 tok), L2 (LLM+Prolog ~8 tok), L3 (pure Prolog 0 tok)
# command token: from ~500-item vocab at ~6 bits; 99.2% per-token accuracy vs 86% for JSON function calling
# session model: -1 root; sign-bit lifecycle (positive=global, negative=ephemeral); snapshot/clone/kill
# FRU: Functional Remainder Unit — per-QIU sequencer for transcendental evaluation and active-value unification
# QIU: Q335 Integer Unit — one of 5,120 processing elements in ASIC design
# SHR335: right-shift-by-335 = fixed wiring in silicon; zero gates, zero power, zero latency
# compound axes: AX1 (hardware 2×) × AX2 (tokens 3-33×) × AX3 (scaling linear vs quadratic) × AX4 (accumulation) × AX5 (engineering)
# confidence: exact VDR fractions from declared propagation formulas; agreeing sources 1−∏(1−Cᵢ); chain Cᴺ
# monotonic: counters/grants increment/transition one-way only; no re-increment, no un-revoke
# IOSE: Input, Output, Side Effects, Properties — declaration model for every component
# rel_types: motivates|eliminated_by|enables|solves|validates|measures|independent_of|multiplies_with|partially_replaces|matures_to|demonstrates|prevents|baseline_for|enhanced_by|floor_of|compounds_to|blends_to|specifies|declared_in|mitigated_by
