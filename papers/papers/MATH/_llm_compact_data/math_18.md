# CONCURRENCY TAX FROM SYSTEM STRUCTURE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: definitions → components → equations → graph → motifs → expert_discount → interventions → domains → predictions → relationships → sections

# definitions(id|symbol|name|definition|unit)
D1|G=(R,S,E)|Contention graph|Graph with shared resources R, processing streams S, edges E connecting streams to resources they require|—
D2|R={r₁..rₘ}|Resource set|Shared resources: anything serving one stream at a time or degrading under concurrent use|—
D3|S={s₁..sₙ}|Stream set|Concurrent processing streams competing for resources and pipeline|—
D4|E⊆S×R|Edge set|Connections between streams and required resources. Each edge annotated with h, f, c|—
D5|h(sᵢ,rⱼ)|Hold duration|Time stream sᵢ holds resource rⱼ per access|time
D6|f(sᵢ,rⱼ)|Access frequency|Rate stream sᵢ requires resource rⱼ|accesses/time
D7|c(sᵢ,rⱼ)|Criticality|Whether stream blocks when resource unavailable. 1=blocks, 0=can proceed|[0,1]
D8|ρ(rⱼ)|Resource utilization|Fraction of time resource occupied. ρ=Σᵢ f(sᵢ,rⱼ)×h(sᵢ,rⱼ)|[0,1+)
D9|W(rⱼ)|Expected wait time|Time stream waits when resource occupied. M/M/1: W=ρ/(μ(1−ρ))|time
D10|κ(sᵢ,sⱼ,rₖ)|Cascade coupling coefficient|Expected cascade promotions in sᵢ per unit of sⱼ's activity on shared resource rₖ|promotions/activity
D11|coord(rⱼ)|Coordination cost per access|Ops for access protocol: acquire, release, verify|ops/access
D12|deg(rⱼ)|Resource contention degree|Number of streams connected to resource rⱼ|count
D13|exp(sᵢ)|Stream exposure|Number of resources stream sᵢ requires|count
D14|overlap(sᵢ,sⱼ)|Contention overlap|Number of resources shared by streams sᵢ and sⱼ|count
D15|tax(sᵢ,G)|Concurrency tax|Total overhead for stream sᵢ in graph G. Sum of five components|ops+time
D16|δ(expert,novice,G)|Tax discount|Ratio expert tax / novice tax on same graph. δ<1|dimensionless
D17|n*|Optimal stream count|Stream count maximizing throughput: n*=argmax_n{n×work−tax(n,G)}|count

# principles(id|principle|rationale)
P1|Concurrency tax is derivable from system structure|Topology of shared resources and competing activities determines overhead. Computable before system runs, not just measurable after
P2|Tax is five distinct phenomena that sum|Contention, cascade, coordination, blocking, interleave. Each has different mechanism, scaling, intervention. Treating as undifferentiated "overhead" obscures structure
P3|Tax is a system property not a stream property|Each stream's tax depends on every other stream through shared resources. Adding a stream increases every other stream's tax
P4|Marginal tax of (k+1)th stream is generally superlinear|New stream contends with k existing streams, generates cascade coupling with k, adds coordination for k interactions. Total increase grows with existing stream count
P5|Tax dominates at high concurrency|At some stream count, tax per stream exceeds isolated cost. Beyond this, adding streams decreases throughput
P6|Diagnosing which component dominates determines which intervention works|Contention→replication. Cascade→isolation. Coordination→simplification. Blocking→async. Interleave→scheduling policy

# components(id|name|mechanism|cost_type|op_count_change|duration_change|pipeline_state|scales_with|intervention)
TC1|Contention|Stream needs occupied resource; waits|Time budget consumed waiting|None (same ops)|Inflated by wait|Occupied (waiting)|ρ nonlinear, diverges as ρ→1|Resource replication
TC2|Cascade|Competing stream's activity invalidates dissolved processing|Ops added from promotions|Increased (promoted elements cost ops)|Unchanged per op|Active (re-processing)|κ × activity rate × inventory size|Isolation; wider envelopes
TC3|Coordination|Managing concurrent access protocols|Ops for lock/handoff/protocol|Increased (coordination ops added)|Unchanged per op|Active (overhead)|Resources × frequency × protocol cost|Protocol simplification
TC4|Blocking|Pipeline idle waiting for critical resource|Dead time, zero ops|None (no ops during block)|N/A|Idle (dead)|Critical resource utilization|Asynchronous decoupling
TC5|Interleave|Choosing which stream to service next|Ops for scheduling decision|Increased (decision ops)|Unchanged per op|Active (meta-decision)|Ready stream count × decision complexity|Scheduling policy

