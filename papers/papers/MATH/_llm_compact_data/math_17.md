
# PROCESSING ENTROPY AS A METRIC SPACE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: concepts → definitions → distances → matrix → trajectories → gaps → clusters → task_topology → test_cases → open_problems → claims → relationships → sections → decode_legend

# concepts(id|name|category|definition)
C1|Processing entropy profile|core|Vector H(p) = (Hp(t₁),...,Hp(tₘ)) of op counts processor p requires for each task in task set T; point in m-dimensional task space
C2|Op|primitive|One irreducible transformation by one processor; diagnostic question, mirror glance, cache lookup, line of code read
C3|Dissolved (Hp=0)|state|Task handled structurally without pipeline cost; doesn't count against time budget; what makes expertise powerful
C4|Undefined (Hp)|state|Task outside processor's domain; not zero (dissolved) nor high (expensive); processor cannot perform at any op count
C5|Shared domain T(p,q)|core|Set of tasks where both processors have defined Hp; where comparison is meaningful; size relative to T measures domain overlap
C6|Processing entropy matrix H|core|Processors as rows, tasks as columns, H[i,j] = Hpᵢ(tⱼ); rows are processor profiles, columns are task cost vectors; single unifying object
C7|Skill gap vector|core|g(p,r) = H(p) − H(r); per-task cost difference from reference; has magnitude (total size), direction (which tasks), shape (concentrated vs distributed)
C8|Trajectory|core|Path H(p,t₀),...,H(p,tₖ) through profile space over time; complete history of expertise development as curve
C9|Transfer affinity|core|Degree to which dissolution of tᵢ reduces first-encounter cost of tⱼ; may differ from processing entropy distance; defines leverage in training
C10|Discrimination power|core|disc(t) = var(Hp₁(t),...,Hpₙ(t)); high variance = task effectively separates skill levels; low = universally easy or universally hard
C11|Task topology|core|Shape of domain as processors experience it; defined by task distances, not conventional taxonomy; clusters by processing structure not subject matter
C12|Skill factors|core|Columns of U in factorization H ≈ U×V; underlying dimensions of expertise; reduce profile space from m to k dimensions
C13|Task cost column|dual|H(t) = (Hp₁(t),...,Hpₙ(t)); vector in n-dimensional processor space; dual of processor profile

# formal_definitions(id|symbol|name|definition|unit)
FD1|T|Task set|Finite collection {t₁,...,tₘ} of elements processor might handle|—
FD2|P|Processor set|Finite collection {p₁,...,pₙ} of processors under comparison|—
FD3|Hp(tᵢ)|Processing entropy|Op count processor p requires for task tᵢ; zero if dissolved; undefined if outside domain|ops
FD4|H(p)|Profile vector|(Hp(t₁),...,Hp(tₘ)) for processor p across T|ops per component
FD5|H(t)|Cost column|(Hp₁(t),...,Hpₙ(t)) for task t across P|ops per component
FD6|H[i,j]|Matrix entry|Hpᵢ(tⱼ); processors as rows, tasks as columns|ops
FD7|T(p,q)|Shared domain|{t ∈ T : Hp(t) defined ∧ Hq(t) defined}|subset of T
FD8|T*|Universal shared domain|∩ᵢⱼ T(pᵢ,pⱼ) across all processor pairs|subset of T
FD9|disc(t)|Discrimination power|var(Hp₁(t),...,Hpₙ(t))|ops²
FD10|g(p,r)|Skill gap vector|H(p) − H(r)|ops per component (signed)
FD11|ρ(p,r,t)|Gap closure rate|−d|g(p,r)|/dt|ops/time
FD12|v(p,t)|Dissolution velocity|dH(p)/dt; negative = dissolving, positive = regression|ops/time per component
FD13|η|Trajectory efficiency|displacement / path length; 1 = direct, <1 = cascades/backtracking|dimensionless [0,1]
FD14|H ≈ U×V|Matrix factorization|U(n×k) = processor positions in skill factor space; V(k×m) = task loadings on factors|ops
FD15|k|Effective dimensionality|Rank of H or retained factors; few factors explain most variation|count
FD16|aff(tᵢ,tⱼ)|Transfer affinity|Degree dissolution of tᵢ reduces first-encounter cost of tⱼ|ops reduced

