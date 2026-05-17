# VDR-23 FUNCTIONAL REMAINDER HARDWARE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → fru_design → recurrences → inference_chain → training → prolog → scale → chip_update → relationships → sections

# principles(id|principle|rationale)
P1|Remainder is precision control surface|R slot carries structural information about what the Q335 frame did not absorb; FRU gives hardware the ability to act on that information
P2|Adaptive precision per value per operation|Not mixed-precision (coarse, static, heuristic); FRU operates per scalar, at runtime, directed by exact structural information in R
P3|Common path unchanged|R=0 (closed) values run at full QIU throughput with zero FRU overhead; FRU activates only on uncommon path (R≠0, expected <1%)
P4|FRU reuses existing ALU|No separate multiplier or adder; FRU is a sequencer that drives the QIU's 384-bit ALU through recurrence loops; adds control logic not compute logic
P5|Data plane self-sufficiency|With FRU, every primitive in the 448-builtin vocabulary executes natively on QIU array; host CPU never touches data path; enables scale without serialization

# claims(id|claim|type|depends_on)
CL1|FRU adds ~496K transistors per QIU (7% per-unit increase); 2.54B chip-wide; 3.4% die area increase (581→601 mm²)|observation|
CL2|Exact exp-softmax over 1,024 logits: ~56 ns on VDR-22+FRU; competitive with float H100 (100-200 ns)|derivation|
CL3|Single-query latency unchanged — LLM forward pass dominates primitives by 300-30,000×; FRU makes already-negligible time more negligible|observation|P3
CL4|Without FRU: host CPU saturates at ~500K concurrent sessions from remainder round-trips; with FRU: no saturation at 10M+ sessions|derivation|P5
CL5|Continuous remainder resolution eliminates Q-basis reprojection stalls; training step time constant (~15.2μs) vs periodic spikes (~72μs) without FRU|derivation|
CL6|Active-value Prolog unification: 6-8 cycles on-chip with FRU vs ~5,000 cycles host round-trip without|observation|
CL7|At investigation 100 with 150 auto-firing rules: 180 host round-trips eliminated (450μs→0.9μs)|derivation|CL6
CL8|LLM cluster 14× smaller at datacenter scale due to 93% rule automation; QIU chip absorbs rule-driven work at negligible utilization|derivation|P5
CL9|Surrogate vs exact exp-softmax: <1% latency difference at full-model level; matrix multiplies dominate|observation|
CL10|VDR-22+FRU forward pass ~1.9× slower per token than H100 float16; net compute per prompt favors VDR from first prompt due to 85-97% token reduction|observation|
CL11|Reciprocal table covers k=1-64; series needing k>64 terms require Newton reciprocal sub-loop (+~32 cycles/term) or argument reduction|observation|

# concepts(id|name|definition|category)
C1|Functional Remainder Unit (FRU)|Small sequencer per QIU: 4 recurrence registers (384-bit), 3KB reciprocal table, convergence comparator, loop controller; drives QIU ALU through recurrence loops; ~496K transistors, ~0.004 mm²|hardware
C2|Recurrence register file|4 × 384-bit dedicated registers: current term, accumulated sum, input x, divisor/scale; separate from QIU general registers to avoid contention|storage
C3|Reciprocal table|64 entries × 48 bytes = 3KB SRAM; reciprocal of integers 1-64 as Q335 values; replaces division-by-k with multiply-by-reciprocal (1-2 cycles vs full divmod)|storage
C4|Convergence comparator|384-bit magnitude comparison against configurable threshold; determines when FRU stops iterating; 1 cycle|hardware
C5|FEVAL instruction|Opcode 0x35; evaluates functional remainder in R slot to depth in Id register using function tag from R flags; variable latency; pipeline stalls|instruction
C6|Adaptive depth|FRU evaluates fewer terms for values needing less precision; exp(0)=1 in 1 cycle; large-negative shifted logit stops after 4-5 terms when below ranking threshold|property
C7|Continuous remainder resolution|Each multiply's remainder resolved inline by FRU (2-5 cycles); nesting never accumulates; reprojection never triggers; training throughput smooth|mechanism
C8|Exact exponential softmax|SM1 with FRU: Taylor exp per logit at adaptive depth + global reduction + Newton reciprocal + normalization; ~56ns for 1,024 logits; exact sum-to-one|capability
C9|Data-plane completeness|All 448 builtins execute natively on QIU+FRU; host handles only control plane (LLM passes, KB tree mgmt, sessions); eliminates serialization bottleneck|property