# equations(id|component|formula|variables)
EQ1|Resource utilization|ρ(rⱼ) = Σᵢ f(sᵢ,rⱼ) × h(sᵢ,rⱼ)|f=access frequency, h=hold duration, sum over connected streams
EQ2|Wait time (M/M/1)|W(rⱼ) = ρ(rⱼ) / (μⱼ × (1−ρ(rⱼ)))|ρ=utilization, μ=service rate. Diverges as ρ→1
EQ3|Contention|contention(sᵢ,G) = Σⱼ f(sᵢ,rⱼ) × W(rⱼ)|Frequency-weighted wait across all resources stream uses
EQ4|Cascade|cascade(sᵢ,G) = Σⱼ≠ᵢ Σₖ κ(sᵢ,sⱼ,rₖ) × activity(sⱼ,rₖ) × recovery_cost(sᵢ)|Triple sum: every other stream through every shared resource, weighted by coupling
EQ5|Coordination|coordination(sᵢ,G) = Σⱼ f(sᵢ,rⱼ) × coord(rⱼ)|Access frequency × protocol cost per resource
EQ6|Blocking|blocking(sᵢ,G) = Σⱼ f(sᵢ,rⱼ) × c(sᵢ,rⱼ) × W(rⱼ)|Like contention but filtered by criticality. Dead time not inflated duration
EQ7|Interleave|interleave(sᵢ,G) = preemption_rate(sᵢ,G) × interleave_cost(active_streams(G))|Interruption frequency × decision cost
EQ8|Total tax|tax(sᵢ,G) = contention + cascade + coordination + blocking + interleave|Sum of five components
EQ9|In situ cost|cost_insitu(sᵢ) = cost_isolated(sᵢ) + tax(sᵢ,G)|Isolated cost + total tax
EQ10|System cost|cost_total(G) = Σᵢ cost_isolated(sᵢ) + Σᵢ tax(sᵢ,G)|Sum across all streams
EQ11|Tax discount|δ(expert,novice,G) = tax(expert,G) / tax(novice,G)|Ratio < 1
EQ12|Optimal streams|n* = argmax_n{n × work_isolated − tax_total(n,G)}|Where marginal tax equals marginal work
EQ13|Brooks crossover|n* = (1 + √(1 + 2/c_edge)) where c_edge = coordination cost per pairwise edge|Complete graph, coordination only. Lower bound on tax

# motifs(id|name|structure|degree|contention_scaling|total_scaling|examples)
MT1|Star|One central resource connected to all n streams|Central: n|O(n/(1−nf̄h̄)); diverges at saturation|Dominated by contention; steep growth, hard ceiling|Single DB pool; single CI pipeline; surgeon's visual attention
MT2|Chain|Sequential pairwise sharing; stream i shares with i+1|All: 2|O(1) per link; delays propagate|Linear with length; propagation adds latency|Pipeline architectures; assembly lines; sequential approvals
MT3|Complete|Every stream shares resource with every other|Near n|O(n²) aggregate|Quadratic; maximum possible tax|Open-plan offices; shared-everything SMP; team meetings; shared mutable state
MT4|Partitioned|Groups of size k; sharing within groups only|k per group|O(k/(1−kf̄h̄)) per group; groups independent|Bounded by k not n; scales by adding groups|NUMA domains; pod-based teams; microservices
MT5|Hierarchical|Tiers: local (few streams), global (many)|Local: 2-4; global: n|O(log n) typical; O(n) for global access|Logarithmic common case; periodic global penalties|Cache hierarchy L1/L2/L3; org hierarchy; federated systems
MT6|Ring|Each stream shares with two neighbors; no global resource|All: 2|O(1) per link; no global bottleneck|Linear distributed; no single bottleneck|Token ring; circular assembly; round-robin responsibilities
MT7|Hybrid star-partition|Multiple stars serving partitions; stars share global resource|Star: k; global: partition count|Two-tier: fast within partition, slow across|Fast local + slow global|Replicated DB with coordinator; multi-team org; multi-socket CPU