# distances(id|name|formula|measures|best_for|sensitivity)
D1|Euclidean (L²)|√(Σᵢ (Hp(tᵢ)−Hq(tᵢ))²)|Overall profile similarity|General similarity; clustering|Large single-task differences (squared)
D2|Manhattan (L¹)|Σᵢ |Hp(tᵢ)−Hq(tᵢ)||Total op count difference|Total cost comparison; resource estimation|Uniform to all differences
D3|Chebyshev (L∞)|maxᵢ |Hp(tᵢ)−Hq(tᵢ)||Maximum single-task difference|Bottleneck identification; certification|Only single largest difference
D4|Weighted L²|√(Σᵢ wᵢ(Hp(tᵢ)−Hq(tᵢ))²)|Operationally weighted similarity|Operational staffing; risk assessment|High-weight task differences

# metric_axioms(id|axiom|holds_for_all|note)
MA1|Non-negativity: d(p,q) ≥ 0|All Lp norms and weighted|Trivially from squares/absolutes/max
MA2|Identity of indiscernibles: d=0 iff H(p)=H(q)|All|Identical profiles = identical cost on every task
MA3|Symmetry: d(p,q)=d(q,p)|All|Absolute differences and squares are symmetric
MA4|Triangle inequality: d(p,r) ≤ d(p,q)+d(q,r)|All over common task set T*|Minkowski inequality; requires care when shared domains differ

# shared_domain_resolution(id|approach|method|tradeoff)
SD1|Common-ground|Restrict all comparisons to T* = ∩ T(pᵢ,pⱼ)|All metric axioms hold automatically; information loss on excluded tasks
SD2|Pairwise|Compute d over T(p,q) per pair, normalized by size|Preserves all information; triangle inequality holds only under nesting or when undefined rare

# matrix_properties(id|property|when_expected|implication)
MP1|Low rank (k << min(n,m))|Processors share training tradition; tasks share structural patterns|Few skill factors explain most variation; profile space has low effective dimensionality
MP2|Full rank|Highly heterogeneous processors; structurally independent tasks|Each task measures something unique; no compression possible
MP3|Block diagonal|Distinct subpopulations with non-overlapping domains|Genuinely different fields; cross-block comparison meaningless
MP4|Banded|Tasks and processors orderable along single difficulty/skill continuum|Simple linear skill progression; one-dimensional expertise
MP5|Sparse (many zeros)|Mature population; most routine dissolved|High expertise; focus on remaining non-zero entries
MP6|Dense (few zeros)|Immature population or extremely broad task set|Low dissolution; most tasks still cost ops

# gap_shapes(id|shape|distribution|prescription)
GS1|Concentrated spike|1-3 tasks >80% of magnitude|Targeted: dissolve specific tasks
GS2|Distributed flat|No task >10% of magnitude|General: broad experience needed
GS3|Bimodal|Two distinct groups (near-zero and moderate)|Hybrid: dissolved set + coherent skill area needing development
GS4|Staircase|Graduated, evenly spread|Sequential: dissolve largest gaps first
GS5|Single outlier|One task >90% of magnitude|Highly targeted: one specific task
GS6|Inverted (strength)|Negative components dominate; processor outperforms reference|Not gap but strength; reference may learn from processor

# trajectory_properties(id|property|formula|interpretation)
TP1|Dissolution velocity magnitude|√(Σᵢ (dHp(tᵢ)/dt)²)|High = rapid change; low = plateau or stability
TP2|Velocity direction|v/|v| (unit vector)|Where change is concentrated; should align with training priorities
TP3|Trajectory efficiency|displacement / path length|Near 1 = direct; <1 = cascades/backtracking; 0.7-1.0 healthy
TP4|Mean component velocity|(1/m) Σᵢ dHp(tᵢ)/dt|Negative = net dissolution; zero = plateau; positive = regression
TP5|Velocity variance|var across components|High = specialist trajectory; low = generalist trajectory
TP6|Cascade signature|Sharp positive spike in |v| followed by recovery|Dissolved elements promoted; recovery is restabilization
TP7|Plateau detection||v| < ε for extended period|Expert plateau (desirable) or development plateau (needs intervention)
TP8|Convergence rate to reference|−d(d(p,r))/dt|Positive = closing gap; negative = falling behind