# fru_resources(component|transistors|area_4nm_mm2)
Recurrence registers (4 × 384-bit)|36,864|0.0003
Reciprocal table (3KB SRAM)|147,456|0.0012
Convergence comparator|50,000|0.0004
Loop controller + tag decoder|2,000|<0.0001
Interconnect to QIU ALU|~260,000|0.0021
**Per-FRU total**|**~496,320**|**~0.004**
**5,120 FRUs (chip-wide)**|**~2.54B**|**~20.5**

# recurrences(tag|function|recurrence|cycles_per_term|depth_100_digits|total_cycles_100d)
0x01|exp(x)|term_k = term_{k-1} × x × reciprocal[k]|3-4|~45|~180
0x02|sqrt(a)|x_{n+1} = (x_n + a/x_n)/2 via reciprocal mul|~7|~8|~56
0x03|ln(1+x)|term_k = -term_{k-1} × x; sum += term_k × reciprocal[k]|3-4|~33 (with arg reduction)|~161
0x04|sin(x)|term_k = -term_{k-1} × x² × reciprocal[2k] × reciprocal[2k+1]|5-6|~45|~315
0x05|cos(x)|term_k = -term_{k-1} × x² × reciprocal[2k-1] × reciprocal[2k]|5-6|~45|~315
0x06|generic|Microcode from instruction BRAM (≤50 instructions)|variable|variable|variable (Borwein ζ n=210: ~5,880)

# adaptive_depth_exp_softmax(shifted_logit_range|expected_count_1024|fru_depth|cycles_per_element)
0 (the maximum)|1|0 (exact 1)|1
(-0.5, 0)|~50|3-4 terms|14-18
(-2, -0.5]|~200|5-7 terms|22-30
(-5, -2]|~300|8-12 terms|34-50
(-10, -5]|~250|13-18 terms|55-75
(-20, -10]|~150|4-5 terms (threshold cut)|18-22
< -20|~73|2-3 terms (threshold cut)|10-14
**Total 1,024**||**avg ~37.8 cycles**|**critical path ~75 cycles**

# softmax_comparison(property|surrogate_SM2|exact_exp_SM1_FRU)
Transcendentals|None|Taylor exp via FRU
Sum-to-one|Exact (1/1)|Exact (1/1)
Monotonicity|Yes|Yes
Latency (1,024 logits)|~10 ns|~56 ns
FRU required|No|Yes
Adaptive depth|N/A|Yes — less work for well-separated logits
Per-value precision info|No (closed)|Yes (R slot carries truncation metadata)
Full-model latency difference||<1% (matrix multiplies dominate)

# inference_chain(component|common_path_R0|uncommon_path_R_nonzero|fru_role)
Attention QKT multiply|Full QIU throughput; 1-2 cycle mul|Check remainder vs threshold; discard if below|Threshold comparison only
Softmax (surrogate)|20 cycles/element; no FRU|N/A|Not involved
Softmax (exact exp)|N/A|FEVAL per logit at adaptive depth|Core FRU function
ReLU|1 cycle compare+copy|V=0 edge: FEVAL resolves sign from R|<0.01% frequency
Rational scaling|Reduction + reciprocal broadcast|Newton reciprocal via FRU (~32 cycles, once)|Single evaluation, broadcast result
Feedforward linear|Same as attention multiply|Same threshold filtering|Same

# training_without_fru(step|avg_denom_bits|max_denom_bits|pct_R_nonzero|max_depth|reprojection)
0|~10|~12|0%|0|No
1,000|~20|~30|0.1%|2|No
10,000|~35|~48|0.8%|4|Approaching
20,000|~40|~55|1.2%|5|**Yes — stall ~20μs**
50,000|~45|~65|2.0%|7|**Multiple stalls**

# training_with_fru(step|avg_denom_bits|max_denom_bits|pct_R_before|pct_R_after|max_depth|reprojection)
0|~10|~12|0%|0%|0|No
1,000|~10|~13|0.1%|0%|0|No
10,000|~10|~14|0.8%|0%|0|No
20,000|~10|~14|1.2%|0%|0|**Never**
50,000|~11|~15|2.0%|0%|0|**Never**