# expert_discount(id|component|novice_cost|expert_cost|discount_δ|dissolution_mechanism|dissolves?)
ED1|Contention|W (wait time)|W (same)|~1.0|Waiting is structural, not a skill|No
ED2|Cascade (cognitive)|15-25 min recovery per interruption|2-5 min recovery|~0.15-0.25|Wider validity envelopes; dissolution under varied conditions including interruptions|Yes
ED3|Cascade (CPU)|~800 cache misses × 200 cycles|~200 misses × 200 cycles|~0.25|Optimized memory patterns; tighter working sets; cache-aware algorithms|Yes
ED4|Coordination (surgical)|5 ops per instrument handoff|1 op (anticipate-extend-accept)|~0.2|Team-specific dissolution; shared mental model; implicit protocols|Yes
ED5|Coordination (software)|3-5 ops per review cycle|1-2 ops|~0.3-0.5|Shared conventions dissolve; codebase familiarity|Yes
ED6|Blocking|W (wait time)|W (may use wait productively)|~0.8-1.0|Expert switches to useful work during block without cascade|Minimally
ED7|Interleave (cognitive)|3-5 ops per switch decision|0-1 ops|~0.1-0.2|Priority patterns dissolve; urgency assessment becomes structural|Yes
ED8|Interleave (CPU)|O(log n) per decision|O(1) achievable|Variable|Algorithmic: O(1) scheduler is pre-computed scheduling|Engineering, not practice

# interventions(id|name|graph_transformation|target_component|tax_change|when_to_apply)
IV1|Resource replication|Split high-degree node into k lower-degree nodes|Contention+Blocking|ρ_new=ρ_old/k; W drops more than proportionally (queueing convexity)|When single resource ρ>0.7 and contention dominates
IV2|Resource upgrade|Reduce h(sᵢ,rⱼ) for all edges (faster resource)|Contention+Blocking|ρ_new=ρ_old×(h_new/h_old)|When hold duration drives utilization
IV3|Stream isolation|Remove cascade coupling edges; separate context spaces|Cascade|κ→0 on isolated edges; cascade→0 for those resources|When cascade dominates; dissolved processing frequently broken
IV4|Protocol simplification|Reduce coord(rⱼ) on resource edges|Coordination|Proportional to coord reduction × frequency|When coordination dominates and protocol has unnecessary steps
IV5|Asynchronous decoupling|Change criticality c from 1→0; add buffer/queue|Blocking|blocking→0 on decoupled edges; interleave/cascade may increase modestly|When blocking dominates and stream can proceed without resource
IV6|Scheduling policy|Replace deliberative decisions with structural rules|Interleave|interleave_cost→O(1)|When interleave frequent and decision pattern regular
IV7|Stream reduction|Remove streams from graph|All|Proportional reduction; superlinear benefit in high-contention topologies|When past n* (tax exceeds useful work)
IV8|Topology restructuring|Transform motif (e.g., complete→partitioned)|All|Changes scaling law|When topology fundamentally mismatched to workload
IV9|Cascade widening|Widen validity envelopes through varied training (no graph change)|Cascade|Reduces κ on existing edges|When cascade dominates and processors have narrow envelopes