# cluster_types(id|type|structure|detection|interpretation)
CL1|Skill level (radial)|Concentric shells at different distances from origin|Cluster by d₂(p, origin)|Similar total dissolution levels (novice/intermediate/expert)
CL2|Specialization (angular)|Wedges at similar distance but different directions|Normalize to unit length, cluster|Similar patterns but possibly different amounts
CL3|Combined|Shells subdivided into wedges|Two-stage: distance then direction|Full skill landscape: level and specialty
CL4|Transition zone|Sparse region between clusters|Density-based (DBSCAN)|Processors pass through quickly; unstable intermediate
CL5|Attractor|Dense point trajectories converge toward|High-density regions|Natural resting states; dissolution-demand equilibrium
CL6|Bifurcation point|Point where trajectories diverge|High trajectory variance|Decision points; specialization commitment
CL7|Outlier|Far from all clusters|Distance to nearest centroid exceeds threshold|Unusual: exceptional, narrow, degraded, or different tradition

# task_topology_properties(id|property|definition|application)
TT1|Task cluster|Tasks with small pairwise distance; natural difficulty classes|Curriculum design: cluster-aligned modules
TT2|Discriminating task|High cost variance across processors|Assessment design: include for maximum separation
TT3|Universal easy|All processors low cost; near origin|Exclude from assessment; low training priority
TT4|Universal hard|All processors high cost|Research target: why hasn't this dissolved?
TT5|Transfer neighborhood|Connected by high transfer affinity|Curriculum leverage: dissolving one accelerates others
TT6|Bridge task|High betweenness centrality; connects distant clusters|Strategic target: unlocks cross-domain skill transfer
TT7|Isolated task|Far from all others; unique processing chain|Must train independently; no transfer benefit
TT8|Hub task|High degree centrality; central in task graph|Highest-leverage target: dissolving accelerates many neighbors

# transfer_affinity_types(id|type|definition|implication)
TA1|Symmetric|aff(tᵢ,tⱼ) = aff(tⱼ,tᵢ)|Shared processing chain; dissolution order doesn't matter
TA2|Asymmetric|aff(tᵢ,tⱼ) ≠ aff(tⱼ,tᵢ)|tᵢ contains tⱼ's chain as sub-chain; tᵢ is more general skill
TA3|Zero|No effect on each other|Independent processing chains
TA4|Negative|Dissolving tᵢ increases cost of tⱼ|Conflicting chains; specialist dissolution can narrow generalist capability
TA5|Transitive|aff chains: tᵢ→tⱼ→tₖ implies tᵢ→tₖ|Connected transfer neighborhoods; exploit transitivity in curriculum
TA6|Non-transitive|tᵢ→tⱼ and tⱼ→tₖ but not tᵢ→tₖ|Hub tasks: tⱼ bridges unrelated skill areas

# profile_types(id|type|distance_from_origin|angular_distribution|signature)
PT1|Complete novice|Maximum (far)|Uniform; no task dissolved|All components high
PT2|Developing generalist|Moderate|Broad; many partially dissolved|Moving toward origin along many axes
PT3|Developing specialist|Moderate overall; near origin on specialty|Concentrated; specialty dissolved, others high|Elongated profile
PT4|Expert generalist|Near origin|Broad near origin; most dissolved|Few high-cost outliers
PT5|Expert specialist|Near origin on specialty; moderate elsewhere|Concentrated near origin on specialty|Very near in specialty, moderate elsewhere
PT6|Degraded expert|Moderate (regression)|Previously near origin; some axes moved out|Cascade signature
PT7|Polymath|Near origin across multiple specialization wedges|Broad multi-specialty coverage|Near origin in multiple orthogonal dimensions
PT8|Savant|Extreme asymmetry; zero some, maximum others|Maximally concentrated|Maximum profile asymmetry