# training_step_timing(component|without_fru|with_fru|difference)
Forward multiply per param|2 cycles|2 cycles|Same
SHR335|0|0|Same
Remainder check|1 cycle|1 cycle|Same
Remainder resolution (when R≠0)|Host ~5,000 cycles|FRU inline ~3 cycles|1,667× faster
Avg per param (1% spill)|53 cycles|3.03 cycles|17.5× faster
10M params total|51.8 μs|15.2 μs|3.4× faster
Periodic reprojection|~20 μs every ~20K steps|Never|Eliminated
Worst-case step|~72 μs|~15.2 μs (constant)|4.7× faster
Variance|High (spikes)|Near-zero|Smooth

# prolog_unification(term_a|term_b|without_fru|with_fru|improvement)
Atom|Atom|1 cycle (UATOM)|1 cycle|None
Integer|Integer|1 cycle (WCMP)|1 cycle|None
VDR closed|VDR closed|2-3 cycles (CROSS_MUL)|2-3 cycles|None
VDR closed|VDR active|Host ~5,000 cycles|6-8 cycles (FEVAL+CROSS_MUL)|~700×
VDR active|VDR active|Host ~10,000 cycles|8-12 cycles (2×FEVAL+CROSS_MUL)|~1,000×
VDR active|Variable|Host+bind ~5,000 cycles|FEVAL+bind ~6 cycles|~800×

# host_roundtrips(cause|frequency_per_investigation|host_cycles_per_trip|total_per_investigation)
Transcendental evaluation|~5|~50,000|~250,000
Active-value Prolog unification|~12 (at inv 50)|~10,000|~120,000
Remainder resolution for constraint|~3|~20,000|~60,000
Deep remainder traversal (>depth 4)|~1|~100,000|~100,000
**Total**|**~21**||**~530,000**

# concurrent_session_scaling(sessions|roundtrips_per_sec_no_fru|host_utilization_no_fru|roundtrips_with_fru|host_utilization_with_fru)
1,000|21,000|~0.5%|0|~0%
10,000|210,000|~4.6%|0|~0%
100,000|2,100,000|~46%|0|~0%
500,000|10,500,000|**~230% saturated**|~500|~0.001%
1,000,000|21,000,000|**~460% saturated**|~1,000|~0.002%
10,000,000|—|**infeasible**|~10,000|~0.02%

# convergence_thresholds(context|threshold_q335|decimal_equiv|rationale)
Softmax ranking|2^315|~10^(-6) relative|Preserves ranking for logits differing >10^(-6)
Attention intermediate|2^305|~10^(-9) relative|Conservative; score differences typically >10^(-3)
Training gradient|2^285|~10^(-15) relative|Preserves gradient direction for typical learning rates
Constraint evaluation|0|0 (exact)|Axiom constraints must be exact
Conservation law|0|0|Must be exact equality
Prolog unification|Context-dependent|—|Must resolve equality definitively

# chip_update(property|vdr22_base|vdr22_fru|change)
Transistors|68B|70.5B|+3.7%
Die area|581 mm²|601 mm²|+3.4%
TDP|400 W|410 W|+2.5%
Q335 closed throughput|5.1T muls/sec|5.1T muls/sec|Unchanged
SHR335|0 gates, 0 power|0 gates, 0 power|Unchanged
exp(x) depth 10|Host-bound (~μs)|~640M evals/sec (~25 cycles)|Native
exp(x) depth 45|Host-bound (~ms)|~36M evals/sec (~180 cycles)|Native
sqrt(x) 100 digits|Host-bound|~1.6B evals/sec (~32 cycles)|Native
ln(x) with reduction|Host-bound|~480M evals/sec (~130 cycles)|Native
sin(x)/cos(x) depth 45|Host-bound|~28M evals/sec (~225 cycles)|Native
Softmax surrogate (1,024)|~10 ns|~10 ns|Unchanged
Softmax exact exp (1,024)|Host-bound|~56 ns|Native
Active-value unification|Host-bound|~4-8 cycles on-chip|Native
Remainder resolution per value|Host-bound|~2-5 cycles on-chip|Native
Training reprojection stalls|Periodic (~ms)|Eliminated (continuous ~ns)|Continuous

# transformer_latency(component|ops|surrogate_latency|exp_fru_latency|notes)
QKV projection (3 linear)|3×1024×512 matmul|~15 μs|~15 μs|Same
Attention QKT (8 heads)|8×1024×1024×64 dot|~100 μs|~100 μs|Same
Softmax|8×1024 rows × 1024|~3 μs|~6 μs|+3μs for FRU exp
Value mixing|8×1024×1024×64|~100 μs|~100 μs|Same
Output projection|1024×512 matmul|~5 μs|~5 μs|Same
Residual + rational scaling|add + reduction + mul|~0.1 μs|~0.1 μs|Same
FF linear 1 (4×)|1024×512×2048|~50 μs|~50 μs|Same
ReLU|1024×2048 compare|~0.4 μs|~0.4 μs|Same
FF linear 2|1024×2048×512|~200 μs|~200 μs|Same
**Per-layer total**||**~474 μs**|**~477 μs**|**<1% difference**