# human_processor_streams(id|stream|resources_required|hold_duration|cascade_coupling_κ|typical_tax)
HS1|Primary development task|Working memory (hours), visual attention (hours), codebase (hours)|Hours|N/A (is primary)|0 (isolated work)
HS2|Simple Slack message|Visual attention (brief), working memory (brief, no context change)|10-30s|~0.1 (doesn't evict primary)|30-60s
HS3|Complex Slack message|Visual attention (extended), working memory (full load, different context)|2-10min|~0.9 (evicts primary context)|20-30min (2-5 direct + 15-25 cascade)
HS4|Code review request|Visual attention, working memory (full load), codebase (different branch)|15-45min|~0.95 (complete context switch)|45-90min (review + recovery)
HS5|Scheduled meeting|Visual attention, working memory, communication bandwidth|30-60min|~0.9 (displaces development context)|60-120min (meeting + cascade recovery)
HS6|Unscheduled interruption|Visual attention (immediate), working memory (forced partial load)|1-5min|~0.7 (forced attention shift)|15-30min (interruption + cascade)
HS7|Production incident|All resources (immediate full priority)|30min-hours|~1.0 (complete context evacuation)|1-4 hours (response + full recovery)
HS8|Background anxiety|Working memory (persistent partial occupation)|Hours-days|~0.4 (persistent low-grade)|10-30% continuous throughput reduction

# domain_tax_profiles(id|domain|dominant|second|contention%|cascade%|coordination%|blocking%|interleave%|tax_as_%budget)
DP1|Multi-threaded software (high contention)|Contention|Blocking|40|20|15|20|5|30-60%
DP2|Multi-process CPU (cache-sensitive)|Cascade|Contention|20|45|5|10|20|20-50%
DP3|Developer (open office)|Cascade|Coordination|5|45|25|10|15|40-70%
DP4|Developer (remote async)|Blocking|Cascade|5|20|20|40|15|20-40%
DP5|Surgical team (routine)|Coordination|Contention|15|15|45|15|10|15-30%
DP6|Surgical team (complex)|Cascade|Coordination|10|40|25|5|20|30-60%
DP7|ATC (moderate)|Interleave|Coordination|10|15|25|10|40|20-40%
DP8|ATC (high load)|Contention|Cascade|35|25|15|5|20|50-80%
DP9|Manufacturing (assembly)|Blocking|Contention|25|5|15|45|10|15-35%
DP10|Emergency department|Cascade|Interleave|10|35|20|10|25|40-70%

# brooks_law(id|claim|mechanism)
BL1|For complete graph topology, coordination grows O(n²) with team size|Edges = n(n−1)/2. Each edge costs c_edge coordination units
BL2|Crossover at n* where marginal coordination tax exceeds marginal isolated work|n* = (1+√(1+2/c_edge)). Lower c_edge raises n*
BL3|Including contention and cascade lowers n* further|Table K shows coordination-only; real teams also contend on codebase, CI, reviews + cascade from interruptions
BL4|Example: c_edge=0.10 → n*≈11. At n=12, adding member decreases throughput|Net throughput peaks then declines. Classic Brooks's Law derived from graph structure

# organizational_test_case(id|resource|degree|hold_time|frequency|utilization|predicted_wait)
OT1|CI pipeline|6 (team size)|12 min/build|30 builds/day across 10h|ρ=0.6|~18 min/build
OT2|Code review pool|6|2h to first review|2 PRs/day per dev|—|~2h blocking per PR
OT3|Team lead attention|6|5-30min/decision|2-8 requests/day per dev|—|Variable queue
OT4|Shared codebase|6|Hours (branch lifetime)|1-5 merges/day per dev|—|Merge conflicts intermittent
OT5|Meeting time|6|30-60min|2-4/day per person|—|1.5-2h/day coordination + cascade recovery
# Predicted total tax per developer per day: 4-7 hours. Leaves 3-6 hours productive. Matches industry measurements of 3-5 hours focused coding per 8-10h workday

# predictions(id|prediction|testable_by)
PR1|Tax predictability — accuracy proportional to annotation completeness|Build graph from profiling, predict, measure, compare. <20% error with full annotation
PR2|Intervention specificity — targeting one component reduces that component, not others|Measure all five before/after single intervention. Non-targeted change <20% of targeted
PR3|Motif-determined scaling — marginal tax follows topology's scaling law|Add streams incrementally, measure. Star: superlinear. Partitioned: constant per group. Hierarchical: logarithmic
PR4|Expert discount components — cascade and interleave dissolve; contention and blocking don't|Compare expert/novice on same graph. δ_cascade,δ_interleave << 1; δ_contention,δ_blocking ≈ 1
PR5|Brooks's Law derivation — crossover at computable n* where marginal tax > marginal work|Measure team throughput at different sizes. Peak at predicted n* then decline
PR6|Optimal concurrency — n* exists for any graph where throughput peaks then declines|Run at varying stream counts. Peak at predicted n*

# open_problems(id|problem|description)
OP1|Dynamic contention graphs|Streams start/end, requirements change, graph evolves. Time-varying tax computation needed
OP2|Degrading resources|Many resources degrade continuously under load rather than blocking. Extend from binary exclusion to continuous degradation functions
OP3|Nested contention|Developer has cognitive contention (internal) + organizational contention (external). Coupled graphs at different levels interact
OP4|Component interaction|High contention increases cascade probability; high cascade increases interleave cost. Second-order terms would improve prediction at high load
OP5|Tax measurement standardization|Define operational procedures for measuring each component per domain for cross-study comparison

# cross_level(id|level|processor|pipeline|streams|resources|budget|dominant_component)
CL1|Instruction|CPU core|Instruction pipeline|Pipeline stages + OoO windows|Execution units, registers, load/store|Pipeline depth|Contention + Cascade (branch mispredict)
CL2|Process|CPU+cache|Scheduling quantum|Concurrent processes|Cache hierarchy, memory bus, I/O|Time slice|Cascade (cache) + Interleave (scheduler)
CL3|Application|Developer|Conscious attention|Concurrent tasks in session|Working memory, visual attention, motor|Work session (hours)|Cascade (working memory)
CL4|Team|Team lead|Decision bandwidth|Concurrent members' work|Codebase, CI, review pool, lead attention|Sprint/iteration|Coordination + Blocking
CL5|Organization|Executive|Strategic bandwidth|Concurrent departments/projects|Budget, headcount, infrastructure|Quarter/year|Coordination + Interleave

# relationships(from|rel|to)
P1|grounds|D1-D17
P2|decomposes|TC1-TC5
P3|derives_from|D1
P4|derives_from|EQ1,EQ2 nonlinearity
P5|produces|D17
P6|enables|IV1-IV9
D1|determines|EQ1-EQ10
D8|drives|EQ2 (diverges as ρ→1)
D10|determines|EQ4
TC1|responds_to|IV1,IV2
TC2|responds_to|IV3,IV9
TC3|responds_to|IV4
TC4|responds_to|IV5
TC5|responds_to|IV6
ED2|derives_from|wider validity envelopes (MATH-16)
ED4|derives_from|team coordination dissolution
BL1|derived_from|MT3 (complete graph) + EQ5

# section_index(section|title|ids)
1|The Phenomenon|P1,P2
2|The Five Components|TC1-TC5,P2
3|The Contention Graph|D1-D14
4|Deriving Tax from Graph|EQ1-EQ7
5|The Concurrency Tax Equation|EQ8-EQ10,P3,P4,P5,P6
6|Architectural Motifs|MT1-MT7
7|Human and Organizational Processors|HS1-HS8,DP1-DP10,OT1-OT5
8|The Expert Tax Discount|ED1-ED8,D16
9|Interventions as Graph Transformations|IV1-IV9
10|Computational Test Case|CL1-CL2
11|Organizational Test Case|OT1-OT5,BL1-BL4
12|Predictions|PR1-PR6
13|Scope and Open Problems|OP1-OP5

# decode_legend
contention_graph: G=(R,S,E) with edge annotations h (hold), f (frequency), c (criticality)
five_components: contention (wait for occupied resource) + cascade (dissolved processing broken) + coordination (protocol overhead) + blocking (dead pipeline) + interleave (scheduling decisions)
total_tax: sum of five components. In situ = isolated + tax. System = Σ isolated + Σ tax
utilization_divergence: W=ρ/(μ(1−ρ)). Halving ρ more than halves W (queueing convexity). Key to replication benefit
expert_discount: cascade and interleave dissolve (δ<<1). Contention and blocking are structural (δ≈1). Coordination dissolves with team experience
motif_scaling: star=O(n/(1−nfh)), chain=O(n), complete=O(n²), partitioned=O(k), hierarchical=O(log n)
brooks_derivation: complete graph + coordination cost per edge → n*=(1+√(1+2/c_edge)). Adding members past n* decreases throughput
human_cascade_dominance: complex Slack (20-30min), code review (45-90min), meeting (60-120min), incident (1-4h). Direct cost small; cascade recovery dominates by order of magnitude
id_prefixes: D=definition|P=principle|TC=tax_component|EQ=equation|MT=motif|ED=expert_discount|IV=intervention|HS=human_stream|DP=domain_profile|BL=brooks_law|OT=org_test|PR=prediction|OP=open_problem|CL=cross_level
spec_counts: 17 definitions|5 tax components|13 equations|7 motifs|8 expert discount entries|9 interventions|8 human stream types|10 domain profiles|6 predictions|5 open problems|5 cross-level mappings