# test_cases(id|domain|task_set|processor_set|op_measurement|key_findings)
TC1|Software engineering|Bug types by root cause on specific codebase|Development team|IDE telemetry, VCS timestamps, screen recording|Matrix rank ~4 (architecture understanding, tool proficiency, language knowledge, domain logic); race condition bugs highest discrimination; build system is hub task for transfer
TC2|Computation (cache)|Memory access patterns (sequential, strided, random, pointer-chasing)|Cache configurations (associativity × capacity × replacement × prefetch)|Hardware performance counters (cycles/access)|Matrix rank ~3 (capacity tier, associativity class, prefetch aggressiveness); pointer-chasing highest discrimination; sequential→strided high transfer, sequential→random low

# maturity_observation
# Conventional taxonomy (organ system, subsystem, weather type) may not match processing topology
# Tasks cluster by processing structure not subject matter: straightforward presentations cluster across organ systems
# Training organized by processing pattern may produce faster dissolution than training by conventional category

# open_problems(id|problem|description)
OP1|Effective dimensionality stability|Is matrix rank stable within domain as processors/tasks added? If so, dimensionality is domain property
OP2|Optimal assessment design|Minimal task subset maximally discriminating; accounting for redundancy and complementarity among tasks
OP3|Trajectory prediction|If dissolution follows known family (power law, exponential), trajectory predictable from position + velocity + curve params; cascade disrupts prediction
OP4|Transfer affinity formalization|Derive from processing chain analysis: tasks sharing reduction sub-chains have high transfer; currently defined but not derived from primitives
OP5|Dynamic task sets|When T changes (new bugs, diseases, scenarios), profile space changes dimensionality; how metric transforms under task set evolution
OP6|Cross-domain comparison|Can profiles from different domains be compared if skill factors are structurally analogous? Distance in skill factor space rather than task space

# claims(id|claim|type|depends_on)
CL1|Processing entropy profile space is a metric space under L², L¹, L∞, and weighted distances|derivation|MA1-MA4,FD4,D1-D4
CL2|Expertise has a geometry: skill gaps are distances with direction, learning is trajectory, clusters are formally identifiable|derivation|C1,C7,C8,CL1
CL3|Two processors with identical profiles are interchangeable on the task set|derivation|MA2
CL4|Task topology reflects processing structure not conventional subject-matter taxonomy|observation|C11,TT1
CL5|Tasks clustered by processing entropy distance may not align with conventional domain categories; training organized by processing pattern may outperform conventional organization|derivation|C11,TT1,C9
CL6|Matrix rank reveals how many independent dimensions of expertise exist; low rank expected when processors share training tradition|derivation|C6,MP1,C12
CL7|High-leverage tasks (hubs in transfer affinity graph) should be prioritized in training for maximum dissolution acceleration|derivation|C9,TT8
CL8|Gap profile shape determines training strategy more precisely than gap magnitude alone|derivation|C7,GS1-GS6
CL9|Cascade in profile space = sudden positive velocity spike followed by recovery; cascade count from prior work maps to simultaneous component regressions|derivation|TP6
CL10|All formal objects (profiles, distances, matrices, trajectories, gaps, clusters, task topology) are measurable in existing systems with existing instrumentation|observation|TC1,TC2
CL11|Discrimination power identifies minimal assessment battery: smallest task set maximally separating processor population|derivation|C10,OP2

# rules(id|rule|rationale)
R1|Use common-ground approach (T*) when comparing processors within single domain|All metric axioms hold automatically; natural when all processors share task domain
R2|Choice of distance determines what "close" means: Euclidean for overall similarity, Manhattan for total cost, Chebyshev for bottleneck, weighted for operational relevance|Each tells different true story about same pair
R3|Three-category distinction (zero/positive/undefined) must be preserved in profiles|Zero ≠ undefined: expertise ≠ impossibility; high ≠ undefined: difficulty ≠ impossibility
R4|Identify hub tasks in transfer affinity graph and prioritize in training|Maximum dissolution leverage; dissolving hub accelerates many neighbors
R5|Diagnose gap shape before prescribing training|Concentrated → targeted; distributed → general; same magnitude can need entirely different programs
R6|Track trajectory efficiency to detect cascades and plateaus|η < 0.5 suggests frequent disruption; |v| ≈ 0 for extended period needs intervention vs recognition of expert plateau