# model_forward_pass(layers|surrogate_total|exp_fru_total|h100_float16|vdr_vs_float)
6|2.84 ms|2.86 ms|~1.5 ms|~1.9× slower per token
12|5.69 ms|5.72 ms|~3.0 ms|~1.9× slower per token
24|11.38 ms|11.45 ms|~6.0 ms|~1.9× slower per token
# At 85-97% token reduction, net compute per prompt favors VDR from first prompt

# software_fallback_comparison(operation|host_cpu_latency|fru_latency|speedup)
exp(x) depth 10|~2 μs|~20 ns|100×
exp(x) depth 45|~10 μs|~90 ns|111×
sqrt(x) 100 digits|~5 μs|~28 ns|179×
ln(x) with reduction|~15 μs|~80 ns|188×
sin(x) depth 45|~12 μs|~160 ns|75×
cos(x) depth 45|~12 μs|~160 ns|75×
ζ(s) Borwein n=210|~200 μs|~2.9 μs|69×
Active-value unification|~5 μs|~8 ns|625×

# sfu_vs_fru(property|float_sfu|vdr_fru)
Purpose|Approximate transcendentals at float precision|Exact rational transcendentals at configurable depth
Method|Polynomial approximation / lookup-interpolation|Taylor/Newton recurrence producing exact partial sums
Precision|Fixed (23-bit FP32 mantissa)|Configurable (depth parameter controls digits)
Error bound|Documented ULP error (1-2 ULP)|Exact: R slot carries precise residual
Latency|~20-30 cycles (fixed)|Variable: 1 cycle (exp(0)) to ~225 cycles (sin depth 45)
Throughput per SM|~8 evals/cycle (shared)|64 evals/cycle (1 per QIU)
Power|~10 mW per SFU|~30 μW per FRU (active)
Die area|~0.1-0.3 mm² per SFU|~0.004 mm² per FRU
Platform-independent|No (vendor-specific polynomial)|Yes (integer arithmetic)

# limitations(id|limitation|detail)
LM1|Single-query latency unchanged|LLM forward pass dominates by 300-30,000×; FRU improvement invisible to user
LM2|Threshold configuration required|Per-context thresholds must be set correctly; too aggressive discards significant remainders; too conservative evaluates unnecessary terms
LM3|Reciprocal table limit k=64|Series needing k>64 terms require Newton reciprocal sub-loop (~32 extra cycles/term) or argument reduction
LM4|Generic tag limited to ~50 instructions|Exotic recurrences exceeding instruction BRAM budget need multi-pass host orchestration
LM5|Unused silicon for pure closed workloads|3.4% area paid by all QIUs regardless of FEVAL usage; mitigated by small absolute area (0.004 mm²/QIU)
LM6|Does not change training scale limitation|96 GB HBM capacity unchanged; model size limited to tens of millions of parameters for exact training

# reciprocal_table_exactness(k_range|exact_power_of_2|approx_plus_minus_1_ulp)
1-8|4 (k=1,2,4,8)|4
9-16|1 (k=16)|7
17-32|1 (k=32)|15
33-64|1 (k=64)|31
**Total**|**7**|**57**
# ±1 ULP error ≈ 2^(-336) ≈ 10^(-101.2); 10^66 below Planck length; tracked through R slot

# fru_power(component|static_uw|dynamic_uw_at_2ghz)
Recurrence registers|0.8|12
Reciprocal table|1.5|8
Convergence comparator|0.3|5
Loop controller|0.1|2
Interconnect|0.5|3
**Per-FRU total (idle)**|**3.2**|**0**
**Per-FRU total (active)**|**3.2**|**~30**
# Full chip worst case (all 5,120 active continuously): 170 mW = 0.042% of 410W TDP

# bram_budget(usage|words|pct_of_512)
Main microprogram|~30|5.9%
FRU tags 0x01-0x05 (fixed)|76|14.8%
FRU generic tag 0x06|≤50|≤9.8%
**Total max**|**~156**|**30.5%**
**Remaining**|**~356**|**69.5%**