# relationships(from|rel|to)
C1|point_in|metric_space
C1|row_of|C6
C5|enables|comparison
C6|contains|C1,C13
C6|factored_as|C12
C7|computed_from|C1
C8|path_through|C1_space
C9|defines|TT5,TT6,TT8
C10|identifies|TT2
C11|induced_by|D1-D4_on_tasks
C12|reduces|C6_dimensionality
C13|column_of|C6
D1|satisfies|MA1-MA4
D2|satisfies|MA1-MA4
D3|satisfies|MA1-MA4
D4|satisfies|MA1-MA4
GS1|determines|targeted_training
GS2|determines|general_training
TP6|maps_to|cascade_from_prior_work
CL1|enables|CL2
CL4|motivates|CL5
CL6|derived_from|MP1
CL8|derived_from|GS1-GS6
CL10|grounded_by|TC1,TC2

# section_index(section|title|ids)
1|The Question|C1,C2,C3,C4
2|The Processing Entropy Profile|C1,FD3,FD4,R3
3|Shared Domain and Comparable Profiles|C5,FD7,FD8,SD1,SD2,R1
4|Distance Between Processors|D1-D4,MA1-MA4,CL1,R2
5|Distance Between Tasks|C13,FD5,C10,FD9
6|The Processing Entropy Matrix|C6,FD6,FD14,FD15,C12,MP1-MP6,CL6
7|Trajectories|C8,FD12,FD13,TP1-TP8,R6
8|Skill Gap as Geometric Object|C7,FD10,FD11,GS1-GS6,CL8,R5
9|Clusters|CL1-CL7
10|Task Topology|C11,TT1-TT8,C9,TA1-TA6,CL4,CL5,CL7,R4
11|Computational Test Case|TC1,TC2,CL10
12|Scope and Open Problems|OP1-OP6

# decode_legend
primitive: op = one irreducible transformation by one processor
profile: H(p) = vector of op counts across task set; point in m-dimensional space
hp_categories: zero(dissolved)|positive(active)|undefined(outside domain) — three distinct categories, not continuous
distances: L²(Euclidean)|L¹(Manhattan)|L∞(Chebyshev)|weighted_L² — all satisfy metric axioms over common task set
shared_domain: common-ground(T*=intersection, all axioms hold)|pairwise(per-pair, normalized, triangle inequality conditional)
matrix: H[i,j] = Hpᵢ(tⱼ); rows=processors, columns=tasks; rank reveals effective dimensionality
factorization: H ≈ U(n×k)×V(k×m); U=processor positions in k skill factors; V=task loadings on factors
trajectory: path through profile space; velocity=dH/dt; efficiency=displacement/path_length
gap: vector g=H(p)−H(r); shapes: concentrated|distributed|bimodal|staircase|outlier|inverted
clusters: radial(skill_level)|angular(specialization)|combined|transition|attractor|bifurcation|outlier
task_topology: clusters by processing structure not subject matter; hub/bridge/isolated tasks by graph centrality
transfer_affinity: symmetric|asymmetric|zero|negative|transitive|non-transitive; defines training leverage
profile_types: novice|developing_generalist|developing_specialist|expert_generalist|expert_specialist|degraded|polymath|savant
claim_types: derivation|observation
rel_types: point_in|row_of|enables|contains|factored_as|computed_from|path_through|defines|identifies|induced_by|reduces|column_of|satisfies|determines|maps_to|derived_from|motivates|grounded_by
builds_on: HOWL-MATH-14-2026 (processing entropy), HOWL-INFO-12-2026 (reduction to cardinality one) — not cross-referenced; noted for provenance only
+standalone: this doc self-contained