# relationships(from|rel|to)
P1|enables|C1
P1|enables|C6
P2|implements|C6
P2|opposes|float mixed-precision
P3|constrains|C1
P4|constrains|C1
P5|enables|C9
P5|enables|CL4
P5|enables|CL8
C1|contains|C2
C1|contains|C3
C1|contains|C4
C1|adds|C5
C2|avoids_contention_with|QIU register file
C3|replaces|division-by-k with multiply-by-reciprocal
C4|enables|C6
C5|invokes|C1
C6|enables|C8
C6|enables|adaptive_depth_exp_softmax
C7|eliminates|reprojection stalls
C7|uses|C1
C8|uses|C5
C8|competes_with|surrogate softmax
C9|enables|CL4
C9|derives_from|P5
CL1|measures|C1
CL2|demonstrates|C8
CL3|constrains|C1
CL4|derives_from|C9
CL5|derives_from|C7
CL6|derives_from|C1
CL7|derives_from|CL6
CL8|derives_from|P5
CL9|supports|C8
CL10|contextualizes|CL9
LM1|constrains|C1
LM2|constrains|C4
LM3|constrains|C3
LM6|unchanged_from|VDR-22

# section_index(section|title|ids)
1|The Remainder Slot as Precision Control Surface|P1,P2,functional remainder definition
2|What the FRU Is|C1,C2,C3,C4,C5,CL1
3|Adaptive Precision in Inference|P3,C6,C8,inference_chain
4|Training with Continuous Resolution|C7,CL5,training tables
5|Prolog Unification Over Active Values|CL6,CL7,prolog_unification
6|Single-Query Performance|CL3,LM1,bottleneck ratio
7|Datacenter-Scale Throughput|P5,C9,CL4,CL8,concurrent_session_scaling
8|Exp-Softmax vs Surrogate|CL9,softmax_comparison
9|Updated Chip Specifications|chip_update
10|Limitations|LM1-LM6
11|Architectural Thesis in Silicon|P1,P2,P4
A|FRU Recurrence Detail|recurrences,adaptive_depth_exp_softmax
B|Reciprocal Table|C3,reciprocal_table_exactness
C|Convergence Thresholds|convergence_thresholds
D|FRU Power Analysis|fru_power
E|Adaptive Depth Distribution|adaptive_depth_exp_softmax
F|Training Remainder Simulation|training tables
G|Prolog Unification Completeness|prolog_unification
H|Instruction BRAM Budget|bram_budget
I|Host Round-Trip Elimination|host_roundtrips,concurrent_session_scaling
J|Functional Remainder Composition|composition rules
K|Die Partition Estimate|CL1
L|Software Fallback Comparison|software_fallback_comparison
M|SFU vs FRU|sfu_vs_fru
N|End-to-End Transformer Latency|transformer_latency,model_forward_pass

# decode_legend
format: pipe-delimited tables, ID-based cross-references
fru: Functional Remainder Unit — sequencer per QIU driving existing ALU through recurrence loops; ~496K transistors, ~0.004 mm²
feval: Opcode 0x35; variable-latency; evaluates functional remainder to requested depth using function tag
function_tags: 0x01 exp|0x02 sqrt|0x03 ln|0x04 sin|0x05 cos|0x06 generic (microcode)
reciprocal_table: 64 entries × 48B = 3KB; replaces division-by-k with multiply-by-reciprocal; ±1 ULP for non-power-of-2 k (≈10^(-101) error)
convergence: per-context configurable threshold in Q335 numerator magnitude; 0 = exact required
chip_delta: +3.4% area (581→601 mm²), +3.7% transistors (68→70.5B), +2.5% TDP (400→410W)
single_query: FRU invisible — LLM forward pass dominates primitives by 300-30,000×
datacenter: FRU eliminates host serialization; without FRU saturates at ~500K sessions; with FRU no saturation at 10M+
training: continuous resolution eliminates reprojection stalls; step time constant vs periodic spikes
unification: active-value Prolog unification 700-1,000× faster on-chip vs host round-trip
softmax: surrogate ~10ns vs exact exp ~56ns for 1,024 logits; <1% model-level difference; both exact sum-to-one
rel_types: enables|implements|opposes|constrains|contains|adds|avoids_contention_with|replaces|invokes|eliminates|uses|competes_with|derives_from|measures|demonstrates|supports|contextualizes|unchanged_from
+standalone: no cross-references to other compact docs
+one_new_instruction: FEVAL (opcode 0x35) added to VDR-22 ISA; all other primitives, IOSE declarations unchanged
